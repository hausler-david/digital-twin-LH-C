# Verification note — group G9_JPARC_G2_AND_HYBRID_TARGET (SRC_ARXIV_1901_03047, SRC_ARXIV_2605_25580)

Adversarial verifier pass of 2026-10-29 (batch 7) over the G9 extraction of
Abe et al., *A New Approach for Measuring the Muon Anomalous Magnetic Moment and Electric Dipole Moment*
(arXiv:1901.03047v2 / PTEP 2019 053C02, 24 pp.) and Sakaki, Kamioka, Yoshida, *Quantitative Evaluation of a
Hybrid Target for Ultraslow-Muon Production in μTRISTAN* (arXiv:2605.25580v1, 11 pp.).

| file | records | result |
|---|---|---|
| `parameters/source/jparc_g2_design_chain_abe2019.yaml` | 128 → 144 | 16 records added (pp. 4, 15, 16, 17); 72 field corrections in 43 records |
| `parameters/acceleration/jparc_g2_muon_linac_abe2019.yaml` | 78 | 20 field corrections in 19 records, no value error |
| `parameters/source/hybrid_target_mutristan_sakaki2026.yaml` | 76 | 23 field corrections in 22 records, no value error |
| `parameters/machine/scenarios_batch7_source.yaml` | 2 scenarios | 16 roles added, 6 `unknown_roles` resolved, 1 role renamed |

Total records re-checked: 282 (every record); 16 added; **none removed** (no unsupported record found).
Every number the files carry was re-read on the page image; no value, unit or page was wrong.
After the fixes: `tools/validate_yaml.py` 0 schema errors in all four files; `uv run python -m lhmuc validate`
0 errors / 0 warnings; `tests/scientific/test_batch7_documents.py` 14 passed; the full test suite passes except
`tests/unit/test_registry_integrity.py::test_csv_registries_in_sync`, which only needs the lead to run
`tools/build_registries.py` (registries/ is generated and was not touched). Status counts of the 298 records:
analogous 228, imported_related 62, analytical_estimate 4, unknown 4 (value null); **no `reported_lhmuc`**.
Confidence: high 290, medium 4 (the computed records), none 4 (the null records). P1: 11 records.

## 1. What was checked and how

* Abe 2019: pages 2–22 viewed as page images (Table 1, Figs 1–14, Tables 2–6, the full §3–§9 text and the
  reference list on pp. 23–24). Sakaki 2026: all 11 pages viewed as images (Figs 1–7, Table I, Appendices,
  references). Every table cell, figure label and quotation was compared with the image; the text layer was
  machine-compared after whitespace/superscript normalisation (146 of 298 quotations match it verbatim; the
  rest are table-cell transcriptions, page-crossing sentences or garbled text-layer passages, all confirmed
  on the images).
* Every derivation recomputed: 0.52 × 2.1e4 / 3.23e6 = 3.381e-3; product of the 19 Table 4 cells = 1.3511e-5;
  post-H-line product 7.819e-4 → 5.2e12 / (7.819e-4 × 2.2e7 s) = 3.023e8 s⁻¹; Table 2 decay survival
  0.83 × 0.81 × 0.99 × 0.96 × 0.99 = 0.6326; ℓ_diff = √(2e-3 cm²/s × 2.197 µs) = 0.663 µm; (1 − e⁻³)/3 = 0.3167;
  Eq. (1) at 293 K and σ_s = 5 cm → 0.773 π mm mrad; N_p = 1 MW / 3 GeV = 2.08e15 s⁻¹; 6e-4 × 2e15 = 1.2e12.
  Audit notes: γ = 3.010, R = p/eB = 333.56 mm, T_c = 7.41 ns (7.40 ns with R = 333 mm), γτ = 6.61 µs,
  Table 6 quadratic sums 39.6 / 56.1 / 68.8 ppb, 1400/66 = 21.2, 3090/300 = 10.3, 0.44 rad = 25.2°, Fig. 5/Fig. 3
  β and energy labels consistent with relativistic kinematics. All agree with the records.
