# Verification note: group G16_BEER2014 (batch 10, 2026-10-29)

Source: SRC_ARXIV_1407_8248. G.A. Beer et al. (28 authors), "Enhancement of muonium emission rate from silica aerogel with
a laser ablated surface", arXiv:1407.8248v1 [physics.ins-det], 31 Jul 2014, 8 pp. (PTEP 2014 (9) 091C01 as cited by later
papers; the journal version was not read). Category PEER_REVIEWED. It is not a PRIMARY_LHMUC source, so no record may be
`reported_lhmuc`.

File verified:

- `parameters/source/muonium_emission_ablated_aerogel_beer2014.yaml`
  - 78 records at hand-over and 78 after verification: 0 added, 0 removed.
  - 18 records corrected or annotated. Every `parameter_id` is unchanged.
  - Four comment lines were added to the header: the generator script is superseded by this file, and this note records
    the verification.
- No scenario file belongs to this group. Every record has `scenario: null`, which is right: no value is an LHμC scenario
  value.

Role: adversarial verifier. For every record I checked value, unit, page, section, table/figure/equation label, quotation,
uncertainty, provenance status and applicability, scenario, derivation, dependencies, confidence, validation label and notes.

## Method

1. **Page images.** All 8 pages were read as images. Two items were re-rendered at 300 dpi and read again:
   - Table 1 (p. 5), cell by cell;
   - the p. 4 diffusion-length expression.
2. **Quotations.**
   - Every quotation was split at the extractor's markers (`[p. N]`, `[...]`, `[text, p. 5]`) and searched in the
     normalised text layer (`…/scratchpad/text/1407.8248v1_pNN.txt`).
   - 11 segments do not match the text layer. All 11 were confirmed on the page images:
     - 9 are Table 1 row transcriptions (the text layer stores the table column by column);
     - 2 are the stacked exponent of `l_d = (Dτ)^{−1/2}`.
   - Two other text-layer artefacts were also confirmed on the images: the line-broken "order-of-magnitude" (p. 2) and
     "260 ◦ C" for 260 °C (p. 5).
   - Every segment lies on a page listed in its record's `page` field.
3. **Values and units.**
   - Every value was compared with its quotation and with the page image.
   - Table 1 is stored per muon stop, so 3.72, 2.74, 16.0, 20.9 and 30.5 per 10^3 become 3.72e-3, 2.74e-3, 0.016, 0.0209
     and 0.0305. The statistical σ are 1.1e-4, 1.1e-4, 2e-4, 7e-4 and 3e-4.
   - Every unit parses with `lhmuc.units.parse_unit`, including fs, nm, second, meter**2/gram, ppm, kelvin and mT.
4. **Arithmetic re-done.** Every "audit arithmetic" or "candidate check" statement was recomputed:
   - 30.5/3.72 = 8.199. Statistical σ 0.256; 0.424 with the 4 % and 1 % systematics added.
   - 3.72/2.74 = 1.358, a 6.3 σ difference. 30.5/2.74 = 11.13.
   - 9.6e-4 × 30.5/2.74 = 1.069e-2, and 9.6e-4 × 8.199 = 7.87e-3.
   - 0.1 ppm × √5 = 0.224 ppm.
   - Adjacent pitch differences: 12.6 σ and 6.7 σ.
   - 5 % FWHM = 2.12 % RMS.
   - Absolute systematics: 0.037, 0.64, 0.84 and 1.22 per 10^3 stops.
   - 4.8e-3/0.5 = 0.96 %. Pitch minus hole diameter: 30, 130 and 230 µm. Unablated remainder: 7 − 4.5…5.0 mm.

   All agree with the file.
