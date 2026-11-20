import math, random
from statistics import NormalDist
Z = NormalDist().inv_cdf
za, zb = Z(1 - 0.05/2), Z(0.80)
AREAS, SETS = 7, 5
def mde(p0, n_seeds, r):
    # smallest d with p1 = p0 - d (or p0 + d at p0 <= .5) detectable, paired-by-seed normal approx
    lo, hi = 0.0, min(p0, 1 - p0) if p0 != 0.5 else 0.5
    hi = p0 if p0 > 0.5 else 1 - p0
    for _ in range(60):
        d = (lo + hi) / 2
        p1 = p0 - d if p0 > 0.5 else p0 + d
        se = math.sqrt((p0*(1-p0) + p1*(1-p1)) / (n_seeds * r))
        if d / se >= za + zb: hi = d
        else: lo = d
    return hi
def sim_power(p0, d, n_seeds, r, sims=4000, sd=1.0, seed=1):
    # seed-level heterogeneity: logit p_i ~ N(logit p0, sd); set B shifted so mean diff ~ d
    rnd = random.Random(seed); hits = 0
    lg = lambda p: math.log(p/(1-p)); ex = lambda x: 1/(1+math.exp(-x))
    # find shift on logit scale giving mean diff d
    def mean_p(shift, n=4000):
        rr = random.Random(7); return sum(ex(lg(p0)+rr.gauss(0,sd)+shift) for _ in range(n))/n
    base = mean_p(0)
    lo, hi = -6, 0
    for _ in range(40):
        mid = (lo+hi)/2
        if base - mean_p(mid) > d: lo = mid
        else: hi = mid
    shift = (lo+hi)/2
    for _ in range(sims):
        diffs = []
        for i in range(n_seeds):
            u = lg(p0) + rnd.gauss(0, sd)
            a = sum(rnd.random() < ex(u) for _ in range(r)) / r
            b = sum(rnd.random() < ex(u+shift) for _ in range(r)) / r
            diffs.append(a - b)
        m = sum(diffs)/n_seeds
        v = sum((x-m)**2 for x in diffs)/(n_seeds-1) if n_seeds > 1 else 0
        if v == 0: continue
        if abs(m)/math.sqrt(v/n_seeds) > za: hits += 1
    return hits/sims
rows = []
for s in (10, 15, 20, 30):
    for r in (1, 3, 5):
        N = s*AREAS
        rows.append((s, N, r, mde(0.5, N, r), mde(0.83, N, r), SETS*N*r))
print('per area | seeds | repeats | MDE p0=0.50 | MDE p0=0.83 | runs (5 sets)')
for s, N, r, a, b, runs in rows:
    print(f'{s:>3} | {N:>4} | {r} | {a*100:5.1f} | {b*100:5.1f} | {runs}')
# sanity check by simulation for two cells
for (s, r, p0) in [(10, 1, 0.5), (20, 3, 0.5), (10, 3, 0.83)]:
    N = s*AREAS; d = mde(p0, N, r)
    print('sim check', s, r, p0, 'd=%.3f' % d, 'power with heterogeneity sd=1: %.2f' % sim_power(p0, d, N, r))
