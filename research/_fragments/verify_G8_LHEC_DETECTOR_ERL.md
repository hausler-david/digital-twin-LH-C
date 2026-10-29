# Verification note — group G8_LHEC_DETECTOR_ERL (arXiv:2201.02436v1, SRC_ARXIV_2201_02436)

Verifier pass of 2026-10-29 (batch 7) over the extraction of André et al., *An Experiment for
Electron-Hadron Scattering at the LHC* (27 pp.). Files checked:

| file | records | result |
|---|---|---|
| `parameters/detector/lhec_detector_andre2022.yaml` | 141 | 2 notes added, no value/unit/page/quotation error |
| `parameters/acceleration/lhec_erl_andre2022.yaml` | 75 | 1 dependency fix, no value error |
| `parameters/interaction_region/lhec_ir_andre2022.yaml` | 59 → 63 | 1 note extended, 4 records added |
| `parameters/physics_programme/lhec_physics_andre2022.yaml` | 0 → 12 | **new file** (verifier additions, see §4) |
| `parameters/machine/scenarios_batch7_lhec.yaml` | 1 scenario | 10 roles added, 2 `unknown_roles` resolved |

Total records re-checked: 275 (every record of the three extraction files); 16 added; **none removed**.
All five files: `tools/validate_yaml.py` 0 schema errors; `python -m lhmuc validate` 0 errors / 0 warnings;
`tests/scientific/test_batch7_documents.py` 14 passed. No record carries `reported_lhmuc`
(261 `imported_related`, 4 `analogous`, 10 + 4 `analytical_estimate` with derivations; the 12 new physics
records are `imported_related`).

## 1. What was checked and how

