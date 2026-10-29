# Verification note: group G7C_MR7_MAGNETS_RF_POWER (G7 IMCC reference tables, 2026-10-29)

Source: SRC_ARXIV_2510_27437. MuCol Milestone Report No. 7, "Consolidated Parameters" (arXiv:2510.27437v1, 93 pp; page header
"Consolidated Parameters Report – November 3, 2025"), category OFFICIAL_CERN, access uploaded. All page numbers below are PDF pages; the
printed page number is PDF − 11 on every page used here. Secondary source for cross-references in notes only: SRC_WS1681458_SCHULTE_IMCC
(D. Schulte, Kraków 2026 deck), slide 45.

File verified (the only file edited): `parameters/machine/imcc_mr7_magnets_rf_power_infrastructure.yaml`.

- 311 records at hand-over and 311 after verification. Added: 0. Removed: 0. Renamed: 25 (listed below).
- Values, units and pages: no value, unit or page was wrong, and none was changed.
- Status: all 311 records are `analogous`, with applicability `analogous`. No record has reported_lhmuc, imported_related,
  derived_lhmuc or analytical_estimate. No record holds a value computed by the extractor, so no record needed a derivation.
- Confidence: 299 medium and 12 low (12 were lowered from medium). None is high.
- Validation: all 311 records are `P0`. None qualifies for P1 (see "P1 decision").
- Fields changed:

  | Field | Records changed |
  |---|---|
  | applicability.explanation | 311 |
  | notes | 105 |
  | validation.notes | 61 |
  | provenance.source.section | 30 |
  | quotation | 25 |
  | name | 25 |
  | parameter_id | 25 |
  | validation.methods | 24 |
  | confidence | 12 |
  | table_figure_or_equation | 10 |

- The file header gained a validation and verification paragraph. The extractor's "Checks: P1 for …" paragraph was replaced.

Role: adversarial verifier. Every record was treated as unverified. For each one I checked value, unit, page, section, table label,
quotation, uncertainty, allowed_range, status, applicability, confidence, derivation, and validation methods and notes.

## Method

1. **Page images.** I rendered every cited page with `pdftoppm` at 200 dpi (Table M.1 also at 250 dpi) and read every table on the
   image: PDF pp. 25, 27, 34, 35, 36, 67, 68, 69, 70, 71, 74, 75, 76, 77, 78, 83, 84, 86 and 89. I also read the following pages for the
   cross-checks quoted in notes:
   - p. 13 (Table 1.1), p. 14 (Table 1.2), p. 19 (Section 6 text and the Table 6.1 footnotes), p. 20 (Tables 6.1 and 6.2);
   - p. 29 (Table 12.3), p. 30 (Table 12.4), p. 42 (Table B.2), p. 85 (Table L.1);
   - Schulte slide 45.

   The text layer in the session scratchpad was used only to locate passages.
2. **Cells.** I typed an independent transcription of every in-scope cell and text value from the images. A script compared value,
   unit and the cell text or quoted fragment with all 311 records (`…/scratchpad/verify_g7c/scripts/expected.py`, `cellcheck.py`).
   Result before and after the edits: 311 compared, 0 mismatches.
3. **Quotations.** All 54 text quotations were normalised and searched in the page text layer (`qcheck.py`). 51 were found. The other
   3 were confirmed on the images:
   - The sentence "The JE values were compared … aiming at 2.5 K margin for HTS operating at 20 K." runs from p. 67 to p. 68, across
     Table H.1. It is used by 2 records.
   - The radical sign of "√(fRF)" (p. 25) is rendered as 'p' in the text layer.
   - Every cell transcription ('Row …, column …: x') and every caption in `table_figure_or_equation` matches the image.
4. **Arithmetic.** Every check named in `validation.methods` or `validation.notes` was recomputed, and so were the cross-checks I
   added (`recompute.py`). Constants: c = 299 792 458 m/s, e = 1.602176634e-19 C, Bρ[T·m] = p[GeV/c]/0.299792458.
5. **Edits and diff discipline.** All edits were made by one script (`apply_edits.py`). It loads the records, modifies them as dicts
   and re-emits them with the generator's own layout (`emitlib.py`); the round trip of the untouched file is byte-identical.
   - A field-level diff (`diffrec.py`) confirmed that only the fields counted above changed.
   - `tools/validate_yaml.py provenance` reports 0 schema errors.
   - `uv run python -m lhmuc validate` reports 0 errors and 0 warnings, the same as before the edit.
   - `uv run pytest` passes except two sync tests that depend on the lead's registry stage: `test_csv_registries_in_sync` and
     `test_source_parameters_extracted_in_sync`. Both already fail for the new G7 files of every group, including the Schulte source.

