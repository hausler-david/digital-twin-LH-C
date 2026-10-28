# LHμC-VirtualLab — Repository architecture

**Document date:** 2026-10-28 · **Project phase:** Phase 0 (evidence and feasibility audit) ·
**Owner:** David Hausler · **Status of this document:** describes what exists on 2026-10-28 and what
is planned; every planned item is marked *future*. Nothing here claims that a digital twin,
a CAD model, a lattice, an event sample or a user interface exists. None does.

Read `CLAUDE.md` first; its rules are binding and this document only explains how the repository
is laid out to satisfy them.

---

## 1. Purpose and scope of the platform

LHμC-VirtualLab is intended to become an evidence-traceable digital twin, theory-recasting and
co-design platform for the proposed **LHμC muon–proton collider at CERN** (HELP4CERN Study Group;
K. Piotrzkowski, PoS DIS2026, arXiv:2610.35154, source id `SRC_ARXIV_2610_35154`). The only
beam-optics-level parameter tables for a μ⁺p collider at CERN come from the predecessor **μLHC**
study (Akturk et al., PTEP 2026 033C04, arXiv:2506.15445, `SRC_ARXIV_2506_15445`), which is a
*related machine*, not LHμC itself.

Phase 0 therefore does one thing: it records, with page-level provenance, what the five uploaded
primary and related documents actually say, what they do not say (as `null`), where they disagree,
and which closed-form checks (P1) reproduce the reported numbers. Everything downstream
(geometry, lattice, generation, simulation, optimization, UI) is architecture only.

---

## 2. Why the prompt tree lives at the repository root

The master project prompt (sections 0–52) prescribes a module tree — `parameters/`, `schemas/`,
`cad/`, `lattice/`, `physics/`, `detector/`, `theory/`, `event_generation/`, `analysis/`,
`optimization/`, `uncertainty/`, `commissioning/`, `backend/`, `frontend/`, `research/`,
`references/`, `registries/`, `results/`, `docs/`. The tree is created **at the repo root, now, with
a README in every placeholder directory**, for four reasons:

1. **The architecture is a contract, not an afterthought.** Reviewers can see where each future
   artefact will land and which entry criterion (milestone) must be met before it may be populated.
2. **Placeholders state "not implemented" explicitly.** Each `*/README.md` says *"Status: not
   implemented (Phase 0 placeholder)"* and names its intended role and entry criterion, so an
   empty directory can never be mistaken for a finished component.
3. **Paths are stable identifiers.** Parameter records already carry `responsible_module` values
   such as `parameters/machine`; schemas and tools refer to fixed paths
   (`lhmuc/registry.py` hard-codes `schemas/`, `parameters/`, `research/`, `theory/benchmarks/`).
   Fixing the layout first prevents a later re-shuffle that would break provenance links.
4. **Licensing is path-based.** `LICENSE-DATA` assigns CC BY 4.0 to `docs/`, `research/`,
   `parameters/`, `registries/`, `schemas/`, `theory/benchmarks/` and Apache-2.0 (`LICENSE`) to the
   code directories; the split only works if the directories exist as named.

---

## 3. Single source of truth and the generation chain

```
parameters/**/*.yaml            authored; schema provenance.schema.json (parameter records)
parameters/machine/scenarios_*.yaml   authored; schema machine.schema.json (roles -> parameter_id, no numbers)
parameters/assumptions/*.yaml   authored; schema assumption.schema.json      (none exist yet, see §5)
parameters/materials/*.yaml     authored; schema material.schema.json        (none exist yet)
research/source_registry.yaml   authored (5 uploads) + merged from research/_fragments/ by tools/merge_research_fragments.py
research/source_conflicts.yaml  authored; schema conflict.schema.json        (not yet present)
theory/benchmarks/*/proposal.yaml   authored; schema proposal.schema.json    (not yet present)
          │
          ▼  tools/build_registries.py   (refuses to write if lhmuc.registry reports any error)
registries/parameter_registry.csv, registries/assumption_registry.csv     GENERATED, never hand-edited
registries/missing_evidence.csv, validation_registry.csv, risk_register.csv   AUTHORED (checked only)
          │
          ▼  later milestones (future)
cad/generators  -> STEP/glTF/GDML        lattice/* -> MAD-X / Xsuite / Bmad decks
event_generation/* -> run records        analysis/reports, docs/reports -> generated reports
```

