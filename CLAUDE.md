# Sistema de Estudio — Enrique (ORT Uruguay)

Workspace de materiales universitarios. Enrique viene de Relaciones Internacionales, completo un Diploma en IA (2025), y ahora cursa Ingenieria en Sistemas (desde marzo 2026). Asumir perspectiva de principiante en matematica y CS.

Workflow principal: Enrique entrega transcripciones de clase y pide explicaciones, resumenes, diagramas, material de parcial, etc. Cero ceremonia — simplemente hablar y producir.

## Principios

1. **Maxima simplicidad** — Explicar de la manera mas sencilla posible sin sacrificar precision
2. **Fidelidad a la fuente** — Solo lo que dijo el profesor; nada inventado
3. **Perspectiva de principiante** — Asumir que no asisti a clase y puedo no dominar el tema
4. **Cobertura exhaustiva** — Todo lo que dijo el profesor queda capturado, incluyendo logistica y tangentes
5. **Asociacion por fecha** — Archivos organizados y nombrados por fecha de clase

## Reglas de Formato

- Formulas en **LaTeX** (`$...$` inline, `$$...$$` bloques) — nunca code blocks para matematica
- Traducir cada simbolo de cada formula inmediatamente despues de presentarla
- Una analogia concreta por cada concepto abstracto
- Un ejemplo numerico por cada formula o proceso
- Tablas para toda comparacion A vs B
- Codigo explicado linea por linea fuera del bloque de codigo, no con comentarios inline
- Registro semi-informal en espanol; terminos tecnicos en ingles sin traducir cuando son estandar
- Citas del profesor preservan su registro original (voseo, lunfardo, coloquialismos)

## Propagacion de Estilo

Antes de generar una nueva explicacion, leer la PRIMERA explicacion aprobada de ese curso. Igualar su nivel de detalle, estructura de headings, y tono. Cada curso tiene su propia voz.

## Perfil de Voz del Profesor (Automatico)

Antes de generar una explicacion de clase:
1. Buscar `voz-profesor.md` en la carpeta del curso
2. Si EXISTE: leerlo antes de procesar la transcripcion
3. Si NO EXISTE: despues de generar la explicacion, crear el archivo con muletillas, frases firma, estilo de explicacion, vocabulario regional. Minimo 10 citas verbatim.
4. Si EXISTE: despues de generar, agregar nuevos patrones observados

## Baseline de Profesores Uruguayos (ORT)

Patrones compartidos a esperar en cualquier profesor nuevo:
- Voseo universal ("vos tenes", "vos podes")
- "Capaz que" en vez de "quizas"; "este" como muletilla dominante
- Diminutivos para suavizar contenido tecnico
- Tono informal-academico: rigor intelectual + coloquialismo
- Mezcla ingles/espanol para terminos tecnicos

## Tipos de Documento

| Tipo | Cuando | Skill |
|------|--------|-------|
| Explicacion de clase | Despues de cada clase, a partir de transcripcion | explicar-clase |
| Checklist de temas | Auditoria rapida de que se cubrio | explicar-clase |
| Preguntas/respuestas de parcial | Antes de cada examen | preparar-parcial |
| Diagrama interactivo / Complete Flow | Para conceptos visuales o procesos | diagrama-interactivo |
| Tutorial de concepto | Cuando un tema necesita mas profundidad | explicar-clase |
| Perfil de voz del profesor | Al inicio de cada curso nuevo | perfil-profesor |
| Version imprimible (PDF A4 B&W) | Cuando se necesita copia fisica | imprimir |

## Impresion

Para generar PDFs imprimibles: `node utils/print/build.js <archivo.md>`. CSS optimizado para A4, blanco y negro, tipografia grande, maxima legibilidad. KaTeX renderiza las formulas LaTeX automaticamente.

## Estructura de Carpetas

```
ort/
  [carrera]/
    [semestre]/
      [curso]/
        voz-profesor.md          — Perfil de voz del profesor
        classes/ o theory/
          [fecha]/
            [fecha].txt          — Transcripcion
            [fecha]-explicacion.md — Explicacion generada
        PARCIAL/
          preguntas.md
          respuestas.md
  utils/
    print/                       — Sistema de impresion (build.js + CSS)
```
