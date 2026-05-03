# Determinantes — Material para el PARCIAL

Este documento cubre todo lo de **determinantes** que entra en parcial: qué son, cómo se calculan, las 9 propiedades con demostración, los dos teoremas (que cierran el "si y solo si" entre invertibilidad y determinante distinto de cero), la fórmula de la inversa por cofactores, y los resultados de matrices nilpotentes, antisimétricas y ortogonales. Al final está todo el práctico (V.1 a V.12) resuelto. Todo explicado asumiendo que no sabés nada — partimos de cero.

---

## Mapa de lo que vamos a ver

| Sección | Tema | ¿Qué se aprende? |
|---------|------|------------------|
| 1 | Definición y cómo calcular | Determinante 1×1, 2×2, 3×3 (Sarrus), n×n (cofactores) |
| 2 | Las 9 propiedades | Cada una con ejemplo + demostración |
| 3 | El "si y solo si" | Teorema 1 + Teorema 2: invertible ⇔ det ≠ 0 |
| 4 | Inversa por cofactores | Cómo calcular A⁻¹ usando determinantes |
| 5 | Resultados clásicos | Nilpotente, antisimétrica impar, ortogonal, triangular |
| 6 | Errores típicos | Las trampas que aparecen en parcial |
| 7 | Checklist y referencia | Antes de calcular cualquier determinante |
| 8 | Ejemplos modelo del práctico | IV.1, IV.2, IV.3 — pre-resueltos |
| 9 | Práctico resuelto (V.1 a V.12) | Cada ejercicio del práctico oficial, paso a paso |
| 10 | Estrategia para el parcial | Qué dominar, qué practicar |

---

# 1. ¿Qué es un determinante? Y cómo se calcula

## 1.1. La idea en una oración

El determinante es **un número** que le asignamos a una matriz cuadrada y que nos dice si esa matriz es invertible o no.

### La analogía

Pensá en el determinante como un **semáforo** de la matriz:
- Si el determinante es **distinto de cero** → luz verde: la matriz tiene inversa, el sistema de ecuaciones tiene solución única, todo funciona.
- Si el determinante es **igual a cero** → luz roja: la matriz NO tiene inversa, algo anda mal.

> "Es un número característico de una matriz, siempre hablando de matrices cuadradas, que entre otras cosas nos va a indicar si la matriz es invertible o no"

**Traducción:** El determinante toma una **matriz cuadrada** (tiene que ser cuadrada, sí o sí) y devuelve **un número**. Ese número nos dice cosas fundamentales sobre la matriz.

### ¿Para qué sirve?

Hasta ahora, para saber si una matriz tenía inversa, teníamos que hacer toda la cuenta del método directo (plantear el sistema de ecuaciones, resolverlo, y ver si tiene solución). El determinante nos da una respuesta **mucho más rápida**: si el número da distinto de cero, la matriz es invertible. Punto.

## 1.2. Notación

Hay dos formas de escribir "el determinante de la matriz $A$":

| Notación | Cómo se lee |
|----------|-------------|
| $\|A\|$ | "determinante de A" (parece valor absoluto, pero NO lo es) |
| $\det(A)$ | "determinante de A" (más explícito) |

> "Esto acá que pareciera el valor absoluto de A significa determinante de A"

**Traducción:** Cuidado con las barras verticales. Cuando rodean una **matriz**, significan "determinante". No es valor absoluto. De hecho, el determinante **puede ser negativo** (el valor absoluto no puede).

## 1.3. Requisito fundamental

Solo se puede calcular el determinante de **matrices cuadradas** ($n \times n$). Si la matriz tiene distinta cantidad de filas que de columnas (por ejemplo $3 \times 4$), no existe su determinante.

## 1.4. ¿De dónde sale la fórmula?

Cuando tenés un sistema de 2 ecuaciones con 2 incógnitas:

$$a \cdot x + b \cdot y = e$$
$$c \cdot x + d \cdot y = f$$

Si lo resolvés despejando (sustitución o igualación), la solución te queda:

$$x = \frac{e \cdot d - b \cdot f}{a \cdot d - b \cdot c}, \quad y = \frac{a \cdot f - c \cdot e}{a \cdot d - b \cdot c}$$

Mirá el **denominador**: $a \cdot d - b \cdot c$. Si ese número es $0$, estás dividiendo por cero y el sistema no tiene solución única. Si es $\neq 0$, el sistema sí tiene solución única.

Ese denominador es exactamente el **determinante** de la matriz de coeficientes $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$. El determinante no es una fórmula arbitraria — es el número que aparece naturalmente cuando intentás resolver un sistema de ecuaciones.

## 1.5. La regla general para calcular un determinante

La regla es: **elegir un número de cada fila, sin repetir columna**, multiplicarlos entre sí, y sumar todos esos productos con cierto signo ($+$ o $-$).

En una $1 \times 1$: hay **1 sola manera** de elegir (el único número). Así que $\det(A) = a_{11}$.

En una $2 \times 2$: hay **2 maneras**, y las dos resultan ser las dos diagonales:

```
| a  b |
| c  d |

Manera 1: fila 1→col 1 (=a), fila 2→col 2 (=d) → a·d     signo +
Manera 2: fila 1→col 2 (=b), fila 2→col 1 (=c) → b·c     signo -

det = a·d - b·c
```

**Ejemplo numérico $2 \times 2$:**

$$A = \begin{pmatrix} 2 & 4 \\ 6 & 1 \end{pmatrix}$$

Manera 1: $2 \cdot 1 = 2$ (con $+$). Manera 2: $4 \cdot 6 = 24$ (con $-$).

$$\det(A) = 2 - 24 = -22$$

Como es $\neq 0$, la matriz es invertible.

## 1.6. Matrices $3 \times 3$ — las 6 combinaciones y la regla de Sarrus

En $3 \times 3$ la regla general da **6 combinaciones**. Solo 2 de las 6 parecen diagonales; las otras 4 no forman ninguna línea visual. La fórmula es:

$$\det(A) = a_{11}a_{22}a_{33} + a_{21}a_{32}a_{13} + a_{31}a_{12}a_{23} - a_{31}a_{22}a_{13} - a_{11}a_{32}a_{23} - a_{21}a_{12}a_{33}$$

> "Sinceramente no me la sé de memoria"

**Traducción:** Ni el profesor se la sabe de memoria. **Sarrus** resuelve todo.

### Regla de Sarrus (solo para $3 \times 3$)

> "Tengan presente que la regla de Sarrus solo para matrices 3x3. He visto varias veces en parciales que aplican la regla de Sarrus para matrices 4x4 o otras dimensiones, no sea 3x3, y está mal"

**Traducción:** Sarrus **SOLAMENTE funciona para matrices $3 \times 3$**. Si la matriz es $4 \times 4$ o más grande, Sarrus no sirve. Esto aparece como error en parciales.

#### Cómo funciona Sarrus

Es un truco visual que convierte las 6 combinaciones de la regla en 6 diagonales que podés ver y recorrer con el dedo.

**Paso 1:** Escribí la matriz. Abajo de ella, copiá la fila 1 y la fila 2:

```
| a₁₁  a₁₂  a₁₃ |    fila 1
| a₂₁  a₂₂  a₂₃ |    fila 2
| a₃₁  a₃₂  a₃₃ |    fila 3
  a₁₁  a₁₂  a₁₃      ← copia de fila 1
  a₂₁  a₂₂  a₂₃      ← copia de fila 2
```

Ahora tenés una grilla de 5 filas × 3 columnas. En esta grilla aparecen **6 diagonales de largo 3**: 3 van hacia abajo-derecha (↘) y 3 van hacia abajo-izquierda (↙).

**Paso 2:** Las 3 diagonales ↘ arrancan desde la **columna 1**, una en cada fila (filas 1, 2 y 3). Van con $+$.

**Paso 3:** Las 3 diagonales ↙ arrancan desde la **columna 3**, una en cada fila (filas 1, 2 y 3). Van con $-$.

**Paso 4:** Restá: (suma de las 3 positivas) − (suma de las 3 negativas). Eso es el determinante.

#### Ejemplo numérico completo con Sarrus

$$A = \begin{pmatrix} 1 & 0 & 2 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$$

**Paso 1:** Copiamos filas 1 y 2 abajo:

```
| 1  0  2 |
| 1  0  1 |
| 0  1  1 |
  1  0  2
  1  0  1
```

**Paso 2 — diagonales positivas (↘) desde columna 1:**
- Desde fila 1: $1 \cdot 0 \cdot 1 = 0$
- Desde fila 2: $1 \cdot 1 \cdot 2 = 2$
- Desde fila 3: $0 \cdot 0 \cdot 1 = 0$

Suma: $0 + 2 + 0 = 2$

**Paso 3 — diagonales negativas (↙) desde columna 3:**
- Desde fila 1: $2 \cdot 0 \cdot 0 = 0$
- Desde fila 2: $1 \cdot 1 \cdot 1 = 1$
- Desde fila 3: $1 \cdot 0 \cdot 1 = 0$

Suma: $0 + 1 + 0 = 1$

**Paso 4:** $\det(A) = 2 - 1 = 1$

## 1.7. Método recursivo (para matrices de cualquier tamaño)

> "Precisamos ahora un método que nos sirva para matrices n por n"

**Traducción:** Sarrus solo funciona para $3 \times 3$. Para $4 \times 4$ o más necesitamos otro método.

### La idea en una oración

Convertir un determinante grande en varios determinantes más chicos. Un determinante de $4 \times 4$ se convierte en varios de $3 \times 3$ (que ya sabés hacer con Sarrus). Uno de $3 \times 3$ se convierte en varios de $2 \times 2$ (que son triviales).

### Paso 1 — Aprender a "borrar" una fila y una columna (matriz adjunta)

> "La matriz adjunta del elemento ij de A surge de quitarle a la matriz A la fila i y la columna j"

Antes de ver el método completo, necesitás saber hacer una sola cosa: dada una matriz, **tachar una fila entera y una columna entera**, y quedarte con lo que sobra. Lo que sobra se llama **matriz adjunta del elemento $(i,j)$**, y se nota $\text{Adj}_{ij}(A)$. Otros libros la llaman **menor** del elemento $(i,j)$.

**Ejemplo:** Partimos de esta matriz $3 \times 3$:

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$$

Vamos a borrar la fila 2 y la columna 2 (donde está el $5$):

```
Antes:                  Tachamos fila 2 y col 2:       Queda:

| 1  2  3 |             | 1  ✕  3 |                    | 1  3 |
| 4  5  6 |      →      | ✕  ✕  ✕ |              →     | 7  9 |
| 7  8  9 |             | 7  ✕  9 |
```

$\text{Adj}_{22}(A) = \begin{pmatrix} 1 & 3 \\ 7 & 9 \end{pmatrix}$. Es una $2 \times 2$ (una dimensión menos que la original).

### Paso 2 — La fórmula del desarrollo recursivo

Dada una matriz $n \times n$, $A = ((a_{ij}))$, el determinante es:

$$\det(A) = \sum_{j=1}^{n} a_{ij} \cdot (-1)^{i+j} \cdot \det(\text{Adj}_{ij}(A))$$

para cualquier fila $i$ que vos elijas.

**Lo que dice la fórmula en palabras:** Elegís una fila. Para cada número de esa fila, hacés tres cosas: lo multiplicás por el signo $(-1)^{i+j}$ (el "tablero de ajedrez"), y por el determinante de la adjunta (matriz más chica). Sumás todo.

**Observación importante:** la fórmula es **igual de válida desarrollando por columnas** que por filas. Da exactamente lo mismo.

### El "tablero de ajedrez" de signos

El factor $(-1)^{i+j}$ alterna entre $+$ y $-$ siguiendo el patrón del tablero de ajedrez:

```
| +  -  +  - |
| -  +  -  + |
| +  -  +  - |
| -  +  -  + |
```

Empieza con $+$ en la esquina superior izquierda.

### Ejemplo completo paso a paso

$$A = \begin{pmatrix} 1 & 0 & 2 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$$

Queremos calcular $\det(A)$. La matriz es $3 \times 3$, así que vamos a descomponerla en determinantes de $2 \times 2$.

**Paso A — Elegir una fila.** Elegimos la **fila 1**: sus elementos son $1$, $0$, $2$. Vamos a procesar cada uno.

**Paso B — Procesar cada elemento.**

**Elemento $(1,1) = 1$:** signo $+$, adjunta $= \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$, determinante $= 0 - 1 = -1$.
Aporte: $1 \cdot (+1) \cdot (-1) = -1$.

**Elemento $(1,2) = 0$:** como es $0$, aporte $= 0$ sin hacer cuentas.

**Elemento $(1,3) = 2$:** signo $+$, adjunta $= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, determinante $= 1$.
Aporte: $2 \cdot (+1) \cdot 1 = 2$.

**Paso C — Sumar.**

$$\det(A) = (-1) + 0 + 2 = 1$$

**Verificación con Sarrus:** $(0+2+0) - (0+1+0) = 1$ ✓

### Truco: elegí la fila o columna con más ceros

> "Siempre sirve lo más fácil es desarrollar por la fila o columna que presente la mayor cantidad de ceros, así tengo que calcular la menor cantidad de matrices adjuntas"

**Traducción:** Cuando un elemento es $0$, su aporte es $0$ sin hacer cuentas. Cuantos más ceros tenga la fila o columna que elegís, menos adjuntas tenés que calcular.

En la matriz de arriba, la **columna 2** tiene dos ceros. Si desarrollamos por columna 2 en vez de fila 1, solo hay que calcular UNA adjunta:

- $(1,2)$ es $0$: aporte $0$
- $(2,2)$ es $0$: aporte $0$
- $(3,2)$ es $1$: signo $-$, adjunta $= \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}$, det $= 1 - 2 = -1$. Aporte: $1 \cdot (-1) \cdot (-1) = 1$.

$$\det(A) = 0 + 0 + 1 = 1$$

Mismo resultado, mucho menos trabajo.

### Para matrices $4 \times 4$ o más grandes

> "Si es 4x4, ahí sí, ya no le va a quedar otra que desarrollar por una fila o columna"

Mismo procedimiento: elegís fila o columna con más ceros, para cada elemento generás una adjunta de $3 \times 3$ y le calculás el determinante con Sarrus, sumás todo con los signos correctos.

---

# 2. Las 9 propiedades del determinante

Estas propiedades son **atajos**. En vez de calcular un determinante desde cero (lo cual puede llevar mucho tiempo), las propiedades te dejan manipular la matriz para simplificarla, o te dicen el resultado directamente.

Para el parcial necesitás: (a) saber cada propiedad, (b) saber cuándo usarla, y (c) **saber demostrarla** (las demos sí entran en parcial).

---

## Propiedad 1: Si hay sumas adentro de una fila, podés separar

### Enunciado

Si en alguna fila (o columna) de la matriz, cada entrada es la suma de dos cosas, podés separar el determinante en la suma de dos determinantes:

$$\det\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ b_{21}+c_{21} & b_{22}+c_{22} & \cdots & b_{2n}+c_{2n} \\ \vdots & & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix} = \det\begin{pmatrix} a_{11} & \cdots & a_{1n} \\ b_{21} & \cdots & b_{2n} \\ \vdots & & \vdots \\ a_{n1} & \cdots & a_{nn} \end{pmatrix} + \det\begin{pmatrix} a_{11} & \cdots & a_{1n} \\ c_{21} & \cdots & c_{2n} \\ \vdots & & \vdots \\ a_{n1} & \cdots & a_{nn} \end{pmatrix}$$

Las demás filas quedan iguales en ambos determinantes.

### Cuándo aparece

1. **Dentro de demostraciones:** cuando una fila fue construida sumando cosas (por ejemplo, la propiedad 7 le suma a una fila un múltiplo de otra).
2. **En ejercicios:** cuando el problema te dice que una fila es "fila 1 + 3·fila 2" o algo similar.
3. **En el práctico (V.10 parte 1):** cuando la matriz te llega con sumas explícitas en una fila.

### Ejemplo concreto

Tenés $A$ con fila 1 = $(1, 3)$ y fila 2 = $(4, 4)$. Te dicen: "sumale la fila 2 a la fila 1". Llamemos $B$ a la nueva matriz:

$$\det\begin{pmatrix} 1+4 & 3+4 \\ 4 & 4 \end{pmatrix} = \det\begin{pmatrix} 1 & 3 \\ 4 & 4 \end{pmatrix} + \det\begin{pmatrix} 4 & 4 \\ 4 & 4 \end{pmatrix}$$

El segundo determinante tiene fila 1 = fila 2 = $(4, 4)$, así que por la **propiedad 5** vale $0$. Quedó: $\det(B) = \det(A) + 0 = \det(A)$.

### Demostración

**Método directo.** Llamamos $A$, $B$ y $C$ a las tres matrices: $A$ la que tiene la suma, $B$ y $C$ las que tienen los sumandos por separado. Desarrollamos $\det(A)$ por la fila que tiene los sumandos (fila 2 en el enunciado):

$$\det(A) = \sum_{j=1}^{n} (b_{2j} + c_{2j}) \cdot (-1)^{2+j} \cdot \det(\text{Adj}_{2j}(A))$$

Como las matrices adjuntas $\text{Adj}_{2j}$ surgen de borrar la fila 2 y se obtienen iguales en $A$, $B$ y $C$ (porque al borrar la fila 2 la única fila que difería desaparece), separamos la sumatoria:

$$\det(A) = \sum_{j=1}^{n} b_{2j} \cdot (-1)^{2+j} \cdot \det(\text{Adj}_{2j}(B)) + \sum_{j=1}^{n} c_{2j} \cdot (-1)^{2+j} \cdot \det(\text{Adj}_{2j}(C))$$

$$\det(A) = \det(B) + \det(C) \quad \blacksquare$$

**Método por inducción completa.** El paso base ($n=1$ y $n=2$) es directo. El paso inductivo desarrolla por una fila que **no** sea la que tiene los sumandos, para poder aplicar la hipótesis de inducción a las adjuntas (que son $n \times n$ y heredan la fila con sumandos).

> "¿Por qué no se puede por la fila 2? Si yo desarrollo por la fila 2, al aplicar la matriz adjunta se me va esa fila 2. Se me va la fila 2, por lo tanto no puedo aplicar la hipótesis"

---

## Propiedad 2: Factor común de una fila sale multiplicando

### Enunciado

Si todas las entradas de una fila (o columna) están multiplicadas por un número $k$, podés "sacar" ese $k$ fuera del determinante:

$$\det\begin{pmatrix} a_{11} & \cdots & a_{1n} \\ k \cdot a_{21} & \cdots & k \cdot a_{2n} \\ \vdots & & \vdots \\ a_{n1} & \cdots & a_{nn} \end{pmatrix} = k \cdot \det\begin{pmatrix} a_{11} & \cdots & a_{1n} \\ a_{21} & \cdots & a_{2n} \\ \vdots & & \vdots \\ a_{n1} & \cdots & a_{nn} \end{pmatrix}$$

### Cuándo aparece

Cuando mirás una fila y ves que todos los números son múltiplos de algo (todos pares, todos múltiplos de 3, todos tienen un $(x-1)$ como factor, etc.). Sacás el factor para simplificar antes de calcular.

### Ejemplo

$$\det\begin{pmatrix} 2 & 2 \\ 4 & 8 \end{pmatrix} = 2 \cdot \det\begin{pmatrix} 1 & 1 \\ 4 & 8 \end{pmatrix}$$

Verificación: izquierda $= 16 - 8 = 8$. Derecha $= 2 \cdot (8 - 4) = 8$ ✓

### Demostración

Sean $A = ((a_{ij}))$ y $B = ((b_{ij}))$ con $b_{1j} = k \cdot a_{1j}$ y $b_{ij} = a_{ij}$ para $i \geq 2$. Desarrollamos $\det(B)$ por la primera fila:

$$\det(B) = \sum_{j=1}^{n} b_{1j} \cdot (-1)^{1+j} \cdot \det(\text{Adj}_{1j}(B))$$

Como $\text{Adj}_{1j}(B) = \text{Adj}_{1j}(A)$ (porque al borrar la fila 1, ambas matrices quedan iguales) y $b_{1j} = k \cdot a_{1j}$:

$$\det(B) = \sum_{j=1}^{n} k \cdot a_{1j} \cdot (-1)^{1+j} \cdot \det(\text{Adj}_{1j}(A)) = k \cdot \det(A) \quad \blacksquare$$

---

## Propiedad 3: Factor común de TODA la matriz sale elevado a $n$

### Enunciado

$$\det(k \cdot A) = k^n \cdot \det(A)$$

donde $n$ es la cantidad de filas (y columnas) de la matriz.

### Cuándo aparece

En ejercicios te piden calcular cosas como $\det(3A)$, $\det(-A)$, $\det((2A)^{-1})$. No te dan la matriz explícita — solo te dicen cuánto vale $\det(A)$ y te piden el determinante de la matriz multiplicada por un número.

### ¿Por qué $k^n$?

Porque multiplicar toda la matriz por $k$ significa que CADA fila queda multiplicada por $k$. Por la propiedad 2, cada vez que sacás un $k$ de una fila, el determinante queda multiplicado por $k$. Si tenés $n$ filas, sacás $k$ $n$ veces, y queda $k \cdot k \cdot \ldots = k^n$.

> "La propiedad 3 no es más que aplicar n veces la propiedad 2"

### Ejemplo

Si $A$ es $3 \times 3$ y $\det(A) = 5$, ¿cuánto vale $\det(4A)$?

$$\det(4A) = 4^3 \cdot \det(A) = 64 \cdot 5 = 320$$

### Demostración (Ejercicio II.1 del práctico — basta con aplicar P2 $n$ veces)

$$\det(k A) = \det\begin{pmatrix} k a_{11} & \cdots & k a_{1n} \\ \vdots & & \vdots \\ k a_{n1} & \cdots & k a_{nn} \end{pmatrix}$$

Aplicando **P2** a la fila 1: sale un factor $k$. Aplicando **P2** a la fila 2: sale otro factor $k$. Y así $n$ veces:

$$\det(k A) = k \cdot k \cdot \ldots \cdot k \cdot \det(A) = k^n \cdot \det(A) \quad \blacksquare$$

### Error común en parciales

| MAL | BIEN | ¿Por qué? |
|-----|------|-----------|
| $\det(4A) = 4 \cdot \det(A)$ | $\det(4A) = 4^n \cdot \det(A)$ | El $k$ sale UNA vez por cada fila, no una sola vez |

| Dimensión | $\det(kA)$ |
|-----------|-----------|
| $2 \times 2$ | $k^2 \cdot \det(A)$ |
| $3 \times 3$ | $k^3 \cdot \det(A)$ |
| $5 \times 5$ | $k^5 \cdot \det(A)$ |

---

## Propiedad 4: Determinante de un producto = producto de determinantes

### Enunciado

$$\det(A \cdot B) = \det(A) \cdot \det(B)$$

> "No significa que B por A sea lo mismo que A por B. Pero el determinante sí es el mismo"

**Traducción:** Las matrices $A \cdot B$ y $B \cdot A$ son matrices distintas (el producto no conmuta). Pero cuando les calculás el determinante, el número que sale es el mismo, porque $\det(A) \cdot \det(B)$ es una multiplicación de números reales, y esa sí conmuta.

