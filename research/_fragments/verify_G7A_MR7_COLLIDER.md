# Verification note: group G7A_MR7_COLLIDER (addendum G7, 2026-10-29)

Source: SRC_ARXIV_2510_27437. MuCol Milestone Report No. 7, "Consolidated Parameters" (arXiv:2510.27437v1; document v1.0 Final, released
30/10/2025; page header "Consolidated Parameters Report – November 3, 2025"), 93 pp. Category OFFICIAL_CERN, access uploaded. The printed page
number is the PDF page minus 11 throughout the pages used here. Secondary source for cross-checks only: SRC_WS1681458_SCHULTE_IMCC (D. Schulte,
"Muon Collider", Kraków, Sept 2026, 45 slides, workshop_talk).

Files verified (both are mine; nothing else was edited):

- `parameters/machine/imcc_mr7_collider_reference.yaml`: 357 records at hand-over and 357 after verification. None were added or removed;
  159 were changed (annotations, labels and notes; no value, unit, page, table label or quotation needed correcting).
- `parameters/machine/scenarios_addendum_imcc.yaml`: scenarios IMCC-MR7-10TEV (now 66 roles, 9 unknown) and IMCC-MR7-3TEV (now 30 roles,
  14 unknown).

Role: adversarial verifier. Every record was treated as unverified, including any the killed verifier touched. I rendered the PDF pages with
`pdftoppm` (110–200 dpi; Table A.2 also at 300 dpi) and read every table on the page images: PDF pp. 13, 14, 16, 17, 19, 20, 25, 27,
28, 37, 38, 39, 40, 51, 56, 57, 58, 84 and 89, and Schulte slides 8 and 21. Pure-text pages (MR7 pp. 12, 44, 70; Schulte slides 3, 7, 10,
13, 18, 28, 38, 43) were read in the text layer of the session scratchpad, which was also used to locate passages and for a normalised
verbatim check of every text quotation. The verification scripts are outside the repository, in the session
scratchpad under `g7a/scripts/` (`checks.py`, `chain.py`, `decay.py`, `cells.py`, `values.py`, `apply_edits.py`).

## What was checked and found correct

**All 331 table records (329 printed cells).** I transcribed the eight tables independently from the page images and compared every
record against the transcription by script: cell text at the end of the quotation, numeric value after unit scaling (10^12 and 10^14 counts, 10^34
luminosities, 10^−3 spreads, 10^9 m^−1 s^−1), unit, page and table label. There were 0 mismatches.

| Table (PDF page) | Records | Content |
|---|---|---|
| 1.1 (p. 13) | 16 | 10 TeV baseline: 10 TeV, 10 ab^−1, 18e34, 11.4 km, 14 T, 1363 turns, 1.8e12, 5 Hz, 14.4 MW, 0.025 eVs, 25 µm, 1.5* mm, 1.5* mm, 0.9 µm, 5e14, 5 GeV |
| A.1 (p. 37) | 32 | Stage 1 / Stage 2: 3/10, 1/10, 2.1/18, 4.5/11.4, 11/14, 1039/1363, 2.2/1.8, 5/5, 5.3/14.4, 0.025/0.025, 25/25, 5/1.5, 5/1.5, 3/0.9, 5/5, 5/5 |
| 1.2 (p. 14) | 79 | all 79 printed cells (17 energies, 17 lengths, 9 + 9 emittances, 8 transmissions, 8 cumulatives, 11 μ−/bunch); arrows and '–' get no record |
| 1.3 (p. 14) | 61 | all 59 printed cells (two '7.7 – 8.5' ranges as _MIN/_MAX pairs); the '500 (p+)' cell shares a record with Table 1.2 |
| 6.1 (p. 20) | 22 | 12 spanning cells and 5 relaxed/target pairs, incl. '≈ 10' km, '≈ 27.2' MeV, '.017' ns |
| 6.2 (p. 20) | 14 | 7 thickness / outer-radius pairs, 23.49 … 69 mm |
| 12.2 (p. 28) | 16 | 3 TeV / 10 TeV columns, '5 – 10' years, 139 days, 1.2 × 10^7 s |
| A.2 (p. 40) | 91 | 13 rows × 7 columns, 0.121 GeV … 72 755 m |

**All 26 text records.** Each quotation was compared with the text layer after normalising whitespace, super/subscripts and glyph
variants. The only residual differences are typesetting artefacts that I confirmed on the page images: the σ_E/E fraction in the eq. (A.9)
sentence (3 records) and the display equation (A.2). The Table 6.1 footnotes (p. 19) and the Table 6.2 caption were checked the same way.

**Provenance.** All 357 records are status analogous with applicability analogous; no reported_lhmuc, imported_related, derived_lhmuc or
analytical_estimate record exists (no record holds a value computed by the extractor). Confidence: 348 medium, 9 low (see corrections),
none high. Units parse; no value is null or zero; ids are unique and no other file references them except the scenario file and the lead's
two logs in `research/_fragments/`.

**Cross-references in notes.** Confirmed on the pages: Table 4.1 (p. 17, 'Note: 64 mm = 0.0225 eVs', 22 mm long-rectilinear option);
Table D.5 (p. 51: A-Stage 4 cumulative 49.6, bunch merge 78.0, 38.7 → 11.1 %); Table D.17 (p. 57: 61.4 %); Table D.21 (p. 58: 86 %,
140 m); Table 9.1 (p. 25: collider arc dipole aperture 140 mm, field 14*); Table 11.3 (p. 27: chamber length 10000 m); Table K.3 (p. 84:
circumference 10 000 m, momentum compaction 0, RF voltage 0 MV); Table M.1 (p. 89: MUON Collider Ring 10000 m); Appendix C.1 (p. 44: no
target 'operation temperature, mechanical response and life-time'); Appendix H (p. 70: Nb3Sn 'suitable for ∼ 3 TeV machines'); Schulte
slides 3, 7, 28, 38 (L/IP 1.8 and 17.5 × 10^34) and slide 8 (◦2430 m RLA2, ◦10000 m collider). IR_LSTAR_MR7 exists (6 m).

