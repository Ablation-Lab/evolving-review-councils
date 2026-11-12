# Outside reviews

The research doc ([experiment-plan.md](experiment-plan.md)) has a rule of no overall reviews: nothing from a review is written straight into it, so that no reviewer steers the research. Outside reviews of the work are still allowed, and each one goes here as a dated entry instead. Each entry records:

- who reviewed the work, and how independent they are;
- what they were given;
- their suggestions in full;
- later, which suggestions were adopted, rejected or parked, with the reason for each.

Before the formal evolution experiment starts, the plan (hypotheses, measures, analysis and stopping rules) is locked, dated and published, in the spirit of a registered report. Later changes to it are logged as deviations. The research doc stays public as the record of how the plan was reached. See "Outside reviews (decided 12 Nov 2026)" in the research doc's section "What checked the research doc, and what it missed".

Entry 1 is copied verbatim from the paper repo's `outside-review-01-paper-gaps.md`, with its headings moved down one level to fit this file.

---

## Outside review 1: gap review of the paper draft

- **Date:** 12 Nov 2026
- **Reviewer:** Claude, the chat assistant that has planned the work and drafted prompts with the researcher throughout. It is **not independent**: it has seen the whole project, helped shape much of it and wrote some of the voice-drafted claims that Section 6 counts.
- **Material given:** `erc-paper/main.pdf` at commit 8fe695f (15 pages, title "Evolving Review Councils: First Results from Councils of AI Reviewers"), read as extracted text. It did not see the research doc, main.tex's source comments or the run files.
- **Brief:** list what is covered but thin, what is missing and experiment ideas. The review states no opinion on whether the research is good, and per the outside-reviews rule nothing here goes into the research doc until the researcher decides.

Items marked *(verify)* rest on the reviewer's general knowledge and haven't been checked against a source.

---

### A. Things to check in the paper itself

1. **EvoMAS is not cited.** The 24 references don't include it, or any work on evolving or automatically designing multi-agent systems. That matters for the "can councils evolve?" question and for any endorser approach built on "you cite their paper".
2. **The skill-file size has no version.** Section 5 gives 4,986 and 4,957 tokens with connectors off, but not which Lite version was measured. Lite 2.2.5 measured 4,416 after the 2.2.3 trim *(verify against the 2.2.x report)*.
3. **Token figures used as cost.** Section 7 says reported tokens are each agent's final context size, not cost (78,934 reported against about 291,000 summed). But 4.2 ("about 21% to the run's tokens", "94% of the cheapest reviewer's") and 4.4 (21k against 50–65k) compare those same reported figures as if they were cost. Either caveat them where they appear or recompute them from summed request tokens.
4. **Appendix A contradicts itself on model families.** The judge and merger "come from a model family kept off every council", but the baselines include "councils of several families". If the multi-family councils use every family available, there's none left for the judge. Name the families for each role.

### B. Covered but thin