Rules enforced in code (`lhmuc/registry.py::cross_check`, run by `uv run python -m lhmuc validate`
and by `tests/unit/test_registry_integrity.py`):

- every `unit` string must parse through `lhmuc/units.py` (pint, `UNIT_ALIASES`);
- `status: unknown` ⇒ `value: null`; a non-unknown status with `value: null` is an error;
  `value: 0` without a `notes` entry raises a warning (zero is a physical value, not "unknown");
- `reported_lhmuc` requires a source whose `category` is `PRIMARY_LHMUC` and a verbatim
  `quotation`; `imported_related` and `analogous` also require a quotation;
- `derived_lhmuc` and `analytical_estimate` require a `derivation` string;
- `synthetic` requires an existing `assumption_id` **and** an `allowed_range` (no bare points);
- `dependencies`, `scenario`, `source_id`, scenario roles, conflict sources and proposal sources
  must resolve (referential integrity);
- a source seen only as a search snippet (`access: snippet_only|blocked|pending_fetch`) caps the
  parameter's `confidence` at `medium` (test `test_snippet_sources_capped_confidence`).

CSV files are *views*: `tools/build_registries.py --check` fails the test-suite if a CSV is out of
sync with the YAML. The YAML is the only place a number is edited.

---

## 4. Schemas and what each governs

All schemas are JSON Schema 2020-12 under `schemas/`, loaded through a `referencing` registry so
that `"$ref": "provenance.schema.json#/$defs/..."` works across files. `tools/validate_yaml.py
<schema-name> <file>` validates one file; `python -m lhmuc validate` validates everything.

| Schema file | Governs | Key content |
|---|---|---|
| `provenance.schema.json` | parameter records (`parameters/**/*.yaml`, top-level `parameters:`) and the **shared vocabulary** | `$defs`: `provenance_status` (8 values), `geometry_fidelity` G0–G5, `validation_level` P0–P5, `source_category` (9 values), `access_mode` (5 values), `confidence`, `review_state`, `applicability_category`, `fidelity_tier` A–E, `quantity`, `uncertainty`, `allowed_range`, `source_ref`, `provenance`, `validation`, `parameter` |
| `machine.schema.json` | machine scenarios (`parameters/machine/scenarios_*.yaml`, top-level `scenarios:`) | `scenario_id`, `machine` ∈ {LHMUC, MULHC, MUTRISTAN, LHEC, HL_LHC, OTHER}, `status` ∈ {reported, partially_reported, derived, superseded, synthetic_scan}, `parameters` (role → parameter_id, **no numbers**), `unknown_roles`, `geometry_fidelity`, `validation_level` |
| `assumption.schema.json` | synthetic/analogous assumption records (`parameters/assumptions/`) | `assumption_id`, `parameter_id`, `reason_required`, `search_summary`, `sources_inspected`, `reason_authoritative_value_missing`, `synthetic_model` (distribution, min, max, unit), `physical_basis`, `analogous_systems`, `affected_outputs`, `replacement_evidence`, `sensitivity_analysis` |
| `source.schema.json` | `research/source_registry.yaml` | `source_id`, `category`, `access`, `publication_date`, `version`, `licence`, `archived_file`, `sha256`, `discovered_by_queries`, `unresolved_questions` |
| `conflict.schema.json` | `research/source_conflicts.yaml` | `conflict_id`, `affected_parameters`, `competing_values` (each with source), `possible_cause`, `selected_treatment`, `effect_on_simulations`, `required_future_evidence` |
| `proposal.schema.json` | `theory/benchmarks/*/proposal.yaml` | `proposal_id`, `arxiv_id`, `source_id`, `access`, `review_state` (LLM-extracted content stays `extracted` until a human marks `reviewed`), `model`, `original_study`, `model_implementation`, `lhmuc_recasting`, `extraction` |
| `material.schema.json` | `parameters/materials/*.yaml` | `material_id`, `composition`, `density`, `geant4_material_name`, `properties`, `provenance`, `used_by_components` |
| `component.schema.json` | geometry/engineering components (future, `cad/`) | `component_id`, `geometry_version`, `geometry_fidelity` (G-label), `physics_validation` (P-label, independent), `dimensions` (reference parameter_ids), `material_id`, `placement`, `source_ids`, `assumption_ids`, `linked_simulation_runs`, `manufacturing_readiness` |
| `experiment.schema.json` | experiment requirement records (future, `theory/recasting`) | translation of a proposal into requirements; LLM-proposed numbers carry `verification_status: proposed` until simulated |
| `simulation_run.schema.json` | immutable run records (future, `results/`) | `run_id`, `code_commit`, `fidelity_tier`, `validation_level`, `is_interface_demo_only`, scenario/geometry/theory/detector versions, generator settings, `software_versions`, `assumption_ids`, `dependency_parameter_ids`, `stale`, `status` ∈ {queued, running, completed, failed, invalidated} |
| `optimization.schema.json` | optimization studies (future, `optimization/`) | variables, objectives, hard/soft constraints, optimizer, seed, stopping criterion, evaluations, `feasibility_rate`, `convergence_evidence`, `uncertainty_treatment`, `high_fidelity_verification_status`, `conclusions_blocked_by` |

