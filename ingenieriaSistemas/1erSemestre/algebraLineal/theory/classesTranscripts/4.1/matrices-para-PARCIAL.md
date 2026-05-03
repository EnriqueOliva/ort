# Matrices — Repaso completo para el PARCIAL

Este documento es el repaso del **módulo de matrices** para el parcial. Cubre todo lo que entra: definiciones, tipos, operaciones, traspuesta, traza, inversa, y los tipos especiales (simétrica, antisimétrica, idempotente, nilpotente, ortogonal). Después está el **práctico completo resuelto ejercicio por ejercicio** (V.1 a V.17 + VI.1 a VI.3 de evaluación), con las resoluciones oficiales de la cátedra. Al final hay una sección dedicada a estrategia de parcial: errores comunes que el profesor mencionó explícitamente, checklist, y resumen final.

Asumí que no fuiste a clase y que no te acordás de nada. Todo está explicado desde cero.

---

## ⚠️ Datos del parcial confirmados por el profesor

| Dato | Confirmación |
|------|--------------|
| **Fecha y hora** | Martes 5 de mayo de 2026, 19:30 |
| **Temas que entran** | 1) Matrices, 2) Determinantes, 3) Sistemas de ecuaciones |
| **Tema que NO entra** | Geometría del espacio (queda fuera, es para el segundo parcial) |
| **Formato típico** | Mayoría de ejercicios + alguna demostración teórica |
| **Tamaño de matrices esperable** | Hasta 5×5 con muchos ceros; nunca 10×10 (límite de tiempo) |

**Citas textuales del profesor confirmando esto:**

> "Va hasta el sistema de ecuaciones... lo hablé con la catedrática y con los otros profesores" *(clase 10, 22-abr)*

> "Primero parcial, les mandé ahí los temas por correo: matrices, determinantes, sistemas de ecuaciones; el miércoles retomamos con geometría" *(clase 12, 29-abr)*

> "El parcial, si bien tiene alguna demostración teórica, es resolver ejercicios" *(clase 1, 17-mar)*

**Sobre demostraciones específicamente:** todas las demos formales del módulo viven en el archivo aparte **`matrices-DEMOSTRACIONES.md`** (mismo folder), organizadas por sección con índice. Cuando una propiedad lleva el ícono 🟢 en este doc, hay una demo paso a paso esperándote en ese archivo.

---

## 🚦 Leyenda de prioridad para el parcial

Cada propiedad, teorema y ejercicio en este documento tiene un ícono que te dice **qué tipo de pregunta puede aparecer en parcial sobre ese contenido**. Es la guía de "¿cuánto debo estudiar esto y cómo?".

| Ícono | Significado | Qué hacer al estudiar |
|-------|-------------|------------------------|
| 🟢 | **Aparece en parcial Y se puede pedir su demostración.** Es decir, podría haber un ejercicio que diga literalmente *"demostrar que esta propiedad/teorema es cierto"*. | **PRIORIDAD MÁXIMA.** Memorizá la demo paso a paso hasta poder reproducirla en blanco. Esquema oficial: hipótesis → tesis → pasos justificados → $\blacksquare$. |
| 🟡 | **Aparece en parcial pero NO se va a pedir demostración** (porque no hay demo formal, o porque es una definición / "no propiedad" / contraejemplo / propiedad básica de aplicación). Te lo van a pedir como **V/F, justificación, citar al aplicarla, dar contraejemplo, etc.** | **PRIORIDAD ALTA.** Saberla bien. Saber cuándo aplicarla. Saber reconocerla en V/F. Pero no necesitás escribir una demo formal de ella. |
| 🔵 | **Ejercicio puramente computacional.** Procedimientos / cálculos directos sin componente teórica. | **PRIORIDAD MEDIA.** Practicar el procedimiento hasta que salga rápido y sin errores. Sin teoría — puro cálculo. |
| 🔴 | **NO entra al parcial.** El profesor lo descartó explícitamente. | **NO ESTUDIAR.** Solo V.17 y las propiedades formales de la matriz ortogonal cayeron acá. |

**Regla mnemotécnica para distinguir 🟢 de 🟡:**
> Preguntate: *"¿el profesor podría escribir como ejercicio del parcial 'demostrar que ...'?"*
> - Si SÍ → 🟢 (estudiá la demo).
> - Si NO (porque es definición, no propiedad, hecho básico que solo se aplica) → 🟡 (saberla, no demostrarla).

**Ejemplo de cada nivel:**
- 🟢 *"Demostrar que $(AB)^{-1} = B^{-1} A^{-1}$"* — el profesor PUEDE pedir esto literal.
- 🟡 *"El producto de matrices NO es conmutativo"* — tenés que saberlo y aplicarlo, pero no se demuestra (se da contraejemplo).
- 🔵 *"Calcular $A \cdot B$ donde A y B son las matrices..."* — puro cálculo.
- 🔴 *V.17 (opcional)* — no preocuparte.

Para la auditoría completa con citas de clase, ver **PARTE 8**.

---

## Mapa de lo que vamos a ver

| Parte | ¿Qué se aprende? |
|-------|-------------------|
| 1 | Qué es una matriz y notación básica |
| 2 | Tipos de matrices (cuadrada, triangular, diagonal, identidad, nula) |
| 3 | Suma, producto por escalar, producto entre matrices |
| 4 | Traspuesta, simétrica, antisimétrica, traza |
| 5 | Matriz inversa: concepto, método directo, propiedades |
| 6 | Tipos especiales: idempotente, nilpotente, ortogonal |
| 7 | **Práctico completo resuelto (V.1 a V.17 + VI.1 a VI.3)** |
| 8 | **Errores comunes que el profesor mencionó explícitamente** |
| 9 | **Resumen final imprescindible** |

📐 **Aparte:** las demostraciones formales viven en el archivo `matrices-DEMOSTRACIONES.md` (mismo folder). Acá vas a ver referencias del estilo *"demo en demos.md §B.2"* cuando aparezca una propiedad — el cuerpo de la demo está en ese archivo.

---

# PARTE 1 — ¿Qué es una matriz?

Una matriz es una **tabla rectangular de números reales** con un cierto número de filas y de columnas. Cada lugar de la tabla se llama **entrada** o **casillero**.

> **Analogía:** una planilla de Excel chiquita. Cada celda tiene una dirección única (fila, columna).

## Notación

$A \in \mathcal{M}_{m \times n}(\mathbb{R})$ significa: matriz $A$ con $m$ filas, $n$ columnas, entradas reales.

Cada entrada se nombra $a_{ij}$ donde:
- $i$ = fila (de arriba a abajo)
- $j$ = columna (de izquierda a derecha)

**El primer subíndice es siempre fila, el segundo es siempre columna. Nunca se invierte.**

**Ejemplo:**

$$A = \begin{pmatrix} 1 & 2 & -1 & 5 \\ 3 & -4 & 5 & 0 \\ -2 & 0 & 3 & 4 \end{pmatrix} \in \mathcal{M}_{3 \times 4}(\mathbb{R})$$

$a_{23} = 5$ (fila 2, col 3); $a_{11} = 1$ (esquina sup. izq.).

## Igualdad de matrices

$A = B$ si y solo si: (1) misma dimensión, (2) $a_{ij} = b_{ij}$ para todo $i, j$.

> **Uso típico en parcial:** "hallar $a, b, c, d$ tales que $A = B$". Igualás entrada por entrada y resolvés el sistema.

---

# PARTE 2 — Tipos de matrices

| Tipo | Forma | Condición | Ejemplo |
|------|-------|-----------|---------|
| **Fila** | $1 \times n$ | una sola fila | $\begin{pmatrix} 1 & 2 & 3 \end{pmatrix}$ |
| **Columna** | $m \times 1$ | una sola columna | $\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ |
| **Cuadrada** | $n \times n$ | $m = n$ | $\begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix}$ |
| **Triangular superior** | $n \times n$ | $a_{ij} = 0$ si $i > j$ (ceros debajo de la diagonal) | $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & -1 \\ 0 & 0 & 2 \end{pmatrix}$ |
| **Triangular inferior** | $n \times n$ | $a_{ij} = 0$ si $i < j$ (ceros encima de la diagonal) | $\begin{pmatrix} 1 & 0 & 0 \\ 2 & 4 & 0 \\ 3 & -1 & 2 \end{pmatrix}$ |
| **Diagonal** | $n \times n$ | $a_{ij} = 0$ si $i \neq j$ (triangular sup. **y** inf.) | $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 2 \end{pmatrix}$ |
| **Identidad** $\text{Id}$ | $n \times n$ | diagonal con todos $1$ | $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ |
| **Nula** $\mathcal{O}$ | $m \times n$ | todas las entradas son $0$ | $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$ |

## Diagonal principal

Los elementos $a_{ii}$ (fila = columna) forman la **diagonal principal**: $a_{11}, a_{22}, \ldots, a_{nn}$. Va de la esquina superior izquierda a la inferior derecha.

## Cosas importantes que tener internalizadas

- **Cuadrada importa porque:** inversa, traza, simetría, determinante, sistemas — todo eso requiere matriz cuadrada. Si no es cuadrada, no podés ni hablar de inversa.
- **Identidad $\text{Id}$ es el neutro del producto:** $A \cdot \text{Id} = \text{Id} \cdot A = A$. Analogía: el $1$ de los números.
- **Nula $\mathcal{O}$ es el neutro de la suma:** $A + \mathcal{O} = A$. Analogía: el $0$ de los números.

> "Siempre que hablamos de matriz inversa estamos en matrices cuadradas" — *el profesor*

---

# PARTE 3 — Operaciones con matrices

## Suma de matrices

**Definición.** Sumás entrada por entrada. Si $A = ((a_{ij}))$ y $B = ((b_{ij}))$, ambas $m \times n$:

$$(A + B)_{ij} = a_{ij} + b_{ij}$$

> **Cómo leer la fórmula:** la entrada en posición $(i,j)$ del resultado es la suma de las entradas en posición $(i,j)$ de $A$ y de $B$. No hay misterio: cada lugar se suma con su correspondiente.

**Requisito:** $A$ y $B$ deben tener la **misma dimensión**. Si no, no se pueden sumar (no hay con quién sumar la entrada faltante).

**Ejemplo paso a paso:**

$$\begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix} + \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}$$

Sumo entrada por entrada:
- Entrada $(1,1)$: $1 + 2 = 3$
- Entrada $(1,2)$: $2 + 1 = 3$
- Entrada $(2,1)$: $3 + 3 = 6$
- Entrada $(2,2)$: $-4 + 4 = 0$

$$= \begin{pmatrix} 3 & 3 \\ 6 & 0 \end{pmatrix}$$

### Propiedades

| Propiedad | Significado | Estado |
|-----------|-------------|--------|
| Cerradura | $m \times n$ + $m \times n$ = $m \times n$ | 🟡 saber/aplicar |
| Conmutativa | $A + B = B + A$ | 🟡 saber/aplicar |
| Asociativa | $(A + B) + C = A + (B + C)$ | 🟡 saber/aplicar |
| Neutro | $A + \mathcal{O} = A$ | 🟡 saber/aplicar |
| Opuesto | $A + (-A) = \mathcal{O}$ | 🟡 saber/aplicar |

> 🟡 **Saber/aplicar (no estudiar demo):** estas 5 son hechos básicos de cualquier suma. Tenés que aplicarlas con fluidez en despejes y manipulaciones, pero no se piden como demos.
>
> ⚠️ **OJO:** la suma SÍ es conmutativa. El **producto NO** es conmutativo — no las confundas.

---

## Producto por un escalar

**Definición.** "Escalar" = un número (real). Multiplicar una matriz por un escalar $k$ significa multiplicar **cada entrada** por $k$:

$$k \cdot A = ((k \cdot a_{ij}))$$

> **Cómo leer la fórmula:** la matriz resultante tiene las mismas dimensiones que $A$, y en cada posición $(i,j)$ está $k$ veces lo que estaba antes.

### Ejemplo paso a paso

Quiero calcular $2 \cdot A$ con $A = \begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix}$.

Multiplico cada entrada por $2$:
- Entrada $(1,1)$: $2 \cdot 1 = 2$
- Entrada $(1,2)$: $2 \cdot 2 = 4$
- Entrada $(2,1)$: $2 \cdot 3 = 6$
- Entrada $(2,2)$: $2 \cdot (-4) = -8$

$$2 \cdot \begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ 6 & -8 \end{pmatrix}$$

> **Notá la diferencia con la suma de matrices:** en la suma necesitás dos matrices del mismo tamaño. Acá necesitás un número y una matriz cualquiera — el escalar "se reparte" sobre cada entrada.

### Propiedades

| Propiedad | Significado | Estado parcial |
|-----------|-------------|---------------|
| $(\alpha \cdot \beta) \cdot A = \alpha \cdot (\beta \cdot A)$ | Asociativa de escalares | 🟡 saber/aplicar |
| $(\alpha + \beta) \cdot A = \alpha A + \beta A$ | Distributiva sobre suma de escalares | 🟡 saber/aplicar |
| $\alpha \cdot (A + B) = \alpha A + \alpha B$ | Distributiva sobre suma de matrices | 🟡 saber/aplicar |
| $1 \cdot A = A$ | El $1$ es neutro del escalar | 🟡 saber/aplicar |

---

## Producto de matrices

Es la operación más importante del módulo. Entendela bien.

### Conformabilidad (cuándo se puede multiplicar)

Para hacer $A \cdot B$: **el número de columnas de $A$ tiene que ser igual al número de filas de $B$**.

$$A \in \mathcal{M}_{m \times n}, \;\; B \in \mathcal{M}_{n \times p} \;\;\implies\;\; A \cdot B \in \mathcal{M}_{m \times p}$$

**Truco visual:** escribí las dimensiones una al lado de la otra: $(m \times \mathbf{n}) \cdot (\mathbf{n} \times p)$. Las del **medio** tienen que coincidir; las de **afuera** determinan el tamaño del resultado.

Si no coinciden, en ese orden no se puede; capaz en el otro orden ($B \cdot A$) sí — pero el resultado no es el mismo.

### Fórmula

$$c_{ik} = \sum_{j=1}^{n} a_{ij} \cdot b_{jk} \qquad\text{(fila $i$ de $A$ por columna $k$ de $B$)}$$

**En palabras:** para cada casillero del resultado, agarrás la fila correspondiente de $A$, la columna correspondiente de $B$, multiplicás par a par y sumás.

### Ejemplo paso a paso $2 \times 2$

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$$

Cada entrada del resultado:

| Entrada | Cálculo | Resultado |
|---------|---------|-----------|
| $(1,1)$ | fila 1 · col 1 = $1\cdot5 + 2\cdot7$ | $19$ |
| $(1,2)$ | fila 1 · col 2 = $1\cdot6 + 2\cdot8$ | $22$ |
| $(2,1)$ | fila 2 · col 1 = $3\cdot5 + 4\cdot7$ | $43$ |
| $(2,2)$ | fila 2 · col 2 = $3\cdot6 + 4\cdot8$ | $50$ |

