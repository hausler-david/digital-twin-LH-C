# CLAUDE.md — working rules for LHμC-VirtualLab

This repository is a research platform for an **evidence-traceable digital twin of the proposed
LHμC muon-proton collider**. Project owner: David Hausler (independent researcher, Czech Republic).
The master project prompt (sections 0–52) is binding; this file condenses the rules every
contributor and every AI session must follow. Read `docs/architecture.md` next.

## 1. Non-negotiable scientific-honesty rules

1. **Never fabricate** collider parameters, dimensions, lattice elements, fields, performance,
   detector efficiencies, radiation levels, event yields, costs, sources, citations, validation
   results, manufacturing readiness or conclusions. "This cannot yet be evaluated because X, Y, Z
   are missing" is a correct result.
2. **`null` means unknown. `0` is a physical value.** Never use one for the other. A parameter
   with `provenance.status: unknown` must have `value: null`.
3. **Every numeric value carries a provenance record** (`schemas/provenance.schema.json`) with one
   status: `reported_lhmuc | derived_lhmuc | imported_related | analogous | analytical_estimate |
   synthetic | scan_variable | unknown`. Reported/imported/analogous values need a `source_id`,
   page and **verbatim quotation**. Derived values need a `derivation` naming input ids.
4. **Synthetic values are ranges or distributions, never bare point estimates**, and require an
   assumption record (`parameters/assumptions/`, `schemas/assumption.schema.json`) stating what was
   searched, why nothing authoritative exists, physical basis, affected outputs and replacement
   evidence. They must be visible in code, configs, UI, plots, exports, run metadata and reports.
5. **Sources are not equal.** Use the category enum and the priority order in
   `research/source_quality_policy.md`. A value seen only in a search snippet (`access:
   snippet_only`) may not back a `reported_lhmuc` status and is capped at confidence `medium`.
6. **Conflicts are preserved, not averaged** (`research/source_conflicts.yaml`): separate
   scenarios or propagated uncertainty, with the decision written down.
7. **Fidelity (G0–G5) and validation (P0–P5) labels are independent** and must be shown
   wherever an object or result is displayed or exported.
8. **Tools, not the LLM, do the science**: optics codes for optics, transport codes for
   material interactions, generators for hard scattering, numerical optimizers for optima. An LLM
   may propose variables, objectives and requirements; numbers come from documented computation.
9. **Never weaken a failing scientific test** without an investigated, documented reason.
10. **Stop and report** instead of inventing when a model is unspecified, a parameter is
    missing, sources conflict materially, a benchmark cannot be reproduced, geometry is invalid,
    constraints are incomplete, statistics are insufficient or a surrogate is out of domain.

## 2. Single source of truth

- Parameter records: `parameters/**/*.yaml` (validated by `schemas/provenance.schema.json`).
- Scenarios: `parameters/machine/scenarios.yaml` (reference parameter ids only; no numbers).
- Assumptions: `parameters/assumptions/*.yaml`. Materials: `parameters/materials/*.yaml`.
- Sources: `research/source_registry.yaml`; archived-file metadata: `research/archived_metadata/`.
- Conflicts: `research/source_conflicts.yaml`. Proposals: `theory/benchmarks/*/proposal.yaml`.
- CSV registries in `registries/` are **generated** (`uv run python tools/build_registries.py`)
  except the authored `missing_evidence.csv`, `validation_registry.csv`, `risk_register.csv`.
- Units: pint-parseable strings (`lhmuc/units.py`); SI internally, explicit conversion at tool
  boundaries.

## 3. Identifier conventions

- `parameter_id`: `UPPER_SNAKE`, prefixed by subsystem and scenario tag where scenario-specific,
  e.g. `MACHINE_MU_BEAM_ENERGY_DIS2026`, `IR_Q1_GRADIENT`, `DET_NOZZLE_OPENING_ANGLE`.
- `source_id`: `SRC_ARXIV_<id with dots as underscores>`, `SRC_INDICO_<event>_<contribution>`,
  `SRC_DOI_<slug>`, `SRC_URL_<slug>`, `SRC_WS1681458_<speaker>_<topic>` for the Kraków workshop.
- `scenario_id`: `LHMUC-DIS2026-1TEV`, `MULHC-PTEP2026-ERL-BOOSTER`, … (uppercase, hyphens).
- `assumption_id`: `ASM_…`; `conflict_id`: `CONF_…`; `proposal_id`: `PROP_…`; run ids
  `lhmuc-<topic>-NNNNNN`.

## 4. How to add things

- New parameter: add a record to the right `parameters/<subsystem>/` file, run
  `uv run python -m lhmuc validate`, then `uv run python tools/build_registries.py` and
  `uv run python tools/sync_parameters_extracted.py`, then `uv run pytest`. The validator rejects confidence above the
  caps of `research/source_quality_policy.md` §4, any P1 label whose `validation.methods`/`check_ids` name no
  existing test, and any scenario `validation_level` above the lowest level of its role records
  (`tools/apply_confidence_caps.py`, `tools/apply_validation_levels.py`, `tools/apply_scenario_levels.py` lower them).
- New source: add to `research/source_registry.yaml` with `access`, licence and SHA-256 if
  archived; add the query rows to `research/search_log.csv`; record what remains unresolved in
  `research/unresolved_searches.md`.
- New synthetic value: assumption record first, parameter record second, sensitivity entry third.
- Reported value arrives for a synthetic parameter: mark the assumption `superseded_by_evidence`
  with `superseded_by`, re-point every scenario slot to the reported id, keep the `_SYN` record only
  as a scan variable (see `docs/synthetic_data_policy.md`, supersession section).
- New result: immutable run record (`schemas/simulation_run.schema.json`); never overwrite; mark
  dependents stale when inputs change.

## 5. Security

Uploaded model files and external repositories are untrusted input: inspect before executing,
run in isolated environments with pinned dependencies and checksums, never let uploads reach
credentials. Do not commit secrets (`.env` is git-ignored). Document third-party licences in
`docs/software_inventory.md`.

## 6. Session etiquette

- After every substantial task, produce the §49 status report (Completed / Evidence used /
  Assumptions / Validation / Limitations / Results / Next highest-value action).
- Do not claim a digital twin, engineering accuracy or validation that has not been performed.
- Commit on the designated branch with clear messages; push with `git push -u origin <branch>`.
