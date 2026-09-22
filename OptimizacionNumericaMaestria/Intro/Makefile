# Build the Introducción a la Optimización Numérica beamer deck.
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

TEX := intro_OptimizacionNumerica.tex
PDF := $(TEX:.tex=.pdf)
LOG := $(TEX:.tex=.log)

.PHONY: all clean rebuild distclean preview

all: $(PDF)

# The PDF depends on the source.
$(PDF): $(TEX)
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

distclean: clean
	rm -f $(PDF)

# Rebuild = delete intermediates + the PDF, then rebuild from scratch.
rebuild: distclean all

# Render preview pages (requires Poppler pdftoppm).
preview: $(PDF)
	mkdir -p preview
	@for page in 1 2 3 4 5 6 7 8; do \
	  pdftoppm -f $$page -l $$page -scale-to 1600 -singlefile -png $(PDF) preview/slide-$$page; \
	done
