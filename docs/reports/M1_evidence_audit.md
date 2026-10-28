# Milestone 1 report — Phase 0 evidence and feasibility audit

**Date:** 2026-10-28 · **Branch:** `claude/lhmc-virtuallab-architecture-eitkjb` · **Author:** Claude
(lead session) for David Hausler · **Status of the platform: evidence audit complete; no digital twin exists.**

This report follows the structure required by the master prompt (§42 and §49). Every number below is
taken from the registries committed in this repository; nothing here is a new claim about LHμC.

## 1. Project understanding

LHμC-VirtualLab is to become an evidence-traceable digital twin of the proposed LHμC μ⁺p collider
(1 or 2 TeV ultra-cold positive muons on the 7 TeV LHC proton beam, √s = 5.3 or 7.5 TeV; a
500 GeV / 3.74 TeV option appears in the HELP4CERN white-paper working points), with a
theory-recasting pipeline for μ⁺p processes, experiment-driven accelerator/detector co-optimization,
uncertainty-aware design and reproducible reporting. Phase 0 had to establish what is actually
known, from which sources, with what confidence, and what is missing — before any geometry, lattice
or event generation is built. See `docs/scientific_scope.md` and `docs/architecture.md`.

## 2. Evidence summary

| Item | Count | Where |
|---|---|---|
| Documents read in full (uploaded) | 5 | `research/archived_metadata/`, `research/source_registry.yaml` (access `uploaded`) |
| Sources registered in total | 218 | `research/source_registry.yaml` |
| … by access: uploaded / fetched / snippet_only / blocked | 5 / 31 / 86 / 96 | same |
| … by category: PRIMARY_LHMUC 5, RELATED_MACHINE 23, OFFICIAL_CERN 19, PEER_REVIEWED 36, CONFERENCE_PROCEEDING 69, OFFICIAL_SOFTWARE_DOCUMENTATION 33, ANALOGOUS_TECHNOLOGY 6, SECONDARY_SOURCE 19, UNVERIFIED 8 | | same |
| Search-log rows (queries × sources, nine reconnaissance families) | 383 | `research/search_log.csv` |
| Unresolved searches and fetch backlog | one register | `research/unresolved_searches.md` |

**Sources examined in full:** arXiv:2610.35154 (Piotrzkowski, HELP4CERN, PoS DIS2026 — primary
baseline, CC BY-NC-ND 4.0, archived in `references/primary/`); arXiv:2506.15445 v2 (Akturk et al.,
μLHC, PTEP 2026 033C04 — related machine); three Kraków-workshop decks (Dagli et al. *Nucleus
Options*; Khanpour *Two-photon physics*; Leboho/Kumar et al. *Anomalous Higgs couplings at the
future μ⁺p collider*). The literature hosts (arxiv.org, indico.cern.ch, cds.cern.ch, inspirehep.net,
pos.sissa.it, doi.org, journal and software-documentation sites) were **blocked by the environment's
network policy** throughout Phase 0; the 213 non-uploaded sources are therefore registered from search
snippets only (`snippet_only`) or as attempted-and-refused fetches (`blocked`), and no value from them
has been admitted as a baseline parameter. The required allow-list is in
`docs/internet_research_protocol.md` and `research/unresolved_searches.md`.

## 3. Parameter coverage

| Provenance status | Records | Meaning |
|---|---|---|
| `reported_lhmuc` | 472 | read directly from a PRIMARY_LHMUC document (page, table/figure, verbatim quotation) |
| `imported_related` | 298 | from the μLHC paper or values it imports from μTRISTAN / LHeC / HL-LHC / PDG |
| `analogous` | 19 | comparison-collider values (HERA, EIC, IMCC) restated by the sources |
| `derived_lhmuc` | 12 | computed from reported values with a stated derivation |
| `analytical_estimate` | 7 | closed-form estimates (e.g. τ_lab, implied β*) with stated formula |
| `synthetic` | 20 | **ranges only**, each with an assumption record in `parameters/assumptions/` |
| `scan_variable` | 1 | g_hhh scan |
| `unknown` | 1 | crossing angle of the DIS2026 set (`value: null`) |
| **Total** | **830** | `registries/parameter_registry.csv`; by subsystem: machine 166, physics programme 387, detector 62, acceleration 61, source 54, ion beam 57, IR 24, proton beam 19 |

Confidence: high 585, medium 220, low 24, none 1. Validation level: P1 276 (analytically
reproduced), P0 554. Every record was re-checked by an independent verification pass against the
page images (`research/_fragments/verify_*.md`): 0 records lacked support; corrections were
limited to applicability wording, uncertainty types, one transcription error and nine added records.

