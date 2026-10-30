"""Integrity of the real evidence registries committed in the repository."""
import subprocess
import sys
from pathlib import Path

import pytest

from lhmuc import REPO_ROOT
from lhmuc.registry import FETCHED_TEXT_NOTE, PARAM_ID_RE, READ_IN_FULL, TEXT_ONLY, load_all, registered_test_names

ev = load_all()


def test_no_validation_errors():
    msgs = [str(e) for e in ev.errors]
    assert not msgs, "\n".join(msgs)


def test_registries_non_empty():
    assert len(ev.parameters) >= 40
    assert len(ev.sources) >= 20
    assert len(ev.scenarios) >= 4
    assert len(ev.conflicts) >= 8
    assert len(ev.proposals) >= 4


def test_every_parameter_has_evidence_or_explicit_status():
    for pid, p in ev.parameters.items():
        st = p["provenance"]["status"]
        if st in ("reported_lhmuc", "imported_related", "analogous"):
            src = p["provenance"]["source"]
            assert src and src["source_id"] in ev.sources and src["quotation"], pid
        elif st in ("derived_lhmuc", "analytical_estimate"):
            assert p["provenance"]["derivation"], pid
        elif st == "synthetic":
            assert p["provenance"]["assumption_id"] in ev.assumptions, pid
            assert p["allowed_range"], pid
        else:
            assert st in ("unknown", "scan_variable"), pid


def test_null_is_not_zero():
    for pid, p in ev.parameters.items():
        if p["provenance"]["status"] == "unknown":
            assert p["value"] is None, pid
        if p["value"] == 0:
            assert p.get("notes"), f"{pid}: zero needs a note"


def test_primary_sources_are_uploaded_or_fetched():
    """A PRIMARY_LHMUC source that was only seen as a snippet may not back a reported_lhmuc value: it must have been read
    in full (uploaded, fetched, or fetched_text through the owner-authorised connector, then capped at medium)."""
    for pid, p in ev.parameters.items():
        if p["provenance"]["status"] == "reported_lhmuc":
            src = ev.sources[p["provenance"]["source"]["source_id"]]
            assert src["access"] in READ_IN_FULL, f"{pid} backed by {src['access']} source"


def test_snippet_sources_capped_confidence():
    for pid, p in ev.parameters.items():
        src = p["provenance"].get("source")
        if src and src.get("source_id") in ev.sources:
            if ev.sources[src["source_id"]]["access"] in ("snippet_only", "blocked", "pending_fetch"):
                assert p["provenance"]["confidence"] in ("medium", "low", "none"), pid


