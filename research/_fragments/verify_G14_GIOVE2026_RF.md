# Verification note: group G14_GIOVE2026_RF (batch 9, 2026-10-29)

Source: SRC_IMCC2026_GIOVE_RF_SYSTEM. D. Giove (INFN), "RF System", IMCC and MuCol Annual Meeting 2026, CERN, 22–25 June 2026,
23 slides. Category ANALOGOUS_TECHNOLOGY. The talk is not a PRIMARY_LHMUC source.

File verified:

- `parameters/source/cooling_rf_thin_windows_giove2026.yaml`: 91 records at hand-over, 91 after verification (0 added, 0 removed,
  10 records edited; header gains one verification line). The group has no scenario file.

Role: adversarial verifier. For every record I checked these fields against the cited slide:

- value, unit, page, section, and table or figure label;
- quotation, uncertainty and provenance status;
- the applicability explanation, scenario assignment and validation label;
- every cross-reference to other registry ids in `notes`.

All 23 slides were read as page images. Slides 6, 7, 15 and 17 were re-rendered at 600 dpi with `pdftoppm` and cropped:

- the slide-6 cell sketch and its conductivity labels;
- the slide-7 aperture inset and table;
- the slide-15 property table and the three foil sketches;
- the slide-17 deformation panels.

The verification scripts are outside the repository, in the session scratchpad under `verify_g14/`:

- `dump.py` dumps the records;
- `quotecheck.py` and `strictcheck.py` compare quotations with the text layer;
- `fix.py` applies the edits.

## What was checked and found correct

**Status and labels.**

- No record is `reported_lhmuc`. 86 records are `analogous` with applicability `analogous`.
- The other 5 records are `unknown`: value null, category `unresolved`, confidence `none`.
- `scenario` is null throughout. That is correct, because the talk belongs to no LHμC scenario. The explanation names the only
  route of relevance: the hybrid-source option, SRC_WS1681458_ROGERS_HYBRID_SOURCE and scenario LHMUC-SOURCE-HYBRID-IMCC. Both
  exist in the registry.
- The claim that the LHμC baseline chain does not use ionisation cooling is supported by SRC_ARXIV_2610_35154 p. 3, which says
  "rather than using the conventional ionisation cooling approach".
- All records are P0. This is correct because `tests/scientific/test_batch9_documents.py` contains only Bakule 2013 and
  Cheung & Wang 2021 tests (`test_bakule2013_*`, `test_cheung2021_*`). No arithmetic in this file needs a derivation.

**Quotations.** I ran an independent check with only whitespace normalised. Every text quotation was found verbatim in the
pdftotext layer of its page. That includes the page-specific micro signs: U+00B5 on slide 5 and U+03BC on slides 15 and 17.
Only three kinds of quotation are not in the text layer, and each was checked against the image instead:

- '_' subscript markers;
- the raster conductivity labels of slide 6;
- the two-column flow texts of slides 16 and 18 joined with '[arrow]'.

**Table cells, all verified against the image.**

| Slide | Cells |
|---|---|
| 6 'Parameter / Value' | L_acc 187,8 mm; R_v 164,7 mm; W_R 60 mm; a 8 mm; b 24 mm; C_R 10 mm |
| 7 'Par, / Value' | R_A_in 85 mm; R_A_ext 113,5 mm; θ_A 15 mm; Fillet 4 mm |
| 15 Be / Al properties | density 1850 / 2710 kg/m³; therm. cond. 202.6 / 237.5 W/m/K; Young's mod. 302.2 / 70.9 GPa; tensile yield str. 525.4 / 114.8 MPa |

On slide 15 the red arrows partly cover the last digits of 70.9 and 114.8. The text layer confirms both values.

**Figure labels, read at 600 dpi.**

- **Slide 6:** 'Cu, σ =5.8e7 (S/m)' along the copper wall. The window label reads 'Al, σ =' / '=3.8e7 (S/m)', with the equals
  sign printed twice.
- **Slide 6 sketch geometry:**
  - The PEC (blue) line lies exactly midway between the mirrored window plane and the red Al window plane. L_acc therefore spans
    the whole cell.
  - R_v runs from the axis to the outer wall.
  - W_R runs from the axis to the bottom of the iris-nose ellipse.
  - a is the axial semi-axis of the ellipse and b the radial one.
  - C_R is the radius of the corner circle.
  - The extractor's sketch readings are all correct.
- **Slide 15 sketches:**
  - '20mm' is the rim width, dimensioned from the step to the edge at R_w.
  - '0.5mm' is the thickness of the thicker rim, dimensioned across its two faces.
  - '1mm' is the axial offset of the curved-step foil at the axis, measured from the reference line at the level of the outer
    section.
