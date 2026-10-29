# LHμC-VirtualLab — Scientific scope

**Document date:** 2026-10-28 · **Addendum:** 2026-10-29 (§1.7–§1.11 and dated notes) ·
**Project phase:** Phase 0 (evidence and feasibility audit) ·
**Owner:** David Hausler · **Companion documents:** `CLAUDE.md` (binding rules),
`docs/architecture.md` (repository layout), `docs/limitations.md` (what is not known or not
verified), `docs/reports/M1_addendum_uploaded_documents.md` (the addendum audit).

> **No digital twin of the LHμC exists.** This document describes what the platform is *for*, what
> the sources say the LHμC *is*, and which physics models are *in scope*. It does not describe a
> model that has been built. On 2026-10-28 the repository holds sourced parameter records,
> scenario definitions, schemas, closed-form (P1) audit arithmetic and tests. There is no CAD
> geometry, no lattice, no event sample, no detector simulation and no user interface.
> *[2026-10-29: still true. The evidence base grew from 5 to 34 uploaded documents (the Kraków
> workshop decks, related-machine papers, source-chain measurements, the AloHEP method paper and
> the MuCol vFFA report); §1.7–§1.11 summarise what they report. Every value they give for the
> LHμC is reported in workshop material and unverified by simulation.]*

---

## 1. The LHμC as described by its proponents

Everything in this section is a *summary of claims made in the sources*, with the source id and
page. None of it has been independently verified by this project beyond the P1 arithmetic listed
in §4 (corrected 2026-10-29; the Phase-0 text pointed to §5). Values marked **(related machine)**
describe the predecessor μLHC concept, not the LHμC.

### 1.1 Concept and headline parameters

| Item | What the source says | Source |
|---|---|---|
| Collision | "a 1 or 2 TeV μ⁺ beam collides with a 7 TeV proton beam, resulting in the μ⁺p centre-of-mass energy of 5.3 or 7.5 TeV, respectively, at an average luminosity close to 10³⁴ cm⁻²s⁻¹" | `SRC_ARXIV_2610_35154` (arXiv:2610.35154v1), abstract p.1 |
| Example parameter set, labelled "Example of the LHμC parameters" | √s 5.3 TeV; peak L 2.1 × 10³⁴ cm⁻²s⁻¹; collision (repetition) rate 4 MHz (12.5 Hz); RMS beam size at IP σ_x,y 4.8 μm for both beams; bunch population 0.07 × 10¹¹ μ⁺ and 22 × 10¹¹ p | same, Table 1 p.4 |
| Bunch train | "The μ⁺ train stored in the main ring in this case contains 80 bunches separated by 250 ns, and the repetition rate is 12.5 Hz" | same, §2 p.4 |
| Assumptions behind Table 1 | "μ⁺ yields at a level of 5% of the ones in the μTRISTAN proposal, a 4 MW proton driver, and the possibility of an increased population of LHC proton bunches due to their smaller number" | same, §2 p.4 |
| Rings | booster "of about 9 km circumference"; main ring "of about 3(6) km positioned tangentially to the LHC" for 1 (2) TeV | same, §2 p.4, Fig. 2 p.3 |
| White-paper working points | option 1: E_μ = 500 GeV, √s ≃ 3.7 TeV, L_int = 250 fb⁻¹; baseline: 1 TeV, 5.3 TeV, 1000 fb⁻¹; option 2: 2 TeV, 7.5 TeV, 1000 fb⁻¹ — "From HELP4CERN White Paper (in preparation)" | `SRC_WS1681458_KHANPOUR_GAMMAGAMMA`, slide 4 |
| Di-Higgs study configuration | E_μ = 500 GeV and 1 TeV on E_p = 7 TeV, √s = 3.74 and 5.29 TeV, L = 1 ab⁻¹ | `SRC_WS_LEBOHO_KUMAR_DIHIGGS`, slide 6 |

The 2.1 × 10³⁴ figure is a *peak* value from an explicitly labelled example; the abstract's
"close to 10³⁴" is an *average*. The platform keeps both as separate parameter records
(`MACHINE_PEAK_LUMINOSITY_DIS2026`, `MACHINE_AVERAGE_LUMINOSITY_DIS2026`) and does not reconcile
them.

### 1.2 The predecessor μLHC (related machine)

The only beam-optics-level numbers for a μ⁺p collider at CERN come from the μLHC paper
(`SRC_ARXIV_2506_15445`, Akturk et al., PTEP 2026 033C04, arXiv:2506.15445v2), which is a
*related machine*: same source technology, same 1 TeV × 7 TeV collision, same 3 km ring idea, but
40 bunches instead of 80, HL-LHC-like proton bunches (22 × 10¹⁰) and μ⁺ optics "adapted from the
μ⁺ beam detailed in the μ⁺e⁻ collider proposal" of μTRISTAN (p.11). Its records carry
`provenance.status: imported_related`.

| Item | Value (related machine) | Source page |
|---|---|---|
| μ⁺ per bunch | 3.7 × 10¹⁰ (μTRISTAN-based booster) / 3.0 × 10¹⁰ (LHeC-ERL-based booster) | Table 1, p.12 |
| β*_x / β*_y at IP, bunch length, ε_n | 3 cm / 0.7 cm, 2 mm, 4 μm (both planes) | Table 1, p.12 |
| Bunches, collision frequency, circumference | 40, 4 MHz, 3 km | Table 1, p.12 |
| Protons | 22 × 10¹⁰ per bunch, 7 TeV, β* 7 cm, ε_n 2 μm, 2760 bunches, 11245 Hz, 26.7 km ("ERL60-upgraded proton parameters", from the LHeC CDR) | Table 2, p.12 |
| Luminosity (AloHEP) | 8.8 × 10³³ / 7.2 × 10³³ cm⁻²s⁻¹; σ_x,y 4.3 μm for both beams | Table 3, p.12 |
| Booster survival | "approximately 82%" after 16 turns, 212 MeV → 960 GeV (μTRISTAN racetrack: two 3 km linacs, 1 km radius arcs); "approximately 67%" after 50 turns to 1 TeV in the LHeC ERL racetrack (two ~1 km linacs, 10 GeV per pass) | §2.2.1 p.6, §2.2.2 p.8–10 |
| Nozzle | "shielding tungsten nozzle cladded with borated polyethylene"; "6-meter-long tungsten shielding cone"; Geant4/FLUKA: "19 % and 81 %" of a 1 TeV muon's energy deposited / passing | §2.4 p.13–14 |

