# Matrices — Repaso completo para el parcial

Este documento es el repaso del **módulo de matrices** (clases 1 a 4) para el parcial. Cubre todo lo que entra: definiciones, tipos, operaciones, traspuesta, traza, inversa, y los tipos especiales (simétrica, antisimétrica, idempotente, nilpotente, ortogonal). Al final hay una sección dedicada a estrategia de parcial: errores comunes que el profesor mencionó explícitamente, checklist, y ejercicios tipo parcial resueltos paso a paso.

Asumí que no fuiste a clase y que no te acordás de nada. Todo está explicado desde cero.

---

## Mapa de lo que vamos a ver

| Parte | ¿Qué se aprende? | Clase |
|-------|-------------------|-------|
| 1 | Qué es una matriz y notación básica | Clase 1 |
| 2 | Tipos de matrices (cuadrada, triangular, diagonal, identidad, nula) | Clase 1 |
| 3 | Suma, producto por escalar, producto entre matrices | Clase 1 |
| 4 | Traspuesta, simétrica, antisimétrica, traza | Clase 2 |
| 5 | Matriz inversa: concepto, método directo, propiedades | Clase 3 |
| 6 | Tipos especiales: idempotente, nilpotente, ortogonal | Clases 3 y 4 |
| 7 | **Estrategia de parcial: errores comunes, checklist** | — |
| 8 | **Ejercicios tipo parcial resueltos** | — |

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

**Por qué importa esto:** En el parcial te van a pedir cosas como "encontrá $a, b, c, d$ tales que esta matriz sea igual a esta otra". Lo que hacés es plantear $a_{ij} = b_{ij}$ entrada por entrada y resolver el sistema que sale.

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

| Propiedad | Significado |
|-----------|-------------|
| Cerradura | La suma de dos matrices $m \times n$ es otra $m \times n$ |
| Conmutativa | $A + B = B + A$ |
| Asociativa | $(A + B) + C = A + B + C$ |
| Existencia de neutro | Existe la nula $\mathcal{O}$ tal que $A + \mathcal{O} = A$ |
| Existencia de opuesto | Para toda $A$ existe $-A$ tal que $A + (-A) = \mathcal{O}$ |

**Importante:** la suma **sí es conmutativa**, a diferencia del producto. Acordate de esto, porque el producto NO conmuta y se confunde fácil.

---

## Producto por un escalar

### ¿Qué dice?

Multiplicar una matriz por un número $k$ (un "escalar") significa multiplicar **cada entrada** por ese número.

### Fórmula

Si $A = ((a_{ij}))$ y $k \in \mathbb{R}$, entonces $k \cdot A = ((k \cdot a_{ij}))$.

### Ejemplo numérico

$$2 \cdot \begin{pmatrix} 1 & 2 \\ 3 & -4 \end{pmatrix} = \begin{pmatrix} 2 \cdot 1 & 2 \cdot 2 \\ 2 \cdot 3 & 2 \cdot (-4) \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ 6 & -8 \end{pmatrix}$$

### Propiedades

| Propiedad | Significado |
|-----------|-------------|
| $(\alpha \cdot \beta) \cdot A = \alpha \cdot (\beta \cdot A)$ | Asociativa de escalares |
| $(\alpha + \beta) \cdot A = \alpha A + \beta A$ | Distributiva sobre suma de escalares |
| $\alpha \cdot (A + B) = \alpha A + \alpha B$ | Distributiva sobre suma de matrices |
| $1 \cdot A = A$ | El $1$ es neutro del escalar |

---

## Producto de matrices

Esta es la operación más importante (y la que más complicada se hace al principio). Hay que entenderla bien.

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

**Traducción del símbolo:**
- $c_{ik}$ — la entrada de la fila $i$, columna $k$ del resultado
- $\sum_{j=1}^{n}$ — sumamos sobre $j$ desde $1$ hasta $n$
- $a_{ij}$ — entrada de la fila $i$ de $A$ (fija) y columna $j$ (varía)
- $b_{jk}$ — entrada de la fila $j$ de $B$ (varía) y columna $k$ (fija)

**En palabras simples:** para calcular el elemento $(i, k)$ del producto, **multiplicás la fila $i$ de $A$ por la columna $k$ de $B$, par a par, y sumás todo**.

### Cómo se hace, paso a paso

Tomamos $A \in \mathcal{M}_{3 \times 2}$ y $B \in \mathcal{M}_{2 \times 3}$. Las dimensiones del medio son ambas $2$ → conformables. Las de afuera son $3$ y $3$ → el resultado es $3 \times 3$.

$$A = \begin{pmatrix} 1 & 2 \\ 3 & -4 \\ 2 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 2 & 1 & 0 \\ 3 & 4 & 3 \end{pmatrix}$$

Calculemos:

**Entrada $(1,1)$ del resultado:** fila 1 de $A$ por columna 1 de $B$:

$$1 \cdot 2 + 2 \cdot 3 = 2 + 6 = 8$$

**Entrada $(1,2)$ del resultado:** fila 1 de $A$ por columna 2 de $B$:

$$1 \cdot 1 + 2 \cdot 4 = 1 + 8 = 9$$

**Entrada $(1,3)$ del resultado:** fila 1 de $A$ por columna 3 de $B$:

$$1 \cdot 0 + 2 \cdot 3 = 0 + 6 = 6$$

