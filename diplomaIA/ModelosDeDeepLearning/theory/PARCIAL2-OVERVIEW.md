# La Historia del Curso: De Imágenes a ChatGPT

## ¿De qué se trata todo esto?

Si te sientes perdido, este documento te explica **el viaje completo** de las clases 8-12.

---

## La Pregunta Central del Curso

> **¿Cómo puede una computadora entender y generar lenguaje humano?**

Todo lo que estudiamos en estas 5 clases es un camino hacia responder esa pregunta. ChatGPT, los traductores automáticos, los asistentes de voz... todos nacen de las ideas que vemos aquí.

---

## El Viaje en Una Imagen

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   CLASE 8                CLASE 9              CLASE 10                        ║
║   ───────                ───────              ────────                        ║
║   "Cerramos imágenes,    "¿Cómo procesamos    "¿Cómo predecimos              ║
║    abrimos texto"         secuencias?"         la siguiente palabra?"         ║
║                                                                               ║
║   ResNet ──────────────▶ RNN ─────────────▶ Modelos de Lenguaje              ║
║   Word2Vec                LSTM/GRU            Seq2Seq (patrón Enc-Dec         ║
║                                               implementado con RNN)           ║
║                                                      │                        ║
║                                                      │ PROBLEMA:              ║
║                                                      │ "Cuello de botella"    ║
║                                                      ▼                        ║
║                          CLASE 11             CLASE 12                        ║
║                          ────────             ────────                        ║
║                          "¿Cómo miramos       "La arquitectura                ║
║                           TODO a la vez?"      completa"                      ║
║                                                                               ║
║                          Attention ─────────▶ TRANSFORMER (patrón Enc-Dec     ║
║                          Self-Attention       implementado con Attention)     ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Capítulo 1: El Puente (Clase 8)

### ¿Dónde estábamos?
La primera mitad del curso fue sobre **imágenes**: CNNs, filtros, pooling. Redes que miran fotos y dicen "esto es un gato".

### El problema que resolvimos primero: Redes muy profundas
Queríamos redes con 100+ capas (más capas = más inteligencia), pero descubrimos que **no aprendían**. Los gradientes se desvanecían.

**La solución: ResNet y Skip Connections**
- Agregar "atajos" que permiten a la información fluir directamente
- Ahora podemos tener redes muy profundas que sí aprenden

> *"Es como agregar escaleras de emergencia en un edificio muy alto. Si el ascensor falla, todavía puedes bajar."*

### El gran giro: De imágenes a texto
El profesor pregunta: *"¿Y si queremos procesar texto en lugar de imágenes?"*

**El problema nuevo:** Las palabras no son píxeles. "Gato" y "felino" significan casi lo mismo, pero para una computadora son solo letras diferentes.

**La solución: Word Embeddings (Word2Vec)**
- Convertir palabras en vectores (listas de números)
- Palabras similares → vectores cercanos
- "Rey - Hombre + Mujer ≈ Reina" (¡las matemáticas capturan significado!)

### ¿Por qué importa?
> Ahora tenemos una forma de convertir palabras en números que una red neuronal puede procesar. Pero... ¿cómo procesamos una SECUENCIA de palabras?

---

## Capítulo 2: Procesando Secuencias (Clase 9)

### El nuevo problema
Una oración es una **secuencia ordenada**. "El perro muerde al hombre" ≠ "El hombre muerde al perro".

Las redes normales (feedforward) no tienen **memoria**. Si les pasas palabra por palabra, se olvidan de lo anterior.

### La solución: Redes Recurrentes (RNN)

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Palabra 1 ──▶ [CAJA] ──▶ Memoria actualizada             │
│                    │                                        │
│   Palabra 2 ──▶ [CAJA] ──▶ Memoria actualizada             │
│                    │        (recuerda palabra 1)            │
│                    │                                        │
│   Palabra 3 ──▶ [CAJA] ──▶ Memoria actualizada             │
│                             (recuerda palabras 1 y 2)       │
│                                                             │
│   La misma "CAJA" se usa en cada paso (weight sharing)      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**La idea:** La red tiene un "estado oculto" que funciona como memoria. Cada palabra actualiza esa memoria.

### Pero hay un problema...
Las RNN básicas **se olvidan** de lo que pasó hace mucho. Si la oración es muy larga, cuando llegas al final ya no recuerdas el principio.

**La solución: LSTM y GRU**
- Agregan "compuertas" que deciden qué recordar y qué olvidar
- **GRU es más simple y el profesor la recomienda**

### ¿Por qué importa?
> Ahora podemos procesar secuencias de cualquier longitud. Pero... ¿qué hacemos con esa capacidad?

---

## Capítulo 3: Predecir Palabras (Clase 10)

### La tarea fundamental
> **Dado:** "Necesito un vaso de..."
> **Predecir:** ¿Cuál es la siguiente palabra?

Esto se llama **Modelo de Lenguaje**. Es la base de TODO: traducción, resumen, chatbots, autocompletado.

### El enfoque antiguo: Contar (N-gramas)
- Miras tu base de datos
- "vaso de agua" aparece 400 veces
- "vaso de leche" aparece 100 veces
- Conclusión: P(agua) = 0.4, P(leche) = 0.1

**Problema:** Hay DEMASIADAS combinaciones posibles. La mayoría nunca las viste.

### El enfoque moderno: Redes Neuronales
Usamos RNN/LSTM/GRU para predecir la siguiente palabra. La red **aprende patrones** en lugar de solo contar.

### El problema de las longitudes diferentes

¿Qué pasa si quiero traducir?
- Entrada: "Hello" (1 palabra)
- Salida: "Hola" (1 palabra) ✓

Pero:
- Entrada: "How are you?" (3 palabras)
- Salida: "¿Cómo estás?" (2 palabras) ✗

**La entrada y la salida pueden tener longitudes diferentes.**

### La solución: El patrón Encoder-Decoder (implementado como "Seq2Seq")

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│   ENCODER                          DECODER                    │
│   ────────                         ───────                    │
│   "Bonjour"  ──┐                 ┌──▶ "Hello"                │
│   "le"       ──┼──▶ [CONTEXTO] ──┼──▶ "world"                │
│   "monde"    ──┘     (vector)    └──▶ (fin)                  │
│                                                               │
│   Comprime TODO          Genera palabra                       │
│   en UN vector           por palabra                          │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

