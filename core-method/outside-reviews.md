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

**Seeds (12 Nov 2026), all adopted by me after reading [seed-sources-research.md](seed-sources-research.md).** Each point says where it came from: Claude's suggestions in that file, or me.

1. **Real bugs are the main seeds.**
   - **Reason:** Kumar et al. (2026) report the best model's F1 at 0.847 on injected bugs and 0.066 on real bug-fix PRs. So written seeds may make councils look far better than they are.
   - **Origin:** the decision is mine. The evidence and the proposal of ReviewBench as the main external source of real seeds came from Claude. Claude's write-up had left real against written seeds open.
   - **Caveats:**
     - Kumar et al.'s injected bugs were made by mutation, not by Claude, so the result says nothing directly about Claude-written seeds.
     - The figures were read only through a fetch tool's summary of the abstract page. They need checking against the paper before the paper cites them.
2. **Order of preference for each ISO area:**
   1. real documented bugs;
   2. seeds made without any Claude model: by mutation tools, or written by a non-Claude model;
   3. Claude-written seeds, only where neither is possible.

   Every seed is tagged with its ISO area and its source. The paper states plainly which areas needed Claude-written seeds and why.
   - **Reason** (Claude's wording; I didn't give one): the further a seed is from a Claude model, the less a mostly-Claude council can be helped by sharing the writer's habits. Real bugs also avoid the injected-seed gap above.
   - **Origin:** the order, the non-Claude writer, the tagging and the statement in the paper are mine. Claude had suggested the mutation tools, as a cheap control rather than the main seeds, and fix commits from our own never-public repos as a held-out real set.
   - **Caveat:** the Kumar et al. result is about mutation seeds, which this order puts second. Tagging by source will show whether they are as easy for our councils.
3. **Equal numbers of seeds per area to start.** This is a starting point, to be adjusted after the first results ("to begin with, anyway", in my words). Results are reported by area and by source, so a weak seat isn't confused with harder or easier seed sources.
   - **Origin:** mine.
4. **Before relying on ReviewBench:**
   - check which models helped build its golden findings;
   - check its data licence;
   - score with our own outside-family judge, not its Claude judge (Claude Sonnet 5).
   - **Origin:** checking the data licence was Claude's suggestion. Checking the models is mine, building on Claude's notes that "several frontier models" helped find the golden findings and that the answers have been public since October 2026. Using our own judge is mine; it applies the plan's existing outside-family judge rule ([experiment-plan.md](experiment-plan.md), from the 31 Oct review) to this source.

**Seat roles (12 Nov 2026), adopted by me.** The full plan is in the Claude Docs doc "Seat roles plan" (12 Nov 2026), which is private. Each point says where it came from, using the discussion record above: Claude, me or both.

1. **ISO/IEC 25010:2023 is the reference map, not a standard to pass.** Every seat and every seed is labelled with the ISO areas it covers, so coverage can be compared with a recognised baseline. The seed tags are seed decision 2 above.
   - **Origin:** Claude proposed ISO/IEC 25010 as a reference point (point 1). Using it as a map rather than a standard, and labelling every seat, are mine.
2. **Council Dial Lite, the read-only tier:**
   - **It keeps** its current areas: correctness; security and privacy; docs and policy accuracy.
   - **It adds** reliability, performance efficiency, safety, the app's own tests and maintainability.
   - **Maintainability is limited to clear-cut problems,** such as dead code, duplicated logic and comments that contradict the code. Taste and style stay out of the scoring.

   That covers six of ISO's nine areas: functional suitability, security, reliability, performance efficiency, maintainability and safety. Docs and policy accuracy and the app's own tests aren't ISO areas. The nearest ISO item to the tests is testability, which falls under maintainability.
   - **Origin:** four of the additions were in Claude's list of areas the seats don't cover (point 1): maintainability, reliability, performance and the app's own tests. Safety came from Claude's literature check ([review-areas-research.md](review-areas-research.md)), which found it missing from that list. The choice of areas and the clear-cut limit on maintainability are mine.
   - **Not decided here:** whether the new areas get seats of their own or are folded into existing briefs. I had suggested folding them in (point 2), and decision 4 leaves it to the tests.
3. **Left out on purpose for now: compatibility, flexibility and interaction capability,** because they need a running app. They come later in the full Council Dial, including a seat that reviews frames of the running app with the video-review tool.
   - **Origin:** mine. The running-app tier and the video-review seat are from point 2, where I also said usability and compatibility matter little for the Claude skills built so far. Flexibility came from Claude's literature check.
   - **Caveat:** Claude had argued that usability does apply to the formal experiment, and that some of it (error messages, settings, help text) can be seen in the code (point 3). Leaving interaction capability out of Lite leaves those readable parts out too.
