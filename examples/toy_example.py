"""
Model Σ — toy example, consolidated.
Reproduces every numerical result quoted in the paper (§9-10): base (Σ,Γ,A),
the competition/exclusion mechanism with exact gamma threshold, the
dissociation dynamics scenario, and the discrete Σ-vs-Γ asymmetry check.

Run: python3 toy_example.py
"""
import numpy as np

# --- Base three-layer system: homeostasis / world-model / self-model ---
Phi = np.array([0.2, 0.6, 0.9])
w0 = np.array([0.1, 0.3, 0.6])
e = np.array([0.0, 0.4, 0.8])
g = np.array([0.0, 0.3, 0.9])
ge = g * e


def sigma_gamma_A(Phi, ge, w0=w0):
    Sigma = np.sum(w0 * Phi)
    Gamma = np.sum(ge)
    Phi_bar, ge_bar = Phi.mean(), ge.mean()
    cov = np.mean((Phi - Phi_bar) * (ge - ge_bar))
    sP = np.sqrt(np.mean((Phi - Phi_bar) ** 2))
    sG = np.sqrt(np.mean((ge - ge_bar) ** 2))
    A = cov / (sP * sG) if sP > 0 and sG > 0 else 0.0
    return Sigma, Gamma, A


print("=== Base (no competition) ===")
S, G, A = sigma_gamma_A(Phi, ge)
print(f"Sigma={S:.3f}  Gamma={G:.3f}  A={A:.3f}")

# --- Competition / exclusion mechanism (canonical §7) ---
print("\n=== Competition mechanism ===")
S1, S2, S3 = {"a", "b"}, {"b", "c", "d"}, {"c", "d", "e", "f"}


def jaccard(A, B):
    return len(A & B) / len(A | B)


l_star = int(np.argmax(Phi))
overlap = np.array([jaccard(S1, S3), jaccard(S2, S3), 0.0])
print(f"l* = layer {l_star + 1}, overlap = {overlap}")

gamma = 0.5
w_minus = gamma * overlap * Phi
w_minus[l_star] = 0.0
w_eff = w0 - w_minus
Sigma_comp = np.sum(w_eff * Phi)
print(f"Sigma (gamma={gamma}) = {Sigma_comp:.3f}  (vs Sigma_+ = {S:.3f})")

K = np.sum(overlap * Phi**2)  # note: Phi squared, not Phi
gamma_crit = S / K
print(f"K = {K:.3f}   gamma_crit = Sigma_+/K = {gamma_crit:.3f}")
for gtest in [gamma_crit, gamma_crit + 1]:
    wm = gtest * overlap * Phi
    wm[l_star] = 0.0
    print(f"  Sigma(gamma={gtest:.3f}) = {np.sum((w0 - wm) * Phi):.4f}")

# --- Dissociation dynamics: l* switches from layer 3 to layer 2 ---
print("\n=== Dissociation scenario (l* switches) ===")
Phi_t0 = np.array([0.2, 0.6, 0.9])
Phi_t1 = np.array([0.2, 0.85, 0.5])
e_t0, g_t0 = np.array([0.0, 0.4, 0.8]), np.array([0.0, 0.3, 0.9])
e_t1, g_t1 = np.array([0.0, 0.7, 0.3]), np.array([0.0, 0.8, 0.4])

S0, G0, A0 = sigma_gamma_A(Phi_t0, g_t0 * e_t0)
S1_, G1_, A1_ = sigma_gamma_A(Phi_t1, g_t1 * e_t1)
print(f"t0: l*={np.argmax(Phi_t0)+1}  Sigma={S0:.3f} Gamma={G0:.3f} A={A0:.3f}")
print(f"t1: l*={np.argmax(Phi_t1)+1}  Sigma={S1_:.3f} Gamma={G1_:.3f} A={A1_:.3f}")

# --- Discrete dynamics: exact Sigma decomposition vs Gamma's cross term ---
print("\n=== Discrete dynamics asymmetry (§10) ===")
dPhi = Phi_t1 - Phi_t0
dSigma_exact = np.sum(w0 * dPhi)
print(f"delta Sigma (exact, w0 static) = {dSigma_exact:.4f}  (matches {S1_-S0:.4f})")

dg, de = g_t1 - g_t0, e_t1 - e_t0
for l in range(3):
    cross = dg[l] * de[l]
    total = g_t1[l] * e_t1[l] - g_t0[l] * e_t0[l]
    if abs(total) > 1e-9:
        print(f"  layer {l+1}: cross term = {cross:.3f}  ({100*cross/total:.0f}% of total change {total:.3f})")
