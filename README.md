# ORT — Material de Estudio

Repositorio personal de material universitario para la [Universidad ORT Uruguay](https://www.ort.edu.uy/).

## Carreras

### Ingenieria de Sistemas (en curso)

Carrera activa desde marzo 2026. Primer semestre:

| Curso | Carpeta |
|-------|---------|
| Algebra Lineal | `ingenieriaSistemas/1erSemestre/algebraLineal/` |
| Programacion 1 | `ingenieriaSistemas/1erSemestre/programacion1/` |
| Taller de Tecnologias 1 | `ingenieriaSistemas/1erSemestre/tallertecnologias1/` |

### Diploma en Inteligencia Artificial (completado)

Completado en 2025. Material de referencia:

| Curso | Carpeta |
|-------|---------|
| Inteligencia Artificial Generativa | `diplomaIA/InteligenciaArtificialGenerativa/` |
| Modelos de Deep Learning | `diplomaIA/ModelosDeDeepLearning/` |
| Taller de Deep Learning | `diplomaIA/TallerDeDeepLearning/` |

## Estructura de carpetas

```
ort/
├── ingenieriaSistemas/           # Carrera activa
│   └── 1erSemestre/
│       ├── algebraLineal/
│       │   ├── classes/          # Transcripciones + explicaciones por fecha
│       │   └── practicoMatrices/ # Ejercicios y soluciones
│       ├── programacion1/
│       │   └── classes/
│       └── tallertecnologias1/
│
├── diplomaIA/                    # Diploma completado (referencia)
│   ├── InteligenciaArtificialGenerativa/
│   │   ├── theory/              # Clases: transcripciones + explicaciones
│   │   ├── PARCIAL/             # Examenes y respuestas
│   │   └── workspace/           # Codigo de practicos y obligatorio
│   ├── ModelosDeDeepLearning/
│   │   ├── theory/
│   │   └── workspace/
│   └── TallerDeDeepLearning/
│       ├── theory/
│       └── workspace/
│
├── PATRONES_ESCRITURA.md         # Guia de estilo para explicaciones
├── CATALOGO_TIPOS_DOCUMENTO.md   # Templates por tipo de documento
└── VOZ_PROFESORES_REFERENCIA.md  # Perfiles de voz de profesores
```

## Contenido

- **Transcripciones** (`.txt`) — Transcripciones de clases grabadas
- **Explicaciones** (`.md`) — Resumen y explicacion de cada clase
- **Examenes** — Letras de parciales con respuestas
- **Codigo** (`.py`, `.ipynb`) — Practicos, obligatorios, y experimentos
- **Diagramas** — Flujos, arquitecturas, y mapas mentales
- **Material de referencia** — Ejercicios, guias, soluciones

## Que NO esta en el repositorio

Los siguientes archivos se excluyen via `.gitignore` por su tamaño:

- Datasets de ML (CIFAR-10, ImageNet, MNIST, FashionMNIST)
- Pesos de modelos entrenados (`.pth`, `.h5`, `.onnx`)
- Grabaciones de clase (`.mp4`)
- Logs de experimentos (WandB)
- Repositorios de terceros clonados como referencia

## Licencia

Este material se distribuye bajo [CC BY-NC-SA 4.0](LICENSE). Ver el archivo LICENSE para mas detalles.