4. **No winner chosen in advance.** These are tested against each other on the same seeds at the same cost, with repeats, and the results decide:
   - **A:** the current seats, as the baseline;
   - **B:** three wide seats with the new areas folded in;
   - **C:** five narrow seats;
   - **a single generalist** with an ISO checklist, as a baseline.
   - **Origin:** testing role sets against each other on the same seeds was joint (point 4). Claude proposed the four sets in a text reply after the review-areas research on 12 Nov 2026. I agreed to test all four against each other rather than choose one in advance. The proposal's own words are in [outside-reviews-sources/2026-11-12-role-sets-proposal.md](outside-reviews-sources/2026-11-12-role-sets-proposal.md). I pasted them from the claude.ai conversation, so they can't be checked against any local transcript. ~~The four sets themselves are in the Seat roles plan, and the record doesn't say who proposed them.~~ (corrected 12 Nov 2026)
5. **Still open: the number of repeats per role set.**
   - **Origin:** mine.

---

## Outside review 3: what the prior-work search means for the plan

- **Date:** 12 Nov 2026
- **Reviewer:** Claude, the chat assistant. It is **not independent**, for the same reasons as in entry 1.
- **Material:** [prior-work-research.md](prior-work-research.md) (commit aabd10f), read in full.
- **Record:** the reviewer's suggestions, then my direction and the focus the reviewer suggested for it. All were adopted by me on 12 Nov 2026. Claude Code checked the figures against the papers' pages and corrected one (suggestion 4).

### Suggestions (all adopted)

1. **A stronger single-reviewer baseline:** one generalist, run several times and pooled, at the same cost as the councils. Then B and C can't win just by spending more.
   - **Basis:** Tran and Kiela (2026), where one agent matched or beat multi-agent systems at equal reasoning tokens; and SWR-Bench's multi-review aggregation, where pooling several runs of one tool raised F1 by up to 43.67%.
2. **Check the scoring judge against my own hand labels** on a sample of findings, and report the agreement.
3. **Add CRBugBench and MCR-Bench to the seed sources to check.** MCR-Bench is included because severity is part of its key: its abstract says each task has defect metadata including "description, type, severity".
   - **Not yet checked:** whether every defect carries a severity label, and both benchmarks' data licences and availability.
4. **Note the persuasive-PR-description threat as a later test,** linked to the R4 worst-case wording idea. That idea covers R4's ratings and the variant packet in [experiment-plan.md](experiment-plan.md), and the dramatic-wording test in entry 1 (D3).
   - **SEVRA-BENCH** wraps reversed vulnerability fixes in persuasive PR descriptions.
   - **"When AI Agrees Too Much"** (Alexopoulos et al., to appear at ICSE 2027) tested an LLM-refined attack against two review pipelines. It got 17 of 17 reintroduced CVEs past the Claude Code pipeline and 15 of 16 past CodeRabbit, 32 of 33 in all. Each CVE was tested against one pipeline only.
   - **Correction:** the prompt said 32 of 33 got past Claude Code's pipeline; that figure covers both pipelines.

### My direction, and the focus the reviewer suggested (adopted)

**My direction:** keep the decisions solid, but aim the work at what prior work hasn't done.

**The reviewer's suggested focus:**
- **Lead with the parts the search didn't find:**
  - an appeal that can reinstate the judge's dismissals;
  - whole role sets compared at equal cost against planted bugs;
  - the judge's severity calls checked against a severity key (MCR-Bench) and against human labels;
  - evolving or racing review councils.
- **Extend Song (2026) rather than repeat it.**
  - **What Song did:** compared single reviews and pairs of review calls, same-model against cross-model. It had no council, judge or appeal.
  - **What this project would do:** put a non-Claude model in one council seat (for example the appeal or one reviewer), and test whether a mixed-family council beats an all-Claude one at equal cost.

**Also for the record:** I came to this work independently and found the prior work afterwards. The paper will say so plainly, and will position the work as building on Song (2026), MARG and EvoMAS (Hu et al.).

---

**Decisions:** all of the above adopted by me on 12 Nov 2026.

---

## Outside review 4: the first reviewer briefs for the role sets

- **Date:** 13 Nov 2026
- **What happened:** a Claude Code session in the local seat-roles worktree wrote:
  - reviewer briefs for role sets B, C and G;
  - set A's file, which has no text of its own and points to the existing templates;
  - a design note.

  They are in commit c49ecb8 on the local `seat-roles` branch of Council Dial Lite. It isn't pushed, because Lite is in directory review.
