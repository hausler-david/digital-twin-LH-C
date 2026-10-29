# Verification note — group G11_MUCOL_M17_VFFA (batch 8, 2026-10-28)

Source: SRC_DOI_10_5281_ZENODO_15054073, MuCol Milestone Report No. 17 "Tentative design of the FFA" (M. Topp-Mugglestone, CERN, WP5,
v1.0 Final, 27 Mar 2025, 16 pp., OFFICIAL_CERN, uploaded). Files verified:

- `parameters/acceleration/mucol_m17_vffa_design_toppmugglestone2025.yaml` (121 records at hand-over, 131 after verification)
- `parameters/machine/scenarios_batch8_vffa.yaml` (2 scenarios: MUCOL-M17-VFFA1-2025, MUCOL-M17-VFFA4-2025)

Role: adversarial verifier. Every record was checked against the cited page (page images for Tables 2.1–2.3, 3.1 and all equations;
text layer for prose), including value, unit, page, table/equation label, quotation, provenance status, derivation inputs and arithmetic,
scenario assignment and validation label. Verification script (outside the repo): `<scratchpad>/verify_mucol_m17_geometry.py`.

## What was checked and found correct

- **All 58 table cells** (Table 2.2: 7 rows × 2 columns; Table 2.3: 12 rows × 4 columns, 44 printed cells incl. blanks not recorded)
  match the p. 11 page image exactly, including `1.8 (NC)`, `1.71 × 10^-6`, `(0.382, 0.079)`, `(0.460, 0.057)`, `0.001180`/`0.001790`
  (recorded as 0.00118/0.00179, numerically identical, quotations keep the printed form) and `-0.492`.
- **All 47 prose quotations** were matched verbatim against the text layer after normalising glyphs (`◦`→`°`, `−`→`-`, ligatures,
  whitespace). The 31 fragments that did not match literally are all text-layer artefacts: line-break hyphens (`skew-|quadrupole`,
  `normal-|quadrupole`, `horizontally-|bending` across the p. 11/12 break, `Rapid-|Cycling` in the abstract, the `acc-|models-mc` URL),
  the stray `√` glyph on its own line (p. 6), spacing before punctuation (`γD ,`, `(Nc )`, `sin θF ;`, `90◦ ,`), and the garbled
  equation typesetting (eqs 1.1, 1.2, 2.1–2.3, 2.8, 3.1–3.7), which were instead checked against the page images.
- **Provenance**: no record carries `reported_lhmuc`; 105 `analogous` (page reads), 16 (now 26) `analytical_estimate` with named inputs;
  `applicability.category: analogous` everywhere with the "MuCol design, not LHμC, lattices still need numerical verification (p. 15)"
  explanation; the RCS comparator columns carry `scenario: null` and are not scenario members. Physical zeros (ramp rate 0 T/s,
  RCS excursion 0 m, path-length difference 0.0, αc = 0) are explicit zeros, not nulls. Units all parse (`radian`, `1/meter`,
  `tesla/second`, `um`, `cm`, `degree`, `dimensionless`).
- **Arithmetic re-done independently**: ρF(eq. 2.3) = 144.289 / 1268.493 m; Bρ/ρF = 6.935 / 13.148 T; 1/m = 31.31 / 82.44 mm;
  ln(p_ext/p_inj)/m = 50.39 / 99.26 mm; ln(B_gfr/B_orbit)/m = 18.52 / 62.60 mm; r0(π/Nc − βF − βD) = 1.1748 / 1.0338 m;
  kicker ½θL = 0.0999 mm; 1/sin 135° = √2; 0.252 rad = 14.44°, −0.492 rad = −28.19°; γF/m = 7.89 / −40.56 mm; 1.71e-6 × 35000 m = 60 mm;
  C/Nc = 7.582 / 35.000 m and 2πr0/Nc = 7.580 / 34.997 m. All agree with the extractor's figures.
