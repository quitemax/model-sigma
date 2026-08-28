# Literature map — 2026-08-28

Second pass on §12 (the first was search-only). Organized by **claim**, each rated
*precedent* (someone has done essentially this), *partial* (the idea exists, this specific form
does not), or *clear* (no precedent found). Bibliographic details are best-effort from search
and **must be verified before citing** — flagged `[verify]` where shaky.

Bottom line up front: the *motivation* (one scalar Φ is not enough) and the *grand-synthesis
ambition* are both well-trodden; two or three specific constructions look genuinely new. The
paper currently over-claims on "Σ can be negative" and under-cites the multidimensional and
IIT+FEP synthesis literature.

---

## A. "A single scalar Φ is not enough" → a multidimensional state — **precedent**

- **Bayne, Hohwy & Owen (2016), "Are there levels of consciousness?"** *Trends in Cognitive
  Sciences* 20(6):405–413. Argues the "levels" picture is untenable and should be replaced by
  **dimensions** of consciousness — content-related and *functional*. This is the direct
  precedent for the (Σ,Γ,A) move. `[verify pages]`
- Follow-ups: Hudetz, "Does Consciousness Have Dimensions?" (Imprint, OA); "Consciousness as a
  multidimensional phenomenon: implications for the assessment of disorders of consciousness,"
  *Neurosci. Conscious.* 2021(2):niab047; "Multidimensional Models of Degrees and Levels of
  Consciousness" (2016). `[verify]`

**Action:** §12 must cite Bayne et al. (2016) and frame (Σ,Γ,A) as an *IIT-grounded, dynamical
instance* of that program — Σ ≈ their integration/differentiation dimension, Γ and A ≈
functional dimensions. Do not present "more than one number" as the novelty.

## B. Functional weight w(ℓ) — weighting Φ_ℓ by a layer's role — **partial**

- The idea that *what a system computes* matters, not only its causal structure, is
  computational functionalism (Agüera y Arcas, and older). No search hit shows a **numerical
  functional weight applied to a per-layer Φ profile**. The specific device (a scalar w(ℓ) ≥ 0
  multiplying Φ_ℓ, split later into w₊ − w₋) appears to be the paper's own.
- Related but different: Oizumi et al. (2016), "Measuring integrated information from the
  decoding perspective," *PLOS Comput. Biol.* 12(1):e1004654 (arXiv:1505.04368) — a practical
  Φ that could be computed per subsystem, but no functional weighting. `[verify]`

**Action:** keep as a modest novelty; cite Oizumi et al. when discussing how Φ_ℓ would actually
be computed.

## C. Hierarchical / layered / multi-scale Φ — **precedent (already cited: NOW)**

- Nested Observer Windows (Riddle & Schooler 2024) — already in the paper.
- Multi-timescale IIT: "From Shorter to Longer Timescales: Converging IIT with the
  Temporo-Spatial Theory of Consciousness" (*Front. Psychol.*, PMC8871397). `[verify]`
- "A Modular Theory of Subjective Consciousness for Natural and Artificial Minds"
  (arXiv:2510.01864, 2025) — modular/hierarchical, AI-facing; check for overlap with §14. `[verify]`
- IIT itself predicts a *single* privileged spatiotemporal scale (the one maximizing
  cause–effect power); the paper's fixed layer set is a deliberate departure worth stating.

## D. Γ — a self-prediction-error / constitutive-self-modelling term — **partial**

- **USK** (Tallam 2026) — already cited; synergistic self-directed information, predicts high-Φ
  / no-self-model gap. Closest existing thing to Γ.
- "Predictive metacognition: a neuro-computational framework for self-monitoring in large
  language models," *Sci. Rep.* 2026 — metacognition as explicit awareness of the
  prediction-error process; directly relevant to §14 and the descriptive/constitutive line. `[verify]`
- The **descriptive vs. constitutive** criterion (does the error drive an online parameter
  update) as the thing that makes a self-model count — no exact precedent found; HOT and
  higher-order approaches ask a related question differently. The *gate* g_ℓ = |∂θ_ℓ/∂e_ℓ| as
  the formal switch looks new.

**Action:** cite the *Sci. Rep.* 2026 metacognition-in-LLMs paper in §14; keep Γ's specific
form (Σ g_ℓ e_ℓ) as a novelty.

## E. Soft / graded exclusion, and Σ < 0 — **the main novelty claim; needs a rewrite**

Two separate things are bundled here and only one is new.

1. **Softening the exclusion postulate** — *partial, well-motivated*. The exclusion postulate
   is under sustained formal attack:
   - **Hanson & Walker (2023), "On the non-uniqueness problem in integrated information
     theory,"** *Neurosci. Conscious.* 2023(1):niad014 — Φ is non-unique *because of* the
     exclusion postulate; Φ=0 and Φ>0 are often predicted simultaneously. `[verify]`
   - "Exclusion and Underdetermined Qualia" (PMC7514894). `[verify]`
   - "Taking Time Seriously in Tononi's IIT" (*JCS* 2016) — precedent for *adding a
     postulate/mechanism to IIT*, which is structurally what §7 does.
   So "replace binary exclusion with something graded" is an idea already in the air. The
   **specific construction** — w = w₊ − w₋, w₋ = γ·Jaccard(S_ℓ, S_{ℓ\*})·Φ_ℓ, with the exact
   linear threshold γ_crit = Σ₊/K — has no precedent found. Keep that as the novelty; cite
   Hanson & Walker as independent motivation.

