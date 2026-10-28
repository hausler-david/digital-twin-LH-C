# Detector

**Status: not implemented (Phase 0 placeholder).** This directory exists so the agreed
architecture is visible; it contains no models, geometry, data or results yet.

Intended role: fast parametric detector (Level 1), Geant4/BDSIM regional simulation (Level 2), beam-induced background models and reconstruction. The μLHC detector sketch and the LHeC detector are the only documented starting points.

Entry criterion: Milestone 2 (fast detector schema), Milestone 3 (HNL benchmark).

Rules that apply once populated (see `CLAUDE.md`): every numeric input must carry a
provenance record; every geometry object a G-label; every physical model a P-label; synthetic
inputs must be declared in `parameters/assumptions/` and surfaced in outputs.