- The 9 tests in `tests/scientific/test_mucol_m17_vffa.py` pass; the 21 P1 citations name existing tests that check the stated arithmetic.
- The ids collide with nothing in the registry; `uv run python -m lhmuc validate`: 0 errors, 0 warnings repo-wide after the edits.

## Corrections made

1. **ACC_VFFA1_D_BEND_ANGLE_DERIVED_MUCOLM17**: value 0.006353 → **0.006554 rad**; **ACC_VFFA4_D_BEND_ANGLE_DERIVED_MUCOLM17**:
   0.004718 → **0.005303 rad**. The extractor recorded the planar estimate θF − π/Nc and noted that eq. (2.1) "would change this at the
   few-per-cent level" without evaluating it. Eq. (2.1) is legible in the p. 8 page image (transcription now in the quotation field);
   evaluated with the Table 2.2 inputs it gives 0.0065543 / 0.0053029 rad, i.e. the planar estimate is 3.1 % / **11.0 %** low (it neglects
   the vertical component of the inclined F-bend). Cross-checks: eq. (2.1) equals arccos(cos θF cos(π/N) + cos γF sin θF sin(π/N)) and the
   small-angle vector sum sqrt((θF cos γF − π/N)² + (θF sin γF)²) to 1e-6, reduces to θF − π/N for γF = 0 and to θF for π/N = 0, γF = 90°
   (p. 12). Name, derivation, dependencies (+γF) and notes rewritten; validation P1 → **P0** (the cited test covers only the planar
   formula; candidate test addition); confidence medium.
2. **Stage-4 peak field "discrepancy" resolved.** The extractor reported that Bρ/ρF = 13.15 T "does NOT reproduce" the tabulated
   13.59 T (−3.3 %) and left the orbit point as unknown. With θD, γD and ρD from eqs (2.1), (2.2), (2.4)–(2.6) the reverse-bend
   D-magnet field is Bρ/ρD = **13.62 T (+0.2 %)**: the Table 2.3 "Peak Dipole Field On Orbit" is max(B_F, B_D) at extraction — the
   F-magnet for stage 1 (6.94 vs 5.83 T) and the D-magnet for stage 4 (13.62 vs 13.15 T). Records **ACC_VFFA4_ON_ORBIT_FIELD_CHECK_MUCOLM17**
   (name + notes; value 13.15 T kept as the F-magnet field, band test still valid), **ACC_VFFA1_ON_ORBIT_FIELD_CHECK_MUCOLM17** (notes),
   **ACC_VFFA1/4_PEAK_FIELD_ON_ORBIT_MUCOLM17** (validation notes) corrected; both stay P0/P1 as before because the D-magnet reconstruction
   is not yet in the test suite.
3. **Ten derived records added** (analytical_estimate, computed_from_registry, confidence medium, P0, inputs named):
   `ACC_VFFA1/4_D_INCLINATION_DERIVED_MUCOLM17` (γD = 0.4039 / −0.7756 rad, eq. 2.2), `ACC_VFFA1/4_D_RADIUS_OF_CURVATURE_DERIVED_MUCOLM17`
   (ρD = 171.6 / 1224.7 m, eqs 2.4–2.6), `ACC_VFFA1/4_D_ON_ORBIT_FIELD_DERIVED_MUCOLM17` (5.83 / 13.62 T),
   `ACC_VFFA1/4_F_MAGNET_LENGTH_DERIVED_MUCOLM17` (2ρFθF = 2.981 / 19.94 m) and `ACC_VFFA1/4_D_MAGNET_LENGTH_DERIVED_MUCOLM17`
   (2ρDθD = 2.249 / 12.99 m; hard-edge orbit path lengths, not engineering lengths). Consistency: the full geometry closes exactly
   (the orbit crosses the F end plane at azimuth βF, enters the D magnet at π/Nc − βD and reaches the D midpoint at π/Nc with a purely
   azimuthal direction), the 3D drift chord equals the table (1.1748 / 1.0338 m) and ρFθF + Ls + ρDθD = πr0/Nc to 4 decimals.
   The scenarios gained the roles `d_magnet_inclination_derived`, `d_magnet_radius_of_curvature_derived`,
   `f/d_magnet_on_orbit_field_check_derived`, `f/d_magnet_length_hard_edge_derived`; `unknown_roles` lost `d_magnet_inclination`,
   `d_magnet_radius_of_curvature`, `f_magnet_length`, `d_magnet_length` and gained `f/d_magnet_physical_length`.