5. **Statuses, confidence and labels.**
   - Status: 73 records are `analogous` and 5 are `unknown` (value null, confidence none). None is reported_lhmuc,
     derived_lhmuc or analytical_estimate, and no record has a derivation.
   - Confidence: never high. Medium everywhere, except low for the misprinted l_d expression.
   - Records restating ref. [7] (Bakule 2013) or ref. [4] (E34 CDR) name that reference in `applicability.explanation`.
   - P1 is claimed for 6 records. Each cites an existing test in `tests/scientific/test_batch10_documents.py`:
     - `test_beer2014_enhancement_at_least_eightfold`
     - `test_beer2014_flat_sample_vs_bakule2013`
     - `test_beer2014_fabrication_and_projection_arithmetic`

     All three tests pass. The extractor deliberately left the design intensity (1e6 s^-1, printed "of the order of") and
     the test inputs (800 pulses, 1 kHz, Table 1 cells) at P0. I agree with that choice.
6. **Cross-references.**
   - All 135 parameter, source and conflict ids named in the file resolve (`lhmuc.registry.load_all`). The four tokens
     that do not resolve are not ids: G16_BEER2014, I_USM, PEER_REVIEWED and the `<rho>MGCC_BAKULE2013` pattern.
   - The `<rho>` patterns expand to existing records for 29, 47, 97 and 178 mg cm^-3.
   - Every number quoted in the notes from other records matches those records. Checked: Bakule 2013, Beare 2020,
     Abe 2019, Aritome 2024 and the Kraków Zhang deck.
   - The cross-document claims were also checked on the other uploads' text layers and page images:
     - Bakule 2013 contains no "0.3%", "1.0%", "about 2 mm", "ethanol" or "260";
     - Abe 2019 refs. [29, 30] are Bakule 2013 and Beer 2014;
     - Zhang 2021 pp. 3–4 quotations, and its ref. [8] = Beer 2014;
     - Beare 2020 pp. 6, 11, 18 and 19;
     - Kraków Zhang deck p. 4.
7. **JPSCP watermark.** The per-download line at the top of each Zhang 2021 page was never transcribed. The Zhang
   quotations in the notes were checked against the text layer with that line excluded, and against page crops that leave
   out the page top. A token-level check finds none of the watermark's tokens in the YAML. This note does not reproduce it.
8. **Validation.**
   - `uv run python tools/validate_yaml.py provenance <file>`: 0 schema errors.
   - `uv run python -m lhmuc validate`: 0 errors, 0 warnings.
   - `uv run pytest`: everything passes except two sync checks on generated files (see residual doubt 12).

## Checked and found correct (no change)

- **Table 1 (p. 5), every cell:**

  | Sample | Pitch | Yield per 10^3 muon stops |
  |---|---|---|
  | Flat | none | 3.72 ± 0.11 |
  | Flat (Ref. [7]) | none | 2.74 ± 0.11 |
  | Laser ablated | 500 µm | 16.0 ± 0.2 |
  | Laser ablated | 400 µm | 20.9 ± 0.7 |
  | Laser ablated | 300 µm | 30.5 ± 0.3 |

  The caption reads "For all laser processed samples, the diameter of the structure is 270 µm".
- **Fabrication (p. 3):** 800 nm, 230 fs, 0.6 mJ/pulse, 1 kHz, 30 µm spot, 0.8 s and 800 pulses per hole, 30 × 30 mm^2,
  300/400/500 µm pitch, 4.5–5.0 mm depth, 7 mm thickness, 29 mg cm^-3, about 270 µm diameter, 5–10 % mass loss,
  one-sided ablation.
- **Set-up (p. 4, footnote 2, Fig. 2):** TRIUMF M15 subsurface muons, 300 µm beam scintillator, ~1e4 s^-1, 5 % FWHM,
  ~23.0 MeV/c, half of the beam stopped, ~2 mm RMS resolution, 100 µm silica plate, −8 < z < 40 mm, regions 10–20, 20–30
  and 30–40 mm, 8 mT vertical field. The Fig. 3 panel labels and legend ('Flat Aerogel (2013)', 'Drilled Aerogel') and the
  y-axis normalisation per 3 × 10^8 muons are as transcribed.
- **J-PARC projection (pp. 5–6):** 28 MeV/c and 5 % RMS; 0.01 per incident muon; 0.2 × 10^6/s; "five times smaller";
  0.1 ppm; 0.4 ppm in 10^7 s at 50 % polarisation.