$$A \cdot B = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

> **Idea para memorizar:** cada casillero = fila de $A$ × columna de $B$ (multiplicar par a par, sumar).

### Ejemplo $3 \times 3$ (mismo patrón, una suma de 3 pares)

$$A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \\ 2 & 0 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 0 & 2 \\ 3 & 1 & 0 \\ 0 & 2 & 1 \end{pmatrix}$$

Algunas entradas para que veas el patrón:

- $(1,1)$: $1\cdot1 + 2\cdot3 + 0\cdot0 = 7$
- $(2,2)$: $0\cdot0 + 1\cdot1 + 3\cdot2 = 7$
- $(3,3)$: $2\cdot2 + 0\cdot0 + 1\cdot1 = 5$

Calculando las 9:

$$A \cdot B = \begin{pmatrix} 7 & 2 & 2 \\ 3 & 7 & 3 \\ 2 & 2 & 5 \end{pmatrix}$$

> **Diferencia entre $2\times 2$ y $3\times 3$:** en el $2\times 2$ sumás 2 pares por entrada; en el $3\times 3$, 3 pares. La idea es la misma.

### Propiedades del producto

| Propiedad | Significado | Estado parcial |
|-----------|-------------|---------------|
| Asociativa | $(A \cdot B) \cdot C = A \cdot (B \cdot C)$ | 🟡 saber/aplicar |
| Distributiva por izquierda | $A \cdot (B + C) = A \cdot B + A \cdot C$ | 🟡 saber/aplicar |
| Distributiva por derecha | $(A + B) \cdot C = A \cdot C + B \cdot C$ | 🟡 saber/aplicar |
| Existencia de neutro | $A \cdot \text{Id} = \text{Id} \cdot A = A$ | 🟡 saber/aplicar |
| Escalar entre factores | $k \cdot (A \cdot B) = (k \cdot A) \cdot B = A \cdot (k \cdot B)$ | 🟡 saber/aplicar |

### 🟡 LO MÁS IMPORTANTE: el producto NO es conmutativo

> **Estado parcial: 🟡 SABER/APLICAR (NO se pide demostración).** Esto NO es un teorema con demo — es una **"no propiedad"** que se ilustra con un **contraejemplo**. El profesor dijo que es el error que más aparece en parciales: alumnos que asumen $AB = BA$ donde no corresponde. En parcial puede aparecer como pregunta V/F, justificar por qué NO, dar contraejemplo, o como trampa en un despeje. **No estudies una "demostración" — estudiá el contraejemplo y los casos donde sí conmutan ($A$ con $\text{Id}$, $A$ con $\mathcal{O}$, $A$ con $A^k$).**

> "Es un error común a su vez que A por B es igual a B por A. El producto de matrices no es conmutativo"

**Lo que esto significa:** en general, $A \cdot B \neq B \cdot A$. Capaz hasta uno de los dos productos no se puede hacer (por dimensiones). Y aun cuando los dos se puedan hacer y el resultado tenga la misma dimensión, dan matrices distintas.

**Contraejemplo (memorizalo):**

$$A = \begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix}, \quad B = \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}$$

$$A \cdot B = \begin{pmatrix} 8 & 9 \\ -6 & -13 \end{pmatrix} \neq \begin{pmatrix} 5 & 0 \\ 15 & -10 \end{pmatrix} = B \cdot A$$

> "Es tentador, ¿no?" *(el profesor cuando un alumno aplica conmutativa donde no corresponde)*

**Esto NO quiere decir que NUNCA conmuten.** Algunas matrices sí conmutan (por ejemplo, $A$ con $\text{Id}$ siempre, $A$ con $\mathcal{O}$ siempre, $A$ con $A^k$ siempre). Pero no se puede asumir que conmuten — hay que probarlo.

> "La verdad que en ningún parcial aparece que asume que conmuta y cuando no, no es así"

**Traducción:** el profesor confirma que en el parcial siempre aparece este tema. Tenés que estar atento.

### Casos donde sí conmutan

- $A$ con $A$ y con cualquier potencia $A^k$
- $A$ con $\text{Id}$ (conmuta con cualquier matriz cuadrada de la misma dimensión)
- $A$ con la nula $\mathcal{O}$
- $A$ con $A^{-1}$ (cuando existe)
- $A$ con $\alpha \cdot \text{Id}$ para cualquier escalar $\alpha$

---

## 🟢 Producto por vectores canónicos

> **Estado parcial: 🟢 SE PIDE.** El profesor lo demostró en clase 2; aparece como ejercicio V.3 del práctico. Es un atajo que ahorra mucho tiempo. **Demo en `matrices-DEMOSTRACIONES.md` §A.1.**

### Qué son

Olvidate del nombre. Son **vectores columna con un solo $1$ y el resto ceros**:

$$\vec{v}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{v}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

El subíndice te dice **dónde está el $1$**. Eso es todo.

> **Analogía:** son botones numerados. Cuando apretás $\vec{v}_j$ contra una matriz, te devuelve la columna $j$.

### El truco con un ejemplo

Tomá $A = \begin{pmatrix} 4 & 7 & 9 \\ 5 & 8 & 1 \\ 6 & 2 & 3 \end{pmatrix}$. Multipliquemos por $\vec{v}_1$:

$$A \cdot \vec{v}_1 = \begin{pmatrix} 4 \cdot 1 + 7 \cdot 0 + 9 \cdot 0 \\ 5 \cdot 1 + 8 \cdot 0 + 1 \cdot 0 \\ 6 \cdot 1 + 2 \cdot 0 + 3 \cdot 0 \end{pmatrix} = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix} = \text{columna 1 de } A$$

**¿Por qué?** El $1$ del $\vec{v}_1$ está en posición $1$, así que en cada fila de $A$ solo sobrevive el primer número — los otros dos los borra el $0$.

**Análogamente:** $A \cdot \vec{v}_2 = \text{col 2}$ y $A \cdot \vec{v}_3 = \text{col 3}$.

### El truco en una frase

> **Multiplicar $A$ por $\vec{v}_j$ te devuelve la columna $j$ de $A$. Punto.**

| Si multiplicás por... | Te quedás con... |
|---|---|
| $\vec{v}_1$ (el $1$ arriba) | la columna 1 de $A$ |
| $\vec{v}_2$ (el $1$ en el medio) | la columna 2 de $A$ |
| $\vec{v}_3$ (el $1$ abajo) | la columna 3 de $A$ |

**Por qué funciona, en criollo:** los ceros del vector canónico **borran** todos los números de la fila menos uno. El único número que sobrevive es el que está justo donde el vector tiene el $1$. Como eso pasa en las tres filas, el resultado termina siendo exactamente la columna que apuntaste.

### ¿Para qué sirve esto?

1. Si en un parcial te piden "encontrá la columna 2 de $A \cdot B$", **no necesitás calcular toda la matriz $A \cdot B$**. Te alcanza con calcular $A \cdot B \cdot \vec{v}_2$, que es la columna 2.
2. Te ahorra tiempo y cuentas.
3. **Aparece en el ejercicio V.3 del práctico.**

### Si querés ver la versión con letras (opcional)

Si en vez de los números $4, 7, 9, \ldots$ ponés letras genéricas:

$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$$

el mismo truco da:

$$A \cdot \vec{v}_1 = \begin{pmatrix} a_{11} \\ a_{21} \\ a_{31} \end{pmatrix} \;\text{(col 1)}, \quad A \cdot \vec{v}_2 = \begin{pmatrix} a_{12} \\ a_{22} \\ a_{32} \end{pmatrix} \;\text{(col 2)}, \quad A \cdot \vec{v}_3 = \begin{pmatrix} a_{13} \\ a_{23} \\ a_{33} \end{pmatrix} \;\text{(col 3)}$$

Es **lo mismo** que el ejemplo numérico, solo que ahora cada número está disfrazado de $a_{ij}$. Si te confunde la versión con letras, ignorala — alcanza con que entiendas la versión con números.

---

# PARTE 4 — Traspuesta y traza

## Matriz traspuesta

**Definición.** $A^T$ se obtiene **intercambiando filas por columnas**.

> **En palabras:** la fila 1 de $A^T$ es la columna 1 de $A$, la fila 2 de $A^T$ es la columna 2 de $A$, etc. Es como "girar" la matriz por la diagonal.

Formalmente: si $A = ((a_{ij}))$, entonces $A^T = ((a_{ji}))$ (los subíndices se intercambian).

**Cambio de dimensión:** si $A$ es $m \times n$, $A^T$ es $n \times m$ (las dimensiones se invierten).

**Ejemplo paso a paso:**

$$A = \begin{pmatrix} 1 & 2 \\ 3 & -4 \\ 2 & 1 \end{pmatrix}$$

$A$ tiene 3 filas y 2 columnas (es $3 \times 2$). Entonces $A^T$ tendrá 2 filas y 3 columnas ($2 \times 3$).

Construyo $A^T$:
- **Fila 1 de $A^T$** = columna 1 de $A$ = $(1, 3, 2)$
- **Fila 2 de $A^T$** = columna 2 de $A$ = $(2, -4, 1)$

$$A^T = \begin{pmatrix} 1 & 3 & 2 \\ 2 & -4 & 1 \end{pmatrix}$$

> **Verificación rápida:** la entrada $(2,3)$ de $A^T$ debería ser la entrada $(3,2)$ de $A$. En $A^T$ vemos $1$ en posición $(2,3)$. En $A$ vemos $1$ en posición $(3,2)$. ✓

### Las 4 propiedades de la traspuesta (las 4 son demo pedible)

| # | Propiedad | Comentario | Estado parcial | Demo |
|---|-----------|-----------|---------------|------|
| 1 | $(A^T)^T = A$ | Trasponer dos veces vuelve al original | 🟢 SE PIDE | demos.md §B.1 |
| 2 | $(A + B)^T = A^T + B^T$ | Traspuesta de suma = suma de traspuestas | 🟢 SE PIDE | demos.md §B.2 |
| 3 | $(\alpha A)^T = \alpha A^T$ | Los escalares no se afectan | 🟢 SE PIDE | demos.md §B.3 |
| 4 | $(A B)^T = B^T A^T$ | **EL ORDEN SE INVIERTE** | 🟢 SE PIDE | demos.md §B.4 |

> 🟢 **Las 4 son demo pedible.** El profesor dijo en clase 2: *"vamos a ver cuatro propiedades que tenemos que manejar"*. Demostró la 2 y la 3 como modelo. **Cualquiera puede aparecer como ejercicio "demostrar que..."**. Las demos paso a paso están en `matrices-DEMOSTRACIONES.md` §B.

### El error común en la propiedad 4

> "El producto de matrices no es conmutativo, así que no podemos escribir $A^T \cdot B^T$. Tiene que ser $B^T \cdot A^T$, con el orden cambiado"

**Por qué se invierte el orden:** porque las matrices no conmutan. Si escribieras $(AB)^T = A^T B^T$, las dimensiones ni siquiera dejarían: si $A$ es $2 \times 3$ y $B$ es $3 \times 4$, entonces $A^T$ es $3 \times 2$ y $B^T$ es $4 \times 3$, no se pueden multiplicar. $B^T A^T$ sí.

---

## Matriz simétrica y antisimétrica

### Definiciones

- **Simétrica 🟡:** $A^T = A$. Lo que está arriba de la diagonal es **igual** a lo que está abajo (en posiciones espejo).
- **Antisimétrica 🟡:** $A^T = -A$. Lo que está arriba de la diagonal es el **opuesto** de lo que está abajo. Y la **diagonal es siempre nula**.

> **Por qué la diagonal de una antisimétrica es nula:** la condición $A^T = -A$ aplicada a la diagonal dice $a_{ii} = -a_{ii}$. El único número que es igual a su opuesto es el $0$, así que cada entrada de la diagonal forzosamente es $0$.

### Ejemplo de simétrica

$$A = \begin{pmatrix} 1 & 3 & 2 \\ 3 & -4 & 1 \\ 2 & 1 & 2 \end{pmatrix}$$

Verifico que $a_{ij} = a_{ji}$ en las posiciones que no son diagonales:
- $a_{12} = 3$ y $a_{21} = 3$ ✓ (iguales)
- $a_{13} = 2$ y $a_{31} = 2$ ✓
- $a_{23} = 1$ y $a_{32} = 1$ ✓

> **Truco visual:** imaginá un espejo en la diagonal. Los números arriba se reflejan iguales abajo.

### Ejemplo de antisimétrica

$$A = \begin{pmatrix} 0 & 3 & -2 \\ -3 & 0 & 1 \\ 2 & -1 & 0 \end{pmatrix}$$

Verifico:
- **Diagonal nula:** $a_{11} = a_{22} = a_{33} = 0$ ✓
- $a_{12} = 3$ y $a_{21} = -3$, opuestos ✓
- $a_{13} = -2$ y $a_{31} = 2$, opuestos ✓
- $a_{23} = 1$ y $a_{32} = -1$, opuestos ✓

---

## Propiedades de simétricas y antisimétricas

| # | Propiedad | Estado parcial | Demo |
|---|-----------|---------------|------|
| 1 | La suma de dos simétricas es simétrica | 🟢 SE PIDE | demos.md §C.1 |
| 2 | La suma de dos antisimétricas es antisimétrica | 🟢 SE PIDE | análoga a §C.1 (en demos.md) |
| 3 | $\alpha A$ es simétrica si $A$ lo es | 🟢 SE PIDE | demos.md §C.2 |
| 4 | $\alpha A$ es antisimétrica si $A$ lo es | 🟢 SE PIDE | análoga a §C.2 (en demos.md) |

> 🟢 **Las 4 son demo pedible.** El profesor dijo en clase 2: *"vamos a denunciar cuatro propiedades del estilo y vamos a demostrar alguna de ellas"*. Demostró la 1 entera; las otras 3 las dejó como análogas.

### Resultados clave que el profesor demostró en clase

| Resultado | Estado | Demo |
|-----------|--------|------|
| **$AB$ simétrica $\iff AB = BA$** (con $A, B$ simétricas) — V.5.2 | 🟢 SE PIDE | demos.md §C.3 |
| **$\frac{1}{2}(A + A^T)$ es simétrica** — V.6.1 | 🟢 SE PIDE | demos.md §C.4 |
| **$\frac{1}{2}(A - A^T)$ es antisimétrica** — V.6.2 | 🟢 SE PIDE | demos.md §C.5 |
| **Toda matriz cuadrada $A = $ sim $+$ antisim** — V.6.3 | 🟢 SE PIDE | demos.md §C.6 |

---

## Traza de una matriz

**Definición.** La traza de una matriz cuadrada $A$ es **la suma de los elementos de la diagonal principal**.

$$tr(A) = \sum_{i=1}^{n} a_{ii} = a_{11} + a_{22} + a_{33} + \cdots + a_{nn}$$

