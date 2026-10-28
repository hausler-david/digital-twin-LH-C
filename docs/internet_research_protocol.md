# Internet research protocol — LHμC-VirtualLab

**Document date:** 2026-10-28 · **Status:** binding Phase 0 procedure (companion to `CLAUDE.md` §1.5, §4 and
`research/source_quality_policy.md`) · **Author:** documentation pass on behalf of the project owner (David Hausler).

This document fixes *how* evidence is searched for, recorded, archived and admitted into the parameter
database. It does not contain any collider parameter. Every numeric statement about the LHμC lives in
`parameters/**/*.yaml` with a provenance record; this protocol only governs how such a record may come
into existence.

---

## 1. Why a protocol is needed

The LHμC (HELP4CERN Study Group; K. Piotrzkowski, PoS DIS2026, arXiv:2610.35154, `SRC_ARXIV_2610_35154`)
is a very young proposal: one proceedings contribution, one predecessor journal paper (μLHC, Akturk et al.,
PTEP 2026 033C04, arXiv:2506.15445, `SRC_ARXIV_2506_15445`), one invitation-only workshop (CERN Indico
event 1681458, Kraków, 24–26 September 2026) and a White Paper that is "in preparation" and not public.
Most of the engineering numbers one would want for a digital twin do not exist yet, and the few that exist
are spread over slides and preprints that change between versions (the μLHC luminosities were corrected by
an erratum; three distinct LHμC parameter sets circulate — see §9).

Under these conditions the dominant risk is not a wrong number but an *unsourced* or *mis-sourced* one.
The protocol therefore makes the search itself part of the evidence: what was asked, what was found, what
was actually read, and what remains open.

---

## 2. Mandatory research procedure

### 2.1 Research topics (master prompt §3, as operationalised in the nine reconnaissance families)

Every topic below is searched before any value for it is admitted as anything other than `unknown`. The
family name is the value of the `family` column in the search log (§3) and the prefix of the fragment files
in `research/_fragments/`.

| # | Family | Topic as searched | Typical target quantities |
|---|---|---|---|
| 1 | `lhmuc-primary` | HELP4CERN / LHμC itself: DIS2026 paper, Kraków workshop contributions, ICHEP 2026 (Natal) and AGH seminar listings, White Paper, help4cern.web.cern.ch | beam energies, √s, luminosity, bunch structure, ring circumferences, IR and detector statements |
| 2 | `mulhc-mutristan` | μLHC (arXiv:2506.15445 and erratum), μTRISTAN (arXiv:2201.06664), earlier μp-collider proposals, AloHEP | β*, emittance, bunch length, bunch numbers, booster survival, luminosity formulae and tools |
| 3 | `ultracold-source` | J-PARC/KEK ultra-slow (ultra-cold) μ⁺ source: muonium formation, laser ionisation, hybrid/hot-tungsten targets, yields and emittance | μ⁺ rate, emittance, repetition rate, proton-driver power, source efficiency |
| 4 | `vffa-acceleration` | vertical FFA / FFAG rapid acceleration (ISIS-II, FETS-FFA, EMMA), RCS alternatives, Topp-Mugglestone thesis | acceleration time, turns, gradients, apertures, survival |
| 5 | `lhec-erl` | LHeC energy-recovery linac and IR (CDR 2012, 2020 update, 2025 "bridge project"), PERLE | ERL energy per pass, L*, β*, Q1 gradient and aperture, crossing angle |
| 6 | `muon-collider-mdi` | IMCC / MAP machine–detector interface: tungsten nozzle, BIB, L*, shielding materials | nozzle geometry and materials, L*, background levels |
| 7 | `lhc-hl-lhc-protons` | LHC / HL-LHC proton and ion beam parameters (design reports, TDR, operation papers, ion runs with Pb/Xe/O/Ne) | N_p, ε_n, bunch numbers, bunch length, ion species parameters |
| 8 | `theory-benchmarks` | BSM and SM benchmark studies to recast for μ⁺p (HNL, 2HDM+VLQ, di-Higgs, two-photon physics) and their UFO models | cross sections, model files, cuts, luminosities assumed |
| 9 | `software-tools` | optics, transport, generator, PDF, geometry, statistics and optimisation software: versions, licences, install routes | version pins and licences for `docs/software_inventory.md` (named in `CLAUDE.md` §5; to be written) |

