"""P1 analytical checks: dimensional relations and reproduction of values quoted in the sources.
Tolerances are stated and justified; do not loosen them without a documented investigation."""
import math

import pytest

from lhmuc import analytical as an


def test_gamma_and_lifetime_1tev():
    g = an.gamma(1000.0)
    assert math.isclose(g, 9464.5, rel_tol=2e-4)            # 1000 / 0.1056583755
    assert math.isclose(an.tau_lab_s(1000.0), 20.79e-3, rel_tol=1e-3)   # "approximately 20 ms" (2506.15445 §2.3)


def test_mulhc_main_ring_turns_and_average_population():
    # 2506.15445 §2.3: 3 km ring, ~10 us per turn, ~2000 turns in a lifetime, average ~0.63 N0
    t_turn = 3000.0 / an.C_M_S
    assert math.isclose(t_turn, 10.0e-6, rel_tol=2e-3)
    n_turns = an.tau_lab_s(1000.0) / t_turn
    assert 2000 <= n_turns <= 2100
    # average over one lifetime of storage
    assert math.isclose(an.average_population_fraction(1000.0, an.tau_lab_s(1000.0)), 1 - math.exp(-1), rel_tol=1e-9)
    assert math.isclose(1 - math.exp(-1), 0.632, abs_tol=1e-3)


@pytest.mark.parametrize("e_mu,e_p,expected", [(500.0, 7000.0, 3.742), (1000.0, 7000.0, 5.292), (2000.0, 7000.0, 7.483)])
def test_sqrt_s(e_mu, e_p, expected):
    assert math.isclose(an.sqrt_s_gev(e_mu, e_p) / 1000, expected, rel_tol=1e-3)
    assert math.isclose(an.sqrt_s_gev(e_mu, e_p, exact=True), an.sqrt_s_gev(e_mu, e_p), rel_tol=1e-6)


def test_dis2026_table1_luminosity_reproduced_with_h_equal_one():
    """arXiv:2610.35154 Table 1: f=4 MHz, N_mu=0.07e11, N_p=22e11, sigma=4.8 um -> L=2.1e34.
    Reproduced by the naive formula with H=1, i.e. the published value does not include a
    hourglass/decay correction (recorded as CONF_LUMI_MODEL_ASSUMPTIONS)."""
    L = an.luminosity_naive_cm2s(4e6, 0.07e11, 22e11, 4.8e-6, 4.8e-6)
    assert math.isclose(L, 2.1e34, rel_tol=0.03)


def test_mulhc_table3_luminosity_reproduced_by_naive_formula_times_decay_average():
    """2506.15445 Tables 1-3: N_mu = 3.0e10 (ERL booster) / 3.7e10 (muTRISTAN booster), N_p = 22e10 = 2.2e11,
    f = 4 MHz, sigma_x,y = 4.3 um for both beams; reported L = 7.2e33 / 8.8e33 (AloHEP, post-erratum).
    Audit finding: both values equal the naive formula multiplied by the 1-lifetime decay average
    (1 - e^-1) = 0.632 that the paper quotes in §2.3, to better than 2%. No additional hourglass
    reduction is visible in the published numbers (recorded in CONF_LUMI_MODEL_ASSUMPTIONS)."""
    decay = 1.0 - math.exp(-1.0)
    for n_mu, reported in ((3.0e10, 7.2e33), (3.7e10, 8.8e33)):
        L = an.luminosity_naive_cm2s(4e6, n_mu, 2.2e11, 4.3e-6, 4.3e-6) * decay
        assert math.isclose(L, reported, rel_tol=0.02), (n_mu, L, reported)


def test_dis2026_proton_bunch_population_is_ten_times_hl_lhc():
    """DIS2026 Table 1 gives the proton bunch population as 22 x 10^11 (2.2e12) whereas muLHC Table 2
    and the HL-LHC baseline use 22 x 10^10 (2.2e11). The factor 10 is a real difference between the
    two documents (DIS2026 explicitly assumes fewer, more populated LHC bunches), not a unit slip:
    with 2.2e11 the DIS2026 luminosity would be 2.1e33, not the published 2.1e34."""
    L_published_inputs = an.luminosity_naive_cm2s(4e6, 0.07e11, 22e11, 4.8e-6, 4.8e-6)
    L_hl_lhc_inputs = an.luminosity_naive_cm2s(4e6, 0.07e11, 2.2e11, 4.8e-6, 4.8e-6)
    assert math.isclose(L_published_inputs / L_hl_lhc_inputs, 10.0, rel_tol=1e-9)
    assert math.isclose(L_published_inputs, 2.1e34, rel_tol=0.03)


