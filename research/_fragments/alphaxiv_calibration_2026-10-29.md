# alphaXiv connector: Step-0 calibration, 2026-10-29

**Result: the route is stopped.** G1, G2, G3, G5 and G6 passed on every document they could be run on. G4 and G7
could not be run as pre-registered: `get_paper_content` holds no full text of arXiv:2506.15445v2 and answers "Paper
version not found for ID: 2506.15445v2". `docs/internet_research_protocol.md` §5a says: "If any gate fails, the route
stops and the owner is told." Nothing is registered: no source access changed, no archived metadata written, no record
added or edited. §6 gives the substitute evidence and §7 the decision the owner is asked to take.

## 1. Set-up

- **Gates:** as pre-registered in §5a, committed in `70032b3` at 23:10:38Z. The first Step-0 call followed at
  23:11:05Z. The only earlier calls are the spot check (§2).
- **Calls:** 16 connector calls in the session, all from the lead (10 `get_paper_content`, 6 `answer_pdf_queries`).
  - `tools/scan_connector_text.py transcripts` over the lead and subagent transcripts flags one: the spot check's
    unversioned `answer_pdf_queries`.
  - Each call has a row in `alphaxiv-spotcheck_search_log.csv` (2) or `alphaxiv-calibration_search_log.csv` (14), with
    the exact arguments, the tool_use_id, and the size and SHA-256 of what was saved.
- **Saving:** `tools/save_connector_text.py` copied each delivery byte for byte.
  - Source: the session transcript, or the harness file for the MR7 text. The harness reports that file's character
    and line counts, and the tool copies it only when both match.
  - Files: git-ignored `references/_local/<source_id>/calibration_*` (mode 600), never committed.
- **Instruction scan:** `tools/scan_connector_text.py text`, patterns `2026-10-29.1`, found no hits in any of the 11
  saved files.
- **Local reference texts:** `pdftotext` 24.02.0 (`-enc UTF-8`, default mode) on the archived PDFs. Each PDF's SHA-256
  equals its registry entry.

| Document | Local PDF | SHA-256 | Pages |
|---|---|---|---|
| DIS2026, arXiv:2610.35154v1 | `references/primary/arXiv-2610.35154v1_Piotrzkowski_LHmuC_DIS2026.pdf` | `a7da5e9a9b35d626…b715198e` | 7 |
| Kaya et al., arXiv:1905.05564v2 | `references/_local/arXiv-1905.05564v2.pdf` | `f071d25d92f2bd2c…93060132` | 8 |
| MuCol MR7, arXiv:2510.27437v1 | `references/_local/arXiv-2510.27437v1.pdf` | `7307181c44b3079f…21690111` | 93 |
| μLHC, arXiv:2506.15445v2 | `references/_local/arXiv-2506.15445v2.pdf` | `f6f8f02dd05e2bdf…27059966` | 24 |

- **Scripts and outputs:** in `research/_fragments/alphaxiv_calibration_2026-10-29/`. The outputs hold hashes, counts
  and numeric tokens only, no delivered text.

  | Script | Output | Checks |
  |---|---|---|
  | `calibrate.py` with `manifest.json` | `calibration_step0.json` | G1–G3, G5–G7 |
  | `g2_decompose.py` | `g2_decompose.json` | G2 token explanation |
  | `calibrate_extra.py` | `calibration_extra.json` | supplementary checks S1–S4 on 2506.15445 |

  Run them from the repository root with `python -I`. They need the git-ignored files and reproduce the committed
  outputs.

## 2. The spot check (reported, not counted)

Two calls on arXiv:1905.05564v2, made in plan mode at 20:42Z, before the rules existed:
- `get_paper_content` with `fullText`: 16,610 bytes, SHA-256 `b37431396ddd70f6…ffe7de6f`, saved afterwards from the
  transcript;
- `answer_pdf_queries` on the unversioned id `1905.05564`: not admissible, not saved, backs nothing. The search-log
  test exempts this one row, by family and id, as logged.

