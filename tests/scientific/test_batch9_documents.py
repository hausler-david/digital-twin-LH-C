"""Lead arithmetic (P1) for the batch-9 uploads: Bakule et al. 2013, "Measurement of muonium emission from silica
aerogel" (arXiv:1306.3810, PTEP 2013 103C01), and Cheung & Wang 2021, "Physics potential of a muon-proton collider"
(arXiv:2101.10476, μ−p). Expected values are quoted from the papers; tolerances are stated. Cheung & Wang study μ−p,
whereas LHμC collides μ+p: nothing here transfers their cross sections to LHμC."""
import math

import lhmuc.analytical as an

GEV_TO_KG = 1.78266192e-27
K_B = 1.380649e-23
M_E_GEV = 0.00051099895


# ---------------------------------------------------------------- Bakule et al. 2013
def test_bakule2013_vacuum_yield_scaling_to_jparc_beam():
    """Eq. (1), p. 10: ỹ = (δp/δp̃)(p/p̃)^3.5 y. With y = 4.8e-3 per incident muon (23 MeV/c, 2 % RMS) the paper
    obtains 9.6e-4 for the J-PARC design beam (28 MeV/c, 5 % RMS)."""
    y_jparc = 4.8e-3 * (0.02 / 0.05) * (23.0 / 28.0) ** 3.5
    assert abs(y_jparc / 9.6e-4 - 1) < 0.01


def test_bakule2013_formation_fraction_vs_beare2020_combined_significance():
    """0.52 ± 0.01 (Bakule p. 3, MuSR, three 2013 aerogel samples) vs 0.655 ± 0.018 (Beare et al. 2020): 6.6 σ with
    both uncertainties, 7.5 σ with Beare's alone. Both are measurements on different samples; the conflict is kept,
    not averaged (CONF_MUONIUM_FORMATION_FRACTION)."""
    z_combined = (0.655 - 0.52) / math.hypot(0.01, 0.018)
    assert 6.4 < z_combined < 6.8
    assert (0.655 - 0.52) / 0.018 > 7.0


def test_bakule2013_density_scaling_alpha_minus_one_point_five():
    """p. 9, Fig. 5: L = L0 (ρ/ρ0)^α with α = −1.5 'best describes the data, except for the 178 mg cm^-3 aerogel'.
    From the Table 1 central values (ρ0 = 29 mg cm^-3, L0 = 0.226 µm): 47 → 0.110 µm (table 0.118 ± 0.009 stat),
    97 → 0.037 µm (0.035 ± 0.004), 178 → 0.0149 µm, three times the measured 0.0050 µm — the stated exception."""
    def l_pred(rho):
        return 0.226 * (rho / 29.0) ** -1.5
    assert abs(l_pred(47) - 0.118) < 0.009 * 1.5
    assert abs(l_pred(97) - 0.035) < 0.004 * 1.5
    assert 2.5 < l_pred(178) / 0.0050 < 3.5


def test_bakule2013_thermal_speed_order_of_magnitude():
    """p. 5: 'the thermal velocity of muonium in vacuum is of the order of 5 mm/µs'. The one-dimensional rms speed
    sqrt(kT/m_Mu) at 295 K is 4.6 mm/µs."""
    m_mu_kg = (an.M_MU_GEV + M_E_GEV) * GEV_TO_KG
    v_1d_mm_per_us = math.sqrt(K_B * 295.0 / m_mu_kg) * 1e-3
    assert 0.5 < v_1d_mm_per_us / 5.0 < 2.0


# ---------------------------------------------------------------- Cheung & Wang 2021
def test_cheung2021_table1_centre_of_mass_energies():
    """Table I: μp-1 (E_p 7 TeV, E_μ 1 TeV) √s = 5.3 TeV; μp-2 (50 TeV, 3 TeV) √s = 24.5 TeV."""
    assert abs(an.sqrt_s_gev(1000.0, 7000.0) / 5300.0 - 1) < 0.002
    assert abs(an.sqrt_s_gev(3000.0, 50000.0) / 24500.0 - 1) < 0.002


def test_cheung2021_integrated_luminosity_from_assumed_peak():
    """p. 2: 1e33 (1e34) cm^-2 s^-1 × 1e7 s/year × 10 years = 0.1 (1) ab^-1; 1 ab^-1 = 1e42 cm^-2."""
    assert math.isclose(1e33 * 1e7 * 10 / 1e42, 0.1)
    assert math.isclose(1e34 * 1e7 * 10 / 1e42, 1.0)


def test_cheung2021_hbb_coupling_precision():
    """p. 3: Δg/g = ½ sqrt((Δσ/σ)² + δ²) with δ = sqrt(0.4² + 0.9²) % = 0.985 % (FCC-ee inputs) gives 0.69 % and
    0.50 % from Δσ/σ = 0.97 % and 0.15 %."""
    delta = math.hypot(0.4, 0.9)
    assert abs(delta - 0.985) < 0.001
    assert abs(0.5 * math.hypot(0.97, delta) - 0.69) < 0.005
    assert abs(0.5 * math.hypot(0.15, delta) - 0.50) < 0.005


def test_cheung2021_higgs_yields():
    """p. 4: SM Higgs production 'roughly 1e5 and 5e6' at μp-1 and μp-2: WW-fusion cross sections 0.978 and 5.103 pb
    (Table II) times 1e5 and 1e6 pb^-1."""
    assert 0.9e5 < 0.978 * 1e5 < 1.1e5
    assert 4.5e6 < 5.103 * 1e6 < 5.5e6


def test_cheung2021_cut_flow_reproduces_delta_sigma_band():
    """Table III cut flow with branching ratios the paper does not print (test inputs: B(h→bb̄) = 0.58, LHC Higgs
    XS WG at m_h = 125 GeV; B(Z→bb̄) = 0.1512, PDG) reproduces Δσ/σ = sqrt(Ns + Nb)/Ns of 0.97 % and 0.15 % within
    2 % and 6 %. Recorded as a band because the branching ratios are external inputs."""
    def rel(lumi_pb, sig_h, eps_h_pr, eps_sig, sig_z, eps_z_pr, eps_bgd):
        ns = lumi_pb * sig_h * 0.58 * eps_h_pr * eps_sig
        nb = lumi_pb * sig_z * 0.1512 * eps_z_pr * eps_bgd
        return 100 * math.sqrt(ns + nb) / ns
    r1 = rel(1e5, 0.978, 0.98, 0.21, 4.67, 0.99, 0.022)
    r2 = rel(1e6, 5.103, 0.91, 0.17, 25.1, 0.97, 0.018)
    assert 0.98 < r1 / 0.97 < 1.03
    assert 1.0 < r2 / 0.15 < 1.08
