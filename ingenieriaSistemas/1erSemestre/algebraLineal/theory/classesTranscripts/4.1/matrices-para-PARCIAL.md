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

**Sobre demostraciones específicamente:** En la **PARTE 8** de este documento hay una **auditoría exhaustiva** que va propiedad por propiedad indicando si el profesor dijo que se pide demostrar, si quedó como opcional, o si demostró ese caso en clase. Leela antes de elegir qué priorizar al estudiar.

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
| 8 | **Errores comunes, auditoría exhaustiva y checklist para el parcial** |
| 9 | **Resumen final imprescindible** |
| 10 | **Banco de demostraciones 🟢 paso a paso (todas las que el profesor hizo)** |

---

# PARTE 1 — ¿Qué es una matriz?

## La idea en una oración

Una matriz es una **tabla rectangular de números reales**, con un cierto número de filas y un cierto número de columnas. Eso es todo. Cada lugar de la tabla se llama **entrada** o **casillero**, y guarda un número.

## La analogía

Pensá en una matriz como una **planilla de Excel** chiquita, con números en cada celda. La fila te dice en qué renglón está, la columna te dice en qué línea vertical. Cada celda tiene una dirección única (fila, columna).

## Notación formal

Si una matriz $A$ tiene $m$ filas y $n$ columnas, se dice que pertenece al conjunto $\mathcal{M}_{m \times n}(\mathbb{R})$.

**Traducción del símbolo:**
- $\mathcal{M}$ — el conjunto de "todas las matrices"
- $m \times n$ — la dimensión: $m$ filas por $n$ columnas (en ese orden, primero filas)
- $(\mathbb{R})$ — los números que viven adentro son **reales** (positivos, negativos, fraccionarios, irracionales — cualquier número real)

Cada entrada se nombra $a_{ij}$:
- $i$ = número de fila (de arriba hacia abajo)
- $j$ = número de columna (de izquierda a derecha)

Por ejemplo, $a_{23}$ es la entrada de la **fila 2, columna 3**.

**Importante:** El primer subíndice es siempre la fila, el segundo es siempre la columna. Este orden no se cambia nunca.

## Ejemplo concreto

$$A = \begin{pmatrix} 1 & 2 & -1 & 5 \\ 3 & -4 & 5 & 0 \\ -2 & 0 & 3 & 4 \end{pmatrix}$$

Esta matriz:
- Tiene **3 filas y 4 columnas**, así que $A \in \mathcal{M}_{3 \times 4}(\mathbb{R})$
- $a_{23} = 5$ (fila 2, columna 3)
- $a_{34} = 4$ (fila 3, columna 4)
- $a_{11} = 1$ (esquina superior izquierda)

---

## Igualdad de matrices

Dos matrices $A$ y $B$ son iguales si, y solo si, cumplen **dos condiciones**:

1. **Misma dimensión** (mismo número de filas y mismo número de columnas)
2. **Todas las entradas correspondientes son iguales**: $a_{ij} = b_{ij}$ para todo $i, j$

Si una de las dos condiciones falla, las matrices son distintas.

**Por qué importa esto en el parcial:** te van a pedir cosas como "encontrá $a, b, c, d$ tales que esta matriz sea igual a esta otra". Lo que hacés es plantear $a_{ij} = b_{ij}$ entrada por entrada y resolver el sistema que sale.

---

# PARTE 2 — Tipos de matrices

## Matriz fila y matriz columna

- **Matriz fila** (también "vector fila"): tiene una sola fila. $A \in \mathcal{M}_{1 \times n}(\mathbb{R})$.

$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \end{pmatrix}$$

- **Matriz columna** (también "vector columna"): tiene una sola columna. $A \in \mathcal{M}_{m \times 1}(\mathbb{R})$.

$$A = \begin{pmatrix} a_{11} \\ a_{21} \\ \vdots \\ a_{m1} \end{pmatrix}$$

---

## Matriz cuadrada

Una matriz es **cuadrada** si tiene **igual cantidad de filas que de columnas** ($m = n$). Pertenece a $\mathcal{M}_{n \times n}(\mathbb{R})$.

$$A = \begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix} \in \mathcal{M}_{2 \times 2}(\mathbb{R})$$

**Por qué importa:** Casi todas las cosas interesantes (inversa, traza, simetría, determinante, sistemas) requieren que la matriz sea cuadrada. Si no es cuadrada, no podés ni hablar de inversa.

> "Siempre que hablamos de matriz inversa estamos en matrices cuadradas"

---

## Diagonal principal

Los elementos $a_{ii}$ (donde fila = columna) forman la **diagonal principal**: $a_{11}, a_{22}, a_{33}, \ldots, a_{nn}$. Va de la esquina superior izquierda a la inferior derecha.

```
| a₁₁  a₁₂  a₁₃ |        ← a₁₁ es diagonal
| a₂₁  a₂₂  a₂₃ |        ← a₂₂ es diagonal
| a₃₁  a₃₂  a₃₃ |        ← a₃₃ es diagonal
```

---

## Matriz triangular superior

Una matriz cuadrada es **triangular superior** si todos los elementos **debajo** de la diagonal principal son cero.

**En lenguaje formal:** $a_{ij} = 0$ para todo $i > j$. (Si la fila es mayor que la columna, la entrada es cero.)

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & -1 \\ 0 & 0 & 2 \end{pmatrix}$$

Los ceros están **debajo** de la diagonal: $a_{21}=0$, $a_{31}=0$, $a_{32}=0$.

---

## Matriz triangular inferior

Una matriz cuadrada es **triangular inferior** si todos los elementos **encima** de la diagonal principal son cero.

**En lenguaje formal:** $a_{ij} = 0$ para todo $i < j$.

$$A = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 4 & 0 \\ 3 & -1 & 2 \end{pmatrix}$$

Los ceros están **encima** de la diagonal.

---

## Matriz diagonal

Una matriz cuadrada es **diagonal** si todos los elementos **fuera** de la diagonal principal son cero. Es decir, es triangular superior **e** inferior al mismo tiempo.

$$D = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 2 \end{pmatrix}$$

Solo la diagonal puede tener números distintos de cero. (Los de la diagonal pueden ser cero también — la nula también es diagonal.)

---

## Matriz identidad

La **identidad** es una matriz **diagonal** cuyos elementos de la diagonal son todos $1$.

$$\text{Id}_{2 \times 2} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad \text{Id}_{3 \times 3} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

**Su propiedad clave:** es el **neutro del producto de matrices**. Es decir, multiplicar cualquier matriz por la identidad (del lado correcto) la deja igual:

$$A \cdot \text{Id} = \text{Id} \cdot A = A$$

**Analogía:** la identidad es a las matrices lo que el $1$ es a los números. $5 \cdot 1 = 5$, $A \cdot \text{Id} = A$.

**Cuando no se aclara la dimensión**, se escribe simplemente $\text{Id}$ o $I$.

---

## Matriz nula

La **nula** es la matriz que tiene **todas sus entradas iguales a cero**. Se nota $\mathcal{O}_{m \times n}$ (o simplemente $\mathcal{O}$ si la dimensión está clara por contexto).

$$\mathcal{O}_{3 \times 3} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

**Su propiedad clave:** es el **neutro de la suma**:

$$A + \mathcal{O} = \mathcal{O} + A = A$$

**Analogía:** la nula es a las matrices lo que el $0$ es a los números.

---

## Tabla resumen de tipos

| Tipo | Forma | Condición |
|------|-------|-----------|
| Fila | $1 \times n$ | una sola fila |
| Columna | $m \times 1$ | una sola columna |
| Cuadrada | $n \times n$ | $m = n$ |
| Triangular superior | $n \times n$ | $a_{ij} = 0$ si $i > j$ |
| Triangular inferior | $n \times n$ | $a_{ij} = 0$ si $i < j$ |
| Diagonal | $n \times n$ | $a_{ij} = 0$ si $i \neq j$ |
| Identidad | $n \times n$ | diagonal con $1$ en la diagonal |
| Nula | $m \times n$ | todas las entradas son $0$ |

---

# PARTE 3 — Operaciones con matrices

## Suma de matrices

### ¿Qué dice?

Para sumar dos matrices, **sumás entrada con entrada**, en la misma posición. La nueva matriz tiene en cada lugar la suma de los lugares originales.

### Requisito

Las dos matrices **tienen que tener la misma dimensión**. Si una es $2 \times 3$ y la otra es $3 \times 2$, no se pueden sumar.

### Fórmula

Si $A = ((a_{ij}))$ y $B = ((b_{ij}))$ son ambas $m \times n$, entonces $C = A + B$ se define como:

$$c_{ij} = a_{ij} + b_{ij} \quad \forall i, j$$

### Ejemplo numérico

$$\begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix} + \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 1+2 & 2+1 \\ 3+3 & -4+4 \end{pmatrix} = \begin{pmatrix} 3 & 3 \\ 6 & 0 \end{pmatrix}$$

### Propiedades

| Propiedad | Significado | Estado parcial |
|-----------|-------------|---------------|
| Cerradura | La suma de dos matrices $m \times n$ es otra $m \times n$ | 🟡 saber/aplicar |
| Conmutativa | $A + B = B + A$ | 🟡 saber/aplicar |
| Asociativa | $(A + B) + C = A + B + C$ | 🟡 saber/aplicar |
| Existencia de neutro | Existe la nula $\mathcal{O}$ tal que $A + \mathcal{O} = A$ | 🟡 saber/aplicar |
| Existencia de opuesto | Para toda $A$ existe $-A$ tal que $A + (-A) = \mathcal{O}$ | 🟡 saber/aplicar |

**Importante:** la suma **sí es conmutativa**, a diferencia del producto. Acordate de esto, porque el producto NO conmuta y se confunde fácil.

> 🟡 **Por qué van como "saber/aplicar":** estas 5 propiedades son las propiedades clásicas de cualquier suma. El profesor no las demostró en clase ni las puso como demos pedibles — son hechos básicos que tenés que tener internalizados para usar al manipular matrices en cualquier ejercicio. **No estudies una demo formal de estas; estudiá saber CUÁL aplicaste cuando hagas un despeje.**

---

## Producto por un escalar

### ¿Qué dice?

Multiplicar una matriz por un número $k$ (un "escalar") significa multiplicar **cada entrada** por ese número.

### Fórmula

Si $A = ((a_{ij}))$ y $k \in \mathbb{R}$, entonces $k \cdot A = ((k \cdot a_{ij}))$.

### Ejemplo numérico

$$2 \cdot \begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix} = \begin{pmatrix} 2 \cdot 1 & 2 \cdot 2 \\ 2 \cdot 3 & 2 \cdot (-4) \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ 6 & -8 \end{pmatrix}$$

### Propiedades

| Propiedad | Significado | Estado parcial |
|-----------|-------------|---------------|
| $(\alpha \cdot \beta) \cdot A = \alpha \cdot (\beta \cdot A)$ | Asociativa de escalares | 🟡 saber/aplicar |
| $(\alpha + \beta) \cdot A = \alpha A + \beta A$ | Distributiva sobre suma de escalares | 🟡 saber/aplicar |
| $\alpha \cdot (A + B) = \alpha A + \alpha B$ | Distributiva sobre suma de matrices | 🟡 saber/aplicar |
| $1 \cdot A = A$ | El $1$ es neutro del escalar | 🟡 saber/aplicar |

---

## Producto de matrices

Esta es la operación más importante (y la que más complicada se hace al principio). Hay que entenderla bien para el parcial.

### Requisito de **conformabilidad**

Para multiplicar $A$ por $B$ (en el orden $A \cdot B$), **el número de columnas de $A$ tiene que ser igual al número de filas de $B$**.

Visualmente:

$$A \in \mathcal{M}_{m \times n}, \quad B \in \mathcal{M}_{n \times p} \implies A \cdot B \in \mathcal{M}_{m \times p}$$

Las dimensiones "del medio" (las dos $n$) tienen que coincidir; las dimensiones "de afuera" ($m$ y $p$) determinan el tamaño del resultado.

**Truco visual:** escribí las dimensiones una al lado de la otra: $(m \times \mathbf{n}) \cdot (\mathbf{n} \times p)$. Si las del medio coinciden, el producto se puede hacer y el resultado es $(m \times p)$.

**Si no coinciden:** no se pueden multiplicar en ese orden. Capaz se pueden multiplicar en el otro orden ($B \cdot A$), pero no es lo mismo.

### Fórmula del producto

Si $A \in \mathcal{M}_{m \times n}$ y $B \in \mathcal{M}_{n \times p}$, entonces $C = A \cdot B$ es la matriz $m \times p$ definida como:

$$c_{ik} = \sum_{j=1}^{n} a_{ij} \cdot b_{jk}$$

**Traducción simple de la fórmula:**
- $c_{ik}$ es el numerito que va en el resultado, en la fila $i$ y columna $k$.
- Para calcularlo, agarrás la **fila $i$ de $A$** y la **columna $k$ de $B$**.
- Multiplicás los números que quedan enfrentados.
- Sumás esos productos.

La fórmula con $\sum$ solo es una forma corta de escribir:

$$\text{casillero del resultado} = \text{fila de } A \cdot \text{columna de } B$$

Ese punto no significa "multiplicar matrices completas" en este mini paso. Significa: **multiplicar par a par y sumar**.

### Cómo se hace, paso a paso

Usemos un ejemplo más chico:

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$$

Ambas son $2 \times 2$, así que el resultado también será $2 \times 2$:

$$A \cdot B = \begin{pmatrix} ? & ? \\ ? & ? \end{pmatrix}$$

**Entrada $(1,1)$ del resultado:** fila 1 de $A$ por columna 1 de $B$:

$$\begin{pmatrix} 1 & 2 \end{pmatrix}
\cdot
\begin{pmatrix} 5 \\ 7 \end{pmatrix}
= 1 \cdot 5 + 2 \cdot 7 = 5 + 14 = 19$$

**Entrada $(1,2)$ del resultado:** fila 1 de $A$ por columna 2 de $B$:

$$\begin{pmatrix} 1 & 2 \end{pmatrix}
\cdot
\begin{pmatrix} 6 \\ 8 \end{pmatrix}
= 1 \cdot 6 + 2 \cdot 8 = 6 + 16 = 22$$

**Entrada $(2,1)$ del resultado:** fila 2 de $A$ por columna 1 de $B$:

$$\begin{pmatrix} 3 & 4 \end{pmatrix}
\cdot
\begin{pmatrix} 5 \\ 7 \end{pmatrix}
= 3 \cdot 5 + 4 \cdot 7 = 15 + 28 = 43$$

**Entrada $(2,2)$ del resultado:** fila 2 de $A$ por columna 2 de $B$:

$$\begin{pmatrix} 3 & 4 \end{pmatrix}
\cdot
\begin{pmatrix} 6 \\ 8 \end{pmatrix}
= 3 \cdot 6 + 4 \cdot 8 = 18 + 32 = 50$$

Entonces:

$$A \cdot B = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

**Idea para memorizar:** cada casillero del resultado sale de cruzar una fila de $A$ con una columna de $B$.

```text
fila de A:       1   2
columna de B:    5   7

multiplico:      1·5 + 2·7
sumo:            5 + 14 = 19
```

### Otro ejemplo: producto $3 \times 3$

Ahora hacemos lo mismo, pero con matrices $3 \times 3$. No cambia la idea: cada entrada sigue siendo **fila por columna**.

$$A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \\ 2 & 0 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 0 & 2 \\ 3 & 1 & 0 \\ 0 & 2 & 1 \end{pmatrix}$$

Como son $3 \times 3$ y $3 \times 3$, el resultado será $3 \times 3$:

$$A \cdot B = \begin{pmatrix} ? & ? & ? \\ ? & ? & ? \\ ? & ? & ? \end{pmatrix}$$

Calculamos las **9 entradas** despacio, una por una:

**Entrada $(1,1)$:** fila 1 de $A$ por columna 1 de $B$:

$$\begin{pmatrix} 1 & 2 & 0 \end{pmatrix}
\cdot
\begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}
= 1 \cdot 1 + 2 \cdot 3 + 0 \cdot 0 = 1 + 6 + 0 = 7$$

**Entrada $(1,2)$:** fila 1 de $A$ por columna 2 de $B$:

$$\begin{pmatrix} 1 & 2 & 0 \end{pmatrix}
\cdot
\begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix}
= 1 \cdot 0 + 2 \cdot 1 + 0 \cdot 2 = 0 + 2 + 0 = 2$$

**Entrada $(1,3)$:** fila 1 de $A$ por columna 3 de $B$:

$$\begin{pmatrix} 1 & 2 & 0 \end{pmatrix}
\cdot
\begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}
= 1 \cdot 2 + 2 \cdot 0 + 0 \cdot 1 = 2 + 0 + 0 = 2$$

**Entrada $(2,1)$:** fila 2 de $A$ por columna 1 de $B$:

$$\begin{pmatrix} 0 & 1 & 3 \end{pmatrix}
\cdot
\begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}
= 0 \cdot 1 + 1 \cdot 3 + 3 \cdot 0 = 0 + 3 + 0 = 3$$

**Entrada $(2,2)$:** fila 2 de $A$ por columna 2 de $B$:

$$\begin{pmatrix} 0 & 1 & 3 \end{pmatrix}
\cdot
\begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix}
= 0 \cdot 0 + 1 \cdot 1 + 3 \cdot 2 = 0 + 1 + 6 = 7$$

**Entrada $(2,3)$:** fila 2 de $A$ por columna 3 de $B$:

$$\begin{pmatrix} 0 & 1 & 3 \end{pmatrix}
\cdot
\begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}
= 0 \cdot 2 + 1 \cdot 0 + 3 \cdot 1 = 0 + 0 + 3 = 3$$

**Entrada $(3,1)$:** fila 3 de $A$ por columna 1 de $B$:

$$\begin{pmatrix} 2 & 0 & 1 \end{pmatrix}
\cdot
\begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}
= 2 \cdot 1 + 0 \cdot 3 + 1 \cdot 0 = 2 + 0 + 0 = 2$$

**Entrada $(3,2)$:** fila 3 de $A$ por columna 2 de $B$:

$$\begin{pmatrix} 2 & 0 & 1 \end{pmatrix}
\cdot
\begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix}
= 2 \cdot 0 + 0 \cdot 1 + 1 \cdot 2 = 0 + 0 + 2 = 2$$

**Entrada $(3,3)$:** fila 3 de $A$ por columna 3 de $B$:

$$\begin{pmatrix} 2 & 0 & 1 \end{pmatrix}
\cdot
\begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}
= 2 \cdot 2 + 0 \cdot 0 + 1 \cdot 1 = 4 + 0 + 1 = 5$$

