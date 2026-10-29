# Verification note — group G5_DETECTOR (Phase 0 addendum, 2026-10-29)

Role: adversarial verifier. Files verified (all written by the G5_DETECTOR extraction of 2026-10-28), records before → after:

- `parameters/detector/lhmuc_detector_concept_ws2026_forthomme.yaml` (168 → 171; 3 added)
- `parameters/detector/tev_muon_resolution_ws2026_yamazaki.yaml` (52 → 52)
- `parameters/detector/near_beam_spectrometer_ws2026_acosta.yaml` (116 → 121; 5 added)
- `parameters/detector/maia_10tev_detector.yaml` (217 → 222; 5 added)
- `parameters/detector/music_10tev_detector.yaml` (117 → 117)
- `parameters/detector/muic_acosta2022_delphes_card.yaml` (155 → 155)

825 records checked, 838 after verification, none removed. Sources: SRC_WS1681458_FORTHOMME_DETECTOR (slides 2–3, 5–14,
18–19), SRC_WS1681458_YAMAZAKI_TEV_MUON (slides 2–16), SRC_WS1681458_ACOSTA_NEAR_BEAM (slides 3–7, 9, 11–12, 16–22, 25–27),
SRC_ARXIV_2502_00181 (MAIA, pp. 10–37), SRC_ARXIV_2601_13189 (MUSIC, pp. 1–5), SRC_ARXIV_2203_06258 (muon-ion collider paper,
PDF pp. 30–31, 37–45).

Method: every record was compared with its cited page. Prose was checked against the text layers. Every slide, table cell,
drawing label, legend, ROOT fit box and plot title was checked on page renderings at 150–400 dpi: all Forthomme, Yamazaki and Acosta
slides that carry records (slides 6, 8, 11 and 12 also at 300–400 dpi), MAIA Fig. 7, MUSIC Figs. 1–2 and MuIC Tables 16–18. MAIA
Tables 1–3 were compared cell by cell with the text layer. A script located every quotation fragment in the page text; the fragments it
could not match were figure labels, equations and two-column or cross-page layout, and all were confirmed on the images. A second script
checked that each numeric value, or its unit-converted form, appears in its own quotation. Its 17 exceptions were word numbers and
phrases ('three', 'four', 'six', 'seven', 'one', 'fewer than five', 'no magnetic field', 'an order of magnitude', '~MGy'), the two
derived MAIA envelope values, the two evaluated Table-16 expressions and the summed pixel-layer count; all were confirmed by hand. All
derivations and P1 checks were recomputed independently. The edits were made by scripts that load, modify and re-dump the YAML with
the generator's dump settings; that round trip is byte-identical, so only the edited fields changed. Every change was logged (187
field-level entries plus the aggregated confidence caps), and the final files were diffed field by field against copies taken before
verification: there are no unlogged value, unit, page or status changes.

## What was checked and found correct