**Scenarios (13):** `LHMUC-DIS2026-1TEV`, `LHMUC-DIS2026-2TEV`, `LHMUC-WP-OPT1-500GEV`,
`LHMUC-WP-BASELINE-1TEV`, `LHMUC-WP-OPT2-2TEV`, `MULHC-PTEP2026-MUTRISTAN-BOOSTER`,
`MULHC-PTEP2026-ERL-BOOSTER`, `LHMUC-NUCL-MU-{PB,XE,O,NE}`, `LHMUC-DIHIGGS-{500GEV,1TEV}`
(`parameters/machine/scenarios_*.yaml`). Scenario slots reference parameter ids only.

**Directly supported LHμC parameters (DIS2026 Table 1):** √s 5.3 TeV; peak L 2.1 × 10³⁴ cm⁻²s⁻¹;
collision rate 4 MHz; repetition rate 12.5 Hz; σ*ₓ,ᵧ 4.8 µm (both beams); Nμ 0.07 × 10¹¹;
Nₚ 22 × 10¹¹; 80 bunches at 250 ns; E_μ 1 (2) TeV; E_p 7 TeV; booster ≈ 9 km; main ring ≈ 3 (6) km;
"5 % of the μTRISTAN yields"; 4 MW proton driver. Everything optics-level (β*, emittance, bunch
length, crossing angle, L*, magnets, nozzle geometry) is **not given** for LHμC and is carried as
unknown or as imported μLHC values in separate scenarios.

## 4. Analytical cross-checks performed (P1, `tests/scientific/`, 65 tests pass)

- γ(1 TeV) = 9464, τ_lab = 20.8 ms (source: "approximately 20 ms"); 3 km ring → 10.0 µs/turn,
  ≈ 2080 turns per lifetime, one-lifetime average population 0.632 (source: "0.63").
- √s = 2√(E_μE_p) = 3.74 / 5.29 / 7.48 TeV for 0.5 / 1 / 2 TeV muons (sources: 3.7 / 5.3 / 7.5).
- DIS2026 Table 1 luminosity 2.1 × 10³⁴ is reproduced by f·N₁N₂/(4πσₓσᵧ) with **H = 1** and
  **N_p = 2.2 × 10¹²**, i.e. ten times the HL-LHC bunch population (the text motivates this by fewer
  bunches); with 2.2 × 10¹¹ it would be 2.1 × 10³³.
- μLHC Table 3 luminosities 7.2 × 10³³ and 8.8 × 10³³ are reproduced to < 2 % by the naive formula
  (1.14 / 1.40 × 10³⁴) times the quoted decay average 0.632. **No hourglass reduction is visible**,
  although the stated optics (β*ᵧ = 0.7 cm, proton β* 7 cm, centimetre-scale proton bunch) would
  give H ≈ 0.5 for a 7.5 cm proton bunch. Recorded as the open conflict
  `CONF_LUMI_MODEL_ASSUMPTIONS`; resolution needs the AloHEP input decks.
- Proton σ* = √(ε_n β*/γ) = 4.33 µm from ε_n 2 µm, β* 7 cm (source 4.3 µm).
- Bρ(1 TeV) = 3336 T·m; 960 GeV on a 1 km radius needs 3.2 T (source "3 T max"); a fully
  dipole-filled 3 km ring at 1 TeV would need 7.0 T (no LHμC main-ring magnet value exists).
- Turn-by-turn racetrack booster decay model: 81.6 % (μTRISTAN layout, 16 turns) and 67.4 %
  (ERL layout, 50 turns) against the paper's 82 % / 67 %.
- Internal-consistency observation (not resolved by the sources): 80 bunches × 250 ns = 20 µs is
  twice the revolution period of a 3 km ring, while 4 MHz × 10 µs = 40 bunches per turn
  (`CONF_MUON_BUNCHES_PER_TRAIN`).

## 5. Conflicts (15, `research/source_conflicts.yaml`)

Peak luminosity (2.1e34 vs 8.8e33 / 7.2e33 vs pre-erratum vs "> 10³³" listings); luminosity-model
assumptions; muon bunches per train (80 vs 40); muon bunch population (0.07e11 vs 3.7e10 / 3.0e10 vs
4.5e10 injected); repetition rate (12.5 vs 50 Hz); IP beam size (4.8 vs 4.3 µm vs 5.5–7.9 µm);
proton bunch population and number (2.2e12 vs 2.2e11 × 2760; HL-LHC 2760 / 2748 / 2808 by
source); proton emittance (2 vs 2.5 vs 3.75 µm); booster design (≈ 9 km vFFAG vs μTRISTAN racetrack
16 turns vs LHeC-ERL racetrack 50 turns); booster injection energy (1 GeV vs 212 MeV); main-ring
circumference (3 vs "3 (6)" km); LHμC design-version evolution (500 GeV / 1 TeV / 1–2 TeV
listings); LHeC crossing angle (6 / 6.8 / 7 mrad vs head-on, snippet-level); μLHC survival-rate
erratum (superseded values kept); J-PARC IH-DTL energy (snippet-level). None was averaged.

