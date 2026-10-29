# Verification note: group G12_BAKULE2013 (batch 9, 2026-10-28)

Source: SRC_ARXIV_1306_3810. P. Bakule et al. (31 authors), "Measurement of muonium emission from silica aerogel",
arXiv:1306.3810v1 [physics.atom-ph], 17 Jun 2013, 11 pp. (PTEP 2013 103C01 according to the source registry; the journal
version was not read, and the arXiv p. 1 header still carries the template line "Prog. Theor. Exp. Phys. 2012, 00000").
Category PEER_REVIEWED. The paper is not a PRIMARY_LHMUC source.

File verified:

- `parameters/source/muonium_emission_aerogel_bakule2013.yaml`: 101 records at hand-over, 101 after verification
  (0 added, 0 removed, 13 records corrected, header extended by two comment lines).
- No scenario file belongs to this group. Every record has `scenario: null`, which is right: no value is an LHμC scenario
  value, and no scenario file in `parameters/machine/` maps a role to a `_BAKULE2013` id.

Role: adversarial verifier. For every record I checked value, unit, page, section, table/figure/equation label, quotation,
uncertainty, provenance status and applicability, scenario, derivation, dependencies, validation label and notes.

## Method

1. **Page images.** All 11 pages were read as page images (`Read` with `pages=N`). Table 1 (p. 8), the Fig. 5 legend and
   Table 2 (p. 9) and eq. (1) with the surrounding p. 10 text were re-rendered at 300 dpi with `pdftoppm` and read cell by cell.
2. **Quotations.** Every quotation was split at the extractor's markers (`[p. N]`, `[§…]`, `[text, p. 8]`,
   `[Fig. 1 caption]`, `[...]`) and each sentence was searched in the normalised text layer (`…/scratchpad/text/
   arXiv-1306.3810v1_pNN.txt`). The 15 sentences not found verbatim are all text-layer artefacts, and each was confirmed on
   the page image:
   - page-break joins: p. 2→3 "reduced differences in | target mass", p. 4→5 "momentum | ends";
   - the stacked fraction dz/dx on p. 5;
   - the line-broken "poten-tial model" on p. 8;
   - superscript/subscript uncertainties on p. 8;
   - the displaced √L on p. 9;
   - the fraction ∆p/p on p. 10;
   - eq. (1).
   A second pass confirmed that every sentence lies on a page listed in the record's `page` field.
3. **Cross-references.** Every parameter id and source id named anywhere in the file resolves (`lhmuc.registry.load_all`,
   `research/source_registry.yaml`). The cross-document statements in the notes were checked on the other uploads' text layers:
   - Beare et al. 2020: p. 25 quotation and ref. [14] = Bakule PTEP 2013; p. 7 "diffusion length of about 30 µm";
   - Aritome et al. 2024: p. 2 "52% [21]", ref. [21] = Bakule PTEP 2013, S2 area, 28 and 0.46 MeV/c from G4BEAMLINE;
   - Abe et al. 2019: p. 7 "27 MeV/c … 5% (RMS)" at the end of the beamline (H-line), Bakule = ref. [29] on pp. 7–8, the
     p. 9 "0.52" without a reference;
   - the Zhang deck records ('0.52 (from TRIUMF measurement)', '~7mm /μs').
4. **Arithmetic** was recomputed independently:
   - eq. (1): 4.8e-3 × (0.02/0.05) × (23/28)^3.5 = 9.645e-4 (scale factor 0.2009);
   - α = −1.5 scaling from (29 mg cm^−3, 0.226 µm): 0.1095 µm at 47, 0.0369 µm at 97, 0.01486 µm at 178 mg cm^−3,
     2.97 × the measured 0.0050 µm;
   - (0.655 − 0.52)/hypot(0.01, 0.018) = 6.556 σ, and 7.50 σ with Beare's uncertainty alone;
   - α/2 + α_µ = 0.25;
   - sqrt(5²/12 + 1.5²) = 2.082 %;
   - 3/(2.2 g cm^−3 · S) = 2.48, 2.20, 1.90, 1.49 nm for S = 550, 620, 716, 914 m² g^−1;
   - the one-dimensional rms speed of Mu at 295 K = 4.64 mm/µs;
   - per-stop conversions of the Table 1 yields and their uncertainties.
   All of them agree with what the file states.