**La idea (el patrón Encoder-Decoder):**
1. El ENCODER lee toda la entrada y la comprime en un vector
2. El DECODER usa ese vector para generar la salida, palabra por palabra

**Nota importante:** "Encoder-Decoder" es el PATRÓN (la idea general). "Seq2Seq" es una ARQUITECTURA específica que implementa ese patrón usando RNN/LSTM/GRU. Más adelante veremos que el Transformer es OTRA arquitectura que implementa el mismo patrón pero con Self-Attention.

### ¿Por qué importa?
> Ahora podemos hacer traducción, resumen, subtítulos de videos... cualquier tarea donde la entrada y salida son secuencias de diferente longitud.

### PERO HAY UN PROBLEMA GRAVE: EL CUELLO DE BOTELLA

Todo el significado de la entrada se comprime en **UN SOLO VECTOR C** de dimensión fija.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       EL PROBLEMA DEL CUELLO DE BOTELLA                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   Frase corta: "Hola"                                                   │
│        │                                                                │
│        └──────────▶  C = [0.2, -0.5, 0.8, ...]  (ej: 256 dimensiones)  │
│                                                                         │
│   Frase LARGA: "El gato negro que vi ayer en el parque                 │
│                 estaba durmiendo tranquilamente bajo el árbol"          │
│        │                                                                │
│        └──────────▶  C = [0.3, -0.1, 0.4, ...]  (¡MISMAS 256 dims!)    │
│                                                                         │
│   ⚠️  PROBLEMA: Toda la información de una frase de 50 palabras        │
│                 tiene que caber en el mismo espacio que una de 2       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

El profesor leyó directamente del paper de Bahdanau:
> *"Esto es un cuello de botella en el mejoramiento del desempeño de esta arquitectura básica encoder-decoder."*

**Analogía:** Es como tratar de resumir un libro entero en una sola oración. Funciona para libros cortos, pero para "Guerra y Paz" vas a perder información importante.

---

## Capítulo 4: Bahdanau Attention - Solucionando el Cuello de Botella (Clase 11)

### El problema en detalle

En Seq2Seq SIN attention:

```
P(yᵢ) = función(C, Sᵢ₋₁, yᵢ₋₁)
                 ↑
        Siempre el MISMO C para todas las palabras
```

Cuando traduces "gato", usas el mismo C que cuando traduces "alfombra".
¿Tiene sentido? **No.** Para traducir "gato" deberías enfocarte en "cat", no en toda la oración.

### La solución de Bahdanau: Contexto DINÁMICO

El paper de Bahdanau propuso un cambio pequeño pero revolucionario:

```
ANTES:  P(yᵢ) = función(C,  Sᵢ₋₁, yᵢ₋₁)    ← C fijo
AHORA:  P(yᵢ) = función(Cᵢ, Sᵢ₋₁, yᵢ₋₁)    ← Cᵢ cambia en cada paso!
```

> *"El único cambio que propone es hacer que ahora dependa de un contexto que depende de la posición en la que estoy. Va a haber un C distinto para cada palabra target."*

### ¿Cómo se calcula Cᵢ?

```
Cᵢ = Σⱼ αᵢⱼ × Hⱼ    (promedio ponderado de TODOS los hidden states)
```

Donde:
- **Hⱼ** = todos los hidden states del encoder (H₁, H₂, H₃, ...)
- **αᵢⱼ** = pesos de atención (qué tan importante es Hⱼ para generar la palabra i)

### IMPORTANTE: Attention se AGREGA a Seq2Seq (no lo reemplaza)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SEQ2SEQ + BAHDANAU ATTENTION                         │
│                    (Sigue siendo Encoder-Decoder!)                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ENCODER (RNN/LSTM/GRU) ← igual que antes                             │
│   ─────────────────────                                                 │
│   "The"   → H₁ ─────────┐                                               │
│   "cat"   → H₂ ─────────┤                                               │
│   "sat"   → H₃ ─────────┼─────▶  TODOS los Hⱼ se guardan               │
│   "on"    → H₄ ─────────┤        (no solo el último!)                   │
│   "mat"   → H₅ ─────────┘                                               │
│                          │                                              │
│                          ▼                                              │
│              ┌───────────────────────┐                                  │
│              │   MECANISMO ATTENTION │  ← ESTO ES LO NUEVO              │
│              │   (Bahdanau)          │                                  │
│              │                       │                                  │
│              │   Calcula αᵢⱼ:        │                                  │
│              │   "Para generar yᵢ,   │                                  │
│              │    ¿cuánto miro a Hⱼ?"│                                  │
│              │                       │                                  │
│              │   Cᵢ = Σ αᵢⱼ × Hⱼ     │                                  │
│              └───────────┬───────────┘                                  │
│                          │                                              │
│                          ▼ Cᵢ (contexto DINÁMICO)                       │
│                                                                         │
│   DECODER (RNN/LSTM/GRU) ← igual que antes                             │
│   ─────────────────────                                                 │
│   <SOS> + C₁ → "El"      (C₁ enfoca en "The")                          │
│   "El"  + C₂ → "gato"    (C₂ enfoca en "cat")                          │
│   "gato"+ C₃ → "se"      (C₃ enfoca en "sat")                          │
│   ...                                                                   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### ¿Por qué se llama "Attention"?

> *"Porque lo que está haciendo es ver... a qué hidens presto más atención para hacer mi siguiente predicción."*

Es como cuando lees: tus ojos no miran todo el texto igual, se **enfocan** en las partes relevantes.

### El nombre técnico: Query, Key, Value

El profesor explicó la terminología moderna:
- **Query (Q):** "¿Qué estoy buscando?" → El hidden state del decoder (Sᵢ₋₁)
- **Keys (K):** "¿Qué opciones hay?" → Los hidden states del encoder (H₁, H₂, ...)
- **Values (V):** "¿Qué información obtengo?" → También los hidden states (H₁, H₂, ...)

> *"Es como buscar en un diccionario. La query es lo que busco, los keys son las palabras del diccionario, y los values son las definiciones."*

