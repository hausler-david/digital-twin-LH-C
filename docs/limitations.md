# LHμC-VirtualLab — Limitations: what is not known and not verified

**Document date:** 2026-10-28 · **Addendum:** 2026-10-29 (§10, plus dated notes in §1, §3–§5,
§7–§9) · **Project phase:** Phase 0 (evidence and feasibility audit) ·
**Owner:** David Hausler · **Companion documents:** `CLAUDE.md`, `docs/architecture.md`,
`docs/scientific_scope.md`, `docs/reports/M1_addendum_uploaded_documents.md`.

> This document is the negative image of `docs/scientific_scope.md`: it lists what the five
> uploaded sources do **not** give, what the project could **not** verify in this environment, where
> the sources **disagree**, and which statements the platform must therefore **never** make.
> Items here are the seed of the missing-evidence register; `unknown` in a parameter record means
> `value: null`, never `0`.

> **Addendum 2026-10-29.** After this document was written the owner uploaded 29 further documents
> (21 in the Phase-0 addendum, then 4, 1 and 3 in batches 7, 8 and 9). All were read in full,
> archived with SHA-256 (`research/archived_metadata/`) and extracted into parameter records that
> independent verifiers checked against the page images (`research/_fragments/verify_G*.md`); 34
> sources are now `access: uploaded`. Items that these documents state **for the LHμC** move from
> *unknown* to **reported in workshop material, unverified by simulation** — they come from
> unrefereed slides (confidence capped at `medium`) and no simulation by this project stands behind
> them. Items they state for other machines (LHeC, IMCC, μTRISTAN, J-PARC, MuIC) remain comparators.
> Superseded statements below carry a dated note; §10 gives the full account.

---

## 1. Unknown LHμC machine parameters

No uploaded source gives a value for the quantities below *for the LHμC*. Where the predecessor
μLHC paper or a non-LHμC design gives a number, that is noted; such numbers are at best
`imported_related` or `analogous` and must not be presented as LHμC values. The scenario files
`parameters/machine/scenarios_*.yaml` list the same gaps as `unknown_roles` per configuration.
*[2026-10-29: for some rows the Kraków decks now give an LHμC value; those rows say "reported in
workshop material, unverified by simulation" and stay in the tables because such a value is a
study option or assumption of its speaker, not a design or a result of this project.]*

### 1.1 Interaction region

| Quantity | Status | What exists instead |
|---|---|---|
| L* (distance IP → first quadrupole) | unknown | 2026-10-28: LHeC L* = 15 m seen only in search snippets (not verified); IMCC 10 TeV L* = 6 m, snippet only. **2026-10-29: still unknown for LHμC**, but the comparators are now read in full: LHeC 15 m (`IR_LSTAR_ANDRE2022`, `SRC_ARXIV_2201_02436` p.16; restated on `SRC_WS1681458_FORTHOMME_DETECTOR` p.4 as `IR_LSTAR_LHEC_WS2026_FORTHOMME`); a 23 m layout on the same slide, whose machine the slide does not name (`IR_LSTAR_FCCEH_WS2026_FORTHOMME`); IMCC 6 m (`IR_LSTAR_MR7`, `SRC_ARXIV_2510_27437` p.65). Conflict `CONF_IR_LSTAR` |
| Q1 (first quadrupole) gradient, aperture, length | unknown | 2026-10-28: LHeC Q1A "252 T/m, 20 mm" snippet only. **2026-10-29:** the LHeC QA1 concept is read in full (`IR_QA1_*_ANDRE2022`, `SRC_ARXIV_2201_02436` p.15, e.g. the electron aperture 106 mm from the proton orbit); no LHμC Q1 value exists |
| Crossing angle | unknown (`IR_CROSSING_ANGLE_DIS2026`, the only `status: unknown` record on 2026-10-28; 28 `unknown` records on 2026-10-29) | DIS2026 says only "a very small crossing angle is needed" (p.4); LHeC values 6–7 mrad vs a head-on 2025 phase-one scheme, snippets only. **2026-10-29:** the Forthomme beam set adds "adding in small crossing angle to drop extra parasitic collisions outside IP" with no value (`IR_CROSSING_ANGLE_SCHEME_WS2026_FORTHOMME`; `IR_CROSSING_ANGLE_WS2026_FORTHOMME` = null, p.17); the LHeC paper read in full has head-on e–p collisions with the electrons steered by the detector dipole (`IR_COLLISION_SCHEME_ANDRE2022`, p.10; `CONF_LHEC_CROSSING_ANGLE`) |
| Separator dipole field, length, position | unknown | "a new separator dipole" named, no numbers (p.4) |
| Muon focusing scheme ("in between" vs "outside" LHC mini-beta quadrupoles) | undecided in source | two options stated, none chosen |
| β*_x, β*_y of the μ⁺ beam for the DIS2026 example set | unknown | only σ = 4.8 μm is given; μLHC uses 3 cm / 0.7 cm with ε_n = 4 μm, which gives σ_x = 3.6 μm, σ_y = 1.7 μm, i.e. *not* the round 4.8 μm beam of Table 1 |
| β* of the proton beam at the LHμC IP | unknown | μLHC 7 cm (from LHeC CDR); Nucleus deck 10 cm for ions. **2026-10-29, reported in workshop material, unverified by simulation:** 7 cm "for ultimate HL-LHC optics" in the Forthomme beam set (`PROTON_BETA_STAR_WS2026_FORTHOMME`, p.17); LHeC 10 cm (`IR_BETA_STAR_PROTON_ANDRE2022`, `SRC_ARXIV_2201_02436` p.16) |
| Muon and proton bunch lengths, energy spreads | unknown for LHμC | μLHC μ⁺ 2 mm; proton bunch length not in any uploaded source (the 7.5 cm used in the hourglass test is a nominal LHC order of magnitude, not a sourced LHμC value) |
| Muon normalised emittance for the DIS2026 set | unknown | μLHC 4 μm (from μTRISTAN) |
| Beam-beam tune shifts, hourglass factor, luminosity lifetime | unknown for LHμC | μLHC Table 3 gives ξ_x,y = 600 × 10⁻⁴ (μ⁺) and 22 / 18 × 10⁻⁴ (p); Nucleus deck ξ values for ions |
| Number of IPs | unknown | layout figure shows one. **2026-10-29:** the Forthomme beam set assumes "same running conditions as LHeC (stand-alone, i.e. collisions at IP2 only)" (`IR_IP_LOCATION_WS2026_FORTHOMME`, p.17) — an assumption, not a siting decision |

### 1.2 Detector and machine-detector interface

