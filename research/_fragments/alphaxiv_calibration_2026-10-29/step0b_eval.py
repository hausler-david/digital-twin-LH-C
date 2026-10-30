"""Step-0b evaluation (docs/internet_research_protocol.md §5a), revision 2026-10-30.2, committed before any Step-0b call.

  evaluate --manifest M --record R --calls A [--out O]
      The decision, computed without judgement from the call plan of M (labels, tools, exact arguments, files), the
      saver's record R (tools/save_connector_text.py --record: one JSON line per saved result or call without a
      result), the transcript audit A (stdout of tools/scan_connector_text.py transcripts --since <plan start>), the
      saved files (re-hashed and scanned), and the local PDFs and Step-0 files named in M. Prints every call's class,
      the verdicts, findings and stops, the G4' outcome per paper, the NO_SUCH_VERSION template and the decision.
      Exit status: 0 when Step 0b passes, 1 when a stop condition holds, 2 on a usage or input error.
  classify --file F --tool T --id ID [--is-error]
      The class of one saved answer (pages, refusal, text or generic_error), for inspection.

Classes. answer_pdf_queries: "pages" (exactly one well-formed paper block, lhmuc.connector_text.parse_answer),
"refusal" (one line that says "not found" and names the requested id as a token), otherwise "generic_error".
get_paper_content: "refusal" as above; "text" (no page tags, at least 2048 bytes and 50 lines, is_error false);
otherwise "generic_error". A call without a result is a generic error. A generic error is retried once (label_r);
only the retry then counts; a second generic error is a stop. A late result (label_late) must agree with the counted one.

Run from the repository root with python -I. The output holds classes, verdicts, counts, hashes and the one-line
template, and no other delivered text.
"""
from __future__ import annotations

import argparse
import functools
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
from lhmuc import connector_text as ct  # noqa: E402
from scan_connector_text import scan_text  # noqa: E402

HERE = Path(__file__).resolve().parent
HEADING = re.compile(r"\b(References|REFERENCES|Bibliography)\b")
G1_RECALL = 0.95        # share of local words found in the delivery (Step 0: 0.9889 at least)
G1_PRECISION = 0.95     # share of delivered words found in the local text (Step 0: calibration_0b_pre.json)
SAME_PAPER_TEXT = 0.60  # min(recall, precision) of a v1 text against the uploaded vN (Step 0: other version of the
                        # same paper 0.913, unrelated papers 0.498 at most; calibration_0b_pre.json)
MIN_TEXT_BYTES, MIN_TEXT_LINES = 2048, 50
P5_MIN_PAGES = 3


class InputError(Exception):
    """A missing or inconsistent input: exit status 2, no decision."""


@functools.lru_cache(maxsize=None)
def pdf_pages(pdf: str) -> tuple[str, ...]:
    out = subprocess.run(["pdftotext", "-enc", "UTF-8", str(ROOT / pdf), "-"], capture_output=True, text=True,
                         check=True).stdout
    pages = out.split("\f")
    return tuple(pages[:-1] if pages and not pages[-1].strip() else pages)


