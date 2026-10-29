# LHμC-VirtualLab — Uncertainty policy

**Document date:** 2026-10-28 · **Addendum:** 2026-10-29 (§2.1, §8a; dated notes in §1, §6–§8) ·
**Project phase:** Phase 0 (evidence and feasibility audit) ·
**Owner:** David Hausler · **Status:** policy. It fixes how uncertainty is represented, propagated
and reported from Milestone 2 onwards; on 2026-10-28 only the representation (§1–§2) is
implemented in schemas and registries. `uncertainty/` contains a README and empty
`priors/ propagation/ sensitivity/ robustness/ calibration/` directories (entry criterion:
Milestone 4). No propagation, surrogate or probabilistic result exists.

Binding rules: `CLAUDE.md` §1.2 (null ≠ 0), §1.3 (provenance on every number), §1.4 (synthetic
values are ranges with an assumption record), §1.5 (source quality, snippet cap), §1.6 (conflicts
preserved, not averaged), §1.8 (tools, not the LLM, do the science). Companion documents:
`docs/validation_plan.md`, `docs/architecture.md`.

---

## 1. Representation of uncertainty

### 1.1 The `uncertainty` object on every parameter record

`schemas/provenance.schema.json#/$defs/uncertainty` is a required field of every parameter
(it may be `null` only for categorical records). Allowed `type` values and when to use them:

| `type` | Fields | Use | Records in the registry on 2026-10-28 (796 parameters, counted with `lhmuc.registry.load_all`) |
|---|---|---|---|
| `gaussian_sigma` | `value`, `unit`, `note` | the source states a 1σ (or clearly symmetric) error, or the value is a documented statistical result | 6 records |
| `interval` | `lower`, `upper`, `unit`, `note` | the source gives a range ("β*_μ ≈ 7–15 cm", "5.5–7.9 μm"); bounds are transcribed, never converted to a σ | 10 records (Nucleus-Options relaxed optics) |
| `relative_fraction` | `value` (fraction, not percent), `note` | the source states a relative precision, or an analytical estimate carries a documented relative error | 4 records |
| `order_of_magnitude` | `note` (mandatory, quoting the wording) | the source says "close to 10³⁴", "about 3 (6) km", "~", "approximately" | 45 records |
| `not_stated` | `note` optional | the source prints digits with no uncertainty — **the default for every table value**; it means "precision unknown", not "exact" | 704 records (27 further categorical records carry `null`) |

*Counts at commit `104073c` (2026-10-29, 5601 parameters):* `gaussian_sigma` 93, `interval` 53,
`relative_fraction` 140, `order_of_magnitude` 75, `not_stated` 5213, `null` (categorical) 27. The
growth of `gaussian_sigma` comes mainly from measurements with stated errors in the uploaded
source-chain papers — Beare 2020 (29 records), Bakule 2013 (13), Aritome 2024 (10), e.g. 0.52 ± 0.01
in `SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAKULE2013` and 0.655 ± 0.018 in
`SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020` — and from the Gaussian-fit parameters with their printed standard errors in the Kilic
nozzle-study insets (16); that of `relative_fraction` almost entirely from the MadGraph scale and PDF
uncertainties of the muon-ion collider tables (132 of 140). Rule 1 below applies unchanged.

Rules:

1. `not_stated` is never silently upgraded. A table value "5.3 TeV" keeps `not_stated`; the
   rounding (5.29 → 5.3) is noted in `validation.notes`, not invented as a σ.
2. `order_of_magnitude` values must not enter a numerical propagation as points; they enter as a
   log-uniform band of at least one decade centred on the quoted value, declared in an assumption
   record (§1.3), or the propagation reports them as unquantified.
3. Converting an `interval` into a distribution for propagation requires an assumption record
   naming the distribution (`uniform` by default). The parameter record itself keeps the interval.
4. A parameter whose `provenance.status` is `unknown` has `value: null` and no uncertainty object
   can rescue it: it is a *missing input*, listed in `scenario.unknown_roles` and in
   `registries/missing_evidence.csv` (authored; not yet present on 2026-10-28), and every result
   depending on it is blocked or carries an explicit assumption.

### 1.2 `allowed_range` and `scan_variable`

`allowed_range {min, max, unit, basis}` is the design-space bound used by optimisation and
scans; it is distinct from the measurement/statement uncertainty above. `scan_variable` records
have no single value and are varied over `allowed_range`; they are never averaged into a point.

