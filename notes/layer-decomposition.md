# The layer decomposition — 2026-08-28

## The problem

$\Sigma$, $\Gamma$, $A$, $R_\ell$, $\chi_\ell$ are all defined relative to a partition of the
system into functional layers $\ell = 1..L$. The paper stipulated this partition ("homeostasis
$\to$ perception/motor $\to$ world-model $\to$ self-model"). **Nothing here is
decomposition-invariant**: $\Phi_\ell$ is the integrated information *of a block*, and blocks
are chosen; $e_\ell$ is a norm on *layer $\ell$'s state*, which changes when layers are merged
or split. So two studies that decompose differently produce $(\Sigma,\Gamma,A)$ values that are
not comparable, and $A$ — a correlation over $L$ points — can swing on a single reassignment. A
principled decomposition is therefore not optional; it is a precondition for the framework
meaning anything across systems.

## Criterion (a criterion, not yet a procedure)

Derive the partition from the system's own dynamics, in two steps.

**Step 1 — timescale bands.** Cluster units by characteristic timescale (autocorrelation time,
or the dominant frequency of the unit's activity). The cortex is already organized this way:
"temporal receptive windows" grow from early sensory areas to association cortex (Hasson et
al. 2008), and hierarchical predictive coding places slow contextual variables above fast
sensory ones (Kiebel, Daunizeau & Friston 2008). Fast band $\approx$ perception/motor
(10s–100s ms); intermediate $\approx$ world-model; slow $\approx$ homeostatic set-point
regulation and narrative self-model (seconds+). $L$ is the number of well-separated bands the
clustering returns — not a fixed 4.

**Step 2 — predict/error asymmetry.** Where the system is (or is modeled as) a hierarchical
predictive system, order the bands by the direction of prediction vs. prediction-error flow:
layer $\ell$ predicts layer $\ell-1$ and receives its errors. This resolves the ordering that
timescale clustering alone leaves ambiguous.

**Identifying the top (self-model) layer.** A layer counts as a self-model layer **iff its
prediction targets are other layers' internal states rather than external input** — i.e. iff
$e_\ell$ (the self-prediction error already in the formalism) is non-degenerate for it. If no
such layer exists, there is no self-model layer and $\Gamma$, $A$ collapse to the
world-modeling part. This ties the top of the hierarchy to something the formalism already
measures, not to a name.

## What remains observer-relative

- The clustering has free choices (distance metric, band-separation threshold). Report them.
- $\Sigma$ and $\Gamma$ tolerate a rough decomposition for **ordinal** claims ($\Sigma$ high
  vs. low). $A$ does not — it must be interpreted only relative to one fixed,
  independently-motivated decomposition, and never compared across differently-decomposed
  systems.
- For a system with no clean timescale separation and no predictive hierarchy, the framework
  simply does not apply. That is the correct behaviour: it should not claim to decompose an
  arbitrary dynamical system.

## Convergent criteria elsewhere

- **Nested Observer Windows** (Riddle & Schooler 2024): $\Phi$ at nested levels, levels
  individuated by the nesting of "observer windows" — structural, not stipulated.
- **Grounded Duality Theory** (cultDynammica, self-published; surfaced via the r/PhilosophyofMind
  thread): individuates a level as "the largest loop with both [a symmetric and an asymmetric]
  channel closed" — a closure criterion, structurally similar to IIT complex-finding applied
  recursively. (See `related-theories.md`.)
- **IIT complex-finding** itself, applied recursively (main complex, then strongest
  sub-complexes), would ground the decomposition in the same cause-effect structure $\Phi$ is
  computed over — at the cost of inheriting IIT's non-uniqueness (Hanson & Walker 2023).

## Status

A criterion, not a procedure with a worked example. A real test: take one open dataset, run the
timescale clustering, check the bands are separable, and check that $(\Sigma,\Gamma,A)$ on the
derived partition are stable under reasonable perturbations of the clustering parameters. Until
that exists, the paper should present this as the intended route and keep the honest caveat
about $A$.
