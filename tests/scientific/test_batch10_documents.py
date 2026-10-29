"""Lead arithmetic (P1) for the batch-10 uploads: Kaya, Ketenoglu, Sultansoy & Zimmermann, "Luminosity and Physics
Considerations on HL-LHC and HE-LHC based µp Colliders" (arXiv:1905.05564v2; EPL 138 (2022) 24002); Beer et al. 2014,
muonium emission from laser-ablated aerogel (arXiv:1407.8248, PTEP 2014 091C01); Zhang et al., JPS Conf. Proc. 33,
011125 (2021), 1S-2S laser ionisation of muonium; Shirotori et al. 2026, J-PARC µ20 muon beamline (arXiv:2608.25374).
Expected values are quoted from the papers; tolerances follow the printed precision. Kaya et al. describe a related
machine (imported_related, not LHμC values); the J-PARC numbers are analogous technology."""
import math

import lhmuc.analytical as an

R_E_M = 2.8179403262e-15
M_E_GEV = 0.00051099895
M_PI_GEV = 0.13957039
TAU_PI_S = 2.6033e-8


def _matches_printed(value: float, printed: str) -> bool:
    """True when value rounds to the printed number (half a unit of its last printed digit)."""
    decimals = len(printed.split(".")[1]) if "." in printed else 0
    return abs(value - float(printed)) <= 0.5 * 10.0 ** -decimals + 1e-12


# ---------------------------------------------------------------- Kaya et al. (EPL 138, 24002)
N_MU = 2e12                                   # Table 3, bunch population
MC = {0.75: (5.9, 1.25e34, 0.01), 1.5: (2.95, 4.4e34, 0.005), 3.0: (1.48, 12e34, 0.0025)}
"""Muon-collider option keyed by E_μ [TeV] (Table 3, √s = 2 E_μ): σ_μ [µm], average L_μμ [cm^-2 s^-1], β* [m]."""
PROTONS = {                                   # E_p [TeV], N_p, σ_p [µm], ε_N [µm], β* [m]
    ("HL-LHC", "nominal"): (7.0, 2.2e11, 7.1, 2.5, 0.15),      # Table 1
    ("HL-LHC", "upgraded"): (7.0, 2.2e11, 4.45, 2.0, 0.07),    # Table 2 (ERL60 ⊗ HL-LHC)
    ("HE-LHC", "nominal"): (13.5, 2.2e11, 9.0, 2.5, 0.45),     # Table 1
    ("HE-LHC", "upgraded"): (13.5, 2.5e11, 4.17, 2.5, 0.10),   # Table 2 (ERL60 ⊗ HE-LHC)
}
TABLE_L = {                                   # Tables 4-5, units of 1e33 cm^-2 s^-1
    ("HL-LHC", "nominal"): {0.75: "0.95", 1.5: "0.84", 3.0: "0.57"},
    ("HL-LHC", "upgraded"): {0.75: "1.4", 1.5: "2.1", 3.0: "1.5"},
    ("HE-LHC", "nominal"): {0.75: "0.59", 1.5: "0.52", 3.0: "0.36"},
    ("HE-LHC", "upgraded"): {0.75: "1.6", 1.5: "2.8", 3.0: "1.9"},
}


def _kaya_eq6(n_p: float, sigma_p_um: float, e_mu_tev: float) -> float:
    """Eq. (6), p. 4: L_μp = (N_p/N_μ) (σ_μ / max[σ_p, σ_μ])² L_μμ, with N_μ and L_μμ of Table 3."""
    sigma_mu, l_mumu, _ = MC[e_mu_tev]
    return (n_p / N_MU) * (sigma_mu / max(sigma_p_um, sigma_mu)) ** 2 * l_mumu


def test_kaya2022_centre_of_mass_energies_tables_4_5():
    """Tables 4-5: √s = 2√(E_μ E_p) with E_p = 7 (HL-LHC) and 13.5 TeV (HE-LHC), within 0.3 %, the precision of the
    printed three significant figures (12.73 TeV is printed as 12.7 and 9.165 TeV as 9.16)."""
    printed = {(7.0, 0.75): 4.58, (7.0, 1.5): 6.48, (7.0, 3.0): 9.16,
               (13.5, 0.75): 6.36, (13.5, 1.5): 9.0, (13.5, 3.0): 12.7}
    for (e_p, e_mu), s in printed.items():
        assert abs(an.sqrt_s_gev(e_mu * 1e3, e_p * 1e3) / 1e3 / s - 1) < 3e-3, (e_p, e_mu)


