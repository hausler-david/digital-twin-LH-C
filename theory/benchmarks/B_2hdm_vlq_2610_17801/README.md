# Benchmark B — CP-odd Higgs A → ZZγ in the 2HDM with vector-like quarks (arXiv:2610.17801)

**Record:** `proposal.yaml` (`PROP_B_2HDM_VLQ_2610_17801`, schema `schemas/proposal.schema.json`)
**Source:** `SRC_ARXIV_2610_17801` — category `UNVERIFIED`, access `pending_fetch` (fetch refused on arxiv.org in the
audit session; re-attempt pending). **Review state:** `pending_fetch`. **Extraction:** search snippets only, Claude
(Phase 0 audit), 2026-10-28, not reviewed.

## Status

Not read. The paper was neither uploaded nor fetchable (arxiv.org, INSPIRE and mirrors blocked). Every content
statement in `proposal.yaml` is a search-engine snippet of the arXiv abstract, quoted verbatim from
`research/_fragments/theory-benchmarks_sources.yaml` and marked "(search snippet, unverified)". No parameter record
is derived from it; no number here may back a `reported_lhmuc` status, and confidence is capped at `medium`.

## What is known (snippet level only)

- First one-loop calculation of A → ZZγ in the 2HDM and in the 2HDM extended with vector-like quarks
  ("we present the first results for the one-loop decay A→ZZγ in the Two-Higgs-Doublet Model and its extension
  with Vector-Like Quarks").
- Branching ratios "can reach 10^{-5}-10^{-4} for several benchmark points within the viable parameter space".
- VLQ loops "can modify the total rates by approximately 5%".
- Polarized and unpolarized final-state Z bosons are treated.
- Collider context is a remark only: "With the high luminosities expected at future multi-TeV muon colliders, these
  effects may be experimentally accessible." There is **no collider simulation**, no production cross section, no
  event selection and no luminosity in the paper.

## What is missing

- The full text: 2HDM Yukawa type, VLQ representations, benchmark-point values (m_A, m_H, m_H±, tan β, alignment
  angle, m_VLQ, mixings), partial widths and BRs per benchmark, any code or form-factor release. Title wording,
  author affiliations and the v1 date are themselves unconfirmed.
- A model implementation: no combined 2HDM+VLQ UFO was found; only separate 2HDM (2HDM_NLO, ycwu1030/2HDM_FR,
  Pseudoscalar_2HDMI) and generic VLQ (VLQ_UFO) models exist, all seen as snippets with licences unseen. The decay
  is loop-induced, so a loop-capable implementation (MadGraph5_aMC@NLO loop-induced mode with an NLO-ready UFO, an
  effective AZZγ vertex from the paper's form factors, or an independent FeynArts/FormCalc/LoopTools calculation) is
  required in any case.
- A production mode for A in μ⁺p collisions — the paper supplies none. Candidates recorded as
  `proposed_unverified`: neutral-current associated production μ⁺q → μ⁺qA (Yukawa-mediated), charged-current
  μ⁺q → ν̄q′A (e.g. μ⁺b → ν̄tA, charge-checked), ZZ/Zγ* fusion (vanishes at tree level for a CP-odd scalar — must
  be checked), and two-photon γγ → A (loop-induced; LHμC photon fluxes would come from the Khanpour deck). b b̄ fusion
  and gluon fusion are `rejected` as structurally absent in μ⁺p.
- ZZγ final-state reconstruction requirements (isolated photon, two Z candidates, A mass reconstruction, forward
  acceptance) against the LHμC detector concept; SM ZZγ backgrounds; the signal-yield arithmetic
  σ(A) × L_int × BR(A→ZZγ) × BR(Z decays) × acceptance, which cannot be evaluated while σ(A) is unknown.

## Next action

1. Fetch `https://arxiv.org/abs/2610.17801` (abstract page and PDF) once arxiv.org is reachable; confirm metadata,
   then re-extract `proposal.yaml` from the full text (benchmark points, widths, model definition, code statement)
   and move `review_state` to `extracted` for human review.
2. Decide whether a combined 2HDM+VLQ loop-capable model is worth building; if yes, first reproduce the published
   partial widths at the benchmark points (the only closure test the original study offers) before any μ⁺p recast.
3. Only then compute σ(μ⁺p → A X) for the candidate channels at the LHμC scenario parameters and judge whether a
   BR of 10⁻⁵–10⁻⁴ yields any events. Until a channel reaches `cross_section_computed`, no P-level above P0 may be
   attached to this benchmark.