2. **Negative integrated information (Σ < 0)** — **not unprecedented; the paper currently
   implies it is.** "Whole-minus-parts" Φ variants already go negative:
   - **Barrett & Mediano (2019),** "The Φ measure of integrated information is not well-defined
     for general physical systems," arXiv:1902.04321.
   - **Mediano, Seth & Barrett (2019),** "Measuring Integrated Information: Comparison of
     Candidate Measures in Theory and Simulation," *Entropy* 21(1):17 (arXiv:1806.09373) —
     several candidate measures take negative values. `[verify]`
   - **Integrated Information Decomposition (ΦID)** — Mediano, Rosas, Carhart-Harris, Seth,
     Barrett (~2019–2021), "Beyond integrated information: a taxonomy of information dynamics"
     (arXiv:1909.02297) — Φ has a **negative component = net redundancy** (whole carries *less*
     than the sum of parts). `[verify year/venue]`

   These are negative because the whole is *reducible/redundant* — a measurement property.
   Model Σ's Σ<0 is different in kind: a competing layer's weight **actively subtracts** via
   w₋. §7 must draw this distinction explicitly ("net fragmentation via an anti-weight" vs
   "negative Φ via redundancy"), or a reviewer familiar with ΦID will say the claim is old.

**Action:** rewrite the framing of §7 / §7.1 and the §12 "Assessment" to (a) cite Hanson &
Walker for the exclusion critique, (b) cite Barrett/Mediano/ΦID and distinguish the two senses
of "negative," (c) narrow the novelty claim to the *w₊ − w₋ construction + exact threshold*.

## F. The grand synthesis (IIT + FEP/predictive processing + functionalism) — **precedent: IWMT**

- **Safron (2020), "An Integrated World Modeling Theory (IWMT) of Consciousness,"** *Frontiers
  in Artificial Intelligence* 3:30 — explicitly combines IIT + Global Neuronal Workspace + the
  Free Energy Principle + active inference. This is the closest existing thing to Model Σ's
  ambition and it is **not currently cited**. Difference: IWMT is conceptual/architectural;
  Model Σ is a formalism with a computed triple, proven boundary properties, and an
  exclusion-mechanism variant. That difference must be stated.
- **INTREPID adversarial-collaboration review** — "Integrated information and predictive
  processing theories of consciousness: an adversarial collaborative review," arXiv:2509.00555,
  in *Neurosci. Biobehav. Rev.* 2026. Replace the vague "INTREPID (ongoing)" mention in §12
  with this citation. `[verify authors]`
- "Bridging integrated information theory and the free-energy principle in living neuronal
  networks," arXiv:2510.04084 (2025) — empirical; repeated stimulation lowers *both* free
  energy and Φ along a hill-shaped trajectory, with hierarchical informational cores. Relevant
  to §18 (repetition suppression) and to the empirical-instantiation plan. `[verify]`

**Action:** add a dedicated "vs IWMT" paragraph to §12; re-cite INTREPID properly.

## G. Readout channel R_ℓ / internal-state vs. observability — **partial (PCI already cited)**

- PCI (Casali et al. 2013) — already cited; the paper positions R_ℓ as its formal counterpart.
- Multidimensional DoC assessment literature (§A above) covers "behaviour under-reports the
  internal state" clinically. R_ℓ as a per-layer information-theoretic channel to a distinct
  efferent substrate M, with the R_ℓ=0 ⟺ conditional-independence characterization and the
  data-processing inequality, looks new. Low priority to defend further.

## H. Foundational caveat the paper inherits

- **Barrett & Mediano (2019)** and **Hanson & Walker (2023)**: Φ is not well-defined for
  general systems / is non-unique. Model Σ builds Φ_ℓ on the same contested base and adds
  "D = e.g. earth mover's distance" without commitment. §1 should acknowledge this dependency
  in one sentence rather than leave it for a reviewer.

---

## New citations to add (priority order)

1. Bayne, Hohwy & Owen (2016) — multidimensional consciousness. (§12, §5.1)
2. Safron (2020), IWMT. (§12 — "vs IWMT" paragraph)
3. Hanson & Walker (2023), non-uniqueness from exclusion. (§7, §12)
4. Barrett & Mediano (2019) + Mediano/Rosas ΦID. (§7, §12 — the "negative Φ" distinction; §1 caveat)
5. INTREPID review (arXiv:2509.00555). (§12 — replace the loose mention)
6. "Predictive metacognition ... in LLMs," *Sci. Rep.* 2026. (§14)
7. Oizumi et al. (2016), decoding-perspective Φ. (§B — how Φ_ℓ gets computed; empirical plan)
8. "Bridging IIT and FEP in living neuronal networks" (2025). (§18, empirical plan)

## Originality verdict

- **New (no precedent found):** the w₊ − w₋ soft-exclusion construction with the exact
  threshold γ_crit = Σ₊/K; Γ = Σ g_ℓ e_ℓ with the constitutivity gate g_ℓ = |∂θ_ℓ/∂e_ℓ|; the
  parameter χ_ℓ = |∂g_ℓ/∂C|; the (Σ,Γ,A) triple *as a package* with proven boundary properties.
- **Not new:** multidimensional consciousness (Bayne 2016); the IIT+FEP+functionalism synthesis
  ambition (IWMT); negative integrated-information *as such* (ΦID redundancy); the exclusion
  postulate being broken (Hanson & Walker, and others).

## Still open (a real systematic review would need)

- PhilPapers / PhilSci-Archive keyword sweeps (not done — search-engine only).
- The full ΦID / information-dynamics literature (Mediano, Rosas, Luppi) read properly, not via
  abstracts.
- Pre-2015 work on functional specialization + integration (Tononi & Sporns, Seth) for the
  functional-weight lineage.
- Whether "Temporal Self-Model" / the metacognition-in-agents literature (§14) has a formal
  self-prediction-error term equivalent to Γ.