The Nucleus-Options deck (`SRC_WS1681458_DAGLI_NUCLEUS`, slide 8) restates the 3.0 × 10¹⁰ μ⁺,
β* 3.0/0.7 cm, 2 mm, 4 μm, 40-bunch, 4 MHz, 3 km table as "Table 1 of the draft; optics values from
the μTRISTAN μ⁺e⁻ design", so the same optics numbers also appear with a `PRIMARY_LHMUC` source;
the platform keeps the two documents' records separate (`_MULHC` and `_NUCL` id tags).

### 1.3 Ultra-cold μ⁺ source

"the LHμC concept primarily relies on the source of ultra-cold anti-muons recently developed at
J-PARC and KEK, rather than using the conventional ionisation cooling approach … the muon cooling
goes via stopping muons from the pion decays in aerogel where 'thermal' muonia are formed and then,
after diffusing out, are ionised by a laser. Clearly, this technique is only applicable for the μ⁺
production." (`SRC_ARXIV_2610_35154` §2 p.3). Modifications cited: proton-beam re-use for
multiple target hits (a second RCS), new aerogel configurations, hot tungsten wires, two-step
cooling, a hybrid source, and pre-acceleration to ~GeV (p.4). The μLHC paper summarises the
μTRISTAN production chain (40 recirculations over a 10 mm graphite target, 0.016 π/p, ~1000-layer
tungsten stopping target, rate enhancement O(10⁵) over J-PARC MLF; `SRC_ARXIV_2506_15445` §2.1
p.5). **No LHμC-specific source rate, bunch charge or emittance is given in any uploaded
source**; the DIS2026 paper gives only the "5% of μTRISTAN" yield assumption.
*[Update 2026-10-29: two LHμC-specific numbers now appear in workshop material — a μ⁺ rate into
the booster of 3 × 10¹³ s⁻¹ in the Forthomme beam set (`SOURCE_MU_RATE_INTO_BOOSTER_WS2026_FORTHOMME`,
p.17) and a bunch charge of 10¹⁰ μ⁺ = 1.6 nC in Nakazawa's space-charge assessment
(`SOURCE_BUNCH_CHARGE_1E10_WS2026_NAKAZAWA`, p.16). Both are requirements or scenarios, not source
designs; the source emittance for the LHμC is still not given. Two source concepts are now
documented, see §1.8.]*

### 1.4 Rapid acceleration

"The rapid acceleration of anti-muons from an energy of 1 GeV to the collision energy of 1 or 2
TeV is one of the most critical challenges of the LHμC design." The proposal is a vertical
Fixed-Field Alternating Gradient (vFFAG) scheme: "if one assumes a three-pass acceleration to
70 GeV, inherited from the nominal LHeC design, adding one vFFAG beamline might allow for further
acceleration up to 500 GeV. Therefore, one can expect to reach a 1 TeV energy and beyond using a
one-pass LHeC and two vFFAG beamlines, for example." (`SRC_ARXIV_2610_35154` §2 p.4). No vFFA
field, aperture, RF or lattice parameter for the LHμC is given.
*[Update 2026-10-29: the Kraków vFFA deck now gives preliminary analytic field, field-index and
excursion options for a 70 → 500 GeV arc pair; aperture, RF and lattice are still not given. See
§1.9.]*

### 1.5 Interaction region and detector

The DIS2026 paper lists *options*, not a design: muon focusing either "in between" or "outside"
the LHC mini-beta quadrupoles; "a very small crossing angle is needed to avoid parasitic
collisions"; "the most preferred scheme is by introducing a new separator dipole"; decay-background
shielding "has to be studied" (§3 p.4–5). The detector baseline is the LHeC detector with "only
relatively minor modifications", plus a nozzle "inside the LHμC detector in the direction of
incoming muons" whose "size has to be carefully optimised"; a CMS-like muon system for high-p_T
muons, special near-beam solutions for small-angle scattered muons, bremsstrahlung luminosity
measurement, negligible-or-small pile-up and triggerless DAQ are mentioned as considerations
(§4 p.5). No dimension, field, angle or material thickness is given for the LHμC detector.
*[Update 2026-10-29: the Kraków detector and nozzle decks now give the nozzle opening angle,
length, tip distance and material as study options, and muon-system resolution targets; no solenoid
field, dimension table or material thickness is given for the LHμC detector. See §1.7.]*

### 1.6 Physics programme (as claimed)

- **QCD at small x and high Q²**: kinematic reach extended "by more than one order of magnitude
  with respect to the LHeC and by more than two orders wrt. HERA" (Fig. 1 p.2); non-linear parton
  dynamics, nuclear effects, PDF flavour decomposition, α_S. μLHC Table 5 (p.15): x = 3.6 × 10⁻⁷
  at Q² = 10 GeV² for √s = 5.3 TeV.
- **Electroweak precision**: M_W and sin²θ_W "due to the significantly larger span in Q²" (p.2).
- **Higgs**: couplings to Z and W; possible self-coupling measurement (p.3). Di-Higgs benchmark
  μ⁺p → hh j ν̄_μ, h → bb̄: σ ≈ 0.17 fb at √s = 3.74 TeV and ≈ 0.33 fb at 5.29 TeV; S/√(S+B) ≈ 4.25
  at 1 ab⁻¹ with 70 % b-tagging; 95 % CL g_hhh range [−0.26, 1.40] at 1 ab⁻¹
  (`SRC_WS_LEBOHO_KUMAR_DIHIGGS` slides 7, 12, 14, 15). μLHC Table 6 (p.17): 27 500 / 33 900
  W-fusion Higgs per 10⁷ s year.
