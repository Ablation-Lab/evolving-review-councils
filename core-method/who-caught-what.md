# Who caught what

I keep this log to record who caught what during the research: me (the researcher), chat Claude, Claude Code and council agents. Each entry says who caught it, whose claim or work it corrected, and what it was.

**Checked** means the entry was verified against the repos, and the source is given. **Reported, not checked** means it couldn't be verified that way.

## 7 Nov 2026

1. **`xargs -d '\n'` is GNU-only**
   - **Caught by:** Claude Code
   - **Corrected:** chat Claude, which suggested `xargs -d '\n'` as the fix for the [agent `rm -rf` incident](experiment-plan.md#command-gating-what-reviewers-may-run-prompted-by-an-agent-rm--rf-incident-nov-2026)
   - **What:** `-d` is a GNU option, and the xargs that ships with macOS doesn't have it, so the portable fix is NUL-separated input with `-0`.
   - **Status:** checked on GNU xargs 4.10, where `-d '\n'` gives the correct parent. That macOS's xargs lacks `-d` comes from its documented options; it wasn't run on a Mac. That chat Claude suggested `-d`: reported, not checked.

2. **The README's appeal limit says NOT REAL, not OVERSTATED**
   - **Caught by:** Claude Code
   - **Corrected:** a voice-drafted claim that Council Dial's README Limits section said OVERSTATED
   - **What:** the Limits section says "The appeal checks only findings the judge marked NOT REAL, not ones it marked OVERSTATED", which matches the code: the appeal brief covers only findings the judge marked NOT REAL.
   - **Status:** checked, in council-dial's `README.md` and `plugin/README.md` (Limits) and `appealBrief()` in `plugin/skills/council-dial/scripts/council.mjs`. The draft's wording: reported, not checked.

3. **Run 2's M12 wasn't planted bug #7**
   - **Caught by:** Claude Code
   - **Corrected:** a voice-drafted claim that run `20261107-2f23`'s M12 was planted bug #7
   - **What:** in run 2, bug #7 (the unchecked `.slugs` path) was `20261107-2f23/M1`, judged REAL, HIGH. Its M12 was an unplanted false positive, dismissed by the judge, and the appeal agreed. Run 1's judge had numbered the path bug M12 (`20261107-f675/M12`, dismissed), and finding numbers restart every run, which caused the mix-up.
   - **Status:** checked, in council-dial's `results/20261107-council-runs.md` (the planted-bug tables and the notes on each M12). The draft's wording: reported, not checked.

4. **Run 1's target description said "planted"**
   - **Caught by:** Claude Code
   - **Corrected:** run 1's setup (`20261107-f675`, on Council Dial 1.0.0)
   - **What:** run 1's stored target description said "made-up module with planted problems", and it went into every brief. Telling reviewers the material has planted problems changes how they review it. Council Dial now refuses descriptions like that.
   - **Status:** checked. The review log stores that description, and `results/20261107-council-runs.md` records the catch. Run 1's description is refused by both 1.2.0 (in progress) and 1.1.0 (published on main): "the description of what to review says "planted"".

5. **The hard list and the escalation rule contradicted each other**
   - **Caught by:** Claude Code
   - **Corrected:** the voice-drafted command-gating design
   - **What:** the hard list said reviewers never run recursive deletes, while the escalation rule sent recursive deletes to the appealer, so it wasn't clear why a command that can never run would need escalating. Resolved by "How the tiers fit together" in the [command-gating section](experiment-plan.md#command-gating-what-reviewers-may-run-prompted-by-an-agent-rm--rf-incident-nov-2026): reviewers can only propose hard-list commands, proposals go straight to the appealer, and nothing on the list runs without a final yes from the user.
   - **Status:** checked, in this repo (commit `a46fedf`).

6. **Council Dial's appeal sees the judge's opinions**
   - **Caught by:** Claude Code
   - **Corrected:** the voice-drafted command-gating design, which didn't note that Council Dial's own appeal works the other way
   - **What:** Council Dial's current appeal sees the judge's reasons for each dismissal (opinions), unlike the command-gating principle "hide opinions from the appealer, not facts".
   - **Status:** checked, in council-dial's `plugin/README.md` (the Appeal row: "with the judge's reasons") and `appealBrief()` in `plugin/skills/council-dial/scripts/council.mjs` ("each with the judge's reasons").

7. **The appeal can't catch severity downgrades, and the two runs' minutes aren't comparable**
   - **Caught by:** chat Claude
   - **Corrected:** Council Dial's appeal design, and comparisons of the two runs' times
   - **What:** the appeal sees only findings the judge marked NOT REAL, so a real HIGH bug that the judge marks OVERSTATED and cuts to LOW is never appealed. Run 1's 3.9 minutes are wall time and run 2's 3.2 minutes are the agents' critical path, so the two can't be compared.
   - **Status:** both facts checked: the appeal limit in council-dial's README Limits section ("The appeal checks only findings the judge marked NOT REAL, not ones it marked OVERSTATED"), and the minutes in `results/20261107-council-runs.md` ("The two times measure different things and can't be compared"). That chat Claude caught them: reported, not checked.

**Human-in-the-loop note:** both voice-drafted claims (entries 2 and 3) were caught because each voice-drafted prompt ends with a line asking Claude Code to verify claims before acting. As in the entries themselves, the voice drafts' wording in entries 2 and 3 is reported, not checked. This belongs in the human-in-the-loop part of the research.

## Voice-draft audit (added 7 Nov 2026)

These entries come from the [voice-draft audit](voice-draft-audit.md) of every voice-drafted prompt in my local Claude Code transcripts, 31 Oct to 7 Nov 2026. Entries 1 to 7 above already cover five of the audit's corrections. Each entry below is one more claim in a voice draft that Claude Code checked and found wrong, incomplete or inconsistent.

**Status for every entry below: transcript.** The check and its result are recorded in the Claude Code session transcript named by its first eight characters; they were not re-run against the repos for this log. The draft's wording is quoted from the prompt in the transcript. "Tagged" means the prompt carried the voice-mode line asking Claude Code to verify claims; "untagged" means it didn't.

8. **No root README had a Development section** (5 Nov, session f767b3c2, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's "keep a short ... 'Development' section at the end, taken from the current root README" for four plugin repos
   - **What:** none of the four root READMEs had a Development section, so there was nothing to take; Claude Code built one from facts it checked in each repo.

9. **The portal's "installer's pass $$" wording didn't match the repo** (5 Nov, f767b3c2, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's relay of a directory-portal hold on Langparity
   - **What:** no "$$" appears anywhere in the repo; "pass" is never next to a `$` placeholder; and Langparity has no installer. The hold's quote looked stitched together from words on different lines.

10. **The plugin list wasn't in the org page's order** (5 Nov, 98fcf261, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's plugin list for the website, given as "the org page's order"
   - **What:** the list followed the plugins-repo README; the live org page orders them differently, and the site used that order.

11. **No repo says the plugins were checked by the directory's own scanner** (5 Nov, 98fcf261, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's "each was then checked by the plugin directory's own scanner"
   - **What:** every README says the plugins were checked with Seaready, our own pre-check, and that the directory's validation and reviewers make the actual decision.

12. **Only four plugins' READMEs mention a review council** (5 Nov, 98fcf261, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's "reviewed by councils of independent AI reviewers before release", said of all the plugins
   - **What:** four READMEs say so; the site names only those four.

13. **Only one README says "built with Claude Code"** (5 Nov, 98fcf261, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's "the plugins were built with Claude Code"
   - **What:** only Cutproof's README says it; the general sentence was dropped from the site.

14. **The org page lists one Windows app, not several** (5 Nov, 98fcf261, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's "Windows apps: the apps listed on the org page"
   - **What:** the org page lists Stowdeck only.

15. **Cutproof and video-review-tool are the same plugin** (6 Nov, 98fcf261, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's claim that two of Claude Code's statements contradicted each other ("only Cutproof's README" versus "only video-review-tool's README")
   - **What:** the repo is video-review-tool and its README is titled "Cutproof (video-review-tool)"; both statements were right.

16. **The thumbnail has no logo** (6 Nov and 7 Nov, 98fcf261 and 6c2335d3, tagged)
   - **Caught by:** Claude Code, in two sessions independently
   - **Corrected:** the voice draft's "re-export the three PNGs ... banner, profile and thumbnail" from the fixed logo
   - **What:** the thumbnail is the title card with the council tree; it has no beaker, so there was nothing to move.

17. **The branding folder isn't in git** (6 Nov and 7 Nov, 98fcf261 and 6c2335d3, tagged)
   - **Caught by:** Claude Code, in two sessions independently
   - **Corrected:** the voice draft's instruction to commit the re-exported branding files
   - **What:** the folder is excluded through the repo's local exclude file, so no tracked file changed and nothing could be committed.

18. **The branding PNGs aren't rendered from logo.svg** (6 Nov, 98fcf261, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's "re-export ... from the fixed logo.svg"
   - **What:** the PNGs come from HTML source pages written by a build script, which still draws the dots off centre; re-running it would undo the fix. Claude Code first confirmed that re-rendering the unchanged pages reproduced the old PNGs pixel for pixel.

19. **"AI overview" was a mishearing** (6 Nov, 6c2335d3, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's description of a narration line that "says an AI overview caught something in our research plan"
   - **What:** the script says "a separate AI caught structural problems in this research plan"; there is no "AI overview".

20. **The banner and profile picture were already fixed** (7 Nov, 6c2335d3, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's request to re-export them
   - **What:** both had been re-exported the night before; re-rendering gave byte-identical files, so nothing was changed.

21. **The privacy check would have missed the text-to-speech key** (7 Nov, 6c2335d3, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's assumption behind "make sure the privacy check would catch it if it ever did"
   - **What:** the check's secret pattern covered one vendor's key prefix only; this vendor's keys use a different prefix. Tested against the real key in memory with nothing printed; a pattern and a self-test were added.

22. **v4 doesn't take style or speaker boost** (7 Nov, 6c2335d3, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's list of v4 voice settings "(stability, similarity_boost, style, speaker boost)"
   - **What:** the models endpoint and the v4 docs page agree that v4 uses stability and similarity only; style, speed and speaker boost are not available.

23. **There was no tool-fallback experiment to link to** (7 Nov, 8c740c5e, tagged, twice)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's "links to the tool-fallback experiment idea", in two prompts
   - **What:** no such idea existed in this repo or any other project, so the section proposes it as a new one.

24. **Council Dial 1.2.0 wasn't the current version** (7 Nov, 8c740c5e, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's "In Council Dial 1.2.0, ..." as a statement of the current state
   - **What:** 1.2.0 existed only in the local working copy; the last commit and the published main were 1.1.0. The section now says the rule is the same in both.

25. **The run-code rule isn't a flat ban** (7 Nov, 8c740c5e, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's "'reviewers may not run code' is a brief instruction"
   - **What:** the brief says "Don't run code from the material unless your brief says the user allowed it"; the exact wording is quoted in the section.

26. **The results-file link would have failed** (7 Nov, 8c740c5e, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's "The full record of both runs is in the council-dial repo at results/20261107-council-runs.md ... link to it"
   - **What:** the file was only staged in that repo, not committed or pushed, so the link would 404 until it reached main. Flagged; the link was kept.

27. **"Best guesses" contradicts the calculator's Learning bullet** (7 Nov, 8c740c5e, tagged)
   - **Caught by:** Claude Code
   - **Corrected:** the voice draft's new line that the calculator's templates start "from best guesses"
   - **What:** the plan's Learning bullet says the calculator is built only after the test runs, so its templates use real results. Flagged as an inconsistency for me to resolve.

28. **A position paper's abstract doesn't say approvals come too fast** (31 Oct, 1d1bbe62, untagged, voice-sourced)
   - **Caught by:** Claude Code
   - **Corrected:** chat Claude's related-work summary, relayed in the prompt: "approvals come too fast and too often to check"
   - **What:** the abstract supports only the point that long AI use erodes oversight skills.

29. **An oversight paper's summary didn't match its abstract** (31 Oct, 1d1bbe62, untagged, voice-sourced)
   - **Caught by:** Claude Code
   - **Corrected:** chat Claude's summary, relayed in the prompt: failures are "usually caused by automation bias, complacency and over-reliance, not missing information"
   - **What:** the abstract proposes a layered agency framework to stop oversight becoming a rubber stamp and says nothing of the sort.

30. **"Supports H3" no longer held** (31 Oct, 1d1bbe62, untagged, voice-sourced)
   - **Caught by:** Claude Code
   - **Corrected:** the prompt's instruction to keep a row's "Supports H2 and H3"
   - **What:** the H3 support rested on the wrong "approvals too fast" claim (entry 28); Claude Code flagged it and the row became "Supports H2."

31. **A vendor guide's advice was narrower than the summary** (31 Oct, 1d1bbe62, untagged, voice-sourced)
   - **Caught by:** Claude Code
   - **Corrected:** chat Claude's voice-mode summary, relayed in the prompt: the guide "advises against tool calls inside the voice loop"
   - **What:** it advises against them only for extracting, summarising or classifying what was just said, not tool use in general.

32. **A research digest's finding was a suggestion over two tasks** (31 Oct, 1d1bbe62, untagged, voice-sourced)
   - **Caught by:** Claude Code
   - **Corrected:** the summary's "speaking aloud compensated"
   - **What:** the digest covers two tasks and presents the point as a suggestion, not a confirmed finding.

33. **Eight repos, not seven; five public, not four** (31 Oct, 1d1bbe62, untagged, voice-sourced)
   - **Caught by:** Claude Code
   - **Corrected:** the prompt's "my other seven local repos" (eight were listed) and "the four already-public repos" (five were public)
   - **What:** all eight were set up, and the fifth public repo was treated as needing approval too.

34. **No test mentioned the lock id** (5 Nov, 02dd5207, untagged, voice-sourced)
   - **Caught by:** a council of three reviewer subagents, merged by Claude Code
   - **Corrected:** the voice-mode Claude's proposed fix "rename it ... everywhere, including tests"
   - **What:** the id is a random lock-file value, never read from the environment; no test mentions it, so the tests needed no change.

35. **There was no download-and-run install line to replace** (5 Nov, 02dd5207, untagged, voice-sourced)
   - **Caught by:** a council of three reviewer subagents, merged by Claude Code
   - **Corrected:** the voice-mode Claude's proposed fix "replace any download-and-run install line in the READMEs with clone-then-run"
   - **What:** a search found no such line; the README already did clone-then-run. The portal's warning probably came from the clone and the run sharing one code block.

36. **The icon mentions were what triggered the hold** (5 Nov, 02dd5207, untagged, voice-sourced)
   - **Caught by:** a council of three reviewer subagents, merged by Claude Code
   - **Corrected:** the voice-mode Claude's proposed fix "leave the icon mentions ... alone"
   - **What:** a test that opens the icon file and a code block naming it are exactly what the directory policy flags; both were changed, and the documented manifest field was kept.

37. **The 2026 study's tasks weren't "reasoning puzzles"** (31 Oct, 6c2335d3, untagged, asks for checks)
   - **Caught by:** Claude Code's claim-check subagent
   - **Corrected:** the prompt's narration line "when small models debated reasoning puzzles"
   - **What:** the paper's tasks were maths, word problems, multiple-choice questions and biographies; the script now says "maths and quiz questions".

38. **One reviewer alone did worse in the 1997 inspection study** (31 Oct, 6c2335d3, untagged, asks for checks)
   - **Caught by:** Claude Code
   - **Corrected:** the script line, and this repo's plan, saying one-reviewer teams found defects about as well as two- and four-reviewer teams
   - **What:** the authors' full technical report says two-person teams equalled four-person teams and both beat one person; the abstract never compares sizes. Claude Code saved a rule to open the full text before citing a paper.

39. **Most of the "papers cited in my plans" weren't cited there** (31 Oct, b0d429ed, untagged, asks for checks)
   - **Caught by:** Claude Code
   - **Corrected:** the prompt's "papers ... cited in my plans" and "my judge-favouritism experiment"
   - **What:** only one of the six papers was cited in this repo; three were in a grant draft elsewhere and two nowhere. No judge-favouritism experiment was written down, so it was read as the outside-judge and self-review arms.

40. **The dictated app walkthrough differed from the app in four places** (3 Nov, 8bc4afb4, untagged, asks for checks)
   - **Caught by:** Claude Code
   - **Corrected:** the prompt's step-by-step description of Stowdeck (then SessionKeeper) for its README
   - **What:** the save dialog also lists the last 24 hours of other sessions unticked, has a whole-snapshot note and a "Save snapshot" button; saved data also includes each session's title, last message and last-active time; Terminal tabs open in one window, entries without a session id start a new conversation, and the app asks before reopening running sessions; "Select all from today" also unticks older rows. The README followed the app.

41. **The plugin installs no hook** (5 Nov, 02dd5207, untagged, asks for checks)
   - **Caught by:** Claude Code
   - **Corrected:** the prompt's "check that plugin.json and marketplace.json descriptions mention that the plugin installs a hook"
   - **What:** only the installer adds the optional daily hook; a plugin-only install can't. The descriptions now say the plugin installs no hooks.

42. **Cutproof doesn't transcribe, and isn't fully offline** (5 Nov, 02dd5207, untagged, asks for checks)
   - **Caught by:** Claude Code
   - **Corrected:** the dictated README paragraph: "lines up your recorded narration" and "nothing is uploaded or downloaded"
   - **What:** the narration comes from a script, subtitles or recording table, not from the audio; frames reach Anthropic when Claude opens them, and Remotion may download its own headless browser. The paragraph now says "from your script or subtitles" and "makes no network requests of its own".

43. **No option to hide session titles existed** (5 Nov, 02dd5207, untagged, asks for checks)
   - **Caught by:** Claude Code
   - **Corrected:** the dictated reviewer note "it can work without them"
   - **What:** the app had no such option, so the note says it "can be changed to work without them".

44. **New skills can load mid-session** (5 Nov, a7e7a8f9, untagged, asks for checks)
   - **Caught by:** Claude Code
   - **Corrected:** the prompt's "New skills only load when a session starts" (also in my memory notes at the time)
   - **What:** Claude Code picked up the newly installed skill during the same session.

45. **Eight dictated org-page descriptions didn't match the READMEs** (5 Nov, f767b3c2, untagged, asks for checks)
   - **Caught by:** Claude Code
   - **Corrected:** the prompt's draft "What it does" text for nine tools, given "as a starting point" with "check every claim against that tool's own README first"
   - **What:** Cutproof doesn't make "a timed transcript of the narration"; Tangent Jar works in a focus session you start, not "any Claude Code session"; the Stowdeck plugin needs the app rather than "works with" it; Stowdeck's Terminals tab also lists dev servers and plain shells, not only "AI terminal windows"; Seaready catches "many of" the portal's problems, and its credential check is about identifiers in code, not plugin names; Bench Diary "leaves out" secrets rather than "never logs" them; Langparity doesn't claim to catch "the mistakes"; Council Dial's consensus is a majority, not "only what the reviewers agree on".

46. **Both published versions refuse the "planted" description** (7 Nov, 8c740c5e, untagged, same evening)
   - **Caught by:** Claude Code
   - **Corrected:** the dictated log entry "which Council Dial 1.2.0 would now refuse" (entry 4 above now says both), and a reference to the doc's "move, don't delete" idea
   - **What:** 1.1.0, published on main, refuses run 1's description as well as 1.2.0; and the doc no longer used the phrase "move, don't delete", so the reference line names the pattern it does describe.

47. **Short run ids are ambiguous** (7 Nov, 9aa52043, untagged, same evening)
   - **Caught by:** Claude Code
   - **Corrected:** the prompt's example of citing findings as "2f23/M12"
   - **What:** the four-character part of a run id is random per day and can repeat on another date, so findings are cited with the full run id.