## Arithmetic, re-done independently

Constants: m_μ = 0.1056584 GeV, τ_μ = 2.19698 µs (cτ_μ = 658.64 m), γ(5 TeV) = 47322.3, γ(1.5 TeV) = 14196.7, γτ_μ(5 TeV) = 0.10397 s.

| Check | Result | Verdict |
|---|---|---|
| P_coll = 2NEf_r | 14.42 MW (10 TeV), 5.287 MW (3 TeV) vs 14.4 / 5.3 | reproduced (pinned test) |
| σ = √(β*ε_n/γ) | 0.890 µm, 2.967 µm vs 0.9 / 3 | reproduced (pinned test) |
| N_turn = γτc/(2C) | 1367.0 (C = 11.4 km), 1038.9 (4.5 km) vs 1363 / 1039; 1558 with C = 10 km | reproduced (pinned test) |
| F_HG(1) = √π e erfc(1) | 0.75787 vs 0.76 (A.1) and 0.758 (Section 6) | reproduced; 0.76 pinned, 0.758 not asserted by the test |
| F_decay eq. (A.7) | 0.25437 (linearised 0.25992) | — |
| eq. (A.9) | 1.891e35 vs 18.8e34 (+0.6 %); linearised 1.932e35; with C = 11.4 km (B_avg 9.19 T) 1.655e35 | reproduced (pinned test) |
| B_avg ↔ C | 10.5 T ↔ C = 9.98 km; Bρ/(10 km/2π) = 10.479 T vs '≈ 10.48' | consistent with the ≈10 km lattice, not 11.4 km |
| L_int/year | 18.8e34 × 1.2e7 s = 2.256 ab^−1 vs '≈ 2.2' (18e34: 2.16) | within 2.6 % (pinned test, 3 %) |
| Years to 10 ab^−1 | 4.55 (one IP), 2.27 (two) vs '∼ 5', '∼ 2.5' | rounded up |
| 200 ms | charge 14.6 % ('about 15%'); luminosity after 200 ms 2.13 % ('2%') | reproduced |
| Table 6.1 geometric L | C = 10 km, F_HG 0.758, linearised F_decay: 5.765e34 / 1.922e35 vs 5.77 / 19.2; exact F_decay 5.64/18.81; C = 11.4 km 5.06/16.86 | reproduced only with 10 km and the linearised factor |
| Lorentz factor | 47322.3 vs 47322 | reproduced |
| Injected power per beam | 7.210 MW vs 7.2 | reproduced |
| ε_l = σ_tσ_E | 0.02502 eVs for both versions vs 0.025 | reproduced |
| σ_z/c | 0.01668 ns, 0.005003 ns vs .017 / 0.005 | reproduced |
| U_0 = C_γ,μ E⁴/ρ | 29.0 MeV (16 T), 25.4 MeV (14 T) vs '≈ 27.2'; 27.2 MeV needs ρ = 1112 m = constant 15.0 T | NOT reproduced |
| RF 30 MV vs U_0 | 30/27.2 = 1.10 | consistent with footnote 4 ('Some margin') |
| Table 6.2 outer radii | running sums 23.50, 53.5, 64.5, 67.5, 68, 69 | reproduced exactly |
| Table 12.2 decay rate 2Nf_r/C | 4.889e9 (3 TeV); 1.579e9 with C = 11.4 km, 1.8e9 with C = 10 km (10 TeV) | 3 TeV reproduced; 10 TeV NOT |
| Table 12.2 e± power (fraction 7/20) | 0.4112 kW/m (3 TeV), 0.4427 kW/m (10 TeV, 11.4 km; 0.505 with 10 km); with 1/3: 0.392 / 0.422 | reproduced with 7/20 (MR7 states no fraction) |
| 139 days | 1.2e7/86400 = 138.9 | reproduced |
| 12 % scaling | 16/14 = 1.143, 11.4/≈10 = 1.14; 12 % needs ≈84 % of C to scale with 1/B | neither reproduced nor refuted |
| Front-end 9 % / 12 % | Table 3.2 at 5 GeV: 1.8e−2 × 5 = 0.09 (μ−), 2.4e−2 × 5 = 0.12 (μ+) | reproduced |
| ε_L 64 mm | m_μc²/c × 64 mm = 22.56 eV ms; MR7: '64 mm = 0.0225 eVs'; 22.9 eV ms ↔ 65.0 mm | Table 1.2 22.9 NOT reproduced |
| ε_L 22 mm | 7.754 eV ms (→ 7.8); MR7 factor 7.734 (→ 7.7); D.17 22.1 mm → 7.79 / 7.77 | 7.7 only with MR7's factor and 22 mm |
| 25.2 eV ms | 1.1 × 22.9 = 25.19; 1.1 × 22.5 = 24.75 | consistent with 22.9 |
| 7.7 – 8.5 | 7.7 × 1.10 = 8.47 | reproduced |
| Table 1.2 cumulative | 8 × 0.9 = 7.20 (printed 7.3); 7.3 × 0.926 = 6.76 (6.7; chain 6.667 ✓); 6.7 × 0.9 = 6.03 (6.1); 6.1 × 0.9 = 5.49 (5.5 ✓); chain 4.86 (4.9 ✓); 4.41 (4.4 ✓) | 7.3 and 6.1 NOT reproduced by any reading |
| Table 1.2 μ−/bunch | 45 × printed cumulative: 3.285, 3.015, 2.745, 2.475, 2.205; 45 × 4.4 % × 0.9 = 1.782 | all reproduced (from the printed cumulative) |
| Table 1.3 cumulative | chain 95.0, 47.12, 36.754, 10.51, 6.454, 5.551, 4.996 → all reproduced; RLA2–RCS4: 4.63, 4.16, 3.75, 3.37, 3.03 vs printed 6.7, 6.1, 5.5, 4.9, 4.4 | first 8 reproduced (36.8 and 6.5 only from the unrounded chain); last 5 NOT (Table 1.2 values copied) |
| Table 1.3 μ−/bunch | 42.75, 21.20, 16.54, 4.730, 2.904, 2.498, 2.248, 2.082, 1.873, 1.686, 1.517, 1.517, 1.366, 1.366 | all 15 reproduced |
| Table 1.3 Rect B 28.6 | Π(B-Stage 1–10 of D.5) = 28.63 %; 11.1/38.7 = 28.68 % | reproduced by the product, not by the ratio |
| Table A.2 per-system T | exp(−∫ds/(βγcτ)) with kinetic energy linear along length × turns: 90.52, 80.33, 70.60, 86.16, 77.64, 89.67, 81.51, 92.64, 90.05, 89.99, 90.06, 89.92, 72.55 | all within 0.16 pp; 8 of 13 to the printed digit; total-energy reading fails (FE 80.3 %, FC undefined) |
| Table A.2 cumulative | product of printed T: 90.50, 72.67, 51.31, 44.12, 34.20, 30.67, 25.00, 23.15, 20.83, 18.75, 16.88, 15.19, 11.03 | within 0.1 pp; 44.2, 23.2, 20.9 differ at the printed digit |
| Table A.2 total length | running sum of lengths reproduced exactly (72 755 m); Σ length × turns = 13 078 860 m | column ≠ text's definition |
| 1000 collider turns | 1e7 m / c = 33.4 ms = 0.32 γτ_μ, vs the 200 ms fill period | not the store length |