Two labels are deliberately independent everywhere they appear (`CLAUDE.md` §1.7):
**G-label** (geometry fidelity, G0 visual placeholder → G5 as-built) and **P-label** (physics
validation, P0 unverified → P5 calibrated on LHμC operations). A beautifully rendered G1 object
can be P0; an analytical P1 check has no geometry at all.

---

## 5. Module map and current status (2026-10-28)

Only `docs/`, `research/`, `schemas/`, `parameters/`, `registries/`, `lhmuc/`, `tools/` and
`tests/` are in scope for Phase 0, and of those several are still being filled by parallel
Phase 0 tasks. Everything else is a placeholder directory with a README.

| Path | Phase 0 status on 2026-10-28 | Entry criterion for real content |
|---|---|---|
| `CLAUDE.md`, `README.md`, `LICENSE`, `LICENSE-DATA`, `CITATION.cff`, `pyproject.toml`, `uv.lock`, `.env.example`, `docker-compose.yml` | present | — |
| `schemas/` | **populated**: 11 schema files (see §4) | — |
| `lhmuc/` | **populated**: `__init__.py`, `__main__.py` (`validate` CLI), `units.py`, `registry.py`, `analytical.py` (P1 audit arithmetic) | — |
| `tools/` | **populated**: `validate_yaml.py`, `build_registries.py`, `merge_research_fragments.py` | — |
| `tests/` | **populated**: `unit/test_schemas.py`, `unit/test_units.py`, `unit/test_registry_integrity.py`, `scientific/test_analytical_checks.py` | — |
| `parameters/` | **being populated** (uncommitted on this date): 18 parameter files in `acceleration/`, `detector/`, `interaction_region/`, `ion_beam/`, `machine/`, `physics_programme/`, `proton_beam/`, `source/` and 5 scenario files (13 scenarios). No `assumptions/` or `materials/` files exist yet. | Phase 0 |
| `research/` | **partially populated**: `source_registry.yaml` (5 uploaded sources), `archived_metadata/` (5 JSON records with SHA-256 and licence), `_fragments/` (8 reconnaissance families × search log / sources / unresolved). The merged `search_log.csv`, `source_conflicts.yaml`, `unresolved_searches.md`, `source_quality_policy.md` referenced by `CLAUDE.md` and the tests are **not yet present**. | Phase 0 |
| `registries/` | **empty** on this date; `parameter_registry.csv` and `assumption_registry.csv` are generated once validation passes; `missing_evidence.csv`, `validation_registry.csv`, `risk_register.csv` are authored. | Phase 0 |
| `references/` | `README.md`; `primary/arXiv-2610.35154v1_Piotrzkowski_LHmuC_DIS2026.pdf` committed (CC BY-NC-ND 4.0 stated on its page 1); `_local/` git-ignored with the 5 uploaded PDFs; empty `accelerator/ detector/ engineering/ software/ theory/` | Phase 0 |
| `docs/` | this file; empty `docs/reports/`. Companion policy documents named in `README.md` (scientific scope, limitations, validation plan, research protocol, synthetic-data, fidelity, uncertainty, security, roadmap, software inventory) are **not yet written**. | Phase 0 |
| `theory/` | README + empty `benchmarks/ importer/ models/ process_builder/ recasting/ ufo/`; proposal records not yet written | Milestone 3 (benchmarks: Phase 0 records only) |
| `physics/` | README only (`analytical/ beam_beam/ beam_dynamics/ luminosity/ muon_decay/ radiation/`) | Milestone 2 |
| `cad/` | README only (`generators/ step/ gdml/ gltf/ meshes/ drawings/ validation/`) | Milestone 2 (G0/G1) |
| `lattice/` | README only (`madx/ xsuite/ bmad/ validation/`) | Milestone 2+ |
| `detector/` | README only (`fast_simulation/ geant4/ bdsim/ backgrounds/ reconstruction/`) | Milestone 2 (fast), 3 |
| `event_generation/` | README only (`madgraph/ pythia/ herwig/ common/`) | Milestone 3 |
| `analysis/` | README only (`selections/ observables/ machine_learning/ statistics/ reports/`) | Milestone 3 |
| `optimization/` | README only (`objectives/ constraints/ gradient/ bayesian/ evolutionary/ reinforcement_learning/ active_learning/ pareto/`) | Milestone 4 |
| `uncertainty/` | README only (`priors/ propagation/ sensitivity/ robustness/ calibration/`) | Milestone 4 |
| `commissioning/` | README only (`virtual_controls/ fault_scenarios/ orbit_correction/ machine_protection/`) | later; no LHμC hardware specs exist |
| `backend/` | README only (`api/ database/ job_scheduler/ workers/`) | Milestone 2 (minimal) |
| `frontend/` | README only (`collider_explorer/ cad_studio/ machine_control/ theory_lab/ event_viewer/ optimization_center/ evidence_graph/`) | Milestone 2 (illustrative) |
| `results/` | `.gitkeep`, `README.md`; contents git-ignored | Milestone 2+ |

