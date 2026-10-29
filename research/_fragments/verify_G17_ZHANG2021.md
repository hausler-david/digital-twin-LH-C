# Verification note: group G17_ZHANG2021 (batch 10, 2026-10-29)

Source: SRC_DOI_10_7566_JPSCP_33_011125. Ce Zhang et al. (24 authors), "Simulation Study of Laser Ionization of Muonium by
1S-2S Excitation for the Muon g − 2/EDM Experiment at J-PARC", JPS Conf. Proc. 33, 011125 (2021), Proc. 3rd J-PARC Symposium
(J-PARC2019), received 10 January 2020, 6 pp. Category CONFERENCE_PROCEEDING (a simulation study). It is not a PRIMARY_LHMUC
source, so no record may be `reported_lhmuc`, and none is.

Files verified:

- `parameters/source/muonium_laser_ionisation_sim_zhang2021.yaml`
  - 104 records at hand-over and 104 after verification: 0 added, 0 removed.
  - 27 records corrected or annotated (list below). Every `parameter_id`, value, unit, scenario, status, quotation and
    validation level is unchanged. One confidence label was lowered (correction 1).
  - Header comments: reworded in three places, and two lines added (corrections 4, 13).
- `parameters/machine/scenarios_batch10_zhang.yaml`
  - Scenario `JPARC-S2-MU-IONISATION-DEMO-ZHANG2021`: description and notes corrected (corrections 2, 4, 10, 12).
  - Roles, unknown_roles, status, machine, G0 and P0 are unchanged. A header line points to this note.

Role: adversarial verifier. For every record I checked value, unit, page, section, table/figure/equation label, quotation,
uncertainty, provenance status and applicability, scenario, derivation, dependencies, confidence, validation label and notes.

## Method

1. **Page images.** All six pages were read as page images.
   - Fig. 1 (p. 2): the picture labels and the kinematic inset, from 600 dpi crops.
   - Fig. 2 (p. 3), Fig. 5 (p. 5) and Fig. 6 (p. 5): from the native embedded images (`pdfimages`). The Fig. 5 statistics
     boxes are raster text at 279 ppi; higher render resolutions add nothing.
   - Fig. 3 labels and the Fig. 4 histogram (p. 4): 600 dpi crops.
   - Table I (p. 6): read cell by cell.
   - Crops leave out the page top. The per-download line printed at the top of every page was not transcribed into any
     file. A token search of both YAML files and of this note finds no part of it.
2. **Quotations.**
   - Every quotation was split at the extractor's markers (`[p. N]`, `[...]`, `|`, `||`, bracketed figure tags). Each
     segment was searched in the normalised text layer (`…/scratchpad/text/jpscp.33.011125_pNN.txt`, page-top line excluded;
     ligatures, `^` and line-break hyphens normalised).
   - Every text segment was found, and every one lies on a page listed in its record's `page` field.
   - 121 segments do not match the text layer. All are figure-label transcriptions: the Fig. 1 picture and inset, the Fig. 2
     labels, the Fig. 3 labels, the Fig. 5 statistics boxes and the Fig. 6 labels. One more is 'GEANT-4' (p. 5), printed
     with a hyphen at a line break. All were confirmed on the images.
   - 'GEANT-4' is most likely a typed hyphen, since LaTeX does not hyphenate 'GEANT4'. The extractor's reading is kept.
3. **Values and units.**
   - Every value was compared with its quotation and with my own reading of the page image: 0 mismatches.
   - Checked: all 14 cells of Table I; the Fig. 1 inset (3.4 MeV, 27 MeV/c, 0.05; 25 meV, 2.3 keV/c, 0.4; 212 MeV, 300 MeV/c,
     4x10^-4); the picture labels (333 uA, 28 MeV/c, 300 K ~ 25 meV); and the Fig. 3 labels (80×80 mm², 100 µm; 45×35 mm²,
     435 µm; 45×35 mm², 8.8 mm).
   - Fig. 5 boxes: 'Y vs. X' gives −1.878 / 0.3673 / 19.53 / 12.65; 'Y vs. Z' gives 0.03006 / 0.3673 / 0.03288 / 12.65.
   - Fig. 6: '~3 m', 'target & SOA lens', EQ1, 2, ED, EQ3, 4, BM and MCP.
   - Every unit parses with `lhmuc.units.parse_unit`, including ppm, meV, keV/c, microampere, megawatt and
     milligram/centimeter**3.