def test_hourglass_factor_for_mulhc_like_optics():
    """Hourglass for beta_y* = 0.7 cm, beta_x* = 3 cm (muon), proton beta* 7 cm, proton bunch length
    7.5 cm (nominal LHC value, an order-of-magnitude input; the LHμC proton bunch length is 'unknown'),
    muon bunch length 2 mm. Found during the Phase 0 audit: H ~ 0.53 for these inputs. The published
    muLHC luminosities, however, are reproduced without any hourglass factor (see the test above), so
    either AloHEP used a much shorter proton bunch, relaxed muon optics, or no hourglass term: an OPEN
    item (CONF_LUMI_MODEL_ASSUMPTIONS). The band below records the computed value so an unintended
    change is detected; it is not a claim about LHμC."""
    e_mu, e_p = 1000.0, 7000.0
    eps_mu = 4e-6 / (e_mu / an.M_MU_GEV)   # geometric from normalised 4 um
    eps_p = 2e-6 / (e_p / an.M_P_GEV)
    h = an.hourglass_factor(0.03, 0.007, 0.002, 0.07, 0.07, 0.075, eps_mu, eps_mu, eps_p, eps_p)
    assert 0.50 < h < 0.57, h
    # sanity: short bunches with long beta* give H -> 1
    h1 = an.hourglass_factor(1.0, 1.0, 0.001, 1.0, 1.0, 0.001, 1e-9, 1e-9, 1e-9, 1e-9)
    assert math.isclose(h1, 1.0, abs_tol=1e-3)


def test_proton_beam_size_reproduces_mulhc_table3():
    """2506.15445 Table 2-3: eps_n = 2 um, beta* = 7 cm, 7 TeV -> sigma = 4.3 um."""
    assert math.isclose(an.sigma_from_emittance(2e-6, 0.07, 7000.0, an.M_P_GEV), 4.3e-6, rel_tol=0.02)


def test_brho_and_bending_field():
    assert math.isclose(an.brho_tm(1000.0), 3335.6, rel_tol=1e-3)
    # muTRISTAN booster: 1 km radius arcs, '3 T max' (2506.15445 §2.2.3)
    assert math.isclose(an.bending_field_t(960.0, 1000.0), 3.2, rel_tol=0.02)
    # 1 TeV main ring of 3 km circumference, if 100% filled with dipoles: rho = C/2pi
    assert math.isclose(an.bending_field_t(1000.0, 3000.0 / (2 * math.pi)), 6.99, rel_tol=0.01)


def test_booster_survival_mutristan_racetrack():
    """2506.15445 §2.2.1: 2 x 3 km linacs (30 GeV each), 1 km radius arcs, 212 MeV -> 960 GeV in 16 turns,
    'approximately 82% of the initial muon population remains'. A turn-by-turn linac/arc decay model
    should land within a few percent; the residual difference is recorded, not tuned away."""
    surv, e_final = an.survival_racetrack_booster(0.212, 30.0, 3000.0, math.pi * 1000.0, 16, n_linacs=2)
    assert math.isclose(e_final, 960.212, rel_tol=1e-3)
    assert 0.75 < surv < 0.90, surv


def test_booster_survival_erl_racetrack():
    """2506.15445 §2.2.2: LHeC ERL 2 x 1 km linacs (10 GeV each), arcs of 1 km radius (Fig. 5/6 geometry),
    212 MeV -> 1 TeV in 50 turns, 'approximately 67%'."""
    surv, e_final = an.survival_racetrack_booster(0.212, 10.0, 1000.0, math.pi * 1000.0, 50, n_linacs=2, e_final_gev=1000.0)
    assert math.isclose(e_final, 1000.0, rel_tol=1e-3)
    assert 0.55 < surv < 0.80, surv


def test_survival_linear_ramp_limits():
    # constant-energy limit: ramp over a tiny energy range equals exp(-T/tau)
    s_const = an.survival_constant_energy(1000.0, 1e-3)
    s_ramp = an.survival_linear_ramp(999.999, 1000.001, 1e-3)
    assert math.isclose(s_const, s_ramp, rel_tol=1e-6)


def test_bjorken_x_reach():
    # 2506.15445 Table 5: at Q^2 = 10 GeV^2, x = 3.6e-7 for sqrt(s)=5.3 TeV
    assert math.isclose(an.bjorken_x_min(10.0, 5300.0), 3.6e-7, rel_tol=0.02)
