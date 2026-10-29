# Milestone 1 addendum — the uploaded documents of the Phase-0 addendum and batches 7–10

**Date:** 2026-10-29 · **Branch:** `claude/lhmc-virtuallab-architecture-eitkjb` · **Basis:** commit
`104073c` plus the registry stage, committed with this report on 2026-10-29 · **Author:** Claude
(documentation task; counts filled by the lead session) for David Hausler · **Status:** registry stage
committed after adversarial verification; batch 10 extracted, verified and committed afterwards (§A.7). The
MR7 reference tables (held, verification pending) get their own section when their records are
committed. Counts the draft gave as working-tree values were confirmed against the committed files.

*Verifier note (registry stage, 2026-10-29):* after this draft was written, HEAD moved to `000f236`.
Commit `ad5ac43` registered batch 10 — Kaya et al. EPL 138 (2022) 24002 (`SRC_ARXIV_1905_05564`), Beer
et al. 2014 (`SRC_ARXIV_1407_8248`), Zhang et al. 2021, JPS Conf. Proc. 33, 011125
(`SRC_DOI_10_7566_JPSCP_33_011125`) and Shirotori et al. 2026 (`SRC_ARXIV_2608_25374`), so 38 of 242
sources are `access: uploaded`, with no parameter records yet (still 5601) — and `000f236` added the
MuCol MR7 luminosity-model arithmetic tests. At `000f236` `uv run pytest` collects 177 tests (120
scientific). The counts below remain those of `104073c` unless stated otherwise.

> **No digital twin of the LHμC exists.** This report records what 29 uploaded documents say, how
> their content entered the evidence registry, and which closed-form (P1) consistency checks the
> lead pinned in tests. Nothing here is a simulation result, an engineering-accuracy statement or a
> validated performance figure. LHμC values taken from workshop slides are **reported in workshop
> material, unverified by simulation**.

Scope: the 21 documents of the Phase-0 addendum (11 Kraków workshop decks and 10 papers or reports),
batch 7 (4 documents), batch 8 (1) and batch 9 (3). Together with the five Phase-0 uploads
(`docs/reports/M1_evidence_audit.md`), 34 sources are now `access: uploaded`. The structure follows
the §49 status report of the master prompt: A Completed · B Evidence used · C Assumptions ·
D Validation · E Limitations · F Results · G Next highest-value action.

---

## A. Completed

### A.1 Documents archived, read in full and extracted

Every document below was copied unmodified, given an archived-metadata record with SHA-256, licence
and read status (`research/archived_metadata/<source_id>.json`), read in full, extracted into
parameter records with page and verbatim quotation, and checked record by record against the page
images by an independent verifier (notes in `research/_fragments/`). Record counts are those of
commit `104073c`; "rep." = `reported_lhmuc`.

| # | source_id | Document | Category | Pages | Records (rep.) | Verifier note |
|---|---|---|---|---|---|---|
| 1 | `SRC_WS1681458_FORTHOMME_DETECTOR` | L. Forthomme, "LHeC/LHμC main detector" | PRIMARY_LHMUC (slides) | 19 | 214 (57) | `verify_G1_MACHINE.md`, `verify_G5_DETECTOR.md` |
| 2 | `SRC_WS1681458_KILIC_NOZZLE` | A. Kilic et al., "Nozzle design studies for mu+p collider detector" | PRIMARY_LHMUC | 25 | 238 (231) | `verify_G4_MDI_NOZZLE.md` |
| 3 | `SRC_WS1681458_YAMAZAKI_TEV_MUON` | Y. Yamazaki, "Challenges of TeV-muon Detectors" | PRIMARY_LHMUC | 17 | 52 (22) | `verify_G5_DETECTOR.md` |
| 4 | `SRC_WS1681458_ACOSTA_NEAR_BEAM` | D. Acosta et al., "Near-Beam Muon Detectors" | PRIMARY_LHMUC | 28 | 165 (108) | `verify_G4_MDI_NOZZLE.md`, `verify_G5_DETECTOR.md` |
| 5 | `SRC_WS1681458_TOPPMUGGLESTONE_VFFA` | M. Topp-Mugglestone, "vFFA and LHμC" | PRIMARY_LHMUC | 52 | 144 (59) | `verify_G3_ACCELERATION.md` |
| 6 | `SRC_WS1681458_ZIMMERMANN_SPS_LHC` | F. Zimmermann, "Potential possibilities of modifying SPS/LHC" | PRIMARY_LHMUC | 14 | 130 (3) | `verify_G1_MACHINE.md` |
| 7 | `SRC_WS1681458_ROGERS_HYBRID_SOURCE` | C. Rogers, "Hybrid Source of Ultra Cold Muons" | PRIMARY_LHMUC | 20 | 131 (17) | `verify_G2_SOURCE.md` |
| 8 | `SRC_WS1681458_ZHANG_MUONIUM` | C. Zhang, "Muonium diffusion modeling and multi-layer target design …" | PRIMARY_LHMUC | 23 | 82 (0) | `verify_G2_SOURCE.md` |
| 9 | `SRC_WS1681458_NAKAZAWA_LOW_VELOCITY` | Y. Nakazawa, "Acceleration in the Low-velocity Region" | PRIMARY_LHMUC | 19 | 86 (9) | `verify_G2_SOURCE.md` |
| 10 | `SRC_WS1681458_HEQCD_SMALLX` | AGH Kraków, "High energy QCD at LHμC" (speaker not named) | PRIMARY_LHMUC | 28 | 87 (57) | `verify_G6_PHYSICS.md` |
| 11 | `SRC_WS1681458_SCHULTE_IMCC` | D. Schulte, "Muon Collider (IMCC overview)" | CONFERENCE_PROCEEDING | 45 | 114 (0) | `verify_G3_ACCELERATION.md`, `verify_G6_PHYSICS.md` |
| 12 | `SRC_ARXIV_2201_06664` | Hamada et al., "μTRISTAN", PTEP 2022 053B02 | RELATED_MACHINE | 24 | 176 (0) | `verify_G2_SOURCE.md`, `verify_G3_ACCELERATION.md`, `verify_G6_PHYSICS.md` |
| 13 | `SRC_ARXIV_2203_06258` | Acosta et al., "The Potential of a TeV-Scale Muon-Ion Collider" | RELATED_MACHINE | 49 | 618 (0) | `verify_G1_MACHINE.md`, `verify_G5_DETECTOR.md`, `verify_G6_PHYSICS.md` |
| 14 | `SRC_ARXIV_2510_27437` | MuCol Milestone Report No. 7 "Consolidated Parameters" (MDI and acceleration sections) | OFFICIAL_CERN | 93 | 680 (0) | `verify_G3_ACCELERATION.md`, `verify_G4_MDI_NOZZLE.md` |
| 15 | `SRC_ARXIV_2502_00181` | Bell et al., "MAIA: A new detector concept for a 10 TeV muon collider" | ANALOGOUS_TECHNOLOGY | 44 | 265 (0) | `verify_G4_MDI_NOZZLE.md`, `verify_G5_DETECTOR.md` |
| 16 | `SRC_ARXIV_2601_13189` | Andreetto et al., "MUSIC: a detector concept for 10 TeV μ⁺μ⁻ collisions" | ANALOGOUS_TECHNOLOGY | 5 | 136 (0) | `verify_G4_MDI_NOZZLE.md`, `verify_G5_DETECTOR.md` |
| 17 | `SRC_ARXIV_2006_01947` | Beare et al. 2020, "Study of muonium emission from laser-ablated silica aerogel" | PEER_REVIEWED | 34 | 90 (0) | `verify_G2_SOURCE.md` |
| 18 | `SRC_ARXIV_2410_11367` | Aritome et al., "Acceleration of positive muons by a radio-frequency cavity", PRL 134, 245001 | PEER_REVIEWED | 6 | 90 (0) | `verify_G2_SOURCE.md` |
| 19 | `SRC_ARXIV_2607_16904` | L. V. Dudko, muon-collider review (turns formula only) | SECONDARY_SOURCE | 40 | 1 (0) | `verify_G6_PHYSICS.md` |
| 20 | `SRC_ARXIV_2609_37117` | U.S. Muon Collider Collaboration, input to the SCAC Facilities Subcommittee | SECONDARY_SOURCE | 5 | 0 | — (context only) |
| 21 | `SRC_ARXIV_2610_14303` | Berg et al., "AI Acceleration of Muon Collider R&D" (AI4MuC report) | SECONDARY_SOURCE | 17 | 0 | — (process rules, `docs/architecture.md` §15.1) |
| 22 | `SRC_ARXIV_2201_02436` | K. D. J. André et al., "An experiment for electron-hadron scattering at the LHC" (batch 7) | PEER_REVIEWED | 27 | 291 (0) | `verify_G8_LHEC_DETECTOR_ERL.md` |
| 23 | `SRC_ARXIV_1901_03047` | M. Abe et al., J-PARC muon g-2/EDM design (batch 7) | PEER_REVIEWED | 24 | 222 (0) | `verify_G9_JPARC_G2_AND_HYBRID_TARGET.md` |
| 24 | `SRC_ARXIV_2605_25580` | Sakaki, Kamioka, Yoshida, μTRISTAN hybrid target (batch 7) | ANALOGOUS_TECHNOLOGY | 11 | 76 (0) | `verify_G9_JPARC_G2_AND_HYBRID_TARGET.md` |
| 25 | `SRC_ARXIV_2610_09839` | B. Dağlı, Y. Karaca, "AloHEP Software" (batch 7) | OFFICIAL_SOFTWARE_DOCUMENTATION | 45 | 251 (0) | `verify_G10_ALOHEP.md` |
| 26 | `SRC_DOI_10_5281_ZENODO_15054073` | MuCol Milestone Report No. 17, "Tentative design of the FFA" (batch 8) | OFFICIAL_CERN | 16 | 131 (0) | `verify_G11_MUCOL_M17_VFFA.md` |
| 27 | `SRC_ARXIV_1306_3810` | P. Bakule et al. 2013, "Measurement of muonium emission from silica aerogel" (batch 9) | PEER_REVIEWED | 11 | 101 (0) | `verify_G12_BAKULE2013.md` |
| 28 | `SRC_ARXIV_2101_10476` | K. Cheung, Z. S. Wang, "Physics potential of a muon-proton collider" (batch 9) | PEER_REVIEWED | 7 | 109 (0) | `verify_G13_CHEUNG2021.md` |
| 29 | `SRC_IMCC2026_GIOVE_RF_SYSTEM` | D. Giove, "RF System", IMCC and MuCol Annual Meeting 2026 (batch 9) | ANALOGOUS_TECHNOLOGY | 23 | 91 (0) | `verify_G14_GIOVE2026_RF.md` |

