# Verification note: group G7B_MR7_SOURCE (G7 IMCC reference tables, 2026-10-29)

Source: SRC_ARXIV_2510_27437, MuCol Milestone Report No. 7 "Consolidated Parameters" (arXiv:2510.27437v1, 93 pp,
category OFFICIAL_CERN, access uploaded). All page numbers below are PDF pages; the printed page number is PDF − 11
(PDF p. 15 = printed p. 4, PDF p. 58 = printed p. 47). Secondary cross-reference: SRC_WS1681458_SCHULTE_IMCC
(D. Schulte, Kraków 2026 deck), slide 12, cited in record notes only.

File verified (the only file edited): `parameters/source/imcc_mr7_proton_driver_target_cooling.yaml`

- 418 records at hand-over, 418 after verification: 0 added, 0 removed, 0 renamed. Every `parameter_id` is kept.
  The scenario file `parameters/machine/scenarios_addendum_imcc.yaml` (not mine, not edited) points to five of them
  (`SOURCE_PD_LINAC_BEAM_POWER_5GEV_MR7`, `SOURCE_TARGET_MATERIAL_BASELINE_MR7`, `SOURCE_FE_OUTGOING_MUMINUS_YIELD_MR7`,
  `SOURCE_COOLING_FINAL_FROM_B8_OUT_EPS_T_MR7`, `SOURCE_COOLING_FINAL_FROM_B8_OUT_EPS_L_MR7`); none of them changed value.
- No numeric value changed. 2 categorical value strings were reworded for accuracy, 1 unit changed, 10 confidence
  labels were lowered from `medium` to `low`, 4 `section` strings and 4 quotations were made more precise, and 26
  record notes and 80 `validation.notes` were added or corrected. All 418 applicability explanations were updated.
- Status: all 418 `analogous` (no `reported_lhmuc`, `imported_related` or `derived_lhmuc`; no extractor-computed value
  needed `analytical_estimate`: the ×10^14 and ×10^-2 factors are unit conversions of printed cells).
- Confidence: 408 `medium`, 10 `low`, none `high`.
- Validation: all 418 `P0`. None could be raised to P1 (see "P1 decision").

Role: adversarial verifier. For every record I checked value, unit, page, section, table/figure label, quotation,
uncertainty, allowed_range, status, applicability, confidence, derivation, validation methods and notes.

## Method

1. **Page images.** Every cited page was read as a rendered page image: PDF pp. 13, 15, 16, 17, 41, 42, 43, 44, 45, 46,
   47, 48, 51, 54, 55, 56, 57 and 58. For the cross-checks I also read pp. 14 (Tables 1.2 and 1.3), 37 (Table A.1) and 40
   (Table A.2), and Schulte slide 12.
2. **Cells.** I typed an independent transcription of every table cell in scope from the images:
   - Tables 2.1, 2.2, B.1, B.2, 3.1, 3.2, C.1–C.8, 4.1 and D.5;
   - the Start and output rows of D.13 and D.17;
   - Table D.21 and every text value.
   I compared it with the YAML values (script `…/scratchpad/verify_g7b/cellcheck.py`): 409 values compared, 0 mismatches.
   The 9 remaining records are categorical strings. I checked them by eye against their quotations.
3. **Quotations.** Every text quotation was normalised and searched in the page text layer (`qcheck.py`), and all were
   found. Three needed the image instead:
   - 'pion-production' (p. 41): the text layer joins the line-break hyphen.
   - The B.4 quotation: it runs from p. 43 onto p. 44, and the section already says 'printed pp. 32-33'.
   - The Fig. D.1 caption 'Bz field-on-axis' (p. 55): the hyphen falls at a line break.

   Every cell transcription ('Row …, column …: x') matches the image. Every table caption in
   `table_figure_or_equation` matches the printed caption.
4. **Arithmetic.** I recomputed every check named in `validation.methods` or `validation.notes` with PDG constants
   (m_μ = 105.6583755 MeV, m_p = 938.27208816 MeV, c = 299 792 458 m/s, e = 1.602176634e-19 C). The script is
   `…/scratchpad/verify_g7b/recompute.py`, and the results are in the table below.
