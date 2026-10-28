# Verification note — SRC_ARXIV_2610_35154 (arXiv:2610.35154v1, Piotrzkowski, LHμC DIS2026 proceedings)

Verifier: adversarial check of every parameter record extracted from this document. Date: 2026-10-28.

## Scope

Files checked (all 71 parameter records + 2 scenarios):

- `parameters/machine/lhmuc_dis2026.yaml` (33 records)
- `parameters/source/lhmuc_dis2026_source.yaml` (12 records)
- `parameters/acceleration/lhmuc_dis2026_acceleration.yaml` (10 records)
- `parameters/interaction_region/lhmuc_dis2026_ir.yaml` (16 records)
- `parameters/machine/scenarios_dis2026.yaml` (2 scenarios)

Method: every record's page, section, table/figure label and quotation were compared against the
per-page text (`.../scratchpad/text/arXiv-2610.35154v1_pNN.txt`, all 7 pages read in full) and the
rendered PDF pages 2, 3 and 4 (Fig. 1, Fig. 2 with labels, Table 1). Analytical records were
recomputed (sqrt(s), 1/250 ns, 80 x 250 ns, 3000 m / c, gamma*tau_mu with PDG constants in
`lhmuc/analytical.py`). `tests/scientific/test_analytical_checks.py` was run (15 passed), confirming
the extractor's P1 claims (sqrt(s), collision rate, Table 1 luminosity reproduced with H = 1).

## Result

- No record was found without support in the document. **Removed: none.**
- No value, unit, page, table/figure label or scenario assignment was wrong. All Table 1 cells
  (5.3 TeV; 2.1e34; 4(12.5); 4.8/4.8 um; 0.07/22 x 10^11), the text numbers (80 bunches, 250 ns,
  12.5 Hz, 1 GeV, 70 GeV, 500 GeV, 3 passes, 1 pass, 2 vFFAG beamlines, 9 km, 3(6) km, 5 %, 4 MW,
  1 GeV to top energy, three neutrino directions, 30 (15) TeV) and the Fig. 1/Fig. 2 labels
  (4 x 10^-3 < y < 1, x_Bj axis from 10^-7, LHeC 50 GeV, proton linac 500 MeV, RCS 3 GeV) were
  confirmed verbatim.
