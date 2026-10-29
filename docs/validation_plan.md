# LHμC-VirtualLab — Validation plan

**Document date:** 2026-10-28 · **Project phase:** Phase 0 (evidence and feasibility audit) ·
**Owner:** David Hausler · **Status:** describes the validation ladder, the checks that exist on
2026-10-28, and the benchmarks planned for later milestones. Every planned item is marked
*planned*; nothing here claims a validation that has not been run.

Binding rules: `CLAUDE.md` §1.7 (fidelity G-labels and validation P-labels are independent),
§1.8 (tools, not the LLM, do the science), §1.9 (never weaken a failing scientific test without
an investigated, documented reason), §1.10 (stop and report when a benchmark cannot be reproduced).
Companion documents: `docs/architecture.md`, `docs/uncertainty_policy.md`.

---

## 1. The validation ladder P0–P5

The `validation_level` enum lives in `schemas/provenance.schema.json#/$defs/validation_level`
and is referenced by every parameter record, scenario, component, simulation run and
optimization record. A level is earned per object or per result, never per module, and a
P-label never changes the geometry G-label (`G0`–`G5`) of the same object.

| Level | Meaning (schema wording) | Entry criterion — what must exist and be recorded before the label may be used | Who/what grants it |
|---|---|---|---|
| **P0** | unverified | default for every new record, model, geometry or result; a published number copied with provenance is still P0 until a check has been run on it | automatic |
| **P1** | dimensional / analytical checks | the value (a) parses through `lhmuc/units.py` and (b) is reproduced, or shown consistent, by a closed-form relation whose inputs are themselves registry parameters, implemented in code under `tests/scientific/` with a stated, justified tolerance; the test passes in CI and the check is listed in `registries/validation_registry.csv` | pytest run, recorded check row |
| **P2** | published benchmark reproduced | a result of a documented computation (optics code, transport code, generator, luminosity code) reproduces a number published by an identified source (`source_id`, page, quotation) within a tolerance stated *before* the run; software versions, seeds and inputs recorded in an immutable run record (`schemas/simulation_run.schema.json`) | run record + check row, human review |
| **P3** | cross-checked with another code | the same quantity computed by two independent codes (e.g. MAD-X vs Xsuite, Geant4 vs BDSIM, two generators) agrees within a stated tolerance; disagreements are investigated and written down, not averaged | two run records + check row |
| **P4** | calibrated on prototype / beam data | measured data from a real device of the same kind (e.g. J-PARC ultra-cold μ⁺ source, LHC proton beam parameters, HL-LHC magnets, IMCC nozzle tests) are compared with the model, with the dataset archived in `references/` and its licence recorded | dataset + calibration record under `uncertainty/calibration/` |
| **P5** | calibrated on LHμC operations | requires an operating LHμC; **unreachable** for this project in any foreseeable milestone and must never appear in the repository except in this table | — |

Rules:

1. A level is claimed only for the specific quantity and scenario the check covers. A P1 check of
   √s does not make the luminosity P1.
   Since 2026-10-29 `uv run python -m lhmuc validate` rejects a P1 label whose `validation.methods` or
   `check_ids` name no existing `test_*` function under `tests/`. Arithmetic written in `validation.methods` of a P0
   record is a candidate check, not a level; it becomes P1 when the test exists. `tools/apply_validation_levels.py`
   lowered 327 committed P1 labels that had no test (list: `research/_fragments/validation_levels_lowered_2026-10-29.csv`).
2. The highest level a *synthetic* input (`provenance.status: synthetic`) can confer on a derived
   result is P1; results that depend on a synthetic input must display the assumption id.
3. The label displayed for a composite result is the **minimum** over its inputs and its own check.
4. A failing check sets the level back to P0 and opens an entry in `registries/risk_register.csv`
   (authored) until resolved.

---

## 2. What is implemented on 2026-10-28 (Phase 0, P1 only)

