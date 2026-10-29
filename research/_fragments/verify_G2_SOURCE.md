# Verification note — group G2_SOURCE (Phase 0 addendum, 2026-10-29)

Role: adversarial verifier. Files verified (all written by the G2_SOURCE extraction of 2026-10-28):

| File | Source(s) | Records before → after |
|---|---|---|
| `parameters/source/muonium_diffusion_ws2026_zhang.yaml` | SRC_WS1681458_ZHANG_MUONIUM (23 pp.) | 76 → 82 |
| `parameters/source/hybrid_source_ws2026_rogers.yaml` | SRC_WS1681458_ROGERS_HYBRID_SOURCE (20 pp.) | 131 → 131 |
| `parameters/source/low_velocity_front_end_ws2026_nakazawa.yaml` | SRC_WS1681458_NAKAZAWA_LOW_VELOCITY (19 pp.) | 85 → 86 |
| `parameters/source/jparc_measurements_aritome2024_beare2020.yaml` | SRC_ARXIV_2410_11367 (6 pp.), SRC_ARXIV_2006_01947 (34 pp.) | 179 → 180 |
| `parameters/source/mutristan2022_source_chain.yaml` | SRC_ARXIV_2201_06664 (24 pp.) | 51 → 51 |
| `parameters/machine/scenarios_addendum_source.yaml` | — | 2 scenarios (roles and notes corrected) |

Total 522 → 530 parameter records: 8 added, **0 removed**, 11 ids renamed (all referenced only inside their own file).
Status counts after verification: analogous 423, imported_related 55, reported_lhmuc 26, analytical_estimate 19,
unknown 7. Validation levels: P1 17, P0 513.

Method: every record was compared with its cited page — the text layer for prose, rendered page images (110–300 dpi
crops) for table cells, figure labels, plot annotations and plot readings; quotations were located verbatim; every
derivation and every P1 check was recomputed independently. Cross-checks used the registered originals SRC_ARXIV_1306_3810
(Bakule et al. 2013), SRC_ARXIV_2605_25580 (Sakaki et al. 2026) and the μTRISTAN paper. Edits were applied by a script that
starts from a backup of the extractor's files and logs every change (verifier's scratchpad `verify_g2/apply_fixes.py`,
`verify_g2/fix_log.json`; the full log is Appendix A). The extractor's YAML anchors/aliases (`&id001`) were expanded;
nothing else in the structure changed.

## Summary of what was wrong