### 1.3 Synthetic inputs (`status: synthetic`) and assumption records

Every synthetic input is a range or a distribution (`CLAUDE.md` §1.4), never a bare point. The
assumption record (`schemas/assumption.schema.json`, `parameters/assumptions/*.yaml`, none written
yet) carries `synthetic_model.distribution ∈ {uniform, log_uniform, triangular, gaussian,
discrete_set, range_only}` with `minimum`, `maximum`, `mode`, `mean`, `sigma` or `values`
*(2026-10-29: 20 records exist in `parameters/assumptions/phase0_assumptions.yaml`; those overtaken
by uploaded evidence are marked `superseded_by_evidence` and their `_SYN` parameters survive only as
scan variables, `docs/synthetic_data_policy.md`)*, plus
`reason_required`, `search_summary`, `reason_authoritative_value_missing`, `physical_basis`,
`analogous_systems`, `affected_outputs`, `replacement_evidence`, `sensitivity_analysis
∈ {not_started, planned, done}`. `range_only` means the band is physical but no distribution can
be justified; such inputs are propagated as interval bounds (§3.1), not sampled.

### 1.4 Uncertainty on results

`schemas/simulation_run.schema.json` has `cross_section` and `cross_section_uncertainty` (statistical
and, where computed, scale/PDF components recorded separately), `software_versions`,
`random_seed`, `assumption_ids` and `dependency_parameter_ids`, so every result uncertainty can be
traced to its inputs. `schemas/optimization.schema.json` requires a free-text
`uncertainty_treatment` and a `conclusions_blocked_by` list.

---

## 2. Uncertain inputs (master prompt §27 mapped to the registry)

The classes of uncertain input named by the master prompt are listed below with what the
registry holds on 2026-10-28. "Reported" means a source states it (status `reported_lhmuc` or
`imported_related` with page and quotation); "unknown" means `value: null`. Snippet-only leads are
marked and are **not** registry values.

