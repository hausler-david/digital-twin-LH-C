"""Audit arithmetic (validation level P1): closed-form relations used to cross-check reported
LHμC / μLHC values. These are *checks*, not a beam-physics model. Constants from CODATA 2018 /
PDG 2024 (recorded in parameters/materials? no: physics constants are recorded here with source).

Sources for constants (PDG 2024 Review of Particle Physics, Physical Constants and Muon listing):
  m_mu c^2 = 105.6583755 MeV, tau_mu = 2.1969811e-6 s, c = 299792458 m/s, e = 1.602176634e-19 C.
"""
from __future__ import annotations

import math

import numpy as np
from scipy import integrate

M_MU_GEV = 0.1056583755          # GeV
TAU_MU_S = 2.1969811e-6          # s
C_M_S = 299_792_458.0            # m/s
M_P_GEV = 0.93827208816          # GeV


def gamma(e_gev: float, m_gev: float = M_MU_GEV) -> float:
    """Lorentz factor for total energy e_gev (E >> m assumed only in the sense gamma = E/m)."""
    return e_gev / m_gev


def tau_lab_s(e_gev: float) -> float:
    """Laboratory muon lifetime tau_lab = gamma * tau_mu."""
    return gamma(e_gev) * TAU_MU_S


def sqrt_s_gev(e_mu_gev: float, e_p_gev: float, exact: bool = False) -> float:
    """Centre-of-mass energy of head-on mu-p collisions.

    Approximate: 2*sqrt(E_mu*E_p) (massless, head-on). Exact: sqrt(m_mu^2 + m_p^2 + 2(E1 E2 + p1 p2)).
    """
    if not exact:
        return 2.0 * math.sqrt(e_mu_gev * e_p_gev)
    p1 = math.sqrt(e_mu_gev**2 - M_MU_GEV**2)
    p2 = math.sqrt(e_p_gev**2 - M_P_GEV**2)
    return math.sqrt(M_MU_GEV**2 + M_P_GEV**2 + 2.0 * (e_mu_gev * e_p_gev + p1 * p2))


def luminosity_naive_cm2s(f_coll_hz: float, n1: float, n2: float, sigma_x_m: float, sigma_y_m: float,
                          h_factor: float = 1.0) -> float:
    """L = f N1 N2 / (4 pi sigma_x sigma_y) * H, for equal-size round-ish beams. Units: cm^-2 s^-1."""
    return f_coll_hz * n1 * n2 / (4.0 * math.pi * sigma_x_m * sigma_y_m) * h_factor / 1e4


def brho_tm(p_gev_c: float, charge_e: int = 1) -> float:
    """Magnetic rigidity B rho [T m] = p[GeV/c] / (0.299792458 * |q|/e)."""
    return p_gev_c / (0.299792458 * abs(charge_e))


def bending_field_t(p_gev_c: float, radius_m: float) -> float:
    """Dipole field needed to bend momentum p on radius rho (uniform bending, fill factor 1)."""
    return brho_tm(p_gev_c) / radius_m


def survival_constant_energy(e_gev: float, duration_s: float) -> float:
    return math.exp(-duration_s / tau_lab_s(e_gev))


def survival_linear_ramp(e0_gev: float, e1_gev: float, duration_s: float) -> float:
    """exp(-∫ dt / (gamma(t) tau)) for a linear energy ramp e0 -> e1 over duration_s."""
    if e1_gev <= e0_gev:
        raise ValueError("e1 must exceed e0")
    integral = (M_MU_GEV / TAU_MU_S) * duration_s / (e1_gev - e0_gev) * math.log(e1_gev / e0_gev)
    return math.exp(-integral)


