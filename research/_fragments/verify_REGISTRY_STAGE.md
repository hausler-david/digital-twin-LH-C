# Verification note: registry stage of the Phase-0 addendum and batches 7–9 (2026-10-29)

Role: adversarial verifier of the registry stage. Basis: HEAD `000f236` (which includes `104073c`, the batch-10
registration `ad5ac43` and the MR7 arithmetic tests `000f236`; parameter files, registries and conflicts are identical
at `104073c` and `000f236`) plus the registry-stage working tree. The verifier wrote only the files named in its role;
it made no web request, did not commit, and did not touch `CLAUDE.md`, schemas, `lhmuc/`, `tests/`, `tools/`,
`research/source_registry.yaml` or any parameter file other than the three `synthetic_ranges_*.yaml` files. Every
statement was checked against the committed parameter records (loaded with `lhmuc.registry.load_all`), the source
registry, the verifier's own `pdftotext` page layers of the uploads and, where layers were ambiguous, rendered page
images. Pre-verification copies of every touched file are kept in the scratchpad for the before/after record.

## Checks run (after all corrections)

| Command | Result |
|---|---|
| `uv run python tools/validate_yaml.py conflict research/source_conflicts.yaml` | 0 schema errors |
| `uv run python tools/validate_yaml.py assumption parameters/assumptions/phase0_assumptions.yaml` | 0 schema errors |
| `uv run python tools/validate_yaml.py provenance parameters/acceleration/synthetic_ranges_acceleration.yaml` | 0 schema errors |
| `uv run python -m lhmuc validate` | 0 errors, 0 warnings (5601 parameters, 242 sources, 36 scenarios, 20 assumptions, 24 conflicts, 4 proposals) |
| `uv run pytest tests/unit -q` | 56 passed, 1 failed: `test_csv_registries_in_sync` (generated `parameter_registry.csv` and `assumption_registry.csv` are out of sync with the registry-stage edits; see residual 1) |
| Scratch copy of the working tree, `tools/build_registries.py` run there, then `pytest` and `lhmuc validate` | registries regenerated (5601 / 20 rows), `--check` clean, **177 passed**, validator 0 errors |
| Clean snapshot of `104073c` (`git archive`) | 151 tests collected (94 scientific), all pass; validator 0 errors, 0 warnings |

## Entries checked

- `parameters/assumptions/phase0_assumptions.yaml`: all 20 records (10 `superseded_by_evidence`, 10 kept synthetic);
  `superseded_by` ids, `superseding_source_ids`, Phase-0 and re-based bands, `range_vs_evidence`, notes.
- The 20 `_SYN` records in the three `synthetic_ranges_*.yaml` files: value = midpoint (geometric for log-uniform), interval
  and `allowed_range` equal to the assumption band in all 20 (e.g. `IR_LSTAR_SYN` 14.5 m on 4–25 m,
  `PROTON_BUNCH_LENGTH_RMS_SYN` 22.4 cm on log 5–100 cm, `SOURCE_LASER_IONISATION_EFFICIENCY_SYN` 3.16e-4 on log 1e-7–1).
- `research/source_conflicts.yaml`: 24 records, 9 new and 9 changed checked in full; every status is a decided
  treatment (none `open`), none averages.
- `registries/missing_evidence.csv` (14 new, 23 changed rows), `registries/risk_register.csv` (10 new, 11 changed),
  `registries/validation_registry.csv` (55 new rows): every test named exists, every id exists, every `obtained` value was
  recomputed in the earlier part of this pass and matches.
- `research/unresolved_searches.md` (the "resolved or narrowed by uploads" section), `docs/limitations.md`,
  `docs/scientific_scope.md`, `docs/research_roadmap.md`, `docs/roadmap.md`, `docs/software_inventory.md`,
  `docs/architecture.md`, `docs/validation_plan.md`, `docs/uncertainty_policy.md`, `README.md` and the draft
  `docs/reports/M1_addendum_uploaded_documents.md`.

Total: 182 entries (20 assumptions, 20 `_SYN` records, 18 conflicts, 37 missing-evidence rows, 21 risk rows, 55 validation
rows, 11 documents).