def g2_reports(docs: list[dict]) -> dict:
    """g2_decompose.py (committed with Step 0) on the delivered vN texts: joins, decimal seams, unexplained tokens."""
    if not docs:
        return {}
    with tempfile.TemporaryDirectory() as d:
        m = Path(d) / "manifest.json"  # paths only, no delivered text
        m.write_text(json.dumps({"documents": docs}), encoding="utf-8")
        out = subprocess.run([sys.executable, "-I", str(HERE / "g2_decompose.py"), str(ROOT), str(m)],
                             capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def text_score(text: str, local_all: str) -> float:
    """Same-paper score of a whole text against a local PDF text: the smaller of recall and precision of words."""
    a, b = ct.words(text), ct.words(local_all)
    return min(ct.overlap(a, b), ct.overlap(b, a))


def vid_of(tool: str, args: dict) -> str:
    if tool == "get_paper_content":
        m = re.fullmatch(r"https://arxiv\.org/abs/(\d{4}\.\d{4,5}v[1-9]\d*)", str(args.get("url", "")))
    else:
        m = re.fullmatch(r"(\d{4}\.\d{4,5}v[1-9]\d*)", str(args.get("paper", "")))
    if not m:
        raise InputError(f"call {args} names no versioned arXiv id")
    return m.group(1)


def classify(tool: str, text: str, vid: str, is_error: bool) -> tuple[str, str]:
    ans = ct.parse_answer(text)
    if ans.kind == "one_line":
        return ("refusal", "") if ct.is_refusal(text, vid) else ("generic_error", "one line without a refusal of " + vid)
    if tool == "answer_pdf_queries":
        if ans.kind == "pages" and not is_error:
            return "pages", ""
        return "generic_error", ans.why or "is_error with pages"
    if ct.ANY_TAG.search(text):
        return "generic_error", "page tags in a full text"
    if is_error or len(text.encode("utf-8")) < MIN_TEXT_BYTES or len(text.split("\n")) < MIN_TEXT_LINES:
        return "generic_error", "not a full text (error flag, or below 2048 bytes or 50 lines)"
    return "text", ""


class Run:
    def __init__(self, manifest: dict, records: list[dict], audit: dict, root: Path = ROOT):
        self.m, self.records, self.audit, self.root = manifest, records, audit, root
        self.plan = {c["label"]: c for c in manifest["calls"]}
        self.stops: list[dict] = []
        self.findings: list[dict] = []
        self.calls: dict[str, dict] = {}
        self.texts: dict[str, str] = {}
        self.cls: dict[str, str] = {}
        self.template: tuple[str, bool] | None = None

    def stop(self, rule: str, msg: str) -> None:
        self.stops.append({"rule": rule, "message": msg})

    def finding(self, rule: str, msg: str) -> None:
        self.findings.append({"rule": rule, "message": msg})

    # ---- inputs -------------------------------------------------------------------------------------------------
    def expected_file(self, label: str) -> str:
        base = label.removesuffix("_r").removesuffix("_late")
        c = self.plan[base]
        return f"references/_local/{c['source_id']}/raw_{label}_{vid_of(c['tool'], c['arguments'])}.txt"

    def check_inputs(self) -> dict[str, dict]:
        by_label: dict[str, dict] = {}
        audit_calls = {c.get("tool_use_id"): c for c in self.audit.get("calls", [])}
        for v in self.audit.get("violations", []):
            if v.get("severity") == "violation":
                self.stop("audit", f"transcript audit violation: {v.get('violation')}")
        for c in audit_calls.values():
            if c.get("flag") or c.get("role") != "lead":
                self.stop("audit", f"inadmissible or subagent connector call {c.get('tool_use_id')}: {c.get('flag')}")
        recorded = set()
        for r in self.records:
            label = r.get("label", "")
            base = label.removesuffix("_r").removesuffix("_late")
            if base not in self.plan:
                self.stop("plan", f"recorded call {label} is not in the call plan")
                continue
            if label in by_label:
                self.stop("plan", f"call {label} recorded twice")
                continue
            p = self.plan[base]
            if r.get("tool") != p["tool"] or r.get("arguments") != p["arguments"] or r.get("source_id") != p["source_id"]:
                self.stop("plan", f"{label}: tool, arguments or source differ from the call plan")
            a = audit_calls.get(r.get("tool_use_id"))
            if a is None or a.get("arguments") != p["arguments"]:
                self.stop("plan", f"{label}: call {r.get('tool_use_id')} is not in the transcript audit as planned")
            recorded.add(r.get("tool_use_id"))
            if r.get("status") == "saved":
                if r.get("mode") != "raw" or r.get("file") != self.expected_file(label):
                    self.stop("plan", f"{label}: saved as {r.get('file')} ({r.get('mode')}), not {self.expected_file(label)}")
                f = self.root / r["file"]
                if not f.is_file():
                    raise InputError(f"{label}: saved file {r['file']} is missing")
                data = f.read_bytes()
                if hashlib.sha256(data).hexdigest() != r.get("sha256"):
                    raise InputError(f"{label}: {r['file']} does not match its recorded SHA-256")
                self.texts[label] = data.decode("utf-8", errors="replace")
            elif r.get("status") != "no_result":
                raise InputError(f"{label}: unknown record status {r.get('status')}")
            by_label[label] = r
        for tid in sorted(set(audit_calls) - recorded, key=str):
            self.stop("plan", f"connector call {tid} ({audit_calls[tid].get('tool')}) is not in the record")
        return by_label

    # ---- classes ------------------------------------------------------------------------------------------------
    def class_of(self, label: str, r: dict) -> tuple[str, str]:
        if r.get("status") == "no_result":
            return "generic_error", "no result"
        p = self.plan[label.removesuffix("_r").removesuffix("_late")]
        return classify(p["tool"], self.texts[label], vid_of(p["tool"], p["arguments"]), bool(r.get("is_error")))

    def effective(self, by_label: dict[str, dict]) -> dict[str, str]:
        """label -> the attempt that counts (the original, or its retry after a generic error)."""
        eff = {}
        for label in self.plan:
            orig = by_label.get(label)
            if orig is None:
                self.stop("plan", f"{label}: planned call not made or not recorded")
                continue
            c, why = self.class_of(label, orig)
            self.calls[label] = {"class": c, "why": why, "tool_use_id": orig.get("tool_use_id"),
                                 "sha256": orig.get("sha256"), "is_error": orig.get("is_error")}
            retry = by_label.get(label + "_r")
            if c != "generic_error":
                if retry is not None:
                    self.stop("plan", f"{label}: retried although its answer was not a generic error")
                eff[label] = label
            elif retry is None:
                self.stop("generic_error", f"{label}: generic error ({why}) not retried")
            else:
                rc, rwhy = self.class_of(label + "_r", retry)
                self.calls[label]["retry"] = {"class": rc, "why": rwhy, "tool_use_id": retry.get("tool_use_id"),
                                              "sha256": retry.get("sha256"), "is_error": retry.get("is_error")}
                if not (retry.get("called_on", "") > orig.get("called_on", "")
                        and retry.get("message_id") != orig.get("message_id")):
                    self.stop("plan", f"{label}: the retry is not in a later message")
                if rc == "generic_error":
                    self.stop("generic_error", f"{label}: second generic error ({rwhy})")
                else:
                    eff[label] = label + "_r"
            if label in eff:
                self.cls[label] = self.class_of(eff[label], by_label[eff[label]])[0]
            late = by_label.get(label + "_late")
            if late is not None:
                lc = self.class_of(label + "_late", late)[0]
                if orig.get("status") != "no_result":
                    self.stop("plan", f"{label}: a late result recorded for a call that had a result")
                elif label not in eff or lc != self.cls[label] or not self.same_answer(label + "_late", eff[label]):
                    self.stop("late_result", f"{label}: the late result ({lc}) disagrees with the counted answer")
        return eff

    def same_answer(self, a: str, b: str) -> bool:
        ta, tb = self.texts.get(a, ""), self.texts.get(b, "")
        pa, pb = ct.parse_answer(ta), ct.parse_answer(tb)
        if pa.kind == "pages" and pb.kind == "pages":
            return pa.paper_id == pb.paper_id and sorted(pa.pages) == sorted(pb.pages)
        return ta == tb

    # ---- helpers ------------------------------------------------------------------------------------------------
    def text(self, label: str, eff: dict[str, str]) -> str:
        return self.texts[eff[label]]

    def vid(self, label: str) -> str:
        p = self.plan[label]
        return vid_of(p["tool"], p["arguments"])

    def is_error(self, label: str, eff: dict[str, str], by_label: dict[str, dict]) -> bool:
        return bool(by_label[eff[label]].get("is_error"))

    def refusal_matches(self, label: str, eff, by_label) -> bool:
        return (self.template is not None and self.cls.get(label) == "refusal"
                and (ct.template_of(self.text(label, eff), self.vid(label)), self.is_error(label, eff, by_label))
                == self.template)

    # ---- rules --------------------------------------------------------------------------------------------------
    def order_rules(self, by_label: dict[str, dict]) -> None:
        a, b = by_label.get("P1a"), by_label.get("P1b")
        if a and b and not (b.get("called_on", "") > a.get("called_on", "") and b.get("message_id") != a.get("message_id")):
            self.stop("plan", "P1b is not in a later message than P1a")
        if b:
            for label in self.plan:
                r = by_label.get(label)
                if label != "P1b" and r and r.get("called_on", "") >= b.get("called_on", ""):
                    self.stop("plan", f"{label} was called after P1b; P1b is the last planned call")
            for label, r in by_label.items():
                if label.endswith("_r") and r.get("called_on", "") <= b.get("called_on", ""):
                    self.stop("plan", f"{label}: retries come after P1b")

    def scan_rule(self) -> None:
        for label, t in sorted(self.texts.items()):
            hits = scan_text(t)["hits"]
            if hits:
                self.stop("scan", f"{label}: {len(hits)} instruction-scan hit(s) (patterns {scan_text('')['patterns_version']})")

    def template_rule(self, eff, by_label) -> None:
        if any(x not in eff for x in ("P1a", "P1b", "P7")):
            return
        p1a, p1b = eff["P1a"], eff["P1b"]
        if self.cls["P1a"] != "refusal" or self.cls["P1b"] != "refusal":
            self.stop("template", f"P1 is not a one-line refusal of 2610.35154v9 ({self.cls['P1a']}, {self.cls['P1b']})")
            return
        if self.texts[p1a] != self.texts[p1b] or self.is_error("P1a", eff, by_label) != self.is_error("P1b", eff, by_label):
            self.stop("template", "the two P1 answers differ")
            return
        self.template = (ct.template_of(self.texts[p1a], self.vid("P1a")), self.is_error("P1a", eff, by_label))
        if not self.refusal_matches("P7", eff, by_label):
            self.stop("template", f"P7 ({self.cls.get('P7')}) does not answer with the P1 template")

    def page_rows(self, ans: ct.Answer, local: tuple[str, ...], full: str | None) -> list[dict]:
        rows = []
        for n in ans.order:
            body = ans.pages[n]
            lp = local[n - 1] if 1 <= n <= len(local) else None
            rows.append({"page": n, "words": len(body.split()),
                         "same": lp is not None and ct.same_page(body, lp),
                         "differs": lp is not None and ct.differs_page(body, lp),
                         "in_full_text": None if full is None else ct.contained(body, full)})
        return rows

    def page_checks(self, label: str, text: str, local: tuple[str, ...], full: str | None = None) -> dict:
        """Verdict of a page-tagged answer against the local pages of another version and, with full, the delivered
        full text of the requested version."""
        vid, ans = self.vid(label), ct.parse_answer(text)
        out = {"paper_id": ans.paper_id, "pages": ans.order}
        if ans.paper_id != vid:
            self.stop("page_id", f"{label}: pages under id {ans.paper_id}, not {vid}")
            return {**out, "verdict": "wrong_id"}
        if ct.stamp_verdict("\n".join(ans.pages.values()), vid) == "other_version":
            self.stop("page_stamp", f"{label}: a page carries the arXiv stamp of another version")
            return {**out, "verdict": "other_stamp"}
        med = ct.same_paper(ans.pages, list(local))
        out["same_paper_median"] = round(med, 4)
        if med < ct.SAME_PAPER_MEDIAN:
            self.stop("page_paper", f"{label}: pages of another paper (median best overlap {med:.3f})")
            return {**out, "verdict": "other_paper"}
        rows = self.page_rows(ans, local, full)
        out["rows"] = rows
        differs = any(r["differs"] for r in rows)
        if full is None:
            return {**out, "verdict": "differs" if differs else "uninformative"}
        if any(r["same"] and not r["in_full_text"] for r in rows):
            self.stop("substitution", f"{label}: a page matches the later version but not the delivered {vid} text")
            return {**out, "verdict": "substitution"}
        if any(not r["in_full_text"] for r in rows):
            self.stop("inconsistent", f"{label}: a page does not occur in the delivered {vid} text")
            return {**out, "verdict": "inconsistent"}
        return {**out, "verdict": "version_specific" if differs else "uninformative"}

    def later_version_rule(self, label: str, local_pdf: str, eff, by_label, v1_full: str | None = None) -> dict:
        c = self.cls.get(label)
        if c is None:
            return {}
        if c == "refusal":
            if self.template is None:
                return {"class": c, "verdict": "not evaluated (no template)"}
            if not self.refusal_matches(label, eff, by_label):
                self.stop("template", f"{label}: a refusal in another form than the P1 template")
                return {"class": c, "verdict": "uncalibrated refusal"}
            return {"class": c, "verdict": "no later version known to the connector"}
        out = {"class": c, **self.page_checks(label, self.text(label, eff), pdf_pages(local_pdf))}
        if out["verdict"] not in ("differs", "uninformative"):
            return out
        if v1_full is not None:
            ans = ct.parse_answer(self.text(label, eff))
            if any(ct.contained(ans.pages[r["page"]], v1_full) and not r["same"] for r in out["rows"]):
                self.stop("relabelled", f"{label}: version-1 content under the {self.vid(label)} label")
                return {**out, "verdict": "relabelled_v1"}
        if out["verdict"] == "uninformative":
            self.stop("later_version", f"{label}: pages labelled {self.vid(label)} that do not differ from the registered "
                                       "version; a later version cannot be told from a relabelled one")
        else:
            self.finding("later_version", f"{label}: pages labelled {self.vid(label)} that differ from the registered "
                                          "version: a later version may exist (only a full-text reading confirms it)")
        return out

    @staticmethod
    def gates(full: str, local: tuple[str, ...], g2: dict) -> dict:
        """G1, G2 and G6 of a delivered later-version text against its uploaded PDF (Step-0b definitions)."""
        local_all = "\n".join(local)
        wl, wc = ct.words(local_all), ct.words(full)
        recall, precision = ct.overlap(wc, wl), ct.overlap(wl, wc)
        heading_local = bool(HEADING.search(local_all[-int(len(local_all) * 0.4):]))
        heading = bool(HEADING.search(full[-int(len(full) * 0.4):]))
        tail = ct.collapse(" ".join(ct.dehyphenate(full).split()[-30:]))
        last2 = ct.collapse(ct.dehyphenate("\n".join(local[-2:])))
        r = {"G1_recall": round(recall, 4), "G1_precision": round(precision, 4), "G1_heading_local": heading_local,
             "G1_heading": heading, "G2_digits_equal": ct.digits(local_all) == ct.digits(full),
             "G2_reported": bool(g2), "G2_decimal_seams": len(g2.get("decimal_seams", [])),
             "G2_unexplained": len(g2.get("unexplained_local", [])) + len(g2.get("unexplained_delivered", [])),
             "G6_tail_in_last_two_pages": tail in last2}
        r["G1_pass"] = recall >= G1_RECALL and precision >= G1_PRECISION and (heading or not heading_local)
        r["G2_pass"] = r["G2_digits_equal"] and r["G2_reported"] and not r["G2_decimal_seams"] and not r["G2_unexplained"]
        r["G6_pass"] = r["G6_tail_in_last_two_pages"]
        return r

    def g4prime(self, spec: dict, eff, by_label, g2: dict) -> dict:
        tag, paper, vn = spec["tag"], spec["paper"], spec["vN"]
        l1, ln, lq = f"G{tag}v1", f"G{tag}{vn}", f"Q{tag}v1"
        local = pdf_pages(spec["local_pdf"])
        local_all = "\n".join(local)
        out = {"paper": paper, "vN": vn, "classes": {k: self.cls.get(k) for k in (l1, ln, lq)}}
        n_stops = len(self.stops)
        c1, cn, cq = self.cls.get(l1), self.cls.get(ln), self.cls.get(lq)
        t1 = self.text(l1, eff) if c1 == "text" else None
        tn = self.text(ln, eff) if cn == "text" else None
        local_stamp = ct.stamp_verdict(local_all, paper + vn)
        out["local_stamp"] = local_stamp
        if tn is not None:
            sv = ct.stamp_verdict(tn, paper + vn)
            out["vN_stamp"] = sv
            if sv == "other_version" or (local_stamp == "matches" and sv != "matches"):
                self.stop("stamp", f"{ln}: the delivered text's arXiv stamp is {sv}, the uploaded {paper}{vn} has one")
            out["vN_gates"] = self.gates(tn, local, g2.get(f"G4p_{paper}{vn}", {}))
            for gate in ("G1_pass", "G2_pass", "G6_pass"):
                if not out["vN_gates"][gate]:
                    self.stop("gates", f"{ln}: {gate.removesuffix('_pass')} fails against the uploaded {paper}{vn}")
        if t1 is not None:
            sv1 = ct.stamp_verdict(t1, paper + "v1")
            rec1 = text_score(t1, local_all)
            out.update(v1_stamp=sv1, v1_score_vs_local_vN=round(rec1, 4))
            if sv1 == "other_version":
                self.stop("stamp", f"{l1}: the delivered text carries the arXiv stamp of another version")
            if rec1 < SAME_PAPER_TEXT:
                self.stop("v1_text", f"{l1}: not a text of this paper (score {rec1:.3f} against the uploaded {vn})")
            if sv1 == "absent" and ct.digits(t1) == ct.digits(local_all):
                self.stop("substitution", f"{l1}: digits equal those of the uploaded {vn} and no v1 stamp")
        if t1 is not None and tn is not None and (t1 == tn or ct.collapse(t1) == ct.collapse(tn)):
            self.stop("substitution", f"{paper}: the v1 and {vn} deliveries are identical")
        if cq == "pages":
            out["v1_pages"] = self.page_checks(lq, self.text(lq, eff), local, t1)
        elif cq == "refusal":
            if self.refusal_matches(lq, eff, by_label):
                self.finding("page_tool", f"{lq}: the page tool answers {paper}v1 with the NO_SUCH_VERSION template")
                out["v1_pages"] = {"verdict": "template"}
            else:
                self.stop("template", f"{lq}: a refusal in another form than the P1 template")
                out["v1_pages"] = {"verdict": "uncalibrated refusal"}
        page_verdict = (out.get("v1_pages") or {}).get("verdict")
        if len(self.stops) > n_stops:
            out["outcome"] = "stopped"
        elif t1 is not None and tn is not None:
            out["outcome"] = "passed" if page_verdict == "version_specific" else "uninformative"
        elif tn is not None:
            out["outcome"] = f"one full-text version held ({vn}); page half {page_verdict}"
        elif t1 is not None:
            out["outcome"] = f"one full-text version held (v1, checked against the uploaded {vn}); page half {page_verdict}"
        else:
            out["outcome"] = f"no full-text version held; page half {page_verdict}"
        return out

    def p5(self, eff) -> dict:
        if self.cls.get("P5") != "pages":
            self.stop("P5", f"P5 is {self.cls.get('P5')}, not the 2506.15445v2 pages served in Step 0")
            return {"class": self.cls.get("P5")}
        ans = ct.parse_answer(self.text("P5", eff))
        rows = self.page_rows(ans, pdf_pages(self.m["local"]["2506.15445v2"]), None)
        out = {"class": "pages", "paper_id": ans.paper_id, "pages": ans.order, "rows": rows}
        if (ans.paper_id != "2506.15445v2" or len(rows) < P5_MIN_PAGES or not all(r["same"] for r in rows)
                or ct.stamp_verdict("\n".join(ans.pages.values()), "2506.15445v2") == "other_version"):
            self.stop("P5", "P5 does not reproduce the local 2506.15445v2 pages (id, three pages or more, each the same)")
            return {**out, "verdict": "fail"}
        self.compare_step0("P5", eff, self.m["step0"]["2506.15445v2_pages"])
        return {**out, "verdict": "same"}

    def compare_step0(self, label: str, eff, step0_file: str) -> None:
        now = ct.parse_answer(self.text(label, eff))
        then = ct.parse_answer((self.root / step0_file).read_text(encoding="utf-8"))
        if sorted(now.pages) != sorted(then.pages):
            self.finding("reproducibility", f"{label}: page set {sorted(now.pages)} differs from Step 0 {sorted(then.pages)}")
        changed = [n for n in set(now.pages) & set(then.pages) if ct.collapse(now.pages[n]) != ct.collapse(then.pages[n])]
        if changed:
            self.finding("reproducibility", f"{label}: pages {sorted(changed)} differ in text from the Step-0 answer")

    def run(self) -> dict:
        by_label = self.check_inputs()
        self.order_rules(by_label)
        eff = self.effective(by_label)
        self.scan_rule()
        self.template_rule(eff, by_label)
        s0 = self.m["step0"]
        v1_full = (self.root / s0["2506.15445v1_full"]).read_text(encoding="utf-8")
        probes = {"P2": self.later_version_rule("P2", self.m["local"]["1905.05564v2"], eff, by_label),
                  "P3": self.later_version_rule("P3", self.m["local"]["2506.15445v2"], eff, by_label, v1_full=v1_full)}
        c4 = self.cls.get("P4")  # an existing intermediate version
        if c4 == "refusal":
            if self.refusal_matches("P4", eff, by_label):
                self.finding("P4", "the page tool answers the existing 2203.06258v2 with the NO_SUCH_VERSION template: "
                                   "a template answer means 'not known to the connector', not 'does not exist'")
                probes["P4"] = {"class": c4, "verdict": "template"}
            else:
                self.stop("template", "P4: a refusal in another form than the P1 template")
                probes["P4"] = {"class": c4, "verdict": "uncalibrated refusal"}
        elif c4 == "pages":
            probes["P4"] = {"class": c4, **self.page_checks("P4", self.text("P4", eff),
                                                            pdf_pages(self.m["local"]["2203.06258v3"]))}
            if probes["P4"]["verdict"] == "uninformative":
                self.finding("P4", "P4 pages do not differ from the uploaded v3: P4 shows no version-specific label")
        if "P5" in self.cls:
            probes["P5"] = self.p5(eff)
        if self.cls.get("P6") == "pages":  # same-session v1 control: Step-0 S2/S3 predict version_specific
            probes["P6"] = {"class": "pages", **self.page_checks("P6", self.text("P6", eff),
                                                                 pdf_pages(self.m["local"]["2506.15445v2"]), v1_full)}
            if probes["P6"]["verdict"] == "uninformative":
                self.stop("P6", "P6 is uninformative although Step 0 predicts version-specific pages")
            self.compare_step0("P6", eff, s0["2506.15445v1_pages"])
        elif "P6" in self.cls:
            self.stop("P6", f"P6 is {self.cls['P6']}, not the 2506.15445v1 pages served in Step 0")
        g4_docs = [{"key": f"G4p_{s['paper']}{s['vN']}", "pdf": s["local_pdf"],
                    "full": by_label[eff[f"G{s['tag']}{s['vN']}"]]["file"]}
                   for s in self.m["g4prime"] if self.cls.get(f"G{s['tag']}{s['vN']}") == "text"]
        g2 = g2_reports(g4_docs)
        g4 = {s["paper"]: self.g4prime(s, eff, by_label, g2) for s in self.m["g4prime"]}
        return {"revision": self.m.get("revision"), "decision": "stop" if self.stops else "pass",
                "stops": self.stops, "findings": self.findings,
                "template": None if self.template is None else self.template[0],
                "template_is_error": None if self.template is None else self.template[1],
                "calls": self.calls, "probes": probes, "g4prime": g4,
                "g4prime_passed": sum(v.get("outcome") == "passed" for v in g4.values())}


def load_record(path: Path) -> list[dict]:
    if not path.is_file():
        raise InputError(f"record {path} is missing")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("evaluate", help="the Step-0b decision (exit 0 pass, 1 stop, 2 input error)")
    e.add_argument("--manifest", type=Path, required=True)
    e.add_argument("--record", type=Path, required=True)
    e.add_argument("--calls", type=Path, required=True, help="stdout of scan_connector_text.py transcripts")
    e.add_argument("--out", type=Path)
    c = sub.add_parser("classify", help="the class of one saved answer")
    c.add_argument("--file", type=Path, required=True)
    c.add_argument("--tool", required=True, choices=["answer_pdf_queries", "get_paper_content"])
    c.add_argument("--id", required=True)
    c.add_argument("--is-error", action="store_true")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "classify":
            klass, why = classify(a.tool, a.file.read_text(encoding="utf-8"), a.id, a.is_error)
            print(json.dumps({"class": klass, "why": why}))
            return 0
        manifest = json.loads(a.manifest.read_text(encoding="utf-8"))
        audit = json.loads(a.calls.read_text(encoding="utf-8"))
        out = Run(manifest, load_record(a.record), audit).run()
    except (InputError, OSError, KeyError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"input_error": str(exc)}), file=sys.stderr)
        return 2
    text = json.dumps(out, ensure_ascii=False, indent=1)
    if a.out:
        a.out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if out["decision"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
