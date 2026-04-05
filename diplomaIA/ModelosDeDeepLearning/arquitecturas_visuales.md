# Arquitecturas de Deep Learning - Clases 8, 9, 10, 11
## Representaciones Visuales

---

# CLASE 8 (27-Oct): ResNet, DenseNet, Word2Vec

---

## 1. ResNet (Residual Network)

### El Problema
Redes profundas (>30 capas) no aprenden bien porque los gradientes "desaparecen" al retropropagar.

### La Solución: Skip Connection
```
┌─────────────────────────────────────────┐
│           BLOQUE RESIDUAL               │
│                                         │
│   ENTRADA (x)                           │
│       │                                 │
│       ├─────────────────────┐           │
│       │                     │           │
│       ▼                     │           │
│   ┌───────┐                 │           │
│   │Conv 1×1│ 256→64        │ SKIP      │
│   └───┬───┘                 │ CONNECTION│
│       │                     │           │
│       ▼                     │           │
│   ┌───────┐                 │           │
│   │  BN   │                 │           │
│   └───┬───┘                 │           │
│       │                     │           │
│       ▼                     │           │
│   ┌───────┐                 │           │
│   │ ReLU  │                 │           │
│   └───┬───┘                 │           │
│       │                     │           │
│       ▼                     │           │
│   ┌───────┐                 │           │
│   │Conv 3×3│ 64 canales    │           │
│   └───┬───┘                 │           │
│       │                     │           │
│       ▼                     │           │
│   ┌───────┐                 │           │
│   │  BN   │                 │           │
│   └───┬───┘                 │           │
│       │                     │           │
│       ▼                     │           │
│   ┌───────┐                 │           │
│   │ ReLU  │                 │           │
│   └───┬───┘                 │           │
│       │                     │           │
│       ▼                     │           │
│   ┌───────┐                 │           │
│   │Conv 1×1│ 64→256        │           │
│   └───┬───┘                 │           │
│       │                     │           │
│       ▼                     │           │
│       │                     │           │
│       └──────────(+)────────┘           │
│               │                         │
│               ▼                         │
│           SALIDA                        │
│        H(x) = F(x) + x                  │
└─────────────────────────────────────────┘
```

### Fórmula Clave
```
H(x) = F(x) + x

- x     = entrada original (pasa directo)
- F(x)  = transformación aprendida
- H(x)  = salida final

Derivada: ∂H/∂x = ∂F/∂x + 1  ← El "+1" evita vanishing gradient
```

### Variantes
- ResNet-18, ResNet-34 (básicas)
- ResNet-50, ResNet-101, ResNet-152 (con bottleneck)

---

## 2. DenseNet

### Diferencia con ResNet
```
ResNet:  F(x) + x      (SUMA)
DenseNet: [F(x), x]    (CONCATENACIÓN)
```

### Estructura Dense Block
```
┌─────────────────────────────────────────────┐
│              DENSE BLOCK                    │
│                                             │
│   x₀ ──┬───────┬───────┬───────┐           │
│        │       │       │       │           │
│        ▼       │       │       │           │
│      [Conv]    │       │       │           │
│        │       │       │       │           │
│        ▼       │       │       │           │
│   x₁ ──┼───────┼───────┼───────┤           │
│        │       ▼       │       │           │
│        │     [Conv]    │       │           │
│        │       │       │       │           │
│        ▼       ▼       │       │           │
│   x₂ ──┼───────┼───────┤       │           │
│        │       │       ▼       │           │
│        │       │     [Conv]    │           │
│        │       │       │       │           │
│        ▼       ▼       ▼       │           │
│   x₃ ──┼───────┼───────┼───────┤           │
│        │       │       │       ▼           │
│        │       │       │     [Conv]        │
│        ▼       ▼       ▼       ▼           │
│   SALIDA = [x₀, x₁, x₂, x₃, x₄]           │
│   (concatenación de todos)                 │
└─────────────────────────────────────────────┘

Cada capa recibe la salida de TODAS las anteriores
```

---

## 3. Word2Vec

