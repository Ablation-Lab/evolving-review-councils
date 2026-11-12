# Seed sources: collections of real, documented bugs

12 Nov 2026. Background for the seat-roles work. It looks for collections of real bugs taken from real projects' histories, which could be seeds instead of, or alongside, Claude-written ones. It also covers mutation-testing tools that can make seeds without an LLM. It doesn't change the experiment plan. For the review areas themselves, see [review-areas-research.md](review-areas-research.md).

**What I needed from each source:**
- languages: Python, C# and JavaScript matter most. Our repos are mostly C# (Winscope, Stowdeck and AirScope, among others), Python (overnight-skills, appeal-stress-test) and JavaScript as Node `.mjs` scripts in the plugins. The video projects are TypeScript (`.ts` and `.tsx`), so TypeScript counts too;
- bugs across ISO/IEC 25010 areas, not just correctness;
- a licence that lets us use the collection and publish results on it;
- contamination risk;
- whether a reviewer could spot the bug by reading, without running tests.

**How each source was read** (same labels as review-areas-research.md):
- **Through a fetch tool:** the page was fetched, but what I saw was the fetch tool's summary of it, with quotes. Figures from these need a second look before they're cited.
- **Read directly:** I read the raw data myself: the GitHub API (licence, last push, latest release), the Hugging Face API (licence field, created and last-modified dates) or a raw file.
- **Abstract or listing only:** only the arXiv abstract page or a conference listing was read.
- **Snippet only:** seen only in search-result snippets. Marked *(snippet only)* wherever it appears.

"Last push" is the newest push to the repository's default branch, from the GitHub API. It shows the repository is maintained, not that the data changed.

## (a) The well-known collections

### Defects4J

