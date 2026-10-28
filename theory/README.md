# Theory

**Status: not implemented (Phase 0 placeholder).** This directory exists so the agreed
architecture is visible; it contains no models, geometry, data or results yet.

Intended role: proposal importer, model records, UFO handling, muon-proton process builder, recasting engine and benchmark records. `theory/benchmarks/` already holds Phase 0 proposal records (extracted/pending state only).

Entry criterion: Milestone 3.

Rules that apply once populated (see `CLAUDE.md`): every numeric input must carry a
provenance record; every geometry object a G-label; every physical model a P-label; synthetic
inputs must be declared in `parameters/assumptions/` and surfaced in outputs.