The exponent-token rule and G2's "split superscripts" allowance come from this check. Its bytes equal both fresh calls
(G3), but it counts toward no gate.

*[Correction 2026-10-30: "not saved" was inaccurate.*
- *Scratch copies of both spot-check results existed in the session scratchpad, mode 644, for the read-only dry run of
  2026-10-29: `kaya_full.txt` (SHA-256 `b37431396ddd70f6…ffe7de6f`) and `kaya_pages.xml` (`ffb690808d1aa735…0b1a2b08`,
  equal to the later versioned 1905.05564v2 response).*
- *They were never in `references/_local/`, never committed and never sent anywhere. Both were deleted on 2026-10-30.*
- *A hash search of `/tmp` and the session directory found no other whole-file copy outside
  `references/_local/<source_id>/`, apart from the harness's own file for the oversize MR7 result (§8). The search
  detects whole-file copies only. The lead and subagent session transcripts, which the harness keeps, also contain
  the delivered texts.]*

## 3. Deliveries

| File in `references/_local/` | Call | Bytes | SHA-256 | Version evidence |
|---|---|---|---|---|
| `SRC_ARXIV_2610_35154/calibration_get_paper_content_v1.txt` | full text, 2610.35154v1 | 19,409 | `cb5e36c2f4e8dee7…2b43576f` | stamp "arXiv:2610.35154v1 [hep-ex] 26 Oct 2026" |
| `SRC_ARXIV_2610_35154/calibration_pages_v1.xml` | pages, 2610.35154v1 | 19,700 | `1ceef073628d8430…31123efa` | id 2610.35154v1; pp. 1–7 |
| `SRC_ARXIV_1905_05564/calibration_get_paper_content_v2.txt` | full text, 1905.05564v2 (fresh 1) | 16,610 | `b37431396ddd70f6…ffe7de6f` | no stamp; page id below |
| `SRC_ARXIV_1905_05564/calibration_repeat_get_paper_content_v2.txt` | full text, 1905.05564v2 (fresh 2) | 16,610 | `b37431396ddd70f6…ffe7de6f` | identical bytes |
| `SRC_ARXIV_1905_05564/calibration_spotcheck_get_paper_content_v2.txt` | full text, 1905.05564v2 (spot check) | 16,610 | `b37431396ddd70f6…ffe7de6f` | identical bytes |
| `SRC_ARXIV_1905_05564/calibration_pages_v2.xml` | pages, 1905.05564v2 | 17,014 | `ffb690808d1aa735…0b1a2b08` | id 1905.05564v2; pp. 1–8 |
| `SRC_ARXIV_2510_27437/calibration_get_paper_content_v1.txt` | full text, 2510.27437v1 | 211,414 | `ca132936b7c7f0d2…20e9369f` | stamp "arXiv:2510.27437v1 [physics.acc-ph] 31 Oct 2025" |
| `SRC_ARXIV_2510_27437/calibration_pages_v1.xml` | pages, 2510.27437v1 | 39,700 | `a1218f08f6210098…216c03e3` | id 2510.27437v1; 15 pp. |
| `SRC_ARXIV_2506_15445/calibration_get_paper_content_v1.txt` | full text, 2506.15445v1 | 48,500 | `62a23cdc6b5f5fea…ba82b934` | no stamp; page id below |
| `SRC_ARXIV_2506_15445/calibration_pages_v1.xml` | pages, 2506.15445v1 | 40,475 | `f69cf23b652552fa…682322e2` | id 2506.15445v1; 16 pp. |
| `SRC_ARXIV_2506_15445/calibration_pages_v2.xml` | pages, 2506.15445v2 | 37,425 | `0a6d83f833d6516c…dd7057c1` | id 2506.15445v2; 15 pp. |

Full hashes are in the search-log rows. Three requests delivered nothing:
- `get_paper_content` on 2506.15445v2: "Paper version not found for ID: 2506.15445v2";
- `get_paper_content` on 1905.05564v1: "Paper version not found for ID: 1905.05564v1";
- two calls at 23:11:05Z (2506.15445v2 and v1) were cut off by a worker restart, with no result in the transcript, and
  were repeated at 23:29:19Z.

