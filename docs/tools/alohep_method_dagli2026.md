# AloHEP — what the code computes and how it will be used for LHμC

Method note for the AloHEP luminosity code, written from the software paper
B. Dağlı, Y. Karaca, *AloHEP Software: A luminosity optimizer for High Energy Physics colliders*,
arXiv:2610.09839v1 [physics.acc-ph], 7 Oct 2026, 45 pp (`SRC_ARXIV_2610_09839`, category
OFFICIAL_SOFTWARE_DOCUMENTATION, access uploaded, read in full on 2026-10-28). Page numbers below are
the printed page numbers of the arXiv PDF. Every number in this note is also a parameter record in
`parameters/machine/alohep_benchmarks_dagli2026.yaml` (ids `MACHINE_ALOHEP_*_DAGLI2026`, all status
`analogous` except five computed values marked `analytical_estimate`, applicability `screening_only`: *tool-benchmark value, not an LHμC design value*); the
10 TeV μ+μ− benchmark set is the scenario `ALOHEP-MUCOL-10TEV-BENCHMARK-2026`
(`parameters/machine/scenarios_batch7_alohep.yaml`, machine IMCC). The code itself has **not** been
run, installed or read in this repository; this note describes the paper, nothing more.

*Verified against the page images of the PDF by the G10 adversarial verification on 2026-10-29*
*(`research/_fragments/verify_G10_ALOHEP.md`); corrections made there are marked [verifier].*

Why it matters here: AloHEP is the code behind the μLHC luminosities 7.2×10³³ / 8.8×10³³ cm⁻²s⁻¹
(`MACHINE_PEAK_LUMINOSITY_ERL_MULHC`, `MACHINE_PEAK_LUMINOSITY_MUTRISTAN_MULHC`,
`MACHINE_LUMINOSITY_CODE_MULHC`; the paper cites the μLHC paper as its ref. [7] and the HL-LHC-based
μp luminosity paper as ref. [6], p. 4, 42) and therefore the tool named in Benchmark 3.1 of
`docs/validation_plan.md` and in the open conflict `CONF_LUMI_MODEL_ASSUMPTIONS`.

---

## 1. What the code models

### 1.1 Geometric luminosity

*Eq. (7), p. 7* — "Presuming head-on collisions between bunches of identical transverse sizes and no
change in the bunch sizes throughout the collision, integration of Eq. (4) yields the geometric
luminosity:"

> L₀ = N₁ N₂ f_c / (4π σ_x σ_y)   (7)

The simulation accumulates the luminosity slice by slice, *Eq. (14), p. 13* (transcribed from the
display):

> L = 2 N₁ N₂ f_c · c Δt / (Δx Δy Δz N_p²) · Σ_n Σ_k Σ_ij Q_ij⁽¹⁾ Q_ij⁽²⁾   (14)

"where N₁, N₂ are the bunch populations, f_c the bunch collision rate, N_p the number of
macroparticles, n each time step, k each slice, and Q_ij⁽¹⁾, Q_ij⁽²⁾ the particle distributions of the
intersecting slices. A prefactor of 10⁻⁴ converts the result from m⁻² s⁻¹ to cm⁻² s⁻¹." (p. 13).
"only the collision of two bunches need be simulated, with the total luminosity obtained by
multiplying by the bunch collision rate." (p. 11).

For **unequal beams** the reference geometric value is *Eq. (24), p. 32*:

> L_geo = N₁ N₂ f_c / [2π √(σ²_x1 + σ²_x2) √(σ²_y1 + σ²_y2)]   (24)

"which reduces to Eq. (7) for identical beams." (p. 33). **The code's own readout is not Eq. (24)** —
see §4 below (footnote 1, p. 33).

### 1.2 Hourglass effect

*Eq. (10), p. 8*: "The change in the transverse beam sizes along s is σ_t² = σ_t*² (1 + s²/β_t*²),
t = x, y." Implemented by giving each macroparticle its field-free transverse velocity and initial
offset, *Eqs. (15)–(16), p. 14–16*: "u₀ = u* − L · u₀′" (p. 16), i.e. "with the hourglass modulation
x(z) = x₀ − x′|z|" (p. 19).

