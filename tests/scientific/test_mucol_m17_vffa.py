"""Lead arithmetic (P1) for the MuCol Milestone 17 report "Tentative design of the FFA"
(M. Topp-Mugglestone, WP5, 27 March 2025, DOI 10.5281/zenodo.15054073), uploaded by the user on
2026-10-28. Expected values are quoted from the report's Tables 2.2 and 2.3 and §3.1; tolerances are
stated. The report's lattices are analytic (not tracked), as it says itself; nothing here is an LHμC
performance claim."""
import math

GEV_PER_TM = 0.299792458

# Table 2.2 (p. 11)
STAGE1 = dict(r0=953.0, theta_f=0.01033, nc=790, beta_f=0.001564, beta_d=0.001180, gamma_f=0.252, m=31.94)
STAGE4 = dict(r0=5570.0, theta_f=0.00786, nc=1000, beta_f=0.001790, beta_d=0.001166, gamma_f=-0.492, m=12.13)


def rho_f(p):
    """Eq. (2.3), p. 8: ρF = r0 tan βF / (sin θF + (1 − cos θF) cos γF tan βF)."""
    return p["r0"] * math.tan(p["beta_f"]) / (
        math.sin(p["theta_f"]) + (1 - math.cos(p["theta_f"])) * math.cos(p["gamma_f"]) * math.tan(p["beta_f"]))


def test_stage1_on_orbit_peak_field_from_closed_orbit_geometry():
    """Table 2.3: Stage 1 vFFA peak dipole field on orbit 6.93 T at the 0.3 TeV extraction energy.
    Bρ(300 GeV) / ρF(eq. 2.3) reproduces it to better than 1 %."""
    b = (300.0 / GEV_PER_TM) / rho_f(STAGE1)
    assert abs(b / 6.93 - 1) < 0.01


def test_stage4_on_orbit_peak_field_recorded_band():
    """Table 2.3: Stage 4 vFFA 13.59 T on orbit at 5 TeV. The same construction gives ≈ 13.15 T,
    3–4 % low; the report does not say at which point of the orbit the tabulated value is taken, so
    the ratio is recorded as a band rather than a reproduction."""
    b = (5000.0 / GEV_PER_TM) / rho_f(STAGE4)
    assert 0.95 < b / 13.59 < 1.0
    assert 13.0 < b < 13.3


def test_cell_bending_angles_consistent_with_cell_count():
    """Half-cell net bend π/Nc must be smaller than the F-magnet bend θF (reverse-bend D-magnet,
    p. 7); θD ≈ θF − π/Nc gives 6.35 mrad (stage 1) and 4.72 mrad (stage 4)."""
    for p, expect in ((STAGE1, 6.35e-3), (STAGE4, 4.72e-3)):
        half = math.pi / p["nc"]
        assert half < p["theta_f"]
        assert abs((p["theta_f"] - half) / expect - 1) < 0.01


def test_vertical_excursion_from_scaling_law_recorded_bands():
    """B(z) = B0 e^{mz} (eq. 1.1) ⇒ orbit displacement Δz = ln(p_ext/p_inj)/m: 50 mm for stage 1
    (table: 0.048 m, 5 % higher) and 99 mm for stage 4 (table: 0.12 m, 17 % lower than the table).
    Recorded as bands: the report's excursion definition is not stated."""
    dz1 = math.log(300.0 / 60.0) / STAGE1["m"]
    dz4 = math.log(5000.0 / 1500.0) / STAGE4["m"]
    assert 0.95 < dz1 / 0.048 < 1.10
    assert 0.75 < dz4 / 0.12 < 0.90


def test_good_field_region_peak_implies_vertical_extent():
    """Table 2.3 good-field peaks 12.52 T (stage 1) and 29.04 T (stage 4) vs on-orbit 6.93 / 13.59 T:
    inverting the scaling law gives a vertical extent of 18.5 mm and 62.6 mm beyond the orbit."""
    ext1 = math.log(12.52 / 6.93) / STAGE1["m"]
    ext4 = math.log(29.04 / 13.59) / STAGE4["m"]
    assert abs(ext1 / 0.0185 - 1) < 0.02
    assert abs(ext4 / 0.0626 - 1) < 0.02


def test_dispersion_is_inverse_field_index():
    """Eq. (3.6), p. 13: D_z = 1/m → 31.3 mm (stage 1), 82.4 mm (stage 4)."""
    assert abs(1 / STAGE1["m"] / 0.0313 - 1) < 0.01
    assert abs(1 / STAGE4["m"] / 0.0824 - 1) < 0.01


def test_kicker_example_deflection():
    """§3.1, p. 11: 0.2 T kicker filling a 1 m drift at 300 GeV deflects the beam by about 0.1 mm at
    the end of the drift (½ θ L with θ = BL/Bρ)."""
    theta = 0.2 * 1.0 / (300.0 / GEV_PER_TM)
    assert abs(0.5 * theta * 1.0 / 1.0e-4 - 1) < 0.02


def test_on_crest_gain_over_135_degree_synchronous_phase():
    """p. 6: on-crest acceleration in a quasi-isochronous vFFA gains a factor √2 over the 135°
    synchronous phase of the RCS."""
    assert abs(1 / math.sin(math.radians(135.0)) / math.sqrt(2) - 1) < 1e-9


def test_lhc_dipole_reference_limit():
    """p. 10: the design limit for the on-orbit SC dipole field is the LHC main dipole at 8.3 T;
    stage 1 (6.93 T) respects it, stage 4 (13.59 T) does not."""
    assert 6.93 < 8.3 < 13.59
