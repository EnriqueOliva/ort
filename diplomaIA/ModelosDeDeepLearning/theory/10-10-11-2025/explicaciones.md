# Clase 10 (10 de Noviembre 2025) - Deep Learning
## Modelos de Lenguaje y Seq2Seq

---

# UBICACIÓN EN EL CURSO: ¿De dónde venimos y hacia dónde vamos?

```
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                    SEGUNDA MITAD DEL CURSO - MAPA DE CLASES                              ║
╠══════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                          ║
║  CLASE 8 (27-Oct) ─────────────────────────────────────────────────────────────────────  ║
║  │  • Vanishing/Exploding Gradient (el problema)                                         ║
║  │  • Skip Connections / ResNet / DenseNet (la solución para CNNs)                       ║
║  │  • Introducción a NLP: Tokenización, Bag of Words, TF-IDF                             ║
║  │  • Word Embeddings: Word2Vec (CBOW y Skip-gram)                                       ║
║  │                                                                                       ║
║  ▼  CONEXIÓN: Ya sabemos representar palabras como vectores (embeddings)                 ║
║                                                                                          ║
║  CLASE 9 (03-Nov) ────────────────────────────────────────────────────────────────────   ║
║  │  • RNN Vanilla: cómo procesar SECUENCIAS (3 matrices: U, V, W)                        ║
║  │  • Vanishing gradient en RNN (demostrado con Copying Task)                            ║
║  │  • LSTM (4 compuertas, Cell + Hidden states)                                          ║
║  │  • GRU (2 compuertas, RECOMENDADA por el profesor)                                    ║
║  │  • Arquitecturas: Bidireccional, Stacked                                              ║
║  │                                                                                       ║
║  ▼  CONEXIÓN: Ya tenemos modelos que procesan secuencias y recuerdan a largo plazo       ║
║                                                                                          ║
║  ════════════════════════════════════════════════════════════════════════════════════    ║
║  ║ CLASE 10 (10-Nov) ◄─── ESTÁS AQUÍ                                              ║      ║
║  ║  • Modelos de Lenguaje: predecir la siguiente palabra                          ║      ║
║  ║  • Procesos Estocásticos y Cadenas de Markov (base matemática)                 ║      ║
║  ║  • N-gramas: el enfoque clásico (y sus problemas)                              ║      ║
║  ║  • MLP + Embeddings: solución neuronal con ventana fija                        ║      ║
║  ║  • Encoder-Decoder / Seq2Seq: diferentes longitudes entrada/salida             ║      ║
║  ║  • Teacher Forcing y Scheduled Sampling: cómo entrenar                         ║      ║
║  ════════════════════════════════════════════════════════════════════════════════════    ║
║  │                                                                                       ║
║  ▼  PROBLEMA: El contexto se comprime en UN SOLO vector (cuello de botella)              ║
║                                                                                          ║
║  CLASE 11 (17-Nov) ────────────────────────────────────────────────────────────────────  ║
║  │  • Attention de Bahdanau: contexto DINÁMICO (miramos TODO el encoder)                 ║
║  │  • Self-Attention: cada palabra mira a TODAS las demás                                ║
║  │  • Query, Key, Value: la terminología moderna                                         ║
║  │  • Multi-Head Attention: varias "cabezas" mirando relaciones distintas               ║
║  │  • Introducción a Transformers                                                        ║
║  │                                                                                       ║
║  ▼  VENTAJA: Ya no necesitamos procesar secuencialmente                                  ║
║                                                                                          ║
║  CLASE 12 (24-Nov) ────────────────────────────────────────────────────────────────────  ║
║     • Transformers en detalle: arquitectura completa                                     ║
║     • Masked Self-Attention: no mirar el futuro                                          ║
║     • Positional Encoding: cómo codificar la posición                                    ║
║     • Entrenamiento vs Inferencia                                                        ║
║                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
```

---

## MAPA CONCEPTUAL DE ESTA CLASE: ¿Cómo se conectan los temas?