> **Cómo leer la fórmula:** $tr(A)$ es un **número** (no una matriz). Sumás solamente las entradas $a_{ii}$ donde fila e índice columna coinciden — la diagonal de la esquina superior izquierda a la inferior derecha.

**Requisito:** $A$ debe ser **cuadrada** (si no, no hay diagonal bien definida).

**Ejemplo paso a paso:**

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 3 & -4 & 2 \\ 2 & 1 & 10 \end{pmatrix}$$

Identifico la diagonal: $a_{11} = 1$, $a_{22} = -4$, $a_{33} = 10$.

Sumo:

$$tr(A) = 1 + (-4) + 10 = 7$$

> **Notá:** los números fuera de la diagonal ($2, 3, 1$, etc.) **no se usan** para la traza. Solo importa la diagonal.

### Las 4 propiedades de la traza (las 4 son demo pedible)

| # | Propiedad | Comentario | Estado | Demo |
|---|-----------|-----------|--------|------|
| 1 | $tr(A + B) = tr(A) + tr(B)$ | Distribuye sobre la suma | 🟢 SE PIDE | demos.md §D.1 |
| 2 | $tr(\alpha A) = \alpha \cdot tr(A)$ | Los escalares salen | 🟢 SE PIDE | demos.md §D.2 |
| 3 | $tr(A^T) = tr(A)$ | La traspuesta no cambia la diagonal | 🟢 SE PIDE | demos.md §D.3 |
| 4 | $tr(AB) = tr(BA)$ | **¡Aunque $AB \neq BA$, sus trazas coinciden!** | 🟢 SE PIDE | demos.md §D.4 |
| corolario | $tr(A - B) = tr(A) - tr(B)$ | Sale combinando 1 y 2 | 🟢 SE PIDE | demos.md §D.5 |

> 🟢 **Las 4 son demo pedible.** El profesor dijo: *"al igual que las traspuestas son 4 propiedades que tenemos que manejar"* (clase 2). Demostró la 1 entera con sumatorias. La 4 es la base de la aplicación estrella (abajo).

> "A por B es una matriz, B por A es otra, pero sumo las diagonales principales y me da lo mismo. Es algo bastante curioso"

### Por qué la propiedad 4 es importante

Aunque el producto **no conmuta**, la **traza del producto sí**. Esta propiedad permite probar cosas que de otro modo no se podrían — la más célebre, abajo.

### 🟢 Aplicación estrella: NO existen $A, B$ tales que $AB - BA = \text{Id}$

> **Estado parcial: 🟢 SE PIDE.** Es **la demo más probable del módulo de traza**. El profesor la hizo completa en clase 3 por absurdo. **Demo paso a paso en `matrices-DEMOSTRACIONES.md` §D.6.**

**Idea de la demo:** suponé que existen, tomá traza a ambos lados. El lado izquierdo da $0$ (porque $tr(AB) = tr(BA)$), el lado derecho da $n \geq 1$. Absurdo.

---

# PARTE 5 — Matriz inversa

Esta parte es la más cargada del módulo. Mucho cae en parcial.

## Definición

$A$ cuadrada es **invertible** si existe $B$ ($n \times n$) tal que:

$$A \cdot B = B \cdot A = \text{Id}$$

Esa $B$ se llama **inversa de $A$** y se nota $A^{-1}$.

**Lo importante:**
- Solo existe para matrices **cuadradas**.
- **No** todas las cuadradas son invertibles (ej: la nula, o cualquiera con dos filas proporcionales).
- Cuando existe, es **única**.
- $A$ y $A^{-1}$ **sí conmutan entre sí** (esto es notable porque las matrices en general no conmutan).
- $A^{-1}$ **NO es** "$\frac{1}{A}$". **No existe la división de matrices** — solo se puede multiplicar por la inversa.

> **Analogía:** $A \cdot A^{-1} = \text{Id}$ es el análogo de $5 \cdot \frac{1}{5} = 1$ en los números reales.

---

## Método directo para hallar la inversa

Es el método clásico. Funciona siempre, pero para matrices grandes (3x3 o más) es lento. Para 2x2 es perfecto.

### Pasos

1. **Plantear** $A \cdot B = \text{Id}$, donde $B$ es una matriz genérica con incógnitas: $B = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ (para 2x2).
2. **Hacer la multiplicación** $A \cdot B$ y dejarla en términos de las incógnitas.
3. **Igualar entrada por entrada** a las entradas de la identidad. Te queda un sistema de ecuaciones (4 ecuaciones, 4 incógnitas en el caso 2x2).
4. **Resolver el sistema.** Si tiene solución única, esa solución es la inversa. Si no tiene solución, la matriz **no es invertible**.

### Ejemplo: hallar la inversa de $A = \begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix}$

**Paso 1 — Plantear la incógnita.** Busco una matriz $B$ del mismo tamaño que $A$ ($2 \times 2$) tal que $A \cdot B = \text{Id}$. Llamo a las entradas de $B$ con letras:

$$B = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

> **Por qué uso letras:** porque $B$ es desconocida. Las letras $a, b, c, d$ son las **incógnitas** que voy a despejar.

**Paso 2 — Multiplicar $A \cdot B$ entrada por entrada.** Aplico fila × columna en cada una de las 4 entradas:

- Entrada $(1,1)$: fila 1 de $A$ por col 1 de $B$ = $1 \cdot a + 2 \cdot c = a + 2c$
- Entrada $(1,2)$: fila 1 por col 2 = $1 \cdot b + 2 \cdot d = b + 2d$
- Entrada $(2,1)$: fila 2 por col 1 = $3 \cdot a + (-4) \cdot c = 3a - 4c$
- Entrada $(2,2)$: fila 2 por col 2 = $3 \cdot b + (-4) \cdot d = 3b - 4d$

Quedando:

$$A \cdot B = \begin{pmatrix} a + 2c & b + 2d \\ 3a - 4c & 3b - 4d \end{pmatrix}$$

**Paso 3 — Igualar a la identidad.** Como queremos $A \cdot B = \text{Id}$:

$$\begin{pmatrix} a + 2c & b + 2d \\ 3a - 4c & 3b - 4d \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

Dos matrices son iguales si lo son entrada por entrada, así que esto se traduce en 4 ecuaciones:

$$\begin{cases} a + 2c = 1 \quad \text{(de la entrada (1,1))} \\ b + 2d = 0 \quad \text{(de la (1,2))} \\ 3a - 4c = 0 \quad \text{(de la (2,1))} \\ 3b - 4d = 1 \quad \text{(de la (2,2))} \end{cases}$$

> **Notá:** las ecuaciones se separan en dos parejas independientes. Las que tienen $a, c$ (1ra y 3ra) y las que tienen $b, d$ (2da y 4ta). Las resuelvo por separado.

**Paso 4 — Resolver para $a$ y $c$ (ecuaciones 1 y 3).**

$$\begin{cases} a + 2c = 1 \\ 3a - 4c = 0 \end{cases}$$

Multiplico la primera ecuación por $2$ para que el coeficiente de $c$ sea $4$:

$$2a + 4c = 2$$

Ahora sumo con la segunda ($3a - 4c = 0$). Los términos en $c$ se cancelan:

$$2a + 3a + 4c - 4c = 2 + 0$$
$$5a = 2 \implies a = \tfrac{2}{5}$$

Vuelvo a la primera ecuación con $a = \frac{2}{5}$:

$$\tfrac{2}{5} + 2c = 1 \implies 2c = 1 - \tfrac{2}{5} = \tfrac{3}{5} \implies c = \tfrac{3}{10}$$

**Paso 5 — Resolver para $b$ y $d$ (ecuaciones 2 y 4).**

$$\begin{cases} b + 2d = 0 \\ 3b - 4d = 1 \end{cases}$$

De la primera: $b = -2d$. Sustituyo en la segunda:

$$3(-2d) - 4d = 1 \implies -6d - 4d = 1 \implies -10d = 1 \implies d = -\tfrac{1}{10}$$

Y vuelvo a $b = -2d = -2 \cdot (-\frac{1}{10}) = \frac{2}{10} = \frac{1}{5}$.

**Paso 6 — Armar la inversa.**

$$\boxed{A^{-1} = \begin{pmatrix} 2/5 & 1/5 \\ 3/10 & -1/10 \end{pmatrix}}$$

**Paso 7 — Verificar (opcional pero recomendable).** Multiplicá $A \cdot A^{-1}$ y debería dar $\text{Id}$. Por ejemplo, entrada $(1,1)$: $1 \cdot \frac{2}{5} + 2 \cdot \frac{3}{10} = \frac{2}{5} + \frac{6}{10} = \frac{4}{10} + \frac{6}{10} = 1$ ✓

### Cuando NO es invertible

Si al armar el sistema queda **incompatible** (sin solución), la matriz no tiene inversa.

**Ejemplo:** $C = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.

Planteando $C \cdot B = \text{Id}$ y sacando las dos primeras ecuaciones (las que involucran $a$ y $c$):

$$\begin{cases} a + 2c = 1 \quad \text{(de entrada (1,1) = 1)} \\ 2a + 4c = 0 \quad \text{(de entrada (2,1) = 0)} \end{cases}$$

> **Mirá la trampa:** la segunda ecuación es exactamente $2$ veces la primera del lado izquierdo. Si la primera dice $a + 2c = 1$, multiplicada por $2$ daría $2a + 4c = 2$. Pero la ecuación dada es $2a + 4c = 0$. **Contradicción:** una misma cosa ($2a + 4c$) no puede valer $2$ y $0$ al mismo tiempo.

Por lo tanto el sistema es **incompatible** — no existe $a, c$ que cumpla ambas. **$C$ no es invertible.**

**Pista visual rápida:** la fila 2 de $C$ es $2$ veces la fila 1. Cuando una fila es múltiplo de otra, la matriz nunca es invertible.

---

## Las 4 propiedades de la inversa (las 4 son demo pedible)

| # | Propiedad | Comentario | Estado | Demo |
|---|-----------|-----------|--------|------|
| 1 | $(A^{-1})^{-1} = A$ | Invertir dos veces vuelve al original | 🟢 SE PIDE | demos.md §E.1 |
| 2 | $(AB)^{-1} = B^{-1} A^{-1}$ | **EL ORDEN SE INVIERTE** | 🟢 SE PIDE | demos.md §E.2 |
| 3 | $(\alpha A)^{-1} = \frac{1}{\alpha} A^{-1}$, $\alpha \neq 0$ | El escalar se invierte | 🟢 SE PIDE | demos.md §E.3 |
| 4 | $(A^T)^{-1} = (A^{-1})^T$ | Inversa de la traspuesta = traspuesta de la inversa | 🟢 SE PIDE | demos.md §E.4 |

> 🟢 **Las 4 son demo pedible.** El profesor dijo: *"vamos a ver ahora las propiedades de la inversa, algunas que tenemos que manejar y vamos a demostrar algunas de ellas"* (clase 3). Demostró la 2 entera en pizarrón. Las otras 3 salen verificando que el "candidato" multiplicado da $\text{Id}$.

### Por qué se invierte el orden en $(AB)^{-1} = B^{-1} A^{-1}$

Mismo motivo que la traspuesta: como las matrices no conmutan, no podés escribir $A^{-1} B^{-1}$. **Analogía:** si me pongo medias y zapatos (en ese orden), para sacármelos hago el orden inverso — zapatos primero, después medias. Lo último que entró es lo primero que sale.

> "No podés mover el A inversa... acuerdate que no conmuta, no podés cambiar el orden"

---

## Despeje de ecuaciones matriciales

**Regla de oro:** no existe división. Para "pasar" una matriz al otro lado, multiplicás por su inversa **del mismo lado en ambos miembros**.

### Ejemplo paso a paso: despejar $X$ de $A \cdot X = B$ (con $A$ invertible)

**Paso 1 — Identificar la incógnita y su posición.** $X$ es lo que querés despejar. Está a la **derecha** de $A$, multiplicada a izquierda por $A$.

**Paso 2 — Elegir el lado por el que multiplicar $A^{-1}$.** Como $A$ está a izquierda de $X$, multiplico por $A^{-1}$ a izquierda en ambos lados de la ecuación:

$$A \cdot X = B \quad\Longrightarrow\quad A^{-1} \cdot (A \cdot X) = A^{-1} \cdot B$$

**Paso 3 — Reagrupar usando asociativa.** Muevo paréntesis:

$$(A^{-1} \cdot A) \cdot X = A^{-1} \cdot B$$

**Paso 4 — Aplicar $A^{-1} \cdot A = \text{Id}$.**

$$\text{Id} \cdot X = A^{-1} \cdot B$$

**Paso 5 — Aplicar $\text{Id} \cdot X = X$.**

$$\boxed{X = A^{-1} \cdot B}$$

> **Importante:** $A^{-1}$ tiene que ir **a la izquierda** de $B$, NO a la derecha. Si pusieras $X = B \cdot A^{-1}$ estarías equivocado, porque las matrices no conmutan.

### Tabla de los 3 casos típicos

| Ecuación | Despejás $X$ así... | Razón |
|----------|---------------------|-------|
| $A \cdot X = B$, $A$ invertible | $X = A^{-1} \cdot B$ | Multiplicás por $A^{-1}$ **a izquierda** porque $A$ estaba a izquierda. |
| $X \cdot A = B$, $A$ invertible | $X = B \cdot A^{-1}$ | Multiplicás por $A^{-1}$ **a derecha** porque $A$ estaba a derecha. |
| $A \cdot X + X = B$ | $X = (A + \text{Id})^{-1} \cdot B$ | Factorizás $X$: $(A + \text{Id}) X = B$, después multiplicás por $(A+\text{Id})^{-1}$ a izquierda (asumiendo que existe). |

### Errores típicos del parcial

1. **Mover $A^{-1}$ al lado equivocado.** Si $A$ estaba a izquierda de $X$, $A^{-1}$ va a izquierda. No podés saltar al otro lado porque las matrices no conmutan.
2. **Factorizar $AX + X$ como $(A+1)X$.** "$1$" es un número, $A$ es una matriz — no se suman. Lo correcto es escribir $X = \text{Id} \cdot X$ explícitamente, y entonces $AX + X = AX + \text{Id} \cdot X = (A + \text{Id}) X$.

---

# PARTE 6 — Tipos especiales de matrices

## Matriz idempotente

### Definición 🟡

> **Estado parcial: 🟡 saber/aplicar.** La definición no se demuestra (es definición), pero tenés que reconocer si una matriz es idempotente para usarla en ejercicios.

Una matriz cuadrada $A$ es **idempotente** si $A^2 = A$.

> **En palabras:** multiplicarla por sí misma da la misma matriz. Es como un número que es igual a su propio cuadrado — los únicos números así son $0$ y $1$. Pero con matrices hay más posibilidades.
>
> **Consecuencia útil:** si $A^2 = A$, entonces $A^3 = A \cdot A^2 = A \cdot A = A^2 = A$. Y por inducción, $A^k = A$ para todo $k \geq 1$.

