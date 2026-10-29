# Verification note: group G7D_SCHULTE_DECK (addendum G7, 2026-10-29)

Source: SRC_WS1681458_SCHULTE_IMCC. D. Schulte (CERN, for the IMCC), "Muon Collider", IMCC overview at the Kraków workshop
'Ultra-cold muons for the LHC' (AGH Kraków, 24–26 Sept 2026), 45 slides. In the registry: source_type workshop_talk,
category CONFERENCE_PROCEEDING, access uploaded. The SHA-256 of the archived PDF (d7509464…8953) matches the registry. The
page number is the slide number, and every slide prints its own number, so the PDF page and the printed slide number are
the same. Slide 27 is a "Reserve" divider, so slides 28–45 are reserve slides. Cross-checks were made against
SRC_ARXIV_2510_27437 (MuCol Milestone Report 7, MR7). In MR7 the PDF page is the printed page + 11.

File verified (the only file edited):

- `parameters/machine/imcc_ws2026_schulte_parameters.yaml`
  - 342 records at hand-over, 341 after verification: 1 duplicate removed, 0 added.
  - All 341 records were touched: each now has a stage- and caveat-specific `applicability.explanation`.
  - No numeric value, unit, page, status, extraction method or validation level changed.
  - The file is re-emitted in the generator's house style, so fields I did not touch are byte-identical.
  - Four comment lines were added to the header, and its scope statement now points to the slide-6 record in the physics
    file.

Role: adversarial verifier. I treated every record as unverified, including any the killed verifier may have touched. I
checked:

- value, unit and page;
- section and table/figure label;
- quotation;
- uncertainty and allowed range;
- status and applicability;
- confidence and validation label;
- notes, against the cited pages.

No record carries a derivation, and none needed one.

## Method

1. **Slide images.**
   - All 45 slides were rendered with `pdftoppm` at 150 dpi.
   - Slides 8 and 18 were also rendered at 300 dpi, slide 21 at 400 dpi and slide 29 at 600 dpi.
   - The five embedded raster images of slide 29 were extracted with `pdfimages`. The slide-29 tables are rasters, and the
     call-out line, red frame and "Totals" box are vector overlays drawn on top of them.
   - The text layer (`…/scratchpad/text/Schulte_Muon_Collider_IMCC_overview_pNN.txt`) was used only to locate passages.
     It garbles superscripts and Symbol-font glyphs: `1012`, `1034` and `m+` stand for 10^12, 10^34 and μ+.
2. **Tables transcribed independently and compared by script.** Every printed cell matched:
   - slide 3: 8 cells;
   - slide 7: 12 cells;
   - slide 38: 8 cells;
   - slide 8: 62 cells;
   - slide 18 radial build: 9 rows and the total;
   - slide 21 power table: 21 cells;
   - slide 29 resource table: 68 visible cells;
   - slide 29 deliverables table: 52 values;
   - slide 45: 9 values.

   Text values were checked against the slide images. These are slides 2, 6, 12, 13, 14, 16, 18, 20, 23, 30, 39, 43 and 45.
3. **Figure reads re-done by pixel analysis** (400 dpi; scripts in `…/scratchpad/g7d/`). Gridlines were fitted linearly:
   - Cost-range chart: residual ≤ 0.02 BCHF. Bar edges and red markers were located by colour.
   - Tornado chart: residual ≤ 1.4 px ≈ 7 MCHF.
4. **MR7 cross-references in notes were checked on the MR7 page images or text layer.** The pages used are:
   - p. 13: Table 1.1;
   - p. 14: Tables 1.2 and 1.3 and their captions;
   - p. 20: Tables 6.1 and 6.2;
   - p. 28: Table 12.2;
   - p. 37: Table A.1;
   - p. 40: Table A.2;
   - p. 70: Appendix H.2;
   - p. 86: Table L.2.
5. **The arithmetic in `validation.methods` and `validation.notes` was recomputed independently** (`…/scratchpad/g7d/arith.py`),
   using PDG constants: m_μ = 0.1056584 GeV and τ_μ = 2.19698 µs.

## Found correct

- **Values, units and pages.** All 341 remaining records hold the printed value: unit-scaled (×10^12, ×10^34) and with the
  printed unit. Every figure read lies within its stated interval.
