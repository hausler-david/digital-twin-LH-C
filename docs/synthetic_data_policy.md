# LHμC-VirtualLab — Synthetic-data policy

**Document date:** 2026-10-28 · **Project phase:** Phase 0 (evidence and feasibility audit) ·
**Owner:** David Hausler · **Status:** binding policy for every synthetic (assumed) value, every
analogous value adopted as a stand-in, and every synthetic demonstration event sample.

Binding rules implemented here: `CLAUDE.md` §1.1 (never fabricate), §1.2 (`null` means unknown,
`0` is a physical value), §1.4 (synthetic values are ranges or distributions with an assumption
record and must be visible everywhere), §1.10 (stop and report instead of inventing), §2 (single
source of truth) and §4 ("New synthetic value: assumption record first, parameter record second,
sensitivity entry third"). Companion documents: `docs/uncertainty_policy.md` §1.3 (how synthetic
bands are propagated), `docs/validation_plan.md` §1 rule 2 (a synthetic input confers at most P1),
`docs/fidelity_policy.md` (G/P labels), `docs/limitations.md` §8 (statements the platform must not
make).

**State of the repository on 2026-10-28:** `parameters/assumptions/` exists and is **empty**;
`uv run python -m lhmuc validate` reports `assumptions: 0` and no parameter with
`provenance.status: synthetic`. The one record with no value is `IR_CROSSING_ANGLE_DIS2026`
(`status: unknown`, `value: null`). This document therefore describes the procedure that *will*
govern the first synthetic value; the worked example in §4 is a template that passes the schema,
not a record that has been adopted.

---

## 1. Definitions

| Term | Meaning in this project |
|---|---|
| **Synthetic value** | A number (or band) that no source reports for the LHμC, that cannot be derived from reported LHμC values, and that the project nevertheless needs in order to build or run a model. Provenance status `synthetic` (`schemas/provenance.schema.json#/$defs/provenance_status`). |
| **Assumption record** | The mandatory companion of every synthetic value: a YAML record in `parameters/assumptions/*.yaml` validated by `schemas/assumption.schema.json`, `assumption_id` pattern `^ASM_[A-Z0-9_]+$`. |
| **Analogous value** | A number read in full from a source describing a *different* machine or device (IMCC, MAP, J-PARC, LHeC, HL-LHC …) and used as a stand-in. Provenance status `analogous` (needs `source_id`, page and verbatim quotation). It is **not** synthetic, but when it is adopted as an input to an LHμC model it also needs an assumption record with `status: analogous_value`, because the applicability to LHμC is itself an assumption. |
| **Unknown** | No value exists and none is assumed: `status: unknown`, `value: null`. This is the default and is always acceptable (`CLAUDE.md` §1.1: "This cannot yet be evaluated because X, Y, Z are missing" is a correct result). |
| **Scan variable** | A quantity deliberately varied over `allowed_range` in a study; `status: scan_variable`, no single value. Not synthetic: it does not claim to represent the LHμC design. |
| **Synthetic demo sample** | A generated event or run dataset whose only purpose is to exercise an interface (viewer, plot, export); flagged `is_interface_demo_only: true` in `schemas/simulation_run.schema.json` (§7 below). |

Distinctions that must never blur: *synthetic* ≠ *unknown* (a synthetic input has a declared band;
an unknown has `null`); *synthetic* ≠ *analogous* (analogous has a verbatim quotation from a
real document); *synthetic* ≠ *analytical_estimate* (the latter has a `derivation` from registry
inputs).

---

## 2. When a synthetic value is permitted

A synthetic value may be introduced **only** when all of the following hold:

1. **The quantity is required.** A concrete model, geometry, scan or test cannot be built without
   it, and the deliverable that needs it is named (e.g. "G1 nozzle placeholder in `cad/`").
   A synthetic value is never added "for completeness" of a table.
2. **The search is exhausted and documented.** All five uploaded primary and related documents
   (`SRC_ARXIV_2610_35154`, `SRC_ARXIV_2506_15445`, `SRC_WS1681458_DAGLI_NUCLEUS`,
   `SRC_WS1681458_KHANPOUR_GAMMAGAMMA`, `SRC_WS_LEBOHO_KUMAR_DIHIGGS`) have been checked for the
   quantity, the result is written into `search_summary`, and the fetch attempts (including
   blocked hosts) are recorded. A value that *is* reported somewhere but has not yet been fetched is
   `pending_fetch`/`unknown`, not synthetic.
