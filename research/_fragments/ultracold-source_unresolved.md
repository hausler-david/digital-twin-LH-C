# Unresolved items — reconnaissance family `ultracold-source`

Searches run 2026-10-28 with WebSearch only (20 queries, 32 sources surfaced). WebFetch attempts to arxiv.org,
www.kek.jp and proceedings.jacow.org failed (`ENOTFOUND` / network policy); every other host was seen through
search snippets only (`access: snippet_only`). Everything below is therefore snippet-level evidence: it may not
back a `reported_lhmuc` status and is capped at confidence `medium` (CLAUDE.md §1.5). Nothing in this file is a
parameter record. Note that the whole family concerns the J-PARC / μTRISTAN ultra-cold muon technology, i.e.
analogous or related-machine evidence; no LHμC-specific source rate, bunch population or emittance was found.

## Unresolved items

- WebFetch to arxiv.org, www.kek.jp and proceedings.jacow.org all failed (ENOTFOUND / network policy); no full texts were read. All values come from search-engine snippets and need verification against the primary PDFs.
- Design-stage laser ionisation efficiency: a snippet quoted 'USM: ~ 105 μ+/s (100μJ @122nm+300mJ @355nm) Efficiency: ~ 1×10-3 / surface μ' and 'Laser for spectroscopy→Very low ionization eff (~10-5)' from 'one J-PARC slide set' in the result list (candidates: imcc_workshop_ver2.pdf on indico.fnal.gov, ishida_nufact10.pdf, IPAC2018 TUPAK007). Exact source not identified; not attributed to any source entry.
- A snippet stated 'A 2025 talk reported a first RF acceleration of cooled muons, but the rate was low, at about 2×10⁻³ per pulse, and was limited by available laser energy' without naming the talk; not attributed.
- Muonium yield per incident muon at J-PARC from Beare et al. (PTEP 2020, arXiv:2006.01947): the snippet confirms a projection to J-PARC conditions was made but the projected number did not appear; only the 0.01 per incident muon estimate from Beer et al. 2014 is quoted.
- No measured 122 nm/355 nm ionisation efficiency appeared in snippets; only the design target (~1e-3 per surface muon), a 244 nm spectroscopy-laser result (1e-7 per mu+) and the theoretical 100% ceiling.
- Silica aerogel as the muonium target was confirmed only via Aritome et al. ('laser-ablated aerogel') and the Beer/Beare papers; the g-2/EDM linac query did not return the aerogel detail.
- EDM sensitivity goal conflicts across sources: 1.5e-21 e cm (PTEP 2019, Venanzoni 2025) vs 1.5e-19 e cm (Mibe 2025 slides as rendered in the snippet); primary collaboration paper should be checked.
- IH-DTL output energy varies across sources: 4.26 MeV (PRAB 29, 093201), 4.5 MeV (Yamazaki 2025 talk, older slides), 4.3 MeV (some conference papers).
- Exact title and author list of PRAB 21, 050101 (2018) first muon RF acceleration paper and of PRAB 19, 040101 (2016) IH-DTL design paper were not shown in snippets.
- Hot tungsten source: PRL 74, 4811 publication year not confirmed (snippet said '1994 experiment'; PRL volume 74 corresponds to 1995); RIKEN-RAL-specific ultraslow muon parameters were not found.
- Two H-line / 29.8 MeV/c quotes were attributed to EPJ Web Conf. 282 01016 by inference only; the snippet did not name the source among the result list (alternatives: PoS 452/003, IPAC2018 TUPAK007).
- INSPIRE-HEP returned no records for the site:inspirehep.net query; indico.cern.ch returned only one relevant contribution (Kimura, Sept 2025) and the FFA'25 Takaura μTRISTAN talk.
- Sakaki-Kamioka-Yoshida arXiv:2605.25580 normalisation (per p–Li nuclear collision) is not directly comparable to the Matsudo 2024 KEK slide figure of ~5.5e-4 muons per proton (assuming 50% efficiency) quoted in the same snippet; the Matsudo slide (conference-indico.kek.jp event 268) was not given its own entry because its title was not shown.
- **Category decisions awaiting the lead**: the J-PARC facility proceedings SRC_URL_EPJCONF_282_01016 (EPJ Web Conf.
  282, 01016) and SRC_URL_PASJ2019_THOH13 keep the journal's `RELATED_MACHINE`; `CONFERENCE_PROCEEDING` may be more
  appropriate since J-PARC MLF is a facility, not a collider concept. The slide decks SRC_URL_JACOW_IPAC2019_MOYPLM1
  and SRC_URL_INDICO_FNAL_13080_KOSEKI_2016 were moved to `CONFERENCE_PROCEEDING`/`workshop_talk` per the lead's rule.