## Corrections

### 1. Ids renamed (25), because the old id named a quantity that MR7 itself contradicts

**LEP2 cavity (Table I.5, p. 74).** Table I.5 heads its columns as follows:

- 352 MHz column (15 MV/m, 4 cells, 1.686 m active length): **'Value linearizer'**.
- 1056 MHz column (25 MV/m, 6 cells, 0.845 m): **'Value accelerator'**.

Table I.6 on the same page assigns the roles the other way round:

- **'RLA2 acc'**: 352 MHz, synchronous phase 95° (90° = on-crest), 15.2 GV, 600 cavities, 200 cryomodules, 1110.6 m.
- **'RLA2 lin'**: 1056 MHz, 275°, 1.69 GV, 80 cavities, 16 cryomodules, 80.8 m.

Table I.6 reproduces the Table I.5 cavities by frequency, not by label:

| Frequency | Table I.6 voltage per cavity | Table I.5 gradient × active length | Table I.6 section length per cavity | Table I.5 total length |
|---|---|---|---|---|
| 352 MHz | 15.2 GV / 600 = 25.33 MV | 15 MV/m × 1.686 m = 25.29 MV | 1110.6 m / 600 = 1.851 m | 1.851 m |
| 1056 MHz | 1.69 GV / 80 = 21.125 MV | 25 MV/m × 0.845 m = 21.125 MV | 80.8 m / 80 = 1.010 m | 1.011 m |

The ids `ACC_RF_LEP2_LINEARIZER_*` and `ACC_RF_LEP2_ACCELERATOR_*` therefore asserted a role that MR7 contradicts. I renamed the ids to
neutral, frequency-keyed ones:

- LINEARIZER → 352MHZ, for FREQUENCY, GRADIENT, R_OVER_Q, ACTIVE_LENGTH, TOTAL_LENGTH, CELLS, EPEAK_OVER_EACC, BPEAK_OVER_EACC,
  CELL_COUPLING, IRIS_APERTURE_INNER_CELL, IRIS_APERTURE_END_CELL and Q0_MIN (12 ids, e.g. `ACC_RF_LEP2_LINEARIZER_GRADIENT_MR7` →
  `ACC_RF_LEP2_352MHZ_GRADIENT_MR7`).
- ACCELERATOR → 1056MHZ, for the same 12 quantities.

The names now state the printed header and the Table I.6 role. Every record's notes preserve the conflict, which was not averaged. The
values stay at confidence medium: they are consistent per frequency.

**Table I.10 row (p. 77).** `ACC_RF_RCS_CERN_ALL_AVG_RF_POWER_TO_BEAM_MR7` became `ACC_RF_RCS_CERN_ALL_AVG_RF_POWER_MR7`.

- The row is printed 'Average RF power to beam during cycle'. Its per-ring values (2.31 / 11.2 / 12.1 MW) equal total peak RF power ×
  RF duty factor (2.29 / 11.21 / 12.04 MW) and average cavity power × N_cav (2.310 / 11.20 / 12.08 MW). That is the power into the
  cavities, the quantity Table I.8 labels 'to cavity'.
- 'Peak RF power to beam' × duty gives only 1.84 + 5.34 + 9.19 = 16.4 MW.
- The value is unchanged (25.6 MW). The label inconsistency is recorded in the name and the notes.

None of the 25 old ids is referenced by any parameter, scenario, test or document other than the lead's logs
`research/_fragments/confidence_caps_applied_2026-10-29.csv` (all 25) and `validation_levels_lowered_2026-10-29.csv` (the TO_BEAM id).
Those logs are not mine and were not edited. The ids referenced by `scenarios_addendum_imcc.yaml` and by
`parameters/source/cooling_rf_thin_windows_giove2026.yaml` were kept:

- ACC_RF_RCS_GF_ALL_AVG_WALL_PLUG_POWER_MR7
- MACHINE_MAGNET_NB3SN_ASSESSMENT_MR7
- MACHINE_IMPEDANCE_MOMENTUM_COMPACTION_TABK3_MR7
- MACHINE_IMPEDANCE_COLLIDER_CHROMATICITY_REQUIRED_MR7
- SOURCE_DEMO_CELL_RF_GRADIENT_MR7
- SOURCE_DEMO_CELL_RF_FREQUENCY_MR7

### 2. Confidence medium → low (12)

