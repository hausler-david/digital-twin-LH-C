# Verification note — SRC_ARXIV_2506_15445 (Akturk et al., μLHC, arXiv:2506.15445v2)

Verifier pass, 2026-10-28. Every parameter record in the seven files written by the extraction agent was
checked against the cited page of `references/_local/arXiv-2506.15445v2.pdf` (page images at 110–300 dpi
for Figures 1, 3, 6/7, 8, 10, 12–16 and Tables 1–6) and against the page-text files
`scratchpad/text/arXiv-2506.15445v2_pNN.txt`.

Files checked (record counts before → after):

| file | before | after |
|---|---|---|
| parameters/machine/mulhc_ptep2026.yaml | 43 | 44 |
| parameters/source/mulhc_ptep2026_source.yaml | 24 | 24 |
| parameters/acceleration/mulhc_ptep2026_acceleration.yaml | 34 | 35 |
| parameters/proton_beam/mulhc_ptep2026_proton.yaml | 13 | 13 |
| parameters/detector/mulhc_ptep2026_detector.yaml | 20 | 22 |
| parameters/physics_programme/mulhc_ptep2026_physics.yaml | 55 | 60 |
| parameters/machine/scenarios_mulhc.yaml | 2 scenarios | 2 scenarios |

Overall verdict: 189 records checked; **1 numerical transcription error**, **1 arithmetic slip in a note**,
**3 wrong "not reproducible" claims** (the numbers do reproduce), **9 misleading applicability texts**,
**17 uncertainty-type misuses**, several wording/metadata fixes; **0 records removed** (every value is
supported by the document); **9 records added**. All seven files validate with 0 schema errors
(`tools/validate_yaml.py provenance|machine`). Status rules were respected throughout: no record uses
`reported_lhmuc`; μTRISTAN-/LHeC-imported values say so in `applicability.explanation`.

## 1. Value / quotation corrections

| parameter_id | field | before | after | evidence |
|---|---|---|---|---|
| DET_NOZZLE_PASSING_ENERGY_FIT_PEAK_MULHC | value, quotation, P1 method | 881.6 GeV; "Mean 881.6 ± 1.2"; 1000−881.6 = 118.4 | **881.8 GeV**; "Mean 881.8 ± 1.2"; 1000−881.8 = 118.2 | Figure 10 right statistics box, p.14, read at 300 dpi |
| ACC_ERL_BOOSTER_EXTRACTION_ENERGY_MULHC | quotation | the 67 % sentence (does not contain the value) | "acceleration of positive muons from 212 MeV to 1 TeV requires 50 turns within the ERL based booster ring." | p.10 |
| ACC_LHEC_PHASE_ONE_CIRCUMFERENCE_FRACTION_MULHC | value | 0.3333 | 0.3333333333 (exact 1/3 noted) | "one-third", p.9 |
| ACC_BOOSTER_INJECTION_ENERGY_MULHC | name | "kinetic energy" | "energy" (+note: kinetic vs total not specified) | p.6 says only "from 212 MeV" |
| DET_SCATTERED_PARTICLE_DIRECTION_MULHC | value | "backward (muon beam direction)" | "backward direction (convention not defined in the text; Figure 8 places the far-backward MS where the μ beam exits)" | p.13 |
| DET_NOZZLE_PLACEMENT_MULHC | extraction_method | manual_text_read | manual_figure_read ("single cone" comes from Figure 8, not the text) | p.13 |