5. **Diff discipline.** All edits were made by a block-level script (`apply_edits.py`) plus two small follow-ups. Each
   result was checked by parsing the file before and after and diffing every field (`diffrec.py`). Only the fields
   listed in this note changed.

## P1 decision

The lead pinned eight tests in `tests/scientific/test_imcc_mr7_reference.py`. All of them check collider-level
quantities:

- the Table A.1 muon beam power 2 N E f_r (14.4 / 5.3 MW);
- the IP beam size;
- the luminosity lifetime;
- the hourglass factor 0.76;
- F_decay from eq. (A.7);
- eq. (A.9) L = 18.8e34;
- L_int = 2.2 ab^-1;
- the one-beam decay factor.

None of them checks a value in this file. `test_mr7_beam_power_is_two_n_e_fr` is the near miss, but it checks the
muon beam power, not the proton-driver power N E f. Every record therefore stays P0. Each `validation.notes` now states
the result of the recomputation and that no test pins it. I invented no test names.

## Corrections (by record)

### Confidence lowered to `low` (10 records): internal contradictions of MR7 and an unprinted number

1. `SOURCE_TARGET_MUON_WINDOW_MATERIAL_MR7` ('Titanium Grade 5'). Table C.1 (p. 45) and the text on the same page, 'it
   is required to use beryllium in proton and muon windows', contradict each other. MR7 does not resolve it. The
   proton window, which is Beryllium in both places, stays medium.
2. `SOURCE_COOLING_SHORTRECT_RECT_END_TRANSMISSION_MR7` (Table 4.1, 14.9 %). This is the Table D.5 B-Stage 8
   cumulative without the 95 % charge-separation factor, so it should be 14.2 %. The long half applies the factor:
   0.95 × 11.1 = 10.5, and Table 1.3 does the same. Kept as printed.
3. `SOURCE_COOLING_SHORTRECT_FINAL_COOLING_END_TRANSMISSION_MR7` (6.4 %). It equals 14.9 × 0.427 and so inherits the
   omission in item 2. With the factor it would be 6.0 %. The extractor had not noticed this; it is a new finding.
4. `SOURCE_COOLING_SHORTRECT_REACCEL_END_TRANSMISSION_MR7` and 5. `SOURCE_COOLING_LONGRECT_REACCEL_END_TRANSMISSION_MR7`
   (5.8 %). The value is not 6.4 % × 86 % (Table D.21), which gives 5.5 %. Table 1.3 (p. 14) uses the same 86 % and
   prints 5.6 %. The Table 1.3 cross-reference is new.
6. `SOURCE_COOLING_LONGRECT_FINAL_COOLING_END_EPS_T_MR7` and 7. `SOURCE_COOLING_LONGRECT_REACCEL_END_EPS_T_MR7`
   (22.5 µm). Table D.17 (p. 57) ends at 0.023 mm, and the D.3.3 text says 'reduces the transverse emittance to 23 µm'.
   Both are above the 22.5 µm that Table 4.1 prints and above the 22.5 µm target. This is new. A matching note was added
   to `SOURCE_COOLING_FINAL_FROM_B10_OUT_EPS_T_MR7`, which stays medium because it agrees with the text.
8. `SOURCE_COOLING_FINAL_FROM_B8_PEAK_FIELD_MAX_MR7` (D.3.2, 'kept below 42 T'). Table D.14 (p. 56) lists −43.4 T for
   Stage 7. The extractor's note already recorded this, but the confidence had stayed medium.
9. `SOURCE_PD_ACCUMULATOR_TURNS_10GEV_MR7` (Table B.2, 4167). The value is identical to the 5 GeV column. The option's
   own inputs give 5.0 ms × c / 300 m = 4996.5 turns, 5000 with c = 3e8 m/s. The value 4167 equals 2.5 ms × 3e8 / 180 m,
   which are the 5 GeV inputs.
10. `SOURCE_TARGET_WINDOW_TITANIUM_PENALTY_MR7` (value 10). This factor is not printed. It encodes the verbal 'by an
    order of magnitude'.

### Factual corrections to notes, values, units and locations

