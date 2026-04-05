# Función de Pérdida de los Modelos de Lenguaje (LLMs)

## La Idea en Una Oración

El modelo aprende a **predecir la siguiente palabra**. La pérdida es qué tan lejos está su predicción de la palabra correcta.

---

## ¿Qué Hace un Modelo de Lenguaje?

Un modelo de lenguaje:
1. Recibe una secuencia de palabras (tokens)
2. Devuelve una **distribución de probabilidad** sobre cuál es la siguiente palabra

**Ejemplo:**
```
Entrada: "Hola, ¿cómo"
Salida: {"estás": 0.35, "andas": 0.15, "te": 0.10, ...}
```

El modelo dice: "35% de probabilidad de que siga 'estás', 15% de que siga 'andas', etc."

---

## La Función de Pérdida: Cross-Entropy

### La Fórmula

```
L = -Σ y_i × log(p_i)
```

Donde:
- **y_i:** Etiqueta real (1 si es la palabra correcta, 0 si no)
- **p_i:** Probabilidad que el modelo asigna a la palabra i

### En Lenguaje Simple

Como solo hay **una** palabra correcta (y_true = 1, el resto = 0):

```
L = -log(p_correcta)
```

**En español:** El negativo del logaritmo de la probabilidad que el modelo le dio a la palabra correcta.

### Ejemplo Numérico

Si el modelo dice:
```
"estás": 0.35
"andas": 0.15
"te": 0.10
...
```

Y la palabra correcta era "estás":

```
L = -log(0.35) ≈ 1.05
```

Si el modelo hubiera dicho "estás": 0.90:
```
L = -log(0.90) ≈ 0.11
```

**Cuanto más alta la probabilidad de la palabra correcta, más baja la pérdida.**

---

## ¿Por Qué Cross-Entropy?

### El Comportamiento del Logaritmo

```
p_correcta = 1.0   →   L = -log(1) = 0      (pérdida mínima)
p_correcta = 0.5   →   L = -log(0.5) ≈ 0.69
p_correcta = 0.1   →   L = -log(0.1) ≈ 2.3
p_correcta = 0.01  →   L = -log(0.01) ≈ 4.6  (pérdida alta)
```

### Propiedades Clave

1. **Cuando p → 1:** L → 0 (pérdida mínima cuando predice perfectamente)
2. **Cuando p → 0:** L → ∞ (pérdida infinita cuando falla completamente)
3. **Gradientes más fuertes cuando se equivoca:** Aprende más de sus errores

---

## El Proceso de Logits a Probabilidades

### Paso 1: El Modelo Produce Logits

Los **logits** son la salida cruda del modelo: números reales que pueden ser positivos o negativos.

```
Logits: ["estás": 2.5, "andas": 1.2, "te": 0.8, "?": 3.1, ...]
```

**Los logits NO son probabilidades** (no suman 1, pueden ser negativos).

### Paso 2: Softmax Convierte a Probabilidades

La función **Softmax** transforma logits en probabilidades:

```
p_i = exp(logit_i) / Σ exp(logit_j)
```

**Propiedades de Softmax:**
- Todos los valores quedan entre 0 y 1
- La suma de todos = 1
- Valores más altos → probabilidades más altas

### Ejemplo

```
Logits:        [2.5, 1.2, 0.8, 3.1]
exp(logits):   [12.2, 3.3, 2.2, 22.2]
suma:          39.9
Softmax:       [0.31, 0.08, 0.06, 0.56]
```

---

## Cross-Entropy con Logits

En PyTorch, hay una función que combina Softmax + Cross-Entropy:

```python
loss = F.cross_entropy(logits, target)
```

**¿Por qué combinada?**
- Es numéricamente más estable
- Evita problemas de overflow/underflow
- Es más eficiente

---

## Entrenamiento de un Modelo de Lenguaje

### El Setup

Tienes un corpus de texto (muchos documentos, libros, páginas web).

### El Proceso

Para cada oración del corpus:

```
Oración: "El gato come pescado"

Ejemplos de entrenamiento:
  Input: "El"           → Target: "gato"
  Input: "El gato"      → Target: "come"
  Input: "El gato come" → Target: "pescado"
```

### El Loop de Entrenamiento

