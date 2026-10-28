# Unresolved items — reconnaissance family `theory-benchmarks`

Searches run 2026-10-28 with WebSearch only (23 queries, 18 sources surfaced). WebFetch attempts were refused by
network policy on arxiv.org, export.arxiv.org, www.alphaxiv.org, api.semanticscholar.org, inspirehep.net,
cp3.irmp.ucl.ac.be and events2.saip.org.za. One URL (github.com/ycwu1030/2HDM_FR) was never fetched although
the journal marks `fetch_blocked=false`; it is therefore `snippet_only`. Everything below is snippet-level
evidence: it may not back a `reported_lhmuc` status and is capped at confidence `medium` (CLAUDE.md §1.5).
Nothing in this file or in `theory-benchmarks_sources.yaml` is a parameter record; the `snippet-quoted` lines
there are leads to verify once the hosts are allowed.

Scope of the family: the two October-2026 theory papers proposed as LHμC physics benchmarks (arXiv:2610.28252,
heavy neutral lepton; arXiv:2610.17801, CP-odd Higgs A → ZZγ in 2HDM+VLQ), the UFO / FeynRules models needed to
recast them, and the `effdihiggs-v2` / `HELv2` model behind the uploaded di-Higgs deck
(`SRC_WS_LEBOHO_KUMAR_DIHIGGS`).

## Unresolved items

- **No full text or abstract page of any source was read.** All titles, authors, dates, abstract sentences and
  numbers come from search-result snippets or the search tool's own summaries. arxiv.org and inspirehep.net must
  be allowed before any of it can be confirmed.
- **arXiv:2610.28252 (HNL) is not a Type-I seesaw paper.** Snippets describe a *Dirac* heavy neutral lepton in a
  radiative neutrino-mass model at a 3 TeV μ⁺μ⁻ collider (1 ab⁻¹, unpolarized). The task hypothesis
  ("Type-I seesaw, displaced vertex") was not supported. Still unconfirmed: the six benchmark HNL masses (the
  search tool paraphrased "about 103–119 GeV" — not shown verbatim, deliberately not recorded), the mixing
  values per benchmark, the scalar content of the radiative model, and whether a public UFO exists (no mention
  found). Companion paper arXiv:2609.08808 (same four authors per summary) likely defines the model — unread.
- **arXiv:2610.17801 (A → ZZγ, 2HDM+VLQ) contains no collider simulation.** It is a one-loop decay-width
  calculation; its only collider remark is "future multi-TeV muon colliders". Unconfirmed: 2HDM type
  (I/II/X/Y), VLQ representations (singlet/doublet), explicit benchmark points (m_A, tan β, VLQ masses), whether
  a UFO exists. The v1 date (13 Oct 2026) and affiliations (HCMUS, DTU, EIU) are from the search summary, not a
  verbatim snippet. Recasting it as an LHμC benchmark would need a production mode for A in μp collisions that
  the paper does not supply.
