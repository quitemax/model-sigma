# predmetacog2026

**Luo, W., & Jho, H.** (2026). *Predictive metacognition: a neuro-computational framework for self-monitoring in large language models.* Scientific Reports.

- DOI: https://doi.org/10.1038/s41598-026-54840-2
- Type: journal article
- Open access: yes (summary below is not verbatim)

## Summary (not verbatim)
Integrates predictive-processing principles and anterior-cingulate-style monitoring into
transformer architectures: an "Error-Driven Learning + Dual-Process Monitoring" scheme in which
the model is fine-tuned (LoRA on Llama-3-8B-Instruct and Phi-3-Mini) to generate a response and
assess its own reliability at the same time. Against GPT-4o and Claude-3.5-Sonnet baselines,
reports statistically significant improvements in confidence calibration.

## Role in Model Σ
§14 — a concrete "self-monitoring in an LLM" case. It improves calibration but the update is a
*training-time* fine-tune, not an online parameter update at deployment, so Γ stays ≡ 0 for the
deployed model. Illustrates the descriptive vs. constitutive line. Added 2026-08-28; see
`../notes/literature.md`.
