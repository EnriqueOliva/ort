# Parcial 2 - Modelos de Deep Learning 2024
## Respuestas Cortas (1-2 oraciones)

**Fecha:** 02/12/2024 | **Duración:** 2h | **Puntaje:** 50/1 Puntos

---

# Ejercicio 1 - Transformers

## 1. Dada la arquitectura de transformers presentada en la imagen, explique en no más de 3 renglones los siguientes elementos:

### a. Input embedding

> **R:** Convierte cada palabra del texto de ENTRADA en un vector de números (típicamente 512). Es una tabla que asocia cada palabra del vocabulario con su representación numérica.

### b. Output embedding

> **R:** Convierte cada palabra del texto de SALIDA en un vector de números. En traducción usa un vocabulario diferente al input; en tareas del mismo idioma puede compartir la tabla con input embedding.

### c. Positional Encoding

> **R:** Suma información de posición a cada vector porque el Transformer procesa todo en paralelo y no sabe el orden. Usa funciones seno/coseno para generar un patrón único por posición.

### d. Multi-Head Attention

> **R:** Permite que cada palabra "mire" a todas las demás para entender contexto. Usa 8 cabezas en paralelo, cada una aprendiendo relaciones diferentes (gramaticales, semánticas, etc.).

### e. Masked Multi-Head Attention

> **R:** Igual que Multi-Head Attention pero con una máscara que impide ver el futuro. Necesario en el decoder para que al predecir posición t solo vea posiciones 0 a t-1.

### f. Add & Norm

> **R:** Add = skip connection (suma entrada + salida de la capa) para facilitar flujo del gradiente. Norm = normaliza los valores para estabilizar el entrenamiento.

### g. Feed Forward

> **R:** Red neuronal de 2 capas (512→2048→512) aplicada a cada posición independientemente. Procesa la información que cada palabra aprendió del contexto.

### h. Linear

> **R:** Proyecta el vector de 512 dimensiones a un vector del tamaño del vocabulario (ej: 30,000). Cada posición del resultado es un "puntaje" para cada palabra posible.

### i. Softmax

> **R:** Convierte los puntajes (logits) en probabilidades que suman 1. La palabra con mayor probabilidad es la predicción del modelo.

### j. Multi-Head Attention (en decoder - Cross-Attention)

> **R:** El decoder mira al encoder. Q viene del decoder, K y V vienen del encoder. Permite al decoder saber qué parte del input es relevante para generar cada palabra.

---

## 2. ¿Qué operación se está realizando en el siguiente diagrama? Explíquela con el mayor nivel de detalle posible.

*[El diagrama muestra el cálculo de Scaled Dot-Product Attention con matrices Q, K, V]*

> **R:** Es el cálculo de **Scaled Dot-Product Attention**:
> 1. La entrada X (n tokens × d dimensiones) se multiplica por 3 matrices de pesos para obtener Q, K, V
> 2. Se calcula QK^T (producto punto entre queries y keys) → matriz de atención n×n
> 3. Se escala dividiendo por √d_k para evitar gradientes muy pequeños en softmax
> 4. Se aplica Softmax por filas → pesos de atención (suman 1)
> 5. Se multiplica por V → salida Z con información contextual ponderada

> **Fórmula:** Attention(Q,K,V) = softmax(QK^T / √d_k) × V

---

# Ejercicio 2 - Seq2Seq

## 1. Explique, con ejemplos y pseudocódigo, cómo implementaría el paso de codificación (encoding) y decoding de una secuencia en un modelo Seq2Seq recurrente.

> **R (Encoding):**
> ```
> h = 0
> for palabra in secuencia_entrada:
>     x = embedding(palabra)
>     h = RNN(x, h)  # h se actualiza en cada paso
> contexto = h  # el último h resume toda la entrada
> ```

> **R (Decoding):**
> ```
> h = contexto
> output = "<SOS>"
> while output != "<EOS>":
>     x = embedding(output)
>     h = RNN(x, h)
>     logits = Linear(h)
>     output = argmax(softmax(logits))
>     resultado.append(output)
> ```

