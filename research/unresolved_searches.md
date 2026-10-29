# Unresolved searches — LHμC-VirtualLab

**Document date:** 2026-10-28, updated 2026-10-29 (new section "Resolved or narrowed by uploads (2026-10-28/29)")
· **Status:** living register (CLAUDE.md §4: "record what remains unresolved in
`research/unresolved_searches.md`") · **Built from:** the nine reconnaissance-family fragments
`research/_fragments/*_unresolved.md` (concatenated, headings demoted one level, bullet blocks that repeat an
earlier family verbatim replaced by a pointer; see the de-duplication note at the end).

Nothing in this file is a parameter record. Every value mentioned in the family sections below was seen in a
search-engine snippet or in a page that could not be fetched; such evidence may not back a `reported_lhmuc`
status and is capped at confidence `medium` (CLAUDE.md §1.5, `research/source_quality_policy.md` §4). The section
"Resolved or narrowed by uploads" instead quotes documents that were uploaded and read in full, and names the
parameter record that carries the provenance of each value. Competing values that were found are registered in
`research/source_conflicts.yaml`; this file lists what could *not* be determined and what must be fetched once the
network allows it.
*[2026-10-29: when the first document is read in full through the owner-authorised alphaXiv connector
(`access: fetched_text`, not checked against page images), a section "Resolved or narrowed by connector text" is
added. It quotes those documents and names the record ids that carry each value, as the uploads section does.]*

## Network access blocked on 2026-10-28

On the document date the session's outbound network allowed only PyPI (`pypi.org`), npm
(`registry.npmjs.org`), Launchpad (`launchpad.net`), GitHub (`github.com`, `raw.githubusercontent.com`) and the
search tool's own snippets. Every other host named by a reconnaissance family was refused (`getaddrinfo
ENOTFOUND` / "not resolvable in this session" / network policy) or was never fetched. The hosts below must be
allowed before any `blocked` or `snippet_only` source can be read in full, quoted verbatim and archived with a
SHA-256; grouped by what they hold.

**Primary LHμC and HELP4CERN material (highest priority):**
`arxiv.org` (and `export.arxiv.org`, `ar5iv.labs.arxiv.org`), `indico.cern.ch` (Kraków workshop event 1681458
timetable and contribution PDFs; ICHEP 2026 event 1522800; Accelerator Design Meeting event 1664360; Sultansoy
talk event 1600007), `help4cern.web.cern.ch`, `indico.fis.agh.edu.pl` (AGH seminar event 462),
`events2.saip.org.za` (SAIP 2026 di-Higgs slides), `pos.sissa.it` (PoS DIS2026 proceedings when published).

**μLHC / μTRISTAN / erratum:** `academic.oup.com` (PTEP 2026 033C04 and its correction), `inspirehep.net`,
`researchgate.net` / `www.researchgate.net`, `avesis.uludag.edu.tr`, `alohep.hepforge.org`, `yef.etu.edu.tr`.

**LHC / HL-LHC / LHeC design documents:** `e-publishing.cern.ch` (HL-LHC TDR 2020, LHC Design Report),
`accelconf.web.cern.ch`, `jacow.org`, `proceedings.jacow.org`, `refs.jacow.org`,
`indico.jacow.org`, `iopscience.iop.org`, `epjc.epj.org`, `jinst.sissa.it`, `pdg.lbl.gov`,
`lhc-machine-outreach.web.cern.ch`, `lhc-closer.es`, `atrium.in2p3.fr`, `hal.archives-ouvertes.fr`,
`infoscience.epfl.ch`, `doi.org` and the journal hosts behind it (`journals.aps.org`, `link.aps.org`,
`link.springer.com`).

**Ultra-cold muon source and J-PARC:** `www.kek.jp`, `www2.kek.jp`, `conference-indico.kek.jp`,
`epaper.kek.jp`, `www.pasj.jp`, `www.s.u-tokyo.ac.jp`, `indico.jlab.org`, `indico.ihep.ac.cn`.

**vFFA / FFA acceleration:** `ora.ox.ac.uk` (Topp-Mugglestone thesis), `zgoubi.sourceforge.io`,
`indico.desy.de`, `indico.stfc.ac.uk`, `indico.bnl.gov`, `indico.fnal.gov`, `www.osti.gov`.

**Muon-collider MDI analogues:** `zenodo.org`, `par.nsf.gov`, `strathprints.strath.ac.uk`.

**Theory benchmarks and models:** `cp3.irmp.ucl.ac.be`, `feynrules.irmp.ucl.ac.be`, `www.alphaxiv.org`,
`api.semanticscholar.org`, `hepdata.net`.

**Software documentation and licences:** `geant4.org`, `root.cern`, `fluka.cern`, `fluka.org`,
`fluka-forum.web.cern.ch`, `www.pp.rhul.ac.uk` (BDSIM), `docs.desy.de`, `g4beamline.muonsinc.com`,
`*.hepforge.org` (Herwig, SARAH, LHAPDF, AloHEP), `dev.opencascade.org`, `pythia.org`, `anaconda.org`.

**Named in the session's network policy but not in any fragment:** `cds.cern.ch` and the `readthedocs.io`
documentation hosts were listed as blocked in the session instructions; no reconnaissance family attempted
them, so they appear here only so the allow-list request is complete.

Status per source is kept in `research/source_registry.yaml` (`access: blocked | snippet_only | pending_fetch`);
the per-family "Fetch backlog" sections below say what to extract from each page once it is reachable.

*[2026-10-29: the probe was repeated (arxiv.org, export.arxiv.org, doi.org, cds.cern.ch, indico.cern.ch, zenodo.org,
inspirehep.net, api.semanticscholar.org and api.crossref.org refused). The owner kept the allow-list unchanged and
authorised instead the alphaXiv connector, which runs outside the container, for arXiv preprints: a paper read in full
through it gets `access: fetched_text` (`docs/internet_research_protocol.md` §5a, §7). It is the only exception:
`www.alphaxiv.org` above is not a WebFetch route, and documents that are not on arXiv still need an upload.]*

---

## Resolved or narrowed by uploads (2026-10-28/29)

**Added:** 2026-10-29 · **Scope:** the documents uploaded by the project owner after the reconnaissance of
2026-10-28 (Phase-0 addendum and batches 7, 8 and 9). Each was read in full, archived with SHA-256
(`research/archived_metadata/<source_id>.json`) and extracted into parameter records that independent verifiers
checked against the page images (`research/_fragments/verify_G*.md`). The network policy has not changed: on
2026-10-29 the literature hosts listed above are still blocked, so every item below was closed or narrowed by an
upload, not by a fetch.

How to read this section: each entry names the backlog item(s) of the family sections further down that the upload
resolves or narrows, what it settled (with the record ids that carry the provenance) and what remains open. The
family sections are kept unchanged as the record of what was searched on 2026-10-28; where an entry here says
*resolved*, it supersedes the corresponding bullet below, and *narrowed* means the bullet stays open with the
residual stated here. Competing values found in the uploads are recorded in `research/source_conflicts.yaml`
(nine new conflict records on 2026-10-29: `CONF_NOZZLE_OPENING_ANGLE`, `CONF_MUONIUM_FORMATION_FRACTION`,
`CONF_LASER_IONISATION_EFFICIENCY`, `CONF_SOURCE_CONCEPT`, `CONF_IR_LSTAR`, `CONF_DETECTOR_SOLENOID_FIELD`,
`CONF_VFFA_PEAK_FIELD`, `CONF_TEV_MUON_RESOLUTION`, `CONF_FRONT_END_SPACE_CHARGE`; nine earlier records extended).

### Kraków workshop decks (Indico 1681458, 24–26 Sept 2026; Phase-0 addendum)

- **Forthomme, "LHeC/LHμC main detector"** (`SRC_WS1681458_FORTHOMME_DETECTOR`; `ME_003`). *Resolves* the
  `lhmuc-primary` item "Kraków workshop contributions" for this talk (cited by arXiv:2610.35154). Settled: a second
  LHμC beam set, "Peak luminosity of 10^34 cm^-2s^-1 for 40 bunches of 10^10 µ⁺ in main ring", "Assuming 300 ns
  bunch spacing", σx,y ≈ 4.3 µm with β* = 7 cm (`MACHINE_PEAK_LUMINOSITY_WS2026_FORTHOMME`,
  `MACHINE_MU_BUNCHES_WS2026_FORTHOMME`, `IR_SIGMA_XY_IP_WS2026_FORTHOMME`; `CONF_PEAK_LUMINOSITY`,
  `CONF_MUON_BUNCHES_PER_TRAIN`, `CONF_IP_BEAM_SIZE`); the nozzle half-angle 40 (100) mrad (`CONF_NOZZLE_OPENING_ANGLE`);
  L* 15 m vs 23 m (`CONF_IR_LSTAR`); Bz = 3.8 T in the LHeC Delphes card (`CONF_DETECTOR_SOLENOID_FIELD`).
  *Still open:* "peak" is undefined; the proton bunch population is not stated (≈ 7.0e11 implied only under H = 1,
  `PROTON_BUNCH_POPULATION_IMPLIED_WS2026_FORTHOMME`); the circumference behind 40 × 300 ns = 12 µs; which machine the
  23 m layout belongs to. The Natal 2026 / ICHEP speaker-attribution item is not touched by this deck.
- **Kilic, "Nozzle design studies for mu+p collider detector"** (`SRC_WS1681458_KILIC_NOZZLE`; `ME_002`; ref. [27]
  of arXiv:2610.35154). *Resolves* the `muon-collider-mdi` items "No LHμC-specific MDI statement (mu+p, asymmetric,
  single muon beam) was found" and "Applicability of the 10 degree nozzle acceptance to LHμC must be checked".
  Settled: a single-sided tungsten nozzle with borated-polyethylene cladding on the incoming-muon side, half-angle
  40 (100) mrad (60 and 80 mrad also studied), 487.8 cm + 100 cm long (587.8 cm), tip 6 cm from the IP
  (`DET_NOZZLE_*_WS2026_KILIC`; `CONF_NOZZLE_OPENING_ANGLE`). *Still open:* the choice between the options; a μ+p
  beam-induced-background simulation (`ME_026`); the Phase-0 band of `DET_NOZZLE_OPENING_ANGLE_SYN` written on
  2026-10-28 (5–20°) excluded the 40 mrad = 2.29° option (supersession under CLAUDE.md §4 is recorded in
  `parameters/assumptions/`, not here).
- **Topp-Mugglestone, "vFFA and LHμC"** (`SRC_WS1681458_TOPPMUGGLESTONE_VFFA`; `ME_004`; ref. [22] of
  arXiv:2610.35154). *Resolves* the `vffa-acceleration` item "Relevance to LHμC is indirect ... the Kraków workshop
  Topp-Mugglestone contribution was not found"; *narrows* "No vFFA muon ring energy range, circumference, RF
  frequency, number of turns, or power-efficiency figure was found". Settled: the LHμC booster stage "70 GeV to 500 GeV
  (to 1 TeV?)" in a single arc pair with order-10 turns; preliminary field options ~8 T (index 60 /m, excursion
  ~3 cm), ~10 T (~44 /m), relaxed < 9 T (< 30 /m, < 7 cm) (`ACC_VFFA_*_WS2026_TOPPMUGGLESTONE`,
  `ACC_BOOSTER_*_WS2026_TOPPMUGGLESTONE`; `CONF_VFFA_PEAK_FIELD`, `CONF_BOOSTER_DESIGN`). *Still open:* an analytic study
  "in untested region of parameter space"; the integrated full-ring simulation is still to be done (deck p.46); no
  LHμC booster lattice (`ME_027`); the Topp-Mugglestone thesis (ora.ox.ac.uk) is still unread.
- **Zimmermann, "Potential possibilities of modifying SPS/LHC"** (`SRC_WS1681458_ZIMMERMANN_SPS_LHC`; `ME_005`; ref.
  [24] of arXiv:2610.35154). *Resolves* the `lhc-hl-lhc-protons` items "The Zimmermann ... talk/note was not found" and
  "Ref. [24] of arXiv:2610.35154 must be resolved". Settled: the deck answers the LHμC request for "a much lower
  number of bunches in the LHC (say, 1% of the today's one)" with older schemes for fewer, more intense bunches
  (Damerau–Garoby long flat bunches, the LHC Project Report 627 super-bunch, QCD Explorer) and the rule "Higher
  intensity is accompanied by longer bunches and/or larger energy spread – Roughly speaking σδ σz ≈ 2 n_b,0 σδ,0 σz,0"
  (`PROTON_*_WS2026_ZIMMERMANN`; `CONF_PROTON_BUNCH_POPULATION_AND_NUMBER`, `CONF_LUMI_MODEL_ASSUMPTIONS`). *Still
  open:* no LHμC proton population, bunch number or bunch length is given; the 200 MHz / 8b4e / 50 ns linkage of the
  `lhc-hl-lhc-protons` bullet is not addressed in the records extracted from the deck (there, 200 MHz appears only as
  the SPS RF at ejection in the Damerau–Garoby scheme); the restated papers themselves were not read.
- **Acosta, "Near-Beam Muon Detectors"** (`SRC_WS1681458_ACOSTA_NEAR_BEAM`; `ME_006`) and **Yamazaki, "Challenges of
  TeV-muon Detectors"** (`SRC_WS1681458_YAMAZAKI_TEV_MUON`; `ME_007`). *Resolve* the `lhmuc-primary` item for these
  two contributions. Settled: TeV-muon momentum resolution "~6% @ 1 TeV" (Geant4) and "~5% @ 1 TeV, ~25% at 5 TeV"
  (idealised) for a far-forward toroidal spectrometer, and "6-7 %" at 1 TeV for the main-detector muon system
  (`CONF_TEV_MUON_RESOLUTION`); Acosta also restates the IMCC nozzle ("6m long tungsten nozzles (~2.4 < |η| < 7)").
  *Still open:* no full simulation of an LHμC muon system; the multiple-scattering impact of the nozzle on the
  downstream muon measurement (`DET_NOZZLE_MS_IMPACT_STATEMENT_WS2026_ACOSTA`) is not quantified for μ+p.
- **Rogers, "Hybrid Source of Ultra Cold Muons"** (`SRC_WS1681458_ROGERS_HYBRID_SOURCE`; `ME_009`; ref. [19] of
  arXiv:2610.35154). *Resolves* the `lhmuc-primary` item for this contribution. Settled: the hybrid IMCC-front-end
  chain (capture, rectilinear A-stage cooling, deceleration, low-energy cooling), "Estimate 0.04 μ+ per 5 GeV proton
  on target to end of A-stage", "Target ~ 50 % efficiency for deceleration" (`SOURCE_HYBRID_*_WS2026_ROGERS`;
  `CONF_SOURCE_CONCEPT`). *Still open:* the deceleration is "Not designed" and the low-energy cooling efficiency is
  unknown (`SOURCE_HYBRID_LOW_ENERGY_COOLING_EFFICIENCY_WS2026_ROGERS` = null); RF breakdown in solenoids (see Giove 2026
  below).
- **Zhang, "Muonium diffusion modeling and multi-layer target design for muon laser ionisation cooling"**
  (`SRC_WS1681458_ZHANG_MUONIUM`; `ME_010`). *Narrows* the `ultracold-source` item "Rate chain (per-stage efficiencies)
  is incomplete": the H-line chain table (p.10) and the μTRISTAN budget 0.52 × 0.6 × 0.6 × 0.73 = 0.137 after stopping
  (p.20; `SOURCE_MUTRISTAN_POST_STOPPING_BUDGET_WS2026_ZHANG`) are now quoted, and the μTRISTAN source numbers ("We
  thank Cedric Zhang to provide us with those numbers") are traced to them; Zhang flags the 0.73 ionisation
  efficiency as "pending updates", and his own g-2 target column implies 0.114 (`CONF_LASER_IONISATION_EFFICIENCY`).
  *Still open:* Kamioka's workshop slides (cited on p.20) are not uploaded; the unattributed "~1e-3 / surface μ" slide
  of the `ultracold-source` family remains unattributed (the nearest uploaded figures are 2.5e-3 per surface muon in
  Abe 2019 and 2.6e-3 in Zhang's g-2 target column).
- **Nakazawa, "Acceleration in the Low-velocity Region"** (`SRC_WS1681458_NAKAZAWA_LOW_VELOCITY`). *Narrows* the
  `ultracold-source` item "IH-DTL output energy varies across sources": "IN/OUT energy 0.34 MeV > 4.26 MeV" is now read
  on p.5, and `CONF_JPARC_IHDTL_ENERGY` is resolved as two design versions (4.5 MeV in Abe 2019). New: the first
  quantitative space-charge statement for LHμC bunch charges, 1e10 μ+ in ~2 ns ≈ 0.75 A at the RFQ entrance, "220
  larger perveance(K) scale than the original 30-mA H⁻ RFQ" (`SOURCE_RFQ_PERVEANCE_RATIO_WS2026_NAKAZAWA`;
  `CONF_FRONT_END_SPACE_CHARGE`). *Still open:* the 4.3 MeV value has no source; PRAB 29, 093201 itself is unread; no
  high-charge front-end design exists (`ME_033`).
- **Schulte, "Muon Collider (IMCC overview)"** (`SRC_WS1681458_SCHULTE_IMCC`) and the AGH **"High energy QCD at LHμC"**
  deck (`SRC_WS1681458_HEQCD_SMALLX`): context for the IMCC programme and the LHμC small-x physics case; they close the
  "speaker list only" part of the `lhmuc-primary` item for these talks and raise no conflict.
- *Not uploaded:* Otani (pre-acceleration, `ME_008`), Piotrzkowski (luminosity measurement, `ME_011`), Tentori
  (`ME_012`) and Holzer (IR design, named in several conflict records). The Kumar, Khanpour and Dağlı decks were
  already uploaded in Phase 0. The timetable, registration-date and proceedings items of `lhmuc-primary` stay open.

### Related machines, reference designs and tools

- **μTRISTAN, arXiv:2201.06664v2** (`SRC_ARXIV_2201_06664`, PTEP 2022 053B02; addendum; `ME_047`). *Resolves* the
  `mulhc-mutristan` item "μTRISTAN Table 1 per-bunch values were quoted from a secondary reproduction
  (arXiv:2403.17034)" and its fetch-backlog entry. Settled in the original: 1.4e10 μ+ per bunch at the IP (2.3 nC),
  β* = 30 mm / 7 mm, σ = 3.6 / 1.7 µm, normalised emittance 4 mm mrad, 7.2 nC ultra-cold μ+ per bunch, booster of 16
  turns in about 700 µs with 3 km linacs and R = 1 km arcs at 3 T, "about a half of the muons decays", a 14 %
  ultra-cold-muon production efficiency with numbers from C. Zhang (`*_MUTRISTAN2022`; `CONF_BOOSTER_DESIGN`,
  `CONF_FRONT_END_SPACE_CHARGE`, `CONF_MUONIUM_FORMATION_FRACTION`, `CONF_LASER_IONISATION_EFFICIENCY`). *Still open:*
  the booster injection energy is not stated (`ACC_BOOSTER_INJECTION_ENERGY_MUTRISTAN2022` = null); the PTEP DOI and
  licence.
- **MuIC, arXiv:2203.06258v3** (`SRC_ARXIV_2203_06258`; addendum). *Resolves* the `lhmuc-primary` item "Name collision
  'LHmuC'" from the full text: one 1.5 TeV beam of a 3 TeV IMCC μ+μ− collider on 7 TeV LHC protons, √s = 6.5 TeV,
  2.8e33 cm^-2 s^-1, 237 fb^-1 per 10 years (`MACHINE_*_LHMUC_MUIC2022`; `RISK_022_LHMUC_NAME_COLLISION`); and the
  `mulhc-mutristan` / `lhmuc-primary` fetch-backlog entries for 2203.06258: parameter tables, "the hour-glass factor,
  H_hg, is assumed to be unity", luminosity with max(σ_μ, σ_p) (`CONF_LUMI_MODEL_ASSUMPTIONS`, `CONF_PEAK_LUMINOSITY`,
  `CONF_MUON_BUNCH_POPULATION`, `CONF_IP_BEAM_SIZE`). *Still open:* the journal reference JINST 18 (2023) P09025 is
  still snippet-level (Forthomme cites it for "δE/E ~ 10%"); the Wei Li Snowmass slides are unread.
- **Cheung & Wang 2021, arXiv:2101.10476v2** (`SRC_ARXIV_2101_10476`, PRD 103, 116009; batch 9). *Resolves* the
  `mulhc-mutristan` fetch-backlog entry (beam combinations and luminosities) and `lhc-hl-lhc-protons` backlog item 30.
  Settled: μp-1 = 7 TeV p × 1 TeV μ− (√s = 5.3 TeV), an assumed 1e33 cm^-2 s^-1 → 0.1 ab^-1, WW-fusion Higgs 0.978 pb,
  Δg_hbb/g_hbb = 0.69 % (`*_CHEUNG2021`; `tests/scientific/test_batch9_documents.py`). *Still open:* μ−p only — LHμC
  collides μ+, which changes the charged-current rates, so the cross sections are screening comparators only
  (`CONF_PEAK_LUMINOSITY` keeps the assumed 1e33 as a comparator); the branching ratios and the LHeC Delphes card
  version are not printed; the journal version was not seen.
- **LHeC detector paper, André et al. 2022, arXiv:2201.02436v1** (`SRC_ARXIV_2201_02436`, EPJC 82, 40; batch 7).
  *Resolves, for this paper,* the `lhec-erl` item "No full text of any LHeC document was read" and its fetch-backlog
  entry for 2201.02436. Settled: L* = 15 m (p.16), β*_p = 10 cm (p.16; the Fig. 19 header gives β*_p = 10.0 cm and
  β*_e = 10.9 cm per beam, not per plane), head-on e–p collisions with the electrons steered by the detector dipole
  and a vertical crossing angle only for the non-colliding proton beam (pp.10, 16; `CONF_LHEC_CROSSING_ANGLE`), a 3 T
  solenoid reduced from 3.5 T (`CONF_DETECTOR_SOLENOID_FIELD`), ERL Tables 2–3 (499 pC, 24.95 ns, 20 mA; arc energies
  and synchrotron radiation), luminosity 8.2e33 cm^-2 s^-1 (Table 4). *Still open:* Table 4 is not reproducible from
  the paper, which lists no proton bunch population or emittance (≈ 0.80 × 8.2e33 with HL-LHC protons;
  `CONF_LUMI_MODEL_ASSUMPTIONS`); the "LHeC-at-HL-LHC proton beam parameter table" item, the LHeC CDR and 2020 update
  (`ME_046`) and the 2025 phase-one paper (arXiv:2503.20475) remain unread; the CC BY 4.0 licence of the journal
  version is still snippet-level.
- **AloHEP method — Dağlı & Karaca 2026, arXiv:2610.09839v1** (`SRC_ARXIV_2610_09839`; batch 7) **and the repository
  it names, github.com/tobbetuyef/AloHEP tag v2.0** (`SRC_URL_GITHUB_TOBBETUYEF_ALOHEP`, MIT, cloned and read as text on
  2026-10-28, nothing built or run). *Narrows* the `mulhc-mutristan` item "AloHEP GitHub repo (yefetu/ALOHEP): no
  license, version tag or release found" and the `SRC_JACOW_IPAC2021_WEPAB278` fetch entry (luminosity formula,
  hourglass handling). Settled: hourglass and beam–beam pinch are simulated with macroparticles and verified to ~1 %;
  "The decay factor is applied analytically" (functional form not written); the internal L_nom uses the equal-beam
  max(σ) approximation, which "underestimates the geometric luminosity when the beams differ"; a "Matched Beams"
  helper exists (`MACHINE_ALOHEP_*_DAGLI2026`; `docs/tools/alohep_method_dagli2026.md`; `CONF_LUMI_MODEL_ASSUMPTIONS`,
  `CONF_IP_BEAM_SIZE`). *Still open:* **the μLHC input decks are still missing** — the public v2.0 repository holds no
  μLHC or LHμC deck, so the PTEP 2026 values 7.2e33 / 8.8e33 cannot be reproduced (`ME_043`); whether the decay factor
  is a one- or two-beam average for μp (the 0.254 μ+μ− benchmark is two-beam; μp needs the one-beam 0.632,
  `tests/scientific/test_batch7_documents.py::test_decay_averaging_differs_between_mumu_and_mup`); the relation between
  tobbetuyef/AloHEP and yefetu/ALOHEP; the IPAC'21 paper itself.
- **vFFA design note — MuCol Milestone Report 17, "Tentative design of the FFA"** (M. Topp-Mugglestone, 27 Mar 2025,
  `SRC_DOI_10_5281_ZENODO_15054073`; batch 8). *Resolves* the `vffa-acceleration` item "No source found giving a vFFA
  muon ring's explicit energy range in GeV/TeV"; *narrows* "Topp-Mugglestone thesis: ... any field/energy numbers for
  the muon-collider vFFA stage not confirmed" and the "no energy range, circumference ..." item. Settled: stage 1
  0.06 → 0.3 TeV, 5990 m, 6.93 T on orbit (the F-magnet field) and 12.52 T in the good-field region; stage 4 1.5 → 5 TeV,
  35000 m, 13.59 T on orbit (the reverse-bend D-magnet field) and 29.04 T good-field; design limit 8.3 T (LHC dipole),
  which stage 4 exceeds (`*_MUCOLM17`; `tests/scientific/test_mucol_m17_vffa.py`; `CONF_VFFA_PEAK_FIELD`). *Still
  open:* analytic lattices only (no tracking, non-linear or longitudinal study); the printed eq. (2.7) appears to
  contain a typographical error (`test_printed_eq27_inconsistent_with_closed_orbit_geometry`); the thesis, the
  acc-models-mc notebooks (CERN GitLab) and the Zenodo licence; the LHμC 70 → 500 GeV booster is in neither M17 nor MR7.
- **MuCol Milestone Report 7, arXiv:2510.27437v1** (`SRC_ARXIV_2510_27437`; addendum, MDI and acceleration sections).
  *Resolves* the `muon-collider-mdi` item "Exact 10 TeV nozzle inner aperture angles ... and total nozzle length were not
  present in any snippet" and the nozzle part of its fetch entry: Table G.1 outer surface (z, r) = (6, 1), (100, 17.57),
  (595, 55) cm, "the inclination amounts to 10 degrees" near the IP, tip 6 cm, L* = 6 m (`DET_NOZZLE_*_MR7`,
  `IR_LSTAR_MR7`; `tests/scientific/test_workshop_decks.py::test_imcc_nozzle_outer_surface_angles_mr7_table_g1`); Table
  F.5 restates the M17 vFFA rings. *Resolved 2026-10-29:* the MR7 reference tables for collider, proton driver, target,
  cooling, magnets, RF and power converters were verified and committed (`docs/reports/M1_addendum_uploaded_documents.md`
  §A.8). *Still open:* the licence is not printed.
- **MAIA, arXiv:2502.00181v2** (`SRC_ARXIV_2502_00181`) and **MUSIC, arXiv:2601.13189v1** (`SRC_ARXIV_2601_13189`;
  addendum). *Resolve* the `muon-collider-mdi` author-list and fetch entries: MAIA (C. Bell et al.) has a 5 T solenoid
  "in contrast to the 3.57 T solenoid of the 3 TeV detector design", the nozzle edge at |η| = 2.44 ≈ 10° and L* = 6 m;
  MUSIC (P. Andreetto et al.) has 5 T chosen "to minimize the effects of the incoherent e+ e− pair production"
  (`CONF_DETECTOR_SOLENOID_FIELD`, `CONF_NOZZLE_OPENING_ANGLE`, `CONF_IR_LSTAR`). *Still open:* journal status; the related
  arXiv:2511.23273.
- **Dudko, arXiv:2607.16904v2** (`SRC_ARXIV_2607_16904`; addendum; SECONDARY_SOURCE). *Resolves* the
  `vffa-acceleration` fetch entry for its authorship, date and scope (L. V. Dudko, SINP MSU; Natural Science Review,
  JINR; CC BY-NC 4.0). Used for the turns-per-lifetime formula n ≃ γ cτ_μ/C with cτ_μ = 659 m — 2079 turns at 1 TeV in
  a 3 km ring (`PHYS_MUON_TURNS_PER_LIFETIME_FORMULA_DUDKO2026`;
  `tests/scientific/test_workshop_decks.py::test_turns_per_lifetime_dudko_formula`).

### Ultra-cold μ+ source chain

- **Origin of the 0.52 — Bakule et al. 2013, arXiv:1306.3810v1** (`SRC_ARXIV_1306_3810`, PTEP 2013 103C01; batch 9).
  *Resolves* the question where the muonium formation fraction 0.52 of the J-PARC/μTRISTAN budgets comes from: a
  MuSR measurement, "the fraction of muonium formed in the three aerogel samples was 0.52 ± 0.01" (p.3;
  `SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAKULE2013`). It is cited directly by Beare et al. 2020 (ref. [14]) and
  Aritome et al. 2024 (ref. [21]); for Abe 2019, the Zhang deck ("from TRIUMF measurement") and μTRISTAN (numbers from
  C. Zhang) the attribution is inferred, not cited; Sakaki et al. 2026 cite Zhang et al. 2022 [15]. Also settled: on
  flat (non-ablated) aerogel the vacuum yield of 4.8e-3 per incident muon at 23 MeV/c scales to 9.6e-4 for the J-PARC
  beam (eq. (1); `SOURCE_MU_VACUUM_YIELD_JPARC_SCALED_BAKULE2013`;
  `tests/scientific/test_batch9_documents.py::test_bakule2013_vacuum_yield_scaling_to_jparc_beam`); laser ablation later
  raised the emission by about an order of magnitude (Abe 2019 p.8; Beare 2020: 5–28 ‰ ablated vs < 5 ‰ flat).
  *Still open:* which three of the four samples and which MuSR facility; Beare et al. 2020 measured 0.655 ± 0.018 on
  different samples, 6.6 σ apart — kept as two measurements (`CONF_MUONIUM_FORMATION_FRACTION`); Zhang et al. 2022 is
  not uploaded; Beer et al. 2014 (arXiv:1407.8248, the "0.01 Mu per incident muon" projection) is still unread.
  *[Verifier note 2026-10-29: after this entry was written, commit `ad5ac43` (batch 10) uploaded and registered Beer et
  al. 2014 (`SRC_ARXIV_1407_8248`; it gives no muonium formation fraction) and Zhang et al. 2021, JPS Conf. Proc. 33,
  011125 (`SRC_DOI_10_7566_JPSCP_33_011125`, which cites Beer et al. 2014 for the 52 % although the value is Bakule 2013
  p.3); neither has parameter records yet. Zhang et al. 2022 (NIM A 1042, 167443; Sakaki ref. [15]) is still not
  uploaded.]*
- **Beare et al. 2020, arXiv:2006.01947v2** (`SRC_ARXIV_2006_01947`; addendum). *Resolves* the `ultracold-source` item
  "Muonium yield per incident muon at J-PARC from Beare et al. ...: the projected number did not appear": "The expected
  rate of the muonium atoms for laser ionization is estimated to be 3.4 × 10^−3 per incident surface muon [13]" (p.32;
  `SOURCE_G2_THERMAL_MUONIUM_PER_SURFACE_MUON_BEARE2020`), the same 3.4e-3 as Abe 2019; formation fraction 0.655 ± 0.018
  (p.25); emission 5–28 ‰ for the ablated targets (p.19). *Still open:* the 0.52 vs 0.655 discrepancy "is not
  understood well" (p.25); the source-registry `unresolved_questions` of this record still carry the snippet-era item
  (for the registry owner to update).
- **J-PARC g-2/EDM design, Abe et al. 2019, arXiv:1901.03047v2** (`SRC_ARXIV_1901_03047`, PTEP 2019 053C02; batch 7).
  *Resolves* the `ultracold-source` fetch entry for 1901.03047; *narrows* "Rate chain (per-stage efficiencies) is
  incomplete". Settled: thermal muonium 3.4e-3 per surface muon (p.8); laser ionisation 0.73, a **calculation** "based on
  the transition rates given by theoretical excitation and dissociation cross sections multiplied with the expected
  laser photon density" (p.8; `SOURCE_LASER_IONISATION_EFF_CALC_ABE2019`); the Table 4 chain, 1.3e-5 per initial muon;
  H-line "∼ 1e8 per second" (Table 5 implies ≈ 3e8/s, an internal-consistency observation,
  `tests/scientific/test_batch7_documents.py::test_abe2019_hline_rate_implied_by_table5_vs_quoted_1e8`); IH-DTL 4.5 MeV
  (`CONF_JPARC_IHDTL_ENERGY`); EDM statistical precision 1.5e-21 e·cm (Table 1, `PHYS_EDM_PRECISION_STAT_TABLE1_ABE2019`),
  which settles the PTEP 2019 side of the `ultracold-source` item on the EDM sensitivity goal. *Still open:* the
  1.5e-19 e·cm rendering of the Mibe 2025 slides (snippet-level, unexplained); 0.52 is quoted without its own reference.
- **Aritome et al. 2024, arXiv:2410.11367v2** (`SRC_ARXIV_2410_11367`, PRL 134, 245001; addendum). *Resolves* the
  `ultracold-source` item 'A snippet stated "A 2025 talk reported a first RF acceleration of cooled muons, but the rate
  was low, at about 2×10⁻³ per pulse ..."': the paper gives 2e-3 μ+/pulse at 100 keV from 9.5e4 surface μ+/pulse, i.e.
  2.1e-8 per surface muon (`SOURCE_USM_PER_SURFACE_MUON_100KEV_ARITOME2024`;
  `tests/scientific/test_workshop_decks.py::test_aritome2024_measured_ultra_slow_muon_chain`). *Narrows* "Normalised-
  emittance chain (design → measured)" (measured εnorm,rms (0.85, 0.32) π mm·mrad, p.4) and "No measured 122 nm/355 nm
  ionisation efficiency appeared" (the test used a 244 nm spectroscopy laser, simulated efficiency 7e-6 – 6e-5; the
  dedicated 122 + 355 nm sources are projected at "around 10%"; `CONF_LASER_IONISATION_EFFICIENCY`). *Still open:* no
  measured 122 + 355 nm efficiency exists anywhere; the measured chain is ≈ 2.5e6 below the μTRISTAN post-stopping
  budget and ≈ 1.2e5 below the g-2 target; the source-registry `unresolved_questions` of this record still say "Full
  text not read" (stale, for the registry owner).
- **μTRISTAN hybrid target, Sakaki et al. 2026, arXiv:2605.25580v1** (`SRC_ARXIV_2605_25580`; batch 7; ref. [18] of
  arXiv:2610.35154). *Resolves* the `ultracold-source` item on its normalisation "per p–Li nuclear collision" and its
  fetch entry: 6e-4 ultraslow muons per p–Li collision with the muon-to-muonium conversion set to one (η_conv "has
  not, however, been separately quantified", `SOURCE_HYBRID_MU_TO_MUONIUM_CONVERSION_SAKAKI2026` = null), N_tot = η_conv ×
  1.2e12 s^-1 per MW before extraction (`SOURCE_HYBRID_PRE_EXTRACTION_RATE_SAKAKI2026`;
  `tests/scientific/test_batch7_documents.py::test_sakaki2026_pre_extraction_rate_upper_limit`; `CONF_SOURCE_CONCEPT`).
  *Still open:* extraction, drift and second-stage cooling losses and the emittance are outside the paper's scope, so no
  end-to-end μ+/s figure exists; the Matsudo 2024 "~5.5e-4 muons per proton" slide is still unattributed.
- **Giove 2026, "RF System"** (IMCC and MuCol Annual Meeting, `SRC_IMCC2026_GIOVE_RF_SYSTEM`; batch 9). No earlier
  backlog item; it narrows the RF question of the hybrid-source option (Rogers: "RF Breakdown (sparking) in
  solenoids"). Settled: thin-window cavities, 704 MHz as the reference frequency of the first cells, "gradients of 30
  MV/m"; no gradient or breakdown measurement is shown (`SOURCE_COOLING_RF_BREAKDOWN_DATA_GIOVE2026` = null). The in-field
  breakdown data restated by Rogers favour beryllium (Cu 24.4 → 12.9 MV/m at 0 → 3 T; Be 41.1 → > 49.8 MV/m), while INFN
  plans aluminium windows for the demonstrator because of beryllium supply and safety. *Still open:* no uploaded source
  gives aluminium breakdown performance in a magnetic field; which hybrid-source cavities Giove's 704 MHz thin-window
  cells would serve is not stated (Rogers' rectilinear A-stages: A1–A2 at 352 MHz, A3–A4 at 704 MHz, p.12,
  `SOURCE_HYBRID_RECT_A*_RF_FREQUENCY_WS2026_ROGERS`; corrected by the registry-stage verifier, 2026-10-29).

### Uploaded, not yet used by any record

- `SRC_ARXIV_2609_37117` (U.S. Muon Collider Collaboration input to the SCAC Facilities Subcommittee) and
  `SRC_ARXIV_2610_14303` (AI4MuC workshop report) are registered and archived as SECONDARY_SOURCE; no parameter record
  cites them as of 2026-10-29.

### Phase-0 synthetic bands overtaken by the uploads

The bands below are those written on 2026-10-28, before the uploads were read. Supersession and re-basing under
CLAUDE.md §4 are recorded in `parameters/assumptions/phase0_assumptions.yaml` and in the `_SYN` records, not here; this
list only records what the uploads showed.

- `DET_NOZZLE_OPENING_ANGLE_SYN` (`ASM_DET_NOZZLE_OPENING_ANGLE`; uniform 5–20°) excluded the reported LHμC option
  40 mrad = 2.29° (`CONF_NOZZLE_OPENING_ANGLE`); the nozzle length and tip-distance bands (2–10 m, 2–50 cm) contained
  the reported 587.8 cm and 6 cm, but reported values now exist for all three quantities.
- `IR_LSTAR_SYN` (`ASM_IR_LSTAR`; 5–20 m) excluded the 23 m layout on Forthomme p.4 (`CONF_IR_LSTAR`); whether that
  layout is relevant to LHμC is open.
- `SOURCE_LASER_IONISATION_EFFICIENCY_SYN` (`ASM_SOURCE_LASER_IONISATION_EFFICIENCY`; log-uniform 1e-3 – 1) excluded
  every demonstrated 244 nm value (~1e-6 – 6e-5); a band that also covers them mixes two laser schemes, so results drawn
  from it must be reported per scheme (`CONF_LASER_IONISATION_EFFICIENCY`).
- `SOURCE_MUONIUM_FORMATION_FRACTION_SYN` (0.3–0.7) and `DET_SOLENOID_FIELD_SYN` (2–5 T) bracketed the values now
  measured or reported (0.52 and 0.655; 3, 3.8 and 5 T), but reported values now exist for both.
- The treatment text of `CONF_LHEC_CROSSING_ANGLE` (2026-10-28) speaks of a 0–7 mrad scan, whereas `IR_CROSSING_ANGLE_SYN`
  spans 0–10 mrad; the record governs (noted in the conflict on 2026-10-29). Likewise the 2026-10-28 text of
  `CONF_LUMI_MODEL_ASSUMPTIONS` speaks of a 7.5–9 cm proton bunch length, whereas `PROTON_BUNCH_LENGTH_RMS_SYN` was 5–12 cm
  (widened on 2026-10-29 to log-uniform 5–100 cm after the Zimmermann deck; `ASM_PROTON_BUNCH_LENGTH_RMS`).

### Batch 10 (uploads of 2026-10-29)

Resolved or narrowed:

- `SRC_ARXIV_1905_05564` (Kaya, Ketenoglu, Sultansoy, Zimmermann; EPL 138 (2022) 24002): full arXiv v2 text read. The
  muon-side inputs are the MAP muon-collider options of Delahaye et al. (arXiv:1901.06150, Table 3: N_μ 2e12, ε_N 25 µm,
  β* 1/0.5/0.25 cm, 15/12/6 Hz); the "2.2×10^12 muons per bunch" of the earlier query note is not in the paper. All 12
  luminosities and 8 tune shifts reproduce (`tests/scientific/test_batch10_documents.py`). Recategorised
  SECONDARY_SOURCE → RELATED_MACHINE.
- `SRC_ARXIV_1407_8248` (Beer et al. 2014): full text read. The "0.01 Mu per incident muon" is this paper's own J-PARC
  projection (p. 5); the "≥ 8×" enhancement is Table 1's 30.5/3.72 = 8.2. The paper gives **no** muonium formation
  fraction.
- `SRC_DOI_10_7566_JPSCP_33_011125` (Zhang et al. 2021, new): the 244 nm 1S-2S demonstrator chain, ionisation
  3.9e-7 per vacuum Mu (p. 4), final 0.0109 s^-1 (Table I).

Still open (new):

- **Origin of the diffusion fit T = 322 K, D = 870 cm² s^-1.** Zhang et al. 2021 cite Beer et al. 2014 [8] for it, for the
  52 % formation fraction and for the 23.2 mg cm^-3 / 8.8 mm sample; Beer et al. 2014 contains none of them (its samples
  are 29 mg cm^-3, 7 mm), and Zhang's reference list does not include Bakule 2013 (the 0.52 matches it by value only). The sample matches Beare et al. 2020 p. 5; T and D appear only on the 2026 Zhang Kraków deck
  p. 7. Wanted: the publication that reports the fit (candidate: a Zhang et al. muonium-diffusion paper, cited by
  Sakaki et al. 2026 as "Zhang et al. 2022"). *[2026-10-29: candidate for the alphaXiv connector if an arXiv version
  exists (search first).]*
- **Zhang et al. 2021 internal inconsistencies**: S2 surface-muon rate 2.4×10^5 (§2) vs 2.4×10^6 (§5, Table I);
  stopping 44.3 % (text) vs 0.467 (Table I); extraction 1.5e3/2.0e3 = 0.75 vs the stated 58.6 %. An erratum or the
  J-PARC S2 commissioning rate would settle the first.
- **Definition of the MAP average luminosity** used by Kaya et al. as L_μμ (decay averaging over two beams, beam-beam
  enhancement, hourglass factor): Delahaye et al. arXiv:1901.06150 (blocked). Needed to turn the one-beam vs two-beam
  decay ratio (1.87–1.97, `tests/scientific/test_imcc_mr7_reference.py`) into a corrected μp number.
  *[2026-10-29: candidate for the alphaXiv connector (search first).]*
- **A μp luminosity calculation for the Kaya et al. options** with the 90 mm proton bunch (hourglass), one decaying
  beam and a beam-beam-limited ξ_p — a documented tool run (AloHEP or an own beam-beam code), not hand arithmetic.
- Bordry et al. arXiv:1810.13022 (HL-LHC/HE-LHC/ERL60 tables quoted by Kaya et al. Tables 1-2): the HL-LHC ERL60 proton
  size 4.45 µm is 2.7 % above √(ε_N β*/γ) with the printed ε_N = 2 µm, β* = 7 cm.
  *[2026-10-29: candidate for the alphaXiv connector (search first).]*
- `SRC_ARXIV_2608_25374` (Shirotori et al. 2026, context only): the stated 85 % ↔ 90° CM emission point does not
  reproduce (two-body kinematics give 78.7 %); the T106 proposal (KEK/J-PARC-PAC 2025-39) behind the ±5 % momentum
  bite was not read.
- **Re-measured ablated target** (`CONF_ABLATED_AEROGEL_REMEASUREMENT`, open): Beer et al.'s 400 µm-pitch target, 20.9 ± 0.7 ‰
  in 2013, was re-measured by Beare et al. (target S2013-1, 'Reuse of O2013-3') at 17.2 ± 0.2 ‰ in 2017 — 5.1 σ on
  statistics, 1.6 σ with the stated systematics; neither paper explains it. Wanted: the authors' statement or a repeat.
- **J-PARC surface-muon momentum** (`CONF_JPARC_SURFACE_MUON_MOMENTUM`, resolved as scenarios): 28 MeV/c in Bakule 2013,
  Beer 2014 and the Zhang 2021 text vs 27 MeV/c in Abe 2019 and the Zhang 2021 Fig. 1 inset; the commissioning value of
  the delivered momentum would settle it.

### Still open after the uploads

- Unchanged from the family sections below: the HELP4CERN White Paper and help4cern.web.cern.ch (`ME_001`); the ICHEP
  2026, ADM, AGH and SAIP listings and slides; the PTEP 2026 erratum text (`ME_016`); the HL-LHC TDR proton tables
  (`ME_044`); the LHeC CDR and 2020 update (`ME_046`) and arXiv:2503.20475; the Topp-Mugglestone thesis; IPAC'21
  WEPAB278; the Kraków contributions not uploaded (Otani `ME_008`, Piotrzkowski `ME_011`, Tentori `ME_012`, Holzer);
  the μLHC AloHEP input decks (`ME_043`); the MR7 reference tables (verified and committed 2026-10-29); every item of the
  `theory-benchmarks` and `software-tools` families.
- New, raised by the uploads: the nine conflict records listed at the top of this section, each with its own
  `required_future_evidence`; in particular a measured 122 + 355 nm ionisation efficiency, a 3D space-charge front-end
  design for ≥ 1e10 μ+ per bunch, an LHμC booster vFFA lattice with tracking, an LHμC IR design (L*, crossing angle,
  separator) and a μ+p beam-induced-background simulation per nozzle option.

---

## Family `lhmuc-primary` (from `research/_fragments/lhmuc-primary_unresolved.md`)

### Unresolved items — reconnaissance family `lhmuc-primary`

Searches run 2026-10-28 with WebSearch only. Every WebFetch attempt failed (`getaddrinfo ENOTFOUND`) on
arxiv.org, indico.cern.ch, help4cern.web.cern.ch, indico.fis.agh.edu.pl, events2.saip.org.za,
avesis.uludag.edu.tr and academic.oup.com. Everything below is therefore snippet-level evidence: it may
not back a `reported_lhmuc` status and is capped at confidence `medium` (CLAUDE.md §1.5). Nothing in this
file is a parameter record.

### Unresolved items

- **help4cern.web.cern.ch** never appeared in any search result and the direct fetch failed. Its page list,
  any parameter tables and the official HELP4CERN statement of the LHμC baseline remain unverified.
- **HELP4CERN White Paper** ("High Energy, High Luminosity Lepton-Hadron Colliders at CERN"): cited as
  "in preparation" by arXiv:2610.35154, by the ICHEP 2026 abstracts and (per the uploaded Khanpour deck)
  as the origin of the benchmark working points. No URL, arXiv id or date exists as of 2026-10-28.
- **Kraków workshop contributions (Indico 1681458)**: no snippet exposed titles or abstracts for Kilic
  (nozzle), Topp-Mugglestone (vFFA), Zimmermann (SPS/LHC modifications), Acosta (near-beam detectors),
  Yamazaki (TeV-muon detectors), Otani (pre-acceleration), Rogers (hybrid source), Zhang (muonium
  diffusion), Kumar (di-Higgs), Khanpour (two-photon), Dagli (nucleus options). Only the speaker list
  (Ce Zhang, Schulte, Otani, Yamazaki, Sultansoy, Forthomme, Piotrzkowski) and the citation of
  Forthomme's "LHeC/LHμC main detector" talk in arXiv:2610.35154 were seen. The timetable fetch was blocked.
- **Registration-date conflict** for Indico 1681458: snippets give 25 May 2026 and 31 July 2026 as
  registration start. Preserved as a conflict; irrelevant to physics but a marker of snippet unreliability.
- **Natal 2026 / ICHEP (Indico 1522800) speaker attribution**: the task names a "Forthomme talk at Natal
  2026"; all snippets list Krzysztof Piotrzkowski as speaker of contribution 6986580 (500 GeV μ+, 7 TeV p,
  √s = 3.74 TeV, L > 1e33 cm^-2 s^-1). Forthomme's role at Natal is unconfirmed. Exact titles of the two
  further Help4CERN contributions 6983210 and 6980628 were not visible.
- **Bunch numbers and repetition rate**: no snippet gave bunch count, bunch population or repetition rate
  (Hz) for the LHμC source, booster or main ring. The full text of arXiv:2610.35154 (uploaded copy, Table 1)
  is the place to check; the web record itself is blocked.
- **Parameter-set evolution (three distinct sets, none labelled "baseline")**:
  (a) 500 GeV μ+ / 7 TeV p / 3.74 TeV / > 1e33 — ICHEP 2026 listing 6986580 and Accelerator Design Meeting
  6996662; (b) 1 TeV / 5.3 TeV / > 1e33 — AGH HEP seminar 462 (May 2026); (c) 1 or 2 TeV / 5.3 or 7.5 TeV /
  average luminosity near 1e34 — arXiv:2610.35154 abstract (26 Oct 2026). Which is current is not stated in
  any snippet; must be modelled as separate scenarios, not averaged (CLAUDE.md §1.6).
- **Accelerator Design Meeting (Indico 1664360)**: meeting date, speaker of companion contribution 6996661
  and availability of slides not visible.
- **AGH HEP seminar (indico.fis.agh.edu.pl event 462)**: exact day in May 2026 not visible.
- **DIS2026**: no DIS2026 Indico event, timetable or proceedings volume for the Piotrzkowski contribution
  was found; only the arXiv comment "contribution to DIS 2026 Proceedings".
- **arXiv:2610.35154 web record**: version number, licence metadata and full author list not confirmed on
  arxiv.org (the uploaded PDF states CC BY-NC-ND 4.0 and v1).
- **arXiv:2506.15445 (μLHC) snippet values**: "960 GeV and up to 1 TeV" booster energy and "above 1e33"
  luminosity must be reconciled with the uploaded v2 and the PTEP erratum (the Nucleus Options deck quotes
  post-erratum 7.2e33 / 8.8e33). Snippets are not to be used for this; the uploaded PDF is.
- **Name collision "LHmuC"**: arXiv:2203.06258 and the Snowmass 2021 muon-ion-collider slides use "LHmuC"
  for a different concept (3 TeV muon-collider beam on LHC protons, ~6.5 TeV). Must stay distinct from the
  HELP4CERN LHμC in every registry and scenario id.
- **SAIP 2026 di-Higgs talk (contribution 653)**: relation to the uploaded Kraków deck
  SRC_WS_LEBOHO_KUMAR_DIHIGGS is inferred from author overlap only; the slides PDF was not fetched; paper
  "still in progress". Lead classed it PRIMARY_LHMUC, but no value from it may be `reported_lhmuc` until read.
- **INSPIRE**: no literature record for LHμC / arXiv:2610.35154 surfaced; only the author profile 993289.
  Journal flags fetch_blocked=false for the profile but does not record a page read, so access is
  `snippet_only`.
- **Not registered (seen only as titles in result sets)**: arXiv:1807.09867 "The LHC based μp colliders",
  arXiv:2207.10565 (muon-nucleus collider parameters), arXiv:1905.05564 (preprint of the EPL 2022 paper,
  recorded as `arxiv_id` of SRC_ARXIV_1905_05564), Snowmass 2021 Wei Li slides
  (indico.fnal.gov/event/52701/contributions/231920). To be registered only after a fetch.
- **Lead category corrections that do not apply to this family** (no such source in the journal):
  arXiv:2504.21417, arXiv:2503.17727, Topp-Mugglestone thesis (ora.ox.ac.uk), DESY/FNAL/STFC decks, Evian
  papers, LHC-MACHINE-OUTREACH page, ResearchGate profile, arXiv:2610.28252, arXiv:2610.17801. None added.

### Fetch backlog (once network access to these hosts is allowed)

- https://arxiv.org/abs/2610.35154 and https://arxiv.org/html/2610.35154 — confirm version (v1?), licence
  metadata, author list, submission comment; cross-check Table 1 bunch numbers / repetition rate against the
  uploaded PDF; record the "in preparation" white-paper reference verbatim.
- https://indico.cern.ch/event/1681458/timetable/ and /contributions/ — full contribution list with titles,
  speakers, abstracts and attached slides (Kilic nozzle, Topp-Mugglestone vFFA, Zimmermann SPS/LHC,
  Acosta near-beam, Yamazaki TeV-muon detector, Otani pre-acceleration, Rogers hybrid source, Zhang muonium,
  Kumar di-Higgs 7263322, Khanpour 7263325, Dagli 7263320); resolve the registration-date conflict; proceedings
  (Acta Physica Polonica B supplement) status.
- https://indico.cern.ch/event/1522800/contributions/6986580 — exact title, speaker (Piotrzkowski vs
  Forthomme), abstract verbatim (500 GeV / 7 TeV / 3.74 TeV / > 1e33), attached slides and their licence.
- https://indico.cern.ch/event/1522800/contributions/6983210 — exact title, speaker, abstract (g-2 EFT,
  RPV SUSY lepton-quark fusion, colour-octet muons), slides.
- https://indico.cern.ch/event/1522800/contributions/6980628 — exact title, speaker, abstract
  (Higgs-Electroweak-Top potential), slides.
- https://indico.cern.ch/event/1664360/contributions/6996662/ and
  https://indico.cern.ch/event/1664360/contributions/6996661/ — meeting date, speakers, abstracts verbatim
  (7 TeV / 3.74 TeV / > 1e33 / 500 GeV), slides with any MDI sketch or beam-parameter table.
- https://indico.fis.agh.edu.pl/event/462/ — seminar date, abstract verbatim (1 TeV / 5.3 TeV / > 1e33), slides.
- https://events2.saip.org.za/event/2/contributions/653/ and the slides PDF
  https://events2.saip.org.za/event/2/contributions/653/attachments/224/507/Di_Higgs_at_the_LHC%20(9).pdf —
  author list, collider configuration, cross sections, cut-flow, 95% CL limits; compare slide-by-slide with
  the uploaded Kraków deck to confirm or refute the inferred link.
- https://help4cern.web.cern.ch/ — site map, any LHμC parameter table, white-paper status, member list.
- https://arxiv.org/abs/2506.15445 and https://academic.oup.com/ptep/article/2026/3/033C04/8503486 —
  arXiv licence and version history; PTEP erratum text (luminosity corrections) to reconcile with uploaded v2.
- https://arxiv.org/abs/2406.02647 — author list, machine options, beam parameters behind 5.29 TeV /
  5.2e33 cm^-2 s^-1.
- https://epljournal.edpsciences.org/10.1209/0295-5075/ac4f98 (and arXiv:1905.05564) — volume/article,
  HL-LHC vs HE-LHC options and the beam assumptions behind the "order 1e33" luminosity.
- https://arxiv.org/abs/2206.00037 — author list; parameter tables of the μp proposals it surveys.
- https://arxiv.org/abs/2203.06258 and
  https://indico.fnal.gov/event/52701/contributions/231920/attachments/151428/195639/MuonIonCollider_Snowmass2021_WeiLi_01272022_v1.pdf
  — the muon-ion-collider "LHmuC" parameters (~6.5 TeV), to document the name collision explicitly.
- https://inspirehep.net/authors/993289 and an INSPIRE literature search for arXiv:2610.35154 — citation
  record, any DIS2026 proceedings entry.
- arXiv:1807.09867, arXiv:2207.10565 — read abstracts before deciding whether to register them.

---

## Family `mulhc-mutristan` (from `research/_fragments/mulhc-mutristan_unresolved.md`)

### Unresolved items - reconnaissance family `mulhc-mutristan`

Searches run 2026-10-28 with WebSearch only (20 queries, 29 source records). WebFetch succeeded only on github.com and
raw.githubusercontent.com; attempts on arxiv.org/ar5iv, indico.cern.ch, academic.oup.com, inspirehep.net, jacow.org,
journals.aps.org and researchgate.net failed. Everything below is snippet-level evidence (or, for the two GitHub pages, a
README without beam-parameter content): it may not back a `reported_lhmuc` status and is capped at confidence `medium`
(CLAUDE.md section 1.5). Nothing in this file is a parameter record. Values from the muLHC / muTRISTAN line are
`imported_related` at best once verified from the full text.

### Unresolved items (from the journal)

- No formal PTEP erratum DOI/article number for μLHC (PTEP 2026 033C04) was found in any search snippet; only (a) the PTEP article page's 'Corrected and typeset 28 March 2026' date, (b) a ResearchGate listing 'Erratum μLHC: ...' dated May 2026 on F. Zimmermann's profile, and (c) the arXiv v2 (12 Jun 2026) change log. Needs direct check of academic.oup.com/ptep or INSPIRE (both hosts blocked here).
- Exact corrected numerical values in μLHC Tables 1, 3, 4, 6 (muons per bunch, beta*, emittance, bunch length, number of bunches, revised luminosities) were not visible in snippets; only the relative change (~x2 μTRISTAN-based option, ~x4 LHeC-based option) and the 7.2 nC / 4.5e10 μ+ per injected bunch figure.
- JINST 18 P09025 citation for Acosta et al. not confirmed by any snippet (arXiv page only says 'submitted to JINST').
- Modern Physics Letters A review: snippets give vol. 37, nos. 37-38 (2022) and DOI 10.1142/S0217732322300130; the task's '(2023)' year not confirmed. Title in repository record is misspelled 'collier'.
- μTRISTAN Table 1 per-bunch values were quoted from a secondary reproduction (arXiv:2403.17034), not from 2201.06664 itself.
- AloHEP GitHub repo (yefetu/ALOHEP): no license, version tag or release found; IPAC'21 paper points to alohep.hepforge.org and yef.etu.edu.tr instead (not fetched). First author of WEPAB278 is B.B. Oner, not Dagli as the task states.
- Hosts blocked in this session (fetch_blocked): arxiv.org/ar5iv, indico.cern.ch, academic.oup.com, inspirehep.net, jacow.org, journals.aps.org, researchgate.net. Only github.com / raw.githubusercontent.com fetched successfully.
- Kaya et al. EPL 138 24002: muon-side bunch population, emittance and beta* not visible in snippets (only proton bunch population 2.2e11 and the √s range).

### Unresolved items added while building the registry fragment

- **Category conflict on `SRC_ARXIV_2203_06258`**: this fragment applies the lead's rule 'Snowmass white papers on arXiv -> CONFERENCE_PROCEEDING'; the lhmuc-primary fragment registered the same id as RELATED_MACHINE. `tools/merge_research_fragments.py` keeps the first text (lhmuc-primary), so the lead must decide which category the merged registry carries.
- **Category conflict on `SRC_INDICO_1681458_OVERVIEW`**: journal had OFFICIAL_CERN for the event.ics record; this fragment follows the lead's Indico rule (CONFERENCE_PROCEEDING, web_page), matching the lhmuc-primary entry for the same event.
- **Shared ids with lhmuc-primary** (`SRC_ARXIV_2406_02647`, `SRC_ARXIV_2206_00037`, `SRC_ARXIV_2203_06258`, `SRC_ARXIV_1905_05564`, `SRC_INDICO_1681458_OVERVIEW`): the two families saw different URLs/snippets; the merge unions lists and appends notes but keeps lhmuc-primary's title/url/access text. `SRC_ARXIV_1905_05564` is recorded here as `blocked` (arxiv.org record) whereas lhmuc-primary recorded `snippet_only` (EPL record) - both are correct for their URL.
- **muLHC journal record registered separately** as `SRC_ARXIV_2506_15445` (same work as the uploaded `SRC_ARXIV_2506_15445`) because it alone carries the 'Corrected and typeset 28 March 2026' status; the lead may prefer to fold it into the upload entry.
- **Query-to-source attribution** is taken from the journal's per-query notes; where a mapping was deduced rather than stated it is labelled '(mapping inferred from the query note)'. Five sources could not be attributed to any query (INSPIRE 2936564, the two GitHub pages obtained by direct WebFetch, arXiv:2308.00115, the Wei Li FNAL slides) and carry query '(see family queries)'.
- **Category labels for preprints**: arXiv records of confirmed journal publications carry the journal's category (PEER_REVIEWED for Cheung-Wang 2101.10476) or RELATED_MACHINE when the work describes a related machine (muTRISTAN 2201.06664, Sultansoy-group reviews); the journal's blanket PEER_REVIEWED label on preprints was not kept. No source was promoted beyond snippet evidence.
- **Licences**: none of the journal's 'arXiv open access' / 'CC-BY typical' remarks is a confirmed licence; all `licence` fields are null except the GitHub repository and README, where the fetched pages state no licence at all.
- **Per-source open questions** are listed in `unresolved_questions` of each entry in `mulhc-mutristan_sources.yaml`.

### Fetch backlog (once network access is allowed)

- `SRC_ARXIV_2506_15445` <https://arxiv.org/abs/2506.15445> - extract: arXiv v2 abstract page: licence, version history (v1 date, v2 '12 Jun 2026' comment text), full author list; compare the v2 PDF with the uploaded references/_local/arXiv-2506.15445v2.pdf (SHA-256) to confirm the upload is the corrected version.
- `SRC_ARXIV_2506_15445` <https://academic.oup.com/ptep/article/2026/3/033C04/8503486> - extract: PTEP 2026 033C04: open-access licence; 'Corrected and typeset 28 March 2026' notice text; whether a separate erratum DOI exists; corrected Tables 1, 3, 4, 6 and Figures 3, 7 (muons per bunch, beta*, emittance, bunch length, number of bunches, survival rates, luminosities for the muTRISTAN-based and LHeC-ERL-based booster options).
- `SRC_ARXIV_2506_15445` <https://inspirehep.net/literature/2936564> - extract: INSPIRE record: erratum record (if any), DOI, citing papers, arXiv/PTEP cross-links.
- `SRC_URL_RESEARCHGATE_ZIMMERMANN_PROFILE` <https://www.researchgate.net/profile/Frank-Zimmermann-5> - extract: ResearchGate listing 'Erratum muLHC ...' (May 2026): venue, DOI, and whether a readable erratum text is attached; low priority (secondary).
- `SRC_ARXIV_2201_06664` <https://arxiv.org/abs/2201.06664> - extract: muTRISTAN preprint: Table 1 (mu+ per bunch 1.4e10?, 40 bunches, 2 mm bunch length, 4 um normalised emittance, beta* 3 cm / 0.7 cm, 4 MHz) to verify the values seen only in the arXiv:2403.17034 reproduction; licence.
- `SRC_ARXIV_2201_06664` <https://academic.oup.com/ptep/article/2022/5/053B02/6556027> - extract: muTRISTAN PTEP 2022 053B02: DOI, licence, and whether the journal table differs from the arXiv version.
- `SRC_ARXIV_2403_17034` <https://arxiv.org/pdf/2403.17034> - extract: Author list; the reproduced muTRISTAN table and the AloHEP input set used for 4.54e33 vs 4.6e33; EPL DOI 10.1209/0295-5075/ad5e1a confirmation.
- `SRC_ARXIV_2206_00037` <https://arxiv.org/abs/2206.00037> - extract: Review of mu-p proposals: LHC-based mu-p tables (muon energies 0.75/1.5/3 TeV; beta* 1/0.5/0.3 cm; L 2.3e33 at 1.5 TeV), the muon-side parameters assumed, HL-LHC proton set (2.2e11, 2.0 um), MuIC (BNL) set and AloHEP settings; licence.
- `SRC_DOI_10_1142_S0217732322300130` <https://avesis.ankara.edu.tr/yayin/d1264ca1-82e9-4609-944a-404d6c7aa83e/review-of-muon-proton-and-muon-nucleus-collier-proposals> - extract: MPLA review repository record: confirm year (2022 vs 2023), volume/issue/pages, DOI 10.1142/S0217732322300130; then fetch the World Scientific record.
- `SRC_ARXIV_2207_10565` <https://arxiv.org/pdf/2207.10565> - extract: Muon-nucleus parameter review: LHC-based muA options (ion species, luminosities) to compare with the uploaded Nucleus Options deck (p.10-14); authors; licence.
- `SRC_ARXIV_1905_05564` <https://arxiv.org/abs/1905.05564> - extract: Kaya et al.: muon-side bunch population, emittance, beta* and the machine options behind the 4.58-12.7 TeV range and ~1e33 luminosities; v2 (Nov 2021) change log.
- `SRC_ARXIV_1905_05564` <https://gcris.etu.edu.tr/handle/20.500.11851/8699?mode=full> - extract: TOBB ETU record: confirm EPL 138(2) 24002 metadata and any deposited full text/licence.
- `SRC_ARXIV_2101_10476` <https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.116009> - extract: Cheung & Wang PRD 103 116009: beam-energy combinations and integrated luminosities (0.1-1 ab^-1) assumed; process list (Higgs, RPV SUSY, g-2) for the LHmuC physics-programme comparison.
- `SRC_ARXIV_2101_10476` <https://export.arxiv.org/abs/2101.10476> - extract: Preprint version history and licence for Cheung & Wang (mirror of arxiv.org; expected to fail while arxiv.org is blocked).
- `SRC_ARXIV_2203_06258` <https://arxiv.org/abs/2203.06258v2> - extract: MuIC Snowmass white paper: parameter tables (muon beam from the Muon Collider design, BNL/FNAL/CERN hadron beams), the 'LHmuC' ~6.5 TeV option, and the journal-reference line (JINST 18 P09025 confirmation).
- `SRC_URL_POS_ICHEP2024_817` <https://pos.sissa.it/476/817/> - extract: PoS(ICHEP2024)817: title, authors, DOI, licence (CC-BY?) and any updated MuIC parameters.
- `SRC_JACOW_IPAC2021_WEPAB278` <https://jacow.org/ipac2021/papers/WEPAB278.pdf> - extract: AloHEP IPAC'21 paper: luminosity formula, beam-beam tune shift, disruption and crossing-angle treatment, hourglass handling, validation cases; JACoW licence statement; canonical download site (alohep.hepforge.org, yef.etu.edu.tr).
- `SRC_URL_ACCELCONF_IPAC2021_WEPAB278_BIB` <https://accelconf.web.cern.ch/ipac2021/export/WEPAB278-bib.htm> - extract: BibTeX export: authoritative author list and DOI for WEPAB278.
- `SRC_URL_GITHUB_YEFETU_ALOHEP` <https://github.com/yefetu/alohep> - extract: Already fetched (repository page). Still to do: inspect the 'save' accelerator JSON files for field names/units, settings.JSON, commit history dates; ask the authors about the licence before any use.
- `SRC_URL_GITHUB_YEFETU_ALOHEP_README` <https://raw.githubusercontent.com/yefetu/ALOHEP/master/README.md> - extract: Already fetched and read; nothing further unless the README changes.
- `SRC_ARXIV_2308_00115` <https://arxiv.org/pdf/2308.00115> - extract: Authors; AloHEP scope statement; LHC-based ep alternatives (background for the LHeC-ERL reuse assumed by LHmuC).
- `SRC_ARXIV_2406_02647` <https://arxiv.org/abs/2406.02647v2> - extract: muTRISTAN-ring + LHC/Tevatron/FCC/SppC paper: the HL-LHC mu+p table (5.29 TeV, 5.2e33 per lhmuc-primary snippets), mu+A luminosities (>1e30), EPJ Plus DOI; licence.
- `SRC_ARXIV_2610_35154` <https://arxiv.org/abs/2610.35154> - extract: LHmuC DIS2026 abstract page: licence metadata, version, comments; the uploaded v1 PDF already supplies the content.
- `SRC_INDICO_1600007_6742086` <https://indico.cern.ch/event/1600007/contributions/6742086/attachments/3171003/5637418/Sultansoy%20muLHC%2011.11.2025.pdf> - extract: Sultansoy e/mu-LHC proposal talk (CERN, 11.11.2025): post-erratum muLHC parameter table (candidate origin of 7.2e33 / 8.8e33 'after the erratum'), booster options, muA options; event name and session.
- `SRC_INDICO_1681458_OVERVIEW` <https://indico.cern.ch/event/1681458/event.ics> - extract: Kraków workshop calendar export: contribution titles, speakers and times for the whole timetable (cross-check with lhmuc-primary's overview-page backlog).
- `SRC_INDICO_1553599_6692057` <https://indico.cern.ch/event/1553599/contributions/6692057/attachments/3137064/5566633/FFA'25Takaura.pdf> - extract: Takaura FFA'25 slides: current muTRISTAN mu+ source and acceleration parameters, any change relative to arXiv:2201.06664.
- `SRC_URL_KEK_IPNS_202203THEORY` <https://www2.kek.jp/ipns//docs/report/2022/03/202203theory.pdf> - extract: KEK IPNS March 2022 report (Japanese): confirm the muTRISTAN summary statements (1 TeV mu+ on 30 GeV e-, ~1e5 Higgs per IP in ten years, 1 TeV mu+mu+ in the same tunnel); low priority (secondary).
- `SRC_ARXIV_2402_10952` <https://arxiv.org/pdf/2402.10952> - extract: FNAL mu-p options: authors; AloHEP inputs behind L = 1.2e33 (high mu-rate) and 1.0e32 (low mu-rate) as an AloHEP cross-check case.
- `SRC_URL_INDICO_FNAL_52701_231920` <https://indico.fnal.gov/event/52701/contributions/231920/attachments/151428/195639/MuonIonCollider_Snowmass2021_WeiLi_01272022_v1.pdf> - extract: Wei Li Snowmass 2021 slides: the 'LHmuC' option slide (reuse of the LHC ring, concurrent running with a 3 TeV muon collider), Muon Collider parameter set used (arXiv:1901.06150), EIC CDR proton parameters.

Also to be located (no URL yet): alohep.hepforge.org and yef.etu.edu.tr (canonical AloHEP distribution named in WEPAB278); the World Scientific record of MPLA DOI 10.1142/S0217732322300130; the EPJ Plus 2025 record of arXiv:2406.02647; JINST 18 P09025 (claimed journal version of arXiv:2203.06258).

---

## Family `lhc-hl-lhc-protons` (from `research/_fragments/lhc-hl-lhc-protons_unresolved.md`)

### Unresolved items — reconnaissance family `lhc-hl-lhc-protons`

Searches run 2026-10-28 with WebSearch only: 20 queries planned, 16 executed (2 of them returned nothing
useful), 4 never run because the per-turn WebSearch budget was exhausted; 30 sources surfaced. The journal
records that WebFetch failed on e-publishing.cern.ch, accelconf.web.cern.ch, pdg.lbl.gov and indico.jacow.org
("not resolvable in this session") and marks every arXiv, Indico and JACoW/refs.jacow entry "fetch blocked".
Nine URLs on other hosts (epaper.kek.jp x3, proceedings.jacow.org, ar5iv.labs.arxiv.org, jinst.sissa.it,
LHC-MACHINE-OUTREACH.web.cern.ch, lhc-closer.es) carry `fetch_blocked=false` in the journal but no page was
ever read, so they are `snippet_only`. Everything below is therefore snippet-level evidence: it may not back a
`reported_lhmuc` status and is capped at confidence `medium` (CLAUDE.md §1.5). Nothing in this file is a
parameter record; every LHC / HL-LHC proton or ion number is at best `imported_related` once verified against
the source table with page number and verbatim quotation.

### Unresolved items

- **No LHC or HL-LHC design document was read in full.** The HL-LHC proton baseline the LHμC proposal
  inherits (7 TeV, 2.2e11 p/b, 2760 bunches, 25 ns, 2.5 µm, β* = 15 cm, 11245 Hz, 26659 m) is presently
  backed only by search snippets of the 2020 TDR, the 2017 TDR V0.1, arXiv:2206.00037, arXiv:2505.03535,
  IPAC'12 MOPPC005 and arXiv:2005.04520. Only Nb = 2.2e11, nb = 2760/2744/2808 and ε = 2.5 µm were seen in a
  TDR snippet; 7 TeV, β* = 15 cm, revolution frequency, circumference and bunch spacing were **not** seen
  verbatim in any TDR snippet.
- **Bunch-count conflict to preserve (CLAUDE.md §1.6), not average:** 2760 (TDR 2020 standard), 2744 (TDR 2020
  BCMS), 2748 (TDR 2017 V0.1 standard, repeated by arXiv:2505.03535), 2604 (TDR 2017 BCMS), 2808 (nominal LHC
  design; also the 25 ns case in IPAC'12 MOPPC005). Which value the LHμC/μLHC papers use for "HL-LHC protons"
  is not stated in anything seen; candidate conflict record `CONF_HLLHC_PROTON_BUNCH_COUNT`.
- **Emittance conflict to preserve:** 2.5 µm (TDR 2020, MOPPC005, arXiv:2206.00037 companion table) vs 2.0 µm
  (arXiv:2206.00037 e-p table) vs 3.75 µm (nominal LHC glossary). β* likewise: 0.15 m (HL-LHC pp IP1/5) vs
  0.07 m (e-p table in arXiv:2206.00037) vs 0.55 m (nominal LHC). The μp IR value is a design choice of the
  LHμC study, not an HL-LHC fact.
- **The Zimmermann "Potential possibilities of modifying SPS/LHC" talk/note was not found** (two dedicated
  queries, one useless). The closest primary statement is arXiv:2610.35154 p.4: a smaller number of LHC proton
  bunches (lower collision rate) could allow a higher population per bunch (22e11 in Table 1), citing its
  ref. [24]. The 200 MHz RF / 8b4e / 50 ns linkage to the LHμC proposal is **unconfirmed**; the only quantified
  8b+4e figure seen (~2.3e11 p/b, 1900 bunches) is from arXiv:1412.7857 and is an LHC-injector scheme, not an
  LHμC statement. Ref. [24] of arXiv:2610.35154 must be resolved from the uploaded PDF reference list (p.6-7).
- **Snippet mis-attributes arXiv:2610.35154 to "S. Moretti, F. Zimmermann et al."**; the uploaded PDF p.1 reads
  "K. Piotrzkowski on behalf of the HELP4CERN Study Group". The registry (uploaded) entry is authoritative. The
  snippet values 4 MHz / 12.5 Hz / 22e11 do agree with Table 1 of the uploaded text.
- **LHC Design Report Vol. 1 (CERN-2004-003-V-1) parameter values were not quoted from the report itself**; the
  nominal numbers (1.15e11, 2808, 3.75 µm, 11245 Hz, 26659 m, β* = 0.55 m) came from the HL-LHC TDR glossary
  snippet and two secondary web pages (lhc-closer.es, LHC Machine Outreach). lhc-closer.es additionally quotes
  an unnamed "design-era document" (26658.87 m, 11.24551 kHz, 400.8 MHz, h = 35640, 2835 bunches) whose origin
  must be identified before any of it is used.
- **PDG "High-Energy Collider Parameters" 2024/2025 editions were not surfaced**; only the 2017/2018/2020 PDFs,
  with no numeric LHC/HL-LHC entries in snippets (only the HL-LHC physics-start year 2026).
- **IPAC'21 MOPAB005 is an oxygen pilot-run study, not a Pb parameter source** (the task description was
  wrong); its values were not obtained (accelconf blocked). **IPAC'18 MOPMF039 is "First Xenon-Xenon Collisions
  in the LHC"** (Xe only, Fill 6295 values in snippet), not a general Pb/Xe parameter paper.
- **Pb beam parameters** (HL-LHC design column: 1240 bunches, 50 ns, 18e7 Pb/bunch, 20.5 MJ) come from an
  ar5iv snippet of arXiv:2107.09560 that the journal itself flags as "partly garbled"; column alignment must
  be verified. Run 3 energy 6.8 Z TeV / Run 4 nominal 7 Z TeV and the 2.2e11 Pb82+ ions/beam target
  (arXiv:2304.03628) are snippet-only.
- **IPAC'26 MOP1054 Table 2 (p-O, O-O, Ne-Ne beam energies, intensities, bunch numbers) not obtained**; its
  companion THP4085 (injectors) and the Schaumann JINR talk and the "indico sps-lhc-batch.pdf" mentioned in
  query notes were not registered as sources (only titles/mentions seen).
- **Category decisions awaiting the lead** (journal classification kept unless a lead rule applied):
  arXiv:2505.03535, arXiv:2505.00947, arXiv:1412.7857, arXiv:1409.5821 are recorded as OFFICIAL_CERN on the
  journal's say-so with authors unconfirmed (candidates: PEER_REVIEWED / CONFERENCE_PROCEEDING / SECONDARY);
  arXiv:2107.09560, arXiv:2304.03628, arXiv:2508.19653, arXiv:2005.04520 are recorded as PEER_REVIEWED without
  a confirmed journal reference (candidate: UNVERIFIED); arXiv:1905.05564 and arXiv:1807.09867 are
  SECONDARY_SOURCE but are μp design papers (candidate: RELATED_MACHINE).
- **Shared ids where this fragment's text wins in the merge** (it sorts first): SRC_ARXIV_2206_00037 set to
  RELATED_MACHINE (matches lhmuc-primary and mulhc-mutristan; journal here said SECONDARY_SOURCE);
  SRC_ARXIV_2203_06258 set to CONFERENCE_PROCEEDING via the lead's Snowmass rule, relying on the
  mulhc-mutristan identification (lhmuc-primary uses RELATED_MACHINE — lead to confirm); SRC_ARXIV_2101_10476
  set to PEER_REVIEWED with DOI 10.1103/PhysRevD.103.116009 taken from the mulhc-mutristan fragment, not from
  this family's snippets.
- **Access-mode ambiguity:** the journal's closing note names only four unresolvable hosts, yet marks every
  arXiv/Indico/JACoW entry "fetch blocked". Those were recorded as `blocked`; if the lead prefers
  `pending_fetch` for entries whose failed fetch is not explicitly logged, change them in
  `lhc-hl-lhc-protons_sources.yaml` (ids listed in the Fetch backlog).
- **Query → source map is inferred**: the journal has no explicit mapping; `discovered_by_queries` and the CSV
  pair rows were built only where a query note names the source (identifier, title or a value unique to it).
  arXiv:1409.5821 could not be attributed and carries "(see family queries)".
- **Four planned queries never ran** (WebSearch budget): MOPAB005 details; INSPIRE record of the LHC Design
  Report; 2025 O/Ne run numbers; TDR 2020 table string search. They are logged with `tool = "WebSearch (not
  executed)"` in the CSV and should be re-run.

