# Decision 6: how many seeds, and when evolution stops

Nov 1, 2026

Research for open decision 6 in the [decisions sheet](decisions-seeded-bugs-and-judge.md): how many planted bugs ("seeds") each app needs, and what rule decides whether a generation advances and when evolution stops. This note doesn't change the [experiment plan](../core-method/experiment-plan.md). It sets out what published work says, works through the options, and recommends one.

**Why the two have to be settled together.** The plan currently uses about 40 seeds per app. It advances a generation if it scores higher, and stops after two generations that improve by less than about 2%. An earlier check ([review notes, section 4](review-notes-oct31.md)) found that 40 seeds can only detect differences of about 20 recall points, so a 2-point rule mostly reacts to noise. How many seeds you have decides how small a difference you can see. That in turn decides what a sensible stopping rule looks like.

**How sources were checked.** Each source below is marked:

- **Full text:** the paper itself was opened and the relevant sections read. The version is named.
- **Abstract only:** only the abstract or landing page was read.
- **Snippet only:** only a search snippet, or another paper's description of it, was seen. Don't rely on these without checking.

The papers were opened and read by research subagents working on this note. I didn't re-open each one myself. "Partial" means only the first part of a long page was read. The numbers in sections 3 to 5 come from my own calculations and simulations, described in section 3.1. They are not taken from any paper.

## Contents

