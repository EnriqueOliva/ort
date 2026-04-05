# Clase 9 (03 de Noviembre 2025) - Deep Learning
## Redes Neuronales Recurrentes (RNN)

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
║  ════════════════════════════════════════════════════════════════════════════════════    ║
║  ║ CLASE 9 (03-Nov) ◄─── ESTÁS AQUÍ                                               ║      ║
║  ║  • RNN Vanilla: cómo procesar SECUENCIAS                                       ║      ║
║  ║  • LSTM y GRU: cómo recordar a LARGO PLAZO                                     ║      ║
║  ║  • Arquitecturas: Bidireccional, Stacked                                       ║      ║
║  ════════════════════════════════════════════════════════════════════════════════════    ║
║  │                                                                                       ║
║  ▼  CONEXIÓN: Ya tenemos modelos que procesan secuencias y recuerdan                     ║
║                                                                                          ║
║  CLASE 10 (10-Nov) ────────────────────────────────────────────────────────────────────  ║
║  │  • Modelos de Lenguaje: predecir la siguiente palabra                                 ║
║  │  • N-gramas y sus problemas                                                           ║
║  │  • Encoder-Decoder / Seq2Seq: traducción, diferentes longitudes                       ║
║  │  • Teacher Forcing: cómo entrenar estos modelos                                       ║
║  │                                                                                       ║
║  ▼  PROBLEMA: El contexto se comprime en UN SOLO vector (cuello de botella)              ║
║                                                                                          ║
║  CLASE 11 (17-Nov) ────────────────────────────────────────────────────────────────────  ║
║  │  • Attention de Bahdanau: contexto DINÁMICO (miramos TODO el encoder)                 ║
║  │  • Self-Attention: cada palabra mira a TODAS las demás                                ║
║  │  • Query, Key, Value: la terminología moderna                                         ║
║  │  • Multi-Head Attention: varias "cabezas" mirando relaciones distintas                ║
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

# MAPA CONCEPTUAL DE ESTA CLASE: Cómo se conectan los temas

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   PROBLEMA: Las redes feedforward no tienen memoria                     │
│   (no pueden procesar secuencias donde el contexto importa)             │
│                                                                         │
└────────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   SOLUCION 1: RNN Vanilla                                               │
│   (red con estado oculto que funciona como memoria)                     │
│                                                                         │
└────────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   PROBLEMA: RNN Vanilla tiene vanishing gradient                        │
│   (se "olvida" de lo que paso hace mucho tiempo)                        │
│   Demostrado en: The Copying Task                                       │
│                                                                         │
└────────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   SOLUCION 2: LSTM y GRU                                                │
│   (agregan "compuertas" para controlar que recordar y que olvidar)      │
│   GRU es la version simplificada y RECOMENDADA por el profesor          │
│                                                                         │
└────────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   EXTENSIONES: Arquitecturas avanzadas                                  │
│   - RNN Apiladas (mas capas)                                            │
│   - RNN Bidireccionales (leen en ambas direcciones)                     │
│   - Como usarlas para clasificacion                                     │
│                                                                         │
└────────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   CONTEXTO HISTORICO:                                                   │
│   RNN → Attention → Transformers (ChatGPT)                              │
│   Las RNN aun se usan para tareas especificas                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

TEMA SEPARADO (tarea practica):
┌─────────────────────────────────────────────────────────────────────────┐
│   Double Descent: Fenomeno donde mas parametros = mejor performance     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

# SECCION A: EL PROBLEMA - Por que necesitamos RNN

## A.1 Que es una secuencia

Una secuencia es una **lista ordenada donde el orden importa**.

**Ejemplos:**
- Palabras de una oracion: ["Hola", "como", "estas"]
- Latidos del corazon medidos cada segundo
- Temperaturas de cada dia del ano
- Precios de una accion a lo largo del tiempo

**El orden importa porque:**
- "El perro mordio al hombre" ≠ "El hombre mordio al perro"
- La temperatura de hoy depende de la de ayer

---

## A.2 El problema de las redes feedforward

Una red feedforward (la red tradicional) tiene un problema fatal:

| Aspecto | Feedforward | Lo que necesitamos |
|---------|-------------|-------------------|
| Memoria | NO tiene | Necesita recordar contexto |
| Entradas | Una sola entrada | Secuencia de entradas |
| Ejemplo | Si le pasas "banco" | No sabe si es dinero o asiento |

**El problema:** Sin contexto, no puede entender secuencias.

---

## A.3 Maquina de estados: la intuicion

**Que es una maquina de estados?**
- Tiene **estados** (situaciones en las que puede estar)
- Tiene **transiciones** (cuando recibe algo, cambia de estado)

**Ejemplo - maquina de cafe:**
1. Estado: "Esperando que elijas bebida"
2. Input: "Boton de capuchino"
3. Transicion: Prepara el cafe
4. Nuevo estado: "Sirviendo bebida"

**Por que importa:** Las RNN funcionan como maquinas de estados. Tienen un "estado interno" (memoria) que cambia segun lo que van viendo.

---

# SECCION B: LA SOLUCION 1 - RNN Vanilla (Basica)

## B.1 La idea central

La RNN agrega un **estado oculto** (hidden state) que funciona como memoria:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   En cada paso de tiempo, la RNN recibe:                    │
│   - X_t: La entrada actual (ej: una palabra)                │
│   - H_{t-1}: El estado oculto anterior (la "memoria")       │
│                                                             │
│   Y produce:                                                │
│   - Y_t: La salida (opcional)                               │
│   - H_t: El nuevo estado oculto (memoria actualizada)       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

El estado oculto H es "todo lo que la red ha visto hasta ahora".

---

## B.2 Las tres matrices de la RNN

Una RNN vanilla tiene exactamente **3 matrices de pesos**. Vamos a entenderlas paso a paso.

### Primero: ¿Qué hace una matriz en una red neuronal?

Recuerda que en una capa Dense (la que ya conoces):
```
salida = W × entrada + b
```
La matriz W **transforma** un vector de una dimensión a otra.

**Ejemplo:** Si W es de tamaño [100 × 50], transforma un vector de 50 números en uno de 100 números.

### Las 3 matrices de la RNN

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      DENTRO DE UNA CELDA RNN                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ENTRADAS:                                                                 │
│   ─────────                                                                 │
│   X_t ──────────▶ [U] ──────┐                                              │
│   (la palabra               │                                              │
│    actual)                  │                                              │
│                             ▼                                              │
│                        ┌─────────┐                                         │
│                        │   (+)   │──▶ tanh() ──▶ H_t (nuevo estado)        │
│                        └─────────┘                     │                   │
│                             ▲                          │                   │
│   H_{t-1} ──────▶ [V] ──────┘                          ▼                   │
│   (memoria del                                    ┌─────────┐              │
│    paso anterior)                                 │   [W]   │              │
│                                                   └────┬────┘              │
│                                                        │                   │
│                                                        ▼                   │
│                                                       Y_t                  │
│                                                   (predicción)             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ¿Qué hace cada matriz?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   ╔═══════════════════════════════════════════════════════════════════╗    │
│   ║  MATRIZ U: "Lo nuevo que entra"                                   ║    │
│   ║  ───────────────────────────────                                  ║    │
│   ║  • Transforma la ENTRADA (X_t) para que pueda combinarse          ║    │
│   ║    con la memoria                                                 ║    │
│   ║  • Dimensiones: [tamaño_estado × tamaño_entrada]                  ║    │
│   ║                                                                   ║    │
│   ║  Ejemplo: Si X_t tiene 300 dimensiones (embedding de palabra)     ║    │
│   ║           y el estado oculto tiene 128 dimensiones:               ║    │
│   ║           U es [128 × 300]                                        ║    │
│   ║           U × X_t = vector de 128 dimensiones                     ║    │
│   ╚═══════════════════════════════════════════════════════════════════╝    │
│                                                                             │
│   ╔═══════════════════════════════════════════════════════════════════╗    │
│   ║  MATRIZ V: "La recurrencia" (lo que ya sabía)                     ║    │
│   ║  ─────────────────────────────────────────────                    ║    │
│   ║  • Transforma el ESTADO ANTERIOR (H_{t-1}) para combinarlo        ║    │
│   ║    con la nueva entrada                                           ║    │
│   ║  • ESTA es la matriz que hace la RNN "recurrente"                 ║    │
│   ║  • Dimensiones: [tamaño_estado × tamaño_estado] (¡cuadrada!)      ║    │
│   ║                                                                   ║    │
│   ║  Ejemplo: Si el estado tiene 128 dimensiones:                     ║    │
│   ║           V es [128 × 128]                                        ║    │
│   ║           V × H_{t-1} = vector de 128 dimensiones                 ║    │
│   ╚═══════════════════════════════════════════════════════════════════╝    │
│                                                                             │
│   ╔═══════════════════════════════════════════════════════════════════╗    │
│   ║  MATRIZ W: "Lo que predigo"                                       ║    │
│   ║  ──────────────────────────                                       ║    │
│   ║  • Transforma el ESTADO ACTUAL (H_t) para producir la SALIDA      ║    │
│   ║  • Dimensiones: [tamaño_salida × tamaño_estado]                   ║    │
│   ║                                                                   ║    │
│   ║  Ejemplo: Si queremos predecir la siguiente palabra               ║    │
│   ║           de un vocabulario de 10,000 palabras:                   ║    │
│   ║           W es [10000 × 128]                                      ║    │
│   ║           W × H_t = vector de 10000 (probabilidades)              ║    │
│   ╚═══════════════════════════════════════════════════════════════════╝    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Ejemplo concreto con dimensiones reales