### Ejemplos

**Ejemplo 1 — la identidad.** $\text{Id}^2 = \text{Id} \cdot \text{Id} = \text{Id}$ (multiplicar por la identidad nunca cambia nada). ✓ Es idempotente.

**Ejemplo 2 — la nula.** $\mathcal{O}^2 = \mathcal{O} \cdot \mathcal{O} = \mathcal{O}$ (cualquier producto que tenga la nula da la nula). ✓ Es idempotente.

**Ejemplo 3 — una matriz "interesante".** $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.

Calculo $A^2$ entrada por entrada:
- $(1,1)$: $1 \cdot 1 + 0 \cdot 0 = 1$
- $(1,2)$: $1 \cdot 0 + 0 \cdot 0 = 0$
- $(2,1)$: $0 \cdot 1 + 0 \cdot 0 = 0$
- $(2,2)$: $0 \cdot 0 + 0 \cdot 0 = 0$

$$A^2 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = A \quad \checkmark$$

Es idempotente. Y **no** es ni la identidad ni la nula — esto demuestra que hay matrices idempotentes "no triviales".

### Resultados clave que el profesor demostró sobre idempotente

| Resultado | Estado | Demo |
|-----------|--------|------|
| **Idempotente $+$ invertible $\Rightarrow A = \text{Id}$** (V.I.2) | 🟢 SE PIDE | demos.md §F.1 |
| **Si $A$ idempotente, $(A + \text{Id})^3 = \text{Id} + 7A$** | 🟢 SE PIDE | demos.md §F.2 |

> **Cuidado:** "idempotente $\Rightarrow \text{Id}$" SOLO vale si además es invertible. Hay idempotentes no invertibles (la nula, $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$) que no son $\text{Id}$.

---

## Matriz nilpotente

### Definición 🟡

> **Estado parcial: 🟡 saber/aplicar.** Definición — no se demuestra.

Una matriz cuadrada $A$ es **nilpotente de grado $k$** si:
1. $A^k = \mathcal{O}$ (alguna potencia da la nula)
2. $A^{k-1} \neq \mathcal{O}$ (la potencia inmediatamente anterior NO da la nula)

Es decir, $k$ es la **primera** potencia que la anula. Si la primera potencia que la anula es $A^3$, decimos que es nilpotente de grado $3$.

### Resultado clave de nilpotente

| Resultado | Estado | Demo |
|-----------|--------|------|
| **$P^{-1} A P$ es nilpotente del mismo grado que $A$** (V.7.2) | 🟢 SE PIDE | demos.md §F.3 |

> **Idea clave:** $B^k = (P^{-1} A P)^k = P^{-1} A^k P = \mathcal{O}$ (los $PP^{-1}$ del medio se cancelan). Para probar que el grado es exactamente $k$, hay un argumento por absurdo. Demo completa en demos.md §F.3.

---

## Matriz ortogonal

### Definición 🟡

> **Estado parcial: 🟡 saber/aplicar.** Definición — no se demuestra. ⚠️ Las **propiedades formales** de matriz ortogonal NO entran al parcial (🔴) — el profesor dijo *"esto es ortogonal, no lo vimos en el teórico"* (clase 4). Sí entran ejercicios que la apliquen (V.12).

Una matriz cuadrada $A$ es **ortogonal** si y solo si $A$ es invertible y $A^{-1} = A^T$.

**Equivalentemente:** $A \cdot A^T = A^T \cdot A = \text{Id}$.


---

# PARTE 7 — PRÁCTICO COMPLETO RESUELTO

Esta es la sección más importante para el parcial. Acá están todos los ejercicios del práctico oficial (V.1 a V.17, más VI.1 a VI.3 de evaluación) **resueltos paso a paso, con la resolución oficial de la cátedra**. Si entendés cómo se resuelven estos, tenés cubierto el parcial.

---

## 🔵 Ejercicio V.1 — Operaciones básicas

**Enunciado.** Dadas las matrices:

$$A = \begin{pmatrix} 2 & -1 & 4 \\ 1 & 0 & 6 \\ 1 & -1 & 2 \end{pmatrix}, \quad B = \begin{pmatrix} 0 & 0 & 1 \\ 3 & 0 & 5 \\ 3 & -2 & 0 \end{pmatrix}, \quad C = \begin{pmatrix} 1 & 1 & 2 \\ -2 & 4 & 0 \\ 0 & 5 & -1 \end{pmatrix}$$

1. Calcular: (i) $A - 2B$, (ii) $3A - C$, (iii) $A + B + C$.
2. Encontrar $D$ tal que $A + B + C + D = \mathcal{O}_{3 \times 3}$.

### Solución

#### (i) $A - 2B$

**Paso 1 — Calcular $2B$ (escalar por matriz).** Multiplicás cada entrada de $B$ por $2$:

$$2B = \begin{pmatrix} 0 \cdot 2 & 0 \cdot 2 & 1 \cdot 2 \\ 3 \cdot 2 & 0 \cdot 2 & 5 \cdot 2 \\ 3 \cdot 2 & -2 \cdot 2 & 0 \cdot 2 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 2 \\ 6 & 0 & 10 \\ 6 & -4 & 0 \end{pmatrix}$$

**Paso 2 — Restar entrada por entrada.** $A - 2B$ es la matriz cuya entrada $(i,j)$ es $a_{ij} - (2B)_{ij}$:

$$A - 2B = \begin{pmatrix} 2-0 & -1-0 & 4-2 \\ 1-6 & 0-0 & 6-10 \\ 1-6 & -1-(-4) & 2-0 \end{pmatrix} = \begin{pmatrix} 2 & -1 & 2 \\ -5 & 0 & -4 \\ -5 & 3 & 2 \end{pmatrix}$$

> **Detalle de $(3,2)$:** $-1 - (-4) = -1 + 4 = 3$. Restar un negativo es sumar.

#### (ii) $3A - C$

**Paso 1 — Calcular $3A$.**

$$3A = \begin{pmatrix} 6 & -3 & 12 \\ 3 & 0 & 18 \\ 3 & -3 & 6 \end{pmatrix}$$

**Paso 2 — Restar $C$.** Entrada por entrada $3a_{ij} - c_{ij}$:

$$3A - C = \begin{pmatrix} 6-1 & -3-1 & 12-2 \\ 3-(-2) & 0-4 & 18-0 \\ 3-0 & -3-5 & 6-(-1) \end{pmatrix} = \begin{pmatrix} 5 & -4 & 10 \\ 5 & -4 & 18 \\ 3 & -8 & 7 \end{pmatrix}$$

#### (iii) $A + B + C$

Sumás las tres entrada por entrada. Por ejemplo, entrada $(1,1)$: $2 + 0 + 1 = 3$. Entrada $(2,3)$: $6 + 5 + 0 = 11$.

$$A + B + C = \begin{pmatrix} 2+0+1 & -1+0+1 & 4+1+2 \\ 1+3+(-2) & 0+0+4 & 6+5+0 \\ 1+3+0 & -1+(-2)+5 & 2+0+(-1) \end{pmatrix} = \begin{pmatrix} 3 & 0 & 7 \\ 2 & 4 & 11 \\ 4 & 2 & 1 \end{pmatrix}$$

#### Parte 2 — hallar $D$ tal que la suma total dé $\mathcal{O}$

**Paso 1 — Despejar $D$.** Partimos de $A + B + C + D = \mathcal{O}$. Pasando $A + B + C$ al otro lado:

$$D = \mathcal{O} - (A + B + C) = -(A + B + C)$$

> **¿Por qué $D$ es el opuesto?** Porque la suma de algo más su opuesto da la nula. Si $A + B + C = M$, necesitamos $M + D = \mathcal{O}$, así que $D = -M$.

**Paso 2 — Calcular $-(A+B+C)$.** Tomo la matriz del paso (iii) y le cambio el signo a cada entrada:

$$D = \begin{pmatrix} -3 & 0 & -7 \\ -2 & -4 & -11 \\ -4 & -2 & -1 \end{pmatrix}$$

---

## 🔵 Ejercicio V.2 — Productos posibles

**Enunciado.** Dadas las matrices:

$$A = \begin{pmatrix} 2 & -1 & 4 \\ 1 & 0 & 6 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 0 & 1 \\ 2 & -1 & 2 \\ 3 & -2 & 0 \end{pmatrix}, \quad C = \begin{pmatrix} 1 & 6 \\ -2 & 4 \\ 0 & 5 \end{pmatrix}$$

Realizar todos los productos posibles entre dos de ellas.

### Solución

#### Paso 1 — Anotar las dimensiones

Antes de multiplicar, siempre conviene anotar las dimensiones:

- $A$ es $2 \times 3$ (2 filas, 3 columnas)
- $B$ es $3 \times 3$
- $C$ es $3 \times 2$

#### Paso 2 — Decidir qué productos son posibles

**Regla de oro:** $X \cdot Y$ se puede hacer si las **columnas de $X$ coinciden con las filas de $Y$**. El resultado tiene las **filas de $X$ y las columnas de $Y$**.

Probamos todas las combinaciones de a pares (12 en total: $A\cdot A, A\cdot B, A\cdot C, B\cdot A, B\cdot B, B\cdot C, C\cdot A, C\cdot B, C\cdot C$, más $A\cdot A$, etc.). Anotando solo las "cruzadas":

| Producto | Dimensiones | ¿Coinciden? | Resultado |
|----------|-------------|-------------|-----------|
| $A \cdot B$ | $(2 \times \mathbf{3}) \cdot (\mathbf{3} \times 3)$ | sí, ambos $3$ | $2 \times 3$ ✓ |
| $A \cdot C$ | $(2 \times \mathbf{3}) \cdot (\mathbf{3} \times 2)$ | sí | $2 \times 2$ ✓ |
| $B \cdot A$ | $(3 \times \mathbf{3}) \cdot (\mathbf{2} \times 3)$ | NO ($3 \neq 2$) | imposible ✗ |
| $B \cdot C$ | $(3 \times \mathbf{3}) \cdot (\mathbf{3} \times 2)$ | sí | $3 \times 2$ ✓ |
| $C \cdot A$ | $(3 \times \mathbf{2}) \cdot (\mathbf{2} \times 3)$ | sí | $3 \times 3$ ✓ |
| $C \cdot B$ | $(3 \times \mathbf{2}) \cdot (\mathbf{3} \times 3)$ | NO ($2 \neq 3$) | imposible ✗ |

**Productos posibles:** $A \cdot B$, $A \cdot C$, $C \cdot A$, $B \cdot C$.

#### Paso 3 — Calcular cada producto

**$A \cdot B$ ($2 \times 3$).** Cada entrada $(i,k)$ = fila $i$ de $A$ por columna $k$ de $B$. Por ejemplo, entrada $(1,1)$: $2 \cdot 1 + (-1) \cdot 2 + 4 \cdot 3 = 2 - 2 + 12 = 12$. Haciendo todas:

$$A \cdot B = \begin{pmatrix} 12 & -7 & 0 \\ 19 & -12 & 1 \end{pmatrix}$$

**$A \cdot C$ ($2 \times 2$).** Por ejemplo, entrada $(1,1)$: $2 \cdot 1 + (-1) \cdot (-2) + 4 \cdot 0 = 2 + 2 + 0 = 4$.

$$A \cdot C = \begin{pmatrix} 4 & 28 \\ 1 & 36 \end{pmatrix}$$

**$C \cdot A$ ($3 \times 3$).** Por ejemplo, entrada $(1,1)$: $1 \cdot 2 + 6 \cdot 1 = 8$. Notá que las filas de $C$ tienen 2 entradas (no 3), así que cada producto suma 2 términos:

$$C \cdot A = \begin{pmatrix} 8 & -1 & 40 \\ 0 & 2 & 16 \\ 5 & 0 & 30 \end{pmatrix}$$

> **Importante:** $A \cdot C \neq C \cdot A$ — ni siquiera tienen la misma dimensión ($2 \times 2$ vs $3 \times 3$). Esto ilustra la **no conmutatividad** del producto.

**$B \cdot C$ ($3 \times 2$).** Por ejemplo, entrada $(1,1)$: $1 \cdot 1 + 0 \cdot (-2) + 1 \cdot 0 = 1$.

$$B \cdot C = \begin{pmatrix} 1 & 11 \\ 4 & 18 \\ 7 & 10 \end{pmatrix}$$

---

## 🟢 Ejercicio V.3 — Producto por vectores canónicos

**Enunciado.** Sea $A$ una matriz $3 \times 3$ con entradas $a_{ij}$ y los tres vectores canónicos:

$$\vec{v}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{v}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

1. Calcular $A \cdot \vec{v}_1$, $A \cdot \vec{v}_2$, $A \cdot \vec{v}_3$.
2. Describir el resultado con palabras.

### Solución

#### Parte 1 — calcular los tres productos

**Para $A \cdot \vec{v}_1$:** $\vec{v}_1$ es UN vector columna (no tiene varias columnas — es UNA sola). Aplico la regla "fila por columna" para cada fila de $A$.

> **Recordá cómo se aplica "fila por columna":** tomás los números de la fila de $A$ (que están uno al lado del otro horizontalmente) y los números del vector $\vec{v}_1$ (que están uno arriba del otro verticalmente). Multiplicás el primero de la fila por el primero del vector, el segundo por el segundo, el tercero por el tercero, y al final sumás esos productos.

Aplicando la regla a cada fila:

**Fila 1 de $A$** es $(a_{11}, a_{12}, a_{13})$. Multiplico contra $\vec{v}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$:

$$a_{11} \cdot 1 + a_{12} \cdot 0 + a_{13} \cdot 0 = a_{11}$$

**Fila 2 de $A$** es $(a_{21}, a_{22}, a_{23})$. Multiplico contra $\vec{v}_1$:

$$a_{21} \cdot 1 + a_{22} \cdot 0 + a_{23} \cdot 0 = a_{21}$$

**Fila 3 de $A$** es $(a_{31}, a_{32}, a_{33})$. Multiplico contra $\vec{v}_1$:

$$a_{31} \cdot 1 + a_{32} \cdot 0 + a_{33} \cdot 0 = a_{31}$$

Apilo los 3 resultados (uno por fila) como vector columna:

$$A \cdot \vec{v}_1 = \begin{pmatrix} a_{11} \\ a_{21} \\ a_{31} \end{pmatrix}$$

> **Observación clave:** ese resultado es **la columna 1 de $A$**.

**Para $A \cdot \vec{v}_2$:** análogo, pero ahora el $1$ del vector está en la **segunda posición** (no la primera). En cada fila de $A$, eso significa que sobrevive solo el segundo número:

- Fila 1: $a_{11} \cdot 0 + a_{12} \cdot 1 + a_{13} \cdot 0 = a_{12}$
- Fila 2: $a_{21} \cdot 0 + a_{22} \cdot 1 + a_{23} \cdot 0 = a_{22}$
- Fila 3: $a_{31} \cdot 0 + a_{32} \cdot 1 + a_{33} \cdot 0 = a_{32}$

