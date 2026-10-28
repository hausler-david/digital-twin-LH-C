# LHμC-VirtualLab — Research roadmap (evidence-gathering tasks ranked by value of information)

**Document date:** 2026-10-28 · **Project phase:** Phase 0 (M1) · **Owner:** David Hausler.

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

---

## 4. Sequencing proposal

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

## 6. Change log

| Date | Change |
|---|---|
| 2026-10-28 | First version: ten tasks, scoring method, ranking table, sequencing. |

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
