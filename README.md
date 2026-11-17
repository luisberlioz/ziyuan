## PrograMate2
* Gradient Descent Visualizer: https://ajithpinninti.github.io/gradient-descent-visualizer/

## Discreta

## MM112

## Análisis Funcional
* Material del curso (bioinformática — Institut Pasteur / HUB): https://gitlab.pasteur.fr/hub/functional_analysis_unah

### Traducción del material del curso

#### 1. Anotación de datos OMICS crudos — `Annotation_OMICS_v.1.Rmd`
*¿Qué cambia entre los organismos no modelo y los modelo?* — "Becoming fluent in OMICs, 2026"

Supongamos que recibes del servicio de secuenciación los resultados de RNA-Seq (o de proteómica) de tu experimento. Tienes una tabla con la expresión génica (o proteica) cruda, con identificadores como `"ERDMAN_0001"`, `"ENSG00000012048"`, `"P60710"`. Son identificadores de gen/proteína (IDs, locus tags, IDs de proteína), **no** nombres de gen (aka símbolos) como `dnaA` o `BRCA1`, y no se interpretan biológicamente sin esfuerzo.

En esta sesión se presentan dos maneras de **anotar** (= traducir) esos identificadores a información génica más significativa:

1. **Parte 1 — Anotación manual:** emparejar los IDs contra una tabla existente con anotación de Gene Ontology.
2. **Parte 2 — Anotación programática en R:** usar paquetes de R para obtener la anotación desde una base de datos pública.

Ambas habilidades se usan a diario en pipelines de bioinformática reales.

**Parte 1: Anotación manual de un organismo no modelo** — *Mycobacterium tuberculosis*, con tres condiciones de crecimiento: **FR** (medio rico completo), **CR** (restringido en carbono) y **HR** (restringido en hipoxia). En esta parte vas a:

1. Cargar y explorar la matriz cruda de conteos.
2. Identificar los identificadores génicos usados en la matriz de conteos.
3. Cargar una tabla de anotación del genoma desde una base pública (BV-BRC) seleccionando las columnas informativas (funciones GO, otros identificadores, etc.).
4. Fusionar esa tabla con la matriz de conteos para recuperar nombres de gen y términos GO.
5. Explorar los términos GO presentes en la matriz de conteos.

**Gene Ontology (GO)** es la mayor fuente de información sobre las funciones de los *genes*. Ese conocimiento es legible por humanos y por máquinas a la vez, y es la base del análisis computacional de experimentos de biología molecular y genética a gran escala.

- **Paso 1.1** — Cargar e inspeccionar la matriz de conteos. **Q1: ¿Cuántos genes y muestras hay en esta tabla?**
- **Paso 1.2** — Cargar la tabla de anotación del genoma desde **BV-BRC** (antes PATRIC). Contiene información sobre cada gen anotado del genoma: locus tag, símbolo del gen, descripción del producto proteico y términos GO. **Q2: ¿Qué columnas dan el 1) nombre del gen, la 2) descripción del gen y la 3) función del gen? ¿Qué columna se usa para combinar la tabla de conteos original con esta información adicional?**
- **Paso 1.3** — Preparar la tabla de anotación: el archivo tiene muchas columnas que aquí no hacen falta; se extraen solo las relevantes para la anotación y se fusionan las dos tablas. **Q4: ¿Qué tan bien anotado está este organismo?** En los organismos modelo la gran mayoría de los genes tienen nombre y función; en *M. tuberculosis* muchos marcos de lectura siguen sin caracterizar — por eso las bases de anotación como BV-BRC son tan valiosas, y por eso la cobertura GO es incompleta incluso para patógenos importantes.
- **Paso 1.4** — Fusionar la matriz de conteos con la anotación. Ambas tablas comparten un identificador (el locus tag) que permite unirlas; la unión se hace sobre ese identificador génico.
- **Paso 1.5** — Inspección de los términos GO. La pregunta más común en anotación funcional: *"¿cuáles de mis genes participan en el proceso X?"* **Q5: ¿Qué tan relevantes son estos términos para entender la función del gen al que se asocian?**
- **Paso 1.6** — (Opcional) Colorear las anotaciones por categoría GO (Proceso Biológico / Función Molecular / Componente Celular) con el paquete `GO.db` — los IDs de GO no revelan su categoría por sí solos. **Q6: ¿Qué representan los NAs?**
- **Paso 1.7** — (Opcional) Anotar tu propio organismo: busca una base de datos con anotaciones para tu organismo y produce una tabla con la información correspondiente.