def test_kaya2022_eq6_reproduces_all_twelve_luminosities():
    """All 12 entries of Tables 4-5 follow from eq. (6) with the inputs of Tables 1-3 (nominal: Table 1 protons;
    upgraded: Table 2 protons). Example: HL-LHC nominal, E_μ = 3 TeV: 0.11 × (1.48/7.1)² × 1.2e35 = 0.574e33."""
    for key, row in TABLE_L.items():
        _, n_p, sigma_p, _, _ = PROTONS[key]
        for e_mu, printed in row.items():
            assert _matches_printed(_kaya_eq6(n_p, sigma_p, e_mu) / 1e33, printed), (key, e_mu)


def test_kaya2022_beam_sizes_follow_from_emittance_and_beta_star():
    """σ = √(ε_N β*/γ). Muon sizes of Table 3 (5.9, 2.95, 1.48 µm) within 1 %; proton sizes of Tables 1-2 within 3 %:
    7.09 (7.1), 8.84 (9), 4.17 (4.17) µm, but HL-LHC upgraded gives 4.33 µm for the printed 4.45 µm (2.7 % below,
    i.e. the printed size corresponds to ε_N ≈ 2.1 µm or β* ≈ 7.4 cm). Immaterial for Tables 4-5 at this precision."""
    for e_mu, (sigma_mu, _, beta) in MC.items():
        s = math.sqrt(25e-6 * beta / an.gamma(e_mu * 1e3)) * 1e6
        assert abs(s / sigma_mu - 1) < 0.01, e_mu
    for key, (e_p, _, sigma_p, eps, beta) in PROTONS.items():
        s = math.sqrt(eps * 1e-6 * beta / an.gamma(e_p * 1e3, an.M_P_GEV)) * 1e6
        assert abs(s / sigma_p - 1) < 0.03, key
    hl_up = PROTONS[("HL-LHC", "upgraded")]
    s_hl_up = math.sqrt(2.0e-6 * 0.07 / an.gamma(7e3, an.M_P_GEV)) * 1e6
    assert 0.02 < 1 - s_hl_up / hl_up[2] < 0.03


def test_kaya2022_table6_tune_shifts_from_eqs_9_10():
    """Table 6, p. 5, matched beams: ξ_p = N_μ r_p/(4π ε_N,p), ξ_μ = N_p r_μ/(4π ε_N,μ) with the printed
    r_p = 1.54e-18 m, r_μ = 1.37e-17 m, N_μ = 2e12, ε_N,μ = 25 µm and the proton N_p, ε_N of Tables 1-2."""
    printed = {("HL-LHC", "nominal"): ("0.098", "0.0096"), ("HL-LHC", "upgraded"): ("0.12", "0.0096"),
               ("HE-LHC", "nominal"): ("0.098", "0.0096"), ("HE-LHC", "upgraded"): ("0.098", "0.011")}
    for key, (xi_p_txt, xi_mu_txt) in printed.items():
        _, n_p, _, eps_p, _ = PROTONS[key]
        xi_p = N_MU * 1.54e-18 / (4 * math.pi * eps_p * 1e-6)
        xi_mu = n_p * 1.37e-17 / (4 * math.pi * 25e-6)
        assert _matches_printed(xi_p, xi_p_txt), key
        assert _matches_printed(xi_mu, xi_mu_txt), key


def test_kaya2022_classical_radii_as_printed():
    """p. 3-4: r_p = 1.54e-18 m and r_μ = 1.37e-17 m; r_e m_e/m gives 1.535e-18 and 1.363e-17 m (printed values 0.3 %
    and 0.5 % high)."""
    r_p = R_E_M * M_E_GEV / an.M_P_GEV
    r_mu = R_E_M * M_E_GEV / an.M_MU_GEV
    assert abs(1.54e-18 / r_p - 1) < 0.006
    assert abs(1.37e-17 / r_mu - 1) < 0.006


