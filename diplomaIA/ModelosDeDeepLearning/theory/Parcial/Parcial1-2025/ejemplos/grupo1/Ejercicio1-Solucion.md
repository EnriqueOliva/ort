# Ejercicio 1 - Red Neuronal para Predicción de Retrasos

## Contexto del problema

Tienes un dataset de aerolíneas para predecir si un vuelo se va a retrasar o no.

**Variables de entrada (features):**
1. Hora de salida (formato 24 horas: 0-23)
2. Día de la semana (0=domingo, 6=sábado)
3. Mes (1-12)
4. Aerolínea (número único por aerolínea)
5. Duración del vuelo (minutos)

**Variable a predecir:** Probabilidad de retraso (número entre 0 y 1)

**Tipo de problema:** Clasificación binaria (SÍ se retrasa / NO se retrasa)

---

## a. ¿Cuántos parámetros entrenables tiene el modelo?

### Fórmula para calcular parámetros en una capa Dense

```
Parámetros = Pesos + Biases
           = (Input × Output) + Output

Donde:
- Input = número de neuronas que entran a la capa
- Output = número de neuronas de salida de la capa
- Pesos = conexiones entre todas las neuronas de entrada y salida
- Biases = un número extra por cada neurona de salida (para ajustar)
```

### Arquitectura de la red

```
Entrada: 5 números (las 5 features)
   ↓
L_1 (Linear): Dense con m neuronas
   ↓
A_1 (Activation): ReLU
   ↓
L_2 (Linear): Dense con n neuronas
   ↓
A_2 (Activation): Sigmoid
   ↓
Salida: 1 número (probabilidad de retraso)
```

### Cálculo de m (dimensión de L_1)

El enunciado dice: **"m triplica el tamaño de su entrada"**

```
Entrada = 5 features
Triplica significa: 5 × 3 = 15

Por lo tanto: m = 15 neuronas
```

### Cálculo de n (dimensión de L_2)

El problema es **clasificación binaria** (predecir SÍ/NO retraso)

Para clasificación binaria necesitas **1 sola neurona** que dé una probabilidad.

```
Por lo tanto: n = 1 neurona
```

### Cálculo de parámetros de L_1

```
L_1: de 5 entradas → 15 salidas

Pesos:
  Cada una de las 15 neuronas de salida está conectada a las 5 entradas
  Total de conexiones = 5 × 15 = 75 pesos

Biases:
  Cada neurona de salida tiene 1 bias
  Total de biases = 15

Parámetros L_1 = 75 + 15 = 90
```

**Explicación detallada de los pesos:**
```
Neurona 1 de salida: recibe 5 números, tiene 5 pesos (w₁, w₂, w₃, w₄, w₅)
Neurona 2 de salida: recibe 5 números, tiene 5 pesos
...
Neurona 15 de salida: recibe 5 números, tiene 5 pesos

Total: 15 neuronas × 5 pesos cada una = 75 pesos
Más: 15 biases (uno por neurona) = 15
Total L_1: 90 parámetros
```

### Cálculo de parámetros de L_2

```
L_2: de 15 entradas (salida de A_1) → 1 salida

Pesos:
  La 1 neurona de salida está conectada a las 15 entradas
  Total de conexiones = 15 × 1 = 15 pesos

Biases:
  1 neurona = 1 bias

Parámetros L_2 = 15 + 1 = 16
```

**Explicación detallada:**
```
La neurona de salida calcula:
  salida = w₁×entrada₁ + w₂×entrada₂ + ... + w₁₅×entrada₁₅ + bias
           ↑ 15 pesos                                         ↑ 1 bias
```

### Total de parámetros

```
L_1: 90 parámetros
L_2: 16 parámetros
A_1: 0 parámetros (ReLU no tiene parámetros, solo transforma)
A_2: 0 parámetros (Sigmoid no tiene parámetros, solo transforma)

TOTAL = 90 + 16 = 106 parámetros entrenables
```

**Respuesta: 106 parámetros**

---

## b. Explique ReLU y L1 regularization

