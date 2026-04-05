# Guía de Estudio - Parcial 2 - Modelos de Deep Learning
## Soluciones Completas y Explicadas

---

# GLOSARIO DE VARIABLES Y SÍMBOLOS

**Antes de resolver los ejercicios, es FUNDAMENTAL entender qué significa cada símbolo.**

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    GLOSARIO COMPLETO DE VARIABLES                                   │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  Este glosario cubre las variables usadas en la ARQUITECTURA TRANSFORMER            │
│  (paper "Attention is All You Need", 2017) y en la arquitectura SEQ2SEQ.            │
│                                                                                     │
│  ══════════════════════════════════════════════════════════════════════════════    │
│  DIMENSIONES EN EL TRANSFORMER (tamaños de los vectores y matrices)                │
│  ══════════════════════════════════════════════════════════════════════════════    │
│                                                                                     │
│  d_model    "dimensión del embedding en el Transformer"                             │
│             ───────────────────────────────────────────                             │
│             ¿QUÉ ES? El tamaño del vector que representa cada token (palabra)       │
│                      en TODAS las capas del Transformer.                            │
│             ¿DÓNDE SE USA? En TODO el Transformer: embeddings, salida de            │
│                            attention, entrada/salida del feed-forward.              │
│             ¿POR QUÉ IMPORTA? Es LA dimensión que define el "ancho" del modelo.     │
│                               Vectores más grandes = más capacidad = más parámetros.│
│             EJEMPLO: d_model = 512 significa que cada token se representa con       │
│                      un vector de 512 números reales: [0.2, -0.5, 0.8, ..., 0.1]    │
│             VALOR EN EL PAPER ORIGINAL: 512                                         │
│                                                                                     │
│  d_k        "dimensión de los vectores Query y Key en Multi-Head Attention"         │
│             ───────────────────────────────────────────────────────────────         │
│             ¿QUÉ ES? El tamaño de los vectores Q y K DENTRO de cada cabeza.         │
│             ¿CÓMO SE CALCULA? d_k = d_model ÷ h (se divide entre el número de       │
│                               cabezas para que al concatenar volvamos a d_model)    │
│             ¿POR QUÉ DIVIDIR? Si tenemos h=8 cabezas y cada una produce vectores    │
│                               de d_k=64, al concatenar: 8 × 64 = 512 = d_model      │
│             EJEMPLO: d_model=512, h=8 → d_k = 512/8 = 64                            │
│             ¿DÓNDE APARECE EN LA FÓRMULA? En el divisor √d_k del scaled attention:  │
│                                           softmax(QKᵀ / √d_k)                       │
│                                                                                     │
│  d_v        "dimensión de los vectores Value en Multi-Head Attention"               │
│             ─────────────────────────────────────────────────────────               │
│             ¿QUÉ ES? El tamaño de los vectores V DENTRO de cada cabeza.             │
│             ¿ES IGUAL A d_k? Sí, en el paper original d_v = d_k = 64.               │
│                              Podrían ser diferentes, pero usualmente son iguales.   │
│             ¿DÓNDE SE USA? El output de cada cabeza tiene dimensión d_v.            │
│                            Luego se concatenan: h × d_v = d_model                   │
│                                                                                     │
│  d_ff       "dimensión de la capa oculta del Feed-Forward Network"                  │
│             ─────────────────────────────────────────────────────────               │
│             ¿QUÉ ES? El tamaño de la capa INTERMEDIA en el FFN de cada bloque.      │
│             ¿CÓMO FUNCIONA EL FFN?                                                  │
│                  Entrada [d_model] → Expandir a [d_ff] → ReLU → Comprimir [d_model] │
│                  Entrada [512] → Expandir a [2048] → ReLU → Comprimir a [512]       │
│             ¿POR QUÉ EXPANDIR? Más dimensiones = más capacidad de transformación.   │
│             VALOR TÍPICO: d_ff = 4 × d_model (ej: 4 × 512 = 2048)                   │
│                                                                                     │
│  ══════════════════════════════════════════════════════════════════════════════    │
│  HIPERPARÁMETROS DEL TRANSFORMER (números que el diseñador elige)                  │
│  ══════════════════════════════════════════════════════════════════════════════    │
│                                                                                     │
│  h          "número de cabezas en Multi-Head Attention"                             │
│             ───────────────────────────────────────────                             │
│             ¿QUÉ ES? Cuántos mecanismos de attention se ejecutan EN PARALELO.       │
│             ¿POR QUÉ MÚLTIPLES? Cada cabeza puede aprender a enfocarse en           │
│                                 diferentes tipos de relaciones:                     │
│                                 - Cabeza 1: relaciones gramaticales (sujeto-verbo)  │
│                                 - Cabeza 2: relaciones semánticas (sinónimos)       │
│                                 - Cabeza 3: relaciones de posición (palabras cerca) │
│             VALOR EN EL PAPER ORIGINAL: h = 8                                       │
│             RESTRICCIÓN: d_model debe ser divisible por h (512/8 = 64, OK)          │
│                                                                                     │
│  N          "número de bloques/capas apilados en el Transformer"                    │
│             ────────────────────────────────────────────────────                    │
│             ¿QUÉ ES? Cuántas veces se repite el bloque Encoder (o Decoder).         │
│             ¿QUÉ CONTIENE CADA BLOQUE DEL ENCODER?                                  │
│                  1. Multi-Head Self-Attention + Add&Norm                            │
│                  2. Feed-Forward Network + Add&Norm                                 │
│             VALOR EN EL PAPER ORIGINAL: N = 6 (6 bloques encoder, 6 decoder)        │
│             MÁS CAPAS = modelo más profundo = más capacidad pero más costoso        │
│                                                                                     │
│  V          "tamaño del vocabulario"                                                │
│             ────────────────────────                                                │
│             ¿QUÉ ES? El número total de tokens DIFERENTES que el modelo conoce.     │
│             ¿DÓNDE SE USA? En la tabla de embeddings: matriz de tamaño [V × d_model]│
│             EJEMPLO: V = 30,000 significa que el modelo conoce 30,000 tokens.       │
│                      Cada token tiene un índice: "hola"=4523, "mundo"=8901, etc.    │
│             INCLUYE: palabras, subpalabras, puntuación, [SOS], [EOS], [PAD], etc.   │
│                                                                                     │
│  L          "longitud máxima de secuencia"                                          │
│             ──────────────────────────────                                          │
│             ¿QUÉ ES? El máximo de tokens que el modelo puede procesar de una vez.   │
│             ¿POR QUÉ HAY LÍMITE? El Positional Encoding tiene tamaño fijo [L×d_model]│
│                                  y la memoria crece como O(L²) por el attention.    │
│             EJEMPLO: L = 512 significa máximo 512 tokens por secuencia.             │
│             SI LA SECUENCIA ES MÁS CORTA: se rellena con [PAD] hasta L.             │
│             SI ES MÁS LARGA: se trunca o se divide en chunks.                       │
│                                                                                     │
│  ══════════════════════════════════════════════════════════════════════════════    │
│  MATRICES DE PESOS EN MULTI-HEAD ATTENTION (parámetros entrenables)                │
│  ══════════════════════════════════════════════════════════════════════════════    │
│                                                                                     │
│  W^Q        "matriz que proyecta la entrada a vectores Query"                       │
│             ─────────────────────────────────────────────────                       │
│             ¿QUÉ HACE? Transforma cada vector de entrada X en un vector Query Q.    │
│             OPERACIÓN: Q = X × W^Q                                                  │
│             DIMENSIÓN: [d_model × d_model] para toda la capa, o                     │
│                        [d_model × d_k] para cada cabeza individual                  │
│             ¿QUÉ REPRESENTA Q? "¿Qué información estoy buscando?"                   │
│             SE ENTRENA: Sí, los valores de W^Q se ajustan con backpropagation.      │
│                                                                                     │
│  W^K        "matriz que proyecta la entrada a vectores Key"                         │
│             ───────────────────────────────────────────────                         │
│             ¿QUÉ HACE? Transforma cada vector de entrada X en un vector Key K.      │
│             OPERACIÓN: K = X × W^K                                                  │
│             DIMENSIÓN: [d_model × d_model] o [d_model × d_k] por cabeza             │
│             ¿QUÉ REPRESENTA K? "¿Cómo me etiqueto/identifico para ser encontrado?"  │
│                                                                                     │
│  W^V        "matriz que proyecta la entrada a vectores Value"                       │
│             ─────────────────────────────────────────────────                       │
│             ¿QUÉ HACE? Transforma cada vector de entrada X en un vector Value V.    │
│             OPERACIÓN: V = X × W^V                                                  │
│             DIMENSIÓN: [d_model × d_model] o [d_model × d_v] por cabeza             │
│             ¿QUÉ REPRESENTA V? "¿Cuál es el contenido/información que aporto?"      │
│                                                                                     │
│  W^O        "matriz que combina las salidas de todas las cabezas"                   │
│             ─────────────────────────────────────────────────────                   │
│             ¿QUÉ HACE? Después de concatenar las h cabezas, proyecta de vuelta.     │
│             OPERACIÓN: Output = Concat(head₁, ..., headₕ) × W^O                     │
│             DIMENSIÓN: [h×d_v × d_model] = [d_model × d_model]                      │
│             ¿POR QUÉ? Para mezclar la información de todas las cabezas.             │
│                                                                                     │
│  W₁, W₂    "matrices del Feed-Forward Network dentro de cada bloque"               │
│             ─────────────────────────────────────────────────────────               │
│             ¿DÓNDE ESTÁN? En el FFN que viene DESPUÉS del Multi-Head Attention.     │
│             W₁: Expande de [d_model] a [d_ff]. Dimensión: [d_model × d_ff]          │
│                 Ejemplo: de 512 dimensiones a 2048 dimensiones                      │
│             W₂: Comprime de [d_ff] a [d_model]. Dimensión: [d_ff × d_model]         │
│                 Ejemplo: de 2048 dimensiones de vuelta a 512                        │
│                                                                                     │
│  b₁, b₂    "vectores bias del Feed-Forward Network"                                │
│             ───────────────────────────────────────                                 │
│             ¿QUÉ SON? Vectores que se SUMAN después de multiplicar por W.           │
│             b₁: Vector de [d_ff] dimensiones (ej: 2048 números)                     │
│             b₂: Vector de [d_model] dimensiones (ej: 512 números)                   │
│             FÓRMULA COMPLETA: FFN(x) = (ReLU(x×W₁ + b₁)) × W₂ + b₂                  │
│                                                                                     │
│  ══════════════════════════════════════════════════════════════════════════════    │
│  VECTORES Q, K, V EN EL MECANISMO DE ATTENTION                                     │
│  ══════════════════════════════════════════════════════════════════════════════    │
│                                                                                     │
│  q          "vector Query" (consulta)                                               │
│             ─────────────────────────                                               │
│             ¿QUÉ ES? El vector que representa "qué información estoy buscando".     │
│             ¿CÓMO SE OBTIENE? q = x × W^Q (multiplicar entrada por matriz W^Q)      │
│             DIMENSIÓN: d_k (ej: 64 números en cada cabeza del Transformer)          │
│             ANALOGÍA: Es como la pregunta que escribes en un buscador.              │
│             EJEMPLO: Si quiero traducir "gato", el query de "gato" busca            │
│                      qué palabras en la entrada son relevantes para traducirlo.     │
│                                                                                     │
│  k          "vector Key" (clave)                                                    │
│             ────────────────────                                                    │
│             ¿QUÉ ES? El vector que representa "cómo me identifico/etiqueto".        │
│             ¿CÓMO SE OBTIENE? k = x × W^K (multiplicar entrada por matriz W^K)      │
│             DIMENSIÓN: d_k (debe ser igual que query para poder hacer producto punto)│
│             ANALOGÍA: Es como el título o etiqueta de un documento.                 │
│             USO: Se compara con el query: score = q · k (producto punto)            │
│                                                                                     │
│  v          "vector Value" (valor)                                                  │
│             ─────────────────────                                                   │
│             ¿QUÉ ES? El vector que contiene "el contenido/información real".        │
│             ¿CÓMO SE OBTIENE? v = x × W^V (multiplicar entrada por matriz W^V)      │
│             DIMENSIÓN: d_v (usualmente igual a d_k, ej: 64)                         │
│             ANALOGÍA: Es como el contenido del documento, no solo su título.        │
│             USO: La salida del attention es un promedio ponderado de los values.    │
│                                                                                     │
│  z          "salida del mecanismo de attention"                                     │
│             ─────────────────────────────────                                       │
│             ¿QUÉ ES? El vector resultado de aplicar attention.                      │
│             ¿CÓMO SE CALCULA? z = Σᵢ αᵢ × vᵢ (suma ponderada de los values)         │
│             DIMENSIÓN: d_v (mismo tamaño que cada value)                            │
│             SIGNIFICADO: Combina la información de todos los values,                │
│                          dando más peso a los que tienen keys más similares al query│
│                                                                                     │
│  ══════════════════════════════════════════════════════════════════════════════    │
│  SCORES Y PESOS EN EL CÁLCULO DE ATTENTION                                         │
│  ══════════════════════════════════════════════════════════════════════════════    │
│                                                                                     │
│  e o eᵢⱼ   "score de atención" (también llamado "energía")                          │
│             ──────────────────────────────────────────────                          │
│             ¿QUÉ ES? Un número que indica qué tan "relacionados" o "similares"      │
│                      están el query de posición i y el key de posición j.           │
│             ¿CÓMO SE CALCULA? eᵢⱼ = qᵢ · kⱼ (producto punto entre vectores)         │
│             RANGO: Puede ser cualquier número real (positivo, negativo, grande...)  │
│             ¿CUÁNDO ES ALTO? Cuando query y key apuntan en direcciones similares.   │
│             IMPORTANTE: Este es el valor ANTES de aplicar softmax.                  │
│             EN SCALED ATTENTION: se divide por √d_k para evitar valores muy grandes │
│                                                                                     │
│  α o αᵢⱼ   "peso de atención" (attention weight)                                    │
│             ─────────────────────────────────────                                   │
│             ¿QUÉ ES? Un número entre 0 y 1 que indica "cuánta atención prestar"     │
│                      al value de la posición j cuando estoy en la posición i.       │
│             ¿CÓMO SE CALCULA? αᵢⱼ = softmax(eᵢⱼ) = e^eᵢⱼ / Σₖ e^eᵢₖ                 │
│             PROPIEDADES:                                                            │
│                  - Siempre entre 0 y 1                                              │
│                  - Todos los α de una fila suman exactamente 1                      │
│                  - Si αᵢⱼ = 0.8, significa "80% de mi atención va a posición j"     │
│             VISUALIZACIÓN: Es como un mapa de calor que muestra qué mira cada palabra│
│                                                                                     │
│  ══════════════════════════════════════════════════════════════════════════════    │
│  ESTADOS OCULTOS EN ARQUITECTURAS RNN Y SEQ2SEQ                                    │
│  ══════════════════════════════════════════════════════════════════════════════    │
│                                                                                     │
│  hₜ         "hidden state del ENCODER en el paso de tiempo t"                       │
│             ─────────────────────────────────────────────────                       │
│             ¿EN QUÉ ARQUITECTURA? En Seq2Seq (que usa RNN/LSTM/GRU).                │
│             ¿QUÉ ES? Un vector que representa toda la información que el encoder    │
│                      ha acumulado después de leer los primeros t tokens de entrada. │
│             ¿CÓMO SE CALCULA? hₜ = f(hₜ₋₁, xₜ) donde f es la celda RNN/LSTM/GRU     │
│             DIMENSIÓN: La que elijas para el hidden state (ej: 256, 512)            │
│             EJEMPLO: Si la entrada es "El gato negro":                              │
│                      h₁ = información después de leer "El"                          │
│                      h₂ = información después de leer "El gato"                     │
│                      h₃ = información después de leer "El gato negro"               │
│                                                                                     │
│  sₜ         "hidden state del DECODER en el paso de tiempo t"                       │
│             ─────────────────────────────────────────────────                       │
│             ¿EN QUÉ ARQUITECTURA? En Seq2Seq (que usa RNN/LSTM/GRU).                │
│             ¿QUÉ ES? Un vector que representa el estado del decoder mientras        │
│                      genera la secuencia de salida, palabra por palabra.            │
│             ¿DE QUÉ DEPENDE? Del contexto c, del estado anterior sₜ₋₁, y de         │
│                              la palabra anterior yₜ₋₁                               │
│             NOTA: Se usa "s" para decoder y "h" para encoder para distinguirlos.    │
│                                                                                     │
│  c o cₜ    "context vector" (vector de contexto)                                    │
│             ────────────────────────────────────                                    │
│             ¿QUÉ ES? El vector que "resume" la información del encoder              │
│                      y se pasa al decoder.                                          │
│             EN SEQ2SEQ SIN ATTENTION:                                               │
│                  c = hₙ (el último hidden state del encoder)                        │
│                  Es FIJO para toda la generación → CUELLO DE BOTELLA                │
│             EN SEQ2SEQ CON BAHDANAU ATTENTION:                                      │
│                  cₜ = Σⱼ αₜⱼ × hⱼ (promedio ponderado de TODOS los hidden states)   │
│                  Es DINÁMICO: cambia en cada paso t de generación                   │
│                  Resuelve el cuello de botella                                      │
│                                                                                     │
│  ══════════════════════════════════════════════════════════════════════════════    │
│  LAYER NORMALIZATION                                                               │
│  ══════════════════════════════════════════════════════════════════════════════    │
│                                                                                     │
│  γ (gamma)  "escala aprendida"                                                      │
│             ──────────────────                                                      │
│             Multiplica la salida normalizada. Vector de d_model dimensiones.        │
│                                                                                     │
│  β (beta)   "desplazamiento aprendido"                                              │
│             ────────────────────────────                                            │
│             Se suma a la salida normalizada. Vector de d_model dimensiones.         │
│                                                                                     │
│  ══════════════════════════════════════════════════════════════════════════════    │
│  TOKENS ESPECIALES                                                                 │
│  ══════════════════════════════════════════════════════════════════════════════    │
│                                                                                     │
│  [SOS]      "Start of Sequence"                                                     │
│             ───────────────────                                                     │
│             Token especial que indica "empieza a generar".                          │
│             También llamado <s>, <bos>, [CLS]                                       │
│                                                                                     │
│  [EOS]      "End of Sequence"                                                       │
│             ─────────────────                                                       │
│             Token especial que indica "terminé de generar".                         │
│             También llamado </s>, <eos>, [SEP]                                      │
│                                                                                     │
│  [PAD]      "Padding"                                                               │
│             ─────────                                                               │
│             Token para rellenar secuencias cortas hasta longitud fija.              │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

