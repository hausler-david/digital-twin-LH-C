# Verification note: group G15_KAYA2022 (batch 10, 2026-10-29)

Source: SRC_ARXIV_1905_05564. U. Kaya, B. Ketenoglu, S. Sultansoy and F. Zimmermann, "Luminosity and Physics Considerations on
HL-LHC and HE-LHC based µp Colliders", arXiv:1905.05564v2 (PDF of 4 Nov 2021), 8 pp. The source registry gives the journal version
as EPL 138 (2022) 24002; that version was not read. Category RELATED_MACHINE. This is not a PRIMARY_LHMUC source, so no record may
carry reported_lhmuc, and none does.

Files verified:

- `parameters/machine/mup_lhc_options_kaya2022.yaml`: 136 records at hand-over and 136 after verification. None were added or
  removed, and 5 were corrected.
- `parameters/machine/scenarios_batch10_kaya.yaml`: 12 scenarios, `KAYA2022-<HLLHC|HELHC>-<NOMINAL|UPGRADED>-EMU<0P75|1P5|3>TEV`.
  None were changed apart from a header line.

Role: adversarial verifier. I read all eight pages as page images. Pages 2–6 were re-rendered at 300 dpi with `pdftoppm`, and
the Fig. 2 labels at 600 dpi. Every table, equation, Fig. 1, Fig. 2 and the text blocks I cite were cropped and read. I also read
the per-page text layer in the session scratchpad. The verification scripts are outside the repository, in the session scratchpad
as `v15_*.py`.

## What was checked and found correct

**All 115 table and text numbers.** I compared each value against my own transcription of the page images. This transcription
was written independently of the extractor's generator. There were 0 mismatches in value, unit, page or table label, and each
printed cell appears at the end of its quotation.

| Source | Cells checked |
|---|---|
| Table 1 (p. 2) | 22 cells, HL-LHC / HE-LHC: 14/27 TeV, 26.7 km, 1.12 A, 2.2e11, 2760/2808, 90 mm, 25 ns, 2.5 µm, 0.15/0.45 m, 7.1/9 µm, 5x10^34/16x10^34 |
| Table 2 (p. 3) | 22 cells: 7/13.5 TeV, 60 GeV, 1.3/1.7 TeV, 25 ns, 2.2/2.5e11, 2/2.5 µm, 2.3/3e9, 15/20 mA, 7/10 cm, 4.45/4.17 µm, 8x10^33/12x10^33 |
| Table 3 (p. 3) | 30 cells for √s = 1.5 / 3 / 6 TeV: 2.5/4.5/6 km, 2e12, 1/0.5/0.2 cm, 25 µm, 1/0.5/0.25 cm, 5.9/2.95/1.48 µm, 15/12/6 Hz, 2 IPs, 1.25/4.4/12x10^34 |
| Tables 4–5 (p. 4) | E_μ 0.75/1.5/3; √s 4.58/6.48/9.16 and 6.36/9/12.7; L 0.95/0.84/0.57 and 1.4/2.1/1.5; L 0.59/0.52/0.36 and 1.6/2.8/1.9 |
| Table 6 (p. 5) | 0.098/0.0096, 0.12/0.0096, 0.098/0.0096, 0.098/0.011 |
| Table 7 (p. 5) | 4.8e-8, 1.2e-6; 2.5e-8, 6.1e-7; 1.3e-8, 3.1e-7; 6.2e-9, 1.6e-7 |
| Text | r_p = 1.54x10^-18 m (p. 3); r_μ = 1.37x10^-17 m (p. 4); 'of order of 10^33' (p. 1, p. 6); 'down to 10^-8' (p. 5) |

The one remaining numeric record is the analytical estimate, 2.8e32 = 2.8e33/10. I recomputed it.

**Equations.** I compared eqs. (1)–(10) and the unnumbered ξ_xp/ξ_yp pair on p. 3 symbol by symbol against the crops. The text
layer garbles all of them. Points checked:

- the denominators σ_xμ(σ_xμ+σ_yμ) and σ_yμ(σ_yμ+σ_xμ) of the proton pair;
- σ_xp(σ_xp+σ_yp) and σ_yp(σ_yp+σ_xp) in eqs. (2)–(3);
- 4πγ in eqs. (7)–(8);
- ε_N^p and ε_N^μ in eqs. (9)–(10);
- max[σ_p, σ_μ] squared in eq. (6).

The extractor's note on equation numbering is correct. The proton pair carries no number. Numbers (2) and (3) belong to the muon
pair, and p. 4 still says "Eqs. (2) and (3) turn into" eqs. (7) and (8).

**Quotations.** I checked every text quotation piece against the text layer after removing whitespace, sub/superscript markers
and µ/μ differences. Every flag that remained is a text-layer artefact, and each was confirmed on the page image:

- garbled equation glyphs;
- line-end hyphens dropped by the text layer: "center-of-|mass", "Beam-|beam", "well-|consistent", "HL-|LHC", and "g-|2", where
  the text layer has "g2";
- the column/page break inside the eq. (6) quotation.

The table-cell quotations follow the house convention "caption; columns; row, column: cell". The Fig. 2 record uses the same
convention for its bar labels.

**Provenance.**

- 135 records are imported_related with category design_variant. One, MACHINE_PEAK_LUMINOSITY_XI_P_LIMITED_MAX_KAYA2022, is
  analytical_estimate, with a derivation that names its input ids.
- Confidence is medium for 134 records and low for 2, the Fig. 2 labels and the estimate. No record is high.
- Values restated by Kaya et al. name their original reference in applicability.explanation:
  - Tables 1–2: ref. [13], Bordry et al., arXiv:1810.13022;
  - Table 3: ref. [14], Delahaye et al., arXiv:1901.06150;
  - the motivation record: refs. [19]–[21];
  - the two-stage record: ref. [22];
  - the AloHEP record: refs. [15]–[17].
- The bibliography (pp. 7–8) confirms each attribution. Neither arXiv:1810.13022, arXiv:1901.06150 nor arXiv:1710.11157 is in
  research/source_registry.yaml, as the explanations state.
- The JPSCP download watermark does not concern this document. A grep finds no watermark text in either file.

**Arithmetic, re-done independently.** Every figure below agrees with the extractor's.

| Check | Result |
|---|---|
| γ_p, γ_μ | 7460.5 and 14388.2; 7098.3, 14196.7 and 28393.4 |
| σ = √(ε_N β*/γ) | 7.090, 8.842, 4.332, 4.168 µm (protons); 5.935, 2.967, 1.484 µm (muons) |
| HL-LHC upgraded σ_p | printed 4.45 µm, 2.7 % above 4.33 µm; ε_N ≈ 2.1 µm or β* ≈ 7.4 cm would reproduce it |
| Eq. (6) | all twelve Table 4–5 cells within the printed precision |
| Eqs. (9)–(10) | 0.0980, 0.1225, 0.00959, 0.0109 |
| Radii | r_e m_e/m = 1.5347e-18 m and 1.3628e-17 m, so the printed values are 0.3 % and 0.5 % high |
| √s = 2√(E_μ E_p) | 4.5826, 6.4807, 9.1652, 6.3640, 9.0000, 12.7279 TeV |
| Two-beam cycle average x/2 (1 − e^(−2/x)) | x = 0.234, 0.374, 0.374; result 0.117, 0.186, 0.186 |
| One-beam to two-beam ratio | 1.97, 1.87, 1.87 |
| Effective f_cμ from eq. (4) | 13.7, 12.0, 8.3 kHz; fraction of c/C = 0.114, 0.181, 0.165 |
| Gaussian-overlap ratios 2 max²/(σ_p²+σ_μ²) | all twelve as quoted in the luminosity explanations (1.18 … 1.95) |
| f_cp | 31.0 and 31.5 MHz |
| Beam current | 1.092 and 1.111 A, against 1.12 A printed |
| Eq. (5) L_pp | 2.37e35 and 1.50e35 |
| √s_ep | 1.296 and 1.800 TeV |
| N_e e/25 ns | 14.7 and 19.2 mA |
| Table 7, Q²/s | all eight cells, including both rounding windows: 6.376–6.389 TeV for the '~ 6.4' row and 8.909–8.944 TeV for the '~ 9' row |
| Fig. 2 labels | each equals a printed luminosity × 1e8 s; the μp bars match the upgraded E_μ = 3 TeV values |
| ξ_p-limited estimate | the ten matched options (σ_μ ≤ σ_p) give 0.036–0.28e33 after the tenfold reduction, maximum HE-LHC upgraded at E_μ = 1.5 TeV |

