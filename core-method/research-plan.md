# Research plan

The research plan for evolving review councils, as its own document. The notebook, [experiment-plan.md](experiment-plan.md), stays the dated record of how the plan was reached.

- **How it was built (19 Nov 2026):** only from what the notebook, [outside-reviews.md](outside-reviews.md), [prior-work-research.md](prior-work-research.md) and the decision files already say. Nothing new is decided here.
- **Its source:** this follows the structure outside review 10 proposed ([reviews L818](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L818)).
- **Links:** each point links to its source lines at commit `87eb410`, so the links don't move when the notebook changes. "plan" is the notebook, "reviews" is outside-reviews.md, "prior" is prior-work-research.md, "briefs" is [decisions-pending-2026-11-17.md](decisions-pending-2026-11-17.md), "sheet" is [the 2 Nov decisions sheet](../research/decisions-seeded-bugs-and-judge.md) and "decision 6" is [decision-6-seeds-and-stopping.md](../research/decision-6-seeds-and-stopping.md).
- **What isn't decided:** each such point is a marked **Decision pending** slot. It says what has to be decided, and points to its finding in outside review 10 or elsewhere. Where sources disagree, the slot lists both and picks neither. (amended 19 Nov 2026: every slot is now filled by my decisions of 19 Nov, and the earlier sources are kept under each.) (amended again 19 Nov 2026: one new slot is open, G12's power part, in section 7.) (amended a third time 19 Nov 2026: it's filled. No slot is open.)
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
  - five more on 19 Nov: C3, C4, G1, G2 and G3, recorded in their slots below;
  - more on 19 Nov: C4's and B1's open parts, C7, G8, G9, G11 and G12's answer list, with G12's power part pending;
  - and last on 19 Nov: G12's power part (15 seeds per area, 3 repeats), H9's omnibus test, separate held-out seeds for evolution and idea 11 dropped;
  - on 20 Nov, from the seed supply report: the 7 seed areas, a severity mix that follows the supply, one seed per pull request or CVE project, the evolution search on the core 105 with a fresh held-out 105, a post-cutoff preference for held-out seeds, the area threat and a performance fallback;
  - fourteen more on 19 Nov, filling every remaining slot: C8, S3, G5, G6, C2, the version pin, G4, the cost measure, C14, G7, C5, G10, the arXiv category and C11, plus G2's counting rules;
  - the seven 19 Nov decisions, (a) to (g) ([plan L1237](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1237));
  - the 2 Nov decisions on seeds and the judge ([sheet L3](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L3));
  - the 12–13 Nov decisions on seed sources, seat roles and who sees the seeds ([reviews L110](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L110), [plan L835](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L835)).
  - Section 9 lists them all.
- **What's next,** in order:
  1. I mark the three hand-check packs ([plan L1275](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1275));
  2. decision (a)'s difficulty check, on "no diff, plus surrounding modules", with bands fixed first ([plan L1243](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1243));
  3. a dry run of Lite under the `SendMessage` deny ([plan L1250](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1250)).
- **Before the first formal run** (a checklist, adopted by the researcher, 19 Nov 2026, outside review 10's G9):
  - [ ] the three hand-check packs marked (15, 20 and 21 items);
  - [ ] a short dry run confirming Lite completes under the `SendMessage` deny;
  - [ ] the run folder's local settings file checked, since local settings can turn agent teams back on;
  - [ ] one scan test with a delivered message, in a throwaway pair of sessions;
  - [ ] whether directory-installed plugins reach Lite's reviewer agents, "still to check" in the notebook;
  - [ ] the route to the scoring judge (GPT-6.1 Sol, with DeepSeek re-judging) built, and checked against at least 50 hand labels;
  - [ ] the caps set after one measured dry run (G4);
  - [ ] the Claude Code version pinned from npm's `stable` channel on the day the plan is locked, with full model IDs.
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

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, C8: [reviews L829](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L829)):** which list of "what's new" the plan states. Before it, the sources disagreed:
> - **The decision:** one list of what's new.
>   1. the appeal, the main contribution, worded for code review only;
>   2. role sets at equal cost against planted bugs;
>   3. evolving whole review councils with a pre-registered keep rule, crediting SGM as prior art;
>   4. checking the judge's severity calls against hand labels.
> - The `CLAUDE.md` test is secondary. The framing is that the contribution is the measurement, not the design.
> - **Aligned the same day:** the notebook's Goals and its "This experiment adds" line, and prior's novelty summaries, all as dated amendments.
> - the plan's Related research names "evolving councils for code review, a council-size scale for each complexity tier, and a calculator" ([plan L1815](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1815)), but the calculator isn't built ([plan L1701](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1701));
> - outside review 3's focus, adopted 12 Nov, names the appeal, role sets at equal cost, the judge's severity calls checked against a key, and evolving or racing councils ([reviews L185](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L185));
> - prior's novelty summary names the appeal within code review, severity calibration, the equal-cost role-set comparison on code and racing councils, and says the contribution is "the measurement, not the architecture" ([prior L700](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L700), [prior L703](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L703)).

## 3. Hypotheses

The sources state these as hypotheses or ideas to test. ~~None is marked confirmatory or exploratory.~~ (amended 19 Nov 2026: by decision S3, H8 and H9 are confirmatory, and H1 to H7 are exploratory.)

| # | Hypothesis | Source | As the source labels it |
|---|---|---|---|
| H1 | A council of different strong models covers each other's blind spots, and beats one model and copies of it | [plan L1465](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1465) | "core hypothesis" |
| H2 | For review, a reviewer without the author's context beats a smarter model checking its own work | [plan L1472](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1472) | hypothesis, tested at the same cost |
| H3 | More effort isn't always better: a judge or appeal on xhigh could make more wrong rulings than one on medium | [plan L1535](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1535) | hypothesis |
| H4 | Background anchors a reviewer on the author's framing, and less context lets it explore more widely | [plan L637](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L637) | hypothesis |
| H5 | Fable may make a stronger judge or analyser | [plan L1338](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1338) | hypothesis, to test |
| H6 | Families may share blind spots inherited from common roots, so a different family buys less independence than assumed | [plan L1335](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1335) | idea, to test |
| H7 | A misleading `CLAUDE.md` lowers catches (the bias side, tested first) | [plan L1263](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1263) | design of decision (e) |
| H8 | The appeal recovers real bugs the judge dismissed, without adding many false ones. Null (adopted by the researcher, 19 Nov 2026): the appeal recovers no more real bugs than the judge alone. "Many false ones" means extras per catch rising by more than G1's 20% guard | decision S3, 19 Nov 2026 (research question 3) | **confirmatory** |
| H9 | Role sets differ in catch rate at equal cost. Null (adopted by the researcher, 19 Nov 2026): every role set has the same catch rate at equal cost. Test (adopted by the researcher, 19 Nov 2026): one omnibus mixed-effects logistic regression across all five sets, likelihood ratio at alpha 0.05, with Holm-corrected pairwise follow-ups | decision S3, 19 Nov 2026 (research question 2) | **confirmatory** |

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, S3: [reviews L810](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L810)):** which hypotheses are confirmatory and which exploratory, and the null hypothesis for each confirmatory one. Prior's reading of *The More the Better?* as "the project's null hypothesis" for the role-set question bears on this ([prior L211](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L211)).
> - **The decision:** two confirmatory hypotheses, H8 and H9 in the table above. H8 is that the appeal recovers real bugs the judge dismissed without adding many false ones. H9 is that role sets differ in catch rate at equal cost. All the others, H1 to H7, are exploratory.
> - ~~**Still to fix in the locked plan** *(Claude Code's note)*: the null hypothesis for each, and what "many false ones" means in numbers.~~ (amended 19 Nov 2026: both adopted by the researcher, 19 Nov 2026, in the table above. H8's null is that the appeal recovers no more real bugs than the judge alone, and "many false ones" means extras per catch rising by more than G1's 20% guard. H9's null is that every role set has the same catch rate at equal cost.)

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

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, G5: [reviews L854](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L854)):** the role-set comparison's design, which has no section of its own. That means its seed count, repeats, cost matching, scoring and analysis. Its parts are spread over the outside reviews and a private plan ([reviews L135](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L135)), and "the number of repeats per role set" is still open ([reviews L156](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L156)).
> - **The decision:** the core comparison is role sets A, A′, B, C and the generalist, at equal cost. The debate arms and the workflow edition are secondary experiments, run afterwards.

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, G6: [reviews L855](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L855)):** how the role-set comparison and the evolution experiment relate. Do they run in sequence, and does one locked plan cover both? Seat roles are to be "settled, researched and tested before the plan is locked" ([reviews L104](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L104)).
> - **The decision:** one locked plan covers both experiments. The role-set comparison runs first, and its winning set becomes the starting council for evolution.

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

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, C2: [reviews L823](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L823)):** the seed design for the formal runs. Before it, the sources disagreed:
> - **The decision:** the main seeds are real bugs from public pull-request datasets, or traced back to the pull requests that introduced them (wording adopted by the researcher, 19 Nov 2026, so it covers the hard tier's SWE-bench-Live and CVE seeds), at three severity levels, in equal numbers per review area. The material is shaped by decision (a): no diff, plus the surrounding modules. Model-written seeds are an extra only, written by Mistral, not Claude.
> - **What it retires:** the "120 per app, four-level mix, WinScope first" line in the notebook, struck through there the same day. The seed count per area isn't set by this decision.
> - **The 7 seed areas (recorded 20 Nov 2026):** correctness, reliability, performance efficiency, security and privacy, the app's own tests, clear-cut maintainability and docs. Safety counts under security and privacy, and policy under docs, as the seed folder's counts-only supply report (`reports\seed-supply-2026-11-20.md`), checked by Claude Code did. The role-set design names nine areas, with safety and policy separate, but kept separate both would be very short: the pilot found 1 seed each.
> - **Severity mix, adopted by the researcher, 20 Nov 2026:** each area has 15 core seeds, and the severities follow the supply rather than an even split. Each area's HIGH, MED and LOW counts are recorded.
> - **Independence, adopted by the researcher, 20 Nov 2026:** at most one seed per pull request, and for CVEs one per project, so seeds are independent as the power check assumes. *(Claude Code's note: by the supply report, that cuts the pool from about 1,700 usable candidates to about 700, still well over 105 core plus 105 held-out.)*
> - **Performance fallback, adopted by the researcher, 20 Nov 2026:** if performance efficiency can't fill 15 core plus 15 held-out under the one-per-pull-request rule, performance-fix commits are traced back with SZZ in the projects already cloned. If it's still short, use what exists and record the shortfall. *(Claude Code's note: the supply report estimates about 45 (25 to 55) performance candidates in all, and about 30 (10 to 40) after 15 core seeds, so the fallback may well be needed. Performance HIGH is about 4 (2 to 6).)*
> - **2 Nov:** 120 seeds per app (80 search, 40 held out), a 10/20/40/30% critical/high/medium/low mix and one clean variant per app, starting with WinScope ([plan L20](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L20), [sheet L74](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L74)). Mistral writes the model-written seeds, and the pilot's real bugs are replayed ([sheet L60](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L60), [sheet L48](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L48)).
> - **12–13 Nov:** real bugs are the main seeds ([reviews L112](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L112)), in equal numbers per area to start ([reviews L127](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L127)). They come from other projects' pull requests, rated HIGH, MED or LOW ([plan L855](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L855)).
> - **What reviewers see:** the 2 Nov decision is "whole codebase by default, with diff as a comparison arm" ([sheet L37](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L37)). The pilot material holds the diff, and the next check drops it (above).

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, C3: [reviews L824](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L824)):** whether the seed pilot's results go in the paper. Before it, the sources disagreed:
> - **The decision:** pilot results are reported in the paper as clearly labelled exploratory findings, never as tests of a hypothesis. Pilot seeds stay out of the formal comparison.
> - **What it changes:** the 13 Nov rule that the pilot seeds are "never reported as results" now allows them as labelled exploratory findings. Keeping them out of the formal comparison is unchanged.
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

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 1, C4: [reviews L50](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L50); outside review 10, G9: [reviews L858](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L858)):** the Claude Code version to pin for the formal runs. Before it, the sources gave:
> - **The decision:** every formal run uses one exact Claude Code version, the one on npm's `stable` channel on the day the plan is locked, with auto-updates off for run sessions only. Each run records its version.
> - **Model IDs, adopted by the researcher, 19 Nov 2026:** every formal run starts with the full model ID (for example `claude-opus-5-5`), never an alias, and records the model ID each transcript reports, for reviewers and the scoring judge alike.
> - *(Claude Code's note)*: transcripts do report it. Every assistant message carries a `model` field (checked in this notes session's transcript on 19 Nov). The scoring judge is GPT-6.1 Sol (G3), so its model ID will come from that route's own records once it's built, not from a Claude Code transcript.
> - pinning matters, because team behaviour changes between versions ([reviews L460](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L460));
> - npm's `stable` channel (2.1.311) is an option ([reviews L461](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L461));
> - the runs so far used 2.1.325, and the Ultrareview runs 2.1.326 ([plan L1087](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1087)).

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, G4: [reviews L853](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L853)):** the numbers the plan relies on but doesn't give. Before it, the sources gave:
> - **The decision:** decision 6's numbers are adopted: 3 variants per generation, 3 repeats per council in the final comparison, and the detectable difference stated as about 20 points within an app and 10 pooled. The caps, tokens and turns per run, are set after one measured dry run. That also stands in for "the pilot's caps".
> - **Still open** *(Claude Code's note)*: the repeats per role set in the core comparison, and the complexity tiers.
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

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, G2: [reviews L851](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L851)):** what counts as a catch. Before it, the sources gave these pieces:
> - **The decision:** a catch is a finding within 3 lines of the planted range whose description matches the planted problem. A finding in the right place with the wrong mechanism is a miss, logged as a close call. It's fixed before any formal run.
> - **What it settles:** the line tolerance and the mechanism question. It matches the close-call definition above, and answers outside review 8's idea 7 (a near-miss rule fixed in advance) for the formal runs.
> - ~~**Still not stated** *(Claude Code's note)*: one finding covering two seeds, merged findings, and per reviewer against pooled.~~
> - **Counting rules, adopted by the researcher, 19 Nov 2026:** a finding can catch only one seed, and if it fits two it counts for the one it describes best. Merged findings are scored as the judge merged them. The main catch rate counts the whole council's final output, with single-reviewer catches reported alongside.
> - flags in a planted range that overlap a known bug count for the seed ([plan L864](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L864));
> - a flag within 3 lines that describes a different problem is a close call, not a catch (above);
> - "score on bugs covered, not findings" ([plan L339](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L339));
> - the hard tier counted flags describing the seed's defect with a different consequence, and bundled findings that included it, as catches ([plan L954](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L954)).
> - **Not stated:** the line tolerance, whether the mechanism must match, one finding covering two seeds, and whether catches are per reviewer or pooled. Outside review 8's idea 7, pending, asks for a near-miss rule fixed in advance ([reviews L582](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L582)).

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, G3: [reviews L852](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L852)):** who scores the formal runs. Before it, the sources gave:
> - **The decision:** keep the 2 Nov choice. The scoring judge is from outside the Claude family: GPT-6.1 Sol, with DeepSeek V4 Pro re-judging, per the decisions sheet ([sheet L26](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L26)). It's checked against at least 50 of my hand labels, with 90% agreement as the pass mark and 95% as the target.
> - **An open task:** building the route to those models. Council Dial runs only Claude subagents, and the cross-family relay is plan only.
> - **What it changes** *(Claude Code's note)*: the 2 Nov sheet says "about 50" labels and "at least 90%" agreement ([sheet L100](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L100)). The decision makes it at least 50 labels, and adds the 95% target.
> - **2 Nov:** OpenAI stays off every council and acts as the judge ([sheet L15](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L15)). GPT-6.1 Sol is pinned at high effort, and DeepSeek V4 Pro re-judges 10–20% of findings ([sheet L26](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L26)).
> - **2 Nov, the check:** about 50 findings labelled by me before the first run, with at least 90% agreement with the judge required ([sheet L100](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L100)). On 12 Nov the hand-check against the scoring judge was adopted again ([reviews L172](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L172)).
> - **In practice so far:** Claude did the matching ([plan L1103](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1103)). Council Dial runs only Claude subagents ([plan L1336](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1336)), and the cross-family relay is "plan only, nothing built" ([plan L1541](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1541)).
> - **Not stated:** how the scoring judge is reached, and what happens if agreement falls below the bar.

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 1, B1: [reviews L36](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L36)):** the cost measure that defines "equal cost". Outside review 7's item 6 was adopted to settle B1 with it ([reviews L409](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L409)), but no measure is recorded. Outside review 1's D5 suggests validating reported tokens against summed request tokens and dollar cost ([reviews L59](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L59)).
> - **The decision:** input, cache-read, cache-write and output tokens are recorded separately. The headline cost is dollars at API rates, the same for every arm.
> - **Where the counts come from, adopted by the researcher, 19 Nov 2026:** from the run transcripts, summing each message's usage (input, cache read, cache write and output), subagent transcripts included, not Claude Code's per-agent figure.
> - **Checked** *(Claude Code's note)*: the transcripts do carry those fields. Each assistant entry has `input_tokens`, `cache_read_input_tokens`, `cache_creation_input_tokens` and `output_tokens`, and subagents have transcripts of their own. That was checked on 19 Nov in this notes session's own transcript and a subagent's, not a run transcript, which holds seed material.
> - **A catch** *(Claude Code's note)*: one API response is often logged as several entries with the same message ID and identical usage. In the transcript checked, 2,635 entries carried usage but only 1,204 message IDs were distinct. So the sum has to count each message ID once, or it overstates the tokens about twofold.

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, C14: [reviews L838](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L838)):** how critical seeds are counted. Before it, the sources disagreed:
> - **The decision:** drop "critical". HIGH seeds are reported as a separate line, with whatever count the material gives.
> - **With the supply, adopted by the researcher, 20 Nov 2026:** HIGH is reported as its own line in every area, with whatever count the supply gives. Severities follow the supply (see C2), so HIGH counts differ by area. The supply report estimates performance HIGH at about 4, against about 180 for correctness.
> - "about 12 critical seeds per app ... ("caught 9 of 12")" ([plan L24](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L24));
> - decision 6's example is "caught 3 of 4 critical" ([decision 6 L247](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L247));
> - outside review 1 counts "about 4 critical seeds per app in the held-out set" ([reviews L43](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L43)).

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, G7: [reviews L856](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L856)):** what happens after the next difficulty check: how many more material designs to try, and what to do if it's too easy again or lands near zero.
> - **The decision:** if the no-diff check lands at 20–80% catches, use the material. If it's too easy, add more of the surrounding project and try once more. If it's near zero, step back towards the diff, once. After that, use the best material and record the limitation.

