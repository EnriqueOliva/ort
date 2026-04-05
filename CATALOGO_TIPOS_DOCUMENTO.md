# Catalogo de Tipos de Documento — Sistema de Estudio Enrique

Este documento define TODOS los tipos de documento que se pueden generar para cualquier curso, con sus templates y reglas. Los tipos fueron desarrollados durante el diploma en IA y aplican a cualquier materia.

---

# INDICE DE TIPOS

| # | Tipo | Descripcion | Cuando Crearlo |
|---|------|-------------|---------------|
| 1 | Explicaciones de clase | Explicacion exhaustiva de una clase a partir de su transcripcion | Despues de cada clase |
| 2 | Checklist de temas | Tabla de auditoria: que se cubrio y que no | Despues de cada clase |
| 3 | Resumen completo de curso | Documento que cubre TODO el curso clase por clase | Al terminar el curso o antes del parcial |
| 4 | Complete Flows | Referencia rapida de un proceso/algoritmo/sistema end-to-end | Para cada proceso central del curso |
| 5 | Diccionario/Glosario | Definiciones rapidas de todos los terminos del curso | Incremental durante el curso |
| 6 | Diagramas HTML interactivos | Visualizaciones interactivas de conceptos complejos | Para temas con arquitecturas o flujos visuales |
| 7 | Mapas mentales | Visualizacion de todo el curso y conexiones entre temas | Al terminar el curso |
| 8 | Preguntas de parcial | Preguntas predichas o recopiladas para practicar | Antes de cada parcial |
| 9 | Respuestas de parcial | Respuestas en doble capa (corta + detallada) | Junto con las preguntas |
| 10 | Tutoriales de concepto | Explicacion profunda de UN concepto desde cero | Cuando un tema necesita mas profundidad |
| 11 | Reportes de obligatorio | Documentacion de proyectos/entregas con decisiones justificadas | Para cada entrega |
| 12 | Experiment logs | Registro de experimentos con hipotesis, config, resultados | Durante trabajo practico |
| 13 | Justificacion de decisiones | Cada decision tecnica justificada con evidencia | Para defensas orales |
| 14 | Perfil de voz del profesor | Analisis del habla y estilo del profesor para imitacion | Al inicio de cada curso |

---

# TIPO 1: EXPLICACIONES DE CLASE

El documento central del sistema. Una explicacion por clase.

## Template

```markdown
# Explicacion de Temas - Clase del DD-MM-YYYY: [Titulo del Tema]

## La Gran Pregunta: [Pregunta Retorica que Enmarca la Clase]

[Respuesta que establece el "por que" antes del "que". 2-4 oraciones.]

---

## Conexion con la Clase Anterior

[Puente explicito con material previo.]

---

## [Tema Principal 1]

### [Sub-concepto A]

> "Cita textual del profesor"

**Traduccion:** [Reformulacion en lenguaje simple]

[Explicacion extendida con analogia y ejemplo numerico si aplica.]

### [Sub-concepto B]
...

---

## [Tema Principal 2]
...

---

## Definiciones para el Parcial

**Termino 1:** Definicion de maximo 2 renglones.
**Termino 2:** Definicion de maximo 2 renglones.

---

## Posibles Preguntas para el Parcial

**Pregunta 1?**
Respuesta de maximo 2 renglones en lenguaje basico del estudiante.

**Pregunta 2?**
Respuesta...
```

## Reglas

- Apertura SIEMPRE con "La Gran Pregunta"
- Citas del profesor en blockquote, seguidas de **Traduccion:**
- Cada formula con traduccion simbolo por simbolo
- Analogias para cada concepto abstracto
- Cierre OBLIGATORIO con Definiciones + Preguntas del Parcial
- Solo negrita para enfasis (nunca italica)
- Horizontal rules entre secciones mayores
- Nada de lo que dijo el profesor se omite

---

# TIPO 2: CHECKLIST DE TEMAS

Auditoria rapida de que se cubrio en cada clase.

## Template

```markdown
# Temas de la clase DD-MM-YYYY

| **Tema** | **Desarrollado en clase** |
|----------|---------------------------|
| **[Tema Mayor]** | [checkmark] **Si** - [Anotacion breve] |
| * [Sub-tema] | [checkmark] **Si** - [Anotacion breve] |
| * [Sub-tema] | [warning] **Parcial** - Solo mencionado |
| **[Tema Mayor 2]** | [X] **No desarrollado** |
```

## Reglas