## 6. Unresolved engineering data (55 entries, `registries/missing_evidence.csv`; 7 critical, 25 high)

Critical: the HELP4CERN white paper (in preparation, not public); the Kraków contributions on the
nozzle (Kilic), main detector (Forthomme), vFFA (Topp-Mugglestone), SPS/LHC modifications
(Zimmermann), pre-acceleration (Otani), hybrid source (Rogers), muonium diffusion (Zhang). High:
the μLHC erratum text; IR L*, Q1 gradient/aperture, crossing angle, β* and IP sizes; emittances,
bunch lengths, energy spreads; nozzle geometry and materials; LHeC detector dimension tables;
beam-induced background for an asymmetric μ⁺p IR; vFFA lattice and fields; the 4 MW proton driver;
the muon yield chain (pion yield, muonium formation, laser ionisation, capture, pre-acceleration
transmission); main-ring lattice/aperture/magnets; beam-beam limits; average-vs-peak luminosity
model; AloHEP code and input decks; HL-LHC TDR, LHeC CDR and μTRISTAN full texts; the two theory
papers and their UFO models; the `effdihiggs-v2` UFO.

## 7. Synthetic assumptions proposed (20 ranges, `parameters/assumptions/phase0_assumptions.yaml`)

IR: L* 5–20 m; crossing angle 0–10 mrad; separator dipole 0.1–1 T and 3–15 m; Q1 gradient
100–300 T/m; Q1 aperture radius 20–60 mm; muon β*ₓ,ᵧ 0.5–20 cm. Detector: nozzle opening angle
5–20°, length 2–10 m, tip distance 2–50 cm, material {tungsten, INERMET180, tungsten + borated
polyethylene}; solenoid 2–5 T. Acceleration: vFFA peak field 3–16 T; RF frequency {325, 352, 400,
802, 1300} MHz; RF gradient 10–30 MV/m. Source: muonium formation fraction 0.3–0.7; laser
ionisation efficiency 10⁻³–1 (log-uniform). Machine: polarisation 0–0.8; proton RMS bunch length
5–12 cm. Each record states what was searched, the analogue values seen (snippet-level, with
source ids), physical basis, affected outputs and the evidence that would replace it. The point
values stored next to the ranges are range midpoints for software demonstration only.

## 8. Architecture delivered

Repository-root layout of the master-prompt tree; YAML parameter records as the single source of
truth validated by eleven JSON Schemas; generated CSV registries; `lhmuc` package (pint units,
registry loader with referential, null-vs-zero and provenance rules, CLI, P1 audit arithmetic);
tools for registry generation, YAML validation and research-fragment merging; tests (unit,
integrity, scientific); policy documents (architecture, scientific scope, validation plan,
research protocol, source-quality policy, synthetic-data, fidelity, uncertainty, security,
limitations, roadmap, research roadmap, software inventory); benchmark proposal records A–D. All
other architecture directories exist only as explicit "not implemented" placeholders.

## 9. Validation strategy

`docs/validation_plan.md` and `registries/validation_registry.csv` (36 checks: 24 pass, 12 planned
for M2–M5: AloHEP reproduction, MAD-X vs Xsuite, Geant4 vs BDSIM, generator cross sections for the
di-Higgs 0.17 / 0.33 fb and the μLHC Higgs yields, HNL limits). Tolerances are stated per check and
may not be loosened without a documented investigation.

## 10. Risk assessment (34 entries, `registries/risk_register.csv`)

Highest-impact scientific risks: the white paper and workshop material are unavailable, so the
baseline may already have moved; the "5 % of μTRISTAN yield" assumption and the 2.2 × 10¹² proton
bunch population carry the luminosity claim; the luminosity model behind the published numbers is
not documented; nozzle acceptance versus forward physics is unquantified; no combined 2HDM+VLQ UFO
exists and the di-Higgs UFO is private. Process/data risks: snippet-only evidence, LLM extraction
errors (mitigated by the verification pass and schema rules), stale-result reuse, network and
compute limits, licence constraints (MAD-X binary, FLUKA registration, AloHEP unlicensed).

## 11. Files created (exact)

