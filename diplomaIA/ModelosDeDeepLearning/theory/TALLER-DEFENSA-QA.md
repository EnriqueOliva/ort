# Preguntas y Respuestas para Defensa del Taller

Este documento contiene posibles preguntas que podrían hacerse en la defensa del taller, basadas en las entregas 1 y 2.

---

# ENTREGA 1: MLP Toy Example

## Sobre la Arquitectura

### P1: ¿Cuál es la arquitectura de la red que implementaste?

> **R:** Es un MLP (Multi-Layer Perceptron) con:
> - **Entrada:** 1 neurona (x es escalar)
> - **Capa oculta:** 2 neuronas con activación softplus
> - **Salida:** 1 neurona (sin activación, regresión)
>
> Flujo: x → (xW₁ + b₁) → softplus → (aW₂ + b₂) → ŷ

### P2: ¿Qué es la función softplus y por qué se usa?

> **R:** La función softplus es: `softplus(z) = log(1 + e^z)`
>
> Es una versión "suave" de ReLU:
> - ReLU: max(0, z) - tiene un quiebre en z=0
> - Softplus: log(1 + e^z) - es diferenciable en todo punto
>
> La derivada de softplus es la **sigmoide**: σ(z) = 1/(1 + e^(-z))

### P3: ¿Cuáles son las dimensiones de las matrices W1, b1, W2, b2?

> **R:**
> - **W1:** (1, 2) - transforma de 1 entrada a 2 neuronas ocultas
> - **b1:** (2,) - un bias por neurona oculta
> - **W2:** (2, 1) - transforma de 2 ocultas a 1 salida
> - **b2:** escalar - un bias para la salida

### P4: ¿Cuántos parámetros tiene esta red?

> **R:** W1 tiene 2, b1 tiene 2, W2 tiene 2, b2 tiene 1 = **7 parámetros**

---

## Sobre el Forward Pass

### P5: Explica paso a paso el forward pass.

> **R:**
> 1. **Entrada:** x con shape (N, 1) donde N es el número de ejemplos
> 2. **Capa 1:** Z = x @ W1 + b1 → shape (N, 2)
> 3. **Activación:** A = softplus(Z) → shape (N, 2)
> 4. **Capa 2:** ŷ = A @ W2 + b2 → shape (N, 1)

### P6: ¿Qué loss function se usa y cuál es su gradiente?

> **R:** Se usa **MSE (Mean Squared Error)**:
>
> ```
> MSE = (1/N) Σ (ŷᵢ - yᵢ)²
> ```
>
> El gradiente respecto a ŷ es:
> ```
> ∂L/∂ŷ = (2/N)(ŷ - y)
> ```

---

## Sobre el Backward Pass (Backpropagation)

### P7: ¿Cómo se calcula el gradiente de W2 y b2?

> **R:** Usando la regla de la cadena:
>
> ```
> ∂L/∂W2 = Aᵀ @ (∂L/∂ŷ)    → shape (2, 1)
> ∂L/∂b2 = sum(∂L/∂ŷ)       → escalar
> ```
>
> Donde A son las activaciones de la capa oculta.

### P8: ¿Cómo se calcula el gradiente de W1 y b1?

> **R:** Hay que propagar hacia atrás a través de la activación:
>
> ```
> ∂L/∂A = (∂L/∂ŷ) @ W2ᵀ           → shape (N, 2)
> ∂L/∂Z = ∂L/∂A * sigmoid(Z)      → shape (N, 2)  (derivada de softplus)
> ∂L/∂W1 = xᵀ @ (∂L/∂Z)           → shape (1, 2)
> ∂L/∂b1 = sum(∂L/∂Z, axis=0)     → shape (2,)
> ```

### P9: ¿Por qué la derivada de softplus es la sigmoide?

> **R:** Derivando softplus(z) = log(1 + e^z):
>
> ```
> d/dz [log(1 + e^z)] = e^z / (1 + e^z) = 1 / (1 + e^(-z)) = sigmoid(z)
> ```

---

## Sobre el Entrenamiento

### P10: ¿Qué algoritmo de optimización se usa?

> **R:** **Gradient Descent (batch completo)**:
>
> ```
> W = W - lr * ∂L/∂W
> ```
>
> Se procesan todos los datos en cada iteración (no es SGD ni mini-batch).

### P11: ¿Qué hiperparámetros se usan y qué efecto tienen?

