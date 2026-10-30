"""Step-0b pre-calibration (docs/internet_research_protocol.md §5a, revision 2026-10-30.2): every threshold and claim the
Step-0b rules rest on, recomputed from the saved Step-0 files and the local PDFs before any Step-0b call. No connector
call. Output: counts, overlaps and verdicts only (research/_fragments/alphaxiv_calibration_2026-10-29/calibration_0b_pre.json).

Run from the repository root: python -I research/_fragments/alphaxiv_calibration_2026-10-29/pre_0b.py > \
    research/_fragments/alphaxiv_calibration_2026-10-29/calibration_0b_pre.json
"""
from __future__ import annotations

import importlib.util
import json
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
from lhmuc import connector_text as ct  # noqa: E402

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
                    "same": ct.same_page(a.pages[n], lp), "differs": ct.differs_page(a.pages[n], lp),
                    "in_full_text": None if full is None else ct.contained(a.pages[n], full)})
    return out


def main() -> int:
    out: dict = {"thresholds": {"SAME_PAGE_OVERLAP": ct.SAME_PAGE_OVERLAP, "SAME_PAPER_MEDIAN": ct.SAME_PAPER_MEDIAN,
                                "MIN_PAGE_WORDS": ct.MIN_PAGE_WORDS, "SAME_PAPER_TEXT": ev.SAME_PAPER_TEXT,
                                "G1_RECALL": ev.G1_RECALL, "G1_PRECISION": ev.G1_PRECISION}}
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
                                                       "min_overlap": min(x["overlap"] for x in r2)}
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
        "same_paper_median": round(ct.same_paper(mu1.pages, list(local2)), 4),
        "P6_predicted_verdict": ("version_specific" if all(x["in_full_text"] for x in r1) and any(x["differs"] for x in r1)
                                 and not any(x["same"] and not x["in_full_text"] for x in r1) else "not version_specific")}
    out["muLHC_v2_pages_in_v1_full_text"] = sum(ct.contained(b, f1) for b in mu2.pages.values())
    out["S2_total"] = {"same_version_pages": out["totals"]["S2_pages"] + out["muLHC_v1_pages_vs_local_v2"]["in_v1_full_text"],
                       "of": sum(v["pages"] for k, v in same_version.items() if "pages only" not in k) + len(r1)}
    # 6: same paper or not (page medians and whole-text recall)
    unrelated = {"Kaya pages vs local muLHC v2": (SAME["Kaya 1905.05564v2"][0], MU_V2_PDF),
                 "DIS2026 pages vs local Kaya v2": (SAME["DIS2026 2610.35154v1"][0], f"{L}/arXiv-1905.05564v2.pdf"),
                 "MR7 pages vs local DIS2026": (SAME["MR7 2510.27437v1"][0], DIS_PDF),
                 "muLHC v2 pages vs local Kaya v2": (MU_V2_PAGES, f"{L}/arXiv-1905.05564v2.pdf")}
    out["same_paper_median_unrelated"] = {k: round(ct.same_paper(answer(p).pages, list(ev.pdf_pages(pdf))), 4)
                                          for k, (p, pdf) in unrelated.items()}
    texts = {"muLHC v1 text vs local muLHC v2 (same paper)": (MU_V1_FULL, MU_V2_PDF),
             "Kaya text vs local muLHC v2": (SAME["Kaya 1905.05564v2"][1], MU_V2_PDF),
             "DIS2026 text vs local Kaya v2": (SAME["DIS2026 2610.35154v1"][1], f"{L}/arXiv-1905.05564v2.pdf"),
             "muLHC v1 text vs local DIS2026": (MU_V1_FULL, DIS_PDF),
             "muLHC v1 text vs local 2201.06664v2": (MU_V1_FULL, f"{L}/arXiv-2201.06664v2.pdf")}
    out["whole_text_score"] = {k: round(ev.text_score(read(t), "\n".join(ev.pdf_pages(pdf))), 4)
                               for k, (t, pdf) in texts.items()}
    out["whole_text_score_unrelated_max"] = round(max(
        ev.text_score(read(t), "\n".join(ev.pdf_pages(pdf)))
        for t in (MU_V1_FULL,) + tuple(v[1] for v in SAME.values())
        for pdf in (MU_V2_PDF, f"{L}/arXiv-1905.05564v2.pdf", DIS_PDF, f"{L}/arXiv-2510.27437v1.pdf", *VN.values())
        if not (t == MU_V1_FULL and pdf == MU_V2_PDF) and not any(t == v[1] and pdf == v[2] for v in SAME.values())), 4)
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