def test_kaya2022_table6_presumes_matched_beam_sizes():
    """Eq. (7) ξ_p = N_μ r_p β*_p/(4π γ_p σ_μ²) equals eq. (9) only when σ_μ = σ_p = √(ε_N β*/γ). For HL-LHC nominal with
    the muon collider's own σ_μ = 1.48 µm (E_μ = 3 TeV, Table 3) eq. (7) gives ξ_p ≈ 2.3, 23 times Table 6. Table 6
    therefore assumes the muon beam is enlarged to the proton size, which leaves eq. (6) unchanged because it
    depends only on max[σ_p, σ_μ]."""
    e_p, _, _, eps, beta = PROTONS[("HL-LHC", "nominal")]
    g_p = an.gamma(e_p * 1e3, an.M_P_GEV)
    sigma_matched = math.sqrt(eps * 1e-6 * beta / g_p)

    def xi_p_eq7(sigma_mu_m):
        return N_MU * 1.54e-18 * beta / (4 * math.pi * g_p * sigma_mu_m ** 2)

    def l_eq1(sigma_p_m, sigma_mu_m):          # eq. (1), round beams, per unit N_μ N_p f
        return 1.0 / (4 * math.pi * max(sigma_p_m, sigma_mu_m) ** 2)

    assert abs(xi_p_eq7(sigma_matched) / (N_MU * 1.54e-18 / (4 * math.pi * eps * 1e-6)) - 1) < 1e-9
    assert 2.1 < xi_p_eq7(1.48e-6) < 2.4
    assert math.isclose(l_eq1(7.1e-6, 1.48e-6), l_eq1(7.1e-6, 7.1e-6))


def test_kaya2022_max_convention_vs_gaussian_overlap():
    """Eq. (1) divides by 4π max[σ_p,σ_μ]² (round beams); the Gaussian overlap integral divides by 2π(σ_p² + σ_μ²).
    The ratio 2 max²/(σ_p² + σ_μ²) is 1 for matched beams and approaches 2 for very unequal ones: 1.92 for HL-LHC
    nominal with E_μ = 3 TeV (7.1 vs 1.48 µm). Kaya's tables are therefore the matched-beam luminosities. The same
    ratio is the AloHEP L_geo/L_nom relation (MACHINE_ALOHEP_LGEO_FROM_LNOM_RELATION_DAGLI2026); for the muon-ion
    collider's LHmuC column (σ_μ = 3 µm, σ_p = 7.1 µm) it is the 1.70 quoted in CONF_LUMI_MODEL_ASSUMPTIONS."""
    def ratio(sp, sm):
        return 2 * max(sp, sm) ** 2 / (sp ** 2 + sm ** 2)

    assert ratio(7.1, 7.1) == 1.0
    assert 1.90 < ratio(7.1, 1.48) < 1.93
    assert abs(ratio(7.1, 3.0) - 1.70) < 0.005
    assert all(1.0 <= ratio(sp, sm) < 2.0 for sp in (4.17, 4.45, 7.1, 9.0) for sm in (1.48, 2.95, 5.9))


def test_kaya2022_luminosity_scales_with_proton_beam_beam_parameter():
    """p. 5: 'ξp values should be reduced by an order … this can be handled by decrease of Nµ and/or increase of
    normalized emittance of proton beam, resulting in corresponding decrease of luminosity.' For matched beams
    L = N_μ N_p f/(4π σ²) with σ² = ε_N β*/γ_p and ξ_p = N_μ r_p/(4π ε_N), so L/ξ_p = N_p f γ_p/(r_p β*) does not depend
    on N_μ or ε_N: a tenfold lower ξ_p means a tenfold lower luminosity. Eq. (1) is linear in N_μ (eq. 6 is too, since
    L_μμ ∝ N_μ² by eq. 4). Applied to the ten options of Tables 4-5 whose eq.-(6) value is the matched-beam luminosity
    (σ_μ ≤ σ_p), the beam-beam-compatible values are 0.036-0.28e33."""
    e_p, n_p, _, _, beta = PROTONS[("HL-LHC", "nominal")]
    g_p = an.gamma(e_p * 1e3, an.M_P_GEV)
    f = 1.0                                    # any effective collision frequency; it cancels in the ratio

    def l_over_xi(n_mu, eps_n):
        sigma2 = eps_n * beta / g_p
        return (n_mu * n_p * f / (4 * math.pi * sigma2)) / (n_mu * 1.54e-18 / (4 * math.pi * eps_n))

    ref = l_over_xi(2e12, 2.5e-6)
    assert math.isclose(l_over_xi(2e11, 2.5e-6), ref, rel_tol=1e-12)
    assert math.isclose(l_over_xi(2e12, 25e-6), ref, rel_tol=1e-12)
    reduced = [_kaya_eq6(PROTONS[k][1], PROTONS[k][2], e) / 10 / 1e33
               for k, row in TABLE_L.items() for e in row if MC[e][0] <= PROTONS[k][2]]
    assert len(reduced) == 10
    assert 0.03 < min(reduced) and max(reduced) < 0.29


# ---------------------------------------------------------------- Beer et al. 2014 (PTEP 2014 091C01)
BEER_TABLE1 = {"flat": (3.72, 0.11), "flat_bakule2013": (2.74, 0.11),
               500: (16.0, 0.2), 400: (20.9, 0.7), 300: (30.5, 0.3)}