| Quantity | Status | What exists instead |
|---|---|---|
| Nozzle opening angle, length, tip position, materials and thicknesses for the LHμC | 2026-10-28: unknown. **2026-10-29: reported in workshop material, unverified by simulation** (angle, length, tip, material); thicknesses and grade still unknown | μLHC: "6-meter-long tungsten shielding cone" cladded with borated polyethylene, 19 % energy deposited (p.13–14); IMCC: INERMET180 + borated PE, tip 6 cm from IP, 10° outer inclination — snippets only on 2026-10-28, 10 TeV μ⁺μ⁻ design, not μ⁺p. **2026-10-29:** LHμC options "conical half opening angle: 40(100) mrad → η_max ~ 4(3)" (`DET_NOZZLE_HALF_OPENING_ANGLE_WS2026_FORTHOMME`, `…_OPTION2_…`, Forthomme p.9; Kilic p.5, with 60 and 80 mrad also studied, p.12); single-sided on the incoming-μ⁺ side, tungsten cladded with borated polyethylene (Kilic p.4); drawing dimensions 487.8 cm + 100 cm and tip 6 cm from the IP (`DET_NOZZLE_LENGTH_WS2026_KILIC`, `DET_NOZZLE_FIRST_SECTION_LENGTH_WS2026_KILIC`, `DET_NOZZLE_TIP_DISTANCE_WS2026_KILIC`, p.4). The IMCC values are now read in full (MR7 Appendix G, pp.65–66: Table G.1 base plane at 595 cm, "the inclination amounts to 10 degrees" near the IP, tip 6 cm, INERMET180 with a borated-polyethylene layer: `DET_NOZZLE_LENGTH_MR7`, `DET_NOZZLE_OUTER_ANGLE_NEAR_IP_MR7`, `DET_NOZZLE_TIP_DISTANCE_MR7`, `DET_NOZZLE_MAIN_MATERIAL_MR7`) and remain analogues of a two-sided 10 TeV μ⁺μ⁻ nozzle. Conflict `CONF_NOZZLE_OPENING_ANGLE`; see §10.2 |
| Detector dimensions, solenoid field, calorimeter depths, tracker radii | unknown | "baseline LHeC detector" with "relatively minor modifications" (p.5); no LHeC detector document is available in this environment. **2026-10-29:** the LHeC detector paper is read in full (`SRC_ARXIV_2201_02436`: 3 T solenoid, `DET_SOLENOID_FIELD_ANDRE2022`, p.10) and the LHeC Delphes card restated by Forthomme uses Bz = 3.8 T (`DET_SOLENOID_FIELD_LHEC_DELPHES_WS2026_FORTHOMME`, p.13); the LHμC concept is "minor adaptations to LHeC detector concept" (`DET_LHMUC_DESIGN_BASIS_WS2026_FORTHOMME`, p.9) and **no LHμC solenoid field or dimension table is stated** (`CONF_DETECTOR_SOLENOID_FIELD`) |
| Acceptance loss due to the nozzle | unknown | qualitative statement only. **2026-10-29, reported in workshop material, unverified by simulation of this project:** for "the hadrons hitting the nozzle tip", Kilic's Geant4 11.4 study tabulates a particle acceptance of 0.97 % (40 mrad) to 0.77 % (100 mrad) and an energy-weighted acceptance of 0.011 % to 0.004 % (energy-loss fraction 99.989–99.996 %; `DET_NOZZLE_HADRON_*_WS2026_KILIC`, p.12), summarised as "Approximately 99.9% of IP-originating hadrons are absorbed" (p.22, a figure the verifier could reproduce from neither column); very forward scattered muons (1.3 TeV μ⁺ at η = 7.72, 3.85 TeV μ⁻ at η = 10.14) lose ≈ 10–11 % of their energy in the nozzle, with a Q² smearing of ≈ 2.5–2.7 % as stated on the slides (p.16–19; the verifier could not reproduce that percentage's definition, `research/_fragments/verify_G4_MDI_NOZZLE.md`). No full LHμC acceptance study exists |
| Beam-induced background rates, fluences, doses | unknown | none computed; Geant4/FLUKA figures in μLHC concern muon energy loss in the cone, not background. **2026-10-29:** still no μ⁺p BIB simulation. Forthomme states "~MGy" for the inner tracker from machine-induced background and muon-decay products (`DET_LHMUC_INNER_TRACKER_DOSE_ORDER_WS2026_FORTHOMME`, p.10) without a simulation shown; the IMCC FLUKA numbers (MR7 p.66, 1.8 × 10¹² muons per bunch, 10 TeV μ⁺μ⁻) are analogues (`DET_BIB_SIM_CODE_MR7`) |
| Near-beam muon tagger, forward proton tagging, luminosity monitor | concept only | named as needed; no parameters. **2026-10-29, reported in workshop material, unverified by simulation:** Acosta's far-forward toroid strawman (r 1.05–5.1 m, 4.5 m long, 4.1 T at the inner radius, ∫B·dl 4–18 T m, stations at 28 / 140 / 660 m covering 2.4 < \|η\| < 7.2, "~6 %" at 1 TeV in Geant4; `DET_FWD_SPECTROMETER_*_WS2026_ACOSTA`, p.11–12) and CSC strawman (p.16–21). Forward proton tagging and the luminosity monitor are still concepts only (Piotrzkowski's luminosity talk not uploaded, `ME_011`) |

### 1.3 Source, acceleration and rings