- **`IR_MAGNET_IR_QUAD_APERTURE_MAX_MR7` (280 mm) and `IR_QUAD_APERTURE_MAX_MR7` (200 mm).** Table 9.1 (p. 25) gives an
  IR-quadrupole aperture of '100 - 280' mm. Appendix H.2 (p. 70) says "The IR quadrupoles are expected to reach magnetic fields up to
  20 T and apertures up to 200 mm". MR7 does not reconcile them.
  - Table 12.4 (p. 30, IR lattice v0.8) lists coil apertures of 7.0–14.5 cm for the final-focus quadrupoles. Read as radii they are
    140–290 mm diameters. The radius reading is mine: the beam aperture column is labelled 'radius', the coil column is not, and every
    coil value exceeds its beam radius.
  - Both upper ends are now low until the conflict gets a treatment.
- **Nine wall-plug records.** Their printed values are 5–21 % below the value the Table I.8 caption's own assumptions give
  (average RF power × 1.32 / 0.65):

  | Record | Printed (MW) | Caption gives (MW) | Difference |
  |---|---|---|---|
  | `ACC_RF_RCS_GF_ALL_AVG_WALL_PLUG_POWER_MR7` | 59.3 | 68.64 | −13.6 % |
  | `ACC_RF_RCS1_GF_WALL_PLUG_POWER_MR7` | 4.22 | 4.508 | −6.4 % |
  | `ACC_RF_RCS2_GF_WALL_PLUG_POWER_MR7` | 5.11 | 5.402 | −5.4 % |
  | `ACC_RF_RCS3_GF_WALL_PLUG_POWER_MR7` | 7.79 | 8.428 | −7.6 % |
  | `ACC_RF_RCS4_GF_WALL_PLUG_POWER_MR7` | 42.2 | 50.36 | −16.2 % |
  | `ACC_RF_RCS_CERN_ALL_AVG_WALL_PLUG_POWER_MR7` | 45.0 | 51.99 | −13.4 % |
  | `ACC_RF_RCS1_CERN_WALL_PLUG_POWER_MR7` | 4.34 | 4.691 | −7.5 % |
  | `ACC_RF_RCS2_CERN_WALL_PLUG_POWER_MR7` | 18.0 | 22.74 | −20.9 % |
  | `ACC_RF_RCS3_CERN_WALL_PLUG_POWER_MR7` | 22.7 | 24.57 | −7.6 % |

  MR7 states no other method, so what the numbers include is uncertain. This matches the G7A verifier's treatment of the energy loss
  per turn, a printed value inconsistent with its own stated assumption. The scenario role `rcs_rf_wall_plug_power` of IMCC-MR7-10TEV
  points to the first of these records, which is now low.
- **`SOURCE_DEMO_CTF3_AVG_BEAM_POWER_MR7` (1.5 kW).** The same table's 14 GeV × 10^13 protons × 0.064 Hz gives 1.436 kW (1.438 kW
  with 1/15.6 s), 4.5 % below the printed value and outside its rounding.

### 3. Quotations (25)

- **19 Table 9.1 records.** These are the 8 'SC dipole' and 11 'CF' cells. The extractor quoted invented row labels 'RCS (continued)'
  and 'Collider arc (continued)'; the Complex cell of these rows is blank in print. They now read "Row 'SC dipole' (second RCS row;
  Complex cell blank in print)" and "Row 'CF' (second Collider-arc row; Complex cell blank in print)".
- **2 records** (`MACHINE_MAGNET_NB3SN_FIELD_LIMIT_MR7`, `MACHINE_MAGNET_NB3SN_ASSESSMENT_MR7`): the text-layer artefact
  '– Nb3 Sn (4.5 K)' became '– Nb3Sn (4.5 K)', as printed with a subscript.
- **`MACHINE_RF_GRADIENT_FREQUENCY_SCALING_MR7`:** 'sqrt(fRF)' became '√(fRF)', as printed.
- **`SOURCE_DEMO_CELL_DIPOLE_FIELD_MR7` and `SOURCE_DEMO_CELL_WEDGE_MATERIAL_MR7`:** the Table 14.2 sub-section ('Dipole', 'Wedge') is
  now named in the cell transcription.
- **`SOURCE_DEMO_SITE_MR7`:** the quotation covered only the TT7 sentence, while the categorical value also claims the LIL/CLIC
  history and the PS link. Two further verbatim p. 84 sentences were added ('The CTF3 building hosted the LIL …', 'Protons would be
  extracted from the PS …').

### 4. Sections (30) and table labels (10)

- **Two Appendix H records** (`SOURCE_COOLING6D_SOLENOID_OPERATING_TEMPERATURE_MR7` and `…_TEMPERATURE_MARGIN_MR7`). The generator
  had left the artefact "H.1.1 … (printed p. 56)-57". The section now reads "H.1.1 Baseline 6D Cooling solenoids (the sentence starts
  on PDF p. 67 and ends on PDF p. 68, after Table H.1; printed pp. 56-57)".