### Fetch backlog

Once network access is allowed, fetch each URL, archive it under `references/` with SHA-256 and
`research/archived_metadata/`, set `access: fetched`, and extract the items listed with page/table and verbatim
quotation. Priority order: 1-4 first (they fix the proton baseline), then ions, then context.

1. `https://e-publishing.cern.ch/index.php/CYRM/article/download/1154/959` (HL-LHC TDR 2020, Appendix A;
   issue page `https://e-publishing.cern.ch/index.php/CYRM/issue/view/127`, Chapter 2
   `.../article/download/1153/967`) — SRC_URL_CERN_2020_010_HLLHC_TDR. Extract Table A-3 (and Chapter 2
   Table 2-1): beam energy, Nb (standard/BCMS), nb (2760/2744), bunch spacing, εn, β* IP1/5, σz, revolution
   frequency, circumference, RF frequency/harmonic, peak and levelled luminosity, crossing angle, crab-cavity
   factors (0.369/0.715); licence statement; confirm or drop the "v1.0" label.
2. `https://dx.doi.org/10.5170/CERN-2004-003-V-1` (LHC Design Report Vol. 1) —
   SRC_DOI_10_5170_CERN_2004_003_V_1. Extract Chapter 2 nominal parameter table (7 TeV, 1.15e11, 2808, 3.75 µm,
   11245 Hz, 26658.9 m, β* 0.55 m, 400.8 MHz, h = 35640) and the CC-BY-3.0 statement.
