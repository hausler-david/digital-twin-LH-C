# Unresolved items — reconnaissance family `lhec-erl`

Searches run 2026-10-28 with WebSearch only (19 queries, 23 sources surfaced). WebFetch attempts failed
(`DNS not resolved`) on arxiv.org, ar5iv.labs.arxiv.org, indico.cern.ch, iopscience.iop.org, jacow.org and
epjc.epj.org. Six URLs on other hosts (atrium.in2p3.fr, hal.archives-ouvertes.fr, accelconf.web.cern.ch ×2,
infoscience.epfl.ch, indico.fis.agh.edu.pl) were never fetched (journal `fetch_blocked=false`, no page read),
so they are `snippet_only`. Everything below is therefore snippet-level evidence: it may not back a
`reported_lhmuc` status and is capped at confidence `medium` (CLAUDE.md §1.5). Nothing in this file is a
parameter record; every LHeC/ERL/PERLE number is at best `imported_related` or `analogous` once verified.

## Unresolved items

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

## Fetch backlog (once network access is allowed)

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