A topic that is *not* covered by a family (e.g. cryogenics, civil engineering, cost) is added as a new family
with its own fragment triple before any search runs; it is never searched "on the side".

### 2.2 Source priority order (1 = highest)

When several sources could back the same quantity, the highest-ranked one that was **read in full**
(`access: uploaded | fetched`) is used; lower-ranked sources are kept as competing values in
`research/source_conflicts.yaml` (schema `schemas/conflict.schema.json`), never discarded and never averaged
(`CLAUDE.md` §1.6). Access mode always dominates rank: a rank-1 source seen only as a snippet ranks below a
rank-5 source that was read (see §5).

| Rank | What | Category (`research/source_quality_policy.md`) | Project example |
|---|---|---|---|
| 1 | Refereed or proceedings text written by the LHμC proponents (HELP4CERN) | `PRIMARY_LHMUC` | `SRC_ARXIV_2610_35154` (arXiv:2610.35154, PoS DIS2026) |
| 2 | Unrefereed LHμC workshop slides and talks by the proponents | `PRIMARY_LHMUC` | `SRC_WS1681458_DAGLI_NUCLEUS`, `SRC_WS1681458_KHANPOUR_GAMMAGAMMA`, `SRC_WS_LEBOHO_KUMAR_DIHIGGS` |
| 3 | CERN official design/technical reports and Yellow Reports (LHC Design Report, HL-LHC TDR, LHeC CDR) | `OFFICIAL_CERN` | `SRC_URL_CERN_2020_010_HLLHC_TDR`, `SRC_DOI_10_5170_CERN_2004_003_V_1` (both still `blocked`) |
| 4 | Peer-reviewed journal articles on the related machines or the enabling technology | `PEER_REVIEWED` / `RELATED_MACHINE` | `SRC_ARXIV_2506_15445` (μLHC, PTEP 2026 033C04); `SRC_ARXIV_2007_14491` (LHeC 2020 update, `blocked`) |
| 5 | Refereed conference proceedings (JACoW, PoS, EPJ Web of Conferences) | `CONFERENCE_PROCEEDING` | `SRC_JACOW_IPAC2021_MOPAB005`, `SRC_JACOW_IPAC2026_MOP1054` (`blocked`) |
| 6 | arXiv preprints without a refereed version, by the relevant collaborations | `RELATED_MACHINE` / `ANALOGOUS_TECHNOLOGY` | `SRC_ARXIV_2406_02647` (μTRISTAN-based μ⁺-hadron colliders), `SRC_ARXIV_2605_25580` (hybrid target for ultraslow muons) |
| 7 | Official software documentation and repositories of the pinned version | `OFFICIAL_SOFTWARE_DOCUMENTATION` | `SRC_URL_PYPI_CPYMAD`, `SRC_URL_LAUNCHPAD_MG5AMCNLO`, `SRC_URL_GITHUB_YEFETU_ALOHEP` (all `fetched`) |
| 8 | Workshop talks and theses outside the HELP4CERN study (IMCC, MAP, ISIS-II, Snowmass) | `CONFERENCE_PROCEEDING` (talks) / `SECONDARY_SOURCE` (theses, as classified by the lead) | `SRC_URL_ORA_OXFORD_TOPP_MUGGLESTONE_THESIS` (`blocked`) |
| 9 | Review articles and parameter compilations (PDG collider-parameter review, review of μp proposals) | `SECONDARY_SOURCE` / `RELATED_MACHINE` | `SRC_URL_PDG_2020_REV_HEP_COLLIDER_PARAMS`, `SRC_ARXIV_2206_00037` |
| 10 | Outreach pages, institutional profiles, indexing records (INSPIRE profile, ResearchGate, LHC outreach) | `SECONDARY_SOURCE` | `SRC_URL_LHC_MACHINE_OUTREACH_VITAL_STATISTICS`, `SRC_URL_INSPIRE_AUTHOR_993289` |
| 11 | Records whose identity or content could not be confirmed | `UNVERIFIED` | `SRC_ARXIV_2610_28252`, `SRC_ARXIV_2610_17801`, `SRC_URL_INSPIRE_FILE_7BCD989A_IMCC_ACCEL_CHAIN` |