**Parte 2: Anotación de un organismo modelo con rutas KEGG** (ratón). En esta parte vas a:

1. Cargar y explorar la matriz cruda de conteos.
2. Identificar los identificadores usados en la matriz de conteos.
3. Explorar la anotación del genoma de este organismo.
4. Fusionar la tabla de anotación con la matriz de conteos para recuperar nombres de gen y rutas KEGG.
5. Explorar las rutas KEGG y visualizar los genes más altamente expresados.

**KEGG** es un recurso de bases de datos para entender las funciones y utilidades de alto nivel del sistema biológico (la célula, el organismo y el ecosistema) a partir de información a nivel molecular, en especial de conjuntos de datos moleculares a gran escala generados por secuenciación del genoma y otras tecnologías experimentales de alto rendimiento. Para encontrar rutas KEGG se usa el paquete R `msigdbr`, que provee todas las colecciones de conjuntos de genes de la *Molecular Signatures Database* (MSigDB) del Broad Institute. *Nota:* si trabajas con organismos no modelo, puedes usar el paquete R `KEGGREST` para acceder a la base KEGG y obtener la anotación de tu organismo específico.

- **Paso 2.1** — Cargar e inspeccionar la matriz de conteos. **Q1: ¿Cuántas proteínas y muestras hay en esta tabla?**
- **Paso 2.2** — Explorar la anotación con `org.Mm.eg.db`. Los nombres de fila son **Uniprot IDs** (p. ej. `P60710`) y hay que traducirlos a símbolos de gen y Entrez IDs para el análisis de rutas. A diferencia de la Parte 1 (donde se descargó una tabla de anotación y se fusionó a mano con la matriz de conteos), aquí se usa el paquete R `org.Mm.eg.db` — una base de datos del genoma del ratón que traduce automáticamente entre los distintos identificadores — con la función `select()` de `AnnotationDbi`.
- **Paso 2.3** — Traducir UniprotID → ENTREZID → Símbolo del gen. *Nota:* los IDs específicos de isoforma (p. ej. `P12345-2`, `Q8BZ98-3`) no están en la base de datos; algunas proteínas tendrán `NA` en ENTREZ y SYMBOL, lo que significa que no están anotadas con un identificador génico válido. **Q2: ¿Cuántas proteínas NO pudieron mapearse a un símbolo? ¿Te parece aceptable ese número para continuar con el análisis posterior?**
- **Paso 2.4** — Recuperar las rutas KEGG con el paquete `KEGGREST`, que da acceso a la *Kyoto Encyclopedia of Genes and Genomes*: descarga la versión vigente de KEGG y da acceso a ~11 mil organismos con anotación KEGG. **Q3: ¿Cuáles son las tres rutas con mayor número de genes? ¿Son las tres suficientemente informativas sobre las funciones moleculares de sus genes? Q4: ¿Puedes encontrar rutas *directamente* asociadas a la inflamación? Q5: ¿Qué tan bien anotado está este organismo?** ¿Qué porcentaje de los genes de tu conjunto de datos tiene un identificador génico *válido*? ¿Qué porcentaje está asociado a al menos una ruta KEGG?

#### 2. Transcriptómica funcional — `Functional_Transcriptomics_v2.Rmd`
*GSEA con rutas KEGG usando `clusterProfiler` — Transcriptómica*

Datos de expresión génica de un estudio sobre enfermedad inflamatoria intestinal realizado en un modelo murino de colitis crónica, comparando dos condiciones: **CAP** (administración de capsaicina) y **DSS** (solvente control), en 3 puntos de tiempo.

