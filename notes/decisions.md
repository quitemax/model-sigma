# Decision log — Model Σ

A chronological record of the calls made, so they don't have to be reconstructed from memory on
every return to the project.

## State description: two-dimensional, then three-dimensional
Considered w(ℓ,t) coupled to g·e (option 1, Σ and Γ tautologically correlated) vs. w(ℓ,t)=w₀(ℓ)
static (option 2, Σ and Γ independent by construction). **Option 2 adopted** — a correlation
measured in a real system is then an empirical finding, not a definitional artifact. Added a
third quantity A(t) (spatial alignment) as a separate, orthogonal diagnostic dimension.

## Competition/exclusion mechanism: §7 vs §7.1
Two versions were considered:
- **§7 (canonical):** w = w₊ − w₋, continuous Jaccard index, w₋ = γ·overlap·Φ. Allows Σ<0
  ("net fragmentation"). Our own construction, inspired by IIT, not derived from it.
- **§7.1 (considered, rejected):** binary overlap gate + tanh relaxation of the Φ difference,
  grounded directly in IIT's canonical (binary) exclusion postulate. Provably forbids Σ<0.

**Decision (settled, 2026-08-28):** keep §7 as canonical. Reachable Σ<0 ("net fragmentation")
stays as an **intended feature of the model, not a bug** — the ability to express it was judged
more valuable than strict fidelity to IIT's binary postulate. §7.1 stays in the paper only as a
documented, rejected variant. This is a deliberate, named departure from IIT — not a
misunderstanding of the formalism; to be flagged outright in any future write-up. Closed topic,
no longer an open question to resolve before publication.

## The layer axis is discrete — the integral form was removed (2026-08-28)
Σ, Γ, A had been written with an integral variant ∫₀ᴸ … dℓ as a "continuum idealization". The
functional-layer axis ℓ is **not** a continuum (L is a handful of strata: homeostasis →
world-model → self-model), so the integral form introduced false generality and an artificial
L→0 artifact. All definitions are now finite sums ∑_{ℓ=1}^{L}. The former "L→0 pathology" is
replaced by a "Discreteness" remark. Affects `model_sigma.md` §2/§3/§5/§5.1/§6/§7 and both
`.tex` files.

## Self- vs. world-modelling (§4.1)
Two independent conditions for genuine self-modelling: (a) prediction target internal (state
h_ℓ) vs. external (token/behaviour), (b) update timing: online at deployment vs. training only.
Only the intersection of both conditions satisfies the full definition of e_ℓ, g_ℓ from §4.
Titans lands in the cell (external target × online) — constitutive, but world-modelling, not
self-modelling.

## Readout channel R_ℓ (§17)
Added after a discussion of different types of loss of consciousness (fainting, seizure, REM
sleep, locked-in syndrome). (Σ,Γ,A) describes the internal state but says nothing about
observability from the outside — hence R_ℓ(t) and the inequality Σ_obs(t) ≤ κ·R_L(t). Direct
inspiration: the Perturbational Complexity Index (Casali et al. 2013), designed precisely to
separate those two clinical questions.

## Context-sensitivity of the gate g_ℓ (§18)
Added after coming across a source linking Friston (2010) to Intense World Theory and "context
blindness" in autism. g_ℓ(t) = h(e_ℓ(t), C(t)), χ_ℓ(t) = |∂g_ℓ/∂C| ≥ 0 as a new parameter
measuring how strongly context modulates the error's weight. Context blindness = χ_ℓ≈0.

## Literature review — second pass (2026-08-28)
The §12 review was search-only. A claim-by-claim precedent map is now in
[`literature.md`](literature.md). Key outcomes that the paper still needs to absorb:
- The *multidimensional* framing is **Bayne, Hohwy & Owen (2016)** — not new; (Σ,Γ,A) is an
  IIT-grounded instance of it.
- The IIT+FEP+functionalism synthesis ambition is largely **Safron's IWMT (2020)** — needs an
  explicit "vs IWMT" contrast.
- **Negative integrated information already exists** (ΦID / whole-minus-parts, as redundancy);
  §7's Σ<0 is a different sense (an active anti-weight) and must be distinguished.
- The exclusion postulate is independently under formal attack (**Hanson & Walker 2023**) —
  this *supports* replacing it.
- Surviving novelties: the w₊−w₋ construction + exact threshold, Γ's specific form, χ_ℓ, the
  triple as a package.
Still not exhaustive: no PhilPapers/PhilSci-Archive sweep; ΦID literature read via abstracts only.

## Overall status
An internally consistent conceptual synthesis, not peer-reviewed. Open: an exhaustive literature
review (second pass done, see above), an empirical instance beyond the toy example, and folding
the second-pass findings into §12 / §7. Settled: §7 vs §7.1 (§7 kept, see above), source
verification of citations (done 2026-08-28, see [`citations.md`](citations.md)), removal of the
integral form (see above).