Y así para las filas 2 y 3 de $A$:

$$A \cdot B = \begin{pmatrix} 8 & 9 & 6 \\ -6 & -13 & -12 \\ 7 & 6 & 3 \end{pmatrix}$$

Resultado: $3 \times 3$, como predijo la regla de dimensiones.

### Propiedades del producto

| Propiedad | Significado |
|-----------|-------------|
| Asociativa | $(A \cdot B) \cdot C = A \cdot (B \cdot C)$ |
| Distributiva por izquierda | $A \cdot (B + C) = A \cdot B + A \cdot C$ |
| Distributiva por derecha | $(A + B) \cdot C = A \cdot C + B \cdot C$ |
| Existencia de neutro | $A \cdot \text{Id} = \text{Id} \cdot A = A$ |
| Escalar entre factores | $k \cdot (A \cdot B) = (k \cdot A) \cdot B = A \cdot (k \cdot B)$ |

### LO MÁS IMPORTANTE: el producto NO es conmutativo

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

## Producto por vectores canónicos (un truco que cae en parcial)

Los **vectores canónicos** son los vectores columna que tienen un solo $1$ y el resto ceros:

$$\vec{v}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{v}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

Si $A$ es $3 \times 3$ genérica:

$$A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$$

entonces:

$$A \cdot \vec{v}_1 = \begin{pmatrix} a_{11} \\ a_{21} \\ a_{31} \end{pmatrix}, \quad A \cdot \vec{v}_2 = \begin{pmatrix} a_{12} \\ a_{22} \\ a_{32} \end{pmatrix}, \quad A \cdot \vec{v}_3 = \begin{pmatrix} a_{13} \\ a_{23} \\ a_{33} \end{pmatrix}$$

**La conclusión que se pide en el parcial:** multiplicar una matriz por el vector canónico $j$-ésimo **extrae la columna $j$ de la matriz**. Es como apuntar con una flecha a una columna específica.

Este resultado es útil para demostrar otros teoremas más adelante.

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

### Las 4 propiedades de la traspuesta (tienen que estar memorizadas)

| # | Propiedad | Comentario |
|---|-----------|-----------|
| 1 | $(A^T)^T = A$ | Trasponer dos veces te devuelve a la original |
| 2 | $(A + B)^T = A^T + B^T$ | La traspuesta de la suma es la suma de las traspuestas |
| 3 | $(\alpha \cdot A)^T = \alpha \cdot A^T$ | Los escalares no se afectan |
| 4 | $(A \cdot B)^T = B^T \cdot A^T$ | **EL ORDEN SE INVIERTE** |

### Demostración de la propiedad 2 (cae en parcial)

Tesis: $(A + B)^T = A^T + B^T$.

$$[A + B]^T = [((a_{ij})) + ((b_{ij}))]^T \quad \text{(definición de suma)}$$
$$= [((a_{ij} + b_{ij}))]^T \quad \text{(suma entrada por entrada)}$$
$$= ((a_{ji} + b_{ji})) \quad \text{(definición de traspuesta: cambiar }i\text{ por }j\text{)}$$
$$= ((a_{ji})) + ((b_{ji})) \quad \text{(separar la suma)}$$
$$= A^T + B^T \quad \blacksquare$$

### Demostración de la propiedad 3

$$(\alpha \cdot A)^T = ((\alpha \cdot a_{ij}))^T = ((\alpha \cdot a_{ji})) = \alpha \cdot ((a_{ji})) = \alpha \cdot A^T \quad \blacksquare$$

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

| Propiedad | Significado |
|-----------|-------------|
| 1 | La suma de dos simétricas es simétrica |
| 2 | La suma de dos antisimétricas es antisimétrica |
| 3 | $\alpha \cdot A$ es simétrica si $A$ lo es |
| 4 | $\alpha \cdot A$ es antisimétrica si $A$ lo es |

### Demostración de la propiedad 1 (cae en el ejercicio V.5 del práctico)

**Hipótesis:** $A^T = A$ y $B^T = B$.
**Tesis:** $(A + B)^T = A + B$.

$$(A + B)^T = A^T + B^T \quad \text{(propiedad 2 de la traspuesta)}$$
$$= A + B \quad \text{(por hipótesis)}$$

Es igual a sí misma trasponiéndola, así que es simétrica. $\blacksquare$

### Demostración de "$\alpha \cdot A$ simétrica si $A$ lo es"

$$(\alpha \cdot A)^T = \alpha \cdot A^T \quad \text{(propiedad 3 de la traspuesta)}$$
$$= \alpha \cdot A \quad \text{(por hipótesis)} \quad \blacksquare$$

---

## Ejercicio V.5 del práctico: $AB$ simétrica si y solo si $A$ y $B$ conmutan

Esto es muy típico de parcial. Sean $A$ y $B$ simétricas. Probar que $AB$ es simétrica **si y solo si** $A \cdot B = B \cdot A$.

### El "si y solo si" — qué hay que probar

Cuando dice "si y solo si", hay que probar **dos implicaciones**:
- **Ida:** Si $AB$ es simétrica, entonces $AB = BA$.
- **Vuelta:** Si $AB = BA$, entonces $AB$ es simétrica.

### Ida: $AB$ simétrica $\implies AB = BA$