Pegamos las 9 entradas en su lugar:

$$A \cdot B =
\begin{pmatrix}
7 & 2 & 2 \\
3 & 7 & 3 \\
2 & 2 & 5
\end{pmatrix}$$

Fijate que en el $2 \times 2$ multiplicábamos y sumábamos **2 pares** de números. En el $3 \times 3$, multiplicamos y sumamos **3 pares** de números. Esa es toda la diferencia.

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

## 🟢 Producto por vectores canónicos (cae como ejercicio V.3)

> **Estado parcial: 🟢 SE PIDE.** El profesor lo demostró en clase 2 (líneas 165-171) y el ejercicio V.3 del práctico lo pide explícitamente. Es un atajo que ahorra mucho tiempo en parciales. Demostración formal en **PARTE 10 — sección A.1**.

### El nombre asusta, la idea no

Olvidate por un segundo de la palabra "canónico". Lo único que estamos por ver son **3 vectores columna muy especiales** que tienen una pinta tonta: son **una columna de ceros con un solo 1 metido en algún lugar**.

Hay tres versiones (para matrices de 3 filas):

$$\vec{v}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{v}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

**Cómo leerlos:**
- $\vec{v}_1$ tiene el $1$ en la **posición 1** (arriba).
- $\vec{v}_2$ tiene el $1$ en la **posición 2** (medio).
- $\vec{v}_3$ tiene el $1$ en la **posición 3** (abajo).

El subíndice del nombre te dice **dónde está el 1**. Eso es todo.

> **Analogía:** son como botones de un control remoto. El $\vec{v}_1$ es el botón "1", el $\vec{v}_2$ el botón "2", el $\vec{v}_3$ el botón "3". Cuando los apretás contra una matriz, pasa algo muy específico. Vamos a ver qué.

### Probémoslo con números reales

Tomemos una matriz cualquiera, sin letras, solo números:

$$A = \begin{pmatrix} 4 & 7 & 9 \\ 5 & 8 & 1 \\ 6 & 2 & 3 \end{pmatrix}$$

Las **columnas** de $A$ son:

$$\text{col 1} = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}, \quad \text{col 2} = \begin{pmatrix} 7 \\ 8 \\ 2 \end{pmatrix}, \quad \text{col 3} = \begin{pmatrix} 9 \\ 1 \\ 3 \end{pmatrix}$$

Ahora multipliquemos $A \cdot \vec{v}_1$ a lo bruto, fila por columna como siempre:

$$A \cdot \vec{v}_1 =
\begin{pmatrix} 4 & 7 & 9 \\ 5 & 8 & 1 \\ 6 & 2 & 3 \end{pmatrix}
\cdot
\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
=
\begin{pmatrix}
4 \cdot 1 + 7 \cdot 0 + 9 \cdot 0 \\
5 \cdot 1 + 8 \cdot 0 + 1 \cdot 0 \\
6 \cdot 1 + 2 \cdot 0 + 3 \cdot 0
\end{pmatrix}
=
\begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}$$

Mirá qué pasó: **dio exactamente la columna 1 de $A$**.

¿Por qué? Porque el $1$ del $\vec{v}_1$ estaba arriba, así que en cada fila de $A$ **solo sobrevivió el primer número** (los otros dos los multiplicó por cero y desaparecieron).

### Probemos con $\vec{v}_2$

$$A \cdot \vec{v}_2 =
\begin{pmatrix} 4 & 7 & 9 \\ 5 & 8 & 1 \\ 6 & 2 & 3 \end{pmatrix}
\cdot
\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}
=
\begin{pmatrix}
4 \cdot 0 + 7 \cdot 1 + 9 \cdot 0 \\
5 \cdot 0 + 8 \cdot 1 + 1 \cdot 0 \\
6 \cdot 0 + 2 \cdot 1 + 3 \cdot 0
\end{pmatrix}
=
\begin{pmatrix} 7 \\ 8 \\ 2 \end{pmatrix}$$

**Dio la columna 2 de $A$.** Porque ahora el $1$ del vector estaba en la **posición 2**, así que de cada fila de $A$ solo sobrevivió el segundo número.

### Y con $\vec{v}_3$

$$A \cdot \vec{v}_3 =
\begin{pmatrix} 4 & 7 & 9 \\ 5 & 8 & 1 \\ 6 & 2 & 3 \end{pmatrix}
\cdot
\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
=
\begin{pmatrix}
4 \cdot 0 + 7 \cdot 0 + 9 \cdot 1 \\
5 \cdot 0 + 8 \cdot 0 + 1 \cdot 1 \\
6 \cdot 0 + 2 \cdot 0 + 3 \cdot 1
\end{pmatrix}
=
\begin{pmatrix} 9 \\ 1 \\ 3 \end{pmatrix}$$

**Dio la columna 3 de $A$.** Misma lógica: el $1$ está abajo, sobrevive el tercer número de cada fila.

### El truco en una sola frase

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

### ¿Qué es?

La traspuesta de $A$ se obtiene **intercambiando filas por columnas**. Lo que era fila pasa a ser columna, y viceversa. Se nota $A^T$ (a veces $A^t$ con minúscula).

**Si $A$ es $m \times n$, entonces $A^T$ es $n \times m$** (las dimensiones se invierten).

**Fórmula:** si $A = ((a_{ij}))$, entonces $A^T = ((b_{ji}))$ donde $b_{ji} = a_{ij}$.

### Ejemplo

$$A = \begin{pmatrix} 1 & 2 \\ 3 & -4 \\ 2 & 1 \end{pmatrix} \in \mathcal{M}_{3 \times 2} \implies A^T = \begin{pmatrix} 1 & 3 & 2 \\ 2 & -4 & 1 \end{pmatrix} \in \mathcal{M}_{2 \times 3}$$

La fila 1 de $A^T$ es la columna 1 de $A$. La fila 2 de $A^T$ es la columna 2 de $A$. Al revés también funciona: la columna 1 de $A^T$ es la fila 1 de $A$.

### Las 4 propiedades de la traspuesta (las 4 son demo pedible)

| # | Propiedad | Comentario | Estado parcial |
|---|-----------|-----------|---------------|
| 1 | $(A^T)^T = A$ | Trasponer dos veces te devuelve a la original | 🟢 SE PIDE — demo pedible |
| 2 | $(A + B)^T = A^T + B^T$ | La traspuesta de la suma es la suma de las traspuestas | 🟢 SE PIDE — demo abajo |
| 3 | $(\alpha \cdot A)^T = \alpha \cdot A^T$ | Los escalares no se afectan | 🟢 SE PIDE — demo abajo |
| 4 | $(A \cdot B)^T = B^T \cdot A^T$ | **EL ORDEN SE INVIERTE** | 🟢 SE PIDE — demo abajo |

> 🟢 **Las 4 son demo pedible.** El profesor dijo en clase 2: *"vamos a ver cuatro propiedades que tenemos que manejar en esta operación"*. **Cualquiera de las 4 puede aparecer como ejercicio "demostrar que..."**. Demostró la 2 y la 3 en clase como modelo. La demo de la 1 es la más corta: si $A = ((a_{ij}))$, entonces $A^T = ((a_{ji}))$, y al trasponer de nuevo $(A^T)^T = ((a_{ij})) = A$. La de la 4 está abajo (necesita sumatorias).

### 🟢 Demostración de la propiedad 2: $(A + B)^T = A^T + B^T$

> **Estado parcial: 🟢 SE PIDE.** El profesor dijo en clase 2 (18-mar) que "tenemos que manejar" las 4 propiedades. Esta es el esquema modelo. **Versión completa con todas las justificaciones en PARTE 10 — sección B.1.**

**Hipótesis:** $A, B \in \mathcal{M}_{m \times n}$. **Tesis:** $(A + B)^T = A^T + B^T$.

$$[A + B]^T = [((a_{ij})) + ((b_{ij}))]^T \quad \text{(definición de suma)}$$
$$= [((a_{ij} + b_{ij}))]^T \quad \text{(suma entrada por entrada)}$$
$$= ((a_{ji} + b_{ji})) \quad \text{(definición de traspuesta: cambiar }i\text{ por }j\text{)}$$
$$= ((a_{ji})) + ((b_{ji})) \quad \text{(separar la suma)}$$
$$= A^T + B^T \quad \blacksquare$$

### 🟢 Demostración de la propiedad 3: $(\alpha A)^T = \alpha A^T$

> **Estado parcial: 🟢 SE PIDE.** El profesor flageó esta como una donde aparece un error común en parcial: poner "$(\alpha A)^T = \alpha^T A^T$", lo cual está mal porque los escalares no se trasponen. **Versión completa en PARTE 10 — sección B.2.**

$$(\alpha \cdot A)^T = ((\alpha \cdot a_{ij}))^T = ((\alpha \cdot a_{ji})) = \alpha \cdot ((a_{ji})) = \alpha \cdot A^T \quad \blacksquare$$

### 🟢 Demostración de la propiedad 4: $(A \cdot B)^T = B^T \cdot A^T$

> **Estado parcial: 🟢 SE PIDE.** Es el error #2 más flageado por el profesor en clase: escribir $(AB)^T = A^T B^T$. **El orden SE INVIERTE.** Esta demo necesita sumatorias.

**Hipótesis:** $A \in \mathcal{M}_{m \times n}$, $B \in \mathcal{M}_{n \times p}$ (conformables).
**Tesis:** $(AB)^T = B^T A^T$.

Sea $C = AB$ con $c_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj}$.

La entrada $(i, j)$ de $C^T$ es la entrada $(j, i)$ de $C$:

$$(C^T)_{ij} = c_{ji} = \sum_{k=1}^{n} a_{jk} \cdot b_{ki} \quad \text{(definición de producto)}$$

La entrada $(i, j)$ de $B^T A^T$, sabiendo que $(B^T)_{ik} = b_{ki}$ y $(A^T)_{kj} = a_{jk}$:

$$(B^T A^T)_{ij} = \sum_{k=1}^{n} b_{ki} \cdot a_{jk} = \sum_{k=1}^{n} a_{jk} \cdot b_{ki} \quad \text{(números reales conmutan dentro de la suma)}$$

Las dos sumatorias son iguales término a término. Entonces $C^T = B^T A^T$, es decir, $(AB)^T = B^T A^T$. $\blacksquare$

### El error común en la propiedad 4

> "El producto de matrices no es conmutativo, así que no podemos escribir $A^T \cdot B^T$. Tiene que ser $B^T \cdot A^T$, con el orden cambiado"

**Por qué se invierte el orden:** porque las matrices no conmutan. Si escribieras $(A \cdot B)^T = A^T \cdot B^T$, las dimensiones ni siquiera te dejarían (¡pensálo!). Si $A$ es $2 \times 3$ y $B$ es $3 \times 4$, entonces $A^T$ es $3 \times 2$ y $B^T$ es $4 \times 3$, así que $A^T \cdot B^T$ ni siquiera se puede hacer. En cambio $B^T \cdot A^T$ sí.

---

## Matriz simétrica

### Definición

Una matriz cuadrada $A$ es **simétrica** si y solo si $A^T = A$.

**Consecuencia:** $a_{ij} = a_{ji}$ para todo $i, j$. Es decir, los elementos en posiciones simétricas respecto a la diagonal son iguales.

### Ejemplo

$$A = \begin{pmatrix} 1 & 3 & 2 \\ 3 & -4 & 1 \\ 2 & 1 & 2 \end{pmatrix}$$

Mirá: $a_{12} = 3$ y $a_{21} = 3$. $a_{13} = 2$ y $a_{31} = 2$. $a_{23} = 1$ y $a_{32} = 1$. Es simétrica.

**Visualmente:** si imaginás un espejo en la diagonal, los números arriba se reflejan iguales abajo.

---

## Matriz antisimétrica

### Definición

Una matriz cuadrada $A$ es **antisimétrica** si y solo si $A^T = -A$.

**Consecuencia 1:** $a_{ij} = -a_{ji}$ (los elementos en posiciones simétricas son **opuestos**).

**Consecuencia 2 (importantísima):** la **diagonal principal es siempre nula**. Porque para los $a_{ii}$ tendríamos $a_{ii} = -a_{ii}$, y el único número que es igual a su opuesto es el $0$.

### Ejemplo

$$A = \begin{pmatrix} 0 & 3 & -2 \\ -3 & 0 & 1 \\ 2 & -1 & 0 \end{pmatrix}$$

Diagonal nula. Y $a_{12} = 3 = -a_{21} = -(-3)$. Es antisimétrica.

---

## Propiedades de simétricas y antisimétricas

| # | Propiedad | Estado parcial |
|---|-----------|---------------|
| 1 | La suma de dos simétricas es simétrica | 🟢 SE PIDE — demo abajo |
| 2 | La suma de dos antisimétricas es antisimétrica | 🟢 SE PIDE — demo análoga |
| 3 | $\alpha \cdot A$ es simétrica si $A$ lo es | 🟢 SE PIDE — demo análoga |
| 4 | $\alpha \cdot A$ es antisimétrica si $A$ lo es | 🟢 SE PIDE — demo análoga |

> 🟢 **Las 4 son demo pedible.** El profesor dijo en clase 2: *"vamos a denunciar cuatro propiedades del estilo y vamos a demostrar alguna de ellas"*. Demostró la 1 entera; las otras 3 las dejó como análogas. **Cualquiera puede aparecer como "demostrar que..."**.

### 🟢 Demostración: suma de simétricas es simétrica

> **Estado parcial: 🟢 SE PIDE.** El profesor la hizo completa en clase 2 (18-mar, líneas 81-90). **Versión completa en PARTE 10 — sección C.1.**

**Hipótesis:** $A, B$ simétricas, es decir, $A^T = A$ y $B^T = B$.
**Tesis:** $A + B$ es simétrica.

$$(A + B)^T = A^T + B^T \quad \text{(propiedad 2 de traspuesta)}$$
$$= A + B \quad \text{(hipótesis: }A, B\text{ simétricas)}$$

Como $(A+B)^T = A+B$, $A+B$ es simétrica. $\blacksquare$

### 🟢 Resultado clave: $AB$ simétrica $\iff AB = BA$ (con $A, B$ simétricas) — ejercicio V.5.2

> **Estado parcial: 🟢 SE PIDE.** El profesor demostró ambas direcciones completas en clase 2 (líneas 177-198). Es uno de los resultados más típicos del módulo. **Versión completa en PARTE 10 — sección C.2.**

**Hipótesis:** $A^T = A$ y $B^T = B$. **Tesis:** $AB$ simétrica $\iff AB = BA$.

**Directo ($\Rightarrow$):** asumimos $AB$ simétrica:

$$AB = (AB)^T = B^T A^T = BA \quad \text{(simétrica + prop 4 trasp + }A^T=A, B^T=B\text{)}$$

**Recíproco ($\Leftarrow$):** asumimos $AB = BA$:

$$(AB)^T = B^T A^T = BA = AB \quad \text{(prop 4 trasp + simétricas + hipótesis)}$$

Como $(AB)^T = AB$, $AB$ es simétrica. Probadas ambas direcciones. $\blacksquare$

### 🟢 Resultado clave: $\frac{1}{2}(A + A^T)$ es simétrica — ejercicio V.6.1

> **Estado parcial: 🟢 SE PIDE.** El profesor lo demostró completo en clase 2 (líneas 199-218). Junto con la análoga $\frac{1}{2}(A - A^T)$ antisimétrica, es la base de la **descomposición $A = $ simétrica $+$ antisimétrica**. **Versión completa en PARTE 10 — sección C.3.**

**Hipótesis:** $A$ cuadrada cualquiera. **Tesis:** $S = \frac{1}{2}(A + A^T)$ es simétrica.

$$S^T = \tfrac{1}{2}(A + A^T)^T = \tfrac{1}{2}(A^T + (A^T)^T) = \tfrac{1}{2}(A^T + A) = \tfrac{1}{2}(A + A^T) = S$$

Por lo tanto $S^T = S$, es decir, $S$ es simétrica. $\blacksquare$

> **Análoga (queda como ejercicio):** $\frac{1}{2}(A - A^T)$ es antisimétrica. Mismo esquema, terminás llegando a $-S$.

---

## Traza de una matriz

### Definición

La **traza** de una matriz cuadrada $A$ es la **suma de los elementos de la diagonal principal**:

$$tr(A) = \sum_{i=1}^{n} a_{ii} = a_{11} + a_{22} + \cdots + a_{nn}$$

**Requisito:** la matriz tiene que ser **cuadrada**.

### Ejemplo

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 3 & -4 & 2 \\ 2 & 1 & 10 \end{pmatrix} \implies tr(A) = 1 + (-4) + 10 = 7$$

### Las 4 propiedades de la traza (las 4 son demo pedible)

| # | Propiedad | Comentario | Estado parcial |
|---|-----------|-----------|---------------|
| 1 | $tr(A + B) = tr(A) + tr(B)$ | La traza distribuye sobre la suma | 🟢 SE PIDE — demo abajo |
| 2 | $tr(\alpha \cdot A) = \alpha \cdot tr(A)$ | Los escalares salen afuera | 🟢 SE PIDE — demo análoga a la 1 |
| 3 | $tr(A^T) = tr(A)$ | La traspuesta no cambia la diagonal | 🟢 SE PIDE — demo corta usando que $a_{ii}$ no cambia al trasponer |
| 4 | $tr(A \cdot B) = tr(B \cdot A)$ | **¡Aunque $AB \neq BA$, sus trazas coinciden!** | 🟢 SE PIDE — demo con doble sumatoria |

> 🟢 **Las 4 son demo pedible.** El profesor dijo: *"al igual que las traspuestas son 4 propiedades que tenemos que manejar"* (clase 2). Demostró la 1 entera. La 4 es la más importante porque es la base de la aplicación estrella *"NO existen $A, B$ con $AB - BA = \text{Id}$"*. **Cualquiera puede aparecer como "demostrar que..."**.

> "A por B es una matriz, B por A es otra, pero sumo las diagonales principales y me da lo mismo. Es algo bastante curioso"

### 🟢 Demostración de la propiedad 1: $tr(A+B) = tr(A) + tr(B)$

> **Estado parcial: 🟢 SE PIDE.** El profesor la hizo completa con sumatorias en clase 2 (líneas 111-122). Es la demo modelo de cómo se prueba algo con sumatorias. **Versión completa en PARTE 10 — sección D.1.**

**Hipótesis:** $A, B \in \mathcal{M}_{n \times n}$. **Tesis:** $tr(A+B) = tr(A) + tr(B)$.