* Every table and figure the records cite was viewed as a page image rendered at 600–1800 dpi
  (own crops, not the extractor's): Fig. 4 (all 15 dimension labels), Table 1 (all 42 cells), Fig. 5/6/7
  labels, Fig. 8 (formula read at 1200/1800 dpi), Table 2, Fig. 9/10/11 labels, Fig. 14, Table 3,
  Table 4, Fig. 19 (header, legend boxes, all seven labelled points, all four axes), Table 5, Table 6,
  Fig. 24 (all labels). Every transcribed cell and label agrees with the records.
* All 124 `manual_text_read` quotations were machine-compared with the pdftotext layer after
  whitespace/ligature/superscript normalisation; 116 match verbatim, the remaining 8 differ only by
  column/page breaks or line-end hyphenation of the text layer (`large-area`, `weak-strong`,
  `non-colliding`, the p.10→p.11 sentence of `DET_TRACKER_LAYOUT_TOOL_ANDRE2022`, the Table-4 interruption
  of the §4.8 sentence, the column break inside the Q = 10^10 sentence and the QA1 sentence). The
  quotations are verbatim.
* Every derivation was recomputed: N_e = 499 pC/e = 3.1145e9; 1/24.95 ns = 40.080 MHz;
  801.58 MHz × 24.95 ns = 19.9994; Table-3 energies = 0.5 + 8.25 n GeV; 8.25 GeV/20.06 MV/m = 411.3 m;
  20 mA × 50 GV = 1.0 GW; 20 mA × 6 passes = 120 mA; ΣP(arcs) = 21.46 MW; √s = 2√(50 × 7000) GeV =
  1183.2 GeV; Bρ_p = 23 349.5 T m (0.07 % from 23 333), Bρ_e = 166.8 T m; Fig. 8 formula at 10 GeV
  → 2.697 %, at 400 GeV → 0.530 % (plotted points ≈ 0.027 / 0.0054 confirmed on the image); E_c ∝ E³ and
  P ∝ E⁴ between arcs 5 and 6 within 1 % (and, as the extractor says, the E⁴ scaling does *not* hold for
  arcs 2–3, so no P1 is claimed there — correct).
* Provenance statuses, applicability categories (`analogous`; `superseded` for the 60 cm / 7-layer /
  3.5 T / 60 GeV previous-design values; `screening_only` for the two Fig. 10 graph readings), confidence
  levels (medium only where the paper leaves an attribution open), units (pint-parseable), scenario
  assignment (detector records scenario-null but linked as G0 geometry roles; accelerator/IR records in
  `LHEC-ANDRE2022-ERL-50GEV`) and the cited test names all check out.

## 2. The extractor's three corrections to the batch-7 brief are confirmed

1. Fig. 19 header reads **β\*_p = 10.0 cm and β\*_e = 10.9 cm** (subscripts p and e, read at 1200 dpi):
   beam, not plane. The ids `IR_BETA_X_STAR_ANDRE2022` / `IR_BETA_Y_STAR_ANDRE2022` are kept as the lead's
   labels; their names and notes state the true meaning. The docstring of
   `test_andre2022_table4_luminosity_with_hl_lhc_proton_parameters_recorded_band` treats the two numbers
   as β\*_x / β\*_y — a misreading in a test I may not edit; the lead should amend it (the band assertion
   itself is unaffected: it only mixes 10.0/10.9 cm as if they were the two planes of one beam).
2. The Fig. 8 constant term is **(0.318 ± 0.02) %**, not ± 0.021 (verified at 1800 dpi).
3. p.10 reads "extended from **60 cm to 80 cm**" (the brief's example quotation "from 60 to 80 cm" is the
   §3.2 wording "extending the radius from 60 to 80 cm", which the record keeps in its notes).

## 3. Corrections applied to the files

| record | field | change | reason |
|---|---|---|---|
| `ACC_ERL_ARC6_ENERGY_ANDRE2022` | `dependencies` | `[ACC_ERL_ENERGY_GAIN_PER_LINAC_ANDRE2022, ACC_ERL_INJECTION_ENERGY_IMPLIED_ANDRE2022]` → `[]` (+ note) | circular: both listed records are *derived from* the Table 3 energies; a table cell has no inputs |
| `DET_TRACKER_LAYOUT_TOOL_ANDRE2022` | `notes` | added | the quoted sentence starts at the foot of p.10 and ends on p.11 |
| `DET_JOINT_TRACKING_POLAR_ANGLE_ANDRE2022` | `notes` | added | the §5.1 bullet's "this" is the envisaged joint eh/hh detector, not the Fig. 4 baseline; stated explicitly |
| `MACHINE_PROTON_EMITTANCE_GROWTH_ANDRE2022` | `notes` | extended | physical-plausibility argument that the Table 4 Δγε = 15 mm mrad is the electron beam (50 % of the 30 mm mrad electron emittance; a proton growth of that size could not be "in the shadow of the other effects"); id token kept as required |
| scenario `LHEC-ANDRE2022-ERL-50GEV` | `parameters`, `unknown_roles`, `notes` | 10 roles added; `ir_sr_absolute_critical_energy`, `ir_sr_absolute_power` removed from `unknown_roles` | the absolute IR SR values are recoverable from Fig. 19 (see §4) |

No value, unit, page, table/figure label or quotation had to be changed. No id was changed.
**Removed records: none.**

## 4. Additions (quotable statements the extractor left out)

### 4a. Absolute IR synchrotron-radiation values from the Fig. 19 twin axes (IR file, 4 records)

Fig. 19 prints only relative differences at its labelled points, but it carries *two* axes per
direction: P_syn [kW] (16–28) against the relative-difference axis (0 … −40 %), and E_crit [keV]
(256 … 360) against the relative-difference axis (−15 … 20 %). Pixel measurement on a 600 dpi render
(frame rows 150.5–1335.5, cols 545–1793; inner gridlines 0 % at row 176.5 … −40 % at row 1190.0;
outer labels 16 kW at the frame bottom, 28 kW at row 344; vertical gridlines at cols 723.5 … 1614.5 for
−10 … 15 %) gives

* `IR_SR_POWER_DIPOLE_SCHEME_FIG19_ANDRE2022` = 30.0 kW (29.5–30.5): the 0 % gridline sits at 30.0 kW,
  the −20 % and −40 % gridlines at 24 and 18 kW (= 30 × 0.8, 30 × 0.6);
* `IR_SR_CRITICAL_ENERGY_DIPOLE_SCHEME_FIG19_ANDRE2022` = 300 keV (299–302): 256 + 15 × 104/35 = 300.6 keV,
  bracketed by 256/0.85 = 301.2 and 360/1.20 = 300.0 keV;
* `IR_SR_POWER_MIN_OPTIMISED_FIG19_ANDRE2022` = 16.9 kW (16.6–17.3) = 30.0 × (1 − 0.4355), the red point
  of the final scheme;
* `IR_SR_CRITICAL_ENERGY_MIN_OPTIMISED_FIG19_ANDRE2022` = 264 keV (262–266) = 300 × (1 − 0.1217).

All four are `analytical_estimate`, confidence medium, interval uncertainties, P1 (arithmetic given in
the records). They are graph calibrations, not printed numbers — use accordingly.

### 4b. Physics-programme prospects of §§2.2–2.4 (new file `parameters/physics_programme/lhec_physics_andre2022.yaml`, 12 records)

Outside the extractor's detector/ERL/IR scope but clearly quantitative and quotable; placed in the
subsystem directory CLAUDE.md §4 prescribes (the lead may relocate the file): Higgs CC cross section
"about 200 fb" (p.5); δκ_c ≃ 4 % (p.5); top-Yukawa 17 % with 1 ab⁻¹ (p.6, **attribution ambiguous**: the
sentence says "at the LHC" inside the LHeC tth discussion and cites an LHeC study [20] — recorded as
printed, confidence medium); single-top CC 1.9 pb and tt̄ photoproduction 0.05 pb (p.6); Wtb coupling
"of order of 1 %" with 100 fb⁻¹ (p.7, two records); NLO fiducial single-top reduction 14 % (p.7);
δα_s(M_Z) = ±0.00022 (inclusive) and ±0.00016 (jets) (p.7); Δsin²θ_W = ±0.00022 (p.8); light-quark Z
couplings "about 1 %" (p.8). Scenario left null on these records because the paper does not tie the
numbers to its 50 GeV configuration explicitly; six of them are linked as scenario roles.

New records carry `date_added: 2026-10-29` (the day they were written; the extraction's records keep
2026-10-28).

## 5. Residual doubts (kept as recorded, not resolved)

1. **Table 4 Δγε = 15 mm mrad**: the table does not name the beam; physics and context point to the
   electron beam; the required id token says PROTON. Lead decision needed (rename or keep with the note).
2. **Table 4 luminosity 8.2e33**: the proton bunch population/emittance behind it are not in the paper;
   the test is a band check only (ratio ≈ 0.75 with assumed HL-LHC protons).
3. **Fig. 4 / Fig. 24 dimension labels** (467, 326, 156, 95, 148, 88, 580, 172, 186, 23, 154, 1140):
   the captions do not map labels to components; the records describe arrow positions (confidence
   medium). A consistency puzzle remains: 95 + 88 = 183 cm would put the EMC barrel outside the 156 cm
   dipole/solenoid line, so 95 and 88 cannot both be "EMC inner radius" and "EMC thickness".
4. Paper-internal inconsistencies preserved as separate records: "five backward disks" (p.10) vs Table 1
   Bwd rings 2 + 1 + 4 = 7; "about 13 m" (Fig. 4 caption) vs 13.75 m (Fig. 24 caption, label 1375);
   "roughly 2 m" magnet radius (p.23) vs the 156 cm drawing label; text "500 pC at 40 MHz" vs Table 2
   "499 pC / 24.95 ns"; §4.7 text "red and black points … minimum critical energy and emitted power,
   respectively" vs the plot where black = lowest E_crit and red = lowest power (records named by plot
   position, colour in the quotation — confirmed on the image).