- **Slide 8 chain table.** All 62 cells are correct. These include the italic '90*' of the Low-Energy Acc. row, the
  '◦' circumference marks, the 'Target' column (Pre-Acc. 4.0, 3 TeV collider 2.2, 10 TeV collider 1.8) and the
  '500 (p+)' and '5 (p+)' proton entries.
- **Slide 21 power table.** All 21 cells are correct, and each of the three TOTAL cells equals the sum of its column exactly.
- **Slide 21 cost-range chart.** My independent read, against the recorded value, is:

  | Scenario | Left end | Red marker | Right end |
  |---|---|---|---|
  | 10 TeV Green Field | 14.04 (14.1) | 19.12 (19.1) | 28.06 (28.0) BCHF |
  | 7.6 TeV @ CERN | 11.54 (11.6) | 15.95 (15.9) | 23.73 (23.7) BCHF |
  | 3.2 TeV @ CERN | 8.71 (8.8) | 11.90 (11.9) | 17.59 (17.5) BCHF |

  All nine agree within 0.1 BCHF, so the values were kept. The slide prints **no "4–18 BCHF"**. Its
  Snowmass-style panel 'Project Cost (no esc., no cont.)' carries the bin labels 4 | 7 | 12 | 18 | 30 | 50 with no unit,
  and the BCHF chart spans ≈ 8.7–28.1 BCHF. The record INFRA_IMCC_COST_PROJECT_SCALE_P21_WS2026_SCHULTE already said so.
- **Slide 21 tornado chart 'Sensitivity Analysis for 7.6 TeV'.** I measured all 18 bar ends independently:

  | Item | Negative variance | Positive variance |
  |---|---|---|
  | SC Magnets | −1008 | +1877 |
  | RF | −993 | +1650 |
  | Solenoids | −950 | +1766 |
  | Other | −417 | +720 |
  | General infrastructure | −287 | +536 |
  | Power Converters | −272 | +439 |
  | Civil Engineering | −258 | +410 |
  | NC Magnets | −204 | +309 |
  | Cryogenics | −103 | +168 |

  Units are MCHF. All 18 lie within 10 MCHF of the records, whose intervals are ±50 MCHF.
- **Slide 21 pie chart.** The seven printed percentages are correct and sum to 100.1 %. The colour-to-category mapping is
  confirmed by the clockwise slice order, which follows the legend order.
- **Slide 29.**
  - All 68 resource-table records are visible cells. None was filled from a hidden cell.
  - The 52 deliverable values match the table. None comes from the hidden 'Fast-ramping magnet system' row.
  - The five 'Totals' box values are correct.
  - The LTS-dipole '160 mm' is struck through by the call-out line on the rendered slide. The embedded raster
    (562 × 731 px) reads '160 mm diameter, 11 T, 4.5 K, 5 m long' without overprint, and slide 45 gives 'Nb3Sn at 4 K,
    11 T, 16 cm aperture'. The record keeps medium confidence.
- **Statuses.** All 341 records are `analogous`, with `applicability.category: analogous`. There is no reported_lhmuc,
  imported_related, derived_lhmuc or analytical_estimate, and no value was computed by the extractor.
  - Confidence: 311 medium, 30 low; none is high.
  - Every value is non-null; no record has value 0.
  - Ids are unique.
  - The four ids used by `parameters/machine/scenarios_addendum_imcc.yaml` are unchanged:
    - INFRA_IMCC_COST_10TEV_GREENFIELD_CENTRAL_P21_WS2026_SCHULTE
    - INFRA_IMCC_POWER_TOTAL_10TEV_P21_WS2026_SCHULTE
    - MACHINE_IMCC_COLLIDER_TECHNOLOGY_3TEV_P7_WS2026_SCHULTE
    - MACHINE_IMCC_COLLIDER_TECHNOLOGY_10TEV_P7_WS2026_SCHULTE
- **"Not duplicated" claims in the header.** I confirmed them against the other files:
  - BIB '40 000 muons/m/bunch crossing': PHYS_IMCC_BIB_MUON_DECAYS_PER_M_PER_CROSSING_WS2026_SCHULTE.
  - Slide-28 table: PHYS_IMCC_*_WS2026_SCHULTE.
  - RCS slides: the acceleration file.
  - Slide-3 bullets: PHYS_IMCC_FEASIBILITY_TARGET_* and PHYS_IMCC_INITIAL_STAGE_*.

  The slide-3 *table* records in my file are not duplicates of these, because they come from a separate printed table.