*Datos del artículo:* Chen, K., Shen, S., Chen, Y. et al. *A proteomic and RNA-seq transcriptomic dataset of capsaicin-aggravated mouse chronic colitis model.* Sci Data 9, 549 (2022). <https://doi.org/10.1038/s41597-022-01637-3> — Acceso a los datos: <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE198304>

GSEA en `clusterProfiler` necesita un **vector numérico con nombres** de estadísticas (usualmente logFC o estadístico t), **ordenado de mayor a menor**, cuyos nombres sean *IDs génicos en un tipo de clave soportado por KEGG* (comúnmente Entrez IDs).

**Cuando la API de KEGG no es accesible:** en algunos servidores o entornos de nube el acceso directo a la API REST de KEGG falla (por ejemplo, devuelve 403 Forbidden); entonces `enrichKEGG()` y `gseKEGG()` fallan antes de que empiece el análisis, solo porque los datos de anotación no se pueden descargar en línea. El rodeo práctico es construir la anotación de KEGG en otra máquina con acceso normal a KEGG, guardarla localmente y reutilizarla en el servidor de destino. Es también una forma cómoda de **congelar la versión de KEGG** usada en un análisis, lo que ayuda a la reproducibilidad:

```r
kk_gson <- gson_KEGG("hsa")
saveRDS(kk_gson, file = paste0(WDIR,"practicals/results/kegg_hsa_gson.rds"))
kk_gson <- readRDS("kegg_hsa_gson.rds")
kk2 <- gseKEGG(geneList = geneList, organism = kk_gson)
```

Este enfoque es útil cuando el servidor de análisis tiene acceso de red inestable, cuando la API de KEGG no está disponible temporalmente, o cuando se quiere congelar la versión exacta de KEGG para reproducir el análisis más tarde.

El objeto GSON también se convierte a data frame para producir una tabla legible de todas las rutas (con el ID de ruta, su nombre y el número de genes de la ruta). Gráficos incluidos: **Enrichment Map**, **Treeplot** y **Ridgeline plot** (ridgeplot), más la comparación de rutas enriquecidas entre todas las condiciones.

#### 3. Proteómica funcional — `Functional_Proteomics_v2.Rmd`
*GSEA con rutas KEGG usando `clusterProfiler` — Proteómica*

Datos de expresión del proteoma de un estudio sobre enfermedad inflamatoria intestinal en *Mus musculus* (tejidos intestinales de ratones con colitis crónica), comparando dos condiciones de alimentación: **CAP** (administración de capsaicina) y **DSS** (solvente control).

*Datos del artículo:* el mismo Chen et al., Sci Data 9, 549 (2022) — Acceso a los datos: GSE198304.

El flujo es el mismo que en transcriptómica, con dos diferencias: la base KEGG se construye para el organismo **`mmu`** (ratón) en lugar de `hsa`, y se agrega como primera capa la **visualización del enriquecimiento con dotplots** (`dotplots`), además de los gráficos de pathways adicionales: **Enrichment Map** (con la similitud calculada por *gene-overlap* en KEGG y un número de categorías a mostrar) y **Treeplot** / **Ridgeline plot**.

#### Datos incluidos en el repositorio

| Ruta | Contenido |
|---|---|
| `data/myct_data/` | `counts_raw_myct.csv` (conteos crudos de *M. tuberculosis*), `GO_annotation_myct.txt` |
| `data/musm_data/` | `counts_musm.csv` (conteos de *Mus musculus*) |
| `data/mice/GEO/` | GSE198304: conteos y FPKM (`.txt` y `.txt.gz`), `target.csv` |
| `data/mice/PRIDE/PXD032186/` | `original_data.csv`, `hypothesis_limma_data.csv`, `peptide_groups.xlsx`, `protein_groups.xlsx`, `proteins.xlsx`, `PSMs.xlsx`, `README` |
| `data/experimentalDesignTemplate-celllines.txt` | plantilla de diseño experimental para líneas celulares |
| `results/` | `kegg_hsa_gson.rds`, `kegg_mmu_gson.rds`, `kegg_mmu_gsea_proteomics.rds` |
