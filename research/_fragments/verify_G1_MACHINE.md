# Verification note — group G1_MACHINE (Phase 0 addendum, 2026-10-29)

Role: adversarial verifier. Files verified (all written by the G1_MACHINE extraction of 2026-10-28):

- `parameters/machine/lhmuc_ws2026_forthomme_beam_set.yaml` (18 records; 18 after verification)
- `parameters/interaction_region/lhec_ir_ws2026_forthomme.yaml` (23 → 25)
- `parameters/proton_beam/lhc_long_bunch_options_ws2026_zimmermann.yaml` (128 → 130)
- `parameters/machine/muic_acosta2022_machine.yaml` (83 → 87)
- `parameters/machine/scenarios_addendum_machine.yaml` (13 scenarios; role links and notes corrected)

Sources: SRC_WS1681458_FORTHOMME_DETECTOR (pp. 2-4, 10, 15-17), SRC_WS1681458_ZIMMERMANN_SPS_LHC (all 14 slides),
SRC_ARXIV_2203_06258 (PDF pp. 1, 3, 5-12, 20, 30). Method: every record was compared with the cited page — text layer for prose,
page images (200-300 dpi crops) for every table cell, figure legend, drawing label and equation; the three Zimmermann tables, the
two Acosta tables and the Forthomme p.4 histogram/drawing/maps and p.10 legend were transcribed cell by cell from the images. All
derivations and P1 checks were recomputed independently (scripts in the verifier's scratchpad: `verify_g1/qcheck2.py` quotation/page
locator, `verify_g1/apply_fixes*.py` edits). Record count after verification: 260 (252 + 8 added, 0 removed).

## What was checked and found correct

- **All numeric values and units** of the 252 records match the cited page: Forthomme p.17 (300 ns, 40 bunches, 1e10 μ⁺, 4.3 µm,
  7 cm, 1e34, 3e13 /s, 50 %), p.4 (15/23 m, 94.69/44.57 keV, 0/2/10 cm Pb), p.16 (7 TeV, < 150 MW, 1e34, 100 fb⁻¹/yr, 1 ab⁻¹,
  0.1, ≪ 1e14, 20 MV/m, 2 linacs, 3 arcs, 1/4); LHC Project Report 627 Table 1 (all 32 cells + caption), QCD Explorer Table 1 (all
  cells + Fig. 1 labels), Damerau-Garoby Tables 1-2 and hardware text, CERN-2005-006 Table 3, SPS/AGS/KEK/PRST-AB excerpts;
  Acosta et al. Table 1 (PDF p.5) and Table 2 (PDF p.8, all cells of the four columns), eqs. (2.1)-(2.2), 300B rule, 12-15 Hz,
  28 wk × 0.5 × 10 yr, 2-4 MW / 4-8 GeV, 20 %/50 %, θ ≲ 1°, 10 years (IMCC).
- **Statuses**: reported_lhmuc only for LHμC statements on PRIMARY_LHMUC decks (Forthomme p.17, Zimmermann p.2 request and p.14
  conclusions); everything restated from LHeC / LHC studies is imported_related; AGS, KEK super-bunch concept, EIC context analogous;
  MuIC paper values imported_related; derived values derived_lhmuc / analytical_estimate with derivations naming input ids;
  unknowns have value null. No status change was needed.
- **Arithmetic re-done**: implied N_p = 1e34 × 4π(4.3 µm)² / ((1/300 ns) × 1e10) = 6.971e11 (H = 1); 40 × 300 ns = 12 µs;
  σ(ε_n = 2.0 µm, β* = 7 cm, 7 TeV) = 4.33 µm; 94.69/44.57 = 2.12; Report 627 luminosities 0.990e34 / 2.34e34 / 7.22e34 from the
  column entries (f_rev = 11245 Hz, Gaussian crossing factor); QCD Explorer spot sizes 11.15/11.21 µm and electron line density
  2.02e10 /m; Damerau-Garoby emittance chain 0.8 × 1.25 × 1.1 × 8 × 1.4 × 1.05 × 2 × 1.1 = 28.46 eVs; 5 × 300 kV; 26.66 km / 3564 =
  7.48 m; c / 40 MHz = 7.49 m; 6.0 ms / 2048 = 2.93 µs; Acosta √s (0.332/0.742/1.028/6.481/1.92 TeV), luminosities
  (7.05e31/2.13e33/4.69e33/2.75e33), integrated luminosities (5.9/177.8/398/237.1 fb⁻¹), σ_p = 7.15/7.09 µm, σ_μ(LHmuC) = 2.97 µm,
  0.3 × 11 T × 290 m = 957 GeV/c, 3300 × 0.5/0.96 = 1719, 12 × 3300 = 39600 Hz. All agree with the extractor except where listed below.
