# Benchmark A — heavy neutral lepton, arXiv:2610.28252

**Proposal record:** `proposal.yaml` (`PROP_A_HNL_2610_28252`, schema `schemas/proposal.schema.json`).
**Source:** `SRC_ARXIV_2610_28252` (entry owned by the research agents, `research/source_registry.yaml`).
**Status (2026-10-28):** `access: pending_fetch`, `review_state: pending_fetch`. Extraction method
"search snippets only" by Claude (Phase 0 audit); **not human-reviewed**.

## What is known (search snippets only, unverified)

The paper was not uploaded and arxiv.org / inspirehep.net were blocked, so nothing was read from the
paper itself. From search-engine snippets (quoted verbatim in `proposal.yaml`):

- Title "Probing a heavy neutral lepton in a radiative neutrino model at a muon collider"; authors
  Bamwidhi, Belfkir, Loualidi, Nasri; arXiv:2610.28252v1 [hep-ph], 20 Oct 2026.
- Model: a **Dirac** heavy neutral lepton in a **radiative neutrino-mass model** (not Type-I seesaw
  as first hypothesised). Direct and Higgs-mediated production, same final state.
- Original collider: mu+ mu-, sqrt(s) = 3 TeV, 1 ab^-1, unpolarised beams; MadGraph5_aMC@NLO with
  lepton ISR and the equivalent photon approximation; detector-level analysis with a classifier.
- Results: median expected 95 % CL limits on the visible cross section 0.027–0.113 fb, mapping to
  |U_muN|^2 about 6.7e-6 to 8.3e-5 across six benchmark points; the Higgs channel gives 15–72 % of the
  selected signal but improves the limits by only 0.18–1.19 %.

Snippet-only evidence is capped at confidence medium and never backs `reported_lhmuc`.

## What is missing

- The paper (abstract page not even read); the Lagrangian / field content of the radiative model
  (companion paper arXiv:2609.08808 by the same authors is a lead, unread).
- The benchmark table: six HNL masses (a search-tool paraphrase "about 103–119 GeV" was **not** shown
  verbatim and is recorded only as an unconfirmed lead, value `null`), mixings, widths, scalar-sector
  parameters; N decay channels and branching ratios.
- A UFO for the radiative model (none confirmed). FeynRules HeavyN (Dirac LO variant) is only a
  partial stand-in: it reproduces mixing-driven production/decays but has no radiative-model scalar
  sector, so the Higgs-mediated channel cannot be reproduced with it.
- Original cut-flow, backgrounds, classifier definition.
- The LHμC scenario record to recast onto, proton PDF and photon-flux choices.

## Recasting to mu+ p

The mu+ mu- initial state does not transfer. Four LLM-proposed channels are listed in
`proposal.yaml` with status `proposed_unverified` (charged-current mu+ q -> N(bar) q';
neutral-current Z radiation with Z -> N nu; W-fusion Higgs production with H -> N nu;
photoproduction mu+ gamma -> N(bar) W+). None has been checked at diagram level or computed.

## Next action

1. Fetch arXiv:2610.28252 (and 2609.08808) once arxiv.org is allowed; record SHA-256 and licence;
   update `access` to `fetched` (or `uploaded`) and `review_state` to `extracted`.
2. Fill the model, benchmark-table, decay and generator fields from the paper with page-numbered
   quotations; confirm or reject the 103–119 GeV paraphrase.
3. Decide on a UFO (paper's own vs. HeavyN partial stand-in with documented gap), then verify the
   candidate mu+ p channels with a diagram tool and compute cross sections (tools, not the LLM).
4. Human review -> `review_state: reviewed`.

Note: `python -m lhmuc validate` reports "unknown source SRC_ARXIV_2610_28252" for this proposal
until the research agents merge the source fragment into `research/source_registry.yaml`.
