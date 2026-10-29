# Verification note — group G6_PHYSICS (Phase 0 addendum, 2026-10-29)

Role: adversarial verifier. Files verified (written by the G6_PHYSICS extraction of 2026-10-28 and its own resume review of
2026-10-29):

- `parameters/physics_programme/smallx_ws2026_heqcd.yaml` (86 records → 87; 1 added)
- `parameters/physics_programme/muic_acosta2022_cross_sections.yaml` (376 → 376)
- `parameters/physics_programme/mutristan2022_physics.yaml` (65 → 65)
- `parameters/physics_programme/imcc_ws2026_schulte_physics_and_dudko_formula.yaml` (48 → 48)

Total: 575 records checked, 576 after verification. Nothing was removed and no id was renamed. No value, unit, page, quotation or
provenance status had to be changed. The corrections are to explanations, names, notes and section strings that carried
unsupported or wrong statements, one validation label, and the confidence caps that the validator now enforces.

Sources and pages read:

- **SRC_WS1681458_HEQCD_SMALLX:** all 28 slides as images. Slides 13, 14, 16 and 17 were also rendered at 300 dpi and measured in
  pixels.
- **SRC_ARXIV_2203_06258:** PDF pp. 4–8, 13–37 and the reference list on p. 45. Tables 3–15 were rendered at 300/400 dpi; Fig. 5
  was rendered at 400 dpi.
- **SRC_ARXIV_2201_06664:** PDF pp. 2–4 and 9–20.
- **SRC_WS1681458_SCHULTE_IMCC:** slides 1–7, 10, 11, 28 and 38.
- **SRC_ARXIV_2607_16904:** p. 14.

Method:

- **Quotations.** Every quotation was located on its cited page, first with a segment-wise checker on the per-page text layer, then
  by eye on the page image wherever the layout scrambles the text: displaced √ signs, rotated figure labels, handwritten slide
  annotations, displayed equations, and sentences running across a page break.
- **Table cells.** All 250 table cells of Tables 3–15 of arXiv:2203.06258 were transcribed a second time, independently, from the
  images. They were compared programmatically with value, cell string, scale up/down, PDF⊕αs up/down and the `relative_fraction`
  encoding. There was no discrepancy and no missing or duplicate cell; the cell set is complete.
- **Arithmetic.** Every P1 arithmetic and every derivation was recomputed.
- **Identifiers.** Every scenario id, dependency id and parameter id mentioned in notes or explanations was resolved against the
  registry.
- **Tooling.** The edits were made by scripts that start from a byte-exact backup and re-dump with the generator's YAML settings,
  so only the edited fields change. The verifier's scratchpad `verify_g6/` holds `patch_*.py`, `log_*.json` and `muic_truth_v.py`
  (the independent table transcription).

## What was checked and found correct

### AGH deck: values and quotations

- The p.5 BFKL λ ≂ 0.5 is correct.
- The p.7 GBW formula and handwritten annotations are correct: Q0 ~ 1 GeV, x0 ~ 10^-4, η ~ 0.3, A^(1/3). So is the statement
  "Saturation is stronger in nuclei."
- The p.9 kT-factorisation condition is correct.
- The p.13 records are correct:
  - the x_Bj ≲ 10^-7 bound at Q² ~ 1 "GeV" (typo kept and noted), with 4 × 10^-3 < y < 1;
  - the "order of magnitude improvement" statement and the FCC-eh statement;
  - the legend, read at 300 dpi: LHeC 50 / 20 GeV × 7 TeV, LHμC 1 / 0.5 TeV × 7 TeV, EIC **21** GeV × 250 GeV, and the datasets;
  - the region labels and the axis ranges.
- The p.14 records are correct (Q = 1.64 / 100 GeV, NNPDF31sx), and so are the p.15 and p.16 records (Q² = 5 / 100 GeV², the
  ≪ 10^-7 statement).
- The p.18 records are correct: Q² = 5 / 25 GeV², x range 1e-7–1e-2, curve names, framework sentences, and the figure-read F2
  values in the notes (re-checked by eye).
- The p.19 statements are correct.
- The p.20 records are correct: √s = 3742 GeV, the cuts, the lowest populated bins at ≈ 9e-8 (x_Bj) and ≈ 1.6e-5 (x_g), checked in
  pixels.
- The p.21 records are correct: √s = 5.3 / 3.3 TeV, "up to 30%", and the R_Pb-p end points in the notes.
- The p.22 EIC comparison is correct: √S = 90 GeV, pT > 3 / 3.8 GeV, and the lab vs starred rapidity windows.
- The p.23 trijet settings, the p.24 summary and the p.27 backup are correct.

### AGH deck: statuses, arithmetic and references

- Statuses are correct. Model inputs and published figures are analogous, the LHeC legend energies are imported_related, and the
  LHμC-specific statements and plot settings are reported_lhmuc.
- The P1 arithmetic agrees:
  - x_min = Q²/(y s) gives 3.6e-8 (1 TeV) and 7.1e-8 (0.5 TeV);
  - the s ratios are 10 and 20 against LHeC, and 2.8 and 1.4 against FCC-eh (50 GeV × 50 TeV);
  - 2√(0.5 TeV × 7 TeV) = 3741.7 GeV and 2√(1 TeV × 7 TeV) = 5291.5 GeV;
  - the 3.3 TeV interpretation, 2√(1000 × 7000 × 82/208) = 3322 GeV, is kept in notes only.
- The scenario ids LHMUC-DIS2026-1TEV and LHMUC-WP-OPT1-500GEV exist, with E_μ = 1.0 TeV and 500 GeV respectively.
- The cross-referenced DIS2026 and MUIC2022 ids exist.

### MuIC paper: values and quotations