- **Top**: "top-quark factory", threshold studies, top charge, single top, rare decays (p.2–3).
- **BSM**: generic searches (p.3, citing arXiv:2101.10476); colour-octet muons μg → μ₈ with a
  5σ discovery reach "approximately … 4100 GeV" at 100 fb⁻¹ (related machine, `SRC_ARXIV_2506_15445`
  §3.3 p.17–20); excited muons, leptoquarks, contact interactions listed in its conclusion (p.20).
  Heavy-neutral-lepton and extended-Higgs (2HDM+VLQ) benchmarks are *candidates* whose papers are
  not available in this environment (see `docs/limitations.md` §6).
- **Two-photon physics**: EPA-factorised γγ → τ⁺τ⁻ (58.5 pb at 3.7 TeV, 70.3 pb at 5.3 TeV for
  W₀ = 10 GeV), γγ → W⁺W⁻ (0.166 pb at 3.7 TeV), anomalous τ moments, quartic couplings
  (`SRC_WS1681458_KHANPOUR_GAMMAGAMMA` slides 9, 15, 19).
- **Neutrino beams**: "very intense and highly collimated in three different directions — along two
  booster linacs as well as the straight section of the main ring", energies "from 1 GeV to the top
  energy" (p.4).
- **Nucleus options**: μ⁺ on LHC Pb, Xe, O, Ne beams; √s per nucleon ≈ 3.3 TeV; AloHEP luminosities
  per nucleon from 0.32 to 4.49 × 10³² cm⁻²s⁻¹ before the ion tune-shift limit, ≈ 1 × 10³² (μ–O)
  after it; μ⁺ optics "relaxed to match (β*_μ ≈ 7–15 cm)" (`SRC_WS1681458_DAGLI_NUCLEUS` slides
  10–14).

### 1.7 Detector concept as presented at the Kraków workshop (addendum 2026-10-29)

Four decks of the HELP4CERN workshop "Ultra-cold muons for the LHC" (Kraków, Indico 1681458,
24–26 Sept 2026) describe the LHμC detector. All are unrefereed slides (`PRIMARY_LHMUC`, confidence
capped at `medium`); the speakers call the concept work in progress, and nothing below has been
simulated by this project.

- **Main detector — Forthomme** (`SRC_WS1681458_FORTHOMME_DETECTOR`). "Minor adaptations to LHeC
  detector concept", e.g. asymmetric pixel/tracker, ECAL/HCAL, muon system, solenoid between the
  calorimeters (`DET_LHMUC_DESIGN_BASIS_WS2026_FORTHOMME`, p.9); a conical tungsten nozzle with
  borated-polyethylene cladding around the μ⁺-side beam pipe, "conical half opening angle: 40(100)
  mrad → η_max ~ 4(3)", trading beamline protection against forward hadron acceptance (p.9); a more
  uniform tracker radiation profile than at the LHeC, an inner-tracker dose of order MGy from
  machine-induced background and muon-decay products, and a "PPS-like" inner-tracker replacement
  between LHeC and LHμC modes (p.10); tighter timing (4D tracking) with looser vertexing requirements
  (p.10); relaxed ECAL and finer HCAL requirements (p.11); a muon system with ∫B·dl of 10–30 T m,
  ≈ 0.1 ns timing for beam-muon rejection and extended backward chambers around the nozzle
  (`DET_MUON_BDL_LHMUC_*_WS2026_FORTHOMME`, `DET_MUON_TIMING_RESOLUTION_TARGET_WS2026_FORTHOMME`, p.12);
  possibly a streamed DAQ without online trigger (p.14). Simulation status: LHeCSW on the Key4hep
  stack with minimal adaptation for the nozzle; fast simulation (Delphes) available for LHeC, "not
  yet for LHμC" (`DET_LHMUC_FAST_SIMULATION_STATUS_WS2026_FORTHOMME`, pp.13–14). The backup slide
  p.17 carries the second LHμC beam set (40 bunches of 10¹⁰ μ⁺, 300 ns, σ 4.3 µm, β*_p 7 cm, 10³⁴ cm⁻²s⁻¹;
  scenario `LHMUC-WS2026-FORTHOMME`).
- **Nozzle — Kilic** (`SRC_WS1681458_KILIC_NOZZLE`). Beam-induced background from the photons,
  electrons and neutrons of muon-beam decay products, mitigated by timing, IR lattice design and
  shielding nozzles (p.3); a single conical tungsten nozzle cladded with borated polyethylene on
  the incoming-muon side, drawn with a 487.8 cm rear section, a 100 cm tip section and the tip 6 cm
  from the IP (p.4), inserted in the LHeC detector design of the ESPP 2025 symposium (p.5); half
  angles 40 and 100 mrad, with 60 and 80 mrad in the acceptance scan (pp.5, 12). Geant4 11.4 with
  MadGraph5_aMC@NLO → Pythia 8.312 → HepMC 2.06.11, μ⁺ 1 TeV on p 7 TeV, 250 000 events (pp.6–7).
  Results as stated: "Approximately 99.9% of IP-originating hadrons are absorbed by the nozzle"
  (p.22); ≈ 10–11 % energy loss and ≈ 2.5–2.7 % Q² smearing for very forward scattered muons
  (pp.16–19). No beam-induced-background simulation is shown.
- **TeV muons in the main detector — Yamazaki** (`SRC_WS1681458_YAMAZAKI_TEV_MUON`). Scattered muons
  of 500 GeV – 5 TeV in −3 < η < 3 (p.2); "The resolution we can achieve at 1 TeV: 6-7 %", with the
  integrated field the most important factor and steel or air-core apparently not mattering (p.10),
  but "This muon momentum resolution is insufficient to reconstruct (x, Q2) in many regions", so the
  Jacquet–Blondel and double-angle methods and jets play a larger role than at an electron machine
  (pp.10–16).
- **Near-beam muons — Acosta** (`SRC_WS1681458_ACOSTA_NEAR_BEAM`). DIS kinematics require tagging
  TeV muons down to η = −7 (2 mrad) (p.4); a far-forward toroid strawman with three stations at 28,
  140 and 660 m covering 2.4 < |η| < 7.2 and "~6 %" at 1 TeV in a Geant4 model (pp.11–12); a cathode-
  strip-chamber strawman (pp.16–21); "BIB impact on potential detectors would need study" (p.22).