11. `SOURCE_PD_ACCUMULATOR_TURNS_5GEV_MR7`, record note. The note claimed 'β = 0.9884 (5 GeV kinetic) … 4116 turns',
    which is wrong. A 5 GeV kinetic proton has γ = 6.329 and β = 0.98744, which gives 4111 turns. The printed 4167 is
    exactly 2.5 ms × 3e8 m/s / 180 m = 4166.7, using β = 1 and c rounded. Note rewritten.
12. `SOURCE_COOLING_RECT_B10_CUM_TRANSMISSION_MR7`, record note. The note claimed 'Table 1.3 Rectilinear B 28.6 % =
    11.1/38.7', but 11.1/38.7 = 28.68 %, which rounds to 28.7. The 28.6 % is the product of the ten printed B-stage
    transmissions, 28.63 %. Note corrected.
13. `SOURCE_TARGET_WINDOW_DPA_PER_YEAR_MR7`: unit changed from `dimensionless` to `'1/year'`, because the text says
    'yearly DPA around 0.5'. The unit parses through `lhmuc.units`.
14. `SOURCE_TARGET_SOLENOID_TECHNOLOGY_MR7`, value. The value said 'the MAP design used resistive magnets'. Reworded to
    'resistive magnets RC1–RC5 were considered in the MAP design', which is MR7's wording.
15. `SOURCE_PD_COMPRESSION_STATUS_MR7`, value. The emittance blow-up was seen in simulation, so the value now says
    'simulated RF compression of the 5 GeV beam shows …'.
16. `section` strings were made precise. `SOURCE_TARGET_MATERIAL_BASELINE_MR7` is on printed p. 4 (PDF 15). Three
    records are on printed p. 5 (PDF 16): `SOURCE_TARGET_YIELD_CAPTURE_MOMENTUM_MAX_MR7`,
    `SOURCE_TARGET_YIELD_STUDY_BEAM_SIGMA_MR7` and `SOURCE_TARGET_YIELD_STUDY_ROD_RADIUS_MR7`. All four previously said
    'pp. 4-5'.
17. `SOURCE_COOLING_FINAL_FROM_B8_OUT_{EPS_T,EPS_L,EPS_6D,CUM_TRANSMISSION}_MR7`, quotations. These records cite PDF p. 56
    for Table D.13, but the bracketed D.3.2 sentence they quote is on PDF p. 55 (printed p. 44). The bracket now says
    '[text, PDF p. 55 (printed p. 44): …]'.
18. Applicability explanations, all 418:
    - Proton driver (65 records): the caption of Table 2.1 was quoted with '1)' and '2)' dropped. It is now verbatim:
      'H- LINAC parameters for the baseline option considering 1) LINAC single use for muon production; 2) Chopping
      will later reduce the average current.'
    - Stage information, which the brief requires, was added to every group:
      - proton driver and target: Table A.1 lists the same 5 GeV and 5 × 10^14 protons on target per bunch for Stage 1
        (3 TeV) and Stage 2 (10 TeV);
      - front end, cooling and pre-accelerator: Table 1.2 shows one chain upstream of both colliders;
      - the 4 MW records belong to the Appendix C.2 alternative.
    - Front end: the explanation was a plain flow scalar. It is now quoted and ends 'not an LHμC value'.
19. Header comment. It said 'P1 marks values the generator recomputed', which was outdated. It now says that every
    record is P0, that the checks were recomputed, and that no test pins them. It now says the B.2 turns are
    'identical to' the 5 GeV value rather than 'copied from' it. The new contradictions are listed.

### Notes added (cross-checks and preserved inconsistencies, no value change)

20. `SOURCE_PD_COMPRESSOR_PROTONS_ON_TARGET_{5GEV,10GEV}_MR7`. The 5 × 10^14 is per pulse and is delivered as one bunch.
    Appendix B (p. 41) says the two compressor bunches are merged into 'a final single bunch'. Tables 1.1 and A.1 print
    it as 'Protons on target/bunch', and Schulte p. 12 as '5 x 10^14 protons/pulse'. N E f reproduces 2 MW and 4 MW
    only with this reading. This settles an apparent conflict between Table 2.2 (2 bunches), Table 3.1 (1 bunch per
    pulse) and Table 1.1 (per bunch). Matching notes were added to `SOURCE_PD_COMPRESSOR_BUNCHES_{5GEV,10GEV}_MR7` and
    `SOURCE_TARGET_BUNCHES_PER_PULSE_MR7`.