### Cuándo aparece

Cuando ves un determinante de un producto, o cuando necesitás calcular $\det(A^3) = \det(A) \cdot \det(A) \cdot \det(A) = \det(A)^3$.

### Ejemplo

$\det(A) = 1$, $\det(B) = 2 \implies \det(A \cdot B) = 1 \cdot 2 = 2$.

**Verificación con matrices concretas:**

$$A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$$

$\det(A) = 1$, $\det(B) = 2$.

$$A \cdot B = \begin{pmatrix} 2 & 2 \\ 0 & 1 \end{pmatrix} \implies \det(A \cdot B) = 2 = 1 \cdot 2 \quad \checkmark$$

### Demostración

No se demuestra en el curso. La propiedad se enuncia y se usa.

---

## Propiedad 5: Dos filas o columnas iguales → det = 0

### Enunciado

Si una matriz tiene dos filas iguales entre sí (o dos columnas iguales entre sí), su determinante vale $0$.

> "En un parcial si ustedes ven una matriz de 7x7, capaz que un compañero se tira a hacer las cuentas y otro se da cuenta que la fila 1 es igual a la fila 5 y el determinante vale 0"

### Cuándo aparece

- **En cálculos directos:** te dan una matriz grande y esperan que MIRES antes de calcular.
- **Dentro de demostraciones:** cuando la propiedad 1 separa un determinante en dos, uno de ellos a veces tiene filas iguales.
- **En ejercicios teóricos:** "¿puede una matriz con dos columnas iguales ser invertible?" — no.
- **En el práctico (V.10 parte 1):** después de aplicar P1 y P2, una de las matrices tiene F1 = F3 → det = 0.

### Ejemplo

$$\det\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 1 & 2 & 3 \end{pmatrix} = 0$$

La fila 1 = fila 3 → $\det = 0$ sin hacer cuentas.

### Demostración (por inducción completa, fila 1 = fila 2)

**Paso base ($n=2$):** $A = \begin{pmatrix} a & b \\ a & b \end{pmatrix}$, $\det(A) = ab - ba = 0$ ✓

**Paso inductivo:** Tenemos $(n+1) \times (n+1)$ con fila 1 = fila 2. Desarrollamos por una fila que NO sea la 1 ni la 2 (por ejemplo la fila 3):

$$\det(A) = \sum_{j=1}^{n+1} a_{3j} \cdot (-1)^{3+j} \cdot \det(\text{Adj}_{3j}(A))$$

Cada $\text{Adj}_{3j}(A)$ es $n \times n$ y mantiene fila 1 = fila 2. Por hipótesis de inducción, $\det(\text{Adj}_{3j}(A)) = 0$. Entonces $\det(A) = \sum a_{3j} \cdot (-1)^{3+j} \cdot 0 = 0$. $\blacksquare$

> "Bueno, en este caso es distinta la demostración. Desarrollo por la fila 3 pero puede ser por cualquier fila que no sea la 1 y la 2"

### Aclaración

Tiene que ser **fila con fila**, o **columna con columna**. Si una fila es igual a una columna, esta propiedad no aplica.

---

## Propiedad 6: Intercambiar dos filas o columnas cambia el signo

### Enunciado

Si intercambiás dos filas (o dos columnas) de una matriz, el determinante se multiplica por $-1$:

$$\det(B) = -\det(A) \quad \text{donde } B \text{ es } A \text{ con dos filas intercambiadas}$$

### Cuándo aparece

- Cuando querés reorganizar la matriz para que quede más cómoda (por ejemplo, poner una fila con muchos ceros arriba).
- En el práctico (V.2 parte A, B, E): aplicaciones directas.

### Ejemplo

$$A = \begin{pmatrix} 3 & 2 & 4 \\ 4 & 6 & 8 \\ 1 & 1 & 6 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 1 & 6 \\ 4 & 6 & 8 \\ 3 & 2 & 4 \end{pmatrix} \text{ (intercambié F1 y F3)}$$

$\det(B) = -\det(A)$.

### Demostración (a partir de P1 y P5)

Sean $A$ y $B$ matrices que difieren solo en que $B$ tiene F1 y F2 intercambiadas. Construimos una matriz auxiliar $C$ con F1 = F2 = $F_1 + F_2$ (ambas filas son la suma):

$$C = \begin{pmatrix} F_1 + F_2 \\ F_1 + F_2 \\ \vdots \end{pmatrix}$$

Por **P5** (dos filas iguales), $\det(C) = 0$.

Aplicamos **P1** en F1 de $C$ (la suma se separa en dos determinantes):

$$\det(C) = \det\begin{pmatrix} F_1 \\ F_1 + F_2 \\ \vdots \end{pmatrix} + \det\begin{pmatrix} F_2 \\ F_1 + F_2 \\ \vdots \end{pmatrix}$$

Aplicamos **P1** otra vez en F2 de cada uno:

$$\det(C) = \det\begin{pmatrix} F_1 \\ F_1 \\ \vdots \end{pmatrix} + \det\begin{pmatrix} F_1 \\ F_2 \\ \vdots \end{pmatrix} + \det\begin{pmatrix} F_2 \\ F_1 \\ \vdots \end{pmatrix} + \det\begin{pmatrix} F_2 \\ F_2 \\ \vdots \end{pmatrix}$$

El 1° y el 4° tienen F1 = F2 → valen $0$ por P5. Quedan los del medio: el 2° es $\det(A)$, el 3° es $\det(B)$.

Como $\det(C) = 0$:

$$0 = \det(A) + \det(B) \implies \det(B) = -\det(A) \quad \blacksquare$$

---

## Propiedad 7: Sumar combinación lineal de filas NO cambia el det

### Enunciado

Si a una fila le sumás un múltiplo de otra fila (o una combinación lineal de varias), el determinante **no cambia**.

**Regla importante:** la fila que modificás NO puede estar multiplicada por un número. Solo le sumás cosas de las OTRAS filas.

> "¿Por qué? Porque si yo la multiplico por un número, el determinante queda multiplicado por ese número por la propiedad 2"

### Cuándo aparece

Es **la herramienta principal** para simplificar matrices grandes antes de calcularles el determinante. Generás ceros en una fila/columna para que el desarrollo por cofactores se simplifique.

- En el práctico (V.1 parte E): F3 ← F3 - F1 para generar ceros y desarrollar fácil.
- En el práctico (V.11): F1 ← F1 - F3 para generar ceros.
- En el práctico (V.2 parte F): C1 ← C1 - C2.

### Ejemplo (generar ceros)

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$$

Para generar ceros en la columna 1:
- $F_2 \leftarrow F_2 - 4 \cdot F_1$: nueva $F_2 = (0, -3, -6)$
- $F_3 \leftarrow F_3 - 7 \cdot F_1$: nueva $F_3 = (0, -6, -12)$