- All 123 text records match their page. Typical layout artefacts that are not errors: √ printed on a separate line, and sentences
  starting at the foot of one PDF page and continuing on the next. The notes already say this for PHYS_PP_EQUIVALENCE_FACTOR_*,
  PHYS_Q2_REACH_*, PHYS_HIGGS_BB_YIELD_FACTOR_MUIC2, PHYS_HBB_SEL_JET_* and PHYS_LHEC_FLAVOUR_TAG_EFF_HBB.
- The Fig. 5 legend matches the 400-dpi rendering, including HERA e⁻ (27.6) and LHmuC μ⁻ (1500) + A (2750).
- The PDF-page references in notes and explanations are now consistent. Examples: p.23 for the MadGraph statement, p.27 for
  PDF4LHC15, p.28 for the scale prescription, p.29 for "only LO diagrams".
- All 250 table cells agree with the independent transcription, including the asymmetric PDF⊕αs cells:
  - Table 7, 1.5 × 50, pTℓ > 2 GeV: 10.1 +1.1 %/−1.0 %;
  - Table 9, 1.5 × 50, pTℓ > 5 GeV: 50.3 +1.2 %/−1.1 %;
  - the trailing-zero strings (0.060, 0.020, 0.30, 0.0090, 0.20, 1.80, 7.00, 25.0, 47.0, 40.0, 75.0, 0.0220, 0.0190, 45.0, 12.0 and
    the others).

### MuIC paper: arithmetic and statuses

- The recomputed arithmetic agrees:
  - CC + NC + tH = total for all 16 polarisation columns of Tables 12–13 (agreement better than 0.05 %);
  - 19.4 pb = 1.80 + 8.93 + 8.69;
  - 2.1e4 W → ℓν = 19.4 pb × 10 fb⁻¹ × 0.108;
  - 229.6 / 19.4 = 11.8;
  - 17 800 = 76.7 fb × 400 fb⁻¹ × 0.58;
  - (235 + 47.9)/(64.5 + 11.6) = 3.72, and the factor-13 ratio = 12.96;
  - 30 440, 113 160 and 394 368 implied Higgs events, and 231 400 implied H → bb̄;
  - 1909 ττ and 2490 gg;
  - 130/76.7 = 1.69 and 1664/500 = 3.3;
  - 197^(1/3) = 5.82;
  - 2√(18 × 275) = 140.7 GeV, 2√(50 × 7000) = 1.18 TeV and 2√(100 × 275) = 332 GeV;
  - 65 GeV gives 84 % of HERA;
  - 6.5 / 3.16 = 2.06 and 6.5 / 1.5 = 4.33;
  - 2.1e33 × 28 wk × 0.5 = 17.8 fb⁻¹/yr;
  - 200/68 = 2.9 and 160/37 = 4.3;
  - s ratios of 3.5 and 11.4.
- Table 2 (p.8) confirms 178 / 400 / 237 fb⁻¹ per 10 years, which several derivations use.
- Statuses are correct. HERA and EIC comparators, refs. [20, 21, 38, 60, 64] and the SM branching ratios are analogous. MuIC,
  MuIC2, LHmuC and LHeC/FCC-eh values are imported_related. The three implied yields are analytical_estimate with derivations that
  name their input ids.

### μTRISTAN paper

- All 65 records match pp. 2–20 (printed page = PDF page):
  - √s 346 GeV, 2 TeV, 775 GeV and 6 TeV;
  - 1 ab⁻¹ with 70 % duty and one detector; 100 and 12 fb⁻¹/yr;
  - eqs. (8)–(16): 91 / 4 fb, 9.5e4, 3.1e-3, 5.5e4, 472 / 20 fb, 4.9e5, 1.3e-3, 8.9e-2 fb and 89 events;
  - the ILC 15 / 40 / 95 / 90 / 80 % comparators;
  - 54 fb and the "factor of ten";
  - γ = 3.0 / 3.9, θ ~ 5–10°, and the Fig. 4 caption values 316 GeV / 10° and 500 GeV / 7.5°;
  - LHCb θ > 15 mrad, the 90 % acceptance, O(100) events/yr, LHC sleptons 700 / 100 GeV, the factor 4 for sneutrinos, 5 TeV
    gauginos, "less than about TeV", and the summary statements.
- The recomputed arithmetic agrees:
  - 346.4, 774.6, 2 TeV and 6 TeV;
  - 1.02 ab⁻¹, 102 and 12.6 fb⁻¹/yr;
  - 95 000 and 492 000 events;
  - 3.07e-3 and 1.35e-3;
  - 89 events;
  - 0.22 = 1.3e-3/0.006;
  - γ = 2.97 and 3.94;
  - (1.25/1.8) gives a 31 % decrease, and (1.8/1.25)² = 2.07.
- The external dependencies resolve with the stated values: MACHINE_PEAK_LUMINOSITY_MUE / _MUMU_MUTRISTAN2022 = 4.6e33 / 5.7e32,
  MACHINE_MUON_POLARISATION_MUTRISTAN2022 = 0.8 and SOURCE_MUON_POLARISATION_WORST_CASE_MUTRISTAN2022 = 0.25.

### IMCC deck and Dudko review

- Schulte p.3 is correct: 10 TeV / 10 ab⁻¹, and "maybe" 3 TeV / 1 ab⁻¹ by around 2050.
- p.5 is correct: the NAS quotations, 100 TeV, and "Private thought: WIMPS > 200 GeV?".
- p.6 is correct: the scaling formula and the μp-advantage line, with the footer "GGI, June/July 2025".
- p.10 is correct: 40 000 muons/m/bunch crossing, 1/3 of the energy in e±, and MUSIC/MAIA ("Aperatus" as printed).
- p.11 is correct: the conclusions and the IP & nozzle callout "several order of magnitude".
- p.28 is correct: all 24 Key-Parameters cells (√s, L/IP, Int L, accumulation time for six columns), "two IPs" and the ramp-up
  5 / 25 / 70 %.