5. **Tests and validation.**
   - Tests: the four `test_bakule2013_*` tests in `tests/scientific/test_batch9_documents.py` and
     `tests/scientific/test_workshop_decks.py::test_muonium_formation_fraction_two_values_are_incompatible` pass.
   - `tools/validate_yaml.py provenance` on the file: 0 errors. `python -m lhmuc validate`: 0 errors, 0 warnings.
   - `tests/unit`: 49 passed, 1 failed. The failure is `test_csv_registries_in_sync`: `registries/` has not been rebuilt for
     the batch-9 files, and `registries/` is outside this verifier's remit.

## Checked and found correct

- **Table 1 (p. 8), every cell.**
  - Yields per 1000 muon stops: 2.74 ± 0.11 +0.10/−0.13, 2.81 ± 0.11 +0.14/−0.08, 3.13 ± 0.20 +0.12/−0.09 and
    1.60 ± 0.11 +0.07/−0.10.
  - Mean free paths (µm, small chemical potential model): 0.226±0.016 +0.113/−0.079, 0.118±0.009 +0.060/−0.034,
    0.035±0.004 +0.018/−0.012 and 0.0050±0.0007 +0.0020/−0.0014.
  - Yields are stored per stopped muon, with σ_stat in `gaussian_sigma` and the asymmetric systematic error in the note.
    No printed uncertainty is dropped.
- **Table 2 (p. 9), every cell:** 550/2.5, 620/2.2, 716/1.9 and 914/1.5 (m² g^−1 / nm).
- **Fig. 5 legend:** α = −1.0 solid, −1.5 dotted, −2.0 dashed. The line-style attributions in the α records are correct, and
  no curve is digitised.
- **Text values** were all found on the cited pages:
  - §2: 4 samples; 100 × 100 mm²; 30 × 40 mm² with the longer side vertical; 29/47/97/178 mg cm^−3;
    6.9/4.8/2.2/2.0 mm.
  - §3.1: 0.64 ± 0.03 [13]; 0.21 ± 0.01; 0.52 ± 0.01; "of order 0.05 µs^−1"; 0.6 mT; 0.50(1) and 4.57(3) × 10^16;
    "nearly 100%".
  - §3.2.1: 10 mm hole; 300 µm; ∼23 MeV/c; 5 % and 1.5 %; approximately half; 22.9/23.2/23.1/24.5 MeV/c; 4 pairs, 4 mm,
    80 wires, 4 mm pitch; ~5 mm/µs and 2.2 µs; "a few mm or less"; 0.2 mm; RoentDek HEX40 MCP.
  - §3.2.2: > 95 %; ±20 mm; |dz/dx| < 0.1; 30 MeV; 2 mm (σ); 0.1 mm plate; 1 ns (σ); −8.4 to 40 mm; regions 10/20/30/40 mm;
    400 K, 0.3 eV [20], 25 meV; 10 %; α_µ = +1.0; α/2 + α_µ; α = −1.0 and the α < −2.0 limit.
  - §4: 4.8 × 10^−3 per incident muon at 23 MeV/c and 2 % (RMS); 28 MeV/c and 5 % (RMS); p^3.5; 9.6 × 10^−4; e^−1 at
    30 µm; "a few millimeters"; 100 µm.
- **Statuses.**
  - No record is `reported_lhmuc`. 96 are `analogous`, 4 `unknown` with value null, and 1 `analytical_estimate`.
  - The analytical estimate is α/2 + α_µ = +0.25. Its derivation names its three input ids.
  - The restated values keep `analogous` and name the original reference in `applicability.explanation`: 0.64 ± 0.03 from
    ref. [13] (Kiefl 1979), 0.3 eV from ref. [20] (Antognini 2012), α_µ ("It is known"), the 2.2 µs muon lifetime, and
    the J-PARC 28 MeV/c and 5 %.
- **P1 labels** cite test names that exist and pass. The four P1 records are:
  - `SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAKULE2013`;
  - `SOURCE_MU_THERMAL_VELOCITY_BAKULE2013`;
  - `SOURCE_AEROGEL_DENSITY_SCALING_ALPHA_BAKULE2013`;
  - `SOURCE_MU_VACUUM_YIELD_JPARC_SCALED_BAKULE2013`.
- **Coverage.** Every number printed in the paper (pp. 1–11) is either extracted or deliberately left out. The deliberate omissions are
  the §1 background (3.5σ, 0.54 ppm, and 1.4 MHz at 10^−4 T, the muonium precession frequency) and the p. 11 grant number.
  I found no missed quantitative statement worth adding.

