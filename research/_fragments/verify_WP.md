# Verification note — SRC_WS1681458_KHANPOUR_GAMMAGAMMA (tag Khanpour_Two-photon_physics_LHmuC)

Verifier pass, 2026-10-28. Every parameter record in the four files written by the extraction
agent was checked against the PDF page image (Read with `pages=N`, plus 300/400/600 dpi
`pdftoppm` crops of legends, insets and panel titles) and the per-page text layer.

Files checked (78 records after this pass; 74 before):

- `parameters/machine/helpcern_wp_working_points.yaml` — 18 records
- `parameters/physics_programme/lhmuc_two_photon_benchmarks.yaml` — 46 → 50 records
- `parameters/detector/lhmuc_two_photon_detector_requirements.yaml` — 10 records
- `parameters/machine/scenarios_wp.yaml` — 3 scenarios

## Result

No record was refuted. All values, units, page numbers, table labels, provenance statuses
(reported_lhmuc only for LHμC rows/columns; LHeC / LHC / FCC-μH comparators imported_related +
screening_only; existing CMS/ATLAS a_τ bounds imported_related + screening_only) and scenario
assignments are supported by the slides. Arithmetic cross-checks recorded in the files were
re-done: 2√(E_μE_p) = 3.74 / 5.29 / 7.48 TeV; 2√(50 GeV·7 TeV) = 1.18 TeV; 731/164 = 4.46,
221/19 = 11.6, 36.77/2.89 = 12.7, 2.23/0.0323 = 69.0; 0.037 pb·250 fb⁻¹ = 9250,
0.166 pb·250 fb⁻¹ = 41 500; 2·80.3692 GeV = 160.7 GeV. Nothing was removed.

Specifically re-read and confirmed: p.4 table and text (E_μ, E_p, √s, L_int, "From HELP4CERN
White Paper (in preparation)"); p.5 table (16 cells) and "Key comparisons" box; p.15 table
(50.4 / 58.5 / 70.3 pb, caption "W0 = 10 GeV") and legend; p.18 text, "Current LHC limits"
box and panel titles "LHeC@1.2 TeV" / "LHmuC@5.3 TeV"; p.19 table (0.037 / 0.166 pb), text
(2m_W ≃ 160 GeV, 250 fb⁻¹, 9.3×10³ / 4.2×10⁴) and legend (FCC-μH, E_μ = 500 GeV, E_p = 50 TeV);
p.21 insets (0.0394/0.0393, 0.0736/0.0735, 0.288/0.303 pb, f_M2/Λ⁴ = 1 TeV⁻⁴); p.22 legends;
p.3, p.10, p.11, p.25, p.26 text.

## Corrections made (all in-place, parameter_ids unchanged)

1. **MACHINE_SQRT_S_WP_OPT1 / _BASELINE / _OPT2 — `notes`.** The extractor had pasted one
   note on all three records claiming each value "appears in the p.15 and p.19 cross-section
   tables … and in the p.21 panel title" and is "identical to the DIS2026 proceedings values
   (MACHINE_SQRT_S_DIS2026 / MACHINE_SQRT_S_2TEV_DIS2026)". That is false for option 1 (3.7 TeV
   has no DIS2026 counterpart; not on p.21) and for option 2 (7.5 TeV appears only on p.4), and
   incomplete for the baseline (5.3 TeV is not in the p.19 table; it is in the p.18 panel
   title). Each note now states exactly where its value appears.
2. **Figure-legend quotations — dash, not minus sign.** The legends print `LHeC (e–p)`,
   `μLHC (μ–p)`, `FCC-μH (μ–p)` with a dash separator (verified at 300 dpi). The extractor
   transcribed a minus sign (`μ−p`), which could be read as a μ⁻ beam. Fixed in
   MACHINE_LHEC_P_BEAM_ENERGY_WP (quotation), MACHINE_FCCMUH_MU_BEAM_ENERGY_WP and
   MACHINE_FCCMUH_P_BEAM_ENERGY_WP (quotation), MACHINE_LHEC_SQRT_S_WP (notes), and the notes of
   PHYS_XSEC_EL_GG_TAUTAU_LHEC_WP / _LHMUC500_WP / _LHMUC1TEV_WP. The explanation of
   MACHINE_MU_BEAM_CHARGE_WP now says explicitly that the dash is not a charge sign.
3. **PHYS_XSEC_GEN_GG_WW_SM_LHMUC1TEV_AQGCFIG_WP and _EFT_… — `table_figure_or_equation`.**
   The p.21 LHμC panel title is `μLHC@5.3TeV: p(γ) ⊗ μ(γ)→W+W−` (verified at 300 dpi). The
   extractor had written `→μ(γ)W+W−` (an extra `μ(γ)` in the final state). Corrected.