What Phase 0 has verified so far (P1, `tests/scientific/test_analytical_checks.py`, inputs from
the uploaded documents): γ(1 TeV μ) = 9464 and τ_lab = 20.8 ms; √s = 2√(E_μE_p) reproduces 5.3 TeV
(1 TeV × 7 TeV) and 7.5 TeV (2 TeV × 7 TeV); the DIS2026 Table 1 peak luminosity 2.1 × 10³⁴ cm⁻²s⁻¹
is reproduced by the naive formula with the Table 1 inputs (4 MHz, 0.07 × 10¹¹ μ⁺, 22 × 10¹¹ p,
σ = 4.8 μm) only if the geometric reduction factor H = 1 is implied, and only with a proton bunch
population ten times the HL-LHC value; for μLHC the naive formula gives 1.14 × 10³⁴ (ERL booster)
and 1.40 × 10³⁴ (μTRISTAN booster), which multiplied by the one-lifetime decay average 0.632 quoted
in the paper reproduce the reported 7.2 × 10³³ and 8.8 × 10³³ to better than 2 %, so no hourglass
reduction is visible in the published values even though the stated optics (β*_y = 0.7 cm against a
centimetre-scale proton bunch) would imply one (open item CONF_LUMI_MODEL_ASSUMPTIONS); the uniform-bending field for
960 GeV/c on a 1 km radius is 3.2 T; the race-track booster survival model gives 81.6 % (16 turns)
and 67.4 % (50 turns) against the paper's 82 % / 67 %. These are *checks of internal consistency*,
not a beam-physics model.

---

## 6. Data flow (text diagram)