- p.38 is correct: "Int L | Ab-1 | 2.2 | 1.8" as printed. The note that it equals p.7 "N | 10^12 | 2.2 | 1.8" was confirmed on the
  p.7 image.
- Dudko p.14 is correct: eqs. (2) and (3), cτ_μ = 659 m, ≈ 297 B̄ and ≈ 149 B̄ turns. The cited test
  `tests/scientific/test_workshop_decks.py::test_turns_per_lifetime_dudko_formula` exists.

### Canonical ids

None of the CANONICAL IDS of the brief belongs to this group. The only canonical id that G6 records depend on,
MACHINE_MUON_POLARISATION_MUTRISTAN2022, exists with the value 0.8.

## Corrections made

### smallx_ws2026_heqcd.yaml

1. **PHYS_SMALLX_GLUON_PLOT_COLLIDER_MARKERS_WS2026_HEQCD (explanation).** The marker positions were re-measured in pixels on a
   300-dpi rendering: line centres against the major ticks, 146.7 px per decade, ±0.03 decade.
   - LHμC is drawn at 2.9e-7 (the draft said 3e-7, which is fine).
   - FCC-eh is at 7.0e-7 (was 8e-7).
   - LHeC is at 5.7e-6 (was 7e-6).
   - **HERA is at 1.9e-4 (was 3e-4, 0.21 decade off).**
   - **EIC is at 7.0e-4 (was 1e-3, 0.16 decade off).**

   The draft claimed ±0.1 decade; two values were outside it.
2. **PHYS_SMALLX_F2FL_PLOT_COLLIDER_MARKERS_WS2026_HEQCD (explanation).** LHeC is drawn at 8.5e-7, not 1e-6. LHμC at 1.0e-8 was
   confirmed. The method is now stated.
3. **PHYS_COVERAGE_PLOT_LHEC_E_ENERGY_50_WS2026_HEQCD (explanation).** "LHeC CDR energies" was removed. The slide cites no LHeC
   document, and the 2012 CDR baseline was 60 GeV.
4. **PHYS_DIJET_SAT_YLAB_MAX_FORWARD_WS2026_HEQCD (name and notes) and PHYS_TRIJET_SAT_YLAB_MAX_WS2026_HEQCD (notes).** Two
   unsupported interpretations were removed:
   - "'forward' selection" in the name;
   - "y_lab < 0, i.e. the muon-going hemisphere" in the notes.

   The deck states neither its rapidity sign convention nor which panel its "forward vs central" bullet refers to. The id is
   unchanged.
5. **Seven trijet records from p.23 (explanation).** These are PHYS_TRIJET_SAT_STATEMENT, _PROCESS, _YLAB_MIN, _YLAB_MAX,
   _PT_BREIT_MIN, _Q2_MIN and _OBSERVABLES_WS2026_HEQCD. Each said "deck's own dijet saturation prediction"; this now reads
   "trijet".
6. **PHYS_DIJET_KT_FACTORISATION_VALIDITY_WS2026_HEQCD (explanation).** The text said "pp. 20–23 (jet pT cuts of 5 GeV)". It now
   reads "pp. 20, 21 and 23". p.22 is the EIC comparison, with 3 and 3.8 GeV cuts.
7. **PHYS_WW_TMD_SUDAKOV_IMPLEMENTATION_WS2026_HEQCD (explanation and notes).**
   - The draft stated as fact that the backup-slide TMD is "the input of the LHμC predictions on pp. 20–23". Only p.20 states that
     the dijet predictions use a WW TMD from the Kutak-Sapeta fit; the Sudakov link is not stated, and p.22 is the 2021 EIC paper
     itself. The explanation was rewritten.
   - A new note says that the quotation token 'ℱ(3)gg' is in the text layer but hidden behind the plot on the rendered slide.
8. **Six EIC-comparison records from p.22 (explanation).** "van Hameren, **Kotko**, Kutak, Sapeta, Zarow 2021" was replaced by the
   citation as printed: 'A. van Hameren, PK, K. Kutak, S. Sapeta, E. Zarow, 2021'. The slide prints only the initials "PK"; the
   registry itself marks the Kotko attribution as unverified.
9. **Five F2 BFKL/BK-panel records from p.18 (explanation).** These are PHYS_SMALLX_F2_BFKL_PLOT_Q2_LOW, _Q2_HIGH, _X_MIN, _X_MAX
   and _CURVES. "Panel settings of the deck's own F2 comparison" became "of the F2 comparison drawn on the LHμC deck", noting that
   no "by …" credit is printed and that the curves cite Stasto-Li 2022 and Hänninen et al. The status stays reported_lhmuc: these
   are plot settings presented for the LHμC x range on a PRIMARY_LHMUC deck.

### muic_acosta2022_cross_sections.yaml

10. **55 μ+p records (explanation).** These are the 11 non-HERA μ+p cells of Table 3, the 12 non-HERA μ+p cells of Table 4, and
    all 32 cells of Table 13. Each was described as "960 GeV **μ−** × 275 GeV p", "960 GeV μ− × 960 GeV p" or "1.5 TeV μ− × 7 TeV
    p". They now read "μ+p at the … beam energies (… μ+ × … p …)". Values, names and scenario ids are unchanged; the scenarios are
    charge-agnostic beam-energy configurations.
11. **PHYS_LHEC_SQRT_S_MUIC2022, PHYS_HIGGS_XSEC_LHEC_60GEV_MUIC2022, PHYS_LHEC_FLAVOUR_TAG_EFF_HBB_MUIC2022 and
    PHYS_LHEC_FLAVOUR_TAG_EFF_HCC_MUIC2022 (explanation).** These called ref. [3] the "LHeC CDR". Ref. [3] (PDF p.45) is
    P. Agostini et al., "The Large Hadron-Electron Collider at the HL-LHC", arXiv:2007.14491, the 2020 update. Ref. [4] is the FCC
    CDR, which was correct.
