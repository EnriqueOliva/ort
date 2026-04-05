# Información del Parcial 2 - Lo que dijo el Profesor

**Fuente:** Clase del 24-11-2025 (transcripción completa)

---

## FORMATO DEL EXAMEN

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ESTRUCTURA DEL PARCIAL                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   El profesor dijo TEXTUALMENTE:                                            │
│                                                                             │
│   "El parcial es la defensa, o sea, pero no es solo la defensa.             │
│    No es solo la defensa. Hay preguntas aparte.                             │
│    La mayor parte son preguntas. Ya creo que dos preguntas, tres."          │
│                                                                             │
│   COMPONENTES:                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │ 1. DEFENSA DEL TALLER (obligatoria, pero NO es todo el parcial)     │   │
│   │ 2. PREGUNTAS ESCRITAS (2-3 preguntas) ← LA MAYOR PARTE              │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## LO QUE NO VA A CAER

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ❌ NO ENTRA EN EL PARCIAL                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   1. ZERO-SHOT LEARNING / TRANSFER LEARNING                                 │
│      "Zero shot learning. Esto no lo vimos, que es transfer,                │
│       no nos dieron clases."                                                │
│                                                                             │
│   2. MODELO CLIP                                                            │
│      "Hay una parte de clip que es un modelo, eso no lo vimos nosotros,     │
│       tuvimos dos clases menos."                                            │
│                                                                             │
│   3. EJERCICIO COMPLETO DE CONTAR PARÁMETROS                                │
│      "No va a haber un ejercicio así."                                      │
│      "No, no, no va a haber."                                               │
│      "Llevo horas calcular todo esto, horas... no va a haber en el          │
│       parcial, pero sí una PARTECITA"                                       │
│                                                                             │
│   4. CALCULAR GPT-3 COMPLETO                                                │
│      (dicho con sarcasmo) "Ejercicio parcial va a ser calcular GPT3"        │
│      → NO, obviamente no va a caer                                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## LO QUE SÍ VA A CAER

El profesor mostró el **Parcial 2 del año pasado (2024)** y confirmó:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ✅ SÍ ENTRA EN EL PARCIAL                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   "Hay un ejercicio de la arquitectura del Transformer.                     │
│    Hay un ejercicio de attention.                                           │
│    Hay un ejercicio de seq to seq."                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1. TRANSFORMERS - Arquitectura

**Pregunta típica:**
> "De la arquitectura de Transformer presentada en la imagen, explique en no más de tres renglones los siguientes elementos."

**Elementos que hay que saber explicar:**
- Input embedding
- Output embedding
- Positional encoding
- Multi-head attention
- Masked multi-head attention
- Add & Norm
- Feed Forward
- Capa Linear final
- Softmax

### 2. ATTENTION - Mecanismo

**Pregunta típica:**
> "¿Qué operación se está realizando en el siguiente diagrama? Explique con el mayor nivel de detalle posible."

El profesor dijo:
> "Ahora la tienen que hacer de taquito... es lo que acabamos de hacer, o sea, en vez de poner d_k, pone d_q, pero es lo mismo. Tengo la WQ, la WK, la WV"

**Lo que hay que saber:**
- Fórmula: softmax(QK^T / √d_k) × V
- Dimensiones de Q, K, V
- Qué hace cada matriz (WQ, WK, WV)
- Por qué se divide por √d_k

### 3. MÁSCARAS EN EL DECODER

**Pregunta típica:**
> "¿Por qué se enmascara? ¿Qué quiere decir que es enmascarado?"

**Respuesta del profesor:**
> "Es para evitar data leakage temporal... cuando vos mires la fila que está en el tiempo tres, vos no querés que la attention pueda mirar las palabras que están en el tiempo tres en adelante, a la hora de predecir la palabra tres."

### 4. SEQ2SEQ

**Preguntas típicas:**
> "Explique con ejemplos y pseudocódigo cómo implementaría el paso de codificación (encoding) y decoding de una secuencia en un modelo Seq2Seq recurrente."

> "¿Qué beneficios tiene un modelo encoder-decoder para los problemas Seq2Seq frente a un modelo que emite un output en cada paso de la secuencia?"