### Arquitectura de la Red (2 capas)
```
┌─────────────────────────────────────────────┐
│                WORD2VEC                     │
│                                             │
│   ┌─────────────┐                          │
│   │  INPUT      │  Vocabulario: 10,000     │
│   │  (One-Hot)  │  [0,0,0,1,0,0,...]       │
│   └──────┬──────┘                          │
│          │                                  │
│          ▼                                  │
│   ┌─────────────┐                          │
│   │  EMBEDDING  │  Dimensión: 300          │
│   │   LAYER     │  (sin activación)        │
│   │             │                          │
│   │  W₁[10000×300]                         │
│   └──────┬──────┘                          │
│          │                                  │
│          ▼                                  │
│   ┌─────────────┐                          │
│   │  OUTPUT     │  Vocabulario: 10,000     │
│   │   LAYER     │  + Softmax               │
│   │             │                          │
│   │  W₂[300×10000]                         │
│   └──────┬──────┘                          │
│          │                                  │
│          ▼                                  │
│   PROBABILIDADES                           │
│   P("gato")=0.02, P("perro")=0.85, ...    │
└─────────────────────────────────────────────┘

El EMBEDDING = columnas de W₁
```

### CBOW (Continuous Bag of Words)
```
┌───────────────────────────────────────┐
│              CBOW                     │
│                                       │
│   CONTEXTO → PALABRA CENTRAL          │
│                                       │
│   ["El", "gato", ___, "en", "casa"]  │
│       │     │           │      │     │
│       ▼     ▼           ▼      ▼     │
│      One-Hot Encoding                │
│       │     │           │      │     │
│       └─────┴─────┬─────┴──────┘     │
│                   │                   │
│              PROMEDIO                 │
│                   │                   │
│                   ▼                   │
│            ┌──────────┐              │
│            │ Embedding │              │
│            └────┬─────┘              │
│                 │                     │
│                 ▼                     │
│            ┌──────────┐              │
│            │ Softmax  │              │
│            └────┬─────┘              │
│                 │                     │
│                 ▼                     │
│           "duerme" ← PREDICCIÓN      │
└───────────────────────────────────────┘
```

### Skip-gram
```
┌───────────────────────────────────────┐
│            SKIP-GRAM                  │
│                                       │
│   PALABRA CENTRAL → CONTEXTO          │
│                                       │
│           "duerme"                    │
│               │                       │
│               ▼                       │
│          One-Hot                      │
│               │                       │
│               ▼                       │
│         ┌──────────┐                 │
│         │ Embedding │                 │
│         └────┬─────┘                 │
│              │                        │
│              ▼                        │
│         ┌──────────┐                 │
│         │ Softmax  │                 │
│         └────┬─────┘                 │
│              │                        │
│    ┌─────────┼─────────┐             │
│    ▼         ▼         ▼             │
│  "El"     "gato"    "en"             │
│         PREDICCIONES                 │
└───────────────────────────────────────┘
```

### Propiedad Mágica
```
king - man + woman ≈ queen

Los vectores capturan relaciones semánticas
```

---

# CLASE 9 (03-Nov): RNN, LSTM, GRU

---

## 4. RNN Vanilla (Recurrent Neural Network)

### Arquitectura Desplegada
```
┌─────────────────────────────────────────────────────────────┐
│                    RNN DESPLEGADA                           │
│                                                             │
│   H₀ ──→ ┌─────┐ ──→ H₁ ──→ ┌─────┐ ──→ H₂ ──→ ┌─────┐    │
│          │ RNN │            │ RNN │            │ RNN │     │
│          │     │            │     │            │     │     │
│          └──┬──┘            └──┬──┘            └──┬──┘     │
│             │                  │                  │         │
│             ▲                  ▲                  ▲         │
│             │                  │                  │         │
│            X₁                 X₂                 X₃        │
│             │                  │                  │         │
│             ▼                  ▼                  ▼         │
│            Y₁                 Y₂                 Y₃        │
│                                                             │
│   Los pesos U, V, W se COMPARTEN en todos los pasos        │
└─────────────────────────────────────────────────────────────┘
```