$$B = \begin{pmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ 0 & -6 & -12 \end{pmatrix}, \quad \det(B) = \det(A)$$

### Demostración (a partir de P1, P2 y P5)

Sea $B$ la matriz que resulta de sumarle a la fila $j$ de $A$ una combinación lineal de las demás filas: $\lambda_1 F_1 + \lambda_2 F_2 + \ldots + F_j + \ldots + \lambda_n F_n$.

**Paso 1 (P1):** Como la fila $j$ es una suma, separamos $\det(B)$ en $n$ determinantes (uno por cada sumando).

**Paso 2 (P2):** En cada determinante salvo uno, sacamos el $\lambda_k$ correspondiente afuera.

**Paso 3 (P5):** Cada uno de esos determinantes (salvo uno) tiene dos filas iguales (la fila $j$ ahora es una copia de otra fila $F_k$, y la fila $k$ original sigue ahí). Por P5, valen $0$.

**Paso 4:** El único determinante que sobrevive es aquel donde la fila $j$ quedó como $F_j$ original. Ese es $\det(A)$.

> "Bueno, cero más cero más determinante de A más cero más cero, nos queda que el determinante de B es igual al determinante de A"

$\blacksquare$

---

## Propiedad 8: Transponer no cambia el determinante

### Enunciado

$$\det(A) = \det(A^T)$$

### Cuándo aparece

Cuando algo te conviene más en columnas que en filas, o viceversa. También aparece en demostraciones que mezclan filas y columnas (ortogonal, antisimétrica, etc).

### Consecuencia importantísima

Como el determinante no cambia al transponer, **toda propiedad que vale para filas también vale para columnas**, y viceversa. Por eso cada propiedad dice "filas o columnas".

### Ejemplo

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad A^T = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$$

$\det(A) = 4 - 6 = -2$, $\det(A^T) = 4 - 6 = -2$ ✓

### Demostración

No se demuestra en el curso (queda como Ejercicio II.2 del práctico, por inducción). El profesor lo enuncia como propiedad y se usa.

---

## Propiedad 9: Triangular → producto de la diagonal

### ¿Qué es triangular?

Una matriz donde todos los números **debajo** de la diagonal principal son $0$ (triangular superior), o todos los que están **arriba** son $0$ (triangular inferior):

```
Triangular superior:          Triangular inferior:

| 7  3  5 |                   | 7  0  0 |
| 0  6  2 |                   | 3  6  0 |
| 0  0  1 |                   | 5  2  1 |
```

### Enunciado

Si $A$ es triangular:

$$\det(A) = a_{11} \cdot a_{22} \cdot \ldots \cdot a_{nn}$$

(producto de la diagonal).

### Cuándo aparece

- **Antes de calcular:** Siempre mirá si la matriz ya es triangular. Si lo es, multiplicá la diagonal y terminaste.
- **Combinada con P7:** Si la matriz no es triangular, podés usar P7 (sumar filas para generar ceros) hasta convertirla en triangular, y después multiplicar la diagonal.
- **Práctico V.6:** "una matriz triangular con todas las entradas de la diagonal $\neq 0$ es invertible" — porque $\det = $ producto de la diagonal $\neq 0$ → P9 + Teorema 2.

> "Si un compañero se da cuenta que es triangular superior y multiplica la diagonal principal, lo saca en 12 segundos"

### Ejemplo

$$A = \begin{pmatrix} 7 & 3 & 5 \\ 0 & 6 & 2 \\ 0 & 0 & 1 \end{pmatrix} \implies \det(A) = 7 \cdot 6 \cdot 1 = 42$$

**Caso particular — diagonal** (ceros arriba Y abajo):

$$A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 6 & 0 \\ 0 & 0 & 4 \end{pmatrix} \implies \det(A) = 2 \cdot 6 \cdot 4 = 48$$

### Consecuencia: $\det(I) = 1$

La identidad es diagonal con todos unos: $\det(I) = 1 \cdot 1 \cdot \ldots \cdot 1 = 1$. Esta consecuencia aparece en casi toda demostración.

### Demostración (triangular superior, por desarrollo por C1)

Sea $A$ triangular superior, $A = ((a_{ij}))$ con $a_{ij} = 0$ para $i > j$:

$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ 0 & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & a_{nn} \end{pmatrix}$$

Desarrollamos por la **columna 1**. Toda la C1 es $0$ excepto $a_{11}$. Solo sobrevive el primer término:

$$\det(A) = a_{11} \cdot (-1)^{1+1} \cdot \det\begin{pmatrix} a_{22} & a_{23} & \cdots & a_{2n} \\ 0 & a_{33} & \cdots & a_{3n} \\ \vdots & & & \vdots \\ 0 & 0 & \cdots & a_{nn} \end{pmatrix}$$

La submatriz también es triangular superior. Repetimos: desarrollamos por C1, sobrevive $a_{22}$, etc. Llegamos a $\det(A) = a_{11} \cdot a_{22} \cdot \ldots \cdot a_{nn}$. $\blacksquare$

> "Es clave acá ir desarrollando por la columna 1"

---

## Lo que NO es propiedad: la suma

> "El determinante de A más B, en general, es distinto del determinante de A más el determinante de B"

$$\det(A + B) \neq \det(A) + \det(B) \quad \text{(en general)}$$

**Traducción:** Es tentador pensar que así como $\det(AB) = \det(A) \cdot \det(B)$, también valdría $\det(A + B) = \det(A) + \det(B)$. Pero **no**.

### Contraejemplo (Ejercicio II.3 del práctico)

$$A = \begin{pmatrix} 1 & 3 \\ -1 & 2 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 5 \\ 1 & 1 \end{pmatrix}$$

$\det(A) = 2 + 3 = 5$, $\det(B) = 1 - 5 = -4$, $\det(A) + \det(B) = 1$.

$$A + B = \begin{pmatrix} 2 & 8 \\ 0 & 3 \end{pmatrix} \implies \det(A + B) = 6 - 0 = 6$$

$6 \neq 1$. No se cumple.

---

## Resumen de las 9 propiedades

| # | ¿Qué te deja hacer? | Regla | ¿Cuándo aparece? |
|---|---------------------|-------|-----------------|
| 1 | Separar sumas dentro de una fila | $\det$ se separa en suma de dos $\det$ | Demostraciones, ejercicios con sumas explícitas en fila |
| 2 | Sacar factor común de una fila | $k$ sale multiplicando | Cuando todos los números de una fila son múltiplos de algo |
| 3 | Sacar factor de toda la matriz | $\det(kA) = k^n \cdot \det(A)$ | Ejercicios con $\det(3A)$, $\det(-A)$, etc. |
| 4 | Separar producto de matrices | $\det(AB) = \det(A) \cdot \det(B)$ | $\det(A \cdot B)$, $\det(A^3) = \det(A)^3$ |
| 5 | Detectar det = 0 sin calcular | Dos filas iguales → $\det = 0$ | Primer chequeo, demostraciones |
| 6 | Reorganizar filas para simplificar | Intercambiar → $\det$ cambia de signo | Mover una fila cómoda arriba |
| 7 | Generar ceros para simplificar | Sumar filas a otra → $\det$ no cambia | Herramienta principal para matrices grandes |
| 8 | Pasar de filas a columnas | $\det(A) = \det(A^T)$ | Cuando una columna te conviene más que una fila |
| 9 | Atajo para triangulares | $\det = $ producto de la diagonal | Si la matriz ya es triangular, o después de usar P7 |

---

# 3. El "si y solo si": invertibilidad ↔ determinante distinto de cero

Toda la teoría de determinantes converge en un teorema central que tiene dos direcciones (una en cada teorema). Juntos forman un **si y solo si**:

> "Quédense con el si solo si. Matriz invertible, determinante distinto de cero, determinante distinto de cero, matriz invertible."

| Dirección | Enunciado | Teorema |
|-----------|-----------|---------|
| → | Si $A$ es invertible, entonces $\det(A) \neq 0$ | Teorema 1 |
| ← | Si $\det(A) \neq 0$, entonces $A$ es invertible | Teorema 2 |

**Traducción:** Ser invertible y tener determinante distinto de cero son **exactamente lo mismo**. Saber una cosa es saber la otra.

---

## Teorema 1: Invertible → det ≠ 0

### Enunciado

Si $A$ es una matriz $n \times n$ invertible, entonces:
1. $\det(A) \neq 0$
2. $\det(A^{-1}) = \dfrac{1}{\det(A)}$

### ¿Por qué importa?

Porque nos da un **criterio rápido**. Si calculamos el determinante y nos da $0$, sabemos que la matriz NO es invertible, sin tener que intentar calcular la inversa.

### Demostración

> "Por la definición de inversa, si A es invertible, significa que existe una matriz A a la menos 1, tal que A por A a la menos 1 me da la identidad"

**Paso 1:** Si $A$ es invertible, existe $A^{-1}$ tal que $A \cdot A^{-1} = I$.

**Paso 2:** Tomamos determinante de ambos lados: $\det(A \cdot A^{-1}) = \det(I)$

**Paso 3:** Por **P4**: $\det(A) \cdot \det(A^{-1}) = \det(I)$

**Paso 4:** Por **P9** (la identidad es diagonal con unos): $\det(I) = 1$. Entonces:

$$\det(A) \cdot \det(A^{-1}) = 1$$

**Paso 5:** Si dos números multiplicados dan $1$, ninguno puede ser $0$ (porque $0$ por cualquier cosa da $0$). Entonces:

$$\det(A) \neq 0 \quad \blacksquare$$

**Paso 6:** Despejando: $\det(A^{-1}) = \dfrac{1}{\det(A)}$ $\blacksquare$

**Analogía:** Es exactamente como con números: si $a \cdot b = 1$, entonces ni $a$ ni $b$ pueden ser cero, y $b = \frac{1}{a}$.

---

## Teorema 2: det ≠ 0 → invertible

### Enunciado

Si $A$ es una matriz $n \times n$ con $\det(A) \neq 0$, entonces $A$ es invertible y:

$$A^{-1} = \frac{1}{\det(A)} \cdot \left[\text{Cof}(A)\right]^T$$

donde $\text{Cof}(A)$ es la **matriz de cofactores** (que vemos en la sección 4).

### ¿Por qué importa?

Cierra el "si y solo si". Y además te da una **fórmula explícita** para calcular la inversa, que es alternativa al método directo.

### Demostración

No se demuestra en el curso. La fórmula se enuncia y se usa.

---

# 4. Calcular la inversa por cofactores

> "Vamos a ver un ejemplo igual para bajar la tierra a esto"

## 4.1. Cofactor de una posición

El **cofactor** de la posición $(i,j)$ es:

$$C_{ij} = (-1)^{i+j} \cdot \det(\text{Adj}_{ij}(A))$$

En palabras: el signo del tablero, multiplicado por el determinante de la adjunta (lo que queda al borrar fila $i$ y columna $j$).

Es exactamente lo que hacías en el desarrollo recursivo, pero ahora tiene nombre.

## 4.2. Matriz de cofactores

La matriz de cofactores $\text{Cof}(A)$ tiene la misma forma que $A$, pero cada entrada es el cofactor correspondiente:

$$\text{Cof}(A) = \begin{pmatrix} C_{11} & C_{12} & \cdots & C_{1n} \\ C_{21} & C_{22} & \cdots & C_{2n} \\ \vdots & & & \vdots \\ C_{n1} & C_{n2} & \cdots & C_{nn} \end{pmatrix}$$

## 4.3. Fórmula final

$$A^{-1} = \frac{1}{\det(A)} \cdot \left[\text{Cof}(A)\right]^T$$

Es decir: armás la matriz de cofactores, la transponés, y dividís cada entrada por $\det(A)$.

## 4.4. Ejemplo completo (Ejercicio III.1 del práctico)

$$A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 2 & 4 \\ 1 & 3 & -3 \end{pmatrix}$$

### Paso 1: Calcular $\det(A)$ con Sarrus

Diagonales positivas: $1 \cdot 2 \cdot (-3) + 2 \cdot 4 \cdot 1 + (-1) \cdot 2 \cdot 3 = -6 + 8 - 6 = -4$

Diagonales negativas: $(-1) \cdot 2 \cdot 1 + 1 \cdot 4 \cdot 3 + 2 \cdot 2 \cdot (-3) = -2 + 12 - 12 = -2$

$$\det(A) = -4 - (-2) = -2$$

Como $\det(A) = -2 \neq 0$, la matriz es invertible.

### Paso 2: Calcular los 9 cofactores

Tablero de signos para $3 \times 3$:

```
| +  -  + |
| -  +  - |
| +  -  + |
```

| Posición | Signo | Adjunta (borrar fila $i$, col $j$) | $\det$ adjunta | Cofactor |
|----------|-------|------------------------------------|----------------|----------|
| $(1,1)$ | $+$ | $\begin{pmatrix} 2 & 4 \\ 3 & -3 \end{pmatrix}$ | $-6 - 12 = -18$ | $C_{11} = -18$ |
| $(1,2)$ | $-$ | $\begin{pmatrix} 2 & 4 \\ 1 & -3 \end{pmatrix}$ | $-6 - 4 = -10$ | $C_{12} = 10$ |
| $(1,3)$ | $+$ | $\begin{pmatrix} 2 & 2 \\ 1 & 3 \end{pmatrix}$ | $6 - 2 = 4$ | $C_{13} = 4$ |
| $(2,1)$ | $-$ | $\begin{pmatrix} 2 & -1 \\ 3 & -3 \end{pmatrix}$ | $-6 + 3 = -3$ | $C_{21} = 3$ |
| $(2,2)$ | $+$ | $\begin{pmatrix} 1 & -1 \\ 1 & -3 \end{pmatrix}$ | $-3 + 1 = -2$ | $C_{22} = -2$ |
| $(2,3)$ | $-$ | $\begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix}$ | $3 - 2 = 1$ | $C_{23} = -1$ |
| $(3,1)$ | $+$ | $\begin{pmatrix} 2 & -1 \\ 2 & 4 \end{pmatrix}$ | $8 + 2 = 10$ | $C_{31} = 10$ |
| $(3,2)$ | $-$ | $\begin{pmatrix} 1 & -1 \\ 2 & 4 \end{pmatrix}$ | $4 + 2 = 6$ | $C_{32} = -6$ |
| $(3,3)$ | $+$ | $\begin{pmatrix} 1 & 2 \\ 2 & 2 \end{pmatrix}$ | $2 - 4 = -2$ | $C_{33} = -2$ |

### Paso 3: Armar la matriz de cofactores

$$\text{Cof}(A) = \begin{pmatrix} -18 & 10 & 4 \\ 3 & -2 & -1 \\ 10 & -6 & -2 \end{pmatrix}$$

### Paso 4: Transponer

$$[\text{Cof}(A)]^T = \begin{pmatrix} -18 & 3 & 10 \\ 10 & -2 & -6 \\ 4 & -1 & -2 \end{pmatrix}$$

### Paso 5: Multiplicar por $\frac{1}{\det(A)} = \frac{1}{-2}$

$$A^{-1} = \frac{1}{-2} \begin{pmatrix} -18 & 3 & 10 \\ 10 & -2 & -6 \\ 4 & -1 & -2 \end{pmatrix} = \begin{pmatrix} 9 & -\frac{3}{2} & -5 \\ -5 & 1 & 3 \\ -2 & \frac{1}{2} & 1 \end{pmatrix}$$

> "Parece un poco largo pero tengan en cuenta por ejemplo, si van a calcular la inversa con el método directo y las ecuaciones son medias feas, también le va a llevar tiempo"

**Traducción:** Largo pero mecánico. El método directo (sistema de ecuaciones) también lleva tiempo. Cada uno elige el que le resulte más cómodo.

---

# 5. Resultados clave (entran en parcial)

## 5.1. Triangular con diagonal no nula → invertible

(Práctico V.6)

**Enunciado:** Si $A$ es triangular y todas las entradas de la diagonal son no nulas, $A$ es invertible.

**Justificación:** Por **P9**, $\det(A) = a_{11} \cdot a_{22} \cdot \ldots \cdot a_{nn}$. Como cada factor es no nulo, el producto es no nulo. Entonces $\det(A) \neq 0$ y por **Teorema 2**, $A$ es invertible. $\blacksquare$

---

## 5.2. Nilpotente → det = 0

(Práctico V.3)

**Recordatorio:** $A$ es **nilpotente de grado $k$** si $A^k = O$ (la matriz nula) y $A^{k-1} \neq O$.

**Enunciado:** Si $A$ es nilpotente, $\det(A) = 0$.

**Demostración:**

$$\det(A^k) \overset{P4}{=} \det(A)^k$$