Totals at `104073c`: 4771 records cite these 29 documents, 563 of them `reported_lhmuc` (all from the
`PRIMARY_LHMUC` decks), 28 `unknown` with `value: null` across the whole registry. The MR7 reference
tables (collider, proton driver, target, cooling, magnets, RF, power converters) were extracted
separately and are **held outside `parameters/`** until their verifier has run; this report cites
`SRC_ARXIV_2510_27437` with a page wherever it needs them. One external repository was fetched:
github.com/tobbetuyef/AloHEP tag v2.0 (`SRC_URL_GITHUB_TOBBETUYEF_ALOHEP`), cloned read-only and
read as text, not built or run.

### A.2 Commits

| Commit | Date (UTC) | Content |
|---|---|---|
| `1f929d1` | 2026-10-28 19:54 | addendum scaffolding: 21 uploads registered with SHA-256, assumption-supersession schema and checks, first addendum P1 tests |
| `b036d7e`, `35bde8a` | 2026-10-28 20:45–20:52 | batch-7 registration and lead arithmetic tests |
| `3e2e0a1`, `213ec93` | 2026-10-28 23:25 – 10-29 00:02 | batch 8: M17 registered, 131 verified records, closed-orbit checks |
| `b948962` | 2026-10-28 23:55 | batch-9 registration |
| `19d3464`, `aecd0eb` | 2026-10-29 00:46–01:18 | batch-7 verified records (LHeC, AloHEP; J-PARC g-2/EDM, hybrid target) |
| `03e0ab1` | 2026-10-29 02:32 | confidence caps enforced; 1088 confidences lowered |
| `9484d49` | 2026-10-29 02:34 | batch-9 verified records (Bakule, Cheung & Wang, Giove) |
| `a8de068` | 2026-10-29 09:46 | P1 test rule enforced; 327 P1 labels lowered |
| `1252bf2` | 2026-10-29 09:57 | addendum verified records (Kraków decks, μTRISTAN, MuIC, MR7 MDI/acceleration, MAIA, MUSIC, Beare, Aritome) |
| `68587c9` | 2026-10-29 10:03 | `parameters_extracted` sync; public AloHEP repository registered |
| `104073c` | 2026-10-29 10:05 | registry loaded once per test session |

### A.3 Tests

`uv run pytest` collects 151 tests at `104073c` and all pass (re-run by this documentation task on a
clean snapshot of the commit, 2026-10-29); 94 are scientific. New since Phase 0:
`tests/scientific/test_workshop_decks.py` (10 functions), `test_batch7_documents.py` (14),
`test_mucol_m17_vffa.py` (13), `test_batch9_documents.py` (9), `test_addendum_canonical_records.py`
(4 functions, 33 cases), `tests/unit/test_confidence_caps.py` (4), `test_validation_levels.py` (2) and
`test_registry_integrity.py::test_source_parameters_extracted_in_sync`. The registry-stage
counterpart `tests/scientific/test_addendum_registry_consistency.py` announced in
`test_addendum_canonical_records.py` is installed with the registry stage (3 functions, 12 cases; not
present at `104073c`).

### A.4 Registry stage (committed 2026-10-29 after adversarial verification)

| Item | Count | Where |
|---|---|---|
| Phase-0 assumptions marked `superseded_by_evidence` | 10 of 20 | `parameters/assumptions/phase0_assumptions.yaml` |
| Conflict records | 24 = 15 Phase-0 + 9 new | `research/source_conflicts.yaml` |
| Missing-evidence rows closed / narrowed / added | 9 `resolved_by_upload` / 13 `partially_resolved` / 14 added; 69 rows (55 at `104073c`, all `open`) | `registries/missing_evidence.csv` |
| Risk-register rows added or changed | 10 added, 11 changed; 44 rows (34 at `104073c`) | `registries/risk_register.csv` |
| Validation-registry rows for the addendum checks | 55 added; 91 rows (36 at `104073c`) | `registries/validation_registry.csv` |
| "Resolved or narrowed by uploads" section | added | `research/unresolved_searches.md` |
| Parameter records after the stage | 5601 (the stage edits assumption and synthetic records only) | `registries/parameter_registry.csv` |