- Status assignment is consistent with the rules: 64 reported_lhmuc (PRIMARY_LHMUC source),
  3 derived_lhmuc and 2 analytical_estimate with derivations naming input ids, 1 imported_related
  (LHeC 50 GeV from the Fig. 1 legend, applicability analogous), 1 unknown with value null
  (crossing angle). The only value the paper itself imports (Fig. 2 layout "based on the μTRISTAN
  proposal", labels 500 MeV / 3 GeV) is already flagged at confidence medium with
  manual_figure_read.
- The extractor's audit observation that 80 bunches x 250 ns = 20 us exceeds the ~10 us revolution
  period of a ~3 km ring is arithmetically correct and is also consistent with the μLHC paper
  (SRC_ARXIV_2506_15445, p.11: 40 bunches, 75 m, 250 ns, "each turn takes approximately 10 μs").
  It remains a candidate `research/source_conflicts.yaml` entry (not written here).

## Corrections made (10 edits, no ids changed)

| # | parameter_id | field | before | after | reason |
|---|---|---|---|---|---|
| 1 | MACHINE_LONG_TERM_SQRT_S_FCCHH_DIS2026 | provenance.applicability.explanation | "...would require e.g. E_mu = 2.25 TeV on 100 TeV protons (audit note...)" | decomposition removed; states that FCC-hh/HE-LHC proton energies and the assumed muon energy are not given in this source | The audit arithmetic was wrong (100 TeV is the FCC-hh c.m. energy, not the proton beam energy) and rested on numbers absent from the document. |
| 2 | ACCEL_LHEC_ERL_PASSES_EXAMPLE_DIS2026 | provenance.applicability.explanation | "(LHeC: 3 passes x 2 linacs x ~10 GeV = ~60 GeV plus injection; ...)" | LHeC lattice arithmetic removed; points to refs [4-6, 23] | Unsourced external numbers (LHeC linac energies) not in the document; the 2020 LHeC CDR values differ from the 2012 ones, so the claim was not safe. |
| 3 | ACCEL_BOOSTER_CIRCUMFERENCE_DIS2026 | provenance.applicability.explanation | "9 km is the LHeC ERL racetrack scale (the LHeC CDR racetrack is ~9 km)" | states only that the paper re-uses LHeC ERL infrastructure and does not give the origin of the 9 km figure | Unsourced external claim; the source does not say this. |
| 4 | PROTON_BUNCH_POPULATION_DIS2026 | provenance.applicability.explanation | "Ten times the HL-LHC nominal 2.2e11" | "Ten times the 22 x 10^10 protons per bunch that the μLHC paper (SRC_ARXIV_2506_15445, Table 2, p.12) quotes for the HL-LHC proton beam" | The comparison number now has a traceable source (verified in the μLHC per-page text, p.12). |
| 5 | MACHINE_AVERAGE_LUMINOSITY_DIS2026 | uncertainty | type order_of_magnitude | type not_stated, note explaining 'close to 10^34' is an approximate statement | "close to 10^34" is not an order-of-magnitude (factor-10) uncertainty; the enum has no "approximate" type, so not_stated + note is the honest encoding. |
| 6 | MACHINE_MAIN_RING_CIRCUMFERENCE_DIS2026 | uncertainty | type order_of_magnitude | type not_stated, note "about 3(6) km ... not an order-of-magnitude uncertainty" | same as 5 |
| 7 | MACHINE_MAIN_RING_CIRCUMFERENCE_2TEV_DIS2026 | uncertainty | type order_of_magnitude | type not_stated (same note) | same as 5 |
| 8 | ACCEL_BOOSTER_CIRCUMFERENCE_DIS2026 | uncertainty | type order_of_magnitude | type not_stated (same note, 'about 9 km') | same as 5 |
| 9 | MACHINE_MAIN_RING_REVOLUTION_PERIOD_DIS2026 | value | 10.0 us | 10.007 us | derived value stated in the derivation string was rounded in `value`; now the exact 3000 m / c result. |
| 10 | MACHINE_MAIN_RING_REVOLUTION_PERIOD_DIS2026 | uncertainty | type order_of_magnitude | type not_stated, note inherits the unquantified 'about 3 km' | same as 5 |

Not changed, but noted (kept because supported, flagged for the lead):

- SOURCE_PRE_ACCELERATION_TARGET_ENERGY_DIS2026 = 1 GeV is read from "to a GeV energy" (p.4)
  combined with the next paragraph's "from an energy of 1 GeV"; the order_of_magnitude uncertainty
  and confidence medium are appropriate and were left as is. It duplicates
  ACCEL_INJECTION_ENERGY_DIS2026 in substance.
- MACHINE_PEAK_LUMINOSITY_LOWER_BOUND_DIS2026 records a bound ("might exceed 10^34") as value 1e34
  with allowed_range.min = 1e34; the name and notes make the bound nature explicit.
- PHYS_FIG1_XBJ_AXIS_MIN_DIS2026 (x_Bj axis from 10^-7) is a plot-axis edge, not a machine
  parameter; it is supported by Fig. 1 (the LHμC bands do reach the left axis edge) and is
  marked screening_only. Low value, but not fabricated.
- MACHINE_LONG_TERM_SQRT_S_{FCCHH,HELHC}_DIS2026: the reading "30 = FCC-hh, (15) = HE-LHC" follows
  the paper's own "1(2) TeV" / "3(6) km" parenthetical convention; still an interpretation and is
  flagged as such in the records.
- Scenario LHMUC-DIS2026-1TEV lists `crossing_angle` both in `parameters` (pointing to the explicit
  unknown record, value null) and in `unknown_roles`; documented in the scenario notes.
- DET_PILEUP_EXPECTATION_DIS2026 contains an illustrative audit calculation using a placeholder
  100 ub total cross section; it is explicitly labelled as not a source claim.

## Missed quantitative statements

None found. All numbers on pages 1-5 are covered; pages 6-7 are references only. Fig. 2 labels
"RF", "target", "laser", "beam dump", "IP", "LHC beam" carry no numbers.

## Validation

`uv run python tools/validate_yaml.py` -> 0 schema errors for all five files.
`uv run python -m lhmuc validate` -> 2 errors, both outside this document's files
(proposals PROP_A_HNL_2610_28252 and PROP_B_2HDM_VLQ_2610_17801 reference source ids not in
`research/source_registry.yaml`); 0 warnings. `research/source_registry.yaml` still has
`parameters_extracted: []` for SRC_ARXIV_2610_35154 (owner of that file to update).
