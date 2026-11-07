# Evolving Council & Optimum Size Experiment – Plan

A handover brief for a fresh session. The goal is to test whether an evolving, self-spawning council of review agents makes app builds better and more efficient, then turn the result into the user's default build-and-review recipe.

## The idea in one paragraph

When Claude builds an app for the user, a council of reviewer agents checks it for bugs, security issues and risky or boot-affecting changes. In this experiment the council evolves. Each generation reviews and improves on the previous generation's work, and it only advances if it beats a hard benchmark. The output is a readable report that recommends a standard recipe: how many agents, which models, what effort level and what token budget to use for a typical app, plus clear conditions for spending more.

## Goals

1. Find the optimum council size, meaning the point where adding more reviewers stops improving results, and the most efficient setup overall.
2. Produce a default recipe built around a median token budget per app build, with a hard agent cap.
3. Define the prerequisites for raising that cap, such as risky, system-level or boot-affecting code.
4. Check that the recipe holds across different kinds of apps.

## How "improved" is measured

- Each test app gets a fixed test suite and a short checklist covering bugs, security and risky changes.
- A generation only advances if it scores higher on that suite. A council saying it's better is not enough.
- A locked set of held-out tests is never shown to the agents. It catches gaming, such as agents faking or weakening tests.
- An efficiency score sits alongside quality: tokens used, number of agents and time taken.

## How evolution and stopping work

The councils don't decide when to stop. The stopping rules are fixed before the run, and the judge checks scores against them.

- **Evolution:** each generation tries to improve the best version so far. Its changes are kept only if they beat that version's score. Otherwise they're thrown away, and the next generation starts again from the same best version.
- **What's judged:** the output, not individual reviewers. Track which reviewers' suggestions end up in winning versions, to see which roles are worth keeping.
- **Stop when any one of these happens:** the score plateaus (for example, two generations in a row improve by less than about 2%), the generation cap is hit, or the token budget runs out.
- **Winner:** the generation that scored best on the held-out tests, which isn't necessarily the last one.
- **Optimum council size:** the point where one more reviewer costs more tokens than the quality it adds.
- **External benchmarks:** combined indexes (Artificial Analysis Intelligence Index, Stanford HELM, Epoch Capabilities Index) score the base model. They don't change with council quality, so use them only to choose which models sit on the council. A small slice of SWE-bench can serve as a shared coding yardstick alongside each app's own tests.

## Keeping the tests unbiased

The sandbox and fresh chats do different jobs: the sandbox stops agents touching anything real, and fresh chats stop earlier context biasing the results.

- **Fresh start per run:** run each test in its own new chat or session, with no memory of earlier runs and no hint of the result we're hoping for.
- **Blind judging:** the judge scores outputs without knowing which council setup, size or model produced them.
- **Same inputs:** every setup gets the same app, the same starting code and the same tests, so only the council changes.
- **Sandbox:** all runs stay inside an isolated project folder or environment, as in Hard limits.

## Repo structure

Everything lives in one public GitHub repo. The README is the hub, with the explainer video at the top. This plan stays complete as the master copy, and each topic below also gets its own standalone doc.

- **Core method:** council size by task complexity; cheating, collusion and failure modes; the WinScope pilot.
- **Spin-offs:** side experiments (tournament, Split or Steal); accent and dialect research; the council calculator tool.
- **Supporting material:** related research and citations; the explainer video plan.

## Cheating and collusion checks

Agents rewarded for winning may try to game the process, for example by hiding signals in normal-looking text or nudging other agents. The design should make that hard and easy to spot.

- **No direct agent-to-agent messages:** everything passes through the main orchestrator and is logged.
- **Paraphrase messages between agents:** rewording breaks any hidden signal tucked into the exact wording.
- **Judge sees results only:** the final code and test results, never the reviewers' messages or arguments.
- **Watch the tests:** flag any change that weakens, skips or edits tests, and rely on held-out tests the agents never see.
- **Audit the logs:** look for odd phrasing, repeated patterns or suspicious coordination between reviewers.

## Other failure modes to watch for