Comparators read in full: the LHeC detector paper (3 T solenoid, `SRC_ARXIV_2201_02436` p.10), the
LHeC Delphes card restated by Forthomme (Bz = 3.8 T, p.13), the IMCC nozzle and MDI of MuCol MR7
(10°, base at 595 cm, tip 6 cm, L* = 6 m; `SRC_ARXIV_2510_27437` pp.65–66) and the 10 TeV detector
concepts MAIA and MUSIC (5 T; `SRC_ARXIV_2502_00181` p.17, `SRC_ARXIV_2601_13189` p.2). The LHμC
values and these comparators are kept apart (`CONF_NOZZLE_OPENING_ANGLE`, `CONF_DETECTOR_SOLENOID_FIELD`,
`CONF_IR_LSTAR`, `CONF_TEV_MUON_RESOLUTION`). **In scope for the platform:** a parameterised G0/G1
nozzle and envelope geometry per option, and a fast-simulation placeholder once a detector card with
provenance exists (M2). **Not yet possible:** any background, dose or acceptance result of this
project (no Geant4, FLUKA or detector geometry, `docs/limitations.md` §4).

### 1.8 Two source concepts (addendum 2026-10-29)

DIS2026 says the LHμC "primarily relies on the source of ultra-cold anti-muons recently developed at
J-PARC and KEK" and lists "a hybrid source" among the modifications considered (p.3–4). The uploads
document both routes; the repository keeps them as separate source scenarios and transfers no yield
between them (`CONF_SOURCE_CONCEPT`).

- **A — ultra-cold muonium source with laser ionisation** (J-PARC/KEK, μTRISTAN). Surface μ⁺ stop
  in silica aerogel, form muonium, diffuse out and are laser-ionised (122 + 355 nm), then
  re-accelerated. Sub-variants: the aerogel multi-layer target of Zhang
  (`SRC_WS1681458_ZHANG_MUONIUM`), whose μTRISTAN budget after stopping is 0.52 × 0.6 × 0.6 × 0.73 =
  0.137 (p.20), and the μTRISTAN hybrid target of Sakaki et al. 2026 — a liquid-lithium target
  surrounded by multilayer tungsten at 2000 K, 6 × 10⁻⁴ ultra-slow muons per p–Li collision with the
  muon-to-muonium conversion set to one (`SRC_ARXIV_2605_25580` pp.2–7; scenario
  `MUTRISTAN-HYBRID-TARGET-2026`). Measured status: 2.1 × 10⁻⁸ μ⁺ at 100 keV per surface muon in the
  2024 J-PARC test, with a 244 nm spectroscopy laser (`SRC_ARXIV_2410_11367` pp.2–4); muonium
  formation 0.52 ± 0.01 (Bakule 2013) and 0.655 ± 0.018 (Beare 2020) on different samples; the 73 %
  ionisation efficiency of the budgets is a calculation (`SRC_ARXIV_1901_03047` p.8). The gap between
  the measured chain and the budgets is set out in `docs/limitations.md` §10.3–§10.4.
- **B — hybrid source** (Rogers, `SRC_WS1681458_ROGERS_HYBRID_SOURCE`). IMCC capture, rectilinear
  stage-A ionisation cooling, deceleration and low-energy cooling (p.5), motivated by the
  observation that stopping an uncooled 200 MeV muon would need 39 m of aerogel (p.3); "Estimate
  0.04 μ⁺ per 5 GeV proton on target to end of A-stage" (p.14); the deceleration is "Not designed"
  (p.13); cost scale "~ O(500) MCHF" (p.15); RF breakdown in solenoids is a listed challenge (p.15).
  This option re-introduces ionisation cooling, the technology the U.S. Muon Collider Collaboration
  calls "the biggest risk in the collider's luminosity performance" for a μ⁺μ⁻ collider
  (`SRC_ARXIV_2609_37117` p.2). Its RF context is Giove 2026 (`SRC_IMCC2026_GIOVE_RF_SYSTEM`):
  thin-window cavities at 704 MHz and 30 MV/m, no breakdown data shown, aluminium windows planned
  for the demonstrator (pp.3, 11–12).

Common to both: the front end. Nakazawa's assessment (`SRC_WS1681458_NAKAZAWA_LOW_VELOCITY` p.16)
gives 10¹⁰ μ⁺ in ~2 ns ≈ 0.75 A at the RFQ entrance, 220 × the generalised perveance of the 30 mA H⁻
RFQ design, and concludes that the front end must be re-optimised including 3D space charge (p.17;
`CONF_FRONT_END_SPACE_CHARGE`). **In scope:** the yield chain as a product of sourced factors with
each factor's provenance and range (M2), reported per source concept and per laser scheme. **Out of
scope until a design exists:** any LHμC source rate presented as achievable.

### 1.9 The vFFA booster and the MuCol M17 design note (addendum 2026-10-29)

- **Kraków deck — Topp-Mugglestone** (`SRC_WS1681458_TOPPMUGGLESTONE_VFFA`). Requirement: inject at
  70 GeV, extract at 500 GeV ("to 1 TeV?"), energy-gain factor 10–20, order-10 turns, a
  sub-millisecond cycle (p.3). RCS, hybrid-RCS and separated-arc RLA options are compared (pp.8–11);
  the vFFA (B = B₀ e^{mZ}, zero momentum compaction, fixed field and fixed path length, on-crest
  acceleration with up to √2 more voltage per cavity power; pp.23, 37) is assessed in the words "vFFA
  is good candidate for LHμC concept", and the long LHμC straights as an ideal testbed for decoupled
  insertions (p.44).
  Preliminary analytic options for a single arc pair: ~8 T at field index 60 /m with ~3 cm
  excursion, ~10 T at ~44 /m, relaxed < 9 T at < 30 /m and < 7 cm (pp.35–36). Status: "promising
  candidate", integrated full-ring simulation pending, magnet design the main unknown, tracking with
  Fixfield (pp.45–46).