- **Query→source attribution**: the journal does not record which query surfaced SRC_URL_KEK_NEWSROOM_2015_03_16,
  SRC_URL_INDICO_FNAL_13080_KOSEKI_2016 or SRC_URL_KEK_KANDA_2023_USM_BEAMLINE_JPCS; they are logged with
  query `(see family queries)`. Other links were taken from the query notes that name the source.
- **Normalised-emittance chain (design → measured)**: 1.5 π mm mrad expected (IPAC2018 FRXGBF1) → 0.315π/0.195π mm mrad
  simulated IH-DTL output (PRAB 19, 040101) → <1 π mm mrad measured (Kimura 2025; Kamioka MIP2025) → 0.85 π mm mrad
  measured at 100 keV (Aritome PRL 134, 245001). Whether each figure is normalised rms, at which energy and plane,
  is not visible in snippets; must be read from the PDFs before any value enters `parameters/source/`.
- **Rate chain (per-stage efficiencies) is incomplete**: H-line/H2 surface muons ~1e8/s design (1 MW) → Mu formation
  fraction (65.5±1.8)% (Beare 2020, aerogel) and vacuum emission 0.01 Mu per incident muon (Beer 2014 projection) →
  laser ionisation design ~1e-3 per surface muon (unattributed slide) → USM design ~1e5/s (Kamioka) vs operating 300 μ+/s
  (U-line, Chen et al. review) vs 1000 μ/s planned for 2027 at 4 MeV (Physics World). The product of the quoted
  efficiencies cannot be checked for consistency from snippets; no measured ionisation efficiency was found.
- **Scaling to LHμC**: the only collider-scale rate claim seen is the μTRISTAN '~1e5 times J-PARC MLF' statement as
  quoted via arXiv:2506.15445, and the hybrid-target yield ~1e-3 USM per p–Li collision (arXiv:2605.25580). Neither is
  an LHμC number; both are `imported_related`/`analogous` at best and require the full texts.

## Fetch backlog

Once network access to the hosts is allowed, fetch each item below, archive the PDF under `references/`, record
SHA-256 in `research/archived_metadata/`, and convert the snippet leads into parameter records only with page +
verbatim quotation.

