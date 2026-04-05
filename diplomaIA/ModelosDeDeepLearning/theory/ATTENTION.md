# ATTENTION: Todos los Tipos Explicados

Este documento explica las diferencias entre los distintos tipos de attention que aparecen en el curso.

---

## PRIMERO: ¿Qué es "Attention" en general?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ATTENTION = "PRESTAR ATENCIÓN"                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Attention es un mecanismo que permite que una parte del modelo            │
│   "mire" selectivamente otras partes de la información.                     │
│                                                                             │
│   ANALOGÍA SIMPLE:                                                          │
│                                                                             │
│   Imaginate que estás en una fiesta con 20 personas hablando.               │
│   No podés escuchar a todos al mismo tiempo.                                │
│   Tu cerebro PRESTA ATENCIÓN a algunas voces más que a otras.               │
│                                                                             │
│   Attention en redes neuronales hace lo mismo:                              │
│   - Tiene mucha información disponible (todas las palabras)                 │
│   - Decide a cuáles prestarle MÁS atención                                  │
│   - Le da más peso a las importantes, menos a las irrelevantes              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## La Fórmula General de CUALQUIER Attention

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   Output = Σ αᵢ × Vᵢ                                                        │
│                                                                             │
│   Donde:                                                                    │
│   - αᵢ = pesos de atención (números entre 0 y 1 que suman 1)                │
│   - Vᵢ = valores (la información que queremos combinar)                     │
│                                                                             │
│   En palabras simples:                                                      │
│   "El output es un PROMEDIO PONDERADO de los valores"                       │
│                                                                             │
│   Ejemplo:                                                                  │
│   - α₁ = 0.7, α₂ = 0.2, α₃ = 0.1  (suman 1)                                 │
│   - Output = 0.7×V₁ + 0.2×V₂ + 0.1×V₃                                       │
│   - V₁ tiene el mayor peso → es el más "atendido"                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# LOS DIFERENTES TIPOS DE ATTENTION

---

## 1. SOFT ATTENTION vs HARD ATTENTION

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SOFT ATTENTION vs HARD ATTENTION                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   La diferencia está en CÓMO se eligen los pesos α:                         │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│   SOFT ATTENTION (Atención Suave)                                           │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   - Los pesos α son números CONTINUOS entre 0 y 1                           │
│   - Se calculan con SOFTMAX                                                 │
│   - Todos los elementos reciben ALGO de atención (aunque sea poca)          │
│   - ES DIFERENCIABLE → se puede entrenar con backpropagation               │
│                                                                             │
│   Ejemplo: α = [0.05, 0.10, 0.70, 0.10, 0.05]                               │
│            Todos reciben algo, pero el tercero recibe 70%                   │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│   HARD ATTENTION (Atención Dura)                                            │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   - Los pesos α son 0 o 1 (binarios)                                        │
│   - Se ELIGE un solo elemento (o pocos)                                     │
│   - Los demás reciben CERO atención                                         │
│   - NO es diferenciable → necesita técnicas especiales (REINFORCE)          │
│                                                                             │
│   Ejemplo: α = [0, 0, 1, 0, 0]                                              │
│            Solo el tercero recibe atención, los demás nada                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         COMPARACIÓN VISUAL                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Imaginá que tenés 5 fotos y querés elegir cuál mirar:                     │
│                                                                             │
│   SOFT ATTENTION:                                                           │
│   ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐                               │
│   │ 5%  │  │ 10% │  │ 70% │  │ 10% │  │ 5%  │                               │
│   │░░░░░│  │░░░░░│  │█████│  │░░░░░│  │░░░░░│                               │
│   └─────┘  └─────┘  └─────┘  └─────┘  └─────┘                               │
│   Mirás todas, pero te enfocás más en la tercera                            │
│                                                                             │
│   HARD ATTENTION:                                                           │
│   ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐                               │
│   │ 0%  │  │ 0%  │  │100% │  │ 0%  │  │ 0%  │                               │
│   │     │  │     │  │█████│  │     │  │     │                               │
│   └─────┘  └─────┘  └─────┘  └─────┘  └─────┘                               │
│   Solo mirás la tercera, ignorás el resto completamente                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    VENTAJAS Y DESVENTAJAS                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────┬──────────────────────┬──────────────────────┐         │
│   │                 │    SOFT ATTENTION    │    HARD ATTENTION    │         │
│   ├─────────────────┼──────────────────────┼──────────────────────┤         │
│   │ Diferenciable   │         ✅ SÍ        │         ❌ NO        │         │
│   ├─────────────────┼──────────────────────┼──────────────────────┤         │
│   │ Entrenamiento   │     Backprop normal  │   Técnicas especiales│         │
│   │                 │                      │   (ej: REINFORCE)    │         │
│   ├─────────────────┼──────────────────────┼──────────────────────┤         │
│   │ Cómputo         │     Más costoso      │     Más barato       │         │
│   │                 │   (suma ponderada)   │   (solo 1 elemento)  │         │
│   ├─────────────────┼──────────────────────┼──────────────────────┤         │
│   │ Información     │   Usa TODO (mezcla)  │   Descarta mucho     │         │
│   ├─────────────────┼──────────────────────┼──────────────────────┤         │
│   │ Uso común       │   Transformers, NLP  │   Visión, RL         │         │
│   └─────────────────┴──────────────────────┴──────────────────────┘         │
│                                                                             │
│   EN EL CURSO: Casi siempre hablamos de SOFT ATTENTION                      │
│   Los Transformers usan Soft Attention (con softmax)                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. ATTENTION (Bahdanau) vs SELF-ATTENTION

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              ATTENTION (Bahdanau) vs SELF-ATTENTION                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ¿QUIÉN MIRA A QUIÉN?                                                      │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│   ATTENTION (Bahdanau, 2015) - También llamado "Cross-Attention"            │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   Una secuencia mira a OTRA secuencia diferente.                            │
│                                                                             │
│   EJEMPLO: Traducción francés → inglés                                      │
│                                                                             │
│   ENCODER (francés):    "Bonjour"  "le"  "monde"                            │
│                              ↑       ↑       ↑                              │
│                              │       │       │                              │
│                         ┌────┴───────┴───────┴────┐                         │
│                         │     ATTENTION           │                         │
│                         └────────────┬────────────┘                         │
│                                      │                                      │
│   DECODER (inglés):              "Hello" ← está mirando al encoder          │
│                                                                             │
│   El DECODER mira al ENCODER para decidir qué traducir.                     │
│   Son DOS secuencias diferentes.                                            │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│   SELF-ATTENTION (Vaswani, 2017)                                            │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   Una secuencia se mira A SÍ MISMA.                                         │
│                                                                             │
│   EJEMPLO: Procesar una oración                                             │
│                                                                             │
│   "El"  ←→  "gato"  ←→  "negro"  ←→  "duerme"                               │
│     ↑         ↑           ↑            ↑                                    │
│     └─────────┴───────────┴────────────┘                                    │
│           Todas las palabras se miran entre sí                              │
│                                                                             │
│   Cada palabra pregunta: "¿Con qué otras palabras de MI MISMA               │
│   oración estoy relacionada?"                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         COMPARACIÓN DETALLADA                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌────────────────────┬───────────────────────┬───────────────────────┐    │
│   │                    │  ATTENTION (Bahdanau) │    SELF-ATTENTION     │    │
│   ├────────────────────┼───────────────────────┼───────────────────────┤    │
│   │ ¿Quién mira?       │  Decoder              │  Cada posición        │    │
│   ├────────────────────┼───────────────────────┼───────────────────────┤    │
│   │ ¿A quién mira?     │  Al Encoder           │  A sí misma y otras   │    │
│   │                    │  (otra secuencia)     │  (misma secuencia)    │    │
│   ├────────────────────┼───────────────────────┼───────────────────────┤    │
│   │ Query viene de     │  Decoder              │  La misma secuencia   │    │
│   ├────────────────────┼───────────────────────┼───────────────────────┤    │
│   │ Key/Value de       │  Encoder              │  La misma secuencia   │    │
│   ├────────────────────┼───────────────────────┼───────────────────────┤    │
│   │ Usado en           │  Seq2Seq con RNN      │  Transformers         │    │
│   ├────────────────────┼───────────────────────┼───────────────────────┤    │
│   │ Propósito          │  Alinear input/output │  Capturar contexto    │    │
│   └────────────────────┴───────────────────────┴───────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. ¿"ATTENTION" y "SELF-ATTENTION" son lo mismo?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESPUESTA CORTA: NO, PERO ESTÁN RELACIONADOS             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   "ATTENTION" es el concepto GENERAL:                                       │
│   → Un mecanismo para ponderar información selectivamente                   │
│                                                                             │
│   "SELF-ATTENTION" es un TIPO ESPECÍFICO de attention:                      │
│   → Cuando una secuencia se atiende a sí misma                              │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   Es como preguntar: ¿"Vehículo" y "Auto" son lo mismo?                     │
│                                                                             │
│   - Vehículo = concepto general (puede ser auto, moto, bici, avión...)      │
│   - Auto = un tipo específico de vehículo                                   │
│                                                                             │
│   - Attention = concepto general                                            │
│   - Self-Attention = un tipo específico de attention                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. ¿"ATTENTION" y "SOFT ATTENTION" son lo mismo?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESPUESTA: CASI SIEMPRE EN LA PRÁCTICA                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Cuando alguien dice "attention" sin especificar, generalmente se          │
│   refiere a SOFT attention.                                                 │
│                                                                             │
│   ¿Por qué?                                                                 │
│   - Soft attention es diferenciable → fácil de entrenar                     │
│   - Es lo que usan los Transformers                                         │
│   - Es lo más común en NLP                                                  │
│                                                                             │
│   Hard attention se usa menos porque:                                       │
│   - No es diferenciable                                                     │
│   - Necesita técnicas de entrenamiento más complicadas                      │
│                                                                             │
│   EN EL CONTEXTO DEL CURSO:                                                 │
│   Cuando el profesor dice "attention", se refiere a SOFT attention.         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## RESUMEN: TODOS LOS TIPOS DE ATTENTION

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MAPA DE TIPOS DE ATTENTION                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                            ATTENTION                                        │
│                         (concepto general)                                  │
│                               │                                             │
│              ┌────────────────┴────────────────┐                            │
│              │                                 │                            │
│       SOFT ATTENTION                    HARD ATTENTION                      │
│    (pesos continuos 0-1)              (pesos binarios 0/1)                  │
│    (usa softmax)                      (elige uno solo)                      │
│    (diferenciable)                    (no diferenciable)                    │
│              │                                                              │
│              │                                                              │
│   ┌──────────┴──────────────────────┐                                       │
│   │                                 │                                       │
│   │                                 │                                       │
│   CROSS-ATTENTION              SELF-ATTENTION                               │
│   (Bahdanau Attention)         (Vaswani)                                    │
│   │                            │                                            │
│   │ Una secuencia              │ Una secuencia                              │
│   │ mira a OTRA                │ se mira a SÍ MISMA                         │
│   │                            │                                            │
│   │ Query: decoder             │ Query: misma secuencia                     │
│   │ Key/Value: encoder         │ Key/Value: misma secuencia                 │
│   │                            │                                            │
│   │ Ej: traducción             │ Ej: entender contexto                      │
│   │                            │                                            │
│   └────────────────────────────┴──────────────────────────────────────┐     │
│                                                                       │     │
│                                                               MULTI-HEAD    │
│                                                               ATTENTION     │
│                                                               │             │
│                                                               │ Hacer self- │
│                                                               │ attention   │
│                                                               │ VARIAS veces│
│                                                               │ en paralelo │
│                                                               │ (8 cabezas) │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## TERMINOLOGÍA EN EL TRANSFORMER