**Hipótesis:** $A^T = A$, $B^T = B$, $(AB)^T = AB$.

$$(AB)^T = AB \quad \text{(hipótesis: }AB\text{ simétrica)}$$

Pero también:

$$(AB)^T = B^T \cdot A^T \quad \text{(propiedad 4 de la traspuesta)}$$
$$= B \cdot A \quad \text{(porque }A\text{ y }B\text{ son simétricas)}$$

Igualando: $AB = BA$. $\blacksquare$

### Vuelta: $AB = BA \implies AB$ simétrica

**Hipótesis:** $A^T = A$, $B^T = B$, $AB = BA$.

$$(AB)^T = B^T \cdot A^T \quad \text{(propiedad 4)}$$
$$= B \cdot A \quad \text{(simetría)}$$
$$= A \cdot B \quad \text{(por hipótesis)} \quad \blacksquare$$

---

## Ejercicio V.6 del práctico: descomposición simétrica/antisimétrica

**Enunciado:** Dada $A$ cualquiera $n \times n$, probar:
1. $\frac{1}{2}(A + A^T)$ es simétrica
2. $\frac{1}{2}(A - A^T)$ es antisimétrica
3. Cualquier matriz se puede escribir como **simétrica + antisimétrica**

### Parte 1

$$\left(\frac{1}{2}(A + A^T)\right)^T = \frac{1}{2}(A + A^T)^T \quad \text{(prop. 3)}$$
$$= \frac{1}{2}(A^T + (A^T)^T) \quad \text{(prop. 2)}$$
$$= \frac{1}{2}(A^T + A) \quad \text{(prop. 1: }(A^T)^T = A\text{)}$$
$$= \frac{1}{2}(A + A^T) \quad \text{(suma conmuta)}$$

Igual a sí misma → simétrica. $\blacksquare$

### Parte 2

$$\left(\frac{1}{2}(A - A^T)\right)^T = \frac{1}{2}(A^T - A) = -\frac{1}{2}(A - A^T)$$

Igual a su opuesta → antisimétrica. $\blacksquare$

### Parte 3

$$\frac{1}{2}(A + A^T) + \frac{1}{2}(A - A^T) = \frac{1}{2}A + \frac{1}{2}A^T + \frac{1}{2}A - \frac{1}{2}A^T = A \quad \blacksquare$$

**Conclusión:** cualquier matriz cuadrada se puede partir en una parte simétrica y una antisimétrica. La simétrica es $\frac{1}{2}(A + A^T)$ y la antisimétrica es $\frac{1}{2}(A - A^T)$.

---

## Traza de una matriz

### Definición

La **traza** de una matriz cuadrada $A$ es la **suma de los elementos de la diagonal principal**:

$$tr(A) = \sum_{i=1}^{n} a_{ii} = a_{11} + a_{22} + \cdots + a_{nn}$$

**Requisito:** la matriz tiene que ser **cuadrada**.

### Ejemplo

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 3 & -4 & 2 \\ 2 & 1 & 10 \end{pmatrix} \implies tr(A) = 1 + (-4) + 10 = 7$$

### Las 4 propiedades de la traza (memorizar)

| # | Propiedad | Comentario |
|---|-----------|-----------|
| 1 | $tr(A + B) = tr(A) + tr(B)$ | La traza distribuye sobre la suma |
| 2 | $tr(\alpha \cdot A) = \alpha \cdot tr(A)$ | Los escalares salen afuera |
| 3 | $tr(A^T) = tr(A)$ | La traspuesta no cambia la diagonal |
| 4 | $tr(A \cdot B) = tr(B \cdot A)$ | **¡Aunque $AB \neq BA$, sus trazas coinciden!** |

> "A por B es una matriz, B por A es otra, pero sumo las diagonales principales y me da lo mismo. Es algo bastante curioso"

### Por qué la propiedad 4 es importante

Es una excepción notable. Aunque el producto **no conmuta**, la **traza del producto sí**. Esta propiedad permite probar cosas que de otro modo no se podrían.

### Aplicación clásica: NO existen $A, B$ tales que $AB - BA = \text{Id}$

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
- **No todas las matrices cuadradas son invertibles.** Hay matrices cuadradas sin inversa (por ejemplo, la nula, o cualquier matriz con dos filas iguales).
- La inversa, **cuando existe, es única**.
- Se requiere que $AB = BA = \text{Id}$. Es decir, **multiplicar en cualquier orden** te da la identidad. Esto es notable porque en general las matrices no conmutan; pero la matriz y su inversa **sí conmutan entre sí**.

> "Si vos tenés algo y algo a la menos uno, ese producto te da la identidad"

### Por qué se llama "inversa"

Por analogía con los números: el inverso de $5$ es $\frac{1}{5}$, y $5 \cdot \frac{1}{5} = 1$. Acá: $A \cdot A^{-1} = \text{Id}$. La identidad hace el papel del $1$.

**ATENCIÓN:** $A^{-1}$ **no es** "$\frac{1}{A}$". La división de matrices **no existe**. Solo se puede multiplicar por la inversa.

> "Acuérdense que X es una matriz, no puedo pasar X dividiendo. Lo análogo es multiplicar por la inversa"

---

## Método directo para hallar la inversa

Es el método que vimos en clase 3. Funciona siempre, pero para matrices grandes (3x3 o más) es lento. Para 2x2 es perfecto.

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

