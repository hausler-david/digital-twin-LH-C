# Unresolved items - reconnaissance family `muon-collider-mdi`

Searches run 2026-10-28 with WebSearch only. WebFetch was attempted on pos.sissa.it, zenodo.org and inspirehep.net and failed
(network policy); arxiv.org and Indico hosts were not attempted per instructions. Everything below is snippet-level evidence:
it may not back a `reported_lhmuc` status and is capped at confidence `medium` (CLAUDE.md §1.5). Nothing in this file is a
parameter record. Note also that every source in this family describes the IMCC/MAP mu+mu- collider or its predecessors,
i.e. an analogous machine; nothing here is an LHμC (mu+p) MDI statement.

## Unresolved items

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

## Fetch backlog

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