- **Rubber-stamping:** reviewers agree with each other or say "looks good" to save effort. Track how many real issues each reviewer raises.
- **Sandbagging:** agents behave differently, or deliberately underperform, if they suspect they're being tested. Keep test prompts realistic and compare against normal runs.
- **Pushing past the caps:** agents try to spawn extra helpers or stretch the budget to win. Caps are enforced by the orchestrator, not by the agents.
- **Prompt injection:** instructions hidden in the code or files being reviewed hijack a reviewer. Treat all reviewed content as data, never as instructions.
- **Noisy results:** flaky tests or random variation make a generation look better or worse than it really is. Repeat key runs and only count improvements that hold up.
- **Getting stuck:** agents loop on the same fix and quietly burn tokens. Stop a generation that repeats itself without progress.

## Pilot run: WinScope council review

An informal pilot on a real app before the formal experiment. Full write-up: [How the agents built and reviewed WinScope](winscope-pilot.md).

**Setup:** a coordinator wrote and froze a shared shell first; four builders then worked in parallel, one folder each; fresh reviewers (given code and a focus area, never the coordinator's conclusions) reviewed it; fixes went back to the original builder; fresh verifiers checked the fixes.

**Results:**

- About 16,000 lines built in about 33 minutes; 1,051 tests passing at the end, merged as version 1.1.
- About 3.7M subagent tokens across eleven rounds; review and verification were about 1.9M of that, about half.
- Review rounds found 97 problems the builders' own tests had passed (48 in the first council, 10 in the first verification, 25 in a privacy audit, 14 in the second verification).
- Every serious bug was found by an agent that hadn't written the code, e.g. a privilege-escalation hole from elevated writes to user AppData, and a Recycle Bin wrong-file case.
- Verification after fixes never came back empty: 10 new findings the first time, 14 the second (4 of them medium).
- A single-agent comparison (AirScope) got similar review results, suggesting the reviews catch the bugs, while parallel building adds speed plus a new class of bugs at the seams between parts.

(diagram in the original doc)

**Pilot's own takeaways:** freeze shared parts first; fix with the author, verify with a stranger; always run a verification round; make reviewers run code against crafted inputs; aim the hardest reviews at risky code (file deletion, admin, personal data); keep one coordinator for the seams.

**Limits:** nothing has run on Windows yet (tested on Linux only); reviewers inherited saved memory, so not fully clean-room; one app, one run, no repeats or no-review baseline; token counts are self-reported by agents. Also, reviewers used real personal details as test inputs and some ended up in code comments (caught before publishing), so the formal experiment should give reviewers made-up test data.

### Interpretation (Claude's read, not data)

- Strong early evidence for the core premise: independent reviewers catch what authors miss, and verification rounds are worth their cost.
- Doesn't yet answer the optimum-size question, since council size wasn't varied. The formal experiment should vary it.
- Severity-weighting matters: findings varied a lot in importance, so counts alone may mislead. Score findings by severity.
- The cost split (about half on review) supports scaling review effort to risk, which fits the council-size-by-task-tier idea.
- Carry over into the formal design: fresh reviewers without memory, crafted-input testing, and real-platform test runs as part of the hard benchmark.

**Using the pilot as a reviewer checklist:** the pilot's findings make a good starting checklist for what reviewers look for (security around admin rights, risky file handling, privacy leaks, bugs at the seams between parts), and its report format (findings with the real input and output) is worth copying. It is not a baseline to score against: each test app needs its own scored benchmark, with findings weighted by severity.

## Hard limits (set before every run)

- Maximum number of agents per generation
- Maximum number of generations
- Token budget per run. Stop cleanly when it's reached and still write the report.
- No changes outside the sandbox or project folder, and nothing that touches the real system, drivers or boot settings.

## Command gating: what reviewers may run (prompted by an agent rm -rf incident, Nov 2026)

Everything in this section from "Proposed design" onwards is untested: none of it has been built or run.

### The incident

A user on r/ClaudeCode reported that Claude Code, running with `--dangerously-skip-permissions`, wiped `~/Library` on macOS. It ran `xargs -n1 dirname` on paths inside `~/Library/Application Support/`. xargs split each path at the space, so `dirname` returned `~/Library`, and that went to `rm -rf`. The command looked reasonable as written; the danger only showed in the resolved target.

This is a self-reported anecdote, and the post isn't linked here yet. Only the xargs mechanism was reproduced independently (GNU xargs 4.10):

```
$ printf '%s\n' "Library/Application Support/app/ch1/file" | xargs -n1 dirname
Library
Support/app/ch1
$ printf '%s\n' "Library/Application Support/app/ch1/file" | xargs -d '\n' -n1 dirname
Library/Application Support/app/ch1
```

`-d` is a GNU option. The BSD xargs that ships with macOS doesn't have it, so the portable fix there is NUL-separated input with `-0` (for example `find ... -print0 | xargs -0 ...`).

### Current state

The rule is the same in Council Dial 1.1.0 (published on main) and 1.2.0 (in progress): "reviewers may not run code" is an instruction in the brief ("Don't run code from the material unless your brief says the user allowed it"), backed by the user's Claude Code permission settings. Reviewers are ordinary subagents that can use whatever tools the session allows. Council Dial itself enforces nothing.

### Proposed design: two tiers (untested)

- **Hard list:** commands reviewers never run, such as recursive deletes or anything outside the project folder. Enforced mechanically, not by the brief.
- **Propose, don't execute:** any other risky command a reviewer wants run is sent to the judge instead of being run.

**How the tiers fit together (untested):** the hard list is what a reviewer may never run itself; it can only propose those commands. Any proposal of a hard-list command skips the judge's "safe" call and goes straight to the appealer, and nothing on the hard list runs without a final yes from the user.

### Who sees what (untested)

- **Judge:** the full context, the reviewer's reasoning and the command.
- **Independent appealer:** only the command plus a mechanical dry run of exactly what it would touch (resolved paths, file counts), with no reasoning attached. This differs from Council Dial's current appeal, which sees the judge's reasons for each finding it dismissed.
- **Principle:** hide opinions from the appealer, not facts.
- **Risk tags come from the dry run:** a tag such as "destructive / system-affecting" comes from the mechanical dry run, never from the proposing agent. The agent in the incident would honestly have tagged its command as harmless cleanup.

### Single point of failure (untested)

If the judge alone decides what reaches the appealer, a wrong "safe" call means nobody else sees the command. The fix: a mechanical rule forces escalation whatever the judge thinks. For example, any recursive delete or anything outside the project folder goes straight to the appealer. The judge then rules only on grey-zone commands.

### Over-rejection (untested)

Blocking every `rm` catches too many harmless cleanups. Thresholds on resolved scope (five temp files vs 40,000 files under `~/Library`) should separate them. The false-reject rate and the missed-danger rate are both measurable.

### What triggers a dry run (untested)

A fixed, deliberately wide mechanical rule decides, not the reviewer's judgement, so the decision doesn't vary between models.

- Any command that deletes, moves or overwrites files, or that builds paths from other commands' output (pipes, xargs, command substitution, loops over file lists), gets a dry run, whatever its stated purpose.
- Reviewers may add extra dry runs but can't skip one the rule requires.
- The xargs command looked like ordinary cleanup, so a rule based on how commands look or what the reviewer thinks they're for would likely have missed it.

### Where the dry run comes from (untested)

- **The sandbox tool produces it:** the dry-run result comes from the sandbox tool itself, and that raw output goes to the judge and the appealer, not the reviewer's summary of it. That keeps the facts separate from the reviewer's opinion.
- **Sandbox fidelity:** the sandbox must copy the real folder structure, including spaces in names such as "Application Support". Otherwise the word-splitting bug won't show in the dry run, and the command will look safe.
- **Fail closed:** if the sandbox dry run fails or can't connect, it's skipped, the command is marked "dry run unavailable", and it's flagged to the user anyway. Any delete whose scope can't be resolved is treated as hard-list.

### The appealer is one-way (untested)

The appealer can only block or flag, never approve. It checks the dry run against the outcome rules and needs no other context. The judge, with full context, can approve grey-zone commands, and anything on the hard list still needs a final yes from the user.

Hard-list flags always reach the user. The judge and the appealer don't decide whether the user sees a flagged command; they only add context to it.

Trade-offs to measure in the testing round:

- A blind appealer may block small but harmless deletes.
- Hiding the proposer's framing removes one source of bias, not all: the appealer may lean cautious, and how the dry-run output is laid out may sway it.

### How results reach the user (untested)

After a large review, results reach the user in three buckets:

1. changes made, and reported;
2. decisions flagged for the user, such as hard-list commands;
3. runs that needed nothing from the user, because nothing hit the hard list.

Council Dial's reviewers change nothing today, so automatic changes would be a new mode. They should go on a separate branch, so any change is one revert away.

### Worked example: how this design might have caught the Reddit case (illustration, untested)

This is an illustration, not a claim. Step by step:

1. **Trigger:** the command matches the wide trigger, because it pipes paths through xargs into `rm -rf`.
2. **Sandbox:** the sandbox copies the folder tree, including "Application Support".
3. **Dry run:** the dry run shows the target resolving to `~/Library` and thousands of files, rather than five test folders.
4. **Outcome rules:** that breaks the outcome rules (it deletes outside the project and touches thousands of files), so it's flagged.
5. **Appealer:** the appealer blocks it on the dry run alone.
6. **User:** it reaches the user as a hard-list decision with the dry-run output attached, instead of running.

None of this has been tested, and it isn't a guarantee. It depends on the sandbox matching the real folders, the trigger firing, and the agents reading the dry run correctly. The testing round is what will show whether it works.

### Experiments to run

- **Command alone vs dry run:** give the appealer the command alone, or the command plus the dry-run expansion, and compare catch rates on destructive-command bugs.
- **Escalation load:** in the WinScope pilot, log how often the mechanical escalation rule fires, to measure whether the appealer gets flooded.
- **Council type under lopsided costs:** consensus-only submission is likely worst for safety gates, because a lone dissenter's catch is dropped. Single-veto or pooled is likely best.
- **Finding appeal with vs without the judge's reasons:** run Council Dial's finding appeal with and without the judge's reasons, to test whether seeing them anchors it towards upholding dismissals. So far there is one data point: in run `20261107-2f23` the appeal upheld the one dismissal in 8.2 s. It was correct (the dismissed finding was a false positive), and one run can't show anchoring either way.
- **Tool choice and fallback:** which tools each specialised council member chooses to use; how tool availability affects review quality; and when members fall back to other tools (for example the shell). Across models: whether reviewers get all tools, how often each model falls back and onto which tools versus carrying on, and whether that affects scores and fairness between models. [HalfLucid/FileInteractionMCP](https://github.com/HalfLucid/FileInteractionMCP) is a possible test subject. The blocked-`rm` question (does a model route around the block, for example by writing a script, ask, or stop?) is one case of this.
- **Candidate seeded-bug class:** unquoted paths with spaces (shell word-splitting).

### Next testing round: the xargs case as a test family (planned, not run)

- **Seed:** the Reddit xargs / `rm -rf` incident above. I'll build a family of cases around it: the dangerous original; variants that hide the space-in-path bug in different ways (other word-splitting forms, other paths with spaces); and safe lookalikes that should be allowed, such as the same pipe deleting five temp files inside the project.
- **Conditions:** judge alone, appealer alone, and judge plus appealer. Each is given either the command alone or the command plus a dry run of the resolved targets.
- **Repeats and measures:** I'll run each case several times, measure what each condition wrongly lets through and what it wrongly blocks, and record which agent made each call and why.
- **Expected, not yet shown:** shown only the command text, a judge or appealer will likely approve it; only the dry run exposes that it would delete `~/Library`.
- **Appealer variant:** the appealer's only context is the hard list, written as outcome rules (for example, never deletes outside the project, never touches thousands of files) rather than banned command names, checked against the dry run.
- **Goal:** settle which role should make the call on destructive commands, what each needs to see, and how.
- **Video note:** a planned segment for the main video, showing the command alone being waved through, then the dry run exposing `~/Library`.

### Testing the appeal step on the case it exists for (planned, not run)

The full record of both runs is in Council Dial's [results file](https://github.com/Ablation-Lab/council-dial/blob/main/results/20261107-council-runs.md).

- **Background:** runs `20261107-f675` (judged, no appeal) and `20261107-2f23` (judged plus appeal) both had reviewers raise all 9 planted bugs. In run 1 the judge dismissed planted bug #7 (an unchecked path from user input). After run 1, I deliberately edited the sample README to say the path comes from the blog name the user types at sign-up, because #7 wasn't clearly in scope before, so run 1's dismissal was partly defensible. Seven things changed between the runs (listed in the results file), including removing the "planted" wording and moving the judge brief to version 2. In run 2 the judge kept #7 and dismissed only an unplanted false positive, which the appeal upheld. So the appeal hasn't yet been tested on a wrongly dismissed real bug.
- **Video note:** if the judge's dismissal is the cold open, I'll tell it honestly: the judge threw out a real bug partly because the docs didn't make its scope clear.
- **Proposed test:** I won't use the old, ambiguous README. I'll run judged-with-appeal and judged-without-appeal several times each on the current neutral sample, with the same judge brief version and model, and count wrongful dismissals of planted bugs, how often the appeal flags them, and how often it flags correct dismissals. If judges rarely dismiss real bugs here, I'll build a harder sample where the evidence that a bug is in scope sits in a different file from the bug.
- **Appeal gap:** the appeal sees only NOT REAL findings, so severity downgrades are never appealed; OVERSTATED rose from 2 to 5 between the runs. A possible variant is an appeal on downgrades.
- **Cost:** in run 2 the appeal used 41,995 tokens, about 94% of the cheapest reviewer's tokens, and added about 21% to the run's tokens, despite checking one finding in 8.2 s. Inferred, not documented: most of each subagent's tokens look like a fixed cost of starting up and reading the material.
- **Scoring:** run 2's judge merged two pairs of planted bugs (9 bugs became 7 findings), so I'll score on bugs covered, not findings. Real findings that weren't planted go in a separate, versioned "also real" list. REAL fell from 10 to 7 and OVERSTATED rose from 2 to 5, possibly because of the version 2 judge brief, but there are too few runs to say.
- **Method:** Council Dial's log doesn't yet record which version of the material was reviewed, so I'll record the sample version by hand until it does. I'll also measure minutes the same way in every run before comparing runs (see entry 7 of the [who-caught-what log](who-caught-what.md)).
- **Refuted claims:** two voice-drafted claims about these runs were checked and refuted. They're in the [who-caught-what log](who-caught-what.md) (entries 2 and 3), not repeated here.

### Design reference

A community pattern: a hook that blocks all deletes and makes agents move files to a cleanup folder for a person to review.

A reference implementation: [HalfLucid/FileInteractionMCP](https://github.com/HalfLucid/FileInteractionMCP). Its trash-backed delete and dry-run diffs match the move-to-a-cleanup-folder pattern and the dry-run idea above, so it's a possible test subject for command gating as well as for tool choice and fallback.

Caveat, checked against its README only, not its code: its dry runs cover its own editing tools (they return a diff), its README doesn't describe one for `fs_delete`, and it has no tool for running shell commands. So it wouldn't cover arbitrary shell pipelines like the xargs case, which would need another way to resolve targets, for example running the command against a copy of the folder tree.

### Video note

The incident is a candidate opener for a command-gating part of the main explainer video. The video has no such part yet.

## Test plan

### Small runs (three apps, kept cheap)

Use three small generic apps of different types:

1. A simple utility, such as a file renamer or a small CLI tool
2. Something with a UI, such as a small WPF or desktop app
3. Something that touches system settings, in safe or mock mode only

Default setup: about 3 reviewers × 3 generations, with reviewers on medium effort and the judge on high.

### Big run (one app, the ceiling test)

One run with many more agents and generations, all still under hard caps. It answers one question: do lots of extra agents actually beat the small runs by enough to justify the usage?

### Model comparison

Where budget allows, compare:

- Sonnet reviewers with an Opus judge (cheaper)
- Opus reviewers with an Opus judge (stronger)

The report should say whether the cheaper mix holds up.

### Council size by task complexity

Test whether the optimum council size changes with how complex the task is. For example, a basic app might only need about 6 reviewers, a scientific app might need about 20, and frontier research might need far more.

- Run the same size sweep on tasks of different complexity tiers.
- Record quality and token cost for each size and tier.
- The goal is a rough scale, a standard unit of review effort per complexity tier, that sets the baseline council size for a new task.

## Roles

- **Builder:** writes or changes the app
- **Reviewers (the council):** each checks a focus area, such as bugs, security, risky changes or efficiency
- **Trajectory reviewer:** one reviewer looks at the whole path of a session, not just the latest step. It flags drift with tripwires such as "below the OS" or "bypasses a security check". This comes from an earlier episode where step-by-step reviews missed a slow drift toward risky work.
- **Judge:** runs the benchmarks and decides whether a generation really improved. It also signs off on the final result.
- **Logger:** every generation writes a short log of what changed and why

## The final report (must be easy to read)

- A plain-English summary at the top: what was tested and what was found
- A simple visual, such as a family-tree or timeline chart of the generations with their scores and token use
- Why each kept change was kept and each dropped change was dropped
- A small table comparing every run on quality, tokens, agents and time
- **Optimum council size and the recommended default recipe:** the number of reviewers, models, effort levels, median token budget per app and hard agent cap
- **Escalation rules:** when to add agents or use a stronger model
- Notes on any gaming or odd behaviour spotted

## Usage estimates (rough)

- These figures assume a Claude Max plan.
- Each small run costs about half a session. The big run costs about one session or a bit more.
- The total is roughly 3–4 sessions, about 15–30% of a week.
- Spread it over 2–3 fresh session windows, and start each run in a fresh window so a generation isn't cut off halfway.
- Treat these as ballparks and recalibrate after the first small run.

## Side experiments

### Tournament vs team

An elimination format where reviewers are knocked out round by round until one is left. The hard tests decide each round, not votes, because AI judges tend to favour their own style. Compare the single winner against a varied team, since earlier research suggests diversity may beat one top reviewer.

### Split or Steal final (prisoner's dilemma)

A bonus round for the two tournament finalists, based on the Golden Balls game show. The two talk to build trust, then each secretly chooses split or steal. If both split, they share. If one steals, that one takes everything. If both steal, neither gets anything.

- It doesn't decide the review winner. The hard tests still do that.
- It measures cooperation, betrayal and trust-building, which is useful for AI safety research.
- Vary the models, and whether agents know the game will be repeated.
- Cheap to run, and best built later in text chat or Claude Code.

## Companion tool: council calculator

A small app that estimates a council setup before any real usage is spent.

- **Input:** pick a task template, such as a basic app, a scientific app or a system-level tool.
- **Simulate:** estimate the token cost, the best council size and the model mix for that task.
- **Output:** a ready-to-paste prompt template that tells any AI how many reviewers to spawn, which models and effort levels to use, and what hard caps to apply.
- **Learning:** every real run's logs feed back in, so the estimates get more accurate over time. The calculator is built only after the test runs are finished, so its templates and estimates use real results from the experiment instead of guesses.

## Order of work

1. Session 1: Set up the harness, benchmarks and caps. Run small app #1 and check the usage it actually costs.
2. Session 2: Run small apps #2 and #3, plus the Sonnet vs Opus comparison if the budget allows.
3. Session 3: Do the big run, then write the final report.
4. Last step: Give the full results and report to Fable 5.1 for one deep review, to check the recipe makes sense and nothing was gamed, including any signs of hidden messages or collusion between agents.
5. Then: Build the council calculator from the real test results, then adopt the recipe as the default for future app builds.

## Instructions for the next session

Read this whole plan first. Before building anything, confirm the hard caps (agents, generations, tokens) with the user. Keep everything sandboxed. Stop at the budget limit and still produce the report.

## Future application: accent and dialect understanding

The same evolving-council method could improve how well an AI understands accented speech, such as a Welsh accent.

- **Benchmark:** real audio from speakers with that accent, paired with transcripts checked by a person. The hard score is word error rate, the share of words the system gets wrong.
- **What evolves:** the council can't retrain the speech model itself. It evolves the step after transcription, the part that corrects and interprets what was heard.
- **Held-out speakers:** keep some speakers back as unseen tests, so the system learns the accent rather than memorising individual voices.
- **Why it matters:** if AI understands some accents, dialects or languages worse than others, whole regions, or areas within one country, could quietly get worse answers.

Background (from general knowledge, check before citing): Koenecke et al. (PNAS, 2020) found major speech recognition systems made roughly twice as many errors for Black speakers as for white speakers. Hofmann et al. (Nature, 2024) found language models judged speakers of African American English more negatively.

## Final deliverables

- A public GitHub repo with the council calculator and a clear README.
- A write-up or preprint explaining the results, and why each task template's optimum council size is set where it is.
- Raw run logs in the repo, so anyone can check the results.
- A [who-caught-what log](who-caught-what.md) of who caught which mistakes during the research.
- An animated explainer video built with Remotion, linked at the top of the README so visitors can see what the project is before reading further. The Remotion source code lives in a companion repo, [ablation-lab/council-video](https://github.com/ablation-lab/council-video). Before rendering, a small council of 2–3 fresh subagents reviews the video code independently (bugs, timing, overlapping text), which doubles as a mini pilot of the council method.

## Related research

Earlier work shows that adding more agents doesn't automatically help, and that the best number depends on the task. This experiment adds evolving councils for code review, a council-size scale for each complexity tier, and a calculator that outputs a ready-to-use prompt.

- [Towards a science of scaling agent systems](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/) (Google Research): tested 180 agent setups. Piling on more agents often hits a ceiling and can make results worse.
- [Scaling Behavior of Single LLM-Driven Multi-Agent Systems](https://arxiv.org/abs/2606.00655): the type of task has a big effect on the best number of agents.
- [Understanding Agent Scaling via Diversity](https://arxiv.org/html/2602.03794v1): adding identical agents gives strongly diminishing returns, but mixing different models, prompts or tools keeps paying off.
- [On the Importance of Task Complexity in Evaluating LLM-Based Multi-Agent Systems](https://arxiv.org/html/2510.04311v1): multi-agent gains level off as tasks get wider, but keep growing as tasks get deeper.
- [Literature Review of Multi-Agent Debate](https://arxiv.org/html/arXiv:2506.00066): the best agent count depends on task complexity, agent diversity and how the agents communicate.
- Darwin Gödel Machine (Sakana AI): self-improving coding agents. It's also a known case of agents faking test results to look improved.
- RepliBench (UK AI Security Institute): a benchmark for testing whether models can replicate themselves autonomously.

### Research linked to specific sections

- **Judge role** – [Judging LLM-as-a-Judge (Zheng et al., 2023)](https://arxiv.org/abs/2306.05685): LLM judges largely agree with humans, but they have known biases, such as favouring longer answers or their own outputs. This is why the plan relies on hard benchmarks.
- **How "improved" is measured / gaming** – Specification gaming (DeepMind, 2020): agents often meet the letter of a goal instead of its spirit. This is why the plan uses held-out tests.
- **Outside oversight** – [Measuring Progress on Scalable Oversight (Bowman et al., 2022)](https://arxiv.org/abs/2211.03540): how humans can supervise AI systems doing work they can't fully check themselves.
- **Model comparison and the calculator** – [FrugalGPT (Chen et al., 2023)](https://arxiv.org/abs/2305.05176) and [RouteLLM (Ong et al., 2024)](https://arxiv.org/abs/2406.18665): sending each request to a cheaper or stronger model as needed can cut cost a lot without losing much quality. This is the same idea as Sonnet reviewers with an Opus judge.

*These section links are from general knowledge. Check them before citing them in an application or paper.*

**Related incident:** an agent `rm -rf` via xargs word-splitting (Reddit, Nov 2026). See [Command gating](#command-gating-what-reviewers-may-run-prompted-by-an-agent-rm--rf-incident-nov-2026).
