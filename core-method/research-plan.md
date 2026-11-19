# Research plan

The research plan for evolving review councils, as its own document. The notebook, [experiment-plan.md](experiment-plan.md), stays the dated record of how the plan was reached.

- **How it was built (19 Nov 2026):** only from what the notebook, [outside-reviews.md](outside-reviews.md), [prior-work-research.md](prior-work-research.md) and the decision files already say. Nothing new is decided here.
- **Its source:** this follows the structure outside review 10 proposed ([reviews L818](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L818)).
- **Links:** each point links to its source lines at commit `87eb410`, so the links don't move when the notebook changes. "plan" is the notebook, "reviews" is outside-reviews.md, "prior" is prior-work-research.md, "briefs" is [decisions-pending-2026-11-17.md](decisions-pending-2026-11-17.md), "sheet" is [the 2 Nov decisions sheet](../research/decisions-seeded-bugs-and-judge.md) and "decision 6" is [decision-6-seeds-and-stopping.md](../research/decision-6-seeds-and-stopping.md).
- **What isn't decided:** each such point is a marked **Decision pending** slot. It says what has to be decided, and points to its finding in outside review 10 or elsewhere. Where sources disagree, the slot lists both and picks neither.
- **Not locked:** this document isn't the locked plan. The notebook says the plan is to be "locked, dated and published" before the formal experiment ([reviews L10](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L10)). Locking it is still to do.

## Contents