> **R:**
> - **Learning rate (lr=0.1):** Qué tan grandes son los pasos. Muy alto = diverge, muy bajo = lento.
> - **Epochs (50000):** Cuántas veces se recorre todo el dataset.
>
> El modelo converge a un MSE cercano a 0 porque los datos son simples.

### P12: ¿Por qué se inicializan los pesos de forma aleatoria y pequeña?

> **R:**
> - **Aleatoria:** Para romper simetría. Si todos empiezan iguales, aprenden lo mismo.
> - **Pequeña (scale=0.3):** Para evitar saturación de activaciones y gradientes muy grandes al inicio.

---

# ENTREGA 2: Double Descent

## Sobre el Fenómeno

### P13: ¿Qué es el fenómeno de Double Descent?

> **R:** Es un patrón donde el error de test NO sigue la curva U clásica del bias-variance tradeoff:
>
> ```
> Error de Test vs Capacidad del Modelo:
>
>                 ↑ pico (interpolation threshold)
>                /\
>               /  \
>              /    \____  ← segundo descenso
>             /
>     ______/
>
>     |-------|---------|----------->
>     bajo    medio     alto (sobreparametrizado)
> ```
>
> Después del pico, agregar más parámetros **mejora** la generalización.

### P14: ¿Qué es el interpolation threshold?

> **R:** Es el punto donde el número de parámetros ≈ número de datos de entrenamiento.
>
> En los experimentos:
> - **4000 ejemplos** de entrenamiento
> - **n_hidden=45** → ~4375 parámetros (cerca del threshold)
>
> En este punto el modelo tiene "justo" la capacidad para memorizar todo, y el error de test es **MÁXIMO**.

### P15: ¿Por qué el error de test es peor en el interpolation threshold?

> **R:** El modelo tiene exactamente la capacidad necesaria para memorizar los datos, pero:
> - No tiene "espacio" para encontrar soluciones más suaves
> - El optimizador encuentra soluciones "tensas" que no generalizan
>
> Es como memorizar las respuestas exactas de un examen sin entender el tema.

---

## Sobre el Ruido en las Etiquetas

### P16: ¿Cómo afecta el ruido en las etiquetas al error mínimo de entrenamiento?

> **R:** El ruido **aumenta** el error mínimo alcanzable:
>
> | Ruido | Error mínimo train |
> |-------|-------------------|
> | 0%    | 0.0000            |
> | 10%   | ~0.0000           |
> | 30%   | 0.0010            |
>
> Con 30% de ruido, hay muestras similares con etiquetas diferentes → contradicción que el modelo no puede resolver perfectamente.

### P17: ¿Cómo influye el ruido en el Double Descent?

> **R:** El ruido **amplifica el pico** en el interpolation threshold:
>
> | Ruido | Error test en el pico (n_hidden≈45) |
> |-------|-------------------------------------|
> | 0%    | 0.4140                              |
> | 10%   | 0.5170                              |
> | 30%   | 0.6445                              |
>
> La forma de la curva se mantiene, pero todo se desplaza hacia arriba.
> Los modelos muy grandes (n_hidden=250) siguen siendo mejores que los del threshold.

---

## Sobre Overfitting vs Sobreparametrización

### P18: ¿Es lo mismo overfitting que sobreparametrización?

> **R:** **NO**, son cosas diferentes:
>
> | Concepto | Definición |
> |----------|------------|
> | **Overfitting** | Bajo error train, alto error test (memoriza sin generalizar) |
> | **Sobreparametrización** | Tener más parámetros que datos |
>
> **Paradoja observada:**
> - n_hidden=50 (cerca del threshold): Error test **PEOR** (0.4140) → overfitting
> - n_hidden=250 (muy sobreparametrizado): Error test **MEJOR** (0.3005) → no overfitting
>
> El overfitting máximo está en el **medio** (interpolation threshold), no con más parámetros.

### P19: ¿Por qué los modelos muy grandes generalizan mejor?

> **R:** Varias hipótesis:
> 1. **Implicit regularization:** El optimizador (SGD/Adam) tiende a encontrar soluciones de baja norma/simples cuando hay muchas soluciones posibles
> 2. **Espacio de soluciones:** Con más parámetros, hay muchas formas de interpolar los datos, y algunas generalizan mejor
> 3. **Suavidad:** El modelo puede encontrar funciones más suaves que se ajustan a los datos

---

## Sobre la Arquitectura y el Experimento