# CLASIFICACIÓN DE CONCEPTOS POR TIPO

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    ¿QUÉ TIPO DE COSA ES CADA CONCEPTO?                              │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  TIPO 1: REPRESENTACIÓN (cómo convertimos cosas reales en números)                 │
│  ─────────────────────────────────────────────────────────────────                  │
│  • Embeddings (Token, Positional)                                                   │
│  • One-Hot Encoding                                                                 │
│                                                                                     │
│  TIPO 2: CAPAS (operaciones matemáticas que transforman datos)                     │
│  ─────────────────────────────────────────────────────────────                      │
│  • Multi-Head Attention                                                             │
│  • Masked Multi-Head Attention                                                      │
│  • Feed-Forward Network                                                             │
│  • Linear / Dense                                                                   │
│  • Softmax                                                                          │
│  • RNN, LSTM, GRU (capas recurrentes)                                               │
│                                                                                     │
│  TIPO 3: ARQUITECTURAS (cómo organizamos las capas)                                │
│  ──────────────────────────────────────────────────                                 │
│  • Seq2Seq (usa RNN/LSTM/GRU, implementa patrón Encoder-Decoder)                    │
│  • Transformer (usa Self-Attention, implementa patrón Encoder-Decoder)              │
│                                                                                     │
│  TIPO 4: PATRONES DE DISEÑO (ideas conceptuales)                                   │
│  ───────────────────────────────────────────────                                    │
│  • Encoder-Decoder (comprimir entrada → generar salida)                             │
│                                                                                     │
│  TIPO 5: TÉCNICAS DE ENTRENAMIENTO                                                 │
│  ─────────────────────────────────                                                  │
│  • Teacher Forcing                                                                  │
│  • Scheduled Sampling                                                               │
│  • Masked Attention (para no ver el futuro)                                         │
│                                                                                     │
│  TIPO 6: TRUCOS ARQUITECTÓNICOS                                                    │
│  ──────────────────────────────                                                     │
│  • Skip Connections (Add)                                                           │
│  • Layer Normalization (Norm)                                                       │
│  • Positional Encoding                                                              │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

# FÓRMULAS CLAVE CON EXPLICACIÓN

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              FÓRMULAS ESENCIALES                                    │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  1. ATTENTION (sin escalar)                                                         │
│  ──────────────────────────                                                         │
│                                                                                     │
│     z = Σᵢ αᵢ × vᵢ       donde    αᵢ = softmax(q · kᵢ)                             │
│                                                                                     │
│     En palabras: "La salida z es el promedio ponderado de los values,               │
│                   donde los pesos α dependen de qué tan similar es                  │
│                   mi query q a cada key k"                                          │
│                                                                                     │
│  2. SCALED DOT-PRODUCT ATTENTION                                                    │
│  ───────────────────────────────                                                    │
│                                                                                     │
│     Attention(Q, K, V) = softmax(Q × Kᵀ / √d_k) × V                                 │
│                                   ───────────────                                   │
│                                         │                                           │
│                                   dividimos por √d_k                                │
│                                   para evitar valores                               │
│                                   muy grandes que                                   │
│                                   saturen el softmax                                │
│                                                                                     │
│  3. MULTI-HEAD ATTENTION                                                            │
│  ───────────────────────                                                            │
│                                                                                     │
│     MultiHead(Q, K, V) = Concat(head₁, ..., headₕ) × W^O                            │
│                                                                                     │
│     donde headᵢ = Attention(Q×Wᵢ^Q, K×Wᵢ^K, V×Wᵢ^V)                                 │
│                                                                                     │
│     En palabras: "Hacemos h attentions en paralelo, cada uno con                    │
│                   sus propias matrices, y concatenamos los resultados"              │
│                                                                                     │
│  4. FEED-FORWARD NETWORK                                                            │
│  ───────────────────────                                                            │
│                                                                                     │
│     FFN(x) = max(0, x×W₁ + b₁) × W₂ + b₂                                            │
│              ─────────────────                                                      │
│                    ReLU                                                             │
│                                                                                     │
│     Flujo: [d_model] → [d_ff] → ReLU → [d_ff] → [d_model]                           │
│              512    →   2048   →      →  2048  →   512                              │
│                                                                                     │
│  5. LAYER NORMALIZATION                                                             │
│  ──────────────────────                                                             │
│                                                                                     │
│     LayerNorm(x) = γ × (x - μ) / σ + β                                              │
│                                                                                     │
│     donde μ = media de x, σ = desviación estándar de x                              │
│           γ y β son parámetros aprendidos (d_model cada uno)                        │
│                                                                                     │
│  6. SOFTMAX                                                                         │
│  ─────────                                                                          │
│                                                                                     │
│     softmax(xᵢ) = e^xᵢ / Σⱼ e^xⱼ                                                    │
│                                                                                     │
│     En palabras: "Convierte números en probabilidades que suman 1"                  │
│     Propiedad clave: e^(-∞) = 0 (así funciona la máscara)                           │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

# SECCIÓN 1: MECANISMO DE ATENCIÓN Y TRANSFORMERS (Ejercicios 1-4)

---

## Ejercicio 1: Cálculo del Mecanismo de Atención

### Enunciado
Dado un query q = (1, 0, 1, 0) y dos pares key-value:
- k₁ = (1, 1, 0, 0), v₁ = (2, 0, 1, 1)
- k₂ = (0, 1, 1, 0), v₂ = (0, 1, 2, 1)

Calcular el vector de salida z usando el mecanismo de atención (sin escalar).

### ¿Qué es el Mecanismo de Atención? (Explicación Básica)

**Analogía**: Imagina que estás en una biblioteca buscando información sobre "recetas de pasta".
- Tu **query (q)** es tu pregunta: "recetas de pasta"
- Los **keys (k)** son los títulos de los libros en los estantes
- Los **values (v)** son el contenido de cada libro

El mecanismo de atención:
1. Compara tu pregunta con cada título (query · key)
2. Decide cuánta "atención" prestar a cada libro
3. Combina los contenidos según esa atención

### Solución Paso a Paso

**Paso 1: Calcular los productos punto (similitudes)**

El producto punto nos dice "qué tan parecidos" son el query y cada key.

```
q · k₁ = (1×1) + (0×1) + (1×0) + (0×0) = 1 + 0 + 0 + 0 = 1
q · k₂ = (1×0) + (0×1) + (1×1) + (0×0) = 0 + 0 + 1 + 0 = 1
```

Ambos keys tienen la misma similitud con el query (= 1).

**Paso 2: Aplicar Softmax para obtener los pesos de atención**

