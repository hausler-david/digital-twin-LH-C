# Verification note — group G4_MDI_NOZZLE (Phase 0 addendum, 2026-10-29)

Role: adversarial verifier. Files verified (all written by the G4_MDI_NOZZLE extraction of 2026-10-28):

- `parameters/interaction_region/nozzle_ws2026_kilic.yaml` (238 records; 238 after verification)
- `parameters/interaction_region/mdi_imcc_mr7_maia_music.yaml` (156 → 156)
- `parameters/interaction_region/nozzle_effects_ws2026_acosta.yaml` (34 → 44; 10 records added)
- `parameters/materials/nozzle_materials_addendum.yaml` (4 materials → 4)

Sources: SRC_WS1681458_KILIC_NOZZLE (all 25 slides), SRC_WS1681458_ACOSTA_NEAR_BEAM (slides 4, 6-7, 10, 13-15, 22, 28),
SRC_ARXIV_2510_27437 (MR7, PDF pp. 22, 24, 65, 66), SRC_ARXIV_2502_00181 (MAIA, PDF pp. 6-10, 17), SRC_ARXIV_2601_13189 (MUSIC,
pp. 1-4); SRC_ARXIV_2203_06258 and arXiv:2506.15445 (ref. list) were consulted only to check two attributions. Method: every
record was compared with the cited page — text layer for prose, page images at 200-600 dpi for every table cell, plot inset, legend,
drawing label and equation (Kilic slides 4, 5, 9-12, 16-21, 25; Acosta 10, 13-15; MR7 Table G.1/G.2/G.3, Fig. G.1, Tables 7.2, 8.1,
8.2; MAIA Fig. 1). The 60 table rows of Kilic slides 20-21 were parsed from the text layer, cross-checked against the images and
compared cell by cell with the records; all derivations and P1 checks were recomputed independently. Scripts (verifier scratchpad
`verify_g4/`): `check_kilic_tables.py` (cells, ΔEloss and Q²rec reproduction), `check_quotes.py` (quotation locator),
`apply_g4_fixes*.py` (edits; the YAML round-trips byte-identically through the generator's dump settings, so only the edited fields
changed), `corrections_log.json` (395 entries: 381 single-field changes, 4 aggregated confidence-cap entries, 10 new records).

## What was checked and found correct

- **Values and units**: every numeric value of the 428 extracted records matches the cited page. Kilic: 487.8 / 100 / 6 cm drawing
  dimensions (slide 4, read at 300 dpi; the 487.8 cm line spans base→step, 100 cm step→tip, 6 cm tip→IP), 40(100) mrad and
  η_max ≃ 4(3), Geant4 11.4, MG5_aMC → Pythia 8.312 → HepMC 2.06.11, NNPDF23_lo_as_0130_qed, 250 000 events, Ep 7 TeV / Eμ 1 TeV,
  the six legend pairs of slides 9-11, all 12 cells of the slide-12 table, the 16 Gaussian-fit inset values of slides 16-19 (xc, w and
  their errors), all 120 cells + 15 η keys of slides 20-21, the summary 99.9 % / 2.4-3 % / 5-17 %. MR7: all 22 Table G.1 coordinates,
  Fig. G.1 4 cm / 8 cm labels, Table G.2 (18 g/cm³, W/Ni/Cu −0.95/−0.035/−0.015, 0.918 g/cm³, H/C/B 0.5/0.25/0.25), Table G.3
  (100 keV, 100 keV, 0.01 meV), 1.8e12, L* = 6 m, 2.3 cm / 1 mm Be pipe, 10°, Table 7.2 nozzle rows (10-600 / 10-550 mm, 60-6000 mm),
  Table 8.1 (14 cells incl. the merged MAIA/MUSIC cells), Table 8.2 (5 species), 1.2e7 s / 139 days, 11.4 km. MAIA: EU24 (v0.8),
  L* = 6 m, 1.8e12, 25 µm rad, 1.5 TeV MAP design, 100 keV / thermal, 477 / 511 keV, 20 Fig. 1 coordinates, |η| = 2.44 ↔ 10°, 5 T vs
  3.57 T. MUSIC: ±6 m, O(10⁸), O(10⁶), < 1 GeV, 100 GeV, two tungsten nozzles, 5 T, 5000 hits/cm² in [−0.5, 15] ns, 400 MeV/cm², ~60 %.
  Acosta: |η| < 2.4, 750 GeV, 6 m, ~2.4 < |η| < 7, ~10 %, the full ROOT statistics box (1000, 816.8, 154.9, 62.68/17, 3.772e−07,
  48.71 ± 2.47, 886.3 ± 1.8, 24.56 ± 1.12), 0.72 / 0.14 / 0.48 mrad, Q² = 20, x = 0.8e−5, η = 6, E = 900 GeV, σ ~ 33 %, 1000 × 7000 GeV.