- **p. 2 context:** 300 MeV/c ring (ref. [4]), order 10^6 s^-1, order 10^8 s^-1, 0.3 %, 1.0 %, order-of-magnitude
  improvement, 2.2 µs, ~30 µm, ~2 mm, order 100 µm, and footnote 1 (up to 1000 m^2 g^-1).
- **The five unknown records are justified:**
  - Vacuum window thickness: the window is only described as "minimized".
  - D: a symbol only.
  - T: the paper says only "room-temperature" and "thermal velocity".
  - Ionisation inputs: these come from ref. [4] and are not printed.
  - Formation fraction: the paper gives none.

  The Zhang 2021 attributions quoted in their notes are verbatim: 52 %, T = 322 K, D = 870 cm²s⁻¹ and 23.2 mg/cm³,
  8.8 mm, all cited to "[8]".
- **Uncertainty types:**
  - "of (the) order of" → `order_of_magnitude`;
  - "about", "~" or "typically" → `not_stated` with the source wording in the note;
  - Table 1 → `gaussian_sigma` with the printed statistical σ.
- **Physics background deliberately not extracted (correct):** the p. 1 "about 3.5 σ" g−2 discrepancy and the E821
  3.094 GeV/c magic momentum. The latter is kept in the notes of `MACHINE_JPARC_G2_MUON_MOMENTUM_BEER2014`.

## Corrections (all ids kept)

1. **A false statement in two records was refuted and corrected.** The records are
   `SOURCE_LASER_ABLATION_MASS_LOSS_FRACTION_MIN_BEER2014` and `SOURCE_LASER_ABLATION_MASS_LOSS_FRACTION_MAX_BEER2014`.
   - Their notes said that Beare et al. 2020's 0.14 µg per hole and this paper's 5–10 % are results that "neither paper
     compares". That is wrong. Beare et al. 2020 p. 11 recall this result ("only 5% − 10% of the expected difference, which
     was based on the ablation geometry and target density [15]").
   - Beare et al. then repeat the comparison on their target S18 (Table 3, p. 12). They find 0.14 µg per hole, "consistent
     with the expected weight loss based on the assumption of a conical shape for the holes".
   - The notes now say this. They add that Beare et al. do not state which hole shape the 2014 "expected difference"
     assumed, so the two ratios are not directly comparable.
2. **`SOURCE_MU_EMISSION_ENHANCEMENT_PITCH300UM_BEER2014`, notes: attribution made precise.**
   - The notes listed the 2026 Kraków Zhang deck as a plain restatement of this result.
   - The deck's p. 4 sentence is "(Double) laser-ablation on surface of aerogel was developed to increase the muonium
     emission by an order of magnitude". It sits on a slide that cites "G. Beer et al., PTEP 091C01 (2014)".
   - This paper ablated one side only and claims "at least eight times". The notes now say exactly that.
   - "Abe et al. 2019, who cite this paper among others" is made precise: Abe's refs. [29, 30] are Bakule 2013 and this
     paper (checked against the Abe reference list).
3. **`SOURCE_MU_VACUUM_YIELD_REGIONS13_BAKULE2013_BEER2014`, explanation.** It said the value was "Restated … from ref. [7]".
   The figure "about 0.3%" does not appear in ref. [7] (text search of all 11 pages). The explanation now calls it Beer et
   al.'s rounded summary of the ref. [7] result; ref. [7] Table 1 gives the per-density yields.
4. **`SOURCE_MU_TOTAL_EMISSION_PROBABILITY_BAKULE2013_BEER2014`, explanation.** Same issue. "1.0%" does not appear in
   ref. [7], which gives a naive-diffusion-model y_vac = 4.8 × 10^-3 per incident muon (p. 10). The explanation now says so.
   The value 0.01 is unchanged: it is what Beer et al. print.
5. **`SOURCE_MU_STOPPING_DISTRIBUTION_EXTENT_BEER2014`, explanation.** The explanation made "about 2 mm" part of the summary
   of ref. [7], while the notes correctly said that ref. [7] has only "a few millimeters". The explanation now says the
   2 mm is Beer et al.'s own figure.