Analytic reference for identical flat beams, *Eq. (22), p. 27* (transcribed):

> H(σ_z/(√2 β_y*)) = (1/√(2π)) ∫_{−∞}^{∞} e^{−u²/2} du / [ √(1 + (σ_z u/(√2 β_x*))²) · √(1 + (σ_z u/(√2 β_y*))²) ]   (22)

"with σ_z = BunLen". The √2 is explained on p. 27: "a pair of particles at intra-bunch longitudinal
positions ξ₁ and ξ₂ meets at s = (ξ₁ + ξ₂)/2, so the collision points are distributed with r.m.s.
σ_z/√2".

Analytic reference for **unequal beams**, *Eq. (23), p. 32* (transcribed):

> H = (1/√(2π)) ∫_{−∞}^{∞} e^{−u²/2} · [ √(σ*²_x1 + σ*²_x2) √(σ*²_y1 + σ*²_y2) ] / [ √(Σ_{i=1,2} σ*²_xi (1 + s²/β*²_xi)) · √(Σ_{i=1,2} σ*²_yi (1 + s²/β*²_yi)) ] du,   with s = u √(σ²_z1 + σ²_z2)/2   (23)

"in which each beam's transverse size follows its own β-function and the collision points are spread
with r.m.s. √(σ²_z1 + σ²_z2)/2 (for identical beams it reduces to Eq. (22))—captures only the
hourglass reduction" (p. 32).

### 1.3 Crossing angle (Piwinski factor)

*Eq. (11), p. 9*: "The impact of the collision angle on the luminosity of symmetric colliders [19,
23, 24] is"

> L = L₀ S,  S = 1/√(1 + Φ²),  Φ = (σ_z/σ_y) tan θ   (11)

"where θ is the half crossing angle (full angle 2θ); σ_y appears because AloHEP implements the
crossing in the longitudinal–vertical (z, y) plane (Section 3), and for round beams σ_x = σ_y so the
choice of plane is immaterial." (p. 10). Worked example, p. 10: "For the LHC, with 2θ = 285 µrad,
σ_x,y = 16.7 µm and σ_s = 7.7 cm (the example of Ref. [19]), S = 0.835, so the luminosity decreases
from 1.20 × 10³⁴ to 1.00 × 10³⁴ cm⁻² s⁻¹." Implementation, *Eq. (17), p. 16*: "A finite crossing angle
is implemented as a rigid rotation of each bunch in the longitudinal–vertical (z, y) plane, i.e. about
the horizontal x-axis, applied before the collision loop".

### 1.4 Beam–beam pinch / disruption and tune shifts

*Eq. (12), p. 10* (single-particle acceleration, transcribed):

> d²x₁/dt² = −(4 r₁ N₂/γ₁) ∬ (x₁ − x)/[(x₁ − x)² + (y₁ − y)²] ρ₂(x, y, s, s₀) dx dy   (12)

"Equation (12) is written for oppositely charged bunches, the minus sign yielding attraction; for like
charges the overall sign is reversed, following the sign of the charge product of the two beams."
(p. 10). Macroparticle form, *Eq. (21), p. 18*:

> a_x^n = −(4 r₁ N₂ / (γ₁^n N_p Δz)) F_x⁽²⁾(x_n, y_n)   (21)

"where r₁ is the classical radius of the (accelerated) beam-1 particle, γ₁^n the Lorentz factor at
step n, and F_x⁽²⁾ the interpolated force ... the code applies the overall sign − sgn(q₁q₂), so
same-charge beams are defocused" (p. 18).