"""Table 1, p. 5: Mu yield in vacuum regions 1-3 (10-40 mm) per 1e3 muon stops, statistical errors."""


def test_beer2014_enhancement_at_least_eightfold():
    """Abstract and p. 6: 'at least eight times higher' for 300 µm pitch. Table 1: 30.5/3.72 = 8.20 ± 0.26 (stat);
    adding the stated systematics (≈4 % ablated, ≈1 % flat) gives ± 0.42. Yield rises as the pitch falls."""
    (y300, e300), (yf, ef) = BEER_TABLE1[300], BEER_TABLE1["flat"]
    r = y300 / yf
    stat = r * math.hypot(e300 / y300, ef / yf)
    total = r * math.sqrt((e300 / y300) ** 2 + (ef / yf) ** 2 + 0.04 ** 2 + 0.01 ** 2)
    assert 8.0 < r < 8.5
    assert 0.24 < stat < 0.28 and 0.39 < total < 0.45
    assert BEER_TABLE1[300][0] > BEER_TABLE1[400][0] > BEER_TABLE1[500][0] > BEER_TABLE1["flat"][0]


def test_beer2014_flat_sample_vs_bakule2013():
    """p. 5: 'The Mu yield from the flat sample is about 40% higher than that in Ref. [7]' — 3.72/2.74 = 1.36."""
    assert 1.3 < BEER_TABLE1["flat"][0] / BEER_TABLE1["flat_bakule2013"][0] < 1.4


def test_beer2014_vs_beare2020_reused_400um_target():
    """The 400 µm-pitch target of Table 1 (20.9 ± 0.7 ‰) was re-measured at TRIUMF in 2017 as Beare et al. 2020 target
    S2013-1, 'Reuse of O2013-3' (Table 1 p. 6; Table 4 p. 18: 17.2 ± 0.2 ‰): 18 % lower, 5.1 σ with statistical errors
    only, 1.6 σ when the stated systematics are added in the direction that closes the gap (this paper ≈ 4 %, p. 5;
    Beare −7 % / +12 %, p. 19). Recorded as CONF_ABLATED_AEROGEL_REMEASUREMENT, not averaged."""
    a, sa, b, sb = 20.9, 0.7, 17.2, 0.2
    assert 0.17 < 1 - b / a < 0.19
    assert 5.0 < (a - b) / math.hypot(sa, sb) < 5.2
    total = math.sqrt(sa ** 2 + (0.04 * a) ** 2 + sb ** 2 + (0.12 * b) ** 2)
    assert 1.5 < (a - b) / total < 1.7


def test_beer2014_fabrication_and_projection_arithmetic():
    """p. 3: 800 pulses at 1 kHz = 0.8 s per hole. p. 6: the projected 0.2e6 ultra-slow µ+/s is 'five times smaller
    than the design intensity' (order 1e6 s^-1, p. 2)."""
    assert math.isclose(800 / 1e3, 0.8)
    assert math.isclose(1e6 / 0.2e6, 5.0)


# ---------------------------------------------------------------- Zhang et al. 2021 (JPS Conf. Proc. 33, 011125)
ZHANG_TABLE_I = [("stopping", 0.467, 1.1e6), ("formation", 0.52, 5.8e5), ("vacuum yield", 0.082, 4.8e4),
                 ("laser ionisation", 3.9e-7, 0.0186), ("slow beamline", 0.651, 0.0121), ("MCP", 0.90, 0.0109)]
"""Table I, p. 6: step, efficiency, event rate [s^-1]; the chain starts from 2.4e6 s^-1 at S2."""


def test_zhang2021_table1_rates_follow_from_efficiencies():
    """Each Table I rate is the previous rate times the step efficiency (within the printed 2-3 digits); the final
    0.0109 s^-1 ('about 0.011/s', p. 6) is 4.6e-9 per surface muon at S2."""
    rate = 2.4e6
    for step, eff, printed in ZHANG_TABLE_I:
        rate *= eff
        assert abs(rate / printed - 1) < 0.03, step
    assert 4.4e-9 < rate / 2.4e6 < 4.7e-9


def test_zhang2021_laser_ionisation_factorises():
    """p. 4: 1S→2S probability 8.8e-7 and 2S→ionisation about 44 % give 'about 3.9×10^-7 per yield Mu'."""
    assert abs(8.8e-7 * 0.44 / 3.9e-7 - 1) < 0.01