Ranks 9–11 may never back a baseline value; they may only point to a higher-ranked source to fetch
(`research/source_quality_policy.md` §3).

### 2.3 Tool-documentation rule

Any statement about a software tool (version, licence, physics model, default, unit convention, API) must come
from the tool's **own documentation or repository at the version that is pinned** (`OFFICIAL_SOFTWARE_DOCUMENTATION`,
rank 7), fetched and read, with the retrieval date recorded. An LLM's recollection of a manual is not a source.
Where the official documentation was not reachable (Geant4, BDSIM, FLUKA, LHAPDF, ROOT on 2026-10-28, see
`docs/limitations.md` §4), the inventory entry stays `pending_fetch` and the tool is **not** adopted. Licence
statements are copied verbatim with their URL; contradictory licence statements (e.g. MAD-X: custom CERN licence
in `License.txt` versus "MIT" in a package index, `SRC_URL_GITHUB_MADX`) are recorded as a conflict, not resolved by
choice.

### 2.4 Step sequence (every research session)

1. **Plan** – list the family, the target quantities and ≈20 queries per family *before* searching. Record the
   plan in the family's `_unresolved.md` if it cannot be completed (budget, blocked hosts).
2. **Search** – run each query with the available tool (`WebSearch` in this environment). One log row per
   (query, candidate source) pair, including rows with `useful = false`, so that negative results are visible.
3. **Classify** – assign `source_type`, `category` and provisional rank to each candidate from its *own* metadata
   (venue, authors, DOI), never from the search tool's summary alone. Collisions with existing ids are checked in
   `research/source_registry.yaml` first.
4. **Fetch and read in full** – attempt the fetch; on success read the whole document (all pages for a PDF), on
   refusal record `access: blocked`. A document that was only seen as a snippet keeps `access: snippet_only`.
5. **Archive** – §6.
6. **Extract** – write parameter records only from `uploaded`/`fetched` sources, with page, table/figure and
   verbatim quotation. Snippet text goes into `notes` as "snippet-quoted: … (to verify)", never into a parameter.
7. **Log** – the search-log rows (§3), the source-registry entries (§4) and the unresolved items go into the
   family fragment (`research/_fragments/<family>_search_log.csv`, `<family>_sources.yaml`, `<family>_unresolved.md`);
   `uv run python tools/merge_research_fragments.py` merges them into `research/search_log.csv` and
   `research/source_registry.yaml` (the five hand-authored upload entries win on id collision).
8. **Validate** – `uv run python -m lhmuc validate` and `uv run pytest` (tests
   `test_primary_sources_are_uploaded_or_fetched` and `test_snippet_sources_capped_confidence` in
   `tests/unit/test_registry_integrity.py` enforce the access rules mechanically).
9. **Report** – the §49 status report names every host that was blocked and every lead left unverified.

---

## 3. Search-log schema (`research/search_log.csv`)

The canonical log is produced by `tools/merge_research_fragments.py` from the per-family fragments; the column
list is `COLS` in that script. One row = one (query, discovered source) pair; a query that found nothing useful
still gets one row with `useful = false` and an empty `source_discovered`.

| Column | Content |
|---|---|
| `search_date` | ISO date the query ran |
| `family` | reconnaissance family (§2.1) |
| `query` | the query string exactly as issued |
| `tool` | `WebSearch`, `WebFetch`, `user upload`, `manual` |
| `useful` | `true`/`false` – whether the row produced a candidate worth registering |
| `source_discovered` | `<source_id> — <title>`; the id must match an entry in the source registry |
| `source_type` | enum of `schemas/source.schema.json` (`journal_article`, `arxiv_preprint`, `conference_proceeding`, `workshop_talk`, `official_report`, `thesis`, `software_repository`, `software_documentation`, `web_page`, `dataset`, `white_paper`) |
| `source_authority` | category enum (`PRIMARY_LHMUC` … `UNVERIFIED`) |
| `publication_date` | as stated by the source; empty if unknown |
| `version` | arXiv version, erratum status, event/contribution ids |
| `url` | canonical URL |
| `access_date` | date of the fetch attempt |
| `access_mode` | `uploaded`, `fetched`, `snippet_only`, `blocked`, `pending_fetch` (§5) |
| `relevance` | why the source matters, plus a "journal note" on what the query did and did not surface |
| `parameters_extracted` | either `none`/`NONE as parameter records` or the ids written; snippet-quoted leads are labelled as such |
| `unresolved_questions` | what the fetch must settle (speaker attribution, version, licence, conflicting numbers) |
| `licensing_considerations` | licence as seen, or "not stated in snippets; to be checked on fetch" |
| `local_archived_filename` | repository path of the archived copy, or empty |