3. **No derivation exists.** The quantity cannot be computed from reported LHμC values by a
   documented formula (that would be `derived_lhmuc` or `analytical_estimate` with a `derivation`).
4. **A physical basis for a band exists.** Bounds can be argued from physics, engineering practice
   or an analogous system and are written down in `physical_basis`. If no bound can be argued, the
   quantity stays `unknown`.
5. **The use is screening, placeholder or sensitivity.** Permitted uses are: G0/G1 placeholder
   geometry; order-of-magnitude feasibility estimates; sensitivity and robustness scans in which
   the synthetic input is varied over its band; defining optimisation variable bounds that are
   explicitly labelled as assumed; interface demonstration (§7). Not permitted: any output that
   would be read as a design result, a validation result, a cost, a radiation level, a yield or a
   detector efficiency for the LHμC.
6. **Replacement is defined.** The record names which document or measurement would retire it
   (`replacement_evidence`).

Cases that are **never** synthetic: values that a source reports but that this project disagrees
with (record the conflict in `research/source_conflicts.yaml` once it exists, never replace the
number); dimensions of an existing device (HL-LHC proton beam, LHeC ERL, J-PARC source) — those
are `imported_related` or `analogous` with a quotation, or `unknown`; physical constants.

---

## 3. The mandatory procedure (11 steps) before a synthetic value exists in the registry

The order is fixed by `CLAUDE.md` §4: assumption record first, parameter record second,
sensitivity entry third. A pull request that adds a `status: synthetic` parameter without steps
1–7 completed is rejected; `uv run python -m lhmuc validate` already fails on steps 7 and 8
(`lhmuc/registry.py::cross_check`: "synthetic parameter without assumption record", "synthetic
parameter must carry an allowed_range (no bare point values)").

1. **State the need.** Name the deliverable, model or test that is blocked without the value and
   why `null` is not an acceptable input for it. If the deliverable can proceed with `null`
   (reporting "cannot be evaluated"), stop here.
2. **Search the uploads page by page.** Record, per source, the page/section inspected and what
   was found (including "named but no number", as the DIS2026 proceedings do for the nozzle).
3. **Search beyond the uploads and log it.** Record every query and fetch attempt with its
   `access` outcome (`fetched`, `snippet_only`, `blocked`, `pending_fetch`) in the research logs
   (`research/_fragments/*_search_log.csv` on 2026-10-28; `research/search_log.csv` once merged).
   A `snippet_only` hit may inform the band but may never be the value itself and is capped at
   confidence `medium` (`CLAUDE.md` §1.5).
4. **Rule out derivation.** Write down why no formula from registry parameters gives the quantity
   (or, if one does, record an `analytical_estimate` instead and stop).
5. **Establish the physical basis of the bounds.** Each bound must have a reason (kinematics,
   acceptance, material limit, analogue scaled by a stated factor). Write the bounds as a band,
   choose the distribution from `{uniform, log_uniform, triangular, gaussian, discrete_set,
   range_only}` and justify the choice; use `range_only` when no distribution can be argued
   (propagated as interval bounds, `docs/uncertainty_policy.md` §3.1). A band narrower than a
   factor of two around a snippet-only analogue, or any band that collapses to a point, is not
   accepted.
6. **Identify analogues honestly.** List each analogous system with its access mode and whether
   it was read in full; state why the analogy is imperfect.
7. **Write the assumption record** (`parameters/assumptions/<topic>.yaml`, schema
   `assumption.schema.json`, §4 below) with `sensitivity_analysis: planned` and
   `date_added`. Validate: `uv run python tools/validate_yaml.py assumption <file>`.
8. **Write the parameter record** with `provenance.status: synthetic`,
   `extraction_method: assumption_record`, `source: null`, `assumption_id` pointing at step 7,
   `allowed_range` equal to the band, `uncertainty: {type: interval, lower, upper}`, confidence
   `low` (or `none`), `validation.level: P0`, and a `notes` field beginning with `SYNTHETIC`.
   The `value` field holds a reference point *inside* the band (the mode or centre) because the
   loader forbids `null` for any status other than `unknown`/`scan_variable`; the reference point is
   a tooling convenience, never an estimate, and the `uncertainty.note` must say so.
9. **Register the dependents.** Every parameter, component, scenario or run that will consume the
   value lists it in `dependencies` / `assumption_ids`, so that the band's retirement marks them
   stale. Scenarios that lack the quantity keep it in `unknown_roles` until the synthetic record is
   explicitly attached; attaching it changes the scenario `status` to `synthetic_scan` if the
   synthetic input is varied.
10. **Add the sensitivity entry and the missing-evidence row.** The quantity is listed in the
    authored `registries/missing_evidence.csv` (to be created; see `CLAUDE.md` §2) with the
    replacement evidence, and a sensitivity study over the band is scheduled under
    `uncertainty/sensitivity/` (placeholder on 2026-10-28). `sensitivity_analysis` moves to `done`
    only when the study's run record exists.
11. **Validate, regenerate, test, report.** `uv run python -m lhmuc validate`,
    `uv run python tools/build_registries.py` (writes `registries/assumption_registry.csv`),
    `uv run pytest`; then list the new assumption under *Assumptions* in the §49 status report of
    the session that introduced it.

Retirement: when evidence arrives, the parameter record is rewritten with the evidential status
and quotation, the assumption record's `status` is set to `proposed_not_adopted` (kept for the
audit trail, never deleted), and every dependent is marked stale and re-run.

