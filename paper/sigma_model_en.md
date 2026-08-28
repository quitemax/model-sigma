# Model Σ — a hierarchical, functionally-weighted extension of IIT (Φ)

> English translation of [`model_sigma.md`](model_sigma.md) (the Polish source of truth).
> If the two ever diverge, the Polish file wins. A condensed, contiguously-renumbered
> version for print is [`sigma_model_en.tex`](sigma_model_en.tex).

Working document collecting the formalism developed so far: from motivation through the full
static and dynamic formalism, proven boundary properties, the competition/exclusion mechanism
(with an explicitly named, deliberate departure from canonical IIT), a toy example, a
preliminary literature review, and application to transformer architectures. Status: an
internally consistent conceptual synthesis, not peer-reviewed. Before any publication attempt
the following are needed: a systematic (not merely search-driven) literature review, and an
empirical instantiation beyond the toy example. Settled: §7 is kept (it allows Σ<0 as an
intended feature), §7.1 remains only as a documented, rejected alternative; source verification
of the citations is done (`notes/citations.md`); the integral form was replaced with finite sums.

---

## 0. Theoretical frameworks we draw on

Model Σ is not the development of a single theory but a synthesis of several independent
conceptual frameworks. Before turning to the formalism it is worth being clear about where each
component comes from and what role it plays.

**Integrated Information Theory (IIT), Giulio Tononi.** The main formal skeleton — Φ as a
measure of integrated information, the axioms/postulates (existence, information, integration,
exclusion, composition), and, crucially for us, the **exclusion postulate** (among competing,
overlapping substrates only the one with maximal φ exists — the "principle of maximal
existence"). Formal criticisms (Aaronson: Φ can be high for trivial systems such as an
error-correcting code; Cerullo: no justification for the exclusion postulate itself) motivate
some of our extensions.

**Computational irreducibility, Stephen Wolfram.** Some computations cannot be "shortcut" — the
only way to know the result is to actually run every step. Here: it gates the temporal term
R_ℓ(i) — some inter-layer couplings can be predicted analytically, others must actually be
"computed through" step by step. Conceptually akin to IIT's structural irreducibility, but a
formally distinct notion.

**"Living matter as functional matter", Blaise Agüera y Arcas.** The claim that a system's
status is decided not only by its cause–effect structure (as in pure IIT) but by *what the
system computes* — function, not just integration. This is the direct inspiration for
introducing the functional weight w(ℓ) — the place in the formalism where a layer's "meaning"
for subjecthood enters explicitly, rather than just its raw integration.

**Predictive processing / test-time-training architectures.** The frameworks from which we
borrow the definition of the *self-prediction error* e_ℓ(t) and the constitutivity criterion
(online parameter updates driven by that error) — distinguishing passive modelling from an
active, self-correcting loop.

**Gazzaniga's interpreter (split-brain studies).** The observation that the left hemisphere
generates fluent, coherent explanations of actions whose causes it has no cognitive access to
(because they lie in the right hemisphere) — pure confabulation, but externally
indistinguishable from genuine insight. It motivates the descriptive/constitutive distinction
(§2.7): fluent self-narration is *not* evidence of a real feedback loop.

**Higher-Order Theories (Rosenthal).** A contrastive reference point, not a source of
formalism — HOT holds that a mental state is conscious when it is represented by a higher-order
state. Our descriptive/constitutive distinction is close to the question HOT raises but answers
it differently (via a *functional* criterion — does the error drive an update — rather than the
mere *existence* of a higher-order representation).

**The cosmological-constant analogy** (§7) — purely metaphorical, not a source theory: used
only to signal that the weight w(ℓ) need not be non-negative by definition, just as Λ in
Einstein's equations is not restricted a priori to one sign.

## 1. Motivation and starting point

Standard Φ (Tononi, IIT) for a system in state *s* and a partition *P*:

$$\varphi_P(s) = D\big(p(s'\mid s)\,\|\,p(s'\mid s)\big|_P\big), \qquad \Phi(s) = \min_{P\in\mathcal P}\varphi_P(s)$$

