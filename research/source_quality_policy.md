# Source quality policy — LHμC-VirtualLab

**Document date:** 2026-10-28 · **Status:** binding (referenced by `CLAUDE.md` §1.5 and by
`tests/unit/test_registry_integrity.py`) · **Companion:** `docs/internet_research_protocol.md` (how sources are found
and logged), `docs/uncertainty_policy.md`, `schemas/provenance.schema.json` (`$defs/source_category`,
`$defs/access_mode`, `$defs/provenance_status`, `$defs/confidence`) · **Addendum 2026-10-29:** access mode `fetched_text`
(§1, §2, §3, §4, §6, §8, §9).

"Sources are not equal." This policy says what each of the nine source categories is, which provenance status a
value taken from it may carry, how confidence is capped, how unrefereed slides are treated and where conflicts go.
It contains no collider parameter.

---

## 1. Two independent axes: category and access

Every source in `research/source_registry.yaml` carries a **category** (who wrote it and how it was reviewed) and an
**access** mode (what this project actually read). Both are needed to decide what a value may be used for:

- the *category* bounds the provenance **status** a value can carry (§2–3);
- the *access* mode bounds the **confidence** and forbids `reported_lhmuc` for anything not read in full (§4).

Access modes (`uploaded | fetched | snippet_only | blocked | pending_fetch`) are defined in
`docs/internet_research_protocol.md` §5. On the document date the only sources read in full are the five uploads
plus the PyPI/npm/GitHub/Launchpad pages of the `software-tools` family; everything else is snippet-level.
*[2026-10-29, owner decision: there is a sixth mode, `fetched_text`. It means read in full through the owner-authorised
alphaXiv connector, but as delivered text only, with no PDF and no page images. It is therefore capped at `medium`
(§4); details in `docs/internet_research_protocol.md` §5a.]*

---

## 2. The nine categories

