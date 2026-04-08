# ORT — Material de Estudio

Repositorio personal de material universitario para la [Universidad ORT Uruguay](https://www.ort.edu.uy/).

## Carreras

### Ingenieria de Sistemas (en curso)

Carrera activa desde marzo 2026. Primer semestre:

| Curso | Profesor | Carpeta |
|-------|----------|---------|
| Algebra Lineal | Gabriel Cisneros | `ingenieriaSistemas/1erSemestre/algebraLineal/` |
| Programacion 1 | Gonzalo Wagner | `ingenieriaSistemas/1erSemestre/programacion1/` |
| Taller de Tecnologias 1 | Por confirmar | `ingenieriaSistemas/1erSemestre/tallertecnologias1/` |

### Diploma en Inteligencia Artificial (completado 2025)

Material de referencia. Incluye transcripciones, explicaciones, examenes, y codigo de practicos/obligatorios.

| Curso | Profesor | Carpeta |
|-------|----------|---------|
| Inteligencia Artificial Generativa | Fran | `diplomaIA/InteligenciaArtificialGenerativa/` |
| Modelos de Deep Learning | Matias Carrasco | `diplomaIA/ModelosDeDeepLearning/` |
| Taller de Deep Learning | Jo Vina | `diplomaIA/TallerDeDeepLearning/` |

## Estructura de carpetas

```
ort/
├── ingenieriaSistemas/                 # Carrera activa
│   └── 1erSemestre/
│       ├── algebraLineal/
│       │   ├── theory/
│       │   │   ├── clasesVideos/       # Grabaciones comprimidas por fecha
│       │   │   ├── classesMaterial/    # Explicaciones por fecha
│       │   │   └── classesTranscripts/ # Transcripciones por fecha
│       │   └── practicos/             # Ejercicios y soluciones
│       ├── programacion1/
│       │   └── theory/
│       │       ├── clasesVideos/
│       │       ├── classesMaterial/
│       │       └── classesTranscripts/
│       └── tallertecnologias1/
│
├── diplomaIA/                          # Diploma completado (referencia)
│   ├── InteligenciaArtificialGenerativa/
│   ├── ModelosDeDeepLearning/
│   └── TallerDeDeepLearning/
│
└── utils/                              # Herramientas
    ├── print/                          # MD -> PDF (A4, B&W, KaTeX)
    └── video-compressor/               # Comprimir videos para GitHub
```

## Contenido por tipo

| Tipo | Formato | Descripcion |
|------|---------|-------------|
| Transcripciones | `.txt` | Transcripciones automaticas de clases grabadas |
| Explicaciones | `.md` | Resumen y explicacion exhaustiva de cada clase |
| Videos | `.mp4` | Grabaciones comprimidas (<95MB por parte) |
| Examenes | `.md` + `.jpg` | Letras de parciales con respuestas |
| Codigo | `.py`, `.ipynb` | Practicos, obligatorios, y experimentos |
| Ejercicios | `.jpg`, `.md`, `.pdf` | Practicos escaneados con soluciones |
| Diagramas | `.html`, `.md` | Flujos, arquitecturas, y mapas mentales |

## Herramientas

### Imprimir a PDF

Convierte archivos Markdown a PDF A4 optimizado para impresion en blanco y negro. Renderiza formulas LaTeX via KaTeX. Tipografia grande y clara, pensada para consulta rapida durante evaluaciones.

```bash
node utils/print/build.js <archivo.md>
```

Requiere: Node.js. Instalar dependencias con `cd utils/print && npm install`.

### Comprimir videos

Comprime grabaciones de clase (1080p) a 480p/10fps H.265 y auto-divide en partes menores a 95MB para poder subirlas a GitHub.

```bash
python utils/video-compressor/compress.py [--output DIR] <video.mp4> [video2.mp4 ...]
```

Requiere: Python 3, ffmpeg en PATH.

## Convenciones de nombres

- Carpetas de fecha: `DD-mmm-YYYY` (ej: `17-mar-2026`)
- Transcripciones: `DD-mmm-YYYY.txt`
- Explicaciones: `DD-mmm-YYYY-explicacion.md` o `explicaciones.md` (segun el curso)
- Videos: `DD-mmm-YYYY.mp4` o `DD-mmm-YYYY-partN.mp4` si fue dividido

## Licencia

[CC BY-NC-SA 4.0](LICENSE) — Atribucion, no comercial, compartir igual.