Softmax convierte los puntajes en probabilidades que suman 1.

```
Fórmula: softmax(xᵢ) = e^(xᵢ) / Σe^(xⱼ)

e¹ = 2.718...

α₁ = e¹ / (e¹ + e¹) = e / 2e = 0.5
α₂ = e¹ / (e¹ + e¹) = e / 2e = 0.5
```

Los pesos de atención son: **α₁ = 0.5** y **α₂ = 0.5**

Esto significa: "presta 50% de atención a cada value".

**Paso 3: Calcular el vector de salida z**

```
z = α₁ · v₁ + α₂ · v₂
z = 0.5 × (2, 0, 1, 1) + 0.5 × (0, 1, 2, 1)
z = (1, 0, 0.5, 0.5) + (0, 0.5, 1, 0.5)
z = (1, 0.5, 1.5, 1)
```

### Respuesta Final
```
z = (1.0, 0.5, 1.5, 1.0)
```

### Verificación
- Los pesos suman 1: 0.5 + 0.5 = 1 ✓
- z es un promedio ponderado de v₁ y v₂ ✓
- Como los pesos son iguales, z está exactamente "en medio" de v₁ y v₂ ✓

---

## Ejercicio 2: Multi-Head Attention - Dimensiones y Parámetros

### Enunciado
Un modelo tiene d_model = 512 y usa 8 cabezas de atención (h = 8).
a) ¿Cuáles son las dimensiones d_k y d_v de cada cabeza?
b) ¿Cuántos parámetros tienen las matrices W^Q, W^K, W^V y W^O?

### ¿Qué es Multi-Head Attention? (Explicación Básica)

**Analogía**: Imagina que tienes 8 expertos analizando un texto:
- Un experto busca relaciones gramaticales
- Otro busca relaciones de significado
- Otro busca referencias temporales
- etc.

Cada "cabeza" de atención aprende a enfocarse en diferentes tipos de relaciones. Al final, combinamos las opiniones de todos los expertos.

**¿Por qué dividir las dimensiones?**
- Si el modelo original tiene 512 dimensiones
- Y tenemos 8 cabezas
- Cada cabeza trabaja con 512/8 = 64 dimensiones
- Esto es más eficiente que tener 8 cabezas de 512 dimensiones cada una

### Solución Parte a): Dimensiones d_k y d_v

```
d_k = d_v = d_model / h = 512 / 8 = 64
```

**Respuesta**: d_k = d_v = **64 dimensiones por cabeza**

### Solución Parte b): Conteo de Parámetros

**Las matrices de proyección:**

Cada cabeza necesita proyectar el input a Q, K, V:
- **W^Q**: proyecta a queries
- **W^K**: proyecta a keys
- **W^V**: proyecta a values
- **W^O**: combina las salidas de todas las cabezas

**Dimensiones de cada matriz:**

```
W^Q, W^K, W^V: (d_model × d_model) = (512 × 512) = 262,144 parámetros cada una
W^O: (d_model × d_model) = (512 × 512) = 262,144 parámetros
```

**Nota importante**: Aunque internamente cada cabeza usa d_k=64, las matrices completas W^Q, W^K, W^V tienen dimensión (512 × 512) porque proyectan desde d_model y luego se dividen entre las cabezas.

**Cálculo total:**

```
Parámetros W^Q + W^K + W^V = 3 × 262,144 = 786,432
Parámetros W^O = 262,144

Total Multi-Head Attention = 786,432 + 262,144 = 1,048,576 parámetros
```

### Respuesta Final
- **d_k = d_v = 64**
- **W^Q, W^K, W^V**: 262,144 parámetros cada una (786,432 total)
- **W^O**: 262,144 parámetros
- **Total MHA**: 1,048,576 parámetros (≈ 1 millón)

---

## Ejercicio 3: Masked Self-Attention

### Enunciado
Dada la matriz de scores de atención S (4×4), construir la máscara M y calcular la matriz enmascarada S'.

```
S = | 0.5  0.3  0.1  0.1 |
    | 0.2  0.4  0.2  0.2 |
    | 0.1  0.2  0.5  0.2 |
    | 0.3  0.1  0.3  0.3 |
```

### ¿Qué es Masked Self-Attention? (Explicación Básica)

**El problema**: En el decoder de un Transformer, cuando generamos una secuencia palabra por palabra:
- Al predecir la palabra 3, NO debemos "ver" las palabras 4, 5, 6...
- Sería como hacer trampa en un examen mirando las respuestas

**Analogía**: Es como escribir una historia donde cada capítulo solo puede basarse en los capítulos anteriores, nunca en los futuros.

**La solución - La Máscara Causal**:
- Ponemos -∞ en las posiciones "prohibidas" (futuro)
- Cuando aplicamos softmax, e^(-∞) = 0
- Así esas posiciones no contribuyen a la atención

### Solución Paso a Paso

**Paso 1: Construir la Máscara Causal M**

La máscara tiene:
- **0** donde SÍ podemos mirar (diagonal y hacia la izquierda = pasado)
- **-∞** donde NO podemos mirar (hacia la derecha = futuro)

```
M = |  0   -∞   -∞   -∞  |    Posición 1: solo ve posición 1
    |  0    0   -∞   -∞  |    Posición 2: ve posiciones 1,2
    |  0    0    0   -∞  |    Posición 3: ve posiciones 1,2,3
    |  0    0    0    0  |    Posición 4: ve todas (1,2,3,4)
```

**Paso 2: Calcular S' = S + M**

```
S' = S + M

S' = | 0.5+0    0.3+(-∞)  0.1+(-∞)  0.1+(-∞) |
     | 0.2+0    0.4+0     0.2+(-∞)  0.2+(-∞) |
     | 0.1+0    0.2+0     0.5+0     0.2+(-∞) |
     | 0.3+0    0.1+0     0.3+0     0.3+0    |

S' = | 0.5   -∞    -∞    -∞  |
     | 0.2   0.4   -∞    -∞  |
     | 0.1   0.2   0.5   -∞  |
     | 0.3   0.1   0.3   0.3 |
```

**Paso 3: Aplicar Softmax a cada fila**

Para la fila 1: softmax([0.5, -∞, -∞, -∞]) = [1.0, 0, 0, 0]
Para la fila 2: softmax([0.2, 0.4, -∞, -∞]) ≈ [0.45, 0.55, 0, 0]
Para la fila 3: softmax([0.1, 0.2, 0.5, -∞]) ≈ [0.23, 0.26, 0.51, 0]
Para la fila 4: softmax([0.3, 0.1, 0.3, 0.3]) ≈ [0.27, 0.22, 0.27, 0.27]

### Respuesta Final

**Máscara M:**
```
M = |  0   -∞   -∞   -∞  |
    |  0    0   -∞   -∞  |
    |  0    0    0   -∞  |
    |  0    0    0    0  |
```

**Matriz enmascarada S':**
```
S' = | 0.5   -∞    -∞    -∞  |
     | 0.2   0.4   -∞    -∞  |
     | 0.1   0.2   0.5   -∞  |
     | 0.3   0.1   0.3   0.3 |
```

### ¿Por qué es importante?
- **Evita "data leakage"**: El modelo no hace trampa viendo el futuro
- **Permite entrenamiento paralelo**: A diferencia de RNNs, podemos entrenar todas las posiciones simultáneamente
- **Es diferente a teacher forcing**: Teacher forcing usa la respuesta correcta como input; la máscara simplemente oculta el futuro

---

## Ejercicio 4: Conteo de Parámetros de un Transformer Completo

### Enunciado
Calcular el número total de parámetros de un Transformer Encoder con:
- Vocabulario: V = 1000
- Dimensión del modelo: d_model = 64
- Cabezas de atención: h = 4
- Dimensión FFN: d_ff = 256
- Longitud máxima de secuencia: L = 50
- Número de capas: N = 2

### Componentes del Transformer (Explicación Básica)

**Analogía del Transformer como una fábrica:**
1. **Embeddings**: Convertir palabras en vectores (como traducir idiomas a números)
2. **Positional Encoding**: Agregar información de posición (como numerar páginas)
3. **Multi-Head Attention**: Los "expertos" que analizan relaciones
4. **Feed-Forward Network**: Procesamiento adicional de cada posición
5. **Layer Norm**: Normalización para estabilidad (no tiene parámetros entrenables en esta versión)

### Solución Paso a Paso

**1. Token Embeddings**
Convierte cada palabra del vocabulario en un vector de d_model dimensiones.
```
Parámetros = V × d_model = 1000 × 64 = 64,000
```

**2. Positional Embeddings**
Un vector para cada posición posible.
```
Parámetros = L × d_model = 50 × 64 = 3,200
```

**3. Multi-Head Attention (por capa)**
```
W^Q: d_model × d_model = 64 × 64 = 4,096
W^K: d_model × d_model = 64 × 64 = 4,096
W^V: d_model × d_model = 64 × 64 = 4,096
W^O: d_model × d_model = 64 × 64 = 4,096

Total MHA por capa = 4 × 4,096 = 16,384
```

**4. Feed-Forward Network (por capa)**
Dos capas lineales: primero expande a d_ff, luego comprime a d_model.
```
W₁: d_model × d_ff = 64 × 256 = 16,384
b₁: d_ff = 256
W₂: d_ff × d_model = 256 × 64 = 16,384
b₂: d_model = 64

Total FFN por capa = 16,384 + 256 + 16,384 + 64 = 33,088
```

**5. Layer Normalization (por capa)**
Dos LayerNorms por capa (después de MHA y después de FFN).
```
Cada LayerNorm: 2 × d_model = 2 × 64 = 128 (gamma y beta)
Total LN por capa = 2 × 128 = 256
```

**6. Total por Capa del Encoder**
```
MHA + FFN + LN = 16,384 + 33,088 + 256 = 49,728
```

**7. Total para N = 2 capas**
```
2 × 49,728 = 99,456
```

**8. TOTAL FINAL**
```
Token Embeddings:      64,000
Positional Embeddings:  3,200
2 Encoder Layers:      99,456
─────────────────────────────
TOTAL:                166,656 parámetros
```

### Respuesta Final

| Componente | Parámetros |
|------------|------------|
| Token Embeddings | 64,000 |
| Positional Embeddings | 3,200 |
| Multi-Head Attention (×2) | 32,768 |
| Feed-Forward Network (×2) | 66,176 |
| Layer Normalization (×2) | 512 |
| **TOTAL** | **166,656** |

**Nota**: Algunos cálculos pueden variar ligeramente dependiendo de si se incluyen biases en las proyecciones de atención.

---

# SECCIÓN 2: SEQ2SEQ Y MODELOS ENCODER-DECODER (Ejercicios 5-10)

---

## Ejercicio 5: Arquitectura Seq2Seq Básica

### Enunciado
Describir la arquitectura básica de un modelo Seq2Seq y explicar el "problema del cuello de botella" (bottleneck problem).

### ¿Qué es Seq2Seq? (Explicación Básica)

**Analogía**: Imagina un traductor humano que:
1. **Escucha** toda una oración en español (ENCODER)
2. **Resume** mentalmente el significado en su cabeza (CONTEXT VECTOR)
3. **Produce** la traducción palabra por palabra en inglés (DECODER)

### Arquitectura Seq2Seq

```
ENTRADA: "El gato come"
         ↓
    ┌─────────────────┐
    │    ENCODER      │  (RNN/LSTM que lee la entrada)
    │  El → gato → come│
    └────────┬────────┘
             │
             ↓
    ┌─────────────────┐
    │ CONTEXT VECTOR  │  (Un solo vector que "resume" todo)
    │      [c]        │
    └────────┬────────┘
             │
             ↓
    ┌─────────────────┐
    │    DECODER      │  (RNN/LSTM que genera la salida)
    │ The → cat → eats│
    └─────────────────┘
             ↓
SALIDA: "The cat eats"
```

### El Problema del Cuello de Botella (Bottleneck)

**El problema**: Todo el significado de la oración de entrada debe comprimirse en UN SOLO vector de tamaño fijo (el context vector).

**Analogía**: Es como intentar resumir una novela de 500 páginas en un solo tweet de 280 caracteres. Inevitablemente, perderás información importante.

**Consecuencias**:
1. **Pérdida de información**: Oraciones largas pierden detalles
2. **Dificultad con dependencias lejanas**: El modelo "olvida" el principio de oraciones largas
3. **Rendimiento degradado**: La calidad baja significativamente con secuencias largas

**La Solución**: El mecanismo de ATENCIÓN permite al decoder "mirar atrás" a todos los estados del encoder, no solo al vector final.

### Respuesta Completa