| Quantity | Status | What exists instead |
|---|---|---|
| Ultra-cold μ⁺ yield per proton, per pulse and per second at the LHμC | unknown | "5% of the ones in the μTRISTAN proposal" (p.4); μTRISTAN rate claims only via the μLHC paper; J-PARC USM ~10⁵ μ⁺/s design, snippet only. **2026-10-29: still unknown for the LHμC.** The Forthomme beam set states a μ⁺ rate into the booster of 3 × 10¹³ s⁻¹ (`SOURCE_MU_RATE_INTO_BOOSTER_WS2026_FORTHOMME`, p.17) — a requirement-level number, not a source design; the demonstrated and design yields that now exist are compared in §10.3 (the source-yield gap) |
| Muonium formation, diffusion and laser-ionisation efficiencies | unknown | none in uploads; snippet-level design targets only. **2026-10-29 (not LHμC values):** two measured formation fractions, 0.52 ± 0.01 (`SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAKULE2013`) and 0.655 ± 0.018 (`SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020`), kept apart (§10.4); laser ionisation 0.73 is a **calculation** (`SOURCE_LASER_IONISATION_EFF_CALC_ABE2019`, `SRC_ARXIV_1901_03047` p.8); the scheme used in the 2024 J-PARC test had ~10⁻⁶ (`SOURCE_LASER_IONISATION_EFF_244NM_WS2026_ZHANG`, Zhang p.10); no measured 122 + 355 nm efficiency exists (`CONF_LASER_IONISATION_EFFICIENCY`) |
| Source emittance, bunch charge, bunch structure at the LHμC | unknown | J-PARC "< 1 π mm mrad" snippet only; μLHC injects 4.5 × 10¹⁰ per bunch (from μTRISTAN). **2026-10-29:** measured J-PARC ultra-slow-muon emittance (0.85, 0.32) π mm mrad at 100 keV (`SRC_ARXIV_2410_11367` p.4) and the thermal-source estimate "∼ 1 π mm mrad" (`SRC_ARXIV_2605_25580` eq. (1)) are analogues; the LHμC bunch charge of 10¹⁰ μ⁺ (1.6 nC) appears in Nakazawa's space-charge assessment (`SOURCE_MU_PER_BUNCH_1E10_WS2026_NAKAZAWA`, p.16), see §10.5 |
| Proton driver energy, current, RCS parameters, target design | unknown | "a 4 MW proton driver" and "two RCS" (p.3–4); no energy or repetition rate. **2026-10-29:** still unknown for the LHμC; the hybrid-source option quotes "0.04 μ⁺ per 5 GeV proton on target to end of A-stage" (`SOURCE_HYBRID_MU_PER_PROTON_END_STAGE_A_WS2026_ROGERS`, p.14); the μTRISTAN hybrid target is normalised per 1 MW at 3 GeV (`SRC_ARXIV_2605_25580`, Table I) |
| Pre-acceleration to 1 GeV | concept only | cited as "actively pursued". **2026-10-29:** Nakazawa's low-velocity deck (IH-DTL 0.34 → 4.26 MeV, p.5) covers the J-PARC front end; Otani's pre-acceleration overview (DIS2026 ref. [20]) is not uploaded (`ME_008`) |
| vFFA fields, apertures, excursion, cell structure, RF frequency and voltage, number of turns | unknown | 70 GeV three-pass / 500 GeV one-beamline / 1 TeV two-beamline *example* (p.4); no numbers. **2026-10-29, reported in workshop material, unverified by simulation:** booster stage 70 → 500 GeV ("to 1 TeV?") in a single arc pair, order-10 turns, sub-millisecond cycle (`ACC_BOOSTER_*_WS2026_TOPPMUGGLESTONE`, p.3); preliminary analytic field options ~8 T (field index 60 /m, excursion ~3 cm), ~10 T (~44 /m), relaxed < 9 T (< 30 /m, < 7 cm) (`ACC_VFFA_*_WS2026_TOPPMUGGLESTONE`, p.35–36). Cell structure, apertures, RF frequency and voltage are still unknown (§10.6) |
| Booster survival for the LHμC chain | unknown | μLHC 82 % / 67 % for the two racetrack options (reproduced 81.6 % / 67.4 % by `lhmuc/analytical.py`) |
| Main-ring dipole field, lattice, RF, injection and extraction, number of turns stored | unknown | circumference "about 3(6) km" only; fill-factor-1 bound 7.0 T. **2026-10-29:** turns per lifetime n = γcτ_μ/C with cτ_μ = 659 m gives ≈ 2079 for 1 TeV in 3 km (`PHYS_MUON_TURNS_PER_LIFETIME_FORMULA_DUDKO2026`, `SRC_ARXIV_2607_16904` p.14 eq. (2); `test_turns_per_lifetime_dudko_formula`) — arithmetic, not a stored-turn design |
| Tunnel coordinates, depth, tangent point to the LHC, footprint of the 9 km booster | unknown | Fig. 2 (p.3) is a schematic |
| Muon polarisation | unknown | "high polarisation of the μ⁺ beam might also be feasible" (p.4). **2026-10-29:** the Forthomme beam set *assumes* 50 % (`MACHINE_MUON_POLARISATION_WS2026_FORTHOMME`, p.17); μTRISTAN assumes 0.8 (`MACHINE_MUON_POLARISATION_MUTRISTAN2022`, `SRC_ARXIV_2201_06664` p.10). Neither is a demonstrated value |
| Wall-plug power, cost, schedule, radiation protection, neutrino radiation from the ring | unknown | no source gives any. **2026-10-29:** still none for the LHμC as a whole. Rogers gives an order-of-magnitude cost scale "~ O(500) MCHF" for the hybrid source only and lists wall-plug power as an open challenge (`SOURCE_HYBRID_COST_SCALE_WS2026_ROGERS`, p.15; `SOURCE_HYBRID_WALL_PLUG_POWER_WS2026_ROGERS` = null); the 150 MW figure on Forthomme p.16 is the LHeC power constraint (`INFRA_POWER_CONSUMPTION_LIMIT_LHEC_WS2026_FORTHOMME`) |

### 1.4 Luminosity-related statements

- The DIS2026 "average luminosity close to 10³⁴" and the Table 1 "peak luminosity 2.1 × 10³⁴" are
  not linked by any stated model; the ratio implies an average-to-peak factor near 0.5 but no
  source states it.
- The μLHC paper's conclusion ("luminosity well-exceeding 10³³") and its acknowledgement of an
  erratum (values increased) mean the uploaded v2 may or may not include every correction; the
  erratum text was not obtained.
- Integrated luminosities (250 / 1000 fb⁻¹ per working point; 1 ab⁻¹ in the di-Higgs study; 72 /
  88 fb⁻¹ per year in μLHC Table 4) are *assumed* inputs of physics studies, not machine outputs.
- **2026-10-29.** A third LHμC luminosity statement now exists: "Peak luminosity of 10^34 cm^-2s^-1
  for 40 bunches of 10^10 µ⁺ in main ring", "Assuming 300 ns bunch spacing", σx,y ≈ 4.3 µm with
  β* = 7 cm (`MACHINE_PEAK_LUMINOSITY_WS2026_FORTHOMME`, `SRC_WS1681458_FORTHOMME_DETECTOR` backup
  slide p.17). It is reported in workshop material and unverified by simulation; "peak" is not
  defined on the slide, the muon energy is not stated (`MACHINE_MU_BEAM_ENERGY_WS2026_FORTHOMME` =
  null), and the proton bunch population is not given (see §5.1). It is a separate scenario
  (`LHMUC-WS2026-FORTHOMME`), not a correction of DIS2026 Table 1 (`CONF_PEAK_LUMINOSITY`).

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

**Addendum 2026-10-29.** The μTRISTAN paper itself is now read in full (`SRC_ARXIV_2201_06664`,
records `*_MUTRISTAN2022`), so the μ⁺ optics and the 7.2 nC bunch charge can be traced to their
original rather than to the μLHC restatement. Three further related machines are now on file and
carry the same restriction: the LHeC detector/ERL/IR paper (`SRC_ARXIV_2201_02436`, comparator only:
50 GeV electrons, no muon decay); the TeV-scale muon-ion collider paper (`SRC_ARXIV_2203_06258`),
whose column called "LHmuC" is **a different concept** — one 1.5 TeV beam of a 3 TeV IMCC μ⁺μ⁻
collider on LHC protons, √s = 6.5 TeV, 2.8 × 10³³ cm⁻²s⁻¹ (`MACHINE_LHMUC_MUON_SOURCE_CONCEPT_MUIC2022`,
PDF p.6; `MACHINE_PEAK_LUMINOSITY_LHMUC_MUIC2022`, p.8; `RISK_022_LHMUC_NAME_COLLISION`); and the
μ⁻p physics study of Cheung & Wang (`SRC_ARXIV_2101_10476`), which collides **μ⁻**, not μ⁺, so its
cross sections are screening comparators only (§10.8). IMCC 10 TeV μ⁺μ⁻ values (MuCol MR7, MAIA,
MUSIC, the M17 vFFA report) are `analogous` throughout.

---

## 3. Snippet-only status of every non-uploaded source

Network policy in this session blocked arxiv.org, indico.cern.ch, cds.cern.ch, inspirehep.net,
pos.sissa.it, doi.org, journal and readthedocs hosts and all CERN hosts. Consequently:

- *[Superseded 2026-10-29: 34 uploaded documents have now been read in full — the five below plus
  the 29 of the addendum and batches 7–9 (§10.1). The network policy is unchanged: no literature
  host was reachable on 2026-10-29 either, and the only additional fetch was the public AloHEP
  repository on GitHub.]* Only the **five uploaded documents** were read. Everything else named in the research
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
  *[Update 2026-10-29: the LHeC L* = 15 m and the proton β* = 10 cm are now read in the LHeC detector
  paper (`SRC_ARXIV_2201_02436` p.16), and the IMCC nozzle (INERMET180 + borated polyethylene, tip
  6 cm, 10°) and L* = 6 m in MuCol MR7 (`SRC_ARXIV_2510_27437` pp.65–66); they are no longer
  unverified leads but read comparators. The Q1A gradient, the 2025 phase-one head-on design, the
  J-PARC design rate, and the HL-LHC bunch counts and emittance remain snippet-level.]*