## Confirmed without change (selection)

- **6.6 σ.** (0.655 − 0.52)/√(0.01² + 0.018²) = 6.556 σ → "6.6 σ"; Beare-only 0.135/0.018 = 7.50 σ. Stated correctly
  wherever it appears (assumptions, conflict, ME_031, RISK_041, `CHK_P1_BAKULE2013_VS_BEARE2020_FORMATION_FRACTION`,
  limitations §10.4, uncertainty policy §2.1, validation plan §2.0, report F.3).
- **Bakule origin.** Bakule 2013 p.3: "the fraction of muonium formed in the three aerogel samples was 0.52 ± 0.01"
  (four samples were studied, p.2). Beare 2020 cites it as ref. [14] (p.25, p.33) and Aritome 2024 as ref. [21]
  (p.2, p.6). Abe 2019 p.9 ("0.52 is the initial formation probability of monism in the aerogel"), μTRISTAN p.7 ("52 %
  for the muonium formation", numbers from C. Zhang) and the Zhang deck (p.10 "from TRIUMF measurement", p.20
  "measurement from TRIUMF") give no reference: the attribution is an inference for them, as the conflict record, ME_031,
  limitations §10.4 and report F.3 already say. Two other places needed the same caveat (corrections 4, 25).
- **Cheung μ⁻ vs μ⁺.** The caveat is carried by the records (`applicability: screening_only`), scientific scope §1.11,
  limitations §10.8, roadmap §3, research roadmap R8, unresolved searches, software inventory §15.3 and report C.4/F.6;
  it was missing in two validation rows and in the validation-plan table (corrections 26, 27).
- **No digital twin / no validated performance.** README, architecture, roadmap, validation plan and report all state that
  no digital twin, simulation, lattice or geometry exists and that nothing is above P1; no statement found that claims a
  validated performance.
- **Report counts at `104073c`** recomputed: per-document record counts and `reported_lhmuc` counts of table A.1 (all 29
  rows), page counts (archived metadata), 4771 / 563 / 28 totals, 34 uploaded sources, commit table A.2 (hashes, times,
  subjects), 151 tests (94 scientific) and the per-file function counts of A.3, A.4 baselines (55 ME rows all open, 34
  risks, 36 validation rows: 24 pass, 12 planned; 5601 records), D.2 (1423 = 1088 + 170 + 165 = 770 + 526 + 127; 847 =
  327 + 520; 100 P1 / 5501 P0; P1 on 33 of 36 scenarios). Architecture §15.3 (confidences 1138 / 4330 / 105 / 28, all
  scenarios G0, 34 archived-metadata files), uncertainty-policy type counts (93 / 53 / 140 / 75 / 5213 / 27; Beare 29,
  Kilic 16, Bakule 13, Aritome 10; MuIC 132 of 140), validation-plan §2.2 (64 records with `check_ids`, all
  `tests/scientific/<file>.py::<test>`).
- **Quotations.** The seven AI4MuC principles (pp.12–13), the p.4, p.8 and pp.11–12 quotes; the software-inventory
  citations (AloHEP pp.2, 18–22; MAIA pp.21–23; Kilic pp.6–7; Cheung p.2; MuIC PDF pp.19, 23, 30; Sakaki pp.4, 9; Abe p.10;
  André pp.15, 18–19; Topp-Mugglestone p.46; Aritome pp.2–3; AI4MuC pp.10–11, 17); US MCC "the biggest risk in the
  collider's luminosity performance" (p.2); Rogers "Estimate 0.04 μ+ per 5 GeV proton on target to end of A-stage"
  (p.14); Giove 704 MHz and 30 MV/m (pp.3, 5) and the aluminium proposal (pp.11–12); Yamazaki "6-7 %" (p.10).