- **MuCol Milestone Report 17** (`SRC_DOI_10_5281_ZENODO_15054073`, Topp-Mugglestone, 27 Mar 2025).
  A tentative vFFA design for IMCC stages 1 (0.06 → 0.3 TeV, 5990 m) and 4 (1.5 → 5 TeV, 35 000 m),
  with an analytic closed-orbit geometry (eqs. (2.1)–(2.6)), Table 2.2 inputs and Table 2.3 results.
  The tabulated "Peak Dipole Field On Orbit" is the F-magnet field for stage 1 (6.93 T) and the
  reverse-bend D-magnet field for stage 4 (13.59 T); the good-field peaks are 12.52 T and 29.04 T.
  The design limit is the LHC dipole field 8.3 T (p.10), which stage 4 exceeds. The lattices are
  analytic: "The lattices proposed using the analytic formalism here must also be verified using
  numerical simulation" (p.15); the printed eq. (2.7) appears to contain a typographical error. MR7
  Table F.5 restates stage 1 (orbit radius 953 m, 6.93 T on orbit); Bρ(0.3 TeV)/953 m gives a mean
  bending field of 1.05 T (`test_vffa_rigidity_and_mr7_vffa1_mean_bending_field`, arithmetic of this
  project). The M17 arithmetic is pinned in `tests/scientific/test_mucol_m17_vffa.py`.

The LHμC 70 → 500 GeV booster is designed in neither M17 nor MR7. **In scope:** a toy vFFA cell built
from the M17 geometry and the Kraków options as a G0 placeholder and as the first optics-code
cross-check object (M2–M3). **Not in scope:** claims of an LHμC booster lattice, survival or field.

### 1.10 The small-x programme (addendum 2026-10-29)

The AGH deck "High energy QCD at LHμC" (`SRC_WS1681458_HEQCD_SMALLX`; speaker not named on the
slides) gives the physics case: x_Bj ≲ 10⁻⁷ at Q² ∼ 1 GeV² for 0.004 < y < 1, one order of magnitude
beyond the LHeC and "comparable (or better!) with FCC-eh" (p.13); a large difference between
fixed-order and NLLx-resummed gluons (p.14); huge resummation uncertainties below x ≈ 10⁻⁷, "exactly
the region where LHμC would provide data" (p.16); BFKL deviating from fixed-order NLO while
saturation (BK NLO) stays close to it (p.18); inclusive structure functions "not very
discriminatory", so complementary observables are needed — dijet, trijet, di-hadron and photon–jet
azimuthal correlations, exclusive processes, quarkonia (p.19); dijet predictions for μ⁺g → μ⁺j₁j₂ at
√s = 3742 GeV (p.20), a nuclear suppression R_Pb-p of up to 30 % (p.21) and trijet correlations as
saturation tests (p.23). The Forthomme kinematic plane (p.10) and Yamazaki's reconstruction-method
comparison (pp.11–15) bear on the same programme. **In scope (M3):** the kinematic reach and the
reconstruction resolution in (x, Q²) for the stated acceptance options. **Not reproduced:** any of
the deck's predictions.

### 1.11 Comparisons: the muon-ion collider paper and Cheung & Wang (addendum 2026-10-29)

Both papers are comparators, and both differ from the LHμC in a way that matters:

- **Muon-ion collider, Acosta et al.** (`SRC_ARXIV_2203_06258`, MuIC/MuIC2 at BNL plus an "LHmuC"
  column at CERN). That "LHmuC" is **not** the HELP4CERN LHμC: it is one 1.5 TeV beam of a 3 TeV IMCC
  μ⁺μ⁻ collider brought into collision with 7 TeV LHC protons (PDF p.6), √s = 6.5 TeV,
  2.8 × 10³³ cm⁻²s⁻¹, 237 fb⁻¹ in 10 years, ε_n = 25 µm and β* = 0.5 cm (PDF p.8; σ ≈ 3 µm,
  `test_muic_lhmuc_column_beam_size_acosta2022`), with the hourglass factor "assumed to be unity"
  (PDF p.7; `RISK_022_LHMUC_NAME_COLLISION`). Its cross-section tables give μ⁺p and μ⁻p separately;
  for its LHmuC column the charged-current rate at Q² > 10⁶ GeV² is 0.098 pb for μ⁻p and 0.024 pb for
  μ⁺p (Table 4, PDF p.22). Its Delphes card (Tables 16–18, PDF pp.41–45) is a candidate starting point
  for a fast-simulation placeholder, with that provenance.
- **Cheung & Wang 2021** (`SRC_ARXIV_2101_10476`, cited by DIS2026 for generic BSM searches, p.3).
  μp-1 is 7 TeV p × 1 TeV **μ⁻** (√s = 5.3 TeV) at an *assumed* 10³³ cm⁻²s⁻¹ and 0.1 ab⁻¹ (p.2), giving
  a WW-fusion Higgs cross section of 0.978 pb (Table II) and Δg_hbb/g_hbb = 0.69 % (pp.2–3, with
  FCC-ee inputs for g²_hWW/Γ_h); RPV-squark and muon g−2 reaches follow (pp.3–5). The μ⁺p value of the
  same cross section is an explicit unknown in this repository
  (`PHYS_VBF_HIGGS_XSEC_WW_MUPLUS_P_7TEV_1TEV_CHEUNG2021` = null).

**The μ⁻ vs μ⁺ caveat.** LHμC collides μ⁺, so charged-current processes (W-fusion Higgs, single top,
high-Q² CC DIS) run on different parton combinations than at a μ⁻p collider and have different rates
— the MuIC Table 4 numbers above illustrate the size at high Q². Cheung & Wang's cross sections and
precisions are therefore screening comparators only, and the μLHC W-fusion Higgs cross section implied
by its yearly yield (385 fb, `PHYS_HIGGS_WFUSION_XSEC_IMPLIED_MULHC`, from μLHC Table 6 p.17) is a
different process from Cheung & Wang's 0.978 pb: the two are never averaged and their difference is
not a discrepancy. **In scope (M3):** recomputing such processes for μ⁺p with a documented generator,
PDF set and scale choice, and comparing with both papers labelled as comparisons.

---

## 2. Central research question of the platform