## Removed (1)

- **MACHINE_IMCC_LUMINOSITY_SCALING_STATEMENT_P6_WS2026_SCHULTE.** It duplicates the committed, verified record
  PHYS_IMCC_LUMI_SCALING_MUP_ADVANTAGE_STATEMENT_WS2026_SCHULTE in
  `parameters/physics_programme/imcc_ws2026_schulte_physics_and_dudko_formula.yaml`, which has the same source, the same
  slide and the same four statements, with a verbatim quotation that includes the '⇒'. The duplicate's value also
  misparaphrased the slide as "constant current for luminosity ∝ energy". The slide says "Constant current for required
  luminosity scaling with collision energy", and its own formula gives L ∝ γ² at constant f_r·N0.

  The removed id appears outside my file only in the lead's historical log
  `research/_fragments/confidence_caps_applied_2026-10-29.csv`, which I did not edit.

## Corrections

**Quotations (24 records), made verbatim against the slide image:**

- MACHINE_IMCC_MU_BUNCH_POPULATION_3TEV/10TEV_P7_WS2026_SCHULTE: unit cell "(1012)" → "(10^12)".
- MACHINE_IMCC_LUMI_PER_IP_3TEV/10TEV_P38_WS2026_SCHULTE: "(1034 cm-2s-1)" → "(10^34 cm-2s-1)".
- MACHINE_IMCC_CHAIN_MUPLUS_EXCESS_P8_WS2026_SCHULTE: "Note: m+ can be 30% higher" → "Note: μ+ can be 30% higher".
- MACHINE_IMCC_CHAIN_TRANSMISSION_STATUS_P8_WS2026_SCHULTE: removed two full stops that are not on the slide.
- INFRA_IMCC_COST_{10TEV_GREENFIELD,7P6TEV_CERN,3P2TEV_CERN}_CENTRAL_P21_WS2026_SCHULTE: "red central marker" → "red marker".
  The slide does not call the marker central.
- Slide-29 resource table (15 records): the cells are now transcribed exactly as printed.
  - TOTALS FTE III and V: '194.0' and '267.0'.
  - Detector FTE III–VII: '70.0' and '93.0'.
  - Magnets Material I, IV and V: '3.0', '10.0' and '11.0'.
  - Demonstrator FTE II: '11.0'.
  - The four 'Accelerator Design' records: row label "Accelerator Design and Technology" →
    "Accelerator Design and Technolo[gies]". The overlay cuts the label after "Technolo", and the raster reads
    "Technologies". The same label was also fixed in the four record names.

**Confidence lowered to low (4 records).**

- INFRA_IMCC_COST_10TEV_GREENFIELD_CENTRAL, INFRA_IMCC_COST_7P6TEV_CERN_CENTRAL, INFRA_IMCC_COST_3P2TEV_CERN_CENTRAL
  (_P21_WS2026_SCHULTE): these are figure reads (no number is printed on the bars), and the slide does not state what
  the red marker is.
- INFRA_IMCC_COST_PROJECT_SCALE_P21_WS2026_SCHULTE: the bin labels are printed, but the MC-3/MC-10 shading is a figure
  read and the panel prints no unit.

All other figure reads were already low: 6 bar ends and 18 tornado bars. The records kept at medium with
`manual_figure_read` carry numbers printed inside figures: the slide-18 radial-build table, the pie labels, the
'±16.7 Tm' label and the slide-13 figure labels.

**Uncertainty (2 records).** MACHINE_IMCC_NB3SN_EXPECTED_FIELD_P14 ("O(11 T)") and
SOURCE_IMCC_DEMO_PROTON_BEAM_POWER_UPGRADE_P23 ("O(80 kW)") changed from `not_stated` to `order_of_magnitude`, as
`docs/uncertainty_policy.md` requires for approximate wording. The note quoting the wording is kept. Both records are now
consistent with the existing "O(10kW)" and "O(±1mradian)" records.