- **Values and units.** Every value matches the cited page, apart from the items listed under the corrections. The checks covered:
  - **Forthomme:** LHeD 13 m × 9 m; ~1° < θ < 179°; 0.1 mm sensors; 2×10^15 and 10^16 n_eq/cm²; ~0.2 X0; 10 µm at 4 < θ < 90°;
    δpT/pT² ~ 0.001 GeV⁻¹ at 100 GeV; 5 / 8 endcap layers vs 7 / 5 wheels; 4 + 4 + 1 + 1 barrel layers.
  - **Forthomme, continued:** the slide-6 drawing labels; the ZDC (Si-W, 30 cm, ~100 m, 1 cm / 1 mm cells); 40 (100) mrad → η_max ~ 4 (3);
    3.8 T Delphes solenoid; ∫B·dl 2–4 → 10–30 T·m (CMS 50, ATLAS 2–6 / 3–8 / 2); 100 ps; ~MGy; the −3 … −6 < η < 6 acceptance options;
    360 / 270 MCHF and 71 %.
  - **Yamazaki:** 1 TeV × 7 TeV; 500–5000 GeV and |η| < 3; x = 0.14; the slide-2 endcap table (CMS 4/5/6/6/8 %, ATLAS 5/6/7/7/12/22 %);
    sagitta ~1 mm; 300 GeV; 90 µm; field ×3; 3.76 and 15.4°; 5/7/12 % and 8/15 %; 6–7 %.
  - **Acosta:** 1 TeV × 7 TeV and 5.3 TeV; η ≈ −7 / 2 mrad; Q² < 10^5; the Bhabha cross sections and rates; the toroid box (1.05 m,
    5.1 m, 4.5 m, 4.1 T, 4–18 T·m); stations at 28 / 140 / 660 m and their η edges; 150 µm; ~6 % at 1 TeV; the fit p0 0.02536 ± 0.0001592.
  - **Acosta, continued:** the CSC rings (210 cm, 55.5 / 171.9 and 84.3 / 143.4 cm, 2.4 m², 30 (31)° and 15 (16)°, 24 + 12 = 36);
    6 strip layers at 10 mm; 3.2 mm wires in groups of 5; the hexagon (1.0 m, 1.73 m, 2.6 m², 36 per disk); 1.6 %/m and 1.7 %;
    5 % and 25 %; 0.25–1 TeV; 'Z = 136.0 m'.
  - **MAIA:** all cells of Tables 1–3; 3×10^4 hits/cm²; 10^14−15 n_eq/cm²; 10^2−5 Gy/yr; timing windows; 265 mm Al, |z| ≲ 2.3 m,
    ~4 X0 / 1 λ; the particle-gun ranges; ACTS 32.1.0; the UltraTight cuts; 1.6×10^6 → O(10) fakes.
  - **MAIA, continued:** efficiencies 99/87/79/48 %; σ(1/pT) 2×10^-4 → 2×10^-5 GeV⁻¹; ~5 µm; photon, neutron and pion working points and
    IQR68 values.
  - **MUSIC:** every §2 dimension; 26.5 X0; ~7 λ; the §3 performance numbers (95 %, a few 10^-5, > 90 %, 1 fake μ, 100 %, 10 % / 17 %,
    85 %, kt R = 0.5, 0.85 fake jets, 30 / 10 / 45 %, 55 / 20 / 0.8 %).
  - **MuIC:** all cells of Tables 16, 17 and 18 (Delphes card); the §5.1–5.2 station geometry (z = −5 m and r ≈ 3.5 m; ≥ 30 m;
    z = −40 m and r = 1 m; ~10 T·m); Δη = 10^-4/arctan(e^η) ↔ 0.2 mrad; the 30 % / 70 % kaon sharing; the H → bb̄ selections, ~900
    events and ~3 %.
- **Statuses.**
  - reported_lhmuc is used only for LHμC statements on the three PRIMARY_LHMUC decks: Forthomme 43, Yamazaki 22, Acosta 81.
  - Every restated LHeC value is imported_related: Forthomme 113.
  - Every ATLAS, CMS, HL-LHC, AstroPix, ePIC, IMCC and 10 TeV μ+μ− value is analogous: Forthomme 15, Yamazaki 30, Acosta 38,
    MAIA 220, MUSIC 117. Pure comparators are screening_only.
  - The MuIC paper (RELATED_MACHINE) backs imported_related: 155.
  - Two analytical estimates each in Acosta and MAIA carry derivations naming their input ids.
  - No non-LHμC value carries reported_lhmuc.
  - Units parse, and null ≠ 0 is respected (DET_MUON_SYSTEM_FIELD_MAIA = 0 T is the stated "no magnetic field", with a note).
- **Scenario.** null everywhere except three MuIC records, which point to MUIC-ACOSTA2022-BNL-960GEV (2) and MUIC-ACOSTA2022-LHMUC (1).
  Both scenarios exist.