- **Reviewer:** the briefs got an independent check: a fresh read-only subagent that the session started. It was given only the new brief files, the design note and [review-areas-research.md](review-areas-research.md), with none of the session's conclusions.
  - **Not independent of Claude:** the writer and the checker are both Claude.
- **Record:** the session's own report, `seat-roles-briefs-report.md`, a local file outside this repo. The figures below are from it. I also checked the commit and the brief files in the worktree.

### Design choices by the session

1. **B, C and G share the same checklist items, word for word, so the sets differ only in grouping.**
   - **How:** the session wrote C by hand, then built B's and G's blocks from it with a scratch script. A second script checked that:
     - all three have the same 55 items, with none repeated;
     - G has C's items in C's order;
     - B's seats are C's seats regrouped.
   - **Tags:** every item is tagged with its ISO/IEC 25010:2023 characteristic, or marked as having none.
   - **Set A** keeps today's templates and has no checklist.
2. **The out-of-scope rule.** Every reviewer stays in its scope, in every set, A included. But it may list up to two problems it would rate HIGH under the heading "Outside my scope". Because those entries carry their own heading, scoring can count catches with and without them.
   - **Not from a source:** the threshold (HIGH) and the cap (two) are the session's judgment calls.

### The independent check

- **Personas:** it found no persona wording in the B, C or G texts.
- **What was changed in the briefs:**
  - **Items that needed knowledge outside the material:** six were reworded, about commit messages, unbounded sizes, batched calls, failure handling, file permissions and example output.
  - **Overlaps between seats:** eight were settled, each by moving the boundary or sending the problem to one seat.
  - **New items:** weak cryptography and guessable values; unprotected transfer and temporary files; crafted input that exhausts the machine; deadlocks; reading back a corrupt state file; order mistakes, including an unawaited call.
  - **Other changes:** a retention clause for personal data, several ISO tags corrected, "naming" narrowed to "naming conventions" and consistent wording between A and the common out-of-scope text.
- **What was changed in the design note only:**
  - how a missing-test finding scores against a code seed;
  - a corrected detail on where out-of-scope entries go;
  - a note that A's opening gives a role identity and the other sets' don't;
  - a note that B's first seat carries 31 items against 16 and 8;
  - a note that "can be found by reading" is an instruction for performance, not an established result.
- **Left unchanged, with the session's reasons:**

  | Point | Why it stayed |
  |---|---|
  | "A return value or default misread" needs knowledge of the library | Reading code always draws on knowing its libraries; saying so wouldn't change what a reviewer does. |
  | Busy waiting overlaps waits with no limit | Both are in the same seat in every set, and they're different defects. |
  | No item for server-side request forgery (SSRF) | Rare in the local apps and skills reviewed so far, and still covered by "other problems within the scope count too". |
  | Resource leaks stay tagged reliability (availability) | Leaks degrade the app and eventually stop it on a long run. |
  | The briefs give the unchecked safety and functional-suitability subcharacteristics without a caveat | Reviewers don't need to know how a source was checked; the design note marks them as unchecked. |
  | Failure handling: impact not added to the item | Impact is the severity's job, not the item's. |

### Two questions the session raised, Claude's suggestions and my decisions (both adopted)

1. **Add A′.** A′ is A's three areas written in the new checklist format, with a neutral opening.
   - **Why:** A against A′ then tests the checklist, and A′ against B and C tests the split of areas. Without it, A differs from the other sets in its role-identity opening and its lack of a checklist at the same time.
   - **Origin:** the session raised A′ as an option in its design note. Claude suggested adding it, and I decided to.
2. **Add policy to the docs seat in B, C and G:** rules, licences and policies the project says it follows. Then every set covers the same ground.
   - **Why:** today only A's docs seat covers policy, so policy seeds would favour A. The design note had said seeds should hold no policy problems unless the other sets gained policy. With this decision they can.
   - **Origin:** the session raised it. Claude suggested adding policy, and I decided to.

### Open item

- **Four ISO subcharacteristics in the briefs come from general knowledge.** They are functional correctness, and safety's operational constraint, fail safe and hazard warning. They must be checked against ISO/IEC 25010:2023 before the plan is locked. [review-areas-research.md](review-areas-research.md) doesn't list subcharacteristics for functional suitability or safety.

---

**Decisions:** A′ and policy in B, C and G adopted by me on 13 Nov 2026. The subcharacteristic check is open.