| Input class | What is known (source) | Uncertainty character | Representation |
|---|---|---|---|
| Muon source yield | DIS2026: μ⁺ yields "at a level of 5% of the ones in the muTRISTAN proposal", 4 MW proton driver (`SRC_ARXIV_2610_35154` p.3–4); μTRISTAN yield itself not in the uploads. Snippet lead (unverified): J-PARC USM ~10⁵ μ⁺/s design | order of magnitude; depends on an external proposal | `order_of_magnitude`; chain factor to be a synthetic log-uniform band once an assumption record exists |
| Muon bunch population N_μ | 0.07×10¹¹ (DIS2026 Table 1); 3.0×10¹⁰ / 3.7×10¹⁰ (μLHC Tables 1–3, arXiv:2506.15445) | document-to-document difference ×4–5 | separate scenarios (`LHMUC-DIS2026-1TEV`, `MULHC-PTEP2026-ERL-BOOSTER`, `MULHC-PTEP2026-MUTRISTAN-BOOSTER`), conflict record |
| Muon normalised emittance | 4 μm (μLHC Table 1, imported from μTRISTAN); LHμC value **unknown**. Snippet lead: J-PARC source < 1 π mm mrad | imported, applicability `design_variant` | `imported_related`; LHμC role in `unknown_roles` |
| Booster survival | 82 % (16 turns) / 67 % (50 turns) (arXiv:2506.15445 §2.2); P1 model gives 81.6 % / 67.4 % | model-dependent (ramp shape, arcs) at the few-% level | `not_stated` on the reported values; model residual recorded in `tests/scientific`, not as a σ |
| Muon β* at the IP | 3 cm / 0.7 cm (μLHC); 7–15 cm "relaxed to match" (Nucleus Options p.12–14, `SRC_WS1681458_DAGLI_NUCLEUS`); LHμC DIS2026 **unknown** | design choice, not a measurement | `interval` where a range is given; `unknown` for DIS2026 |
| Proton bunch population N_p | 22×10¹¹ (DIS2026 Table 1) vs 2.2×10¹¹ (μLHC Table 2; HL-LHC). Snippet leads on HL-LHC: 2.2×10¹¹, ε_n 2.5 μm, 2760/2748/2808 bunches by source | factor 10, real design difference | separate scenarios; conflict record; the factor 10 is verified by `test_dis2026_proton_bunch_population_is_ten_times_hl_lhc` |
| Proton β*, emittance, bunch length | β* 7 cm, ε_n 2 μm (μLHC Table 2); DIS2026 σ = 4.8 μm at the IP implies β* ≈ 6.9 cm for ε_n = 2.5 μm (audit arithmetic). Proton bunch length **unknown** in all LHμC documents (7.5 cm LHC value used only as an order-of-magnitude input to the hourglass check). Snippet lead: LHeC β* 10 → 7 cm | imported; bunch length missing | `imported_related`; bunch length `unknown`; hourglass sensitivity is an open item |
| Luminosity model (hourglass, decay, crossing angle, beam–beam) | DIS2026 2.1×10³⁴ reproduced with H = 1; μLHC 7.2/8.8×10³³ reproduced as naive × 0.632 decay average; computed hourglass ≈ 0.53 for μLHC-like optics with 7.5 cm proton bunch (`docs/validation_plan.md` §2) | **model-form uncertainty**: which terms the published numbers include is not stated | conflict `CONF_LUMI_MODEL_ASSUMPTIONS` (to be written); propagated as a discrete set of model variants, never as a Gaussian |
| Average vs peak luminosity, fill pattern | DIS2026: 12.5 Hz repetition (80 ms) against τ_lab = 20.8 ms; "average luminosity close to 10³⁴" (`order_of_magnitude`); 80 bunches × 250 ns = 20 μs train vs ~10 μs revolution of a 3 km ring (see `validation.notes` in `parameters/machine/lhmuc_dis2026.yaml`) | averaging procedure not stated | `order_of_magnitude`; averaging model variants as a discrete set |
| Crossing angle and L* | `IR_CROSSING_ANGLE_DIS2026` is the one `unknown` record (`python -m lhmuc validate`); L* unknown. Snippet leads (unverified): LHeC L* = 15 m, 6–7 mrad vs head-on; IMCC L* = 6 m at 10 TeV | missing | `unknown`; any value used in a model is `synthetic` with an assumption record |
| IR magnets | snippet lead: LHeC Q1A 252 T/m, 20 mm aperture — unverified | missing for LHμC | `unknown` until a source is read in full |
| Main-ring and booster dipole fields | "3 T max" for 1 km-radius arcs (arXiv:2506.15445 §2.2.3); 3.2 T from Bρ; 7.0 T for a fully-dipole 3 km ring (idealisation) | fill factor, lattice unknown | `analytical_estimate` with derivation; lattice fill factor a synthetic range when needed |
| Nozzle / machine-detector interface | 6 m tungsten + borated polyethylene, 19 % of energy deposited (μLHC §2.4). Snippet leads: IMCC INERMET180, tip 6 cm from IP, 10° — unverified | geometry imported from a related design | `imported_related`; IMCC leads `analogous`, confidence ≤ medium |
| Detector efficiencies and resolutions | di-Higgs deck: 70 % b-tag working point, S/√(S+B) = 4.25 at 1 ab⁻¹ (`SRC_WS_LEBOHO_KUMAR_DIHIGGS` p.14–16); two-photon requirements (`SRC_WS1681458_KHANPOUR_GAMMAGAMMA` p.26) | assumed by the analyses; no LHμC detector exists | `reported_lhmuc` as *analysis assumptions*; varied as a discrete set in sensitivity studies |
| Theory inputs: cross sections, PDFs, scales, EFT models | MG5_aMC v3.6.7, CTEQ6L1, HELv2 `effdihiggs-v2` (not public), σ = 0.17 fb / 0.33 fb; μLHC Tables 4–6 yields; EPA γγ cross sections | LO; scale/PDF uncertainties not given by the decks | `not_stated`; propagation needs generator runs with scale and PDF variations recorded in run records |
| Beam-induced background, radiation dose, activation | no LHμC number; qualitative statements only | missing | blocked until transport simulations (Geant4/BDSIM) exist; reported as "not evaluable" |
| Power and cost | 4 MW proton driver (DIS2026); wall-plug power and cost **unknown** | missing | `unknown`; no estimate is produced by the LLM |

The table is the Phase 0 input to `uncertainty/priors/` (Milestone 4). An input missing from
the registry cannot be given a prior by this document.

### 2.1 Addendum 2026-10-29 — input classes changed by the uploaded documents