### ReLU (Rectified Linear Unit)

**Fórmula matemática:**
```
ReLU(z) = max(0, z)

Esto significa:
- Si z es negativo (z < 0) → ReLU devuelve 0
- Si z es cero o positivo (z ≥ 0) → ReLU devuelve z sin cambios
```

**Ejemplos numéricos:**
```
ReLU(-5) = max(0, -5) = 0     (el negativo se anula)
ReLU(-0.3) = max(0, -0.3) = 0 (el negativo se anula)
ReLU(0) = max(0, 0) = 0
ReLU(3.2) = max(0, 3.2) = 3.2 (el positivo se mantiene)
ReLU(100) = max(0, 100) = 100 (el positivo se mantiene)
```

**¿Para qué sirve ReLU?**

1. **No satura:** La derivada de ReLU es 1 cuando z > 0, lo que significa que los gradientes fluyen bien durante backpropagation
2. **Simple de calcular:** Solo compara con 0
3. **Muy usada:** Es la activación estándar en capas ocultas

**Comparación con otras activaciones:**
```
Sigmoid: puede saturar (derivada→0 cuando z es muy grande/chico)
Tanh: puede saturar
ReLU: NO satura para valores positivos
```

### L1 Regularization

**¿Qué problema resuelve?**

Imagina que la red aprende estos pesos:
```
Neurona A: w₁ = 150.0 (PESO ENORME)
           w₂ = 0.1
           w₃ = 0.2

Output = 150.0 × input₁ + 0.1 × input₂ + 0.2 × input₃

Problema: La neurona depende CASI EXCLUSIVAMENTE del input₁
Si input₁ cambia un poquito → la predicción cambia mucho
Esto es OVERFITTING (sobreajuste)
```

**Solución: Penalizar pesos grandes**

**Fórmula de L1:**
```
Loss_total = Loss_original + λ × (suma de valores absolutos de pesos)

Donde:
- Loss_original = error de predicción normal
- λ = parámetro que controla cuánto penalizamos (ej: 0.01)
- Suma de valores absolutos = |w₁| + |w₂| + |w₃| + ... + |wₙ|
```

**Ejemplo numérico:**
```
Pesos de una capa:
w₁ = 10.0
w₂ = -8.0
w₃ = 15.0
w₄ = 0.5

Suma de valores absolutos:
|10.0| + |-8.0| + |15.0| + |0.5| = 10.0 + 8.0 + 15.0 + 0.5 = 33.5

Si λ = 0.01:
Penalización L1 = 0.01 × 33.5 = 0.335

Si el error de predicción era 0.25:
Loss_total = 0.25 + 0.335 = 0.585
```

**¿Qué hace esto durante el entrenamiento?**

La red ahora tiene que balancear DOS objetivos:
1. Minimizar el error de predicción
2. Mantener los pesos pequeños

**Resultado:** Pesos se distribuyen más uniformemente en lugar de concentrarse en pocas conexiones

**Característica especial de L1:** Tiende a poner algunos pesos **exactamente en 0**

```
Antes de L1:
w₁ = 10.0, w₂ = -8.0, w₃ = 15.0, w₄ = 0.5, w₅ = -0.8, w₆ = 1.2

Después de entrenar con L1:
w₁ = 8.5, w₂ = -6.2, w₃ = 12.0, w₄ = 0.0, w₅ = 0.0, w₆ = 0.0
                                      ↑ CEROS (conexiones "apagadas")

Beneficio: Red más simple, menos conexiones activas
```

---

## c. ¿De qué tipo de problema se trata?

**Respuesta: Clasificación binaria**

**¿Cómo lo sabemos?**

1. **La variable a predecir es:** Probabilidad de retraso (entre 0 y 1)
2. **Hay solo 2 posibles resultados:** SÍ se retrasa / NO se retrasa
3. **La última capa tiene:** 1 neurona con activación Sigmoid
4. **Sigmoid produce:** Valores entre 0 y 1 (probabilidades)

