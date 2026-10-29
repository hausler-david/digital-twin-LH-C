"""Registry-stage checks for the addendum: the Phase 0 synthetic assumptions that now have reported values must be
marked superseded (CLAUDE.md §4), their _SYN parameters must stay scan-only, and the new conflicts must exist."""
import math

import pytest

from lhmuc.registry import load_all
from lhmuc.units import to_si

ev = load_all()


def si(pid: str) -> float:
    p = ev.parameters[pid]
    assert p["value"] is not None, f"{pid} has no value"
    return to_si(float(p["value"]), p["unit"])


SUPERSEDED = ["ASM_DET_NOZZLE_OPENING_ANGLE", "ASM_DET_NOZZLE_LENGTH", "ASM_DET_NOZZLE_TIP_DISTANCE_FROM_IP", "ASM_DET_NOZZLE_MATERIAL",
              "ASM_DET_SOLENOID_FIELD", "ASM_ACC_VFFA_PEAK_FIELD", "ASM_SOURCE_MUONIUM_FORMATION_FRACTION",
              "ASM_SOURCE_LASER_IONISATION_EFFICIENCY", "ASM_IR_LSTAR", "ASM_MACHINE_MUON_POLARISATION"]


@pytest.mark.parametrize("aid", SUPERSEDED)
def test_phase0_assumption_superseded_by_uploaded_evidence(aid):
    a = ev.assumptions[aid]
    assert a["status"] == "superseded_by_evidence", aid
    assert a.get("superseded_by"), aid
    for pid in a["superseded_by"]:
        assert ev.parameters[pid]["provenance"]["status"] not in ("synthetic", "unknown", "scan_variable"), (aid, pid)


def test_superseded_synthetic_parameters_remain_scan_only():
    for aid in SUPERSEDED:
        pid = ev.assumptions[aid]["parameter_id"]
        p = ev.parameters[pid]
        assert p["provenance"]["status"] == "synthetic" and p["provenance"]["applicability"]["category"] == "screening_only", pid
        for sid, s in ev.scenarios.items():
            assert pid not in s.get("parameters", {}).values(), (sid, pid)


def test_new_conflicts_registered():
    for cid in ("CONF_NOZZLE_OPENING_ANGLE", "CONF_MUONIUM_FORMATION_FRACTION", "CONF_LASER_IONISATION_EFFICIENCY",
                "CONF_SOURCE_CONCEPT", "CONF_IR_LSTAR", "CONF_DETECTOR_SOLENOID_FIELD", "CONF_VFFA_PEAK_FIELD", "CONF_FRONT_END_SPACE_CHARGE"):
        assert cid in ev.conflicts, cid
        assert len(ev.conflicts[cid]["competing_values"]) >= 2, cid