- **Access mode for the two target papers.** The lead's note reads "(access pending_fetch)"; the journal,
  however, documents an attempted WebFetch refused by network policy on arxiv.org, so both records carry
  `access: blocked` (the schema's definition of an attempted, refused fetch) with the pending re-attempt noted.
  The lead may flip these to `pending_fetch` if a different reading was intended.
- **Category of the two target papers.** Kept `UNVERIFIED` per lead decision (unrefereed and unread) although
  their existence and metadata are confirmed by arXiv listing snippets. Re-classify (arxiv_preprint, possibly
  PEER_REVIEWED later) only after the abstract pages are read.
- **No INSPIRE literature record** was returned for either arXiv id (probable indexing lag); INSPIRE API fetch
  blocked.
- **`effdihiggs-v2` / `HELv2` UFO has no public hosting location** in any result (not on the FeynRules wiki,
  GitHub or Zenodo). Only the SAIP slide deck (contribution 653, slides PDF `Di_Higgs_at_the_LHC (9).pdf`) names
  "effdihiggs-v2 UFO model" / "HELv2 effective Lagrangian" alongside Kumar et al. arXiv:1509.04016 and a muon beam
  (up to 1 TeV) on 7 TeV protons. Presenter, date and exact wording are unverified (fetch blocked). The
  reproduction path for the di-Higgs benchmark therefore still depends on obtaining the UFO from the authors
  (as already recorded in `SRC_WS_LEBOHO_KUMAR_DIHIGGS.unresolved_questions`). The documented ancestor is the
  FeynRules HEL model (Alloul, Fuks, Sanz, arXiv:1310.5150); HEFT_DH is an adjacent NLO alternative, not the
  same model.
- **SAIP deck id shared with the `lhmuc-primary` fragment.** This family surfaced the slides-PDF URL; the sibling
  fragment registers the contribution-page URL under `SRC_URL_SAIP2026_653_NKADIMENG_DIHIGGS`. The same id is
  used here so `tools/merge_research_fragments.py` unions the two records (lists merged, first text kept) rather
  than creating a duplicate source. The lead should confirm that the merged `url` (contribution page) is the
  preferred canonical one and that the PDF URL survives in `version`/`notes`.
- **No public combined 2HDM+VLQ UFO exists in the results.** Only separate models were found: 2HDM_NLO
  (FeynRules NLOModels), ycwu1030/2HDM_FR (Zenodo 10.5281/zenodo.8207058, v0.5.1), Pseudoscalar_2HDMI
  (arXiv:2404.05704) and the generic VLQ_UFO. A recast would require building or obtaining a combined model.
  The Benbrik–Moretti 2HDM-II+VLQ series (arXiv:2403.13021 and the ids 2401.16219, 2409.20104, 2211.07259 named
  in its snippet) is a candidate source of conventions; no UFO release confirmed.
- **2HDMC (Eriksson, Rathsman, Stål) UFO/MadGraph interface**: not found in results.
- **HeavyN as HNL stand-in.** The FeynRules HeavyN family (Majorana and Dirac variants, LO/NLO; defaults
  300 GeV, 500 GeV, 1 TeV, 15 free parameters) is the obvious public UFO for a Dirac-HNL recast, but it has no
  radiative-model scalar sector, so the Higgs-mediated channel of arXiv:2610.28252 (15–72 % of the selected
  signal per snippet) is probably not reproducible with it. Download path pattern
  `https://feynrules.irmp.ucl.ac.be/raw-attachment/wiki/HeavyN/<filename>` is snippet-level.
- **Journal (peer-review) status not confirmed** for arXiv:1412.6955 ("Automated Two Higgs Doublet Model at
  NLO", kept PEER_REVIEWED as the journal classified it — candidate for downgrade to UNVERIFIED), arXiv:1602.06957
  (HeavyN usage reference, not registered as a source), arXiv:2301.07117 and arXiv:2510.18390 (APS DOI
  `10.1103/prx6-wnwr` snippet-level). JHEP references for arXiv:1310.5150 (JHEP 04 (2014) 110) and
  arXiv:2306.17368 (JHEP 09 (2023) 131) are from snippets without DOIs.
- **Category of ycwu1030/2HDM_FR.** The journal classified a community GitHub repository as
  OFFICIAL_SOFTWARE_DOCUMENTATION; the lead may prefer SECONDARY_SOURCE. Kept as classified, flagged in `notes`.
- **Query → source attribution is inferred.** The journal does not map queries to sources; `discovered_by_queries`
  was filled only where a query note names the source's identifier or a value unique to it. The CSV therefore has
  one row per query plus one "(see family queries)" row per source.
- **arXiv ids named in query notes but not registered as sources** (not added, per instructions): 2301.02602,
  2606.19906, 2602.05158 (muon-collider HNL), 1901.03709, 1507.07020 (2HDM+VLQ background), 2411.15303
  (same-sign muon collider HNL), 1406.3030 (2HDM_NLO reference), 1602.06957 and 1812.08750 (HeavyN references),
  2401.16219, 2409.20104, 2211.07259 (Benbrik–Moretti series). They are leads for a later pass, not sources.
- **Applicability to the LHμC.** Every physics number quoted in this family (3 TeV μ⁺μ⁻, 1 ab⁻¹, |U_μN|² limits
  6.7×10⁻⁶–8.3×10⁻⁵, BR(A→ZZγ) 10⁻⁵–10⁻⁴, g_hhh precision at FCC-he) refers to a *different* collider. None of it
  may enter an LHμC parameter record as anything other than `imported_related`/`analogous` with an explicit
  applicability explanation, and only after the full text is read.

## Fetch backlog

Fetch each once the host is allowed; record page, section and verbatim quotation for every number.

- `https://arxiv.org/abs/2610.28252` (and PDF / HTML version) — confirm title, authors, v1 date 20 Oct 2026,
  licence; extract the six benchmark points (HNL masses, mixings), the radiative model's field content, collider
  set-up (3 TeV, 1 ab⁻¹, unpolarized), MadGraph5_aMC@NLO/ISR/EPA settings, the 95 % CL visible-cross-section and
  |U_μN|² limits, the Higgs-channel share; look for a UFO/FeynRules model statement and a data/code availability
  note. Then re-decide category (UNVERIFIED → PEER_REVIEWED only on journal acceptance).
- `https://arxiv.org/abs/2609.08808` — companion model paper: Lagrangian, scalar sector, parameter names; confirm
  it is the model used in 2610.28252.
- `https://arxiv.org/abs/2610.17801` (and PDF) — confirm authors/affiliations and v1 date 13 Oct 2026; extract
  2HDM type, VLQ representations, benchmark points (m_A, tan β, m_VLQ, mixing), partial widths and BRs
  (unpolarized/polarized Z), the ~5 % VLQ effect, any UFO/code statement.
- `https://inspirehep.net/api/literature?q=arxiv:2610.28252` and `…arxiv:2610.17801` — INSPIRE records, citation
  metadata, journal status.
- `https://cp3.irmp.ucl.ac.be/projects/feynrules/wiki/HeavyN` — package list (SM_HeavyN_NLO_UFO.tgz,
  SM_HeavyN_Gen3Mass_NLO.tgz, SM_HeavyN_CKM_AllMasses_LO.tgz, SM_HeavyN_Dirac_CKM_Masses_LO_UFO.tgz), default
  masses/parameters, licence, download URLs, SHA-256 of the archive to be registered in
  `research/archived_metadata/`.
- `https://cp3.irmp.ucl.ac.be/projects/feynrules/wiki/VLQ` (and its singlet-T, (T,B), (X,T), singlet-B subpages)
  — Lagrangian, particle content X/T/B/Y, default widths (snippet: 1 GeV, must be set manually), licence,
  download.
- `https://cp3.irmp.ucl.ac.be/projects/feynrules/wiki/NLOModels` — 2HDM_NLO entry: UFO download, reference
  arXiv:1406.3030, parameter conventions, licence.
- `https://arxiv.org/abs/1412.6955` — confirm authors, title, journal status (decides PEER_REVIEWED vs
  UNVERIFIED); 2HDM NLO UFO conventions.
- `https://raw.githubusercontent.com/ycwu1030/2HDM_FR/master/README.md` (reachable now) and
  `https://github.com/ycwu1030/2HDM_FR` — README, licence file, parameter convention, Zenodo DOI
  10.5281/zenodo.8207058 / version 0.5.1 confirmation.
- `https://arxiv.org/abs/2404.05704` — confirm authors/date; Pseudoscalar_2HDMI UFO availability and restriction
  cards (adjacent model only).
- `https://cp3.irmp.ucl.ac.be/projects/feynrules/wiki/HEL` — HEL.fr / HEL_UFO operator list, default coupling
  value 0.1, licence, download; check for any "HELv2" mention.
- `https://arxiv.org/abs/1310.5150` — confirm JHEP 04 (2014) 110 and DOI; operator basis behind the di-Higgs
  effective couplings.
- `https://cp3.irmp.ucl.ac.be/projects/feynrules/wiki/HEFT_DH` — model scope, MadGraph version requirement
  (snippet: 3.0.1+), licence (adjacent alternative).
- `https://arxiv.org/abs/1509.04016` and `https://doi.org/10.1016/j.physletb.2016.11.039` — confirm authors, PLB
  764 (2017) 247, CC BY licence; extract the FCC-he di-Higgs set-up and the g_hhh precision quote with page.
- `https://events2.saip.org.za/event/2/contributions/653/` and
  `https://events2.saip.org.za/event/2/contributions/653/attachments/224/507/Di_Higgs_at_the_LHC%20(9).pdf` —
  presenter, date, slide text naming "effdihiggs-v2 UFO model" / "HELv2 effective Lagrangian", beam energies
  (500 GeV / 1 TeV μ on 7 TeV p), any cross sections, cut-flow and 95 % CL limits; compare slide-by-slide with the
  uploaded `SRC_WS_LEBOHO_KUMAR_DIHIGGS` to confirm or refute the inferred relation.
- `https://arxiv.org/abs/2510.18390` — authors, YITP-25-166, APS DOI 10.1103/prx6-wnwr, μTRISTAN beam
  assumptions, HNL sensitivity curves (comparison only).
- `https://arxiv.org/abs/2301.07117` — HNL mass range, μ⁺μ⁻ collider energies/luminosities, sensitivity
  (comparison only).
- `https://arxiv.org/abs/2306.17368` — JHEP 09 (2023) 131 DOI, same-sign VBS HNL set-up (comparison only).
- `https://arxiv.org/abs/2403.13021` — 2HDM-II+VLQ benchmark conventions, alignment-limit parameters, any UFO
  statement; note sibling ids 2401.16219, 2409.20104, 2211.07259 for a later pass.