3. `https://e-publishing.cern.ch/index.php/CYRM/issue/download/40/11` (HL-LHC TDR V0.1, 2017; arXiv mirrors
   1705.08830 / 1705.09447) — SRC_URL_CERN_2017_007_M_HLLHC_TDR_V0_1. Extract the parameter table (2748/2604
   bunches) to document the 2017→2020 change; CC-BY-4.0 statement.
4. `https://arxiv.org/abs/2610.35154` — SRC_ARXIV_2610_35154 (already uploaded). Only read the abstract page for
   licence metadata and author list; resolve ref. [24] (fewer bunches → higher population) from the PDF.
5. `https://jinst.sissa.it/LHC/LHCmachine/2008_JINST_3_S08001.pdf` — SRC_URL_JINST_2008_3_S08001_LHC_MACHINE.
   Extract Chapter 2 nominal parameter table and DOI; cross-check against item 2.
6. `https://arxiv.org/pdf/2206.00037` — SRC_ARXIV_2206_00037. Extract author list, Table 15 (HL-LHC proton
   parameters as used in μp proposals) and the companion table (2.5 µm / β* 0.15 m); μp √s values
   4.58/6.48/9.16 TeV; which HL-LHC document each table cites.
7. `https://arxiv.org/pdf/2505.03535` — SRC_ARXIV_2505_03535. Extract authors, venue (decide category) and the
   nominal/achieved/HL-LHC/ultimate comparison table (2748 bunches, 5e34).