```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                    PROBLEMA CENTRAL: PREDECIR LA SIGUIENTE PALABRA                   ║
║                                                                                      ║
║    Dado: "necesito un vaso de..."  →  ¿Cuál es la siguiente palabra?                ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
                                          │
        ┌─────────────────────────────────┼─────────────────────────────────┐
        │                                 │                                 │
        ▼                                 ▼                                 ▼
╔═══════════════════╗          ╔═══════════════════╗          ╔═══════════════════╗
║  BASE MATEMÁTICA  ║          ║ ENFOQUE CLÁSICO   ║          ║ ENFOQUE NEURONAL  ║
║                   ║          ║  (Estadístico)    ║          ║  (Paramétrico)    ║
║ • Proceso         ║          ║                   ║          ║                   ║
║   Estocástico     ║───────▶  ║ • N-gramas        ║───────▶  ║ • MLP + Embedding ║
║ • Cadenas de      ║          ║ • Conteo de       ║          ║ • RNN/LSTM/GRU    ║
║   Markov          ║          ║   frecuencias     ║          ║ • Encoder-Decoder ║
╚═══════════════════╝          ╚═══════════════════╝          ╚═══════════════════╝
                                         │                              │
                                         ▼                              │
                               ╔═══════════════════╗                    │
                               ║    PROBLEMAS:     ║                    │
                               ║ • Combinatoria    ║                    │
                               ║   explosiva       ║ ──────────────────▶│
                               ║ • Datos esparsos  ║    (los resuelve)  │
                               ║ • Ventana fija    ║                    │
                               ╚═══════════════════╝                    │
                                                                        │
        ┌───────────────────────────────────────────────────────────────┘
        │
        ▼
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                    EVOLUCIÓN DE SOLUCIONES (¡CUIDADO CON LOS TIPOS!)                 ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                      ║
║   ⚠️  NO es una cadena donde cada cosa "reemplaza" a la anterior.                    ║
║       Son TIPOS diferentes de cosas que se COMBINAN.                                 ║
║                                                                                      ║
║   ┌─────────────────────────────────────────────────────────────────────────────┐    ║
║   │  NIVEL 1: ¿CÓMO PREDIGO LA SIGUIENTE PALABRA? (enfoques/capas)              │    ║
║   │  ───────────────────────────────────────────────────────────────            │    ║
║   │                                                                             │    ║
║   │  N-GRAMAS ──▶ MLP + EMBEDDING ──▶ RNN ──▶ LSTM/GRU                          │    ║
║   │  (contar)     (ventana fija)     (secuencial)  (mejor memoria)              │    ║
║   │                                                      │                      │    ║
║   │                                                      │ estas CAPAS          │    ║
║   │                                                      │ se USAN dentro de... │    ║
║   │                                                      ▼                      │    ║
║   └─────────────────────────────────────────────────────────────────────────────┘    ║
║                                                                                      ║
║   ┌─────────────────────────────────────────────────────────────────────────────┐    ║
║   │  NIVEL 2: ¿CÓMO ORGANIZO LAS CAPAS? (patrón + arquitectura)                 │    ║
║   │  ──────────────────────────────────────────────────────────                 │    ║
║   │                                                                             │    ║
║   │  ┌─────────────────────────────────────────────────────────────────────┐   │    ║
║   │  │  PATRÓN: Encoder-Decoder                                            │   │    ║
║   │  │  (idea: comprimir entrada → generar salida de diferente longitud)   │   │    ║
║   │  │                        │                                            │   │    ║
║   │  │      ┌─────────────────┴─────────────────┐                          │   │    ║
║   │  │      ▼                                   ▼                          │   │    ║
║   │  │  ┌───────────────────┐           ┌───────────────────┐              │   │    ║
║   │  │  │ ARQUITECTURA:     │           │ ARQUITECTURA:     │              │   │    ║
║   │  │  │ Seq2Seq           │           │ Transformer       │              │   │    ║
║   │  │  │ (usa RNN/LSTM/GRU │           │ (usa Self-        │              │   │    ║
║   │  │  │  como capas)      │           │  Attention)       │              │   │    ║
║   │  │  │                   │           │                   │              │   │    ║
║   │  │  │ CLASE 10 ◄────────┤           │ CLASES 11-12      │              │   │    ║
║   │  │  └───────────────────┘           └───────────────────┘              │   │    ║
║   │  └─────────────────────────────────────────────────────────────────────┘   │    ║
║   └─────────────────────────────────────────────────────────────────────────────┘    ║
║                                                                                      ║
║   RESUMEN:                                                                           ║
║   • LSTM/GRU son CAPAS (se usan DENTRO de arquitecturas, no se "reemplazan")         ║
║   • Encoder-Decoder es un PATRÓN (idea de diseño)                                    ║
║   • Seq2Seq es una ARQUITECTURA (implementa Enc-Dec usando LSTM/GRU como capas)      ║
║   • Transformer es OTRA ARQUITECTURA (implementa Enc-Dec usando Attention)           ║
║                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

---

## SECCIÓN A: ¿Qué es un Modelo de Lenguaje?

### Definición simple

Un **modelo de lenguaje** predice la siguiente palabra dada una secuencia.

```
Entrada:  "necesito un vaso de..."
Salida:   P(agua) = 0.4,  P(cerveza) = 0.3,  P(leche) = 0.1, ...
```

### Importancia actual

> "Hoy por hoy estos son en su bajo nivel redes neuronales que aproximan modelos de lenguaje."

Los LLMs como ChatGPT son, en esencia, **modelos de lenguaje neuronales muy potentes**.

### Historia: Esto no es nuevo

Viene desde **Shannon** (años 1940-1950):

> "Shannon cuando produjo la entropía de Shannon, modelaba texto con cadenas de Markov y en el fondo un modelo de lenguaje no es algo demasiado diferente a una cadena de Markov."

**¿Qué cambió?** El poder de cómputo y la cantidad de datos.

---

## SECCIÓN B: Base Matemática - Procesos Estocásticos

### ¿Qué es un proceso estocástico?

> "Un proceso estocástico es una sucesión de variables aleatorias."

**Traducción simple:** Una secuencia de eventos donde cada uno es aleatorio.

### En el lenguaje:
- Cada **palabra** = una **variable aleatoria**
- Las palabras vienen una tras otra = **tiempo discreto**
- Cada palabra puede ser cualquiera del **vocabulario**

### Tipos de procesos (mencionados en clase):

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **i.i.d.** | Cada evento es independiente del pasado | Ruido puro |
| **Series temporales** | Valores reales en el tiempo | Temperatura |
| **Cadenas de Markov** | El futuro depende solo del presente | Lenguaje (simplificado) |

---

## SECCIÓN C: Cadenas de Markov - El Concepto Clave

### La propiedad de Markov

> "Condicionado al presente, el futuro y el pasado son independientes."

**Traducción simple:** Si sabes el **presente**, el **pasado** no te da información extra sobre el **futuro**.

### Dos formas de entenderlo:

```
FORMA 1: P(siguiente | TODO el pasado) = P(siguiente | SOLO el último)