The rows above stay as written on 2026-10-28. The uploads of the Phase-0 addendum and batches 7–9
change what is known for the classes below; the representation column says how each enters a
future propagation. LHμC values from the Kraków decks are reported in workshop material and
unverified by simulation; everything else is a comparator.

| Input class | What is known now (record, source page) | Uncertainty character | Representation |
|---|---|---|---|
| Muon source yield | measured 2.1 × 10⁻⁸ μ⁺ at 100 keV per surface muon (`SOURCE_USM_PER_SURFACE_MUON_100KEV_ARITOME2024`, pp.2, 4); design budgets 2.5–2.6 × 10⁻³ per surface muon (J-PARC g-2) and 0.137 after stopping (μTRISTAN, Zhang p.20); hybrid source 0.04 μ⁺ per 5 GeV proton to the end of stage A (Rogers p.14); hybrid target 6 × 10⁻⁴ per p–Li collision × unknown η_conv | gap of 10⁵–10⁶ between demonstrated and design values; scheme-dependent | separate scenarios per source concept and laser scheme (`CONF_SOURCE_CONCEPT`, `CONF_LASER_IONISATION_EFFICIENCY`); a result that needs η_conv or the extraction efficiency is **not evaluable** (both null) |
| Muonium formation fraction | 0.52 ± 0.01 (Bakule 2013 p.3) and 0.655 ± 0.018 (Beare 2020 p.25), different samples, 6.6 σ apart | two measurements, not one quantity with scatter | the value of the target type the model represents, with its σ; never a pooled mean (`CONF_MUONIUM_FORMATION_FRACTION`) |
| Laser-ionisation efficiency | 0.73 calculated (Abe 2019 p.8); ~10⁻⁶ for the 244 nm scheme used in 2024 (Zhang p.10); simulated 7 × 10⁻⁶ – 6 × 10⁻⁵ (Aritome); "around 10%" projected for 122 + 355 nm (Aritome p.5) | model-form: which scheme | discrete set by scheme, each labelled calculated / simulated / projected; no measured 122 + 355 nm value exists |
| Nozzle opening angle and length | 40 / 60 / 80 / 100 mrad, 587.8 cm, tip 6 cm (Kilic, Forthomme); IMCC 10°, 595 cm base plane (MR7) | design options | discrete set of options (`CONF_NOZZLE_OPENING_ANGLE`); the superseded `_SYN` bands only as scan variables |
| L* | 15 m (LHeC), 23 m (unnamed layout), 6 m (IMCC) — none for the LHμC | missing for LHμC | `IR_LSTAR_SYN` as scan variable, every result labelled with the L* used (`CONF_IR_LSTAR`) |
| Detector solenoid field | 3 T (LHeC paper), 3.8 T (LHeC Delphes card), 5 T (MAIA, MUSIC) — none for the LHμC | missing for LHμC | `DET_SOLENOID_FIELD_SYN` scan, results per field (`CONF_DETECTOR_SOLENOID_FIELD`) |
| vFFA peak field | Kraków options ~8 / ~10 / < 9 T (preliminary analytic); M17 6.93 T (F-magnet, stage 1) and 13.59 T (D-magnet, stage 4), good-field 12.52 / 29.04 T | definition-dependent (which magnet, on orbit vs good-field region) | separate scenarios with the field definition stated (`CONF_VFFA_PEAK_FIELD`) |
| Proton bunch population | 2.2 × 10¹¹ (μLHC/HL-LHC), ≈ 7.0 × 10¹¹ implied by the Forthomme set under H = 1, 22 × 10¹¹ (DIS2026) | design difference plus an unstated convention | separate scenarios (`CONF_PROTON_BUNCH_POPULATION_AND_NUMBER`); the implied value carries its conventions in the derivation |
| Proton bunch length | still no LHμC value; Zimmermann's rule σδσz ≈ 2 n_b,0 σδ,0 σz,0 for merged bunches (p.14) | missing; correlated with the bunch population | `PROTON_BUNCH_LENGTH_RMS_SYN` (synthetic range) with the correlation to the population stated in any model that varies both |
| Luminosity model | AloHEP: hourglass and pinch simulated, decay applied analytically, L_nom equal-beam approximation (`SRC_ARXIV_2610_09839` pp.33, 36); H = 1 stated by the muon-ion collider paper (PDF p.7); one-beam (0.632) vs two-beam (0.432) decay average over one lifetime | model-form uncertainty, now enumerable | discrete set of option sets (§3.2), results per option set; the decay term always in its one-beam μp form |
| TeV-muon momentum resolution | 6–7 % at 1 TeV main detector (Yamazaki p.10); ~6 % far-forward toroid, Geant4 (Acosta p.12) | by detector region and method | per region (`CONF_TEV_MUON_RESOLUTION`) |
| Front-end transmission for ≥ 10¹⁰ μ⁺ per bunch | unknown; 0.75 A at the RFQ entrance, 220 × the design perveance (Nakazawa p.16) | missing | `unknown`; no scaled J-PARC value is used (`CONF_FRONT_END_SPACE_CHARGE`) |
| Muon polarisation | assumed 50 % (Forthomme p.17), assumed 0.8 (μTRISTAN p.10), 50 % for the J-PARC g-2/EDM muon beam (Abe 2019 p.4, Table 1) | assumptions or design values, not measurements | discrete set of assumed values, labelled as assumptions |

