# LHμC-VirtualLab — Research roadmap (evidence-gathering tasks ranked by value of information)

**Document date:** 2026-10-28 · **Revised:** 2026-10-29 (status lines on R1–R10, new ranking §3a,
sequencing §4a; connector reachability §3b) · **Project phase:** Phase 0 (M1) · **Owner:** David Hausler.

**Purpose.** List the evidence that the platform still lacks, rank the tasks that would obtain it,
and name the next action type for each. Companion to `docs/roadmap.md` (milestones),
`docs/internet_research_protocol.md` §10 (fetch backlog by URL), `docs/limitations.md` (what is
unknown) and the per-family `research/_fragments/*_unresolved.md` files (per-source extraction
lists). Every item below is a *task to obtain evidence*; none of its expected content is a value.

**Boundary conditions on 2026-10-28.** arxiv.org, indico.cern.ch, cds.cern.ch, inspirehep.net,
pos.sissa.it, doi.org, journals, readthedocs and all CERN hosts are blocked; only PyPI, npm,
Launchpad, GitHub and raw.githubusercontent are reachable. Every non-uploaded source is therefore
`snippet_only`, `blocked` or `pending_fetch`; snippets may never back `reported_lhmuc` and are
capped at confidence `medium` (`CLAUDE.md` §1.5). The realistic routes to new evidence are
(a) the owner uploading documents, (b) direct author contact, (c) a network allow-list change
(`docs/internet_research_protocol.md` §8), (d) computation with tools that are installable here.
*[2026-10-29, owner decision: a route (e) is added, the owner-authorised alphaXiv connector. It can
deliver arXiv full texts as `fetched_text` (read in full, no page images, confidence ≤ `medium`;
`docs/internet_research_protocol.md` §5a). Route (c) is not pursued.]*

**Update 2026-10-29.** Route (a) delivered: the owner uploaded 29 documents (21 in the Phase-0
addendum, 4 + 1 + 3 in batches 7–9), all read in full and verified record by record. The network
policy is unchanged — the literature hosts were still blocked on 2026-10-29 — and the only other new
evidence is the public AloHEP repository on GitHub. Allowing **arxiv.org, cds.cern.ch,
indico.cern.ch, zenodo.org and doi.org** would let the lead fetch most of the remaining public items
of §3a; the White Paper, the μLHC AloHEP input decks and the `effdihiggs-v2` model need the authors.
*[2026-10-29: the five-host allow-list is not requested (owner decision). For arXiv-hosted items the
connector stands in for it (§3b); items that are not on arXiv still need the owner or the authors.]*

---

## 1. Ranking method

**VoI = expected reduction in decision uncertainty ÷ effort.** Both factors are the author's
qualitative judgement, not a measurement:

- *Decision uncertainty reduced* (U): which platform decisions or `unknown_roles` the evidence
  would settle, scored 3 (settles a baseline-level question for several milestones), 2 (settles a
  subsystem question), 1 (cross-check or context).
- *Effort* (E): 1 = hours once accessible (read one paper, run a script), 2 = days (several
  documents, installation, reproduction), 3 = weeks or dependent on third parties.
- *Accessibility today* (A): can it be done in the current environment? yes / upload needed /
  network or author needed. Accessibility does not change the VoI score but decides sequencing:
  a high-VoI item that needs the network becomes an *owner action* (upload or request).

Rank = U/E, ties broken by accessibility. Scores are in the table of §3; the detailed cards are in
§2.

---

## 2. Task cards

### R1 — Obtain the HELP4CERN White Paper and the Kraków workshop contributions
- **What.** The White Paper "High Energy, High Luminosity Lepton-Hadron Colliders at CERN"
  (cited as "in preparation" by arXiv:2610.35154 and, per `SRC_WS1681458_KHANPOUR_GAMMAGAMMA`
  p.4, the origin of the three benchmark working points 500 GeV/3.7 TeV/250 fb⁻¹,
  1 TeV/5.3 TeV/1000 fb⁻¹, 2 TeV/7.5 TeV/1000 fb⁻¹) and the Indico 1681458 contributions cited by
  the DIS2026 paper: Kilic (nozzle), Topp-Mugglestone (vFFA), Zimmermann (SPS/LHC modifications,
  incl. the 22×10¹¹ p/bunch assumption, ref. [24]), Yamazaki and Forthomme (detectors), Acosta
  (near-beam), Otani (pre-acceleration), Rogers and Zhang (source). Only the Dagli, Khanpour and
  Leboho/Kumar decks are in hand (`SRC_INDICO_1681458_OVERVIEW` is a snippet-level overview
  record).
- **Why.** These are the only PRIMARY_LHMUC sources that could fill the recurring `unknown_roles`
  (`l_star`, `crossing_angle`, `nozzle_opening_angle`, `main_ring_dipole_field`,
  `beta_x_star_muon`, `muon_norm_emittance`, `muon_bunch_length`, `wall_plug_power`) and could
  justify or refute the 22×10¹¹ proton bunch population and the "5 % of μTRISTAN" yield
  assumption. They decide whether M2 runs on LHμC or on μLHC-imported optics.
- **Scores.** U = 3, E = 3 (depends on authors/Indico), A = network or author needed.
- **Next action.** *Literature* (fetch/upload and page-level extraction) preceded by an *owner
  action*: request the slides from the authors or the workshop organisers; ask whether a White
  Paper draft can be shared under embargo. Record each as `uploaded` with hash on arrival.
- **Output.** New `parameters/**` records tagged `_WS…`, updated scenarios, closure of
  `missing_evidence.csv` rows; conflict records where the decks disagree with DIS2026.
- **Status 2026-10-29 — Kraków part largely done, White Paper still open.** Eleven decks were
  uploaded and read in full: Kilic, Topp-Mugglestone, Zimmermann, Forthomme, Yamazaki, Acosta,
  Rogers, Zhang, Nakazawa, the AGH high-energy-QCD deck and Schulte (`SRC_WS1681458_*`; 1443 records,
  563 of them `reported_lhmuc`). They give workshop-level options for `nozzle_opening_angle`, the
  nozzle length and tip, vFFA field options, a second LHμC beam set and source/front-end numbers,
  but **no** value for `l_star`, the crossing angle, `main_ring_dipole_field`, `beta_x_star_muon`,
  `muon_norm_emittance`, `muon_bunch_length` or `wall_plug_power`. Zimmermann answers the
  22×10¹¹ request with earlier fewer-bunch schemes and a scaling rule, not an LHμC proton bunch.
  Not uploaded: Otani, Kamioka, Piotrzkowski, Tentori, Sultansoy, Holzer. The White Paper is still
  "in preparation" and heads the 2026-10-29 ranking (§3a, W1).

### R2 — Fetch and read the μLHC erratum (PTEP 2026 033C04) and reconcile v1/v2/deck values
- **What.** The PTEP article page shows "Corrected and typeset 28 March 2026"; a ResearchGate
  listing "Erratum μLHC …" (May 2026) and the arXiv v2 (12 Jun 2026) change log exist as
  snippets; no erratum DOI was found (`research/_fragments/mulhc-mutristan_unresolved.md`). The
  uploaded v2 gives 8.8×10³³ / 7.2×10³³ cm⁻²s⁻¹; the Nucleus deck p.8 quotes the same post-erratum
  values.
