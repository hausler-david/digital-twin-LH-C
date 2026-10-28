# Unresolved items — reconnaissance family `lhmuc-primary`

Searches run 2026-10-28 with WebSearch only. Every WebFetch attempt failed (`getaddrinfo ENOTFOUND`) on
arxiv.org, indico.cern.ch, help4cern.web.cern.ch, indico.fis.agh.edu.pl, events2.saip.org.za,
avesis.uludag.edu.tr and academic.oup.com. Everything below is therefore snippet-level evidence: it may
not back a `reported_lhmuc` status and is capped at confidence `medium` (CLAUDE.md §1.5). Nothing in this
file is a parameter record.

## Unresolved items

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
  recorded as `arxiv_id` of SRC_DOI_10_1209_0295_5075_AC4F98), Snowmass 2021 Wei Li slides
  (indico.fnal.gov/event/52701/contributions/231920). To be registered only after a fetch.
- **Lead category corrections that do not apply to this family** (no such source in the journal):
  arXiv:2504.21417, arXiv:2503.17727, Topp-Mugglestone thesis (ora.ox.ac.uk), DESY/FNAL/STFC decks, Evian
  papers, LHC-MACHINE-OUTREACH page, ResearchGate profile, arXiv:2610.28252, arXiv:2610.17801. None added.

## Fetch backlog (once network access to these hosts is allowed)

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
