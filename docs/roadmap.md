# LHμC-VirtualLab — Roadmap (Milestones M1–M5)

**Document date:** 2026-10-28 · **Revised:** 2026-10-29 (baseline note, M1 state, §2.1 M2 inputs
now available, dated notes on blockers) · **Project phase:** Phase 0 = Milestone M1 (evidence and
feasibility audit) · **Owner:** David Hausler.

**Scope note.** The master project prompt (§42–46) defines the milestone sequence M1–M5; the
prompt itself is not stored in this repository. This document restates that sequence as it is
already summarised in `docs/scientific_scope.md` §3 and `docs/validation_plan.md` §3 and adds
concrete deliverables, entry/exit criteria, dependencies and blockers. Where the restatement and
the master prompt differ, the master prompt wins and this file must be corrected. Nothing below
claims that a digital twin, CAD model, lattice, event sample, user interface, optimisation or
validation beyond P1 exists: on 2026-10-28 none does (`README.md`, `docs/limitations.md` §7).

**Repository state used as the baseline (verified 2026-10-28):** `uv run python -m lhmuc validate`
reports 796 parameters (470 `reported_lhmuc`, 289 `imported_related`, 17 `analogous`,
12 `derived_lhmuc`, 6 `analytical_estimate`, 1 `scan_variable`, 1 `unknown`), 5 sources,
13 scenarios, 0 assumptions, 0 conflicts, 0 proposals, 0 errors. Present: schemas, `lhmuc/`,
`tools/`, `tests/unit` + `tests/scientific` (15 P1 checks), five archived PDFs with metadata,
nine research fragment families, and the policy documents `architecture`, `scientific_scope`,
`validation_plan`, `internet_research_protocol`, `synthetic_data_policy`, `fidelity_policy`,
`uncertainty_policy`, `limitations`, `security_policy`, this roadmap and `research_roadmap`.
**Not yet present:** `research/search_log.csv`, `research/source_registry.yaml` merged from the
fragments (only the five-upload registry exists), `research/source_conflicts.yaml`,
`research/unresolved_searches.md`, `registries/*.csv`, `parameters/assumptions/*.yaml`,
`parameters/materials/*.yaml`, `theory/benchmarks/*/proposal.yaml`, `docs/software_inventory.md`,
and the M1 report under `docs/reports/`.

**Baseline update (commit `104073c`, 2026-10-29):** `uv run python -m lhmuc validate` reports 5601
parameters (1035 `reported_lhmuc`, 1748 `imported_related`, 2647 `analogous`, 27 `derived_lhmuc`,
95 `analytical_estimate`, 20 `synthetic`, 1 `scan_variable`, 28 `unknown`), 236 sources (34
`uploaded`), 36 scenarios, 20 assumptions, 15 conflicts, 4 proposals, 0 errors, 0 warnings; the suite
collects 151 tests. Every item of the "not yet present" list above now exists, including the M1
report `docs/reports/M1_evidence_audit.md` and its addendum `docs/reports/M1_addendum_uploaded_documents.md`
(draft). A registry stage (assumption supersession, nine new conflict records, missing-evidence,
risk and validation rows) was in progress in the working tree on 2026-10-29; the counts above are
those of the commit, not of that stage.

---

## 0. Milestone overview

| Milestone | Title | Target label at exit | Status 2026-10-28 |
|---|---|---|---|
| **M1** | Phase 0 evidence and feasibility audit | P1 (closed-form checks), G0 | in progress |
| **M2** | Analytical and conceptual model; G0/G1 placeholder geometry; minimal evidence UI | P1–P2, G0–G1 | not started; entry criteria not met |
| **M3** | Benchmarks, generation and recasting; simulation geometry | P2–P3 (where codes exist), G1–G2 | not started; blocked on inputs |
| **M4** | Optimisation, uncertainty propagation and robustness | P2–P3 | not started |
| **M5** | Integrated co-design loop, commissioning-style studies and virtual controls | depends on inputs | not started; entry criterion ("LHμC hardware specifications exist") unreachable today |

*Status 2026-10-29:* unchanged in kind. M1 is still in progress (addendum extraction and
verification complete; registry stage and addendum report being finalised); M2–M5 are not started.
The uploads move several M2 inputs from "unknown" to "reported in workshop material, unverified by
simulation" (§2.1); none of them is a design, and no milestone label changes.