4. **PHYS_EL_PHOTON_VIRTUALITY_CUT_WP — `applicability.explanation`.** Replaced "presumably
   p.12/13/22" by what was verified: p.12 and p.13 carry the same cut with a semicolon
   (`Q_ℓ² < M_Z² GeV²; Q_p² < M_Z² GeV²`) and label the curves `LHμC (μ–p)` (not `μLHC`); both
   p.22 panels carry the comma form.
5. **PROTON_BEAM_ENERGY_WP / MACHINE_LHEC_SQRT_S_WP — page lists.** `E_p = 7 TeV` legend
   occurrences extended from "p.12, p.15, p.19" to p.12, p.13, p.15, p.19, p.22 (verified).
6. **Detector file — hyphenation artefacts.** `signa-tures` and `disso-ciation` in the
   quotations of DET_GG_MISSING_MOMENTUM_WP, DET_GG_FORWARD_PROTON_TAGGING_WP and
   DET_GG_PROTON_DISSOCIATION_CONTROL_WP are end-of-line hyphenations of the PDF text layer,
   not slide text; replaced by `signatures` / `dissociation`. The shared `notes` string of all
   ten detector records now says so.
7. **scenarios_wp.yaml — LHMUC-WP-BASELINE-1TEV description.** Added the p.18 panel
   `LHmuC@5.3 TeV` to the list of places that use the baseline.

## Records added (missed by the extractor; quotable, read at 600 dpi)

The p.18 figure has, under each M_ττ distribution, a `Ratio (BSM/SM)` panel with a printed
linear fit. Four records added to `lhmuc_two_photon_benchmarks.yaml`:

| parameter_id | value | unit | quotation |
|---|---|---|---|
| PHYS_ATAU_RATIO_FIT_SLOPE_LHEC_WP | 0.0004 ± 0.0001 | GeV^-1 | `Fit: y = (0.0004 ± 0.0001)x + (1.0139 ± 0.0015),` |
| PHYS_ATAU_RATIO_FIT_INTERCEPT_LHEC_WP | 1.0139 ± 0.0015 | dimensionless | same |
| PHYS_ATAU_RATIO_FIT_SLOPE_LHMUC1TEV_WP | 0.0005 ± 0.0000 | GeV^-1 | `Fit: y = (0.0005 ± 0.0000)x + (1.0120 ± 0.0012),` |
| PHYS_ATAU_RATIO_FIT_INTERCEPT_LHMUC1TEV_WP | 1.0120 ± 0.0012 | dimensionless | same |

LHeC → imported_related / screening_only; LHμC (panel `LHmuC@5.3 TeV`) → reported_lhmuc,
scenario LHMUC-WP-BASELINE-1TEV. Confidence medium (figure-inset read). The x variable is the
panel's shared abscissa M_ττ in GeV, hence the slope unit; fit range, binning and generator are
not stated, and the slide itself says a projected limit "still requires a dedicated
detector-level statistical analysis". The LHμC slope uncertainty is recorded as 0.0 only
because the slide prints `± 0.0000`; this is a rounding artefact, not a zero uncertainty.

## Removed

None.

## Residual doubts / points for the lead

- The `order_of_magnitude` uncertainty type on the `∼ 4.5 / 12 / 13 / 69` enhancement factors
  and on the `≃ 9.3×10³ / 4.2×10⁴` counts follows the lead's instruction; the actual rounding
  is percent-level (recorded in `validation.notes`). A `relative_fraction` type would describe
  the source better.
- PHYS_WW_THRESHOLD_WGG_WP is `analytical_estimate` although the 160 GeV is printed on the
  slide; defensible either way (the derivation 2m_W is also printed).
- Existing CMS/ATLAS a_τ bounds are filed as `imported_related` (closest enum value); they are
  measurements, not a related proposal.
- The in-source discrepancy LHeC σ(γγ→W⁺W⁻) 0.037 pb (p.19 table) vs σ_gen 0.0394 pb (p.21
  inset) and the naming inconsistency `LHμC` (p.12/13 legends, p.18 `LHmuC`) vs `μLHC`
  (p.15/19/21 legends and panel) are confirmed and remain for `research/source_conflicts.yaml`.
- `research/source_registry.yaml` entry SRC_WS1681458_KHANPOUR_GAMMAGAMMA still has
  `parameters_extracted: []` (not this verifier's file).

## Validation

`uv run python tools/validate_yaml.py` → 0 schema errors for each of the four files.
`uv run python -m lhmuc validate` → 2 errors, both outside these files (proposals
PROP_A_HNL_2610_28252 and PROP_B_2HDM_VLQ_2610_17801 reference unknown source ids); the WP
files contribute 0 errors and 0 warnings.