21. `SOURCE_COOLING_SHORTRECT_FINAL_COOLING_END_EPS_T_MR7`: Table D.13 ends at 0.0224 mm, and the text says 22.4 µm.
    This is consistent.
22. `SOURCE_COOLING_SHORTRECT_FINAL_COOLING_END_EPS_L_{MIN,MAX}_MR7`: the upper end of the range, 72, coincides with the
    71.72 mm of Table D.12 (final cooling from MAP initial conditions, p. 55). MR7 does not state where the range comes
    from.
23. `SOURCE_COOLING_SHORTRECT_REACCEL_END_EPS_L_MR7` (64 mm). The value equals the 64 mm target, but the cooling tables
    give 42.68 mm for this option, and MR7 shows no emittance growth for re-acceleration. The 64 mm cannot be derived
    from the tables.
24. `SOURCE_COOLING_FINAL_FROM_B8_START_EPS_6D_MR7` (0.12): Table D.5 B-Stage 8 prints 0.13 mm³.
25. `SOURCE_PREACC_LINAC_LENGTH_MR7`: added the page for Table A.2 (PDF p. 40, 245 m) and Table 1.2's 140 m.
26. `SOURCE_PREACC_INJECTION_ENERGY_MR7` (5 MeV). This agrees with Tables 1.2 and A.2, which give 0.005 GeV out of final
    cooling. The end-of-cooling mean p_z of 28 and 26.5 MeV/c corresponds to T = 3.6 and 3.3 MeV if p ≈ p_z. Marked as a
    verifier observation.
27. New candidate checks (P0) were added to `validation.methods`:
    - `SOURCE_TARGET_VESSEL_DIAMETER_MR7`: D346/2 = 173 mm, the r_e of the Table C.3 titanium vessel.
    - `SOURCE_TARGET_SHIELDING_VESSEL_DIAMETER_MR7`: D1218/2 = 609 mm, the r_e of the Table C.3 outer tungsten
      shielding.

    Both reproduce exactly.

## Removed

None. No value was unsupported, read from a plot, assigned to the wrong stage or table, or invented.

## Arithmetic checks (all recomputed)

