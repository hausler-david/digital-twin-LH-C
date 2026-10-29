import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from lhmuc.registry import SCHEMA_DIR, validator

SCHEMAS = sorted(p.stem.replace(".schema", "") for p in SCHEMA_DIR.glob("*.schema.json"))


@pytest.mark.parametrize("name", SCHEMAS)
def test_schema_compiles(name):
    doc = json.loads((SCHEMA_DIR / f"{name}.schema.json").read_text())
    Draft202012Validator.check_schema(doc)
    assert doc["$id"].endswith(f"{name}.schema.json")


def test_required_schema_set_present():
    required = {"machine", "component", "material", "proposal", "experiment", "simulation_run", "optimization", "provenance"}
    assert required <= set(SCHEMAS)


def test_parameter_unknown_requires_null_value():
    v = validator("provenance")
    base = {
        "parameter_id": "TEST_PARAM", "name": "t", "symbol": None, "subsystem": "machine", "value": 1.0,
        "unit": "GeV", "uncertainty": None, "allowed_range": None,
        "provenance": {"status": "unknown", "extraction_method": "not_applicable", "source": None,
                       "applicability": {"category": "unresolved", "explanation": "x"}, "confidence": "none"},
        "validation": {"level": "P0", "methods": []}, "dependencies": [], "date_added": "2026-10-28",
        "responsible_module": "test",
    }
    assert list(v.iter_errors({"parameters": [base]}))
    base["value"] = None
    assert not list(v.iter_errors({"parameters": [base]}))


def test_parameter_synthetic_requires_assumption_id():
    v = validator("provenance")
    p = {
        "parameter_id": "TEST_SYN", "name": "t", "symbol": None, "subsystem": "detector", "value": 10,
        "unit": "degree", "uncertainty": None, "allowed_range": {"min": 5, "max": 20, "unit": "degree"},
        "provenance": {"status": "synthetic", "extraction_method": "assumption_record", "source": None,
                       "applicability": {"category": "screening_only", "explanation": "x"}, "confidence": "low"},
        "validation": {"level": "P0", "methods": []}, "dependencies": [], "date_added": "2026-10-28",
        "responsible_module": "test",
    }
    assert list(v.iter_errors({"parameters": [p]}))
    p["provenance"]["assumption_id"] = "ASM_TEST"
    assert not list(v.iter_errors({"parameters": [p]}))


def test_reported_requires_source_ref():
    v = validator("provenance")
    p = {
        "parameter_id": "TEST_REP", "name": "t", "symbol": None, "subsystem": "machine", "value": 5.3,
        "unit": "TeV", "uncertainty": None, "allowed_range": None,
        "provenance": {"status": "reported_lhmuc", "extraction_method": "manual_table_read", "source": None,
                       "applicability": {"category": "direct", "explanation": "x"}, "confidence": "high"},
        "validation": {"level": "P0", "methods": []}, "dependencies": [], "date_added": "2026-10-28",
        "responsible_module": "test",
    }
    assert list(v.iter_errors({"parameters": [p]}))


def _source_entry(**kw):
    e = {"source_id": "SRC_ARXIV_1234_56789", "title": "t", "source_type": "arxiv_preprint", "category": "PEER_REVIEWED",
         "url": "https://arxiv.org/abs/1234.56789", "access_date": "2026-10-29", "access": "fetched_text", "relevance": "r"}
    e.update(kw)
    return {"sources": [e]}


def test_source_schema_requires_archive_for_fetched_text():
    v = validator("source")
    assert list(v.iter_errors(_source_entry()))
    complete = dict(archived_file="references/_local/SRC_ARXIV_1234_56789/full.txt (git-ignored)", sha256="a" * 64,
                    version="v2", arxiv_id="1234.56789")
    assert not list(v.iter_errors(_source_entry(**complete)))
    assert list(v.iter_errors(_source_entry(**{**complete, "archived_file": "elsewhere/full.txt"})))
    assert not list(v.iter_errors(_source_entry(access="snippet_only")))


def test_unknown_access_mode_rejected():
    assert list(validator("source").iter_errors(_source_entry(access="mirror")))


def test_proposal_accepts_fetched_text():
    import yaml
    path = sorted(Path(SCHEMA_DIR.parent / "theory" / "benchmarks").glob("*/proposal.yaml"))[0]
    doc = yaml.safe_load(path.read_text())
    doc["access"] = "fetched_text"
    assert not list(validator("proposal").iter_errors(doc))


def test_archived_metadata_connector_text_branch():
    v = validator("archived_metadata")
    base = json.loads(sorted((SCHEMA_DIR.parent / "research" / "archived_metadata").glob("*.json"))[0].read_text())
    assert not list(v.iter_errors(base))
    connector = {**base, "content_kind": "connector_text"}
    assert list(v.iter_errors(connector))
    connector.update(local_file="references/_local/SRC_ARXIV_1234_56789/full.txt", committed_copy=None, upload_name=None,
                     connector="alphaXiv", connector_tool="get_paper_content (fullText: true)",
                     connector_calls=[{"tool": "get_paper_content", "arguments": {"fullText": True}, "tool_use_id": "toolu_1",
                                       "called_on": "2026-10-29"}],
                     delivered_version="v2", version_evidence="page-tagged response paper id 1234.56789v2", page_images=False,
                     page_tag_files=[{"file": "references/_local/SRC_ARXIV_1234_56789/pages.xml", "sha256": "b" * 64,
                                      "pages": [1, 2], "tool_use_id": "toolu_2"}],
                     instruction_scan={"patterns_version": "2026-10-29.1", "hits": []},
                     storage="owner decision 2026-10-29: store only")
    assert not list(v.iter_errors(connector))
    assert list(v.iter_errors({**connector, "page_images": True}))
    assert list(v.iter_errors({**connector, "delivered_version": "2"}))
    assert list(v.iter_errors({**connector, "instruction_scan": "0 hits"}))


def test_access_modes_partition_the_schema_enum():
    from lhmuc.registry import FULL_PAGE_READ, NOT_READ_IN_FULL, READ_IN_FULL, TEXT_ONLY
    enum = json.loads((SCHEMA_DIR / "provenance.schema.json").read_text())["$defs"]["access_mode"]["enum"]
    assert set(READ_IN_FULL) | set(NOT_READ_IN_FULL) == set(enum)
    assert not set(READ_IN_FULL) & set(NOT_READ_IN_FULL)
    assert set(TEXT_ONLY) <= set(READ_IN_FULL) and not set(TEXT_ONLY) & set(FULL_PAGE_READ)