- **Slide 7 inset:** θ_A is drawn as an arc between the two radial edges of the aperture. The table nevertheless prints '15 mm'.
  The extractor stored it as printed, with confidence medium. That is correct.

**Text values.** The following were all confirmed on the cited slides:

| Slide | Values |
|---|---|
| 3 | 704 MHz ('of the order of'); 30 MV/m |
| 5 | 12 cm; 16 cm; 50–200 µm; 'equal'; 704 MHz |
| 8 | 127 microns; 160 mm; 99 %; 98.5 % |
| 9 | 2022 |
| 11 | 3 companies; 12000$ |
| 12 | 6061T6 / 6082T6; 150–250 micron |
| 13 | 100 mm; 15 microns |
| 14 | September 2025; max. 150 microns |
| 16 | 20 °C, stored as 293.15 K |
| 18 | 5 Hz |
| 19 | CF160; 6 circuits |

**Conversions and policies.**

- Storing 20 °C as 293.15 K is an exact conversion. I confirmed that `lhmuc.units.to_si` raises `OffsetUnitCalculusError` for
  degC.
- No value was digitised. The slide-7 |Ez| curve, the slide-17 colour maps and colour-bar limits, and the slide-18 first-mode
  curves are recorded only as explicit unknowns.

**Coverage.** I re-read every slide for numbers. None was missed. Slides 1–2 and 20–23 carry no values. The slide-21 drawing
scale 'A-A ( 0,12 : 1 )' is not a physical parameter.

**Cross-references in `notes`.** All exist and match:

- **MR7 cooling cell:** SOURCE_DEMO_CELL_RF_FREQUENCY_MR7 = 0.704 GHz and SOURCE_DEMO_CELL_RF_GRADIENT_MR7 = 30 MV/m, both
  SRC_ARXIV_2510_27437 p. 36, Table 14.2.
- **Rogers stage table, frequencies:** A1–A2 at 352 MHz and A3–A4 at 704 MHz.
- **Rogers stage table, maximum gradients:** 31.5 MV/m for A3 and 31.7 MV/m for A4.
- **Rogers, end of the concept:** the hybrid concept stops at the end of stage A4.
- **Bowring et al. 2020 via Rogers:** Cu 12.9 ± 0.4 MV/m and Be > 49.8 ± 2.5 MV/m, both at 3 T.
- **Repetition rate:** ACC_RCS1_REPETITION_RATE_MR7 = 5 Hz.

**Ids and validation.** No id collides with another file. `uv run python tools/validate_yaml.py provenance <file>` reports
0 schema errors. `uv run python -m lhmuc validate` reports 0 errors and 0 warnings over the whole registry (exit 0).

## Corrections (10 records)

1. **SOURCE_COOLING_RF_WINDOW_DESIGN_COUNT_GIOVE2026** and **SOURCE_COOLING_RF_WINDOW_SHAPES_GIOVE2026**
   (`provenance.applicability.explanation`).
   - **Before:** the explanation ended "Scan point of the INFN window parametric study (slide 15: …); a study input, not a design
     choice."
   - **Why it was wrong:** these records are the three design alternatives, not scan points.
   - **After:** "Design alternatives of the INFN window parametric study (slide 15: 'Three possible design analysed'); an
     analysis set, not a selected window design."
2. **SOURCE_COOLING_RF_WINDOW_STEP_RIM_WIDTH_GIOVE2026**, **…_STEP_RIM_THICKNESS_GIOVE2026** and
   **…_CURVED_AXIAL_OFFSET_GIOVE2026** (`provenance.applicability.explanation`).
   - **Before:** the same "Scan point" sentence.
   - **Why it was wrong:** the 20 mm, 0.5 mm and 1 mm labels are fixed sketch dimensions, not scanned variables.
   - **After:** "Fixed dimension printed on the slide-15 window sketches, not one of the scanned study variables (foil
     thickness, window radius, gradient, material); its geometric meaning is read from the arrow placement."
3. **SOURCE_COOLING_RF_WINDOW_DISPLACEMENT_EXAMPLE_CASE_GIOVE2026** (`provenance.applicability.explanation`).
   - **Before:** the same "Scan point" sentence.
   - **After:** "Case label of the slide-17 deformation colour maps: one combination of the slide-15 study variables shown as an
     example; not a selected design and not a result."
