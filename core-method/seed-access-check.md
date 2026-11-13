# Seed access check: which real-bug sources we can actually use

13 Nov 2026. Step 4 of the Seat roles plan: before building test material, check which real-bug sources are downloadable, licensed for our use and fit for review by reading. It builds on [seed-sources-research.md](seed-sources-research.md) and doesn't change the experiment plan.

**How this was checked:**
- **ReviewBench, CRBugBench and MCR-Bench:** a research agent cloned each repository into a scratch folder. It parsed the data files without running anything, read the papers' full text and the repos' docs, and fetched PR dates with `gh api`. I rechecked the three licences on the GitHub API, and the ReviewBench producer counts from the golden files.
- **SWE-bench-Live, SWE-Sharp-Bench, CVEfixes and ISO:**
  - **SWE-bench-Live and SWE-Sharp-Bench:** I read each dataset's fields and splits from the Hugging Face API, then computed dates and fix-diff sizes from every row.
  - **CVEfixes:** I read its README, data dictionary and Zenodo record.
  - **ISO:** I read the iTeh FDIS sample myself and iso25000.com through a fetch tool.
- **"Computed"** means counted from the raw data, not taken from a paper.
- **Contamination:** bugs fixed after mid-2026 are the least likely to be in the training data of models with a mid-2026 cutoff. Each model's cutoff should be checked for the models actually used.

## At a glance