```
[Theory proposal]  arXiv paper / workshop deck ─────────────────────────────────────┐
      │  theory/importer (future): proposal.yaml, review_state=extracted            │
      ▼                                                                             │
[Extraction]  manual page-level reads of uploaded PDFs → parameters/**/*.yaml        │
      │       every value: status, source_id, page, table, verbatim quotation        │
      │       conflicts → research/source_conflicts.yaml (kept, never averaged)      │
      ▼                                                                             │
[μ-p process derivation]  theory/process_builder (future): μ⁺p initial state,       │
      │       PDFs, cuts, UFO model → experiment.yaml requirements (status proposed) │
      ▼                                                                             │
[Generation]  event_generation/{madgraph,pythia,herwig} (future) → LHE/HepMC         │
      │       + simulation_run record (seed, versions, assumption_ids, stale flag)   │
      ▼                                                                             │
[Machine + detector simulation]  lattice/* (optics), physics/* (luminosity, decay,   │
      │       beam-beam), detector/{fast_simulation,geant4,bdsim} on geometry C      │
      ▼                                                                             │
[Statistics]  analysis/{selections,observables,statistics} (pyhf likelihoods)        │
      ▼                                                                             │
[Optimization]  optimization/* with hard constraints g_k(θ) ≤ 0; unknown bounds      │
      │       block conclusions (optimization.schema.json: conclusions_blocked_by)   │
      ▼                                                                             │
[Engineering / uncertainty]  cad/* (A→B→C geometry), uncertainty/* propagation,      │
      │       commissioning/* (only if hardware specs exist)                         │
      ▼                                                                             │
[Candidate design + report]  docs/reports/, analysis/reports/ ──────────────────────┘
       every number shown with provenance status, G-label and P-label
```

In Phase 0 only the first two boxes carry real content (extraction into `parameters/` and the
source registry). All later boxes are design intent.

---

## 7. Geometry pipeline (future, Milestone 2 onwards)

```
parameter model (parameters/**, scenario roles)
   → cad/generators  (CadQuery 2.8 / build123d 0.13 on Open Cascade; parameter-driven B-rep)
   → cad/step        (STEP master geometry, one file per component, component.yaml alongside)
   → healing         (Open Cascade shape-fix, tolerance report stored with the component)
   → cad/gltf        (tessellated glTF for the browser, with metadata: component_id, G-label, P-label, provenance of each dimension)
   → simplified simulation geometry  (de-featured solids, material_id per volume)
   → cad/gdml        (GDML via pyg4ometry 1.4.6 for Geant4 / BDSIM)
   → cad/validation  (overlap and volume-consistency checks; results recorded, failures block use)
```

Three representations are kept, with distinct roles and distinct fidelity ceilings:

| Representation | Format / location | Purpose | Fidelity label rule |
|---|---|---|---|
| **A — Engineering master** | STEP B-rep in `cad/step/`, generated from `cad/generators/` | dimensional truth; drawings; manufacturing readiness | carries the component's own G-label (G1 parameterised conceptual at first; G3 only when real engineering input exists; G4/G5 unreachable without a project) |
| **B — Visual** | glTF meshes in `cad/gltf/`, `cad/meshes/` | three.js display in the Collider Explorer / CAD Studio | inherits A's G-label and may **never display a higher one**; purely illustrative objects are G0 and must be drawn as such |
| **C — Simulation** | simplified solids → GDML in `cad/gdml/` | Geant4 / BDSIM transport, beam-induced background | at most G2 "physics-simulation geometry"; must pass `cad/validation` overlap checks before any run record may reference it |

Each component record (`component.schema.json`) references parameter ids for its dimensions, so a
change in `parameters/` marks the derived STEP/glTF/GDML stale rather than silently diverging.
On 2026-10-28 every scenario carries `geometry_fidelity: G0` and no geometry file exists.

---

## 8. Backend and frontend plan (future, Milestone 2 onwards)

Nothing in this section exists. `docker-compose.yml` defines only a `validate` service and keeps
`api`, `worker` and `frontend` commented out; `.env.example` reserves `LHMUC_DATABASE_URL`
(SQLite default) and `LHMUC_API_PORT`.