### P20: ¿Cuál es la arquitectura usada en el experimento?

> **R:** MLP con 3 capas:
> ```
> Input (40) → Linear → ReLU → Linear → ReLU → Linear → Output (10)
> ```
> - **Entrada:** 40 (dimensión de MNIST-1D)
> - **Ocultas:** n_hidden neuronas (varía: 2, 10, 26, 45, 48, 50, 55, 70, 120, 200, 250)
> - **Salida:** 10 (clases 0-9)

### P21: ¿Cómo se cuentan los parámetros de esta red?

> **R:** Para n_hidden = H:
>
> ```
> Capa 1: 40 * H + H = 41H
> Capa 2: H * H + H = H² + H
> Capa 3: H * 10 + 10 = 10H + 10
>
> Total = H² + 52H + 10
> ```
>
> Para H=45: 45² + 52*45 + 10 = 2025 + 2340 + 10 = **4375 parámetros**

### P22: ¿Por qué se usa MNIST-1D en lugar de MNIST normal?

> **R:**
> - **MNIST-1D** tiene 40 dimensiones (vs 784 de MNIST normal)
> - Permite entrenar más rápido
> - Muestra el mismo fenómeno de Double Descent
> - 4000 ejemplos de entrenamiento → fácil alcanzar el interpolation threshold

---

## Preguntas Conceptuales Generales

### P23: ¿Qué aprendiste del taller 1 sobre backpropagation?

> **R:**
> - Backprop es aplicar la **regla de la cadena** de forma sistemática
> - Los gradientes se calculan de atrás hacia adelante
> - Cada capa necesita guardar su entrada (cache) para el backward pass
> - La derivada de la activación es crucial (sigmoid para softplus)

### P24: ¿Qué aprendiste del taller 2 sobre el bias-variance tradeoff?

> **R:**
> - El tradeoff clásico dice: más capacidad → más varianza → peor generalización
> - **Double Descent** muestra que esto NO es siempre cierto
> - En el régimen sobreparametrizado, más capacidad puede **mejorar** generalización
> - El punto crítico es el interpolation threshold, no "más parámetros = peor"

### P25: ¿Cómo se relacionan los dos talleres?

> **R:**
> - **Taller 1:** Entender cómo funciona un MLP por dentro (forward, backward, training)
> - **Taller 2:** Usar MLPs para estudiar un fenómeno empírico (Double Descent)
>
> Taller 1 da las bases para entender qué hace la red. Taller 2 muestra que el comportamiento de las redes es más complejo de lo que la teoría clásica predice.

---

## Preguntas de Código

### P26: ¿Qué hace la función `count_parameters`?

> **R:**
> ```python
> def count_parameters(model):
>     return sum(p.numel() for p in model.parameters() if p.requires_grad)
> ```
> Suma el número de elementos de todos los tensores de parámetros entrenables del modelo.

### P27: ¿Por qué se usa `torch.manual_seed(42)` antes de crear cada modelo?

> **R:** Para reproducibilidad. Asegura que la inicialización aleatoria de pesos sea la misma en cada experimento, permitiendo comparaciones justas entre diferentes valores de n_hidden.

### P28: ¿Qué hace el scheduler `StepLR`?

> **R:**
> ```python
> scheduler = StepLR(optimizer, step_size=500, gamma=0.1)
> ```
> Reduce el learning rate por un factor de 0.1 cada 500 epochs.
> Esto ayuda a que el modelo converja mejor al final del entrenamiento.

---

## Preguntas Difíciles (Para Prepararse)

### P29: Si el modelo con 250 unidades ocultas generaliza mejor que uno con 50, ¿por qué no usar siempre modelos enormes?

> **R:** Porque hay trade-offs:
> - **Costo computacional:** Más parámetros = más memoria y tiempo
> - **El fenómeno depende del problema:** No siempre hay Double Descent
> - **Requiere más datos:** Para problemas más complejos, el threshold se mueve
> - **En la práctica:** Se usa regularización, dropout, early stopping que cambian la dinámica

### P30: ¿El Double Descent ocurre en todos los modelos y datasets?

> **R:** No necesariamente. Depende de:
> - El tipo de modelo (se ve más en redes neuronales)
> - El dataset (más común con datos ruidosos)
> - El método de entrenamiento (SGD vs otros optimizadores)
> - La arquitectura específica
>
> Es un fenómeno empírico observado, pero no universal.
