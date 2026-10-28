# Lattice

**Status: not implemented (Phase 0 placeholder).** This directory exists so the agreed
architecture is visible; it contains no models, geometry, data or results yet.

Intended role: accelerator optics descriptions for MAD-X, Xsuite and Bmad, generated from the parameter model; validation against analytical optics. BDSIM is not used for optics design.

Entry criterion: Milestone 2+ once IR and ring parameters have provenance; lattice elements for LHμC are currently unknown.

Rules that apply once populated (see `CLAUDE.md`): every numeric input must carry a
provenance record; every geometry object a G-label; every physical model a P-label; synthetic
inputs must be declared in `parameters/assumptions/` and surfaced in outputs.