Por otro lado, $A^k = O$, entonces $\det(A^k) = \det(O) = 0$.

Igualando: $\det(A)^k = 0$.

¿Qué número elevado a una potencia da $0$? Solo el $0$. Entonces $\det(A) = 0$ $\blacksquare$.

**Consecuencia:** Toda matriz nilpotente es **no invertible** (porque $\det = 0$).

---

## 5.3. Antisimétrica de dimensión impar → det = 0

(Práctico V.4)

**Recordatorio:** $A$ es **antisimétrica** si $A^T = -A$.

**Enunciado parte 1:** $\det(A^T) = (-1)^n \cdot \det(A)$.

**Demostración parte 1:**

$$\det(A^T) \overset{\text{hipótesis}}{=} \det(-A) \overset{P3}{=} (-1)^n \cdot \det(A) \quad \blacksquare$$

**Enunciado parte 2:** Si $n$ es impar, $\det(A) = 0$.

**Demostración parte 2:** Por la parte 1: $\det(A^T) = (-1)^n \cdot \det(A)$. Si $n$ es impar, $(-1)^n = -1$:

$$\det(A^T) = -\det(A)$$

Por **P8**: $\det(A^T) = \det(A)$. Entonces:

$$\det(A) = -\det(A) \implies 2 \det(A) = 0 \implies \det(A) = 0 \quad \blacksquare$$

**Consecuencia:** Toda matriz antisimétrica de dimensión impar es **no invertible**.

---

## 5.4. Ortogonal → det = ±1

(Práctico V.5)

**Recordatorio:** $A$ es **ortogonal** si $A$ es invertible y $A^{-1} = A^T$. Equivalentemente: $A \cdot A^T = I$.

**Enunciado parte 1:** Si $A$ es ortogonal, $\det(A) = 1$ o $\det(A) = -1$.

**Demostración:**

Por hipótesis $A \cdot A^T = I$. Tomamos determinante:

$$\det(A \cdot A^T) = \det(I) = 1$$

Por **P4** y **P8** ($\det(A^T) = \det(A)$):

$$\det(A)^2 = 1 \implies \det(A) = 1 \text{ o } \det(A) = -1 \quad \blacksquare$$

**Parte 2: ¿Vale el recíproco?** Es decir, si $\det(A) = \pm 1$, ¿$A$ es ortogonal? **No**. Contraejemplos:

$$A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \det(A) = 2 - 1 = 1$$

Pero:

$$A \cdot A^T = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \cdot \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix} \neq I$$

→ $A$ no es ortogonal a pesar de tener $\det = 1$.

Análogamente $B = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}$ tiene $\det(B) = -1$ pero $B \cdot B^T \neq I$.

---

# 6. Errores típicos en parcial

### Error 1: Usar Sarrus en matrices que NO son $3 \times 3$

> "He visto varias veces en parciales que aplican la regla de Sarrus para matrices 4x4"

Sarrus **solo** para $3 \times 3$. Para $4 \times 4$ o más: desarrollo por cofactores.

### Error 2: Pensar que $\det(kA) = k \cdot \det(A)$

| MAL | BIEN |
|-----|------|
| $\det(4A) = 4 \cdot \det(A)$ | $\det(4A) = 4^n \cdot \det(A)$ |

Si $A$ es $3 \times 3$: $\det(4A) = 4^3 \cdot \det(A) = 64 \cdot \det(A)$.

### Error 3: Pensar que $\det(A+B) = \det(A) + \det(B)$

**Falso.** No existe propiedad de la suma. Lo que existe es $\det(A \cdot B) = \det(A) \cdot \det(B)$ (producto, no suma).

### Error 4: No mirar la matriz antes de calcular

Antes de hacer ninguna cuenta, chequeá:
- ¿Tiene dos filas o columnas iguales? → $\det = 0$ (P5)
- ¿Es triangular? → multiplicar la diagonal (P9)
- ¿Hay una fila/columna con muchos ceros? → desarrollar por ahí

### Error 5: Multiplicar la fila objetivo al usar P7

Cuando sumás combinación lineal a una fila (P7), la fila que modificás **no puede estar multiplicada** por un número. Si la multiplicás, cambiaste el determinante (P2).

### Error 6: Confundir $(2A)^{-1}$ con $2 \cdot A^{-1}$

> "Se entiende la diferencia, ¿no? Acá puedo aplicar el teorema porque está todo invertido. Acá es la inversa por 2"

| Expresión | ¿Qué significa? | Cálculo (con $A$ $n \times n$, $\det(A) = d$) |
|-----------|-----------------|-----|
| $(2A)^{-1}$ | Primero multiplicás $A$ por $2$, después invertís | $\det((2A)^{-1}) = \dfrac{1}{2^n \cdot d}$ |
| $2 \cdot A^{-1}$ | Primero invertís, después multiplicás por $2$ | $\det(2 \cdot A^{-1}) = 2^n \cdot \dfrac{1}{d}$ |

Son cosas distintas y se calculan distinto.

---

# 7. Checklist y referencia rápida

## Checklist antes de calcular un determinante

1. ¿Hay dos filas (o columnas) iguales? → $\det = 0$, listo (P5)
2. ¿Es triangular (o diagonal)? → multiplicar la diagonal, listo (P9)
3. ¿Hay alguna fila/columna entera de ceros? → $\det = 0$, listo
4. ¿Puedo sacar factor común de alguna fila? → sacarlo (P2) y simplificar
5. ¿Puedo generar ceros con P7? → hacerlo y después desarrollar por la fila/columna con ceros
6. ¿Es $3 \times 3$? → Sarrus
7. ¿Es $4 \times 4$ o más? → desarrollo por cofactores por la fila/columna con más ceros

## Referencia rápida de propiedades

| # | Nombre corto | Fórmula |
|---|-------------|---------|
| 1 | Separar sumandos | $\det = \det_1 + \det_2$ |
| 2 | Factor de fila | $k$ sale multiplicando |
| 3 | Factor de toda la matriz | $\det(kA) = k^n \cdot \det(A)$ |
| 4 | Producto | $\det(AB) = \det(A) \cdot \det(B)$ |
| 5 | Filas iguales | $\det = 0$ |
| 6 | Intercambio | cambia de signo |
| 7 | Comb. lineal de filas | no cambia |
| 8 | Transpuesta | $\det(A) = \det(A^T)$ |
| 9 | Triangular | producto de la diagonal |
| ✗ | Suma (NO) | $\neq \det(A) + \det(B)$ |

## Atajos para la inversa

| Resultado | Fórmula |
|-----------|---------|
| Inversa | $A^{-1} = \dfrac{1}{\det(A)} \cdot [\text{Cof}(A)]^T$ |
| Det de la inversa | $\det(A^{-1}) = \dfrac{1}{\det(A)}$ |
| Det de potencia | $\det(A^k) = \det(A)^k$ |

---

# 8. Ejemplos modelo del práctico (IV.1, IV.2, IV.3)

Estos son los tres ejemplos pre-resueltos del práctico oficial. Aparecen ANTES de la sección de ejercicios, justo para mostrar cómo combinar propiedades.

---

## Ejemplo IV.1: Determinante con polinomios en $x$

**Enunciado:** Calcular $\det(A)$ donde

$$A = \begin{pmatrix} x-1 & x^2 - 1 & 0 \\ 2x & x & x \\ 3x - 6 & x - 2 & x - 2 \end{pmatrix}$$

### Resolución

**Paso 1 — Factorizar cada fila:**
- Fila 1: $(x-1)$, $(x^2-1) = (x-1)(x+1)$, $0$. **Factor común** $(x-1)$.
- Fila 2: $2x$, $x$, $x$. **Factor común** $x$.
- Fila 3: $3(x-2)$, $(x-2)$, $(x-2)$. **Factor común** $(x-2)$.

**Paso 2 — Sacar factores (P2 tres veces):**

$$\det(A) = (x-1) \cdot x \cdot (x-2) \cdot \det\begin{pmatrix} 1 & x+1 & 0 \\ 2 & 1 & 1 \\ 3 & 1 & 1 \end{pmatrix}$$

**Paso 3 — Calcular la $3 \times 3$ con Sarrus:**

Positivas: $1 \cdot 1 \cdot 1 + 2 \cdot 1 \cdot 0 + 3 \cdot (x+1) \cdot 1 = 1 + 0 + 3(x+1) = 1 + 3x + 3 = 3x + 4$

Negativas: $3 \cdot 1 \cdot 0 + 1 \cdot 1 \cdot 1 + 2 \cdot (x+1) \cdot 1 = 0 + 1 + 2x + 2 = 2x + 3$

$\det(\text{interna}) = (3x + 4) - (2x + 3) = x + 1$

**Paso 4 — Resultado:**

$$\det(A) = (x-1) \cdot x \cdot (x-2) \cdot (x+1)$$

> "Se podía hacer por Sarrus toda la expresión original, se podía desarrollar por fila o columna, y vamos a llegar a lo mismo, sí, pero aplicando acá la propiedad 2 se simplifica bastante"

**Traducción:** Sin sacar factores con P2, hubiéramos tenido que hacer Sarrus con expresiones polinómicas largas. Sacando factores antes, queda una matriz numérica simple.

---

## Ejemplo IV.2: Combinar propiedades con $\det(A) = 2$

**Enunciado:** Sean $A$ y $B$ matrices $2 \times 2$ tales que $\det(A) = 2$ y $B = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.

Calcular: (a) $\det(3A^3 \cdot B^T)$, (b) $\det((2A)^{-1})$, (c) $\det(2 \cdot A^{-1})$.

### Dato previo

$\det(B) = 2 \cdot 2 - 0 \cdot 1 = 4$ (es triangular superior, P9: $2 \cdot 2 = 4$).

### Parte (a) — $\det(3A^3 \cdot B^T)$

**Paso 1 — P4** (separar el producto):

$$\det(3A^3 \cdot B^T) = \det(3A^3) \cdot \det(B^T)$$

**Paso 2 — P3** sobre $3A^3$ ($A$ es $2 \times 2$, exponente $2$):

$$\det(3A^3) = 3^2 \cdot \det(A^3) = 9 \cdot \det(A^3)$$

**Paso 3 — P4** sobre $A^3 = A \cdot A \cdot A$:

$$\det(A^3) = \det(A)^3 = 2^3 = 8$$

**Paso 4 — P8** sobre $B^T$:

$$\det(B^T) = \det(B) = 4$$

**Resultado:** $\det(3A^3 \cdot B^T) = 9 \cdot 8 \cdot 4 = 288$.

### Parte (b) — $\det((2A)^{-1})$

**Paso 1 — Teorema 1** (det de la inversa):

$$\det((2A)^{-1}) = \frac{1}{\det(2A)}$$

**Paso 2 — P3** sobre $2A$:

$$\det(2A) = 2^2 \cdot \det(A) = 4 \cdot 2 = 8$$

**Resultado:** $\det((2A)^{-1}) = \dfrac{1}{8}$.

### Parte (c) — $\det(2 \cdot A^{-1})$

> "Se entiende la diferencia, ¿no? Acá puedo aplicar el teorema porque está todo invertido. Acá es la inversa por 2"

**Traducción:** Esto NO es lo mismo que (b). Acá primero invertimos $A$ y después multiplicamos por $2$.

**Paso 1 — P3:**

$$\det(2 \cdot A^{-1}) = 2^2 \cdot \det(A^{-1}) = 4 \cdot \det(A^{-1})$$

**Paso 2 — Teorema 1:**

$$\det(A^{-1}) = \frac{1}{\det(A)} = \frac{1}{2}$$

**Resultado:** $\det(2 \cdot A^{-1}) = 4 \cdot \dfrac{1}{2} = 2$.

### Comparación de las tres partes