- **Arithmetic.** η_max 3.91 / 3.00 / 2.44; N_p = 6.97e11 under H = 1 with 1e10 μ⁺ per bunch at 1/300 ns; I_peak 0.75 A
  for 1.6 nC in a 2 ns-FWHM Gaussian; perveance ratio ≈ 220; 0.52 × 0.6 × 0.6 × 0.73 = 0.137; 2.1e-8 per surface muon,
  ≈ 2.5e6 below 0.137 per stopped muon and ≈ 1.2e5 below 2.6e-3; decay averages 0.632 / 0.432 and the MuCol 0.254;
  2079 turns at 1 TeV in 3 km with cτ = 659 m; H = 0.535 for the μLHC-like optics with σz,p = 7.5 cm (independent
  1-D integral); 37.5 m = c × 250 ns / 2.
- **Considered and refuted (no change):** ME_033's "340 keV in 2026 (Nakazawa, preliminary)" is right — Nakazawa p.17
  "These results indicate that we have successfully accelerated muons to 340 keV" (June 2026 beam test, p.12). ME_017's
  "label assigned by the lead" matches the record `IR_LSTAR_FCCEH_WS2026_FORTHOMME` ("The id token FCCEH was assigned by
  the project lead"). The 14 Kraków decks of the README and research roadmap §4 are 3 Phase-0 + 11 addendum decks.

## Corrections

Files: A = `parameters/assumptions/phase0_assumptions.yaml`, C = `research/source_conflicts.yaml`, U =
`research/unresolved_searches.md`, ME / RISK / VAL = the three authored registries, R = the report draft.

1. **A, `ASM_IR_BETA_X_STAR_MUON`, `ASM_IR_BETA_Y_STAR_MUON`, `ASM_PROTON_BUNCH_LENGTH_RMS` (6 places).** Before:
   "SRC_ARXIV_2506_15445 Table 2 (p.12)" for the μLHC muon β* (3 / 0.7 cm) and the 2 mm muon bunch length. After: "Table 1".
   Reason: p.12 has "Table 1. Main parameters of μ+ beam" and "Table 2. ERL60-upgraded proton parameters"; the records
   `MACHINE_MU_BETA_X_STAR_MULHC`, `MACHINE_MU_BETA_Y_STAR_MULHC` and `MACHINE_MU_BUNCH_LENGTH_MULHC` cite Table 1. Five of
   the six were Phase-0 text inside records the stage changed; the sixth is the stage's rewrite of a Phase-0 sentence
   that already carried the error.
2. **A, `ASM_IR_LSTAR` physical basis and `ASM_DET_NOZZLE_LENGTH` physical basis.** Before: "The documented nozzles end at
   the first magnet (IMCC …; LHmuC study base 593.8 cm from the IP …)". After: the IMCC nozzle ends at the last magnet
   (MR7 p.65, L* = 6 m); the LHmuC study gives the base 593.8 cm from the IP but does not say what lies behind it.
   Reason: the Kilic deck mentions no magnet, quadrupole or L*; only MR7 ties the nozzle base to the last magnet.
3. **A, `ASM_SOURCE_MUONIUM_FORMATION_FRACTION` analogous systems.** Before: Bakule 2013 is "the origin of the 0.52 used
   by J-PARC, muTRISTAN, the Zhang deck and Aritome". After: cited as the source by Beare 2020 (ref. [14]) and Aritome
   2024 (ref. [21]); Abe 2019 (p.9), μTRISTAN (p.7) and the Zhang deck (p.20) give no reference, so the origin is
   inferred for them. Reason: the citation chain (see "Bakule origin" above).
4. **A, same record, `range_vs_evidence` and analogous systems; `_SYN` basis.** Before: Beare 0.655 "laser-ablated aerogel,
   all targets combined"; "different silica-aerogel samples"; "two measured silica-aerogel values"; "brackets both
   silica-aerogel measurements". After: "all aerogel targets of that study combined — laser-ablated and flat, silica and
   PMSQ (p.23), Eq. (4) p.25"; "different aerogel samples"; "two measured aerogel values"; "both aerogel measurements";
   `SOURCE_MUONIUM_FORMATION_FRACTION_SYN` `allowed_range.basis` now says the 0.655 combines silica and PMSQ targets.
   Reason: Beare p.23 "All the aerogel targets (even those composed of PMSQ instead of silica) yielded the same muonium
   amplitudes, within statistical uncertainties; therefore all such data were combined"; flat (non-ablated) targets were
   part of the study (p.5).
5. **A, `ASM_SOURCE_LASER_IONISATION_EFFICIENCY` physical basis.** Before: "2.1e-8 … per surface muon at 100 keV, with an
   implied ionisation-and-transport factor of 1.5e-6 - 2.5e-6". After: the factor (≈ 2.0e-6, test band 1.5e-6 – 2.5e-6)
   is the 5.7 keV yield 4.2e-8 divided by 0.38 × 0.52 × 0.13 × 0.81 = 0.0208. Reason: the test divides the 5.7 keV yield;
   the 100 keV yield would give 1.0e-6, outside the band.
6. **A, same record, notes.** Before: "That conflict record says the synthetic range should cover the 122 + 355 nm scheme
   only; this record instead brackets both schemes". After: the conflict requires every scan band to state its laser scheme
   and results from a band spanning both schemes to be reported per scheme; this record brackets both and makes the
   per-point label mandatory. Reason: `CONF_LASER_IONISATION_EFFICIENCY` `selected_treatment` contains no "only" rule.
7. **C, `CONF_LUMI_MODEL_ASSUMPTIONS` competing value (μLHC audit context).** Added a dated note to "proton bunch length
   assumed 7.5 cm = PROTON_BUNCH_LENGTH_RMS_SYN": the 7.5 cm is the order-of-magnitude input of
   `test_hourglass_factor_for_mulhc_like_optics`; the `_SYN` value was 8.5 cm (Phase-0 midpoint) and is 22.4 cm since
   2026-10-29; the sourced nominal LHC value is 7.7 cm (`PROTON_LHC_PR627_RMS_BUNCH_LENGTH_NOMINAL_WS2026_ZIMMERMANN`).
   The original sentence is kept.
8. **C, `CONF_LUMI_MODEL_ASSUMPTIONS` treatment (iv).** Before: "PROTON_BUNCH_LENGTH_RMS_SYN (…; 5–12 cm as written on
   2026-10-28, whereas the text above says 7.5–9 cm — the record governs)". After: uniform 5–12 cm on 2026-10-28, widened on
   2026-10-29 to log-uniform 5–100 cm; plus the caution that `lhmuc.analytical.hourglass_factor` under-reports H above
   σz,p ≈ 0.13 m and may be used for such a scan only once fixed or bounded by a test. Reason: stale band; the stage's own
   widening was not carried into the conflict that governs the scan.