---

## 4. Source-registry schema (`research/source_registry.yaml`, `schemas/source.schema.json`)

Top-level key `sources:`; `additionalProperties: false`. Required: `source_id`, `title`, `source_type`,
`category`, `url`, `access_date`, `access`, `relevance`.

| Field | Rule |
|---|---|
| `source_id` | `^SRC_[A-Z0-9_]+$`; conventions in `CLAUDE.md` §3 (`SRC_ARXIV_<id, dots→underscores>`, `SRC_INDICO_<event>_<contribution>`, `SRC_DOI_<slug>`, `SRC_URL_<slug>`, `SRC_WS1681458_<SPEAKER>_<TOPIC>`); the fragments additionally use `SRC_JACOW_<conference>_<paper code>` for JACoW proceedings |
| `title`, `authors_or_org` | as printed on the document; a presenter is named as such |
| `source_type` | enum, see §3 |
| `category` | one of the nine categories; the lead's correction overrides the scout's classification and is noted in `notes` |
| `publication_date`, `version` | as stated; `version` carries arXiv version, erratum status, event ids, "slides, N pages" |
| `url`, `doi`, `arxiv_id` | canonical identifiers; `null` when absent |
| `access_date`, `access` | date and mode of the last attempt (§5) |
| `relevance` | one paragraph: what the source gives this project |
| `parameters_extracted` | list of `parameter_id`s that cite this source; empty is allowed and is the state of all entries on the document date |
| `unresolved_questions` | list; every snippet-level lead and every licence or version doubt |
| `licence`, `archived_file`, `sha256` | §6; `null` until known |
| `discovered_by_queries` | the exact query strings (or `user upload`) that surfaced the source |
| `notes` | read status ("Read in full (N pages)"), lead decisions, snippet-quoted leads |

Each archived document additionally has `research/archived_metadata/<source_id>.json` (title, venue, identifier,
page count, licence, redistribution decision, SHA-256, size, archive date and method, read status); the five
uploads have one each.

---

## 5. Access modes and what each permits

| `access` | Meaning (`provenance.schema.json` `$defs/access_mode`) | May back `reported_lhmuc`? | May back `imported_related` / `analogous`? | Confidence cap | Typical use |
|---|---|---|---|---|---|
| `uploaded` | file supplied by the owner and read in full | yes, if `PRIMARY_LHMUC` | yes | none (set by evidence quality) | the five documents in `references/_local/` |
| `fetched` | downloaded by the session and read in full | yes, if `PRIMARY_LHMUC` | yes | none | PyPI/npm/GitHub/Launchpad pages on 2026-10-28 |
| `snippet_only` | only search-engine snippets seen; text may be the search tool's paraphrase | **no** | only as a *lead*; a value needs its own assumption record or stays `unknown` | `medium` | most 2026-10-28 reconnaissance |
| `blocked` | fetch attempted and refused by network policy | **no** | as `snippet_only` | `medium` | arXiv, Indico, CDS, INSPIRE, PoS, DOI, journals, CERN hosts |
| `pending_fetch` | identified, fetch not yet attempted | **no** | no | `medium` | fetch backlog (§7) |

Rules enforced by tests: a `reported_lhmuc` value must cite a source whose `access` is `uploaded` or `fetched`;
any parameter citing a `snippet_only`/`blocked`/`pending_fetch` source has `confidence` ≤ `medium`.
Snippet-level values are written, if at all, into `notes`/`unresolved_questions` prefixed "snippet-quoted" and never
into `value`.

---

## 6. Archiving rule

1. **Always**: registry entry + `research/archived_metadata/<source_id>.json` with SHA-256 (`sha256sum`), size,
   licence as stated *in the document*, archive date and method, and read status. A hash is recorded even for a
   file that cannot be redistributed, so that any later copy can be verified.
