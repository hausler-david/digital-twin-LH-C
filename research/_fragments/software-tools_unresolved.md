# Unresolved items — reconnaissance family `software-tools`

Searches run 2026-10-28 with WebSearch (45 queries, 40 sources surfaced). WebFetch succeeded only on
pypi.org, registry.npmjs.org, launchpad.net, github.com and raw.githubusercontent.com (29 sources marked
`fetched`: PyPI/npm registry JSON, GitHub release/repository pages, one License.txt). Fetches of arxiv.org,
geant4.org, www.pp.rhul.ac.uk, docs.desy.de, fluka-forum.web.cern.ch, hepforge.org hosts,
feynrules.irmp.ucl.ac.be, dev.opencascade.org, root.cern and hepdata.net failed (11 sources marked `blocked`;
their values come from search snippets or secondary pages). Nothing in this family is a collider parameter:
every `snippet-quoted` line in `software-tools_sources.yaml` is a software version / licence / install-route
lead for `docs/software_inventory.md`, and snippet-level evidence is capped at confidence `medium`
(CLAUDE.md §1.5). No file was archived (`archived_file: null` everywhere); nothing was installed or executed.

## Unresolved items

### From the journal (verbatim scope, one bullet per item)

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

### Added by the research-log builder (process items)

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

## Fetch backlog (once network access is allowed)

Each item: URL → what to extract and what it unblocks. Primary/official pages first, then arXiv abstract pages.

### Official project / licence pages (currently blocked)

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

### arXiv abstract pages (blocked; needed to verify dates, journal references, licences, categories)

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