Rule for every milestone: a milestone may *start* only when its entry criteria are met, may
*exit* only when every exit criterion is verified by a test or a reviewed report, and every result
it produces carries the G/P labels and the `conclusions_blocked_by` list where applicable
(`docs/fidelity_policy.md`, `docs/validation_plan.md`).

---

## 1. M1 — Phase 0 evidence and feasibility audit (current)

**Purpose.** Record, with page-level provenance, what the five uploaded documents say about the
LHμC and the related μLHC, what they do not say (`null`), where they disagree, and which
closed-form checks reproduce the reported numbers.

**Deliverables**

| # | Deliverable | Location | State 2026-10-28 |
|---|---|---|---|
| 1.1 | Parameter records for all five uploads with verbatim quotations | `parameters/**/*.yaml` | 796 records present; human line-by-line review pending |
| 1.2 | Scenario definitions with explicit `unknown_roles` | `parameters/machine/scenarios_*.yaml` | 13 scenarios present |
| 1.3 | JSON schemas, loader/validator, CLI | `schemas/`, `lhmuc/` | present |
| 1.4 | P1 analytical cross-checks (γ, τ_lab, √s, naive L, Bρ, booster survival, hourglass) | `lhmuc/analytical.py`, `tests/scientific/` | present, 15 checks |
| 1.5 | Source registry, search log, unresolved searches merged from the nine fragment families | `research/source_registry.yaml`, `search_log.csv`, `unresolved_searches.md` | fragments present; merge via `tools/merge_research_fragments.py` not yet run |
| 1.6 | Conflict records (at least: luminosity-model assumptions; 80 vs 40 bunches; 2760/2748/2808 proton bunches; 5.3 vs 5.29 TeV; decay average 0.63 vs ≈0.64) | `research/source_conflicts.yaml` | not yet written |
| 1.7 | Assumption records for any synthetic range; materials records | `parameters/assumptions/`, `parameters/materials/` | directories empty |
| 1.8 | Generated and authored registries | `registries/parameter_registry.csv`, `assumption_registry.csv` (generated), `missing_evidence.csv`, `validation_registry.csv`, `risk_register.csv` (authored) | none present |
| 1.9 | Benchmark proposal records A–D | `theory/benchmarks/*/proposal.yaml` | none present |
| 1.10 | Policy and architecture documents, software inventory | `docs/*.md` | 11 of 12 present; `software_inventory.md` missing |
| 1.11 | M1 evidence-audit report (§49 format) | `docs/reports/` | not written |

*State of the deliverables on 2026-10-29 (commit `104073c`):* 1.1 — 5601 records, of which 4771 cite
the 29 addendum documents, each verified against the page images by an independent agent
(`research/_fragments/verify_G*.md`); human line-by-line review still pending. 1.2 — 36 scenarios.
1.4 — P1 checks in five scientific test files (`test_analytical_checks.py`, `test_workshop_decks.py`,
`test_batch7_documents.py`, `test_mucol_m17_vffa.py`, `test_batch9_documents.py`) plus canonical-value
tests; 151 tests collected. 1.5 — merged registry and logs present. 1.6 — 15 conflict records
committed, nine more drafted in the registry stage. 1.7 — 20 assumption records, of which the
registry stage marks those overtaken by uploaded evidence `superseded_by_evidence`; materials records
present. 1.8 — all five registries present (authored ones being extended in the registry stage). 1.9
— four proposal records. 1.10 — all documents present, revised on 2026-10-29. 1.11 —
`docs/reports/M1_evidence_audit.md` (2026-10-28) and the draft addendum
`docs/reports/M1_addendum_uploaded_documents.md`.

**Entry criteria (met).** Uploaded documents available and archived with SHA-256.

**Exit criteria.**
- `uv run python -m lhmuc validate` and `uv run pytest` pass with the registries present.
- Every `unknown_roles` entry across the 13 scenarios appears in `registries/missing_evidence.csv`
  with the search already performed and the next action.
- Every number quoted in `docs/*.md` resolves to a `parameter_id` or a `source_id` + page.
- Conflict records exist for the five conflicts listed in 1.6 and are referenced from the parameter
  `notes`.
- The M1 report lists: completed / evidence used / assumptions (none synthetic so far) / validation
  (P1 only) / limitations / results / next highest-value action.