FORMA 2: Presente conocido → Pasado y futuro son INDEPENDIENTES
```

### Ventanas más grandes

Puedes generalizar: en vez de mirar solo la última palabra, miras las últimas N:

```
Markov orden 1:  P(siguiente | última palabra)
Markov orden 2:  P(siguiente | últimas 2 palabras)
Markov orden 3:  P(siguiente | últimas 3 palabras)
```

### Conexión con RL (para quienes vieron agentes):

> "En agentes ven Markov Decision Process (MDP), que una vez que uno elige una política es una cadena de Markov."

---

## SECCIÓN D: N-gramas - El Enfoque Clásico

### ¿Qué son los N-gramas?

> "Los n-gramas es una secuencia de n tokens consecutivos."

Es mirar una **ventana de N palabras** para predecir la siguiente.

### Ejemplo con "I need a glass of"

| N | Nombre | Ejemplos |
|---|--------|----------|
| 1 | Unigrama | "I", "need", "a", "glass", "of" |
| 2 | Bigrama | "I need", "need a", "a glass", "glass of" |
| 3 | Trigrama | "I need a", "need a glass", "a glass of" |

### ¿Cómo se calcula la probabilidad? (Conteo)

```
P(water | "a glass of") = Conteo("a glass of water") / Conteo("a glass of")
```

**Ejemplo numérico:**
- "a glass of" aparece 1000 veces
- "a glass of water" aparece 400 veces
- "a glass of milk" aparece 100 veces

Entonces:
- P(water) = 400/1000 = **0.4**
- P(milk) = 100/1000 = **0.1**

### Relación con ventana de contexto moderna

Un estudiante preguntó si esto es como la ventana de contexto de ChatGPT:

> "Se puede pensar, sí."

**Diferencia:** Los LLMs modernos tienen ventanas de ~2 millones de tokens. Los n-gramas clásicos usaban N = 3, 4, 5.

---

## SECCIÓN E: Problemas del Enfoque Clásico

### PROBLEMA 1: Combinatoria explosiva

> "La combinatoria es gigante y entonces muy probablemente tengamos pocos conteos de ocurrencias."

Si tienes vocabulario de 50,000 palabras:
- Bigramas posibles: 50,000² = 2.5 mil millones
- Trigramas posibles: 50,000³ = 125 trillones

### PROBLEMA 2: Datos esparsos

> "Cada grama aparece muy poquitas veces en los datos, entonces se vuelve muy difícil el conteo."

La mayoría de n-gramas posibles **nunca aparecen** en tus datos.

### PROBLEMA 3: Dilema del tamaño de N

```
┌──────────────────────────────────────────────────────────────┐
│  N muy CHICO                    N muy GRANDE                 │
│  ↓                              ↓                            │
│  Solo tendencias cortas         Datos muy esparsos           │
│  "débil"                        Nunca viste esa secuencia    │
└──────────────────────────────────────────────────────────────┘
```

### PROBLEMA 4: Siempre hay frases más largas

> "Siempre hay una oración que sea más grande que ese N."

No importa qué N elijas, algunas frases necesitarán más contexto.

### PROBLEMA 5: Orden flexible en idiomas

> "En lenguajes donde sea flexible el orden de las palabras, aumenta las combinaciones."

"El gato come" y "come el gato" son n-gramas distintos pero significan lo mismo.

---

## SECCIÓN F: Solución 1 - MLP con Embeddings

### La idea

> "Una idea natural es hacer eso de forma paramétrica con, por ejemplo, una red, un MLP."

En vez de **contar**, usamos una **red neuronal** que aprende la función.

### Arquitectura

```
┌─────────────────────────────────────────────────────────────────────┐
│                        MLP PARA MODELO DE LENGUAJE                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ENTRADA: N palabras (ventana fija)                                │
│      │                                                              │
│      ▼                                                              │
│   ┌─────────────────────────────────────┐                          │
│   │  EMBEDDING: cada palabra → vector   │                          │
│   │  Ej: 4 palabras × 4 dims = 16 dims  │                          │
│   └─────────────────────────────────────┘                          │
│      │                                                              │
│      ▼ (concatenar todos)                                           │
│   ┌─────────────────────────────────────┐                          │
│   │  CAPAS OCULTAS (densas + ReLU)      │                          │
│   └─────────────────────────────────────┘                          │
│      │                                                              │
│      ▼                                                              │
│   ┌─────────────────────────────────────┐                          │
│   │  SOFTMAX: |vocabulario| salidas     │  ← clasificación         │
│   └─────────────────────────────────────┘                          │
│                                                                     │
│   SALIDA: P(palabra_i) para cada palabra del vocabulario            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### ¿Cuántas salidas tiene la última capa?

