# Safeguard flags

A log of every time a safety system interrupts work on this research: a classifier stop, or a flag from the model's safeguards. Building test material for review research (planted bugs and their answer keys) can look like security work to safeguards, so each flag is recorded here as it happens. The background is in the [experiment plan's process note](experiment-plan.md#appeal-stress-test-first-runs-8-nov-2026).

Entries are high level only: they never describe planted bugs or how they could be triggered. Times are UTC.

| Date and time (UTC) | What the session was building | Safeguard | What was offered | What I chose | What happened to the work |
|---|---|---|---|---|---|
| 8 Nov 2026, 23:30 | Harder appeal test material (version 2, a file-sync and backup daemon): writing its detailed answer key | Classifier stop | The session stopped and asked how to go on | Carry on with a terser key: item IDs, file and line, real or decoy, and accepted severities | The detailed key wasn't written |
| 8 Nov 2026, 23:40 | The same material: writing the terser key | Opus 5.5 flag | Claude Code offered to switch to Opus 4.8 | Stay on Opus 5.5 and park the key | The material was committed without a key (`fc7dce7` in the appeal-stress-test repo, 23:46). The key is parked, and the key rule now limits what any key may hold |

## Notes on the entries

- **Times** come from the session's transcript. In it, both events appear the same way: "stopped by a safety classifier", and "Opus 5.5's safeguards stopped the response above". The difference between the two safeguards in the table is from my account.
- **The offer to switch to Opus 4.8** isn't in the transcript, so it's from my account.
- **The key rule** is in `runs/appeal-direct/NEXT-MATERIAL-PLAN.md` (section 9) in the appeal-stress-test repo.