4. **Arithmetic re-done.** All agree with the file except where a correction is listed.
   - Fig. 1 kinematics with m_μ = 105.658 MeV: T(27 MeV/c) = 3.395 MeV, T(28 MeV/c) = 3.647 MeV, T(300 MeV/c) = 212.40 MeV,
     p(25 meV) = 2.298 keV/c.
   - k_B T = 25.85 meV at 300 K and 27.7 meV at 322 K. 3 GeV × 333 µA = 0.999 MW.
   - FWHM/2.3548: 19.96, 12.74, 32.70 and 12.32 mm.
   - S2 rate over S1 rate: 1.263 and 12.63. 2.4e6/0.00717 = 3.35e8.
   - Table I running product: 1.1208e6, 5.828e5, 4.779e4, 0.018638, 0.012134 and 0.010920 against the printed values:
     +1.9 %, +0.5 %, −0.4 %, +0.2 %, +0.3 % and +0.2 %. That is 4.550e-9 per S2 surface muon, against 0.0109/2.4e6 =
     4.542e-9.
   - 8.8e-7 × 0.44 = 3.872e-7. The laser ratios are 2.56, 17.9, 153.8 and 1.87e6.
   - 0.467/0.443 = 1.054. 1.5e3/2.0e3 = 0.75. 0.87 × 0.85 × 0.90 = 0.66555. 0.651 × 0.90 = 0.5859.
   - Binomial σ on 2.0e3 trials: 1.10 % at 0.586 and 0.97 % at 0.75.
5. **Cross-references.**
   - All 49 external parameter ids (45 at hand-over, 4 added by correction 1), 5 source ids and 2 conflict ids named in the
     two files resolve (`lhmuc.registry.load_all`). The tokens that do not resolve are symbols or enum names, not ids: E_244,
     E_355, N_MCP, P_1S2S, R_MCP, T_ED, V_ED, V_SOA, M_MU_GEV, JPARC_MUSE, CONFERENCE_PROCEEDING and G17_ZHANG2021.
   - Every number the notes quote from another record was checked against that record:
     - Abe et al. 2019: text layer pp. 2, 4, 6–9, and the Fig. 3 image on p. 8, whose inset is identical to the Zhang
       Fig. 1 inset;
     - Aritome et al. 2024 (9.5e4/pulse, 940 kW, 25 Hz, 420 µm, 38 %, 5.7 keV, 42 mm, 60 %, 19 %, 0.5–1.3 mJ, 7e-6–6e-5,
       2.1e-8);
     - the Kraków Zhang deck: text pp. 6–8, 10, 12, including "at the J-PARC MLF S2 area 2022" and "Inside single-layer
       aerogel";
     - Bakule 2013, Beare 2020 and Beer 2014 records;
     - `CONF_MUONIUM_FORMATION_FRACTION` and `CONF_LASER_IONISATION_EFFICIENCY`, both `resolved_as_scenarios`;
       treatment (c) of the latter is quoted correctly.
   - One cross-reference was false (correction 1).
6. **Statuses, confidence and labels.**
   - Status: 98 `analogous`, 3 `analytical_estimate` and 3 `unknown` (value null, confidence none). No reported_lhmuc and
     no high.
   - The three analytical estimates have derivations that name their input ids, and all three were recomputed.
   - P1 is claimed for 11 records. Each names an existing test in `tests/scientific/test_batch10_documents.py`:
     - `test_zhang2021_table1_rates_follow_from_efficiencies`;
     - `test_zhang2021_laser_ionisation_factorises`;
     - `test_zhang2021_internal_inconsistencies_recorded`;
     - `test_zhang2021_244nm_demonstrator_vs_122nm_design_ionisation`, named only as a comparison.

     All four tests pass.