Disruption parameter, p. 28: "the magnitude of the effect should grow with the disruption parameter
[30] D_y = 2ZN r₀ σ_z/[γ σ_y (σ_x + σ_y)] (with Z the charge number of the opposing bunch's particle)
... (for unit charge r₀/γ = e²/(4πε₀E), so the particle mass cancels and only the beam energy E and
the bunch geometry remain)".

Tune shifts, Table 5 caption, p. 34: "The linear beam–beam tune shifts ξ_x,y are those of the
(disrupted) electron beam, from the standard per-plane formula
ξ_t = |Z_p| N_p r_e β*_e,t / [2π γ_e σ_p,t (σ_p,x + σ_p,y)] (t = x, y); these are the values emitted by
the headless -fom output. Being analytic functions of the beam parameters, D_y and ξ_x,y are
deterministic and independent of the macroparticle sampling". Which figure of merit is reported is
set by the database tag: "tagged linear or circle according to the name of the particle folder (e.g.
electron-linac); this tag selects whether the results report disruption parameters D_x,y (linear
machines) or beam–beam tune shifts ξ_x,y (circular machines)." (p. 18–19).

### 1.5 Numerical method (p. 2–3, 11–18, Fig. 17 p. 20)

Particle-in-cell with cloud-in-cell deposition, direct Green's-function convolution for the slice
potential (Eqs. (18)–(19), p. 16), finite-difference forces at the cell faces (Eq. (20), p. 17), C¹
bicubic (Catmull–Rom) force interpolation (p. 17), first-order Euler push "v += a Δt; x += v Δt"
(Fig. 17, p. 20). Collision box, *Eq. (13), p. 11*: S_x,y = k × max[σ_x1,y1, σ_x2,y2],
S_z = k × (σ_z1 + σ_z2)/2, with "all benchmarks of Section 5 use the default k = 4, and the Gaussian
sampling of the macroparticles is truncated at ±kσ" (p. 11); "When the hourglass effect is enabled and
σ_z/β_y* > 1/2, the vertical half-size is additionally multiplied by 2σ_z/β_y*" (p. 11). Cost: "O(N_x²
N_y²) per slice repeated O(N_z²) times per crossing, i.e. O(N_g⁶) for a cubic grid" (p. 3); measured
exponents 5.1 (10→30) and 5.8 (50→100) (p. 25).

---

## 2. Which effects are toggles, and what a run returns

p. 21–22: "The Checkboxes panel (centre) enables the hourglass effect, the beam–beam pinch,
beamstrahlung and particle decay; each can be toggled independently, with the dependencies enforced
automatically (enabling pinch, hourglass or beamstrahlung turns on the macroparticle simulation, and
beamstrahlung requires the pinch). With all boxes cleared no macroparticle simulation is run: the
Matched Beams helper is applied and the analytic nominal luminosity L_nom is reported." The crossing
angle is a numeric setting ("the crossing angle (entered in radians)", p. 21), as are the grid
(N_x, N_y, N_z), the macroparticle count and k ("Scale of Sigma") (p. 21).

Outputs: "LuminosityCalc output: L_eff, L_nom, D_x,y, ξ_x,y" (Fig. 17, p. 20); the results window
"reports the centre-of-mass energy, the nominal and effective luminosities and their ratio, together
with the per-beam spot sizes σ_x,y and ... either the disruption parameters D_x,y or the beam–beam
tune shifts ξ_x,y" (p. 22).

Inputs per beam (Custom): "bunch population, beam energy, β*_x,y, normalised emittances, bunch length
and revolution frequency" (p. 21). **Not in the paper:** "the rules by which the collision frequency
and the storage time are derived from them" — "given in the repository README rather than repeated
here" (p. 21).

"Matched Beams" helper (p. 19): "equalises the transverse spot sizes by enlarging the smaller-spot
beam to the larger of the two, recomputing the β-functions from β = σ²_max/ε." This is the only
operation in the paper that matches the μLHC phrase "with beam size matched accordingly"
(`MACHINE_LUMINOSITY_CODE_MULHC`, `MACHINE_MU_BETA_STAR_MATCHED_IMPLIED_MULHC`); whether the μLHC
authors used it is not stated in either paper.

---

## 3. How the decay factor is applied