Root: `CLAUDE.md`, `README.md`, `LICENSE`, `LICENSE-DATA`, `CITATION.cff`, `pyproject.toml`,
`uv.lock`, `.env.example`, `docker-compose.yml`, `.gitignore` (extended).
`docs/`: `architecture.md`, `scientific_scope.md`, `validation_plan.md`,
`internet_research_protocol.md`, `synthetic_data_policy.md`, `fidelity_policy.md`,
`uncertainty_policy.md`, `security_policy.md`, `limitations.md`, `roadmap.md`,
`research_roadmap.md`, `software_inventory.md`, `reports/M1_evidence_audit.md`.
`research/`: `search_log.csv`, `source_registry.yaml`, `source_conflicts.yaml`,
`unresolved_searches.md`, `source_quality_policy.md`, `archived_metadata/*.json` (5),
`_fragments/` (per-family logs, source fragments, unresolved lists, five verification notes).
`references/primary/arXiv-2610.35154v1_Piotrzkowski_LHmuC_DIS2026.pdf` (CC BY-NC-ND 4.0);
`references/README.md`; other uploads git-ignored under `references/_local/`.
`schemas/`: `provenance`, `source`, `assumption`, `conflict`, `machine`, `component`, `material`,
`proposal`, `experiment`, `simulation_run`, `optimization` (`.schema.json`).
`parameters/`: 26 YAML files under `machine/`, `source/`, `acceleration/`, `interaction_region/`,
`detector/`, `proton_beam/`, `ion_beam/`, `physics_programme/`, `assumptions/`.
`registries/`: `parameter_registry.csv`, `assumption_registry.csv`, `missing_evidence.csv`,
`validation_registry.csv`, `risk_register.csv`.
`theory/benchmarks/{A_hnl_2610_28252,B_2hdm_vlq_2610_17801,C_dihiggs_leboho_kumar,D_two_photon_khanpour}/{proposal.yaml,README.md}`.
`lhmuc/{__init__,units,registry,analytical,__main__}.py`; `tools/{build_registries,validate_yaml,merge_research_fragments}.py`;
`tests/conftest.py`, `tests/unit/{test_schemas,test_units,test_registry_integrity}.py`,
`tests/scientific/test_analytical_checks.py`; placeholder `README.md` in `cad/`, `lattice/`,
`physics/`, `detector/`, `theory/`, `event_generation/`, `analysis/`, `optimization/`,
`uncertainty/`, `commissioning/`, `backend/`, `frontend/`, `results/`.

## 12. §49 status report

**A. Completed.** Files above; `lhmuc` package; 65 tests passing; `python -m lhmuc validate`:
0 errors, 0 warnings. No simulations were run (none are in scope for Phase 0).

**B. Evidence used.** Five uploaded documents read in full (page-referenced quotations for 807
records); 213 further sources registered at snippet/blocked level; applicability recorded per record.

**C. Assumptions.** 20 synthetic ranges (above); 19 analogous and 298 imported values flagged by
status; unresolved dependencies listed in `registries/missing_evidence.csv`.

**D. Validation.** P1 reproductions listed in §4 all pass within stated tolerances; the booster
survival model matches the published 82 % / 67 % to 0.4 percentage points; discrepancies found
and recorded, not tuned: the 20 µs train vs 10 µs revolution period; the absence of a visible
hourglass reduction in the μLHC luminosities; the factor-10 proton bunch population difference
between DIS2026 and μLHC/HL-LHC. One lead error (a factor-10 slip in the μLHC proton population
used in an early version of the luminosity check) was caught by the registry author and corrected
in the tests and in `CONF_LUMI_MODEL_ASSUMPTIONS`.

**E. Limitations.** Literature hosts blocked (no full-text verification of any non-uploaded source);
Geant4, BDSIM, FLUKA, MadGraph, ROOT, LHAPDF not installed; the HNL and 2HDM+VLQ papers and UFOs not
obtained; GitHub push blocked (403: Claude GitHub App not authorised for the repository) — commits
exist locally on the designated branch. See `docs/limitations.md`.

**F. Results.** Verified: the analytical reproductions in §4. Preliminary: the conflict and
missing-evidence registers. Interface-only: none (no demonstration data was produced).

**G. Next highest-value action.** Allow the literature hosts (list in
`docs/internet_research_protocol.md`), then run the fetch backlog in
`research/unresolved_searches.md` starting with the Kraków contributions and the μLHC erratum, and
clone `yefetu/ALOHEP` (reachable today) to reproduce 7.2 × 10³³ / 8.8 × 10³³ and settle
`CONF_LUMI_MODEL_ASSUMPTIONS`. That single step converts the largest block of `snippet_only`
evidence into verified values and is the prerequisite for Milestone 2 (sourced machine
configuration, analytical models, illustrative G0/G1 layout).
