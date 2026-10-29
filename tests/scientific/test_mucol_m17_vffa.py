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
    """Table 2.3: Stage 4 vFFA 13.59 T on orbit at 5 TeV. Bρ/ρF is the F-magnet field, ≈ 13.15 T, 3–4 %
    below the table. The tabulated peak is the reverse-bend D-magnet field, reproduced to +0.2 % by
    test_tabulated_peak_fields_are_f_magnet_stage1_and_d_magnet_stage4; this band stays as the F-magnet check."""
    b = (5000.0 / GEV_PER_TM) / rho_f(STAGE4)
    assert 0.95 < b / 13.59 < 1.0
    assert 13.0 < b < 13.3


def test_cell_bending_angles_consistent_with_cell_count():
    """Half-cell net bend π/Nc must be smaller than the F-magnet bend θF (reverse-bend D-magnet,
    p. 7). The planar estimate θD ≈ θF − π/Nc gives 6.35 mrad (stage 1) and 4.72 mrad (stage 4); it neglects
    the inclined F-bend and lies 3.1 % and 11.0 % below eq. (2.1), see
    test_eq21_reverse_bend_angle_exceeds_planar_estimate."""
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


# ---------------------------------------------------------------- closed-orbit geometry, eqs (2.1)–(2.6)
# Added after the batch-8 adversarial verification (research/_fragments/verify_G11_MUCOL_M17_VFFA.md); the
# equations are transcribed from the p. 8 page image.
def closed_orbit(p):
    a = math.pi / p["nc"]
    th_f, g_f, b_f, b_d = p["theta_f"], p["gamma_f"], p["beta_f"], p["beta_d"]
    k = math.tan(a) * math.cos(g_f) * math.tan(th_f) + 1
    num = math.sqrt((math.tan(a) - math.cos(g_f) * math.tan(th_f)) ** 2 + math.sin(g_f) ** 2 * math.sin(th_f) ** 2 * k ** 2)
    den = math.sqrt(1 - math.sin(g_f) ** 2 * math.sin(th_f) ** 2) * k
    th_d = math.atan(num / den)                                                   # (2.1)
    g_d = math.asin(math.sin(th_f) / math.sin(th_d) * math.sin(g_f))              # (2.2)
    r_f = rho_f(p)                                                                # (2.3)
    r1 = r_f * math.sin(th_f) / math.sin(b_f)                                     # (2.4)
    r2 = r1 * (math.cos(b_f) + math.tan(th_f) * math.cos(g_f) * math.sin(b_f)) / (
        math.cos(a - b_d) + math.tan(th_f) * math.cos(g_f) * math.sin(a - b_d))   # (2.5)
    r_d = r2 * math.sin(b_d) / math.sin(th_d)                                     # (2.6)
    return dict(a=a, theta_d=th_d, gamma_d=g_d, rho_f=r_f, r2=r2, rho_d=r_d)


def reconstruct_r3(p, g):
    """Independent 3D construction of the half-cell orbit from the F-magnet centre K to the D-magnet centre C;
    returns the radius of C from the machine axis."""
    r0, th_f, g_f, th_d = p["r0"], p["theta_f"], p["gamma_f"], g["theta_d"]
    t0, n = (0.0, 1.0, 0.0), (-math.cos(g_f), 0.0, math.sin(g_f))
    h = tuple((r0, 0.0, 0.0)[i] + g["rho_f"] * (n[i] * (1 - math.cos(th_f)) + t0[i] * math.sin(th_f)) for i in range(3))
    t_h = tuple(n[i] * math.sin(th_f) + t0[i] * math.cos(th_f) for i in range(3))
    alpha = g["a"] - p["beta_d"]
    s = (math.tan(alpha) * h[0] - h[1]) / (t_h[1] - math.tan(alpha) * t_h[0])
    e = tuple(h[i] + s * t_h[i] for i in range(3))
    t_c = (-math.sin(g["a"]), math.cos(g["a"]), 0.0)
    n_d = tuple((t_c[i] - t_h[i] * math.cos(th_d)) / math.sin(th_d) for i in range(3))
    c = tuple(e[i] + g["rho_d"] * (t_h[i] * math.sin(th_d) + n_d[i] * (1 - math.cos(th_d))) for i in range(3))
    return math.hypot(c[0], c[1]), s


