# LHμC-VirtualLab — Limitations: what is not known and not verified

**Document date:** 2026-10-28 · **Project phase:** Phase 0 (evidence and feasibility audit) ·
**Owner:** David Hausler · **Companion documents:** `CLAUDE.md`, `docs/architecture.md`,
`docs/scientific_scope.md`.

> This document is the negative image of `docs/scientific_scope.md`: it lists what the five
> uploaded sources do **not** give, what the project could **not** verify in this environment, where
> the sources **disagree**, and which statements the platform must therefore **never** make.
> Items here are the seed of the missing-evidence register; `unknown` in a parameter record means
> `value: null`, never `0`.

---

## 1. Unknown LHμC machine parameters

No uploaded source gives a value for the quantities below *for the LHμC*. Where the predecessor
μLHC paper or a non-LHμC design gives a number, that is noted; such numbers are at best
`imported_related` or `analogous` and must not be presented as LHμC values. The scenario files
`parameters/machine/scenarios_*.yaml` list the same gaps as `unknown_roles` per configuration.

### 1.1 Interaction region

| Quantity | Status | What exists instead |
|---|---|---|
| L* (distance IP → first quadrupole) | unknown | LHeC L* = 15 m seen only in search snippets (not verified); IMCC 10 TeV L* = 6 m, snippet only |
| Q1 (first quadrupole) gradient, aperture, length | unknown | LHeC Q1A "252 T/m, 20 mm" snippet only |
| Crossing angle | unknown (`IR_CROSSING_ANGLE_DIS2026`, the only `status: unknown` record on 2026-10-28) | DIS2026 says only "a very small crossing angle is needed" (p.4); LHeC values 6–7 mrad vs a head-on 2025 phase-one scheme, snippets only |
| Separator dipole field, length, position | unknown | "a new separator dipole" named, no numbers (p.4) |
| Muon focusing scheme ("in between" vs "outside" LHC mini-beta quadrupoles) | undecided in source | two options stated, none chosen |
| β*_x, β*_y of the μ⁺ beam for the DIS2026 example set | unknown | only σ = 4.8 μm is given; μLHC uses 3 cm / 0.7 cm with ε_n = 4 μm, which gives σ_x = 3.6 μm, σ_y = 1.7 μm, i.e. *not* the round 4.8 μm beam of Table 1 |
| β* of the proton beam at the LHμC IP | unknown | μLHC 7 cm (from LHeC CDR); Nucleus deck 10 cm for ions |
| Muon and proton bunch lengths, energy spreads | unknown for LHμC | μLHC μ⁺ 2 mm; proton bunch length not in any uploaded source (the 7.5 cm used in the hourglass test is a nominal LHC order of magnitude, not a sourced LHμC value) |
| Muon normalised emittance for the DIS2026 set | unknown | μLHC 4 μm (from μTRISTAN) |
| Beam-beam tune shifts, hourglass factor, luminosity lifetime | unknown for LHμC | μLHC Table 3 gives ξ_x,y = 600 × 10⁻⁴ (μ⁺) and 22 / 18 × 10⁻⁴ (p); Nucleus deck ξ values for ions |
| Number of IPs | unknown | layout figure shows one |

### 1.2 Detector and machine-detector interface

| Quantity | Status | What exists instead |
|---|---|---|
| Nozzle opening angle, length, tip position, materials and thicknesses for the LHμC | unknown | μLHC: "6-meter-long tungsten shielding cone" cladded with borated polyethylene, 19 % energy deposited (p.13–14); IMCC: INERMET180 + borated PE, tip 6 cm from IP, 10° outer inclination — snippets only, 10 TeV μ⁺μ⁻ design, not μ⁺p |
| Detector dimensions, solenoid field, calorimeter depths, tracker radii | unknown | "baseline LHeC detector" with "relatively minor modifications" (p.5); no LHeC detector document is available in this environment |
| Acceptance loss due to the nozzle | unknown | qualitative statement only |
| Beam-induced background rates, fluences, doses | unknown | none computed; Geant4/FLUKA figures in μLHC concern muon energy loss in the cone, not background |
| Near-beam muon tagger, forward proton tagging, luminosity monitor | concept only | named as needed; no parameters |

### 1.3 Source, acceleration and rings