- The Kraków workshop contributions cited by the DIS2026 paper (refs. [8], [10], [13], [17],
  [19]–[20], [22], [24], [26]–[29], [32]–[33]) — including the vFFA, nozzle-design, detector,
  near-beam-muon and luminosity-measurement talks — were **not** obtained. The HELP4CERN White Paper
  ("in preparation") does not exist publicly.
  *[Update 2026-10-29: eleven Kraków decks are now uploaded — Forthomme, Topp-Mugglestone,
  Zimmermann, Rogers, Zhang, Kilic, Yamazaki, Acosta, Nakazawa, the AGH high-energy-QCD deck and
  Schulte. Not uploaded: Otani (`ME_008`), Kamioka (cited by Zhang p.20), Piotrzkowski (`ME_011`,
  `ME_013`), Tentori (`ME_012`), Sultansoy and Holzer. The White Paper is still not public (`ME_001`).]*
- The LHeC CDR/2020 update, the μTRISTAN paper (arXiv:2201.06664), the HL-LHC TDR and the IMCC
  reports were **not read**; their values appear here only as quoted by the uploads.
  *[Update 2026-10-29: the μTRISTAN paper and MuCol Milestone Reports 7 (`SRC_ARXIV_2510_27437`) and
  17 (`SRC_DOI_10_5281_ZENODO_15054073`) are now read in full. The MR7 reference tables for the
  collider, proton driver, target, cooling, magnets, RF and power converters are still being
  verified and are not in `parameters/`; cite `SRC_ARXIV_2510_27437` with a page until they are.
  The LHeC CDR, its 2020 update (`SRC_ARXIV_2007_14491`), André et al. 2025 (`SRC_ARXIV_2503_20475`),
  MuCol Report 5 (`SRC_ARXIV_2411_02966`) and the HL-LHC TDR (`SRC_URL_CERN_2020_010_HLLHC_TDR`)
  remain unread.]*

---

## 4. Software not available in this environment

| Tool | Status here | Consequence |
|---|---|---|
| Geant4, BDSIM, FLUKA | not installed; download/licence pages blocked; FLUKA licence requires registration and approval | no particle transport, no nozzle or background study, no detector response; μLHC's 19 % figure cannot be reproduced |
| MadGraph5_aMC@NLO | not installed; launchpad/GitHub reachable, so installation is *possible* but not done | no cross sections have been computed by this project |
| HELv2 `effdihiggs-v2` UFO | not public | di-Higgs benchmark cannot be reproduced without the authors' model |
| LHAPDF, ROOT | not installed; PyPI routes stale or alpha | PDF convolutions and ROOT-based analyses not available |
| AloHEP | not installed, not evaluated. **2026-10-29:** method paper read in full (`SRC_ARXIV_2610_09839`, `docs/tools/alohep_method_dagli2026.md`); public repository tag v2.0 (MIT) cloned read-only into an isolated folder, decks read as text, nothing compiled or run (`SRC_URL_GITHUB_TOBBETUYEF_ALOHEP`) | the μLHC and Nucleus-deck luminosities cannot be re-run with the original tool: the v2.0 repository contains **no μLHC or LHμC input deck** (`ME_043`), see §5.1 |
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
*[Update 2026-10-29: `docs/architecture.md` §5 states 1.14 × 10³⁴; `CONF_LUMI_MODEL_ASSUMPTIONS`
exists (committed with status `open` in the Phase-0 stage-2 commit; the registry-stage update of
2026-10-29 records a decided treatment — confirm in `research/source_conflicts.yaml` once
committed). The observation itself is unchanged: the hourglass question is not resolved.]*

Other preserved conflicts: 80 bunches at 12.5 Hz (DIS2026) vs 40 bunches (μLHC, Nucleus deck);
decay average "0.63" (μLHC p.11) vs "≈ 0.64 N₀" (Nucleus deck slide 8); 2760 proton bunches
(μLHC Table 2) vs 2748 / 2808 in other HL-LHC/LHC documents (snippets); √s written as 5.3 TeV
(both papers) vs 5.29 TeV (di-Higgs deck). *[2026-10-29: the conflicts raised by the uploads are
listed in §10.9.]*

### 5.1 Addendum 2026-10-29 — what the uploads add to the luminosity-model question

None of the following resolves the open item; together they narrow it and make the missing input
explicit.

1. **AloHEP is now documented** (`SRC_ARXIV_2610_09839`, read in full; method note
   `docs/tools/alohep_method_dagli2026.md`; records `MACHINE_ALOHEP_*_DAGLI2026`, applicability
   `screening_only`). The hourglass effect (eqs. (10), (22)–(23)) and the beam–beam pinch (eqs. (12),
   (21)) are *simulated* with macroparticles: the hourglass reproduces the analytic eqs. (22)–(23) to
   about 1 % for A = σ_z/β*_y ≲ 1.5 (p.27; HERA and EIC within 0.3 % and 0.5 %, p.33), and the pinch
   is validated in the regime D_y ≤ 1.3 the paper targets, not at D_y ≫ 1 (p.31). A centimetre-scale
   proton bunch against the μLHC β*_y = 0.7 cm would lie outside the validated hourglass range. The
   **muon-decay factor is applied analytically**: "The decay factor is applied analytically, so the
   residual difference is the statistical scatter of the simulated geometric luminosity" (p.36;
   `MACHINE_ALOHEP_DECAY_IMPLEMENTATION_DAGLI2026`); its functional form is not written in the paper.
2. **One beam decays at a μp collider, two at a μ⁺μ⁻ collider.** The paper's 10 TeV μ⁺μ⁻ value 0.254
   (p.36) is reproduced as the *two-beam* store average (1 − e^{−2T/γτ})/(2T/γτ) with γτ = 0.104 s and
   T = 0.2 s (`test_dagli2026_mucol_10tev_decay_factor_and_turns`). A μp collider needs the *one-beam*
   average (1 − e^{−T/γτ})/(T/γτ): over one dilated lifetime 0.632, against 0.432 for two beams
   (`test_decay_averaging_differs_between_mumu_and_mup`). Which form the code applies to an
   asymmetric pair is not stated; a run that used the two-beam form for μp would understate L by the
   ratio of the two averages.
3. **The internal nominal luminosity underestimates unequal beams.** Footnote 1, p.33: the readout
   L_nom = N₁N₂f_c/[4π max(σ_x1, σ_x2) max(σ_y1, σ_y2)] "underestimates the geometric luminosity when
   the beams differ"; the conversion to L_geo is given in Appendix A (p.39). A "Matched Beams" helper
   (p.19) enlarges the smaller spot to the larger one — the only operation in the paper that matches
   the μLHC phrase "with beam size matched accordingly"; whether the μLHC authors used it is not
   stated.
4. **No μLHC input deck exists in the public code.** The repository named by the paper,
   github.com/tobbetuyef/AloHEP, tag v2.0 (MIT; `SRC_URL_GITHUB_TOBBETUYEF_ALOHEP`), holds decks for
   MuCol 10 TeV, MuIC, Tevatron-based μp and LHC/HL-LHC protons, but **no μLHC or LHμC deck**. The
   values 7.2 × 10³³ / 8.8 × 10³³ therefore cannot be reproduced from the public repository alone
   (`ME_043_ALOHEP_CODE_AND_INPUT_DECKS`). The code was cloned read-only and not built or run
   (`docs/security_policy.md`).
