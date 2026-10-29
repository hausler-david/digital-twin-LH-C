"""P1 checks enabled by the documents uploaded in the Phase 0 addendum (2026-10-28).

Each test pins arithmetic that the lead performed on numbers quoted verbatim from an uploaded
document (page cited). They are consistency checks of the sources and of this repository's
derived statements; none is a claim about LHμC performance. Tolerances are stated; do not loosen
them without a documented investigation (CLAUDE.md §1.9)."""
import math

from lhmuc import analytical as an


def eta_max(theta_rad: float) -> float:
    """Pseudorapidity of the nozzle edge for a half-opening angle theta: eta = -ln tan(theta/2)."""
    return -math.log(math.tan(theta_rad / 2.0))


def test_nozzle_half_angle_to_eta_max_forthomme_and_imcc():
    # Forthomme, Kraków deck p.9: "conical half opening angle: 40(100) mrad → η_max ~ 4(3)"
    assert math.isclose(eta_max(0.040), 3.91, abs_tol=0.01)
    assert math.isclose(eta_max(0.100), 3.00, abs_tol=0.01)
    assert round(eta_max(0.040)) == 4 and round(eta_max(0.100)) == 3
    # MAIA arXiv:2502.00181 §III: "nozzle extends down to |η| = 2.44, corresponding to approximately 10°"
    assert math.isclose(eta_max(math.radians(10.0)), 2.44, abs_tol=0.01)


def test_imcc_nozzle_outer_surface_angles_mr7_table_g1():
    # MuCol Milestone Report 7 (arXiv:2510.27437) Table G.1, outer surface (z, r) in cm: (6, 1), (100, 17.57), (595, 55);
    # text: "Near the interaction point, the inclination amounts to 10 degrees".
    a1 = math.degrees(math.atan((17.57 - 1.0) / (100.0 - 6.0)))
    a2 = math.degrees(math.atan((55.0 - 17.57) / (595.0 - 100.0)))
    assert math.isclose(a1, 10.0, abs_tol=0.05)
    assert 4.0 < a2 < 4.6


def test_forthomme_beam_set_implied_proton_bunch_population():
    """Forthomme p.17: "Assuming 300 ns bunch spacing", "σx,y ~ 4.3µm", "Peak luminosity of 10^34 cm-2 s-1 for 40 bunches
    of 10^10 µ+", "may consider higher proton bunches population than HL-LHC's". With the naive formula (H = 1, the
    convention that reproduces the DIS2026 and μLHC tables) the stated luminosity implies a proton bunch population of
    ≈ 7.0e11, i.e. ≈ 3.2 × the HL-LHC 2.2e11 and ≈ 1/3 of the DIS2026 22e11. Recorded in CONF_PROTON_BUNCH_POPULATION_AND_NUMBER."""
    f_coll = 1.0 / 300e-9
    l_per_proton = an.luminosity_naive_cm2s(f_coll, 1e10, 1.0, 4.3e-6, 4.3e-6)
    n_p = 1e34 / l_per_proton
    assert 6.5e11 < n_p < 7.5e11, n_p
    assert 2.9 < n_p / 2.2e11 < 3.4


def test_zhang_hline_chain_and_mutristan_budget():
    # Zhang, Kraków deck p.10 "Efficiencies breakdown": 1.8e6 /s → ×0.467 → 8.4e5 → ×0.52 → 4.3e5 → ×0.082 → 3.5e4 → ×~1e-6 → 0.19 /s
    assert math.isclose(1.8e6 * 0.467, 8.4e5, rel_tol=0.01)
    assert math.isclose(1.8e6 * 0.467 * 0.52, 4.3e5, rel_tol=0.02)
    assert math.isclose(1.8e6 * 0.467 * 0.52 * 0.082, 3.5e4, rel_tol=0.03)
    # g-2 target column: 7.21e6 muonium /s → 8.24e5 ultra-slow μ+ /s implies a laser-ionisation efficiency of 0.114 (122 nm, 100 µJ)
    assert math.isclose(8.24e5 / 7.21e6, 0.114, abs_tol=0.002)
    # p.20 "Connection to μTRISTAN": 0.52 × 0.6 × 0.6 × 0.73 = 0.137 ("14 %")
    assert math.isclose(0.52 * 0.6 * 0.6 * 0.73, 0.137, abs_tol=0.001)


def test_aritome2024_measured_ultra_slow_muon_chain():
    """arXiv:2410.11367v2 (J-PARC, March–April 2024): 9.5e4 surface μ+/pulse; (4.0 ± 0.4)e-3 μ+/pulse at 5.7 keV;
    2e-3 μ+/pulse at 100 keV; stopping 38 %, muonium conversion 52 %, emission 13 %, mesh loss 19 %; the 244 nm laser was
    a spectroscopy laser (simulated ionisation efficiency 7e-6 – 6e-5). Measured per-surface-muon yields are therefore
    orders of magnitude below both the μTRISTAN budget (0.137 after stopping, Zhang p.20) and the J-PARC g-2 target column
    (8.24e5 / 3.2e8 = 2.6e-3 per surface muon, Zhang p.10). This gap is recorded as CONF_LASER_IONISATION_EFFICIENCY and as
    a top risk; it is a statement about demonstrated numbers, not a feasibility verdict on the 122 nm scheme."""
    per_surface_100kev = 2e-3 / 9.5e4
    per_surface_5p7kev = 4.0e-3 / 9.5e4
    assert math.isclose(per_surface_100kev, 2.1e-8, rel_tol=0.02)
    assert math.isclose(per_surface_5p7kev, 4.2e-8, rel_tol=0.02)
    pre_ionisation = 0.38 * 0.52 * 0.13 * (1.0 - 0.19)
    assert math.isclose(pre_ionisation, 0.0208, rel_tol=0.01)
    implied_ionisation_and_transport = per_surface_5p7kev / pre_ionisation
    assert 1.5e-6 < implied_ionisation_and_transport < 2.5e-6
    post_stopping_measured = per_surface_100kev / 0.38
    assert 1e6 < 0.137 / post_stopping_measured < 4e6
    g2_target_per_surface = 8.24e5 / 3.2e8
    assert 1.0e5 < g2_target_per_surface / per_surface_100kev < 1.5e5