$$tr(A + B) = \sum_{i=1}^{n} (A + B)_{ii} \quad \text{(definición de traza)}$$
$$= \sum_{i=1}^{n} (a_{ii} + b_{ii}) \quad \text{(definición de suma)}$$
$$= \sum_{i=1}^{n} a_{ii} + \sum_{i=1}^{n} b_{ii} \quad \text{(separar la sumatoria)}$$
$$= tr(A) + tr(B) \quad \blacksquare$$

> 🟡 **Análogas (esquema mental):** 
> - $tr(\alpha A) = \alpha \cdot tr(A)$: misma demo pero sale $\alpha$ como factor común de la sumatoria.
> - $tr(A-B) = tr(A) - tr(B)$: corolario inmediato escribiendo $A - B = A + (-1)B$ y aplicando props 1 y 2.
> - $tr(A^T) = tr(A)$: la diagonal principal no cambia al trasponer (el $a_{ii}$ queda en su lugar).

### Por qué la propiedad 4 es importante

Es una excepción notable. Aunque el producto **no conmuta**, la **traza del producto sí**. Esta propiedad permite probar cosas que de otro modo no se podrían.

### 🟢 Aplicación clásica: NO existen $A, B$ tales que $AB - BA = \text{Id}$

> **Estado parcial: 🟢 SE PIDE.** Es **la estrella del módulo de traza**. El profesor la demostró completa en clase 3 (líneas 276-298) y dijo *"vamos a probarla por lo que se llama el absurdo"*. Probabilidad alta de caer en parcial. **Versión completa con todos los detalles en PARTE 10 — sección D.3.**

Probar por **el absurdo**: supongamos que existen.

$$AB - BA = \text{Id}$$

Tomamos traza de ambos lados:

$$tr(AB - BA) = tr(\text{Id})$$

Lado izquierdo: $tr(AB) - tr(BA) = tr(AB) - tr(AB) = 0$ (por propiedad 4).

Lado derecho: $tr(\text{Id}) = 1 + 1 + \cdots + 1 = n$ (sumando $n$ unos).

Entonces $0 = n$. Contradicción (porque $n \geq 1$). Por lo tanto, **no pueden existir** esas matrices. $\blacksquare$

---

# PARTE 5 — Matriz inversa

Esta parte es la más cargada del módulo. Mucho cae en parcial.

## Definición

Una matriz cuadrada $A$ es **invertible** si y solo si **existe** otra matriz $B$ (también $n \times n$) tal que:

$$A \cdot B = B \cdot A = \text{Id}$$

A esa matriz $B$ se la llama **inversa de $A$** y se nota $A^{-1}$.

### Las cosas importantísimas a entender

- La inversa **existe solo para matrices cuadradas**. Si la matriz no es cuadrada, la inversa ni siquiera tiene sentido.
- **No todas las matrices cuadradas son invertibles.** Hay matrices cuadradas sin inversa (por ejemplo, la nula, o cualquier matriz con dos filas iguales o proporcionales).
- La inversa, **cuando existe, es única**.
- Se requiere que $AB = BA = \text{Id}$. Es decir, **multiplicar en cualquier orden** te da la identidad. Esto es notable porque en general las matrices no conmutan; pero la matriz y su inversa **sí conmutan entre sí**.

> "Si vos tenés algo y algo a la menos uno, ese producto te da la identidad"

### Por qué se llama "inversa"

Por analogía con los números: el inverso de $5$ es $\frac{1}{5}$, y $5 \cdot \frac{1}{5} = 1$. Acá: $A \cdot A^{-1} = \text{Id}$. La identidad hace el papel del $1$.

**ATENCIÓN:** $A^{-1}$ **no es** "$\frac{1}{A}$". La división de matrices **no existe**. Solo se puede multiplicar por la inversa.

> "Acuérdense que X es una matriz, no puedo pasar X dividiendo. Lo análogo es multiplicar por la inversa"

---

## Método directo para hallar la inversa

Es el método clásico. Funciona siempre, pero para matrices grandes (3x3 o más) es lento. Para 2x2 es perfecto.

### Pasos

1. **Plantear** $A \cdot B = \text{Id}$, donde $B$ es una matriz genérica con incógnitas: $B = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ (para 2x2).
2. **Hacer la multiplicación** $A \cdot B$ y dejarla en términos de las incógnitas.
3. **Igualar entrada por entrada** a las entradas de la identidad. Te queda un sistema de ecuaciones (4 ecuaciones, 4 incógnitas en el caso 2x2).
4. **Resolver el sistema.** Si tiene solución única, esa solución es la inversa. Si no tiene solución, la matriz **no es invertible**.

### Ejemplo: hallar la inversa de $A = \begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix}$

**Paso 1.** Buscar $B = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ tal que $A \cdot B = \text{Id}$.

**Paso 2.** Multiplicar:

$$A \cdot B = \begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix} \cdot \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} a + 2c & b + 2d \\ 3a - 4c & 3b - 4d \end{pmatrix}$$

**Paso 3.** Igualar a la identidad:

$$\begin{pmatrix} a + 2c & b + 2d \\ 3a - 4c & 3b - 4d \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

Sistema (igualando entrada por entrada):

$$\begin{cases} a + 2c = 1 \\ b + 2d = 0 \\ 3a - 4c = 0 \\ 3b - 4d = 1 \end{cases}$$

**Paso 4.** Resolver:
- De $a + 2c = 1$ y $3a - 4c = 0$: multiplicando la primera por $2$, $2a + 4c = 2$, sumando con $3a - 4c = 0$ → $5a = 2$ → $a = 2/5$. Luego $c = (1 - 2/5)/2 = 3/10$.
- De $b + 2d = 0$ y $3b - 4d = 1$: $b = -2d$, sustituyendo: $-6d - 4d = 1$ → $d = -1/10$. Luego $b = 1/5$.

**Resultado:**

$$A^{-1} = \begin{pmatrix} 2/5 & 1/5 \\ 3/10 & -1/10 \end{pmatrix}$$

### Cuando NO es invertible

Si al armar el sistema te queda **incompatible** (no tiene solución), la matriz no es invertible.

**Ejemplo:** $C = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$. Si planteás $C \cdot B = \text{Id}$, te queda:

$$\begin{cases} a + 2c = 1 \\ 2a + 4c = 0 \end{cases}$$

La segunda ecuación es $2$ veces la primera, pero los lados derechos no son proporcionales ($1$ y $0$). Sistema incompatible. $C$ no es invertible.

**Pista visual:** la fila 2 de $C$ es $2$ veces la fila 1. Cuando una fila es múltiplo de otra, la matriz no es invertible.

---

## Las 4 propiedades de la inversa (las 4 son demo pedible)

| # | Propiedad | Comentario | Estado parcial |
|---|-----------|-----------|---------------|
| 1 | $(A^{-1})^{-1} = A$ | Invertir dos veces vuelve al original | 🟢 SE PIDE — demo corta |
| 2 | $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$ | **EL ORDEN SE INVIERTE** | 🟢 SE PIDE — demo abajo |
| 3 | $(\alpha \cdot A)^{-1} = \frac{1}{\alpha} \cdot A^{-1}$, $\alpha \neq 0$ | El escalar se invierte también | 🟢 SE PIDE — demo corta |
| 4 | $(A^T)^{-1} = (A^{-1})^T$ | Inversa de la traspuesta = traspuesta de la inversa | 🟢 SE PIDE — aparece como V.16.3 |

> 🟢 **Las 4 son demo pedible.** El profesor dijo: *"vamos a ver ahora las propiedades de la inversa, algunas que tenemos que manejar y vamos a demostrar algunas de ellas"* (clase 3). Demostró la 2 entera. **Cualquiera puede aparecer como "demostrar que..."**. Demos cortas para las otras (estilo: verificar que el "candidato" multiplicado da $\text{Id}$):
> - **Prop 1:** $A^{-1} \cdot A = \text{Id}$ ya prueba que $A$ es la inversa de $A^{-1}$, o sea $(A^{-1})^{-1} = A$.
> - **Prop 3:** $(\alpha A) \cdot (\frac{1}{\alpha} A^{-1}) = (\alpha \cdot \frac{1}{\alpha}) (A \cdot A^{-1}) = 1 \cdot \text{Id} = \text{Id}$.
> - **Prop 4:** ver demo completa en PARTE 10 — sección H.2.

### 🟢 Demostración de la propiedad 2: $(AB)^{-1} = B^{-1} A^{-1}$

> **Estado parcial: 🟢 SE PIDE.** Esta demo el profesor la hizo **completa en pizarrón en clase 3 (24-mar, líneas 54-66)**. Dijo *"vamos a ver ahora las propiedades de la inversa, algunas que tenemos que manejar y vamos a demostrar algunas de ellas"*. **Versión completa con todas las justificaciones en PARTE 10 — sección E.1.**

**Tesis:** $(AB)^{-1} = B^{-1} A^{-1}$.

Para probar que $X$ es la inversa de $Y$, basta verificar que $Y \cdot X = \text{Id}$ (por unicidad de la inversa, alcanza con probar un lado).

Veamos $(AB) \cdot (B^{-1} A^{-1})$:

$$(AB)(B^{-1} A^{-1}) = A \cdot (B \cdot B^{-1}) \cdot A^{-1} \quad \text{(asociativa)}$$
$$= A \cdot \text{Id} \cdot A^{-1} \quad \text{(definición de inversa)}$$
$$= A \cdot A^{-1} \quad \text{(identidad neutra)}$$
$$= \text{Id} \quad \blacksquare$$

### Por qué se invierte el orden

Mismo motivo que la traspuesta: como las matrices no conmutan, no podés escribir $A^{-1} B^{-1}$. Pensá en una analogía con poner ropa: si me pongo medias y zapatos (en ese orden), para sacarmelos hago la inversa: zapatos y medias. **Lo último que pusiste es lo primero que sacás.**

> "No podés mover el A inversa... acuerdate que no conmuta, no podés cambiar el orden"

---

## Despeje de ecuaciones matriciales

Cuando aparece una ecuación con matrices y la incógnita es una matriz $X$, hay que **despejar** $X$. La regla de oro: **NO se puede dividir matrices**. Lo equivalente es **multiplicar por la inversa**, y hay que hacerlo **del mismo lado en ambos miembros**.

### Ejemplo: $A \cdot X = B$, $A$ invertible. Despejar $X$.

$$A \cdot X = B$$
$$A^{-1} \cdot (A \cdot X) = A^{-1} \cdot B \quad \text{(multiplico por }A^{-1}\text{ por la izquierda en ambos lados)}$$
$$(A^{-1} \cdot A) \cdot X = A^{-1} \cdot B \quad \text{(asociativa)}$$
$$\text{Id} \cdot X = A^{-1} \cdot B$$
$$X = A^{-1} \cdot B$$

### Ejemplo: $X \cdot A = B$, $A$ invertible. Despejar $X$.

$$X \cdot A = B$$
$$X \cdot A \cdot A^{-1} = B \cdot A^{-1} \quad \text{(multiplico por }A^{-1}\text{ por la }\textbf{derecha}\text{)}$$
$$X = B \cdot A^{-1}$$

### El error común

> "No podés mover el A inversa..."

Si te aparece $A \cdot X = B$, **NO** podés escribir $X = B \cdot A^{-1}$. Esto sería como decir "$X$ y $A^{-1}$ conmutan", y no es cierto en general. La forma correcta es $X = A^{-1} \cdot B$ (la $A^{-1}$ va del **mismo lado** del que estaba la $A$).

### Y el otro error grave

> "No puedo sumar un número a una matriz, tengo que factorizar con la identidad"

Si te aparece $A \cdot X + X = B$, **NO** podés sacar factor común como $(A + 1) \cdot X = B$, porque "$1$" es un número y $A$ es una matriz, no se pueden sumar. Lo correcto:

$$A \cdot X + X = A \cdot X + \text{Id} \cdot X = (A + \text{Id}) \cdot X = B$$

Y ahora si $(A + \text{Id})$ es invertible: $X = (A + \text{Id})^{-1} \cdot B$.

---

# PARTE 6 — Tipos especiales de matrices

## Matriz idempotente

### Definición 🟡

> **Estado parcial: 🟡 saber/aplicar.** La definición no se demuestra (es definición), pero tenés que reconocer si una matriz es idempotente para usarla en ejercicios.

Una matriz cuadrada $A$ es **idempotente** si $A^2 = A$.

### Ejemplos

- La identidad: $\text{Id}^2 = \text{Id}$. Es idempotente.
- La nula: $\mathcal{O}^2 = \mathcal{O}$. Es idempotente.
- $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ — verificá: $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}^2 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. Es idempotente y **no es ni la identidad ni la nula**.

### 🟢 Resultado clave: idempotente $+$ invertible $\Rightarrow A = \text{Id}$ (ejercicio VI.2)

> **Estado parcial: 🟢 SE PIDE.** Demostrada completa por el profesor en clase 3 (líneas 79-86). **Versión completa en PARTE 10 — sección F.1.**

**Hipótesis:** $A^2 = A$ y $A$ invertible. **Tesis:** $A = \text{Id}$.

$$A^2 = A \implies A^{-1} \cdot A^2 = A^{-1} \cdot A \implies A^{-1} \cdot A \cdot A = \text{Id} \implies \text{Id} \cdot A = \text{Id} \implies A = \text{Id} \quad \blacksquare$$

> **Cuidado:** esto NO dice que toda idempotente sea $\text{Id}$. Solo si además es invertible. Hay idempotentes no invertibles (la nula, $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$).

### 🟢 Identidad útil: si $A$ idempotente, $(A + \text{Id})^3 = \text{Id} + 7A$

> **Estado parcial: 🟢 SE PIDE.** Demostrada completa en clase 4 (líneas 17-29). **Versión completa en PARTE 10 — sección F.2.**

Como $A$ idempotente y $A$ conmuta con $\text{Id}$ (siempre conmutan), aplicamos el binomio de Newton:

$$(A + \text{Id})^3 = A^3 + 3A^2 + 3A + \text{Id} = A + 3A + 3A + \text{Id} = 7A + \text{Id} \quad \blacksquare$$

(Usando $A^k = A$ para todo $k \geq 1$ porque $A^2 = A \Rightarrow A^3 = A \cdot A^2 = A \cdot A = A$.)

---

## Matriz nilpotente

### Definición 🟡

> **Estado parcial: 🟡 saber/aplicar.** Definición — no se demuestra.

Una matriz cuadrada $A$ es **nilpotente de grado $k$** si:
1. $A^k = \mathcal{O}$ (alguna potencia da la nula)
2. $A^{k-1} \neq \mathcal{O}$ (la potencia inmediatamente anterior NO da la nula)

Es decir, $k$ es la **primera** potencia que la anula. Si la primera potencia que la anula es $A^3$, decimos que es nilpotente de grado $3$.

### 🟢 Resultado clave: $P^{-1} A P$ es nilpotente del mismo grado que $A$ (ejercicio V.7.2)

> **Estado parcial: 🟢 SE PIDE.** Demostrada completa por el profesor en clase 4 (líneas 71-84). **Versión completa con paso 1 + paso 2 (absurdo) en PARTE 10 — sección F.3.**

**Hipótesis:** $A$ nilpotente de grado $k$ ($A^k = \mathcal{O}$, $A^{k-1} \neq \mathcal{O}$); $P$ invertible.
**Tesis:** $B = P^{-1} A P$ es nilpotente de grado $k$.

**Idea clave:** $B^k = (P^{-1} A P)^k = P^{-1} A^k P = P^{-1} \cdot \mathcal{O} \cdot P = \mathcal{O}$ (los $P P^{-1}$ del medio se cancelan asociando). Y por absurdo, $B^{k-1} = \mathcal{O}$ implicaría $A^{k-1} = \mathcal{O}$, contradicción.

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

## 🔵 Ejercicio V.1 — Operaciones básicas (cálculo directo)

**Enunciado.** Dadas las matrices:

$$A = \begin{pmatrix} 2 & -1 & 4 \\ 1 & 0 & 6 \\ 1 & -1 & 2 \end{pmatrix}, \quad B = \begin{pmatrix} 0 & 0 & 1 \\ 3 & 0 & 5 \\ 3 & -2 & 0 \end{pmatrix}, \quad C = \begin{pmatrix} 1 & 1 & 2 \\ -2 & 4 & 0 \\ 0 & 5 & -1 \end{pmatrix}$$

1. Calcular: (i) $A - 2B$, (ii) $3A - C$, (iii) $A + B + C$.
2. Encontrar una matriz $D$, $3 \times 3$, tal que $A + B + C + D = \mathcal{O}_{3 \times 3}$.

### Solución

**(i)** $A - 2B$. Primero hacemos $-2 \cdot B$ (producto escalar por matriz):

$$-2 B = \begin{pmatrix} 0 & 0 & -2 \\ -6 & 0 & -10 \\ -6 & 4 & 0 \end{pmatrix}$$

Ahora sumamos $A + (-2B)$:

$$A - 2B = \begin{pmatrix} 2 & -1 & 4 \\ 1 & 0 & 6 \\ 1 & -1 & 2 \end{pmatrix} + \begin{pmatrix} 0 & 0 & -2 \\ -6 & 0 & -10 \\ -6 & 4 & 0 \end{pmatrix} = \begin{pmatrix} 2 & -1 & 2 \\ -5 & 0 & -4 \\ -5 & 3 & 2 \end{pmatrix}$$

**(ii)** $3A - C$:

$$3A = \begin{pmatrix} 6 & -3 & 12 \\ 3 & 0 & 18 \\ 3 & -3 & 6 \end{pmatrix}, \quad -C = \begin{pmatrix} -1 & -1 & -2 \\ 2 & -4 & 0 \\ 0 & -5 & 1 \end{pmatrix}$$

$$3A - C = \begin{pmatrix} 5 & -4 & 10 \\ 5 & -4 & 18 \\ 3 & -8 & 7 \end{pmatrix}$$

**(iii)** $A + B + C$:

$$A + B + C = \begin{pmatrix} 3 & 0 & 7 \\ 2 & 4 & 11 \\ 4 & 2 & 1 \end{pmatrix}$$

**Parte 2.** $A + B + C + D = \mathcal{O}_{3 \times 3}$. Como ya sabemos que $A + B + C = \begin{pmatrix} 3 & 0 & 7 \\ 2 & 4 & 11 \\ 4 & 2 & 1 \end{pmatrix}$, para que la suma con $D$ dé la nula, $D$ debe ser **el opuesto** de $A + B + C$:

$$D = \begin{pmatrix} -3 & 0 & -7 \\ -2 & -4 & -11 \\ -4 & -2 & -1 \end{pmatrix}$$

---

## 🔵 Ejercicio V.2 — Productos posibles (verificar conformabilidad)

**Enunciado.** Dadas las matrices:

$$A = \begin{pmatrix} 2 & -1 & 4 \\ 1 & 0 & 6 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 0 & 1 \\ 2 & -1 & 2 \\ 3 & -2 & 0 \end{pmatrix}, \quad C = \begin{pmatrix} 1 & 6 \\ -2 & 4 \\ 0 & 5 \end{pmatrix}$$

Realizar todos los productos posibles entre dos de ellas.

### Solución

Dimensiones: $A$ es $2 \times 3$, $B$ es $3 \times 3$, $C$ es $3 \times 2$.

**Productos posibles:** $A \cdot B$, $A \cdot C$, $C \cdot A$, $B \cdot C$.

**No se puede hacer** $B \cdot A$ (las columnas de $B$ son $3$, las filas de $A$ son $2$, no coinciden). **Tampoco** $C \cdot B$ (columnas de $C$ son $2$, filas de $B$ son $3$).

**$A \cdot B$** ($2 \times 3$ por $3 \times 3$ → $2 \times 3$):

$$A \cdot B = \begin{pmatrix} 12 & -7 & 0 \\ 19 & -12 & 1 \end{pmatrix}$$

**$A \cdot C$** ($2 \times 3$ por $3 \times 2$ → $2 \times 2$):

$$A \cdot C = \begin{pmatrix} 4 & 28 \\ 1 & 36 \end{pmatrix}$$

**$C \cdot A$** ($3 \times 2$ por $2 \times 3$ → $3 \times 3$):

$$C \cdot A = \begin{pmatrix} 8 & -1 & 40 \\ 0 & 2 & 16 \\ 5 & 0 & 30 \end{pmatrix}$$

**$B \cdot C$** ($3 \times 3$ por $3 \times 2$ → $3 \times 2$):

$$B \cdot C = \begin{pmatrix} 1 & 11 \\ 4 & 18 \\ 7 & 10 \end{pmatrix}$$

---

## 🟢 Ejercicio V.3 — Producto por vectores canónicos (SE PIDE)

**Enunciado.** Dadas:

$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}, \quad \vec{v}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{v}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

1. Calcular $A \cdot \vec{v}_1$, $A \cdot \vec{v}_2$, $A \cdot \vec{v}_3$.
2. Describir con palabras los resultados.

### Solución

**Parte 1.** Aplicando la fórmula del producto:

$$A \cdot \vec{v}_1 = \begin{pmatrix} a_{11} \\ a_{21} \\ a_{31} \end{pmatrix}, \quad A \cdot \vec{v}_2 = \begin{pmatrix} a_{12} \\ a_{22} \\ a_{32} \end{pmatrix}, \quad A \cdot \vec{v}_3 = \begin{pmatrix} a_{13} \\ a_{23} \\ a_{33} \end{pmatrix}$$

Cada producto pertenece a $\mathcal{M}_{3 \times 1}(\mathbb{R})$.

**Parte 2.** En palabras: **multiplicar $A$ por el vector canónico $\vec{v}_j$ extrae la columna $j$-ésima de $A$**. Es decir, $A \cdot \vec{v}_j$ devuelve la columna $j$ de $A$ como vector columna.

---

## 🟢 Ejercicio V.4 — Potencias por inducción (SE PIDE — el profe dijo "podrían hacerlo")

**Enunciado.** Dada la matriz $A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$. Calcular $A^2$, $A^3$ y probar que:

$$A^n = \begin{pmatrix} 1 & n & \frac{n^2 + n}{2} \\ 0 & 1 & n \\ 0 & 0 & 1 \end{pmatrix} \quad \forall n \in \mathbb{N}, n \geq 1$$

### Solución

**Cálculo de $A^2$ y $A^3$:**

$$A^2 = A \cdot A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}$$

(Para $n=2$: $\frac{2^2+2}{2} = 3$ ✓)

$$A^3 = A^2 \cdot A = \begin{pmatrix} 1 & 3 & 6 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{pmatrix}$$

(Para $n=3$: $\frac{3^2+3}{2} = 6$ ✓)

**Inducción completa sobre $n$:**

**Base inductiva ($n = 1$):** $A^1 = A$, y la fórmula da $\begin{pmatrix} 1 & 1 & \frac{1^2+1}{2} \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix} = A$ ✓

**Hipótesis ($n = h$):** $A^h = \begin{pmatrix} 1 & h & \frac{h^2 + h}{2} \\ 0 & 1 & h \\ 0 & 0 & 1 \end{pmatrix}$.

**Tesis ($n = h+1$):** $A^{h+1} = \begin{pmatrix} 1 & h+1 & \frac{(h+1)^2 + (h+1)}{2} \\ 0 & 1 & h+1 \\ 0 & 0 & 1 \end{pmatrix}$.

**Demostración:** $A^{h+1} = A^h \cdot A$. Multiplicando:

$$A^h \cdot A = \begin{pmatrix} 1 & h & \frac{h^2+h}{2} \\ 0 & 1 & h \\ 0 & 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$$

Calculo entrada por entrada:
- $(1,1) = 1$, $(1,2) = 1 + h = h+1$, $(1,3) = 1 + h + \frac{h^2+h}{2} = \frac{2 + 2h + h^2 + h}{2} = \frac{h^2 + 3h + 2}{2}$
- $(2,2) = 1$, $(2,3) = 1 + h = h+1$
- $(3,3) = 1$

Verificamos $(1,3)$: $\frac{(h+1)^2 + (h+1)}{2} = \frac{h^2 + 2h + 1 + h + 1}{2} = \frac{h^2 + 3h + 2}{2}$ ✓

$$A^{h+1} = \begin{pmatrix} 1 & h+1 & \frac{(h+1)^2 + (h+1)}{2} \\ 0 & 1 & h+1 \\ 0 & 0 & 1 \end{pmatrix} \quad \blacksquare$$

---

## 🟢 Ejercicio V.5 — Suma y producto de simétricas (SE PIDE — demostrado entero en clase 2)

**Enunciado.** Sean $A$ y $B$ matrices $n \times n$ simétricas y $\lambda \in \mathbb{R}$.

1. Probar que $A + B$ y $\lambda A$ son simétricas.
2. Probar que $AB$ es simétrica si y solo si $A$ y $B$ conmutan.

### Solución

**Parte 1.** Hipótesis: $A^T = A$ y $B^T = B$. Aplicando propiedades de la traspuesta:

$$(A + B)^T = A^T + B^T = A + B \quad \blacksquare$$
$$(\lambda A)^T = \lambda \cdot A^T = \lambda \cdot A \quad \blacksquare$$

**Parte 2.** Hay que probar **dos implicaciones** porque es "si y solo si".

**Directo: si $AB$ es simétrica $\implies AB = BA$.**

Por hipótesis: $AB = (AB)^T$ (porque $AB$ es simétrica).

Aplicando la propiedad 4 de la traspuesta: $(AB)^T = B^T A^T$.

Como $A$ y $B$ son simétricas: $B^T A^T = BA$.

Entonces $AB = BA$. $\blacksquare$

**Recíproco: si $AB = BA \implies AB$ es simétrica.**

Queremos probar que $(AB)^T = AB$:

$$(AB)^T = B^T A^T \quad \text{(propiedad 4)}$$
$$= BA \quad \text{(simétricas)}$$
$$= AB \quad \text{(hipótesis)} \quad \blacksquare$$

---

## 🟢 Ejercicio V.6 — Descomposición simétrica + antisimétrica (SE PIDE — parte 1 demostrada en clase)

**Enunciado.** Sea $A$ una matriz $n \times n$ cualquiera.

1. Probar que $\frac{1}{2}(A + A^T)$ es simétrica.
2. Probar que $\frac{1}{2}(A - A^T)$ es antisimétrica.
3. Concluir que cualquier matriz se puede escribir como suma de una simétrica más una antisimétrica.

### Solución

**Parte 1.** Calculamos la traspuesta de $A + A^T$:

$$(A + A^T)^T = A^T + (A^T)^T = A^T + A = A + A^T$$

Entonces $A + A^T$ es simétrica, y multiplicar por $\frac{1}{2}$ no la afecta (propiedad 3 de simétricas). Por lo tanto $\frac{1}{2}(A + A^T)$ es simétrica. $\blacksquare$

**Parte 2.** Calculamos la traspuesta de $A - A^T$:

$$(A - A^T)^T = A^T - (A^T)^T = A^T - A = -(A - A^T)$$

Entonces $A - A^T$ es antisimétrica, y multiplicar por $\frac{1}{2}$ no la afecta. Por lo tanto $\frac{1}{2}(A - A^T)$ es antisimétrica. $\blacksquare$

**Parte 3.** Sumando las dos partes:

$$\frac{1}{2}(A + A^T) + \frac{1}{2}(A - A^T) = \frac{1}{2}A + \frac{1}{2}A^T + \frac{1}{2}A - \frac{1}{2}A^T = A \quad \blacksquare$$

**Conclusión:** cualquier matriz cuadrada se puede partir en una parte simétrica y una antisimétrica. La simétrica es $\frac{1}{2}(A + A^T)$ y la antisimétrica es $\frac{1}{2}(A - A^T)$.

---

## 🟢 Ejercicio V.7 — Matriz nilpotente (SE PIDE — parte 2 demostrada por el profesor en clase 4)

**Enunciado.** Una matriz $n \times n$ $A$ es **nilpotente de grado $k$** si y solo si $A^k = \mathcal{O}_{n \times n}$ y $A^{k-1} \neq \mathcal{O}_{n \times n}$.

Dada $A = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$.

1. Probar que $A$ es nilpotente. ¿De qué grado?
2. Si $P$ es una matriz $3 \times 3$ invertible cualquiera, ¿$P^{-1} A P$ es nilpotente? ¿De qué grado?

### Solución

**Parte 1.** Calculamos las potencias de $A$:

$$A^2 = A \cdot A = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \neq \mathcal{O}$$

$$A^3 = A^2 \cdot A = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \mathcal{O}$$

Como $A^3 = \mathcal{O}$ y $A^2 \neq \mathcal{O}$, **$A$ es nilpotente de grado $k = 3$**. $\blacksquare$

**Parte 2.** $P$ invertible significa $P P^{-1} = P^{-1} P = \text{Id}$. Calculamos las potencias de $P^{-1} A P$:

$$(P^{-1} A P)(P^{-1} A P) = P^{-1} A (P P^{-1}) A P = P^{-1} A \cdot \text{Id} \cdot A P = P^{-1} A^2 P$$

Y otra vez:

$$(P^{-1} A^2 P)(P^{-1} A P) = P^{-1} A^2 (P P^{-1}) A P = P^{-1} A^2 \cdot \text{Id} \cdot A P = P^{-1} A^3 P = P^{-1} \mathcal{O} P = \mathcal{O}$$

Es decir, $(P^{-1} A P)^3 = \mathcal{O}$ y $(P^{-1} A P)^2 = P^{-1} A^2 P \neq \mathcal{O}$ (porque $A^2 \neq \mathcal{O}$ y $P, P^{-1}$ son invertibles).

**Conclusión:** $P^{-1} A P$ es nilpotente de grado $3$, igual que $A$. $\blacksquare$

---

## 🟢 Ejercicio V.8 — Ecuación matricial polinomial (SE PIDE — factorización clave)

**Enunciado.** Dada $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{pmatrix}$.

1. Verificar que $A$ satisface la ecuación matricial $-A^3 + 5A^2 - 7A + 3 \cdot \text{Id}_{3 \times 3} = \mathcal{O}_{3 \times 3}$.
2. Demostrar que $A$ es invertible y hallar su inversa.

### Solución

**Parte 1.** Calculamos las potencias necesarias:

$$A^2 = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 9 \end{pmatrix}, \quad A^3 = \begin{pmatrix} 1 & 3 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 27 \end{pmatrix}$$

Multiplicamos escalarmente: $A^3 \cdot (-1)$, $A^2 \cdot 5$, $A \cdot (-7)$, $\text{Id} \cdot 3$, y sumamos las cuatro matrices. Entrada por entrada se obtiene la matriz nula $\mathcal{O}_{3 \times 3}$. ✓

**Parte 2.** $A$ es triangular superior con todas las entradas de la diagonal distintas de $0$, así que su determinante es no nulo (cosa que se verá más adelante en el curso). Por lo tanto $A$ es invertible: existe $A^{-1}$ tal que $A \cdot A^{-1} = A^{-1} \cdot A = \text{Id}$.

**Asumiendo eso, despejamos la inversa de la ecuación de la parte 1:**

Multiplicamos toda la ecuación por $A^{-1}$ por la derecha:

$$-A^3 \cdot A^{-1} + 5 A^2 \cdot A^{-1} - 7 A \cdot A^{-1} + 3 \text{Id} \cdot A^{-1} = \mathcal{O} \cdot A^{-1}$$

$$-A^2 + 5A - 7\text{Id} + 3 A^{-1} = \mathcal{O}$$

Despejamos $A^{-1}$:

$$3 A^{-1} = A^2 - 5A + 7\text{Id}$$

$$A^{-1} = \frac{1}{3}\left(A^2 - 5A + 7\text{Id}\right)$$

Calculamos:

$$A^2 - 5A + 7\text{Id} = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 9 \end{pmatrix} - \begin{pmatrix} 5 & 5 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 15 \end{pmatrix} + \begin{pmatrix} 7 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 7 \end{pmatrix} = \begin{pmatrix} 3 & -3 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

$$A^{-1} = \frac{1}{3}\begin{pmatrix} 3 & -3 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1/3 \end{pmatrix}$$

---

## 🔵 Ejercicio V.9 — Inversas por método directo (cálculo — el profe dijo "en parciales se dice 'hallen la inversa'")

**Enunciado.** Encontrar la inversa (si existe) de:

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 2 & 1 \\ 4 & 2 \end{pmatrix}, \quad C = \begin{pmatrix} 1 & 1 & -1 \\ 1 & -1 & 1 \\ 1 & 1 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 5 & 0 \\ 2 & 4 & 3 \end{pmatrix}, \quad E = \begin{pmatrix} 1 & 0 & 1 & -1 \\ 2 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & -1 & 2 & 1 \end{pmatrix}$$

### Soluciones (oficiales)

$$A^{-1} = \begin{pmatrix} -1/5 & 2/5 \\ 3/5 & -1/5 \end{pmatrix}$$

$$B^{-1} \text{ no existe}$$
(la fila 2 es $2$ veces la fila 1 → sistema incompatible al plantear $B \cdot X = \text{Id}$)

$$C^{-1} = \begin{pmatrix} 1/2 & 1/2 & 0 \\ 0 & -1/2 & 1/2 \\ -1/2 & 0 & 1/2 \end{pmatrix}$$

$$D^{-1} = \begin{pmatrix} -1 & -2/5 & 1 \\ 0 & 1/5 & 0 \\ 2/3 & 0 & -1/3 \end{pmatrix}$$

$$E^{-1} = \begin{pmatrix} 0 & 1/2 & -1/2 & 0 \\ -1/4 & 1/8 & 5/8 & -1/4 \\ 1/4 & -1/8 & 3/8 & 1/4 \\ -3/4 & 3/8 & -1/8 & 1/4 \end{pmatrix}$$

**Nota de la cátedra:** "En los casos $3 \times 3$ y $4 \times 4$ se recomienda calcular la inversa por escalerización (Gauss-Jordan que se verá más adelante)". Para el parcial actual, el método directo (planteando el sistema) sigue siendo el válido.

**Ejemplo del paso a paso para $A$:** Buscamos $X = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ tal que $A \cdot X = \text{Id}$:

$$\begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} a + 2c & b + 2d \\ 3a + c & 3b + d \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

Sistema: $a + 2c = 1$, $b + 2d = 0$, $3a + c = 0$, $3b + d = 1$. Resolviendo: $a = -1/5$, $b = 2/5$, $c = 3/5$, $d = -1/5$.

---

## 🟢 Ejercicio V.10 — $A^2 = 2A - \text{Id}$ (SE PIDE — ejercicio CLAVE para parcial)

**Enunciado.** Sea $A = \begin{pmatrix} 5 & -4 & 2 \\ 2 & -1 & 1 \\ -4 & 4 & -1 \end{pmatrix}$.

1. Probar que $A^2 = 2A - \text{Id}$. Deducir que $A$ es invertible.
2. Probar que $A^3 = 3A - 2 \text{Id}$ y hallar $A^3$.
3. Probar por inducción completa que $A^n = n \cdot A - (n-1) \cdot \text{Id}$, $\forall n \in \mathbb{N}, n \geq 2$.

### Solución

**Parte 1.** Calculamos $A^2$ directamente:

$$A^2 = A \cdot A = \begin{pmatrix} 5 & -4 & 2 \\ 2 & -1 & 1 \\ -4 & 4 & -1 \end{pmatrix} \cdot \begin{pmatrix} 5 & -4 & 2 \\ 2 & -1 & 1 \\ -4 & 4 & -1 \end{pmatrix} = \begin{pmatrix} 9 & -8 & 4 \\ 4 & -3 & 2 \\ -8 & 8 & -3 \end{pmatrix}$$

Calculamos $2A - \text{Id}$:

$$2A - \text{Id} = \begin{pmatrix} 10 & -8 & 4 \\ 4 & -2 & 2 \\ -8 & 8 & -2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 9 & -8 & 4 \\ 4 & -3 & 2 \\ -8 & 8 & -3 \end{pmatrix}$$

Coinciden. Se verifica la igualdad. ✓

**Deducir invertibilidad:** de $A^2 = 2A - \text{Id}$, despejamos:

$$A^2 - 2A = -\text{Id}$$
$$A \cdot (A - 2\text{Id}) = -\text{Id}$$
$$A \cdot (2\text{Id} - A) = \text{Id}$$

Como $A$ multiplicada por $(2\text{Id} - A)$ da la identidad, por **definición de inversa** $A$ es invertible y:

$$A^{-1} = 2\text{Id} - A = \begin{pmatrix} -3 & 4 & -2 \\ -2 & 3 & -1 \\ 4 & -4 & 3 \end{pmatrix}$$

> "Si probaste que esta es la inversa, estás probando las dos cosas a la misma vez"

**Parte 2.** Calculamos $A^3$ usando la igualdad de la parte 1:

$$A^3 = A^2 \cdot A \stackrel{(\text{por 1})}{=} (2A - \text{Id}) \cdot A \stackrel{\text{(distrib.)}}{=} 2A^2 - A \stackrel{(\text{por 1})}{=} 2(2A - \text{Id}) - A = 3A - 2\text{Id}$$

Y calculamos $A^3$ numéricamente:

$$A^3 = 3A - 2\text{Id} = \begin{pmatrix} 15 & -12 & 6 \\ 6 & -3 & 3 \\ -12 & 12 & -3 \end{pmatrix} - \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix} = \begin{pmatrix} 13 & -12 & 6 \\ 6 & -5 & 3 \\ -12 & 12 & -5 \end{pmatrix}$$