7. **Scenario.**
   - All 90 roles resolve, and each was checked against its record by name, value and unit.
   - The 16 unknown_roles are genuine gaps. Three of them also have explicit-unknown records, which follows the
     `LHMUC-SOURCE-HYBRID-IMCC` convention.
   - Six role records keep `scenario: null` by design: facility values, the S1 measurement and the TRIUMF fit sample. 44
     of the 49 registry scenarios do the same.
   - `tools/apply_scenario_levels.py --check` reports 0 excess labels.
8. **Validation runs (after the corrections).**
   - `uv run python tools/validate_yaml.py provenance …zhang2021.yaml` and `… machine …scenarios_batch10_zhang.yaml`: 0
     schema errors each.
   - `uv run python -m lhmuc validate`: 0 errors, 0 warnings.
   - `uv run pytest`: 191 passed, 2 failed. The failures are the generated-registry sync checks (residual doubt 12).

## Extractor deviations from the task: both upheld

- **`SOURCE_S2_SURFACE_MU_RATE_SECTION2_ZHANG2021` stays P0.**
  - `test_zhang2021_internal_inconsistencies_recorded` only asserts 2.4e6/2.4e5 = 10. That shows the value inconsistent
    with Table I; it neither reproduces it nor shows it consistent.
  - docs/validation_plan.md §1 rule 1 and the P1 entry criterion therefore give P0. The test stays named in methods and
    check_ids.
  - The same reasoning keeps 0.443 at P0.
- **Scenario `validation_level` stays P0.** Rule 3 makes a composite's level the minimum over its inputs, and most role
  records are P0. The Kaya verifier (G15) kept the same choice.

## Checked and found correct (no change)

- **§1 (p. 1):** 0.1 ppm (value; see correction 1 for the attribution), 28 MeV/c, 3 GeV, 25 meV, 244 nm, 355 nm and
  Lyman-α 122 nm.
- **§2 (pp. 2–3):**
  - four experimental areas; 500 kW now and 1 MW expected; double pulsed; three bending magnets;
  - S1 1.9 × 10^5/s per pulse at 500 kW, ref. [5];
  - G4Beamline with relative S1 rates; last three triplets;
  - 47 × 30 mm; 2 mm spot; 2.4 × 10^5/s per pulse; 77 × 29 mm.
- **§3 (pp. 3–4):** 100 µm Kapton; 78 × 78 × 6 mm; 2 mm; 435 µm; 44.3 %; about 350 ns; 52 %; 100 %; T = 322 K;
  D = 870 cm²s⁻¹; 23.2 mg/cm³; 8.8 mm; 0.082; 3 mm; 2 × 40 × 2 mm³; near 0.8 µs; 0.6 µs apart; 8.8×10⁻⁷; about 44 %;
  about 3.9×10⁻⁷.
- **§4 (pp. 5–6):** two mesh and three cylindrical electrodes; 20 kV; 5 kV / 20 keV; ϕ42 mm; 2.0 × 10³ and 1.5 × 10³;
  (58.6 ± 0.9) %, with the ± stored as `gaussian_sigma` 0.009; 13 %, 85 % and 90 %.
- **§5 and Table I (p. 6):** 2.4×10⁶ per pulse at 500 kW; about 0.011/s; and all 14 cells.
- **Explicit unknowns are justified.** No laser pulse energy, duration, linewidth or repetition rate, and no ablation state,
  is printed anywhere in the paper.
- **The registry entry's five unresolved_questions** are all represented by separate records and notes: S2 intensity,
  stopping efficiency, the extraction numbers, the [8] attributions, and ablation and laser energies.
- **No clearly quantitative statement is missing.**
  - Not recorded, correctly: the scale bars of Figs. 2 and 6, which are drawing scales, and the Fig. 4 and Fig. 5
    histograms, which are not digitised.
  - Fig. 2 has no SQ13-15 label, as the extractor says.

## Corrections (all ids kept)