- Canonical ids of this group exist with the stated values: MACHINE_MU_BUNCH_SPACING_WS2026_FORTHOMME (300 ns),
  MACHINE_MU_BUNCHES_WS2026_FORTHOMME (40), MACHINE_MU_BUNCH_POPULATION_WS2026_FORTHOMME (1e10), IR_SIGMA_XY_IP_WS2026_FORTHOMME
  (4.3 um), PROTON_BETA_STAR_WS2026_FORTHOMME (7 cm), MACHINE_PEAK_LUMINOSITY_WS2026_FORTHOMME (1e34),
  SOURCE_MU_RATE_INTO_BOOSTER_WS2026_FORTHOMME (3e13 /s), MACHINE_MUON_POLARISATION_WS2026_FORTHOMME (0.5),
  PROTON_BUNCH_POPULATION_IMPLIED_WS2026_FORTHOMME (6.97e11, derived_lhmuc, P1), IR_LSTAR_LHEC_WS2026_FORTHOMME (15 m),
  IR_LSTAR_FCCEH_WS2026_FORTHOMME (23 m). No id was renamed.

## Corrections made

### Acosta et al. (muic_acosta2022_machine.yaml)
1. **Page numbers (75 records)**: the extractor mixed printed page numbers (most records) with PDF page numbers (Table 1, the two
   section-2.1 LHmuC statements, the staging statement). All records now cite the PDF page, as the other two SRC_ARXIV_2203_06258
   files do (convention added to `source.version` and the file header): Table 2 7 → 8; eqs. 2.1-2.2, 300B, H = 1, parameter origins
   6 → 7; 10-bunch split, 25 mrad, 28 wk / 0.5 / 10 yr 7 → 8; B = 11 T 4 → 5; r = 290 m 5 → 6; IP2 and proton driver 8 → 9;
   polarisation and ring tilt 10 → 11; IMCC 10 years 11 → 12. Each page was confirmed by locating the quotation in the PDF text layer.
2. **MACHINE_LHMUC_MUON_SOURCE_CONCEPT_MUIC2022**: quotation not verbatim ("If we assume a 3 TeV ...") → "If we assume **that** a 3 TeV ...".
3. **MACHINE_MU_CYCLES_PER_TESLA_MUIC2022**: arithmetic error in the independent check: 0.3 B c τ_μ/(2π m_μ) = **297.6 B/T** (297.4 with
   0.2998), not 299.6 B/T. Conclusion ("about 300B" to 1 %) unchanged.
4. **PROTON_BUNCH_POPULATION_LHMUC_MUIC2022** notes: PROTON_BUNCH_POPULATION_MULHC was quoted as 22e11; it is **2.2e11** (the 22e11
   is PROTON_BUNCH_POPULATION_DIS2026).
5. **MACHINE_MU_BUNCH_TRAIN_SPLIT_MUIC2022** notes: "two orders smaller per train" was wrong; LHμC trains (4e11-5.6e11 μ⁺) are 3.6-5 ×
   below the 2e12 per MuIC/LHmuC cycle; per bunch 20-30 × below the split (2e11) and 200-290 × below the unsplit bunch.
6. **IR_BETA_STAR_MUON_MUIC074_MUIC2022** and **IR_SIGMA_XY_IP_MUON_LHMUC_MUIC2022**: cell transcriptions "1.0" / "3.0" → "1" / "3" as printed.
7. Notes citing pages corrected to PDF pages (MACHINE_LUMINOSITY_FORMULA p.6 → 7, IR_CROSSING_ANGLE_EIC_DESIGN p.7 → 8,
   MACHINE_PEAK_LUMINOSITY_MUIC100 p.7 → 8); cross-page quotations flagged (B = 11 T: pp. 5-6; proton-parameter origin: pp. 7-8).
