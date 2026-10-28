# Physics

**Status: not implemented (Phase 0 placeholder).** This directory exists so the agreed
architecture is visible; it contains no models, geometry, data or results yet.

Intended role: analytical and numerical beam-physics models: beam dynamics, luminosity (including hourglass, decay averaging, beam-beam), muon decay losses per metre, radiation proxies. Phase 0 keeps the audit arithmetic in `lhmuc/analytical.py`; it moves here in Milestone 2.

Entry criterion: Milestone 2.

Rules that apply once populated (see `CLAUDE.md`): every numeric input must carry a
provenance record; every geometry object a G-label; every physical model a P-label; synthetic
inputs must be declared in `parameters/assumptions/` and surfaced in outputs.