Supongamos:
- **Embedding de palabras:** 300 dimensiones (X_t es un vector de 300 números)
- **Estado oculto:** 128 dimensiones
- **Vocabulario:** 10,000 palabras

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     EJEMPLO CON DIMENSIONES REALES                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   X_t                                                                       │
│   [300]        ×    U [128×300]    =    [128]                              │
│   (palabra)         (pesos)            (contribución de la entrada)         │
│                                                                             │
│   H_{t-1}                                                                   │
│   [128]        ×    V [128×128]    =    [128]                              │
│   (memoria)         (pesos)            (contribución de la memoria)         │
│                                                                             │
│   [128] + [128] = [128]  →  tanh()  →  H_t [128]                           │
│   (se suman)                            (nuevo estado)                      │
│                                                                             │
│   H_t                                                                       │
│   [128]        ×    W [10000×128]  =    [10000]  →  softmax  →  Y_t        │
│   (estado)          (pesos)             (probabilidad de cada palabra)      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ¿Por qué se SUMAN U×X_t y V×H_{t-1}?

```
H_t = tanh( U×X_t  +  V×H_{t-1} )
            ─────     ─────────
              │           │
              │           └── "lo que recuerdo del pasado"
              │
              └────────────── "lo nuevo que estoy viendo"
```

La suma combina ambas informaciones. El `tanh` comprime el resultado entre -1 y 1.

**Restricción:** U×X_t y V×H_{t-1} DEBEN tener la **misma dimensión** porque se suman.
- U×X_t produce un vector de 128
- V×H_{t-1} produce un vector de 128
- [128] + [128] = [128] ✓

### Las fórmulas completas

```
H_t = tanh(U × X_t + V × H_{t-1} + b_h)    ← Nuevo estado (memoria actualizada)
Y_t = W × H_t + b_y                         ← Salida (predicción)
```

Donde `b_h` y `b_y` son los **bias** (vectores de números que se suman al final).

### Comparación con una capa Dense

| Capa Dense | RNN |
|------------|-----|
| `y = W × x + b` | `H_t = tanh(U × X_t + V × H_{t-1} + b)` |
| Una sola entrada | Dos entradas: X_t y H_{t-1} |
| Sin memoria | El H_{t-1} trae información del pasado |
| Una matriz W | Dos matrices U y V (más W para la salida) |

---

## B.3 Unfolding: visualizando la RNN en el tiempo

```
Tiempo t=1:  X_1 → [RNN] → Y_1
                    ↓ H_1
Tiempo t=2:  X_2 → [RNN] → Y_2
                    ↓ H_2
Tiempo t=3:  X_3 → [RNN] → Y_3
```

**CRUCIAL - Weight Sharing:**

Las matrices U, V, W **SON SIEMPRE LAS MISMAS** en cada paso. No son copias diferentes, es la misma matriz usada una y otra vez.

