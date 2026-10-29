# Verification note — group G3_ACCELERATION (Phase 0 addendum, 2026-10-29)

Role: adversarial verifier. Files verified (all written by the G3_ACCELERATION extraction of 2026-10-28):

| File | Source | Records before → after |
|---|---|---|
| `parameters/acceleration/vffa_ws2026_topp_mugglestone.yaml` | SRC_WS1681458_TOPPMUGGLESTONE_VFFA (52 slides) | 138 → 144 (+6 added) |
| `parameters/acceleration/mucol_mr7_acceleration_chain.yaml` | SRC_ARXIV_2510_27437 (MuCol MR7, PDF pp. 17-19, 58-64) | 586 → 586 |
| `parameters/acceleration/mutristan2022_booster_ring.yaml` | SRC_ARXIV_2201_06664 (μTRISTAN, PDF pp. 4-13) | 60 → 60 |
| `parameters/acceleration/imcc_ws2026_schulte_acceleration.yaml` | SRC_WS1681458_SCHULTE_IMCC (slides 8, 9, 17, 20, 21, 41-43) | 59 → 67 (+9 added, 1 removed) |

Total 843 → 857. No scenario file belongs to this group (all records keep `scenario: null`).

## Method

- **Tables, cell by cell.** MR7 Tables 5.1, 5.2, E.1, E.2, F.1, F.2, F.3, F.4, F.5 and the MuCol table on Topp-Mugglestone (TM)
  slide 9 were re-transcribed independently from 200-dpi page renders (pdftoppm; 400-800 dpi crops where needed) into a script
  (`verify_g3/mr7_tables.py`, `cmp_tm9.py` in the verifier scratchpad). Every record's row, unit column, column header, cell text
  and stored value were compared programmatically: 467 MR7 cells + 64 TM cells, all present, no value error; 26 cell
  transcriptions corrected (25 MR7 incl. the four 'No.S̃RF' labels, 1 TM; below). Cells printed '-' correctly have no record.
- **Text and figure quotations.** Every free-text quotation was located on the cited page in two text layers (pdftotext layout
  and raw order) with a normalising matcher; the 72 quotations that cannot be matched automatically (raster figure labels on the
  Schulte and TM slides, μTRISTAN Figure 1 whose μ glyph maps to 'm', equations, multi-column slide layouts, page-spanning
  sentences) were each checked by eye on the page image.
- **Arithmetic.** Every P1 method and every derivation was recomputed (`verify_g3/p1_mr7.py`, `audit_numbers.py`, the fix
  scripts). Physical constants from `lhmuc/analytical.py` (m_μ = 0.1056583755 GeV, τ_μ = 2.1969811 µs).
- **Status rules.** reported_lhmuc only for LHμC statements on the PRIMARY_LHMUC TM deck; the MuCol table on TM slide 9, IMCC
  (MR7, Schulte) and prior-art FFA statements analogous; μTRISTAN imported_related; computed values derived_lhmuc /
  analytical_estimate with every input id named.
- **P1 rule applied consistently** (the addendum brief: "P0 unless an arithmetic reproduction exists"): P1 kept only where a
  closed-form computation from *other* quantities reproduces or bounds the value with a stated tolerance. Checks that only found
  the same number printed elsewhere (text vs table of the same report, the same design value in another document of the same
  study, a rounded restatement on the same slide, a design-pattern observation such as "264 = 3 × 88") were moved to
  `validation.notes` and the level set to P0. This follows the G8 precedent ("internal consistency is not an arithmetic
  reproduction").
- Edits were applied by script to the parsed records and re-emitted with the extractor's own emitter (round trip verified
  byte-identical before editing), so formatting is unchanged. Scripts: `/tmp/claude-0/-home-user-digital-twin-LH-C/0f2c7853-3fdb-534d-84ae-c6857c596b01/scratchpad/verify_g3/fix_{mr7,tm,mut,sch}.py`
  (they reload the pre-verification backups in `verify_g3/backup/`, so they are re-runnable); per-record change logs `verify_g3/log_*.json`.

## Checked and found correct