8. Beam-size audit note of the three MuIC muon columns reworded (eq. 2.2 gives 59.9/7.3/4.5 µm vs table 48/7.6/4.7 µm = +25/−4/−3 %;
   the extractor's sign convention was ambiguous); scenario MUIC-ACOSTA2022-BNL-960GEV note −4 % → −3 %.
9. **1134 cycles (0.1 TeV column)**: observation added to MACHINE_MU_CYCLES_PER_BUNCH_MUIC033, MACHINE_MU_CYCLES_PER_TESLA and the
   BNL-100GEV scenario: 3300 × 0.33/0.96 = 1134.4, i.e. the γ-scaling evaluated with the column's √s instead of its muon energy — a
   probable slip in the paper (not asserted; the luminosity cell is reproduced with the printed 1134).

### Forthomme beam set (lhmuc_ws2026_forthomme_beam_set.yaml)
10. **MACHINE_MU_BUNCH_POPULATION_WS2026_FORTHOMME** notes: "10 x below the μLHC/μTRISTAN 1e11 (SOURCE_MU_BUNCH_POPULATION_MULHC)" was
    false (that record is 4.5e10; no 1e11 exists). Replaced by the correct comparators (μLHC 3.0e10 / 3.7e10, booster injection 4.5e10,
    μTRISTAN μ⁺e⁻ 1.4e10).
11. "Fourth LHμC beam-parameter set" removed from 7 applicability texts, the file header and the scenario description (the ordinal is
    not supported: DIS2026 has two sets and μLHC two).
12. Quotation apostrophe "HL-LHC's" → "HL-LHC’s" as printed (4 records).
13. **MACHINE_MU_BEAM_ENERGY_WS2026_FORTHOMME** (kept null): explanation/notes now state that the same deck's kinematic-plane plot (p.10)
    is labelled "LHμC (1 TeV× 7 TeV, ...)" (detector-group records) but slide 17 does not tie its beam set to it.
14. MACHINE_MU_TRAIN_DURATION_IMPLIED: definition clarified (40 slots × 300 ns; first-to-last bunch 11.7 µs).
15. PROTON_OPTICS_ASSUMPTION and IR_IP_LOCATION: note on the reading of "stand-alone, i.e. collisions at IP2 only" (dedicated running
    without pp collisions elsewhere; contrast the concurrent operation claimed by Acosta et al.).

### LHeC IR / baseline facts (lhec_ir_ws2026_forthomme.yaml)
16. Applicability of all 23 records: "original source: the LHeC design, CDR 2020 / HL-LHC baseline" was an unverified attribution (the
    slides cite nothing). p.4 records now name the slide as an uncited BDSIM IR study (method and published L* = 15 m IR in André et al.
    2022, SRC_ARXIV_2201_02436); p.16 records say the slide cites no source.
17. **IR_LSTAR_FCCEH_WS2026_FORTHOMME**: quotation contained a paraphrase ("IR layout drawing annotation: ... (on both sides of the IP)");
    now verbatim ("... | L* = 23 m") with the drawing reference moved to table_figure_or_equation.
18. **IR_SR_CRITICAL_ENERGY_LSTAR15/23**: names no longer expand 'COL_END_0' into "IR collimator end" (not stated); quotations are the
    legend entries as printed ("L* = 15 m | ϵc = 94.69 keV"), figure reference completed.
19. **IR_LAYOUT_ELEMENT_LABELS**: the grouping "proton side: Q0F, Q0D, TAS, Q1A; electron side: QY, QX, BEND_0" was an interpretation
    (QY/QX appear on both sides of the IP); replaced by a positional description of the drawing.
20. **MACHINE_INTEGRATED_LUMINOSITY_TOTAL_LHEC_WS2026_FORTHOMME**: P1 → **P0** (nothing is reproduced: the exploitation duration is not
    stated; 1 ab⁻¹ / 100 fb⁻¹ yr⁻¹ = 10 yr is an inference). The per-year value keeps P1 (convention-based 1e7 s check, method named).
21. IR_LSTAR_LHEC notes: L* = 15 m is also the published LHeC IR value (IR_LSTAR_ANDRE2022). INFRA_POWER_CONSUMPTION_LIMIT notes: "no
    power figure exists for LHμC" sharpened (only proton-driver/target beam powers exist; Rogers' wall-plug power is an explicit unknown).

### Zimmermann (lhc_long_bunch_options_ws2026_zimmermann.yaml)
22. Applicability of the AGS (2), SPS (4) and KEK super-bunch (2) records said "an LHC(-upgrade) value"; corrected to BNL AGS measurement /
    SPS observation / KEK concept-paper claim.
23. PROTON_BUNCH_NUMBER_FRACTION_REQUESTED: "1 % of 2808 bunches" now says 2808 is the nominal LHC number from slide 9 (the slide does not
    give "today's" number).
24. PROTON_QCDX_SUPERBUNCH_FIGURE_LENGTH: Figure-1 quotation missed a comma ("2808 proton bunches, spaced by 25 ns"); attribution caveat
    added (slide 10 shows the PAC 2003 header above the EPAC 2004 paper; Figure 1 and the "Colliding 7-TeV ..." sentence are not
    explicitly assigned) — also on MACHINE_QCDX_CONCEPT.
25. **MACHINE_QCDX_LUMINOSITY_WS2026_ZIMMERMANN**: P0 → **P1**. Reproduced from Table 1 cells: short electron bunches crossing the proton
    super-bunch over l_IR with hourglass, L = f_coll n_b N_e λ_p · 4β* arctan(l_IR/2β*)/(4πσ*²) = 1.13e31 (σ* = 11 µm) / 1.09e31
    (11.2 µm) vs 1.1e31 (dependencies added). The paper's own formula is not on the slide (stated in validation.notes).
26. **PROTON_QCDX_SUPERBUNCH_LINE_DENSITY**: the table's 2.1e12 /m is reproduced exactly by N/(√(2π)σ_z) = 2.09e12 /m (the extractor's
    6.5e13/30 m = 2.17e12 is 3 % off). The "12.4 m rms (uniform)" vs "30 m long" puzzle becomes consistent if 12.4 m is the
    Gaussian-equivalent σ of a flat bunch of effective length √(2π) × 12.4 = 31 m (recorded as an observation in the rms-length and
    line-density records and the QCD-EXPLORER-EPAC2004 scenario notes; both values kept as read).