## Las 4 propiedades de la inversa (memorizar)

| # | Propiedad | Comentario |
|---|-----------|-----------|
| 1 | $(A^{-1})^{-1} = A$ | Invertir dos veces vuelve al original |
| 2 | $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$ | **EL ORDEN SE INVIERTE** |
| 3 | $(\alpha \cdot A)^{-1} = \frac{1}{\alpha} \cdot A^{-1}$, $\alpha \neq 0$ | El escalar se invierte también |
| 4 | $(A^T)^{-1} = (A^{-1})^T$ | Inversa de la traspuesta = traspuesta de la inversa |

### Demostración de la propiedad 2 (cae en parcial)

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

## Ejercicio V.8 del práctico: ecuación matricial para hallar inversa

**Dada $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{pmatrix}$, verificar que $-A^3 + 5A^2 - 7A + 3\text{Id} = \mathcal{O}$ y hallar $A^{-1}$.**

### Estrategia

Ecuaciones polinómicas en $A$ son útiles para hallar la inversa **sin método directo**. La idea es despejar $A^{-1}$ multiplicando ambos lados por $A^{-1}$.

### Paso 1: verificación

Calculamos $A^2$, $A^3$, sustituimos en la ecuación y verificamos que da la nula. (Cuentas largas pero mecánicas, las hacemos.)

$$A^2 = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 9 \end{pmatrix}, \quad A^3 = \begin{pmatrix} 1 & 3 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 27 \end{pmatrix}$$

Verificación entrada por entrada: la suma da la nula.

### Paso 2: hallar la inversa

Partimos de $-A^3 + 5A^2 - 7A + 3\text{Id} = \mathcal{O}$. Multiplicamos ambos lados por $A^{-1}$ por la derecha (o izquierda — las potencias de $A$ conmutan con $A^{-1}$):

$$-A^2 + 5A - 7\text{Id} + 3A^{-1} = \mathcal{O}$$
$$3A^{-1} = A^2 - 5A + 7\text{Id}$$
$$A^{-1} = \frac{1}{3}(A^2 - 5A + 7\text{Id})$$

Calculamos:

$$A^2 - 5A + 7\text{Id} = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 9 \end{pmatrix} - \begin{pmatrix} 5 & 5 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 15 \end{pmatrix} + \begin{pmatrix} 7 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 7 \end{pmatrix} = \begin{pmatrix} 3 & -3 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

$$A^{-1} = \frac{1}{3}\begin{pmatrix} 3 & -3 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1/3 \end{pmatrix}$$

---

## Ejercicio V.10 del práctico: $A^2 = 2A - \text{Id}$

**Dada $A = \begin{pmatrix} 5 & -4 & 2 \\ 2 & -1 & 1 \\ -4 & 4 & -1 \end{pmatrix}$. Probar que $A^2 = 2A - \text{Id}$ y deducir que $A$ es invertible.**

### Idea clave

De la ecuación, se puede **factorizar** y leer directamente la inversa:

$$A^2 = 2A - \text{Id}$$
$$A^2 - 2A + \text{Id} = \mathcal{O}$$
$$A^2 - 2A = -\text{Id}$$
$$A \cdot (A - 2\text{Id}) = -\text{Id}$$
$$A \cdot (2\text{Id} - A) = \text{Id}$$

¡Ahí está! Tenés una matriz multiplicada por otra y te da la identidad. Por la **definición de inversa**, $(2\text{Id} - A)$ es la inversa de $A$:

$$A^{-1} = 2\text{Id} - A = \begin{pmatrix} -3 & 4 & -2 \\ -2 & 3 & -1 \\ 4 & -4 & 3 \end{pmatrix}$$

> "Si probaste que esta es la inversa, estás probando las dos cosas a la misma vez"

**Traducción:** cuando probás $A \cdot B = \text{Id}$, automáticamente probás que $A$ es invertible **y** que $B = A^{-1}$. No hace falta hacer dos pruebas.

### Calcular $A^3$ usando la ecuación

$$A^3 = A \cdot A^2 = A \cdot (2A - \text{Id}) = 2A^2 - A = 2(2A - \text{Id}) - A = 3A - 2\text{Id}$$

---

## Ejercicio V.11 del práctico: ley de simplificación

### Parte 1: Si $AB = A$ y $A$ es invertible, entonces $B = \text{Id}$.

$$AB = A \quad \text{(hipótesis)}$$
$$A^{-1} \cdot (AB) = A^{-1} \cdot A \quad \text{(multiplico por }A^{-1}\text{ por la izquierda)}$$
$$(A^{-1} A) B = \text{Id}$$
$$\text{Id} \cdot B = \text{Id}$$
$$B = \text{Id} \quad \blacksquare$$

### Parte 2: Si $AB = AC$ y $A$ es invertible, entonces $B = C$.

Mismo método: multiplico por $A^{-1}$ por la izquierda y obtengo $B = C$.

### Parte 3: contraejemplo cuando $A$ NO es invertible

$$A = \begin{pmatrix} 0 & 3 \\ 0 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 2 & 1 \\ 3 & 0 \end{pmatrix}, \quad C = \begin{pmatrix} 5 & 4 \\ 3 & 0 \end{pmatrix}$$