---

## Capítulo 4.5: Self-Attention - La Siguiente Evolución

### De Attention a Self-Attention

**Bahdanau Attention:** El decoder mira al encoder
**Self-Attention:** Cada palabra mira a TODAS las demás palabras (de la misma secuencia)

### ¿Para qué sirve?

La siguiente evolución: ¿Y si CADA palabra pudiera mirar a TODAS las otras palabras para entender su contexto?

Ejemplo: "El banco está cerca del río"
- La palabra "banco" necesita ver "río" para saber que es un banco de tierra, no de dinero

### Query, Key, Value: La terminología

El profesor usa una analogía:
> *"Es como buscar en un catálogo de fotos. Tu QUERY es lo que buscas. Las KEYS son las etiquetas de cada foto. Los VALUES son las fotos mismas."*

- **Query (Q):** Lo que estoy buscando
- **Key (K):** Las etiquetas de cada elemento
- **Value (V):** La información que quiero obtener

### ¿Por qué importa?
> Attention resuelve el cuello de botella. Ahora el modelo puede "enfocarse" en las partes relevantes de la entrada.

---

## Capítulo 5: El Transformer (Clase 12)

### El último problema: Velocidad

Las RNN procesan **secuencialmente**: palabra 1, luego palabra 2, luego palabra 3...

Si tienes millones de oraciones (Wikipedia entera), esto toma **años**.

### La idea revolucionaria

> **¿Y si eliminamos la recurrencia por completo y procesamos TODAS las palabras al mismo tiempo?**

Eso es el **Transformer**.

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│   RNN:        palabra1 → palabra2 → palabra3 → palabra4      │
│               (secuencial, lento)                             │
│                                                               │
│   TRANSFORMER: palabra1                                       │
│                palabra2    ──▶ TODO EN PARALELO               │
│                palabra3                                       │
│                palabra4                                       │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### Pero hay un problema: El orden importa

Si procesamos todo al mismo tiempo, ¿cómo sabe el modelo que "palabra1" viene antes que "palabra2"?

**Solución: Positional Encoding**
- Agregamos información de posición a cada palabra
- "Esta palabra está en la posición 1, esta en la posición 2..."

### Otro problema: No mirar el futuro

Durante entrenamiento, el modelo ve toda la oración. Pero en la vida real, cuando generas texto, no sabes qué viene después.

**Solución: Masked Attention**
- Una "máscara" que impide mirar palabras futuras
- El modelo aprende a predecir sin hacer trampa

### La arquitectura completa

```
┌─────────────────────────────────────────────────────────────────────┐
│                         TRANSFORMER                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ENCODER                              DECODER                      │
│   ────────                             ───────                      │
│   ┌─────────────────┐                  ┌─────────────────┐         │
│   │ Self-Attention  │                  │ Masked Self-Att │         │
│   │ + Skip Connect  │                  │ + Skip Connect  │         │
│   │ + Layer Norm    │                  │ + Layer Norm    │         │
│   ├─────────────────┤                  ├─────────────────┤         │
│   │ Feed-Forward    │                  │ Cross-Attention │         │
│   │ + Skip Connect  │    CONTEXTO      │ (mira encoder)  │         │
│   │ + Layer Norm    │ ──────────────▶  │ + Skip Connect  │         │
│   └─────────────────┘                  ├─────────────────┤         │
│         × N bloques                    │ Feed-Forward    │         │
│                                        │ + Skip Connect  │         │
│                                        │ + Layer Norm    │         │
│                                        └─────────────────┘         │
│                                              × N bloques            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### ¿Por qué importa?
> El Transformer es la arquitectura detrás de ChatGPT, BERT, GPT-4, y prácticamente todos los modelos de lenguaje modernos. Entender esto es entender cómo funciona la IA actual.

---

## Resumen: La Historia Completa

| Clase | Pregunta | Respuesta | Problema que queda |
|-------|----------|-----------|-------------------|
| **8** | ¿Cómo representamos palabras? | Word Embeddings | ¿Cómo procesamos secuencias? |
| **9** | ¿Cómo procesamos secuencias? | RNN, LSTM, GRU | ¿Cómo predecimos palabras? |
| **10** | ¿Cómo predecimos palabras? | Modelos de Lenguaje, Seq2Seq | Cuello de botella del contexto |
| **11** | ¿Cómo miramos lo relevante? | Attention, Self-Attention | Procesamiento secuencial lento |
| **12** | ¿Cómo procesamos en paralelo? | **Transformer** | (Resuelto!) |

---

## ¿Qué tienen que ver las Skip Connections con todo esto?

Las Skip Connections de la clase 8 aparecen **dentro del Transformer**. Cada bloque tiene conexiones residuales.

El mismo truco que usamos para entrenar redes profundas de imágenes (ResNet) se usa para entrenar Transformers profundos.

---

## El Mensaje Final del Profesor

> *"No piensen en esto como magia. Los modelos de lenguaje modernos están haciendo fundamentalmente lo mismo que Shannon hacía en los años 40: estimar qué palabra viene después. La diferencia es que ahora lo hacemos con redes neuronales, más datos, y más poder de cómputo."*

> *"El Transformer no es mejor que las RNN porque 'performa mejor'. Es mejor porque **escala**. Puedes entrenarlo con todo Wikipedia en días, no años."*

---

## Mapa de Conceptos

```
PRIMERA MITAD DEL CURSO          SEGUNDA MITAD DEL CURSO
─────────────────────────        ─────────────────────────────────────────

    IMÁGENES                          SECUENCIAS (TEXTO)
       │                                     │
       ▼                                     ▼
     CNNs                             Word Embeddings (Clase 8)
       │                                     │
       ▼                                     ▼
   ResNet/DenseNet ─────────────────▶ RNN/LSTM/GRU (Clase 9)
   (Skip Connections)                        │
                                             ▼
                                    Modelos de Lenguaje (Clase 10)
                                    Seq2Seq (patrón Enc-Dec con RNN)
                                             │
                                             ▼
                                    Attention (Clase 11)
                                    Self-Attention
                                             │
                                             ▼
                                    TRANSFORMER (Clase 12)
                                    (patrón Enc-Dec con Attention)
                                             │
                                             ▼
                                    ChatGPT, BERT, GPT-4...