def survival_racetrack_booster(e_inj_gev: float, de_per_linac_gev: float, linac_length_m: float,
                               arc_length_m: float, n_turns: int, n_linacs: int = 2,
                               e_final_gev: float | None = None) -> tuple[float, float]:
    """Turn-by-turn survival in a racetrack booster: linacs with linear energy gain, arcs at
    constant energy. Returns (survival_fraction, final_energy_gev). If e_final_gev is given the
    last pass is truncated when that energy is reached (energy gain assumed uniform along linac)."""
    e = e_inj_gev
    log_surv = 0.0
    for _turn in range(n_turns):
        for _lin in range(n_linacs):
            e_next = e + de_per_linac_gev
            length = linac_length_m
            if e_final_gev is not None and e_next > e_final_gev:
                frac = (e_final_gev - e) / de_per_linac_gev
                e_next = e_final_gev
                length = linac_length_m * frac
            if e_next > e:
                t = length / C_M_S
                log_surv -= (M_MU_GEV / TAU_MU_S) * t / (e_next - e) * math.log(e_next / e)
            e = e_next
            if e_final_gev is not None and e >= e_final_gev:
                return math.exp(log_surv), e
            # arc after each linac
            log_surv -= (arc_length_m / C_M_S) / tau_lab_s(e)
    return math.exp(log_surv), e


def average_population_fraction(e_gev: float, store_time_s: float) -> float:
    """Time-averaged N/N0 of a decaying stored beam over store_time: (1 - e^{-T/tau}) tau / T."""
    tau = tau_lab_s(e_gev)
    x = store_time_s / tau
    return (1.0 - math.exp(-x)) / x


def hourglass_factor(beta_x1: float, beta_y1: float, sigma_z1: float,
                     beta_x2: float, beta_y2: float, sigma_z2: float,
                     eps_x1: float, eps_y1: float, eps_x2: float, eps_y2: float) -> float:
    """Geometric luminosity reduction for two head-on Gaussian bunches with s-dependent beam sizes
    sigma_i(s)^2 = eps_i beta_i (1 + s^2/beta_i^2). All lengths in metres, emittances geometric.
    Returns L / L(no hourglass). Numerical double integral over s and ct."""
    def sig2(eps, beta, s):
        return eps * beta * (1.0 + (s / beta) ** 2)

    def g(z, sz):
        return math.exp(-0.5 * (z / sz) ** 2) / (math.sqrt(2 * math.pi) * sz)

    smax = 6.0 * max(sigma_z1, sigma_z2)

    def integrand(ct, s):
        sx = sig2(eps_x1, beta_x1, s) + sig2(eps_x2, beta_x2, s)
        sy = sig2(eps_y1, beta_y1, s) + sig2(eps_y2, beta_y2, s)
        return g(s - ct, sigma_z1) * g(s + ct, sigma_z2) / math.sqrt(sx * sy)

    val, _ = integrate.dblquad(integrand, -smax, smax, lambda s: -smax, lambda s: smax, epsabs=0, epsrel=1e-6)
    l_full = 2.0 * val / (2.0 * math.pi)
    sx0 = eps_x1 * beta_x1 + eps_x2 * beta_x2
    sy0 = eps_y1 * beta_y1 + eps_y2 * beta_y2
    l_ref = 1.0 / (2.0 * math.pi * math.sqrt(sx0 * sy0))
    return l_full / l_ref


def luminosity_general_cm2s(f_coll_hz: float, n1: float, n2: float,
                            sigma_x1: float, sigma_y1: float, sigma_x2: float, sigma_y2: float,
                            h_factor: float = 1.0) -> float:
    """L = f N1 N2 / (2 pi sqrt(sx1^2+sx2^2) sqrt(sy1^2+sy2^2)) * H  [cm^-2 s^-1]; sizes in m."""
    return f_coll_hz * n1 * n2 / (2.0 * math.pi * math.sqrt(sigma_x1**2 + sigma_x2**2)
                                  * math.sqrt(sigma_y1**2 + sigma_y2**2)) * h_factor / 1e4


def sigma_from_emittance(eps_n_m: float, beta_m: float, e_gev: float, m_gev: float) -> float:
    """RMS beam size from normalised emittance: sigma = sqrt(eps_n beta / (beta_rel gamma))."""
    gam = e_gev / m_gev
    beta_rel = math.sqrt(1.0 - 1.0 / gam**2)
    return math.sqrt(eps_n_m * beta_m / (beta_rel * gam))


def bjorken_x_min(q2_gev2: float, sqrt_s_gev: float) -> float:
    """x_min at fixed Q^2 for inclusive DIS (y <= 1): x = Q^2 / s."""
    return q2_gev2 / sqrt_s_gev**2


__all__ = [n for n in dir() if not n.startswith("_")]
