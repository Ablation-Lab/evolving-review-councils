import numpy as np, sys, time
from scipy.optimize import minimize
from scipy.special import expit, gammaln
from scipy.stats import chi2
N, R, J, TAU = 105, 3, 5, 1.0
gh_x, gh_w = np.polynomial.hermite_e.hermegauss(20); gh_w = gh_w / gh_w.sum()
LC = gammaln(R+1) - gammaln(np.arange(R+1)+1) - gammaln(R-np.arange(R+1)+1)
def nll(theta, k, full):
    a = theta[0]; b = np.zeros(J)
    if full: b[1:] = theta[1:J]
    tau = np.exp(theta[-1])
    eta = a + b[None, :, None] + tau * gh_x[None, None, :]          # (1,J,Q)
    p = np.clip(expit(eta), 1e-12, 1-1e-12)
    ll = LC[k][:, :, None] + k[:, :, None]*np.log(p) + (R-k)[:, :, None]*np.log(1-p)   # (N,J,Q)
    per = ll.sum(1)                                                   # (N,Q)
    m = per.max(1, keepdims=True)
    return -(m[:, 0] + np.log((np.exp(per-m) * gh_w).sum(1))).sum()
def fit(k, full):
    x0 = np.zeros(J+1 if full else 2); x0[0] = np.log((k.mean()/R+1e-3)/(1-k.mean()/R+1e-3))
    r = minimize(nll, x0, args=(k, full), method='BFGS')
    return r.fun
def marg(a, b, rng_u):
    return expit(a + b + TAU*rng_u).mean()
def calib(p0, deltas):
    # baseline a for mean p0, and logit shifts giving marginal differences deltas
    u = np.random.default_rng(7).normal(0, 1, 200000)
    lo, hi = -10, 10
    for _ in range(80):
        a = (lo+hi)/2
        if marg(a, 0, u) < p0: lo = a
        else: hi = a
    shifts = []
    for d in deltas:
        lo, hi = -10, 10
        for _ in range(80):
            s = (lo+hi)/2
            if marg(a, s, u) - p0 < d: lo = s
            else: hi = s
        shifts.append((lo+hi)/2)
    return a, np.array(shifts)
def power(p0, deltas, sims, seed):
    a, b = calib(p0, deltas)
    rng = np.random.default_rng(seed); crit = chi2.ppf(0.95, J-1); hits = 0
    for _ in range(sims):
        u = rng.normal(0, TAU, N)
        p = expit(a + b[None, :] + u[:, None])
        k = rng.binomial(R, p)
        lr = 2*(fit(k, False) - fit(k, True))
        hits += lr > crit
    return hits/sims
scen = {
 'no difference (size check)': [0,0,0,0,0],
 'one set 5 points better': [0,0,0,0,0.05],
 'one set 10 points better': [0,0,0,0,0.10],
 'one set 15 points better': [0,0,0,0,0.15],
 'even spread, 0 to 10 points': [0,0.025,0.05,0.075,0.10],
}
sims = int(sys.argv[1]); out = []
for p0 in (0.5, 0.83):
    for name, d in scen.items():
        dd = [x if p0 + max(d) <= 0.99 else x for x in d]
        t = time.time(); pw = power(p0, dd, sims, 11)
        out.append((p0, name, pw)); print(f'{p0:.2f} | {name} | power {pw:.3f} | {time.time()-t:.0f}s', flush=True)
