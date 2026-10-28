# LHμC-VirtualLab — Software inventory

**Document date:** 2026-10-28 · **Project phase:** Phase 0 (evidence and feasibility audit) ·
**Owner:** David Hausler · **Status of this document:** inventory of the tools the master project
prompt (§3) names for later milestones, with the version, licence and install route *seen on
2026-10-28*, and the honest state of this environment. **Nothing in this table has been adopted,
pinned, installed or executed except the core Python stack in §9.** No lattice, geometry, transport,
generator, analysis or optimisation code exists yet (see `docs/limitations.md` §4).

Read `CLAUDE.md` first. CLAUDE.md §5 requires third-party licences to be documented here; CLAUDE.md §1.8
("tools, not the LLM, do the science") is the reason every tool below has an explicit *role* and an
explicit *must-not* column.

---

## 1. How this document was produced and how to read it

### 1.1 Evidence behind every cell

| Mark | Meaning | Where the evidence lives |
|---|---|---|
| **J** | Taken verbatim from the `software-tools` reconnaissance journal (45 WebSearch queries, 40 sources, 2026-10-28). Values are quoted exactly as the journal recorded them; the journal itself summarised PyPI/npm JSON, GitHub release pages, one `License.txt`, and search snippets for blocked hosts. | `research/_fragments/software-tools_sources.yaml`, `research/_fragments/software-tools_search_log.csv`, `research/_fragments/software-tools_unresolved.md` (source_ids `SRC_URL_*`, `SRC_ARXIV_*` below) |
| **J-snippet** | In the journal, but the host was fetch-blocked and the value came from a search snippet or a secondary page. Capped at confidence *medium* (CLAUDE.md §1.5). | same files, source `access: blocked` |
| **P** | Probed in *this* session on 2026-10-28 by an HTTP request to a reachable host (PyPI JSON, raw.githubusercontent.com, conda-forge repodata HEAD). Not in the journal; not archived; no SHA-256 recorded; must be re-fetched and archived before it is pinned. | nowhere in the repository yet — listed in §8 as a to-do |
| **L** | Environment fact stated by the lead for this session (e.g. "PyPI has xsuite 0.67"). Not independently verified here unless a **P** mark follows it. | this document only |
| **E** | Read from the installed environment (`uv pip list`, `importlib.metadata`) in this session. | `uv.lock`, `pyproject.toml` |
| **not verified** | Not in the journal, not probed, not installed. The cell states only that the fact is unknown; it is never filled by recollection. | — |

Software versions and licences are **not collider parameters** and never enter `parameters/**/*.yaml`;
they back only this inventory and future run metadata (`research/source_quality_policy.md` §2, category
`OFFICIAL_SOFTWARE_DOCUMENTATION`).

### 1.2 Host reachability in this environment (probed 2026-10-28)

