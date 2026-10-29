"""Lead arithmetic (P1) for the IMCC reference parameters of MuCol Milestone Report 7 (SRC_ARXIV_2510_27437,
arXiv:2510.27437v1, 'Consolidated Parameters Report', 3 Nov 2025): Table 1.1 (PDF p. 13) and Table A.1 (PDF p. 37) for
the 3 TeV and 10 TeV stages, and the luminosity model of Appendix A.1 (PDF pp. 37-39, eqs. A.1-A.13). These are
analogue values (IMCC μ+μ− collider), not LHμC values. The decay factor of eqs. (A.6)-(A.7) averages N² over a cycle
because both beams decay; for μp only the muon beam decays, which the last test quantifies."""
import math

import lhmuc.analytical as an

E_CHARGE = 1.602176634e-19
GEV_TO_KG = 1.78266192e-27

STAGES = {   # Table A.1: E_cm [TeV], C [km], N [1e12], f_r [Hz], P_coll [MW], beta* [mm], sigma [um], N_turn
    3: dict(e_beam_gev=1500.0, c_km=4.5, n=2.2e12, f_r=5.0, p_mw=5.3, beta_mm=5.0, sigma_um=3.0, n_turn=1039),
    10: dict(e_beam_gev=5000.0, c_km=11.4, n=1.8e12, f_r=5.0, p_mw=14.4, beta_mm=1.5, sigma_um=0.9, n_turn=1363),
}
EPS_N = 25e-6   # Table A.1, normalised rms transverse emittance [m]


def _f_decay_two_beams(e_gev: float, f_r: float) -> float:
    """Eq. (A.7): <N²>/N0² over one cycle T_r = 1/f_r when both colliding bunches decay."""
    x = f_r * an.tau_lab_s(e_gev)
    return x / 2 * (1 - math.exp(-2 / x))


def _f_decay_one_beam(e_gev: float, f_r: float) -> float:
    """The same average for <N> (one decaying beam against a stable one, as in μp): x (1 − e^{−1/x})."""
    x = f_r * an.tau_lab_s(e_gev)
    return x * (1 - math.exp(-1 / x))


def test_mr7_beam_power_is_two_n_e_fr():
    """Table A.1 beam power P_coll = 2 N E f_r (both beams, one bunch each): 14.4 MW at 10 TeV, 5.3 MW at 3 TeV. Table 6.1
    (PDF p. 20) prints the per-beam half for 10 TeV, 'Injected beam power per beam' 7.2 MW = N E f_r (computed 7.21)."""
    for s in STAGES.values():
        p_mw = 2 * s["n"] * s["e_beam_gev"] * 1e9 * E_CHARGE * s["f_r"] / 1e6
        assert abs(p_mw / s["p_mw"] - 1) < 0.01
    s10 = STAGES[10]
    assert abs(s10["n"] * s10["e_beam_gev"] * 1e9 * E_CHARGE * s10["f_r"] / 1e6 / 7.2 - 1) < 0.005


def test_mr7_ip_beam_size_from_emittance_and_beta_star():
    """Table A.1 IP beam size σ = √(β* ε_n/γ): 0.9 µm at 10 TeV (β* 1.5 mm), 3 µm at 3 TeV (β* 5 mm)."""
    for s in STAGES.values():
        sigma_um = an.sigma_from_emittance(EPS_N, s["beta_mm"] * 1e-3, s["e_beam_gev"], an.M_MU_GEV) * 1e6
        assert abs(sigma_um / s["sigma_um"] - 1) < 0.02


def test_mr7_luminosity_lifetime_in_turns():
    """Table A.1 luminosity lifetime N_turn = γτc/(2C) (luminosity ∝ N², so half the beam lifetime): 1363 turns at
    10 TeV in 11.4 km (computed 1367, 0.3 %) and 1039 at 3 TeV in 4.5 km (computed 1039)."""
    for s in STAGES.values():
        n_turn = an.tau_lab_s(s["e_beam_gev"]) * an.C_M_S / (2 * s["c_km"] * 1e3)
        assert abs(n_turn / s["n_turn"] - 1) < 0.005


