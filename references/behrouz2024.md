# behrouz2024

**Behrouz, A., Zhong, P., & Mirrokni, V.** (2024). *Titans: Learning to Memorize at Test Time.* arXiv:2501.00663 [cs.LG]. (Google Research; submitted 31 Dec 2024.)

- DOI: https://doi.org/10.48550/arXiv.2501.00663
- URL: https://arxiv.org/abs/2501.00663
- Type: preprint
- Open access: yes

## Abstract (verbatim)
"Over more than a decade there has been an extensive research effort on how to effectively utilize recurrent models and attention. While recurrent models aim to compress the data into a fixed-size memory (called hidden state), attention allows attending to the entire context window, capturing the direct dependencies of all tokens. This more accurate modeling of dependencies, however, comes with a quadratic cost, limiting the model to a fixed-length context. We present a new neural long-term memory module that learns to memorize historical context and helps attention to attend to the current context while utilizing long past information. We show that this neural memory has the advantage of fast parallelizable training while maintaining a fast inference. From a memory perspective, we argue that attention due to its limited context but accurate dependency modeling performs as a short-term memory, while neural memory due to its ability to memorize the data, acts as a long-term, more persistent, memory. Based on these two modules, we introduce a new family of architectures, called Titans, and present three variants to address how one can effectively incorporate memory into this architecture. Our experimental results on language modeling, common-sense reasoning, genomics, and time series tasks show that Titans are more effective than Transformers and recent modern linear recurrent models. They further can effectively scale to larger than 2M context window size with higher accuracy in needle-in-haystack tasks compared to baselines."

## Role in Model Σ
The first concrete, working instance of the constitutive mechanism of §4: "surprise" = the
gradient of the associative-memory loss with respect to input (the e_ℓ counterpart) drives a
real online state update (the g_ℓ > 0 counterpart). **Caveat (§14):** Titans predicts *context
content* (keys/values from input), not the system's own future internal state — so this is
constitutive *world*-modelling, not self-modelling. In the 2×2 of §14 it lands in the cell
(target = external behaviour) × (online update).