2. **File committed only if the licence permits redistribution.** Today only `SRC_ARXIV_2610_35154` (CC BY-NC-ND 4.0
   stated on its page 1) is committed, unmodified, as
   `references/primary/arXiv-2610.35154v1_Piotrzkowski_LHmuC_DIS2026.pdf`. The other four uploads
   (μLHC v2, three Kraków decks: licence `null`, not stated) live in git-ignored `references/_local/` and are
   described only by their metadata JSON.
3. Archived files are never edited; a new version is a new file with a new hash and an updated `version` field.
4. Licence metadata on the host (e.g. the arXiv licence badge) is recorded separately from the licence stated in
   the file; when the host is blocked this remains an `unresolved_question` (as it does for all five uploads).

---

## 7. When hosts are blocked

Network policy in the 2026-10-28 sessions returned `ENOTFOUND`/refusals for arxiv.org, export.arxiv.org,
indico.cern.ch, cds.cern.ch, inspirehep.net, pos.sissa.it, doi.org, academic.oup.com, journals.aps.org,
iopscience.iop.org, jacow.org/accelconf, readthedocs and every `*.cern.ch` host; only pypi.org,
registry.npmjs.org, launchpad.net, github.com and raw.githubusercontent.com answered. When that happens:

- **Record** the refusal: `access: blocked` on the source, the host and error in the family `_unresolved.md`
  header, and the row in the search log. Do not retry in a loop and do not route around the policy.
- **Cap** every value that depends on the source at confidence `medium`, keep its status at best
  `imported_related`/`analogous` with an explicit note, or leave it `unknown` with `value: null`.
- **Keep a fetch backlog**: each family `_unresolved.md` lists, per source id, the URL and *what to extract on
  fetch*. The merged list becomes `research/unresolved_searches.md` (named in `CLAUDE.md` §4 and tested for in
  `tests/unit/test_registry_integrity.py`; produced from the fragments).
- **Prefer uploads**: ask the owner to upload the document; an upload read in full is `uploaded` and ranks by its
  category, not by its web accessibility.
- **Never promote** a snippet to a quotation. If a fragment contains a snippet number that later contradicts the
  read document, the read document wins and the snippet is retained in `notes` as the earlier, superseded lead.

---

## 8. Domain allow-list required for this project

To run the protocol without the snippet-only restriction, the session network policy needs the following hosts
(all literature hosts below were blocked on 2026-10-28):

| Group | Hosts |
|---|---|
| Preprints and indexing | `arxiv.org`, `export.arxiv.org`, `inspirehep.net`, `doi.org`, `zenodo.org` |
| CERN documents and events | `indico.cern.ch`, `cds.cern.ch`, `e-publishing.cern.ch`, `accelconf.web.cern.ch`, `help4cern.web.cern.ch`, `muoncollider.web.cern.ch`, `lhec.web.cern.ch`, `geant4.web.cern.ch`, `gitlab.cern.ch` |
| Journals and proceedings | `pos.sissa.it`, `jinst.sissa.it`, `academic.oup.com`, `journals.aps.org`, `iopscience.iop.org`, `link.springer.com`, `jacow.org`, `pdg.lbl.gov`, `ora.ox.ac.uk` |
| Software and documentation | `pythia.org`, `hepforge.org`, `cp3.irmp.ucl.ac.be`, `readthedocs.io`, `github.com`, `bitbucket.org` |
| Muon-source institutions | `g-2.kek.jp`, `www.kek.jp` |

Already reachable and sufficient for the software family: `pypi.org`, `registry.npmjs.org`, `launchpad.net`,
`github.com`, `raw.githubusercontent.com`.

---

## 9. Reconnaissance already performed (2026-10-28)

Measured from `research/_fragments/` on the document date:

- **9 families**, each with a search-log, sources and unresolved fragment: `lhc-hl-lhc-protons`, `lhec-erl`,
  `lhmuc-primary`, `mulhc-mutristan`, `muon-collider-mdi`, `software-tools`, `theory-benchmarks`,
  `ultracold-source`, `vffa-acceleration`.
- **383 search-log rows** covering **210 distinct (family, query) strings**; the families' own headers report
  ≈16–45 queries each (the lead's working figure of ≈160 queries counts planned query families rather than
  variant strings). **245 candidate source records** in the fragment YAMLs (243 distinct ids in the logs).