**Parte 3 — Inducción completa.** Tesis: $A^n = n \cdot A - (n-1) \cdot \text{Id}$, $\forall n \in \mathbb{N}, n \geq 2$.

**Base inductiva ($n = 2$):** $A^2 = 2A - \text{Id}$. Demostrado en parte 1. ✓

**Hipótesis inductiva ($n = h$):** $A^h = h \cdot A - (h-1) \cdot \text{Id}$, para algún $h \geq 2$.

**Tesis inductiva ($n = h+1$):** $A^{h+1} = (h+1) \cdot A - h \cdot \text{Id}$.

**Demostración:**

$$A^{h+1} = A^h \cdot A \stackrel{(\text{H.I.})}{=} \left[h \cdot A - (h-1) \cdot \text{Id}\right] \cdot A$$

$$\stackrel{(\text{distrib.})}{=} h \cdot A^2 - (h-1) \cdot A$$

$$\stackrel{(\text{base})}{=} h \cdot (2A - \text{Id}) - (h-1) \cdot A$$

$$= 2h \cdot A - h \cdot \text{Id} - h \cdot A + A$$

$$= (h + 1) \cdot A - h \cdot \text{Id} \quad \blacksquare$$

---

## 🟢 Ejercicio V.11 — Ley de simplificación (SE PIDE — comentado por el profe en clase 4)

**Enunciado.**

1. Probar que si $A$ y $B$ satisfacen $AB = A$ y $A$ es invertible, entonces $B = \text{Id}_{n \times n}$.
2. Probar que si $A$, $B$ y $C$ satisfacen $AB = AC$ y $A$ es invertible, entonces $B = C$.
3. Dadas $A = \begin{pmatrix} 0 & 3 \\ 0 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 2 & 1 \\ 3 & 0 \end{pmatrix}$, $C = \begin{pmatrix} 5 & 4 \\ 3 & 0 \end{pmatrix}$. Mostrar que $AB = AC$ pero $B \neq C$. ¿Qué conclusión se puede sacar?

### Solución

**Parte 1.** Hipótesis: $AB = A$ y existe $A^{-1}$. Multiplicamos ambos lados por $A^{-1}$ por la izquierda:

$$A^{-1} \cdot (AB) = A^{-1} \cdot A = \text{Id}$$

Por asociativa: $(A^{-1} \cdot A) \cdot B = \text{Id} \cdot B = B$. Entonces $B = \text{Id}$. $\blacksquare$

**Parte 2.** Hipótesis: $AB = AC$ y existe $A^{-1}$. Multiplicamos por $A^{-1}$ por la izquierda:

$$A^{-1} \cdot (AB) = A^{-1} \cdot (AC)$$

Por asociativa: $(A^{-1} \cdot A) \cdot B = (A^{-1} \cdot A) \cdot C$, es decir $\text{Id} \cdot B = \text{Id} \cdot C$, así que $B = C$. $\blacksquare$

**Parte 3.** Calculamos:

$$AB = \begin{pmatrix} 0 & 3 \\ 0 & 0 \end{pmatrix} \cdot \begin{pmatrix} 2 & 1 \\ 3 & 0 \end{pmatrix} = \begin{pmatrix} 9 & 0 \\ 0 & 0 \end{pmatrix}$$

$$AC = \begin{pmatrix} 0 & 3 \\ 0 & 0 \end{pmatrix} \cdot \begin{pmatrix} 5 & 4 \\ 3 & 0 \end{pmatrix} = \begin{pmatrix} 9 & 0 \\ 0 & 0 \end{pmatrix}$$

Entonces $AB = AC$ pero $B \neq C$.

**Conclusión:** $A$ **no es invertible**. Si lo fuera, por la parte 2 se cumpliría $B = C$, lo cual es falso en este ejemplo. La ley de simplificación **no vale** sin la hipótesis de invertibilidad.

---

## 🟢 Ejercicio V.12 — Matriz ortogonal (SE PIDE como ejercicio — propiedades formales de ortogonal NO entran)

**Enunciado.** Una matriz $n \times n$ $A$ es **ortogonal** si y solo si $A$ es invertible y $A^{-1} = A^T$.

Dada $A = \begin{pmatrix} 4/5 & 3/5 \\ \alpha & \beta \end{pmatrix}$, con $\alpha, \beta \in \mathbb{R}$, determinar los valores de $\alpha$ y $\beta$ para que $A$ sea ortogonal y hallar su inversa.

### Solución

$A^{-1} = A^T \implies A^T \cdot A = \text{Id}$. Imponemos esa condición:

$$A^T \cdot A = \begin{pmatrix} 4/5 & \alpha \\ 3/5 & \beta \end{pmatrix} \cdot \begin{pmatrix} 4/5 & 3/5 \\ \alpha & \beta \end{pmatrix} = \begin{pmatrix} 16/25 + \alpha^2 & 12/25 + \alpha\beta \\ 12/25 + \alpha\beta & 9/25 + \beta^2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

Igualando entrada por entrada:

- $16/25 + \alpha^2 = 1 \implies \alpha^2 = 9/25 \implies \alpha = \pm 3/5$
- $9/25 + \beta^2 = 1 \implies \beta^2 = 16/25 \implies \beta = \pm 4/5$
- $12/25 + \alpha \beta = 0 \implies \alpha \beta = -12/25$

Las dos parejas que cumplen las tres condiciones:

**Caso 1:** $\alpha = 3/5, \beta = -4/5 \implies A^{-1} = A^T = \begin{pmatrix} 4/5 & 3/5 \\ 3/5 & -4/5 \end{pmatrix}$

**Caso 2:** $\alpha = -3/5, \beta = 4/5 \implies A^{-1} = A^T = \begin{pmatrix} 4/5 & -3/5 \\ 3/5 & 4/5 \end{pmatrix}$

---

## 🔵 Ejercicio V.13 — Hallar parámetros para $P^{-1} A P$ (SE PIDE)

**Enunciado.** Dadas $A = \begin{pmatrix} 1 & 2 \\ 5 & 4 \end{pmatrix}$ y $P = \begin{pmatrix} 2 & 1 \\ x & y \end{pmatrix}$, con $x, y \in \mathbb{R}$, hallar $x$ e $y$ para que:

$$P^{-1} \cdot A \cdot P = \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix}$$

### Solución

**Truco:** multiplicar ambos lados por $P$ por la izquierda para eliminar $P^{-1}$ (sin tener que calcularlo):

$$P \cdot (P^{-1} \cdot A \cdot P) = P \cdot \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix}$$

Por asociativa: $(P \cdot P^{-1}) \cdot A \cdot P = \text{Id} \cdot A \cdot P = A \cdot P$. Entonces:

$$A \cdot P = P \cdot \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix}$$

Calculamos ambos lados:

$$A \cdot P = \begin{pmatrix} 1 & 2 \\ 5 & 4 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ x & y \end{pmatrix} = \begin{pmatrix} 2 + 2x & 1 + 2y \\ 10 + 4x & 5 + 4y \end{pmatrix}$$

$$P \cdot \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ x & y \end{pmatrix} \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 12 & -1 \\ 6x & -y \end{pmatrix}$$

Igualando entrada por entrada:

- $2 + 2x = 12 \implies x = 5$
- $1 + 2y = -1 \implies y = -1$
- (verificación) $10 + 4(5) = 30 = 6(5)$ ✓
- (verificación) $5 + 4(-1) = 1 = -(-1)$ ✓

**Resultado:** $x = 5$, $y = -1$.

---

## 🟢 Ejercicio V.14 — ¿$A + B$ y $AB$ son invertibles si $A, B$ lo son? (SE PIDE — comentado por el profe)

**Enunciado.** Sean matrices reales $n \times n$.

1. Si $A$ y $B$ son invertibles, ¿necesariamente $A + B$ es invertible?
2. Si $A$ y $B$ son invertibles, ¿necesariamente $AB$ es invertible?

### Solución

**Parte 1.** **NO** es cierto. Contraejemplo concreto para $n = 3$:

$$A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{pmatrix}$$

Ambas son invertibles ($A^{-1} = A$ y $B^{-1} = B$). Sin embargo:

$$A + B = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \mathcal{O}_{3 \times 3}$$

La nula no es invertible. Entonces $A + B$ **no es invertible** aunque $A$ y $B$ lo sean. $\blacksquare$

**Parte 2.** **SÍ**, siempre. Demostración:

Por hipótesis existen $A^{-1}$ y $B^{-1}$. Vamos a demostrar que $(AB)^{-1} = B^{-1} A^{-1}$ verificando $AB \cdot (B^{-1} A^{-1}) = \text{Id}$:

$$AB \cdot (B^{-1} A^{-1}) \stackrel{(\text{asoc.})}{=} A \cdot (B \cdot B^{-1}) \cdot A^{-1} = A \cdot \text{Id} \cdot A^{-1} = A \cdot A^{-1} = \text{Id}$$

Análogamente $(B^{-1} A^{-1}) \cdot AB = \text{Id}$. Por lo tanto $AB$ es invertible y su inversa es $B^{-1} A^{-1}$. $\blacksquare$

---

## 🟢 Ejercicio V.15 — Conmutatividad (SE PIDE — demo de conmutatividad bajo hipótesis)

**Enunciado.** Dos matrices $A$ y $B$ conmutan si y solo si $AB = BA$.

1. Sean $A$, $B$, $C$ matrices reales $n \times n$ tales que $A$ conmuta con $B$ y $A$ conmuta con $C$. Probar que $A$ conmuta con $D = \mu B + \lambda C$, donde $\mu, \lambda \in \mathbb{R}$.
2. Sea $A = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix}$. Hallar todas las matrices que conmutan con $A$. Verificar que $A$ y $\text{Id}$ son dos de las matrices halladas. Concluir, sin multiplicar, que $D_1 = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix}$ y $D_2 = \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix}$ conmutan con $A$.

### Solución

**Parte 1.**

$$A \cdot D = A \cdot (\mu B + \lambda C) \stackrel{(\text{distrib.})}{=} \mu (AB) + \lambda (AC) \stackrel{(\text{hip.})}{=} \mu (BA) + \lambda (CA) \stackrel{(\text{distrib.})}{=} (\mu B + \lambda C) \cdot A = D \cdot A \quad \blacksquare$$

**Parte 2.** Sea $B = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ una matriz que conmuta con $A$. Imponemos $AB = BA$:

$$AB = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} a - c & b - d \\ a & b \end{pmatrix}$$

$$BA = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} a + b & -a \\ c + d & -c \end{pmatrix}$$

Igualando entrada por entrada:
- $a - c = a + b \implies c = -b$
- $b - d = -a \implies d = a + b$
- $a = c + d \implies a = -b + a + b = a$ (siempre cierto)
- $b = -c$ (ya lo tenemos)

**Conclusión:** las matrices que conmutan con $A$ son de la forma:

$$B = \begin{pmatrix} a & b \\ -b & a + b \end{pmatrix}, \quad \forall a, b \in \mathbb{R}$$

**Verificaciones:**
- $A$ conmuta consigo misma: $A = B$ con $a = 1, b = -1$. ✓
- $\text{Id}$ conmuta con $A$: $\text{Id} = B$ con $a = 1, b = 0$. ✓

**Conclusión sin multiplicar:**
- $D_1 = \begin{pmatrix} 2 & -1 \\ 1 & 1 \end{pmatrix} = 1 \cdot A + 1 \cdot \text{Id}$, conmuta con $A$ por la parte 1.
- $D_2 = \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix} = 1 \cdot A - 1 \cdot \text{Id}$, conmuta con $A$ por la parte 1.

---

## 🟢 Ejercicio V.16 — VERDADERO o FALSO (SE PIDE — estilo de parcial confirmado)

**Enunciado.** Demostrar las siguientes afirmaciones si son ciertas, o mostrar un contraejemplo si no lo son. Si es posible, agregar hipótesis adicionales para que se cumplan. Sean $A, B$ matrices reales $n \times n$.

1. $(A + B)^2 = A^2 + 2AB + B^2$
2. Si $A, B$ son simétricas, entonces $AB$ es simétrica.
3. Si $A$ es invertible, entonces $A^T$ también lo es y $(A^T)^{-1} = (A^{-1})^T$.

### Solución

**Parte 1. FALSO.** Desarrollando:

$$(A + B)^2 = (A + B)(A + B) = A^2 + AB + BA + B^2$$

Solo es igual a $A^2 + 2AB + B^2$ si $AB = BA$ (es decir, si conmutan).

**Contraejemplo (oficial):** $A = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.

$(A + B)^2 = \begin{pmatrix} 2 & 1 \\ 2 & 0 \end{pmatrix}^2 = \begin{pmatrix} 6 & 2 \\ 4 & 2 \end{pmatrix}$

$A^2 + 2AB + B^2 = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} + \begin{pmatrix} 4 & 2 \\ 2 & 2 \end{pmatrix} + \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 7 & 3 \\ 4 & 3 \end{pmatrix}$

No coinciden.

**Hipótesis adicional para que sea cierta:** $AB = BA$. Demostración: $(A+B)^2 = (A+B)(A+B) = A^2 + AB + BA + B^2 = A^2 + 2AB + B^2$ (usando $AB = BA$).

**Parte 2. FALSO.** Tenemos $(AB)^T = B^T A^T = BA$ (porque son simétricas). Para que $AB$ sea simétrica necesitamos $AB = BA$, es decir, que conmuten.

**Contraejemplo (oficial):** $A = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.

$A^T = A$ y $B^T = B$ (ambas simétricas). Pero:

$AB = \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}$, que no es simétrica (la entrada $a_{12} = 0$ y $a_{21} = 1$).

**Hipótesis adicional para que sea cierta:** $AB = BA$. Demostración: $(AB)^T = B^T A^T = B A = AB$ (usando $AB = BA$).

**Parte 3. VERDADERO.** Hay que demostrar que $(A^T)(A^{-1})^T = (A^{-1})^T (A^T) = \text{Id}$, lo que prueba que $A^T$ es invertible y que su inversa es $(A^{-1})^T$.

Demostramos $(A^T)(A^{-1})^T = \text{Id}$ (la otra es análoga):

$$A^T \cdot (A^{-1})^T \stackrel{(*)}{=} (A^{-1} \cdot A)^T = \text{Id}^T = \text{Id} \quad \blacksquare$$

(*) se usa la propiedad $(BC)^T = C^T B^T$ aplicada al revés: $C^T B^T = (BC)^T$ con $C = A^{-1}$ y $B = A$.

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

## 🟢 Ejercicio VI.1 — Inducción sobre $A^n$ (SE PIDE — ejercicio de evaluación continua)

**Enunciado.** Sea $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. Demostrar por inducción completa sobre $n$ que:

$$A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix} \quad \forall n \text{ natural positivo}$$

### Solución

**Base inductiva ($n = 1$):** $A^1 = A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. La fórmula da $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. ✓

**Hipótesis ($n = h$):** $A^h = \begin{pmatrix} 1 & h \\ 0 & 1 \end{pmatrix}$.

**Tesis ($n = h + 1$):** $A^{h+1} = \begin{pmatrix} 1 & h+1 \\ 0 & 1 \end{pmatrix}$.

**Demostración:**

$$A^{h+1} = A^h \cdot A \stackrel{(\text{H.I.})}{=} \begin{pmatrix} 1 & h \\ 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 \cdot 1 + h \cdot 0 & 1 \cdot 1 + h \cdot 1 \\ 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 1 \end{pmatrix} = \begin{pmatrix} 1 & h+1 \\ 0 & 1 \end{pmatrix} \quad \blacksquare$$

---

## 🟢 Ejercicio VI.2 — Idempotente e invertible (SE PIDE — demostrado entero en clase 3)

**Enunciado.** Una matriz $A$, $n \times n$, real, es **idempotente** si y solo si $A^2 = A$.

1. Probar que si $A$ es idempotente e invertible, entonces $A$ es la matriz identidad.
2. Dar un ejemplo de una matriz idempotente que no sea ni la nula ni la identidad.

### Solución

**Parte 1.** Hipótesis: $A^2 = A$ y existe $A^{-1}$. Tesis: $A = \text{Id}$.

$$A^2 = A$$
$$A^{-1} \cdot A^2 = A^{-1} \cdot A \quad \text{(multiplico por }A^{-1}\text{)}$$
$$A^{-1} \cdot A \cdot A = \text{Id}$$
$$\text{Id} \cdot A = \text{Id}$$
$$A = \text{Id} \quad \blacksquare$$

**Parte 2.** Ejemplo:

$$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$$

Verificación: $A^2 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \cdot \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = A$. ✓

Y $A \neq \mathcal{O}$ (tiene un $1$), $A \neq \text{Id}$ (tiene un $0$ en la diagonal).

---

## 🟢 Ejercicio VI.3 — $A^3 = \mathcal{O} \implies (A + \text{Id})^{-1} = A^2 - A + \text{Id}$ (SE PIDE — demostrado en clase 3)

**Enunciado.** Sea $A$ matriz real $n \times n$ tal que $A^3 = \mathcal{O}$ ($\mathcal{O}$ es la matriz nula).

1. Demostrar que $(A + \text{Id})$ es invertible y además $(A + \text{Id})^{-1} = A^2 - A + \text{Id}$.
2. Usar el resultado anterior para hallar la inversa de $B = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$. Verificar que efectivamente es la pedida.

### Solución

**Parte 1.** Para probar que $A^2 - A + \text{Id}$ es la inversa de $A + \text{Id}$, verificamos que su producto es la identidad. Multiplicamos:

$$(A + \text{Id})(A^2 - A + \text{Id})$$

Distribuyendo (cuidado con el orden, las matrices no conmutan, pero $A$ y $\text{Id}$ sí):

$$= A \cdot A^2 - A \cdot A + A \cdot \text{Id} + \text{Id} \cdot A^2 - \text{Id} \cdot A + \text{Id} \cdot \text{Id}$$

$$= A^3 - A^2 + A + A^2 - A + \text{Id}$$

$$= A^3 + (- A^2 + A^2) + (A - A) + \text{Id}$$

$$= A^3 + \text{Id}$$

$$\stackrel{(\text{hip.})}{=} \mathcal{O} + \text{Id} = \text{Id} \quad \blacksquare$$

**Parte 2.** Identificamos $A$ tal que $B = A + \text{Id}$:

$$A = B - \text{Id} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

Verificamos que $A^3 = \mathcal{O}$:

$$A^2 = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \neq \mathcal{O}$$

$$A^3 = A^2 \cdot A = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} = \mathcal{O} \quad \checkmark$$

Aplicamos la fórmula $B^{-1} = A^2 - A + \text{Id}$:

