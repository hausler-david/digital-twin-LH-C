"""Step-0b pre-calibration (docs/internet_research_protocol.md §5a, revision 2026-10-30.3): every threshold and claim the
Step-0b rules rest on, recomputed from the saved Step-0 files and the local PDFs before any Step-0b call. No connector
call. Output: counts, overlaps and verdicts only (research/_fragments/alphaxiv_calibration_2026-10-29/calibration_0b_pre.json).

Run from the repository root: python -I research/_fragments/alphaxiv_calibration_2026-10-29/pre_0b.py > \
    research/_fragments/alphaxiv_calibration_2026-10-29/calibration_0b_pre.json
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
from lhmuc import connector_text as ct  # noqa: E402
from scan_connector_text import scan_text  # noqa: E402

spec = importlib.util.spec_from_file_location("step0b_eval", HERE / "step0b_eval.py")
ev = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ev)

L = "references/_local"
DIS_PDF = "references/primary/arXiv-2610.35154v1_Piotrzkowski_LHmuC_DIS2026.pdf"
SAME = {  # Step-0 page-tagged answer, full text of the same version, local PDF of the same version
    "DIS2026 2610.35154v1": (f"{L}/SRC_ARXIV_2610_35154/calibration_pages_v1.xml",
                             f"{L}/SRC_ARXIV_2610_35154/calibration_get_paper_content_v1.txt", DIS_PDF),
    "Kaya 1905.05564v2": (f"{L}/SRC_ARXIV_1905_05564/calibration_pages_v2.xml",
                          f"{L}/SRC_ARXIV_1905_05564/calibration_get_paper_content_v2.txt", f"{L}/arXiv-1905.05564v2.pdf"),
    "MR7 2510.27437v1": (f"{L}/SRC_ARXIV_2510_27437/calibration_pages_v1.xml",
                         f"{L}/SRC_ARXIV_2510_27437/calibration_get_paper_content_v1.txt", f"{L}/arXiv-2510.27437v1.pdf"),
}
MU_V1_PAGES = f"{L}/SRC_ARXIV_2506_15445/calibration_pages_v1.xml"
MU_V2_PAGES = f"{L}/SRC_ARXIV_2506_15445/calibration_pages_v2.xml"
MU_V1_FULL = f"{L}/SRC_ARXIV_2506_15445/calibration_get_paper_content_v1.txt"
MU_V2_PDF = f"{L}/arXiv-2506.15445v2.pdf"
VN = {"2203.06258v3": f"{L}/arXiv-2203.06258v3.pdf", "2201.06664v2": f"{L}/arXiv-2201.06664v2.pdf",
      "2101.10476v2": f"{L}/arXiv-2101.10476v2.pdf"}


def read(p: str) -> str:
    return (ROOT / p).read_text(encoding="utf-8")


def answer(p: str) -> ct.Answer:
    a = ct.parse_answer(read(p))
    assert a.kind == "pages", (p, a.why)
    return a


def rows(a: ct.Answer, local: tuple[str, ...], full: str | None = None) -> list[dict]:
    out = []
    for n in a.order:
        lp = local[n - 1] if 1 <= n <= len(local) else ""
        out.append({"page": n, "overlap": round(ct.overlap(ct.words(a.pages[n]), ct.words(lp)), 4),
                    "same": ct.same_page(a.pages[n], lp), "differs": ct.differs_page(a.pages[n], local, n),
                    "in_full_text": None if full is None else ct.contained(a.pages[n], full)})
    return out


def sha(p: str) -> str:
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def main() -> int:
    out: dict = {"thresholds": {"SAME_PAGE_OVERLAP": ct.SAME_PAGE_OVERLAP, "SAME_PAPER_MEDIAN": ct.SAME_PAPER_MEDIAN,
                                "SAME_PAPER_CHUNKS": ct.SAME_PAPER_CHUNKS, "MIN_PAGE_WORDS": ct.MIN_PAGE_WORDS,
                                "CHUNK_WORDS": ct.CHUNK_WORDS, "G1_RECALL": ev.G1_RECALL,
                                "G1_PRECISION": ev.G1_PRECISION}}
    # 1-4: same-version pages (strict parse, S1', S2, differs) and the Step-0 gates under the Step-0b definitions
    same_version, gates = {}, {}
    g2 = json.loads((HERE / "g2_decompose.json").read_text(encoding="utf-8"))
    g2_key = {"DIS2026 2610.35154v1": "DIS2026_2610.35154v1", "Kaya 1905.05564v2": "Kaya_1905.05564v2",
              "MR7 2510.27437v1": "MR7_2510.27437v1"}
    for k, (pages, full, pdf) in SAME.items():
        a, f, local = answer(pages), read(full), ev.pdf_pages(pdf)
        r = rows(a, local, f)
        same_version[k] = {"pages": len(r), "same": sum(x["same"] for x in r), "differs": sum(x["differs"] for x in r),
                           "in_full_text": sum(x["in_full_text"] for x in r), "min_overlap": min(x["overlap"] for x in r),
                           "min_words": min(len(a.pages[n].split()) for n in a.order),
                           "same_paper_median": round(ct.same_paper(a.pages, list(local)), 4),
                           "full_text_stamp": ct.stamp_verdict(f, k.split()[1]),
                           "page_stamp": ct.stamp_verdict("\n".join(a.pages.values()), k.split()[1])}
        gates[k] = ev.Run.gates(f, local, g2[g2_key[k]])
    mu2, local2 = answer(MU_V2_PAGES), ev.pdf_pages(MU_V2_PDF)
    r2 = rows(mu2, local2)
    same_version["muLHC 2506.15445v2 (pages only)"] = {"pages": len(r2), "same": sum(x["same"] for x in r2),
                                                       "differs": sum(x["differs"] for x in r2),
                                                       "min_overlap": min(x["overlap"] for x in r2),
                                                       "min_words": min(len(mu2.pages[n].split()) for n in mu2.order),
                                                       "same_paper_median": round(ct.same_paper(mu2.pages, local2), 4)}
    out["same_version_pages"] = same_version
    out["totals"] = {"pages_same_version_S1prime": sum(v["pages"] for v in same_version.values()),
                     "same": sum(v["same"] for v in same_version.values()),
                     "differs": sum(v["differs"] for v in same_version.values()),
                     "S2_pages": sum(v.get("in_full_text", 0) for k, v in same_version.items() if "pages only" not in k)}
    out["step0_gates_under_step0b_definitions"] = gates
    # 5: the muLHC v1 pages against the local v2 and the v1 full text: the P6 prediction and S2 on v1
    mu1, f1 = answer(MU_V1_PAGES), read(MU_V1_FULL)
    r1 = rows(mu1, local2, f1)
    out["muLHC_v1_pages_vs_local_v2"] = {
        "pages": len(r1), "same": sum(x["same"] for x in r1), "differs": sum(x["differs"] for x in r1),
        "in_v1_full_text": sum(x["in_full_text"] for x in r1),
        "same_paper_median": round(ct.same_paper(mu1.pages, local2), 4),
        "min_words": min(len(mu1.pages[n].split()) for n in mu1.order),
        "P6_predicted_verdict": ("version_specific" if all(x["in_full_text"] for x in r1) and any(x["differs"] for x in r1)
                                 and not any(x["same"] and not x["in_full_text"] for x in r1) else "not version_specific")}
    out["muLHC_v2_pages_in_v1_full_text"] = sum(ct.contained(b, f1) for b in mu2.pages.values())
    out["S2_total"] = {"same_version_pages": out["totals"]["S2_pages"] + out["muLHC_v1_pages_vs_local_v2"]["in_v1_full_text"],
                       "of": sum(v["pages"] for k, v in same_version.items() if "pages only" not in k) + len(r1)}
    # 6: same paper or not: the median page window share and the whole-text chunk score, against every local PDF of
    # another paper (the three uploaded later versions included)
    page_sets = {"DIS2026": SAME["DIS2026 2610.35154v1"][0], "Kaya": SAME["Kaya 1905.05564v2"][0],
                 "MR7": SAME["MR7 2510.27437v1"][0], "muLHC v1": MU_V1_PAGES, "muLHC v2": MU_V2_PAGES}
    texts = {"DIS2026": SAME["DIS2026 2610.35154v1"][1], "Kaya": SAME["Kaya 1905.05564v2"][1],
             "MR7": SAME["MR7 2510.27437v1"][1], "muLHC v1": MU_V1_FULL}
    locals_ = {"DIS2026": DIS_PDF, "Kaya": f"{L}/arXiv-1905.05564v2.pdf", "MR7": f"{L}/arXiv-2510.27437v1.pdf",
               "muLHC v2": MU_V2_PDF, **{k: v for k, v in VN.items()}}
    paper_of = {"DIS2026": "DIS2026", "Kaya": "Kaya", "MR7": "MR7", "muLHC v1": "muLHC", "muLHC v2": "muLHC",
                "muLHC v2 local": "muLHC"}
    unrelated_pages, unrelated_texts = {}, {}
    for k, pf in page_sets.items():
        for lk, pdf in locals_.items():
            if paper_of.get(k) == paper_of.get(lk, lk) or (k.startswith("muLHC") and lk == "muLHC v2"):
                continue
            s = ct.same_paper(answer(pf).pages, ev.pdf_pages(pdf))
            unrelated_pages[f"{k} pages vs local {lk}"] = None if s is None else round(s, 4)
    for k, tf in texts.items():
        for lk, pdf in locals_.items():
            if paper_of.get(k) == paper_of.get(lk, lk) or (k.startswith("muLHC") and lk == "muLHC v2"):
                continue
            unrelated_texts[f"{k} text vs local {lk}"] = round(ct.chunk_score(read(tf), ev.pdf_pages(pdf)), 4)
    out["same_paper_page_median"] = {
        "same version (minimum over DIS2026, Kaya, MR7, muLHC v2)": min(
            v["same_paper_median"] for v in same_version.values()),
        "muLHC v1 pages vs local v2 (other version)": out["muLHC_v1_pages_vs_local_v2"]["same_paper_median"],
        "unrelated maximum": max(v for v in unrelated_pages.values() if v is not None),
        "unrelated": unrelated_pages}
    out["whole_text_chunk_score"] = {
        "muLHC v1 text vs local v2 (other version)": round(ct.chunk_score(read(MU_V1_FULL), local2), 4),
        "same version minimum": min(round(ct.chunk_score(read(f), ev.pdf_pages(pdf)), 4) for _, f, pdf in SAME.values()),
        "unrelated maximum": max(unrelated_texts.values()), "unrelated": unrelated_texts}
    # 7: the uploaded later versions of the G4' papers, before any delivery
    vn = {}
    for vid, pdf in VN.items():
        local = ev.pdf_pages(pdf)
        alltext = "\n".join(local)
        selfg = ev.Run.gates(alltext, local, {"decimal_seams": [], "unexplained_local": [], "unexplained_delivered": []})
        vn[vid] = {"pages": len(local), "astral_characters": sum(ord(c) > 0xFFFF for c in alltext),
                   "heading_in_last_40pct": selfg["G1_heading_local"], "local_stamp": ct.stamp_verdict(alltext, vid),
                   "self_test_G1_G6": selfg["G1_pass"] and selfg["G6_pass"]}
    out["uploaded_later_versions"] = vn
    out["instruction_scan_hits_on_local_texts"] = {
        **{pdf.rsplit("/", 1)[-1]: len(scan_text("\n".join(ev.pdf_pages(pdf)))["hits"])
           for pdf in [MU_V2_PDF, f"{L}/arXiv-1905.05564v2.pdf", *VN.values()]},
        "Step-0 muLHC v1 text": len(scan_text(read(MU_V1_FULL))["hits"])}
    out["input_sha256"] = {p: sha(p) for p in [f"{L}/arXiv-1905.05564v2.pdf", MU_V2_PDF, *VN.values(), MU_V1_FULL,
                                                MU_V1_PAGES, MU_V2_PAGES]}
    # 8: the refusal classifier on the Step-0 refusals (logged verbatim in the search log)
    refusals = {"2506.15445v2": "Paper version not found for ID: 2506.15445v2",
                "1905.05564v1": "Paper version not found for ID: 1905.05564v1"}
    out["step0_refusals"] = {v: {"is_refusal": ct.is_refusal(t, v), "template": ct.template_of(t, v)}
                             for v, t in refusals.items()}
    out["step0_answers_strictly_parsed"] = {p.rsplit("/", 2)[-2] + "/" + p.rsplit("/", 1)[-1]: answer(p).order
                                            for p in [v[0] for v in SAME.values()] + [MU_V1_PAGES, MU_V2_PAGES]}
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
