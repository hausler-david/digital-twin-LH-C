# References

**Status: not implemented (Phase 0 placeholder).** This directory exists so the agreed
architecture is visible; it contains no models, geometry, data or results yet.

Intended role: archived source documents by domain. Only documents whose licence permits redistribution are committed; others live in git-ignored `references/_local/` and are described by `research/archived_metadata/*.json` (title, SHA-256, licence).
*[2026-10-29, owner decision:]* connector-delivered texts (`access: fetched_text`) are always kept in `references/_local/<source_id>/`, never committed and not sent anywhere, whatever the paper's licence; `research/archived_metadata/<source_id>.json` records the SHA-256 of the delivered text (`docs/internet_research_protocol.md` §5a, §6).

Entry criterion: Phase 0 (active).

Rules that apply once populated (see `CLAUDE.md`): every numeric input must carry a
provenance record; every geometry object a G-label; every physical model a P-label; synthetic
inputs must be declared in `parameters/assumptions/` and surfaced in outputs.
