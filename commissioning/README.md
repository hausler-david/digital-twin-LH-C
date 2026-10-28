# Virtual commissioning

**Status: not implemented (Phase 0 placeholder).** This directory exists so the agreed
architecture is visible; it contains no models, geometry, data or results yet.

Intended role: virtual devices, fault scenarios, orbit correction and machine protection. Speculative virtual controls must be separated from hardware-specification-based interfaces.

Entry criterion: Later milestone; no hardware specifications exist for LHμC.

Rules that apply once populated (see `CLAUDE.md`): every numeric input must carry a
provenance record; every geometry object a G-label; every physical model a P-label; synthetic
inputs must be declared in `parameters/assumptions/` and surfaced in outputs.