4. **Confidence high → medium** on the seven formula evaluations that were marked high (ρF ×2, 1/m ×2, energy ratio ×2, stage-1
   F-field check): the batch rule reserves `high` for values read directly from the page.
5. **ACC_VFFA1/4_DRIFT_LENGTH_FROM_ANGLES_DERIVED_MUCOLM17**: notes record the exact-chord and half-cell-closure checks.
6. **ACC_VFFA_CLOSED_ORBIT_MODEL_ASSUMPTION_MUCOLM17**: note added that eq. (2.7) as printed, r3 = r2 cos βD − ρD(1 − cos θD cos γD),
   gives r3 = 939 m (stage 1) / 5220 m (stage 4) — impossible inside a metre-scale magnet — whereas the 3D reconstruction gives
   r3 = r2 cos βD − ρD(1 − cos θD) cos γD = 952.98 / 5569.95 m; the printed equation appears to carry a typographical error.
   No record uses eq. (2.7).
7. File header comment and both scenario `notes` updated to describe the above and the test coverage honestly.

## Removed

None. Every record at hand-over was supported by the cited page; none was fabricated, rounded beyond the printed precision or
mis-attributed.

## Residual doubts (not resolvable from this document; network blocked)

- Tabulated **vertical excursions** (0.048 / 0.12 m) vs the scaling-law displacement ln(p_ext/p_inj)/m (50.4 / 99.3 mm): +5 % / −17 %.
  The closed-orbit vertical sag within a half-cell from the 3D reconstruction (6.4 mm stage 1, 34.4 mm stage 4, F-midpoint to
  D-midpoint) does not reconcile them either (sum 56.8 / 133.7 mm). The report's excursion definition remains unknown; recorded as bands.
- **Tune pairs**: plane assignment and per-cell vs ring tunes not stated; values not checkable without the transfer-matrix formalism
  (thesis ref. [3] and the acc-models-mc notebooks are blocked).
- **Good-field-region peaks** (12.52 / 29.04 T) depend on the Mais–Ripken projection and an unstated beam-size multiple; only the
  equivalent one-dimensional vertical extents (18.5 / 62.6 mm) are derived.
- The derived D-magnet quantities rest on eqs (2.1), (2.2), (2.6) as transcribed from the page image; they pass two limiting-case
  checks and an independent 3D reconstruction, and reproduce the stage-4 peak to +0.2 % (within the 3–4 significant figures of
  Table 2.2), but were not run against the author's notebooks.
- **RCS4 "16" T**: NC or SC qualifier not printed. **`horizontally-bending`** (p. 11/12 break): hyphen kept as printed; may be a
  line-break hyphen.
- Scenario `status: reported` was kept; `partially_reported` would be equally defensible for an analytic design with 20 unknown roles.
- Registry follow-ups outside this group's files: `research/source_registry.yaml` `parameters_extracted` for
  SRC_DOI_10_5281_ZENODO_15054073 is still empty; the intra-source excursion band and the eq. (2.7) typo are candidates for
  `research/source_conflicts.yaml`/`unresolved_searches.md`; the D-magnet reconstruction and the exact-chord drift are candidate
  additions to `tests/scientific/test_mucol_m17_vffa.py` (tests/ not edited by this verifier).