8. `https://arxiv.org/pdf/2505.00947` — SRC_ARXIV_2505_00947. Extract the HL-LHC vs nominal p/b statement with
   its TDR citation and the Run 3 injector table (2.8e11 p/b at 50 ns vs LIU 2.0e11): where measured, which
   machine.
9. `https://arxiv.org/pdf/1412.7857` — SRC_ARXIV_1412_7857. Extract authors/venue and the beam-variant table
   (8b+4e: ~2.3e11 p/b, 1900 bunches; 50 ns and 25 ns variants).
10. `https://arxiv.org/pdf/1409.5821` — SRC_ARXIV_1409_5821. Extract authors/venue (decide category) and any
    SPS 200 MHz RF upgrade intensity limits relevant to higher-population bunches.
11. `https://epaper.kek.jp/ipac2018/papers/thpaf053.pdf` — SRC_JACOW_IPAC2018_THPAF053. Confirm title/authors;
    extract statements on 200 MHz slip-stacking, 80 MHz capture RF, compact 200 MHz LHC RF and intensity
    limits; verify which statements belong to this paper.
12. `https://arxiv.org/abs/2506.15445` — SRC_ARXIV_2506_15445 (already uploaded). Abstract page only: licence,
    v2 comment text; locate the "250 ns, one in ten 25 ns proton bunches" statement in the uploaded PDF with
    page number.