**Arquitectura Seq2Seq**:
- **Encoder**: RNN que procesa la secuencia de entrada y produce estados ocultos
- **Context Vector**: El último estado oculto del encoder (o combinación de estados)
- **Decoder**: RNN que genera la secuencia de salida condicionada al context vector

**Problema del Bottleneck**:
El context vector de tamaño fijo no puede capturar toda la información de secuencias largas, causando pérdida de información y degradación del rendimiento.

---

## Ejercicio 6: Diferencia entre Entrenamiento e Inferencia

### Enunciado
Explicar la diferencia entre el modo de entrenamiento y el modo de inferencia en un modelo Seq2Seq.

### Modo de Entrenamiento: Teacher Forcing

**Analogía**: Es como aprender a conducir con un instructor que corrige el volante constantemente. Aunque te equivoques, el instructor pone el carro en la posición correcta para el siguiente movimiento.

```
Objetivo: Traducir "Hola mundo" → "Hello world"

Paso 1: Input = [SOS]           → Modelo predice "Hello" ✓
Paso 2: Input = [SOS, "Hello"]  → Modelo predice "world" ✓
        (Usamos "Hello" real, no la predicción del modelo)
Paso 3: Input = [SOS, "Hello", "world"] → Modelo predice [EOS] ✓
```

**Ventajas de Teacher Forcing**:
- Entrenamiento más rápido y estable
- El modelo siempre ve la secuencia correcta
- Gradientes más informativos

**Desventaja - Exposure Bias**:
- Durante entrenamiento, el modelo SIEMPRE ve inputs correctos
- Durante inferencia, el modelo ve SUS PROPIAS predicciones (posiblemente erróneas)
- El modelo nunca aprendió a recuperarse de errores

### Modo de Inferencia: Autoregresivo

**Analogía**: Ahora conduces solo, sin instructor. Cada decisión que tomas afecta la siguiente.

```
Paso 1: Input = [SOS]           → Modelo predice "Hello"
Paso 2: Input = [SOS, "Hello"]  → Modelo predice "world"
        (Usamos la predicción anterior, no la respuesta correcta)
Paso 3: Input = [SOS, "Hello", "world"] → Modelo predice [EOS]
```

**Problema del Error Acumulativo**:
```
Si el modelo predice mal:
Paso 1: Input = [SOS]      → Predice "Hi" (debía ser "Hello")
Paso 2: Input = [SOS, "Hi"] → El modelo nunca vio "Hi" en entrenamiento
                              → Predice algo raro como "there"
Paso 3: Los errores se acumulan...
```

### Solución: Scheduled Sampling

Técnica que mezcla gradualmente teacher forcing con predicciones del modelo:
- Al inicio: 100% teacher forcing
- Gradualmente: 90%, 80%, 70%... de teacher forcing
- Al final: Mayormente predicciones propias

### Respuesta Resumen

| Aspecto | Entrenamiento | Inferencia |
|---------|---------------|------------|
| Input al decoder | Secuencia correcta (ground truth) | Predicción anterior del modelo |
| Técnica | Teacher Forcing | Autoregresivo |
| Errores | Se corrigen inmediatamente | Se acumulan |
| Velocidad | Puede paralelizarse | Secuencial obligatorio |

---

## Ejercicio 7: Tokens Especiales SOS y EOS

### Enunciado
Explicar el propósito de los tokens especiales SOS (Start of Sequence) y EOS (End of Sequence) en modelos Seq2Seq.

### ¿Qué son SOS y EOS? (Explicación Básica)

**Analogía del libro**:
- **SOS** es como la portada de un libro: indica "aquí comienza la historia"
- **EOS** es como la palabra "FIN": indica "la historia terminó"

Sin estos tokens, el modelo no sabría cuándo empezar o terminar de generar texto.

### Token SOS (Start of Sequence)

**Propósito**: Dar al decoder un "punto de partida" para comenzar la generación.

```
Sin SOS: ¿Con qué alimentamos el decoder en el paso 1?
         El decoder necesita un input inicial, pero no hay palabra previa.

Con SOS:
         Paso 1: Input = [SOS] → Modelo genera primera palabra
         Paso 2: Input = primera palabra → Modelo genera segunda palabra
         ...
```

**Función técnica**:
- Es un token especial en el vocabulario (ej: índice 1)
- Tiene su propio embedding que el modelo aprende
- Actúa como "señal de inicio" para el decoder

### Token EOS (End of Sequence)

**Propósito**: Indicar al modelo cuándo debe DEJAR de generar.

```
Sin EOS: ¿Cómo sabe el modelo cuándo parar?
         Podría generar infinitamente: "Hello world how are you today..."

Con EOS:
         Entrada: "Hola" → Salida deseada: "Hello [EOS]"
         El modelo aprende que después de "Hello" debe generar [EOS]
```

**En inferencia**:
```
while True:
    next_token = modelo.predecir()
    if next_token == EOS:
        break  # ¡Terminamos!
    output.append(next_token)
```

### Ejemplo Completo

```
Traducción: "Hola mundo" → "Hello world"

ENCODER recibe: [Hola, mundo]
DECODER recibe y genera:

Paso 0: Input = [SOS]         → Output = "Hello"
Paso 1: Input = "Hello"       → Output = "world"
Paso 2: Input = "world"       → Output = [EOS]    ← Señal de parar
```

### Respuesta Resumen

| Token | Significado | Propósito |
|-------|-------------|-----------|
| **SOS** | Start of Sequence | Input inicial del decoder; señal de "empieza a generar" |
| **EOS** | End of Sequence | Señal de "deja de generar"; criterio de parada en inferencia |

**Nota**: Algunos modelos usan otros nombres como `<s>`, `</s>`, `[CLS]`, `[SEP]`, `<bos>`, `<eos>`, pero el concepto es el mismo.

---

## Ejercicio 8: Pesos de Atención en Seq2Seq

### Enunciado
Dado un encoder que produce 4 hidden states y un decoder en el paso t, explicar cómo se calculan los pesos de atención y qué representan.

### ¿Qué son los Pesos de Atención? (Explicación Básica)

**Analogía**: Imagina que estás traduciendo la palabra "gato" al inglés:
- Los pesos de atención te dicen "mira principalmente la posición 2 de la entrada"
- Es como un resaltador que marca las partes relevantes del texto original

### Configuración del Problema

```
Encoder produce 4 hidden states: h₁, h₂, h₃, h₄
(Correspondientes a 4 palabras de entrada)

Decoder está en el paso t con estado sₜ
```

### Cálculo de los Pesos de Atención

**Paso 1: Calcular scores (similitudes)**

Para cada hidden state del encoder, calculamos qué tan "relevante" es para el estado actual del decoder.

```
Método común - Producto punto:
score(sₜ, hᵢ) = sₜ · hᵢ

Ejemplo numérico:
e₁ = sₜ · h₁ = 2.1
e₂ = sₜ · h₂ = 4.5  ← más similar
e₃ = sₜ · h₃ = 1.2
e₄ = sₜ · h₄ = 0.8
```

**Paso 2: Aplicar Softmax**

Convertir scores en probabilidades (que suman 1).

```
α₁ = softmax(e₁) = e^2.1 / (e^2.1 + e^4.5 + e^1.2 + e^0.8) ≈ 0.08
α₂ = softmax(e₂) = e^4.5 / (...) ≈ 0.82  ← mayor peso
α₃ = softmax(e₃) ≈ 0.03
α₄ = softmax(e₄) ≈ 0.02

Verificación: 0.08 + 0.82 + 0.03 + 0.02 ≈ 1.0 ✓
```

**Paso 3: Calcular el Context Vector**

```
cₜ = α₁·h₁ + α₂·h₂ + α₃·h₃ + α₄·h₄
cₜ = 0.08·h₁ + 0.82·h₂ + 0.03·h₃ + 0.02·h₄
```

El context vector es principalmente h₂, con pequeñas contribuciones de los demás.

### ¿Qué Representan los Pesos?

Los pesos de atención αᵢ representan:

1. **Relevancia**: Qué tan importante es cada posición de entrada para la predicción actual
2. **Alineamiento**: En traducción, qué palabras de entrada corresponden a la palabra que estamos generando
3. **Distribución de probabilidad**: Suman 1, interpretable como "probabilidad de atender a cada posición"

### Visualización

```
Entrada:    "El    gato   negro   duerme"
             ↓      ↓       ↓        ↓
Pesos:     0.05   0.70    0.20     0.05
             ↓      ↓       ↓        ↓
Salida:              "cat"
                      ↑
         El modelo "atiende" principalmente a "gato"
```

### Respuesta Resumen

Los pesos de atención se calculan mediante:
1. **Score**: Similitud entre estado del decoder y cada estado del encoder
2. **Softmax**: Normalización para obtener probabilidades
3. **Promedio ponderado**: Combinar hidden states según los pesos

Representan la **relevancia** de cada posición de entrada para la predicción actual del decoder.

---

## Ejercicio 9: Rol del Encoder vs Decoder

### Enunciado
Explicar las diferencias fundamentales entre el encoder y el decoder en una arquitectura Seq2Seq.

### Encoder: El "Lector"

**Analogía**: El encoder es como alguien que lee un libro completo y toma notas detalladas.

**Características**:
```
Entrada: Secuencia completa (ej: oración en español)
         "El gato negro"
              ↓
Proceso: Lee TODA la secuencia
         Puede ver pasado Y futuro (bidireccional posible)
              ↓
Salida:  Hidden states para cada posición
         h₁, h₂, h₃ (representaciones contextualizadas)
```

**Propiedades del Encoder**:
- Procesa la entrada de forma **no autoregresiva** (puede paralelizar)
- Puede ser **bidireccional** (ver contexto completo)
- Su trabajo es **comprender** y **representar** la entrada
- No genera nada, solo crea representaciones

### Decoder: El "Escritor"

**Analogía**: El decoder es como un escritor que mira las notas y escribe un nuevo texto, palabra por palabra.

**Características**:
```
Entrada: Token anterior + Context del encoder
         [SOS] + representación de "El gato negro"
              ↓
Proceso: Genera UN token a la vez
         Solo puede ver el PASADO (unidireccional)
              ↓
Salida:  Siguiente token
         "The" → "black" → "cat" → [EOS]
```

**Propiedades del Decoder**:
- Procesa de forma **autoregresiva** (secuencial obligatorio en inferencia)
- Es **unidireccional** (solo ve tokens ya generados)
- Su trabajo es **generar** la secuencia de salida
- Usa masked self-attention para no ver el futuro

### Tabla Comparativa

| Aspecto | Encoder | Decoder |
|---------|---------|---------|
| **Función** | Comprender entrada | Generar salida |
| **Direccionalidad** | Bidireccional posible | Unidireccional (causal) |
| **Input** | Secuencia completa | Token anterior + context |
| **Output** | Hidden states | Tokens generados |
| **Paralelizable** | Sí (entrenamiento) | No en inferencia |
| **Atención** | Self-attention | Self-attention + Cross-attention |

### Cross-Attention: El Puente

El decoder usa **cross-attention** para conectarse con el encoder:
- **Query**: Viene del decoder (estado actual)
- **Key, Value**: Vienen del encoder (representaciones de entrada)

```
Decoder pregunta: "¿Qué parte de la entrada necesito para generar la siguiente palabra?"
Encoder responde: Los hidden states con sus pesos de atención
```

### Respuesta Resumen

**Encoder**:
- Lee y comprende la secuencia de entrada
- Produce representaciones contextualizadas
- Puede procesar en paralelo y bidireccionalmente

**Decoder**:
- Genera la secuencia de salida token por token
- Solo puede mirar hacia atrás (causal)
- Usa cross-attention para consultar al encoder

---

## Ejercicio 10: Interpretación de Mapas de Atención

### Enunciado
Dado un mapa de atención de una traducción español-inglés, interpretar qué indican los patrones observados.

### ¿Qué es un Mapa de Atención?

**Analogía**: Es como una fotografía térmica de "dónde mira" el modelo cuando genera cada palabra.

```
               ENTRADA (Español)
               El   gato  negro  duerme
SALIDA    The  0.1  0.3   0.1    0.5
(Inglés)  black 0.1 0.2   0.6    0.1
          cat  0.1  0.7   0.1    0.1
          sleeps 0.1 0.1  0.1    0.7
```

### Patrones Típicos

**1. Patrón Diagonal (Alineamiento Monótono)**
```
    E₁   E₂   E₃   E₄
D₁  ██
D₂       ██
D₃            ██
D₄                 ██
```
- Las palabras se corresponden en orden
- Típico en idiomas con orden similar (español-inglés)