12. **PHYS_XBJ_REGIME_LOWER_MUIC2022 and _UPPER_MUIC2022 (explanation).** The phrase 'their maximum beam energies' was quoted as
    if it belonged to the p.6 / Fig. 1 statement. It belongs to the Fig. 5 caption on p.14. Both explanations were reworded, adding
    that the paper does not say which configuration reaches which end of 10^-7–10^-8.
13. **PHYS_MUMU_EQUIVALENT_SQRT_S_RATIO_MUIC2022 and PHYS_LHMUC_EQUIVALENT_MUMU_SQRT_S_MUIC2022 (section).** The section string
    said "pp. 13–14", which are printed pages, for statements on PDF p.15. It now reads "PDF pp. 14–15".

### mutristan2022_physics.yaml

14. **PHYS_LUMI_REDUCTION_MUMU_VS_MUE_MUTRISTAN2022 (validation P1 → P0).** Eqs. (6)/(7) give 4.6e33/5.7e32 = 8.1 against "about a
    factor of ten". That is a 19 % gap, so the check is a consistency bracket, not a reproduction. This applies the same standard as
    the extractor's own downgrade of the MuIC "10 times" vs 13 record. The arithmetic is kept in `validation.notes`.

### All four files: confidence caps

15. **Confidence caps.** The validator now enforces research/source_quality_policy.md §4 (lhmuc/registry.py::confidence_cap). This
    caused 206 errors in these files, which is why the extractor's "0 errors" no longer held. All were lowered from 'high' to
    'medium'; no other field changed with them:
    - smallx: 49 for unrefereed slides and 28 for status analogous;
    - MuIC: 23 for status analogous;
    - μTRISTAN: 52 for imported_related from a design_variant and 13 for status analogous;
    - IMCC/Dudko: 41 for status analogous (the Schulte deck is also unrefereed slides).

    The full id list is in the appendix.

## Records added (1)

- **PHYS_SMALLX_F2FL_BONVINI_PLOT_Q2_WS2026_HEQCD.**
  - Record: p.17, Q² = 5 GeV², quotation 'NNPDF3.1sx, Q2 = 5 GeV2', status analogous, confidence medium, P0.
  - Source: the panel title of the F2^p / F_L^p pseudo-data figure that the slide says was "taken from talk by M. Bonvini (2020)".
    This is the analogue of the p.16 Q² records, which the extraction had missed.
  - Notes: the FCC-eh / LHeC kinematic-range arrows (≈ 5e-7 – 1e-4 and ≈ 5e-6 – 9e-4, from pixel measurement) appear only as
    approximate figure reads.

## Records removed

None. Every record is supported by its cited page.

## Validation after verification

- `uv run python tools/validate_yaml.py provenance <file>` reports 0 errors for each of the four files.
- `uv run python -m lhmuc validate` reports **0 errors and 0 warnings for the four G6 files**. 1502 errors remain repository-wide.
  All are confidence-cap errors in other groups' files:
  - imcc_mr7_proton_driver_target_cooling 418;
  - imcc_mr7_collider_reference 357;
  - imcc_mr7_magnets_rf_power_infrastructure 311;
  - imcc_ws2026_schulte_parameters 251;
  - lhc_long_bunch_options_ws2026_zimmermann 129;
  - lhec_ir_ws2026_forthomme 21;
  - lhmuc_ws2026_forthomme_beam_set 13;
  - muic_acosta2022_machine 2.
- `uv run pytest`: every test passes except `test_no_validation_errors`, which fails on the 1502 errors in other files, and
  `test_csv_registries_in_sync`, which is the lead's registry stage.

## Residual doubts

- **AGH p.13:** the slide does not say which LHμC option (1 or 0.5 TeV × 7 TeV) the x_Bj ≲ 1e-7 bound refers to. It prints
  "Q² ~ 1 GeV"; GeV² is recorded as an interpretation of the typo.
- **AGH p.14 / p.16:** the Q²/y convention behind the collider markers is not stated. Assuming beam energies that are not all on that slide (the p.13 legend
  for LHμC 1 TeV × 7 TeV, LHeC 50 GeV × 7 TeV and EIC 21 × 250 GeV; 50 GeV × 50 TeV for FCC-eh; 27.5 × 920 GeV for HERA), Q² = x·s at
  the p.14 markers ranges from about 7 to 19 GeV², so the markers follow no single Q²/s rule. Positions are kept as figure reads in the
  explanations only.
- **AGH p.21 / p.23:** the beam energies and nucleus behind √s = 3.3 TeV are not printed; the Pb interpretation lives in notes
  only.
- **AGH pp. 20–23:** no integrated luminosity, event count or statistical precision is given for the LHμC dijet/trijet
  predictions.
- **AGH p.18:** the authorship of the F2 BFKL / BK NLO comparison is not printed. If the lead decides that it is a published
  calculation (Stasto-Li 2022, Hänninen et al. 2026) rather than a deck-specific one, the five p.18 setting records should become
  analogous. They are reported_lhmuc now.
- **AGH p.20:** the deck's "forward vs central" wording cannot be mapped onto the two rapidity windows (−4 < y < 4 and −4 < y < 0)
  without a sign convention.
- **AGH axis-range records:** PHYS_COVERAGE_PLOT_* and PHYS_SMALLX_F2_BFKL_PLOT_X_* are plot metadata with little physics content.
  They are supported by printed ticks and were kept.
- **MuIC, table discrepancies:** Table 12 (P = 0) differs from Table 14 and Table 15 for the same configuration without
  explanation: σCC 65.1 vs 64.5 fb, and σtH 0.0158 vs 0.019 fb. Both are recorded as printed. This is a conflict candidate.
- **MuIC, FCC-eh energy:** √s is 3.5 TeV on p.4 and 3.16 TeV from 50 GeV × 50 TeV on p.6 and in Fig. 5. This is a conflict
  candidate.