### A.5 Documentation updated by this task (dated addenda, no wholesale rewrite)

`docs/limitations.md` (§5.1, §10 and dated notes), `docs/scientific_scope.md` (§1.7–§1.11),
`docs/research_roadmap.md` (status lines, ranking §3a, sequencing §4a), `docs/roadmap.md` (§2.1 M2
inputs), `docs/software_inventory.md` (§15, AloHEP correction), `docs/architecture.md` (§15: AI4MuC
principles, validator rules), `docs/validation_plan.md` (§2.0, §6a), `docs/uncertainty_policy.md`
(§2.1, §8a), `README.md` (status paragraph), and this report.

### A.7 After the registry stage (2026-10-29)

**Batch 10.** Four uploads, read in full and registered in `ad5ac43` (arithmetic pinned in
`tests/scientific/test_batch10_documents.py`), then extracted and adversarially verified:

| # | source_id | Document | Category | Pages | Records | Verifier note |
|---|---|---|---|---|---|---|
| 30 | `SRC_ARXIV_1905_05564` | U. Kaya, B. Ketenoglu, S. Sultansoy, F. Zimmermann, "Luminosity and Physics Considerations on HL-LHC and HE-LHC based µp Colliders", EPL 138 (2022) 24002 (arXiv v2) | RELATED_MACHINE (was SECONDARY_SOURCE) | 8 | 136 + 12 scenarios (148 checked, 6 corrections) | `verify_G15_KAYA2022.md` |
| 31 | `SRC_ARXIV_1407_8248` | G. A. Beer et al., "Enhancement of muonium emission rate from silica aerogel with a laser ablated surface", PTEP 2014 091C01 (arXiv v1) | PEER_REVIEWED | 8 | 78 (78 checked, 19 corrections) | `verify_G16_BEER2014.md` |
| 32 | `SRC_DOI_10_7566_JPSCP_33_011125` | Ce Zhang et al., "Simulation Study of Laser Ionization of Muonium by 1S-2S Excitation …", JPS Conf. Proc. 33, 011125 (2021) | CONFERENCE_PROCEEDING | 6 | 104 + 1 scenario (105 checked, 34 corrections) | `verify_G17_ZHANG2021.md` |
| 33 | `SRC_ARXIV_2608_25374` | K. Shirotori et al., "Feasibility demonstration of a high-momentum, high-purity muon beamline at the J-PARC Hadron Experimental Facility" (arXiv v1, 26 Aug 2026) | ANALOGOUS_TECHNOLOGY | 20 | 0 (context only) | — |

No record carries `reported_lhmuc`; none was removed. The Zhang PDF is kept only in `references/_local/`
because every page carries a per-download watermark. Results are in F.2 and F.3.

**Follow-ups of the registry verifier** (`3ea3f63`): `lhmuc.analytical.hourglass_factor` now does the
collision-time integral analytically (1-D in s); it had under-reported H by 10/35/49 % for proton bunches of
0.2/0.5/1 m (round β* = 7 cm), the range opened by `PROTON_BUNCH_LENGTH_RMS_SYN`, and is now checked against
the closed form √π u e^{u²} erfc(u) (`test_hourglass_factor_matches_closed_form_for_equal_optics`). New
`CONF_JPARC_DLS_FREQUENCY` (1296 MHz Abe 2019 vs 2592 MHz Nakazawa), an M17 internal tension recorded in
`CONF_VFFA_PEAK_FIELD` (8.3 T objective vs 13.59 T stage 4 "within realistic bounds"), two record fixes, and
the 1.70 max(σ) factor and the Zimmermann bunch-length extrapolation pinned as tests.

**Scenario labels.** `lhmuc validate` now applies rule 3 of `docs/validation_plan.md` §1 to scenarios: a
scenario's `validation_level` may not exceed the lowest level among its role records. All 33 scenarios
labelled P1 pointed to at least one P0 record and were lowered to P0 with `tools/apply_scenario_levels.py`
(log `research/_fragments/scenario_levels_lowered_2026-10-29.csv`; a dated comment marks each in its file).
No scenario is P1 now; individual records keep their own P1 checks.

**Other.** Four software sources the inventory cited but the registry lacked were fetched and registered
(`e0cfb0b`); the MuCol MR7 luminosity model (Table A.1, eqs. A.5–A.9) is pinned in
`tests/scientific/test_imcc_mr7_reference.py` (`000f236`). Conflicts: 27 (24 after the stage, plus
`CONF_JPARC_DLS_FREQUENCY`, `CONF_ABLATED_AEROGEL_REMEASUREMENT`, `CONF_JPARC_SURFACE_MUON_MOMENTUM`).

### A.6 Not done

No simulation, no generator run, no transport run, no optics run, no geometry. AloHEP was not built
or executed. No record was promoted above P1. No value from a search snippet was admitted.

---

## B. Evidence used

**B.1 Basis.** Only the uploaded documents (34) and one fetched repository. The literature hosts
(arxiv.org, cds.cern.ch, indico.cern.ch, inspirehep.net, doi.org, zenodo.org, journals, CERN hosts)
were still blocked on 2026-10-29.

**B.2 What each group contributed** (pages are those of the source; record ids in §F and in
`docs/limitations.md` §10):

- *Kraków decks — LHμC concept level.* Detector concept and the second LHμC beam set (Forthomme
  pp.9–14, 17); nozzle geometry and the Geant4 acceptance study (Kilic pp.3–22); TeV-muon resolution
  and kinematic reconstruction (Yamazaki pp.2–16); far-forward spectrometer strawman (Acosta
  pp.4–22); vFFA requirement and preliminary options (Topp-Mugglestone pp.3, 23–46); the LHC
  fewer-bunch question (Zimmermann pp.2, 9, 13–14); hybrid source (Rogers pp.3–20); muonium diffusion,
  the H-line chain and the μTRISTAN budget (Zhang pp.10, 20); front-end space charge (Nakazawa
  pp.5, 11, 16–17); the small-x programme (AGH pp.13–24); IMCC context (Schulte).
- *Related machines and reference designs.* μTRISTAN in full (`SRC_ARXIV_2201_06664`); the muon-ion
  collider tables, its "LHmuC" column (a different concept) and Delphes card (`SRC_ARXIV_2203_06258`);
  the IMCC nozzle, MDI and vFFA restatement in MR7 (pp.65–66, Table F.5); MAIA and MUSIC; the LHeC
  detector, ERL and IR paper (`SRC_ARXIV_2201_02436`); the MuCol M17 vFFA design note.
- *Source chain.* Bakule 2013 (origin of the 0.52), Beare 2020 (0.655 from all its aerogel targets
  combined; laser-ablation emission yields), Abe 2019
  (J-PARC g-2/EDM design chain, the 73 % calculation), Aritome 2024 (the measured chain), Sakaki 2026
  (hybrid target), Giove 2026 (thin-window RF for the cooling option).
- *Tools.* The AloHEP software paper and repository (§F.2); the codes named by every document are
  inventoried in `docs/software_inventory.md` §15.
- *Physics comparators.* Cheung & Wang 2021 (μ⁻p) and the muon-ion collider cross sections (§F.6).
- *Context and process.* Dudko (turns formula only), the U.S. MCC SCAC input (cooling risk, p.2),
  the AI4MuC report (verifiable-workflow principles, pp.4, 8, 10–13).