**2. Patrón Difuso**
```
    E₁   E₂   E₃   E₄
D₁  ░░   ░░   ░░   ██
D₂  ░░   ██   ░░   ░░
D₃  ██   ░░   ░░   ░░
```
- Indica reordenamiento de palabras
- Típico cuando los idiomas tienen diferente estructura

**3. Patrón de Atención Fuerte**
```
    E₁   E₂   E₃   E₄
D₁  0.0  0.9  0.1  0.0
```
- El modelo está muy seguro de la correspondencia
- Útil para palabras con traducción directa

### Ejemplo de Interpretación

```
Entrada: "El perro grande ladra"
Salida:  "The big dog barks"

Mapa de atención:
              El   perro  grande  ladra
    The      0.6   0.2    0.1     0.1
    big      0.1   0.2    0.6     0.1   ← "big" mira a "grande"
    dog      0.1   0.7    0.1     0.1   ← "dog" mira a "perro"
    barks    0.1   0.1    0.1     0.7   ← "barks" mira a "ladra"
```

**Observaciones**:
1. "big" atiende fuertemente a "grande" (traducción directa)
2. "dog" atiende fuertemente a "perro" (traducción directa)
3. El orden cambia: en español "perro grande", en inglés "big dog"
4. El mapa muestra este reordenamiento (no es diagonal perfecta)

### Usos de los Mapas de Atención

1. **Depuración**: Ver si el modelo está "mirando" las palabras correctas
2. **Interpretabilidad**: Entender las decisiones del modelo
3. **Detección de errores**: Patrones extraños indican problemas
4. **Alineamiento automático**: Crear diccionarios de traducción

### Respuesta Resumen

Los mapas de atención muestran:
- **Qué palabras de entrada** el modelo considera al generar cada palabra de salida
- **Patrones de alineamiento** entre idiomas
- **Reordenamientos** cuando el orden difiere entre idiomas
- **Confianza del modelo** (valores más altos = más seguridad)

---

# SECCIÓN 3: RESNETS Y CONEXIONES RESIDUALES (Ejercicios 11-15)

---

## Ejercicio 11: Skip Connections en ResNets

### Enunciado
Explicar qué son las skip connections (conexiones residuales) y por qué son importantes en redes profundas.

### ¿Qué es una Skip Connection? (Explicación Básica)

**Analogía del Teléfono Descompuesto**:
- En una red tradicional: A susurra a B, B susurra a C, C susurra a D...
- El mensaje se distorsiona con cada paso
- En ResNet: A también puede hablar DIRECTAMENTE con D, saltándose intermediarios

**Fórmula Clave**:
```
Red tradicional: H(x) = F(x)        "La salida es lo que calcula la capa"
ResNet:          H(x) = F(x) + x    "La salida es lo calculado MÁS la entrada original"
```

### Visualización

```
RED TRADICIONAL:
    x → [Capa 1] → [Capa 2] → [Capa 3] → y

RESNET con Skip Connection:
    x ──────────────────────────────────┐
    │                                   │
    ↓                                   ↓
    x → [Capa 1] → [Capa 2] → [Capa 3] → (+) → y = F(x) + x
                                         ↑
                              La entrada se SUMA a la salida
```

### ¿Por qué F(x) + x en lugar de solo F(x)?

**Intuición**: Es más fácil aprender "qué cambiar" que "todo desde cero".

**Analogía del Editor de Fotos**:
- Sin skip: El modelo debe reconstruir toda la imagen desde cero
- Con skip: El modelo solo aprende los "ajustes" (brillo, contraste) sobre la imagen original

**Matemáticamente**:
```
Si la transformación óptima es H(x) = x (identidad):
- Sin skip: F debe aprender F(x) = x (difícil)
- Con skip: F debe aprender F(x) = 0 (fácil, solo poner pesos en 0)
```

### Beneficios de las Skip Connections

1. **Resuelve el problema del gradiente que desaparece**:
   - El gradiente tiene un "camino directo" hacia atrás
   - No se multiplica por muchos pesos pequeños

2. **Permite redes más profundas**:
   - ResNet-152 funciona bien; redes tradicionales de 152 capas fallan

3. **Aprendizaje residual**:
   - El modelo aprende "correcciones" sobre la entrada
   - Si una capa no ayuda, puede aprender F(x) = 0

### Respuesta Resumen

**Skip Connections** son conexiones que saltan capas y suman la entrada original a la salida:
- Fórmula: H(x) = F(x) + x
- Permiten que el gradiente fluya sin degradarse
- Hacen posible entrenar redes muy profundas (100+ capas)
- El modelo aprende "residuos" (cambios) en lugar de transformaciones completas

---

## Ejercicio 12: Degradación vs Overfitting

### Enunciado
Explicar la diferencia entre el problema de degradación y el overfitting en redes neuronales profundas.

### El Problema de Degradación

**Definición**: A medida que agregamos más capas, el ERROR DE ENTRENAMIENTO (no solo el de validación) AUMENTA.

**Esto es contraintuitivo**: Si una red de 20 capas funciona bien, una de 56 debería funcionar AL MENOS igual de bien (las capas extra podrían ser identidades).

```
Capas:          20      30      40      50      56
Error Train:    5%      6%      7%      8%      9%   ← ¡AUMENTA!
Error Val:      7%      8%      9%      10%     11%

¡Ambos errores suben! Esto NO es overfitting.
```

**Causa**: Las capas adicionales no logran aprender ni siquiera la función identidad.

### El Problema de Overfitting

**Definición**: El modelo memoriza los datos de entrenamiento pero no generaliza.

```
Capas:          20      30      40      50      56
Error Train:    5%      3%      1%      0.5%    0.1%  ← BAJA
Error Val:      7%      10%     15%     20%     25%   ← SUBE

El error de entrenamiento baja, pero el de validación sube.
```

**Causa**: El modelo es demasiado complejo para los datos disponibles.

### Comparación Visual

```
DEGRADACIÓN:                    OVERFITTING:
Error                           Error
  │    Train ↗                    │         Val ↗
  │    Val ↗                      │
  │   ↗                           │         ↗
  │ ↗                             │       ↗
  │↗                              │     ↗
  └──────────→ Capas              │   Train ↘
                                  │     ↘
                                  └──────────→ Capas
```

### Tabla Comparativa

| Aspecto | Degradación | Overfitting |
|---------|-------------|-------------|
| Error de entrenamiento | Aumenta | Disminuye |
| Error de validación | Aumenta | Aumenta |
| Causa | Dificultad de optimización | Exceso de capacidad |
| Solución | Skip connections (ResNet) | Regularización, más datos |
| Relación con profundidad | Empeora con más capas | Empeora con más parámetros |

### Soluciones

**Para Degradación**:
- Skip connections (ResNets)
- Batch normalization
- Mejor inicialización de pesos

**Para Overfitting**:
- Regularización (L1, L2, Dropout)
- Más datos de entrenamiento
- Data augmentation
- Early stopping

### Respuesta Resumen

| Problema | Síntoma | Causa | Solución |
|----------|---------|-------|----------|
| **Degradación** | Ambos errores suben con más capas | Optimización difícil | ResNets, skip connections |
| **Overfitting** | Error train baja, error val sube | Modelo memoriza | Regularización, más datos |

---

## Ejercicio 13: Convoluciones 1×1

### Enunciado
Explicar el propósito de las convoluciones 1×1 en las arquitecturas ResNet.

### ¿Qué es una Convolución 1×1? (Explicación Básica)

**Analogía**: Imagina que tienes una imagen con 256 "capas" de colores. Una conv 1×1 es como mezclar esos colores pixel por pixel, sin mirar a los vecinos.

```
Convolución 3×3: Mira un vecindario de 9 pixels
Convolución 1×1: Mira SOLO 1 pixel, pero todos sus canales
```

### Visualización

```
INPUT: 56×56×256 (altura × ancho × canales)
                ↓
        Conv 1×1 con 64 filtros
                ↓
OUTPUT: 56×56×64 (misma altura/ancho, menos canales)

Cada posición (i,j):
- Toma los 256 valores del input en (i,j)
- Aplica una combinación lineal
- Produce 64 valores de output en (i,j)
```

### Propósitos en ResNet

**1. Reducción de Dimensionalidad (Bottleneck)**

```
Antes del Bottleneck:
    Input: 256 canales
       ↓
    Conv 3×3, 256 filtros (COSTOSO: 256×256×9 = 589,824 params)
       ↓
    Output: 256 canales

Con Bottleneck:
    Input: 256 canales
       ↓
    Conv 1×1, 64 filtros (BARATO: 256×64×1 = 16,384 params)
       ↓
    Conv 3×3, 64 filtros (BARATO: 64×64×9 = 36,864 params)
       ↓
    Conv 1×1, 256 filtros (BARATO: 64×256×1 = 16,384 params)
       ↓
    Output: 256 canales

Total sin bottleneck: 589,824 params
Total con bottleneck: 69,632 params (¡88% menos!)
```

**2. Ajuste de Dimensiones para Skip Connections**

Cuando la skip connection cruza un cambio de dimensión:
```
    x (56×56×64) ─────────────────────────┐
           ↓                              ↓
    [Conv que reduce a 28×28×128]    Conv 1×1 (64→128) + stride 2
           ↓                              ↓
        F(x) (28×28×128)    +    x' (28×28×128)
```

**3. Aumento de No-Linealidad**

Cada conv 1×1 va seguida de BatchNorm y ReLU:
```
Conv 1×1 → BatchNorm → ReLU → Conv 3×3 → BatchNorm → ReLU → Conv 1×1 → BatchNorm → ReLU
```
Esto añade más no-linealidad sin costo espacial.

### Bloque Bottleneck Completo

```
              x (256 canales)
              │
    ┌─────────┴─────────┐
    │                   │
    ↓                   │
Conv 1×1 (256→64)       │  ← Reducir
    ↓                   │
BatchNorm + ReLU        │
    ↓                   │
Conv 3×3 (64→64)        │  ← Procesar (económico)
    ↓                   │
BatchNorm + ReLU        │
    ↓                   │
Conv 1×1 (64→256)       │  ← Expandir
    ↓                   │
BatchNorm               │
    │                   │
    └────────(+)────────┘
              ↓
           ReLU
              ↓
         y (256 canales)
```

### Respuesta Resumen

Las **convoluciones 1×1** en ResNet sirven para:

1. **Reducir parámetros**: Comprimir canales antes de convs costosas (bottleneck)
2. **Ajustar dimensiones**: Hacer que skip connections funcionen cuando cambian las dimensiones
3. **Añadir no-linealidad**: Más capas de activación sin costo espacial
4. **Mezclar canales**: Combinar información de diferentes feature maps

---

## Ejercicio 14: Suma vs Concatenación

### Enunciado
Comparar las operaciones de suma y concatenación para combinar features en redes residuales.

### Operación de SUMA (ResNet)

```
x (64 canales) ────────────────────┐
       ↓                           │
   F(x) (64 canales)               │
       ↓                           ↓
       └───────────( + )───────────┘
                    ↓
            Salida (64 canales)
```

**Características**:
- Mantiene el número de canales
- Combina la información "mezclándola"
- Más eficiente en memoria
- Fuerza a F(x) y x a tener las mismas dimensiones

### Operación de CONCATENACIÓN (DenseNet)

```
x (64 canales) ────────────────────┐
       ↓                           │
   F(x) (64 canales)               │
       ↓                           ↓
       └───────[ concat ]──────────┘
                    ↓
            Salida (128 canales)
```

**Características**:
- Duplica (o más) el número de canales
- Preserva información separadamente
- Usa más memoria
- Permite diferentes dimensiones de F(x) y x

### Comparación Detallada

| Aspecto | Suma (ResNet) | Concatenación (DenseNet) |
|---------|---------------|--------------------------|
| **Canales de salida** | Igual que entrada | Suma de ambas entradas |
| **Memoria** | Eficiente | Crece rápidamente |
| **Información** | Se mezcla | Se preserva por separado |
| **Gradiente** | Directo, constante | Directo, pero más paths |
| **Requisito dim.** | F(x) y x deben coincidir | Pueden diferir |

### Ejemplo Numérico

```
SUMA:
x = [1, 2, 3, 4]  (4 canales)
F(x) = [0.5, -0.5, 0.1, 0.2]  (4 canales)
Salida = [1.5, 1.5, 3.1, 4.2]  (4 canales)

CONCATENACIÓN:
x = [1, 2, 3, 4]  (4 canales)
F(x) = [0.5, -0.5, 0.1, 0.2]  (4 canales)
Salida = [1, 2, 3, 4, 0.5, -0.5, 0.1, 0.2]  (8 canales)
```

### ¿Cuándo usar cada una?

**Usar SUMA cuando**:
- Se necesita eficiencia de memoria
- El objetivo es aprender residuos (cambios pequeños)
- Las dimensiones ya coinciden