**Por que importa:**
1. El tamano del modelo NO crece con la longitud de la secuencia
2. Los gradientes se ACUMULAN de todos los pasos

---

## B.4 Como se entrena: Backpropagation Through Time (BPTT)

**Proceso:**
1. **Forward:** Procesas toda la secuencia, calculando H_t y Y_t
2. **Backward:** Despliegas la red como grafo y aplicas backprop normal
3. Los gradientes de U, V, W se **suman** de todas las apariciones

**Problema con secuencias largas:** Si tienes 1000 pasos, el grafo es enorme.

**Solucion - Truncated BPTT:** Usar una ventana deslizante de tamano K.
- Procesas K elementos
- Calculas gradiente solo para esa ventana
- Mueves la ventana K pasos adelante
- Es una **aproximacion**, pero funciona

---

## B.5 Ventajas y desventajas de RNN

| Ventajas | Desventajas |
|----------|-------------|
| Secuencias de cualquier longitud | Computo lento (secuencial, no paralelo) |
| Tamano del modelo fijo | Dificultad para recordar pasado lejano |
| Memoria historica | No puede ver el futuro |
| Weight sharing | Vanishing/Exploding gradients |

---

# SECCION C: EL PROBLEMA CON RNN VANILLA

## C.1 Vanishing y Exploding Gradients

Este es **EL problema** que hace que la RNN vanilla sea dificil de usar:

### Exploding Gradient
- Los gradientes se vuelven MUY GRANDES
- Ocurre si valores de V > 1, al multiplicarse muchas veces → crece exponencialmente
- **Solucion:** Gradient clipping (recortar si es muy grande)

### Vanishing Gradient (el mas grave)
- Los gradientes se vuelven MUY PEQUENOS (cercanos a cero)
- Ocurre si valores de V < 1, al multiplicarse muchas veces → tiende a cero
- **Consecuencia:** La red "olvida" lo que paso hace mucho tiempo
- **NO tiene solucion facil** en RNN vanilla

---

## C.2 The Copying Task: Demostracion empirica del problema

Este experimento demuestra que la RNN vanilla no puede recordar a largo plazo.

**La tarea:**
```
ENTRADA: [3, 7, 2, 8, 1] [blank × 500] [DELIM] [blank × 5]
         └─ secuencia ─┘ └─ retardo ─┘         └─ espacio ─┘

SALIDA:  [blank × (500+5+1)] [3, 7, 2, 8, 1]
                              └─ debe reproducir la secuencia original ─┘
```

**El desafio:** Recordar algo de hace 500+ pasos atras.

**Resultados:**

| Modelo | Resultado |
|--------|-----------|
| RNN Vanilla | ❌ FALLA - despues de 1000 pasos adivina al azar |
| LSTM | ✓ Error muy bajo |
| GRU | ✓ Error muy bajo |

**Esto demuestra empiricamente** que necesitamos LSTM o GRU.

---

# SECCION D: LA SOLUCION 2 - LSTM y GRU

## D.1 La idea: Compuertas (Gates)

La solucion es usar **compuertas** que controlen el flujo de informacion, como valvulas que abren o cierran el paso.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   Las compuertas deciden:                                       │
│   - Que informacion OLVIDAR del pasado                          │
│   - Que informacion NUEVA agregar                               │
│   - Que informacion MOSTRAR en la salida                        │
│                                                                 │
│   Son valores entre 0 y 1 (sigmoid):                            │
│   - 0 = cerrar completamente (bloquear)                         │
│   - 1 = abrir completamente (dejar pasar)                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## D.2 LSTM (Long Short-Term Memory)

### Dos estados separados
- **Cell State (C):** Memoria a LARGO plazo
- **Hidden State (H):** Memoria de TRABAJO

### Las 4 compuertas

| Compuerta | Funcion | Formula |
|-----------|---------|---------|
| Forget (f) | Que olvidar del Cell State anterior | f_t = σ(W_f × X_t + U_f × H_{t-1}) |
| Input (i) | Que tan importante es lo nuevo | i_t = σ(W_i × X_t + U_i × H_{t-1}) |
| Cell Candidate | Propuesta de nuevo contenido | C̃_t = tanh(W_c × X_t + U_c × H_{t-1}) |
| Output (o) | Que mostrar del estado | o_t = σ(W_o × X_t + U_o × H_{t-1}) |