### Celda RNN Individual
```
┌─────────────────────────────────────┐
│           CELDA RNN                 │
│                                     │
│      Xₜ              Hₜ₋₁          │
│       │                │            │
│       ▼                ▼            │
│    ┌─────┐          ┌─────┐        │
│    │  U  │          │  V  │        │
│    └──┬──┘          └──┬──┘        │
│       │                │            │
│       └───────┬────────┘            │
│               │                     │
│               ▼                     │
│           ┌───────┐                │
│           │ tanh  │                │
│           └───┬───┘                │
│               │                     │
│               ▼                     │
│              Hₜ ──────────────→    │
│               │                     │
│               ▼                     │
│            ┌─────┐                 │
│            │  W  │                 │
│            └──┬──┘                 │
│               │                     │
│               ▼                     │
│              Yₜ                    │
└─────────────────────────────────────┘

Fórmulas:
Hₜ = tanh(U·Xₜ + V·Hₜ₋₁ + b)
Yₜ = W·Hₜ
```

### Las 3 Matrices
```
U: [hidden_dim × input_dim]   → Procesa entrada
V: [hidden_dim × hidden_dim]  → Procesa estado previo
W: [output_dim × hidden_dim]  → Genera salida
```

---

## 5. LSTM (Long Short-Term Memory)

### Estructura de la Celda
```
┌──────────────────────────────────────────────────────────────────┐
│                         CELDA LSTM                               │
│                                                                  │
│   Cₜ₋₁ ════════════════╤═══════════════════════════════ Cₜ     │
│            │            │                    │                   │
│            │            │                    │                   │
│            ▼            ▼                    ▼                   │
│         ┌─────┐     ┌─────┐              ┌─────┐                │
│         │  ×  │     │  +  │              │tanh │                │
│         └──┬──┘     └──┬──┘              └──┬──┘                │
│            │           │                    │                    │
│            │     ┌─────┴─────┐              │                    │
│            │     │           │              │                    │
│   ┌────────┴─────┴───┐   ┌───┴───┐     ┌───┴───┐               │
│   │                  │   │       │     │       │               │
│   │   FORGET GATE    │   │   ×   │     │   ×   │ ──────→ Hₜ   │
│   │      (fₜ)        │   │       │     │       │               │
│   │                  │   └───┬───┘     └───┬───┘               │
│   │    σ(Wf·[Hₜ₋₁,Xₜ])    │             │                    │
│   └────────┬─────────┘      │             │                    │
│            │                │             │                    │
│            │          ┌─────┴─────┐       │                    │
│            │          │           │       │                    │
│            │    INPUT GATE    CANDIDATE   OUTPUT GATE          │
│            │       (iₜ)        (C̃ₜ)        (oₜ)               │
│            │                              │                    │
│            │  σ(Wi·[Hₜ₋₁,Xₜ])  tanh(Wc·[Hₜ₋₁,Xₜ])  σ(Wo·[Hₜ₋₁,Xₜ])  │
│            │          │           │       │                    │
│            │          └─────┬─────┘       │                    │
│            │                │             │                    │
│            └────────────────┴─────────────┘                    │
│                             │                                   │
│                      Xₜ ────┴──── Hₜ₋₁                         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Las 4 Compuertas
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  1. FORGET GATE (fₜ):  σ(Wf·[Hₜ₋₁, Xₜ])           │
│     → ¿Qué olvidar del pasado? (0=olvidar, 1=recordar)│
│                                                     │
│  2. INPUT GATE (iₜ):   σ(Wi·[Hₜ₋₁, Xₜ])           │
│     → ¿Qué tan importante es la info nueva?         │
│                                                     │
│  3. CANDIDATE (C̃ₜ):   tanh(Wc·[Hₜ₋₁, Xₜ])        │
│     → Nueva información propuesta                   │
│                                                     │
│  4. OUTPUT GATE (oₜ):  σ(Wo·[Hₜ₋₁, Xₜ])           │
│     → ¿Qué mostrar del estado?                      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Fórmulas Clave
```
Cₜ = fₜ ⊙ Cₜ₋₁ + iₜ ⊙ C̃ₜ   ← NUEVO CELL STATE
Hₜ = oₜ ⊙ tanh(Cₜ)          ← NUEVO HIDDEN STATE