> "El tamaño del vocabulario."

Es un **problema de clasificación** con tantas clases como palabras posibles.

### ¿Qué resuelven los Embeddings?

> "Los embeddings permiten olvidarse del problema de la combinatoria."
> "El embedding compacta esa información en un vector de tamaño más chico, preservando cierta estructura."

**Ventajas:**
1. Compactan información
2. Preservan semántica (palabras similares → vectores similares)
3. Eliminan datos esparsos

### ¿Pueden ser preentrenados?

> "Podés usar un embedding que ya esté preentrenado (Word2Vec, GloVe) o entrenarlos como parte del modelo."

### PROBLEMA que queda: Ventana fija

> "Todavía tiene problemas: la ventana siempre es chica porque agrandar la ventana implica agrandar la cantidad de pesos."

---

## SECCIÓN G: Solución 2 - Redes Recurrentes (RNN/LSTM/GRU)

### La pregunta del profesor

> "¿Qué se les ocurre como alternativa al MLP?"

Respuesta de estudiante: **"Una recurrente"**

### Ventajas sobre MLP

| Ventaja | Explicación |
|---------|-------------|
| **Parámetros fijos** | "La cantidad de parámetros no va a escalar con el tamaño de la ventana." |
| **Cualquier largo** | "Una red recurrente puede consumir secuencias de largo variado." |
| **Memoria larga** | "Las LSTM y GRU aprenden dependencias bastante largas." |
| **Comparten pesos** | "Se aprende una sola función, no una por posición." |
| **Más eficientes** | Para N muy grande, son más rápidas que MLP. |

### Dominaron hasta los Transformers

> "Fueron quienes dominaron el procesamiento de lenguaje natural hasta que aparecieron los Transformers."

---

## SECCIÓN H: RNN vs Transformers - ¿Por qué usar cada uno?

**📌 NOTA:** En esta clase el profesor respondió preguntas sobre Transformers pero sin entrar en detalles técnicos. Los Transformers se estudiarán en profundidad en las **clases 11 y 12**. Aquí solo vemos la comparación general.

### La pregunta del estudiante

> "¿Por qué se sigue usando [RNN] si están los Transformers?"

### Respuesta clave: ESCALABILIDAD, no desempeño

> "Los Transformers no es por un problema de desempeño, es por un problema de escalabilidad."

### ¿Qué introdujeron los Transformers?

> "Los Transformers introdujeron la capacidad de paralelización de forma mucho más eficiente."
> "Entrenar una red con todo Wikipedia con una recurrente era imposible. Con Transformer se puede."

### Analogía del tractor vs la pala

> "Es como un tractor para superficies grandes. Pero si vos tenés tu jardincito, con una palita mucho mejor."

### ¿Cuándo usar cada uno?

| Situación | Usar |
|-----------|------|
| Problemas de gran escala, muchos datos | **Transformer** |
| Series temporales | **RNN/LSTM/GRU** |
| Tareas sencillas de texto | **RNN** (más barato) |
| Recursos limitados | **RNN** |
| Quieres aprovechar modelos preentrenados | **Transformer** |

### Modelos específicos vs generales

> "Hay modelos más sencillos que funcionan mejor que un modelo general. Hay modelos pequeños que pueden resolver problemas de razonamiento mejor que un modelo gigante."

---

## SECCIÓN I: Modelo de Lenguaje con RNN

### Arquitectura desplegada