$$AB = \begin{pmatrix} 9 & 0 \\ 0 & 0 \end{pmatrix} = AC$$

Pero $B \neq C$. La ley de simplificación **no vale** sin la hipótesis de invertibilidad. $A$ acá no es invertible (su segunda fila es nula).

---

# PARTE 6 — Tipos especiales de matrices

## Matriz idempotente

### Definición

Una matriz cuadrada $A$ es **idempotente** si $A^2 = A$.

### Ejemplos

- La identidad: $\text{Id}^2 = \text{Id}$. Es idempotente.
- La nula: $\mathcal{O}^2 = \mathcal{O}$. Es idempotente.
- $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ — verificá: $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}^2 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. Es idempotente y **no es ni la identidad ni la nula**.

### Ejercicio VI.2 del práctico: idempotente e invertible $\implies$ identidad

**Hipótesis:** $A^2 = A$ y $A$ invertible.
**Tesis:** $A = \text{Id}$.

$$A^2 = A$$
$$A^{-1} \cdot A^2 = A^{-1} \cdot A \quad \text{(multiplico por }A^{-1}\text{)}$$
$$A^{-1} \cdot A \cdot A = \text{Id}$$
$$\text{Id} \cdot A = \text{Id}$$
$$A = \text{Id} \quad \blacksquare$$

**Lectura:** la **única** matriz a la vez idempotente e invertible es la identidad. Las otras idempotentes (la nula, las "proyecciones" como la del ejemplo) no son invertibles.

---

## Matriz nilpotente

### Definición

Una matriz cuadrada $A$ es **nilpotente de grado $k$** si:
1. $A^k = \mathcal{O}$ (alguna potencia da la nula)
2. $A^{k-1} \neq \mathcal{O}$ (la potencia inmediatamente anterior NO da la nula)

Es decir, $k$ es la **primera** potencia que la anula. Si la primera potencia que la anula es $A^3$, decimos que es nilpotente de grado $3$.

### Ejemplo del práctico (V.7)

$$A = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$

Calculamos:

$$A^2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \neq \mathcal{O}$$

$$A^3 = A^2 \cdot A = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \mathcal{O}$$

Como $A^3 = \mathcal{O}$ y $A^2 \neq \mathcal{O}$, $A$ es **nilpotente de grado 3**.

### Parte 2 del ejercicio: $P^{-1} A P$ es nilpotente del mismo grado

**Idea clave:** las potencias de $P^{-1} A P$ se simplifican porque $P \cdot P^{-1} = \text{Id}$.

$$(P^{-1} A P)^2 = (P^{-1} A P)(P^{-1} A P) = P^{-1} A (P P^{-1}) A P = P^{-1} A^2 P$$

$$(P^{-1} A P)^3 = P^{-1} A^3 P = P^{-1} \mathcal{O} P = \mathcal{O}$$

Y $(P^{-1} A P)^2 = P^{-1} A^2 P \neq \mathcal{O}$ (porque $A^2 \neq \mathcal{O}$ y $P, P^{-1}$ son invertibles).

Conclusión: nilpotente de grado $3$, igual que $A$.

---

## Ejercicio VI.3 del práctico: $A^3 = \mathcal{O}$ entonces $(A + \text{Id})^{-1} = A^2 - A + \text{Id}$

Este ejercicio es muy importante. Combina nilpotencia con cálculo de inversa.

### Parte 1: verificar que $A^2 - A + \text{Id}$ es la inversa de $A + \text{Id}$

Para probarlo, multiplicamos las dos:

$$(A + \text{Id})(A^2 - A + \text{Id})$$

Distribuyendo (cuidado: las matrices no conmutan, así que respetamos el orden):

$$= A \cdot A^2 - A \cdot A + A \cdot \text{Id} + \text{Id} \cdot A^2 - \text{Id} \cdot A + \text{Id} \cdot \text{Id}$$
$$= A^3 - A^2 + A + A^2 - A + \text{Id}$$
$$= A^3 + \text{Id} \quad \text{(se cancelan }-A^2 + A^2\text{ y }+A - A\text{)}$$
$$= \mathcal{O} + \text{Id} \quad \text{(por hipótesis }A^3 = \mathcal{O}\text{)}$$
$$= \text{Id}$$

Como el producto da la identidad, una es la inversa de la otra. $\blacksquare$

### Parte 2: aplicar a una matriz $4 \times 4$ específica

Dada $B = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$, hallar $B^{-1}$.

**Paso 1:** identificar $A$ tal que $B = A + \text{Id}$:

$$A = B - \text{Id} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

**Paso 2:** verificar que $A^3 = \mathcal{O}$:

$$A^2 = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad A^3 = \mathcal{O}$$

**Paso 3:** aplicar la fórmula $B^{-1} = A^2 - A + \text{Id}$:

$$B^{-1} = \begin{pmatrix} 1 & -1 & 0 & 1 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

---

## Matriz ortogonal

### Definición

Una matriz cuadrada $A$ es **ortogonal** si y solo si $A$ es invertible y $A^{-1} = A^T$.

**Equivalentemente:** $A \cdot A^T = A^T \cdot A = \text{Id}$.

### Ejemplo del práctico (V.12)

$A = \begin{pmatrix} 4/5 & 3/5 \\ \alpha & \beta \end{pmatrix}$. Encontrar $\alpha, \beta$ para que sea ortogonal.

