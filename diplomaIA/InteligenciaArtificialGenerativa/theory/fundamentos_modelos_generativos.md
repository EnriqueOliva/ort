# Fundamentos de Modelos Generativos

Este documento explica todos los conceptos fundamentales necesarios antes de estudiar modelos generativos específicos (VAE, GAN, Difusión, etc.). Cubre las clases 1-5 del curso.

---

## Tabla de Contenidos

0. [Dos Preguntas Fundamentales](#0-dos-preguntas-fundamentales)
   - [¿Por Qué Estimar P(imagen) Nos Permite Generar?](#01-por-qué-estimar-pimagen-nos-permite-generar-imágenes-nuevas)
   - [Relación Perceptrón de Hinton y Modelos Autorregresivos](#02-cuál-es-la-relación-entre-el-perceptrón-de-hinton-y-los-modelos-autorregresivos)
1. [¿Qué es un Modelo Generativo?](#1-qué-es-un-modelo-generativo)
2. [Conceptos de Probabilidad](#2-conceptos-de-probabilidad)
3. [Redes Bayesianas](#3-redes-bayesianas)
4. [Variables Aleatorias Continuas](#4-variables-aleatorias-continuas)
5. [Mezclas de Distribuciones](#5-mezclas-de-distribuciones)
6. [La Cadena de Evolución: Del Problema a la Solución](#6-la-cadena-de-evolución-del-problema-a-la-solución)
7. [Modelos Autorregresivos](#7-modelos-autorregresivos)
8. [El Perceptrón como Estimador de Distribuciones](#8-el-perceptrón-como-estimador-de-distribuciones)
9. [Por Qué Entrenar es Paralelo pero Generar es Secuencial](#9-por-qué-entrenar-es-paralelo-pero-generar-es-secuencial)
10. [Entrenamiento: De KL Divergence a BCE](#10-entrenamiento-de-kl-divergence-a-bce)
11. [El Proceso Completo: Del Dato a la Generación](#11-el-proceso-completo-del-dato-a-la-generación)

---

## 0. Dos Preguntas Fundamentales

Antes de entrar en detalle, respondamos dos preguntas que son la clave de todo:

### 0.1 ¿Por Qué Estimar P(imagen) Nos Permite Generar Imágenes Nuevas?

Esta es la pregunta más importante y a veces se pasa por alto. Vamos paso a paso:

**¿Qué significa "generar"?**

Generar = **muestrear** de una distribución de probabilidad.

```
┌─────────────────────────────────────────────────────────────────┐
│                    ¿QUÉ ES MUESTREAR?                           │
│                                                                 │
│   Ejemplo simple: Moneda cargada                                │
│   ──────────────────────────────                                │
│   Si sé que P(cara) = 0.7, puedo "generar" tiradas así:         │
│                                                                 │
│   1. Genero número aleatorio entre 0 y 1 (ej: 0.45)            │
│   2. Si el número < 0.7 → salió "cara"                          │
│   3. Si el número ≥ 0.7 → salió "cruz"                          │
│                                                                 │
│   ¡Eso es muestrear! Convertir una probabilidad en un dato      │
│   concreto usando aleatoriedad.                                 │
│                                                                 │
│   ═══════════════════════════════════════════════════════════   │
│                                                                 │
│   Para imágenes es IGUAL:                                       │
│   ────────────────────────                                      │
│   Si conozco P(píxel=1 | píxeles anteriores) = 0.65             │
│                                                                 │
│   1. Genero número aleatorio (ej: 0.30)                         │
│   2. 0.30 < 0.65, entonces píxel = 1 (blanco)                  │
│                                                                 │
│   Repito para cada píxel y ¡tengo una imagen generada!         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**La conexión clave:**

```
┌─────────────────────────────────────────────────────────────────┐
│              ESTIMAR → MUESTREAR → GENERAR                      │
│                                                                 │
│   PASO 1: ESTIMAR                                               │
│   ─────────────────                                             │
│   Aprendemos P(imagen) de los datos de entrenamiento.           │
│   Más precisamente: aprendemos P(Xᵢ | anteriores) para cada i.  │
│                                                                 │
│   PASO 2: MUESTREAR                                             │
│   ──────────────────                                            │
│   Usamos esas probabilidades aprendidas para "tirar la moneda"  │
│   en cada posición y obtener valores concretos (0 o 1).         │
│                                                                 │
│   PASO 3: GENERAR                                               │
│   ─────────────────                                             │
│   El resultado del muestreo ES la imagen generada.              │
│   Es una imagen NUEVA (no estaba en el dataset).                │
│   Pero se PARECE a las del dataset porque usamos las mismas     │
│   probabilidades que aprendimos de ellas.                       │
│                                                                 │
│   ═══════════════════════════════════════════════════════════   │
│                                                                 │
│   ¿Por qué las imágenes generadas se parecen a las reales?      │
│   ─────────────────────────────────────────────────────────     │
│   Porque las PROBABILIDADES fueron aprendidas de imágenes       │
│   reales. Si en las fotos de gatos el píxel 100 suele ser       │
│   blanco cuando los píxeles 1-99 forman cierto patrón,          │
│   nuestro modelo aprendió eso y lo replica al generar.          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Analogía del profesor:** Es como tener una receta de cocina probabilística. La receta dice "si ya pusiste harina y huevos, hay 70% de probabilidad de que el siguiente ingrediente sea azúcar". Siguiendo la receta (muestreando), generas un postre nuevo pero que sigue los patrones de los postres que inspiraron la receta.

### 0.2 ¿Qué es el Perceptrón de Hinton?

#### Definición directa

El **perceptrón de Hinton** es una función matemática:

```
P(Xᵢ = 1 | X₁, X₂, ..., Xᵢ₋₁) = σ(w₁X₁ + w₂X₂ + ... + wᵢ₋₁Xᵢ₋₁ + b)
```

Donde:
- **Xⱼ** = valor del píxel j (0 o 1)
- **wⱼ** = peso aprendible asociado al píxel j
- **b** = bias aprendible
- **σ** = función sigmoide: σ(z) = 1/(1 + e^(-z))

**¿Qué hace?** Recibe los valores de los píxeles anteriores y devuelve un número entre 0 y 1 que representa la probabilidad de que el píxel actual sea 1.

#### ¿Por qué existe?

**El problema:** Queremos calcular P(Xᵢ | X₁, ..., Xᵢ₋₁) para cada píxel i.

**Opción 1 - Tabla:** Guardar la probabilidad para cada combinación posible de píxeles anteriores.
- Para el píxel 10, necesito guardar un valor para cada combinación de X₁...X₉
- Eso son 2^9 = 512 valores
- Para el píxel 784, serían 2^783 valores (más que átomos en el universo)
- **IMPOSIBLE**

**Opción 2 - Perceptrón:** Usar una función con pocos parámetros que APROXIME esa tabla.
- Para el píxel 10, necesito 9 pesos + 1 bias = 10 parámetros
- Para el píxel 784, necesito 783 pesos + 1 bias = 784 parámetros
- **POSIBLE**

```
┌─────────────────────────────────────────────────────────────────┐
│                    TABLA vs PERCEPTRÓN                          │
│                                                                 │
│   Píxel     Tabla (parámetros)    Perceptrón (parámetros)      │
│   ─────     ──────────────────    ───────────────────────       │
│     2              2                        2                   │
│     3              4                        3                   │
│     5             16                        5                   │
│    10            512                       10                   │
│    20        524,288                       20                   │
│   100         10^30                       100                   │
│   784        10^236                       784                   │
│                                                                 │
│   La tabla crece EXPONENCIALMENTE: 2^(i-1)                      │
│   El perceptrón crece LINEALMENTE: i                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### ¿Qué es la sigmoide y por qué la usamos?

**¿Qué es la sigmoide?**

Es una función matemática con esta fórmula:

```
σ(z) = 1 / (1 + e^(-z))
```

Donde `e` es el número de Euler (≈ 2.718).

**¿Qué hace?** Toma CUALQUIER número real y lo transforma a un número entre 0 y 1.

```
┌─────────────────────────────────────────────────────────────────┐
│                    QUÉ HACE LA SIGMOIDE                         │
│                                                                 │
│   ENTRADA (z)          SALIDA σ(z)                              │
│   ───────────          ───────────                              │
│      -100         →      0.0000...  (prácticamente 0)           │
│       -10         →      0.00005                                │
│        -5         →      0.007                                  │
│        -2         →      0.12                                   │
│        -1         →      0.27                                   │
│         0         →      0.50       (exactamente la mitad)      │
│        +1         →      0.73                                   │
│        +2         →      0.88                                   │
│        +5         →      0.993                                  │
│       +10         →      0.99995                                │
│      +100         →      0.9999...  (prácticamente 1)           │
│                                                                 │
│   Gráficamente tiene forma de "S":                              │
│                                                                 │
│        1 ─────────────────────────────────····                  │
│          │                           ······                     │
│          │                       ····                           │
│      0.5 │─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ·· ─ ─ ─ ─ ─ ─ ─                  │
│          │               ····                                   │
│          │           ····                                       │
│        0 ────····───────────────────────────                    │
│             -5    -2    0    +2    +5                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**¿Por qué la necesitamos?**

El problema es este:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   PASO 1: Calculamos una suma ponderada                         │
│   ─────────────────────────────────────                         │
│   z = w₁X₁ + w₂X₂ + w₃X₃ + b                                    │
│                                                                 │
│   Ejemplo con pesos entrenados:                                 │
│   w₁ = 2.5, w₂ = -1.3, w₃ = 0.8, b = -0.5                       │
│   Si X₁=1, X₂=0, X₃=1:                                          │
│   z = 2.5(1) + (-1.3)(0) + 0.8(1) + (-0.5) = 2.8                │
│                                                                 │
│   PROBLEMA: z puede ser CUALQUIER número                        │
│   - Si los pesos son grandes y positivos → z = +500             │
│   - Si los pesos son grandes y negativos → z = -500             │
│   - z puede ir de -∞ a +∞                                       │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   PASO 2: Necesitamos una PROBABILIDAD                          │
│   ──────────────────────────────────────                        │
│   Una probabilidad DEBE estar entre 0 y 1.                      │
│   - P = 0.7 ✓  (válido)                                         │
│   - P = 0.01 ✓ (válido)                                         │
│   - P = 2.8 ✗  (inválido, >1)                                   │
│   - P = -3.5 ✗ (inválido, <0)                                   │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   SOLUCIÓN: La sigmoide transforma z al rango válido            │
│   ────────────────────────────────────────────────────          │
│   z = 2.8  →  σ(2.8) = 1/(1+e^(-2.8)) = 0.94                    │
│                                                                 │
│   Ahora 0.94 SÍ es una probabilidad válida.                     │
│   Significa: "hay 94% de probabilidad de que este píxel sea 1"  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**¿Por qué no usar otra cosa?**

Podríamos usar otras funciones que también mapean a (0,1), pero la sigmoide tiene propiedades matemáticas útiles:
- Es diferenciable (necesario para entrenar con gradiente descendente)
- Su derivada es simple: σ'(z) = σ(z)(1-σ(z))
- Es la función "natural" para modelar probabilidades binarias (sale de la teoría de máxima verosimilitud)

**Resumen:**
- La suma ponderada da cualquier número
- La sigmoide lo aplasta entre 0 y 1
- Ahora tenemos una probabilidad válida

#### ¿Qué tiene que ver con Bernoulli?

Un píxel binario (0 o 1) sigue una distribución **Bernoulli** con parámetro θ:
- P(X = 1) = θ
- P(X = 0) = 1 - θ

El perceptrón **calcula ese θ**. La salida del perceptrón ES el parámetro de la Bernoulli.

```
Ejemplo concreto:

El perceptrón recibe X₁=1, X₂=0, X₃=1 y calcula:
  z = w₁(1) + w₂(0) + w₃(1) + b = 0.8
  θ = σ(0.8) = 0.69

Esto significa:
  P(X₄ = 1 | X₁=1, X₂=0, X₃=1) = 0.69
  P(X₄ = 0 | X₁=1, X₂=0, X₃=1) = 0.31

Para generar X₄:
  - Genero número aleatorio r entre 0 y 1
  - Si r < 0.69 → X₄ = 1
  - Si r ≥ 0.69 → X₄ = 0
```

#### La innovación de Hinton: La matriz triangular

En vez de tener 784 perceptrones separados, Hinton los empaquetó en **una sola matriz**:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   784 perceptrones separados:                                   │
│   ───────────────────────────                                   │
│   P₁ = σ(b₁)                          ← solo bias               │
│   P₂ = σ(w₂₁X₁ + b₂)                  ← 1 peso + bias           │
│   P₃ = σ(w₃₁X₁ + w₃₂X₂ + b₃)          ← 2 pesos + bias          │
│   P₄ = σ(w₄₁X₁ + w₄₂X₂ + w₄₃X₃ + b₄)  ← 3 pesos + bias          │
│   ...                                                           │
│                                                                 │
│   UNA matriz triangular inferior:                               │
│   ───────────────────────────────                               │
│                                                                 │
│   ┌                    ┐   ┌    ┐   ┌    ┐       ┌    ┐         │
│   │ 0    0    0    0   │   │ X₁ │   │ b₁ │       │ P₁ │         │
│   │ w₂₁  0    0    0   │ × │ X₂ │ + │ b₂ │ → σ → │ P₂ │         │
│   │ w₃₁  w₃₂  0    0   │   │ X₃ │   │ b₃ │       │ P₃ │         │
│   │ w₄₁  w₄₂  w₄₃  0   │   │ X₄ │   │ b₄ │       │ P₄ │         │
│   └                    ┘   └    ┘   └    ┘       └    ┘         │
│          W                  X         b            P            │
│                                                                 │
│   Los CEROS arriba de la diagonal son fundamentales:            │
│   - La fila 3 tiene cero en las columnas 3 y 4                  │
│   - Por eso P₃ solo "ve" X₁ y X₂, no X₃ ni X₄                   │
│   - Esto GARANTIZA la estructura autorregresiva                 │
│                                                                 │
│   Beneficio: P = σ(W·X + b) calcula TODO de una vez             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Relación con otros conceptos del curso

```
┌─────────────────────────────────────────────────────────────────┐
│           CÓMO SE CONECTA CON TODO LO DEMÁS                     │
│                                                                 │
│   REGLA DEL PRODUCTO (Clase 1-2)                                │
│   ──────────────────────────────                                │
│   P(X₁,...,Xₙ) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂) × ...          │
│                                                                 │
│   El perceptrón de Hinton CALCULA cada uno de esos términos.    │
│   La regla del producto dice QUÉ calcular.                      │
│   El perceptrón dice CÓMO calcularlo.                           │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   MODELO AUTORREGRESIVO (Clase 3)                               │
│   ───────────────────────────────                               │
│   Es la estrategia de usar la regla del producto para generar   │
│   datos secuencialmente: primero X₁, después X₂, etc.           │
│                                                                 │
│   El perceptrón de Hinton es la HERRAMIENTA que usa el modelo   │
│   autorregresivo para calcular cada probabilidad condicional.   │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   DISTRIBUCIÓN BERNOULLI (Clase 3)                              │
│   ────────────────────────────────                              │
│   Cada píxel binario sigue una Bernoulli con parámetro θ.       │
│                                                                 │
│   El perceptrón de Hinton ESTIMA ese θ para cada píxel.         │
│   Recibe los píxeles anteriores → devuelve θ.                   │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   BCE - BINARY CROSS ENTROPY (Clase 4-5)                        │
│   ──────────────────────────────────────                        │
│   BCE(x, p) = -x·log(p) - (1-x)·log(1-p)                        │
│                                                                 │
│   Es la función de pérdida que usamos para ENTRENAR el          │
│   perceptrón. Compara la probabilidad predicha (p) con el       │
│   valor real del píxel (x) del dataset.                         │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   KL DIVERGENCE (Clase 5)                                       │
│   ───────────────────────                                       │
│   Minimizar KL(P_data || P_modelo) es equivalente a             │
│   minimizar la suma de BCEs sobre todos los píxeles.            │
│                                                                 │
│   Entrenar el perceptrón minimizando BCE = hacer que el         │
│   modelo se parezca a la distribución real de los datos.        │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   MODELOS POSTERIORES (NADE, MADE, PixelCNN, GPT)               │
│   ───────────────────────────────────────────────               │
│   Son MEJORAS al perceptrón de Hinton:                          │
│                                                                 │
│   - NADE: Comparte pesos entre posiciones → menos parámetros    │
│   - MADE: Usa máscaras en vez de matriz triangular explícita    │
│   - PixelCNN: Usa convoluciones en vez de fully connected       │
│   - GPT: Usa transformers, mismo principio autorregresivo       │
│                                                                 │
│   Todos siguen la misma idea: aproximar P(Xᵢ|anteriores)        │
│   con una red neuronal, pero con arquitecturas más potentes.    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### ¿Qué diferencia hay con el MLP de clasificación?

En Deep Learning ven el **MLP (Multi-Layer Perceptron)** para clasificación. Es importante entender qué comparten y qué los diferencia del perceptrón de Hinton.

**¿Qué es el MLP de clasificación?**

```
┌─────────────────────────────────────────────────────────────────┐
│                    MLP PARA CLASIFICACIÓN                       │
│                                                                 │
│   Entrada: Una imagen completa X (784 píxeles)                  │
│   Salida: Una clase Y (ej: "es un 7", "es un 3", etc.)          │
│                                                                 │
│   Arquitectura típica:                                          │
│                                                                 │
│   X (784) → [Capa oculta 256] → [Capa oculta 128] → Y (10)     │
│              con ReLU           con ReLU          con Softmax   │
│                                                                 │
│   ¿Qué calcula?                                                 │
│   P(Y = clase | X = imagen)                                     │
│                                                                 │
│   "Dada esta imagen, ¿qué dígito es?"                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**¿Qué es el perceptrón de Hinton?**

```
┌─────────────────────────────────────────────────────────────────┐
│                   PERCEPTRÓN DE HINTON                          │
│                                                                 │
│   Entrada: Píxeles anteriores X₁, X₂, ..., Xᵢ₋₁                │
│   Salida: Probabilidad del píxel actual Xᵢ                      │
│                                                                 │
│   Arquitectura:                                                 │
│                                                                 │
│   X₁...Xᵢ₋₁ → [Suma ponderada + bias] → Pᵢ                     │
│                     con Sigmoide                                │
│                                                                 │
│   ¿Qué calcula?                                                 │
│   P(Xᵢ = 1 | X₁, ..., Xᵢ₋₁)                                    │
│                                                                 │
│   "Dados los píxeles anteriores, ¿cuál es la probabilidad       │
│    de que este píxel sea blanco?"                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Comparación directa:**

```
┌─────────────────────────────────────────────────────────────────┐
│              MLP CLASIFICACIÓN vs PERCEPTRÓN HINTON             │
│                                                                 │
│                    MLP Clasificación    Perceptrón Hinton       │
│                    ──────────────────   ─────────────────       │
│                                                                 │
│   Objetivo         Predecir etiqueta    Generar datos           │
│                    P(Y|X)               P(X) vía P(Xᵢ|ant.)     │
│                                                                 │
│   Entrada          Imagen COMPLETA      Píxeles ANTERIORES      │
│                    (784 valores)        (i-1 valores)           │
│                                                                 │
│   Salida           Clase (1 de 10)      Probabilidad (0 a 1)    │
│                                                                 │
│   Capas            Múltiples capas      UNA capa (lineal)       │
│                    ocultas                                      │
│                                                                 │
│   Activación       ReLU + Softmax       Solo Sigmoide           │
│   salida                                                        │
│                                                                 │
│   Matriz pesos     Densa (todos con     Triangular inferior     │
│                    todos)               (solo anteriores)       │
│                                                                 │
│   Uso              Clasificar           Generar                 │
│                    "¿Qué número es?"    "Crear un número"       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**¿Qué comparten?**

1. **Son redes neuronales:** Ambos tienen pesos (W), biases (b), y funciones de activación
2. **Se entrenan con gradiente descendente:** Ambos usan backpropagation para ajustar pesos
3. **Usan funciones de activación:** Sigmoide, ReLU, Softmax, etc.
4. **Aproximan funciones:** En vez de tablas, usan parámetros aprendibles

**¿Qué los diferencia fundamentalmente?**

```
┌─────────────────────────────────────────────────────────────────┐
│                   LA DIFERENCIA FUNDAMENTAL                     │
│                                                                 │
│   MLP CLASIFICACIÓN:                                            │
│   ──────────────────                                            │
│   Calcula P(Y | X) → "¿Qué etiqueta tiene este dato?"           │
│                                                                 │
│   - X es la ENTRADA (dato completo, conocido)                   │
│   - Y es la SALIDA (etiqueta a predecir)                        │
│   - NO genera datos nuevos, solo clasifica existentes           │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   PERCEPTRÓN DE HINTON:                                         │
│   ──────────────────────                                        │
│   Calcula P(Xᵢ | X<ᵢ) → "¿Qué valor tiene el siguiente píxel?"  │
│                                                                 │
│   - X<ᵢ es la ENTRADA (píxeles anteriores)                      │
│   - Xᵢ es la SALIDA (píxel a generar)                           │
│   - SÍ genera datos nuevos, muestreando secuencialmente         │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   CLAVE: El MLP ve TODO el dato y predice una etiqueta.         │
│          Hinton ve PARTE del dato y predice el siguiente trozo. │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**¿Por qué el perceptrón de Hinton es tan simple (una capa)?**

El perceptrón de Hinton original es simple porque:
1. Era una prueba de concepto de 2006
2. Funciona para imágenes pequeñas (28×28)
3. Es fácil de entender y analizar

Los modelos modernos (NADE, MADE, PixelCNN, GPT) usan arquitecturas más complejas (múltiples capas, convoluciones, atención) pero siguen el mismo principio: calcular P(Xᵢ|anteriores).

**Resumen:**
- **MLP clasificación:** Imagen completa → Etiqueta (discriminativo)
- **Perceptrón Hinton:** Píxeles anteriores → Siguiente píxel (generativo)
- Ambos son redes neuronales, pero resuelven problemas opuestos

#### Resumen en una oración

El perceptrón de Hinton es una red neuronal con matriz triangular que aproxima cada probabilidad condicional P(Xᵢ|anteriores), permitiendo usar la regla del producto para modelar y generar imágenes sin necesitar tablas exponencialmente grandes.

---

## 1. ¿Qué es un Modelo Generativo?

### La Diferencia Fundamental

En Machine Learning tradicional (clasificación, regresión), entrenamos modelos para **predecir** algo:
- "¿Esta imagen es un gato o un perro?"
- "¿Cuánto va a llover mañana?"

En **Inteligencia Artificial Generativa**, el objetivo es completamente diferente: queremos **crear datos nuevos** que se parezcan a los datos reales.

```
┌─────────────────────────────────────────────────────────────────┐
│                     MACHINE LEARNING TRADICIONAL                │
│                                                                 │
│    Imagen ──────► [Modelo] ──────► "Es un gato" (etiqueta)     │
│                                                                 │
│    El modelo responde UNA pregunta: ¿qué es esto?              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                     MODELO GENERATIVO                           │
│                                                                 │
│    Ruido ──────► [Modelo] ──────► Nueva imagen de gato         │
│                                                                 │
│    El modelo CREA algo nuevo que no existía                     │
└─────────────────────────────────────────────────────────────────┘
```

### ¿Qué Significa "Generar"?

Generar datos significa **muestrear** de una distribución de probabilidad.

**Analogía simple:** Imagina que tienes una bolsa con muchas bolitas de colores. Si sabes que hay 50% rojas, 30% azules y 20% verdes, puedes "generar" el color de una bolita eligiendo al azar según esas probabilidades.

Con imágenes es igual, pero mucho más complejo:
- Tenemos miles de fotos de gatos
- Queremos aprender "cómo son los gatos" (qué patrones tienen, qué colores, qué formas)
- Y luego poder crear NUEVAS fotos que sigan ese mismo patrón

**El problema central es:** ¿Cómo estimamos la distribución de probabilidad de datos complejos como imágenes?

### ¿Por Qué es Difícil?

Una imagen de 28×28 píxeles en blanco y negro tiene 784 píxeles. Cada píxel puede ser 0 (negro) o 1 (blanco).

El número total de imágenes posibles es: **2^784 ≈ 10^236**

Para comparar: hay aproximadamente 10^80 átomos en el universo observable.

**Es IMPOSIBLE** hacer una tabla que diga "esta imagen tiene probabilidad X, esta otra tiene probabilidad Y..." porque hay más imágenes posibles que átomos en el universo.

Necesitamos formas inteligentes de representar esta distribución sin enumerar todas las posibilidades.

---

## 2. Conceptos de Probabilidad

Antes de entender modelos generativos, necesitamos dominar estos conceptos básicos de probabilidad. Son la base matemática de todo lo que sigue.

### 2.1 Variable Aleatoria

Una **variable aleatoria** es algo que puede tomar diferentes valores con cierta probabilidad.

**Ejemplos:**
- El resultado de lanzar un dado (valores: 1, 2, 3, 4, 5, 6)
- El clima de mañana (valores: soleado, nublado, lluvioso)
- El valor de un píxel en una imagen (valores: 0 a 255, o simplemente 0 y 1)

**¿Por qué nos importa?** Porque vamos a pensar cada píxel de una imagen como una variable aleatoria. Una imagen de 784 píxeles = 784 variables aleatorias.

### 2.2 Probabilidad Conjunta

La **probabilidad conjunta** P(X, Y) nos dice la probabilidad de que **ambos** eventos ocurran simultáneamente.

```
Ejemplo: Dado + Moneda

         │ Cara  │ Cruz
─────────┼───────┼──────
Dado = 1 │ 1/12  │ 1/12
Dado = 2 │ 1/12  │ 1/12
Dado = 3 │ 1/12  │ 1/12
Dado = 4 │ 1/12  │ 1/12
Dado = 5 │ 1/12  │ 1/12
Dado = 6 │ 1/12  │ 1/12

P(Dado=3, Moneda=Cara) = 1/12
```

**¿Por qué nos importa?** Porque la probabilidad de una imagen es la probabilidad conjunta de TODOS sus píxeles:
```
P(imagen) = P(píxel1, píxel2, píxel3, ..., píxel784)
```

### 2.3 Probabilidad Marginal (Regla de la Suma)

La **probabilidad marginal** P(X) es la probabilidad de un evento, ignorando las otras variables. Se obtiene **sumando** sobre todos los valores posibles de la otra variable.

```
P(X = x) = Σᵢ P(X = x, Y = yᵢ)
```

**Ejemplo:** ¿Cuál es la probabilidad de que la moneda sea Cara?

```
P(Cara) = P(Dado=1, Cara) + P(Dado=2, Cara) + ... + P(Dado=6, Cara)
P(Cara) = 1/12 + 1/12 + 1/12 + 1/12 + 1/12 + 1/12 = 6/12 = 1/2
```

**¿Por qué nos importa?** Porque a veces queremos saber la probabilidad de algo sin importar el resto. Por ejemplo: "¿Cuál es la probabilidad de que el píxel 5 sea blanco?" sin importar los demás píxeles.

### 2.4 Probabilidad Condicional

La **probabilidad condicional** P(Y|X) nos dice la probabilidad de Y **dado que YA SABEMOS** que X ocurrió.

```
P(Y|X) = P(X,Y) / P(X)
```

**Ejemplo:** Si sé que salió un número par en el dado, ¿cuál es la probabilidad de que sea un 4?

```
P(Dado=4 | Dado es par) = P(Dado=4) / P(Dado es par) = (1/6) / (3/6) = 1/3
```

**¿Por qué nos importa?** Porque vamos a generar imágenes píxel por píxel. Cuando generamos el píxel 5, ya conocemos los píxeles 1, 2, 3 y 4. Entonces necesitamos:
```
P(píxel5 | píxel1, píxel2, píxel3, píxel4)
```

### 2.5 Regla del Producto (MUY IMPORTANTE)

Esta regla nos permite **descomponer** una probabilidad conjunta en un **producto** de condicionales:

```
P(X, Y) = P(X) × P(Y|X)
```

Por simetría, también:
```
P(X, Y) = P(Y) × P(X|Y)
```

**¿Por qué es TAN importante?** Porque nos permite transformar un problema imposible en problemas manejables:

```
┌─────────────────────────────────────────────────────────────────┐
│                    LA MAGIA DE LA REGLA DEL PRODUCTO            │
│                                                                 │
│   PROBLEMA ORIGINAL:                                            │
│   Estimar P(X₁, X₂, X₃) directamente                           │
│   → Necesitamos una tabla con 2³ = 8 entradas                   │
│                                                                 │
│   CON REGLA DEL PRODUCTO:                                       │
│   P(X₁, X₂, X₃) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂)               │
│                                                                 │
│   → Dividimos en 3 problemas más pequeños                       │
│   → Cada uno se puede estimar por separado                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.6 Generalización para N Variables

Para muchas variables aleatorias, la regla del producto se generaliza así:

```
P(X₁, X₂, ..., Xₙ) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂) × ... × P(Xₙ|X₁,...,Xₙ₋₁)
```

O de forma compacta (productoria):

```
P(X₁, ..., Xₙ) = ∏ᵢ₌₁ⁿ P(Xᵢ | X₁, ..., Xᵢ₋₁)
```

**Diagrama:**

```
┌──────────────────────────────────────────────────────────────────────┐
│                    REGLA DEL PRODUCTO GENERALIZADA                   │
│                                                                      │
│  P(X₁,X₂,X₃) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂)                       │
│                                                                      │
│      ↓           ↓              ↓                                    │
│   [Prior]   [Condicional   [Condicional                              │
│    (base)    simple]        compuesta]                               │
│                                                                      │
│  Observa: Cada término depende de TODOS los anteriores               │
│  X₃ depende de X₁ Y de X₂, no solo de X₂                             │
└──────────────────────────────────────────────────────────────────────┘
```

### 2.7 Independencia

Dos variables son **independientes** si conocer una no nos da información sobre la otra:

```
X ⊥ Y  significa que  P(X,Y) = P(X) × P(Y)
```

También implica que:
```
P(Y|X) = P(Y)    (saber X no cambia la probabilidad de Y)
```

**Ejemplo:** El resultado de tirar un dado NO afecta el resultado de tirar una moneda. Son independientes.

**Contraejemplo:** El peso de una persona y su altura NO son independientes. Si sabes que alguien pesa 120kg, probablemente es alto.

**¿Por qué nos importa?** Si las variables son independientes, la probabilidad conjunta se simplifica ENORMEMENTE:

```
Si X₁, X₂, ..., Xₙ son TODAS independientes:
P(X₁, X₂, ..., Xₙ) = P(X₁) × P(X₂) × ... × P(Xₙ)

¡No hay condicionales! Solo multiplicamos las marginales.
```

**Problema:** Los píxeles de una imagen NO son independientes. El píxel de al lado del ojo probablemente también es parte del ojo.

### 2.8 Independencia Condicional

Esta es una noción **intermedia** muy útil. Decimos que X y Z son **condicionalmente independientes dado Y** si:

```
P(X,Z|Y) = P(X|Y) × P(Z|Y)
```

**¿Qué significa en palabras simples?** Si YA conocemos Y, entonces conocer X no nos da más información sobre Z (y viceversa).

**Ejemplo del gato:**
- Y = sexo del gato (macho/hembra)
- X = peso del gato
- Z = longitud del gato

Sin saber el sexo: peso y longitud están relacionados (gatos grandes pesan más)
Sabiendo el sexo: dado que es macho, el peso ya no te dice mucho sobre la longitud (dentro de la categoría "macho", la variación es más aleatoria)

**¿Por qué nos importa?** Porque nos permite simplificar la regla del producto:

```
SIN independencia condicional:
P(X,Y,Z) = P(X) × P(Y|X) × P(Z|X,Y)
                           ↑
                    Z depende de X e Y

CON independencia condicional (Z indep. de X dado Y):
P(X,Y,Z) = P(X) × P(Y|X) × P(Z|Y)
                           ↑
                    Z solo depende de Y
                    (nos "ahorramos" considerar X)
```

### 2.9 El Problema de la Dimensionalidad

Aquí está el problema central que motiva TODO el curso:

**Si tenemos N variables aleatorias y cada una puede tomar K valores:**
- La tabla completa de probabilidad conjunta tiene **K^N** entradas
- Para una imagen de 28×28 píxeles en blanco y negro: 2^784 ≈ 10^236 entradas

```
┌─────────────────────────────────────────────────────────────────┐
│               EL PROBLEMA DE LA DIMENSIONALIDAD                 │
│                                                                 │
│   Variables    Valores     Entradas en tabla                    │
│   ──────────   ───────     ─────────────────                    │
│       2           2              4           ← Fácil            │
│       3           2              8           ← Fácil            │
│      10           2           1,024         ← Manejable         │
│      20           2         1,048,576       ← Difícil           │
│     100           2         2^100 ≈ 10^30   ← Imposible         │
│     784           2         2^784 ≈ 10^236  ← MUY Imposible     │
│                                                                 │
│   Para contexto: átomos en el universo ≈ 10^80                  │
│                                                                 │
│   ¡IMPOSIBLE estimar tablas para imágenes!                      │
└─────────────────────────────────────────────────────────────────┘
```

**La pregunta del curso:** ¿Cómo representamos P(imagen) sin necesitar 10^236 números?

---

## 3. Redes Bayesianas

Las **Redes Bayesianas** (Belief Networks) son una forma de representar las relaciones de dependencia entre variables aleatorias usando un grafo. Fueron propuestas como una forma de SIMPLIFICAR el problema de la dimensionalidad.

### 3.1 ¿Qué es una Red Bayesiana?

Es un **grafo dirigido acíclico** (las flechas no forman ciclos) donde:
- **Nodos** = Variables aleatorias
- **Arcos (flechas)** = Relaciones de dependencia directa

**La idea clave:** Si no hay flecha de A a B, entonces B no depende DIRECTAMENTE de A.

```
┌─────────────────────────────────────────────────────────────────┐
│                    EJEMPLOS DE REDES BAYESIANAS                 │
│                                                                 │
│   CASO 1: Independencia Total        CASO 2: Dependencia Total  │
│   (no hay flechas)                   (cadena completa)          │
│                                                                 │
│       (X)    (Y)    (Z)                    (X)                  │
│                                             ↓                   │
│   P(X,Y,Z) = P(X)×P(Y)×P(Z)               (Y)                  │
│                                             ↓                   │
│   Parámetros: solo 3 valores               (Z)                  │
│   (uno por variable)                                            │
│                                      P(X,Y,Z) = P(X)×P(Y|X)×P(Z|X,Y)
│                                      Parámetros: muchos más     │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   CASO 3: Independencia Condicional (Cadena de Markov)          │
│                                                                 │
│              (X)                                                │
│               ↓                                                 │
│              (Y)     ← Y depende de X                           │
│               ↓                                                 │
│              (Z)     ← Z depende SOLO de Y (no de X)            │
│                                                                 │
│   P(X,Y,Z) = P(X) × P(Y|X) × P(Z|Y)                             │
│                               ↑                                 │
│                          ¡Solo Y! No X                          │
│                                                                 │
│   Esto REDUCE los parámetros necesarios                         │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Propiedades de Markov

Cuando asumimos que cada variable **solo depende de su inmediata anterior** (no de todas las anteriores), obtenemos una **cadena de Markov**:

```
P(X₁, X₂, ..., Xₙ) = P(X₁) × P(X₂|X₁) × P(X₃|X₂) × ... × P(Xₙ|Xₙ₋₁)
```

**Compara con la versión general:**
```
General:  P(X₃|X₁,X₂)  ← depende de X₁ Y X₂
Markov:   P(X₃|X₂)     ← solo depende de X₂
```

**¿Por qué es útil?** Reduce DRÁSTICAMENTE los parámetros:

```
┌─────────────────────────────────────────────────────────────────┐
│              COMPARACIÓN DE PARÁMETROS (K=2 valores)            │
│                                                                 │
│   Posición    Sin Markov           Con Markov                   │
│   ────────    ──────────           ──────────                   │
│      3        P(X₃|X₁,X₂)          P(X₃|X₂)                     │
│               4 parámetros          2 parámetros                │
│                                                                 │
│      10       P(X₁₀|X₁,...,X₉)     P(X₁₀|X₉)                    │
│               512 parámetros        2 parámetros                │
│                                                                 │
│      784      P(X₇₈₄|X₁,...,X₇₈₃)  P(X₇₈₄|X₇₈₃)                │
│               2^783 parámetros      2 parámetros                │
│                                                                 │
│   ¡Markov hace posible trabajar con muchas variables!           │
└─────────────────────────────────────────────────────────────────┘
```

**Problema de Markov:** Es demasiado restrictivo para imágenes. El píxel 784 probablemente SÍ tiene relación con el píxel 1 (ambos podrían ser parte del fondo).

### 3.3 Trade-off: Simplificación vs Expresividad

```
┌─────────────────────────────────────────────────────────────────┐
│                         ESPECTRO DE MODELOS                     │
│                                                                 │
│   Independencia         Markov              Dependencia         │
│     Total              (cadena)              Completa           │
│                                                                 │
│  ────────────────────────────────────────────────────────────►  │
│                                                                 │
│  Menos parámetros                          Más parámetros       │
│  Menos expresivo                           Más expresivo        │
│  Fácil de estimar                          Difícil de estimar   │
│  "Olvida" relaciones                       Captura todo         │
│                                                                 │
│  Queremos algo en el MEDIO: que capture relaciones importantes  │
│  pero sin explotar en parámetros                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Variables Aleatorias Continuas

Hasta ahora hablamos de variables **discretas** (valores finitos como 0 o 1). Ahora pasamos a **continuas**.

### 4.1 De Discreto a Continuo

**Discreto:** Valores específicos, contables
```
P(X = 1) = 0.3
P(X = 2) = 0.5
P(X = 3) = 0.2
Puedo listar todos los valores y sus probabilidades
```

**Continuo:** Infinitos valores posibles (cualquier número real)
```
¿P(X = 1.234567...)? No tiene sentido preguntar por UN valor exacto
En cambio, preguntamos por RANGOS: P(1.2 < X < 1.3)
```

Para continuas, usamos **funciones de densidad de probabilidad** (PDF):
```
p(x) = función que indica qué tan "probable" es cada región
```

La probabilidad de un intervalo se calcula como el **área bajo la curva**:
```
P(a ≤ X ≤ b) = ∫ₐᵇ p(x) dx
```

### 4.2 Distribución Uniforme

La más simple: todos los valores en un intervalo [a, b] son igualmente probables.

```
         p(x)
          │
    1     │    ┌──────────────┐
   ───    │    │              │  ← Altura constante
   b-a    │    │              │
          │    │              │
          │────┴──────────────┴────► x
               a              b

p(x) = 1/(b-a)    si a ≤ x ≤ b
p(x) = 0          fuera del intervalo
```

**¿Por qué la altura es 1/(b-a)?** Porque el área total debe ser 1:
```
Área = base × altura = (b-a) × 1/(b-a) = 1 ✓
```

### 4.3 Distribución Normal (Gaussiana)

La más importante en estadística y machine learning. Tiene forma de "campana".

```
         p(x)
          │
          │         ╭───╮
          │        ╱     ╲       ← La mayoría de valores
          │       ╱       ╲        cerca de la media
          │      ╱         ╲
          │   __╱           ╲__  ← Pocos valores muy lejos
          │──────────────────────► x
                   μ

p(x) = (1 / (σ√(2π))) × exp(-(x-μ)² / (2σ²))
```

**Parámetros (solo 2 números definen toda la forma):**
- **μ (mu):** La media - dónde está el centro de la campana
- **σ (sigma):** La desviación estándar - qué tan "ancha" es la campana

```
┌─────────────────────────────────────────────────────────────────┐
│                   EFECTO DE LOS PARÁMETROS                      │
│                                                                 │
│   σ pequeño (σ=0.5)         σ grande (σ=2)                      │
│                                                                 │
│        │  ╱╲                      │   ╱────╲                    │
│        │ ╱  ╲                     │  ╱      ╲                   │
│        │╱    ╲                    │ ╱        ╲                  │
│   ─────┴──────┴─────         ────┴──────────┴────               │
│          μ                           μ                          │
│                                                                 │
│   Más concentrado            Más disperso                       │
│   "Más seguro" del valor     "Menos seguro" del valor           │
└─────────────────────────────────────────────────────────────────┘
```

**¿Por qué es tan importante?** Porque muchos fenómenos naturales siguen esta distribución (alturas, pesos, errores de medición). Y porque matemáticamente es muy conveniente para hacer cálculos.

### 4.4 Distribución Laplaciana

Similar a la Gaussiana pero con un "pico" más pronunciado (más puntiaguda).

```
         p(x)
          │
          │         /\
          │        /  \        ← Pico más agudo que Gaussiana
          │       /    \
          │      /      \
          │   __/        \__   ← Colas más "pesadas"
          │──────────────────► x
                   μ

p(x) = (1 / 2b) × exp(-|x-μ| / b)
```

**¿Cuándo se usa?** Cuando esperamos que la mayoría de valores estén MUY cerca de la media, pero ocasionalmente haya valores muy lejanos (outliers).

### 4.5 Propiedad Fundamental

Todas las distribuciones de probabilidad válidas cumplen:
```
∫_{-∞}^{+∞} p(x) dx = 1
```

El área total bajo la curva siempre es 1 (porque la probabilidad total es 100%).

---

## 5. Mezclas de Distribuciones

### 5.1 ¿Qué es una Mezcla?

A veces, los datos no siguen una sola distribución simple, sino una **combinación** de varias.

**Ejemplo: Peso de gatos**

Los gatos machos y hembras tienen pesos diferentes:
- Hembras: media ≈ 3.5 kg
- Machos: media ≈ 4.5 kg

Si miramos todos los gatos juntos SIN saber el sexo:

```
┌─────────────────────────────────────────────────────────────────┐
│                    MEZCLA DE GAUSSIANAS                         │
│                                                                 │
│   p(peso)                                                       │
│    │                                                            │
│    │       ╭──╮        ← Campana de hembras                     │
│    │      ╱    ╲        ╭──╮  ← Campana de machos               │
│    │     ╱      ╲      ╱    ╲                                   │
│    │    ╱        ╲    ╱      ╲                                  │
│    │___╱          ╲__╱        ╲___                              │
│    └────────────────────────────────► peso                      │
│            3.5kg      4.5kg                                     │
│          (hembras)   (machos)                                   │
│                                                                 │
│   Lo que vemos: DOS "montañas" (bimodal)                        │
│   Causa: son DOS poblaciones mezcladas                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Fórmula de la Mezcla

```
P(peso) = P(hembra) × P(peso|hembra) + P(macho) × P(peso|macho)
        = θ × N(peso; μ_h, σ_h) + (1-θ) × N(peso; μ_m, σ_m)
```

donde θ = proporción de hembras en la población.

**En general, para K componentes:**

```
P(X) = Σₖ θₖ × P(X | componente k)
```

donde:
- θₖ = probabilidad de pertenecer al componente k ("peso" de esa campana)
- Σₖ θₖ = 1 (los pesos suman 1)

### 5.3 Conexión con lo que Vimos

Esta fórmula es exactamente la **regla de la suma** que vimos antes:

```
P(X) = Σᵧ P(X,Y) = Σᵧ P(Y) × P(X|Y)
```

Es decir: la probabilidad marginal de X es un promedio ponderado de las condicionales.

**¿Por qué nos importa?** Porque en el mundo real, muchas distribuciones son mezclas:
- Imágenes de dígitos: mezcla de "distribución del 0", "distribución del 1", etc.
- Flores: mezcla de distribuciones de cada especie

---

## 6. La Cadena de Evolución: Del Problema a la Solución

Esta sección es el **MAPA MENTAL** que conecta todo. Cada solución resuelve un problema pero crea otro nuevo.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                    CADENA DE EVOLUCIÓN DE SOLUCIONES                        │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  PROBLEMA INICIAL                                                           │
│  ════════════════                                                           │
│  Queremos estimar P(imagen) para poder generar imágenes nuevas              │
│                                                                             │
│                              ▼                                              │
│                                                                             │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ INTENTO 1: Tabla Completa                                          │    │
│  │ ─────────────────────────                                          │    │
│  │ Idea: Guardar P(imagen) para cada imagen posible                   │    │
│  │                                                                    │    │
│  │ Problema: 2^784 ≈ 10^236 entradas. IMPOSIBLE.                      │    │
│  │           No hay suficientes átomos en el universo.                │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                              │                                              │
│                              ▼                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ INTENTO 2: Regla del Producto (Factorización)                      │    │
│  │ ─────────────────────────────────────────────                      │    │
│  │ Idea: P(x₁,...,xₙ) = P(x₁) × P(x₂|x₁) × P(x₃|x₁,x₂) × ...         │    │
│  │       Descomponer en producto de condicionales                     │    │
│  │                                                                    │    │
│  │ Ventaja: Ya no necesito UNA tabla gigante                          │    │
│  │                                                                    │    │
│  │ Problema: Cada condicional P(xᵢ|x₁,...,xᵢ₋₁) todavía es enorme    │    │
│  │           P(x₇₈₄|x₁,...,x₇₈₃) necesita 2^783 parámetros           │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                              │                                              │
│                              ▼                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ INTENTO 3: Independencia Total                                     │    │
│  │ ─────────────────────────────                                      │    │
│  │ Idea: Asumir que todos los píxeles son independientes              │    │
│  │       P(x₁,...,xₙ) = P(x₁) × P(x₂) × ... × P(xₙ)                   │    │
│  │                                                                    │    │
│  │ Ventaja: Solo necesito N parámetros (uno por píxel)                │    │
│  │                                                                    │    │
│  │ Problema: FALSO. Los píxeles NO son independientes.                │    │
│  │           Genera ruido aleatorio, no imágenes coherentes.          │    │
│  │           Si el píxel 1 es "ojo", el píxel 2 probablemente         │    │
│  │           también es parte del ojo.                                │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                              │                                              │
│                              ▼                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ INTENTO 4: Markov (Independencia Condicional)                      │    │
│  │ ─────────────────────────────────────────────                      │    │
│  │ Idea: Cada píxel solo depende del INMEDIATO anterior               │    │
│  │       P(xᵢ|x₁,...,xᵢ₋₁) = P(xᵢ|xᵢ₋₁)                              │    │
│  │                                                                    │    │
│  │ Ventaja: Solo 2 parámetros por condicional                         │    │
│  │                                                                    │    │
│  │ Problema: Demasiado restrictivo para imágenes.                     │    │
│  │           El píxel 784 SÍ puede depender del píxel 1.              │    │
│  │           Pierde relaciones de largo alcance.                      │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                              │                                              │
│                              ▼                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ ★ SOLUCIÓN HINTON: Aproximar con Redes Neuronales ★                │    │
│  │ ═══════════════════════════════════════════════════                │    │
│  │                                                                    │    │
│  │ Idea Genial: No asumir independencia NI usar tablas.               │    │
│  │              Usar un PERCEPTRÓN para APROXIMAR cada condicional.   │    │
│  │                                                                    │    │
│  │   P(xᵢ|x₁,...,xᵢ₋₁) ≈ σ(w₁x₁ + w₂x₂ + ... + wᵢ₋₁xᵢ₋₁ + b)        │    │
│  │                                                                    │    │
│  │ Ventajas:                                                          │    │
│  │   ✓ Solo i parámetros para la condicional i (crece linealmente)   │    │
│  │   ✓ Captura dependencias de TODOS los anteriores                  │    │
│  │   ✓ El perceptrón "aprende" las relaciones de los datos           │    │
│  │                                                                    │    │
│  │ Tradeoff: No es perfecto, es una APROXIMACIÓN.                     │    │
│  │           Pero funciona sorprendentemente bien.                    │    │
│  │                                                                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                              │                                              │
│                              ▼                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ MEJORAS POSTERIORES A HINTON                                       │    │
│  │ ────────────────────────────                                       │    │
│  │                                                                    │    │
│  │ NADE (Neural Autoregressive Density Estimator):                    │    │
│  │   - Comparte pesos entre las distintas condicionales               │    │
│  │   - Más eficiente en parámetros                                    │    │
│  │                                                                    │    │
│  │ MADE (Masked Autoencoder for Distribution Estimation):             │    │
│  │   - Usa "máscaras" para garantizar el orden autorregresivo         │    │
│  │   - Más fácil de implementar                                       │    │
│  │                                                                    │    │
│  │ PixelCNN / PixelRNN:                                               │    │
│  │   - Redes convolucionales/recurrentes                              │    │
│  │   - Capturan mejor la estructura espacial de imágenes              │    │
│  │                                                                    │    │
│  │ GPT (para texto):                                                  │    │
│  │   - Mismo principio autorregresivo                                 │    │
│  │   - Transformers en lugar de perceptrones                          │    │
│  │                                                                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│  RESUMEN DE LA EVOLUCIÓN:                                                   │
│                                                                             │
│  Tabla    →  Factorización  →  Independencia  →  Markov  →  Perceptrón    │
│  (10^236)    (aún grande)      (demasiado        (muy       (balance       │
│                                 simple)          restrictivo) perfecto!)   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Comparación de Parámetros

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   NÚMERO DE PARÁMETROS POR MÉTODO                           │
│                   (imagen 784 píxeles, binaria)                             │
│                                                                             │
│   Método                    Parámetros           ¿Viable?                   │
│   ───────────────────────   ──────────────────   ────────                   │
│   Tabla completa            2^784 ≈ 10^236       NO (infinito)              │
│   Independencia total       784                  SÍ pero malo               │
│   Markov orden 1            784 × 2 = 1,568      SÍ pero restrictivo        │
│   Perceptrón (Hinton)       784×785/2 ≈ 307,000  SÍ y expresivo            │
│   NADE (pesos compartidos)  ~500,000             SÍ y mejor                 │
│   PixelCNN                  ~1,000,000           SÍ y muy bueno             │
│                                                                             │
│   El perceptrón encuentra el BALANCE entre expresividad y tractabilidad    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Modelos Autorregresivos

### 7.1 La Idea Central

Un modelo **autorregresivo** genera datos **secuencialmente**, donde cada elemento depende de los anteriores.

**"Auto"** = a sí mismo
**"Regresivo"** = que vuelve atrás

Es decir: para generar el elemento actual, "miramos hacia atrás" a lo que ya generamos.

```
┌─────────────────────────────────────────────────────────────────┐
│                    GENERACIÓN AUTORREGRESIVA                    │
│                                                                 │
│   Paso 1: Generar X₁ (sin mirar nada)     → Sale X₁ = 1        │
│   Paso 2: Generar X₂ (mirando X₁)         → Sale X₂ = 0        │
│   Paso 3: Generar X₃ (mirando X₁,X₂)      → Sale X₃ = 1        │
│   ...                                                           │
│   Paso n: Generar Xₙ (mirando X₁,...,Xₙ₋₁) → Sale Xₙ = 0       │
│                                                                 │
│   Resultado final: [1, 0, 1, ..., 0]                            │
│                                                                 │
│   Cada paso USA lo que generamos antes                          │
└─────────────────────────────────────────────────────────────────┘
```

### 7.2 Aplicación a Imágenes

Para generar una imagen de N píxeles:

1. **Ordenamos** los píxeles: X₁, X₂, ..., Xₙ (ej: de izquierda a derecha, de arriba a abajo)
2. **Generamos** cada píxel condicionado a los anteriores

**Nota importante:** El orden es ARBITRARIO. Podríamos ir de derecha a izquierda, en espiral, etc. Lo importante es que sea CONSISTENTE durante entrenamiento y generación.

```
┌─────────────────────────────────────────────────────────────────┐
│              IMAGEN COMO SECUENCIA DE PÍXELES                   │
│                                                                 │
│   Imagen 3×3:                 Secuencia (orden de lectura):     │
│                                                                 │
│   ┌───┬───┬───┐                                                 │
│   │ 1 │ 2 │ 3 │               X₁ → X₂ → X₃                      │
│   ├───┼───┼───┤                         ↓                       │
│   │ 4 │ 5 │ 6 │               X₄ → X₅ → X₆                      │
│   ├───┼───┼───┤                         ↓                       │
│   │ 7 │ 8 │ 9 │               X₇ → X₈ → X₉                      │
│   └───┴───┴───┘                                                 │
│                                                                 │
│   P(imagen) = P(X₁)           ← Prior: sin contexto             │
│             × P(X₂|X₁)        ← Depende de 1 píxel              │
│             × P(X₃|X₁,X₂)     ← Depende de 2 píxeles            │
│             × P(X₄|X₁,X₂,X₃)  ← Depende de 3 píxeles            │
│             × ...                                               │
│             × P(X₉|X₁,...,X₈) ← Depende de 8 píxeles            │
│                                                                 │
│   Es la REGLA DEL PRODUCTO aplicada a píxeles                   │
└─────────────────────────────────────────────────────────────────┘
```

### 7.3 ¿Por Qué el Orden No Importa para la Probabilidad?

La probabilidad conjunta P(X₁, X₂, ..., Xₙ) es la misma sin importar el orden de factorización:

```
P(A, B, C) = P(A) × P(B|A) × P(C|A,B)     [orden A→B→C]
           = P(B) × P(A|B) × P(C|A,B)     [orden B→A→C]
           = P(C) × P(A|C) × P(B|A,C)     [orden C→A→B]
           = ... (todas dan el mismo resultado)
```

Por eso podemos elegir CUALQUIER orden para los píxeles. Elegimos de izquierda a derecha porque es natural, no porque sea matemáticamente necesario.

---

## 8. El Perceptrón como Estimador de Distribuciones

### 8.1 El Problema que Resuelve

Tenemos que estimar P(Xᵢ = 1 | X₁, X₂, ..., Xᵢ₋₁) para cada posición i.

**Sin perceptrón:** Necesitamos una tabla con 2^(i-1) entradas.
**Con perceptrón:** Usamos una función que "comprime" toda esa información.

### 8.2 Para Imágenes en Blanco y Negro

Si cada píxel es 0 o 1, la distribución de cada píxel es una **Bernoulli** con parámetro θ.

**Bernoulli:** Una distribución simple para eventos binarios.
```
P(X = 1) = θ
P(X = 0) = 1 - θ
```

**El truco de Hinton:** Un perceptrón con sigmoide nos da un valor entre 0 y 1. ¡Perfecto para ser θ!

```
┌─────────────────────────────────────────────────────────────────┐
│            PERCEPTRÓN COMO ESTIMADOR DE BERNOULLI               │
│                                                                 │
│   Entradas: X₁, X₂, ..., Xᵢ₋₁ (píxeles anteriores)             │
│                                                                 │
│   X₁ ──────┐                                                    │
│            │    ┌─────────────┐    ┌─────────┐                  │
│   X₂ ──────┼───►│ Σ wⱼxⱼ + b │───►│ σ(·)    │───► θᵢ          │
│            │    └─────────────┘    └─────────┘                  │
│   ...──────┤     (suma ponderada)   (sigmoide)   (probabilidad) │
│            │                                                    │
│   Xᵢ₋₁ ────┘                                                    │
│                                                                 │
│   θᵢ = σ(w₁X₁ + w₂X₂ + ... + wᵢ₋₁Xᵢ₋₁ + b)                     │
│                                                                 │
│   Donde σ(z) = 1/(1 + e^(-z)) "aplasta" cualquier número a (0,1)│
│                                                                 │
│   Interpretación:                                               │
│   P(Xᵢ = 1 | X₁,...,Xᵢ₋₁) = θᵢ                                  │
│   P(Xᵢ = 0 | X₁,...,Xᵢ₋₁) = 1 - θᵢ                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 8.3 ¿Por Qué Funciona?

El perceptrón aprende a detectar patrones:

```
Ejemplo intuitivo (muy simplificado):

Si los píxeles 1, 2, 3 son blancos (parte de un borde),
probablemente el píxel 4 también sea blanco.

El perceptrón aprende pesos como:
  w₁ = 0.8  (si píxel 1 es blanco, aumenta prob. de píxel 4)
  w₂ = 0.7  (si píxel 2 es blanco, aumenta prob. de píxel 4)
  w₃ = 0.6  (si píxel 3 es blanco, aumenta prob. de píxel 4)
  b = -1.5  (sesgo base)

Si X₁=1, X₂=1, X₃=1:
  z = 0.8×1 + 0.7×1 + 0.6×1 - 1.5 = 0.6
  θ₄ = σ(0.6) ≈ 0.65  (65% prob. de ser blanco)

Si X₁=0, X₂=0, X₃=0:
  z = 0.8×0 + 0.7×0 + 0.6×0 - 1.5 = -1.5
  θ₄ = σ(-1.5) ≈ 0.18  (18% prob. de ser blanco)
```

### 8.4 Reducción de Parámetros

```
┌─────────────────────────────────────────────────────────────────┐
│               COMPARACIÓN DE PARÁMETROS                         │
│                                                                 │
│   Para estimar P(Xᵢ | X₁,...,Xᵢ₋₁):                            │
│                                                                 │
│   Con tabla:                                                    │
│   ──────────                                                    │
│   Necesito un número por cada combinación de X₁,...,Xᵢ₋₁       │
│   = 2^(i-1) parámetros                                          │
│                                                                 │
│   Con perceptrón:                                               │
│   ────────────────                                              │
│   Necesito un peso wⱼ por cada entrada + un bias               │
│   = i parámetros (i-1 pesos + 1 bias)                           │
│                                                                 │
│   Posición    Tabla         Perceptrón     Ahorro               │
│   ────────    ─────         ──────────     ──────               │
│      2          2               2          Igual                │
│      3          4               3          25%                  │
│      5         16               5          69%                  │
│     10        512              10          98%                  │
│    100       10^30            100          99.99999...%         │
│    784      10^236            784          ∞                    │
│                                                                 │
│   ¡El perceptrón hace POSIBLE trabajar con imágenes!            │
└─────────────────────────────────────────────────────────────────┘
```

### 8.5 Red de Hinton: Todos los Perceptrones en Una Matriz

En lugar de tener perceptrones separados para cada posición, Hinton propuso juntarlos en una sola red con una **matriz triangular inferior**:

```
┌─────────────────────────────────────────────────────────────────┐
│                    RED DE HINTON (NADE-like)                    │
│                                                                 │
│   Entrada: [X₁, X₂, X₃, ..., Xₙ] (toda la imagen)               │
│   Salida:  [P₁, P₂, P₃, ..., Pₙ] (probabilidad de cada píxel)   │
│                                                                 │
│   Matriz de pesos W (triangular inferior):                      │
│                                                                 │
│        X₁   X₂   X₃   X₄                                        │
│   P₁ [  0    0    0    0  ]   ← P₁ no ve nada (solo bias)       │
│   P₂ [ w₂₁  0    0    0  ]   ← P₂ solo ve X₁                    │
│   P₃ [ w₃₁ w₃₂  0    0  ]   ← P₃ ve X₁ y X₂                    │
│   P₄ [ w₄₁ w₄₂ w₄₃  0  ]   ← P₄ ve X₁, X₂, X₃                 │
│                                                                 │
│   ¿Por qué ceros arriba de la diagonal?                         │
│   ──────────────────────────────────────                        │
│   Para que P₃ NO pueda ver X₃ ni X₄.                            │
│   Solo puede ver X₁ y X₂ (los ANTERIORES).                      │
│   Esto GARANTIZA la estructura autorregresiva.                  │
│                                                                 │
│   Operación:                                                    │
│   P = σ(W × X + b)                                              │
│   Una sola multiplicación matricial nos da TODAS las P          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**¿Por qué es útil esta estructura matricial?** Porque permite calcular TODAS las probabilidades de una vez durante el entrenamiento (ver siguiente sección).

---

## 9. Por Qué Entrenar es Paralelo pero Generar es Secuencial

Esta es una distinción **CRUCIAL** que confunde a muchos estudiantes.

### 9.1 La Diferencia Fundamental

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   ENTRENAMIENTO: Tenemos la imagen COMPLETA                     │
│   ════════════════════════════════════════                      │
│                                                                 │
│   Datos de entrada: [X₁=1, X₂=0, X₃=1, X₄=1, ...]              │
│                      ↑    ↑    ↑    ↑                           │
│                      │    │    │    │                           │
│                      CONOCIDOS (vienen del dataset)             │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   GENERACIÓN: NO tenemos la imagen, la estamos CREANDO          │
│   ═══════════════════════════════════════════════════           │
│                                                                 │
│   Paso 1: [X₁=?, ?, ?, ?, ...]  → Generar X₁                   │
│   Paso 2: [X₁=1, X₂=?, ?, ?, ...]  → Generar X₂ usando X₁      │
│   Paso 3: [X₁=1, X₂=0, X₃=?, ?, ...]  → Generar X₃ usando X₁,X₂│
│   ...                                                           │
│                                                                 │
│   Cada paso NECESITA el resultado del paso anterior             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 9.2 Por Qué Podemos Entrenar en Paralelo

Durante el entrenamiento, ya tenemos la imagen real del dataset. Todos los valores X₁, X₂, ... son **CONOCIDOS**.

```
┌─────────────────────────────────────────────────────────────────┐
│                    ENTRENAMIENTO (PARALELO)                     │
│                                                                 │
│   Imagen real del dataset: [1, 0, 1, 1, 0, 1, 0, 0, 1]         │
│                             ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓          │
│                                                                 │
│   Paso 1 - Calcular probabilidades (TODO A LA VEZ):             │
│                                                                 │
│   P₁ = σ(b₁)                        = 0.6  (predice 1)         │
│   P₂ = σ(w₂₁×1 + b₂)               = 0.3  (predice 0)         │
│   P₃ = σ(w₃₁×1 + w₃₂×0 + b₃)       = 0.7  (predice 1)         │
│   P₄ = σ(w₄₁×1 + w₄₂×0 + w₄₃×1 + b₄) = 0.8  (predice 1)       │
│   ...                                                           │
│        ↑                                                        │
│        │                                                        │
│   PUEDO calcular P₄ porque YA SÉ que X₁=1, X₂=0, X₃=1          │
│   No necesito esperar a "generar" X₁, X₂, X₃                    │
│                                                                 │
│   Paso 2 - Comparar con la realidad y calcular pérdida:         │
│                                                                 │
│   Real: [1,   0,   1,   1,  ...]                                │
│   Pred: [0.6, 0.3, 0.7, 0.8, ...]                               │
│   Loss: BCE(1, 0.6) + BCE(0, 0.3) + BCE(1, 0.7) + BCE(1, 0.8)   │
│                                                                 │
│   TODO se calcula en paralelo con multiplicación matricial      │
└─────────────────────────────────────────────────────────────────┘
```

**La clave:** Para calcular P₄, necesito conocer X₁, X₂, X₃. Durante el entrenamiento, ¡YA LOS CONOZCO! Están en el dataset.

### 9.3 Por Qué Debemos Generar Secuencialmente

Durante la generación, NO tenemos la imagen. La estamos **creando** de la nada.

```
┌─────────────────────────────────────────────────────────────────┐
│                    GENERACIÓN (SECUENCIAL)                      │
│                                                                 │
│   Estado inicial: [?, ?, ?, ?, ?, ?, ?, ?, ?]                  │
│                    No sabemos NINGÚN valor                      │
│                                                                 │
│   Paso 1: Calcular P₁                                           │
│   ─────────────────────                                         │
│   P₁ = σ(b₁) = 0.6                                              │
│   Muestrear: random() < 0.6? → Sí → X₁ = 1                     │
│                                                                 │
│   Estado: [1, ?, ?, ?, ?, ?, ?, ?, ?]                          │
│                                                                 │
│   Paso 2: Calcular P₂ (necesito X₁)                            │
│   ────────────────────────────────                              │
│   P₂ = σ(w₂₁×1 + b₂) = 0.3                                     │
│                  ↑                                              │
│                  └─ NECESITO saber que X₁=1                     │
│                     Si no hubiera generado X₁, no podría        │
│   Muestrear: random() < 0.3? → No → X₂ = 0                     │
│                                                                 │
│   Estado: [1, 0, ?, ?, ?, ?, ?, ?, ?]                          │
│                                                                 │
│   Paso 3: Calcular P₃ (necesito X₁ y X₂)                       │
│   ──────────────────────────────────────                        │
│   P₃ = σ(w₃₁×1 + w₃₂×0 + b₃) = 0.7                             │
│                  ↑       ↑                                      │
│                  └───────┴─ NECESITO X₁ y X₂                    │
│   Muestrear: random() < 0.7? → Sí → X₃ = 1                     │
│                                                                 │
│   Estado: [1, 0, 1, ?, ?, ?, ?, ?, ?]                          │
│                                                                 │
│   ... y así sucesivamente hasta completar la imagen             │
│                                                                 │
│   ═══════════════════════════════════════════════════════════   │
│   CADA PASO DEPENDE DEL RESULTADO DEL PASO ANTERIOR            │
│   Por eso NO se puede paralelizar                               │
│   ═══════════════════════════════════════════════════════════   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 9.4 Resumen de la Diferencia

```
┌─────────────────────────────────────────────────────────────────┐
│                    ENTRENAMIENTO VS GENERACIÓN                  │
│                                                                 │
│             ENTRENAMIENTO              GENERACIÓN               │
│             ═════════════              ══════════               │
│                                                                 │
│   Entrada   Imagen REAL completa       NADA (creamos desde 0)   │
│                                                                 │
│   X₁,X₂...  CONOCIDOS (del dataset)    DESCONOCIDOS (a crear)   │
│                                                                 │
│   Cálculo   PARALELO (una pasada)      SECUENCIAL (n pasos)     │
│             P = σ(W×X + b)             P₁→X₁→P₂→X₂→...→Pₙ→Xₙ   │
│                                                                 │
│   Tiempo    Rápido (matrices)          Lento (loop)             │
│                                                                 │
│   ¿Por qué? Todos los X son INPUT      Cada X es OUTPUT del     │
│             (ya existen)               paso anterior            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 9.5 Analogía: Escribir vs Leer

**Leer un libro (entrenamiento):**
- El libro ya está escrito
- Puedes leer cualquier página sin leer las anteriores
- Puedes leer varias páginas "a la vez" (en paralelo)

**Escribir un libro (generación):**
- El libro no existe, lo estás creando
- Para escribir la página 5, necesitas saber qué pasó en las páginas 1-4
- No puedes escribir la página 100 antes de escribir la página 1

---

## 10. Entrenamiento: De KL Divergence a BCE

### 10.1 ¿Qué Queremos Lograr?

Queremos que nuestra distribución estimada P_θ(x) se **parezca** a la distribución real P_data(x).

**Pregunta:** ¿Cómo medimos si dos distribuciones se "parecen"?

### 10.2 KL Divergence: Midiendo la Diferencia

La **divergencia de Kullback-Leibler** mide qué tan diferentes son dos distribuciones:

```
KL(P_data || P_θ) = E_P_data[log(P_data(x)) - log(P_θ(x))]
                  = E_P_data[log(P_data(x)/P_θ(x))]
```

**Propiedades:**
- KL ≥ 0 siempre (nunca negativo)
- KL = 0 **solo** cuando P_data = P_θ (distribuciones idénticas)
- No es simétrica: KL(P||Q) ≠ KL(Q||P)

**Interpretación intuitiva:** Mide cuánta "información" perdemos si usamos P_θ para aproximar P_data.

### 10.3 ¿Por Qué KL se Simplifica?

Cuando minimizamos KL respecto a los parámetros θ:

```
KL(P_data || P_θ) = E_P_data[log(P_data(x))] - E_P_data[log(P_θ(x))]
                    ────────────────────────   ──────────────────────
                     Este término es CONSTANTE   Este término depende de θ
                     (no depende de θ)
```

**Conclusión:** Minimizar KL es equivalente a minimizar:

```
min_θ E_P_data[-log(P_θ(x))]
```

### 10.4 De Esperanza a Promedio

No conocemos P_data exactamente, pero tenemos **muestras** de ella (nuestro dataset).

**Aproximación:** Reemplazamos la esperanza por un promedio sobre los datos:

```
E_P_data[-log(P_θ(x))] ≈ (1/N) Σᵢ -log(P_θ(xᵢ))
```

Esto se llama **Negative Log-Likelihood (NLL)** o **Maximum Likelihood Estimation (MLE)**.

### 10.5 Aplicando a Modelos Autorregresivos

Para un modelo autorregresivo, P_θ(x) es un producto de condicionales:

```
P_θ(x) = ∏ᵢ P_θ(Xᵢ | X₁,...,Xᵢ₋₁)
```

Aplicando logaritmo:

```
log(P_θ(x)) = log(∏ᵢ P_θ(Xᵢ|...))
            = Σᵢ log(P_θ(Xᵢ|...))    ← Logaritmo de producto = suma de logs
```

Entonces:

```
-log(P_θ(x)) = -Σᵢ log(P_θ(Xᵢ|...))
             = Σᵢ -log(P_θ(Xᵢ|...))
```

### 10.6 ¿Por Qué Usamos Logaritmo?

**Razón matemática:** Convierte productos en sumas (más fácil de calcular).

**Razón numérica (MUY IMPORTANTE):** Evita problemas de underflow.

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROBLEMA DE UNDERFLOW                        │
│                                                                 │
│   P(imagen) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂) × ...             │
│                                                                 │
│   Supongamos que cada probabilidad es ≈ 0.5                     │
│   Para 784 píxeles:                                             │
│                                                                 │
│   P(imagen) ≈ 0.5^784 ≈ 10^(-236)                               │
│                                                                 │
│   ¡La computadora NO puede representar números tan pequeños!    │
│   El mínimo float de 64 bits es ≈ 10^(-308)                     │
│   Pero con 784 multiplicaciones, acumulamos error.              │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   SOLUCIÓN: Usar logaritmos                                     │
│                                                                 │
│   log P(imagen) = log P(X₁) + log P(X₂|X₁) + ...               │
│                 ≈ 784 × log(0.5)                                │
│                 ≈ 784 × (-0.693)                                │
│                 ≈ -543                                          │
│                                                                 │
│   ¡-543 es un número perfectamente manejable!                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 10.7 El Problema del Perceptrón

El perceptrón nos da:
```
σ(...) = P(Xᵢ = 1 | X₁,...,Xᵢ₋₁)
```

Pero necesitamos:
```
P(Xᵢ = xᵢ | X₁,...,Xᵢ₋₁)  donde xᵢ puede ser 0 o 1
```

**El problema:** El perceptrón SIEMPRE nos da la probabilidad de ser 1, pero a veces el píxel real es 0.

### 10.8 Solución: Binary Cross-Entropy (BCE)

La BCE resuelve este problema:

```
BCE(xᵢ, pᵢ) = -xᵢ × log(pᵢ) - (1-xᵢ) × log(1-pᵢ)
```

donde:
- xᵢ = valor real del píxel (0 o 1) - viene del dataset
- pᵢ = salida del perceptrón (probabilidad de ser 1)

**¿Cómo funciona?**

```
┌─────────────────────────────────────────────────────────────────┐
│                    CÓMO FUNCIONA BCE                            │
│                                                                 │
│   BCE actúa como un "SELECTOR" automático                       │
│                                                                 │
│   Caso 1: El píxel real es 1 (xᵢ = 1)                          │
│   ─────────────────────────────────────                        │
│   BCE = -1×log(pᵢ) - 0×log(1-pᵢ)                               │
│       = -log(pᵢ)                                                │
│                ↑                                                 │
│       Si pᵢ ≈ 1: -log(1) ≈ 0     (pérdida baja, bien!)         │
│       Si pᵢ ≈ 0: -log(0) → ∞     (pérdida alta, mal!)          │
│                                                                 │
│   → El modelo aprende a predecir pᵢ alto cuando xᵢ=1           │
│                                                                 │
│   ─────────────────────────────────────────────────────────     │
│                                                                 │
│   Caso 2: El píxel real es 0 (xᵢ = 0)                          │
│   ─────────────────────────────────────                        │
│   BCE = -0×log(pᵢ) - 1×log(1-pᵢ)                               │
│       = -log(1-pᵢ)                                              │
│                  ↑                                               │
│       Si pᵢ ≈ 0: -log(1) ≈ 0     (pérdida baja, bien!)         │
│       Si pᵢ ≈ 1: -log(0) → ∞     (pérdida alta, mal!)          │
│                                                                 │
│   → El modelo aprende a predecir pᵢ bajo cuando xᵢ=0           │
│                                                                 │
│   ═══════════════════════════════════════════════════════════   │
│   BCE = -log(P(Xᵢ = xᵢ | ...))                                  │
│   Es exactamente el negative log-likelihood que queríamos!      │
│   ═══════════════════════════════════════════════════════════   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 10.9 La Pérdida Completa

Para una imagen completa:

```
L(θ) = Σ_píxeles BCE(xᵢ, pᵢ)
     = Σᵢ [-xᵢ log(pᵢ) - (1-xᵢ) log(1-pᵢ)]
```

Para todo el dataset:

```
J(θ) = (1/N) Σ_imágenes Σ_píxeles BCE(xᵢ, pᵢ)
```

Esta es la función que minimizamos con gradient descent.

### 10.10 Conexión Completa

```
┌─────────────────────────────────────────────────────────────────┐
│              CADENA DE EQUIVALENCIAS                            │
│                                                                 │
│   Minimizar KL(P_data || P_θ)                                   │
│         ↓  (eliminar término constante)                         │
│   Minimizar E[-log P_θ(x)]                                      │
│         ↓  (aproximar esperanza con promedio)                   │
│   Minimizar (1/N) Σ -log P_θ(xᵢ)                               │
│         ↓  (usar regla del producto)                            │
│   Minimizar (1/N) Σ Σⱼ -log P_θ(xᵢⱼ|anteriores)                │
│         ↓  (para Bernoulli con perceptrón)                      │
│   Minimizar (1/N) Σ Σⱼ BCE(xᵢⱼ, pᵢⱼ)                           │
│                                                                 │
│   TODO es equivalente. BCE viene de KL divergence.              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 11. El Proceso Completo: Del Dato a la Generación

### 11.1 Visión General

```
┌─────────────────────────────────────────────────────────────────┐
│              PROCESO COMPLETO DE MODELADO GENERATIVO            │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                    FASE 1: DATOS                        │   │
│   │                                                         │   │
│   │   Tenemos un dataset de imágenes reales                 │   │
│   │   Ejemplo: 60,000 imágenes de dígitos MNIST             │   │
│   │   Cada imagen: 28×28 = 784 píxeles                      │   │
│   │                                                         │   │
│   │   Objetivo: Aprender P_data(imagen)                     │   │
│   │                                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                             ↓                                   │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                  FASE 2: MODELADO                       │   │
│   │                                                         │   │
│   │   Decisión: Usar modelo autorregresivo                  │   │
│   │                                                         │   │
│   │   P(imagen) = P(X₁) × P(X₂|X₁) × ... × P(X₇₈₄|...)     │   │
│   │                                                         │   │
│   │   Cada condicional: un perceptrón                       │   │
│   │   P(Xᵢ=1|...) = σ(Σⱼ wᵢⱼxⱼ + bᵢ)                       │   │
│   │                                                         │   │
│   │   Arquitectura: matriz triangular inferior W + bias b   │   │
│   │                                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                             ↓                                   │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                FASE 3: ENTRENAMIENTO                    │   │
│   │                                                         │   │
│   │   Para cada imagen del dataset:                         │   │
│   │   1. Forward pass: P = σ(W×X + b)                       │   │
│   │   2. Calcular pérdida: L = Σ BCE(xᵢ, pᵢ)               │   │
│   │   3. Backward pass: calcular gradientes                 │   │
│   │   4. Actualizar: W ← W - lr×∂L/∂W                       │   │
│   │                                                         │   │
│   │   Repetir muchas épocas hasta convergencia              │   │
│   │                                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                             ↓                                   │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                 FASE 4: GENERACIÓN                      │   │
│   │                                                         │   │
│   │   Para crear una nueva imagen:                          │   │
│   │   1. p₁ = σ(b₁), x₁ = muestrear(p₁)                    │   │
│   │   2. p₂ = σ(w₂₁x₁ + b₂), x₂ = muestrear(p₂)           │   │
│   │   3. p₃ = σ(w₃₁x₁ + w₃₂x₂ + b₃), x₃ = muestrear(p₃)   │   │
│   │   ... (784 pasos)                                       │   │
│   │                                                         │   │
│   │   Resultado: ¡imagen nueva que parece real!             │   │
│   │                                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 11.2 Algoritmo de Entrenamiento (Detallado)

```
┌─────────────────────────────────────────────────────────────────┐
│                  ALGORITMO DE ENTRENAMIENTO                     │
│                                                                 │
│   ENTRADA: Dataset D = {imagen₁, imagen₂, ..., imagenₙ}         │
│   SALIDA:  Parámetros entrenados W, b                           │
│                                                                 │
│   1. Inicializar W (triangular inferior) y b aleatoriamente    │
│                                                                 │
│   2. Para cada época = 1, 2, ..., num_epochs:                   │
│      │                                                          │
│      │  Para cada imagen x en D:                                │
│      │  │                                                       │
│      │  │  // FORWARD PASS (paralelo)                          │
│      │  │  z = W × x + b           // combinación lineal       │
│      │  │  p = σ(z)                 // aplicar sigmoide        │
│      │  │                                                       │
│      │  │  // CALCULAR PÉRDIDA                                 │
│      │  │  L = Σᵢ BCE(xᵢ, pᵢ)      // suma sobre píxeles      │
│      │  │                                                       │
│      │  │  // BACKWARD PASS                                    │
│      │  │  ∂L/∂W = backprop(L)     // gradientes automáticos  │
│      │  │  ∂L/∂b = backprop(L)                                 │
│      │  │                                                       │
│      │  │  // ACTUALIZAR PARÁMETROS                            │
│      │  │  W = W - lr × ∂L/∂W      // gradient descent         │
│      │  │  b = b - lr × ∂L/∂b                                  │
│      │  │                                                       │
│      │  └──────────────────────────────────────────────────    │
│      │                                                          │
│      │  Imprimir pérdida promedio de la época                   │
│      │                                                          │
│      └──────────────────────────────────────────────────────    │
│                                                                 │
│   3. Retornar W, b                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 11.3 Algoritmo de Generación (Detallado)

**¿Qué tenemos disponible para generar?**

Después del entrenamiento, tenemos:
- **W** (matriz de pesos): números que aprendió el modelo mirando miles de imágenes reales
- **b** (vector de bias): un número por cada píxel

Estos W y b codifican TODO lo que el modelo "sabe" sobre cómo lucen las imágenes reales.

**¿Cuál es el objetivo?**

Crear una imagen NUEVA (que nunca existió) pero que se vea como las imágenes de entrenamiento.

---

#### PASO 1: Generar el primer píxel (x₁)

```
┌─────────────────────────────────────────────────────────────────┐
│   GENERAR x₁ (primer píxel)                                     │
│                                                                 │
│   Problema: No hay píxeles anteriores para mirar.               │
│   Solución: Usar solo el bias b₁                                │
│                                                                 │
│   Paso 1.1: Calcular la probabilidad de que x₁ sea 1            │
│   ─────────────────────────────────────────────────             │
│                                                                 │
│      p₁ = σ(b₁)                                                 │
│                                                                 │
│      Ejemplo numérico:                                          │
│      - Si b₁ = 0.5 (valor que aprendió el modelo)               │
│      - σ(0.5) = 1/(1+e^(-0.5)) = 1/(1+0.606) = 0.622            │
│      - p₁ = 0.622                                               │
│                                                                 │
│      Esto significa: "hay 62.2% de probabilidad de que          │
│      el primer píxel sea blanco (1)"                            │
│                                                                 │
│   Paso 1.2: Lanzar una "moneda cargada"                         │
│   ─────────────────────────────────────────────────             │
│                                                                 │
│      u = random()   ← número aleatorio entre 0 y 1              │
│                                                                 │
│      Ejemplo: la computadora genera u = 0.35                    │
│                                                                 │
│   Paso 1.3: Decidir el valor del píxel                          │
│   ─────────────────────────────────────────────────             │
│                                                                 │
│      if u < p₁:     ← ¿0.35 < 0.622? SÍ                         │
│         x₁ = 1      ← el primer píxel es BLANCO                 │
│      else:                                                      │
│         x₁ = 0                                                  │
│                                                                 │
│   Resultado: x = [1]   (tenemos el primer píxel)                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**¿Por qué funciona el paso 1.3?**

Si p₁ = 0.622, entonces:
- Cualquier u entre 0.000 y 0.622 → x₁ = 1 (62.2% de los casos)
- Cualquier u entre 0.622 y 1.000 → x₁ = 0 (37.8% de los casos)

Como `random()` genera números uniformemente distribuidos entre 0 y 1:
- La probabilidad de que u < 0.622 es exactamente 62.2%

Esto es lo que significa **muestrear de una distribución Bernoulli**.

---

#### PASO 2: Generar el segundo píxel (x₂)

```
┌─────────────────────────────────────────────────────────────────┐
│   GENERAR x₂ (segundo píxel)                                    │
│                                                                 │
│   Ahora SÍ tenemos un píxel anterior: x₁ = 1                    │
│                                                                 │
│   Paso 2.1: Calcular la probabilidad                            │
│   ─────────────────────────────────────────────────             │
│                                                                 │
│      p₂ = σ(w₂₁ × x₁ + b₂)                                      │
│             ↑     ↑    ↑                                        │
│             │     │    └── bias del píxel 2 (aprendido)         │
│             │     └─────── valor del píxel 1 que generamos (1)  │
│             └───────────── peso de conexión 1→2 (aprendido)     │
│                                                                 │
│      Ejemplo numérico:                                          │
│      - w₂₁ = 1.2 (el modelo aprendió que si x₁=1,               │
│                   entonces x₂ probablemente también es 1)       │
│      - x₁ = 1 (lo que generamos en el paso anterior)            │
│      - b₂ = -0.3                                                │
│                                                                 │
│      Cálculo:                                                   │
│      z = w₂₁ × x₁ + b₂                                          │
│      z = 1.2 × 1 + (-0.3)                                       │
│      z = 1.2 - 0.3                                              │
│      z = 0.9                                                    │
│                                                                 │
│      p₂ = σ(0.9) = 1/(1+e^(-0.9)) = 0.711                       │
│                                                                 │
│      Interpretación: "dado que x₁=1, hay 71.1% de               │
│      probabilidad de que x₂ también sea 1"                      │
│                                                                 │
│   Paso 2.2: Lanzar moneda cargada                               │
│   ─────────────────────────────────────────────────             │
│                                                                 │
│      u = random() = 0.82 (ejemplo)                              │
│                                                                 │
│   Paso 2.3: Decidir                                             │
│   ─────────────────────────────────────────────────             │
│                                                                 │
│      if u < p₂:     ← ¿0.82 < 0.711? NO                         │
│         x₂ = 1                                                  │
│      else:                                                      │
│         x₂ = 0      ← el segundo píxel es NEGRO                 │
│                                                                 │
│   Resultado: x = [1, 0]   (tenemos dos píxeles)                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Observación importante:** Aunque la probabilidad de x₂=1 era alta (71.1%), el número aleatorio cayó en el 28.9% donde x₂=0. Esto es normal y es lo que hace que cada imagen generada sea diferente.

---

#### PASO 3: Generar el tercer píxel (x₃)

```
┌─────────────────────────────────────────────────────────────────┐
│   GENERAR x₃ (tercer píxel)                                     │
│                                                                 │
│   Ahora tenemos DOS píxeles anteriores: x₁=1, x₂=0              │
│                                                                 │
│   Paso 3.1: Calcular la probabilidad                            │
│   ─────────────────────────────────────────────────             │
│                                                                 │
│      p₃ = σ(w₃₁ × x₁ + w₃₂ × x₂ + b₃)                           │
│             ↑          ↑          ↑                             │
│             │          │          └── bias del píxel 3          │
│             │          └───────────── contribución de x₂        │
│             └──────────────────────── contribución de x₁        │
│                                                                 │
│      Ejemplo numérico:                                          │
│      - w₃₁ = 0.8, w₃₂ = -1.5, b₃ = 0.2                          │
│      - x₁ = 1, x₂ = 0                                           │
│                                                                 │
│      Cálculo:                                                   │
│      z = w₃₁ × x₁ + w₃₂ × x₂ + b₃                               │
│      z = 0.8 × 1 + (-1.5) × 0 + 0.2                             │
│      z = 0.8 + 0 + 0.2                                          │
│      z = 1.0                                                    │
│                                                                 │
│      p₃ = σ(1.0) = 0.731                                        │
│                                                                 │
│      NOTA: El término w₃₂ × x₂ = -1.5 × 0 = 0                   │
│      Cuando un píxel anterior es 0, su peso NO contribuye.      │
│      Solo los píxeles que son 1 "votan" en la decisión.         │
│                                                                 │
│   Paso 3.2 y 3.3: (igual que antes)                             │
│   ─────────────────────────────────────────────────             │
│                                                                 │
│      u = random() = 0.45                                        │
│      ¿0.45 < 0.731? SÍ → x₃ = 1                                 │
│                                                                 │
│   Resultado: x = [1, 0, 1]   (tenemos tres píxeles)             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

#### PASO GENERAL: Generar el píxel i-ésimo (xᵢ)

```
┌─────────────────────────────────────────────────────────────────┐
│   GENERAR xᵢ (cualquier píxel después del primero)              │
│                                                                 │
│   Tenemos: x₁, x₂, ..., xᵢ₋₁ (todos los anteriores)            │
│                                                                 │
│   FÓRMULA GENERAL:                                              │
│   ────────────────                                              │
│                                                                 │
│      pᵢ = σ( Σⱼ₌₁ⁱ⁻¹ wᵢⱼ × xⱼ + bᵢ )                           │
│                                                                 │
│      Esto significa:                                            │
│                                                                 │
│      z = wᵢ₁×x₁ + wᵢ₂×x₂ + wᵢ₃×x₃ + ... + wᵢ,ᵢ₋₁×xᵢ₋₁ + bᵢ    │
│          └─────────────────────────────────────────────────┘    │
│                    suma de todas las contribuciones             │
│                    de los píxeles anteriores                    │
│                                                                 │
│      pᵢ = σ(z) = 1/(1+e^(-z))                                   │
│                                                                 │
│   MUESTREO:                                                     │
│   ─────────                                                     │
│      u = random()                                               │
│      xᵢ = 1  si u < pᵢ                                          │
│      xᵢ = 0  si u ≥ pᵢ                                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

#### RESUMEN: El loop completo de generación

```
┌─────────────────────────────────────────────────────────────────┐
│   ALGORITMO COMPLETO                                            │
│                                                                 │
│   Para una imagen de n=784 píxeles (MNIST 28×28):               │
│                                                                 │
│   x = []                          // imagen vacía               │
│                                                                 │
│   // Píxel 1                                                    │
│   p₁ = σ(b₁)                      // solo bias                  │
│   x₁ = Bernoulli(p₁)              // 0 o 1                      │
│   x = [x₁]                                                      │
│                                                                 │
│   // Píxel 2                                                    │
│   p₂ = σ(w₂₁×x₁ + b₂)                                           │
│   x₂ = Bernoulli(p₂)                                            │
│   x = [x₁, x₂]                                                  │
│                                                                 │
│   // Píxel 3                                                    │
│   p₃ = σ(w₃₁×x₁ + w₃₂×x₂ + b₃)                                  │
│   x₃ = Bernoulli(p₃)                                            │
│   x = [x₁, x₂, x₃]                                              │
│                                                                 │
│   // ... continúa hasta ...                                     │
│                                                                 │
│   // Píxel 784                                                  │
│   p₇₈₄ = σ(w₇₈₄,₁×x₁ + w₇₈₄,₂×x₂ + ... + w₇₈₄,₇₈₃×x₇₈₃ + b₇₈₄) │
│   x₇₈₄ = Bernoulli(p₇₈₄)                                        │
│   x = [x₁, x₂, ..., x₇₈₄]        // ¡IMAGEN COMPLETA!           │
│                                                                 │
│   Retornar x                                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

#### ¿Por qué NO se puede paralelizar?

```
┌─────────────────────────────────────────────────────────────────┐
│   EL PROBLEMA DE LA SECUENCIALIDAD                              │
│                                                                 │
│   Para calcular p₃, necesito x₂.                                │
│   Pero x₂ no existe hasta que lo genero.                        │
│   Y para generar x₂, necesito p₂.                               │
│   Y para p₂, necesito x₁.                                       │
│                                                                 │
│   Cadena de dependencias:                                       │
│                                                                 │
│   p₁ → x₁ → p₂ → x₂ → p₃ → x₃ → p₄ → x₄ → ...                  │
│                                                                 │
│   CADA PASO DEPENDE DEL ANTERIOR                                │
│                                                                 │
│   Para MNIST (784 píxeles):                                     │
│   - Necesitas hacer 784 pasos secuenciales                      │
│   - No puedes calcular x₅₀₀ sin haber calculado x₁ a x₄₉₉       │
│   - Esto hace la GENERACIÓN lenta                               │
│                                                                 │
│   (El ENTRENAMIENTO sí se puede paralelizar porque ahí          │
│   los valores de x ya existen - son las imágenes reales)        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

#### Ejemplo visual: Generando una mini-imagen de 4 píxeles

```
┌─────────────────────────────────────────────────────────────────┐
│   EJEMPLO COMPLETO: Imagen de 2×2 = 4 píxeles                   │
│                                                                 │
│   Imagen real (de entrenamiento):    Orden de píxeles:          │
│   ┌───┬───┐                          ┌───┬───┐                  │
│   │ 1 │ 1 │                          │ 1 │ 2 │                  │
│   ├───┼───┤                          ├───┼───┤                  │
│   │ 0 │ 1 │                          │ 3 │ 4 │                  │
│   └───┴───┘                          └───┴───┘                  │
│                                                                 │
│   Parámetros aprendidos (ejemplo simplificado):                 │
│   b = [0.5, 0.3, -0.8, 0.1]                                     │
│   W = matriz triangular inferior (ver sección 0.2)              │
│                                                                 │
│   ═══════════════════════════════════════════════════════════   │
│   GENERACIÓN PASO A PASO:                                       │
│   ═══════════════════════════════════════════════════════════   │
│                                                                 │
│   PASO 1: x₁                                                    │
│   p₁ = σ(0.5) = 0.622                                           │
│   random() = 0.35 → 0.35 < 0.622 → x₁ = 1 ✓                     │
│   Imagen: [1, ?, ?, ?]                                          │
│   ┌───┬───┐                                                     │
│   │ 1 │ ? │                                                     │
│   ├───┼───┤                                                     │
│   │ ? │ ? │                                                     │
│   └───┴───┘                                                     │
│                                                                 │
│   PASO 2: x₂                                                    │
│   p₂ = σ(1.2×1 + 0.3) = σ(1.5) = 0.818                          │
│   random() = 0.72 → 0.72 < 0.818 → x₂ = 1 ✓                     │
│   Imagen: [1, 1, ?, ?]                                          │
│   ┌───┬───┐                                                     │
│   │ 1 │ 1 │                                                     │
│   ├───┼───┤                                                     │
│   │ ? │ ? │                                                     │
│   └───┴───┘                                                     │
│                                                                 │
│   PASO 3: x₃                                                    │
│   p₃ = σ(0.5×1 + 0.8×1 + (-0.8)) = σ(0.5) = 0.622               │
│   random() = 0.91 → 0.91 > 0.622 → x₃ = 0 ✓                     │
│   Imagen: [1, 1, 0, ?]                                          │
│   ┌───┬───┐                                                     │
│   │ 1 │ 1 │                                                     │
│   ├───┼───┤                                                     │
│   │ 0 │ ? │                                                     │
│   └───┴───┘                                                     │
│                                                                 │
│   PASO 4: x₄                                                    │
│   p₄ = σ(0.3×1 + 0.6×1 + 1.5×0 + 0.1) = σ(1.0) = 0.731          │
│   random() = 0.28 → 0.28 < 0.731 → x₄ = 1 ✓                     │
│   Imagen: [1, 1, 0, 1]                                          │
│   ┌───┬───┐                                                     │
│   │ 1 │ 1 │                                                     │
│   ├───┼───┤                                                     │
│   │ 0 │ 1 │                                                     │
│   └───┴───┘                                                     │
│                                                                 │
│   ¡IMAGEN GENERADA! Se parece a las de entrenamiento            │
│   porque usamos los pesos W y bias b que aprendieron            │
│   las relaciones entre píxeles.                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

#### ¿Por qué la imagen generada se parece a las de entrenamiento?

```
┌─────────────────────────────────────────────────────────────────┐
│   LA MAGIA ESTÁ EN LOS PESOS W                                  │
│                                                                 │
│   Durante el entrenamiento, el modelo vio miles de imágenes     │
│   y ajustó los pesos para capturar patrones como:               │
│                                                                 │
│   1. "Si los píxeles 1 y 2 son blancos, el píxel 4              │
│       probablemente también es blanco"                          │
│       → pesos w₄₁ y w₄₂ serán POSITIVOS y GRANDES               │
│                                                                 │
│   2. "Si el píxel 50 es blanco, el píxel 51 probablemente       │
│       también es blanco" (continuidad en trazos)                │
│       → peso w₅₁,₅₀ será POSITIVO                               │
│                                                                 │
│   3. "Los píxeles de las esquinas casi siempre son negros"      │
│       → bias bᵢ para esos píxeles será MUY NEGATIVO             │
│       → σ(número muy negativo) ≈ 0                              │
│                                                                 │
│   Los pesos CODIFICAN la estructura de las imágenes reales.     │
│   Cuando generamos, esos pesos GUÍAN la generación para         │
│   producir imágenes con la misma estructura.                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 11.4 Mapa Conceptual Final

```
┌─────────────────────────────────────────────────────────────────┐
│                   MAPA CONCEPTUAL COMPLETO                      │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                    PROBLEMA                             │   │
│   │   Estimar P(imagen) con 2^784 posibilidades            │   │
│   └───────────────────────┬─────────────────────────────────┘   │
│                           ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │               SOLUCIÓN MATEMÁTICA                       │   │
│   │   Regla del producto:                                   │   │
│   │   P(x) = ∏ P(Xᵢ|anteriores)                            │   │
│   └───────────────────────┬─────────────────────────────────┘   │
│                           ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              SOLUCIÓN COMPUTACIONAL                     │   │
│   │   Perceptrón para cada condicional:                     │   │
│   │   P(Xᵢ|...) ≈ σ(Σ wⱼxⱼ + b)                            │   │
│   └───────────────────────┬─────────────────────────────────┘   │
│                           ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │             CRITERIO DE OPTIMALIDAD                     │   │
│   │   Minimizar KL(P_data || P_θ)                           │   │
│   │   = Minimizar Σ BCE(xᵢ, pᵢ)                            │   │
│   └───────────────────────┬─────────────────────────────────┘   │
│                           ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │               MÉTODO DE OPTIMIZACIÓN                    │   │
│   │   Gradient Descent + Backpropagation                    │   │
│   │   (lo ven en Deep Learning)                             │   │
│   └───────────────────────┬─────────────────────────────────┘   │
│                           ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                   RESULTADO                             │   │
│   │   Modelo entrenado que puede generar imágenes nuevas   │   │
│   │   muestreando secuencialmente de las condicionales     │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 11.5 Próximos Pasos: Otros Modelos

Los modelos autorregresivos que vimos son la BASE. Los modelos más avanzados resuelven sus limitaciones:

```
┌─────────────────────────────────────────────────────────────────┐
│                    FAMILIA DE MODELOS                           │
│                                                                 │
│   AUTORREGRESIVOS (lo que vimos):                               │
│   ───────────────────────────────                               │
│   + Probabilidad exacta (podemos calcular P(imagen))            │
│   + Entrenamiento estable                                       │
│   - Generación LENTA (secuencial)                               │
│   - Orden arbitrario de píxeles                                 │
│   Ejemplos: NADE, PixelCNN, PixelRNN, GPT                       │
│                                                                 │
│   VAE (Variational Autoencoders) - SIGUIENTE TEMA:              │
│   ─────────────────────────────────────────────────             │
│   + Generación RÁPIDA (paralela)                                │
│   + Aprende representaciones útiles (espacio latente)           │
│   - Probabilidad aproximada (no exacta)                         │
│   - Imágenes a veces "borrosas"                                 │
│                                                                 │
│   GAN (Generative Adversarial Networks):                        │
│   ──────────────────────────────────────                        │
│   + Imágenes muy nítidas                                        │
│   + Generación rápida                                           │
│   - Entrenamiento inestable                                     │
│   - No calcula probabilidades                                   │
│                                                                 │
│   DIFFUSION MODELS (estado del arte):                           │
│   ────────────────────────────────────                          │
│   + Mejor calidad actual                                        │
│   + Entrenamiento estable                                       │
│   - Generación lenta (muchos pasos)                             │
│   - Matemática más compleja                                     │
│                                                                 │
│   ═══════════════════════════════════════════════════════════   │
│   TODOS comparten la idea fundamental:                          │
│   Modelar/aproximar la distribución P(datos)                    │
│   ═══════════════════════════════════════════════════════════   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Resumen de Fórmulas Clave

### Probabilidad Básica
```
Regla del producto:     P(X,Y) = P(X) × P(Y|X)
Regla de la suma:       P(X) = Σᵧ P(X,Y)
Independencia:          P(X,Y) = P(X) × P(Y)
Indep. condicional:     P(X,Z|Y) = P(X|Y) × P(Z|Y)
```

### Modelo Autorregresivo
```
Probabilidad conjunta:  P(X₁,...,Xₙ) = ∏ᵢ P(Xᵢ|X₁,...,Xᵢ₋₁)
Aproximación:           P(Xᵢ=1|...) = σ(Σⱼ<ᵢ wᵢⱼxⱼ + bᵢ)
Sigmoide:               σ(z) = 1/(1 + e^(-z))
```

### Entrenamiento
```
Objetivo:              min_θ KL(P_data || P_θ)
Equivalente a:         min_θ (1/N) Σᵢ -log P_θ(xᵢ)
Para Bernoulli:        min_θ (1/N) Σᵢ Σⱼ BCE(xᵢⱼ, pᵢⱼ)
BCE:                   -x×log(p) - (1-x)×log(1-p)
```

### Distribuciones
```
Uniforme:              p(x) = 1/(b-a) para a ≤ x ≤ b
Normal:                p(x) = (1/σ√(2π)) × exp(-(x-μ)²/(2σ²))
Bernoulli:             P(X=1) = θ,  P(X=0) = 1-θ
```

---

## Glosario

- **Autorregresivo:** Modelo donde cada elemento depende de los anteriores
- **BCE (Binary Cross-Entropy):** Función de pérdida para clasificación binaria
- **Bernoulli:** Distribución de probabilidad para eventos binarios (0 o 1)
- **Condicional:** Probabilidad de un evento dado que otro ya ocurrió
- **Conjunta:** Probabilidad de que múltiples eventos ocurran juntos
- **Gradiente:** Dirección de máximo crecimiento de una función
- **KL Divergence:** Medida de diferencia entre dos distribuciones
- **Likelihood:** Probabilidad de los datos dado el modelo
- **Marginal:** Probabilidad de un evento ignorando otras variables
- **MLE:** Maximum Likelihood Estimation - encontrar parámetros que maximizan P(datos)
- **NLL:** Negative Log-Likelihood - lo que minimizamos en la práctica
- **PDF:** Probability Density Function - función de densidad para variables continuas
- **Prior:** Probabilidad inicial, antes de observar datos
- **Red Bayesiana:** Grafo que representa dependencias entre variables
- **Sigmoide:** Función σ(x) = 1/(1+e^(-x)) que mapea cualquier valor a (0,1)
- **Underflow:** Error numérico cuando un número es demasiado pequeño para representar

---

*Documento basado en las clases 1-5 del curso de Inteligencia Artificial Generativa*