$$A \cdot \vec{v}_2 = \begin{pmatrix} a_{12} \\ a_{22} \\ a_{32} \end{pmatrix} = \text{columna 2 de } A$$

**Para $A \cdot \vec{v}_3$:** el $1$ del vector está en la **tercera posición**:

- Fila 1: $a_{11} \cdot 0 + a_{12} \cdot 0 + a_{13} \cdot 1 = a_{13}$
- Fila 2: $a_{21} \cdot 0 + a_{22} \cdot 0 + a_{23} \cdot 1 = a_{23}$
- Fila 3: $a_{31} \cdot 0 + a_{32} \cdot 0 + a_{33} \cdot 1 = a_{33}$

$$A \cdot \vec{v}_3 = \begin{pmatrix} a_{13} \\ a_{23} \\ a_{33} \end{pmatrix} = \text{columna 3 de } A$$

Cada producto es un vector columna ($3 \times 1$).

#### Parte 2 — descripción en palabras

**Multiplicar $A$ por el vector canónico $\vec{v}_j$ devuelve exactamente la columna $j$-ésima de $A$.**

> **Demo formal en `matrices-DEMOSTRACIONES.md` §A.1.**
>
> **Idea central:** los ceros del vector "borran" las otras columnas; el $1$ "selecciona" una sola.
>
> **Para qué sirve este truco en parcial:** si te piden la columna $j$ de un producto $A \cdot B$, no hace falta calcular toda la matriz $AB$ — alcanza con calcular $A \cdot B \cdot \vec{v}_j$. Te ahorra cuentas.

---

## 🟢 Ejercicio V.4 — Potencias por inducción

**Enunciado.** Sea $A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$. Calcular $A^2$, $A^3$ y probar:

$$A^n = \begin{pmatrix} 1 & n & \frac{n^2 + n}{2} \\ 0 & 1 & n \\ 0 & 0 & 1 \end{pmatrix} \quad \forall n \geq 1$$

### Solución

#### Paso 1 — calcular $A^2 = A \cdot A$ entrada por entrada

Hago "fila × columna" en cada una de las 9 entradas. Algunos ejemplos:

- Entrada $(1,2)$ de $A^2$: tomo la fila 1 de $A$ (cuyas entradas son $1, 1, 1$) y la multiplico contra la columna 2 de $A$ (cuyas entradas, leídas de arriba a abajo, son $1, 1, 0$). Producto par-a-par y suma: $1 \cdot 1 + 1 \cdot 1 + 1 \cdot 0 = 2$.

- Entrada $(1,3)$: fila 1 ($1, 1, 1$) por columna 3 ($1, 1, 1$ de arriba a abajo): $1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1 = 3$.

- Entrada $(2,3)$: fila 2 ($0, 1, 1$) por columna 3 ($1, 1, 1$): $0 \cdot 1 + 1 \cdot 1 + 1 \cdot 1 = 2$.

$$A^2 = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}$$

> **Verificación con la fórmula:** para $n = 2$, la fórmula da $\frac{2^2+2}{2} = \frac{6}{2} = 3$ en posición $(1,3)$. ✓

#### Paso 2 — calcular $A^3 = A^2 \cdot A$ entrada por entrada

Ejemplos:

- Entrada $(1,3)$ de $A^3$: fila 1 de $A^2$ ($1, 2, 3$) por columna 3 de $A$ ($1, 1, 1$ de arriba a abajo): $1 \cdot 1 + 2 \cdot 1 + 3 \cdot 1 = 6$.

- Entrada $(2,3)$: fila 2 de $A^2$ ($0, 1, 2$) por columna 3 de $A$ ($1, 1, 1$): $0 \cdot 1 + 1 \cdot 1 + 2 \cdot 1 = 3$.

$$A^3 = \begin{pmatrix} 1 & 3 & 6 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{pmatrix}$$

> **Verificación:** $\frac{3^2+3}{2} = 6$ en posición $(1,3)$. ✓

#### Paso 3 — generalizar por inducción

Demo paso a paso de la inducción completa en `matrices-DEMOSTRACIONES.md` §G.3.

> **Idea de la inducción:** la base son los casos $n=1$, $n=2$ que acabamos de verificar. Asumimos que la fórmula vale para $n=h$ y probamos que vale para $n=h+1$ multiplicando $A^h \cdot A$. La entrada $(1,3)$ es la que requiere más álgebra ($1 + h + \frac{h(h+1)}{2}$ tiene que dar $\frac{(h+1)(h+2)}{2}$).

---

## 🟢 Ejercicio V.5 — Suma y producto de simétricas

**Enunciado.** Sean $A, B$ matrices $n \times n$ simétricas y $\lambda \in \mathbb{R}$.

1. Probar que $A + B$ y $\lambda A$ son simétricas.
2. Probar que $AB$ es simétrica si y solo si $AB = BA$.

### Solución (referenciada)

| Parte | Resultado | Demo |
|-------|-----------|------|
| 1 — $A+B$ simétrica | $(A+B)^T = A^T + B^T = A + B$ | demos.md §C.1 |
| 1 — $\lambda A$ simétrica | $(\lambda A)^T = \lambda A^T = \lambda A$ | demos.md §C.2 |
| 2 — $AB$ sim $\iff AB = BA$ (ambas direcciones) | demo completa con directo y recíproco | demos.md §C.3 |

---

## 🟢 Ejercicio V.6 — Descomposición simétrica + antisimétrica

**Enunciado.** Sea $A$ matriz $n \times n$ cualquiera.

1. Probar que $\frac{1}{2}(A + A^T)$ es simétrica.
2. Probar que $\frac{1}{2}(A - A^T)$ es antisimétrica.
3. Concluir: cualquier $A$ cuadrada $=$ simétrica $+$ antisimétrica.

### Solución (referenciada)

| Parte | Demo |
|-------|------|
| 1 — $\frac{1}{2}(A + A^T)$ simétrica | demos.md §C.4 |
| 2 — $\frac{1}{2}(A - A^T)$ antisimétrica | demos.md §C.5 |
| 3 — descomposición $A = \frac{1}{2}(A+A^T) + \frac{1}{2}(A-A^T)$ | demos.md §C.6 |

---

## 🟢 Ejercicio V.7 — Matriz nilpotente

**Enunciado.** Sea $A = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$.

1. Probar que $A$ es nilpotente. ¿De qué grado?
2. Si $P$ es invertible, ¿$P^{-1} A P$ es nilpotente? ¿De qué grado?

### Solución

#### Parte 1 — calcular potencias hasta encontrar la nula

**Paso 1 — Calcular $A^2 = A \cdot A$ entrada por entrada.**

- Entrada $(1,1)$: fila 1 de $A$ ($0, 1, 1$) por columna 1 de $A$ ($0, 0, 0$ leída de arriba a abajo): $0 + 0 + 0 = 0$.
- Entrada $(1,2)$: fila 1 ($0, 1, 1$) por columna 2 ($1, 0, 0$ de arriba a abajo): $0 \cdot 1 + 1 \cdot 0 + 1 \cdot 0 = 0$.
- Entrada $(1,3)$: fila 1 ($0, 1, 1$) por columna 3 ($1, 1, 0$ de arriba a abajo): $0 \cdot 1 + 1 \cdot 1 + 1 \cdot 0 = 1$. ← ¡no cero!
- Otras entradas: el resto da cero por la estructura triangular.

$$A^2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

$A^2 \neq \mathcal{O}$ porque tiene un $1$ en la entrada $(1,3)$.

**Paso 2 — Calcular $A^3 = A^2 \cdot A$.**

- La fila 1 de $A^2$ es $(0, 0, 1)$. Solo "ve" la fila 3 de $A$, que es $(0, 0, 0)$ (toda nula).
- Las filas 2 y 3 de $A^2$ son nulas.

Todas las entradas de $A^3$ dan cero:

$$A^3 = \mathcal{O}$$

**Paso 3 — Conclusión sobre el grado.** Como $A^3 = \mathcal{O}$ pero $A^2 \neq \mathcal{O}$, la **primera potencia** que anula es la $3$. Por definición de nilpotente:

$$\boxed{A \text{ es nilpotente de grado } 3} \;\;\blacksquare$$

> **¿Qué significa "grado $k$"?** $k$ es el menor entero tal que $A^k = \mathcal{O}$. No basta con que SE anule en algún punto — también hay que decir CUÁNDO se anula por primera vez.

#### Parte 2 — $P^{-1} A P$ tiene el mismo grado

Como $A$ es nilpotente de grado $3$, **$P^{-1} A P$ también es nilpotente de grado $3$**.

> **Idea (demo completa en `matrices-DEMOSTRACIONES.md` §F.3):**
> - Por un lado, $(P^{-1} A P)^3 = P^{-1} A^3 P = P^{-1} \mathcal{O} P = \mathcal{O}$ (los $P P^{-1}$ del medio se cancelan).
> - Por otro, $(P^{-1} A P)^2 = P^{-1} A^2 P \neq \mathcal{O}$ (porque $A^2 \neq \mathcal{O}$ y $P$ es invertible — si fuera cero, podríamos despejar $A^2 = \mathcal{O}$, contradicción).

---

## 🟢 Ejercicio V.8 — Ecuación matricial polinomial (SE PIDE — factorización clave)

**Enunciado.** Dada $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{pmatrix}$.

1. Verificar que $A$ satisface la ecuación matricial $-A^3 + 5A^2 - 7A + 3 \cdot \text{Id}_{3 \times 3} = \mathcal{O}_{3 \times 3}$.
2. Demostrar que $A$ es invertible y hallar su inversa.

### Solución

#### Parte 1 — Verificar la ecuación $-A^3 + 5A^2 - 7A + 3\text{Id} = \mathcal{O}$

**Paso 1 — Calcular $A^2$ haciendo $A \cdot A$.** Hago "fila × columna" en cada entrada. Por ejemplo, entrada $(1,2)$ de $A^2$:

$$\text{fila 1 de } A \cdot \text{col 2 de } A = 1 \cdot 1 + 1 \cdot 1 + 0 \cdot 0 = 2$$

Haciendo todas las entradas:

$$A^2 = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 9 \end{pmatrix}$$

> **¿Por qué la entrada $(3,3)$ es $9$?** Porque la fila 3 de $A$ es $0, 0, 3$ (horizontal) y la columna 3 de $A$ tiene las entradas $0, 0, 3$ leídas de arriba a abajo (vertical). Multiplicando par a par: $0 \cdot 0 + 0 \cdot 0 + 3 \cdot 3 = 9$.

**Paso 2 — Calcular $A^3$ haciendo $A^2 \cdot A$.**

$$A^3 = \begin{pmatrix} 1 & 3 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 27 \end{pmatrix}$$

> **Observación:** la entrada $(1,2)$ pasó de $1 \to 2 \to 3$, y la $(3,3)$ pasó de $3 \to 9 \to 27$. Eso pasa porque $A$ es casi diagonal y las potencias siguen un patrón.

**Paso 3 — Calcular cada término de la ecuación con su signo y escalar.**

$$-A^3 = \begin{pmatrix} -1 & -3 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -27 \end{pmatrix}, \quad 5A^2 = \begin{pmatrix} 5 & 10 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 45 \end{pmatrix}$$

$$-7A = \begin{pmatrix} -7 & -7 & 0 \\ 0 & -7 & 0 \\ 0 & 0 & -21 \end{pmatrix}, \quad 3\text{Id} = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix}$$

**Paso 4 — Sumar las cuatro matrices.** Entrada por entrada. Por ejemplo, $(1,1)$: $-1 + 5 - 7 + 3 = 0$. $(1,2)$: $-3 + 10 - 7 + 0 = 0$. $(3,3)$: $-27 + 45 - 21 + 3 = 0$. Y así todas:

$$-A^3 + 5A^2 - 7A + 3\text{Id} = \mathcal{O}_{3 \times 3} \quad \checkmark$$

#### Parte 2 — Demostrar que $A$ es invertible y hallar $A^{-1}$

**Paso 1 — Estrategia: usar la ecuación de la parte 1 para despejar $A^{-1}$.** La idea es factorizar la ecuación hasta tener algo de la forma $A \cdot (\text{algo}) = \text{Id}$.

**Paso 2 — Reordenar la ecuación.** De la parte 1: $-A^3 + 5A^2 - 7A + 3\text{Id} = \mathcal{O}$. Pasando $3\text{Id}$ a la derecha:

$$-A^3 + 5A^2 - 7A = -3\text{Id}$$

Multiplicando por $-1$:

$$A^3 - 5A^2 + 7A = 3\text{Id}$$

**Paso 3 — Sacar $A$ como factor común a izquierda.**

$$A \cdot (A^2 - 5A + 7\text{Id}) = 3\text{Id}$$

> **¿Por qué puedo factorizar?** Porque $A^3 = A \cdot A^2$, $5A^2 = A \cdot 5A$ (escalar entre factores), y $7A = A \cdot 7\text{Id}$. Todos tienen $A$ a izquierda.

**Paso 4 — Dividir ambos lados por $3$ (multiplicar por $\frac{1}{3}$).**

$$A \cdot \tfrac{1}{3}(A^2 - 5A + 7\text{Id}) = \text{Id}$$

> **¡Ahí está!** Tengo la forma $A \cdot (\text{algo}) = \text{Id}$. Por definición de inversa, ese "algo" es $A^{-1}$:

$$A^{-1} = \tfrac{1}{3}(A^2 - 5A + 7\text{Id})$$

**Paso 5 — Calcular numéricamente $A^2 - 5A + 7\text{Id}$.**

$$A^2 - 5A + 7\text{Id} = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 9 \end{pmatrix} - \begin{pmatrix} 5 & 5 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 15 \end{pmatrix} + \begin{pmatrix} 7 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 7 \end{pmatrix}$$

Entrada por entrada: $(1,1) = 1 - 5 + 7 = 3$, $(1,2) = 2 - 5 + 0 = -3$, etc.

$$= \begin{pmatrix} 3 & -3 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

**Paso 6 — Multiplicar por $\frac{1}{3}$ (cada entrada se divide por $3$).**

$$\boxed{A^{-1} = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1/3 \end{pmatrix}}$$

---

## 🔵 Ejercicio V.9 — Inversas por método directo

**Enunciado.** Encontrar la inversa (si existe) de:

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix}, \;\; B = \begin{pmatrix} 2 & 1 \\ 4 & 2 \end{pmatrix}, \;\; C = \begin{pmatrix} 1 & 1 & -1 \\ 1 & -1 & 1 \\ 1 & 1 & 1 \end{pmatrix}, \;\; D = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 5 & 0 \\ 2 & 4 & 3 \end{pmatrix}, \;\; E = \begin{pmatrix} 1 & 0 & 1 & -1 \\ 2 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & -1 & 2 & 1 \end{pmatrix}$$

### Solución paso a paso (caso $A$, modelo)