---

## 3. Propagation strategy

Propagation is done by code under `uncertainty/propagation/` (not yet written), on the registry,
with the method recorded in the run record. Three methods, chosen by cost of the model and by the
type of the inputs:

### 3.1 Analytical (fidelity tier `A_analytical`)

For closed-form relations (√s, γ, τ_lab, L_naive, Bρ, σ from ε_n and β*, x_min): first-order
error propagation for `gaussian_sigma` and `relative_fraction` inputs; **interval arithmetic**
(min/max over corners or monotone bounds) for `interval`, `range_only` and `order_of_magnitude`
inputs. Outputs are reported as intervals when any input is an interval. Correlations stated by
a source (e.g. N_μ and the booster survival both derive from the same source yield) are kept by
propagating the common parent, never by assuming independence silently.

### 3.2 Monte Carlo sampling (tiers `A`, `B_fast_simulation`)

For fast models (luminosity with decay, hourglass and crossing angle; fast detector simulation;
yield × efficiency × luminosity): Latin-hypercube or quasi-random sampling of all declared
distributions (assumption records) with a recorded seed, ≥ 10³ samples for interval summaries
and ≥ 10⁴ for tail probabilities (§4). Model-form alternatives (which luminosity terms apply,
which averaging procedure) are sampled as a **discrete set**, and results are reported per model
variant as well as pooled; pooling across variants is labelled as such.

### 3.3 Surrogates (tier `C_surrogate`)

When a high-fidelity model (optics tracking, Geant4/BDSIM transport, full generator chains) is
too expensive to sample, a surrogate (Gaussian process or neural network, trained on run records)
may replace it **inside its training domain only**. Rules: the training set, validation error and
domain hull are stored with the surrogate; a query outside the hull is refused and reported
(`CLAUDE.md` §1.10, "surrogate is out of domain"); the surrogate's own prediction error is added
to the propagated uncertainty; conclusions drawn through a surrogate carry
`high_fidelity_verification_status` in the optimisation record and are not final until a
high-fidelity verification run of the selected point exists (tier `D_high_fidelity`, then `E_independent_validation`).

### 3.4 Sensitivity analysis

Before any probabilistic statement is published, a global sensitivity analysis (Sobol indices or
Morris screening, `uncertainty/sensitivity/`) ranks the inputs; assumption records update their
`sensitivity_analysis` field to `done` with the index value, and inputs that dominate a
conclusion are listed in the report with their provenance status. A conclusion dominated by a
`synthetic` or `order_of_magnitude` input is reported as such.

---

## 4. Probabilistic reporting

Results are reported as probabilities over the declared input uncertainty, not as single
numbers, whenever any input is uncertain. The required statements and their definitions:

| Statement | Definition | Required inputs | Phase 0 status |
|---|---|---|---|
| **P(L > L_required)** | fraction of samples (per model variant) in which the computed average luminosity exceeds the value the physics case requires (e.g. the integrated-luminosity working points 250 fb⁻¹ / 1000 fb⁻¹ divided by an assumed operating time, which must itself be an assumption record) | N_μ, N_p, σ_x,y or (β*, ε_n), f, decay/hourglass/crossing model, fill pattern, operating time | not computable: proton bunch length, muon β* (DIS2026), crossing angle, operating time unknown |
| **P(5σ)** | probability that a stated benchmark reaches a 5σ discovery significance (or a stated exclusion) given the luminosity distribution, cross-section uncertainty and efficiency distribution; computed with pyhf likelihoods, Asimov or toys stated | signal and background cross sections with scale/PDF variations, efficiencies, L distribution | not computable: `effdihiggs-v2` not public; only the deck's own S/√(S+B) = 4.25 (1 ab⁻¹, 70 % b-tag) is recorded as reported |
| **P(dose ≤ limit)** | probability that the computed radiation dose (or activation) at a specified location stays below a specified limit | transport simulation (Geant4/BDSIM) on validated geometry, source term from muon decay and beam losses | not computable: no geometry, no transport code installed, no limit specified by a source |
| **P(power ≤ budget)** | probability that the computed wall-plug or component power stays below a budget | magnet, RF, cryogenic and driver power models; a budget stated by a source or declared as an assumption | not computable: only the 4 MW proton-driver figure is reported; no budget exists |

Reporting rules:

1. Every probability names the model variant(s), the sample size, the seed, the assumption ids and
   the run ids; it carries the minimum P-label of its inputs and the fidelity tier of its model.
2. A probability computed with any `synthetic` input is displayed with the assumption ids next to
   it, in the UI, plots, exports and reports (`CLAUDE.md` §1.4).
3. When a required input is `unknown`, the statement is **"not evaluable; missing: …"**, not a
   number. The missing ids go to `registries/missing_evidence.csv`.
4. Thresholds (L_required, limits, budgets) are parameters with provenance like any other; an LLM
   may propose one, but it is recorded with `status: synthetic` and an assumption record until a
   source states it.

---

## 5. Robust-design rule

Optimisation (Milestone 4+) does not optimise the nominal design point alone. Every candidate
θ_nominal is evaluated together with perturbed points θ_nominal + δ, where δ is drawn from the
declared input uncertainties and the tolerances of the design variables (alignment, field errors,
emittance growth, population jitter — each as an assumption record if no source gives it). A
design is **feasible** only if the hard constraints g_k(θ_nominal + δ) ≤ 0 hold for the stated
fraction of perturbations (default 95 %, recorded in `optimization.uncertainty_treatment`), and
the objective reported is the expectation or a stated quantile over δ, not the nominal value. The
nominal-point objective is shown alongside for transparency. An optimisation whose constraint
bounds are unknown (e.g. no aperture, no dose limit) lists them in `conclusions_blocked_by` and
reports no optimum.

---

## 6. LLM confidence is never scientific uncertainty

- The `provenance.confidence ∈ {high, medium, low, none}` field expresses **how reliably the value
  was read from the source** (clear table cell → `high`; inferred from text or figure → `medium`;
  snippet or ambiguous → `low`; none). It is a provenance-quality flag, not a physical error bar,
  and never enters a propagation.
- A number proposed by an LLM (a threshold, a plausible β*, an efficiency) is a hypothesis. It is
  recorded, if at all, as `synthetic` with an assumption record and a range; the LLM's stated
  self-confidence about it is not written anywhere as an uncertainty. Numbers come from documented
  computation by tools (`CLAUDE.md` §1.8).
- LLM-extracted proposal content keeps `review_state: extracted` until a human marks it
  `reviewed` (`schemas/proposal.schema.json`); extraction confidence does not shorten that step.
- Reports never phrase a scientific uncertainty as "we are fairly confident"; they give the
  interval, the distribution or the statement "not evaluable", with the method.
- *Added 2026-10-29:* the `confidence` field is now bounded by the caps of
  `research/source_quality_policy.md` §4, enforced by the validator; 1423 records were lowered from
  `high` to `medium` on 2026-10-29 (`research/_fragments/confidence_caps_applied_2026-10-29.csv`). The
  lowering changed provenance quality flags only — no value, interval or σ was touched, and none
  enters a propagation.

---

## 7. How snippet-only sources cap confidence

Sources with `access ∈ {snippet_only, blocked, pending_fetch}` (`schemas/source.schema.json`,
`research/source_registry.yaml`) were not read; only search-engine snippets or paraphrases were
seen. Consequences, enforced by `lhmuc/registry.py::cross_check` and
`tests/unit/test_registry_integrity.py` (`test_primary_sources_are_uploaded_or_fetched`,
`test_snippet_sources_capped_confidence`):

1. Such a source can never back `status: reported_lhmuc`; at most `imported_related`,
   `analogous` or a lead for a later fetch.