6. **`SOURCE_MUONIUM_FORMATION_FRACTION_BEER2014`, explanation.**
   - It said Zhang 2021's 52 % "originates in" Bakule 2013 p. 3. That is an inference: Zhang 2021's references [1]–[10]
     do not include Bakule 2013.
   - The explanation now reads "matches the MuSR result 0.52 ± 0.01 of Bakule et al. 2013 p. 3 (origin inferred, Zhang et
     al. 2021 do not cite Bakule et al. 2013)". The value stays null.
7. **`SOURCE_LASER_ABLATION_HOLE_DIAMETER_BEER2014`, symbol.** The diameter used `d_hole`, the same symbol as the two depth
   records. It is now `phi_hole`, which follows Beare 2020's φ for diameter and d for depth.
8. **Cross-references added so that the same measurement is not counted twice.**
   - Beare et al. 2020 Table 4 (p. 18) relists this paper's four samples as "The emission rates measured in the previous
     study [15]": O2013-1 3.72 ± 0.11, O2013-2 16.0 ± 0.2, O2013-3 20.9 ± 0.7 and O2013-4 30.5 ± 0.3 ‰.
   - A sentence saying "the same measurement, not an independent one" was appended to the notes of
     `SOURCE_MU_VACUUM_YIELD_REGIONS13_FLAT_BEER2014` and of `…_ABLATED_PITCH500UM_`, `…_PITCH400UM_` and
     `…_PITCH300UM_BEER2014`.
   - The 300 µm record now links `SOURCE_MU_EMISSION_RATE_O2013_4_TRIUMF_BEARE2020`.
9. **Beare 2020 data on this paper's targets, appended to notes.** Each item is quoted from Beare and labelled as not
   being in this paper:
   - `SOURCE_MU_VACUUM_YIELD_REGIONS13_ABLATED_PITCH400UM_BEER2014`:
     - Beare's Table 1 (p. 6) lists target S2013-1 with the remark "Reuse of O2013-3", with T 8 mm, ρ 26.0 mg/cm^3,
       φ 0.27 mm, p 0.4 mm and d 4.75 mm.
     - It was re-measured at TRIUMF in 2017 at 17.2 ± 0.2 ‰ (Table 4), against 20.9 ± 0.7 ‰ here.
     - Beare et al. do not comment on the difference (text search).
   - `SOURCE_AEROGEL_DENSITY_BEER2014` and `SOURCE_AEROGEL_THICKNESS_BEER2014`: Beare lists ρ = 29 mg/cm^3 and T = 7 mm for
     O2013-1 to O2013-4, but ρ = 26.0 and T = 8 mm for the reused O2013-3. So the 29 mg cm^-3 here may be a nominal value.
   - `SOURCE_LASER_ABLATED_AREA_SIDE_BEER2014`: Beare's Table 1 footnote c ("These targets have a height and width of
     40 mm and 30 mm, respectively.") covers S2013-1, the reused 400 µm target. That transverse size is Beare's statement;
     this paper gives none.
   - `SOURCE_LASER_ABLATION_HOLE_DEPTH_MIN_BEER2014` and `SOURCE_LASER_ABLATION_HOLE_DEPTH_MAX_BEER2014`: Beare lists
     d = 4.75 mm for O2013-2 to O2013-4.
   - `SOURCE_MU_VACUUM_YIELD_SYST_REL_ABLATED_BEER2014`, for comparison: Beare p. 19 gives −7 % to +12 % relative systematics
     for its 2017 TRIUMF rates, dominated by target positioning and background modelling.
10. **Header.** Two comment lines were replaced by four:
    - the generator script (`scratchpad gen/g16_beer2014.py`) is superseded by the YAML;
    - pointer to this note.

## Removed

Nothing. Every record is backed by a verbatim quotation or an exact cell transcription on the cited page. The five
unknown records document values that the paper does not give but that later papers attribute to it, or that a model of the
measurement needs.

## Residual doubts (for the lead)

1. **Misprint on p. 4.** `l_d = (Dτ)^{−1/2}` is printed with a negative exponent. That is dimensionally an inverse length;
   the planar diffusion length is (Dτ)^{1/2}. It is transcribed as printed with confidence low. The journal version was
   not seen and might correct it.
