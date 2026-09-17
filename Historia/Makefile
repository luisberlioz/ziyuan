# Build the Historia beamer deck.
#
# pdflatex is run in a loop until the log no longer contains a
# "Rerun to get" warning — this stabilizes the \AtBeginSection
# TOC inserts and hyperref bookmarks.
#
# Usage:
#   make          # build the PDF
#   make clean    # remove intermediate LaTeX build artifacts
#   make rebuild  # clean + build
#
# Requires: pdflatex on PATH (TeX Live / MiKTeX / MacTeX).

TEX := historia_sistemas_numericos_beamer.tex
PDF := $(TEX:.tex=.pdf)
LOG := $(TEX:.tex=.log)

.PHONY: all clean rebuild

all: $(PDF)

# The PDF depends on the source plus every image in images/.
$(PDF): $(TEX) $(wildcard images/*)
	@echo "Building $(PDF)..."
	@i=1; \
	while [ $$i -le 5 ]; do \
	  echo "  pdflatex pass $$i"; \
	  pdflatex -interaction=nonstopmode -halt-on-error $(TEX) >/dev/null || exit 1; \
	  if ! grep -q "Rerun to get" $(LOG); then \
	    echo "  TOCs stable after $$i pass(es)"; \
	    break; \
	  fi; \
	  i=$$((i + 1)); \
	done

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.fls *.fdb_latexmk *.synctex.gz

rebuild: clean all
