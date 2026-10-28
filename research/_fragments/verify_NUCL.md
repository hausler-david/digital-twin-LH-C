# Verification note — SRC_WS1681458_DAGLI_NUCLEUS (Canbay, Dagli et al., "LHμC: Nucleus Options", Kraków workshop slides, 16 pp.)

Verifier pass, 2026-10-28. Every parameter record in the four files written by the extraction agent was
checked against the cited page of `references/_local/LHuC_Nucleus_Options.pdf` (page images of pp. 4, 7, 8, 10,
12, 13, 14 rendered and read cell by cell; all 16 page-text files
`scratchpad/text/LHuC_Nucleus_Options_pNN.txt` read in full). Checked per record: value, unit, page, table/figure
label, quotation (verbatim or exact cell transcription), provenance status, confidence, scenario assignment,
dependencies, derivation strings and the hand-check arithmetic in the validation blocks.

Files checked (record counts before → after):

| file | before | after |
|---|---|---|
| parameters/machine/lhmuc_nucleus_options.yaml | 110 | 110 |
| parameters/ion_beam/lhc_ion_beams_nucleus_options.yaml | 57 | 57 |
| parameters/physics_programme/lhmuc_nucleus_options_physics.yaml | 18 | 18 |
| parameters/machine/scenarios_nucleus.yaml | 4 scenarios | 4 scenarios |

