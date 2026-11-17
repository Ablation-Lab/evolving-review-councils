# Decisions pending, 17 Nov 2026

Seven open decisions, each set out for the researcher to make. Claude Code prepared these briefs overnight on 17 Nov 2026 from the research doc, the outside reviews, the prior-work file, the human-in-the-loop plan, the paper's fix list and the seed folder's seed-free reports. It decided nothing. Each section gives the options, the evidence already on file, the risks, what the decision needs, and a suggestion, marked as one.

Sources used, all seed-free:
- [experiment-plan.md](experiment-plan.md), the research doc, mostly its notes from 13 to 17 Nov under [What checked the research doc, and what it missed](experiment-plan.md#what-checked-the-research-doc-and-what-it-missed-12-nov-2026);
- [outside-reviews.md](outside-reviews.md), especially [outside review 7](outside-reviews.md#outside-review-7-claude-code-agent-features-eight-pages-read-16-nov-2026);
- [prior-work-research.md](prior-work-research.md), including its new section 7 (2026 additions, 17 Nov 2026);
- the [human-in-the-loop plan](https://github.com/Ablation-Lab/human-in-the-loop/blob/main/plan.md);
- the seed folder's seed-free reports, named by file (`reports\...`), which aren't public.

Where these briefs say "the docs", they mean Claude Code's docs as read on 17 Nov 2026, on Claude Code 2.1.326.

---

## (a) How to make the material harder

**The question:** both tiers were too easy for the comparison as planned. What changes before the real runs: the material, the measure, or both?

**The options:**
1. **No diff (lever (a) in the research doc):** give the code after the change plus the modules around it, with no diff.
2. **Put the surrounding project back:** the real project at the introducing commit, or a larger real pull request.
3. **Drop the one-line description.**
4. **Rank-first as a main measure:** keep the material and score whether the seed is the top finding (and in the top 3).
5. **Other precision measures (lever (b)):** extras per catch, and scoring the output after the judge where there is one.
6. **A mix** of the above.

**The evidence on file:**
- **Catches are saturated in both tiers.** Easy tier: 10 of 10 seeds, single reviewers 25 of 30 pairs. Hard tier: 10 of 10, all 6 HIGH, single reviewers 29 of 30. Both are in the too-easy band fixed in advance ("The pilot difficulty check" and "The hard-tier difficulty check" in the research doc; `reports\difficulty-results.md` and `reports\difficulty-hard-results.md`).
- **The diff points straight at the seed.** In all 10 hard folders the diff contains the seeded lines, and in 9 every seeded line was added or rewritten by the change ("The material's size"; `reports\hard-material-size.md`).
- **The material is a small slice of the project:** a median of about 1 file in 196 and 1 line in 22. The median project has 1,436 files and 61,143 lines of code (same report). So option 2 means far more reading per seat.
- **Rank isn't saturated.** The seed was the top finding in 17 of 29 catches (59%), in the top 3 in 25 (86%) ("Rank rescore and human reviews"; `reports\hard-rank-and-reviews.md`). But the lists are sorted by severity, so rank-first partly measures the reviewers' severity calls. Applying the difficulty bands to rank was chosen after seeing the figures.
- **Noise is large.** 238 unconfirmed extras across the 10 hard folders (88% of 272 findings), 8.2 extras per catch overall, and a median of 6 per catching list.
- **The human reviewers had the diff.** Every introducing change was a merged pull request reviewed by someone other than its author, a median of 2 review submissions from 1 reviewer. So with no diff, a council's task is harder than the one the humans failed at, and the comparison with their miss weakens (the Claude Code note under lever (a)).
- **An accidental data point:** Ultrareview's run 2 reviewed every file whole, with no diff, and still caught its seed. That's one run, on another system, and it had only the material's files, not the modules around them ("The Ultrareview baseline").
- **The description:** Ultrareview never got it and still caught 2 of 3. Neither seed-folder report says the description helped. The research doc records that the report suggests dropping the diff, where the researcher suggested dropping the description ("Open decision, pending").
- **Prior work (section 7 of the prior-work file):** CRBugBench scores recall in the top 5 comments, the nearest published analogue to rank-first. SWE-PRBench found all 8 models got worse as context grew, which bears on option 2. Zietsman warns that hints leak through context such as docstrings and unused imports.

**The risks:**
- **Option 1** changes what's being compared with the humans, and it may push catches below the band's floor. A drop to 0 or 1 of 10 is as useless as 10 of 10.
- **Option 2** multiplies tokens per seat and may hit context limits. It's the most realistic option and the most expensive.
- **Option 3** is cheap, but the evidence suggests it will change little. If it's mixed with another lever in one check, the effects can't be told apart.
- **Option 4** rests on a band applied after the figures were seen. It must be fixed in the locked plan before the formal runs, as decided on 17 Nov, or it becomes a post-hoc measure.
- **Option 5** needs the extras checked, since on the easy tier all 20 sampled extras were real problems ("The extras sample"). Counting extras as noise would then penalise the best reviewers (outside review 1, B5).

**What the decision needs:**
- whether a council's catch should stay comparable with the human reviewers' miss;
- the budget for option 2;
- whether to run one more difficulty check, with bands fixed first, before choosing;
- the hand-check packs in (g), which settle how far the extras and the matches can be trusted.

**Suggestion (Claude Code's, not a decision):** a mix, in two steps.
1. **Now, before any formal run:** fix rank-first (top 1 and top 3) and extras per catch in the locked plan as main precision measures alongside catches, scored after the judge where there is one. Report extras in three groups, as real, false or unchecked, from a hand-checked sample.
2. **Then, one difficulty check on option 1 alone:** the 10 hard folders as the code after the change plus the modules around them, with no diff and the description unchanged. Use a fresh session and the same bands, fixed before the run. If catches land in the workable band, use it as the harder tier. Leave option 2 until the cost of one folder is measured, and leave option 3 out, so there's one change per check.

---

## (b) The messaging rule

**The question:** the proposed run rule says any `SendMessage` or `ListAgents` call in a run is logged as a deviation, and a message that carries content into or out of a run session or seat voids the run ("A proposed run rule" under "The messaging check" in the research doc). Adopt it, change it or drop it?

**The options:**
1. **Adopt as proposed:** a call is a deviation, and only a message that carried content voids.
2. **Stricter:** any delivered message voids, whatever it carried. Refused calls and refused deliveries are logged as deviations.
3. **Looser:** log everything, void nothing, and report runs with messages separately.

**The evidence on file:**
- **Nothing has happened yet in a run.** The dry run, review A and review B had 0 messaging calls and 0 incoming messages, and all 76 seats were Lite's read-only agent, without either tool. Their main sessions had both tools and called neither (`reports\messaging-check.md`).
- **Outside the runs, it has happened.** Two calls ran in development sessions, each from a main session to its own subagent. One sent a reviewer "No action needed; continue your review." while it was still working. The human-in-the-loop plan records this as an instruction no brief contained reaching a reviewer mid-review ("Messages that didn't go through me").
- **The current run folder blocks it.** Its project settings deny `SendMessage` and `ListAgents` and set `crossSessionInbound` to `refuse`, and the canary's message was refused. Checked again in the settings file on 17 Nov.
- **The docs:** a deny on `SendMessage` "also removes messaging to subagents and agent-team teammates". A `refuse` in project or local settings "applies over every other source". A refusing session shows no change in `/status`, so the settings files are the record.
- **The scan already reports it.** A received message is stored as a user turn from a peer. Subagent hand-backs use the same channel and are listed apart (79 of them, none in the runs).
- **The team arm needs messaging.** Outside review 7's item 8, adopted on 16 Nov, keeps `SendMessage` allowed in the team folder. Teammate messages are logged as expected, and any message to or from a session outside the team voids the run.

**The risks:**
- **"Carried content" needs a definition,** or it becomes a judgement made after the run. Does a 39-character "continue your review" carry content? It carried an instruction but no material.
- **Option 2** could void a run over a harmless notice. With the denies and the `refuse` in place, a delivered message should be very rare, so the cost is small.
- **Option 3** leaves contaminated runs in the data.
- **Still to check:** whether Lite completes with the `SendMessage` deny. Lite names neither tool, but it hasn't run under the deny yet.

**What the decision needs:**
- a definition of "content" if option 1 is kept;
- whether a refused inbound message, which no run tool called, counts as anything;
- the team arm's carve-out written into the same rule;
- a dry run confirming Lite completes with the deny.

**Suggestion (Claude Code's, not a decision):** option 2, with three definitions, so nothing is left to judgement after a run:
- **Deviation:** any `SendMessage` or `ListAgents` call by a run session or seat, whether it ran or was refused.
- **Void:** any message delivered into or out of a run session or seat, except a subagent's hand-back to its own main session and, in the team arm only, messages between that team's members.
- **Logged, not void:** a delivery that `crossSessionInbound` refused.

Then confirm, in a short dry run, that Lite completes with the deny before the first real run.

---

## (c) One fresh session per review in the formal runs

**The question:** both difficulty checks ran all their reviews in one session (8 in review A, 10 in review B). Should each review in the formal runs get its own fresh session?

**The options:**
1. **One fresh session per review.**
2. **One session per configuration,** with the reviews in a random order, and a check for carry-over.
3. **One session per batch,** as in the difficulty checks.

**The evidence on file:**
- **The plan already says so.** "Keeping the tests unbiased" in the research doc: "**Fresh start per run:** run each test in its own new chat or session, with no memory of earlier runs and no hint of the result we're hoping for." The difficulty checks departed from that, and neither the research doc nor the seed-free reports record the choice as a deviation. The seed folder's own plans weren't read for these briefs. They were checks, not results, so nothing was invalidated.
- **What carries over in one session is the main session's context.** Seats are fresh subagents each time, since the docs say "each subagent invocation creates a new instance". But the main session writes the plan, saves the reports, writes the overview and, in Quick, checks each pooled finding itself, all after seeing every earlier review's material and findings. That's the channel the research doc's open question "Should the main session stay blind to the material?" is about.
- **The briefs are a narrow channel.** They're built word for word from templates and checked, and the description was fixed word for word in `RUN.md`. So carry-over would show mainly in the main session's own words and checks, not in what seats are handed.
- **Long sessions bring their own risks:**
  - after a compaction, only the first 5,000 tokens of a skill are re-attached, and a compaction during a run is still untested ("How big is Lite's SKILL.md?" and the Lite 2.0.0 notes);
  - the hard tier's scan exception came from the run session's own test in its scratchpad, in a long session ("A post-hoc exception").
- **Prior work:** Mazaheri and Mazaheri found that an earlier episode in context shifts a verifier's threshold (prior-work file, section 7). That's an argument for fresh context, though not about review.
- **More sessions means more hand steps.** The human-in-the-loop notes from 17 Nov record three slips at hand-run steps: a template block to repeat, a placeholder typed in, and a silent failure behind redirected output.

**The risks:**
- **Option 1** costs more start-up tokens and more launches by hand, which means more chances for a relay slip, unless the launches are scripted.
- **Option 2** keeps carry-over inside each configuration. It's measurable, but it adds a confound to every comparison.
- **Option 3** breaks the plan's own rule, and any order effect can't be separated from the configuration.

**What the decision needs:**
- whether the formal runs are interactive, since Lite asks for a yes on its plan and teams need an interactive session, or could be headless;
- whether the per-session checks (canary, `/mcp`, the skills list) run once per batch or once per session;
- how a launch is recorded, such as each session's ID in the run record.

**Suggestion (Claude Code's, not a decision):** option 1, which follows the plan as written.
- Run the canary and the environment checks once per batch, in a throwaway session from the same launch line.
- Give each review a launch file with every command written out in full with its own values, never a block to repeat or a placeholder, as fixes (a) and (c) in the 17 Nov human-in-the-loop notes say.
- Record each session's ID against its review.
- Log the difficulty checks' single sessions as a departure from "Fresh start per run", for the record.

---

## (d) The interrupted workflow run rule

**The question:** outside review 7's item 5 proposes this for the workflow edition. If a run is interrupted and finished by a relaunch, it counts as one run if the script wasn't edited, with the run ID and the reason logged. If the script was edited between launches, the run is void. Adopt it, change it or replace it?

**The options:**
1. **Adopt as proposed.**
2. **Adopt with limits:** count it as one run only after a technical interruption, cap the relaunches, and log which agents ran again.
3. **Void every interrupted run** and start a fresh one.

**The evidence on file (outside review 7, item 5, and the docs re-read on 17 Nov):**
- **A relaunch can rerun finished agents.** A failed agent "runs again, and so does every agent the script starts after it, even ones that completed". An agent whose output differs from its first try also makes every later agent run again. So a run counted as one may hold second attempts.
- **Stalled agents restart automatically,** "at most five times", inside the same run. These aren't relaunches, but they cost tokens.
- **Usage limits:** a run pauses at a usage limit only in an interactive session. In `-p`, the Agent SDK, a background or a teammate session, the agent fails, and a relaunch is needed to finish.
- **Run IDs:** `resumeFromRunId` and the output's `runId` are now documented on the Agent SDK reference. The docs still don't say whether a relaunch returns the same `runId`.
- **A recent fix:** the 2.1.326 changelog, as the docs check read it, fixes workflow resume telling Claude "every finished agent would be reused after a call failed". Claude is now told how many results were reused and where reuse stopped. That's from a subagent's reading of the changelog, not rechecked here.
- **Lite has no such rule.** Interrupted Lite runs so far were handled case by case, such as the 2.2.3 test's second try ("Process and design notes from the Lite 2.2.3 installed-copy test").

**The risks:**
- **A stop after seeing output.** If the researcher stops a run after seeing partial results and then relaunches, the counted run carries a choice made after seeing results. Option 1 doesn't separate that from a crash.
- **Relaunches until success.** With no cap, a run can be relaunched until it completes, which is a form of selection.
- **"Edited" needs defining.** Does a changed argument count, or only a changed script file?
- **Option 3** wastes the finished agents' tokens and may void many runs if usage limits bite.

**What the decision needs:**
- the definition of a technical interruption (a usage limit, an API error, a crash, a closed session) against a stop by the researcher;
- a cap on relaunches;
- what the run record must hold: every run ID, which agents re-ran (from `/workflows`), the Claude Code version and the reason.

**Suggestion (Claude Code's, not a decision):** option 2.
- Count a relaunched run as one only after a technical interruption, with at most one relaunch.
- A stop by the researcher, a second relaunch or any change to the script or its arguments voids the run, and it's redone as a fresh run.
- Log every run ID, the agents that re-ran and why.
- Fix this in the plan before the first workflow run, as item 5 already says.

---

## (e) Whether to run the CLAUDE.md help-or-bias test, and how

**The question:** outside review 7's item 12 replaced the old comparison with a revised plan, proposed and pending: does letting every seat read the reviewed project's `CLAUDE.md` help (context) or hurt (bias)? Run it now, later or not at all? And in what design?

**The options:**
1. **Park it** until the main comparison is locked and running.
2. **Run it as item 12 proposes:** a research copy of Lite 2.2.5 with `omitClaudeMd` against one without it, on material with a realistic project `CLAUDE.md`.
3. **A wider design:** several kinds of file (none, accurate, misleading and random), each with seats that see it and seats that don't.

**The evidence on file:**
- **Item 12's own notes:**
  - the arms differ only if the file loads as the session's own project file, at the project level and not under the `material` exclusion, which needs a different run-folder layout;
  - the main session loads the file in both arms;
  - since 2.2.1, Lite names any line addressed to the council and asks the user;
  - both copies would report `liteVersion` 2.2.5, so `run.json` needs a new field;
  - the research copy must stay off Lite's main while it's in review.
- **The only like-for-like data:** the 2.2.0 marker test, one run on each side, on Claude Code 2.1.322. It shows the setting works, not how big any effect is.
- **A docs point found on 17 Nov:** a subfolder `AGENTS.md` also loads on demand when a file beside it is read, and the run folder's exclusion patterns name only `CLAUDE.md` (amendment under item 12).
- **Prior work (section 7 of the prior-work file), all on coding agents, not reviewers:**
  - **Evaluating AGENTS.md:** context files don't generally improve success, and add over 20% to cost.
  - **Stale Instruction Files:** 90.1% of choices followed a stale file over the code, and Claude Code named the conflict in 79 of 80 runs and followed the file anyway.
  - **Guardrails Beat Guidance:** random rules helped as much as curated ones, so the gain looks like priming.
  - **Khatri:** 120 to 200 tasks are needed to detect a 10-point effect.
- **The ceiling doesn't block the bias side.** A misleading file is expected to *lower* catches, so even the too-easy material can show a drop. The help side can't be seen on saturated material.

**The risks:**
- **Seed leaks.** A file that describes the project could hint at the seeds. Item 12 already says seed-free sessions design it, and the seed folder's sessions never do.
- **Power:** at the sizes in the prior work, a small pilot shows only large effects.
- **Scope creep:** the test touches the run-folder layout, a new `run.json` field and a research copy of Lite, all while Lite is in review.
- **The design:** without a random-file control, any gain could be priming, as Guardrails found.

**What the decision needs:**
- the priority against the main comparison;
- which material, since the seeds so far are pilot-only;
- whether the misleading-file arm is in;
- the Claude Code version to pin, and a check of the setting on it.

**Suggestion (Claude Code's, not a decision):** run it, but as a pre-registered secondary experiment after the main plan is locked, and in design 3.
- **The bias side first:** an accurate file against a subtly misleading one that would excuse a seeded bug's pattern, each with seats that see it and seats that don't.
- **A random-content file** as the priming control.
- **A pilot on pilot-only folders** to size it. It can show a drop in catches even on easy material.
- **Fix the `run.json` field, the folder layout and an `AGENTS.md` check before any run.**

---

## (f) Formally adopting outside review 7, items 1 to 10

**A correction to the question:** item 8, the debate council as an agent team, was already adopted by the researcher on 16 Nov 2026, with its design written out. So the items still pending are 1 to 7, 9 and 10 (the Decisions line of [outside review 7](outside-reviews.md#outside-review-7-claude-code-agent-features-eight-pages-read-16-nov-2026)).

**The options:** adopt all the pending items together, adopt each one on its own, or adopt some and park the rest.

**Each item, its state and the suggestion (Claude Code's, not a decision):**

| Item | What it asks | State on 17 Nov 2026 | Suggestion |
|---|---|---|---|
| 1. Cross-session messaging | `crossSessionInbound` set to `refuse`, and denies on `SendMessage` and `ListAgents`, confirmed from the settings file | All three are in the current run folder's settings. Still to check: Lite completes with the deny | Adopt, with that dry run, and decide (b) |
| 2. Agent teams | Teams off (`0`) in the run project, and `CLAUDE_CODE_DISABLE_WORKFLOWS=1` on the launch line | Both in place: the `0` in the settings, the variable in `RUN.md`'s launch line. The docs say local settings can turn teams back on over a project `0`, and the folder has a local settings file that wasn't read | Adopt, and check the local settings file |
| 3. Transcript scan | A messaging call or a delivered message means the run isn't CLEAN | The scan checks the stored form and lists hand-backs apart. Not yet tried on a transcript holding a delivered message from another session | Adopt, after one test with a delivered message in a throwaway pair of sessions |
| 4. Records | Copy subagent transcripts and workflow results into each run record | The `runs\` rule covers the three runs. The run folder now sets `cleanupPeriodDays` to 365. The docs say a session that leaves out user settings, with no other source for the key, skips the sweep | Adopt. Also set `cleanupPeriodDays` in every new run folder, and copy team mailbox files before a team session ends |
| 5. Workflow edition design | One workflow per stage, schema-checked findings, fresh runs only | Not built. The interrupted-run rule is (d) | Adopt the design, and decide (d) |
| 6. Cost measure | Record input, cache-read, cache-write and output tokens separately, with `/workflows` as a third figure | Not built. Outside review 1's B1, one cost measure, is still undecided | Adopt, and settle B1 with it |
| 7. Seat definitions | `omitClaudeMd` and a read-only `tools` list; isolation stays in the folder's settings; run folders out of git | The read-only list is in place, and no run folder is in git. The directory refused `omitClaudeMd` in Lite, so it's possible only in research copies or the full edition | Adopt, narrowed to research copies and the full edition |
| 9. A human-in-the-loop experiment | Hand relay against cross-session messaging, with leaks as a measure | Already an idea in the research doc, and it belongs to the human-in-the-loop project | Park it in that project's plan, section 6 |
| 10. Worktree note | `isolation: worktree` starts from the default branch unless `worktree.baseRef` is `"head"` | Supported by the docs. No council uses worktrees | Adopt as a note for any run that uses worktrees |

**The evidence:** each item's checked notes in outside review 7, including the dated amendments of 17 Nov 2026 from the docs re-read.

**The risks:** adopting an item records a rule. It doesn't make it true in every run folder. Items 1, 2 and 4 depend on files that each new run folder must copy. Item 7's `omitClaudeMd` can't ship in Lite while the directory refuses it.

**What the decision needs:** whether to adopt the items together or one by one, and the two checks above: Lite under the deny, and the local settings file.

---

## (g) The two unmarked hand-check packs

**The state:** two hand-check packs for the hard tier are built and waiting for the researcher. Claude Code didn't open them, since they name seeds and lines. From the seed-free report `reports\messaging-check.md`:
- **The match pack:** 15 matches, a stratified random sample of 5 catches, 2 known-bug matches, 5 close calls and 3 judgement calls. Each needs a right-or-wrong mark.
- **The extras pack:** 20 of the 238 unconfirmed extras, picked at random. Each needs a mark of real problem, not a problem or can't tell.

**Why they matter now:**
- The hard tier's matching was done by Claude and is unchecked. The easy tier's 15-item check found no errors, which still allows up to about 20% ("The pilot difficulty check").
- The rank rescore and the Ultrareview baseline both rest on the same matching.
- On the easy tier, all 20 sampled extras were real problems. If that holds here, extras can't be read as noise, which bears directly on (a).
- **A third check, with no pack:** the Ultrareview baseline's matching spot-check is also still to do ("The Ultrareview baseline").

**The options:** mark both before deciding (a), or decide (a) first and mark them later.

**The risk:** if (a) fixes precision measures before the extras are understood, it may fix a measure that penalises real findings.

**What the decision needs:** only the researcher's time. Nothing else blocks them.

**Suggestion (Claude Code's, not a decision):** mark both packs before deciding (a). Also mark the Ultrareview matches before that baseline is quoted anywhere.