> **Ejemplo:** Traducir "hola mundo" → Encoder procesa "hola", "mundo" y genera contexto C. Decoder recibe C, genera "hello", luego "world", luego "<EOS>".

---

## 2. ¿Qué beneficios tiene un modelo encoder-decoder para los problemas Seq2Seq frente a un modelo que emite un output en cada paso de la secuencia?

> **R:**
> 1. **Longitud variable:** Encoder-decoder puede generar secuencias de longitud DIFERENTE a la entrada (ej: "buenos días" → "good morning" tiene distinta cantidad de palabras)
> 2. **Separación de responsabilidades:** El encoder se especializa en ENTENDER, el decoder en GENERAR
> 3. **Contexto completo:** El encoder ve TODA la entrada antes de que el decoder empiece a generar, mientras que un modelo paso-a-paso genera sin ver el futuro del input

---

## 3. ¿Qué diferencias tiene implementar el punto 1 con una RNN o con un modelo de tipo transformer?

> **R:**

| Aspecto | RNN | Transformer |
|---------|-----|-------------|
| **Procesamiento** | Secuencial (palabra por palabra) | Paralelo (todas las palabras juntas) |
| **Velocidad** | Lento (no paralelizable) | Rápido (paralelizable en GPU) |
| **Dependencias largas** | Difícil (vanishing gradient) | Fácil (attention directo) |
| **Contexto** | Vector fijo C (cuello de botella) | Attention sobre todos los estados |
| **Posición** | Implícita (orden de procesamiento) | Explícita (positional encoding) |
| **Memoria** | Estado oculto h acumula info | Attention accede a todo directamente |

---
---

# SECCIÓN DE CONTEXTO: ¿Dónde encaja cada cosa?

Esta sección explica cómo se relacionan todos los conceptos mencionados arriba.

---