5. **The Forthomme beam set implies a third proton bunch population.** With the naive formula, H = 1
   (the convention that reproduces the DIS2026 and μLHC tables) and f = 1/300 ns, "10^34 for 40
   bunches of 10^10 µ⁺" with σ = 4.3 µm implies N_p ≈ 7.0 × 10¹¹ — about 3.2 × the HL-LHC 2.2 × 10¹¹ and
   about one third of the DIS2026 22 × 10¹¹ (`PROTON_BUNCH_POPULATION_IMPLIED_WS2026_FORTHOMME`,
   derived, P1; `test_forthomme_beam_set_implied_proton_bunch_population`). The slide only says "may
   consider higher proton bunches population than HL-LHC's" (p.17).
6. **H = 1 is stated explicitly elsewhere.** The muon-ion collider paper writes "For simplicity, the
   hour-glass factor, H_hg, is assumed to be unity" (`MACHINE_HOURGLASS_FACTOR_ASSUMED_MUIC2022`,
   `SRC_ARXIV_2203_06258` PDF p.7). DIS2026 and μLHC never state their convention; the MuIC sentence
   shows that the H = 1 convention is in use in this literature, not that the LHμC numbers used it.
7. **More protons per bunch means longer bunches.** Zimmermann's answer to the LHμC request for
   "a much lower number of bunches in the LHC (say, 1% of the today's one)" (p.2) is the rule
   "Higher intensity is accompanied by longer bunches and/or larger energy spread – Roughly speaking
   σδ σz ≈ 2 n_b,0 σδ,0 σz,0" (p.14; `PROTON_BUNCH_MERGING_SCALING_RELATION_WS2026_ZIMMERMANN`; checked
   against LHC Project Report 627 Table 1 restated on p.9, ratio 0.91 in the record's derivation). A
   bunch population raised ten-fold by merging therefore comes with a longer bunch (a larger
   hourglass reduction against a centimetre-scale muon β*) and/or a larger energy spread. No source
   gives the resulting LHμC proton bunch length; `PROTON_BUNCH_LENGTH_RMS_SYN` stays a synthetic range.
8. **The LHeC Table 4 luminosity is not reproducible from its paper.** André et al. 2022 quote
   8.2 × 10³³ cm⁻²s⁻¹ (`MACHINE_PEAK_LUMINOSITY_ANDRE2022`, Table 4 p.18) but list no proton bunch
   population or emittance. With HL-LHC protons (2.2 × 10¹¹, ε_n = 2.5 µm), the Fig. 19 proton
   β*_p = 10.0 cm in both planes (the header gives β*_p = 10.0 cm and β*_e = 10.9 cm *per beam*, not per
   plane), the electron beam matched to the proton size (p.13) and the Table 2 bunch charge and
   spacing (499 pC, 24.95 ns), the naive formula gives about 6.5 × 10³³, a ratio of about 0.80. This
   is recorded as a band, not a reproduction, because the proton inputs are not in the paper
   (`test_andre2022_table4_luminosity_with_hl_lhc_proton_parameters_recorded_band`).

What would settle the item: the μLHC AloHEP input decks with the option set (hourglass, pinch,
decay form, matched beams) used for 7.2 × 10³³ / 8.8 × 10³³, or the PTEP erratum text if it states
them (`ME_016`, `ME_043`). Until then every luminosity in this repository is reported with the
model under which it was reproduced, and no LHμC luminosity is computed.

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

**Addendum 2026-10-29.** None of the five items above has changed: arXiv:2610.28252 and
arXiv:2610.17801 are still `blocked` (`ME_049`, `ME_050`) and `effdihiggs-v2` is still not public
(`ME_051`). Two physics documents arrived that are *comparators*, not benchmarks of this list:
Cheung & Wang 2021 (`SRC_ARXIV_2101_10476`, the paper DIS2026 cites for generic BSM searches)
studies **μ⁻p** — its μp-1 is 7 TeV p × 1 TeV μ⁻, √s = 5.3 TeV, an *assumed* 10³³ cm⁻²s⁻¹ and
0.1 ab⁻¹, giving Δg_hbb/g_hbb = 0.69 % (`PHYS_HBB_COUPLING_PRECISION_MUP1_CHEUNG2021`, p.2–3;
`test_cheung2021_hbb_coupling_precision`) — and the muon-ion collider paper (`SRC_ARXIV_2203_06258`)
tabulates μ⁺p and μ⁻p rates for its own "LHmuC" column. Because LHμC collides μ⁺, charged-current
rates differ (§10.8); neither paper's numbers are LHμC predictions, and the corresponding μ⁺p value
in Cheung & Wang is an explicit unknown (`PHYS_VBF_HIGGS_XSEC_WW_MUPLUS_P_7TEV_1TEV_CHEUNG2021` = null).
The AGH small-x deck (`SRC_WS1681458_HEQCD_SMALLX`) adds the LHμC small-x programme as reported
physics motivation (see `docs/scientific_scope.md` §1.10); no number from it has been reproduced.

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
- **Update 2026-10-29.** The artefacts listed as missing in the first bullet now exist (registries,
  search log, conflicts, unresolved searches, source-quality policy, 20 assumption records, materials
  records, four proposal records). At commit `104073c` the validator reports 5601 parameters, 236
  sources, 36 scenarios, 20 assumptions, 15 conflicts, 4 proposals, 0 errors and 0 warnings, and the
  suite collects 151 tests. A registry stage (supersession of assumptions, new conflict records,
  missing-evidence, risk and validation rows) was in progress in the working tree when this addendum
  was written; its counts are left to `docs/reports/M1_addendum_uploaded_documents.md`. All 36
  scenarios carry `geometry_fidelity: G0`; 100 parameter records are P1 and 5501 are P0 — none higher.
  The extraction of the addendum documents was verified record by record against the page images by
  independent agents (`research/_fragments/verify_G1…G14_*.md`), but **no human has yet reviewed the
  records line by line** (`RISK_028_HUMAN_REVIEW_PENDING`).

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

Added 2026-10-29:

11. a value read from a Kraków workshop deck (nozzle options, vFFA fields, the Forthomme beam set,
    the hybrid-source yield, TeV-muon resolutions) is a **frozen specification or a simulated
    result of this project** — it is "reported in workshop material, unverified by simulation";
12. the muonium formation fraction is a single number: 0.52 ± 0.01 and 0.655 ± 0.018 are **two
    measurements on different samples** and are never averaged (`CONF_MUONIUM_FORMATION_FRACTION`);
13. the 73 % laser-ionisation efficiency has been **measured** — it is a calculation (Abe 2019 p.8);
    or that the ultra-cold source has **demonstrated** any yield close to the μTRISTAN or LHμC budgets
    (§10.3);
14. AloHEP output **reproduces** the μLHC luminosities, or that its analytic decay factor for μ⁺μ⁻
    applies unchanged to μp (§5.1);
15. a μ⁻p result (Cheung & Wang 2021), a muon-ion-collider "LHmuC" value (`SRC_ARXIV_2203_06258`) or
    an IMCC 10 TeV μ⁺μ⁻ value **is** an LHμC value;
16. the MuCol M17 vFFA lattices are **tracked or validated designs** (they are analytic, and the
    report says the lattices still need numerical verification), or that an LHμC booster lattice
    exists;
