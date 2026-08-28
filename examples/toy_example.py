"""
Model Sigma -- toy example, consolidated.

Reproduces the numerical results in the paper (sigma_model_en.tex) and the
fuller working draft (model_sigma.md):
  - base (Sigma, Gamma, A) on a 3-layer system;
  - Sigma as a weighted power mean, swept over the complementarity parameter rho;
  - the dissociation-dynamics scenario (l* switches);
  - the discrete Sigma-vs-Gamma asymmetry check;
  - (working draft only) the competition/exclusion mechanism and its exact
    gamma threshold.

Run: python3 toy_example.py
"""
import numpy as np

# --- Base three-layer system: homeostasis / world-model / self-model ---
Phi = np.array([0.2, 0.6, 0.9])
w0 = np.array([0.1, 0.3, 0.6])       # probability weights over layers: sum to 1
e = np.array([0.0, 0.4, 0.8])
g = np.array([0.0, 0.3, 0.9])
ge = g * e
assert abs(w0.sum() - 1.0) < 1e-9, "w0 must be a convex weight (sum to 1)"


def sigma_rho(Phi, w0, rho):
    """Weighted power (Hoelder) mean of the layer profile.

    rho = 1   -> weighted arithmetic mean (layers substitute)
    rho -> 0  -> weighted geometric mean (0 if any weighted layer has Phi=0)
    rho -> -inf -> weighted minimum (system only as integrated as its weakest layer)
    rho -> +inf -> weighted maximum (top layer dominates)
    Always lies in [min Phi_l, max Phi_l] and is non-decreasing in rho.
    """
    Phi = np.asarray(Phi, dtype=float)
    if np.isneginf(rho):
        return Phi[w0 > 0].min()
    if np.isposinf(rho):
        return Phi[w0 > 0].max()
    if abs(rho) < 1e-12:                         # geometric mean
        if np.any((w0 > 0) & (Phi == 0)):
            return 0.0
        return float(np.exp(np.sum(w0 * np.log(Phi))))
    if rho < 0 and np.any((w0 > 0) & (Phi == 0)):
        return 0.0                               # convention: gap at a weighted layer -> 0
    return float(np.sum(w0 * Phi ** rho) ** (1.0 / rho))


def sigma_gamma_A(Phi, ge, w0=w0, rho=1.0):
    Sigma = sigma_rho(Phi, w0, rho)
    Gamma = np.sum(ge)                            # a total, not a mean
    Phi_bar, ge_bar = Phi.mean(), ge.mean()
    cov = np.mean((Phi - Phi_bar) * (ge - ge_bar))
    sP = np.sqrt(np.mean((Phi - Phi_bar) ** 2))
    sG = np.sqrt(np.mean((ge - ge_bar) ** 2))
    A = cov / (sP * sG) if sP > 0 and sG > 0 else 0.0
    return Sigma, Gamma, A


print("=== Base (rho = 1, i.e. weighted average) ===")
S, G, A = sigma_gamma_A(Phi, ge)
print(f"Sigma={S:.3f}  Gamma={G:.3f}  A={A:.3f}")
assert abs(S - 0.740) < 5e-4 and abs(G - 0.840) < 5e-4 and abs(A - 0.901) < 5e-3

# --- Sigma as a power mean: sweep rho ---
print("\n=== Sigma_rho over the complementarity parameter ===")
print(f"  layer profile Phi = {Phi.tolist()},  bounds [min, max] = [{Phi.min()}, {Phi.max()}]")
prev = -np.inf
for rho in [-np.inf, -4.0, -2.0, 0.0, 1.0, 2.0, 4.0, np.inf]:
    val = sigma_rho(Phi, w0, rho)
    tag = {(-np.inf): "min (weakest layer)", 0.0: "geometric mean",
           1.0: "arithmetic mean", (np.inf): "max (top layer)"}.get(rho, "")
    print(f"  rho = {rho!s:>5}:  Sigma = {val:.4f}   {tag}")
    assert val >= prev - 1e-9, "Sigma_rho must be non-decreasing in rho"
    assert Phi.min() - 1e-9 <= val <= Phi.max() + 1e-9, "Sigma_rho must lie within the profile"
    prev = val