All other values, units, pages, table/figure labels and quotations were confirmed verbatim (Tables 1–6 cell by
cell against the page images; Figure 1 labels; Figure 10 left box "Entries 2000 / Mean 184.2 / Std Dev 152.4 /
Constant 191.8 ± 7.1 / Mean 114.9 ± 1.1 / Sigma 34.28 ± 1.36"; Figure 10 right box "Entries 2000 / Mean 810.2 /
Std Dev 157.3 / Constant 181.2 ± 6.6 / Mean 881.8 ± 1.2 / Sigma 35.52 ± 1.33").

## 2. Validation claims corrected (numbers that *do* reproduce)

| parameter_id | before | after |
|---|---|---|
| ACC_BOOSTER_SURVIVAL_MUTRISTAN_MULHC | P0, note "not reproduced: coarse integral gives 86–89 %" | **P1**: turn-by-turn decay integral (linear +30 GeV ramp inside each 3 km linac, constant energy in each π·1 km arc, 0.212 → 960 GeV, 16 turns, cτ = 658.6 m) gives **0.816 = 82 %** as printed (Figure 3 label "(0.82)"). The extractor's model kept the energy constant over a whole turn. |
| ACC_BOOSTER_SURVIVAL_ERL_MULHC | "not reproducible here" | stays P0 (arc geometry not printed) but documented: the same integral gives 67 % for L_arc = 3.2 km (C ≈ 8.4 km); 65.6 % for C = 1/3 LHC (8.9 km); 68.1 % for C = 8.0 km — consistent with a booster of LHeC-ERL size. |
| MACHINE_PEAK_LUMINOSITY_MUTRISTAN_MULHC / _ERL_ | P0; note "naive L = 1.4e35" | **P1**: naive L = f N_μ N_p/(4π σ²) = **1.40e34** (ERL: 1.14e34) — the note was a factor-10 slip — and × 0.632 (the paper's own 1−1/e average-population factor, p.11) gives 8.86e33 / 7.18e33, i.e. the printed 8.8e33 / 7.2e33 to 1 %. |
| PROTON_TUNE_SHIFT_MUTRISTAN_MULHC (+ERL) | P0 | **P1**: ξ_p = N_μ r_p β*_p/(2π γ_p σ(σ_x+σ_y)) = 2.29e-3 (printed 22e-4); ERL 1.86e-3 (printed 18e-4). |
| MACHINE_MU_TUNE_SHIFT_MUTRISTAN_MULHC (+ERL) | P0 | **P1** (conditional): 0.041 / 0.0095 with the Table 1 β* (3 cm / 0.7 cm) but **0.0597 ≈ 600e-4** with the matched β*_μ = σ²γ/ε_n = 4.37 cm. |
| MACHINE_IP_BEAM_SIZE_MU_MUTRISTAN_MULHC | "discrepancy recorded, not resolved" | explained: 4.3 μm ⇔ β*_μ = 4.37 cm in both planes (new record MACHINE_MU_BETA_STAR_MATCHED_IMPLIED_MULHC, analytical_estimate with derivation); this is what "beam size matched accordingly" (p.12) did. |

Scenario file: both scenarios raised from P0 to **P1** (luminosity and, for μTRISTAN, survival reproduced
analytically); notes rewritten accordingly. Labels "post-erratum" → "as printed in arXiv v2; erratum status
unresolved" (the PDF itself never uses the word erratum; the acknowledgements only give the ×2 / ×4 factors).

## 3. Applicability texts that contradicted the record

The generator's μTRISTAN boilerplate "… adopted unchanged for the μLHC chain" was attached to values that are
explicitly **not** adopted. Replaced by "NOT a μLHC parameter / NOT adopted" on:
MACHINE_MUTRISTAN_MUMU_BUNCH_CHARGE_MULHC, MACHINE_MUTRISTAN_MUMU_BUNCHES_MULHC,
MACHINE_MUTRISTAN_MUE_MU_BUNCH_CHARGE_MULHC (now also records that the μLHC bunch population 3.7e10 = 5.9 nC
is inconsistent by ×2.7 with the μ+e⁻ label 2.2 nC although Table 1 claims to adapt the μ+e⁻ beam),
MACHINE_MUTRISTAN_MUE_E_BEAM_ENERGY_MULHC, MACHINE_MUTRISTAN_MUE_E_BUNCH_CHARGE_MULHC,
MACHINE_MUTRISTAN_MUE_BUNCHES_MULHC, MACHINE_MUTRISTAN_MAIN_RING_COUNT_MULHC (μLHC: "a single main ring"),
ACC_BOOSTER_SURVIVAL_MUTRISTAN_ORIGINAL_CLAIM_MULHC, ACC_BOOSTER_OUTPUT_BUNCH_CHARGE_MUTRISTAN_ORIGINAL_MULHC.

ACC_BOOSTER_SURVIVAL_MUTRISTAN_MULHC: "the acknowledgements attribute the corrected survival rates to
K. Piotrzkowski" → the paper only thanks him "for pointing out the inconsistency in antimuon survival rates"
(quoted verbatim now).

PHYS_MU8_DISCOVERY_MASS_HLLHC_MULHC and PHYS_MU8_LUMINOSITY_EQUIVALENT_TO_HLLHC_MULHC said the HL-LHC
integrated luminosity is "not stated": it **is** stated in the Figure 16 legend ("Pair prod. HL-LHC L_int = 3 ab⁻¹";
μLHC curves at 1 ab⁻¹, 100 fb⁻¹, 100 pb⁻¹, 100 nb⁻¹). Texts corrected; the "100 nb⁻¹" unit is confirmed by the legend.

## 4. Uncertainty-type misuse

`order_of_magnitude` had been used whenever the source says "approximately/about/~". That asserts a factor-10
uncertainty the source does not claim and was inconsistent with the 82 %/67 %/19 %/81 % records (which used
`not_stated` + note). Changed to `not_stated` with the qualifier quoted in `note` on 15 records:
MACHINE_LUMINOSITY_ERRATUM_FACTOR_MUTRISTAN/ERL, MACHINE_MU_LIFETIME_LAB, MACHINE_MAIN_RING_REVOLUTION_TIME,
MACHINE_MAIN_RING_TURNS_PER_LIFETIME, MACHINE_MU_AVERAGE_POPULATION_FRACTION,
MACHINE_MU_AVERAGE_BUNCH_POPULATION_MUTRISTAN/ERL, SOURCE_TARGET_ENERGY_LOSS_PER_PASS,
SOURCE_STOPPING_TARGET_LAYERS, SOURCE_STOPPING_TARGET_LENGTH, ACC_BOOSTER_ACCELERATION_TIME_MUTRISTAN,
ACC_ERL_LINAC_LENGTH, PHYS_MU8_DISCOVERY_MASS_HLLHC, PHYS_MU8_DISCOVERY_MASS_MULHC_100FB.
`order_of_magnitude` kept only for SOURCE_MUON_RATE_ENHANCEMENT_MULHC ("𝒪(10⁵)").

DET_NOZZLE_DEPOSITED_ENERGY_MEAN_MULHC / DET_NOZZLE_PASSING_ENERGY_MEAN_MULHC carried the histogram "Std Dev"
(152.4 / 157.3 GeV) as `gaussian_sigma` on the mean; a distribution width is not an uncertainty on the mean.
Changed to `not_stated` (statistical error of the mean ≈ 3.4 / 3.5 GeV noted) and the widths recorded as their
own records (below).

## 5. Metadata

* Section labels of the Table 5 and Table 6 comparator records: "3. Physics Potential…" → "3.1 Small x-Bjorken"
  (9 ids) / "3.2 Higgs production" (4 ids).
* SOURCE_PION_RING_LABEL_CHARGE_PER_PION_MULHC: note now records that the figure prints "⊿Ep" and that the value
  must not be used numerically (meaning of "100 nC/π" still undefined; confidence low kept).
* File headers: added one line pointing to this note.

## 6. Records added (all quotable; none existed)

| parameter_id | value | where |
|---|---|---|
| MACHINE_MU_BETA_STAR_MATCHED_IMPLIED_MULHC | 4.37 cm (analytical_estimate, derivation σ²γ/ε_n) | Table 3 "beam size matched", p.12 |
| DET_NOZZLE_DEPOSITED_ENERGY_STDDEV_MULHC | 152.4 GeV | Figure 10 left stats box, p.14 |
| DET_NOZZLE_PASSING_ENERGY_STDDEV_MULHC | 157.3 GeV | Figure 10 right stats box, p.14 |
| PHYS_MU8_HLLHC_INTEGRATED_LUMINOSITY_MULHC | 3 ab⁻¹ | Figure 16 legend, p.20 |
| PHYS_MU8_SIGNIFICANCE_LUMINOSITY_SET_MULHC | "1 ab⁻¹, 100 fb⁻¹, 100 pb⁻¹, 100 nb⁻¹" | Figure 16 legend, p.20 |
| PHYS_MU8_BENCHMARK_MASSES_MULHC | "1.5, 2.5, 3.5 TeV" | Figures 14–15 legends, p.19 |
| PHYS_MU8_HLLHC_PRESELECTION_MULHC | "2 muons and 2 jets; same η cuts as μLHC" | p.19 |
| PHYS_LHEC_SQRT_S_TEXT_MULHC | 1.2 TeV (analogous; Table 4 prints 1.18) | p.4 |
| ACC_MUON_COLLIDER_COOLING_DEMONSTRATOR_YEAR_MULHC | 2035 (calendar year; analogous, from ref. [49]) | p.2 |

## 7. Removed

None. Every record had document support. (The low-confidence "100 nC/π" label record was kept as a verbatim
figure label with an explicit "do not use numerically" note rather than deleted.)

## 8. Checked and left unchanged (examples of attempted refutations that failed)

* Table 1–3 and Table 4–6 transcriptions: all 50+ cells match the page images (including ξ 600/22/18 ×10⁻⁴,
  EIC √s 0.105 vs 0.145 conflict, HERA 0.8 (total)).
* Figure 1 labels ("RCS : 3 GeV x 6.6 μC x 2-bunch x 50 Hz = 2 MW", "1 TeV x (7.2nC=>3.6nC)/μ x 40 bunch x 50Hz = 9 MW",
  "30 GeV muon LINAC ~ 3 km", "R=1 km (B = 3 T max)", "16 turns ~ 700μs", "3 km Main ring τμ = 20 ms (2000 turns)",
  "μ+μ+ : 1 TeV, 2.2 nC x 1 TeV,2.2 nC x 20bunch", "μ+e- : 1 TeV, 2.2 nC x 30 GeV,10 nC x 40bunch") verified.
* 9 MW booster power still not reproduced (7.2 / 14.4 MW); confidence low kept.
* P1 arithmetic re-done: 2√(E_μE_p) = 5.29 TeV; γτ = 20.8 ms; 3 km/c = 10.0 μs; 1−1/e = 0.632; 7.2 nC = 4.49e10;
  σ_p = 4.33 μm; c/26.659 km = 11245 Hz; Table 5 x/Q² values; implied Higgs cross sections 385 fb / 75 fb.
* Source metadata ("PTEP 2026 033C04") is not in the PDF but matches the lead's `research/source_registry.yaml`
  entry; author list and title verified against p.1.

## 9. Residual doubts / open items for other owners

* `uv run python -m lhmuc validate` currently aborts on **another agent's file**
  `parameters/physics_programme/lhmuc_two_photon_benchmarks.yaml` (YAML parse error at line 1940/1948, an
  unbalanced quote in `table_figure_or_equation`). Not touched here. All seven μLHC files validate individually,
  all MULHC dependency ids and scenario references resolve (749 ids loaded excluding that file), and all 29 unit
  strings parse.
* Whether arXiv v2 contains all erratum corrections remains unresolved (registry item).
* The 9 MW Figure 1 label and the "100 nC/π" label remain unexplained.
* Conflict entries still to be created by the research-log owner: EIC √s 0.105 vs 0.145 TeV; μTRISTAN "about
  half" vs 82 %; LHeC √s 1.2 vs 1.18 TeV (rounding); μ+e⁻ label 2.2 nC vs μLHC 5.9 nC per bunch.

## 10. Final validation run

`uv run python -m lhmuc validate` (after the two-photon file was repaired by its owner): 809 parameters,
5 sources, 13 scenarios loaded; **0 errors in any μLHC file**. The only 2 remaining errors are in other owners'
proposal records (`PROP_A_HNL_2610_28252`, `PROP_B_2HDM_VLQ_2610_17801` reference source ids not yet in the
registry) — outside this assignment.