**B.3 Status assignment.** `reported_lhmuc` only from `PRIMARY_LHMUC` decks, and only for statements
about the LHμC; restated LHeC, IMCC, J-PARC and μTRISTAN values on those decks are
`imported_related` or `analogous` with an applicability explanation. AloHEP benchmark values and
Cheung & Wang values carry `applicability: screening_only`. Confidence follows the caps of
`research/source_quality_policy.md` §4 (§D.2).

**B.4 Not used for values.** `SRC_ARXIV_2609_37117` and `SRC_ARXIV_2610_14303` have no parameter
records; the MR7 reference tables are held (A.1).

---

## C. Assumptions

### C.1 Phase-0 synthetic assumptions overtaken by uploaded evidence

Recorded by the registry stage under the supersession rule of `CLAUDE.md` §4 and
`docs/synthetic_data_policy.md`; the table shows the committed state of 2026-10-29 (10 superseded,
10 kept). Each superseded record keeps its Phase-0 band as history in `range_vs_evidence` and a
dated note; six scan bands were re-based on 2026-10-29 to bracket every documented option (L* uniform
4–25 m, nozzle angle 2–12°, solenoid 3–5.5 T, vFFA peak field 5–14 T, formation fraction 0.4–0.75,
ionisation efficiency log-uniform 10⁻⁷–1), and each `_SYN` parameter survives only as a scan variable.

| Assumption | Phase-0 band | Superseding records | Range vs evidence |
|---|---|---|---|
| `ASM_DET_NOZZLE_OPENING_ANGLE` | uniform 5–20° | `DET_NOZZLE_HALF_OPENING_ANGLE_WS2026_FORTHOMME`, `…_OPTION2_…`, `DET_NOZZLE_OUTER_ANGLE_NEAR_IP_MR7` | **outside (below)** for the LHμC baseline: 40 mrad = 2.29°; 100 mrad = 5.73° inside |
| `ASM_DET_NOZZLE_LENGTH` | uniform 2–10 m | `DET_NOZZLE_LENGTH_WS2026_KILIC`, `DET_NOZZLE_TOTAL_LENGTH_IMPLIED_WS2026_KILIC`, `DET_NOZZLE_LENGTH_MR7`, `DET_NOZZLE_PHYSICAL_LENGTH_IMPLIED_MR7` | inside (587.8 cm; 589 cm) |
| `ASM_DET_NOZZLE_TIP_DISTANCE_FROM_IP` | uniform 2–50 cm | `DET_NOZZLE_TIP_DISTANCE_WS2026_KILIC`, `DET_NOZZLE_TIP_DISTANCE_MR7` | inside, near the lower edge (6 cm) |
| `ASM_DET_NOZZLE_MATERIAL` | {tungsten, INERMET180, tungsten + borated PE} | `DET_NOZZLE_MATERIAL_WS2026_KILIC`, `DET_NOZZLE_CLADDING_MATERIAL_WS2026_KILIC` | inside |
| `ASM_DET_SOLENOID_FIELD` | uniform 2–5 T | `DET_SOLENOID_FIELD_LHEC_DELPHES_WS2026_FORTHOMME`, `DET_SOLENOID_FIELD_ANDRE2022`, `DET_SOLENOID_FIELD_MAIA`, `DET_SOLENOID_FIELD_MUSIC` | inside (3, 3.8, 5 T); none is an LHμC value |
| `ASM_IR_LSTAR` | uniform 5–20 m | `IR_LSTAR_LHEC_WS2026_FORTHOMME`, `IR_LSTAR_ANDRE2022`, `IR_LSTAR_MR7` | inside (6, 15 m); the 23 m layout lies above; none is an LHμC value |
| `ASM_ACC_VFFA_PEAK_FIELD` | uniform 3–16 T | `ACC_VFFA_PEAK_DIPOLE_FIELD_8T_WS2026_TOPPMUGGLESTONE`, `…_10T_…`, `ACC_VFFA_PEAK_FIELD_RELAXED_MAX_WS2026_TOPPMUGGLESTONE`, `ACC_VFFA1_/ACC_VFFA4_PEAK_FIELD_ON_ORBIT_MUCOLM17` | inside |
| `ASM_SOURCE_MUONIUM_FORMATION_FRACTION` | uniform 0.3–0.7 | `SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAKULE2013`, `SOURCE_MUONIUM_FORMATION_FRACTION_BEARE2020` | inside (0.52, 0.655) |
| `ASM_SOURCE_LASER_IONISATION_EFFICIENCY` | log-uniform 10⁻³–1 | `SOURCE_LASER_IONISATION_EFF_244NM_WS2026_ZHANG`, `…_122NM_BUDGET_WS2026_ZHANG`, `…_CALC_ABE2019`, `…_PROJECTED_122_355NM_ARITOME2024` | **outside (below)** for the demonstrated 244 nm scheme (~10⁻⁶); calculated and projected values inside |
| `ASM_MACHINE_MUON_POLARISATION` | uniform 0–0.8 | `MACHINE_MUON_POLARISATION_WS2026_FORTHOMME`, `…_MUTRISTAN2022`, `…_ABE2019` | inside (assumed values, not measurements) |

Calibration lessons: two of ten bands excluded a reported or demonstrated value (nozzle angle,
laser-ionisation efficiency), and the L* band excluded a documented layout. All three Phase-0 bands
had been built on snippet-level analogues or design targets — the MAP/IMCC 10° cone, the LHeC 15 m
and IMCC 6 m L* (the FCC-eh 23 m was listed as outside), and the "100 % in principle" ionisation
ceiling with a lower bound set by what the DIS2026 yield needs; the uploads show the LHμC nozzle to
be far narrower than the IMCC one and the demonstrated ionisation far below the design targets.

### C.2 Synthetic assumptions kept

`ASM_IR_CROSSING_ANGLE`, `ASM_IR_SEPARATOR_DIPOLE_FIELD`, `ASM_IR_SEPARATOR_DIPOLE_LENGTH`,
`ASM_IR_Q1_GRADIENT`, `ASM_IR_Q1_APERTURE_RADIUS`, `ASM_IR_BETA_X_STAR_MUON`, `ASM_IR_BETA_Y_STAR_MUON`,
`ASM_PROTON_BUNCH_LENGTH_RMS`, `ASM_ACC_RF_FREQUENCY`, `ASM_ACC_RF_GRADIENT` (10). No
upload gives an LHμC value for these; the crossing angle is stated only qualitatively
(`IR_CROSSING_ANGLE_SCHEME_WS2026_FORTHOMME`, value null) and the proton bunch length only through
Zimmermann's scaling rule.

### C.3 Conventions behind derived values (stated in each derivation)

- Implied proton bunch population of the Forthomme set: naive formula with **H = 1** and a collision
  rate **f = 1/300 ns** (`PROTON_BUNCH_POPULATION_IMPLIED_WS2026_FORTHOMME`).
- LHeC Table 4 band: HL-LHC protons (2.2 × 10¹¹, ε_n = 2.5 µm), β*_p = 10.0 cm in both planes, electron
  beam matched to the proton size — inputs the paper does not list.
- Cheung & Wang cut-flow band: B(h → bb̄) = 0.58 and B(Z → bb̄) = 0.1512 from external references.
- Hourglass check of Phase 0: a 7.5 cm proton bunch, an unsourced order-of-magnitude input of
  `test_hourglass_factor_for_mulhc_like_optics` (the sourced nominal-LHC value is 7.7 cm,
  `PROTON_LHC_PR627_RMS_BUNCH_LENGTH_NOMINAL_WS2026_ZIMMERMANN`). It is not the value of
  `PROTON_BUNCH_LENGTH_RMS_SYN`, which was 8.5 cm (Phase-0 band 5–12 cm) and is 22.4 cm, the geometric
  midpoint of the log-uniform 5–100 cm band of 2026-10-29.
