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