```python
for batch in dataloader:
    inputs, targets = batch  # tokens de entrada y siguiente token

    # Forward pass
    logits = model(inputs)  # [batch, seq_len, vocab_size]

    # Calcular pérdida
    loss = F.cross_entropy(logits.view(-1, vocab_size), targets.view(-1))

    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

---

## Negative Log-Likelihood (NLL)

### Es lo mismo

Cross-Entropy y Negative Log-Likelihood son **equivalentes** cuando tienes una sola clase correcta:

```
Cross-Entropy = -Σ y_i × log(p_i)
              = -log(p_correcta)    (cuando y_correcta = 1, resto = 0)
              = Negative Log-Likelihood
```

### En Código

```python
# Estos son equivalentes:
loss1 = F.cross_entropy(logits, targets)
loss2 = F.nll_loss(F.log_softmax(logits, dim=-1), targets)
```

---

## Perplexity: La Métrica

### ¿Qué Es?

**Perplexity** mide qué tan "confundido" está el modelo. Es el exponencial de la pérdida promedio:

```
Perplexity = exp(L_promedio)
```

### Interpretación

- **Perplexity = 1:** Perfecto (el modelo siempre predice con probabilidad 1)
- **Perplexity = V:** Aleatorio (V = tamaño del vocabulario)
- **Perplexity más baja = mejor**

### Ejemplo

Si el vocabulario tiene 50,000 palabras:
- Perplexity ≈ 50,000: Como adivinar al azar
- Perplexity ≈ 100: Bastante bueno
- Perplexity ≈ 20: Muy bueno

---

## Código Completo

```python
import torch
import torch.nn.functional as F

class LanguageModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.transformer = nn.TransformerEncoder(...)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x):
        # x: [batch, seq_len] - tokens de entrada
        x = self.embedding(x)           # [batch, seq_len, embed_dim]
        x = self.transformer(x)         # [batch, seq_len, hidden_dim]
        logits = self.fc(x)             # [batch, seq_len, vocab_size]
        return logits

# Entrenamiento
def train_step(model, batch, optimizer):
    inputs, targets = batch

    # Forward
    logits = model(inputs)  # [batch, seq_len, vocab_size]

    # Pérdida: Cross-Entropy
    # Aplanar para la función de pérdida
    loss = F.cross_entropy(
        logits.view(-1, vocab_size),  # [batch*seq_len, vocab_size]
        targets.view(-1)               # [batch*seq_len]
    )

    # Backward
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    return loss.item()

# Calcular Perplexity
def perplexity(model, dataloader):
    total_loss = 0
    total_tokens = 0

    with torch.no_grad():
        for batch in dataloader:
            inputs, targets = batch
            logits = model(inputs)
            loss = F.cross_entropy(logits.view(-1, vocab_size), targets.view(-1))
            total_loss += loss.item() * targets.numel()
            total_tokens += targets.numel()

    avg_loss = total_loss / total_tokens
    return math.exp(avg_loss)
```

---

## Resumen Visual

```
┌────────────────────────────────────────────────────────────────┐
│               PÉRDIDA DE MODELOS DE LENGUAJE                   │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   Input: "El gato come"                                        │
│   Target: "pescado"                                            │
│                                                                │
│   1. Modelo → logits: [1.2, -0.5, 2.8, 0.1, ...]              │
│                        ↑                                       │
│                   vocab_size números                           │
│                                                                │
│   2. Softmax → probabilidades: [0.05, 0.01, 0.30, 0.02, ...]  │
│                                         ↑                      │
│                                    "pescado"                   │
│                                                                │
│   3. Loss = -log(p_pescado) = -log(0.30) ≈ 1.2                │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   Cross-Entropy = -log(p_correcta)                             │
│                                                                │
│   p → 1  ⟹  Loss → 0   (predicción perfecta)                 │
│   p → 0  ⟹  Loss → ∞   (predicción terrible)                 │
│                                                                │
│   Perplexity = exp(Loss_promedio)                              │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## Para el Parcial

**Cross-Entropy:** Pérdida que mide qué tan lejos está la predicción del modelo de la palabra correcta; L = -log(p_correcta).

**Logits:** Salida cruda del modelo, números reales que no son probabilidades; se convierten en probabilidades con Softmax.

**Softmax:** Función que convierte logits en probabilidades; p_i = exp(logit_i) / Σ exp(logit_j).

**Negative Log-Likelihood (NLL):** Equivalente a Cross-Entropy cuando hay una sola clase correcta.

**Perplexity:** Métrica que mide confusión del modelo = exp(L_promedio); más baja = mejor.

**El modelo es determinístico:** Para la misma entrada, siempre da la misma distribución de probabilidades; la aleatoriedad viene del muestreo.
