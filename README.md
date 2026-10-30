# Evolving Review Councils

An experiment plan: AI reviewer councils that evolve over generations, to find how many reviewers each kind of task is worth.

When AI agents build software, a council of reviewer agents checks the work for bugs, security holes and risky changes. Here the council evolves. Each generation tries to improve on the best version so far, and a change is kept only if it beats a fixed set of hard tests. Held-out tests the agents never see catch gaming. Repeating the runs at different council sizes and on tasks of different complexity shows where one more reviewer stops paying for itself.

<!-- Teaser video goes here. -->

> **Teaser video:** coming soon.

The explainer video's Remotion source, script and narration are in [ablation-lab/council-video](https://github.com/ablation-lab/council-video).

## Core method

- [Experiment plan](core-method/experiment-plan.md): the full plan. It covers how "improved" is measured, evolution and stopping rules, keeping tests unbiased, cheating and collusion checks, failure modes, hard limits, the test plan and the final report.
- [How the agents built and reviewed WinScope](core-method/winscope-pilot.md): the informal pilot. Fresh reviewers found 97 problems the builders' own tests had passed, across 11 rounds and about 3.7M subagent tokens.
- [Council size by task complexity](core-method/council-size-by-task-complexity.md): whether the best number of reviewers grows with how hard the task is.

## Spin-offs

- [Side experiments](spin-offs/side-experiments.md): a knockout tournament against a varied team, and a Split or Steal final between the two finalists.
- [Accent and dialect understanding](spin-offs/accent-and-dialect-understanding.md): the same method applied to how well AI understands accented speech, such as Welsh English.

## Supporting material

- [Supporting material](supporting-material/): related research and citations. The explainer video source is in [ablation-lab/council-video](https://github.com/ablation-lab/council-video).

## Status

Planning stage. The pilot is done. The formal experiment, the council calculator, the write-up and the raw run logs will be added here as they're produced.