- **MuIC, open questions:**
  - the perturbative order of the MadGraph cross sections (Tables 5–15) is not stated;
  - it is not said whether the "about 3 %" H → bb̄ statistical uncertainty includes background: 1/√900 = 3.3 % for signal-only
    counting, √(S+B)/S = 4.7 % with S/B ≈ 1.
- **MuIC, charge coverage:** W, Z, top and Higgs cross sections at 1.5 × 7 TeV exist for μ−p only. The μ+p values the HELP4CERN
  LHμC would need exist only for NC/CC DIS (Tables 3–4) and, at MuIC energies, for the Higgs (Table 13). The paper's 'LHmuC'
  (proton-driver μ−, IMCC beam) is not the HELP4CERN LHμC.
- **Schulte p.38:** "Int L | Ab-1 | 2.2 | 1.8" conflicts with 1 / 10 ab⁻¹ on pp. 3 and 28 and is most likely a mislabelled N row.
  It is recorded as printed (category unresolved, confidence low); a conflict candidate.
- **Schulte p.10 and p.11:** the energy and bunch population behind "40 000 muons/m/bunch crossing" are not stated, and the IP and
  nozzle reduction is unquantified ("several order of magnitude").
- **Schulte p.28:** the '2+x' accumulation-time format is not defined. The "2+" may be the ramp-up years, but the slide lists three
  ramp-up years.
- **Dudko (SRC_ARXIV_2607_16904):** the source is a SECONDARY_SOURCE. Policy §3 says secondary sources back no status, but the brief
  allows "formulas only". PHYS_MUON_TURNS_PER_LIFETIME_FORMULA_DUDKO2026 (status analogous, P1) is a formula-traceability record
  and was kept. The lead may prefer to re-cite eq. (2) to a primary text.
- **Missing LHμC-specific inputs:** none of the four documents gives a cross section, event yield or integrated-luminosity
  assumption specific to the LHμC (ultra-cold μ+) physics programme.

## Items for the lead (files outside G6)

1. **Registry metadata errors (confirmed on PDF p.1):**
   - `SRC_ARXIV_2203_06258.authors_or_org` says "Rice, Northeastern, **Fermilab**". The affiliations are Rice University,
     Northeastern University and the University of Science and Technology of China.
   - `SRC_ARXIV_2201_06664.authors_or_org` says "**Ryan** Matsudo". The author is Ryutaro Matsudo.
2. **Conflict candidates for research/source_conflicts.yaml:**
   - Schulte p.38 Int L vs pp. 3 and 28;
   - MuIC FCC-eh 3.5 vs 3.16 TeV;
   - MuIC Table 12 vs Tables 14 and 15.
3. **Extractor notes that are out of date:**
   - (a) `parameters/machine/muic_acosta2022_machine.yaml` already cites PDF pages: Table 1 at p.5 and Table 2 at p.8. The
     extractor's "printed pages" warning no longer applies.
   - (c) The Schulte machine rows of p.7 and p.38 (C, B_dipole, technology, N, f_r, L/IP) are already recorded in
     `parameters/machine/imcc_ws2026_schulte_parameters.yaml`. Still unrecorded: the p.28 rows C, B_dipole and collider dipole
     technology for the CERN 2-tunnel and 1-tunnel columns (C 4.8 / 8.7 / 11 / 11 km, B 11 / 14 / 4.8 / 11 T,
     Nb3Sn / HTS / NbTi / "Nb3Sn or HTS"), and p.38 f_r.

## Appendix — records whose confidence was lowered from 'high' to 'medium' (policy §4)