5. `ACC_ERL_ARC_CELL_LENGTH_ANDRE2022` = 28.085 m: the Fig. 11 s-axis prints no unit (metres assumed,
   confidence medium).
6. Fig. 10 graph readings (Q₀ ≈ 4e10 at ≈ 20 MV/m; quench ≈ 30 MV/m) are `screening_only`, confidence
   low; my own reading (3.9e10, 30.2 MV/m) agrees.
7. The absolute SR values of §4a are twin-axis calibrations good to ≈ 1–2 %; the P-axis label-centre
   fits scatter between 29.5 and 30.0 kW, hence the intervals.
8. The lead's list of 33 required ids was not available to the verifier (not in the repo or the
   scratchpad); no id was renamed or removed, so whatever the extractor reported present is still present
   (`IR_BETA_X/Y_STAR_ANDRE2022`, `MACHINE_PROTON_EMITTANCE_GROWTH_ANDRE2022`, `DET_TRACKER_OUTER_RADIUS_ANDRE2022`,
   `ACC_ERL_GRADIENT_ANDRE2022`, `MACHINE_LUMINOSITY_GOAL_ANDRE2022`, `MACHINE_PEAK_LUMINOSITY_ANDRE2022`,
   `DET_NEUTRON_FLUENCE_ANDRE2022`, `IR_LSTAR_ANDRE2022` … all confirmed with the stated values).