- Human review of the LLM-extracted records has been done for at least the headline tables
  (DIS2026 Table 1; μLHC Tables 1–3; Khanpour working points; di-Higgs configuration).

**Dependencies.** None external. Parallel tasks 5–10 of the Phase 0 work plan (parameter
extraction, research logs, assumptions, registries, report).

**Open audit items carried into M2** (`docs/limitations.md` §5, `docs/validation_plan.md` §2.1):
the DIS2026 peak luminosity 2.1×10³⁴ cm⁻²s⁻¹ is reproduced by the naive formula with H = 1
(2.13×10³⁴); the μLHC 7.2×10³³ / 8.8×10³³ values are reproduced from 1.14×10³⁴ / 1.40×10³⁴ by the
decay average 0.63 alone, while the hourglass factor for the stated optics with a 7.5 cm proton
bunch is ≈0.53 and is not visible in the published numbers; the DIS2026 proton bunch population
22×10¹¹ is ten times the HL-LHC value and rests on a workshop reference not available here.
*[Update 2026-10-29: the workshop reference (Zimmermann, `SRC_WS1681458_ZIMMERMANN_SPS_LHC`) is now
read; it answers with earlier fewer-bunch schemes and the rule σδσz ≈ 2 n_b,0 σδ,0 σz,0 (p.14), not
with an LHμC proton bunch. AloHEP simulates hourglass and pinch and applies the decay factor
analytically; its public v2.0 code holds no μLHC deck. Details in `docs/limitations.md` §5.1.]*

---

## 2. M2 — Analytical and conceptual model

**Purpose.** Turn the P1 arithmetic into a documented, range-propagating analytical model; create
parameterised placeholder geometry that is visibly G0/G1; show provenance labels in a minimal UI.

**Deliverables**
- `physics/analytical/`, `physics/luminosity/`, `physics/muon_decay/`: luminosity with decay,
  hourglass, crossing-angle and (simple) beam-beam terms, each term switchable and recorded;
  muon lifetime and survival along booster/ring; dipole field vs radius; all inputs by
  `parameter_id`, all outputs with propagated ranges (`docs/uncertainty_policy.md`).
- **Benchmark 3.1** of `docs/validation_plan.md`: reproduce AloHEP 7.2×10³³ / 8.8×10³³ and the
  Nucleus-deck μA luminosities within 5 % *with the option set recorded*; target P2.
- `cad/generators/`: parameterised G0/G1 placeholders (main ring ≈3 (6) km, booster ≈9 km, IR
  envelope, nozzle cone) built from scenario parameters; every dimension with no LHμC source is
  either `analogous` with an assumption record or `synthetic` as a range — never a bare number.
  Candidate tools (not adopted): cadquery 2.8 / build123d 0.13, pyg4ometry 1.4.6 for GDML.
- `detector/fast_simulation/`: parametrised acceptance/resolution placeholders tagged G0, P0.
- `backend/api/` + `frontend/evidence_graph/` minimal: serve the parameter registry and show
  provenance status, G/P labels and synthetic badges (`docs/synthetic_data_policy.md` §UI);
  docker-compose `api` and `frontend` services uncommented only when they run.
- `lhmuc/analytical.py` moved to `physics/analytical/` (`docs/architecture.md` §12).
- Optics toy: a 3 km ring with the stated revolution period (10.0 μs) in cpymad and xsuite,
  **Benchmark 3.2** tolerances pre-registered; P3 applies to the toy lattice only.

**Entry criteria.** M1 exit; assumption records exist for every synthetic range that M2 will use
(hourglass needs the proton bunch length and muon β*, both unknown for LHμC proper and therefore
either `imported_related` from μLHC with an applicability note or synthetic ranges).

**Exit criteria.** Benchmark 3.1 passes or its failure is documented with the option set that
comes closest; every geometry object has `geometry_fidelity` set and a `SYNTHETIC DIMENSION`
badge where applicable; the UI displays no number without its status; `tests/geometry/` exists
with overlap and label-propagation tests; the M2 report is written.

**Dependencies / blockers.**
- *AloHEP model*: the GitHub repository `yefetu/ALOHEP` README was fetched (no beam-parameter
  content, no licence or release found); the IPAC'21 paper (`SRC_JACOW_IPAC2021_WEPAB278`) and
  the hepforge page are blocked. Without the formula set, Benchmark 3.1 can only test candidate
  option sets (research roadmap item R9).
