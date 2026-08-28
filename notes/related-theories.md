# Related theories surfaced after posting — 2026-08-28

Informal notes on frameworks pointed out in response to the r/PhilosophyofMind post. Not
citations in the paper unless promoted.

## Grounded Duality Theory (GDT) v3.0.0 — cultDynammica

Self-published, ~85k words, not peer-reviewed.
Source: `https://github.com/cultDynammica/Emotional-Architecture-and-Processing-Guides`

**Thesis.** Subjective awareness requires an internal division that terminates *outside* the
system at a "transductive surface" and *inside* at "uptake structures"; unification presupposes
prior partition. Four cognitive capacities — Observation, Structuring, Organisation,
Communication — with a coupling matrix over their six pairs. "Grounded" duality (inherited
transducers, real homeostatic grounding) vs. "facilitated" duality (designed transducers,
borrowed grounding; corporations as the example).

**Formal apparatus.**
- Profile $\langle Ob, S, Or, C\rangle$ + coupling matrix (6 undirected / 12 directed entries;
  "open modelling choice").
- **TCCI index**: $\text{TCCI} = \big(\tfrac14\sum_i x_i^{\rho}\big)^{1/\rho}$ — a generalized
  power (Hölder) mean of the four capacities. $\rho=1$: substitutable (arithmetic mean);
  $\rho\to0$: geometric mean; $\rho\to-\infty$: weakest-link (min). Explicitly "ordinal and
  comparative only"; no external anchor.
- Valence: "stakes" = states natively good/bad for the system, from homeostatic error against a
  defended boundary. "Establishment" (error generated at the transductive surface) vs. "uptake"
  (error narrowing which internal states are occupied — constraint, not signal).
- Predictive-advantage metric: reduction in $H(\text{state}_{t+1}\mid \text{self-model})$
  relative to $H(\text{state}_{t+1})$.
- Level individuation: "the largest loop with both [symmetric and asymmetric] channels closed";
  nested at interhemispheric / thalamocortical / cortico-subcortical / neuraxial scales.
- **Declines to propose a consciousness index** — "prioritizes architectural clarity over
  mathematical closure." The opposite editorial choice to Model $\Sigma$.

**Overlap with Model $\Sigma$.**
1. Both aggregate per-component values into one scalar. $\Sigma = \sum w_0(\ell)\Phi_\ell$ is a
   weighted arithmetic mean; TCCI is a power mean with a substitutability/complementarity knob.
2. Both hit the decomposition/individuation problem and both leave it partly open. GDT's
   closure criterion ("largest loop with both channels closed") is a *structural* individuation
   rule — more principled than $\Sigma$'s stipulation. See `layer-decomposition.md`.
3. GDT's "non-substitution requirement" (representing state and represented process must occupy
   non-substituted substrate) is kin to the descriptive/constitutive distinction, framed via
   substrate rather than via "error drives an update."
4. Both use conditional-entropy reduction as the self-model's payoff (cf. $R_\ell$, $e_\ell$).
5. Both lean on split-brain / corpus callosum and DID.

**Borrowed (adopted 2026-08-28).** The **power-mean-with-$\rho$** aggregation. $\Sigma$ is now
$\big(\sum_\ell w_0(\ell)\,\Phi_\ell^{\rho}\big)^{1/\rho}$ with $w_0$ a probability weight
($\sum w_0 = 1$) and $\rho\in\mathbb R$ a complementarity parameter: $\rho=1$ recovers the
previous weighted average (layers substitute), $\rho\to0$ the geometric mean, $\rho\to-\infty$
the weakest-weighted-layer minimum. This makes explicit a modeling choice the linear form hid,
gives $\Sigma$ the clean bound $\min_\ell\Phi_\ell\le\Sigma\le\max_\ell\Phi_\ell$, and removes
axiom A1 (non-negativity of $\Sigma$ now follows from $\Phi_\ell\ge0$). Side effect: the
demoted competing-layers direction can no longer produce $\Sigma<0$ via the weighting --- it
would have to suppress $\Phi_\ell$ directly, which is the rejected §7.1 route. Attribution to
GDT recorded here and in `layer-decomposition.md`; GDT itself is not cited in the paper
(self-published).

**Caveats.** Idiosyncratic terminology, no external validation, and — like Model $\Sigma$ —
mostly a vocabulary rather than a predictive theory. Its clinical predictions (anosognosia as
intact awareness + locally incorrigible self-model; DID as one loop with multiple narrative
syntheses) are stated but untested.