27. PROTON_LHC_PR627_LUMINOSITY_UPGRADE_SUPERBUNCH (stays P0): independent flat-bunch large-Piwinski estimate added (6.71e34 vs 9.0e34;
    Gaussian 6.56e34), confirming the extractor's "not reproduced".
28. PROTON_BUNCH_MERGING_SCALING_RELATION (stays P1): Damerau-Garoby check added (28.5 eVs vs 2 × 16 × 0.8-1.0 eVs, ratio 1.8-2.2 per
    merged bunch); caveat that the Report 627 check assumes n_b,0 = 2808 merged bunches although the super-bunch carries 1.0 A vs 0.56 A
    (with n_b,0 ≈ 5000 the ratio would be 0.51).
29. PROTON_LHC_LONGBUNCH_LAMBDA2_INTEGRAL_N2: cell transcription "0.7" → "0.70" as printed.

### Scenarios (scenarios_addendum_machine.yaml)
30. LHMUC-WS2026-FORTHOMME: "nozzle_opening_angle" was listed as unknown although the same deck (p.9) gives the LHμC nozzle half-opening
    angle; now linked to the canonical detector ids (`nozzle_half_opening_angle: DET_NOZZLE_HALF_OPENING_ANGLE_WS2026_FORTHOMME`,
    `nozzle_half_opening_angle_alternative: DET_NOZZLE_HALF_OPENING_ANGLE_OPTION2_WS2026_FORTHOMME`); description/notes corrected.
31. LHEC-WS2026-FORTHOMME: the extractor's note "the electron beam energy ... is on slides 2-3" was wrong (slide 2 gives the ep √s of
    1.2 TeV; the 50 GeV is in the p.10 legend). Roles added: `electron_beam_energy`, `electron_beam_energy_alice3_option` (new records),
    `sqrt_s: MACHINE_SQRT_S_LHEC_WS2026_FORTHOMME`, `solenoid_field_delphes_model: DET_SOLENOID_FIELD_LHEC_DELPHES_WS2026_FORTHOMME`;
    `electron_beam_energy`, `sqrt_s`, `solenoid_field`, `detector_dimensions` removed from unknown_roles (LHeD 13 m × 9 m are recorded by
    the detector group as DET_LHED_LENGTH/DIAMETER_WS2026_FORTHOMME, named in the notes); notes rewritten (P1 basis stated).
32. QCD-EXPLORER-EPAC2004 notes (luminosity now reproduced; line-density and 12.4 m / 30 m observation); LHC-DAMERAU-GAROBY-LONGBUNCH-EPAC2004
    gains `collision_mode_rf`; MUIC-ACOSTA2022-BNL-960GEV gains `tunnel_straight_sections`; BNL-100GEV note gains the 1134 observation.

## Records added (quotable statements the extractor missed)

- MACHINE_ELECTRON_BEAM_ENERGY_LHEC_WS2026_FORTHOMME — 50 GeV, Forthomme p.10 legend "LHeC (50 GeV× 7 TeV, -4.5 <η< 5.1)", imported_related,
  P1 (2√(50 GeV × 7 TeV) = 1.18 TeV reproduces the 1.2 TeV of p.2).