```
┌──────────────────────────────────────────────────────────────────────┐
│                   RNN COMO MODELO DE LENGUAJE                        │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  h₀ ──▶ ┌─────┐ ──▶ h₁ ──▶ ┌─────┐ ──▶ h₂ ──▶ ┌─────┐ ──▶ h₃       │
│         │ RNN │            │ RNN │            │ RNN │                │
│  x₁ ──▶ └─────┘ ──▶ o₁    └─────┘ ──▶ o₂    └─────┘ ──▶ o₃        │
│         "the"       ↓      "cat"       ↓      "sat"       ↓         │
│                  softmax            softmax            softmax       │
│                     ↓                  ↓                  ↓          │
│                 P(cat|the)       P(sat|the,cat)   P(on|the,cat,sat) │
│                                                                      │
│  Donde:                                                              │
│  • hᵢ = estado oculto (hidden) → memoria de lo anterior             │
│  • xᵢ = palabra de entrada (pasada por embedding)                   │
│  • oᵢ = salida → pasa por softmax → distribución de probabilidades  │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### Paso a paso

1. **h₀** = estado inicial (ceros o random)
2. Entra la primera palabra → se procesa con h₀
3. Se produce: **output** (predicción) + **nuevo hidden**
4. El hidden pasa al siguiente paso
5. Se repite para cada palabra

### Cálculo del error

> "El error se calcula sumando cada tiempo."

Se suma el error de predicción en cada paso temporal (cross-entropy).

---

## SECCIÓN J: El Problema de Longitudes Diferentes

### El problema

> "Una red recurrente solo tiene la habilidad de generar algo del mismo largo que [la entrada]."

**Ejemplo:** Quiero traducir "Hello" (1 palabra) → "Hola" (1 palabra). OK.
Pero "How are you?" (3 palabras) → "¿Cómo estás?" (2 palabras). **Problema.**

### La solución: Encoder-Decoder

```
┌──────────────────────────────────────────────────────────────────────┐
│                      IDEA DEL ENCODER-DECODER                        │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│    ENTRADA              ESPACIO LATENTE            SALIDA            │
│  (cualquier largo)        (fijo)             (cualquier largo)       │
│                                                                      │
│  ┌───────────┐         ┌─────────┐          ┌─────────────┐         │
│  │ "Bonjour" │         │         │          │  "Hello"    │         │
│  │ "le"      │ ──────▶ │ CONTEXTO│ ───────▶ │  "world"    │         │
│  │ "monde"   │         │ (vector)│          │             │         │
│  └───────────┘         └─────────┘          └─────────────┘         │
│       ↑                     ↑                     ↑                  │
│    ENCODER              Dimensión             DECODER                │
│   (comprime)              fija              (expande)                │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## SECCIÓN K: Encoder-Decoder - La Arquitectura

### La idea genial

> "La primera vez que vi esto a mí me pareció una idea estupenda."

> "Codificar algo a un espacio común y después descodificarlo permite hacer cosas: codificar texto y descodificarlo en imagen, o al revés."

### Aplicaciones posibles

| Entrada | Salida | Aplicación |
|---------|--------|------------|
| Texto francés | Texto inglés | Traducción |
| Texto largo | Texto corto | Resumen |
| Audio | Texto | Transcripción |
| Imagen | Texto | Image captioning |
| Texto | Imagen | Generación de imágenes |
| Pregunta | Respuesta | Q&A |

### El Encoder

**Objetivo:** Generar un **vector de contexto** que resume la secuencia.

```
┌──────────────────────────────────────────────────────────────────────┐
│                            ENCODER                                   │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   Entrada: "Bonjour" "le" "monde" <EOS>                             │
│                │       │      │      │                               │
│                ▼       ▼      ▼      ▼                               │
│            ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                          │
│   h₀ ────▶│ GRU │─▶│ GRU │─▶│ GRU │─▶│ GRU │─────▶ CONTEXTO         │
│            └─────┘ └─────┘ └─────┘ └─────┘         (hidden final)   │
│               │       │       │       │                              │
│               ▼       ▼       ▼       ▼                              │
│              (o₁)    (o₂)    (o₃)    (o₄)  ← estos se TIRAN         │
│                                                                      │
│   Salida: Solo el HIDDEN FINAL (el contexto)                        │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### Sobre One-Hot Encoding

> "Un label encoding no tiene sentido. Porque qué quiere decir 85 - 2... confundís el modelo si lo hacés tipo número entero."

Las palabras se representan como **one-hot** (vector con un 1 en la posición de la palabra, resto 0), luego pasan por embedding.

### El Decoder

**Objetivo:** Generar la secuencia de salida a partir del contexto.

```
┌──────────────────────────────────────────────────────────────────────┐
│                            DECODER                                   │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   CONTEXTO ────────────────────────────────────────────────┐        │
│      │                                                      │        │
│      ▼                                                      ▼        │
│   ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐                         │
│   │ GRU │──▶ │ GRU │──▶ │ GRU │──▶ │ GRU │                         │
│   └─────┘    └─────┘    └─────┘    └─────┘                         │
│      │          │          │          │                              │
│      ▼          ▼          ▼          ▼                              │
│   softmax    softmax    softmax    softmax                          │
│      │          │          │          │                              │
│      ▼          ▼          ▼          ▼                              │
│   "Hello"    "world"    <EOS>      (para)                           │
│                                                                      │
│      ▲          ▲          ▲                                        │
│   <SOS>      "Hello"    "world"   ← INPUTS durante entrenamiento    │
│              (real)     (real)      (Teacher Forcing)               │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### El Decoder es como un modelo de lenguaje

