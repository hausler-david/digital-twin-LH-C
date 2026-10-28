"""Lead arithmetic (P1) for the batch-7 uploads: LHeC detector/ERL paper (arXiv:2201.02436),
J-PARC g-2/EDM design (arXiv:1901.03047), μTRISTAN hybrid target (arXiv:2605.25580) and the
AloHEP luminosity code paper (arXiv:2610.09839). Every expected value is quoted from the document
named in the test; tolerances are stated explicitly. These tests pin the cross-checks cited by the
parameter records' validation.methods; they are not performance claims for LHμC."""
import math

import lhmuc.analytical as an

GEV_PER_TM = 0.299792458  # B rho [T m] = p [GeV/c] / 0.299792458
E_CHARGE = 1.602176634e-19


# ---------------------------------------------------------------- LHeC (André et al. 2022)
def test_andre2022_magnetic_rigidities():
    """p. 15: (Bρ)_p = 23 333 T m, (Bρ)_e = 167 T m for 7 TeV protons and 50 GeV electrons."""
    brho_p = 7000.0 / GEV_PER_TM
    brho_e = 50.0 / GEV_PER_TM
    assert abs(brho_p / 23333.0 - 1) < 2e-3  # 23 349.5 T m vs 23 333 (0.07 %)
    assert abs(brho_e / 167.0 - 1) < 5e-3  # 166.8 T m


def test_andre2022_table2_current_from_charge_and_spacing():
    """Table 2: 499 pC at 24.95 ns spacing must give the 20 mA electron current."""
    i_ma = 499e-12 / 24.95e-9 * 1e3
    assert abs(i_ma / 20.0 - 1) < 5e-3
    n_e = 499e-12 / E_CHARGE
    assert 3.0e9 < n_e < 3.2e9  # electrons per bunch, not stated in the paper


def test_andre2022_table3_synchrotron_scaling_between_arcs():
    """Table 3: arc 5 (41.75 GeV: 354.8 keV, 5.87 MW) vs arc 6 (50 GeV: 609.3 keV, 12.17 MW).
    Same bending radius, so E_c ∝ E^3 and P ∝ E^4."""
    r = 50.0 / 41.75
    assert abs((609.3 / 354.8) / r**3 - 1) < 0.01
    assert abs((12.17 / 5.87) / r**4 - 1) < 0.01


def test_andre2022_table4_luminosity_with_hl_lhc_proton_parameters_recorded_band():
    """Table 4 quotes 8.2e33 cm^-2 s^-1. The paper does not list the proton bunch population or
    emittance used; with HL-LHC nominal protons (2.2e11, ε_n 2.5 µm, γ 7461), β* = 10.0 / 10.9 cm
    (Fig. 19) and the Table 2 electron beam, the naive formula gives ≈ 6e33. The ratio is recorded
    as a band (0.5–1.5), not a reproduction: the proton inputs are not in the paper."""
    n_e = 499e-12 / E_CHARGE
    f = 1.0 / 24.95e-9
    gamma_p = 7000.0 / an.M_P_GEV
    sx = math.sqrt(0.100 * 2.5e-6 / gamma_p)
    sy = math.sqrt(0.109 * 2.5e-6 / gamma_p)
    lum = an.luminosity_naive_cm2s(f, n_e, 2.2e11, sx, sy)
    ratio = lum / 8.2e33
    assert 0.5 < ratio < 1.5
    assert 0.65 < ratio < 0.85  # recorded value ≈ 0.75; a change here means an input changed


# ---------------------------------------------------------------- J-PARC g-2/EDM (Abe et al. 2019)
def test_abe2019_fig4_thermal_muonium_efficiency_decomposition():
    """Fig. 4 caption: 0.0034 = 0.52 × 2.1e4 / 3.23e6."""
    assert abs(0.52 * 2.1e4 / 3.23e6 - 0.0034) < 1e-4


def test_abe2019_table4_overall_efficiency_product():
    """Table 4 breakdown multiplies to the stated 1.3e-5 detected e+ per initial muon."""
    effs = [0.16, 0.0034, 0.73, 0.78, 0.72, 0.95, 0.81, 0.99, 0.99, 1.00, 0.96, 1.00, 0.99, 0.85,
            0.99, 0.93, 0.12, 1.00, 0.90]
    assert 1.2e-5 < math.prod(effs) < 1.4e-5


def test_abe2019_table2_decay_survival_through_linac():
    """Table 2 decay losses 17/19/1/4/1 % → survival ≈ 0.63 through Soa–RFQ–IH–DAW–DLS."""
    surv = math.prod(1 - x for x in (0.17, 0.19, 0.01, 0.04, 0.01))
    assert 0.62 < surv < 0.65