- **Table 14.1 records (6):** "printed pp. 23-25" became "printed p. 24".
- **`SOURCE_DEMO_CELL_REFERENCE_MR7`:** "printed pp. 23-25" became "printed p. 23".
- **20 Table L.2 records:** these claimed section "L.1 …". The section is now "Appendix L, Table L.2 (cited in L.1, printed after
  the L.2.1 heading; printed p. 75)".
- **`SOURCE_DEMO_SITE_MR7`:** the section now names L.1 and L.2.
- **10 Table I.10 records:** the caption is "… CERN-based RCS acceleration chain." in lower case. The extractor had written
  "Acceleration Chain".

### 5. Unsupported claims in notes, removed or corrected

- **`SOURCE_MAGNET_COOLING6D_SOLENOID_COUNT_MR7` (≈ 6000).** The extractor explained the gap to H.1.1's 3054 solenoids with "this row
  counts solenoid coils". MR7 does not say this; the target row (23) is also labelled 'Solenoid Coils'. The note now says that the
  factor ≈ 2 is unexplained. It adds that 2 × 3054 = 6108 would match if both charge-separated lines were counted (p. 16: charge
  separation "splits the positive and negative muon species into separate beamlines"), but that MR7 does not say so.
- **`MACHINE_MAGNET_NBTI_ASSESSMENT_MR7`.** The extractor attributed Schulte slide 45 ('NbTi at 4 K, 4.8 T, 16 cm aperture') to a
  "3.2 TeV CERN variant", which the slide does not say. The note now quotes the slide's three 'Dipoles appear feasible' lines and says
  that they concern NbTi at 4 K and 4.8 T, not the 1.9 K high-field case.
- **`MACHINE_IMPEDANCE_TOTAL_RF_VOLTAGE_TABK3_MR7`.** "Table 6.1 lists 30 MV to compensate synchrotron-radiation losses" was made
  precise: the Table 6.1 row is 'Integrated RF gradient' 30 MV, with footnote 4 'Assuming that only the synchrotron radiation losses
  have to be compensated.'
- **`ACC_RF_RCS2_CERN_WALL_PLUG_POWER_MR7`.** "typo for RCS2" became "presumably RCS2", since MR7 prints 'RC2 LHC'.
- **`MACHINE_IMPEDANCE_MOMENTUM_COMPACTION_TABK3_MR7`.** The isochronicity quote is now attributed to its page (Appendix K.1, p. 82).

### 6. Over-claimed reproductions corrected

The extractor's P1 claims hid two kinds of mismatch inside a ±2 or ±0.2 tolerance:

- **'All' RF section lengths:** 1079 + 684 + 614 + 2838 = 5215 m vs 5214 m (Table I.8), and 903 + 1888 + 2449 = 5240 m vs 5241 m
  (Table I.10). The validation notes now say NOT reproduced exactly (1 m, rounding level).
- **Table I.10 'All' voltage:** 134.2 GV vs 134.0 GV, at the edge of the ±0.2 GV that rounding allows.

### 7. Applicability explanations (all 311)

The extractor used nine generic explanations. They were replaced by 15 variants, each with page-specific caveats and an
energy-stage attribution:

- **Table 9.1:** split into source solenoids (common to the 3 and 10 TeV stages, Table 1.2), RCS dipoles, and 10 TeV collider magnets.
  - The verifier's integrated-bending check confirms the 10 TeV attribution of the arc rows. The arc rows give
    1050 × 5 m × 14 T + 628 × (5–10 m) × (4–8 T) = 86 060–123 740 T·m. This brackets 2πBρ(5 TeV) = 104 792 T·m and is far above the
    31 438 T·m needed at 1.5 TeV.
  - All three variants quote "not yet to specification", "bound to adapt" and "work in progress".