| Source | Download | Data licence | Severity labels | Kinds filterable | Languages we need | Date range | Fit for reading |
|---|---|---|---|---|---|---|---|
| ReviewBench | GitHub, now | MIT (repo-wide; no separate data licence) | yes: high, medium, low (Claude Sonnet 5 classifier, human-audited) | yes: `category` | C# 25, Python 41, JS 15, TS 68 PRs | PRs 29 Mar 2025 to 4 May 2026 | findings have file and lines, but each item is a whole PR (median 9 files, 562 lines) |
| CRBugBench | GitHub, now (an author's rebuild) | **none** | **no** in the public data | **no** in the public data | C#, Python, JS, TS (counts by repo only) | bugs from 2015 to 28 Jun 2026 | one known bug per PR diff (median 5 files, 167 lines) |
| MCR-Bench | GitHub, now | Apache-2.0 (repo-wide) | yes: six levels (LLM-assigned, human-verified) | yes: `taxonomy` (functional F.* against evolvability E.*) | C# 454, Python 410, JS 409, TS 440 records | events 31 May 2012 to 2 Dec 2025 | best: file and lines per defect, small diffs (median 2 files, 14 lines) |
| SWE-bench-Live MultiLang | Hugging Face, now | MIT | no | no | C# 136, JS 108, TS 111 tasks (no Python) | C# to 30 Jul 2026, JS to 28 Jul 2026, TS to 20 Apr 2026 | about a quarter are one-file fixes of 20 lines or fewer |
| SWE-bench-Live Python | Hugging Face, now | MIT | no | no | Python, 1,888 tasks (full) | 22 Jul 2021 to 2 Sep 2025 | 28% one-file fixes of 20 lines or fewer |
| SWE-Sharp-Bench | Hugging Face, now | CDLA-Permissive-2.0 | no | no field (the paper's bug, feature and other split isn't in the data) | C#, 150 tasks | 16 Jun 2020 to 20 Apr 2025 | 33% one-file fixes of 20 lines or fewer |
| CVEfixes | Zenodo, now (12.7 GB zip) | CC BY 4.0 | yes: CVSS v2 and v3 scores from the NVD | yes: CWE types | many; per-file and repository language fields | CVEs to 23 Jul 2024 (rerunnable for later) | file and function level, before and after |

## Source by source

### ReviewBench
- **Download:** `git clone https://github.com/review-bench/ReviewBench` (pushed 12 Nov 2026).
  - `corpus/manifest.json` lists 219 PRs with base and head commits, and `golden/` has one JSON file per PR.
  - Each source repository is mirrored at `github.com/review-bench/<owner>_<repo>`.
- **Licence:** one MIT licence at the repository root and no separate data licence. The README says "The full corpus manifest and all golden findings are public".
  - **Use:** read as covering the golden files, MIT allows running reviews, publishing results and quoting findings. Quoted code stays under each upstream project's licence.
  - **The leaderboard rule:** offline scores can't be published *on the leaderboard*. That doesn't restrict our own write-ups.
- **Models behind the golden findings:** 2,623 true positives, counted from each finding's `producer` field (rechecked):

  | Producer | True positives | Share |
  |---|---:|---:|
  | Claude Sonnet 4.6 (LLM review) | 1,206 | 46.0% |
  | GPT-5.5, medium effort (`ccr`, an LLM review system the methodology doesn't yet name) | 957 | 36.5% |
  | Claude Opus 4.7, medium effort (`ccr`) | 228 | 8.7% |
  | Gemini 2.5 Pro (LLM review) | 149 | 5.7% |
  | human review | 39 | 1.5% |
  | GPT-4o (LLM review) | 36 | 1.4% |
  | Semgrep | 8 | 0.3% |

  - **Claude models wrote about 55% of the true positives.** Labels were first set by a Claude Sonnet 4.6 classifier and then a Claude Sonnet 5 classifier, with a human audit that corrected 47 false true positives.
  - **Judge:** official results are judged by Claude Sonnet 5 (README). HARBOR.md says its package's judge is `claude-opus-5`, which is a discrepancy.
  - **Its own warning:** the methodology says a reviewer that "shares models with a producer, may benefit from overlap with its own earlier output". For us, a Claude council may score higher partly because Claude wrote much of the key.
- **Severity:** high, medium or low on every finding. The classifier agreed with humans 62.9% of the time exactly and 98.7% within one level.
- **Kinds:** the `category` field. True positives by category:
  - correctness 1,068, maintainability 365, reliability 362 and documentation 306;
  - testing 223, security 98, api-architecture 81, performance 63 and accessibility 57.
- **Dates:** the manifest has no dates. PR creation dates fetched for 207 of 219 PRs run from 29 Mar 2025 to 4 May 2026, and 191 are from 2026.
- **Fit:** each finding has a file, start line and end line, and the median span is 4 lines. But each item is a whole PR: median 9 files and 562 changed lines, with 35.6% over 1,000 lines. There are 139 high-severity correctness and 12 high-severity security true positives.
- **Other discrepancy:** the blog lists "author follow-up commits" among the sources of findings, but the methodology says no source is labelled as an inferred author action.

### CRBugBench
- **Download:** the paper says "We are unable to make the replication package publicly available". It points to an open-source version at [github.com/malusamayo/CRBugBench](https://github.com/malusamayo/CRBugBench), whose README says it was "rebuilt ... from descriptions in the paper".
  - **Size:** 995 tasks (500 fix-track, 495 comment-track), not the paper's 1,000. The 800 industry tasks aren't released.
  - **For reading only:** the diffs and ground truth are plain files. Running the tasks would need about 650 GB of Docker images.
- **Licence:** **none.** There's no LICENSE file and the GitHub API reports none (rechecked). The paper's CC BY 4.0 covers the paper only. Nothing grants reuse or redistribution, so ask the first author (Chenyang Yang) before publishing anything built on it.
- **Severity:** the paper says an unnamed LLM annotated severity against a rubric. A check of 40 samples by people gave κ = 0.64, or 0.90 when grouped into two levels. **The public data has none:** `issue_severity` and `issue_priority` are empty in all 500 fix cases, and the comment cases have no severity field.
- **Kinds:** the paper annotates ISO/IEC 25010 impact, visibility and change type, but none of these are in the public files.
- **Languages and dates:** C#, Python, Rust, JS/TS and Java. By repository: Python 21, Java 20, C# 19, Rust 18, TS 15 and JS 4. The paper says bugs run from 2015 to 2026. A sample of 119 PRs ran from 22 Nov 2015 to 28 Jun 2026.
- **Fit:** one known bug per PR diff, with a median of 5 files and 167 lines. Location detail differs by track:
  - **comment track:** the location is a file and line;
  - **fix track:** files only, plus the eventual fix diff showing where the bug was fixed.
- **Discrepancy:** the judge panel's Gemini model is "gemini-3.1-flash" in the paper and "gemini-3.5-flash" in the repo. The panel includes a Claude model (claude-opus-4.8) in both.

### MCR-Bench
- **Download:** `dataset/{csharp,java,js,py,ts}.jsonl` in [github.com/DeepSoftwareAnalytics/MCR-bench](https://github.com/DeepSoftwareAnalytics/MCR-bench) (56 MB, last push 12 May 2026). There's no Hugging Face or Zenodo copy.
- **Licence:** Apache-2.0, repository-wide, with no data-specific licence (rechecked). It allows running reviews, publishing results and quoting findings, with attribution. The paper says source repositories were kept only under permissive licences.
- **Severity:** six levels: Blocker, Critical, Major, Normal, Minor and Trivial.
  - **How it was assigned:** the annotation LLM (unnamed in the paper) was prompted to "Assign severity based on the discussion context, reviewer's comments, tone, and the issue's potential impact". The pipeline runs three times and keeps only consistent cards. Two developers check each card and a third arbitrates. The κ of 0.87 is for whole cards, with no separate figure for severity.
  - **Counts:** Normal 1,599, Minor 1,320, Trivial 1,197, Major 1,087, Blocker 125 and Critical 50.
  - **Looseness:** the first record opened was a documentation edit labelled Blocker.
- **Kinds:** the `taxonomy` field.
  - **Functional codes:** F.1 interface, F.2 logic, F.3 resource, F.4 check, F.5 support, F.6 performance and F.7 security and privacy. Their counts are F.2 723, F.1 279, F.4 259, F.6 201, F.3 196, F.5 170 and F.7 34.
  - **Evolvability codes (E.*)** make up most of the data, and textual issues alone are 1,032.
- **Size and dates:**
  - **Records:** 2,269, by language Java 556, C# 454, TS 440, Python 410 and JS 409.
  - **What a record is:** the paper calls them "multi-round review tasks", but each record is one review round, from only 558 PRs in 37 repositories.
  - **Dates:** event dates run from 31 May 2012 to 2 Dec 2025, mostly 2017 to 2025.
  - **Repeats:** a defect repeats across rounds, so of 5,378 defect entries only 2,212 are in state New.
- **Fit:** the best of the three. Every defect has a file and line range, and each round's diff has a median of 2 files and 14 lines.

### SWE-bench-Live: MultiLang and Python
- **Download:** the Hugging Face datasets [SWE-bench-Live/MultiLang](https://huggingface.co/datasets/SWE-bench-Live/MultiLang) and [SWE-bench-Live/SWE-bench-Live](https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live), with parquet files. Each task has the base commit, the fix `patch`, a test patch, the issue text, `created_at` and a Docker image.
- **Licence:** MIT on both dataset cards and on the code. Each task's code keeps its own project's licence.
- **Severity and kinds:** neither. There's no bug, feature or category field, so bug fixes have to be picked by hand. The Python set has a `difficulty` field.
- **MultiLang** (1,077 tasks, one split per language, computed):

  | Language | Tasks | Created | From 1 Jul 2026 | One-file fixes | One file, 20 lines or fewer |
  |---|---:|---|---:|---:|---:|
  | C# | 136 | 29 May 2025 to 30 Jul 2026 | 22 | 48 (35%) | 36 (26%) |
  | JavaScript | 108 | 8 Jan 2023 to 28 Jul 2026 | 13 | 31 (29%) | 21 (19%) |
  | TypeScript | 111 | 21 Nov 2020 to 20 Apr 2026 | 0 | 39 (35%) | 30 (27%) |

  MultiLang has no Python. Its other splits are C, C++, Go, Java and Rust.
- **Python, full split** (1,888 tasks; test 1,000, lite 300, verified 500):
  - **Dates:** created 22 Jul 2021 to 2 Sep 2025, so **none from 2026**, although the dataset was last modified on 3 Nov 2026.
  - **Fit:** 758 are one-file fixes (40%), and 534 are one-file fixes of 20 lines or fewer (28%).
- **Fit:** the fix diff gives the location, and the median fix touches 2 files. The bug's own lines have to be found from the fix, and features filtered out.

### SWE-Sharp-Bench
- **Download:** the Hugging Face dataset [microsoft/SWE-Sharp-Bench](https://huggingface.co/datasets/microsoft/SWE-Sharp-Bench), 150 rows in one split.
- **Licence:** CDLA-Permissive-2.0. It allows use, modification and sharing of the data, and "does not impose any restriction or obligations" on Results, defined as "any outcome obtained by computational analysis of Data" ([cdla.dev](https://cdla.dev/permissive-2-0/), read through a fetch tool).
- **Severity and kinds:** neither. The paper's split into 91 bug fixes, 47 feature requests and 12 others isn't a field in the data. It was seen only in a snippet earlier, in seed-sources-research.md.
- **Dates:** created 16 Jun 2020 to 20 Apr 2025 (computed). None are recent.
- **Fit:** 60 one-file fixes (40%), and 49 of 20 lines or fewer (33%). The median fix is 2 files and 25.5 lines.

### CVEfixes
- **Download:** the v1.0.8 dataset is one 12.7 GB zip on [Zenodo](https://doi.org/10.5281/zenodo.4476563) (open access, published 28 Jul 2024). The GitHub repository has the code to rebuild it from scratch, which is how 2025–2026 CVEs would be collected.
- **Licence:** the data is CC BY 4.0 (Zenodo record and README), and the code is MIT. It allows running reviews, publishing results and quoting with attribution.
- **Severity:** yes. The data dictionary has CVSS v2 and v3 base scores and severities from the NVD, so these are the NVD's scores, not the project's.
- **Kinds:** security only, filterable by CWE type (272 types).
- **Languages:** repository language and file-level fields are in the data dictionary. The language counts weren't checked.
- **Dates:** CVEs published up to 23 Jul 2024. A rerun would be needed for anything recent.
- **Fit:** good for single functions. It holds before-and-after code for 51,342 files and 138,974 functions, with lines added and deleted.

## ISO/IEC 25010:2023: the open subcharacteristics

Both lists can be confirmed. The briefs' four open items are all in the model:
- **Functional suitability** (FDIS sample, section 3.1, read in full by me). It has three subcharacteristics:
  - **functional completeness:** "capability of a product to provide a set of functions that covers all the specified tasks and intended users' objectives";
  - **functional correctness:** "capability of a product to provide the accurate results when used by intended users";
  - **functional appropriateness:** "capability of a product to provide functions that facilitate the accomplishment of specified tasks and objectives".
- **Safety:**
  - **The list:** the FDIS sample's foreword, read in full by me, says "Safety has been added as a quality characteristic with subcharacteristics, i.e. operational constraint, risk identification, fail safe, hazard warning and safe integration."
  - **The definitions:** the sample stops before section 3.9, so these come from [iso25000.com](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010?start=8), page 2, read through a fetch tool:
    - **operational constraint:** constraining operation "to within safe parameters or states when encountering operational hazard";
    - **risk identification:** identifying "a course of events or operations that can expose life, property or environment to unacceptable risk";
    - **fail safe:** automatically placing itself "in a safe operating mode, or to revert to a safe condition in the event of a failure";
    - **hazard warning:** providing "warnings of unacceptable risks ... so that they can react in sufficient time";
    - **safe integration:** maintaining "safety during and after integration with one or more components".
- **Caveats:**
  - The iTeh file is the Final Draft International Standard (voting began 25 Aug 2023), not the published text.
  - iso25000.com is a secondary site that doesn't state its edition.
  - The briefs use three of safety's five subcharacteristics. Risk identification and safe integration aren't used.

## What we can use first

1. **MCR-Bench functional defects.** Its functional (F.*) defects in state New are the best fit for reading: a file and line range, small diffs, all four of our languages and a permissive licence. Its severity was LLM-assigned and looks loose, so hand-check each one used as a seed. All its events are from 2025 or earlier.
2. **ReviewBench high-severity correctness and security findings.** There are 139 and 12, preferring the smaller PRs. Its licence is clear and it has category and severity. But Claude wrote about 55% of the key, so:
   - score with the outside-family judge;
   - report results separately for findings from Claude and non-Claude producers;
   - remember its PRs predate mid-2026.
3. **SWE-bench-Live MultiLang, C# and JS tasks from July 2026,** 22 and 13 of them. These are the freshest real bugs found, and MIT. They need hand-picking (bugs, not features), and the bug's lines found from the fix.
4. **CVEfixes, rerun for 2025–2026 CVEs, for security seeds.** It has a clear licence, NVD severities and CWE types, at the cost of running the collection.
5. **Hold:**
   - **CRBugBench:** no licence, and its public data has no severity or kinds. Ask the author.
   - **SWE-bench-Live Python:** nothing after September 2025.
   - **SWE-Sharp-Bench:** a C# fallback, from 2025 or earlier.

**Not confirmed:**
- CVEfixes' language counts;
- which LLM annotated MCR-Bench, and the end of its paper (the agent read 100k of 118k characters);
- which of ReviewBench's 12 unresolved PRs fall outside the date range above;
- whether each SWE-bench-Live task's issue is a bug.