- Access outcome of the log rows: `blocked` 161, `snippet_only` 117, `fetched` 35 (PyPI/npm/GitHub/Launchpad
  pages, AloHEP README), 70 rows without a candidate. **No literature host was readable**; the only
  `uploaded` sources remain the five documents supplied by the owner.
- Category mix of the 245 fragment records: `CONFERENCE_PROCEEDING` 74, `PEER_REVIEWED` 39, `RELATED_MACHINE` 39,
  `OFFICIAL_SOFTWARE_DOCUMENTATION` 33, `SECONDARY_SOURCE` 21, `OFFICIAL_CERN` 20, `UNVERIFIED` 8,
  `ANALOGOUS_TECHNOLOGY` 6, `PRIMARY_LHMUC` 5 (the DIS2026 paper seen again as a blocked web record, plus the
  SAIP 2026 di-Higgs talk `SRC_URL_SAIP2026_653_NKADIMENG_DIHIGGS`, which is `PRIMARY_LHMUC` by authorship but
  snippet-level and therefore cannot back a `reported_lhmuc` value).
- Findings that shape the parameter database (all snippet-level unless from the uploads):
  three distinct LHμC parameter sets — 500 GeV μ⁺ / √s 3.74 TeV / L > 10³³ (ICHEP 2026 listing), 1 TeV / 5.3 TeV
  / > 10³³ (AGH seminar, May 2026), 1 or 2 TeV / 5.3 or 7.5 TeV / average ≈ 10³⁴ (arXiv:2610.35154) — kept as
  separate scenarios; the name collision "LHmuC" for a different 3 TeV muon-collider-on-LHC concept
  (arXiv:2203.06258); the μLHC erratum (post-erratum 7.2 × 10³³ / 8.8 × 10³³ cm⁻²s⁻¹ as quoted in
  `SRC_WS1681458_DAGLI_NUCLEUS`); HL-LHC bunch-number variants 2760 / 2748 / 2808 by source, preserved as a
  conflict.
- Specific snippet-only leads **not** to be used as inputs until read (`docs/limitations.md` §3): LHeC L* = 15 m,
  β* 10 → 7 cm, Q1A 252 T/m with 20 mm aperture, 6–7 mrad crossing angle versus a head-on 2025 phase-one option;
  IMCC nozzle INERMET180 + borated polyethylene, tip 6 cm from the IP, 10° outer inclination, L* = 6 m at 10 TeV;
  J-PARC ultra-slow-muon design rate ≈ 10⁵ μ⁺/s and emittance < 1 π mm mrad; HL-LHC 2.2 × 10¹¹ p/bunch,
  ε_n 2.5 μm; arXiv:2610.28252 (HNL at a 3 TeV μ⁺μ⁻ collider, 1 ab⁻¹) and arXiv:2610.17801 (one-loop
  A → ZZγ in 2HDM+VLQ) identified by title only, `UNVERIFIED`.

---

## 10. Fetch backlog (highest value first)

1. Kraków workshop (Indico 1681458) contributions cited by arXiv:2610.35154 — vFFA (Topp-Mugglestone), nozzle
   (Kilic), SPS/LHC modifications (Zimmermann), detectors (Yamazaki, Forthomme), near-beam (Acosta),
   pre-acceleration (Otani), source (Rogers, Zhang) — the only route to LHμC-specific IR, nozzle and acceleration
   numbers.
2. μLHC PTEP erratum text and the arXiv licence of arXiv:2506.15445 and arXiv:2610.35154.
3. LHeC CDR (arXiv:1206.2913) and 2020 update (arXiv:2007.14491); HL-LHC TDR (CERN-2020-010); LHC Design Report
   Vol. 1 — to turn `imported_related` proton/ERL/IR numbers from "as quoted by the uploads" into read values.
4. μTRISTAN (arXiv:2201.06664) and the J-PARC ultra-slow-muon papers for the source yield chain.
5. IMCC MDI reports for the nozzle analogy; Geant4/BDSIM/FLUKA licence pages for the software inventory.
6. arXiv:2610.28252 and arXiv:2610.17801 abstract pages to lift them from `UNVERIFIED`.

---

## 11. Change log

| Date | Change |
|---|---|
| 2026-10-28 | First version: procedure, schemas, access modes, archiving, blocked-host handling, allow-list, record of the 2026-10-28 reconnaissance. |