13. `https://ar5iv.labs.arxiv.org/html/2107.09560` (or arXiv:2107.09560) — SRC_ARXIV_2107_09560. Extract Table 1
    (Pb design / 2018 achieved / Run 3-HL-LHC: bunches, spacing, ions per bunch, emittance, stored energy) with
    verified column alignment; confirm EPJ Plus reference.
14. `https://arxiv.org/pdf/2304.03628` — SRC_ARXIV_2304_03628. Extract authors, venue, Pb run parameter table
    (6.8 Z TeV Run 3, 7 Z TeV Run 4, 2.2e11 Pb82+/beam target).
15. `https://arxiv.org/html/2508.19653v3` — SRC_ARXIV_2508_19653. Extract authors, venue and the species table
    (Pb, Xe, O, Ne, …: energy per nucleon, ions per bunch, bunches, luminosities).
16. `https://epaper.kek.jp/ipac2018/papers/mopmf039.pdf` — SRC_JACOW_IPAC2018_MOPMF039. Extract Fill 6295 Xe-Xe
    table (6.5 Z TeV, 20 bunches, ~3e11 charges, β* (0.3, 10, 3) m, colliding bunches (8, 16, 8)) plus Xe
    ions per bunch and emittance.
17. `https://refs.jacow.org/reference/show/106501` → `https://jacow.org/ipac2021/papers/MOPAB005.pdf` —
    SRC_JACOW_IPAC2021_MOPAB005. Extract oxygen pilot-run beam parameters (O ions per bunch, bunches, energy,
    p-O/O-O luminosity).
18. `https://indico.jacow.org/event/95/papers/13011/files/6586-MOP1054.pdf` — SRC_JACOW_IPAC2026_MOP1054.
    Extract Table 2 (p-O, O-O, Ne-Ne energies, intensities, bunch numbers, optics) and the companion THP4085
    reference (register it if useful).
19. `https://indico.cern.ch/event/663598/contributions/2782520/attachments/1561185/2669656/Paper-HeavyIonRun2018.pdf`
    — SRC_INDICO_663598_2782520. Extract 2018 Pb-Pb optics, bunch parameters and luminosity estimates.
20. `https://epaper.kek.jp/ipac2019/papers/weyyplm2.pdf` — SRC_JACOW_IPAC2019_WEYYPLM2. Extract the achieved 2018
    Pb parameters vs HL-LHC targets table.
21. `https://proceedings.jacow.org/ipac2018/export/TUXGBD2-bib.htm` → paper PDF — SRC_JACOW_IPAC2018_TUXGBD2.
    Extract the heavy-ion operation overview table (Pb and Xe runs through 2018).
22. `https://pdg.web.cern.ch/2020/reviews/rpp2020-rev-hep-collider-params.pdf` and the 2024/2025 editions on
    pdg.lbl.gov — SRC_URL_PDG_2020_REV_HEP_COLLIDER_PARAMS. Extract LHC and HL-LHC columns (energy, luminosity,
    bunches, particles per bunch, β*, emittance, bunch length) as a cross-check only.
23. `https://accelconf.web.cern.ch/IPAC2012/papers/moppc005.pdf` — SRC_JACOW_IPAC2012_MOPPC005. Extract authors
    and the 25 ns / 50 ns parameter table (2.2e11, 2808, β* 0.15 m, 2.5 µm) as a historical lead.
24. `https://arxiv.org/pdf/2005.04520` — SRC_ARXIV_2005_04520. Extract venue (decide category) and the β*
    15 cm vs 25 cm statement with page.
25. `https://LHC-MACHINE-OUTREACH.web.cern.ch/lhc-vital-statistics.htm` —
    SRC_URL_LHC_MACHINE_OUTREACH_VITAL_STATISTICS. Record page date/version; cross-check 26,659 m / 11.2455 kHz
    against item 2 (never cite as a parameter source).
26. `https://lhc-closer.es/taking_a_closer_look_at_lhc/1.lhc_parameters` — SRC_URL_LHC_CLOSER_ES_LHC_PARAMETERS.
    Identify the "design-era document" it reproduces (26658.87 m, 11.24551 kHz, 400.8 MHz, h = 35640, 2835
    bunches) and register that document instead.
27. `https://arxiv.org/pdf/1905.05564` — SRC_ARXIV_1905_05564. Extract authors, venue and the HL-LHC/HE-LHC
    proton parameter table used for the μp designs (√s 4.58-12.7 TeV).
28. `https://arxiv.org/pdf/1807.09867` — SRC_ARXIV_1807_09867. Extract authors, venue and the LHC proton
    parameters assumed for the LHC-based μp options.
29. `https://arxiv.org/pdf/2203.06258` — SRC_ARXIV_2203_06258. Confirm Snowmass 2021 status / JINST publication,
    author list, and the LHC-based "Large Hadron-Muon Collider" parameters (7 TeV p, 1.5 TeV μ, ~6.5 TeV √s).
30. `https://arxiv.org/pdf/2101.10476` — SRC_ARXIV_2101_10476. Confirm PRD 103 116009 and the 1 TeV μ × 7 TeV p,
    0.1 ab⁻¹ benchmark (physics_programme context).

Re-run after fetching: the four unexecuted queries (see above), plus a search for the Zimmermann SPS/LHC
modification note by title and for the IPAC'26 THP4085 injector paper.

---

## Family `lhec-erl` (from `research/_fragments/lhec-erl_unresolved.md`)

### Unresolved items — reconnaissance family `lhec-erl`

Searches run 2026-10-28 with WebSearch only (19 queries, 23 sources surfaced). WebFetch attempts failed
(`DNS not resolved`) on arxiv.org, ar5iv.labs.arxiv.org, indico.cern.ch, iopscience.iop.org, jacow.org and
epjc.epj.org. Six URLs on other hosts (atrium.in2p3.fr, hal.archives-ouvertes.fr, accelconf.web.cern.ch ×2,
infoscience.epfl.ch, indico.fis.agh.edu.pl) were never fetched (journal `fetch_blocked=false`, no page read),
so they are `snippet_only`. Everything below is therefore snippet-level evidence: it may not back a
`reported_lhmuc` status and is capped at confidence `medium` (CLAUDE.md §1.5). Nothing in this file is a
parameter record; every LHeC/ERL/PERLE number is at best `imported_related` or `analogous` once verified.

### Unresolved items

- **No full text of any LHeC document was read.** All ERL (two ~1 km linacs, 10 GeV/pass, three arcs, 100 MW
  cap, ~50 GeV, 8.1 GV per linac, 5.332 km) and IR (L* = 15 m, β* = 10 cm / 7 cm, Q1A 252 T/m, Q1B 164 T/m,
  0.3 T × 9 m separator) values come from search snippets and must be re-read in the source tables
  (arXiv:2007.14491 and arXiv:2206.07678) with page numbers and verbatim quotations before they become
  `imported_related` parameter records.