- Una sola tabla Markdown, sin prosa
- Status: Checkmark Si / Warning Parcial|Mencionado|Asignado / X No desarrollado
- Temas mayores en negrita, sub-temas con bullet `*`
- Documento puramente de tracking — cero explicaciones

---

# TIPO 3: RESUMEN COMPLETO DE CURSO

Dos variantes posibles:

## Variante A: Enciclopedica

- Organizacion cronologica clase-por-clase
- Maximo detalle: codigo, formulas, ejercicios
- Diccionario alfabetico A-Z al final
- Guia de estudio con checklists
- 1000+ lineas

## Variante B: Narrativa

- Organizacion tematica por "Partes" y "Capitulos"
- Detalle moderado: conceptos, citas, poco codigo
- Gran pregunta como apertura
- Seccion final "Sintesis y Conexiones" unificando todo
- Tabla comparativa de conceptos centrales
- ~500 lineas

---

# TIPO 4: COMPLETE FLOWS

Referencia rapida de un proceso/algoritmo/sistema. Formato tipo "cheat sheet" mecanico.

## Template

```markdown
# [NOMBRE] - Flujo Completo

## Que es

[1-2 oraciones. Cero tecnicismos. Que HACE este proceso/sistema/algoritmo.]

---

## FLUJO [PRINCIPAL / DE EJECUCION / DE PROCESAMIENTO]

**Entrada:** [Tipo de dato/input]
**Salida:** [Tipo de resultado]

```
1. [VERBO IMPERATIVO] una accion
   - Explicacion de por que (1-2 lineas)
2. [VERBO IMPERATIVO] siguiente accion
   - Explicacion
   ...
```

---

## Diagrama

```
[ASCII art del flujo de datos con flechas -->]
```

---

## Por que funciona / Puntos clave

### [Pregunta "por que" 1]
[Respuesta concisa]
```

## Reglas

- SIN formulas matematicas — solo nombres de variables/conceptos
- SIN citas del profesor — voz de par que escribe cheat sheet
- SIN analogias — mecanismo puro
- Entrada/Salida explicita
- Pasos numerados en code block = que haces
- Indentaciones con guion = por que lo haces
- Diagrama ASCII despues de los pasos

---

# TIPO 5: DICCIONARIO/GLOSARIO

## Template por Entrada

```markdown
### [Termino] ([Alias / Nombre alternativo])

[Definicion en lenguaje llano, 1-3 oraciones]

**Para que sirve:** [Proposito funcional]
**Cuando aparece en el curso:** [Contextos especificos]
**Formula:** `[si aplica, en code block]`
```

## Reglas

- Organizado por categoria tematica
- Cada entrada sigue el template exacto
- Tabla de referencia cruzada al final mostrando que terminos aparecen en que temas/modulos

---

# TIPO 6: DIAGRAMAS HTML INTERACTIVOS

## Estructura Pedagogica

1. Definicion simple como pregunta: "Que es X?"
2. Bullet list con labels en negrita como unidad explicativa core
3. Diagrama SVG/Canvas interactivo
4. Tabla de comparacion para A vs B
5. Bloque de codigo con implementacion (si aplica)
6. Warning boxes para problemas practicos
7. Resumen con cards

## Convenciones Visuales

- Cards con borde izquierdo de color segun tipo (azul=formula, amarillo=ejemplo, rojo=warning, verde=exito)
- Hover-to-elevate en cards
- Monospace para formulas, separacion visual de la prosa
- Background gradiente unico por archivo (identidad tematica)
- Autocontenido: todo CSS y JS inline, cero dependencias externas

---

# TIPO 8: PREGUNTAS Y RESPUESTAS DE PARCIAL

## Preguntas

```markdown
# Preguntas de Repaso - [Curso] [Periodo]

## Tema 1: [Nombre]

1. [Pregunta conceptual/definitional]
2. [Pregunta de interpretacion de formula]
3. [Pregunta de aplicacion/pseudocodigo]
4. [Pregunta comparativa]
```

## Respuestas (Doble Capa)

```markdown
### Pregunta N

> **Respuesta corta (para el parcial):**
> [2-4 lineas densas con terminologia precisa]

**Explicacion detallada:**

[Citas del profesor, formulas, ejemplos, tablas comparativas]
```

## Respuestas Cortas (Solo para repaso rapido)

```markdown
> [Solo la respuesta del blockquote, sin explicacion extendida]
```

---

# TIPO 10: TUTORIALES DE CONCEPTO

Para cuando un tema necesita explicacion mas profunda que la clase.

## Template