2. **Fig. 3 legend.** The legend says 'Flat Aerogel (2013)' and the caption says only "flat aerogel (open circles)", so it is
   not stated whether the open circles are this work's flat sample (3.72) or the ref. [7] sample (2.74).
   - Beare 2020 names all four of this paper's targets "O2013-…", which suggests 2013 is this work's sample or measurement
     year.
   - The Kraków Zhang deck p. 4 reproduces a Region 1 panel labelled "no hole" and "w/ holes".

   Neither settles it. No curve was digitised, so no value depends on it.
3. **Origin of "0.01 per incident muon" (p. 5).** The paper shows no arithmetic.
   - The reading 9.6e-4 (Bakule 2013 eq. (1) J-PARC scaling) × 30.5/2.74 = 1.07e-2 reproduces it. It is recorded only in
     notes and validation.notes, labelled as not stated.
   - Whether 0.01 counts all vacuum decays or only those 10–40 mm from the surface is unknown.
4. **Design intensity.** p. 2 says "of the order of 10^6 s^-1". Only p. 6 ("five times smaller" than the design, with
   0.2 × 10^6/s projected) pins it at 1 × 10^6. The record stays P0 and `order_of_magnitude`; I agree.
5. **0.4 ppm projection vs 0.1 ppm design.** Neither can be re-derived because the design running time and polarisation
   are not printed. Simple 1/√rate scaling gives 0.22 ppm, not 0.4 ppm.
6. **Reproducibility of the ablated yields.**
   - Beare 2020 re-measured the reused 400 µm target at 17.2 ± 0.2 ‰ against 20.9 ± 0.7 ‰ here: 18 % lower, 5.1 σ with
     statistical errors only.
   - Beare lists a different ρ and T for that target.
   - Beare's systematics are −7 %/+12 %, against the 4 % (ablated) and 1 % (flat) quoted here.

   Anyone using Table 1 as a target-performance input should treat the 4 % as optimistic and consider target-to-target
   and run-to-run spread. The ~36 % difference between the two nominally similar flat samples, 3.72 vs 2.74, points the
   same way. These are cross-paper observations, not conflicts in this file.
7. **Precision of the restated ref. [7] summaries.** "about 0.3%", "1.0%" and "about 2 mm" are Beer et al.'s own
   summaries. The denominator of the 1.0 % is not restated; per stopping muon is the likely reading, because
   4.8e-3 per incident muon divided by about 0.5 stopping is about 0.96 %.
8. **J-PARC design momentum.** It is 28 MeV/c with 5 % RMS here, a sentence identical to Bakule 2013 p. 10. Abe et al.
   2019 give 27 MeV/c with 5 % RMS. The records are kept separate.
   `research/source_conflicts.yaml` has no entry for this; decide whether it is a design evolution or a conflict.
9. **Footnote 1, specific surface area.** "up to 1000 m^2 g^-1 in some of our samples" is not tied to the 29 mg cm^-3
   targets. Bakule 2013 measured at most 914 m^2 g^-1.
10. **Formation-fraction conflict.** `SOURCE_MUONIUM_FORMATION_FRACTION_BEER2014` (null) documents the Zhang 2021
    mis-citation. The extractor suggests adding it to `CONF_MUONIUM_FORMATION_FRACTION.affected_parameters`; I support
    that.
11. **Stale note in `registries/missing_evidence.csv`.** The bracketed verifier note in ME_031 says Beer 2014 and Zhang
    2021 have no parameter records yet. That is now out of date; this verifier did not edit registries/.
12. **Generated files are out of sync.** `uv run pytest` fails only `test_csv_registries_in_sync` and
    `test_source_parameters_extracted_in_sync`, for SRC_ARXIV_1407_8248 and another agent's SRC_ARXIV_1905_05564. They
    clear when the lead runs `tools/build_registries.py` and `tools/sync_parameters_extracted.py`.
13. **Journal version not seen.** All page numbers refer to arXiv v1, whose header still carries the PTEP template
    placeholders.
