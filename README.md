# Model Σ

*English | [Polski](README.pl.md)*

A hierarchical, functionally-weighted extension of Integrated Information Theory (IIT) — a
working conceptual synthesis developed in dialogue with Claude (Anthropic), August 2026.

## Navigation

- **Start here:** [`paper/model_sigma.md`](paper/model_sigma.md) — the full working draft (19 sections), **the source of truth**
- Polish translation: [`paper/model_sigma.pl.md`](paper/model_sigma.pl.md)
- Typeset versions: [PDF EN](paper/sigma_model_en.pdf) · [PDF PL](paper/sigma_model_pl.pdf) (sources: [`sigma_model_en.tex`](paper/sigma_model_en.tex) · [`sigma_model_pl.tex`](paper/sigma_model_pl.tex))
- Why it is the way it is: [`notes/decisions.md`](notes/decisions.md) · literature map: [`notes/literature.md`](notes/literature.md)
- Bibliography with abstracts: [`references/`](references/) ([index](references/README.md)) · citation audit: [`notes/citations.md`](notes/citations.md)
- The paper's numbers, executable: [`examples/toy_example.py`](examples/toy_example.py)
- [Project status](#project-status) · [Open threads](#open-threads) · [Building the PDFs](#building-the-pdfs) · [Running the example](#running-the-numerical-example)

## Repository layout

- [`paper/`](paper/)
  - [`model_sigma.md`](paper/model_sigma.md) — the full working draft (19 sections), **the source of truth** (English)
  - [`model_sigma.pl.md`](paper/model_sigma.pl.md) — Polish translation (keep in sync with `model_sigma.md`)
  - [`sigma_model_en.tex`](paper/sigma_model_en.tex) / [`sigma_model_pl.tex`](paper/sigma_model_pl.tex) — LaTeX sources (EN / PL), a condensed and contiguously renumbered version
  - [`sigma_model_en.pdf`](paper/sigma_model_en.pdf) / [`sigma_model_pl.pdf`](paper/sigma_model_pl.pdf) — compiled PDFs, build artifacts (regenerate with `make`)
  - [`Makefile`](paper/Makefile) — `make` builds both PDFs, `make clean` removes auxiliary files
- [`notes/`](notes/)
  - [`decisions.md`](notes/decisions.md) — a log of the key decisions (the why, not just the what)
  - [`citations.md`](notes/citations.md) — citation audit (what was verified / corrected)
  - [`literature.md`](notes/literature.md) — claim-by-claim precedent map; what's new vs. already done
- [`references/`](references/) — one `.md` file per bibliography entry (details, link, abstract, role in Σ); [index](references/README.md)
- [`examples/`](examples/)
  - [`toy_example.py`](examples/toy_example.py) — every numerical result from the paper, in one place
- [`.github/workflows/build-paper.yml`](.github/workflows/build-paper.yml) — CI: compiles both PDFs and runs `toy_example.py`

## Project status

An internally consistent conceptual synthesis: the full static and dynamic formalism (Σ, Γ, A)
— finite sums over layers, no integral form — proven boundary properties, a competition/
exclusion mechanism (soft w = w₊ − w₋, allows Σ<0 as an intended feature), the readout channel
R_ℓ, context-sensitivity of the gate g_ℓ, a numerical example, a preliminary literature review,
and application to transformer architectures. **Not peer-reviewed.**

## Open threads

- A systematic (not merely search-driven) literature review
- An empirical instantiation beyond the toy example — e.g. computing (Σ,Γ,A) on real EEG/fMRI
  data (propofol vs. ketamine, PCI under anaesthesia) — see the hypothesis in §16 of the paper

Settled: §7 vs §7.1 (§7 kept, Σ<0 as a feature), citation verification
([`notes/citations.md`](notes/citations.md)), removal of the integral form. Full decision log
and rationale: [`notes/decisions.md`](notes/decisions.md).

## Building the PDFs

Requires a TeX distribution (TeX Live / MiKTeX):

```
cd paper
make            # builds sigma_model_en.pdf and sigma_model_pl.pdf (two passes each)
make clean      # removes auxiliary files (.aux/.log/.out/.toc)
```

Without `make` (e.g. a bare MiKTeX on Windows):

```
cd paper
pdflatex sigma_model_en.tex && pdflatex sigma_model_en.tex
pdflatex sigma_model_pl.tex && pdflatex sigma_model_pl.tex
```

The PDFs committed to the repo are build artifacts — after editing the sources they must be
rebuilt (`make`) or downloaded from the CI artifacts (the `build-paper` workflow).

## Running the numerical example

```
cd examples
python3 toy_example.py
```