p. 36 (μ+μ−, √s = 10 TeV, MuCol baseline): "With muon decay disabled the geometric luminosity is again
recovered to ∼ 1% (three runs between 0.997 and 1.003), while enabling the decay channel (-decay)
reduces the time-integrated luminosity by the muon-survival factor over the store—a reduction to
0.252 for this configuration, against the analytic factor F_decay = 0.254 of Ref. [35]—set by the
dilated lifetime γτ = 0.104 s relative to the storage time. **The decay factor is applied
analytically, so the residual difference is the statistical scatter of the simulated geometric
luminosity.**"

Our reading [verifier]: the decay is therefore not simulated particle by particle (the paper does not say so in
those words), and the geometric (or pinch/hourglass) luminosity of the
crossing is multiplied by an analytic survival average over the store (0.2 s = 5260 turns of the
11.4 km ring, p. 36). The paper does not write the formula. The lead's test
`tests/scientific/test_batch7_documents.py::test_dagli2026_mucol_10tev_decay_factor_and_turns`
reproduces γτ = 0.104 s, 5260 turns and the value 0.254 as the **two-beam** store average
(1 − e^{−2T/γτ})/(2T/γτ) with T = 0.2 s, i.e. N₁N₂ ∝ e^{−2t/γτ} because *both* μ+μ− beams decay
(records `MACHINE_ALOHEP_MUCOL_DECAY_FACTOR_ANALYTIC_DAGLI2026`, `_SIM_`, `_GAMMA_TAU_`,
`_TURNS_PER_STORE_`).

**For a μp collider the average is different.** Only the muon beam decays, so the store average is
(1 − e^{−T/γτ})/(T/γτ): over one dilated lifetime this is 1 − e⁻¹ = 0.632 (the factor found in the
μLHC audit, `MACHINE_MU_AVERAGE_POPULATION_FRACTION_MULHC` = 0.63), whereas the μ+μ− two-beam average
over the same time is (1 − e⁻²)/2 = 0.432 —
`tests/scientific/test_batch7_documents.py::test_decay_averaging_differs_between_mumu_and_mup`. The
paper exercises decay only for the symmetric μ+μ− store; which form the code applies to an asymmetric
pair is not stated (record `MACHINE_ALOHEP_DECAY_IMPLEMENTATION_DAGLI2026`).

---

## 4. The L_nom footnote (p. 33) and its consequence for asymmetric μp beams

Footnote 1, p. 33: "The code's internal nominal-luminosity readout uses the equal-beam approximation
L_nom = N₁N₂f_c/[4π max(σ_x1, σ_x2) max(σ_y1, σ_y2)], which coincides with Eq. (24) for symmetric beams
but underestimates the geometric luminosity when the beams differ; we therefore compare against
Eq. (24) for the asymmetric cases." Appendix A, p. 39: "The two differ only by a purely geometric
factor, L_geo = L_nom · 2 max(σ_x1, σ_x2) max(σ_y1, σ_y2) / [√(σ²_x1 + σ²_x2) √(σ²_y1 + σ²_y2)]", and
"results_asymmetric.csv ... records the code's equal-beam L_nom".

Consequences for LHμC (μ+ on protons, generally unequal spots):

- The ratio L_eff/L_nom printed by the code is **not** L_eff/L_geo unless the spots are equal. For the
  HERA / EIC benchmarks the factor is only 1.0045 / 1.0034 (computed here from Table 5,
  `MACHINE_ALOHEP_HERA_LGEO_OVER_LNOM_FACTOR_DAGLI2026`, `_EIC_`), because those beams are nearly
  matched; a 3:1 spot ratio in one plane would give 2·3/√10 = 1.90.
- If the μLHC authors used the Matched Beams helper (both spots 4.3 µm: `MACHINE_IP_BEAM_SIZE_MU_ERL_MULHC`,
  `PROTON_IP_BEAM_SIZE_ERL_MULHC` and the μTRISTAN-option twins),
  L_nom = L_geo and the footnote is harmless; if the Forthomme set
  (`LHMUC-WS2026-FORTHOMME`, equal σ_x,y for both beams by construction) is run matched, the same holds.
  Any unmatched μp run must convert L_nom to L_geo with the Appendix-A factor before comparing with
  the analytic formula of `lhmuc/analytical.py::luminosity_general_cm2s`.