$$B^{-1} = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} - \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} + \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 & 0 & 1 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

**Verificación:** $B \cdot B^{-1} = ?$

$$\begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & -1 & 0 & 1 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

Calculo entrada por entrada (la fila $i$ de $B$ por la columna $j$ de $B^{-1}$):
- $(1,1) = 1 \cdot 1 = 1$, $(1,2) = 1 \cdot (-1) + 1 \cdot 1 = 0$, $(1,3) = 0$, $(1,4) = 1 \cdot 1 + 1 \cdot (-1) = 0$
- $(2,1) = 0$, $(2,2) = 1 \cdot 1 = 1$, $(2,3) = 0$, $(2,4) = 1 \cdot (-1) + 1 \cdot 1 = 0$
- $(3,1) = 0$, $(3,2) = 0$, $(3,3) = 1$, $(3,4) = 0$
- $(4,1) = 0$, $(4,2) = 0$, $(4,3) = 0$, $(4,4) = 1$

$$B \cdot B^{-1} = \text{Id}_{4 \times 4} \quad \checkmark$$

---

# PARTE 8 — Estrategia de parcial: errores comunes y checklist

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

---

## Checklist mental antes de cada cuenta

Antes de hacer una operación, hacete estas preguntas:

| Operación | Pregunta |
|-----------|----------|
| Suma $A + B$ | ¿Tienen la misma dimensión? |
| Producto $A \cdot B$ | ¿Las columnas de $A$ coinciden con las filas de $B$? (Conformabilidad) |
| Inversa $A^{-1}$ | ¿$A$ es cuadrada? ¿Se planteó si es invertible? |
| Despejar $X$ | ¿En qué lado está $X$? ¿Multiplico por la inversa por ese mismo lado? |
| Trasponer producto | ¿Invertí el orden? |
| Invertir producto | ¿Invertí el orden? |
| Conmutar $AB \to BA$ | ¿Tengo hipótesis que lo permita? |
| Sacar factor común con $X$ | ¿Tengo que poner $\text{Id} \cdot X$ explícitamente? |

---

## Auditoría exhaustiva: ¿qué demostraciones de matrices pueden caer en parcial?

Esta sección audita **cada propiedad y cada demostración** del módulo de matrices contra lo que el profesor dijo textualmente en las 12 clases del semestre. La metodología fue: leer las 12 transcripciones completas, encontrar cada vez que el profesor habló de qué entra o no entra en parcial respecto a demostraciones, y mapear sus citas a las propiedades concretas del módulo.

### Conclusión central (leé esto antes que la tabla)

> **El profesor NUNCA dijo "esta demostración NO se pide en parcial" para ninguna propiedad o teorema de matrices.** La instrucción literal y repetida fue **"tenemos que manejar"** las 4 propiedades de traspuesta, las 4 de traza, y las 4 de inversa — eso significa estar preparado para **demostrar cualquiera de ellas**. La única exclusión explícita en todo el módulo fue el **ejercicio V.17, marcado como "podría ser opcional"**.

### Las 6 reglas explícitas del profesor sobre demostraciones en parcial

| # | Regla | Cita textual del profesor (clase:fecha) |
|---|-------|------------------------------------------|
| 1 | El parcial **sí** tiene demostraciones teóricas, no es solo cuentas | *"el parcial, si bien tiene alguna demostración teórica, es resolver ejercicios"* (clase 1, 17-mar) |
| 2 | En cualquier demostración hay que **citar qué propiedad estás aplicando** | *"en los parciales si se pide justificar las propiedades que aplican"* (clase 2, 18-mar) |
| 3 | No hace falta memorizar el **número** de la propiedad — basta **describirla con palabras** | *"eso no importa. Lo que importa es saber aplicarla y aclarar qué propiedad estás aplicando. No hay un texto así... describí con palabras"* (clase 5, 7-abr) |
| 4 | Las **4 propiedades de traspuesta** "tenemos que manejar" | *"vamos a ver cuatro propiedades que tenemos que manejar en esta operación"* (clase 2, 18-mar) |
| 5 | Las **4 propiedades de traza** "tenemos que manejar" | *"al igual que las traspuestas son 4 propiedades que tenemos que manejar"* (clase 2, 18-mar) |
| 6 | Las **4 propiedades de inversa** "tenemos que manejar y demostrar algunas" | *"vamos a ver ahora las propiedades de la inversa, algunas que tenemos que manejar y vamos a demostrar algunas de ellas"* (clase 3, 24-mar) |

### Tabla maestra: cada demostración del módulo y su veredicto

> ⚠️ **OJO con los emojis acá:** En esta tabla de auditoría, los emojis describen **cómo el profesor presentó cada propiedad en clase** (evidencia bruta). NO es lo mismo que la **leyenda de prioridad** que usás en el resto del documento. Para "qué hago con esto al estudiar", mirá el resto del doc — la leyenda al inicio resume el sistema de prioridad simplificado a 4 niveles. Esta tabla es la fuente cruda de evidencia.

**Leyenda de evidencia (solo para esta tabla):**
- 🟢 **DEMOSTRADA EN PIZARRÓN** — el profesor la hizo entera en clase. **Demo pedible en parcial — prioridad MÁXIMA.**
- 🟡 **EN ESQUEMA / ANALOGÍA** — el profesor la sketcheó o dijo "es análoga a esta otra". **Demo pedible — saberla deducir.**
- 🔵 **ENUNCIADA "QUE TENEMOS QUE MANEJAR"** — propiedad listada pero el profesor no la demostró formalmente. **La mayoría son demo pedible** (ver columna "Veredicto").
- ⚪ **DEFINICIÓN / CÁLCULO** — no hay demostración formal asociada; es definicional o computacional. Va como 🟡 (saber/aplicar) o 🔵 (cálculo) en la prioridad de estudio.
- 🔴 **EXCLUIDA EXPLÍCITAMENTE** — el profesor dijo que NO entra en parcial.

**Veredicto:**
- **SE PIDE** = puede caer como demostración (prioridad de estudio: 🟢 en el sistema simplificado).
- **NO SE PIDE** = el profesor lo excluyó explícitamente (prioridad de estudio: 🔴).
- **SE APLICA** = entra como herramienta de cálculo, no como demostración (prioridad de estudio: 🟡 saber, o 🔵 procedimiento).

#### A. Suma de matrices y producto por escalar

| Propiedad | Estado | Veredicto | Evidencia |
|-----------|--------|-----------|-----------|
| Asociativa de la suma: $(A+B)+C = A+(B+C)$ | 🔵 Enunciada | SE PIDE | Clase 1, 17-mar (líneas 170-187) — enunciada sin demo, dentro de las "que tenemos que manejar" |
| Conmutativa de la suma: $A+B = B+A$ | 🔵 Enunciada | SE PIDE | Idem |
| Neutro de la suma: $A + \mathcal{O} = A$ | 🔵 Enunciada | SE PIDE | Idem |
| Opuesto: $A + (-A) = \mathcal{O}$ | 🔵 Enunciada | SE PIDE | Idem |
| Asociativa del escalar: $\alpha(\beta A) = (\alpha\beta)A$ | 🔵 Enunciada | SE PIDE | Clase 1, 17-mar |
| Distributiva 1: $\alpha(A+B) = \alpha A + \alpha B$ | 🔵 Enunciada | SE PIDE | Idem |
| Distributiva 2: $(\alpha+\beta)A = \alpha A + \beta A$ | 🔵 Enunciada | SE PIDE | Idem |
| Neutro escalar: $1 \cdot A = A$ | 🔵 Enunciada | SE PIDE | Idem |

#### B. Producto de matrices

| Propiedad | Estado | Veredicto | Evidencia |
|-----------|--------|-----------|-----------|
| Asociativa: $A(BC) = (AB)C$ | 🔵 Enunciada | SE PIDE | Clase 1, 17-mar (línea 233-242) |
| Distributiva izq: $A(B+C) = AB+AC$ | 🔵 Enunciada | SE PIDE | Idem |
| Distributiva der: $(A+B)C = AC+BC$ | 🔵 Enunciada | SE PIDE | Idem |
| Neutro: $A \cdot \text{Id} = \text{Id} \cdot A = A$ | 🔵 Enunciada | SE PIDE | Idem |
| Escalar entre factores: $k(AB) = (kA)B = A(kB)$ | 🔵 Enunciada | SE PIDE | Idem |
| **NO conmutatividad: $AB \neq BA$ en general** | 🟢 Enfatizada con contraejemplo | SE PIDE saber aplicar | Clase 1, 17-mar (231-233): *"lo veo siempre en los parciales A por B igual a B por A que lo asumen... vamos a hacer énfasis en eso, en ningún parcial aparece que asume que conmuta"* |
| Producto por vector canónico extrae columna $j$ | 🟢 Demostrada en clase | SE PIDE | Clase 2, 18-mar (líneas 165-171); ejercicio V.3 lo pide explícitamente |

#### C. Traspuesta — las 4 propiedades

> Cita maestra: *"vamos a ver cuatro propiedades que tenemos que manejar en esta operación"* (clase 2, 18-mar, línea 35).

| Propiedad | Estado | Veredicto | Evidencia |
|-----------|--------|-----------|-----------|
| Prop 1: $(A^T)^T = A$ | 🔵 Enunciada | SE PIDE | Clase 2, 18-mar — bajo "tenemos que manejar" |
| Prop 2: $(A+B)^T = A^T + B^T$ | 🟢 **Demostrada en este doc** | SE PIDE | Esquema modelo de demostración |
| Prop 3: $(\alpha A)^T = \alpha A^T$ | 🟢 **Demostrada en este doc** + error común flagged en clase | SE PIDE | Clase 2, 18-mar (46-48): *"un error común... ponen alfa por a traspuesta igual a alfa traspuesta por a traspuesta"* |
| Prop 4: $(AB)^T = B^T A^T$ — **orden invertido** | 🟢 Error común enfatizado en clase | SE PIDE | Clase 2, 18-mar (52-58): *"esto está mal porque las matrices no conmutan... los corregirían si lo ponés así como mal"* |

#### D. Simétrica y antisimétrica

| Propiedad / Teorema | Estado | Veredicto | Evidencia |
|---------------------|--------|-----------|-----------|
| Definición simétrica: $A^T = A$ | ⚪ Definición | Definicional | Clase 2, 18-mar |
| Definición antisimétrica: $A^T = -A$ + diagonal nula | ⚪ Definición | Definicional | Idem |
| Suma de simétricas es simétrica | 🟢 **Demostrada completa en clase** | SE PIDE | Clase 2, 18-mar (líneas 81-90) |
| $\alpha \cdot A$ simétrica si $A$ simétrica | 🟡 Esquema en clase | SE PIDE | Clase 2, 18-mar (90-93): *"algo muy similar se puede hacer para la propiedad 2"* |
| Suma de antisimétricas es antisimétrica | 🟡 Análoga | SE PIDE | Clase 2, 18-mar (90-93): *"algo muy parecido acá se podría hacer / la propiedad de la antisimétrica"* |
| $\alpha \cdot A$ antisimétrica si $A$ antisimétrica | 🟡 Análoga | SE PIDE | Idem |
| **$AB$ simétrica $\iff AB = BA$** (con $A, B$ simétricas) — directo y recíproco | 🟢 **Demostrada completa en clase**, ambas direcciones | SE PIDE | Clase 2, 18-mar (177-198) — ejercicio V.5.2 |
| $\frac{1}{2}(A + A^T)$ es simétrica | 🟢 **Demostrada completa en clase** | SE PIDE | Clase 2, 18-mar (199-218) — ejercicio V.6.1 |
| $\frac{1}{2}(A - A^T)$ es antisimétrica | ⚪ Tarea (análoga) | SE PIDE | Clase 2, 18-mar (218): *"les dejo para que ustedes hagan la parte 2"* |
| Toda matriz cuadrada = simétrica + antisimétrica | ⚪ Tarea | SE PIDE | Clase 2, 18-mar (218); también clase 4, 25-mar (33) |

#### E. Traza — las 4 propiedades

> Cita maestra: *"al igual que las traspuestas son 4 propiedades que tenemos que manejar... vamos a demostrar por ejemplo la 1 y la 2 a partir de la definición de la traza"* (clase 2, 18-mar, línea 103).

| Propiedad | Estado | Veredicto | Evidencia |
|-----------|--------|-----------|-----------|
| Prop 1: $tr(A+B) = tr(A) + tr(B)$ | 🟢 **Demostrada completa en clase con sumatorias** | SE PIDE | Clase 2, 18-mar (111-122) |
| Prop 2: $tr(\alpha A) = \alpha \cdot tr(A)$ | 🟡 Esquema en clase ("análoga") | SE PIDE | Clase 2, 18-mar (122) |
| Prop 3: $tr(A^T) = tr(A)$ | 🟡 Explicada verbalmente | SE PIDE | Clase 2, 18-mar (106): *"como la diagonal principal no cambia al traspone, la traza tampoco"* |
| Prop 4: $tr(AB) = tr(BA)$ | 🔵 Enunciada (no demostrada formal) pero **muy importante** | SE PIDE | Clase 2, 18-mar (106-107): *"la que es muy poco intuitiva... siempre se cumple"* |
| **Aplicación: NO existen $A, B$ con $AB - BA = \text{Id}$** | 🟢 **Demostrada por absurdo en clase** | SE PIDE | Clase 3, 24-mar (276-298) — usa traza prop 4 |
| $tr(A - B) = tr(A) - tr(B)$ | 🟢 Verificada en clase | SE PIDE | Clase 3, 24-mar (264-275) |

#### F. Inversa — las 4 propiedades

> Cita maestra: *"vamos a ver ahora las propiedades de la inversa, algunas que tenemos que manejar y vamos a demostrar algunas de ellas"* (clase 3, 24-mar, línea 48).

| Propiedad | Estado | Veredicto | Evidencia |
|-----------|--------|-----------|-----------|
| Definición: $A \cdot A^{-1} = A^{-1} \cdot A = \text{Id}$ | ⚪ Definición | Definicional | Clase 3, 24-mar |
| Unicidad de la inversa | 🔵 Enunciada | SE PIDE | Clase 3, 24-mar (48): *"4 propiedades... unicidad"* |
| Prop 1: $(A^{-1})^{-1} = A$ | 🔵 Enunciada (intuitiva) | SE PIDE | Clase 3, 24-mar |
| Prop 2: $(AB)^{-1} = B^{-1} A^{-1}$ — **orden invertido** | 🟢 **Demostrada completa en clase y en este doc** | SE PIDE | Clase 3, 24-mar (54-66) |
| Prop 3: $(\alpha A)^{-1} = \frac{1}{\alpha} A^{-1}$ | 🔵 Enunciada | SE PIDE | Clase 3, 24-mar |
| Prop 4: $(A^T)^{-1} = (A^{-1})^T$ | 🔵 Enunciada + ejercicio V.16.3 lo pide demostrar | SE PIDE | Clase 3, 24-mar; ejercicio V.16.3 |
| **Cálculo de inversa por método directo** | 🟢 Hecho en clase | SE PIDE como ejercicio | Clase 3, 24-mar (8): *"generalmente en los parciales se dice 'hallen la inversa' y ustedes aplican el método"* |
| **Despeje matricial $A \cdot X = B$, $X \cdot A = B$** | 🟢 Estilo "ejercicio de parcial" | SE PIDE | Clase 3, 24-mar (312): *"lo que vemos ahora son más apuntando, son más ejercicios de parcial"* |

#### G. Tipos especiales

| Concepto | Estado | Veredicto | Evidencia |
|----------|--------|-----------|-----------|
| Definición idempotente: $A^2 = A$ | ⚪ Definición | Definicional | Clase 3, 24-mar |
| **Idempotente + invertible $\Rightarrow A = \text{Id}$** | 🟢 **Demostrada completa en clase** | SE PIDE | Clase 3, 24-mar (79-86) — ejercicio VI.2 |
| $(A+\text{Id})^3 = \text{Id} + 7A$ si $A$ idempotente | 🟢 **Demostrada completa en clase** | SE PIDE | Clase 4, 25-mar (17-29) |
| Definición nilpotente: $A^k = \mathcal{O}$, $A^{k-1} \neq \mathcal{O}$ | ⚪ Definición | Definicional | Clase 4, 25-mar (33-34) |
| **$P^{-1} A P$ nilpotente del mismo grado que $A$** | 🟢 **Demostrada completa en clase** (V.7.2) | SE PIDE | Clase 4, 25-mar (71-84) |
| Definición ortogonal: $A^T = A^{-1}$ | ⚪ Definición | Definicional | Clase 4, 25-mar (89, 94) |
| Propiedades formales de ortogonal | 🔴 *"no lo vimos en el teórico"* | NO se piden propiedades formales | Clase 4, 25-mar (89): *"esto es ortogonal, no lo vimos en el teórico, pero esto lo podrían hacer"* |
| Ejercicios con ortogonal (V.12) | 🟢 Hechos en clase | SE PIDE como ejercicio | Idem |

#### H. Inducción y factorización (técnicas de los ejercicios V.4, V.8, V.10, V.11, VI.1, VI.3)

| Técnica / Ejercicio | Estado | Veredicto | Evidencia |
|---------------------|--------|-----------|-----------|
| **Inducción para potencia $A^n$ (V.4)** | 🟢 Anunciada como pedible | SE PIDE | Clase 4, 25-mar (31-32): *"con eso podrían hacer el ejercicio 4"*; clase 12, 29-abr (232-233): *"repasen la inducción completa"* |
| **Inducción $A^2 = 2A - \text{Id} \Rightarrow A^n$ (V.10.3)** | 🟢 Anunciada como pedible | SE PIDE | Clase 4, 25-mar (40); clase 12, 29-abr |
| **Inducción $A^n$ para triangular 2×2 (VI.1)** | 🟢 Demostrada en clase para caso similar | SE PIDE | Clase 3, 24-mar (165-172) hace una versión análoga |
| **Inducción para diagonal $A^k$** | 🟢 Demostrada en clase | SE PIDE | Clase 3, 24-mar (231-237) |
| **Factorización para invertibilidad: $A^3 - A = \text{Id} \Rightarrow A^{-1} = A^2 - \text{Id}$** | 🟢 Demostrada en clase | SE PIDE | Clase 4, 25-mar (9-14) |
| **Factorización $A^3 = \mathcal{O} \Rightarrow (A+\text{Id})^{-1} = A^2 - A + \text{Id}$ (VI.3)** | 🟢 Demostrada en clase | SE PIDE | Clase 3, 24-mar (115-130) |
| **Ley de simplificación V.11**: $AB = AC, A$ invertible $\Rightarrow B = C$ | 🟢 Demostrada en clase | SE PIDE | Clase 4, 25-mar (86-87) |
| **V.16 V/F (3 partes)**: identificar enunciados ciertos/falsos + agregar hipótesis | 🟢 Estilo de parcial | SE PIDE | Clase 4, 25-mar (105) |
| **V.17 — $\lambda \text{Id}$ conmuta con todo** | 🔴 **MARCADO COMO OPCIONAL** | NO SE PIDE | Clase 4, 25-mar (105): *"el 17 podría ser opcional"* |