def test_mr7_hourglass_factor_for_beta_star_equal_bunch_length():
    """A.1, PDF p. 37-38: 'The hourglass effect reduces the luminosity by a factor 0.76 for round beams with the
    beta-function and the rms bunch length being equal'; closed form √π u e^{u²} erfc(u) at u = β*/σ_z = 1 gives
    0.7579, and the numerical double integral of lhmuc.analytical.hourglass_factor agrees. Section 6 (PDF p. 19) prints
    the same factor to three digits for β* = σ_z = 1.5 mm: 'fhg = 0.758'."""
    closed = math.sqrt(math.pi) * math.e * math.erfc(1.0)
    assert abs(closed - 0.76) < 0.005
    assert round(closed, 3) == 0.758
    eps_geo = EPS_N / an.gamma(5000.0)
    numeric = an.hourglass_factor(1.5e-3, 1.5e-3, 1.5e-3, 1.5e-3, 1.5e-3, 1.5e-3, eps_geo, eps_geo, eps_geo, eps_geo)
    assert abs(numeric / closed - 1) < 2e-3


def test_mr7_decay_factor_eq_a7_at_10_tev():
    """Eq. (A.7) with γτ_μ0 = 0.104 s and f_r = 5 Hz: F_decay = 0.254 (both beams decay)."""
    assert abs(_f_decay_two_beams(5000.0, 5.0) - 0.254) < 0.001


def test_mr7_analytic_luminosity_eq_a9():
    """Eq. (A.9) with the PDF p. 39 inputs (N0 1.8e12, ε_n 25 µm, ε_l 0.025 eVs, B_avg 10.5 T, E 5 TeV, σ_E/E 0.1 %,
    F_HG(1) 0.76, f_r 5 Hz, β* = σ_z = 1.5 mm) 'yields L ≈ 18.8 × 10^34 cm^-2 s^-1'; computed 18.9e34. Written as
    eq. (A.8): f0 = eB_avg/(2πγm) (C = 9.98 km for B_avg 10.5 T at 5 TeV), σ_z = c ε_l/((σ_E/E) E)."""
    gam = an.gamma(5000.0)
    f0 = E_CHARGE * 10.5 / (2 * math.pi * gam * an.M_MU_GEV * GEV_TO_KG)
    sigma_z = an.C_M_S * 0.025 / (1e-3 * 5000e9)
    assert abs(sigma_z / 1.5e-3 - 1) < 1e-3
    lum_m2 = (1.8e12 ** 2 * f0 * gam / (4 * math.pi * sigma_z * EPS_N)) * 0.76 * _f_decay_two_beams(5000.0, 5.0)
    assert abs(lum_m2 / 1e4 / 18.8e34 - 1) < 0.01
    assert abs(an.C_M_S / f0 / 1e3 - 9.98) < 0.01


def test_mr7_integrated_luminosity_per_year():
    """PDF p. 39: 1.2e7 s per year 'leads to L_int(1 year) ≈ 2.2 ab^-1' at 18.8e34 cm^-2 s^-1 (1 ab^-1 = 1e42 cm^-2)."""
    assert abs(18.8e34 * 1.2e7 / 1e42 / 2.2 - 1) < 0.03


def test_mr7_decay_factor_one_decaying_beam_exceeds_two_beam_average():
    """For μp only the muon bunch decays, so the cycle average is <N>/N0 = x(1 − e^{−1/x}) with x = f_r γτ, not
    eq. (A.7). At MR7 10 TeV (x = 0.52) the one-beam factor is 0.444, 1.75 times the 0.254 of eq. (A.7). For the MAP
    options of Kaya et al. Table 3 (1.5/3/6 TeV at 15/12/6 Hz; SRC_ARXIV_1905_05564) the ratio is 1.97/1.87/1.87: a
    luminosity scaled from a decay-averaged L_μμ (Kaya eq. 6) omits this factor, while it also inherits the μμ
    hourglass and pinch factors, which do not apply to μp — the net correction needs a dedicated μp calculation."""
    assert abs(_f_decay_one_beam(5000.0, 5.0) - 0.444) < 0.001
    assert abs(_f_decay_one_beam(5000.0, 5.0) / _f_decay_two_beams(5000.0, 5.0) - 1.745) < 0.005
    for e_gev, f_r, ratio in ((750.0, 15.0, 1.97), (1500.0, 12.0, 1.87), (3000.0, 6.0, 1.87)):
        assert abs(_f_decay_one_beam(e_gev, f_r) / _f_decay_two_beams(e_gev, f_r) - ratio) < 0.01