* All 38 REQUIRED IDS of the brief exist with the stated values (unit `pi mm mrad` for the two exit emittances,
  defined in `lhmuc/units.py` as the same 1e-6 m as `mm mrad`). The four recomputed records keep status
  `analytical_estimate` instead of the brief's "derived_lhmuc": the schema defines `derived_lhmuc` as
  "computed from reported LHμC values", which J-PARC values are not — the extractor's deviation is correct.
* Both scenarios: machine/status as required; MUTRISTAN-HYBRID-TARGET-2026 lists η_conv, extraction
  efficiency, extracted μ+ rate and emittance after extraction in `unknown_roles` as required.

## 2. Corrections applied — Abe 2019 source chain (`jparc_g2_design_chain_abe2019.yaml`)

| record(s) | field | before → after | reason |
|---|---|---|---|
| MACHINE_FIELD_UNIFORMITY_LOCAL_ABE2019 | quotation | "MRI-type solenoid …" → "Magnetic Resonance Imaging (MRI)-type solenoid storage ring with 1 ppm local magnetic field uniformity for the muon storage region" | not verbatim (p. 3 prints "(MRI)-type") |
| MACHINE_CYCLOTRON_PERIOD_ABE2019 | notes | "2πR/(βc) with R = 333 mm … gives 7.41 ns" → 7.41 ns from 2πγm/(eB) (R = p/eB = 333.6 mm); 7.40 ns with R = 333 mm | arithmetic in the note was wrong (7.399 ns for R = 333 mm) |
| MACHINE_SOLENOID_DIAMETER_RATIO_VS_PREVIOUS_G2_ABE2019 | uncertainty.note | "source says 'about (p. 12)'" → "the abstract (p. 2) says 'a factor of 20'; p. 12 says 'about a factor of 20'" | garbled note |
| SOURCE_PROTON_ACCELERATOR_ABE2019 | value | "Rapid Cycle Synchrotron (J-PARC RCS)" → "Rapid Cycle Synchrotron" | categorical value carried text not on the page; identification moved to notes |
| PHYS_DETECTED_ELECTRONS_TABLE1_ABE2019 | value | "none: Table 1 cell is '−' (μ+ experiment, no e− are detected)" → "not applicable (Table 1 cell '−')" | unquoted interpretation removed from the value; reason moved to notes with the p. 4 quotation |
| 14 §8 records (10 Table 4 cells + SOURCE_G2_CHAIN_EFFICIENCY, …_PRODUCT, PHYS_EXPECTED_POSITRONS_1MW, MACHINE_DATA_TAKING_TIME) | section | "8 Sensitivity (Table 4)" → "8 Estimation of the number of reconstructed positrons (Table 4)" | §8 title as printed on p. 18 |
| SOURCE_G2_CHAIN_EFFICIENCY_ABE2019, SOURCE_G2_CHAIN_EFFICIENCY_PRODUCT_ABE2019, PHYS_EXPECTED_POSITRONS_1MW_ABE2019, MACHINE_DATA_TAKING_TIME_ABE2019 | quotation | "is 1.3 × 10^−5 …" → "The total efficiency is 1.3 × 10^−5 per initial muon at production. …" | sentence starts at the foot of **p. 18**; notes said "foot of p. 19 (below Fig. 13)" — p. 19 is a full-page figure. Page-crossing documented in notes |
| SOURCE_G2_CHAIN_EFFICIENCY_ABE2019 | name, validation | name aligned with "total efficiency … per initial muon at production"; P0 → **P1** (`test_abe2019_table4_overall_efficiency_product`) | the stated 1.3e-5 is pinned by the lead's test |
| SOURCE_THERMAL_MU_EFFICIENCY_CHECK_ABE2019, SOURCE_G2_CHAIN_EFFICIENCY_PRODUCT_ABE2019, SOURCE_HLINE_RATE_IMPLIED_BY_TABLE5_ABE2019 | confidence | high → **medium** | batch-7 rule: "high" only for values read on the page image; these are computed |
| SOURCE_HLINE_RATE_IMPLIED_BY_TABLE5_ABE2019 | notes | added the audit assumption (Table 5 count after kicker decay; 2.81e8 s⁻¹ if counted before, < 7 %) and the per-fill cross-check | interpretive assumption made explicit |
| SOURCE_MUONIUM_FORMATION_PROBABILITY_ABE2019 | notes | rewritten: origin **Bakule et al. 2013, SRC_ARXIV_1306_3810, p. 3** ("…the fraction of muonium formed in the three aerogel samples was 0.52 ± 0.01", verified on the uploaded file); Abe et al. cite Bakule et al. (PTEP 2013, 103C01) as ref. [29] on p. 8; "conflict … already open" → conflict id named in the source registry but **absent from `research/source_conflicts.yaml`** | lead note 2026-10-29; the old wording asserted a conflict entry that does not exist |
| SOURCE_THERMAL_MU_EFFICIENCY_ABE2019, SOURCE_THERMAL_MU_EFFICIENCY_CHECK_ABE2019, SOURCE_G2_EFF_MU_EMISSION_ABE2019, SOURCE_FIG4_BEAM_MUONS_ABE2019, SOURCE_FIG4_MU_IN_LASER_REGION_PEAK_ABE2019 | notes | appended the Bakule 2013 origin of the 0.52 | lead note (records that use or quote 0.52); values and statuses unchanged |
| 17 records (see list) | applicability.explanation | appended the reference the paper itself cites | batch-7 rule (name the original source where the document cites one) |
| SOURCE_LASER_IONISATION_EFF_CALC_ABE2019 | notes, validation.notes | "far lower efficiency (SRC_ARXIV_2410_11367)" → Aritome 2024 simulated 7e-6–6e-5 (244 nm) and projected "around 10%" with 122/355 nm, defined relative to all emitted muonium incl. decay (not directly comparable); P1 flagged as a consistency check only | vague claim replaced by the actual records; 73 % stays an unvalidated calculation |
| SOURCE_THERMAL_MU_EFFICIENCY_ABE2019 | validation.check_ids | second pinning test moved from `notes` into `check_ids` | completeness |
| DET_G2_EFF_RECONSTRUCTION_ABE2019, MACHINE_STORED_MUONS_TOTAL_ABE2019, MACHINE_STORAGE_FIELD_INTEGRATED_UNIFORMITY_ABE2019, MACHINE_FIELD_INDEX_ABE2019, MACHINE_KICKER_COIL_HEIGHT_ABE2019, MACHINE_INJECTION_SCHEME_ABE2019, MACHINE_FIELD_UNIFORMITY_LOCAL_ABE2019 | notes | supporting quotation (p. 18 "> 90%") or cross-references to the new records | traceability |