| Expresión | Resultado | Propiedades usadas |
|-----------|-----------|-------------------|
| $\det(3A^3 \cdot B^T)$ | $288$ | P4, P3, P4, P8 |
| $\det((2A)^{-1})$ | $\frac{1}{8}$ | T1, P3 |
| $\det(2 \cdot A^{-1})$ | $2$ | P3, T1 |

---

## Ejemplo IV.3: $4 \times 4$ con P1 y P5

**Enunciado:** Calcular el determinante de

$$A = \begin{pmatrix} 1 & -2 & -1 & -1 \\ 2 & 3 & -2 & 5 \\ 0 & 1 & -3 & 1 \\ 1 & 1 & 0 & 2 \end{pmatrix}$$

### Resolución

**Observación inicial:** Si miramos las columnas, vemos que **C4 = C1 + C2**:
- $-1 = 1 + (-2)$
- $5 = 2 + 3$
- $1 = 0 + 1$
- $2 = 1 + 1$

**Paso 1 — Reescribir C4 como suma:**

$$\det(A) = \det\begin{pmatrix} 1 & -2 & -1 & 1 + (-2) \\ 2 & 3 & -2 & 2 + 3 \\ 0 & 1 & -3 & 0 + 1 \\ 1 & 1 & 0 & 1 + 1 \end{pmatrix}$$

**Paso 2 — P1 (separar la suma en C4):**

$$\det(A) = \det\begin{pmatrix} 1 & -2 & -1 & 1 \\ 2 & 3 & -2 & 2 \\ 0 & 1 & -3 & 0 \\ 1 & 1 & 0 & 1 \end{pmatrix} + \det\begin{pmatrix} 1 & -2 & -1 & -2 \\ 2 & 3 & -2 & 3 \\ 0 & 1 & -3 & 1 \\ 1 & 1 & 0 & 1 \end{pmatrix}$$

**Paso 3 — P5 en cada determinante:**

- En el primero, **C1 = C4** (ambas son $(1, 2, 0, 1)$). Por P5, vale $0$.
- En el segundo, **C2 = C4** (ambas son $(-2, 3, 1, 1)$). Por P5, vale $0$.

**Paso 4 — Resultado:** $\det(A) = 0 + 0 = 0$.

> "Es importante dominarlas porque pueden facilitar temas de tiempos en un parcial"

**Traducción:** Calcular un determinante $4 \times 4$ con cofactores hubiera llevado mucho tiempo. Mirar la matriz y descubrir la relación entre columnas resolvió todo en 4 pasos.

---

# 9. Práctico resuelto (V.1 a V.12)

## Ejercicio V.1: Calcular determinantes

Calcular los determinantes detallando las propiedades utilizadas.

### Parte A — $A = \begin{pmatrix} 2 & -5 \\ 2 & 6 \end{pmatrix}$ (2×2)

$\det(A) = 2 \cdot 6 - (-5) \cdot 2 = 12 + 10 = 22$ (definición de $2 \times 2$).

**Resultado:** $\det(A) = 22$.

### Parte B — $B = \begin{pmatrix} -1 & 0 & 2 \\ 3 & 1 & 4 \\ 2 & 0 & -6 \end{pmatrix}$ (3×3)

Por Sarrus:

Positivas: $(-1)(1)(-6) + (3)(0)(2) + (2)(0)(4) = 6 + 0 + 0 = 6$

Negativas: $(2)(1)(2) + (-1)(0)(4) + (3)(0)(-6) = 4 + 0 + 0 = 4$

$\det(B) = 6 - 4 = 2$.

**Atajo:** la columna 2 tiene dos ceros (en posiciones $(1,2)$ y $(3,2)$). Desarrollando por C2 solo sobrevive el cofactor de $b_{22} = 1$, signo $+$:

$\det(B) = 1 \cdot \det\begin{pmatrix} -1 & 2 \\ 2 & -6 \end{pmatrix} = (-1)(-6) - (2)(2) = 6 - 4 = 2$ ✓

**Resultado:** $\det(B) = 2$.

### Parte C — $C = \begin{pmatrix} -3 & 2 & 4 \\ 1 & -1 & 2 \\ -1 & 4 & 0 \end{pmatrix}$ (3×3)

Por Sarrus:

Positivas: $(-3)(-1)(0) + (1)(4)(4) + (-1)(2)(2) = 0 + 16 - 4 = 12$

Negativas: $(-1)(-1)(4) + (-3)(4)(2) + (1)(2)(0) = 4 - 24 + 0 = -20$

$\det(C) = 12 - (-20) = 32$.

**Resultado:** $\det(C) = 32$.

### Parte D — $D = \begin{pmatrix} 2 & -1 & 3 \\ 4 & 0 & 6 \\ 5 & -2 & 3 \end{pmatrix}$ (3×3)

Por Sarrus:

Positivas: $(2)(0)(3) + (4)(-2)(3) + (5)(-1)(6) = 0 - 24 - 30 = -54$

Negativas: $(5)(0)(3) + (2)(-2)(6) + (4)(-1)(3) = 0 - 24 - 12 = -36$

$\det(D) = -54 - (-36) = -18$.

**Resultado:** $\det(D) = -18$.

### Parte E — $E = \begin{pmatrix} 1 & -1 & 2 & 4 \\ 0 & -3 & 0 & 6 \\ 1 & 4 & 5 & 3 \\ 0 & 5 & -6 & 7 \end{pmatrix}$ (4×4)

Sarrus no sirve (es $4 \times 4$). Estrategia: usamos **P7** para generar ceros en la columna 1 y después desarrollamos por C1.

**Paso 1 (P7):** $F_3 \leftarrow F_3 - F_1$:

$$E' = \begin{pmatrix} 1 & -1 & 2 & 4 \\ 0 & -3 & 0 & 6 \\ 0 & 5 & 3 & -1 \\ 0 & 5 & -6 & 7 \end{pmatrix}$$

$\det(E') = \det(E)$ (P7 no cambia det).

**Paso 2 — Desarrollo por C1:** Solo sobrevive el cofactor de $e_{11} = 1$, signo $+$:

$$\det(E') = 1 \cdot \det\begin{pmatrix} -3 & 0 & 6 \\ 5 & 3 & -1 \\ 5 & -6 & 7 \end{pmatrix}$$

**Paso 3 — Sarrus en la 3×3:**

Positivas: $(-3)(3)(7) + (5)(-6)(6) + (5)(0)(-1) = -63 - 180 + 0 = -243$

Negativas: $(5)(3)(6) + (-3)(-6)(-1) + (5)(0)(7) = 90 - 18 + 0 = 72$

$\det = -243 - 72 = -315$.

**Resultado:** $\det(E) = -315$.

---

## Ejercicio V.2: Operaciones con $\det(A) = 8$

Sabiendo que $\det\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} = 8$, calcular los determinantes de las siguientes matrices.

### Parte A — $A = \begin{pmatrix} a_{31} & a_{32} & a_{33} \\ a_{21} & a_{22} & a_{23} \\ a_{11} & a_{12} & a_{13} \end{pmatrix}$

Las filas están en orden 3, 2, 1. Esto es la matriz original con **F1 ↔ F3**. Un solo intercambio.

Por **P6**: $\det(A) = -8$.

### Parte B — $B = \begin{pmatrix} a_{31} & a_{32} & a_{33} \\ a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{pmatrix}$

Las filas están en orden 3, 1, 2. Hay que pensarlo en pasos:
- Original: F1, F2, F3
- Intercambio F1 ↔ F3: queda F3, F2, F1 → cambia signo
- Intercambio F2 ↔ F3: queda F3, F1, F2 → vuelve a cambiar signo

Dos intercambios → $\det(B) = (-1)^2 \cdot 8 = 8$.

### Parte C — $C = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ 2 a_{21} & 2 a_{22} & 2 a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$

La fila 2 está multiplicada por 2. Por **P2**: $\det(C) = 2 \cdot 8 = 16$.

### Parte D — $D = \begin{pmatrix} -3 a_{11} & -3 a_{12} & -3 a_{13} \\ 2 a_{21} & 2 a_{22} & 2 a_{23} \\ 5 a_{31} & 5 a_{32} & 5 a_{33} \end{pmatrix}$

Cada fila está multiplicada por un escalar distinto. Aplicamos **P2** tres veces, una por fila:

$\det(D) = (-3) \cdot 2 \cdot 5 \cdot \det(\text{original}) = -30 \cdot 8 = -240$.

### Parte E — $E = \begin{pmatrix} a_{11} & a_{13} & a_{12} \\ a_{21} & a_{23} & a_{22} \\ a_{31} & a_{33} & a_{32} \end{pmatrix}$

Las columnas están en orden 1, 3, 2. Esto es la matriz original con **C2 ↔ C3**. Un solo intercambio.

Por **P6**: $\det(E) = -8$.

### Parte F — $F = \begin{pmatrix} a_{11}-a_{12} & a_{12} & a_{13} \\ a_{21}-a_{22} & a_{22} & a_{23} \\ a_{31}-a_{32} & a_{32} & a_{33} \end{pmatrix}$

La C1 nueva es $C_1 - C_2$. Las otras columnas no cambiaron.

Esto es **P7 aplicada a columnas**: a la C1 le restamos la C2 (combinación lineal de las otras columnas). El determinante **no cambia**:

$\det(F) = 8$.

---

## Ejercicio V.3: Determinante de una matriz nilpotente

¿Cuánto vale el determinante de una matriz nilpotente?

**Definición:** $A$ es nilpotente de grado $k$ si $A^k = O$ y $A^{k-1} \neq O$.

**Resolución:**

Tomamos determinante de $A^k = O$:

$$\det(A^k) = \det(O) = 0$$

Por **P4** aplicada $k$ veces ($\det(A \cdot A) = \det(A)^2$, etc.):

$$\det(A)^k = 0$$

El único número real cuya potencia $k$-ésima es $0$ es el $0$:

$$\det(A) = 0 \quad \blacksquare$$

**Consecuencia:** Toda matriz nilpotente es no invertible.

---

## Ejercicio V.4: Antisimétrica

Sea $A$ una matriz $n \times n$ antisimétrica ($A^T = -A$).

### Parte 1: Mostrar que $\det(A^T) = (-1)^n \cdot \det(A)$

$$\det(A^T) \overset{\text{hipótesis}}{=} \det(-A) \overset{P3}{=} (-1)^n \cdot \det(A) \quad \blacksquare$$

### Parte 2: Si $n$ es impar, ¿cuánto vale $\det(A)$?

Por la parte 1: $\det(A^T) = (-1)^n \cdot \det(A)$.

Si $n$ es impar, $(-1)^n = -1$:

$$\det(A^T) = -\det(A)$$

Por **P8**: $\det(A^T) = \det(A)$. Entonces:

$$\det(A) = -\det(A) \implies 2 \det(A) = 0 \implies \det(A) = 0 \quad \blacksquare$$

---

## Ejercicio V.5: Ortogonal

### Parte 1: Si $A$ es ortogonal, $\det(A) = 1$ o $\det(A) = -1$

Por hipótesis $A^{-1} = A^T$, entonces $A \cdot A^T = I$. Tomamos determinante:

$$\det(A \cdot A^T) = \det(I) = 1$$

Por **P4** y **P8** ($\det(A^T) = \det(A)$):

$$\det(A)^2 = 1 \implies \det(A) = 1 \text{ o } \det(A) = -1 \quad \blacksquare$$

### Parte 2: ¿Vale el recíproco?

Es decir: si $\det(A) = \pm 1$, ¿$A$ es ortogonal? **No**. Contraejemplos:

$$A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \det(A) = 2 - 1 = 1$$

Pero:

$$A \cdot A^T = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \cdot \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix} \neq I$$