---

## 5. Running it: command line, licence, repository, hardware

Headless entry point (p. 19):

```
java -cp ".:gson-2.9.1.jar:bin" \
org.hepforge.alohep.HeadlessLauncher \
-left proton-ele/EIC-PDG1 -right electron-ring/EIC-PDG \
-hourglass -pinch -macrop 50000 \
-xres 50 -yres 50 -zres 50 -csv
```

GUI: `java -cp ".:gson-2.9.1.jar:bin" org.hepforge.alohep.Launcher` (p. 21). Other options named in the
paper: `-decay` (p. 36), `-fom` (p. 34). Parameter sets live in a JSON tree `save/` parsed by
`DataManager` (p. 18). Licence and repository: "Licensing provisions: MIT License (the bundled Gson
library is distributed under the Apache License 2.0)"; "Developer's repository link:
https://github.com/tobbetuyef/AloHEP" (p. 2; repeated p. 21 and p. 39). Language: "Java (Java
7-compatible syntax; builds and runs on OpenJDK 8–21, benchmarks run with OpenJDK 17; external library
Gson 2.9.1)" (p. 2). Note that the copy registered earlier as `SRC_URL_GITHUB_YEFETU_ALOHEP`
(github.com/yefetu/ALOHEP, no licence file seen) is a different URL; the paper does not mention it.
The licence of the paper itself is not stated in the PDF.

Benchmark hardware (p. 22): "a single thread (serial garbage collector, 4 GB heap limit via -Xmx4g),
utilising a single core of an AMD Ryzen 9 9900X processor (4.4 GHz base clock, twelve cores
available), with 48 GB RAM under Windows 11, using OpenJDK 17.0.19 ... no GPU acceleration is used.
Each configuration was executed three times (the macroparticle sampling uses an unseeded random
generator, so repeated runs differ statistically)". Runtime: "a full crossing of 5 × 10⁴
macroparticles on a 30³ grid completes in ∼ 12 s and a 100³ convergence run in ∼ 3.2 h" (p. 3);
Table 1: 0.092 s / 12.2 s / 208 s / 3.20 h for 10³ / 30³ / 50³ / 100³ (p. 24); HERA and EIC at 50³:
80–92 s per crossing (Table 6, p. 34). Run-to-run scatter "below ∼ 1% for the symmetric verification
runs and below ∼ 0.6% for both HERA and EIC at 5 × 10⁴ macroparticles" (p. 22) — bit-exact
reproduction of the paper's L_eff is not possible (unseeded RNG).

---

## 6. Verification results

### 6.1 Analytic limit and grid convergence (Table 1, p. 24; §5.1)

ILC-125, √s = 250 GeV, 5 × 10⁴ macroparticles, no perturbing effects, L_nom = 3.786 × 10³³ cm⁻²s⁻¹:
L_eff/L_nom = 0.9032 (10³), 0.9926 (30³), 0.9959 (50³), 0.9988 (100³); "∼ 10% at 10³, ∼ 1% at 30³"
and "agreement at the 0.1% level on a 100³ grid" (p. 37). The deficit is explained analytically by the
cloud-in-cell smoothing "[1 + (2k/N_g)²/6]⁻¹, i.e. by the factors 0.904, 0.988, 0.996 and 0.999 for
N_g = 10, 30, 50 and 100 with k = 4" (p. 24).

### 6.2 Hourglass and crossing angle (§5.3–5.4, p. 26–28)

Hourglass sweep A = BunLen/β_y* with BunLen = 0.3 mm on a 50×100×50 grid: "reproduces Eq. (22) to
within ∼ 1% across the full range A ≲ 1.5 that spans realistic machines (the ILC sits at A ≃ 0.75),
with deviations nowhere exceeding ∼ 0.8%"; "about 0.7% at A = 2, 1.3% at A = 3, and 3% at the extreme
A = 5"; A = 5 deficit "from 8.8% (three 50 × 50 × 50 runs, Appendix A) to 3.0%" when N_y is doubled
(p. 27). Crossing angle (50³, pinch off): "tracks the Piwinski factor across the full reduction from
S ≃ 1 down to S ≃ 0.25 (Fig. 22), to within ∼ 1%"; "holds up to θ ∼ 10⁻⁴ rad for these beam
parameters" (p. 27–28).

