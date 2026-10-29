"""Rule 3 of docs/validation_plan.md §1 for scenarios: a scenario's validation_level may not exceed the minimum over
the records its roles point to, as enforced by lhmuc.registry.cross_check."""
from lhmuc.registry import Evidence, cross_check, scenario_level_cap


def _ev(levels: dict, scenario_level: str) -> Evidence:
    ev = Evidence()
    for pid, lvl in levels.items():
        ev.parameters[pid] = {"parameter_id": pid, "unit": "dimensionless", "value": 1.0, "notes": None,
                              "provenance": {"status": "synthetic"}, "validation": {"level": lvl}}
    ev.scenarios["TEST-SCENARIO"] = {"scenario_id": "TEST-SCENARIO", "parameters": {f"r{i}": p for i, p in enumerate(levels)},
                                     "primary_source_ids": [], "validation_level": scenario_level}
    return ev


def test_cap_is_the_minimum_over_role_records():
    both = _ev({"A": "P1", "B": "P1"}, "P1")
    assert scenario_level_cap(both, both.scenarios["TEST-SCENARIO"]) == "P1"
    ev = _ev({"A": "P1", "B": "P0"}, "P1")
    assert scenario_level_cap(ev, ev.scenarios["TEST-SCENARIO"]) == "P0"
    assert scenario_level_cap(Evidence(), {"parameters": {}}) == "P0"


def test_validator_rejects_a_scenario_label_above_its_weakest_record():
    ev = _ev({"A": "P1", "B": "P0"}, "P1")
    cross_check(ev)
    assert any("TEST-SCENARIO" in i.where and "rule 3" in i.message for i in ev.errors), ev.errors
    ok = _ev({"A": "P1", "B": "P0"}, "P0")
    cross_check(ok)
    assert not any("rule 3" in i.message for i in ok.errors)