> "El decoder es como un language model."

Es un modelo de lenguaje **condicionado al contexto** del encoder.

---

## SECCIÓN L: Seq2Seq - El Problema General

### Definición

> "El problema del Seq2Seq es aprender a partir de una secuencia de entrada una secuencia de salida, donde pueden tener longitudes diferentes."

### Es una generalización

> "Generaliza lo que sería un language model. El language model predice un solo Y₁ que es el siguiente. Seq2Seq predice toda una secuencia."

### Desafíos

1. **Longitudes diferentes** → Encoder-Decoder lo resuelve
2. **Orden diferente en idiomas** → RNN puede manejarlo
3. **Referencias a información lejana** → LSTM/GRU tienen memoria
4. **Definir inicio y fin** → Tokens especiales `<SOS>` y `<EOS>`

---

## SECCIÓN M: Tokens Especiales

### ¿Para qué sirven?

> "Se necesitan definir un inicio y un fin claro."

### Los tokens

| Token | Significado | Dónde se usa |
|-------|-------------|--------------|
| `<SOS>` o `<BOS>` | Start/Begin of Sequence | Inicio del decoder |
| `<EOS>` | End of Sequence | Final del encoder y decoder |

### En inferencia

> "El decoder va recibiendo el token de start y luego utiliza sus propios outputs hasta que produzca el end of sequence."

### Problema potencial

> "Podría quedarse generando y no generar nunca el end of sequence."

Por eso se pone un **límite máximo de longitud**.

---

## SECCIÓN N: Teacher Forcing

### ¿Qué es?

Durante entrenamiento, en cada paso le pasamos la **palabra correcta** (no la que predijo).

### Las dos alternativas

| Modo | Input del decoder | Cuándo |
|------|-------------------|--------|
| **Teacher Forcing** | Palabra real (ground truth) | Entrenamiento |
| **Free Running** | Lo que predijo el modelo | Inferencia |

### El problema de solo usar Teacher Forcing

> "No es la mejor forma de entrenar siempre usando Teacher Forcing."

### Analogía de la bicicleta

> "Es como cuando le enseñas a andar en bicicleta a tu hijo que siempre lo estás sosteniendo. A veces tenés que dejar que se caiga un poquito."

> "Para que aprenda de su propio error, de que esa predicción lo llevó por un camino que derrapó."

### La solución: Scheduled Sampling

> "Lo que se suele hacer es aleatoriamente a veces forcing a veces no. Al inicio es más [Teacher Forcing] y eso va disminuyendo hasta que al final prácticamente no se usa."

```
Inicio del entrenamiento:  90% Teacher Forcing, 10% Free Running
Mitad del entrenamiento:   50% Teacher Forcing, 50% Free Running
Final del entrenamiento:   10% Teacher Forcing, 90% Free Running
```

---

## SECCIÓN O: Entrenamiento vs Inferencia

### Tabla comparativa

| Aspecto | Entrenamiento | Inferencia |
|---------|---------------|------------|
| **Datos del decoder** | Tenemos X (francés) e Y (inglés) | Solo tenemos X |
| **Input del decoder** | Palabra real (Teacher Forcing) | Lo que predijo el modelo |
| **Cuándo para** | Cuando termina Y | Cuando genera `<EOS>` |
| **Error** | Se calcula comparando con Y | No hay error (predicción) |

### Pregunta de estudiante sobre los datos

> "¿Cómo ya está en inglés en el decoder?"

Respuesta:
> "Tus datos son dos frases: la frase en francés y la frase en inglés. Si no, no tiene forma de aprender."

### Entrenamiento end-to-end

> "El decoder se va a estar entrenando a la vez que el encoder."

El gradiente fluye desde el error final hacia atrás por todo el sistema.

---

## SECCIÓN P: Mejora - Pasar Contexto a Todos los Pasos

### La primera mejora

> "Una primer mejora es pasar en vez de pasar solo el contexto al primero, por qué no pasárselo a todos."

```
        CONTEXTO ─────────┬─────────┬─────────┬─────────┐
                          │         │         │         │
                          ▼         ▼         ▼         ▼
                       ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
                   ──▶ │ GRU │─▶│ GRU │─▶│ GRU │─▶│ GRU │
                       └─────┘  └─────┘  └─────┘  └─────┘
```