Explanations extended with the cited reference (17): SOURCE_SURFACE_MU_FOCUS_SIGMA_X/Y ([27] G4beamline),
SOURCE_HLINE_OPTICS_CONCEPT ([26] Kawamura et al., PTEP 2018 113G01), SOURCE_MUONIUM_EMISSION_ENHANCEMENT_ABLATION
([29] Bakule 2013, [30] Beer 2014), SOURCE_THERMAL_MU_EFFICIENCY, SOURCE_G2_EFF_MU_EMISSION, SOURCE_FIG4_BEAM_MUONS,
SOURCE_FIG4_MU_IN_LASER_REGION_PEAK, SOURCE_LASER_IONISATION_OPTIMUM_TIME ([30] Beer et al. 2014, diffusion fit),
SOURCE_LYMAN_ALPHA_GENERATION, SOURCE_LASER_PUMP_AMPLIFIER_STAGES, SOURCE_LASER_FREQUENCY_CONVERTER_STAGES ([31] Saito
et al. 2016), PHYS_EDM_IMPROVEMENT_FACTOR ([15] Bennett et al. 2009), MACHINE_INJECTION_SCHEME ([49] Iinuma et al. 2016),
MACHINE_STORAGE_MAGNET_TYPE / _HEIGHT_FIG8 / _WIDTH_FIG8 ([47] Sasaki et al. 2016).