```

---

## Para Estudiar

Cada clase tiene su archivo `explicaciones.md` con los detalles técnicos. Este documento es el **mapa** que te dice por qué estás estudiando cada cosa y cómo se conectan.

Cuando estudies un tema específico, pregúntate:
1. ¿Qué problema resuelve esto?
2. ¿Qué problema queda sin resolver?
3. ¿Cómo lo resuelve la siguiente clase?

Esa es la historia del curso.

---
---

# APÉNDICE: Clasificación de Conceptos por Tipo

## ¿Por qué esta sección?

Los conceptos del curso son de **tipos muy diferentes**. No es lo mismo una "RNN" que un "Encoder-Decoder" que "Word Embedding". Son categorías distintas.

**Para entender la diferencia, vamos a usar una CNN básica como referencia.**

---

## Primero: Recordemos una CNN básica

Tú ya conoces una CNN para clasificar imágenes. Vamos a usarla como base:

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         CNN BÁSICA PARA IMÁGENES                              ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ENTRADA                                                                     ║
║   ───────                                                                     ║
║   Una foto de un gato                                                         ║
║        │                                                                      ║
║        ▼                                                                      ║
║   ┌─────────────────────────────────────────────────────────────────────┐     ║
║   │  PREPROCESAMIENTO: Convertir foto a números                         │     ║
║   │  ─────────────────────────────────────────                          │     ║
║   │  Foto (JPG) → Tensor de números [224 × 224 × 3]                     │     ║
║   │               (altura × ancho × canales RGB)                        │     ║
║   │                                                                     │     ║
║   │  Esto es REPRESENTACIÓN DE LOS DATOS                                │     ║
║   └─────────────────────────────────────────────────────────────────────┘     ║
║        │                                                                      ║
║        ▼                                                                      ║
║   ┌─────────────────────────────────────────────────────────────────────┐     ║
║   │  LA RED NEURONAL: Capas que procesan                                │     ║
║   │  ───────────────────────────────────────                            │     ║
║   │                                                                     │     ║
║   │  Conv2D → ReLU → MaxPool → Conv2D → ReLU → MaxPool → Flatten → Dense│     ║
║   │                                                                     │     ║
║   │  Cada una de estas (Conv2D, ReLU, MaxPool, Dense) es una CAPA       │     ║
║   └─────────────────────────────────────────────────────────────────────┘     ║
║        │                                                                      ║
║        ▼                                                                      ║
║   SALIDA: "Esto es un gato" (probabilidad 0.95)                               ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

**Ahora identifiquemos LOS TRES TIPOS de cosas diferentes:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   1. REPRESENTACIÓN DE DATOS        2. CAPAS                3. ARQUITECTURA │
│      (cómo entran los datos)           (qué hace el cálculo)   (cómo se     │
│                                                                organizan)   │
│   ┌───────────────────┐            ┌──────────────────┐    ┌─────────────┐ │
│   │ Foto → Tensor     │            │ Conv2D           │    │ "VGG"       │ │
│   │ [224×224×3]       │            │ ReLU             │    │ "LeNet"     │ │
│   │                   │            │ MaxPool          │    │ "AlexNet"   │ │
│   │ Label → One-hot   │            │ Dense            │    │ "ResNet"    │ │
│   │ [0,0,1,0,0]       │            │ Dropout          │    │             │ │
│   └───────────────────┘            └──────────────────┘    └─────────────┘ │
│                                                                             │
│   OCURRE ANTES de      │            SON las piezas que      ES el PLANO    │
│   entrar a la red      │            hacen el trabajo        que dice cómo  │
│                        │                                    ordenar las    │
│                        │                                    piezas         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## La diferencia CLAVE entre los 3 tipos

### En una CNN (que ya conoces):

| Pregunta | Respuesta | Tipo |
|----------|-----------|------|
| ¿Cómo convierto una foto en números? | Tensor [224×224×3] | **REPRESENTACIÓN** |
| ¿Qué operaciones matemáticas hago? | Conv2D, MaxPool, Dense | **CAPAS** |
| ¿En qué orden pongo las capas? | "Pon 2 Conv, luego Pool, luego Dense..." | **ARQUITECTURA** |

### En NLP (lo que estamos aprendiendo):

| Pregunta | Respuesta | Tipo |
|----------|-----------|------|
| ¿Cómo convierto una palabra en números? | Word Embedding, One-Hot | **REPRESENTACIÓN** |
| ¿Qué operaciones matemáticas hago? | RNN, LSTM, GRU, Self-Attention | **CAPAS** |
| ¿En qué orden pongo las capas? | Seq2Seq, Transformer (ambos usan patrón Enc-Dec) | **ARQUITECTURA** |

---

## Diagrama: ¿Dónde encaja cada cosa?

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                    ┌──────────────────────────────────────┐                   ║
║                    │         MUNDO REAL                   │                   ║
║                    │   (fotos, palabras, audio)           │                   ║
║                    └──────────────────┬───────────────────┘                   ║
║                                       │                                       ║
║                                       ▼                                       ║
║   ┌───────────────────────────────────────────────────────────────────────┐   ║
║   │                                                                       │   ║
║   │   ██████████████████████████████████████████████████████████████████  │   ║
║   │   █  REPRESENTACIÓN DE DATOS                                       █  │   ║
║   │   █  ────────────────────────                                      █  │   ║
║   │   █  Convierte cosas reales en NÚMEROS que la red puede procesar   █  │   ║
║   │   █                                                                █  │   ║
║   │   █  CNN:  Foto → Tensor [224×224×3]                               █  │   ║
║   │   █  NLP:  "gato" → Vector [0.2, -0.5, 0.8, ...] (embedding)       █  │   ║
║   │   █                                                                █  │   ║
║   │   ██████████████████████████████████████████████████████████████████  │   ║
║   │                                                                       │   ║
║   └───────────────────────────────────┬───────────────────────────────────┘   ║
║                                       │                                       ║
║                                       ▼                                       ║
║   ┌───────────────────────────────────────────────────────────────────────┐   ║
║   │                                                                       │   ║
║   │   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │   ║
║   │   ▓  CAPAS (los tipos de operación)                                ▓  │   ║
║   │   ▓  ──────────────────────────────                                ▓  │   ║
║   │   ▓  Son las OPERACIONES MATEMÁTICAS que transforman los datos     ▓  │   ║
║   │   ▓                                                                ▓  │   ║
║   │   ▓  CNN:  Conv2D, MaxPool, Dense, ReLU, Dropout                   ▓  │   ║
║   │   ▓  NLP:  RNN, LSTM, GRU, Self-Attention, Feed-Forward            ▓  │   ║
║   │   ▓                                                                ▓  │   ║
║   │   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  │   ║
║   │                                                                       │   ║
║   │   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │   ║
║   │   ░  ARQUITECTURA (cómo se organizan las capas)                    ░  │   ║
║   │   ░  ──────────────────────────────────────────                    ░  │   ║
║   │   ░  Es el PLANO que dice qué capas usar y en qué orden            ░  │   ║
║   │   ░                                                                ░  │   ║
║   │   ░  CNN:  VGG, LeNet, AlexNet, ResNet                             ░  │   ║
║   │   ░  NLP:  Seq2Seq (con RNN), Transformer (con Attention)          ░  │   ║
║   │   ░        (Ambos implementan el PATRÓN Encoder-Decoder)           ░  │   ║
║   │   ░                                                                ░  │   ║
║   │   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │   ║
║   │                                                                       │   ║
║   └───────────────────────────────────┬───────────────────────────────────┘   ║
║                                       │                                       ║
║                                       ▼                                       ║
║                    ┌──────────────────────────────────────┐                   ║
║                    │         PREDICCIÓN                   │                   ║
║                    │   "Es un gato" / "La traducción es X"│                   ║
║                    └──────────────────────────────────────┘                   ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## Ahora sí: Los 7 Tipos de Cosas (con nombres claros)

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║  ██  TIPO 1: REPRESENTACIÓN DE DATOS                                             ║
║  ██  ───────────────────────────────                                             ║
║  ██  CUÁNDO: ANTES de que la red procese                                         ║
║  ██  QUÉ HACE: Convierte cosas reales (palabras, imágenes) en números            ║
║  ██                                                                              ║
║  ██  En CNN:     Foto → Tensor, Label → One-hot                                  ║
║  ██  En NLP:     Word Embeddings, One-Hot, Bag of Words, Positional Encoding     ║
║  ██                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║  ▓▓  TIPO 2: CAPAS (tipos de operación matemática)                               ║
║  ▓▓  ─────────────────────────────────────────────                               ║
║  ▓▓  CUÁNDO: DENTRO de la red neuronal                                           ║
║  ▓▓  QUÉ HACE: La operación matemática que transforma datos                      ║
║  ▓▓                                                                              ║
║  ▓▓  En CNN:     Conv2D, MaxPool, Dense, ReLU, Dropout, BatchNorm                ║
║  ▓▓  En NLP:     RNN, LSTM, GRU, Self-Attention, Multi-Head Attention, FFN       ║
║  ▓▓                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║  ░░  TIPO 3: ARQUITECTURA (el diseño/plano de la red)                            ║
║  ░░  ────────────────────────────────────────────────                            ║
║  ░░  CUÁNDO: Cuando DISEÑAS la red (antes de programar)                          ║
║  ░░  QUÉ HACE: Dice QUÉ capas usar y EN QUÉ ORDEN conectarlas                    ║
║  ░░                                                                              ║
║  ░░  En CNN:     LeNet, AlexNet, VGG, ResNet, DenseNet                           ║
║  ░░  En NLP:     Seq2Seq, Transformer (implementan patrón Encoder-Decoder)       ║
║  ░░                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║  TIPO 4: TÉCNICAS DE ENTRENAMIENTO                                               ║
║  ─────────────────────────────────                                               ║
║  CUÁNDO: Solo durante ENTRENAMIENTO (no cuando usas el modelo)                   ║
║  QUÉ HACE: Estrategias para que el modelo aprenda mejor                          ║
║                                                                                  ║
║  • Teacher Forcing    • Scheduled Sampling    • Masked Attention    • BPTT       ║
║                                                                                  ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║  TIPO 5: TRUCOS/MEJORAS ARQUITECTÓNICAS                                          ║
║  ──────────────────────────────────────                                          ║
║  CUÁNDO: Se agregan a las arquitecturas para mejorarlas                          ║
║  QUÉ HACE: Soluciona problemas específicos de entrenar redes profundas           ║
║                                                                                  ║
║  • Skip Connections    • Layer Normalization    • Gradient Clipping              ║
║                                                                                  ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║  TIPO 6: PROBLEMAS/FENÓMENOS                                                     ║
║  ───────────────────────────                                                     ║
║  CUÁNDO: Ocurren durante entrenamiento (no los buscamos, simplemente pasan)      ║
║  QUÉ ES: Situaciones que hay que entender y a veces solucionar                   ║
║                                                                                  ║
║  • Vanishing Gradient    • Exploding Gradient    • Double Descent                ║
║                                                                                  ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                  ║
║  TIPO 7: TAREAS (el problema que quieres resolver)                               ║
║  ─────────────────────────────────────────────────                               ║
║  CUÁNDO: Es lo PRIMERO que defines (¿qué quiero lograr?)                         ║
║  QUÉ ES: El objetivo final                                                       ║
║                                                                                  ║
║  En CNN:     Clasificar imágenes, detectar objetos                               ║
║  En NLP:     Traducir, resumir, predecir siguiente palabra, clasificar texto     ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
```