**Validation labels.**

- 71 records are P1. Each names `tests/scientific/test_batch10_documents.py::test_kaya2022_*` and, for the decay caveat,
  `tests/scientific/test_imcc_mr7_reference.py::test_mr7_decay_factor_one_decaying_beam_exceeds_two_beam_average`. I checked
  that every test function exists under exactly that name in that file, that it uses the record's value, and that it passes.
- No P1 record lacks a test, and every other record is P0. Arithmetic beyond the tests stays in validation.notes as a
  "candidate check".

**Cross-references.** All of these exist with the values stated:

- PROTON_BUNCH_LENGTH_RMS_SYN (range 5–100 cm);
- PROTON_BUNCH_POPULATION_MULHC (22e10), PROTON_NORM_EMITTANCE_MULHC (2 µm), PROTON_BETA_STAR_MULHC (7 cm) and
  PROTON_IP_BEAM_SIZE_ERL_MULHC (4.3 µm). The μLHC set is the LHeC ERL60-upgraded proton set, as claimed.
- MACHINE_LUMINOSITY_FORMULA_MUIC2022 (with H_hg);
- MACHINE_ALOHEP_EFFECT_TOGGLES_DAGLI2026;
- SRC_ARXIV_2506_15445 and SRC_ARXIV_2101_10476;
- scenario CHEUNG2021-MUP1-MUMINUS-P;
- CONF_LUMI_MODEL_ASSUMPTIONS.

**Ids, units, format.**

- All ids end in `_KAYA2022`, none collides with another file, and the 12 scenario ids are unique.
- Units parse, the key sets are identical to the committed Bakule 2013 records, and every dependency id resolves.
- No record is null or zero.

**Scenarios.** A script rebuilt the expected role → record map for each of the 12 scenarios (ring × proton option × E_μ) and
found 0 mismatches. Each role record's applicability lists the scenario. The labels and descriptions quote the right √s, L, σ_p,
σ_μ, ξ_p, ξ_μ, β*_μ and decay ratio.

The upgraded scenarios list proton_bunch_length and proton_number_of_bunches as unknown, which is correct: Table 2 prints neither.

validation_level P0 is kept. `tools/apply_scenario_levels.py --check` reports 0 excess labels, and docs/validation_plan.md §1 rule 3
makes a composite's level the minimum over its inputs, which here include P0 records such as bunch lengths, circumference,
repetition rate and bunch spacing.

**Consistency with the source registry.** The records match the lead's reading in research/source_registry.yaml, including each
unresolved question:

- decay averaging carried through L_μμ;
- no μp hourglass factor;
- the max convention against the Gaussian overlap;
- synchronisation and the abort gap;
- the tenfold ξ_p reduction to 0.04–0.28e33 (0.036 before rounding);
- the radii offsets;
- the journal version not seen.

The registry's correction of the earlier snippet "2.2×10^12 muons per bunch" to the printed 2×10^12 is reflected in the three
N_μ records.

## Corrections made

All corrections were made in place, and no parameter_id or value was changed.

