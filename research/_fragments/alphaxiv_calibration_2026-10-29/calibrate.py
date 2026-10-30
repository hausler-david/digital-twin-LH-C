"""Step-0 calibration of the alphaXiv connector against PDFs held locally (docs/internet_research_protocol.md §5a).

Gates (pre-registered in §5a before any data was seen):
  G1 kind      fullText output is raw text: word overlap with local pdftotext >= 0.95 and a reference list at the end
  G2 numbers   the multiset of digits (whole document) equals local pdftotext; numeric-token differences are listed
  G3 determinism  a repeated identical call returns identical bytes (two fresh calls; the spot check is reported only)
  G4 version   v1 and v2 of 2506.15445 differ and v2 passes G2
  G5 pages     answer_pdf_queries page N matches local page N (digits equal, best word match among all pages)
  G6 capture   the last 30 words of the saved text occur in the last two local pages (exact), or failing that each
               of its last 10 words does (both results are reported)
  G7 coverage  >= 99 % of the verified records (2506.15445v2, 2610.35154v1) have every numeric token of their
               quotation among the delivered numeric tokens; misses are listed and classified by hand

Run from the repository root (manifest paths are relative to it; the saved texts and the PDFs are git-ignored):
  python -I research/_fragments/alphaxiv_calibration_2026-10-29/calibrate.py . \
      research/_fragments/alphaxiv_calibration_2026-10-29/manifest.json
The output holds hashes, counts and numeric tokens only, no delivered text.
"""
from __future__ import annotations

import collections
import glob
import hashlib
import html
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

WORD = re.compile(r"[A-Za-z]{3,}")
NUM = re.compile(r"\d+(?:\.\d+)?")
PAGE = re.compile(r'<page num="(\d+)">(.*?)</page>', re.S)


def pdf_pages(pdf: Path) -> list[str]:
    out = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
    pages = out.split("\f")
    return pages[:-1] if pages and not pages[-1].strip() else pages


def words(t: str) -> collections.Counter:
    return collections.Counter(w.lower() for w in WORD.findall(t))


def digits(t: str) -> collections.Counter:
    return collections.Counter(ch for ch in t if ch.isdigit())


def overlap(a: collections.Counter, b: collections.Counter) -> float:
    """Share of b's tokens also present in a (multiset)."""
    return sum((a & b).values()) / max(1, sum(b.values()))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip()


def record_tokens(root: Path, sid: str) -> list[tuple[str, list[str]]]:
    out = []
    for f in glob.glob(str(root / "parameters" / "**" / "*.yaml"), recursive=True):
        d = yaml.safe_load(open(f))
        if not isinstance(d, dict) or "parameters" not in d:
            continue
        for r in d["parameters"]:
            src = (r.get("provenance") or {}).get("source") or {}
            if src.get("source_id") == sid and src.get("quotation"):
                q = re.sub(r"\[p\.?\s*\d+[^\]]*\]|\bp\.\s*\d+|PDF p\.\s*\d+", " ", src["quotation"])
                out.append((r["parameter_id"], NUM.findall(q)))
    return out


def main() -> int:
    root, manifest = Path(sys.argv[1]), json.load(open(sys.argv[2]))
    report = {}
    for doc in manifest["documents"]:
        key = doc["key"]
        local = pdf_pages(root / doc["pdf"])
        local_all = "\n".join(local)
        full_p = root / doc["full"]
        full = full_p.read_text(encoding="utf-8")
        r = {"pdf_pages": len(local), "full_sha256": sha(full_p), "full_bytes": full_p.stat().st_size}
        # G1
        r["G1_word_overlap"] = round(overlap(words(full), words(local_all)), 4)
        r["G1_reference_list"] = bool(re.search(r"\b(References|REFERENCES|Bibliography)\b", full[-int(len(full) * 0.4):]))
        r["G1_pass"] = r["G1_word_overlap"] >= 0.95 and r["G1_reference_list"]
        # G2
        dl, dc = digits(local_all), digits(full)
        r["G2_digit_diff_local_minus_conn"] = dict(dl - dc)
        r["G2_digit_diff_conn_minus_local"] = dict(dc - dl)
        tl, tc = collections.Counter(NUM.findall(local_all)), collections.Counter(NUM.findall(full))
        r["G2_numtokens_only_local"] = sorted((tl - tc).elements())[:60]
        r["G2_numtokens_only_conn"] = sorted((tc - tl).elements())[:60]
        r["G2_pass"] = dl == dc
        # G3
        if doc.get("repeat"):
            r["G3_pass"] = sha(root / doc["repeat"]) == r["full_sha256"]
        if doc.get("spot_check"):
            r["G3_spot_check_identical"] = sha(root / doc["spot_check"]) == r["full_sha256"]
        # G4 (only on the doc that carries a v1 delivery)
        if doc.get("v1_full"):
            v1 = root / doc["v1_full"]
            r["G4_v1_sha256"] = sha(v1)
            r["G4_v1_differs"] = r["G4_v1_sha256"] != r["full_sha256"]
            r["G4_pass"] = r["G4_v1_differs"] and r["G2_pass"]
        # G5
        g5 = []
        for tf in doc.get("page_tags", []):
            for n, body in PAGE.findall((root / tf).read_text(encoding="utf-8")):
                n, body = int(n), html.unescape(body)
                if n < 1 or n > len(local):
                    g5.append({"page": n, "ok": False, "why": "outside the PDF"})
                    continue
                scores = [overlap(words(body), words(p)) for p in local]
                best = max(range(len(local)), key=lambda i: scores[i]) + 1
                g5.append({"page": n, "best_local_page": best, "word_overlap": round(scores[n - 1], 4),
                           "digits_equal": digits(body) == digits(local[n - 1]), "ok": best == n})
        r["G5"] = g5
        r["G5_pass"] = bool(g5) and all(x["ok"] for x in g5) if doc.get("page_tags") else None
        # G6
        tail = norm(" ".join(full.split()[-30:]))
        last2 = norm(" ".join(local[-2:]))
        r["G6_tail_exact"] = tail in last2
        r["G6_last10_words"] = all(w in last2 for w in tail.split()[-10:])
        r["G6_pass"] = r["G6_tail_exact"] or r["G6_last10_words"]
        # G7
        if doc.get("records_source_id"):
            conn_tokens = set(NUM.findall(full))
            recs = record_tokens(root, doc["records_source_id"])
            misses = [(pid, [t for t in toks if t not in conn_tokens]) for pid, toks in recs]
            misses = [(pid, m) for pid, m in misses if m]
            r["G7_records"] = len(recs)
            r["G7_covered"] = len(recs) - len(misses)
            r["G7_share"] = round((len(recs) - len(misses)) / max(1, len(recs)), 4)
            r["G7_misses"] = misses[:80]
        report[key] = r
    print(json.dumps(report, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