> "¿Qué diferencias tiene implementar el punto uno con una RNN o con un modelo de tipo Transformer?"

**Respuesta clave del profesor:**
> "La salida puede ser de distinto largo que la entrada" - Ventaja principal de encoder-decoder

### 5. RESNETS Y SKIP CONNECTIONS

**⚠️ PREGUNTA MUY IMPORTANTE - ESTÁ EN LA GUÍA**

El profesor dijo textualmente:
> "Esta pregunta está en la guía de estudio: 'Justifique conceptualmente por qué una red más profunda puede entrenar peor que una red más superficial, incluso teniendo mayor capacidad representacional.'"

**Puntos clave de la respuesta:**
- Es problema de **vanishing gradient**, NO de overfitting
- Es un problema de **optimización**, no de capacidad
- En teoría, capas adicionales podrían ser identidad
- Skip connections ayudan porque la derivada siempre tiene un "+1"

**El profesor enfatizó:**
> "Compare este fenómeno con el sobreajuste. O sea, que no tiene que ver con sobreajuste, son cosas diferentes."

### 6. REDES RECURRENTES

**Pregunta típica:**
> "En una red recurrente, escriba qué ocurriría si B fuese la matriz nula."

**Respuesta del profesor:**
> "Si fuese cero... es un MLP."

### 7. MAPAS DE ATENCIÓN

**Pregunta típica:**
> "Complete la tabla cualitativamente (con X o valores como alta, media, baja) para un mapa de atención."

**Pregunta clave del profesor:**
> "¿Cómo se leen estos? ¿Tienen que llenar las columnas o tienen que llenar las filas?"

**Respuesta correcta:** "Las filas" - Cada fila representa qué palabras del encoder mira la palabra del decoder.

### 8. TOKENS ESPECIALES (SOS, EOS)

**Pregunta de la guía:**
> "Explique por qué se necesita explícitamente el token start of sequence. Describa qué problema surge si no se incluye."

**El profesor dijo:**
> "Sin el begin of sequence no puedes arrancar. Es como que no tuvieras ruedas en el auto."

### 9. LANGUAGE MODELS

**Ejercicio típico:**
> "Dado el siguiente texto: 'El perro corre rápido. El perro es feliz.' Construya un conjunto de datos de entrada y salida para entrenar una RNN en el problema de language model."

**Respuesta:** Crear n-gramas, bigramas, trigramas, ventanas deslizantes.

### 10. WORD2VEC

**Ejercicio típico:**
> "Armar los datos que se entrenan a partir de una frase - cómo arman los datos."

---

## SOBRE EL CÁLCULO DE PARÁMETROS

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CÁLCULO DE PARÁMETROS - IMPORTANTE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   El profesor dijo:                                                         │
│                                                                             │
│   "No va a haber un ejercicio completo de contar parámetros"                │
│   PERO                                                                      │
│   "Puede haber alguna parte de un cálculo... una PARTECITA"                 │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ IGUAL HAY QUE SABERLO?                                           │
│                                                                             │
│   "Forzarse a calcular los parámetros es como que te fuerza a entender      │
│    la arquitectura de punta a punta de la red."                             │
│                                                                             │
│   "Creo que los ayuda a bajar a tierra el tema en cuestión que van          │
│    a estudiar."                                                             │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   LO QUE SÍ DEBES SABER CALCULAR:                                           │
│   • Parámetros en Multi-Head Attention (WQ, WK, WV, WO + bias)              │
│   • Parámetros en Feed Forward (dos capas lineales)                         │
│   • Parámetros en Embeddings (vocabulario × d_model)                        │
│   • Parámetros en Layer Norm (γ y β)                                        │
│                                                                             │
│   IMPORTANTE: Los parámetros NO dependen de 'n' (longitud de secuencia)     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## MATERIALES DE ESTUDIO RECOMENDADOS