→ $A$ no es ortogonal a pesar de tener $\det = 1$.

Análogamente $B = \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}$ tiene $\det(B) = -1$ pero $B \cdot B^T \neq I$.

---

## Ejercicio V.6: Triangular con diagonal no nula es invertible

**Enunciado:** Explicar por qué una matriz triangular con todas las entradas de la diagonal principal no nulas tiene inversa.

**Resolución:** Sea $A$ triangular superior (igual razonamiento si es inferior). Por **P9**:

$$\det(A) = a_{11} \cdot a_{22} \cdot \ldots \cdot a_{nn}$$

Como cada factor es no nulo (por hipótesis), el producto es no nulo: $\det(A) \neq 0$.

Por **Teorema 2**, $A$ es invertible. $\blacksquare$

---

## Ejercicio V.7: Verdadero/falso

### 1. $A$ es invertible ⇔ $A^T$ es invertible

**Verdadero.** Por **P8**, $\det(A) = \det(A^T)$. Entonces $A$ invertible $\iff \det(A) \neq 0 \iff \det(A^T) \neq 0 \iff A^T$ invertible.

### 2. Si $\det(A) \neq 0$, $A$ es invertible y $\det(A^{-1}) = 1/\det(A)$

**Verdadero.** Esto es directamente el **Teorema 2** (la dirección det ≠ 0 → invertible) y la fórmula del **Teorema 1** ($\det(A^{-1}) = 1/\det(A)$).

### 3. Una matriz $A$ con una fila de ceros puede ser invertible

**Falso.** Si $A$ tiene una fila de ceros, al desarrollar el determinante por esa fila, todos los términos llevan un cero como factor. Entonces $\det(A) = 0$ → $A$ no invertible (por **Teorema 1** contrapositivo).

### 4. Una matriz $A$ con una columna de ceros puede tener determinante no nulo

**Falso.** Mismo razonamiento que el anterior, desarrollando por la columna: $\det(A) = 0$.

### 5. Una matriz con dos filas iguales no es invertible

**Verdadero.** Por **P5**, $\det(A) = 0$. Por **Teorema 1** contrapositivo, $A$ no es invertible.

### 6. Es posible hallar la inversa de una matriz con dos columnas iguales

**Falso.** Por **P5** (vale para columnas también), $\det(A) = 0$. La matriz no es invertible, no existe $A^{-1}$.

---

## Ejercicio V.8: Valores de $\lambda$ para los cuales la matriz es invertible

### Matriz A — $A = \begin{pmatrix} \lambda & 1 & 0 & 0 \\ 0 & \lambda & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & \lambda & 0 & 0 \end{pmatrix}$ (4×4)

**Estrategia:** Desarrollamos por F4 (tiene tres ceros). Solo sobrevive $a_{42} = \lambda$, signo $(-1)^{4+2} = +$:

$$\det(A) = \lambda \cdot \det\begin{pmatrix} \lambda & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$$

Esa 3×3 tiene C1 con dos ceros. Desarrollamos por C1: solo sobrevive $\lambda$ en posición $(1,1)$, signo $+$:

$$\det(A) = \lambda \cdot \lambda \cdot \det\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \lambda^2 \cdot (0 - 1) = -\lambda^2$$

**Conclusión:** $A$ invertible $\iff \det(A) \neq 0 \iff -\lambda^2 \neq 0 \iff \lambda \neq 0$.

### Matriz B — $B = \begin{pmatrix} \lambda & 0 & \lambda \\ 1 & 1 & \lambda \\ \lambda & 1 & 0 \end{pmatrix}$ (3×3)

**Estrategia:** Desarrollamos por F1 (tiene un cero):

$$\det(B) = \lambda \cdot \det\begin{pmatrix} 1 & \lambda \\ 1 & 0 \end{pmatrix} - 0 + \lambda \cdot \det\begin{pmatrix} 1 & 1 \\ \lambda & 1 \end{pmatrix}$$

$= \lambda \cdot (0 - \lambda) + \lambda \cdot (1 - \lambda) = -\lambda^2 + \lambda - \lambda^2 = -2\lambda^2 + \lambda$

**Conclusión:** $\det(B) = -2\lambda^2 + \lambda = \lambda(1 - 2\lambda)$. Vale $0 \iff \lambda = 0$ o $\lambda = 1/2$.

$B$ invertible $\iff \lambda \neq 0$ y $\lambda \neq 1/2$.

### Matriz C — $C = \begin{pmatrix} \lambda & 0 & \lambda & 0 \\ 1 & 1 & \lambda & 0 \\ \lambda & 1 & 0 & 0 \\ 0 & 0 & 0 & \lambda \end{pmatrix}$ (4×4)

**Estrategia:** F4 tiene tres ceros. Desarrollamos por F4: solo sobrevive $c_{44} = \lambda$, signo $(-1)^{4+4} = +$:

$$\det(C) = \lambda \cdot \det\begin{pmatrix} \lambda & 0 & \lambda \\ 1 & 1 & \lambda \\ \lambda & 1 & 0 \end{pmatrix} = \lambda \cdot \det(B) = \lambda \cdot (-2\lambda^2 + \lambda) = -2\lambda^3 + \lambda^2$$

**Conclusión:** $\det(C) = \lambda^2(1 - 2\lambda)$. Vale $0 \iff \lambda = 0$ o $\lambda = 1/2$.

$C$ invertible $\iff \lambda \neq 0$ y $\lambda \neq 1/2$.

---

## Ejercicio V.9: Investigar si $A$ es invertible

Sean $A$ y $B$ matrices $3 \times 3$ tales que:

$$\det\left[A \cdot \left(\frac{1}{2} B\right)^{-1}\right] = \det(3B) + \det(A - A \cdot B)$$

con $B = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 2 & 1 \end{pmatrix}$. Investigar si $A$ es invertible.

**Paso 1: Calcular $\det(B)$.** $B$ es triangular inferior. Por **P9**: $\det(B) = 1 \cdot 1 \cdot 1 = 1$.

**Paso 2: Lado izquierdo.**

$$\det\left[A \cdot \left(\tfrac{1}{2}B\right)^{-1}\right] \overset{P4}{=} \det(A) \cdot \det\left[\left(\tfrac{1}{2}B\right)^{-1}\right] \overset{T1}{=} \det(A) \cdot \frac{1}{\det\left(\tfrac{1}{2}B\right)} \overset{P3}{=} \det(A) \cdot \frac{1}{(1/2)^3 \cdot \det(B)}$$

$= \det(A) \cdot \dfrac{1}{(1/8) \cdot 1} = 8 \cdot \det(A)$

**Paso 3: Primer término del lado derecho.**

$$\det(3B) \overset{P3}{=} 3^3 \cdot \det(B) = 27 \cdot 1 = 27$$

**Paso 4: Segundo término del lado derecho.**

Factorizamos: $A - A \cdot B = A \cdot (I - B)$. Por **P4**:

$$\det(A - AB) = \det(A) \cdot \det(I - B)$$

Calculamos $I - B$:

$$I - B = \begin{pmatrix} 0 & 0 & 0 \\ -2 & 0 & 0 \\ 0 & -2 & 0 \end{pmatrix}$$

Esta matriz tiene F1 toda de ceros → $\det(I - B) = 0$ (al desarrollar por F1, todos los términos son $0$).

Entonces el segundo término vale $\det(A) \cdot 0 = 0$.

**Paso 5: Despejar.**

$$8 \cdot \det(A) = 27 + 0 = 27 \implies \det(A) = \frac{27}{8}$$

Como $\det(A) = 27/8 \neq 0$, por **Teorema 2**, $A$ es invertible. $\blacksquare$

---

## Ejercicio V.10: $\det(A) = 3$, calcular varios determinantes

Sea $A$ una matriz $3 \times 3$ con $\det(A) = 3$.

### Parte 1: Determinante de la matriz transformada

$$M = \begin{pmatrix} 2 a_{12} & 2 a_{11} & 2 a_{13} \\ -2 a_{22} & -2 a_{21} & -2 a_{23} \\ \tfrac{1}{2} a_{32} + 10 a_{12} & \tfrac{1}{2} a_{31} + 10 a_{11} & \tfrac{1}{2} a_{33} + 10 a_{13} \end{pmatrix}$$

**Paso 1 (P1):** F3 tiene sumandos. Separamos en dos determinantes — el primero con $\tfrac{1}{2}a_{3j}$, el segundo con $10 a_{1j}$:

$$\det_1 = \det\begin{pmatrix} 2 a_{12} & 2 a_{11} & 2 a_{13} \\ -2 a_{22} & -2 a_{21} & -2 a_{23} \\ \tfrac{1}{2} a_{32} & \tfrac{1}{2} a_{31} & \tfrac{1}{2} a_{33} \end{pmatrix}$$

$$\det_2 = \det\begin{pmatrix} 2 a_{12} & 2 a_{11} & 2 a_{13} \\ -2 a_{22} & -2 a_{21} & -2 a_{23} \\ 10 a_{12} & 10 a_{11} & 10 a_{13} \end{pmatrix}$$

**Paso 2 — $\det_2 = 0$:** En $\det_2$, F3 = $5 \cdot$ F1 (porque $10 = 5 \cdot 2$, y los términos coinciden con los de F1 multiplicados por $5$). Sacando factor 2 de F1 y factor 10 de F3 con **P2**, queda F1 = F3 = $(a_{12}, a_{11}, a_{13})$. Por **P5**, $\det_2 = 0$.

**Paso 3 — $\det_1$:** Sacamos factores de cada fila por **P2**:
- F1: factor $2$
- F2: factor $-2$
- F3: factor $1/2$

Producto: $2 \cdot (-2) \cdot (1/2) = -2$.

Queda:

$$\det_1 = -2 \cdot \det\begin{pmatrix} a_{12} & a_{11} & a_{13} \\ a_{22} & a_{21} & a_{23} \\ a_{32} & a_{31} & a_{33} \end{pmatrix}$$

Esa matriz interior es $A$ con **C1 ↔ C2**. Por **P6**:

$$\det\begin{pmatrix} a_{12} & a_{11} & a_{13} \\ a_{22} & a_{21} & a_{23} \\ a_{32} & a_{31} & a_{33} \end{pmatrix} = -\det(A) = -3$$

Entonces $\det_1 = -2 \cdot (-3) = 6$.

**Paso 4 — total:**

$$\det(M) = \det_1 + \det_2 = 6 + 0 = 6$$

**Resultado:** $6$.

### Parte 2: Calcular $\det(A^T) \cdot \det(6 A (2A)^{-1})$

$$\det(A^T) \overset{P8}{=} \det(A) = 3$$

$$\det(6 A (2A)^{-1}) \overset{P3}{=} 6^3 \cdot \det(A (2A)^{-1}) \overset{P4}{=} 216 \cdot \det(A) \cdot \det((2A)^{-1})$$

$$\det((2A)^{-1}) \overset{T1}{=} \frac{1}{\det(2A)} \overset{P3}{=} \frac{1}{2^3 \cdot \det(A)} = \frac{1}{8 \cdot 3} = \frac{1}{24}$$

$$\det(6A (2A)^{-1}) = 216 \cdot 3 \cdot \frac{1}{24} = \frac{648}{24} = 27$$

**Resultado total:** $3 \cdot 27 = 81$.

### Parte 3: ¿Es invertible $B = 2 \cdot A^2 \cdot (4A)^{-1} \cdot \left(\frac{1}{2} A^T\right)$?

$B$ invertible $\iff \det(B) \neq 0$. Calculamos:

$$\det(B) = \det\left(2 \cdot A^2 \cdot (4A)^{-1} \cdot \tfrac{1}{2} A^T\right) \overset{P3}{=} 2^3 \cdot \det\left(A^2 (4A)^{-1} \tfrac{1}{2} A^T\right)$$