## Corrections (all ids kept)

| # | Record | Change | Reason |
|---|---|---|---|
| 1 | `SOURCE_MUSR_OXYGEN_CONCENTRATION_FIG1B_BAKULE2013` | confidence high → medium; notes reworded | The stored unit molecule/centimeter**3 is an interpretation of the printed 'mol cm^−3'. The literal moles reading is physically impossible, so the extractor's reading is kept, but the unit is not "read directly" (batch-9 rule for `high`). The notes now say that 'mol' = molecules is an inference. |
| 2 | `SOURCE_MUSR_OXYGEN_CONCENTRATION_FIG1C_BAKULE2013` | same as 1 | same |
| 3 | `SOURCE_VETO_COUNTER_HOLE_SIZE_BAKULE2013` | symbol `d_veto` → null; note extended | The symbol implied a diameter, which the paper does not state ("10 mm hole"). |
| 4 | `SOURCE_MU_BEAM_TRANSVERSE_SIZE_M15_BAKULE2013` | symbol `sigma_xy` → null; note extended | The symbol implied a Gaussian σ. The paper speaks only of "transverse dimensions" and gives no value. |
| 5 | `SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAKULE2013` | notes rewritten; second check id added | The notes called this paper "the origin" of every downstream 0.52, but only Beare 2020 (ref. [14]) and Aritome 2024 (ref. [21]) cite it directly. For Abe 2019 (0.52 on p. 9 without a reference), the Zhang deck ("from TRIUMF measurement") and μTRISTAN 2022 (numbers from C. Zhang), the origin is now marked as inferred. The notes also add that the MuSR facility is not named. `tests/scientific/test_workshop_decks.py::test_muonium_formation_fraction_two_values_are_incompatible` was added to `check_ids` and `methods` for consistency with the Beare and Zhang records. `validation.notes` now states that P1 certifies only the discrepancy arithmetic. |
| 6 | `SOURCE_MU_THERMAL_VELOCITY_BAKULE2013` | `validation.notes` added | The test uses 295 K, which is not a registry value: the temperature record is null. The new note states that the factor-2 band passes for any temperature from about 86 K to about 1370 K, so the unstated "room temperature" does not decide the outcome. It also states that the 295 K mean (7.4 mm/µs) and most-probable (6.6 mm/µs) speeds also pass. |
| 7 | `SOURCE_MUONIUM_DIFFUSION_MODEL_NAIVE_BAKULE2013` | value "free parameter = mean free path" → "a model parameter is the mean free path between collisions" | The paper says "A parameter in this model is the mean free path between collisions"; it does not say "free" or "the only" parameter. |
| 8 | `SOURCE_MU_TOTAL_VACUUM_YIELD_23MEVC_BAKULE2013` | notes reworded | The old note attached "about half of the incident muons stop" to y_vac. That statement belongs to the measurement set-up (p. 5); §4 does not restate the stopping fraction behind y_vac. |
| 9 | `SOURCE_MU_JPARC_DESIGN_MOMENTUM_BAKULE2013` | notes and explanation reworded | The old note said "Later design documents differ" and then listed Aritome 2024. That paper is a measurement at MUSE S2, not a design document, and it agrees at 28 MeV/c (0.46 MeV/c rms, G4BEAMLINE). The explanation now records that the §4 sentence cites nothing, while §1 cites the J-PARC experiment as ref. [1]. |
| 10 | `SOURCE_MU_JPARC_DESIGN_MOMENTUM_SPREAD_BAKULE2013` | explanation as in 9 | same |
| 11 | `SOURCE_MU_VACUUM_YIELD_JPARC_SCALED_BAKULE2013` | `SOURCE_MU_VACUUM_YIELD_BEAM_SCALING_LAW_BAKULE2013` added to `dependencies` | The value is obtained with eq. (1). |
| 12 | `SOURCE_MUONIUM_FORMATION_FRACTION_POROUS_SILICA_BAKULE2013` | "not pursued" → "the §3.2 imaging measurement used only the aerogel slabs" | The paper says "not investigated further" only for powder and particulate aerogel. |
| 13 | `SOURCE_CALIBRATION_SILICA_PLATE_THICKNESS_BAKULE2013` | "(p. 7)" → "(p. 6) … (p. 7)" | The resolution use is on p. 6 and the background scaling on p. 7. |

The file header now has two extra lines naming this note. No value, unit, page, quotation, uncertainty or status of a
measured quantity needed correcting.