1. [Summary](#1-summary)
2. [What published work says](#2-what-published-work-says)
3. [Working it out for this experiment](#3-working-it-out-for-this-experiment)
4. [The options](#4-the-options)
5. [Recommendation](#5-recommendation)
6. [In plain English](#6-in-plain-english)
7. [Sources](#7-sources)

## 1. Summary

- **No source gives a rule for seeds per app.** Inspection and testing experiments used about 15 to 42 defects per document and almost never checked their statistical power. Mutation testing does give a sampling answer: about 100 mutants pin a score to roughly ±7 points, and about 1,000 to roughly ±2 points.
- **The right analysis is paired.** Give every council the same seeds and compare them seed by seed. Use McNemar's test or a bootstrap over seeds. With repeat runs, average each seed's runs first; don't count every run as a separate data point.
- **Sizes needed** (two-sided, 80% power, 20 to 30% of seeds caught by only one of the two councils):

  | Difference to detect | Seeds needed |
  | --- | --- |
  | 20 recall points | about 40 to 55 |
  | 10 points | about 155 to 235 |
  | 5 points | about 630 to 940 |

  Repeat runs help but can't replace seeds. Five points is out of reach for any single app.
- **The 2% rule doesn't work.** In my simulation, when no variant is really better, 55 to 70% of generations still "advance". No source supports a fixed-percentage plateau rule.
- **Tuning research uses a different pattern.** Racing and configuration tools (F-Race, irace, SMAC):
  - compare candidates on the same test items
  - accept a challenger only on a statistical test, not a fixed threshold
  - re-run the current best as they go
  - stop after two rounds in a row with no change
  - check the final pick on a separate test set

  The winner's score usually drops on new items. One study saw 38.0% fall to 30.7%.
- **Recommendation (option C):** 120 seeds per app, split 80 for the evolution search and 40 held out.
  - **Advance:** only if a 90% confidence interval for "variant minus parent", computed on the same seeds, lies above zero.
  - **Stop:** after two generations in a row where nothing advances, or at the caps.
  - **Final claims:** pool the held-out seeds across the three apps and run each council 3 times.

  The evolution search can then reliably find 20-point gains within an app. The final cross-app comparison can detect about 10 points (85% power). The plan should state that 5-point differences can't be resolved.
- **Cost of option C:** about 150 council reviews of an app version per app, per evolving run. That's roughly 150M tokens: about $800 at Sonnet 5.5 rates or $1,300 at Opus 5.5 rates, including the judge. Today's design costs about $300 to $500 per app. The main extra cost is human: 360 checked seeds across three apps instead of 120. That trades against decision 5.

## 2. What published work says

### 2.1 Sample sizes in mutation-testing and seeded-defect studies

- **Inspection-era experiments used a few dozen defects, without power analysis.**
  - Porter, Votta and Basili's requirements-inspection experiment used documents with 42 and 26 faults. The word "power" never appears in the report.
  - Briand et al.'s capture-recapture study used documents with 15 to 29 defects. It lists earlier studies with 16 to 38 seeded defects. Its simulation found most of the gain in estimation accuracy came from going from 6 to 12 defects. That's a different question (estimating how many defects remain), so it doesn't transfer to comparing reviewers.
- **Detection rates from about 34 faults are noisy.** Andrews, Briand, Labiche and Siami Namin (TSE 2006) compared 34 real faults with 736 mutants. Real-fault detection varied far more than mutant detection, because it "is based on 34 faults only". That is almost exactly the plan's 40-seed setup.
- **Mutation testing has a size answer.** Gopinath et al. (ISSRE 2015) tested 158 Java projects:
  - 100 sampled mutants estimated the mutation score to within about ±7 points 95% of the time.
  - 1,000 mutants got it to within about ±2 points.
  - The size needed doesn't depend on how many mutants exist in total.

  This is about measuring one score, not comparing two. A comparison needs more, or the paired design below.
- **Redundant seeds inflate scores.** Papadakis et al.'s survey reports that duplicate or "subsumed" mutants can flip experimental conclusions. Seeds that are near-copies of each other make the sample look bigger than it is.
- **Recent LLM code-review benchmarks don't report uncertainty.** CR-Bench reports 5 to 9 point recall differences from single runs with no intervals, and Qodo's PR-Review-Bench (580 injected issues) reports none either. CriticGPT (McAleese et al.) is an exception: it reports bootstrap confidence intervals.
- **Software engineering experiments are usually underpowered.** Dybå et al. (2006) found power was "substantially below accepted norms"; I saw only a snippet of this one. Kampenes et al. advise that if enough power is hard to get, you report effect sizes with confidence intervals rather than pass/fail tests.

### 2.2 Comparing recall or precision between two systems

- **Paired data needs a paired test.** When two councils review the same seeds, each seed is caught by both, by neither, or by only one. Only the "only one" seeds carry information about which council is better.
  - McNemar's test is the standard test for this (Card et al. 2020; Dietterich 1998).
  - Dietterich found McNemar's test never exceeded its stated false-positive rate. He warns it ignores the system's own run-to-run randomness, which for LLM councils is large, so average repeat runs per seed first.
  - Fagerland et al. (2013) recommend the mid-p or plain asymptotic version. The exact and continuity-corrected versions are too cautious.
- **Sample-size formula.** Connor (1987) gives the formula for McNemar's test, as reproduced in the SAS documentation. It depends on two numbers: the difference you want to detect, and the share of seeds where the two councils disagree. Card et al. recommend running the planned test on simulated data across a range of plausible effects, not relying on a single formula.
- **Precision and F1 need resampling.** They aren't simple per-item averages, so use a paired bootstrap that resamples seeds (Berg-Kirkpatrick et al. 2012; Koehn 2004) or a paired randomisation test (Card et al., appendix F).
  - Dror et al. (2018) warn the bootstrap is weak on small test sets.
  - Bowyer et al. (2025) found standard intervals under-cover below a few hundred items. A nominal 95% interval covered only about 92.5% at 100 items. They recommend Wilson or Bayesian intervals.
- **Repeat runs.** Miller (2024) gives a sample-size formula that includes K repeat runs per item. Repeats shrink only the run-to-run part of the noise; the spread between items stays. In his example, going from 1 to 10 repeats cut the smallest detectable difference from 13.2% to 7.5% at 198 items. Never treat K × n runs as K × n independent items.
- **Decision rules from one-sided bounds.** Walker and Nowacki (2011): to show A is "not worse than B by more than δ", check that the lower limit of a 90% interval is above −δ. Fix δ before collecting data. A non-significant result doesn't show two systems are equal.

### 2.3 When evolutionary and AutoML searches stop under noise

- **Racing.**
  - **Hoeffding races** (Maron and Moore 1994): add one test item per round, and drop a candidate once its best case is worse than the leader's worst case.
  - **F-Race** (Birattari et al. 2002): uses a Friedman test with test items as blocks, so all candidates see the same items. It drops only candidates that are significantly worse.
  - **irace defaults** (user guide v4.5.1; TR 2011-004):
    - It runs no elimination test until 5 instances, or 10 if instances vary a lot. After that it tests after every instance at 95% confidence.
    - It keeps the current best until challengers have run on the same instances.
    - Each race stops after two tests in a row eliminate nothing.
    - It doesn't correct for multiple comparisons, because "the search stagnates".
    - It recommends checking final picks on separate test instances.
- **Re-running the current best.**
  - SMAC (Hutter et al. 2011) gives the current best an extra run each time it's challenged. A challenger runs on the same instances and seeds, and takes over only after matching all of the current best's runs while scoring at least as well.
  - Rakshit et al.'s survey (2017) gives the reason: re-evaluating stored elites keeps genuinely good candidates and removes lucky ones.
  - Point-based searches like hill-climbing, which is roughly what the plan's "best variant replaces parent" is, are "affected by a mediocre solution with illusive good fitness".
- **Adaptive resampling.**
  - Cantú-Paz (2004) uses a one-sided t-test at 90% confidence and takes more samples until the two candidates are clearly separated. He notes this costs a lot, and that a slightly larger population with direct comparisons may be the cheaper option.
  - Branke and Schmidt (2003) spend extra samples on close pairs.
  - Hansen et al. (2009) note that re-evaluation schemes typically multiply evaluations per generation by 3 to 100.
- **Selection overfits a noisy score.** Cawley and Talbot (2010) show that when the selection score is noisy, optimising it too long makes true performance worse. The bias is "of comparable magnitude to differences between learning algorithms". Their remedies are early stopping and reporting final performance from data that played no part in the selection.
- **LLM self-improvement loops.**
  - **Darwin Gödel Machine:** screens on a small set, promotes candidates over a noise-calibrated cutoff to a bigger set, and doesn't re-run. Its best agent scored 38.0% on the 50-task subset it was picked on but 30.7% on the full benchmark.
  - **OPRO:** training accuracy was "often 5%–20% higher" than test.
  - **GEPA:** accepts a child that beats its parent on a minibatch of 3, then ranks on a separate 300-item validation set and reports on a held-out test set.
  - **EvoPrompt:** "less than 0.3% improvement over two iterations" appears only as a convergence measure, not as a stopping rule.
  - No source endorses a fixed percentage-plateau rule like the plan's 2%.

### 2.4 LLM run-to-run variance and how many items

- **Temperature 0 isn't deterministic.**
  - Ouyang et al.: ChatGPT gave inconsistent test results on 18 to 44% of coding problems even at temperature 0.
  - Atil et al.: accuracy varied by up to about 15 points between identical runs.
- **Agentic coding benchmarks swing between runs.** Bjarnason et al. (2026) ran each of 6 agent setups 10 times on SWE-bench Verified's 500 tasks. Single runs swung by 2.2 to 6.0 points. Scaled from 500 tasks to 40 seeds, that suggests single-run recall on one app could move by roughly 5+ points from noise alone (the subagent's calculation, rough).
- **Small benchmarks are noisy, and subsets more so.** Madaan et al. (2024) found the smallest benchmarks had the highest seed-to-seed variance. 100-item subsets flipped about 12% of model comparisons. Biderman et al. (2024) recommend reporting variance over several runs and releasing per-item outputs.
- **How many items.** Miller's formula, with his example variances, gives about 1,400 / 350 / 87 items for 5 / 10 / 20 points with one run each. With 5 repeats it gives about 560 / 140 / 35. Unlimited repeats can never get below 349 / 87 / 22.

## 3. Working it out for this experiment

### 3.1 Method

- **Sample sizes:** Connor's McNemar formula, at 80% power. The key unknown is the share of seeds caught by one council and missed by the other. I used 20% and 30%; the earlier review assumed 20 to 30%.
- **Stopping rules:** simulated one generation (a fresh parent run plus 3 variants), 2,000 times per setting. The model:
  - Each seed has its own difficulty, shared by all councils.
  - Each council has its own seed-by-seed strengths and weaknesses. These stay fixed when the same council re-runs the same seeds.
  - Each run then catches or misses each seed at random.
  - Base recall is 50%. In the default setting two different councils disagree on about 32% of seeds, and the same council re-run disagrees with itself on about 29%. Run-to-run noise is therefore a large part of the noise, which is consistent with the run-to-run results in 2.4.
- **Sensitivity:** I varied how strongly seeds differ in difficulty and how much councils' strengths differ. Disagreement ranged from 25 to 43%. The ranking of the rules didn't change. The exact percentages did, by up to about 15 points.

These are rough planning figures. The real disagreement rate should be measured before seed counts are fixed (step 1 of the recommendation).

### 3.2 Seeds needed for a given difference

Seeds needed when both councils review the same seeds (two-sided test, 80% power):

| Difference to detect | 20% of seeds disagree | 30% of seeds disagree |
| --- | --- | --- |
| 20 recall points | 37 | 56 |
| 15 points | 67 | 102 |
| 10 points | 155 | 233 |
| 5 points | 626 | 940 |

The smallest difference a given seed count can detect, under the same assumptions:

| Seeds | 20% disagree | 30% disagree |
| --- | --- | --- |
| 40 | 19 points | 24 points |
| 80 | 14 points | 17 points |
| 120 | 11 points | 14 points |
| 240 | 8 points | 10 points |
| 360 | 7 points | 8 points |

### 3.3 How each stopping rule behaves

The tests below use 80 search seeds and 3 variants per generation, one run each:

- "False advance" is the share of generations that advance when no variant is really better.
- The three middle columns show how often a generation advances when one variant is really better by 5, 10 or 20 points.

The cost column counts council reviews of the whole seed set per generation (N = search seeds, M = fresh confirmation seeds).

| Rule | False advance | +5 | +10 | +20 | Cost per generation |
| --- | --- | --- | --- | --- | --- |
| **Plan today:** best variant beats parent by more than 2 points | 64% | 78% | 92% | 100% | 4N |
| **CI rule:** the 90% interval for best-minus-parent lies above zero | 13% | 25% | 48% | 95% | 4N |
| CI rule with a correction for picking the best of 3 | 5% | 12% | 31% | 84% | 4N |
| **Re-run the top two:** re-run parent and top two on the same seeds, and decide on the re-run | 10% | 21% | 49% | 95% | 7N |
| **Fresh confirmation:** re-run parent and top one on 40 new seeds, and decide on those | 6% | 10% | 27% | 73% | 4N + 2M |
| Both: CI rule on the search seeds, then fresh confirmation | 0.7% | 3% | 14% | 70% | 4N + 2M, sometimes |

What this shows:

- **The 2% rule advances on noise most of the time.** It gives 55 to 70% false advances across all seed counts tested. The earlier review estimated 79%. The difference arises because the three variants share one parent run, so their chances of beating it aren't independent. When it does advance on noise, the reported gain is inflated by about 7 points at 80 seeds.
- **The CI rule cuts false advances to about 1 in 8** at no extra cost, and still catches a real 20-point gain almost every time once there are 80 seeds.
- **Re-running the top two on the same seeds isn't worth it.** It costs about 75% more per generation and buys almost nothing. A council that got lucky on particular seeds is usually lucky on them again, because part of its luck is its fixed strengths on those seeds. It only removes the run-to-run part.
- **Fresh confirmation seeds remove the winner's-curse bias** but cost power, because the decision rests on fewer seeds. The plan's held-out set already does this job once at the end. Doing it every generation adds 40 seeds per generation in human checking.
- **Correcting for best-of-3 halves false advances but loses power.** irace's guide advises against such corrections because the search stalls. A false advance isn't fatal here: the final held-out comparison catches it.

### 3.4 Seeds or repeats?

Here is the CI rule at the same review budget (120 seed-reviews per council):

| Design | Real +10 caught |
| --- | --- |
| 120 seeds × 1 run | 54 to 71% |
| 60 seeds × 2 runs | 46 to 68% |
| 40 seeds × 3 runs | 45 to 66% |

More seeds always did at least as well, and the gap widens as councils' seed-by-seed strengths differ more. Repeats are cheaper in human time, though: they need no extra seeding or checking. Miller's formula agrees. Repeats help until run noise is small next to seed-to-seed differences, and beyond that only more seeds help.

### 3.5 The final comparison

The final comparison is one winner against one comparator: the starting council, or the non-evolving control. It's chosen in advance with no best-of-k selection, so a standard two-sided 95% test applies. Pooling held-out seeds across the 3 apps gives:

| Held-out seeds, pooled | Runs per council | +5 | +10 | +20 |
| --- | --- | --- | --- | --- |
| 60 (20 per app) | 3 | 20% | 57% | 99% |
| 120 (40 per app) | 1 | 18% | 50% | 99% |
| 120 (40 per app) | 3 | 36% | **85%** | 100% |
| 300 (100 per app) | 3 | 69% | 100% | 100% |

Pooling assumes the effect is broadly similar across apps. Analyse it as seeds clustered within apps (Miller's clustered errors, or Bowyer's Bayesian model), and still report each app separately.

### 3.6 Cost assumptions

These use the plan's figures:

- **Review tokens:** one council review of one app version is about 1M tokens. In the WinScope pilot, the 4-reviewer council used 1.0M tokens on about 16,000 lines. Smaller apps or 3-reviewer councils will use less, and everything scales linearly.
- **Seeds per version:** about 10, from the decisions sheet's 8 to 12 per variant. Each council evaluation also reviews one clean (seed-free) version.
- **Judge:** about $2 per version review, which is GPT-6.1 Sol's central $4 per 2M-token run.
- **Council prices:** Sonnet 5.5 at $2/$10 and Opus 5.5 at $4/$20 per million input/output tokens (Anthropic price table, cached Oct 6, 2026). Assuming 85% of tokens are input, the blend is about $3.20 per million on Sonnet and $6.40 on Opus. Prompt caching would lower this. Mixed-family councils will differ.
- **Run shape:** 3 generations, a fresh parent run plus 3 variants each. The final comparison covers winner, starting council and non-evolving control, with 3 runs each on the held-out seeds.
- **Scope:** per app, one evolving run. Multiply by 3 apps and by the plan's repeats. Roughly double it if the non-evolving control gets its own matching spend during the search.

## 4. The options

"Detects" means 80% or better power at the stated level. Costs are per app, for one evolving run.

| Option | Seeds per app (search + held-out) | What the search can find | What the final comparison can show (3 apps pooled) | Advance rule | False advance per generation | Reviews | Tokens | Cost (Sonnet to Opus) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **A. Today** | 40 + not sized | about 20 to 24 points | not planned | beats parent by 2 points | 55 to 70% | 60 | 60M | $310 to $500 |
| **B. Light** | 40 + 20 | 20 points about 3 times in 4 | 20 points (99%); 10 points only 57% | CI clears zero | about 13% | 87 | 87M | $450 to $730 |
| **C. Recommended** | 80 + 40 | 20 points (95%) | **10 points (85%)** | CI clears zero | about 13% | 153 | 153M | $800 to $1,290 |
| **D. 10 points per app** | 200 + 100 | 10 points (about 80%) | 5 points (69%) | CI clears zero | about 12% | 351 | 351M | $1,830 to $2,950 |
| **E. 5 points per app** | 800 + 400 | 5 points | 5 points | CI clears zero | about 12% | 1,341 | 1.3B | $7,000 to $11,300 |
| C with re-run top two | 80 + 40 | same as C | same as C | re-run on same seeds | about 10% | 234 | 234M | $1,220 to $1,970 |
| C with fresh confirmation | 80 + 40 + 40 per generation | 20 points about 3 times in 4 | same as C | fresh-seed CI | about 6% | 183 | 183M | $950 to $1,540 |

- **B** costs least and fixes the noise problem, but its final claims stay at about 20 points.
- **D** is the cheapest way to make within-app claims at 10 points, but it needs 900 checked seeds across three apps.
- **E** isn't realistic. If 5-point differences matter, they need pooling across many apps, or a cheaper source of seeds such as automated mutants with automated checks.

## 5. Recommendation

**Option C**, as a pre-registered package:

1. **Calibrate first.** Before fixing the numbers, run the starting council 3 times on one app's seeds, and run one variant once. Measure two things: how often the two councils disagree on a seed, and how often the same council disagrees with itself. If disagreement is under 20%, 60 search seeds will do. If it's over 35%, move toward 100. Publish the measured numbers with the plan.
2. **Seeds.** 120 per app: 80 for the evolution search and 40 held out, never shown to the search. About 10 per app version, plus one clean version.
   - Every council sees the same seeds.
   - Drop near-duplicate seeds, so the count isn't inflated.
   - Keep the 10/20/40/30 severity mix. Report severity groups as counts ("caught 3 of 4 critical") rather than percentages.
3. **Advance rule.** Each generation, re-run the parent alongside the 3 variants on the search seeds. The best variant advances only if the 90% confidence interval for its recall minus the parent's, seed by seed, lies entirely above zero.
   - Use a paired bootstrap over seeds, or the McNemar-based interval.
   - Optionally, add a guard so precision can't fall by more than a pre-set margin, such as 10 points.
4. **Stop rule.** Stop after two generations in a row in which no variant clears the bar, or at the generation, token or time caps, whichever comes first. This is irace's "two tests in a row with no change". It replaces "two generations under about 2%".
5. **Final claims.**
   - Run the winner, the starting council and the non-evolving control 3 times each on the 40 held-out seeds per app.
   - Pool across the 3 apps, treating seeds as clustered within apps, for the headline comparisons.
   - Report every app separately too, with Wilson or Bayesian intervals.
   - Report the winner's held-out score, not its search score, because the search score is inflated.
6. **Say what can't be resolved.** State in the plan that the evolution search can only reliably find gains of about 20 points within one app, the final pooled comparison can detect about 10, and differences of about 5 points can't be resolved.

**Why C over the others:**

- It fixes the 2% rule's noise problem at no extra cost per generation.
- It's the cheapest option whose final, pooled claims reach 10 points. That's about the size of difference the council-size and evolution questions are likely to turn on.
- It stays within what one person can realistically check for three apps.
- Re-running the top two on the same seeds costs about 75% more and adds almost nothing.
- Fresh confirmation every generation costs more checked seeds for a guard the held-out set already provides.

**What it costs:** about 150M tokens per app per evolving run, about $800 to $1,300 at API rates including the judge. That's about 2.5 times today's design. The biggest added cost is human: about 360 checked seeds across three apps instead of 120, which bears directly on decision 5.

## 6. In plain English

Imagine judging two spell-checkers by hiding 40 typos in a document and counting how many each one finds. If one finds 22 and the other 20, is it really better? Probably not. Some typos are easy and some are hard, and on a different day either checker might find a couple more or fewer. With only 40 typos, a gap of a few points can easily be luck.

The plan's current rule says "keep the new version if it scores higher, and stop when improvements fall under 2%". With 40 typos, luck alone moves the score by far more than 2 points. So the rule would keep "improvements" that are really just lucky days, most of the time. It would also rarely stop, because noise keeps looking like progress.

The fix has three parts:

1. **Give everyone the same typos, and compare typo by typo.** Typos both checkers find, or both miss, tell you nothing about which is better. Only the ones where they disagree do. Comparing on the same typos removes the "this test happened to be easier" problem.
2. **Only keep a change when the evidence clears a bar.** A confidence interval is the range the true difference probably sits in, given the noise. "Advance only if the whole range is above zero" means: keep the new version only if, even allowing for bad luck, it's still better. Sometimes a real improvement gets missed, but far fewer flukes get kept.
3. **Keep some typos back for the end.** The search keeps whichever variant looked best, and looking best partly means getting lucky. So check the final winner on typos it never saw. That score is the honest one.

More typos give sharper answers, but the cost grows fast. Halving the size of difference you can detect takes about four times as many seeds. With the recommended 120 per app, the experiment can tell a 20-point improvement from luck within one app. Combining all three apps at the end, it can do the same for a 10-point improvement. A 5-point difference would need several hundred seeds per app, so the plan should simply say it can't resolve differences that small.

## 7. Sources

Status is how the source was read: **Full text**, **Abstract only** or **Snippet only**, as defined at the top.

### Mutation testing and seeded defects

1. Gopinath, Alipour, Ahmed, Jensen & Groce, "How Hard Does Mutation Analysis Have to Be, Anyway?", ISSRE 2015, pp. 216–227. [Author copy](https://nimble-genie-739c5b.netlify.app/resources/issre2015/gopinath2015howhard.pdf). **Full text.**
2. Zhang, Hou, Hu, Xie & Mei, "Is Operator-Based Mutant Selection Superior to Random Mutant Selection?", ICSE 2010. [PDF](https://taoxie.cs.illinois.edu/publications/icse10-mutation.pdf). **Full text.**
3. Andrews, Briand & Labiche, "Is Mutation an Appropriate Tool for Testing Experiments?", ICSE 2005. **Snippet only:** the PDF needed a login. Its findings are known from item 4.
4. Andrews, Briand, Labiche & Siami Namin, "Using Mutation Analysis for Assessing and Comparing Testing Coverage Criteria", IEEE TSE 32(8), 2006. [PDF](https://www.depts.ttu.edu/cs/research/avesta/documents/papers/TSE2006/TSE06.pdf). **Full text.**
5. Papadakis, Kintis, Zhang, Jia, Le Traon & Harman, "Mutation Testing Advances: An Analysis and Survey", Advances in Computers 112, 2019. [Accepted preprint](https://mutationtesting.uni.lu/survey.pdf). **Full text.**
6. Porter, Votta & Basili, "Comparing Detection Methods for Software Requirements Inspections: A Replicated Experiment", IEEE TSE 21(6), 1995. [UMD tech report CS-TR-3327.1](https://api.drum.lib.umd.edu/server/api/core/bitstreams/332d6328-bdce-4726-9102-e00bac748f9a/content). **Full text** of the tech report, not the published journal version.
7. Basili & Selby, "Comparing the Effectiveness of Software Testing Strategies", IEEE TSE 13(12), 1987. **Snippet only.**
8. Briand, El Emam, Freimut & Laitenberger, "A Comprehensive Evaluation of Capture-Recapture Models for Estimating Software Defect Content", IEEE TSE 26(6), 2000. [NRC tech report ERB-1084](https://www.ehealthinformation.ca/web/default/files/wp-files/2001-A-Comprehensive-Evaluation.pdf). **Full text** of the tech report.
9. Eick et al., capture-recapture in software inspections, 1992. **Snippet only:** known through item 8.
10. Pereira, Sinha, Ghosh & Dutta, "CR-Bench", [arXiv 2603.11078v1](https://arxiv.org/html/2603.11078v1), 2026. **Full text.**
11. Qodo, PR-Review-Bench [dataset card](https://huggingface.co/datasets/Qodo/PR-Review-Bench/blob/main/README.md). **Full text** of the card. It is a dataset card, not a paper.
12. McAleese et al., "LLM Critics Help Catch LLM Bugs", [arXiv 2407.00215v1](https://arxiv.org/pdf/2407.00215v1), 2024. **Full text.** The size of the evaluation set wasn't found.
13. Dybå, Kampenes & Sjøberg, "A Systematic Review of Statistical Power in Software Engineering Experiments", Information and Software Technology 48(8), 2006. **Snippet only.**
14. Kampenes, Dybå, Hannay & Sjøberg, "A Systematic Review of Effect Size in Software Engineering Experiments". [Simula preprint](https://cms.simula.no/sites/default/files/publications/Kampenes.2006.1.pdf). **Full text** of the preprint. Its journal details weren't confirmed from that copy.
15. de Oliveira Neto, Torkar, Feldt et al., "Evolution of Statistical Analysis in Empirical Software Engineering Research", [arXiv 1706.00933v7](https://arxiv.org/pdf/1706.00933). **Full text.**

### Comparing two systems: power and tests

16. Card, Henderson, Khandelwal, Jia, Mahowald & Jurafsky, "With Little Power Comes Great Responsibility", EMNLP 2020. [ACL Anthology PDF](https://aclanthology.org/2020.emnlp-main.745.pdf) for the main text; arXiv 2010.06595v1 for the appendices. **Full text.**
17. Dietterich, "Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms", Neural Computation 10(7), 1998. [Author preprint, Dec 1997](https://web.engr.oregonstate.edu/~tgd/publications/dietterich-approximate-statistical-tests-nc1998.pdf). **Full text** of the preprint, not the typeset journal version.
18. Fagerland, Lydersen & Laake, "The McNemar Test for Binary Matched-Pairs Data: Mid-p and Asymptotic Are Better than Exact Conditional", BMC Medical Research Methodology 13:91, 2013. [PMC HTML](https://pmc.ncbi.nlm.nih.gov/articles/PMC3716987/). **Full text.**
19. Dror, Baumer, Shlomov & Reichart, "The Hitchhiker's Guide to Testing Statistical Significance in NLP", ACL 2018. [ACL Anthology P18-1128](https://aclanthology.org/P18-1128.pdf). **Full text.**
20. Berg-Kirkpatrick, Burkett & Klein, "An Empirical Investigation of Statistical Significance in NLP", EMNLP-CoNLL 2012. [ACL Anthology D12-1091](https://aclanthology.org/D12-1091.pdf). **Full text.**
21. Koehn, "Statistical Significance Tests for Machine Translation Evaluation", EMNLP 2004. [ACL Anthology W04-3250](https://aclanthology.org/W04-3250.pdf). **Full text.**
22. Connor, "Sample Size for Testing Differences in Proportions for the Paired-Sample Design", Biometrics 43:207–211, 1987. **Snippet only:** JSTOR wouldn't load. The formula was taken from the [SAS PROC POWER documentation](https://support.sas.com/documentation/cdl/en/statug/67523/HTML/default/statug_power_details55.htm), which was read in full.
23. Lachin, "Power and Sample Size Evaluation for the McNemar Test…", Statistics in Medicine 11(9), 1992. **Snippet only.**
24. Lachenbruch, "On the Sample Size for Studies Based upon McNemar's Test", Statistics in Medicine 11(11), 1992. **Snippet only:** known through item 16.
25. McNemar, "Note on the Sampling Error of the Difference Between Correlated Proportions or Percentages", Psychometrika 12(2), 1947. **Snippet only.**
26. Field & Welsh, "Bootstrapping Clustered Data", JRSS-B 69(3), 2007. **Abstract only.**
27. Walker & Nowacki, "Understanding Equivalence and Noninferiority Testing", J Gen Intern Med 26(2), 2011. [PMC3019319](https://pmc.ncbi.nlm.nih.gov/articles/PMC3019319/). **Full text.**

### Noisy evolutionary and AutoML search

28. Jin & Branke, "Evolutionary Optimization in Uncertain Environments — A Survey", IEEE TEVC 9(3), 2005. **Snippet only:** the PDF returned 404.
29. Rakshit, Konar & Das, "Noisy Evolutionary Optimization Algorithms — A Comprehensive Survey", Swarm and Evolutionary Computation 33, 2017. [Author's accepted manuscript](https://next.openmole.org/paper/rakshit2016.pdf). **Full text.**
30. Hansen, Niederberger, Guzzella & Koumoutsakos, "A Method for Handling Uncertainty in Evolutionary Optimization…", IEEE TEVC 13(1), 2009. [Author PDF with errata](https://cmap.polytechnique.fr/~nikolaus.hansen/TEC2009online.pdf). **Full text.**
31. Branke & Schmidt, "Selection in the Presence of Noise", GECCO 2003, LNCS 2723. [PDF](https://www.cs.york.ac.uk/rts/docs/GECCO_2003/papers/2723/27230766.pdf). **Full text.**
32. Cantú-Paz, "Adaptive Sampling for Noisy Problems", GECCO 2004, LNCS 3102. [PDF](https://www.cs.york.ac.uk/rts/docs/GECCO_2004/Conference%20proceedings/papers/3102/31020947.pdf). **Full text.**
33. Maron & Moore, "Hoeffding Races", NIPS 6, 1994. [NeurIPS PDF](https://papers.neurips.cc/paper_files/paper/1993/file/02a32ad2669e6fe298e607fe7cc0e1a0-Paper.pdf). **Full text.** The 1997 journal follow-up wasn't opened.
34. Birattari, Stützle, Paquete & Varrentrapp, "A Racing Algorithm for Configuring Metaheuristics", GECCO 2002. [PDF](https://iridia.ulb.ac.be/~mbiro/paperi/BirStuPaqVar2002gecco.pdf). **Full text.**
35. López-Ibáñez et al., irace: [user guide v4.5.1](https://cran.r-project.org/web/packages/irace/vignettes/irace-package.pdf) and IRIDIA TR/IRIDIA/2011-004 (revised Jan 2013). **Full text** of both. The 2016 Operations Research Perspectives journal paper returned 403 and wasn't read.
36. Hutter, Hoos & Leyton-Brown, "Sequential Model-Based Optimization for General Algorithm Configuration" (SMAC), LION 5, 2011. [Extended tech report](https://www.cs.ubc.ca/~hutter/papers/10-TR-SMAC.pdf). **Full text** of the tech report.
37. Li, Jamieson, DeSalvo, Rostamizadeh & Talwalkar, "Hyperband", JMLR 18, 2018. [PDF](https://jmlr.org/papers/volume18/16-558/16-558.pdf). **Full text.** Jamieson & Talwalkar (2016) on successive halving wasn't opened separately.
38. Cawley & Talbot, "On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation", JMLR 11, 2010. [PDF](https://jmlr.org/papers/volume11/cawley10a/cawley10a.pdf). **Full text.**
39. Zhang, Hu, Lu, Lange & Clune, "Darwin Gödel Machine", [arXiv 2505.22954v3](https://arxiv.org/html/2505.22954). **Full text, partial:** the methods sections were read.
40. Agrawal et al., "GEPA", [arXiv 2507.19457v2](https://arxiv.org/html/2507.19457v2). **Full text.**
41. Yang et al., "Large Language Models as Optimizers" (OPRO), [arXiv 2309.03409v3](https://arxiv.org/html/2309.03409). **Full text, partial.**
42. Guo et al., "EvoPrompt", [arXiv 2309.08532v3](https://arxiv.org/html/2309.08532). **Full text, partial.**
43. Novikov et al., "AlphaEvolve", [arXiv 2506.13131v1](https://arxiv.org/html/2506.13131). **Full text, partial.**

### LLM evaluation variance

44. Miller, "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations", [arXiv 2411.00640v1](https://arxiv.org/abs/2411.00640), 2024. **Full text.**
45. Bowyer, Aitchison & Ivanova, "Position: Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints", ICML 2025, [arXiv 2503.01747v3](https://arxiv.org/html/2503.01747). **Full text, partial.**
46. Madaan et al., "Quantifying Variance in Evaluation Benchmarks", [arXiv 2406.10229v1](https://arxiv.org/html/2406.10229), 2024. **Full text.** Its "seeds" are training seeds, not inference reruns.
47. Heineman et al., "Signal and Noise: A Framework for Reducing Uncertainty in Language Model Evaluation", [arXiv 2508.13144v1](https://arxiv.org/html/2508.13144), 2025. **Full text, partial.**
48. Maia Polo et al., "tinyBenchmarks: Evaluating LLMs with Fewer Examples", ICML 2024, [arXiv 2402.14992v2](https://arxiv.org/html/2402.14992). **Full text.** The exact per-method error figures are only in charts, so treat those as **abstract only**.
49. Biderman et al., "Lessons from the Trenches on Reproducible Evaluation of Language Models", [arXiv 2405.14782v3](https://arxiv.org/html/2405.14782), 2024. **Full text, partial.**
50. Ouyang, Zhang, Harman & Wang, "An Empirical Study of the Non-determinism of ChatGPT in Code Generation", [arXiv 2308.02828v2](https://arxiv.org/html/2308.02828v2). **Full text.**
51. Atil et al., "Non-Determinism of 'Deterministic' LLM Settings" (first titled "LLM Stability"), [arXiv 2408.04667v5](https://arxiv.org/html/2408.04667). **Full text.**
52. Bjarnason, Silva & Monperrus, "On Randomness in Agentic Evals", [arXiv 2602.07150v2](https://arxiv.org/html/2602.07150v2), 2026. **Full text.**
53. Yang et al., "SWE-agent", arXiv 2405.15793, 2024 (run-to-run SD on SWE-bench Lite). **Snippet only.** Not cited above.

### Prices

54. Anthropic model price table (Sonnet 5.5, Opus 5.5), as cached Oct 6, 2026 in Claude Code's API reference. Recheck before the run, as decision 9 recommends.