### 6.3 Pinch sign and magnitude (Table 3, p. 30)

| Collision | Charge product | D_y | Pinch ratio | Effect |
|---|---|---|---|---|
| pp (LHC, 30³) | same (+, +) | 0.0066 | 0.984 | negligible (high energy, large spot) |
| HERA (ep, 50³) | opposite (+, −) | 0.147 | 1.014 | focusing (enhancement) |
| EIC (ep, 50³) | opposite (+, −) | 1.34 | 1.068 | focusing (enhancement) |
| e−e− (ILC, 50³) | same (−, −) | 24.8 | 0.43 | defocusing (reduction) |
| e+e− (ILC, 50³) | opposite (−, +) | 24.8 | 2.22 | focusing (enhancement) |

Caption, p. 30: "For pp, e−e− and e+e− (hourglass never enabled) the ratio is L_eff/L_nom against the
flat, hourglass-off analytic baseline; for HERA and EIC (always run with hourglass enabled, Table 6)
the ratio instead isolates the pinch alone, L_eff(hourglass+pinch)/L_eff(hourglass only)." The ILC
e+e− pinch-only factor 2.22 (D_y = 24.8) is compared with the staging-report H_D = 2.19 (D_y = 24.5),
but with hourglass enabled as well AloHEP gives only H_L = 1.46–1.48, "so the gap to the design value
is a property of the slice-based model itself, which has not been validated at D_y ≫ 1" (p. 31).

### 6.4 Asymmetric ep colliders (Table 5 and Table 6, p. 34 — copied)

Table 5 (beam sizes, electron tune shifts and disruption; deterministic):

| Collider | √s [GeV] | proton σ_x × σ_y | electron σ_x × σ_y | ξ_x, ξ_y (e) | D_y (e) |
|---|---|---|---|---|---|
| HERA (ep) | 318.7 | 111 × 30 µm | 110 × 30 µm | 0.0224, 0.0358 | 0.1471 |
| EIC (ep) | 105 | 94.9 × 8.58 µm | 94.8 × 8.63 µm | 0.07245, 0.09967 | 1.3420 |

Table 6 (50³ grid, 5 × 10⁴ macroparticles each; means of three runs; L_geo = Eq. (24); luminosities in
cm⁻²s⁻¹):

| Collider | √s [GeV] | Configuration | L_geo | L_eff | L_eff/L_geo | Runtime |
|---|---|---|---|---|---|---|
| HERA (ep) | 318.7 | hourglass only | 4.32 × 10³¹ | 4.22 × 10³¹ | 0.977 | 80.0 s |
| | | hourglass+pinch | 4.32 × 10³¹ | 4.28 × 10³¹ | 0.991 | 79.9 s |
| EIC (ep) | 105 | hourglass only | 1.05 × 10³⁴ | 9.55 × 10³³ | 0.912 | 91.4 s |
| | | hourglass+pinch | 1.05 × 10³⁴ | 1.02 × 10³⁴ | 0.974 | 92.2 s |

Analytic Eq. (23) hourglass factors 0.980 (HERA) and 0.916 (EIC): the hourglass-only simulations are
"within 0.3% and 0.5% respectively" (p. 33). Inputs behind the deficits: "the long proton bunches
(σ_z ≃ 8.5 cm for HERA, ≃ 6 cm for EIC) ... at the EIC, where σ_z/β_y* ≃ 0.83" (p. 33). HERA was run
as p 920 GeV × e 27.6 GeV and the EIC as p 275 GeV × e 10 GeV (p. 32); "The EIC design collides the
beams at a 25 mrad crossing angle compensated by crab cavities; we simulate the crab-compensated,
effectively head-on collision" (p. 32).