1. **A false attribution was refuted: `PHYS_JPARC_G2_EDM_PRECISION_GOAL_ZHANG2021`.**
   - The notes said the 0.1 ppm "Restates the J-PARC g−2/EDM goal of ref. [1]". Ref. [1] is Abe et al. 2019
     (SRC_ARXIV_1901_03047). It prints 450 ppb (statistical) and < 70 ppb (systematic) for a_μ and 1.5 × 10⁻²¹ e·cm for the
     EDM: Table 1 p. 4, abstract p. 2, and records `PHYS_AMU_PRECISION_STAT_TABLE1_ABE2019` etc. It does not print 0.1 ppm.
   - 0.1 ppm equals the "final statistical sensitivity of 0.1 ppm on g−2" of Beer et al. 2014 p. 6
     (`PHYS_JPARC_G2_DESIGN_STAT_SENSITIVITY_BEER2014`).
   - The notes and `applicability.explanation` now say this. Confidence is lowered from medium to low: the paper attaches
     the 0.1 ppm to both moments, and its cited reference gives different goals.
   - The value is unchanged: it is what the paper prints.
2. **Origin of the 0.52 marked as inferred: `SOURCE_MUONIUM_FORMATION_FRACTION_ZHANG2021` and the scenario notes.**
   - Both said the 0.52 "originates in" or "is" Bakule et al. 2013. Bakule 2013 is not among Zhang's references [1]–[13];
     the paper cites Beer 2014 [8].
   - The wording is now "matches … — origin inferred, not cited". That matches `CONF_MUONIUM_FORMATION_FRACTION`, which lists
     the Zhang-family attributions as inferred, and the G16 verifier's correction of
     `SOURCE_MUONIUM_FORMATION_FRACTION_BEER2014`.
3. **A non-discriminating argument was replaced: `SOURCE_SURFACE_MU_STOPPING_EFF_TEXT_ZHANG2021`, notes.**
   - The notes argued that the chain uses 0.467 because 2.4e6 × 0.467 = 1.12e6 ≈ 1.1e6. But 2.4e6 × 0.443 = 1.06e6 also
     prints as 1.1×10⁶, so this does not tell the two apart.
   - The next row does: × 0.52 gives 5.83e5 with 0.467, printed 5.8×10⁵, against 5.53e5 with 0.443.
4. **Beam FWHM 47 × 30 mm vs 77 × 29 mm, in four records** (`SOURCE_S2_BEAM_FWHM_{X,Y}_{OPTIMISED,GAUSSIAN}_ZHANG2021`), the
   header and the scenario notes.
   - (a) The notes called the pair an "internal inconsistency" and placed the 77 × 29 mm sentence "two sentences after the
     S2 intensity estimate". It is the sentence right after it.
   - The paragraph also says the profile "was tuned specifically to be shrunk vertically and extended in horizontal
     direction". 77 × 29 mm is wider horizontally and narrower vertically than 47 × 30 mm, so a two-stage reading makes the
     two statements consistent.
   - The notes now say the relation is not stated: consistent as two tuning stages, conflicting as one beam.
   - (b) The validation notes claimed that the Fig. 5 σ (19.53 × 12.65 mm) is "closer to the 47 × 30 mm profile". That is
     not supportable. The muonium is emitted from the target surface, so its distribution is bounded by the target's
     transverse size.
   - Verifier arithmetic, not stored in the registry: a 77 mm-FWHM Gaussian truncated at ±39 mm (78 mm target) has σ = 20.4
     mm, and a 47 mm one 17.4 mm. So with truncation the 77 mm reading is the closer one in x. The box values cannot rank the
     two statements, and the notes now say so.
5. **The same caveat for the Fig. 5 widths: `SOURCE_MU_SURFACE_YIELD_STDDEV_X_FIG5_ZHANG2021`, `…_STDDEV_Y_…`.**
6. **A "no beam size" statement was made precise: `SOURCE_LASER_PULSE_ENERGY_244NM_ZHANG2021` and
   `SOURCE_LASER_EXCITATION_SIM_METHOD_ZHANG2021`, notes.**
   - The notes said no laser beam size is printed. p. 3 prints a 2 mm "spot size" for "the laser", without saying which
     wavelength (`SOURCE_LASER_SPOT_SIZE_ZHANG2021`).
   - The notes now point to it.
