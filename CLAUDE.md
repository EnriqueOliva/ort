# Sistema de Estudio — Enrique (ORT Uruguay)

Este workspace contiene materiales de estudio universitario. Cada subcarpeta es una carrera o diploma, con cursos organizados por semestre.

## Documentos de Referencia (LEER cuando se genere contenido)

Antes de generar explicaciones, resumenes, o material de estudio, consultar estos archivos para seguir los patrones establecidos:

- `ort/PATRONES_ESCRITURA.md` — Como escribir explicaciones (tecnicas, formato, matematica, analogias, meta-reglas)
- `ort/CATALOGO_TIPOS_DOCUMENTO.md` — Templates para cada tipo de documento (explicaciones, checklists, flows, parciales, tutoriales, etc.)
- `ort/VOZ_PROFESORES_REFERENCIA.md` — Ejemplos de analisis de voz de profesores + template para nuevos profesores

## Principios Fundamentales

1. **Maxima simplicidad** — Explica de la manera mas sencilla posible
2. **Fidelidad a la fuente** — Solo lo que dijo el profesor, nada inventado
3. **Perspectiva de principiante** — Asumir que no asisti a clase y puedo no dominar el tema
4. **Cobertura exhaustiva** — Nada de lo que dijo el profesor se omite
5. **Asociacion por fecha** — Archivos organizados y nombrados por fecha de clase

## Reglas de Escritura (Resumen Rapido)

### Estructura de Explicaciones de Clase

Siempre usar esta estructura:
- Abrir con **"La Gran Pregunta"** — pregunta retorica que enmarca la clase
- **Conexion con clase anterior** — puente explicito
- Por cada tema: **cita del profesor en blockquote** -> **Traduccion:** en negrita -> explicacion extendida
- Cerrar con **Definiciones para el Parcial** (max 2 renglones cada una) y **Posibles Preguntas para el Parcial** (con respuestas cortas)

### Formato

- **Negrita** para enfasis — NUNCA italica
- Formulas en **code blocks** (no LaTeX), seguidas de traduccion simbolo por simbolo
- **Horizontal rules** (`---`) entre secciones mayores
- **Tablas** para toda comparacion A vs B
- **Diagramas ASCII** para flujos y arquitecturas
- Sin emojis en contenido explicativo (solo en checklists de auditoria)
- Sin comentarios en codigo — explicar afuera

### Matematica

Siempre: numeros concretos primero -> variables nombradas -> formula general -> "por que importa". Toda formula recibe traduccion inmediata de cada simbolo.

### Citas del Profesor

Siempre en blockquote Markdown, preservando su registro original (voseo, lunfardo, coloquialismos). Seguidas de **Traduccion:** con reformulacion simple.

### Idioma

- Prosa en espanol
- Terminos tecnicos en ingles sin traducir cuando son estandar
- Codigo: variables en ingles, prints/logs en espanol
- Registro semi-informal, tono de "estudiante mayor explicando a otro"

## Protocolo de Generacion

1. **Triple pasada** — Leer la transcripcion 3 veces antes de producir output
2. **Propagacion de estilo** — Igualar la primera explicacion aprobada del curso
3. **Analogias obligatorias** — Cada concepto abstracto recibe al menos una analogia concreta
4. **Ejemplo numerico obligatorio** — Cada formula/proceso recibe un ejemplo con numeros reales

## Tipos de Documento Disponibles

Referencia completa en `CATALOGO_TIPOS_DOCUMENTO.md`. Los mas frecuentes:

| Tipo | Cuando |
|------|--------|
| Explicacion de clase | Despues de cada clase, a partir de transcripcion |
| Checklist de temas | Auditoria rapida de que se cubrio |
| Preguntas/respuestas de parcial | Antes de cada examen |
| Tutorial de concepto | Cuando un tema necesita mas profundidad |
| Perfil de voz del profesor | Al inicio de cada curso nuevo |
| Complete Flow | Para cada proceso/algoritmo central |
| Glosario | Incremental durante el curso |

## Perfiles de Profesores

Para cada profesor nuevo, crear un perfil de voz siguiendo el template en `VOZ_PROFESORES_REFERENCIA.md`. Capturar: muletillas, frases firma, como introduce temas, como explica, analogias, vocabulario regional, tono. Al menos 10 citas verbatim por clase analizada.

## Estructura de Carpetas Esperada

```
ort/
  [carrera]/
    [semestre]/
      [curso]/
        theory/
          [N-DD-MM-YYYY]/
            [fecha].txt          — Transcripcion
            explicaciones.md     — Explicacion generada
            [fecha].md           — Checklist de temas
        PARCIAL/
          preguntas.md
          respuestas.md
        CLAUDE.md                — Instrucciones especificas del curso (si las hay)
```