> El método directo es el mismo procedimiento mecánico para todas. Te lo desarrollo entero para $A$ y después listo solo los resultados.

**Paso 1 — Plantear la incógnita.** Buscamos una matriz $X$ del mismo tamaño que $A$ ($2 \times 2$) tal que $A \cdot X = \text{Id}$. Llamamos a sus entradas $a, b, c, d$:

$$X = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

**Paso 2 — Multiplicar $A \cdot X$ entrada por entrada.** Hacemos "fila × columna" en cada una de las 4 entradas:

- Entrada $(1,1)$: $1 \cdot a + 2 \cdot c = a + 2c$
- Entrada $(1,2)$: $1 \cdot b + 2 \cdot d = b + 2d$
- Entrada $(2,1)$: $3 \cdot a + 1 \cdot c = 3a + c$
- Entrada $(2,2)$: $3 \cdot b + 1 \cdot d = 3b + d$

Quedando:

$$A \cdot X = \begin{pmatrix} a + 2c & b + 2d \\ 3a + c & 3b + d \end{pmatrix}$$

**Paso 3 — Igualar a la identidad.** Por hipótesis queremos $A \cdot X = \text{Id}$:

$$\begin{pmatrix} a + 2c & b + 2d \\ 3a + c & 3b + d \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

**Paso 4 — Sacar el sistema de ecuaciones.** Dos matrices son iguales si lo son entrada por entrada:

$$\begin{cases} a + 2c = 1 \\ b + 2d = 0 \\ 3a + c = 0 \\ 3b + d = 1 \end{cases}$$

> **Notá:** son 4 ecuaciones con 4 incógnitas. Y se separan naturalmente en dos parejas: $(a, c)$ usan las ecuaciones 1 y 3; $(b, d)$ usan las 2 y 4.

**Paso 5 — Resolver para $a, c$ (ecuaciones 1 y 3).** Sistema:

$$\begin{cases} a + 2c = 1 \\ 3a + c = 0 \end{cases}$$

De la segunda ecuación, $c = -3a$. Sustituyo en la primera: $a + 2(-3a) = 1 \Rightarrow a - 6a = 1 \Rightarrow -5a = 1 \Rightarrow a = -\frac{1}{5}$. Y $c = -3 \cdot (-\frac{1}{5}) = \frac{3}{5}$.

**Paso 6 — Resolver para $b, d$ (ecuaciones 2 y 4).** Sistema:

$$\begin{cases} b + 2d = 0 \\ 3b + d = 1 \end{cases}$$

De la primera, $b = -2d$. Sustituyo: $3(-2d) + d = 1 \Rightarrow -6d + d = 1 \Rightarrow -5d = 1 \Rightarrow d = -\frac{1}{5}$. Y $b = -2 \cdot (-\frac{1}{5}) = \frac{2}{5}$.

**Paso 7 — Armar la inversa.**

$$\boxed{A^{-1} = \begin{pmatrix} -1/5 & 2/5 \\ 3/5 & -1/5 \end{pmatrix}}$$

> **Verificación rápida:** podés multiplicar $A \cdot A^{-1}$ y ver que da $\text{Id}$. Es buena costumbre hacerlo.

### Resultados (oficiales) para las otras matrices

$$B^{-1} \text{ no existe}$$
> **¿Por qué?** La fila 2 de $B$ es $2$ veces la fila 1. Cuando planteás $B \cdot X = \text{Id}$, el sistema queda incompatible (una ecuación pide $0 = 1$, imposible).

$$C^{-1} = \begin{pmatrix} 1/2 & 1/2 & 0 \\ 0 & -1/2 & 1/2 \\ -1/2 & 0 & 1/2 \end{pmatrix}$$

$$D^{-1} = \begin{pmatrix} -1 & -2/5 & 1 \\ 0 & 1/5 & 0 \\ 2/3 & 0 & -1/3 \end{pmatrix}$$

$$E^{-1} = \begin{pmatrix} 0 & 1/2 & -1/2 & 0 \\ -1/4 & 1/8 & 5/8 & -1/4 \\ 1/4 & -1/8 & 3/8 & 1/4 \\ -3/4 & 3/8 & -1/8 & 1/4 \end{pmatrix}$$

**Nota de la cátedra:** *"En los casos $3 \times 3$ y $4 \times 4$ se recomienda calcular la inversa por escalerización (Gauss-Jordan que se verá más adelante)"*. Para este parcial el método directo es el válido.

---

## 🟢 Ejercicio V.10 — $A^2 = 2A - \text{Id}$ (CLAVE para parcial)

**Enunciado.** Sea $A = \begin{pmatrix} 5 & -4 & 2 \\ 2 & -1 & 1 \\ -4 & 4 & -1 \end{pmatrix}$.

1. Probar que $A^2 = 2A - \text{Id}$. Deducir que $A$ es invertible.
2. Probar que $A^3 = 3A - 2 \text{Id}$ y hallar $A^3$.
3. Probar por inducción que $A^n = nA - (n-1)\text{Id}$, $\forall n \geq 2$.

### Solución

#### Parte 1 — verificar $A^2 = 2A - \text{Id}$ y deducir invertibilidad

**Paso 1 — Calcular $A^2$ haciendo $A \cdot A$ entrada por entrada.** Aplico fila × columna en cada una de las 9 entradas. Por ejemplo, la entrada $(1,1)$ de $A^2$ es:

$$\text{fila 1 de } A \cdot \text{col 1 de } A = 5 \cdot 5 + (-4) \cdot 2 + 2 \cdot (-4) = 25 - 8 - 8 = 9$$

Haciendo lo mismo con las otras 8 entradas:

$$A^2 = \begin{pmatrix} 9 & -8 & 4 \\ 4 & -3 & 2 \\ -8 & 8 & -3 \end{pmatrix}$$

**Paso 2 — Calcular $2A - \text{Id}$.** Primero $2A$ (multiplicar cada entrada por 2):

$$2A = \begin{pmatrix} 10 & -8 & 4 \\ 4 & -2 & 2 \\ -8 & 8 & -2 \end{pmatrix}$$

Después restamos $\text{Id}$ (que tiene unos en la diagonal y ceros afuera):

$$2A - \text{Id} = \begin{pmatrix} 10-1 & -8 & 4 \\ 4 & -2-1 & 2 \\ -8 & 8 & -2-1 \end{pmatrix} = \begin{pmatrix} 9 & -8 & 4 \\ 4 & -3 & 2 \\ -8 & 8 & -3 \end{pmatrix}$$

> **¿Qué cambió?** Solo restamos $1$ a las entradas de la diagonal: $10 \to 9$, $-2 \to -3$, $-2 \to -3$. El resto queda igual.

**Paso 3 — Comparar.** Los pasos 1 y 2 dan la misma matriz: ✓ se cumple $A^2 = 2A - \text{Id}$.

**Paso 4 — Deducir invertibilidad por factorización.** Empiezo de la igualdad recién probada y voy moviendo términos hasta que aparezca un producto $A \cdot (\text{algo}) = \text{Id}$:

$$A^2 = 2A - \text{Id}$$

Paso $\text{Id}$ a la izquierda:

$$A^2 - 2A = -\text{Id}$$

Multiplico ambos lados por $-1$ (cambia los signos):

$$-A^2 + 2A = \text{Id}$$

Agrupo factor común $A$ a izquierda. $-A^2 = -A \cdot A$ y $2A = A \cdot 2\text{Id}$, así que:

$$A \cdot (-A) + A \cdot (2\text{Id}) = A \cdot (-A + 2\text{Id}) = A \cdot (2\text{Id} - A)$$

Igualando con el lado derecho:

$$A \cdot (2\text{Id} - A) = \text{Id}$$

> **¿Qué dice esto?** Encontré una matriz ($2\text{Id} - A$) que multiplicada por $A$ da $\text{Id}$. Por definición de inversa, esa es $A^{-1}$.

**Paso 5 — Calcular numéricamente $A^{-1} = 2\text{Id} - A$.**

$$2\text{Id} - A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 5 & -4 & 2 \\ 2 & -1 & 1 \\ -4 & 4 & -1 \end{pmatrix} = \begin{pmatrix} -3 & 4 & -2 \\ -2 & 3 & -1 \\ 4 & -4 & 3 \end{pmatrix}$$

$$\boxed{A^{-1} = \begin{pmatrix} -3 & 4 & -2 \\ -2 & 3 & -1 \\ 4 & -4 & 3 \end{pmatrix}}$$

> **Cita del profesor:** *"Si probaste que esta es la inversa, estás probando las dos cosas a la misma vez"* — porque encontrar la inversa explícita es prueba directa de que $A$ es invertible.

#### Parte 2 — probar $A^3 = 3A - 2\text{Id}$

**Paso 1 — Reescribir $A^3$ como $A^2 \cdot A$.**

$$A^3 = A^2 \cdot A$$

**Paso 2 — Reemplazar $A^2$ usando la parte 1 ($A^2 = 2A - \text{Id}$).**

$$A^3 = (2A - \text{Id}) \cdot A$$

**Paso 3 — Distribuir el producto.**

$$= 2A \cdot A - \text{Id} \cdot A = 2 A^2 - A$$

> **¿Qué pasó?** $2A \cdot A = 2 A^2$ (los escalares salen y $A \cdot A = A^2$). Y $\text{Id} \cdot A = A$.

**Paso 4 — Reemplazar $A^2$ otra vez por $2A - \text{Id}$.**

$$= 2(2A - \text{Id}) - A$$

**Paso 5 — Distribuir el $2$ y juntar términos.**

$$= 4A - 2\text{Id} - A = (4-1)A - 2\text{Id} = 3A - 2\text{Id} \quad \checkmark$$

**Paso 6 — Calcular numéricamente.**

$$3A = \begin{pmatrix} 15 & -12 & 6 \\ 6 & -3 & 3 \\ -12 & 12 & -3 \end{pmatrix}, \quad 2\text{Id} = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix}$$

$$A^3 = 3A - 2\text{Id} = \begin{pmatrix} 13 & -12 & 6 \\ 6 & -5 & 3 \\ -12 & 12 & -5 \end{pmatrix}$$

#### Parte 3 — inducción $A^n = nA - (n-1)\text{Id}$

Demo completa paso a paso en `matrices-DEMOSTRACIONES.md` §G.2. Es la generalización por inducción de lo que hicimos en la Parte 2.

> **Idea de toda la inducción:** lo que en la parte 2 hicimos para pasar de $A^2$ a $A^3$, lo hacemos en general para pasar de $A^h$ a $A^{h+1}$. La hipótesis $A^2 = 2A - \text{Id}$ se usa en cada paso para "bajar la potencia".

---

## 🟢 Ejercicio V.11 — Ley de simplificación

**Enunciado.**

1. Si $AB = A$ y $A$ es invertible, probar $B = \text{Id}$.
2. Si $AB = AC$ y $A$ es invertible, probar $B = C$.
3. Con $A = \begin{pmatrix} 0 & 3 \\ 0 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 2 & 1 \\ 3 & 0 \end{pmatrix}$, $C = \begin{pmatrix} 5 & 4 \\ 3 & 0 \end{pmatrix}$: mostrar $AB = AC$ pero $B \neq C$. ¿Qué conclusión?

### Solución (referenciada)

**Partes 1 y 2 — demos:** ambas multiplican por $A^{-1}$ a izquierda. Demo paso a paso en `matrices-DEMOSTRACIONES.md` §I.1.

**Parte 3 — contraejemplo:** $AB = AC = \begin{pmatrix} 9 & 0 \\ 0 & 0 \end{pmatrix}$ pero $B \neq C$. **Conclusión:** $A$ no es invertible. La ley de simplificación **no vale** sin la hipótesis de invertibilidad — verifica el contraejemplo del práctico.

---

## 🟢 Ejercicio V.12 — Matriz ortogonal

**Enunciado.** $A$ ortogonal significa que $A^{-1} = A^T$, lo que es equivalente a $A^T \cdot A = \text{Id}$.

Dada $A = \begin{pmatrix} 4/5 & 3/5 \\ \alpha & \beta \end{pmatrix}$, hallar $\alpha, \beta \in \mathbb{R}$ para que $A$ sea ortogonal y dar su inversa.

### Solución

**Paso 1 — Traducir la condición.** "$A$ ortogonal" significa $A^{-1} = A^T$. Eso es equivalente a $A^T \cdot A = \text{Id}$ (por definición de inversa). Vamos a usar esta segunda forma porque se calcula directamente.

**Paso 2 — Calcular $A^T$.** Trasponer = intercambiar fila por columna:

$$A^T = \begin{pmatrix} 4/5 & \alpha \\ 3/5 & \beta \end{pmatrix}$$

**Paso 3 — Calcular $A^T \cdot A$ entrada por entrada.**

- $(1,1)$: $\frac{4}{5} \cdot \frac{4}{5} + \alpha \cdot \alpha = \frac{16}{25} + \alpha^2$
- $(1,2)$: $\frac{4}{5} \cdot \frac{3}{5} + \alpha \cdot \beta = \frac{12}{25} + \alpha\beta$
- $(2,1)$: $\frac{3}{5} \cdot \frac{4}{5} + \beta \cdot \alpha = \frac{12}{25} + \alpha\beta$
- $(2,2)$: $\frac{3}{5} \cdot \frac{3}{5} + \beta \cdot \beta = \frac{9}{25} + \beta^2$

Quedando:

$$A^T \cdot A = \begin{pmatrix} 16/25 + \alpha^2 & 12/25 + \alpha\beta \\ 12/25 + \alpha\beta & 9/25 + \beta^2 \end{pmatrix}$$

**Paso 4 — Igualar a $\text{Id}$.** Pedimos $A^T \cdot A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$. Eso da el sistema:

$$\begin{cases} \frac{16}{25} + \alpha^2 = 1 \\ \frac{9}{25} + \beta^2 = 1 \\ \frac{12}{25} + \alpha\beta = 0 \end{cases}$$

> **Nota:** las entradas $(1,2)$ y $(2,1)$ son la misma ecuación, por eso solo cuentan como una.

**Paso 5 — Resolver $\alpha$.** De la primera: $\alpha^2 = 1 - \frac{16}{25} = \frac{9}{25}$. Tomando raíz:

$$\alpha = \pm \frac{3}{5}$$

> **¿Por qué dos signos?** Porque tanto $\frac{3}{5}$ como $-\frac{3}{5}$ elevados al cuadrado dan $\frac{9}{25}$.

**Paso 6 — Resolver $\beta$.** Análogo: $\beta^2 = 1 - \frac{9}{25} = \frac{16}{25}$, así que $\beta = \pm \frac{4}{5}$.

**Paso 7 — Usar la tercera ecuación para combinar signos.** La tercera ecuación dice $\alpha\beta = -\frac{12}{25}$. Como $\frac{3}{5} \cdot \frac{4}{5} = \frac{12}{25}$ es positivo, $\alpha$ y $\beta$ deben tener **signos opuestos** (uno positivo, otro negativo).