**Usar CONCATENACIÓN cuando**:
- Se quiere preservar toda la información
- Se tienen features muy diferentes que no deben mezclarse
- El costo de memoria no es crítico

### DenseNet: Ejemplo de Concatenación

```
Capa 1: x₀ → F₁(x₀)
        Salida: [x₀, F₁(x₀)]

Capa 2: [x₀, F₁(x₀)] → F₂(...)
        Salida: [x₀, F₁(x₀), F₂(...)]

Capa 3: [x₀, F₁(x₀), F₂(...)] → F₃(...)
        Salida: [x₀, F₁(x₀), F₂(...), F₃(...)]

¡Cada capa tiene acceso a TODAS las features anteriores!
```

### Respuesta Resumen

| Operación | Fórmula | Uso Principal | Arquitectura |
|-----------|---------|---------------|--------------|
| **Suma** | y = F(x) + x | Aprendizaje residual, eficiencia | ResNet |
| **Concatenación** | y = [F(x), x] | Reutilización densa de features | DenseNet |

---

## Ejercicio 15: Gradiente en Skip Connections

### Enunciado
Demostrar matemáticamente cómo las skip connections ayudan con el flujo del gradiente.

### El Problema del Gradiente que Desaparece

**Sin skip connections**, el gradiente se multiplica en cada capa:

```
Gradiente = ∂L/∂x₁ = (∂L/∂xₙ) × (∂xₙ/∂xₙ₋₁) × ... × (∂x₂/∂x₁)

Si cada factor < 1:
0.5 × 0.5 × 0.5 × 0.5 × ... = casi 0

Los pesos de las primeras capas no se actualizan.
```

### Análisis Matemático con Skip Connections

**Definición de un bloque residual**:
```
y = F(x) + x
```

**Calculemos el gradiente**:
```
∂y/∂x = ∂F(x)/∂x + ∂x/∂x
∂y/∂x = ∂F(x)/∂x + 1
```

**El término "+1" es clave**: Siempre hay un camino de gradiente = 1.

### Ejemplo con Múltiples Bloques

```
Bloque 1: y₁ = F₁(x) + x
Bloque 2: y₂ = F₂(y₁) + y₁
Bloque 3: y₃ = F₃(y₂) + y₂
```

**Gradiente de y₃ respecto a x**:
```
∂y₃/∂x = ∂y₃/∂y₂ × ∂y₂/∂y₁ × ∂y₁/∂x

∂y₁/∂x = ∂F₁/∂x + 1
∂y₂/∂y₁ = ∂F₂/∂y₁ + 1
∂y₃/∂y₂ = ∂F₃/∂y₂ + 1
```

**Expandiendo**:
```
∂y₃/∂x = (∂F₃/∂y₂ + 1) × (∂F₂/∂y₁ + 1) × (∂F₁/∂x + 1)

Esto incluye el término:
1 × 1 × 1 = 1

¡Siempre hay un "camino directo" con gradiente = 1!
```

### Visualización del Flujo de Gradiente

```
SIN SKIP CONNECTIONS:
L ← × ← × ← × ← × ← × ← x
    0.3  0.4  0.5  0.3  0.4

Gradiente final: 0.3×0.4×0.5×0.3×0.4 = 0.007 (¡casi 0!)

CON SKIP CONNECTIONS:
L ← + ← + ← + ← + ← + ← x
    │   │   │   │   │
    1   1   1   1   1   (camino directo)

Gradiente mínimo: 1×1×1×1×1 = 1 (¡se preserva!)
```

### Demostración Formal

Para una red con L bloques residuales:

```
xₗ = xₗ₋₁ + F(xₗ₋₁, Wₗ₋₁)

El gradiente de la pérdida respecto a x₀:

∂ℒ/∂x₀ = ∂ℒ/∂xₗ × ∂xₗ/∂x₀

∂xₗ/∂x₀ = ∂/∂x₀[x₀ + Σᵢ F(xᵢ, Wᵢ)]
        = 1 + Σᵢ ∂F(xᵢ, Wᵢ)/∂x₀

El término "1" garantiza que el gradiente nunca sea 0.
```

### Por qué funciona

1. **Camino corto**: El gradiente puede "saltar" directamente por la skip connection
2. **Suma, no multiplicación**: Los gradientes se SUMAN, no se multiplican
3. **Gradiente residual**: Incluso si ∂F/∂x es pequeño, el "1" lo rescata

### Respuesta Resumen

**Sin skip connections**:
```
∂y/∂x = ∂F₁/∂x × ∂F₂/∂F₁ × ... → Producto de términos pequeños → ≈ 0
```

**Con skip connections**:
```
∂y/∂x = (∂F₁/∂x + 1) × (∂F₂/∂y₁ + 1) × ... → Incluye términos "1" → ≠ 0
```

Las skip connections garantizan que siempre exista un "camino directo" con gradiente = 1, evitando el problema del gradiente que desaparece.

---

# SECCIÓN 4: RNN, LSTM Y GRU (Ejercicios 16-19)

---

## Ejercicio 16: Ecuaciones de una RNN Simple

### Enunciado
Escribir y explicar las ecuaciones de una RNN simple, identificando cada matriz de pesos.

### ¿Qué es una RNN? (Explicación Básica)

**Analogía**: Una RNN es como leer un libro y tomar notas mentales:
- **Estado oculto (h)**: Tus notas mentales actuales
- **Entrada (x)**: La palabra que estás leyendo ahora
- **Salida (y)**: Tu interpretación actual

Lo especial es que las "notas" del paso anterior influyen en cómo interpretas la palabra actual.

### Ecuaciones de la RNN

```
hₜ = tanh(Wₕₓ · xₜ + Wₕₕ · hₜ₋₁ + bₕ)
yₜ = Wᵧₕ · hₜ + bᵧ
```

### Desglose de cada componente

**1. Estado oculto hₜ**:
```
hₜ = tanh(Wₕₓ · xₜ + Wₕₕ · hₜ₋₁ + bₕ)
     │     │    │    │     │     │
     │     │    │    │     │     └── Bias del estado oculto
     │     │    │    │     └──────── Estado oculto anterior (memoria)
     │     │    │    └────────────── Matriz que procesa la memoria
     │     │    └─────────────────── Entrada actual
     │     └──────────────────────── Matriz que procesa la entrada
     └────────────────────────────── Función de activación
```

**2. Salida yₜ**:
```
yₜ = Wᵧₕ · hₜ + bᵧ
     │     │    │
     │     │    └── Bias de salida
     │     └─────── Estado oculto actual
     └───────────── Matriz que genera la salida
```

### Las Matrices de Pesos

| Matriz | Dimensión | Función |
|--------|-----------|---------|
| **Wₕₓ** (o U) | hidden × input | Transforma la entrada al espacio oculto |
| **Wₕₕ** (o W) | hidden × hidden | Transforma el estado anterior (recurrencia) |
| **Wᵧₕ** (o V) | output × hidden | Genera la salida desde el estado oculto |

### Ejemplo Numérico

```
Configuración:
- Tamaño de entrada: 3
- Tamaño oculto: 2
- Tamaño de salida: 4

Dimensiones:
- Wₕₓ: (2 × 3) = 6 parámetros
- Wₕₕ: (2 × 2) = 4 parámetros
- Wᵧₕ: (4 × 2) = 8 parámetros
- bₕ: 2 parámetros
- bᵧ: 4 parámetros

Total: 6 + 4 + 8 + 2 + 4 = 24 parámetros
```

### Visualización del Flujo

```
Tiempo t-1              Tiempo t               Tiempo t+1
    │                      │                      │
    ↓                      ↓                      ↓
  xₜ₋₁                    xₜ                    xₜ₊₁
    │                      │                      │
    ↓ Wₕₓ                  ↓ Wₕₓ                  ↓ Wₕₓ
    ↓                      ↓                      ↓
hₜ₋₂→[RNN]→hₜ₋₁──Wₕₕ──→[RNN]→hₜ───Wₕₕ───→[RNN]→hₜ₊₁
              │              │               │
              ↓ Wᵧₕ          ↓ Wᵧₕ           ↓ Wᵧₕ
              ↓              ↓               ↓
            yₜ₋₁            yₜ             yₜ₊₁
```

### Notación Alternativa Común

A veces se usan otras letras:
```
hₜ = tanh(U · xₜ + W · hₜ₋₁ + b)
yₜ = V · hₜ + c

Donde:
- U = Wₕₓ (input-to-hidden)
- W = Wₕₕ (hidden-to-hidden)
- V = Wᵧₕ (hidden-to-output)
```

### Respuesta Resumen

**Ecuaciones RNN**:
```
hₜ = tanh(Wₕₓ · xₜ + Wₕₕ · hₜ₋₁ + bₕ)
yₜ = Wᵧₕ · hₜ + bᵧ
```

**Matrices**:
- **Wₕₓ (U)**: input → hidden
- **Wₕₕ (W)**: hidden → hidden (recurrencia)
- **Wᵧₕ (V)**: hidden → output

---

## Ejercicio 17: Backpropagation Through Time (BPTT)

### Enunciado
Explicar el algoritmo BPTT y por qué las RNNs sufren del problema del gradiente que desaparece.

### ¿Qué es BPTT? (Explicación Básica)

**Analogía**: BPTT es como revisar tus decisiones pasadas:
- Cometiste un error en el paso 10
- Para corregirlo, debes ver cómo cada decisión anterior (9, 8, 7...) contribuyó al error
- Retrocedes en el tiempo calculando la responsabilidad de cada paso

### El Algoritmo BPTT

**Paso 1: Forward Pass (hacia adelante)**
```
Para t = 1 hasta T:
    hₜ = tanh(U·xₜ + W·hₜ₋₁)
    yₜ = V·hₜ
    Lₜ = Loss(yₜ, target)
```

**Paso 2: Backward Pass (hacia atrás)**
```
Para t = T hasta 1:
    ∂L/∂yₜ = ∂Lₜ/∂yₜ
    ∂L/∂hₜ = ∂L/∂yₜ · V + ∂L/∂hₜ₊₁ · ∂hₜ₊₁/∂hₜ
    ∂L/∂W = Σₜ ∂L/∂hₜ · ∂hₜ/∂W
```

### Visualización del BPTT

```
Forward (→):
x₁ → h₁ → y₁ → L₁
      ↓
x₂ → h₂ → y₂ → L₂
      ↓
x₃ → h₃ → y₃ → L₃

Backward (←):
     ∂L₁ ←── ∂h₁ ←─┐
              ↑     │
     ∂L₂ ←── ∂h₂ ←─┤ (gradientes se acumulan)
              ↑     │
     ∂L₃ ←── ∂h₃ ←─┘
```

### El Problema del Gradiente que Desaparece

**El culpable: multiplicación repetida**

```
∂hₜ/∂hₜ₋ₖ = ∂hₜ/∂hₜ₋₁ × ∂hₜ₋₁/∂hₜ₋₂ × ... × ∂hₜ₋ₖ₊₁/∂hₜ₋ₖ

Cada término = W × diag(tanh'(hᵢ))

Si ||W|| < 1: El producto → 0 (gradiente desaparece)
Si ||W|| > 1: El producto → ∞ (gradiente explota)
```

**Ejemplo numérico**:
```
Si cada factor ≈ 0.5:
Después de 10 pasos: 0.5¹⁰ ≈ 0.001
Después de 20 pasos: 0.5²⁰ ≈ 0.000001

¡El gradiente prácticamente desaparece!
```

### Por qué tanh empeora el problema

```
tanh(x) tiene derivada máxima = 1 (en x=0)
tanh'(x) < 1 para x ≠ 0

Esto significa que casi siempre estamos multiplicando por números < 1
```

### Visualización del Gradiente Decayendo

```
Pérdida en t=10
     │
Gradiente hacia atrás:
     │
t=10: |████████████████████| = 1.0
t=9:  |██████████████████  | = 0.8
t=8:  |████████████████    | = 0.6
t=7:  |██████████████      | = 0.5
t=6:  |████████████        | = 0.4
t=5:  |██████████          | = 0.3
t=4:  |████████            | = 0.2
t=3:  |██████              | = 0.1
t=2:  |████                | = 0.05
t=1:  |██                  | = 0.01  ← ¡Casi no aprende!
```

### Consecuencias

1. **No aprende dependencias lejanas**: Si la información relevante está en t=1 pero la pérdida en t=20, no hay gradiente significativo
2. **Sesgo hacia lo reciente**: El modelo aprende mejor las relaciones cercanas
3. **Límite práctico de ~10-20 pasos**

### Soluciones