1. **PHYS_X_BJORKEN_REACH_KAYA2022: uncertainty changed from order_of_magnitude to not_stated.**
   - The text says "can be explored down to 10^-8" (p. 5). That is a power-of-ten bound, not "of the order".
   - The batch rule reserves order_of_magnitude for "of the order" wording.
   - The note now quotes the wording and gives the Table 7 span, 4.8e-8 to 6.2e-9 at Q² = 1 GeV².
2. **MACHINE_EP_SQRT_S_HELHC_ERL60_KAYA2022: candidate-check note made precise.**
   - The note said "1.7 TeV corresponds to E_p ≈ 12.0 TeV".
   - At the printed precision, 1.65–1.75 TeV, the value corresponds to E_p = 11.3–12.8 TeV with E_e = 60 GeV. For example,
     E_p = 12.5 TeV gives 1.73 TeV.
   - The conflict with the 13.5 TeV printed in the same column is unchanged.
3. **MACHINE_MUMU_AVERAGE_LUMINOSITY_MC6TEV_KAYA2022: "consistent" corrected.**
   - The note called the √s = 6 TeV effective collision fraction "consistent with a cycle (decay) average".
   - It is 0.165, 11 % below the two-beam average of 0.186. The 1.5 and 3 TeV columns agree within 3 %.
   - The note now states the 11 % residual and that it is not explained here, because ref. [14] was not read.
4. **MACHINE_LUMINOSITY_FORMULA_MUMU_EQ4_KAYA2022: inference no longer stated as fact.**
   - The note said the Table 3 average luminosity "already contains the cycle (decay) average".
   - It now says this is consistent: within 3 % at 1.5 and 3 TeV, 11 % low at 6 TeV.
   - It also says this is an inference that assumes one bunch per beam, which neither the paper nor Table 3 states.
5. **PHYS_X_MIN_Q2_25GEV2_SQRTS12P7_KAYA2022: rounding stated.**
   - Q²/s at the unrounded √s = 12.728 TeV is 1.543e-7, which rounds to 1.5e-7.
   - The printed 1.6e-7 follows only from the rounded 12.7 TeV, as 1.550e-7 rounded half up.
   - The note now says so; before, it gave the two numbers without a conclusion.
6. **File headers.** Both files gained one line recording this verifier pass.

## Added

None. I scanned all 8 pages for clearly quantitative statements without a record. Only the introduction context that the
extractor's header deliberately excludes remains:

- "98% of mass of the visible part of our Universe" (p. 1);
- the √s = 100 TeV µp collider with an additional 50 TeV proton ring of ref. [10] (p. 2).

Neither concerns the options of this paper, and I agree with leaving them out. The definition f_c = N_b f_rev (p. 3) is quoted
inside the eq. (1) record.

## Removed

None. Every record is supported by the cited page. No value was invented, rounded beyond the printed precision, digitised from a
plot or mis-attributed.

PHYS_MU8_FIG2_BAR_LABELS_KAYA2022 transcribes printed raster text from Fig. 2, not curve values. I confirmed it at 600 dpi:

- 'MC √s=6 TeV 12 ab^-1'
- 'HL-LHC √s=14 TeV 5 ab^-1'
- 'µ⊗HL-LHC √s=9,16 TeV 0,15 ab^-1'
- 'HE-LHC √s=27 TeV 16 ab^-1'
- 'µ⊗HE-LHC √s=12,7 TeV 0,19 ab^-1'
- y axis 'Me8 (TeV)'

The bar heights are not digitised. The record is kept at confidence low and P0.

## Residual doubts and follow-ups for the parent

These cannot be resolved from this document. The network is blocked, and some lie outside this group's files.

1. **No validation-registry rows.** `registries/validation_registry.csv` has no rows for the `test_kaya2022_*` tests that back
   the 71 P1 records. Section 1 of docs/validation_plan.md expects P1 checks to be listed there. This authored registry is outside
   this group's files.