17. a P1 label, or a confidence above the caps of `research/source_quality_policy.md` §4, is valid
    without the test or the source quality behind it (the validator rejects both since 2026-10-29).

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
- *Added 2026-10-29:* the addendum arithmetic is pinned in `tests/scientific/test_workshop_decks.py`,
  `test_batch7_documents.py`, `test_mucol_m17_vffa.py` and `test_batch9_documents.py`; canonical
  values in `test_addendum_canonical_records.py`. Uploads that resolve or narrow a backlog item are
  listed in `research/unresolved_searches.md` ("Resolved or narrowed by uploads"). Confidence caps
  and P1 labels are enforced by `uv run python -m lhmuc validate`; the lowering logs are
  `research/_fragments/confidence_caps_applied_2026-10-29.csv` and
  `research/_fragments/validation_levels_lowered_2026-10-29.csv`.

This document should be revised whenever one of the items above is resolved, with the date and
the evidence that resolved it.

---

## 10. Addendum 2026-10-29 — the uploaded documents of the Phase-0 addendum and batches 7–9

### 10.1 What was added

| Group | Documents (source_id) | Records at `104073c` |
|---|---|---|
| Kraków workshop decks, Indico 1681458 (11, all `PRIMARY_LHMUC` except Schulte, `CONFERENCE_PROCEEDING`) | `SRC_WS1681458_FORTHOMME_DETECTOR`, `_TOPPMUGGLESTONE_VFFA`, `_ZIMMERMANN_SPS_LHC`, `_ROGERS_HYBRID_SOURCE`, `_ZHANG_MUONIUM`, `_KILIC_NOZZLE`, `_YAMAZAKI_TEV_MUON`, `_ACOSTA_NEAR_BEAM`, `_NAKAZAWA_LOW_VELOCITY`, `_HEQCD_SMALLX`, `_SCHULTE_IMCC` | 1443 |
| Related machines and reference designs (addendum) | μTRISTAN `SRC_ARXIV_2201_06664`; MuIC `SRC_ARXIV_2203_06258`; MuCol MR7 `SRC_ARXIV_2510_27437` (MDI and acceleration sections); MAIA `SRC_ARXIV_2502_00181`; MUSIC `SRC_ARXIV_2601_13189` | 1875 |
| Source measurements (addendum) | Beare 2020 `SRC_ARXIV_2006_01947`; Aritome 2024 `SRC_ARXIV_2410_11367` | 180 |
| Context (addendum) | Dudko `SRC_ARXIV_2607_16904`; U.S. MCC SCAC input `SRC_ARXIV_2609_37117`; AI4MuC report `SRC_ARXIV_2610_14303` | 1 (the last two have no parameter records) |
| Batch 7 | LHeC detector/ERL/IR, André et al. 2022 `SRC_ARXIV_2201_02436`; J-PARC g-2/EDM, Abe et al. 2019 `SRC_ARXIV_1901_03047`; μTRISTAN hybrid target, Sakaki et al. 2026 `SRC_ARXIV_2605_25580`; AloHEP, Dağlı & Karaca 2026 `SRC_ARXIV_2610_09839` | 840 |
| Batch 8 | MuCol Milestone Report 17 "Tentative design of the FFA", `SRC_DOI_10_5281_ZENODO_15054073` | 131 |
| Batch 9 | Bakule et al. 2013 `SRC_ARXIV_1306_3810`; Cheung & Wang 2021 `SRC_ARXIV_2101_10476`; Giove 2026 RF talk `SRC_IMCC2026_GIOVE_RF_SYSTEM` | 301 |

Of the 4771 records citing these 29 documents, 563 are `reported_lhmuc` (all from the Kraków decks),
the rest `analogous`, `imported_related`, `derived_lhmuc`, `analytical_estimate` or `unknown`. Every
newly reported LHμC item is **reported in workshop material, unverified by simulation**:

| Item | Status before (2026-10-28) | Status now | Record ids (source, page) |
|---|---|---|---|
| Nozzle half-opening angle | unknown (synthetic 5–20°) | reported in workshop material, unverified by simulation: 40 mrad (baseline) and 100 mrad (alternative); 60 and 80 mrad studied | `DET_NOZZLE_HALF_OPENING_ANGLE_WS2026_FORTHOMME`, `…_OPTION2_…` (Forthomme p.9); `DET_NOZZLE_HALF_OPENING_ANGLE_*_WS2026_KILIC` (Kilic pp.5, 12) |
| Nozzle length, tip distance, material, side | unknown | reported in workshop material, unverified by simulation: 487.8 cm + 100 cm drawing dimensions (587.8 cm tip to base, derived), tip 6 cm, tungsten with borated-polyethylene cladding, incoming-muon side only | `DET_NOZZLE_LENGTH_WS2026_KILIC`, `DET_NOZZLE_TOTAL_LENGTH_IMPLIED_WS2026_KILIC`, `DET_NOZZLE_TIP_DISTANCE_WS2026_KILIC`, `DET_NOZZLE_MATERIAL_WS2026_KILIC`, `DET_NOZZLE_PLACEMENT_WS2026_KILIC` (Kilic p.4) |
| Detector concept | "baseline LHeC detector with minor modifications" | reported in workshop material: minor adaptations of the LHeC detector, LHeC Key4hep toolbox for re-optimisation, PPS-like inner-tracker replacement, 4D tracking, streamed DAQ, extended backward muon chambers | `DET_LHMUC_*_WS2026_FORTHOMME` (Forthomme pp.9–14) |
| Muon-system resolution at 1 TeV | unknown | reported in workshop material: 6–7 % main detector (Yamazaki p.10), ~6 % (Geant4) far-forward toroid (Acosta p.12) | `DET_MUON_P_RESOLUTION_1TEV_ACHIEVABLE_*_WS2026_YAMAZAKI`, `DET_FWD_SPECTROMETER_P_RESOLUTION_1TEV_G4_WS2026_ACOSTA`; `CONF_TEV_MUON_RESOLUTION` |
| Second LHμC beam set | none | reported in workshop material: 40 bunches of 10¹⁰ μ⁺, 300 ns, σ 4.3 µm, β*_p 7 cm, 10³⁴, 3 × 10¹³ μ⁺/s into the booster, 50 % polarisation assumed | `MACHINE_*_WS2026_FORTHOMME`, `IR_SIGMA_XY_IP_WS2026_FORTHOMME`, `PROTON_BETA_STAR_WS2026_FORTHOMME` (Forthomme p.17) |
| vFFA booster stage | example only | reported in workshop material, preliminary analytic study: 70 → 500 GeV single arc pair, ~8 / ~10 / < 9 T options | `ACC_BOOSTER_*_WS2026_TOPPMUGGLESTONE` (p.3), `ACC_VFFA_*_WS2026_TOPPMUGGLESTONE` (pp.35–36); `CONF_VFFA_PEAK_FIELD` |
| Hybrid source option | named only (DIS2026 p.4) | reported in workshop material: IMCC capture + rectilinear stage-A cooling + deceleration + low-energy cooling; 0.04 μ⁺ per 5 GeV proton to the end of stage A; deceleration "Not designed" | `SOURCE_HYBRID_*_WS2026_ROGERS` (Rogers pp.5, 13–14); scenario `LHMUC-SOURCE-HYBRID-IMCC`; `CONF_SOURCE_CONCEPT` |
| Front-end bunch charge | unknown | reported in workshop material: 10¹⁰ μ⁺ (1.6 nC) in ~2 ns → ~0.75 A, 220 × the perveance of the 30 mA H⁻ RFQ | `SOURCE_RFQ_*_WS2026_NAKAZAWA` (Nakazawa p.16); `CONF_FRONT_END_SPACE_CHARGE` |
| Proton-bunch request to the LHC | one unavailable reference | reported in workshop material: "say, 1% of the today's one" bunches; σδσz ≈ 2 n_b,0 σδ,0 σz,0 | `PROTON_*_WS2026_ZIMMERMANN` (Zimmermann pp.2, 14) |
| Small-x reach | Fig. 1 of DIS2026 | reported in workshop material: x_Bj ≲ 10⁻⁷ at Q² ~ 1 GeV², one order beyond LHeC | `PHYS_SMALLX_*_WS2026_HEQCD` (AGH deck p.13) |