1. **What "same cost" means.** Matched-cost baselines are the paper's central comparison, but cost isn't defined yet. Given A3, the plan needs one cost measure (summed input and output tokens including cache reads, or money at list price) and a way to measure it that doesn't rely on the per-agent figure Claude Code reports.
2. **Run-to-run variation versus the advance rule.** Section 4.5 shows the same council on the same material giving 1 to 3 HIGH findings. Appendix A's 90% interval is computed "on the same seeds", which captures variation across seeds but not across runs. The plan should say how many repeats each variant gets and whether the interval includes run-to-run variance.
3. **Choosing the best of several variants.** Each generation tries "a few variants" and keeps the best if it passes. Picking the best of several and then testing it on the same seeds favours lucky variants (selection bias, or the winner's curse). Options include re-testing the chosen variant on a fresh draw of runs, or correcting for the number of variants tried.
4. **Who proposes the variants?** "Changing its size, roles, briefs or models" doesn't say who writes the changed briefs. If a Claude session proposes them after seeing which seeds were missed, the 80 search seeds leak into the briefs. The held-out 40 catch that only at the end. Say what the proposer may see.
5. **How unplanted real findings are scored.** The pilot and the stress test both found real flaws the key had missed. Appendix A scores catches, misses and false flags against seeds, but doesn't say how a real, unplanted finding counts: as a false flag, as ignored or as a bonus. Scoring it as a false flag would penalise the best reviewers.
6. **The person's calls.** In the Lite runs a person decided appeal disagreements. Say whether the formal experiment includes a human call (then the person is a variable, and their calls should be blind to the configuration) or scores the council's output before any human call.
7. **How Section 6 links to the question.** The human-in-the-loop material is well evidenced, but it answers the companion project's question more than this paper's. A sentence on why it belongs here would help, such as how relay errors affect council results. Otherwise it could move to the Human in the Loop project's own write-up.
8. **Power.** 40 held-out seeds across four severity tiers is about 4 critical seeds per app in the held-out set. There's no estimate of what size of improvement that can detect. A quick simulation using the variance already seen in 4.5 would show whether 40 is enough.

### C. Missing

1. **Related work on evolving or automatically designed agent systems:** EvoMAS, and *(verify)* ADAS (automated design of agentic systems), AFlow and GPTSwarm-style graph optimisation. These are the nearest prior work to question 2, and a reviewer of the paper would expect them.
2. **Related work on LLM code review:** benchmarks or studies of LLMs reviewing code or finding bugs *(verify names: have a session search)*. At the moment the related work covers multi-agent counts, debate, judges and oversight, but not code review by LLMs.
3. **How bugs are seeded,** with literature. Mutation testing is the standard way to plant bugs, and its tools generate them without any LLM *(verify which tools fit Python and C#)*. That would weaken the "Claude wrote every seed" limitation.
4. **Environment pinning.** Section 5 says to record the environment. The plan should also **fix** it: connectors off, no instruction files, messaging off, a pinned Claude Code version (it moved from 2.1.319 to 2.1.322 during these tests) and pinned model versions, with any update logged as a deviation.
5. **Budget and time.** No estimate of the formal experiment's total cost, and no cap figures. The caps are mentioned but not given numbers.

### D. Experiment ideas

1. **Seeds not written by Claude.** Make part of each app's seeds with a mutation tool and part from real bug-fix commits in open-source projects (revert the fix, and the bug is the seed). Compare catch rates on Claude-written, tool-made and real seeds. If councils do much better on Claude-written seeds, the same-family problem is measurable rather than just a caveat.
2. **Capture–recapture estimate of missed bugs.** Software-inspection research estimates how many defects remain from how much independent reviewers' findings overlap *(verify: capture–recapture in software inspections)*. Councils produce exactly that overlap. That gives an estimate of what everyone missed, which is useful because the keys have missed real flaws twice.
3. **The dramatic-wording test (R4), done properly.** The same bug described plainly or with a spelled-out worst case, across many trials and several judge models, measuring the severity shift. It's cheap, clean and pre-registrable, it follows directly from 4.3, and it matters for any council in which reviewers write prose that judges read.
4. **How many repeats are enough?** Use the six byte-identical slug runs, plus more, to estimate the run-to-run variance and choose the repeat count for the formal experiment before locking the plan.
5. **Validating the cost measure.** For a few runs, compare Claude Code's reported tokens with summed request tokens and the dollar cost from the API, then pick the measure for "same cost".
6. **Human calls as a variable.** Run the same disputed findings past the person with and without the configuration visible, to see whether knowing which council produced a finding changes the call.
7. **The steering test** (already planned) fits the locked plan well as a secondary experiment, since its setup is simple and its outcome is a severity shift.

### E. For locking the plan

From the above, these are the decisions the locked plan needs that the paper doesn't yet make:
- the cost measure;
- the repeat count per variant, and whether the advance interval includes run-to-run variance;
- the correction for choosing among several variants;
- what the variant proposer may see;
- how unplanted real findings are scored;
- whether human calls are in the experiment;
- which model families take which roles;
- the seed sources (Claude, tool, real bugs) and their proportions;
- the environment pins;
- the held-out size, from a power check;
- the budget and caps, in numbers.

---

**Decisions** (to be filled in by the researcher): adopted, rejected or parked, with a reason for each.

---

## Outside review 2: which review areas should council seats cover?

- **Date:** 12 Nov 2026
- **Reviewer:** Claude, the chat assistant, in a voice discussion with me while I read the paper's Figure 1. It is **not independent**, for the same reasons as in entry 1.
- **Material:** the council's seat roles as the Lite runs use them: correctness; security and privacy; docs and policy accuracy.
- **Record:** who raised each point, in the order they came up. Claims marked *(verify)* rest on the reviewer's memory; they are checked in [review-areas-research.md](review-areas-research.md).

### The discussion

1. **Claude: the roles came from practice, not a framework.**
   - **Reference points:** the ISO/IEC 25010 quality model, and studies of what human code reviewers flag. From memory, most review comments concern maintainability, not bugs *(verify)*.
   - **Areas the roles don't cover:** maintainability; reliability (error handling, failure cases); performance; the app's own tests, meaning whether they test the right things (relevant because the WinScope pilot's 97 problems had all passed the builders' own tests); usability; compatibility.
   - **Performance by reading:** many performance problems can be spotted by reading the code, such as nested loops over large data, loading whole files or slow work on the UI thread, so they could be seeded.
2. **Me: fold some areas in rather than adding seats.**
   - Performance, maintainability and reliability could go into the existing briefs as subsections rather than new seats.
   - A basic performance check could join the existing tests.
   - Usability and compatibility matter little for the Claude skills built so far.
   - Full Council Dial could use the video-review tool to review frames of a running app as part of a review. That needs a running app, so it's a separate tier from read-only review.
3. **Claude: usability does apply to the formal experiment.** It reviews apps like WinScope, where usability matters. Some of it (error messages, settings, help text) is visible in the code.
4. **Joint: test role sets against each other on the same seeds,** for example performance folded into correctness against performance as its own seat. If a dedicated seat doesn't catch more, folding it in wins.
5. **My decision:** the seat roles are settled, researched and tested before the plan is locked. This is a core item, to do now.

---

**Decisions** (to be filled in by the researcher): adopted, rejected or parked, with a reason for each.