| Quantity | Status | What exists instead |
|---|---|---|
| Ultra-cold μ⁺ yield per proton, per pulse and per second at the LHμC | unknown | "5% of the ones in the μTRISTAN proposal" (p.4); μTRISTAN rate claims only via the μLHC paper; J-PARC USM ~10⁵ μ⁺/s design, snippet only |
| Muonium formation, diffusion and laser-ionisation efficiencies | unknown | none in uploads; snippet-level design targets only |
| Source emittance, bunch charge, bunch structure at the LHμC | unknown | J-PARC "< 1 π mm mrad" snippet only; μLHC injects 4.5 × 10¹⁰ per bunch (from μTRISTAN) |
| Proton driver energy, current, RCS parameters, target design | unknown | "a 4 MW proton driver" and "two RCS" (p.3–4); no energy or repetition rate |
| Pre-acceleration to 1 GeV | concept only | cited as "actively pursued" |
| vFFA fields, apertures, excursion, cell structure, RF frequency and voltage, number of turns | unknown | 70 GeV three-pass / 500 GeV one-beamline / 1 TeV two-beamline *example* (p.4); no numbers |
| Booster survival for the LHμC chain | unknown | μLHC 82 % / 67 % for the two racetrack options (reproduced 81.6 % / 67.4 % by `lhmuc/analytical.py`) |
| Main-ring dipole field, lattice, RF, injection and extraction, number of turns stored | unknown | circumference "about 3(6) km" only; fill-factor-1 bound 7.0 T |
| Tunnel coordinates, depth, tangent point to the LHC, footprint of the 9 km booster | unknown | Fig. 2 (p.3) is a schematic |
| Muon polarisation | unknown | "high polarisation of the μ⁺ beam might also be feasible" (p.4) |
| Wall-plug power, cost, schedule, radiation protection, neutrino radiation from the ring | unknown | no source gives any |

### 1.4 Luminosity-related statements

- The DIS2026 "average luminosity close to 10³⁴" and the Table 1 "peak luminosity 2.1 × 10³⁴" are
  not linked by any stated model; the ratio implies an average-to-peak factor near 0.5 but no
  source states it.
- The μLHC paper's conclusion ("luminosity well-exceeding 10³³") and its acknowledgement of an
  erratum (values increased) mean the uploaded v2 may or may not include every correction; the
  erratum text was not obtained.
- Integrated luminosities (250 / 1000 fb⁻¹ per working point; 1 ab⁻¹ in the di-Higgs study; 72 /
  88 fb⁻¹ per year in μLHC Table 4) are *assumed* inputs of physics studies, not machine outputs.

---

## 2. Values known only from a related machine

The μLHC paper (`SRC_ARXIV_2506_15445`) supplies β*, emittance, bunch length, bunch count, the
AloHEP luminosities and the booster survival fractions. It is a different concept: 40 bunches (not
80), 22 × 10¹⁰ protons per bunch (not 22 × 10¹¹), a μTRISTAN-style booster or an LHeC ERL
booster (not vFFA), "optics values from the μTRISTAN μ⁺e⁻ design". Several of its inputs are
themselves imported: the proton table from the LHeC CDR ("Table 2.11 in [12]"), the μ⁺ optics
from μTRISTAN, the injection bunch charge 7.2 nC from μTRISTAN. Every such record carries
`imported_related` with an `applicability.explanation` saying so. Using them for the LHμC is an
*assumption* and must be recorded as one (`parameters/assumptions/`, `schemas/assumption.schema.json`)
before any computation depends on it.

---

## 3. Snippet-only status of every non-uploaded source

Network policy in this session blocked arxiv.org, indico.cern.ch, cds.cern.ch, inspirehep.net,
pos.sissa.it, doi.org, journal and readthedocs hosts and all CERN hosts. Consequently:

- Only the **five uploaded documents** were read. Everything else named in the research
  fragments (`research/_fragments/*_sources.yaml`, `*_unresolved.md`; eight families: lhmuc-primary,
  mulhc-mutristan, ultracold-source, vffa-acceleration, lhec-erl, muon-collider-mdi,
  lhc-hl-lhc-protons, software-tools, theory-benchmarks) was seen as **search-engine snippets** or
  not at all (`access: snippet_only | blocked | pending_fetch`).