- *Proton bunch length and muon β* for LHμC*: `unknown_roles` in the DIS2026 scenarios.
- *Nozzle geometry*: only the μLHC description (6 m tungsten + borated polyethylene, 19 % of the
  energy deposited) is read; IMCC numbers are snippet-only (R4).
- *Update 2026-10-29:* the AloHEP model is now documented (`SRC_ARXIV_2610_09839`) and its public code
  is on file: github.com/tobbetuyef/AloHEP, tag v2.0, MIT (`SRC_URL_GITHUB_TOBBETUYEF_ALOHEP`), the
  repository the method paper names, not the `yefetu/ALOHEP` copy of the first bullet; it has no μLHC
  deck (first bullet narrowed, not resolved); the proton bunch length and muon β*
  are still unknown; the nozzle geometry is now reported in workshop material and the IMCC numbers are
  read in full (§2.1).

### 2.1 M2 inputs now available (2026-10-29)

The uploads of the Phase-0 addendum and batches 7–9 put the following on file for M2. Each is an
input *with provenance*, not a design; LHμC values are "reported in workshop material, unverified by
simulation", the rest are comparators or analogues.

| M2 deliverable | Input now available | Record ids / source (page) | Still missing |
|---|---|---|---|
| Luminosity model, Benchmark 3.1 | AloHEP equations, toggles, outputs, decay treatment and limits; public code v2.0 (MIT) with a headless entry point; the one-beam vs two-beam decay average pinned | `MACHINE_ALOHEP_*_DAGLI2026`, `SRC_ARXIV_2610_09839` pp.7–39, `docs/tools/alohep_method_dagli2026.md`, `SRC_URL_GITHUB_TOBBETUYEF_ALOHEP`; `test_decay_averaging_differs_between_mumu_and_mup` | μLHC input decks and option set (`ME_043`); proton bunch length |
| Luminosity model, second LHμC set | Forthomme beam set (40 bunches of 10¹⁰ μ⁺, 300 ns, σ 4.3 µm, β*_p 7 cm, 10³⁴) and its implied N_p ≈ 7.0 × 10¹¹ under H = 1 | `MACHINE_*_WS2026_FORTHOMME`, `PROTON_BUNCH_POPULATION_IMPLIED_WS2026_FORTHOMME` (p.17) | muon energy, emittance, β* and bunch length of that set |
| Luminosity model, proton side | Zimmermann's fewer-bunch schemes and σδσz rule; LHC Project Report 627 and CERN-2005-006 tables as restated | `PROTON_*_WS2026_ZIMMERMANN` (request p.2, Report 627 Table 1 p.9, CERN-2005-006 Table 3 p.13, rule p.14), scenarios `LHC-PR627-*`, `QCD-EXPLORER-EPAC2004`, `LHC-DAMERAU-GAROBY-LONGBUNCH-EPAC2004` | an LHμC proton bunch population and length; HL-LHC TDR (`ME_044`) |
| Hourglass / IR comparators | LHeC L* 15 m, β*_p 10 cm, Fig. 19 β*_p 10.0 cm / β*_e 10.9 cm (per beam), head-on scheme, QA1 concept; IMCC L* 6 m; MuIC H = 1 convention | `IR_*_ANDRE2022` (pp.10–18), `IR_LSTAR_MR7` (p.65), `MACHINE_HOURGLASS_FACTOR_ASSUMED_MUIC2022` (p.7) | LHμC L*, Q1, crossing angle, separator (`ME_017`–`ME_020`) |
| G0/G1 nozzle placeholder | LHμC options 40 / 60 / 80 / 100 mrad, 487.8 cm + 100 cm drawing dimensions, tip 6 cm, tungsten + borated polyethylene, single-sided; IMCC Table G.1 profile and INERMET180 composition | `DET_NOZZLE_*_WS2026_KILIC` (pp.4–5, 12), `DET_NOZZLE_*_WS2026_FORTHOMME` (p.9), `DET_NOZZLE_*_MR7` (pp.65–66), `MAT_INERMET180_MR7`; `test_nozzle_half_angle_to_eta_max_forthomme_and_imcc` | base dimensions (to be set by simulation, Kilic p.22); tungsten grade and cladding thickness (not stated) |
| G0/G1 detector envelope | LHeC detector (LHeD 13 m × 9 m, 3 T in the 2022 paper, 3.8 T in the Delphes card); LHμC adaptations | `DET_LHED_LENGTH_WS2026_FORTHOMME`, `DET_LHED_DIAMETER_WS2026_FORTHOMME` (p.3), `DET_SOLENOID_FIELD_*`, `DET_LHMUC_*_WS2026_FORTHOMME` | an LHμC dimension table and solenoid field (`CONF_DETECTOR_SOLENOID_FIELD`) |
| Fast detector placeholder | MuIC Delphes card (Tables 16–18); LHeC Delphes resolutions as restated; TeV-muon resolutions 6–7 % (main) and ~6 % (far-forward) | `DET_DELPHES_*_MUIC2022` (PDF pp.41–45), `DET_DELPHES_*_LHEC_WS2026_FORTHOMME` (p.13), `CONF_TEV_MUON_RESOLUTION` | an LHμC card with provenance |
| Booster placeholder, toy vFFA cell | Kraków requirement and preliminary field options; M17 closed-orbit geometry and Tables 2.2–2.3 | `ACC_*_WS2026_TOPPMUGGLESTONE` (pp.3, 35–36), `*_MUCOLM17` (pp.6–13), `tests/scientific/test_mucol_m17_vffa.py` | an LHμC booster lattice with tracking (`ME_027`); RF |
| Muon decay along booster and ring | turns per lifetime n = γcτ_μ/C (2079 at 1 TeV in 3 km) | `PHYS_MUON_TURNS_PER_LIFETIME_FORMULA_DUDKO2026` (p.14); `test_turns_per_lifetime_dudko_formula` | stored-turn and fill-pattern model (`ME_042`) |
| Source-chain model | measured 2024 chain; formation fractions 0.52 and 0.655; the 0.73 calculation; μTRISTAN 0.137 budget; hybrid-target yield with η_conv unknown; hybrid-source 0.04 μ⁺/p; front-end space charge | `*_ARITOME2024`, `*_BAKULE2013`, `*_BEARE2020`, `*_ABE2019`, `*_WS2026_ZHANG`, `*_SAKAKI2026`, `*_WS2026_ROGERS`, `*_WS2026_NAKAZAWA` | measured 122 + 355 nm ionisation; extraction and second-stage cooling; a ≥ 10¹⁰ μ⁺ front-end design (`ME_030`–`ME_033`) |

Not available and still blocking M2 exit: the μLHC AloHEP input decks (Benchmark 3.1), the LHμC
proton bunch length and muon β*. (The MR7 reference tables, listed here before, were verified and committed on
2026-10-29; `docs/reports/M1_addendum_uploaded_documents.md` §A.8.) M2 may start on the inputs above only after the M1 exit criteria are met (§1), with
every synthetic input carried as a range with its assumption record.

---

## 3. M3 — Benchmarks, generation and recasting

**Purpose.** Compute μ⁺p processes with documented generators; recast the uploaded benchmarks;
build simulation geometry; run transport codes only if they become available.

**Deliverables**
- `event_generation/madgraph/`, `pythia/`: MadGraph5_aMC@NLO (installable from
  Launchpad/GitHub, not installed), Pythia 8 via `pythia8mc 8.318`, LHE handling via `pylhe 2.1`;
  all in containers per `docs/security_policy.md` §4–§6; PDF set and scale choices recorded.
- **Benchmark 3.4**: μLHC SM Higgs yields (arXiv:2506.15445 §3, Tables 4–6) within 10 %;
  di-Higgs μ⁺p → hhjν̄ cross sections 0.17 fb / 0.33 fb and S/√(S+B) = 4.25 at 70 % b-tag with
  1 ab⁻¹ (`SRC_WS_LEBOHO_KUMAR_DIHIGGS`, MG5_aMC v3.6.7, CTEQ6L1) — a *comparison* with a public
  EFT model unless `effdihiggs-v2` is obtained; two-photon EPA cross sections at the three
  working points (`SRC_WS1681458_KHANPOUR_GAMMAGAMMA`) within 10 % once the photon-flux
  cut-offs are quoted from the slides.