1. [Status](#1-status)
2. [Aims and research questions](#2-aims-and-research-questions)
3. [Hypotheses](#3-hypotheses)
4. [Design](#4-design)
5. [Procedure and run rules](#5-procedure-and-run-rules)
6. [Measures and scoring](#6-measures-and-scoring)
7. [Analysis](#7-analysis)
8. [Pilot and exploratory results](#8-pilot-and-exploratory-results)
9. [Decisions log](#9-decisions-log)
10. [Threats and limits](#10-threats-and-limits)
11. [Related work](#11-related-work)
12. [Open questions and the ideas backlog](#12-open-questions-and-the-ideas-backlog)
13. [Publishing and deliverables](#13-publishing-and-deliverables)

## 1. Status

As of 19 Nov 2026.

- **What has run** (details in section 8):
  - the WinScope pilot ([plan L178](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L178));
  - the first Council Dial runs and the appeal stress tests, including 72 direct appeal trials ([plan L359](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L359));
  - the run-isolation dry run ([plan L870](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L870));
  - two difficulty checks on pilot seeds, review A on the easy tier and review B on the hard tier ([plan L889](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L889), [plan L943](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L943));
  - the messaging check ([plan L1058](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1058));
  - an exploratory Ultrareview baseline ([plan L1092](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1092)).
- **What hasn't run:**
  - the appeal experiment, judged with against without the appeal ([plan L330](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L330));
  - the role-set comparison ([reviews L150](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L150));
  - the formal evolution experiment.
- **What's decided:**
  - the seven 19 Nov decisions, (a) to (g) ([plan L1237](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1237));
  - the 2 Nov decisions on seeds and the judge ([sheet L3](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L3));
  - the 12–13 Nov decisions on seed sources, seat roles and who sees the seeds ([reviews L110](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L110), [plan L835](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L835)).
  - Section 9 lists them all.
- **What's next,** in order:
  1. I mark the three hand-check packs ([plan L1275](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1275));
  2. decision (a)'s difficulty check, on "no diff, plus surrounding modules", with bands fixed first ([plan L1243](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1243));
  3. a dry run of Lite under the `SendMessage` deny ([plan L1250](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1250)).
- **What's locked:** nothing yet.
  - **Frozen:** the role-set briefs, for the comparison ([plan L836](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L836)).
  - **To fix in the locked plan before the formal runs:** rank-first, among other things ([plan L1015](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1015)).

## 2. Aims and research questions

**Aims,** as the notebook's Goals give them ([plan L11](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L11)):

1. Find the optimum council size, and the most efficient setup overall.
2. Produce a default recipe built around a median token budget per app build, with a hard agent cap.
3. Define the prerequisites for raising that cap.
4. Check that the recipe holds across different kinds of apps.

**Research questions,** numbered here from where the sources pose them. The sources give no single list (outside review 10, S3: [reviews L810](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L810)).

1. **Does a council beat simpler set-ups at the same cost?** ([plan L1455](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1455))
2. **Do whole role sets differ at equal cost against planted bugs?** That covers A, A′, B, C and a generalist ([reviews L150](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L150), [reviews L254](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L254)).
3. **Does an appeal that can reinstate the judge's dismissals recover wrongly dismissed bugs, and at what cost?** ([plan L336](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L336))
4. **Does an evolving council improve, against a non-evolving control at the same spend?** ([plan L43](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L43))
5. **Does the optimum council size change with task complexity?** ([plan L1547](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1547))
6. **Do mixed-family councils beat all-Claude ones at equal cost?** ([reviews L192](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L192))
7. **How much freedom should the orchestration have?** That's the workflow edition against Lite ([reviews L473](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L473)).
8. **Does a project's `CLAUDE.md` help or bias reviewers?** A secondary experiment ([plan L1262](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1262)).

> **Decision pending (outside review 10, C8: [reviews L829](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L829)):** which list of "what's new" the plan states. The sources disagree:
> - the plan's Related research names "evolving councils for code review, a council-size scale for each complexity tier, and a calculator" ([plan L1815](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1815)), but the calculator isn't built ([plan L1701](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1701));
> - outside review 3's focus, adopted 12 Nov, names the appeal, role sets at equal cost, the judge's severity calls checked against a key, and evolving or racing councils ([reviews L185](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L185));
> - prior's novelty summary names the appeal within code review, severity calibration, the equal-cost role-set comparison on code and racing councils, and says the contribution is "the measurement, not the architecture" ([prior L700](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L700), [prior L703](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L703)).

## 3. Hypotheses

The sources state these as hypotheses or ideas to test. None is marked confirmatory or exploratory.

| # | Hypothesis | Source | As the source labels it |
|---|---|---|---|
| H1 | A council of different strong models covers each other's blind spots, and beats one model and copies of it | [plan L1465](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1465) | "core hypothesis" |
| H2 | For review, a reviewer without the author's context beats a smarter model checking its own work | [plan L1472](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1472) | hypothesis, tested at the same cost |
| H3 | More effort isn't always better: a judge or appeal on xhigh could make more wrong rulings than one on medium | [plan L1535](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1535) | hypothesis |
| H4 | Background anchors a reviewer on the author's framing, and less context lets it explore more widely | [plan L637](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L637) | hypothesis |
| H5 | Fable may make a stronger judge or analyser | [plan L1338](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1338) | hypothesis, to test |
| H6 | Families may share blind spots inherited from common roots, so a different family buys less independence than assumed | [plan L1335](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1335) | idea, to test |
| H7 | A misleading `CLAUDE.md` lowers catches (the bias side, tested first) | [plan L1263](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1263) | design of decision (e) |

> **Decision pending (outside review 10, S3: [reviews L810](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L810)):** which hypotheses are confirmatory and which exploratory, and the null hypothesis for each confirmatory one. Prior's reading of *The More the Better?* as "the project's null hypothesis" for the role-set question bears on this ([prior L211](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L211)).

## 4. Design

### 4.1 The arms

- **Role sets,** decided 12–13 Nov ([reviews L135](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L135)):
  - **A:** the current seats, as the baseline;
  - **A′:** A's three areas in the new checklist format, with a neutral opening ([reviews L254](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L254));
  - **B:** three wide seats, with the new areas folded in;
  - **C:** five narrow seats;
  - **a single generalist** with an ISO checklist ([reviews L150](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L150)).
  - **Coverage:** six of ISO/IEC 25010's nine areas, plus docs and policy accuracy ([reviews L139](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L139)). Policy is in the docs seat of B, C and G too ([reviews L257](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L257)).
  - **Scoring A′:** against B and C, only on seeds whose checklist item A′ has ([reviews L301](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L301)).
  - **The briefs:** written on the local `seat-roles` branch of Lite ([reviews L210](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L210)), and frozen for the comparison ([plan L836](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L836)).
- **Baselines** ([plan L1455](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1455)):
  - one reviewer with a broader brief and the same budget;
  - one reviewer rerun several times;
  - a self-recheck;
  - builder self-review at the same cost;
  - generalists, specialists or a mix, at equal cost;
  - the diverse-models arms (three copies of one model, models from one family, a cross-family mix, each model alone, and a size mix);
  - a smarter model alone.
  - **A stronger single-reviewer baseline,** adopted 12 Nov: one generalist, run several times and pooled, at the same cost as the councils ([reviews L170](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L170)).
- **Debate arms,** adopted 16 Nov: independent seats, structured debate relayed by the main session, and free debate as an agent team ([reviews L423](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L423)).
- **The workflow edition** against Lite, adopted for comparison on 16 Nov ([reviews L492](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L492)). Its design is outside review 7's item 5, adopted with the interrupted-run rule on 19 Nov ([reviews L397](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L397)).
- **The evolution experiment:** each evolving council against a non-evolving one with the same rounds and spend ([plan L43](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L43)).
- **Other arms in the notebook:**
  - merging options ([plan L1475](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1475));
  - simpler alternatives such as linters ([plan L1493](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1493));
  - cheaper against stronger reviewers ([plan L1502](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1502));
  - effort levels ([plan L1532](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1532)).
- **The `CLAUDE.md` test:** a secondary experiment after the plan is locked ([plan L1262](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1262)).

> **Decision pending (outside review 10, G5: [reviews L854](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L854)):** the role-set comparison's design, which has no section of its own. That means its seed count, repeats, cost matching, scoring and analysis. Its parts are spread over the outside reviews and a private plan ([reviews L135](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L135)), and "the number of repeats per role set" is still open ([reviews L156](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L156)).

> **Decision pending (outside review 10, G6: [reviews L855](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L855)):** how the role-set comparison and the evolution experiment relate. Do they run in sequence, and does one locked plan cover both? Seat roles are to be "settled, researched and tested before the plan is locked" ([reviews L104](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L104)).

### 4.2 Material and seed tiers

- **The easy tier (pilot only):** 35 candidates from ReviewBench and MCR-Bench, five in each of seven areas ([plan L820](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L820)). It grew to 37 seeds in 35 folders ([plan L858](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L858)).
- **The hard tier (pilot only):** 10 escaped bugs, traced from later fixes with SZZ and hand-checked ([plan L917](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L917)). Both tiers proved too easy (section 8).
- **Next:** the 10 hard folders as the code after the change plus the modules around it, with no diff ([plan L1243](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1243)).
- **What a folder holds:** the changed files, the diff and a one-line neutral description, and nothing from the fix ([plan L860](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L860)).
- **Rules for material:**
  - generated files are left out ([plan L928](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L928));
  - no web access in council runs ([plan L863](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L863));
  - future seeds favour bugs fixed after the models' training cutoff, as a precaution ([plan L974](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L974)).
- **Seed sources,** decided 13 Nov: MCR-Bench first, ReviewBench, SWE-bench-Live as a contamination check, CVEfixes later, and written seeds only for safety and policy ([reviews L328](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L328)).
- **Checklist-item tags:** every pilot seed has one (47 seeds, 42 tagged, 5 "none"; 26 carry an A′ item) ([plan L1286](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1286)).

> **Decision pending (outside review 10, C2: [reviews L823](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L823)):** the seed design for the formal runs. The sources disagree:
> - **2 Nov:** 120 seeds per app (80 search, 40 held out), a 10/20/40/30% critical/high/medium/low mix and one clean variant per app, starting with WinScope ([plan L20](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L20), [sheet L74](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L74)). Mistral writes the model-written seeds, and the pilot's real bugs are replayed ([sheet L60](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L60), [sheet L48](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L48)).
> - **12–13 Nov:** real bugs are the main seeds ([reviews L112](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L112)), in equal numbers per area to start ([reviews L127](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L127)). They come from other projects' pull requests, rated HIGH, MED or LOW ([plan L855](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L855)).
> - **What reviewers see:** the 2 Nov decision is "whole codebase by default, with diff as a comparison arm" ([sheet L37](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L37)). The pilot material holds the diff, and the next check drops it (above).

> **Decision pending (outside review 10, C3: [reviews L824](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L824)):** whether the seed pilot's results go in the paper. The sources disagree:
> - "the 35 pilot seeds are used only for the difficulty check and tooling tests, never reported as results" ([plan L846](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L846)), and the hard-tier seeds are pilot-only too ([plan L938](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L938));
> - the paper "leads with its experiments, the appeal and the pilot results" ([plan L814](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L814)), and outside review 9's item 2, pending, asks to bring in the results since 12 Nov ([reviews L713](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L713)).
> - "The pilot results" may mean WinScope rather than the seed pilot. The sources don't say.

### 4.3 Seats and briefs

- **Brief version 3:** what each seat is given and blind to, for reviewers, the judge, the appeal and Lite's check ([plan L60](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L60)).
- **The read-only agent:** Read, Grep and Glob only, when running code isn't allowed ([plan L62](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L62)).
- **The appeal:** it gets a dismissed block and a severity block ([plan L71](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L71)).
- **`omitClaudeMd`:** Lite 2.2.5 dropped it, and the full edition keeps it ([plan L139](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L139)). Outside review 7's item 7 is narrowed to research copies and the full edition ([reviews L413](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L413)).

### 4.4 The two judges

- **The scoring judge** is outside the council, blind to its setup, size and models, and from a family that isn't on it. **The council's judge** is a seat that merges findings, keeps or dismisses them and sets severity ([plan L35](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L35)).
- **The scoring judge sees the keys,** and doesn't shape councils ([plan L850](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L850)).
- **Its family and model:** see the G3 slot in section 6.

### 4.5 Who is seed-aware

- **Seed-aware:** the chat assistant and the seed pilot session. They may record, build seeds and score, and never edit the briefs, the council set-up or the choice of material ([plan L848](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L848)).
  - **The notes session** is listed there as seed-aware, but has been treated as seed-free since 16 Nov (the amendment on the same line).
- **Seed-free:** the seat-roles session and every session that runs a council. They never see the seeds folder, the keys or the candidate list ([plan L849](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L849)).
- **Chat replies:** the seed-free rule covers seed-aware sessions' chat replies as well as their reports ([plan L938](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L938)).

## 5. Procedure and run rules

- **Sessions:** one fresh session per review in the formal runs, with the canary and environment checks once per batch, a launch file per review and each session's ID recorded ([plan L1251](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1251)). This follows "Fresh start per run" ([plan L51](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L51)).
- **Isolation:**
  - **The dry run's set-up:** `--setting-sources project,local`, a separate plugin cache, `ENABLE_CLAUDEAI_MCP_SERVERS=false`, and denies on web tools, shells and outside reads ([plan L872](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L872)).
  - **Outside review 7's items 1, 2 and 7,** adopted with conditions: cross-session messaging refused, agent teams off with the local settings file checked, and the read-only seat definitions ([reviews L374](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L374), [reviews L381](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L381)).
  - **Run folders:** given neutral names ([plan L939](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L939)).
  - **Hard limits:** no changes outside the sandbox or project folder ([plan L212](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L212)).
- **Messaging,** decision (b):
  - **Deviation:** any messaging call.
  - **Void:** any delivered message, except a subagent's hand-back and, in the team arm only, team-internal messages.
  - **Logged, not void:** refused deliveries ([plan L1246](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1246)).
- **Records:**
  - every run record states the version and setting it used ([reviews L543](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L543));
  - subagent transcripts and workflow results are copied into each run record, with `cleanupPeriodDays` set in every run folder ([reviews L391](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L391));
  - prices are rechecked the week before the first run and recorded ([sheet L111](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L111)).
- **Voids and deviations:**
  - the transcript scan's BREACH voids runs ([plan L1043](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1043));
  - the messaging rule above;
  - interrupted runs below.
  - Outside review 10's G7 notes these rules are spread out ([reviews L856](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L856)).
- **Interrupted runs,** decision (d): a run counts as one only after a technical interruption, with at most one relaunch. A stop by me after seeing output, a second relaunch or any change to the script or its arguments voids it ([plan L1257](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1257)).

> **Decision pending (outside review 1, C4: [reviews L50](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L50); outside review 10, G9: [reviews L858](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L858)):** the Claude Code version to pin for the formal runs. The sources give:
> - pinning matters, because team behaviour changes between versions ([reviews L460](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L460));
> - npm's `stable` channel (2.1.311) is an option ([reviews L461](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L461));
> - the runs so far used 2.1.325, and the Ultrareview runs 2.1.326 ([plan L1087](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1087)).

> **Decision pending (outside review 10, G4: [reviews L853](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L853)):** the numbers the plan relies on but doesn't give. The sources give:
> - **Caps:** listed with no values ([plan L209](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L209)). Outside review 1 says "the caps are mentioned but not given numbers" ([reviews L51](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L51)). "The pilot's caps" are named but never defined ([plan L1541](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1541)).
> - **Repeats:** "several times" ([plan L27](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L27)), against decision 6's 3 runs each for the final comparison ([decision 6 L253](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L253)). Repeats per role set are still open (G5 above).
> - **Variants per generation:** "a few" ([plan L39](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L39)), against decision 6's 3 ([decision 6 L248](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L248)).
> - **Sizes and tiers:** the default small run is "about 3 reviewers × 3 generations" ([plan L1449](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1449)). The complexity tiers aren't defined ([plan L1549](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1549)).

## 6. Measures and scoring

- **Catch:** see the G2 slot below.
- **Close call:** a flag within 3 lines of a planted range that describes a different problem, used in every report since 19 Nov. It isn't counted as a catch ([plan L1279](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1279)).
- **Extra:** an unconfirmed extra finding, matching neither a planted seed nor a known bug. From now, extras are reported in three groups (real, false or unchecked) from a hand-checked sample ([plan L1241](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1241)). On the easy tier, all 20 sampled extras were real problems ([plan L901](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L901)).
- **Known, not planted:** real bugs from the sources in the same files, kept in the keys so a council isn't scored down for finding them. A flag on one that overlaps a planted range counts as finding the seed ([plan L864](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L864)).
- **Headline precision:** count only planted bugs, and also report a second figure that credits real bugs nobody planted ([sheet L89](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L89)).
- **Rank-first and extras per catch:** main measures from 19 Nov, alongside catches, scored after the judge where there is one ([plan L1239](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1239)).
  - **A caveat:** rank follows severity, since reviewer lists are sorted by it ([plan L1016](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1016)).
- **Severity:** serious and critical findings are scored separately, as counts ([plan L24](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L24)). Who rates severity: see the C12 fix ([plan L367](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L367)).
- **Cost:**
  - an efficiency score of tokens, agents and time, with cost in money as well as tokens ([plan L25](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L25));
  - input, cache-read, cache-write and output tokens recorded separately, from outside review 7's item 6, adopted ([reviews L409](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L409));
  - the token figures reported so far are context sizes, not cost ([plan L1586](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1586)).
- **Hand-check samples:**
  - **The easy tier:** a stratified 15 of its matches, which found no errors, and 20 extras, all done ([plan L898](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L898)).
  - **Still to mark:** the hard tier's 15 matches and 20 extras, and all 21 Ultrareview findings ([plan L1284](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1284)).
  - **The labeller:** the hand labels are mine alone, "as one non-specialist" ([plan L900](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L900)).
- **Bands:** 9 or 10 caught of 10 means too easy ([plan L894](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L894)). The rank figures were read against "the 20 to 80% band", which was a new use, chosen after seeing them ([plan L1033](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1033)).

> **Decision pending (outside review 10, G2: [reviews L851](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L851)):** what counts as a catch. The pieces in the sources:
> - flags in a planted range that overlap a known bug count for the seed ([plan L864](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L864));
> - a flag within 3 lines that describes a different problem is a close call, not a catch (above);
> - "score on bugs covered, not findings" ([plan L339](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L339));
> - the hard tier counted flags describing the seed's defect with a different consequence, and bundled findings that included it, as catches ([plan L954](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L954)).
> - **Not stated:** the line tolerance, whether the mechanism must match, one finding covering two seeds, and whether catches are per reviewer or pooled. Outside review 8's idea 7, pending, asks for a near-miss rule fixed in advance ([reviews L582](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L582)).

> **Decision pending (outside review 10, G3: [reviews L852](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L852)):** who scores the formal runs. The sources give:
> - **2 Nov:** OpenAI stays off every council and acts as the judge ([sheet L15](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L15)). GPT-6.1 Sol is pinned at high effort, and DeepSeek V4 Pro re-judges 10–20% of findings ([sheet L26](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L26)).
> - **2 Nov, the check:** about 50 findings labelled by me before the first run, with at least 90% agreement with the judge required ([sheet L100](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L100)). On 12 Nov the hand-check against the scoring judge was adopted again ([reviews L172](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L172)).
> - **In practice so far:** Claude did the matching ([plan L1103](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1103)). Council Dial runs only Claude subagents ([plan L1336](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1336)), and the cross-family relay is "plan only, nothing built" ([plan L1541](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1541)).
> - **Not stated:** how the scoring judge is reached, and what happens if agreement falls below the bar.

> **Decision pending (outside review 1, B1: [reviews L36](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L36)):** the cost measure that defines "equal cost". Outside review 7's item 6 was adopted to settle B1 with it ([reviews L409](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L409)), but no measure is recorded. Outside review 1's D5 suggests validating reported tokens against summed request tokens and dollar cost ([reviews L59](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L59)).

> **Decision pending (outside review 10, C14: [reviews L838](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L838)):** how critical seeds are counted. The sources disagree:
> - "about 12 critical seeds per app ... ("caught 9 of 12")" ([plan L24](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L24));
> - decision 6's example is "caught 3 of 4 critical" ([decision 6 L247](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L247));
> - outside review 1 counts "about 4 critical seeds per app in the held-out set" ([reviews L43](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L43)).

> **Decision pending (outside review 10, G7: [reviews L856](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L856)):** what happens after the next difficulty check: how many more material designs to try, and what to do if it's too easy again or lands near zero.

## 7. Analysis

- **The keep rule:** a generation advances only if a 90% confidence interval for its score minus its parent's, computed on the same seeds, lies above zero ([plan L21](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L21)). Decision 6, adopted 2 Nov, specifies a paired bootstrap or McNemar-based interval on recall, with an optional precision guard ([decision 6 L248](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L248), [sheet L73](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L73)).
  - **Prior art:** SGM ([prior L688](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L688)).
  - **Pending ideas:** an error budget across generations, outside review 8's idea 30 ([reviews L656](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L656)), and outside review 1's B2 and B3, on run-to-run variance and choosing the best of several variants ([reviews L37](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L37), [reviews L38](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L38)).
- **Stopping:** two generations in a row with no advance, or at the caps ([plan L41](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L41), [decision 6 L251](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L251)).
- **Power:** decision 6 estimates what the search and the final comparison can detect ([decision 6 L257](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L257)). Outside review 1's B8 asks for a power check on the held-out set ([reviews L43](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L43)).
- **The final comparison:** one winner against one comparator, chosen in advance with no best-of-k selection ([decision 6 L199](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L199)), run 3 times each on the held-out seeds, pooled across apps and reported per app ([decision 6 L252](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L252)).
- **What can't be resolved,** as decision 6 says to state it in the plan: the search can reliably find gains of about 20 points within one app, the pooled final comparison about 10, and differences of about 5 points can't be resolved ([decision 6 L257](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L257)). Those figures assume decision 6's seed design, which the C2 slot puts in question.

> **Decision pending (outside review 10, G1: [reviews L850](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L850)):** which score the keep rule's interval is computed on. The sources give:
> - catches, misses, false flags and severity ([plan L19](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L19)), with false alarms counting against a council ([plan L23](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L23));
> - recall, with an optional precision guard ([decision 6 L248](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L248));
> - rank-first and extras per catch as main measures since 19 Nov (section 6).

> **Decision pending (outside review 10, C4: [reviews L825](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L825)):** how the winner is picked and how held-out seeds are used. The sources disagree:
> - "Winner: the generation that scored best on the held-out tests" ([plan L42](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L42)), which is a selection made on the held-out set;
> - decision 6's final comparison is chosen in advance, with no best-of-k selection, and reports "the winner's held-out score" ([decision 6 L256](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L256));
> - prior describes the keep rule as using held-out seeds ([prior L507](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L507)), while the plan says "computed on the same seeds";
> - outside review 1's B3 and outside review 8's idea 27, both pending, bear on it ([reviews L650](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L650)).

> **Decision pending (outside review 10, C5: [reviews L826](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L826)):** the definition of the optimum council size. The sources disagree:
> - "the point where adding more reviewers stops improving results" ([plan L11](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L11));
> - "the point where one more reviewer costs more tokens than the quality it adds" ([plan L44](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L44)), which needs an exchange rate between tokens and quality that isn't given.

## 8. Pilot and exploratory results

"Pilot-only" means the sources say so. Where they don't say, it's marked "not stated", and the C3 slot above applies.

| Date | Result | Status | Source |
|---|---|---|---|
| 30 Oct (the write-up's date) | WinScope: review rounds found 97 problems the builders' tests had passed. One app, one run, no repeats | informal pilot | [plan L188](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L188), [winscope-pilot.md](winscope-pilot.md) |
| 7 Nov | First Council Dial runs: the judge dismissed planted bug #7, and the appeal was added | not stated | [plan L334](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L334) |
| 7 Nov | A subagent's effort follows its model's default unless set | measured | [plan L1510](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1510) |
| 8 Nov | Two identical Lite runs differed, so one run per configuration isn't enough | field example | [plan L28](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L28) |
| 8 Nov | Appeal stress test: three scored runs on the `shelfkeep` material | not stated | [plan L343](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L343) |
| 8–9 Nov | Direct appeal trials: 161 of 162 wrongful dismissals caught. Severity changes 92 of 108 (85%) with R4's key corrected. All Claude-written | not stated | [plan L360](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L360), [plan L361](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L361) |
| 8 Nov | The voice-tag controlled test | controlled test | [plan L1604](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1604) |
| 9 Nov | Context anchoring: three reviews with different context | "not a controlled test" | [plan L567](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L567) |
| 13 Nov | The run-isolation dry run: all checks passed, on made-up material | dry run | [plan L875](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L875) |
| 14 Nov | Review A, the easy tier: 10 of 10 caught, single reviewers 25 of 30, 182 findings with 94 extras. Too easy | pilot-only | [plan L894](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L894) |
| 15 Nov | The extras sample: all 20 real | pilot-only | [plan L900](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L900) |
| 15 Nov | Review B, the hard tier: 10 of 10 caught, 29 of 30, 272 findings with 238 extras. Too easy | pilot-only | [plan L948](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L948) |
| 16 Nov | Material size: the material is a small slice of each project, and the diff points at the seed | pilot-only | [plan L958](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L958) |
| 16 Nov | Messaging check: no message carried content between sessions or seats in the runs | check | [plan L1058](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1058) |
| 17 Nov | Rank rescore: the seed was 1st in 17 of 29 catches and in the top 3 in 25. Extras per catch 8.2. The human reviews had a median of 2 submissions | exploratory, "not in the plan" | [plan L1025](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1025) |
| 17 Nov | Ultrareview: 2 of 3 caught against Lite Quick's 3 of 3, plus a rerun row | exploratory, n=3, no inference | [plan L1107](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1107) |
| 14–18 Nov | The email app's reviews, and the 0.5.3 council review with its fix passes | field cases | [plan L1722](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1722), [plan L1746](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1746) |
| 19 Nov | Close calls under one definition: easy 29, Ultrareview 8, hard 43. No catch changes | pilot-only | [plan L1280](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1280) |

## 9. Decisions log

| Date | Decision | Where it's recorded | What it replaced |
|---|---|---|---|
| 2 Nov | OpenAI judges and stays off every council. GPT-6.1 Sol pinned, with DeepSeek re-judging | [sheet L15](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L15) | — |
| 2 Nov | Whole codebase by default, with diff as an arm | [sheet L37](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L37) | — (see the C2 slot) |
| 2 Nov | Mistral writes the model-written seeds, and pilot bugs are replayed | [sheet L60](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L60) | — (see the C2 slot) |
| 2 Nov | Decision 6's option C: 120 seeds per app, the paired-CI advance rule, the stop rule and calibration first | [sheet L73](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L73) | "two generations under about 2%" ([decision 6 L251](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L251)) |
| 2 Nov | Headline precision counts only planted bugs, plus a second figure | [sheet L89](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L89) | — |
| 2 Nov | About 50 hand labels, with at least 90% agreement with the judge | [sheet L100](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L100) | — |
| 2 Nov | Prices rechecked the week before the first run | [sheet L111](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L111) | — |
| 8 Nov | I don't rate severity for the stress-test key. Narrowed to that key on 19 Nov | [plan L367](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L367) | — |
| 12 Nov | Outside reviews go in outside-reviews.md, and the plan is locked before the formal experiment | [plan L777](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L777) | — |
| 12 Nov | Paper format: LaTeX, ICML style, an arXiv preprint | [plan L1795](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1795) | — |
| 12 Nov | Paper edits parked. Out of parking on 19 Nov, as a research paper | [plan L813](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L813) | parking (19 Nov) |
| 12 Nov | Seeds: real bugs first, the order of preference by source, equal numbers per area, checks before ReviewBench | [reviews L110](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L110) | 2 Nov seed writing, in part (see the C2 slot) |
| 12 Nov | Seat roles: the ISO map, Lite's areas, role sets A, B, C and the generalist | [reviews L135](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L135) | — |
| 12 Nov | Outside review 3: a pooled single-reviewer baseline, the judge checked against hand labels, the focus | [reviews L198](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L198) | — |
| 13 Nov | Who sees the seeds; seed-aware and seed-free sessions; pilot seeds pilot-only | [plan L847](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L847) | "The chat assistant doesn't see the seeds" |
| 13 Nov | A′, and policy in B, C and G; four A′ decisions; the out-of-scope rule kept | [reviews L267](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L267) | — |
| 13 Nov | Outside review 5: the source plan, private seeds, a pilot first | [reviews L353](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L353) | — |
| 15 Nov | Generated files left out of seed material | [plan L928](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L928) | — |
| 15 Nov | A neutral run folder name | [plan L939](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L939) | — |
| 16 Nov | The debate council as an agent team (outside review 7's item 8) | [reviews L463](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L463) | — |
| 16 Nov | The workflow edition comparison (item 11), and the record rule (item 12) | [reviews L492](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L492) | — |
| 16 Nov | Future seeds favour post-cutoff fixes, as a precaution | [plan L974](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L974) | its first wording, the same day |
| 17 Nov | Rank-first, if adopted, is fixed before the formal runs | [plan L1015](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1015) | — |
| 19 Nov | Decisions (a) to (g) | [plan L1237](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1237) | the proposed messaging rule ((b)), item 5's run rule ((d)) |
| 19 Nov | Outside review 7: items 1–4, 6 and 10 adopted, 5 with (d), 7 narrowed, 9 parked | [reviews L547](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L547) | — |
| 19 Nov | Outside review 10's 22 clerical fixes, and S1–S10 addressed by this document | [reviews L781](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L781) | — |

**Deviations and post-hoc exceptions:**
- **The hard-tier scan exception:** BREACH on 2 calls, accepted as an exception before scoring. "The CLEAN verdict comes from a rule written after the calls it judges" ([plan L1040](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1040)).
- **Both difficulty checks** ran all their reviews in one session, a departure from "Fresh start per run" ([plan L1252](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1252)).
- **The first difficulty check's folder name** contained "difficulty" ([plan L941](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L941)).
- **Rank:** the bands were applied to rank after seeing the figures (section 6).
- **Ultrareview run 2** reviewed every file whole, because it was launched with another repository's base hash. It's scored and flagged ([plan L1122](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1122)).
- **The rerun is an extra row,** with the withdrawn replacement and its timing ([plan L1198](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1198)).
- **Decisions overtaken but still marked pending:** outside review 10's G8 lists these ([reviews L857](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L857)).

## 10. Threats and limits

- **What reaches an agent:** connector instructions, instruction files, labels and folder names reach agents outside the council's control ([plan L97](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L97), [plan L55](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L55)).
- **One family:**
  - Claude wrote the stress-test material, its key, the judge reasons and the scoring, and every appeal was Claude ([plan L376](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L376));
  - so far there's no non-Claude seat ([plan L1336](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1336));
  - ReviewBench's producers split 14 Claude to 8 GPT-5.5 ([plan L831](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L831)).
- **Contamination:**
  - the post-cutoff precaution "doesn't guard against knowing the project" ([plan L975](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L975));
  - for several hard-tier changes, a model may have seen the code ([plan L936](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L936)).
- **Material too easy:** both tiers saturated ([plan L948](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L948)).
- **One rater:** hand labels by one non-specialist (section 6).
- **Small n:** the Ultrareview baseline is n=3 with no inference (section 8). The hard tier is "a pilot of 10" ([plan L936](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L936)).
- **Version drift:** the Lite runs used 2.1.325 and Ultrareview 2.1.326 ([plan L1102](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1102)).
- **The human relay:** five recorded relay slips of seed detail ([plan L1056](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1056)).
- **The post-hoc scan exception** (section 9).

## 11. Related work

The full survey is in [prior-work-research.md](prior-work-research.md). Its "How new is this?" table ([prior L670](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L670)) and the notes after the 17 Nov sweep ([prior L699](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L699)) say this:

- **Councils with a judge** are well studied, and also a shipped product shape, so the contribution is the measurement, not the architecture ([prior L703](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L703)).
- **Equal cost:** *The More the Better?* is the prior test of the specialist-against-generalist question at equal cost, in document review. The project's result is to be framed as the code-review test of it ([prior L702](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L702)).
- **Scoring against known or planted bugs** has prior work (CRBugBench, CR-Bench, SWR-Bench, MCR-Bench, SecPRBench), for single reviewers ([prior L679](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L679)).
- **The appeal** still looks new within code review only. Klieber et al. is a static-analysis counter-example ([prior L685](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L685)).
- **Same-family blind spots** have close prior answers (Song 2026, CyberDual) ([prior L689](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L689)).
- **Evolving configurations:** MemCo, the Red Queen Gödel Machine and MetaVul come close, and SGM is prior art for the keep rule ([prior L704](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L704), [prior L705](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L705)).
- **What still looks new:** the appeal within code review, the severity-calibration check, the equal-cost role-set comparison on code and racing whole review councils ([prior L700](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L700)). Which of these the plan claims is the C8 slot in section 2.

## 12. Open questions and the ideas backlog

| Item | Source | Status |
|---|---|---|
| Should the main session stay blind to the material? | [plan L58](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L58) | open |
| The appeal experiment, judged with against without | [plan L330](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L330) | planned, not run. Outside review 9's item 12 calls it the minimum before submission ([reviews L749](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L749)) |
| The xargs case as a test family | [plan L317](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L317) | planned, not run, not next |
| Cross-family judges and appealers | [plan L1322](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1322) | planned, not next |
| Fable as judge or analyser | [plan L1338](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1338) | to test |
| Who owns severity | [plan L1344](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1344) | to test |
| Does the source of a rating sway agreement? | [plan L1354](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1354) | to test |
| The command appealer | [plan L1356](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1356) | planned (the findings appealer exists in effect) |
| What reaches the user | [plan L1363](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1363) | planned |
| A default checklist in reviewer briefs | [plan L1369](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1369) | leaning, not decided. Outside review 10's G8 notes A′ tests it |
| Harder stress-test material, version 2 | [plan L353](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L353) | planned |
| Effort levels: a test round, per-role effort | [plan L1534](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1534) | to test |
| Mixed model strengths across roles | [plan L1709](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1709) | to test |
| A weaker reviewer's unique catches | [plan L1760](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1760) | to test |
| Dynamic councils, and template tuning | [plan L1703](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1703) | planned, not run |
| Council size by task complexity | [plan L1545](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1545) | planned |
| The Horizon case; re-reviewing plugin updates | [plan L1679](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1679), [plan L1688](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1688) | ideas, not planned |
| A code-only council against one with live read access (the Cloudflare case) | [plan L1425](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1425) | not adopted |
| The "Experiment idea" bullets in the notebook, 18 of them, for example on the check agent, context anchoring and the plan-check stage | [plan L413](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L413) and after | ideas |
| Outside review 1's 24 items (A1 to D7) and its list for locking the plan | [reviews L80](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L80) | pending |
| Outside review 8's 35 ideas | [reviews L688](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L688) | all pending |
| Outside review 9's 16 suggestions on the paper | [reviews L777](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L777) | all pending |
| Outside review 10's remaining findings | [reviews L900](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L900) | C2–C5, C7, C8, C11, C14 and G1–G12 pending |
| The `CLAUDE.md` test's misleading file, and who can write it without seeing the seeds | [reviews L859](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L859) | pending |
| The evidence behind "real bugs are the main seeds" | [reviews L860](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L860) | pending |

> **Decision pending (outside review 10, G10: [reviews L859](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L859)):** how the `CLAUDE.md` test's misleading file is written. The brief's design targets "a seeded bug's pattern" ([briefs L209](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/decisions-pending-2026-11-17.md?plain=1#L209)), but "seed-free sessions design the files" ([plan L1267](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1267)), and those sessions never see the seeds.

## 13. Publishing and deliverables

- **Deliverables:** the calculator's repo and README, a write-up or preprint, the raw run logs, the who-caught-what log and the explainer video ([plan L1785](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1785)).
- **The paper:**
  - LaTeX in ICML style, posted as an arXiv preprint ([plan L1795](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1795));
  - out of parking since 19 Nov, as a research paper that leads with its experiments, because arXiv cs takes review and position papers only after peer review ([plan L814](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L814));
  - the parked fixes still apply ([plan L813](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L813));
  - outside review 9's 16 suggestions are pending (section 12).
- **The route:** a personal endorsement, a research paper rather than a position paper, arXiv's submission limits, and every reference checked ([plan L1810](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1810)).

> **Decision pending (the notebook's paper route: [plan L1802](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1802)):** the arXiv primary category, and so the endorsement domain. The paper session recommended cs.MA with cs.SE as a cross-list.

> **Decision pending (outside review 10, C11: [reviews L835](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L835)):** the cost estimate and the order of work. The sources disagree:
> - "Each small run costs about half a session" and "The total is roughly 3–4 sessions" ([plan L1574](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1574)), with an order of work that starts with "Run small app #1" ([plan L1764](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1764));
> - decision 6: "about 150M tokens per app per evolving run, about $800 to $1,300 at API rates", and "about 360 checked seeds across three apps" ([decision 6 L267](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L267)).
> - **Missing from the order of work:** the seeds, the calibration run, the plan lock and the role-set comparison. It ends with a review by "Fable 5.1", which is still to choose ([plan L1767](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1767)).

---

Built on 19 Nov 2026 by Claude Code, from the sources above only.