- **Backend:** FastAPI service exposing the parameter model, scenarios, provenance graph and run
  records; a job scheduler dispatching simulation/optimization jobs to isolated, resource-limited
  **workers**; **SQLite** for development and single-user use, **PostgreSQL** when multi-user or
  concurrent job tracking is needed. Run records are immutable (`simulation_run.schema.json`);
  dependents are marked `stale` when inputs change.
- **Frontend (three.js / React) workspaces** per master prompt §37, mirrored by the
  `frontend/` sub-directories: **Collider Explorer** (3D layout with clickable metadata),
  **CAD Studio**, **Machine Control** (virtual controls, clearly separated from speculative
  devices), **Theory Lab**, **Event Viewer**, **Optimization Center**, **Evidence Graph**.
- **UI invariant:** every displayed value must be visually distinguished as published, derived,
  analogous, synthetic, unknown or user-modified, and must show its G- and P-labels.

---

## 9. Identifier conventions

| Kind | Pattern | Examples in the repository |
|---|---|---|
| `parameter_id` | `UPPER_SNAKE`, `<SUBSYSTEM>_<NAME>_<TAG>`; `TAG` ∈ `DIS2026 \| MULHC \| NUCL \| WP \| DIHIGGS` identifies the source document so ids never collide across documents; species-specific ion records append `_PB`, `_XE`, `_O`, `_NE` | `MACHINE_SQRT_S_DIS2026`, `PROTON_BETA_STAR_MULHC`, `IR_SIGMA_X_IP_MUON_DIS2026`, `DET_NOZZLE_LENGTH_MULHC` |
| subsystem prefixes in use | `MACHINE_`, `SOURCE_`, `ACCEL_` / `ACC_` (both occur: `ACCEL_` in the DIS2026 and Nucleus-Options files, `ACC_` in the μLHC files — to be unified in a later pass), `IR_`, `DET_`, `PHYS_`, `PROTON_`, `ION_` | — |
| `subsystem` enum | `machine, source, acceleration, interaction_region, detector, materials, physics_programme, infrastructure, proton_beam, ion_beam` | — |
| `source_id` | `SRC_ARXIV_<id, dots→underscores>`, `SRC_INDICO_<event>_<contribution>`, `SRC_DOI_<slug>`, `SRC_URL_<slug>`, `SRC_WS1681458_<SPEAKER>_<TOPIC>` (Kraków workshop) | `SRC_ARXIV_2610_35154`, `SRC_ARXIV_2506_15445`, `SRC_WS1681458_DAGLI_NUCLEUS`, `SRC_WS1681458_KHANPOUR_GAMMAGAMMA`, `SRC_WS_LEBOHO_KUMAR_DIHIGGS` |
| `scenario_id` | `UPPER-WITH-HYPHENS`, `<MACHINE>-<DOCUMENT>-<VARIANT>` | `LHMUC-DIS2026-1TEV`, `LHMUC-DIS2026-2TEV`, `MULHC-PTEP2026-MUTRISTAN-BOOSTER`, `MULHC-PTEP2026-ERL-BOOSTER`, `LHMUC-NUCL-MU-PB`, `LHMUC-WP-BASELINE-1TEV`, `LHMUC-DIHIGGS-1TEV` |
| `assumption_id` / `conflict_id` / `proposal_id` | `ASM_…` / `CONF_…` / `PROP_…` | none exist yet |
| run ids | `lhmuc-<topic>-NNNNNN` | none exist yet |
| units | pint-parseable strings via `lhmuc/units.py::UNIT_ALIASES`: `GeV, TeV, um, mm, cm, m, km, MHz, Hz, "cm^-2 s^-1", "fb^-1", "ab^-1", pb, fb, dimensionless, degree, mrad, ms, us, ns, nC, "T/m", "mm mrad", percent, "g/cm^3"` | — |
| provenance status for the five uploads | `reported_lhmuc` only from `PRIMARY_LHMUC` sources (DIS2026 paper and the three workshop decks); μLHC values are `imported_related`; values the μLHC paper itself imports from μTRISTAN / LHeC / HL-LHC are `imported_related` with `applicability.explanation` saying so | — |