```
┌─────────────────────────────────────────────────────────────────────────────┐
│            DÓNDE APARECE CADA TIPO EN EL TRANSFORMER                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ENCODER:                                                                  │
│   ─────────                                                                 │
│   "Multi-Head Attention" = Multi-Head SELF-Attention                        │
│   → Las palabras del input se miran entre sí                                │
│   → Q, K, V vienen TODAS del input                                          │
│                                                                             │
│   DECODER:                                                                  │
│   ─────────                                                                 │
│   "Masked Multi-Head Attention" = Multi-Head SELF-Attention con máscara     │
│   → Las palabras del output se miran entre sí (sin ver el futuro)           │
│   → Q, K, V vienen TODAS del output                                         │
│                                                                             │
│   "Multi-Head Attention" (el segundo) = CROSS-Attention                     │
│   → El output mira al input                                                 │
│   → Q viene del decoder, K y V vienen del encoder                           │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   TODOS usan SOFT attention (con softmax)                                   │
│   TODOS son "Multi-Head" (8 cabezas en paralelo)                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# EXPLICACIÓN DEL DIAGRAMA 2 DEL PARCIAL

## Primero: ¿Qué muestra el diagrama?

El diagrama muestra cómo funciona **Scaled Dot-Product Attention**.
Vamos a explicar CADA CAJA del diagrama, una por una.

---

## ELEMENTO 1: La caja verde "X" (Inputs)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              LA ENTRADA: X                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   En el diagrama ves:                                                       │
│                                                                             │
│        ┌─────────┐                                                          │
│        │    X    │  ← Caja verde que dice "Inputs"                          │
│        │  n × d  │                                                          │
│        └─────────┘                                                          │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ ES X?                                                                │
│                                                                             │
│   X es una TABLA (matriz) que contiene las palabras de tu oración.          │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   EJEMPLO: La oración "El gato duerme"                                      │
│                                                                             │
│   X es una tabla con:                                                       │
│   - 3 FILAS (una por cada palabra)                                          │
│   - 512 COLUMNAS (512 números que describen cada palabra)                   │
│                                                                             │
│              columna 1   columna 2   columna 3  ...  columna 512            │
│            ┌───────────────────────────────────────────────────┐            │
│   fila 1   │   0.2         -0.5        0.8      ...    0.1     │  ← "El"    │
│   fila 2   │   0.7          0.3       -0.2      ...    0.4     │  ← "gato"  │
│   fila 3   │  -0.1          0.9        0.5      ...    0.6     │  ← "duerme"│
│            └───────────────────────────────────────────────────┘            │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   LAS DIMENSIONES:                                                          │
│                                                                             │
│   n = número de palabras (tokens) = 3 en este ejemplo                       │
│   d = "embedding size" = cuántos números describen cada palabra = 512       │
│                                                                             │
│   Por eso X tiene dimensión "n × d" (en el ejemplo: 3 × 512)                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ELEMENTO 2: Las cajas grises "Weights" (Wq, Wk, Wv)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LAS CAJAS GRISES: MATRICES DE PESOS                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   En el diagrama ves TRES cajas grises que dicen "Weights":                 │
│                                                                             │
│        ┌─────────┐                                                          │
│        │  Wq^T   │  ← Caja gris "Weights" para crear Q                      │
│        └─────────┘                                                          │
│                                                                             │
│        ┌─────────┐                                                          │
│        │  Wk^T   │  ← Caja gris "Weights" para crear K                      │
│        └─────────┘                                                          │
│                                                                             │
│        ┌─────────┐                                                          │
│        │  Wv^T   │  ← Caja gris "Weights" para crear V                      │
│        └─────────┘                                                          │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ SON ESTAS CAJAS GRISES?                                              │
│                                                                             │
│   Son TABLAS DE NÚMEROS que el modelo APRENDIÓ durante el entrenamiento.    │
│                                                                             │
│   Pensalo así:                                                              │
│   - Cuando entrenás el modelo con millones de textos                        │
│   - El modelo APRENDE qué números poner en estas tablas                     │
│   - Estos números son los "pesos" (weights) de la red neuronal              │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿PARA QUÉ SIRVEN?                                                         │
│                                                                             │
│   Sirven para TRANSFORMAR X en tres cosas diferentes: Q, K, y V.            │
│                                                                             │
│   Es como si tuvieras tres "filtros" o "lentes" diferentes:                 │
│   - Un filtro para crear "preguntas" (Q)                                    │
│   - Un filtro para crear "etiquetas" (K)                                    │
│   - Un filtro para crear "contenido" (V)                                    │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿QUÉ SIGNIFICA EL "^T" (TRANSPUESTA)?                                     │
│                                                                             │
│   Transponer una matriz = "voltearla" (las filas pasan a ser columnas)      │
│                                                                             │
│   Original:        Transpuesta:                                             │
│   ┌───┬───┐        ┌───┬───┬───┐                                            │
│   │ 1 │ 2 │        │ 1 │ 3 │ 5 │                                            │
│   │ 3 │ 4 │   →    │ 2 │ 4 │ 6 │                                            │
│   │ 5 │ 6 │        └───┴───┴───┘                                            │
│   └───┴───┘                                                                 │
│   (3×2)            (2×3)                                                    │
│                                                                             │
│   En el diagrama aparece Wq^T porque matemáticamente necesitamos            │
│   la transpuesta para que la multiplicación funcione.                       │
│   No te preocupes mucho por esto - es un detalle técnico.                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ELEMENTO 3: Las cajas blancas Q, K, V

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         LAS CAJAS Q, K, V                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   En el diagrama ves que de X salen TRES flechas, cada una pasa por         │
│   una caja gris (Weights) y produce una caja blanca:                        │
│                                                                             │
│              ┌───────┐         ┌───────┐                                    │
│        X ───▶│ Wq^T  │────────▶│   Q   │                                    │
│              └───────┘         └───────┘                                    │
│                                                                             │
│              ┌───────┐         ┌───────┐                                    │
│        X ───▶│ Wk^T  │────────▶│   K   │                                    │
│              └───────┘         └───────┘                                    │
│                                                                             │
│              ┌───────┐         ┌───────┐                                    │
│        X ───▶│ Wv^T  │────────▶│   V   │                                    │
│              └───────┘         └───────┘                                    │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ OPERACIÓN SE HACE?                                                   │
│                                                                             │
│   Multiplicación de matrices:                                               │
│                                                                             │
│   Q = X × Wq^T    (X multiplicado por la matriz de pesos Wq)                │
│   K = X × Wk^T    (X multiplicado por la matriz de pesos Wk)                │
│   V = X × Wv^T    (X multiplicado por la matriz de pesos Wv)                │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ SIGNIFICA MULTIPLICAR MATRICES? (Explicación simple)                 │
│                                                                             │
│   Imaginate que X es la descripción de tus palabras.                        │
│   Multiplicar por Wq es como "filtrar" esa descripción                      │
│   para quedarte solo con cierta información.                                │
│                                                                             │
│   Ejemplo simple con números:                                               │
│                                                                             │
│   X = descripción de "gato" = [0.7, 0.3, -0.2]   (3 números)                │
│                                                                             │
│   Wq = │ 0.5   0.1 │                                                        │
│        │ 0.2   0.8 │  (matriz de 3×2)                                       │
│        │-0.1   0.3 │                                                        │
│                                                                             │
│   Q = X × Wq = [0.7×0.5 + 0.3×0.2 + (-0.2)×(-0.1),                          │
│                 0.7×0.1 + 0.3×0.8 + (-0.2)×0.3]                             │
│              = [0.35 + 0.06 + 0.02, 0.07 + 0.24 - 0.06]                     │
│              = [0.43, 0.25]   (ahora tiene 2 números)                       │
│                                                                             │
│   La palabra "gato" ahora tiene una nueva representación [0.43, 0.25]       │
│   que es su "query" (Q).                                                    │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ REPRESENTAN Q, K, V? (Analogía del buscador)                         │
│                                                                             │
│   Imaginate que cada palabra es como una persona en una red social:         │
│                                                                             │
│   Q (Query) = "¿Qué estoy buscando?"                                        │
│               Es la PREGUNTA que hace cada palabra.                         │
│               "gato" pregunta: "¿Quién es mi verbo? ¿Quién me describe?"    │
│                                                                             │
│   K (Key) = "¿Cómo me pueden encontrar?"                                    │
│             Es la ETIQUETA de cada palabra.                                 │
│             "duerme" tiene etiqueta: "Soy un verbo, busco un sujeto"        │
│                                                                             │
│   V (Value) = "¿Qué información tengo para dar?"                            │
│               Es el CONTENIDO de cada palabra.                              │
│               "gato" tiene contenido: "animal, mascota, felino..."          │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   DIMENSIONES EN EL DIAGRAMA:                                               │
│                                                                             │
│   Q tiene dimensión (n × dq):  n palabras, dq números por palabra           │
│   K tiene dimensión (n × dk):  n palabras, dk números por palabra           │
│   V tiene dimensión (n × dv):  n palabras, dv números por palabra           │
│                                                                             │
│   IMPORTANTE: dq = dk (deben ser iguales para la multiplicación QK^T)       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ELEMENTO 4: La caja naranja "QK^T" (Attention Matrix)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LA CAJA NARANJA: QK^T                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   En el diagrama ves:                                                       │
│                                                                             │
│        Q ────┐                                                              │
│              ├───▶ ┌─────────┐                                              │
│        K ────┘     │  QK^T   │  ← Caja naranja "Attention matrix"           │
│                    │  n × n  │                                              │
│                    └─────────┘                                              │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ OPERACIÓN ES ESTA?                                                   │
│                                                                             │
│   Q × K^T = multiplicar Q por K transpuesta                                 │
│                                                                             │
│   Recuerda: transponer K significa "voltear" la tabla.                      │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿QUÉ PRODUCE?                                                             │
│                                                                             │
│   Una tabla de n × n (tantas filas como palabras, tantas columnas como      │
│   palabras).                                                                │
│                                                                             │
│   Con 3 palabras ("El gato duerme"), produce una tabla de 3×3:              │
│                                                                             │
│                          El      gato    duerme                             │
│                    ┌─────────────────────────────┐                          │
│   El              │   2.1      0.8       0.3    │                          │
│   gato            │   0.7      1.9       1.2    │                          │
│   duerme          │   0.4      1.5       1.0    │                          │
│                    └─────────────────────────────┘                          │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿QUÉ SIGNIFICA CADA NÚMERO?                                               │
│                                                                             │
│   Cada número dice: "¿Cuánto la palabra de la FILA se relaciona             │
│                      con la palabra de la COLUMNA?"                         │
│                                                                             │
│   Fila "duerme", Columna "gato" = 1.5                                       │
│   → "duerme" tiene una relación de 1.5 con "gato"                           │
│   → Es un número alto, significa que están MUY relacionados                 │
│   → (tiene sentido: "gato" es el sujeto de "duerme")                        │
│                                                                             │
│   Fila "duerme", Columna "El" = 0.4                                         │
│   → "duerme" tiene una relación de 0.4 con "El"                             │
│   → Es un número bajo, no están muy relacionados                            │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ SE LLAMA "ATTENTION MATRIX"?                                     │
│                                                                             │
│   Porque te dice A QUÉ debe prestar ATENCIÓN cada palabra.                  │
│   Los números altos = "prestá atención a esto"                              │
│   Los números bajos = "ignorá esto"                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ELEMENTO 5: La caja gris "Softmax"

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         LA CAJA SOFTMAX                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   En el diagrama ves:                                                       │
│                                                                             │
│        ┌─────────┐         ┌─────────┐                                      │
│        │  QK^T   │────────▶│ Softmax │                                      │
│        └─────────┘         └─────────┘                                      │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ HACE SOFTMAX?                                                        │
│                                                                             │
│   Convierte números "crudos" en PORCENTAJES que suman 100%.                 │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   EJEMPLO:                                                                  │
│                                                                             │
│   ANTES de softmax (números crudos):                                        │
│   Fila "duerme": [0.4, 1.5, 1.0]                                            │
│                   ↑     ↑     ↑                                             │
│                  El   gato  duerme                                          │
│                                                                             │
│   DESPUÉS de softmax (porcentajes):                                         │
│   Fila "duerme": [0.15, 0.50, 0.35]                                         │
│                   ↑      ↑      ↑                                           │
│                  15%    50%    35%     → suman 100%                         │
│                  El    gato  duerme                                         │
│                                                                             │
│   INTERPRETACIÓN:                                                           │
│   "duerme" presta 50% de atención a "gato"                                  │
│   "duerme" presta 35% de atención a sí mismo                                │
│   "duerme" presta 15% de atención a "El"                                    │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ CONVERTIR A PORCENTAJES?                                         │
│                                                                             │
│   Porque después vamos a hacer un PROMEDIO PONDERADO.                       │
│   Necesitamos que los pesos sumen 1 (o 100%) para que tenga sentido.        │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   NOTA: En el diagrama real también se divide por √dk antes del softmax.    │
│   Esto es para ESTABILIDAD NUMÉRICA (evitar números muy grandes).           │
│   No tiene significado especial de machine learning.                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ELEMENTO 6: La caja blanca "A"

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           LA CAJA A                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   En el diagrama ves:                                                       │
│                                                                             │
│        ┌─────────┐         ┌─────────┐                                      │
│        │ Softmax │────────▶│    A    │                                      │
│        └─────────┘         │  n × n  │                                      │
│                            └─────────┘                                      │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ ES A?                                                                │
│                                                                             │
│   A es la MATRIZ DE PESOS DE ATENCIÓN.                                      │
│   Es el resultado de aplicar softmax a QK^T.                                │
│                                                                             │
│   Con 3 palabras, A es una tabla de 3×3:                                    │
│                                                                             │
│                          El      gato    duerme                             │
│                    ┌─────────────────────────────┐                          │
│   El              │   0.60     0.25      0.15   │  ← suma = 1.00           │
│   gato            │   0.20     0.55      0.25   │  ← suma = 1.00           │
│   duerme          │   0.15     0.50      0.35   │  ← suma = 1.00           │
│                    └─────────────────────────────┘                          │
│                                                                             │
│   CADA FILA SUMA 1.00 (o 100%)                                              │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿CÓMO SE LEE?                                                             │
│                                                                             │
│   Lee por FILAS:                                                            │
│                                                                             │
│   Fila "duerme" = [0.15, 0.50, 0.35]                                        │
│                                                                             │
│   Significa:                                                                │
│   - "duerme" presta 15% de atención a "El"                                  │
│   - "duerme" presta 50% de atención a "gato"  ← ¡LA MÁS ALTA!               │
│   - "duerme" presta 35% de atención a "duerme" (a sí mismo)                 │
│                                                                             │
│   Tiene sentido: "duerme" necesita saber QUIÉN duerme → mira a "gato"       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ELEMENTO 7: La caja verde "Z" (Outputs)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         LA CAJA Z (OUTPUT)                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   En el diagrama ves:                                                       │
│                                                                             │
│        ┌─────────┐                                                          │
│        │    A    │────┐                                                     │
│        └─────────┘    │     ┌─────────┐                                     │
│                       ├────▶│    Z    │  ← Caja verde "Outputs"             │
│        ┌─────────┐    │     │  n × dv │                                     │
│        │    V    │────┘     └─────────┘                                     │
│        └─────────┘                                                          │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ OPERACIÓN SE HACE?                                                   │
│                                                                             │
│   Z = A × V                                                                 │
│                                                                             │
│   Multiplicamos la matriz de atención (A) por los valores (V).              │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ SIGNIFICA ESTO? (EXPLICACIÓN SIMPLE)                                 │
│                                                                             │
│   Es un PROMEDIO PONDERADO.                                                 │
│                                                                             │
│   Imaginate que cada palabra tiene "información" (su V).                    │
│   Z dice: "Voy a mezclar la información de todas las palabras,              │
│            pero le doy más peso a las que tienen atención alta."            │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   EJEMPLO CONCRETO:                                                         │
│                                                                             │
│   Para calcular Z₃ (la representación nueva de "duerme"):                   │
│                                                                             │
│   Fila 3 de A = [0.15, 0.50, 0.35]  (los pesos de atención de "duerme")     │
│                                                                             │
│   Z₃ = 0.15 × V₁ + 0.50 × V₂ + 0.35 × V₃                                    │
│         ↑           ↑           ↑                                           │
│        15% de      50% de      35% de                                       │
│        info de     info de     info de                                      │
│        "El"        "gato"      "duerme"                                     │
│                                                                             │
│   RESULTADO:                                                                │
│   Z₃ es una MEZCLA de la información de todas las palabras,                 │
│   pero con 50% de la información de "gato" (porque es lo más relevante).    │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿QUÉ REPRESENTA Z?                                                        │
│                                                                             │
│   Z es la nueva representación de cada palabra, ENRIQUECIDA con             │
│   información del contexto.                                                 │
│                                                                             │
│   - X era: cada palabra SOLA, sin saber nada de las demás                   │
│   - Z es: cada palabra SABIENDO cosas sobre las demás                       │
│                                                                             │
│   Z tiene la misma cantidad de filas que X (una por palabra),               │
│   pero ahora cada palabra "entiende" su contexto.                           │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   DIMENSIONES:                                                              │
│                                                                             │
│   Z tiene dimensión (n × dv):                                               │
│   - n filas = una por cada palabra                                          │
│   - dv columnas = dimensión de los values                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## RESUMEN: EL FLUJO COMPLETO DEL DIAGRAMA

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         FLUJO COMPLETO PASO A PASO                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   PASO 1: Empezamos con X (las palabras)                                    │
│           X = ["El", "gato", "duerme"] representadas como números           │
│                                                                             │
│   PASO 2: Multiplicamos X por tres matrices de pesos (las cajas grises)     │
│           X × Wq → Q (las preguntas de cada palabra)                        │
│           X × Wk → K (las etiquetas de cada palabra)                        │
│           X × Wv → V (el contenido de cada palabra)                         │
│                                                                             │
│   PASO 3: Multiplicamos Q × K^T                                             │
│           Resultado: una tabla que dice cuánto se relaciona                 │
│           cada palabra con cada otra palabra                                │
│                                                                             │
│   PASO 4: Aplicamos Softmax                                                 │
│           Convertimos esos números en porcentajes (pesos de atención)       │
│           Resultado: matriz A                                               │
│                                                                             │
│   PASO 5: Multiplicamos A × V                                               │
│           Mezclamos la información según los pesos de atención              │
│           Resultado: Z (las palabras enriquecidas con contexto)             │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   LA FÓRMULA COMPLETA:                                                      │
│                                                                             │
│   Attention(Q, K, V) = softmax(Q × K^T / √dk) × V                           │
│                                                                             │
│   En palabras:                                                              │
│   1. Calcular cuánto se relaciona cada palabra con cada otra (QK^T)         │
│   2. Dividir por √dk (para estabilidad numérica)                            │
│   3. Convertir a porcentajes (softmax)                                      │
│   4. Mezclar la información según esos porcentajes (× V)                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DIAGRAMA VISUAL SIMPLIFICADO                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                                                                             │
│        X (palabras)                                                         │
│        ┌─────────┐                                                          │
│        │ n × d   │                                                          │
│        └────┬────┘                                                          │
│             │                                                               │
│    ┌────────┼────────┐                                                      │
│    │        │        │                                                      │
│    ▼        ▼        ▼                                                      │
│  ┌────┐  ┌────┐  ┌────┐       ← Cajas grises (Weights)                      │
│  │ Wq │  │ Wk │  │ Wv │         Son los pesos aprendidos                    │
│  └──┬─┘  └──┬─┘  └──┬─┘                                                     │
│     │       │       │                                                       │
│     ▼       ▼       ▼                                                       │
│  ┌────┐  ┌────┐  ┌────┐       ← Cajas blancas Q, K, V                       │
│  │ Q  │  │ K  │  │ V  │         Representaciones transformadas              │
│  └──┬─┘  └──┬─┘  └──┬─┘                                                     │
│     │       │       │                                                       │
│     └───┬───┘       │                                                       │
│         │           │                                                       │
│         ▼           │                                                       │
│     ┌───────┐       │         ← Caja naranja QK^T                           │
│     │ QK^T  │       │           "¿Cuánto se relacionan las palabras?"       │
│     └───┬───┘       │                                                       │
│         │           │                                                       │
│         ▼           │                                                       │
│     ┌───────┐       │         ← Caja Softmax                                │
│     │Softmax│       │           Convierte a porcentajes                     │
│     └───┬───┘       │                                                       │
│         │           │                                                       │
│         ▼           │                                                       │
│     ┌───────┐       │         ← Caja A                                      │
│     │   A   │       │           Pesos de atención (porcentajes)             │
│     └───┬───┘       │                                                       │
│         │           │                                                       │
│         └─────┬─────┘                                                       │
│               │                                                             │
│               ▼                                                             │
│           ┌───────┐           ← Caja verde Z (Output)                       │
│           │   Z   │             Palabras enriquecidas con contexto          │
│           │ n × dv│                                                         │
│           └───────┘                                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ¿CUÁL ES LA DIFERENCIA ENTRE QK^T Y A?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         QK^T vs A: LA DIFERENCIA                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Mucha gente se confunde porque QK^T y A tienen LA MISMA DIMENSIÓN (n×n). │
│   Pero contienen INFORMACIÓN DIFERENTE.                                     │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   QK^T = SCORES CRUDOS (números "brutos")                                   │
│   ────────────────────────────────────────                                  │
│                                                                             │
│   - Son el resultado de multiplicar Q × K^T                                 │
│   - Pueden ser CUALQUIER número: positivo, negativo, grande, pequeño        │
│   - NO suman 1                                                              │
│   - NO son probabilidades                                                   │
│                                                                             │
│   Ejemplo de una fila de QK^T:                                              │
│   [2.1, 8.5, -1.3, 4.7]  ← números crudos, no significan nada por sí solos  │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   A = PESOS DE ATENCIÓN (probabilidades)                                    │
│   ──────────────────────────────────────                                    │
│                                                                             │
│   - Son el resultado de aplicar SOFTMAX a QK^T (dividido por √dk)           │
│   - Son números entre 0 y 1                                                 │
│   - SUMAN 1 en cada fila                                                    │
│   - SON probabilidades (o porcentajes)                                      │
│                                                                             │
│   Ejemplo de una fila de A:                                                 │
│   [0.05, 0.70, 0.02, 0.23]  ← suman 1.00 (5% + 70% + 2% + 23% = 100%)       │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   EL FLUJO ENTRE ELLOS:                                                     │
│                                                                             │
│   QK^T ──→ ÷√dk ──→ Softmax ──→ A                                           │
│                                                                             │
│   Hay DOS operaciones entre QK^T y A:                                       │
│   1. Dividir por √dk (para estabilidad numérica)                            │
│   2. Aplicar Softmax (para convertir a probabilidades)                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    EJEMPLO NUMÉRICO CONCRETO                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Supongamos que dk = 64, entonces √dk = 8                                  │
│                                                                             │
│   Fila de QK^T (para "duerme"):                                             │
│   [3.2, 12.0, 8.8]  ← scores crudos para [El, gato, duerme]                 │
│                                                                             │
│   PASO 1: Dividir por √dk = 8                                               │
│   [3.2/8, 12.0/8, 8.8/8] = [0.4, 1.5, 1.1]                                  │
│                                                                             │
│   PASO 2: Aplicar Softmax                                                   │
│   softmax([0.4, 1.5, 1.1]) = [0.13, 0.52, 0.35]                             │
│                               ↑     ↑      ↑                                │
│                              13%   52%    35%  ← suman 100%                 │
│                                                                             │
│   Fila de A (para "duerme"):                                                │
│   [0.13, 0.52, 0.35]  ← ahora son probabilidades                            │
│                                                                             │
│   INTERPRETACIÓN:                                                           │
│   "duerme" presta 13% de atención a "El"                                    │
│   "duerme" presta 52% de atención a "gato"  ← ¡el más alto!                 │
│   "duerme" presta 35% de atención a sí mismo                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ¿POR QUÉ NECESITAMOS CONVERTIR A PROBABILIDADES?         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Porque después vamos a hacer un PROMEDIO PONDERADO con V.                 │
│                                                                             │
│   Z = A × V                                                                 │
│                                                                             │
│   Si A no sumara 1, el resultado sería un "promedio" mal escalado.          │
│                                                                             │
│   EJEMPLO:                                                                  │
│                                                                             │
│   CON QK^T (no suma 1):                                                     │
│   Z = 3.2×V₁ + 12.0×V₂ + 8.8×V₃                                             │
│   → El resultado sería 24 veces más grande de lo que debería                │
│   → Los números explotarían                                                 │
│                                                                             │
│   CON A (suma 1):                                                           │
│   Z = 0.13×V₁ + 0.52×V₂ + 0.35×V₃                                           │
│   → El resultado es un promedio ponderado bien escalado                     │
│   → Z tiene magnitud similar a los V individuales                           │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ANALOGÍA:                                                                 │
│                                                                             │
│   Imaginate que querés mezclar 3 colores de pintura:                        │
│                                                                             │
│   MAL (QK^T): "Poné 3.2 litros de rojo, 12 litros de azul, 8.8 de verde"    │
│   → Te sobra pintura, no sabés cuánta mezcla vas a tener                    │
│                                                                             │
│   BIEN (A): "Poné 13% de rojo, 52% de azul, 35% de verde"                   │
│   → Siempre te da 100% de mezcla, bien proporcionada                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ¿POR QUÉ CADA COSA SE CONECTA CON OTRA? (LAS CONEXIONES)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MAPA DE CONEXIONES DEL DIAGRAMA                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                              X                                              │
│                              │                                              │
│              ┌───────────────┼───────────────┐                              │
│              │               │               │                              │
│              ▼               ▼               ▼                              │
│           ┌─────┐        ┌─────┐        ┌─────┐                             │
│           │ Wq  │        │ Wk  │        │ Wv  │                             │
│           └──┬──┘        └──┬──┘        └──┬──┘                             │
│              │              │              │                                │
│              ▼              ▼              ▼                                │
│           ┌─────┐        ┌─────┐        ┌─────┐                             │
│           │  Q  │        │  K  │        │  V  │                             │
│           └──┬──┘        └──┬──┘        └──┬──┘                             │
│              │              │              │                                │
│              └──────┬───────┘              │                                │
│                     │                      │                                │
│                     ▼                      │                                │
│                 ┌───────┐                  │                                │
│                 │ QK^T  │                  │                                │
│                 └───┬───┘                  │                                │
│                     │                      │                                │
│                     ▼                      │                                │
│                 ┌───────┐                  │                                │
│                 │÷ √dk  │                  │                                │
│                 └───┬───┘                  │                                │
│                     │                      │                                │
│                     ▼                      │                                │
│                 ┌───────┐                  │                                │
│                 │Softmax│                  │                                │
│                 └───┬───┘                  │                                │
│                     │                      │                                │
│                     ▼                      │                                │
│                 ┌───────┐                  │                                │
│                 │   A   │                  │                                │
│                 └───┬───┘                  │                                │
│                     │                      │                                │
│                     └──────────┬───────────┘                                │
│                                │                                            │
│                                ▼                                            │
│                            ┌───────┐                                        │
│                            │   Z   │                                        │
│                            └───────┘                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

Ahora expliquemos CADA conexión:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CONEXIÓN 1: X → Wq, Wk, Wv                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                              X                                              │
│                              │                                              │
│              ┌───────────────┼───────────────┐                              │
│              ▼               ▼               ▼                              │
│           ┌─────┐        ┌─────┐        ┌─────┐                             │
│           │ Wq  │        │ Wk  │        │ Wv  │                             │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿POR QUÉ X SE CONECTA CON TRES COSAS?                                     │
│                                                                             │
│   Porque necesitamos crear TRES representaciones diferentes de cada         │
│   palabra, y las tres vienen de la MISMA información original (X).          │
│                                                                             │
│   ANALOGÍA:                                                                 │
│   Imaginate que tenés una foto de una persona.                              │
│   De esa MISMA foto, querés extraer:                                        │
│   - Información sobre su cara (para reconocerla) → Q                        │
│   - Información sobre su ropa (para describirla) → K                        │
│   - Información sobre su pose (para analizarla) → V                         │
│                                                                             │
│   La foto es una sola (X), pero la procesás de 3 formas diferentes.         │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ TRES Y NO DOS O CINCO?                                           │
│                                                                             │
│   Porque el mecanismo de attention necesita exactamente 3 roles:            │
│   - Q: "¿Qué busco?" (la pregunta)                                          │
│   - K: "¿Cómo me encuentran?" (la etiqueta para ser encontrado)             │
│   - V: "¿Qué información doy?" (el contenido a devolver)                    │
│                                                                             │
│   Es como un diccionario:                                                   │
│   - Q = tu búsqueda                                                         │
│   - K = las palabras del diccionario                                        │
│   - V = las definiciones                                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CONEXIÓN 2: Wq→Q, Wk→K, Wv→V                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│           ┌─────┐        ┌─────┐        ┌─────┐                             │
│           │ Wq  │        │ Wk  │        │ Wv  │                             │
│           └──┬──┘        └──┬──┘        └──┬──┘                             │
│              │              │              │                                │
│              ▼              ▼              ▼                                │
│           ┌─────┐        ┌─────┐        ┌─────┐                             │
│           │  Q  │        │  K  │        │  V  │                             │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ HACE ESTA CONEXIÓN?                                                  │
│                                                                             │
│   Cada W transforma X en algo diferente:                                    │
│   - X × Wq = Q (las queries)                                                │
│   - X × Wk = K (las keys)                                                   │
│   - X × Wv = V (los values)                                                 │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ USAR MATRICES DIFERENTES?                                        │
│                                                                             │
│   Porque queremos que Q, K, V capturen ASPECTOS DIFERENTES de las palabras. │
│                                                                             │
│   Si usáramos la misma matriz para todo, Q, K, V serían iguales.            │
│   No tendría sentido.                                                       │
│                                                                             │
│   ANALOGÍA:                                                                 │
│   Es como ver algo con tres lentes de colores diferentes:                   │
│   - Lente rojo (Wq): resalta ciertas características → Q                    │
│   - Lente azul (Wk): resalta otras características → K                      │
│   - Lente verde (Wv): resalta otras diferentes → V                          │
│                                                                             │
│   El objeto es el mismo (X), pero cada lente te muestra algo distinto.      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CONEXIÓN 3: Q y K → QK^T                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│           ┌─────┐        ┌─────┐                                            │
│           │  Q  │        │  K  │                                            │
│           └──┬──┘        └──┬──┘                                            │
│              │              │                                               │
│              └──────┬───────┘                                               │
│                     │                                                       │
│                     ▼                                                       │
│                 ┌───────┐                                                   │
│                 │ QK^T  │                                                   │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿POR QUÉ SE MULTIPLICAN Q y K?                                            │
│                                                                             │
│   Para calcular CUÁNTO SE PARECEN las preguntas (Q) a las etiquetas (K).    │
│                                                                             │
│   Multiplicar vectores es una forma de medir SIMILITUD:                     │
│   - Si Q y K apuntan en la misma dirección → número ALTO                    │
│   - Si Q y K apuntan en direcciones opuestas → número BAJO o negativo       │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ K TRANSPUESTA (K^T)?                                             │
│                                                                             │
│   Por cómo funciona la multiplicación de matrices.                          │
│                                                                             │
│   Queremos que cada fila de Q se compare con cada fila de K.                │
│   Pero en multiplicación de matrices, las filas se multiplican por COLUMNAS.│
│   Entonces transponemos K para que sus filas pasen a ser columnas.          │
│                                                                             │
│   Q × K^T:                                                                  │
│   - Fila 1 de Q se multiplica por Columna 1 de K^T (que era Fila 1 de K)    │
│   - Fila 1 de Q se multiplica por Columna 2 de K^T (que era Fila 2 de K)    │
│   - etc.                                                                    │
│                                                                             │
│   Resultado: cada palabra (fila de Q) se compara con cada palabra (fila de K)│
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ NO SE USA V AQUÍ?                                                │
│                                                                             │
│   Porque V es el CONTENIDO, no la ETIQUETA.                                 │
│                                                                             │
│   Primero decidimos A QUIÉN prestar atención (comparando Q con K).          │
│   Después usamos V para obtener la información de esos "quiénes".           │
│                                                                             │
│   ANALOGÍA:                                                                 │
│   Buscás en Google: "recetas de pasta" (tu Q)                               │
│   Google compara con los títulos de las páginas (las K)                     │
│   Todavía no leés el CONTENIDO de las páginas (los V)                       │
│   Solo estás decidiendo cuáles son relevantes                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CONEXIÓN 4: QK^T → ÷√dk → Softmax → A                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                 ┌───────┐                                                   │
│                 │ QK^T  │                                                   │
│                 └───┬───┘                                                   │
│                     │                                                       │
│                     ▼                                                       │
│                 ┌───────┐                                                   │
│                 │÷ √dk  │                                                   │
│                 └───┬───┘                                                   │
│                     │                                                       │
│                     ▼                                                       │
│                 ┌───────┐                                                   │
│                 │Softmax│                                                   │
│                 └───┬───┘                                                   │
│                     │                                                       │
│                     ▼                                                       │
│                 ┌───────┐                                                   │
│                 │   A   │                                                   │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿POR QUÉ DIVIDIR POR √dk?                                                 │
│                                                                             │
│   Por ESTABILIDAD NUMÉRICA.                                                 │
│                                                                             │
│   Cuando dk es grande (ej: 64), los productos en QK^T pueden ser            │
│   números muy grandes (ej: 50, 100, 200...).                                │
│                                                                             │
│   Si le pasamos números muy grandes a softmax:                              │
│   - softmax([1, 10, 2]) = [0.00, 1.00, 0.00]  ← se "satura"                 │
│   - Pierde la capacidad de distinguir matices                               │
│                                                                             │
│   Dividir por √64 = 8 hace los números más pequeños:                        │
│   - softmax([0.1, 1.2, 0.2]) = [0.15, 0.60, 0.25]  ← más suave              │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ √dk Y NO OTRO NÚMERO?                                            │
│                                                                             │
│   Es una elección basada en estadística.                                    │
│   Si Q y K tienen varianza 1, entonces QK^T tiene varianza dk.              │
│   Dividir por √dk hace que el resultado tenga varianza ~1.                  │
│   (No te preocupes si no entendés esto - es un detalle técnico)             │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ SOFTMAX?                                                         │
│                                                                             │
│   Para convertir scores en PROBABILIDADES que sumen 1.                      │
│                                                                             │
│   Softmax hace dos cosas:                                                   │
│   1. Convierte cualquier número en un número entre 0 y 1                    │
│   2. Hace que todos los números de una fila sumen exactamente 1             │
│                                                                             │
│   Necesitamos que sumen 1 para hacer un promedio ponderado válido.          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CONEXIÓN 5: A y V → Z                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                 ┌───────┐                  ┌─────┐                          │
│                 │   A   │                  │  V  │                          │
│                 └───┬───┘                  └──┬──┘                          │
│                     │                         │                             │
│                     └────────────┬────────────┘                             │
│                                  │                                          │
│                                  ▼                                          │
│                              ┌───────┐                                      │
│                              │   Z   │                                      │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿POR QUÉ SE MULTIPLICAN A y V?                                            │
│                                                                             │
│   Para hacer el PROMEDIO PONDERADO de los valores.                          │
│                                                                             │
│   - A dice: "cuánta atención prestar a cada palabra" (los pesos)            │
│   - V dice: "qué información tiene cada palabra" (el contenido)             │
│   - Z dice: "la mezcla de información según los pesos"                      │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   EJEMPLO:                                                                  │
│                                                                             │
│   Para "duerme", A dice: [0.13, 0.52, 0.35]                                 │
│                           ↑      ↑      ↑                                   │
│                          El    gato  duerme                                 │
│                                                                             │
│   V contiene la "información" de cada palabra:                              │
│   - V₁ = información de "El" (64 números)                                   │
│   - V₂ = información de "gato" (64 números)                                 │
│   - V₃ = información de "duerme" (64 números)                               │
│                                                                             │
│   Z₃ = 0.13×V₁ + 0.52×V₂ + 0.35×V₃                                          │
│                                                                             │
│   Z₃ es la nueva representación de "duerme", que ahora contiene:            │
│   - 13% de información de "El"                                              │
│   - 52% de información de "gato"  ← la mayor parte                          │
│   - 35% de información de sí mismo                                          │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ NO SE USA Q NI K AQUÍ?                                           │
│                                                                             │
│   Porque Q y K ya cumplieron su función:                                    │
│   - Q y K sirvieron para DECIDIR a quién prestar atención                   │
│   - Esa decisión quedó guardada en A                                        │
│   - Ahora A se usa para MEZCLAR los contenidos (V)                          │
│                                                                             │
│   ANALOGÍA:                                                                 │
│   Ya buscaste en Google (Q vs K) y ya decidiste qué páginas leer (A).       │
│   Ahora leés el CONTENIDO de esas páginas (V) y tomás notas (Z).            │
│   Ya no necesitás los títulos (K) ni tu búsqueda original (Q).              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESUMEN: EL PROPÓSITO DE CADA CONEXIÓN                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   CONEXIÓN              │  PROPÓSITO                                        │
│   ──────────────────────┼─────────────────────────────────────────────────  │
│   X → Wq, Wk, Wv        │  Crear 3 vistas diferentes de las palabras        │
│   ──────────────────────┼─────────────────────────────────────────────────  │
│   Wq→Q, Wk→K, Wv→V      │  Transformar X en queries, keys y values          │
│   ──────────────────────┼─────────────────────────────────────────────────  │
│   Q, K → QK^T           │  Medir cuánto se relaciona cada par de palabras   │
│   ──────────────────────┼─────────────────────────────────────────────────  │
│   QK^T → ÷√dk           │  Escalar para estabilidad numérica                │
│   ──────────────────────┼─────────────────────────────────────────────────  │
│   ÷√dk → Softmax        │  Convertir scores en probabilidades (suman 1)     │
│   ──────────────────────┼─────────────────────────────────────────────────  │
│   Softmax → A           │  Obtener los pesos de atención finales            │
│   ──────────────────────┼─────────────────────────────────────────────────  │
│   A, V → Z              │  Mezclar el contenido según los pesos de atención │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   EN RESUMEN, EL FLUJO COMPLETO ES:                                         │
│                                                                             │
│   1. Empezamos con palabras (X)                                             │
│   2. Las transformamos en preguntas (Q), etiquetas (K), contenidos (V)      │
│   3. Comparamos preguntas con etiquetas para ver quién se relaciona (QK^T)  │
│   4. Convertimos eso en porcentajes de atención (A)                         │
│   5. Mezclamos los contenidos según esos porcentajes (Z)                    │
│   6. Terminamos con palabras enriquecidas con contexto (Z)                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## DIMENSIONES DE CADA ELEMENTO (MUY IMPORTANTE)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ¿QUÉ SIGNIFICA "DIMENSIÓN"?                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Cuando decimos que algo tiene dimensión "n × d", significa:               │
│                                                                             │
│   - Es una TABLA (matriz)                                                   │
│   - Tiene n FILAS                                                           │
│   - Tiene d COLUMNAS                                                        │
│                                                                             │
│   Ejemplo: Una matriz de 3 × 4 tiene 3 filas y 4 columnas:                  │
│                                                                             │
│            col1  col2  col3  col4                                           │
│          ┌─────────────────────────┐                                        │
│   fila1  │  1     2     3     4    │                                        │
│   fila2  │  5     6     7     8    │                                        │
│   fila3  │  9    10    11    12    │                                        │
│          └─────────────────────────┘                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    VARIABLES QUE USAMOS EN EL DIAGRAMA                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   n  = número de palabras (tokens) en la oración                            │
│        Ejemplo: "El gato duerme" → n = 3                                    │
│                                                                             │
│   d  = tamaño del embedding (cuántos números describen cada palabra)        │
│        Ejemplo típico: d = 512 (en el Transformer original)                 │
│                                                                             │
│   dq = dimensión de las queries                                             │
│        Ejemplo típico: dq = 64                                              │
│                                                                             │
│   dk = dimensión de las keys                                                │
│        IMPORTANTE: dk = dq (deben ser iguales)                              │
│        Ejemplo típico: dk = 64                                              │
│                                                                             │
│   dv = dimensión de los values                                              │
│        Ejemplo típico: dv = 64                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DIMENSIÓN DE X (LA ENTRADA)                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   X tiene dimensión: (n × d)                                                │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                     │   │
│   │       d columnas (512 números por palabra)                          │   │
│   │   ←─────────────────────────────────────────→                       │   │
│   │                                                                     │   │
│   │   ┌───────────────────────────────────────────┐  ↑                  │   │
│   │   │  0.2   -0.5   0.8   ...   0.1   (512 núm) │  │                  │   │
│   │   ├───────────────────────────────────────────┤  │ n filas          │   │
│   │   │  0.7    0.3  -0.2   ...   0.4   (512 núm) │  │ (3 palabras)     │   │
│   │   ├───────────────────────────────────────────┤  │                  │   │
│   │   │ -0.1    0.9   0.5   ...   0.6   (512 núm) │  ↓                  │   │
│   │   └───────────────────────────────────────────┘                     │   │
│   │      ↑       ↑      ↑          ↑                                    │   │
│   │     "El"   "gato" "duerme"                                          │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   ¿POR QUÉ ESTAS DIMENSIONES?                                               │
│                                                                             │
│   - n filas porque tenemos n palabras (cada fila = una palabra)             │
│   - d columnas porque cada palabra se representa con d números              │
│     (el embedding convierte cada palabra en d números)                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DIMENSIÓN DE Wq, Wk, Wv (LOS PESOS)                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Wq tiene dimensión: (d × dq)     Ejemplo: (512 × 64)                      │
│   Wk tiene dimensión: (d × dk)     Ejemplo: (512 × 64)                      │
│   Wv tiene dimensión: (d × dv)     Ejemplo: (512 × 64)                      │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ ESTAS DIMENSIONES?                                               │
│                                                                             │
│   Porque queremos TRANSFORMAR de d dimensiones a dq/dk/dv dimensiones.      │
│                                                                             │
│   Piensa en Wq como un "compresor":                                         │
│   - Entrada: 512 números (el embedding de una palabra)                      │
│   - Salida: 64 números (la "query" de esa palabra)                          │
│                                                                             │
│   Para que la multiplicación X × Wq funcione:                               │
│   - X tiene d columnas (512)                                                │
│   - Wq debe tener d filas (512) para que coincida                           │
│   - Wq tiene dq columnas (64) que es lo que queremos de salida              │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   LA REGLA DE MULTIPLICACIÓN DE MATRICES:                                   │
│                                                                             │
│   (n × d) × (d × dq) = (n × dq)                                             │
│      ↑        ↑   ↑       ↑                                                 │
│      │        │   │       └─ columnas del resultado                         │
│      │        │   └─ columnas de la segunda matriz                          │
│      │        └─ DEBEN COINCIDIR (d = d) para poder multiplicar             │
│      └─ filas del resultado                                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DIMENSIÓN DE Q, K, V                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Q = X × Wq    →    (n × d) × (d × dq) = (n × dq)                          │
│   K = X × Wk    →    (n × d) × (d × dk) = (n × dk)                          │
│   V = X × Wv    →    (n × d) × (d × dv) = (n × dv)                          │
│                                                                             │
│   Ejemplo con números concretos:                                            │
│   Q: (3 × 512) × (512 × 64) = (3 × 64)                                      │
│   K: (3 × 512) × (512 × 64) = (3 × 64)                                      │
│   V: (3 × 512) × (512 × 64) = (3 × 64)                                      │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿QUÉ SIGNIFICA ESTO?                                                      │
│                                                                             │
│   Q tiene (n × dq) = (3 × 64):                                              │
│   - 3 filas = una query por cada palabra                                    │
│   - 64 columnas = cada query tiene 64 números                               │
│                                                                             │
│   ┌─────────────────────────────────────┐                                   │
│   │  Query de "El":     [64 números]    │                                   │
│   │  Query de "gato":   [64 números]    │                                   │
│   │  Query de "duerme": [64 números]    │                                   │
│   └─────────────────────────────────────┘                                   │
│                                                                             │
│   Lo mismo para K y V: cada palabra tiene su key y su value.                │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ "COMPRIMIR" DE 512 A 64?                                         │
│                                                                             │
│   1. Reduce el costo computacional (menos números = más rápido)             │
│   2. Fuerza al modelo a extraer la información más importante               │
│   3. En Multi-Head Attention, se hacen 8 "cabezas" de 64 cada una           │
│      → 8 × 64 = 512 (se recupera la dimensión original)                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DIMENSIÓN DE QK^T (LA ATTENTION MATRIX)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   QK^T = Q × K^T                                                            │
│                                                                             │
│   Primero: ¿Qué dimensión tiene K^T (K transpuesta)?                        │
│                                                                             │
│   K tiene (n × dk)  →  K^T tiene (dk × n)                                   │
│                                                                             │
│   Ejemplo: K es (3 × 64)  →  K^T es (64 × 3)                                │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   Ahora la multiplicación:                                                  │
│                                                                             │
│   Q × K^T  =  (n × dq) × (dk × n)  =  (n × n)                               │
│                  ↑          ↑                                               │
│                  └────┬─────┘                                               │
│               dq = dk (deben ser iguales para que funcione)                 │
│                                                                             │
│   Ejemplo: (3 × 64) × (64 × 3) = (3 × 3)                                    │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ EL RESULTADO ES (n × n)?                                         │
│                                                                             │
│   ¡Porque queremos una tabla de PALABRA × PALABRA!                          │
│                                                                             │
│   Con 3 palabras, QK^T es una tabla de 3×3:                                 │
│                                                                             │
│                     El     gato   duerme                                    │
│               ┌─────────────────────────────┐                               │
│   El         │  ___      ___      ___      │  ← relación de "El" con cada  │
│   gato       │  ___      ___      ___      │  ← relación de "gato" con cada│
│   duerme     │  ___      ___      ___      │  ← relación de "duerme" c/cada│
│               └─────────────────────────────┘                               │
│                                                                             │
│   Cada celda (i, j) = "¿Cuánto la palabra i se relaciona con la palabra j?" │
│                                                                             │
│   POR ESO es n × n: queremos comparar CADA palabra con CADA otra palabra.   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DIMENSIÓN DE A (DESPUÉS DE SOFTMAX)                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   A = softmax(QK^T / √dk)                                                   │
│                                                                             │
│   A tiene dimensión: (n × n)   (igual que QK^T)                             │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ LA MISMA DIMENSIÓN?                                              │
│                                                                             │
│   Porque softmax NO cambia el tamaño de la matriz.                          │
│   Solo convierte los números en probabilidades.                             │
│                                                                             │
│   ANTES (QK^T):  [0.4, 1.5, 1.0]  ← números crudos                          │
│   DESPUÉS (A):   [0.15, 0.50, 0.35]  ← probabilidades (suman 1)             │
│                                                                             │
│   La cantidad de números es la misma, solo cambian los valores.             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DIMENSIÓN DE Z (EL OUTPUT)                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Z = A × V                                                                 │
│                                                                             │
│   Z = (n × n) × (n × dv) = (n × dv)                                         │
│                                                                             │
│   Ejemplo: (3 × 3) × (3 × 64) = (3 × 64)                                    │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿QUÉ SIGNIFICA ESTO?                                                      │
│                                                                             │
│   Z tiene (n × dv) = (3 × 64):                                              │
│   - 3 filas = una representación nueva por cada palabra                     │
│   - 64 columnas = cada representación tiene 64 números (igual que V)        │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ Z TIENE n FILAS?                                                 │
│                                                                             │
│   Porque empezamos con n palabras y terminamos con n palabras.              │
│   La cantidad de palabras NO cambia.                                        │
│                                                                             │
│   Lo que SÍ cambia es que ahora cada palabra tiene información              │
│   del contexto (de las otras palabras).                                     │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ¿POR QUÉ Z TIENE dv COLUMNAS?                                             │
│                                                                             │
│   Porque el output es una mezcla de los V (values).                         │
│   Cada V tiene dv columnas, entonces la mezcla también tiene dv columnas.   │
│                                                                             │
│   Z₁ = 0.60×V₁ + 0.25×V₂ + 0.15×V₃                                          │
│         ↑         ↑         ↑                                               │
│        (64)      (64)      (64)   → resultado: (64)                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESUMEN DE TODAS LAS DIMENSIONES                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ELEMENTO    │  DIMENSIÓN   │  EJEMPLO (n=3, d=512, dq=dk=dv=64)           │
│   ────────────┼──────────────┼─────────────────────────────────────────     │
│   X           │  (n × d)     │  (3 × 512)                                   │
│   Wq          │  (d × dq)    │  (512 × 64)                                  │
│   Wk          │  (d × dk)    │  (512 × 64)                                  │
│   Wv          │  (d × dv)    │  (512 × 64)                                  │
│   Q           │  (n × dq)    │  (3 × 64)                                    │
│   K           │  (n × dk)    │  (3 × 64)                                    │
│   V           │  (n × dv)    │  (3 × 64)                                    │
│   K^T         │  (dk × n)    │  (64 × 3)                                    │
│   QK^T        │  (n × n)     │  (3 × 3)                                     │
│   A           │  (n × n)     │  (3 × 3)                                     │
│   Z           │  (n × dv)    │  (3 × 64)                                    │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   OBSERVACIONES IMPORTANTES:                                                │
│                                                                             │
│   1. dq DEBE ser igual a dk                                                 │
│      → Para que Q × K^T funcione (las columnas de Q deben coincidir         │
│        con las filas de K^T)                                                │
│                                                                             │
│   2. QK^T es (n × n)                                                        │
│      → Porque queremos comparar CADA palabra con CADA palabra               │
│      → n palabras × n palabras = n² comparaciones                           │
│                                                                             │
│   3. Z tiene las mismas filas que X (n)                                     │
│      → Entramos con n palabras, salimos con n palabras                      │
│      → La cantidad de palabras NO cambia                                    │
│                                                                             │
│   4. Los parámetros (Wq, Wk, Wv) NO dependen de n                           │
│      → Podemos procesar oraciones de CUALQUIER largo                        │
│      → Una oración de 5 palabras o de 100 usa los MISMOS pesos              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## DIAGRAMA VISUAL COMPLETO

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SCALED DOT-PRODUCT ATTENTION - FLUJO                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                              X (input)                                      │
│                             (n × d)                                         │
│                                │                                            │
│              ┌─────────────────┼─────────────────┐                          │
│              │                 │                 │                          │
│              ▼                 ▼                 ▼                          │
│         ┌────────┐        ┌────────┐        ┌────────┐                      │
│         │  × Wq  │        │  × Wk  │        │  × Wv  │                      │
│         └───┬────┘        └───┬────┘        └───┬────┘                      │
│             │                 │                 │                           │
│             ▼                 ▼                 ▼                           │
│         ┌───────┐         ┌───────┐         ┌───────┐                       │
│         │   Q   │         │   K   │         │   V   │                       │
│         │(n×dq) │         │(n×dk) │         │(n×dv) │                       │
│         └───┬───┘         └───┬───┘         └───┬───┘                       │
│             │                 │                 │                           │
│             │      ┌──────────┘                 │                           │
│             ▼      ▼                            │                           │
│         ┌────────────┐                          │                           │
│         │   Q × K^T  │                          │                           │
│         │   (n × n)  │                          │                           │
│         └─────┬──────┘                          │                           │
│               │                                 │                           │
│               ▼                                 │                           │
│         ┌────────────┐                          │                           │
│         │  ÷ √dk     │  ← escalar               │                           │
│         └─────┬──────┘                          │                           │
│               │                                 │                           │
│               ▼                                 │                           │
│         ┌────────────┐                          │                           │
│         │  softmax   │  ← por filas             │                           │
│         └─────┬──────┘                          │                           │
│               │                                 │                           │
│               ▼                                 │                           │
│         ┌───────┐                               │                           │
│         │   A   │   Attention                   │                           │
│         │(n×n)  │   Weights                     │                           │
│         └───┬───┘                               │                           │
│             │                    ┌──────────────┘                           │
│             │                    │                                          │
│             ▼                    ▼                                          │
│         ┌────────────────────────────┐                                      │
│         │         A × V              │                                      │
│         └────────────┬───────────────┘                                      │
│                      │                                                      │
│                      ▼                                                      │
│                  ┌───────┐                                                  │
│                  │   Z   │  OUTPUT                                          │
│                  │(n×dv) │  (representación contextualizada)                │
│                  └───────┘                                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## PARA EL PARCIAL: RESPUESTA MODELO

Si te preguntan "¿Qué operación se está realizando en el diagrama?":

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         RESPUESTA PARA EL PARCIAL                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   El diagrama muestra el cálculo de SCALED DOT-PRODUCT ATTENTION.           │
│                                                                             │
│   1. A partir de la entrada X (n tokens × d dimensiones), se crean          │
│      tres matrices Q, K, V multiplicando por matrices de pesos              │
│      aprendibles Wq, Wk, Wv.                                                │
│                                                                             │
│   2. Se calcula la matriz de attention QK^T, donde cada posición (i,j)      │
│      representa qué tan relacionado está el token i con el token j.         │
│                                                                             │
│   3. Se divide por √dk para estabilidad numérica (evitar saturación         │
│      del softmax cuando los valores son muy grandes).                       │
│                                                                             │
│   4. Se aplica softmax fila por fila, convirtiendo los scores en            │
│      pesos de atención (probabilidades que suman 1 por fila).               │
│                                                                             │
│   5. Se multiplica la matriz A de pesos por V, obteniendo Z:                │
│      cada fila de Z es un promedio ponderado de los valores V,              │
│      donde los pesos indican cuánta atención presta cada token              │
│      a los demás.                                                           │
│                                                                             │
│   El resultado Z tiene la misma cantidad de tokens que X, pero              │
│   ahora cada token incorpora información contextual de los demás.           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## RESUMEN FINAL: GLOSARIO RÁPIDO

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              GLOSARIO RÁPIDO                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ATTENTION: Mecanismo general para ponderar información selectivamente     │
│                                                                             │
│   SOFT ATTENTION: Pesos continuos (0 a 1), usa softmax, diferenciable       │
│                                                                             │
│   HARD ATTENTION: Pesos binarios (0 o 1), selecciona uno, no diferenciable  │
│                                                                             │
│   SELF-ATTENTION: Una secuencia se atiende a sí misma (Q, K, V del mismo X) │
│                                                                             │
│   CROSS-ATTENTION: Una secuencia atiende a otra (Q de una, K/V de otra)     │
│                                                                             │
│   SCALED DOT-PRODUCT: La fórmula softmax(QK^T/√dk) × V                      │
│                                                                             │
│   MULTI-HEAD: Hacer self-attention varias veces en paralelo (ej: 8 cabezas) │
│                                                                             │
│   Q (Query): "¿Qué busco?"                                                  │
│   K (Key): "¿Cómo me encuentran?"                                           │
│   V (Value): "¿Qué información tengo?"                                      │
│                                                                             │
│   √dk: División para estabilidad numérica (no tiene significado de ML)      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ¿CUÁNDO APARECE ESTE DIAGRAMA? (Self-Attention vs Cross-Attention)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│            ESTE DIAGRAMA APARECE EN AMBOS TIPOS DE ATTENTION                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   El diagrama de "Scaled Dot-Product Attention" es la OPERACIÓN BÁSICA     │
│   que se usa en TODOS los tipos de attention del Transformer.              │
│                                                                             │
│   La operación (softmax(QK^T/√dk) × V) es SIEMPRE LA MISMA.                 │
│                                                                             │
│   Lo que CAMBIA es de DÓNDE vienen Q, K, y V:                               │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   SELF-ATTENTION (Encoder o Decoder)                                        │
│   ───────────────────────────────────                                       │
│                                                                             │
│        X (una sola secuencia)                                               │
│              │                                                              │
│        ┌─────┼─────┐                                                        │
│        │     │     │                                                        │
│        ▼     ▼     ▼                                                        │
│        Q     K     V      ← LOS TRES vienen del MISMO X                     │
│                                                                             │
│   Ejemplo: "El gato duerme" se atiende A SÍ MISMA                           │
│   Cada palabra mira a las otras palabras de la MISMA oración.               │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   CROSS-ATTENTION (Decoder mirando al Encoder)                              │
│   ─────────────────────────────────────────────                             │
│                                                                             │
│        Decoder          Encoder                                             │
│           │                │                                                │
│           ▼           ┌────┴────┐                                           │
│           Q           K        V   ← K y V vienen del ENCODER               │
│           │           │        │      Q viene del DECODER                   │
│           └─────┬─────┴────────┘                                            │
│                 │                                                           │
│              Attention                                                      │
│                                                                             │
│   Ejemplo: Traducción "The cat sleeps" → "El gato duerme"                   │
│   El decoder (generando español) PREGUNTA al encoder (inglés)               │
│   Q = "¿Qué palabra inglesa debo mirar ahora?"                              │
│   K, V = información de las palabras en inglés                              │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   RESUMEN:                                                                  │
│                                                                             │
│   │ TIPO            │ FUENTE DE Q │ FUENTE DE K, V │                        │
│   │─────────────────│─────────────│────────────────│                        │
│   │ Self-Attention  │ X           │ X (la misma)   │                        │
│   │ Cross-Attention │ Decoder     │ Encoder        │                        │
│                                                                             │
│   La OPERACIÓN del diagrama es idéntica en ambos casos.                     │
│   Solo cambia de DÓNDE vienen los datos.                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```