- Decay averaging for μp: one beam decays; the two-beam form is for μ⁺μ⁻ only.
- Per stopped muon in the Aritome chain: the stopping fraction 0.38 of the same paper.

### C.4 Applicability

IMCC 10 TeV μ⁺μ⁻ values (MR7, M17, MAIA, MUSIC) are `analogous`; LHeC values are comparators for an
electron machine; μTRISTAN values are a design variant of the LHμC source chain; the muon-ion
collider's "LHmuC" is a different concept (`RISK_022_LHMUC_NAME_COLLISION`); Cheung & Wang collide
μ⁻ (`screening_only`).

---

## D. Validation

### D.1 P1 checks added

All are consistency checks of numbers printed in the documents; tolerances are stated in each test.

- `test_workshop_decks.py`: `test_nozzle_half_angle_to_eta_max_forthomme_and_imcc`,
  `test_imcc_nozzle_outer_surface_angles_mr7_table_g1`, `test_forthomme_beam_set_implied_proton_bunch_population`,
  `test_zhang_hline_chain_and_mutristan_budget`, `test_aritome2024_measured_ultra_slow_muon_chain`,
  `test_muonium_formation_fraction_two_values_are_incompatible`, `test_nakazawa_space_charge_scaling`,
  `test_vffa_rigidity_and_mr7_vffa1_mean_bending_field`, `test_turns_per_lifetime_dudko_formula`,
  `test_muic_lhmuc_column_beam_size_acosta2022`.
- `test_batch7_documents.py`: `test_andre2022_magnetic_rigidities`,
  `test_andre2022_table2_current_from_charge_and_spacing`, `test_andre2022_table3_synchrotron_scaling_between_arcs`,
  `test_andre2022_table4_luminosity_with_hl_lhc_proton_parameters_recorded_band`,
  `test_abe2019_fig4_thermal_muonium_efficiency_decomposition`, `test_abe2019_table4_overall_efficiency_product`,
  `test_abe2019_table2_decay_survival_through_linac`, `test_abe2019_hline_rate_implied_by_table5_vs_quoted_1e8`,
  `test_abe2019_vs_zhang_g2_target_chain_consistency`, `test_sakaki2026_diffusion_length_and_emitted_fraction`,
  `test_sakaki2026_thermal_source_emittance_estimate`, `test_sakaki2026_pre_extraction_rate_upper_limit`,
  `test_dagli2026_mucol_10tev_decay_factor_and_turns`, `test_decay_averaging_differs_between_mumu_and_mup`.
- `test_mucol_m17_vffa.py`: stage-1 and stage-4 on-orbit fields, cell angles, vertical excursion bands,
  good-field extents, dispersion, kicker, √2 gain, the 8.3 T limit, `test_eq21_reverse_bend_angle_exceeds_planar_estimate`,
  `test_tabulated_peak_fields_are_f_magnet_stage1_and_d_magnet_stage4`, `test_drift_length_from_half_cell_angles`,
  `test_printed_eq27_inconsistent_with_closed_orbit_geometry`.
- `test_batch9_documents.py`: `test_bakule2013_vacuum_yield_scaling_to_jparc_beam`,
  `test_bakule2013_formation_fraction_vs_beare2020_combined_significance`,
  `test_bakule2013_density_scaling_alpha_minus_one_point_five`, `test_bakule2013_thermal_speed_order_of_magnitude`,
  `test_cheung2021_table1_centre_of_mass_energies`, `test_cheung2021_integrated_luminosity_from_assumed_peak`,
  `test_cheung2021_hbb_coupling_precision`, `test_cheung2021_higgs_yields`,
  `test_cheung2021_cut_flow_reproduces_delta_sigma_band`.
- `test_addendum_canonical_records.py`: canonical values, the `reported_lhmuc`/analogue split, and
  uploaded sources with checksums.

**Bands, not reproductions:** the LHeC Table 4 luminosity (ratio ≈ 0.80), the Cheung cut flow, the M17
stage-4 F-magnet field and the vertical excursions. The Abe 2019 Table 5 rate (≈ 3 × 10⁸ s⁻¹ implied
against "∼ 1e8 per second" quoted) is recorded as an internal-consistency observation of the design
paper, not as a conflict.

### D.2 Validator rules and label hygiene of 2026-10-29

- **Confidence caps** (`03e0ab1`): confidence above the §4 caps of `research/source_quality_policy.md`
  is an error (analogous, unrefereed slides, `imported_related` from a design variant and sources not
  read in full at most `medium`; synthetic at most `low`). 1423 records lowered from `high` to `medium`:
  1088 (`03e0ab1`) + 170 (`9484d49`) + 165 (`1252bf2`); by rule 770 analogous, 526 slides, 127
  design-variant imports (`research/_fragments/confidence_caps_applied_2026-10-29.csv`). The conflict
  cap (competitors of a conflict without a decided treatment at most `low`) is applied by hand, so
  every conflict written in the registry stage names a treatment.
- **P1 requires a registered test** (`a8de068`): a P1 record must name an existing `test_*` function in
  `validation.methods` or `check_ids`. 847 labels lowered to P0: 327 (`a8de068`) + 520 (`1252bf2`)
  (`research/_fragments/validation_levels_lowered_2026-10-29.csv`); three further batch-9 labels were
  lowered by hand because their tests check a derived quantity or need inputs outside the registry
  (`9484d49`), and individual labels were lowered by verifiers (e.g. the four LHeC Fig. 19 calibration
  records, the M17 D-bend angles).
- **`parameters_extracted` sync** (`68587c9`).
- Values, quotations and every other field were unchanged by the lowering; the tools abort if
  anything but the target token changes.

After the hygiene, 100 records are P1 and 5501 P0; none is higher. Scenario-level `validation_level`
labels (P1 on 33 of 36 scenarios) are not covered by the record-level rule — an open point for the
lead, not changed here.

### D.3 Verification of the extraction

Each group had an independent adversarial verifier who compared every record with the page images
(tables cell by cell), re-did the arithmetic and corrected values, pages, quotations, statuses and
applicability. Examples of what the verifiers caught: the LHeC Fig. 19 header gives β*_p = 10.0 cm and
β*_e = 10.9 cm per beam, not per plane (ids renamed, the band test corrected, ratio 0.75 → 0.80,
bands unchanged); the M17 stage-4 tabulated field is the D-magnet field (13.62 T reconstructed,
+0.2 %), not a discrepancy; the muon-ion collider records were moved to a single PDF-page
convention; six Acosta nozzle records were moved from `reported_lhmuc` to `analogous`. Residual doubts
are listed in E.

### D.4 What is not validated

No P2 or higher anywhere. No luminosity, background, acceptance, optics or source-rate result of this
project exists. The Kraków numbers are not reproduced by any simulation of this project; AloHEP was
not run.

---

## E. Limitations