- **Arithmetic re-done.** The following agree with the records:
  - Forthomme: −ln tan(20 mrad) = 3.91 and −ln tan(50 mrad) = 2.99; 2√(0.05 × 7) TeV = 1.18 TeV; the EMC fit gives 2.70 % at 10 GeV and
    0.53 % at 400 GeV.
  - Yamazaki: cosh 2 = 3.762; 2·atan(e^−2) = 15.4°; 1/7 = 0.143.
  - Acosta: 2√7 = 5.29 TeV; 2·atan(e^−7) = 1.82 mrad. The station η edges are 2.40/3.98, 4.01/5.59 and 5.56/7.14.
  - Acosta, toroid: an ideal toroid gives ∫B·dl = 4.1 × 4.5 = 18.45 T·m at R_in and 3.80 T·m at R_out.
  - Acosta, CSC rings: W/(2 tan(α/2)) gives 1.00/3.10 m and 3.00/5.10 m, matching the handwritten 1.0/3.1/3.0/5.1 m of slide 18;
    trapezoid areas 2.39 m².
  - Acosta, hexagon: 1.732 m and 2.598 m².
  - Acosta, rates: σ·L reproduces all ten Bhabha rates; the implied σ are 8.5 and 200 pb.
  - Acosta, resolution: the ideal formula at r = 3.075 m gives 4.94 % at 1 TeV and 24.7 % at 5 TeV. The slide-12 fit is a
    proportional fit through the origin, and the red line reaches ≈9.6 % at 380 cm, so p0 is the slope in %/cm.
  - MAIA: 2 × 620.0 cm = 12.4 m; 2 × 589.5 cm = 11.79 m; η(57.5°) = 0.600.
  - MUSIC: 96.32/2 = 48.16 cm and 138.46/2 = 69.23 cm (the MAIA Inner Tracker barrel |z|); 888.8/2 = 444.4 cm.
  - MuIC: 5 cm at 5 m gives |η| 5.30, at 30 m 7.09 and at 40 m 7.38; 1 m at 40 m gives 4.38; the small-angle Δη ↔ Δθ relation holds.
- **Canonical ids.** Each exists once with the stated value:
  - In the G5 files: DET_NOZZLE_HALF_OPENING_ANGLE_WS2026_FORTHOMME (40 mrad), DET_NOZZLE_HALF_OPENING_ANGLE_OPTION2_WS2026_FORTHOMME
    (100 mrad), DET_ETA_MAX_WS2026_FORTHOMME (4), DET_ETA_MAX_OPTION2_WS2026_FORTHOMME (3), DET_SOLENOID_FIELD_LHEC_DELPHES_WS2026_FORTHOMME
    (3.8 T).
  - In the G4 file, as referenced by the G5 headers: DET_SOLENOID_FIELD_MAIA (5 T), DET_SOLENOID_FIELD_MUSIC (5 T),
    DET_NOZZLE_ETA_EDGE_MAIA (2.44).
  - In the G1 files: IR_LSTAR_LHEC_WS2026_FORTHOMME (15 m), IR_LSTAR_FCCEH_WS2026_FORTHOMME (23 m), and the Forthomme beam set
    (300 ns, 40 bunches, 1e10, 1e34, 4.3 µm, 7 cm, 3e13 /s, 0.5, implied 6.97e11 protons).
  - No id was renamed or removed. All nine G5 ids referenced from other files (scenarios_addendum_machine.yaml,
    lhmuc_ws2026_forthomme_beam_set.yaml, lhec_ir_ws2026_forthomme.yaml, muic_acosta2022_machine.yaml, nozzle_ws2026_kilic.yaml,
    nozzle_effects_ws2026_acosta.yaml, mdi_imcc_mr7_maia_music.yaml) still resolve.

## Corrections made

### All six files
1. **Confidence caps** (validator errors since research/source_quality_policy.md §4 is enforced): 628 records lowered from 'high' to 'medium'
   with tools/apply_confidence_caps.py. By file: Forthomme 12 (status analogous) + 131 (unrefereed slides); Yamazaki 29 + 20; Acosta 33 +
   76; MAIA 211 (analogous); MUSIC 116 (analogous); MuIC 0 (no cap applies). No other field was touched by this step. Every record of the
   five capped files is now ≤ 'medium'.
2. **Confidence 'low'** (policy §4: "analogous … low when the analogy requires rescaling"). This is the same rule the G4 verifier applied
   to the MR7/MUSIC BIB, dose and fluence records. It covers 29 records whose numbers scale with the beam energy, bunch intensity
   (1.8e12 μ/bunch vs LHμC 1e10), lattice or nozzle of the 10 TeV μ+μ− collider:
   - MAIA: DET_VXD_L1_BIB_HIT_DENSITY_MAIA; DET_TRACKER_NEQ_FLUENCE_MIN/MAX_MAIA; DET_TRACKER_TID_PER_YEAR_MIN/MAX_MAIA;
     DET_BIB_SIM_DISK_PER_EVENT_MAIA; DET_BIB_FAKE_TRACKS_PER_EVENT_LOOSE/ULTRATIGHT_MAIA; DET_FAKE_PHOTONS_PER_EVENT_MAX_MAIA.
   - MUSIC: DET_ECAL_ENDCAP_BIB_ENERGY_DENSITY_RATIO_MUSIC, DET_FAKE_MUONS_PER_EVENT_MUSIC, DET_FAKE_JETS_PER_EVENT_MUSIC.
   - Acosta: the three 10 TeV Bhabha cross sections, the ten Bhabha rates, the two implied cross sections, and
     DET_VBF_SCATTERED_MUON_ETA_MIN/MAX_MUMU10TEV_WS2026_ACOSTA.

   Each record carries a one-line note giving the reason. Geometry, segmentation, timing, thresholds and the performance figures stay
   'medium'.
