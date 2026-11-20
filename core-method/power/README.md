# Power simulations

These are the scripts behind the power figures in [research-plan.md](../research-plan.md), written and run by Claude Code on 19 and 20 Nov 2026. They are pure simulation: they read no files and use no seed material, so they don't touch the seed wall.

## What each one does

| Script | What it gives | Where the plan uses it |
|---|---|---|
| `pairwise.py` | The smallest catch-rate difference between two councils detectable at 80% power and a two-sided alpha of 0.05, for 10, 15, 20 and 30 seeds per area (7 areas) and 1, 3 or 5 repeats, at 50% and 83% catch rates. It uses a normal approximation for a paired comparison on the same seeds, with a simulation check that adds seed-to-seed variation in difficulty. Optional arguments set the alpha and the sides, for example `python pairwise.py 0.0166667 1` for one-sided at 0.05/3. | G12's power table (section 7), and H11's one-sided detectable difference |
| `omnibus.py` | The power of H9's omnibus test at 105 seeds and 3 repeats: a mixed-effects logistic regression with five role sets as a fixed effect and seed as a random effect (SD 1 on the logit scale), fitted by maximum likelihood with 20-point Gauss–Hermite quadrature and tested by likelihood ratio on 4 degrees of freedom. | the omnibus power table under G12 |
| `h10.py` | The first H10 check: 15 pre-cutoff against 15 post-cutoff seeds, one council, 3 repeats, by the same kind of mixed-effects likelihood-ratio test on 1 degree of freedom. | H10's Power note (section 10) |
| `h10b.py` | The same test as `h10.py`, with the seeds a side and the repeats as arguments, for the four options in H10's size decision. | H10's size decision (section 10) |

## Results as run

These are in `results/`:
- `omnibus_400.txt`: `omnibus.py` with 400 simulations per row.
- `h10_first.txt`: `h10.py`.
- `h10b_15x3.txt`, `h10b_15x5.txt`, `h10b_25x3.txt` and `h10b_25x5.txt`: `h10b.py` for each option.
  - Each line gives the seeds a side, the repeats, the base catch rate, the difference and the power.
  - A difference of 0 gives the false-positive rate.

- `pairwise_2sided_0.05.txt`, `pairwise_1sided_0.05.txt` and `pairwise_1sided_0.0167.txt`: `pairwise.py` at two-sided 0.05 (the G12 table), one-sided 0.05 and one-sided 0.05/3. The "runs" column counts 5 role sets, so it doesn't apply to H11's two councils.

## Versions

The scripts ran on Python 3.11.9, with numpy 2.4.6 and scipy 1.17.1. `pairwise.py` needs only the Python standard library.

## Re-running

From this folder, in a fresh virtual environment:

```
python -m venv .venv
.venv/Scripts/python -m pip install numpy==2.4.6 scipy==1.17.1   (on Linux or macOS: .venv/bin/python)
python pairwise.py
python pairwise.py 0.05 1
python omnibus.py 400
python h10.py
python h10b.py 25 3
```

- **Arguments:** `omnibus.py` takes the number of simulations per row. `h10b.py` takes the seeds a side and the repeats.
- **Random seeds:** each script fixes its own, so a re-run gives the same figures on the same versions.
- **Timing:** each row takes from a few seconds to about a minute.
- **H10 at a smaller size:** if the post-cutoff supply comes in short, the shortfall rule calls for H10's power at the actual size. Run `h10b.py` with that size, for example `python h10b.py 20 3`.
