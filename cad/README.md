# CAD

**Status: not implemented (Phase 0 placeholder).** This directory exists so the agreed
architecture is visible; it contains no models, geometry, data or results yet.

Intended role: parameter-driven boundary-representation geometry (Open Cascade / CadQuery / build123d), STEP master geometry, healing, glTF export, simplified simulation geometry and GDML export, overlap checks. Subfolders: generators, step, gdml, gltf, meshes, drawings, validation.

Entry criterion: Milestone 2 (illustrative G0/G1 layout, parameterised IR and nozzle placeholders).

Rules that apply once populated (see `CLAUDE.md`): every numeric input must carry a
provenance record; every geometry object a G-label; every physical model a P-label; synthetic
inputs must be declared in `parameters/assumptions/` and surfaced in outputs.
