# Verification note — SRC_WS_LEBOHO_KUMAR_DIHIGGS (tag Leboho_Kumar_Anomalous_Higgs_couplings_mu+p)

Verifier pass, 2026-10-28. Every parameter record in the three files written by the extraction
agent was checked against the PDF page image (Read with `pages=N` on
`references/_local/Leboho_Kumar_Anomalous_Higgs_couplings_mu+p.pdf`: pages 2, 3, 4, 6, 7, 8, 9,
11, 12, 13, 14, 15, 16, 22, 23, 24 viewed as images) and against the per-page text layer
(`…/scratchpad/text/Leboho_Kumar_Anomalous_Higgs_couplings_mu+p_pNN.txt`, all 24 pages read).

Files checked (278 records after this pass; 277 before):

- `parameters/physics_programme/lhmuc_dihiggs_benchmark.yaml` — 259 → 260 records
- `parameters/detector/lhmuc_dihiggs_analysis_assumptions.yaml` — 18 records
- `parameters/machine/scenarios_dihiggs.yaml` — 2 scenarios (unchanged)

## Method

1. Automated cell check: all 144 cut-flow cells (p.12, p.23, p.24: 6 rows × 8 columns × 3
   working points) were parsed from the text layer and compared with each record's `value`,
   `unit`, `page` and the cell string and full-row transcription inside `quotation`. 0 mismatches.
   The six tables (p.8, p.12, p.15, p.16, p.22, p.23, p.24) were then re-read cell by cell from
   the page images; the text layer and the images agree for every cell.
2. Every numeric value of the 278 records was searched verbatim on its cited page's text; the
   only three not found are benign ("13" is written "Thirteen-point", "−1.5" uses a Unicode
   minus, "100 percent" transcribes "ϵb = 1").
3. Arithmetic re-done: 2√(E_μE_p) = 3.742 / 5.292 TeV; Σ MC gen = 2 900 000; σ×1000 for the
   eight "Events / ab⁻¹" cells; 166.7×0.7⁴ = 40.02, ×0.6⁴ = 21.60, ×0.9⁴ = 109.37; all 18
   "Tot. Bkg" sums and all 18 + 5 S/√(S+B) values (within rounding; the p.22 "70%, 2%" row gives
   4.246 from rounded cells, left at P0 as the extractor noted); 22.27/166.7 = 0.1336;
   (0.01)²(0.7)² = 4.9e-5, (0.6)²(0.01)² = 3.6e-5, (0.9)²(0.01)² = 8.1e-5; 2√(60 GeV·50 TeV) =
   3.46 TeV; HL-LHC interval 1−0.26 = 0.74, 1+0.29 = 1.29; FCC-he 1.00−0.17 = 0.83, +0.24 = 1.24.
4. Provenance statuses: 258 reported_lhmuc (all from this PRIMARY_LHMUC deck), 18
   imported_related + screening_only (p.2 LHC σ_ggF/σ_VBF, p.4 FCC-he numbers, p.16
   ATLAS/CMS/HL-LHC/FCC comparators — none has a citation on the slides; correctly flagged), 1
   scan_variable with value null. Source title, author list, date (24 September 2026) and page
   count match the title page and the archived-metadata JSON. Scenario assignments
   (LHMUC-DIHIGGS-500GEV for everything downstream of p.8; LHMUC-DIHIGGS-1TEV only for the
   p.7 scan values) match the p.8 caption "Signal at Eμ = 500 GeV (√s = 3.74 TeV), the
   configuration of the cut-flow".

## Result

No value, unit, page, table label, status or scenario was refuted. Nothing was removed. The
corrections below concern quotation transcription and source attribution only.

## Corrections made (all in-place, parameter_ids unchanged)

1. **Superscripts flattened by the PDF text layer — restored in quotations (misleading as
   numbers).** The rendered slides read `× 0.7⁴ = 40.02` (p.12), `× 0.6⁴ = 21.60` (p.23),
   `× 0.9⁴ = 109.37` (p.24); the text layer, and therefore the extractor's quotations, read
   `× 0.74`, `× 0.64`, `× 0.94`, which are different numbers. Replaced by `× 0.7^4`, `× 0.6^4`,
   `× 0.9^4` in the caption part of all 144 cut-flow quotations and in
   PHYS_DIHIGGS_SIGNAL_EVENTS_PRETAG_500GEV_DIHIGGS (145 occurrences).
2. **p.8 cross-section exponents.** `1.67 × 10−1`, `4.15 × 10−1`, `5.36 × 10−1`, `5.82 × 10−1`,
   `3.20 × 101`, `7.96 × 102`, `1.24 × 100`, `1.38 × 100` (text layer; the last four read as 101,
   102, 100) replaced by `× 10^-1`, `× 10^1`, `× 10^2`, `× 10^0` in the 33 p.8 quotations
   (PHYS_DIHIGGS_XSEC_*, _EVENTS_*, _MCGEN_* records), matching the rendered `10⁻¹`, `10¹`,
   `10²`, `10⁰`. The record values themselves (0.167, 32.0, 796.0, 1.24, 0.415, 1.38, 0.536,
   0.582 fb) were already correct.