| Solución | Cómo funciona |
|----------|---------------|
| **LSTM** | Gates que permiten gradiente constante |
| **GRU** | Versión simplificada de LSTM |
| **Gradient clipping** | Limita el gradiente máximo |
| **Skip connections** | Caminos directos de gradiente |

### Respuesta Resumen

**BPTT** retropropaga el error a través del tiempo, calculando cómo cada paso contribuyó a la pérdida final.

**Problema del gradiente que desaparece**:
- El gradiente se multiplica en cada paso
- Si los factores son < 1, el producto → 0
- Las dependencias lejanas no pueden aprenderse
- Solución principal: LSTM/GRU con mecanismos de compuerta

---

## Ejercicio 18: LSTM vs GRU

### Enunciado
Comparar las arquitecturas LSTM y GRU, explicando sus mecanismos de compuerta.

### ¿Por qué necesitamos compuertas? (Explicación Básica)

**Analogía del estudiante tomando notas**:
- **RNN simple**: Reescribes todas tus notas en cada clase (olvidas todo lo anterior)
- **LSTM/GRU**: Decides qué borrar, qué mantener, y qué agregar de nuevo

Las compuertas son como "filtros" que controlan el flujo de información.

### LSTM (Long Short-Term Memory)

**4 componentes principales**:

```
1. Forget Gate (fₜ): ¿Qué olvidar del pasado?
   fₜ = σ(Wf·[hₜ₋₁, xₜ] + bf)

2. Input Gate (iₜ): ¿Qué información nueva guardar?
   iₜ = σ(Wi·[hₜ₋₁, xₜ] + bi)

3. Candidate Memory (c̃ₜ): ¿Cuál es la información nueva?
   c̃ₜ = tanh(Wc·[hₜ₋₁, xₜ] + bc)

4. Output Gate (oₜ): ¿Qué mostrar como salida?
   oₜ = σ(Wo·[hₜ₋₁, xₜ] + bo)
```

**Actualización de la memoria**:
```
cₜ = fₜ ⊙ cₜ₋₁ + iₜ ⊙ c̃ₜ     (memoria de largo plazo)
hₜ = oₜ ⊙ tanh(cₜ)           (salida/estado oculto)

⊙ = multiplicación elemento a elemento
```

### GRU (Gated Recurrent Unit)

**2 compuertas principales** (más simple):

```
1. Reset Gate (rₜ): ¿Cuánto del pasado usar para calcular lo nuevo?
   rₜ = σ(Wr·[hₜ₋₁, xₜ] + br)

2. Update Gate (zₜ): ¿Cuánto actualizar vs mantener?
   zₜ = σ(Wz·[hₜ₋₁, xₜ] + bz)
```

**Actualización del estado**:
```
h̃ₜ = tanh(W·[rₜ ⊙ hₜ₋₁, xₜ])   (candidato)
hₜ = (1-zₜ) ⊙ hₜ₋₁ + zₜ ⊙ h̃ₜ   (interpolación)
```

### Comparación Visual

```
LSTM:
        ┌────────────────────────────────┐
        │         Cell State (c)         │
        │   ────×────────(+)────×────    │
        │       │         │     │        │
        │       │    ┌────┴────┐│        │
        │       │    │   tanh  ││        │
        │    forget  │         ││        │
        │    gate    │  input  │output   │
        │      ↑     │  gate   │ gate    │
        │      │     │   ↑     │  ↑      │
        └──────┴─────┴───┴─────┴──┴──────┘
              σ     tanh  σ       σ
              │      │    │       │
              └──────┴────┴───────┘
                   [hₜ₋₁, xₜ]

GRU:
        ┌────────────────────────────────┐
        │      ┌──────(×)────────┐       │
        │      │                 │       │
        │   (1-z)               (z)      │
        │      │                 │       │
        │      │            ┌────┴────┐  │
        │      │            │  tanh   │  │
        │      │            │         │  │
        │   hₜ₋₁      reset gate     update gate
        │      │            ↑          ↑        │
        └──────┴────────────┴──────────┴────────┘
```

### Tabla Comparativa

| Aspecto | LSTM | GRU |
|---------|------|-----|
| **Compuertas** | 3 (forget, input, output) | 2 (reset, update) |
| **Estados** | 2 (cell state c, hidden h) | 1 (hidden h) |
| **Parámetros** | 4 conjuntos de pesos | 3 conjuntos de pesos |
| **Complejidad** | Mayor | Menor (~33% menos params) |
| **Memoria separada** | Sí (cell state) | No |
| **Rendimiento** | Mejor en secuencias muy largas | Similar o mejor en muchos casos |

### Conteo de Parámetros

```
Para: input_size = n, hidden_size = h

LSTM: 4 × (h×(n+h) + h) = 4h(n+h) + 4h
      (4 conjuntos: Wf, Wi, Wc, Wo)

GRU:  3 × (h×(n+h) + h) = 3h(n+h) + 3h
      (3 conjuntos: Wr, Wz, W)

GRU tiene ~75% de los parámetros de LSTM
```

### ¿Cuándo usar cada uno?

**Usar LSTM cuando**:
- Secuencias muy largas (1000+ tokens)
- Se necesita memoria de largo plazo muy precisa
- Hay recursos computacionales suficientes

**Usar GRU cuando**:
- Recursos limitados (móviles, edge)
- Secuencias moderadas
- Se necesita entrenamiento más rápido
- Datos de entrenamiento limitados

### Respuesta Resumen

| Característica | LSTM | GRU |
|----------------|------|-----|
| Gates | forget, input, output | reset, update |
| Estados | cell + hidden | solo hidden |
| Parámetros | Más | ~25% menos |
| Memoria | Explícita (cell state) | Implícita |
| Uso ideal | Secuencias muy largas | Eficiencia, secuencias medias |

---

## Ejercicio 19: Conteo de Parámetros en RNNs

### Enunciado
Calcular el número de parámetros de una RNN, LSTM y GRU con:
- Tamaño de entrada: input_size = 100
- Tamaño oculto: hidden_size = 256

### RNN Simple

**Matrices**:
```
U (input → hidden):  hidden × input = 256 × 100 = 25,600
W (hidden → hidden): hidden × hidden = 256 × 256 = 65,536
bₕ (bias hidden):    hidden = 256
```

**Total RNN**:
```
25,600 + 65,536 + 256 = 91,392 parámetros
```

### LSTM

**4 conjuntos de pesos** (forget, input, cell, output):

```
Para cada gate/componente:
  - W (input parte):   hidden × input = 256 × 100 = 25,600
  - W (hidden parte):  hidden × hidden = 256 × 256 = 65,536
  - bias:              hidden = 256

Total por gate = 25,600 + 65,536 + 256 = 91,392

4 gates × 91,392 = 365,568 parámetros
```

**Desglose**:
```
Forget gate:    91,392
Input gate:     91,392
Cell gate:      91,392
Output gate:    91,392
─────────────────────
Total LSTM:    365,568 parámetros
```

### GRU

**3 conjuntos de pesos** (reset, update, candidate):

```
Reset gate:     91,392
Update gate:    91,392
Candidate:      91,392
─────────────────────
Total GRU:     274,176 parámetros
```

### Comparación Final

| Modelo | Parámetros | % vs RNN |
|--------|------------|----------|
| **RNN** | 91,392 | 100% |
| **LSTM** | 365,568 | 400% (4× RNN) |
| **GRU** | 274,176 | 300% (3× RNN) |

### Fórmula General

```
RNN:  params = hidden × (input + hidden) + hidden
            = h × (n + h + 1)  [con bias]

LSTM: params = 4 × [hidden × (input + hidden) + hidden]
            = 4 × h × (n + h + 1)

GRU:  params = 3 × [hidden × (input + hidden) + hidden]
            = 3 × h × (n + h + 1)
```

### Verificación con nuestra configuración

```
n = 100, h = 256

RNN:  256 × (100 + 256 + 1) = 256 × 357 = 91,392 ✓
LSTM: 4 × 91,392 = 365,568 ✓
GRU:  3 × 91,392 = 274,176 ✓
```

### Respuesta Final

| Modelo | Fórmula | Parámetros |
|--------|---------|------------|
| **RNN** | h(n + h) + h | **91,392** |
| **LSTM** | 4 × [h(n + h) + h] | **365,568** |
| **GRU** | 3 × [h(n + h) + h] | **274,176** |

**Nota**: El LSTM tiene exactamente 4× los parámetros de una RNN simple, y GRU tiene 3×.

---

# SECCIÓN 5: WORD2VEC Y MODELOS DE LENGUAJE (Ejercicios 20-23)

---

## Ejercicio 20: Word2Vec - CBOW vs Skip-Gram

### Enunciado
Explicar las diferencias entre los modelos CBOW y Skip-Gram de Word2Vec.

### ¿Qué es Word2Vec? (Explicación Básica)

**Idea central**: Las palabras que aparecen en contextos similares tienen significados similares.

**Analogía**: "Dime con quién andas y te diré quién eres"
- Si "perro" y "gato" aparecen en contextos similares ("el ___ come", "mi ___ duerme")
- Entonces sus vectores serán similares

### CBOW (Continuous Bag of Words)

**Objetivo**: Predecir la palabra central dado el contexto.

```
Contexto: "el gato ___ sobre el"
          ↓
     Predecir: "salta"
```

**Arquitectura**:
```
     el    gato    [?]   sobre    el
      ↓      ↓            ↓       ↓
   embed  embed        embed  embed
      ↓      ↓            ↓       ↓
      └──────┴──────┬─────┴───────┘
                    │
              PROMEDIO
                    │
                    ↓
               Hidden Layer
                    │
                    ↓
                 Softmax
                    │
                    ↓
              P("salta"|contexto)
```

**Características CBOW**:
- Entrada: Varias palabras de contexto
- Salida: Una palabra (la central)
- Promedia los embeddings del contexto
- Más rápido de entrenar
- Mejor para palabras frecuentes

### Skip-Gram

**Objetivo**: Predecir el contexto dada la palabra central.

```
Palabra central: "salta"
          ↓
Predecir: "el", "gato", "sobre", "el"
```

**Arquitectura**:
```
            "salta"
               ↓
            embed
               │
    ┌──────────┼──────────┐
    ↓          ↓          ↓
 Softmax    Softmax    Softmax
    ↓          ↓          ↓
P("el")   P("gato")  P("sobre")
```

**Características Skip-Gram**:
- Entrada: Una palabra (la central)
- Salida: Varias palabras (el contexto)
- Más lento de entrenar (más predicciones)
- Mejor para palabras raras
- Mejor representaciones de baja frecuencia

### Ejemplo de Datos de Entrenamiento

```
Oración: "el gato negro salta alto"
Ventana de contexto: 2 palabras a cada lado

CBOW crea estos ejemplos:
Contexto → Target
[el, negro] → gato
[gato, salta] → negro
[negro, alto] → salta

Skip-Gram crea estos ejemplos:
Target → Contexto
gato → el
gato → negro
negro → gato
negro → salta
salta → negro
salta → alto
```

### Comparación Visual

```
CBOW:                              Skip-Gram:
     contexto                           palabra
    ┌────────┐                        ┌────────┐
    │ el     │                        │        │
    │ gato   │ ──→ "negro"            │ negro  │ ──→ "el", "gato", "salta"
    │ salta  │                        │        │
    └────────┘                        └────────┘
```

### Tabla Comparativa

| Aspecto | CBOW | Skip-Gram |
|---------|------|-----------|
| **Input** | Contexto (múltiples palabras) | Palabra central |
| **Output** | Palabra central | Contexto (múltiples palabras) |
| **Velocidad** | Más rápido | Más lento |
| **Palabras frecuentes** | Mejor | Peor |
| **Palabras raras** | Peor | Mejor |
| **Pares de entrenamiento** | Menos | Más |

### Respuesta Resumen

| Modelo | Predice | A partir de | Fortaleza |
|--------|---------|-------------|-----------|
| **CBOW** | Palabra central | Contexto | Rápido, palabras frecuentes |
| **Skip-Gram** | Contexto | Palabra central | Palabras raras, mejor calidad |

---

## Ejercicio 21: Modelo de Lenguaje con MLP (Ventana Fija)

### Enunciado
Describir un modelo de lenguaje basado en MLP con ventana fija de contexto y calcular sus parámetros.

### ¿Qué es un Modelo de Lenguaje? (Explicación Básica)

**Definición**: Un modelo que predice la siguiente palabra dado el contexto.

**Ejemplo**:
```
Input: "El gato está en el"
Output: P("tejado") = 0.3, P("jardín") = 0.25, P("sofá") = 0.2, ...
```

### Arquitectura con MLP y Ventana Fija