2. Any parameter citing it has `confidence ≤ medium`.
3. For propagation, a snippet-backed value is treated like a `synthetic` input: it must be
   widened into a range by an assumption record stating that the value is unverified, and the
   affected results display that assumption id. The snippet leads listed in §2 (LHeC L* and
   β*, Q1A gradient, crossing angle, IMCC nozzle details, J-PARC source rate and emittance, HL-LHC
   bunch counts, the HNL and 2HDM+VLQ paper contents) are in this class.
4. When the document is later fetched and read in full, the record is re-extracted with page and
   quotation; the snippet-era record is marked `applicability.category: superseded`, not deleted.

*Update 2026-10-29:* several leads of item 3 are now read in uploaded documents and leave this
class — LHeC L* = 15 m and β*_p = 10 cm (`SRC_ARXIV_2201_02436` p.16), the IMCC nozzle and L* = 6 m
(`SRC_ARXIV_2510_27437` pp.65–66), the J-PARC chain (Abe 2019, Aritome 2024), the HNL and 2HDM+VLQ
papers excepted (still blocked). They enter as read comparators with their own provenance; the
Q1A gradient, the J-PARC design rate and the HL-LHC bunch counts and emittance remain snippet-level.

---

## 8. How conflicts become uncertainty

Conflicting values between sources are recorded in `research/source_conflicts.yaml`
(`schemas/conflict.schema.json`; file not yet present on 2026-10-28) with `competing_values`,
`possible_cause`, `selected_treatment`, `effect_on_simulations`, `required_future_evidence` and a
`status ∈ {open, resolved_as_scenarios, resolved_superseded, propagated_as_uncertainty}`. The
decision tree:

1. **Different machines or design variants** (DIS2026 vs μLHC bunch populations; 3 km vs 6 km
   ring; μTRISTAN vs ERL booster) → `resolved_as_scenarios`: separate scenarios, each with its
   own results; no pooled number is ever produced.
2. **Same quantity, one source newer and explicitly superseding** (pre- vs post-erratum μLHC
   luminosities) → `resolved_superseded`: the older record stays with
   `applicability.category: superseded`; the newer value is used.
3. **Same quantity and design, unexplained disagreement** (e.g. two decks quoting different
   luminosities for the same configuration, or an unstated model term such as the hourglass
   factor) → `propagated_as_uncertainty`: the competing values become a `discrete_set`
   distribution in an assumption record; propagation samples the set; results are reported per
   value and pooled with the pooling labelled. The conflict is **not** averaged into a mean
   (`CLAUDE.md` §1.6).
4. **Not yet decided** → `open`: dependent results are blocked (`conclusions_blocked_by`), and
   the conflict id is shown wherever either competing value is displayed.

The first entry to be written is `CONF_LUMI_MODEL_ASSUMPTIONS` (referenced by
`tests/scientific/test_analytical_checks.py`), covering the H = 1 reproduction of DIS2026 Table 1,
the decay-only reproduction of the μLHC Tables 1–3 and the computed hourglass ≈ 0.53; its status
will be `open` until the luminosity model behind the published numbers is documented.

*Update 2026-10-29:* `research/source_conflicts.yaml` holds 15 records at commit `104073c`, among them
`CONF_LUMI_MODEL_ASSUMPTIONS` with status `open`. Because `research/source_quality_policy.md` §4 caps
every competitor of an undecided conflict at `low`, each conflict must name a treatment. The registry
stage of 2026-10-29 records decided treatments for the open Phase-0 records and drafts nine new
records, which illustrate the decision tree: design options kept as scenarios
(`CONF_NOZZLE_OPENING_ANGLE`, `CONF_SOURCE_CONCEPT`, `CONF_VFFA_PEAK_FIELD`, `CONF_TEV_MUON_RESOLUTION`);
two measurements on different samples kept per sample, never pooled
(`CONF_MUONIUM_FORMATION_FRACTION`); calculated, simulated and projected values kept per scheme
(`CONF_LASER_IONISATION_EFFICIENCY`); comparators carried by a scan variable
(`CONF_IR_LSTAR`, `CONF_DETECTOR_SOLENOID_FIELD`, both `propagated_as_uncertainty`); and a scaled
design rejected in favour of an explicit unknown (`CONF_FRONT_END_SPACE_CHARGE`). The committed file
is authoritative; confirm statuses there once the registry stage is committed.

---