9. **C, `CONF_LHEC_CROSSING_ANGLE` possible cause.** Added a bracketed verifier note to "250 ns muon bunch spacing moves
   the first parasitic encounter to 37.5 m": this holds only if the proton bunches are also ≥ 250 ns apart (DIS2026 p.4
   suggests a reduced proton bunch number but states no spacing); with 25 ns proton spacing each muon bunch meets a proton
   bunch every 3.75 m.
10. **C, `CONF_DETECTOR_SOLENOID_FIELD` treatment.** Added that the re-based band (uniform 3–5.5 T) also brackets 3, 3.8
    and 5 T; the sentence named only the Phase-0 band.
11. **C, `CONF_PROTON_BUNCH_POPULATION_AND_NUMBER` competing value.** Before: "QCD Explorer 6.5e13 protons in one 12.4 m
    uniform super-bunch". After: one super-bunch of 12.4 m rms length with a uniform profile (Table 1 "12.4 m (uniform)";
    Fig. 1 says "30 m long"), with `PROTON_QCDX_SUPERBUNCH_RMS_LENGTH_WS2026_ZIMMERMANN`. Reason: 12.4 m is the rms, not
    the length.
12. **C, `CONF_BOOSTER_DESIGN` treatment.** Before: "the Kraków 70 → 500 GeV single-arc-pair vFFA is recorded as the
    booster-stage description of LHMUC-DIS2026-*". After: it is the documented booster-stage option for LHMUC-DIS2026-type
    scenarios; no scenario slot points to the `ACC_*_WS2026_TOPPMUGGLESTONE` records and they carry no scenario tag.
    Reason: all 144 records have `scenario: null` and no scenario file references them.