---

## Explicación detallada de TIPO 1, 2 y 3 (los que confunden)

### TIPO 1: REPRESENTACIÓN DE DATOS

**¿Qué es?**
Es CÓMO CONVIERTES algo del mundo real en números. Pasa **ANTES** de que la red neuronal haga nada.

**Analogía:** Es como el **combustible** de un auto. Antes de que el motor funcione, necesitas convertir petróleo crudo en gasolina.

**Ejemplo CNN (que conoces):**
```
ANTES:   Una foto de un gato (archivo JPG)
         ↓
         [Representación: convertir a tensor]
         ↓
DESPUÉS: Tensor de números [224, 224, 3]
         (224 píxeles alto × 224 ancho × 3 canales RGB)

         Cada píxel tiene un valor entre 0 y 255.
         Ahora SÍ puede entrar a la red.
```

**Ejemplo NLP:**
```
ANTES:   La palabra "gato"
         ↓
         [Representación: Word Embedding]
         ↓
DESPUÉS: Vector de 300 números [0.2, -0.5, 0.8, 0.1, ...]

         Estos números SIGNIFICAN algo:
         - "gato" y "felino" tienen vectores parecidos
         - "gato" y "avión" tienen vectores muy distintos
```

**Lista de representaciones en NLP:**

| Representación | ¿Qué convierte? | Resultado |
|----------------|-----------------|-----------|
| **One-Hot** | "gato" (palabra #53 de 10,000) | Vector [0,0,...,1,...,0] con 10,000 posiciones |
| **Word Embedding** | "gato" | Vector denso [0.2, -0.5, ...] de ~300 números |
| **Positional Encoding** | "posición 5 en la oración" | Vector que indica ubicación |
| **Bag of Words** | "el gato come" (documento) | [1, 1, 1, 0, 0, ...] conteo de palabras |

---

### TIPO 2: CAPAS (Tipos de Operación)

**¿Qué es?**
Son las **OPERACIONES MATEMÁTICAS** que transforman los datos. Pasan **DENTRO** de la red.

**Analogía:** Son las **piezas del motor**: pistones, válvulas, bujías. Cada una hace una operación específica.

**Ejemplo CNN (que conoces):**
```
CAPAS QUE YA CONOCES:
─────────────────────

Conv2D    →  Aplica filtros para detectar patrones (bordes, texturas)
MaxPool   →  Reduce el tamaño tomando el máximo de cada región
ReLU      →  Si el número es negativo, lo convierte en 0
Dense     →  Multiplica por una matriz de pesos (fully connected)
Dropout   →  Apaga neuronas al azar durante entrenamiento
```

**Capas equivalentes en NLP:**
```
CAPAS NUEVAS:
─────────────

RNN           →  Procesa secuencia paso a paso, tiene "memoria"
LSTM          →  Como RNN pero con mejor memoria a largo plazo
GRU           →  Como LSTM pero más simple (RECOMENDADA)
Self-Attention →  Cada palabra "mira" a todas las demás
Feed-Forward  →  Igual que Dense, multiplica por matriz de pesos
```

**La clave:** Una CAPA es una operación matemática con parámetros (pesos) que se entrenan.

| Capa (CNN) | Capa equivalente (NLP) | ¿Qué hace? |
|------------|------------------------|------------|
| Conv2D | - | Detecta patrones locales |
| Dense | Feed-Forward | Multiplica por matriz de pesos |
| - | RNN/LSTM/GRU | Procesa secuencias con memoria |
| - | Self-Attention | Relaciona todas las posiciones entre sí |

---

### TIPO 3: ARQUITECTURA (El Diseño)

**¿Qué es?**
Es el **PLANO** que dice qué capas usar y cómo conectarlas. Es una **receta**, no una operación.

**Analogía:** Es el **diseño del auto** (sedan, SUV, camioneta). Dice qué piezas usar y dónde ponerlas.

**Ejemplo CNN (que conoces):**

```
ARQUITECTURA "LeNet" (una receta específica):
─────────────────────────────────────────────
Conv2D(6 filtros) → MaxPool → Conv2D(16 filtros) → MaxPool → Dense(120) → Dense(84) → Dense(10)

ARQUITECTURA "VGG16" (otra receta):
───────────────────────────────────
Conv2D → Conv2D → MaxPool → Conv2D → Conv2D → MaxPool → ... (16 capas en total)

Ambas usan las MISMAS CAPAS (Conv2D, MaxPool, Dense)
Pero las ORGANIZAN de forma diferente.
```

**Arquitecturas en NLP:**

```
ARQUITECTURA "Seq2Seq" (una receta):
────────────────────────────────────
ENCODER: GRU → GRU → GRU  (procesa entrada)
              ↓
         [vector contexto]
              ↓
DECODER: GRU → GRU → GRU  (genera salida)


ARQUITECTURA "Transformer" (otra receta):
─────────────────────────────────────────
ENCODER: Self-Attention → Feed-Forward → Self-Attention → Feed-Forward
              ↓
         [contexto]
              ↓
DECODER: Masked-Self-Attention → Cross-Attention → Feed-Forward

Ambas son ENCODER-DECODER (misma idea general)
Pero usan CAPAS diferentes:
  - Seq2Seq usa: GRU
  - Transformer usa: Self-Attention + Feed-Forward
```

**La clave:** La ARQUITECTURA no tiene parámetros propios. Es solo instrucciones de cómo armar las capas.

---

### ¿Qué es ENCODER-DECODER exactamente?

**ENCODER-DECODER no es una arquitectura específica. Es un PATRÓN DE DISEÑO.**

Es como decir "auto con motor adelante y maletero atrás" - muchos autos siguen ese patrón (sedan, coupé, etc.) pero son autos diferentes.

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                        EL PATRÓN ENCODER-DECODER                              ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ENTRADA                      CUELLO                         SALIDA          ║
║   (cualquier                   DE                             (cualquier      ║
║    longitud)                   BOTELLA                         longitud)      ║
║                                                                               ║
║   ┌─────────────┐         ┌───────────┐         ┌─────────────┐              ║
║   │             │         │           │         │             │              ║
║   │   ENCODER   │ ──────▶ │  VECTOR   │ ──────▶ │   DECODER   │              ║
║   │             │         │ (tamaño   │         │             │              ║
║   │  "Lee" y    │         │  fijo)    │         │  "Genera"   │              ║
║   │  comprime   │         │           │         │  la salida  │              ║
║   │             │         │           │         │             │              ║
║   └─────────────┘         └───────────┘         └─────────────┘              ║
║                                                                               ║
║   Ejemplo: "Bonjour le monde" ──▶ [vector] ──▶ "Hello world"                  ║
║            (3 palabras)          (256 nums)    (2 palabras)                   ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

**¿Por qué existe este patrón?**

Problema: Quiero convertir una secuencia en OTRA secuencia de DIFERENTE longitud.
- Traducir: "Hello" (1 palabra) → "Hola" (1) ✓
- Traducir: "How are you?" (3 palabras) → "¿Cómo estás?" (2 palabras) ✗

Una red normal no puede hacer esto. Necesitas:
1. Algo que "lea" toda la entrada y la resuma (ENCODER)
2. Algo que genere la salida a partir del resumen (DECODER)

**Relación entre los términos:**

```
ENCODER-DECODER (el patrón/concepto)
        │
        ├── Seq2Seq (implementación con RNN/LSTM/GRU)
        │
        └── Transformer (implementación con Self-Attention)
```

| Término | ¿Qué es? | Analogía con autos |
|---------|----------|-------------------|
| **Encoder-Decoder** | Patrón de diseño | "Auto con motor adelante" |
| **Seq2Seq** | Arquitectura específica que sigue el patrón | "Toyota Corolla" |
| **Transformer** | Otra arquitectura que sigue el patrón | "Tesla Model 3" |

**En código, la diferencia sería:**

```python
# Seq2Seq: Encoder-Decoder implementado con GRU
encoder = GRU(256)
decoder = GRU(256)

# Transformer: Encoder-Decoder implementado con Self-Attention
encoder = SelfAttention(256) + FeedForward(256)
decoder = MaskedSelfAttention(256) + CrossAttention(256) + FeedForward(256)

# Ambos siguen el MISMO PATRÓN:
# entrada → encoder → vector contexto → decoder → salida
```

---

## Resumen: Las 3 preguntas que distinguen TIPO 1, 2 y 3

| Pregunta | Si la respuesta es... | Es TIPO... |
|----------|----------------------|------------|
| ¿Cómo convierto mi input en números? | Word Embedding, One-Hot, Tensor | **1 (Representación)** |
| ¿Qué operación matemática hago? | RNN, LSTM, Self-Attention, Conv2D | **2 (Capa)** |
| ¿En qué orden organizo las operaciones? | Transformer, Seq2Seq, VGG, ResNet | **3 (Arquitectura)** |

---

## Ejemplo completo: Cómo se usan los 3 tipos juntos

```
TAREA: Traducir "Hello world" al español
───────────────────────────────────────

PASO 1 - REPRESENTACIÓN (Tipo 1):
─────────────────────────────────
"Hello" → Word Embedding → [0.2, -0.1, 0.8, ...]
"world" → Word Embedding → [0.5, 0.3, -0.2, ...]
Posición 1 → Positional Encoding → [0.0, 1.0, 0.0, ...]
Posición 2 → Positional Encoding → [0.84, 0.54, 0.84, ...]

PASO 2 - ARQUITECTURA (Tipo 3) dice qué hacer:
──────────────────────────────────────────────
"Usa un Transformer:
 - Primero pasa por el Encoder (6 bloques)
 - Luego pasa por el Decoder (6 bloques)
 - Cada bloque tiene Self-Attention + Feed-Forward"

PASO 3 - LAS CAPAS (Tipo 2) hacen el trabajo:
─────────────────────────────────────────────
[vectores de Hello, world]
        ↓
   Self-Attention  ← CAPA: cada palabra mira a la otra
        ↓
   Feed-Forward    ← CAPA: transforma los vectores
        ↓
   (repetir 6 veces)
        ↓
   [representación del encoder]
        ↓
   Masked-Self-Attention  ← CAPA: genera palabra por palabra
        ↓
   Cross-Attention        ← CAPA: mira el encoder
        ↓
   Feed-Forward           ← CAPA: transforma
        ↓
SALIDA: "Hola mundo"
```

---

## Los otros 4 tipos (explicación breve)

### TIPO 4: Técnicas de Entrenamiento

**¿Qué son?**
Son estrategias que usamos **solo durante entrenamiento** para que el modelo aprenda mejor. No se usan cuando el modelo ya está funcionando.

| Técnica | ¿Cuál es el problema? | ¿Cómo lo resuelve? |
|---------|----------------------|-------------------|
| **Teacher Forcing** | Durante entrenamiento del decoder, ¿qué palabra le damos como input? | Le damos la palabra CORRECTA (no la que predijo) |
| **Scheduled Sampling** | Teacher Forcing hace que el modelo no aprenda de sus errores | A veces damos la correcta, a veces la que predijo |
| **Masked Attention** | El modelo puede "hacer trampa" mirando palabras futuras | Bloqueamos la vista hacia el futuro |
| **BPTT** | ¿Cómo calculamos gradientes en secuencias muy largas? | Usamos una ventana y calculamos gradientes por partes |

**¿Por qué "Masked Attention" y el problema del futuro?**

Este es el concepto que más confunde. Aquí está la explicación completa:

```
CONTEXTO: Estamos ENTRENANDO un modelo para generar texto.
───────────────────────────────────────────────────────────

SITUACIÓN DE ENTRENAMIENTO:
───────────────────────────
Tenemos la oración completa de antemano:
   "El gato come pescado"

Le pedimos al modelo que PREDIGA cada palabra:
   Dado ""           → predice "El"
   Dado "El"         → predice "gato"
   Dado "El gato"    → predice "come"
   Dado "El gato come" → predice "pescado"

EL PROBLEMA:
────────────
En Self-Attention, el modelo ve TODA la oración al mismo tiempo.
Entonces cuando le pedimos que prediga "gato", ¡ya puede VER "gato"!
Eso es hacer trampa. No aprende nada.

LA SOLUCIÓN - MASKED ATTENTION:
───────────────────────────────
Ponemos una "máscara" que BLOQUEA la vista hacia adelante:

   Cuando predice "El":      solo ve: [         ]  (nada)
   Cuando predice "gato":    solo ve: [El       ]
   Cuando predice "come":    solo ve: [El gato  ]
   Cuando predice "pescado": solo ve: [El gato come]

Así el modelo aprende a predecir SIN ver el futuro.

¿POR QUÉ IMPORTA EL "TIEMPO"?
─────────────────────────────
Hablamos de "futuro" y "pasado" porque generar texto es un proceso
en el TIEMPO:

   Tiempo 1: generas "El"
   Tiempo 2: generas "gato"
   Tiempo 3: generas "come"
   Tiempo 4: generas "pescado"

"Futuro" = palabras que aún no has generado
"Pasado" = palabras que ya generaste

En entrenamiento tienes TODA la oración, pero simulas que no la tienes.
En uso real (inferencia), realmente NO tienes el futuro.
```

---

### TIPO 5: Trucos Arquitectónicos

**¿Qué son?**
Son modificaciones que se agregan a las arquitecturas para que funcionen mejor. Son como "mejoras" o "parches".

| Truco | ¿Qué problema resuelve? | ¿Cómo funciona? |
|-------|------------------------|-----------------|
| **Skip Connections** | Gradientes se desvanecen en redes profundas | Agregar "atajos" para que la información fluya directo |
| **Layer Normalization** | El entrenamiento es inestable | Normalizar los valores en cada capa |
| **Gradient Clipping** | Gradientes explotan (se vuelven gigantes) | Si el gradiente es muy grande, lo recortas |

---

### TIPO 6: Problemas/Fenómenos

**¿Qué son?**
Son cosas que **ocurren** durante el entrenamiento. No son técnicas ni bloques, son situaciones.

| Fenómeno | ¿Qué pasa? | ¿Es malo? |
|----------|-----------|-----------|
| **Vanishing Gradient** | Los gradientes se vuelven casi cero | Sí, el modelo no aprende |
| **Exploding Gradient** | Los gradientes se vuelven gigantes | Sí, el modelo explota (NaN) |
| **Double Descent** | El error baja, sube, y vuelve a bajar | No necesariamente, es un fenómeno interesante |
| **Cuello de botella** | Toda la información pasa por un punto único | Sí, se pierde información |

---

### TIPO 7: Tareas/Aplicaciones

**¿Qué son?**
Son los PROBLEMAS que queremos resolver. Todo lo demás (bloques, arquitecturas, técnicas) son HERRAMIENTAS para resolver estas tareas.

| Tarea | ¿Qué hace? | ¿Qué arquitectura usa? |
|-------|-----------|----------------------|
| **Modelo de Lenguaje** | Predecir la siguiente palabra | RNN, LSTM, Transformer |
| **Traducción** | Texto en idioma A → texto en idioma B | Seq2Seq, Transformer |
| **Resumen** | Texto largo → texto corto | Seq2Seq, Transformer |
| **Clasificación de sentimiento** | Texto → positivo/negativo | RNN + clasificador, BERT |
| **Generación de texto** | Prompt → texto generado | Transformer (GPT) |

---

## Tabla Resumen: ¿Qué es cada cosa?

| Concepto | TIPO | Equivalente en CNN |
|----------|------|-------------------|
| **REPRESENTACIÓN DE DATOS** | | |
| Word Embeddings | 1 - Representación | Como convertir foto a tensor |
| One-Hot Encoding | 1 - Representación | Como label a vector [0,0,1,0] |
| Positional Encoding | 1 - Representación | (no hay equivalente en CNN) |
| Bag of Words | 1 - Representación | (no hay equivalente en CNN) |
| **CAPAS (operaciones)** | | |
| RNN | 2 - Capa | Como Conv2D o Dense |
| LSTM | 2 - Capa | Como Conv2D o Dense |
| GRU | 2 - Capa | Como Conv2D o Dense |
| Self-Attention | 2 - Capa | Como Conv2D o Dense |
| Multi-Head Attention | 2 - Capa | Como Conv2D o Dense |
| Feed-Forward | 2 - Capa | = Dense (es lo mismo) |
| **PATRÓN DE DISEÑO** | | |
| Encoder-Decoder | PATRÓN (no arquitectura) | Como "tener motor adelante" en autos |
| **ARQUITECTURAS (diseños)** | | |
| Seq2Seq | 3 - Arquitectura (usa patrón Enc-Dec con RNN) | Como "VGG" o "LeNet" |
| Transformer | 3 - Arquitectura (usa patrón Enc-Dec con Attention) | Como "ResNet" |
| **TÉCNICAS DE ENTRENAMIENTO** | | |
| Teacher Forcing | 4 - Técnica | Como Data Augmentation |
| Masked Attention | 4 - Técnica | Como Dropout |
| BPTT | 4 - Técnica | Como Backpropagation normal |
| **TRUCOS ARQUITECTÓNICOS** | | |
| Skip Connections | 5 - Truco | = Skip Connections (es lo mismo) |
| Layer Normalization | 5 - Truco | Como BatchNorm |
| **PROBLEMAS/FENÓMENOS** | | |
| Vanishing Gradient | 6 - Problema | = Vanishing Gradient (mismo problema) |
| Double Descent | 6 - Fenómeno | = Double Descent (mismo fenómeno) |
| **TAREAS** | | |
| Modelo de Lenguaje | 7 - Tarea | Como "Clasificación de imágenes" |
| Traducción | 7 - Tarea | (no hay equivalente directo) |

---

## Diagrama Final: Cómo se relacionan los tipos

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   QUIERO RESOLVER UNA TAREA (ej: traducción)                              ║
║                          │                                                ║
║                          ▼                                                ║
║   ELIJO UNA ARQUITECTURA (ej: Transformer)                                ║
║                          │                                                ║
║                          ▼                                                ║
║   LA ARQUITECTURA USA BLOQUES (ej: Self-Attention + Feed-Forward)         ║
║                          │                                                ║
║                          ▼                                                ║
║   LOS BLOQUES NECESITAN REPRESENTACIONES (ej: Word Embeddings + Pos.Enc.) ║
║                          │                                                ║
║                          ▼                                                ║
║   DURANTE ENTRENAMIENTO USO TÉCNICAS (ej: Teacher Forcing, Masking)       ║
║                          │                                                ║
║                          ▼                                                ║
║   AGREGO TRUCOS PARA QUE FUNCIONE (ej: Skip Connections, LayerNorm)       ║
║                          │                                                ║
║                          ▼                                                ║
║   ENFRENTO PROBLEMAS (ej: Vanishing Gradient) → LOS RESUELVO              ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```
