# Voice-draft audit: how Claude Code handled dictated prompts

An audit of every prompt I drafted in voice mode and pasted into Claude Code, and of what Claude Code did with the factual claims in them. It records confirmations as well as corrections, so the numbers show how often voice drafts were wrong, not only the catches.

Written 7 November 2026 from the local Claude Code session transcripts. Everything here comes from reading those transcripts (the prompt and Claude Code's response in the same turn), not from re-running the checks against the repos. Where a correction is also in the [who-caught-what log](who-caught-what.md), the entry says so.

## Scope and method

- **Transcripts on disk** cover 30 October to 7 November 2026. Nothing older exists locally. Times are UTC.
- **Tagged prompts:** every user prompt containing "drafted in voice mode" or "drafted from a voice-mode conversation" (case-insensitive), across all projects, up to 21:30 UTC on 7 November, when this audit started. That gives 31 hits in 13 sessions. One prompt was sent twice in the same session (a question about plugin hooks), so there are 30 distinct prompts. Two tagged prompts sent after the cutoff (21:37 and 21:38) are not coded.
- **Untagged prompts** (part 3 of the brief) were picked in three groups: (A) prompts from before the tag existed whose text shows they came from a voice-mode conversation (a 31 October session on the human-in-the-loop plan, whose catch log and the prompts themselves say the summaries came from chat Claude in voice mode, plus a 5 November prompt that lists "proposed fixes (from the voice-mode Claude)"); (B) pre-tag prompts in the same pasted, conversational style that ask for claims to be checked in their own words ("check every claim against the actual files"); (C) untagged prompts from the same evening as the tagged ones, in the same sessions, with the same style. Groups B and C are my best guess at voice drafts, not certain ones; the earlier blinded study described below used the same "verify words" group.
- **A claim** is a factual statement in the prompt about code, docs, files, a run, a paper or product behaviour that Claude Code could check. Instructions, questions and design ideas are not claims, except where the prompt presents a design fact that turned out to be inconsistent with the repo; those are marked as such.
- **Outcomes:** **confirmed** (checked and found right), **corrected** (checked and found wrong, incomplete or inconsistent; the prompt's wording was not acted on as written), **not checked** (taken on my word, or not checkable by Claude Code).
- **Not counted as claims:** figures Claude Code itself had produced earlier in the same session and I was repeating back, unless Claude Code re-checked them against a file. Checks Claude Code made of its own earlier work are listed separately.

## Totals

| Group | Prompts | Prompts with at least one correction | Claims checked | Confirmed | Corrected | Not checked |
|---|---|---|---|---|---|---|
| Tagged (5–7 Nov) | 30 distinct (31 hits) | 15 (50%) | 91 | 61 (67%) | 30 (33%) | 6 |
| Untagged A: voice-sourced, 31 Oct and 5 Nov | 7 | 5 | 19 | 9 | 10 | 3 |
| Untagged B: pre-tag, asks for checks in its own words | 12 | 9 | 42 | 21 | 21 | 2 |
| Untagged C: same evening as the tag, no tag | 4 | 2 | 9 | 6 | 3 | 0 |
| Untagged, all | 23 | 16 (70%) | 70 | 36 (51%) | 34 (49%) | 5 |

Other counts:

| Measure | Tagged | Untagged |
|---|---|---|
| Acted on a claim that later proved wrong or unconfirmed | 0 | 1 (a "voice mode doesn't load skills" line was used while flagged as unconfirmed; I had it removed in the next prompt) |
| Draft defects that weren't claims (placeholder left in, message cut off, pasted into the wrong session) | 3 | 3 |
| The same prompt text sent to two sessions, both catching the same errors | 1 pair | 0 |
| Claude Code corrected by me | 1 (it took a repo note saying the takes were made with v3; they were v4) | 1 (I corrected "all 9 runs' reports" to 9 reports across 2 runs) |
| Claude Code corrected its own earlier statement in the turn | 2 | 4 |

**What the numbers say, and don't.** Roughly a third of the checkable claims in tagged voice drafts were wrong or incomplete, and half the tagged prompts had at least one such claim. The untagged prompts that asked for checks in their own words had a higher correction rate, not a lower one. So the tag is not what makes Claude Code check; asking for a check in any wording does, and the correction rate mostly reflects how many checkable claims a prompt carries. Group B was picked because it asks for checks, so its high rate is partly selection. The two groups also differ in date, task and session, so none of this isolates the tag. The one clean result is that no tagged claim was acted on wrongly in these transcripts.

An earlier blinded comparison, run on 7 November from the same transcripts (20 tagged, 15 "verify words", 37 plain untagged prompts, coded by subagents that didn't know the group), found the same pattern: corrections in 40% of tagged prompts, 73% of verify-words prompts and 22% of plain untagged prompts, none of the gaps statistically clear, and no tagged claim acted on wrongly. That study lives in my local research notes, not in this repo.

## Tagged prompts

| # | Date (UTC) | Project | Session | Confirmed | Corrected | Not checked | Notes |
|---|---|---|---|---|---|---|---|
| T1 | 5 Nov 21:01 | four plugin repos | f767b3c2-3658-4d02-bc7e-9b170facd149 | 3 | 1 | 0 | first tagged prompt |
| T2 | 5 Nov 21:57 | langparity | f767b3c2-3658-4d02-bc7e-9b170facd149 | 1 | 3 | 0 | the wrong claims were the portal's message, relayed |
| T3 | 5 Nov 22:17 | local Claude setup | 02dd5207-cae8-434d-b140-0449410e5b60 | 1 | 0 | 0 | |
| T4 | 5 Nov 23:42 | ablationlab-site | 98fcf261-bfc6-4f2e-bbd0-5499779fc45d | 3 | 5 | 1 | |
| T5 | 6 Nov 00:06 | ablationlab-site, org page | 98fcf261-bfc6-4f2e-bbd0-5499779fc45d | 3 | 1 | 1 | placeholder "[PASTE CHOSEN TAGLINE]" left in; Claude stopped and asked |
| T6 | 6 Nov 00:37 | ablationlab-site | 98fcf261-bfc6-4f2e-bbd0-5499779fc45d | 4 | 0 | 0 | all three measured claims right |
| T7 | 6 Nov 00:46 | council-video branding | 98fcf261-bfc6-4f2e-bbd0-5499779fc45d | 1 | 3 | 0 | |
| T8 | 6 Nov 00:57 | council-video | 6c2335d3-35df-40de-9f93-288d979c8a4a | 1 | 1 | 0 | a dictation error |
| T9 | 7 Nov 03:20 | council-video branding | 6c2335d3-35df-40de-9f93-288d979c8a4a | 0 | 3 | 0 | same text as T7, sent to a second session; same three catches |
| T10 | 7 Nov 03:41 | council-video | 6c2335d3-35df-40de-9f93-288d979c8a4a | 2 | 1 | 2 | |
| T11 | 7 Nov 03:56 | council-video | 6c2335d3-35df-40de-9f93-288d979c8a4a | 2 | 1 | 1 | I corrected Claude here (v4, not v3) |
| T12 | 7 Nov 15:35 | plugin install | 5c100b44-2eef-4914-9458-7b3414664c27 | 2 | 0 | 0 | |
| T13 | 7 Nov 15:40 | plugin install | 5c100b44-2eef-4914-9458-7b3414664c27 | 2 | 0 | 0 | |
| T14 | 7 Nov 15:55 and 15:56 | question | fd6b54b4-f1ce-4511-98db-469a01909582 | 0 | 0 | 0 | a question, sent twice; no claims |
| T15 | 7 Nov 16:48 | stowdeck | afd00c33-2fcd-4dfa-8122-f9edec174657 | 3 | 0 | 0 | |
| T16 | 7 Nov 19:00 | council-dial | 9aa52043-8198-4d9a-b24e-530ece72cfb5 | 3 | 0 | 0 | |
| T17 | 7 Nov 19:31 | council-dial | 9aa52043-8198-4d9a-b24e-530ece72cfb5 | 2 | 0 | 0 | turn ended at a clarification question |
| T18 | 7 Nov 19:43 | council-dial | 9aa52043-8198-4d9a-b24e-530ece72cfb5 | 1 | 1 | 0 | who-caught-what entry 2 |
| T19 | 7 Nov 19:45 | transcripts, models | b06058c6-3865-4825-8086-b9d1e2891684 | 3 | 0 | 0 | |
| T20 | 7 Nov 20:23 | council-dial | 9aa52043-8198-4d9a-b24e-530ece72cfb5 | 2 | 1 | 0 | who-caught-what entry 3 |
| T21 | 7 Nov 20:26 | transcripts | cf247806-4754-4929-8664-34e548627c1d | 2 | 0 | 0 | the earlier blinded study |
| T22 | 7 Nov 20:31 | this repo | 8c740c5e-d61a-489a-adee-3f24cf99abb3 | 2 | 2 | 1 | who-caught-what entry 1 |
| T23 | 7 Nov 20:41 | council-dial | 9aa52043-8198-4d9a-b24e-530ece72cfb5 | 3 | 0 | 0 | |
| T24 | 7 Nov 20:44 | this repo | 8c740c5e-d61a-489a-adee-3f24cf99abb3 | 2 | 5 | 0 | who-caught-what entries 5 and 6 |
| T25 | 7 Nov 20:53 | this repo | 8c740c5e-d61a-489a-adee-3f24cf99abb3 | 3 | 0 | 0 | |
| T26 | 7 Nov 21:04 | this repo | 8c740c5e-d61a-489a-adee-3f24cf99abb3 | 2 | 1 | 0 | message cut off at entry 6; nine figures checked against the results file |
| T27 | 7 Nov 21:19 | this repo | 8c740c5e-d61a-489a-adee-3f24cf99abb3 | 0 | 0 | 0 | resend of T26 with the missing items; no new claims |
| T28 | 7 Nov 21:27 | this repo | 8c740c5e-d61a-489a-adee-3f24cf99abb3 | 2 | 1 | 0 | |
| T29 | 7 Nov 21:28 | council-dial | da5508a6-b629-415e-aae7-23d03d50816a | 1 | 0 | 0 | independent review; turn still running when read |
| T30 | 7 Nov 21:30 | this repo | 131969a1-e47d-48e0-8eb9-067a88a9fe36 | 5 | 0 | 0 | the prompt for this audit |

Confirmed claims worth noting: the site column was 608 px wide and the logo dots were 5 units off centre, as dictated (T6); the Stowdeck snapshot, badge and transcript-cleanup descriptions were right (T15); the Council Dial sample, run ids and log paths existed as named (T16, T19, T23); every figure dictated back from the council results file matched it (T26); and the premise of this audit (repo, files, privacy check, commit identity) held (T30).

Not checked: whether the plugins were "submitted to the Claude plugin directory" (T4, T5; taken on my word), the key's credit cap and my chosen voice id (T10; the key can't read them), that the Section 1 takes were made with v4 (T11; the key can't read the history), and the Reddit thread behind the xargs incident (T22; not found by search).

## Corrections in tagged prompts

Each entry: what the prompt said, what was true, how Claude Code found out, and the session. "Log" points to the entry in [who-caught-what.md](who-caught-what.md).

1. **T1, f767b3c2.** Said: keep a "Development" section "taken from the current root README". True: none of the four root READMEs had one. Found by reading the root READMEs; Claude built the section from facts it checked in each repo. Log 8.
2. **T2, f767b3c2.** Said (relaying the portal): the README "spells the remote url host github.com and is given the installer's pass $$". True: no "$$" anywhere in the repo. Found by searching every tracked file. Log 9.
3. **T2, f767b3c2.** Said: "pass" sits near a `$` placeholder. True: the only `$` signs were placeholder examples on another line, far from either "pass". Found by searching the README. Log 9.
4. **T2, f767b3c2.** Said: "the installer's pass". True: Langparity has no installer. Found by reading the repo. Log 9.
5. **T4, 98fcf261.** Said: list the plugins "in the org page's order", then gave a list. True: the list was the plugins-repo README's order; the org page's order differs. Found by fetching the live org page. Log 10.
6. **T4, 98fcf261.** Said: "each was then checked by the plugin directory's own scanner". True: no README says this; they say the plugins were checked with Seaready, "our own pre-check". Found by reading every plugin README. Log 11.
7. **T4, 98fcf261.** Said: the plugins were "reviewed by councils of independent AI reviewers before release". True: only four READMEs say so. Found by reading the READMEs; the site names those four. Log 12.
8. **T4, 98fcf261.** Said: the plugins were "built with Claude Code". True: only one README (Cutproof) says it. Found by searching the READMEs. Log 13.
9. **T4, 98fcf261.** Said: "Windows apps: the apps listed on the org page". True: the org page lists one app, Stowdeck. Found by reading the org page. Log 14.
10. **T5, 98fcf261.** Said, as a contradiction: "Your summary says only Cutproof's README says 'Built with Claude Code', but the sources table says only video-review-tool's README does". True: they are the same plugin; the repo is video-review-tool and its README is titled "Cutproof (video-review-tool)". Found by reading the README. Log 15.
11. **T7, 98fcf261.** Said: "re-export the three PNGs ... banner, profile and thumbnail" from the fixed logo. True: the thumbnail has no beaker or logo; it is the title card with the council tree. Found by checking its source page and pixels. Log 16.
12. **T7, 98fcf261.** Said: commit the branding files. True: the branding folder is excluded from git through the repo's local exclude file, so nothing could be committed. Found with git's ignore check. Log 17.
13. **T7, 98fcf261.** Said: the PNGs are exported "from the fixed logo.svg". True: they are rendered from HTML source pages written by a build script, which still draws the dots off centre; re-running it would undo the fix. Found by reading the build script and re-rendering (pixel-identical to the originals first). Log 18.
14. **T8, 6c2335d3.** Said: a narration line "says an AI overview caught something in our research plan". True: the line is "a separate AI caught structural problems in this research plan"; there is no "AI overview" (a mishearing). Found by reading the script and the take's word timings. Log 19.
15. **T9, 6c2335d3.** Same text as T7 sent to a second session: the thumbnail has no logo (log 16). Found the same way.
16. **T9, 6c2335d3.** Said: re-export the PNGs. True: the banner and profile picture already carried the fix from the night before; re-rendering gave byte-identical files. Found by re-rendering and comparing. Log 20.
17. **T9, 6c2335d3.** Said: commit. True: nothing in git (log 17). Found with git's ignore check.
18. **T10, 6c2335d3.** Said: "make sure the privacy check would catch it [the key] if it ever did", assuming it could. True: the check's pattern covered one vendor's key prefix only, and this vendor's prefix differs, so the key would have been missed. Found by testing the pattern against the key in memory, printing nothing; a pattern and self-test were added. Log 21.
19. **T11, 6c2335d3.** Said: check whether v4 "uses the same voice settings (stability, similarity_boost, style, speaker boost)". True: v4 supports stability and similarity; style, speed and speaker boost are not available. Found from the models endpoint and the v4 docs page. Log 22.
20. **T18, 9aa52043.** Said: the Limits section says "The appeal checks only findings the judge marked OVERSTATED". True: it says NOT REAL, matching the code. Log 2.
21. **T20, 9aa52043.** Said: M12 is planted bug 7, so the judge dismissed a real bug. True: bug 7 was M1 (kept, HIGH); M12 was an unplanted false positive. Log 3.
22. **T22, 8c740c5e.** Said: "xargs -d '\n' gives the correct parent" as the fix. True on GNU only; macOS xargs lacks `-d`. Log 1.
23. **T22, 8c740c5e.** Said: "links to the tool-fallback experiment idea". True: no such idea existed in this repo or any other project. Found by searching all projects; written as a new idea. Log 23.
24. **T24, 8c740c5e.** Said: "In Council Dial 1.2.0 ..." as the current version. True: 1.2.0 existed only in the local working copy; the last commit and the published main were 1.1.0. Found from the git log and the manifests. Log 24.
25. **T24, 8c740c5e.** Said: "'reviewers may not run code' is a brief instruction". True: the brief says "Don't run code from the material unless your brief says the user allowed it", not a flat ban. Found by reading the script; the exact wording was quoted instead. Log 25.
26. **T24, 8c740c5e.** Said: "links to the tool-fallback experiment" again. True: still none (log 23).
27. **T24, 8c740c5e.** Design omission: the principle "hide opinions from the appealer, not facts" without noting that Council Dial's own appeal sees the judge's reasons. Log 6.
28. **T24, 8c740c5e.** Design inconsistency: the hard list says reviewers never run recursive deletes, while the escalation rule sends them to the appealer. Log 5.
29. **T26, 8c740c5e.** Said: "The full record of both runs is in the council-dial repo at results/20261107-council-runs.md ... link to it". True: the file was only staged there, not committed or pushed, so the link would have failed. Found by listing the remote branch's tree; flagged, link kept. Log 26.
30. **T28, 8c740c5e.** Said: the calculator's templates would start "from best guesses". The plan's own Learning bullet says the calculator is built only after the test runs so its templates use real results. Inconsistency flagged; wording kept for my call. Found by reading the section. Log 27.

## Untagged prompts

### Group A: voice-sourced before the tag

| # | Date (UTC) | Project | Session | Confirmed | Corrected | Not checked | Evidence of voice drafting |
|---|---|---|---|---|---|---|---|
| U1 | 31 Oct 19:45 | human-in-the-loop | 1d1bbe62-11ec-4784-9227-48a49f3a3f46 | 2 | 2 | 3 | the plan says chat Claude was used "in voice and text"; the next prompts say the summaries came from voice mode |
| U2 | 31 Oct 19:55 | human-in-the-loop | 1d1bbe62-11ec-4784-9227-48a49f3a3f46 | 0 | 1 | 0 | same session |
| U3 | 31 Oct 19:58 | human-in-the-loop | 1d1bbe62-11ec-4784-9227-48a49f3a3f46 | 0 | 0 | 0 | prompt records "in voice mode, chat Claude ... two summaries turned out wrong" |
| U4 | 31 Oct 20:09 | human-in-the-loop | 1d1bbe62-11ec-4784-9227-48a49f3a3f46 | 4 | 2 | 0 | same session |
| U5 | 31 Oct 20:16 | human-in-the-loop, all repos | 1d1bbe62-11ec-4784-9227-48a49f3a3f46 | 0 | 2 | 0 | catch-log row names "Chat Claude (snippet-level summary in voice mode)" |
| U6 | 31 Oct 20:26 | all public repos | 1d1bbe62-11ec-4784-9227-48a49f3a3f46 | 2 | 0 | 0 | same session |
| U7 | 5 Nov 03:17 | claude-lore | 02dd5207-cae8-434d-b140-0449410e5b60 | 1 | 3 | 0 | lists "proposed fixes (from the voice-mode Claude)" |

### Group B: before the tag, asks for checks in its own words

| # | Date (UTC) | Project | Session | Confirmed | Corrected | Not checked | Notes |
|---|---|---|---|---|---|---|---|
| U8 | 31 Oct 16:20 | council-video | 6c2335d3-35df-40de-9f93-288d979c8a4a | 2 | 1 | 0 | citations checked by a subagent; result landed in the next turn |
| U9 | 31 Oct 16:30 | council-video | 6c2335d3-35df-40de-9f93-288d979c8a4a | 1 | 0 | 0 | "some of these may already be in": two were |
| U10 | 31 Oct 16:36 | research-framework | 8fa7b85f-75e5-464f-a3ea-ad6859640d4d | 0 | 0 | 0 | the same prompt pasted into the wrong project; no claims checked |
| U11 | 31 Oct 21:57 | council-video, this repo | 6c2335d3-35df-40de-9f93-288d979c8a4a | 1 | 1 | 0 | |
| U12 | 31 Oct 22:40 | this repo | b0d429ed-7c71-44d0-abf9-b21fcfe5d4da | 0 | 2 | 0 | |
| U13 | 2 Nov 23:19 | this repo | 64ab5a39-df08-4596-a7fa-db4eb81f2d58 | 7 | 0 | 0 | five claims about three papers, all supported with nuances |
| U14 | 3 Nov 01:42 | stowdeck (then SessionKeeper) | 8bc4afb4-bcdd-4789-bd2c-15163687a8c5 | 1 | 4 | 0 | |
| U15 | 5 Nov 01:51 | claude-lore | 02dd5207-cae8-434d-b140-0449410e5b60 | 2 | 1 | 1 | the unconfirmed voice-mode line was used, flagged, and later removed |
| U16 | 5 Nov 02:49 | video-review-tool | 02dd5207-cae8-434d-b140-0449410e5b60 | 1 | 2 | 0 | |
| U17 | 5 Nov 05:06 | stowdeck (then SessionKeeper) | 02dd5207-cae8-434d-b140-0449410e5b60 | 1 | 1 | 1 | |
| U18 | 5 Nov 05:26 | overnight build (five plugins) | a7e7a8f9-6a7a-4a54-b021-b57529ec0f2c | 1 | 1 | 0 | |
| U19 | 5 Nov 20:31 | org page, four plugin repos | f767b3c2-3658-4d02-bc7e-9b170facd149 | 4 | 8 | 0 | 30 minutes before the first tagged prompt |

### Group C: same evening as the tag, no tag

| # | Date (UTC) | Project | Session | Confirmed | Corrected | Not checked | Notes |
|---|---|---|---|---|---|---|---|
| U20 | 7 Nov 20:58 | this repo | 8c740c5e-d61a-489a-adee-3f24cf99abb3 | 4 | 2 | 0 | message cut off at entry 6 |
| U21 | 7 Nov 21:11 | this repo | 8c740c5e-d61a-489a-adee-3f24cf99abb3 | 0 | 0 | 0 | cut off again; nothing done |
| U22 | 7 Nov 21:21 | this repo | 8c740c5e-d61a-489a-adee-3f24cf99abb3 | 0 | 0 | 0 | no claims; Claude found the researcher's first name in two unpushed pilot files and in a pushed file |
| U23 | 7 Nov 20:47 | council-dial | 9aa52043-8198-4d9a-b24e-530ece72cfb5 | 2 | 1 | 0 | I caught Claude's "all 9 runs' reports" wording |

## Corrections in untagged prompts

1. **U1, 1d1bbe62.** Said: a position paper found that "approvals come too fast and too often to check". True: its abstract says nothing about that; only the skills-erosion point is there. Found by fetching the abstract. Log 28.
2. **U1, 1d1bbe62.** Said: an oversight paper finds failures "are usually caused by automation bias, complacency and over-reliance, not missing information". True: its abstract proposes a layered agency framework against rubber-stamping and says nothing of the sort. Found by fetching the abstract. Log 29.
3. **U2, 1d1bbe62.** Said: keep the row's "Supports H2 and H3". True: the H3 support rested on the wrong "approvals too fast" claim, so only H2 was supported. Claude flagged it; I cut it in the next prompt. Log 30.
4. **U4, 1d1bbe62.** Said: a vendor guide "advises against tool calls inside the voice loop". True: it advises against them only for extracting, summarising or classifying what was just said. Found by fetching the page. Log 31.
5. **U4, 1d1bbe62.** Said: a research digest shows "speaking aloud compensated". True: it covers two tasks only and presents this as a suggestion, not a finding. Found by fetching the page. Log 32.
6. **U5, 1d1bbe62.** Said: "my other seven local repos", then listed eight. True: eight. Found by counting; all eight were set up. Log 33.
7. **U5, 1d1bbe62.** Said: "the four already-public repos". True: five were public. Found by checking each remote. Log 33.
8. **U7, 02dd5207.** Said (fix a): rename the lock id "everywhere, including tests". True: no test mentions it. Found by three independent reviewers reading the code. Log 34.
9. **U7, 02dd5207.** Said (fix c): "replace any download-and-run install line in the READMEs with clone-then-run". True: no such line exists; the README already does clone-then-run. Found by searching for curl, wget and similar. Log 35.
10. **U7, 02dd5207.** Said (fix d): "leave the icon mentions alone". True: two of the three icon mentions (a test that opens the icon, and a code block naming the file) are exactly what the policy hold flags. Found by reading the code and the portal's docs. Log 36.
11. **U8, 6c2335d3.** Said: in the 2026 study "small models debated reasoning puzzles". True: the tasks were maths, word problems, multiple-choice questions and biographies. Found by reading the paper; the script now says "maths and quiz questions". Log 37.
12. **U11, 6c2335d3.** Asked to check: "did one-reviewer teams really find defects about as well as two- and four-reviewer teams?" True: the full text says two-person teams equalled four-person teams and both beat one person; the abstract never compares sizes. Found by reading the authors' 42-page technical report. The same wrong line was in this repo's plan and was fixed there too. Log 38.
13. **U12, b0d429ed.** Said: six papers "cited in my plans". True: only one was cited in this repo; three were in a grant draft elsewhere; two weren't cited anywhere. Found by searching the projects. Log 39.
14. **U12, b0d429ed.** Said: "my judge-favouritism experiment". True: no such experiment was written down; treated as the outside-judge and self-review arms. Found by searching the projects. Log 39.
15. **U14, 8bc4afb4.** Said: the save dialog is "untick any sessions you don't want, name the snapshot, optionally add a note per session, save". True: it also lists the last 24 hours of other sessions unticked, has a note for the whole snapshot, and the button is "Save snapshot". Found by reading the window code and labels. Log 40.
16. **U14, 8bc4afb4.** Said: what gets saved is "each session's ID, project folder and note". True: also the title, last message and last-active time, plus the snapshot's name, time and note. Found by reading the model code. Log 40.
17. **U14, 8bc4afb4.** Said: restore reopens each session "in its own PowerShell window or Terminal tab" and resumes the conversation. True: Terminal tabs open in one window; entries saved without a session id start a new conversation; the app asks before reopening running sessions. Found by reading the launcher code. Log 40.
18. **U14, 8bc4afb4.** Said: "Select all from today" selects today's sessions. True: it also unticks older rows. Found by reading the code. Log 40.
19. **U15, 02dd5207.** Said: "check that plugin.json and marketplace.json descriptions mention that the plugin installs a hook". True: the plugin installs no hook; only the installer adds it. Found by reading the plugin code and tests; the descriptions now say the opposite. Log 41.
20. **U16, 02dd5207.** Said: Cutproof "lines up your recorded narration with what's on screen". True: it doesn't transcribe speech; the narration comes from a script, subtitles or recording table. Found by reading the script. Log 42.
21. **U16, 02dd5207.** Said: "nothing is uploaded or downloaded". True: frames reach Anthropic when Claude opens them, and Remotion may download its own headless browser; changed to "makes no network requests of its own". Found by reading the code and the review flow. Log 42.
22. **U17, 02dd5207.** Said: the plugin "can work without them [auto-generated titles]". True: no option to hide titles existed, so it was changed to "can be changed to work without them". Found by reading the code. Log 43.
23. **U18, a7e7a8f9.** Said: "New skills only load when a session starts". True: Claude Code picked up the new skill mid-session. Found by observing it during the run. Log 44.
24. **U19, f767b3c2.** Said: Cutproof produces "frames plus a timed transcript of the narration". True: no transcription; see 20. Found by reading the README. Log 45.
25. **U19, f767b3c2.** Said: Tangent Jar "helps you stay on track in any Claude Code session". True: only in a focus session you start. Found by reading the README. Log 45.
26. **U19, f767b3c2.** Said: the Stowdeck plugin "works with the Stowdeck Windows app". True: it can't do anything without it; "needs". Found by reading the plugin README. Log 45.
27. **U19, f767b3c2.** Said: Stowdeck keeps "a tab for your other AI terminal windows". True: the tab also lists dev servers and plain shells. Found by reading the README. Log 45.
28. **U19, f767b3c2.** Said: Seaready catches "the problems the portal would hold it for: names that look like credentials or are already taken". True: it catches many of them, not all, and the credential check is about identifiers in code, not plugin names. Found by reading the README. Log 45.
29. **U19, f767b3c2.** Said: Bench Diary "never logs secrets or personal details". True: its Limits say what to log is Claude's judgement; "leaves out". Found by reading the README. Log 45.
30. **U19, f767b3c2.** Said: Langparity "checks translations ... and catches the mistakes". True: an overclaim the README doesn't make; dropped. Found by reading the README. Log 45.
31. **U19, f767b3c2.** Said: Council Dial can keep "only what the reviewers agree on". True: it's a majority consensus. Found by reading the README. Log 45.
32. **U20, 8c740c5e.** Said: run 1's "planted" description is one "which Council Dial 1.2.0 would now refuse". True: both 1.1.0 (published) and 1.2.0 refuse it. Found by running both versions' check on the stored description. Log 46.
33. **U20, 8c740c5e.** Said: the reference implementation matches the "move, don't delete" idea. True: the doc no longer used that phrase; reworded to the pattern it does describe. Found by searching the doc. Log 46.
34. **U23, 9aa52043.** Said: cite findings as "2f23/M12". True: the four-character part of a run id can repeat on another date, so only the full run id is unambiguous. Found by reading the id format in the script. Log 47.

## Other observations from the transcripts

- **Draft defects that weren't claims:** a placeholder "[PASTE CHOSEN TAGLINE]" left in a tagged prompt (T5); two tagged messages and two untagged ones cut off mid-list (T26, U20, U21, and T27 resent the full text); one prompt pasted into the wrong project (U10). Claude Code stopped and asked in every case except U10, where it had nothing to act on.
- **Repeated prompts:** T7 and T9 are the same text sent to two sessions three hours apart. Both sessions caught the same three errors, independently.
- **Where Claude Code was wrong and caught by me:** it assumed the narration takes were v3 from the repo's own gitignore note; I corrected it to v4 (T11). Its "all 9 runs' reports" wording meant 9 reports across 2 runs (U23).
- **Where Claude Code corrected itself within a turn:** a results file named the wrong cheapest reviewer (T26); a README line number cited earlier had moved (T23); a broken privacy-check pattern had reported "no hits" without checking anything, caught after the push (U2); "none of your repos has a check" missed one repo's untracked script (U5); "the claude.ai copies are gone" was wrong, a fresh session still loaded them (U16).
- **Catches that were not prompt claims but are worth the log:** the researcher's surname was still served by GitHub from an old commit after a history rewrite (T5); two unpushed pilot files and one pushed file named the researcher (U22); the privacy check would have missed the key's format (T10); the review log recorded no model for any run (T19).

## Limits of this audit

- It is one reader's coding of transcripts, done in one pass, with no second coder. Granularity matters: a dictated list of five plugin facts counts as five claims, a dictated paragraph of design as none, so the ratios depend on these choices.
- Claims were coded from what Claude Code reported checking. A claim it checked silently and found right may be missing from the confirmed count.
- The untagged groups were chosen for signs of voice drafting or for asking for checks, which selects for prompts with checkable claims. They are not a random sample of untagged prompts; the earlier blinded study drew one and is summarised above.
- The tag's wording varied across the 30 prompts; the first four also say "tell me which ones were wrong", which invites an itemised report.
- Several turns were still running or ended at a clarification question when the transcript was read (T17, T21, T29, U7, U8), so corrections that landed in the next turn are counted only where the next turn was read (U7, U8).