## 3. Corrections applied — Abe 2019 linac (`jparc_g2_muon_linac_abe2019.yaml`)

| record(s) | field | change | reason |
|---|---|---|---|
| 9 Table 4 linac cells (ACC_G2_EFF_*) | section | "8 Sensitivity (Table 4)" → "8 Estimation of the number of reconstructed positrons (Table 4)" | §8 title |
| ACC_G2_LINAC_DECAY_SURVIVAL_ABE2019 | confidence | high → medium | computed value |
| ACC_G2_LINAC_IH_MODE_ABE2019 | quotation | extended with "Since the use of APF eliminates the need for installing quadrupoles in the drift tubes, a higher shunt impedance per length can be achieved." | the value's element "no quadrupoles in the drift tubes" was not covered by the quotation |
| ACC_G2_LINAC_RFQ_ORIGIN ([35] Kondo 2013), ACC_G2_LINAC_RFQ_OUTPUT_ENERGY ([36] Kondo IPAC2015), ACC_G2_LINAC_IH_CELLS / _CELLS_TOTAL_LENGTH / _Q0 / _POWER_DISSIPATION / _SHUNT_IMPEDANCE ([40] Otani 2016), ACC_G2_LINAC_DLS_DESIGN_FEATURE ([46] Kondo 2017) | applicability.explanation | cited reference appended | batch-7 rule |

## 4. Corrections applied — Sakaki 2026 (`hybrid_target_mutristan_sakaki2026.yaml`)

| record(s) | field | change | reason |
|---|---|---|---|
| SOURCE_HYBRID_PRE_EXTRACTION_RATE_SAKAKI2026 | uncertainty | not_stated → **order_of_magnitude** (note quotes §IV.D "an order-of-magnitude estimate", Table I caption, idealised upper limit, ∼ 10 % hadronic systematic) | the paper itself labels the Eq. (6) number an order-of-magnitude estimate |
| SOURCE_HYBRID_EMITTED_FRACTION_UNIFORM_3LDIFF_SAKAKI2026 | validation.methods | "within 2 % of 1/3" → "|0.317 − 1/3| = 0.017 absolute (5 % relative), inside the test's 0.02 absolute tolerance" | the method text misstated the agreement |
| 10 Table I records (REMPI, L_x, L_z±, gap, thickness, N_layers, L_y, yield) + SOURCE_HYBRID_HADRONIC_SYSTEMATIC | section | "V Future prospects" → "IV Simulation studies of the proposed target D (Table I)" | Table I floats in the §V column of p. 7 but belongs to §IV.D ("Table I summarizes the target geometry used for this estimation") |
| SOURCE_HYBRID_PROTON_ENERGY, _PION_TARGET_MATERIAL, _STOPPING_TARGET_MATERIAL, _Z_ASYMMETRY; SOURCE_HYBRID_PION_LIFETIME_REFERENCE | section | subsection letters A / C added | precision, consistent with the rest of the file |
| SOURCE_THERMAL_SOURCE_EMITTANCE_ESTIMATE, SOURCE_THERMAL_SOURCE_RMS_SIZE_TYPICAL | applicability.explanation | "value restated" → "estimate made by Sakaki et al. (Eq. 1, citing [10] Reiser)" | the paper makes this estimate itself |
| SOURCE_SURFACE_PION_STOP_YIELD_PER_PROTON_SAKAKI2026 | applicability.explanation | "(H-line design)" gloss → printed title of [11] Kawamura et al. 2018 and the note that Abe et al. cite the same paper as their H-line reference [26] | unquoted gloss replaced by checkable facts |
| SOURCE_AEROGEL_MUONIUM_FORMATION_SAKAKI2026 | notes, explanation | Bakule 2013 origin of 0.52 added (Sakaki cite Zhang 2022 instead); "Conflict … remains open" → conflict id has no entry in `research/source_conflicts.yaml` | lead note; false statement corrected |
| SOURCE_AEROGEL_MU_EMISSION_EFFICIENCY_SAKAKI2026 | notes | the 1.3 % includes the 52 % whose origin is Bakule 2013 | lead note |