$$\overset{P4}{=} 8 \cdot \det(A^2) \cdot \det((4A)^{-1}) \cdot \det\left(\tfrac{1}{2} A^T\right)$$

Cada factor:
- $\det(A^2) = \det(A)^2 = 9$ (P4)
- $\det((4A)^{-1}) = \dfrac{1}{\det(4A)} = \dfrac{1}{4^3 \cdot 3} = \dfrac{1}{192}$ (T1 + P3)
- $\det(\tfrac{1}{2} A^T) = (\tfrac{1}{2})^3 \cdot \det(A^T) = \dfrac{1}{8} \cdot 3 = \dfrac{3}{8}$ (P3 + P8)

Total:

$$\det(B) = 8 \cdot 9 \cdot \frac{1}{192} \cdot \frac{3}{8} = \frac{8 \cdot 9 \cdot 3}{192 \cdot 8} = \frac{216}{1536} = \frac{9}{64}$$

Como $\det(B) = 9/64 \neq 0$, $B$ es invertible.

---

## Ejercicio V.11: Para qué $\lambda$ es invertible

Determinar para qué valores de $\lambda$ la matriz

$$A = \begin{pmatrix} \lambda^2 - 4 & \lambda - 3 & 3\lambda \\ \lambda - 2 & \lambda^2 - 9 & 3\lambda^2 \\ 2\lambda - 4 & \lambda - 3 & 3\lambda \end{pmatrix}$$

es invertible.

**Paso 1 — Factorizar cada columna:**
- C1: $\lambda^2 - 4 = (\lambda-2)(\lambda+2)$, $\lambda - 2$, $2\lambda - 4 = 2(\lambda-2)$. Factor común: $(\lambda - 2)$.
- C2: $\lambda - 3$, $\lambda^2 - 9 = (\lambda-3)(\lambda+3)$, $\lambda - 3$. Factor común: $(\lambda - 3)$.
- C3: $3\lambda$, $3\lambda^2$, $3\lambda$. Factor común: $3\lambda$.

**Paso 2 — Sacar factores comunes (P2 aplicada a columnas):**

$$\det(A) = (\lambda-2)(\lambda-3)(3\lambda) \cdot \det\begin{pmatrix} \lambda+2 & 1 & 1 \\ 1 & \lambda+3 & \lambda \\ 2 & 1 & 1 \end{pmatrix}$$

**Paso 3 — Generar ceros con P7:** $F_1 \leftarrow F_1 - F_3$:

Nueva F1 = $(\lambda + 2 - 2, \; 1 - 1, \; 1 - 1) = (\lambda, 0, 0)$.

$$\det(A) = (\lambda-2)(\lambda-3)(3\lambda) \cdot \det\begin{pmatrix} \lambda & 0 & 0 \\ 1 & \lambda+3 & \lambda \\ 2 & 1 & 1 \end{pmatrix}$$

**Paso 4 — Desarrollo por F1:** Solo sobrevive el $\lambda$ de $(1,1)$:

$$\det\begin{pmatrix} \lambda & 0 & 0 \\ 1 & \lambda+3 & \lambda \\ 2 & 1 & 1 \end{pmatrix} = \lambda \cdot \det\begin{pmatrix} \lambda+3 & \lambda \\ 1 & 1 \end{pmatrix} = \lambda \cdot ((\lambda+3) - \lambda) = \lambda \cdot 3 = 3\lambda$$

**Paso 5 — Total:**

$$\det(A) = (\lambda-2)(\lambda-3)(3\lambda) \cdot 3\lambda = (\lambda-2)(\lambda-3)(3\lambda)^2$$

$\det(A) = 0$ cuando $\lambda = 2$, $\lambda = 3$, o $\lambda = 0$.

**Conclusión:** $A$ invertible $\iff \lambda \neq 0, 2, 3$.

---

## Ejercicio V.12: Producto y determinantes con parámetros

Sean

$$A = \begin{pmatrix} 0 & \alpha & 0 \\ \alpha & 0 & 0 \\ 0 & 0 & \alpha \end{pmatrix}, \quad B = \begin{pmatrix} -4 & 0 & -3 \\ 0 & \beta & 0 \\ -3 & 0 & 4 \end{pmatrix}$$

con $\alpha, \beta$ reales positivos.

### Parte 1: Calcular $C = A \cdot B$

Producto fila por columna:

| Posición | Cálculo | Valor |
|----------|---------|-------|
| $C_{11}$ | $0 \cdot (-4) + \alpha \cdot 0 + 0 \cdot (-3)$ | $0$ |
| $C_{12}$ | $0 \cdot 0 + \alpha \cdot \beta + 0 \cdot 0$ | $\alpha\beta$ |
| $C_{13}$ | $0 \cdot (-3) + \alpha \cdot 0 + 0 \cdot 4$ | $0$ |
| $C_{21}$ | $\alpha \cdot (-4) + 0 \cdot 0 + 0 \cdot (-3)$ | $-4\alpha$ |
| $C_{22}$ | $\alpha \cdot 0 + 0 \cdot \beta + 0 \cdot 0$ | $0$ |
| $C_{23}$ | $\alpha \cdot (-3) + 0 \cdot 0 + 0 \cdot 4$ | $-3\alpha$ |
| $C_{31}$ | $0 \cdot (-4) + 0 \cdot 0 + \alpha \cdot (-3)$ | $-3\alpha$ |
| $C_{32}$ | $0 \cdot 0 + 0 \cdot \beta + \alpha \cdot 0$ | $0$ |
| $C_{33}$ | $0 \cdot (-3) + 0 \cdot 0 + \alpha \cdot 4$ | $4\alpha$ |

$$C = \begin{pmatrix} 0 & \alpha\beta & 0 \\ -4\alpha & 0 & -3\alpha \\ -3\alpha & 0 & 4\alpha \end{pmatrix}$$

### Parte 2: $\det(A)$, $\det(B)$, $\det(AB)$

**$\det(A)$:** F1 tiene dos ceros (en $(1,1)$ y $(1,3)$). Desarrollo por F1: solo sobrevive el $\alpha$ en posición $(1,2)$, signo $(-1)^{1+2} = -$:

$$\det(A) = -\alpha \cdot \det\begin{pmatrix} \alpha & 0 \\ 0 & \alpha \end{pmatrix} = -\alpha \cdot \alpha^2 = -\alpha^3$$

**$\det(B)$:** F2 tiene dos ceros (en $(2,1)$ y $(2,3)$). Desarrollo por F2: solo sobrevive el $\beta$ en $(2,2)$, signo $+$:

$$\det(B) = \beta \cdot \det\begin{pmatrix} -4 & -3 \\ -3 & 4 \end{pmatrix} = \beta \cdot (-16 - 9) = -25\beta$$

**$\det(AB)$:** Por **P4**:

$$\det(AB) = \det(A) \cdot \det(B) = (-\alpha^3) \cdot (-25\beta) = 25\alpha^3 \beta$$

---

# 10. Para el parcial: estrategia y lo que tenés que saber

## 10.1. Lo que SÍ entra (y hay que dominar)

| Tema | Nivel exigido |
|------|---------------|
| Calcular determinantes 2×2 | Mecánico |
| Sarrus en 3×3 | Mecánico |
| Desarrollo por cofactores en 4×4+ | Mecánico, eligiendo fila/columna óptima |
| Adjunta de un elemento (menor) | Saber qué es y cómo se obtiene |
| Las 9 propiedades | Cuándo usarlas + saber demostrarlas |
| Teorema 1 + Teorema 2 (el "si y solo si") | Enunciado, idea de demostración del T1 |
| Inversa por cofactores | Procedimiento + ejemplo completo |
| $\det(A^{-1}) = 1/\det(A)$ | Aplicación directa |
| Combinar propiedades | $\det(3A^2 \cdot B^T)$, $\det((2A)^{-1})$, etc. |
| Nilpotente → $\det = 0$ | Resultado + demostración |
| Antisimétrica + $n$ impar → $\det = 0$ | Resultado + demostración |
| Ortogonal → $\det = \pm 1$ | Resultado + demostración + recíproco con contraejemplo |
| Triangular con diagonal no nula → invertible | Justificar con P9 + T2 |
| Para qué $\lambda$ es invertible | Calcular $\det$ en función de $\lambda$, ver dónde se anula |

## 10.2. Lo que NO hace falta memorizar al pie de la letra

- La fórmula directa de Sarrus (es para entender cómo funciona, pero en la práctica ejecutás el procedimiento visual)
- La fórmula explícita $\sum_{j=1}^{n}$ del cofactor (basta con entender el procedimiento)
- Los exponentes de $(-1)^{i+j}$ — el tablero de signos es más rápido visualmente

## 10.3. Antes de calcular cualquier determinante en parcial

Aplicar el **checklist**:

1. ¿Filas/columnas iguales? → $0$
2. ¿Triangular? → producto diagonal
3. ¿Fila/columna entera de ceros? → $0$
4. ¿Sumas en alguna fila? → P1 + P5 (ojo si dos sumandos generan filas iguales)
5. ¿Factor común en alguna fila/columna? → P2
6. ¿Hay forma de generar ceros con P7? → hacerlo
7. ¿Sigue siendo $3 \times 3$? → Sarrus. ¿Es más grande? → cofactores

## 10.4. Recetas rápidas para combinar propiedades

| Si te piden... | Aplicá... |
|----------------|-----------|
| $\det(kA)$ | P3: $k^n \cdot \det(A)$ |
| $\det(A^k)$ | P4 $k$ veces: $\det(A)^k$ |
| $\det(A^{-1})$ | T1: $1/\det(A)$ |
| $\det(A^T)$ | P8: $\det(A)$ |
| $\det(A \cdot B)$ | P4: $\det(A) \cdot \det(B)$ |
| $\det((kA)^{-1})$ | T1 + P3: $1/(k^n \cdot \det(A))$ |
| $\det(k \cdot A^{-1})$ | P3 + T1: $k^n / \det(A)$ |

## 10.5. Cuando aparece "investigar si es invertible"

Tres caminos posibles:

| Camino | Cuándo usarlo |
|--------|--------------|
| Calcular $\det(A)$ y verificar $\neq 0$ | Si te dan la matriz explícita o expresión computable |
| Argumento estructural | Si la matriz es triangular, antisimétrica impar, nilpotente, etc. |
| Despejar $\det(A)$ de una ecuación | Si te dan una ecuación que involucra $\det(A)$ junto con otras cosas (V.9, V.10) |

## 10.6. Cuando aparece "para qué $\lambda$ es invertible"

1. Calcular $\det(A)$ en función de $\lambda$
2. Factorizar el polinomio resultante
3. Las raíces dicen "para qué $\lambda$ NO es invertible"
4. La respuesta: "$\lambda \neq$ esas raíces"

## 10.7. Demostrar igualdades del tipo $\det(\ldots) = $ algo

Estrategia general:
1. Empezar del lado más complicado
2. Aplicar **P4** para separar productos
3. Aplicar **P3** para sacar escalares
4. Aplicar **P8** si aparece transpuesta
5. Aplicar **T1** si aparece inversa
6. Llegar al lado más simple

---

## Cierre

El tema de determinantes es **casi todo procedimiento**. No hay teoría rara — hay 9 propiedades, 2 teoremas, una fórmula para la inversa, y unos resultados clásicos (nilpotente, antisimétrica, ortogonal, triangular). Con eso y práctica, todos los ejercicios del parcial salen.

> "Es importante dominarlas porque pueden facilitar temas de tiempos en un parcial"

**Traducción:** En el parcial el tiempo es escaso. Las propiedades son atajos. Saber cuándo aplicar cada una te ahorra cuentas. **Antes de calcular nada, mirá la matriz.**
