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

**Decisions** ~~(to be filled in by the researcher)~~ (pending: the researcher to decide; amended 19 Nov 2026): adopted, rejected or parked, with a reason for each.

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

**Decisions** ~~(to be filled in by the researcher)~~: adopted, rejected or parked, with a reason for each. (amended 19 Nov 2026: this label was left over from the template. The decisions are recorded just below, under "Seeds (12 Nov 2026)" and "Seat roles (12 Nov 2026)", all adopted by me, on 12 Nov 2026, in `18d0869` (seeds) and `65d0648` (seat roles), after the entry itself was added in `9b556d8`.)

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

**Decisions:** A′ and policy in B, C and G adopted by me on 13 Nov 2026. The subcharacteristic check is open. *(Closed 13 Nov 2026: see outside review 5.)*

### Second round (13 Nov 2026)

- **The commit:** 83d9897 on the local `seat-roles` branch, after c49ecb8. It isn't pushed.
- **Source:** the "Second round" section of `seat-roles-briefs-report.md`. I also checked the commit and the brief files in the worktree.

**What changed:**
- **A′ added:** three seats with 32 items (12, 11 and 9), all copied by script from the shared pool in set C. It uses the same neutral opening, layout and out-of-scope rule as B and C. The skill files spell it "A-prime" to stay plain ASCII.
  - **Selection:** its items follow A's own focus texts in `briefs/v3/shared.md`, not ISO areas alone.
  - **Partial areas:** where it takes part of an area (reliability, and maintainability for comments only), it has its own ISO line naming just what its items cover.
- **Three policy items added:** licence problems against the project's stated licence, stated project rules the code breaks and promises the code breaks.
  - **Where:** each is in the docs seat of A′, B and C and in G's list, word for word the same. C's docs seat is renamed "docs, policies and maintainability", and B's to match.
  - **Tag:** "no ISO characteristic: policy", so policy seeds can be reported as their own area.
  - **Counts:** B, C and G now share 58 items.
- **A wording change for B and C too:** the shared neutral opening no longer says "the other reviews cover the rest", since that isn't true for A′. B's and C's out-of-scope paragraphs still say other reviews cover those areas. No council has run on the first-round texts, so no runs are left incomparable.
- **The script checks were rerun and passed:**
  - B, C and G hold the same 58 items, and A′'s 32 are pool items word for word;
  - the policy items are in every set once, always in the docs seat;
  - there's no persona wording;
  - every file from de465aa is unchanged.

**The second independent check.** A fresh read-only subagent got only the round-two diff, the new A′ file, the current set C and the shared layout file. It found no persona wording and confirmed the counts.
- **Changed in the briefs:**
  - **Licence items:** reworded so they don't need licence knowledge from outside the material.
  - **Rules item:** limited to what the code, manifests or packaging files in the material show.
  - **Privacy wording:** "the review that covers privacy", not an item the docs reviewer can't see.
  - **Overlaps settled:**
    - promises about system changes go to the review that covers safety;
    - promises broken by collecting, keeping or sending personal data go to the review that covers privacy;
    - licence notices belong to the licence item, not the rules item.
  - **A′'s correctness out-of-scope line:** now says how the code handles failures and malformed outside input isn't reviewed.
  - **Partial failures added to A′'s correctness seat,** since A's focus names "data loss", which brought A′ to 32 items.
  - **Two header notes completed:** what A′ leaves out compared with A and that A′ leaves out scope lines.
- **Changed in the design note:** every seed is also tagged with the checklist item it plants (or "none"). A′ against B and C is then scored only on seeds whose item A′ has.
- **Left unchanged, with the session's reason:** "runs code it downloads" and "uses the network" fall on the same lines as the security items on unchecked downloads and plain HTTP. They're different problems, a broken promise against a missing check, so both may be reported and the judge merges them if they turn out to be one. This is recorded in the design note.

**My decisions, each adopted on Claude's suggestion (13 Nov 2026):**
1. **A′'s items follow A's own focus texts.** So partial failures, races, deadlocks and contradicting comments are in, which keeps A against A′ a test of format.
2. **Broken personal-data promises belong to the privacy seat, not the policy items,** so no promise sits in two seats.
3. **A′ not being a pure format test is accepted and recorded.** Its checklist and out-of-scope paragraphs draw sharper edges between seats than A's overlapping focus texts do.
4. **A′ has no seat for broken system-change promises.** That follows from A's areas, so it stays.

**My decisions on round one's open questions (13 Nov 2026):**
1. **The out-of-scope rule stays** (HIGH only, at most two), as a recorded judgement call. I'll revisit it after the first runs, by scoring with and without those entries.
2. **The design note will move out of the plugin** to this repo before any merge.
3. **A version name for the role-set briefs** is decided when they're wired into Lite.

**Open item, unchanged** *(closed 13 Nov 2026: see outside review 5)*: functional suitability's "functional correctness", and safety's operational constraint, fail safe and hazard warning, come from general knowledge. They must be checked against ISO/IEC 25010:2023 before the plan is locked.

---

## Outside review 5: which real-bug sources to use

- **Date:** 13 Nov 2026
- **Reviewer:** Claude, the chat assistant. It is **not independent**, for the same reasons as in entry 1.
- **Material:** [seed-access-check.md](seed-access-check.md) (commit 0610c52), read in full.
- **Record:** the reviewer's suggestions, all adopted by me on 13 Nov 2026, then the closing of the ISO item left open in entry 4. Claude Code checked each point against the access check and added notes where the check doesn't settle it.

### Suggestions (all adopted)

1. **The source plan:**
   - **MCR-Bench first.** Its functional defects (F.6 performance and F.7 security and privacy among them) are included, plus evolvability defects filtered down to clear-cut maintainability. Every seed's severity is hand-checked, because its labels are LLM-assigned and loose.
     - **Not yet checked:** whether the evolvability codes separate clear-cut problems (dead code, duplicated logic, comments that contradict the code) from style, so that filter may need reading each defect.
     - **Small pool:** F.7 has only 34 defects, across all rounds.
   - **ReviewBench** for correctness, reliability, tests, docs and performance. Results are always reported separately for findings from Claude producers and from non-Claude producers, since Claude models wrote about 55% of its key.
   - **SWE-bench-Live MultiLang's C# and JavaScript tasks from July 2026** (22 and 13) serve as a contamination check, not as main seeds.
   - **CVEfixes, rerun for 2025 to 2026 CVEs,** gives security seeds later.
   - **Only safety and policy need written seeds,** from a non-Claude writer first. No source in the access check labels either area.
     - **Privacy:** it has no label of its own in any source either. It is part of MCR-Bench's F.7 and isn't separated in ReviewBench's security category. Privacy seeds may also need writing if the real ones prove too few.
   - **CRBugBench is on hold:** it has no licence, and its public data has no severity or category labels.