**Imponemos** $A^T \cdot A = \text{Id}$:

$$\begin{pmatrix} 4/5 & \alpha \\ 3/5 & \beta \end{pmatrix} \cdot \begin{pmatrix} 4/5 & 3/5 \\ \alpha & \beta \end{pmatrix} = \begin{pmatrix} 16/25 + \alpha^2 & 12/25 + \alpha\beta \\ 12/25 + \alpha\beta & 9/25 + \beta^2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

Sistema:
- $16/25 + \alpha^2 = 1 \implies \alpha^2 = 9/25 \implies \alpha = \pm 3/5$
- $9/25 + \beta^2 = 1 \implies \beta^2 = 16/25 \implies \beta = \pm 4/5$
- $12/25 + \alpha \beta = 0 \implies \alpha \beta = -12/25$

Las dos soluciones que cumplen el producto:
- $\alpha = 3/5, \beta = -4/5$
- $\alpha = -3/5, \beta = 4/5$

---

## Ejercicio V.14 del práctico: ¿$A + B$ y $AB$ son invertibles si $A, B$ lo son?

### Parte 1: $A + B$ invertible si $A, B$ lo son? **NO necesariamente.**

**Contraejemplo:** $A = \text{Id}$, $B = -\text{Id}$. Ambas son invertibles ($\text{Id}^{-1} = \text{Id}$, $(-\text{Id})^{-1} = -\text{Id}$). Pero:

$$A + B = \text{Id} + (-\text{Id}) = \mathcal{O}$$

La nula no es invertible. Entonces $A + B$ puede no ser invertible aunque $A$ y $B$ lo sean.

### Parte 2: $AB$ invertible si $A, B$ lo son? **SÍ, siempre.**

Por la propiedad 2 de la inversa: $(AB)^{-1} = B^{-1} A^{-1}$.

Como $A^{-1}$ y $B^{-1}$ existen (porque $A$ y $B$ son invertibles), $(AB)^{-1}$ también existe. $\blacksquare$

---

## Ejercicio V.15 del práctico: conmutatividad

### Parte 1: si $A$ conmuta con $B$ y $A$ conmuta con $C$, entonces $A$ conmuta con $D = \mu B + \lambda C$.

$$AD = A(\mu B + \lambda C) = \mu (AB) + \lambda (AC) = \mu (BA) + \lambda (CA) = (\mu B + \lambda C) A = DA \quad \blacksquare$$

### Parte 2: hallar todas las matrices que conmutan con $A = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix}$

Sea $B = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Imponemos $AB = BA$:

$$AB = \begin{pmatrix} a-c & b-d \\ a & b \end{pmatrix}, \quad BA = \begin{pmatrix} a+b & -a \\ c+d & -c \end{pmatrix}$$

Igualando:
- $a - c = a + b \implies c = -b$
- $b - d = -a \implies d = a + b$
- $a = c + d \implies a = -b + a + b = a$ (siempre cierto)
- $b = -c$ (ya lo tenemos)

Conclusión: $B = \begin{pmatrix} a & b \\ -b & a+b \end{pmatrix}$ para cualesquiera $a, b \in \mathbb{R}$.

**Verificación:** la propia $A$ conmuta (con $a=1, b=-1$). $\text{Id}$ conmuta (con $a=1, b=0$).

---

## Ejercicio V.16 del práctico: VERDADERO o FALSO

### V/F 1: $(A + B)^2 = A^2 + 2AB + B^2$? **FALSO en general.**

**Por qué falla.** Desarrollando con cuidado:

$$(A + B)^2 = (A+B)(A+B) = A^2 + AB + BA + B^2$$

Solo es igual a $A^2 + 2AB + B^2$ si $AB = BA$, es decir, **si conmutan**. En general no conmutan, así que es falso.

**Contraejemplo:**

$$A = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$

$(A + B)^2 = \begin{pmatrix} 2 & 1 \\ 2 & 0 \end{pmatrix}^2 = \begin{pmatrix} 6 & 2 \\ 4 & 2 \end{pmatrix}$

$A^2 + 2AB + B^2 = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} + 2\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} + \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 4 & 3 \end{pmatrix}$

No coinciden. Es falso.

### V/F 2: $A, B$ simétricas $\implies AB$ simétrica? **FALSO en general.**

**Por qué falla.** $(AB)^T = B^T A^T = BA$. Para que $AB$ sea simétrica, necesitamos $AB = BA$, es decir, **conmuten**. En general no conmutan.

**Contraejemplo:**

$$A = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$$

Ambas simétricas. $AB = \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}$, que NO es simétrica.

### V/F 3: $A$ invertible $\implies A^T$ invertible y $(A^T)^{-1} = (A^{-1})^T$? **VERDADERO.**

**Demostración:** queremos verificar que $(A^{-1})^T$ es la inversa de $A^T$. Multiplicamos:

$$A^T \cdot (A^{-1})^T = (A^{-1} \cdot A)^T \quad \text{(propiedad 4 de la traspuesta, con orden invertido)}$$
$$= \text{Id}^T \quad \text{(definición de inversa)}$$
$$= \text{Id}$$

Análogamente $(A^{-1})^T \cdot A^T = \text{Id}$. Por lo tanto $(A^{-1})^T$ es la inversa de $A^T$. $\blacksquare$