13. **C, `CONF_NOZZLE_OPENING_ANGLE` effect.** "the synthetic 5–20° range" → "the Phase-0 synthetic 5–20° range
    (re-based on 2026-10-29 to uniform 2–12°)".
14. **U, Giove entry.** Before: "which hybrid-source stages would need 704 MHz (Rogers' A-stages use 352 MHz)". After:
    Rogers' rectilinear A-stages are A1–A2 at 352 MHz and A3–A4 at 704 MHz (p.12, `SOURCE_HYBRID_RECT_A*_RF_FREQUENCY_WS2026_ROGERS`);
    which cavities Giove's 704 MHz cells would serve is not stated.
15. **U, Bakule entry.** Added a verifier note: Beer et al. 2014 and Zhang et al. 2021 (JPS Conf. Proc. 33) arrived in
    batch 10 (`ad5ac43`); Beer 2014 gives no formation fraction, Zhang 2021 cites Beer 2014 for the 52 % although the value
    is Bakule 2013 p.3; Zhang et al. 2022 (NIM A 1042, 167443) is still not uploaded. Reason: "Beer et al. 2014 … is still
    unread" is false at HEAD.
16. **U, Phase-0 bands list.** Added that `PROTON_BUNCH_LENGTH_RMS_SYN` was widened on 2026-10-29 to log-uniform 5–100 cm.
17. **ME_003.** "40 x 1e10 mu+" → "40 bunches of 1e10 mu+" (Forthomme p.17 "40 bunches of 10^10 µ⁺"; the notation read as
    4e11 per bunch would give N_p ≈ 1.7e10, not 6.97e11). Same fix in limitations §10 table, scientific scope §1.7, roadmap
    §2.1 and report F.2 (correction 30).
18. **ME_007.** Before: "sagitta ~1 mm at 300 GeV". After: "sagitta 'O(mm) for 1 TeV' and 'Ec ~ 300 GeV for iron' (p.3)".
    Reason: Yamazaki p.3 has the two separate statements; 300 GeV is the muon critical energy in iron.
19. **ME_031.** Before (residual): "Zhang et al. 2022 and Beer et al. 2014 are not uploaded." After: Zhang et al. 2022 is
    not uploaded; dated note on the batch-10 Beer 2014 and Zhang 2021 uploads as in correction 15. Status unchanged
    (`partially_resolved`).
20. **ME_034 and RISK_030.** Before: "two stated values" (Forthomme 50 %, μTRISTAN 0.8). After: three, adding 50 % for the
    J-PARC g-2/EDM muon beam (`MACHINE_MUON_POLARISATION_ABE2019`, Abe 2019 p.4 Table 1), which is one of the three
    `superseded_by` records of `ASM_MACHINE_MUON_POLARISATION`. Same addition in the uncertainty-policy §2.1 row.
21. **ME_058, RISK_039, `CHK_P1_M17_GOOD_FIELD_VERTICAL_EXTENT` notes.** Before: 13.59 T on orbit "and 29.04 T in the
    good-field region, above the report's own 8.3 T limit"; "1.51 x and 3.50 x the report's 8.3 T limit". After: 13.59 T
    on orbit exceeds the report's 8.3 T **on-orbit** limit (M17 p.10: "maintaining a peak SC dipole field on-orbit below
    that achievable with current technology … 8.3 T"); the good-field peaks are compared with 8.3 T as a computed demand,
    the report setting no good-field limit.
22. **RISK_039 quotation.** Before: "('magnet design main unknown')". After: "(Topp-Mugglestone p.46: 'Magnet design ...
    Main ‘unknown’ for high-energy vFFA?')". Reason: the earlier text was not verbatim and dropped the question mark.
23. **ME_063, RISK_037, RISK_003 (H = 1 circularity).** Before: "the published LHμC luminosities (DIS2026 2.1e34,
    Forthomme 1e34) correspond to H = 1"; "the Forthomme set reproduces 1e34 only under H = 1 with N_p = 6.97e11". After:
    only DIS2026 (all inputs printed) shows H = 1; the Forthomme 1e34 cannot test H because its N_p is itself implied
    under H = 1. Report F.2 now says the same.