- **Network.** Still blocked; unread items are ranked in `docs/research_roadmap.md` §3a (White Paper,
  μLHC erratum and AloHEP decks, remaining Kraków slides, theory papers and UFO, LHeC 2020 update and
  André et al. 2025, HL-LHC TDR and LHC Project Report 627 / CERN-2005-006, Topp-Mugglestone thesis
  and notebooks, Beer 2014 and the Zhang papers, Kaya et al. EPL 138, IMCC BIB papers). *[Verifier
  note: Beer 2014, Zhang et al. 2021 (JPS Conf. Proc. 33) and Kaya et al. arrived in batch 10, commit
  `ad5ac43`, after this draft; they are registered and read but not yet extracted into records.]*
- **Source quality.** The LHμC-specific numbers come from unrefereed slides (cap `medium`); several are
  explicitly preliminary (vFFA "in untested region of parameter space"; detector "still a WIP").
- **Human review.** Pending (`RISK_028_HUMAN_REVIEW_PENDING`).
- **MR7 reference tables.** Not yet in `parameters/`.
- **Registry stage.** Committed after adversarial verification (`research/_fragments/verify_REGISTRY_STAGE.md`:
  182 entries checked, 39 corrections, none removed); its residual doubts are listed in that note.
- **Residual extraction doubts** (verifier notes): the Kilic π⁺ 40 mrad panel duplicates the 100 mrad
  histogram (candidate erratum); the Kilic "ΔQ²rec %" definition and the "≈ 99.9 % absorbed" summary
  are not reproduced from the tabulated columns; MR7 Table 7.2 (nozzle z_max 6000 mm) vs Table G.1
  (base plane 595 cm); one vs two nozzles undecided across decks; the 23 m layout on Forthomme p.4 is
  not attributed to a machine; the relation of github.com/tobbetuyef/AloHEP to github.com/yefetu/ALOHEP.
- **Still unknown for the LHμC:** muon β*, emittance and bunch length of every beam set; the
  deliverable proton bunch population and length; crossing angle, separator, L*, Q1; main-ring lattice
  and dipole field; booster lattice and RF; pre-accelerator; proton-driver energy and repetition
  rate; the achievable source rate; μ⁺p beam-induced background; power, cost and siting.
- Details: `docs/limitations.md` §5.1 and §10.

---

## F. Results — what the documents state and what the arithmetic shows

These are statements of the sources and P1 consistency checks, not performance results.

### F.1 Nozzle

- LHμC options: "conical half opening angle: 40(100) mrad → η_max ~ 4(3)"
  (`DET_NOZZLE_HALF_OPENING_ANGLE_WS2026_FORTHOMME`, `DET_NOZZLE_HALF_OPENING_ANGLE_OPTION2_WS2026_FORTHOMME`,
  Forthomme p.9; Kilic p.5). η_max = −ln tan(θ/2) gives 3.91 and 3.00; the IMCC 10° nozzle
  (`DET_NOZZLE_OUTER_ANGLE_NEAR_IP_MR7`, MR7 p.66) gives 2.44 (`test_nozzle_half_angle_to_eta_max_forthomme_and_imcc`;
  MAIA §III states 2.44 ≈ 10°).
- The Phase-0 synthetic range 5–20° **excluded** the 40 mrad = 2.3° option (C.1).
- Lengths: Kilic drawing 487.8 cm rear section + 100 cm tip section, tip 6 cm from the IP
  (`DET_NOZZLE_LENGTH_WS2026_KILIC`, `DET_NOZZLE_TIP_DISTANCE_WS2026_KILIC`, p.4); MR7 Table G.1 base
  plane 595 cm, tip 6 cm (`DET_NOZZLE_LENGTH_MR7`, `DET_NOZZLE_TIP_DISTANCE_MR7`, pp.65–66). Material:
  tungsten cladded with borated polyethylene (Kilic p.4) vs INERMET180 with a borated-polyethylene layer
  (MR7 p.66). Conflict `CONF_NOZZLE_OPENING_ANGLE` (options kept as scenarios).

### F.2 Luminosity

- **Forthomme set.** 40 bunches of 10¹⁰ μ⁺, 300 ns spacing, σ 4.3 µm, L = 10³⁴ (p.17) implies
  N_p ≈ 7.0 × 10¹¹ = 3.2 × HL-LHC under H = 1 (`PROTON_BUNCH_POPULATION_IMPLIED_WS2026_FORTHOMME`;
  `test_forthomme_beam_set_implied_proton_bunch_population`). Because N_p is itself derived under
  H = 1, this set cannot test the hourglass question; only the DIS2026 2.1 × 10³⁴, whose inputs are all
  printed, shows that a published LHμC luminosity corresponds to H = 1.
- **H = 1 stated explicitly** in the muon-ion collider paper ("For simplicity, the hour-glass factor,
  H_hg, is assumed to be unity", `MACHINE_HOURGLASS_FACTOR_ASSUMED_MUIC2022`, PDF p.7).
- **Zimmermann:** "Higher intensity is accompanied by longer bunches and/or larger energy spread –
  Roughly speaking σδ σz ≈ 2 n_b,0 σδ,0 σz,0" (p.14): a ten-fold bunch population means longer bunches
  and a larger hourglass loss, or a larger energy spread.
- **AloHEP** (`MACHINE_ALOHEP_*_DAGLI2026`): hourglass and pinch are simulated and verified to about
  1 % (hourglass for A ≲ 1.5, p.27; pinch in the D_y ≤ 1.3 regime, p.31); the muon-decay factor is
  applied **analytically** (p.36). Its two-beam average reproduces the μ⁺μ⁻ 0.254
  (`test_dagli2026_mucol_10tev_decay_factor_and_turns`), whereas a μp collider needs the one-beam
  average, 0.632 over one dilated lifetime (`test_decay_averaging_differs_between_mumu_and_mup`). The
  internal L_nom underestimates unequal beams (p.33). The public v2.0 repository (MIT) contains **no
  μLHC input deck** (`ME_043`).
- **LHeC Table 4** 8.2 × 10³³ (`MACHINE_PEAK_LUMINOSITY_ANDRE2022`, p.18) is not reproducible from the
  paper (proton inputs missing); with HL-LHC protons the band ratio is ≈ 0.80
  (`test_andre2022_table4_luminosity_with_hl_lhc_proton_parameters_recorded_band`).
- `CONF_LUMI_MODEL_ASSUMPTIONS`: its treatment is now decided (`propagated_as_uncertainty`,
  every luminosity carried with the model that reproduces it), but its cause is unresolved: the μLHC
  values remain naive × 0.632 with no visible hourglass reduction.
- **Kaya et al. (EPL 138, 24002), an earlier LHC-based μp proposal.** All 12 luminosities of Tables 4–5
  (0.36–2.8 × 10³³) follow from eq. (6), L_μp = (N_p/N_μ)(σ_μ/max[σ_p,σ_μ])² L_μμ, and all 8 tune shifts of
  Table 6 from eqs. (9)–(10) (`test_kaya2022_eq6_reproduces_all_twelve_luminosities`,
  `test_kaya2022_table6_tune_shifts_from_eqs_9_10`). The paper itself says that ξ_p 'should be reduced by an
  order'; for matched beams L ∝ ξ_p, so the beam-beam-compatible values are about ten times lower,
  0.04–0.28 × 10³³ (an order-of-magnitude bound, `MACHINE_PEAK_LUMINOSITY_XI_P_LIMITED_MAX_KAYA2022`).
  Eq. (6) also scales a μ⁺μ⁻ luminosity that is averaged over two decaying beams (MR7 eq. A.7); with one
  decaying beam the average is 1.87–1.97 times larger for these options
  (`test_mr7_decay_factor_one_decaying_beam_exceeds_two_beam_average`), while the μμ hourglass and pinch
  factors it inherits do not apply to μp and no μp hourglass factor is applied (σ_z,p = 90 mm against
  β*_μ = 0.25–1 cm). The net effect needs a μp luminosity calculation; RISK_042 and
  `CONF_LUMI_MODEL_ASSUMPTIONS` record this.

### F.3 Source chain

- **Origin of the 0.52.** A MuSR measurement, 0.52 ± 0.01 on three 2013 aerogel samples (Bakule 2013 p.3,
  `SOURCE_MUONIUM_FORMATION_FRACTION_MUSR_BAKULE2013`), cited directly by Beare 2020 and Aritome 2024
  and, by inference, the value inside the J-PARC (Abe 2019), μTRISTAN and Zhang budgets. Beare 2020
  measured 0.655 ± 0.018 on different samples (p.25): **6.6 σ** apart with both uncertainties, 7.5 σ
  with Beare's alone (`test_bakule2013_formation_fraction_vs_beare2020_combined_significance`,
  `test_muonium_formation_fraction_two_values_are_incompatible`) — two measurements, both kept, never
  averaged (`CONF_MUONIUM_FORMATION_FRACTION`).
