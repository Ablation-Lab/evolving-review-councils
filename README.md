# Evolving Review Councils

Does a council of AI reviewer agents catch more real problems in code than one reviewer at the same cost, and can a council evolve to get better? This repo holds the research plan, the notebook it grew from and the outside reviews of it, published as the work happens.

When an AI agent reviews code, it usually works alone. This project tests councils of reviewers against single reviewers and against each other, at equal cost, on real bugs from public pull requests and security fixes. A council here is several Claude subagents with different roles, a judge that rules on their findings and an appeal that re-checks what the judge dismissed. Then the best council evolves: a change is kept only if it beats the version before it, and the result is scored on held-out bugs the search never saw.

It started when I asked Claude to spawn a council of separate reviewer agents instead of reviewing alone. Those councils kept catching problems the builder had missed, which raised the question: is a council actually worth it, or would one reviewer do as well for the same cost?

> **Teaser video:** coming soon. The explainer video's source is in [council-video](https://github.com/Ablation-Lab/council-video).

## Where it stands (20 Nov 2026)

- **The research plan is built,** and its main design decisions are made. A few smaller decisions and checks remain before it's locked.
- **Three confirmatory hypotheses:**
  - **H8:** the appeal recovers real bugs the judge wrongly dismissed, without adding many false findings.
  - **H9:** role sets, meaning different ways of dividing the review areas among the seats, differ in catch rate at equal cost.
  - **H11:** on the held-out bugs, the evolved council catches more than the council it started from, at about the same cost per review.
- **One exploratory hypothesis, H10:** whether catch rates differ between security bugs fixed before and after the reviewing model's training cutoff, as a check on memorised fixes.
- **The core comparison:** five role sets on 105 real bugs (15 in each of seven review areas), 3 repeats each. A fresh set of 105 is held out for the final comparison. Scoring is by a judge model from outside the Claude family.

## What's been run so far

All pilots, reported as exploratory:
- **An informal pilot on one app:** fresh reviewers found 97 problems the builders' own tests had passed.
- **Early council runs and an appeal stress test:** in 72 direct appeal trials, the appeal caught 161 of 162 wrongful dismissals.
- **Two difficulty checks, of 10 bugs each:** councils caught all 10 both times, so the material was too easy. The next check uses harder material.
- **Smaller checks:** run-isolation and messaging checks, and a small comparison with a cloud review tool (3 runs, one on each of 3 pilot bugs).
- **Dry runs on made-up material (20 Nov):** these confirmed the run set-up. They also found two routes into the agents that hadn't been recorded, which the set-up now closes.

## What's next

Hand-checking three packs of pilot findings, then a difficulty check on harder material. After a few remaining checks and decisions, the plan is locked, dated and published, and the formal runs start.

## Read more

- [Research plan](core-method/research-plan.md): the plan itself, covering the hypotheses, design, run rules, measures, analysis, decisions and threats.
- [Notebook](core-method/experiment-plan.md): the working record the plan was built from, with every run and field note.
- [Outside reviews](core-method/outside-reviews.md): every outside review of the work, with each suggestion's decision.
- [Power simulations](core-method/power/): the scripts behind the plan's power figures, and their results.
- [Prior work](core-method/prior-work-research.md): how much of this has been done before.
- Also: [the WinScope pilot](core-method/winscope-pilot.md), [council size by task complexity](core-method/council-size-by-task-complexity.md), [spin-offs](spin-offs/) and [supporting material](supporting-material/).

The runs use [Council Dial Lite](https://github.com/Ablation-Lab/council-dial-lite).

---

Research by George, Ablation Lab.