- `theory/`: proposal importer, UFO handling (inspection per security policy), μ⁺p process
  builder, recasting engine; proposal records for benchmarks A (HNL, arXiv:2610.28252) and B
  (2HDM+VLQ, arXiv:2610.17801) **only after the papers are read in full**; until then they stay
  `access: pending_fetch`, `review_state: extracted`, P0.
- `cad/gdml/` simulation geometry from the M2 placeholders; `detector/geant4/`, `detector/bdsim/`
  **only if** Geant4 is installed (Benchmark 3.3: Geant4 vs BDSIM nozzle energy deposition, 10 %).
- `analysis/`: selections and observables for the recast benchmarks; `pyhf 0.7.6` likelihoods.

**Entry criteria.** M2 exit; generator installed at a pinned release with hash and licence in
`docs/software_inventory.md`; UFO models obtained, inspected and licence-checked.

**Exit criteria.** At least one generator benchmark reproduced within tolerance with a run
record; every recast carries the P-level it earned (P0 if the original limits were not
reproduced first); every unreproducible benchmark is reported as such, not tuned.

**Dependencies / blockers.**
- **Geant4 / ROOT / LHAPDF / FLUKA not installed**; download and licence pages blocked
  (`docs/limitations.md` §4). Without Geant4 there is no nozzle, background or detector-response
  study and the 19 % figure cannot be reproduced.
- **MadGraph installation** possible (Launchpad/GitHub reachable) but not done; needs a container
  build, hash and licence record first.
- **The two theory papers** arXiv:2610.28252 (HNL at a 3 TeV μ⁺μ⁻ collider, 1 ab⁻¹) and
  arXiv:2610.17801 (one-loop A → ZZγ in 2HDM+VLQ, BR 10⁻⁵–10⁻⁴) are `UNVERIFIED`, known from
  snippets only; neither is a μ⁺p paper; no public UFO for either model was identified (HeavyN
  is a stand-in without the scalar sector; no combined 2HDM+VLQ UFO found).
- **`effdihiggs-v2` (HELv2)** is not public.
- **HELP4CERN White Paper** ("in preparation"): origin of the Khanpour working points
  (500 GeV/3.7 TeV/250 fb⁻¹; 1 TeV/5.3 TeV/1000 fb⁻¹; 2 TeV/7.5 TeV/1000 fb⁻¹) and presumably of
  the baseline the benchmarks assume; no URL, arXiv id or date exists.
- *Update 2026-10-29:* all four bullets above stand. New for M3: the Kilic nozzle study used
  Geant4 11.4, Pythia 8.312, HepMC 2.06.11, MadGraph5_aMC@NLO and NNPDF23_lo_as_0130_qed
  (`DET_NOZZLE_SIM_*_WS2026_KILIC`, pp.6–7) — a reproduction (Benchmark 3.3 class) needs those
  versions; the μ⁻p results of Cheung & Wang and the μ⁺p/μ⁻p tables of the muon-ion collider paper
  are comparators for M3 generator runs, never targets for μ⁺p (`docs/scientific_scope.md` §1.11).

---

## 4. M4 — Optimisation and uncertainty

**Purpose.** Define objectives and hard constraints from sourced or declared-synthetic bounds; run
sensitivity, robustness and Pareto studies whose conclusions state what blocks them.

**Deliverables**
- `uncertainty/priors/` from the Phase 0 input table (`docs/uncertainty_policy.md`),
  `propagation/`, `sensitivity/` (which unknowns dominate L, event yields, backgrounds),
  `robustness/`.
- `optimization/objectives/`, `constraints/`, `pareto/`, Bayesian (`botorch`) and evolutionary
  (`pymoo`) drivers validated first on analytic test functions (**Benchmark 3.5**); every record
  per `schemas/optimization.schema.json` with `convergence_evidence`, `feasibility_rate` and
  `conclusions_blocked_by`.
- Candidate differentiable-tracking surrogate (`cheetah-accelerator 0.8`, GPLv3 per README badge,
  licence file not yet read) evaluated for gradient-based IR studies — adoption decision recorded.
- Statistics closure: pyhf asymptotic vs toy limits against the di-Higgs deck's 95 % CL ranges
  within 10 %.

**Entry criteria.** M3 exit; every constraint bound either sourced (`parameter_id`) or declared
synthetic with an assumption record and a band.