### LA FORMULA CLAVE del Cell State:
```
C_t = f_t ⊙ C_{t-1} + i_t ⊙ C̃_t
      └─ que MANTENGO ─┘   └─ que AGREGO ─┘
```

### El Hidden State:
```
H_t = o_t ⊙ tanh(C_t)
```

### Parametros
- 8 matrices (4 W + 4 U) + 4 bias
- Mucho mas que RNN vanilla

---

## D.3 GRU (Gated Recurrent Unit) - LA RECOMENDADA

El profesor dijo: **"La GRU me parece la mejor. Es mejor en todo aspecto: tiene menos parametros, es mas facil de entrenar."**

### Simplificacion respecto a LSTM

| Aspecto | LSTM | GRU |
|---------|------|-----|
| Estados | 2 (C y H) | **1 (solo H)** |
| Compuertas | 4 | **2** |
| Parametros | Mas | **Menos** |

### Las 2 compuertas

| Compuerta | Funcion | Formula |
|-----------|---------|---------|
| Reset (r) | Cuanto olvidar del estado previo | r_t = σ(W_r × X_t + U_r × H_{t-1}) |
| Update (z) | Balance mantener vs actualizar | z_t = σ(W_z × X_t + U_z × H_{t-1}) |

### LA FORMULA CLAVE:
```
H_t = (1 - z_t) ⊙ H̃_t + z_t ⊙ H_{t-1}
      └─ lo NUEVO ─┘      └─ lo ANTERIOR ─┘
```

### Interpretacion (observacion de un estudiante que el profesor celebro):

- **Si z_t → 1:** H_t ≈ H_{t-1} → MANTIENE la memoria anterior
- **Si z_t → 0:** H_t ≈ H̃_t → ACTUALIZA con informacion nueva

### Por que GRU funciona en Copying Task

El profesor explico: **"Cada vez que ve el simbolo blanco, le dice: 'No, quedate con el hidden que tenias antes.' Eso lo aprendio."**

---

## D.4 Comparacion final

| Criterio | RNN Vanilla | LSTM | GRU |
|----------|-------------|------|-----|
| Memoria largo plazo | ❌ | ✓ | ✓ |
| Facilidad de entrenar | Media | Dificil | **Facil** |
| Parametros | Pocos | Muchos | **Medio** |
| Recomendacion profesor | No usar | Usar si necesario | **Usar primero** |

---

# SECCION E: ARQUITECTURAS AVANZADAS

## E.1 RNN Apiladas (Stacked)

Apilar varias capas de RNN:
```
X → [RNN Capa 1] → [RNN Capa 2] → [RNN Capa 3] → Salida
```

**Importante:** Cada capa tiene sus PROPIAS matrices (no comparten).

---

## E.2 RNN Bidireccionales

Procesar en ambas direcciones:
```
Forward:  →  →  →  → H_forward
Backward: ←  ←  ←  ← H_backward
```

Se combinan (concatenar o promediar).

**Cuando usarla:** Cuando ya tienes toda la secuencia disponible (ej: clasificar un electrocardiograma completo).

**Cuando NO usarla:** Cuando predices en tiempo real (seria "trampa" usar el futuro).

---

## E.3 Pipeline para clasificacion con RNN

```
1. EMBEDDING
   Convertir palabras en vectores (Word2Vec, GloVe, o aprender)

2. RNN/LSTM/GRU
   Procesar la secuencia → obtener H_1, H_2, ..., H_T

3. REPRESENTACION FINAL
   - Tomar el ultimo estado H_T, o
   - Promediar todos los estados, o
   - Agregacion ponderada (attention)

4. CLASIFICADOR (MLP)
   Pasar por red densa + softmax → probabilidades
```

**Recomendacion del profesor:** "Prueben con 2 o 3 capas de GRU."

---

# SECCION F: CONTEXTO HISTORICO

## F.1 Evolucion (linea de tiempo)

```
RNN Vanilla → LSTM/GRU → Attention → Transformers (ChatGPT)
   1990s        1997/2014    2014        2017
                    ↑
              ESTAMOS AQUI
              (esta clase)
```

