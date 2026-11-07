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
