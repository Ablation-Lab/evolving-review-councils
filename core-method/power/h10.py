# H10 power: 15 pre-cutoff vs 15 post-cutoff seeds, one council, R repeats.
# Seed logit intercept ~ N(mu_g, 1). Group shift calibrated so the mean catch-rate difference equals d.
# Test: mixed-effects logistic LR test (group fixed, seed random), 20-point Gauss-Hermite, chi2 1 df.
import numpy as np
from scipy import optimize, stats, special
rng = np.random.default_rng(20261120)
gh_x, gh_w = np.polynomial.hermite.hermgauss(20)
nodes = np.sqrt(2) * gh_x; wts = gh_w / np.sqrt(np.pi)

def meanp(mu, sd=1.0):
    return np.sum(wts * special.expit(mu + sd * nodes))

def mu_for(p):
    return optimize.brentq(lambda m: meanp(m) - p, -10, 10)

def nll(params, y, n, g):
    b0, b1, lsd = params; sd = np.exp(lsd)
    eta = b0 + b1 * g[:, None] + sd * nodes[None, :]
    p = special.expit(eta)
    ll = y[:, None] * np.log(p + 1e-300) + (n - y)[:, None] * np.log(1 - p + 1e-300)
    m = ll.max(axis=1, keepdims=True)
    return -np.sum(m[:, 0] + np.log(np.sum(wts[None, :] * np.exp(ll - m), axis=1)))

def fit(y, n, g, null):
    if null:
        f = lambda q: nll([q[0], 0.0, q[1]], y, n, g); x0 = [0.0, 0.0]
    else:
        f = lambda q: nll(q, y, n, g); x0 = [0.0, 0.0, 0.0]
    return optimize.minimize(f, x0, method='Nelder-Mead', options={'xatol': 1e-4, 'fatol': 1e-5, 'maxiter': 4000}).fun

def power(base, d, k=15, R=3, sims=400):
    m0 = mu_for(base); m1 = mu_for(base + d) if d else m0
    g = np.r_[np.zeros(k), np.ones(k)]; n = np.full(2 * k, R)
    hits = 0
    for _ in range(sims):
        u = rng.normal(0, 1, 2 * k)
        p = special.expit(np.where(g == 0, m0, m1) + u)
        y = rng.binomial(R, p)
        lr = 2 * (fit(y, n, g, True) - fit(y, n, g, False))
        hits += lr > stats.chi2.ppf(0.95, 1)
    return hits / sims

for base in (0.5, 0.83):
    for d in (0.0, 0.1, 0.2, 0.3):
        if base + d >= 0.99 or base - 0 <= 0: continue
        # for the 83% base, test a drop (memorised fixes inflate pre-cutoff catches)
        dd = d if base == 0.5 else -d
        print(base, dd, power(base, dd))