Overall verdict: 185 parameter records + 4 scenarios checked; **0 numerical transcription errors**,
**0 wrong pages or table labels**, **0 non-verbatim quotations** (table rows are quoted as
`Row label [unit] v_Pb v_Xe v_O v_Ne`, superscripts written as `10^x`, as the file header declares);
**1 provenance-status inconsistency** fixed, **9 uncertainty-type misuses** fixed, **1 metadata string
not supported by the document** fixed (185 records), **1 note added**; **0 records removed** (every value is
supported by the deck); **0 records added** (the deck's quantitative content is fully covered, see §5).
All four files validate with 0 schema errors (`tools/validate_yaml.py provenance|machine`).

## 1. Value / quotation checks (no corrections needed)

Every numeric value was re-read from the page image and the page text:

- p.4 headline boxes: 5.3 TeV, 7.2 × 10^33, 8.8 × 10^33 "(values after the erratum)", 72 fb^-1, 10^7 s,
  ≈ 2.8 × 10^4 Higgs, "1 TeV µ+ on 7 TeV protons: 4.5× the LHeC energy" — all as recorded.
- p.5 chain: 3 GeV / 2 MW / 50 Hz; 10 mm graphite, 40 crossings, 0.016 π per proton; 25 meV; 212 MeV,
  εn = 4 µm, 40 bunches of 4.5 × 10^10 (7.2 nC); "about 1 ms"; "about 10^5 times" — all as recorded.
- p.6: 2 × 1 km linacs, 10 GeV per pass, 20 GeV per turn, 50 turns, ≈ 1.4 ms, 1 km radius, vFFA — as recorded.
  The in-deck conflict "about 1 ms" (p.5) vs "≈ 1.4 ms" (p.6) is correctly kept as two records.
- p.7 chart: 140 / 743 / 3,320 GeV; caption "Eµ = 1 TeV on 2.76 TeV/u Pb; LHeC: 50 GeV e on 2.76 TeV/u Pb;
  EIC: 18 GeV e on 275 GeV/u Au; fixed target: Eµ = 470 GeV"; side boxes "Over ×20", "×4.5",
  "x ≈ 9 × 10^-7 reached at Q^2 = 10 GeV^2", "LHeC e–Pb: 1.8 × 10^-5; EIC e–Au: 1.3 × 10^-3" — as recorded.
- p.8 table (8 rows: 3.0 / 1000 / 3.0 / 0.7 / 2 / 4 / 40 / 4 / 3) and side boxes (4 MHz, ≈ 20 ms, about 2000
  turns, ≈ 0.64 N0, 50 Hz refills), caption "optics values from the µTRISTAN µ+e− design … β*µ ≈ 7–15 cm" — as
  recorded; the 3.0 / 0.7 cm β* are correctly `imported_related` (μTRISTAN) and `design_variant`.
- p.9: since 2010 / October 2017 / July 2025; √sAA = 5.44 TeV with 16 bunches; √sAA = 5.36 TeV with 62 bunches;
  "1200 bunches of 1.8 × 10^8 lead ions" — as recorded.
- p.10 table (4 columns × 10 rows, incl. Z/A headers 82/208, 54/129, 8/16, 10/20) — every cell verified:
  0.018/0.027/0.29/0.20; 574/350.88/42.88/53.60; 2.76/2.72/2.68/2.68; 0.10 ×4; 1.5/0.87/1.3/1.77;
  0.51/0.30/0.46/0.62; 1200/16/62/62; 11245 ×4; 26.659 ×4. "One assumption" and "Conservative baseline" boxes
  quoted verbatim.
- p.11: σ* = 5.5–7.9 µm, β*µ ≈ 7–15 cm, fc = min(4 MHz, nb × 11.245 kHz), Pb 4 MHz / O, Ne 0.70 MHz /
  Xe 0.18 MHz — as recorded.
- p.12 table (7 rows × 4 columns) — every cell verified: 47.9/37.5/13.1/14.6; 3.32/3.30/3.27/3.27;
  2.16/0.248/6.73/3.44; 4.49/0.32/1.08/0.69; 7.14/5.48/6.78/7.87; 4.00/3.95/6.29/5.42; 78.9/95.2/11.2/10.3.
  Caption "AloHEP with Nµ = 3.0 × 10^10 per bunch (Table 3 of the draft). L per nucleon = A × L.
  µTRISTAN-based values are in the backup." verbatim.
- p.13: reductions ÷ 8 / ÷ 10 / ÷ 1.12 / ÷ 1.03; "Stability limit ξA = 10 × 10^-3"; bar labels
  78.9/95.2/11.2/10.3 — as recorded.
- p.14 bar labels: before 449 / 32 / 108 / 68.8, after 56.9 / 3.36 / 96.1 / 66.8 (×10^30 per nucleon) — the
  four "after" records are correct; "≈ 1 × 10^32", "≈ 7 × 10^31", "÷ 10 … 16 bunches (fc = 0.18 MHz)" quoted.
- p.15: "50 turns, 67% survival, 40 bunches and 3.0 × 10^10 µ+ per bunch and 2000 turns in a 3 km main
  ring"; "exceed a luminosity of 10^32 cm^-2s^-1 per nucleon for all ions"; next steps — as recorded.

Independent recomputation (script, not the extractor's numbers) of every P1 hand check:
γμ = 9464.5, εμ = 0.4226 nm, τlab = 20.8 ms = 2078 turns, decay-averaging factor 0.642;
√s = 47.92 / 37.46 / 13.10 / 14.64 TeV; √s per nucleon 3.322 / 3.298 / 3.274 / 3.274 TeV;
fc = min(4 MHz, nb × 11.245 kHz) = 4.00 / 0.180 / 0.697 / 0.697 MHz; σ* = √(εA β*A) = 7.14 / 5.48 / 6.78 / 7.87 µm;
L = 0.64 fc Nμ NA/(4πσ²) = 2.158e30 / 2.473e29 / 6.747e30 / 3.454e30 cm^-2 s^-1 (deck: 2.16 / 0.248 / 6.73 / 3.44);
A × L = 4.49e32 / 3.19e31 / 1.08e32 / 6.91e31; β*μ = σ²/εμ = 12.1 / 7.1 / 10.9 / 14.7 cm (inside the stated
7–15 cm); ξμ = 4.02 / 3.97 / 6.32 / 5.45 ×10^-3 (deck 4.00 / 3.95 / 6.29 / 5.42); ξA = 78.4 / 94.5 / 11.1 / 10.3
×10^-3 (deck 78.9 / 95.2 / 11.2 / 10.3). All agree to ≤ 1 %, confirming the extractor's validation blocks and
the reading that the p.12 luminosities include the 0.64 N0 decay-averaging factor.

## 2. Corrections applied

| # | parameter_id(s) | field | before | after | reason |
|---|---|---|---|---|---|
| 1 | ACCEL_BOOSTER_SURVIVAL_NUCL | provenance.status, applicability.explanation | reported_lhmuc | imported_related (explanation says the 67 % is the μLHC-paper ERL-booster result restated under "µTRISTAN and LHeC based LHµC is taken as basis") | Inconsistent with the extractor's own policy: all other booster-chain records from the same p.5/p.6/p.15 statements (ACCEL_BOOSTER_TURNS_NUCL, _INJECTION_ENERGY_, _TOP_ENERGY_, _RAMP_TIME_, _LINAC_*) are imported_related; the survival fraction is a property of that imported booster, not an LHμC-nucleus-specific result. Upstream record: ACC_* survival records of the MULHC file. |
| 2 | ACCEL_BOOSTER_RAMP_TIME_P5_NUCL, ACCEL_BOOSTER_RAMP_TIME_P6_NUCL, MACHINE_MU_LIFETIME_LAB_NUCL, MACHINE_MU_LIFETIME_TURNS_NUCL, MACHINE_MU_TIME_AVERAGED_POPULATION_FRACTION_NUCL, MACHINE_SQRT_S_PER_NUCLEON_HEADLINE_NUCL, PHYS_HIGGS_PER_YEAR_WW_FUSION_MUP_NUCL, PHYS_FIXED_TARGET_X_LOWER_BOUND_NUCL, PHYS_X_MIN_MUPB_NUCL (9 records) | uncertainty.type (+note) | order_of_magnitude | not_stated, note "source marks the value as approximate ('…'); no numerical uncertainty is given and the approximation is not an order-of-magnitude uncertainty" | "about 1 ms", "≈ 20 ms", "≈ 0.64 N0", "~3.3 TeV", "≈ 2.8 × 10^4", "x ≈ 9 × 10^-7", "x ≳ 10^-3" are approximate statements, not factor-of-10 uncertainties; same convention as verify_DIS2026.md §5–10. SOURCE_MU_YIELD_GAIN_VS_JPARC_NUCL ("about 10^5 times") keeps order_of_magnitude because the value itself is an order-of-magnitude statement (consistent with the MULHC file). |
| 3 | all 185 records (3 files) | provenance.source.author_or_org | "… Institute of Physics Baku, CERN)" | "… Institute of Physics of the Ministry of Science and Education of Azerbaijan, CERN)" | The deck (p.1) says "Institute of Physics, Ministry of Science and Education, Azerbaijan"; "Baku" does not appear in the document and must not be added. |
| 4 | MACHINE_PEAK_LUMINOSITY_PER_NUCLEON_NUCL_NE | validation.notes, notes | '' / null | note that the p.14 chart prints the same "before" quantity as 68.8 × 10^30 (unrounded), the p.12 cell 0.69 × 10^32 being the rounded form; value kept as the table cell | Missed cross-reference; both numbers reproduce from 20 × 3.44e30. |

## 3. Status and scenario assignment (verified, no change)

- `reported_lhmuc` is used only for statements the PRIMARY_LHMUC deck makes about the LHμC nucleus options;
  confidence `high` only for table cells (p.8, p.10 headers, p.12, p.13), `medium` for text, chart labels and
  headline boxes, `low` for the "it appears possible to exceed 10^32" aspiration — consistent with the rules.
- `imported_related` is used for everything the deck itself imports and says so: μTRISTAN/μLHC production chain
  (p.5), LHeC ERL booster (p.6), μTRISTAN μ+e− optics 3.0/0.7 cm (p.8 caption), LHC ion beams from LHeC CDR 2021
  Table 4 / PDG tables (p.10 "Sources" box), LHeC e–Pb comparison numbers (p.7), the LHC operational √sAA values
  (p.9), and now the 67 % booster survival. `analogous` for EIC and fixed-target comparison numbers.
- The six `derived_lhmuc` records (μ+ geometric emittance, four matched β*μ, four reduced Nμ) all carry a
  derivation naming input ids and are reproduced here; they are clearly labelled "derived here, not stated by
  the deck". The scenario files map beta_x/y_star_muon to these derived records and list the reported
  per-species β*μ under unknown_roles, which is the honest encoding of "β*µ ≈ 7–15 cm".
- Scenario assignment: species-specific records carry LHMUC-NUCL-MU-PB/XE/O/NE; μ+-complex records common to all
  four carry `scenario: null` with an explanation naming the four scenarios. Scenario files reference ids only
  (no numbers in `parameters`), `status: reported`, G0, P1 with the P1 justification in `notes`.

## 4. Residual doubts (not resolvable from the document)

- Whether the p.12 luminosities (and the p.4 7.2e33 / 8.8e33) are peak or time-averaged is not stated; the
  0.64 N0 factor is needed to reproduce the p.12 values, which is noted in the records but remains an
  interpretation.
- The "÷ 8 / ÷ 10" reductions are rounded versions of ξA/0.01 = 7.9 / 9.5; the Nμ actually used in the p.14
  AloHEP recalculation is not given (p.14 "after" values do not scale exactly with 1/factor).
- The μTRISTAN-booster variant of the μA table ("in the backup") is not in the uploaded 16 pages.
- The upstream LHeC CDR 2021 Table 4 / PDG collider tables were not consulted (network blocked); the ion
  records quote the deck only.
- EIC x_min = 1.3 × 10^-3 at Q^2 = 10 GeV^2 is not reproduced by Q^2/s at y = 1 (5.1 × 10^-4); recorded as
  stated with the discrepancy noted.
- The fixed-target reference "Eµ = 470 GeV" is not attributed to an experiment in the deck.
- The physical justification of the ξA ≤ 0.01 stability limit is not given in the deck.
- The "Institute of Physics … Azerbaijan" affiliation string is taken from p.1 as printed; the Indico
  contribution page (url in the records, per ref. [9] of arXiv:2610.35154) could not be fetched to confirm the
  contribution id.

## 5. Coverage check

All quantitative statements on pp. 2–15 were mapped to a record (p.2 "Up to 10^32 … per nucleon (µ–O, after
beam–beam limits)" and p.13 "O, Ne: marginal, 3–12%" are carried in applicability/notes of the corresponding
records rather than as separate records, since they restate p.14 / p.13 table values). No quantitative statement
was found that the extractor missed; nothing was added.

## 6. Validation

`uv run python tools/validate_yaml.py provenance|machine <file>`: 0 schema errors for each of the four files.
`uv run python -m lhmuc validate`: the four NUCL files produce no error or warning; the 2 repository-wide errors
(`proposal PROP_A_HNL_2610_28252: unknown source SRC_ARXIV_2610_28252`, `proposal PROP_B_2HDM_VLQ_2610_17801:
unknown source SRC_ARXIV_2610_17801`) come from other agents' theory-benchmark proposals whose sources are not
yet in `research/source_registry.yaml` (task #6 pending) and were not touched.