def test_zhang2021_internal_inconsistencies_recorded():
    """Recorded, not resolved: S2 intensity 2.4e5 (§2, p. 3) vs 2.4e6 (§5 and Table I, p. 6) — a factor 10; stopping
    44.3 % (p. 3) vs 0.467 (Table I); extraction 1.5e3/2.0e3 = 0.75 reach the MCP, stated transmission 58.6 % = 0.651 ×
    0.90 (Table I), while the named factors 0.87 × 0.85 × 0.90 give 0.666."""
    assert math.isclose(2.4e6 / 2.4e5, 10.0)
    assert abs(0.467 / 0.443 - 1) > 0.05
    assert math.isclose(1.5e3 / 2.0e3, 0.75)
    assert abs(0.651 * 0.90 - 0.586) < 0.001
    assert abs((1 - 0.13) * 0.85 * 0.90 - 0.666) < 0.001


def test_zhang2021_244nm_demonstrator_vs_122nm_design_ionisation():
    """The 244 nm demonstrator estimate (3.9e-7 per vacuum Mu, p. 4) is 1.9e6 times below the 73 % ionisation
    efficiency of the 122 nm + 355 nm design budget (SOURCE_LASER_IONISATION_EFF_122NM_BUDGET_WS2026_ZHANG)."""
    assert 1.8e6 < 0.73 / 3.9e-7 < 1.95e6


# ---------------------------------------------------------------- Shirotori et al. 2026 (arXiv:2608.25374)
def _muon_momentum_fraction(p_pi_gev: float, cos_theta_star: float) -> float:
    """Lab momentum of the muon from π → μν over the pion momentum, for CM emission angle θ* (exact kinematics)."""
    e_star = (M_PI_GEV ** 2 + an.M_MU_GEV ** 2) / (2 * M_PI_GEV)
    p_star = (M_PI_GEV ** 2 - an.M_MU_GEV ** 2) / (2 * M_PI_GEV)
    e_pi = math.hypot(p_pi_gev, M_PI_GEV)
    g, gb = e_pi / M_PI_GEV, p_pi_gev / M_PI_GEV
    p_long = gb * e_star + g * p_star * cos_theta_star
    p_trans = p_star * math.sqrt(1 - cos_theta_star ** 2)
    return math.hypot(p_long, p_trans) / p_pi_gev


def test_shirotori2026_backward_decay_momentum_fraction():
    """p. 6: 'pµ = (m²µ/m²π)pπ ∼ 0.57pπ in the relativistic limit'; exact kinematics at 3-10 GeV/c agree within 0.2 %.
    p. 6: cτ_π 'approximately 7.8 m'."""
    r = (an.M_MU_GEV / M_PI_GEV) ** 2
    assert abs(r - 0.57) < 0.005
    for p in (3.0, 5.0, 10.0):
        assert abs(_muon_momentum_fraction(p, -1.0) / r - 1) < 0.002
    assert abs(an.C_M_S * TAU_PI_S - 7.8) < 0.05


def test_shirotori2026_ninety_degree_point_is_not_85_percent():
    """p. 10: 85 % 'corresponds to the laboratory momentum of muons emitted at 90° in the center-of-mass frame'.
    Two-body kinematics give (1 + m_μ²/m_π²)/2 = 0.787 at θ* = 90° for 3-10 GeV/c pions, not 0.85 (recorded in the
    source registry; the measured intensities and purities are unaffected)."""
    for p in (3.0, 5.0, 10.0):
        x90 = _muon_momentum_fraction(p, 0.0)
        assert abs(x90 - 0.787) < 0.002
        assert 0.85 - x90 > 0.06


def test_shirotori2026_headline_values_match_tables():
    """Abstract: 1.7e3 particles/spill and purity 98.0 ± 0.6 % for the 3 GeV/c mode = Table 2 and Table 3 at 5 GeV/c
    upstream × 60 %. Tables 2-3 show the trade-off stated on p. 19: intensity rises and purity falls with the
    downstream scaling factor at every upstream momentum. Spill 2 s per 4.24 s cycle (p. 4)."""
    intensity = {3: (0.42, 0.64, 1.0, 2.0), 5: (1.7, 2.6, 3.7, 8.3), 10: (2.4, 4.6, 6.6, 17.0)}
    purity = {3: (90.2, 85.2, 79.1, 61.4), 5: (98.0, 95.6, 90.3, 63.9), 10: (98.3, 97.1, 95.4, 53.2)}
    assert intensity[5][0] * 1e3 == 1.7e3 and purity[5][0] == 98.0
    assert math.isclose(0.60 * 5.0, 3.0)
    for p in intensity:
        assert list(intensity[p]) == sorted(intensity[p])
        assert list(purity[p]) == sorted(purity[p], reverse=True)
    assert 0.47 < 2.0 / 4.24 < 0.48