- **All 586 MR7 values and units** (after the unit conventions of the file header: ps → ns, 10^12 → plain number, 10^-4 / 10^-6
  → plain dimensionless); table captions, PDF pages and printed pages; the 43 free-text statements of §5.1/5.2 and Appendices
  E/F (p. 17-18, 58-64) including the cross-page continuation p.17→18 (already flagged by the extractor).
- **All 64 slide-9 cells** of the TM deck; all 74 other TM records (slides 3-52) against the slide images; the six energy-ratio
  and scaling-law derivations (500/70 = 7.14, 1000/70 = 14.29, ln(500/70)/m = 4.92/3.28/6.55/4.47 cm for m = 40/60/30/44 /m).
- **μTRISTAN**: Figure 1 labels (250 dpi), §2.3-2.7, §4; the extractor's arithmetic for 12.28 km, 40.97 µs, 655 µs, (1 - 1/e) ×
  3.6 nC = 2.28 nC, 1.44e10, 6.24e10, L(μ+e−) = 4.51e33, L(μ+μ+) = 5.68e32, γτ = 20.8 ms, 1999 turns, 6.99 T bound.
- **Schulte**: slide-42 table (all 18 cells), slide-17 ring schematic labels (800 dpi), challenge/conclusion lists, slides 8, 9, 20,
  21, 41, 43. Slide-8 and slide-21 tables are recorded by the machine group (imcc_ws2026_schulte_parameters.yaml), not duplicated.
- **Canonical ids present with the stated values**: ACC_VFFA_PEAK_DIPOLE_FIELD_8T_WS2026_TOPPMUGGLESTONE 8 T (index
  ACC_VFFA_FIELD_INDEX_8T_OPTION 60 /m), ACC_VFFA_PEAK_DIPOLE_FIELD_10T_WS2026_TOPPMUGGLESTONE 10 T (index ~44 /m),
  ACC_VFFA_PEAK_FIELD_RELAXED_MAX 9 T, ACC_VFFA_FIELD_INDEX_MIN_5CM 40 /m, ACC_VFFA_EXCURSION_8T 3 cm,
  ACC_VFFA_EXCURSION_RELAXED_MAX 7 cm, ACC_BOOSTER_INJECTION_ENERGY 70 GeV, ACC_BOOSTER_EXTRACTION_ENERGY 500 GeV (all
  _WS2026_TOPPMUGGLESTONE), ACC_VFFA1_PEAK_FIELD_ON_ORBIT_MR7 6.93 T, ACC_VFFA1_ORBIT_RADIUS_MR7 953 m,
  ACC_VFFA1_FIELD_INDEX_MR7 31.94 /m. No id was renamed; ids referenced by other files (M17 vFFA file, scenarios_addendum_imcc,
  mutristan2022_physics, Forthomme beam set, Giove file) all still exist.

## Corrections — value / unit errors (most severe first)

1. **MACHINE_MU_GEOMETRIC_EMITTANCE_1TEV_MUTRISTAN2022: 0.42 mm mrad → 420 nm mrad** (unit as printed). The paper prints
   "ϵ = 420 nm mrad" = 4.2e-10 m rad = 4.2e-4 mm mrad; the stored 0.42 mm mrad was **1000 × too large** and its note
   ("0.42 mm mrad (= 420 nm mrad)") was wrong. Method fixed: 4 mm mrad / 9464 = 422.6 nm mrad (the old method wrote
   "0.423 nm mrad").
2. **MACHINE_MU_SIGMA_X_IP / _SIGMA_Y_IP_MUTRISTAN2022**: the P1 methods computed 112 µm and 54.2 µm from the wrong
   emittance and were nevertheless labelled P1 against the printed 3.6 / 1.7 µm. Recomputed: √(4.2e-10 m × 30 mm) = 3.55 µm,
   √(4.2e-10 m × 7 mm) = 1.71 µm (P1 now genuine).

## Corrections — quotations (verbatim / exact cell transcription)