## 5. Records added (16, all `analogous`, confidence high, P0, quoted verbatim from the page images)

The extraction summary listed "injection-efficiency number", "storage time", "kicker and weak-focus field
strengths", "muons per pulse" and "detector geometry" as undeterminable; the paper gives most of them.

| id | value | page | quotation (abridged) |
|---|---|---|---|
| MACHINE_INJECTION_EFFICIENCY_GAIN_ABE2019 | ≥ 10 (interval, lower bound) | 4 | "will improve injection efficiency by more than an order of magnitude" |
| MACHINE_STORAGE_REGION_RADIAL_HALF_WIDTH_ABE2019 | 15 mm | 15, Table 3 | "Main field — Location: r = 333 ± 15 mm, z = ±50 mm" |
| MACHINE_STORAGE_REGION_HALF_HEIGHT_ABE2019 | 50 mm | 15, Table 3 | same cell |
| MACHINE_STORAGE_FIELD_LOCAL_UNIFORMITY_TABLE3_ABE2019 | < 1e-6 (bound) | 15, Table 3 | "Local uniformity < 1,000 ppb" |
| MACHINE_INJECTION_REGION_Z_MIN_ABE2019 / _Z_MAX_ABE2019 | 0.4 m / 1.1 m | 15, Table 3 | "Injection field — Location: 0.4 < z < 1.1 m" |
| MACHINE_KICKER_REGION_Z_HALF_EXTENT_ABE2019 | 0.4 m | 15, Table 3 | "Kicker field — Location: \|z\| < 0.4 m" |
| MACHINE_FIELD_INDEX_TABLE3_ABE2019 | 1.5e-4 (interval 1.0e-4–2.0e-4) | 15, Table 3 | "n-index ∼ (1.5 ± 0.5) × 10^−4" |
| MACHINE_MUON_DILATED_LIFETIME_ABE2019 | 6.6 µs | 16 | "…with a dilated lifetime of 6.6 µs" |
| MACHINE_MUONS_PER_FILL_ABE2019 | 1e4 (order of magnitude) | 17 | "The number of muons per fill is about 10^4." (Table 5 check: 5.2e12/(2.2e7 s × 25 Hz) = 9.5e3) |
| MACHINE_MEASUREMENT_INTERVAL_PER_FILL_ABE2019 | 33 µs | 17 | "…an interval following the fill of 33 µs, which is five times larger than the time-dilated muon lifetime" |
| DET_G2_RADIAL_COVERAGE_MIN/MAX_ABE2019, DET_G2_HEIGHT_COVERAGE_HALF_ABE2019 | 90 mm / 290 mm / 200 mm | 17 | "Geometrical coverage of the detector is 90–290 mm in radial direction and within ±200 mm in height." |
| DET_G2_VANES_ABE2019 / DET_G2_SENSORS_PER_VANE_ABE2019 | 40 / 16 | 17 | "The detector consists of 40 radial modules called vanes. Each vane consists of 16 sensors, …" |

## 6. Scenario file (`scenarios_batch7_source.yaml`)

* JPARC-G2-EDM-DESIGN-2019: 16 roles added for the new records; `unknown_roles` no longer lists
  `injection_efficiency_value` (Table 4: 0.85; p. 4: > 10×), `storage_time` (p. 17: 33 µs measurement interval),
  `storage_region_size` and `weak_focus_field_strength` (Table 3), `detector_radius` and `detector_layer_count`
  (p. 17); description wording "detected e+ per surface muon" → "per initial muon at production" (p. 20);
  notes: 0.52 origin and conflict-id status corrected. `muons_per_bunch_stored`, `muons_per_pulse_at_linac_exit`
  and `kicker_field_strength` stay unknown (not stated). Status `reported` kept (as the sibling batch-7 scenarios).