## 1. LA JERARQUÍA: De lo más grande a lo más pequeño

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    JERARQUÍA DE CONCEPTOS                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   NIVEL 1: PATRÓN                                                           │
│   └── Encoder-Decoder                                                       │
│       (idea abstracta: una parte entiende, otra genera)                     │
│                                                                             │
│   NIVEL 2: ARQUITECTURAS (implementan el patrón)                            │
│   ├── Seq2Seq con RNN                                                       │
│   │   (usa RNNs para encoder y decoder)                                     │
│   │                                                                         │
│   └── Transformer                                                           │
│       (usa Attention para encoder y decoder)                                │
│                                                                             │
│   NIVEL 3: COMPONENTES DEL TRANSFORMER                                      │
│   ├── Input/Output Embedding (convertir palabras a vectores)                │
│   ├── Positional Encoding (agregar info de posición)                        │
│   ├── Multi-Head Attention (mecanismo de atención)                          │
│   ├── Feed Forward (procesar cada posición)                                 │
│   ├── Add & Norm (estabilizar entrenamiento)                                │
│   ├── Linear (proyectar a vocabulario)                                      │
│   └── Softmax (convertir a probabilidades)                                  │
│                                                                             │
│   NIVEL 4: DENTRO DE MULTI-HEAD ATTENTION                                   │
│   └── Scaled Dot-Product Attention                                          │
│       (la fórmula matemática que hace el cálculo)                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. ¿Qué es Scaled Dot-Product Attention y dónde encaja?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│         SCALED DOT-PRODUCT ATTENTION = EL CORAZÓN DE TODO                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Es la OPERACIÓN MATEMÁTICA que está DENTRO de Multi-Head Attention.       │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    MULTI-HEAD ATTENTION                             │   │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐    │   │
│   │  │  Cabeza 1   │ │  Cabeza 2   │ │  Cabeza 3   │ │    ...      │    │   │
│   │  │             │ │             │ │             │ │             │    │   │
│   │  │ ┌─────────┐ │ │ ┌─────────┐ │ │ ┌─────────┐ │ │ ┌─────────┐ │    │   │
│   │  │ │ Scaled  │ │ │ │ Scaled  │ │ │ │ Scaled  │ │ │ │ Scaled  │ │    │   │
│   │  │ │Dot-Prod │ │ │ │Dot-Prod │ │ │ │Dot-Prod │ │ │ │Dot-Prod │ │    │   │
│   │  │ │Attention│ │ │ │Attention│ │ │ │Attention│ │ │ │Attention│ │    │   │
│   │  │ └─────────┘ │ │ └─────────┘ │ │ └─────────┘ │ │ └─────────┘ │    │   │
│   │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘    │   │
│   │         │               │               │               │           │   │
│   │         └───────────────┴───────────────┴───────────────┘           │   │
│   │                                 │                                   │   │
│   │                           Concatenar                                │   │
│   │                                 │                                   │   │
│   │                         Proyección final                            │   │
│   │                                 │                                   │   │
│   │                              Salida                                 │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   Multi-Head Attention = Correr Scaled Dot-Product Attention 8 veces        │
│                          en paralelo, cada una con diferentes pesos         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. La fórmula de Scaled Dot-Product Attention explicada

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   Attention(Q, K, V) = softmax( QK^T / √d_k ) × V                           │
│                                                                             │
│   ¿De dónde salen Q, K, V?                                                  │
│   ─────────────────────────                                                 │
│                                                                             │
│   Entrada X: matriz de n tokens × d dimensiones                             │
│   (ej: 10 palabras × 512 números cada una)                                  │
│                                                                             │
│   Q = X × W_Q    (Query: "¿qué busco?")                                     │
│   K = X × W_K    (Key: "¿qué ofrezco?")                                     │
│   V = X × W_V    (Value: "¿cuál es mi contenido?")                          │
│                                                                             │
│   W_Q, W_K, W_V son matrices de pesos que SE APRENDEN durante entrenamiento │
│                                                                             │
│   ¿Qué hace cada parte de la fórmula?                                       │
│   ───────────────────────────────────                                       │
│                                                                             │
│   PASO 1: QK^T                                                              │
│   ────────────                                                              │
│   Multiplica queries por keys transpuestas.                                 │
│   Resultado: matriz n×n donde posición (i,j) dice                           │
│   "cuánto la palabra i quiere atender a la palabra j"                       │
│                                                                             │
│   Ejemplo con 3 palabras:                                                   │
│                    palabra1  palabra2  palabra3                             │
│   palabra1    [     0.8       0.1       0.5    ]  ← palabra1 atiende a...   │
│   palabra2    [     0.2       0.9       0.3    ]  ← palabra2 atiende a...   │
│   palabra3    [     0.4       0.6       0.7    ]  ← palabra3 atiende a...   │
│                                                                             │
│   PASO 2: / √d_k                                                            │
│   ─────────────                                                             │
│   Divide por raíz de la dimensión de las keys.                              │
│   ¿Por qué? Sin esto, los valores serían muy grandes y softmax              │
│   daría casi todo el peso a un solo elemento (gradientes muy pequeños).     │
│                                                                             │
│   PASO 3: softmax                                                           │
│   ──────────────                                                            │
│   Convierte cada FILA en probabilidades que suman 1.                        │
│   Ahora tenemos "pesos de atención" normalizados.                           │
│                                                                             │
│   PASO 4: × V                                                               │
│   ──────────                                                                │
│   Multiplica los pesos por los valores.                                     │
│   Resultado: cada palabra obtiene un promedio ponderado de todas            │
│   las demás, según cuánto les prestó atención.                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Los tres tipos de Attention en el Transformer