### En lenguaje práctico: ¿qué significa todo esto para Enrique?

**Todo entra como demostración pedible, salvo V.17 (opcional).** El profesor no descartó ninguna otra. Ahora bien, no todo tiene la misma probabilidad — la prioridad para estudiar es:

1. **Prioridad MÁXIMA (🟢 demostradas en pizarrón por el profesor — el modelo exacto que esperaría ver):**
   - Suma de simétricas es simétrica
   - $AB$ simétrica $\iff AB = BA$ (con $A, B$ simétricas)
   - $\frac{1}{2}(A + A^T)$ es simétrica
   - $tr(A+B) = tr(A) + tr(B)$ — la demo con sumatorias
   - **NO existen $A, B$ con $AB - BA = \text{Id}$** ← la estrella del módulo
   - $(AB)^{-1} = B^{-1} A^{-1}$
   - Idempotente + invertible $\Rightarrow A = \text{Id}$
   - $A^3 - A = \text{Id} \Rightarrow A^{-1} = A^2 - \text{Id}$
   - $A^3 = \mathcal{O} \Rightarrow (A + \text{Id})^{-1} = A^2 - A + \text{Id}$
   - $P^{-1}AP$ nilpotente del mismo grado que $A$
   - Inducción para potencias (V.4, V.10, VI.1)

2. **Prioridad ALTA (🔵 enunciadas pero "que tenemos que manejar" — probables como demo):**
   - Las **3 propiedades restantes de traspuesta** (1, 2, 3 — ya tenés el modelo de la 2 y 3 en el doc)
   - Las **2 propiedades restantes de traza** (3, 4 — sobre todo la 4 con sumatorias dobles)
   - Las **3 propiedades restantes de inversa** (1, 3, 4)

3. **Prioridad MEDIA (🟡 esquemas / análogas — saber deducirlas):**
   - $\alpha A$ simétrica si $A$ es simétrica (análoga a suma)
   - Mismas para antisimétrica
   - $tr(\alpha A) = \alpha \cdot tr(A)$

4. **NO estudiar para demo (🔴):**
   - **V.17** — opcional explícito.
   - **Propiedades formales de matriz ortogonal** — el profesor dijo que no entró al teórico, aunque la **definición** y los **ejercicios** sí.

### Lo que el profesor reiteró sobre cómo presentar una demo en parcial

| Regla | Por qué importa |
|-------|------------------|
| Escribir **hipótesis** y **tesis** explícitamente | Estructura mínima esperada |
| Justificar cada paso citando la propiedad usada | Sin esto, te bajan puntos |
| No hace falta el número de la propiedad — describila con palabras | Te quita estrés de memorización |
| Cerrar con $\blacksquare$ o "L.Q.Q.D." o "queda demostrado" | Cierre formal |
| **Nunca asumir $AB = BA$** salvo hipótesis explícita | Es el error #1 que el prof flageó: *"lo veo siempre en los parciales"* |

---

## Patrón de demostraciones que aparecen en parcial

El profesor estructura las demostraciones siempre igual. Si en parcial te piden una demostración, segui este esquema:

1. **Escribir la hipótesis** explícitamente (lo que te dan)
2. **Escribir la tesis** (lo que tenés que probar)
3. **Justificar cada paso** (qué propiedad usaste, qué hipótesis aplicaste)
4. **Cerrar con QED** (escribir "queda demostrado", "L.Q.Q.D." o el símbolo $\blacksquare$ al final)

Ejemplo del esqueleto:

> **Hipótesis:** $A^T = A$, $B^T = B$, $AB = BA$.
> **Tesis:** $AB$ es simétrica.
>
> $(AB)^T = B^T A^T$ — *propiedad 4 de la traspuesta*
> $= BA$ — *hipótesis: $A, B$ simétricas*
> $= AB$ — *hipótesis: conmutan* $\blacksquare$

---

## Mapa de qué herramienta usar según el tipo de ejercicio

| Tipo de ejercicio del práctico | Técnica clave |
|--------------------------------|---------------|
| Cálculo directo (V.1, V.2) | Aplicar definiciones, cuidar conformabilidad |
| Producto por canónicos (V.3) | Saber que extrae columnas |
| Potencias por inducción (V.4, V.10.3, VI.1) | Base + hipótesis + tesis + demostración usando $A^{h+1} = A^h \cdot A$ |
| Simétricas / antisimétricas (V.5, V.6, V.16.2) | Aplicar $(\cdot)^T$ y propiedades 1-4 de traspuesta |
| Nilpotente (V.7) | Calcular potencias hasta encontrar la nula; usar $P P^{-1} = \text{Id}$ |
| Ecuación polinomial → inversa (V.8, V.10.1, VI.3) | Despejar $A^{-1}$ multiplicando por $A^{-1}$, o factorizar $A \cdot (\ldots) = \text{Id}$ |
| Inversa por método directo (V.9) | Plantear $AX = \text{Id}$, resolver sistema |
| Ley de simplificación (V.11) | Multiplicar por $A^{-1}$ por izquierda |
| Ortogonal (V.12) | Imponer $A^T A = \text{Id}$, resolver sistema |
| Diagonalización ($P^{-1}AP$, V.13) | Multiplicar por $P$ para evitar calcular $P^{-1}$ |
| ¿Invertible? Contraejemplo (V.14) | Probar con $\text{Id}$ y $-\text{Id}$ |
| Conmutatividad (V.15, V.17) | Plantear $AB = BA$ con incógnitas, resolver sistema |
| V/F (V.16) | Buscar contraejemplos con $\text{Id}$, $\mathcal{O}$, $\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$ |

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

# PARTE 10 — Banco de demostraciones 🟢 paso a paso

Esta parte reúne **todas las demostraciones que el profesor hizo en pizarrón** (las marcadas como 🟢 en la auditoría de PARTE 8) en un solo lugar consolidado. Están escritas siguiendo el esquema oficial que pidió el profesor en parcial:

1. **Hipótesis** explícita (qué te dan)
2. **Tesis** explícita (qué probar)
3. **Pasos** con justificación de cada uno
4. **Cierre con $\blacksquare$**

Estas son las demos de **prioridad MÁXIMA** para parcial. Si las dominás todas, estás cubierto.

> 📌 **Sobre la duplicación con secciones anteriores:** muchas de estas demos ya aparecen en sus secciones naturales del documento (PARTE 4 trata traspuesta/sym/traza, PARTE 5 trata inversa, PARTE 6 trata idempotente/nilpotente, PARTE 7 trata los ejercicios del práctico). Esta PARTE 10 las **consolida en un mismo lugar para repaso final** — útil para los 30 minutos antes del parcial. Cada subsección de abajo cita la sección original para referencia cruzada.

### Mapa de dónde vive cada demo en el documento

| Demo | Aparece en (sección original) | Aparece consolidada en |
|------|-------------------------------|------------------------|
| Producto por vector canónico extrae columna | PARTE 3 (con ejemplo numérico) | PARTE 10.A.1 |
| Traspuesta props 2, 3, 4 | PARTE 4 — Traspuesta | PARTE 10.B.1, B.2, B.3 |
| Suma simétricas + ½(A+Aᵀ) sim + AB sim ⟺ conmutan | PARTE 4 — Simétricas | PARTE 10.C.1, C.2, C.3 |
| Traza prop 1 + corolario tr(A−B) + NO ∃ AB−BA=Id | PARTE 4 — Traza | PARTE 10.D.1, D.2, D.3 |
| Inversa prop 2: (AB)⁻¹ = B⁻¹A⁻¹ | PARTE 5 — Inversa | PARTE 10.E.1 |
| Idempotente+invertible⇒Id, (A+Id)³, P⁻¹AP nilpotente | PARTE 6 — Tipos especiales | PARTE 10.F.1, F.2, F.3 |
| Inducciones (V.4, V.10, VI.1) + diagonal Aᵏ | PARTE 7 — Ejercicios | PARTE 10.G.1, G.2, G.3, G.4 |
| Factorizaciones (V.8, VI.3) | PARTE 7 — Ejercicios | PARTE 10.G.5, G.6 |
| Ley simplificación V.11 + (Aᵀ)⁻¹ = (A⁻¹)ᵀ | PARTE 7 — Ejercicios | PARTE 10.H.1, H.2 |

---

## Sección A — Producto y vectores canónicos

### A.1 — Producto por vector canónico extrae columna $j$

**Hipótesis:** $A \in \mathcal{M}_{n \times n}$ y $\vec{v}_j$ es el vector canónico (columna con un $1$ en la posición $j$ y ceros en el resto).

**Tesis:** $A \cdot \vec{v}_j$ es la columna $j$ de $A$.

**Demostración:**

Sea $A = ((a_{ik}))$ y $\vec{v}_j$ con componentes $v_k = 1$ si $k = j$, $v_k = 0$ si $k \neq j$.

La fila $i$ del producto es:

$$(A \cdot \vec{v}_j)_i = \sum_{k=1}^{n} a_{ik} \cdot v_k \quad \text{(definición de producto fila}\times\text{columna)}$$

$$= a_{ij} \cdot 1 + \sum_{k \neq j} a_{ik} \cdot 0 \quad \text{(porque }v_k = 0\text{ salvo en }k=j\text{)}$$

$$= a_{ij}$$

Como esto vale para toda fila $i$, el resultado es la columna $j$ de $A$. $\blacksquare$

> Ejemplo numérico desarrollado: ver PARTE 3, sección "Producto por vectores canónicos".

---

## Sección B — Traspuesta

### B.1 — Propiedad 2: $(A + B)^T = A^T + B^T$

**Hipótesis:** $A, B \in \mathcal{M}_{m \times n}$.

**Tesis:** $(A + B)^T = A^T + B^T$.

**Demostración:**

$$[A + B]^T = [((a_{ij})) + ((b_{ij}))]^T \quad \text{(definición de }A\text{ y }B\text{ por entradas)}$$

$$= [((a_{ij} + b_{ij}))]^T \quad \text{(definición de suma entrada por entrada)}$$

$$= ((a_{ji} + b_{ji})) \quad \text{(definición de traspuesta: intercambiar }i\text{ con }j\text{)}$$

$$= ((a_{ji})) + ((b_{ji})) \quad \text{(separar la suma)}$$

$$= A^T + B^T \quad \blacksquare$$

### B.2 — Propiedad 3: $(\alpha \cdot A)^T = \alpha \cdot A^T$

**Hipótesis:** $A \in \mathcal{M}_{m \times n}$, $\alpha \in \mathbb{R}$.

**Tesis:** $(\alpha A)^T = \alpha A^T$.

**Demostración:**

$$(\alpha \cdot A)^T = ((\alpha \cdot a_{ij}))^T \quad \text{(definición de producto por escalar)}$$

$$= ((\alpha \cdot a_{ji})) \quad \text{(definición de traspuesta)}$$

$$= \alpha \cdot ((a_{ji})) \quad \text{(sacar el escalar como factor común)}$$

$$= \alpha \cdot A^T \quad \blacksquare$$

> **Error común a evitar:** escribir $(\alpha A)^T = \alpha^T A^T$. Los escalares no se trasponen — un número real es lo que es.

### B.3 — Propiedad 4: $(A \cdot B)^T = B^T \cdot A^T$ (orden invertido)

**Hipótesis:** $A \in \mathcal{M}_{m \times n}$, $B \in \mathcal{M}_{n \times p}$ (conformables para producto).

**Tesis:** $(AB)^T = B^T A^T$.

**Demostración:**

Llamemos $C = AB$ con entradas $c_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj}$.

La entrada $(i, j)$ de $C^T$ es la entrada $(j, i)$ de $C$:

$$(C^T)_{ij} = c_{ji} = \sum_{k=1}^{n} a_{jk} \cdot b_{ki} \quad \text{(definición de producto)}$$

Ahora calculemos la entrada $(i, j)$ de $B^T A^T$. Como $(B^T)_{ik} = b_{ki}$ y $(A^T)_{kj} = a_{jk}$:

$$(B^T A^T)_{ij} = \sum_{k=1}^{n} (B^T)_{ik} \cdot (A^T)_{kj} = \sum_{k=1}^{n} b_{ki} \cdot a_{jk} \quad \text{(definición de producto + traspuesta)}$$

$$= \sum_{k=1}^{n} a_{jk} \cdot b_{ki} \quad \text{(conmutar números reales adentro de la suma)}$$

Comparando: $(C^T)_{ij} = (B^T A^T)_{ij}$ para todo $i, j$. Entonces $C^T = (AB)^T = B^T A^T$. $\blacksquare$

> **Error común a evitar:** escribir $(AB)^T = A^T B^T$. **El orden se invierte** porque las matrices no conmutan, y porque las dimensiones ni siquiera te dejan en general.

---

## Sección C — Simétrica y antisimétrica

### C.1 — Suma de simétricas es simétrica

**Hipótesis:** $A, B$ simétricas (es decir, $A^T = A$ y $B^T = B$).

**Tesis:** $A + B$ es simétrica.

**Demostración:**

$$(A + B)^T = A^T + B^T \quad \text{(propiedad 2 de traspuesta)}$$

$$= A + B \quad \text{(hipótesis: }A, B\text{ simétricas)}$$

Entonces $(A+B)^T = A + B$, que es la definición de simétrica. $\blacksquare$

### C.2 — $AB$ simétrica $\iff AB = BA$ (con $A, B$ simétricas)

**Hipótesis:** $A, B$ matrices simétricas, es decir, $A^T = A$ y $B^T = B$.

**Tesis:** $AB$ es simétrica $\iff AB = BA$.

Hay que probar las **dos direcciones** ("$\iff$" pide ambas).

**Directo ($\Rightarrow$):** asumimos $AB$ simétrica, queremos llegar a $AB = BA$.

$$AB = (AB)^T \quad \text{(hipótesis: }AB\text{ simétrica)}$$

$$= B^T A^T \quad \text{(propiedad 4 de traspuesta)}$$

$$= B \cdot A \quad \text{(hipótesis: }A, B\text{ simétricas)}$$

Entonces $AB = BA$. ✓

**Recíproco ($\Leftarrow$):** asumimos $AB = BA$, queremos llegar a que $AB$ es simétrica.

$$(AB)^T = B^T A^T \quad \text{(propiedad 4 de traspuesta)}$$

$$= B \cdot A \quad \text{(hipótesis: }A, B\text{ simétricas)}$$

$$= A \cdot B \quad \text{(hipótesis: }AB = BA\text{)}$$

Entonces $(AB)^T = AB$, o sea $AB$ es simétrica. ✓

Probadas ambas direcciones. $\blacksquare$

### C.3 — $\frac{1}{2}(A + A^T)$ es simétrica

**Hipótesis:** $A$ matriz cuadrada cualquiera.

**Tesis:** $S = \frac{1}{2}(A + A^T)$ es simétrica.

**Demostración:**

$$S^T = \left[\tfrac{1}{2}(A + A^T)\right]^T$$

$$= \tfrac{1}{2}(A + A^T)^T \quad \text{(propiedad 3 de traspuesta: el escalar sale)}$$

$$= \tfrac{1}{2}(A^T + (A^T)^T) \quad \text{(propiedad 2 de traspuesta: traspuesta de una suma)}$$

$$= \tfrac{1}{2}(A^T + A) \quad \text{(propiedad 1 de traspuesta: }(A^T)^T = A\text{)}$$

$$= \tfrac{1}{2}(A + A^T) \quad \text{(conmutativa de la suma)}$$

$$= S$$

Como $S^T = S$, $S$ es simétrica. $\blacksquare$

> **Análoga (queda como ejercicio):** $\frac{1}{2}(A - A^T)$ es antisimétrica. Mismo esquema, terminás llegando a $-S$.

---

## Sección D — Traza

### D.1 — Propiedad 1: $tr(A + B) = tr(A) + tr(B)$

**Hipótesis:** $A, B \in \mathcal{M}_{n \times n}$ (cuadradas, misma dimensión).

**Tesis:** $tr(A + B) = tr(A) + tr(B)$.

**Demostración:**

$$tr(A + B) = \sum_{i=1}^{n} (A + B)_{ii} \quad \text{(definición de traza)}$$

$$= \sum_{i=1}^{n} (a_{ii} + b_{ii}) \quad \text{(definición de suma de matrices)}$$

$$= \sum_{i=1}^{n} a_{ii} + \sum_{i=1}^{n} b_{ii} \quad \text{(separar la sumatoria)}$$

$$= tr(A) + tr(B) \quad \text{(definición de traza)}$$

$\blacksquare$

### D.2 — Corolario: $tr(A - B) = tr(A) - tr(B)$

**Hipótesis:** $A, B \in \mathcal{M}_{n \times n}$.

**Tesis:** $tr(A - B) = tr(A) - tr(B)$.

**Demostración:**

$$tr(A - B) = tr(A + (-1) \cdot B) \quad \text{(reescribir resta como suma con escalar }-1\text{)}$$

$$= tr(A) + tr((-1) \cdot B) \quad \text{(propiedad 1 de traza)}$$

$$= tr(A) + (-1) \cdot tr(B) \quad \text{(propiedad 2 de traza: el escalar sale)}$$

$$= tr(A) - tr(B) \quad \blacksquare$$

### D.3 — Aplicación clásica: NO existen $A, B$ tales que $AB - BA = \text{Id}$

> Esta es **la estrella del módulo** — la demo más probable de caer en parcial dentro de traza.

**Tesis:** No existen matrices cuadradas $A, B$ tales que $AB - BA = \text{Id}$.

**Demostración por absurdo:** supongamos que sí existen. Entonces:

$$AB - BA = \text{Id}$$

Tomamos traza a ambos lados:

$$tr(AB - BA) = tr(\text{Id})$$

**Lado izquierdo:**

$$tr(AB - BA) = tr(AB) - tr(BA) \quad \text{(corolario D.2)}$$

$$= tr(AB) - tr(AB) \quad \text{(propiedad 4 de traza: }tr(AB) = tr(BA)\text{)}$$

$$= 0$$

**Lado derecho:**

$$tr(\text{Id}) = \underbrace{1 + 1 + \cdots + 1}_{n \text{ veces}} = n$$

Igualando: $0 = n$. Como $n \geq 1$ (la matriz tiene al menos una fila), esto es **absurdo**. Por lo tanto, no pueden existir $A, B$ con $AB - BA = \text{Id}$. $\blacksquare$