3. **P1 levels.** P1 is kept only where the arithmetic reproduces a printed value to its printed precision, or confirms a stated
   inequality or coverage. Failed or approximate checks, symmetry or design-convention observations, unit conversions, trivial sums and
   checks that rest on an external PDG constant without reproducing the value were set to P0. In every case the former check is kept
   verbatim in validation.notes, prefixed "Verifier (G5_DETECTOR, 2026-10-29): former P1 check retained as a remark", with the reason.
   This applies to 29 records:
   - Forthomme (3): DET_LHED_POLAR_ANGLE_MAX (symmetry); INFRA_LHED_COST_FWD_CALO_SILICON and _FRACTION (failed check, 270/360 = 75 % vs
     71 % printed).
   - Yamazaki (1): DET_HIGH_Y_MUON_ENERGY_BOUND.
   - Acosta (2): DET_CSC_STEREO_ANGLE_BETWEEN_VIEWS; DET_FWD_SPECTROMETER_STATION3_ETA_MAX (7.14, not 7.2).
   - MAIA (7): DET_SOLENOID_ALUMINIUM_THICKNESS (3.0 X0 from the PDG X0, vs "around 4"); DET_GUN_THETA_MIN and DET_GUN_ETA_MAX (8° ↔
     2.66, not 2.44); DET_GUN_THETA_MAX, DET_BARREL_ONLY_THETA_MAX and DET_PION_STUDY_THETA_MAX (symmetry); DET_TRANSITION_REGION_ETA_MAX
     (1.04 vs 1.01).
   - MUSIC (9): DET_OT_BARREL_LAYER_LENGTH, DET_ECAL_LAYERS, DET_ECAL_BARREL_LENGTH, DET_HCAL_ABSORBER_THICKNESS (8.3 λ vs ~7),
     DET_MUON_BARREL_R_MAX (13.6 vs 12.8 m), DET_MUON_ENDCAP_Z_MAX (11.8 vs 11.4 m), DET_MAGNET_TANK_THICKNESS,
     DET_PHOTON_EFF_CENTRAL_THETA_MIN and _MAX.
   - MuIC (7): PHYS_HBB_STAT_UNCERTAINTY (3 % vs 4.7 %); DET_FAR_BWD_STATION1_ETA_MAX (|η| 1.15 at r = 3.5 m, not 1);
     DET_DELPHES_KAON_HCAL_FRACTION (trivial sum); DET_T16_PHOTON_ and DET_T16_NEUTRAL_HADRON_ANGULAR_RESOLUTION (the stored 0.02511 is
     the extraction's own evaluation of '0.087/√12'); DET_DELPHES_ECAL_ and DET_DELPHES_HCAL_BARREL_GRID_DETA (the 'Δη = Δφ in radians'
     observation; 1° = 0.01745 rad, not the printed 0.0174).

   Conversely, DET_FWD_SPECTROMETER_BDL_MIN/MAX_WS2026_ACOSTA were raised from P0 to P1. The ideal-toroid arithmetic above reproduces the
   printed '4−18 T·m', and the four toroid ids were added as dependencies.
4. **File headers.** Each file gained a "Verified 2026-10-29" line pointing to this note. The Acosta and MuIC headers gained a line saying
   that P1 claims listed above them follow item 3.

### Forthomme deck (lhmuc_detector_concept_ws2026_forthomme.yaml)
5. DET_FIG_BWD_TRACKER_RADIUS_LABEL_LHEC: the drawing prints 'r≈84', not 'r=84'. Name and quotation were corrected, and the uncertainty
   note now reads "source says '≈'".