- **Arithmetic re-done** (all agree with the extractor unless listed under corrections): −ln tan(20 mrad) = 3.912, −ln tan(50 mrad) =
  2.995, −ln tan(5°) = 2.436; 487.8 + 100 = 587.8; 6 + 100 + 487.8 = 593.8; 595 − 6 = 589; atan(16.57/94) = 9.997°, atan(37.43/495) =
  4.324°; 55 − 51 = 4, 51 − 43 = 8; exit fractions 521/235253 = 0.002215, 652/221398 = 0.002945, 11545/960005 = 0.012026, 725/119755 =
  0.006054, 819/102604 = 0.007982; 100 − energy-weighted acceptance = 99.989/99.993/99.995/99.996; ΔEloss = (1 − Erec/Etrue)·100
  reproduces all 30 cells within 0.01 (rounding of Erec); 1 − 1158.85169/1300 = 10.86 %, 1 − 1159.08133/1300 = 10.84 %,
  1 − 3457.25332/3850 = 10.20 %, 1 − 3454.34894/3850 = 10.28 %; (w/2)/xc = 2.68 / 2.62 / 2.73 / 2.82 % (the tabulated ΔQ²rec % is
  ≈ 0.95 × these, not reproduced); Table 8.2 sum = 2.11251e8; 1.2e7 s / 86400 = 138.9 d; Highland θ0 for 600 cm W (X0 = 0.3504 cm) =
  0.722 / 0.144 / 0.481 mrad at 1 / 5 / 1.5 TeV; 1 − 886.3/1000 = 11.4 %, 1 − 816.8/1000 = 18.3 %, 24.56/886.3 = 2.8 %;
  DIS point y = 20/(0.8e−5 · 2.8e7) = 0.089, E′ = 910.7 GeV, η = 6.06; BPE mass fractions H 0.0812 / C 0.4836 / B 0.4352.
- **Statuses** of the Kilic and MR7/MAIA/MUSIC records are correct (reported_lhmuc for the Kilic LHμC study; analogous for every IMCC
  value; analytical_estimate / derived_lhmuc with derivations naming the input ids). Units parse; null ≠ 0 respected (two null
  densities are genuine "not stated"); scenario null everywhere (no scenario file assigned to this group).
- **Canonical ids** exist once with the stated values: DET_NOZZLE_LENGTH_WS2026_KILIC (487.8 cm), DET_NOZZLE_FIRST_SECTION_LENGTH_WS2026_KILIC
  (100 cm), DET_NOZZLE_TIP_DISTANCE_WS2026_KILIC (6 cm), DET_NOZZLE_MATERIAL_WS2026_KILIC ('tungsten'),
  DET_NOZZLE_HADRON_ABSORPTION_FRACTION_WS2026_KILIC (0.999), DET_NOZZLE_TIP_DISTANCE_MR7 (6 cm), DET_NOZZLE_LENGTH_MR7 (595 cm),
  DET_NOZZLE_OUTER_ANGLE_NEAR_IP_MR7 (10 degree), IR_LSTAR_MR7 (6 m), DET_SOLENOID_FIELD_MAIA (5 T), DET_SOLENOID_FIELD_MUSIC (5 T),
  DET_NOZZLE_ETA_EDGE_MAIA (2.44). No id was renamed or removed.

## Corrections made