> **Can the performance claimed for the LHμC — a 5.3 (7.5) TeV μ⁺p collider at average luminosity
> ~10³⁴ cm⁻²s⁻¹ built largely from LHeC infrastructure — be reproduced, bounded or refuted from
> traceable evidence and documented computation, and what would its physics programme actually
> deliver under the resulting uncertainty?**

Subsidiary questions, each answerable only with the stated evidence:

1. Which published numbers are mutually consistent (P1 arithmetic), which rest on assumptions
   not stated in the sources, and which are unknown?
2. What luminosity follows from a documented beam model (decay, hourglass, crossing angle,
   beam-beam) once the missing IR parameters are given as ranges rather than guesses?
3. What does the muon-decay background imply for a nozzle-shielded detector, and how much
   acceptance does the shielding cost?
4. Which theory benchmarks (di-Higgs, two-photon, colour-octet muons, HNL, extended Higgs) can be
   recast for the μ⁺p initial state with public models, and with what statistical power under
   parameter uncertainty?
5. Where in parameter space does a multi-objective, constraint-respecting optimisation point,
   and which conclusions remain blocked by unknown bounds?

A valid answer to any of these can be "cannot be evaluated because X, Y, Z are missing"
(`CLAUDE.md` §1.1, §1.10).

---

## 3. Scope of each milestone

Milestone contents follow `docs/architecture.md` §5. A milestone may *start* only when its entry
criterion is met; nothing below is claimed to exist unless marked present.

| Milestone | Scope | Entry criterion | Status 2026-10-28 |
|---|---|---|---|
| **M1 — Phase 0 evidence audit** (this phase) | Page-level extraction of the five uploaded documents into `parameters/**` with provenance; scenario definitions with explicit `unknown_roles`; source registry and search logs; conflict records; assumption records for any synthetic range; P1 arithmetic cross-checks; policy documents; the evidence-audit report | Uploaded documents available | in progress (parameters, scenarios, schemas, tests, this document present; several registries and policy documents being produced by parallel tasks) |
| **M2 — Analytical and conceptual model** | `physics/` analytical luminosity, decay, hourglass and beam-beam estimates with propagated ranges; G0/G1 parameterised placeholder geometry (`cad/`) tagged as such; fast detector parametrisation; minimal backend/front-end that *displays* provenance labels | M1 complete; assumption records exist for every synthetic range | not started |
| **M3 — Benchmarks and generation** | μ⁺p process derivation, event generation (MadGraph5_aMC@NLO / Pythia 8 via `pylhe`, `pythia8mc`), recasting of the di-Higgs and two-photon benchmarks, proposal records for HNL / 2HDM+VLQ once the papers are obtained; GDML simulation geometry and Geant4/BDSIM runs *only if those codes become available* | M2 complete; generator and UFO models obtained and licence-checked | not started |
| **M4 — Optimisation and uncertainty** | Objectives, hard constraints, Pareto studies, sensitivity and robustness with explicit `conclusions_blocked_by` lists | M3 complete; constraint bounds sourced or declared synthetic | not started |
| Later | Commissioning, virtual controls, machine protection | LHμC hardware specifications exist | no such specifications exist |

*Status 2026-10-29:* M1 remains in progress. The extraction and independent verification of the 29
addendum documents is complete and committed (5601 parameter records, 36 scenarios at `104073c`);
the registry stage (assumption supersession, conflicts, missing evidence, risks, validation rows) and
the addendum report `docs/reports/M1_addendum_uploaded_documents.md` are being finalised. M2–M4 are
not started; the inputs that the uploads make available to M2 are listed in `docs/roadmap.md` §2.
No LHμC hardware specification exists, so the entry criterion of the last row is still unmet.

---

## 4. Physics models in scope

The models below are the closed-form relations the platform uses for P1 checks now
(`lhmuc/analytical.py`, tested in `tests/scientific/test_analytical_checks.py`) and the
convolution-level models planned for M2–M3. Notation: E in GeV, c = 1 unless shown; m_μ =
0.1056583755 GeV, τ_μ = 2.1969811 μs, m_p = 0.93827208816 GeV (PDG 2024, recorded in the module
docstring).

**Lorentz factor and laboratory lifetime** (`gamma`, `tau_lab_s`)

    γ = E_μ / m_μ            τ_lab = γ τ_μ

For E_μ = 1 TeV: γ = 9464, τ_lab = 20.8 ms (matches "approximately 20 ms",
`SRC_ARXIV_2506_15445` p.11). For 2 TeV: 41.6 ms.

**Decay during storage** (`average_population_fraction`)

    N(t) = N₀ exp(−t/τ_lab)        ⟨N⟩/N₀ over a store of length T = (1 − e^{−T/τ_lab}) τ_lab / T

For T = τ_lab the average is 1 − e⁻¹ = 0.632 ("approximately 0.63", p.11; the Nucleus deck
slide 8 writes "≈ 0.64 N₀").

**Survival during acceleration** (`survival_linear_ramp`, `survival_racetrack_booster`)

    S = exp( − ∫ dt / (γ(t) τ_μ) ) = exp( − (m_μ/τ_μ) ∫ dt / E(t) )

For a linear ramp E₀ → E₁ in time Δt the integral is (m_μ/τ_μ) Δt ln(E₁/E₀)/(E₁ − E₀). Applied
turn by turn to the two racetrack boosters of the μLHC paper (linacs with linear gain, arcs at
constant energy) this gives 81.6 % (16 turns, 212 MeV → 960 GeV) and 67.4 % (50 turns, → 1 TeV)
against the paper's "approximately 82%" and "approximately 67%".

**Centre-of-mass energy** (`sqrt_s_gev`)

    √s ≈ 2 √(E_μ E_p)      (massless, head-on; exact form with masses also implemented)

500 GeV × 7 TeV → 3.74 TeV; 1 TeV × 7 TeV → 5.29 TeV; 2 TeV × 7 TeV → 7.48 TeV. Crossing-angle
and beam-energy-spread corrections are not included; the crossing angle is unknown.

**Muon–parton subprocess energy and kinematic reach** (`bjorken_x_min`)

    ŝ = x s          Q² = x y s          x_min(Q²) = Q² / s  (y ≤ 1)