- MACHINE_ELECTRON_BEAM_ENERGY_ALICE3_OPTION_LHEC_WS2026_FORTHOMME — 20 GeV, p.10 legend "LHeC (20 GeV× 7 TeV, ALICE3 accept.)", P0.
- PROTON_LHC_LONGBUNCH_COLLISION_MODE_RF_WS2026_ZIMMERMANN — "0.8/0.8/0.4 MV at 40/80/120 MHz" (Damerau-Garoby Table 2; the scenario
  description already quoted it without a record).
- PROTON_LHC_PR627_HYBRID_CROSSING_SCHEME_WS2026_ZIMMERMANN — Report 627 abstract on slide 9 (alternating H/V crossing vs inclined
  hybrid collisions at 45° and 135°).
- MACHINE_MUIC_TUNNEL_STRAIGHT_SECTIONS_MUIC2022 — 6 (PDF p.9).
- MACHINE_MUIC_LUMINOSITY_CONTEXT_STATEMENT_MUIC2022 — "1.0 TeV and luminosity of 10^33–10^34 ... comparable to ... LHeC ... 1.2 TeV ...
  50 GeV" (PDF p.6; the 1e34 upper end is not backed by Table 2, noted).
- MACHINE_PEAK_LUMINOSITY_LESS_STRINGENT_EXAMPLE_MUIC2022 — ≈1e32 cm⁻² s⁻¹ "operating for several years" (PDF p.8).
- MACHINE_EIC_LUMINOSITY_CONTEXT_MUIC2022 — EIC 1.5 fb⁻¹/month at ≈1e33, 10 fb⁻¹ ≈ 30 weeks (PDF p.8; analogous, categorical).

## Removed

None. Every record at hand-over is supported by the cited page; no value was found fabricated, rounded beyond the printed precision or
attributed to the wrong column/table.

## Residual doubts (not resolvable from the uploaded documents; network blocked)

- Forthomme p.17: whether "peak" is the in-train rate and whether the 40 bunches circulate together (the implied N_p ≈ 7.0e11 rests on
  H = 1 and f = 1/300 ns); the muon/proton energies of the set (p.10 plots 1 × 7 TeV, p.17 is silent); the crossing-angle value; the
  exact meaning of "stand-alone, i.e. collisions at IP2 only".
- Forthomme p.4: which L* option is the LHeC baseline (the published 2022 IR uses 15 m); what 'COL_END_0' is; the electron energy and
  lattice behind ε_c = 94.69/44.57 keV, which are far below the 256-360 keV axis range of André et al. 2022 Fig. 19 (different element/
  configuration, not comparable as read); the referent of the "0.3 m" bar; the IR_LSTAR_FCCEH id token is the lead's label, not a slide fact.
- Zimmermann: Report 627 super-bunch luminosity 9.0e34 and the IBS growth times (report's formulas not on the slide); QCD Explorer
  beam-beam tune shift 0.004 (a simple estimate gives ≈ 2.7e-3); definition of the Damerau-Garoby "luminosity gain" (∫λ² ratio fails
  for n = 2); population and length of the merged long bunch (only the 4-5 m class of CERN-2005-006 Table 3); the "super-bunches" vs
  "superbunches" hyphenation in the PRL abstract (line-break hyphen, cannot be decided from the slide).
- Acosta et al.: the LHmuC storage-ring field (3300 = 300 × 11 T only if the MuIC 11 T is assumed); whether Table 2's 20e11 μ bunch or
  the proposed train of 10 is meant; the three MuIC muon beam sizes (48/7.6/4.7 µm) do not follow eq. 2.2; 1134 cycles (see item 9).
- Cross-file links: the LHMUC and LHEC scenarios now reference detector-group records (canonical DET_NOZZLE_HALF_OPENING_ANGLE*_WS2026_FORTHOMME
  and DET_SOLENOID_FIELD_LHEC_DELPHES_WS2026_FORTHOMME, plus MACHINE_SQRT_S_LHEC_WS2026_FORTHOMME); the lead's registry stage should keep
  those ids stable.

## Validation after verification

- `uv run python tools/validate_yaml.py provenance <file>`: 0 schema errors for the four parameter files; `machine` schema: 0 errors for
  the scenario file; all 260 units parse; every id referenced in the five files exists.
- `uv run python -m lhmuc validate`: 0 errors, 0 warnings (repository-wide, other groups' files present).
- `uv run pytest` (all tests except `test_csv_registries_in_sync`): pass. `test_csv_registries_in_sync` fails only because
  `registries/parameter_registry.csv` must be regenerated (`uv run python tools/build_registries.py`), which belongs to the lead's
  registry stage.
