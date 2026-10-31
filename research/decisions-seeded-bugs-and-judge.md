# Decisions: seeded bugs and the judge

Oct 31, 2026. The nine open decisions from [seeded-bugs-and-judge.md](seeded-bugs-and-judge.md), ordered so the ones that block others come first.

## 1. Which model family stays off every council?

- **OpenAI:** strong, cheap judge (GPT-6.1 Sol). Con: no OpenAI models in the cross-family council.
- **DeepSeek:** open-weight judge anyone can rerun. Con: slow, and weaker in general.
- **Google:** strongest general scores. Con: no code-review results yet, and the price doubles Dec 1.

**Recommendation:** OpenAI. Sol gives the best mix of review precision, price and context. Councils can still mix Anthropic, Google and DeepSeek models.

**Affects:** 2, 5, 8, 9.

George's decision:

## 2. Should the judge favour reproducibility or strength?

- **Closed API (GPT-6.1 Sol):** faster and stronger. Con: OpenAI may retire it.
- **Open weights (DeepSeek V4 Pro):** the exact judge can be rerun forever. Con: 440 s per PR, and a lower general score.

**Recommendation:** Sol as the main judge, pinned to a dated snapshot, with DeepSeek re-judging 10–20% of findings. The sample shows whether verdicts depend on the judge, and it leaves a rerunnable check.

**Affects:** 8, 9.

George's decision:

## 3. Do reviewers see the whole codebase or a diff?

- **Whole codebase:** seeds hide naturally. Con: more tokens per review.
- **Diff:** cheaper, and like real pull requests. Con: needs decoy changes, or every changed hunk is a bug.

**Recommendation:** whole codebase for the main runs. It matches how the pilot reviewed WinScope and avoids a design for decoys. A diff arm can be added later.

**Affects:** 6, and token budgets.

George's decision:

## 4. Are replays of the pilot's real bugs allowed as seeds?

- **Yes:** the most realistic seeds, with known severity. Con: the pilot write-up in this repo describes them, so reviewers need no web or repo access.
- **No:** no leak risk. Con: more weight falls on synthetic seeds, which overstate recall.

**Recommendation:** yes, with strict sandboxing, and some replays kept only in the held-out set. Without them, scores lean on the kind of seeds that inflated F1 about tenfold in one study.

**Affects:** 6, and the sandbox rules.

George's decision:

## 5. Who writes the LLM seeds, and how much do you check by hand?

- **A model family on neither the council nor the judge, with every seed checked by you:** the most realistic. Con: your time.
- **The same, with only a sample checked:** faster. Con: unrealistic seeds can slip through.
- **The judge's family:** simple. Con: the judge marks bugs its own family wrote.

**Recommendation:** a family on neither, with every seed checked by a person. With about 40 seeds per app this is manageable, and it's the main guard against unrealistic seeds.

**Affects:** 6.

George's decision:

## 6. How many seeds, and in what severity mix?

- **About 40 per app, 8–12 per variant, 10/20/40/30% critical/high/medium/low:** usable confidence intervals. Con: more seeding work.
- **About 20 per app:** cheaper. Con: intervals about 40 points wide, too wide to compare councils.

**Recommendation:** the first option, plus one clean variant per app to measure false alarms. Fewer seeds can't separate councils that differ by a few points.

**Affects:** cost, and how the held-out set is built.

George's decision:

## 7. Which precision is the headline score?

- **Grounded (planted bugs only):** fair and fixed across councils. Con: real bugs nobody planted count as false alarms.
- **Augmented (the judge also rules on unmatched findings):** credits real finds. Con: the denominator changes per council, and the judge does more work.

**Recommendation:** grounded as the headline and augmented as a second figure, as GitHub's ReviewBench does. Comparisons stay fair, and good reviewers still get credit.

**Affects:** 8, and judge cost.

George's decision:

## 8. How do we check the judge before the first run?

- **About 50 findings labelled by a person, at least 90% agreement required:** a real check. Con: a few hours of labelling.
- **About 20 findings:** quicker. Con: the agreement figure is too uncertain to trust.

**Recommendation:** about 50 findings, publishing the agreement rate. GitHub reports 96.6% engineer agreement, so 90% is a reasonable minimum.

**Affects:** the start date.

George's decision:

## 9. When do we lock in prices?

- **Recheck all prices the week before the first run:** the budget is accurate. Con: the estimates may move.
- **Use today's prices:** simple. Con: Gemini 4 Argon doubles on Dec 1, and others may change.

**Recommendation:** recheck the week before, and record the prices used in the run logs. Judging is cheap (about $2–8 per run on Sol), so this is about accurate reporting more than budget.

**Affects:** nothing else.

George's decision:
