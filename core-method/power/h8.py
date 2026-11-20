# H8 draft (20 Nov 2026): power for a within-run test of the appeal.
# The appeal sees only the judge's dismissals (and some severities) and can only flag them, so within a run
# catches and extras can only rise. Two parts:
#   A. the recovery rate R: of the judge's wrongful dismissals of seeds, the share the appeal flags WRONGLY DISMISSED.
#      One-sided exact binomial test of H0: R <= R0, at alpha 0.05 and 0.05/3 (Holm's first step). Ignores
#      clustering of dismissals by seed, so it is optimistic when one seed is dismissed in several runs.
#   B. the false-ones guard: extras per catch with the appeal, over extras per catch from the judge alone, must have
#      a one-sided upper confidence bound under 1.20. Simulated over judged runs, with a seed-cluster bootstrap.
# Run: python h8.py
import numpy as np
from scipy import stats

print("A. Recovery rate, exact one-sided binomial test of R <= 0.5")
print("alpha | wrongful dismissals D | power at true R = 0.7 / 0.8 / 0.9")
for alpha in (0.05, 0.05 / 3):
    for D in (5, 10, 15, 20, 30):
        k = next(k for k in range(D + 2) if stats.binom.sf(k - 1, D, 0.5) <= alpha)   # smallest k with P(X >= k | 0.5) <= alpha
        pw = [stats.binom.sf(k - 1, D, r) for r in (0.7, 0.8, 0.9)]
        print(f"{alpha:.4f} | {D:>2} | " + " / ".join(f"{p:.2f}" for p in pw) + f"   (reject if at least {k} of {D})")

print()
print("B. False-ones guard: power that the upper bound of (extras per catch, appeal / judge) stays under 1.20")
rng = np.random.default_rng(20261120)
SEEDS, RUNS_PER_SEED = 105, 12            # 4 judged role sets x 3 repeats
CATCH, RAISE, WRONG_DISMISS, Q = 0.5, 0.65, 0.02, 0.95
ALPHA, SIMS, BOOT = 0.05 / 3, 300, 400

def one_sim(mu_e, mu_f, p_f):
    n = SEEDS * RUNS_PER_SEED
    seed = np.repeat(np.arange(SEEDS), RUNS_PER_SEED)
    caught = rng.random(n) < CATCH                                     # kept by the judge
    raised_not_kept = (~caught) & (rng.random(n) < (RAISE - CATCH) / (1 - CATCH))
    wrongly = raised_not_kept & (rng.random(n) < WRONG_DISMISS / ((RAISE - CATCH) / (1 - CATCH)))
    recovered = wrongly & (rng.random(n) < Q)
    extras = rng.poisson(mu_e, n)
    fair = rng.poisson(mu_f, n)
    false_re = rng.binomial(fair, p_f)
    per = np.zeros((SEEDS, 4))
    np.add.at(per, seed, np.c_[caught, recovered, extras, false_re])
    def ratio(t):
        cj, rc, ej, fr = t[..., 0], t[..., 1], t[..., 2], t[..., 3]
        return ((ej + fr) / (cj + rc)) / (ej / cj)
    idx = rng.integers(0, SEEDS, (BOOT, SEEDS))
    boot = ratio(per[idx].sum(1))
    upper = np.quantile(boot, 1 - ALPHA)
    return upper < 1.20

print(f"alpha one-sided {ALPHA:.4f}; {SEEDS} seeds x {RUNS_PER_SEED} judged runs; catch {CATCH}, raised {RAISE}, wrongly dismissed {WRONG_DISMISS}")
print("judge's extras per run | fair dismissals per run | false reinstatement rate | power")
for mu_e in (0.5, 2.0):
    for mu_f in (0.5, 2.0):
        for p_f in (0.01, 0.05, 0.10):
            pw = np.mean([one_sim(mu_e, mu_f, p_f) for _ in range(SIMS)])
            print(f"{mu_e} | {mu_f} | {p_f} | {pw:.2f}", flush=True)
