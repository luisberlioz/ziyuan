# Egyptian numeral hieroglyph vector assets

Vector (SVG + PDF) assets for the seven base numerals of the ancient Egyptian
hieroglyphic numeral system, prepared for the **Historia de la Matemática**
beamer deck (`historia_sistemas_numericos_beamer.tex`, course MM-517,
Universidad Nacional Autónoma de Honduras).

All seven glyphs were sourced from Wikimedia Commons as authentic SVG
renders of each numeral symbol. The SVG sources are pure path geometry —
**no embedded fonts, no `<text>` elements, no external font URLs**.

## Mapping

| Value       | Symbol                          | Local filename (SVG + PDF)        | Commons category                         | Commons file                                  |
| ----------- | ------------------------------- | --------------------------------- | ---------------------------------------- | --------------------------------------------- |
| 1           | stroke                          | `1-stroke.{svg,pdf}`              | Stroke (hieroglyph)                      | `Num aeg hierog 0000001 L2R 80px.svg`         |
| 10          | cattle hobble (heel-bone)       | `10-cattle-hobble.{svg,pdf}`      | Animal fetter "10" (hieroglyph)          | `Num aeg hierog 0000010 L2R 80px.svg`         |
| 100         | coil of rope                    | `100-coil-rope.{svg,pdf}`         | Coil "100" (hieroglyph)                  | `Num aeg hierog 0000100 L2R 80px.svg`         |
| 1 000       | lotus plant                     | `1000-lotus.{svg,pdf}`            | Lotus plant (hieroglyph)                 | `Num aeg hierog 0001000 L2R 80px.svg`         |
| 10 000      | finger (pointing)               | `10000-finger.{svg,pdf}`          | Finger (hieroglyph)                      | `Num aeg hierog 0010000 L2R 80px.svg`         |
| 100 000     | tadpole                         | `100000-tadpole.{svg,pdf}`        | Tadpole (hieroglyph)                     | `Num aeg hierog 0100000 L2R 80px.svg`         |
| 1 000 000   | Heh (god of infinity, kneeling) | `1000000-heh.{svg,pdf}`           | Heh-god (hieroglyph)                     | `Num aeg hierog 1000000 L2R 80px.svg`         |

All paths are relative to this folder, `Historia/images/egyptian/`. The
seven numerals above are the seven canonical values of the Egyptian
hieroglyphic numeral system; composition is purely additive (e.g. 2 500 =
2 lotuses + 5 hundreds + 0 tens + 0 units) so the table covers the conventional powers of ten through one million.

## License and attribution

All seven SVG files are by **Otfried Lieberknecht** (Wikimedia Commons
username; the user page is a redlink as of 2026-09-17, but the file
upload history is auditable) and were published by the author under the
**Creative Commons Attribution-ShareAlike 3.0** license (CC BY-SA 3.0).

- License text: <https://creativecommons.org/licenses/by-sa/3.0/legalcode>
- Author (redlink user page): <https://commons.wikimedia.org/w/index.php?title=User:Otfried_Lieberknecht&action=edit&redlink=1>
- Per-file description pages (verify, license, history, dimensions):
  `https://commons.wikimedia.org/wiki/File:<Commons file name from the
  mapping table above>`

> **Attribution (English).** Egyptian numeral hieroglyphs by Otfried
> Lieberknecht, via Wikimedia Commons, used under CC BY-SA 3.0.

> **Atribución (Español).** Jeroglíficos numerales egipcios por Otfried
> Lieberknecht, vía Wikimedia Commons, utilizados bajo CC BY-SA 3.0.

The accompanying PDF files in this folder are direct `rsvg-convert -f pdf`
derivatives of the SVGs and inherit the CC BY-SA 3.0 license terms
(ShareAlike applies to the asset if it is re-shared as a standalone work;
embedding in a larger document is permitted with attribution).

> **Note on "public-domain".** Commons has these files under CC BY-SA 3.0
> rather than PD-marked; they are authentic hieroglyph reproductions by a
> named author and the attribution is recorded above. The actual ancient
> hieroglyph designs are not copyrightable, but this SVG rendering is.

## Verification (2026-09-17)

- **Authenticity.** All 7 SVGs were fetched directly from
  `upload.wikimedia.org` using the URLs returned by the Commons
  `imageinfo` API (`action=query&prop=imageinfo&iiprop=url`). Per-file
  Commons categories (the column above) confirm the glyph identity and
  are reproducible from the description page.
- **No font / text dependency.** `grep -ciE 'font-|<text |@font-face|\.ttf|\.otf|\.woff'`
  reports **0** matches in every SVG. The one `font-family:Sans; ...`
  style block that was originally attached to the `<path>` of
  `10-cattle-hobble.svg` (an Inkscape-default text-style applied to a
  non-text element) was stripped locally; the path now carries only
  `style="color:#000000;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1px"`.
  Renderers like `rsvg-convert`, Inkscape, and modern browsers all treat
  such styles as inert on `<path>`, but the strip is the belt-and-braces
  guarantee.
- **Vector PDFs.** All 7 PDFs are 1-page PDF 1.5 documents produced by
  `rsvg-convert 2.54.7`. They embed the SVG path data as native PDF path
  operators (not rasterized). Sizes range 1075–2439 bytes; intrinsic
  dimensions match the Commons `imageinfo` `width`/`height` (all ~80 px
  tall, width depends on the glyph).
- **Intrinsic dimensions** (verified from each SVG's `width`/`height`):

  | File                  | width × height (px) |
  | --------------------- | ------------------- |
  | `1-stroke.svg`        | 16.4 × 80.6         |
  | `10-cattle-hobble.svg`| 67.3 × 80.0         |
  | `100-coil-rope.svg`   | 39.9 × 79.9         |
  | `1000-lotus.svg`      | 32.0 × 79.9         |
  | `10000-finger.svg`    | 22.9 × 79.8         |
  | `100000-tadpole.svg`  | 45.6 × 80.1         |
  | `1000000-heh.svg`     | 63.5 × 80.0         |

## Usage in the Beamer deck

The PDFs are LaTeX-ready. Example include (mirrors the existing
`maya_unicode` pattern in the same deck):

```latex
\raisebox{-0.3\height}{%
  \includegraphics[height=0.7cm]{images/egyptian/1-stroke.pdf}%
}\,{\scriptsize 1}
```

The SVG sources are kept in-tree so that future edits (color, sizing,
composing compound numerals, exporting a slide-ready PNG via
`rsvg-convert -w <px> -b white -o out.png in.svg`) can be done without
re-downloading from Commons.