### 6.5 Species coverage (§5.7, p. 34–36)

Pb–Pb at the LHC (Z = 82) and Au–Au at RHIC (Z = 79), head-on, pinch off: "reproduces the analytic
geometric value to ∼ 1%, and a Pb–Pb run with the pinch enabled gives L_eff/L_nom = 0.998" (p. 36).
μ+μ− at 10 TeV: §3 above (0.997–1.003 decay off; 0.252 vs 0.254 with decay).

---

## 7. Limits stated in the paper (what the benchmarks do not cover)

1. **No beamstrahlung in any benchmark**: "preliminary ... not included in the quantitative benchmarks
   above" (p. 36); "not yet validated" (p. 3). Irrelevant for muons but the option exists.
2. **No crab crossing**: "the rigid-rotation model of Section 3 does not include crab kicks" (p. 32);
   crossing angles are validated only "up to θ ∼ 10⁻⁴ rad for these beam parameters" (ILC, p. 28),
   because the rotated bunch must stay inside the ±kσ_y box.
3. **No lepton–hadron benchmark with decay**: decay was exercised only for the symmetric μ+μ− store
   (p. 36); the HERA / EIC runs have no decay; no μp or μA run appears anywhere in the paper.
4. **D_y ≫ 1 not validated** (p. 3, 31); the target regime is "D_y ≤ 1.3" (p. 31).
5. **Hourglass at A ≳ 2 under-counted** by the vertical grid (0.7–3 % for N_y = 100, 8.8 % at A = 5
   with N_y = 50, p. 27) — relevant to a long proton bunch against a small muon β*_y.
6. **Single bunch-pair crossing, Gaussian initial distributions, ultra-relativistic, Euler
   integration** (p. 3). "no multi-bunch effects" (p. 3).
7. **L_nom readout is the equal-beam approximation** (p. 33, §4 above).
8. **Collision-frequency and storage-time rules are README-only** (p. 21); unseeded RNG (p. 22).
9. **No μLHC / LHμC input deck is printed**: the paper lists the μLHC paper among the applications
   (refs. [7], [16], p. 4) but gives none of its parameters or option sets; the open item
   `ME_043_ALOHEP_CODE_AND_INPUT_DECKS` stays open.
10. The benchmark machines' underlying inputs (N₁, N₂, f_c, β*, emittances for HERA, EIC, LHC, RHIC)
    are not printed; only the derived Tables 5–6 values are (sources: PDG [32], EIC CDR [33]).

---

## 8. How this will be used for LHμC in M2 (Benchmark 3.1, `docs/validation_plan.md` §3.1)

Target values (existing records; none of them produced here):

| Parameter id | Value | Scenario | Source |
|---|---|---|---|
| `MACHINE_PEAK_LUMINOSITY_ERL_MULHC` | 7.2 × 10³³ cm⁻²s⁻¹ | `MULHC-PTEP2026-ERL-BOOSTER` | arXiv:2506.15445 p. 12 (AloHEP result) |
| `MACHINE_PEAK_LUMINOSITY_MUTRISTAN_MULHC` | 8.8 × 10³³ cm⁻²s⁻¹ | `MULHC-PTEP2026-MUTRISTAN-BOOSTER` | arXiv:2506.15445 p. 12 (AloHEP result) |
| `MACHINE_PEAK_LUMINOSITY_WS2026_FORTHOMME` | 1 × 10³⁴ cm⁻²s⁻¹ | `LHMUC-WS2026-FORTHOMME` | Kraków deck, backup slide 17 (code not stated) |

Plan, per `CONF_LUMI_MODEL_ASSUMPTIONS` (option set recorded with every run, tolerance 5 %):

1. **Reconstruct the μLHC decks** from the registry (μ+: N, E, β*, ε_n, σ_z = 2 mm, revolution
   frequency; p: N, E, β* = 7 cm, ε_n; `MULHC-PTEP2026-*` scenarios) as `save/` JSON entries, one
   `circle`-tagged muon beam and one proton beam. Every input is a parameter id; the proton bunch
   length is **not** in the μLHC paper and must be taken from `PROTON_BUNCH_LENGTH_RMS_SYN` (synthetic
   range) with its assumption badge.