Values, units and quotations were mostly right. The substantive errors were attributions and interpretations:
the Zhang p.10 "Intensity (/s)" column was labelled H-line (it is the present-intensity chain; 9 ids renamed); the Zhang
p.21 "new version" was attributed to Hamada et al. 2022 (it is Sakaki et al. 2026); the p.19 4×/8× gains were attributed to
the μTRISTAN paper (they are Zhang's unpublished simulation); the μTRISTAN 0.016 pions/proton was described as "over the
40 traversals" (it is per traversal); an IMCC unit conversion carried reported_lhmuc; a Nakazawa quotation came from hidden
(non-rendered) PDF text; the "> 7 sigma" formation-fraction statements were corrected to 6.6 sigma (lead note); one P1 claim
pointed at a test that does not exist; plot-axis readings were not marked as analytical estimates; and 475 confidences
exceeded the §4 caps that `lhmuc validate` has enforced since 2026-10-29.

## What was checked and found correct

- **Values, units, pages** of the remaining records, including: Zhang p.10 table (all four columns), p.20 μTRISTAN budget
  (0.52 / 0.6 / 0.6 / 0.73 → "14 %"), p.7 fit (T = 322 K, D = 870 cm²/s), p.21 (1.2e12 /s per MW, D = 2×10⁻³ cm²/s,
  ρ0 ≃ 60 mm⁻¹); Rogers p.14 IMCC table (Rectilinear A row 1240 µm, 0.6 eV ms, 49.6 %, 47.1 %, 21.2e12) and the concept
  statements of pp.3, 5, 12–15, 19–20; Nakazawa p.16 LHμC column (1e10, 1.6 nC, FWHM ~2 ns, ~0.75 A, 3.4 mA, 220, ~10 A)
  and p.14 emittances (0.84 ± 0.04 / 0.38 ± 0.01 π mm mrad; simulation 0.63 / 0.36); Aritome et al. pp.2–4 (9.5e4 /pulse,
  38 / 52 / 13 / 19 %, (4.0 ± 0.4)e-3 and 2e-3 μ+/pulse, 7e-6 – 6e-5, 20 % decay loss); Beare et al. target tables, emission
  rates and Eq. (4); Hamada et al. pp.4–7 (150 mb, 0.016, 110 nC, 40 turns, 2 bunches, 50 Hz, 50 %, 6.8 %, 5.5e-4, 7.2 nC,
  9.0e13 /s, O(10⁵)).
- **Statuses**: reported_lhmuc only for Rogers' own hybrid-concept statements, targets and guesses and for Nakazawa's
  LHμC 1e10 space-charge column (26 records after one demotion); restated IMCC, J-PARC, TRIUMF, Kamioka and μTRISTAN values
  are analogous or imported_related with the original named; unknowns have value null.
- **Arithmetic re-done** (agrees with the records except where corrected below): 1.8e6 × 0.467 = 8.4e5, × 0.52 = 4.37e5
  (printed 4.3e5), × 0.082 = 3.6e4 (printed 3.5e4); 8.24e5 / 7.21e6 = 0.114; 0.52 × 0.6 × 0.6 × 0.73 = 0.1367;
  √(Dτ_μ) = 0.437 mm (870 cm²/s) and 0.66 µm (2×10⁻³ cm²/s); 1.741 mm × m_μ c²/c = 0.614 ns MeV; 21.2e12 / 500e12 = 0.042;
  Gaussian peak current of 1.6 nC with 2 ns FWHM = 0.753 A; 30 mA × m_μ/m_p = 3.38 mA; 0.753 A / 3.38 mA = 223;
  4.0e-3 / 9.5e4 = 4.2e-8; 2e-3 / 9.5e4 = 2.1e-8; 0.38 × 0.52 × 0.13 × 0.81 = 0.0208; 2 × 0.155 / 0.474 = 0.654;
  (0.655 − 0.52)/√(0.01² + 0.018²) = 6.56; 3 GeV × 6.6 µC × 2 × 50 Hz = 1.98 MW; 0.016 × 0.5 × 0.068 = 5.4e-4;
  5.5e-4 × 2 × 6.6 µC = 7.26 nC, × 40 turns × 50 Hz / e = 9.1e13 /s (printed 9.0e13); Kilpatrick field at 324 MHz 17.8 MV/m;
  thermal Mu speed at 322 K 7.7 mm/µs; 150 mb on 10 mm graphite (2.2 g/cm³) = 0.0166 per pass.
- **Canonical ids** — all 13 exist with the stated values (table below); none was renamed.

## Corrections made

### Zhang deck (`muonium_diffusion_ws2026_zhang.yaml`)
1. **p.10 "Intensity (/s)" column is not the H-line.** The slide does not name a beamline; the chain uses the 244 nm laser
   and ends at 0.1 /s on an MCP, matching the 2022 S2-area test of pp.11–12 (0.126 Hz). The H-line appears only in the p.9
   simulation (40 % stopping, versus 0.467 in this column). Applicability rewritten for 7 records and **9 ids renamed**
   `…_HLINE_…` → `…_PRESENT_…` (the vacuum-yield factor → `…_DIFFUSION_MODEL_…`); see the rename table.
2. g-2 target column: note that its implied stopping fraction (1.35e8 / 3.2e8 = 0.42) is close to the 40 % H-line
   simulation, without asserting that the column uses it.
3. **p.21 "new version" is Sakaki, Kamioka and Yoshida 2026** (SRC_ARXIV_2605_25580, Fig. 1 and Eq. (6)), not Hamada et
   al. 2022 (4 records). η_conv record: the original paper also leaves it unquantified (SOURCE_HYBRID_MU_TO_MUONIUM_CONVERSION_SAKAKI2026
   is null), so no uploaded source gives it. N_tot definition taken from Sakaki Eq. (6); tungsten T = 2000 K and
   D = 2×10⁻³ cm²/s cross-referenced to the _SAKAKI2026 records; the ρ0 √(Dτ) form matches Sakaki App. A but ρ0 ≃ 60 mm⁻¹
   is not in the paper (implied y = 0.040 stays confidence low).
4. **p.19 vertical-variant gains (4×, 8×) are Zhang's own unpublished simulation** ("Yet another version (not published
   in my paper)"), not μTRISTAN values: status imported_related → analogous, category design_variant → analogous,
   explanation rewritten (2 records). The vertical-variant concept record now quotes Hamada et al. p.7 ("a layer structure
   in the vertical direction …") to support "muTRISTAN took this idea".
5. **Kamioka E34 CM30 plot (p.20)**: the quotation pointed at the "Phase2-1 122nm 100μJ" arrow, which marks the 40 mJ
   (green) curve; the recorded 0.10 is the 300 mJ (blue) curve, marked by "Phase2-2 Both laser are ready" — quotation
   fixed; other curves re-read at 250 dpi (10 mJ ≈ 0.015, not 0.02).
6. **Plot-axis readings → analytical_estimate** (research/source_quality_policy.md §5.3) with the reading method as the
   derivation, re-read on a 200 dpi render (7 records: optimal interval 7 mm; thermal-muon yield gains 5.2 / 3.4 / 2.5;
   Kamioka 0.10 and 0.15; TDR reference 0.20). The TDR reference line is dash-dot, not dashed.
7. Plot/annotation re-readings: p.7 χ²_min + 2.30 contour reaches 850 cm²/s at 322 K (not 855); p.18 reflection-model
   dip at about 650 ns (not 700).
8. Thermal-velocity audit: 7.7 mm/µs at the fitted 322 K (7.5 mm/µs is the 300 K value).
9. "~3 m" photograph annotation: name made interpretive (the slide does not say what the arrow spans); confidence → low.
10. Diffusion-length note: the unsupported "different definitions" explanation replaced by the factual statement that the
    two numbers come from different model fits.
11. **Lead note**: "> 7 sigma" → 6.6 sigma with both uncertainties (7.5 sigma with Beare's alone), check_ids = both pinning
    tests; origin of "0.52 (from TRIUMF measurement)" named (Bakule et al. 2013, SRC_ARXIV_1306_3810 p.3, MuSR, 0.52 ± 0.01;
    SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAKULE2013) in the 0.52 record, both formation-rate records whose quotation
    contains it, the 0.137 budget (with the 0.172 sensitivity for 0.655), the multilayer-budget record and the new Kamioka
    0.52 record.
12. Six records added (p.3 schematic 3.4 MeV; p.9 H-line simulation 40 % / 52 % / 6 % / 27 % and their product 3.37e-3,
    which reproduces Beare et al.'s 3.4e-3 per surface muon).

### Rogers deck (`hybrid_source_ws2026_rogers.yaml`)
13. SOURCE_HYBRID_CONCEPT value no longer selects laser ionisation (p.5 says only "Low energy cooling"; p.2 lists laser
    ionisation and frictional cooling): `…_low_energy_laser_ionisation_cooling` → `…_low_energy_cooling`; the shared concept
    sentence of 13 records changed accordingly.
14. **SOURCE_HYBRID_STAGE_A4_LONGITUDINAL_EMITTANCE_NSMEV_WS2026_ROGERS**: reported_lhmuc → analogous (a unit conversion of
    the IMCC stage-A4 value; equals the 0.6 eV ms of the p.14 table); audit 0.614 ns MeV.
15. Five transverse-emittance notes asserted an IMCC convention ("π mm rad, normalised") that the slide does not state —
    removed.
16. Decelerator 1 ns target: the ~2 ns FWHM comparator on the Nakazawa deck is the ultraslow-muon pulse, not a surface-muon
    pulse. RF-breakdown records (4): "MuCool Test Area" is not on the slide. Proton-driver energy: comes from p.14
    "per 5 GeV proton on target", not from the reproduced table. End-of-stage-A comparator: μTRISTAN's 5.5e-4 is per pass
    (≈ 0.022 per proton overall).
17. 39 m aerogel range: independent Bethe–Bloch check added (92.7 g/cm² → 39.6 m at 23.4 mg/cm³; scratchpad
    `verify_g2/range_check.py`).

### Nakazawa deck (`low_velocity_front_end_ws2026_nakazawa.yaml`)
18. **"~2 m" / "~3 m" (p.8) are RFQ lengths**, not setup lengths: 2 ids renamed, names and explanations fixed.
19. **IH-DTL "scheduled for 2028"**: the quoted sentence exists only in the PDF text layer of pp.5 and 7 and is not
    rendered on either slide; the record now cites the visible p.8 "Step 3 … ⑤ IH-DTL → Future (~2028)" (page, section,
    figure, quotation, uncertainty note "~2028", notes).
20. p.14 emittances are not labelled "preliminary" (the TOF and bunch plots on pp.13, 15 are); names say "discrepancy with
    simulation under investigation".
21. The ~200× gain 2024 → 2026 is not broken down on the deck; it also involves the move from S2 to H2.
22. RFQ redesign reference: the slide gives only the J-STAGE URL (no year). IH-DTL 4.26 MeV: noted as the first non-snippet
    source for CONF_JPARC_IHDTL_ENERGY.
23. One record added: laser irradiation +1332 ns (p.13 legend; 1332 + 1030 ns = 2362 ns, where the accelerated peak sits).

### Aritome et al. / Beare et al. (`jparc_measurements_aritome2024_beare2020.yaml`)
24. **5.7 keV yield**: the implied ionisation-plus-transport efficiency (2.0e-6; 2.5e-6 without the 20 % transport decay)
    is about 3× *below* the lower end of the simulated 7e-6 – 6e-5; the previous text reasoned the opposite and applied the
    "10–40 % lower laser energy" remark (which concerns the 100 keV run) to it. Quotation page marker and page "3, 2" added;
    the P1 method now states the implied 2.0e-6 and that 1.5e-6 – 2.5e-6 is the test window.
25. Unit of SOURCE_DIAG_QM_GRADIENT_PER_AMPERE_ARITOME2024: T/m → tesla/meter/ampere ("2.25 × Ii (T/m)").
26. Prototype RFQ vs full-scale RFQ (3 MeV H⁻ design, 0.34 MeV for μ+); stopping-efficiency comparator corrected to the
    present-intensity chain and the 40 % H-line simulation; H-line attribution of the surface-muon gain rests on ref. [35];
    implied 100 keV rate assumes every 25 Hz pulse reaches the MLF.
27. **Lead note**: conversion efficiency 0.52 → origin Bakule et al. 2013 (0.52 ± 0.01) and 6.6 sigma; Beare 0.655 record:
    methods/check_ids corrected (6.6 sigma combined, 7.5 sigma Beare-only), origin of the 0.52 named; the
    Bakule-as-quoted-by-Beare record points to the primary record.
28. Beare 0.655: the value comes from the µSR data of **all aerogel targets combined** (p.23, "even those composed of PMSQ
    instead of silica"; Fig. 11 caption "silica aerogel targets"), so it is not specific to laser-ablated targets; the shared
    context sentence of the other 88 Beare records now names the paper and defers to the target named in each record
    (it called every value — including PMSQ and flat-target values — one for "laser-ablated silica aerogel targets").
29. Beare g-2 estimate 3.4e-3 Mu per surface muon: the "6× not reconciled" statement compared different quantities; the
    Kamioka H-line breakdown on Zhang p.9 reproduces it (40 % × 52 % × 6 % × 27 % = 3.37e-3).
30. M15 note: the 22.5 MeV/c peak is the yield maximum, not the half-stop momentum. Cross-page quotations: pages "2-3",
    "15-16", "31-32". Five floating-point artefacts (e.g. 0.027600000000000003) cleaned.
31. One record added: prototype RFQ length 1973 mm (Fig. 1 dimension; scenario role `rfq_length_figure`).

### μTRISTAN paper (`mutristan2022_source_chain.yaml`)
32. **0.016 pions/proton is per traversal** of the 10 mm target: the paper converts it to "110 nC/bunch (times 40 turns
    times 2 bunches)" (0.016 × 6.6 µC = 106 nC) and 150 mb × 10 mm graphite gives 0.0166 per pass. Name and explanation
    fixed; 5.5e-4 is per pass ("per production-ring turn"), i.e. 9.0e13 /s ÷ 4.1e15 p/s ≈ 0.022 per proton overall; the
    bunch-charge record says per turn.
33. **SOURCE_PROTON_DRIVER_POWER_MUTRISTAN2022: P1 → P0** — the claimed pin "for the μLHC copy … in
    tests/scientific/test_analytical_checks.py" does not exist; the 1.98 MW audit is kept as a note.
34. Cross-page quotations: pages "4, 6" and "6-7". Lead note: origin of the 0.52 named in the formation-fraction record.

### All five parameter files
35. `unit: string` → `dimensionless` for 40 categorical records (task rule; "string" is only an alias).
36. Empty `check_ids` filled for 15 P1 records with the tests their methods name (all 17 P1 check ids resolve to existing
    test functions).
37. **Confidence caps (§4)**: 475 confidences lowered high → medium, nothing else changed — Zhang 57 (43 analogous,
    10 imported_related design_variant, 4 unrefereed slides), Rogers 122 (109 analogous, 13 slides), Nakazawa 77 (68, 9),
    Aritome/Beare 174 (analogous), μTRISTAN 45 (38 design_variant, 7 analogous). List in Appendix B. Five analytical
    estimates computed from refereed papers keep `high` (no mechanical cap applies; see residual doubts).

### Scenario file (`scenarios_addendum_source.yaml`)
38. LHMUC-SOURCE-HYBRID-IMCC: `cost` removed from `unknown_roles` (its record carries the order-of-magnitude value
    ~O(500) MCHF); notes now name all three roles that are both explicit-unknown records and unknown roles
    (low_energy_cooling_efficiency, wall_plug_power, hts_radiation_tolerance).
39. JPARC-MUSE-S2-2024: role `rfq_length_figure` → SOURCE_RFQ_PROTOTYPE_LENGTH_FIG1_ARITOME2024 added; notes name the origin
    of the 52 % (Bakule et al. 2013, 0.52 ± 0.01, 6.6 sigma from Beare) and state the implied 2.0e-6 instead of the test
    window "1.5e-6 – 2.5e-6". Header line pointing to this note added.

## Ids renamed

| Old id | New id |
|---|---|
| SOURCE_SURFACE_MUON_RATE_HLINE_WS2026_ZHANG | SOURCE_SURFACE_MUON_RATE_PRESENT_WS2026_ZHANG |
| SOURCE_STOPPED_MUON_RATE_HLINE_WS2026_ZHANG | SOURCE_STOPPED_MUON_RATE_PRESENT_WS2026_ZHANG |
| SOURCE_MUONIUM_FORMATION_RATE_HLINE_WS2026_ZHANG | SOURCE_MUONIUM_FORMATION_RATE_PRESENT_WS2026_ZHANG |
| SOURCE_MUONIUM_VACUUM_YIELD_HLINE_WS2026_ZHANG | SOURCE_MUONIUM_VACUUM_YIELD_DIFFUSION_MODEL_WS2026_ZHANG |
| SOURCE_MUONIUM_VACUUM_RATE_HLINE_WS2026_ZHANG | SOURCE_MUONIUM_VACUUM_RATE_PRESENT_WS2026_ZHANG |
| SOURCE_USM_RATE_HLINE_244NM_WS2026_ZHANG | SOURCE_USM_RATE_PRESENT_244NM_WS2026_ZHANG |
| SOURCE_USM_PER_SURFACE_MUON_HLINE_244NM_WS2026_ZHANG | SOURCE_USM_PER_SURFACE_MUON_PRESENT_244NM_WS2026_ZHANG |
| SOURCE_USM_RATE_AFTER_EXTRACTION_HLINE_WS2026_ZHANG | SOURCE_USM_RATE_AFTER_EXTRACTION_PRESENT_WS2026_ZHANG |
| SOURCE_USM_RATE_AT_MCP_HLINE_WS2026_ZHANG | SOURCE_USM_RATE_AT_MCP_PRESENT_WS2026_ZHANG |
| SOURCE_JPARC_STEP1_SETUP_LENGTH_WS2026_NAKAZAWA | SOURCE_JPARC_PROTO_RFQ_LENGTH_FIGURE_WS2026_NAKAZAWA |
| SOURCE_JPARC_STEP2_SETUP_LENGTH_WS2026_NAKAZAWA | SOURCE_JPARC_FULL_RFQ_LENGTH_FIGURE_WS2026_NAKAZAWA |

No file outside the six assigned ones references any old id (repository-wide search).

## Records added

| parameter_id | Value | Page | Quotation | Status / confidence |
|---|---|---|---|---|
| SOURCE_SURFACE_MUON_ENERGY_SCHEMATIC_WS2026_ZHANG | 3.4 MeV | Zhang p.3 | "Surface muon beam ( 3.4 MeV)" | analogous / medium |
| SOURCE_HLINE_SIM_STOPPING_EFF_KAMIOKA_WS2026_ZHANG | 0.40 | Zhang p.9 | "Simulation of H-line of J-PARC • Efficiency breakdown: • Stopping eff: 40% • Mu formation eff: 52% • Vacuum emission: 6% • Overlap with laser: 27%" | analogous / medium |
| SOURCE_HLINE_SIM_MUONIUM_FORMATION_EFF_KAMIOKA_WS2026_ZHANG | 0.52 | Zhang p.9 | same | analogous / medium |
| SOURCE_HLINE_SIM_VACUUM_EMISSION_KAMIOKA_WS2026_ZHANG | 0.06 | Zhang p.9 | same | analogous / medium |
| SOURCE_HLINE_SIM_LASER_OVERLAP_KAMIOKA_WS2026_ZHANG | 0.27 | Zhang p.9 | same | analogous / medium |
| SOURCE_HLINE_SIM_MU_FOR_IONISATION_PER_SURFACE_MUON_WS2026_ZHANG | 3.37e-3 | Zhang p.9 | same (derivation: product of the four ids) | analytical_estimate / medium |
| SOURCE_LASER_TIMING_2026_WS2026_NAKAZAWA | 1332 ns | Nakazawa p.13 | "laser irradiation: +1332 ns … time relative to the first surface-muon arrival [ns]" | analogous / medium |
| SOURCE_RFQ_PROTOTYPE_LENGTH_FIG1_ARITOME2024 | 1973 mm | Aritome p.2, Fig. 1 | "RFQ … 1973 mm" | analogous / medium |

## Removed

None. Every record is supported by its cited page after the corrections above; unsupported interpretations were removed
from texts rather than deleting records.

## Canonical ids (all confirmed)

| Canonical id | Value | Status / confidence / level |
|---|---|---|
| SOURCE_MUONIUM_FORMATION_FRACTION_TRIUMF_WS2026_ZHANG | 0.52 | analogous / medium / P1 |
| SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020 | 0.655 ± 0.018 | analogous / medium / P1 |
| SOURCE_LASER_IONISATION_EFF_244NM_WS2026_ZHANG | ~1e-6 (order_of_magnitude) | analogous / medium / P0 |
| SOURCE_LASER_IONISATION_EFF_122NM_BUDGET_WS2026_ZHANG | 0.73 | imported_related / medium / P0 |
| SOURCE_LASER_IONISATION_EFF_IMPLIED_G2_TARGET_WS2026_ZHANG | 0.114 | analytical_estimate / medium / P1 |
| SOURCE_MUTRISTAN_POST_STOPPING_BUDGET_WS2026_ZHANG | 0.137 (= 0.52 × 0.6 × 0.6 × 0.73) | analytical_estimate / medium / P1 |
| SOURCE_USM_PER_SURFACE_MUON_100KEV_ARITOME2024 | 2.1e-8 | analytical_estimate / high / P1 |
| SOURCE_USM_PER_PULSE_100KEV_ARITOME2024 | 2e-3 | analogous / medium / P0 |
| SOURCE_SURFACE_MU_PER_PULSE_ARITOME2024 | 9.5e4 | analogous / medium / P0 |
| SOURCE_RFQ_PEAK_CURRENT_1E10_WS2026_NAKAZAWA | 0.75 A | reported_lhmuc / medium / P1 |
| SOURCE_RFQ_PERVEANCE_RATIO_WS2026_NAKAZAWA | 220 | reported_lhmuc / medium / P1 |
| SOURCE_BUNCH_CHARGE_1E10_WS2026_NAKAZAWA | 1.6 nC | reported_lhmuc / medium / P1 |
| MACHINE_MUON_POLARISATION_MUTRISTAN2022 | 0.8 | imported_related / medium / P0 |

## Validation

- `uv run python tools/validate_yaml.py provenance|machine <file>`: 0 schema errors in each of the six files.
- `uv run python -m lhmuc validate`: **0 errors and 0 warnings in the six G2_SOURCE files**, including the §4
  confidence-cap check added on 2026-10-29 (`tools/apply_confidence_caps.py --check` on the five parameter files:
  "0 record(s) exceed a §4 cap"). The repository-wide run still reports confidence-cap errors (3501 when the caps were
  applied here, 2738 at the time of writing as other groups apply them), all in other agents' untracked addendum files
  (MR7, Schulte, Kilic, MAIA/MUSIC, Forthomme, Zimmermann, Acosta, Yamazaki, HEQCD, μTRISTAN physics, MuIC …), which this
  verifier may not edit; no other error type remains.
- `uv run pytest`: 113 passed; 2 failed only for repository-wide reasons outside these files —
  `test_no_validation_errors` (the cap errors above) and `test_csv_registries_in_sync` (registries are regenerated by
  the lead with `tools/build_registries.py`; the 8 added and 11 renamed ids also change `registries/parameter_registry.csv`).

## Items for the registry stage (lead)

1. **CONF_MUONIUM_FORMATION_FRACTION** (still absent from `research/source_conflicts.yaml`): 0.52 (Bakule et al. 2013 MuSR,
   0.52 ± 0.01; restated by Zhang pp.9, 10, 20, Aritome et al. ref. [21], μTRISTAN footnote †, Beare ref. [14]) vs
   0.655 ± 0.018 (Beare et al. Eq. (4), all aerogel targets combined): **6.6 sigma** with both uncertainties, not "> 7 sigma".
   Competitors in these files: SOURCE_MUONIUM_FORMATION_FRACTION_TRIUMF_WS2026_ZHANG,
   SOURCE_HLINE_SIM_MUONIUM_FORMATION_EFF_KAMIOKA_WS2026_ZHANG, SOURCE_MUONIUM_CONVERSION_EFF_ARITOME2024,
   SOURCE_MUONIUM_FORMATION_FRACTION_BAKULE2013_BEARE2020, SOURCE_MUONIUM_FORMATION_FRACTION_MUTRISTAN2022,
   SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020 (plus SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAKULE2013). Under §4 every
   competitor drops to `low` while the conflict record has no decided treatment.
2. **CONF_LASER_IONISATION_EFFICIENCY** (also absent): 0.73 (μTRISTAN budget), 0.114 (implied by Zhang's g-2 column),
   0.10 / 0.15 and the 0.20 TDR line (Kamioka plot, now analytical_estimate plot readings), ~0.10 (Aritome projection),
   ~1e-6 (244 nm, Zhang) and 7e-6 – 6e-5 (Aritome simulation); demonstrated end-to-end 2.1e-8 per surface muon. Records
   that already cite the conflict: SOURCE_LASER_IONISATION_EFF_244NM_WS2026_ZHANG, SOURCE_LASER_IONISATION_EFF_IMPLIED_G2_TARGET_WS2026_ZHANG,
   SOURCE_LASER_IONISATION_EFF_122NM_BUDGET_WS2026_ZHANG, SOURCE_MUTRISTAN_POST_STOPPING_BUDGET_WS2026_ZHANG,
   SOURCE_LASER_IONISATION_EFF_SIM_MIN_ARITOME2024, SOURCE_USM_PER_SURFACE_MUON_100KEV_ARITOME2024,
   SOURCE_LASER_IONISATION_EFF_PROJECTED_122_355NM_ARITOME2024, SOURCE_LASER_IONISATION_EFF_MUTRISTAN2022; the Kamioka
   plot readings (SOURCE_LASER_IONISATION_EFF_KAMIOKA_CM30_*, SOURCE_USM_PER_VACUUM_MUONIUM_G2_TDR_REFERENCE_WS2026_ZHANG)
   belong to the same comparison.
3. **Hand-over notes of the extractor that were wrong**: "> 7 sigma" (6.6); "(d) Beare's 3.4e-3 vs Zhang's 0.020–0.023
   differ by ~6× and are not reconciled" (different quantities; the Kamioka breakdown reproduces 3.4e-3); "(e) emittances
   … preliminary" (p.14 does not say preliminary) and the 200× gain is not attributable to laser and RFQ alone (S2 → H2);
   status counts are now analogous 423 / imported_related 55 / reported_lhmuc 26 / analytical_estimate 19 / unknown 7.
4. **CONF_JPARC_IHDTL_ENERGY**: the uploaded Nakazawa deck (p.5) now gives 4.26 MeV in full text
   (SOURCE_IHDTL_OUTPUT_ENERGY_WS2026_NAKAZAWA); the conflict record cites 4.26 MeV only at snippet level.
5. **Other agent's μLHC record** SOURCE_PION_YIELD_PER_PROTON_MULHC (`parameters/source/mulhc_ptep2026_source.yaml`) is
   named "Pion yield per proton after 40 recirculations" and quotes the μLHC paper's "enhanced pion yield of 0.016 pions
   per proton"; in the μTRISTAN original 0.016 is per traversal (item 32). Worth a note there; not edited here.
6. The test `tests/scientific/test_workshop_decks.py::test_zhang_hline_chain_and_mutristan_budget` checks the p.10
   present-intensity chain; "hline" in its name is a misnomer after item 1 (arithmetic unaffected; not edited).
7. Registries must be rebuilt (`tools/build_registries.py`) once the other addendum files pass the cap check.

## Residual doubts

1. Rogers p.3 "Need 39 m aerogel to stop 200 MeV muon — 23.4 mg/cm^3" and the 23.4 mg/cm³ density stay reported_lhmuc:
   the author's own argument on a PRIMARY_LHMUC deck, not restated from another machine, but generic physics (the record
   says so). The lead may prefer analytical_estimate.
2. Zhang p.10 g-2 column: the stopping fraction (implied 0.42) and vacuum yield (implied 0.103 = 7.21e6 / 7.01e7) it uses
   are not stated; the closeness of 0.42 to the 40 % H-line simulation is an observation only.
3. Identification of the p.10 "Intensity (/s)" column with the 2022 S2-area test is an inference (244 nm laser, MCP,
   0.1 /s vs 0.126 Hz); the slide names no beamline.
4. Zhang p.9 is an image of a slide by S. Kamioka (same workshop; his deck is not among the uploads); the four simulated
   efficiencies are read from that image (confidence medium) and the target geometry behind 6 % vacuum emission is not given.
5. Zhang p.3 "3.4 MeV": the schematic does not say where along the beamline it applies (3.4 MeV ↔ 27.0 MeV/c; compare
   4.1 MeV at production in Beare et al. and the "4 MeV" Nakazawa label).
6. Zhang p.21 tungsten emission normalisation ρ0 ≃ 60 mm⁻¹ is defined neither on the slide nor in Sakaki et al.'s text; the
   implied y = 0.040 keeps confidence low.
7. All plot readings (Zhang pp.7, 17, 18, 19, 20) are manual readings of slide images (±0.02 on the Kamioka plot, ±0.2 on
   p.17); the Kamioka arrow-to-curve assignment rests on the arrow geometry.
8. Aritome et al.: the residual factor ~3 between the implied 2.0e-6 (2.5e-6 without transport decay) and the simulated
   7e-6 lower bound is not itemised in the paper.
9. Beare et al. combine all aerogel targets for f_Mu = 0.655 while the Fig. 11 caption says "silica aerogel targets"; the
   paper itself says the discrepancy with 0.52 "is not understood well".
10. μTRISTAN "O(10⁵)" enhancement and the "(times 40 turns times 2 bunches)" bookkeeping are recorded as printed.
11. The Zhu et al. PRAB 28 (2025) 041003 article number in the LHMUC-SOURCE-HYBRID-IMCC design_version is supported only
    by MR7's reference list, not by the Rogers deck.
12. Nakazawa PDF: hidden (non-rendered) text on pp.5 and 7 was not used for any value; other hidden strings were not
    systematically searched.
13. Not recorded (low value for the LHμC twin, small print): Nakazawa p.14 inset Twiss parameters (e.g. measured
    ε = 0.8428 ± 0.042 π mm mrad, α, β) and the Rogers p.7 scan plots.
14. LHMUC-SOURCE-HYBRID-IMCC lists low_energy_cooling_efficiency, wall_plug_power and hts_radiation_tolerance both as roles
    (null records) and as unknown roles — deliberate, stated in the notes.
15. Five analytical estimates computed from refereed-paper values keep confidence `high` (SOURCE_PRE_IONISATION_CHAIN_EFF,
    SOURCE_USM_PER_SURFACE_MUON_5P7KEV, SOURCE_USM_PER_SURFACE_MUON_100KEV, SOURCE_USM_RATE_100KEV_IMPLIED (all _ARITOME2024)
    and SOURCE_USM_BUNCH_POPULATION_MUTRISTAN2022): no mechanical §4 cap applies, as for the committed _ANDRE2022 estimates,
    although their inputs are capped at medium.

## Appendix A — correction log

All 150 logged edits in application order (the script's `fix_log.json`). Ids are shown under their final name; long texts are abbreviated (the full before/after texts are in the files and in the log). Aggregate rows cover the shared-sentence, unit, check_ids and confidence-cap edits.

| # | parameter_id | field | change | reason |
|---|---|---|---|---|
| 1 | SOURCE_SURFACE_MUON_RATE_PRESENT_WS2026_ZHANG (was SOURCE_SURFACE_MUON_RATE_HLINE_WS2026_ZHANG) | provenance.applicability.explanation | text edit: → “ Column 'Intensity (/s)' of the p.10 table (present-intensity chain). The slide does not name the beamline; t…” | Mis-attribution: the 'Intensity (/s)' column is the present-intensity (S2-area-type, 244 nm laser, MCP) chain, not the H-line; on the deck the H-line appears only in the p.9 simulation and in the g-2… |
| 2 | SOURCE_STOPPED_MUON_RATE_PRESENT_WS2026_ZHANG (was SOURCE_STOPPED_MUON_RATE_HLINE_WS2026_ZHANG) | provenance.applicability.explanation | text edit: → “ Column 'Intensity (/s)' of the p.10 table (present-intensity chain). The slide does not name the beamline; t…” | Mis-attribution: the 'Intensity (/s)' column is the present-intensity (S2-area-type, 244 nm laser, MCP) chain, not the H-line; on the deck the H-line appears only in the p.9 simulation and in the g-2… |
| 3 | SOURCE_MUONIUM_FORMATION_RATE_PRESENT_WS2026_ZHANG (was SOURCE_MUONIUM_FORMATION_RATE_HLINE_WS2026_ZHANG) | provenance.applicability.explanation | text edit: → “ Column 'Intensity (/s)' of the p.10 table (present-intensity chain). The slide does not name the beamline; t…” | Mis-attribution: the 'Intensity (/s)' column is the present-intensity (S2-area-type, 244 nm laser, MCP) chain, not the H-line; on the deck the H-line appears only in the p.9 simulation and in the g-2… |
| 4 | SOURCE_MUONIUM_VACUUM_RATE_PRESENT_WS2026_ZHANG (was SOURCE_MUONIUM_VACUUM_RATE_HLINE_WS2026_ZHANG) | provenance.applicability.explanation | text edit: → “ Column 'Intensity (/s)' of the p.10 table (present-intensity chain). The slide does not name the beamline; t…” | Mis-attribution: the 'Intensity (/s)' column is the present-intensity (S2-area-type, 244 nm laser, MCP) chain, not the H-line; on the deck the H-line appears only in the p.9 simulation and in the g-2… |
| 5 | SOURCE_USM_RATE_PRESENT_244NM_WS2026_ZHANG (was SOURCE_USM_RATE_HLINE_244NM_WS2026_ZHANG) | provenance.applicability.explanation | text edit: → “ Column 'Intensity (/s)' of the p.10 table (present-intensity chain). The slide does not name the beamline; t…” | Mis-attribution: the 'Intensity (/s)' column is the present-intensity (S2-area-type, 244 nm laser, MCP) chain, not the H-line; on the deck the H-line appears only in the p.9 simulation and in the g-2… |
| 6 | SOURCE_USM_RATE_AFTER_EXTRACTION_PRESENT_WS2026_ZHANG (was SOURCE_USM_RATE_AFTER_EXTRACTION_HLINE_WS2026_ZHANG) | provenance.applicability.explanation | text edit: → “ Column 'Intensity (/s)' of the p.10 table (present-intensity chain). The slide does not name the beamline; t…” | Mis-attribution: the 'Intensity (/s)' column is the present-intensity (S2-area-type, 244 nm laser, MCP) chain, not the H-line; on the deck the H-line appears only in the p.9 simulation and in the g-2… |
| 7 | SOURCE_USM_RATE_AT_MCP_PRESENT_WS2026_ZHANG (was SOURCE_USM_RATE_AT_MCP_HLINE_WS2026_ZHANG) | provenance.applicability.explanation | text edit: → “ Column 'Intensity (/s)' of the p.10 table (present-intensity chain). The slide does not name the beamline; t…” | Mis-attribution: the 'Intensity (/s)' column is the present-intensity (S2-area-type, 244 nm laser, MCP) chain, not the H-line; on the deck the H-line appears only in the p.9 simulation and in the g-2… |
| 8 | SOURCE_SURFACE_MUON_RATE_HLINE_WS2026_ZHANG | parameter_id | SOURCE_SURFACE_MUON_RATE_HLINE_WS2026_ZHANG → SOURCE_SURFACE_MUON_RATE_PRESENT_WS2026_ZHANG | Id encoded 'HLINE' for the p.10 present-intensity column, which is not the H-line (see the applicability correction); renamed. The id was referenced only inside this file. |
| 9 | SOURCE_STOPPED_MUON_RATE_HLINE_WS2026_ZHANG | parameter_id | SOURCE_STOPPED_MUON_RATE_HLINE_WS2026_ZHANG → SOURCE_STOPPED_MUON_RATE_PRESENT_WS2026_ZHANG | Id encoded 'HLINE' for the p.10 present-intensity column, which is not the H-line (see the applicability correction); renamed. The id was referenced only inside this file. |
| 10 | SOURCE_MUONIUM_FORMATION_RATE_HLINE_WS2026_ZHANG | parameter_id | SOURCE_MUONIUM_FORMATION_RATE_HLINE_WS2026_ZHANG → SOURCE_MUONIUM_FORMATION_RATE_PRESENT_WS2026_ZHANG | Id encoded 'HLINE' for the p.10 present-intensity column, which is not the H-line (see the applicability correction); renamed. The id was referenced only inside this file. |
| 11 | SOURCE_MUONIUM_VACUUM_YIELD_HLINE_WS2026_ZHANG | parameter_id | SOURCE_MUONIUM_VACUUM_YIELD_HLINE_WS2026_ZHANG → SOURCE_MUONIUM_VACUUM_YIELD_DIFFUSION_MODEL_WS2026_ZHANG | Id encoded 'HLINE' for the p.10 present-intensity column, which is not the H-line (see the applicability correction); renamed. The id was referenced only inside this file. |
| 12 | SOURCE_MUONIUM_VACUUM_RATE_HLINE_WS2026_ZHANG | parameter_id | SOURCE_MUONIUM_VACUUM_RATE_HLINE_WS2026_ZHANG → SOURCE_MUONIUM_VACUUM_RATE_PRESENT_WS2026_ZHANG | Id encoded 'HLINE' for the p.10 present-intensity column, which is not the H-line (see the applicability correction); renamed. The id was referenced only inside this file. |
| 13 | SOURCE_USM_RATE_HLINE_244NM_WS2026_ZHANG | parameter_id | SOURCE_USM_RATE_HLINE_244NM_WS2026_ZHANG → SOURCE_USM_RATE_PRESENT_244NM_WS2026_ZHANG | Id encoded 'HLINE' for the p.10 present-intensity column, which is not the H-line (see the applicability correction); renamed. The id was referenced only inside this file. |
| 14 | SOURCE_USM_PER_SURFACE_MUON_HLINE_244NM_WS2026_ZHANG | parameter_id | SOURCE_USM_PER_SURFACE_MUON_HLINE_244NM_WS2026_ZHANG → SOURCE_USM_PER_SURFACE_MUON_PRESENT_244NM_WS2026_ZHANG | Id encoded 'HLINE' for the p.10 present-intensity column, which is not the H-line (see the applicability correction); renamed. The id was referenced only inside this file. |
| 15 | SOURCE_USM_RATE_AFTER_EXTRACTION_HLINE_WS2026_ZHANG | parameter_id | SOURCE_USM_RATE_AFTER_EXTRACTION_HLINE_WS2026_ZHANG → SOURCE_USM_RATE_AFTER_EXTRACTION_PRESENT_WS2026_ZHANG | Id encoded 'HLINE' for the p.10 present-intensity column, which is not the H-line (see the applicability correction); renamed. The id was referenced only inside this file. |
| 16 | SOURCE_USM_RATE_AT_MCP_HLINE_WS2026_ZHANG | parameter_id | SOURCE_USM_RATE_AT_MCP_HLINE_WS2026_ZHANG → SOURCE_USM_RATE_AT_MCP_PRESENT_WS2026_ZHANG | Id encoded 'HLINE' for the p.10 present-intensity column, which is not the H-line (see the applicability correction); renamed. The id was referenced only inside this file. |
| 17 | SOURCE_STOPPED_MUON_RATE_G2_TARGET_WS2026_ZHANG | validation.notes | text edit: → “the g-2 column evidently uses a different stopping fraction, not stated on the slide. The implied 0.42 is clo…” | Added the observation that links the unexplained 0.42 to the p.9 H-line simulation (without asserting it). |
| 18 | SOURCE_MUONIUM_DIFFUSION_CONSTANT_FIT_WS2026_ZHANG | uncertainty.note | roughly 855-890 cm^2/s → roughly 850-890 cm^2/s | Plot reading corrected: the chi2_min + 2.30 (green) contour on p.7 reaches 850 cm^2/s at T = 322 K. |
| 19 | SOURCE_MUONIUM_THERMAL_VELOCITY_WS2026_ZHANG | validation.notes | text edit: → “sqrt(8kT/(π m_Mu)) at the fitted T = 322 K = 7.7 mm/μs (7.5 mm/μs at 300 K), consistent with '~7'.” | Arithmetic error: with m_Mu = 106.17 MeV/c^2 the mean speed at 322 K is 7.73 mm/us, not 7.5. |
| 20 | SOURCE_MULTILAYER_VALIDATION_PROPOSAL_LASER_RADIUS_WS2026_ZHANG | provenance.applicability.explanation | reflection (about 700-1230 ns) → reflection (about 650-1230 ns) | Plot reading corrected: the reflection-model curve on p.18 dips to about 645-650 ns at z = 5 mm and z = 19 mm. |
| 21 | SOURCE_IONISATION_TEST_FLIGHT_PATH_WS2026_ZHANG | name | text edit: → “Length annotated '~ 3 m' on the photograph of the 2022 S2-area ionisation-test setup (taken here as the aerog…” | The slide only draws a '~ 3 m' arrow across the photograph; calling it the aerogel-to-MCP flight path is an interpretation and is now labelled as such. |
| 22 | SOURCE_IONISATION_TEST_FLIGHT_PATH_WS2026_ZHANG | provenance.confidence | medium → low | Meaning of the annotation is interpretive (value read correctly). |
| 23 | SOURCE_MULTILAYER_VERTICAL_VARIANT_WS2026_ZHANG | provenance.applicability.explanation | text edit: → “(design variant). Hamada et al. p.7 describe the aerogel target as having 'a layer structure in the vertical …” | Added the μTRISTAN-paper sentence that supports the 'muTRISTAN took this idea' attribution. |
| 24 | SOURCE_MULTILAYER_VERTICAL_VARIANT_YIELD_GAIN_4LAYERS_WS2026_ZHANG | provenance.status | imported_related → analogous | The yield gains are Zhang's unpublished target simulation shown on p.19, not values of the μTRISTAN paper; status imported_related -> analogous. |
| 25 | SOURCE_MULTILAYER_VERTICAL_VARIANT_YIELD_GAIN_4LAYERS_WS2026_ZHANG | provenance.applicability.category | design_variant → analogous | Follows the status change. |
| 26 | SOURCE_MULTILAYER_VERTICAL_VARIANT_YIELD_GAIN_4LAYERS_WS2026_ZHANG | provenance.applicability.explanation | text edit: → “Zhang's own simulation of the vertical multi-layer aerogel variant ('Yet another version (not published in my…” | The explanation attributed the numbers to Hamada et al. PTEP 2022, which does not contain them. |
| 27 | SOURCE_MULTILAYER_VERTICAL_VARIANT_YIELD_GAIN_MAX_WS2026_ZHANG | provenance.status | imported_related → analogous | The yield gains are Zhang's unpublished target simulation shown on p.19, not values of the μTRISTAN paper; status imported_related -> analogous. |
| 28 | SOURCE_MULTILAYER_VERTICAL_VARIANT_YIELD_GAIN_MAX_WS2026_ZHANG | provenance.applicability.category | design_variant → analogous | Follows the status change. |
| 29 | SOURCE_MULTILAYER_VERTICAL_VARIANT_YIELD_GAIN_MAX_WS2026_ZHANG | provenance.applicability.explanation | text edit: → “Zhang's own simulation of the vertical multi-layer aerogel variant ('Yet another version (not published in my…” | The explanation attributed the numbers to Hamada et al. PTEP 2022, which does not contain them. |
| 30 | SOURCE_MUTRISTAN_NEW_TARGET_MATERIAL_WS2026_ZHANG | provenance.applicability.explanation | text edit: → “New μTRISTAN version (hybrid liquid-lithium / multi-layer hot-tungsten target): the layout figure and the N_t…” | Mis-attribution: the 'new version' slide (p.21) shows the Sakaki et al. 2026 hybrid target (uploaded, batch 7), not the 2022 μTRISTAN paper. |
| 31 | SOURCE_MUTRISTAN_NEW_PROTON_TARGET_WS2026_ZHANG | provenance.applicability.explanation | text edit: → “New μTRISTAN version (hybrid liquid-lithium / multi-layer hot-tungsten target): the layout figure and the N_t…” | Mis-attribution: the 'new version' slide (p.21) shows the Sakaki et al. 2026 hybrid target (uploaded, batch 7), not the 2022 μTRISTAN paper. |
| 32 | SOURCE_MUTRISTAN_NEW_SLOW_MUON_ENERGY_RANGE_WS2026_ZHANG | provenance.applicability.explanation | text edit: → “New μTRISTAN version (hybrid liquid-lithium / multi-layer hot-tungsten target): the layout figure and the N_t…” | Mis-attribution: the 'new version' slide (p.21) shows the Sakaki et al. 2026 hybrid target (uploaded, batch 7), not the 2022 μTRISTAN paper. |
| 33 | SOURCE_MUTRISTAN_NEW_USM_RATE_PER_MW_WS2026_ZHANG | provenance.applicability.explanation | text edit: → “New μTRISTAN version (hybrid liquid-lithium / multi-layer hot-tungsten target): the layout figure and the N_t…” | Mis-attribution: the 'new version' slide (p.21) shows the Sakaki et al. 2026 hybrid target (uploaded, batch 7), not the 2022 μTRISTAN paper. |
| 34 | SOURCE_MUTRISTAN_NEW_USM_RATE_PER_MW_WS2026_ZHANG | notes | text edit: → “Record holds the prefactor 1.2e12 /s per MW; multiply by eta_conv (unknown) and the beam power in MW. N_tot i…” | Definition of N_tot supplied from the uploaded original. |
| 35 | SOURCE_MUTRISTAN_NEW_CONVERSION_EFFICIENCY_WS2026_ZHANG | provenance.applicability.explanation | text edit: → “Symbol appears in the formula; no value is given on the deck. The same symbol is left unquantified by the ori…” | The record claimed the new μTRISTAN paper is 'not in the uploaded set'; it is (batch 7, Sakaki et al. 2026) and also leaves eta_conv unquantified. |
| 36 | SOURCE_TUNGSTEN_MUONIUM_TEMPERATURE_WS2026_ZHANG | provenance.applicability.explanation | text edit: → “analogous technology for a tungsten-based LHμC source option. Sakaki et al. 2026 p.4 likewise assume T = 2000…” | Cross-reference to the uploaded originals that carry the same assumption. |
| 37 | SOURCE_TUNGSTEN_MUONIUM_DIFFUSION_CONSTANT_WS2026_ZHANG | provenance.applicability.explanation | text edit: → “4e5 x smaller than the aerogel value 870 cm^2/s. Same value in Sakaki et al. 2026 p.4 (citing Mills et al., P…” | Cross-reference to the uploaded original. |
| 38 | SOURCE_TUNGSTEN_MUONIUM_EMISSION_YIELD_IMPLIED_WS2026_ZHANG | notes | text edit: → “Low confidence: formula normalisation not stated on the slide. The functional form matches Sakaki et al. 2026…” | Context for the low-confidence audit evaluation. |
| 39 | SOURCE_LASER_IONISATION_EFF_KAMIOKA_CM30_122NM100UJ_WS2026_ZHANG | provenance.source.quotation | text edit: → “This is the really new challenge for lasers!! 2-1: O(10)μJ to 100μJ @122nm (+ more 355nm) 2-2: 10mJ (40mJ) to…” | The quoted 'Phase2-1 122nm 100μJ ...' annotation points at the 40 mJ (green) curve; the recorded value is the 300 mJ (blue) curve at 100 μJ, which the 'Phase2-2 Both laser are ready' arrow marks. |
| 40 | SOURCE_LASER_IONISATION_EFF_KAMIOKA_CM30_122NM100UJ_WS2026_ZHANG | notes | text edit: → “10 mJ about 0.015. The 'Phase2-1 122nm 100μJ' arrow marks the 40 mJ curve (about 0.04).” | Plot re-read at 250 dpi; orange (10 mJ) curve is about 0.014 at 100 μJ. |
| 41 | SOURCE_MUONIUM_DIFFUSION_LENGTH_WS2026_ZHANG | notes | text edit: → “the deck does not reconcile the two numbers, which come from different model fits (Zhang et al. 2022 vs the e…” | Removed an unsupported interpretation ('different definitions'). |
| 42 | SOURCE_MUONIUM_FORMATION_FRACTION_TRIUMF_WS2026_ZHANG | validation.methods | text edit: → “["(0.655 - 0.52)/sqrt(0.01^2 + 0.018^2) = 6.6 sigma between the Bakule et al. 2013 MuSR value 0.52 +- 0.01 an…” | Lead note 2026-10-29: '> 7 sigma' corrected to 6.6 sigma with both uncertainties (7.5 sigma with Beare's alone). |
| 43 | SOURCE_MUONIUM_FORMATION_FRACTION_TRIUMF_WS2026_ZHANG | validation.check_ids | text edit: → “["tests/scientific/test_batch9_documents.py::test_bakule2013_formation_fraction_vs_beare2020_combined_signifi…” | check_ids filled with the two pinning tests. |
| 44 | SOURCE_MUONIUM_FORMATION_FRACTION_TRIUMF_WS2026_ZHANG | provenance.applicability.explanation | text edit: → “— CONF_MUONIUM_FORMATION_FRACTION, 6.6 sigma apart with both uncertainties. Origin of the 0.52 'from TRIUMF m…” | Lead note 2026-10-29: name the origin of the 0.52 cited 'from TRIUMF measurement'. |
| 45 | SOURCE_MUTRISTAN_POST_STOPPING_BUDGET_WS2026_ZHANG | notes | text edit: → “The 0.52 input is the Bakule et al. 2013 MuSR value (0.52 +- 0.01, SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAK…” | Lead note 2026-10-29: name the origin of the 0.52; shows the sensitivity to CONF_MUONIUM_FORMATION_FRACTION. |
| 46 | SOURCE_MUONIUM_VACUUM_YIELD_MULTILAYER_BUDGET_WS2026_ZHANG | notes | text edit: → “p.20 bullet for the formation factor of the same budget: '0.52: Muonium formation in aerogel (measurement fro…” | Lead note 2026-10-29: name the origin wherever the p.20 budget is restated. |
| 47 | SOURCE_MUONIUM_FORMATION_RATE_PRESENT_WS2026_ZHANG | notes | text edit: → “The quoted row's efficiency '0.52 (from TRIUMF measurement)', which this present-intensity rate uses, is the …” | Lead note 2026-10-29: name the origin wherever the 0.52 is cited 'from TRIUMF measurement' (the quotation of this record contains it). |
| 48 | SOURCE_MUONIUM_FORMATION_RATE_G2_TARGET_WS2026_ZHANG | notes | text edit: → “The quoted row's efficiency '0.52 (from TRIUMF measurement)', which this g-2 target rate uses, is the Bakule …” | Lead note 2026-10-29: name the origin wherever the 0.52 is cited 'from TRIUMF measurement' (the quotation of this record contains it). |
| 49 | SOURCE_MULTILAYER_OPTIMAL_INTERVAL_WS2026_ZHANG | provenance.status | analogous → analytical_estimate | research/source_quality_policy.md §5.3: numbers read off a plot axis of a slide are analytical_estimate with the reading method in derivation (re-read on a 200 dpi render of the page). |
| 50 | SOURCE_MULTILAYER_OPTIMAL_INTERVAL_WS2026_ZHANG | provenance.derivation | text edit: → “Read off the p.17 left plot 'Mu inside laser region [a.u.] vs Interval [mm]' (scan points 3-9 mm): the highes…” | Reading method recorded as the derivation (follows the status change). |
| 51 | SOURCE_MULTILAYER_THERMAL_MUON_YIELD_GAIN_122NM500UJ_355NM1P5J_WS2026_ZHANG | provenance.status | analogous → analytical_estimate | research/source_quality_policy.md §5.3: numbers read off a plot axis of a slide are analytical_estimate with the reading method in derivation (re-read on a 200 dpi render of the page). |
| 52 | SOURCE_MULTILAYER_THERMAL_MUON_YIELD_GAIN_122NM500UJ_355NM1P5J_WS2026_ZHANG | provenance.derivation | text edit: → “Read off the p.17 right plot 'Thermal muon yield [a.u.] vs Interval [mm]' (blue triangles, legend '122 nm of …” | Reading method recorded as the derivation (follows the status change). |
| 53 | SOURCE_MULTILAYER_THERMAL_MUON_YIELD_GAIN_122NM100UJ_355NM1P5J_WS2026_ZHANG | provenance.status | analogous → analytical_estimate | research/source_quality_policy.md §5.3: numbers read off a plot axis of a slide are analytical_estimate with the reading method in derivation (re-read on a 200 dpi render of the page). |
| 54 | SOURCE_MULTILAYER_THERMAL_MUON_YIELD_GAIN_122NM100UJ_355NM1P5J_WS2026_ZHANG | provenance.derivation | text edit: → “Read off the p.17 right plot 'Thermal muon yield [a.u.] vs Interval [mm]' (red squares, legend '122 nm of 100…” | Reading method recorded as the derivation (follows the status change). |
| 55 | SOURCE_MULTILAYER_THERMAL_MUON_YIELD_GAIN_122NM100UJ_355NM300MJ_WS2026_ZHANG | provenance.status | analogous → analytical_estimate | research/source_quality_policy.md §5.3: numbers read off a plot axis of a slide are analytical_estimate with the reading method in derivation (re-read on a 200 dpi render of the page). |
| 56 | SOURCE_MULTILAYER_THERMAL_MUON_YIELD_GAIN_122NM100UJ_355NM300MJ_WS2026_ZHANG | provenance.derivation | text edit: → “Read off the p.17 right plot 'Thermal muon yield [a.u.] vs Interval [mm]' (green circles, legend '122 nm of 1…” | Reading method recorded as the derivation (follows the status change). |
| 57 | SOURCE_LASER_IONISATION_EFF_KAMIOKA_CM30_122NM100UJ_WS2026_ZHANG | provenance.status | analogous → analytical_estimate | research/source_quality_policy.md §5.3: numbers read off a plot axis of a slide are analytical_estimate with the reading method in derivation (re-read on a 200 dpi render of the page). |
| 58 | SOURCE_LASER_IONISATION_EFF_KAMIOKA_CM30_122NM100UJ_WS2026_ZHANG | provenance.derivation | text edit: → “Read off the reproduced p.20 plot 'USM/vacuum emitted Mu vs 122nm pulse energy [μJ]' (S. Kamioka at E34 CM30)…” | Reading method recorded as the derivation (follows the status change). |
| 59 | SOURCE_LASER_IONISATION_EFF_KAMIOKA_CM30_MAX_WS2026_ZHANG | provenance.status | analogous → analytical_estimate | research/source_quality_policy.md §5.3: numbers read off a plot axis of a slide are analytical_estimate with the reading method in derivation (re-read on a 200 dpi render of the page). |
| 60 | SOURCE_LASER_IONISATION_EFF_KAMIOKA_CM30_MAX_WS2026_ZHANG | provenance.derivation | text edit: → “Read off the same reproduced p.20 plot: end point of the red curve '355nm: 600mJ, t=1.35 μs, y_laser=0 mm' at…” | Reading method recorded as the derivation (follows the status change). |
| 61 | SOURCE_USM_PER_VACUUM_MUONIUM_G2_TDR_REFERENCE_WS2026_ZHANG | provenance.status | analogous → analytical_estimate | research/source_quality_policy.md §5.3: numbers read off a plot axis of a slide are analytical_estimate with the reading method in derivation (re-read on a 200 dpi render of the page). |
| 62 | SOURCE_USM_PER_VACUUM_MUONIUM_G2_TDR_REFERENCE_WS2026_ZHANG | provenance.derivation | text edit: → “Read off the same reproduced p.20 plot: height of the magenta dash-dot line labelled 'TDR reference' in the l…” | Reading method recorded as the derivation (follows the status change). |
| 63 | SOURCE_USM_PER_VACUUM_MUONIUM_G2_TDR_REFERENCE_WS2026_ZHANG | name | (dashed line on the Kamioka plot) → (dash-dot line on the Kamioka plot) | The legend draws 'TDR reference' as a dash-dot line. |
| 64 | SOURCE_USM_PER_VACUUM_MUONIUM_G2_TDR_REFERENCE_WS2026_ZHANG | provenance.source.table_figure_or_equation | dashed line → dash-dot line 'TDR reference' | The legend draws 'TDR reference' as a dash-dot line. |
| 65 | SOURCE_HYBRID_CONCEPT_WS2026_ROGERS | value | text edit: → “imcc_capture_rectilinear_stage_a_cooling_deceleration_low_energy_cooling” | The deck (p.5) says only 'Low energy cooling' and lists laser-ionisation and frictional cooling as options (p.2); the value must not select laser ionisation. |
| 66 | 13 Rogers records (shared concept sentence) | provenance.applicability.explanation | low-energy laser-ionisation cooling) → low-energy muon cooling, laser-ionisation or frictional) | The deck does not choose laser ionisation over frictional cooling for the low-energy stage. |
| 67 | SOURCE_HYBRID_STAGE_A4_LONGITUDINAL_EMITTANCE_NSMEV_WS2026_ROGERS | provenance.status | reported_lhmuc → analogous | Unit conversion of the IMCC (Zhu et al.) stage-A4 value; restated IMCC numbers are analogous, so reported_lhmuc was wrong. |
| 68 | SOURCE_HYBRID_STAGE_A4_LONGITUDINAL_EMITTANCE_NSMEV_WS2026_ROGERS | provenance.applicability.category | direct → analogous | Follows the status change. |
| 69 | SOURCE_HYBRID_STAGE_A4_LONGITUDINAL_EMITTANCE_NSMEV_WS2026_ROGERS | provenance.applicability.explanation | text edit: → “IMCC stage-A4 value of Zhu et al. (SOURCE_HYBRID_RECT_A4_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, 1.741 mm) rest…” | Explanation rewritten for the status change. |
| 70 | SOURCE_HYBRID_STAGE_A4_LONGITUDINAL_EMITTANCE_NSMEV_WS2026_ROGERS | validation.notes | text edit: → “Audit arithmetic: 1.741e-3 m x 105.658 MeV / 0.299792 m/ns = 0.614 ns MeV, consistent with 0.6.” | Audit arithmetic restated with full precision. |
| 71 | SOURCE_HYBRID_RECT_START_TRANSVERSE_EMITTANCE_WS2026_ROGERS | notes | text edit: → “Unit as printed ('mm'); the slide does not state the emittance convention (normalised/rms).” | The convention is not stated on the slide (external knowledge removed). |
| 72 | SOURCE_HYBRID_RECT_A1_TRANSVERSE_EMITTANCE_WS2026_ROGERS | notes | text edit: → “Unit as printed ('mm'); the slide does not state the emittance convention (normalised/rms).” | The convention is not stated on the slide (external knowledge removed). |
| 73 | SOURCE_HYBRID_RECT_A2_TRANSVERSE_EMITTANCE_WS2026_ROGERS | notes | text edit: → “Unit as printed ('mm'); the slide does not state the emittance convention (normalised/rms).” | The convention is not stated on the slide (external knowledge removed). |
| 74 | SOURCE_HYBRID_RECT_A3_TRANSVERSE_EMITTANCE_WS2026_ROGERS | notes | text edit: → “Unit as printed ('mm'); the slide does not state the emittance convention (normalised/rms).” | The convention is not stated on the slide (external knowledge removed). |
| 75 | SOURCE_HYBRID_RECT_A4_TRANSVERSE_EMITTANCE_WS2026_ROGERS | notes | text edit: → “Unit as printed ('mm'); the slide does not state the emittance convention (normalised/rms).” | The convention is not stated on the slide (external knowledge removed). |
| 76 | SOURCE_HYBRID_DECEL_TARGET_BUNCH_LENGTH_WS2026_ROGERS | provenance.applicability.explanation | text edit: → “Compare the ~2 ns FWHM ultraslow-muon pulse at the J-PARC RFQ entrance (Nakazawa deck pp.3, 9, 16; SOURCE_USM…” | The 2 ns FWHM on the Nakazawa deck is the laser-ionised ultraslow-muon pulse, not a surface-muon pulse. |
| 77 | SOURCE_HYBRID_RF_BREAKDOWN_GRADIENT_CU_0T_WS2026_ROGERS | provenance.applicability.explanation | (Fermilab MuCool Test Area) → (Fermilab) | 'MuCool Test Area' is not on the slide (slide: 'Bowring et al, PRAB 23 072001, 2020 (Fermilab)'). |
| 78 | SOURCE_HYBRID_RF_BREAKDOWN_GRADIENT_CU_3T_WS2026_ROGERS | provenance.applicability.explanation | (Fermilab MuCool Test Area) → (Fermilab) | 'MuCool Test Area' is not on the slide (slide: 'Bowring et al, PRAB 23 072001, 2020 (Fermilab)'). |
| 79 | SOURCE_HYBRID_RF_BREAKDOWN_GRADIENT_BE_0T_WS2026_ROGERS | provenance.applicability.explanation | (Fermilab MuCool Test Area) → (Fermilab) | 'MuCool Test Area' is not on the slide (slide: 'Bowring et al, PRAB 23 072001, 2020 (Fermilab)'). |
| 80 | SOURCE_HYBRID_RF_BREAKDOWN_GRADIENT_BE_3T_WS2026_ROGERS | provenance.applicability.explanation | (Fermilab MuCool Test Area) → (Fermilab) | 'MuCool Test Area' is not on the slide (slide: 'Bowring et al, PRAB 23 072001, 2020 (Fermilab)'). |
| 81 | SOURCE_HYBRID_PROTON_DRIVER_ENERGY_WS2026_ROGERS | provenance.applicability.explanation | text edit: → “Proton energy of the author's yield estimate (p.14: 'per 5 GeV proton on target'), i.e. the IMCC proton-drive…” | The previous text said the energy came 'through the reproduced performance table', which does not show it. |
| 82 | SOURCE_HYBRID_AEROGEL_STOPPING_LENGTH_200MEV_WS2026_ROGERS | validation.notes | text edit: → “Audit arithmetic (not pinned in a test): Bethe-Bloch CSDA integration for SiO2 (PDG <Z/A> = 0.4993, I = 139.2…” | Independent check of the slide value added (verifier's scratchpad verify_g2/range_check.py). |
| 83 | SOURCE_HYBRID_MU_PER_PROTON_END_STAGE_A_WS2026_ROGERS | notes | text edit: → “Compare μTRISTAN's 5.5e-4 ultra-cold μ+ per 3 GeV proton per pass of the pion production ring (SOURCE_USM_PER…” | The μTRISTAN 5.5e-4 is per pass through the production target (see the μTRISTAN corrections); the per-proton total is 0.022. |
| 84 | SOURCE_JPARC_STEP1_SETUP_LENGTH_WS2026_NAKAZAWA | parameter_id | SOURCE_JPARC_STEP1_SETUP_LENGTH_WS2026_NAKAZAWA → SOURCE_JPARC_PROTO_RFQ_LENGTH_FIGURE_WS2026_NAKAZAWA | The p.8 '~ 2 m' arrow spans the prototype RFQ, not the setup; id renamed (referenced only in this file). |
| 85 | SOURCE_JPARC_PROTO_RFQ_LENGTH_FIGURE_WS2026_NAKAZAWA | name | text edit: → “Length of the prototype RFQ in the Step 1 (2024) schematic (figure label '~ 2 m')” | The arrow spans the prototype RFQ box. |
| 86 | SOURCE_JPARC_PROTO_RFQ_LENGTH_FIGURE_WS2026_NAKAZAWA | provenance.applicability.explanation | text edit: → “J-PARC muon g-2/EDM front-end (RFQ / IH-DTL) design value or measurement restated on a PRIMARY_LHMUC deck; an…” | Meaning of the label made explicit. |
| 87 | SOURCE_JPARC_STEP2_SETUP_LENGTH_WS2026_NAKAZAWA | parameter_id | SOURCE_JPARC_STEP2_SETUP_LENGTH_WS2026_NAKAZAWA → SOURCE_JPARC_FULL_RFQ_LENGTH_FIGURE_WS2026_NAKAZAWA | The p.8 '~ 3 m' arrow spans the full-scale RFQ, not the setup; id renamed (referenced only in this file). |
| 88 | SOURCE_JPARC_FULL_RFQ_LENGTH_FIGURE_WS2026_NAKAZAWA | name | text edit: → “Length of the full-scale RFQ in the Step 2 (2026) schematic (figure label '~ 3 m')” | The arrow spans the RFQ box. |
| 89 | SOURCE_JPARC_FULL_RFQ_LENGTH_FIGURE_WS2026_NAKAZAWA | provenance.applicability.explanation | text edit: → “J-PARC muon g-2/EDM front-end (RFQ / IH-DTL) design value or measurement restated on a PRIMARY_LHMUC deck; an…” | Meaning of the label made explicit. |
| 90 | SOURCE_IHDTL_MULTISTAGE_TEST_SCHEDULE_WS2026_NAKAZAWA | provenance.source.page | 5 → 8 | The quoted p.5 sentence exists only in the PDF text layer (pp.5 and 7) and is not rendered on either slide; the visible statement is on p.8. |
| 91 | SOURCE_IHDTL_MULTISTAGE_TEST_SCHEDULE_WS2026_NAKAZAWA | provenance.source.section | IH-DTL : Inter-digital H-mode Drift Tube Linac → acceleration test (2024 ~ ) | Section of p.8. |
| 92 | SOURCE_IHDTL_MULTISTAGE_TEST_SCHEDULE_WS2026_NAKAZAWA | provenance.source.table_figure_or_equation | null → 'Step 3' box | Location of the visible statement. |
| 93 | SOURCE_IHDTL_MULTISTAGE_TEST_SCHEDULE_WS2026_NAKAZAWA | provenance.source.quotation | text edit: → “Step 3 Multistage Acceleration w/ 324-MHz IH-DTL. ④ Medium energy beam transport line ⑤ IH-DTL → Future (~202…” | Quotation replaced by the visible p.8 text. |
| 94 | SOURCE_IHDTL_MULTISTAGE_TEST_SCHEDULE_WS2026_NAKAZAWA | uncertainty | {"type": "not_stated"} → {"type": "not_stated", "note": "source says '~2028'"} | The visible source gives '~2028'. |
| 95 | SOURCE_IHDTL_MULTISTAGE_TEST_SCHEDULE_WS2026_NAKAZAWA | provenance.applicability.explanation | text edit: → “J-PARC muon g-2/EDM front-end (RFQ / IH-DTL) design value or measurement restated on a PRIMARY_LHMUC deck; an…” | Removed the p.8 cross-reference now that p.8 is the cited page. |
| 96 | SOURCE_IHDTL_MULTISTAGE_TEST_SCHEDULE_WS2026_NAKAZAWA | notes | text edit: → “The sentence 'Multi-stage acceleration demonstration tests using the 324 MHz IH-DTL are scheduled for 2028.' …” | Documents the hidden-text finding. |
| 97 | SOURCE_USM_NORM_EMITTANCE_X_MEASURED_340KEV_WS2026_NAKAZAWA | name | (Q-scan, preliminary) → (Q-scan; discrepancy with simulation under investigation) | p.14 does not label the emittance result 'preliminary' (the TOF and bunch plots on pp.13, 15 are); it says the discrepancies are 'under investigation'. |
| 98 | SOURCE_USM_NORM_EMITTANCE_Y_MEASURED_340KEV_WS2026_NAKAZAWA | name | (Q-scan, preliminary) → (Q-scan; discrepancy with simulation under investigation) | p.14 does not label the emittance result 'preliminary' (the TOF and bunch plots on pp.13, 15 are); it says the discrepancies are 'under investigation'. |
| 99 | SOURCE_USM_PER_PULSE_PRESENT_WS2026_NAKAZAWA | notes | text edit: → “0.4 / 2e-3 = 200. The deck does not break the gain down: the 2026 run used the upgraded laser (~2 ns pulse), …” | The attribution of the gain to the laser and RFQ alone was not supported; the beamline/area also changed. |
| 100 | SOURCE_RFQ_REDESIGN_OPTIONS_WS2026_NAKAZAWA | notes | text edit: → “(J-STAGE URL on the slide: pjab/95/7, i.e. Proc. Jpn. Acad. Ser. B vol. 95 no. 7)” | The year is not on the slide; only the URL is. |
| 101 | SOURCE_IHDTL_OUTPUT_ENERGY_WS2026_NAKAZAWA | provenance.applicability.explanation | text edit: → “See CONF_JPARC_IHDTL_ENERGY for the values quoted elsewhere; this uploaded deck (p.5) is the first non-snippe…” | Note for the registry stage. |
| 102 | SOURCE_MUON_STOPPING_EFF_ARITOME2024 | provenance.applicability.explanation | text edit: → “Compare 0.467 in the present-intensity chain of the Zhang deck (p.10, SOURCE_MUON_STOPPING_FRACTION_AEROGEL_W…” | The Zhang p.10 chain is not the H-line (see the Zhang corrections). |
| 103 | SOURCE_MUONIUM_CONVERSION_EFF_ARITOME2024 | provenance.applicability.explanation | text edit: → “ref. [21] is P. Bakule et al., PTEP 2013 103C01, whose MuSR value is 0.52 ± 0.01 for three 2013 aerogel sampl…” | Lead note 2026-10-29: origin and corrected significance. |
| 104 | SOURCE_USM_PER_SURFACE_MUON_5P7KEV_ARITOME2024 | provenance.applicability.explanation | text edit: → “Demonstrated chain efficiency before RF acceleration. Dividing by the pre-ionisation product 0.0208 implies a…” | Wrong reasoning: the implied value is BELOW the simulated range even after the decay loss; the '10-40 % lower laser energy' applies to the 100 keV measurement, not to this 5.7 keV one. |
| 105 | SOURCE_USM_PER_SURFACE_MUON_5P7KEV_ARITOME2024 | provenance.source.quotation | text edit: → “(4.0 ± 0.4) × 10^−3 µ+ /pulse ... (p.2) 9.5 × 10^4 muons per pulse” | Page marker added: the second fragment is on p.2. |
| 106 | SOURCE_USM_PER_SURFACE_MUON_5P7KEV_ARITOME2024 | provenance.source.page | 3 → 3, 2 | Quotation spans two pages. |
| 107 | SOURCE_USM_PER_SURFACE_MUON_5P7KEV_ARITOME2024 | validation.methods | text edit: → “["4.0e-3 / 9.5e4 = 4.2e-8; implied ionisation x transport = 4.2e-8 / 0.0208 = 2.0e-6, asserted inside the win…” | Wording: '1.5e-6-2.5e-6' is the test's acceptance window around the implied 2.0e-6, not a range of the implied value. |
| 108 | SOURCE_RFQ_DESIGN_HMINUS_ENERGY_ARITOME2024 | provenance.applicability.explanation | text edit: → “Prototype RFQ, not the full-scale RFQ (3 MeV H- design, 0.34 MeV for μ+) used in the 2026 test (Nakazawa deck…” | Clarified: the full-scale RFQ accelerates μ+ to 0.34 MeV, not 3 MeV. |
| 109 | SOURCE_DIAG_QM_GRADIENT_PER_AMPERE_ARITOME2024 | unit | T/m → tesla/meter/ampere | The stored coefficient is a gradient per ampere ('2.25 × Ii (T/m)'); 'T/m' was dimensionally wrong. |
| 110 | SOURCE_DIAG_QM_GRADIENT_PER_AMPERE_ARITOME2024 | notes | text edit: → “Gradient coefficient per ampere of magnet current ('field gradients of 2.25 × Ii (T/m)').” | Follows the unit fix. |
| 111 | SOURCE_HLINE_SURFACE_MU_GAIN_ARITOME2024 | notes | text edit: → “The paper does not name the beamline; its ref. [35] (Kawamura et al., PTEP 2018 113G01, 'New concept for a la…” | The '(H-line)' in the name rests on the reference, not on the text; made explicit. |
| 112 | SOURCE_USM_RATE_100KEV_IMPLIED_ARITOME2024 | notes | text edit: → “Assumes every 25 Hz RCS pulse reaches the MLF; the paper does not state the delivered pulse rate.” | Caveat on the audit product. |
| 113 | SOURCE_LASER_WAVELENGTH_ARITOME2024 | provenance.source.page | 2 → 2-3 | Quotation runs from p.2 onto p.3. |
| 114 | SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020 | validation.methods | text edit: → “["2 x 0.155 / 0.474 = 0.654 reproduces Eq. (4) (audit arithmetic, not pinned). (0.655 - 0.52)/sqrt(0.01^2 + 0…” | Lead note 2026-10-29: '> 7 sigma' corrected to 6.6 sigma with both uncertainties (7.5 sigma with Beare's alone). |
| 115 | SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020 | validation.check_ids | text edit: → “["tests/scientific/test_batch9_documents.py::test_bakule2013_formation_fraction_vs_beare2020_combined_signifi…” | check_ids filled with the two pinning tests. |
| 116 | SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020 | provenance.applicability.explanation | text edit: → “Conflicts with the 0.52 used by Zhang, Aritome and μTRISTAN, which is the Bakule et al. 2013 MuSR value 0.52 …” | Lead note 2026-10-29: origin and corrected significance. |
| 117 | SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020 | provenance.applicability.explanation | text edit: → “Measured value of Beare et al. (PTEP 2020 123C01) from the µSR data of all aerogel targets combined (p.23: 'A…” | The template sentence attributed the value to laser-ablated silica targets; p.23 combines all aerogel targets (silica and PMSQ). |
| 118 | 88 Beare records (shared context sentence) | provenance.applicability.explanation | text edit: → “Measured value from Beare et al., 'Study of muonium emission from laser-ablated silica aerogel' (PTEP 2020 12…” | The shared sentence called every value one for laser-ablated silica targets, including the flat-target and PMSQ records; it now names the paper and defers to the target named in the record. |
| 119 | SOURCE_MUONIUM_FORMATION_FRACTION_BAKULE2013_BEARE2020 | provenance.applicability.explanation | text edit: → “Measured value from Beare et al., 'Study of muonium emission from laser-ablated silica aerogel' (PTEP 2020 12…” | Lead note 2026-10-29: point to the primary record now in the registry. |
| 120 | SOURCE_TRIUMF_M15_MOMENTUM_BEARE2020 | notes | text edit: → “p.15: the positron yield of the flat target peaks at around 22.5 MeV/c; the half-stop momentum is on the high…” | The note conflated the yield maximum with the half-stop momentum. |
| 121 | SOURCE_HALF_STOP_CONDITION_BEARE2020 | provenance.source.page | 15 → 15-16 | Quotation runs from p.15 onto p.16. |
| 122 | SOURCE_G2_MUONIUM_PEAK_TIME_BEARE2020 | provenance.source.page | 31 → 31-32 | Quotation runs from p.31 onto p.32. |
| 123 | SOURCE_G2_THERMAL_MUONIUM_PER_SURFACE_MUON_BEARE2020 | provenance.applicability.explanation | text edit: → “those are total vacuum yields per surface muon without the laser-region overlap. The H-line simulation breakd…” | The '6 x, not reconciled' statement compared quantities with different definitions; the Zhang p.9 breakdown reproduces 3.4e-3. |
| 124 | SOURCE_MU_EMISSION_RATE_SP_TRIUMF_BEARE2020 | uncertainty.value | 7.000000000000001e-05 → 7e-05 | Floating-point artefact of the per-mille conversion cleaned (no change of the printed value). |
| 125 | SOURCE_MU_EMISSION_RATE_S18_TRIUMF_BEARE2020 | value | 0.027600000000000003 → 0.0276 | Floating-point artefact of the per-mille conversion cleaned (no change of the printed value). |
| 126 | SOURCE_MU_EMISSION_RATE_S03_JPARC_BEARE2020 | value | 0.0058200000000000005 → 0.00582 | Floating-point artefact of the per-mille conversion cleaned (no change of the printed value). |
| 127 | SOURCE_MU_EMISSION_RATE_S03_JPARC_BEARE2020 | uncertainty.value | 0.0006500000000000001 → 0.00065 | Floating-point artefact of the per-mille conversion cleaned (no change of the printed value). |
| 128 | SOURCE_MU_EMISSION_RATE_S05_JPARC_BEARE2020 | value | 0.0040999999999999995 → 0.0041 | Floating-point artefact of the per-mille conversion cleaned (no change of the printed value). |
| 129 | SOURCE_PROTON_DRIVER_POWER_MUTRISTAN2022 | validation.level | P1 → P0 | P1 claimed a pin 'for the μLHC copy of the same chain in tests/scientific/test_analytical_checks.py'; no such check exists there (P1 requires a closed-form check under tests/scientific/). |
| 130 | SOURCE_PROTON_DRIVER_POWER_MUTRISTAN2022 | validation.methods | text edit: → “[]” | Follows the level change. |
| 131 | SOURCE_PROTON_DRIVER_POWER_MUTRISTAN2022 | validation.notes | text edit: → “Audit arithmetic (not pinned in a test): 3 GeV x 6.6 μC x 2 x 50 Hz = 1.98 MW, consistent with the stated 2 M…” | Audit arithmetic kept as a note. |
| 132 | SOURCE_PION_YIELD_PER_PROTON_MUTRISTAN2022 | name | text edit: → “Pions generated per proton per traversal of the 10 mm graphite target (150 mb at 3 GeV)” | 0.016 is per traversal, not 'over the 40 traversals'. |
| 133 | SOURCE_PION_YIELD_PER_PROTON_MUTRISTAN2022 | provenance.applicability.explanation | text edit: → “Per traversal: the paper turns it into '110 nC/bunch (times 40 turns times 2 bunches)', i.e. per bunch per tu…” | The text is not ambiguous once the 110 nC/bunch and 9.0e13 /s arithmetic is followed. |
| 134 | SOURCE_USM_PER_PROTON_MUTRISTAN2022 | name | text edit: → “Ultra-cold muons per proton per pass through the production target (one turn of the pion production ring)” | Follows the per-traversal reading of 0.016 (5.5e-4 x 2 x 6.6 μC = 7.2 nC per turn; x 40 turns x 50 Hz = 9.0e13 /s). |
| 135 | SOURCE_USM_BUNCH_CHARGE_MUTRISTAN2022 | name | text edit: → “Ultra-cold muon bunch charge per production-ring turn after combining the two proton bunches” | Made the per-turn meaning explicit. |
| 136 | SOURCE_RCS_REPETITION_RATE_MUTRISTAN2022 | provenance.source.page | 4 → 4, 6 | Quotation runs from p.4 onto p.6 (p.5 is the figure page). |
| 137 | SOURCE_AEROGEL_TARGET_LENGTH_MUTRISTAN2022 | provenance.source.page | 6 → 6-7 | Quotation runs from p.6 onto p.7. |
| 138 | SOURCE_MUONIUM_FORMATION_FRACTION_MUTRISTAN2022 | notes | text edit: → “Numbers provided by C. Zhang (footnote †, p.7); the 0.52 is the Bakule et al. 2013 MuSR value 0.52 ± 0.01 (SR…” | Lead note 2026-10-29: name the origin of the 0.52. |
| 139 | 40 categorical records: SOURCE_MUONIUM_DIFFUSION_MODEL_WS2026_ZHANG, SOURCE_IONISATION_TEST_DEMONSTRATION_WS2026_ZHAN… | unit | string → dimensionless | Task rule: categorical values are strings with unit 'dimensionless' ('string' is only an alias). |
| 140 | 15 P1 records: SOURCE_STOPPED_MUON_RATE_PRESENT_WS2026_ZHANG, SOURCE_MUONIUM_FORMATION_RATE_PRESENT_WS2026_ZHANG, SOU… | validation.check_ids | [] → test node ids named in validation.methods | check_ids were empty although every P1 method names its pinning test. |
| 141 | 109 records of parameters/source/hybrid_source_ws2026_rogers.yaml | provenance.confidence | high → medium | research/source_quality_policy.md §4 cap (status analogous), enforced by lhmuc validate since 2026-10-29; no other field changed. |
| 142 | 13 records of parameters/source/hybrid_source_ws2026_rogers.yaml | provenance.confidence | high → medium | research/source_quality_policy.md §4 cap (unrefereed slides), enforced by lhmuc validate since 2026-10-29; no other field changed. |
| 143 | 174 records of parameters/source/jparc_measurements_aritome2024_beare2020.yaml | provenance.confidence | high → medium | research/source_quality_policy.md §4 cap (status analogous), enforced by lhmuc validate since 2026-10-29; no other field changed. |
| 144 | 68 records of parameters/source/low_velocity_front_end_ws2026_nakazawa.yaml | provenance.confidence | high → medium | research/source_quality_policy.md §4 cap (status analogous), enforced by lhmuc validate since 2026-10-29; no other field changed. |
| 145 | 9 records of parameters/source/low_velocity_front_end_ws2026_nakazawa.yaml | provenance.confidence | high → medium | research/source_quality_policy.md §4 cap (unrefereed slides), enforced by lhmuc validate since 2026-10-29; no other field changed. |
| 146 | 10 records of parameters/source/muonium_diffusion_ws2026_zhang.yaml | provenance.confidence | high → medium | research/source_quality_policy.md §4 cap (imported_related from a design_variant), enforced by lhmuc validate since 2026-10-29; no other field changed. |
| 147 | 43 records of parameters/source/muonium_diffusion_ws2026_zhang.yaml | provenance.confidence | high → medium | research/source_quality_policy.md §4 cap (status analogous), enforced by lhmuc validate since 2026-10-29; no other field changed. |
| 148 | 4 records of parameters/source/muonium_diffusion_ws2026_zhang.yaml | provenance.confidence | high → medium | research/source_quality_policy.md §4 cap (unrefereed slides), enforced by lhmuc validate since 2026-10-29; no other field changed. |
| 149 | 38 records of parameters/source/mutristan2022_source_chain.yaml | provenance.confidence | high → medium | research/source_quality_policy.md §4 cap (imported_related from a design_variant), enforced by lhmuc validate since 2026-10-29; no other field changed. |
| 150 | 7 records of parameters/source/mutristan2022_source_chain.yaml | provenance.confidence | high → medium | research/source_quality_policy.md §4 cap (status analogous), enforced by lhmuc validate since 2026-10-29; no other field changed. |

## Appendix B — confidence lowered from high to medium (research/source_quality_policy.md §4)

475 records; only the `confidence` field changed. Grouped by file and by the cap that applied (`lhmuc.registry.confidence_cap`, which reports the first of several equal caps).

- `parameters/source/muonium_diffusion_ws2026_zhang.yaml` — status analogous (43): SOURCE_LASER_ABLATION_EMISSION_GAIN_WS2026_ZHANG, SOURCE_MUONIUM_DIFFUSION_MODEL_WS2026_ZHANG, SOURCE_MUONIUM_DIFFUSION_TEMPERATURE_FIT_WS2026_ZHANG, SOURCE_MUONIUM_DIFFUSION_CONSTANT_FIT_WS2026_ZHANG, SOURCE_MUONIUM_VACUUM_EMISSION_FRACTION_SINGLE_LAYER_WS2026_ZHANG, SOURCE_MUONIUM_DIFFUSION_LENGTH_WS2026_ZHANG, SOURCE_MUONIUM_LASER_REGION_PEAK_TIME_SINGLE_LAYER_WS2026_ZHANG, SOURCE_SURFACE_MUON_RATE_PRESENT_WS2026_ZHANG, SOURCE_SURFACE_MUON_RATE_G2_TARGET_WS2026_ZHANG, SOURCE_MUON_STOPPING_FRACTION_AEROGEL_WS2026_ZHANG, SOURCE_STOPPED_MUON_RATE_PRESENT_WS2026_ZHANG, SOURCE_STOPPED_MUON_RATE_G2_TARGET_WS2026_ZHANG, SOURCE_MUONIUM_FORMATION_FRACTION_TRIUMF_WS2026_ZHANG, SOURCE_MUONIUM_FORMATION_RATE_PRESENT_WS2026_ZHANG, SOURCE_MUONIUM_FORMATION_RATE_G2_TARGET_WS2026_ZHANG, SOURCE_MUONIUM_VACUUM_YIELD_DIFFUSION_MODEL_WS2026_ZHANG, SOURCE_MUONIUM_VACUUM_RATE_PRESENT_WS2026_ZHANG, SOURCE_MUONIUM_VACUUM_RATE_G2_TARGET_WS2026_ZHANG, SOURCE_LASER_IONISATION_EFF_244NM_WS2026_ZHANG, SOURCE_LASER_PULSE_ENERGY_244NM_WS2026_ZHANG, SOURCE_USM_RATE_PRESENT_244NM_WS2026_ZHANG, SOURCE_LASER_PULSE_ENERGY_122NM_G2_TARGET_WS2026_ZHANG, SOURCE_USM_RATE_G2_TARGET_122NM_WS2026_ZHANG, SOURCE_SLOW_MUON_BEAMLINE_EXTRACTION_EFF_WS2026_ZHANG, SOURCE_USM_RATE_AFTER_EXTRACTION_PRESENT_WS2026_ZHANG, SOURCE_MCP_DETECTION_EFF_WS2026_ZHANG, SOURCE_USM_RATE_AT_MCP_PRESENT_WS2026_ZHANG, SOURCE_IONISATION_TEST_DEMONSTRATION_WS2026_ZHANG, SOURCE_IONISATION_TEST_LASER_WAVELENGTH_WS2026_ZHANG, SOURCE_IONISATION_TEST_SIGNAL_RATE_JPARC2022_WS2026_ZHANG, SOURCE_IONISATION_TEST_SIGNAL_RATE_RAL1999_WS2026_ZHANG, SOURCE_IONISATION_TEST_LASER_LINEWIDTH_JPARC2022_WS2026_ZHANG, SOURCE_IONISATION_TEST_LASER_LINEWIDTH_RAL1999_WS2026_ZHANG, SOURCE_MULTILAYER_CONCEPT_WS2026_ZHANG, SOURCE_MUONIUM_THERMAL_VELOCITY_WS2026_ZHANG, SOURCE_MULTILAYER_LAYER_INTERVAL_SIMULATED_WS2026_ZHANG, SOURCE_MUONIUM_VACUUM_YIELD_MULTILAYER_WS2026_ZHANG, SOURCE_MULTILAYER_EXTRACTION_LIMITATION_WS2026_ZHANG, SOURCE_MULTILAYER_VERTICAL_VARIANT_YIELD_GAIN_4LAYERS_WS2026_ZHANG, SOURCE_MULTILAYER_VERTICAL_VARIANT_YIELD_GAIN_MAX_WS2026_ZHANG, SOURCE_TUNGSTEN_MUONIUM_TEMPERATURE_WS2026_ZHANG, SOURCE_TUNGSTEN_MUONIUM_DIFFUSION_CONSTANT_WS2026_ZHANG, SOURCE_TUNGSTEN_MUONIUM_EMISSION_DENSITY_RHO0_WS2026_ZHANG

- `parameters/source/muonium_diffusion_ws2026_zhang.yaml` — unrefereed slides (4): SOURCE_LASER_IONISATION_EFF_IMPLIED_G2_TARGET_WS2026_ZHANG, SOURCE_USM_PER_SURFACE_MUON_G2_TARGET_WS2026_ZHANG, SOURCE_USM_PER_SURFACE_MUON_PRESENT_244NM_WS2026_ZHANG, SOURCE_MUTRISTAN_POST_STOPPING_BUDGET_WS2026_ZHANG

- `parameters/source/muonium_diffusion_ws2026_zhang.yaml` — imported_related from a design_variant (10): SOURCE_MULTILAYER_VERTICAL_VARIANT_WS2026_ZHANG, SOURCE_MUTRISTAN_TOTAL_EFFICIENCY_QUOTED_WS2026_ZHANG, SOURCE_MUONIUM_VACUUM_YIELD_MULTILAYER_BUDGET_WS2026_ZHANG, SOURCE_MUONIUM_DECAY_SURVIVAL_BUDGET_WS2026_ZHANG, SOURCE_LASER_SHOOTING_TIME_BUDGET_WS2026_ZHANG, SOURCE_LASER_IONISATION_WAVELENGTHS_BUDGET_WS2026_ZHANG, SOURCE_MUTRISTAN_NEW_TARGET_MATERIAL_WS2026_ZHANG, SOURCE_MUTRISTAN_NEW_SLOW_MUON_ENERGY_RANGE_WS2026_ZHANG, SOURCE_MUTRISTAN_NEW_USM_RATE_PER_MW_WS2026_ZHANG, SOURCE_MULTILAYER_TARGET_EFFICIENCY_GAIN_MUTRISTAN_WS2026_ZHANG

- `parameters/source/hybrid_source_ws2026_rogers.yaml` — unrefereed slides (13): SOURCE_HYBRID_CONCEPT_WS2026_ROGERS, SOURCE_HYBRID_MOTIVATION_WS2026_ROGERS, SOURCE_HYBRID_AEROGEL_STOPPING_LENGTH_200MEV_WS2026_ROGERS, SOURCE_HYBRID_AEROGEL_DENSITY_RANGE_CALC_WS2026_ROGERS, SOURCE_HYBRID_LOW_ENERGY_COOLING_MOMENTUM_SPREAD_CONDITION_WS2026_ROGERS, SOURCE_HYBRID_COOLING_END_POINT_WS2026_ROGERS, SOURCE_HYBRID_DECELERATION_DESIGN_STATUS_WS2026_ROGERS, SOURCE_HYBRID_DECEL_TARGET_ENERGY_SPREAD_WS2026_ROGERS, SOURCE_HYBRID_DECEL_TARGET_BUNCH_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_MU_PER_PROTON_END_STAGE_A_WS2026_ROGERS, SOURCE_HYBRID_DECELERATION_EFFICIENCY_TARGET_WS2026_ROGERS, SOURCE_HYBRID_CHALLENGES_WS2026_ROGERS, SOURCE_HYBRID_DESIGN_STATUS_WS2026_ROGERS

- `parameters/source/hybrid_source_ws2026_rogers.yaml` — status analogous (109): SOURCE_HYBRID_TARGET_BEAM_POWER_MIN_WS2026_ROGERS, SOURCE_HYBRID_TARGET_BEAM_POWER_MAX_WS2026_ROGERS, SOURCE_HYBRID_TARGET_UNSPENT_PROTON_POWER_WS2026_ROGERS, SOURCE_HYBRID_TARGET_MATERIAL_WS2026_ROGERS, SOURCE_HYBRID_TARGET_STATION_CONCEPT_WS2026_ROGERS, SOURCE_HYBRID_FRONT_END_CONCEPT_WS2026_ROGERS, SOURCE_HYBRID_RECT_START_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_START_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_START_6D_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_6D_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_REFERENCE_MOMENTUM_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_6D_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_REFERENCE_MOMENTUM_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_6D_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_REFERENCE_MOMENTUM_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_6D_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_REFERENCE_MOMENTUM_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_CELL_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_STAGE_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_PIPE_RADIUS_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_MAX_ONAXIS_BZ_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_RF_FREQUENCY_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_RF_CELLS_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_RF_CELL_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_MAX_RF_GRADIENT_WS2026_ROGERS, SOURCE_HYBRID_RECT_A1_RF_PHASE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_CELL_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_STAGE_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_PIPE_RADIUS_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_MAX_ONAXIS_BZ_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_RF_FREQUENCY_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_RF_CELLS_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_RF_CELL_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_MAX_RF_GRADIENT_WS2026_ROGERS, SOURCE_HYBRID_RECT_A2_RF_PHASE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_CELL_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_STAGE_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_PIPE_RADIUS_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_MAX_ONAXIS_BZ_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_RF_FREQUENCY_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_RF_CELLS_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_RF_CELL_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_MAX_RF_GRADIENT_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3_RF_PHASE_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_CELL_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_STAGE_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_PIPE_RADIUS_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_MAX_ONAXIS_BZ_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_RF_FREQUENCY_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_RF_CELLS_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_RF_CELL_LENGTH_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_MAX_RF_GRADIENT_WS2026_ROGERS, SOURCE_HYBRID_RECT_A4_RF_PHASE_WS2026_ROGERS, SOURCE_HYBRID_STAGE_A4_LONGITUDINAL_EMITTANCE_NSMEV_WS2026_ROGERS, SOURCE_HYBRID_PERF_PROTON_DRIVER_PARTICLES_PER_BUNCH_WS2026_ROGERS, SOURCE_HYBRID_PERF_FRONT_END_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_FRONT_END_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_FRONT_END_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_FRONT_END_CUMULATIVE_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_FRONT_END_PARTICLES_PER_BUNCH_WS2026_ROGERS, SOURCE_HYBRID_PERF_CHARGE_SEP_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_CHARGE_SEP_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_CHARGE_SEP_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_CHARGE_SEP_CUMULATIVE_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_CHARGE_SEP_PARTICLES_PER_BUNCH_WS2026_ROGERS, SOURCE_HYBRID_PERF_RECT_A_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_RECT_A_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_RECT_A_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_RECT_A_CUMULATIVE_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_RECT_A_PARTICLES_PER_BUNCH_WS2026_ROGERS, SOURCE_HYBRID_PERF_BUNCH_MERGE_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_BUNCH_MERGE_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_BUNCH_MERGE_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_BUNCH_MERGE_CUMULATIVE_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_BUNCH_MERGE_PARTICLES_PER_BUNCH_WS2026_ROGERS, SOURCE_HYBRID_PERF_RECT_B_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_RECT_B_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_RECT_B_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_RECT_B_CUMULATIVE_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_RECT_B_PARTICLES_PER_BUNCH_WS2026_ROGERS, SOURCE_HYBRID_PERF_FINAL_COOLING_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_FINAL_COOLING_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_FINAL_COOLING_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_FINAL_COOLING_CUMULATIVE_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_FINAL_COOLING_PARTICLES_PER_BUNCH_WS2026_ROGERS, SOURCE_HYBRID_PERF_PRE_ACC_TRANSVERSE_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_PRE_ACC_LONGITUDINAL_EMITTANCE_WS2026_ROGERS, SOURCE_HYBRID_PERF_PRE_ACC_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_PRE_ACC_CUMULATIVE_TRANSMISSION_WS2026_ROGERS, SOURCE_HYBRID_PERF_PRE_ACC_PARTICLES_PER_BUNCH_WS2026_ROGERS, SOURCE_HYBRID_PROTON_DRIVER_ENERGY_WS2026_ROGERS, SOURCE_HYBRID_RF_BREAKDOWN_GRADIENT_CU_0T_WS2026_ROGERS, SOURCE_HYBRID_RF_BREAKDOWN_GRADIENT_CU_3T_WS2026_ROGERS, SOURCE_HYBRID_RF_BREAKDOWN_GRADIENT_BE_0T_WS2026_ROGERS, SOURCE_HYBRID_RF_BREAKDOWN_GRADIENT_BE_3T_WS2026_ROGERS, SOURCE_HYBRID_CAVITY_RND_STATUS_WS2026_ROGERS, SOURCE_HYBRID_ENGINEERING_STATUS_WS2026_ROGERS

- `parameters/source/low_velocity_front_end_ws2026_nakazawa.yaml` — status analogous (68): SOURCE_JPARC_MUON_LINAC_CHAIN_WS2026_NAKAZAWA, SOURCE_JPARC_DAW_CCL_FREQUENCY_WS2026_NAKAZAWA, SOURCE_JPARC_DLS_FREQUENCY_WS2026_NAKAZAWA, SOURCE_JPARC_LOW_VELOCITY_BETA_IN_WS2026_NAKAZAWA, SOURCE_JPARC_LOW_VELOCITY_BETA_RFQ_OUT_WS2026_NAKAZAWA, SOURCE_JPARC_LOW_VELOCITY_BETA_IHDTL_OUT_WS2026_NAKAZAWA, SOURCE_USM_PULSE_FWHM_WS2026_NAKAZAWA, SOURCE_USM_PULSE_PHASE_WIDTH_WS2026_NAKAZAWA, SOURCE_JPARC_RFQ_REUSE_WS2026_NAKAZAWA, SOURCE_RFQ_INJECTION_ENERGY_HMINUS_DESIGN_WS2026_NAKAZAWA, SOURCE_RFQ_INJECTION_ENERGY_MU_OPERATION_WS2026_NAKAZAWA, SOURCE_RFQ_EXTRACTION_ENERGY_HMINUS_DESIGN_WS2026_NAKAZAWA, SOURCE_RFQ_EXTRACTION_ENERGY_MU_OPERATION_WS2026_NAKAZAWA, SOURCE_RFQ_INTERVANE_VOLTAGE_HMINUS_DESIGN_WS2026_NAKAZAWA, SOURCE_RFQ_INTERVANE_VOLTAGE_MU_OPERATION_WS2026_NAKAZAWA, SOURCE_RFQ_RF_POWER_HMINUS_DESIGN_WS2026_NAKAZAWA, SOURCE_RFQ_RF_POWER_MU_OPERATION_WS2026_NAKAZAWA, SOURCE_RFQ_FREQUENCY_HMINUS_DESIGN_WS2026_NAKAZAWA, SOURCE_RFQ_FREQUENCY_MU_OPERATION_WS2026_NAKAZAWA, SOURCE_RFQ_LENGTH_HMINUS_DESIGN_WS2026_NAKAZAWA, SOURCE_RFQ_LENGTH_MU_OPERATION_WS2026_NAKAZAWA, SOURCE_RFQ_AVERAGE_BORE_RADIUS_HMINUS_DESIGN_WS2026_NAKAZAWA, SOURCE_RFQ_AVERAGE_BORE_RADIUS_MU_OPERATION_WS2026_NAKAZAWA, SOURCE_RFQ_BETA_RANGE_WS2026_NAKAZAWA, SOURCE_RFQ_PEAK_CURRENT_HMINUS_DESIGN_WS2026_NAKAZAWA, SOURCE_RFQ_VANE_GEOMETRY_REUSE_WS2026_NAKAZAWA, SOURCE_IHDTL_FREQUENCY_WS2026_NAKAZAWA, SOURCE_IHDTL_ACCELERATION_MODE_WS2026_NAKAZAWA, SOURCE_IHDTL_INPUT_ENERGY_WS2026_NAKAZAWA, SOURCE_IHDTL_OUTPUT_ENERGY_WS2026_NAKAZAWA, SOURCE_IHDTL_LENGTH_WS2026_NAKAZAWA, SOURCE_IHDTL_BORE_RADIUS_WS2026_NAKAZAWA, SOURCE_IHDTL_SYNCHRONOUS_PHASE_MIN_WS2026_NAKAZAWA, SOURCE_IHDTL_SYNCHRONOUS_PHASE_MAX_WS2026_NAKAZAWA, SOURCE_IHDTL_EFF_SHUNT_IMPEDANCE_WS2026_NAKAZAWA, SOURCE_IHDTL_MAX_SURFACE_FIELD_WS2026_NAKAZAWA, SOURCE_IHDTL_KILPATRICK_FACTOR_WS2026_NAKAZAWA, SOURCE_IHDTL_NOMINAL_POWER_WS2026_NAKAZAWA, SOURCE_IHDTL_MULTISTAGE_TEST_SCHEDULE_WS2026_NAKAZAWA, SOURCE_IHDTL_FIELD_ERROR_REQUIREMENT_WS2026_NAKAZAWA, SOURCE_IHDTL_EMITTANCE_GROWTH_LIMIT_WS2026_NAKAZAWA, SOURCE_IHDTL_FIELD_ERROR_ACHIEVED_WS2026_NAKAZAWA, SOURCE_JPARC_STEP1_ENERGY_2024_WS2026_NAKAZAWA, SOURCE_JPARC_STEP1_LASER_PULSE_LENGTH_WS2026_NAKAZAWA, SOURCE_JPARC_STEP2_ENERGY_2026_WS2026_NAKAZAWA, SOURCE_JPARC_STEP2_LASER_PULSE_LENGTH_WS2026_NAKAZAWA, SOURCE_JPARC_STEP3_PROGRAMME_WS2026_NAKAZAWA, SOURCE_EXPECTED_TOF_340KEV_WS2026_NAKAZAWA, SOURCE_JPARC_2026_SETUP_DETECTORS_WS2026_NAKAZAWA, SOURCE_BUNCH_WIDTH_RFQ_EXIT_SIM_WS2026_NAKAZAWA, SOURCE_BUNCH_WIDTH_AT_DETECTOR_SIM_WS2026_NAKAZAWA, SOURCE_JPARC_340KEV_BEAM_TEST_DATE_WS2026_NAKAZAWA, SOURCE_JPARC_340KEV_ACCELERATION_RESULT_WS2026_NAKAZAWA, SOURCE_USM_NORM_EMITTANCE_X_MEASURED_340KEV_WS2026_NAKAZAWA, SOURCE_USM_NORM_EMITTANCE_X_SIM_340KEV_WS2026_NAKAZAWA, SOURCE_USM_NORM_EMITTANCE_Y_MEASURED_340KEV_WS2026_NAKAZAWA, SOURCE_USM_NORM_EMITTANCE_Y_SIM_340KEV_WS2026_NAKAZAWA, SOURCE_BUNCH_MONITOR_TIME_RESOLUTION_WS2026_NAKAZAWA, SOURCE_RF_BUNCH_INTERVAL_324MHZ_WS2026_NAKAZAWA, SOURCE_BUNCH_WIDTH_MEASURED_AT_DETECTOR_WS2026_NAKAZAWA, SOURCE_BUNCH_WIDTH_SIGMA68_MEASURED_WS2026_NAKAZAWA, SOURCE_BUNCH_MAIN_FRACTION_MEASURED_WS2026_NAKAZAWA, SOURCE_BUNCH_WIDTH_SIGMA68_SIM_WS2026_NAKAZAWA, SOURCE_BUNCH_MAIN_FRACTION_SIM_WS2026_NAKAZAWA, SOURCE_JPARC_MUSE_TRIGGER_RATE_WS2026_NAKAZAWA, SOURCE_USM_PER_PULSE_PRESENT_WS2026_NAKAZAWA, SOURCE_USM_RATE_PRESENT_WS2026_NAKAZAWA, SOURCE_RFQ_PEAK_CURRENT_PRESENT_WS2026_NAKAZAWA

- `parameters/source/low_velocity_front_end_ws2026_nakazawa.yaml` — unrefereed slides (9): SOURCE_MU_PER_BUNCH_1E10_WS2026_NAKAZAWA, SOURCE_BUNCH_CHARGE_1E10_WS2026_NAKAZAWA, SOURCE_RFQ_INPUT_PULSE_FWHM_1E10_WS2026_NAKAZAWA, SOURCE_RFQ_PEAK_CURRENT_1E10_WS2026_NAKAZAWA, SOURCE_RFQ_SAME_PERVEANCE_MU_CURRENT_WS2026_NAKAZAWA, SOURCE_RFQ_PERVEANCE_RATIO_WS2026_NAKAZAWA, SOURCE_RFQ_EXIT_PEAK_CURRENT_1E10_WS2026_NAKAZAWA, SOURCE_RFQ_REDESIGN_OPTIONS_WS2026_NAKAZAWA, SOURCE_FRONT_END_SPACE_CHARGE_CONCLUSION_WS2026_NAKAZAWA

- `parameters/source/jparc_measurements_aritome2024_beare2020.yaml` — status analogous (174): SOURCE_SURFACE_MU_PER_PULSE_ARITOME2024, SOURCE_PROTON_BEAM_POWER_MLF_ARITOME2024, SOURCE_RCS_PROTON_ENERGY_ARITOME2024, SOURCE_RCS_REPETITION_RATE_ARITOME2024, SOURCE_SURFACE_MU_BEAM_SIZE_X_ARITOME2024, SOURCE_SURFACE_MU_BEAM_SIZE_Y_ARITOME2024, SOURCE_SURFACE_MU_MOMENTUM_MEAN_ARITOME2024, SOURCE_SURFACE_MU_MOMENTUM_RMS_ARITOME2024, SOURCE_SURFACE_MU_NORM_EMITTANCE_X_ARITOME2024, SOURCE_SURFACE_MU_NORM_EMITTANCE_Y_ARITOME2024, SOURCE_DEGRADER_AL_THICKNESS_ARITOME2024, SOURCE_AEROGEL_TARGET_DIAMETER_ARITOME2024, SOURCE_AEROGEL_TARGET_THICKNESS_ARITOME2024, SOURCE_AEROGEL_TARGET_DENSITY_ARITOME2024, SOURCE_ABLATION_HOLE_DIAMETER_ARITOME2024, SOURCE_ABLATION_HOLE_PITCH_ARITOME2024, SOURCE_AEROGEL_ABLATION_SIDES_ARITOME2024, SOURCE_MUON_STOPPING_EFF_ARITOME2024, SOURCE_MUONIUM_CONVERSION_EFF_ARITOME2024, SOURCE_MUONIUM_EMISSION_EFF_ARITOME2024, SOURCE_MESH_LOSS_FRACTION_ARITOME2024, SOURCE_LASER_WAVELENGTH_ARITOME2024, SOURCE_LASER_PULSE_ENERGY_MIN_ARITOME2024, SOURCE_LASER_PULSE_ENERGY_MAX_ARITOME2024, SOURCE_LASER_BEAM_DIAMETER_ARITOME2024, SOURCE_LASER_PULSE_DURATION_ARITOME2024, SOURCE_LASER_TARGET_DISTANCE_ARITOME2024, SOURCE_LASER_IONISATION_EFF_SIM_MIN_ARITOME2024, SOURCE_LASER_IONISATION_EFF_SIM_MAX_ARITOME2024, SOURCE_SOA_LENS_ENERGY_ARITOME2024, SOURCE_USM_NORM_EMITTANCE_X_5P7KEV_SIM_ARITOME2024, SOURCE_USM_NORM_EMITTANCE_Y_5P7KEV_SIM_ARITOME2024, SOURCE_USM_ENERGY_SPREAD_5P7KEV_SIM_ARITOME2024, SOURCE_TRANSPORT_DECAY_LOSS_ARITOME2024, SOURCE_USM_PER_PULSE_5P7KEV_ARITOME2024, SOURCE_LASER_TIMING_ARITOME2024, SOURCE_RFQ_DESIGN_HMINUS_ENERGY_ARITOME2024, SOURCE_RFQ_PRIOR_MUMINUS_ION_ENERGY_ARITOME2024, SOURCE_RFQ_TRANSVERSE_ACCEPTANCE_ARITOME2024, SOURCE_RFQ_ENERGY_ACCEPTANCE_ARITOME2024, SOURCE_RFQ_FREQUENCY_ARITOME2024, SOURCE_RFQ_PEAK_POWER_ARITOME2024, SOURCE_RFQ_PULSE_WIDTH_ARITOME2024, SOURCE_RFQ_DECAY_LOSS_ARITOME2024, SOURCE_RFQ_TRANSMITTANCE_EXCL_DECAY_ARITOME2024, SOURCE_DIAG_QM_GRADIENT_PER_AMPERE_ARITOME2024, SOURCE_DIAG_LINE_DECAY_LOSS_ARITOME2024, SOURCE_MCP_EFFECTIVE_DIAMETER_ARITOME2024, SOURCE_MCP_APERTURE_RATIO_ARITOME2024, SOURCE_MCP_DIGITIZER_RATE_ARITOME2024, SOURCE_BPM_EFFECTIVE_DIAMETER_ARITOME2024, SOURCE_BPM_EXPOSURE_TIME_ARITOME2024, SOURCE_TOF_ACCELERATED_PEAK_ARITOME2024, SOURCE_TOF_PENETRATING_PEAK_ARITOME2024, SOURCE_TOF_LASER_TO_MCP_MEASURED_ARITOME2024, SOURCE_TOF_LASER_TO_MCP_SIM_ARITOME2024, SOURCE_USM_PER_PULSE_100KEV_ARITOME2024, SOURCE_ACCELERATION_EFFICIENCY_ARITOME2024, SOURCE_LASER_ENERGY_DEFICIT_100KEV_MIN_ARITOME2024, SOURCE_LASER_ENERGY_DEFICIT_100KEV_MAX_ARITOME2024, SOURCE_BEAM_SIZE_Y_EXAMPLE_ARITOME2024, SOURCE_MOMENTUM_SPREAD_100KEV_ARITOME2024, SOURCE_USM_NORM_EMITTANCE_X_MEASURED_ARITOME2024, SOURCE_USM_NORM_EMITTANCE_Y_MEASURED_ARITOME2024, SOURCE_USM_NORM_EMITTANCE_X_SIM_ARITOME2024, SOURCE_USM_NORM_EMITTANCE_Y_SIM_ARITOME2024, SOURCE_PHASE_SPACE_REDUCTION_X_ARITOME2024, SOURCE_PHASE_SPACE_REDUCTION_Y_ARITOME2024, SOURCE_EMITTANCE_SYST_X_RMS_BEAM_SIZE_ARITOME2024, SOURCE_EMITTANCE_SYST_X_MOMENTUM_SPREAD_ARITOME2024, SOURCE_EMITTANCE_SYST_X_BEAM_LOSS_ARITOME2024, SOURCE_EMITTANCE_SYST_X_TOTAL_ARITOME2024, SOURCE_EMITTANCE_SYST_Y_RMS_BEAM_SIZE_ARITOME2024, SOURCE_EMITTANCE_SYST_Y_BEAM_LOSS_ARITOME2024, SOURCE_EMITTANCE_SYST_Y_TOTAL_ARITOME2024, SOURCE_LASER_IONISATION_EFF_PROJECTED_122_355NM_ARITOME2024, SOURCE_HLINE_SURFACE_MU_GAIN_ARITOME2024, SOURCE_TOTAL_RATE_GAIN_EXPECTED_MIN_ARITOME2024, SOURCE_TOTAL_RATE_GAIN_EXPECTED_MAX_ARITOME2024, SOURCE_COOLING_EFFICIENCY_ACHIEVABLE_ARITOME2024, SOURCE_USM_NORM_EMITTANCE_POSSIBLE_ARITOME2024, SOURCE_USM_THERMAL_ENERGY_ARITOME2024, SOURCE_USM_PULSE_DURATION_ORDER_ARITOME2024, SOURCE_USM_ENERGY_SPREAD_ORDER_ARITOME2024, SOURCE_EXPERIMENT_PERIOD_ARITOME2024, SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020, SOURCE_MUONIUM_FORMATION_FRACTION_BAKULE2013_BEARE2020, SOURCE_MUONIUM_ASYMMETRY_BEARE2020, SOURCE_MAX_ASYMMETRY_A0_BEARE2020, SOURCE_MU_EMISSION_RATE_ABLATED_MIN_BEARE2020, SOURCE_MU_EMISSION_RATE_ABLATED_MAX_BEARE2020, SOURCE_MU_EMISSION_RATE_FLAT_MAX_BEARE2020, SOURCE_MU_EMISSION_RATE_SP_TRIUMF_BEARE2020, SOURCE_MU_EMISSION_RATE_S08_TRIUMF_BEARE2020, SOURCE_MU_EMISSION_RATE_S01_TRIUMF_BEARE2020, SOURCE_MU_EMISSION_RATE_S18_TRIUMF_BEARE2020, SOURCE_MU_EMISSION_RATE_S19_TRIUMF_BEARE2020, SOURCE_MU_EMISSION_RATE_S21H_TRIUMF_BEARE2020, SOURCE_MU_EMISSION_RATE_S22V_TRIUMF_BEARE2020, SOURCE_MU_EMISSION_RATE_S14_TRIUMF_BEARE2020, SOURCE_MU_EMISSION_RATE_O2013_4_TRIUMF_BEARE2020, SOURCE_TARGET_S08_THICKNESS_BEARE2020, SOURCE_TARGET_S08_DENSITY_BEARE2020, SOURCE_TARGET_S01_THICKNESS_BEARE2020, SOURCE_TARGET_S01_DENSITY_BEARE2020, SOURCE_TARGET_S01_HOLE_DIAMETER_BEARE2020, SOURCE_TARGET_S01_HOLE_PITCH_BEARE2020, SOURCE_TARGET_S01_HOLE_DEPTH_BEARE2020, SOURCE_TARGET_S18_THICKNESS_BEARE2020, SOURCE_TARGET_S18_DENSITY_BEARE2020, SOURCE_TARGET_S18_HOLE_DIAMETER_BEARE2020, SOURCE_TARGET_S18_HOLE_PITCH_BEARE2020, SOURCE_TARGET_S18_HOLE_DEPTH_BEARE2020, SOURCE_TARGET_S19_THICKNESS_BEARE2020, SOURCE_TARGET_S19_DENSITY_BEARE2020, SOURCE_TARGET_S19_HOLE_DIAMETER_BEARE2020, SOURCE_TARGET_S19_HOLE_PITCH_BEARE2020, SOURCE_TARGET_S19_HOLE_DEPTH_BEARE2020, SOURCE_TARGET_SLAB_SIZE_BEARE2020, SOURCE_TARGET_ABLATED_AREA_BEARE2020, SOURCE_BEAM_COLLIMATED_DIAMETER_BEARE2020, SOURCE_AEROGEL_DENSITY_MIN_BEARE2020, SOURCE_AEROGEL_DENSITY_MAX_BEARE2020, SOURCE_AEROGEL_THICKNESS_MIN_BEARE2020, SOURCE_AEROGEL_THICKNESS_MAX_BEARE2020, SOURCE_PMSQ_LOW_DENSITY_BEARE2020, SOURCE_PMSQ_HIGH_DENSITY_BEARE2020, SOURCE_MUONIUM_DIFFUSION_LENGTH_PAST_MODEL_BEARE2020, SOURCE_MUON_RANGE_STRAGGLING_BEARE2020, SOURCE_ABLATION_GAIN_PREVIOUS_STUDY_BEARE2020, SOURCE_ABLATION_LASER_WAVELENGTH_BEARE2020, SOURCE_ABLATION_LASER_PULSE_DURATION_BEARE2020, SOURCE_ABLATION_THRESHOLD_FLUENCE_BEARE2020, SOURCE_ABLATION_WEIGHT_LOSS_PER_HOLE_BEARE2020, SOURCE_TRIUMF_M15_MUON_RATE_BEARE2020, SOURCE_TRIUMF_M15_MOMENTUM_BEARE2020, SOURCE_TRIUMF_M15_MOMENTUM_SPREAD_BEARE2020, SOURCE_TRIUMF_M15_MOMENTUM_SPREAD_FIT_BEARE2020, SOURCE_HALF_STOP_CONDITION_BEARE2020, SOURCE_MU_EMISSION_SYST_LOW_BEARE2020, SOURCE_MU_EMISSION_SYST_HIGH_BEARE2020, SOURCE_ABLATION_OPTIMAL_DEPTH_BOUND_BEARE2020, SOURCE_MU_EMISSION_STABILITY_DURATION_BEARE2020, SOURCE_TARGET_CHAMBER_VACUUM_MIN_BEARE2020, SOURCE_TARGET_CHAMBER_VACUUM_MAX_BEARE2020, SOURCE_JPARC_D2_REPETITION_RATE_BEARE2020, SOURCE_JPARC_D2_BUNCH_SEPARATION_BEARE2020, SOURCE_JPARC_D2_BUNCH_WIDTH_BEARE2020, SOURCE_JPARC_D2_MOMENTUM_BEARE2020, SOURCE_JPARC_D2_MOMENTUM_SPREAD_BEARE2020, SOURCE_JPARC_D2_BACKGROUND_RATE_BEARE2020, SOURCE_MU_EMISSION_RATE_S08_JPARC_BEARE2020, SOURCE_MU_EMISSION_RATE_S01_JPARC_BEARE2020, SOURCE_MU_EMISSION_RATE_S03_JPARC_BEARE2020, SOURCE_MU_EMISSION_RATE_S04_JPARC_BEARE2020, SOURCE_MU_EMISSION_RATE_S05_JPARC_BEARE2020, SOURCE_JPARC_EMISSION_SYST_LOW_BEARE2020, SOURCE_JPARC_EMISSION_SYST_HIGH_BEARE2020, SOURCE_PROJECTION_MOMENTUM_SPREAD_RATIO_BEARE2020, SOURCE_PROJECTION_VACUUM_REGION_FACTOR_BEARE2020, SOURCE_PROJECTION_RESOLUTION_FACTOR_BEARE2020, SOURCE_PROJECTION_ACCURACY_BEARE2020, SOURCE_HLINE_MOMENTUM_SPREAD_EXPECTED_BEARE2020, SOURCE_G2_LASER_REGION_HALF_WIDTH_X_BEARE2020, SOURCE_G2_LASER_REGION_HALF_WIDTH_Y_BEARE2020, SOURCE_G2_LASER_REGION_DEPTH_BEARE2020, SOURCE_G2_MUONIUM_PEAK_TIME_BEARE2020, SOURCE_G2_THERMAL_MUONIUM_PER_SURFACE_MUON_BEARE2020, SOURCE_G2_USM_THERMAL_ENERGY_BEARE2020, SOURCE_G2_REACCELERATION_ENERGY_BEARE2020, SOURCE_G2_MOMENTUM_SPREAD_BEARE2020, SOURCE_G2_TRANSVERSE_EMITTANCE_BEARE2020, SOURCE_SURFACE_MUON_ENERGY_BEARE2020, SOURCE_HOT_TUNGSTEN_MUONIUM_ENERGY_BEARE2020

- `parameters/source/mutristan2022_source_chain.yaml` — imported_related from a design_variant (38): SOURCE_PROTON_DRIVER_POWER_MUTRISTAN2022, SOURCE_RCS_PROTON_ENERGY_MUTRISTAN2022, SOURCE_RCS_BUNCH_CHARGE_MUTRISTAN2022, SOURCE_RCS_BUNCH_POPULATION_MUTRISTAN2022, SOURCE_RCS_BUNCHES_MUTRISTAN2022, SOURCE_RCS_REPETITION_RATE_MUTRISTAN2022, SOURCE_PION_TARGET_MATERIAL_MUTRISTAN2022, SOURCE_PION_TARGET_THICKNESS_MUTRISTAN2022, SOURCE_PROTON_TARGET_HITS_MUTRISTAN2022, SOURCE_PROTON_ENERGY_LOSS_PER_HIT_MUTRISTAN2022, SOURCE_PROTON_ENERGY_LOSS_FRACTION_PER_HIT_MUTRISTAN2022, SOURCE_PION_RING_RF_POWER_MUTRISTAN2022, SOURCE_PION_PRODUCTION_XSEC_MUTRISTAN2022, SOURCE_PION_YIELD_PER_PROTON_MUTRISTAN2022, SOURCE_PION_CHARGE_PER_BUNCH_MUTRISTAN2022, SOURCE_PION_TRANSPORT_EFFICIENCY_MUTRISTAN2022, SOURCE_STOPPING_TARGET_MATERIAL_MUTRISTAN2022, SOURCE_STOPPING_TARGET_FOIL_THICKNESS_MUTRISTAN2022, SOURCE_STOPPING_TARGET_FOIL_INTERVAL_MUTRISTAN2022, SOURCE_STOPPING_TARGET_LAYERS_MUTRISTAN2022, SOURCE_STOPPING_TARGET_LENGTH_MUTRISTAN2022, SOURCE_AEROGEL_TARGET_LENGTH_MUTRISTAN2022, SOURCE_IONISATION_LASER_MUTRISTAN2022, SOURCE_USM_PRODUCTION_EFFICIENCY_FIRST_TARGET_MUTRISTAN2022, SOURCE_MUONIUM_FORMATION_FRACTION_MUTRISTAN2022, SOURCE_MUONIUM_VACUUM_YIELD_MUTRISTAN2022, SOURCE_MUONIUM_DECAY_SURVIVAL_MUTRISTAN2022, SOURCE_SECOND_TARGET_SIZE_MUTRISTAN2022, SOURCE_USM_EFFICIENCY_FROM_STOPPED_PIONS_MUTRISTAN2022, SOURCE_USM_PER_PROTON_MUTRISTAN2022, SOURCE_USM_BUNCH_CHARGE_MUTRISTAN2022, SOURCE_USM_RATE_MUTRISTAN2022, SOURCE_USM_RATE_ESTIMATE_MIN_MUTRISTAN2022, SOURCE_USM_RATE_ESTIMATE_MAX_MUTRISTAN2022, SOURCE_USM_RATE_ENHANCEMENT_VS_JPARC_MUTRISTAN2022, SOURCE_MUON_POLARISATION_WORST_CASE_MUTRISTAN2022, SOURCE_MUON_POLARISATION_PER_MUONIUM_FORMATION_MUTRISTAN2022, SOURCE_POLARISATION_LONGITUDINAL_FIELD_MUTRISTAN2022

- `parameters/source/mutristan2022_source_chain.yaml` — status analogous (7): SOURCE_JPARC_MLF_STOPPED_PIONS_PER_PROTON_MUTRISTAN2022, SOURCE_JPARC_MLF_SURFACE_MUONS_PER_PROTON_MUTRISTAN2022, SOURCE_JPARC_MLF_CAPTURE_SOLID_ANGLE_MUTRISTAN2022, SOURCE_JPARC_MLF_CAPTURED_MUONS_PER_PROTON_MUTRISTAN2022, SOURCE_JPARC_MLF_TRANSPORT_FRACTION_MUTRISTAN2022, SOURCE_JPARC_MLF_MUONS_PER_PROTON_MUTRISTAN2022, SOURCE_G2_POLARISATION_TARGET_MUTRISTAN2022