## Removed

None. Every record is supported by a quotation on its cited page, and the single computed record has a derivation.

## Residual doubts (for the lead)

1. **Fig. 1 unit.** Fig. 1 prints 'mol cm^−3'. The brief's unit hint was mole/centimeter**3; the file keeps the
   extractor's molecule/centimeter**3 because the literal reading is impossible. If the literal unit is preferred, revert
   both Fig. 1 records together and keep the notes.
2. **P1 on the formation fraction.**
   - `SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAKULE2013` is P1 on the strength of a test that only computes the
     6.6 σ / 7.5 σ separation. It neither reproduces nor bounds 0.52.
   - Under `docs/fidelity_policy.md` §3 ("reproduces or bounds the value") this is not a P1 check of the quantity. The label
     was kept for consistency with SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020 and
     SOURCE_MUONIUM_FORMATION_FRACTION_TRIUMF_WS2026_ZHANG, which use the same convention.
   - The convention should be decided project-wide.
3. **P1 on the thermal speed.** `SOURCE_MU_THERMAL_VELOCITY_BAKULE2013` is P1 although its test input (295 K) is not in the
   registry, and `docs/fidelity_policy.md` §7.2 lists "inputs not in the registry" as a P0→P1 blocker. It was kept because
   the brief maps that test to this record and the outcome does not depend on the temperature (correction 6).
4. **Confidence cap for `analogous`.** `research/source_quality_policy.md` §4 caps `analogous` at `medium`. In this file
   93 analogous records are `high`, following the batch-9 brief ("high … for table/text values read directly from the page
   image") and the practice of the committed batch-7/8 files (for example, 141 of 141 analogous records are `high` in
   `jparc_g2_design_chain_abe2019.yaml`). The policy text and the practice should be reconciled. I did not mass-downgrade.
5. **Conflict entry.**
   - CONF_MUONIUM_FORMATION_FRACTION (0.52 ± 0.01 here vs 0.655 ± 0.018, Beare 2020; 6.6 σ) is still missing from
     `research/source_conflicts.yaml`.
   - If it is added without a treatment, the same §4 caps every competitor at `low`.
   - The records already state the treatment "kept separate, not averaged".
6. **Unknown records.** These items are not stated in the paper and stay `unknown` or are recorded in notes:
   - which three of the four samples enter the 0.52 (the MuSR facility is not named either);
   - the transverse beam size;
   - the MCP efficiency uncertainty;
   - the numeric "room temperature";
   - whether the 5 % flat top is a full width and the 1.5 % smearing a σ;
   - whether the "10 mm hole" is a diameter;
   - which O2 concentration "high" means;
   - whether the 10 % model spread of the mean free path is inside the Table 1 systematic uncertainties;
   - the SiO2 density behind the Table 2 radii.
7. **Readings the paper does not fully determine.**
   - The optimum momenta 22.9/23.2/23.1/24.5 MeV/c are mapped to 29/47/97/178 mg cm^−3 by "respectively" only. The
     sentence does not repeat the densities, but the ordering is consistent with the areal densities 6.9 × 29, 4.8 × 47,
     2.2 × 97 and 2.0 × 178 mg cm^−2.
   - Possible internal tension: §5 says the density dependence is "weaker than predicted by naive scaling", while p. 9 says it
     is "clearly larger than for α = −1.0". "Naive scaling" is undefined. The tension is preserved in the α record, not
     resolved.
   - The Fig. 3/4 legends say "Data (30mg/cc)", while the captions, text and tables say 29 mg cm^−3.
8. **Audit arithmetic in notes, without tests.** These are extractor or verifier computations, not paper values:
   - the 2.08 % RMS of a 5 % flat top with 1.5 % σ smearing;
   - ρ_SiO2 ≈ 2.2 g cm^−3 reproducing the Table 2 radii;
   - the 86–1370 K band.
   The analytical estimate α/2 + α_µ = +0.25 is P0 with confidence `medium` and no test.
9. **Uncertainties not given.** No uncertainty is printed for y_vac = 4.8e-3, ỹ_vac = 9.6e-4, the 30 µm e^−1 depth or
   α = −1.5. α is the best of three plotted values, not a fit.
10. **Journal version.** PTEP 2013 103C01 was not seen; only arXiv v1 was read.
11. **Registries.** `registries/*.csv` must be rebuilt (`uv run python tools/build_registries.py`) once all batch-9
    groups are final.