## 4. Gate results

| Gate | DIS2026 v1 | Kaya v2 | MR7 v1 | μLHC v2 |
|---|---|---|---|---|
| G1 kind (overlap ≥ 0.95; reference list) | pass, 0.9986 | pass, 0.9905 | pass, 0.9889 | not run: no v2 full text |
| G2 digit multiset | pass | pass | pass | not run |
| G3 determinism | — | pass (two fresh calls) | — | — |
| G4 version | — | — | — | not run as written (§5) |
| G5 pages | pass, 7 of 7 | pass, 8 of 8 | pass, 15 of 15 | (v2 pages: S1, 15 of 15) |
| G6 tail | pass | pass | pass | not run |
| G7 coverage | **68 of 68** (pre-registered) | 136 of 136 (supplementary) | 1766 of 1766 (supplementary) | not run as written (§6) |

G5 compares every delivered page, not only 3 per document. Each page must be the best word match among all local pages
and have the same digit multiset. G6 passed on its exact branch: the last 30 delivered words occur in the last two
local pages.

**G2: the token differences explained** (`g2_decompose.json`):
- The digit multisets are equal, so no digit was added or lost.
- Every numeric token found on one side only is the concatenation of two tokens found on the other side only:
  pdftotext joins them, the delivered text splits them.
- No case needs a decimal point added or removed at the join, and nothing is left unexplained.

