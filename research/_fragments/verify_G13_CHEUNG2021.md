# Verification note: group G13_CHEUNG2021 (batch 9, 2026-10-28)

Source: SRC_ARXIV_2101_10476. K. Cheung and Z. S. Wang, "Physics potential of a muon-proton collider", arXiv:2101.10476v2 [hep-ph],
10 May 2021, 7 pp. (Phys. Rev. D 103, 116009 according to the source registry; the journal version was not read). Category
PEER_REVIEWED. The paper is not a PRIMARY_LHMUC source.

Files verified:

- `parameters/physics_programme/mup_physics_cheung2021.yaml`: 108 records at hand-over, 109 after verification (1 added, 0 removed).
- `parameters/machine/scenarios_batch9_cheung.yaml`: 2 scenarios, CHEUNG2021-MUP1-MUMINUS-P and CHEUNG2021-MUP2-MUMINUS-P.

Role: adversarial verifier. For every record I checked these fields against the cited page:

- value, unit, page, section, and table, figure or equation label;
- quotation, uncertainty and provenance status;
- the applicability caveat, scenario assignment, derivation and arithmetic;
- the validation label.

All seven PDF pages were read as page images. Tables I–IV and the Fig. 2 legends were re-rendered at 300–400 dpi
(`pdftoppm`) and read cell by cell. The p. 3 formulas and the p. 4 SMEFT paragraph were cropped and read the same way. The
verification scripts are outside the repository, in the session scratchpad under `verify_g13/scripts/` (`qcheck*.py`,
`apply_edits.py`, `apply_scen_edits.py`).

## What was checked and found correct

**All table cells.** Every printed cell of Tables I–IV matches the page image and the text layer:

| Table | μp-1 | μp-2 | Comparators |
|---|---|---|---|
| I (E_p, E_μ−, √s, L_int) | 7, 1, 5.3, 0.1 | 50, 3, 24.5, 1 | none |
| II, WW (pb) | 0.978 | 5.103 | LHeC 0.110 [13], FCC-he 0.577 [13], LHC-14 4.233 [42] |
| II, ZZ (pb) | 0.216 | 1.263 | LHeC 0.020 [13], FCC-he 0.127 [13] |
| III | 0.98, 4.67 pb, 0.99, 0.21, 0.022, 0.97 %, 0.69 % | 0.91, 25.1 pb, 0.97, 0.17, 0.018, 0.15 %, 0.50 % | none |
| IV | 120 pb, 1.29 × 10^-2 pb, 1.13 × 10^-8 | 30 pb, 3.15 × 10^-1 pb, 9.10 × 10^-10 | none |

- The LHC-14 cell "4.233 [42]" is printed once, vertically centred across the WW and ZZ rows. One record for it is correct.
- The Table III header prints ε^{pr-cut}_{zbb} (lower-case z), while the p. 3 text writes ε^{pr-cut}_{Zbb}. Both are transcribed as
  printed.
- The Table IV signal column is σ^sig × (Λ²/(100 TeV² C_T^μc))², as printed. The record names and notes state this normalisation
  correctly.

**Text values** were all found on the cited pages with the stated wording:

| Topic | Values |
|---|---|
| Luminosity and running (p. 2) | 1e33 and 1e34 cm^-2 s^-1; 10^7 s/year; 10 years |
| DIS reach (p. 1) | Q² of order 10^7 GeV² at a CM energy of 5 TeV |
| h → bb̄ selection | p_T > 5 GeV; \|η\| < 5.5; b-tag 75 %; exactly two b-jets; \|m_bb − m_h\| < 25 GeV; m_h = 125 GeV |
| FCC-ee inputs (p. 3) | 0.4 %, 0.9 %, 0.985 % |
| Δg_hbb/g_hbb comparators (p. 3) | LHeC 0.97 %; CMS 4 % with 3 ab^-1 |
| RPV bounds (p. 3) | 0.090 m/1 TeV + 0.014; 0.053 m/1 TeV + 0.029 |
| RPV statements | S = 2; λ′_21k down to 0.02 (0.01); FCC-hh about 10 TeV; muon-collider leptoquark mass of the order of 10 TeV |
| Muon g−2 (pp. 4–5) | 251(59) × 10^-11; ∼ 4.2σ; v = 246 GeV; Br ∼ 10^-13; Δa_μ ∼ 3 × 10^-9; roughly 10^5 and 5 × 10^6 Higgs events; Λ ≲ 10 TeV; Λ = 10 TeV in the logarithm; ∼ 100 % and ∼ 70 % below m_μc = 5 TeV |