**Interpretación del output:**
```
Output = 0.85 → 85% probabilidad de retraso → Predice: SÍ se retrasa
Output = 0.15 → 15% probabilidad de retraso → Predice: NO se retrasa

Regla de decisión:
  Si output ≥ 0.5 → clase 1 (SÍ retraso)
  Si output < 0.5 → clase 0 (NO retraso)
```

**Comparación con otros tipos:**
- **NO es multiclase:** tendría N neuronas + Softmax (ej: clasificar en 5 tipos de vehículos)
- **NO es regresión:** no tiene restricción 0-1, predice cualquier número (ej: predecir precio)

---

## d. ¿Qué función de loss usaría?

**Respuesta: Binary Cross-Entropy (BCE)**

### Fórmula matemática

```
BCE = -[y × log(ŷ) + (1-y) × log(1-ŷ)]

Donde:
- y = etiqueta real (0 o 1)
- ŷ = probabilidad predicha por la red (entre 0 y 1)
- log = logaritmo natural
```

### ¿Cómo funciona esta fórmula?

La fórmula tiene DOS términos, pero solo UNO se activa según la etiqueta real:

**CASO 1: Si el vuelo SÍ se retrasó (y = 1)**
```
BCE = -[1 × log(ŷ) + 0 × log(1-ŷ)]
    = -log(ŷ)

El segundo término desaparece porque (1-1) = 0
Solo importa log(ŷ)
```

**Ejemplos numéricos:**
```
Si la red predice ŷ = 0.95 (95% segura que se retrasa):
  BCE = -log(0.95) = 0.051 ← Error pequeño ✓ (buena predicción)

Si la red predice ŷ = 0.50 (50% segura):
  BCE = -log(0.50) = 0.693 ← Error medio

Si la red predice ŷ = 0.10 (10% segura, está MUY equivocada):
  BCE = -log(0.10) = 2.303 ← Error GRANDE ✗ (mala predicción)
```

**CASO 2: Si el vuelo NO se retrasó (y = 0)**
```
BCE = -[0 × log(ŷ) + 1 × log(1-ŷ)]
    = -log(1-ŷ)

El primer término desaparece porque 0 × log(ŷ) = 0
Solo importa log(1-ŷ)
```

**Ejemplos numéricos:**
```
Si la red predice ŷ = 0.05 (5% segura que se retrasa):
  BCE = -log(1-0.05) = -log(0.95) = 0.051 ← Error pequeño ✓

Si la red predice ŷ = 0.50:
  BCE = -log(0.50) = 0.693 ← Error medio

Si la red predice ŷ = 0.90 (90% segura, pero ESTÁ EQUIVOCADA):
  BCE = -log(1-0.90) = -log(0.10) = 2.303 ← Error GRANDE ✗
```

### Ejemplo completo con un batch de 3 vuelos

```
Vuelo 1:
  Etiqueta real: y = 1 (SÍ se retrasó)
  Predicción: ŷ = 0.85
  BCE₁ = -log(0.85) = 0.163

Vuelo 2:
  Etiqueta real: y = 0 (NO se retrasó)
  Predicción: ŷ = 0.15
  BCE₂ = -log(1-0.15) = -log(0.85) = 0.163

Vuelo 3:
  Etiqueta real: y = 1 (SÍ se retrasó)
  Predicción: ŷ = 0.60
  BCE₃ = -log(0.60) = 0.511

Promedio del batch:
BCE_total = (0.163 + 0.163 + 0.511) / 3 = 0.279
```

Este valor 0.279 es lo que la red intentará minimizar durante el entrenamiento.

### ¿Por qué BCE es la correcta?

1. **Matemáticamente fundamentada:** Minimizar BCE = Maximizar la probabilidad de observar las etiquetas correctas
2. **Penaliza fuerte las equivocaciones confiadas:** Si estás 99% seguro pero te equivocas, el error es enorme
3. **Compatible con Sigmoid:** La combinación Sigmoid+BCE tiene buenas propiedades para backpropagation

---

**Fuentes:** Clases 2-01-09-2025, 5-29-09-2025, 6-06-10-2025, 7-13-10-2025