---

## 10. Canonical scenario roles

`machine.schema.json` keeps roles free-form but asks for the canonical names below
(role → `parameter_id`; a role whose value the source does not give is listed in `unknown_roles`
instead, never filled with a guess):

```
muon_beam_energy          proton_beam_energy        sqrt_s
peak_luminosity           average_luminosity        integrated_luminosity_per_year
collision_rate            repetition_rate
muon_bunch_population     proton_bunch_population   muon_bunches        proton_bunches
bunch_spacing             sigma_x_ip                sigma_y_ip
beta_x_star_muon          beta_y_star_muon          beta_star_proton
muon_norm_emittance       proton_norm_emittance     muon_bunch_length
main_ring_circumference   booster_circumference     booster_turns
booster_survival          muon_lifetime_lab
```

Document-specific extensions already in use follow the same style and are allowed, e.g.
`sigma_x_ip_proton`, `muon_train_duration`, `booster_injection_energy`, `proton_driver_power`,
`muon_yield_fraction_of_mutristan`, `nozzle_length`, `nozzle_material`, `crossing_angle`,
`ion_species`, `ion_beam_energy_per_nucleon`, `peak_luminosity_per_nucleon`, `sqrt_s_per_nucleon`.
Roles that recur in `unknown_roles` across scenarios (`beta_x_star_muon`, `muon_norm_emittance`,
`muon_bunch_length`, `crossing_angle`, `l_star`, `main_ring_dipole_field`, `nozzle_opening_angle`,
`wall_plug_power`, `cost`) are the Phase 0 missing-evidence list in embryo.

---

## 11. Software environment

- Python 3.13 managed with **uv** (`pyproject.toml`, `uv.lock`); runtime dependencies
  `pyyaml, jsonschema, referencing, pint, numpy, scipy`; dev `pytest, ruff`.
- Commands: `uv run python -m lhmuc validate`, `uv run python tools/build_registries.py [--check]`,
  `uv run python tools/validate_yaml.py <schema> <file>`, `uv run pytest`.
- Candidate tools for later milestones, confirmed installable from PyPI in this environment but
  **not yet adopted or pinned**: xsuite 0.67, cpymad 1.20 (MAD-X), cheetah-accelerator 0.8,
  pythia8mc 8.318, pylhe 2.1, pyhf 0.7.6, cadquery 2.8, build123d 0.13, pyg4ometry 1.4.6, pymoo,
  botorch; MadGraph5_aMC@NLO via launchpad/GitHub. **Not installed:** Geant4, ROOT, LHAPDF, FLUKA.
  Licences will be recorded in `docs/software_inventory.md` when that document is written.

---

## 12. Design decisions log