⊙ = multiplicación elemento a elemento
```

---

## 6. GRU (Gated Recurrent Unit)

### Estructura de la Celda
```
┌──────────────────────────────────────────────────────┐
│                     CELDA GRU                        │
│                                                      │
│            Hₜ₋₁                                     │
│              │                                       │
│    ┌─────────┼─────────┐                            │
│    │         │         │                            │
│    ▼         ▼         ▼                            │
│ ┌─────┐   ┌─────┐   ┌─────┐                        │
│ │RESET│   │UPDATE│  │     │                        │
│ │GATE │   │GATE │   │     │                        │
│ │ rₜ  │   │ zₜ  │   │     │                        │
│ └──┬──┘   └──┬──┘   │     │                        │
│    │         │      │     │                        │
│    │         │      │     │                        │
│    ▼         │      │     │                        │
│ rₜ⊙Hₜ₋₁     │      │     │                        │
│    │         │      │     │                        │
│    └────┬────┘      │     │                        │
│         │           │     │                        │
│         ▼           │     │                        │
│    ┌─────────┐      │     │                        │
│    │  tanh   │      │     │                        │
│    │   H̃ₜ   │      │     │                        │
│    └────┬────┘      │     │                        │
│         │           │     │                        │
│         ▼           ▼     │                        │
│    ┌─────────────────┐    │                        │
│    │                 │    │                        │
│    │  Hₜ = (1-zₜ)⊙H̃ₜ + zₜ⊙Hₜ₋₁                  │
│    │                 │    │                        │
│    └────────┬────────┘    │                        │
│             │             │                        │
│             ▼             │                        │
│            Hₜ ────────────┘                        │
│                                                      │
│             ▲                                        │
│             │                                        │
│            Xₜ                                       │
└──────────────────────────────────────────────────────┘
```

### Las 2 Compuertas
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  1. RESET GATE (rₜ):  σ(Wr·[Hₜ₋₁, Xₜ])            │
│     → ¿Cuánto del pasado usar para el candidato?    │
│                                                     │
│  2. UPDATE GATE (zₜ): σ(Wz·[Hₜ₋₁, Xₜ])            │
│     → Balance entre pasado y nuevo                  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Fórmula Clave
```
H̃ₜ = tanh(W·[rₜ⊙Hₜ₋₁, Xₜ])     ← Candidato
Hₜ = (1-zₜ)⊙H̃ₜ + zₜ⊙Hₜ₋₁       ← NUEVO ESTADO

Si zₜ→1: Hₜ ≈ Hₜ₋₁  (mantiene pasado)
Si zₜ→0: Hₜ ≈ H̃ₜ   (actualiza con nuevo)
```

### Comparación LSTM vs GRU
```
┌────────────────┬────────────────┬────────────────┐
│    Aspecto     │      LSTM      │      GRU       │
├────────────────┼────────────────┼────────────────┤
│ Estados        │ 2 (C y H)      │ 1 (solo H)     │
│ Compuertas     │ 4              │ 2              │
│ Parámetros     │ Más            │ Menos          │
│ Entrenamiento  │ Más difícil    │ Más fácil      │
│ Rendimiento    │ Similar        │ Similar        │
└────────────────┴────────────────┴────────────────┘
```

---

# CLASE 10 (10-Nov): Seq2Seq, Encoder-Decoder

---

## 7. Arquitectura Encoder-Decoder

### Estructura General
```
┌─────────────────────────────────────────────────────────────────┐
│                    ENCODER-DECODER                              │
│                                                                 │
│       ENCODER                           DECODER                 │
│                                                                 │
│   "Je" → ┌─────┐                    ┌─────┐ → "I"              │
│          │ RNN │→H₁                 │ RNN │                     │
│          └─────┘                    └──┬──┘                     │
│                                       ▲                         │
│  "suis"→ ┌─────┐                      │                         │
│          │ RNN │→H₂                <START>                     │
│          └─────┘                                                │
│                                    ┌─────┐ → "am"              │
│ "prof"→  ┌─────┐                   │ RNN │                     │
│          │ RNN │→H₃ ═══════════════└──┬──┘                     │
│          └─────┘      CONTEXTO C      ▲                         │
│                      (último H)       │                         │
│                                      "I"                        │
│                                                                 │
│                                    ┌─────┐ → "a"               │
│                                    │ RNN │                     │
│                                    └──┬──┘                     │
│                                       ▲                         │
│                                       │                         │
│                                     "am"                        │
└─────────────────────────────────────────────────────────────────┘
```

### El Flujo
```
ENCODER:
1. Procesa secuencia de entrada (ej: francés)
2. Produce vector de contexto C = último hidden state

