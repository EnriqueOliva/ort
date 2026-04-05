# Guia de Patrones de Escritura y Explicacion — Sistema de Estudio Enrique

Este documento define COMO se deben escribir explicaciones, resumenes, y materiales de estudio para cualquier curso. Los patrones fueron extraidos del diploma en IA pero son aplicables a cualquier materia de ingenieria en sistemas o posgrado.

---

# 1. PRINCIPIOS FUNDACIONALES

Toda generacion de contenido debe respetar estos principios:

1. **Maxima simplicidad**: Explica de la manera mas sencilla posible, sin sacrificar precision.
2. **Fidelidad a la fuente**: Explica UNICAMENTE los temas dados en la clase/transcripcion. No inventar ni agregar contenido externo.
3. **Perspectiva de principiante**: Asumir que el lector no asistio a clase y puede no dominar el tema. Explicar hasta lo mas basico si es necesario.
4. **Cobertura exhaustiva**: Todo lo que dijo el profesor debe quedar capturado. Nada se omite.
5. **Asociacion por fecha**: Todos los archivos de una clase se nombran y organizan por fecha.

La **persona** del lector: un estudiante que no asistio a esa clase y necesita entender todo lo que se dicto a partir del material escrito.

---

# 2. PROTOCOLO DE GENERACION

## Triple Pasada
Antes de producir output, el material fuente (transcripcion, slides, etc.) se lee 3 veces completas en busca de detalles omitidos. Solo al final se produce el documento.

## Propagacion de Estilo
La primera explicacion aprobada para un curso se convierte en el "template". Todas las clases subsiguientes deben igualar ese nivel de detalle y estilo.

## Ultrathink
Los prompts de generacion terminan con "Ultrathink" para maxima profundidad de analisis.

---

# 3. TECNICAS DE EXPLICACION

## 3.1 El Patron "Cita-Traduccion"

La tecnica mas importante. Se usa 10-25 veces por archivo de explicacion:

1. Cita textual del profesor en blockquote (`>`)
2. Etiqueta en negrita: **Traduccion:** / **Traduccion simple:** / **En espanol:**
3. Reformulacion en lenguaje llano

```markdown
> "Cita textual del profesor con su jerga y estilo propio"

**Traduccion:** Reformulacion en lenguaje simple que cualquiera puede entender.
```

Variaciones de la etiqueta:
- **Traduccion:** (mas comun, para jerga tecnica)
- **Traduccion simple:** (para pasajes particularmente densos)
- **En espanol:** (para formulas o notacion matematica)
- **Que significa esto? Vamos por partes:** (para definiciones formales complejas)

## 3.2 El Patron "Palabra Aterradora, Significado Simple"

Desmitificar terminos tecnicos explicitamente:

```markdown
"'[Termino complejo]' suena complicado pero es simple: significa [definicion en una oracion]."
"**[Termino] = [sinonimo cotidiano], [sinonimo cotidiano 2]**"
```

## 3.3 El Patron "Antes/Despues"

Contrastes explicitos para transiciones conceptuales:

```markdown
### Antes ([Enfoque previo]):
1. Paso A
2. Paso B
3. **Resultado limitado**

### Ahora ([Enfoque nuevo]):
1. Paso A modificado
2. Paso B nuevo
3. **Resultado mejorado porque...**
```

## 3.4 El Patron "Problema-Solucion"

Cada concepto se introduce via el PROBLEMA que resuelve:

1. Establecer el problema en lenguaje cotidiano
2. Dar una analogia o escenario concreto
3. Introducir el concepto formal como la solucion

Nunca definir un concepto en aislamiento. Siempre emerge de un problema concreto.

## 3.5 El Patron "Que Pasaria Si..."

Razonamiento contrafactual para entender componentes:

```markdown
- **Sin [componente A]:** [Consecuencia negativa concreta]
- **Sin [componente B]:** [Consecuencia negativa diferente]
- **Con ambos:** [Resultado equilibrado]
```

## 3.6 El Patron "Lo Que SI / Lo Que NO"

Gestionar prioridades de estudio para parciales:

```markdown
**Lo que SI Necesitas Entender:**
- [Concepto clave 1]
- [Concepto clave 2]

**Lo que NO Necesitas Memorizar:**
- [Detalle de implementacion]
- [Derivacion completa]
```

## 3.7 Decomposicion por Zoom Anidado

Panorama general primero, luego zoom a cada componente con sub-secciones H3 dedicadas. Cada sub-componente recibe su propia seccion con citas, traduccion, y ejemplo.

## 3.8 Decomposicion Linea por Linea de Codigo

Cuando hay codigo, cada linea se explica:

```markdown
**Que hace cada parte?**
- `linea 1` -> Explicacion de que hace
- `linea 2` -> Explicacion de que hace
- `linea 3` -> Explicacion de que hace
```

---

# 4. TRATAMIENTO DE MATEMATICA Y FORMULAS

## Principio: Numeros Primero, Simbolos Despues, Formulas al Final

### Capa 1: Aritmetica Concreta
Ejemplo numerico especifico trabajado paso a paso.

### Capa 2: Variables Nombradas
Reemplazar numeros por nombres descriptivos.

### Capa 3: Formula General
La expresion matematica formal.

### Capa 4: "Por que importa?"
Interpretacion en lenguaje simple.

## Regla de Oro: Cada Formula Recibe Traduccion Inmediata

Sin excepcion, toda expresion matematica va seguida de explicacion simbolo por simbolo:

```markdown
**[Formula]**

Que significa esto?
- [Simbolo 1] = [significado en lenguaje simple]
- [Simbolo 2] = [significado en lenguaje simple]
- [La formula completa dice:] [reformulacion en una oracion]
```

## Formulas en Code Blocks (No LaTeX)

Las formulas se colocan en bloques de codigo triple-backtick. Los subindices se escriben como texto plano. Se usa `x` o `*` para multiplicacion.

## Etiqueta "No Memorizar"

Cuando una formula es para entendimiento, no para el examen:
```markdown
**Formula (no memorizar):**
[formula en code block]
```

---

# 5. ANALOGIAS Y EJEMPLOS

## Principio: Toda Abstraccion Recibe al Menos una Analogia Concreta

Las analogias deben ser:
- De la vida cotidiana (cocina, transporte, deportes, trabajo)
- Especificas al contexto del estudiante cuando sea posible
- Atribuidas al profesor si vienen de la clase

## Principio: Todo Concepto Recibe un Ejemplo Numerico Concreto

Sin excepcion. Cada formula, cada proceso, cada algoritmo — un ejemplo con numeros reales trabajado paso a paso.

## Catalogo de Analogias

Cada curso debe mantener un catalogo de analogias usadas por el profesor. Formato:

```markdown
| Tema | Analogia | Fuente |
|------|---------|--------|
| [Concepto] | [Analogia del profesor] | Clase N |
```

---

# 6. FORMATO Y CONVENCIONES VISUALES

## Enfasis

- **Negrita** para terminos clave en su primera aparicion y para enfasis general
- **Italica NUNCA se usa** — todo el enfasis es via negrita
- **MAYUSCULAS** para advertencias criticas: "MUY IMPORTANTE", "CRITICO!"
- Bloques de codigo para formulas, pseudocodigo, y diagramas ASCII

## Citas del Profesor

Siempre en blockquote Markdown:
```markdown
> "Cita textual del profesor"
```
Seguidas de atribucion: "Como dijo el profesor:", "El profesor explico:"

## Diagramas ASCII

Usados para flujos de datos, arquitecturas, y procesos:
```
[Entrada] --> [Proceso 1] --> [Proceso 2] --> [Salida]
```

Para cajas de resumen:
```
+======================================+
|           TITULO EN CAPS              |
+======================================+
|   Contenido                           |
+======================================+
```

## Tablas de Comparacion

Usadas para TODA decision "A vs B":
```markdown
| Aspecto | Opcion A | Opcion B |
|---------|----------|----------|
| [Criterio] | [Valor] | [Valor] |
```

## Emojis y Simbolos

- Checkmark / Warning / X — Solo en checklists de auditoria, no en contenido explicativo
- En documentos de explicacion: emojis con moderacion o sin emojis

## Separadores

- Regla horizontal (`---`) entre TODA seccion mayor
- Headings H3 crean ritmo dentro de secciones

---

# 7. ESTRUCTURA DE RESPUESTAS DE EXAMEN

## Formato Doble Capa

### Capa 1: Respuesta Corta (para el parcial)
En blockquote, 2-4 lineas densas con formula clave y terminologia:
```markdown
> [Respuesta concisa con la formula y los terminos clave, en el lenguaje basico que usaria el estudiante en el examen real]
```

### Capa 2: Explicacion Detallada
Breakdown extenso con citas del profesor, sub-headings, bullet points, code blocks, ejemplos concretos, y tablas comparativas.

## Principio para Formulas en Examenes
Las formulas se INTERPRETAN, no se DERIVAN. Preparar respuestas que expliquen cada termino de una formula dada, no que la deriven desde cero (salvo que el curso lo requiera).

---

# 8. IDIOMA Y REGISTRO

## Espanol con Terminos Tecnicos en Ingles

- Prosa en espanol
- Terminos tecnicos sin traducir cuando son estandar en la industria
- Codigo: variables en ingles, prints/logs en espanol

## Registro Semi-Informal

- Tuteo directo: "Imagina que tienes...", "Si tuvieras que explicarselo a alguien"
- Coloquialismos aceptables: "Vamos por partes", "Fin de la historia"
- Nunca condescendiente — tono de "estudiante mayor explicando a uno menor"
- Preguntas retoricas como transiciones: "verdad?", "Por que?", "Que significa esto?"

## Voseo Rioplatense en Citas

Las citas del profesor preservan su registro original incluyendo voseo, lunfardo, y coloquialismos. El texto autor puede usar "tu" implicito o "vos" — ambos son aceptables.

---

# 9. META-REGLAS TRANSVERSALES

1. **Nunca definir en aislamiento** — Los terminos emergen de problemas concretos
2. **Cada formula tiene un ejemplo numerico** — Sin excepcion
3. **Citas del profesor como ancla de autoridad** — Validar claims con lo que dijo el profesor
4. **Multiples representaciones** — Texto + numero + diagrama + analogia + tabla para cada concepto importante
5. **La negrita lo es todo** — Es el unico mecanismo de enfasis (no italica)
6. **Progresion de lo simple a lo complejo** — Dentro de cada archivo y entre archivos
7. **Orientacion al parcial** — Todo contenido termina con definiciones y preguntas de examen
8. **Exhaustividad sobre concision** — Es mejor explicar de mas que de menos
9. **Fidelidad al profesor** — Preservar su registro coloquial en las citas
10. **Conceptos antes del codigo** — El codigo siempre viene despues de la explicacion conceptual
11. **Sin comentarios en codigo** — El codigo se explica afuera, no adentro
12. **Principio "menos es mas" para notebooks** — Simple y sobrio en entregas