def test_csv_registries_in_sync():
    r = subprocess.run([sys.executable, str(REPO_ROOT / "tools" / "build_registries.py"), "--check"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


@pytest.mark.parametrize("name", ["missing_evidence.csv", "validation_registry.csv", "risk_register.csv",
                                  "parameter_registry.csv", "assumption_registry.csv"])
def test_registry_csv_exists_and_has_rows(name):
    path = REPO_ROOT / "registries" / name
    assert path.exists(), name
    lines = [ln for ln in path.read_text().splitlines() if ln.strip()]
    assert len(lines) >= 3, f"{name} has fewer than 2 data rows"


def test_csv_files_have_header_field_count():
    """Every row of the CSV registries, the search log and its fragments has as many fields as its header: an
    unquoted comma in an authored field shifts every later column (edit authored CSVs through the csv module)."""
    import csv
    files = sorted((REPO_ROOT / "registries").glob("*.csv")) + [REPO_ROOT / "research" / "search_log.csv"] + \
        sorted((REPO_ROOT / "research" / "_fragments").glob("*.csv"))
    for f in files:
        with f.open(newline="") as fh:
            rows = list(csv.reader(fh))
        bad = [n for n, r in enumerate(rows[1:], 2) if r and len(r) != len(rows[0])]
        assert not bad, f"{f.relative_to(REPO_ROOT)}: rows {bad[:5]} do not have {len(rows[0])} fields"


def test_search_log_and_unresolved_exist():
    assert (REPO_ROOT / "research" / "search_log.csv").exists()
    assert (REPO_ROOT / "research" / "unresolved_searches.md").exists()
    assert (REPO_ROOT / "research" / "source_quality_policy.md").exists()


def test_source_parameters_extracted_in_sync():
    """Every source lists exactly the parameter ids that cite it (tools/sync_parameters_extracted.py)."""
    import subprocess
    import sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[2]
    r = subprocess.run([sys.executable, str(root / "tools" / "sync_parameters_extracted.py"), "--check"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-2000:]


def _citing(sid: str):
    for kind, recs in (("parameter", ev.parameters), ("material", ev.materials)):
        for rid, r in recs.items():
            if ((r.get("provenance") or {}).get("source") or {}).get("source_id") == sid:
                yield f"{kind} {rid}", r


def test_fetched_text_records_flagged():
    """Every record citing a fetched_text source (connector-delivered text, docs/internet_research_protocol.md §5a) is at
    most medium, cites an integer PDF page, is no figure read and says it was not checked against page images.
    Vacuous until the first fetched_text source is registered."""
    for sid in (s for s, src in ev.sources.items() if src["access"] in TEXT_ONLY):
        for where, r in _citing(sid):
            prov = r["provenance"]
            assert prov["confidence"] in ("medium", "low", "none"), where
            assert prov["extraction_method"] != "manual_figure_read", where
            assert isinstance(prov["source"]["page"], int), where
            assert FETCHED_TEXT_NOTE in (r.get("notes") or "").lower(), where


def test_archived_metadata_matches_registry_and_files():
    """research/archived_metadata/*.json agrees with the registry; every committed copy exists and still has its
    recorded SHA-256 and size; files under git-ignored references/_local/ (archived PDFs, saved connector texts and
    page-tagged responses) are re-hashed when this checkout has them."""
    import hashlib
    assert ev.archives, "no archived metadata loaded"
    for sid, a in ev.archives.items():
        assert ev.sources[sid].get("sha256") == a["sha256"], sid
        if a.get("committed_copy"):
            data = (REPO_ROOT / a["committed_copy"]).read_bytes()
            assert hashlib.sha256(data).hexdigest() == a["sha256"] and len(data) == a["size_bytes"], sid
        files = [(a["local_file"], a["sha256"], a["size_bytes"])]
        files += [(pt["file"], pt["sha256"], pt.get("size_bytes")) for pt in a.get("page_tag_files") or []]
        for rel, sha, size in files:
            if (REPO_ROOT / rel).is_file():
                data = (REPO_ROOT / rel).read_bytes()
                assert hashlib.sha256(data).hexdigest() == sha, f"{sid}: {rel}"
                assert size is None or len(data) == size, f"{sid}: {rel} size"


def test_nothing_under_references_local_is_tracked():
    """Archived files without a redistribution licence and every saved connector text stay git-ignored."""
    r = subprocess.run(["git", "ls-files", "references/_local"], cwd=REPO_ROOT, capture_output=True, text=True)
    assert r.returncode == 0 and r.stdout.strip() == "", r.stdout


def test_search_log_connector_rows():
    """Search-log rows follow §5a: one tool per row, get_paper_content always with fullText on a versioned arXiv URL,
    discovery and page-attribution rows never claim fetched_text, calibration rows claim no access, and every
    fetched_text source has its full-text row with access fetched_text."""
    import csv
    import re
    import json
    modes = {"uploaded", "fetched", "fetched_text", "snippet_only", "blocked", "pending_fetch", ""}
    tools = {"alphaXiv:discover_papers", "alphaXiv:get_paper_content", "alphaXiv:answer_pdf_queries"}
    rows = list(csv.DictReader((REPO_ROOT / "research" / "search_log.csv").open()))
    # the read-only spot check of 2026-10-29 was made before the §5a rules ("Step-0 gates"): its unversioned
    # answer_pdf_queries call is logged as made, marked not admissible, never archived (a scratch copy existed until
    # 2026-10-30), and backs nothing
    spot_check = ("alphaxiv-spotcheck", "1905.05564")
    full_text_urls = set()
    for r in rows:
        assert r["access_mode"] in modes, r
        if "alphaxiv" not in r["tool"].lower():
            assert r["access_mode"] != "fetched_text", r
            continue
        assert r["tool"] in tools, r
        args = json.loads(r["query"])
        if r["family"] in ("alphaxiv-calibration", "alphaxiv-spotcheck"):
            assert r["access_mode"] == "", r
        if r["tool"] == "alphaXiv:get_paper_content":
            assert args.get("fullText") is True and args.get("url") == r["url"], r
            assert re.fullmatch(r"https://arxiv\.org/abs/\d{4}\.\d{4,5}v\d+", r["url"]), r
            if r["access_mode"] == "fetched_text":
                full_text_urls.add(r["url"])
        else:
            assert r["access_mode"] != "fetched_text", r
            if r["tool"] == "alphaXiv:answer_pdf_queries":
                if (r["family"], str(args.get("paper"))) == spot_check:
                    assert "NOT ADMISSIBLE" in r["relevance"] and not r["local_archived_filename"], r
                    continue
                assert re.fullmatch(r"\d{4}\.\d{4,5}v\d+", str(args.get("paper"))), r
    for sid, src in ev.sources.items():
        if src["access"] in TEXT_ONLY:
            assert f"https://arxiv.org/abs/{src['arxiv_id']}{ev.archives[sid]['delivered_version']}" in full_text_urls, sid


def test_research_fragments_merged():
    r = subprocess.run([sys.executable, str(REPO_ROOT / "tools" / "merge_research_fragments.py"), "--check"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_validation_registry_names_existing_tests():
    """Every test named in the method column of registries/validation_registry.csv exists (function or module)."""
    import csv
    import re
    known = registered_test_names(REPO_ROOT) | {f.stem for f in (REPO_ROOT / "tests").rglob("test_*.py")}
    for r in csv.DictReader((REPO_ROOT / "registries" / "validation_registry.csv").open()):
        for name in re.findall(r"(test_\w+)", r["method"]):
            assert name in known, f"{r['check_id']}: {name}"


def test_parameter_ids_match_the_id_pattern():
    """lhmuc.registry.capped_inputs finds inputs named in a derivation with PARAM_ID_RE; every id must match it."""
    bad = [pid for pid in list(ev.parameters) + list(ev.materials) if not PARAM_ID_RE.fullmatch(pid)]
    assert not bad, bad


def test_fetched_text_quotations_check():
    """tools/check_fetched_text_quotes.py passes on the committed registry (it skips saved texts this checkout lacks)."""
    r = subprocess.run([sys.executable, str(REPO_ROOT / "tools" / "check_fetched_text_quotes.py")], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-2000:]