---

# PARTE 7 — Estrategia de parcial: errores comunes y checklist

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
| 9 | Aplicar Sarrus o regla a matrices grandes | (cuando aparezcan determinantes) | Sarrus solo $3 \times 3$. |
| 10 | Confundir simétrica con antisimétrica | En ejercicios V/F | Simétrica: $A^T = A$. Antisimétrica: $A^T = -A$. La antisim tiene **diagonal nula**. |

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

## Patrón de demostraciones que aparecen en parcial

El profesor estructura las demostraciones siempre igual. Si en parcial te piden una demostración, segui este esquema:

1. **Escribir la hipótesis** explícitamente (lo que te dan)
2. **Escribir la tesis** (lo que tenés que probar)
3. **Justificar cada paso** (qué propiedad usaste, qué hipótesis aplicaste)
4. **Cerrar con QED** (escribir "queda demostrado" o el símbolo $\blacksquare$ al final)

Ejemplo del esqueleto:

> **Hipótesis:** $A^T = A$, $B^T = B$, $AB = BA$.
> **Tesis:** $AB$ es simétrica.
>
> $(AB)^T = B^T A^T$ — *propiedad 4 de la traspuesta*
> $= BA$ — *hipótesis: $A, B$ simétricas*
> $= AB$ — *hipótesis: conmutan* $\blacksquare$

---

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

# PARTE 8 — Ejercicios tipo parcial

Estos son los patrones más probables que aparecen en parcial. Resueltos paso a paso.

## Tipo 1: cálculo de productos y conformabilidad

**Enunciado:** Dadas $A \in \mathcal{M}_{2 \times 3}$, $B \in \mathcal{M}_{3 \times 3}$, $C \in \mathcal{M}_{3 \times 2}$. ¿Cuáles productos son posibles? ¿Qué dimensiones tienen los resultados?

**Estrategia:** chequear conformabilidad (columnas del primero = filas del segundo).

| Producto | Dimensiones | ¿Conforma? | Resultado |
|----------|-------------|-----------|-----------|
| $A \cdot B$ | $2 \times \mathbf{3}$ por $\mathbf{3} \times 3$ | Sí | $2 \times 3$ |
| $A \cdot C$ | $2 \times \mathbf{3}$ por $\mathbf{3} \times 2$ | Sí | $2 \times 2$ |
| $C \cdot A$ | $3 \times \mathbf{2}$ por $\mathbf{2} \times 3$ | Sí | $3 \times 3$ |
| $B \cdot C$ | $3 \times \mathbf{3}$ por $\mathbf{3} \times 2$ | Sí | $3 \times 2$ |
| $B \cdot A$ | $3 \times \mathbf{3}$ por $\mathbf{2} \times 3$ | $3 \neq 2$ | NO se puede |
| $C \cdot B$ | $3 \times \mathbf{2}$ por $\mathbf{3} \times 3$ | $2 \neq 3$ | NO se puede |

---

## Tipo 2: despejar $X$ en una ecuación matricial

**Enunciado:** $A$ invertible. Despejar $X$ de la ecuación $A \cdot X \cdot B + X = C$, suponiendo que todo está bien definido y que $(\text{cosas})^{-1}$ existen.

**Solución:**

$$A X B + X = C$$
$$A X B + \text{Id} \cdot X = C \quad \text{(escribo } X = \text{Id} \cdot X \text{ para factorizar)}$$

Acá no se puede factorizar fácil porque $X$ aparece multiplicada por cosas distintas en cada término. Una estrategia distinta: factorizar por la izquierda. Pero $X$ aparece a la derecha de $A$ en un término y "sola" en el otro. Probemos con un planteo distinto.

Reorganizamos: $A X B = C - X$. Esto sigue teniendo $X$ a ambos lados.

**Caso más simple:** si la ecuación fuera $A \cdot X = C$, sería $X = A^{-1} C$. Si fuera $X \cdot A = C$, sería $X = C A^{-1}$.

**Lección:** identificá si $X$ aparece a la izquierda o a la derecha, y multiplicá por la inversa correspondiente del **mismo lado**.

---

## Tipo 3: V/F con demostración o contraejemplo

**Enunciado:** ¿Es cierto que si $A^2 = A^3$, entonces $A = \text{Id}$? Justificar con prueba o contraejemplo.

**Solución:** la afirmación es **FALSA**.

**Contraejemplo:** $A = \mathcal{O}$. Cumple $A^2 = \mathcal{O} = A^3$, pero $A \neq \text{Id}$.

Otro: $A = \text{Id}$ también cumple ($\text{Id}^2 = \text{Id}^3$). Pero la afirmación dice "$A = \text{Id}$ siempre", y la nula es contraejemplo.

**¿Cuándo SÍ se cumple?** Si $A$ es invertible, entonces multiplicando por $A^{-2}$ ambos lados: $\text{Id} = A$, así que sí.

**Lección de parcial:** los contraejemplos típicos son la **nula** ($\mathcal{O}$) y la **identidad** ($\text{Id}$). Probalos siempre.

---

## Tipo 4: matriz idempotente y demostración

**Enunciado:** Sea $A$ idempotente. Probar que $(A + \text{Id})^3 = \text{Id} + 7A$.

**Solución:**