**NOTA:** En esta clase (clase 9) aprendimos RNN, LSTM y GRU. Attention y Transformers se veran en clases 11 y 12.

## F.2 Neural Turing Machine (mencion historica)

Paper del 2014: Combina RNN con memoria externa (como la cinta de una maquina de Turing), pero diferenciable.

El profesor: **"No se que paso con la Neural Turing Machine despues, pero me parece espectacular."**

## F.3 ¿Y que viene despues de las RNN?

El profesor menciono que las RNN evolucionaron hacia Attention y Transformers:

> **"En algunas tareas concretas, una RNN bien entrenada puede tener mejor performance que Transformers."**

**¿Por que seguir aprendiendo RNN si existen Transformers?**
- Las RNN siguen siendo utiles para tareas especificas
- Requieren menos recursos computacionales
- Son mas adecuadas cuando no tienes millones de datos

**⏭️ ADELANTO (clases 11-12):** Veremos que los Transformers resuelven el problema de la paralelizacion, pero las RNN siguen siendo relevantes en ciertos contextos.

---

# SECCION G: TAREA PRACTICA - Double Descent

**NOTA:** Este tema es INDEPENDIENTE de RNN. Es una tarea practica sobre un fenomeno general de deep learning.

## G.1 Que es Double Descent

```
Error
  │
  │    ╱╲
  │   ╱  ╲    ╱
  │  ╱    ╲  ╱
  │ ╱      ╲╱
  │╱
  └──────────────────→ Complejidad del modelo
    │    │     │
    │    │     └── Zona "sobreparametrizada" (error baja de nuevo!)
    │    └──────── Interpolation threshold (pico)
    └───────────── Zona clasica (underfitting → overfitting)
```

**Lo sorprendente:** Despues del overfitting, si sigues aumentando la complejidad, el error VUELVE A BAJAR.

## G.2 Cuando ocurre

- Cuando: Parametros > Datos de entrenamiento
- "El interpolation threshold" es donde parametros ≈ datos

## G.3 La tarea

1. Dataset: Fashion MNIST "destruido" (4000 ejemplos, 40 features)
2. Modelo: MLP de 3 capas
3. Variar: `n_hidden` (2, 10, 26, 45, 76, 128, ...)
4. Guardar: SOLO el error final de la epoca 1000
5. Graficar: n_hidden vs error final
6. Repetir con ruido: 0%, 10%, 30%

**Tiempo de ejecucion:** ~30 minutos
**Fecha:** 17 de noviembre (flexible)

---

# SECCION H: RESUMEN EJECUTIVO

## Lo mas importante de cada tema

### RNN Vanilla
- Estado oculto H como memoria
- Tres matrices: U (entrada), V (recurrencia), W (salida)
- **Problema:** Vanishing gradient → no recuerda largo plazo

### LSTM
- Dos estados: Cell (largo plazo) + Hidden (trabajo)
- Cuatro compuertas: forget, input, cell candidate, output
- **Formula clave:** C_t = f_t ⊙ C_{t-1} + i_t ⊙ C̃_t

### GRU (RECOMENDADA)
- Un estado: solo Hidden
- Dos compuertas: reset, update
- **Formula clave:** H_t = (1-z_t) ⊙ H̃_t + z_t ⊙ H_{t-1}
- Menos parametros, mas facil de entrenar

### Cuando usar que (lo que sabemos hasta ahora)
- **GRU:** Primera opcion, probar con 2-3 capas
- **LSTM:** Si GRU no funciona bien
- **Transformers:** Se veran en clases 11-12 (cuando tienes muchos recursos y datos)

---

# SECCION I: INFORMACION ADMINISTRATIVA

| Item | Fecha | Detalles |
|------|-------|----------|
| Tarea Double Descent | 17 noviembre | ~30 min ejecucion |
| Cuestionario | 17 noviembre | 16 min, intentos ilimitados, CNN + Sobreparametrizacion |
| Parcial | 1 diciembre | Ultima clase antes: ejercicios |

---

# SECCION J: RECURSOS

1. **Curso de Hugging Face:** Modulo sobre RNN - "Estaba bastante bueno"
2. **Wikipedia:** Buenas figuras explicativas
3. **Libro de Deep Learning:** Capitulo sobre RNN (poco detallado segun el profesor)