x_min(10 GeV²) = 3.6 × 10⁻⁷ at √s = 5.3 TeV, reproducing μLHC Table 5. The DIS2026 Fig. 1 uses
the acceptance band 4 × 10⁻³ < y < 1, which the platform records but does not yet model.

**Luminosity** (`luminosity_naive_cm2s`, `luminosity_general_cm2s`, `hourglass_factor`)

    L = f_coll N_μ N_p H / ( 2π √(σ²_x,μ + σ²_x,p) √(σ²_y,μ + σ²_y,p) )
      = f_coll N_μ N_p H / (4π σ_x σ_y)   for equal beam sizes

    σ*_i = √( ε_n,i β*_i / (β_rel γ_i) )         f_coll = n_b f_rev  (or the stated collision rate)

H is the geometric reduction factor collecting the hourglass effect (computed numerically for
Gaussian bunches with σ_i(s)² = ε_i β_i (1 + s²/β_i²)), the crossing-angle (Piwinski) factor, and
the decay average ⟨N_μ⟩/N₀ where a time-averaged value is wanted. The naive formula with H = 1
reproduces the DIS2026 Table 1 peak luminosity (2.13 × 10³⁴ from 4 MHz, 0.07 × 10¹¹, 22 × 10¹¹,
4.8 μm); the status of H for the μLHC values is an open audit item described in
`docs/limitations.md` §5.

**Magnetic rigidity and bending field** (`brho_tm`, `bending_field_t`)

    Bρ [T m] = p [GeV/c] / 0.299792458        B = Bρ / ρ

960 GeV/c on a 1 km radius → 3.2 T (compare "alternative gradient bending magnets of 3 T",
`SRC_ARXIV_2506_15445` p.10); 1 TeV on a fully dipole-filled 3 km ring → 7.0 T. These are
fill-factor-1 bounds, not lattice designs.

**Hard-scattering cross section via PDF convolution** (planned, M3)

    σ(μ⁺p → X) = Σ_i ∫₀¹ dx f_i(x, μ_F²) σ̂( μ⁺ q_i(x P) → X ; ŝ = x s )

with f_i proton PDFs (the di-Higgs benchmark used CTEQ6L1; the platform will record the set and
scale) and σ̂ from a generator (MadGraph5_aMC@NLO with a documented UFO model). For two-photon
processes the EPA factorisation of `SRC_WS1681458_KHANPOUR_GAMMAGAMMA` slide 9 is in scope:

    σ_ℓp = ∫ dy_ℓ dy_p Φ_ℓ(y_ℓ) Φ_p(y_p) σ_γγ(W) = ∫ dW S_γγ(W) σ_γγ(W),   W² ≃ y_ℓ y_p s

**Beam-beam tune shift** (planned, M2; the Nucleus deck reports AloHEP values ξ_μ, ξ_A and a
stability limit ξ_A ≤ 0.01, slides 12–13). The platform will use the standard linear formula
ξ = N r₀ β*/(2π γ σ (σ_x + σ_y)) with the species' classical radius and will record it as an
analytical estimate only.

Every value these models produce carries `provenance.status: derived_lhmuc` or
`analytical_estimate` with a `derivation` string naming its inputs, and inherits the lowest
confidence of those inputs.

---

## 5. Out of scope (Phase 0 and, unless stated, later milestones)

- Any **lattice design** for the booster, vFFA beamlines or main ring; the sources give none.
- Any **engineering geometry** at G3 or higher; no magnet, cryostat, tunnel or civil-engineering
  data for the LHμC exist in the sources.
- **Ionisation-cooling or μ⁻ production** models (the concept is μ⁺-only). *[2026-10-29: the
  hybrid-source option (§1.8 B) uses IMCC capture and rectilinear stage-A ionisation cooling; it is
  recorded as a reported design option with its RF dependencies (Giove 2026), not modelled. μ⁻p
  physics (Cheung & Wang 2021; the μ⁻ columns of the muon-ion collider paper) enters only as a
  screening comparator, §1.11.]*
- **IMCC 10 TeV μ⁺μ⁻ designs as LHμC designs** (added 2026-10-29): MuCol MR7, M17, MAIA and MUSIC
  values are analogues for the nozzle, MDI, detector and vFFA; they are never re-derived or adopted
  for the LHμC without an assumption record.
- **Independent re-derivation of μTRISTAN, LHeC or HL-LHC designs**; their values enter only as
  `imported_related` with the importing document's quotation.
- **Cost, schedule, power and environmental assessments**; no source gives a number.
- **Detector performance beyond parametrised fast simulation** until Geant4/BDSIM are available
  and a GDML geometry has passed `cad/validation` (none exists).
- **Claims about physics sensitivity** that are not reproduced from a documented generator run
  with a documented model; slide-level numbers are recorded as reported, never re-used as results.
- **Neutrino-beam physics studies**; the platform records the claimed beam directions and energy
  band only.
- **FCC-hh / HE-LHC-based 30 (15) TeV muon-hadron options and FCC-μe** mentioned in the DIS2026
  outlook (p.5–6): recorded as statements, not modelled.
- **Web reconnaissance values** (`access: snippet_only`) as inputs to any computation.

---

## 6. Status statement

No digital twin of the LHμC exists in this repository or, to the project's knowledge, anywhere
else. The LHμC itself is a concept described in a 7-page proceedings paper and workshop slides; its
parameter table is explicitly an example; its white paper is "in preparation". The platform's
first deliverable is therefore an *audit*: a machine-readable statement of what is reported, what
is derived, what is imported from related machines, and what is unknown. Any later model will be
labelled with its geometry fidelity (G0–G5) and validation level (P0–P5) independently, and
synthetic inputs will be visible as ranges with assumption records wherever they are used.

---

## 7. Sources cited