- **Why.** The μLHC tables are the only beam-optics-level numbers the platform has; the P1 audit
  shows the published values equal naive × 0.63 (decay) with no visible hourglass factor
  (`docs/limitations.md` §5). The erratum text may state what was corrected and which terms
  AloHEP included, directly resolving the open audit item and fixing Benchmark 3.1's option set.
- **Scores.** U = 2, E = 1 (one short document), A = network needed (academic.oup.com, INSPIRE
  blocked) or upload.
- **Next action.** *Literature*; then *analytical* (re-run `lhmuc/analytical.py` checks with the
  erratum's stated option set).
- **Output.** `CONF_LUMI_MODEL_ASSUMPTIONS` conflict record updated; `SRC_ARXIV_2506_15445`
  promoted from snippet to fetched; parameter `notes` on `MACHINE_*_MULHC` luminosities.
- **Status 2026-10-29 — open, and now coupled with R9.** The erratum text is still not obtained
  (`ME_016`). The AloHEP method paper shows that the code simulates hourglass and pinch and applies
  the decay factor analytically, and the public v2.0 repository holds no μLHC deck (R9 status), so
  the erratum and the μLHC input decks together are the only route to the option set behind
  7.2×10³³ / 8.8×10³³. Merged into §3a W2.

### R3 — LHeC IR design papers: L*, Q1, separator, crossing angle
- **What.** LHeC CDR (arXiv:1206.2913, `SRC_ARXIV_1206_2913`), 2020 update (arXiv:2007.14491,
  `SRC_ARXIV_2007_14491`), ERL paper (arXiv:2206.07678, `SRC_ARXIV_2206_07678`), 2025 phase-one design (arXiv:2503.20475,
  `SRC_ARXIV_2503_20475`). Snippet-only leads, NOT verified: L* = 15 m, β* 10 → 7 cm, Q1A 252 T/m
  with 20 mm aperture, Q1B 164 T/m / 32 mm, separator 0.3 T × 9 m (2012), crossing angle 6 / 6.8 /
  7 mrad vs head-on 2025 phase-one (a four-way conflict to preserve).
- **Why.** LHμC reuses LHeC infrastructure (`SRC_ARXIV_2610_35154` §2 p.4, as summarised in
  `README.md` and `docs/scientific_scope.md` §1.4), and `IR_CROSSING_ANGLE_DIS2026` is the one
  `unknown` record. The
  LHeC IR is the natural `analogous`/`imported_related` basis for the LHμC IR until R1 delivers;
  it bounds L*, Q1 gradient/aperture and separation scheme for the M2 placeholder geometry and
  the M4 constraint set. A muon beam has no synchrotron-radiation constraint and a larger
  emittance, so applicability must be stated explicitly in each record.
- **Scores.** U = 2, E = 2 (four long documents, tables to locate), A = network needed or upload.
- **Next action.** *Literature* → *analytical* (aperture vs beam size at Q1 for the μLHC optics;
  dipole-field and separation estimate), then *expert review* of applicability to a μ⁺ beam.
- **Output.** `IR_*_LHEC` records (`imported_related`/`analogous`, applicability notes),
  `CONF_LHEC_CROSSING_ANGLE` conflict record, assumption records when adopted as M2 inputs.
- **Status 2026-10-29 — partially done.** The LHeC detector/ERL/IR paper André et al. 2022
  (`SRC_ARXIV_2201_02436`, batch 7) is read in full: L* = 15 m and β*_p = 10 cm (p.16), the QA1
  concept (p.15), head-on e–p collisions with the electrons steered by the detector dipole (p.10),
  the Fig. 19 separation scheme, a 3 T solenoid, and a Table 4 luminosity that cannot be reproduced
  from the paper (`docs/limitations.md` §5.1). No Q1 gradient is given. Still unread: the CDR
  (`SRC_ARXIV_1206_2913`), the 2020 update (`SRC_ARXIV_2007_14491`), the ERL paper
  (`SRC_ARXIV_2206_07678`) and André et al. 2025 (`SRC_ARXIV_2503_20475`) — §3a W5. *[2026-10-29: see §3b.]*

### R4 — IMCC MuCol Milestone Reports No. 5 and No. 7: nozzle geometry and beam-induced background
- **What.** `SRC_ARXIV_2411_02966` (Report No. 5, Preliminary Parameters) and
  `SRC_ARXIV_2510_27437` (Report No. 7, Consolidated Parameters), plus arXiv:2303.08533
  (`SRC_ARXIV_2303_08533`, "Towards a muon collider", MDI chapter). Snippet-only leads, NOT
  verified: INERMET180 + borated polyethylene, tip 6 cm from the IP, 10° outer inclination,
  L* = 6 m at 10 TeV; the three inner aperture angles (Report No. 5 Table 9.1) and total nozzle
  length were not in any snippet.
- **Why.** The only nozzle description read is μLHC §2.4 (6 m tungsten + borated polyethylene,
  19 % of the energy deposited). The IMCC geometry is the best-documented analogue for the M2
  nozzle placeholder (`DET_NOZZLE_*`), the M3 Geant4/BDSIM benchmark geometry and the detector
  acceptance; BIB rates per bunch crossing set the detector requirements. An asymmetric μ⁺p
  collision (one decaying beam, the proton side needs no nozzle) differs from μ⁺μ⁻, so these
  values are `analogous` at best.
- **Scores.** U = 2, E = 2, A = network needed or upload (Zenodo/arXiv blocked).
- **Next action.** *Literature* → *simulation* only if Geant4 becomes available (otherwise the
  item ends in an `analogous` parameterised geometry with an assumption record).
- **Output.** `DET_NOZZLE_*_IMCC` analogous records with page/table quotations; materials record
  for INERMET180 (density, composition) in `parameters/materials/`; assumption record for its use
  in LHμC.
- **Status 2026-10-29 — Report No. 7 done for MDI and acceleration; Report No. 5 open.** MR7
  (`SRC_ARXIV_2510_27437`) was uploaded: Table G.1 nozzle (595 cm base plane, 10° near the IP, tip
  6 cm), INERMET180 with a borated-polyethylene layer (material record `MAT_INERMET180_MR7`, Table
  G.2), L* = 6 m and the FLUKA BIB set-up (pp.65–66) are in `DET_NOZZLE_*_MR7`; MAIA and MUSIC were
  read as well. The MR7 reference tables for collider, proton driver, target, cooling, magnets, RF
  and power converters are still being verified and are not in `parameters/`. *[Update 2026-10-29: verified and
  committed; `docs/reports/M1_addendum_uploaded_documents.md` §A.8.]* Still unread:
  MuCol Report No. 5 (`SRC_ARXIV_2411_02966`), arXiv:2303.08533 and the IMCC BIB papers (§3a W10).
  The LHμC nozzle itself is now reported in workshop material (Kilic, Forthomme), so the IMCC values
  are comparators rather than the basis of a synthetic band. *[2026-10-29: see §3b.]*

### R5 — J-PARC ultra-slow muon source: ionisation efficiency and yield chain
- **What.** J-PARC USM / μTRISTAN source papers: `SRC_ARXIV_2201_06664` (μTRISTAN),
  `SRC_ARXIV_2605_25580` (hybrid target), `SRC_DOI_10_1103_PHYSREVLETT_74_4811` (laser resonant
  ionisation of thermal muonium), `SRC_JACOW_IPAC2018_FRXGBF1`, `SRC_ARXIV_2410_11367` (RF
  acceleration of μ⁺), the KEK/J-PARC talks listed in
  `research/_fragments/ultracold-source_sources.yaml`. Snippet-only leads, NOT verified: design
  rate ~10⁵ μ⁺/s, emittance < 1 π mm mrad, laser ionisation efficiency ~10⁻³ per surface muon.
- **Why.** DIS2026 Table 1 rests on "μ⁺ yields at a level of 5% of the ones in the μTRISTAN
  proposal, a 4 MW proton driver"; the μLHC paper's Fig. 1 chain (μTRISTAN numbers) is the only
  quantified source chain the platform has, and it is `imported_related`. The yield chain
  (surface μ⁺ → muonium → ionised μ⁺ → accelerated μ⁺ with 82 % / 67 % booster survival) decides
  whether N_μ = 0.07×10¹¹ per bunch at 12.5 Hz × 80 bunches is reachable, i.e. whether the
  luminosity claim is credible at all. This is the central feasibility question of
  `docs/scientific_scope.md` §2.
- **Scores.** U = 3, E = 2, A = network needed or upload (arxiv.org, kek.jp blocked).
- **Next action.** *Literature* → *analytical* (yield-chain multiplication with ranges in
  `physics/` at M2; comparison with the 5 % statement) → *expert review* (the extrapolation from
  measured J-PARC rates to a 4 MW driver is the step most likely to be contested).
- **Output.** `SOURCE_*_JPARC` analogous records; `SOURCE_YIELD_CHAIN_*` analytical estimates
  with derivation strings; assumption record for the 5 %-of-μTRISTAN scaling.
- **Status 2026-10-29 — literature largely done; the decisive number does not exist yet.** Read in
  full: μTRISTAN (`SRC_ARXIV_2201_06664`), the J-PARC g-2/EDM design (`SRC_ARXIV_1901_03047`), the
  2024 measured chain (`SRC_ARXIV_2410_11367`), Bakule 2013 (`SRC_ARXIV_1306_3810`), Beare 2020
  (`SRC_ARXIV_2006_01947`), the hybrid target (`SRC_ARXIV_2605_25580`) and the Zhang, Rogers and
  Nakazawa decks. Outcome: the measured 2.1×10⁻⁸ μ⁺ per surface muon at 100 keV lies ≈ 1.2×10⁵ below
  the g-2 design target and ≈ 2.5×10⁶ below the μTRISTAN post-stopping budget; the 73 % ionisation
  efficiency is a calculation; the 0.52 formation fraction is a 2013 MuSR measurement that a 2020
  measurement on other samples does not reproduce (`docs/limitations.md` §10.3–§10.4). Still missing:
  Beer et al. 2014 (`SRC_ARXIV_1407_8248`), the Zhang muonium papers, Kamioka's slides (§3a W3, W8),
  and a measured 122 + 355 nm ionisation efficiency, which no literature fetch can supply. *[Verifier
  note 2026-10-29: Beer et al. 2014 and Zhang et al. 2021 (JPS Conf. Proc. 33) arrived in batch 10,
  commit `ad5ac43`, without parameter records yet; see the note under §3a.]*

### R6 — Topp-Mugglestone vFFA thesis and vFFA lattice papers
- **What.** `SRC_URL_ORA_OXFORD_TOPP_MUGGLESTONE_THESIS` (blocked), `SRC_JACOW_IPAC2021_THPAB124`
  (Machida, Lagrange, Topp-Mugglestone; blocked), `SRC_INDICO_DESY_45968_185344` (IMCC meeting
  poster), `SRC_ARXIV_2011_10783`; licence, DOI and field/energy numbers unconfirmed
  (`research/_fragments/vffa-acceleration_unresolved.md`).
- **Why.** The LHμC booster combines LHeC-type ERL passes with vFFAG beamlines
  (`SRC_ARXIV_2610_35154` §2 p.4, quoted in `docs/scientific_scope.md` §1.4); the DIS2026 paper
  gives only the ≈9 km booster circumference and no vFFA lattice, and the P1
  survival model (81.6 % / 67.4 %, reproducing μLHC's 82 % / 67 % for 16 / 50 turns) needs the
  turn count and ramp. vFFA field range, orbit excursion and acceptance set the booster's
  G0/G1 footprint and the muon-survival budget in M2.
- **Scores.** U = 2, E = 2 (thesis-length), A = network needed or upload.
- **Next action.** *Literature* → *analytical* (turns × circumference vs lifetime 20.8 ms at
  1 TeV, γ = 9464) → later *simulation* (cpymad/xsuite toy vFFA cell, M2–M3).
- **Output.** `ACCEL_VFFA_*` analogous records; scenario role `booster_turns` filled or declared
  synthetic with a range.
- **Status 2026-10-29 — partially done.** The Kraków deck "vFFA and LHμC"
  (`SRC_WS1681458_TOPPMUGGLESTONE_VFFA`) and the MuCol M17 report (`SRC_DOI_10_5281_ZENODO_15054073`)
  are read in full: requirement 70 → 500 GeV with order-10 turns, preliminary 8 / 10 / < 9 T options
  (records `ACC_*_WS2026_TOPPMUGGLESTONE`), and the analytic stage-1 / stage-4 IMCC designs with their
  closed-orbit arithmetic pinned in `tests/scientific/test_mucol_m17_vffa.py`. No LHμC booster lattice
  exists in either document. Still unread: the thesis (`SRC_URL_ORA_OXFORD_TOPP_MUGGLESTONE_THESIS`),
  the acc-models-mc optics notebooks (CERN GitLab; `ACC_VFFA_OPTICS_NOTEBOOK_LOCATION_MUCOLM17`) and
  the IPAC'21 paper — §3a W7. *[2026-10-29: see §3b.]*

### R7 — HL-LHC TDR proton tables (and LHC Design Report)
- **What.** `SRC_URL_CERN_2020_010_HLLHC_TDR` (CERN-2020-010, Appendix A / Chapter 2 tables),
  HL-LHC TDR V0.1 (2017), LHC Design Report Vol. 1 (CERN-2004-003-V-1); per
  `research/_fragments/lhc-hl-lhc-protons_unresolved.md`. Snippet-only leads, NOT verified:
  2.2×10¹¹ p/bunch, ε_n 2.5 μm, 2760 / 2744 / 2748 / 2604 / 2808 bunches by document and
  version — a conflict to preserve, not average.
- **Why.** Proton-side values are currently `imported_related` *as quoted by the μLHC paper*
  (2.2×10¹¹, 7 TeV, β* 7 cm, ε_n 2 μm, 2760 bunches, 11245 Hz, 26.7 km). The TDR turns them into
  read values and documents the 2 μm vs 2.5 μm emittance difference (μLHC's 2 μm is a μp design
  choice, not an HL-LHC fact). Needed before any luminosity result is called P2.
- **Scores.** U = 1 (cross-check; the uploads already fix the values the proponents use), E = 1,
  A = network needed (e-publishing.cern.ch blocked) or upload.
- **Next action.** *Literature*.
- **Output.** `PROTON_*_HLLHC_TDR` records; `CONF_HLLHC_PROTON_BUNCH_COUNT` and emittance conflict
  records; applicability notes on the μLHC proton records.
- **Status 2026-10-29 — open, value raised.** The TDR is still unread (`ME_044`). Zimmermann's deck
  restates LHC Project Report 627 Table 1 and CERN-2005-006 Table 3 (records `PROTON_LHC_PR627_*`,
  scenarios `LHC-PR627-*`), but the originals are unread; together with the rule σδσz ≈ 2 n_b,0 σδ,0
  σz,0 they are the only route to a sourced proton bunch length for high-population bunches, the
  missing input of the hourglass question. Upgraded to U = 2 in §3a W6.

### R8 — The two theory papers and UFO availability
- **What.** arXiv:2610.28252 ("Probing a heavy neutral lepton in a radiative neutrino model at a
  muon collider": 3 TeV μ⁺μ⁻, 1 ab⁻¹) and arXiv:2610.17801 (one-loop A → ZZγ in 2HDM+VLQ,
  BR 10⁻⁵–10⁻⁴); both `UNVERIFIED`, snippet-level only. UFO status: no public model for the
  radiative HNL model (HeavyN lacks the scalar sector), no combined 2HDM+VLQ UFO (separate
  2HDM_NLO, Pseudoscalar_2HDMI and VLQ_UFO exist as leads), `effdihiggs-v2` (HELv2) not public
  (`research/_fragments/theory-benchmarks_unresolved.md`).
- **Why.** Benchmarks A and B of M3 cannot even be *defined* (masses, mixings, 2HDM type, VLQ
  representations) without the papers; neither is a μ⁺p study, so the recast would start from
  their μ⁺μ⁻ or decay-width results. The di-Higgs reproduction (benchmark C) is blocked by the
  UFO. The value is high for M3 but zero for the machine-feasibility question; hence U = 2.
- **Scores.** U = 2, E = 2 (two papers + model hunting/building), A = network or author needed.
- **Next action.** *Literature* (abstract pages first to lift from `UNVERIFIED`; full text) →
  *owner action* (ask Kumar et al. for `effdihiggs-v2` terms) → *simulation* (M3).
- **Output.** `theory/benchmarks/*/proposal.yaml` with `review_state` advanced from `extracted`;
  UFO inspection records per `docs/security_policy.md` §3.
- **Status 2026-10-29 — unchanged.** Both papers are still `blocked` and the UFO is still private
  (`ME_049`–`ME_051`). Cheung & Wang 2021 (`SRC_ARXIV_2101_10476`) is now read, but it is a μ⁻p
  comparator, not one of these benchmarks. §3a W4. *[2026-10-29: see §3b.]*

### R9 — AloHEP source code: reproduce 7.2×10³³ and 8.8×10³³
- **What.** `SRC_URL_GITHUB_YEFETU_ALOHEP` (repository page fetched; README read; no licence,
  tag or release; "save" accelerator JSON files not yet inspected), `SRC_JACOW_IPAC2021_WEPAB278`
  (blocked), alohep.hepforge.org (not fetched).
- **Why.** The only computation-based route to the μLHC and Nucleus-deck luminosities available
  *today*: the repository is reachable. Reading its luminosity formula (decay average, hourglass,
  crossing angle, beam-beam, "matched" beam sizes) would resolve the open audit item in
  `docs/limitations.md` §5 (reported/naive = 0.63 with H ≈ 0.53 unexplained; σ_x = 3.6 μm,
  σ_y = 1.7 μm from Table 1 optics vs 4.3 μm "matched") and fix Benchmark 3.1's option set.
  Lower U than R2 only because the code may not match the version used for the paper.
- **Scores.** U = 2, E = 1 (code reading; running it is optional), A = **yes, now** (GitHub
  reachable) — subject to `docs/security_policy.md` §3–§5 (inspect before running; `-I`; own
  directory; no execution from the clone directory).
- **Next action.** *Analytical* (read the formulas, re-derive by hand in `lhmuc/analytical.py`
  tests) → *simulation* (run AloHEP in a container on the μLHC Table 1–3 inputs and record the
  option set) → *expert review* if the hourglass treatment remains unclear.
- **Output.** Software-inventory entry (licence unknown → ask authors before any
  redistribution), `CONF_LUMI_MODEL_ASSUMPTIONS` resolution or sharpened statement, Benchmark 3.1
  pre-registration.
- **Status 2026-10-29 — done as far as reading allows; blocked on the input decks.** The method
  paper (`SRC_ARXIV_2610_09839`, batch 7) is read in full and summarised in
  `docs/tools/alohep_method_dagli2026.md`; the repository it names, github.com/tobbetuyef/AloHEP tag
  v2.0, is MIT-licensed (`SRC_URL_GITHUB_TOBBETUYEF_ALOHEP`) and was cloned read-only into an
  isolated folder, its decks read as text, nothing built or run. Findings: hourglass and pinch are
  simulated, the decay factor is applied analytically, L_nom underestimates unequal beams, and the
  repository has **no μLHC or LHμC deck** (`ME_043`). Building and running the code is an M2 task
  under `docs/security_policy.md` (pinned commit, isolated build). The relation to the earlier
  github.com/yefetu/ALOHEP copy is unresolved. Next step folded into §3a W2.

### R10 — Accelerator digital-twin and differentiable-tracking literature
- **What.** Cheetah (`SRC_URL_PYPI_CHEETAH_ACCELERATOR`, `SRC_ARXIV_2401_05815`; PyPI 0.8,
  licence GPLv3 per README badge, licence file not read), Xsuite (`SRC_URL_PYPI_XTRACK`,
  `SRC_ARXIV_2310_00317`), Bmad/pytao (`SRC_URL_GITHUB_BMAD_ECOSYSTEM`, `SRC_URL_PYPI_PYTAO`),
  cpymad/MAD-X, and the published accelerator digital-twin / surrogate-model literature (not yet
  surveyed; no source records exist for it in the fragments).
- **Why.** Decides the M2–M4 tool stack (optics code, surrogate for optimisation, GPL
  implications for the Apache-2.0 code base) and how the "digital twin" claim will eventually be
  earned rather than asserted. It does not reduce any LHμC physics uncertainty, hence U = 1.
- **Scores.** U = 1, E = 2, A = partly yes (PyPI/GitHub pages and licence files reachable;
  arXiv papers blocked).
- **Next action.** *Literature* (licence files from GitHub now; papers when reachable) →
  *simulation* (toy 3 km ring, Benchmark 3.2, in M2) → decision record in
  `docs/architecture.md` §12 and `docs/software_inventory.md`.
- **Output.** Software inventory entries with licences; tool-adoption decision; pinned versions
  in `uv.lock`.
- **Status 2026-10-29 — partially done.** The AI4MuC workshop report (`SRC_ARXIV_2610_14303`) is
  read in full; its "Verifiable AI workflows" principles (§11, pp.12–13) are adopted as process rules
  in `docs/architecture.md` §15, and its software section (p.11) names the MuonColliderSoft stack
  (Key4hep, EDM4hep, ACTS, Spack, CVMFS) now listed in `docs/software_inventory.md` §15. The
  differentiable-tracking and surrogate literature is still not surveyed. *[2026-10-29: see §3b.]*

---

## 3. Ranking table

| Rank | Task | U | E | VoI = U/E | Accessible now? | Action type | Milestone unblocked |
|---|---|---|---|---|---|---|---|
| 1 | R9 AloHEP source: reproduce 7.2e33 / 8.8e33 | 2 | 1 | 2.0 | **yes** (GitHub) | analytical → simulation | M2 Benchmark 3.1 |
| 2 | R2 μLHC erratum | 2 | 1 | 2.0 | no (upload/network) | literature → analytical | M2 Benchmark 3.1 |
| 3 | R5 J-PARC USM efficiency and yield chain | 3 | 2 | 1.5 | no (upload/network) | literature → analytical → expert review | M2 (feasibility question) |
| 4 | R1 White Paper + Kraków contributions | 3 | 3 | 1.0 | no (authors/Indico) | owner request → literature | M2, M3, M4 (LHμC-specific IR, nozzle, acceleration) |
| 5 | R3 LHeC IR papers | 2 | 2 | 1.0 | no (upload/network) | literature → analytical → expert review | M2 geometry, M4 constraints |
| 6 | R4 IMCC MuCol Reports 5 and 7 | 2 | 2 | 1.0 | no (upload/network) | literature → (simulation if Geant4) | M2 nozzle placeholder, M3 Benchmark 3.3 |
| 7 | R6 vFFA thesis and papers | 2 | 2 | 1.0 | no (upload/network) | literature → analytical | M2 booster model |
| 8 | R8 Theory papers and UFOs | 2 | 2 | 1.0 | no (authors/network) | literature → owner request → simulation | M3 benchmarks A–C |
| 9 | R7 HL-LHC TDR proton tables | 1 | 1 | 1.0 | no (upload/network) | literature | M2 P2 label on luminosity |
| 10 | R10 Digital-twin / differentiable-tracking literature | 1 | 2 | 0.5 | partly | literature → simulation | M2–M4 tool stack |

Reading of the table: R1 has the largest payoff but the lowest controllability; R9 is the only
item executable without any change to network policy and is therefore the **next action for the
platform itself**; R2 and R5 are the **next upload requests to the owner**. Ties at VoI = 1.0 are
ordered by how many milestones they unblock, then by how LHμC-specific the evidence is.
*[Superseded 2026-10-29 by §3a: R9 is done as far as reading allows, R5 and the Kraków part of R1
were delivered by uploads.]*

---

## 3a. Value-of-information ranking, revision of 2026-10-29

After the uploads, the remaining evidence gaps are ranked below. The order was set by the lead on
2026-10-29: LHμC-specific evidence that blocks the M2 baseline first, then direct inputs of the
open luminosity and source questions, then comparators. The U and E scores of §1 are given for
information; VoI = U/E. "Hosts" names what would have to be reachable for the lead to fetch a public
item; "authors" means no fetch can supply it.

| Rank | Item | Missing-evidence row | U | E | VoI | Public? / hosts | Action type | Unblocks |
|---|---|---|---|---|---|---|---|---|
| W1 | **HELP4CERN White Paper** "High Energy, High Luminosity Lepton-Hadron Colliders at CERN" — the only expected source of an official LHμC baseline (IR, optics, nozzle, booster, source rate) | `ME_001` | 3 | 3 | 1.0 | not public — authors / owner | owner request → literature | M2 baseline, M3, M4 |
| W2 | **μLHC PTEP 2026 erratum text with the AloHEP input decks and option set** used for 7.2×10³³ / 8.8×10³³ (hourglass, pinch, decay form, matched beams) | `ME_016`, `ME_043` | 3 | 1 | 3.0 | erratum via doi.org, then the journal host academic.oup.com (not in the five-host list); decks from the authors (the public v2.0 repository has none) | literature + owner request → simulation (M2 Benchmark 3.1) | `CONF_LUMI_MODEL_ASSUMPTIONS`, Benchmark 3.1 |
| W3 | **Remaining Kraków slides**: Otani (pre-acceleration of ultra-slow muons), Kamioka (cited by Zhang p.20 for the latest ionisation-efficiency studies), Piotrzkowski (luminosity measurement; FCC-μe), Tentori (Higgs couplings), Sultansoy (title not known here; an earlier CERN talk on e/μ-LHC proposals is `SRC_INDICO_1600007_6742086`) | `ME_008`, `ME_011`, `ME_012`, `ME_013` | 2 | 1 | 2.0 | indico.cern.ch (event 1681458) if attached publicly, else owner | literature | M2 source and front end, M3 luminosity measurement and Higgs |
| W4 | **Theory papers** arXiv:2610.28252 (`SRC_ARXIV_2610_28252`) and arXiv:2610.17801 (`SRC_ARXIV_2610_17801`) **and the `effdihiggs-v2` UFO** | `ME_049`–`ME_051` | 2 | 2 | 1.0 | papers via arxiv.org; UFO from the authors | literature → owner request → simulation | M3 benchmarks A–C |
| W5 | **LHeC 2020 update** (`SRC_ARXIV_2007_14491`) **and André et al. 2025** (`SRC_ARXIV_2503_20475`) — IR, crossing scheme, phase-one head-on design, proton parameters behind the LHeC luminosity | `ME_046` | 2 | 2 | 1.0 | arxiv.org | literature → analytical | M2 IR comparators; the LHeC Table 4 band |
| W6 | **HL-LHC TDR** (`SRC_URL_CERN_2020_010_HLLHC_TDR`) **and LHC Project Report 627 / CERN-2005-006** (known only as restated by Zimmermann) — proton bunch population, emittance, bunch length of high-intensity bunches | `ME_044` | 2 | 1 | 2.0 | cds.cern.ch, doi.org | literature → analytical | proton bunch length (hourglass), `CONF_PROTON_BUNCH_POPULATION_AND_NUMBER` |
| W7 | **Topp-Mugglestone thesis** (`SRC_URL_ORA_OXFORD_TOPP_MUGGLESTONE_THESIS`) **and the vFFA optics notebooks** (acc-models-mc, `ACC_VFFA_OPTICS_NOTEBOOK_LOCATION_MUCOLM17`) | `ME_027` | 2 | 2 | 1.0 | ora.ox.ac.uk and gitlab.cern.ch — **not** in the five-host list | literature → simulation (toy vFFA cell) | M2 booster placeholder, Benchmark 3.2 |
| W8 | **Beer et al. 2014** (`SRC_ARXIV_1407_8248`, the laser-ablation emission enhancement) **and the Zhang muonium papers** (e.g. Zhang et al. 2022, cited by Sakaki et al. 2026) | `ME_031` | 2 | 1 | 2.0 | arxiv.org, doi.org | literature | source-chain factors (`CONF_MUONIUM_FORMATION_FRACTION`) |
| W9 | **Kaya et al., EPL 138 (2022) 24002** (`SRC_ARXIV_1905_05564`) — HL-LHC / HE-LHC μp luminosity considerations of the AloHEP group | — | 1 | 1 | 1.0 | arxiv.org, doi.org | literature | luminosity-model lineage |
| W10 | **IMCC beam-induced-background papers**: Collamati et al. (`SRC_ARXIV_2105_09116`), Calzolari et al. PoS ICHEP2024 (`SRC_URL_POS_ICHEP2024_819`), MuCol Report No. 5 (`SRC_ARXIV_2411_02966`) | `ME_026`, `ME_048` | 2 | 2 | 1.0 | arxiv.org; the PoS paper via doi.org, then pos.sissa.it (not in the five-host list) | literature → (simulation if FLUKA/Geant4) | M3 background analogue for μ⁺p |

*[Verifier note 2026-10-29: after this ranking was written, commit `ad5ac43` (batch 10) uploaded and
registered Beer et al. 2014 (`SRC_ARXIV_1407_8248`) and Zhang et al. 2021, JPS Conf. Proc. 33, 011125
(`SRC_DOI_10_7566_JPSCP_33_011125`) of W8 and Kaya et al., EPL 138 (2022) 24002 (`SRC_ARXIV_1905_05564`,
W9), together with Shirotori et al. 2026 (`SRC_ARXIV_2608_25374`). They are read and their arithmetic is
pinned in `tests/scientific/test_batch10_documents.py`, but no parameter records exist yet; W8 still
lacks Zhang et al. 2022 (NIM A 1042, 167443).]* *[Update 2026-10-29: the three papers of W8/W9 are now
extracted and adversarially verified (Kaya 148 records checked, Beer 78, Zhang 105; notes `verify_G15_KAYA2022.md`,
`verify_G16_BEER2014.md`, `verify_G17_ZHANG2021.md`); Shirotori et al. 2026 stays context-only. W8 still lacks
Zhang et al. 2022 and the primary publication of the T = 322 K / D = 870 cm² s^-1 diffusion fit.]*

Internal items that need no network and are not ranked here: verification of the MuCol MR7
reference tables (done 2026-10-29, report §A.8); the owner's line-by-line
review of the headline tables (`RISK_028_HUMAN_REVIEW_PENDING`); building and running AloHEP v2.0 in an
isolated container for the decks it does contain, as the first step of Benchmark 3.1.

**What the five hosts would unlock.** With arxiv.org, cds.cern.ch, indico.cern.ch, zenodo.org and
doi.org allowed, the lead could fetch W3 (if the slides are attached publicly), the papers of W4,
W5, W6, W8, W9 and the arXiv papers of W10, and the Zenodo records of the MuCol reports (licence of
M17, Report No. 5). The PTEP erratum (W2) and the PoS paper (W10) additionally need their publishers'
hosts (academic.oup.com, pos.sissa.it), which doi.org only redirects to. The White Paper (W1),
the μLHC AloHEP input decks (W2), the `effdihiggs-v2` model (W4) and the thesis and notebooks
(W7, on ora.ox.ac.uk and gitlab.cern.ch) would still need the owner or the authors.
*[2026-10-29: not requested (owner decision); see §3b.]*

---

## 3b. Reachability through the alphaXiv connector (2026-10-29)

*[2026-10-29, owner decision:]* the owner-authorised alphaXiv connector can deliver arXiv full texts,
which are registered as `access: fetched_text` (read in full, no PDF and no page images, confidence
≤ `medium`; `docs/internet_research_protocol.md` §5a). The table states only what the connector could
reach for each item of §3a; it records no reading. Each "yes", "partial" or "possible" is a candidate
to be confirmed by search.

| Rank | Missing-evidence rows | Connector | What it could deliver |
|---|---|---|---|
| W1 | `ME_001` | no | The White Paper is not public. A connector search can only confirm that it has not appeared on arXiv (a negative search-log row); `ME_001` stays with the owner and the authors. |
| W2 | `ME_016`, `ME_043` (related: `ME_066`, `ME_054`) | partial, to be confirmed by search | Only a version of arXiv:2506.15445 later than the uploaded v2, if one exists: read as `fetched_text` under its own id `SRC_ARXIV_2506_15445_V<n>` and compared with v2, with a `CONF_` record for any difference. It may narrow `ME_016`, and `ME_054` only if the delivered text states licence or version; the uploaded v2 reading is not replaced. No for the erratum (journal host) and the AloHEP decks (authors): `ME_043` and `ME_066` are unchanged. |
| W3 | `ME_008`, `ME_011`, `ME_012`, `ME_013` (related: `ME_014`, `ME_068`, `ME_069`) | no for the slides; possible for the cited texts, to be confirmed by search | The slides are on Indico, so Otani (`ME_008`) and Kamioka (`ME_069`) stay with the owner and the authors. Possible only if posted on arXiv: the texts the DIS2026 paper cites as "in preparation" or "in These Proceedings" (Piotrzkowski `ME_011`, `ME_013`; Tentori `ME_012`; Kotko and Khanpour `ME_014`, `ME_068`). Written by the proponents, they would be `PRIMARY_LHMUC` candidates and could back `reported_lhmuc` at ≤ `medium`. `SRC_URL_APS_PRAB_29_093201_NAKAZAWA` (an `ME_008` candidate) only if an arXiv version exists. |
| W4 | `ME_049`, `ME_050`, `ME_051` | yes for the papers, to be confirmed by search; no for the UFO | arXiv:2610.28252 and arXiv:2610.17801 as `fetched_text`: identity and category from the delivered front matter (the step that lifts `UNVERIFIED`) and the definitions of benchmarks A and B; the proposals would then carry `access: fetched_text`, `review_state: extracted`, P0. Further arXiv candidates named in `ME_049`/`ME_050`: `SRC_ARXIV_2609_08808`, `SRC_ARXIV_2301_07117`, `SRC_ARXIV_2510_18390`, `SRC_ARXIV_2403_13021`. No for `effdihiggs-v2` (`ME_051`) and the UFO halves of `ME_049`/`ME_050`: the FeynRules hosts are blocked, and GitHub-hosted models are reached by git, not through the connector. |
| W5 | `ME_046` (related: `ME_064`; comparators for `ME_018`, `ME_019`, `ME_020`) | yes, to be confirmed by search | arXiv:2007.14491 and arXiv:2503.20475, plus the other `ME_046` candidates arXiv:1206.2913 (CDR) and arXiv:2206.07678 (ERL). They could narrow `ME_046`, `ME_064` (the proton inputs behind the LHeC Table 4) and the Q1, crossing-angle and separator comparators of `ME_018`–`ME_020`, as `imported_related`/`analogous` at ≤ `medium`. |
| W6 | `ME_044` | no | The HL-LHC TDR, LHC Project Report 627 and CERN-2005-006 are on CDS / e-publishing. At most comparators from arXiv compilations (`SRC_ARXIV_2206_00037`, an `ME_044` candidate; Bordry et al. arXiv:1810.13022, see W9), which never substitute for the TDR; `ME_044` stays open. |
| W7 | `ME_027` (related: `ME_067`) | no | Neither the thesis (ORA) nor the acc-models-mc notebooks (gitlab.cern.ch), so `ME_067` stays open. Side literature only: `SRC_ARXIV_2011_10783` (vFFA optics design, an `ME_027` candidate) could narrow `ME_027` as `analogous`; IPAC'21 THPAB124 (`SRC_JACOW_IPAC2021_THPAB124`) only if an arXiv version exists. |
| W8 | `ME_031` | possible, to be confirmed by search | Only if arXiv versions exist of Zhang et al. 2022 (NIM A 1042, 167443), the candidate source of the T = 322 K / D = 870 cm² s^-1 diffusion fit, or of another publication of that fit; never assumed. They could narrow `ME_031` and `CONF_MUONIUM_FORMATION_FRACTION`. |
| W9 | — (candidates: `ME_042`, `ME_037`, or a new row) | residuals yes, to be confirmed by search | Kaya et al. was uploaded and read in batch 10; its tabulated inputs come from two unread arXiv papers: Delahaye et al. arXiv:1901.06150 (Table 3; the MAP average-luminosity definition, needed for the one- versus two-beam decay correction, `research/unresolved_searches.md`, batch 10) and Bordry et al. arXiv:1810.13022 (Tables 1–2). Neither has a source id yet (new `SRC_ARXIV_1901_06150`, `SRC_ARXIV_1810_13022`). |
| W10 | `ME_026`, `ME_048` | yes for the arXiv papers, to be confirmed by search; no for PoS | arXiv:2105.09116 (Collamati et al.) and arXiv:2411.02966 (MuCol Report No. 5), plus the `ME_048` candidates arXiv:2303.08533 and arXiv:2407.12450 (IMCC Interim Report). They could narrow `ME_026` and `ME_048` as `analogous`. No for `SRC_URL_POS_ICHEP2024_819` and `SRC_URL_POS_ICHEP2022_063` unless arXiv versions exist. |

Outside W1–W10, also candidates to be confirmed by search: the `ME_015` precursor arXiv:1509.04016
(`SRC_ARXIV_1509_04016`); the seven software papers listed under the `software-tools` family of
`research/unresolved_searches.md`; the R10 literature once surveyed; Bowring et al. 2020 (PRAB 23
072001, `ME_059`) and Zhu et al. PRAB 28 (2025) 041003 only if arXiv versions exist.

---

## 4. Sequencing proposal

*[Superseded 2026-10-29 by §4a; the list below is kept as written on 2026-10-28. Item 1: R9 is done
as far as reading allows, on the repository named in the AloHEP paper (github.com/tobbetuyef/AloHEP,
tag v2.0), not on `yefetu/ALOHEP`; R10's licence-file fetch is still open
(`docs/software_inventory.md` §12, e.g. the Cheetah LICENSE file). Item 2: the uploads delivered
μTRISTAN (`SRC_ARXIV_2201_06664`), the J-PARC source-chain measurements and MuCol Report No. 7
(`SRC_ARXIV_2510_27437`); the erratum, both LHeC IR papers, MuCol Report No. 5 and the HL-LHC TDR
are still missing (§3a W2, W5, W10, W6). Item 3: 14 Kraków decks arrived; the remaining slides, the
White Paper and the `effdihiggs-v2` terms are still open (§3a W3, W1, W4).]*

1. **Now (no network change needed).** R9: clone `yefetu/ALOHEP` into its own empty directory,
   inspect per the security policy, read the luminosity routine, write the formula into the P1
   test file as a *hypothesis* and compare with the 0.63 / 0.53 audit numbers. R10 (partial):
   fetch licence files for Cheetah, Xsuite, cpymad, pyg4ometry, cadquery from GitHub.
2. **Owner uploads (highest VoI per upload).** R2 (erratum + PTEP article page), R5 (μTRISTAN
   arXiv:2201.06664 and the J-PARC USM rate/efficiency papers), R3 (arXiv:2007.14491 and
   arXiv:2503.20475), R4 (MuCol Reports No. 5 and No. 7), R7 (HL-LHC TDR 2020 Appendix A).
3. **Owner requests to authors.** R1 (Kraków slides; White Paper status), R8 (`effdihiggs-v2`
   terms; the two theory papers if arXiv remains blocked).
4. **When the allow-list of `docs/internet_research_protocol.md` §8 is granted.** Run the fetch
   backlog of §10 there and of every `research/_fragments/*_unresolved.md` in the order above;
   promote sources from `snippet_only` to `fetched`, record SHA-256 and licence, and re-run the
   four unexecuted `lhc-hl-lhc-protons` queries.

Each completed task closes with: source record promoted, archived-metadata JSON written,
parameter records added or corrected with verbatim quotations, conflicts recorded,
`missing_evidence.csv` rows closed or re-pointed, and a line in the milestone report.

### 4a. Sequencing, revision of 2026-10-29

1. **Owner requests now (no network change):** W1 (White Paper status, embargoed draft if possible)
   and W2 (the μLHC AloHEP input decks and option set; the erratum text) to the HELP4CERN and AloHEP
   authors; W4's `effdihiggs-v2` terms; the Kraków slides of W3 if they are not on Indico.
2. **Network allow-list:** arxiv.org, cds.cern.ch, indico.cern.ch, zenodo.org, doi.org; then fetch
   W3–W6 and W8–W10 in the order of §3a and run the fetch backlog of
   `research/unresolved_searches.md`. *[2026-10-29: not pursued (owner decision); for arXiv items the
   connector route 2a replaces it.]*
   - **2a. Connector route** *(2026-10-29, owner decision; the alphaXiv connector is loaded in the lead session
     of that date)*: once the Step-0 gates G1–G7 of `docs/internet_research_protocol.md` §5a have passed, the
     lead search-confirms each "yes", "partial" or "possible" item of §3b in the rank order of §3a (W2 version
     check, W3 texts in preparation, W4, W5, W8, W9 residuals, W10), reads it with `get_paper_content`,
     registers it as `fetched_text`, extracts, has it verified against the saved delivered text and folds it in.
     *[2026-10-29, Step 0 run: G4 and G7 could not be run as written, so the route is stopped until the owner decides
     on the substitute evidence (`research/_fragments/alphaxiv_calibration_2026-10-29.md`).]*
3. **Platform, no network:** finish the registry stage and the MR7 reference-table verification (both done on
   2026-10-29);
   prepare Benchmark 3.1 as a pre-registered test that runs AloHEP v2.0 (pinned commit, isolated
   build) on reconstructed μLHC decks for every option set, with the proton bunch length taken from
   `PROTON_BUNCH_LENGTH_RMS_SYN` and the one-beam decay average applied outside the code if the
   code's form is the two-beam one (`docs/tools/alohep_method_dagli2026.md` §8).

---

## 5. What this roadmap does not claim

- No value named in §2 ("~10⁵ μ⁺/s", "L* = 15 m", "INERMET180", "2760 bunches" …) is a parameter
  of the platform; they are *leads* that identify what to look for and are explicitly marked as
  snippet-only and unverified.
- The VoI scores are judgements made on 2026-10-28 by the documentation author to order work;
  they are not measurements and should be revised when the owner's priorities or the network
  policy change.
- Obtaining the evidence does not by itself make the LHμC feasible or infeasible; it makes the
  question *evaluable* (`CLAUDE.md` §1.1, §1.10).
- *[2026-10-29:]* Values from `fetched_text` sources (§3b) are read in full but not checked against page
  images; they stay at confidence ≤ `medium` and their records say so (`docs/internet_research_protocol.md` §5a).

## 6. Change log

| Date | Change |
|---|---|
| 2026-10-28 | First version: ten tasks, scoring method, ranking table, sequencing. |
| 2026-10-29 | Status lines on R1–R10 after the uploads of the Phase-0 addendum and batches 7–9; new ranking W1–W10 (§3a) headed by the White Paper and the μLHC erratum with the AloHEP input decks; host list for the allow-list request; sequencing §4a. The 2026-10-28 table of §3 and the list of §4 are kept as the record of the first ranking, each with a dated superseded note; the hosts needed beyond the five (academic.oup.com, pos.sissa.it, ora.ox.ac.uk, gitlab.cern.ch) are named in §3a. |
| 2026-10-29 | Connector addendum (owner decision; `docs/internet_research_protocol.md` §5a): new §3b, the reachability of W1–W10 through the alphaXiv connector, each item to be confirmed by search (reachability only, no reading recorded); route (e) in the boundary conditions; the five-host allow-list not requested (§4a item 2) and the connector route as item 2a; dated notes in the header, the update paragraph, R3, R4, R6, R8, R10, §3a, §5 and §7. |

## 7. Sources cited

Uploaded (read in full): `SRC_ARXIV_2610_35154` (arXiv:2610.35154v1), `SRC_ARXIV_2506_15445`
(arXiv:2506.15445v2), `SRC_WS1681458_DAGLI_NUCLEUS`, `SRC_WS1681458_KHANPOUR_GAMMAGAMMA`,
`SRC_WS_LEBOHO_KUMAR_DIHIGGS`.

Snippet-level or blocked leads (source ids as registered in `research/_fragments/*_sources.yaml`;
not read): `SRC_INDICO_1681458_OVERVIEW`, `SRC_ARXIV_2506_15445`,
`SRC_ARXIV_1206_2913`, `SRC_ARXIV_2007_14491`, `SRC_ARXIV_2206_07678`, `SRC_ARXIV_2503_20475`, `SRC_ARXIV_2411_02966`,
`SRC_ARXIV_2510_27437`, `SRC_ARXIV_2303_08533`, `SRC_ARXIV_2201_06664`, `SRC_ARXIV_2605_25580`,
`SRC_DOI_10_1103_PHYSREVLETT_74_4811`, `SRC_JACOW_IPAC2018_FRXGBF1`, `SRC_ARXIV_2410_11367`,
`SRC_URL_ORA_OXFORD_TOPP_MUGGLESTONE_THESIS`, `SRC_JACOW_IPAC2021_THPAB124`,
`SRC_INDICO_DESY_45968_185344`, `SRC_ARXIV_2011_10783`, `SRC_URL_CERN_2020_010_HLLHC_TDR`,
`SRC_ARXIV_2610_28252`, `SRC_ARXIV_2610_17801`, `SRC_URL_GITHUB_YEFETU_ALOHEP`,
`SRC_JACOW_IPAC2021_WEPAB278`, `SRC_URL_PYPI_CHEETAH_ACCELERATOR`, `SRC_ARXIV_2401_05815`,
`SRC_URL_PYPI_XTRACK`, `SRC_ARXIV_2310_00317`, `SRC_URL_GITHUB_BMAD_ECOSYSTEM`,
`SRC_URL_PYPI_PYTAO`.

Added 2026-10-29 — uploaded and read in full: the Kraków decks `SRC_WS1681458_FORTHOMME_DETECTOR`,
`_TOPPMUGGLESTONE_VFFA`, `_ZIMMERMANN_SPS_LHC`, `_ROGERS_HYBRID_SOURCE`, `_ZHANG_MUONIUM`,
`_KILIC_NOZZLE`, `_YAMAZAKI_TEV_MUON`, `_ACOSTA_NEAR_BEAM`, `_NAKAZAWA_LOW_VELOCITY`, `_HEQCD_SMALLX`,
`_SCHULTE_IMCC`; `SRC_ARXIV_2201_06664`, `SRC_ARXIV_2203_06258`, `SRC_ARXIV_2510_27437`,
`SRC_ARXIV_2502_00181`, `SRC_ARXIV_2601_13189`, `SRC_ARXIV_2006_01947`, `SRC_ARXIV_2410_11367`,
`SRC_ARXIV_2607_16904`, `SRC_ARXIV_2609_37117`, `SRC_ARXIV_2610_14303`, `SRC_ARXIV_2201_02436`,
`SRC_ARXIV_1901_03047`, `SRC_ARXIV_2605_25580`, `SRC_ARXIV_2610_09839`, `SRC_DOI_10_5281_ZENODO_15054073`,
`SRC_ARXIV_1306_3810`, `SRC_ARXIV_2101_10476`, `SRC_IMCC2026_GIOVE_RF_SYSTEM`; fetched:
`SRC_URL_GITHUB_TOBBETUYEF_ALOHEP`. Named in §3a and not read: `SRC_ARXIV_2007_14491`,
`SRC_ARXIV_2503_20475`, `SRC_URL_CERN_2020_010_HLLHC_TDR`, `SRC_URL_ORA_OXFORD_TOPP_MUGGLESTONE_THESIS`,
`SRC_ARXIV_1407_8248`, `SRC_ARXIV_1905_05564`, `SRC_ARXIV_2105_09116`, `SRC_URL_POS_ICHEP2024_819`,
`SRC_ARXIV_2411_02966`, `SRC_INDICO_1600007_6742086`, `SRC_ARXIV_2610_28252`, `SRC_ARXIV_2610_17801`.
*[Verifier note 2026-10-29: `SRC_ARXIV_1407_8248` and `SRC_ARXIV_1905_05564` were uploaded and read in
batch 10 (commit `ad5ac43`) after this list was written; no parameter record cites them yet.]*
*[2026-10-29: sources read through the alphaXiv connector (`access: fetched_text`) will be listed here separately,
with their version and "not checked against page images".]*