3. **Mistag-weight formulas (detector file).** `w = (ϵmis)2 · (ϵb)2 = (0.01)2 (0.7)2 = 4.9 × 10−5`
   → `(ϵmis)^2 · (ϵb)^2 = (0.01)^2 (0.7)^2 = 4.9 × 10^-5` (DET_DIHIGGS_MISTAG_WEIGHT_70_DIHIGGS,
   p.13 image verified); `ϵ2b ϵ2mis = (0.6)2 (0.01)2 = 3.6 × 10−5` and `(0.9)2 (0.01)2 = 8.1 × 10−5`
   → `ϵb^2 ϵmis^2 = (0.6)^2 (0.01)^2 = 3.6 × 10^-5` / `(0.9)^2 (0.01)^2 = 8.1 × 10^-5`
   (DET_DIHIGGS_MISTAG_WEIGHT_60/90_DIHIGGS, p.23/p.24 images verified); `(ϵ4b for four-b final
   states)` → `(ϵb^4 …)` in the three p.9 b-tagging quotations (DET_DIHIGGS_ANALYSIS_LEVEL_,
   _BTAG_EFF_NOMINAL_, _MISTAG_RATE_NOMINAL_DIHIGGS).
4. **PHYS_DIHIGGS_LAMBDA_SM_DIHIGGS quotation.** `λSM = mh2/2v2 ≈ 0.13` → `λSM = mh^2/2v^2 ≈ 0.13`
   (p.3 image: m_h²/2v²).
   The text-layer forms `ab−1`, `fb−1`, `√s`, `S/√S+B` were left as they are: they are the
   convention used in the other verified parameter files of this repository and are not
   readable as different numbers.
5. **Source attribution caveat (all 277 records, `source.version`).** The records give the
   Indico URL `…/event/1681458/contributions/7263322/` and the workshop name as if established.
   `research/source_registry.yaml` and `research/archived_metadata/SRC_WS_LEBOHO_KUMAR_DIHIGGS.json`
   record that this mapping (file 'Krakow_Updated_Presentation', title page dated "24 September
   2026 • University of Witwatersrand") to contribution 7263322 "Status of Di-Higgs at LHμC" is
   *inferred, not verified*. The version string of every record now says so and points to the
   registry; the URL itself was kept so that the records stay consistent with the registry entry.

## Added (1 record)

- **PHYS_DIHIGGS_MISTAG_YIELD_AFTER_CUTS_APPROX_DIHIGGS** — p.13: "This replaces the unphysical
  zero with a small, defensible yield (≈ 0.03 events after all cuts) …". 0.03 events,
  reported_lhmuc, confidence medium (text value), P1 by consistency with the p.12 cell 0.033;
  dependency PHYS_DIHIGGS_CUTFLOW70_HWIN_MISTAG_DIHIGGS. The extractor had recorded only the
  table cell.

## Checked and left as extracted (worth stating)

- p.9 pairing ("minimising the distance to m_h = 125 GeV") vs p.17 ("Truth-based b-pairing …
  no mass bias"): both preserved on DET_DIHIGGS_HIGGS_CANDIDATE_PAIRING_DIHIGGS, confidence
  medium — confirmed on both page images; the slides do not reconcile them.
- p.12 Tot. Bkg 5.19 vs p.22 Background 5.18 vs text 5.2: separate records, rounding not a
  conflict (4.26+0.60+0.30+0.033 = 5.193) — confirmed.
- The 0.00 cells of the 4b column after the Higgs windows are physical zeros (p.14: "removed
  entirely"), not unknowns — confirmed.
- PHYS_DIHIGGS_LAMBDA_SM_DIHIGGS (λ_SM ≈ 0.13) and PHYS_DIHIGGS_GHHH1_SM_DIHIGGS (= 1) are
  theory normalisations stated on the LHμC slides, kept reported_lhmuc with applicability
  explanations saying they are not collider parameters.
- The p.4 FCC-he e⁻p cut-flow table (Kumar et al., PLB 764 (2017), Table 2) was deliberately not
  transcribed: it is a third-party table reproduced on the slide; only its headline 7.5σ and the
  FCC-he configuration are recorded as imported_related + screening_only.
- Machine-level records (E_μ, E_p, √s, L) remain in the physics_programme file as the extractor
  documented; the scenario file references them by id.

## Residual doubts (not resolvable from the slides)

- Functional form of the 12% jet-energy smearing; what the 5% systematic applies to; whether the
  p.9 object cuts were applied at generation for the p.8 cross sections; MadGraph integration
  uncertainties (explicitly not quoted); no cut-flow, yields or limits for the 1 TeV
  configuration; p.16 comparator numbers quoted without citations; UFO model 'effdihiggs-v2'
  not public; the p.22 "70% b-tag, 2% mistag" significance 4.24 is not reproduced from the
  rounded table cells (4.246) — all already listed by the extractor and unchanged.
- The mapping of this deck to Indico contribution 7263322 is inferred (see correction 5).

## Validation

`uv run python tools/validate_yaml.py` — 0 schema errors for each of the three files.
`uv run python -m lhmuc validate` — 0 errors attributable to these files; the 2 repo-wide errors
(`PROP_A_HNL_2610_28252`, `PROP_B_2HDM_VLQ_2610_17801`: unknown sources SRC_ARXIV_2610_28252 /
SRC_ARXIV_2610_17801) come from proposal records in `theory/benchmarks/` owned by another agent
and were not touched.