**Allowed-range basis (2 records).** MACHINE_IMCC_NBTI_OPERATING_TEMPERATURE_MIN/MAX_P14: the basis now quotes the slide
verbatim, "'operating at 2-4 k'" with its lower-case k.

**Categorical values (3 records).**

- SOURCE_IMCC_TARGET_MATERIAL_QUESTION_P13: "graphite instead of mercury" stated the slide's question as a fact. It is now
  "'Can we replace mercury with graphite?' (challenge); …".
- SOURCE_IMCC_TARGET_SOLENOID_CONCEPTS_P13: removed "(IMCC)" after "All-HTS solenoid", which the slide does not state.
  The value now lists the two figure labels verbatim.
- MACHINE_IMCC_CHAIN_TRANSMISSION_STATUS_P8: added the 3 TeV shortfall (1.7 vs 2.2e12) next to the pre-acceleration and
  10 TeV ones.

**Names (11 records).**

- The three cost markers (see above).
- MACHINE_IMCC_COLLIDER_DECAY_POWER_LOSS_P18: the slide says only "500 W/m loss". The decay-product attribution is
  from MR7 §12.2 and is now marked as such.
- MACHINE_IMCC_MOVER_VERTICAL_BEND_P18: the neutrino-flux purpose is stated on slide 19, not slide 18. This is now said
  in a note.
- INFRA_IMCC_RD_DELIVERABLE_FINAL_COOLING_ABSORBER_MUONS_P29: "muons per bunch" → number of muons. "Per bunch" is not
  printed.
- MACHINE_IMCC_BEAM_BEAM_FEEDBACK_TURNS_P43: the name is now neutral. The bullet says only "20 turn feedback". A note
  records that a plot on the same slide has the axis "Damping time [# of turns]", which supports the damping-time
  reading.
- The four Accelerator-Design records (label).

**Explanations (all 341 records).** The generic text named neither the stage nor the deck's own caveat. Each
explanation now names:

- the IMCC machine and stage: 3 / 10 TeV, the 3.2 / 7.6 TeV CERN variants, or a chain part shared by both stages;
- the slide's own qualifier: 'Site independent', 'Muon Collider Target Parameters', 'Achieved' = simulated status vs
  'Target', 'Challenge' = requirement, 'Expect …', 'Bottom up cost estimate … Conceptual designs', '(no esc., no cont.)',
  R&D-plan goals;
- reserve-slide status, for slides 29, 30, 38, 39, 43 and 45;
- figure-read status and the source's unrefereed-slide status.

Two explanations wrongly said "Read from a figure on the slide (no printed number)" about numbers that *are* printed as
figure labels: '±16.7 Tm' and 'L = 702.30 [m]'. Both are fixed. The 702.3 m record stays low because the plotted
section is not identified.

**Section labels (137 records).** Slides 29, 30, 43 and 45 are now marked "(reserve slide N)", as slides 38 and 39
already were.

**Notes.**

- **Slide 8, all 62 table records.** MR7 comparisons were attached to the wrong quantities. For example, the
  transmission and μ−/bunch comparisons sat on the *energy* records, the RLA2 length comparison on RLA2 *energy*, and the
  10 TeV circumference comparison on 10 TeV *energy*. Each record now carries the MR7 Table 1.2/1.3 (PDF p. 14) or
  Table A.2 (PDF p. 40) value of its own quantity. Where the values differ, the note says "conflict candidate, not
  averaged". The differences are:
  - energies: Charge Sep. 0.17/0.2, Rect. A 0.14/0.2, Bunch Merge 0.12/0.13, Rect. B 0.14/0.124 GeV;
  - lengths:
    - RLA2: ◦2430 on the slide vs ◦2400 in MR7 Table 1.2; MR7 Table A.2 also gives 2430.
    - Rect. B and Pre-Acc.: Table A.2 gives 487 and 245 m.
    - 10 TeV collider: ◦10000 on the slide vs ◦11400 in Table 1.2; Table A.2 gives 10000.
  - transmissions: Rect. A 50/49.6, Rect. B 32/28.6, Final Cooling 60/61.4, RLA2 90/92.6 %;
  - μ−/bunch: slide 'Achieved' vs MR7 Table 1.3 'Estimated', from Rect. A onwards;
  - Pre-Acc. target: 4.0/3.6e12.