## Validation labels

- **P1 (12 records)**, each now naming a test that checks exactly its printed value; I ran the file (8 passed):
  - `test_mr7_beam_power_is_two_n_e_fr`: MACHINE_BEAM_POWER_10TEV_MR7, MACHINE_BEAM_POWER_3TEV_MR7, MACHINE_BEAM_POWER_10TEV_TABA1_MR7;
  - `test_mr7_ip_beam_size_from_emittance_and_beta_star`: IR_SIGMA_IP_10TEV_MR7, IR_SIGMA_IP_3TEV_MR7, IR_SIGMA_IP_10TEV_TABA1_MR7;
  - `test_mr7_luminosity_lifetime_in_turns`: MACHINE_LUMINOSITY_LIFETIME_TURNS_10TEV_MR7, _3TEV_MR7, _10TEV_TABA1_MR7;
  - `test_mr7_hourglass_factor_for_beta_star_equal_bunch_length`: MACHINE_HOURGLASS_FACTOR_BETA_EQ_SIGMAZ_MR7 (0.76);
  - `test_mr7_analytic_luminosity_eq_a9`: MACHINE_LUMINOSITY_ANALYTIC_10TEV_MR7 (18.8e34);
  - `test_mr7_integrated_luminosity_per_year`: MACHINE_INT_LUMI_PER_YEAR_10TEV_MR7 (2.2 ab^−1).
- **Deliberately kept P0** although a test touches the quantity: MACHINE_HOURGLASS_FACTOR_10TEV_MR7 (0.758; the test asserts 0.76 ± 0.005),
  MACHINE_AVG_DIPOLE_FIELD_LUMI_FORMULA_10TEV_MR7 (10.5 T is an input of the A.9 test, which pins only the implied 9.98 km),
  MACHINE_INJECTED_BEAM_POWER_PER_BEAM_TAB61_MR7 (7.2 MW per beam is not asserted). `test_mr7_decay_factor_eq_a7_at_10_tev` checks
  F_decay = 0.254, which MR7 does not print and no record holds.