- **Appendix H:** split into H.1 (6D solenoids: "not feasible from the point of view of cell integration", "Further optimization
  will be needed") and H.2 (collider magnets: "exceeds current technological limits", 3 TeV vs 10 TeV for Nb3Sn).
- **Table 10.1:** "to be used in the beam dynamics studies", i.e. study inputs, not demonstrated performance.
- **Reference cavities:** LEP2 (I.2, RLA2, with the label conflict) and TESLA (I.3, "initial beam dynamics and power requirements
  studies").
  - The extractor's single cavity text had applied the I.3 ILC caveat to the LEP2 cavity.
- **RCS RF:** greenfield (RCS1–RCS4 to 5 TeV, 10 TeV collider), CERN-site ("Tentative parameter tables", App. F.1) and caption
  assumptions (ILC DKS, Table I.7).
  - The extractor's quote omitted "[41]" without an ellipsis.
- **Power converters:** the explanation keeps the conservative all-dipole assumption.
- **Impedance:** the explanation says that the model uses a 10 000 m ring (≈ 10 km lattice), not the 11.4 km baseline.
- **Demonstrator:** split into Section 14 and the CTF3 option of Appendix L (still being studied, 'TBD' entries).
- **CERN civil engineering:** the explanation names the "new 10 km Collider Ring".

### 8. Notes added: cross-references and preserved conflicts

| Record | What the note adds |
|---|---|
| `SOURCE_MAGNET_COOLING6D_SOLENOID_FIELD_MAX_MR7` | Table H.1/H.2 peak coil fields up to 19.2 / 16.5 T; Table 9.1 does not say on-axis vs peak |
| `ACC_MAGNET_RCS_NC_DIPOLE_RAMP_MR7` | mean ramp rates implied by Tables J.1/J.2 (see arithmetic) |
| `MACHINE_MAGNET_ARC_DIPOLE_APERTURE_MR7`, `…_ARC_CF_APERTURE_MR7` | 2 × 69 mm coil radius of Table 6.2; App. H "160 mm"; Schulte "HTS at 20 K, 14 T, 14 cm aperture" |
| `MACHINE_MAGNET_ARC_DIPOLE_FIELD_MR7`, `MACHINE_ARC_MAGNET_DESIGN_FIELD_MAX_MR7` | Table 1.1 14 T; Table 6.1 footnote 2 "assumes a collider arc peak field of 16 T, but will likely be updated later to reduce the field to 14 T" |
| `MACHINE_ARC_MAGNET_DESIGN_APERTURE_MAX_MR7` | 140 mm (Tables 9.1/6.2) vs 160 mm; 40 mm absorber of Table 12.3 → 158 mm; Schulte pairs 16 cm with 4 K LTS; not reconciled |
| IR-quadrupole gradient pair | the `**` caveat and App. H "up to 300 T/m … up to 140 mm" |
| Appendix H B10-1 and low-stress records | consistency with Table H.1/H.2 rows |
| `SOURCE_COOLING6D_CHANNEL_LENGTH_MR7` | 0.85 km = 363 + 487 m of Table A.2 |
| Impedance chamber length and circumference | 11.4 km (Table 1.1) vs ≈ 10 km (Section 6) vs 10 000 m |
| `MACHINE_IMPEDANCE_CHAMBER_RADIUS_TAB113_MR7` | 23 mm vs the 23.5 mm of the text and Table 6.2 |
| J.1 LHC1 / LHC2 acceleration times | 2.60 vs 2.58 ms and 4.42 vs 4.41 ms (Table I.10); J.1 LHC1 duty cycle '≈ 2.8' breaks the duty = t_acc pattern |
| Table 14.1 end values | the text announces "two different cooling channel lengths", the table shows one |
| Demonstrator cell RF gradient and Table 10.1 704 MHz conservative gradient | both 30 MV/m |
| `ACC_RF_RCS_ADDITIONAL_POWER_FRACTION_MR7`, `ACC_RF_RCS_KLYSTRON_EFFICIENCY_MR7` | Table I.7 |
| Table M.1 notes | page references; '◦2400' with the caption meaning of ◦ |

## Arithmetic checks, recomputed independently

"Yes" = reproduces the printed value. Every record whose methods or notes carried generator arithmetic now has a "G7C verifier
2026-10-29: …" validation note.

### RCS RF, Table I.8 (greenfield) and Table I.10 (CERN site)

| Record (check) | Result | Reproduces |
|---|---|---|
| GF 'All' voltage | 27.6 + 17.5 + 15.7 + 72.7 = 133.5 vs 133.0 GV; N × 30 MV/m × 1.065 m = 133.55 | **No** (−0.37 %) |
| GF 'All' cavities | 865 + 548 + 492 + 2275 = 4180 | Yes, exact |
| GF 'All' cryomodules | 97 + 61 + 55 + 253 = 466; Σ ceil(N/9) = 97 + 61 + 55 + 253 = 466 | Yes, exact |
| GF 'All' RF section length | 1079 + 684 + 614 + 2838 = 5215 vs 5214 m; N × 1.247 m = 5212.5 m; cells imply 1.2474–1.2482 m per cavity | **No** (1 m) |
| GF 'All' klystrons | 109 + 50 + 41 + 91 = 291; Σ ceil(N/cav per klystron) = 109 + 50 + 41 + 91 = 291 | Yes, exact |
| GF 'All' average RF power to cavity | 2.22 + 2.66 + 4.15 + 24.8 = 33.83 → 33.8 MW; per ring = peak RF × duty (2.217, 2.645, 4.145, 24.85) = avg cavity power × N (2.223, 2.658, 4.153, 24.80) | Yes |
| GF 'All' wall plug | per-ring sum 59.32 → 59.3 (yes); caption × 1.32/0.65 = 68.64 (−13.6 %) | Sum yes, caption **no** |
| GF RCS1–RCS4 wall plug | × 1.32/0.65 = 4.508, 5.402, 8.428, 50.36 vs 4.22, 5.11, 7.79, 42.2 (−6.4, −5.4, −7.6, −16.2 %); P/0.65 + 0.32 P gives +2.3, +3.4, +1.0, −8.4 %; printed/RF ratios 1.90, 1.92, 1.88, 1.70 ≠ 2.031 | **No** |
| CERN 'All' voltage | 23.1 + 48.4 + 62.7 = 134.2 vs 134.0 GV; N × 31.95 MV = 134.25 | **No** (−0.15 %) |
| CERN 'All' cavities | 724 + 1514 + 1964 = 4202 | Yes, exact |
| CERN 'All' cryomodules | 81 + 169 + 219 = 469; Σ ceil(N/9) = 469 | Yes, exact |
| CERN 'All' RF section length | 903 + 1888 + 2449 = 5240 vs 5241 m; per ring = N × 1.247 m to the metre | **No** (1 m) |
| CERN 'All' klystrons | 104 + 109 + 58 = 271; Σ ceil(724/7, 1514/14, 1964/34) = 271 | Yes, exact |
| CERN 'All' average RF power (renamed) | 2.31 + 11.2 + 12.1 = 25.61 → 25.6; per ring = peak RF × duty (2.29, 11.21, 12.04); beam-power reading 16.4 | Sum yes; label **no** |
| CERN 'All' wall plug | sum 45.04 → 45.0 (yes); caption 51.99 (−13.4 %) | Sum yes, caption **no** |
| CERN RCS1–RCS3 wall plug | 4.691, 22.74, 24.57 vs 4.34, 18.0, 22.7 (−7.5, −20.9, −7.6 %) | **No** |
| `ACC_RF_RCS_CAVITIES_PER_CRYOMODULE_MR7` | Σ ceil(N/9) = 466 (I.8) and 469 (I.10) | Yes |

Also checked, as consistency of the I.8 inputs: RF pulse = filling + acceleration time (0.60, 1.53, 2.82, 7.43 ms, exact) and duty =
pulse × 5 Hz (0.30, 0.765 → 0.76, 1.41, 3.715 → 3.72 %).

### Reference cavities, Tables I.5, I.6 and I.9

| Record (check) | Result | Reproduces |
|---|---|---|
| LEP2, Table I.6 cross-check | 15.2 GV/600 = 25.33 vs 25.29 MV; 1110.6/600 = 1.851 m; 1.69 GV/80 = 21.125 = 21.125 MV; 80.8/80 = 1.010 vs 1.011 m | Yes, by frequency; the role labels are inverted |
| LEP2 active lengths vs N × λ/2 | 4 × λ/2 (352 MHz) = 1.703 m vs 1.686 (−1.0 %); 6 × λ/2 (1056 MHz) = 0.852 vs 0.845 (−0.8 %) | Approximately |
| TESLA active length | 9 × λ/2 at 1.3 GHz = 1.038 m vs 1.065 m (+2.6 %) | **No** |
| TESLA active length, used consistently | V/N_cav in I.8/I.10 = 31.91–31.96 MV = 30 MV/m × 1.065 m (31.95 MV) | Yes |
| TESLA total length | I.10 per ring N × 1.247 = 902.8 / 1888.0 / 2449.1 m vs 903 / 1888 / 2449 | Yes (I.8 within 0.05 %) |

### Power converters, Tables J.1 and J.2

| Record (check) | Result | Reproduces |
|---|---|---|
| Peak power (7 columns) | V_ind × 12 kA = 120.0 / 94.8 / 76.8 / 141.6 / 60.0 / 48.0 / 84.0 GW vs 110 / 87 / 70 / 130 / 55 / 44 / 77 (ratio 0.9115–0.9181); V_ind × 11 kA = 110.0 / 86.9 / 70.4 / 129.8 / 55.0 / 44.0 / 77.0 matches all seven | V·I **no**; empirical 11 kA fit yes (convention unstated) |
| Resistive/inductive ratio | 0.290, 1.684, 1.438, 0.220, 0.360, 0.775, 2.086 % vs 0.29, 1.7, 1.4, 0.22, 0.36, 0.77, 2.08 | Yes (cells not extracted) |
| Acceleration times vs I.8/I.10 | GF 0.34 / 1.10 / 2.37 / 6.37 ms = I.8; SPS 0.45 = I.10 | Yes |
| LHC1, LHC2 acceleration times | 2.60 vs I.10 2.58 ms; 4.42 vs 4.41 ms | **No** |

### Impedance, Tables 11.3 and K.3

| Record (check) | Result | Reproduces |
|---|---|---|
| K.3 ε_l = σ_z σ_E | 1.5 mm × (1e−3 × 5 TeV) = 7.5 MeV·m (relaxed 5 mm × 0.3e−3 gives the same); / c = 0.02502 eV·s vs Table 1.1 0.025 eVs | Yes, exact |
| K.3 bunch length | c × 0.025 eVs / (1e−3 × 5 TeV) = 1.499 mm vs 1.5 | Yes (consistency; see P1 decision) |
| Table 11.3 chamber radius | 23 mm vs text 23.5 mm and Table 6.2 23.49 + 0.01 mm | **No** (model value kept) |

### Demonstrator, Table L.2

| Record (check) | Result | Reproduces |
|---|---|---|
| CTF3 repetition rate | 1/15.6 s = 0.0641 → 0.064 Hz | Yes |
| CTF3 average beam power | 14 GeV × 1e13 × 0.064 Hz = 1.436 kW vs 1.5 (needs 0.0669 Hz or 1.045e13) | **No** |

### Civil engineering, Table M.1

| Record (check) | Result | Reproduces |
|---|---|---|
| ARCR length | π × 200 m = 628.3 → 628 m; equals the Table B.2 compressor circumference 628 m (p. 42) | Yes |
| Cooling length vs Table 1.2 | 12 + 363 + 134 + 424 + 100 = 1033 m vs 1000 m | **No** (different definitions; kept) |
| RLA2 racetrack | 2300 m vs ◦2400 (Table 1.2) and 2430 (Table A.2) | **No** (kept) |

### Magnets, Table 9.1 and Appendix H

| Record (check) | Result | Reproduces |
|---|---|---|
| Arc rows, integrated bending | 86 060–123 740 T·m brackets 2πBρ(5 TeV) = 104 792 T·m | Yes (10 TeV attribution) |
| Arc dipole aperture | 2 × 69 mm = 138 mm (Table 6.2) vs 140 mm | Yes, within 2 mm |
| 6D-cooling count | Table 9.1 ≈ 6000 vs H.1.1 3054 (2 × 3054 = 6108) | **No** (unexplained in MR7) |
| `SOURCE_COOLING6D_CHANNEL_LENGTH_MR7` | 363 + 487 m (Table A.2) = 850 m = 0.85 km | Yes |
| Cell and solenoid types | Table H.1: 14 cell rows and 26 coil rows | Yes |
| B10-1 values | Table H.1 row: 19.2 T, 378 MPa, 49 MPa | Yes |
| Low-stress counts | Table H.2: radial > 20 MPa only for B8-1 / B9-1 / B10-1 (23.7 / 28.8 / 30.9); hoop > 300 MPa only for B9-1 / B10-1 (301.4 / 333.6); B_peak > 15 T only for those three (15.3 / 15.7 / 16.5) | Yes |
| RCS NC ramp rate | 2 × 1.8 T / t_acc (J.2) = 10 588 / 3 273 / 1 519 / 565 T/s; (J.1) 8 000 / 1 385 / 814 T/s | No relation reproduces 4200 T/s (informational) |

## P1 decision

No record of this file is pinned by `tests/scientific/test_imcc_mr7_reference.py`. Its seven MR7 tests concern the collider's beam
power, IP beam size, luminosity lifetime, hourglass and decay factors, eq. A.9 luminosity and integrated luminosity. All 311 records
stay P0, and every validation note says so.

The closest case is `MACHINE_IMPEDANCE_BUNCH_LENGTH_TABK3_MR7` (1.5 mm). `test_mr7_analytic_luminosity_eq_a9` asserts
σ_z = c·ε_l/((σ_E/E)·E) = 1.499 mm from the Table 1.1 / p. 39 inputs. But the test does not read Table K.3, and the lead lists its
pinned values as 18.8e34 and B_avg 10.5 T ↔ C 9.98 km. The G7A verifier also kept the Table 1.1/A.1 σ_z records at P0, so I did not
claim P1. If the lead regards that assertion as pinning the 10 TeV rms bunch length, this record and the collider file's σ_z records
qualify together. No record cites a test, and no test name was invented.

## Removed

None. Every record is supported by the cited page and every value is an exact cell or text value:

- none was read from a figure, taken from the wrong stage, table or column, or rounded beyond the printed precision;
- the 24 LEP2 records are correct cells under disputed column labels, so they were renamed, not removed.

## Conflict candidates for the lead

These were not added to `research/source_conflicts.yaml`, which is not my file. Per `research/source_quality_policy.md` §4, once one
is recorded without a decided treatment, its competing records drop to low.

1. **IR-quadrupole aperture upper end:** Table 9.1 280 mm vs Appendix H.2 200 mm. Table 12.4 coil apertures, if read as radii, give
   up to 290 mm. Records already low: IR_MAGNET_IR_QUAD_APERTURE_MAX_MR7 and IR_QUAD_APERTURE_MAX_MR7.
2. **RLA2 cavity roles:** Table I.5 headers vs Table I.6 (24 LEP2 records, now frequency-keyed).
3. **Table I.10 row label** 'Average RF power to beam during cycle' vs its content, the cavity input power (ACC_RF_RCS_CERN_ALL_AVG_RF_POWER_MR7).
4. **RCS RF wall-plug powers:** Tables I.8/I.10 vs the caption's 32 % / 65 % assumptions (9 records, now low).
5. **6D-cooling solenoid count:** Table 9.1 ≈ 6000 vs H.1.1 3054.
6. **Arc-magnet aperture and field:** Table 9.1 140 mm and 14* T vs Appendix H.2 "up to 16 T and 160 mm".
   - The 14 T vs 16 T part is resolved by MR7 itself (Table 6.1 footnote 2: lattice at 16 T, to be reduced to 14 T).
   - The 140 vs 160 mm part is not.
7. **10 TeV collider circumference:** 10 000 m (Tables 11.3, K.3, M.1; Section 6 ≈ 10 km) vs 11.4 km (Table 1.1). This is the same
   conflict as the G7A note's item 1.
8. **CTF3 average beam power:** 1.5 kW vs 1.44 kW from Table L.2's own inputs (now low).
9. **J.1 'RCS LHC1' acceleration time:** 2.60 ms (duty cycle ≈ 2.8 %) vs Table I.10 2.58 ms.

## Residual doubts

- **J.1/J.2 peak powers.** The "V_ind × 11 kA" regularity is an empirical fit, not a stated formula. In a resonant circuit the
  instantaneous peak of V·I depends on the waveform, which MR7 does not give. The records stay P0 with the observation.
- **Wall-plug derivation.** I could not reproduce it with any reading I tried (×1.32/0.65; P/0.65 + 0.32 P; pulse or acceleration-time
  averaging; per-klystron peak power). The values are kept as printed, at low confidence.
- **TESLA active length 1.065 m.** It is used consistently by MR7 but is 2.6 % longer than 9 × λ/2 = 1.038 m. MR7 cites [41] and [42]
  for Table I.9. I could not check those references (network blocked) and did not change the record.
- **Table 12.4 coil apertures.** Reading them as radii is my inference; the table does not label the unit as radius or diameter.
- **Table 9.1 6D-cooling 'Field' (2–17 T).** It may be on-axis while H.1/H.2 give peak coil fields (up to 19.2 T); MR7 does not say.
- **Table 9.1 RCS rows.** They may refer to the greenfield or the CERN-site chain; MR7 does not say.
- **Table M.1 'Single/Double Width' tunnels (5m x 4m, 8m x 4m).** The records read the first number as the width. This is the natural
  reading, but the caption does not say so; it is kept in the notes.
- **Repository state.** `registries/` and `parameters_extracted` were not rebuilt; that is the lead's registry stage.
  `tools/build_registries.py` and `tools/sync_parameters_extracted.py` must run before the two sync tests can pass. The 25 renamed ids
  appear under their old names in the lead's two CSV logs of 2026-10-29.
- **Other verifiers.** Nothing outside my file was edited. Each of the six ids that other files reference is kept unchanged.
