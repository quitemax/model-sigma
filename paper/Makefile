# Build the Model Sigma paper PDFs from the LaTeX sources.
# Requires a TeX distribution (TeX Live / MiKTeX) providing pdflatex.
#
#   make          # build both PDFs
#   make clean    # remove LaTeX aux files (not the PDFs)

LATEX   := pdflatex -interaction=nonstopmode -halt-on-error
SOURCES := sigma_model_en sigma_model_pl
PDFS    := $(addsuffix .pdf,$(SOURCES))
AUX     := $(foreach s,$(SOURCES),$(s).aux $(s).log $(s).out $(s).toc)

.PHONY: all clean

all: $(PDFS)

# Two passes so \ref, \cite and the thebibliography numbering resolve.
%.pdf: %.tex
	$(LATEX) $<
	$(LATEX) $<

clean:
	rm -f $(AUX)