- **Links:** [github.com/rjust/defects4j](https://github.com/rjust/defects4j). The page and README were read through a fetch tool, and the licence and last push were read directly.
- **Authors and date:** René Just, Darioush Jalali and Michael D. Ernst, "Defects4J: A Database of Existing Faults to Enable Controlled Testing Studies for Java Programs", ISSTA 2014. The current version is 3.0.1, which has no GitHub release. The last push was on 7 Apr 2026.
- **Languages:** Java only. All bugs are reproduced on Java 11.
- **Bugs:** 854 active and 10 deprecated, from 17 projects (Closure 174, JacksonDatabind 110, Math 106, Jsoup 93 and others).
  - **Collection rules:** each bug has an issue in a tracker and is fixed in a single commit. The fix touches source code, not configuration, docs or tests, and is minimised by hand. A triggering test fails before the fix and passes after it.
  - **Kinds:** the page doesn't categorise bugs. Since every bug needs a failing test, they are functional faults by construction.
  - **Deprecated bugs:** bugs that stop reproducing on newer Java versions move from `active-bugs.csv` to `deprecated-bugs.csv`.
- **Licence:** MIT.
- **Contamination:** high. It contains no recent bugs, has no held-out split and isn't refreshed with new bugs. Ramos et al. found it "consistently exhibits the highest rate of potential memorization" of the bug benchmarks they tested (see section (f)).
- **For code review:** the bugs are small and isolated, so they suit reading. But Java isn't one of our languages.

### BugsInPy

- **Links:** [github.com/soarsmu/BugsInPy](https://github.com/soarsmu/BugsInPy), read through a fetch tool, with the licence and last push read directly. The paper is [arXiv 2401.15481](https://arxiv.org/abs/2401.15481); only its abstract page was read.
- **Authors and date:** Ratnadira Widyasari, David Lo and 14 others, Singapore Management University. Published at ESEC/FSE 2020, pages 1556–1560. The arXiv copy was posted on 27 Jan 2024. The last push was on 10 Feb 2026.
- **Languages:** Python.
- **Bugs:** 493 real bugs from 17 Python projects, per the abstract. Each one can be checked out as a buggy or a fixed version, with tests to run. The framework also has `coverage`, `mutation` and `fuzz` commands.
  - **Kinds:** the repository page lists no categories.
- **Licence:** **none.** The GitHub API reports no licence and the page shows no LICENSE file. Without a licence, permission to redistribute the database isn't granted. Each bug's code keeps its own project's licence.
- **Contamination:** high. The bugs come from fixes made up to about 2020, with no refresh and no held-out split. I found no study that measures memorisation of BugsInPy itself.
- **For code review:** the bugs are isolated and Python, so they suit reading. Of the old collections it is the nearest match to our languages.

### BugsJS

- **Links:** [bugsjs.github.io](https://bugsjs.github.io/) and [github.com/BugsJS/bug-dataset](https://github.com/BugsJS/bug-dataset), read through a fetch tool, with the licence and last push read directly.
- **Authors and date:** Péter Gyimesi, Béla Vancsics, Andrea Stocco, Davood Mazinanian, Árpád Beszédes, Rudolf Ferenc and Ali Mesbah. Published at ICST 2019. The last push was on 27 Nov 2019, so nothing has changed since.
- **Languages:** JavaScript, server-side Node.js only.
- **Bugs:** 453, checked by hand, from 10 projects. ESLint has 333 of them; the next largest are Mongoose (29) and Express (27).
  - **Selection:** only issues with a bug label were taken, which leaves out feature requests, build problems and docs tasks.
  - **Versions:** each bug has Git tags for the buggy, test-only, fixed and full versions.
  - **Kinds:** the site lists no types. The paper may have a taxonomy, but I didn't read the paper.
- **Licence:** MIT on the repository. The site itself shows only "BugsJS Copyright 2019".
- **Contamination:** high. The bugs predate 2019, with no refresh and no held-out split.
- **For code review:** in our language, but three quarters of the bugs come from one project (ESLint).

### SWE-bench and its variants

- **Links:** [swebench.com](https://www.swebench.com/) and its Verified and Multilingual pages, plus [github.com/SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench) and the Hugging Face dataset cards. These were read through a fetch tool, and the licence and dates from both APIs were read directly.
- **Authors and date:** Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press and Karthik R. Narasimhan. The paper is [arXiv 2310.06770](https://arxiv.org/abs/2310.06770), an oral at ICLR 2024. The dataset was created on Hugging Face on 10 Oct 2023, and the repository's last push was on 18 Sep 2026.
- **The variants** (all are issue-resolution tasks, not only bugs):

  | Variant | Size | Languages | Notes |
  |---|---|---|---|
  | Full | 2,294 issue and pull-request pairs from 12 Python repositories | Python | Hugging Face card |
  | Lite | not checked | Python | I didn't read its own page; the fetch tool's "300" came from its general knowledge, not the page |
  | Verified | 500, a "human-validated subset" made with OpenAI | Python | announced 13 Aug 2024 |
  | Multilingual | 300 tasks from 42 repositories | C, C++, Go, Java, JavaScript, TypeScript, PHP, Ruby and Rust | **no Python and no C#**; paper arXiv 2504.21798 |
  | Multimodal | v2 has 480 tasks, open source from 1 Sep 2026 | not checked | from the GitHub news |

- **Bugs:** tasks come from merged pull requests that close a GitHub issue, so some are features rather than bugs. The pages don't break down by kind.
- **Licence:** the code is MIT. Multilingual's Hugging Face card says MIT. The Full, Lite and Verified cards have no licence field, and the Verified page says "All rights reserved". Each task's code keeps its own project's licence.
- **Contamination:** high for Full and Verified.
  - Liang et al. found models can name the file to change from the issue text alone (see section (f)).
  - OpenAI stopped reporting Verified on 23 Feb 2026, saying it is increasingly contaminated, and recommended SWE-bench Pro *(snippet only: the OpenAI page refused the fetch)*.
  - Epoch AI's review of 3 Sep 2026 rates Verified "Flawed" *(snippet only)*.
- **For code review:** the fix diff gives an answer key. But many fixes span several files and some tasks are features, so the bug-fix tasks would need to be picked out by hand.

## (b) Refreshed and contamination-aware collections

### SWE-bench-Live (Microsoft)

- **Links:** [github.com/microsoft/SWE-bench-Live](https://github.com/microsoft/SWE-bench-Live), read through a fetch tool, with the licence, release and dataset dates read directly. The paper is [arXiv 2505.23419](https://arxiv.org/abs/2505.23419), seen only in snippets.
- **Date:** the paper is from May 2025. The last push was on 8 Nov 2026, and the three Hugging Face datasets were last modified on 3 Nov 2026.
- **Datasets:**
  - **Python:** 50 "newly verified" issues are added to the test split every month. The `lite` and `verified` splits are frozen for leaderboard comparison, and `full` holds all the latest issues. The README's last note on the Python data says it was "updated through 08/2025" (17 Sep 2025).
  - **MultiLang** (released 1 Jan 2026): 1,077 tasks from 431 repositories in 8 languages, at 21 Aug 2026. The January news lists C/C++, C#, Java, TS/JS, Go and Rust.
  - **Windows** (released 8 Mar 2026): 66 tasks from 48 repositories in 9 languages, with PowerShell actions.
  - **The first release** had 1,319 tasks from issues created since 2024, in 93 repositories *(snippet only, from the abstract)*.
- **Bugs:** issue-resolution tasks with a Docker image each. The pages don't break down by kind.
- **Licence:** MIT (code and all three datasets).
- **Contamination:** low if tasks are picked by date. New issues keep arriving, so tasks created after a model's training cutoff can be chosen. There's no private held-out split.
- **For code review:** the best fit of the refreshed sets for our languages, with C#, JavaScript and TypeScript in MultiLang and Python in the main set. Bug fixes still need picking out from features.

### SWE-rebench (Nebius)

- **Links:** [swe-rebench.com](https://swe-rebench.com/) and the abstract of [arXiv 2505.20411](https://arxiv.org/abs/2505.20411), read through a fetch tool, with the Hugging Face licence and dates read directly.
- **Authors and date:** Ibragim Badertdinov, Boris Yangel and 7 others. v1 is from 26 May 2025 and v2 from 4 Nov 2025. It was submitted to NeurIPS 2025. The leaderboard dataset was last modified on 28 Jul 2026, and the site's latest news is from 1 Jul 2026.
- **Languages:** Python. The site has a language filter, so other languages may have been added; "SWE-rebench v2" is promoted, but I didn't read it.
- **Size:** over 21,000 Python tasks for training. The leaderboard uses a moving window: "111 problems from 65 repositories" for 15 May to 1 Jul 2026.
- **Licence:** CC BY 4.0, on both datasets.
- **Contamination:** designed against it. The window moves, and the leaderboard marks some results "Potential contamination" or "Beyond eval range". The page doesn't explain how either mark is set.
- **For code review:** good for fresh Python bugs. Mostly functional, as with SWE-bench.

### SWE-bench Pro (Scale AI)

- **Links:** the [Scale blog post](https://scale.com/blog/swe-bench-pro), read through a fetch tool. The [Hugging Face card](https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro) was read directly, and so was the GitHub API for `scaleapi/SWE-bench_Pro-os`.
- **Date:** the post is from 19 Sep 2025. The dataset was last modified on 22 Sep 2026.
- **Subsets:** 731 public, 858 held-out and 276 commercial tasks, 1,865 in all, from 41 repositories.
  - The Hugging Face card's default test split has 642 rows, not 731. I didn't find out why.
- **Languages:** the post names Go, Python, JavaScript and TypeScript, without a full list.
- **Licence:** the public tasks come from copyleft (GPL) repositories, chosen because such code is "likely to be excluded from training data". The card has no licence field, and the evaluation code is MIT.
- **Contamination:** the only collection I found with a **private held-out split**. The held-out set is kept for Scale's own checks and the commercial set uses private code, so neither is available to us. The copyleft argument is Scale's own claim and hasn't been measured.
- **For code review:** the tasks are long and span many files, so they make hard seeds. Fair to use for publishing results, but GPL code quoted in a paper needs care.

### Multi-SWE-bench (ByteDance Seed)

- **Links:** [github.com/multi-swe-bench/multi-swe-bench](https://github.com/multi-swe-bench/multi-swe-bench) and the [Hugging Face card](https://huggingface.co/datasets/ByteDance-Seed/Multi-SWE-bench), read through a fetch tool, with the licence and release read directly.
- **Authors and date:** Daoguang Zan et al., [arXiv 2504.02605](https://arxiv.org/abs/2504.02605), released 3 Apr 2025 and in the NeurIPS 2025 Datasets and Benchmarks track. v1.0.0 came out on 5 Jun 2025, and the last push was on 18 Dec 2025.
- **Size and languages:** 1,632 tasks in Java, TypeScript, JavaScript, Go, Rust, C and C++. There's no Python and no C#. There's also a mini set (400 tasks) and a flash set (300).
- **Licence:** the code is Apache 2.0. The data card says "licensed under CC0, subject to any intellectual property rights in the dataset owned by Bytedance".
- **Contamination:** issues up to early 2025, with no refresh or held-out split.
- **For code review:** useful only for JavaScript and TypeScript.

### SWE-PolyBench (Amazon)

- **Links:** [github.com/amazon-science/SWE-PolyBench](https://github.com/amazon-science/SWE-PolyBench), read through a fetch tool, with the licence and dates read directly.
- **Authors and date:** Muhammad Shihab Rashid et al., [arXiv 2504.08703](https://arxiv.org/abs/2504.08703), 2025. The Verified split came out on 27 Aug 2025, and the last push was on 14 Aug 2026.
- **Size and languages:** 2,110 tasks in Java, JavaScript, TypeScript and Python.
  - **PB500:** 125 tasks per language, split 40-40-20 between bug fixes, features and refactoring.
  - **Verified:** 382 tasks, including 100 JavaScript, 113 Python and 100 TypeScript.
- **Licence:** MIT (code and dataset).
- **Contamination:** no refresh or held-out split.
- **For code review:** it's the only one that labels tasks as bug fix, feature or refactor, which makes picking bug fixes easy.

### SWE-Sharp-Bench (Microsoft)

- **Links:** the [arXiv 2511.02352](https://arxiv.org/abs/2511.02352) abstract page, read through a fetch tool, and the [Hugging Face dataset](https://huggingface.co/datasets/microsoft/SWE-Sharp-Bench) licence and dates, read directly.
- **Authors and date:** Sanket Mhatre, Yasharth Bajpai, Sumit Gulwani, Emerson Murphy-Hill and Gustavo Soares. v1 is from 4 Nov 2025 and v3 from 18 Nov 2025. The dataset was last modified on 6 Nov 2025.
- **Languages:** C# and .NET. It is the only C#-specific collection I found.
- **Bugs:** 150 tasks from 17 repositories, of which 91 are bug fixes, 47 feature requests and 12 others *(snippet only)*. Only pull requests with a pass, fail, pass test pattern were kept *(snippet only)*. The repositories have at least 5,000 stars *(snippet only)*.
  - **Solve rates:** 40% of its tasks are resolved, against 70% on SWE-bench Verified.
- **Licence:** the dataset is CDLA-Permissive-2.0, which allows use and publishing results. The paper itself is CC BY-NC-SA 4.0.
- **Contamination:** issues up to 2025, with no refresh or held-out split, and unmeasured.
- **For code review:** the obvious C# source, but small.

## (c) Security and performance collections

### CVEfixes

- **Links:** [github.com/secureIT-project/CVEfixes](https://github.com/secureIT-project/CVEfixes), read through a fetch tool, with the release read directly.
- **Authors and date:** Guru Bhandari, Amara Naseer and Leon Moonen, PROMISE '21. v1.0.8 came out on 30 Jul 2024 and covers CVEs published up to 23 Jul 2024.
- **Size:** 12,107 vulnerability-fixing commits in 4,249 projects, covering 11,873 CVEs in 272 CWE types. It holds the code before and after each change for 51,342 files and 138,974 functions.
- **Languages:** not listed on the page. It is drawn from many projects, but I didn't check which languages.
- **Licence:** the code is MIT and the data is CC BY 4.0.
- **Contamination:** the release stops in July 2024, but the repository includes the collection code, so it could be rerun to collect 2025–2026 CVEs. There are no tests: these are fixes, not reproducible bugs.
- **For code review:** security seeds by reading, at function level. It's the best route to recent real security bugs in our languages, at the cost of running the collection ourselves.

### SecBench.js

- **Links:** [github.com/cristianstaicu/SecBench.js](https://github.com/cristianstaicu/SecBench.js), *(snippet only)*, apart from the licence and last push, read directly.
- **Authors and date:** Masudul Hasan Masud Bhuiyan, Adithya Srinivas Parthasarathy, Nikos Vasilakis, Michael Pradel and Cristian-Alexandru Staicu, ICSE 2023 *(snippet only)*. The last push was on 20 Aug 2026.
- **Bugs:** 600 executable vulnerabilities in npm packages, each with an exploit and a check *(snippet only)*. They cover prototype pollution (192), path traversal (169), command injection (101), ReDoS (98) and code injection (40).
- **Licence:** **none** (GitHub API).
- **For code review:** JavaScript security seeds, but unlicensed and from 2023 or earlier.

### Performance: SWE-Perf, GSO and SWE-fficiency

- **SWE-Perf:** He et al., [arXiv 2507.12415](https://arxiv.org/abs/2507.12415) (abstract page, read through a fetch tool). v1 is from 16 Jul 2025 and v2 from 1 Jul 2026, accepted at ICML 2026.
  - It has 140 tasks drawn from performance-improving pull requests.
  - The abstract doesn't say which language they are in or whether the data is released.
- **GSO** (102 tasks) and **SWE-fficiency** (498 tasks, from repositories such as numpy, pandas and scipy, [arXiv 2511.06090](https://arxiv.org/abs/2511.06090)): *(snippet only)*.
- **A reliability critique:** a 2026 paper (arXiv 2607.01211) found the reference patches stay valid in replays on other machines for only 39 of 102 GSO tasks and 11 of 140 SWE-Perf tasks *(snippet only, from an aggregator page)*.
- **For code review:** these are optimisation tasks, not bugs: the "before" code works, just slowly. They could give performance seeds, but by the critique's figures a slowdown is hard even to measure, let alone spot by reading.

## (d) Collections built for code review

### ReviewBench (GitHub)

- **Links:** the [GitHub blog post](https://github.blog/ai-and-ml/reviewbench-an-open-benchmark-for-ai-code-review/) and [github.com/review-bench/ReviewBench](https://github.com/review-bench/ReviewBench), read through a fetch tool, with the licence and last push read directly.
- **Authors and date:** Michelle Zhou and Alejandro Carderera de Diego of GitHub, 5 Oct 2026, built with Microsoft *(snippet only)*. The last push was on 12 Nov 2026.
- **Size and languages:** 219 public pull requests from 187 repositories in 19 languages, with 2,623 true-positive findings. The full set has TypeScript 68, Python 41, C# 25, Go 19, JavaScript 15 and 51 other PRs.
- **Ground truth:** findings were gathered from:
  - human review comments;
  - the authors' later fixes;
  - static analysis;
  - several frontier models.

  Each finding was then checked against a rubric. Senior engineers re-labelled every finding and agreed with the benchmark 96.6% of the time. The judge is Claude Sonnet 5.
- **Kinds:** findings are labelled by category and severity. In the 25-PR test set (352 findings), the counts are:
  - correctness 133, reliability 58, maintainability 44, testing 35;
  - security 27, documentation 21, performance 12;
  - API architecture 12, accessibility 10.
- **Licence:** the repository is MIT. No separate data licence is stated, though "the full corpus manifest and all golden findings are public". Results from offline runs "can't be published on the leaderboard". That is a leaderboard rule, not a ban on publishing elsewhere.
- **Contamination:** not discussed. The PRs are public and so are all the answers, from October 2026 on, so later models may train on them. There's no private split.
- **For code review:** **the closest match to what we need.** It is built for reading review, has C#, Python, TypeScript and JavaScript, and its categories cover most ISO/IEC 25010 areas. It's not bug-only, though: a finding can be any true, relevant, non-trivial review point.

### Martian Code Review Bench

- **Links:** [github.com/withmartian/code-review-benchmark](https://github.com/withmartian/code-review-benchmark), read through a fetch tool, with the licence and last push read directly. The [codereview.withmartian.com](https://codereview.withmartian.com/) page returned only its title.
- **Date:** launched 26 Feb 2026 *(snippet only)*. The last push was on 15 Sep 2026.
- **Offline set:** 50 PRs from 5 projects with 173 human-checked "golden comments". The projects are Sentry (Python), Cal.com (TypeScript), Grafana (Go), Discourse (Ruby) and Keycloak (Java).
  - **Categories:** bug, security, concurrency, data, api, perf, test_gap, doc_defect, style and speculative.
  - **Severities:** low to critical.
- **Online set:** samples fresh GitHub PRs where review bots commented, and checks whether developers acted on the comments.
- **Licence:** MIT.
- **Contamination:** the offline set is fixed and public. The online set refreshes, but it measures bots' comments, not seeded bugs.
- **For code review:** built for it, with Python and TypeScript, and the only set besides ReviewBench with test-gap and performance labels. It's small.

### Qodo Code Review Benchmark 1.0

- **Links:** the [Qodo blog post](https://www.qodo.ai/blog/how-we-built-a-real-world-benchmark-for-ai-code-review/), read through a fetch tool, and the GitHub API for `agentic-review-benchmarks/benchmark-pr-mapping`.
- **Authors and date:** Tomer Yanay and Bar Fingerman, 4 Feb 2026.
- **Bugs: not real.** Qodo takes merged PRs and injects defects into them:
  - an LLM adds best-practice violations;
  - 1–3 functional or logic bugs are added to each PR.

  That gives 100 PRs with 580 issues. A later post's 125 PRs and 703 bugs are *(snippet only)*.
- **Languages:** TypeScript, Python, JavaScript, C, C#, Rust and Swift.
- **Licence:** **none** on the repository (GitHub API).
- **For code review:** the defects are written seeds, partly made by an LLM, placed in real code. It's no help in getting away from written seeds.

### "Bigger Isn't Always Better" (Kumar, Bararia and Raj, 2026)

- **Links:** the [arXiv 2606.15689](https://arxiv.org/abs/2606.15689) abstract page, read through a fetch tool.
- **Data:** 150 samples: 100 bugs injected by mutation and 50 real bug-fix PRs from 8 repositories. The data is released, under a licence that isn't stated.
- **Why it matters here:** it measures the gap between written and real seeds directly. The best model's F1 was 0.847 on the synthetic samples and 0.066 on the real PRs. Recall on performance bugs was near zero for every model. The authors say "synthetic-only evaluation dramatically overestimates model capability".

## (e) Mutation-testing tools (seeds without an LLM)

All four are actively maintained. Each makes small rule-based changes, such as swapping an operator or removing a call. The licence, latest release and last push were read directly from the GitHub API, and only Stryker.NET's page was read beyond that, through a fetch tool.

| Tool | Language | Licence | Latest release |
|---|---|---|---|
| [mutmut](https://github.com/boxed/mutmut) | Python | BSD-3-Clause | 3.8.0, 12 Sep 2026 |
| [Cosmic Ray](https://github.com/sixty-north/cosmic-ray) | Python | MIT | v8.9.0, 10 Nov 2026 |
| [Stryker.NET](https://github.com/stryker-mutator/stryker-net) | C# (.NET Core and .NET Framework) | Apache 2.0 | 5.1.0, 10 Nov 2026 |
| [StrykerJS](https://github.com/stryker-mutator/stryker-js) | JavaScript (and, I believe, TypeScript; not checked) | Apache 2.0 | v10.1.1, 23 Oct 2026 |

BugsInPy also has a `mutation` command.

- **Strengths:** mutants are cheap, reproducible and free of any model's habits. They can be made in our own apps, so there's no contamination at all.
- **Weaknesses** (my reading, not from a source): they are almost all functional, local and often obvious by reading. They won't give security, maintainability or test-quality seeds, and the 0.847 against 0.066 gap above suggests they are much easier than real bugs.

## (f) Work measuring memorisation

- **Ramos, Mamede, Jain, Canelas, Gamboa and Le Goues, "Are Large Language Models Memorizing Bug Benchmarks?"** ([arXiv 2411.13323](https://arxiv.org/abs/2411.13323), abstract page read through a fetch tool). v1 is from 20 Nov 2024 and v3 from 31 Mar 2025. It was at the ICSE 2025 LLM4Code workshop *(snippet only)*.
  - **Method:** they checked whether benchmarks appear in training sets, and measured negative log-likelihood and n-gram accuracy.
  - **Findings:** codegen-multi showed "significant evidence of memorization", and Defects4J the most. Newer models such as LLaMa 3.1 showed limited leakage.
- **Liang, Garg and Zilouchian Moghaddam, "The SWE-Bench Illusion"** ([arXiv 2506.12286](https://arxiv.org/abs/2506.12286), abstract page read through a fetch tool). v1 is from 14 Jun 2025 and v4 from 1 Dec 2025.
  - **File paths:** models named the right file from the issue text alone up to 76% of the time on SWE-bench, against up to 53% on other repositories.
  - **Verbatim reproduction:** up to 35% five-gram accuracy reproducing the fix on Verified and Full, against up to 18% elsewhere.
- **OpenAI, "Why we no longer evaluate SWE-bench Verified"**, 23 Feb 2026 *(snippet only)*. Its audit of 138 hard problems reportedly found many flawed tests. The 59.4% figure is from a secondary report *(snippet only)*.
- **Epoch AI:** its benchmark review of 3 Sep 2026 rates Verified "Flawed" *(snippet only)*.

None of these measures memorisation of BugsInPy, BugsJS, SWE-Sharp-Bench, ReviewBench or Martian's set.

## Comparison

| Source | Our languages | Real bugs? | Areas beyond correctness | Licence | Newest bugs | Refreshed / held out | Built for review |
|---|---|---|---|---|---|---|---|
| Defects4J | none (Java) | yes | no | MIT | old | no / no | no |
| BugsInPy | Python | yes | not stated | **none** | ~2020 | no / no | no |
| BugsJS | JavaScript | yes | not stated | MIT | ≤2019 | no / no | no |
| SWE-bench Full / Verified | Python | issues (some features) | not stated | code MIT, data none stated | ≤2023 | no / no | no |
| SWE-bench Multilingual | JS, TS | issues | not stated | MIT | 2025 | no / no | no |
| SWE-bench-Live | Python, C#, JS, TS | issues | not stated | MIT | 2026 | **monthly** / no | no |
| SWE-rebench | Python | issues | not stated | CC BY 4.0 | 2026 | **moving window** / no | no |
| SWE-bench Pro | Python, JS, TS | issues | not stated | GPL code; card none | 2025 | no / **private held-out** | no |
| Multi-SWE-bench | JS, TS | issues | not stated | CC0 (with a ByteDance caveat) | early 2025 | no / no | no |
| SWE-PolyBench | Python, JS, TS | labelled bug / feature / refactor | refactoring | MIT | 2025 | no / no | no |
| SWE-Sharp-Bench | **C#** | 91 of 150 bug fixes | not stated | CDLA-Permissive-2.0 | 2025 | no / no | no |
| CVEfixes | several (not checked) | yes, fixes only | **security** | MIT / CC BY 4.0 | Jul 2024, rerunnable | **by rerunning** / no | partly |
| SecBench.js | JavaScript | yes | **security** | **none** | ≤2023 | no / no | no |
| SWE-Perf etc. | not checked | optimisations | **performance** | not checked | 2025 | no / no | no |
| ReviewBench | Python, C#, JS, TS | review findings | **reliability, maintainability, testing, security, performance** | MIT (code) | 2026 | no / no | **yes** |
| Martian offline | Python, TS | review findings | **security, perf, test gaps, style** | MIT | 2026 | online part only | **yes** |
| Qodo 1.0 | Python, C#, JS, TS | **injected** | best practice | **none** | 2026 | no / no | yes |
| Mutation tools | all four | **injected by rule** | no | permissive | n/a | made fresh | no |

## Which look best for our seeds, and why

These are my recommendations, not decisions.

1. **ReviewBench, as the main external source of real seeds.** It's the only collection built for reading review that has C#, Python, TypeScript and JavaScript, with findings labelled across most ISO/IEC 25010 areas: reliability, maintainability, testing, security and performance. A council can be run on the PR as it stands, with the golden findings as the answer key.
   - **Contamination:** its answers became public in October 2026, so it is cleanest for models whose training ended before then. The PRs' code itself is older and may already be in training data.
   - **Licence:** the data licence should be confirmed before quoting findings in the paper.
2. **SWE-bench-Live (MultiLang and Python) and SWE-rebench, for fresh bugs.** I'd pick bug-fix tasks created after the reviewing model's training cutoff. The buggy commit is the seed, the fix diff is the answer key and the test confirms the bug is real.
   - **Licences:** both are permissive (MIT and CC BY 4.0).
   - **Limits:** the seeds are mostly functional, and features have to be filtered out by hand.
3. **SWE-Sharp-Bench, for C#,** as the only C#-specific set (91 bug fixes, CDLA-Permissive-2.0). Its 2025 issues aren't fresh, and nobody has measured its contamination.
4. **CVEfixes, rerun for 2025–2026 CVEs,** for security seeds in our languages. SecBench.js would fit JavaScript, but it has no licence.
5. **Performance, maintainability and test seeds are the gap.** Only ReviewBench and Martian's set label these, and in small numbers: ReviewBench's test set has 12 performance findings. The optimisation benchmarks aren't bugs, and their measurements are unreliable on other machines *(snippet only)*.
6. **Defects4J, BugsInPy, BugsJS and SWE-bench Verified: sanity checks only, not headline results.** They're old, most likely memorised and, for Defects4J, not in our languages. BugsInPy also has no licence.
7. **Mutation tools, as a cheap control rather than the main seeds.** mutmut or Cosmic Ray, Stryker.NET and StrykerJS can plant uncontaminated, rule-made bugs in our own apps. The 0.847 against 0.066 gap suggests results on them won't carry over to real bugs. That makes them a useful floor to compare against, and a test of the same point for Claude-written seeds.
8. **An idea, not from any source:** our own apps' histories could give a truly held-out set. Fix commits in repos that have never been public can't have been seen by any model. They need no licence, and they're in our languages. The cost is the work of picking and checking each fix ourselves.

**Choosing between real and written seeds** isn't settled by these sources. The one direct comparison I found (Kumar et al.) used mutation, not Claude-written bugs. A run with the same council on ReviewBench PRs and on written seeds in matched areas would measure the gap for our setup.