| Host | Result | Consequence |
|---|---|---|
| `pypi.org` (JSON API) | HTTP 200 (**P**) | pip/uv installs from PyPI are possible |
| `registry.npmjs.org` | HTTP 200 (**P**) | npm packages (three.js, opencascade.js) are resolvable |
| `launchpad.net/mg5amcnlo` | HTTP 200 (**P**) | MadGraph5_aMC@NLO tarball download possible |
| `raw.githubusercontent.com`, `github.com` | HTTP 200 (**P**; `LICENSE`, `VERSION`, `README.md` of `mg5amcnlo/mg5amcnlo` branch `3.x` fetched) | git clones and raw files reachable |
| `conda.anaconda.org/conda-forge` (HEAD on `noarch/repodata.json.bz2`) | HTTP 200 (**P**) | channel answers, but **no conda/mamba binary is installed and no package was resolved**; conda-forge install routes below remain *unverified* |
| `geant4.org`, `arxiv.org`, `herwig.hepforge.org` | proxy refused the CONNECT tunnel (HTTP 403) (**P**) | all CERN hosts, hepforge hosts, arXiv, INSPIRE, Indico, CDS, DOI resolvers and journal sites are blocked (lead's host list confirmed for the three probed) |
| `fluka.cern` | not probed; blocked per lead and per journal (**J**) | FLUKA additionally requires registration "subject to approval" (**J**) |

---

## 2. Accelerator optics and tracking

| Tool | Intended domain | Latest version seen | Licence | Install route | Reachable here | Phase 0 status | Evidence |
|---|---|---|---|---|---|---|---|
| **MAD-X** | Linear/non-linear optics, matching, lattice design (CERN reference code) | "5.09.00 (per LCG Info; GitHub releases section empty)" | **Conflicting:** repository `License.txt` is a custom CERN licence ("MAD-X License: CERN EUROPEAN ORGANISATION FOR NUCLEAR RESEARCH … CERN program library entry: T5001"); "LCG Info says 'MIT License'; CERN gitlab mirror (2011) says EPICS Open License". Treated as **non-free / terms unconfirmed** until the 5.09.00 tag is read. | source (GitHub `MethodicalAcceleratorDesign/MAD-X`); binary bundled inside cpymad wheels | GitHub yes; CERN pages blocked | not installed | **J** (`SRC_URL_GITHUB_MADX`) |
| **cpymad** | Python (Cython) driver for MAD-X | 1.20.0 (requires Python ">=3.10") | PyPI `license_expression`: **"GPL-3.0-or-later AND Apache-2.0 AND LicenseRef-CERN-MADX-Proprietary"**; older listing: "Source: CC0, Apache \| Binary: Non-Free" — i.e. the *wheel* is non-free because it embeds the MAD-X binary | pip (`cpymad`) | PyPI yes | not installed; "cpymad 1.20" available on PyPI (**L**) | **J** (`SRC_URL_PYPI_CPYMAD`) |
| **Xsuite** (`xsuite` umbrella; `xtrack`, `xpart`, `xfields`, `xcoll`, `xobjects`, `xdeps`) | Symplectic tracking, particle ensembles, beam–beam and collective effects; Geant4/BDSIM interface for collimation | xtrack "0.118.5 (released Oct 28, 2026)", xpart 0.23.23, xfields 0.27.6 (**J**); umbrella `xsuite` 0.67.1, `requires_python` "<3.15,>=3.11" (**P**; journal left the umbrella version uncaptured) | xtrack "Apache-2.0" (LICENSE file "Apache License Version 2.0, January 2004"); xpart "Apache 2.0"; xfields "Apache-2.0"; umbrella `license_expression` "Apache-2.0" (**P**) | pip (`xsuite`) | PyPI yes | not installed; "xsuite 0.67" on PyPI (**L**) | **J** (`SRC_URL_PYPI_XTRACK`, `SRC_URL_PYPI_XPART`, `SRC_URL_PYPI_XFIELDS`, `SRC_ARXIV_2310_00317` — arXiv:2310.00317 "The modules are Xobjects, Xpart, Xtrack, Xcoll, Xfields and Xdeps.") + **P** |
| **Bmad / Tao** | Charged-particle optics library and its interactive front end (Cornell CLASSE) | not captured ("conda-forge 'bmad' version not captured") | **not confirmed from the repository** ("raw LICENSE 404 on both main and master"); only a third-party aggregator claim: "Depscope lists the conda package as GPL-3.0-or-later." | conda-forge (`bmad`), not PyPI | channel answers (**P**) but unverified | not installed | **J** (`SRC_URL_GITHUB_BMAD_ECOSYSTEM`) |
| **PyTao** | Python interface to Tao | 1.3.3 (requires Python ">=3.10") | "GPL v3 (full GPLv3 text in license field)" | conda-forge preferred ("conda install -c conda-forge pytao"); also PyPI; "Requires Bmad built with shared libs" | PyPI yes; conda-forge unverified | not installed | **J** (`SRC_URL_PYPI_PYTAO`) |
| **Bmad-X** | Differentiable/PyTorch re-implementation of Bmad element maps (as named in the master prompt) | not verified | not verified | not verified | not probed | not installed | **not verified** — absent from the journal |
| **Cheetah** (`cheetah-accelerator`) | Fast differentiable (PyTorch) beam-optics simulation for ML surrogates and gradient optimisation | 0.8.4 (requires Python ">=3.11") | "GPL v3 (README badge; metadata license field empty)" | pip (`cheetah-accelerator`) | PyPI yes | not installed; "cheetah-accelerator 0.8" on PyPI (**L**) | **J** (`SRC_URL_PYPI_CHEETAH_ACCELERATOR`, `SRC_ARXIV_2401_05815` — arXiv:2401.05815) |
| **BLonD** | Longitudinal beam dynamics (RF, bunching, intensity effects) — CERN code, as named in the master prompt | not verified | not verified | not verified | not probed | not installed | **not verified** — absent from the journal |

**Role in this project / must NOT be used for**

- *MAD-X (via cpymad), Xsuite, Bmad/PyTao* — the optics codes of `lattice/{madx,xsuite,bmad}` (`docs/architecture.md`
  §5–6): Twiss functions, matching, chromaticity, dynamic aperture, IR optics and β* studies, generated from the
  parameter model. They must not be used to assert LHμC lattice *parameters* that no source gives: the LHμC
  lattice is currently **unknown** (`lattice/README.md`), so any deck is a *synthetic* input with an assumption
  record. Cross-checks between at least two codes are required before a P-label above P1 is claimed
  (`docs/validation_plan.md`).
- *MAD-X licence* — because the terms are conflicting (see §10, item 1), MAD-X/cpymad results may be *used*, but the
  binary may not be redistributed by this project, and no derived work may be published as if MAD-X were MIT.
- *BLonD* — longitudinal dynamics of the μ⁺ bunch train and RF system in the booster/main ring, once an RF
  specification exists (none does). Not for transverse optics.
- *Cheetah, Bmad-X* — surrogates and differentiable models for `optimization/gradient` and
  `analysis/machine_learning`. They must not be used as the *reference* optics result; every Cheetah/Bmad-X
  result needs a MAD-X/Xsuite/Bmad reference run in the same run record (surrogate out-of-domain is a
  stop-and-report condition, CLAUDE.md §1.10).

---

## 3. Particle–matter transport and radiation

| Tool | Intended domain | Latest version seen | Licence | Install route | Reachable here | Phase 0 status | Evidence |
|---|---|---|---|---|---|---|---|
| **Geant4** | Detector response, shielding, beam-induced background, nozzle energy deposition | "11.4.3 (GitHub tag v11.4.3, released 01 Oct); 11.4.0 released 2025-12-05" | "Geant4 Software License, Version 1.0 (custom permissive)" ("Version 1.0, 28 June 2006") | source (CMake; CERN GitLab / GitHub mirror); C++ | `geant4.org` blocked (**P**); GitHub mirror reachable | not installed | **J-snippet** (`SRC_URL_GEANT4_LICENSE`) |
| **geant4-pybind** (`geant4_pybind`) | Alternative pybind11 Python bindings for Geant4 | 0.1.3; `requires_python` "<4,>=3.7"; author "Benjamin H."; homepage `github.com/HaarigerHarald/geant4_pybind` | PyPI `license` field "Public Domain" (classifiers empty) — the bindings only; Geant4 itself keeps its own licence | pip (`geant4-pybind`); wheel content and Geant4 version it bundles **not inspected** | PyPI yes | not installed | **P** (journal: "geant4_pybind on PyPI not checked") |
| **BDSIM** | Geant4-based accelerator tracking *with* particle–matter interactions: beam loss, machine-induced background, collimation | "1.7.7 (manual sidebar, per snippet)" | "GNU GPL version 3" ("BDSIM is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License … version 3 of the License.") | source: "git clone --recursive https://bitbucket.org/jairhul/bdsim" (CMake, needs Geant4 + ROOT); required Geant4 version "not captured" | `www.pp.rhul.ac.uk` and bitbucket blocked (**J**) | not installed | **J-snippet** (`SRC_URL_RHUL_BDSIM_MANUAL_LICENCE`, `SRC_ARXIV_1808_10745` — arXiv:1808.10745) |
| **pybdsim** | Python utilities for BDSIM input/output | 3.9.0; `requires_python` ">=3.7"; licence field empty; repository `bitbucket.org/jairhul/pybdsim` | not stated in PyPI metadata — **not verified** | pip (`pybdsim`) | PyPI yes | not installed | **P** |
| **G4beamline** | Geant4-based single-particle beamline tracking (widely used for muon beamlines) | "3.08 / 3.08b (Mu2e wiki); official site not fetched"; "3.08b compatible with Geant4 11.3.2" | "GPL (per DESY listing)" — publisher's own statement not seen | binary download from Muons, Inc.; not PyPI | `g4beamline.muonsinc.com` not reachable (**J**) | not installed | **J-snippet** (`SRC_URL_DESY_MAXWELL_G4BEAMLINE`, category SECONDARY_SOURCE) |
| **FLUKA** | Shielding, activation, dose, hadronic cascades | not captured | "Registration + approval required; FLUKA Single User Licence Agreement"; "Registration as a FLUKA user is subject to approval."; older course material: "free for scientific and academic purposes, ad-hoc agreement for commercial purposes, … may not be used for weapons applications" — current licence text **not verified** | registered download only; not PyPI, not conda-forge | `fluka.cern` blocked; **no account exists** | not installed, not available | **J-snippet** (`SRC_URL_FLUKA_FORUM_REGISTRATION_FAQ`) |

**Role in this project / must NOT be used for**

- *Geant4* — `detector/geant4` Level-2 regional detector simulation, nozzle/shielding energy deposition and
  beam-induced background on the **C — Simulation** geometry (`docs/architecture.md` §7). Must not be run on the
  visual (B) geometry, and must not be used to produce "LHμC background rates" while the IR layout, nozzle
  dimensions and L* are unknown — those inputs are `null` today (`docs/limitations.md`).
- *BDSIM* — `detector/bdsim` and `detector/backgrounds`: machine-induced background, muon-decay electron
  showers along the final-focus, collimation losses. **BDSIM is not an optics design code and must not be used
  for optics** (`lattice/README.md`: "BDSIM is not used for optics design"); its lattice must be *imported* from
  the MAD-X/Xsuite/Bmad deck of the same run record.
- *G4beamline* — candidate for the ultra-cold μ⁺ source and transfer-line stage (muon-beamline tradition); not
  for ring optics, not for detector response.
- *FLUKA* — activation/dose studies; **cannot be planned for** until a registered account exists; until then
  Geant4/BDSIM only, and the μLHC nozzle figure ("19% energy deposited", `SRC_ARXIV_2506_15445`,
  arXiv:2506.15445) cannot be re-derived by this project.
- *geant4-pybind / pybdsim* — scripting glue only; they add no physics and their licence/bundling status is
  not yet inspected.

---

## 4. Event generation, theory models and PDFs

| Tool | Intended domain | Latest version seen | Licence | Install route | Reachable here | Phase 0 status | Evidence |
|---|---|---|---|---|---|---|---|
| **MadGraph5_aMC@NLO** | Matrix-element generation (LO/NLO) for μp signal and background, UFO model import | Launchpad: "3.8.x (MG5_aMC_v3.8.1.tar.gz)", "released on 2026-09-14" (**J**); branch `3.x` `VERSION` file: `version = 3.8.1`, `date = 2026-10-09` (**P**; dates differ — tarball vs. branch head, both kept) | "UoI-NCSA open source license ('Other/Open Source')" (**J**); `LICENSE` on branch `3.x`: "adapted from the University of Illinois/NCSA license", "Copyright (c) 2009, 2013, the MadTeam" (**P**) | tarball from Launchpad or "git clone https://github.com/mg5amcnlo/mg5amcnlo.git -b 3.x"; Python 3 + Fortran/gfortran | Launchpad and GitHub yes (**P**) | not installed; installation *possible* | **J** (`SRC_URL_LAUNCHPAD_MG5AMCNLO`, `SRC_ARXIV_1405_0301` — arXiv:1405.0301) + **P** |
| **Pythia 8** (`pythia8mc`) | Parton shower, hadronisation, MPI; DIS/photoproduction modelling | "8.318.0 (Pythia 8.318)" | "GNU GPL v2 or later" | "pip install pythia8mc" (import `pythia8mc`); source `gitlab.com/Pythia8/releases` | PyPI yes | not installed; "pythia8mc 8.318" on PyPI (**L**) | **J** (`SRC_URL_PYPI_PYTHIA8MC`) |
| **Herwig 7** | Alternative shower/hadronisation generator (systematics) | "Herwig 7.3.0 (LCG lists 7.3.0p1)"; "no evidence of 7.3.x point releases" | "GNU GPL version 3 with MCnet guidelines" | bootstrap script from `herwig.hepforge.org` (needs ThePEG, LHAPDF, …); not PyPI | hepforge blocked (**P**) | not installed, not available here | **J-snippet** (`SRC_ARXIV_2312_05175` — arXiv:2312.05175) |
| **Delphes** | Fast parametric detector simulation | "3.5.1 (Latest); 3.5.2pre02 pre-release"; release year of 3.5.1 not shown | "GPL v3 or later; docs CC BY-SA 4.0" | source (GitHub `delphes/delphes`; C++, needs ROOT) | GitHub yes | not installed (blocked by missing ROOT) | **J** (`SRC_URL_GITHUB_DELPHES_RELEASES`) |
| **FeynRules** | Lagrangian → Feynman rules → UFO export (Mathematica package) | "FeynRules 2.0 (wiki snapshot links feynrules-current.tar.gz labelled 2.3)"; current version unknown | "'Licensing provisions: None' (CPC program summary)"; **requires proprietary Mathematica** ("Mathematica version 7.0 or higher" per the 2.0 paper) | download from `feynrules.irmp.ucl.ac.be` | blocked (**J**) | not installed; no Mathematica licence in this environment | **J-snippet** (`SRC_ARXIV_1310_1921` — arXiv:1310.1921) |
| **SARAH** | Model builder (not only SUSY) generating UFO/SPheno output (Mathematica package) | "SARAH 4 (current version not confirmed)" | "'GNU library public license' per manual"; **requires Mathematica** | download from `sarah.hepforge.org` | hepforge blocked | not installed | **J-snippet** (`SRC_ARXIV_1309_7223` — arXiv:1309.7223) |
| **LHAPDF** | PDF interpolation for MG5/Pythia/Herwig | "6.5.5 (Fedora/Gentoo packaging); PyPI 'LHAPDF' record 6.2.1.post10 (stale, empty metadata)" | "GPL-3.0-only (conda-forge, Fedora); Gentoo lists GPL-2" — conflict kept | conda-forge (`lhapdf`) or source from hepforge; **pip is not a supported route** | hepforge blocked; conda-forge unverified | not installed | **J** (`SRC_URL_GITHUB_CONDA_FORGE_LHAPDF_FEEDSTOCK`) |
| **pylhe** | Reading LHE files (MG5 output) into Python | 2.1.0 (requires Python ">=3.10") | "Apache-2.0" | pip (`pylhe`) | PyPI yes | not installed; "pylhe 2.1" on PyPI (**L**) | **J** (`SRC_URL_PYPI_PYLHE`) |

**Role in this project / must NOT be used for**

- *MadGraph5_aMC@NLO, Pythia 8, Herwig 7* — `event_generation/{madgraph,pythia,herwig}`: hard scattering, shower
  and hadronisation for μp processes with immutable run records. **No sample exists; nothing may be presented as
  a prediction** (`event_generation/README.md`). Generator runs must use the scenario parameters by
  `parameter_id`, never typed-in numbers.
- *Delphes* — `detector/fast_simulation` Level-1 response **only after** a detector card with provenance exists;
  no LHμC detector card exists (only the μLHC sketch and the LHeC detector are documented starting points,
  `detector/README.md`). Not a substitute for Geant4 where material effects matter.
- *FeynRules, SARAH* — `theory/` UFO handling for BSM benchmarks. Both need Mathematica, which this project does
  not have; benchmarks that depend on a private model cannot be reproduced. In particular the Kraków di-Higgs
  deck (`SRC_WS_LEBOHO_KUMAR_DIHIGGS`) uses "MG5_aMC v3.6.7" with the model "HELv2 effdihiggs-v2 (not public)" and
  "CTEQ6L1": the **model file is not public**, so that benchmark is *pending* and cannot be re-run even once MG5
  is installed (designated location `theory/benchmarks/<id>/proposal.yaml`, CLAUDE.md §2; **no proposal record
  exists yet** — the directory is empty on the document date).
- *LHAPDF* — PDF sets for the generators and for `physics/` cross-section checks. Must not be installed from the
  stale PyPI record. Note that the di-Higgs deck used CTEQ6L1, a legacy set; a reproduction must record the set
  and its LHAPDF ID in the run record.
- *pylhe* — I/O only.

---

## 5. Analysis, statistics and data publication

| Tool | Intended domain | Latest version seen | Licence | Install route | Reachable here | Phase 0 status | Evidence |
|---|---|---|---|---|---|---|---|
| **ROOT** | HEP data analysis framework (needed by BDSIM, Delphes, many HepMC workflows) | "v6-40-04" (release assets "2026-08-27") | "LGPL-2.1-or-later (plus bundled BSD/NCSA components per Arch packaging)" | "conda install -c conda-forge root"; "pip install root" exists only "in alpha mode … on Linux" for 6.38 — status for 6.40 not verified | `root.cern` blocked; GitHub yes; conda-forge unverified | not installed | **J** (`SRC_URL_GITHUB_ROOT_RELEASES`) |
| **pyhf** | Pure-Python HistFactory likelihoods for sensitivity studies | 0.7.6 | "Apache-2.0" | pip (`pyhf`) | PyPI yes | not installed; "pyhf 0.7.6" on PyPI (**L**) | **J** (`SRC_URL_PYPI_PYHF`) |
| **HEPData** (`hepdata_lib`; hepdata.net) | Publishing digitised results | `hepdata_lib` 0.21.0 | `hepdata_lib` "MIT license"; platform: "HEPData is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License"; "the default license applied to all data uploaded to HEPData is CC0" | pip (`hepdata_lib`); the portal itself is a web service | PyPI yes; `hepdata.net` not fetched (**J**) | not installed | **J** (`SRC_URL_GITHUB_HEPDATA_LIB`) |

**Role in this project / must NOT be used for**

- *ROOT* — file I/O and histogramming where BDSIM/Delphes require it. Not a project-wide dependency: Python-side
  analysis stays in numpy/scipy/pyhf so that results do not depend on a tool the environment cannot install today.
- *pyhf* — `analysis/statistics`: every sensitivity claim (e.g. recasting the di-Higgs "S/sqrt(S+B)=4.25 at 70%
  b-tag" at 1 ab⁻¹ from the Kraków deck) must be a pyhf (or equivalent documented) likelihood with the statistical
  model in the run record. It must not be used to "confirm" the deck's number without the deck's own inputs,
  which are not available (`docs/limitations.md`).
- *HEPData* — only for results this project has computed with full provenance; never for re-publishing the
  proponents' tables.

---

## 6. CAD, geometry conversion and visualisation

| Tool | Intended domain | Latest version seen | Licence | Install route | Reachable here | Phase 0 status | Evidence |
|---|---|---|---|---|---|---|---|
| **Open CASCADE Technology (OCCT)** | B-rep CAD kernel under CadQuery/OCP/build123d/FreeCAD/opencascade.js | "V8_0_1 (8.0.1)", release assets "2026-07-30" | "LGPL 2.1 with Open CASCADE exception" ("GNU Lesser General Public License version 2.1 … with a special exception") | via the wrappers below | `dev.opencascade.org` blocked; GitHub yes | not installed | **J** (`SRC_URL_GITHUB_OCCT_RELEASES`) |
| **OCP** (`cadquery-ocp`) | Python bindings to OCCT | 8.0.1.1.0 ("Python <3.15,>=3.11") | "Apache-2.0 (wrapper); underlying OCCT LGPL-2.1 with exception" | pip (`cadquery-ocp`) | PyPI yes | not installed | **J** (`SRC_URL_PYPI_CADQUERY_OCP`) |
| **CadQuery** | Parametric CAD scripting in Python | 2.8.0 (requires Python ">=3.11") | "Apache Public License 2.0" | pip (`cadquery`) or conda | PyPI yes | not installed; "cadquery 2.8" on PyPI (**L**) | **J** (`SRC_URL_PYPI_CADQUERY`) |
| **build123d** | Pythonic CAD on OCP | 0.13.0 ("<3.15,>=3.11") | "Apache-2.0" | pip (`build123d`) | PyPI yes | not installed; "build123d 0.13" on PyPI (**L**) | **J** (`SRC_URL_PYPI_BUILD123D`) |
| **OpenCascade.js** (`opencascade.js`) | OCCT compiled to WebAssembly for in-browser CAD | npm "1.1.1"; bundles "OCCT version in README: 7.6.2"; "repository appears inactive (tracker: last push Aug 2023)" | "LGPL-2.1-only" | npm | npm yes | not installed; **adoption not recommended before a maintenance check** (two OCCT major versions behind OCP 8.0.1) | **J** (`SRC_URL_GITHUB_OPENCASCADE_JS`) |
| **FreeCAD** | Scriptable desktop CAD (Python API, GDML workbench) | "1.1.4 (Latest stable); weekly-2026.10.28 dev build" | "LGPL v2 or later (source headers)" — no licence badge seen on the GitHub page | desktop installer / source; conda-forge `freecad` "not verified here" | GitHub yes | not installed | **J** (`SRC_URL_GITHUB_FREECAD_RELEASES`) |
| **pyg4ometry** | GDML read/write, STEP (CAD) import, FLUKA conversion — bridge from CAD to Geant4/BDSIM/FLUKA | 1.4.6 (requires Python ">=3.6.8") | "GPL-3.0 (full GPLv3 text in license field; GitHub shows GPL-3.0 license)" | pip (`pyg4ometry`) | PyPI yes | not installed; "pyg4ometry 1.4.6" on PyPI (**L**) | **J** (`SRC_URL_PYPI_PYG4OMETRY`) |
| **three.js** (`three`) | WebGL/WebGPU rendering for the Collider Explorer / CAD Studio | "0.186.1 (r186)" | "MIT" | npm (`three`) | npm yes | not installed | **J** (`SRC_URL_NPM_THREE`) |

**Role in this project / must NOT be used for**

- *OCCT/OCP, CadQuery, build123d* — `cad/generators`: parameter-driven B-rep master geometry (A), STEP export,
  healing, simplified solids for GDML (`docs/architecture.md` §7). Every generated solid carries a G-label; in Phase
  0 any LHμC layout is **G0 illustrative** because the IR, nozzle and ring dimensions are unknown
  (`cad/README.md`). CAD must not be used to "measure" dimensions that no source gives.
- *pyg4ometry* — the only planned path from STEP to GDML and to FLUKA input; GDML must pass `cad/validation`
  overlap checks before any run record references it. It is GPL-3.0: if project code *imports* it, the licence
  interaction with this repository's Apache-2.0 code licence must be settled before distribution (§10, item 2).
- *three.js, OpenCascade.js* — `frontend/` display of the **B — Visual** geometry only; the viewer "may never
  display a higher" G-label than the master geometry and must visually distinguish published/derived/synthetic/
  unknown values (`frontend/README.md`). OpenCascade.js is a candidate, not a decision (stale upstream).
- *FreeCAD* — optional interactive authoring and GDML inspection; not part of the automated pipeline.

---

## 7. Optimisation and surrogate tooling

| Tool | Intended domain | Latest version seen | Licence | Install route | Reachable here | Phase 0 status | Evidence |
|---|---|---|---|---|---|---|---|
| **pymoo** | Evolutionary multi-objective optimisation (NSGA-II/III etc.), Pareto fronts | 0.6.2 (requires Python ">=3.10") | "Apache-2.0" | pip (`pymoo`) | PyPI yes | not installed; on PyPI (**L**) | **J** (`SRC_URL_PYPI_PYMOO`) |
| **BoTorch** | Bayesian optimisation in PyTorch | 0.18.1 | "MIT" | pip (`botorch`) or conda | PyPI yes | not installed; on PyPI (**L**) | **J** (`SRC_URL_PYPI_BOTORCH`) |
| **Ax** (`ax-platform`) | Adaptive experimentation / BO orchestration on BoTorch | 1.3.1 (requires Python ">=3.11") | "MIT" | pip (`ax-platform`) | PyPI yes | not installed | **J** (`SRC_URL_PYPI_AX_PLATFORM`) |
| **Xopt** | Accelerator-oriented optimisation framework (as named in the master prompt) | not verified | not verified | not verified | not probed | not installed | **not verified** — absent from the journal |
| **scikit-optimize** | Lightweight GP/BO | 0.10.2 ("2024-06"); "original repository read-only, and a separate maintainer decided to continue development … and to publish new releases to PyPI" | "BSD 3-clause" | pip (`scikit-optimize`) | PyPI yes | not installed; **maintenance caveat** | **J** (`SRC_URL_PYPI_SCIKIT_OPTIMIZE`) |
| **Optuna** | Define-by-run black-box optimisation with pruning/storage | 5.0.0 (requires Python ">=3.9") | "MIT License" (classifier and README) | pip (`optuna`) or conda-forge | PyPI yes | not installed | **J** (`SRC_URL_PYPI_OPTUNA`) |

**Role in this project / must NOT be used for**

- All of these serve `optimization/{bayesian,evolutionary,pareto,active_learning}` (`optimization/README.md`):
  the optimiser, not the LLM, finds optima (CLAUDE.md §1.8). They must not be run against objectives whose
  constraints have unknown bounds — "hard constraints with unknown bounds block conclusions rather than being
  invented" — and in Phase 0 every LHμC constraint is unknown or imported from μLHC/LHeC/HL-LHC with
  `applicability` caveats. No optimisation has been run.

---

## 8. Luminosity tool used by the proponents

| Tool | Intended domain | Latest version seen | Licence | Install route | Reachable here | Phase 0 status | Evidence |
|---|---|---|---|---|---|---|---|
| **AloHEP** | Luminosity, beam–beam tune shift and disruption calculator used in the μLHC paper and the Kraków "Nucleus Options" deck | "master branch, 12 commits; no releases/tags listed (as fetched 2026-10-28)" | **"none stated (no LICENSE file or licence statement visible on the repository page or in README at fetch time)"** — "Reuse of the code requires clarifying the licence with the authors (yef.etu.edu.tr)" | Java GUI ("AloHEP.jar", "requires JRE 7+") from `github.com/yefetu/ALOHEP`; canonical distribution per IPAC'21 paper: `alohep.hepforge.org` (blocked) | GitHub yes; hepforge blocked | not installed, not executed, not evaluated | **J** (`SRC_URL_GITHUB_YEFETU_ALOHEP`, `SRC_URL_GITHUB_YEFETU_ALOHEP_README`, in `research/_fragments/mulhc-mutristan_sources.yaml`) |

**Role / must NOT:** the only way to re-run the μLHC luminosities (L = 8.8e33 / 7.2e33 cm⁻²s⁻¹, `SRC_ARXIV_2506_15445`)
and the Nucleus-deck μA luminosities (`SRC_WS1681458_DAGLI_NUCLEUS`, p.12–14) with the original tool. Until the
licence is clarified it is **untrusted third-party code** (CLAUDE.md §5): inspect before executing, run isolated,
never let it touch credentials. Its luminosity formula is not documented in the README, so AloHEP output cannot be
cited as a derivation — the project's own closed-form check (`lhmuc/analytical.py`; naive L(μLHC) = 1.14e34 and
1.40e34 for the two booster options, which times the one-lifetime decay average 0.632 give 7.2e33 and 8.8e33 to
better than 2 %, i.e. no hourglass reduction is visible in the published values; see `docs/limitations.md` §5) is
what `tests/scientific` reproduces.

---

## 9. What is actually installed (Phase 0 environment, read with `uv pip list` / `importlib.metadata`)

Python 3.13.17 managed with `uv`; `pyproject.toml` declares `requires-python = ">=3.11"`, project licence Apache-2.0.

| Package | Installed version | Licence metadata as installed | Role | Evidence |
|---|---|---|---|---|
| numpy | 2.5.4 | "BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0" | audit arithmetic (`lhmuc/analytical.py`) | **E** |
| scipy | 1.18.1 | classifier "BSD License" | audit arithmetic | **E** |
| pint | 0.26.2 | "BSD-3-Clause" | unit parsing (`lhmuc/units.py`) | **E** |
| jsonschema | 4.26.0 | "MIT" | schema validation | **E** |
| referencing | 0.37.0 | "MIT" | schema `$ref` resolution | **E** |
| pyyaml | 6.0.3 | "MIT" | parameter/scenario files | **E** |
| pytest (dev) | 9.2.0 | "MIT" | tests | **E** |
| ruff (dev) | 0.17.3 | "MIT" | linting | **E** |

**Nothing from §2–§8 is installed.** No conda/mamba, no C++ toolchain check, no Fortran check, no Java runtime
check and no Mathematica has been performed or is claimed.

---

## 10. Licence notes that require a decision before adoption

1. **MAD-X licence conflict (preserved, not averaged — CLAUDE.md §1.6).** Repository `License.txt` = custom CERN
   licence; LCG Info label = "MIT License"; 2011 CERN gitlab mirror = "EPICS Open License". cpymad's own
   `license_expression` names "LicenseRef-CERN-MADX-Proprietary" for the bundled binary. Working rule: *use*
   allowed for research, *redistribution* of the binary not allowed by this project; record in
   `research/source_conflicts.yaml` when that file is built (it does not exist yet). Resolution requires reading
   the 5.09.00 tag (fetch backlog in `research/_fragments/software-tools_unresolved.md`).
2. **GPL-licensed Python packages imported by project code** (pyg4ometry GPL-3.0; PyTao GPL v3; Cheetah GPL v3;
   pythia8mc GPL v2+; LHAPDF GPL-3.0-only/GPL-2 conflict). This repository is Apache-2.0 (`LICENSE`) with data under
   `LICENSE-DATA`. Calling these tools as **separate processes** through run records avoids linking questions;
   importing them into distributed project modules does not. The owner decides per module before Milestone 2;
   this document does not give legal advice.
3. **Proprietary dependency: Mathematica** for FeynRules and SARAH. Not available; benchmarks requiring a fresh
   UFO export cannot be executed. Public UFO files can still be used with MG5.
4. **Registration-gated: FLUKA.** "Registration as a FLUKA user is subject to approval." No account; not planned.
5. **No licence at all: AloHEP** (GitHub copy). Cannot be redistributed or modified; may only be *run* after the
   authors clarify terms.
6. **Non-public model file: "HELv2 effdihiggs-v2 (not public)"** (Kraków di-Higgs deck). Not software this project
   can obtain; the benchmark stays *pending*.
7. **Stale or unmaintained routes:** PyPI `LHAPDF` 6.2.1.post10 ("stale, empty metadata"); `pip install root`
   "alpha"; opencascade.js "last push Aug 2023"; scikit-optimize continued by a separate maintainer. None may be
   pinned without a fresh check.

---

## 11. Version drift, pinning and archiving policy

- Every version above is a **2026-10-28 snapshot** (xtrack 0.118.5 was "released Oct 28, 2026"). The inventory
  is not a lock file. When a tool is adopted its exact version is pinned in `uv.lock` (Python) or a `package-lock`
  (npm), and its PyPI/npm JSON, licence file and checksum are archived under `references/` with SHA-256 recorded in
  `research/archived_metadata/` — the journal values are *summaries of fetches*, "not archived copies" (`archived_file:
  null`, `sha256: null` everywhere in the fragment).
- Session probes (**P**) in this document (xsuite 0.67.1, geant4-pybind 0.1.3, pybdsim 3.9.0, MG5 `VERSION`
  3.8.1 / 2026-10-09, MG5 `LICENSE` text, conda-forge HEAD 200) are **not yet in any registry fragment**. To-do
  for the research-log step: add them as `SRC_URL_PYPI_XSUITE`, `SRC_URL_PYPI_GEANT4_PYBIND`,
  `SRC_URL_PYPI_PYBDSIM`, `SRC_URL_GITHUB_MG5AMCNLO_3X_LICENSE` with `access: fetched`, or re-fetch and archive them.
- No compatibility statement (cpymad 1.20.0 ↔ MAD-X 5.09.00, PyTao ↔ conda-forge `bmad`, pyg4ometry 1.4.6 ↔
  Geant4 11.4, BDSIM 1.7.7 ↔ Geant4 version, Delphes ↔ ROOT 6.40) has been tested; those tests belong to the
  Milestone 2 environment-setup task, not to this inventory.
- Reachability is session-specific. The blocked-host list and the FLUKA registration requirement mean that
  **Geant4, BDSIM, FLUKA, Herwig, LHAPDF, FeynRules, SARAH, ROOT, G4beamline and AloHEP cannot be installed from
  their official sources in this environment today**; MG5, Pythia (pythia8mc), Xsuite, cpymad, Cheetah, PyTao,
  the CAD stack, pyhf, pylhe and the optimisers can be.

---

## 12. Open items (mirror of `research/_fragments/software-tools_unresolved.md`, abridged)

MAD-X licence at the 5.09.00 tag · Bmad core licence and conda-forge version · Geant4 official pages and
geant4-pybind wheel contents · BDSIM release and required Geant4 · G4beamline publisher licence · FLUKA current
Single User Licence text · Herwig 7.3.x point releases · FeynRules and SARAH current versions and licence texts ·
LHAPDF upstream version and GPL-2 vs GPL-3 · hepdata.net terms · ROOT `pip` status for 6.40 · Delphes 3.5.1 year ·
OCCT official release page · opencascade.js maintenance · FreeCAD licence file and conda-forge · Cheetah LICENSE
file · **BLonD, Bmad-X and Xopt: no evidence gathered at all** · arXiv abstract pages for all seven cited software papers
(fetch-blocked; details are snippet-level).

---

## 13. Sources cited in this document

Software-tool sources (category `OFFICIAL_SOFTWARE_DOCUMENTATION`, `OFFICIAL_CERN`, `PEER_REVIEWED`,
`CONFERENCE_PROCEEDING`, `SECONDARY_SOURCE` as classified by the scout; fragment `research/_fragments/software-tools_sources.yaml`):
`SRC_URL_GITHUB_MADX`, `SRC_URL_PYPI_CPYMAD`, `SRC_URL_PYPI_XTRACK`, `SRC_URL_PYPI_XPART`, `SRC_URL_PYPI_XFIELDS`,
`SRC_ARXIV_2310_00317` (arXiv:2310.00317), `SRC_URL_PYPI_PYTAO`, `SRC_URL_GITHUB_BMAD_ECOSYSTEM`,
`SRC_URL_PYPI_CHEETAH_ACCELERATOR`, `SRC_ARXIV_2401_05815` (arXiv:2401.05815), `SRC_URL_GEANT4_LICENSE`,
`SRC_URL_RHUL_BDSIM_MANUAL_LICENCE`, `SRC_ARXIV_1808_10745` (arXiv:1808.10745), `SRC_URL_DESY_MAXWELL_G4BEAMLINE`,
`SRC_URL_FLUKA_FORUM_REGISTRATION_FAQ`, `SRC_URL_GITHUB_ROOT_RELEASES`, `SRC_URL_LAUNCHPAD_MG5AMCNLO`,
`SRC_ARXIV_1405_0301` (arXiv:1405.0301), `SRC_URL_PYPI_PYTHIA8MC`, `SRC_ARXIV_2312_05175` (arXiv:2312.05175),
`SRC_URL_GITHUB_DELPHES_RELEASES`, `SRC_ARXIV_1310_1921` (arXiv:1310.1921), `SRC_ARXIV_1309_7223` (arXiv:1309.7223),
`SRC_URL_GITHUB_CONDA_FORGE_LHAPDF_FEEDSTOCK`, `SRC_URL_PYPI_PYLHE`, `SRC_URL_PYPI_PYHF`, `SRC_URL_GITHUB_HEPDATA_LIB`,
`SRC_URL_GITHUB_OCCT_RELEASES`, `SRC_URL_PYPI_CADQUERY_OCP`, `SRC_URL_PYPI_CADQUERY`, `SRC_URL_PYPI_BUILD123D`,
`SRC_URL_GITHUB_OPENCASCADE_JS`, `SRC_URL_GITHUB_FREECAD_RELEASES`, `SRC_URL_PYPI_PYG4OMETRY`, `SRC_URL_NPM_THREE`,
`SRC_URL_PYPI_PYMOO`, `SRC_URL_PYPI_BOTORCH`, `SRC_URL_PYPI_AX_PLATFORM`, `SRC_URL_PYPI_SCIKIT_OPTIMIZE`,
`SRC_URL_PYPI_OPTUNA`; AloHEP: `SRC_URL_GITHUB_YEFETU_ALOHEP`, `SRC_URL_GITHUB_YEFETU_ALOHEP_README`
(fragment `research/_fragments/mulhc-mutristan_sources.yaml`).

Project documents referenced for tool usage context: `SRC_ARXIV_2506_15445` (Akturk et al., μLHC, PTEP 2026,
arXiv:2506.15445 — AloHEP luminosities, nozzle energy deposition), `SRC_WS1681458_DAGLI_NUCLEUS` (Kraków
"Nucleus Options" deck — AloHEP μA tables), `SRC_WS_LEBOHO_KUMAR_DIHIGGS` (Kraków di-Higgs deck — MG5_aMC v3.6.7,
HELv2 effdihiggs-v2, CTEQ6L1), `SRC_ARXIV_2610_35154` (Piotrzkowski, LHμC, PoS DIS2026, arXiv:2610.35154 — the
machine this platform models; it names no software).

Companion documents: `docs/architecture.md` §11 (software environment), `docs/limitations.md` §4 (software not
available), `research/source_quality_policy.md` §2 (category `OFFICIAL_SOFTWARE_DOCUMENTATION`),
`docs/internet_research_protocol.md` §5 (access modes).

---

## 14. Change log

| Date | Change |
|---|---|
| 2026-10-28 | First version: 40 table rows covering the 33 tools and tool groups named in master prompt §3 (including AloHEP, BLonD, Bmad-X, Xopt) plus geant4-pybind, pybdsim and the installed core stack; versions/licences quoted from the software-tools journal; session reachability probes; licence decisions list; drift/pinning policy. |