### All four files
1. **Confidence caps** (validator errors since commit 03e0ab1, source_quality_policy.md §4/§5.2): Kilic 219 'high' → 'medium'
   (unrefereed slides; 17 records were already medium and the two π⁺ 40 mrad counts stay 'low'); Acosta 27 'high' → 'medium' (7 were
   already medium); MR7/MAIA/MUSIC 130 'high' → 'medium' (status analogous; analytical estimates not above their inputs); materials
   4 'high' → 'medium'.
2. **Confidence 'low'** (policy §4 "low when the analogy requires rescaling") for 26 MR7/MUSIC records whose numbers scale with beam
   energy, bunch intensity (1.8e12 vs the LHμC 1e10) and lattice: the five Table 8.2 BIB multiplicities and their sum, the 14 Table 8.1
   doses/fluences, MUSIC O(10⁸) BIB and O(10⁶) IPP secondaries, IPP 100 GeV end point, 5000 hits/cm², 400 MeV/cm², ~60 % endcap
   photon efficiency.

### Kilic deck (nozzle_ws2026_kilic.yaml)
3. **Table quotations not exact (60 records)**: the slides 20-21 cell strings had trailing zeros dropped ('31.7' for 31.70, '7.0' for
   7.00, '5.5', '1.2', '0.4', '10.2', '978.2', '2.6', '20.5', '11.6', '7.3'); restored to the printed cells (values were right).
4. **Inset quotations (8 records)**: fit errors printed in E-notation ('4.83649E-4', '9.67574E-4', '3.92949E-4', '7.85908E-4',
   '5.18511E-5', '1.03775E-4', '3.62866E-5', '7.2578E-5') had been converted to decimals; restored as printed.