24. **ME_063 value-of-information note, RISK_037 mitigation.** Added that `lhmuc.analytical.hourglass_factor` must be fixed
    or bounded by a registered test before scanning metre-scale proton bunches (independently reproduced: −0.2 % at
    0.15 m, −4.5 / −16 / −24 % at 0.2 / 0.5 / 1 m for μLHC-like optics, −10 / −35 / −49 % for round 7 cm optics).
25. **RISK_041.** Before: "(Bakule 2013 MuSR, p.3; restated by Abe 2019, μTRISTAN, Zhang, Aritome 2024)". After: "used by
    Abe 2019, μTRISTAN and the Zhang deck without a reference and by Aritome 2024 with one".
26. **VAL `CHK_P1_CHEUNG2021_INTEGRATED_LUMINOSITY`, `CHK_P1_CHEUNG2021_CUT_FLOW_DELTA_SIGMA_BAND` notes.** Added the μ⁻
    caveat (Cheung & Wang study p μ⁻ → j ν_μ h; LHμC collides μ⁺; screening comparators only).
27. **`docs/validation_plan.md` §2.0 table.** Added "(μ⁻p, screening comparators for the μ⁺p LHμC)" to the Cheung & Wang
    entry.
28. **VAL `CHK_P1_ARITOME2024_MEASURED_USM_CHAIN` notes.** "about 3 x below the simulated 7e-6 lower bound" → "about 3.5 x"
    (7e-6 / 2.02e-6 = 3.47).
29. **`docs/limitations.md` §10.4.** Before: "0.655 ± 0.018 on different, laser-ablated samples … state that the difference
    'is not understood well'". After: "on different samples — all aerogel targets of their study combined, laser-ablated
    and flat, silica and PMSQ (p.23) — … state that the discrepancy 'is not understood well'" (Beare p.25 wording).
30. **R, F.2.** "40 × 10¹⁰ μ⁺, 300 ns" → "40 bunches of 10¹⁰ μ⁺, 300 ns spacing", plus the H = 1 circularity remark
    (correction 23).
31. **R, F.2.** Before: "`CONF_LUMI_MODEL_ASSUMPTIONS` stays unresolved". After: treatment decided (working tree:
    `propagated_as_uncertainty`), cause unresolved. Reason: F.9 of the same report lists it among the conflicts moved to a
    decided treatment.
32. **R, F.9.** Filled the working-tree statuses of the four formerly open Phase-0 conflicts
    (`propagated_as_uncertainty`, `resolved_as_scenarios`, `propagated_as_uncertainty`, `resolved_as_scenarios`); `<N>` kept.
33. **R, B.2.** "Beare 2020 (0.655, laser ablation)" → "Beare 2020 (0.655 from all its aerogel targets combined;
    laser-ablation emission yields)".
34. **R, C.1 introduction.** Before: "Each superseded record keeps its band as history". After: the Phase-0 band is kept
    in `range_vs_evidence` and a dated note; six scan bands were re-based on 2026-10-29 (L* 4–25 m, nozzle angle 2–12°,
    solenoid 3–5.5 T, vFFA 5–14 T, formation fraction 0.4–0.75, ionisation log 1e-7–1). The table's "Phase-0 band" column
    was checked against `HEAD` and is correct.
35. **R, C.1 calibration lessons.** Before: "All three Phase-0 bands had been built on IMCC or design-target analogues".
    After: on snippet-level analogues or design targets — the MAP/IMCC 10° cone, the LHeC 15 m and IMCC 6 m L* (FCC-eh
    23 m listed as outside), the "100 % in principle" ionisation ceiling with a lower bound set by the DIS2026 yield need.
    Reason: the Phase-0 L* band rested on LHeC as well as IMCC values (`HEAD` physical basis).
36. **R, C.3.** Before: "Hourglass check of Phase 0: a 7.5 cm proton bunch (now `PROTON_BUNCH_LENGTH_RMS_SYN`)". After: the
    7.5 cm is the unsourced input of the Phase-0 test, not the `_SYN` value (8.5 cm, now 22.4 cm); the sourced nominal LHC
    value is 7.7 cm.
