"""P1 entry criterion of docs/validation_plan.md as enforced by lhmuc.registry."""
from lhmuc.registry import p1_test_references, registered_test_names


def test_references_are_read_from_methods_and_check_ids_only():
    v = {"methods": ["2√(E_μE_p) (tests/scientific/test_analytical_checks.py::test_sqrt_s)"],
         "check_ids": ["tests/scientific/test_batch7_documents.py::test_andre2022_magnetic_rigidities"],
         "notes": "see test_not_a_reference_from_notes"}
    refs = p1_test_references(v)
    # file names such as test_analytical_checks also match the token pattern; the rule intersects the
    # references with real function names, so only the function names matter here
    assert {"test_sqrt_s", "test_andre2022_magnetic_rigidities"} <= refs
    assert "test_not_a_reference_from_notes" not in refs
    assert {"test_sqrt_s", "test_andre2022_magnetic_rigidities"} <= refs & registered_test_names()


def test_known_test_functions_are_discovered():
    names = registered_test_names()
    assert "test_aritome2024_measured_ultra_slow_muon_chain" in names
    assert "test_references_are_read_from_methods_and_check_ids_only" in names