- `SRC_ARXIV_2410_11367` — https://arxiv.org/abs/2410.11367v2 — extract: abstract page + PDF (v2): exact emittance definition, 5.7 keV / 100 keV chain, muon rate per pulse at 100 keV, reduction factors, aerogel/laser set-up, licence.
- `SRC_URL_KEK_TOPICS_202605261000` — https://www.kek.jp/en/topics/202605261000 — extract: page date; confirms PRL Collection of the Year 2025 selection only.
- `SRC_JACOW_IPAC2018_FRXGBF1` — https://proceedings.jacow.org/ipac2018/doi/JACoW-IPAC2018-FRXGBF1.html — extract: pp. 5041-5046: linac stage energies, 30 meV USM energy, 1.5 π mm mrad expectation, 0.1% momentum spread, RF frequencies, 212 MeV; licence CC-BY.
- `SRC_JACOW_IPAC2018_TUPAL076` — https://proceedings.jacow.org/ipac2018/doi/JACoW-IPAC2018-TUPAL076.html — extract: 88.6 keV Mu- RFQ result, October 2017, transmission/rate.
- `SRC_URL_DOAJ_PRAB_21_050101` — https://doaj.org/article/5bfba7e8e15a402399aaf6b909c5785b — extract: resolve the real article (title, authors, DOI) behind the DOAJ listing; 89 vs 88.6 keV.
- `SRC_ARXIV_2605_25580` — https://arxiv.org/pdf/2605.25580 — extract: hybrid target geometry, USM yield per p–Li collision, assumptions (unit Mu conversion), proton energy/power normalisation.
- `SRC_ARXIV_2506_15445` — https://arxiv.org/pdf/2506.15445 — extract: already uploaded (registry); only re-check whether the '1e5 x MLF' and '0.016 pions/proton' statements are the paper's or μTRISTAN's.
- `SRC_ARXIV_2201_06664` — https://arxiv.org/abs/2201.06664v1 — extract: μTRISTAN source assumptions: μ+ rate, bunch population, emittance, repetition rate, 3 km ring; v2 changes.
- `SRC_ARXIV_1407_8248` — https://arxiv.org/pdf/1407.8248 — extract: PTEP 2014 reference; 0.01 Mu per incident muon projection and its assumptions; ≥8x enhancement at 300 μm pitch.
- `SRC_ARXIV_2006_01947` — https://arxiv.org/pdf/2006.01947 — extract: (65.5±1.8)% Mu formation fraction; projected vacuum Mu yield per incident muon under J-PARC pulsed conditions.
- `SRC_URL_KEK_NEWSROOM_2015_03_16` — https://www2.kek.jp/en/newsroom/2015/03/16/1300/ — extract: press summary only; confirm 'order of magnitude' wording.
- `SRC_ARXIV_1901_03047` — https://arxiv.org/pdf/1901.03047 — extract: PTEP 2019 053C02: surface muon rate, USM rate, linac energies, emittance, 450 ppb / <70 ppb / 1.5e-21 e cm.
- `SRC_ARXIV_2512_20335` — https://arxiv.org/abs/2512.20335 — extract: late-2025 status: linac stage naming (Alvarez vs DAW/DLS), ~300 MeV/c, schedule.
- `SRC_URL_APS_PRAB_29_093201_NAKAZAWA` — https://journals.aps.org/prab/issues/29/9 — extract: article DOI; 0.34-4.26 MeV, 1.4% field error, 390 kW, design field, beam-test status.
- `SRC_DOI_10_1103_PHYSREVACCELBEAMS_19_040101` — https://link.aps.org/doi/10.1103/PhysRevAccelBeams.19.040101 — extract: exact title; APF IH-DTL design; 0.315π/0.195π mm mrad output emittances (definition, energy).
- `SRC_URL_INDICO_IHEP_24109_KAMIOKA_MIP2025` — https://indico.ihep.ac.cn/event/24109/contributions/189912/attachments/91221/118876/04-MIP2025_skamioka_ver3.pdf — extract: spec sheet slide: 25 Hz, 2 ns, ~1e5/s, <1 π mm mrad, laser energies, 4 MeV 2027 milestone; MIP2025 date/venue.
- `SRC_URL_INDICO_JLAB_951_YAMAZAKI_BDX2025` — https://indico.jlab.org/event/951/contributions/17508/attachments/13298/21439/250905_BDX&Beyond_yamazaki.pdf — extract: linac energy breakdown (0.3 / 4.5 / 40 / 212 MeV), H2 milestones with years.
- `SRC_ARXIV_2601_15818` — https://arxiv.org/abs/2601.15818v2 — extract: review tables: facility rates (300 μ+/s USM), 122+355 nm scheme, efficiency statements.
- `SRC_URL_KEK_INDICO_346_HOKKAIDO_2026` — https://conference-indico.kek.jp/event/346/contributions/7562/attachments/5135/8350/Hokkaido_2026_ver1.pdf — extract: speaker/title; 1e-7 per μ+ with 244 nm laser; efficiency factorisation; any measured 122 nm efficiency.
- `SRC_DOI_10_1103_PHYSREVLETT_74_4811` — https://link.aps.org/doi/10.1103/PhysRevLett.74.4811 — extract: publication year; 2300 K tungsten, 0.2 eV; USM yield per incident muon (hot-W alternative).
- `SRC_URL_INSPIRE_FILES_6103970C` — https://s3.cern.ch/inspire-prod-files-6/6103970c6ab123d9a8571e71d1fff3fa — extract: identify the paper; 6N 50 μm W foil; 122.088 nm Lyman-α scheme.
- `SRC_URL_UTOKYO_PRESS_11225` — https://www.s.u-tokyo.ac.jp/en/press/11225/ — extract: 31 Aug 2026 release: 4 MeV → 25 meV → 0.3 MeV, 3x/200x gains, absolute rate if stated, 2027-28 plan (also kek.jp/?p=48023).
- `SRC_URL_PHYSICSWORLD_MUON_BEAM_COLLIDER` — https://physicsworld.com/a/high-quality-muon-beam-holds-promise-for-future-collider/ — extract: article date; '4 MeV at 1000 muon/s planned for 2027' quote and who said it.
- `SRC_URL_POS_MUON4FUTURE2023_008` — https://pos.sissa.it/452/008/pdf — extract: designed USM flux ~1e5/s, FY2026 completion, H2 layout.
- `SRC_INDICO_1528564_6573983` — https://indico.cern.ch/event/1528564/contributions/6573983 — extract: conference name; abstract with <1 π mm mrad measured normalised emittance; slides if attached.
- `SRC_URL_INDICO_ED_112_MIBE_G2TI_2025` — https://indico.ph.ed.ac.uk/event/112/contributions/1681/attachments/1024/1425/J-PARC_muon_g-2_at_5th_g-2_Theory_Initiatives.pdf — extract: H2 ~1e8/s surface muons; DAW 4-40 MeV; resolve EDM 1.5e-19 vs 1.5e-21 e cm.
- `SRC_URL_EPJCONF_282_01016` — https://www.epj-conferences.org/10.1051/epjconf/202328201016/pdf — extract: authors; H-line design 1e8/s at 1 MW; 29.8 MeV/c; confirm attribution of the quoted sentences.
- `SRC_URL_PASJ2019_THOH13` — https://www-linac.kek.jp/mirror/www.pasj.jp/web_publish/pasj2019/proceedings/PDF/THOH/THOH13_oral.pdf — extract: RCS 3 GeV / 1 MW / 333 μA / 8.3e13 ppp / 25 Hz / <1 μs; graphite IG430 target 2 cm x 30 cm rotating.
- `SRC_URL_JACOW_IPAC2019_MOYPLM1` — https://accelconf.web.cern.ch/ipac2019/talks/moyplm1_talk.pdf — extract: speaker; RCS 1 MW design, 1.5 MW second target station plan.
- `SRC_URL_INDICO_FNAL_13080_KOSEKI_2016` — https://indico.fnal.gov/event/13080/contributions/17160/attachments/11491/14678/US-JAPAN-WS_J-PARC_koseki_pub.pdf — extract: RCS 25 Hz, 348.3 m circumference, 1 MW design.
- `SRC_URL_JACOW_LINAC2022_WE1AA05` — https://accelconf.web.cern.ch/linac2022/doi/JACoW-LINAC2022-WE1AA05.html — extract: authors; RFQ II spare re-use; 324 MHz RFQ 2017 demonstration.
- `SRC_URL_KEK_KANDA_2023_USM_BEAMLINE_JPCS` — https://research.kek.jp/people/kanda/2023/03/01/ultra-slow-muon-beamline-jpcs.html — extract: locate the JPCS paper (U-line USM beamline) and its rate/emittance figures.

### Unattributed leads to locate (no source entry; not in the journal source list)

- Slide set quoting 'USM: ~1e5 μ+/s (100 μJ @122 nm + 300 mJ @355 nm) Efficiency: ~1e-3 / surface μ' and 'Laser for
  spectroscopy → very low ionization eff (~1e-5)' — candidates per journal: imcc_workshop_ver2.pdf (indico.fnal.gov),
  ishida_nufact10.pdf, IPAC2018 TUPAK007.
- '2025 talk: first RF acceleration of cooled muons at ~2e-3 per pulse, limited by laser energy' — talk not named.
- Matsudo 2024 KEK slides (conference-indico.kek.jp event 268): ~5.5e-4 muons per proton assuming 50% efficiency — title not shown.
- Nagoya University news item and KEK 2024 press PDF pr202405231500 on the 2024 RF acceleration result — surfaced but not registered.
- Kamioka 'Muon4Future2023' companion PoS 452/003 and IPAC2018 TUPAK007 — possible true sources of the H-line sentences attributed by inference to EPJ Web Conf. 282, 01016.