The Fig. 2 legend thresholds are printed analysis settings, not curve values: 0.0, 0.5 and 1.0 TeV for μp-1, plus 1.5 TeV for
μp-2. No curve of Fig. 1 or Fig. 2 was digitised.

**Quotations.**

- I ran my own independent check of every quotation piece against the text layer: character 3-gram windows after removing
  whitespace and hyphens, over all pages.
- Twenty-three records keep flags. All of them are text-layer artefacts:
  - garbled mathematics (ε^{pr-cut}, g²_hWW/Γ_h, λ′ rendered as "λ0", 251(59) × 10^−11, the |Δa_μ| formula);
  - two-column interleaving ("measure-|ment", "exper-|imental", "strategies,|should be");
  - page breaks (p. 2/3, p. 3/4, p. 4/5);
  - footnote markers left out of the quotes ("model file⁴", "side²").
- I checked each flagged formula against the page images.
- The quoted fragments inside the notes and explanations were checked by eye. They include:
  - the p. 1 BIB motivation and the p. 3 Fig. 2 sentence;
  - footnotes 4 and 5;
  - the 'source says …' uncertainty notes.
- No flattened superscripts were found (for example "1033" for 10^33, or "ab−1"). The extractor used "^" throughout.

**Provenance.**

- No record carries reported_lhmuc.
- 103 records are imported_related with screening_only, 2 are analytical_estimate with screening_only, and 4 are unknown with
  value null and category unresolved.
- Every record's explanation carries the required caveats: the paper studies NEGATIVE muons (Table I header E_µ−), LHμC collides
  μ+p, and the 1e33 and 1e34 luminosities are the authors' assumptions.
- Every restated comparator names its original reference, and each one was checked against the bibliography on pp. 5–7:
  [13], [24], [32], [37], [42], [50]–[53], [67]–[69], [70]–[73].

**Arithmetic, re-done independently.** All of the following agree with the extractor's figures:

| Check | Result |
|---|---|
| √s = 2√(E_p E_μ) | 5.2915 TeV (−0.16 %) and 24.495 TeV (−0.02 %) |
| L_int | 1e33 × 1e7 × 10 = 1e41 cm^-2 = 0.1 ab^-1 (and 1 ab^-1 for μp-2) |
| L_int per year | 10 and 100 fb^-1 |
| Quadrature of the FCC-ee inputs | √(0.4² + 0.9²) = 0.98489 % |
| Δg_hbb/g_hbb = ½√(Δσ/σ)² + 0.985²) | 0.691 % and 0.498 % |
| Higgs yields (WW only) | 0.978 × 1e5 = 9.78e4 and 5.103 × 1e6 = 5.10e6; adding ZZ gives 1.19e5 and 6.37e6, so the paper's "roughly 10^5 and 5 × 10^6" matches WW only |
| Cut flow with external branching ratios 0.58 and 0.1512, μp-1 | N_s = 11 674, N_b = 1 538, Δσ/σ = 0.985 % |
| Cut flow, μp-2 | N_s = 457 872, N_b = 66 263, Δσ/σ = 0.158 % |
| Table IV audit, μp-1 (m_c = 1.27 GeV external, S = 2) | N_s = 6 928.2, C/Λ² = 0.023175 TeV^-2, \|Δa_μ\| = 1.1307e-8 (printed 1.13e-8, +0.06 %) |
| Table IV audit, μp-2 | C/Λ² = 0.0018648 TeV^-2, \|Δa_μ\| = 9.098e-10 (printed 9.10e-10, −0.02 %) |
| Other ratios | Table II ratios 8.89 / 8.84 / 10.8 / 9.94 / 0.282 / 1.504; 251/59 = 4.25; RPV formulas 0.104 and 0.082 at 1 TeV; Q²_max = s = 2.5e7 GeV² at 5 TeV |