4. **SOURCE_COOLING_RF_WINDOW_DISPLACEMENT_EXAMPLE_CASE_GIOVE2026** (`notes`).
   - **Before:** "the drawn profile resembles the curved step foil".
   - **Why it was wrong:** in each slide-17 panel the S-shaped coloured curve is the deformed shape, at an unstated
     magnification. The undeformed window is the light-grey outline.
   - **After:** the note now says this. The undeformed outline shows a thin section, not drawn horizontal, joining a thicker
     outer section. That is consistent with the curved step foil of slide 15. The conclusion is unchanged; the basis is
     corrected.
5. **SOURCE_COOLING_RF_WINDOW_FAILURE_MECHANISM_GIOVE2026** (`notes`). Added: the slide does not say whether its first two
   paragraphs describe INFN work or summarise the LBNL work cited in the next paragraph ('see PAC 2001 contributions'). They may
   be restated heritage.
6. **SOURCE_COOLING_RF_GRADIENT_GIOVE2026** and **SOURCE_COOLING_RF_BREAKDOWN_DATA_GIOVE2026** (`notes`). "The only in-field
   breakdown numbers/data in the registry are …" is now "At extraction (2026-10-28) the only … were …". Other batches are writing
   to the registry concurrently, so the claim needs its date.
7. **File header.** Added one comment line pointing to this note.

No value, unit, page, quotation, status, confidence or validation label needed correcting.

## Removed

None. The 5 `unknown` records are explicit evidence gaps, as the null-means-unknown policy requires:

- breakdown data;
- shunt impedance;
- LBNL foil pre-tension;
- maximum axial deformation;
- first-mode frequency.

## Residual doubts

- **θ_A '15 mm' (slide 7).** The symbol and the inset arc indicate an angle, but the unit is a length. It is unresolved whether
  this is an angle in degrees, an arc length or a width. Confidence medium; do not use it as an angle.
- **'cavities with up to 16 cm diameter' (slide 5).** The referent is ambiguous. It cannot be the outer diameter of the slide-6
  cell, which is 2 × 164.7 mm. It matches 2 × R_w,max = 160 mm and the 160 mm LBNL foil, so it is probably the window aperture.
  Confidence medium.
- **Slide-15 property table.**
  - The table gives no reference, temperature, grade or temper.
  - It is open whether the 'Al' row represents pure aluminium or the 6061-T6 / 6082-T6 alloys proposed on slide 12.
  - The Be grade is not stated either.
  - These values are study inputs. Check them against an authoritative materials database before any use. The slides cannot
    settle this.
- **'equal' surface/axis field (slide 5).** It is stored as the ratio 1. That is a qualitative design claim, not a field-map
  result.
- **704 MHz and 30 MV/m.** The talk says only "Depending on at which cooling stages", so the stage assignment is not given.
- **'flatness control … of the order of 15 microns' (slide 13).** Read as the instrument's capability; the tool was not bought.
  The sentence opens "The flatness of the surface so far obtained may be studied", so the reading rests on grammar.
- **'in 2022' (slide 9).** The phrase grammatically allows "R&D activities … in 2022" as well as "in 2022 we have resumed". The
  year is the same either way.
- **Window thicknesses.** The span is 50–200 µm (slide 5), the commercial sheet search covered 150–250 µm (slide 12), and the
  COMEB target is max. ~150 µm (slide 14). The talk does not reconcile these. They are recorded in the notes; this is not a
  cross-source conflict.
- **Modal criterion (slide 18).** Whether every case meets 'lowest mechanical resonant frequency >> 5 Hz' cannot be checked.
  The first-mode frequencies are only plotted.
- **Talk metadata.** The talk day within 22–25 June 2026 and the Indico URL are not printed (url null).

## For the parent (files I may not edit)

- **`research/source_registry.yaml`, SRC_IMCC2026_GIOVE_RF_SYSTEM, `unresolved_questions`.**
  - The entry says "Rogers' hybrid-source rectilinear A-stages use 352 MHz". This is incomplete.
  - The Rogers records give A1–A2 at 352 MHz and A3–A4 at 704 MHz, with maximum gradients of 31.5 and 31.7 MV/m
    (SOURCE_HYBRID_RECT_A3/A4_RF_FREQUENCY_WS2026_ROGERS, SOURCE_HYBRID_RECT_A3/A4_MAX_RF_GRADIENT_WS2026_ROGERS).
  - The hybrid concept stops at the end of stage A4. 704 MHz cavities would therefore concern stages A3–A4.
  - This confirms the extractor's flag.
- **`relevance` text of the same entry.** It calls the slide-7 apertures "coupling slots". The slide does not name their
  function, so it should say "presumably coupling slots".