- **P0 (345 records).** For every record whose validation.methods or notes carried generator arithmetic (all 113 records the lead lowered
  from P1, plus the 10 records with the extractor's "not reproduced" notes; a script confirms none is left without a verifier note) I recomputed it and appended "Verifier 2026-10-29: …" to validation.notes, saying
  whether it really reproduces the printed digit. The extractor's method lines were kept; where its ±0.11 pp or ±0.18 tolerance had hidden a
  last-digit mismatch the note now says NOT reproduced.
- Scenario labels stay P0 (`tools/apply_scenario_levels.py --check`: 0 excess labels).

## Corrections made

No parameter_id, value, unit, page, table label or quotation was wrong; all corrections are to labels, annotations and scenario roles.

1. **P0 → P1 for the 12 records above** (validation.methods gained the test path).
2. **Confidence medium → low for 9 records whose printed value contradicts MR7 itself:**
   - MACHINE_ENERGY_LOSS_PER_TURN_TAB61_MR7 (≈ 27.2 MeV; its own footnote assumption, constant 16 T, gives 29.0 MeV; 27.2 needs 15.0 T);
   - MACHINE_RAD_STUDY_DECAY_RATE_PER_M_10TEV_MR7 (1.8e9 /m/s needs C = 10 km; its column says 11.4 km and its e± power uses 11.4 km);
   - MACHINE_CHAIN_FINAL_COOLING_TARGET_EPS_L_MR7, MACHINE_CHAIN_PRE_ACC_TARGET_EPS_L_MR7 (22.9 eV ms vs MR7's own '64 mm = 0.0225 eVs');
   - MACHINE_CHAIN_{RLA2,RCS1,RCS2,RCS3,RCS4}_EST_CUM_TRANSMISSION_MR7 (Table 1.2 target values copied into the estimate column; the
     estimated chain gives 4.63, 4.16, 3.75, 3.37, 3.03 %).
3. **Extractor arithmetic error fixed** in the shared note of the five Table 1.3 RLA2–RCS4 records: "5.0 × 0.926 × 0.9^n would give …,
   3.4, 3.1" → "…, 3.4, 3.0" (4.63 × 0.9^4 = 3.04).
4. **Unsupported claim removed**: MACHINE_DECAY_COLLIDER_TURNS_MR7 said "1000 turns in the collider is the store length assumed for the
   decay estimate". MR7 says no such thing; 1000 turns of 10 km last 33 ms, against a 200 ms fill. The note now says so, and
   MACHINE_DECAY_COLLIDER_CUM_TRANSMISSION_MR7 notes that its 11 % is after 1000 turns.
5. **Over-claimed reproductions corrected in validation.notes** (methods text kept): Table 1.2 cumulative 7.3 (8 × 0.9 = 7.2) and 6.1
   (6.7 × 0.9 = 6.03) are NOT reproduced; 6.7 only from the unrounded chain, not from the printed 7.3; Table 1.3 36.8 and 6.5 only from the
   unrounded chain (printed predecessors give 36.7 and 6.4); Table 1.3 Rect B 28.6 comes from the product of the D.5 stage transmissions
   (28.63 %), not from 11.1/38.7 (28.68 % → 28.7); Table 1.3 7.7 eV ms only with MR7's own 64 mm = 0.0225 eVs factor (physical
   conversion of 22 mm gives 7.75 → 7.8); MACHINE_ARC_FIELD_14T_SCALING_MR7 rephrased from "Not reproduced" to "neither reproduced nor
   refuted" (12 % follows if ≈84 % of C scales with the field).
6. **Circumference notes made precise** (MACHINE_COLLIDER_CIRCUMFERENCE_10TEV_MR7 and _TABA1): Table 11.3 gives a chamber length, Table
   M.1 the collider-ring tunnel length; Table 1.2 ◦11400 and Schulte slide 8 ◦10000 added; which derived numbers fit 11.4 vs 10 km.
7. **Conflict notes added** (preserved, not averaged): Schulte 2026 L/IP 17.5e34 vs MR7 18e34 (10 TeV, both records); Schulte slide 8
   target 4.0e12 / achieved 2.8e12 after the pre-accelerator vs MR7 3.6e12 / 2.5e12 (4 records); achieved 1.5e12 vs 1.4e12 at the 10 TeV
   collider and 1.7e12 vs 1.5e12 at 3 TeV; Table A.2 vs Table 1.2 front-end (0.200 vs 0.17 GeV) and Rectilinear A (0.162 vs 0.2 GeV) output
   energies (4 records); MR7 p. 16 "339 MeV/c momentum which is 250 MeV kinetic energy" added to the Pre-Acc energy record and the Table
   4.1 mean p_z of 288 MeV/c (kinetic 201 MeV) to the Charge Sep. energy record (both support the extractor's kinetic-energy reading).
8. **applicability.explanation** of the 24 text records replaced: the generic "statement in the MR7 text" now names the section and its
   caveats (Section 1 'ideal design specifications'; Appendix A.1 'roughly estimated analytically', 'No crossing angle', 'Ignoring the
   beam-beam enhancement', beam removed at injection, GUINEA-PIG 'full model is being developed'; Section 6 'extrapolations from lower
   energy', 16 T lattice). The 0.76 hourglass record now says it is a general β* = σ_z result applicable to both stages.
9. **File headers** of both files gained a verification paragraph; the extractor's validation paragraph is marked as superseded.

## Scenarios

A script resolved every role to its record and I checked that each record holds the quantity the role names.

- **IMCC-MR7-10TEV**: `cooling_output_emittance_transverse` / `_longitudinal` pointed to the short-rectilinear Table D.13 output
  (0.0224 mm, 42.68 mm), an alternative staging that the MR7 chain tables do not use (Table 1.3 uses the long-rectilinear B10 option:
  28.6 % = Π D.5, 61.4 % = D.17, 7.7 eV ms = 22 mm). Re-pointed to the Table 1.2 targets (MACHINE_CHAIN_FINAL_COOLING_TARGET_EPS_T/L_MR7) and
  added `cooling_output_emittance_transverse_estimated` / `_longitudinal_estimated` (Table 1.3). Role `decay_only_transmission_to_end_of_store`
  renamed `decay_only_cumulative_transmission_1000_collider_turns` (same record). Notes rewritten: which roles are P1, which are reproduced,
  which belong to the ≈10 km / 16 T lattice, the conflicts, and the basis of each unknown role.
- **IMCC-MR7-3TEV**: `hourglass_factor` mapped to MACHINE_HOURGLASS_FACTOR_BETA_EQ_SIGMAZ_MR7 (MR7's general statement for β* = σ_z; Table
  A.1 Stage 1 has 5 mm = 5 mm) and removed from unknown_roles; status reported → partially_reported (MR7 "only considers the final
  product"; 14 roles unknown); description and notes updated (Table 6.2 caption, "For the 3 TeV parameters the disruption is higher").
- **Unknown roles re-searched** in the MR7 text layer and the Schulte deck: peak luminosity, crossing angle (A.1 analytic estimate only
  assumes "No crossing angle"), collision rate and revolution period (derivable from C, not printed), polarisation, beam-beam tune shift
  (only "disruption parameter is of the order of 1"), energy acceptance (Schulte slide 18: "not yet full target energy acceptance", no
  number), target temperature and lifetime (App. C.1 says none are listed); for 3 TeV additionally geometric luminosity, energy spread
  (derivable, 0.1 %), L*, U_0, RF voltage, L_int/year (Schulte gives an accumulation time only), wall-plug power and cost (Schulte slides
  20-21 only for the 3.2 TeV CERN-site variant). All confirmed absent.
- Roles pointing to other G7 files (proton driver/target/cooling, magnets/RF/power, Schulte) and to the committed acceleration and MDI files
  resolve at the time of writing; the other three G7 verifiers work in parallel, so a rename there would break a role (see residual doubts).

## Added

None. Statements left without a record: "For the 3 TeV parameters the disruption is higher" (qualitative); the A.1 assumption list (quoted
in the explanations instead); Fig. A.1 (a plot, not read); Section 7 detector dimensions (detector scope).

## Removed

None. Every record is supported by the cited page; no value was invented, read from a plot, rounded beyond the printed precision or taken
from the wrong stage, table or column.

## Conflict candidates for the lead (not added to research/source_conflicts.yaml, which is not my file)

1. 10 TeV collider circumference: 11.4 km (Tables 1.1, A.1, 12.2; ◦11400 m Table 1.2) vs ≈ 10 km (Table 6.1, Section 6) vs 10 000 m
   (Tables A.2, 11.3, K.3, M.1; Schulte slide 8). The Table 6.1 geometric luminosities, the A.9 analytic estimate (B_avg 10.5 T) and the
   Table 12.2 10 TeV decay rate are computed for ≈10 km.
2. 10 TeV luminosity: MR7 18e34 (Tables 1.1, A.1; eq. A.4 1.8e35) vs Schulte 2026 L/IP 17.5e34.
3. 3 TeV luminosity: MR7 2.1e34 vs Schulte 2026 L/IP 1.8e34.
4. μ−/bunch chain: MR7 Table 1.2/1.3 vs Schulte slide 8 (pre-acc target 3.6 vs 4.0, estimated 2.5 vs achieved 2.8; collider 1.4 vs 1.5 at
   10 TeV, 1.5 vs 1.7 at 3 TeV, all × 10^12).
5. Cooling-output target ε_L: Table 1.2 22.9 eV ms vs Table 4.1 64 mm = 0.0225 eVs.
6. Table 1.3 cumulative estimated transmission RLA2–RCS4 (copies of Table 1.2).
7. Energy loss per turn: printed ≈ 27.2 MeV vs 29.0 MeV for the footnote's constant 16 T.
8. Table A.2 vs Table 1.2 per-system lengths and energies (Rect B 487 vs 424 m, Pre-Acc 245 vs 140 m, RLA1 800 vs ◦500 m, RLA2 2430 vs
   ◦2400 m; front-end out 0.200 vs 0.17 GeV, Rect A out 0.162 vs 0.2 GeV).

Per research/source_quality_policy.md §4, once items 1–4 are recorded without a decided treatment, the competing records drop to low.

## Residual doubts

- How Table 1.1's 18e34 at 11.4 km was obtained cannot be reconstructed: the A.1 chain (GUINEA-PIG 1.86e35, adopted 1.8e35, analytic
  18.8e34) states no circumference, and its analytic input B_avg = 10.5 T implies ≈10 km; eq. (A.9) at 11.4 km gives 16.5e34 before
  beam-beam enhancement (up to 24 %).
- MACHINE_HOURGLASS_FACTOR_10TEV_MR7 (0.758) stays P0 only because the pinned test asserts 0.76; one extra assertion at 0.758 ± 0.0005
  would promote it. The same holds for MACHINE_INJECTED_BEAM_POWER_PER_BEAM_TAB61_MR7 (7.2 MW) and the Table 6.1 geometric luminosities.
- The e± energy fraction 7/20 used to reproduce Table 12.2's power per metre is my assumption; MR7 does not state it (the Schulte deck says
  "1/3", which does not reproduce the table).
- Table A.2's per-system transmissions for FC, Pre-Acc and the RCS rows agree only to 0.05–0.16 pp; MR7 may have used a slightly different
  energy ramp or lifetime constant.
- The 3 TeV hourglass mapping applies MR7's general β* = σ_z statement to Stage 1; MR7 prints no stage-specific value.
- The 3 TeV status change (reported → partially_reported) and the cooling-role re-pointing are judgement calls; both are documented in the
  scenario notes.
- The parallel G7B note (research/_fragments/verify_G7B_MR7_SOURCE.md) says this scenario file points to five of its records; after my
  re-pointing of the cooling roles it points to three (SOURCE_PD_LINAC_BEAM_POWER_5GEV_MR7, SOURCE_TARGET_MATERIAL_BASELINE_MR7,
  SOURCE_FE_OUTGOING_MUMINUS_YIELD_MR7); SOURCE_COOLING_FINAL_FROM_B8_OUT_EPS_T/L_MR7 are no longer referenced.
- Roles that point into the three other G7 files (12 role entries, e.g. SOURCE_PD_LINAC_BEAM_POWER_5GEV_MR7, MACHINE_IMPEDANCE_*_MR7,
  ACC_RF_RCS_GF_ALL_AVG_WALL_PLUG_POWER_MR7, the three Schulte roles) depend on those verifiers keeping the ids; `uv run python -m lhmuc
  validate` must be re-run after all four G7 verifiers finish.

## Checks run

- `uv run python tools/validate_yaml.py provenance parameters/machine/imcc_mr7_collider_reference.yaml`: 0 schema errors.
- `uv run python tools/validate_yaml.py machine parameters/machine/scenarios_addendum_imcc.yaml`: 0 schema errors.
- `uv run python -m lhmuc validate`: 0 errors, 0 warnings.
- `uv run python tools/apply_scenario_levels.py --check parameters/machine/scenarios_addendum_imcc.yaml`: 0 excess labels.
- `uv run pytest tests/scientific/test_imcc_mr7_reference.py`: 8 passed. Full suite: all pass except test_csv_registries_in_sync and
  test_source_parameters_extracted_in_sync, which need the lead's `tools/build_registries.py` and `tools/sync_parameters_extracted.py`
  (registries/ and the source registry are not my files).
- Field-level diff against the hand-over file: 159 records changed (validation.notes 133, notes 31, applicability.explanation 24,
  validation.level 12, validation.methods 12, confidence 9); values, units and source blocks of all 357 records byte-identical after parsing.

## Appendix: every changed record, by field

Generated by script from the field-level diff against the hand-over file (ids in file order). The text of each change is in the
record itself; arithmetic additions start with "Verifier 2026-10-29:".

- **validation.level** (12): MACHINE_LUMINOSITY_LIFETIME_TURNS_10TEV_MR7, MACHINE_LUMINOSITY_LIFETIME_TURNS_3TEV_MR7, MACHINE_LUMINOSITY_LIFETIME_TURNS_10TEV_TABA1_MR7, MACHINE_BEAM_POWER_10TEV_MR7, MACHINE_BEAM_POWER_3TEV_MR7, MACHINE_BEAM_POWER_10TEV_TABA1_MR7, IR_SIGMA_IP_10TEV_MR7, IR_SIGMA_IP_3TEV_MR7, IR_SIGMA_IP_10TEV_TABA1_MR7, MACHINE_HOURGLASS_FACTOR_BETA_EQ_SIGMAZ_MR7, MACHINE_LUMINOSITY_ANALYTIC_10TEV_MR7, MACHINE_INT_LUMI_PER_YEAR_10TEV_MR7.
- **validation.methods** (12): MACHINE_LUMINOSITY_LIFETIME_TURNS_10TEV_MR7, MACHINE_LUMINOSITY_LIFETIME_TURNS_3TEV_MR7, MACHINE_LUMINOSITY_LIFETIME_TURNS_10TEV_TABA1_MR7, MACHINE_BEAM_POWER_10TEV_MR7, MACHINE_BEAM_POWER_3TEV_MR7, MACHINE_BEAM_POWER_10TEV_TABA1_MR7, IR_SIGMA_IP_10TEV_MR7, IR_SIGMA_IP_3TEV_MR7, IR_SIGMA_IP_10TEV_TABA1_MR7, MACHINE_HOURGLASS_FACTOR_BETA_EQ_SIGMAZ_MR7, MACHINE_LUMINOSITY_ANALYTIC_10TEV_MR7, MACHINE_INT_LUMI_PER_YEAR_10TEV_MR7.
- **provenance.confidence** (9): MACHINE_CHAIN_FINAL_COOLING_TARGET_EPS_L_MR7, MACHINE_CHAIN_PRE_ACC_TARGET_EPS_L_MR7, MACHINE_CHAIN_RLA2_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS1_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS2_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS3_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS4_EST_CUM_TRANSMISSION_MR7, MACHINE_ENERGY_LOSS_PER_TURN_TAB61_MR7, MACHINE_RAD_STUDY_DECAY_RATE_PER_M_10TEV_MR7.
- **notes** (31): MACHINE_ESTIMATED_LUMINOSITY_10TEV_MR7, MACHINE_ESTIMATED_LUMINOSITY_10TEV_TABA1_MR7, MACHINE_COLLIDER_CIRCUMFERENCE_10TEV_MR7, MACHINE_COLLIDER_CIRCUMFERENCE_10TEV_TABA1_MR7, MACHINE_EST_MU_CHARGE_AFTER_COOLING_MR7, MACHINE_REQUIRED_MU_CHARGE_AFTER_COOLING_MR7, MACHINE_CHAIN_FRONT_END_ENERGY_OUT_MR7, MACHINE_CHAIN_CHARGE_SEP_ENERGY_OUT_MR7, MACHINE_CHAIN_RECT_A_ENERGY_OUT_MR7, MACHINE_CHAIN_PRE_ACC_ENERGY_OUT_MR7, MACHINE_CHAIN_FINAL_COOLING_TARGET_EPS_L_MR7, MACHINE_CHAIN_PRE_ACC_TARGET_EPS_L_MR7, MACHINE_CHAIN_PRE_ACC_TARGET_MU_PER_BUNCH_MR7, MACHINE_CHAIN_BUNCH_MERGE_T13_TRANSMISSION_MR7, MACHINE_CHAIN_PRE_ACC_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RLA2_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS1_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS2_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS3_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_COLLIDER_3TEV_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RCS4_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_COLLIDER_10TEV_EST_MU_PER_BUNCH_MR7, MACHINE_DECAY_FRONT_END_ENERGY_OUT_MR7, MACHINE_DECAY_RECT_A_ENERGY_OUT_MR7, MACHINE_DECAY_COLLIDER_LENGTH_MR7, MACHINE_DECAY_COLLIDER_TURNS_MR7, MACHINE_DECAY_COLLIDER_CUM_TRANSMISSION_MR7, MACHINE_RUN_TIME_PER_YEAR_LUMI_MR7, MACHINE_NUMBER_OF_EXPERIMENTS_10TEV_MR7, MACHINE_ENERGY_LOSS_PER_TURN_TAB61_MR7, MACHINE_RAD_STUDY_DECAY_RATE_PER_M_10TEV_MR7.
- **provenance.applicability.explanation** (24): PHYS_EQUIVALENT_FCCHH_ENERGY_MR7, MACHINE_ARC_FIELD_14T_SCALING_MR7, MACHINE_EST_MU_CHARGE_AFTER_COOLING_MR7, MACHINE_REQUIRED_MU_CHARGE_AFTER_COOLING_MR7, MACHINE_LONG_EMITTANCE_TARGET_POLICY_MR7, MACHINE_CHARGE_REMAINING_AFTER_200MS_10TEV_MR7, MACHINE_INT_LUMI_FRACTION_AFTER_200MS_10TEV_MR7, MACHINE_HOURGLASS_FACTOR_BETA_EQ_SIGMAZ_MR7, MACHINE_DISRUPTION_PARAMETER_ORDER_10TEV_MR7, MACHINE_GP_LONG_DISTRIBUTION_RADIUS_MR7, MACHINE_BEAM_BEAM_ENHANCEMENT_MAX_10TEV_MR7, MACHINE_LUMINOSITY_GUINEAPIG_10TEV_MR7, MACHINE_LUMINOSITY_ADOPTED_10TEV_MR7, MACHINE_LUMINOSITY_ANALYTIC_10TEV_MR7, MACHINE_AVG_DIPOLE_FIELD_LUMI_FORMULA_10TEV_MR7, MACHINE_ENERGY_SPREAD_LUMI_FORMULA_10TEV_MR7, MACHINE_RUN_TIME_PER_YEAR_LUMI_MR7, MACHINE_INT_LUMI_PER_YEAR_10TEV_MR7, MACHINE_YEARS_TO_10ABINV_ONE_IP_MR7, MACHINE_YEARS_TO_10ABINV_TWO_IPS_MR7, MACHINE_NUMBER_OF_EXPERIMENTS_10TEV_MR7, MACHINE_HOURGLASS_FACTOR_10TEV_MR7, MACHINE_AVG_BENDING_FIELD_SEC6_10TEV_MR7, MACHINE_LATTICE_ARC_PEAK_FIELD_ASSUMED_MR7.
- **validation.notes** (133): MACHINE_LUMINOSITY_LIFETIME_TURNS_10TEV_MR7, MACHINE_LUMINOSITY_LIFETIME_TURNS_3TEV_MR7, MACHINE_LUMINOSITY_LIFETIME_TURNS_10TEV_TABA1_MR7, MACHINE_BEAM_POWER_10TEV_MR7, MACHINE_BEAM_POWER_3TEV_MR7, MACHINE_BEAM_POWER_10TEV_TABA1_MR7, IR_SIGMA_IP_10TEV_MR7, IR_SIGMA_IP_3TEV_MR7, IR_SIGMA_IP_10TEV_TABA1_MR7, MACHINE_ARC_FIELD_14T_SCALING_MR7, MACHINE_CHAIN_FINAL_COOLING_TARGET_EPS_L_MR7, MACHINE_CHAIN_PRE_ACC_TARGET_EPS_L_MR7, MACHINE_CHAIN_RCS4_TARGET_EPS_L_MR7, MACHINE_CHAIN_COLLIDER_10TEV_TARGET_EPS_L_MR7, MACHINE_CHAIN_FINAL_COOLING_EST_EPS_L_MR7, MACHINE_CHAIN_PRE_ACC_EST_EPS_L_MR7, MACHINE_CHAIN_RCS4_EST_EPS_L_MAX_MR7, MACHINE_CHAIN_COLLIDER_10TEV_EST_EPS_L_MAX_MR7, MACHINE_CHAIN_FRONT_END_TARGET_TRANSMISSION_MR7, MACHINE_CHAIN_FRONT_END_TARGET_MU_PER_BUNCH_MR7, MACHINE_CHAIN_PRE_ACC_TARGET_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_PRE_ACC_TARGET_MU_PER_BUNCH_MR7, MACHINE_CHAIN_LINAC_RLA1_TARGET_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_LINAC_RLA1_TARGET_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RLA2_TARGET_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RLA2_TARGET_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RCS1_TARGET_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS1_TARGET_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RCS2_TARGET_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS2_TARGET_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RCS3_TARGET_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS3_TARGET_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RCS4_TARGET_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS4_TARGET_MU_PER_BUNCH_MR7, MACHINE_CHAIN_FRONT_END_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_CHARGE_SEP_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_CHARGE_SEP_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RECT_A_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RECT_A_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_BUNCH_MERGE_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_BUNCH_MERGE_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RECT_B_T13_TRANSMISSION_MR7, MACHINE_CHAIN_RECT_B_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RECT_B_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_FINAL_COOLING_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_FINAL_COOLING_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_PRE_ACC_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_PRE_ACC_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_LINAC_RLA1_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_LINAC_RLA1_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RLA2_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RLA2_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RCS1_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS1_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RCS2_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS2_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RCS3_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS3_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_COLLIDER_3TEV_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_RCS4_EST_CUM_TRANSMISSION_MR7, MACHINE_CHAIN_RCS4_EST_MU_PER_BUNCH_MR7, MACHINE_CHAIN_COLLIDER_10TEV_EST_MU_PER_BUNCH_MR7, MACHINE_DECAY_FRONT_END_TRANSMISSION_MR7, MACHINE_DECAY_FRONT_END_CUM_TRANSMISSION_MR7, MACHINE_DECAY_FRONT_END_TOTAL_LENGTH_MR7, MACHINE_DECAY_RECT_A_TRANSMISSION_MR7, MACHINE_DECAY_RECT_A_CUM_TRANSMISSION_MR7, MACHINE_DECAY_RECT_A_TOTAL_LENGTH_MR7, MACHINE_DECAY_RECT_B_TRANSMISSION_MR7, MACHINE_DECAY_RECT_B_CUM_TRANSMISSION_MR7, MACHINE_DECAY_RECT_B_TOTAL_LENGTH_MR7, MACHINE_DECAY_FINAL_COOLING_TRANSMISSION_MR7, MACHINE_DECAY_FINAL_COOLING_CUM_TRANSMISSION_MR7, MACHINE_DECAY_FINAL_COOLING_TOTAL_LENGTH_MR7, MACHINE_DECAY_PRE_ACC_TRANSMISSION_MR7, MACHINE_DECAY_PRE_ACC_CUM_TRANSMISSION_MR7, MACHINE_DECAY_PRE_ACC_TOTAL_LENGTH_MR7, MACHINE_DECAY_LINAC_TRANSMISSION_MR7, MACHINE_DECAY_LINAC_CUM_TRANSMISSION_MR7, MACHINE_DECAY_LINAC_TOTAL_LENGTH_MR7, MACHINE_DECAY_RLA1_TRANSMISSION_MR7, MACHINE_DECAY_RLA1_CUM_TRANSMISSION_MR7, MACHINE_DECAY_RLA1_TOTAL_LENGTH_MR7, MACHINE_DECAY_RLA2_TRANSMISSION_MR7, MACHINE_DECAY_RLA2_CUM_TRANSMISSION_MR7, MACHINE_DECAY_RLA2_TOTAL_LENGTH_MR7, MACHINE_DECAY_RCS1_TRANSMISSION_MR7, MACHINE_DECAY_RCS1_CUM_TRANSMISSION_MR7, MACHINE_DECAY_RCS1_TOTAL_LENGTH_MR7, MACHINE_DECAY_RCS2_TRANSMISSION_MR7, MACHINE_DECAY_RCS2_CUM_TRANSMISSION_MR7, MACHINE_DECAY_RCS2_TOTAL_LENGTH_MR7, MACHINE_DECAY_RCS3_TRANSMISSION_MR7, MACHINE_DECAY_RCS3_CUM_TRANSMISSION_MR7, MACHINE_DECAY_RCS3_TOTAL_LENGTH_MR7, MACHINE_DECAY_RCS4_TRANSMISSION_MR7, MACHINE_DECAY_RCS4_CUM_TRANSMISSION_MR7, MACHINE_DECAY_RCS4_TOTAL_LENGTH_MR7, MACHINE_DECAY_COLLIDER_TRANSMISSION_MR7, MACHINE_DECAY_COLLIDER_CUM_TRANSMISSION_MR7, MACHINE_DECAY_COLLIDER_TOTAL_LENGTH_MR7, MACHINE_CHARGE_REMAINING_AFTER_200MS_10TEV_MR7, MACHINE_INT_LUMI_FRACTION_AFTER_200MS_10TEV_MR7, MACHINE_HOURGLASS_FACTOR_BETA_EQ_SIGMAZ_MR7, MACHINE_LUMINOSITY_ANALYTIC_10TEV_MR7, MACHINE_AVG_DIPOLE_FIELD_LUMI_FORMULA_10TEV_MR7, MACHINE_INT_LUMI_PER_YEAR_10TEV_MR7, MACHINE_YEARS_TO_10ABINV_ONE_IP_MR7, MACHINE_YEARS_TO_10ABINV_TWO_IPS_MR7, MACHINE_HOURGLASS_FACTOR_10TEV_MR7, MACHINE_AVG_BENDING_FIELD_SEC6_10TEV_MR7, MACHINE_LORENTZ_FACTOR_TAB61_MR7, MACHINE_INJECTED_BEAM_POWER_PER_BEAM_TAB61_MR7, MACHINE_LONG_EMITTANCE_TAB61_MR7, MACHINE_ENERGY_LOSS_PER_TURN_TAB61_MR7, MACHINE_INTEGRATED_RF_VOLTAGE_TAB61_MR7, MACHINE_GEOMETRIC_LUMINOSITY_RELAXED_TAB61_MR7, MACHINE_GEOMETRIC_LUMINOSITY_TARGET_TAB61_MR7, MACHINE_BUNCH_LENGTH_TIME_RELAXED_TAB61_MR7, MACHINE_BUNCH_LENGTH_TIME_TARGET_TAB61_MR7, MACHINE_ARC_DIPOLE_COPPER_COATING_OUTER_RADIUS_MR7, MACHINE_ARC_DIPOLE_TUNGSTEN_ABSORBER_OUTER_RADIUS_MR7, MACHINE_ARC_DIPOLE_SUPPORT_INSULATION_OUTER_RADIUS_MR7, MACHINE_ARC_DIPOLE_COLD_BORE_OUTER_RADIUS_MR7, MACHINE_ARC_DIPOLE_KAPTON_INSULATION_OUTER_RADIUS_MR7, MACHINE_ARC_DIPOLE_COIL_CLEARANCE_OUTER_RADIUS_MR7, MACHINE_RAD_STUDY_PARTICLE_ENERGY_3TEV_MR7, MACHINE_RAD_STUDY_PARTICLE_ENERGY_10TEV_MR7, MACHINE_RAD_STUDY_DECAY_RATE_PER_M_3TEV_MR7, MACHINE_RAD_STUDY_DECAY_RATE_PER_M_10TEV_MR7, MACHINE_RAD_STUDY_EPM_POWER_PER_M_3TEV_MR7, MACHINE_RAD_STUDY_EPM_POWER_PER_M_10TEV_MR7, MACHINE_RAD_STUDY_OPERATION_DAYS_PER_YEAR_MR7.
