# Historia de la Matemática — presentación

Fuente: `historia_sistemas_numericos_beamer.tex` (Beamer/Madrid, español).
Salida: `historia_sistemas_numericos_beamer.pdf` (28 páginas).

## Compilar y previsualizar

```sh
cd /data/MyTera/ziyuan/Historia
make           # PDFLaTeX, hasta estabilizar índices
make rebuild   # limpia auxiliares/PDF y recompila
make preview   # PNG de páginas 14, 17, 20, 21 y 25, a 1600 px
```

`make` requiere PDFLaTeX y los paquetes de la fuente. `make preview` requiere
Poppler (`pdftoppm`). Los PDF vectoriales están incluidos: la compilación no
requiere red, fuentes mayas/egipcias ni conversión SVG. Los cambios en imágenes
anidadas también invalidan el PDF gracias a las dependencias del Makefile.

Para regenerar los numerales mayas: `python3 scripts/generate_maya.py`
(requiere `rsvg-convert`). Para reconvertir un SVG egipcio o la estela:
`rsvg-convert -f pdf -o archivo.pdf archivo.svg`.

## Activos y créditos

- `images/maya_vector/`: 20 numerales esquemáticos originales CC0, SVG + PDF;
  `SOURCES.md` documenta convenciones y correspondencias Unicode.
- `images/egyptian/`: siete jeroglíficos, SVG + PDF, Otfried Lieberknecht /
  Wikimedia Commons, CC BY-SA 3.0. Mapeo y fuentes en `SOURCES.md`.
- `images/calendars/`: dibujo histórico de la Estela C de Quiriguá, atribuido
  a Maudslay, dominio público; SVG + PDF, `SOURCES.md` y metadatos de Commons.
- Los antiguos PNG `images/maya_unicode/` se conservan para evitar una
  eliminación innecesaria, **pero ya no se incluyen**: todos mostraban el
  mismo contenido, independientemente del valor.

No son fotografías generadas. El cero/concha y el ejemplo 13.0.0.0.0 se
identifican expresamente como esquemas; el dibujo de Quiriguá no es un calco
con correspondencia uno a uno con esos signos simplificados.

## Verificación — 2026-09-17

- `make rebuild`: éxito, dos pasadas, 28 páginas; `make` posterior confirma
  que la salida está al día.
- Log final: **cero** `Overfull`, `Underfull`, `Missing character`,
  `LaTeX Warning` o archivos no encontrados. Antes había 11 avisos de cajas
  desbordadas. Los ajustes adicionales fueron límites de altura, leyendas
  pequeñas y enlaces de texto corto, conservando las imágenes anteriores.
- `make preview`: páginas 14, 17, 20, 21 y 25 renderizadas desde el PDF final.
- Comprobación final independiente: páginas 14, 21 y 25 renderizadas de nuevo
  a 2000 px en `preview/final-check/`, con OCR Tesseract `.txt` por página.
- `pdftotext -bbox-layout`: ningún término fuera del papel en las cinco
  páginas afectadas (`preview/final-check/pdf-text.html`). Texto español,
  siete valores egipcios, veinte valores mayas y créditos presentes.
- Los 20 SVG mayas tienen hashes distintos; para 1–19 se verificó
  `5 × barras + puntos = valor`. El cero está dibujado mediante contornos
  de concha. Sin texto ni fuentes en las formas de los numerales.
- `pdfimages` en páginas 14, 21 y 25: ninguna imagen raster; se incorporaron
  los vectores. `pdffonts`: todas las fuentes de texto del PDF incrustadas.
- `git diff --check`: limpio. Cambios limitados a `Historia/`; sin push,
  despliegue ni commit.

**Límite de inspección visual:** se generaron y analizaron los PNG con OCR y
geometría; la herramienta disponible no permite al asistente abrir/ver esos
PNG directamente. No se afirma una revisión visual humana. Abrir sobre todo
`preview/final-check/slide-14.png` y `slide-21.png` para confirmar a simple
vista legibilidad de los jeroglíficos y detalle de la estela en proyección.
El OCR no lee los glifos antiguos; su valor se comprobó por fuente y vectores,
no interpretando las letras espurias que Tesseract produce sobre dibujos.

No se hizo una auditoría histórica completa del resto del texto preexistente.
