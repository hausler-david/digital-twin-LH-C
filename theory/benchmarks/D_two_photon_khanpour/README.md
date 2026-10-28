# Benchmark D — Two-photon (γγ) physics in μ⁺p collisions (Khanpour, Kraków workshop deck)

**Record:** `proposal.yaml` (`PROP_D_TWO_PHOTON_MU_P`, schema `schemas/proposal.schema.json`)
**Source:** `SRC_WS1681458_KHANPOUR_GAMMAGAMMA` — H. Khanpour (AGH), "Two-Photon Physics at the LHμC",
Ultra-cold muons for the LHC, AGH Kraków, 24–26 Sept 2026, 26 slides, category `PRIMARY_LHMUC`,
`access: uploaded`, read in full (slide images of p.4, p.15, p.19, p.22 inspected).
**Review state:** `extracted` — LLM-assisted extraction by Claude (Phase 0 audit), 2026-10-28, **not human-reviewed**.

## Status

This is the only one of the theory benchmarks whose source was uploaded and read in full, and the only one
whose original study is already a μ⁺p (LHμC) study, so the initial state transfers directly. It is an
unrefereed workshop deck: the quantitative curves are credited to Forthomme, Khanpour, Piotrzkowski and
Yamazaki, "High energy γγ interactions at the LHeC (in preparation)", and the working points to the
"HELP4CERN White Paper (in preparation)" — neither is available. The deck itself states that no projected
limit exists yet ("a quantitative projected limit still requires a dedicated detector-level statistical
analysis", p.18).

## What is known (quoted verbatim in `proposal.yaml`, with slide numbers)

- **Model:** SM + SMEFT. Dimension-6 τ dipole operators (C_τB/Λ², C_τW/Λ²) giving anomalous a_τ and d_τ
  (p.16); dimension-8 aQGC decomposition f_S,j / f_M,j / f_T,j over Λ⁴ with the single benchmark
  f_M2/Λ⁴ = 1 TeV⁻⁴ (p.20–21); τ benchmark deformation δa_τ = 0.005 (p.18). Operator definitions and
  normalisation conventions are not on the slides.
- **Working points (p.4):** E_μ = 500 GeV / 1 TeV / 2 TeV with E_p = 7 TeV, √s ≃ 3.7 / 5.3 / 7.5 TeV,
  L_int = 250 / 1000 / 1000 fb⁻¹; LHeC comparison at E_e = 20, 50 GeV (√s 1.2 TeV).
  These map to `LHMUC-WP-OPT1-500GEV`, `LHMUC-WP-BASELINE-1TEV`, `LHMUC-WP-OPT2-2TEV`
  (`parameters/machine/scenarios_wp.yaml`, parameter agents).
- **Formalism:** EPA factorisation σ_ℓp = ∫ dW S_γγ(W) σ_γγ(W); elastic (dipole form factors) and
  proton-dissociative (F2-based) proton fluxes; point-like μ⁺ flux with muon-mass Q²_min (p.9–11).
- **Numbers:** elastic γγ → τ⁺τ⁻ for W0 = 10 GeV: 50.4 / 58.5 / 70.3 pb at LHeC 1.2 TeV / LHμC 3.7 TeV /
  LHμC 5.3 TeV (p.15). Elastic γγ → W⁺W⁻: 0.037 / 0.166 pb at 1.2 / 3.7 TeV, i.e. ≃ 9.3 × 10³ and
  ≃ 4.2 × 10⁴ produced pairs at an illustrative 250 fb⁻¹, before BRs, acceptance and efficiencies (p.19).
  Inclusive (non-γγ) ℓp Higgs/top cross-section table and enhancement factors ∼4.5 / 12 / 13 / 69 (p.5).
  Current a_τ limits as quoted on p.18: CMS [−0.0022, 0.0041] (arXiv:2406.03975), ATLAS [−0.0024, 0.0047]
  at 95 % CL (arXiv:2503.19836) — the two papers were **not** fetched (arxiv.org blocked); nothing beyond
  the deck's sentence is asserted about them.
- **Other channels (no numbers):** loop-induced γγ → ZZ, γγ → t t̄ (figure only), γγ → H, charged higgsino
  pairs (figure only, model point unknown), γγ → ℓ⁺ℓ⁻ calibration, light-by-light.
- **Detector requirements (p.26, qualitative):** wide central tracking and lepton acceptance with robust τ
  reconstruction; W/Z/t reconstruction; exclusivity and acoplanarity; missing momentum; scattered-muon
  measurement; forward proton tagging and proton-dissociation control.

The corresponding parameter records (`PHYS_XSEC_EL_GG_*_WP`, `PHYS_NWW_*_WP`, `PHYS_ATAU_*_WP`,
`PHYS_AQGC_FM2_BENCHMARK_WP`, `DET_GG_*_WP`, …) are owned by the parameter agents; this record creates none.

## What is missing

- The in-preparation paper and White Paper; the EPA code/generator; the F2 parametrisation; the elastic
  Q_ℓ² / Q_p² cuts (in figure legends, not legible); the M_N range.
- Operator definitions/normalisation for f_M2 and the (C_τB, C_τW, Λ) ↔ δa_τ mapping.
- W⁺W⁻ cross sections at 5.3 and 7.5 TeV; every ZZ / t t̄ / H / higgsino / ℓ⁺ℓ⁻ / γγ number; the
  unspecified "LHC" configuration of p.21.
- Any event selection, background, efficiency, statistical method or projected limit (none exist, p.18).
- A verified model implementation: `model_implementation.available: partial` — public EPA tools, SMEFT
  dipole UFOs and dimension-8 aQGC UFOs are believed to exist (prior knowledge, unverified; no network and
  nothing downloaded), but the speaker's actual set-up, versions and licences are unknown.
- Quantified detector-concept values to set against the p.26 requirements.

## Recasting to μ⁺p

Transfers directly (`original_initial_state_transfers_directly: true`). Eight candidate channels are listed
(τ⁺τ⁻ with dipoles, W⁺W⁻ with aQGC, ZZ, t t̄, H, higgsino pairs, ℓ⁺ℓ⁻ calibration, light-by-light), all
`proposed_unverified`: nothing has been checked at diagram level or run through a generator here.

## Next action

1. Reproduce the five tabulated elastic cross sections (p.15, p.19) with a documented EPA tool run
   (point-like μ⁺ flux with muon-mass Q²_min, dipole proton form factors, W0 = 10 GeV for τ⁺τ⁻), recording
   the Q² cuts as assumptions until the in-preparation paper fixes them; only then attach a P-level above P0.
2. Obtain and inspect (checksum, licence) a SMEFT dipole UFO and an aQGC UFO; match the f_M2 convention
   before comparing with the p.21 EFT/SM ratios.
3. Request the Forthomme–Khanpour–Piotrzkowski–Yamazaki paper / HELP4CERN White Paper numbers; fetch
   arXiv:2406.03975 and 2503.19836 once arxiv.org is reachable to confirm the quoted a_τ intervals.
4. Human review → `review_state: reviewed`.