2. **Run three option sets** per configuration and record L_nom, L_eff, ξ_x,y of the muon beam:
   (a) hourglass only; (b) hourglass + pinch; (c) each of these multiplied by the **one-beam** decay
   average (1 − e^{−T/γτ})/(T/γτ) over the μLHC store (2000 turns, `MACHINE_MU_AVERAGE_POPULATION_FRACTION_MULHC` = 0.63),
   applied outside the code if the code's `-decay` option turns out to implement the two-beam μ+μ−
   average — the two differ (0.632 vs 0.432 over one lifetime,
   `tests/scientific/test_batch7_documents.py::test_decay_averaging_differs_between_mumu_and_mup`)
   and the paper does not say which the code uses for asymmetric pairs (§3).
3. **Compare with the audit**: the registry audit shows 7.2 × 10³³ / 8.8 × 10³³ = naive formula ×
   0.632 with no visible hourglass reduction, although the stated optics (μ β*_y = 0.7 cm, p β* = 7 cm,
   μ σ_z = 2 mm, p σ_z ≈ 7.5 cm — an HL-LHC-type assumption, not a source value, cf. `PROTON_BUNCH_LENGTH_RMS_SYN` [verifier])
   would give an hourglass factor ≈ 0.53 (`CONF_LUMI_MODEL_ASSUMPTIONS`,
   `docs/validation_plan.md` row 6–7). Option set (a) with and without the Matched Beams helper
   (§2; `MACHINE_MU_BETA_STAR_MATCHED_IMPLIED_MULHC` = 4.37 cm ≈ 4.4 cm [verifier]) decides which model reproduces the
   printed numbers. Passing proves that the published values are understood, not that they are
   achievable.
4. **Convert L_nom to L_geo** with the Appendix-A factor (§4) for any unmatched run before comparing
   with `lhmuc/analytical.py::luminosity_general_cm2s`; report the muon-beam ξ_x,y and D_y from the
   `-fom` output alongside (the paper warns that "a luminosity quoted without the beam–beam tune shifts
   of the stored beams ... can be unrealistically high", p. 2).
5. **Forthomme set**: same three option sets with the slide-17 inputs (40 bunches of 10¹⁰ μ+, 300 ns
   spacing, HL-LHC-like protons; muon energy, emittances and bunch lengths are `unknown_roles` of
   `LHMUC-WS2026-FORTHOMME`), so the result is a band over the unknown inputs, not a point.
6. **Resolution**: 50³ with 5 × 10⁴ macroparticles as in the paper's asymmetric benchmarks (≈ 80–92 s
   per crossing on one core, Table 6); check the hourglass parameter A = σ_z,p/β*_y,μ of each deck
   against the validated range A ≲ 1.5 and refine N_y when it is exceeded (§6.2); use the box rule of
   p. 11 to anticipate the loss of vertical resolution.
7. **Before any run**: pin the repository commit and the SHA-256 of the jar / sources, record the JDK
   (OpenJDK 17 as in the paper), and treat the code as untrusted input (`docs/security_policy.md`);
   the MIT licence (p. 2) permits this, but the relation between github.com/tobbetuyef/AloHEP and the
   earlier-registered github.com/yefetu/ALOHEP must be established first (`ME_043`).

What AloHEP will **not** settle for LHμC even after Benchmark 3.1: the proton bunch length and the
muon β* of LHμC proper (unknown roles of the DIS2026 scenarios), the crab-crossing option (not
modelled), and multi-bunch / train effects (single bunch pair only).

---

*Status labels*: geometry fidelity not applicable (software), validation of the benchmark numbers P0
for this repository (the paper's own results) except the arithmetic reproductions marked P1 in the
parameter file (Table 1 / Table 6 ratios, cloud-in-cell factors, scaling exponents, the Piwinski example, sqrt(s), D_y and σ*_y of ILC-125, decay factor, turns,
γτ). Nothing in this note has been verified by running the code.
