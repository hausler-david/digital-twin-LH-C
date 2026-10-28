# Benchmark C — charged-current di-Higgs and anomalous Higgs couplings at mu+ p (Leboho, Kumar et al.)

**Record:** `proposal.yaml` (`PROP_C_DIHIGGS_MU_P`, schema `schemas/proposal.schema.json`).
**Source:** `SRC_WS_LEBOHO_KUMAR_DIHIGGS` — category `PRIMARY_LHMUC`, workshop slides "Probing anomalous Higgs
couplings at the future μ+p collider", 24 pages, dated 24 September 2026 (`research/source_registry.yaml`;
PDF `references/_local/Leboho_Kumar_Anomalous_Higgs_couplings_mu+p.pdf`, git-ignored).
**Status (2026-10-28):** `access: uploaded`, `review_state: extracted`. Extraction "LLM-assisted extraction from
uploaded slides" by Claude (Phase 0 audit); **not human-reviewed**.

## Status

Read in full. Unlike benchmarks A and B this one is an uploaded primary LHμC document, so every number in
`proposal.yaml` is quoted verbatim with a page number and may back `reported_lhmuc` (the actual parameter records
with provenance blocks are owned by the parameter agents: `parameters/physics_programme/lhmuc_dihiggs_benchmark.yaml`,
`parameters/detector/lhmuc_dihiggs_analysis_assumptions.yaml`, `parameters/machine/scenarios_dihiggs.yaml`). Two
cited documents were **not** read (arxiv.org / FeynRules blocked): Kumar et al. PLB 764 (2017) and the FeynRules HEL
model; everything said about them beyond the slide text is marked "(search snippet, unverified)".

## What is known (from the slides)

- **Model:** "HELv2" effective Lagrangian, UFO `effdihiggs-v2` (p.6); `L = L_SM + L_hhh + L_hWW + L_hhWW` with
  couplings g^(1,2)_hhh, g^(1,2)_hWW, g~_hWW, g^(1,2)_hhWW, g~_hhWW; SM limit g^(1)_hhh = 1, all others 0 (p.21).
  No new particles.
- **Collider:** μ+ at E_μ = 500 GeV and 1 TeV on E_p = 7 TeV, √s = 3.74 / 5.29 TeV, L = 1 ab^-1 (p.6);
  scenarios `LHMUC-DIHIGGS-500GEV` and `LHMUC-DIHIGGS-1TEV`. The 500 GeV configuration is the one of all
  tables; at 1 TeV only the coupling-scan cross sections exist.
- **Process:** μ+ p → h h j ν̄μ, h → bb̄ (CC W-fusion), final state 4b + forward jet + E_T^miss (p.5).
  σ_SM ≈ 0.17 fb (3.74 TeV) / ≈ 0.33 fb (5.29 TeV); 13-point g^(1)_hhh scan from −2.5 to +2.5 (p.7).
- **Generator:** MadGraph5_aMC v3.6.7, parton level, CTEQ6L1, 2.9 M events on CERN LXPLUS/EOS (p.6);
  12 % jet-energy smearing; b-tag as weights ε_b = 70 % (60 %, 90 % variants), mistag 1 % (p.9, p.22).
- **Backgrounds (p.8):** 4b, 2b, tt̄j hadronic and semi-leptonic, hbb̄j, hZj, ZZj with σ_CC, events/ab^-1 and MC
  counts; tt̄j and 2b enter via a mistag region with weight (0.01)²(0.7)² = 4.9e-5 (p.13).
- **Selection:** C1 ≥ 4 b + 1 light jet; C2 η(j1) < −1.5; C3 E_T^miss > 10 GeV; C4 m(4b) > 200 GeV;
  C5 105 < m(bb̄) < 145 GeV for both candidates (p.9). Full cut-flows at 70 % (p.12), 60 % (p.23), 90 % (p.24).
- **Results:** S ≈ 22.3, B ≈ 5.2, S/√(S+B) ≈ 4.25 at 1 ab^-1 and 70 % b-tag (3.12 at 60 %, 7.03 at 90 %).
  Expected 95 % CL intervals (1 / 10 ab^-1): g^(1)_hhh [−0.26, 1.40] / [−0.04, 1.19]; g^(1)_hWW [−0.16, 0.34] /
  [−0.08, 0.26]; g^(1)_hhWW [−0.052, 0.031] / [−0.037, 0.016] (p.15), from the fiducial cross section with
  s = Lε[σ(g) − σ_SM], b = L[εσ_SM + B], ε = 0.134, 5 % systematics, excluded if Z_A ≥ 1.96 (p.15).

Preserved, not resolved: p.9 describes Higgs candidates from "the b pairing minimising the distance to
mh = 125 GeV", p.17 says "Truth-based b-pairing (each b to its parent Higgs, no mass bias)". Minor rounding
differences (167 vs 166.7 events; B = 5.19 / 5.18 / ≈ 5.2) are listed in `proposal.yaml` notes.

## What is missing

- The UFO `effdihiggs-v2` (not public; `model_implementation.available: yes_private`). The public FeynRules HEL
  (or HEFT_DH) is only a partial stand-in in a different operator basis; a documented mapping would be needed.
- Process/run/parameter cards, scales, PDF identifier; detector simulation beyond parton level (no shower,
  hadronisation, jet clustering or b-tag model beyond flat weights); definition of Z_A and of the 5 % systematic.
- Cut-flow and limits at 1 TeV; anything at 2 TeV; the announced Δφ(E_T^miss, J) shape analysis and NN
  classifier; limits on g^(2)_hhh, g^(2)_hWW, g~_hWW, g^(2)_hhWW, g~_hhWW.
- Kumar et al. PLB 764 (2017) 247 (arXiv:1509.04016 — search snippet, unverified) for the cited e−p "Table 2".
- A luminosity assumption per LHμC scenario tied to the machine records (the slides assume a flat 1 ab^-1).

## Recasting to mu+ p

`original_initial_state_transfers_directly: true` — the schema note "always false for μ+μ− or pp originals" does
not apply because the original is itself a μ+ p study at LHμC energies. Four channels are listed, all
`proposed_unverified`: the original process at `LHMUC-DIHIGGS-500GEV` (reproduction target), at
`LHMUC-DIS2026-1TEV` (√s = 5.3 TeV), at `LHMUC-DIS2026-2TEV` (√s = 7.5 TeV, not studied on the slides), and an
LLM-proposed NC Z-fusion complement μ+ p → μ+ h h j that is not in the original study. Nothing has been
reproduced or computed in this project.

## Next action

1. Request `effdihiggs-v2` (version, checksum, licence) and the MG5 cards from the authors; until then record the
   HEL/HEFT_DH stand-in gap as an assumption, not a substitute.
2. Reproduce Configuration A with the obtained UFO: σ_SM ≈ 0.17 fb, the p.8 background table and the p.12
   cut-flow (tools, not the LLM); record as an immutable run.
3. Recompute efficiencies at the 1 TeV and 2 TeV scenarios with a documented luminosity assumption from the
   machine records; verify the NC channel at diagram level before any cross section.
4. Human review of `proposal.yaml` → `review_state: reviewed`.