* MUTRISTAN-HYBRID-TARGET-2026: role `hadronic_model` pointed at the HARP Be benchmark-target record; renamed
  `harp_benchmark_target` (the model, JAM, is in the `simulation_code` record).

## 7. Removals

None. Every record is supported by its page.

## 8. Residual doubts (for the lead)

1. **CONF_MUONIUM_FORMATION_FRACTION does not exist in `research/source_conflicts.yaml`**, although
   `research/source_registry.yaml` and several parameter files (Zhang deck, Aritome/Beare, μTRISTAN 2022, and
   formerly these files) call it "open". It should be entered: 0.52 ± 0.01 (Bakule 2013, MuSR; used by Abe 2019,
   μTRISTAN, Zhang, Sakaki 2026) vs 0.655 ± 0.018 (Beare 2020, laser-ablated aerogel).
2. H-line intensity: text "∼ 10^8 per second" (p. 7) vs 3.0e8 s⁻¹ implied by Table 5 and the post-H-line Table 4
   factors (2.8e8 if Table 5 counts before the kicker decay). Kept as an internal-consistency observation of the
   design paper (the "∼" is an order-of-magnitude statement), not a conflict.
3. Source-internal duplicates kept separately: IH transmission 100 % (Table 2) vs 0.99 (Table 4); IH length 1.4 m
   (Fig. 5) vs 1.29 m cells (text); DAW 16 m (Fig. 5) vs 16.3 m (text); local uniformity "1 ppm" (p. 3) vs
   "< 1,000 ppb" (Table 3); field index "n ∼ 10^−4" (p. 5) vs "(1.5 ± 0.5) × 10^−4" (Table 3).
4. The 73 % ionisation efficiency is a calculation; its P1 rests on a cross-document consistency test
   (`test_abe2019_vs_zhang_g2_target_chain_consistency`) that is not an independent reproduction, and the Zhang
   deck may itself derive from Abe's numbers.
5. Minor paper-internal inconsistency not recorded as a value: p. 17 says the positron rate changes "by a factor
   of 160" over the 33 µs interval, whereas e^(33/6.6) = 148.
6. Unpinned audit arithmetic (γ, R, T_c, γτ, Table 6 quadratic sums, N_p, L_y, muons per fill) stays at P0; the
   lead may pin it in `tests/scientific/test_batch7_documents.py` if P1 is wanted.
7. Not extracted (outside the G9 brief, which scoped pp. 1–11 and 19–21 plus §6): the remaining positron-detector
   and DAQ specifications of pp. 17–18 (sensor 97.28 × 97.28 mm², 0.32 mm thick, 2 × 512 strips at 190 µm, 655k
   strips, 5 ns time stamp, 360 MB/s, ENC < 1600 e−, peaking time < 50 ns, 10 µrad alignment, clock stability
   1e-11), the NMR probe size (5–10 mm) and positioning (< 0.1 mm), the 309 MeV/c positron end point, and the EDM
   alignment numbers of p. 22 (3.6 µrad → 0.36e-21 e·cm).
8. Sakaki 2026: η_conv, extraction efficiency, extracted rate and initial emittance remain null (explicitly not
   quantified); the Fig. 2, Fig. 4 and Fig. 5 curves are not transcribed (only the text values ≈ 10 %, ≈ 0.001 and
   the Table I 6e-4); the pairing of the Fig. 6 times (0.3/0.5/0.65/0.8 µs) with the 5/10/15/20 mm gaps is
   inferred from Fig. 5 (peaks at those times), not stated.
9. `registries/*.csv` are out of sync until the lead runs `tools/build_registries.py`.
