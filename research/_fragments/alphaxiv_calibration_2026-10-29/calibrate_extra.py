"""Step-0 supplementary checks on the page-tagged responses for 2506.15445 (docs/internet_research_protocol.md §5a).

These are NOT the pre-registered gates. They are added after G4/G7 could not be run as written, because
get_paper_content refuses 2506.15445v2 ("Paper version not found") while answer_pdf_queries delivers v2 pages.
  S1  answer_pdf_queries v2 pages vs local v2 PDF pages (best word match and equal digit multiset per page)
  S2  answer_pdf_queries v1 pages vs the get_paper_content v1 full text (each page a substring after whitespace collapse)
  S3  v1 and v2 page-tagged pages with the same number differ
  S4  verified records of SRC_ARXIV_2506_15445 (read from v2): numeric tokens of each quotation present on the cited
      page (or the next one) of the delivered v2 pages; records citing undelivered pages are counted separately
Run from the repository root (all paths relative to it):
  python -I research/_fragments/alphaxiv_calibration_2026-10-29/calibrate_extra.py . \
      references/_local/arXiv-2506.15445v2.pdf \
      references/_local/SRC_ARXIV_2506_15445/calibration_get_paper_content_v1.txt \
      references/_local/SRC_ARXIV_2506_15445/calibration_pages_v1.xml \
      references/_local/SRC_ARXIV_2506_15445/calibration_pages_v2.xml
"""
import collections, glob, html, json, re, subprocess, sys
from pathlib import Path
import yaml

WORD = re.compile(r"[A-Za-z]{3,}")
NUM = re.compile(r"\d+(?:\.\d+)?")
PAGE = re.compile(r'<page num="(\d+)">(.*?)</page>', re.S)
PAPER = re.compile(r'<paper id="([^"]+)">')

def words(t): return collections.Counter(w.lower() for w in WORD.findall(t))
def digits(t): return collections.Counter(c for c in t if c.isdigit())
def overlap(a, b): return sum((a & b).values()) / max(1, sum(b.values()))
def norm(t): return re.sub(r"\s+", " ", t).strip()

def pdf_pages(pdf):
    out = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
    pages = out.split("\f")
    return pages[:-1] if pages and not pages[-1].strip() else pages

def tagged(p):
    t = Path(p).read_text(encoding="utf-8")
    return PAPER.findall(t)[0], {int(n): html.unescape(b) for n, b in PAGE.findall(t)}

root, pdf, v1_full, v1_xml, v2_xml = sys.argv[1:6]
local = pdf_pages(Path(root) / pdf)
full1 = Path(v1_full).read_text(encoding="utf-8")
id1, p1 = tagged(v1_xml)
id2, p2 = tagged(v2_xml)
out = {"local_v2_pdf_pages": len(local), "v1_paper_id": id1, "v2_paper_id": id2,
       "v1_pages": sorted(p1), "v2_pages": sorted(p2)}
s1 = []
for n, body in sorted(p2.items()):
    scores = [overlap(words(body), words(p)) for p in local]
    best = max(range(len(local)), key=lambda i: scores[i]) + 1
    s1.append({"page": n, "best_local_page": best, "word_overlap": round(scores[n - 1], 4),
               "digits_equal": digits(body) == digits(local[n - 1])})
out["S1"] = s1
out["S1_pass"] = all(x["best_local_page"] == x["page"] and x["digits_equal"] for x in s1)
nf = norm(full1)
out["S2"] = [{"page": n, "substring_of_v1_full_text": norm(b) in nf} for n, b in sorted(p1.items())]
out["S2_pass"] = all(x["substring_of_v1_full_text"] for x in out["S2"])
out["S3"] = [{"page": n, "v1_equals_v2": norm(p1[n]) == norm(p2[n]), "digits_equal": digits(p1[n]) == digits(p2[n])}
             for n in sorted(set(p1) & set(p2))]
# S4
recs = []
for f in glob.glob(str(Path(root) / "parameters" / "**" / "*.yaml"), recursive=True):
    d = yaml.safe_load(open(f))
    if not isinstance(d, dict) or "parameters" not in d:
        continue
    for r in d["parameters"]:
        src = (r.get("provenance") or {}).get("source") or {}
        if src.get("source_id") == "SRC_ARXIV_2506_15445" and src.get("quotation"):
            q = re.sub(r"\[p\.?\s*\d+[^\]]*\]|\bp\.\s*\d+|PDF p\.\s*\d+", " ", src["quotation"])
            recs.append((r["parameter_id"], src.get("page"), NUM.findall(q)))
on, off, cov, miss = 0, 0, 0, []
pages_cited = collections.Counter()
for pid, page, toks in recs:
    pages_cited[str(page)] += 1
    if not isinstance(page, int) or page not in p2:
        off += 1
        continue
    on += 1
    text = p2[page] + "\n" + p2.get(page + 1, "")
    have = set(NUM.findall(text))
    m = [t for t in toks if t not in have]
    if m:
        miss.append((pid, page, m))
    else:
        cov += 1
out["S4_records"] = len(recs)
out["S4_pages_cited"] = dict(sorted(pages_cited.items(), key=lambda kv: (len(kv[0]), kv[0])))
out["S4_on_delivered_pages"] = on
out["S4_on_undelivered_pages"] = off
out["S4_covered"] = cov
out["S4_misses"] = miss
print(json.dumps(out, indent=1, ensure_ascii=False))