---

## Sección E — Inversa

### E.1 — Propiedad 2: $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$ (orden invertido)

**Hipótesis:** $A, B$ invertibles, ambas cuadradas $n \times n$.

**Tesis:** $(AB)^{-1} = B^{-1} A^{-1}$.

**Estrategia:** para probar que $X$ es la inversa de $Y$, basta verificar que $Y \cdot X = \text{Id}$ (por unicidad de la inversa, alcanza con un lado).

**Demostración:** verificamos $(AB) \cdot (B^{-1} A^{-1}) = \text{Id}$.

$$(AB)(B^{-1} A^{-1}) = A \cdot (B \cdot B^{-1}) \cdot A^{-1} \quad \text{(asociativa del producto)}$$

$$= A \cdot \text{Id} \cdot A^{-1} \quad \text{(definición de inversa: }B \cdot B^{-1} = \text{Id}\text{)}$$

$$= A \cdot A^{-1} \quad \text{(neutro del producto: }M \cdot \text{Id} = M\text{)}$$

$$= \text{Id} \quad \text{(definición de inversa)}$$

Entonces $B^{-1} A^{-1}$ es la inversa de $AB$, es decir, $(AB)^{-1} = B^{-1} A^{-1}$. $\blacksquare$

> **Por qué se invierte el orden:** porque las matrices no conmutan. Analogía: si te ponés medias y después zapatos, para sacártelos el orden inverso — primero zapatos, después medias. **Lo último que entró es lo primero que sale.**

---

## Sección F — Idempotente y nilpotente

### F.1 — Idempotente + invertible $\Rightarrow A = \text{Id}$ (ejercicio VI.2)

**Hipótesis:** $A$ idempotente ($A^2 = A$) **y** $A$ invertible (existe $A^{-1}$).

**Tesis:** $A = \text{Id}$.

**Demostración:** partimos de la hipótesis de idempotencia y multiplicamos por $A^{-1}$ a izquierda en ambos lados:

$$A^2 = A$$

$$A^{-1} \cdot A^2 = A^{-1} \cdot A \quad \text{(multiplicar por }A^{-1}\text{ a izquierda)}$$

$$A^{-1} \cdot A \cdot A = A^{-1} \cdot A \quad \text{(reescribir }A^2\text{ como }A \cdot A\text{)}$$

$$\text{Id} \cdot A = \text{Id} \quad \text{(}A^{-1} \cdot A = \text{Id}\text{ por definición de inversa)}$$

$$A = \text{Id} \quad \blacksquare$$

> **Cuidado:** esto NO dice que toda matriz idempotente sea $\text{Id}$. Solo cuando además es invertible. Hay idempotentes no invertibles (como la matriz nula).

### F.2 — Si $A$ es idempotente, entonces $(A + \text{Id})^3 = \text{Id} + 7A$

**Hipótesis:** $A$ idempotente ($A^2 = A$, lo que implica también $A^k = A$ para todo $k \geq 1$).

**Tesis:** $(A + \text{Id})^3 = \text{Id} + 7A$.

**Demostración:** desarrollamos el cubo del binomio. **Cuidado:** $A$ y $\text{Id}$ sí conmutan (siempre conmutan con $\text{Id}$), así que podemos usar el binomio de Newton libremente.

$$(A + \text{Id})^3 = A^3 + 3 A^2 \text{Id} + 3 A \text{Id}^2 + \text{Id}^3 \quad \text{(binomio de Newton — conmutan)}$$

$$= A^3 + 3 A^2 + 3 A + \text{Id} \quad \text{(}\text{Id}^k = \text{Id}\text{; multiplicar por }\text{Id}\text{ no cambia nada)}$$

$$= A + 3 A + 3 A + \text{Id} \quad \text{(hipótesis: }A^2 = A\text{ implica }A^3 = A \cdot A^2 = A \cdot A = A\text{)}$$

$$= 7A + \text{Id} \quad \text{(suma de términos en }A\text{)}$$

$$= \text{Id} + 7A \quad \blacksquare$$

### F.3 — $P^{-1} A P$ es nilpotente del mismo grado que $A$ (ejercicio V.7.2)

**Hipótesis:** $A$ nilpotente de grado $k$ (es decir, $A^k = \mathcal{O}$ y $A^{k-1} \neq \mathcal{O}$); $P$ invertible.

**Tesis:** $B = P^{-1} A P$ es nilpotente del mismo grado $k$, o sea $B^k = \mathcal{O}$ y $B^{k-1} \neq \mathcal{O}$.

**Demostración:**

**Paso 1: $B^k = \mathcal{O}$.**

Calculemos $B^k = (P^{-1} A P)^k$. Probamos por inducción (o por desarrollo directo):

$$B^2 = (P^{-1} A P)(P^{-1} A P) = P^{-1} A (P P^{-1}) A P = P^{-1} A \cdot \text{Id} \cdot A P = P^{-1} A^2 P$$

Por inducción se generaliza: $B^k = P^{-1} A^k P$.

$$B^k = P^{-1} A^k P \quad \text{(asociativa + }P P^{-1} = \text{Id}\text{ aplicado }k-1\text{ veces)}$$

$$= P^{-1} \cdot \mathcal{O} \cdot P \quad \text{(hipótesis: }A^k = \mathcal{O}\text{)}$$

$$= \mathcal{O} \quad \text{(cualquier producto con la matriz nula da la nula)}$$

**Paso 2: $B^{k-1} \neq \mathcal{O}$.**

Supongamos por absurdo que $B^{k-1} = \mathcal{O}$. Entonces:

$$P^{-1} A^{k-1} P = \mathcal{O}$$

Multiplicando por $P$ a izquierda y por $P^{-1}$ a derecha:

$$P \cdot P^{-1} A^{k-1} P \cdot P^{-1} = P \cdot \mathcal{O} \cdot P^{-1}$$

$$\text{Id} \cdot A^{k-1} \cdot \text{Id} = \mathcal{O}$$

$$A^{k-1} = \mathcal{O}$$

Pero esto **contradice** la hipótesis de que $A^{k-1} \neq \mathcal{O}$. Absurdo. Por lo tanto, $B^{k-1} \neq \mathcal{O}$.

Combinando paso 1 y paso 2: $B$ es nilpotente de grado exactamente $k$. $\blacksquare$

---

## Sección G — Inducción y factorización

### G.1 — Inducción para $A^n$ con $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ (ejercicio VI.1)

**Tesis:** Para todo $n \geq 1$:

$$A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$$

**Demostración por inducción completa sobre $n$:**

**Base ($n = 1$):**

$$A^1 = A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \;\;\checkmark$$

Coincide con la fórmula tomando $n = 1$.

**Hipótesis inductiva ($n = h$):** asumimos válido para $h$:

$$A^h = \begin{pmatrix} 1 & h \\ 0 & 1 \end{pmatrix}$$

**Tesis ($n = h+1$):** queremos probar:

$$A^{h+1} = \begin{pmatrix} 1 & h+1 \\ 0 & 1 \end{pmatrix}$$

**Paso inductivo:**

$$A^{h+1} = A^h \cdot A \quad \text{(propiedad de potencias)}$$

$$= \begin{pmatrix} 1 & h \\ 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \quad \text{(hipótesis inductiva)}$$

Multiplicando fila por columna:

$$= \begin{pmatrix} 1 \cdot 1 + h \cdot 0 & 1 \cdot 1 + h \cdot 1 \\ 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 1 \end{pmatrix} = \begin{pmatrix} 1 & h+1 \\ 0 & 1 \end{pmatrix} \;\;\checkmark$$

Coincide con la fórmula para $n = h + 1$. Por inducción, vale para todo $n \geq 1$. $\blacksquare$

### G.2 — Inducción para $A^n$ con $A^2 = 2A - \text{Id}$ (ejercicio V.10.3)

**Hipótesis:** $A$ cuadrada con $A^2 = 2A - \text{Id}$.

**Tesis:** Para todo $n \geq 1$:

$$A^n = nA - (n-1)\text{Id}$$

**Demostración por inducción:**

**Base ($n = 1$):** $A^1 = A = 1 \cdot A - 0 \cdot \text{Id}$. ✓

**Hipótesis ($n = h$):** $A^h = hA - (h-1)\text{Id}$.

**Tesis ($n = h+1$):** $A^{h+1} = (h+1)A - h \cdot \text{Id}$.

**Paso inductivo:**

$$A^{h+1} = A^h \cdot A$$

$$= [hA - (h-1)\text{Id}] \cdot A \quad \text{(hipótesis inductiva)}$$

$$= hA^2 - (h-1)\text{Id} \cdot A \quad \text{(distributiva)}$$

$$= hA^2 - (h-1) A \quad \text{(}\text{Id} \cdot A = A\text{)}$$

$$= h(2A - \text{Id}) - (h-1) A \quad \text{(hipótesis: }A^2 = 2A - \text{Id}\text{)}$$

$$= 2hA - h\,\text{Id} - (h-1) A$$

$$= [2h - (h-1)] A - h \,\text{Id}$$

$$= (h+1) A - h \,\text{Id} \;\;\checkmark$$

Coincide con la tesis. $\blacksquare$

### G.3 — Inducción para $A^n$ con $A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$ (ejercicio V.4)

**Tesis:** Para todo $n \geq 1$:

$$A^n = \begin{pmatrix} 1 & n & \frac{n(n+1)}{2} \\ 0 & 1 & n \\ 0 & 0 & 1 \end{pmatrix}$$

> **Nota:** la fórmula equivalente $\frac{n^2 + n}{2}$ aparece en el resumen anterior (es lo mismo: $\frac{n(n+1)}{2} = \frac{n^2+n}{2}$).

**Demostración por inducción:**

**Base ($n = 1$):** $A^1 = A$. La fórmula da $\frac{1 \cdot 2}{2} = 1$ en la posición $(1,3)$, que coincide. ✓

**Hipótesis ($n = h$):**

$$A^h = \begin{pmatrix} 1 & h & \frac{h(h+1)}{2} \\ 0 & 1 & h \\ 0 & 0 & 1 \end{pmatrix}$$

**Tesis ($n = h+1$):**

$$A^{h+1} = \begin{pmatrix} 1 & h+1 & \frac{(h+1)(h+2)}{2} \\ 0 & 1 & h+1 \\ 0 & 0 & 1 \end{pmatrix}$$

**Paso inductivo:**

$$A^{h+1} = A^h \cdot A = \begin{pmatrix} 1 & h & \frac{h(h+1)}{2} \\ 0 & 1 & h \\ 0 & 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$$

Calculando entrada por entrada:

- $(1,1)$: $1 \cdot 1 + h \cdot 0 + \tfrac{h(h+1)}{2} \cdot 0 = 1$ ✓
- $(1,2)$: $1 \cdot 1 + h \cdot 1 + \tfrac{h(h+1)}{2} \cdot 0 = 1 + h = h + 1$ ✓
- $(1,3)$: $1 \cdot 1 + h \cdot 1 + \tfrac{h(h+1)}{2} \cdot 1 = 1 + h + \tfrac{h(h+1)}{2} = \tfrac{2 + 2h + h(h+1)}{2} = \tfrac{h^2 + 3h + 2}{2} = \tfrac{(h+1)(h+2)}{2}$ ✓
- $(2,1)$: $0$, $(2,2)$: $1$, $(2,3)$: $0 + 1 + h = h + 1$ ✓
- $(3,*)$: $0, 0, 1$ ✓

Coincide con la tesis. $\blacksquare$

### G.4 — $A^k$ para matriz diagonal

**Hipótesis:** $A = \text{diag}(d_1, d_2, \ldots, d_n)$ (matriz diagonal).

**Tesis:** Para todo $k \geq 1$:

$$A^k = \text{diag}(d_1^k, d_2^k, \ldots, d_n^k)$$

**Demostración por inducción sobre $k$:**

**Base ($k = 1$):** trivial, $A^1 = A$ y los $d_i^1 = d_i$. ✓

**Hipótesis ($k = h$):** $A^h = \text{diag}(d_1^h, \ldots, d_n^h)$.

**Paso inductivo ($k = h + 1$):**

$$A^{h+1} = A^h \cdot A = \text{diag}(d_1^h, \ldots, d_n^h) \cdot \text{diag}(d_1, \ldots, d_n)$$

Cuando multiplicás dos matrices diagonales, el resultado es diagonal con entradas obtenidas multiplicando las correspondientes:

$$= \text{diag}(d_1^h \cdot d_1, \, d_2^h \cdot d_2, \, \ldots, \, d_n^h \cdot d_n) = \text{diag}(d_1^{h+1}, \ldots, d_n^{h+1}) \;\;\checkmark$$

$\blacksquare$

### G.5 — Factorización: $A^3 - A = \text{Id} \implies A$ invertible y $A^{-1} = A^2 - \text{Id}$

**Hipótesis:** $A$ cuadrada con $A^3 - A = \text{Id}$.

**Tesis:** $A$ es invertible y $A^{-1} = A^2 - \text{Id}$.

**Demostración:** factorizamos para que aparezca un producto $A \cdot (\ldots) = \text{Id}$:

$$A^3 - A = \text{Id}$$

$$A \cdot A^2 - A \cdot \text{Id} = \text{Id} \quad \text{(reescribir}A^3 = A \cdot A^2\text{ y }A = A \cdot \text{Id}\text{)}$$

$$A \cdot (A^2 - \text{Id}) = \text{Id} \quad \text{(factor común }A\text{ a izquierda)}$$

Esto significa que **existe** una matriz $B = A^2 - \text{Id}$ tal que $A \cdot B = \text{Id}$. Por la definición de inversa, $A$ es invertible y:

$$A^{-1} = A^2 - \text{Id} \quad \blacksquare$$

> **Por qué alcanza con un lado:** se puede probar (por unicidad) que si $AB = \text{Id}$ con $A, B$ cuadradas de la misma dimensión, entonces también $BA = \text{Id}$. Por eso al ver $A \cdot (A^2 - \text{Id}) = \text{Id}$, ya tenemos la inversa.

### G.6 — Factorización: $A^3 = \mathcal{O} \implies (A + \text{Id})^{-1} = A^2 - A + \text{Id}$ (ejercicio VI.3)

**Hipótesis:** $A$ cuadrada con $A^3 = \mathcal{O}$ (o sea, $A$ es nilpotente de grado $\leq 3$).

**Tesis:** $A + \text{Id}$ es invertible, y su inversa es $A^2 - A + \text{Id}$.

**Demostración:** verificamos que $(A + \text{Id}) \cdot (A^2 - A + \text{Id}) = \text{Id}$.

$$(A + \text{Id})(A^2 - A + \text{Id}) = A \cdot A^2 - A \cdot A + A \cdot \text{Id} + \text{Id} \cdot A^2 - \text{Id} \cdot A + \text{Id} \cdot \text{Id} \quad \text{(distributiva)}$$

$$= A^3 - A^2 + A + A^2 - A + \text{Id} \quad \text{(simplificar productos con }\text{Id}\text{)}$$

$$= A^3 + (-A^2 + A^2) + (A - A) + \text{Id} \quad \text{(agrupar términos)}$$

$$= A^3 + \text{Id}$$

$$= \mathcal{O} + \text{Id} \quad \text{(hipótesis: }A^3 = \mathcal{O}\text{)}$$

$$= \text{Id}$$

Como $(A + \text{Id})(A^2 - A + \text{Id}) = \text{Id}$, por definición de inversa:

$$(A + \text{Id})^{-1} = A^2 - A + \text{Id} \quad \blacksquare$$

> **Truco general:** este es un caso particular de la identidad $(x+1)(x^2 - x + 1) = x^3 + 1$ del álgebra de polinomios, aplicada a matrices. Cuando veas estructuras así en parcial, pensá en factorizaciones algebraicas conocidas.

---

## Sección H — Ley de simplificación y V/F

### H.1 — Ley de simplificación a izquierda (ejercicio V.11)

**Enunciado:** Si $A$ es invertible y $A \cdot B = A \cdot C$, entonces $B = C$.

**Hipótesis:** $A$ invertible; $AB = AC$.

**Tesis:** $B = C$.

**Demostración:** multiplicamos a **izquierda** por $A^{-1}$ en ambos lados:

$$AB = AC$$

$$A^{-1} \cdot (AB) = A^{-1} \cdot (AC) \quad \text{(multiplicar por }A^{-1}\text{ a izquierda)}$$

$$(A^{-1} A) B = (A^{-1} A) C \quad \text{(asociativa)}$$

$$\text{Id} \cdot B = \text{Id} \cdot C \quad \text{(definición de inversa)}$$

$$B = C \quad \blacksquare$$

> **Cuidado: esto NO vale si $A$ no es invertible.** Contraejemplo (V.11.3): $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, $C = \begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix}$. Verificás que $AB = AC$ pero $B \neq C$.

### H.2 — Ejercicio V.16: $A$ invertible $\implies A^T$ invertible y $(A^T)^{-1} = (A^{-1})^T$

**Hipótesis:** $A$ invertible.

**Tesis:** $A^T$ es invertible y $(A^T)^{-1} = (A^{-1})^T$.

**Demostración:** verificamos que $(A^{-1})^T$ funciona como inversa de $A^T$, es decir, $A^T \cdot (A^{-1})^T = \text{Id}$.

$$A^T \cdot (A^{-1})^T = (A^{-1} \cdot A)^T \quad \text{(propiedad 4 de traspuesta:}(XY)^T = Y^T X^T\text{, leyendo de derecha a izquierda)}$$

$$= \text{Id}^T \quad \text{(definición de inversa: }A^{-1} A = \text{Id}\text{)}$$

$$= \text{Id} \quad \text{(la identidad es simétrica, }\text{Id}^T = \text{Id}\text{)}$$

Como $A^T \cdot (A^{-1})^T = \text{Id}$, por definición de inversa:

$$A^T \text{ es invertible y } (A^T)^{-1} = (A^{-1})^T \quad \blacksquare$$

---

## Cómo usar este banco para estudiar

| Si tenés... | Hacé esto |
|-------------|-----------|
| 30 minutos antes del parcial | Revisá las demos D.3, E.1, F.1, C.2 (las que tienen mayor probabilidad) |
| Una hora | Sumá las demos B.3 (traspuesta del producto) y G.5/G.6 (factorización) |
| Más tiempo | Hacé todas las inducciones G.1-G.4 una vez sin mirar el papel |
| Querés sentirte seguro | Reescribí cada demo desde cero solo viendo la tesis. Si podés hacerlo, dominás el módulo |

¡Suerte en el parcial! Si entendés todo lo de acá (especialmente la PARTE 7 con todos los ejercicios del práctico resueltos y este banco de demostraciones), tenés cubierto el módulo entero de matrices.