| source_id | Reference | Access |
|---|---|---|
| `SRC_ARXIV_2610_35154` | K. Piotrzkowski on behalf of the HELP4CERN Study Group, "LHμC: A high energy, high luminosity muon-hadron collider at CERN", PoS DIS2026, arXiv:2610.35154v1 (26 Oct 2026), 7 pp. | uploaded; committed copy `references/primary/arXiv-2610.35154v1_Piotrzkowski_LHmuC_DIS2026.pdf` (CC BY-NC-ND 4.0) |
| `SRC_ARXIV_2506_15445` | D. Akturk et al., "μLHC: Antimuon Ring and HL-LHC based μ⁺p Collider", PTEP 2026 033C04, arXiv:2506.15445v2, 24 pp. (related machine) | uploaded; git-ignored local copy; metadata `research/archived_metadata/SRC_ARXIV_2506_15445.json` |
| `SRC_WS1681458_DAGLI_NUCLEUS` | B. Dagli et al., "LHμC: Nucleus Options", Kraków workshop (Indico 1681458, contribution 7263320), 16 slides | uploaded; git-ignored |
| `SRC_WS1681458_KHANPOUR_GAMMAGAMMA` | H. Khanpour, "Two-Photon Physics at the LHμC", Kraków workshop (contribution 7263325), 26 slides | uploaded; git-ignored |
| `SRC_WS_LEBOHO_KUMAR_DIHIGGS` | T. Leboho, M. Kumar et al., "Probing anomalous Higgs couplings at the future μ⁺p collider", Kraków workshop slides, 24 slides | uploaded; git-ignored |

Full records with SHA-256, licence and unresolved questions: `research/source_registry.yaml`
and `research/archived_metadata/`.

**Added 2026-10-29** (all `access: uploaded`, read in full; git-ignored local copies unless the
licence permits redistribution):

| source_id | Reference | Used in |
|---|---|---|
| `SRC_WS1681458_FORTHOMME_DETECTOR` | L. Forthomme, "LHeC/LHμC main detector", Kraków workshop slides (19 pp.) | §1.7, beam set p.17 |
| `SRC_WS1681458_KILIC_NOZZLE` | A. Kilic et al., "Nozzle design studies for mu+p collider detector" | §1.7 |
| `SRC_WS1681458_YAMAZAKI_TEV_MUON` | Y. Yamazaki, "Challenges of TeV-muon Detectors" | §1.7 |
| `SRC_WS1681458_ACOSTA_NEAR_BEAM` | D. Acosta et al. (Rice University), "Near-Beam Muon Detectors" | §1.7 |
| `SRC_WS1681458_ZHANG_MUONIUM` | C. Zhang, "Muonium diffusion modeling and multi-layer target design for muon laser ionisation cooling" | §1.8 |
| `SRC_WS1681458_ROGERS_HYBRID_SOURCE` | C. Rogers, "Hybrid Source of Ultra Cold Muons" | §1.8 |
| `SRC_WS1681458_NAKAZAWA_LOW_VELOCITY` | Y. Nakazawa, "Acceleration in the Low-velocity Region" | §1.8 |
| `SRC_WS1681458_TOPPMUGGLESTONE_VFFA` | M. Topp-Mugglestone, "vFFA and LHμC" | §1.9 |
| `SRC_WS1681458_ZIMMERMANN_SPS_LHC` | F. Zimmermann, "Potential possibilities of modifying SPS/LHC" | `docs/limitations.md` §5.1 |
| `SRC_WS1681458_HEQCD_SMALLX` | AGH Kraków, "High energy QCD at LHμC" (speaker not named) | §1.10 |
| `SRC_WS1681458_SCHULTE_IMCC` | D. Schulte, "Muon Collider (IMCC overview)" (`CONFERENCE_PROCEEDING`) | context |
| `SRC_ARXIV_2201_06664` | μTRISTAN, PTEP 2022 053B02 (related machine) | §1.8, `docs/limitations.md` §2 |
| `SRC_ARXIV_2203_06258` | D. Acosta et al., "The Potential of a TeV-Scale Muon-Ion Collider" (related machine) | §1.11 |
| `SRC_ARXIV_2510_27437` | MuCol Milestone Report No. 7, "Consolidated Parameters" (`OFFICIAL_CERN`; MDI and acceleration sections extracted) | §1.7, §1.9 |
| `SRC_DOI_10_5281_ZENODO_15054073` | MuCol Milestone Report No. 17, "Tentative design of the FFA" (`OFFICIAL_CERN`) | §1.9 |
| `SRC_ARXIV_2502_00181`, `SRC_ARXIV_2601_13189` | MAIA and MUSIC 10 TeV detector concepts (`ANALOGOUS_TECHNOLOGY`) | §1.7 |
| `SRC_ARXIV_2201_02436` | K. D. J. André et al., "An experiment for electron-hadron scattering at the LHC" (LHeC detector, ERL, IR) | §1.7 |
| `SRC_ARXIV_1306_3810`, `SRC_ARXIV_2006_01947`, `SRC_ARXIV_2410_11367` | Bakule et al. 2013, Beare et al. 2020, Aritome et al. 2024 (muonium emission and the measured J-PARC chain) | §1.8 |
| `SRC_ARXIV_1901_03047` | Abe et al. 2019, J-PARC muon g-2/EDM design | §1.8 |
| `SRC_ARXIV_2605_25580` | Sakaki, Kamioka, Yoshida 2026, μTRISTAN hybrid target | §1.8 |
| `SRC_IMCC2026_GIOVE_RF_SYSTEM` | D. Giove (INFN), "RF System", IMCC and MuCol Annual Meeting 2026 (`ANALOGOUS_TECHNOLOGY`) | §1.8 |
| `SRC_ARXIV_2610_09839` | Dağlı & Karaca 2026, AloHEP software paper (`OFFICIAL_SOFTWARE_DOCUMENTATION`) | `docs/limitations.md` §5.1 |
| `SRC_ARXIV_2101_10476` | Cheung & Wang 2021, "Physics potential of a muon-proton collider" (μ⁻p) | §1.11 |
| `SRC_ARXIV_2607_16904` | Dudko 2026, muon-collider review (`SECONDARY_SOURCE`; turns-per-lifetime formula only) | §4 context |
| `SRC_ARXIV_2609_37117` | U.S. Muon Collider Collaboration, input to the SCAC Facilities Subcommittee (`SECONDARY_SOURCE`) | §1.8 |
| `SRC_ARXIV_2610_14303` | AI4MuC workshop report (`SECONDARY_SOURCE`; process principles, `docs/architecture.md` §15) | process |
