# premakumar2026

**Premakumar, V. N., Vaiana, M., Pop, F., Rosenblatt, J., Schwerz de Lucena, D., Ziman, K., & Graziano, M. S. A.** (2026). *Unexpected benefits of self-modelling in neural systems.* Philosophical Transactions of the Royal Society A, 384(2320), 20240531. Preprint: arXiv:2407.10188 [cs.LG] (2024).

- DOI: https://doi.org/10.1098/rsta.2024.0531 · https://arxiv.org/abs/2407.10188
- Type: journal article (preprint 2024, journal version 2026)
- Open access: preprint yes

## Abstract (verbatim, arXiv version)
"Self-models have been a topic of great interest for decades in studies of human cognition and more recently in machine learning. Yet what benefits do self-models confer? Here we show that when artificial networks learn to predict their internal states as an auxiliary task, they change in a fundamental way. To better perform the self-model task, the network learns to make itself simpler, more regularized, more parameter-efficient, and therefore more amenable to being predictively modeled. To test the hypothesis of self-regularizing through self-modeling, we used a range of network architectures performing three classification tasks across two modalities. In all cases, adding self-modeling caused a significant reduction in network complexity. The reduction was observed in two ways. First, the distribution of weights was narrower when self-modeling was present. Second, a measure of network complexity, the real log canonical threshold (RLCT), was smaller when self-modeling was present. Not only were measures of complexity reduced, but the reduction became more pronounced as greater training weight was placed on the auxiliary task of self-modeling. These results strongly support the hypothesis that self-modeling is more than simply a network learning to predict itself. The learning has a restructuring effect, reducing complexity and increasing parameter efficiency. This self-regularization may help explain some of the benefits of self-models reported in recent machine learning literature, as well as the adaptive value of self-models to biological systems. In particular, these findings may shed light on the possible interaction between the ability to model oneself and the ability to be more easily modeled by others in a social or cooperative context."

## Role in Model Σ
§14, the 2×2 table: a network trained with an auxiliary hidden-state self-prediction loss
(target = *internal state* h_ℓ) — but the update is **frozen after training**, so at deployment
it is descriptive (g_ℓ ≈ 0). Cell (target = internal state) × (training only).
