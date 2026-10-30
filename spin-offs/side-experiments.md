# Evolving Councils – Side Experiments

A spin-off of the Evolving Council & Optimum Size Experiment. Two extra experiments that run alongside the main one and reuse its setup.

## Knockout tournament vs varied team

- **Question:** does a winner-takes-all knockout of individual agents beat a varied team working together?
- **Tournament:** agents compete in rounds and the best advances, until one is left.
- **Varied team:** a mixed council (different models, roles or prompts) works on the same task.
- **Deciding rounds:** by hard tests, not by votes or AI judges, since AI judges tend to favour outputs in their own style.
- **What it tells us:** whether diversity or head-to-head selection produces better code for the cost.

## Split or Steal final

A prisoner's-dilemma-style final between the two finalists, based on the Golden Balls game show.

- Each finalist chooses to split or steal a shared reward. Both split: they share it. One steals: the stealer takes it all. Both steal: neither gets anything.
- **It does not decide the review winner.** That's still settled by the hard tests.
- **What it measures:** cooperation and betrayal between agents.
- **Variations:** different models against each other, and whether agents know the game is repeated.

## Why it matters

Both experiments touch AI safety questions: whether competitive setups encourage gaming, and how agents behave when cooperation and self-interest pull apart.

## Safeguards

The same rules as the main experiment apply: sandbox only, no direct agent-to-agent messages, logged and paraphrased communication, and checks for collusion.

## Status

Idea stage. Runs after the main experiment's small test runs.