- **MACHINE_IMCC_CHAIN_LOW_ENERGY_ACC_ACHIEVED_TRANSMISSION_P8.** Added that the asterisk's meaning is not on the slide,
  and that in MR7 Table 1.2 the asterisk marks RCS4's '90*' with the 10 % loss-budget footnote.
- **Luminosity records (P3, P7, P38).**
  - 10 TeV: added "MR7 Tables 1.1/A.1: 18e34" (17.5 vs 18).
  - 3 TeV: MR7 Table A.1 gives 2.1e34; added to P3 and P38, and P7 now gives the page.
- **10 TeV circumference (P7, P38).** Added the in-deck conflict: slide 8 ◦10000 m and the slide-20 CERN-site plan
  "Length 10 km", against MR7's 11.4 km, 10000 m and '≈ 10' km.
- **Slide-38 records.** The 'Int L' row (2.2 / 1.8 'Ab-1') sits where slide 7 has 'N | 10^12 | 2.2 | 1.8', which is a
  probable label slip.
- **MACHINE_IMCC_ARC_SHIELDING_MIN/MAX_P18.** Removed the unsupported "(14 T/20 K)" attribution to MR7 Table 6.2. Table
  6.2 says only 30 mm, and its caption says 40 mm "for options using low temperature superconductor, i.e. at 3 TeV".
  The note now flags the same-slide conflict: 30-40 mm in the heading vs 20-40 mm in the radial-build table.
- **IR_IMCC_BETA_STAR_MIN/MAX_P18.** Both readings are now given: Table 6.1 target/relaxed 1.5/5 mm at 10 TeV, and Table
  A.1 5 mm at 3 TeV and 1.5 mm at 10 TeV.
- **MACHINE_IMCC_DIPOLE_LIMIT_NBTI_FIELD_P45.**
  - MR7 H.2 (PDF p. 70) calls NbTi (1.9 K) "inadequate" for arc magnets of up to 16 T / 160 mm. That is a different
    requirement, not a statement about 10 TeV only.
  - The match with the slide-28 'CERN 1 tunnel' 3.2 TeV column is not stated on slide 45. The note no longer says that
    the slide-45 figure "applies to" that column.
- **INFRA_IMCC_POWER_TOTAL_10TEV_P21.** The site of the 10 TeV power column is not stated; it is probably the green-field
  design.
- **Pages added to MR7 references:**
  - MACHINE_IMCC_COLLIDER_DECAY_POWER_LOSS_P18: Table 12.2, p. 28;
  - SOURCE_IMCC_DEMO_PROTON_BEAM_POWER_LIMITED_COST_P23: Table L.2, p. 86;
  - MUPLUS: Table 1.2 caption, quoted in full.

## Arithmetic re-done

Constants: γ(5 TeV) = 47322.3, so γτ_μ = 103.97 ms.

