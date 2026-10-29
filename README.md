# LHμC-VirtualLab

**An engineering-aware 3D digital twin, theory-recasting, experiment-driven collider co-design
and optimization platform for the proposed LHμC muon-proton collider at CERN.**

Project owner: David Hausler, Independent Researcher, Czech Republic.

> **Status (2026-10-29): Phase 0 — evidence and feasibility audit, with the addendum of uploaded
> documents. No digital twin exists.**
> This repository contains a sourced parameter database — 5601 records, 5578 of them with page-level
> provenance from 34 uploaded documents (the DIS2026 and μLHC papers, 14 Kraków workshop decks, related-machine
> papers such as μTRISTAN, the muon-ion collider, LHeC and MuCol reports, the J-PARC source-chain
> measurements, the AloHEP method paper and the MuCol vFFA report) and the other 23 synthetic ranges
> with assumption records or derived values with derivations; each sourced record was verified against
> the page images by an independent agent but not yet reviewed line by line by a human — together with
> provenance schemas, research logs, policy documents and a validation package of analytical (P1)
> cross-checks only (151 tests at commit `104073c`; 177 at `000f236`, which adds the batch-10 and
> MuCol MR7 luminosity-arithmetic checks). Since 2026-10-29 the validator rejects confidences above the
> source-quality caps and P1 labels without a registered test. There is no CAD, no lattice, no event
> generation, no detector simulation and no user interface. Values taken from workshop slides are
> reported in workshop material and unverified by simulation; everything that is unknown is recorded
> as unknown. What the uploads changed, and what they did not: `docs/reports/M1_addendum_uploaded_documents.md`
> (draft) and `docs/limitations.md` §10.

## What LHμC is (as reported by its proponents)

The LHμC concept (HELP4CERN Study Group, K. Piotrzkowski, PoS DIS2026, arXiv:2610.35154)
collides a 1 or 2 TeV positive-muon beam with the 7 TeV LHC proton beam, giving μ⁺p
centre-of-mass energies of 5.3 or 7.5 TeV at an average luminosity "close to 10³⁴ cm⁻²s⁻¹".
Muons come from an ultra-cold μ⁺ source (muonium formation and laser ionisation, as developed
at J-PARC/KEK), are accelerated rapidly in a booster that reuses the LHeC energy-recovery-linac
infrastructure plus vertical fixed-field alternating-gradient (vFFAG) beamlines, and are stored in
a ≈3 km main ring tangential to the LHC. The predecessor μLHC study (Akturk et al., PTEP 2026
033C04, arXiv:2506.15445) gives the only published beam-optics-level parameter tables for such a
machine. See `docs/scientific_scope.md` for the sourced summary and `docs/limitations.md` for
what is not known.

## Repository map

| Path | Content (Phase 0) |
|---|---|
| `CLAUDE.md` | Binding working rules: no fabrication, null ≠ 0, provenance statuses, fidelity labels |
| `docs/` | architecture, scientific scope, validation plan, research protocol, synthetic-data, fidelity, uncertainty and security policies, limitations, roadmaps, software inventory, milestone reports |
| `research/` | `search_log.csv`, `source_registry.yaml`, `source_conflicts.yaml`, `unresolved_searches.md`, `source_quality_policy.md`, `archived_metadata/` (SHA-256 and licence of every archived file) |
| `references/` | archived documents whose licence permits redistribution (others are git-ignored under `references/_local/`) |
| `schemas/` | JSON Schema 2020-12: provenance/parameter, source, assumption, conflict, machine scenario, component, material, proposal, experiment, simulation run, optimization |
| `parameters/` | **single source of truth**: parameter records with provenance, scenarios, assumptions (synthetic ranges), materials |
| `registries/` | generated CSV views (`parameter_registry.csv`, `assumption_registry.csv`) and authored registries (`missing_evidence.csv`, `validation_registry.csv`, `risk_register.csv`) |
| `theory/benchmarks/` | proposal records for benchmarks A (HNL, pending fetch), B (2HDM+VLQ, pending fetch), C (di-Higgs μ⁺p, uploaded), D (two-photon physics, uploaded) |
| `lhmuc/` | Python package: units, registry loader/validator, audit arithmetic (P1) |
| `tools/` | `build_registries.py`, `validate_yaml.py`, `merge_research_fragments.py` |
| `tests/` | unit, scientific (P1 reproductions), integrity tests |
| other directories | architecture placeholders with a README stating "not implemented" |

## Quick start

```bash
uv sync --extra dev
uv run python -m lhmuc validate          # validates every registry, prints provenance counts
uv run python tools/build_registries.py  # regenerates registries/*.csv from parameters/**
uv run pytest                            # schema, integrity and scientific P1 tests
```

## Provenance in one glance

Every number in `parameters/` has one status:
`reported_lhmuc` · `derived_lhmuc` · `imported_related` · `analogous` · `analytical_estimate` ·
`synthetic` · `scan_variable` · `unknown` — and a source with page, table and verbatim quotation
where applicable. Synthetic values are ranges with an assumption record. Search-snippet
evidence never backs a reported value. Conflicts between sources are kept as separate scenarios
(`research/source_conflicts.yaml`).

## Licences

Code: Apache-2.0 (`LICENSE`). Data, documentation and registries: CC BY 4.0 (`LICENSE-DATA`).
Third-party documents keep their own licences (`research/archived_metadata/`).

## Citation

See `CITATION.cff`. Please also cite the primary LHμC sources listed there.