def test_abe2019_hline_rate_implied_by_table5_vs_quoted_1e8():
    """Table 5: 5.2e12 muons stored in 2.2e7 s. Dividing by the Table 4 efficiencies downstream of
    the H-line (Mu emission … kicker decay) implies ≈ 3e8 surface μ+/s at the H-line, against the
    text's '∼ 1e8 per second' (p. 7). The factor is recorded (1–5) as an internal-consistency
    observation of the design paper, not as a conflict."""
    post_hline = [0.0034, 0.73, 0.78, 0.72, 0.95, 0.81, 0.99, 0.99, 1.00, 0.96, 1.00, 0.99, 0.85,
                  0.99, 0.93]
    rate = 5.2e12 / (math.prod(post_hline) * 2.2e7)
    assert 1.0 < rate / 1e8 < 5.0
    assert 2.5e8 < rate < 3.5e8


def test_abe2019_vs_zhang_g2_target_chain_consistency():
    """Abe 2019: 3.4e-3 Mu emission × 0.73 ionisation = 2.5e-3 thermal μ+ per surface muon; the
    Kraków Zhang deck's H-line chain table gives 8.24e5/3.2e8 = 2.6e-3 for the g-2 target
    (tests/scientific/test_workshop_decks.py). Consistent within 10 %."""
    assert abs((0.0034 * 0.73) / (8.24e5 / 3.2e8) - 1) < 0.10


# ---------------------------------------------------------------- hybrid target (Sakaki et al. 2026)
def test_sakaki2026_diffusion_length_and_emitted_fraction():
    """Eq. (2): ℓ_diff = sqrt(D τ_μ) with D = 2e-3 cm^2/s at 2000 K → ≈ 0.7 µm (p. 4); Appendix A:
    one third of muons uniformly stopped within 3 ℓ_diff reach the surface before decay."""
    l_diff_um = math.sqrt(2e-3 * an.TAU_MU_S) * 1e4
    assert 0.6 < l_diff_um < 0.75
    assert abs((1 - math.exp(-3)) / 3 - 1 / 3) < 0.02


def test_sakaki2026_thermal_source_emittance_estimate():
    """Eq. (1): ε_n,rms ≈ σ_s sqrt(kT/mc^2); σ_s = 5 cm at room temperature → '∼ 1 π mm mrad'."""
    kT_ev = 8.617333e-5 * 293.0
    eps_mm_mrad = 50.0 * math.sqrt(kT_ev / (an.M_MU_GEV * 1e9)) * 1e3
    assert 0.5 < eps_mm_mrad < 1.5


def test_sakaki2026_pre_extraction_rate_upper_limit():
    """Eq. (5) with Table I: 6e-4 per p–Li collision × N_p = 2e15 s^-1 (1 MW, 3 GeV) → 1.2e12 s^-1
    times the unquantified conversion factor η_conv, in the one-collision-per-proton limit."""
    assert abs(6e-4 * 2e15 / 1.2e12 - 1) < 1e-9


# ---------------------------------------------------------------- AloHEP (Dağlı & Karaca 2026)
def _two_beam_decay_average(gamma_tau_s, t_store_s):
    """Store-averaged N1 N2 ∝ exp(-2t/γτ) when both beams decay."""
    x = 2 * t_store_s / gamma_tau_s
    return (1 - math.exp(-x)) / x


def _one_beam_decay_average(gamma_tau_s, t_store_s):
    x = t_store_s / gamma_tau_s
    return (1 - math.exp(-x)) / x


def test_dagli2026_mucol_10tev_decay_factor_and_turns():
    """§5.7: 5 TeV muons, γτ = 0.104 s, one repetition period 0.2 s = 5260 turns of an 11.4 km
    ring; analytic decay factor 0.254 (simulated 0.252)."""
    gamma_tau = an.tau_lab_s(5000.0)
    assert abs(gamma_tau / 0.104 - 1) < 0.01
    turns = 0.2 * an.C_M_S / 11400.0
    assert abs(turns / 5260 - 1) < 0.01
    assert abs(_two_beam_decay_average(gamma_tau, 0.2) / 0.254 - 1) < 0.01


def test_decay_averaging_differs_between_mumu_and_mup():
    """For a μp collider only one beam decays: averaging over one dilated lifetime gives
    1 − e^{-1} = 0.632 (the factor found in the μLHC luminosity audit), whereas the μ+μ− two-beam
    average over the same store is (1 − e^{-2})/2 = 0.432. The two must not be confused when
    AloHEP's analytic decay option is applied to LHμC."""
    assert abs(_one_beam_decay_average(1.0, 1.0) - 0.632) < 1e-3
    assert abs(_two_beam_decay_average(1.0, 1.0) - 0.432) < 1e-3