| Record(s) | Check | Result | Verdict |
|---|---|---|---|
| MU_LIFETIME_P2 | γτ_μ for 5 TeV beams | 103.97 ms (104.1 with 2.2 µs) vs 'Up to 100 ms' | reproduced as a rounded statement (−3.8 %) |
| 13 CHAIN_*_ACHIEVED_MU_PER_BUNCH_P8 | previous printed × transmission | 45, 42.75, 21.4, 16.69, 5.344, 3.18, 2.752, 2.52, 2.25, 2.07, 1.89, 1.71, 1.53 vs 45.0 … 1.5 | all within ±0.05 (printed rounding); unrounded chain 500e12 → 1.463e12 vs 1.5e12 |
| PD_BEAM_POWER_P12 | 5e14 × 5 GeV × 5 Hz | 2.003 MW vs 2 MW | reproduced |
| TARGET_ENERGY_PER_PULSE_P13 | 2 MW / 5 Hz | 0.4 MJ vs printed '400 MJ/pulse' | **NOT reproduced** (factor 1000; slide 29 prints 0.4 MJ/pulse); kept as printed, low |
| ARC_MAGNET_APERTURE_MIN/MAX_P18 | 2 × Σ Δr (W 20 / 40 mm) | 118.00 / 158.00 mm | reproduced exactly |
| POWER_TOTAL_{3P2,7P6,10}TEV_P21 | column sums | 113.425 / 172.265 / 188.015 MW | reproduced exactly |
| RD_DETECTOR_MATERIAL/FTE_P29 | Σ Detector row (all visible) | 20.4 MCHF / 907.3 FTEy vs 20 / 900 | within rounding (+2 %, +0.8 %) |
| RD_ACCELERATOR_MATERIAL/FTE_P29 | Σ TOTALS − Σ Detector (visible rows only) | 304.7 MCHF / 1772.3 FTEy vs 300 / 1800 | within rounding (+1.6 %, −1.5 %) |
| RD_TOTALS_{MATERIAL,FTE}_Y01/Y02_P29 | sum of the four groups | 5.7, 103.3, 11.4, 146.5 | reproduced exactly (only years I–II have all four groups visible) |
| RD_DURATION_P29 | count of year columns | 10 | consistent (a count, not a check) |
| RD_DELIVERABLE_TARGET_STUDIES_ENERGY_PER_PULSE_P29 | 0.4 MJ × 5 Hz | 2.0 MW = slides 12/13 | reproduced |
| ACCUMULATION_TIME_SI3/SI10_P3 (new candidate check) | 2 + Int L / (2 IPs × L × 1e7 s) | 2 + 2.78 / 2 + 2.86 vs '2+2.8' / '2+2.9'; slide-28 CERN variants 2.50 / 5.00 / 5.56 / 6.33 vs '2+2.5' / '2+5' / '2+5.6' / '2+6.3' | reproduced if a year is 1e7 s at nominal L (not printed; inferred). The '2' matches the slide-28 ramp-up 5 + 25 + 70 % = 1 nominal year in 3 |
| COLLIDER_DECAY_POWER_LOSS_P18 (note) | 2NEf_r/C × 1/3 at 10 TeV | 0.42 kW/m (C = 11.4 km), 0.48 kW/m (10 km) vs '500 W/m' | order-of-magnitude consistent (MR7 Table 12.2: 0.443 kW/m) |
| COST_7P6TEV_CERN_CENTRAL_P21 (note) | tornado sums vs bar | Σneg −4.53 (−4.49) BCHF vs marker − left 4.3 (4.41); Σpos +7.84 (+7.88) vs right − marker 7.8 (7.78) | consistent: the bar is the marker ± the summed variances, which supports reading the marker as the point estimate |
| COST_SHARE_*_P21 | pie sum | 100.1 % | consistent (rounding) |

## P1 labels

No record in this file qualifies for P1. The pinned tests in `tests/scientific/test_imcc_mr7_reference.py` check MR7
quantities:

- Table A.1: beam power, IP beam size, luminosity lifetime;
- the hourglass factor;
- eq. (A.7)/(A.9);
- integrated luminosity per year.

None of these is a value of a Schulte-deck record. Where a slide prints the same number as an MR7 input (N = 1.8e12,
f_r = 5 Hz, C = 11.4 km), the tests use it as an *input* and do not assert it. MU_LIFETIME's 100 ms is not 0.104 s and
is not asserted either. The 30 records of this file that the lead lowered from P1 (listed in
`research/_fragments/validation_levels_lowered_2026-10-29.csv`) stay P0. Each of them now carries a "Verifier 2026-10-29"
`validation.notes` entry that recomputes the claimed arithmetic and states that no test checks the value. Three other P0
records got the same kind of note: the 400 MJ/pulse record and the two accumulation-time records.

## Slide-29 hidden cells

On the rendered slide, two areas are hidden:

- the 'Totals' box covers the year III–X cells of the 'Accelerator Design and Technologies' and 'Demonstrator' rows, and
  the header labels III–X;
- the enlarged deliverables box hides the 'Fast-ramping magnet system' row.

The embedded raster images under the overlays still contain these cells and that row. Following the lead's rule, they
were **not** recorded, and their contents are not repeated here. No check above uses them. If the lead decides that
underlay content may be used, the rasters can be extracted with
`pdfimages -f 29 -l 29 -png <pdf> <prefix>`: image 2 is the deliverables table and image 4 the resource table.

## Residual doubts (for the lead)

