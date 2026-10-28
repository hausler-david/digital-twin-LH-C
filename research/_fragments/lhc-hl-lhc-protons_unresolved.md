# Unresolved items — reconnaissance family `lhc-hl-lhc-protons`

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

## Unresolved items

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

## Fetch backlog

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