- **Budgets vs measurement.** μTRISTAN post-stopping budget 0.52 × 0.6 × 0.6 × 0.73 = 0.137 (Zhang p.20).
  Measured 2024 chain 2.1 × 10⁻⁸ per surface muon at 100 keV (Aritome pp.2, 4): ≈ 2.5 × 10⁶ below the
  μTRISTAN budget after stopping and ≈ 1.2 × 10⁵ below the J-PARC g-2 target 2.6 × 10⁻³ per surface muon
  (`test_aritome2024_measured_ultra_slow_muon_chain`). Abe 2019: 3.4 × 10⁻³ thermal Mu × 0.73 =
  2.5 × 10⁻³, consistent with the Zhang target column within 10 %
  (`test_abe2019_vs_zhang_g2_target_chain_consistency`).
- **Ionisation.** The 73 % (`SOURCE_LASER_IONISATION_EFF_CALC_ABE2019`, Abe p.8) is a **calculation**;
  the 2024 test used a 244 nm scheme (~10⁻⁶, Zhang p.10); the dedicated 122 + 355 nm source is
  projected at "around 10%" (Aritome p.5). `CONF_LASER_IONISATION_EFFICIENCY`.
- **Emission.** Bakule: flat aerogel at J-PARC beam conditions gives 9.6 × 10⁻⁴ muonium in vacuum per
  incident muon (p.10; `test_bakule2013_vacuum_yield_scaling_to_jparc_beam`); laser ablation later raised
  the yield (Beare 2020: 5–28 ‰ ablated vs < 5 ‰ flat, p.19).
- **Hybrid target** (Sakaki 2026): 6 × 10⁻⁴ ultra-slow muons per p–Li collision with **unit**
  muon-to-muonium conversion (η_conv unknown), an order-of-magnitude pre-extraction rate
  η_conv × 1.2 × 10¹² s⁻¹ per MW (`test_sakaki2026_pre_extraction_rate_upper_limit`); extraction,
  second-stage cooling and emittance unknown (null records).
- **Hybrid source** (Rogers): 0.04 μ⁺ per 5 GeV proton to the end of stage A (p.14); deceleration not
  designed (p.13). `CONF_SOURCE_CONCEPT` keeps the source concepts apart.
- **Beer et al. 2014** (laser-ablated aerogel): 30.5/3.72 = 8.2 times the flat-sample vacuum yield at
  300 µm pitch ('at least eight times'); the paper gives **no** muonium formation fraction
  (`SOURCE_MUONIUM_FORMATION_FRACTION_BEER2014` = null). Its 400 µm target, re-measured by Beare et al. in
  2017, came out 18 % lower (20.9 ± 0.7 vs 17.2 ± 0.2 ‰: 5.1 σ statistical, 1.6 σ with the stated
  systematics) — `CONF_ABLATED_AEROGEL_REMEASUREMENT`, open.
- **Zhang et al. 2021** (J-PARC S2 1S-2S demonstrator, simulation): Table I chain to 0.0109 s⁻¹ with laser
  ionisation 3.9 × 10⁻⁷ per vacuum Mu, 1.9 × 10⁶ below the 0.73 of the 122 nm design
  (`CONF_LASER_IONISATION_EFFICIENCY`). It cites Beer et al. 2014 for the 52 % formation fraction, the
  diffusion fit T = 322 K / D = 870 cm² s⁻¹ and a 23.2 mg cm⁻³ sample; Beer et al. contain none of them, and
  the 0.52 matches Bakule 2013 by value only (origin inferred). Internal inconsistencies (S2 rate 2.4 × 10⁵ vs
  2.4 × 10⁶; stopping 44.3 % vs 0.467) are kept in the record notes.

### F.4 Front-end space charge

Nakazawa (p.16): 10¹⁰ μ⁺ in 2 ns ≈ 0.75 A at the RFQ entrance, **220 ×** the perveance of the 30 mA H⁻
design (`SOURCE_RFQ_PERVEANCE_RATIO_WS2026_NAKAZAWA`; `test_nakazawa_space_charge_scaling`); "front end
must be re-optimised including 3D space charge" (p.17). `CONF_FRONT_END_SPACE_CHARGE`: no scaled J-PARC
front end is adopted.

### F.5 vFFA

- Kraków deck: 8–10 T (< 9 T relaxed), field index 40–60 /m (< 30 /m relaxed), excursion 3–7 cm
  (pp.35–36) — `reported_lhmuc`, preliminary.
- MuCol M17: stage-1 6.93 T on orbit is the F-magnet field (12.52 T good-field); stage-4 13.59 T is the
  reverse-bend D-magnet field (29.04 T good-field); design limit 8.3 T (LHC dipole), which stage 4
  exceeds; analytic lattices only, no tracking; the printed eq. (2.7) appears to contain a typo
  (`test_printed_eq27_inconsistent_with_closed_orbit_geometry`).
- The LHμC 70–500 GeV booster lattice is in neither M17 nor MR7. `CONF_VFFA_PEAK_FIELD`.

### F.6 IR, detector and physics comparators

- L*: 15 m (LHeC: `IR_LSTAR_LHEC_WS2026_FORTHOMME`, `IR_LSTAR_ANDRE2022`) vs 23 m
  (`IR_LSTAR_FCCEH_WS2026_FORTHOMME`; the slide does not name FCC-eh) vs 6 m (`IR_LSTAR_MR7`).
  `CONF_IR_LSTAR`.
- Solenoid: 3.8 T (LHeC Delphes card, `DET_SOLENOID_FIELD_LHEC_DELPHES_WS2026_FORTHOMME`) vs 3 T (LHeC
  detector paper, `DET_SOLENOID_FIELD_ANDRE2022`) vs 5 T (`DET_SOLENOID_FIELD_MAIA`, `_MUSIC`).
  `CONF_DETECTOR_SOLENOID_FIELD`.