- Snippet evidence **may not back `reported_lhmuc`**, is capped at `confidence: medium`, and may be
  the search tool's paraphrase rather than verbatim text (`CLAUDE.md` §1.5; several fragments flag
  exactly this).
- Specific leads that remain **unverified** and must not be used as inputs: LHeC IR L* = 15 m,
  β* 10 → 7 cm, Q1A 252 T/m with 20 mm aperture, crossing angle 6–7 mrad versus a head-on 2025
  phase-one design; IMCC nozzle INERMET180 + borated polyethylene, tip 6 cm from the IP, 10° outer
  inclination, L* = 6 m at 10 TeV; J-PARC ultra-slow-muon design rate ~10⁵ μ⁺/s and emittance
  < 1 π mm mrad; HL-LHC 2.2 × 10¹¹ p/bunch, ε_n 2.5 μm and 2760 / 2748 / 2808 bunches depending on
  source and version (a conflict to preserve, not average).
- The Kraków workshop contributions cited by the DIS2026 paper (refs. [8], [10], [13], [17],
  [19]–[20], [22], [24], [26]–[29], [32]–[33]) — including the vFFA, nozzle-design, detector,
  near-beam-muon and luminosity-measurement talks — were **not** obtained. The HELP4CERN White Paper
  ("in preparation") does not exist publicly.
- The LHeC CDR/2020 update, the μTRISTAN paper (arXiv:2201.06664), the HL-LHC TDR and the IMCC
  reports were **not read**; their values appear here only as quoted by the uploads.

---

## 4. Software not available in this environment

| Tool | Status here | Consequence |
|---|---|---|
| Geant4, BDSIM, FLUKA | not installed; download/licence pages blocked; FLUKA licence requires registration and approval | no particle transport, no nozzle or background study, no detector response; μLHC's 19 % figure cannot be reproduced |
| MadGraph5_aMC@NLO | not installed; launchpad/GitHub reachable, so installation is *possible* but not done | no cross sections have been computed by this project |
| HELv2 `effdihiggs-v2` UFO | not public | di-Higgs benchmark cannot be reproduced without the authors' model |
| LHAPDF, ROOT | not installed; PyPI routes stale or alpha | PDF convolutions and ROOT-based analyses not available |
| AloHEP | not installed, not evaluated | the μLHC and Nucleus-deck luminosities cannot be re-run with the original tool |
| MAD-X / Xsuite / Bmad, CadQuery / build123d, pyg4ometry, pyhf, pymoo, botorch | installable from PyPI (versions listed in `docs/architecture.md` §11) but **not adopted, pinned or used**; the environment currently holds only `pyyaml, jsonschema, referencing, pint, numpy, scipy, pytest, ruff` | no lattice, geometry, statistics or optimisation code exists |
| Web access | literature hosts blocked; `WebSearch` snippets only | see §3 |

---

## 5. The luminosity-model discrepancy (open audit item)

The published luminosities can be reproduced arithmetically only under assumptions the sources do
not state. Audit results from `lhmuc/analytical.py` (checked in `tests/scientific/test_analytical_checks.py`):

| Case | Inputs | Naive L = f N_μ N_p / (4π σ_x σ_y) | Reported | Ratio reported / naive |
|---|---|---|---|---|
| DIS2026 Table 1 | 4 MHz, 0.07 × 10¹¹, 22 × 10¹¹, σ = 4.8 μm | 2.13 × 10³⁴ | 2.1 × 10³⁴ (peak) | 0.99 → **H = 1 implied** (no hourglass, crossing-angle or decay reduction visible) |
| μLHC ERL-based | 4 MHz, 3.0 × 10¹⁰, 2.2 × 10¹¹, σ = 4.3 μm | 1.14 × 10³⁴ | 7.2 × 10³³ (AloHEP) | 0.63 |
| μLHC μTRISTAN-based | 4 MHz, 3.7 × 10¹⁰, 2.2 × 10¹¹, σ = 4.3 μm | 1.40 × 10³⁴ | 8.8 × 10³³ (AloHEP) | 0.63 |

Observations the project records, without resolving them:

1. The μLHC ratios equal the **one-lifetime decay average** 1 − e⁻¹ = 0.632 quoted in the paper's
   §2.3 to better than 2 %. **No additional hourglass reduction is visible** in the published
   numbers.
2. Yet the hourglass factor computed for the stated optics (β*_μ = 3 cm / 0.7 cm, σ_z,μ = 2 mm,
   β*_p = 7 cm, assuming a nominal-LHC 7.5 cm proton bunch) is **H ≈ 0.53**. With β*_y = 0.7 cm and a
   7.5 cm proton bunch the hourglass effect cannot be negligible; the published value therefore
   implies either a much shorter proton bunch, relaxed muon optics (the Nucleus deck's "β*_μ ≈ 7–15
   cm" for ions shows relaxation is used), equal-size "matched" beams treated differently in
   AloHEP, or no hourglass term at all. **Which one is not determinable from the sources.**
3. The μ⁺ optics in Table 1 give σ_x = 3.6 μm, σ_y = 1.7 μm at 1 TeV, not the 4.3 μm "matched"
   round size of Table 3; how AloHEP matched the beams is not stated.
4. For the DIS2026 set, H = 1 is implied for a *peak* value, which is consistent with a
   freshly injected train but leaves the relation to the "average … close to 10³⁴" unstated.
5. The DIS2026 proton bunch population (22 × 10¹¹) is **ten times** the μLHC / HL-LHC value
   (22 × 10¹⁰). This is a real difference between documents (DIS2026 explicitly assumes fewer, more
   populated LHC bunches), not a unit slip: with 2.2 × 10¹¹ the DIS2026 luminosity would be
   2.1 × 10³³. Whether the LHC injector chain can deliver 2.2 × 10¹² protons per bunch is **not
   established by any source** (DIS2026 cites a workshop talk, ref. [24], not available here).

**Correction note.** An earlier internal summary (and `docs/architecture.md` §5 as written on
2026-10-28) quotes the naive μLHC luminosity as 1.14 × 10³⁵ with the hourglass and decay factors
"explaining part of the gap". The correct naive value with the Table 1–3 inputs is
**1.14 × 10³⁴**, and the decay average alone closes the gap; the hourglass factor is the *unexplained*
item. The test file carries the corrected statement; `docs/architecture.md` should be amended by
its author. These results are checks of internal consistency, not a beam-physics model, and the
intended conflict record (`CONF_LUMI_MODEL_ASSUMPTIONS` in `research/source_conflicts.yaml`) had
not yet been written when this document was.

Other preserved conflicts: 80 bunches at 12.5 Hz (DIS2026) vs 40 bunches (μLHC, Nucleus deck);
decay average "0.63" (μLHC p.11) vs "≈ 0.64 N₀" (Nucleus deck slide 8); 2760 proton bunches
(μLHC Table 2) vs 2748 / 2808 in other HL-LHC/LHC documents (snippets); √s written as 5.3 TeV
(both papers) vs 5.29 TeV (di-Higgs deck).

---

## 6. Missing theory-benchmark inputs

- **arXiv:2610.28252** (heavy neutral lepton). Known only from snippets: "Probing a heavy neutral
  lepton in a radiative neutrino model at a muon collider", a 3 TeV μ⁺μ⁻ collider study at 1 ab⁻¹
  with a *Dirac* HNL and a Higgs-mediated channel. Not an LHμC or μ⁺p paper; benchmark masses,
  mixings and model content unconfirmed; no public UFO of the radiative model identified (HeavyN is
  a stand-in without the scalar sector). **Not obtained.**
- **arXiv:2610.17801** (A → ZZγ in 2HDM + vector-like quarks). Snippets describe a one-loop
  decay-width calculation (BR ~10⁻⁵–10⁻⁴) with no collider simulation; 2HDM type, VLQ representations
  and benchmark points unconfirmed; no public combined 2HDM+VLQ UFO found. **Not obtained.**
- **HELv2 `effdihiggs-v2`** (di-Higgs benchmark): not public; reproduction depends on the authors.
- **Khanpour γγ cross sections**: computed with an EPA framework described as "in preparation";
  photon-flux cut-offs, proton dissociation treatment and survival factors are not given on the
  slides.
- **Colour-octet muon model file** (μLHC ref. [71]): FeynRules model named but not available here.

Proposal records for these benchmarks (`theory/benchmarks/*/proposal.yaml`) must carry
`access: pending_fetch` and `review_state: extracted` until the papers are read in full.

---

## 7. Repository state caveats (2026-10-28)

- At the time of writing, several Phase 0 artefacts referenced by `CLAUDE.md`, `README.md` and the
  tests were being produced by parallel tasks and were **not yet present**: the generated
  `registries/*.csv`, the authored `missing_evidence.csv`, `validation_registry.csv`,
  `risk_register.csv`, `research/search_log.csv`, `research/source_conflicts.yaml`,
  `research/unresolved_searches.md`, `research/source_quality_policy.md`, `parameters/assumptions/`,
  `parameters/materials/`, `theory/benchmarks/*/proposal.yaml`, and some of the companion policy
  documents (other `docs/*.md` files were appearing while this one was written). Check the
  repository rather than this sentence; the integrity tests fail until the registries exist.
- All 13 scenarios carry `geometry_fidelity: G0`; validation levels are P0 or P1, none higher.
- Parameter records were extracted by LLM-assisted reading of the PDFs with verbatim quotations
  and have not yet been reviewed line by line by a human; the parameter schema has no review
  field, so the review has to be recorded in the milestone report (the `review_state` vocabulary
  in `schemas/provenance.schema.json` is used by proposal records).
- Some μLHC-derived ids use the prefix `ACC_` and DIS2026 ids `ACCEL_`; unification is pending.
- The uploaded μLHC PDF's licence is not stated in the file and could not be checked on arXiv; it
  is therefore git-ignored and described only by metadata and hash.

---

## 8. Statements the platform must not make

Until evidence or documented computation exists, no output of this project (code, YAML, UI,
plot, export, report or conversation) may state or imply that:

1. the LHμC **will achieve** 10³⁴ cm⁻²s⁻¹ (peak or average), any integrated luminosity, or any
   centre-of-mass energy other than as a *reported claim* with its source;
2. the LHμC **has** a lattice, an IR optics solution, a crossing angle, a nozzle geometry, a
   detector design, a tunnel location, a power figure or a cost — none exists in the sources;
3. μLHC, μTRISTAN, LHeC, HL-LHC or IMCC values **are** LHμC values;
4. a number seen only in a search snippet is a reported value, or has confidence above `medium`;
5. the di-Higgs, two-photon, colour-octet-muon, HNL or 2HDM+VLQ sensitivities have been
   **reproduced** by this project, or that the HNL and 2HDM+VLQ papers describe μ⁺p collisions;
6. the booster survival fractions, hourglass factor or bending fields computed here are
   **design results** rather than consistency checks of published numbers;
7. the ultra-cold μ⁺ source **delivers** any rate at the LHμC, or that any laser-ionisation
   efficiency has been measured at the required level;
8. a **digital twin, CAD model, Geant4 geometry, event sample, surrogate model or optimisation
   result** exists;
9. an unknown quantity has the value **zero**, or a synthetic range is a measured value;
10. conflicting sources have been **reconciled** by averaging.

The correct form of a result in any of these areas is: "cannot yet be evaluated because X, Y, Z
are missing", with X, Y, Z named as parameter ids and listed in the missing-evidence register.

---

## 9. How these limitations are tracked

- Per-configuration gaps: `unknown_roles` in `parameters/machine/scenarios_*.yaml`.
- Unknown parameter values: records with `provenance.status: unknown` and `value: null`
  (`uv run python -m lhmuc validate` lists them).
- Unverified web leads and fetch backlogs: `research/_fragments/*_unresolved.md`, to be merged by
  `tools/merge_research_fragments.py` into `research/unresolved_searches.md`.
- Source-level open questions: `unresolved_questions` in `research/source_registry.yaml`.
- Conflicts: `research/source_conflicts.yaml` (schema `schemas/conflict.schema.json`), one record
  per disagreement, never an average.
- Audit arithmetic and its tolerances: `tests/scientific/test_analytical_checks.py`; a failing
  scientific test is never weakened without a documented investigation (`CLAUDE.md` §1.9).

This document should be revised whenever one of the items above is resolved, with the date and
the evidence that resolved it.