## 7. Analysis

- **The keep rule:** a generation advances only if a 90% confidence interval for its score minus its parent's, computed on the same seeds, lies above zero ([plan L21](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L21)). Decision 6, adopted 2 Nov, specifies a paired bootstrap or McNemar-based interval on recall, with an optional precision guard ([decision 6 L248](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L248), [sheet L73](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decisions-seeded-bugs-and-judge.md?plain=1#L73)).
  - **Prior art:** SGM ([prior L688](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L688)).
  - **Pending ideas:** an error budget across generations, outside review 8's idea 30 ([reviews L656](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L656)), and outside review 1's B2 and B3, on run-to-run variance and choosing the best of several variants ([reviews L37](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L37), [reviews L38](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L38)).
- **Stopping:** two generations in a row with no advance, or at the caps ([plan L41](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L41), [decision 6 L251](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L251)).
- **Power:** decision 6 estimates what the search and the final comparison can detect ([decision 6 L257](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L257)). Outside review 1's B8 asks for a power check on the held-out set ([reviews L43](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L43)).
- **Held-out seeds, adopted by the researcher, 19 Nov 2026:** the evolution experiment's held-out seeds are separate from the core comparison's 105, with no overlap. (amended 20 Nov 2026: the evolution search reuses the core 105, and the held-out set is a fresh 105, 15 per area, preferring post-cutoff fixes where they exist. See the G12 slot.)
- **The final comparison:** one winner against one comparator, chosen in advance with no best-of-k selection ([decision 6 L199](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L199)), run 3 times each on the held-out seeds, pooled across apps and reported per app ([decision 6 L252](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L252)).
- **What can't be resolved,** as decision 6 says to state it in the plan: the search can reliably find gains of about 20 points within one app, the pooled final comparison about 10, and differences of about 5 points can't be resolved ([decision 6 L257](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L257)). Those figures assume decision 6's seed design, which the C2 slot puts in question.

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, G12, the power part):** the core comparison uses 15 seeds per review area, 105 in all, and 3 repeats per role set. Before it, the slot read: the seed count per area and the repeats per role set for the core comparison. A power check, run on 19 Nov 2026 by Claude Code, gives the smallest catch-rate difference between two role sets detectable at 80% power and a two-sided alpha of 0.05:
>
> | Seeds per area | Seeds in all (7 areas) | Repeats per role set | Detectable at a 50% catch rate | Detectable at an 83% catch rate | Council runs (5 role sets) |
> |---|---|---|---|---|---|
> | 10 | 70 | 1 | 22.5 points | 20.5 points | 350 |
> | 10 | 70 | 3 | 13.4 | 11.3 | 1,050 |
> | 10 | 70 | 5 | 10.5 | 8.6 | 1,750 |
> | 15 | 105 | 1 | 18.6 | 16.5 | 525 |
> | 15 | 105 | 3 | 11.0 | 9.1 | 1,575 |
> | 15 | 105 | 5 | 8.6 | 7.0 | 2,625 |
> | 20 | 140 | 1 | 16.3 | 14.1 | 700 |
> | 20 | 140 | 3 | 9.6 | 7.8 | 2,100 |
> | 20 | 140 | 5 | 7.4 | 6.0 | 3,500 |
> | 30 | 210 | 1 | 13.4 | 11.3 | 1,050 |
> | 30 | 210 | 3 | 7.8 | 6.3 | 3,150 |
> | 30 | 210 | 5 | 6.1 | 4.8 | 5,250 |
>
> - **The method:** a normal approximation for a paired comparison of two role sets on the same seeds, with each seed's catch rate averaged over its repeats. It was checked by simulation with seed-to-seed variation in difficulty, which gave 81% to 87% power at three of the cells, so the table is slightly conservative.
> - **The catch rates:** the pilot's councils caught 10 of 10 in both tiers, which leaves no variance to work from. So the table uses the single-reviewer rates of the easy tier (25 of 30, 83%) and 50%, the middle of the 20–80% band the next material aims for. At the hard tier's 97%, only differences of a few points are even possible.
> - **Assumptions:** repeats are independent given the seed; areas are pooled; one pairwise comparison. With 10 pairwise comparisons among 5 role sets and a Bonferroni correction (alpha 0.005), each figure grows by about 30%.
> - **Rough cost:** at about 110,000 tokens per council run as reported (the 2.2.x installed runs' context sizes), 350 runs is about 39M tokens and 5,250 runs about 580M. Summed per-message usage runs about 3.7 times higher, by outside review 1's 78,934 against about 291,000. The no-diff material, with surrounding modules, will cost more per run.
> - **Not decided:** which cell to use. Decision 6's "about 10 points pooled" target sits near 10 per area with 5 repeats, or 15 to 20 per area with 3.
> - **The H9 test, adopted by the researcher, 19 Nov 2026:** one omnibus test across all five role sets. It's a mixed-effects logistic regression with role set as a fixed effect and seed as a random effect, tested by likelihood ratio at alpha 0.05. Pairwise comparisons are follow-ups, Holm-corrected.
> - **Its power at 15 × 3,** by simulation on 19 Nov 2026 (400 simulated comparisons per row):
>
> | Differences between role sets | Power at a 50% catch rate | Power at an 83% catch rate |
> |---|---|---|
> | No difference (size check) | 5% | 4% |
> | One set 5 points better | 25% | 48% |
> | One set 10 points better | 82% | 99% |
> | One set 15 points better | over 99% | over 99% |
> | Even spread, 0 to 10 points | 72% | 98% |
>
> - **How it was simulated:**
>   - each seed's catch probability came from a random intercept on the logit scale (SD 1), with role-set shifts set so the average differences match each row;
>   - each role set reviewed every seed 3 times;
>   - the full and null models were fitted by maximum likelihood, with 20-point Gauss–Hermite quadrature over the seed effect;
>   - the likelihood-ratio statistic was compared with chi-square on 4 degrees of freedom.
>   - The "no difference" row is the test's false-positive rate. With 400 simulations, each figure is within about ±5 points.
> - **The token multiplier, checked:** outside review 1's "about 291,000 summed" already counted each message once. That judge's transcript has 17 entries but 5 distinct message IDs, and they sum to 291,191 with duplicates removed (922,093 with them). So the 3.7 multiplier stands, and the table's token columns don't change. *(Claude Code's note: across all five agents of that run, the ratio of summed to reported tokens is 3.2, so the "summed" column may run about 13% high.)*
> - **Seeds for evolution and the final comparison, adopted by the researcher, 20 Nov 2026:** the evolution search reuses the core comparison's 105 seeds. The held-out set for the final comparison is a fresh 15 per area, 105 in all, with no overlap, so it's as large as the core comparison. It builds on the 19 Nov decision that the evolution experiment's held-out seeds are separate from the core 105, which still holds.
>   - *(Claude Code's note)*: the final comparison is one winner against one comparator (section 7), so its power isn't the omnibus test's. At 105 seeds and 3 repeats, the pairwise table gives about 11 points at a 50% catch rate, close to decision 6's "about 10 pooled".
>   - *(Claude Code's note)*: with the search reusing the core 105, and the core comparison's winner becoming the starting council (G6), both selections are made on the same seeds. The fresh held-out set is what keeps the final score clean.
> - **The held-out set prefers bugs fixed after the reviewing model's training cutoff,** where they exist, adopted by the researcher, 20 Nov 2026. *(Claude Code's note: by the supply report, they barely do outside CVEs. SWE-bench-Live's July 2026 tasks were all read in the hard-tier pilot, MCR-Bench's commits run from 2016 to 2024 and ReviewBench's pull requests end in April 2026. 3,515 of 4,178 CVEs in the pool were published in 2026, but which fall after the cutoff wasn't measured. So in practice the preference mostly reaches security and privacy.)*

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, G1: [reviews L850](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L850)):** which score the keep rule's interval is computed on. Before it, the sources gave:
> - **The decision:** the keep rule's primary score is the catch rate on planted seeds. The guard is that extras per catch mustn't worsen by more than 20% against the parent. Rank-first is reported alongside, not used for the decision.
> - **What it replaces:** decision 6's optional guard, that precision can't fall by more than a pre-set margin "such as 10 points" ([decision 6 L250](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L250)). Its recall is the catch rate.
> - catches, misses, false flags and severity ([plan L19](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L19)), with false alarms counting against a council ([plan L23](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L23));
> - recall, with an optional precision guard ([decision 6 L248](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L248));
> - rank-first and extras per catch as main measures since 19 Nov (section 6).

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, C4: [reviews L825](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L825)):** how the winner is picked and how held-out seeds are used. Before it, the sources disagreed:
> - **The decision:** the winning generation is picked on the search seeds only, then scored once on the held-out seeds at the end, alongside the baselines. The held-out set is never used for selection.
> - **What it replaces:** "Winner: the generation that scored best on the held-out tests" ([plan L42](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L42)). It agrees with decision 6's final comparison, which is chosen in advance with no best-of-k selection.
> - **Not settled by it** *(Claude Code's note)*: decision 6 runs the winner, the starting council and the non-evolving control 3 times each on the held-out seeds ([decision 6 L253](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L253)). Whether "scored once" means one final phase of runs or one run per council is still open, and so is the repeat count, which is the G4 slot.
> - "Winner: the generation that scored best on the held-out tests" ([plan L42](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L42)), which is a selection made on the held-out set;
> - decision 6's final comparison is chosen in advance, with no best-of-k selection, and reports "the winner's held-out score" ([decision 6 L256](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L256));
> - prior describes the keep rule as using held-out seeds ([prior L507](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/prior-work-research.md?plain=1#L507)), while the plan says "computed on the same seeds";
> - outside review 1's B3 and outside review 8's idea 27, both pending, bear on it ([reviews L650](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L650)).

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, C5: [reviews L826](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L826)):** the definition of the optimum council size. Before it, the sources disagreed:
> - **The decision:** the optimum council size is the point where adding a reviewer no longer significantly raises the catch rate, with cost per catch reported beside it.
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
| 19 Nov | C3: pilot results reported only as labelled exploratory findings; pilot seeds stay out of the formal comparison | section 4.2 | "never reported as results" (13 Nov) |
| 19 Nov | C4: the winner picked on the search seeds only, then scored on the held-out seeds at the end | section 7 | "the generation that scored best on the held-out tests" |
| 19 Nov | G1: catch rate as the keep rule's primary score, with an extras-per-catch guard of 20%; rank-first reported alongside | section 7 | decision 6's optional precision guard |
| 19 Nov | G2: a catch is within 3 lines and the right problem; the wrong mechanism is a miss, logged as a close call | section 6 | — |
| 19 Nov | G3: the 2 Nov scoring judge kept (GPT-6.1 Sol, DeepSeek re-judging); at least 50 hand labels, 90% to pass, 95% the target; the route to build | section 6 | "about 50" labels |
| 19 Nov | G2 counting rules: one seed per finding, merged findings as the judge merged them, the council's final output as the main rate | section 6 | — |
| 19 Nov | C2: real bugs from public pull-request datasets, or traced back to the pull requests that introduced them, as the main seeds, three levels, equal per area, decision (a)'s material, Mistral seeds as an extra only | section 4.2 | "120 per app, four-level mix, WinScope first" (2 Nov) |
| 19 Nov | G5: the core comparison is role sets A, A′, B, C and the generalist; debate and the workflow edition are secondary, afterwards | section 4.1 | — |
| 19 Nov | G6: one locked plan; the role-set comparison first, its winner the starting council for evolution | section 4.1 | — |
| 19 Nov | G4: decision 6's numbers (3 variants, 3 final repeats, about 20 and 10 points detectable); caps after one measured dry run | section 5 | "a few" variants, "several" repeats |
| 19 Nov | C14: "critical" dropped; HIGH seeds reported as a separate line | section 6 | "about 12 critical seeds per app" |
| 19 Nov | C11: decision 6's cost estimate; the order of work rewritten | section 13 | "about half a session" per small run, and the old order |
| 19 Nov | G7: what happens after the no-diff check | section 6 | — |
| 19 Nov | C5: the optimum size is where another reviewer no longer significantly raises the catch rate, with cost per catch beside it | section 7 | the two earlier definitions |
| 19 Nov | C8: one list of what's new, with the appeal first; the measurement, not the design | section 2 | the five earlier lists |
| 19 Nov | S3: H8 and H9 confirmatory, the rest exploratory | section 3 | — |
| 19 Nov | G10: misleading `CLAUDE.md` files written against review areas; a seed-aware count of seeds touched | section 12 | — |
| 19 Nov | The version pin: npm `stable` on the day the plan is locked, auto-updates off in run sessions | section 5 | — |
| 19 Nov | The cost measure: four token types recorded, dollars at API rates as the headline | section 6 | — |
| 19 Nov | arXiv: cs.MA primary, cs.SE cross-list | section 13 | — |
| 19 Nov | H8's null: the appeal recovers no more real bugs than the judge alone; "many false ones" is extras per catch up by more than 20% | section 3 | — |
| 19 Nov | H9's null: every role set has the same catch rate at equal cost | section 3 | — |
| 19 Nov | C2's wording widened to cover seeds traced back to their introducing pull requests | section 4.2 | "real bugs from public pull-request datasets" |
| 19 Nov | Outside review 1: C4 adopted, settled by the version pin; B1 adopted, settled by the cost measure | section 5, section 6 | — |
| 19 Nov | C4's open part: full model IDs, never aliases, and each transcript's model ID recorded | section 5 | — |
| 19 Nov | B1's open part: tokens summed from the transcripts' per-message usage, subagents included, counting each message ID once | section 6 | Claude Code's per-agent figure |
| 19 Nov | C7: (g)'s change of order logged as a deviation | section 9 | "Each follows the brief's suggestion" |
| 19 Nov | G8: items settled elsewhere marked, with pointers | sections 12 and outside reviews 1, 3 and 8 | — |
| 19 Nov | G9: a pre-run checklist | section 1 | — |
| 19 Nov | G11: Kumar et al.'s 0.847 and 0.066 rechecked against the paper | outside review 2 | "read only through a fetch tool" |
| 19 Nov | G12: a reviewer's questions answered; the power part pending | sections 10 and 7 | — |
| 19 Nov | G12's power part: 15 seeds per area (105 in all), 3 repeats per role set | section 7 | — |
| 19 Nov | H9's test: one omnibus mixed-effects logistic regression, likelihood ratio at alpha 0.05; pairwise follow-ups Holm-corrected | section 3 | pairwise tests |
| 19 Nov | The evolution experiment's held-out seeds separate from the core comparison's 105 | section 7 | — |
| 19 Nov | Outside review 8's idea 11 dropped as a separate arm, covered by the pooled-generalist baseline | section 12 | — |
| 20 Nov | The 7 seed areas, with safety under security and privacy, and policy under docs | section 4.2 (C2) | — |
| 20 Nov | 15 core seeds per area, with severities following the supply; each area's HIGH, MED and LOW counts recorded | section 4.2 (C2), section 6 (C14) | "three severity levels" with no split stated |
| 20 Nov | The evolution search reuses the core 105; a fresh held-out 105 (15 per area), no overlap | section 7 (G12) | "held-out seeds separate from the core 105" (kept) |
| 20 Nov | At most one seed per pull request, and per project for CVEs | section 4.2 (C2) | the easy pilot's up to 3 per pull request |
| 20 Nov | The held-out set prefers post-cutoff fixes, where they exist | section 7 (G12) | — |
| 20 Nov | Area entangled with source and difficulty; per-area results reported with their source | section 10 | — |
| 20 Nov | Performance fallback: SZZ in the cloned projects, then record any shortfall | section 4.2 (C2) | — |

**Deviations and post-hoc exceptions:**
- **Decision (g) changed the brief's order** (adopted by the researcher, 19 Nov 2026, outside review 10's C7): brief (g) said to mark the packs before deciding (a). (a) was decided first, and the packs come before (a)'s difficulty check instead. It's logged here as a deviation, and the notebook's line that each decision "follows the brief's suggestion" is amended.
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

- **Area is entangled with source and difficulty** (adopted by the researcher, 20 Nov 2026): security and privacy comes mainly from CVE fixes (about 175 of 205). Tests, docs, performance and clear-cut maintainability come only from the two review datasets, which gave the easy tier, while CVEs and SWE-bench-Live gave the hard tier. Every role set reviews every seed, so the core comparison controls for it, but per-area claims don't. Results by area are reported with their source. The source is the seed folder's counts-only supply report (`reports\seed-supply-2026-11-20.md`), checked by Claude Code.

**What a reviewer of the paper would ask, and the answers so far** (adopted by the researcher, 19 Nov 2026, outside review 10's G12):
- **Is anything in the pipeline not Claude?** Yes for scoring: the scoring judge is GPT-6.1 Sol, with DeepSeek re-judging (G3). No council seat is non-Claude yet, so the mixed-family question stays exploratory.
- **What if the no-diff check is too easy too?** G7 sets the steps: more of the project once, or back towards the diff once, then the best material with its limitation recorded.
- **Rank-first was chosen after seeing the figures.** It's reported alongside and doesn't decide anything (G1), and the pilot figures are exploratory (C3).
- **Contamination:** seeds favour post-cutoff fixes as a precaution, and the post-cutoff check rests on 5 seeds. Project knowledge isn't guarded against (this section).
- **Has the appeal been tested on unsaturated material?** Not yet. It's planned, and H8 is its confirmatory test.
- **Are the costs real costs?** From the formal runs on, yes: summed per-message usage from the transcripts, in dollars at API rates (B1). The pilot's token figures are context sizes.
- **What size of difference can the core comparison detect?** See the power slot in section 7. Its numbers are still to choose.
- **Which languages, areas and licences?** Seven areas in the pilot. The languages and the sources' licence terms are still to state in the locked plan.

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
| A default checklist in reviewer briefs | [plan L1369](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1369) | leaning, not decided. Outside review 10's G8 notes A′ tests it | (amended 19 Nov 2026, G8, adopted by the researcher, 19 Nov 2026: settled as tested by A′ against A, so the leaning isn't a separate decision.)
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
| Outside review 8's 35 ideas | [reviews L688](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L688) | all pending | (amended 19 Nov 2026, G8: idea 33 is settled in part by decision (e). Idea 11 overlaps the adopted pooled-generalist baseline, noted under it.) (amended again 19 Nov 2026: idea 11 is dropped as a separate arm, adopted by the researcher, 19 Nov 2026, as covered by the pooled-generalist baseline.)
| Outside review 9's 16 suggestions on the paper | [reviews L777](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L777) | all pending |
| Outside review 10's remaining findings | [reviews L900](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L900) | C2–C5, C7, C8, C11, C14 and G1–G12 pending |
| The `CLAUDE.md` test's misleading file, and who can write it without seeing the seeds | [reviews L859](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L859) | pending |
| The evidence behind "real bugs are the main seeds" | [reviews L860](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L860) | pending |

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, G10: [reviews L859](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L859)):** how the `CLAUDE.md` test's misleading file is written. The brief's design targets "a seeded bug's pattern" ([briefs L209](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/decisions-pending-2026-11-17.md?plain=1#L209)), but "seed-free sessions design the files" ([plan L1267](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1267)), and those sessions never see the seeds.
> - **The decision:** the misleading `CLAUDE.md` files are written against whole review areas, not specific seeds. A seed-aware session then reports, in counts only, how many seeds each file touches.

## 13. Publishing and deliverables

- **Deliverables:** the calculator's repo and README, a write-up or preprint, the raw run logs, the who-caught-what log and the explainer video ([plan L1785](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1785)).
- **The paper:**
  - LaTeX in ICML style, posted as an arXiv preprint ([plan L1795](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1795));
  - out of parking since 19 Nov, as a research paper that leads with its experiments, because arXiv cs takes review and position papers only after peer review ([plan L814](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L814));
  - the parked fixes still apply ([plan L813](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L813));
  - outside review 9's 16 suggestions are pending (section 12).
- **The route:** a personal endorsement, a research paper rather than a position paper, arXiv's submission limits, and every reference checked ([plan L1810](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1810)).

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (the notebook's paper route: [plan L1802](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1802)):** the arXiv primary category, and so the endorsement domain. The paper session recommended cs.MA with cs.SE as a cross-list.
> - **The decision:** cs.MA as the primary category, with cs.SE as a cross-list. So the endorser has to be in cs.MA's endorsement domain.

> **~~Decision pending~~ Decision: adopted by the researcher, 19 Nov 2026 (outside review 10, C11: [reviews L835](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/outside-reviews.md?plain=1#L835)):** the cost estimate and the order of work. Before it, the sources disagreed:
> - **The decision:** decision 6's estimate replaces the old one: about 150M tokens and $800–1,300 per app per evolving run.
> - **The order of work, rewritten:**
>   1. the three hand-check packs;
>   2. the next difficulty check;
>   3. lock the plan;
>   4. the role-set comparison;
>   5. then evolution.
> - The notebook's old "Order of work" stays there as the record.
> - "Each small run costs about half a session" and "The total is roughly 3–4 sessions" ([plan L1574](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1574)), with an order of work that starts with "Run small app #1" ([plan L1764](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1764));
> - decision 6: "about 150M tokens per app per evolving run, about $800 to $1,300 at API rates", and "about 360 checked seeds across three apps" ([decision 6 L267](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/research/decision-6-seeds-and-stopping.md?plain=1#L267)).
> - **Missing from the order of work:** the seeds, the calibration run, the plan lock and the role-set comparison. It ends with a review by "Fable 5.1", which is still to choose ([plan L1767](https://github.com/Ablation-Lab/evolving-review-councils/blob/87eb410/core-method/experiment-plan.md?plain=1#L1767)).

---

Built on 19 Nov 2026 by Claude Code, from the sources above only.