**Exit criteria.** No optimisation result is presented as an optimum without its
`conclusions_blocked_by` list and the sensitivity ranking of unknown inputs; the M4 report
states explicitly which LHμC decisions remain undecidable.

**Dependencies / blockers.** Constraint bounds for the IR (L*, Q1 gradient and aperture, crossing
angle), nozzle, ring dipole field, wall-plug power and cost are all unknown for LHμC (recurring
`unknown_roles`); until the Kraków contributions or the White Paper are read, M4 can only run
on μLHC-derived or synthetic bounds and must say so.

---

## 5. M5 — Integrated co-design loop, commissioning-style studies, virtual controls

**Purpose.** Close the loop between evidence graph, geometry, lattice, generation, detector,
analysis and optimisation; add commissioning-style simulation (injection, ramp, orbit/optics
correction, machine protection) and virtual controls in `commissioning/`.

**Deliverables (conditional).** End-to-end tests in `tests/end_to_end/`; stale-propagation of
dependents on parameter change (`tests/integration/`); commissioning scenarios on the toy or
published lattice; virtual-controls interfaces that expose only validated models with their
labels.

**Entry criteria.** M4 exit **and** LHμC hardware-level specifications (lattice, magnets, IR,
nozzle, RF) published by the proponents. `docs/scientific_scope.md` §3 records the entry
criterion as "LHμC hardware specifications exist — no such specifications exist".

**Exit criteria.** To be defined when the entry criterion is in sight; P5 (calibration on an
operating LHμC) is unreachable for this project and never appears in the repository
(`docs/validation_plan.md` §1).

**Status.** Blocked indefinitely by the absence of LHμC hardware specifications; nothing in this
milestone is scheduled.

---

## 6. Cross-cutting blockers (apply to several milestones)

| Blocker | Affects | What unblocks it | Tracked in |
|---|---|---|---|
| **Network allow-list**: arxiv.org, indico.cern.ch, cds.cern.ch, inspirehep.net, pos.sissa.it, doi.org, journals, readthedocs, all CERN hosts blocked; only PyPI/npm/Launchpad/GitHub reachable | M1 (source promotion from snippet to read), M2 (AloHEP paper), M3 (papers, UFOs, licences), M4 (bounds) | hosts in `docs/internet_research_protocol.md` §8 allowed, or owner uploads | `research/_fragments/*_unresolved.md`; `docs/research_roadmap.md` |
| **Geant4 / BDSIM / FLUKA / ROOT / LHAPDF not installed** | M3 (Benchmark 3.3, detector response, backgrounds), M4 (BIB-dependent objectives) | licence check + container build once download hosts are reachable; FLUKA needs registration | `docs/limitations.md` §4 |
| **MadGraph5_aMC@NLO not installed** (reachable) | M3 | container build at pinned release, hash, licence in `docs/software_inventory.md` | this file, security policy §6 |
| **Two theory papers unverified** (arXiv:2610.28252, arXiv:2610.17801) and no public UFOs | M3 benchmarks A, B | fetch/upload, read in full, locate or build models | `research/_fragments/theory-benchmarks_unresolved.md` |
| **HELP4CERN White Paper "in preparation"** | all: it is the only likely source of an official LHμC baseline, IR and nozzle numbers | publication or author contact | `research/_fragments/lhmuc-primary_unresolved.md` |
| **Kraków workshop contributions (Indico 1681458)** not obtained (nozzle, vFFA, SPS/LHC modifications, detector, near-beam) | M2 geometry, M3 backgrounds, M4 bounds | Indico reachable or slides uploaded | `docs/internet_research_protocol.md` §10 |
| **`effdihiggs-v2` UFO not public** | M3 benchmark C | authors | `docs/limitations.md` §6 |
| **AloHEP luminosity model undocumented here** | M2 Benchmark 3.1 | IPAC'21 paper, hepforge page, or reading the repository source | `research/_fragments/mulhc-mutristan_unresolved.md` |
| *2026-10-29:* **AloHEP model documented; μLHC input decks missing** (replaces the row above) | M2 Benchmark 3.1 | the decks and option set from the authors or the PTEP erratum | `ME_043`, `docs/tools/alohep_method_dagli2026.md` |
| *2026-10-29:* Kraków contributions — **eleven uploaded**; Otani, Kamioka, Piotrzkowski, Tentori, Sultansoy, Holzer still missing (updates the Kraków row above) | M2 source/front end, M3 | Indico reachable or slides uploaded | `docs/research_roadmap.md` §3a W3 |
| *2026-10-29:* **MR7 reference tables not yet verified** | M2 (IMCC analogues for driver, target, cooling, magnets, RF, power converters) | completion of the lead's verifier pass | cite `SRC_ARXIV_2510_27437` with a page meanwhile |
| *2026-10-29 (later):* **MR7 reference tables verified and committed** (replaces the row above) | M2 | — | `docs/reports/M1_addendum_uploaded_documents.md` §A.8; `CONF_IMCC_*` |