6. Slide-6 drawing:
   - Explanations of 10 records: the extraction said the drawing is "the same drawing as André et al. 2022 Fig. 4". It is a version of
     it. Six labels coincide (172, 148, 186, 154, 23, 23). Others differ: 53 here vs 88 there, and 146 vs 148. 'Dipole 966' and 'r≈84'
     appear only here. The unit cm is inferred.
   - Notes of 8 records: they called two labels raster-ambiguous, but both are legible at 300 dpi and are now recorded (see Records added).
7. ZDC radiation level (DET_ZDC_NEQ_FLUENCE_MIN/MAX_LHEC, DET_ZDC_TECHNOLOGY_LHEC):
   - The quotation said '10^15-10^16 neq/cm2', but slide 8 prints '1015-1016 neq/cm2' with no superscript formatting. It is now
     verbatim.
   - The 10^15–10^16 reading is an interpretation, supported by the formatted '10^16' of slide 5. A note says so, and confidence was
     lowered to medium.
8. DET_ZDC_HG_CELL_SIZE_FIG_LHEC: quotation corrected. The 1 mm arrow spans the magnified box labelled '1 HG cell', not the 'HG cells'
   grid.
9. DET_MUON_TECHNOLOGY_BASIS_LHEC: the quotation did not cover the RPC/sMDT content asserted in the value. It was extended to the
   printed bullets and the drawing labels ('sMDT Multilayer 2 | sMDT Multilayer 1 | thin-RPC Triplet'). A note lists the unlabelled
   chamber dimensions (287, 39.231, 45.6, 43.0), which are not transcribed as values.
10. DET_LHMUC_HCAL_TECHNOLOGY_OPTIONS: the value glossed 'HE' as 'high-η regions', which the slide does not say. It now reads 'HE' (as
    printed), with a note that 'HE' is not expanded. The closing ')' was restored to the quotation.
11. DET_SYNERGY_EIC_TRACKING_PID_STATEMENT: the value said 'MAPS/MGPD-type sensors', but 'MAPS' is not on slide 19. It now reads 'MGPDs'
    (as printed), with a note.
12. DET_MULTI_TEV_MUON_RESOLUTION_LHC_REF: the explanation equated the cited 'JINST 18 (2023) 09, P09025' with SRC_ARXIV_2203_06258.
    That identification rests only on a search snippet. The uploaded v3 says 'Prepared for submission to JINST' and contains no '~10 %'
    TeV-muon statement. The explanation now says so.
13. MACHINE_SQRT_S_LHEC: a note was added. The kinematic plot on the same slide 2 is labelled 'LHeC, Ep = 7 TeV, Ee = 70 GeV'
    (√s = 1.4 TeV), which is inconsistent with the 1.2 TeV title and the 50 GeV legend of slide 10. The inconsistency is preserved.
14. DET_LHED_COST_REDUCTION_STATEMENT: subsystem changed from infrastructure to detector (DET_ id; a statement on detector design
    choices).

### Yamazaki deck (tev_muon_resolution_ws2026_yamazaki.yaml)
15. DET_ATLAS_ENDCAP_TO_BARREL_FIELD_RATIO: the name inserted '(∫B·dl)'. The slide says "Endcap field ~3x stronger than barrel", and the
    name now follows it.
16. MAT_IRON_MUON_CRITICAL_ENERGY: the explanation said the value was "quoted from memory", an unsupported characterisation. It now says
    "quoted on the slide (no reference given)".

### Acosta deck (near_beam_spectrometer_ws2026_acosta.yaml)
17. Toroid strawman:
    - The explanations of DET_FWD_SPECTROMETER_TOROID_RIN/ROUT/LENGTH/BIN and BDL_MIN/MAX, and the file header, asserted that the
      boxed numbers are the ATLAS endcap toroid's own figures.
    - Slide 11 says only "Explored using an (ATLAS) endcap toroidal magnet as a realistic strawman design" and prints the box beside an
      ATLAS picture. The text now says the slide does not state whether the numbers are as-built ATLAS values or model values.
    - Ten records from backup slides 26–27 (ideal-resolution formula, slope 1.6 %/m, intercept 1.7 %, 5 % and 25 %, the 0.25–1 TeV
      range, Z = 136 m, and two statements) were called 'ATLAS-magnet figures'. They are study results, and their explanations were
      rewritten.