Still **unknown** for the LHμC after the uploads: the muon β* and emittance of every LHμC beam set,
the proton bunch length and population actually deliverable, the crossing angle and separation
scheme, L*, Q1, the main-ring lattice and dipole field, the booster lattice and RF, the
pre-accelerator, the proton driver energy and repetition rate, the source rate actually achievable,
the μ⁺p beam-induced background, power, cost and siting. The scenario files list them as
`unknown_roles`.

### 10.2 Nozzle: the Phase-0 synthetic band excluded the reported baseline

The Phase-0 assumption `ASM_DET_NOZZLE_OPENING_ANGLE` carried a uniform 5–20° band. The LHμC
baseline of 40 mrad = 2.29° lies **below** it (100 mrad = 5.73° lies inside). Converted to
pseudorapidity, η_max = −ln tan(θ/2) gives 3.91 for 40 mrad and 3.00 for 100 mrad, against 2.44
for the IMCC 10° nozzle (`test_nozzle_half_angle_to_eta_max_forthomme_and_imcc`; the MR7 Table G.1
slopes are pinned by `test_imcc_nozzle_outer_surface_angles_mr7_table_g1`). The slides round η_max to
"~ 4(3)". The single-sided LHμC nozzle is therefore far narrower than the IMCC analogue, which was
the basis of the Phase-0 band: a calibration lesson recorded with the supersession of the assumption
(`docs/synthetic_data_policy.md`, supersession section). Lengths are comparable (Kilic 487.8 cm rear
section + 100 cm tip section; MR7 base plane at 595 cm; tip 6 cm in both). Open: the choice between
the options, the base dimensions and tungsten grade (Kilic p.22), and any μ⁺p background simulation
(`ME_024`, `ME_026`). Conflict `CONF_NOZZLE_OPENING_ANGLE` keeps the options as separate scenarios.

### 10.3 The source-yield gap

The measured chain and the design budgets now sit side by side, per surface muon:

| Quantity | Value | Record / test |
|---|---|---|
| Measured 2024 J-PARC chain, μ⁺ at 100 keV per surface muon | 2.1 × 10⁻⁸ (2 × 10⁻³ per pulse from 9.5 × 10⁴ surface μ⁺ per pulse) | `SOURCE_USM_PER_SURFACE_MUON_100KEV_ARITOME2024` (`SRC_ARXIV_2410_11367` pp.2, 4) |
| J-PARC g-2 design target per surface muon | 2.6 × 10⁻³ (Zhang p.10: 8.24 × 10⁵ / 3.2 × 10⁸); Abe 2019: 3.4 × 10⁻³ thermal Mu × 0.73 = 2.5 × 10⁻³ — consistent within 10 % | `test_abe2019_vs_zhang_g2_target_chain_consistency` |
| μTRISTAN budget after stopping | 0.52 × 0.6 × 0.6 × 0.73 = 0.137 ("14 %", Zhang p.20) | `SOURCE_MUTRISTAN_POST_STOPPING_BUDGET_WS2026_ZHANG`; `test_zhang_hline_chain_and_mutristan_budget` |