| Record(s) | Check | Result |
|---|---|---|
| SOURCE_PD_LINAC_BEAM_POWER_5GEV_MR7, SOURCE_TARGET_BEAM_POWER_MR7 | 5e14 × 5 GeV × e × 5 Hz | 2.0027 MW vs 2: reproduces (+0.14 %) |
| SOURCE_PD_LINAC_BEAM_POWER_10GEV_MR7, SOURCE_TARGET_4MW_BEAM_POWER_MR7 | 5e14 × 10 GeV × e × 5 Hz | 4.0054 MW vs 4: reproduces (+0.14 %) |
| SOURCE_PD_ACCUMULATOR_TURNS_5GEV_MR7 | 2.5 ms × c / 180 m, β = 1 | 4163.8 vs 4167 (0.08 %); exactly 4166.7 with c = 3e8. With β(5 GeV kin) = 0.98744: 4111. Reproduces only under β = 1 |
| SOURCE_PD_ACCUMULATOR_TURNS_10GEV_MR7 | 5.0 ms × c / 300 m | 4996.5 vs 4167 (−16.6 %): NOT reproduced |
| SOURCE_TARGET_YIELD_MUPLUS_5GEV_MR7 | 0.024 /GeV × 5 GeV vs 12 % (Table 1.2 caption) | 0.120: reproduces exactly |
| SOURCE_TARGET_YIELD_MUMINUS_5GEV_MR7 | 0.018 × 5 vs 9 % | 0.090: reproduces exactly |
| SOURCE_FE_OUTGOING_MUMINUS_YIELD_MR7 | 0.018 × 5 × 500e12 vs Table 1.2 45e12 μ− | 45.0: reproduces exactly |
| SOURCE_FE_OUTGOING_LONG_EMITTANCE_MR7 | 46 mm × m_μc²/c vs 16.0 eV ms | 16.21 eV ms: consistent within 1.3 %, not exact (16.0 eV ms = 45.4 mm) |
| SOURCE_TARGET_ROD_DIAMETER_MR7 | 30/2 vs 15 mm rod radius (text, C.3) | 15: reproduces exactly |
| SOURCE_TARGET_VESSEL_DIAMETER_MR7 (new) | 346/2 vs C.3 r_e 173 | reproduces exactly |
| SOURCE_TARGET_SHIELDING_VESSEL_DIAMETER_MR7 (new) | 1218/2 vs C.3 r_e 609 | reproduces exactly |
| SOURCE_TARGET_RADIAL_BUILD_L02…L20_{RE,DR}_MR7 (38) | r_e = r_i of the layer above; Δr = r_e − r_i | all 19 Δr and 19 continuity checks reproduce exactly |
| SOURCE_COOLING_REACCEL_FINAL_MOMENTUM_MR7 | p(T = 250 MeV) | 339.60 MeV/c vs 339: reproduces (+0.18 %) |
| SOURCE_COOLING_REACCEL_FINAL_KINETIC_ENERGY_MR7 | T(p = 339 MeV/c) | 249.43 MeV vs 250: reproduces (−0.23 %) |
| SOURCE_COOLING_{SHORT,LONG}RECT_{FINAL_COOLING,REACCEL}_END_EPS_T_TARGET_MR7 (4) | 0.9 × 25 µm | 22.5: reproduces exactly |
| SOURCE_COOLING_SHORTRECT_RECT_END_TRANSMISSION_MR7 | 0.95 × 14.9 | 14.155 vs 14.9: NOT reproduced (confirmed) |
| SOURCE_COOLING_SHORTRECT_FINAL_COOLING_END_TRANSMISSION_MR7 | 14.9 × 0.427 | 6.36 → 6.4: the stated product reproduces. With the 0.95 factor, 6.04 → 6.0: not reproduced |
| SOURCE_COOLING_LONGRECT_RECT_END_TRANSMISSION_MR7 | 0.95 × 11.1 | 10.545 → 10.5: reproduces |
| SOURCE_COOLING_LONGRECT_FINAL_COOLING_END_TRANSMISSION_MR7 | 10.5 × 0.614 | 6.447 → 6.4: reproduces. Table 1.3 prints 6.5 for the same chain (10.512 × 0.614 = 6.454) |
| SOURCE_COOLING_{SHORT,LONG}RECT_REACCEL_END_TRANSMISSION_MR7 | 6.4 × 0.86 | 5.50 vs 5.8: NOT reproduced (confirmed). Table 1.3 gives 5.6 |
| SOURCE_COOLING_EPS_L_TARGET_EVS_EQUIVALENT_MR7 | 0.064 m × m_μc²/c | 0.022556 eV s vs 0.0225: reproduces (+0.25 %) |
| SOURCE_COOLING_TARGET_EMITTANCE_MARGIN_MR7 | 1 − 22.5/25; 1 − 0.0225/0.025 | 10.0 % both: reproduces exactly. 0.025 eV s = 70.9 mm, and 0.9 × 70.9 = 63.8 ≈ 64 mm |
| SOURCE_COOLING_RECT_{A1…A4,BUNCH_MERGE,B1…B10}_CUM_TRANSMISSION_MR7 (15) | running product of the printed stage transmissions | see below |

Running product of the printed D.5 stage transmissions against the printed cumulative transmission:

| Stage | A1 | A2 | A3 | A4 | Bunch merge | B1 | B2 | B3 |
|---|---|---|---|---|---|---|---|---|
| Product | 75.20 | 63.47 | 54.33 | 49.60 | 38.69 | 32.96 | 29.47 | 25.79 |
| Printed | 75.2 | 63.5 | 54.3 | 49.6 | 38.7 | 33.0 | 29.4 | 25.8 |