El profesor mencionó explícitamente:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      📚 QUÉ USAR PARA ESTUDIAR                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   1. GUÍA DE ESTUDIO                                                        │
│      "Tiene como 20 y pico preguntas de cada tema... de ahí va a salir      │
│       el parcial, todo lo que está ahí va a salir para el parcial."         │
│                                                                             │
│   2. PARCIAL DEL AÑO PASADO (2024)                                          │
│      "Vamos a ver un parcial que viene de parciales viejos"                 │
│      El profesor lo revisó en clase como referencia directa.                │
│                                                                             │
│   3. GUÍA DE EJERCICIOS DEL AÑO PASADO                                      │
│      "También miren la guía de ejercicios del año pasado,                   │
│       no está mal, bastante parecida."                                      │
│                                                                             │
│   4. LAS DIAPOSITIVAS (SLIDES)                                              │
│      "Cuando agarren esa diapo, agarren este ejercicio y                    │
│       traten de resolver."                                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## CÓMO ESTUDIAR - CONSEJOS DEL PROFESOR

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         💡 ESTRATEGIA DE ESTUDIO                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   1. "Bajen a tierra" - Entender la operativa, no solo la teoría            │
│                                                                             │
│   2. "Forzarse a calcular los parámetros te fuerza a entender               │
│       la arquitectura de punta a punta"                                     │
│                                                                             │
│   3. "Usen la guía como guía de estudio, traten de responder                │
│       estas preguntas cuando están estudiando el tema"                      │
│                                                                             │
│   4. "Cuando veas el teórico, mira el ejercicio" - Relacionar               │
│       teoría con práctica                                                   │
│                                                                             │
│   5. "Pasen eso porque es bien de eso. Cuando agarren esa diapo,            │
│       agarren este ejercicio y traten de resolver."                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## PREGUNTAS ESPECÍFICAS DE LA GUÍA MENCIONADAS

El profesor leyó varias preguntas de la guía en clase:

1. "Describa el proceso de cálculo de autoatención en términos de las matrices Q, K, V"

2. "¿Qué son los positional encodings? ¿Cómo se calculan y cómo influyen en la representación del texto?"

3. "Compare el costo computacional de los Transformers con las RNN y explique en qué circunstancias el costo puede ser prohibitivo"

4. "¿Qué problemas específicos de las RNN resuelve la self-attention en los Transformers?"

5. "Explique el papel de las máscaras en el mecanismo de atención de un Transformer"

6. "Explique por qué el modelo Seq2Seq necesita explícitamente el token SOS. Describa qué problema surge si no se incluye un token EOS"

7. "Compare conceptualmente soft attention con hard attention indicando ventajas y desventajas"

8. "Describa el objetivo principal del encoder y qué tipo de información produce. Explique cómo el decoder utiliza esa información"

9. "Justifique por qué una red más profunda puede entrenar peor que una más superficial" ⚠️

10. "En una red recurrente, ¿qué ocurriría si la matriz V fuese nula?"

---

## RESUMEN EJECUTIVO

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            RESUMEN FINAL                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   FORMATO: Defensa taller + 2-3 preguntas escritas (mayor parte)            │
│                                                                             │
│   ✅ TEMAS QUE ENTRAN:                                                      │
│   • Transformers (arquitectura, componentes)                                │
│   • Attention (self, masked, cross, fórmula)                                │
│   • Seq2Seq (encoder-decoder, pseudocódigo, beneficios)                     │
│   • RNN/LSTM (comparación con Transformers, conceptos)                      │
│   • ResNets (skip connections, vanishing gradient, degradación)             │
│   • Language Models (construcción de datos)                                 │
│   • Word2Vec (construcción de datos de entrenamiento)                       │
│   • Tokens especiales (SOS, EOS)                                            │
│   • Cálculo PARCIAL de parámetros (una partecita)                           │
│                                                                             │
│   ❌ NO ENTRA:                                                              │
│   • Zero-shot learning                                                      │
│   • Transfer learning                                                       │
│   • Modelo CLIP                                                             │
│   • Ejercicio COMPLETO de contar parámetros                                 │
│                                                                             │
│   📚 MATERIALES:                                                            │
│   • Guía de estudio (~20 preguntas por tema)                                │
│   • Parcial 2 del año pasado                                                │
│   • Guía de ejercicios del año pasado                                       │
│   • Diapositivas del curso                                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## CONTACTO

El profesor mencionó:
> "Cualquier cosa de orden, me escriben a mí con copia a Martín. Teams, es lo más fácil."
