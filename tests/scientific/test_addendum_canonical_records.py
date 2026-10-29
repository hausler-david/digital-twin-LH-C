"""Single-source-of-truth checks for the addendum: the canonical parameter records written from the uploaded
documents must carry exactly the values that tests/scientific/test_workshop_decks.py pins, keep the status their
source category allows, and cite uploaded sources with checksums. The supersession and conflict checks follow in
tests/scientific/test_addendum_registry_consistency.py once the registry stage has run."""
import math

import pytest

from lhmuc.registry import load_all
from lhmuc.units import to_si

ev = load_all()


def si(pid: str) -> float:
    p = ev.parameters[pid]
    assert p["value"] is not None, f"{pid} has no value"
    return to_si(float(p["value"]), p["unit"])


CANONICAL = {
    # parameter_id: (value, unit, rel_tol)
    "DET_NOZZLE_HALF_OPENING_ANGLE_WS2026_FORTHOMME": (40, "mrad", 1e-9),
    "DET_NOZZLE_HALF_OPENING_ANGLE_OPTION2_WS2026_FORTHOMME": (100, "mrad", 1e-9),
    "MACHINE_MU_BUNCH_SPACING_WS2026_FORTHOMME": (300, "ns", 1e-9),
    "MACHINE_MU_BUNCHES_WS2026_FORTHOMME": (40, "dimensionless", 1e-9),
    "MACHINE_MU_BUNCH_POPULATION_WS2026_FORTHOMME": (1e10, "dimensionless", 1e-9),
    "IR_SIGMA_XY_IP_WS2026_FORTHOMME": (4.3, "um", 1e-9),
    "PROTON_BETA_STAR_WS2026_FORTHOMME": (7, "cm", 1e-9),
    "MACHINE_PEAK_LUMINOSITY_WS2026_FORTHOMME": (1e34, "cm^-2 s^-1", 1e-9),
    "MACHINE_MUON_POLARISATION_WS2026_FORTHOMME": (0.5, "dimensionless", 1e-9),
    "PROTON_BUNCH_POPULATION_IMPLIED_WS2026_FORTHOMME": (6.97e11, "dimensionless", 0.02),
    "IR_LSTAR_LHEC_WS2026_FORTHOMME": (15, "m", 1e-9),
    "IR_LSTAR_MR7": (6, "m", 1e-9),
    "DET_NOZZLE_TIP_DISTANCE_MR7": (6, "cm", 1e-9),
    "DET_NOZZLE_OUTER_ANGLE_NEAR_IP_MR7": (10, "degree", 1e-9),
    "DET_NOZZLE_LENGTH_WS2026_KILIC": (487.8, "cm", 1e-9),
    "DET_NOZZLE_TIP_DISTANCE_WS2026_KILIC": (6, "cm", 1e-9),
    "DET_SOLENOID_FIELD_MAIA": (5, "T", 1e-9),
    "DET_SOLENOID_FIELD_MUSIC": (5, "T", 1e-9),
    "SOURCE_MUONIUM_FORMATION_FRACTION_TRIUMF_WS2026_ZHANG": (0.52, "dimensionless", 1e-9),
    "SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020": (0.655, "dimensionless", 1e-9),
    "SOURCE_LASER_IONISATION_EFF_122NM_BUDGET_WS2026_ZHANG": (0.73, "dimensionless", 1e-9),
    "SOURCE_SURFACE_MU_PER_PULSE_ARITOME2024": (9.5e4, "dimensionless", 1e-9),
    "SOURCE_USM_PER_PULSE_100KEV_ARITOME2024": (2e-3, "dimensionless", 1e-9),
    "SOURCE_USM_PER_SURFACE_MUON_100KEV_ARITOME2024": (2.1e-8, "dimensionless", 0.02),
    "SOURCE_RFQ_PERVEANCE_RATIO_WS2026_NAKAZAWA": (220, "dimensionless", 1e-9),
    "ACC_VFFA_PEAK_DIPOLE_FIELD_8T_WS2026_TOPPMUGGLESTONE": (8, "T", 1e-9),
    "ACC_VFFA_PEAK_DIPOLE_FIELD_10T_WS2026_TOPPMUGGLESTONE": (10, "T", 1e-9),
    "ACC_VFFA1_PEAK_FIELD_ON_ORBIT_MR7": (6.93, "T", 1e-9),
    "ACC_VFFA1_ORBIT_RADIUS_MR7": (953, "m", 1e-9),
    "MACHINE_MUON_POLARISATION_MUTRISTAN2022": (0.8, "dimensionless", 1e-9),
}


@pytest.mark.parametrize("pid,expected", sorted(CANONICAL.items()))
def test_canonical_record_matches_pinned_value(pid, expected):
    assert pid in ev.parameters, f"canonical record {pid} missing"
    value, unit, tol = expected
    assert math.isclose(si(pid), to_si(value, unit), rel_tol=tol), (pid, ev.parameters[pid]["value"], ev.parameters[pid]["unit"])


def test_reported_lhmuc_records_come_from_workshop_decks():
    for pid in ("DET_NOZZLE_HALF_OPENING_ANGLE_WS2026_FORTHOMME", "DET_NOZZLE_LENGTH_WS2026_KILIC", "SOURCE_RFQ_PERVEANCE_RATIO_WS2026_NAKAZAWA"):
        p = ev.parameters[pid]
        assert p["provenance"]["status"] == "reported_lhmuc", pid
        assert ev.sources[p["provenance"]["source"]["source_id"]]["category"] == "PRIMARY_LHMUC", pid


def test_analogue_records_are_not_reported_lhmuc():
    for pid in ("IR_LSTAR_MR7", "DET_SOLENOID_FIELD_MAIA", "ACC_VFFA1_PEAK_FIELD_ON_ORBIT_MR7", "SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020"):
        assert ev.parameters[pid]["provenance"]["status"] in ("analogous", "imported_related"), pid



def test_uploaded_sources_registered_with_checksums():
    for sid in ("SRC_WS1681458_FORTHOMME_DETECTOR", "SRC_WS1681458_KILIC_NOZZLE", "SRC_WS1681458_ZHANG_MUONIUM", "SRC_WS1681458_NAKAZAWA_LOW_VELOCITY",
                "SRC_ARXIV_2510_27437", "SRC_ARXIV_2410_11367", "SRC_ARXIV_2006_01947", "SRC_ARXIV_2201_06664"):
        s = ev.sources[sid]
        assert s["access"] == "uploaded" and s.get("sha256") and len(s["sha256"]) == 64, sid