1. **Registry relevance text.** `research/source_registry.yaml` describes the source as having a "cost 4–18 BCHF
   scale". The slide prints no such range. It prints a unit-less 4 | 7 | 12 | 18 | 30 | 50 panel, and a BCHF chart with
   bars from ≈ 8.7 to ≈ 28.1 BCHF. The registry is not my file.
2. **Figure reads and status.** Policy §5 rule 3 says that numbers read off a plot axis are `analytical_estimate`. The
   cost-bar and tornado reads (27 records) and the Snowmass-style panel (1 record) follow the lead's G7 rule instead:
   `analogous`, low, "approximate", with interval uncertainty for the 27 numeric reads. The lead should confirm which rule
   governs.
3. **Conflict candidates kept in notes, not in `research/source_conflicts.yaml`** (not my file). If they are registered,
   policy §4 requires `low` for every competitor until a treatment is decided. The candidates are:
   - 10 TeV circumference: 11.4 km (slides 7 and 38; MR7 Tables 1.1, 1.2, A.1) vs ◦10000 m (slide 8; MR7 Table A.2) vs
     '≈ 10' km (MR7 Table 6.1);
   - L/IP: 17.5 vs 18e34 (10 TeV) and 1.8 vs 2.1e34 (3 TeV);
   - slide 8 vs MR7 Tables 1.2/1.3 (energies, lengths, transmissions, μ−/bunch, Pre-Acc. target);
   - shielding: heading 30-40 mm vs table 20-40 mm on slide 18;
   - slide 13 '400 MJ/pulse' vs 0.4 MJ.
4. **Physics file (not mine).** PHYS_IMCC_INT_LUMI_3TEV/10TEV_P38_WS2026_SCHULTE (2.2 / 1.8 ab^-1) are the slide-38
   'Int L' cells. These are almost certainly the bunch populations under a wrong row label (slide 7 prints
   'N | 10^12 | 2.2 | 1.8' in that position). The records are already low and flagged.
5. **Scenario file (not mine).**
   - IMCC-MR7-10TEV uses INFRA_IMCC_POWER_TOTAL_10TEV_P21_WS2026_SCHULTE. The slide does not say which 10 TeV design
     that column is: the green-field design, or the CERN 10 TeV that is 'maybe possible'.
   - It also uses INFRA_IMCC_COST_10TEV_GREENFIELD_CENTRAL_P21_WS2026_SCHULTE, which is now `low`.

   The scenario stays P0 in either case.
6. **The red marker on the cost bars** is not defined on the slide. The tornado-sum consistency supports reading it as
   the point estimate, but that is an inference.
7. **Accumulation time.** The 1e7 s per year in the '2 + X' reconstruction is inferred, not printed. The records keep the
   printed strings.
8. **Id prefix.** The slide-8 chain ids use the prefix MACHINE_ while their `subsystem` is `source`, `acceleration` or
   `machine`. The ids were kept because they name the right quantity and renaming would only add churn.
9. **Reused slide.** Slide 6 carries the footer "D. Schulte, Muon Collider Overview, GGI, June/July 2025". It was reused
   from an earlier talk. The statement is now recorded only in the physics file.

## Validation

- `uv run python tools/validate_yaml.py provenance parameters/machine/imcc_ws2026_schulte_parameters.yaml`: 0 schema errors.
- `uv run python -m lhmuc validate`: 0 errors, 0 warnings, for the whole registry.
- `uv run pytest`: all tests pass except two, which only the lead's registry stage can fix:
  - tests/unit/test_registry_integrity.py::test_csv_registries_in_sync;
  - tests/unit/test_registry_integrity.py::test_source_parameters_extracted_in_sync.

  The lead must run `tools/build_registries.py` and `tools/sync_parameters_extracted.py`. Both tests fail for every new
  G7 file, not because of this verification.
- Nothing was committed.
- Scripts and renders are in `/tmp/claude-0/-home-user-digital-twin-LH-C/0f2c7853-3fdb-534d-84ae-c6857c596b01/scratchpad/g7d/`:
  - `scripts/apply_g7d.py`, which applies every correction to the pristine copy `imcc_ws2026_schulte_parameters.ORIG.yaml`;
  - `scripts/emit7d.py`, the house-style emitter;
  - `check_p8.py`, `check_p29.py`, `measure_cost.py`, `measure_sens.py` and `arith.py`;
  - `changes.json`, the per-record change log.