def test_muonium_formation_fraction_two_values_are_incompatible():
    # Beare et al. arXiv:2006.01947 abstract: (65.5 ± 1.8) %; Zhang p.10/p.20 and the μTRISTAN budget: 0.52 "from TRIUMF measurement".
    # Origin of 0.52 identified in batch 9: Bakule et al. arXiv:1306.3810 p. 3, MuSR, 0.52 ± 0.01 for three 2013 aerogel samples.
    # This assertion uses Beare's uncertainty alone (7.5 sigma); with both uncertainties the separation is 6.6 sigma
    # (tests/scientific/test_batch9_documents.py::test_bakule2013_formation_fraction_vs_beare2020_combined_significance).
    assert abs(0.655 - 0.52) / 0.018 > 7.0   # a genuine discrepancy between two measurements (CONF_MUONIUM_FORMATION_FRACTION), not rounding


def test_nakazawa_space_charge_scaling():
    """Nakazawa p.16: 1e10 μ+/pulse = 1.6 nC, FWHM ~2 ns → I_peak ~0.75 A at the RFQ entrance; "30 mA H- ≃ 3.4 mA μ+
    (same K, same β)"; "220 larger perveance (K) scale than the original 30-mA H- RFQ"."""
    q = 1e10 * 1.602176634e-19
    assert math.isclose(q, 1.6e-9, rel_tol=0.01)
    sigma_t = 2e-9 / 2.3548                       # Gaussian with 2 ns FWHM
    i_peak = q / (sigma_t * math.sqrt(2 * math.pi))
    assert math.isclose(i_peak, 0.75, rel_tol=0.03)
    m_ratio = an.M_P_GEV / an.M_MU_GEV            # generalized perveance K ∝ I / (m β³γ³): same K, same β → I_μ = I_H m_μ/m_p
    assert math.isclose(30e-3 / m_ratio, 3.4e-3, rel_tol=0.02)
    assert math.isclose(i_peak / (30e-3 / m_ratio), 220.0, rel_tol=0.05)


def test_vffa_rigidity_and_mr7_vffa1_mean_bending_field():
    # Topp-Mugglestone p.35–36: single arc pair 70 → 500 GeV; peak dipole ~8 T (index 60 /m, excursion ~3 cm), ~10 T (index ~44 /m), relaxed < 9 T (< 30 /m, < 7 cm)
    assert math.isclose(an.brho_tm(500.0), 1668.0, rel_tol=1e-3)
    assert 160 < an.brho_tm(500.0) / 10.0 < 170 and 205 < an.brho_tm(500.0) / 8.0 < 210
    # MuCol MR7 Table F.5 vFFA1: orbit radius 953 m, extraction 0.3 TeV, peak dipole field on orbit 6.93 T → mean bending field 1.05 T
    mean_field = an.brho_tm(300.0) / 953.0
    assert math.isclose(mean_field, 1.05, abs_tol=0.01)
    assert mean_field < 6.93


def test_turns_per_lifetime_dudko_formula():
    # Dudko arXiv:2607.16904 §3.5: n = γ c τ_μ / C with "cτ_μ = 659 m"; independent of the T_rev route used in test_analytical_checks
    c_tau = an.C_M_S * an.TAU_MU_S
    assert math.isclose(c_tau, 658.6, abs_tol=0.5)
    n = an.gamma(1000.0) * c_tau / 3000.0
    assert 2070 < n < 2090
    assert math.isclose(an.gamma(2000.0) * c_tau / 6000.0, n, rel_tol=1e-9)
    assert math.isclose(an.gamma(500.0) * c_tau / 3000.0, n / 2.0, rel_tol=1e-9)


def test_muic_lhmuc_column_beam_size_acosta2022():
    # arXiv:2203.06258 LHmuC column: 1.5 TeV muons, ε_n 25 µm, β* 0.5 cm → σ ≈ 3 µm
    s = an.sigma_from_emittance(25e-6, 0.005, 1500.0, an.M_MU_GEV)
    assert math.isclose(s, 3.0e-6, rel_tol=0.02)


def test_zimmermann_rule_bunch_length_extrapolation():
    """Zimmermann slide 14 rule of thumb σ_δ σ_z ≈ 2 n_b,0 σ_δ,0 σ_z,0, with σ_z,0 = 7.7 cm (nominal LHC, LHC Project
    Report 627) and n_b,0 counted in 2.2e11 bunches (ASM_PROTON_BUNCH_LENGTH_RMS physical basis). The Forthomme-implied
    7.0e11 gives 0.19 m if the growth is shared equally between σ_δ and σ_z and 0.49 m if it all goes into length; the
    DIS2026 22e11 gives 0.34 m and 1.54 m. Audit arithmetic on a rule of thumb, not a design value."""
    for n_p, (equal_share, all_length) in ((7.0e11, (0.19, 0.49)), (22e11, (0.34, 1.54))):
        n_b0 = n_p / 2.2e11
        assert abs(0.077 * math.sqrt(2 * n_b0) - equal_share) < 0.01, n_p
        assert abs(0.077 * 2 * n_b0 - all_length) < 0.01, n_p