7. **'Preliminary' label added: `SOURCE_LASER_1S2S_EXCITATION_PROB_ZHANG2021`, `SOURCE_LASER_2S_IONISATION_PROB_ZHANG2021`.**
   - The paper labels this simulation "preliminary" (p. 4). research/source_quality_policy.md §4 asks that such a label be
     carried in `applicability.explanation`. The 3.9e-7 record already had it; it is now added to these two.
8. **Figure/table label: `SOURCE_THERMAL_MU_RATE_MCP_ZHANG2021`.**
   - `table_figure_or_equation` named "§5 text", but the quotation is the Table I row only. The §5 "about 0.011/s" is its
     own record. "§5 text" was removed.
9. **Method text: `SOURCE_LASER_IONISATION_EFF_244NM_ZHANG2021`, `validation.methods[2]`.**
   - It said "4.8e4 × 3.9e-7 → 0.0186 within the printed digits". In fact 4.8e4 × 3.9e-7 = 0.01872, which prints as 0.0187.
   - The test multiplies the running product 4.78e4 s⁻¹, giving 0.01864, which matches 0.0186. The text now says this, with
     the 3 % tolerance. P1 is unchanged.
10. **Extraction numbers: a candidate reading added (P0, verifier arithmetic, not a registered test).**
    - 0.75 × 0.87 × 0.90 = 0.587 and 0.75 × 0.87 = 0.6525 reproduce the stated (58.6 ± 0.9) % and Table I's 0.651 within the
      rounding of the two-figure counts.
    - That fits the reading that the 85 % mesh transmission is already inside the simulated 1.5e3/2.0e3 count, and that the
      13 % decay loss and the 90 % MCP aperture ratio were applied to it. The paper does not say so.
    - The reading is written into the validation notes of `SOURCE_THERMAL_MU_EXTRACTION_TRANSMISSION_ZHANG2021`. A pointer
      was appended to the shared sentence "The paper does not explain how 0.75, 0.586 and 0.666 relate" in 7 records
      (`…_TRANSMISSION_`, `…_DECAY_LOSS_`, `SOURCE_SOA_MESH_TRANSMISSION_EFF_`, `SOURCE_MCP_APERTURE_RATIO_`,
      `SOURCE_SLOW_BEAMLINE_TRANSMISSION_`, `…_COUNT_RATIO_`, `…_NAMED_FACTORS_PRODUCT_ZHANG2021`), and to the scenario notes.
    - Nothing is resolved: all records and P-labels stay as they were.
11. **Axis label: five aerogel-target records** (`SOURCE_AEROGEL_TARGET_*_ZHANG2021`). The notes now give the Fig. 4 axis
    label exactly as printed, 'Z[mm]'.
12. **Scenario description: S1 validation wording.**
    - It said the G4Beamline model was "validated on the measured S1 intensity". The paper (p. 2) validates it "by
      reproducing the relative surface muon rate at S1 at different conditions (with or without slits)". The S2 estimate
      rests on "the comparison with the measurement at S1".
    - The description now says both.
13. **Headers.**
    - Parameter file:
      - the [8] wording ("where matching numbers are found (inferred, not cited)");
      - the FWHM wording;
      - the confidence line (the 0.1 ppm exception);
      - two lines pointing to this note.
    - Scenario file: one line pointing to this note.

The edits were made at data level by a script, `…/scratchpad/verify_g17/apply_g17_fixes.py` and `apply_g17_fixes2.py`. The
script re-dumps with the extractor's settings, which round-trip both files byte-identically. The header edits were made by
hand. A per-field log is kept in `…/scratchpad/verify_g17/fix_log_g17.json`.

## Removed

Nothing. Every record is backed by a verbatim quotation, an exact cell transcription, or a printed figure label on the cited
page. The three unknown records document parameters the paper does not give.

## Residual doubts (for the lead)

1. **S2 intensity: 2.4 × 10⁵/s per pulse (§2) vs 2.4×10⁶ per pulse (§5) and 2.4×10⁶ in Table I's "Event rate (/s)".**
   - It is not known which is the misprint, what "/s per pulse" means, or whether one or both bunches are counted.
   - For context only, not a resolution: Aritome et al. 2024's 9.5e4 μ⁺/pulse × 25 Hz = 2.4e6 s⁻¹. That is numerically equal
     to the Table I start rate, but at 940 kW, not 500 kW.