| Date | Decision | Rationale / consequence |
|---|---|---|
| 2026-10-28 | **Repository layout = master-prompt module tree at the repo root**, every unpopulated directory holding a README that states "not implemented" and its entry criterion. | Architecture visible and reviewable now; stable paths for provenance links and licence split (§2). |
| 2026-10-28 | **YAML is the truth; CSV registries are generated.** `registries/parameter_registry.csv` and `assumption_registry.csv` are written only by `tools/build_registries.py`, which refuses to write when validation errors exist; `--check` runs in the test-suite. `missing_evidence.csv`, `validation_registry.csv`, `risk_register.csv` stay authored. | One place to edit a number; spreadsheets remain available for review without becoming a second source of truth. |
| 2026-10-28 | **Scenarios hold no numbers**, only role → `parameter_id` maps plus `unknown_roles`. | Prevents silent duplication of values; makes "what is unknown for this configuration" a first-class, machine-readable list. |
| 2026-10-28 | **pint for units** (`lhmuc/units.py`), SI internally, explicit conversion at tool boundaries; collider-specific units (`fb^-1`, `cm^-2 s^-1`, `mm mrad`, `T/m`) registered once in `UNIT_ALIASES`. | Every unit string is validated at load time; dimensional checks become part of P1 validation. |
| 2026-10-28 | **Analytical audit arithmetic kept in `lhmuc/analytical.py` for Phase 0**, with tests in `tests/scientific/`; it moves to `physics/analytical/` in Milestone 2. | Phase 0 needs cross-checks of reported values (γ, τ_lab, √s, naive luminosity, Bρ, booster survival, hourglass) but no beam-physics model; keeping them in the core package avoids populating `physics/` prematurely. |
| 2026-10-28 | **Fidelity (G) and validation (P) labels are independent** fields in every schema that describes an object or result. | A rendered placeholder must not look validated; an analytical check must not look like engineering. |
| 2026-10-28 | **PDFs are git-ignored under `references/_local/` unless the licence permits redistribution.** Only arXiv:2610.35154v1 (CC BY-NC-ND 4.0 stated on its page 1) is committed, unmodified, under `references/primary/`; every archived file is described in `research/archived_metadata/*.json` with SHA-256, size, licence and read status. | Respect third-party licences while keeping provenance verifiable by hash. |
| 2026-10-28 | **Snippet-only research mode** for web reconnaissance: arxiv.org, indico.cern.ch, cds.cern.ch, inspirehep.net, pos.sissa.it, doi.org, journals, readthedocs and all CERN hosts are blocked by the session network policy, so web evidence is `access: snippet_only` or `blocked`, may never back `reported_lhmuc`, is capped at confidence `medium`, and every unresolved item is written to the family's `_unresolved.md` under `research/_fragments/`. | Honest about what was actually read; the five uploaded documents are the only `uploaded` sources and the only basis for `reported_lhmuc`. |
| 2026-10-28 | **Reconnaissance is written per family into `research/_fragments/` and merged** by `tools/merge_research_fragments.py` into `research/search_log.csv` and `research/source_registry.yaml`; the five upload entries win on id collision. | Parallel research tasks cannot overwrite each other; the merge is reproducible. |
| 2026-10-28 | **Parameter ids carry a document tag** (`_DIS2026`, `_MULHC`, `_NUCL`, `_WP`, `_DIHIGGS`). | The same physical quantity reported by different documents is kept as separate records (conflicts preserved, `CLAUDE.md` §1.6) and can be compared in `source_conflicts.yaml`. |
| 2026-10-28 | **Code Apache-2.0, data/docs CC BY 4.0**, split by path (`LICENSE`, `LICENSE-DATA`). | Reuse of the evidence database with attribution; standard permissive licence for tooling. |
| 2026-10-28 | **Docker Compose defines only a `validate` service**; `api`, `worker`, `frontend` remain commented. | Nothing claims that a backend or frontend exists before Milestone 2. |

---

## 13. Companion documents

Named in `README.md` and `CLAUDE.md` and planned for Phase 0, but **not present on 2026-10-28**:
`docs/scientific_scope.md`, `docs/limitations.md`, `docs/validation_plan.md`,
`docs/research_protocol.md`, synthetic-data / fidelity / uncertainty / security policy documents,
`docs/roadmap.md`, `docs/software_inventory.md`, `research/source_quality_policy.md`,
`research/unresolved_searches.md`, and the milestone report under `docs/reports/`. When they are
written, this section should be replaced by links.

## 14. Sources cited in this document

- `SRC_ARXIV_2610_35154` — K. Piotrzkowski (HELP4CERN), "LHμC: A high energy, high luminosity
  muon-hadron collider at CERN", PoS DIS2026, arXiv:2610.35154v1 (26 Oct 2026). Committed copy
  `references/primary/arXiv-2610.35154v1_Piotrzkowski_LHmuC_DIS2026.pdf`.
- `SRC_ARXIV_2506_15445` — D. Akturk et al., "μLHC: Antimuon Ring and HL-LHC based μ⁺p Collider",
  PTEP 2026 033C04, arXiv:2506.15445v2 (related machine; git-ignored local copy).
- `SRC_WS1681458_DAGLI_NUCLEUS`, `SRC_WS1681458_KHANPOUR_GAMMAGAMMA`,
  `SRC_WS_LEBOHO_KUMAR_DIHIGGS` — Kraków workshop (Indico 1681458) decks, uploaded; metadata in
  `research/archived_metadata/`.