37. **R, header, E, G.2 and sources.** Added dated verifier notes: HEAD moved to `000f236` (batch 10: 38 of 242 sources
    uploaded, still 5601 records; 177 tests, 120 scientific); Beer 2014, Zhang 2021 and Kaya et al. are uploaded and read
    but not extracted, so "unread"/"fetch" statements are superseded. The counts of the draft remain those of `104073c`.
38. **`docs/research_roadmap.md` R5, §3a and sources.** Same batch-10 notes (W8 still lacks Zhang et al. 2022).
39. **`docs/validation_plan.md` §2.0 and §5.** Before: "the scientific suite holds five files"; "`tests/scientific/` holds
    the five files of §2.0". After: six files at `104073c` (`test_analytical_checks.py` plus the five of the table), with
    `test_batch10_documents.py` (18) and `test_imcc_mr7_reference.py` (8) since `000f236`.
40. **`docs/roadmap.md` §2.1 nozzle row.** Before: "base dimensions, tungsten grade, cladding thickness (Kilic p.22)".
    After: "base dimensions (to be set by simulation, Kilic p.22); tungsten grade and cladding thickness (not stated)".
    Reason: Kilic p.22 names only the base dimensions as open; the other two are simply absent from the deck.
41. **`docs/software_inventory.md` §15.2 MuonColliderSoft row.** "`SRC_ARXIV_2502_00181` pp.21, 23" → "pp.21–23
    (k4MarlinWrapper p.22)".
42. **`README.md` status.** Before: "5601 records with page-level provenance from 34 uploaded documents"; "(151 tests)".
    After: 5578 of the 5601 records carry page-level provenance from the 34 documents, the other 23 are synthetic ranges
    with assumption records or derived values with derivations (20 synthetic, 2 analytical estimates, 1 derived); 151
    tests at `104073c`, 177 at `000f236`.

## Removed

None. No entry was found to be unsupported as a whole; every error was a wording, page, table, count or attribution
error that could be corrected in place.

## Residual doubts (for the lead)

1. **Generated registries out of sync.** `registries/parameter_registry.csv` and `registries/assumption_registry.csv`
   must be regenerated with `uv run python tools/build_registries.py` before the registry stage is committed
   (`test_csv_registries_in_sync` fails until then). Verified in a scratch copy: after regeneration the full suite passes
   (177) and the validator reports 0 errors.
2. **`lhmuc.analytical.hourglass_factor` above σz,p ≈ 0.13 m.** The under-estimate is documented in the assumption,
   conflict, ME_063 and RISK_037 but pinned by no test, and no missing-evidence or risk row tracks the tool itself; a
   registered bound or fix (in `lhmuc/` and `tests/`) is outside the verifier's remit.
3. **J-PARC DLS frequency.** Abe 2019 p.11 "An RF frequency of 1,296 MHz is adequate for the wider phase space" (Fig. 5
   label p.10 "1296 MHz (spanning DAW and DLS)", `ACC_G2_LINAC_RF_FREQUENCY_HIGH_ABE2019`) vs Nakazawa 2026 slide 2 "DLS
   (2592 MHz)" (`SOURCE_JPARC_DLS_FREQUENCY_WS2026_NAKAZAWA`). Both records are kept, `ASM_ACC_RF_FREQUENCY` says so, but
   no conflict record exists. Proposed: `CONF_JPARC_DLS_FREQUENCY`, `resolved_as_scenarios` by design version (2019
   design vs 2026 front end), never averaged, entering no LHμC parameter — the pattern of `CONF_JPARC_IHDTL_ENERGY`. Not
   written here because it would change the conflict count (24 = 15 + 9) used in six documents.
4. **Status decisions of four Phase-0 conflicts** (`CONF_LUMI_MODEL_ASSUMPTIONS`, `CONF_LHEC_CROSSING_ANGLE` →
   `propagated_as_uncertainty`; `CONF_PROTON_BUNCH_POPULATION_AND_NUMBER`, `CONF_JPARC_IHDTL_ENERGY` →
   `resolved_as_scenarios`) were made by the registry stage, dated and reasoned; they need the lead's confirmation.
