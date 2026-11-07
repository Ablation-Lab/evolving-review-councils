# WinScope pilot: pre-registration

**Status: DRAFT, not yet frozen.** Written Nov 3, 2026, before any pilot run. It is frozen (dated and committed) only after the researcher approves the design. After that it doesn't change; any later deviation is reported as a deviation.

**This is a pilot.** With about 40 seeds it can only detect differences of about 20 recall points ([decision 6 note](../research/decision-6-seeds-and-stopping.md)). It doesn't replace the full experiment in the [experiment plan](../core-method/experiment-plan.md), and nothing here is a final result. Design details and costs are in [design-and-costs.md](design-and-costs.md).

## Question

On one real app (WinScope 1.1, about 17,600 lines of C# and XAML), does a three-reviewer council find more planted bugs than one reviewer at roughly the same usage? Does an author-framed reviewer find fewer than a fresh one? Does a mixed-family council do better than a Claude-only council? And how much do results vary between repeat runs?

## Seeds

- **40 planted bugs:** 13 replays of real pilot bugs, 14 Stryker.NET mutants and 13 bugs written by Mistral Large 4.
- **Severity:** 4 critical, 8 high, 16 medium and 12 low (the plan's 10/20/40/30% mix).
- **Variants:** four seeded variants of 10 seeds each, assigned at random within severity and source (the random seed is recorded). One clean variant with no seeds measures false alarms.
- **Proof:** every seed has a triggering test that fails with it and passes without it. Reviewers never see the tests.
- **Checking:** Stryker mutants are checked automatically (they must compile and fail at least one held-out test). The researcher checks every replay and every Mistral seed by hand.
- **Hiding:** reviewers get a source tree with no git history and no tests, formatted the same way throughout. Comments that describe the exact behaviour a seed breaks are made neutral.

## Conditions

Every condition reviews all five variants with the same brief and the same read-only tools (list, read, search).

| ID | Condition | Runs |
| --- | --- | --- |
| S1 | One Claude reviewer, broad brief | 1 |
| C3 | Three Claude reviewers (logic; security and privacy; Windows and WPF risks), together using about the same as S1 | 3 (run-to-run variance) |
| SR | Author-framed review: Claude told it wrote the code and given the build notes (a proxy for builder self-review; see the design doc) | 1 |
| MX | Mixed council: Claude, Gemini 4 Argon and DeepSeek V4 Pro, with the three roles rotated between runs | 2 |

All Claude reviewers use Opus 5.5 at medium effort, through Claude Code on the Max plan, each in a fresh session with no memory or project notes. Every reviewer uses made-up test data only.

## Scoring

- **Merger:** every condition's output, including single reviewers', passes through the same merger (GPT-6.1 Sol). The merger doesn't see the answer key, and its output hides how many reviewers there were.
- **Judge:** GPT-6.1 Sol, pinned to a dated snapshot, at high effort. It sees the merged findings, the answer key and the code, but not which condition produced them. A location pre-match (same file, within ±5 lines) narrows the candidates. The judge then rules each finding a match to seed X (same root cause), a real bug that wasn't planted, or a false alarm, and sets its severity.
- **Second judge:** DeepSeek V4 Pro re-judges a random 15% of findings, drawn only from conditions with no DeepSeek reviewer. Agreement is reported as a percentage and as Cohen's kappa.
- **Judge calibration:** before scoring, the researcher labels about 50 findings from a separate calibration run (S1 on one variant, not counted in results). Scoring goes ahead only if the judge agrees with at least 90% of them.
- **Metrics for each condition and run:**
  - recall on the 40 seeds, with a Wilson 95% interval
  - severity-weighted recall (×4 critical, ×2 high, ×1 medium, ×0.5 low)
  - precision counting only planted bugs (the headline), plus a second precision that also credits real bugs nobody planted
  - false alarms on the clean variant
  - tokens, time and cost
- **Variance:** across the three C3 runs, the spread in recall and the per-seed disagreement rate. These feed the calibration step of the full experiment.
- **Failures:** a run that errors, refuses or is cut off is rerun once, then reported as a failure, not as "no findings".

## Pre-registered comparisons

All comparisons are paired on the same 40 seeds, using the recall difference with a 90% paired-bootstrap interval:

1. C3 (mean of 3 runs) vs S1
2. SR vs S1
3. MX (mean of 2 runs) vs C3 (mean of 3 runs)

## What counts as a result

- **"Detected at pilot scale":** the 90% interval for a difference lies entirely above or below zero.
- **"Not detected":** anything else. It means no difference, or a difference smaller than about 20 points. It is never reported as "the same".
- **Cost:** reported alongside quality for every condition.
- **Reporting:** all conditions, failures and deviations are reported, whatever the outcome.
- **Publication:** the seed key and the seeded diffs are published after the runs.