The measured value is ≈ 1.2 × 10⁵ below the g-2 design target and, per stopped muon (÷ 0.38),
≈ 2.5 × 10⁶ below the μTRISTAN post-stopping budget
(`test_aritome2024_measured_ultra_slow_muon_chain`). The 2024 test used a 244 nm spectroscopy laser
(ionisation ~10⁻⁶ from laser simulation, Zhang p.10; simulated 7 × 10⁻⁶ – 6 × 10⁻⁵ in Aritome 2024),
while the budgets assume the 122 + 355 nm scheme whose 73 % is a **calculation** (Abe 2019 p.8,
"calculated to be 73% based on the transition rates given by theoretical excitation and
dissociation cross sections") and which Zhang flags as "pending updates" (p.20); the dedicated light
source is projected at "around 10%" (Aritome p.5). The gap is therefore a statement about
demonstrated numbers, **not a feasibility verdict** on the 122 nm scheme — but no LHμC luminosity
that rests on the "5 % of μTRISTAN" yield can be called supported by measurement
(`RISK_002_FIVE_PERCENT_YIELD_ASSUMPTION`, `CONF_LASER_IONISATION_EFFICIENCY`). Two further
quantities stay open by the sources' own statements: the hybrid target gives 6 × 10⁻⁴ ultra-slow muons
per p–Li collision with the muon-to-muonium conversion set to one (η_conv "has not, however, been
separately quantified"; `SOURCE_HYBRID_MU_TO_MUONIUM_CONVERSION_SAKAKI2026` = null), an
order-of-magnitude pre-extraction rate of η_conv × 1.2 × 10¹² s⁻¹ per MW
(`test_sakaki2026_pre_extraction_rate_upper_limit`), with extraction, second-stage cooling and
emittance outside the paper's scope (`SOURCE_HYBRID_EXTRACTED_USM_RATE_SAKAKI2026` = null); and Bakule
2013 scales the flat-aerogel vacuum yield of 4.8 × 10⁻³ per incident muon to 9.6 × 10⁻⁴ for J-PARC beam
conditions (`SOURCE_MU_VACUUM_YIELD_JPARC_SCALED_BAKULE2013`, p.10;
`test_bakule2013_vacuum_yield_scaling_to_jparc_beam`), a figure that laser ablation later raised
(Beare 2020: 5–28 ‰ for ablated targets against < 5 ‰ for flat ones, p.19).

### 10.4 The muonium-formation discrepancy and its origin

The 0.52 used in the J-PARC and μTRISTAN budgets is a **MuSR measurement**: "the fraction of
muonium formed in the three aerogel samples was 0.52 ± 0.01" (Bakule et al. 2013, `SRC_ARXIV_1306_3810`
p.3; `SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAKULE2013`). Beare et al. 2020 and Aritome et al. 2024
cite it directly; for Abe 2019, the Zhang deck ("from TRIUMF measurement") and μTRISTAN (numbers from
C. Zhang) the attribution is inferred, not cited. Beare et al. 2020 measured 0.655 ± 0.018 on
different samples — all aerogel targets of their study combined, laser-ablated and flat, silica and
PMSQ (p.23) — (`SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020`, p.25, eq. (4)) and state that the
discrepancy "is not understood well". The two are 6.6 σ apart with both uncertainties
(7.5 σ with Beare's alone; `test_bakule2013_formation_fraction_vs_beare2020_combined_significance`,
`test_muonium_formation_fraction_two_values_are_incompatible`). They are **two measurements, kept
both, never averaged**: a source-chain model names the target type it represents and uses that
sample's value (`CONF_MUONIUM_FORMATION_FRACTION`). The Phase-0 synthetic band 0.3–0.7 contained both.

### 10.5 The space-charge finding

Nakazawa's assessment for LHμC bunch charges (p.16): 10¹⁰ μ⁺ per bunch = 1.6 nC; in a ~2 ns FWHM
pulse this is ≈ 0.75 A at the RFQ entrance; "30 mA H⁻ ≃ 3.4 mA μ⁺ (same K, same β)"; hence "220
larger perveance(K) scale than the original 30-mA H⁻ RFQ at the entrance"
(`SOURCE_RFQ_PERVEANCE_RATIO_WS2026_NAKAZAWA`, reported_lhmuc, P1; `test_nakazawa_space_charge_scaling`),
and ~10 A at the RFQ exit for σ ≈ 50 ps. The conclusion on p.17 is that the front end must be
re-optimised including 3D space charge. Consequence for this repository: a scaled J-PARC front end is
**not** adopted for any high-bunch-charge scenario; front-end transmission, emittance growth and bunch
length for ≥ 10¹⁰ μ⁺ per bunch are unknown (`CONF_FRONT_END_SPACE_CHARGE`, `ME_033`). The DIS2026
bunch population (0.07 × 10¹¹ = 7 × 10⁹) is of the same order.

### 10.6 vFFA: preliminary values and an analytic design note

The Kraków deck's vFFA numbers are **reported_lhmuc but preliminary**: an analytic parameter study
"in untested region of parameter space" for one arc pair from 70 to 500 GeV, with peak dipole field
~8 T at field index 60 /m (excursion ~3 cm), ~10 T at ~44 /m, relaxed < 9 T (< 30 /m, < 7 cm)
(pp.35–36); the integrated full-ring simulation is still to be done (p.46). The MuCol M17 report
(`SRC_DOI_10_5281_ZENODO_15054073`) designs IMCC stages, not the LHμC booster: stage 1 (0.06 → 0.3 TeV,
5990 m) has 6.93 T on orbit, which is the **F-magnet** field, and 12.52 T in the good-field region;
stage 4 (1.5 → 5 TeV, 35 000 m) has 13.59 T on orbit, which is the **reverse-bend D-magnet** field,
and 29.04 T good-field (`test_tabulated_peak_fields_are_f_magnet_stage1_and_d_magnet_stage4`,
`test_good_field_region_peak_implies_vertical_extent`). Its design limit is the LHC dipole field
8.3 T, which stage 4 exceeds (`test_lhc_dipole_reference_limit`). The lattices are analytic — no
tracking, non-linear or longitudinal study — and the printed eq. (2.7) appears to contain a
typographical error (`test_printed_eq27_inconsistent_with_closed_orbit_geometry`; no record uses it).
The LHμC 70 → 500 GeV booster lattice is in neither M17 nor MR7 (`ME_027`, `CONF_VFFA_PEAK_FIELD`).

### 10.7 RF for the hybrid-source option only

The baseline ultra-cold source needs no ionisation cooling; the hybrid option does (Rogers lists "RF
Breakdown (sparking) in solenoids" among its challenges, p.15). Giove 2026 (`SRC_IMCC2026_GIOVE_RF_SYSTEM`)
describes thin-window cavities with 704 MHz as the reference frequency of the first cells and
"gradients of 30 MV/m" (p.3), but shows **no gradient or breakdown measurement**
(`SOURCE_COOLING_RF_BREAKDOWN_DATA_GIOVE2026` = null). The in-field breakdown data restated by Rogers
(p.17) favour beryllium (Cu 24.4 → 12.9 MV/m at 0 → 3 T; Be 41.1 → > 49.8 MV/m), while INFN plans
aluminium windows for the demonstrator because of beryllium supply and safety (Giove pp.11–12). **No
uploaded source has aluminium in-field breakdown data.**

### 10.8 Physics comparators and the μ⁻ vs μ⁺ caveat

Cheung & Wang 2021 study μ⁻p; the MuIC paper's "LHmuC" is an IMCC 1.5 TeV beam on LHC protons. For
that MuIC column the charged-current rates differ by charge at high Q²: Q² > 10⁶ GeV² gives 0.098 pb
for μ⁻p → ν_μX and 0.024 pb for μ⁺p → ν̄_μX (`PHYS_XSEC_CC_MUM_Q2GT1E6_LHMUC_MUIC2022`,
`PHYS_XSEC_CC_MUP_Q2GT1E6_LHMUC_MUIC2022`, Table 4 p.22). The μLHC W-fusion Higgs cross section implied
by its yearly yield (385 fb, `PHYS_HIGGS_WFUSION_XSEC_IMPLIED_MULHC`) and Cheung & Wang's 0.978 pb
(`PHYS_VBF_HIGGS_XSEC_WW_MUP1_CHEUNG2021`) belong to different processes (μ⁺p vs μ⁻p) and are never
averaged or compared as a discrepancy.

### 10.9 Conflicts raised by the uploads

Nine conflict records were drafted in the registry stage of 2026-10-29, each with a named treatment:
`CONF_NOZZLE_OPENING_ANGLE`, `CONF_MUONIUM_FORMATION_FRACTION`, `CONF_LASER_IONISATION_EFFICIENCY`,
`CONF_SOURCE_CONCEPT`, `CONF_IR_LSTAR`, `CONF_DETECTOR_SOLENOID_FIELD`, `CONF_VFFA_PEAK_FIELD`,
`CONF_TEV_MUON_RESOLUTION`, `CONF_FRONT_END_SPACE_CHARGE`; several Phase-0 records were extended
(e.g. `CONF_PEAK_LUMINOSITY`, `CONF_PROTON_BUNCH_POPULATION_AND_NUMBER`, `CONF_LHEC_CROSSING_ANGLE`,
`CONF_JPARC_IHDTL_ENERGY`). The committed file at `104073c` holds the 15 Phase-0 records; the
authoritative list after the registry stage is `research/source_conflicts.yaml`. Under the §4 rule of
`research/source_quality_policy.md` a competitor of a conflict without a decided treatment is capped
at `low`; every conflict written in this stage names a treatment.

### 10.10 Label hygiene of 2026-10-29

The extraction briefs of Phase 0 and of the addendum batches had allowed `high` confidence for any
value read directly from a page, and agents had assigned P1 after arithmetic in scratch scripts. On
2026-10-29 the lead lowered **1423 confidences** to the caps of `research/source_quality_policy.md`
§4 (1088 in commit `03e0ab1`, 170 in `9484d49`, 165 in `1252bf2`; by rule 770 `analogous`, 526
unrefereed slides, 127 `imported_related` from a design variant) and **847 P1 labels** that named no
registered test to P0 (327 in `a8de068`, 520 in `1252bf2`); values, quotations and every other field
were unchanged (`research/_fragments/confidence_caps_applied_2026-10-29.csv`,
`research/_fragments/validation_levels_lowered_2026-10-29.csv`). Both rules are now validator errors
(`lhmuc/registry.py`), so the lowered labels cannot silently return. The arithmetic text remains in
`validation.methods` as a candidate check that becomes P1 when a test exists. One gap is noted, not
changed here: scenario-level `validation_level` labels (P1 on 33 of the 36 scenarios) are not covered
by the record-level P1 rule.