The only validation code present is `lhmuc/analytical.py` (closed-form audit arithmetic,
constants from PDG 2024 as stated in its docstring) and the tests in
`tests/scientific/test_analytical_checks.py`. `uv run pytest tests/scientific -v` on 2026-10-28
collects **15 tests (13 functions, `test_sqrt_s` parametrised ×3) and all 15 pass**. These are
checks of the *internal consistency* of the numbers printed in the uploaded documents, not a
beam-physics model, and they confer at most P1 on the parameters they touch.

Inputs come from `SRC_ARXIV_2610_35154` (Piotrzkowski, LHμC, PoS DIS2026, arXiv:2610.35154v1,
`PRIMARY_LHMUC`) and `SRC_ARXIV_2506_15445` (Akturk et al., μLHC, PTEP 2026 033C04,
arXiv:2506.15445v2, `RELATED_MACHINE`). Values quoted below as "reported" are the sources'
numbers; "computed" values are what the test code produces (recomputed on 2026-10-28).

| # | Test (function in `tests/scientific/test_analytical_checks.py`) | Relation checked | Inputs (source, location) | Reported value | Computed value | Tolerance in the test | Result |
|---|---|---|---|---|---|---|---|
| 1 | `test_gamma_and_lifetime_1tev` | γ = E/m_μ; τ_lab = γ τ_μ | E_μ = 1 TeV; m_μ = 105.6583755 MeV, τ_μ = 2.1969811 μs (PDG 2024) | "approximately 20 ms" (arXiv:2506.15445 §2.3) | γ = 9464.5; τ_lab = 20.79 ms | γ: rel 2×10⁻⁴ against 9464.5; τ_lab: rel 10⁻³ against 20.79 ms | pass |
| 2 | `test_mulhc_main_ring_turns_and_average_population` | T_rev = C/c; N_turns = τ_lab/T_rev; ⟨N/N₀⟩ over one lifetime = 1 − e⁻¹ | C = 3 km (arXiv:2506.15445 §2.3) | "~10 μs per turn, ~2000 turns, average ~0.63 N₀" (§2.3) | 10.0 μs; 2078 turns; 0.632 | T_rev rel 2×10⁻³; 2000 ≤ N_turns ≤ 2100; 0.632 abs 10⁻³ | pass |
| 3 | `test_sqrt_s[500/1000/2000 GeV]` | √s = 2√(E_μE_p) (massless, head-on); exact form with masses | E_p = 7 TeV; E_μ = 0.5, 1, 2 TeV (DIS2026 Table 1 p.4 and §2; White-Paper working points, `SRC_WS1681458_KHANPOUR_GAMMAGAMMA` p.4) | 3.7 / 5.3 / 7.5 TeV | 3.742 / 5.292 / 7.483 TeV | rel 10⁻³ against 3.742 / 5.292 / 7.483; exact vs approximate rel 10⁻⁶ | pass (×3) |
| 4 | `test_dis2026_table1_luminosity_reproduced_with_h_equal_one` | L = f N_μ N_p /(4π σ_x σ_y) · H | f = 4 MHz, N_μ = 0.07×10¹¹, N_p = 22×10¹¹, σ = 4.8 μm (DIS2026 Table 1, p.4) | 2.1×10³⁴ cm⁻²s⁻¹ | 2.13×10³⁴ (H = 1) | rel 0.03 (observed deviation 1.3 %) | pass — the published value is reproduced **only with H = 1**, i.e. no hourglass or decay reduction is visible in Table 1 (open item, see §2.1) |
| 5 | `test_dis2026_proton_bunch_population_is_ten_times_hl_lhc` | same formula with N_p = 2.2×10¹¹ vs 22×10¹¹ | DIS2026 Table 1 vs μLHC Table 2 / HL-LHC baseline | 2.1×10³⁴ | ratio exactly 10; L(2.2×10¹¹) = 2.1×10³³ | ratio rel 10⁻⁹; L rel 0.03 | pass — the factor 10 between the two documents is a real design difference (DIS2026: fewer, more populated LHC bunches), not a unit slip |
| 6 | `test_mulhc_table3_luminosity_reproduced_by_naive_formula_times_decay_average` | L_naive × (1 − e⁻¹) | f = 4 MHz, N_μ = 3.0×10¹⁰ (ERL booster) / 3.7×10¹⁰ (μTRISTAN booster), N_p = 2.2×10¹¹, σ_x,y = 4.3 μm (arXiv:2506.15445 Tables 1–3, §2.3) | 7.2×10³³ / 8.8×10³³ (AloHEP, post-erratum) | L_naive = 1.14×10³⁴ / 1.40×10³⁴ (ratio to reported 1.58 / 1.59); × 0.632 → 7.18×10³³ / 8.86×10³³ | rel 0.02 (observed deviations 0.25 % and 0.66 %) | pass — both reported values equal the naive formula times the one-lifetime decay average; **no additional hourglass reduction is visible** |
| 7 | `test_hourglass_factor_for_mulhc_like_optics` | geometric hourglass factor H by double numerical integral (`analytical.hourglass_factor`) | β*_x,μ = 3 cm, β*_y,μ = 0.7 cm, σ_z,μ = 2 mm, ε_n,μ = 4 μm (arXiv:2506.15445 Table 1); β*_p = 7 cm, ε_n,p = 2 μm (Table 2); **σ_z,p = 7.5 cm is an order-of-magnitude LHC input, not a source value — the LHμC proton bunch length is unknown** | none (the paper quotes no H) | H = 0.535 | 0.50 < H < 0.57 (band to detect unintended change); sanity limit H → 1 abs 10⁻³ | pass — recorded as an **open inconsistency**: if H ≈ 0.53 applied, the published μLHC luminosities would not be reproduced (see §2.1) |
| 8 | `test_proton_beam_size_reproduces_mulhc_table3` | σ = √(ε_n β*/(β_rel γ)) | ε_n = 2 μm, β* = 7 cm, E_p = 7 TeV (arXiv:2506.15445 Tables 2–3) | 4.3 μm | 4.33 μm | rel 0.02 | pass |
| 9 | `test_brho_and_bending_field` | Bρ = p/(0.2998 q); B = Bρ/ρ | p = 1 TeV/c; ρ = 1 km, p = 960 GeV/c (μTRISTAN booster arcs, arXiv:2506.15445 §2.2.3 "3 T max"); ρ = 3 km/2π for a fully-dipole 3 km ring | "3 T max" | Bρ = 3335.6 T m; B(960 GeV, 1 km) = 3.20 T; B(1 TeV, 3 km ring, fill factor 1) = 6.99 T | Bρ rel 10⁻³; 3.2 T rel 0.02; 6.99 T rel 0.01 | pass — 3.2 T is consistent with "3 T max" within the uniform-bending idealisation |
| 10 | `test_booster_survival_mutristan_racetrack` | turn-by-turn decay in linacs (linear ramp) and arcs (constant energy), `analytical.survival_racetrack_booster` | 2 × 3 km linacs, 30 GeV each, 1 km radius arcs, 212 MeV → 960 GeV in 16 turns (arXiv:2506.15445 §2.2.1) | "approximately 82 %" | 81.6 % (E_final = 960.2 GeV) | E_final rel 10⁻³; 0.75 < survival < 0.90 | pass — residual 0.4 % recorded, not tuned away |
| 11 | `test_booster_survival_erl_racetrack` | same model | 2 × 1 km linacs, 10 GeV each, 1 km radius arcs, 212 MeV → 1 TeV in 50 turns (arXiv:2506.15445 §2.2.2) | "approximately 67 %" | 67.4 % | E_final rel 10⁻³; 0.55 < survival < 0.80 | pass |
| 12 | `test_survival_linear_ramp_limits` | constant-energy limit of the linear-ramp formula | — (internal consistency of `analytical.py`) | — | agreement | rel 10⁻⁶ | pass |
| 13 | `test_bjorken_x_reach` | x_min = Q²/s | Q² = 10 GeV², √s = 5.3 TeV (arXiv:2506.15445 Table 5) | 3.6×10⁻⁷ | 3.56×10⁻⁷ | rel 0.02 | pass |

The survival bands in rows 10–11 are deliberately wide (±7–12 %) because the paper does not
state its decay model (ramp shape, arc lengths, injection details); the band asserts that the
simple model lands in the same region, not that it reproduces the digits. Narrowing these bands
requires the authors' model, not a tuned parameter.

### 2.1 Open items raised by the P1 checks (not resolved in Phase 0)

- **Luminosity model assumptions.** DIS2026 Table 1 is reproduced with H = 1 (row 4); μLHC
  Tables 1–3 are reproduced with the decay average only (row 6); the hourglass factor computed for
  μLHC-like optics with a 7.5 cm proton bunch is ≈ 0.53 (row 7). Either AloHEP used a much shorter
  proton bunch, relaxed muon optics or no hourglass term, or the published numbers are
  peak-without-geometric-reduction values. The tests reference this as conflict
  `CONF_LUMI_MODEL_ASSUMPTIONS`, to be recorded in `research/source_conflicts.yaml` (file **not yet
  present** on 2026-10-28; `python -m lhmuc validate` reports `conflicts: 0`).
- **Proton bunch population.** 22×10¹¹ (DIS2026) vs 2.2×10¹¹ (μLHC / HL-LHC) — kept as separate
  scenarios (`LHMUC-DIS2026-1TEV` vs `MULHC-PTEP2026-*`), never averaged (`CLAUDE.md` §1.6).