DECODER:
1. Recibe C como estado inicial
2. Empieza con token <START>
3. Genera palabra por palabra
4. Termina cuando predice <END>
```

### Teacher Forcing
```
┌─────────────────────────────────────────────┐
│                                             │
│  ENTRENAMIENTO (Teacher Forcing):           │
│  → Usa la palabra CORRECTA como input       │
│  → Aunque el modelo haya predicho otra      │
│                                             │
│  INFERENCIA:                                │
│  → Usa la palabra PREDICHA como input       │
│  → Genera secuencia completa                │
│                                             │
└─────────────────────────────────────────────┘
```

---

# CLASE 11 (17-Nov): Attention, Transformers

---

## 8. Mecanismo de Attention (Bahdanau)

### El Problema
```
Encoder-Decoder clásico comprime TODO en UN vector C
→ Cuello de botella para secuencias largas
```

### La Solución: Contexto Dinámico
```
┌─────────────────────────────────────────────────────────────────┐
│                    ATTENTION                                    │
│                                                                 │
│   ENCODER OUTPUTS: [H₁, H₂, H₃, H₄]                           │
│                     │   │   │   │                               │
│                     ▼   ▼   ▼   ▼                               │
│                   ┌───────────────┐                            │
│   Sᵢ₋₁ ─────────→│   SCORES      │                            │
│   (estado        │  e₁  e₂  e₃  e₄│                            │
│    decoder)      └───────┬────────┘                            │
│                          │                                      │
│                          ▼                                      │
│                      SOFTMAX                                    │
│                          │                                      │
│                          ▼                                      │
│                    [α₁ α₂ α₃ α₄]                               │
│                     │   │   │   │                               │
│                     ▼   ▼   ▼   ▼                               │
│                   ┌───────────────┐                            │
│                   │  COMBINACIÓN  │                            │
│                   │ Cᵢ = Σ αⱼ·Hⱼ │                            │
│                   └───────┬───────┘                            │
│                           │                                     │
│                           ▼                                     │
│                    CONTEXTO Cᵢ                                 │
│                    (dinámico para cada paso)                    │
└─────────────────────────────────────────────────────────────────┘
```

### Fórmulas
```
eᵢⱼ = v^T · tanh(Ws·Sᵢ₋₁ + Wh·Hⱼ)   ← Score
αᵢⱼ = softmax(eᵢⱼ)                   ← Peso normalizado
Cᵢ  = Σⱼ αᵢⱼ · Hⱼ                    ← Contexto
```

---

## 9. Self-Attention

### Concepto
```
Cada palabra "mira" a TODAS las otras palabras
de la MISMA secuencia
```

### Proceso Query-Key-Value
```
┌─────────────────────────────────────────────────────────────────┐
│                    SELF-ATTENTION                               │
│                                                                 │
│   Input: [X₁, X₂, X₃]                                          │
│            │   │   │                                            │
│            ▼   ▼   ▼                                            │
│   ┌────────────────────────┐                                   │
│   │     PROYECCIONES       │                                   │
│   │                        │                                   │
│   │  Q = X · Wq  (Queries) │                                   │
│   │  K = X · Wk  (Keys)    │                                   │
│   │  V = X · Wv  (Values)  │                                   │
│   └────────────────────────┘                                   │
│            │                                                    │
│            ▼                                                    │
│   ┌────────────────────────┐                                   │
│   │    SCORES              │                                   │
│   │                        │                                   │
│   │    Q · K^T             │                                   │
│   │    ───────             │                                   │
│   │      √dₖ               │                                   │
│   └────────────────────────┘                                   │
│            │                                                    │
│            ▼                                                    │
│   ┌────────────────────────┐                                   │
│   │      SOFTMAX           │                                   │
│   │   (por filas)          │                                   │
│   └────────────────────────┘                                   │
│            │                                                    │
│            ▼                                                    │
│   ┌────────────────────────┐                                   │
│   │  COMBINACIÓN           │                                   │
│   │                        │                                   │
│   │  Output = Softmax · V  │                                   │
│   └────────────────────────┘                                   │
│            │                                                    │
│            ▼                                                    │
│   Output: [Z₁, Z₂, Z₃]                                         │
│   (embeddings contextuales)                                     │
└─────────────────────────────────────────────────────────────────┘
```

### Fórmula Compacta
```
                    Q · K^T
