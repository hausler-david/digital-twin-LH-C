"""Integrity of the real evidence registries committed in the repository."""
import subprocess
import sys
from pathlib import Path

import pytest

from lhmuc import REPO_ROOT
from lhmuc.registry import load_all

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
    """A PRIMARY_LHMUC source that was only seen as a snippet may not back a reported_lhmuc value."""
    for pid, p in ev.parameters.items():
        if p["provenance"]["status"] == "reported_lhmuc":
            src = ev.sources[p["provenance"]["source"]["source_id"]]
            assert src["access"] in ("uploaded", "fetched"), f"{pid} backed by {src['access']} source"


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


def test_search_log_and_unresolved_exist():
    assert (REPO_ROOT / "research" / "search_log.csv").exists()
    assert (REPO_ROOT / "research" / "unresolved_searches.md").exists()
    assert (REPO_ROOT / "research" / "source_quality_policy.md").exists()