3. MR7 cell texts with dropped trailing zeros: ACC_RCS2_ACCELERATION_TIME ('1.10'), ACC_RCS4_HORIZONTAL_TUNE ('82.40'),
   ACC_FNAL_RCS1-4_AVERAGE_GRADIENT ('2.50', '2.00', '2.00', '1.00'), ACC_FNAL_RCS1_INJ_BUNCH_POPULATION ('2.70', note too),
   ACC_FNAL_RCS1-4_RF_FREQUENCY ('1.30'), ACC_VFFA1_F/D_MAGNET_HALF_OPENING_ANGLE ('0.0015640', '0.0011800'),
   ACC_VFFA4_F/D_MAGNET_HALF_OPENING_ANGLE ('0.0019700', '0.0011660'), ACC_VFFA4_TUNE_1/_2 ('(0.460, 0.057)', notes too)
   — all _MR7.
4. MR7 ACC_RCS1-4_TURNS_MR7: the unit column of Table 5.1 'Number of turns' is printed '-', not empty.
5. MR7 ACC_RLA1/RLA2_SRF_CAVITIES_352MHZ/_1056MHZ_MR7: row label printed 'No.S̃RF cavities' (typesetting artefact), quoted as
   printed; the pairing with 352/1056 MHz follows the printed sub-column alignment (now stated in notes).
6. TM ACC_RCS2_ACCELERATION_TIME_WS2026_TOPPMUGGLESTONE: '1.10' as printed.
7. TM ACC_SEPARATED_ARC_RLA_ASSESSMENT, ACC_VFFA_DISPERSION_SUPPRESSOR_RULE: bullets '•' inserted by the extractor do not exist
   on slides 11/42; separate lines now joined with ' | ' (and 'However:' kept). ACC_EMMA_RESONANCE_CROSSING: spurious full stop
   removed.
8. μTRISTAN: lunate 'ϵ' as printed in the five §2.4 emittance/beta/σ records; MACHINE_LUMINOSITY_FORMULA_MUTRISTAN2022 equation
   transcribed in the printed order "Nbeam1 Nbeam2/(4πσx σy) frep".
9. Schulte slide-17 ring labels (12 records ACC_RCS1-4_TURNS/_INJECTION_ENERGY/_EXTRACTION_ENERGY): separate labels joined by
   ' | '; RCS 2 label printed with a hyphen '313 - 750 GeV' (en dash only for RCS 1; checked at 800 dpi).
   ACC_RCS_FIGURE_LEGEND: 'RF station and Impedance' (capital I, symbols not bullets).
10. Schulte figure-label records: descriptive text removed from the quotation and moved to `table_figure_or_equation`
    (ACC_RCS_PULSED_DIPOLE_HM_HEIGHT/_HM_WIDTH/_YOKE_WIDTH/_YOKE_HEIGHT/_YOKE_STEEL/_GEOMETRY_OPTIONS).
11. **ACC_RCS_PULSED_DIPOLE_HM_HEIGHT_WS2026_SCHULTE: page 42 → 17** — on slide 42 the '0.38 m' label is hidden behind the red
    circle; it is legible on slide 17 (same figure).

## Corrections — names, notes, interpretation

12. ACC_RCS_PULSED_DIPOLE_GEOMETRY_OPTIONS: value said "WF1, WF1M, HM, WF3 (window-frame variants)" — HM is not a window-frame
    in the caption; note quoted "Hourglass, J = 10 A/mm2" although that J is cut off in the image. Both corrected.
13. ACC_RCS_PULSED_DIPOLE_YOKE_WIDTH/_HEIGHT: "half-model" removed from the names (symmetry not stated); note adds that the slide
    does not say whether the field map is the HG or the HM option.
14. ACC_RCS_DESIGN_STATUS_WS2026_SCHULTE: value restricted to what the quoted slide-41 text says.
15. MR7 ACC_RCS4_SC_AVERAGE_FIELD_MR7: name said "in the SC magnets"; the text says "the average magnetic field in the
    accelerator". The Table 5.1 field integral gives 4.25 T averaged over the dipoles (2.99 T over C), so the 16 T can only be
    the steady SC dipole field; name/notes rewritten, cross-page (pp. 59-60) flagged, P1 → P0 (it compared two differently
    defined quantities).
16. MR7 ACC_LOW_ENERGY_CHAIN_INJECTION_ENERGY_MR7: name asserted "kinetic" while its note said the type is not stated.
    Resolved: Table 4.1 (p.17) gives mean pz = 339 MeV/c at the end of reacceleration = 249 MeV kinetic; name and note now say
    "kinetic by consistency, not stated in the sentence".