Attention(Q,K,V) = softmax(───────) · V
                      √dₖ
```

---

## 10. Multi-Head Attention

### Concepto
```
Aplicar Self-Attention MÚLTIPLES VECES en paralelo
con diferentes proyecciones
```

### Estructura
```
┌─────────────────────────────────────────────────────────────────┐
│                  MULTI-HEAD ATTENTION                           │
│                                                                 │
│   Input                                                         │
│     │                                                           │
│     ├──────────┬──────────┬──────────┬──────────┐              │
│     │          │          │          │          │              │
│     ▼          ▼          ▼          ▼          ▼              │
│  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐             │
│  │Head 1│  │Head 2│  │Head 3│  │Head 4│  │...   │             │
│  │      │  │      │  │      │  │      │  │      │             │
│  │Wq₁   │  │Wq₂   │  │Wq₃   │  │Wq₄   │  │      │             │
│  │Wk₁   │  │Wk₂   │  │Wk₃   │  │Wk₄   │  │      │             │
│  │Wv₁   │  │Wv₂   │  │Wv₃   │  │Wv₄   │  │      │             │
│  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘             │
│     │         │         │         │         │                   │
│     └────┬────┴────┬────┴────┬────┴────┬────┘                   │
│          │                                                      │
│          ▼                                                      │
│   ┌──────────────┐                                             │
│   │  CONCATENAR  │                                             │
│   └──────┬───────┘                                             │
│          │                                                      │
│          ▼                                                      │
│   ┌──────────────┐                                             │
│   │    LINEAR    │                                             │
│   │     (Wo)     │                                             │
│   └──────┬───────┘                                             │
│          │                                                      │
│          ▼                                                      │
│       Output                                                    │
└─────────────────────────────────────────────────────────────────┘

Cada cabeza aprende relaciones DIFERENTES
- Head 1: relaciones sintácticas
- Head 2: relaciones semánticas
- Head 3: dependencias de largo alcance
- etc.
```

---

## 11. Positional Encoding

### El Problema
```
Self-Attention es INVARIANTE al orden
"El perro mordió al hombre" = "hombre mordió El al perro"
```

### La Solución
```
┌─────────────────────────────────────────────────────────────────┐
│                 POSITIONAL ENCODING                             │
│                                                                 │
│   PE(pos, 2i)   = sin(pos / 10000^(2i/d))                      │
│   PE(pos, 2i+1) = cos(pos / 10000^(2i/d))                      │
│                                                                 │
│   Input final = Embedding(palabra) + PE(posición)              │
│                                                                 │
│   Cada posición tiene un "patrón único" de senos/cosenos       │
│                                                                 │
│   Pos 0: [0.0,  1.0,  0.0,  1.0, ...]                         │
│   Pos 1: [0.84, 0.54, 0.01, 0.99, ...]                        │
│   Pos 2: [0.91, -0.4, 0.02, 0.98, ...]                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 12. Transformer Completo

### Arquitectura
```
┌─────────────────────────────────────────────────────────────────────────┐
│                          TRANSFORMER                                    │
│                                                                         │
│         ENCODER (×N)                        DECODER (×N)                │
│                                                                         │
│   Input Embedding                      Output Embedding                 │
│         +                                    +                          │
│   Positional Encoding                  Positional Encoding              │
│         │                                    │                          │
│         ▼                                    ▼                          │
│   ┌───────────────┐                   ┌───────────────┐                │
│   │  Multi-Head   │                   │ Masked Multi- │                │
│   │ Self-Attention│                   │Head Self-Attn │                │
│   └───────┬───────┘                   └───────┬───────┘                │
│           │                                   │                         │
│           ▼                                   ▼                         │
│      Add & Norm                          Add & Norm                     │
│           │                                   │                         │
│           ▼                                   ▼                         │
│   ┌───────────────┐                   ┌───────────────┐                │
│   │  Feed Forward │                   │  Multi-Head   │◄───────────────┤
│   │    Network    │                   │   Attention   │   (Cross-Attn) │
│   └───────┬───────┘                   └───────┬───────┘                │
│           │                                   │                         │
│           ▼                                   ▼                         │
│      Add & Norm ────────────────────→   Add & Norm                     │
│           │                                   │                         │
│           │                                   ▼                         │
│           │                           ┌───────────────┐                │
│           │                           │  Feed Forward │                │
│           │                           │    Network    │                │
│           │                           └───────┬───────┘                │
│           │                                   │                         │
│           │                                   ▼                         │
│           │                              Add & Norm                     │
│           │                                   │                         │
│           │                                   ▼                         │
│           │                              Linear                         │
│           │                                   │                         │
│           │                                   ▼                         │
│           │                              Softmax                        │
│           │                                   │                         │
│           │                                   ▼                         │
│           │                           Output Probs                      │
│           │                                                             │
└───────────┴─────────────────────────────────────────────────────────────┘
```