### Conexión con Attention (clases 11 y 12)

> "Si hay attention va a tener ponderación de todos y puede variar de acuerdo a cuál es la palabra."

El mecanismo de **Attention** es la siguiente mejora importante que resuelve el **cuello de botella**.

---

## SECCIÓN P.5: El Problema del Cuello de Botella (IMPORTANTE - Se resuelve en clase 11)

### ¿Cuál es exactamente el problema?

En la arquitectura Seq2Seq que vimos:
- El Encoder procesa TODA la frase de entrada
- Produce UN SOLO vector de contexto C (el último hidden state)
- El Decoder usa ese ÚNICO C para generar TODA la salida

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       EL CUELLO DE BOTELLA                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ENCODER                                                               │
│   "El" → H₁                                                             │
│   "gato" → H₂        ┐                                                  │
│   "negro" → H₃       │                                                  │
│   "duerme" → H₄      ├──▶  Solo guardamos H₄ como C                     │
│   "en" → H₅          │     (¡tiramos H₁, H₂, H₃!)                       │
│   "el" → H₆          │                                                  │
│   "jardín" → H₇ ─────┘                                                  │
│                  │                                                      │
│                  ▼                                                      │
│              C = H₇  ← TODO tiene que pasar por este punto              │
│                  │                                                      │
│                  ▼                                                      │
│   DECODER usa SOLO C para generar "The cat sleeps in the garden"        │
│                                                                         │
│   ⚠️ PROBLEMA: Si la frase es muy larga, C no tiene suficiente         │
│                capacidad para recordar todo                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### ¿Por qué es un problema?

1. **Frases largas:** Toda la información de 50 palabras tiene que caber en un vector de (por ejemplo) 256 dimensiones
2. **Información perdida:** Los primeros hidden states H₁, H₂, H₃ se "olvidan" parcialmente
3. **Mismo C para todo:** Para traducir "gato" y "jardín" usas el mismo C

### La solución (clase 11): Bahdanau Attention

En lugar de usar un solo C, el mecanismo de Attention permite:
- **Guardar TODOS los hidden states** del encoder (H₁, H₂, ..., Hₙ)
- **Calcular un contexto diferente Cᵢ** para cada palabra que genera el decoder
- **Cᵢ es un promedio ponderado** de todos los Hⱼ, donde los pesos indican "a cuál presto más atención"

```
ANTES (Seq2Seq):     P(yᵢ) = función(C,  Sᵢ₋₁, yᵢ₋₁)    ← C fijo
DESPUÉS (Attention): P(yᵢ) = función(Cᵢ, Sᵢ₋₁, yᵢ₋₁)    ← Cᵢ varía!
```

**NOTA:** Attention se AGREGA al Seq2Seq, no lo reemplaza. Seguimos teniendo Encoder y Decoder, pero ahora el Decoder puede "mirar" todos los estados del Encoder.

---

## SECCIÓN Q: Comparación con Transformers

**📌 NOTA:** Esta comparación es un adelanto. Los detalles de cómo funcionan los Transformers (arquitectura, Self-Attention, Masked Attention) se verán en las **clases 11 y 12**.

### Diferencia fundamental

| RNN | Transformer |
|-----|-------------|
| Procesamiento **secuencial** | Procesamiento **paralelo** |
| Paso a paso | Todo de una vez |
| No necesita máscara | Necesita máscara temporal |

### El problema de los Transformers

> "Como vos no tenés esta cuestión secuencial, tenés que poner una máscara temporal para que no mire para adelante."

> "Porque si no puede hacer trampa y mirar [el futuro]."

En RNN esto no pasa porque procesa paso a paso.

---

## SECCIÓN R: Parte Práctica - Curvas de Entrenamiento

*(Esta sección es sobre el laboratorio, no teoría)*

### El problema con las instrucciones originales

> "Les dije que con 1000 épocas alcanza, pero puede variar de 200 épocas a 5000 o más."

### Qué graficar

- **Línea azul:** Error en train
- **Línea naranja:** Error en test

### Patrones a observar

| Patrón | Significado |
|--------|-------------|
| Error muy alto y errático | Modelo muy pequeño |
| Error train baja pero no llega a 0 | Necesita más épocas |
| Error train llega a 0 | El modelo tiene suficiente capacidad |
| Error train bajo, test sube | Overfitting (lo que buscamos ver) |

### Cuándo parar

> "Con un modelo más complejo llegas más rápido a train cero, que es donde se estabiliza."

El objetivo es entrenar **hasta que se vea overfitting**, no un número fijo de épocas.

### Consejo

> "En vez de entrenar [un número fijo] y ver qué pasa, graficar las curvas de entrenamiento y chequear que los modelos complejos lleguen a error cero."

---

## RESUMEN VISUAL: La Evolución Completa