5. **Supersession by related-machine values.** `ASM_IR_LSTAR` and `ASM_DET_SOLENOID_FIELD` are superseded by LHeC, IMCC,
   MAIA and MUSIC values, none an LHμC value. The records say so; whether this meets the schema wording ("a reported or
   authoritative value now exists") is the lead's call.
6. **Parameter records outside the verifier's remit.** `SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020` is named "… in
   laser-ablated silica aerogel … (sum of all aerogel targets, 1.92 mT)", although the sum includes flat and PMSQ targets;
   `DET_RECO_FRAMEWORK_MAIA` cites p.23 for content that is partly on p.22 (k4MarlinWrapper). `ASM_DET_NOZZLE_MATERIAL`
   lists `SRC_ARXIV_2510_27437` in `superseding_source_ids` but no MR7 material record (`DET_NOZZLE_MAIN_MATERIAL_MR7`,
   `DET_NOZZLE_CLADDING_MATERIAL_MR7`) in `superseded_by`. The "silica-aerogel" domain wording of the formation-fraction
   band is kept as a conservative domain statement.
7. **Batch-10 content not yet folded in.** Zhang et al. 2021 cites Beer et al. 2014 for the 52 % (`CONF_MUONIUM_FORMATION_FRACTION`
   lists the citation chain without it); Kaya et al. eq. (6) carries the μ⁺μ⁻ decay average and no hourglass factor
   (relevant to `CONF_LUMI_MODEL_ASSUMPTIONS`, RISK_042); the `000f236` test gives a one-beam/two-beam factor of 1.75 at
   MR7 10 TeV. These belong to the batch-10 extraction stage.
8. **MuCol M17 internal inconsistency.** p.15 "These vFFA rings have been shown to have parameters (drift lengths, peak
   dipole strengths on orbit) within realistic bounds" while Table 2.3 gives 13.59 T on orbit for stage 4, above the
   report's own 8.3 T (p.10). `CONF_VFFA_PEAK_FIELD` and RISK_039 record the exceedance, not the contradicting conclusion
   (`ACC_VFFA_CONCLUSION_STABLE_OPTICS_MUCOLM17`).
9. **Unpinned audit numbers.** The factor 1.70 of the max(σ) convention for the MuIC LHmuC spot sizes
   (`CONF_LUMI_MODEL_ASSUMPTIONS` effect) and the Zimmermann extrapolation in `ASM_PROTON_BUNCH_LENGTH_RMS` (HL-LHC
   population 2.2e11 combined with the nominal-LHC 7.7 cm) are labelled audit arithmetic but have no test.
10. **`CONF_LASER_IONISATION_EFFICIENCY` required future evidence** asks for "the results of the 2026 J-PARC 340 keV run";
    the Nakazawa deck already reports the acceleration (p.17, preliminary) and ~0.4 μ⁺/pulse (p.16). What is missing is
    the yield and ionisation efficiency with the upgraded laser; the wording could be sharpened.
11. **Pre-existing items outside this stage.** `ASM_ACC_RF_GRADIENT` pairs the "31.25 GeV" text with
    `ACC_BOOSTER_LINAC_ENERGY_GAIN_MUTRISTAN_MULHC` = 30 GeV, and the LHeC real-estate gradient 9.2 MV/m lies below its
    10–30 MV/m band (flagged by the stage); the 325 MHz member of `ASM_ACC_RF_FREQUENCY` has no source of its own;
    ME_066 overlaps ME_043; scenario-level P1 labels (33 of 36) are not covered by the record-level P1 rule;
    `docs/security_policy.md` (line 35) and `docs/reports/M1_evidence_audit.md` (line 215) still name only
    `yefetu/ALOHEP`; some `unresolved_questions` in `research/source_registry.yaml` predate the uploads.
12. **Report placeholders.** The `<N>` counts of the report draft remain for the lead to fill once the stage is committed.