### Componentes del Encoder Block
```
┌─────────────────────────────────────┐
│         ENCODER BLOCK               │
│                                     │
│   Input                             │
│     │                               │
│     ├─────────────────────┐         │
│     │                     │         │
│     ▼                     │         │
│  Multi-Head               │         │
│  Self-Attention           │         │
│     │                     │         │
│     ▼                     │         │
│    (+) ◄──────────────────┘         │
│     │       Residual                │
│     ▼                               │
│  Layer Norm                         │
│     │                               │
│     ├─────────────────────┐         │
│     │                     │         │
│     ▼                     │         │
│  Feed-Forward             │         │
│  (Linear→ReLU→Linear)     │         │
│     │                     │         │
│     ▼                     │         │
│    (+) ◄──────────────────┘         │
│     │       Residual                │
│     ▼                               │
│  Layer Norm                         │
│     │                               │
│     ▼                               │
│   Output                            │
└─────────────────────────────────────┘
```

### Componentes del Decoder Block
```
┌─────────────────────────────────────┐
│         DECODER BLOCK               │
│                                     │
│   Output (shifted)                  │
│     │                               │
│     ├─────────────────────┐         │
│     ▼                     │         │
│  Masked Multi-Head        │         │
│  Self-Attention           │         │
│  (no ve el futuro)        │         │
│     │                     │         │
│    (+) ◄──────────────────┘         │
│     │                               │
│  Layer Norm                         │
│     │                               │
│     ├─────────────────────┐         │
│     ▼                     │         │
│  Multi-Head               │         │
│  Attention                │         │
│  (Q=decoder, K,V=encoder) │         │
│     │                     │         │
│    (+) ◄──────────────────┘         │
│     │                               │
│  Layer Norm                         │
│     │                               │
│     ├─────────────────────┐         │
│     ▼                     │         │
│  Feed-Forward             │         │
│     │                     │         │
│    (+) ◄──────────────────┘         │
│     │                               │
│  Layer Norm                         │
│     │                               │
│     ▼                               │
│   Output                            │
└─────────────────────────────────────┘
```

### Máscara Causal (Decoder)
```
┌─────────────────────────────────────┐
│       MÁSCARA CAUSAL                │
│                                     │
│   Scores antes de softmax:          │
│                                     │
│         pos1  pos2  pos3  pos4      │
│   pos1 [  0   -∞   -∞   -∞  ]      │
│   pos2 [  0    0   -∞   -∞  ]      │
│   pos3 [  0    0    0   -∞  ]      │
│   pos4 [  0    0    0    0  ]      │
│                                     │
│   -∞ → softmax da 0                 │
│   → No puede ver posiciones futuras │
│                                     │
└─────────────────────────────────────┘
```

### Ventajas del Transformer
```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  1. PARALELIZACIÓN                                              │
│     → Procesa toda la secuencia simultáneamente                 │
│     → RNN debe procesar paso a paso                             │
│                                                                 │
│  2. DEPENDENCIAS A LARGO PLAZO                                  │
│     → Attention conecta cualquier par de palabras directamente  │
│     → RNN pierde información en secuencias largas               │
│                                                                 │
│  3. ESCALABILIDAD                                               │
│     → Entrena eficientemente con grandes datasets               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Dimensiones Típicas (Paper Original)

```
┌─────────────────────────────────────┐
│                                     │
│   d_model    = 512                  │
│   d_ff       = 2048                 │
│   num_heads  = 8                    │
│   d_k = d_v  = 64 (512/8)          │
│   N (capas)  = 6                    │
│                                     │
└─────────────────────────────────────┘
```
