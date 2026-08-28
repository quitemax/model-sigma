# Model Σ

*English | [Polski](README.pl.md)*

A hierarchical, functionally-weighted extension of Integrated Information Theory (IIT) — a
working conceptual synthesis developed in dialogue with Claude (Anthropic), August 2026.

## Navigation

- **The paper:** [`paper/sigma_model_en.tex`](paper/sigma_model_en.tex) — the leaner, argued version (leads with the $(\Sigma,\Gamma,A)$ triple and the AI argument; competing-layers / $\Sigma<0$ is one paragraph). PDFs: [EN](paper/sigma_model_en.pdf) · [PL](paper/sigma_model_pl.pdf) (Polish source: [`sigma_model_pl.tex`](paper/sigma_model_pl.tex))
- **The full working draft** (everything considered, accreted order): [`paper/model_sigma.md`](paper/model_sigma.md) · Polish: [`paper/model_sigma.pl.md`](paper/model_sigma.pl.md)
- Why it is the way it is: [`notes/decisions.md`](notes/decisions.md) · literature map: [`notes/literature.md`](notes/literature.md)
- Bibliography with abstracts: [`references/`](references/) ([index](references/README.md)) · citation audit: [`notes/citations.md`](notes/citations.md)
- The paper's numbers, executable: [`examples/toy_example.py`](examples/toy_example.py)
- [Project status](#project-status) · [Open threads](#open-threads) · [Building the PDFs](#building-the-pdfs) · [Running the example](#running-the-numerical-example)

## Repository layout

- [`paper/`](paper/)
  - [`sigma_model_en.tex`](paper/sigma_model_en.tex) / [`sigma_model_pl.tex`](paper/sigma_model_pl.tex) — **the paper** (EN / PL): the leaner, argued version
  - [`model_sigma.md`](paper/model_sigma.md) — the full working draft, English (everything considered, in accreted order); the paper's editorial choices are the current position where they differ
  - [`model_sigma.pl.md`](paper/model_sigma.pl.md) — Polish translation of the working draft
  - [`sigma_model_en.pdf`](paper/sigma_model_en.pdf) / [`sigma_model_pl.pdf`](paper/sigma_model_pl.pdf) — compiled PDFs, build artifacts; **currently stale** (predate the restructure) — regenerate with `make` or the `build-paper` CI
  - [`Makefile`](paper/Makefile) — `make` builds both PDFs, `make clean` removes auxiliary files
- [`notes/`](notes/)
  - [`decisions.md`](notes/decisions.md) — a log of the key decisions (the why, not just the what)
  - [`citations.md`](notes/citations.md) — citation audit (what was verified / corrected)
  - [`literature.md`](notes/literature.md) — claim-by-claim precedent map; what's new vs. already done
  - [`layer-decomposition.md`](notes/layer-decomposition.md) — how the functional layers should be derived, not stipulated
  - [`related-theories.md`](notes/related-theories.md) — notes on adjacent frameworks (e.g. Grounded Duality Theory)
- [`references/`](references/) — one `.md` file per bibliography entry (details, link, abstract, role in Σ); [index](references/README.md)
- [`examples/`](examples/)
  - [`toy_example.py`](examples/toy_example.py) — every numerical result from the paper, in one place
- [`.github/workflows/build-paper.yml`](.github/workflows/build-paper.yml) — CI: compiles both PDFs and runs `toy_example.py`

## Project status

An internally consistent conceptual synthesis. Core: the state triple **(Σ, Γ, A)** over a
small fixed set of functional layers — integrated information, constitutive self-correction
activity (self-prediction error that drives an online parameter update, not merely a report),
and their alignment — built from disjoint variables. Sharpest consequence: Γ ≡ 0 for any
frozen-weight LLM at inference, by definition. Plus a readout channel R_ℓ, a numerical example,
and a literature review. The competing-layers / Σ<0 material is kept only as a sketched
direction. **Not peer-reviewed; no empirical instantiation; inherits IIT's foundational
problems.**

## Open threads

- A systematic (not merely search-driven) literature review — PhilPapers / PhilSci-Archive
- One worked empirical case — e.g. computing (Σ,Γ,A) on real EEG/fMRI (propofol vs. ketamine),
  though g_ℓ may not be recoverable from neural data
- A principled account of the layer decomposition (currently stipulated)

Settled: the paper (`sigma_model_en.tex`) leads with the triple + AI argument and demotes
competing-layers to one paragraph; citation verification
([`notes/citations.md`](notes/citations.md)); removal of the integral form. Full decision log
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