```
╔══════════════════════════════════════════════════════════════════════════════╗
║          EVOLUCIÓN DE MODELOS DE LENGUAJE (separado por TIPOS)               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  ENFOQUES/CAPAS para predecir la siguiente palabra:                    │  ║
║  │  ──────────────────────────────────────────────────                    │  ║
║  │                                                                        │  ║
║  │  1. N-GRAMAS (conteo de frecuencias)                                   │  ║
║  │     └─ Problema: combinatoria, datos esparsos                          │  ║
║  │                   │                                                    │  ║
║  │                   ▼                                                    │  ║
║  │  2. MLP + EMBEDDINGS (redes neuronales)                                │  ║
║  │     └─ Resuelve: combinatoria gracias a embeddings                     │  ║
║  │     └─ Problema: ventana fija                                          │  ║
║  │                   │                                                    │  ║
║  │                   ▼                                                    │  ║
║  │  3. RNN (recurrentes)                                                  │  ║
║  │     └─ Resuelve: cualquier largo, comparte pesos                       │  ║
║  │     └─ Problema: vanishing gradient, memoria limitada                  │  ║
║  │                   │                                                    │  ║
║  │                   ▼                                                    │  ║
║  │  4. LSTM / GRU (capas con compuertas)                                  │  ║
║  │     └─ Resuelve: memoria a largo plazo                                 │  ║
║  │     └─ Problema: solo genera mismo largo que entrada                   │  ║
║  │                   │                                                    │  ║
║  │                   │ ← Estas CAPAS se usan DENTRO de arquitecturas      │  ║
║  │                   ▼                                                    │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  PATRÓN de diseño:                                                     │  ║
║  │  ─────────────────                                                     │  ║
║  │                                                                        │  ║
║  │  5. ENCODER-DECODER (patrón, NO arquitectura)                          │  ║
║  │     └─ Idea: comprimir entrada en vector → generar salida              │  ║
║  │     └─ Resuelve: diferentes longitudes entrada/salida                  │  ║
║  │     └─ Problema: cuello de botella en el contexto único                │  ║
║  │                   │                                                    │  ║
║  │                   │ ← Este PATRÓN se implementa con arquitecturas      │  ║
║  │                   ▼                                                    │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  ARQUITECTURAS que implementan el patrón Encoder-Decoder:              │  ║
║  │  ────────────────────────────────────────────────────────              │  ║
║  │                                                                        │  ║
║  │  6. SEQ2SEQ (arquitectura con LSTM/GRU + Teacher Forcing)              │  ║
║  │     └─ Implementa: Encoder-Decoder usando RNN/LSTM/GRU como capas      │  ║
║  │     └─ Permite: traducción, resumen, captioning                        │  ║
║  │     └─ Problema: cuello de botella, no paraleliza                      │  ║
║  │                   │                                                    │  ║
║  │                   │ + Mejora: Bahdanau Attention (clase 11)            │  ║
║  │                   ▼                                                    │  ║
║  │                                                                        │  ║
║  │  7. TRANSFORMER (arquitectura con Self-Attention)                      │  ║
║  │     └─ Implementa: Encoder-Decoder usando Attention como capas         │  ║
║  │     └─ Resuelve: cuello de botella + paralelización masiva             │  ║
║  │     └─ Es la base de: GPT, BERT, ChatGPT (clases 11-12)                │  ║
║  │                                                                        │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                                                              ║
║  CLAVE: LSTM/GRU no se "reemplazan" por Seq2Seq.                             ║
║         LSTM/GRU son capas que se USAN DENTRO de Seq2Seq.                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## FÓRMULAS CLAVE

### Probabilidad con N-gramas (conteo)
```
P(wₜ | wₜ₋ₙ₊₁, ..., wₜ₋₁) = Conteo(wₜ₋ₙ₊₁, ..., wₜ) / Conteo(wₜ₋ₙ₊₁, ..., wₜ₋₁)
```

### Propiedad de Markov
```
P(wₜ | w₁, w₂, ..., wₜ₋₁) = P(wₜ | wₜ₋₁)
```

### RNN básica
```
hₜ = f(Wxₜ + Uhₜ₋₁ + b)
oₜ = softmax(Vhₜ + c)
```

### Loss en Seq2Seq
```
L = Σₜ CrossEntropy(yₜ_real, yₜ_pred)
```

---

## ¿Qué viene en la próxima clase?

> "El plan de la próxima es ver attention en este contexto y pasar a Transformer."

El mecanismo de **Attention** resuelve el cuello de botella del contexto único, y los **Transformers** permiten paralelización masiva.

---

## Recursos mencionados

- **Tutorial de PyTorch sobre Seq2Seq:** código paso a paso de un traductor
- **Blog de Medium:** ejemplos de traducción, audio a texto, image captioning
- **Wikipedia sobre Seq2Seq:** animaciones del mecanismo de atención