def test_eq21_reverse_bend_angle_exceeds_planar_estimate():
    """Eq. (2.1) gives θD = 6.554 mrad (stage 1) and 5.303 mrad (stage 4); the vector form
    arccos(cos θF cos(π/N) + cos γF sin θF sin(π/N)) agrees; the planar estimate is 3.1 % and 11.0 % lower."""
    for p, expect, planar_deficit in ((STAGE1, 6.554e-3, 0.031), (STAGE4, 5.303e-3, 0.110)):
        g = closed_orbit(p)
        vec = math.acos(math.cos(p["theta_f"]) * math.cos(g["a"])
                        + math.cos(p["gamma_f"]) * math.sin(p["theta_f"]) * math.sin(g["a"]))
        assert abs(g["theta_d"] / expect - 1) < 1e-3
        assert abs(g["theta_d"] / vec - 1) < 1e-6
        assert abs(1 - (p["theta_f"] - g["a"]) / g["theta_d"] - planar_deficit) < 0.003


def test_tabulated_peak_fields_are_f_magnet_stage1_and_d_magnet_stage4():
    """Table 2.3 'Peak Dipole Field On Orbit': stage 1 6.93 T is the F-magnet field Bρ/ρF = 6.935 T (D-magnet
    5.83 T); stage 4 13.59 T is the reverse-bend D-magnet field Bρ/ρD = 13.62 T (+0.2 %; F-magnet 13.15 T)."""
    g1, g4 = closed_orbit(STAGE1), closed_orbit(STAGE4)
    brho1, brho4 = 300.0 / GEV_PER_TM, 5000.0 / GEV_PER_TM
    b_f1, b_d1 = brho1 / g1["rho_f"], brho1 / g1["rho_d"]
    b_f4, b_d4 = brho4 / g4["rho_f"], brho4 / g4["rho_d"]
    assert b_d1 < b_f1 and abs(b_f1 / 6.93 - 1) < 0.002 and abs(b_d1 - 5.83) < 0.01
    assert b_f4 < b_d4 and abs(b_d4 / 13.59 - 1) < 0.004 and abs(b_f4 - 13.15) < 0.01


def test_drift_length_from_half_cell_angles():
    """Table 2.3 drift lengths 1.18 m and 1.03 m equal r0(π/Nc − βF − βD) = 1.1748 m and 1.0338 m and the exact
    3D chord of the reconstruction to better than 0.5 %, so βF and βD are half-magnet opening angles."""
    for p, table in ((STAGE1, 1.18), (STAGE4, 1.03)):
        g = closed_orbit(p)
        flat = p["r0"] * (g["a"] - p["beta_f"] - p["beta_d"])
        _, chord = reconstruct_r3(p, g)
        assert abs(flat / table - 1) < 0.005
        assert abs(chord / flat - 1) < 1e-4


def test_printed_eq27_inconsistent_with_closed_orbit_geometry():
    """Eq. (2.7) as printed, r3 = r2 cos βD − ρD (1 − cos θD cos γD), gives 939.2 m (stage 1) and 5219.7 m
    (stage 4), whereas the independent 3D construction of the same half-cell gives 952.98 m and 5569.95 m.
    The variant r2 cos βD − ρD (1 − cos θD) cos γD reproduces the construction, so the printed form most likely
    contains a typographical error. No parameter record uses eq. (2.7)."""
    for p, printed_expect, r3_expect in ((STAGE1, 939.18, 952.98), (STAGE4, 5219.65, 5569.95)):
        g = closed_orbit(p)
        printed = g["r2"] * math.cos(p["beta_d"]) - g["rho_d"] * (1 - math.cos(g["theta_d"]) * math.cos(g["gamma_d"]))
        variant = g["r2"] * math.cos(p["beta_d"]) - g["rho_d"] * (1 - math.cos(g["theta_d"])) * math.cos(g["gamma_d"])
        r3, _ = reconstruct_r3(p, g)
        assert abs(printed - printed_expect) < 0.05
        assert abs(r3 - r3_expect) < 0.05
        assert abs(variant / r3 - 1) < 1e-6
        assert abs(printed / r3 - 1) > 0.01