**Tests.**

- The five tests cited as P1 exist under exactly these names in `tests/scientific/test_batch9_documents.py`, and they pass:
  - `test_cheung2021_table1_centre_of_mass_energies`
  - `test_cheung2021_integrated_luminosity_from_assumed_peak`
  - `test_cheung2021_hbb_coupling_precision`
  - `test_cheung2021_higgs_yields`
  - `test_cheung2021_cut_flow_reproduces_delta_sigma_band`
- No P1 record lacks check_ids, and no P0 record carries any.

**Ids, units and validation.**

- All ids end in `_CHEUNG2021` and collide with nothing in the registry.
- Every unit parses through `lhmuc/units.py`: TeV, GeV, GeV^2, pb, ab^-1, cm^-2 s^-1, s/year, year, fb^-1/year, percent, events,
  dimensionless.
- Each record's `scenario` equals its `applicability.scenario`, and each scenario role points at a record of the same scenario
  or a shared one (scenario null).
- The LHμC cross-references in the notes exist with the stated values: PROTON_BEAM_ENERGY_DIS2026 = 7 TeV,
  MACHINE_MU_BEAM_ENERGY_DIS2026 = 1 TeV, MACHINE_SQRT_S_DIS2026 = 5.3 TeV.
- No LHμC scenario has the μp-2 energies (3 TeV μ, 50 TeV p).

## Corrections made

All corrections were made in place; no parameter_id was changed.

1. **"W W" changed to the printed "WW" in 14 quotation spans.** The text layer splits the italic WW. The page reads "the WW and ZZ
   vector-boson-fusion", "the WW VBF process", "the corresponding WW VBF for Z-boson production" and "Br(h → WW)". Records affected:
   - MACHINE_MUON_CHARGE_CHEUNG2021
   - PHYS_VBF_HIGGS_XSEC_WW_MUPLUS_P_7TEV_1TEV_CHEUNG2021
   - PHYS_HBB_SIGNAL_PROCESS_CHEUNG2021 (2 spans)
   - PHYS_HBB_BACKGROUND_PROCESS_CHEUNG2021
   - PHYS_FCCEE_ZH_XSEC_PRECISION_CHEUNG2021, PHYS_FCCEE_ZH_XSEC_TIMES_BR_WW_PRECISION_CHEUNG2021 and
     PHYS_HWW_OVER_GAMMA_PRECISION_CHEUNG2021 (3 spans each)
2. **Two per-year luminosity records lowered from P1 to P0, with check_ids emptied.**
   - The records are MACHINE_INTEGRATED_LUMINOSITY_PER_YEAR_MUP1_CHEUNG2021 (10 fb^-1/yr) and
     MACHINE_INTEGRATED_LUMINOSITY_PER_YEAR_MUP2_CHEUNG2021 (100 fb^-1/yr).
   - The cited test `test_cheung2021_integrated_luminosity_from_assumed_peak` asserts only the 10-year product, 0.1 and 1 ab^-1.
     It does not assert the per-year intermediate.
   - `docs/validation_plan.md` rule 1 says that "a level is claimed only for the specific quantity … the check covers".
   - The values, analytical_estimate status and derivations are unchanged, and are arithmetically correct. The consistency
     arithmetic stays in `methods`, and the reason for the level is in `validation.notes`.
   - P1 records: 13 → 11.
3. **PHYS_VBF_HIGGS_XSEC_LHC14_CHEUNG2021: attribution reworded.**
   - The extractor called ref. [42] the "LHC Higgs cross-section working group web page".
   - The paper prints only "CERNYellowReportPageAt1314TeV2014, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/…" and names no
     group.
   - The explanation now quotes the printed reference and says that no group, version or date is given.
