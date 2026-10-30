# How the agents built and reviewed WinScope

Oct 30, 2026

Four builders working in parallel behind a shared shell produced WinScope's 16,000 lines in about 33 minutes. Most of the serious bugs were then found by fresh reviewers who hadn't written the code, not by the builders' own tests.

## At a glance

Eleven rounds used about 3.7 million subagent tokens, and the review rounds found 97 problems that the builders' own tests had passed. The table is in the order things happened.

| # | Round | Agents | Wall time | Tokens | What came out |
| --- | --- | --- | --- | --- | --- |
| 1 | Shell and contract | Me (main thread) | \~1 h | not measured | The tool interface, elevation, settings, safe file writes, theme, main window, stub tools, a rules doc |
| 2 | Parallel build (1.0) | 4 fresh builders | 33 min | 1.14 M | \~13,000 lines across four tools, 528 tests |
| 3 | Review council | 4 fresh reviewers | 14 min | 1.00 M | 48 findings (storage safety, interop, integration, logic) |
| 4 | Fix round | 4 resumed builders | 17 min | 0.32 M | 60 fix items closed |
| 5 | Verification | 2 fresh reviewers | 8 min | 0.39 M | 10 more findings |
| 6 | Storage final fix | 1 resumed builder | 3 min | 0.02 M | 6 items closed |
| 7 | Reports feature (1.1) | 4 resumed builders | 7 min | 0.19 M | One report section per tool |
| 8 | Privacy audit | 1 fresh reviewer | 10 min | 0.23 M | 25 findings: 12 leaks, 3 redactor bugs, 10 correctness |
| 9 | Report fixes | 4 resumed builders and me | 4.5 min | 0.11 M | All 25 addressed; 999 tests passing |
| 10 | Verification of report fixes | 1 fresh reviewer | 14 min | 0.26 M | 31 of 34 earlier findings confirmed fixed; 14 new (4 medium, 10 low) |
| 11 | Last fixes | 3 resumed builders and me | 2 min, after a 25 min usage-limit pause | 0.04 M | All 4 medium and 8 low fixed, 2 kept as trade-offs; 1,051 tests; merged as 1.1 |

Tokens are what each agent reported processing, including re-reading its own context. Resumed builders are counted by the extra tokens that round added. Wall time is the slowest agent in the round, because they run side by side. My own main-thread work isn't included in the token totals.

## How the parallel build was set up

The split worked because the shared parts were written and frozen before any builder started. Each builder could then work blind to the others.

(diagram in the original doc)

**1. The shell came first, written by me.** Before any builder started, I wrote:

- The `IToolModule` contract every tool implements: title, icon, a dashboard card, a full view, Start, visibility changes, Dispose.
- Elevation handling: knowing when it's running as admin, and restarting elevated on the same screen.
- Settings, and a safe file-writer that refuses to write while elevated.
- The dark theme, the main window with the dashboard and navigation, and a stub of each tool so the whole app compiled from minute one.
- A one-page rules doc:
  - each builder touches only `Modules/<its tool>/`
  - nothing in Core changes
  - zero warnings
  - unit tests for the logic
  - report back with a sample of the output

**2. Four builders started at the same moment, each told only its own tool's brief plus the rules.** Performance, Network, Events and Storage each got a fresh agent. None of them saw the others' code or my reasoning. They finished between 22 and 33 minutes later, adding 263k–323k tokens each.

**3. Each builder compiled in its own private copy of the tree.** On the first attempt they all built in the shared folder. Whenever Events was mid-edit, the whole tree failed to compile for everyone else. The fix was for each to copy the tree and build its copy, while still writing its finished files into its own folder in the real tree.

**4. The contract grew without breaking anyone.** New needs became default interface members, so tools that didn't care compiled unchanged:

- `BeginStop` (stop all tools in parallel on close)
- `BusyReason` (don't restart as admin mid-cleanup)
- `BuildReport` (the 1.1 Reports feature)

**5. Cross-cutting fixes stayed with the owner of the shared code.** A reviewer finding in Core or the window came to me. A finding inside a tool went back to that tool's builder by message. No two agents ever edited the same file.

## What independent review caught

Every serious bug in WinScope was found by an agent that hadn't written the code. Authors test the cases they designed for. Fresh reviewers go after the edges: other accounts, odd file names, elevation, Windows quirks, and the seams between tools. Reviewers got the code and an area to focus on, never my opinion of it.

| Found by | Problem | Why the author missed it |
| --- | --- | --- |
| Storage safety audit | A file name ending in a dot or space could send the wrong file to the Recycle Bin (Windows quietly strips the trailing character) | Storage's 282 passing tests only used names the builder thought of |
| Integration audit | When elevated, WinScope wrote settings and logs into the user's own AppData. A process running as admin trusting a folder the user can write to is a privilege-escalation hole | It was in my shell; no builder owned it, and I'd reviewed my own code |
| Integration audit | The Network graph redrew every screen frame (constant CPU), and closing the app froze for 6 s | Each tool was fine alone; the cost only showed with all four running |
| Events logic audit | Refreshing lost events; merging blue screens swallowed a second crash; a "get an 850 W power supply" hint was wrong | The builder's tests encoded its own understanding of the logs |
| Native interop audit | Nothing: 0 struct layout bugs, proved by checking every size and offset | A clean result from an independent check is worth having for unsafe-looking code |
| Verification round | Temp cleanup matched nothing when Windows uses short names (`C:\Users\USERNA~1`); the 760 px minimum height pushed the window off small laptop screens | The fixes from round 4 were correct but incomplete; only a second fresh pair of eyes saw the gap |
| Privacy audit | My redactor skipped `DNS server 203.0.113.53`, because "server" contains "ver" and it thought it was a version number; it didn't remove emails at all; a Wi-Fi adapter renamed after the network leaked the network's name | I wrote and tested the redactor myself, with inputs I expected |
| Storage builder, mid-fix | My redactor turned `AppData\LocalLow` into `%LOCALAPPDATA%Low` | Builders read the shared code closely while using it, and sometimes spot bugs in it |
| My own test harness, after the audit | 5 bugs in my rewrite of the redactor, including a pattern that took 10 s on a long line | Self-testing does work once it's adversarial, i.e. built to break the code rather than show it works |

The pattern held across all five review rounds. First reviews of new code found a lot: 48 findings, then 25. Verification of the fixes found less but never nothing: 10 findings the first time, 14 the second (4 of them medium). Worth noting: the privacy audit ran the real redactor code against crafted inputs rather than just reading it. Every leak it reported came with the actual input and output, which made the fixes quick and left no arguing over whether a problem was real.

## Resuming builders vs starting fresh

The rule that worked was simple: send fixes back to the agent that wrote the code, and send verification to a stranger. A resumed builder still has its whole context, so a fix costs a fraction of the original build. But it also keeps its own assumptions, so it should never be the one to confirm its own fix worked.

|  | Resumed builder (sent a message) | Fresh agent |
| --- | --- | --- |
| Extra tokens per job | 12k–127k (fixes); 40k–63k (a whole new report section) | 170k–320k, mostly reading code it has never seen |
| Time per job | 1–7 min typically; 17 min for the biggest Storage fix list | 6–14 min |
| Knows the code | Yes: no re-reading, and it remembers why each decision was made | No: rebuilds understanding from the source |
| Shares the author's assumptions | Yes | No |
| Best for | Fixing listed problems, adding features to its own tool, re-running its tests | Reviews and verifying fixes |

Two cautions:

- **Context keeps growing.** Every turn of a resumed agent re-reads everything it has done before, so the reported totals climb. The Storage builder is now at about 510k tokens cumulative, against 292k for its original build. Most of that re-reading is cached and cheap, but the context window is finite. A very long-lived builder would eventually need replacing with a fresh one and a handover note.
- **A resumed builder can rebuild a lot from memory with no outside check.** In the first fix round, the Storage builder rewrote the Recycle Bin code on a raw Windows COM interface (`IFileOperation`), with no Windows machine to run it on. Only the fresh verifier that followed confirmed every interface layout and GUID was right.

## Where it didn't work

The biggest limit is that none of this has run on Windows yet. Every agent compiled and tested on Linux, so the author's first test run on Windows is the real final review.

- **Native code is unproven.** The Windows-specific parts (network tracing, event logs, the Recycle Bin COM interface, GPU counters, the clipboard, Wi-Fi lookups) compile and pass logic tests, but have never executed. Each builder's report ends with a "check on Windows" list.
- **Tests run against stand-ins.** The builders' test projects swap in fakes for the clipboard, the redactor and the elevation check. When I changed the shared redactor:
  - two builders had to update their fakes by hand
  - one Performance test (1 of 145) failed because it expected the old placeholder text, though the module was fine
  - Network's tests can't cover the "admin running as someone else" case at all
- **Builders broke each other's builds** until each built in a private copy (see the set-up section).
- **Small inconsistencies crept in between tools.** Each builder wrote its own small helpers:
  - Storage wrote durations as "2 h 5 min" while the rest said "2h 5m"
  - Network's default adapter-name check only knows English names (German "WLAN" counts as renamed)
- **Cross-tool problems need a coordinator.** Builders can't talk to each other. Events knows the author's Wi-Fi network names and Network prints adapter names; joining those up went through me, and so did triaging every finding into "shell" or "tool".
- **Reports all sound equally sure.** An agent describes a guess in the same tone as a measured result. The best reports labelled their guesses: the privacy auditor wrote "as I understand WPF's implementation; not checked". Treat each report as a claim to verify, not a result.
- **Reviewers aren't completely blank.** They don't see my reasoning, but they do inherit saved memory, which is how one could mention the author's preference for reviews. That's mostly harmless, but it isn't a pure clean-room.
- **It's expensive.** About 3.7 M subagent tokens went into one app, and review and verification were 1.9 M of that, about half. For a tool that only reads data, a single review would do. For code that deletes files, runs as admin or publishes personal data, the extra rounds paid for themselves.

Three more turned up in the last round:

- **A usage limit stopped three builders mid-task.** Their work was saved, and a one-line message resumed each one 25 minutes later. Network had stopped halfway through a change, with an old declaration still in place, and found that itself on resuming. Resuming beat restarting: a fresh agent would have had to rediscover the half-done state.
- **Sharing the real folder still bit.** Builders write finished files into the shared tree. During the last round, Storage hit Network's half-written code when it compiled, and had to stub the other tools to check its own.
- **Review examples leaked into the code.** Reviewers used the author's real name and email as test inputs, and two of those examples ended up in code comments. I swapped them for a made-up name before pushing to the author's public repo. Anything an agent sees can end up in what it writes.

## AirScope: the single-agent comparison

AirScope was built by me alone, then reviewed the same way. The review results look much the same as WinScope's, which suggests the reviews, not the parallel build, are what catch the bugs. Parallel building buys speed, and costs a new category of bugs at the seams between tools.

|  | AirScope 1.1–1.2 | WinScope 1.0–1.1 |
| --- | --- | --- |
| Build | One agent (me), one step at a time | Shell by me, then four builders side by side |
| Reviews | 5 fresh reviewers in two councils, plus 2 verifications | 5 fresh reviewers in a council plus the privacy audit, plus 2 verifications |
| Review tokens | 1.15 M | 1.88 M |
| Biggest catch | Cached Wi-Fi scan results being read as fresh, which caused fake signal dips | Elevated writes to the user's AppData; the Recycle Bin wrong-file case |
| Privacy leaks found | 9, in Screenshot mode | 12, in Reports |
| Bugs at seams between parts | None, one author held the whole picture | Several: the 6 s freeze on close, constant graph CPU, Wi-Fi names known by one tool and shown by another |

In both apps, the feature that hides personal details had the most problems. One author can't imagine every place a name or address turns up. A reviewer who tries crafted inputs finds them quickly.

## Takeaways

1. **Write the shared parts first and freeze them.** The interface, the shared services and a stub of every part let four agents work without seeing each other. Extend the contract with defaults so nobody's code breaks.
2. **Give each builder one folder and its own build copy.** Ownership by folder prevents edit collisions. Private builds stop one agent's half-finished file blocking the rest.
3. **Fix with the author, verify with a stranger.** Resumed builders fix cheaply and quickly. Only a fresh agent, given the code and not the coordinator's conclusions, should judge whether the fix worked.
4. **Always run a verification round.** Even after careful fixes it found 10 more problems the first time.
5. **Make reviewers run the code against crafted inputs.** Findings that come with the real input and output are faster to fix and harder to argue with than findings from reading alone.
6. **Aim the hardest reviews at what can do damage:** deleting files, running as admin, and anything that hides personal data.
7. **Keep one coordinator for the seams.** Someone has to own the shared code, route findings to the right builder, and spot problems that span two tools.
8. **Real-world testing is still a separate step.** Agents with no Windows machine can only promise that the code compiles and the logic tests pass. The author's run on a real PC is the review they can't do.