## 8a. Addendum 2026-10-29 — the AI4MuC principles applied to uncertainty

The AI4MuC report (`SRC_ARXIV_2610_14303`, §11, pp.12–13; adopted as process rules in
`docs/architecture.md` §15.1) states, among its seven principles: "Validate tails and failures. For
Muon Collider problems, losses, rare backgrounds, high occupancies, quenches, breakdown, and unusual
signal signatures may dominate the risk." and "Track uncertainty and domain of validity. Fast models
are most useful when users know where they can and cannot be trusted." For this policy they mean:

1. **Tail statements need tail statistics.** P(dose ≤ limit), occupancy and breakdown statements
   (§4) are computed with sample sizes adequate for the tail (≥ 10⁴ for tail probabilities, §3.2), and
   the sampling procedure must not erase the tail. The report notes that current IMCC BIB samples take
   "a FLUKA sample representing 10% of a single bunch crossing's parent muon population, clones and
   randomizes each parent's decay products in azimuth", which "washes out the genuine asymmetries" and
   under-represents rare events (p.10); such samples may be used for means, not for tails, and any
   surrogate trained on them inherits that limit.
2. **Every fast model carries its domain.** A surrogate stores its training hull and refuses
   queries outside it (§3.3); an external code is used inside the regime its authors validated — for
   AloHEP the hourglass treatment to A = σ_z/β*_y ≲ 1.5 and the pinch to D_y ≤ 1.3
   (`SRC_ARXIV_2610_09839` pp.27, 31) — and any result outside it is labelled as such until a refined
   run or a second code confirms it.
3. **Comparison with trusted tools bounds model-form uncertainty.** "Compare to trusted tools" (p.12)
   is how the discrete model variants of §3.2 are narrowed: a variant survives only if it reproduces
   the published benchmark it claims to describe (`docs/validation_plan.md` §3.1).
4. **Unknowns stay unknown.** Where the uploads say a quantity was not determined — the
   muon-to-muonium conversion η_conv and the extraction efficiency of the hybrid target, the RF
   breakdown gradient of the thin-window cavities, the front-end transmission at ≥ 10¹⁰ μ⁺ per bunch —
   the dependent statement is "not evaluable; missing: …" (§4, rule 3), not a sampled number.

## 9. Sources cited

- `SRC_ARXIV_2610_35154` — K. Piotrzkowski (HELP4CERN), "LHμC: A high energy, high luminosity
  muon-hadron collider at CERN", PoS DIS2026, arXiv:2610.35154v1 (2026-10-26): Table 1 p.4; §2–§4.
- `SRC_ARXIV_2506_15445` — D. Akturk et al., "μLHC: Antimuon Ring and HL-LHC based μ⁺p Collider",
  PTEP 2026 033C04, arXiv:2506.15445v2: §2.2, §2.3 Tables 1–3, §2.4, §3 Tables 4–6.
- `SRC_WS1681458_DAGLI_NUCLEUS` — "LHμC: Nucleus Options" slides, p.8, p.11–14.
- `SRC_WS1681458_KHANPOUR_GAMMAGAMMA` — "Two-Photon Physics at the LHμC" slides, p.4, 5, 9–11, 15,
  19, 26.
- `SRC_WS_LEBOHO_KUMAR_DIHIGGS` — "Probing anomalous Higgs couplings at the future μ⁺p collider"
  slides, p.6–8, 12, 14–16.
- Snippet-only leads (unverified, `research/_fragments/*_sources.yaml`): LHeC IR, IMCC nozzle,
  J-PARC source, HL-LHC beam parameters, arXiv:2610.28252, arXiv:2610.17801.
- Added 2026-10-29 (uploaded, read in full): `SRC_ARXIV_2610_14303` (AI4MuC, pp.10, 12–13),
  `SRC_ARXIV_2610_09839` (AloHEP, pp.27, 31, 33, 36), `SRC_ARXIV_1306_3810`, `SRC_ARXIV_2006_01947`,
  `SRC_ARXIV_2410_11367`, `SRC_ARXIV_1901_03047`, `SRC_ARXIV_2605_25580`, `SRC_ARXIV_2201_02436`,
  `SRC_ARXIV_2510_27437`, `SRC_ARXIV_2203_06258`, `SRC_DOI_10_5281_ZENODO_15054073` and the Kraków decks
  `SRC_WS1681458_*` cited in §2.1 (pages there).
