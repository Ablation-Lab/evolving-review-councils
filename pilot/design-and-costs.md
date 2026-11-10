# WinScope pilot: design and cost estimate

Nov 3, 2026. For the researcher to review before anything is spent. Nothing paid has run yet. The pre-registration is in [pilot-plan.md](pilot-plan.md).

## 1. What the checks found

- **WinScope has no tests in its repo.** The pilot's 1,051 tests were never committed. The repo is a single `WinScope.csproj` (WPF, `net8.0-windows10.0.19041.0`, WinExe), with no test project anywhere in its history.
- **The buggy pre-fix versions aren't in git.** 1.0 was committed as one squashed commit with the review fixes already in. So the pilot bugs can't be replayed from diffs. Each replay has to be rebuilt by hand from the pilot write-up, then checked by the researcher.
- **WinScope builds on this PC** (the .NET 8.0.427 SDK; the .NET 10 runtime is installed), with no warnings.
- **The Stryker spike works.** I copied WinScope to a scratch folder, added an xUnit project with 16 tests for `WinPath.Normalize`, and ran Stryker.NET on `PathSafety.cs`.
  - The current Stryker, 5.0.0, won't install with the .NET 8 SDK. **4.16.0 does**, and it handles the WPF WinExe project without changes.
  - Stryker created 371 mutants in that file. Only 21 (6%) failed to compile. Stryker's safe mode handles these automatically.
  - Of the mutants it tested, 75 were killed by my 16 tests and 32 survived. The other mutants weren't covered by any test or were ignored.
  - **So the mutant source works, provided I write held-out tests** to give the researcher's automatic check ("compiles, and at least one test fails") something to fail. Those tests also serve as the seeds' triggering tests.
- **Reviewer isolation works on the Max plan.** A smoke test ran Opus 5.5 with these flags:

  ```
  claude -p --safe-mode --restricted --tools Read,Grep,Glob --strict-mcp-config --no-session-persistence --output-format json
  ```

  The session ran in a fresh folder outside the folder that holds my project repos. It reported no CLAUDE.md, memory or project notes, and only the three tools. It was refused when it tried to read a file outside its folder.
  - `--bare` can't be used: it only accepts an API key, so it would bill the API instead of the Max plan.
  - The JSON output reports tokens and a notional cost. That's how "roughly equal usage" is measured and logged.
- **The original builder sessions aren't on this PC.** There are no WinScope session files under `~/.claude/projects`, so a true builder self-review (resuming the actual author) isn't possible unless they exist elsewhere. See decision A.

## 2. How it works

**Seeds (private until the runs are done).** Seeds are built in a private folder outside both public repos (`../pilot-private/`, next to this repo rather than inside it, and not a git repo). That folder holds:

- the seed patches and the answer key
- the held-out test project
- the five exported variants

Each variant is a copy of WinScope's `src` with no `.git` folder, no tests and no README, with only its own seeds applied.

**Seed sources.**

- **Replays (13):** rebuilt by me from the pilot write-up. See section 4 for the list for the researcher to check.
- **Stryker mutants (14):** chosen by a script from killed mutants, spread across modules and operator types, using a fixed random seed. They're checked automatically.
- **Mistral seeds (13):** Mistral Large 4 (`mistral-large-4-0`) gets one source file and a brief: category, severity, must compile, must look like real code, and no hinting comments. It returns a patch, a one-line root cause and a triggering test. About 20 candidates are generated, those that fail to compile or have no failing test are dropped, and the researcher checks the rest. They're mostly security, privacy, deletion and WPF bugs, to fill the critical and high slots.

**Seed severity by source:**

| Source | Critical | High | Medium | Low | Total |
| --- | --- | --- | --- | --- | --- |
| Replays | 2 | 3 | 5 | 3 | 13 |
| Mistral | 2 | 4 | 4 | 3 | 13 |
| Stryker | 0 | 1 | 7 | 6 | 14 |
| **Total** | **4** | **8** | **16** | **12** | **40** |

**Reviewers.**