- `smallx_ws2026_heqcd.yaml` — 28 records, rule 'status analogous': PHYS_BFKL_GROWTH_EXPONENT_LAMBDA_WS2026_HEQCD, PHYS_SATURATION_SCALE_FORMULA_GBW_WS2026_HEQCD, PHYS_SATURATION_Q0_GBW_WS2026_HEQCD, PHYS_SATURATION_X0_GBW_WS2026_HEQCD, PHYS_SATURATION_ETA_GBW_WS2026_HEQCD, PHYS_SATURATION_A_EXPONENT_GBW_WS2026_HEQCD, PHYS_SATURATION_STRONGER_IN_NUCLEI_WS2026_HEQCD, PHYS_COVERAGE_PLOT_EIC_E_ENERGY_WS2026_HEQCD, PHYS_COVERAGE_PLOT_EIC_P_ENERGY_WS2026_HEQCD, PHYS_DIJET_KT_FACTORISATION_VALIDITY_WS2026_HEQCD, PHYS_SMALLX_RESUMMED_PDF_SET_WS2026_HEQCD, PHYS_SMALLX_GLUON_PLOT_Q_LOW_WS2026_HEQCD, PHYS_SMALLX_GLUON_PLOT_Q_HIGH_WS2026_HEQCD, PHYS_SMALLX_RESUMMATION_SCHEME_WS2026_HEQCD, PHYS_SMALLX_F2FL_FRAMEWORK_WS2026_HEQCD, PHYS_SMALLX_F2FL_PLOT_Q2_LOW_WS2026_HEQCD, PHYS_SMALLX_F2FL_PLOT_Q2_HIGH_WS2026_HEQCD, PHYS_SMALLX_F2FL_FIXED_ORDER_COMPARISON_WS2026_HEQCD, PHYS_SMALLX_F2FL_BONVINI_PLOT_Q2_WS2026_HEQCD, PHYS_SMALLX_F2_BFKL_FRAMEWORK_WS2026_HEQCD, PHYS_SMALLX_F2_BK_FRAMEWORK_WS2026_HEQCD, PHYS_DIJET_EIC_SUPPRESSION_STATEMENT_WS2026_HEQCD, PHYS_DIJET_EIC_XG_MIN_WS2026_HEQCD, PHYS_DIJET_EIC_SQRT_S_WS2026_HEQCD, PHYS_DIJET_EIC_PT_MIN_WS2026_HEQCD, PHYS_DIJET_EIC_PT_MIN_PANEL2_WS2026_HEQCD, PHYS_DIJET_EIC_RAPIDITY_WINDOWS_WS2026_HEQCD, PHYS_WW_TMD_SUDAKOV_IMPLEMENTATION_WS2026_HEQCD
- `smallx_ws2026_heqcd.yaml` — 49 records, rule 'unrefereed slides': PHYS_SMALLX_XBJ_REACH_INCLUSIVE_DIS_WS2026_HEQCD, PHYS_SMALLX_Q2_REFERENCE_WS2026_HEQCD, PHYS_SMALLX_Y_MIN_WS2026_HEQCD, PHYS_SMALLX_Y_MAX_WS2026_HEQCD, PHYS_SMALLX_REACH_GAIN_VS_LHEC_WS2026_HEQCD, PHYS_SMALLX_REACH_VS_FCCEH_WS2026_HEQCD, PHYS_COVERAGE_PLOT_LHMUC_MU_ENERGY_WS2026_HEQCD, PHYS_COVERAGE_PLOT_LHMUC_MU_ENERGY_OPTION05_WS2026_HEQCD, PHYS_COVERAGE_PLOT_LHMUC_PROTON_ENERGY_WS2026_HEQCD, PHYS_COVERAGE_PLOT_LHEC_E_ENERGY_50_WS2026_HEQCD, PHYS_COVERAGE_PLOT_LHEC_E_ENERGY_20_WS2026_HEQCD, PHYS_COVERAGE_PLOT_LEGEND_DATASETS_WS2026_HEQCD, PHYS_COVERAGE_PLOT_REGION_LABELS_WS2026_HEQCD, PHYS_SMALLX_GLUON_RESUMMATION_CONCLUSION_WS2026_HEQCD, PHYS_SMALLX_F2FL_UNCERTAINTY_X_THRESHOLD_WS2026_HEQCD, PHYS_SMALLX_F2FL_LHMUC_DATA_REGION_WS2026_HEQCD, PHYS_SMALLX_F2_BFKL_PLOT_Q2_LOW_WS2026_HEQCD, PHYS_SMALLX_F2_BFKL_PLOT_Q2_HIGH_WS2026_HEQCD, PHYS_SMALLX_F2_BFKL_CURVES_WS2026_HEQCD, PHYS_SMALLX_F2_BFKL_CONCLUSION_WS2026_HEQCD, PHYS_SMALLX_F2_SATURATION_CONCLUSION_WS2026_HEQCD, PHYS_SMALLX_INCLUSIVE_SF_DISCRIMINATION_WS2026_HEQCD, PHYS_SMALLX_COMPLEMENTARY_OBSERVABLES_WS2026_HEQCD, PHYS_SMALLX_LHMUC_COMPLEMENTARITY_WS2026_HEQCD, PHYS_DIJET_SAT_FRAMEWORK_WS2026_HEQCD, PHYS_DIJET_SAT_PROCESS_WS2026_HEQCD, PHYS_DIJET_SAT_SQRT_S_WS2026_HEQCD, PHYS_DIJET_SAT_YLAB_MIN_WS2026_HEQCD, PHYS_DIJET_SAT_YLAB_MAX_FULL_WS2026_HEQCD, PHYS_DIJET_SAT_YLAB_MAX_FORWARD_WS2026_HEQCD, PHYS_DIJET_SAT_PT_BREIT_MIN_WS2026_HEQCD, PHYS_DIJET_SAT_Q2_MIN_WS2026_HEQCD, PHYS_DIJET_SAT_TARGETS_AND_CURVES_WS2026_HEQCD, PHYS_DIJET_CORR_DECORRELATION_STATEMENT_WS2026_HEQCD, PHYS_DIJET_RPBP_MAX_SUPPRESSION_WS2026_HEQCD, PHYS_DIJET_CORR_SQRT_S_PLOT_WS2026_HEQCD, PHYS_DIJET_CORR_SQRT_S_NUCLEAR_WS2026_HEQCD, PHYS_DIJET_CORR_OBSERVABLES_WS2026_HEQCD, PHYS_TRIJET_SAT_STATEMENT_WS2026_HEQCD, PHYS_TRIJET_SAT_PROCESS_WS2026_HEQCD, PHYS_TRIJET_SAT_SQRT_S_WS2026_HEQCD, PHYS_TRIJET_SAT_YLAB_MIN_WS2026_HEQCD, PHYS_TRIJET_SAT_YLAB_MAX_WS2026_HEQCD, PHYS_TRIJET_SAT_PT_BREIT_MIN_WS2026_HEQCD, PHYS_TRIJET_SAT_Q2_MIN_WS2026_HEQCD, PHYS_TRIJET_SAT_OBSERVABLES_WS2026_HEQCD, PHYS_SMALLX_SUMMARY_COVERAGE_WS2026_HEQCD, PHYS_SMALLX_SUMMARY_RESUMMATION_WS2026_HEQCD, PHYS_SMALLX_SUMMARY_SATURATION_WS2026_HEQCD
- `muic_acosta2022_cross_sections.yaml` — 23 records, rule 'status analogous': PHYS_MUMU14_PP100_EQUIVALENCE_STATEMENT_MUIC2022, PHYS_EIC_SQRT_S_MAX_MUIC2022, PHYS_EIC_SATURATION_ENTRY_X_AU_MUIC2022, PHYS_EIC_GLUON_POLARISATION_X_REACH_MUIC2022, PHYS_QUARK_SPIN_FRACTION_MUIC2022, PHYS_DELTA_G_UNCONSTRAINED_X_MUIC2022, PHYS_PP_EQUIVALENCE_FACTOR_MIN_MUIC2022, PHYS_PP_EQUIVALENCE_FACTOR_MAX_MUIC2022, PHYS_HERA_SQRT_S_MUIC2022, PHYS_HERA_NC_SENSITIVITY_XSEC_MUIC2022, PHYS_HERA_NC_SAMPLE_SIZE_MUIC2022, PHYS_HERA_Q2_REACH_MUIC2022, PHYS_HERA_W_EVENTS_MUIC2022, PHYS_XSEC_NC_MUM_Q2GT3E4_HERA_MUIC2022, PHYS_XSEC_NC_MUP_Q2GT3E4_HERA_MUIC2022, PHYS_XSEC_CC_MUM_Q2GT1_HERA_MUIC2022, PHYS_XSEC_CC_MUM_Q2GT3E4_HERA_MUIC2022, PHYS_XSEC_CC_MUP_Q2GT1_HERA_MUIC2022, PHYS_XSEC_CC_MUP_Q2GT3E4_HERA_MUIC2022, PHYS_HIGGS_XSEC_MUMU_3TEV_MUIC2022, PHYS_HIGGS_BR_BB_MUIC2022, PHYS_HCC_BR_RATIO_TO_HBB_MUIC2022, PHYS_HBB_HLLHC_COMPARATOR_LUMI_MUIC2022
- `mutristan2022_physics.yaml` — 52 records, rule 'imported_related from a design_variant': PHYS_SQRT_S_MUE_MUTRISTAN2022, PHYS_SQRT_S_MUMU_3KM_MUTRISTAN2022, PHYS_SQRT_S_MUTEVATRON_MUE_MUTRISTAN2022, PHYS_SQRT_S_MUMU_LARGE_RING_MUTRISTAN2022, PHYS_INT_LUMI_10YR_MUE_MUTRISTAN2022, PHYS_DUTY_FACTOR_MUTRISTAN2022, PHYS_RUNNING_YEARS_MUTRISTAN2022, PHYS_DETECTORS_ASSUMED_MUTRISTAN2022, PHYS_INT_LUMI_PER_YEAR_MUE_MUTRISTAN2022, PHYS_INT_LUMI_PER_YEAR_MUMU_MUTRISTAN2022, PHYS_LUMI_REDUCTION_MUMU_VS_MUE_MUTRISTAN2022, PHYS_BEAM_POL_E_ASSUMED_MUTRISTAN2022, PHYS_HIGGS_WBF_XSEC_LOSS_LOW_POLARISATION_MUTRISTAN2022, PHYS_SUSY_XSEC_REDUCTION_LOW_POLARISATION_MUMU_MUTRISTAN2022, PHYS_HIGGS_XSEC_WBF_MUE_MUTRISTAN2022, PHYS_HIGGS_XSEC_ZBF_MUE_MUTRISTAN2022, PHYS_HIGGS_XSEC_GENERATOR_MUTRISTAN2022, PHYS_HIGGS_EVENTS_PER_AB_MUE_MUTRISTAN2022, PHYS_HIGGS_SEL_EFFICIENCY_ASSUMED_MUTRISTAN2022, PHYS_HIGGS_KAPPA_STAT_PRECISION_MUE_MUTRISTAN2022, PHYS_HIGGS_ZBB_BACKGROUND_PER_AB_MUE_MUTRISTAN2022, PHYS_HIGGS_XSEC_ZBF_MUMU_2TEV_MUTRISTAN2022, PHYS_HIGGS_XSEC_WBF_MUTEVATRON_MUTRISTAN2022, PHYS_HIGGS_XSEC_ZBF_MUTEVATRON_MUTRISTAN2022, PHYS_HIGGS_EVENTS_PER_AB_MUTEVATRON_MUTRISTAN2022, PHYS_HIGGS_KAPPA_STAT_PRECISION_MUTEVATRON_MUTRISTAN2022, PHYS_HIGGS_PAIR_XSEC_MUTEVATRON_MUTRISTAN2022, PHYS_HIGGS_PAIR_EVENTS_PER_AB_MUTEVATRON_MUTRISTAN2022, PHYS_HIGGS_SELF_COUPLING_PRECISION_MIN_MUTEVATRON_MUTRISTAN2022, PHYS_HIGGS_SELF_COUPLING_PRECISION_MAX_MUTEVATRON_MUTRISTAN2022, PHYS_HIGGS_KAPPA_LAMBDA_PRECISION_SINGLE_HIGGS_MUTEVATRON_MUTRISTAN2022, PHYS_HIGGS_BOOST_GAMMA_MUE_MUTRISTAN2022, PHYS_HIGGS_BOOST_GAMMA_MUTEVATRON_MUTRISTAN2022, PHYS_HIGGS_POLAR_ANGLE_PEAK_MIN_MUTRISTAN2022, PHYS_HIGGS_POLAR_ANGLE_PEAK_MAX_MUTRISTAN2022, PHYS_FINAL_STATE_POLAR_ANGLE_STATEMENT_MUTRISTAN2022, PHYS_B_QUARK_MOMENTUM_PEAK_MUE_MUTRISTAN2022, PHYS_B_QUARK_ANGLE_PEAK_MUE_MUTRISTAN2022, PHYS_B_QUARK_MOMENTUM_PEAK_MUTEVATRON_MUTRISTAN2022, PHYS_B_QUARK_ANGLE_PEAK_MUTEVATRON_MUTRISTAN2022, PHYS_HBB_ACCEPTANCE_THETA_CUT_STATEMENT_MUTRISTAN2022, PHYS_HBB_ACCEPTED_FRACTION_TARGET_MUTRISTAN2022, PHYS_BEAM_BACKGROUND_SHIELDING_STATEMENT_MUTRISTAN2022, PHYS_SUSY_EVENT_THRESHOLD_PER_YEAR_MUTRISTAN2022, PHYS_SUSY_MODEL_ASSUMPTIONS_MUTRISTAN2022, PHYS_SUSY_MUE_REACH_STATEMENT_MUTRISTAN2022, PHYS_SNEUTRINO_XSEC_FACTOR_MUE_MUTRISTAN2022, PHYS_SUSY_MUMU_GAUGINO_MASS_EXAMPLE_MUTRISTAN2022, PHYS_SUSY_MUMU_REACH_STATEMENT_MUTRISTAN2022, PHYS_SUMMARY_HIGGS_FACTORY_STATEMENT_MUTRISTAN2022, PHYS_NEUTRINO_RADIATION_STATEMENT_MUTRISTAN2022, PHYS_OTHER_HIGGS_DECAY_MODES_STATEMENT_MUTRISTAN2022
- `mutristan2022_physics.yaml` — 13 records, rule 'status analogous': PHYS_BEAM_POL_E_TARGET_SUPERKEKB_MUTRISTAN2022, PHYS_HIGGS_BR_BB_USED_MUTRISTAN2022, PHYS_ILC_SEL_EFFICIENCY_250_MUTRISTAN2022, PHYS_ILC_SEL_EFFICIENCY_500_MUTRISTAN2022, PHYS_ILC_ZBB_REJECTION_250_MUTRISTAN2022, PHYS_ILC_ZBB_REJECTION_500_MUTRISTAN2022, PHYS_ILC_SIGNAL_SURVIVAL_MUTRISTAN2022, PHYS_HIGGS_PRECISION_REF10_STATEMENT_MUTRISTAN2022, PHYS_HIGGS_SELF_COUPLING_ONE_LOOP_WBF_EFFECT_MUTRISTAN2022, PHYS_LHCB_FORWARD_COVERAGE_REF_MUTRISTAN2022, PHYS_LHC_SLEPTON_MASS_LIMIT_MUTRISTAN2022, PHYS_LHC_SLEPTON_MASS_DIFFERENCE_CONDITION_MUTRISTAN2022, PHYS_G2_SUPERPARTICLE_MASS_SCALE_MUTRISTAN2022
- `imcc_ws2026_schulte_physics_and_dudko_formula.yaml` — 41 records, rule 'status analogous': PHYS_IMCC_FEASIBILITY_TARGET_SQRT_S_WS2026_SCHULTE, PHYS_IMCC_FEASIBILITY_TARGET_INT_LUMI_WS2026_SCHULTE, PHYS_IMCC_INITIAL_STAGE_TIMING_WS2026_SCHULTE, PHYS_NAS_10X_LHC_STATEMENT_WS2026_SCHULTE, PHYS_NAS_10TEV_MUC_DISCOVERY_REACH_STATEMENT_WS2026_SCHULTE, PHYS_IMCC_EQUIVALENT_PP_SQRT_S_WS2026_SCHULTE, PHYS_MUC_PHYSICS_ADVANTAGE_STATEMENT_WS2026_SCHULTE, PHYS_MUC_COMPLEMENTARITY_FCC_STATEMENT_WS2026_SCHULTE, PHYS_IMCC_BIB_MUON_DECAYS_PER_M_PER_CROSSING_WS2026_SCHULTE, PHYS_IMCC_BIB_ENERGY_FRACTION_ELECTRONS_WS2026_SCHULTE, PHYS_IMCC_DETECTOR_CONCEPTS_WS2026_SCHULTE, PHYS_IMCC_PHYSICS_FEASIBILITY_CONCLUSION_WS2026_SCHULTE, PHYS_IMCC_SQRT_S_SI3_WS2026_SCHULTE, PHYS_IMCC_LUMI_PER_IP_SI3_WS2026_SCHULTE, PHYS_IMCC_INT_LUMI_SI3_WS2026_SCHULTE, PHYS_IMCC_ACCUMULATION_TIME_SI3_WS2026_SCHULTE, PHYS_IMCC_SQRT_S_SI10_WS2026_SCHULTE, PHYS_IMCC_LUMI_PER_IP_SI10_WS2026_SCHULTE, PHYS_IMCC_INT_LUMI_SI10_WS2026_SCHULTE, PHYS_IMCC_ACCUMULATION_TIME_SI10_WS2026_SCHULTE, PHYS_IMCC_SQRT_S_C2T32_WS2026_SCHULTE, PHYS_IMCC_LUMI_PER_IP_C2T32_WS2026_SCHULTE, PHYS_IMCC_INT_LUMI_C2T32_WS2026_SCHULTE, PHYS_IMCC_ACCUMULATION_TIME_C2T32_WS2026_SCHULTE, PHYS_IMCC_SQRT_S_C2T76_WS2026_SCHULTE, PHYS_IMCC_LUMI_PER_IP_C2T76_WS2026_SCHULTE, PHYS_IMCC_INT_LUMI_C2T76_WS2026_SCHULTE, PHYS_IMCC_ACCUMULATION_TIME_C2T76_WS2026_SCHULTE, PHYS_IMCC_SQRT_S_C1T32_WS2026_SCHULTE, PHYS_IMCC_LUMI_PER_IP_C1T32_WS2026_SCHULTE, PHYS_IMCC_INT_LUMI_C1T32_WS2026_SCHULTE, PHYS_IMCC_ACCUMULATION_TIME_C1T32_WS2026_SCHULTE, PHYS_IMCC_SQRT_S_C1T76_WS2026_SCHULTE, PHYS_IMCC_LUMI_PER_IP_C1T76_WS2026_SCHULTE, PHYS_IMCC_INT_LUMI_C1T76_WS2026_SCHULTE, PHYS_IMCC_ACCUMULATION_TIME_C1T76_WS2026_SCHULTE, PHYS_IMCC_IPS_FOR_ACCUMULATION_WS2026_SCHULTE, PHYS_IMCC_RAMP_UP_YEAR1_WS2026_SCHULTE, PHYS_IMCC_RAMP_UP_YEAR2_WS2026_SCHULTE, PHYS_IMCC_RAMP_UP_YEAR3_WS2026_SCHULTE, PHYS_MUON_TURNS_PER_LIFETIME_FORMULA_DUDKO2026