where *D* is a distance measure (e.g. earth mover's distance) between the actual distribution
and the distribution after cutting the system according to partition *P*. Criticism of the
starting point: Φ is a single number — "no if-statement", no distinction of the *kind* or the
*location* of integration. Close to Aaronson's formal criticism; related to the question of
Wolfram's computational irreducibility (kindred but distinct notions).

Inspiration for the extension: Agüera y Arcas's claim that "what a system computes matters"
(function, not just structure), plus the observation that different levels of a processing
hierarchy (cerebellum: much computation, little integration vs. self-modelling: less
computation, integration of a qualitatively different kind) call for a functional weight, not
just a structural one.

## 2. Hierarchical profile and the first version of Σ

We divide a system *S* into functional layers ℓ = 1,...,L (homeostasis → perception/motor →
world-model → self-model). The layer index is inherently discrete: L is a small, finite number
of functional strata, not a continuum — there is no L→∞ limit and none is needed. Instead of a
single number — a profile:

$$\Phi(s) = \big(\Phi_1(s),\dots,\Phi_L(s)\big)$$

collapsed by the functional weight w(ℓ) into a finite sum:

$$\Sigma(t) = \sum_{\ell=1}^{L} w(\ell,t)\,\Phi(s,\ell,t)$$

### 2.1 The inter-layer term Φ_{ℓ,ℓ-1}

Structural (not temporal) — integration *between* adjacent layers ℓ and ℓ-1 at a given moment,
computed analogously to base φ (via the same distance measure D). **Non-negative by
definition** (a distance), with no extra assumptions — it measures the degree of cause–effect
coupling and has no natural sign.

### 2.2 §2.7 — descriptive vs. constitutive self-modelling

A distinction crucial for interpretation: fluent self-narration (the Gazzaniga-interpreter
analogy) is **not** evidence of a real feedback loop. Constitutivity criterion: online
parameter updates driven by the self-prediction error (as in test-time-training
architectures).

## 3. Temporal dynamics

A notational distinction the first version lacked: the index (ℓ,ℓ-1) is a *layer*, not
*time*. Temporal dynamics is a separate object, derived from the full derivative of Σ:

$$\frac{d\Sigma}{dt} = \sum_{\ell=1}^{L} \left[\frac{\partial w(\ell,t)}{\partial t}\,\Phi(s,\ell,t) + w(\ell,t)\,\frac{\partial\Phi(s,\ell,t)}{\partial t}\right]$$

It separates two qualitatively different sources of change: ∂Φ/∂t (whether integration at a
layer is rising/falling — can be ±, e.g. going under / emerging from anaesthesia) and ∂w/∂t
(whether the layer's relevance for self-modelling is rising/falling).

## 4. w(ℓ,t) and the self-prediction error

Per the constitutivity criterion of §2.7:

- **Self-prediction error:** $e_\ell(t) = \|\hat s_\ell(t+\Delta t\mid t) - s_\ell(t+\Delta t)\|^2 \geq 0$ (for layers with no self-prediction mechanism: taken as 0)
- **Constitutivity gate:** $g_\ell(t) = \left|\dfrac{\partial\theta_\ell(t)}{\partial e_\ell(t)}\right| \in [0,1]$, normalized — g=0: the error is computed but nothing is done with it (descriptive); g=1: full constitutive coupling

### 4.1 Resolving self- vs. world-modelling (two independent conditions)

Genuine self-modelling requires **two independent conditions**, not one: (a) the prediction
target must be an **internal representational state** (h_ℓ — activations), not externally
observable behaviour/a token — even if that token is authored by the system itself; (b) the
update must occur **online, at deployment**, not merely as a frozen effect of training (this is
already §2.7, descriptive vs. constitutive). Crossing the two conditions gives a 2×2 (worked
out in §14 on architectural examples) — only the cell (target = internal) × (update = online)
satisfies the full definition of e_ℓ(t), g_ℓ(t) from this section.

## 5. Decision: a two-dimensional state description (Σ, Γ), then three-dimensional (Σ, Γ, A)

Two options for w(ℓ,t) were considered:

- **Option 1** — w(ℓ,t) = w₀(ℓ) + β·g_ℓ(t)e_ℓ(t): Σ and Γ share a term, correlation *tautological* (built into the definition)
- **Option 2 (adopted as canonical)** — w(ℓ,t) = w₀(ℓ), static: Σ and Γ are formally independent (built from disjoint variables), so a measured correlation between them in a real system is an empirical finding, not a definitional artifact

$$\Sigma(t) = \sum_{\ell=1}^{L} w_0(\ell)\,\Phi(s,\ell,t), \qquad \Gamma(t) = \sum_{\ell=1}^{L} g_\ell(t)\,e_\ell(t)$$

### 5.1 The third quantity — spatial alignment A(t)

$$A(t) = \frac{\mathrm{Cov}_\ell(t)}{\sigma_\Phi(t)\,\sigma_{ge}(t)} \in[-1,1], \qquad \mathrm{Cov}_\ell(t) = \frac{1}{L}\sum_{\ell=1}^{L}[\Phi(s,\ell,t)-\bar\Phi(t)][g_\ell(t)e_\ell(t)-\overline{ge}(t)]$$

Boundary convention: when σ_Φ=0 or σ_ge=0 (a uniform profile), A(t):=0.

**Interpretation of the triple (Σ, Γ, A):** Σ — how much integrated information, weighted by
architecture; Γ — how much real self-correction is occurring in the system *at all*; A —
whether that self-correction occurs *where* integration actually is. The case A≈-1 despite
high Σ and Γ = the signature of the "Gazzaniga interpreter": active, fluent self-narration
living in a shallow layer, cut off from the system's integrative core.

## 6. Proven boundary properties

1. **Σ(t) ≥ 0** — conditional: requires axiom **A1: w₀(ℓ) ≥ 0 ∀ℓ** (does not follow
   automatically from anything else; semantically: a negative base weight would have no good
   interpretation without an additional mechanism — see §7)
2. **Γ(t) ≥ 0** — unconditional: g_ℓ∈[0,1], e_ℓ≥0 (squared norm), a sum of products of
   non-negative terms
3. **A(t) ∈ [-1,1]** — proof via the Cauchy–Schwarz inequality on the profiles (finite
   vectors) f=Φ-Φ̄, h=ge-ge̅. Equality condition: A=1 ⟺ g_ℓe_ℓ is an increasing affine function
   of Φ(s,ℓ,t) over ℓ; A=-1 for a decreasing one
4. **Monotonicity:** ∂Γ/∂g_ℓ = e_ℓ ≥ 0, ∂Γ/∂e_ℓ = g_ℓ ≥ 0, ∂Σ/∂Φ(ℓ) = w₀(ℓ) ≥ 0 (under A1)
   — no counter-intuitive side effects
5. **Discreteness:** Σ, Γ, A are finite sums over a fixed, small set of layers — the ℓ axis is
   not a continuum, there is no L→∞ limit and no integral form. (An earlier draft carried an
   integral form; its L→0 artifact — Σ→0 regardless of how concentrated the integration is —
   came from the vanishing integration measure and does not occur here.)

## 7. Interfering layers — extension with competition/exclusion

Opening question: must w₀(ℓ) be non-negative, or can there be layers that *actively harm*
global integration (analogy to the sign of the cosmological constant)? Empirical candidates:
competing sub-narratives (split-brain, dissociation, confabulation), Gazzaniga's interpreter in
an overwriting/distorting mode rather than passive description.

Solution: splitting the weight into two non-negative components instead of a free sign:

$$w(\ell) = w_+(\ell) - w_-(\ell), \qquad w_+,w_- \geq 0$$

Grounded in the **IIT exclusion postulate** (the maximally irreducible complex wins):

$$\ell^{\ast}(t) = \arg\max_\ell \Phi(s,\ell,t)$$

$$\text{overlap}(\ell,\ell^{\ast}) = \frac{|S_\ell\cap S_{\ell^{\ast}}|}{|S_\ell\cup S_{\ell^{\ast}}|}\in[0,1] \quad\text{(Jaccard index on substrates)}$$

$$w_-(\ell,t) = \begin{cases}0 & \ell=\ell^{\ast}(t)\\ \gamma\cdot\text{overlap}(\ell,\ell^{\ast}(t))\cdot\Phi(s,\ell,t) & \ell\neq\ell^{\ast}(t)\end{cases}, \quad \gamma\geq 0$$

**Bound on Σ(t) with competition:**

$$\sum_{\ell\neq\ell^{\ast}}[w_+(\ell)-\gamma]\Phi(\ell,t) + w_+(\ell^{\ast})\Phi(\ell^{\ast},t) \;\leq\; \Sigma(t) \;\leq\; \Sigma_+(t)$$

(γ=0 recovers the old, competition-free Σ₊ as a limiting case — a sanity check).

**Threshold interpretation:** γ vs. inf_ℓ w₊(ℓ) acts as an order parameter:
- γ ≤ inf w₊(ℓ) → Σ(t) stays ≥0 always; the system is structurally resistant to fragmentation
- γ > inf w₊(ℓ) → Σ(t)<0 becomes genuinely reachable = "net fragmentation" of the system

Γ(t) and A(t) do not depend on w₀/w₊/w₋ — the extension is local and does not touch the other
definitions.

### 7.1 A considered alternative — grounding in IIT's hard exclusion (rejected)

A version more strictly grounded in IIT's canonical exclusion postulate was considered: overlap
as a binary gate (whether the substrates overlap at all) + a smooth `tanh` relaxation of the Φ
difference between winner and loser, acting directly on Φ (not on the weight). Checked formally
and numerically — it correctly recovers canonical, hard exclusion in the limit κ→∞.

**Deliberately rejected**, because it structurally **forbids Σ<0** (the losing candidate has at
most φ=0, never φ<0 — as in real IIT). This directly contradicts what we want to keep: the
possibility of "net fragmentation" of the system (the cosmological-constant analogy — layers
that genuinely *subtract* from subjecthood, not merely lose their contribution). Decision:
**priority goes to the model's ability to express the phenomenon, not to strict fidelity to
IIT's canonical exclusion postulate.** This is a deliberate, explicit departure from IIT — to
be named outright in any future write-up so a reviewer does not read it as a misunderstanding
of the formalism.

**The canonical version remains the one from §7** (w=w₊−w₋, continuous Jaccard index,
w₋=γ·overlap·Φ, the exact threshold γ_krit from §9.1) — it allows Σ<0, which is treated here as
a feature of the model, not a bug.

## 9. Toy example — a 3-layer system

Layers: ℓ=1 (homeostasis), ℓ=2 (world-model), ℓ=3 (self-model).

| ℓ | Φ(ℓ) | w₀(ℓ) | e_ℓ | g_ℓ | g_ℓe_ℓ |
|---|------|-------|-----|-----|--------|
| 1 | 0.2 | 0.1 | 0.0 | 0.0 | 0.0 |
| 2 | 0.6 | 0.3 | 0.4 | 0.3 | 0.12 |
| 3 | 0.9 | 0.6 | 0.8 | 0.9 | 0.72 |

**Without competition:** Σ=0.74, Γ=0.84, A≈0.90 — high integration, high constitutive
activity, well spatially aligned (sanity check: the model gives an intuitive result on an
intuitively constructed example).

**With competition (§7):** substrates S₁={a,b}, S₂={b,c,d}, S₃={c,d,e,f}; ℓ\*=argmax Φ = layer
3. overlap(1,3)=0, overlap(2,3)=0.4. At γ=0.5: Σ=0.668, correctly inside the interval
[0.34, 0.74] derived in §7, closer to the upper bound (because the actual overlap(1,3)=0 <<
worst-case=1 assumed in the lower-bound proof — the bound is correct but not tight for these
particular data).

### 9.1 Correction to §7 — the exact critical threshold γ

Since w₋(ℓ)=γ·overlap(ℓ,ℓ\*)·Φ(ℓ) is linear in γ, Σ(γ) is **exactly linear**, not merely
bounded:

$$\Sigma(\gamma) = \Sigma_+ - \gamma\sum_{\ell\neq\ell^{\ast}}\text{overlap}(\ell,\ell^{\ast})\,\Phi(\ell)^2, \qquad \gamma_{\text{krit}} = \frac{\Sigma_+}{\sum_{\ell\neq\ell^{\ast}}\text{overlap}(\ell,\ell^{\ast})\Phi(\ell)^2}$$

(note: the subtracted term is w₋(ℓ)·Φ(ℓ) = γ·overlap·Φ(ℓ)², i.e. Φ squared — not to the first
power). For the example: γ_krit = 0.74/(0.4×0.6²) = 0.74/0.144 ≈ **5.139**, confirmed
numerically (Σ(5.139)=0, Σ(6)=−0.124). This is a sharper result than the inequalities alone —
given a known overlap profile one can state the exact fragmentation threshold, not just a
range.

### 9.2 Dynamic scenario — dissociation, ℓ\* shifts

Two moments: t₀ (layer 3 dominates) → t₁ (a competing sub-narrative in layer 2 takes over:
Φ₂: 0.6→0.85, Φ₃: 0.9→0.5).

| | Σ | Γ | A | ℓ\* |
|---|---|---|---|---|
| t₀ | 0.740 | 0.840 | 0.901 | layer 3 |
| t₁ | 0.575 | 0.680 | 0.963 | layer 2 |

Non-trivial result: Σ and Γ both fall (ΔΣ=−0.165, ΔΓ=−0.16), but **A rises**. This shows that
A(t) does not measure "whether the system is healthy" but "whether self-correction keeps up
with wherever the integrative centre currently is" — a separate question from how much
integration/activity there is in total.

## 10. Discrete dynamics — an asymmetry between Σ and Γ

Checking whether dΣ/dt from §3 reproduces ΔΣ from simulation 9.2 via partial derivatives
rather than a finite difference reveals an important structural asymmetry between Σ and Γ.

**Σ: clean, no error.** In the canonical model (option 2, §5) w(ℓ,t)=w₀(ℓ) is static —
∂w₀/∂t≡0 by definition. The general two-term formula from §3 collapses to one term:

$$\Delta\Sigma = \sum_\ell w_0(\ell)\,\Delta\Phi(\ell), \qquad \Delta\Phi=[0,\,0.25,\,-0.4]$$

$$0.1{\times}0 + 0.3{\times}0.25 + 0.6{\times}(-0.4) = -0.165$$

Exactly matches ΔΣ from the simulation — **with no correction term at all**, because the
absence of a second time-varying factor (w₀ does not change) eliminates the nonlinearity
problem for finite steps entirely.

**Γ: a real, non-trivial second-order error.** Γ=Σg_ℓe_ℓ is a product of *two* time-varying
quantities — the exact discrete identity for the change of a product is:

$$\Delta(g_\ell e_\ell) = \Delta g_\ell\cdot e_\ell(t_0) + g_\ell(t_0)\cdot\Delta e_\ell + \Delta g_\ell\cdot\Delta e_\ell$$

The third term (the cross term) vanishes only in the infinitesimal limit — for finite time
steps (like a dissociative event, not an infinitesimal step) it is real and can be large.
Checked for layer 2: Δg=0.5, Δe=0.3, e₀=0.4, g₀=0.3 → 0.5×0.4 + 0.3×0.3 + 0.5×0.3 =
0.2+0.09+**0.15** = 0.44 (consistent with a direct computation). The cross term (0.15) is about
**34% of the total change** — the discarded infinitesimal approximation ∂Γ/∂t from Theorem 4
would give a significant error here (0.29 instead of 0.44) for an event of this scale.

**Methodological conclusion:** the continuous formula ∂Γ/∂t (Thm. 4, §6) is correct only as an
approximation for small/slow changes; for step-like events (a sudden switch of ℓ\*, a
dissociative episode) one must use the full discrete identity with the cross term, otherwise a
simulation systematically underestimates Γ's variability. Σ is structurally "safer" in this
sense — its linearity in Φ under a static w₀ makes it immune to this problem, whereas Γ, being
bilinear by nature (g×e), is not.

## 12. Literature review (preliminary)

**Conceptually closest work:**
- **Nested Observer Windows (NOW)** (*Neuroscience of Consciousness*, Oxford, 2024) — a
  hierarchical model of consciousness that computes Φ separately at nested "observer window"
  levels; the ratio of Φ between levels as a panpsychism-vs-emergentism test. Close to our
  profile Φ(s,ℓ) — Σ (functional weighting + dynamics) must be explicitly distinguished from
  their approach (the bare Φ_ℓ/Φ_ℓ₋₁ ratio).
- **"Consciousness as Uncommon Self-Knowledge" (USK)** (arXiv, 2026) — synergistic,
  self-directed information as an alternative to raw Φ; explicitly predicts a gap between high Φ
  and the absence of a self-model. An independent confirmation of the intuition behind Γ/A — to
  be cited with a clear distinction from our triple (Σ,Γ,A) with temporal dynamics and the
  exclusion mechanism.
- **"Can We Test Consciousness Theories on AI?"** (December 2025) — architectural ablations:
  removing the self-model abolishes metacognitive calibration while leaving task performance
  intact — an empirical counterpart of the descriptive/constitutive distinction of §2.7 (a good
  source for a testability section).
- **INTREPID** (Templeton World Charity Foundation; Tononi, Friston, Pennartz) — an ongoing
  formal adversarial collaboration IIT vs. predictive processing — confirms that R_ℓ(i) gated
  by Wolfram irreducibility (bridging IIT with a predictive hierarchy) is an active, unresolved
  research front.

**Important correction to §7:** the official exclusion postulate in IIT 4.0 is **binary**
("winner takes all" — substrates with lower φ are excluded entirely, φ=0), not gradable. Our
mechanism w₋(ℓ)=γ·overlap·Φ(ℓ) is a **soft, continuous generalization**, a deliberate
departure from the canonical postulate, not its direct interpretation — this must be named
outright in the paper, otherwise a reviewer will read it as a misunderstanding of the IIT
formalism.

**Assessment:** the Σ synthesis (hierarchical + functionally weighted + self-prediction-error
dynamics + soft exclusion) has no direct counterpart in the literature found — the components
exist separately (NOW, USK, INTREPID), their combination into one formalism with proven
boundary properties appears original. The review is still preliminary — PhilPapers/PhilSci-
Archive and older work (2015–2023) beyond what was found by search have not been checked
systematically.

## 14. Application to transformer architectures

**The constitutive loop.** A standard transformer at inference has frozen weights — g_ℓ(t)≡0,
regardless of self-narration quality. Sharp conclusion from §2.7: **Γ(t)≡0 for any standard LLM
at inference, by definition**. A further consequence from §5.1: since g_ℓe_ℓ≡0 everywhere (no
variance), A(t):=0 by the boundary convention — the spatial-alignment question loses its
meaning, exactly as predicted.

**Titans** (Behrouz, Zhong, Mirrokni; Google Research, December 2024; NeurIPS 2025) — a
long-term memory module updated *at inference time*: "surprise" = the gradient of the loss with
respect to input (the e_ℓ counterpart), driving a real online state update (the g_ℓ>0
counterpart):
$$S_t = \arg\min_S \tfrac{1}{2}\|Sk_t-v_t\|^2 + \tfrac{1}{2\eta}\|S-S_{t-1}\|^2$$
The first concrete instance of the constitutive mechanism of §4. **Caveat:** it predicts data
from context (associative memory), not the system's own future state as in the e_ℓ definition
of §4 — genuinely constitutive world-modelling, not necessarily self-modelling, unless the
system processes its own earlier utterances as part of the context (in conversational dialogue
this boundary blurs).

A weaker, intermediate case: **in-context learning as implicit gradient descent** (von Oswald
et al. 2023) — attention alone, in a single forward pass, implements a "mesa-optimization"
structurally similar to a gradient step, but it does not survive beyond the context window (no
lasting change to θ) — a candidate for an intermediate category between descriptive and
constitutive, fully neither.

**Homeostatic layer** — a confirmed, real gap. "Interoceptive Machine Framework" (2026) and
"Truth or Consequences: Homeostatic Self-Regulation" (ALIFE) propose regulating internal states
against a set point — an active but marginal current, nowhere merged with mainstream LLMs.
Layer norm is structural stabilization, not homeostasis in this sense.

**Genuine recurrence** — present in SSMs (Mamba) and Titans-style hybrids (a real state
evolving independently of new tokens), absent from pure attention (the KV-cache is context
memory, not a dynamical loop).

**Resolving the self- vs. world-modelling ambiguity (§4.1):** two independent conditions — (a)
prediction target: internal state (h_ℓ) or external behaviour (a token)? (b) update timing:
online at deployment or only during training?

| | training only | online at deployment |
|---|---|---|
| target = external behaviour | ordinary predictive training | **Titans** — constitutive, but *world*-modelling |
| target = internal state | **"Unexpected benefits of self-modelling"** (Royal Society, 2026) — a self-model, but frozen after training = descriptive | **"Temporal Self-Model"** (2026) — the only cell satisfying the full definition of e_ℓ,g_ℓ from §4; needs confirmation that the update is genuinely online, not just trained by standard backprop |

Only the bottom-right corner is genuine constitutive self-modelling in our sense. Titans,
despite its prominence, lands in a different cell than it first appeared to.

**Synthesis:** a standard, frozen LLM at inference: potentially high Σ (attentional
integration), Γ≡0, A≡0 by convention. None of the architectures found is yet a confirmed,
unambiguous example of the bottom-right corner — TSM is the closest, with a caveat.

## 16. Hypothesis: two independent mechanisms of anaesthesia in (Σ,Γ,A)

At a constant level of integration, self-referentiality can be reduced in two qualitatively
different ways: (1) lower Γ directly, in place, or (2) displace it toward a region of lower
integration (a drop in A, not necessarily Γ). The anaesthesiology literature supplies two
separate cases matching this distinction.

**Mechanism 1 (Γ drops directly, in place):** propofol and sevoflurane strike the so-called
*posterior hot zone* — the region IIT proponents explicitly identify as the primary substrate
of consciousness (as opposed to GNW, which favours frontoparietal networks) — and at the same
time disrupt frontoparietal feedback connectivity (front→back), associated with higher-order
processing. Integration and self-correction collapse together, in the same place.
Behaviourally: complete loss of consciousness, no report at all — consistent with Σ and Γ
falling together.

**Mechanism 2 (Γ persists, A drops):** subanaesthetic ketamine produces dissociation —
responsiveness and often vivid, rich experience can persist, but with a disturbed sense of
self. It separately desegregates the salience network ("minimal", bodily self) and the DMN
("biographical", narrative self) — two tiers of self-modelling that map reasonably onto the
layers ℓ of this model. Overall experiential richness does not collapse the way it does under
propofol (hence the vivid, "psychedelic"-quality ketamine reports) — self-correction does not
vanish, it merely decouples from wherever integration currently is: a drop in A, not
necessarily in Σ or Γ.

**Status:** a plausible, anatomically grounded hypothesis, not a confirmed result — no one has
computed (Σ,Γ,A) directly on EEG/fMRI data from either anaesthetic. A concrete, testable
prediction: the (Σ,Γ,A) profile should clearly distinguish propofol/sevoflurane (Σ↓, Γ↓
together) from ketamine (Σ relatively preserved, Γ relatively preserved, A↓) — even though both
"switch off" some form of normal functioning.

## 17. The readout channel R_ℓ(t) — separating internal state from observability

Section 16 exposes an axis the formalism previously lacked: (Σ,Γ,A) describes the *internal*
state but says nothing about whether that state can be read off from behaviour. Clinically this
is exactly the problem that forced Massimini and Tononi to invent the Perturbational Complexity
Index — a measure "independent of sensory processing and behaviour" (Casali et al. 2013).

### 17.1 Definition

We single out a separate efferent substrate M(t) (units responsible for movement/
communication), distinct from the layers ℓ. The readout channel from layer ℓ to M, using the
same distance measure D as base Φ:

$$R_\ell(t) = D\big(p(m' \mid s_\ell, m) \,\|\, p(m' \mid m)\big)$$

— how much knowing layer ℓ's state changes the predictability of the effectors' future state,
beyond what knowing the effectors' current state alone provides. Structurally identical to the
definition of Φ_{ℓ,ℓ-1} (§2.1), just directed at the layer→output channel. **R_ℓ(t) ≥ 0** by
the same argument (a distance), with no extra assumptions. Of particular importance:
**R_L(t)** — the channel from the topmost, self-modelling layer to the effectors.

### 17.2 Observable vs. actual

What the clinician sees (Σ_obs — "visible" consciousness, from behaviour) is bottlenecked by
R_L, independent of the actual Σ:

$$\Sigma_{\text{obs}}(t) \le \kappa \cdot R_L(t) \quad \text{for some } \kappa > 0$$

If R_L(t)=0, then Σ_obs(t)=0 **regardless of how high the actual Σ(t) is** — a formalization of
the risk of conflating Σ_obs with Σ.

### 17.3 Clinical mapping

- **Locked-in syndrome:** Σ,Γ,A normal; R_L≈0 due to structural damage to efferent pathways
  (e.g. a ventral pontine stroke) → Σ_obs≈0 despite high Σ.
- **REM sleep:** Σ,Γ,A relatively preserved (PCI≈wakefulness, Casali et al. 2013); R_L actively
  suppressed by a known, specific, reversible physiological mechanism — REM atonia, inhibition
  of spinal motor neurons by the subcoeruleus nucleus. Confirms that R_ℓ as a separate,
  gate-able quantity has a real neural substrate, not just theoretical convenience.
- **"Cognitive motor dissociation"** (a subset of vegetative-state patients, Owen-style
  paradigms): R_L partial — enough to modulate a neuroimaging response to command, not enough
  to reach muscle. Suggests a possible extension: R computed separately to different subsets of
  M (neural, detectable in fMRI, vs. muscular).
- **True vegetative state (no covert awareness):** both Σ and R_L low — the distinction PCI was
  built to resolve.

## 18. Context-sensitivity of the gate g_ℓ — "context blindness" and a "too intense world"

A source (contextthinking.org, citing Friston 2010 and Van de Cruys et al. 2014, "Precise
minds in uncertain worlds: Predictive coding in autism", *Psychological Review*): "Processing
context requires the brain to give its expectations the right weight. If those expectations are
given too little weight, or if prediction errors remain too rigidly large, integrating context
fails." Van de Cruys et al. propose **aberrant precision** as a mechanism in autism —
prediction errors receive too rigidly high a weight, independent of context. Qela et al. (2025)
map related predictive-mechanism deviations across autism, schizophrenia, and depression.

### 18.1 A closing gap in the model

"Weight given to expectations" is, in predictive-processing jargon, **precision** — and that is
structurally exactly our g_ℓ(t). The formalism so far had no place for **context** to normally
modulate that weight. Extension:

$$g_\ell(t) = h\big(e_\ell(t),\, C(t)\big), \qquad \chi_\ell(t) = \left|\frac{\partial g_\ell}{\partial C}\right| \ge 0$$

where C(t) is a contextual signal and χ_ℓ(t) — a **new parameter** — measures how strongly
context modulates the error's weight. **χ_ℓ(t) ≥ 0** trivially (an absolute value), with no
extra assumptions — as with R_ℓ, we assume no upper bound without further axioms about the
shape of h.

### 18.2 Two regimes

- **Normal, context-sensitive precision (χ_ℓ>0):** familiar, expected, contextually irrelevant
  signals automatically get a lower weight — g_ℓ drops regardless of whether e_ℓ is itself
  large.
- **"Context blindness" (χ_ℓ≈0):** g_ℓ(t) ≈ ĝ_ℓ(e_ℓ(t)) — a rigid function of the error
  alone, context changes nothing. Effect: signals that context would normally suppress keep
  getting full weight — the formal counterpart of a "too intense world" (Intense World Theory,
  Markram & Markram 2010): nothing is discounted by default as "already predicted in this
  context".

### 18.3 Consequence for Γ

Typically, repeated, contextually irrelevant stimulation lowers both e_ℓ (via predictive
learning — repetition suppression) and g_ℓ (via active contextual suppression, χ_ℓ>0) — a
compounded drop in the contribution to Γ. Under context blindness only the first mechanism
operates (if at all) — Γ(t) stays elevated/variable even in low-novelty environments. A
formalizable, at least qualitatively testable difference in Γ dynamics between the typical and
the "aberrant precision" case — though no one has measured it directly in these terms.

## 19. Further considerations (informal — no proofs, lower status than the rest)

### 19.1 Scale: from a single cell to the whole universe

The question of the range of scales over which the model permits subjecthood — from the
smallest to the largest possible systems.

**Lower bound.** Bare IIT is permissive: "Minimal physicalism as a scale-free substrate for
cognition and consciousness" (2021) argues that gene-regulatory and signal-transduction
networks at the single-cell level have positive Φ. **Our model is more restrictive** —
positive Φ is not enough, Γ>0 is required, a real, online self-prediction loop. A single cell
has homeostasis, not a self-model in the sense of §4. *C. elegans* (302 neurons, a mostly
feedforward connectome, little recurrence) is a good test case: probably low/zero Γ despite
non-zero Φ.

**Upper bound.** "Upper bounds for integrated information" (2024) shows that Φ can grow
hyper-exponentially with unit count — no mathematical ceiling. But: (1) the exclusion postulate
does not allow summing upward — a larger system wins only if it has **higher** Φ, not more
units; (2) large-scale systems (the internet, the biosphere, society) have sparse, slow
connectivity relative to neurons, so empirically they do not outdo the brain.

**The whole universe — a "double no".** This is literally the *combination problem* of
panpsychism, pushed to the limit. Two independent lines of reasoning converge on the same
conclusion: (1) **structurally**, Koch/Tononi's answer to Searle's objection ("consciousness
smeared like jam") — "my consciousness, your consciousness, but nothing in between" — the
universe is a mosaic of local maxima ("ontological dust"), never a superordinate whole,
because an aggregate (e.g. a brain + the rest of the cosmos) has lower Φ than its more densely
connected parts; (2) **physically**, regions beyond each other's cosmological horizons have
never been in causal contact — there is not even anything to put into the transition matrix Φ
requires. Under Σ a third reason is added: no unified Γ at cosmological scale exists. A
non-rigorous aside: since integration requires dense, fast structure, and the universe is
thinning toward heat death, we may be closer to the peak possible integration density in the
history of the cosmos than to it lying in the far future.

**Overarching caveat:** IIT itself, on which all this rests, is scientifically contested (2023:
an open letter from 124 researchers, including Dennett, calling IIT pseudoscience;
COGITATE/Templeton — an inconclusive result against GNW).

### 19.2 Alien hand syndrome as an illustration of net fragmentation (§7)

The cleanest illustration of Σ<0 found. With damage to the corpus callosum — a reduced
Φ_{ℓ,ℓ-1} between the hemispheres — two candidate motor-intentional complexes not only stop
cooperating but **actively oppose each other**: "diagonistic dyspraxia" — one hand literally
undoes what the other just did. This is integration below zero, not merely its absence —
exactly the mechanism of §7, and the same line of research (split-brain, corpus callosum) as
the Gazzaniga interpreter motivating §2.7 at the very start.

**A weaker, partial match: dissociative identity disorder (DID).** Well documented: distinct,
compartmentalized neural signatures for different identity states, connectivity shifts on
switching — fits ℓ\*(t) changing over time (the dissociation scenario of §9.2). Less well
documented: whether one state **actively degrades** another's integration (true Σ<0) or merely
replaces it (amnesia barriers look more like "lack of access" than active interference in the
w₋ sense). The status of DID as a diagnostic category is itself a matter of genuine scientific
debate (trauma model vs. sociocognitive model) — unresolved.

## 20. Open threads

- Toy example — computed (§9); literature review — preliminarily done (§12), but unsystematic
  (no search of PhilPapers/PhilSci-Archive and 2015–2023 work beyond what was found)
- Source verification of citations — done 2026-08-28, see `notes/citations.md` (a few
  volume/page numbers still flagged there)
- Application to transformer architectures: what is missing (a homeostatic layer, genuine
  recurrence, a constitutive loop) — partly touched on, not formalized
- Publication venues considered earlier: LessWrong/Alignment Forum, PhilSci-Archive (low
  barrier), arXiv q-bio.NC/cs.AI (needs endorsement), Journal of Consciousness Studies, Entropy
  (MDPI), Neuroscience of Consciousness (Oxford)