```markdown
# [CONCEPTO] - Explicado Desde Cero

[Encuadre: "Te voy a explicar que es X como si nunca hubieras visto esto."]

---

## NIVEL 1: [Fundamento mas basico]

[Definiciones elementales con numeros concretos, cero simbolos]

## NIVEL 2: [Siguiente capa]

[Variables nombradas, primer formula simple]

...

## NIVEL N: [Aplicacion / Comparacion]

[Cuando usar, comparacion con alternativas]

---

## Resumen

[Tabla o bullets de takeaways]
```

## Reglas

- Auto-contenido: un archivo, un concepto
- Progresion explicita de NIVEL 1 a N
- Numeros concretos antes que simbolos
- Analogias como herramienta principal
- Definicion de CADA termino, incluso los "obvios"
- Sub-headers como preguntas: "Que es X?", "Para que sirve?", "Por que?"
- Glossarios al final

---

# TIPO 11: REPORTES DE OBLIGATORIO/ENTREGA

```markdown
# [Titulo del Proyecto]

## Contexto
[Problema, dataset, restricciones]

## Decisiones
[Cada decision con: alternativas, evidencia, tabla de resultados, decision final + razon]

## Resultados
| Metrica | Valor |

## Debilidades / Analisis de Errores
[Honesto, con ejemplos especificos]

## Conclusiones
```

---

# TIPO 12: EXPERIMENT LOG

```markdown
# [Tarea] - Experiment Log

## Version 1: [Nombre descriptivo] [emoji status]
**Date:** YYYY-MM-DD
**Story:** [Narrativa del razonamiento]
**Config:** [Valores exactos]
**Justification:** [Por que estos valores]
**Result:** [Metricas]
**Analysis:** [Observaciones candidas, incluyendo sorpresas y fallos]

## Version 2: [...]
```

## Reglas

- Cambio de UNA variable por vez
- Admision honesta de fallos
- Comparacion explicita con version anterior
- Recomendaciones del profesor tratadas como hipotesis testeables

---

# TIPO 13: JUSTIFICACION DE DECISIONES

Cada decision tecnica se justifica con hasta 4 pilares:

1. **Literatura/referencia** — Cita del paper, libro, o documentacion oficial
2. **Instrucciones del profesor** — Cita textual de clase
3. **Evidencia experimental** — Tabla de resultados comparativos
4. **Justificacion teorica** — Razonamiento o investigacion externa

```markdown
### Decision: [Nombre]

**Problema:** [Que desafio resuelve]
**Alternativas consideradas:**
- [Opcion A]: [Pro/con]
- [Opcion B]: [Pro/con]
**Evidencia:**
| Config | Resultado | Cambio |
**Decision:** [Opcion elegida] porque [razon]
```

---

# TIPO 14: PERFIL DE VOZ DEL PROFESOR

Para CADA profesor nuevo, crear un perfil que capture su estilo para poder imitarlo.

## Template

```markdown
# Perfil de Voz - [Nombre del Profesor] — [Curso]

## Personalidad General
[2-3 oraciones describiendo su estilo comunicativo]

## Muletillas y Marcadores Discursivos (Orden de Frecuencia)
1. **"[muletilla]"** — [como la usa, ejemplo verbatim]
2. ...

## Frases Firma
| Frase | Significado/Uso | Ejemplo Verbatim |
|-------|----------------|------------------|

## Como Introduce Temas
[Patrones observados]

## Como Explica Conceptos Complejos
[Usa analogias? Ejemplos? Derivaciones? Codigo? Historias?]

## Analogias Recurrentes
| Analogia | Concepto | Cita |
|----------|---------|------|

## Vocabulario Regional / Coloquialismos
[Voseo, lunfardo, expresiones propias]

## Como Maneja Preguntas
[Paciente? Socratico? Redirige?]

## Tono General
[Formal? Informal? Mix? Humor?]
```

## Regla
Capturar al menos 10 frases verbatim por clase para tener suficiente material.

---

# REGLAS TRANSVERSALES PARA TODOS LOS TIPOS

1. **Idioma de prosa**: Espanol
2. **Idioma de codigo**: Ingles para variables/funciones, espanol para prints/logs
3. **Formulas**: En code blocks, nunca LaTeX
4. **Enfasis**: Solo negrita, nunca italica
5. **Separadores**: Horizontal rules entre secciones
6. **Emojis**: Solo en checklists, no en contenido explicativo
7. **Footer**: "Documento generado mediante analisis exhaustivo (3 pasadas) de la transcripcion de la clase..."
8. **Sin comentarios en codigo**: El codigo se explica afuera
9. **Principio "menos es mas"** para notebooks y entregas
10. **Nombres de variables completos**: Nunca abreviar