9. Scenario status `reported` with 23 `unknown_roles` follows the repository convention for scenarios
   built from a peer-reviewed design paper (cf. `MULHC-PTEP2026-*`, `JPARC-G2-EDM-DESIGN-2019`); the
   missing proton-side inputs are listed, not guessed.
10. `test_csv_registries_in_sync` (unit tests) still fails because `registries/*.csv` are generated and
    out of date for all batch-7 files; `registries/` was not touched (lead runs `tools/build_registries.py`).

## 6. Candidate conflict / missing-evidence entries for the lead (not written by the verifier)

* `MACHINE_LUMINOSITY_GOAL_ANDRE2022` (1e34, design goal) vs `MACHINE_PEAK_LUMINOSITY_ANDRE2022`
  (8.2e33, Table 4 simulation).
* `DET_NEUTRON_FLUENCE_ANDRE2022` (~1e13 neq/cm²) vs `DET_NEQ_FLUENCE_LHEC_UPPER_BOUND_WS2026_FORTHOMME` (≪ 1e14).
* `IR_LSTAR_ANDRE2022` = 15 m vs the Forthomme 15 / 23 m options.
* `ACC_ERL_GRADIENT_ANDRE2022` = 20.06 MV/m vs `ACC_ERL_GRADIENT_LHEC_WS2026_FORTHOMME`.
* `PHYS_HIGGS_CC_XSEC_ANDRE2022` (≈ 200 fb) vs the DIS2026 working-point enhancement factors
  (`PHYS_ENHANCEMENT_1TEV_VS_LHEC50_CC_HIGGS_WP`) — the LHeC reference energy/polarisation is unstated here.
* Missing evidence: proton bunch population and normalised emittance used for Table 4; linac fill
  factor / RF phase; LHC circumference (Table 6 fractions); IP2 crossing angle and horizontal offset of
  the non-colliding beam (mentioned, no numbers).

## Lead reconciliation (2026-10-29)

- Ids renamed after checking the Fig. 19 header on a 400 dpi crop of p. 18 (it reads β*_p = 10.0 cm and β*_e = 10.9 cm): `IR_BETA_X_STAR_ANDRE2022` → `IR_BETA_STAR_PROTON_FIG19_ANDRE2022`, `IR_BETA_Y_STAR_ANDRE2022` → `IR_BETA_STAR_ELECTRON_FIG19_ANDRE2022` (the §4.6 text value keeps its own id `IR_BETA_STAR_PROTON_ANDRE2022`). The x/y tokens came from the lead brief and were wrong.
- `MACHINE_PROTON_EMITTANCE_GROWTH_ANDRE2022` → `MACHINE_ELECTRON_EMITTANCE_GROWTH_ANDRE2022`, following this note's residual doubt and §4.8 (p. 18); confidence stays medium.
- The 4 twin-axis Fig. 19 calibration records were lowered from P1 to P0: a graph reading checked for internal consistency is not an arithmetic reproduction.
- `tests/scientific/test_batch7_documents.py::test_andre2022_table4_luminosity_with_hl_lhc_proton_parameters_recorded_band` now uses the proton β* = 10.0 cm in both planes; the recorded ratio moves from ≈ 0.75 to ≈ 0.80, inside the unchanged 0.65–0.85 band.