**Paso 8 — Las dos soluciones.**

- **Caso 1:** $\alpha = \frac{3}{5}, \beta = -\frac{4}{5}$. Entonces $A^{-1} = A^T = \begin{pmatrix} 4/5 & 3/5 \\ 3/5 & -4/5 \end{pmatrix}$.

- **Caso 2:** $\alpha = -\frac{3}{5}, \beta = \frac{4}{5}$. Entonces $A^{-1} = A^T = \begin{pmatrix} 4/5 & -3/5 \\ 3/5 & 4/5 \end{pmatrix}$.

> **Idea central:** ortogonal $\Leftrightarrow A^T A = \text{Id}$. Plantear esa condición da un sistema con $n^2$ ecuaciones en las incógnitas, que se resuelve con álgebra básica.

---

## 🔵 Ejercicio V.13 — Hallar parámetros para $P^{-1} A P$

**Enunciado.** Dadas $A = \begin{pmatrix} 1 & 2 \\ 5 & 4 \end{pmatrix}$ y $P = \begin{pmatrix} 2 & 1 \\ x & y \end{pmatrix}$, hallar $x, y$ para que:

$$P^{-1} \cdot A \cdot P = \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix}$$

### Solución

**Paso 1 — Truco para evitar calcular $P^{-1}$.** Calcular $P^{-1}$ explícitamente sería un fastidio (y encima depende de $x, y$, así que sería con incógnitas). Mejor: **multiplico por $P$ a izquierda en ambos lados** para que el $P^{-1}$ se cancele.

$$P \cdot (P^{-1} \cdot A \cdot P) = P \cdot \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix}$$

> **¿Por qué a izquierda?** Porque $P^{-1}$ está a izquierda de $A \cdot P$. Para que $P \cdot P^{-1} = \text{Id}$ se forme, $P$ tiene que estar a la izquierda de $P^{-1}$.

**Paso 2 — Reagrupar usando asociativa.**

$$\underbrace{(P \cdot P^{-1})}_{=\text{Id}} \cdot A \cdot P = P \cdot \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix}$$

$P \cdot P^{-1} = \text{Id}$, y $\text{Id} \cdot A = A$. Queda:

$$A \cdot P = P \cdot \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix}$$

> **¡Listo!** Ya no aparece $P^{-1}$. Es una ecuación con incógnitas $x, y$ que podemos resolver.

**Paso 3 — Calcular el lado izquierdo $A \cdot P$.** Multiplicación entrada por entrada:

$$A \cdot P = \begin{pmatrix} 1 & 2 \\ 5 & 4 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ x & y \end{pmatrix} = \begin{pmatrix} 1 \cdot 2 + 2 \cdot x & 1 \cdot 1 + 2 \cdot y \\ 5 \cdot 2 + 4 \cdot x & 5 \cdot 1 + 4 \cdot y \end{pmatrix} = \begin{pmatrix} 2 + 2x & 1 + 2y \\ 10 + 4x & 5 + 4y \end{pmatrix}$$

**Paso 4 — Calcular el lado derecho $P \cdot \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix}$.**

$$P \cdot \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ x & y \end{pmatrix} \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 12 & -1 \\ 6x & -y \end{pmatrix}$$

> **Cálculo de la entrada $(2,2)$ del lado derecho:** la fila 2 de $P$ es $x, y$ (horizontal). La columna 2 de la matriz diagonal es $0, -1$ leída de arriba a abajo (vertical). Multiplicando par a par y sumando: $x \cdot 0 + y \cdot (-1) = -y$.

**Paso 5 — Igualar entrada por entrada.** Las dos matrices tienen que ser iguales:

$$\begin{cases} 2 + 2x = 12 & \text{(entrada } (1,1) \text{)} \\ 1 + 2y = -1 & \text{(entrada } (1,2) \text{)} \\ 10 + 4x = 6x & \text{(entrada } (2,1) \text{)} \\ 5 + 4y = -y & \text{(entrada } (2,2) \text{)} \end{cases}$$

**Paso 6 — Resolver.** De la primera ecuación: $2x = 10 \Rightarrow x = 5$. De la segunda: $2y = -2 \Rightarrow y = -1$.

**Paso 7 — Verificar las dos restantes (deberían ser consistentes).**

- Ecuación (3): $10 + 4(5) = 30$, ¿igual a $6(5) = 30$? Sí ✓
- Ecuación (4): $5 + 4(-1) = 1$, ¿igual a $-(-1) = 1$? Sí ✓

**Resultado:** $\boxed{x = 5, \;\; y = -1}$.

> **Idea central del ejercicio:** cuando aparece $P^{-1}$ en una ecuación matricial, casi siempre conviene multiplicar por $P$ del lado correcto para hacer desaparecer el $P^{-1}$, en lugar de calcularlo.

---

## 🟢 Ejercicio V.14 — ¿$A + B$ y $AB$ invertibles si $A, B$ lo son?

**Enunciado.** $A, B$ matrices reales $n \times n$ invertibles.

1. ¿$A + B$ necesariamente invertible?
2. ¿$AB$ necesariamente invertible?

### Solución

**Parte 1. NO.** Contraejemplo: $A = \text{Id}$, $B = -\text{Id}$. Ambas invertibles, pero $A + B = \mathcal{O}$ que no lo es.

**Parte 2. SÍ.** $(AB)^{-1} = B^{-1} A^{-1}$. **Demo en `matrices-DEMOSTRACIONES.md` §E.2.**

---

## 🟢 Ejercicio V.15 — Conmutatividad

**Enunciado.**

1. Si $A$ conmuta con $B$ y $A$ conmuta con $C$, probar que $A$ conmuta con $D = \mu B + \lambda C$.
2. Sea $A = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix}$. Hallar todas las que conmutan con $A$. Concluir sin multiplicar que $D_1 = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix}$ y $D_2 = \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix}$ conmutan.

### Solución

#### Parte 1 — demo

Ver `matrices-DEMOSTRACIONES.md` §I.3 paso a paso. Idea: usar las hipótesis $AB = BA$ y $AC = CA$ junto con la distributiva.

#### Parte 2 — hallar todas las matrices que conmutan con $A$

**Paso 1 — Plantear $B$ con incógnitas.** Sea $B = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ una matriz $2 \times 2$ genérica. Vamos a encontrar qué relaciones deben cumplir $a, b, c, d$ para que $AB = BA$.

**Paso 2 — Calcular $AB$.**

$$AB = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 1 \cdot a + (-1) \cdot c & 1 \cdot b + (-1) \cdot d \\ 1 \cdot a + 0 \cdot c & 1 \cdot b + 0 \cdot d \end{pmatrix} = \begin{pmatrix} a - c & b - d \\ a & b \end{pmatrix}$$

**Paso 3 — Calcular $BA$.**

$$BA = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} a \cdot 1 + b \cdot 1 & a \cdot (-1) + b \cdot 0 \\ c \cdot 1 + d \cdot 1 & c \cdot (-1) + d \cdot 0 \end{pmatrix} = \begin{pmatrix} a + b & -a \\ c + d & -c \end{pmatrix}$$

**Paso 4 — Imponer $AB = BA$ y obtener el sistema.** Igualamos entrada por entrada:

$$\begin{cases} a - c = a + b & (1,1) \\ b - d = -a & (1,2) \\ a = c + d & (2,1) \\ b = -c & (2,2) \end{cases}$$

**Paso 5 — Resolver el sistema.**

- De la ecuación $(1,1)$: $a - c = a + b \Rightarrow -c = b \Rightarrow \boxed{c = -b}$
- De la ecuación $(2,2)$: $b = -c$ — consistente con la anterior.
- De la ecuación $(1,2)$: $b - d = -a \Rightarrow d = a + b \Rightarrow \boxed{d = a + b}$
- De la ecuación $(2,1)$: $a = c + d$. Sustituyo $c = -b$ y $d = a + b$: $a = -b + a + b = a$ ✓ (siempre cierto, no agrega info nueva).

**Paso 6 — Conclusión.** Las matrices que conmutan con $A$ son las de la forma:

$$\boxed{B = \begin{pmatrix} a & b \\ -b & a+b \end{pmatrix}, \quad \text{con } a, b \in \mathbb{R} \text{ libres}}$$

> **¿Por qué solo dos parámetros libres?** Porque las ecuaciones del paso 4 fijaron $c$ y $d$ en términos de $a$ y $b$. Quedan 2 grados de libertad.

**Paso 7 — Verificar casos particulares.**

- ¿$A$ conmuta consigo misma? $A = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix}$. Identifico $a = 1, b = -1$, así que $-b = 1$ ✓ y $a+b = 0$ ✓. Sí, $A$ tiene esa forma.
- ¿$\text{Id}$ conmuta con $A$? $\text{Id} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$. Identifico $a = 1, b = 0$, así que $-b = 0$ ✓ y $a + b = 1$ ✓. Sí, $\text{Id}$ tiene esa forma.

**Paso 8 — Concluir sin multiplicar para $D_1, D_2$.** En lugar de multiplicar, escribo cada $D$ como combinación lineal de $A$ y $\text{Id}$:

- $D_1 = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} + \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = A + \text{Id}$
- $D_2 = \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} - \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = A - \text{Id}$

Como $A$ conmuta consigo misma (trivial) y $A$ conmuta con $\text{Id}$ (la identidad conmuta con todas), **por la parte 1** $A$ conmuta con cualquier combinación lineal de $A$ y $\text{Id}$ — incluyendo $D_1$ y $D_2$. ✓

> **Idea central de la parte 2:** plantear $B$ genérico, hacer los productos, obtener un sistema, resolverlo. Eso te da TODAS las matrices que conmutan con $A$ (no solo una).

---

## 🟢 Ejercicio V.16 — VERDADERO o FALSO

**Enunciado.** Probar si son ciertas o dar contraejemplo. Si son falsas, agregar hipótesis para que se cumplan.

1. $(A + B)^2 = A^2 + 2AB + B^2$
2. Si $A, B$ simétricas $\Rightarrow AB$ simétrica.
3. $A$ invertible $\Rightarrow A^T$ invertible y $(A^T)^{-1} = (A^{-1})^T$.

### Solución

#### Parte 1 — FALSO en general

**Paso 1 — Desarrollar $(A+B)^2$ honestamente.** $(A+B)^2$ significa $(A+B) \cdot (A+B)$. Aplicando la distributiva (cuidado: como las matrices NO conmutan en general, hay que mantener el orden):

$$(A+B)(A+B) = A \cdot A + A \cdot B + B \cdot A + B \cdot B = A^2 + AB + BA + B^2$$

> **¡Atención!** Aparecen $AB$ **y** $BA$ por separado.

**Paso 2 — Comparar con $A^2 + 2AB + B^2$.** Esta segunda expresión tiene $2AB$ en lugar de $AB + BA$. Solo serían iguales si $AB = BA$ — lo cual NO siempre pasa.

**Paso 3 — Contraejemplo oficial.** $A = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.

Calculo $A + B = \begin{pmatrix} 2 & 1 \\ 2 & 0 \end{pmatrix}$.

Calculo $(A+B)^2 = (A+B)(A+B)$:
- $(1,1)$: $2 \cdot 2 + 1 \cdot 2 = 6$
- $(1,2)$: $2 \cdot 1 + 1 \cdot 0 = 2$
- $(2,1)$: $2 \cdot 2 + 0 \cdot 2 = 4$
- $(2,2)$: $2 \cdot 1 + 0 \cdot 0 = 2$

$$(A+B)^2 = \begin{pmatrix} 6 & 2 \\ 4 & 2 \end{pmatrix}$$

Calculo $A^2 + 2AB + B^2$:
- $A^2 = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$
- $AB = \begin{pmatrix} 1 \cdot 1 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \\ 1 \cdot 1 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, así $2AB = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$
- $B^2 = \begin{pmatrix} 1 \cdot 1 + 1 \cdot 1 & 1 \cdot 1 + 1 \cdot 0 \\ 1 \cdot 1 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$

Suma: $A^2 + 2AB + B^2 = \begin{pmatrix} 1+2+2 & 0+2+1 \\ 1+2+1 & 0+2+1 \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 4 & 3 \end{pmatrix}$

**No coinciden:** $\begin{pmatrix} 6 & 2 \\ 4 & 2 \end{pmatrix} \neq \begin{pmatrix} 5 & 3 \\ 4 & 3 \end{pmatrix}$ ✓ contraejemplo válido.

**Paso 4 — Hipótesis adicional para que la igualdad sea cierta.** Necesitamos $AB = BA$. Bajo esa hipótesis, $AB + BA = AB + AB = 2AB$, y la fórmula del paso 1 colapsa en $A^2 + 2AB + B^2$.

#### Parte 2 — FALSO en general

**Paso 1 — Aplicar la traspuesta a $AB$.** Como $A$ y $B$ son simétricas, $A^T = A$ y $B^T = B$. Entonces:

$$(AB)^T = B^T A^T = BA$$

**Paso 2 — Comparar con $AB$.** Para que $AB$ sea simétrica necesitaríamos $(AB)^T = AB$, o sea $BA = AB$. Pero eso no siempre se cumple.

**Paso 3 — Contraejemplo oficial.** $A = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$. Verificá:

- $A^T = A$ ✓ (simétrica)
- $B^T = B$ ✓ (simétrica)

Ahora calculá $AB$:
- $(1,1)$: $1 \cdot 1 + (-1) \cdot 1 = 0$
- $(1,2)$: $1 \cdot 1 + (-1) \cdot 1 = 0$
- $(2,1)$: $-1 \cdot 1 + 2 \cdot 1 = 1$
- $(2,2)$: $-1 \cdot 1 + 2 \cdot 1 = 1$

$$AB = \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}$$

**No es simétrica:** la entrada $(1,2) = 0$ y la $(2,1) = 1$, no son iguales. ✓ contraejemplo válido.

**Paso 4 — Hipótesis adicional.** $AB = BA$ (es el resultado del ejercicio V.5.2 — bajo simetría, $AB$ simétrica $\iff AB = BA$).

#### Parte 3 — VERDADERO

Demo paso a paso en `matrices-DEMOSTRACIONES.md` §E.4. Idea: verificar que $(A^{-1})^T$ multiplicada por $A^T$ da $\text{Id}$, usando la propiedad 4 de traspuesta al revés.

---

## 🔴 Ejercicio V.17 — $\lambda \text{Id}$ conmuta con todo (NO SE PIDE — el profe dijo "podría ser opcional")

**Enunciado.**

1. Probar que $\lambda \cdot \text{Id}_{n \times n}$ conmuta con todas las matrices, $\forall \lambda \in \mathbb{R}$.
2. Probar que si la matriz $A$, $n \times n$, conmuta con todas las matrices, entonces $\exists \lambda \in \mathbb{R}$ tal que $A = \lambda \cdot \text{Id}_{n \times n}$.

### Solución (esquema)

**Parte 1.** Sea $M$ cualquier matriz $n \times n$:

$$(\lambda \text{Id}) \cdot M = \lambda \cdot (\text{Id} \cdot M) = \lambda \cdot M = M \cdot \lambda = (M \cdot \text{Id}) \cdot \lambda = M \cdot (\lambda \text{Id})$$

Conmutan. $\blacksquare$

**Parte 2.** Hipótesis: $A \cdot B = B \cdot A$ para toda $B$ $n \times n$. Tesis: existe $\lambda \in \mathbb{R}$ tal que $A = \lambda \cdot \text{Id}$.

**Sugerencia (de la cátedra):** considerar $B = ((b_{ij}))$ con $b_{11} = 1$ y todas las demás entradas $0$. Imponer $AB = BA$ lleva a que todas las entradas $a_{ij}$ con $i \neq j$ son cero. Luego, repitiendo con $B$ que tenga $b_{ii} = 1$ y el resto cero para distintos $i$, se concluye que todos los $a_{ii}$ son iguales. Entonces $A = \lambda \cdot \text{Id}$ con $\lambda = a_{11}$.

---

## 🟢 Ejercicio VI.1 — Inducción sobre $A^n$

**Enunciado.** Sea $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. Probar por inducción que $A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$ para todo $n \geq 1$.

### Solución

Demo paso a paso en `matrices-DEMOSTRACIONES.md` §G.1.

---

## 🟢 Ejercicio VI.2 — Idempotente e invertible

**Enunciado.** $A$ idempotente ($A^2 = A$).

1. Si además es invertible, probar $A = \text{Id}$.
2. Dar ejemplo de idempotente que no sea ni $\mathcal{O}$ ni $\text{Id}$.

### Solución

**Parte 1 — demo:** ver `matrices-DEMOSTRACIONES.md` §F.1.

**Parte 2 — ejemplo:** $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. Verificás que $A^2 = A$; no es $\mathcal{O}$ ni $\text{Id}$. (Esta no es invertible — coherente con la parte 1.)

---

## 🟢 Ejercicio VI.3 — $A^3 = \mathcal{O} \implies (A + \text{Id})^{-1} = A^2 - A + \text{Id}$

**Enunciado.** $A$ matriz con $A^3 = \mathcal{O}$.

1. Probar que $(A + \text{Id})$ es invertible y $(A + \text{Id})^{-1} = A^2 - A + \text{Id}$.
2. Aplicar para hallar $B^{-1}$ con $B = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$.

### Solución

#### Parte 1 — demostración

Demo paso a paso en `matrices-DEMOSTRACIONES.md` §H.2.

> **Idea:** verificar que $(A + \text{Id})(A^2 - A + \text{Id}) = A^3 + \text{Id} = \mathcal{O} + \text{Id} = \text{Id}$. Eso prueba que $A^2 - A + \text{Id}$ es la inversa.

#### Parte 2 — aplicación al $B$ concreto

**Paso 1 — Reconocer la estructura.** $B$ tiene unos en la diagonal y "perturbaciones" arriba: $B = \text{Id} + (\text{algo nilpotente})$. Definimos:

$$A = B - \text{Id}$$

Restando entrada por entrada (sólo la diagonal cambia):

$$A = \begin{pmatrix} 1-1 & 1 & 0 & 0 \\ 0 & 1-1 & 0 & 1 \\ 0 & 0 & 1-1 & 0 \\ 0 & 0 & 0 & 1-1 \end{pmatrix} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

> **¿Por qué hago esto?** Porque la fórmula del ejercicio aplica a $A + \text{Id}$, así que necesito identificar quién es $A$ a partir de $B$. Despejando: $A = B - \text{Id}$.

**Paso 2 — Verificar que $A^3 = \mathcal{O}$ (la hipótesis necesaria).** Calculo $A^2$:

Para la entrada $(1,4)$ de $A^2$: fila 1 de $A$ es $0, 1, 0, 0$ (horizontal). Columna 4 de $A$ es $0, 1, 0, 0$ leída de arriba a abajo (vertical). Multiplicando par a par y sumando: $0 \cdot 0 + 1 \cdot 1 + 0 \cdot 0 + 0 \cdot 0 = 1$.

El resto de entradas dan cero (ejercicio: convencete). Entonces:

$$A^2 = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

Calculo $A^3 = A^2 \cdot A$. La fila 1 de $A^2$ es $(0, 0, 0, 1)$ y solo "ve" la fila 4 de $A$, que es toda ceros. Entonces todas las entradas de $A^3$ son cero:

$$A^3 = \mathcal{O} \quad \checkmark$$

**Paso 3 — Aplicar la fórmula del ejercicio.** Como $A^3 = \mathcal{O}$, podemos usar:

$$(A + \text{Id})^{-1} = A^2 - A + \text{Id}$$

Y como $B = A + \text{Id}$, eso es justamente $B^{-1}$:

$$B^{-1} = A^2 - A + \text{Id}$$

**Paso 4 — Calcular numéricamente $A^2 - A + \text{Id}$.**

$$A^2 = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad -A = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad \text{Id} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

Sumando entrada por entrada:

$$\boxed{B^{-1} = A^2 - A + \text{Id} = \begin{pmatrix} 1 & -1 & 0 & 1 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}}$$

**Paso 5 — Verificación: comprobar $B \cdot B^{-1} = \text{Id}$.** Calculamos algunas entradas para asegurarnos:

- $(1,1)$: fila 1 de $B$ es $1, 1, 0, 0$ (horizontal). Columna 1 de $B^{-1}$ es $1, 0, 0, 0$ de arriba a abajo. Producto: $1 \cdot 1 + 1 \cdot 0 + 0 \cdot 0 + 0 \cdot 0 = 1$ ✓
- $(1,2)$: misma fila 1 de $B$ ($1, 1, 0, 0$). Columna 2 de $B^{-1}$ es $-1, 1, 0, 0$ de arriba a abajo. Producto: $1 \cdot (-1) + 1 \cdot 1 + 0 + 0 = 0$ ✓
- $(1,4)$: misma fila 1. Columna 4 de $B^{-1}$ es $1, -1, 0, 1$ de arriba a abajo. Producto: $1 \cdot 1 + 1 \cdot (-1) + 0 + 0 = 0$ ✓
- $(2,2)$: fila 2 de $B$ es $0, 1, 0, 1$. Columna 2 de $B^{-1}$ ($-1, 1, 0, 0$). Producto: $0 + 1 \cdot 1 + 0 + 1 \cdot 0 = 1$ ✓
- $(2,4)$: misma fila 2. Columna 4 ($1, -1, 0, 1$). Producto: $0 \cdot 1 + 1 \cdot (-1) + 0 + 1 \cdot 1 = 0$ ✓

Continuando con todas las entradas:

$$B \cdot B^{-1} = \text{Id}_{4 \times 4} \quad \checkmark$$

> **Idea central del ejercicio:** identificar la estructura $B = \text{Id} + A$ con $A$ nilpotente te permite aplicar una fórmula cerrada para la inversa. Sin esa estructura, calcular $B^{-1}$ por método directo en $4 \times 4$ sería un dolor.

---

# PARTE 8 — Errores comunes que el profesor mencionó

## Los errores que el profesor mencionó explícitamente

Este es el oro del documento. El profesor dice repetidamente cuáles son los errores típicos en parcial. **Leelos con mucha atención.**

| # | Error | Cuándo ocurre | Cómo evitarlo |
|---|-------|---------------|---------------|
| 1 | Asumir $A \cdot B = B \cdot A$ | En cálculos, despejes, demostraciones | Tratar siempre $A \cdot B$ y $B \cdot A$ como distintos. Solo intercambiar si tenés una hipótesis explícita o si es con $\text{Id}$, $\mathcal{O}$, $A^k$. |
| 2 | Aplicar mal la traspuesta del producto | Escribir $(AB)^T = A^T B^T$ | El orden se invierte: $(AB)^T = B^T A^T$. |
| 3 | Aplicar mal la inversa del producto | Escribir $(AB)^{-1} = A^{-1} B^{-1}$ | El orden se invierte: $(AB)^{-1} = B^{-1} A^{-1}$. |
| 4 | "Pasar dividiendo" una matriz | En despejes de ecuaciones matriciales | Multiplicar por la inversa **del mismo lado** en ambos miembros. Verificar primero que la inversa exista. |
| 5 | Mover factores de lado al despejar | Cambiar $A^{-1}$ a la otra punta de la expresión | El orden importa: si la $A$ estaba a la izquierda, la $A^{-1}$ tiene que ir a la izquierda. |
| 6 | Sumar un número con una matriz | Factor común "$X + AX = (A + 1)X$" | Hay que escribir $\text{Id} \cdot X$ explícitamente: $X + AX = (A + \text{Id})X$. |
| 7 | Olvidar que la inversa requiere matriz cuadrada | Hablar de "inversa" de una matriz $2 \times 3$ | Solo hay inversa para matrices cuadradas. |
| 8 | Asumir $A + B$ invertible si $A, B$ lo son | En razonamientos teóricos | NO es cierto. Contraejemplo: $A = \text{Id}, B = -\text{Id}$. |
| 9 | Confundir simétrica con antisimétrica | En ejercicios V/F | Simétrica: $A^T = A$. Antisimétrica: $A^T = -A$. La antisimétrica tiene **diagonal nula**. |
| 10 | Aplicar la ley de simplificación sin verificar invertibilidad | $AB = AC \implies B = C$ sin pedir que $A$ sea invertible | Solo vale si $A$ es invertible. Sin esa hipótesis, contraejemplo en V.11. |

> "Importante, no subestimen las cuentas porque después en los parciales el tiempo no sobra y a veces tiene que estar como ágil para las cuentas"

> "La verdad que en ningún parcial aparece que asume que conmuta y cuando no, no es así"

> 📐 **Sobre demostraciones, esquema oficial, auditoría con citas de clase y mapa de técnicas por ejercicio:** todo eso vive en `matrices-DEMOSTRACIONES.md` (mismo folder). Acá no se duplica.

---

# PARTE 9 — Resumen final imprescindible

Si tenés que repasar 30 minutos antes del parcial, mirá esto.

## Resumen de fórmulas memorizables

### Operaciones básicas

- Suma: $C = A + B \iff c_{ij} = a_{ij} + b_{ij}$
- Escalar: $kA = ((k \cdot a_{ij}))$
- Producto: $c_{ik} = \sum_j a_{ij} b_{jk}$ (fila por columna)

### Traspuesta — 4 propiedades

1. $(A^T)^T = A$
2. $(A + B)^T = A^T + B^T$
3. $(\alpha A)^T = \alpha A^T$
4. $(AB)^T = B^T A^T$ ← **orden invertido**

### Inversa — 4 propiedades

1. $(A^{-1})^{-1} = A$
2. $(AB)^{-1} = B^{-1} A^{-1}$ ← **orden invertido**
3. $(\alpha A)^{-1} = \frac{1}{\alpha} A^{-1}$
4. $(A^T)^{-1} = (A^{-1})^T$

### Traza — 4 propiedades

1. $tr(A + B) = tr(A) + tr(B)$
2. $tr(\alpha A) = \alpha \cdot tr(A)$
3. $tr(A^T) = tr(A)$
4. $tr(AB) = tr(BA)$ ← **vale aunque $AB \neq BA$**

### Tipos especiales — definiciones

| Tipo | Definición |
|------|-----------|
| Simétrica | $A^T = A$ |
| Antisimétrica | $A^T = -A$ (diagonal nula) |
| Idempotente | $A^2 = A$ |
| Nilpotente grado $k$ | $A^k = \mathcal{O}$, $A^{k-1} \neq \mathcal{O}$ |
| Ortogonal | $A^{-1} = A^T$ (equivale a $A A^T = \text{Id}$) |
| Invertible | Existe $A^{-1}$ tal que $AA^{-1} = A^{-1}A = \text{Id}$ |

---

## Las 5 cosas que NO podés equivocar

1. **El producto NO es conmutativo.** $A \cdot B \neq B \cdot A$ en general.
2. **El orden se invierte** en $(AB)^T = B^T A^T$ y $(AB)^{-1} = B^{-1} A^{-1}$.
3. **No se divide matrices.** Para despejar, multiplicar por la inversa **del mismo lado** en ambos miembros.
4. **No se suma número con matriz.** $X + AX = (\text{Id} + A) X$, no "$(1 + A) X$".
5. **La inversa requiere matriz cuadrada** (y aún así, no toda cuadrada es invertible).

## Las 4 cosas que se demuestran tomando $(\cdot)^T$ o $(\cdot)^{-1}$

1. $(AB)^T = B^T A^T$
2. $(AB)^{-1} = B^{-1} A^{-1}$
3. $A$ simétrica + $B$ simétrica + $AB = BA$ → $AB$ simétrica
4. $A$ invertible → $A^T$ invertible y $(A^T)^{-1} = (A^{-1})^T$

## Las 3 cosas que se demuestran tomando $tr(\cdot)$

1. $tr(AB) = tr(BA)$ (a pesar de que $AB \neq BA$)
2. **No existen** $A, B$ con $AB - BA = \text{Id}$
3. $tr(A^T) = tr(A)$

## Las 2 cosas que se demuestran factorizando

1. $A^k - p(A) = \text{Id} \implies A^{-1} = (\text{algo en función de }A)$ — método para hallar inversa por ecuaciones matriciales (ejercicios V.8, V.10, VI.3)
2. $A$ idempotente e invertible → $A = \text{Id}$ (multiplicando $A^2 = A$ por $A^{-1}$, ejercicio VI.2)

## Los 3 patrones de inducción del práctico

1. V.4: $A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix} \implies A^n = \begin{pmatrix} 1 & n & \frac{n^2+n}{2} \\ 0 & 1 & n \\ 0 & 0 & 1 \end{pmatrix}$
2. V.10.3: $A^2 = 2A - \text{Id} \implies A^n = nA - (n-1)\text{Id}$
3. VI.1: $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \implies A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$

**Esquema común:** Base ($n = 2$ o $n = 1$), Hipótesis ($n = h$), Tesis ($n = h+1$), Demostración usando $A^{h+1} = A^h \cdot A$ y la hipótesis inductiva.

---

> "Vamos a ver más adelante" — *el profesor, en cada clase, sobre lo que no entra todavía*

> "En el parcial..." — *referencia constante; tomalo como aviso*

---

# 📐 Demostraciones — archivo separado

**Todas las demos formales del módulo viven en `matrices-DEMOSTRACIONES.md`** (mismo folder). Acá en el archivo principal solo verás **referencias** del estilo "demo en demos.md §X.Y" cuando aparezca una propiedad. Para ver la demostración paso a paso con hipótesis, tesis, justificaciones y QED, abrí ese archivo.

¡Suerte en el parcial! Si entendés todo lo de acá (especialmente la PARTE 7 con los ejercicios del práctico resueltos) **y** sabés reproducir las demos del archivo `matrices-DEMOSTRACIONES.md`, tenés cubierto el módulo entero de matrices.