---

## 7. Decision points for the owner

1. **Whether to proceed to M2 with μLHC-imported optics** (β*, bunch length, emittance) as
   `imported_related` stand-ins for LHμC, each with an assumption record — or to wait for the
   White Paper / Kraków slides. Recommendation: proceed, because the sensitivity study itself
   is informative, but label every result as μLHC-optics-based.
2. **Whether to install MadGraph now** (possible) to start Benchmark 3.4 on the μLHC Higgs
   tables in parallel with M2. Recommendation: yes, after the software inventory entry and a
   container build per the security policy.
3. **Whether to request the two theory papers, the di-Higgs UFO and the Kraków slides directly
   from the authors**, since network access may remain restricted. Recommendation: yes; this is
   the highest value-of-information action in `docs/research_roadmap.md`.

---

## 8. Change log

| Date | Change |
|---|---|
| 2026-10-28 | First version. Baseline = repository state at the end of the Phase 0 extraction (796 parameters, 13 scenarios, 0 assumptions/conflicts/proposals, registries and M1 report pending). |
| 2026-10-29 | Baseline note for commit `104073c` (5601 parameters, 36 scenarios, 34 uploaded sources); M1 deliverable states; §2.1 M2 inputs now available from the addendum and batches 7–9; dated notes on the M2/M3 blockers and the cross-cutting table. No milestone status changed. |

## 9. Sources cited

- `SRC_ARXIV_2610_35154` — K. Piotrzkowski (HELP4CERN), "LHμC: A high energy, high luminosity muon-hadron collider at CERN", PoS DIS2026, arXiv:2610.35154v1 (Table 1 p.4; layout Fig. 2 p.3).
- `SRC_ARXIV_2506_15445` — Akturk et al., "μLHC: Antimuon Ring and HL-LHC based μ+p Collider", PTEP 2026 033C04, arXiv:2506.15445v2 (Tables 1–6; §2.4 nozzle).
- `SRC_WS1681458_DAGLI_NUCLEUS` — Dagli, "LHμC: Nucleus Options", Kraków workshop slides (p.8 post-erratum luminosities; p.11–14 AloHEP μA parameters).
- `SRC_WS1681458_KHANPOUR_GAMMAGAMMA` — Khanpour, "Two-Photon Physics at the LHμC", Kraków workshop slides (p.4 working points attributed to the HELP4CERN White Paper, in preparation).
- `SRC_WS_LEBOHO_KUMAR_DIHIGGS` — Leboho, Kumar, "Probing anomalous Higgs couplings at the future μ+p collider" (p.6–8 configuration and cross sections; p.14–16 results).
- Snippet-level (not read, `UNVERIFIED`): arXiv:2610.28252, arXiv:2610.17801 (`research/_fragments/theory-benchmarks_sources.yaml`).
- Added 2026-10-29 (uploaded, read in full; pages as cited in §2.1): `SRC_ARXIV_2610_09839` (AloHEP), `SRC_URL_GITHUB_TOBBETUYEF_ALOHEP` (fetched), `SRC_WS1681458_FORTHOMME_DETECTOR`, `SRC_WS1681458_ZIMMERMANN_SPS_LHC`, `SRC_WS1681458_KILIC_NOZZLE`, `SRC_WS1681458_TOPPMUGGLESTONE_VFFA`, `SRC_DOI_10_5281_ZENODO_15054073`, `SRC_ARXIV_2510_27437`, `SRC_ARXIV_2201_02436`, `SRC_ARXIV_2203_06258`, `SRC_ARXIV_2607_16904`, and the source-chain documents listed in `docs/scientific_scope.md` §7.