**El problema de la ventana fija**: Solo podemos ver un número fijo de palabras anteriores.

```
Ventana fija de 4 palabras:

"El perro grande ladra fuerte en el parque"
                    │
              Solo vemos:
         "ladra fuerte en el"
                    │
                    ↓
              Predecir: "parque"
```

**Arquitectura**:
```
    w₋₄    w₋₃    w₋₂    w₋₁
     │      │      │      │
     ↓      ↓      ↓      ↓
  [E(w₋₄)] [E(w₋₃)] [E(w₋₂)] [E(w₋₁)]   ← Embeddings (d dimensiones cada uno)
     │      │      │      │
     └──────┴──────┴──────┘
               │
               ↓
        Concatenar: vector de 4d dimensiones
               │
               ↓
        ┌─────────────┐
        │  Capa Oculta│  W₁: (hidden × 4d)
        │   + ReLU    │
        └─────────────┘
               │
               ↓
        ┌─────────────┐
        │   Softmax   │  W₂: (vocab × hidden)
        │   (Salida)  │
        └─────────────┘
               │
               ↓
    P(w|w₋₄, w₋₃, w₋₂, w₋₁)
```

### Cálculo de Parámetros

**Configuración**:
- Vocabulario: V = 10,000
- Tamaño de embedding: d = 128
- Ventana de contexto: n = 4
- Capa oculta: h = 256

**1. Matriz de Embeddings**:
```
E: V × d = 10,000 × 128 = 1,280,000 parámetros
```

**2. Capa Oculta**:
```
W₁: h × (n × d) = 256 × (4 × 128) = 256 × 512 = 131,072
b₁: h = 256
```

**3. Capa de Salida**:
```
W₂: V × h = 10,000 × 256 = 2,560,000
b₂: V = 10,000
```

**Total**:
```
Embeddings:     1,280,000
Capa oculta:      131,328  (W₁ + b₁)
Capa salida:    2,570,000  (W₂ + b₂)
────────────────────────
TOTAL:          3,981,328 parámetros
```

### Limitaciones de la Ventana Fija

1. **No captura dependencias largas**:
```
"El gato que persiguió al ratón que se escondió en el agujero ___"
   ↑                                                          │
   └─ Esta información está fuera de la ventana de 4 palabras ─┘
```

2. **Tamaño fijo de entrada**: Siempre necesita exactamente n palabras

3. **Parámetros crecen linealmente** con la ventana:
```
Ventana 4: W₁ tiene 4d columnas
Ventana 8: W₁ tiene 8d columnas (el doble)
```

### Respuesta Resumen

**Arquitectura MLP con ventana fija**:
```
[w₋ₙ, ..., w₋₁] → Embeddings → Concat → Hidden → Softmax → P(w)
```

**Parámetros** (V=10000, d=128, n=4, h=256):
- Embeddings: V × d = 1,280,000
- Hidden: h × (n×d) + h = 131,328
- Output: V × h + V = 2,570,000
- **Total: ~4 millones de parámetros**

**Limitación principal**: No puede ver más allá de la ventana fija.

---

## Ejercicio 22: Modelo de Lenguaje con RNN

### Enunciado
Describir un modelo de lenguaje basado en RNN y explicar sus ventajas sobre el modelo con ventana fija.

### Arquitectura del RNN Language Model

**Idea clave**: La RNN puede procesar secuencias de CUALQUIER longitud, manteniendo un "resumen" en el estado oculto.

```
"El gato negro duerme en el sofá"

   El    →   gato   →   negro  →  duerme  →   en    →   el    →   sofá
    │         │          │          │         │         │         │
    ↓         ↓          ↓          ↓         ↓         ↓         ↓
 [RNN]  →  [RNN]  →   [RNN]  →  [RNN]  →  [RNN]  →  [RNN]  →  [RNN]
    │         │          │          │         │         │         │
    ↓         ↓          ↓          ↓         ↓         ↓         ↓
 P(gato) P(negro) P(duerme) P(en)  P(el)  P(sofá)   P(?)
```

**En cada paso t**:
```
xₜ = embedding de la palabra actual
hₜ = RNN(xₜ, hₜ₋₁)
yₜ = softmax(W · hₜ)  →  Distribución sobre vocabulario
```

### Comparación con MLP de Ventana Fija

| Aspecto | MLP Ventana Fija | RNN |
|---------|------------------|-----|
| **Contexto** | Solo n palabras | Teóricamente infinito |
| **Parámetros** | Crecen con n | Constantes |
| **Longitud variable** | No (padding necesario) | Sí |
| **Dependencias largas** | Limitadas a ventana | Posibles (con LSTM/GRU) |
| **Entrenamiento** | Paralelizable | Secuencial |

### Ventajas de RNN sobre Ventana Fija

**1. Contexto Ilimitado**:
```
MLP (ventana 4): "... escondió en el agujero" → predice ?
                 (no ve "gato" ni "ratón")

RNN: "El gato que persiguió al ratón que se escondió en el agujero"
     h₀ → h₁ → ... → hₜ (contiene info de toda la oración)
```

**2. Parámetros Compartidos**:
```
MLP ventana 4: W₁ tiene tamaño (h × 4d)
MLP ventana 8: W₁ tiene tamaño (h × 8d)  ← El doble

RNN ventana 4: U, W tienen tamaños fijos
RNN ventana 8: U, W tienen los MISMOS tamaños  ← Sin cambio
```

**3. Maneja Secuencias Variables**:
```
RNN puede procesar:
- "Hola" (1 palabra)
- "El gato duerme" (3 palabras)
- "El gato que vimos ayer duerme en el sofá" (9 palabras)

Con los MISMOS parámetros.
```

### Cálculo de Parámetros RNN LM

**Configuración**: V = 10,000, d = 128, h = 256

```
1. Embeddings: V × d = 10,000 × 128 = 1,280,000

2. RNN:
   U (input→hidden):  h × d = 256 × 128 = 32,768
   W (hidden→hidden): h × h = 256 × 256 = 65,536
   bₕ: h = 256

3. Capa de salida:
   V × h = 10,000 × 256 = 2,560,000
   bᵧ: V = 10,000

Total RNN: 32,768 + 65,536 + 256 = 98,560

TOTAL: 1,280,000 + 98,560 + 2,570,000 = 3,948,560
```

### Comparación de Parámetros

```
MLP (ventana 4):  ~3,981,328
RNN:              ~3,948,560  ← Similar

MLP (ventana 8):  ~4,063,328  ← Crece
RNN:              ~3,948,560  ← Igual

MLP (ventana 16): ~4,227,328  ← Sigue creciendo
RNN:              ~3,948,560  ← Sigue igual
```

### Entrenamiento: Teacher Forcing

```
Target: "El gato negro duerme"

Paso 1: Input=[SOS]   → Predecir "El"     → Loss
Paso 2: Input="El"    → Predecir "gato"   → Loss  (usamos "El" real)
Paso 3: Input="gato"  → Predecir "negro"  → Loss  (usamos "gato" real)
...

Loss total = Σ CrossEntropy(predicción, target)
```

### Respuesta Resumen

**RNN Language Model**:
```
xₜ → Embedding → RNN(hₜ₋₁) → hₜ → Softmax → P(wₜ₊₁|w₁...wₜ)
```

**Ventajas sobre MLP con ventana fija**:
1. **Contexto ilimitado**: Puede usar toda la historia
2. **Parámetros fijos**: No crecen con la longitud del contexto
3. **Secuencias variables**: Mismo modelo para cualquier longitud
4. **Compartición de pesos**: Aprende patrones generales del lenguaje

---

## Ejercicio 23: Parámetros de un RNN Language Model

### Enunciado
Calcular el número total de parámetros de un modelo de lenguaje RNN con:
- Vocabulario: V = 50,000
- Dimensión de embedding: d = 300
- Tamaño oculto: h = 512

### Componentes del Modelo

```
┌─────────────────────────────────────────────────────────────┐
│                    RNN Language Model                        │
│                                                              │
│   Palabra wₜ                                                 │
│       │                                                      │
│       ↓                                                      │
│   ┌───────────────┐                                          │
│   │  EMBEDDINGS   │  E: V × d                                │
│   │   50,000×300  │  = 15,000,000 parámetros                │
│   └───────────────┘                                          │
│       │                                                      │
│       ↓ (vector de 300 dims)                                │
│   ┌───────────────┐                                          │
│   │     RNN       │  U: h × d = 153,600                     │
│   │               │  W: h × h = 262,144                     │
│   │   hₜ₋₁ →      │  bₕ: h = 512                            │
│   └───────────────┘  Total RNN: 416,256                     │
│       │                                                      │
│       ↓ (vector de 512 dims)                                │
│   ┌───────────────┐                                          │
│   │    OUTPUT     │  Wₒ: V × h = 25,600,000                 │
│   │   SOFTMAX     │  bₒ: V = 50,000                         │
│   │  50,000×512   │  Total Output: 25,650,000               │
│   └───────────────┘                                          │
│       │                                                      │
│       ↓                                                      │
│   P(wₜ₊₁ | w₁...wₜ)                                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Cálculo Detallado

**1. Matriz de Embeddings (E)**:
```
Cada palabra del vocabulario tiene un vector de d dimensiones.

E: V × d = 50,000 × 300 = 15,000,000 parámetros
```

**2. Capa RNN**:
```
U (input-to-hidden): h × d = 512 × 300 = 153,600
W (hidden-to-hidden): h × h = 512 × 512 = 262,144
bₕ (bias): h = 512

Total RNN: 153,600 + 262,144 + 512 = 416,256 parámetros
```

**3. Capa de Salida**:
```
Wₒ (hidden-to-output): V × h = 50,000 × 512 = 25,600,000
bₒ (bias): V = 50,000

Total Output: 25,600,000 + 50,000 = 25,650,000 parámetros
```

### Suma Total

```
┌────────────────────────────────────────────┐
│ Componente      │ Parámetros  │ Porcentaje │
├────────────────────────────────────────────┤
│ Embeddings (E)  │ 15,000,000  │   36.5%    │
│ RNN (U, W, bₕ)  │    416,256  │    1.0%    │
│ Output (Wₒ, bₒ) │ 25,650,000  │   62.5%    │
├────────────────────────────────────────────┤
│ TOTAL           │ 41,066,256  │  100.0%    │
└────────────────────────────────────────────┘
```

### Observaciones Importantes

**1. La capa de salida domina**:
```
Output: 25.6M (62.5% del total)
```
Esto es porque debe generar una distribución sobre TODO el vocabulario.

**2. Técnica de Weight Tying**:
Una optimización común es compartir los embeddings con la capa de salida:
```
Sin weight tying: E (15M) + Output (25.6M) = 40.6M
Con weight tying: Solo E (15M) usado en ambos lugares

Ahorro: ~25M parámetros (¡más de 60%!)
```

**3. El RNN en sí es pequeño**:
```
RNN: 416,256 (solo 1% del total)
```
La mayoría de parámetros están en los embeddings y la salida.

### Fórmulas Generales

```
Total = V×d + [h×d + h×h + h] + [V×h + V]
      = V×d + h(d + h + 1) + V(h + 1)
      = V(d + h + 1) + h(d + h + 1)
      = (V + h)(d + h + 1)
```

**Verificación**:
```
(50,000 + 512)(300 + 512 + 1) = 50,512 × 813 = 41,066,256 ✓
```

### Respuesta Final

| Componente | Fórmula | Parámetros |
|------------|---------|------------|
| **Embeddings** | V × d | 15,000,000 |
| **RNN** | h(d + h) + h | 416,256 |
| **Output** | V × h + V | 25,650,000 |
| **TOTAL** | - | **41,066,256** |

**≈ 41 millones de parámetros**

---

# RESUMEN FINAL

## Fórmulas Clave para el Parcial

### Atención
```
Attention(Q, K, V) = softmax(QK^T / √d_k) × V
```

### Multi-Head Attention
```
d_k = d_v = d_model / h
Parámetros MHA = 4 × d_model²
```

### Transformer
```
Parámetros por capa ≈ 4d² + 8d×d_ff + parámetros LN
```

### RNN
```
hₜ = tanh(Uxₜ + Whₜ₋₁ + b)
Parámetros = h(n + h + 1)
```

### LSTM
```
Parámetros = 4 × h(n + h + 1)
```

### GRU
```
Parámetros = 3 × h(n + h + 1)
```

### ResNet
```
H(x) = F(x) + x
∂H/∂x = ∂F/∂x + 1  (gradiente nunca desaparece)
```

### Language Model
```
Parámetros ≈ V×d + RNN + V×h
```

---

**Documento generado para preparación del Parcial 2 - Modelos de Deep Learning**