2. **Seeds and answer keys stay private until the experiment is done:** in a local-only folder with no remote, outside this repo and outside anything a council reviews.
3. **Before the full set, a pilot:** about five seeds per area, hand-checked, for the difficulty check (step 5 of the Seat roles plan).

### Closing the ISO item from entry 4

- **The open item is closed.** Functional suitability's "functional correctness" and the safety subcharacteristics used in the briefs are confirmed. The source is the ISO/IEC FDIS 25010 sample from iTeh, read in full by Claude Code.
- **Functional suitability** has three subcharacteristics: functional completeness, functional correctness and functional appropriateness (section 3.1).
- **Safety** has five, listed in the foreword: operational constraint, risk identification, fail safe, hazard warning and safe integration. The briefs use three of them: operational constraint, fail safe and hazard warning.
- **Definitions:** the safety definitions come from iso25000.com, because the sample stops before the safety section.
- **Caveats:**
  - the source is the Final Draft International Standard, not the published text;
  - iso25000.com doesn't state which edition it describes.

---

**Decisions:** all of the above adopted by me on 13 Nov 2026. The ISO item from entry 4 is closed.

---

## Outside review 7: Claude Code agent features: eight pages read 16 Nov 2026

- **Date:** 16 Nov 2026
- **Reviewer:** Claude, the chat assistant. It is **not independent**, for the same reasons as in entry 1.
- **Material:** Anthropic's article [Introducing dynamic workflows in Claude Code](https://claude.com/resources/articles/introducing-dynamic-workflows-in-claude-code) (28 May 2026, since updated to say the feature is generally available) and seven Claude Code docs pages:
  - [dynamic workflows](https://code.claude.com/docs/en/workflows);
  - [subagents](https://code.claude.com/docs/en/sub-agents);
  - [running agents in parallel](https://code.claude.com/docs/en/agents);
  - [agent view](https://code.claude.com/docs/en/agent-view);
  - [worktrees](https://code.claude.com/docs/en/worktrees);
  - [agent teams](https://code.claude.com/docs/en/agent-teams);
  - [cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging).
- **Record:** the reviewer's ten suggestions, all waiting for my decision. Nothing from them is in the research doc yet. Claude Code checked each one against the pages on 16 Nov 2026 (Claude Code 2.1.325 on this machine), and the corrections and extra notes are marked *(Claude Code's note)*.
- **Who acts on them** *(Claude Code's note)*: items 5, 7 and 8 change the council set-up, which only seed-free sessions may do (see "Seed-aware and seed-free sessions" in the research doc). Items 1 to 4 are run isolation and records, which belong to the seed folder's session.

### Suggestions (decision pending)

1. **Isolation gap: cross-session messaging.** It's on by default from Claude Code 2.1.224, and Claude may send messages without being asked. Runs need `crossSessionInbound` set to `"refuse"` and a `ListAgents` deny in the project settings, confirmed from the settings file, because `/status` shows nothing.
   - **Checked** *(Claude Code's note)*: the docs say Claude "can decide to send a message without being asked". A `refuse` in project or local settings "applies over every other source". And a refusing session "shows no visible change" in `/status`, so the docs say to check the settings files.
   - **Correction** *(Claude Code's note)*: 2.1.224 is the minimum on macOS and Linux. On native Windows, which these runs use, it's 2.1.234.
   - **Correction** *(Claude Code's note)*: the docs' way to stop sending and listing is deny rules naming **both** `SendMessage` and `ListAgents`. Without `ListAgents`, Claude can't list sessions, but the docs don't say that a message to a name it already knows is blocked. Denying `SendMessage` also removes messaging to subagents, so first check that Lite doesn't use it.
   - **Already in place** *(Claude Code's note)*: the current run folder's settings have the `refuse` and a `ListAgents` deny, but no `SendMessage` deny.
     - (amended 16 Nov 2026 *(Claude Code's note)*: the folder now denies `SendMessage` too. Whether Lite completes with that deny is still to check. See "The messaging check" in the research doc.)
   - **Decision:** ~~pending.~~ adopted by the researcher, 19 Nov 2026, following [decision brief (f)](decisions-pending-2026-11-17.md#f-formally-adopting-outside-review-7-items-1-to-10). Condition from the brief: a dry run first confirms that Lite completes with the `SendMessage` deny. The rule for what a message does to a run is decided in the research doc's decision (b).
2. **Isolation gap: agent teams.** If agent teams are on, named subagents become teammates that can message each other. Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=0` in the run project, and add `CLAUDE_CODE_DISABLE_WORKFLOWS=1` to the launch line.
   - **Checked** *(Claude Code's note)*: agent teams are experimental and off by default. While they're on, a subagent that Claude names in an interactive session launches as a teammate, unless the call is a fork or sets `isolation` itself. Teammates message each other directly. A `0` in a settings file's `env` overrides a shell export, and only higher-precedence settings, such as a `--settings` value or managed settings, could turn teams back on. `CLAUDE_CODE_DISABLE_WORKFLOWS=1` is read at startup.
     - (amended 17 Nov 2026 *(Claude Code's note)*: the agent teams page lists the sources that win over a `0` as "project settings, local settings, and a `--settings` payload", which "apply after user settings", plus managed settings, which "apply after every other source". So for the run folder's project-level `0`, its own local settings file could also turn teams back on. The current run folder has a `.claude/settings.local.json`, which I didn't read, so I can't say what it sets.)
   - **Already in place** *(Claude Code's note)*: the current run folder has both.
     - (amended 17 Nov 2026 *(Claude Code's note)*: checked again in the files. The `0` is in the project `settings.json`'s `env`. `CLAUDE_CODE_DISABLE_WORKFLOWS=1` isn't in the settings file. It's set on the launch line in the run folder's `RUN.md`, as this item suggests.)
   - **Decision:** ~~pending.~~ adopted by the researcher, 19 Nov 2026, following [decision brief (f)](decisions-pending-2026-11-17.md#f-formally-adopting-outside-review-7-items-1-to-10). Condition from the brief: check the run folder's local settings file, since local settings can turn teams back on over a project `0`.
3. **Transcript scan.** A `SendMessage` or `ListAgents` call, or a "Message from @" line, means the run isn't CLEAN.
   - **To test** *(Claude Code's note)*: the docs show "Message from @" as the on-screen preview of an arriving message. They don't say that the transcript file stores that text. So the scan's rule should be tried once on a transcript known to hold a delivered message.
     - (amended 16 Nov 2026 *(Claude Code's note)*: answered by the seed folder's messaging check. A received message is stored as a user turn marked as coming from a peer, not as the preview line. So the scan now checks the stored form and lists subagent hand-backs, which use the same channel, separately. It hasn't yet been tried on a transcript holding a delivered message from another session, since the canary's message was refused.)
   - **Decision:** ~~pending.~~ adopted by the researcher, 19 Nov 2026, following [decision brief (f)](decisions-pending-2026-11-17.md#f-formally-adopting-outside-review-7-items-1-to-10). Condition from the brief: one test first with a delivered message, in a throwaway pair of sessions.
4. **Records.** Subagent transcripts and saved workflow results are deleted after `cleanupPeriodDays` (30 by default). Copy them into each run record.
   - **Checked** *(Claude Code's note)*: subagent transcripts are deleted with their parent session's transcript once it's older than `cleanupPeriodDays`, which defaults to 30. The workflows page says a run's saved results are kept under the session's directory, but neither page lists them in the sweep. So they probably go with the session, but the docs don't say so.
   - **A related risk, not checked** *(Claude Code's note)*: my user settings set `cleanupPeriodDays` to 365. Run sessions start with `--setting-sources project,local`, which leaves user settings out, so a run session may use the 30-day default. The docs don't say whether a session's sweep covers every project's transcripts or only its own. If it covers all of them, a run session could delete my older transcripts. The seed folder's checks already count session folders before and after each run, and the docs' `retention_sweep` event would settle it.
     - (amended 16 Nov 2026 *(Claude Code's note)*: the messaging check found no transcripts missing, and every run folder has its session. That doesn't settle the risk. The oldest sessions it scanned date from 4 Nov, so even a 30-day sweep couldn't have removed them yet.)
     - (amended 17 Nov 2026 *(Claude Code's note)*: the docs now settle most of it. The `retention_sweep` event on the [monitoring page](https://code.claude.com/docs/en/monitoring-usage) gives a skip reason, `user_source_disabled`: "User settings are excluded, for example by the `--setting-sources` flag … and no enabled source provides `cleanupPeriodDays`". The sweep then reports `"skipped"`, so a run session started that way pauses the sweep rather than running it at 30 days. The same page says the sweep covers every project's transcripts ("the top-level `~/.claude/projects/*/*.jsonl` files"), so the concern was the right one to raise. The current run folder's project settings now set `cleanupPeriodDays` to 365, so a session there sweeps at 365 days. The dry-run and review A folders don't set it, so their sessions would have skipped. The event goes only to an OpenTelemetry backend, so this rests on the docs, not on a recorded event.)
   - **Decision:** ~~pending.~~ adopted by the researcher, 19 Nov 2026, following [decision brief (f)](decisions-pending-2026-11-17.md#f-formally-adopting-outside-review-7-items-1-to-10). From the brief: also set `cleanupPeriodDays` in every new run folder, and copy team mailbox files before a team session ends.
5. **Workflow edition design.** The script holds the plan, so comparing a workflow edition with Lite isolates the orchestrator. My call between stages means separate workflows: reviewers, judge and appeal; then the call; then the check. Use schema-checked findings. A repeat must be a new run, never a relaunch, because relaunches return saved results.
   - **Checked** *(Claude Code's note)*: in the docs' comparison table, the script decides what runs next. The docs say a workflow takes no input mid-run, and "for sign-off between stages, run each stage as its own workflow". A `schema` makes an agent return JSON of that shape, ~~retried up to five times~~ and the call fails if the output still doesn't validate after five attempts (corrected 17 Nov 2026 from the workflows page: five attempts, not five retries, and `MAX_STRUCTURED_OUTPUT_RETRIES` changes the count). On a relaunch, completed agents return their saved results, and the runtime blocks timestamps and random numbers inside the script so that a relaunch repeats the same calls.
   - **The repeat rule, stated plainly** (my wording, 16 Nov 2026): every repeat must be a fresh workflow run, never a relaunch of a stopped run, because a relaunch returns saved results for agents that already finished.
   - **Checked** *(Claude Code's note, workflows page re-read on 16 Nov 2026)*: a relaunch replays the run in the order its agents start. Each agent that completed returns its saved result, unless its prompt differs from the previous run's. The first agent that differs runs again, and so does every agent after it. Agents still running when the run was stopped start over. Relaunching isn't only for stopped runs. It's also how Claude finishes a run with failed agents, one stopped at a usage limit or one cut off when its session closed. It works only in the same session, including one reopened with `claude --resume`. In a fresh session, or when the saved results are gone (a `nothing to resume` error), Claude starts the workflow over as a new run. So the rule should cover a relaunch of any earlier run, not just a stopped one.
   - **How the record can show it** *(Claude Code's note)*: a fresh run is a Workflow call that doesn't resume an earlier run. The transcript holds each call's input, so the transcript scan can check for a call that resumes an earlier run (the tool's `resumeFromRunId` input, from the tool list in this session, not the docs page). Each run record should also log the run's ID.
     - (amended 17 Nov 2026 *(Claude Code's note)*: it's now documented, on the [Agent SDK TypeScript reference](https://code.claude.com/docs/en/agent-sdk/typescript)'s Workflow tool entry: `resumeFromRunId` is the "Run ID of a prior `Workflow` invocation to resume", and the output's `runId` is the "Workflow run identifier to pass as `resumeFromRunId` on a later invocation". It still doesn't say whether a relaunch returns the same `runId` or a new one.)
   - ~~**Open** *(Claude Code's note)*: what to do with a run that was interrupted and then finished by a relaunch. Its finished agents keep their own results, so it may still count as one run. Decide before the runs whether such a run is kept, redone as a fresh run or voided.~~ (amended 16 Nov 2026: see the next point.)
   - **Interrupted runs: proposed, pending the researcher's decision before any workflow runs** (my wording, 16 Nov 2026): if the script wasn't edited, count it as one run, and log the run ID and the reason for the relaunch. If the script was edited between launches, void the run.
     - **Checked** *(Claude Code's note)*: even without an edit, a relaunch can rerun agents that had finished. A failed agent runs again, and so does every agent the script starts after it. An agent that returns something different from its first try also makes every agent after it run again. So a run counted as one may hold second attempts, and the record should say which agents ran again, where `/workflows` shows it.
     - **Run IDs** *(Claude Code's note)*: the docs don't say whether a relaunch keeps the run's ID or gets a new one, so log every ID the run used.
     - **Not a relaunch** *(Claude Code's note)*: the runtime restarts a stalled agent automatically, up to five times, inside the same run. So this rule doesn't apply to those restarts. They still use tokens, so the cost measure includes them.
   - **Decision:** ~~pending.~~ adopted by the researcher, 19 Nov 2026, together with the interrupted-run rule as decided in the research doc's decision (d), following [decision brief (f)](decisions-pending-2026-11-17.md#f-formally-adopting-outside-review-7-items-1-to-10) and [brief (d)](decisions-pending-2026-11-17.md#d-the-interrupted-workflow-run-rule). The rule proposed above is replaced by that one: a relaunched run counts as one only after a technical interruption, with at most one relaunch, and a stop by me after seeing output voids it.
6. **Cost measure.** Workflow agents share a prompt cache, with a 5-minute TTL. Record input, cache-read, cache-write and output tokens separately. The `/workflows` per-agent tokens give a third figure to check against.
   - **Checked** *(Claude Code's note)*: agents in the same run share a cache when they have the same model, effort, agent type, tools, output schema and working directory. The default TTL is five minutes, or an hour with `subagentPromptCacheTtl`. `/workflows` shows each agent's token usage.
   - **Note** *(Claude Code's note)*: what's shared is the tools and system prompt prefix, not any agent's findings, so it doesn't break the seats' independence. But it makes later seats cheaper, so a cost comparison with Lite needs to know whether Lite's seats share a cache too. The runtime also holds matching agents for up to 5 seconds so they can read the first one's cache.
   - **Decision:** ~~pending.~~ adopted by the researcher, 19 Nov 2026, following [decision brief (f)](decisions-pending-2026-11-17.md#f-formally-adopting-outside-review-7-items-1-to-10). From the brief: settle outside review 1's B1 (one cost measure) with it.
7. **Seat definitions.** Use `omitClaudeMd` plus a read-only `tools` list as extra isolation. Plugin agents ignore `hooks`, `permissionMode` and `mcpServers`, so isolation stays in the run folder's settings. Subagents get a git status snapshot, so keep run folders out of git.
   - **Checked** *(Claude Code's note)*: `omitClaudeMd` leaves out the user, project and local `CLAUDE.md` files, but managed policy files still load, and it needs Claude Code 2.1.271 or later. The docs confirm that plugin agents ignore those three fields, and that a subagent starts with a git status snapshot.
   - **Already true** *(Claude Code's note)*: none of the dry-run or review run folders is in a git repository.
   - **Note** *(Claude Code's note)*: Lite's reader agent is a plugin agent, and Lite is in review. So adding `omitClaudeMd` means a new Lite version.
     - (amended 16 Nov 2026 *(Claude Code's note)*: the directory refused that key in Lite 2.2.4, and 2.2.5 removed it. See item 12.)
     - (amended 16 Nov 2026 *(Claude Code's note)*: `omitClaudeMd` and the run folders' `claudeMdExcludes` keep out different files, so neither replaces the other. The full edition already sets `omitClaudeMd` always. See item 12's corrections.)
   - **Decision:** ~~pending.~~ adopted by the researcher, 19 Nov 2026, narrowed as [decision brief (f)](decisions-pending-2026-11-17.md#f-formally-adopting-outside-review-7-items-1-to-10) suggests: `omitClaudeMd` and the read-only `tools` list apply to research copies and the full edition only, since the directory refused `omitClaudeMd` in Lite.
8. **Possible later arm:** a debate council run as an agent team, to test talking against independence.
   - **Checked** *(Claude Code's note)*: the agent teams page gives a debate as a use case: teammates "talk to each other to try to disprove each other's theories". But teammates load `CLAUDE.md`, MCP servers and skills like an ordinary session, start in the lead's permission mode, and need an interactive session. So the isolation would differ from a subagent council, and it would need its own dry run.
   - **The design** (my wording, 16 Nov 2026):
     - **Three arms, on the same material and seats:**
       - **independent seats:** current Lite;
       - **structured debate:** Lite's debate turns, relayed by the main session;
       - **free debate:** an agent team, whose teammates message each other directly.
     - **Measures:** catch rate, false flags, deviation rates and cost. Also anchoring signs, such as a finding raised by one seat and then adopted by others without independent evidence.
     - **Isolation for the team arm:** a separate run folder, with agent teams enabled (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) in its project settings only.
       - `SendMessage` stays allowed there, because teammates need it.
       - `crossSessionInbound` stays `refuse`.
       - `ListAgents` stays denied, if teams still work without it. A dry run checks that.
       - The scan logs teammate messages as expected. Any message to or from a session outside the team voids the run.
     - **Limits:** agent teams are experimental, use in-process mode on Windows, and can't be resumed. Pin the Claude Code version.
   - **Checked against the agent teams and cross-session messaging pages, 16 Nov 2026** *(Claude Code's note)*:
     - **Enabling:** right. The variable is set to `1` in the shell or in a settings file's `env`. A project settings `env` entry applies after user settings, so the team folder's own settings can turn teams on there and leave every other folder off. Teammates spawn only in an interactive session. With `-p`, a named subagent runs as an ordinary subagent.
     - **`SendMessage` must stay allowed:** right. The messaging page says denying `SendMessage` "also removes messaging to subagents and agent-team teammates, since the same tool serves both". An in-process teammate runs under the lead's live deny rules. So in the team arm the lead can also send to sessions outside the team, and only the scan would catch that.
     - **`crossSessionInbound` set to `refuse`:** the page says it drops messages "arriving from your other sessions". Neither page says it touches messages inside a team, which go through the team's mailbox files rather than the session's inbox. Nothing found says it blocks teammates. The dry run should confirm that teammates still receive messages with it set.
     - **`ListAgents`:** the teams page doesn't name it for teammates.
       - Teammates message each other by the names the lead gives them.
       - They can read the team config's member list.
       - `/list-agents` does list a session's own teammates, though.
       
       So teams may work without it. That's still for the dry run, as planned.
     - **"The same seats":** partly. A teammate can be spawned from a subagent definition such as Lite's `council-reader`.
       - **What it keeps:** that definition's `tools` (Read, Grep, Glob), plus `SendMessage`, added for every in-process teammate even if the definition leaves it out. In a session that has the Task tools, it also gets those.
       - **The definition's body:** appended to the teammate's default system prompt, where a subagent uses the body alone.
       - **The definition's `skills`:** not applied. The teammate loads skills, `CLAUDE.md` and MCP servers from the project and user settings like an ordinary session. When the lead starts with `--setting-sources`, it uses the same restricted sources.
       
       So a teammate seat also differs from a subagent seat in its system prompt and loaded context, not only in messaging. The comparison should record this.
     - **Where teammate messages are recorded:** each agent's mailbox is a JSON file at `~/.claude/teams/{team-name}/inboxes/{agent-name}.json`. Claude Code removes the team config directory when the session ends, and the mailboxes sit inside it, so they probably go too. The task list (`~/.claude/tasks/{team-name}/`) stays. The docs don't say where a teammate's transcript is kept, or whether its messages appear there. So the dry run should find where the scan can see teammate messages. The records rule (copy into `runs\` before scanning) may need to copy the mailbox files before the session ends.
     - **"In-process mode on Windows":** partly right. In-process is the default display mode in every terminal. Split panes need tmux or iTerm2, which native Windows doesn't have, so in-process is what runs here. The docs don't name Windows.
     - **"Can't be resumed":** partly right. `/resume` and `/rewind` don't restore in-process teammates, so a resumed session has lost its team. Within one running session, Claude Code does bring back a teammate that stopped when it's messaged. So an interrupted team run can't be continued with its team. The plan should say, before the runs, what happens to such a run.
     - **Also from the docs:**
       - **Other arms:** while teams are on, any subagent Claude names launches as a teammate, so the other two arms need folders with teams off (`0`), as the current run folder has.
       - **Permission mode:** a teammate starts in the lead's permission mode.
       - **One team:** a session has one team, and teammates can't spawn teammates.
       - **Teammates' own subagents:** they run in the foreground.
       - **Cache:** an in-process teammate's prompt cache holds for 5 minutes by default, which matters for the cost measure.
     - **Version:** this machine has Claude Code 2.1.325, the version of all three runs so far.
       - (amended 17 Nov 2026 *(Claude Code's note)*: by the seed folder's rank-and-reviews report, 2.1.326 was installed on this machine at 22:23 UTC on 16 Nov, and this item was committed at 22:57 UTC (`883d422`). So the machine had 2.1.326 by then, though the session that wrote this was probably still running 2.1.325. 2.1.326 is still the latest release on 17 Nov, by npm.) The docs' version notes show team behaviour changing recently. For example, split-pane teammates loaded every settings source before 2.1.281. So pinning the version matters.
       - **A pinning option** (added 19 Nov 2026): npm's `stable` channel was 2.1.311 when `latest` was 2.1.326, on 17 Nov 2026, as the overnight audit recorded. Pinning the formal runs to `stable` would give a version that has been out longer. *(Claude Code's note)*: checked on npm at 19 Nov 2026. `stable` is still 2.1.311, published 26 Oct 2026, and `latest` is now 2.1.328. 2.1.326 was published on 16 Nov at 18:43 UTC and stayed `latest` until 2.1.327 at 20:33 UTC on 17 Nov. So `stable` lags `latest` by weeks. Whichever is chosen, the version is fixed in the locked plan and recorded per run, and the team-arm features noted above would need checking on 2.1.311.
     - **Recorded by** *(Claude Code's note)*: the seed folder's session wrote this down at the researcher's request. As the note at the top of this entry says, building the team arm's run folder, its settings and its dry run belongs to seed-free sessions.
   - **Decision:** adopted by the researcher, 16 Nov 2026.
9. **Possible human-in-the-loop experiment:** hand relay against cross-session messaging, comparing errors and leaks.
   - **Already recorded** *(Claude Code's note)*: the research doc has this idea under the misdirected prompt in "Voice-tag controlled test". It compares the same multi-session task relayed by hand and with the sessions messaging each other. This suggestion adds leaks as a measure.
   - **Decision:** ~~pending.~~ parked by the researcher, 19 Nov 2026, following [decision brief (f)](decisions-pending-2026-11-17.md#f-formally-adopting-outside-review-7-items-1-to-10): moved to the human-in-the-loop plan, section 6, as a linked experiment.
10. **Worktree note:** `isolation: worktree` starts from the default branch unless `worktree.baseRef` is `"head"`.
    - **Checked** *(Claude Code's note)*: the other value is `"fresh"`, the default, which branches from the remote's default branch. With no remote, it falls back to the local `HEAD`.
    - **Decision:** ~~pending.~~ adopted by the researcher, 19 Nov 2026, following [decision brief (f)](decisions-pending-2026-11-17.md#f-formally-adopting-outside-review-7-items-1-to-10), as a note for any run that uses worktrees.

### Added by me (16 Nov 2026)

11. **Research question for the workflow edition: how much freedom should the orchestration have?** ~~Lite gives the main session and the subagents more autonomy: they choose turn by turn, and the findings are free text. A workflow fixes the steps and the output form. The aim is to measure the differences, not to find the best setup. Freedom may help on fuzzy judgements (UI, design and interaction review), and fixed steps may help bug hunts stay consistent. This is a key part of the workflow comparison, measured by task type. Matching free-text findings to the key wasn't a large error source in the pilot (15 of 15 hand-checked matches were right), so differences are more likely in consistency and skipped steps than in scoring.~~ (amended 16 Nov 2026, reframed using Claude Code's corrections below:)
    - **The difference:** both editions fix the steps and the output format. What differs is how they're enforced.
      - **In Lite:** by instructions, with slips logged as deviations.
      - **In a workflow:** by the script, plus a runtime schema check wherever one is set.
    - **The aim** is to measure the differences, not to find the best setup.
    - **The expectation:** room to drift may help on fuzzy judgements (UI, design and interaction review), and enforcement may help bug hunts stay consistent.
    - **Measures, by task type:** deviation rates (skipped steps, reordered steps and count slips), alongside catch rates. This is a key part of the workflow comparison.
    - **Scoring:** no errors were found in a stratified sample of 15 of the pilot's matches. So differences are more likely in consistency and skipped steps than in scoring.
    - **Correction** *(Claude Code's note)*: Lite's steps and findings aren't free either. Its skill sets out every step in its step files, and briefs come from templates word for word. Reviewers report in a fixed format: numbered findings, each with a severity, title, file and line, evidence, fix and confidence. The difference is what holds these in place. In Lite it's instructions, and the main session logs any slips as deviations. In a workflow it's the script, and for an `agent()` call with a `schema`, JSON that the runtime checks. So the freedom being compared is the freedom to skip, reorder or drift, not a freedom designed in.
    - **Correction** *(Claude Code's note)*: the reviewers are subagents in both editions, so in a workflow they still choose their own reads and tool calls. What a workflow fixes is the orchestration. It fixes the output form only for calls that set a `schema`. Without one, an agent returns prose.
    - **Loose** *(Claude Code's note)*: the 15 were a stratified sample of the matches a Claude session made: 5 catches, 5 matches to known bugs and 5 close calls. Claude Code checked this against the seed folder's record. Finding no errors in 15 still allows an error rate of up to about 20%, by the rule of three (3 ÷ 15, at 95% confidence). So the claim holds only as "no errors found in a sample of 15". The research doc's pilot difficulty note still calls this check "still to do". (amended 16 Nov 2026: that note is now updated, and the hard tier's matching spot-check is still to do.)
    - **Connection** *(Claude Code's note)*: this widens the experiment idea already in the research doc under "Dynamic workflows: a scripted Council Dial". That idea measures copy errors, count mismatches, deviations, tokens and time. The same entry says that copying hasn't slipped in any Lite check so far. It also says both recorded count slips were in count lines the agents wrote themselves. That fits the expectation here. A workflow script would calculate those counts instead of an agent writing them.
    - **Limits on the counts** *(Claude Code's note)*:
      - A script can count only what it holds as data, so it needs schema output for those calls. From prose, it would still need an agent to count.
    - **What each edition's deviation rate means** *(Claude Code's note)*:
      - **In a workflow:** the script can't skip or reorder its own steps. So skipped and reordered steps there can come only from a bug in the script, or from agents skipping parts of their own briefs. Workflow-side slips to count instead: agents that return nothing (`null`, after a stop or an unrecoverable error), calls that still fail the schema check after five attempts, and stalled agents that restarted.
      - **In Lite:** its own deviation log undercounts (see "Self-reported deviations undercount" in the research doc). So its rate needs slips found afterwards as well as the ones logged, as the existing experiment idea already says.
    - **Task types** *(Claude Code's note)*: Lite is the read-only tier. It leaves out interaction capability on purpose, because judging that needs a running app (entry 2, seat roles decision 3). So in Lite, UI and interaction review is limited to what the code shows, such as error messages, settings and help text. A full test of interaction review waits for the full Council Dial's seat that reviews frames of the running app.
    - **Who acts on it** *(Claude Code's note)*: it shapes the workflow edition's design, so it belongs to seed-free sessions, like item 5.
    - **Decision:** adopted by the researcher, for the workflow edition comparison, on 16 Nov 2026.
12. **`omitClaudeMd` on reviewer seats.** Council Dial Lite 2.2.5 dropped `omitClaudeMd` from its reviewer agent for directory submission reasons. Run folders exclude `CLAUDE.md` through their settings instead, which the dry run confirmed. ~~The plan is to offer `omitClaudeMd` as an option only in the GitHub edition (full or research), and to compare seats with and without it on the same material, under controlled conditions.~~ (amended 16 Nov 2026: plan revised, see "Revised plan" below.) Every run record must state which version and setting it used.
    - **Checked** *(Claude Code's note)*: the reason is right.
      - The directory's automatic policy check refused Lite 2.2.4 (`7049778`) with `LOCAL_CODE_FRONTMATTER_KEY`. It accepts frontmatter keys outside its list only from Verified organisations.
      - Lite 2.2.5 (`de465aa`) removed the key and passed the check.
      - The agent is Lite's read-only agent, `council-reader`. In brief version 3 it runs every seat (reviewers, judge, appeal and check) unless running code is allowed.
    - **Correction** *(Claude Code's note)*: the run folders' settings don't replace it. They cover a different set of files.
      - **The run folders' setting, `claudeMdExcludes`:** keeps out `CLAUDE.md` files under the `material` folder, for the whole session.
      - **`omitClaudeMd`:** leaves out the user, project and local `CLAUDE.md` files, for that agent only. By the docs and Lite's README, it doesn't stop a subfolder's `CLAUDE.md` from loading when the agent reads files there.
      - **What keeps the other files out:** in the run folders, only the fact that there's no user, project or parent-folder `CLAUDE.md`, `CLAUDE.local.md` or `AGENTS.md`. Claude Code checked this on 16 Nov 2026.
      - **A subfolder `AGENTS.md`** (added 17 Nov 2026 *(Claude Code's note)*): the [memory page](https://code.claude.com/docs/en/memory) says Claude also reads "a subdirectory's `AGENTS.md`, when Claude opens a file there with the Read tool and that subdirectory has none of the three `CLAUDE.md` files of its own". The current run folder's exclusion patterns name `CLAUDE.md` only. The hard tier's material holds no `AGENTS.md` (by the seed folder's hard-tier prep report), so no run so far is affected. But material that holds one would need its own exclusion pattern, or a check.
    - **Correction** *(Claude Code's note)*: the dry run didn't confirm it. No `CLAUDE.md` loaded, but there was no control run without the exclusion. So the run doesn't show that the exclusion is what stopped it. The research doc says so under the dry run's "Not settled".
    - **Correction** *(Claude Code's note)*: the full edition already sets `omitClaudeMd: true` on its read-only agent, always, and has since Council Dial 1.8.0 (`4a92f9e`). Version 1.9.1 still does. So making it an option means changing the full edition.
    - **Lite's history** *(Claude Code's note, from its git log and changelog)*: no version has a tag or a GitHub release. Every version was pushed to main.
      - **With `omitClaudeMd`:** 2.2.0 (`3b7b74c`) to 2.2.4 (`7049778`), all on 11 Nov 2026.
      - **Without it:** every version up to 2.1.2, and 2.2.5, the version in review and the one the pilot used.
    - **Earlier runs with each** *(Claude Code's note)*:
      - **With it:**
        - the five installed-copy Standard councils, one on each version from 2.2.0 to 2.2.4. Each project's `CLAUDE.md` held a marker line, and none of their 35 agent transcripts contains it;
        - one session of the 2.2.0 marker test. Asked about the marker, the agent answered NONE.
      - **Without it:**
        - the marker test's other session, whose agent named the marker word;
        - every test council from Lite 1.0.0 to 2.1.2;
        - on 2.2.5, the dry run and the 8 pilot difficulty runs.
      - **No run:** the 2.2.5 installed-copy test folder holds a `CLAUDE.md` but no run.
    - **Not controlled, but partly for a different reason** *(Claude Code's note)*: some of these runs did review the same material. The 2.1.2 Standard council and the 2.2.0 and 2.2.1 installed-copy councils reviewed byte-identical copies of the same target. They still aren't a controlled comparison:
      - the Lite version and the way it was installed changed;
      - only the installed-copy projects held a `CLAUDE.md`;
      - each version had one run.
      
      The dry run and the pilot used other material. The marker test is the only like-for-like pair, and it had one run on each side and asked a probe question rather than running a review.
    - **What the comparison needs** *(Claude Code's note)*: the setting changes what an agent gets only when a user, project or local `CLAUDE.md` is there to leave out. Without one, both arms get the same context.
    - **Records** *(Claude Code's note)*: Lite's `run.json` records `liteVersion` but has no field for this setting, because the version implies it. An edition where the setting is an option needs a field for it.
    - **Who acts on it** *(Claude Code's note)*: it changes the council set-up, so it belongs to seed-free sessions and the full edition's repo.
    - **Revised plan: proposed, pending** (my wording, 16 Nov 2026):
      - **Why the old plan is dropped:** in run folders with no user, project or local `CLAUDE.md`, the two arms are identical, so that comparison measures nothing.
      - **The real-world question instead:** does letting every seat read the reviewed project's `CLAUDE.md` help (context) or hurt (bias)?
      - **The arms:** a research copy of Lite 2.2.5 with `omitClaudeMd` and one without it, on material that includes a realistic project `CLAUDE.md`.
      - **Who designs that file:** seed-free sessions design it, never the seed folder's sessions.
      - **Background:**
        - the full edition already sets `omitClaudeMd` always, and has since 1.8.0;
        - the marker-test pair shows the setting works, but with one run each way it isn't an effect size;
        - `run.json` needs a field recording the setting.
      - **Checked** *(Claude Code's note)*: "identical" holds by the docs, for the `CLAUDE.md` files these settings cover. The marker test ran on Claude Code 2.1.322, and this machine now has 2.1.325, so the setting should be checked again on the version the runs pin. The 35 installed-copy transcripts back it up, but they had no arm without the setting.
      - **Where the `CLAUDE.md` has to sit** *(Claude Code's note)*: the arms differ only if the file loads as the session's own project file, from its start folder or a folder above it, as when someone starts Claude Code in their own project.
        - In the current run folders, each material item sits in a subfolder under `material`, so its `CLAUDE.md` would be a subfolder file.
        - `claudeMdExcludes` keeps that out of the whole session.
        - Without the exclusion, the file would load whenever an agent read files beside it, in both arms, because `omitClaudeMd` doesn't stop subfolder files.
        - So this test needs a different run-folder layout, with the `CLAUDE.md` at the project level and not covered by the exclusion.
      - **The main session** *(Claude Code's note)*: `omitClaudeMd` applies only to the agent, so the main session loads the file in both arms. Since 2.2.1, Lite also names any line addressed to the council in its plan and asks the user. So the material's `CLAUDE.md` should hold no such line, unless that's what's being tested.
      - **Labels** *(Claude Code's note)*: both copies would report `liteVersion` 2.2.5, and Lite groups runs by a label that includes the version. So without the new field the two arms' runs would be estimated and compared together. The research copy must also stay off Lite's main while it's in review.
    - **Decision:** ~~adopted by the researcher, on 16 Nov 2026.~~ (amended 16 Nov 2026: the record rule, that every run record states the version and setting it used, stays adopted by the researcher, on 16 Nov 2026. The comparison is replaced by the revised plan, which is proposed, pending.) (amended 19 Nov 2026: the revised comparison is decided by the research doc's decision (e), following [brief (e)](decisions-pending-2026-11-17.md#e-whether-to-run-the-claudemd-help-or-bias-test-and-how): the `CLAUDE.md` test is a secondary experiment after the plan is locked, testing the bias side first, an accurate file against a misleading one, with a random-file control. Adopted by the researcher.)

---

**Decisions:** ~~all pending.~~ Items 1 to 10 are pending. Item 11 was adopted by me on 16 Nov 2026. (amended 16 Nov 2026: item 11 added) Item 12 was adopted by me on 16 Nov 2026. (amended 16 Nov 2026: item 12 added) (amended again 16 Nov 2026: item 12's record rule is adopted, and its revised comparison is pending. Item 5's interrupted-run rule is proposed, pending.) (amended again 16 Nov 2026: item 8, the debate council as an agent team, is adopted by me on 16 Nov 2026, with its design written out under the item. Items 1 to 7, 9 and 10 are pending.) (amended 19 Nov 2026: items 1 to 4, 6 and 10 are adopted by me, item 5 is adopted together with the interrupted-run rule, item 7 is adopted narrowed to research copies and the full edition, and item 9 is parked in the human-in-the-loop plan, all following decision brief (f). Item 12's revised comparison is settled by decision (e). No item of this entry is pending.)


---

## Outside review 8: experiment ideas from the 17 Nov literature sweep

- **Date:** 17 Nov 2026, logged here on 18 Nov 2026.
- **Reviewer:** the overnight literature sweep session, Claude (a Claude Code session with seven research subagents). It is **not independent**: it is the same model family as the councils, it was briefed from this repo's docs, and it read the experiment plan before suggesting changes to it.
- **Material:** the sweep's follow-ups of every source in [prior-work-research.md](prior-work-research.md) and its new searches on eleven topics. The work each idea comes from is named in brackets after it.
- **Source:** the section "Experiment ideas the literature suggests (suggestions only)" in [research/sweep-2026-11-17.md](../research/sweep-2026-11-17.md#experiment-ideas-the-literature-suggests-suggestions-only). The sweep says: "These are suggestions from the literature, not decisions. None has been added to the plan."
- **Record:** all 35 ideas, in the sweep's order and grouping, each waiting for my decision. Nothing from them is in the research doc. The papers they cite are entered in [prior-work-research.md](prior-work-research.md), in full or as one-line notes in its section 8.
- **Who acts on them** *(Claude Code's note)*: many of these change the council set-up, the briefs or the seeds. Only the sessions allowed to make each kind of change may act on them: see "Seed-aware and seed-free sessions" in the research doc.

### Suggestions (decision pending)

**The appeal and the judge**

1. **A "burden of proof" judge arm as a rival to the appeal.** The judge may dismiss a finding only with a concrete refutation, not because it's unsure. Compare it with the current judge plus appeal on recall, precision and tokens. (Kodus, where this change "roughly doubled delivered recall"; Unblocked; VulnSAGE.)
   - **Decision:** pending.
2. **Claim-by-claim verification.** The judge checks each finding in a separate call and is shown which claims were refuted. Compare it with one call over all findings. (Trusting the Tool, +12 points under false assurances.)
   - **Decision:** pending.
3. **Blind the appeal to the judge's reasons.** One arm gives the appeal the judge's dismissal reasons, as now. The other gives it only the dismissed findings and the code. (Grounded but Not Immune, where one authority note overturned up to 40% of correct verdicts; Silent Dissent.)
   - **Decision:** pending.
4. **A cheap appeal baseline: rerun the same judge.** Run the same judge again, independently, on the dismissed set, or "keep if the judge's runs disagree". Compare it with the appeal agent. (Figalová et al., where two identical runs differed on 29 eligible records; Klieber et al.'s consistency check.)
   - **Decision:** pending.
5. **Report "recoverable headroom" directly:**
   - seeds that at least one seat raised but the judge dropped;
   - the share the appeal wins back;
   - separately, how often a reinstated finding's severity is then right.

   (When Debate Helps, on proposal supply and read-out; Detection Without Correction, on detecting an error against fixing it.)
   - **Decision:** pending.
6. **Re-file instead of dismiss.** Let the judge move a finding to the seat whose scope it fits, rather than rule it a false alarm. (*The More the Better?*, where many of the team's false alarms were true defects under another seat's requirement.)
   - **Decision:** pending.
7. **A matching rule for near misses, fixed in advance.** Decide whether a finding in the right file with the wrong mechanism is a hit, a partial hit or a miss, and let the appeal contest such rulings. (SecPRBench's 68%.)
   - **Decision:** pending.
8. **A judge-swap check on the keep rule.** Re-score a sample of parent-against-child comparisons with a second judge model, to see whether keep decisions survive. (Swapping the Judge Changes the Ranking, where rankings didn't survive a change of judge.)
   - **Decision:** pending.
9. **Report what the judge drops by bug class.** (Sifting the Noise, where losses ranged from 0.41% to 84.50% depending on the CWE.)
   - **Decision:** pending.

**Seats, diversity and debate**

10. **An effective number of independent seats.** Estimate pairwise error correlation between seats and judges (double faults on seeds), and report n_eff alongside council size. (Agreement Overstates Evidence; the capability-controlled diversity audit, arXiv 2607.20768.)
    - **Decision:** pending.
11. **A "sample the generalist three times, flag on any draw" arm** at equal tokens, alongside the existing baseline that reruns one reviewer. (*The More the Better?*, where it beat the split team.)
    - **Decision:** pending.
    - *(Claude Code's note)*: a recheck of that paper on 18 Nov 2026 found this result is exploratory, on balanced accuracy, and shown for its two Claude models only.
12. **For the debate arm:**
    - give the judge and the appeal the findings from before the debate as well as after it;
    - add a matched "re-think alone" control, so that changes after debate aren't all credited to debate.

    (Unanimity Without Persuasion; Not All Flips Are Conformity.)
    - **Decision:** pending.
13. **Effort and agreement.** Measure whether raising seat effort makes seats agree more than accuracy explains, since that would cancel some of a mixed council's diversity. (Does Reasoning Make Language Models Agree?)
    - **Decision:** pending.
14. **Check what "mixed family" means.** Before treating a non-Claude model as independent, check whether it is known or reported to be distilled from Claude. (Exposing Vulnerability Monoculture, on lower systemic robustness in pools distilled from Claude Opus 4.6.)
    - **Decision:** pending.
15. **Report the strongest single reviewer alone,** not only the gain over the author or over same-model pairs, since cross-model "review" gains can be capability transfer from the stronger model. (Review Rarely Beats the Stronger Model; the Song 2026 qualification.)
    - **Decision:** pending.
16. **A judge-quality null for the self-preference analysis.** Compare a judge's rulings on its own family's findings with its rulings on others', not with a fixed standard. (Are LLM Evaluators Really Narcissists?, where only 51% of earlier significant cases survived this control.)
    - **Decision:** pending.
17. **Randomise or fix seat order in the sequential arm,** and log it. (When Order Matters, where a stronger model placed after weaker ones lost much of its advantage.)
    - **Decision:** pending.
18. **Check how the judge counts restated findings.** Test whether a bug that several seats restate gets more weight than one independent reading would justify. (Copies or Sources?, where a forwarded copy counted for 0.06 to 0.42 of a new reading.)
    - **Decision:** pending.
19. **Run the official `code-review` plugin and OpenCodeReview's Claude Code plugin as named outside arms** next to `/code-review ultra`, since both run on Claude and can be inspected. (The plugin's README; OpenCodeReview's README.)
    - **Decision:** pending.

**Seeds and contamination**

20. **FeatAdd-style Claude seeds.** Claude adds a feature to a test app, and regressions the tests catch become seeds, so the planter isn't choosing where bugs go. Tag them separately from seeds planted on purpose. (BugPilot.)
    - **Decision:** pending.
21. **A seed validity check:**
    - a seed must pass the app's existing tests but fail a stronger oracle;
    - drop seeds that an equivalent-mutant check says change nothing.

    (Test-aware mutant generation, arXiv 2609.35841; Meta ACH.)
    - **Decision:** pending.
22. **Seeds at random sites against seeds at sites Claude chooses,** to measure whether a Claude planter's placement makes seeds easier or harder for Claude reviewers. (BugFarm, which steers bugs to where a detector looks least.)
    - **Decision:** pending.
23. **Escaped bugs:**
    - trace them with an agentic SZZ, and record agreement with a classic SZZ or a non-Claude tracer, so that seed choice doesn't depend only on Claude;
    - add escaped bugs from `Fixes:` tags and reverts, where the projects use those conventions;
    - record the labelling strategy for each seed.

    (Kondo et al.; Risse and Böhme; AgentSZZ; ReDef; One Strategy Does Not Fit All.)
    - **Decision:** pending.
24. **Cheap contamination probes on candidate seeds:**
    - can Claude name the buggy file from the PR title alone?
    - do independent sessions give suspiciously uniform answers?
    - in each case, compare against matched controls from the same repository.

    (SWE-Bench-Verified memory study, arXiv 2512.10218; Cross-Context Verification, arXiv 2603.21454; the measurement-first audit, arXiv 2610.05830.)
    - **Decision:** pending.
25. **Neutral PR descriptions for seeds, plus an arm with the metadata removed.** Descriptions can leak the bug (SWE-Bench+) or hide it (When AI Agrees Too Much, where removing PR metadata restored detection in all affected cases).
    - **Decision:** pending.

**The evolution loop**

26. **Canary seeds and key isolation.** Plant a seed whose key entry can't be inferred from the code, so that "finding" it signals leakage. Keep the key off any path a reviewer or mutation proposer can read. (PROCTOR; the Meta-Agent Challenge's "ground-truth exfiltration".)
    - **Decision:** pending.
27. **A final held-out set that no keep decision ever reads,** plus a winner's-curse correction, or a re-score on fresh seeds, for kept children when several compete on the same seeds. (SIREN; Anthropic's hillclimb recipe, which consults its test set in every keep decision.)
    - **Decision:** pending.
28. **Track brief length across generations, and check for "phantom" rules** added for failures that never happened. (TextReg; Phantom Guardrails.)
    - **Decision:** pending.
29. **Replicate whole evolution runs,** not just evaluations, since the design process itself varies a lot between runs. (Meta-Agent Challenge; *Auditing the Product, Not the Recursion*, arXiv 2610.27610, where only 22% of self-improvement studies audited two or more reruns of the full loop.)
    - **Decision:** pending.
30. **An error budget across generations** for the keep rule, so that the chance of keeping at least one spurious change over the whole run is bounded, not just per comparison. (SGM.)
    - **Decision:** pending.
31. **A majority-vote and random-search baseline in every generation,** plus a check that evolved councils haven't degenerated into "the same generalist three times". (The Illusion of Multi-Agent Advantage, on AFlow's "Degeneration to Trivial Ensembles"; Simple Baselines are Competitive with Code Evolution.)
    - **Decision:** pending.
32. **Three outcomes for each generation:** advance, reject or "inconclusive, run more seeds", with a sequential stopping test. (AgentAssay. The evidence is weak: it's single-author and unreviewed.)
    - **Decision:** pending.

**`CLAUDE.md`, orchestration and human cost**

33. **`CLAUDE.md` conditions:**
    - none;
    - real;
    - a placebo of the same length (irrelevant or shuffled);
    - stale or wrong.

    In each, measure false alarms and misses separately, and check with a canary string that the "none" condition really excludes the file. (Guardrails Beat Guidance; Stale Instruction Files; the Claude Code subagents page on `omitClaudeMd` and nested files.)
    - **Decision:** pending.
    - *(Claude Code's note)*: outside review 7's item 12 already covers the with-and-without comparison and where the `CLAUDE.md` has to sit. This idea adds the placebo and stale conditions, and the canary.
34. **Scripted against agent-led, done as the COBOL study did it:**
    - hold models, briefs and tools fixed, and vary only who controls execution;
    - report the mean score, run-to-run variance, worst case and tokens;
    - log over-spawning and duplicated work in the agent-led arm;
    - account for workflow prompt-cache sharing when comparing costs.

    (Deterministic vs. LLM-Controlled Orchestration; Anthropic's multi-agent research post; the workflows docs.)
    - **Decision:** pending.
    - *(Claude Code's note)*: this bears on outside review 7's item 11, the workflow edition comparison.
35. **A human-cost proxy in the final report:** the findings shown to a person per run, and an estimated triage time per finding, so that volume counts against a council. (Beko, where PR closure time rose from 5h52m to 8h20m; Meta's randomised trial, where reviewers were over 5% slower; Habituation at the Gate.)
    - **Decision:** pending.

---

**Decisions:** all 35 pending.