2. **Stopping efficiency: 0.443 (§3, 435 µm degrader) vs 0.467 (Table I, used).** Unexplained.
3. **Target geometry: 78 × 78 × 6 mm (text) vs 45×35 mm², 8.8 mm (Fig. 3).** The visual hints disagree:
   - the Fig. 4 stopping histogram reaches about −9 mm in depth;
   - the Fig. 5 muonium map reaches about ±40 mm transversely.
   - Verifier arithmetic, not in the registry: a 45 × 35 mm target would truncate the Fig. 5 widths to about 12 × 9 mm,
     well below the printed 19.53 × 12.65 mm. So the simulation behind Fig. 5 apparently did not use 45 × 35 mm. This is an
     inference.
4. **Extraction numbers.**
   - Correction 10 is a candidate reading only.
   - The origin of the ± 0.9 % is unknown. A binomial σ gives 1.1 % on 0.586, and 0.76 % after scaling the σ of 0.75 by
     0.87 × 0.90.
5. **0.1 ppm goal (correction 1).** The paper's "[1]" attribution is inaccurate. The record is kept as printed at
   confidence low.
6. **Surface-muon momentum: 28 MeV/c (§1 and the Fig. 1 picture) vs 27 MeV/c (Fig. 1 inset, as in Abe 2019).** The inset's
   3.4 MeV corresponds to 27 MeV/c.
7. **Unidentified sources.**
   - What the S-line transport efficiency 0.00717 is normalised to: the implied 3.35e8 s⁻¹ upstream has no stated meaning.
   - The primary publication of the T = 322 K / D = 870 cm² s⁻¹ fit.
   - The primary source of the 0.52 for the 23.2 mg/cm³ sample.
8. **Laser parameters behind 3.9e-7 (energies, durations, linewidth, which laser has the 2 mm spot).** Not printed;
   ref. [9] is a private communication.
9. **Readings of the drawings, flagged as such in the notes.**
   - Which three triplets are "the last three". On the drawing they are SQ10-12, SQ16-18 and SQ19-21. SQ10-12 lies upstream
     of the SB3 split, so re-tuning it would also change S1.
   - What length the "~3 m" mark of Fig. 6 means.
10. **No conflict records yet.**
    - None of the internal inconsistencies has an entry in research/source_conflicts.yaml. If the lead writes entries for
      the S2 intensity, stopping efficiency, target geometry and extraction numbers, policy §4 drops the competitors to
      confidence low until a treatment is decided.
    - `CONF_LASER_IONISATION_EFFICIENCY.affected_parameters` does not yet list `SOURCE_LASER_IONISATION_EFF_244NM_ZHANG2021`,
      although the record cites the conflict.
    - `CONF_MUONIUM_FORMATION_FRACTION` does not list `SOURCE_MUONIUM_FORMATION_FRACTION_ZHANG2021`.
11. **Source-registry wording** (research/source_registry.yaml, not edited).
    - The relevance text says "G4Beamline S-line model validated on S1 (1.9e5, 500 kW)". The same precision fix as
      correction 12 would apply.
    - "0.52 ± 0.01 is Bakule et al. 2013 p. 3" would read better as "matches", as in correction 2.
    - The `registries/missing_evidence.csv` ME_031 verifier note says the same ("although the value is Bakule 2013").
12. **Generated files.**
    - `test_csv_registries_in_sync` and `test_source_parameters_extracted_in_sync` fail with OUT OF SYNC for
      SRC_ARXIV_1905_05564, SRC_ARXIV_1407_8248 and SRC_DOI_10_7566_JPSCP_33_011125 until the lead runs
      `tools/build_registries.py` and `tools/sync_parameters_extracted.py`.
13. **Other groups' scenario levels (not this group's files, not edited).** `tools/apply_scenario_levels.py --check` reports
    three scenarios at P1 above their P0 cap:
    - `JPARC-MUSE-S2-2024` (scenarios_addendum_source.yaml);
    - `JPARC-G2-EDM-DESIGN-2019` and `MUTRISTAN-HYBRID-TARGET-2026` (scenarios_batch7_source.yaml).
