# Seeded bugs and the outside judge: background research

Oct 31, 2026

Background research for two parts of the [experiment plan](../core-method/experiment-plan.md): planting known bugs so reviewer councils can be scored on recall and precision, and choosing the non-Anthropic model that acts as the fixed judge and merger. This note doesn't change the plan. It sets out options and recommendations for decisions that are still open.

**How sources were checked.** Every source cited below was opened and read, unless it's marked **[unverified]**. That tag means only a search snippet was seen, or the page couldn't be opened, so don't rely on it before checking it yourself. Prices and benchmark scores are as shown on Oct 31, 2026. They change often.

## Contents

1. [Seeded bugs](#1-seeded-bugs)
2. [Judge and merger model](#2-judge-and-merger-model)
3. [Summary](#3-summary)
4. [Open decisions](#4-open-decisions)
5. [Sources](#5-sources)

## 1. Seeded bugs

### 1.1 The idea, and why it's hard

Planting known bugs to measure how good a reviewer is goes back to the 1970s. It's called *bebugging*, fault seeding or error seeding. Weinberg named it in 1970, mainly as a way to train and assess programmers, and Mills turned it into an estimate of how many bugs remain. The basic assumption is that reviewers find planted bugs at about the same rate as real ones ([Wikipedia: Bebugging](https://en.wikipedia.org/wiki/Bebugging)).

The whole method rests on that assumption, and there's evidence it often fails:

- **Synthetic bugs are much easier than real ones.** Kumar, Bararia and Raj ([arXiv 2606.15689](https://arxiv.org/html/2606.15689v1), Apr 2026) scored five LLM code reviewers on 100 mutation-injected bugs and 50 real bug-fix PRs. Claude Haiku 4.5 scored an F1 of 0.847 on the synthetic bugs but only 0.066 on the real PRs, a 92% drop. The authors conclude that "synthetic-only evaluation overestimates capability by an order of magnitude". Part of the gap is diff size (median 5 lines synthetic, 117 real), so planted bugs should sit in realistic amounts of surrounding code.
- **Some kinds of bug barely get caught.** In the same study, recall on performance bugs (N+1 queries, unbounded queries) was 0% for four of the five models. Security recall was about 70%, and logic recall was low. A seed set that leans on one category will give a skewed score.
- **Mutants stand in for real faults only partly.** Just et al. ([FSE 2014](https://homes.cs.washington.edu/~mernst/pubs/mutation-effectiveness-fse2014.pdf)) studied 357 real faults in 5 Java projects against 230,000 mutants. Mutant detection correlated significantly with real-fault detection. 73% of the real faults were coupled to common mutants. 10% needed new or stronger mutation operators, and 17% (mostly algorithm changes or deleted code) weren't coupled to any mutant at all.

### 1.2 Ways to plant bugs

| Approach | Examples | Strengths | Weaknesses for this experiment |
| --- | --- | --- | --- |
| **Rule-based mutation** | Stryker.NET (C#), StrykerJS, PIT | Cheap, automatic, reproducible, large volume | Small, local changes, often easy to spot. Misses the 17% of real faults that no mutant matches, and has few security, concurrency or design-level bugs |
| **LLM-generated mutation** | LLMorpheus; BugFarm (evaluated in Wang et al.) | More varied and closer to real bugs | More mutants that don't compile, duplicate others or change nothing; needs filtering |
| **Real-bug replay** | Defects4J, SWE-bench, SWE-Sharp-Bench, your own fix history | Real bugs, often with a test that proves each one | Public sets are probably in training data. Few real-bug sets exist for C# |
| **Taint-based vulnerability injection** | LAVA | Each bug comes with a triggering input, at large volume | C only, buffer overflows only; can't inject logic bugs; injection created unintended extra bugs |
| **Hand-seeded** | KyleSau/reviewbench | Realistic and labelled exactly as intended | Slow, small sets, and the author's own blind spots shape the seeds |

**Rule-based mutation for C#/.NET: Stryker.NET.** It's the main C# mutation tool. Its operators cover arithmetic, equality, logical and boolean operators, assignments, initialisers, removing statements or blocks (including `return`, `throw` and method calls), LINQ swaps (`First` to `FirstOrDefault`, `All` to `Any`), string and string-method changes, regex, bitwise and math operators, null-coalescing (`??`), the conditional operator and collection expressions ([mutations](https://stryker-mutator.io/docs/stryker-net/mutations/)).

Its [configuration](https://stryker-mutator.io/docs/stryker-net/configuration/) has the controls seeding needs:

- `mutate` globs, including character spans such as `File.cs{10..100}`
- `mutation-level` and `ignore-mutations`
- `since` (mutate only code changed since a git target)
- a `json` reporter that lists every mutant
- `target-framework` for multi-targeted projects

You run it from the unit-test project folder, and it needs the .NET 10 runtime even when the app targets an older .NET ([getting started](https://stryker-mutator.io/docs/stryker-net/getting-started/)).

Stryker.NET's docs don't mention WPF, XAML or `net8.0-windows`, and a search found no clear statement either way, so WPF support is **unknown and needs a quick test**. It only mutates C#, never XAML.

**LLM-generated mutation.**

- **LLMorpheus** (Tip, Bell & Schaefer, [arXiv 2404.09952](https://arxiv.org/abs/2404.09952)) puts placeholders in JavaScript code and asks an LLM what should replace them. It produced mutants that resemble real bugs StrykerJS can't generate.
- **Wang et al.** ([arXiv 2406.09843](https://arxiv.org/abs/2406.09843v5)) compared LLM mutation with rule-based mutation on 851 real Java bugs. LLM mutants were more varied and behaved more like real bugs: they detected 87.98% of the real bugs against 41.64%. But they had 26.6 points more non-compiling mutants, 10.1 points more duplicates and 3.5 points more equivalent mutants (changes that don't alter behaviour).

**Real-bug datasets.**

- **Defects4J** ([GitHub](https://github.com/rjust/defects4j)), v3.0.1: 854 active real Java bugs from 17 projects. Each has a buggy version, a fixed version and a test that fails on the bug and passes on the fix.
- **SWE-bench** (Jimenez et al., ICLR 2024, [arXiv 2310.06770](https://arxiv.org/abs/2310.06770)): 2,294 tasks from real GitHub issues in 12 Python repositories. [swebench.com](https://www.swebench.com/) lists Lite, Verified, Multilingual and Multimodal variants. The page didn't give their sizes or languages.
- **SWE-Sharp-Bench** (Mhatre et al., Microsoft, [arXiv 2511.02352](https://arxiv.org/abs/2511.02352v3)): 150 C# tasks from 17 repositories. About 40% are resolved, against about 70% on SWE-bench Verified with the same set-ups. It's the closest .NET set. It tests issue resolution, not review, so it suits the plan's outside coding yardstick, not WinScope scoring.
- **Contamination.** Liang, Garg & Zilouchian Moghaddam ([arXiv 2506.12286](https://arxiv.org/abs/2506.12286)) gave models only the issue text. Models named the buggy file with up to 76% accuracy on SWE-bench Verified, but up to 53% on repositories outside SWE-bench. They also reproduced code word for word more often on SWE-bench (up to 35% 5-gram overlap, against 18%). Public bug sets may be partly memorised, and a private, freshly seeded app avoids that. The LAVA authors made the same point in 2016: released bug corpora "rapidly become stale".

**Taint-based injection: LAVA.** Dolan-Gavitt et al. ([IEEE S&P 2016](https://css.csail.mit.edu/6.566/2018/readings/lava.pdf)) used dynamic taint analysis to find input bytes that reach a program unchanged and could trigger a bug. They then injected thousands of buffer overflows into eight real programs, including bash, tshark and the GNU coreutils. Each bug came with an input that triggers it. Three lessons carry over to C#, even though the tool doesn't:

- **Seeding can add bugs by accident.** LAVA's injection code sometimes added extra bugs (use-after-free, uninitialised pointers), and tools under test found them. The authors had to remove them and rerun.
- **Some bug classes can't be injected this way.** The authors expect logic errors, crypto flaws and side channels to stay out of reach.
- **False alarms are the hard part.** For tools that "gesture at a line" without a triggering input, the authors saw no way to measure false alarms without a lot of manual work. That's exactly the precision problem with AI reviewers, and it's why the plan needs a judge.

**Code-review benchmarks: how others score reviewers.**

| Benchmark | Ground truth | Size | Matching | Notes |
| --- | --- | --- | --- | --- |
| [GitHub ReviewBench](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/) (Oct 2026) | Real PRs; findings pooled from human reviewers, follow-up commits, static analysis and several LLM families, then deduplicated | 219 PRs (25-PR dev split) | LLM judge (Claude Sonnet 5) against a rubric; senior engineers agreed with 96.6% of labels | Reports *grounded* precision and recall (known issues only) and *augmented* ones (the judge also rules on findings outside the gold set). The dataset is public, so it isn't hidden |
| [Qodo](https://www.qodo.ai/blog/which-llm-should-review-your-code/) (Oct 2026) | Real bugs traced back to the PR that introduced them, **not injected** | 125 internal PRs, 703 bugs | LLM judge (Claude Sonnet 4.6), pairwise | Vendor-run and private. The text and table disagree on some figures |
| [Kodus CodeReviewBench](https://www.codereviewbench.com/leaderboard) | Human-authored golden bugs in real PRs | 30 PRs, 95 bugs | LLM judge (Claude Haiku 4.5) | Ranks by F1 because "recall alone rewards whoever talks most" |
| [KyleSau/reviewbench](https://github.com/KyleSau/reviewbench) | Hand-seeded bugs in small PRs (Python, TypeScript, **C#**), plus 6 clean PRs | 25 PRs, 21 issues | Same file, within ±3 lines, matching category, one-to-one; an optional blind LLM judge | Wilson 95% intervals. With only 21 issues, one issue moves recall by about 4.8 points |
| [Kumar et al.](https://arxiv.org/html/2606.15689v1) | 100 mutation seeds and 50 real PRs | 150 samples | Deterministic file and ±5 lines first (about 70% of cases), then an LLM judge; partial match scores 0.5 | Severity-weighted F1 (critical ×4, high ×2, medium ×1, low ×0.5) |

Two patterns recur:

- **Matching happens in two steps.** A cheap location match comes first, and an LLM judge rules only on unclear cases.
- **Real bugs outside the answer key need their own bucket.** A reviewer will find genuine bugs nobody planted. Counting them as false alarms punishes good reviewers, which is why GitHub reports augmented scores.

### 1.3 Keeping seeds realistic, varied and hidden

Pulled together from the sources above:

**Realistic**

- Mix sources. Synthetic-only scores overstate ability by about ten times (Kumar et al.), and mutants miss about a sixth of real fault types (Just et al.).
- Prefer seeds that the existing tests don't catch. This matches how the pilot's 97 findings all slipped past the builders' tests.
- Put seeds in realistically large code, not tiny diffs.
- Give every seed a proof: a held-out test or input that fails with the seed and passes without it, as Defects4J and LAVA do.

**Varied in severity and kind**

- Label each seed's category and severity on the same scale the judge uses.
- Spread seeds across logic, security, privacy, concurrency, performance, resource leaks and seams between modules.
- Score recall for each category and severity separately, plus severity-weighted recall, so an average can't hide a missed critical bug.

**Hidden from reviewers**

- Keep the answer key and the triggering tests outside the reviewers' sandbox (KyleSau's harness strips labels from what the reviewer sees).
- Remove every clue:
  - no git history, or one squashed commit with a neutral message
  - no telling comments, names or TODOs
  - run the formatter after seeding so the seeded code doesn't stand out by style
  - don't put telling hints in PR descriptions; KyleSau's PR descriptions may give bugs away
- If reviewers see a diff, mix harmless real changes into it so that not every changed hunk is a bug.
- Include clean variants with no seeds, to measure false alarms.

**Fair to score**

- After seeding, check each seed adds only the intended defect (LAVA's accidental bugs).
- Record "real, but not seeded" findings separately (GitHub's augmented scores).
- Use enough seeds for useful confidence intervals: 21 issues gave KyleSau intervals about 40 points wide.

**Protected against gaming**

- Rotate seed sets across generations.
- Keep one seed set that is never used during evolution, as the held-out test, so an evolving council can't learn the answer key.

### 1.4 Recommended approach for WinScope (.NET 8 WPF)

The aim is a private, versioned set of seeded WinScope variants with an answer key, built from three sources and checked by a person.

**1. Freeze a base.** Tag WinScope 1.1 (about 16,000 lines, 1,051 tests) as the base. Build seeded variants in a private copy. Reviewers get an exported tree with no `.git` folder, the planted-bug list, the triggering tests or the pilot write-up.

**2. Draw seeds from three sources, about a third each:**

- **a. Replay real pilot bugs.** The pilot's 97 findings are real WinScope bugs with known severity, for example:
  - the Recycle Bin trailing-dot bug
  - elevated writes to user AppData
  - temp cleanup that missed 8.3 short names
  - the redactor treating "server" as a version string

  Their buggy versions are in WinScope's history. This is the most realistic source. Two cautions:
  - The pilot write-up in this repo describes many of these bugs, so reviewers must have no web or repo access.
  - Councils that see the same replayed bugs every generation could learn them, so keep some replays in the held-out set only.
- **b. Stryker.NET mutants that survive the tests.** Run Stryker on the logic-heavy projects (Core and each `Modules/<tool>` library and its tests) and use the JSON report to pick mutants the 1,051 tests didn't kill. Check each one by hand to throw out equivalent mutants. They're cheap and reproducible, but small and local, so limit them to about a third. First check that Stryker builds a `net8.0-windows` WPF solution. If it doesn't, point it only at the class libraries that don't depend on WPF.
- **c. LLM-written, test-aware seeds for kinds mutation can't produce:**
  - WPF: UI-thread and Dispatcher misuse, `async void` handlers, event-handler and binding leaks
  - Windows: path normalisation, short names, elevation and time-of-check bugs, registry access
  - privacy: redaction gaps
  - performance: redraw loops, slow shutdown
  - seams between modules

  Each seed must compile, pass the existing tests and come with a held-out test that fails with it. Have a model family that's neither on the council nor the judge write them. A person reviews every one (it takes some time, but it's the main guard against unrealistic seeds).

**3. Severity mix and numbers.** Use the judge's scale (critical, high, medium, low). A reasonable starting mix is about 10% critical, 20% high, 40% medium and 30% low. Use roughly 8 to 12 seeds per variant, so reviewers aren't flooded with bugs, and at least 40 seeds across an app's variants, so recall intervals mean something. Add one clean variant per app.

**4. The answer key.** One record per seed:

- ID and source (replay, Stryker or LLM)
- file and line range
- category and severity
- one-sentence root cause
- the triggering test

Keep the key outside every agent's sandbox, version it, and publish it only after the runs, to match the plan's "published first" rule for scoring rules.

**5. Scoring.**

- **Matching:** same file, within about ±5 lines, then the judge rules on whether the finding has the same root cause, without knowing which council produced it.
- **Duplicates:** count once.
- **Precision and recall:** report grounded figures (seeds only) and augmented figures (the judge also rules on unmatched findings, real-unseeded or false).
- **Breakdowns:** recall for each source, category and severity, plus severity-weighted recall. Show Wilson intervals throughout.
- **Check for synthetic inflation:** if recall on Stryker seeds is far above recall on replays, that's the effect Kumar et al. found, and the headline figure should lean on the realistic seeds.

**6. Rotation.** Make several seeded variants per app. Use some during evolution, and keep one variant (with its own seeds) for the held-out test of the winner.

## 2. Judge and merger model

### 2.1 What the judge has to be good at

The judge doesn't need to find bugs. It has to:

- match findings to the answer key
- decide whether an unmatched finding is a real bug or a false alarm, and set its severity
- merge findings without dropping good ones

That's closer to checking than to finding, so precision and calibration matter more than recall. No public benchmark measures LLM *judging* of code-review findings directly. The review benchmarks below are the nearest proxy.

It also needs to:

- **Stay fixed** for the whole experiment: a pinned model version that won't change or be retired halfway through.
- **Stay off every council**, as the plan requires.
- **Be cheap** enough to rerun.

### 2.2 Three options

| | **OpenAI GPT-6.1 Sol** | **Google Gemini 4 Argon** | **DeepSeek V4 Pro** (open weights) |
| --- | --- | --- | --- |
| API ID | `gpt-6.1-sol` | `gemini-4-argon` | `deepseek-v4-pro` (V4-Pro-0813) |
| Price per 1M tokens (input / output) | $2 / $10 ([pricing](https://developers.openai.com/api/docs/pricing)) | $2 / $10 until Nov 30, 2026, then **$4 / $20** from Dec 1 ([pricing](https://ai.google.dev/gemini-api/docs/pricing)) | $1.32 / $3.96 peak, $0.66 / $1.98 off-peak, cache-miss input ([pricing](https://api-docs.deepseek.com/quick_start/pricing)) |
| Discounts | Batch or Flex 50% off; cached input $0.10 | Batch 50% off; cached input $0.10 | Cache-hit input $0.022 to $0.044; off-peak is half price |
| Long-input surcharge | Requests over 272K input tokens cost $4 / $15 | None listed | None listed |
| Context | 1.05M tokens, 128K max output ([models](https://developers.openai.com/api/docs/models)) | 1,048,576 tokens shared by input and output; 65,536 output by default ([model page](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon)) | 1M tokens ([model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)) |
| Code review, Qodo | Not tested. The older **GPT-6 Sol** (medium effort): precision 59.1%, recall 41.4%, F1 48.7%, $0.18 per PR | Not tested | Precision 59.4%, recall 43.0%, F1 49.9%, $1.05 per PR, 440 s per PR |
| Code review, Kodus | Not tested | Not tested | #1 of 13: F1 43.9 (precision 43.6%, recall 44.2%) |
| Vals Index (agentic; about 37% coding) ([Vals](https://www.vals.ai/benchmarks/vals_index)) | 63.94%, #8 | 69.24%, #4, the top non-Anthropic model | 52.97%, #23 |
| Weights | Closed | Closed | MIT licence, 1.6T total and 49B active parameters |

For scale, Anthropic models led Qodo's table, with Opus 5.5 at F1 56.8%, but they're ruled out as judge by design. GPT-6 Astra, OpenAI's flagship at $10 / $50, scored *below* GPT-6 Sol on Qodo (F1 46.6%), so paying five times more buys no review advantage there. Gemini 3.8 Flash had the highest precision on Qodo (71.0%) but low recall. Kimi K3 (open weights) scored F1 49.0% on Qodo.

**Reading the table.**

- **GPT-6.1 Sol** is the safest all-rounder:
  - verified prices and a 1M context
  - Batch pricing, since judging doesn't need to be instant
  - its predecessor's precision is close to the best non-Anthropic models at a fraction of the cost
  - the main risk is that OpenAI retires older models over time, which hurts reproducibility
- **Gemini 4 Argon** has the strongest general agentic score, but it has no code-review results yet. It's new, and its price doubles on Dec 1, before the runs are likely to start.
- **DeepSeek V4 Pro**:
  - led one review leaderboard and is the cheapest
  - its MIT-licensed weights mean anyone can rerun exactly the same judge later, the strongest argument for reproducibility
  - against: slow (440 s per Qodo PR), a much lower general score, peak and off-peak pricing, and code sent to DeepSeek's API unless it runs elsewhere
  - at 1.6T parameters, self-hosting isn't practical for this project

**Recommendation.** Use **GPT-6.1 Sol** as the fixed judge and merger, pinned to a dated snapshot and run through Batch. Use **DeepSeek V4 Pro** as a second judge on a 10 to 20% sample of findings to measure how far the judge's verdicts depend on which model gives them. Before the first run, check the judge against about 50 findings labelled by a person, and publish its agreement rate. GitHub's 96.6% engineer agreement is a useful bar. If OpenAI models are wanted on councils, make DeepSeek V4 Pro the main judge instead, and accept the slower runs.

### 2.3 Cost of judging one council run (about 2M review tokens)

The judge doesn't need to re-read all 2M tokens. In the pilot, the 4-reviewer council used 1.0M tokens to produce 48 findings, and those token counts include agents re-reading their own context. The judge reads the findings, the answer key, the rubric and the code around each finding. So three cases:

- **Lean:** 0.5M input, 0.1M output
- **Central:** 1M input, 0.2M output
- **Heavy:** the judge re-reads everything, 2M input, 0.4M output

Output includes reasoning tokens. Google's price table says so for Gemini, and other reasoning models bill thinking as output too. Merging is included in these figures.

Cost per council run, at standard (not Batch) rates:

| Model | Lean | Central | Heavy | Central, Batch |
| --- | --- | --- | --- | --- |
| GPT-6.1 Sol | $2.00 | $4.00 | $8.00 | $2.00 |
| GPT-6 Astra (for comparison) | $10.00 | $20.00 | $40.00 | $10.00 |
| Gemini 4 Argon, until Nov 30 | $2.00 | $4.00 | $8.00 | $2.00 |
| Gemini 4 Argon, from Dec 1 | $4.00 | $8.00 | $16.00 | $4.00 |
| DeepSeek V4 Pro, peak | $1.06 | $2.11 | $4.22 | no Batch listed |
| DeepSeek V4 Pro, off-peak | $0.53 | $1.06 | $2.11 | no Batch listed |

Assumptions and caveats:

- **OpenAI charges more for requests over 272K input tokens.** Judge one finding, or a small batch, per request to stay under it.
- **Caching cuts input costs.** Caching the rubric and answer key prefix lowers input costs further: cached input is $0.10 per million on Sol and Argon, and under $0.05 on DeepSeek.
- **Effort level changes output volume.** The plan runs the judge on high effort. Higher effort produces more output tokens, which is where most of the cost goes.
- **Across the experiment:** at the central case, 100 judged runs cost about $400 on Sol ($200 with Batch), $400 to $800 on Argon, and $106 to $211 on DeepSeek. Judging is a small cost next to the councils themselves.

## 3. Summary

- **Seeded bugs work, with a known flaw.** Synthetic bugs make reviewers look far better than they are (a 92% F1 drop on real PRs in one study), and mutants miss about a sixth of real fault types. Mix sources and score each source separately.
- **For WinScope, use three sources, about a third each.** Replays of the pilot's 97 real bugs, Stryker.NET mutants the tests don't catch, and LLM-written WPF and Windows bugs checked by a person. Each seed gets a severity label and a hidden triggering test.
- **Hide seeds properly and score fairly.** No git history, formatter run after seeding, clean variants, a held-out seed set that's never used during evolution, and a separate bucket for real bugs that weren't planted.
- **Two things to check before building on them.** Stryker.NET's WPF support is undocumented and needs a quick test. No public C# review benchmark exists; SWE-Sharp-Bench tests fixing issues, not review.
- **Judge: GPT-6.1 Sol, pinned and run through Batch,** with DeepSeek V4 Pro as a spot-check second judge. Gemini 4 Argon is strong but has no review results, and its price doubles on Dec 1.
- **Judging one 2M-token council run costs about $2 to $8 on GPT-6.1 Sol,** about $4 central and $2 with Batch. On DeepSeek V4 Pro it's about $0.50 to $4.

## 4. Open decisions

1. **Which model family stays off every council?** This decides the judge. If the cross-family council arm should include OpenAI models, the judge has to be Google or DeepSeek.
2. **How much reproducibility do you need?** Open weights (DeepSeek) let anyone rerun the exact judge later. A closed API (Sol) is faster and stronger in general, but the model may be retired.
3. **Do reviewers see the whole codebase or a diff?** This changes how seeds are hidden: whether decoy changes are needed, and how large a review unit is.
4. **Are replayed pilot bugs allowed?** They're the most realistic seeds, but they're described publicly in this repo, so reviewers would need strict isolation from the web and the repo.
5. **Seed numbers and severity mix.** The suggestion is about 40 or more seeds per app, 8 to 12 per variant, and roughly 10/20/40/30% critical, high, medium and low. This decides how wide the confidence intervals are.
6. **Who writes the LLM seeds, and how much checking by a person can you afford?** The seed-writing model should be on neither the council nor the judge.
7. **Grounded or augmented precision as the headline score?** Grounded is fairer for comparing councils. Augmented credits real bugs that weren't planted.
8. **Judge check before the first run:** how many findings to label by hand, and what agreement rate is good enough to go ahead.
9. **Timing against price changes:** Gemini 4 Argon doubles in price on Dec 1, 2026. Recheck all prices before the runs.

## 5. Sources

### Opened and read

**Seeded bugs**

- [Bebugging](https://en.wikipedia.org/wiki/Bebugging), Wikipedia.
- Dolan-Gavitt et al., [LAVA: Large-scale Automated Vulnerability Addition](https://css.csail.mit.edu/6.566/2018/readings/lava.pdf), IEEE S&P 2016 (full PDF text read).
- Just et al., [Are Mutants a Valid Substitute for Real Faults in Software Testing?](https://homes.cs.washington.edu/~mernst/pubs/mutation-effectiveness-fse2014.pdf), FSE 2014 (full PDF text read).
- Tip, Bell & Schaefer, [LLMorpheus: Mutation Testing using Large Language Models](https://arxiv.org/abs/2404.09952), arXiv 2404.09952 (abstract page).
- Wang et al., [A Comprehensive Study on Large Language Models for Mutation Testing](https://arxiv.org/abs/2406.09843v5), arXiv 2406.09843 (abstract page).
- Stryker.NET docs: [mutations](https://stryker-mutator.io/docs/stryker-net/mutations/), [configuration](https://stryker-mutator.io/docs/stryker-net/configuration/), [getting started](https://stryker-mutator.io/docs/stryker-net/getting-started/), [introduction](https://stryker-mutator.io/docs/stryker-net/introduction/).
- [Defects4J](https://github.com/rjust/defects4j) repository README.
- Jimenez et al., [SWE-bench](https://arxiv.org/abs/2310.06770), ICLR 2024 (abstract page); [swebench.com](https://www.swebench.com/) leaderboards page.
- Mhatre et al., [SWE-Sharp-Bench](https://arxiv.org/abs/2511.02352v3), arXiv 2511.02352 (abstract page).
- Liang, Garg & Zilouchian Moghaddam, [The SWE-Bench Illusion](https://arxiv.org/abs/2506.12286), arXiv 2506.12286 (abstract page).

**Code-review benchmarks**

- Kumar, Bararia & Raj, [Bigger Isn't Always Better: A Comparative Evaluation of LLMs for Automated Code Review](https://arxiv.org/html/2606.15689v1), arXiv 2606.15689.
- GitHub Blog, [ReviewBench: An open benchmark for AI code review](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/), Oct 5, 2026.
- [KyleSau/reviewbench](https://github.com/KyleSau/reviewbench) repository README.
- Qodo, [Which LLM should review your code?](https://www.qodo.ai/blog/which-llm-should-review-your-code/), Oct 12, 2026.
- Kodus, [AI Code Review Benchmark Leaderboard](https://www.codereviewbench.com/leaderboard).

**Judge models**

- OpenAI, [API pricing](https://developers.openai.com/api/docs/pricing) and [models](https://developers.openai.com/api/docs/models).
- Google, [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) (updated Oct 30, 2026), [models overview](https://ai.google.dev/gemini-api/docs/models) and [Gemini 4 Argon model page](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon).
- DeepSeek, [API pricing](https://api-docs.deepseek.com/quick_start/pricing); [DeepSeek-V4-Pro model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) on Hugging Face.
- Vals AI, [Vals Index](https://www.vals.ai/benchmarks/vals_index) (updated Oct 29, 2026) and [Gemini 4 Argon comparison page](https://www.vals.ai/comparisons/google_gemini-4-argon-vs-meta_muse-wonder-full).
- Vellum, [GPT-6 Astra benchmarks explained](https://vellum.ai/blog/gpt-6-astra-benchmarks-explained). Background only: Astra released Sep 3, 2026; its coding lead is contested.

### [unverified]: seen only as search snippets, or couldn't be opened

These aren't relied on above.

- **OpenAI pages that wouldn't open.** [Introducing GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol/) and [openai.com/api/pricing](https://openai.com/api/pricing/) both returned HTTP 403. Sol's prices above come from the developer pricing page instead, which did open.
- **Kimi K3.1 Pro.** API pricing of $2 / $10, a 1M context and open weights due Nov 4, 2026, seen only in snippets ([letsdatascience](https://letsdatascience.com/news/moonshot-releases-kimi-k31-pro-api-open-weights-due-nov-4-786e160c), [aicybr](https://aicybr.com/blog/kimi-k3-1-pro-api-open-weights-benchmarks-cyber-training)). No primary Moonshot page was opened. The Vals Index (opened) puts K3.1 Pro at 62.52%, #9.
- **Gemini 4 Argon.** Third-party coding claims such as DeepSWE 77.9 and FrontierSWE v2 55.0% against GPT-6 Astra's 65.5% ([apidog](https://apidog.com/blog/gemini-4-argon-benchmarks/), [DataLearner](https://www.datalearner.com/en/ai-models/pretrained-models/gemini-4-argon/analysis)).
- **Test-aware LLM seeding.** Kiele et al., ESEM 2026 ([arXiv/alphaxiv 2609.35841](https://www.alphaxiv.org/abs/2609.35841)): LLM-generated subtle bugs that still pass existing tests. Seen only as a snippet. The test-aware seeding advice above stands without it.
- **SWE-Mutation** ([arXiv 2605.22175](https://arxiv.org/html/2605.22175v1)): agentic LLM mutation for judging test suites.
- **Stryker.NET and WPF.** A search found nothing either way.
- **SWE-Sharp-Bench's motivation.** The claim that C# was "absent" from earlier SWE-bench-style sets was seen in a snippet, not on the abstract page.
- **Other surveys.** [Augment Code guide on AI review accuracy](https://www.augmentcode.com/guides/ai-code-review-accuracy) and a [Medium survey of 2026 code-review benchmarks](https://medium.com/@codzee.io/we-compared-the-public-ai-code-review-benchmarks-from-2026-methodology-datasets-metrics-and-269dd35637a6). One search snippet described Qodo's benchmark as "injected defects", but the Qodo page itself says its bugs are real and not injected.