- **Inconsistent statement to correct.** `docs/architecture.md` §5 and the Phase 0 task brief
  state a naive μLHC luminosity of 1.14×10³⁵ (ratio ≈ 16 to the reported 7.2×10³³). The committed
  test (commit dfec8d7, "corrected muLHC luminosity audit check") computes 1.14×10³⁴, ratio 1.58,
  fully explained by the decay average. The test is right (f N_μ N_p /(4πσ²) with the Table 1–3
  inputs gives 1.14×10³⁴); the prose in `architecture.md` §5 should be corrected by its author.

### 2.2 How the P1 checks are linked to parameter records

Parameter records carry `validation.level` and `validation.methods`; on 2026-10-28, of 796 records
267 are `P1` and 529 are `P0` (counted with `lhmuc.registry.load_all`); no record claims P2 or higher. The `P1` records name the test
function in `validation.methods` (e.g. "reproduced by 2*sqrt(E_mu*E_p) = 5.29 TeV …
(tests/scientific/test_analytical_checks.py::test_sqrt_s)"). The `validation.check_ids` field is
**empty in every record** on this date; it is to be filled with the `check_id`s of
`registries/validation_registry.csv` once that registry exists (§5).

---

## 3. Planned benchmarks for Milestones M2–M5 (nothing below exists yet)

Each benchmark below is written as *target → source of truth → tolerance → what passing proves*.
Tolerances are fixed here, before any run, and may only be tightened. A benchmark that cannot be
reproduced is a result to report (`CLAUDE.md` §1.10), not a parameter to tune.

### 3.1 Luminosity benchmark via AloHEP comparison (M2, target P2)

- Reproduce the AloHEP luminosities 7.2×10³³ and 8.8×10³³ cm⁻²s⁻¹ (arXiv:2506.15445 Tables 1–3,
  restated post-erratum in `SRC_WS1681458_DAGLI_NUCLEUS` p.8) and the μA luminosities and tune
  shifts of the Nucleus-Options deck (p.11–14) with a documented luminosity code in
  `physics/luminosity/` that includes decay, hourglass, crossing angle and beam–beam terms with
  switchable options.
- Tolerance: 5 % on L for each configuration, **with the option set recorded**; the test must state
  which terms were switched off to reproduce the published number. Passing proves that the
  published values are understood, not that they are achievable.
- Blocked until: AloHEP's model (or its documentation) is obtained — all CERN/Indico hosts are
  blocked in the current session; the proton bunch length and muon β* for LHμC proper are unknown
  (`unknown_roles` in `parameters/machine/scenarios_dis2026.yaml`).

### 3.2 Optics cross-check MAD-X vs Xsuite (M2–M3, target P3)

- Candidate codes: cpymad 1.20 (MAD-X) and xsuite 0.67, both installable from PyPI in this
  environment (`docs/architecture.md` §11); neither adopted or pinned yet.
- Test: identical lattice description (first a toy 3 km ring reproducing the stated circumference
  and revolution period 10.0 μs, later any published μLHC/LHμC lattice if one becomes available)
  → Twiss parameters, tunes, β* at the IP. Tolerance: β-functions rel 10⁻³, tunes abs 10⁻⁴,
  closed orbit abs 1 μm for a lattice without errors (both codes solve the same linear problem).
- A **P3 label from this check applies to the lattice model only**, not to LHμC: no LHμC lattice
  has been published (DIS2026 gives "about 3 (6) km" and Fig. 2 only).

### 3.3 Material-interaction cross-check Geant4 vs BDSIM (M3, target P3)

- Geant4 is **not installed** in this environment and BDSIM depends on it; pyg4ometry 1.4.6 (GDML
  writing) is installable. Benchmark: energy deposition and particle fluence behind the μLHC-type
  nozzle (6 m tungsten + borated polyethylene, "19 % of the energy deposited", arXiv:2506.15445
  §2.4) from a 1 TeV μ⁺ decay-electron spectrum.
- Tolerance (pre-registered): total deposited energy fraction rel 10 % between the two codes
  with identical geometry (GDML from `cad/gdml/`) and physics lists recorded; fluence maps compared
  bin-wise with statistical uncertainty ≥ 10⁴ primaries per run.
- The snippet-only IMCC leads (INERMET180, nozzle tip 6 cm from the IP, 10° outer inclination,
  L* = 6 m at 10 TeV) are **not verified** and may be used only as `analogous`, confidence ≤ medium.

### 3.4 Generator cross-section reproduction (M3, target P2)

- **Di-Higgs μ⁺p → hhjν̄** (`SRC_WS_LEBOHO_KUMAR_DIHIGGS`, slides p.6–8): reproduce the stated
  cross sections 0.17 fb and 0.33 fb (configurations as given on p.7–8) with MadGraph5_aMC@NLO
  v3.6.7 and CTEQ6L1, then the cut-flow (p.12) and S/√(S+B) = 4.25 at 70 % b-tag efficiency with
  1 ab⁻¹ (p.14–16). Tolerance: LO cross section rel 5 % (same generator version, PDF set and cuts;
  residual from scale/seed choices stated by the deck only partially); cut-flow efficiencies abs
  2 % per step. **Blocked**: the UFO model `effdihiggs-v2` (HELv2) is not public; a reproduction
  with another EFT implementation is a *comparison*, not a reproduction, and must be labelled so.
- **μLHC Higgs yields** (arXiv:2506.15445 §3, Tables 4–6): reproduce the SM Higgs production
  cross sections / event yields at √s = 5.3 TeV with MG5_aMC and a stated PDF set; tolerance
  rel 10 % (PDF set and scale choices in the paper to be checked against its text before the run).
- **Two-photon benchmarks** (`SRC_WS1681458_KHANPOUR_GAMMAGAMMA` p.5, p.15, p.19): reproduce the
  EPA γγ cross sections for the three working points (500 GeV/3.7 TeV/250 fb⁻¹;
  1 TeV/5.3 TeV/1000 fb⁻¹; 2 TeV/7.5 TeV/1000 fb⁻¹, attributed to the "HELP4CERN White Paper
  (in preparation)", not public) with the EPA implementation recorded (p.9–11). Tolerance rel 10 %
  given the sensitivity to the photon-flux cut-offs, which must be read from the slides and quoted.
- **HNL benchmark (arXiv:2610.28252)**: the paper is `access: blocked`, category `UNVERIFIED`
  (`research/_fragments/theory-benchmarks_sources.yaml`); only snippets are known (3 TeV μ⁺μ⁻,
  1 ab⁻¹, six benchmark points, expected limits on |U_μN|² ≈ 6.7×10⁻⁶ – 8.3×10⁻⁵ per snippet). The
  validation step is: fetch and read the paper, reproduce its μ⁺μ⁻ limits with its model (if a UFO
  is public) **before** any μ⁺p recast; until then no P-level above P0 may be attached to a recast.
- **arXiv:2610.17801 (2HDM+VLQ, A → ZZγ)** is a decay-width paper (BR 10⁻⁵–10⁻⁴ per snippet) with
  no collider simulation; validation would consist of reproducing the published partial widths at
  the benchmark points, which requires the full text (blocked).

### 3.5 Statistics and optimisation (M4–M5)

- pyhf 0.7.6 likelihoods: closure test against the asymptotic limits quoted in the di-Higgs deck
  (95 % CL limits on g_hhh, g_hWW, g_hhWW, p.14–16) within 10 % on the limit; toy-vs-asymptotic
  agreement checked where the deck gives enough information.
- Optimizers (pymoo, botorch): recovery of known optima on analytic test functions before use;
  `optimization.schema.json` requires `convergence_evidence`, `feasibility_rate` and
  `conclusions_blocked_by` — an optimisation whose constraint bounds are unknown reports no
  conclusion.

---

## 4. Test categories (master prompt §40) and the tolerance rule

| Category | Location | Content now (2026-10-28) | Content planned |
|---|---|---|---|
| **unit** | `tests/unit/` | `test_schemas.py` (every schema compiles, null-vs-zero and synthetic rules enforced), `test_units.py` (pint parsing of every unit string), `test_registry_integrity.py` (referential integrity, provenance rules, snippet-confidence cap, CSV sync, presence of the authored registries) | loaders, converters, CAD generators, API handlers |
| **scientific** | `tests/scientific/` | `test_analytical_checks.py` — the 15 P1 checks of §2 | P2/P3 benchmark reproductions of §3, each with pre-registered tolerance, source quotation and run-record id |
| **geometry** | *(no directory yet; to be `tests/geometry/`)* | — | STEP validity, overlap checks (`cad/validation`), volume and mass consistency against material records, G-label propagation A→B→C |
| **integration** | `tests/integration/` (empty) | — | parameter change → stale propagation → regenerated registries; scenario → lattice deck → optics run record end-to-end on toy inputs |
| **regression** | `tests/regression/` (empty) | — | frozen outputs of every completed P2/P3 benchmark; any change in a result must be explained in the commit |
| end-to-end | `tests/end_to_end/` (empty) | — | later milestones |

**Tolerance rule.** A scientific or regression tolerance is set *before* the first run, with its
justification written in the test docstring (as in §2). It may be tightened at any time. It is
**never loosened** without (a) an investigation written in `docs/reports/` or the commit message
that identifies the physical or numerical cause, (b) a reviewer other than the author of the
change, and (c) an entry in `registries/validation_registry.csv` recording the old and new
tolerance and the reason. Making a failing check pass by widening its band or by changing an
input value is prohibited (`CLAUDE.md` §1.9); the correct outcome of an irreproducible benchmark
is a failing test marked `xfail(strict=True)` with the investigation referenced, and the affected
parameters reset to P0.

---

## 5. `registries/validation_registry.csv` — format

The file is **authored** (not generated; `tools/build_registries.py` only checks that it exists)
and does **not yet exist** on 2026-10-28 (`registries/` is empty). `tests/unit/
test_registry_integrity.py::test_registry_csv_exists_and_has_rows` will fail until it has at
least two data rows. One row per check; `check_id` is referenced from parameter records through
`validation.check_ids`.

| Column | Content |
|---|---|
| `check_id` | `CHK_<LEVEL>_<TOPIC>`, UPPER_SNAKE, e.g. `CHK_P1_GAMMA_TAU_1TEV`, `CHK_P1_LUMI_DIS2026_H1`, `CHK_P2_ALOHEP_LUMI_MULHC` |
| `level` | `P1` … `P4` (the level this check confers when it passes) |
| `category` | `unit | scientific | geometry | integration | regression` |
| `description` | one sentence stating the relation and what passing proves |
| `target_parameter_ids` | `;`-separated parameter ids whose `validation.level` depends on this check |
| `input_parameter_ids` | `;`-separated inputs (or `constants:PDG2024` for physical constants) |
| `source_ids` | `;`-separated `source_id`s whose values are reproduced |
| `code_reference` | `path::function` of the implementing test or run record id (`lhmuc-<topic>-NNNNNN`) |
| `reported_value` | value and unit as quoted by the source (or `none`) |
| `computed_value` | value and unit produced by the check |
| `tolerance` | as coded, e.g. `rel 1e-3`, `abs 1e-3`, `band [0.50,0.57]` |
| `tolerance_justification` | why this tolerance (rounding in the source, unstated model, statistics) |
| `result` | `pass | fail | xfail | not_run` |
| `last_run` | ISO date |
| `tolerance_history` | empty, or `YYYY-MM-DD: old -> new (reason, report path)` entries separated by `;` |
| `open_items` | conflict ids (`CONF_…`), assumption ids (`ASM_…`) or free text |
| `notes` | free text |

Rows are added when a test is added, updated when it is re-run with a different outcome, and
never deleted (a retired check gets `result: not_run` and a note). The 13 functions of §2 map to
13 rows (`test_sqrt_s` as one row listing its three parametrisations).

---

## 6. Reporting

Every milestone report under `docs/reports/` lists, per claimed result: provenance status of the
inputs, G-label, P-label, the check ids that support the P-label, the assumption ids involved,
and the open conflicts. A result whose P-label is P0 is reported as unverified in those words.

## 7. Sources cited

- `SRC_ARXIV_2610_35154` — K. Piotrzkowski (HELP4CERN Study Group), "LHμC: A high energy, high
  luminosity muon-hadron collider at CERN", PoS DIS2026, arXiv:2610.35154v1 (2026-10-26). Table 1
  p.4; layout Fig. 2 p.3; IR §3 p.4–5; detector §4 p.5.
- `SRC_ARXIV_2506_15445` — D. Akturk et al., "μLHC: Antimuon Ring and HL-LHC based μ⁺p Collider",
  PTEP 2026 033C04, arXiv:2506.15445v2. §2.2 (booster survival), §2.3 and Tables 1–3 (beam
  parameters, luminosity), §2.4 (nozzle), §3 and Tables 4–6 (physics).
- `SRC_WS1681458_DAGLI_NUCLEUS` — Dagli et al., "LHμC: Nucleus Options", Kraków workshop slides
  (Indico 1681458), μ⁺ table p.8, AloHEP p.11, μA parameters p.12–14.
- `SRC_WS1681458_KHANPOUR_GAMMAGAMMA` — H. Khanpour, "Two-Photon Physics at the LHμC", working
  points p.4, cross sections p.5, 15, 19, EPA p.9–11.
- `SRC_WS_LEBOHO_KUMAR_DIHIGGS` — T. Leboho, M. Kumar et al., "Probing anomalous Higgs couplings at
  the future μ⁺p collider", configuration p.6, cross sections p.7–8, cut-flow p.12, results p.14–16.
- arXiv:2610.28252 and arXiv:2610.17801 — `access: blocked`, `UNVERIFIED`; metadata from search
  snippets only (`research/_fragments/theory-benchmarks_sources.yaml`).
