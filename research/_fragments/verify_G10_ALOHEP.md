# Verification note — group G10_ALOHEP (SRC_ARXIV_2610_09839, Dağlı & Karaca, AloHEP software paper, arXiv:2610.09839v1, 45 pp)

Adversarial verification of the batch-7 extraction, 2026-10-29. Files checked (the only files edited):

- `parameters/machine/alohep_benchmarks_dagli2026.yaml` — 250 records on arrival, 251 after verification (one added, none removed)
- `parameters/machine/scenarios_batch7_alohep.yaml` — scenario `ALOHEP-MUCOL-10TEV-BENCHMARK-2026` (26 roles, 21 unknown roles)
- `docs/tools/alohep_method_dagli2026.md` — method note

## What was checked

Every one of the 250 records was compared with the cited page of the PDF (`references/_local/arXiv-2610.09839v1.pdf`):
the pdftotext layer of all 45 pages was read, and the number-bearing pages were opened as page images (2, 3, 10, 11, 13, 17,
19, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 39). Checked per record: value, unit (pint parse through
`lhmuc/units.py`), page, table/figure label, verbatim quotation or cell transcription, provenance status, scenario
assignment, applicability text (original source named where the paper cites one: PDG [32], EIC CDR [33], ILC staging
report [31], MuCol MR7 [35], Herr–Muratori [19], LHC [22], RHIC [34]), dependencies and every derivation / P1 arithmetic.

- Tables 1, 2, 3, 4, 5, 6 and A.1: every cell transcription matches the page image (Table A.1 entries also checked
  against the text layer because the printed table is very small).
- Program summary (p. 2), hardware paragraph (p. 22), ILC-125 comparison (p. 31), HERA/EIC text (p. 32–33), species
  coverage and the 10 TeV μ+μ− decay benchmark (p. 36), Appendix A relation (p. 39): all quotations verbatim.
- Status: 246 `analogous`, 5 `analytical_estimate`; **no record carries `reported_lhmuc`** (grep count 0). Applicability
  `screening_only` with the required explanation on all 251 records.
- Required ids present with the stated values: `MACHINE_ALOHEP_MUCOL_SQRT_S_DAGLI2026` 10 TeV,
  `_BUNCH_POPULATION_` 1.8e12, `_BETA_X_STAR_` / `_BETA_Y_STAR_` / `_BUNCH_LENGTH_` 1.5 mm, `_NORM_EMITTANCE_` 25 µm,
  `_RING_CIRCUMFERENCE_` 11.4 km, `_REPETITION_RATE_` 5 Hz, `_STORE_TIME_` 0.2 s, `_TURNS_PER_STORE_` 5260,
  `_GAMMA_TAU_` 0.104 s, `_DECAY_FACTOR_SIM_` 0.252, `_DECAY_FACTOR_ANALYTIC_` 0.254 (all on p. 36, confirmed on the image).

