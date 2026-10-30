"""Step-0b evaluation (docs/internet_research_protocol.md §5a, pre-registered 2026-10-30; this script is committed
before the Step-0b calls). It reads only saved connector answers under references/_local/<source_id>/ and local PDFs.

  pages-same   --pdf P --pages X.xml --id ID --expect-pages N...
                                              P5: the answer names paper ID, returns exactly the expected page set, and
                                              every page is "the same" as the local page with that number (S1)
  pages-differ --pdf P --pages X.xml --id ID --role R [--full F]
                                              the answer names paper ID and has pages; the verdict compares each page
                                              with the local page of that number (another version of the paper):
                                                differs        at least one page is not "the same"
                                                uninformative  every page is "the same" (the versions may agree there)
                                              With --full F (the delivered full text of the requested version), each
                                              page must also occur in F (the S2 test: substring after whitespace
                                              collapse, 46 of 46 same-version pages in Step 0):
                                                version_specific  every page occurs in F and at least one differs
                                                uninformative     every page occurs in F and is "the same"
                                                substitution      a page is "the same" as the local page but not in F
                                                inconsistent      a page is neither "the same" nor in F
                                              The role fixes which verdicts pass (pre-registered, §5a):
                                                probe-negative  P2, P3          differs
                                                known-positive  P4              differs, uninformative
                                                g4-v1           G4' v1 halves   version_specific, uninformative
                                                                                (requires --full)

"The same" is the S1 criterion: equal digit multiset and best word match on the same page number. Calibrated before the
Step-0b calls on the Step-0 files: all 45 same-version pages meet it (DIS2026 7, Kaya 8, MR7 15, μLHC v2 15; word
overlap down to 0.857, so overlap alone does not decide). Of the 16 μLHC v1 pages compared with the local v2, only
page 1 (the title page) meets it. Exact text equality is not used: the connector's text layer orders and splits tokens
differently from pdftotext even within one version.
  stamps       --full F --id ID               a full text: every arXiv stamp of the same paper ("arXiv:<id>v<n>") names
                                              the requested version (verdict matches, or absent when the text layer has
                                              none; other_version fails). Stamps of other papers (citations) are ignored.
  full-pair    --v1 F1 --vn FN --id-v1 ID1 --id-vn IDN
                                              a G4' pair: both texts pass stamps and they are not byte-identical (a
                                              byte-identical pair is a silent substitution)
  template     --ids ID... --answers A.txt... --is-error B...
                                              P1-P3: no answer has pages, every answer names its requested id, and with
                                              that id replaced by {id} all answers are the same bytes with the same
                                              is_error flag (the NO_SUCH_VERSION template); prints it

Run from the repository root with python -I. Output: JSON with counts and verdicts only, no delivered text except the
one-line template.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import html
import json
import re
import subprocess
import sys
from pathlib import Path

WORD = re.compile(r"[A-Za-z]{3,}")
PAGE = re.compile(r'<page num="(\d+)">(.*?)</page>', re.S)
PAPER = re.compile(r'<paper id="([^"]+)">')
STAMP = re.compile(r"arXiv:\s*(\d{4}\.\d{4,5})(v[1-9]\d*)")
VERSIONED = re.compile(r"(\d{4}\.\d{4,5})(v[1-9]\d*)")


def words(t):
    return collections.Counter(w.lower() for w in WORD.findall(t))


def digits(t):
    return collections.Counter(c for c in t if c.isdigit())


def overlap(a, b):
    return sum((a & b).values()) / max(1, sum(b.values()))


def norm(t):
    return re.sub(r"\s+", " ", t).strip()


ROLES = {"probe-negative": {"differs"}, "known-positive": {"differs", "uninformative"},
         "g4-v1": {"version_specific", "uninformative"}}


def pdf_pages(pdf: Path) -> list[str]:
    out = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
    pages = out.split("\f")
    return pages[:-1] if pages and not pages[-1].strip() else pages


def tagged(path: Path) -> tuple[str | None, dict[int, str]]:
    t = path.read_text(encoding="utf-8")
    ids = PAPER.findall(t)
    return (ids[0] if ids else None), {int(n): html.unescape(b) for n, b in PAGE.findall(t)}


def _compare(local: list[str], pages: dict[int, str]) -> list[dict]:
    """Per returned page: best word match among the local pages, digit equality with the local page of that number,
    and whether it is "the same" page (both)."""
    rows = []
    for n, body in sorted(pages.items()):
        scores = [overlap(words(body), words(p)) for p in local]
        best = max(range(len(local)), key=lambda i: scores[i]) + 1
        eq = 1 <= n <= len(local) and digits(body) == digits(local[n - 1])
        rows.append({"page": n, "best_local_page": best, "digits_equal": eq, "same": eq and best == n})
    return rows


def pages_same(pdf: Path, pages_file: Path, paper_id: str, expect_pages: list[int]) -> dict:
    paper, pages = tagged(pages_file)
    rows = _compare(pdf_pages(pdf), pages)
    ok = paper == paper_id and sorted(pages) == sorted(expect_pages) and bool(rows) and all(r["same"] for r in rows)
    return {"paper_id": paper, "expected_id": paper_id, "pages": sorted(pages), "expected_pages": sorted(expect_pages),
            "rows": rows, "pass": ok}


def pages_differ(pdf: Path, pages_file: Path, paper_id: str, role: str, full: Path | None = None) -> dict:
    if (role == "g4-v1") != (full is not None):
        raise SystemExit("--full is required with --role g4-v1 and not allowed otherwise")
    paper, pages = tagged(pages_file)
    rows = _compare(pdf_pages(pdf), pages)
    if full is not None:
        nf = norm(full.read_text(encoding="utf-8"))
        for r in rows:
            r["in_full_text"] = norm(pages[r["page"]]) in nf
    differing = sum(not r["same"] for r in rows)
    if paper != paper_id:
        verdict = "wrong_id"
    elif not rows:
        verdict = "no_pages"
    elif full is None:
        verdict = "differs" if differing else "uninformative"
    elif any(r["same"] and not r["in_full_text"] for r in rows):
        verdict = "substitution"
    elif any(not r["in_full_text"] for r in rows):
        verdict = "inconsistent"
    else:
        verdict = "version_specific" if differing else "uninformative"
    return {"paper_id": paper, "expected_id": paper_id, "role": role, "pages": len(rows), "pages_differing": differing,
            "rows": rows, "verdict": verdict, "pass": verdict in ROLES[role]}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stamps(full: Path, paper_id: str) -> dict:
    m = VERSIONED.fullmatch(paper_id)
    if not m:
        raise SystemExit(f"--id must be a versioned arXiv id, got {paper_id!r}")
    base, version = m.groups()
    found = [b + v for b, v in STAMP.findall(full.read_text(encoding="utf-8")) if b == base]
    verdict = "absent" if not found else "matches" if all(f == paper_id for f in found) else "other_version"
    return {"file": str(full), "sha256": sha256(full), "expected_id": paper_id, "stamps": found, "verdict": verdict,
            "pass": verdict != "other_version"}


def full_pair(v1: Path, vn: Path, id_v1: str, id_vn: str) -> dict:
    a, b = stamps(v1, id_v1), stamps(vn, id_vn)
    identical = a["sha256"] == b["sha256"]
    return {"v1": a, "vn": b, "byte_identical": identical, "pass": a["pass"] and b["pass"] and not identical}


def template(ids: list[str], answers: list[Path], is_error: list[bool]) -> dict:
    forms = []
    for i, a, e in zip(ids, answers, is_error):
        raw = a.read_bytes()
        forms.append({"id": i, "is_error": e, "has_pages": bool(PAGE.search(raw.decode("utf-8", "replace"))),
                      "names_id": i.encode() in raw, "template": raw.replace(i.encode(), b"{id}")})
    same = (len({(f["template"], f["is_error"]) for f in forms}) == 1 and not any(f["has_pages"] for f in forms)
            and all(f["names_id"] for f in forms))
    return {"answers": [{k: v for k, v in f.items() if k != "template"} for f in forms],
            "template": forms[0]["template"].decode("utf-8", "replace") if same else None,
            "is_error": forms[0]["is_error"] if same else None, "pass": same}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("pages-same")
    s.add_argument("--pdf", type=Path, required=True)
    s.add_argument("--pages", type=Path, required=True)
    s.add_argument("--id", required=True)
    s.add_argument("--expect-pages", type=int, nargs="+", required=True)
    d = sub.add_parser("pages-differ")
    d.add_argument("--pdf", type=Path, required=True)
    d.add_argument("--pages", type=Path, required=True)
    d.add_argument("--id", required=True)
    d.add_argument("--role", required=True, choices=sorted(ROLES))
    d.add_argument("--full", type=Path, help="the delivered full text of the requested version (role g4-v1)")
    s2 = sub.add_parser("stamps")
    s2.add_argument("--full", type=Path, required=True)
    s2.add_argument("--id", required=True)
    f = sub.add_parser("full-pair")
    f.add_argument("--v1", type=Path, required=True)
    f.add_argument("--vn", type=Path, required=True)
    f.add_argument("--id-v1", required=True)
    f.add_argument("--id-vn", required=True)
    t = sub.add_parser("template")
    t.add_argument("--ids", nargs="+", required=True)
    t.add_argument("--answers", type=Path, nargs="+", required=True)
    t.add_argument("--is-error", nargs="+", required=True, choices=["true", "false"],
                   help="the is_error flag of each answer, from the saver's later_version_probe object")
    a = ap.parse_args(argv)
    if a.cmd == "pages-same":
        out = pages_same(a.pdf, a.pages, a.id, a.expect_pages)
    elif a.cmd == "pages-differ":
        out = pages_differ(a.pdf, a.pages, a.id, a.role, a.full)
    elif a.cmd == "stamps":
        out = stamps(a.full, a.id)
    elif a.cmd == "full-pair":
        out = full_pair(a.v1, a.vn, a.id_v1, a.id_vn)
    else:
        if not len(a.ids) == len(a.answers) == len(a.is_error):
            raise SystemExit("--ids, --answers and --is-error must pair up")
        out = template(a.ids, a.answers, [x == "true" for x in a.is_error])
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0 if out["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