- **Claude:** `claude -p` with the flags above, run from `C:\pilot-ws\<run-id>\` with Opus 5.5 at medium effort. Briefs are real task instructions, with no bare persona labels.
- **Gemini and DeepSeek:** a small Python loop with the same three read-only tools (list, read, search), confined to the same workspace, plus a turn cap and a token cap.
- **The same output format for everyone:** file, lines, root cause, severity, and the input that shows the problem.

**Merger, judge, scoring.**

- `merge.py` and `judge.py` call GPT-6.1 Sol. The judge runs through the Batch API, which is half price.
- `rejudge.py` calls DeepSeek V4 Pro.
- `score.py` computes Wilson intervals and paired-bootstrap 90% intervals.

**Logs.** Each call records:

- the model ID and its dated snapshot
- the price table in use
- tokens, cost and duration
- the Claude Code CLI version (2.1.317), Stryker version (4.16.0) and .NET SDK version (8.0.427)

Logs go in `pilot/runs/` and are committed after the runs, once they've passed the privacy check.

**Workload.**

- **Claude reviews (Max plan):** 65 sessions (S1 ×5, C3 ×45, SR ×5, Claude member of MX ×10). At the pilot's 170k–320k tokens per fresh review, that's about 15–20M tokens, roughly five times the original WinScope pilot. Spread it over about 3–5 days of Max limits.
- **Paid API reviews:** Gemini and DeepSeek do 10 reviews each.

## 3. Cost estimate (paid API only)

Prices were checked Oct 31 and Nov 3, 2026. Every figure assumes no caching, so they're upper estimates.

| Step | Assumptions | Estimate |
| --- | --- | --- |
| Mistral seed candidates | 20 × 25k input / 6k output at $0.70 / $2.10 | $0.60 |
| Gemini 4 Argon reviews | 10 × 1.5M input / 60k output at $2 / $10 | $36 (**$72 if run on or after Dec 1**, when prices double) |
| DeepSeek V4 Pro reviews | 10 × 1.5M / 60k at the peak rate of $1.32 / $3.96 | $22 |
| Merger (Sol) | 35 outputs × 30k / 8k | $5 |
| Judge (Sol, Batch) | about 575 findings, including calibration, × 15k / 4k at $1 / $5 | $20 ($40 without Batch) |
| Second judge (DeepSeek) | about 85 findings × 15k / 4k | $3 |
| Smoke tests and version pinning | | $2 |
| **Subtotal** | | **$89** (Gemini before Dec 1); $125 after |
| **With a 25% contingency** | | **$111, about £89**; $156, about £125 |

GBP uses $1.25 to £1, deliberately below recent rates of about $1.29–1.34. I couldn't find a rate dated today, so the GBP figures lean slightly high. **The worst case, about £125, is under the £160 stop.**

The 1.5M input per API review is the cumulative total over an agent's turns. If the provider caches the repeated context, it costs much less.

**Budget controls**

1. **A ledger in the harness.** Before every paid call, it estimates the cost and adds it to the spend so far. It refuses the call and stops the run if the projected total would pass **£160 (80% of £200)**, then writes a report for the researcher. Each step also shows its estimate before it starts.
2. **Caps with each provider, set by the researcher.** The suggested caps add up to about $190 (£152), so they hold even if the ledger fails:
   - OpenAI project budget: $50
   - DeepSeek prepaid top-up: $40
   - Mistral: $10
   - Google: a $90 budget alert, plus an API key restricted to the Gemini API

   Whether each provider can enforce a *hard* stop wasn't checked. Google budgets only send alerts, so the ledger is the real stop there.
3. **API keys.** Keys go in environment variables (none are set yet). They're never written to files in either repo.

## 4. Replays for the researcher to check

These are rebuilt from the [pilot write-up](../core-method/winscope-pilot.md). The comments that currently describe each fix are made neutral as part of the seed.

| # | Bug to reintroduce | Where | Severity |
| --- | --- | --- | --- |
| R1 | Settings and logs written to the user's AppData while elevated (privilege escalation) | `Core/UserFiles.cs`, `Core/AppSettings.cs` | critical |
| R2 | A name ending in a dot or space sends the wrong file to the Recycle Bin | `Modules/Storage/PathSafety.cs`, `Recycler.cs` | critical |
| R3 | The redactor treats "server" as a version number and skips the IP after it | `Core/Reports.cs` (`VersionBefore`) | high |
| R4 | The redactor doesn't remove email addresses | `Core/Reports.cs` | high |
| R5 | A Wi-Fi adapter renamed after its network leaks the network name | Network report and redaction | high |
| R6 | Temp cleanup matches nothing when the profile path uses 8.3 short names | `Core/Reports.cs` / Storage cleanup | medium |
| R7 | A redactor pattern that takes seconds on a long line | `Core/Reports.cs` | medium |
| R8 | The Network graph redraws every frame (constant CPU) | `Modules/Network/NetGraph.cs` | medium |
| R9 | Closing the app freezes while tools stop one by one, not in parallel | `MainWindow.xaml.cs` (`BeginStop`) | medium |
| R10 | Refreshing the Events view loses events | `Modules/Events` | medium |
| R11 | Merging blue-screen events swallows a second crash | `Modules/Events/EventAggregator.cs` | medium |
| R12 | `AppData\LocalLow` comes out as `%LOCALAPPDATA%Low` | `Modules/Storage/StorageReport.cs` | low |
| R13 | A wrong power-supply sizing hint | `Modules/Events/EventRules.cs` | low |

R10 and R11 are described only briefly in the write-up, so I'd have to reconstruct a plausible version of each. Reserves, if any of these can't be rebuilt cleanly:

- the minimum window height pushing the window off small screens (the current XAML still has `MinHeight="760"`, so this needs checking)
- a non-English adapter name ("WLAN") counted as renamed

## 5. Decisions needed before I build

- **A. Self-review condition.**
  - If the original builder sessions still exist (for example as cloud sessions on claude.ai/code), the best option is to fork them and ask them to review. That's a true self-review.
  - Otherwise, the **recommendation** is the author-framed proxy in the pre-registration, clearly labelled. It tests whether *being told* it's the author makes a reviewer go easier. That's weaker than true self-review, so it's labelled as such.
  - The third option is to drop it from the pilot.
- **B. Tools for API reviewers.**
  - **Recommendation:** the same read-only agent tools as Claude, which keeps the comparison fair. That's what the estimate above assumes.
  - The cheaper option is to paste the whole codebase (about 250k tokens) into one prompt. That costs about half as much, but then Claude and the other models aren't working the same way.
- **C. Five variants, or fewer?** Five (four seeded plus one clean) keeps 10 seeds per variant, but needs 65 Claude sessions. Three variants (two seeded with 20 seeds each, plus one clean) cuts that to about 39, but puts twice as many bugs in each copy.
- **D. Timing.** Run the Gemini reviews before Dec 1 to avoid the price rise. Recheck all prices the week before (decision 9).
- **E. Publishing the seed key after the pilot.** **Recommendation:** publish it, so the pilot results can be checked in applications, and use fresh seeds for the full experiment. That needs 120 per app anyway.
- **F. Provider caps.** The researcher sets them and adds the API keys as environment variables. I can't do either.

## 6. What I build after approval

The harness goes in `pilot/harness/` in this repo (Python standard library only). Run order:

1. **Free steps first:** the held-out test project and the replay seeds.
2. **The researcher checks the replays.**
3. **Paid:** about 20 Mistral candidates, about $0.60.
4. **The researcher checks the Mistral seeds.**
5. **Free:** select Stryker mutants and build the variants.
6. **Max plan:** the calibration run.
7. **The researcher labels the calibration findings.**
8. **Paid, about $5:** judge agreement check.
9. **Freeze the pre-registration.**
10. **Reviews:** Claude conditions on the Max plan, then MX (paid).
11. **Paid:** merger and judge.
12. **Score, then write up.**

The ledger checks every paid step against the £160 stop.