2. **Registry sync.**
   - `tests/unit/test_registry_integrity.py::test_csv_registries_in_sync` and `::test_source_parameters_extracted_in_sync` fail
     until the lead runs `tools/build_registries.py` and `tools/sync_parameters_extracted.py`.
   - The sync tool reports SRC_ARXIV_1905_05564, SRC_ARXIV_1407_8248 and SRC_DOI_10_7566_JPSCP_33_011125 out of sync.
   - Everything else passes: `uv run python -m lhmuc validate` reports 0 errors and 0 warnings, both files show 0 schema errors,
     and all test_batch10_documents.py and test_imcc_mr7_reference.py tests pass.
3. **Unresolved internal inconsistencies of the paper.** Ref. [13] was not read, so none is decided. All are recorded as P0
   candidate checks:
   - The HE-LHC ERL60 √s_ep is printed as 1.7 TeV. 2√(E_e E_p) gives 1.80 TeV with the printed E_p = 13.5 TeV.
   - The HL-LHC beam current is printed as 1.12 A, against N_b N_p e c/C = 1.09 A.
   - Eq. (5) with the Table 1 inputs gives L_pp of 4.7 and 0.94 times the printed values. Crossing angle and levelling are not
     discussed.
   - The HL-LHC upgraded σ_p is printed as 4.45 µm, against 4.33 µm from ε_N and β*.
4. **Table 7.**
   - In the '~ 9' row, the Q² = 1 GeV² cell is printed as 1.3e-8, but Q²/s gives 1.2e-8 at both 9 and 9.16 TeV.
   - In the 12.7 TeV row, the Q² = 25 GeV² cell (1.6e-7) needs the rounded √s.
   - Assigning the two '~' rows to options is an inference from the √s values, and the paper prints no x_min formula.
5. **What L_μμ and Tables 4–5 contain.**
   - The Table 3 'average luminosity' appears to be a cycle (decay) average, but this is inferred, not stated, and leaves an 11 %
     residual at 6 TeV.
   - Whether the luminosity is per IP or summed over the 2 IPs is not stated.
   - Whether the Table 3 bunch length is rms is not stated.
   - Whether Tables 4–5 give peak or average values is not stated. The required ids say PEAK_LUMINOSITY and the notes flag this.
6. **Luminosity-model caveats** (CONF_LUMI_MODEL_ASSUMPTIONS). Each needs a dedicated μp luminosity calculation:
   - μp hourglass factor: σ_z,p = 9 cm against β*_μ = 0.25–1 cm;
   - one-beam decay average, 1.97 or 1.87 times the two-beam one;
   - μμ hourglass and pinch factors that may sit inside L_μμ;
   - ring synchronisation and the abort gap.
7. **Beam-beam.**
   - The target ξ_p, and the limit against which ξ_μ is 'acceptable', are not stated.
   - MACHINE_PEAK_LUMINOSITY_XI_P_LIMITED_MAX_KAYA2022 takes "reduced by an order" as exactly 10, and is an order-of-magnitude
     bound only.
8. **Not given in the paper.** These stay as scenario unknown_roles and are absent, not zero:
   - the muon charge sign;
   - the number of μp interaction points, the number of muon bunches and the collision frequency;
   - the bunch length and number of bunches of the upgraded proton ring;
   - which beam the Table 2 bunch spacing refers to;
   - the inputs and outputs of the AloHEP double-check;
   - the run time behind the Fig. 2 integrated luminosities.
9. **Scenario level.** The scenarios stay P0. The batch-10 task allowed P0 or P1, and the extractor's original task asked for P1.
   The lead may raise them only if the composite-level convention of docs/validation_plan.md §1 rule 3 changes.
10. **Journal version.** EPL 138 (2022) 24002 was not seen. Differences from arXiv v2, for example in Table 2 or Table 7, are
    unknown.
