TECTONIC ?= tectonic

MANUSCRIPT_TEX := manuscript/main.tex
MANUSCRIPT_BIB := manuscript/references.bib
MANUSCRIPT_PDF := manuscript/main.pdf
OUTPUT_PDF := output/pdf/constructive-ym-fixed-volume-milestone.pdf

.PHONY: all manuscript

all: manuscript

manuscript: $(OUTPUT_PDF)

$(OUTPUT_PDF): $(MANUSCRIPT_TEX) $(MANUSCRIPT_BIB)
	mkdir -p output/pdf
	cd manuscript && $(TECTONIC) --keep-logs --keep-intermediates main.tex
	cp $(MANUSCRIPT_PDF) $(OUTPUT_PDF)