Arithmetic recomputed by the verifier (all agree with the extractor's P1 methods):

| record | reproduction |
|---|---|
| Table 1 ratios | 3.420/3.786 = 0.9033, 3.758/3.786 = 0.9926, 3.771/3.786 = 0.9960, 3.782/3.786 = 0.9989 |
| CIC smoothing factors | [1 + (8/N_g)²/6]⁻¹ = 0.9036, 0.9883, 0.9958, 0.9989 for N_g = 10, 30, 50, 100 |
| updateQ exponent | log(4.63 s/48 ms)/log(100) = 0.99 |
| grid exponents | log[(12.2×0.975)/(0.092×0.47)]/log 3 = 5.11; log[(11520×1.00)/(208×0.996)]/log 2 = 5.80 |
| A_x, A_ILC | 0.3/13 = 0.023; 0.3/0.40 = 0.75 |
| LHC Piwinski example | Φ = (7.7 cm/16.7 µm)·tan(142.5 µrad) = 0.657, S = 0.836; 1.20e34 × 0.835 = 1.00e34 |
| Table 3 / Table 6 | 0.991/0.977 = 1.014; 0.974/0.912 = 1.068; 4.22/4.32 = 0.977; 4.28/4.32 = 0.991; 9.55/10.5 = 0.910 (printed 0.912); 10.2/10.5 = 0.971 (printed 0.974) — rounding of 3-digit cells |
| Table 4 | 8.394/3.786 = 2.217; 8.334/3.786 = 2.201; 8.394/8.334 − 1 = 0.72 %; 603/277 = 2.18 |
| ILC-125 | H_D = 0.82/0.374 = 2.19; σ*_y = sqrt(35 nm × 0.41 mm/244 618) = 7.66 nm, with 0.40 mm 7.57 nm; D_y = 2 N r_e σ_z/[γ σ_y(σ_x+σ_y)] = 24.8 with σ_x = 0.729 µm |
| HERA / EIC | 2√(920×27.6) = 318.7 GeV; 2√(275×10) = 104.9 GeV; 0.977/0.980 − 1 = −0.3 %; 0.912/0.916 − 1 = −0.4 %; 94.9/8.58 = 11.1; 30/8.58 = 3.50; 27.6/10 = 2.76 |
| L_geo/L_nom factors | HERA 2·111·30/(√(111²+110²)·√(30²+30²)) = 1.0045; EIC 2·94.9·8.63/(√(94.9²+94.8²)·√(8.58²+8.63²)) = 1.0034 |
| μ+μ− benchmark | 1/(5 Hz) = 0.2 s; 0.2 s·c/11.4 km = 5259.5 turns; γτ = (5000/0.10566)·2.197 µs = 0.1040 s; two-beam store average (1−e^(−2T/γτ))/(2T/γτ) = 0.2544 (one-beam form would give 0.444, so the 0.254 of MuCol is the two-beam average); 0.252/0.254 = 0.992; σ* = √(25 µm·1.5 mm/47 322) = 0.89 µm |

The lead's tests `tests/scientific/test_batch7_documents.py::test_dagli2026_mucol_10tev_decay_factor_and_turns` and
`::test_decay_averaging_differs_between_mumu_and_mup` pass (14 passed in the file).

Cross-references of the method note to the registry were checked: `MACHINE_PEAK_LUMINOSITY_ERL_MULHC` 7.2e33 and
`_MUTRISTAN_MULHC` 8.8e33 (SRC_ARXIV_2506_15445 p. 12), `MACHINE_PEAK_LUMINOSITY_WS2026_FORTHOMME` 1e34 (slide 17),
`MACHINE_MU_AVERAGE_POPULATION_FRACTION_MULHC` 0.63 ('2000-turn circulation period'), `MACHINE_MU_BUNCH_LENGTH_MULHC` 2 mm,
`PROTON_BETA_STAR_MULHC` 7 cm, `MACHINE_IP_BEAM_SIZE_MU_ERL_MULHC` / `PROTON_IP_BEAM_SIZE_ERL_MULHC` 4.3 µm,
`PROTON_BUNCH_LENGTH_RMS_SYN` (synthetic), `ME_043_ALOHEP_CODE_AND_INPUT_DECKS` (open), `CONF_LUMI_MODEL_ASSUMPTIONS`
(open; hourglass ≈ 0.53 for a 7.5 cm proton bunch per docs/validation_plan.md rows 6–7), `lhmuc/analytical.py::luminosity_general_cm2s`
and `::hourglass_factor` exist, scenarios `MULHC-PTEP2026-*` and `LHMUC-WS2026-FORTHOMME` exist and the Forthomme
unknown_roles do include muon energy, emittances and bunch lengths.

## Corrections made

1. `MACHINE_ALOHEP_DECAY_IMPLEMENTATION_DAGLI2026` — value trimmed to what the paper states ('applied analytically
   (muon-survival factor over the store; the functional form is not written in the paper)'); the clause 'not simulated
   particle by particle' is an inference and was moved to the notes as a verifier reading.
2. `MACHINE_ALOHEP_MUCOL_BEAM_ENERGY_DAGLI2026` (5 TeV, analytical_estimate) — confidence high → medium: the paper never
   prints '5 TeV'; it is √s/2 (rule: high only for values read from the page).
3. `MACHINE_ALOHEP_MUCOL_CROSSING_ANGLE_DAGLI2026` (0 mrad) — confidence high → medium and notes extended: the number 0 is
   inferred from the word 'head-on' (Fig. 24 caption and p. 36 text), not printed as a number. Kept as a 0 (physical
   value), consistent with the paper's definition of head-on (p. 6, v1 = −v2).
4. `MACHINE_ALOHEP_GRID_DEFICIT_100CUBED_DAGLI2026` — uncertainty note added ("source says 'at the 0.1% level'").
5. `MACHINE_ALOHEP_GRID_SCALING_EXPONENT_10_30_DAGLI2026` / `_50_100_` — dependencies completed with the Table 1
   potential-solve-share records, which the P1 reproduction uses.
6. `MACHINE_ALOHEP_VALIDATED_DY_UPPER_DAGLI2026` — name corrected: the paper's 'D_y ≤ 1.3' is a rounded bound, not the
   largest tabulated value (Table 5 EIC D_y = 1.3420).
7. `MACHINE_ALOHEP_HERA_SQRT_S_DAGLI2026`, `MACHINE_ALOHEP_EIC_SQRT_S_DAGLI2026`,
   `MACHINE_ALOHEP_ASYMMETRIC_BENCHMARK_GRID_POINTS_DAGLI2026`, `_MACROPARTICLES_` — table_figure_or_equation corrected:
   the quotation is p. 32 text; the tables that restate the value are on p. 34.
8. `parameters/machine/scenarios_batch7_alohep.yaml` — header comment corrected: it said the crossing-angle setting of
   the muon run is unknown while the scenario maps `crossing_angle` to the 0 mrad head-on record; now says hourglass /
   grid / macroparticle settings are unknown and that the run is head-on.
9. `docs/tools/alohep_method_dagli2026.md` — (a) 'all status analogous' → five computed values are analytical_estimate;
   (b) §3 'So decay is not simulated particle by particle' marked as our reading, not the paper's words;
   (c) §8 `MACHINE_MU_BETA_STAR_MATCHED_IMPLIED_MULHC` = 4.4 cm → 4.37 cm (≈ 4.4 cm, the registry value);
   (d) §8 the 7.5 cm proton bunch length flagged as an HL-LHC-type assumption (`PROTON_BUNCH_LENGTH_RMS_SYN`), not a source value;
   (e) §8 HERA/EIC runtime '≈ 80–90 s' → '≈ 80–92 s' (Table 6: 79.9–92.2 s); (f) status-label list of P1 reproductions
   made non-exhaustive; (g) verification line added at the top.

## Added

- `MACHINE_ALOHEP_POTENTIAL_GRID_MARGIN_DAGLI2026` = 2 (dimensionless), p. 17: 'the potential grid extends two cells
  beyond the charge grid so that the interpolation stencil of the force (below) is complete everywhere inside the
  collision region' — a numerical-method detail missed by the extractor, relevant to reproducing the paper's grids.

## Removed

None. All 250 original records are supported by the cited page; no value was found invented, rounded or mis-attributed.

## Residual doubts (not resolvable from the paper)

1. The functional form of the `-decay` factor is not written; the two-beam average (1−e^(−2T/γτ))/(2T/γτ) reproduces the
   MuCol 0.254 but whether the code applies a one-beam or a two-beam average to an asymmetric μp pair is unknown.
2. Grid, macroparticle count, hourglass setting and absolute L_nom of the 10 TeV μ+μ− run are not printed (only ratios).
3. Underlying inputs (N, f_c, β*, emittances, σ_z of both beams) of the HERA, EIC, LHC pp, Pb–Pb, Au–Au benchmarks are not
   printed; the EIC β*_y ≈ 7.2 cm is only implied by σ_z/β*_y ≈ 0.83 with σ_z ≈ 6 cm, and which beam's β*_y is meant is
   not stated.
4. The rules by which AloHEP derives the collision frequency and the storage time from the per-beam inputs are in the
   repository README only (p. 21), not in the paper.
5. Relation between github.com/tobbetuyef/AloHEP (MIT License, named in the paper) and the earlier-registered
   github.com/yefetu/ALOHEP (`SRC_URL_GITHUB_YEFETU_ALOHEP`, no licence seen) is unknown; the licence of the paper itself is
   not stated in the PDF.
6. 'Potential-solve share ∼ 100%' (Table 1, 100³) is recorded as 100 percent with an approximation note; the exact figure is
   not printed.
7. The scenario is labelled `status: reported` (as the other batch-7/μLHC scenarios whose roles are mostly paper values)
   although two roles (beam energy, implied IP spot) are computed here; `partially_reported` would also be defensible.
8. Nothing in this group has been verified by running the code; the GitHub repository was not fetched (network policy).

## Validation after the corrections

`tools/validate_yaml.py provenance` → 0 errors (251 records); `tools/validate_yaml.py machine` → 0 errors;
`python -m lhmuc validate` → 0 errors, 0 warnings; `pytest tests/scientific/test_batch7_documents.py` → 14 passed.
Confidence: 245 high / 6 medium; validation: 202 P0 / 49 P1; status: 246 analogous / 5 analytical_estimate; reported_lhmuc: 0.