---

## 4. The assumption record and a full worked example

### 4.1 Schema (`schemas/assumption.schema.json`)

Top-level key `assumptions:` (list). Required fields: `assumption_id`, `parameter_id`, `status`
(`synthetic_assumption | analogous_value | proposed_not_adopted`), `reason_required`,
`search_summary` (≥ 1 entry), `reason_authoritative_value_missing`, `synthetic_model`
(`distribution`, `unit` required; `minimum`, `maximum`, `mode`, `mean`, `sigma`, `values`
optional), `physical_basis` (≥ 1), `applicability`, `affected_outputs` (≥ 1),
`replacement_evidence`, `sensitivity_analysis` (`not_started | planned | done`), `date_added`.
Optional: `sources_inspected`, `analogous_systems`, `notes`. No other keys are allowed.

### 4.2 Worked example: `DET_NOZZLE_OPENING_ANGLE`

Why this quantity: the DIS2026 proceedings name the nozzle but give no size ("the so-called
*nozzle* should be located inside the LHμC detector in the direction of incoming muons [27], its size
has to be carefully optimised", `SRC_ARXIV_2610_35154` p. 5 §4); the μLHC paper gives a length and
materials but no angle ("the 6-meter-long tungsten shielding cone", "The shielding tungsten nozzle
cladded with borated polyethylene is placed to the muon coming side", `SRC_ARXIV_2506_15445`
pp. 13–14 §2.4; "19 % and 81 %" deposited/passing energy for 1 TeV muons, p. 14). The registry
already holds the μLHC facts as `imported_related` records (`DET_NOZZLE_LENGTH_MULHC`,
`DET_NOZZLE_MATERIAL_MULHC`, `DET_NOZZLE_CLADDING_MULHC`, `DET_NOZZLE_DEPOSITED_FRACTION_MULHC`
in `parameters/detector/mulhc_ptep2026_detector.yaml`), and all 13 scenarios list
`nozzle_opening_angle` under `unknown_roles`. The IMCC/MAP analogue (10° outer inclination,
INERMET180 + borated polyethylene, tip ≈ 6 cm from the IP) was seen **only in search snippets** and
is therefore used only to centre the band, with confidence capped at `medium`.

The two records below were validated on 2026-10-28 with
`uv run python tools/validate_yaml.py assumption …` and `… provenance …` (0 schema errors each).
They are **not** in `parameters/`; adopting them requires steps 9–11 of §3.

```yaml
# parameters/assumptions/detector_nozzle.yaml  (template, not adopted)
assumptions:
  - assumption_id: ASM_DET_NOZZLE_OPENING_ANGLE
    parameter_id: DET_NOZZLE_OPENING_ANGLE
    status: synthetic_assumption
    reason_required: >-
      A cone half-angle is needed to build the G0/G1 parameterised nozzle placeholder in cad/ (Milestone 2)
      and to estimate the backward angular acceptance lost to the shielding. Without it the nozzle cannot be
      drawn or its acceptance cost estimated at all.
    search_summary:
      - "SRC_ARXIV_2610_35154 p.5 §4: the nozzle is named and 'its size has to be carefully optimised'; no dimension, angle or material is given."
      - "SRC_ARXIV_2506_15445 p.13-14 §2.4: 6-meter-long tungsten shielding cone cladded with borated polyethylene; 19 % / 81 % deposited / passing energy for 1 TeV muons; no angle, radius or distance to the IP."
      - "SRC_WS1681458_DAGLI_NUCLEUS, SRC_WS1681458_KHANPOUR_GAMMAGAMMA, SRC_WS_LEBOHO_KUMAR_DIHIGGS: no numeric nozzle parameter."
      - "A. Kilic et al., 'Nozzle design studies for mu+p collider detector', LHmuC workshop contribution (ref. [27] of arXiv:2610.35154, indico event 1681458 contribution 7263330): identified, not obtained (indico.cern.ch blocked in this session)."
      - "IMCC / MAP muon-collider nozzle literature: seen only as search snippets (access snippet_only); not read in full."
    sources_inspected:
      - SRC_ARXIV_2610_35154
      - SRC_ARXIV_2506_15445
      - SRC_WS1681458_DAGLI_NUCLEUS
      - SRC_WS1681458_KHANPOUR_GAMMAGAMMA
      - SRC_WS_LEBOHO_KUMAR_DIHIGGS
    reason_authoritative_value_missing: >-
      No LHmuC nozzle geometry has been published. The DIS2026 proceedings defer the design to a dedicated
      workshop contribution that could not be fetched; the muLHC paper gives only the cone length and
      materials used in its Geant4/FLUKA energy-loss study.
    synthetic_model:
      distribution: uniform
      minimum: 5
      maximum: 20
      mode: null
      mean: null
      sigma: null
      values: []
      unit: degree
    physical_basis:
      - "The nozzle must shadow the innermost tracker from electrons and photons produced by decays of the incoming TeV muon beam, so its outer surface must subtend a polar angle of at least a few degrees around the incoming-muon axis."
      - "The nozzle removes acceptance in the backward (incoming-muon) hemisphere where, according to SRC_ARXIV_2506_15445 p.13, 'the scattered parton (e.g., jets) and muon are mostly going toward the backward direction'; angles well above ~20 degrees would remove a large part of the physics acceptance and are therefore excluded from the screening band."
      - "The band 5-20 degrees brackets the only known analogue value (10 degrees, snippet-only) by a factor of two in each direction, which is the minimum spread this policy allows for a value with no LHmuC-specific evidence."
    analogous_systems:
      - "muLHC (SRC_ARXIV_2506_15445, uploaded, read in full): 6-meter-long tungsten shielding cone cladded with borated polyethylene on the muon-coming side; angle not stated."
      - "IMCC / MAP muon-collider nozzle (snippet_only, unverified, confidence capped at medium): INERMET180 tungsten alloy with borated polyethylene cladding, tip about 6 cm from the IP, about 10 degree outer inclination. Mu+mu- collider nozzles are symmetric on both sides; at LHmuC only the incoming-muon side needs one."
    applicability: >-
      screening_only. Valid for G0/G1 placeholder geometry, order-of-magnitude acceptance and BIB estimates, and
      sensitivity scans. Not valid for engineering, radiation-protection or detector-performance claims. Applies to
      every LHmuC scenario until a scenario-specific value exists.
    affected_outputs:
      - "Backward polar-angle acceptance of the tracker and calorimeters (incoming-muon side)."
      - "Beam-induced-background fluence in the vertex detector and inner tracker."
      - "Nozzle volume, mass and instrumented-volume loss in cad/ components."
      - "Any physics-benchmark acceptance (e.g. di-Higgs b-jets, two-photon forward muon) evaluated with a detector model that includes the nozzle."
    replacement_evidence: >-
      Kilic et al., LHmuC workshop contribution 7263330 (nozzle design studies), read in full; the HELP4CERN
      White Paper when published; or an IMCC nozzle paper read in full. Any of these replaces this record and the
      parameter status becomes reported_lhmuc, imported_related or analogous as appropriate.
    sensitivity_analysis: planned
    date_added: "2026-10-28"
    notes: >-
      Definition used here: polar angle of the nozzle's outer conical surface measured from the incoming-muon
      beam axis (cone half-angle). Replace this record, do not edit the range, when evidence arrives.
```

The matching parameter record (step 8), shown in the compact style used in `parameters/`:

```yaml
# parameters/detector/lhmuc_nozzle_synthetic.yaml  (template, not adopted)
parameters:
  - parameter_id: DET_NOZZLE_OPENING_ANGLE
    name: Shielding-nozzle outer cone half-angle (synthetic screening band)
    symbol: theta_nozzle
    subsystem: detector
    scenario: null
    value: 10
    unit: degree
    uncertainty: {type: interval, lower: 5, upper: 20, unit: degree, note: "Uniform synthetic band; value is the band centre used only when a single sample is required and is not an estimate."}
    allowed_range: {min: 5, max: 20, unit: degree, basis: "ASM_DET_NOZZLE_OPENING_ANGLE"}
    provenance:
      status: synthetic
      extraction_method: assumption_record
      source: null
      derivation: null
      applicability: {category: screening_only, scenario: null, explanation: "No LHμC nozzle geometry is published; band justified in ASM_DET_NOZZLE_OPENING_ANGLE. Screening and placeholder geometry only."}
      confidence: low
      assumption_id: ASM_DET_NOZZLE_OPENING_ANGLE
    validation: {level: P0, methods: ["dimensional check"], check_ids: [], notes: "Synthetic input; may confer at most P1 on dependents."}
    dependencies: []
    date_added: "2026-10-28"
    responsible_module: parameters/detector
    notes: "SYNTHETIC. Half-angle of the outer cone surface from the incoming-muon axis. Not a reported, derived or analogous value."
```

What the example deliberately does **not** do: it does not quote a nozzle angle for the LHμC; it
does not promote the snippet-only 10° to a value; it does not state the nozzle length for LHμC
(the 6 m is μLHC, kept in its own `imported_related` record); and it does not attach itself to any
scenario.

---

## 5. Visibility requirements

A synthetic input must be recognisable as such at every point where it can be seen
(`CLAUDE.md` §1.4). Concretely:

| Layer | Requirement | Where it is (or will be) enforced |
|---|---|---|
| **YAML / code** | `provenance.status: synthetic`, `assumption_id`, `allowed_range`, `notes` starting with `SYNTHETIC`. Loaders expose the status alongside the value; no API returns a synthetic number without its status and assumption id. | `lhmuc/registry.py::cross_check` (present); backend API (future, `backend/`) |
| **CLI** | `uv run python -m lhmuc validate` prints the section "synthetic parameters (range only, see parameters/assumptions)" listing every synthetic id with its assumption id. | present |
| **Generated registries** | `registries/parameter_registry.csv` carries `provenance_status`, `allowed_range` and `assumption_id` columns; `registries/assumption_registry.csv` lists every record with distribution, bounds and `sensitivity_analysis`. | `tools/build_registries.py` (present; CSVs not yet generated on 2026-10-28) |
| **Configs** | Any run or optimisation configuration that resolves a synthetic input must copy the `assumption_id` into the run record's `assumption_ids` and the parameter id into `dependency_parameter_ids`. A config that hard-codes the number without the ids is invalid. | `schemas/simulation_run.schema.json`, `schemas/optimization.schema.json` (present); runners (future) |
| **UI** | Every displayed value is visually classed as published / derived / analogous / **synthetic** / unknown / user-modified (`docs/architecture.md` §8, `frontend/README.md`). Synthetic values use a distinct colour **and** a distinct icon or hatch pattern (colour alone is not sufficient for accessibility), show the band rather than a point by default, and link to the assumption record. 3D objects whose dimensions depend on a synthetic input are drawn with a distinct material/outline and carry a "SYNTHETIC DIMENSION" badge in their metadata panel next to the G/P labels. | future, Milestone 2 |
| **Plots** | A plot whose inputs include a synthetic value shows the band (shaded region or error band, never a single line only), prints the assumption ids in the caption or legend, and has the word "synthetic" in the figure annotation. | future; required by `docs/uncertainty_policy.md` §4 |
| **Exports** | CSV/JSON/STEP/glTF/GDML exports carry the provenance status and assumption ids per value or per component; glTF metadata includes the assumption ids of synthetic dimensions; exports that cannot carry metadata (plain images) get a sidecar `.provenance.json` or a visible watermark. | future |
| **Run metadata** | `assumption_ids` and `dependency_parameter_ids` are required fields of the run record; results that depend on a synthetic input display the assumption id and are capped at P1 (`docs/validation_plan.md` §1 rule 2). | schema present |
| **Reports** | Every milestone/status report lists synthetic inputs in an *Assumptions* section with band, assumption id and affected outputs, and states which results depend on them. | `CLAUDE.md` §6 |

---

## 6. Prohibited behaviours

1. Introducing a synthetic value without an assumption record, or an assumption record without a
   band (`minimum`/`maximum`, `values` or `sigma`) — the loader rejects both.
2. Writing a synthetic point estimate (`allowed_range: null`, or min = max) — rejected.
3. Using `value: 0` or `value: null` to mean "assumed" — `0` is physical, `null` is unknown.
4. Promoting a search-snippet number to a value, or giving it confidence above `medium`.
5. Silently replacing a reported value one disagrees with — record a conflict instead.
6. Narrowing, re-centring or deleting a band because a downstream result "looks better".
7. Averaging the band away in a result, or reporting the centre of the band as "the value".
8. Letting a synthetic input confer a validation level above P1 on anything, or a geometry
   fidelity above G1 on a component whose dimension depends on it.
9. Presenting a synthetic-dependent output in any medium (code comment, docstring, UI, plot,
   export, report, conversation) without the assumption id and the word "synthetic".
10. Having an LLM "estimate" a value in conversation and committing it as anything other than a
    synthetic band with a full record (`docs/uncertainty_policy.md` §6: the LLM may propose
    variables and bounds; numbers come from documented computation or documented assumption).
11. Deleting a retired assumption record (set `status: proposed_not_adopted` instead).
12. Attaching a synthetic input to a scenario while leaving the scenario `status: reported`.

---

## 7. Synthetic demonstration event samples (interface-only)

Interfaces (Event Viewer, Theory Lab plots, export pipelines) need test data before any
physics-grade generator run exists. Such data is permitted only under the following rules:

- The run record has `is_interface_demo_only: true` (`schemas/simulation_run.schema.json`:
  "true for synthetic demonstration samples; such runs are excluded from scientific reports"),
  `fidelity_tier: A_analytical` or `B_fast_simulation` at most, `validation_level: P0`, and
  `machine_scenario_id` set to the scenario whose kinematics it mimics so the mismatch is explicit.
- The `run_id` topic segment is `demo` (`lhmuc-demo-NNNNNN`), the `process` field starts with
  `DEMO:`, and `warnings` contains the sentence "Interface demonstration sample; not a physics
  result."
- The sample carries no cross section (`cross_section: null`) and no event weights that could be
  read as a prediction; if a generator was used, its settings are recorded anyway.
- Every file produced for or from such a run is named with the prefix `demo_` and stored under
  `results/` only with its run record; it is never placed in `references/` or `parameters/`.
- The UI shows a persistent "DEMO SAMPLE — not a physics result" banner while a demo run is loaded,
  using the same colour/icon class as synthetic values, and excludes demo runs from any statistics,
  comparison or optimisation view.
- Demo runs are excluded from `docs/reports/`, from registries of results, from P-level
  bookkeeping and from any statement about LHμC physics; `tools/build_registries.py` and future
  report generators filter on `is_interface_demo_only`.
- A demo sample is retired (status `invalidated`) as soon as a real run for the same interface
  exists.

On 2026-10-28 no event sample of any kind exists (`results/README.md`; `docs/limitations.md` §8
item 8).

---

## 8. Sources cited

- `SRC_ARXIV_2610_35154` — K. Piotrzkowski (HELP4CERN Study Group), "LHμC: A high energy, high
  luminosity muon-hadron collider at CERN", PoS DIS2026, arXiv:2610.35154v1, 7 pp., uploaded;
  nozzle statement p. 5 §4; ref. [27] A. Kilic et al., LHμC workshop contribution (not obtained).
- `SRC_ARXIV_2506_15445` — D. Akturk et al., "μLHC: Antimuon Ring and HL-LHC based μ⁺p Collider",
  PTEP 2026 033C04, arXiv:2506.15445v2, 24 pp., uploaded; nozzle §2.4 pp. 13–14, Figs. 8–10.
- `SRC_WS1681458_DAGLI_NUCLEUS`, `SRC_WS1681458_KHANPOUR_GAMMAGAMMA`, `SRC_WS_LEBOHO_KUMAR_DIHIGGS`
  — Kraków LHμC workshop slide decks, uploaded; inspected for nozzle numbers, none found.
- IMCC/MAP nozzle numbers (10°, INERMET180, 6 cm tip distance): search snippets only, no
  `source_id`, not citable as evidence.