18. PHYS_BHABHA_XSEC_FWD_ETA24_40 and _ETA40_56_IMPLIED: applicability changed from direct to analogous, since a 10 TeV μ+μ− quantity
    cannot be direct for the LHμC.
    - Notes were added on the slide's per-event-time slips. '0.5h/ev' is printed beside 0.35 mHz, but 1/0.35 mHz = 0.79 h. '1.3s' is
      printed beside 0.85 Hz, but 1/0.85 Hz = 1.18 s.
    - The three printed and two implied cross sections carry an independent LO cross-check in validation.notes (see the residual
      doubts). Their level is unchanged.
19. DET_FWD_SPECTROMETER_STATIONS_PER_TOROID: the slide's "2 detector stations in front and behind toroid" is ambiguous. The name now
    quotes the wording, a note gives both readings, and confidence was lowered to medium.
    - DET_HEX_CSC_HEIGHT_WIDTH: a note says √3·s = 1.73 m is only the flat-to-flat dimension; vertex-to-vertex is 2s = 2.0 m.
    - DET_FWD_SPECTROMETER_STATION2_Z_FIG: the title is truncated on the slide. The quotation is now verbatim ('… 750.( (150.0 um
      position res)').
    - DET_VBF_STUDY_BEAM_ENERGY_MUMU: a note says the plot is labelled 'MuIC Prospective' while the slide states 5 × 5 TeV μ+μ−.

### MAIA (maia_10tev_detector.yaml)
20. Changes to existing records:
    - DET_OVERALL_LENGTH_MAIA and DET_OVERALL_DIAMETER_MAIA: applicability changed from direct to analogous. Confidence changed from
      high to medium, because an analytical_estimate inherits the lowest confidence of its inputs (docs/scientific_scope.md §4).
    - DET_VXD_L1_BIB_HIT_DENSITY: the uncertainty note asserted "before timing cuts", which the sentence does not say. It was replaced
      by the Fig. 7 reading: ≈3×10^4 hits/cm² in [−0.5, 15] ns, ≈1.5×10^3 after the [−3σt, 5σt] selection.
    - Quotations were extended to cover the full value: DET_ECAL_VARIABLE_THRESHOLD_STATEMENT (central-region sentence) and
      DET_BIB_CLONING_METHOD (overlay sentence).
    - DET_ECAL_PHOTON_HIT_WINDOW_START: page changed from 24 to 25, where the numbers are printed. A note says '−0.5 ps' may be a slip
      for −0.5 ns.
    - DET_RESOLUTION_METRIC: a note gives the Fig. 19 axis label 'IQR68 / (2 * (1 + median))'.

### MUSIC (music_10tev_detector.yaml)
21. Changes to existing records:
    - DET_TRACK_PT_RESOLUTION_HIGH_PT: a note gives the Fig. 2 reading (≈1.6–2.8×10^-5 GeV⁻¹ in the central bins). It qualifies the
      stored order-of-magnitude 1e-5 against the printed 'a few 10^-5'.
    - DET_PHYSICS_ANALYSES_STATEMENT: subsystem changed from physics_programme to detector (DET_ id).

### Muon-ion collider paper (muic_acosta2022_delphes_card.yaml)
22. Version and attribution:
    - All 155 records: the version said "JINST 18 (2023) P09025 per the registry". The PDF says 'Prepared for submission to JINST',
      and the JINST reference is snippet-level. The version now says so.
    - PHYS_HBB_STUDY_MU_BEAM_ENERGY and _PROTON_BEAM_ENERGY: subsystem changed from machine/proton_beam to physics_programme (PHYS_ id).
23. Notes and quotations:
    - Table 16 (DET_T16_FWD_MUON_P_RESOLUTION_LINEAR_TERM, DET_T16_CHARGED_ANGULAR_RESOLUTION_P_TERM): the notes claimed p in GeV follows
      from the caption. It does not, and the GeV unit is now marked as assumed.
    - The 18 Table-18 records: the notes said "as printed". Table 18 prints no units, and the notes now say so.
    - The two Table-16 angular-resolution records: a note says the stored 0.02511 is the evaluation of the printed '0.087/√12'.
    - PHYS_DIS_KINEMATICS_MUON_ACCEPTANCE_STATEMENT: the quotation was extended to the hadronic-system sentence the value asserts.
    - PHYS_DIS_LOW_X_FORMULAS: a page note was added (Eqs. A.1–A.2 on p.39, A.3–A.4 on p.40).
    - DET_CENTRAL_ACCEPTANCE_ETA_MAX: the note asserted a correspondence with the 10° IMCC nozzle, which the paper does not state. It
      was softened.
    - DET_FAR_BWD_STATION2_ETA_MAX: the method text '4.38 ≈ 4.5' was made precise. The check confirms the coverage; the 4.5 edge itself
      corresponds to r ≈ 0.89 m.
    - Header typo fixed: 0.087/√12 = 0.02511, not 0.02512.