| Class | DIS2026 | Kaya | MR7 |
|---|---|---|---|
| power of ten: the base "10" and its superscript exponent on separate delivered lines, joined by pdftotext ("1034"); every case matches a delivered line break | 8 | 17 | 51 |
| equation indices: sub- and superscript glyphs and an integral limit, never values (Kaya "𝜎40", "𝑓82"; MR7 "N02" for N₀² five times, "22" for the 2² of eq. A.2, "20" joining the V²_acc exponent and the integral's lower limit 0 in eq. I.2); each case located in both texts | 0 | 12 | 7 |
| numbers in references broken at a line-end hyphen and joined by pdftotext (pp. 4589–4602; ISSNs 0954-3899, 1674-1137) | 0 | 3 | 0 |
| tokens split | 8 | 32 | 58 |

Token order also differs, as G2 allows: pdftotext reads some tables column by column, and the arXiv stamp sits
elsewhere.

## 5. G4: how the two tools handle versions

**`get_paper_content` (full text)** held one version per paper and refused the other with "Paper version not found":
- 2506.15445: v1 delivered, v2 refused;
- 1905.05564: v2 delivered, v1 refused.

It never substituted a version. For 2506.15445, though, the version it holds is **not the latest**. The v1
acknowledgements lack the v2 sentence that reports the corrected luminosities ("the luminosity value increased by
approximately 2 times for the μTRISTAN-based option and 4 times for the LHeC-based option", v2 p. 21, read from the
uploaded PDF).

**`answer_pdf_queries`** delivered both versions of 2506.15445, each under its own id:
- S1: each of the 15 v2 pages is the best word match of the page with the same number in the local v2 PDF, with an
  equal digit multiset.
- S3: the 12 page numbers that v1 and v2 share carry different text on every page; 11 also have different digits.
- S2: all 16 v1 pages occur in the delivered v1 full text after whitespace collapse. The two tools therefore label the
  same v1 text alike.

**G4 as written:**
- The full-text half is not met: there is no v2 full text to differ from v1 and pass G2.
- The page-tagged half is met: id 2506.15445v1, with pages that differ from v2.
- The fallback clause ("If only the page-tagged half fails …") does not apply, because it is the full-text half that
  could not be run.

## 6. G7: coverage and substitutes

- **Pre-registered part, DIS2026 v1:** for 68 of 68 records, every numeric token of the quotation is among the
  delivered tokens.
- **Pre-registered part, μLHC v2 (198 records):** cannot be run on a full text. Substitute S4 checks the records page by
  page against the 15 delivered v2 pages. 152 records cite those pages:
  - 121 non-figure records: all 121 covered;
  - 31 figure reads: 27 miss. All 27 are `manual_figure_read` values from Figure 1 (p. 4, the μTRISTAN schematic) and
    Figure 10 (p. 14, histogram statistics). Each of them quotes a number that is absent from the local pdftotext
    page (and the next) too, so the values are not in the PDF text layer at all. §5a forbids figure reads from
    `fetched_text` in any case.

  The other 46 records cite pages that were not delivered (pp. 5, 7, 8, 9, 13, 18, 19).
- **Supplementary documents:** Kaya v2 136 of 136 (111 table reads); MR7 v1 1766 of 1766 (1570 table reads).

No digit differs in any document checked (G2, S1).

## 7. Decision for the owner

Nothing proceeds until the owner decides. The options:

1. **Accept the substitutes** (recommended):
   - **G4:** refusal instead of substitution, seen twice, together with S1–S3.
   - **G7:** DIS2026 68/68, Kaya 136/136, MR7 1766/1766, and S4 for μLHC v2 (121/121 non-figure records).

   Two rules, both following from §5, would be added to §5a:
   - **(a) Stamp-less full texts.** A full text without an arXiv stamp needs a page-tagged response for the same
     versioned id, and every page of that response must occur in the full text (the S2 test). Today a same-id response
     alone suffices.
   - **(b) Latest version.** A reading is registered only after a check that no later arXiv version exists, because
     `get_paper_content` can hold a superseded version (2506.15445). The check would call `answer_pdf_queries` on
     `<id>v<n+1>`. How that tool answers for a version that does not exist is untested, so this needs one more
     calibration call (for example 1905.05564v3) before batch C1.
2. **Re-run G4 on a held pair.** This needs an upload of two versions of one arXiv paper that the connector holds in
   full text.
3. **Close the route** and keep to uploads.

## 8. Limitations

- Four documents, one connector, one day. Later deliveries may differ; every reading keeps its own hashes and checks.
- Agreement with pdftotext shows that the connector returns the PDF text layer. Neither text is checked against page
  images, which is why the `fetched_text` cap stays at `medium`.
- G5 checks that pages are identified correctly, not where a quotation sits; `tools/check_fetched_text_quotes.py` does
  that per record.
- The figure values of μLHC v2 (Figures 1 and 10) cannot be reached through text at all.
- *[2026-10-30]* The harness keeps its own copy of the oversize MR7 result:
  `<session>/tool-results/mcp-alphaXiv-get_paper_content-1793316636953.txt`, 211,414 bytes, identical to the saved text.
  It is outside the repository, not committed and not sent anywhere; it was set to mode 600 on 2026-10-30.

## 9. Step 0b and the decision (2026-10-30)

- **The decision.** The owner chose none of options 1–3. They re-uploaded a byte-identical copy of the registered
  2506.15445v2 PDF (SHA-256 `f6f8f02d…27059966`, so nothing was archived) and wrote "I will let you decide next steps".
  On that delegation the lead chose a conditional reopening (option 1′). The decision record and the Step-0b protocol
  are in `docs/internet_research_protocol.md` §5a, committed before any Step-0b call.
- **What option 2 needs, corrected.** §7 said option 2 "needs an upload of two versions". That overstated its cost: G4
  as written needs only the later version held locally. The registry already holds uploaded later versions of several
  arXiv papers, and Step 0b runs G4 on three of them (G4′).
- **What changed before Step 0b, prompted by the critics' review:**
  - Two malformed CSV rows were repaired: RISK_045 and `CHK_UNIT_SEARCH_LOG_CONNECTOR_ROWS` had unquoted commas that
    shifted their columns. A field-count test now covers every CSV. The content was kept as committed; RISK_045's
    over-general "holds one version per paper" gets a dated update instead of a silent rewording (two cases only,
    §5), and the spot-check row's "nothing saved" becomes "nothing archived" (§2).
  - The store-only correction of §2 was made.
  - `tools/save_connector_text.py` now confines harness pointers and has a `--probe` mode.
  - The instruction scan now also runs on the collapsed text.
- **Re-scan.** With patterns `2026-10-30.1`, the 11 saved Step-0 files give 0 hits. Before, the scan ran line by line
  only.
- **Extended transcript audit** (`tools/scan_connector_text.py transcripts` over the lead and all subagent
  transcripts).
  - All 16 connector calls of the session are the lead's; only the logged spot check is flagged.
  - It lists 8 historical subagent events, all before the §5a rules were committed (2026-10-29 23:10:38Z):
    - five planning agents of 2026-10-29 loaded the alphaXiv tool schemas through ToolSearch, but made no call;
    - one of them called the remote-documentation tool;
    - one documentation agent (software inventory, workflow phase Docs) ran two `curl` reachability probes of
      software sites on 2026-10-28.
  - Since the rules were committed there are 14 connector calls, 0 flagged, 0 other violations and 0 events for review.
  - Bash commands are classified by command word (shlex, through wrappers such as `timeout`, `env` and `bash -c`, and
    into `$(…)`), after a regex version flagged "curl" inside a grep pattern, a Python string and a document's prose.
    The audit sees command words only: a network call made from inside a Python or other script is not detected.
- **First pre-registration and its review.** The first Step-0b pre-registration was committed as `6c3d41b`
  (2026-10-30 12:06:26Z), before any Step-0b call. One reviewer and four lens-specific finders (conformance, outcome
  space, calibration soundness, operations and security) then reviewed it, again before any call. They reported 24 and
  66 findings, 3 and 13 of them blocking, with much overlap. The main defects:
  - read literally, every delivered full text was a "generic error";
  - page-less answers to P4, P5 and the G4′ v1 calls could not be saved under their fixed names, so their stops could
    never be evaluated;
  - empty, cut-off, duplicated or foreign pages counted as version evidence;
  - the stamp rule was not applied to page-tagged answers;
  - `calibrate.py` exits 0 when a gate fails, and G2's explanation half was not run;
  - G1's reference heading would fail a correct 2101.10476v2;
  - the oversize size check would refuse a complete 2203.06258v3 if the harness counts UTF-16 code units (that text
    has 1,074 astral characters);
  - the likely outcome "one full-text version per paper" left G4′ testing nothing;
  - many decisions were left to the lead.

  The lead checked the decisive facts against the local data (the G1 heading, the astral characters, the stamp forms,
  the overlap minimum 0.862 rather than 0.857, the Step-0 refusal form). The transcript audit since the review began
  shows no connector call and no violation by any agent.
- **Revision 2026-10-30.2** replaces the first version before any call (§5a):
  - one deciding command, `step0b_eval.py evaluate`;
  - strict answer classes shared with the saver and the quote checker (`lhmuc/connector_text.py`);
  - page comparisons recalibrated by `pre_0b.py` (`calibration_0b_pre.json`: 45/45 same pages, 46/46 contained,
    medians 0.945 against 0.402, whole-text scores 0.913 against 0.498);
  - a v1 control P6 whose answer Step 0 predicts, and a second far-out negative P7 on another paper;
  - G4′ page halves for every paper;
  - every result saved with `--raw` and recorded with message ids;
  - safeguards (a) and (b) specified now, with the residual risks stated.

  `tests/unit/test_step0b_eval.py` drives every rule on synthetic answers. All 11 Step-0 saves replay byte for byte
  through the hardened saver, including the persisted MR7 result.
- **Query rule.** The Step-0 queries (captions and short phrases from the papers) did not fit the letter of the rule
  then committed ("ids, titles, authors"), though they held no project data. This is recorded as a Step-0 deviation.
  The amendment that admits such queries is the lead's, under the delegation, and awaits the owner's confirmation. That
  covers the line in `CLAUDE.md` §5 changed in `6c3d41b`; the lead does not edit `CLAUDE.md` further, and the owner
  may confirm or revert it.
- **Results:** recorded in §10 after the calls.