| Category | Definition | Examples in this project | Highest provenance status it may back | Typical `applicability.category` |
|---|---|---|---|---|
| `PRIMARY_LHMUC` | Written by the LHμC proponents (HELP4CERN Study Group and the groups presenting at its workshops) *about the LHμC*: proceedings, preprints, workshop slides, the future White Paper. | `SRC_ARXIV_2610_35154` (Piotrzkowski, PoS DIS2026, arXiv:2610.35154); `SRC_WS1681458_DAGLI_NUCLEUS`; `SRC_WS1681458_KHANPOUR_GAMMAGAMMA`; `SRC_WS_LEBOHO_KUMAR_DIHIGGS`; snippet-level: `SRC_URL_SAIP2026_653_NKADIMENG_DIHIGGS` | `reported_lhmuc` (only if `access` is `uploaded`/`fetched`; *2026-10-29:* or `fetched_text`, then confidence ≤ `medium`) | `direct` |
| `OFFICIAL_CERN` | CERN design reports, TDRs, Yellow Reports, official accelerator web pages and CERN-maintained software repositories. | `SRC_URL_CERN_2020_010_HLLHC_TDR`; `SRC_DOI_10_5170_CERN_2004_003_V_1` (LHC Design Report Vol. 1); `SRC_URL_GITHUB_MADX` | `imported_related` (HL-LHC/LHC beam parameters the LHμC reuses) | `design_variant` or `analogous`, with the explanation naming the machine |
| `PEER_REVIEWED` | Journal articles that passed peer review, on related machines, enabling technology or theory. | `SRC_ARXIV_2506_15445` is both peer-reviewed (PTEP 2026 033C04) and `RELATED_MACHINE`; `SRC_ARXIV_2007_14491` (LHeC 2020 update); `SRC_ARXIV_2101_10476` (physics potential of a μp collider) | `imported_related` or `analogous`; for theory benchmarks the original study in `theory/benchmarks/*/proposal.yaml` | `design_variant`, `analogous` |
| `CONFERENCE_PROCEEDING` | Refereed or editor-reviewed proceedings (JACoW, PoS, EPJ WoC) **and** the slide decks of conferences and workshops outside the HELP4CERN study. | `SRC_JACOW_IPAC2021_MOPAB005` (LHC oxygen pilot run); `SRC_JACOW_IPAC2026_MOP1054`; `SRC_INDICO_1522800_6986580` (ICHEP 2026 LHμC listing — proponents' talk, but recorded by the scout as a conference listing; see §5) | `imported_related` / `analogous` | as `PEER_REVIEWED` |
| `OFFICIAL_SOFTWARE_DOCUMENTATION` | Documentation, repository, package index or licence file of a software tool at a stated version. | `SRC_URL_PYPI_CPYMAD`; `SRC_URL_LAUNCHPAD_MG5AMCNLO`; `SRC_URL_PYPI_PYTHIA8MC`; `SRC_URL_GITHUB_YEFETU_ALOHEP` | none for collider parameters; backs version/licence/model statements in the software inventory and in run metadata | n/a |
| `RELATED_MACHINE` | Documents describing a *different* machine whose design the LHμC inherits or reuses: μLHC, μTRISTAN, LHeC/PERLE, HL-LHC, earlier μp proposals. | `SRC_ARXIV_2506_15445` (μLHC); `SRC_ARXIV_2406_02647` (μTRISTAN-based μ⁺-hadron colliders); `SRC_ARXIV_2206_00037` (review of μp proposals); `SRC_ARXIV_2503_17727` (LHeC bridge project); `SRC_URL_HAL_02283606` (PERLE) | `imported_related` | `design_variant` (same concept, other parameter set) or `analogous` |
| `ANALOGOUS_TECHNOLOGY` | Documents on a technology the LHμC would adopt, developed for another purpose: IMCC/MAP nozzle and MDI, J-PARC ultra-slow muons, FFA rings (ISIS-II, FETS-FFA, EMMA). | `SRC_ARXIV_2605_25580` (hybrid target for ultraslow-muon production); `SRC_DOI_10_1103_PHYSREVLETT_74_4811` (laser-ionised thermal muonium, PRL 74 4811); `SRC_JACOW_EPAC2008_THPP004` (EMMA); `SRC_URL_PASJ2023_WEOB3` (ISIS-II) | `analogous` | `analogous` or `screening_only` |
| `SECONDARY_SOURCE` | Reviews, compilations, outreach pages, indexing records, theses and news that restate primary material. | `SRC_URL_PDG_2020_REV_HEP_COLLIDER_PARAMS`; `SRC_URL_LHC_MACHINE_OUTREACH_VITAL_STATISTICS`; `SRC_URL_INSPIRE_AUTHOR_993289`; `SRC_URL_RESEARCHGATE_ZIMMERMANN_PROFILE`; `SRC_URL_ORA_OXFORD_TOPP_MUGGLESTONE_THESIS` | **none** — may only point to a primary source to fetch | n/a |
| `UNVERIFIED` | Record whose identity, content or relevance could not be confirmed (title-only hits, unidentified files). | `SRC_ARXIV_2610_28252`; `SRC_ARXIV_2610_17801`; `SRC_URL_INSPIRE_FILE_7BCD989A_IMCC_ACCEL_CHAIN`; `SRC_URL_KEK_INDICO_346_HOKKAIDO_2026` | **none** | n/a |

A source keeps one category. Where two apply (μLHC: `PEER_REVIEWED` and `RELATED_MACHINE`) the category that
determines *use* wins — here `RELATED_MACHINE`, because the statuses it can back are the stricter constraint —
and the other property is recorded in `version`/`notes` ("PTEP 2026 033C04").

---

## 3. Category → provenance status

| Provenance status (`CLAUDE.md` §1.3) | Admissible source categories | Additional requirements |
|---|---|---|
| `reported_lhmuc` | `PRIMARY_LHMUC` only | `access` ∈ {`uploaded`, `fetched`} (*2026-10-29:* or `fetched_text`, owner decision; then confidence ≤ `medium` and the note "not checked against page images"); page, table/figure/equation and **verbatim** quotation; `applicability.category: direct` |
| `derived_lhmuc` | computed from `reported_lhmuc` inputs | `derivation` naming every input `parameter_id`; reproduced in `tests/scientific` |
| `imported_related` | `RELATED_MACHINE`, `OFFICIAL_CERN`, `PEER_REVIEWED`, `CONFERENCE_PROCEEDING` | source, page, quotation; `applicability.explanation` names the machine the value belongs to. A value the μLHC paper *itself* imports (μTRISTAN source yield, LHeC ERL, HL-LHC protons) stays `imported_related` and the explanation says "as quoted by arXiv:2506.15445 from …" |
| `analogous` | `ANALOGOUS_TECHNOLOGY` (and `PEER_REVIEWED`/`CONFERENCE_PROCEEDING` about such technology) | as above; `applicability.category: analogous`; an assumption record when the value is used as an LHμC input |
| `analytical_estimate` | any read source for the *formula*; inputs by their own ids | `derivation` string; formula reference |
| `synthetic` | no source backs the value | assumption record with a range or distribution (`schemas/assumption.schema.json`), visible everywhere the value appears |
| `scan_variable` | n/a | range declared in the scan definition |
| `unknown` | n/a | `value: null` |

`SECONDARY_SOURCE` and `UNVERIFIED` back **no** status. Their only legitimate roles are (a) `discovered_by_queries`
provenance, (b) `unresolved_questions` that name the primary document to fetch, (c) `sources_inspected` in an
assumption record, documenting that the search was done.

---

## 4. Confidence caps

`confidence` ∈ {`high`, `medium`, `low`, `none`} describes how far the recorded value can be trusted *as a statement
of what the source says and means for the LHμC*. Caps combine (the lowest applies):

| Condition | Cap |
|---|---|
| source `access` is `snippet_only`, `blocked` or `pending_fetch` | `medium` (`CLAUDE.md` §1.5; test `test_snippet_sources_capped_confidence`) |
| *2026-10-29:* source `access` is `fetched_text` (connector-delivered text read in full; no PDF, no page images) | `medium`; `notes` say "not checked against page images"; no figure reads; integer PDF page from the saved page-tagged text (validator; `tests/unit/test_fetched_text_rules.py`) |
| *2026-10-29:* `derived_lhmuc` or `analytical_estimate` with an input (dependency or id in `derivation`) whose source is not `uploaded`/`fetched` | `medium`, inherited (validator, `lhmuc.registry.capped_inputs`) |
| source is unrefereed slides (§5), value read in full | `medium`, unless the same value also appears in a refereed `PRIMARY_LHMUC` text, in which case the refereed text is cited and `high` is allowed |
| status `imported_related` from a `design_variant` (e.g. μLHC β*, emittance used for LHμC optics) | `medium` |
| status `analogous` | `medium`; `low` when the analogy requires rescaling (energy, aperture, material) |
| source labelled by itself as example, preliminary, draft or "in preparation" (DIS2026 Table 1 "Example of the LHμC parameters"; White Paper working points "in preparation" on `SRC_WS1681458_KHANPOUR_GAMMAGAMMA` p.4) | `high` is allowed for *what the source says*, but `applicability.explanation` must carry the label and `notes` must say the value is not a specification |
| value appears in a search tool's paraphrase rather than quoted text | `low`, and it is a lead, not a value |
| competing values exist in `research/source_conflicts.yaml` and no treatment has been decided | `low` for every competitor until the conflict record names a treatment |
| `synthetic` | `low` or `none`; the range, not the confidence, carries the information |

`high` therefore requires: category admissible for the status, `access` `uploaded`/`fetched` (never `fetched_text`),
verbatim quotation with page, no unresolved conflict, and — for `reported_lhmuc` — a `PRIMARY_LHMUC` text.

---

## 5. Unrefereed workshop slides

Three of the four `PRIMARY_LHMUC` uploads are slide decks from the Kraków workshop (Indico 1681458, 24–26 September
2026) and were never refereed. Rules:

1. They **may** back `reported_lhmuc` when uploaded or fetched and read in full, because they are the proponents'
   own statements about the LHμC — nothing more authoritative exists for ion beams (`SRC_WS1681458_DAGLI_NUCLEUS`
   p.10–14), the White Paper working points (`SRC_WS1681458_KHANPOUR_GAMMAGAMMA` p.4) or the di-Higgs analysis
   set-up (`SRC_WS_LEBOHO_KUMAR_DIHIGGS` p.6–16).
2. Confidence is capped at `medium` (§4), `source_type: workshop_talk`, and `version` records "slides, N pages"
   and the Indico contribution id when known. Where the link between a deck and an Indico contribution is
   inferred (the di-Higgs deck's file name versus contribution 7263322), `version` says "relation inferred, not
   verified".
3. Numbers read from a slide table are quoted with the slide number as `page` and the table/plot caption as
   `table_figure_or_equation`; numbers read off a plot axis are `analytical_estimate` with the reading method in
   `derivation`, never `reported_lhmuc`.
4. A deck that restates another document (the Nucleus-Options μ⁺ table restates μLHC post-erratum values) is cited
   for *its own* statement; the restated value also gets its own record from the original document, and the two are
   linked through `research/source_conflicts.yaml` if they differ.
5. Slides that cite a non-public document ("Table 1 of the draft", "HELP4CERN White Paper, in preparation") are the
   source of record until that document appears; the dependency is written in the source's `unresolved_questions`
   and in the parameter's `notes`, and a benchmark proposal built on such a deck keeps `review_state: extracted`
   (`schemas/proposal.schema.json`) until the public text is read.
6. Workshop talks by **non-proponents** (IMCC, ISIS-II, Snowmass decks) are `CONFERENCE_PROCEEDING` or
   `ANALOGOUS_TECHNOLOGY`, never `PRIMARY_LHMUC`, however relevant.

---

## 6. Secondary and unverified material

- A `SECONDARY_SOURCE` value is never copied into a parameter even when it is the only number available; the
  parameter stays `unknown` (`value: null`) and the secondary hit is listed in the fetch backlog
  (`docs/internet_research_protocol.md` §10).
- `UNVERIFIED` records are promoted only after their abstract page or full text has been read; until then they
  carry no category decision beyond the snippet title. Example: arXiv:2610.28252 and arXiv:2610.17801 were
  identified by title only on 2026-10-28 and are `pending_fetch` candidates for theory benchmarks A and B.
  *[2026-10-29: a full read through the connector (`fetched_text`) is enough to decide the category, taken from the
  delivered text's own front matter. Since 2026-10-29 the validator rejects any `reported_lhmuc`, `imported_related`
  or `analogous` record that cites an `UNVERIFIED` source.]*
- Name collisions are flagged in `notes`: "LHmuC" in arXiv:2203.06258 and the Snowmass 2021 muon-ion-collider
  slides denotes a different concept (3 TeV muon-collider beam on LHC protons), not the HELP4CERN LHμC.

---

## 7. Conflicts

Conflicts are recorded, not resolved by averaging (`CLAUDE.md` §1.6). Pointers:

- **Where**: `research/source_conflicts.yaml`, schema `schemas/conflict.schema.json` (`conflict_id` `CONF_…`,
  `affected_parameters`, `competing_values` each with its source, `possible_cause`, `selected_treatment`,
  `effect_on_simulations`, `required_future_evidence`). The file is named in `CLAUDE.md` §2 and
  `docs/architecture.md` §3; it is created when the first conflict record is written.
- **What counts as a conflict**: two read sources giving different values for the same quantity in the same
  scenario; a document and its erratum; a document and a later version; a snippet and the read text (recorded with
  the snippet as `low`-confidence competitor so the discrepancy stays visible).
- **Treatments** available: separate scenarios (the default — hence the document tags `_DIS2026`, `_MULHC`, `_NUCL`,
  `_WP`, `_DIHIGGS` on parameter ids), propagated uncertainty (`docs/uncertainty_policy.md`), or explicit selection
  of the higher-ranked source with the reason written down.
- **Known open conflicts on the document date** (to be written as `CONF_…` records): three circulating LHμC
  parameter sets (500 GeV/3.74 TeV, 1 TeV/5.3 TeV, 1–2 TeV/5.3–7.5 TeV); μLHC pre- versus post-erratum luminosities;
  HL-LHC bunch numbers 2760/2748/2808; MAD-X licence statements; the luminosity-model discrepancy documented in
  `docs/limitations.md` §5 (reported values reproduced only with hourglass factor H = 1 while the μLHC-like optics
  give H ≈ 0.53 with an assumed 7.5 cm proton bunch).

---

## 8. Checklist before a source backs a value

1. Category assigned from the document's own metadata, not from a search summary.
2. `access` is `uploaded` or `fetched`, and the whole document was read (*2026-10-29:* or `fetched_text`: the whole
   delivered text was read and passed the checks of `docs/internet_research_protocol.md` §5a; then item 5 caps it at
   `medium`).
3. The status requested is admissible for the category (§3); `reported_lhmuc` ⇒ `PRIMARY_LHMUC`.
4. Page, table/figure/equation and verbatim quotation copied; units pint-parseable (`lhmuc/units.py`).
5. Confidence set to the lowest applicable cap (§4); slide-deck values ≤ `medium`. Since 2026-10-29 `uv run python -m lhmuc validate` reports every record above a mechanical cap (synthetic, analogous, imported_related from a design_variant, source not read in full, unrefereed slides) as an error; `tools/apply_confidence_caps.py` lowers them. The conflict cap is still applied by hand.
6. Any competing value found in the registry or fragments → conflict record, not a choice.
7. `research/source_registry.yaml` entry complete (licence, SHA-256 if archived — for `fetched_text` the SHA-256 of
   the saved delivered text —, `discovered_by_queries`), fragments merged, `uv run python -m lhmuc validate`,
   `uv run python tools/check_fetched_text_quotes.py` and `uv run pytest` pass.

---

## 9. Change log

| Date | Change |
|---|---|
| 2026-10-28 | First version: nine categories with project examples, category→status mapping, confidence caps, slide rule, secondary/unverified rule, conflict pointers, checklist. |
| 2026-10-29 | §4 caps enforced by the validator (`lhmuc/registry.py::confidence_cap`). 1088 committed records were above a cap (594 analogous, 367 slide values, 127 imported_related from a design_variant) because extraction briefs had allowed `high` for any value read directly from a page; all were lowered from `high` to `medium` without other changes. List: `research/_fragments/confidence_caps_applied_2026-10-29.csv`. |
| 2026-10-29 | Access mode `fetched_text` (owner decision; `docs/internet_research_protocol.md` §5a): cap `medium`, mandatory note "not checked against page images", no figure reads, integer PDF page; may back `reported_lhmuc` for `PRIMARY_LHMUC` texts. The validator now also enforces the read-in-full rule for `reported_lhmuc`, the UNVERIFIED half of the §3 rule, the caps on material records and the cap a derived record inherits from its inputs (0 records affected on that date). The SECONDARY_SOURCE half of §3 is not enforced yet: one record, `PHYS_MUON_TURNS_PER_LIFETIME_FORMULA_DUDKO2026` (status `analogous`), cites the SECONDARY_SOURCE `SRC_ARXIV_2607_16904`; re-categorise the source or re-label the record before extending the rule. |