4. **PHYS_G2_BKG_XSEC_MUP1_CHEUNG2021 and PHYS_G2_BKG_XSEC_MUP2_CHEUNG2021: notes made neutral.**
   - The extractor wrote that "the paper gives no further selection that would explain" 30 pb (μp-2) < 120 pb (μp-1).
   - In fact the paper states the parton-level cuts p_T^j > 5 GeV and |η^j| < 5.5 for both set-ups. Their acceptance differs at
     the more asymmetric 50 × 3 TeV set-up, and whether that accounts for the drop cannot be decided without a generator run.
   - Both cells were re-read at 400 dpi and are correctly transcribed. They must still not be rescaled.
5. **PHYS_RPV_FCCHH_SQUARK_REACH_CHEUNG2021: attribution corrected.**
   - The author string is now as printed: "J. I. Loukas Gouskos, Allan Sung". The extractor's "FCC-hh talk, 2018" was inferred
     from the file name, which is now named instead.
   - New caveat: ref. [69] is titled "Top squark searches at 100 TeV", whereas the sentence speaks of "SUSY squarks". The 10 TeV
     figure was not checked against ref. [69].
6. **PHYS_RPV_LHC_BOUND_36FB_CHEUNG2021 and PHYS_RPV_HLLHC_BOUND_3AB_CHEUNG2021: notes added.**
   - Which inequality is the current (36 fb^-1) bound and which is the projected (3 ab^-1) bound follows only from the word order
     of the p. 3 sentence. The paper does not label them individually.
   - The Fig. 2 red curves (solid and dashed) are named and were not digitised.
7. **Scenarios: `status: reported` changed to `partially_reported` for both.**
   - The paper prints only beam energies, √s, the assumed peak luminosities and the run-time benchmark.
   - 35 machine roles are unknown.
   - The `integrated_luminosity_per_year` role is our analytical_estimate, not a printed value. The extractor's own definition
     ("as printed in Table I") did not hold.
   - This follows the registry convention: LHMUC-DIS2026-1TEV, MUIC-ACOSTA2022-MUIC2 and LHMUC-WS2026-FORTHOMME are all
     partially_reported.
   - The scenario notes now:
     - mark the per-year role as P0;
     - say that the μp-1 energies also equal those of LHMUC-WP-BASELINE-1TEV and LHMUC-DIHIGGS-1TEV, both of which I checked
       are μ+ on 7 TeV p;
     - separate the charge difference (from all three) from the luminosity-basis difference (from DIS2026).
   - validation_level stays P1, because √s and L_int are covered by registered tests.
8. **File header comments** in both files were updated to describe this verifier pass.

## Added

- **PHYS_G2_SMEFT_VALIDITY_SCALE_CHEUNG2021** (p. 4, Sec. V). The record holds the SMEFT validity condition, quoted from the page
  image: "If the NP scale, Λ, is much higher than the EW scale, i.e., Λ ≫ 1 TeV, we can describe physics at energies much below Λ
  with the framework of the Standard Model Effective Field Theory (SMEFT) [74–77]".
  - Record fields: categorical, imported_related, screening_only, P0, confidence high, with the standard μ−/μ+ and luminosity
    caveat.
  - It pairs with PHYS_G2_UNITARITY_LAMBDA_MAX_CHEUNG2021 (Λ ≲ 10 TeV). The note says that the paper does not itself combine the
    two statements.

## Removed

None. Every record at hand-over is supported by the cited page. No value was fabricated, rounded beyond the printed precision,
digitised from a plot or mis-attributed. The four unknown records stay null, and they are legitimate, explicit unknowns:

- the μ+p WW-fusion cross section at 7 × 1 TeV;
- Br(h → bb̄) and Br(Z → bb̄) as used in N_s and N_b;
- the m_c used in the |Δa_μ| conversion.

## Residual doubts and follow-ups for the parent

These cannot be resolved from this document, the network is blocked, and they lie outside this group's files.

1. **The P1 claims are not yet backed by registry rows.** `docs/validation_plan.md` requires a P1 check to be listed in
   `registries/validation_registry.csv`, which has no rows for the five Cheung tests. The authored registry was not edited by
   this verifier. The parent should add rows for the five tests, or lower the 11 P1 records.