17. MR7 ACC_LINAC_RLA1_TARGET_TRANSMISSION_MR7: name said "(each)", which the text does not say; the 4.1 MV/m equivalence is
    reproduced only for LINAC + RLA1 together (item 23).
18. MR7 RLA notes: ACC_RLA1/RLA2_ENERGY_GAIN_PER_PASS and ACC_RLA2_LINAC_LENGTH asserted that the RF length is "per linac" (not
    stated); ACC_RLA1_PASSES assumed two linacs for RLA1 (Table E.2 gives no RLA1 linac length). Qualified.
19. μTRISTAN ACC_BOOSTER_DECAY_LOSS_FRACTION: the extractor's audit ("~90 % survival") started the ramp at 60 GeV and omitted the
    first turn. Redone: 32 linac passes of 30 GeV with π × 1 km arcs from 212 MeV give **82.2 %**, reproducing the μLHC
    paper's 82 % (ACC_BOOSTER_SURVIVAL_MUTRISTAN_MULHC); a linear-in-time ramp over 16 × 40.97 µs gives 77 %. All far above
    "about a half".
20. Cross-page quotations flagged in `section`: MACHINE_MU_LIFETIME_LAB_1TEV (starts p.4), MACHINE_MAIN_RING_DIPOLE_FIELD,
    MACHINE_HL_LHC_DIPOLE_FIELD_REFERENCE, MACHINE_MAIN_RING_MAGNET_TECHNOLOGY (end on p.11) — μTRISTAN.
21. TM: derivations of ACC_VFFA_EXCURSION_IMPLIED_M40/M60/M30/M44 did not name the field-index input ids (now
    ACC_VFFA_FIELD_INDEX_MIN_5CM / _8T_OPTION / _RELAXED_MAX / _10T_OPTION, also added to `dependencies`);
    ACC_VFFA_EXCURSION_MAX_ASSUMED (an assumption) no longer "depends" on the gradient it implies, ACC_VFFA_FIELD_INDEX_MIN_5CM now
    lists it; ACC_VFFA_FIELD_INDEX_8T_OPTION notes that "field gradient of 60" is printed without unit;
    ACC_BOOSTER_CYCLE_TIME_UPPER_BOUND uncertainty → order_of_magnitude ("sub-millisecond order") with survival context (linear
    70→500 GeV ramp: 90 % at 0.48 ms, 80 % at 1 ms). Twelve slide-35-37 records note that these slides carry the footer and
    text-layer date of the speaker's 13/05/2025 "Update on vFFA" talk (slides 23-30, 32, 35-37, 39-43, 52 are reused material).
22. μTRISTAN: ACC_BOOSTER_INJECTION_ENERGY (unknown, null) confidence high → none (repository convention); analytical estimates
    ACC_BOOSTER_CIRCUMFERENCE / _REVOLUTION_PERIOD / _ENERGY_GAIN_PER_TURN / _TOTAL_ENERGY_GAIN and the six TM derived records
    high → medium (computed, not read); circumference note states the semicircular-arc assumption;
    MACHINE_PEAK_LUMINOSITY_MUMU dependencies gain σx, σy; MACHINE_MUMU_DECAY_REDUCTION_FACTOR notes that 0.4323 evaluates the
    printed expression; tolerances stated in ACC_BOOSTER_TOP_ENERGY / _TURNS; MACHINE_MAIN_RING_DIPOLE_FIELD method reworded as
    the bound it checks (≥ 6.99 T; fill factor 0.70).

## Validation-level changes