## Records added (13; quotable quantitative statements the extractor missed)
- **Forthomme:**
  - DET_FIG_HAC_BARREL_RADIAL_LABEL_LHEC_WS2026_FORTHOMME: 146 cm, slide-6 drawing.
  - DET_FIG_DIPOLE_LABEL_LHEC_WS2026_FORTHOMME: 'Dipole 966', 966 cm. Both are imported_related, manual_figure_read, medium, and the cm
    unit is inferred.
  - DET_ASTROPIX_PIXEL_SIZE_REF_WS2026_FORTHOMME: 500 µm ('500x500µm² pixel size', slide 19); analogous, screening_only.
- **Acosta:**
  - MACHINE_IMCC_MU_BUNCH_POPULATION_BIB_FIG_WS2026_ACOSTA: 2×10^12 per bunch ('N±μ~2x10^12/bunch', slide 9); analogous,
    screening_only.
  - DET_CSC_FIG_WIRE_SPACING_CMS_WS2026_ACOSTA (3.12 mm), DET_CSC_FIG_GAP_CMS_WS2026_ACOSTA (9.5 mm), and
    DET_CSC_FIG_STRIP_WIDTH_MIN/MAX_CMS_WS2026_ACOSTA (3 and 16 mm): labels of the CMS CSC drawing on slide 16; analogous,
    screening_only, attribution by this reading.
- **MAIA, §VII Conclusions on p.37** (analogous, medium, P0):
  - DET_TRACK_PT_RESOLUTION_BEST_CONCLUSION_MAIA ('approaching 1%').
  - DET_IMPACT_PARAMETER_RESOLUTION_BEST_CONCLUSION_MAIA ('approaching … 2 µm').
  - DET_PHOTON_RECO_EFF_CENTRAL_BARREL_MIN_CONCLUSION_MAIA ('surpass 95%').
  - DET_PHOTON_RESOLUTION_BEST_CONCLUSION_MAIA ('approaching 1%').
  - DET_PION_EFF_HIGH_E_CONCLUSION_MAIA ('approaching 95%').

  Each carries a note comparing it with the body text (see the residual doubts).

## Records removed
None. Every record is supported by its cited page; no invented, rounded or misattributed value was found beyond the corrections above.

## Residual doubts (for the lead / registry stage; network blocked, so nothing could be checked beyond the uploaded files)

### Forthomme
- The text says 8 forward tracker layers; the drawing (p.5) says '7 Fwd-Tracker Wheels'.
- Slide 18: 270 / 360 MCHF = 75 % vs the printed 71 %.
- p.2: the kinematic plot is at 70 GeV, the title at 1.2 TeV.
- ZDC '1015-1016' is printed without exponents.
- The cm unit of the slide-6 labels is inferred, and the attribution of '146' and 'Dipole 966' to components is this reading.
- The JINST ↔ arXiv:2203.06258 identity is unverified.

### Yamazaki
- '6-7 %' at 1 TeV is the speaker's assessment, not a measurement.
- The slide-11 legend percentages are unlabelled, and the CMS '-1%' entries are kept only as strings.

### Acosta
- Station 2 is at 140 m on slide 11 vs 'Z = 136.0 m' on backup slide 27. The station-3 edge 7.2 is not reproduced (7.14 at
  z = 660 m and R_in = 1.05 m).