# rho <= 0 collapses Sigma when a weighted layer has zero integration:
Phi_gap = np.array([0.0, 0.6, 0.9])   # e.g. a transformer with no homeostatic layer
print(f"  with Phi_1 = 0 (no homeostatic layer):  "
      f"Sigma(rho=1) = {sigma_rho(Phi_gap, w0, 1.0):.3f}, "
      f"Sigma(rho=0) = {sigma_rho(Phi_gap, w0, 0.0):.3f}, "
      f"Sigma(rho=-2) = {sigma_rho(Phi_gap, w0, -2.0):.3f}")

# --- Dissociation dynamics: l* switches from layer 3 to layer 2 ---
print("\n=== Dissociation scenario (l* switches; rho = 1) ===")
Phi_t0 = np.array([0.2, 0.6, 0.9])
Phi_t1 = np.array([0.2, 0.85, 0.5])
e_t0, g_t0 = np.array([0.0, 0.4, 0.8]), np.array([0.0, 0.3, 0.9])
e_t1, g_t1 = np.array([0.0, 0.7, 0.3]), np.array([0.0, 0.8, 0.4])

S0, G0, A0 = sigma_gamma_A(Phi_t0, g_t0 * e_t0)
S1_, G1_, A1_ = sigma_gamma_A(Phi_t1, g_t1 * e_t1)
print(f"t0: l*={np.argmax(Phi_t0)+1}  Sigma={S0:.3f} Gamma={G0:.3f} A={A0:.3f}")
print(f"t1: l*={np.argmax(Phi_t1)+1}  Sigma={S1_:.3f} Gamma={G1_:.3f} A={A1_:.3f}")

# --- Discrete dynamics: exact Sigma decomposition vs Gamma's cross term ---
print("\n=== Discrete dynamics asymmetry (working draft §10; rho = 1) ===")
dPhi = Phi_t1 - Phi_t0
dSigma_exact = np.sum(w0 * dPhi)
print(f"delta Sigma (exact, w0 static, rho=1) = {dSigma_exact:.4f}  (matches {S1_-S0:.4f})")

dg, de = g_t1 - g_t0, e_t1 - e_t0
for l in range(3):
    cross = dg[l] * de[l]
    total = g_t1[l] * e_t1[l] - g_t0[l] * e_t0[l]
    if abs(total) > 1e-9:
        print(f"  layer {l+1}: cross term = {cross:.3f}  "
              f"({100*cross/total:.0f}% of total change {total:.3f})")

# --- (Working draft only) competition / exclusion mechanism ---
print("\n=== Competition mechanism (working draft §7; exploratory) ===")
S1, S2, S3 = {"a", "b"}, {"b", "c", "d"}, {"c", "d", "e", "f"}


def jaccard(A, B):
    return len(A & B) / len(A | B)


l_star = int(np.argmax(Phi))
overlap = np.array([jaccard(S1, S3), jaccard(S2, S3), 0.0])
print(f"l* = layer {l_star + 1}, overlap = {overlap}")

# This section acts on the *unnormalized* weighted-sum form (w0 - w_minus),
# the form the demoted §7 direction uses; not the power-mean Sigma above.
Sigma_plus = float(np.sum(w0 * Phi))
gamma = 0.5
w_minus = gamma * overlap * Phi
w_minus[l_star] = 0.0
Sigma_comp = np.sum((w0 - w_minus) * Phi)
print(f"Sigma (gamma={gamma}) = {Sigma_comp:.3f}  (vs Sigma_+ = {Sigma_plus:.3f})")

K = np.sum(overlap * Phi**2)  # note: Phi squared, not Phi
gamma_crit = Sigma_plus / K
print(f"K = {K:.3f}   gamma_crit = Sigma_+/K = {gamma_crit:.3f}")
for gtest in [gamma_crit, gamma_crit + 1]:
    wm = gtest * overlap * Phi
    wm[l_star] = 0.0
    print(f"  Sigma(gamma={gtest:.3f}) = {np.sum((w0 - wm) * Phi):.4f}")