23. **New P1 (closed-form reproductions found by the verifier)**, 31 records (23 MR7 and 4 Schulte re-levelled, 4 added):
    - straight-section length = C − total arc length, exact: ACC_RCS1-4_STRAIGHT_SECTION_LENGTH_MR7,
      ACC_CERN_RCS_SPS/LHC1/LHC2_STRAIGHT_SECTION_LENGTH_MR7 (this also proves that the Table F.2 columns RCS1/2/3 are the
      Table F.1 rings SPS/LHC1/LHC2);
    - closed-orbit field integral ΣL·B = 2πBρ at injection (pulsed −1.8 T) and extraction (+1.8 T): ACC_RCS1-4_PULSED_DIPOLE_LENGTH_MR7,
      ACC_RCS2-4_STEADY_DIPOLE_LENGTH_MR7, ACC_CERN_RCS_SPS/LHC1/LHC2_PULSED_DIPOLE_LENGTH_MR7,
      ACC_CERN_RCS_LHC2_STEADY_DIPOLE_LENGTH_MR7 (all within 0.06 %);
    - ACC_FNAL_RCS1-4_FILL_RATIO_DIPOLE_MR7: the extractor's "not reproduced, definition not stated" is wrong — the Fermilab fill
      ratios are the field-integral bending lengths over C (33.2/34.2/51.6/72.3 % vs 33.1/34.2/51.6/72.3 %); it is the
      Table F.3 "Length with … dipole magnets" entries that exceed those bending lengths by 1.20/1.33/1.20/1.05 (now in the
      validation notes of the seven F.3 length records, P0);
    - ACC_LINAC_RLA1_EFFECTIVE_GRADIENT_MR7: S = (E1/E0)^(−mc²/(G cτ)) with S = 0.90, 250 MeV → 5 GeV kinetic gives 4.06 MV/m
      vs 4.1 MV/m (the extractor's 4.6 MV/m treated 0.25 GeV as a total energy);
    - Schulte ACC_RCS_SPS1/LHC1/LHC2_CYCLE_LOSS: Loss = (E_iron + E_copper)/E = 1.14/1.58/6.28 %; ACC_RCS_STORED_MAGNETIC_ENERGY:
      Σ E[J/m] × CERN NC-magnet length (MR7 F.1) = 201.6 MJ vs "200 MJ" (the extractor compared with the greenfield Table J.2,
      152 MJ);
    - new records ACC_VFFA_DISPERSION_SUPPRESSOR_PHASE_ADVANCE (180°: reflection 2D2 − D1 = D3) and three CBETA records.
24. **P1 → P0 (consistency or failed checks, not reproductions)**, 38 records:
    - MR7 (21): ACC_LINAC_CM2_FINAL_ENERGY, ACC_LINAC_CM1/CM2_RF_FREQUENCY_SECOND, ACC_RLA1/RLA2_RF_FREQUENCY_SECOND,
      ACC_RLA1/RLA2_RF_LENGTH_352MHZ/_1056MHZ, ACC_LOW_ENERGY_CHAIN_EXTRACTION_ENERGY, ACC_RCS1_RCS2_SAME_TUNNEL,
      ACC_RCS_NC_DIPOLE_FIELD_LIMIT, ACC_RCS2_RCS3_SC_DIPOLE_FIELD, ACC_RCS4_SC_AVERAGE_FIELD, ACC_TEVATRON_TUNNEL_CIRCUMFERENCE,
      ACC_FNAL_RCS4_CIRCUMFERENCE_BASIS, ACC_FNAL_RCS_MAGNET_FIELD_ASSUMPTIONS, ACC_VFFA1/VFFA4_INJECTION/EXTRACTION_ENERGY (_MR7);
    - TM (6): ACC_BOOSTER_INJECTION_ENERGY and _EXTRACTION_ENERGY (the "independent source" DIS2026 is the same study group's
      text, same design values), ACC_MUON_REST_LIFETIME (agreement with PDG), ACC_RCS_MUCOL_RAMP_RATE_QUOTED (rounding of the
      same slide's 4232 T/s), ACC_VFFA_ON_CREST_VOLTAGE_GAIN_FACTOR (the method only converted "√2" into 1.4142),
      ACC_VFFA_EXCURSION_MAX_ASSUMED (an assumption cannot be reproduced from what it implies) (_WS2026_TOPPMUGGLESTONE);
    - μTRISTAN (1): ACC_BOOSTER_ARC_DIPOLE_FIELD (the check fails: 3 T × 1 km bends 899 GeV/c, not 1 TeV);
    - Schulte (10): ACC_RCS_REPETITION_RATE, _PULSE_LENGTH_MIN, _CIRCUMFERENCE_MIN/_MAX, _RF_FREQUENCY, ACC_RCS1-4_TURNS (MR7
      duplicates), ACC_RCS_ENERGY_RECOVERY_EFFICIENCY_MAX (98-99 % fits SPS 1/LHC 1 but not LHC 2's 6.3 % loss) (_WS2026_SCHULTE).
25. Method arithmetic refined (levels unchanged): ACC_RCS4_TURNS_MR7 and _WS2026_TOPPMUGGLESTONE (116.75 µs → 54.6),
    ACC_RCS2_BEAM_CURRENT_PER_BUNCH_MR7 (unrounded 2.43e12 → 19.48 mA), ACC_CERN_RCS_SPS_TURNS (19.5 vs 19), _LHC1_EXT_BUNCH_POPULATION
    (2.043e12), _SPS/_LHC1_RAMP_RATE (unrounded B_inj gives exactly 3280 and 540.9 T/s), ACC_VFFA1_FIELD_INDEX /
    _VERTICAL_EXCURSION (0.0489 m with 63 GeV), the two "eight straights" records (8-fold alternation stated). Observation added
    to ACC_CERN_RCS_*_BEAM_POWER_MR7: the cells equal 2√2 × gain/turn × current within 1 % (definition not stated; P0).

## Confidence caps (research/source_quality_policy.md §4, now enforced by `lhmuc validate`, lead commit 03e0ab1)

26. Applied with `lhmuc.registry.confidence_cap` inside the fix scripts: 586 MR7 records (status analogous), 132 TM records
    (analogous or unrefereed slides) and 37 Schulte records lowered high → medium. μTRISTAN records keep high (refereed
    paper, imported_related, applicability not design_variant). No value or quotation changed by this step.

## Records added (quotable statements the extraction missed)

- ACC_VFFA_DISPERSION_SUPPRESSOR_PHASE_ADVANCE_WS2026_TOPPMUGGLESTONE — 180°, TM slide 42 figure (arrow spanning the
  "Dispersion suppressor D=D2" region along μz), reported_lhmuc, P1 (consistent with D2 = (D1+D3)/2: half a betatron oscillation
  about the D2 orbit maps D1 to 2D2 − D1 = D3).
- ACC_CBETA_INJECTOR_ENERGY (6 MeV), _MAIN_LINAC_ENERGY_GAIN (36 MeV, "± 36 MeV"), _FFA_RETURN_LOOP_ENERGY_MIN (42 MeV) / _MAX
  (150 MeV), _BEAM_STOP_ENERGY (6 MeV) — TM backup slide 49 CBETA drawing, analogous; 42/78/114/150 = 6 + 36n MeV (P1).
- ACC_RCS_SYNCHRONOUS_PHASE_REFERENCE_WS2026_SCHULTE — 135° (legend "ϕs = 135, 135, 135, 135 | ϕs = optimised", Schulte slide 17,
  also slide 41; unit inferred). The header claimed the plot had "no stated numbers".
- ACC_CERN_SITE_SC_LINAC_FOOTPRINT_LENGTH (200 m, "200x25 m."), _RLA1_LENGTH (200 m), _RLA2_LENGTH (1000 m),
  _INJECTION_TUNNEL_RLA2_SPS_LENGTH (1010 m), _INJECTION_TUNNEL_1_LENGTH (2006 m), _INJECTION_TUNNEL_2_LENGTH (2006 m),
  _TI18_LENGTH (257 m), _TI12_LENGTH (533 m) (_WS2026_SCHULTE) — CERN-site plan on Schulte slide 20, legible at 400 dpi,
  analogous, P0.

## Removed

- **ACC_RCS_LHC2_CYCLE_LOSS_SECOND_VALUE_WS2026_SCHULTE** (2 %): the cell reads "6.3/2"; reading it as a second loss value of
  2 % is unsupported (it may equally mean 6.3 divided by 2), and the 6.3 % is reproduced by (E_iron + E_copper)/E like the other
  rows. The remaining record ACC_RCS_LHC2_CYCLE_LOSS_WS2026_SCHULTE quotes the cell and explains the open '/2'. No other file
  referenced the removed id.

## Conflicts to register (preserved, not averaged) — for the lead's registry stage

The extractor's seven candidates are confirmed: (1) μTRISTAN Figure 1 2.2 nC vs text/Eq. (3) 2.3 nC; (2) μTRISTAN "about a half"
decay loss vs μLHC 82 % (now reproduced by the verifier's stepwise model, see item 19); (3) μTRISTAN 3 T × 1 km bends 899 GeV/c vs
1 TeV (needs 3.34 T); (4) Schulte 313 GeV vs MR7 314 GeV RCS1/RCS2 boundary; (5) MR7 "average magnetic field in the accelerator
16 T" vs Table 5.1 "Max. steady dipole field 16 T" (field integral: average 4.25 T); (6) TM "~10-20x gain" vs 500/70 = 7.1;
(7) MR7 RF bucket mismatch 1.3 GHz (RCS1) vs 352 MHz (RLA2). Additional: (8) MR7 Table F.3 dipole lengths 1.05-1.33 × the
field-integral bending lengths that the Table F.4 fill ratios imply; (9) Schulte "98-99 %" recovery vs the 6.3 % LHC 2 loss on
the same slide; (10) Schulte "200 MJ stored" (= Σ E × L = 202 MJ) vs MR7 Table J.1 magnetic energies 26 + 96 + 56 = 178 MJ;
(11) MR7 text 62.5 GeV vs tables 63 GeV (rounding, low priority).

## Residual doubts (not resolvable from the uploaded documents)

- **Status of generic vFFA statements on the TM deck** (slides 23, 30, 33, 37, 39-43: scaling law, zero momentum compaction,
  coupled optics, decoupling at γ = 90°, matching rules) kept reported_lhmuc/direct as the extractor chose: the speaker presents
  them as properties of the proposed LHμC booster and slide 37 restates them for the LHμC parameter set, but they are generic
  ideal-vFFA properties on slides reused from a May 2025 talk. Likewise ACC_HYBRID_RCS_PATH_LENGTH and ACC_RCS_STUDIED_BY_IMCC
  (statements about the IMCC RCS made inside the LHμC candidate review) and ACC_MUON_REST_LIFETIME (a physical constant restated
  on the requirement slide). The lead may prefer analogous for these.
- MR7 Table E.1 '88 / 264' MHz and '5 / 8' MV/m pairing (printed order only); Table E.2 RF length per linac or total; the
  synchronous phases of RLA1/RLA2 (energy gain per pass not reproduced; RLA2 4.5 × 13.5 + 5 = 65.75 ≠ 63 GeV).
- MR7 'Beam power' (Table F.1) definition: 2√2 × gain × current fits within 1 %, but Appendix J lists φs = 140/117/135° and
  557/368/326 MW to beam for the same rings.
- MR7 Table F.3 "Length with … dipole magnets": what the extra 5-33 % over the bending length contains.
- Schulte "6.3/2"; which magnet option the slide-42 field map shows; φs unit (degrees inferred); which machines "Injection
  Tunnel 1/2" connect on the slide-20 plan.
- μTRISTAN: booster circumference (semicircular arcs assumed from the sketch), injection energy (unknown), the 9 MW beam
  loading (not reproduced by any averaging rule).
- The 4.1 MV/m reproduction assumes the 90 % applies to LINAC + RLA1 together and kinetic energies; the report does not say so.
- P1 policy: this note applies "arithmetic reproduction only"; other groups' verifiers kept some consistency-based P1 labels, so
  the lead may want one repository-wide rule.

## Validation after verification

- `uv run python tools/validate_yaml.py provenance <file>`: 0 schema errors for each of the four files.
- `uv run python -m lhmuc validate`: **0 errors in this group's four files**; the repository total of 2738 errors are all
  §4 confidence-cap errors in other groups' uncommitted addendum files (detector, IR, machine, physics, source). All units parse;
  no id collision; every id referenced by these files exists.
- `uv run pytest`: all tests pass except `tests/unit/test_registry_integrity.py::test_no_validation_errors` and
  `::test_csv_registries_in_sync`, which fail only because of those other files' cap errors (the registry build refuses to run
  while validation errors exist).
