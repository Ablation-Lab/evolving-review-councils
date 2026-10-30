# Evolving Councils – Council Size by Task Complexity

Part of the core method of the Evolving Council & Optimum Size Experiment. It asks whether the best number of reviewers grows with how hard the task is, and by how much.

## The question

Is there a council size where adding another reviewer stops paying for itself, and does that point move as tasks get more complex?

## Working guesses (to be tested)

- **Basic app:** around 6 reviewers.
- **Scientific or technical work:** around 20.
- **Frontier research:** far more.

These are starting guesses only. The point of the experiment is to replace them with measured numbers.

## Unit of review effort

The aim is a rough "unit of review effort" per complexity tier: how many reviewers, generations and tokens a task of that tier needs before extra review stops improving the result. This is what the later calculator tool will be built from.

## How it's measured

- Run the same council setup at different sizes on tasks of each tier.
- Score each run on the hard benchmark and held-out tests, plus an efficiency score (tokens, agents, time).
- The optimum is where the quality gain from one more reviewer drops below its cost.
- Weight findings by severity, since a security hole matters far more than a typo. Counts alone can mislead.

## What can realistically be measured

The largest tiers need far more usage than a personal plan allows. Only the lower tiers can be measured directly. The higher tiers will be estimated from the trend, clearly labelled as estimates, unless research credits become available.

## Early signal from the WinScope pilot

The pilot didn't vary council size, so it can't answer this question. It did suggest that review effort should scale with risk: code that deletes files, runs as admin or handles personal data justified extra rounds, while read-only code needed less.

## Prior work (verify before citing)

- Google Research, "Towards a science of scaling agent systems": more agents hits a ceiling and can degrade.
- "Scaling Behavior of Single LLM-Driven Multi-Agent Systems": task type changes the best agent count.
- "Understanding Agent Scaling via Diversity": identical agents give diminishing returns, while varied agents keep paying.

## Status

Planned. Measured during the small test runs and the large ceiling run of the main experiment.