```
┌─────────────────────────────────────────────────────────────────────────────┐
│           TRES USOS DE MULTI-HEAD ATTENTION EN EL TRANSFORMER               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Todos usan la MISMA fórmula (Scaled Dot-Product Attention),               │
│   pero con DIFERENTES fuentes de Q, K, V:                                   │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │ 1. SELF-ATTENTION (en el Encoder)                                   │   │
│   ├─────────────────────────────────────────────────────────────────────┤   │
│   │                                                                     │   │
│   │ Q, K, V vienen TODOS del ENCODER                                    │   │
│   │                                                                     │   │
│   │ ¿Qué hace?                                                          │   │
│   │ Cada palabra del INPUT mira a TODAS las palabras del INPUT.         │   │
│   │                                                                     │   │
│   │ Ejemplo: "El gato negro duerme"                                     │   │
│   │ → "duerme" mira a "gato" y aprende que es su sujeto                 │   │
│   │ → "negro" mira a "gato" y aprende que lo está describiendo          │   │
│   │                                                                     │   │
│   │ ¿Tiene máscara? NO - puede ver todas las palabras                   │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │ 2. MASKED SELF-ATTENTION (en el Decoder)                            │   │
│   ├─────────────────────────────────────────────────────────────────────┤   │
│   │                                                                     │   │
│   │ Q, K, V vienen TODOS del DECODER                                    │   │
│   │                                                                     │   │
│   │ ¿Qué hace?                                                          │   │
│   │ Cada palabra del OUTPUT mira a las palabras ANTERIORES del OUTPUT.  │   │
│   │                                                                     │   │
│   │ Ejemplo: Generando "Hello world"                                    │   │
│   │ → "world" puede ver "Hello" y "<SOS>"                               │   │
│   │ → "world" NO puede ver lo que viene después (no existe todavía)     │   │
│   │                                                                     │   │
│   │ ¿Tiene máscara? SÍ - solo ve el pasado (posiciones anteriores)      │   │
│   │                                                                     │   │
│   │ La máscara pone -∞ en las posiciones futuras antes del softmax,     │   │
│   │ haciendo que esos pesos sean 0.                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │ 3. CROSS-ATTENTION (en el Decoder)                                  │   │
│   ├─────────────────────────────────────────────────────────────────────┤   │
│   │                                                                     │   │
│   │ Q viene del DECODER                                                 │   │
│   │ K, V vienen del ENCODER                                             │   │
│   │                                                                     │   │
│   │ ¿Qué hace?                                                          │   │
│   │ Cada palabra del OUTPUT mira a TODAS las palabras del INPUT.        │   │
│   │                                                                     │   │
│   │ Ejemplo: Traduciendo "Bonjour monde" → "Hello world"                │   │
│   │ → Al generar "Hello", el decoder pregunta "¿qué parte del francés   │   │
│   │   debo mirar?" y atiende principalmente a "Bonjour"                 │   │
│   │ → Al generar "world", atiende principalmente a "monde"              │   │
│   │                                                                     │   │
│   │ ¿Tiene máscara? NO - puede ver todo el input (ya está completo)     │   │
│   │                                                                     │   │
│   │ Esta es la ÚNICA conexión entre Encoder y Decoder.                  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Seq2Seq con RNN vs Transformer: El problema del cuello de botella

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SEQ2SEQ CON RNN: EL CUELLO DE BOTELLA                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   En Seq2Seq con RNN:                                                       │
│                                                                             │
│   ENCODER (RNN):                                                            │
│   "Bonjour" → h₁ → "le" → h₂ → "monde" → h₃ = C (contexto)                  │
│                                            │                                │
│                                            │ ← TODA la información de la    │
│                                            │   oración está comprimida      │
│                                            │   en UN SOLO vector C          │
│                                            ▼                                │
│   DECODER (RNN):                                                            │
│   C → "Hello" → "world" → "<EOS>"                                           │
│                                                                             │
│   PROBLEMA: Si la oración es larga, C no puede recordar todo.               │
│   Esto se llama "cuello de botella" (bottleneck).                           │
│                                                                             │
│   ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│   SOLUCIÓN 1: Bahdanau Attention (2014)                                     │
│   El decoder puede mirar TODOS los estados ocultos h₁, h₂, h₃               │
│   en cada paso de generación, no solo el último C.                          │
│                                                                             │
│   SOLUCIÓN 2: Transformer (2017)                                            │
│   Elimina las RNNs por completo. Usa solo Attention.                        │
│   El decoder hace Cross-Attention sobre todos los estados del encoder.      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. ¿Por qué el Transformer necesita Positional Encoding?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RNN vs TRANSFORMER: ORDEN DE LAS PALABRAS                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   RNN: PROCESA SECUENCIALMENTE                                              │
│   ────────────────────────────                                              │
│                                                                             │
│   "El" → "gato" → "negro" → "duerme"                                        │
│    t=1    t=2      t=3       t=4                                            │
│                                                                             │
│   La RNN SABE el orden porque procesa palabra por palabra.                  │
│   La posición está IMPLÍCITA en el orden de procesamiento.                  │
│                                                                             │
│   ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│   TRANSFORMER: PROCESA EN PARALELO                                          │
│   ─────────────────────────────────                                         │
│                                                                             │
│   "El"    "gato"    "negro"    "duerme"                                     │
│     │        │         │          │                                         │
│     └────────┴─────────┴──────────┘                                         │
│              │                                                              │
│        (todos juntos)                                                       │
│                                                                             │
│   El Transformer ve todas las palabras AL MISMO TIEMPO.                     │
│   Sin Positional Encoding, no distinguiría entre:                           │
│   - "El gato negro duerme"                                                  │
│   - "Negro el duerme gato"                                                  │
│                                                                             │
│   Positional Encoding SUMA un vector de posición a cada embedding:          │
│   embedding("gato") + posición(2) = vector que representa "gato en pos 2"   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Resumen: El flujo completo del Transformer

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              FLUJO COMPLETO: TRADUCIR "Bonjour monde" → "Hello world"       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   PASO 1: ENCODER                                                           │
│   ───────────────                                                           │
│   "Bonjour monde"                                                           │
│         │                                                                   │
│         ▼                                                                   │
│   [Input Embedding] → vectores para cada palabra                            │
│         │                                                                   │
│         ▼                                                                   │
│   [+ Positional Encoding] → vectores con info de posición                   │
│         │                                                                   │
│         ▼                                                                   │
│   [Self-Attention] → cada palabra mira a las otras                          │
│   [Add & Norm]                                                              │
│   [Feed Forward] → procesa cada posición                                    │
│   [Add & Norm]                                                              │
│         │                                                                   │
│         │ (repetir N veces)                                                 │
│         ▼                                                                   │
│   REPRESENTACIÓN FINAL DEL ENCODER                                          │
│   (lista de vectores enriquecidos con contexto)                             │
│         │                                                                   │
│         │                                                                   │
│   PASO 2: DECODER (genera palabra por palabra)                              │
│   ───────────────────────────────────────────                               │
│         │                                                                   │
│   Iteración 1: Generar "Hello"                                              │
│   ─────────────────────────────                                             │
│   "<SOS>"                                                                   │
│         │                                                                   │
│         ▼                                                                   │
│   [Output Embedding] → vector para "<SOS>"                                  │
│   [+ Positional Encoding]                                                   │
│         │                                                                   │
│         ▼                                                                   │
│   [Masked Self-Attention] → "<SOS>" solo se ve a sí mismo                   │
│   [Add & Norm]                                                              │
│         │                                                                   │
│         ▼                                                                   │
│   [Cross-Attention] ←───── K,V del encoder                                  │
│   [Add & Norm]        (mira "Bonjour monde", atiende a "Bonjour")           │
│         │                                                                   │
│         ▼                                                                   │
│   [Feed Forward]                                                            │
│   [Add & Norm]                                                              │
│         │                                                                   │
│         │ (repetir N veces)                                                 │
│         ▼                                                                   │
│   [Linear] → 30,000 puntajes (uno por palabra inglesa)                      │
│   [Softmax] → probabilidades                                                │
│         │                                                                   │
│         ▼                                                                   │
│   "Hello" (palabra con mayor probabilidad)                                  │
│                                                                             │
│   Iteración 2: Generar "world"                                              │
│   ─────────────────────────────                                             │
│   "<SOS>" "Hello"                                                           │
│         │                                                                   │
│         ▼                                                                   │
│   [Masked Self-Attention] → "Hello" puede ver "<SOS>" y a sí mismo          │
│   [Cross-Attention] → atiende a "monde"                                     │
│         │                                                                   │
│         ▼                                                                   │
│   "world"                                                                   │
│                                                                             │
│   Iteración 3: Generar "<EOS>"                                              │
│   ─────────────────────────────                                             │
│   "<SOS>" "Hello" "world"                                                   │
│         │                                                                   │
│         ▼                                                                   │
│   "<EOS>" → FIN                                                             │
│                                                                             │
│   RESULTADO: "Hello world"                                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```