| Stage | B4 | B5 | B6 | B7 | B8 | B9 | B10 |
|---|---|---|---|---|---|---|---|
| Product | 23.16 | 20.70 | 18.30 | 16.98 | 14.93 | 12.72 | 11.08 |
| Printed | 23.2 | 20.7 | 18.2 | 17.0 | 14.9 | 12.7 | 11.1 |

13 of the 15 rows reproduce to the printed digit. B2 (+0.07 pp) and B6 (+0.10 pp) are within the extractor's ±0.15 pp
tolerance but miss by one unit in the last digit, which rounding of the stage values explains.

Extra checks, not written into records:

- Table 1.3 chain: 95 × 49.6 × 78 × 28.6 × 61.4 × 86 % gives 47.12, 36.75, 10.51, 6.45 and 5.55. The printed values
  are 47.1, 36.8, 10.5, 6.5 and 5.6, so all reproduce.
- Products of the D.5 stages:
  - A1–A4: 49.60 %, the Table 1.3 'Rectilinear A' value;
  - B1–B10: 28.63 %, the Table 1.3 'Rectilinear B' value;
  - B1–B8: 38.58 %.
- ε_6D against ε_T²·ε_L in D.5: the ratio ranges from 0.97 to 1.07. This is consistent, as expected for a 6D emittance
  that includes correlations, but it is not an identity.

## Residual doubts (not resolved; for the lead / conflict registry)

1. **Conflict candidates for `research/source_conflicts.yaml`** (not my file; none of them is there yet):
   - muon window Ti (Table C.1) vs Be (text, p. 45);
   - Table 4.1 short-rectilinear 14.9 % and the 6.4 % that inherits it;
   - 5.8 % after re-acceleration vs 5.5 % (D.21) and 5.6 % (Table 1.3);
   - Table 4.1 long-rectilinear ε_T 22.5 µm vs D.17 23 µm;
   - the 42 T bound vs D.14 −43.4 T;
   - Table B.2 accumulator turns 4167 vs 5000;
   - the short-rectilinear 64 mm after re-acceleration vs 42.68 mm after final cooling.

   Under policy §4, the competitors should stay `low` until a treatment is recorded.
2. Table 3.2 header unit '[10^-2 GeV /p+]'. It is read as 10^-2 per (GeV · proton). The reading is confirmed by the
   Table 1.2 caption, which says 'The 9% transmission in the front-end refers to the yields from Option 1 as per Table
   3.2' and gives 12 % for μ+, and by Table C.8 ('1/GeV per p+'). The printed unit itself is still typographically
   inconsistent.
3. The accumulator turns (5 GeV) relation is the extractor's hypothesis: injection over the full 2.5 ms source pulse at
   β = 1. MR7 does not say how 4167 was obtained.
4. 'Option 1' in the Table 1.2 caption is not defined next to the table. Fig. B.2 labels the 2 MW scheme 'Option 1',
   which is the likely meaning.
5. Mean p_z at the end of 6D cooling is 200 MeV/c (Table 4.1). The first rows of D.16 and D.20, the start of final
   cooling, print 135 and 95 MeV/c. MR7 does not describe the transition. Not recorded in this file, because D.16 and
   D.20 are out of the extraction scope.
6. The 5 MeV pre-accelerator injection energy vs the 28 and 26.5 MeV/c mean p_z (3.6 and 3.3 MeV): see note 26.
   Transverse momentum would raise the kinetic energy only slightly, so a small gap may remain. This is an observation,
   not a conflict.
7. Registry stage. `tests/unit/test_registry_integrity.py::test_csv_registries_in_sync` and
   `::test_source_parameters_extracted_in_sync` fail until the lead runs `tools/build_registries.py` and
   `tools/sync_parameters_extracted.py`. Both failures come from the new, uncommitted G7 files and not from these edits,
   which change no id.

## Validation runs (after the last edit)

- `uv run python tools/validate_yaml.py provenance parameters/source/imcc_mr7_proton_driver_target_cooling.yaml`:
  0 schema errors.
- `uv run python -m lhmuc validate`: 0 errors, 0 warnings over the whole tree, 7347 parameters at the time of the run.
- `uv run pytest tests/unit tests/scientific`, with the two registry-sync tests above deselected: 193 passed.