5. **Cropped 40 mrad legends (6 records, slides 9-11)**: the quotation reconstructed the hidden left part of the legend ("Entering primary
   protons (N=221398)"); replaced by the visible text with '…' ("…rimary protons (N=221398) | …mary protons (N=652)", "…ring primary
   pion plus (N=960005) | …g primary pion plus (N=11545)", "…ering primary kaon plus (N=102604) | …ting primary kaon plus (N=819)").
6. **DET_NOZZLE_PIPLUS_ENTERING/EXITING_40MRAD notes were wrong**: they said the 40 mrad plateau is an order of magnitude lower (≈2e3 vs
   ≈3e4 per bin). Reading the 40 mrad panel's own decade grid (10⁰ tick, minor-grid spacing) gives a plateau of ≈3e4, and sampling both
   panels every 0.05 in log₁₀E (172 points) shows the curves agree within 0.05 in log₁₀(counts) except at 6 bin-edge points: the 40 mrad
   π⁺ panel duplicates the 100 mrad histogram and legend. Notes rewritten; confidence stays low.
7. **Q²rec cells now reproduced (30 records, P0 → P1)**: the extracted notes said the Q²rec cells cannot be reproduced. All 30 are
   reproduced to the printed two decimals by Q²rec = 4·Etrue·Erec/(1 + e^(2η)), i.e. the slide-25 formula with Ebeam := Etrue and
   E′ := Erec (identification inferred, stated as such); Ebeam = 1 TeV fails (0.91 vs 1.19, 7.98 vs 1.20 GeV²). Method, dependency on
   the Erec record and notes updated; DET_NOZZLE_Q2_DEFINITION_WS2026_KILIC notes corrected accordingly (they presumed Ebeam = 1 TeV).
8. **DET_NOZZLE_SIM_BEAM_DIRECTIONS_WS2026_KILIC notes were wrong**: they claimed the +z nozzle (slide 25) contradicts the 'muon coming
   side' (slide 4). With the μ⁺ moving toward −z it arrives from +z, so the statements agree (the +z side is also the proton/forward-hadron side).
9. **DET_NOZZLE_Q2_SMEARING_METHOD_SOURCE_WS2026_KILIC notes mis-identified the reference** as SRC_ARXIV_2203_06258 ("The Potential of a
   TeV-Scale Muon-Ion Collider", JINST). The cited title "Physics Potential, Accelerator Options, and Experimental Challenges of a TeV-Scale
   Muon-Ion Collider" is PoS(ICHEP2024)817 (2024) (μLHC paper arXiv:2506.15445 ref. [63]); not registered, not read.
10. **DET_NOZZLE_HOST_DETECTOR_WS2026_KILIC value mis-attributed** the detector figure to K. Piotrzkowski (DIS 2026). On slide 5 the
    LHeC/ESPP credit sits by the detector figure and "Adapted from K. Piotrzkowski, DIS 2026." heads the 40(100) mrad text box. Value now
    'LHeC detector design presented at the ESPP Open Symposium 2025 (adapted)'; the Piotrzkowski credit is documented in its notes and
    in the notes of the four 40/100 mrad and η_max records.
11. **DET_NOZZLE_MATERIAL_WS2026_KILIC quotation** mixed a slide-5 label into a page-4 citation; the page-4 sentences are kept and the
    slide-5/8 mentions moved to notes (same fix for MAT_TUNGSTEN_WS2026_KILIC, whose table_figure_or_equation 'nozzle drawing' → null).
12. **DET_NOZZLE_HADRON_ABSORPTION_FRACTION_WS2026_KILIC notes**: "consistent only with the energy-weighted figures" was wrong (those are
    99.989-99.996 %, i.e. ≈ 99.99 %); the summary's ≈ 99.9 % matches neither the by-count (99.03-99.23 %) nor the by-energy figures.
13. **Inferences marked as inferences**: the 12 hadron-count names no longer assert "(Geant4, 250 000 events)" (the slides do not say
    which sample the histograms count; notes say "presumably"); the four particle-acceptance notes flag the "transmitted fraction"
    reading as an interpretation; the 30 Erec notes now say only the 1300/3850 GeV rows are shown to be Gaussian-fit centres; the word
    "radiative" (not on the Kilic slides) removed from 34 notes; the five exit-fraction notes say what the histograms show.
14. **Validation methods**: the four η_max / half-angle P1 records name the lead's test
    `tests/scientific/test_workshop_decks.py::test_nozzle_half_angle_to_eta_max_forthomme_and_imcc` (check_ids added); the four
    summary-range P1 records state which table cell reproduces which end (2.48 → "≈2.4", 2.97 → 3, 5.01 → 5, 16.82 → 17).
15. Residual drawing ambiguity documented in DET_NOZZLE_FIRST_SECTION_LENGTH and DET_NOZZLE_BASE_DISTANCE_FROM_IP_IMPLIED (see doubts).

### MR7 / MAIA / MUSIC (mdi_imcc_mr7_maia_music.yaml)
16. **P1 → P0 (13 records)** where the "check" was only the same number in another table or document (corroboration, not an arithmetic
    reproduction): DET_NOZZLE_TIP_DISTANCE_MR7, IR_FIRST_MAGNET_DISTANCE_MR7, DET_NOZZLE_RMIN/ZMIN_MUCOLL_MR7,
    DET_NOZZLE_RMIN/RMAX/ZMIN_MUSIC_MR7, DET_NOZZLE_RMIN/RMAX/ZMIN_MAIA_MR7, DET_BIB_SIM_THRESHOLD_NON_NEUTRON_MAIA,
    DET_SOLENOID_FIELD_MAIA, DET_SOLENOID_FIELD_MUSIC. The corroboration text is kept in validation.notes.
17. Test ids added to DET_NOZZLE_OUTER_ANGLE_NEAR_IP_MR7, DET_NOZZLE_OUTER_ANGLE_FAR_IMPLIED_MR7
    (`test_imcc_nozzle_outer_surface_angles_mr7_table_g1`), DET_NOZZLE_ETA_EDGE_MAIA and DET_NOZZLE_POLAR_ANGLE_EDGE_MAIA; the latter's
    reproduction now uses MAIA's own Fig. 1 points (−6, 1), (−100, 17.57).
18. **DET_NOZZLE_OUTER_W_SHELL_THICKNESS_BASE_MR7 notes were self-contradictory** ("tapers to zero at z = 100 cm" next to "4 cm there");
    Table G.1 gives a constant 4 cm shell (55 − 51 at 595 cm, 17.57 − 13.57 at 100 cm). Both Fig. G.1 label records: label position
    "z ≈ −560 cm" → "z ≈ −545 cm" (measured at 300 dpi).
19. **DET_NOZZLE_BPE_OUTER_END_Z_MR7 notes**: claimed MAIA Fig. 1 prints the (100, 13.57) point; it does not (MAIA labels 10 of the 11
    Table G.1 points).
20. **DET_BIB_NOZZLE_EXIT_POSITION_STATEMENT_MAIA**: page 8 → 7 (the quotation starts on PDF p.7 and runs onto p.8).
21. Notes: Table 8.2 records — "IR lattice v0.8" is stated for the Table 8.1 studies and only presumed for Table 8.2, rescaling caveat
    added; DET_NOZZLE_MAP_DESIGN_CM_ENERGY_MR7 — "no optimisation exists at all" softened (the Kilic study exists, no optimisation);
    DET_NOZZLE_COUNT_MUSIC — causal "because both beams decay" is not in the proceedings.

### Acosta deck (nozzle_effects_ws2026_acosta.yaml)
22. **Status reported_lhmuc → analogous (6 records)**: DET_NOZZLE_LENGTH_WS2026_ACOSTA (6 m), DET_NOZZLE_MATERIAL_WS2026_ACOSTA,
    DET_NOZZLE_ETA_COVERAGE_MIN/MAX_WS2026_ACOSTA (~2.4 / 7), DET_NOZZLE_REFERENCE_FIGURE_WS2026_ACOSTA and
    DET_CENTRAL_MUON_COVERAGE_ETA_MAX_WS2026_ACOSTA (|η| < 2.4). These restate the μ⁺μ⁻-collider nozzle ("the 6m long tungsten nozzles",
    drawing attributed to JINST 13 P09004 (2018)) and the central coverage left by forward AND backward nozzles (the same |η| < 2.4 is
    used on slide 7 for the 10 TeV muon collider); they are not LHμC design values. applicability → analogous with the original source
    named. The deck's own LHμC statements and estimates (configuration, condition, GEANT energy loss, σθ, Q² resolution, summary) stay
    reported_lhmuc.
23. DET_NOZZLE_MS_FORMULA_WS2026_ACOSTA value: "PDG Highland formula" → "PDG multiple-scattering formula" ('Highland' is not printed).
24. P1 wording for DET_NOZZLE_MUON_ENERGY_LOSS_PEAK_1TEV and _FIT_MEAN: 11.4 % "is consistent with", not "reproduces", '~10 %'.
25. Notes: DET_NOZZLE_REFERENCE_FIGURE ("match the IMCC/MAP nozzle" → close to but not identical: 60 cm at 600 cm vs 55 cm at 595 cm);
    DET_Q2_RESOLUTION_TEST_X ('10--5' is a text-layer artefact; the slide shows superscript −5); DET_NOZZLE_MS_SIGMA_THETA_1P5TEV
    (1.5 TeV = muon-ion-collider 'LHmuC' option, not the HELP4CERN 1 TeV baseline); DET_NOZZLE_LENGTH (what the value is).

### Materials (nozzle_materials_addendum.yaml)
26. Unsourced numbers/facts removed from notes: "Plansee trade name" and "19.25 g/cm³ for pure tungsten" (MAT_INERMET180_MR7),
    "typically 5 wt.% B" (MAT_BORATED_POLYETHYLENE_MR7), "handbook 1.85 g/cm³" (MAT_BERYLLIUM_PIPE_MR7).

## Records added (10)
DET_BIB_COLLAMATI_{PHOTONS,ELECTRONS_POSITRONS,NEUTRONS,CHARGED_HADRONS,MUONS}_{WITH,WITHOUT}_NOZZLES_WS2026_ACOSTA: the legend
values of the F. Collamati et al. 2021 (JINST 16 P11009, 750 GeV beams) Fig. 11 reproduced on Acosta slide 10 — γ Y 5.0e+07 / N 3.4e+08,
e⁺/e⁻ 8.5e+05 / 2.5e+07, n 1.1e+08 / 1.8e+07, ch. had. 1.7e+04 / 4.1e+04, μ⁺/μ⁻ 1.0e+03 / 1.0e+03 (Y = with nozzles, N = without, per
the printed caption). Status analogous, confidence low (normalisation not stated on the slide, original paper not read, 1.5 TeV μ⁺μ⁻
case). Notable: the nozzles reduce photons ×6.8 and e± ×29 but increase the neutron count ×6 in that figure — a quantitative counterpoint
to Kilic slide 3 "reduce the BIB by several orders of magnitude".

## Records removed
None. Every record is supported by its cited page.

## Residual doubts (for the lead / registry stage)
- **Kilic π⁺ 40 mrad panel (slide 10)** duplicates the 100 mrad histogram and legend: DET_NOZZLE_PIPLUS_ENTERING/EXITING_40MRAD_WS2026_KILIC
  are very likely not 40 mrad results (candidate erratum / conflict record; author query).
- **Kilic ΔQ²rec % definition** still not reproduced: the tabulated value is ≈ 0.95 × (w/2)/xc of the insets for all four fitted rows
  (2.56 vs 2.68, 2.49 vs 2.62, 2.58 vs 2.73, 2.67 vs 2.82); possibly the histogram RMS/mean. Q²rec itself is now reproduced.
- **Kilic Ebeam := Etrue** in the Q²calc formula is an inference from the 30-cell reproduction, not stated on the slides.
- **Kilic slide-4 drawing**: the sketch resembles the MAP/IMCC nozzle; read literally, '100 cm' is the tip-section length (step at
  106 cm, base at 593.8 cm); if it meant 100 cm from the IP (as in the IMCC table) the base would be at 587.8 cm. The rotated blue
  annotation by the nozzle on slide 5 reads "9.65 m…" at 600 dpi with the last character under an arrowhead (m or mm): not extracted.
- **Kilic summary "≈ 99.9 % absorbed"** is reproduced by neither the by-count (99.03-99.23 %) nor the by-energy (99.989-99.996 %) columns;
  the hadron sample of slides 9-12 (250 000 events?) is not stated; base dimensions, nozzle W grade/density and cladding are open (slide 22).
- **MR7 internal discrepancy**: Table 7.2 nozzle z_max 6000 mm vs Table G.1 base plane 595 cm (candidate conflict record, as flagged
  by the extractor). Also MuColl solenoid 3.6 T (MR7 Table 7.2) vs 3.57 T (MAIA text) — rounding, not a conflict.
- **MR7 Table G.2 borated polyethylene** 25 at.% B (≈ 43.5 wt.%) recorded as printed; candidate author query.
- **Acosta**: who ran the 1 TeV GEANT simulation and with which geometry (pure W or the W/BCH2 drawing) is not stated; the multiple-
  scattering P1 assumes 6 m of pure W (X0 = 0.3504 cm, PDG, not on the slide); JINST 13 P09004 and Collamati et al. 2021 not read.
- **Status judgement** (item 22) is a verifier decision; if the lead prefers to treat "the 6 m tungsten nozzle assumed in the LHμC
  estimate" as an LHμC study assumption, revert the six records to reported_lhmuc — the applicability text then still names the source.
- One vs two nozzles for the LHμC remains undecided across decks (Kilic: muon-coming side; Acosta: "might need just incoming muon beam
  side"; MuIC paper: single-sided, −5 < η < 2.4).

## Validation after the fixes
- `tools/validate_yaml.py`: 0 schema errors in all four files (provenance ×3, material ×1).
- `python -m lhmuc validate`: 0 errors and 0 warnings in the four G4 files (the remaining errors of the run, 2335, are confidence-cap
  errors in other groups' files); `tools/apply_confidence_caps.py --check` on the three parameter files: 0 records exceed a §4 cap.
- `pytest`: tests/unit/test_confidence_caps.py, test_schemas.py, test_units.py and tests/scientific/test_workshop_decks.py pass;
  test_no_validation_errors fails only on other groups' files, test_csv_registries_in_sync only because the registries are not yet
  rebuilt (registry stage: `uv run python tools/build_registries.py`).