2. **The Δσ/σ P1 (PHYS_HBB_XSEC_PRECISION_MUP1/MUP2) is a band.**
   - It rests on two external constants that are not registry parameters: Br(h→bb̄) = 0.58 and Br(Z→bb̄) = 0.1512.
   - The paper's own branching ratios are unknown, and the test reproduces the printed values to ratios of 1.015 and 1.054.
   - I kept P1, in line with the test docstring and with the precedent of the PDG constants in CHK_P1_GAMMA_TAU_1TEV. Under a
     strict reading of the P1 entry criterion ("inputs are themselves registry parameters"), the parent may prefer P0.
3. **Table IV σ^bgd.** 30 pb (μp-2) < 120 pb (μp-1) is unexplained in the paper. It is not a transcription error. Do not rescale.
4. **Inconsistencies inside the paper**, kept as printed:
   - Fig. 2's lower panel says "LHC 3000 fb^-1", while the upper panel says "HL−LHC 3000 fb^-1".
   - The Table IV caption mentions integrated luminosities, but the table has no luminosity column.
   - "where performed" and "the the" are typos in the original.
5. **The 2σ criterion of Sec. V is not defined there.** The S = N_s/√N_b of Sec. IV reproduces Table IV only together with an
   external m_c of 1.27 GeV. The Table IV audit is a candidate P1 test, but only if m_c is first registered as an external
   constant.
6. **Comparators were not checked against their original references.** No local copies exist, and the network is blocked:
   - [13] LHeC/FCC-he 0.110 / 0.577 / 0.020 / 0.127 pb (arXiv:2007.14491 is registered but not archived);
   - [42] LHC-14 4.233 pb;
   - [50] FCC-ee 0.4 % and 0.9 %;
   - [51] LHeC 0.97 %;
   - [52, 53] CMS 4 %;
   - [67] RPV bounds;
   - [69] FCC-hh 10 TeV;
   - [32] leptoquark 10 TeV;
   - [70]–[73] g−2.

   The paper gives neither the perturbative order nor the beam energies behind them, while its own μp cells are leading order.
7. **Possible μ−p vs μ+p comparison at the same √s.** PHYS_HIGGS_WFUSION_XSEC_IMPLIED_MULHC is an analytical_estimate of
   385 fb at √s = 5.3 TeV, obtained from the μLHC paper's Table 6 yield divided by its Table 4 luminosity. Cheung's μ−p
   WW-fusion value is 978 fb (×2.5).
   - The two must not be averaged, and are not one quantity.
   - The charge (μ−p couples to u-type quarks in charged-current scattering, μ+p to d-type) plausibly explains much of the
     factor. However, I did not verify the polarisation, generator or selection behind the μLHC figure.
   - This is a candidate entry for `research/source_conflicts.yaml` (charge dependence) and for the μ+p generator computation
     listed as missing evidence.
8. **Different luminosity bases at the same 7 × 1 TeV energies.**
   - Cheung μp-1: 1e33 cm^-2 s^-1 assumed, 0.1 ab^-1.
   - LHMUC-DIS2026-1TEV: 2.1e34 cm^-2 s^-1.
   - LHMUC-WP-BASELINE-1TEV: 1000 fb^-1.

   These are separate machines with separate assumptions. Keep them as separate scenarios; do not reconcile them.
9. **Registry hygiene.**
   - `research/source_registry.yaml` still lists `parameters_extracted: []` for SRC_ARXIV_2101_10476.
   - The generated CSV registries must be rebuilt (`uv run python tools/build_registries.py`). Until then
     `tests/unit/test_registry_integrity.py::test_csv_registries_in_sync` fails, as expected. The other 110 tests in tests/unit
     and tests/scientific pass.

## Validation state after this pass

- `uv run python tools/validate_yaml.py provenance parameters/physics_programme/mup_physics_cheung2021.yaml`: 0 schema errors.
- `uv run python tools/validate_yaml.py machine parameters/machine/scenarios_batch9_cheung.yaml`: 0 schema errors.
- `uv run python -m lhmuc validate`: 0 errors, 0 warnings across the whole registry.
- Final counts: 109 records. Statuses: 103 imported_related, 2 analytical_estimate, 4 unknown, 0 reported_lhmuc. Validation:
  11 P1, 98 P0. Both scenarios are partially_reported, G0, P1.