- Q² < 10^5 has no printed unit (GeV² assumed).
- The wording 'stations in front and behind' is ambiguous.
- The stereo strips are 'rotated −15º' yet '30º between them'.
- The hexagon 'height, width' holds flat-to-flat only.
- The Geant4 slope of 2.54 %/m vs the ideal 1.6 %/m is not reconciled on the slides.
- Whether the toroid box values are the as-built ATLAS endcap-toroid dimensions cannot be checked without the ATLAS documentation.
- LO Bhabha cross-check: integrating the slide-6 formula at √s = 10 TeV gives the following, in pb:

  | abs(η) range | α = 1/137.036 | α = 1/128 | printed |
  |---|---|---|---|
  | < 2.4 | 0.298 | 0.341 | 0.35 |
  | < 2.0 | 0.127 | 0.146 | 0.14 |
  | < 1.5 | 0.042 | 0.048 | 0.043 |
  | 2.4–4.0 | 7.43 | 8.52 | 8.5 (implied) |
  | 4.0–5.6 | 183 | 210 | 200 (implied) |

  This is consistent within ≈15 %, but α, generator and cuts are not stated.

### MAIA
- The gun range starts at 8°, which is |η| 2.66, while the paper says |η| < 2.44 (10°).
- The fluence '10^14−15' carries no explicit period ("per year" is attached to the dose).
- 'roughly 1 ns' may refer to the ATLAS Tile rather than the MAIA HCAL.
- '−0.5 ps' is possibly −0.5 ns.
- The transition edge 1.01 is not reproduced from Table 1 (1.04 / 1.22 / 0.94 at the corners).
- '~4 X0' vs 3.0 X0 for the aluminium alone.
- The conclusions are more optimistic than the body: 2 µm vs ~5 µm; > 95 % vs 90–95 % over all η; 1 % vs < 2 %; 95 % 'across the
  detector' vs the barrel only.

### MUSIC
- The muon barrel reaches 680 cm (13.6 m diameter) vs the stated 12.8 m.
- The muon endcap reaches 11.8 m vs the stated 11.4 m length.
- 70 × 2 cm Fe = 8.3 λ_I vs 'approximately seven'.
- The HCAL '290.2 cm in radius' is not stated to be the inner or the outer radius.
- 'a few 10^-5' is stored as the order 1e-5.

### Muon-ion collider paper
- 'pions 100 % in the ECAL' is recorded verbatim (presumably π0).
- '3 %' statistical uncertainty vs √(S+B)/S = 4.7 %.
- r ≈ 3.5 m at z = 5 m does not reach η = −1.
- Tables 16 and 18 print no units.
- The registry's source_type journal_article for SRC_ARXIV_2203_06258 is not supported by the uploaded v3. That is a registry matter,
  which the verifier did not edit.

### Policy questions for the lead
- 13 reported_lhmuc records carry applicability design_variant: the Forthomme 100 mrad / η_max 3 option, the slide-10 acceptance
  options, and the 8 hexagonal-CSC idea records. The §3 table asks for 'direct', but lhmuc_dis2026*.yaml and
  helpcern_wp_working_points.yaml use the same convention for proponents' alternative options, so they were left unchanged.
- The 29 'low' confidences of item 2 are a verifier judgement in line with G4. The lead may harmonise the rule across groups.
- 154 MuIC records keep 'high'. They are imported_related with applicability analogous, a combination for which §4 has no mechanical
  cap, while comparable MAIA/MUSIC values are 'medium' because of their source category. This matches the letter of §4, but the
  lead may want a uniform treatment.

## Validation after the fixes
- `tools/validate_yaml.py provenance`: 0 schema errors in each of the six files.
- `python -m lhmuc validate`: 0 errors and 0 warnings in the six G5 files. The run's remaining 1502 errors are all confidence-cap errors
  in eight other groups' files, which were still being fixed by their own verifiers during this run:
  - imcc_mr7_proton_driver_target_cooling 418, imcc_mr7_collider_reference 357, imcc_mr7_magnets_rf_power_infrastructure 311
  - imcc_ws2026_schulte_parameters 251, lhc_long_bunch_options_ws2026_zimmermann 129
  - lhec_ir_ws2026_forthomme 21, lhmuc_ws2026_forthomme_beam_set 13, muic_acosta2022_machine 2
- `tools/apply_confidence_caps.py --check` on the six files: 0 records exceed a §4 cap.
- `pytest tests/unit tests/scientific`: 113 passed, 2 failed. test_no_validation_errors fails only on the other groups' files above.
  test_csv_registries_in_sync fails only because the registries are not rebuilt; the registry stage runs
  `uv run python tools/build_registries.py`.