- **Journal has no query→source map.** `discovered_by_queries` in `lhec-erl_sources.yaml` was inferred from
  the per-query notes (only where a note names the source's identifier or a value unique to it); three
  sources (arXiv:1211.5102, IPAC2011 TUPC054, arXiv:2506.15445) could not be attributed and carry
  "(see family queries)".
- **New J. Phys. reference for André, Holzer, Forthomme, Piotrzkowski (arXiv:2503.20475)**: snippets confirm
  only "published in New Journal of Physics", received 31 Mar 2025, revised 24 Oct 2025, published
  31 Dec 2025. Volume 28 / article 013001 and the publisher DOI (10.1088/1367-2630/…) are NOT confirmed.
  Category PEER_REVIEWED therefore rests on snippet text only.
- **Peer-review status of arXiv:2206.07678 ("An Energy Recovery Linac for the LHeC")**: the journal
  classified it PEER_REVIEWED, but snippets show only an arXiv preprint (the ERL chapter of the LHeC
  report); no journal reference appeared. Kept as the journal classified it pending a lead decision
  (candidate: CONFERENCE_PROCEEDING or UNVERIFIED). Author list also unconfirmed.
- **LHeC-at-HL-LHC proton beam parameter table not retrieved verbatim.** "2760 bunches" did not appear in
  any snippet (the only "2760" hit was the Pb energy per nucleon, 2760 GeV); normalised emittance 2.5 µm was
  not found (snippets give 3.75 µm baseline and 2 µm upgrade, Pellegrini talk); 2.2e11 protons per bunch
  (CDR 2012 / Pellegrini talk) and β*_p = 7 cm (arXiv:1802.04317, a secondary source) were confirmed only via
  snippets. The table in arXiv:2007.14491 must be read directly.
- **Separator dipole field for the 50 GeV / L* = 15 m IR (2020 design)** not found; only the 2012 CDR value
  (0.3 T over 9 m → 7 cm separation at Q1) and the 2025 head-on scheme (no separator at all) were seen.
- **Crossing-angle evolution — four distinct values, not to be averaged (CLAUDE.md §1.6)**: 6 mrad
  (IPAC2011 THPZ016), 6.8 mrad (IPAC2014 TUPRO070), 7 mrad "for both proton beams" (DIS2022 André slides,
  2020/2022 design), head-on / no crossing angle (arXiv:2503.20475, 2025 phase-one design). Which geometry
  the LHμC IR would inherit is not stated anywhere seen; needs full-text reconciliation and, if kept,
  separate IR scenarios.
- **Q1 design evolution**: 2011 half-quadrupole Q1 with 175 T/m and 25 T/m electron fringe (THPZ016) →
  2020 "old half-quadrupole" with a 4.45 T dipole component rejected, replaced by Q1A 252 T/m / 3.5 m /
  20 mm and Q1B 164 T/m / 3.0 m / 32 mm (arXiv:2007.14491) → 2025: "only Q1 of the proton lattice
  replaced", electron quads ~20 T/m × 1.8 m (arXiv:2503.20475). Values are snippets; apertures, L* and
  gradients for a muon beam (no synchrotron-radiation constraint, large emittance) are not addressed by any
  LHeC source.
- **ERL wall-plug power budget**: 100 MW cap stated by arXiv:1211.5102 ("about half of CERN's maximum
  site power") and arXiv:2206.07678; IPAC2022 WEOXGD2 gives SR loss 45 MW → 27 MW at 20 mA with FFA arcs;
  a "2013 cryogenic estimate ~21 MW" appeared in a query note but could not be attributed to a source. The
  power breakdown table itself was not seen.
- **20 GeV single-pass phase-one ERL (Run 5, Point 2, after LS4, 2036 target)**: confirmed only by snippets
  from arXiv:2503.20475, the ESPP briefing book (arXiv:2511.03883), Indico 1439855/6461558 and the
  Piotrzkowski AGH talk of 22 Nov 2024. Whether the LHμC booster/main ring assumes the 20 GeV phase-one
  ERL or the full 50 GeV three-turn ERL is not stated in any snippet; must be checked against the uploaded
  arXiv:2610.35154 and arXiv:2506.15445 texts.
- **PERLE (PRAB 27, 031603 (2024))**: no arXiv identifier confirmed; licence (PRAB CC BY) not confirmed;
  author list of the 2019 HAL record (hal-02283606 / IPAC2019 TUPGW008) not confirmed.
- **arXiv:2503.17727 (LHeC bridge project)**: PoS 485/583 "The LHeC collider as a bridge between major
  colliders at CERN" appeared as a conference version, but its author list and date were not confirmed.
  Category corrected by the lead to RELATED_MACHINE (the journal had PRIMARY_LHMUC).
- **INSPIRE-HEP**: `site:inspirehep.net` queries returned no literature records; citation counts and
  record ids remain unverified for every source in this family.
- **Pellegrini LHeC parameter talk (Indico 353906 / 2278712)**: date, event name and the exact table
  context (which LHeC design year the 0.1 → 0.05 m β* and 3.75 → 2 µm emittance refer to) not visible.
- **Indico 1439855 / 6461558**: speaker, event name and date (2024 or 2025) not confirmed.
- **Licences**: only arXiv:2007.14491 (CC BY 4.0, repository record) and arXiv:2201.02436 (CC BY 4.0)
  have a licence confirmed by snippets; all others are "arXiv open access" / "JACoW open access" /
  "public indico attachment" claims from snippets, to be checked on fetch before any archiving.

### Fetch backlog (once network access is allowed)

Each item: URL → what to extract (page, table/figure, verbatim quotation) and what it unblocks.

- https://arxiv.org/abs/2007.14491 (and PDF) → abstract page: version list, licence; PDF: the LHeC/HL-LHC
  luminosity parameter table (electron current 15/25 mA, β* 10/7 cm, proton bunch population, bunch
  number, normalised emittance, peak luminosity 0.5e34), the ERL parameter table, the IR table with Q1A/Q1B
  (252/164 T/m, 3.5/3.0 m, 20/32 mm), L* = 15 m, separator field, crossing angle. Unblocks the proton-side
  `imported_related` records and the ERL-reuse geometry.
- https://arxiv.org/abs/2206.07678 (and PDF) → author list (check peer-review status), ERL parameter table
  (8.1 GV per linac, 49.2 GeV, 5.332 km total length, 20 mA, 6× linac current), the 100 MW wall-plug budget
  breakdown (RF, cryogenics, SR). Unblocks ERL dimensioning and the category decision.
- https://arxiv.org/abs/1206.2913 (and PDF; DOI 10.1088/0954-3899/39/7/075001) → CDR IR chapter: β* 0.1 m,
  separator 0.3 T × 9 m, 7 cm separation at Q1, 48 kW IR SR; CDR ERL chapter: two 10 GeV linacs, 60 GeV,
  triple return arcs. Confirms the 2012 baseline against which later changes are tracked.
- https://arxiv.org/abs/2503.20475 (and PDF) → version list; NJP volume/article/DOI; phase-one ERL
  parameters (20 GeV, 60 mA, circumference one-third LHC), head-on IR, electron quads ~20 T/m × 1.8 m,
  "only Q1 replaced"; Run 5 schedule. Unblocks the staged LHeC scenario the LHμC reuse case relies on.
- https://arxiv.org/abs/2503.17727 (v3) → author list (F. Ahmadova + 41), PoS 485/583 cross-reference,
  1 ab⁻¹ in 6 years, 50 GeV ERL, HL-LHC end ~2041 timing; FCC-ee injector reuse statement.
- https://arxiv.org/abs/2201.02436 (DOI 10.1140/epjc/s10052-021-09967-z) → detector envelope (tracker
  radius, forward-backward symmetrised option), common eh/hh IR concept; licence CC BY 4.0 confirmation.
- https://arxiv.org/abs/1211.5102 → venue (which 2012 symposium/proceedings), the 100 MW cap statement and
  power-budget composition quotation with page.
- https://arxiv.org/abs/2207.02095 → authors; LHeC IR description with L* = 15 m and 106 mm electron
  aperture distance (page, figure).
- https://arxiv.org/abs/1802.04317 → authors; the "β_p = 7 cm" statement with page.
- https://arxiv.org/abs/2511.03883 (ESPP 2026 Physics Briefing Book) → page and quotation for the phased
  LHeC approach (20 GeV single-pass ERL without spreader/recombiner); any LHμC/muon-hadron mention.
- https://arxiv.org/abs/2506.15445 → abstract page only (licence, version list) — the PDF is already
  uploaded and registered; do not re-import parameters from the web view.
- https://jacow.org/ipac2021/papers/WEPAB001.pdf (DOI 10.18429/JACoW-IPAC2021-WEPAB001) → ERL and IR
  summary numbers by the core design team; licence (JACoW CC BY 3.0).
- https://accelconf.web.cern.ch/IPAC2011/papers/thpz016.pdf (+ companion WEPZ013) → 6 mrad crossing angle,
  Q1 175 T/m and 25 T/m fringe table, half-quadrupole design; author list.
- https://jacow.org/IPAC2014/papers/TUPRO070.pdf → 6.8 mrad crossing angle, D1 ×3.43 / D2 ×1.21 scaling;
  author list.
- https://accelconf.web.cern.ch/IPAC2011/papers/tupc054.pdf → 1 km linacs, 10 GeV/pass, 1 km-radius arcs;
  author list.
- https://jacow.org/IPAC2022/papers/WEOXGD2.pdf → FFA single-arc proposal; SR loss 45 MW → 27 MW at 20 mA;
  author list (Bogacz et al. per snippet).
- https://indico.cern.ch/event/1072533/contributions/4787015/attachments/2437656/4175192/DIS2022%20-%20LHeC%20.pdf
  → slide numbers for L* = 15 m, β* = 10 cm, 7 mrad crossing angle (LHeC) vs L* = 23 m, β* = 30 cm (FCC-eh).
- https://indico.cern.ch/event/353906/contributions/2278712/attachments/1331132/2000523/6_Pellegrini_LHeC.pdf
  → talk date/event; proton parameter slide (2.2e11 p/bunch, 25 ns, emittance 3.75 → 2 µm, β* 0.1 → 0.05 m).
- https://indico.cern.ch/event/1439855/contributions/6461558 → speaker, date, abstract/slides for the 20 GeV
  ERL at P2 after LS4 (Run 5).
- https://indico.fis.agh.edu.pl/event/302/attachments/431/768/22112024-KrzysztofPiotrzkowski-LHeC.pdf →
  slide with the 2036 target, 20 GeV at IP2, 0.75 TeV ep/eA; any early LHμC/muon mention (proponent is the
  LHμC author).
- https://atrium.in2p3.fr/nuxeo/nxfile/default/ea0a643f-523c-4951-b203-1716b48749bd/blobholder:0/PhysRevAccelBeams.27_2024_031603.pdf
  (or https://doi.org/10.1103/PhysRevAccelBeams.27.031603, HAL hal-04523882v1) → PERLE parameter table
  (500 MeV, 7 MeV injection, 82.2 MeV per linac, 20 mA, 120 mA cavity load, 500 pC, 801.58 MHz); licence;
  arXiv id if any.
- https://hal.archives-ouvertes.fr/hal-02283606 → author list, IPAC2019 TUPGW008 cross-reference, PERLE
  500 MeV / 20 mA / 801.6 MHz statement.
- https://infoscience.epfl.ch/record/216397?ln=en → PRSTAB 2015 volume/article/DOI for Pellegrini, Latina,
  Schulte, Bogacz; beam-beam and multi-turn stability parameters of the 60 GeV ERL.
- INSPIRE-HEP (https://inspirehep.net) → literature records and citation metadata for every arXiv id above.

---

## Family `vffa-acceleration` (from `research/_fragments/vffa-acceleration_unresolved.md`)

### Unresolved items — reconnaissance family `vffa-acceleration`

Searches run 2026-10-28 with WebSearch only (17 queries, 34 sources surfaced). WebFetch attempts failed on ora.ox.ac.uk, arxiv.org, jacow.org and zgoubi.sourceforge.io (hosts not resolvable under network policy); four sources are therefore `blocked` (`SRC_URL_ORA_OXFORD_TOPP_MUGGLESTONE_THESIS`, `SRC_ARXIV_2011_10783`, `SRC_JACOW_IPAC2021_THPAB124`, `SRC_DOI_10_1038_NPHYS2179`) and the other 30 were never fetched (`snippet_only`). Everything below is snippet-level evidence, in several cases the search tool's paraphrase rather than verbatim text. It may not back a `reported_lhmuc` status and is capped at confidence `medium` (CLAUDE.md §1.5). Nothing in this file or in `vffa-acceleration_sources.yaml` is a parameter record; vFFA/RCS/FFAG numbers are at best `imported_related` or `analogous` once verified against the primary text, and none of them describes the LHμC itself (no PRIMARY_LHMUC source appeared in this family).

### Unresolved items

- **Journal-level items (verbatim from the reconnaissance journal):**
  - All WebFetch attempts failed (ora.ox.ac.uk, arxiv.org, jacow.org, zgoubi.sourceforge.io not resolvable under network policy); every parameter above is quoted from WebSearch summary text, not from the primary document, and several quotes are the search tool's paraphrase rather than guaranteed verbatim page text.
  - Topp-Mugglestone thesis: license/access status, DOI, and any field/energy numbers for the muon-collider vFFA stage not confirmed; full abstract not retrieved.
  - Exact title of IPAC'21 THPAB124 (Machida, Lagrange, Topp-Mugglestone) not confirmed.
  - Whether the DESY 12-16 May 2025 vFFA poster (contribution 185344) is the IPAC'25 contribution, and whether a JACoW IPAC'25 paper exists with lattice numbers (energy range, field, circumference), is unresolved.
  - Journal publication status of arXiv:2011.10783 (PRAB?) not confirmed.
  - EMMA machine parameters reported in the search summary (circumference ~16.57 m, 42 cells, 19 RF cavities ~1.3 GHz, 40 pC bunch) could not be attributed to a specific URL and were therefore not recorded as quoted parameters.
  - inspirehep file 7bcd989a5066031ea54b234875d49d90 (IMCC parameter table) and 12757f301a5c0c862f7d1fb682c39776 (ISIS-II FFA options): titles, authors and dates unknown.
  - IPAC MOP1094 hybrid RCS paper: title, authors and conference year unknown.
  - No source found giving a vFFA muon ring's explicit energy range in GeV/TeV; only 'footprints comparable to RCS1 and RCS4' and the 63 GeV to 5 TeV RCS range.
  - Brooks IPAC'22 MOPOTK036 appeared in results but was not characterised; Brooks BNL 2023 FFA workshop talk (indico.bnl.gov event 17880) on permanent-magnet/electromagnet nonlinear FFA fields not characterised beyond title.
  - No power-efficiency figures for vFFA vs RCS found in snippets.
- **Query→source map is inferred.** The journal has no explicit map; `discovered_by_queries` was inferred from per-query notes that name a source's identifier or a value unique to it. `SRC_ARXIV_2607_16904` (UNK-site muon collider review) could not be attributed to any query.
- **Category decisions needing lead confirmation:** `SRC_ARXIV_2011_10783` kept as the journal's PEER_REVIEWED although only an arXiv preprint was seen and the journal reference is unconfirmed; `SRC_URL_INSPIRE_FILE_7BCD989A_IMCC_ACCEL_CHAIN` recorded as UNVERIFIED (journal: RELATED_MACHINE but 'UNVERIFIED-adjacent'); `SRC_URL_INSPIRE_FILE_12757F30_ISIS2_FFA_OPTIONS` kept as ANALOGOUS_TECHNOLOGY although title/authors are unknown; `SRC_INDICO_1553599_6692118` moved from OFFICIAL_CERN to CONFERENCE_PROCEEDING per the lead's slide-deck rule; `SRC_INDICO_STFC_487_3908` and `SRC_URL_BNL_MUTAC_2009_BERG_IDSNF_ACCELERATION` likewise moved to CONFERENCE_PROCEEDING/workshop_talk; `SRC_ARXIV_2203_07919` (Snowmass FFA report) moved to CONFERENCE_PROCEEDING.
- **Leads named in query notes but not characterised as sources (NOT added, per instructions):** Oxford staff page for Topp-Mugglestone (Q1); an IPAC'23 companion paper (Q1); IPAC2022 MOPOTK036 (Q10, 'not characterised'); Brooks BNL 2023 FFA workshop talk, indico.bnl.gov event 17880 (Q7); CYCLOTRONS2022 MOBI01 companion of the Snowmass report (Q16); PAC'07 THOBAB01 and the STFC ASTeC EMMA page (bundled into `SRC_JACOW_EPAC2008_THPP004`). Each needs its own registry entry once read.
- **Paraphrase vs quotation.** Several 'snippet-quoted' strings are visibly the search tool's prose (e.g. 'which works out to about 4 kT/s', 'Berg lists the energy bands as …', 'A table of the acceleration chain lists …'); they must be replaced by verbatim text with page/table references before any provenance record cites them.
- **Relevance to LHμC is indirect.** The family documents the vFFA/RCS acceleration options studied for the IMCC muon collider and the ISIS-II proton driver. Whether the LHμC concept (ultra-cold μ+, SPS/LHC reuse) foresees a vFFA stage at all is not established by any source here; the Kraków workshop Topp-Mugglestone contribution (family lhmuc-primary) was not found. No LHμC-specific acceleration-chain number exists in this family.
- **No vFFA muon ring energy range, circumference, RF frequency, number of turns, or power-efficiency figure was found** — only 'footprints comparable to RCS1 and RCS4', the 63 GeV → 5 TeV RCS range, the < 120 mm excursion and the < 8 T / < 16 T on-orbit field limits (arXiv:2504.21417, snippet).
- **vFFA readiness caveat to carry forward:** per `SRC_INDICO_STFC_487_3908` (snippet) the ISIS-II baseline moved from vFFA to a horizontal DF-spiral FFA in 2022 citing superconducting-magnet development; per `SRC_INDICO_DESY_45968_185344` (snippet) transverse-optics and longitudinal-stability simulations of the muon vFFA were still pending in May 2025. No vFFA has ever been built (Snowmass report, snippet).

### Fetch backlog (once network access is allowed)

- `SRC_URL_ORA_OXFORD_TOPP_MUGGLESTONE_THESIS` (blocked) — https://ora.ox.ac.uk/objects/uuid:f15ec97f-3d72-440f-82df-5d158d3e8358 — extract: ORA record and PDF /files/d5999n419f: licence, DOI, abstract, chapter on the muon-collider vFFA stage (energy range, field, excursion, circumference, turn count), optimisation results; page numbers for every quoted number.
- `SRC_ARXIV_2011_10783` (blocked) — https://arxiv.org/abs/2011.10783 — extract: abstract page: journal reference and DOI (PRAB?), version/date; full text: vFFA field law B ∝ exp(k y), tune/momentum-compaction statements, maximum-field driver (end fields), muon-collider motivation.
- `SRC_DOI_10_1103_PHYSREVSTAB_16_084001` (snippet_only) — https://epubs.stfc.ac.uk/manifestation/9731/PhysRevSTAB.16.084001.pdf — extract: verbatim abstract (12 GeV ring, ≥ 2.18 MW), licence (CC-BY?), lattice parameters of the 3/5/12 GeV ISIS-upgrade rings, tracking results, energy-recovery electron remark.
- `SRC_JACOW_IPAC2012_MOPPD019` (snippet_only) — https://refs.jacow.org/reference/show/3920 — extract: paper PDF jacow.org/IPAC2012/papers/MOPPD019.pdf: edge-focusing concept, ring energies 3/5/12 GeV, circumferences, fields; confirm paper code.
- `SRC_JACOW_HB2012_MOP255` (snippet_only) — https://epaper.kek.jp/HB2012/papers/mop255.pdf — extract: injection energy 800 MeV, field-with-height law, acceleration scheme (RF frequency fixed?).
- `SRC_INDICO_PSI_7313_19980` (snippet_only) — https://indico.psi.ch/event/7313/contributions/19980/ — extract: FFA'19 slides: permanent-magnet vFFA prototype measurements, 18 GeV electron lattice in RHIC tunnel (circumference, field, excursion).
- `SRC_JACOW_IPAC2014_TUYB01` (snippet_only) — https://refs.jacow.org/author/show/539400 — extract: invited overview: confirm title, abstract, any tabulated V-FFAG parameters.
- `SRC_JACOW_IPAC2021_THPAB236` (snippet_only) — https://epaper.kek.jp/ipac2021/papers/thpab236.pdf — extract: confirm DOI/pages; analytic vFFA model assumptions (linearised Hamiltonian), validity range, comparison with tracking.
- `SRC_JACOW_IPAC2021_THPAB124` (blocked) — https://jacow.org/ipac2021/papers/THPAB124.pdf — extract: confirm exact title; muon-collider vFFA concept: isochronous acceleration, fixed RF frequency, skew-quadrupole collider arc; any energies/fields/circumferences.
- `SRC_INDICO_DESY_45968_185344` (snippet_only) — https://indico.desy.de/event/45968/contributions/185344 — extract: poster/abstract: confirm whether it is the IPAC'25 contribution and whether a JACoW paper exists; RCS1/RCS4-equivalent vFFA footprints (circumference, field, excursion), argument on ramp rate / power efficiency / time-of-flight; status of optics and longitudinal simulations.
- `SRC_INDICO_1553599_6692118` (snippet_only) — https://indico.cern.ch/event/1553599/contributions/6692118/attachments/3137263/5567034/20250917-muon-ffa.pdf — extract: slides 20250917-muon-ffa.pdf: event and contribution titles, speaker; the 4.2 kT/s RCS1 ramp-rate slide, the 63 GeV → 5 TeV / 50 % survival / ms cycle-time statement, FFA collider-ring idea.
- `SRC_INDICO_STFC_927_5619` (snippet_only) — https://indico.stfc.ac.uk/event/927/contributions/5619/attachments/1909/3359/Muons_meeting_11-24.pdf — extract: Muons_meeting_11-24.pdf: date, speakers, the RCS-vs-vFFA comparison table (565 T/s vs 0; 10 cm vs 1.3 cm; any other rows such as energy, circumference, magnet type).
- `SRC_ARXIV_2504_21417` (snippet_only) — https://arxiv.org/abs/2504.21417 — extract: section on FFAs: verbatim passage with page/figure numbers for '< 120 mm', '< 8 T', '< 16 T', fully-coupled optics statement; RCS parameter tables for comparison.
- `SRC_ARXIV_2303_08533` (snippet_only) — https://arxiv.org/abs/2303.08533 — extract: journal reference (EPJC); acceleration-chain table: 63 GeV linac, RCS energies 0.31/0.75/1.5/5 TeV, circumferences 5990/5990/10700/35000 m, hybrid-bending statement, FFA remark.
- `SRC_ARXIV_2407_12450` (snippet_only) — https://arxiv.org/abs/2407.12450 — extract: RCS1 NC dipole specification 0.36 → 1.8 T in 0.35 ms with table/page reference.
- `SRC_URL_INSPIRE_FILE_7BCD989A_IMCC_ACCEL_CHAIN` (snippet_only) — https://inspirehep.net/files/7bcd989a5066031ea54b234875d49d90 — extract: identify title, authors, date, venue; the ramp-rate table (4200/3282/1519/565 T/s), −1.8 → +1.8 T swing, 16 T collider dipole; then re-categorise.
- `SRC_URL_INDICO_JACOW_95_MOP1094` (snippet_only) — https://indico.jacow.org/event/95/papers/13703/files/6332-MOP1094.pdf — extract: identify title, authors, conference year; hybrid RCS description and any parameters.
- `SRC_JACOW_PAC2009_WE6PFP097` (snippet_only) — https://accelconf.web.cern.ch/PAC2009/papers/we6pfp097.pdf — extract: authors; NC dipole swing −1.8 → 1.8 T in 1 ms (3700 T/s) with context.
- `SRC_ARXIV_1811_10694` (snippet_only) — https://arxiv.org/abs/1811.10694 — extract: authors; RLA with multi-pass (5–20 turn) NS-FFAG arcs in the LHC tunnel: energies, circumference, fields — the closest precedent for a TeV muon machine in the LHC tunnel.
- `SRC_ARXIV_2412_00463` (snippet_only) — https://arxiv.org/abs/2412.00463 — extract: authors; Q_s ≈ 0.5 statement, RF voltage per turn, number of RF stations.
- `SRC_JACOW_NAPAC2025_BERG_RCS_CHAIN` (snippet_only) — https://epaper.kek.jp/napac2025/institute/jsberg-bnl-gov-j-berg/index.html — extract: paper code and PDF; ring circumferences 6.28–15.5 km, 63 GeV injection, ramp rates.
- `SRC_DOI_10_1038_NPHYS2179` (blocked) — https://link.springer.com/article/10.1038/nphys2179 — extract: abstract (10–20 MeV; 12–18 MeV/c within 10 mm); machine parameters (circumference, cell count, RF frequency, bunch charge) to attribute the unsourced EMMA numbers; licence.
- `SRC_JACOW_EPAC2008_THPP004` (snippet_only) — https://jacow.org/e08/papers/THPP004.pdf — extract: EMMA design parameters with table reference; split PAC'07 THOBAB01 and the STFC ASTeC page into their own entries.
- `SRC_URL_INSPIRE_FILE_12757F30_ISIS2_FFA_OPTIONS` (snippet_only) — https://inspirehep.net/files/12757f301a5c0c862f7d1fb682c39776 — extract: identify title, authors, date; confirm '25 cells × 6 m' vFFA driver and '25 m / 10 cells' prototype; vFFA-vs-DF-spiral comparison.
- `SRC_JACOW_IPAC2021_TUPAB208` (snippet_only) — https://epaper.kek.jp/ipac2021/papers/tupab208.pdf — extract: FETS-FFA injection: 5 of 10 cells, painting scheme, ring parameters.
- `SRC_INDICO_STFC_487_3908` (snippet_only) — https://indico.stfc.ac.uk/event/487/contributions/3908/attachments/1340/2416/machida20220929_v3.2.pdf — extract: machida20220929_v3.2.pdf: baseline change vFFA → DF-spiral, stated reasons (SC magnet development), timeline, prototype radius ~4 m.
- `SRC_URL_PASJ2023_WEOB3` (snippet_only) — https://ibic12.kek.jp/mirror/www.pasj.jp/web_publish/pasj2023/proceedings/PDF/WEOB/WEOB3.pdf — extract: original PASJ URL; ISIS-II options status 2023; FETS-FFA testbed parameters.
- `SRC_ARXIV_2203_07919` (snippet_only) — https://arxiv.org/abs/2203.07919 — extract: vFFA prototype passage (3 → 12 MeV, 0.53 m excursion) with page; 'no viable high-power solution' statement; CYCLOTRONS2022 MOBI01 companion.
- `SRC_URL_OSTI_984419` (snippet_only) — https://www.osti.gov/biblio/984419 — extract: OSTI record: title, authors, report number; '~4 turns in an RLA' statement context.
- `SRC_URL_BNL_MUTAC_2009_BERG_IDSNF_ACCELERATION` (snippet_only) — https://www.cap.bnl.gov/mumu/conf/MUTAC-090406/talks/JSBerg1-090406.pdf — extract: slides: IDS-NF chain energy bands (0.9 / 3.6 / 12.6 / 25 GeV) verbatim.
- `SRC_JACOW_IPAC2011_MOPZ007` (snippet_only) — https://accelconf.web.cern.ch/IPAC2011/papers/mopz007.pdf — extract: NS-FFAG final stage parameters (12.6–25 GeV, circumference, turns, RF).
- `SRC_URL_NUFACT10_PASTERNAK_NSFFAG` (snippet_only) — https://indico.ino.tifr.res.in/event/68/contributions/3181/attachments/1496/1846/Nufact10_FFAG_JPasternak_paper_corrected.pdf — extract: 'about 12 turns' statement, injection/extraction requirements, lattice.
- `SRC_JACOW_PAC2003_FPAB062` (snippet_only) — https://accelconf.web.cern.ch/p03/PAPERS/FPAB062.PDF — extract: authors; review of FFAG muon-acceleration options (historical).
- `SRC_ARXIV_2607_16904` (snippet_only) — https://arxiv.org/abs/2607.16904 — extract: abstract page: authors, date, scope; magnet-technology statements (all-HTS designs) relevant to fixed-field magnet limits; decide final category.

Uncharacterised leads (no URL recorded in the journal; locate first): Topp-Mugglestone Oxford staff page; Topp-Mugglestone IPAC'23 paper; IPAC2022 MOPOTK036; Brooks BNL 2023 FFA workshop talk (indico.bnl.gov event 17880); CYCLOTRONS2022 MOBI01; PAC'07 THOBAB01; STFC ASTeC EMMA page (https://www.astec.stfc.ac.uk/Pages/Accelerator-Physics-EMMA.aspx).

---

## Family `ultracold-source` (from `research/_fragments/ultracold-source_unresolved.md`)

### Unresolved items — reconnaissance family `ultracold-source`

Searches run 2026-10-28 with WebSearch only (20 queries, 32 sources surfaced). WebFetch attempts to arxiv.org,
www.kek.jp and proceedings.jacow.org failed (`ENOTFOUND` / network policy); every other host was seen through
search snippets only (`access: snippet_only`). Everything below is therefore snippet-level evidence: it may not
back a `reported_lhmuc` status and is capped at confidence `medium` (CLAUDE.md §1.5). Nothing in this file is a
parameter record. Note that the whole family concerns the J-PARC / μTRISTAN ultra-cold muon technology, i.e.
analogous or related-machine evidence; no LHμC-specific source rate, bunch population or emittance was found.

### Unresolved items

- WebFetch to arxiv.org, www.kek.jp and proceedings.jacow.org all failed (ENOTFOUND / network policy); no full texts were read. All values come from search-engine snippets and need verification against the primary PDFs.
- Design-stage laser ionisation efficiency: a snippet quoted 'USM: ~ 105 μ+/s (100μJ @122nm+300mJ @355nm) Efficiency: ~ 1×10-3 / surface μ' and 'Laser for spectroscopy→Very low ionization eff (~10-5)' from 'one J-PARC slide set' in the result list (candidates: imcc_workshop_ver2.pdf on indico.fnal.gov, ishida_nufact10.pdf, IPAC2018 TUPAK007). Exact source not identified; not attributed to any source entry.
- A snippet stated 'A 2025 talk reported a first RF acceleration of cooled muons, but the rate was low, at about 2×10⁻³ per pulse, and was limited by available laser energy' without naming the talk; not attributed.
- Muonium yield per incident muon at J-PARC from Beare et al. (PTEP 2020, arXiv:2006.01947): the snippet confirms a projection to J-PARC conditions was made but the projected number did not appear; only the 0.01 per incident muon estimate from Beer et al. 2014 is quoted.
- No measured 122 nm/355 nm ionisation efficiency appeared in snippets; only the design target (~1e-3 per surface muon), a 244 nm spectroscopy-laser result (1e-7 per mu+) and the theoretical 100% ceiling.
- Silica aerogel as the muonium target was confirmed only via Aritome et al. ('laser-ablated aerogel') and the Beer/Beare papers; the g-2/EDM linac query did not return the aerogel detail.
- EDM sensitivity goal conflicts across sources: 1.5e-21 e cm (PTEP 2019, Venanzoni 2025) vs 1.5e-19 e cm (Mibe 2025 slides as rendered in the snippet); primary collaboration paper should be checked.
- IH-DTL output energy varies across sources: 4.26 MeV (PRAB 29, 093201), 4.5 MeV (Yamazaki 2025 talk, older slides), 4.3 MeV (some conference papers).
- Exact title and author list of PRAB 21, 050101 (2018) first muon RF acceleration paper and of PRAB 19, 040101 (2016) IH-DTL design paper were not shown in snippets.
- Hot tungsten source: PRL 74, 4811 publication year not confirmed (snippet said '1994 experiment'; PRL volume 74 corresponds to 1995); RIKEN-RAL-specific ultraslow muon parameters were not found.
- Two H-line / 29.8 MeV/c quotes were attributed to EPJ Web Conf. 282 01016 by inference only; the snippet did not name the source among the result list (alternatives: PoS 452/003, IPAC2018 TUPAK007).
- INSPIRE-HEP returned no records for the site:inspirehep.net query; indico.cern.ch returned only one relevant contribution (Kimura, Sept 2025) and the FFA'25 Takaura μTRISTAN talk.
- Sakaki-Kamioka-Yoshida arXiv:2605.25580 normalisation (per p–Li nuclear collision) is not directly comparable to the Matsudo 2024 KEK slide figure of ~5.5e-4 muons per proton (assuming 50% efficiency) quoted in the same snippet; the Matsudo slide (conference-indico.kek.jp event 268) was not given its own entry because its title was not shown.
- **Category decisions awaiting the lead**: the J-PARC facility proceedings SRC_URL_EPJCONF_282_01016 (EPJ Web Conf.
  282, 01016) and SRC_URL_PASJ2019_THOH13 keep the journal's `RELATED_MACHINE`; `CONFERENCE_PROCEEDING` may be more
  appropriate since J-PARC MLF is a facility, not a collider concept. The slide decks SRC_URL_JACOW_IPAC2019_MOYPLM1
  and SRC_URL_INDICO_FNAL_13080_KOSEKI_2016 were moved to `CONFERENCE_PROCEEDING`/`workshop_talk` per the lead's rule.
- **Query→source attribution**: the journal does not record which query surfaced SRC_URL_KEK_NEWSROOM_2015_03_16,
  SRC_URL_INDICO_FNAL_13080_KOSEKI_2016 or SRC_URL_KEK_KANDA_2023_USM_BEAMLINE_JPCS; they are logged with
  query `(see family queries)`. Other links were taken from the query notes that name the source.
- **Normalised-emittance chain (design → measured)**: 1.5 π mm mrad expected (IPAC2018 FRXGBF1) → 0.315π/0.195π mm mrad
  simulated IH-DTL output (PRAB 19, 040101) → <1 π mm mrad measured (Kimura 2025; Kamioka MIP2025) → 0.85 π mm mrad
  measured at 100 keV (Aritome PRL 134, 245001). Whether each figure is normalised rms, at which energy and plane,
  is not visible in snippets; must be read from the PDFs before any value enters `parameters/source/`.
- **Rate chain (per-stage efficiencies) is incomplete**: H-line/H2 surface muons ~1e8/s design (1 MW) → Mu formation
  fraction (65.5±1.8)% (Beare 2020, aerogel) and vacuum emission 0.01 Mu per incident muon (Beer 2014 projection) →
  laser ionisation design ~1e-3 per surface muon (unattributed slide) → USM design ~1e5/s (Kamioka) vs operating 300 μ+/s
  (U-line, Chen et al. review) vs 1000 μ/s planned for 2027 at 4 MeV (Physics World). The product of the quoted
  efficiencies cannot be checked for consistency from snippets; no measured ionisation efficiency was found.
- **Scaling to LHμC**: the only collider-scale rate claim seen is the μTRISTAN '~1e5 times J-PARC MLF' statement as
  quoted via arXiv:2506.15445, and the hybrid-target yield ~1e-3 USM per p–Li collision (arXiv:2605.25580). Neither is
  an LHμC number; both are `imported_related`/`analogous` at best and require the full texts.

### Fetch backlog

Once network access to the hosts is allowed, fetch each item below, archive the PDF under `references/`, record
SHA-256 in `research/archived_metadata/`, and convert the snippet leads into parameter records only with page +
verbatim quotation.

- `SRC_ARXIV_2410_11367` — https://arxiv.org/abs/2410.11367v2 — extract: abstract page + PDF (v2): exact emittance definition, 5.7 keV / 100 keV chain, muon rate per pulse at 100 keV, reduction factors, aerogel/laser set-up, licence.
- `SRC_URL_KEK_TOPICS_202605261000` — https://www.kek.jp/en/topics/202605261000 — extract: page date; confirms PRL Collection of the Year 2025 selection only.
- `SRC_JACOW_IPAC2018_FRXGBF1` — https://proceedings.jacow.org/ipac2018/doi/JACoW-IPAC2018-FRXGBF1.html — extract: pp. 5041-5046: linac stage energies, 30 meV USM energy, 1.5 π mm mrad expectation, 0.1% momentum spread, RF frequencies, 212 MeV; licence CC-BY.
- `SRC_JACOW_IPAC2018_TUPAL076` — https://proceedings.jacow.org/ipac2018/doi/JACoW-IPAC2018-TUPAL076.html — extract: 88.6 keV Mu- RFQ result, October 2017, transmission/rate.
- `SRC_URL_DOAJ_PRAB_21_050101` — https://doaj.org/article/5bfba7e8e15a402399aaf6b909c5785b — extract: resolve the real article (title, authors, DOI) behind the DOAJ listing; 89 vs 88.6 keV.
- `SRC_ARXIV_2605_25580` — https://arxiv.org/pdf/2605.25580 — extract: hybrid target geometry, USM yield per p–Li collision, assumptions (unit Mu conversion), proton energy/power normalisation.
- `SRC_ARXIV_2506_15445` — https://arxiv.org/pdf/2506.15445 — extract: already uploaded (registry); only re-check whether the '1e5 x MLF' and '0.016 pions/proton' statements are the paper's or μTRISTAN's.
- `SRC_ARXIV_2201_06664` — https://arxiv.org/abs/2201.06664v1 — extract: μTRISTAN source assumptions: μ+ rate, bunch population, emittance, repetition rate, 3 km ring; v2 changes.
- `SRC_ARXIV_1407_8248` — https://arxiv.org/pdf/1407.8248 — extract: PTEP 2014 reference; 0.01 Mu per incident muon projection and its assumptions; ≥8x enhancement at 300 μm pitch.
- `SRC_ARXIV_2006_01947` — https://arxiv.org/pdf/2006.01947 — extract: (65.5±1.8)% Mu formation fraction; projected vacuum Mu yield per incident muon under J-PARC pulsed conditions.
- `SRC_URL_KEK_NEWSROOM_2015_03_16` — https://www2.kek.jp/en/newsroom/2015/03/16/1300/ — extract: press summary only; confirm 'order of magnitude' wording.
- `SRC_ARXIV_1901_03047` — https://arxiv.org/pdf/1901.03047 — extract: PTEP 2019 053C02: surface muon rate, USM rate, linac energies, emittance, 450 ppb / <70 ppb / 1.5e-21 e cm.
- `SRC_ARXIV_2512_20335` — https://arxiv.org/abs/2512.20335 — extract: late-2025 status: linac stage naming (Alvarez vs DAW/DLS), ~300 MeV/c, schedule.
- `SRC_URL_APS_PRAB_29_093201_NAKAZAWA` — https://journals.aps.org/prab/issues/29/9 — extract: article DOI; 0.34-4.26 MeV, 1.4% field error, 390 kW, design field, beam-test status.
- `SRC_DOI_10_1103_PHYSREVACCELBEAMS_19_040101` — https://link.aps.org/doi/10.1103/PhysRevAccelBeams.19.040101 — extract: exact title; APF IH-DTL design; 0.315π/0.195π mm mrad output emittances (definition, energy).
- `SRC_URL_INDICO_IHEP_24109_KAMIOKA_MIP2025` — https://indico.ihep.ac.cn/event/24109/contributions/189912/attachments/91221/118876/04-MIP2025_skamioka_ver3.pdf — extract: spec sheet slide: 25 Hz, 2 ns, ~1e5/s, <1 π mm mrad, laser energies, 4 MeV 2027 milestone; MIP2025 date/venue.
- `SRC_URL_INDICO_JLAB_951_YAMAZAKI_BDX2025` — https://indico.jlab.org/event/951/contributions/17508/attachments/13298/21439/250905_BDX&Beyond_yamazaki.pdf — extract: linac energy breakdown (0.3 / 4.5 / 40 / 212 MeV), H2 milestones with years.
- `SRC_ARXIV_2601_15818` — https://arxiv.org/abs/2601.15818v2 — extract: review tables: facility rates (300 μ+/s USM), 122+355 nm scheme, efficiency statements.
- `SRC_URL_KEK_INDICO_346_HOKKAIDO_2026` — https://conference-indico.kek.jp/event/346/contributions/7562/attachments/5135/8350/Hokkaido_2026_ver1.pdf — extract: speaker/title; 1e-7 per μ+ with 244 nm laser; efficiency factorisation; any measured 122 nm efficiency.
- `SRC_DOI_10_1103_PHYSREVLETT_74_4811` — https://link.aps.org/doi/10.1103/PhysRevLett.74.4811 — extract: publication year; 2300 K tungsten, 0.2 eV; USM yield per incident muon (hot-W alternative).
- `SRC_URL_INSPIRE_FILES_6103970C` — https://s3.cern.ch/inspire-prod-files-6/6103970c6ab123d9a8571e71d1fff3fa — extract: identify the paper; 6N 50 μm W foil; 122.088 nm Lyman-α scheme.
- `SRC_URL_UTOKYO_PRESS_11225` — https://www.s.u-tokyo.ac.jp/en/press/11225/ — extract: 31 Aug 2026 release: 4 MeV → 25 meV → 0.3 MeV, 3x/200x gains, absolute rate if stated, 2027-28 plan (also kek.jp/?p=48023).
- `SRC_URL_PHYSICSWORLD_MUON_BEAM_COLLIDER` — https://physicsworld.com/a/high-quality-muon-beam-holds-promise-for-future-collider/ — extract: article date; '4 MeV at 1000 muon/s planned for 2027' quote and who said it.
- `SRC_URL_POS_MUON4FUTURE2023_008` — https://pos.sissa.it/452/008/pdf — extract: designed USM flux ~1e5/s, FY2026 completion, H2 layout.
- `SRC_INDICO_1528564_6573983` — https://indico.cern.ch/event/1528564/contributions/6573983 — extract: conference name; abstract with <1 π mm mrad measured normalised emittance; slides if attached.
- `SRC_URL_INDICO_ED_112_MIBE_G2TI_2025` — https://indico.ph.ed.ac.uk/event/112/contributions/1681/attachments/1024/1425/J-PARC_muon_g-2_at_5th_g-2_Theory_Initiatives.pdf — extract: H2 ~1e8/s surface muons; DAW 4-40 MeV; resolve EDM 1.5e-19 vs 1.5e-21 e cm.
- `SRC_URL_EPJCONF_282_01016` — https://www.epj-conferences.org/10.1051/epjconf/202328201016/pdf — extract: authors; H-line design 1e8/s at 1 MW; 29.8 MeV/c; confirm attribution of the quoted sentences.
- `SRC_URL_PASJ2019_THOH13` — https://www-linac.kek.jp/mirror/www.pasj.jp/web_publish/pasj2019/proceedings/PDF/THOH/THOH13_oral.pdf — extract: RCS 3 GeV / 1 MW / 333 μA / 8.3e13 ppp / 25 Hz / <1 μs; graphite IG430 target 2 cm x 30 cm rotating.
- `SRC_URL_JACOW_IPAC2019_MOYPLM1` — https://accelconf.web.cern.ch/ipac2019/talks/moyplm1_talk.pdf — extract: speaker; RCS 1 MW design, 1.5 MW second target station plan.
- `SRC_URL_INDICO_FNAL_13080_KOSEKI_2016` — https://indico.fnal.gov/event/13080/contributions/17160/attachments/11491/14678/US-JAPAN-WS_J-PARC_koseki_pub.pdf — extract: RCS 25 Hz, 348.3 m circumference, 1 MW design.
- `SRC_URL_JACOW_LINAC2022_WE1AA05` — https://accelconf.web.cern.ch/linac2022/doi/JACoW-LINAC2022-WE1AA05.html — extract: authors; RFQ II spare re-use; 324 MHz RFQ 2017 demonstration.
- `SRC_URL_KEK_KANDA_2023_USM_BEAMLINE_JPCS` — https://research.kek.jp/people/kanda/2023/03/01/ultra-slow-muon-beamline-jpcs.html — extract: locate the JPCS paper (U-line USM beamline) and its rate/emittance figures.

#### Unattributed leads to locate (no source entry; not in the journal source list)

- Slide set quoting 'USM: ~1e5 μ+/s (100 μJ @122 nm + 300 mJ @355 nm) Efficiency: ~1e-3 / surface μ' and 'Laser for
  spectroscopy → very low ionization eff (~1e-5)' — candidates per journal: imcc_workshop_ver2.pdf (indico.fnal.gov),
  ishida_nufact10.pdf, IPAC2018 TUPAK007.
- '2025 talk: first RF acceleration of cooled muons at ~2e-3 per pulse, limited by laser energy' — talk not named.
- Matsudo 2024 KEK slides (conference-indico.kek.jp event 268): ~5.5e-4 muons per proton assuming 50% efficiency — title not shown.
- Nagoya University news item and KEK 2024 press PDF pr202405231500 on the 2024 RF acceleration result — surfaced but not registered.
- Kamioka 'Muon4Future2023' companion PoS 452/003 and IPAC2018 TUPAK007 — possible true sources of the H-line sentences attributed by inference to EPJ Web Conf. 282, 01016.

---

## Family `muon-collider-mdi` (from `research/_fragments/muon-collider-mdi_unresolved.md`)

### Unresolved items - reconnaissance family `muon-collider-mdi`

Searches run 2026-10-28 with WebSearch only. WebFetch was attempted on pos.sissa.it, zenodo.org and inspirehep.net and failed
(network policy); arxiv.org and Indico hosts were not attempted per instructions. Everything below is snippet-level evidence:
it may not back a `reported_lhmuc` status and is capped at confidence `medium` (CLAUDE.md §1.5). Nothing in this file is a
parameter record. Note also that every source in this family describes the IMCC/MAP mu+mu- collider or its predecessors,
i.e. an analogous machine; nothing here is an LHμC (mu+p) MDI statement.

### Unresolved items

- All WebFetch attempts failed: pos.sissa.it, zenodo.org and inspirehep.net do not resolve from this session (network policy); arxiv.org and indico hosts were not attempted per instructions. Every parameter above is from search snippets only.
- Exact 10 TeV nozzle inner aperture angles (three angles per MuCol Report No. 5 Table 9.1) and total nozzle length were not present in any snippet; only outer inclination 10 degrees, tip at 6 cm, bottleneck at 100 cm, L* = 6 m are quotable.
- 3 TeV per-species BIB numbers from PoS(ICHEP2022)063 Table 1 were cut off in snippets; only the 10 TeV photon (1.1e8) and neutron (1.0e8) values appeared.
- Authorship and abstract of arXiv:2504.21417 'The Muon Collider' not confirmed from snippets (only its reference list surfaced).
- Author list of MUSIC arXiv:2601.13189 and of arXiv:2511.23273 not in snippets.
- No standalone arXiv preprint on vFFA for muon acceleration (Topp-Mugglestone 2025) found; only indico talks and IPAC2021 proceedings.
- Licenses marked 'typical; not confirmed' for PoS, MDPI and JACoW items are inferred from publisher norms, not verified for these specific items.
- MuCol Report No. 7 snippet gives license CC BY via Zenodo/avesis mirror; not verified against arXiv page.
- No Geant4-specific BIB study at 3 or 10 TeV surfaced; FLUKA (and historical MARS15/G4beamline) dominate the found sources.
- Query-to-source mapping in the search log is inferred from the journal query notes (the journal has no explicit mapping); the Snowmass 2021 detector-performance white paper (SRC_ARXIV_2203_07964) is named by no query note and is logged with query '(see family queries)'.
- Category decisions applied here (lead, 2026-10-28): arXiv:2504.21417 'The Muon Collider' -> RELATED_MACHINE; arXiv:2506.15445 -> RELATED_MACHINE (existing uploaded id SRC_ARXIV_2506_15445 reused); Indico/DESY/FNAL slide decks and posters -> CONFERENCE_PROCEEDING / workshop_talk; Snowmass white papers on arXiv -> CONFERENCE_PROCEEDING. Three arXiv-only preprints the journal called PEER_REVIEWED without any journal reference (MAIA arXiv:2502.00181, Collamati et al. arXiv:2105.09116, Burk et al. arXiv:2608.02714) are recorded as RELATED_MACHINE until their abstract pages are read; this follows the lead's rule for 2610.* records and should be confirmed by the lead.
- OFFICIAL_CERN for the MuCol Milestone Reports (No. 5 and No. 7) rests on the snippet phrase 'CERN lead beneficiary'; they are EU design-study deliverables, not CERN Yellow Reports. The IMCC Interim Report (CERN-2024-002) is a confirmed CERN Yellow Report.
- No LHμC-specific MDI statement (mu+p, asymmetric, single muon beam) was found by this family; all BIB and nozzle numbers refer to symmetric mu+mu- colliders at 1.5, 3 or 10 TeV and cannot be transferred to LHμC without a dedicated derivation (status analogous / analytical_estimate).
- Applicability of the 10 degree nozzle acceptance to LHμC must be checked against the uploaded primary documents (arXiv:2610.35154 §3-4 and the μLHC paper §2.4), which are the only sources that discuss a nozzle for a mu+p detector.

### Fetch backlog

Fetch each URL once the host is allowed, archive the file under references/ with SHA-256, then re-check every 'snippet-quoted' lead in
`research/_fragments/muon-collider-mdi_sources.yaml` against the full text before any parameter record is written.

- `SRC_ARXIV_2510_27437` <https://arxiv.org/abs/2510.27437> (access now: blocked) - extract: consolidated 10 TeV parameter tables; nozzle section (material INERMET180, geometry, L*, aperture angles); licence statement; version/date.
- `SRC_ARXIV_2411_02966` <https://arxiv.org/abs/2411.02966> (access now: snippet_only) - extract: Table 9.1 nozzle coordinates and the three aperture angles; nozzle total length; borated-polyethylene layer thickness; licence.
- `SRC_ARXIV_2303_08533` <https://arxiv.org/abs/2303.08533> (access now: snippet_only) - extract: MDI/nozzle chapter, BIB per bunch crossing by species at 3 and 10 TeV, erratum content; licence.
- `SRC_ARXIV_2407_12450` <https://arxiv.org/abs/2407.12450> (access now: snippet_only) - extract: MDI and detector chapters; staged 3/10 TeV parameters; CC-BY-4.0 confirmation.
- `SRC_ARXIV_2504_21417` <https://arxiv.org/abs/2504.21417> (access now: snippet_only) - extract: author list, abstract, date, licence; whether it is the ESPPU input document; any MDI/nozzle numbers.
- `SRC_ARXIV_2209_01318` <https://doi.org/10.1088/1748-0221/19/02/T02015> (access now: snippet_only) - extract: nozzle acceptance statement (polar angle above 10 degrees) in context; FLUKA/MARS15 comparison section; CC BY 4.0 confirmation.
- `SRC_ARXIV_2502_00181` <https://arxiv.org/abs/2502.00181> (access now: snippet_only) - extract: author list, journal status, nozzle description (tungsten heavy-alloy + borated polyethylene), solenoid 5 T, BIB efficiency statements with their conditions.
- `SRC_ARXIV_2601_13189` <https://arxiv.org/abs/2601.13189> (access now: snippet_only) - extract: author list; 11.4 m length, 5 T solenoid, PbF2 ECAL statements; relation to arXiv:2511.23273.
- `SRC_URL_POS_ICHEP2024_819` <https://pos.sissa.it/476/819/> (access now: blocked) - extract: full author list; 10 TeV nozzle adjustment geometry and resulting BIB numbers; licence.
- `SRC_URL_POS_ICHEP2022_063` <https://pos.sissa.it/414/063/> (access now: blocked) - extract: Table 1 in full (1.5, 3, 10 TeV per-species BIB per bunch crossing, one beam, MAP-like nozzle); licence.
- `SRC_URL_MDPI_PARTICLES_2025_8_1_25` <https://www.mdpi.com/2571-712X/8/1/25> (access now: snippet_only) - extract: decay rate 2.34e5 /m/beam/BX with its stated beam population; BIB order of magnitude; readout window sign and bounds; 10 TeV adaptation; CC BY confirmation.
- `SRC_ARXIV_2311_03280` <https://arxiv.org/abs/2311.03280> (access now: snippet_only) - extract: nozzle role and IR/nozzle optimisation statements; BIB mitigation summary; licence.
- `SRC_ARXIV_2203_08033` <https://arxiv.org/abs/2203.08033> (access now: snippet_only) - extract: MAP nozzle description (two tungsten cones, borated polyethylene coating, 10 degree opening angle) in context; authors.
- `SRC_ARXIV_2105_09116` <https://arxiv.org/abs/2105.09116> (access now: snippet_only) - extract: author list; journal status; BIB composition and origin (decays within tens of metres of the IP) at 1.5 TeV; FLUKA vs MARS15 comparison.
- `SRC_INDICO_DESY_45968_187027` <https://indico.desy.de/event/45968/contributions/187027/attachments/97249/133765/MDI_annual_meeting25.pdf> (access now: snippet_only) - extract: speaker; nozzle material and geometry slides; the L* 6 m vs 10 m result that the snippet cut off.
- `SRC_INDICO_1293507_5594289` <https://indico.cern.ch/event/1293507/contributions/5594289/attachments/2722540/4730396/poster_mdi.pdf> (access now: snippet_only) - extract: authors; FLUKA figure for ~6.4e9 particles/BX and ~1.18e7 decays/BX with conditions (energy, nozzle state).
- `SRC_INDICO_FNAL_64493_294885` <https://indico.fnal.gov/event/64493/contributions/294885/attachments/180657/247612/USMCC_first_collaboration_MDI.pdf> (access now: snippet_only) - extract: speaker; 10 TeV layout with L* = 6 m; nozzle optimisation plan for 3 and 10 TeV.
- `SRC_ARXIV_2608_02714` <https://arxiv.org/abs/2608.02714> (access now: snippet_only) - extract: forward neutrino flux (~1e12 /s) with the design assumptions used; factor-120 comparison baseline; journal status; companion arXiv:2608.02718.
- `SRC_ARXIV_PHYSICS_9908017` <https://arxiv.org/abs/physics/9908017> (access now: snippet_only) - extract: author confirmation (B.J. King?); dose estimates vs energy; siting conclusion.
- `SRC_ARXIV_2511_03883` <https://arxiv.org/abs/2511.03883> (access now: snippet_only) - extract: hybrid RCS description and the ~2 cm orbit excursion statement; CERN report number; licence.
- `SRC_INDICO_DESY_45968_185344` <https://indico.desy.de/event/45968/contributions/185344> (access now: snippet_only) - extract: abstract text and any slides; vFFA footprint comparison with RCS1/RCS4.
- `SRC_INDICO_1553599_6692118` <https://indico.cern.ch/event/1553599/contributions/6692118/attachments/3137263/5567034/20250917-muon-ffa.pdf> (access now: snippet_only) - extract: slides: vFFA parameter studies, decoupled insertions, FFA collider ring, open issues.
- `SRC_JACOW_IPAC2021_THPAB124` <https://jacow.org/ipac2021/papers/THPAB124.pdf> (access now: snippet_only) - extract: paper text: skew-quadrupole vFFA arc concept for a muon collider; CC BY 3.0 confirmation.
- `SRC_ARXIV_2506_15445` <https://arxiv.org/abs/2506.15445> (access now: snippet_only) - extract: arXiv abstract page only (licence, version history); the PDF is already uploaded and read in full.
- `SRC_ARXIV_2203_07964` <https://arxiv.org/abs/2203.07964> (access now: snippet_only) - extract: authors; nozzle re-optimisation statement for 3 and 10 TeV MDI; 3 TeV detector performance with BIB.

Additional URLs named in the journal but not registered as sources (confirm or discard on fetch):

- <https://zenodo.org/records/17476875> - Zenodo record of MuCol Milestone Report No. 7: licence (CC BY) and version 1.0 Final confirmation.
- <https://inspirehep.net/literature/2642414> and <https://inspirehep.net/literature/2845756> - INSPIRE records for 'Towards a muon collider' and MuCol Report No. 5: metadata only.
- <https://arxiv.org/abs/2608.02718> - companion paper to 'Neutrino Fluxes at a Muon Collider' (named in a query note; not a source entry).
- <https://arxiv.org/abs/2511.23273> - MUSIC proof-of-concept paper (named in a query note; not a source entry).
- <https://arxiv.org/abs/2605.21590> - names the MUSIC concept (named in a query note; not a source entry).
- <https://pos.sissa.it/449/630/> - 'Machine-Detector interface for multi-TeV Muon Collider' (named in a query note; not a source entry).
- <https://e-publishing.cern.ch> CYRM issue 171 - IMCC Interim Report publisher page (named in the version field).
- <https://par.nsf.gov/servlets/purl/10509840> and <https://strathprints.strath.ac.uk/88720> - open mirrors of the Forum report and of 'Towards a muon collider' (reachable-host alternatives if primary hosts stay blocked).

---

## Family `theory-benchmarks` (from `research/_fragments/theory-benchmarks_unresolved.md`)

### Unresolved items — reconnaissance family `theory-benchmarks`

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

### Unresolved items

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

### Fetch backlog

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

---

## Family `software-tools` (from `research/_fragments/software-tools_unresolved.md`)

### Unresolved items — reconnaissance family `software-tools`

Searches run 2026-10-28 with WebSearch (45 queries, 40 sources surfaced). WebFetch succeeded only on
pypi.org, registry.npmjs.org, launchpad.net, github.com and raw.githubusercontent.com (29 sources marked
`fetched`: PyPI/npm registry JSON, GitHub release/repository pages, one License.txt). Fetches of arxiv.org,
geant4.org, www.pp.rhul.ac.uk, docs.desy.de, fluka-forum.web.cern.ch, hepforge.org hosts,
feynrules.irmp.ucl.ac.be, dev.opencascade.org, root.cern and hepdata.net failed (11 sources marked `blocked`;
their values come from search snippets or secondary pages). Nothing in this family is a collider parameter:
every `snippet-quoted` line in `software-tools_sources.yaml` is a software version / licence / install-route
lead for `docs/software_inventory.md`, and snippet-level evidence is capped at confidence `medium`
(CLAUDE.md §1.5). No file was archived (`archived_file: null` everywhere); nothing was installed or executed.

### Unresolved items

#### From the journal (verbatim scope, one bullet per item)

- **MAD-X licence is contradictory across sources**: repository `License.txt` is a custom CERN licence
  restricting use to collaborating organisations, while LCG Info labels 5.09.00 "MIT License" and a 2011 CERN
  gitlab mirror says "EPICS Open License". Needs confirmation at the 5.09.00 tag (GitHub releases section
  empty). Until resolved, MAD-X must be treated as **non-free / terms unconfirmed** in the software inventory;
  cpymad's own PyPI `license_expression` ("GPL-3.0-or-later AND Apache-2.0 AND LicenseRef-CERN-MADX-Proprietary")
  corroborates the proprietary reading for the bundled binary. Conflict preserved, not averaged (CLAUDE.md §1.6).
- **Bmad core library licence not confirmed** from the repository (raw `LICENSE` 404 on both `main` and
  `master`); only a third-party aggregator claim (depscope) of GPL-3.0-or-later. conda-forge `bmad` version
  not captured. PyTao (1.3.3) is confirmed GPLv3 from PyPI metadata.
- **Geant4**: official download/licence pages (geant4.org) not fetchable; latest version taken from the GitHub
  mirror tag v11.4.3 (year not shown on page); 11.4 release date 2025-12-05 from a news snippet. Python
  bindings (`geant4_pybind` on PyPI) not checked.
- **BDSIM**: current release number only from a search snippet (manual sidebar "1.7.7"); www.pp.rhul.ac.uk and
  bitbucket not fetched. Required Geant4 version not captured.
- **G4beamline**: official site g4beamline.muonsinc.com not reachable; licence "GPL" only via the DESY Maxwell
  secondary listing; version 3.08/3.08b (compatible with Geant4 11.3.2) from the Mu2e wiki (secondary).
- **FLUKA**: fluka.cern and fluka.org blocked; licence conditions come from the CERN forum FAQ snippet and
  2009-2013 course slides; the current Single User Licence Agreement text was not verified. Registration is
  "subject to approval" — FLUKA cannot be assumed available for the project until an account exists.
- **Herwig**: hepforge blocked; only 7.3.0 (and LCG 7.3.0p1) confirmed, no evidence of 7.3.x point releases.
- **FeynRules**: official site blocked; current version unknown (a wiki snapshot labels a "current" tarball as
  2.3); licence stated only as "Licensing provisions: None" in the 2.0 CPC summary. Requires Mathematica
  (7.0+ per the 2.0 paper) — a proprietary dependency that must be declared in the inventory.
- **SARAH**: hepforge blocked; current version unknown; licence only from older manuals ("GNU library public
  license"). Also requires Mathematica.
- **LHAPDF**: hepforge blocked; latest upstream version inferred from distro packaging (6.5.5); the PyPI
  `LHAPDF` record (6.2.1.post10) is stale with empty metadata — pip is not a supported route per results;
  conda-forge is (GPL-3.0-only there; Gentoo lists GPL-2 — conflict noted).
- **HEPData** (hepdata.net) itself not fetched; only `hepdata_lib` (MIT, 0.21.0) and the platform GPL statement
  from docs snippets; CC0 default data licence from a snippet.
- **ROOT**: root.cern not fetched; PyPI `root` wheel status (alpha, Linux-only per the 6.38.00 announcement)
  not verified for 6.40 (GitHub latest v6-40-04, 2026-08-27).
- **Delphes**: release year for 3.5.1 not shown on the GitHub page ("released this 04 Feb"); 3.5.2pre02 is a
  pre-release only.
- **OCCT**: official dev.opencascade.org blocked; release data from GitHub (V8_0_1, 2026-07-30).
- **opencascade.js**: repository appears inactive (tracker: last push Aug 2023) and bundles OCCT 7.6.2 (two
  major versions behind OCCT 8.0.1 used by cadquery-ocp 8.0.1.1.0); npm 1.1.1 — maintenance status should be
  checked before adoption for the web viewer.
- **FreeCAD**: GitHub page did not display a licence badge; LGPL-2+ taken from a source-header snippet;
  conda-forge availability not checked; wiki `FreeCAD_API` page is marked outdated.
- **Xsuite umbrella package** (`xsuite` on PyPI) version not captured; only xtrack 0.118.5 / xpart 0.23.23 /
  xfields 0.27.6 individually (all Apache-2.0 from PyPI metadata). Query 3 on the core-package licence
  returned only xcoll/xboinc results.
- **Cheetah**: PyPI metadata has empty license fields; GPLv3 only from the README badge.
- **Search-operator failure**: `site:inspirehep.net` and `site:indico.cern.ch` operators returned no
  INSPIRE/Indico records (operator not honoured by the search backend); arXiv pages are fetch-blocked so all
  arXiv details (dates, journal references, licences) are from snippets only.

#### Added by the research-log builder (process items)

- **Journal has no explicit query→source map.** `discovered_by_queries` and the 49 paired rows in
  `software-tools_search_log.csv` were inferred from the per-query `note` text (the note names the package,
  identifier or a value unique to the source). Three queries surfaced no registrable source and have
  query-only rows: "Xsuite xtrack xpart xfields PyPI CERN beam dynamics license Apache", "Pythia 8 event
  generator pythia.org GPL license latest version 8.3 pip pythia8mc" (distro packaging only; pythia8mc was
  found by the later dedicated query) and "SARAH sarah.hepforge.org download version 4.15 …". Every source
  has at least one inferred query, so no "(see family queries)" row was needed.
- **Access-mode interpretation.** `fetched` was assigned where the journal marks `fetch_blocked=false` and the
  quotations are registry JSON fields or page text (29 sources). These were WebFetch reads summarised in the
  journal, not archived copies: `sha256` is null and the exact page revision cannot be reproduced. `blocked`
  was assigned to the 11 `fetch_blocked=true` sources. No source was given `snippet_only` because the journal
  records a fetch attempt (successful or refused) for every one; if the lead prefers `snippet_only` for the
  blocked arXiv records whose values came purely from snippets, that is a one-field change.
- **Category labels kept as the scout classified them; candidates for lead review** (no lead correction was
  issued for this family):
  - PEER_REVIEWED on arXiv-only records whose journal reference was NOT seen in snippets: arXiv:2401.05815
    (Cheetah; snippets gave only "CC BY 4.0 (arXiv HTML)", 2024), arXiv:2312.05175 (Herwig 7.3 *release
    note* — a release note is normally not a refereed article), arXiv:1309.7223 (SARAH 4; journal ref not
    quoted). By the rule the lead applied to arXiv:2610.28252 / 2610.17801 these could be downgraded to
    UNVERIFIED pending the abstract page. arXiv:1405.0301 (JHEP07(2014)079), arXiv:1310.1921 (CPC program
    summary) and arXiv:1808.10745 ("CPC 2020") have snippet-level journal references and were kept.
  - OFFICIAL_CERN for Geant4 (the Geant4 Collaboration is international; CERN hosts the project) and for the
    FLUKA forum FAQ (a CERN-hosted forum post, not a CERN report) — both arguably OFFICIAL_SOFTWARE_DOCUMENTATION.
  - CONFERENCE_PROCEEDING for arXiv:2310.00317 (Xsuite, HB2023 JACoW) is consistent with the lead's
    Snowmass/Evian rule; `source_type` left as `arxiv_preprint` per the journal.
- **Version drift.** All versions are a 2026-10-28 snapshot (xtrack 0.118.5 was released that same day). The
  inventory must pin versions by lock file, not by this fragment.
- **Nothing was installed or run.** No statement about compatibility (e.g. cpymad 1.20.0 with MAD-X 5.09.00,
  PyTao with a conda-forge `bmad`, pyg4ometry with Geant4 11.4) was tested; those belong to the software
  inventory's verification step, not to reconnaissance.

### Fetch backlog (once network access is allowed)

Each item: URL → what to extract and what it unblocks. Primary/official pages first, then arXiv abstract pages.

#### Official project / licence pages (currently blocked)

- https://github.com/MethodicalAcceleratorDesign/MAD-X/blob/master/License.txt (full text) and
  https://github.com/MethodicalAcceleratorDesign/MAD-X/tags → full licence text (collaborating-organisation
  clause, verbatim), whether a 5.09.00 tag exists and its date; compare with
  https://lcginfo.cern.ch (package madx 5.09.00 "MIT License" label) and the CERN gitlab mirror "EPICS Open
  License" claim → resolves the MAD-X licence conflict (record in `research/source_conflicts.yaml` if it
  persists).
- https://github.com/bmad-sim/bmad-ecosystem (LICENSE file at its real path; releases page) and
  https://anaconda.org/conda-forge/bmad → Bmad licence text, latest tag/date, conda-forge version →
  confirms or replaces the aggregator GPL-3.0-or-later claim.
- https://geant4.org/download/license (Geant4 Software License v1.0 full text),
  https://geant4.org/download (current release number + date, patch history),
  https://geant4.org/news (11.4 announcement 2025-12-05) and https://pypi.org/pypi/geant4-pybind/json →
  licence verbatim, 11.4.3 release date, Python-binding availability/version/licence.
- https://www.pp.rhul.ac.uk/bdsim/manual/licence.html and
  https://www.pp.rhul.ac.uk/bdsim/manual/ (sidebar version), https://bitbucket.org/jairhul/bdsim (tags,
  CHANGELOG) → GPLv3 statement verbatim, current release (1.7.7?), required Geant4 version range.
- https://g4beamline.muonsinc.com/ (or https://www.muonsinc.com/Website1/tiki-index.php?page=G4beamline) →
  licence statement from the publisher (not DESY), current version (3.08/3.08b?), Geant4 compatibility
  (11.3.2 per Mu2e wiki), download conditions.
- https://docs.desy.de/maxwell/applications/g4beamline/ → the exact DESY listing sentence ("License: GPL")
  for the archived secondary record.
- https://fluka-forum.web.cern.ch/t/important-registration-and-package-download-faq/3857 and
  https://fluka.cern/download/licences (Single User Licence Agreement) → current licence text, academic vs
  commercial conditions, registration/approval procedure → decides whether FLUKA can be planned for shielding
  and activation studies (otherwise Geant4/BDSIM only).
- https://root.cern/install/ and https://root.cern/releases/ → 6.40 release notes, licence (LGPL-2.1+),
  status of `pip install root` for 6.40 (alpha? Linux-only?) → install route for the inventory.
- https://launchpad.net/mg5amcnlo (download listing) and
  https://github.com/mg5amcnlo/mg5amcnlo/tree/3.x (LICENSE) → exact 3.8.x tarball name/date and the
  UoI-NCSA licence text.
- https://pythia.org/ (releases, licence) and https://gitlab.com/Pythia8/releases → Pythia 8.318 release
  date, GPL-2.0-or-later statement verbatim; confirm pythia8mc 8.318.0 tracks the same release.
- https://herwig.hepforge.org/ (downloads, news) → latest 7.3.x release and date, GPLv3 + MCnet guidelines
  text, bootstrap-script dependencies (ThePEG, LHAPDF, …).
- https://cp3.irmp.ucl.ac.be/projects/delphes and https://github.com/delphes/delphes/releases → 3.5.1
  release year, whether 3.5.2 is final, ROOT version requirement.
- https://feynrules.irmp.ucl.ac.be/ (downloads page) → current FeynRules version and release date, any
  licence statement, Mathematica version requirement.
- https://sarah.hepforge.org/ → current SARAH version (4.15.x?), licence text, Mathematica requirement.
- https://lhapdf.hepforge.org/ (downloads, index of changes) → latest LHAPDF 6.5.x version and date, licence
  (GPL-3.0-only vs GPL-2 conflict between conda-forge/Fedora and Gentoo), supported Python-binding route;
  https://pypi.org/pypi/LHAPDF/json → confirm the PyPI record is stale/unmaintained.
- https://www.hepdata.net/ (about/terms) → platform licence (GPL) and default data licence (CC0) verbatim
  for publishing digitised results.
- https://dev.opencascade.org/release and https://github.com/Open-Cascade-SAS/OCCT/blob/master/LICENSE_LGPL_21.txt
  plus OCCT_LGPL_EXCEPTION.txt → licence + exception text, 8.0.1 release notes.
- https://github.com/donalffons/opencascade.js (commits, issues) and https://www.npmjs.com/package/opencascade.js
  → last commit date, bundled OCCT version (7.6.2?), maintenance status → adopt/reject for the web viewer.
- https://github.com/FreeCAD/FreeCAD/blob/main/LICENSE and https://wiki.freecad.org/FreeCAD_API,
  https://anaconda.org/conda-forge/freecad → licence text, 1.1.4 release year, scripting-API documentation
  location, conda-forge availability (for headless geometry export).
- https://pypi.org/pypi/xsuite/json and https://github.com/xsuite/xsuite → umbrella-package version and the
  pinned xtrack/xpart/xfields/xcoll/xobjects/xdeps set; LICENSE files of each module.
- https://github.com/desy-ml/cheetah/blob/master/LICENSE → Cheetah licence text (GPLv3 badge only so far).
- https://threejs.org/ and https://github.com/mrdoob/three.js/releases → r186 release date, MIT text.
- https://pypi.org/pypi/pytao/json, /cpymad/json, /pyg4ometry/json, /pylhe/json, /pyhf/json, /pymoo/json,
  /botorch/json, /ax-platform/json, /scikit-optimize/json, /optuna/json, /cadquery/json, /cadquery-ocp/json,
  /build123d/json, /cheetah-accelerator/json, /pythia8mc/json, /xtrack/json, /xpart/json, /xfields/json,
  https://registry.npmjs.org/three/latest, https://registry.npmjs.org/opencascade.js/latest → re-fetch and
  **archive** (save JSON, record SHA-256 in `research/archived_metadata/`) so that the version/licence
  values quoted in the fragment become reproducible rather than journal-summarised.

#### arXiv abstract pages (blocked; needed to verify dates, journal references, licences, categories)

- https://arxiv.org/abs/2310.00317 → Xsuite paper: version list/dates, comments field (HB2023 TUA2I1 /
  IPAC'24 WEPR56), licence → confirms CONFERENCE_PROCEEDING.
- https://arxiv.org/abs/2401.05815 → Cheetah: journal reference (if published), licence → decides
  PEER_REVIEWED vs UNVERIFIED.
- https://arxiv.org/abs/1808.10745 → BDSIM: CPC reference (volume, year, DOI), licence.
- https://arxiv.org/abs/1405.0301 → MG5_aMC: confirm JHEP07(2014)079 and DOI 10.1007/JHEP07(2014)079.
- https://arxiv.org/abs/2312.05175 → Herwig 7.3 release note: version/date, whether any journal reference
  exists → likely downgrade to UNVERIFIED or CONFERENCE_PROCEEDING-equivalent.
- https://arxiv.org/abs/1310.1921 → FeynRules 2.0: CPC reference and DOI; "Licensing provisions" text.
- https://arxiv.org/abs/1309.7223 → SARAH 4: CPC reference and DOI; licence sentence verbatim.

---

## De-duplication note

No bullet block was an exact repeat of another family's text (after whitespace normalisation), so every fragment is reproduced in full. Several families do refer to the same *source* from different angles (e.g. `SRC_ARXIV_2506_15445` in `lhmuc-primary` and `mulhc-mutristan`, `SRC_ARXIV_2206_00037` in `lhc-hl-lhc-protons` and `lhmuc-primary`); those items are kept because the open questions differ. The lead's merge into `research/source_registry.yaml` should carry one record per `source_id` with the union of the `unresolved_questions` lists.