- LHeC Fig. 19: β*_p = 10.0 cm and β*_e = 10.9 cm (per beam, not per plane).
- TeV muons: 6–7 % at 1 TeV (Yamazaki p.10), ~6 % far-forward (Acosta p.12). `CONF_TEV_MUON_RESOLUTION`.
- Cheung & Wang μp-1 is 7 TeV p × 1 TeV **μ⁻** (√s 5.3 TeV, assumed 10³³, 0.1 ab⁻¹;
  Δg_hbb/g_hbb = 0.69 %, `test_cheung2021_hbb_coupling_precision`). LHμC collides μ⁺, which changes the
  charged-current rates (the muon-ion collider's LHmuC column: 0.098 pb μ⁻p vs 0.024 pb μ⁺p CC at
  Q² > 10⁶ GeV², Table 4 PDF p.22), so their cross sections are screening comparators only. μLHC's
  implied W-fusion Higgs cross section (385 fb, `PHYS_HIGGS_WFUSION_XSEC_IMPLIED_MULHC`) and Cheung's
  0.978 pb are different processes (charge) — never averaged.
- Small-x programme (AGH deck): x_Bj ≲ 10⁻⁷ at Q² ~ 1 GeV², one order beyond LHeC (p.13), resummation
  and saturation tests with dijet and trijet correlations (pp.14–23); reported motivation only.

### F.7 RF (hybrid-source option only)

Giove 2026: thin-window 704 MHz cavities near 30 MV/m (p.3), no gradient or breakdown measurement
(`SOURCE_COOLING_RF_BREAKDOWN_DATA_GIOVE2026` = null). In-field breakdown data restated by Rogers favour
beryllium (Cu 24.4 → 12.9 MV/m at 0 → 3 T; Be 41.1 → > 49.8 MV/m, p.17), while INFN plans aluminium
windows for the demonstrator because of beryllium supply and safety (Giove pp.11–12); no source has
aluminium in-field breakdown data.

### F.8 Turns per lifetime

n = γcτ_μ/C with cτ_μ = 659 m (Dudko p.14, eq. (2)): 2079 at 1 TeV in 3 km
(`test_turns_per_lifetime_dudko_formula`), consistent with the Phase-0 T_rev route.

### F.9 Conflicts

| Conflict | Origin | Treatment (registry-stage draft, to be confirmed) |
|---|---|---|
| 15 Phase-0 records (`CONF_PEAK_LUMINOSITY` … `CONF_JPARC_IHDTL_ENERGY`) | Phase 0 | unchanged in substance; several extended with the uploads; `CONF_LUMI_MODEL_ASSUMPTIONS`, `CONF_PROTON_BUNCH_POPULATION_AND_NUMBER`, `CONF_LHEC_CROSSING_ANGLE`, `CONF_JPARC_IHDTL_ENERGY` move from `open` to a decided treatment (`propagated_as_uncertainty`, `resolved_as_scenarios`, `propagated_as_uncertainty`, `resolved_as_scenarios`; confirmed by the lead) |
| `CONF_NOZZLE_OPENING_ANGLE` | Forthomme, Kilic vs MR7/MAIA | resolved as scenarios (design options) |
| `CONF_MUONIUM_FORMATION_FRACTION` | Bakule 2013 vs Beare 2020 | resolved as scenarios by target sample; never averaged |
| `CONF_LASER_IONISATION_EFFICIENCY` | Abe 2019, Zhang, Aritome | resolved as labelled scenarios (calculated / demonstrated / projected) |
| `CONF_SOURCE_CONCEPT` | ultra-cold multilayer, hybrid target, hybrid source | resolved as separate source scenarios |
| `CONF_IR_LSTAR` | LHeC 15 m, 23 m layout, IMCC 6 m | propagated as uncertainty (scan variable) |
| `CONF_DETECTOR_SOLENOID_FIELD` | 3 / 3.8 / 5 T | propagated as uncertainty (scan variable) |
| `CONF_VFFA_PEAK_FIELD` | Kraków options vs M17 | resolved as scenarios with field definitions |
| `CONF_TEV_MUON_RESOLUTION` | Yamazaki vs Acosta | resolved as scenarios by detector region |
| `CONF_FRONT_END_SPACE_CHARGE` | Nakazawa vs scaled J-PARC front end | explicit unknown; scaled design not adopted |

Total after the stage: 24. None is averaged. Added afterwards (§A.7): `CONF_JPARC_DLS_FREQUENCY` (1296 vs 2592 MHz,
resolved as scenarios), `CONF_ABLATED_AEROGEL_REMEASUREMENT` (open) and `CONF_JPARC_SURFACE_MUON_MOMENTUM`
(27 vs 28 MeV/c, resolved as scenarios); batch 10 also extended `CONF_PEAK_LUMINOSITY`,
`CONF_LUMI_MODEL_ASSUMPTIONS`, `CONF_MUONIUM_FORMATION_FRACTION` and `CONF_LASER_IONISATION_EFFICIENCY`. Total: 27.

### F.10 Demonstration or interface-only results

None.

---

## G. Next highest-value action

1. **Owner requests (no network needed):** ask the HELP4CERN authors for the White Paper (or an
   embargoed draft) and the AloHEP authors for the **μLHC input decks and option set** behind
   7.2 × 10³³ / 8.8 × 10³³, together with the PTEP erratum text. These two items settle the largest
   remaining unknowns: the official LHμC baseline and `CONF_LUMI_MODEL_ASSUMPTIONS`
   (`docs/research_roadmap.md` §3a W1–W2).
2. **Network:** allow arxiv.org, cds.cern.ch, indico.cern.ch, zenodo.org and doi.org; the lead can then
   fetch the remaining public items of §3a (Kraków slides if attached, theory papers, LHeC 2020 update
   and André et al. 2025, HL-LHC TDR and LHC Project Report 627 / CERN-2005-006, Beer 2014, Kaya et al.,
   IMCC BIB papers). *[Beer 2014 and Kaya et al. have since been uploaded, extracted and verified
   (batch 10, §A.7).]*
3. **Platform:** finish the MR7 reference-table verification; compute a μp luminosity for the Kaya and
   LHμC options with the one-beam decay average and the μp hourglass factor in a recorded run; and
   pre-register Benchmark 3.1 (AloHEP v2.0 in an isolated build, option sets of
   `docs/validation_plan.md` §3.1) for the start of M2.

---

## Sources cited

Uploaded (read in full): the 29 documents of table A.1 with the pages cited in the text; Phase-0
uploads `SRC_ARXIV_2610_35154`, `SRC_ARXIV_2506_15445` (Tables 1–3, 6; §2.3; p.14, p.17),
`SRC_WS1681458_DAGLI_NUCLEUS`, `SRC_WS1681458_KHANPOUR_GAMMAGAMMA`, `SRC_WS_LEBOHO_KUMAR_DIHIGGS`.
Fetched: `SRC_URL_GITHUB_TOBBETUYEF_ALOHEP` (tag v2.0). Named but not read: `SRC_ARXIV_2007_14491`,
`SRC_ARXIV_2503_20475`, `SRC_URL_CERN_2020_010_HLLHC_TDR`, `SRC_URL_ORA_OXFORD_TOPP_MUGGLESTONE_THESIS`,
`SRC_ARXIV_1407_8248`, `SRC_ARXIV_1905_05564`, `SRC_ARXIV_2105_09116`, `SRC_URL_POS_ICHEP2024_819`,
`SRC_ARXIV_2411_02966`, `SRC_ARXIV_2610_28252`, `SRC_ARXIV_2610_17801`, `SRC_URL_GITHUB_YEFETU_ALOHEP`.
*[Verifier note: `SRC_ARXIV_1407_8248` and `SRC_ARXIV_1905_05564` were read in batch 10 (`ad5ac43`),
after this list was written; this report cites no value from them.]*