$$(A + \text{Id})^3 = (A + \text{Id})(A + \text{Id})(A + \text{Id})$$

Calculamos $(A + \text{Id})^2$ primero:

$$(A + \text{Id})^2 = A^2 + A \cdot \text{Id} + \text{Id} \cdot A + \text{Id}^2 = A^2 + 2A + \text{Id}$$

Como $A$ es idempotente, $A^2 = A$:

$$(A + \text{Id})^2 = A + 2A + \text{Id} = 3A + \text{Id}$$

Ahora multiplicamos otra vez por $(A + \text{Id})$:

$$(A + \text{Id})^3 = (3A + \text{Id})(A + \text{Id})$$
$$= 3A^2 + 3A + A + \text{Id}$$
$$= 3A + 3A + A + \text{Id} \quad (A^2 = A)$$
$$= 7A + \text{Id} \quad \blacksquare$$

---

## Tipo 5: ecuación con $A^k$ y conclusión sobre invertibilidad

**Enunciado:** Sea $A$ tal que $A^3 - A = \text{Id}$. Probar que $A$ es invertible y hallar $A^{-1}$.

**Solución:**

$$A^3 - A = \text{Id}$$
$$A(A^2 - \text{Id}) = \text{Id}$$

¡Listo! Tenés $A$ multiplicada por $(A^2 - \text{Id})$ y da la identidad. Por la **definición de inversa**:

$$A^{-1} = A^2 - \text{Id}$$

Y $A$ es invertible porque encontramos su inversa explícitamente. $\blacksquare$

---

## Tipo 6: usar la traza para probar imposibilidad

**Enunciado:** Probar que no existen $A, B$ matrices $n \times n$ tales que $AB - BA = \text{Id}_n$.

**Solución:** por **el absurdo**, suponemos que existen.

Tomamos traza:

$$tr(AB - BA) = tr(\text{Id})$$

Lado izquierdo: $tr(AB) - tr(BA) = 0$ por propiedad 4 de la traza ($tr(AB) = tr(BA)$).

Lado derecho: $tr(\text{Id}_n) = n$.

Conclusión: $0 = n$, absurdo. Por lo tanto no pueden existir tales $A, B$. $\blacksquare$

---

## Tipo 7: hallar parámetros para una matriz especial

**Enunciado:** Hallar $x, y$ para que $P^{-1} A P = \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix}$, donde $A = \begin{pmatrix} 1 & 2 \\ 5 & 4 \end{pmatrix}$ y $P = \begin{pmatrix} 2 & 1 \\ x & y \end{pmatrix}$.

**Estrategia:** multiplicar $P$ por la matriz buscada para evitar calcular $P^{-1}$:

$$P^{-1} A P = D \implies AP = PD$$

donde $D = \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix}$.

$$AP = \begin{pmatrix} 1 & 2 \\ 5 & 4 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ x & y \end{pmatrix} = \begin{pmatrix} 2 + 2x & 1 + 2y \\ 10 + 4x & 5 + 4y \end{pmatrix}$$

$$PD = \begin{pmatrix} 2 & 1 \\ x & y \end{pmatrix} \begin{pmatrix} 6 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 12 & -1 \\ 6x & -y \end{pmatrix}$$

Igualando:
- $2 + 2x = 12 \implies x = 5$
- $1 + 2y = -1 \implies y = -1$

Verificación con las otras dos entradas: $10 + 4(5) = 30 = 6(5)$ ✓; $5 + 4(-1) = 1 = -(-1)$ ✓.

---

## Tipo 8: descomposición en simétrica + antisimétrica

**Enunciado:** Descomponer $A = \begin{pmatrix} 1 & 2 \\ 4 & 3 \end{pmatrix}$ como simétrica + antisimétrica.

**Solución:** usar la fórmula del ejercicio V.6:

$$\text{Parte simétrica:} \quad S = \frac{1}{2}(A + A^T) = \frac{1}{2}\begin{pmatrix} 2 & 6 \\ 6 & 6 \end{pmatrix} = \begin{pmatrix} 1 & 3 \\ 3 & 3 \end{pmatrix}$$

$$\text{Parte antisimétrica:} \quad K = \frac{1}{2}(A - A^T) = \frac{1}{2}\begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$

Verificación: $S + K = \begin{pmatrix} 1 & 2 \\ 4 & 3 \end{pmatrix} = A$ ✓.

$S$ es simétrica ($S^T = S$). $K$ es antisimétrica ($K^T = -K$, diagonal nula).

---

# Resumen final — lo absolutamente imprescindible

Si tenés que repasar 30 minutos antes del parcial, mirá esto.

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

1. $A^k - p(A) = \text{Id} \implies A^{-1} = (\text{algo en función de }A)$ — método para hallar inversa por ecuaciones matriciales
2. $A$ idempotente e invertible → $A = \text{Id}$ (multiplicando $A^2 = A$ por $A^{-1}$)

## La cosa que se demuestra por el absurdo

- **No existen** $A, B$ con $AB - BA = \text{Id}_n$ (por traza)

---

> "Vamos a ver más adelante" — *el profesor, en cada clase, sobre lo que no entra todavía*

> "En el parcial..." — *referencia constante; tomalo como aviso*

¡Suerte en el parcial! Si entendés todo lo de acá, tenés cubierto el módulo entero de matrices.
