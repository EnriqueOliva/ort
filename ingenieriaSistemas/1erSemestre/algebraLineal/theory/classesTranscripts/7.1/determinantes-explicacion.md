# Determinantes — Explicación paso a paso, desde cero

Este documento cubre **determinantes**: qué son, cómo se calculan, las 9 propiedades, el teorema central, y ejercicios. Al final hay preparación para la evaluación continua del 15 de abril. Todo explicado asumiendo que no sabés nada.

---

## Mapa de lo que vamos a ver

| Parte | ¿Qué se aprende? |
|-------|-------------------|
| 1 | Qué es un determinante, cómo calcularlo, y las 9 propiedades (Clase 5) |
| 2 | El teorema que conecta "invertible" con "determinante ≠ 0", más ejercicios (Clase 6) |
| 3 | Teorema 2 (la vuelta: det ≠ 0 → invertible), nueva fórmula para la inversa, demostraciones de propiedades (Clase 7) |
| 4 | **Prep evaluación continua: errores comunes, checklist, preguntas de práctica** |

---

# PARTE 1 — ¿Qué es un determinante? (Clase 5, 7 de abril)

## La Gran Pregunta de Hoy: ¿Qué es el determinante y cómo se calcula?

Esta es la primera clase después de vacaciones y arranca un tema completamente nuevo. Vamos a ver:
1. Qué es un determinante (en palabras simples)
2. Cómo calcularlo (empezando por las matrices más chicas)
3. Las 9 propiedades (atajos que ahorran cuentas en el parcial)

## Anuncio sobre la prueba

> "La prueba va a ser de determinantes específicas"

**Traducción:** La segunda prueba de evaluación continua será el miércoles 16 de abril, sobre determinantes. Mismo formato que la primera: nivel básico, en grupo, con material.

---

## Conexión con la Clase Anterior

La clase 4 fue práctica, cerró matrices. Hubo prueba de evaluación continua y luego vacaciones. Hoy arranca un tema nuevo desde cero.

---

## ¿Qué es un determinante?

### La idea en una oración

El determinante es **un número** que le asignamos a una matriz cuadrada y que nos dice si esa matriz es invertible o no.

### La analogía

Pensá en el determinante como un **semáforo** de la matriz:
- Si el determinante es **distinto de cero** → luz verde: la matriz tiene inversa, el sistema de ecuaciones tiene solución única, todo funciona.
- Si el determinante es **igual a cero** → luz roja: la matriz NO tiene inversa, algo anda mal.

> "Es un número característico de una matriz, siempre hablando de matrices cuadradas, que entre otras cosas nos va a indicar si la matriz es invertible o no"

**Traducción:** El determinante toma una **matriz cuadrada** (tiene que ser cuadrada, sí o sí) y devuelve **un número**. Ese número nos dice cosas fundamentales sobre la matriz.

### ¿Para qué sirve?

Hasta ahora, para saber si una matriz tenía inversa, teníamos que hacer toda la cuenta del método directo (plantear el sistema de ecuaciones, resolverlo, y ver si tiene solución). El determinante nos da una respuesta **mucho más rápida**: si el número da distinto de cero, la matriz es invertible. Punto.

### Notación

Hay dos formas de escribir "el determinante de la matriz $A$":

| Notación | Cómo se lee |
|----------|-------------|
| $\|A\|$ | "determinante de A" (parece valor absoluto, pero NO lo es) |
| $\det(A)$ | "determinante de A" (más explícito) |

> "Esto acá que pareciera el valor absoluto de A significa determinante de A"

**Traducción:** Cuidado con las barras verticales. Cuando rodean una **matriz**, significan "determinante". No es valor absoluto. De hecho, el determinante **puede ser negativo** (el valor absoluto no puede).

### Requisito fundamental

Solo se puede calcular el determinante de **matrices cuadradas** ($n \times n$). Si la matriz tiene distinta cantidad de filas que de columnas (por ejemplo $3 \times 4$), no existe su determinante.

---

## Cómo calcular un determinante

### Antes de calcular: ¿de dónde sale la fórmula del determinante?

Cuando tenés un sistema de 2 ecuaciones con 2 incógnitas:

$$a \cdot x + b \cdot y = e$$
$$c \cdot x + d \cdot y = f$$

Si lo resolvés despejando (sustitución o igualación), la solución te queda:

$$x = \frac{e \cdot d - b \cdot f}{a \cdot d - b \cdot c}, \quad y = \frac{a \cdot f - c \cdot e}{a \cdot d - b \cdot c}$$

Mirá el **denominador**: $a \cdot d - b \cdot c$. Si ese número es $0$, estás dividiendo por cero y el sistema no tiene solución única. Si es $\neq 0$, el sistema sí tiene solución única.

Ese denominador es exactamente el **determinante** de la matriz de coeficientes $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$. El determinante no es una fórmula arbitraria — es el número que aparece naturalmente cuando intentás resolver un sistema de ecuaciones. Si vale $0$, no hay solución única. Si vale $\neq 0$, sí la hay.

### La regla general para calcular un determinante

La regla es: **elegir un número de cada fila, sin repetir columna**, multiplicarlos entre sí, y sumar todos esos productos con cierto signo ($+$ o $-$).

En una $1 \times 1$: hay **1 sola manera** de elegir (el único número). Así que $\det(A) = a_{11}$.

En una $2 \times 2$: hay **2 maneras** de elegir un número por fila sin repetir columna, y las dos resultan ser las dos diagonales:

```
| a  b |
| c  d |

Manera 1: fila 1→col 1 (=a), fila 2→col 2 (=d) → a·d     signo +
Manera 2: fila 1→col 2 (=b), fila 2→col 1 (=c) → b·c     signo -

det = a·d - b·c
```

En $2 \times 2$, la regla y "multiplicar diagonales" dan lo mismo. Pero en $3 \times 3$ ya no, porque hay **6 maneras** de elegir un número por fila sin repetir columna, y solo 2 de las 6 parecen diagonales. Las otras 4 no forman ninguna línea visual en la matriz.

**Ejemplo numérico $2 \times 2$:**

$$A = \begin{pmatrix} 2 & 4 \\ 6 & 1 \end{pmatrix}$$

Manera 1: $2 \cdot 1 = 2$ (con $+$). Manera 2: $4 \cdot 6 = 24$ (con $-$).

$$\det(A) = 2 - 24 = -22$$

Como es $\neq 0$, la matriz es invertible.

---

### Matrices $3 \times 3$: las 6 combinaciones

**Ejemplo con números:**

$$A = \begin{pmatrix} 4 & 1 & 3 \\ 2 & 5 & 7 \\ 6 & 0 & 8 \end{pmatrix}$$

Las 6 maneras de elegir (un número por fila, columnas distintas):

| # | Fila 1 → | Fila 2 → | Fila 3 → | Producto | Signo |
|---|----------|----------|----------|----------|-------|
| 1 | col 1 = $4$ | col 2 = $5$ | col 3 = $8$ | $160$ | $+$ |
| 2 | col 2 = $1$ | col 3 = $7$ | col 1 = $6$ | $42$ | $+$ |
| 3 | col 3 = $3$ | col 1 = $2$ | col 2 = $0$ | $0$ | $+$ |
| 4 | col 3 = $3$ | col 2 = $5$ | col 1 = $6$ | $90$ | $-$ |
| 5 | col 1 = $4$ | col 3 = $7$ | col 2 = $0$ | $0$ | $-$ |
| 6 | col 2 = $1$ | col 1 = $2$ | col 3 = $8$ | $16$ | $-$ |

$$\det(A) = (160 + 42 + 0) - (90 + 0 + 16) = 96$$

¿Por qué unas van con $+$ y otras con $-$? La regla de los signos tiene que ver con permutaciones y no hace falta saberla. La **regla de Sarrus** (abajo) te da los 6 productos con sus signos correctos de forma visual, sin pensar.

> "Sinceramente no me la sé de memoria"

**Traducción:** Ni el profesor se la sabe de memoria. Sarrus resuelve todo.

---

### Regla de Sarrus (solo para $3 \times 3$ — esto es muy importante)

> "Tengan presente que la regla de Sarrus solo para matrices 3x3. He visto varias veces en parciales que aplican la regla de Sarrus para matrices 4x4 o otras dimensiones, no sea 3x3, y está mal"

**Traducción:** Sarrus **SOLAMENTE funciona para matrices $3 \times 3$**. Si la matriz es $4 \times 4$ o más grande, Sarrus no sirve. Esto aparece como error en parciales.

#### ¿Cómo funciona Sarrus?

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

**Paso 2:** Las 3 diagonales ↘ arrancan desde la **columna 1**, una en cada fila (filas 1, 2 y 3). Van con $+$:

```
 [a₁₁] a₁₂   a₁₃       ↘ desde fila 1: a₁₁ · a₂₂ · a₃₃
  a₂₁ [a₂₂]  a₂₃
  a₃₁  a₃₂  [a₃₃]
  a₁₁  a₁₂   a₁₃
  a₂₁  a₂₂   a₂₃

  a₁₁  a₁₂   a₁₃       ↘ desde fila 2: a₂₁ · a₃₂ · a₁₃
 [a₂₁] a₂₂   a₂₃
  a₃₁ [a₃₂]  a₃₃
  a₁₁  a₁₂  [a₁₃]  ← esta es la copia de fila 1
  a₂₁  a₂₂   a₂₃

  a₁₁  a₁₂   a₁₃       ↘ desde fila 3: a₃₁ · a₁₂ · a₂₃
  a₂₁  a₂₂   a₂₃
 [a₃₁] a₃₂   a₃₃
  a₁₁ [a₁₂]  a₁₃   ← copia de fila 1
  a₂₁  a₂₂  [a₂₃]  ← copia de fila 2
```

**Paso 3:** Las 3 diagonales ↙ arrancan desde la **columna 3**, una en cada fila (filas 1, 2 y 3). Van con $-$:

```
  a₁₁  a₁₂  [a₁₃]      ↙ desde fila 1: a₁₃ · a₂₂ · a₃₁
  a₂₁ [a₂₂]  a₂₃
 [a₃₁] a₃₂   a₃₃
  a₁₁  a₁₂   a₁₃
  a₂₁  a₂₂   a₂₃

  a₁₁  a₁₂   a₁₃       ↙ desde fila 2: a₂₃ · a₃₂ · a₁₁
  a₂₁  a₂₂  [a₂₃]
  a₃₁ [a₃₂]  a₃₃
 [a₁₁] a₁₂   a₁₃   ← copia de fila 1
  a₂₁  a₂₂   a₂₃

  a₁₁  a₁₂   a₁₃       ↙ desde fila 3: a₃₃ · a₁₂ · a₂₁
  a₂₁  a₂₂   a₂₃
  a₃₁  a₃₂  [a₃₃]
  a₁₁ [a₁₂]  a₁₃   ← copia de fila 1
 [a₂₁] a₂₂   a₂₃   ← copia de fila 2
```

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

**Paso 2:** Diagonales positivas (↘), arrancando desde columna 1:

```
 [1] 0  2       ↘ desde fila 1: 1·0·1 = 0
  1 [0] 1
  0  1 [1]
  1  0  2
  1  0  1

  1  0  2       ↘ desde fila 2: 1·1·2 = 2
 [1] 0  1
  0 [1] 1
  1  0 [2]
  1  0  1

  1  0  2       ↘ desde fila 3: 0·0·1 = 0
  1  0  1
 [0] 1  1
  1 [0] 2
  1  0 [1]
```

Suma: $0 + 2 + 0 = 2$

**Paso 3:** Diagonales negativas (↙), arrancando desde columna 3:

```
  1  0 [2]      ↙ desde fila 1: 2·0·0 = 0
  1 [0] 1
 [0] 1  1
  1  0  2
  1  0  1

  1  0  2       ↙ desde fila 2: 1·1·1 = 1
  1  0 [1]
  0 [1] 1
 [1] 0  2
  1  0  1

  1  0  2       ↙ desde fila 3: 1·0·1 = 0
  1  0  1
  0  1 [1]
  1 [0] 2
 [1] 0  1
```

Suma: $0 + 1 + 0 = 1$

**Paso 4:** $\det(A) = 2 - 1 = 1$

---

### Método recursivo (para matrices de cualquier tamaño)

> "Precisamos ahora un método que nos sirva para matrices n por n"

**Traducción:** Sarrus solo funciona para $3 \times 3$. Para $4 \times 4$ o más necesitamos otro método.

#### La idea en una oración

Convertir un determinante grande en varios determinantes más chicos. Un determinante de $4 \times 4$ se convierte en varios de $3 \times 3$ (que ya sabés hacer con Sarrus). Uno de $3 \times 3$ se convierte en varios de $2 \times 2$ (que son triviales).

---

#### Paso 1: Aprender a "borrar" una fila y una columna (esto se llama "menor")

> "La matriz adjunta del elemento ij de A surge de quitarle a la matriz A la fila i y la columna j"

Antes de ver el método completo, necesitás saber hacer una sola cosa: dada una matriz, **tachar una fila entera y una columna entera**, y quedarte con lo que sobra. Lo que sobra se llama **menor**.

**Ejemplo:** Partimos de esta matriz $3 \times 3$:

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$$

Vamos a borrar la fila 2 y la columna 2 (donde está el $5$):

```
Antes:                  Tachamos fila 2 y col 2:       Queda:

| 1  2  3 |             | 1  ✕  3 |                    | 1  3 |
| 4  5  6 |      →      | ✕  ✕  ✕ |              →     | 7  9 |
| 7  8  9 |             | 7  ✕  9 |
```

La menor es $\begin{pmatrix} 1 & 3 \\ 7 & 9 \end{pmatrix}$. Es una $2 \times 2$ (una dimensión menos que la original).

**Otro ejemplo:** Borramos fila 1 y columna 3 (donde está el $3$):

```
Antes:                  Tachamos fila 1 y col 3:       Queda:

| 1  2  3 |             | ✕  ✕  ✕ |                    | 4  5 |
| 4  5  6 |      →      | 4  5  ✕ |              →     | 7  8 |
| 7  8  9 |             | 7  8  ✕ |
```

La menor es $\begin{pmatrix} 4 & 5 \\ 7 & 8 \end{pmatrix}$.

Eso es todo lo que es una menor: **tachar una fila y una columna, quedarte con el resto**.

---

#### Paso 2: El método completo (receta)

1. **Elegí una fila** (cualquiera, el resultado es el mismo)
2. **Recorré cada elemento de esa fila**, y para cada uno hacé:
   - Anotá el **número** que hay en esa posición
   - Calculá la **menor**: borrá la fila y columna de ese elemento, y sacá el determinante de lo que queda
   - Multiplicá el número por el determinante de la menor
   - Asignale un **signo** ($+$ o $-$) — esto se explica en el ejemplo de abajo
3. **Sumá** todos los resultados
4. Eso es el determinante

---

#### Ejemplo completo, paso a paso

$$A = \begin{pmatrix} 1 & 0 & 2 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$$

Elegimos la **fila 1**: sus elementos son $1$, $0$, $2$.

**Antes de arrancar: ¿cómo sé el signo de cada elemento?**

Cada posición tiene un signo fijo. Empezás con $+$ en la esquina superior izquierda y vas alternando como un tablero de ajedrez:

```
| +  -  + |
| -  +  - |
| +  -  + |
```

Posición $(1,1)$ → $+$, posición $(1,2)$ → $-$, posición $(1,3)$ → $+$, etc. Siempre es el mismo patrón. Ahora sí, el ejemplo:

**Elemento 1: el $1$ que está en la posición $(1,1)$**

- Número: $1$
- Signo de $(1,1)$: miramos el tablero → $+$
- Menor: borramos fila 1 y columna 1:

```
| ✕  ✕  ✕ |           | 0  1 |
| 1  0  1 |     →     | 1  1 |
| 0  1  1 |
```

- Determinante de la menor: $0 \cdot 1 - 1 \cdot 1 = -1$
- Resultado de este elemento: $1 \cdot (+1) \cdot (-1) = -1$

**Elemento 2: el $0$ que está en la posición $(1,2)$**

- Número: $0$
- Como el número es $0$, todo el resultado va a ser $0$ sin importar el signo ni la menor. No hace falta calcular nada más.
- Resultado: $0$

**Elemento 3: el $2$ que está en la posición $(1,3)$**

- Número: $2$
- Signo de $(1,3)$: miramos el tablero → $+$
- Menor: borramos fila 1 y columna 3:

```
| ✕  ✕  ✕ |           | 1  0 |
| 1  0  ✕ |     →     | 0  1 |
| 0  1  ✕ |
```

- Determinante de la menor: $1 \cdot 1 - 0 \cdot 0 = 1$
- Resultado de este elemento: $2 \cdot (+1) \cdot 1 = 2$

**Sumamos:** $-1 + 0 + 2 = 1$ ← coincide con Sarrus.

---

#### Truco: elegí la fila o columna con más ceros

> "Siempre sirve lo más fácil es desarrollar por la fila o columna que presente la mayor cantidad de ceros, así tengo que calcular la menor cantidad de matrices adjuntas"

**Traducción:** Cuando un elemento es $0$, su resultado es $0$ sin hacer cuentas. Así que cuantos más ceros tenga la fila que elegís, menos menores tenés que calcular.

En nuestra matriz, la **columna 2** es $(0, 0, 1)$ — tiene dos ceros. Si desarrollamos por columna 2 en vez de fila 1, solo hay que calcular UNA menor (la del $1$):

- El $0$ en $(1,2)$: resultado $0$
- El $0$ en $(2,2)$: resultado $0$
- El $1$ en $(3,2)$: signo del tablero → $-$, menor $= \begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix}$, $\det = 1-2 = -1$

$$\det(A) = 0 + 0 + 1 \cdot (-1) \cdot (-1) = 1$$

Mismo resultado, mucho menos trabajo.

---

#### Para matrices $4 \times 4$

> "Si es 4x4, ahí sí, ya no le va a quedar otra que desarrollar por una fila o columna"

Es exactamente el mismo procedimiento:
1. Elegís la fila o columna con más ceros
2. Para cada elemento, borrás su fila y columna → te queda una menor de $3 \times 3$
3. A cada menor $3 \times 3$ le calculás el determinante con Sarrus

#### Da igual qué fila o columna elijas

> "No importa por qué fila o columna desarrollemos, siempre el resultado del determinante me da lo mismo"

**Traducción:** Podés elegir **cualquier** fila o columna. Siempre da lo mismo. Elegí la que tenga más ceros.

---

## Las 9 propiedades del determinante (atajos para el parcial)

Estas propiedades son **atajos**. En vez de calcular un determinante desde cero (lo cual puede llevar mucho tiempo), las propiedades te dejan manipular la matriz para simplificarla, o te dicen el resultado directamente. Cada propiedad viene con un "¿cuándo la uso?" para que sepas cuándo aplicarla.

---

### Propiedad 1: Sumandos en una fila se pueden separar

**¿Qué dice?** Si en una fila (o columna) cada entrada tiene dos sumandos, podés separar el determinante en la suma de dos determinantes: uno con los primeros sumandos y otro con los segundos. El resto de la matriz no se toca.

**¿Cuándo la uso?** Cuando ves que las entradas de una fila son sumas de cosas, y te conviene separarlas.

**Ejemplo en $2 \times 2$:**

$$\det\begin{pmatrix} 1+1 & 3+0 \\ 4 & 4 \end{pmatrix} = \det\begin{pmatrix} 1 & 3 \\ 4 & 4 \end{pmatrix} + \det\begin{pmatrix} 1 & 0 \\ 4 & 4 \end{pmatrix}$$

Verificación:
- Izquierda: $\det\begin{pmatrix} 2 & 3 \\ 4 & 4 \end{pmatrix} = 8 - 12 = -4$
- Derecha: $(4 - 12) + (4 - 0) = -8 + 4 = -4$
- Coincide.

---

### Propiedad 2: Factor común de una fila sale multiplicando

**¿Qué dice?** Si todas las entradas de una fila (o columna) están multiplicadas por un número $k$, podés "sacar" ese $k$ fuera del determinante.

$$\det(\text{matriz con fila } i \text{ multiplicada por } k) = k \cdot \det(A)$$

**Analogía:** Es como sacar factor común con números. Si tenés $2 \cdot 5 - 2 \cdot 3$, sacás el $2$: $2 \cdot (5 - 3)$. Acá es lo mismo pero con una fila entera.

**¿Cuándo la uso?** Cuando ves que toda una fila tiene un factor en común. Lo sacás afuera y la matriz queda más simple.

**Ejemplo:**

$$\det\begin{pmatrix} 2 & 2 \\ 4 & 8 \end{pmatrix} = 2 \cdot \det\begin{pmatrix} 1 & 1 \\ 4 & 8 \end{pmatrix}$$

Verificación:
- Izquierda: $16 - 8 = 8$
- Derecha: $2 \cdot (8 - 4) = 2 \cdot 4 = 8$
- Coincide.

---

### Propiedad 3: Factor común de TODA la matriz sale elevado a $n$

**¿Qué dice?** Si toda la matriz está multiplicada por un escalar $k$, entonces:

$$\det(k \cdot A) = k^n \cdot \det(A)$$

donde $n$ es la dimensión de la matriz.

> "La propiedad 3 no es más que aplicar n veces la propiedad 2"

**Traducción:** Si $k$ multiplica toda la matriz, eso significa que cada una de las $n$ filas está multiplicada por $k$. Sacando $k$ de cada fila (propiedad 2, aplicada $n$ veces), el $k$ sale elevado a la $n$.

**¿Cuándo la uso?** Cuando ves algo como $\det(3A)$ o $\det(-A)$ en un ejercicio.

**Ejemplo:** Si $A$ es $3 \times 3$ y $\det(A) = 5$:

$$\det(4A) = 4^3 \cdot \det(A) = 64 \cdot 5 = 320$$

**Error común en parciales:** Pensar que $\det(4A) = 4 \cdot \det(A)$. **NO.** El escalar sale elevado a la dimensión, no multiplicando.

| Dimensión | $\det(kA)$ |
|-----------|-----------|
| $2 \times 2$ | $k^2 \cdot \det(A)$ |
| $3 \times 3$ | $k^3 \cdot \det(A)$ |
| $5 \times 5$ | $k^5 \cdot \det(A)$ |

---

### Propiedad 4: Determinante de un producto = producto de determinantes

**¿Qué dice?**

$$\det(A \cdot B) = \det(A) \cdot \det(B)$$

> "No significa que B por A sea lo mismo que A por B. Pero el determinante sí es el mismo"

**Traducción:** Las matrices $A \cdot B$ y $B \cdot A$ son matrices distintas (el producto no conmuta). Pero cuando les calculás el determinante, el número que sale es el mismo, porque $\det(A) \cdot \det(B)$ es una multiplicación de números reales, y esa sí conmuta.

**¿Cuándo la uso?** Cuando ves un determinante de un producto de matrices, o cuando necesitás calcular $\det(A^3)$, que es $\det(A) \cdot \det(A) \cdot \det(A) = \det(A)^3$.

**Ejemplo:** $\det(A) = 1$, $\det(B) = 2 \implies \det(A \cdot B) = 1 \cdot 2 = 2$.

**Verificación con matrices concretas:**

$$A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$$

$\det(A) = 1 \cdot 1 - 0 \cdot 2 = 1$, $\det(B) = 2 \cdot 1 - 0 \cdot 0 = 2$.

$$A \cdot B = \begin{pmatrix} 2 & 2 \\ 0 & 1 \end{pmatrix} \implies \det(A \cdot B) = 2 - 0 = 2 = 1 \cdot 2 \quad \checkmark$$

---

### Propiedad 5: Dos filas o columnas iguales → determinante es 0

**¿Qué dice?** Si una matriz tiene dos filas iguales entre sí (o dos columnas iguales entre sí), su determinante vale $0$ automáticamente.

> "Esta propiedad es un poco parecido al caso que les decía, en un parcial si ustedes ven una matriz de 7x7, bueno, capaz que un compañero se tira a hacer las cuentas y otro se da cuenta que la fila 1 es igual a la fila 5 y el determinante vale 0"

**Traducción:** Antes de hacer ninguna cuenta, **siempre mirá si hay filas o columnas repetidas**. Si las hay, el determinante es $0$ sin hacer nada. Esto te puede ahorrar mucho tiempo en el parcial.

**¿Cuándo la uso?** Siempre como primer chequeo antes de calcular. También aparece dentro de demostraciones (como cuando querés probar que algo vale 0).

**Ejemplo:**

$$\det\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 1 & 2 & 3 \end{pmatrix} = 0$$

La fila 1 y la fila 3 son iguales $(1, 2, 3)$, así que el determinante es $0$ sin hacer una sola cuenta.

**Aclaración:** Tiene que ser fila con fila, o columna con columna. Si una fila es igual a una columna, esta propiedad **no aplica**.

---

### Propiedad 6: Intercambiar dos filas o columnas cambia el signo

**¿Qué dice?** Si agarrás una matriz y le intercambiás dos filas (o dos columnas), el determinante cambia de signo: si era positivo, pasa a negativo, y viceversa.

$$\det(B) = -\det(A)$$

donde $B$ es la misma matriz que $A$ pero con dos filas (o columnas) intercambiadas.

**¿Cuándo la uso?** Cuando querés reorganizar una matriz para facilitar el cálculo y necesitás saber cómo eso afecta el determinante.

**Ejemplo:**

$$A = \begin{pmatrix} 3 & 2 & 4 \\ 4 & 6 & 8 \\ 1 & 1 & 6 \end{pmatrix} \implies B = \begin{pmatrix} 1 & 1 & 6 \\ 4 & 6 & 8 \\ 3 & 2 & 4 \end{pmatrix}$$

$B$ se obtuvo intercambiando la fila 1 con la fila 3 de $A$. Entonces $\det(B) = -\det(A)$.

---

### Propiedad 7: Sumar combinación lineal de filas NO cambia el determinante (la más útil)

**¿Qué dice?** Si a una fila le sumás un múltiplo de otra fila (o una combinación de varias filas), el determinante no cambia.

**Analogía:** Es como si tuvieras una receta y le agregaras "0 de sabor" — por más que mezcles filas con otras, si no multiplicás la fila que estás modificando por un número, el resultado no cambia.

> "Ven que hago lambda 1 por fila 1, lambda 2 por fila 2, llego a la fila j que no está multiplicada por nada. ¿Por qué? Porque si yo la multiplico por un número, el determinante queda multiplicado por ese número por la propiedad 2"

**Traducción:** La fila que estás modificando **no puede estar multiplicada** por un escalar. Solo le sumás múltiplos de las OTRAS filas. Si multiplicaras la fila en sí, estarías cambiando el determinante (por la propiedad 2).

**¿Cuándo la uso?** Para **generar ceros** en la matriz. Si lográs que una fila o columna tenga muchos ceros, calcular el determinante se vuelve más fácil (porque al desarrollar por esa fila, la mayoría de los términos desaparecen).

**Ejemplo:**

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$$

Hacemos $F_3 \leftarrow F_3 + 3 \cdot F_2 + 2 \cdot F_1$ (le sumamos a la fila 3 el triple de la fila 2 más el doble de la fila 1):

- Nueva entrada $(3,1)$: $7 + 3 \cdot 4 + 2 \cdot 1 = 7 + 12 + 2 = 21$
- Nueva entrada $(3,2)$: $8 + 3 \cdot 5 + 2 \cdot 2 = 8 + 15 + 4 = 27$
- Nueva entrada $(3,3)$: $9 + 3 \cdot 6 + 2 \cdot 3 = 9 + 18 + 6 = 33$

$$B = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 21 & 27 & 33 \end{pmatrix}$$

$\det(A) = \det(B)$. La matriz cambió, pero el determinante es el mismo.

---

### Propiedad 8: Transponer no cambia el determinante

**¿Qué dice?**

$$\det(A) = \det(A^T)$$

El determinante de una matriz es igual al determinante de su transpuesta.

**¿Cuándo la uso?** Cuando algo te conviene más en columnas que en filas, o viceversa.

**Consecuencia importantísima:** Como el determinante no cambia al transponer, **toda propiedad que vale para filas también vale para columnas**, y viceversa. Por eso cada propiedad dice "filas o columnas".

**Ejemplo:**

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \implies A^T = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$$

$\det(A) = 4 - 6 = -2$, $\det(A^T) = 4 - 6 = -2$. Son iguales.

---

### Propiedad 9: Matrices triangulares → multiplicar la diagonal y listo

**¿Qué dice?** Si la matriz es **triangular** (todos ceros debajo de la diagonal, o todos ceros arriba de la diagonal), el determinante es simplemente el **producto de los números de la diagonal principal**.

$$\det(A) = a_{11} \cdot a_{22} \cdot a_{33} \cdot \ldots \cdot a_{nn}$$

> "Si un compañero se da cuenta que es triangular superior y multiplica la diagonal principal, lo saca en 12 segundos"

**Traducción:** Este es el atajo más grande. Si la matriz es triangular, no hay que hacer ninguna expansión, ningún Sarrus, nada. Se multiplica la diagonal y listo.

**¿Cuándo la uso?** Siempre chequeá si la matriz es triangular antes de empezar a calcular. También combiná con la propiedad 7 (que sirve para generar ceros y convertir una matriz en triangular).

**Ejemplo — triangular superior** (ceros debajo de la diagonal):

$$A = \begin{pmatrix} 7 & 3 & 5 \\ 0 & 6 & 2 \\ 0 & 0 & 1 \end{pmatrix} \implies \det(A) = 7 \cdot 6 \cdot 1 = 42$$

**Ejemplo — diagonal** (caso particular de triangular):

$$A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 6 & 0 \\ 0 & 0 & 4 \end{pmatrix} \implies \det(A) = 2 \cdot 6 \cdot 4 = 48$$

**Consecuencia directa:** La identidad $I$ es diagonal con unos, así que $\det(I) = 1 \cdot 1 \cdot \ldots \cdot 1 = 1$.

---

### Resumen de las 9 propiedades

| # | Propiedad | Regla rápida | ¿Cuándo usarla? |
|---|-----------|-------------|-----------------|
| 1 | Sumandos en una fila | Se separa en suma de dos $\det$ | Cuando las entradas son sumas |
| 2 | Fila multiplicada por $k$ | $k$ sale multiplicando | Cuando hay factor común en una fila |
| 3 | Toda la matriz por $k$ | $\det(kA) = k^n \cdot \det(A)$ | Cuando ves $\det(kA)$ en un ejercicio |
| 4 | Producto de matrices | $\det(AB) = \det(A) \cdot \det(B)$ | Cuando ves $\det(A \cdot B)$ |
| 5 | Dos filas iguales | $\det = 0$ | Primer chequeo antes de calcular |
| 6 | Intercambio de filas | $\det$ cambia de signo | Cuando reorganizás la matriz |
| 7 | Comb. lineal a una fila | $\det$ no cambia | Para generar ceros y simplificar |
| 8 | Transpuesta | $\det(A) = \det(A^T)$ | Para pasar de filas a columnas |
| 9 | Triangular | $\det = $ producto de la diagonal | Atajo gigante si es triangular |

---

### Lo que NO es una propiedad: la suma

> "El determinante de A más B, en general, es distinto del determinante de A más el determinante de B"

$$\det(A + B) \neq \det(A) + \det(B) \quad \text{(en general)}$$

**Traducción:** Es tentador pensar que así como $\det(AB) = \det(A) \cdot \det(B)$ (propiedad 4), también valdría $\det(A + B) = \det(A) + \det(B)$. Pero **no**. Eso es falso.

**Contraejemplo:**

$$A = \begin{pmatrix} 1 & 3 \\ -1 & 2 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 5 \\ 1 & 1 \end{pmatrix}$$

$\det(A) = 2 - (-3) = 5$, $\det(B) = 1 - 5 = -4$, $\det(A) + \det(B) = 1$.

$$A + B = \begin{pmatrix} 2 & 8 \\ 0 & 3 \end{pmatrix} \implies \det(A + B) = 6 - 0 = 6$$

$6 \neq 1$. No se cumple.

---

## Ejercicio de clase: Determinante en función de $x$

### Enunciado

Calcular el determinante de una matriz $3 \times 3$ cuyas filas tienen factores comunes que involucran $x$.

### La idea del ejercicio

Las filas de la matriz tienen expresiones con $x$. En vez de expandir todo (que sería un quilombo), usamos la **propiedad 2** para sacar factores comunes de cada fila y simplificar la cuenta.

### Desarrollo

**Paso 1:** La fila 1 tiene factor $(x-1)$ en todas sus entradas (por ejemplo, $x^2 - 1 = (x+1)(x-1)$). Sacamos $(x-1)$ afuera por la propiedad 2.

**Paso 2:** La fila 2 tiene factor $x$ en todas sus entradas. Sacamos $x$ afuera.

**Paso 3:** La fila 3 tiene factor $(x-2)$ en todas sus entradas. Sacamos $(x-2)$ afuera.

**Paso 4:** Lo que queda adentro es una $3 \times 3$ más simple, que calculamos con Sarrus.

**Resultado:**

$$\det(A) = (x-1) \cdot x \cdot (x-2) \cdot (x+1)$$

> "Se podía hacer por Sarrus toda la expresión original, se podía desarrollar por fila o columna, y vamos a llegar a lo mismo, sí, pero aplicando acá la propiedad 2 se simplifica bastante"

**Traducción:** Siempre intentá simplificar antes de calcular. Sacar factores comunes (propiedad 2) es uno de los atajos más útiles.

---

## Ejercicio de clase: Determinante $4 \times 4$ con propiedades 1 y 5

### Enunciado

Se tiene una matriz $4 \times 4$ cuya cuarta columna se puede descomponer como suma de dos vectores columna, y cada uno coincide con otra columna de la matriz.

### Desarrollo

**Paso 1:** Usamos la **propiedad 1** en la columna 4 (que tiene dos sumandos). Esto separa un determinante en la suma de dos determinantes.

**Paso 2:** En el primer determinante, la columna 4 resultante es igual a la columna 1 → por **propiedad 5**, ese determinante vale $0$.

**Paso 3:** En el segundo determinante, la columna 4 resultante es igual a la columna 2 → por **propiedad 5**, ese determinante también vale $0$.

**Resultado:** $\det(A) = 0 + 0 = 0$.

> "Es importante dominarlas porque pueden facilitar temas de tiempos en un parcial"

---

# PARTE 2 — El teorema central y ejercicios (Clase 6, 8 de abril)

## La Gran Pregunta de Hoy: ¿Cómo se conectan "ser invertible" y "tener determinante distinto de cero"?

Hoy se demuestra formalmente algo que ya anticipamos: que si una matriz es invertible, su determinante es distinto de cero. Además se ve cómo calcular el determinante de la inversa. Después, ejercicios que combinan todas las propiedades.

---

## Conexión con la Clase Anterior

La clase 5 definió determinantes, vio los métodos de cálculo y las 9 propiedades. Hoy se cierra la teoría con un teorema y se practica. La semana que viene viene la otra dirección del teorema ($\det \neq 0 \implies$ invertible) y el método de cofactores para calcular la inversa.

---

## Teorema 1: Si una matriz es invertible, su determinante es distinto de cero

### ¿Qué dice este teorema?

Si $A$ es invertible (es decir, tiene inversa), entonces:
1. $\det(A) \neq 0$ (el determinante no puede ser cero)
2. $\det(A^{-1}) = \dfrac{1}{\det(A)}$ (el determinante de la inversa es 1 dividido el determinante original)

### ¿Por qué importa?

Porque nos da un **criterio rápido**. Si calculamos el determinante y nos da $0$, sabemos que la matriz NO es invertible, sin tener que intentar calcular la inversa.

### Demostración (es cortita y usa las propiedades que ya vimos)

> "Por la definición de inversa, si A es invertible, significa que existe una matriz A a la menos 1, tal que A por A a la menos 1 me da la identidad"

**Paso 1:** Si $A$ es invertible, existe $A^{-1}$ tal que:

$$A \cdot A^{-1} = I$$

Esto es la **definición** de inversa, nada nuevo.

**Paso 2:** Tomamos el determinante de ambos lados de la ecuación:

$$\det(A \cdot A^{-1}) = \det(I)$$

**Paso 3:** Del lado izquierdo usamos la **propiedad 4** ($\det$ del producto = producto de $\det$):

$$\det(A) \cdot \det(A^{-1}) = \det(I)$$

**Paso 4:** Del lado derecho: $\det(I) = 1$ (la identidad es diagonal con unos, propiedad 9). Entonces:

$$\det(A) \cdot \det(A^{-1}) = 1$$

**Paso 5:** Ahora pensemos. Tenemos dos números que multiplicados dan $1$. ¿Puede alguno de ellos ser $0$? No, porque $0$ multiplicado por cualquier cosa da $0$, no $1$. Entonces:

$$\det(A) \neq 0 \quad \blacksquare$$

**Paso 6:** Además, si $\det(A) \cdot \det(A^{-1}) = 1$, podemos despejar:

$$\det(A^{-1}) = \frac{1}{\det(A)} \quad \blacksquare$$

**Analogía:** Es exactamente como con números: si $a \cdot b = 1$, entonces ni $a$ ni $b$ pueden ser cero, y $b = \frac{1}{a}$.

---

## Ejercicio 1: Calcular determinantes usando propiedades

### Enunciado

$A$ y $B$ son matrices $2 \times 2$. $\det(A) = 2$. $B = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.

Calcular: (a) $\det(3A^3 \cdot B^T)$, (b) $\det((2A)^{-1})$, (c) $\det(2 \cdot A^{-1})$.

### Dato previo

$\det(B) = 2 \cdot 2 - 0 \cdot 1 = 4$.

### Parte (a): $\det(3A^3 \cdot B^T)$

Esto parece complicado, pero vamos paso a paso aplicando propiedades:

**Paso 1 — Propiedad 4** (el $\det$ del producto es el producto de los $\det$):

$$\det(3A^3 \cdot B^T) = \det(3A^3) \cdot \det(B^T)$$

**Paso 2 — Propiedad 3** (sacar el $3$ de la primera):

$3A^3$ es la matriz $A^3$ multiplicada por el escalar $3$. Como $A$ es $2 \times 2$:

$$\det(3A^3) = 3^2 \cdot \det(A^3) = 9 \cdot \det(A^3)$$

El exponente es $2$ (no $3$) porque $A$ es $2 \times 2$.

**Paso 3 — Propiedad 4** (de nuevo, para separar $A^3 = A \cdot A \cdot A$):

$$\det(A^3) = \det(A)^3 = 2^3 = 8$$

**Paso 4 — Propiedad 8** (la transpuesta no cambia el determinante):

$$\det(B^T) = \det(B) = 4$$

**Resultado:**

$$\det(3A^3 \cdot B^T) = 9 \cdot 8 \cdot 4 = 288$$

### Parte (b): $\det((2A)^{-1})$

Acá tenemos la inversa de la matriz $2A$ (primero multiplicamos $A$ por $2$, y después le buscamos la inversa a eso).

**Paso 1 — Teorema 1** (el determinante de la inversa es $1$ dividido el determinante):

$$\det((2A)^{-1}) = \frac{1}{\det(2A)}$$

**Paso 2 — Propiedad 3:**

$$\det(2A) = 2^2 \cdot \det(A) = 4 \cdot 2 = 8$$

**Resultado:**

$$\det((2A)^{-1}) = \frac{1}{8}$$

### Parte (c): $\det(2 \cdot A^{-1})$

> "Se entiende la diferencia, ¿no? Acá puedo aplicar el teorema porque está todo invertido. Acá es la inversa por 2"

**Traducción:** Esto NO es lo mismo que la parte (b). En la parte (b), primero se multiplica por $2$ y después se invierte: $(2A)^{-1}$. Acá, primero se invierte y después se multiplica por $2$: $2 \cdot A^{-1}$. Son cosas distintas.

**Paso 1 — Propiedad 3** (sacar el $2$):

$$\det(2 \cdot A^{-1}) = 2^2 \cdot \det(A^{-1}) = 4 \cdot \det(A^{-1})$$

**Paso 2 — Teorema 1:**

$$\det(A^{-1}) = \frac{1}{\det(A)} = \frac{1}{2}$$

**Resultado:**

$$\det(2 \cdot A^{-1}) = 4 \cdot \frac{1}{2} = 2$$

### Comparación de las tres partes

| Expresión | Resultado | Propiedades usadas |
|-----------|-----------|-------------------|
| $\det(3A^3 \cdot B^T)$ | $288$ | P4, P3, P4, P8 |
| $\det((2A)^{-1})$ | $\frac{1}{8}$ | Teorema 1, P3 |
| $\det(2 \cdot A^{-1})$ | $2$ | P3, Teorema 1 |

---

## Ejercicio 2: Probar $\det(A) = \det(B)$ sin usar propiedad 7

### Enunciado

La matriz $B$ difiere de $A$ solo en la fila 2: la fila 2 de $B$ es la fila 2 de $A$ más un múltiplo de la fila 1. Probar que $\det(A) = \det(B)$ sin usar directamente la propiedad 7.

### ¿Cuál es el punto de este ejercicio?

Mostrar que la propiedad 7 se puede **deducir** de las propiedades 1, 2 y 5. Es un ejercicio de práctica con propiedades.

### Desarrollo

**Paso 1 — Propiedad 1:** La fila 2 de $B$ tiene dos sumandos (la fila 2 original + $k$ veces la fila 1). Separamos en dos determinantes:

$$\det(B) = \det(A) + \det(C)$$

donde $C$ es una matriz que tiene la fila 1 de $A$ como fila 1, y $k$ veces la fila 1 de $A$ como fila 2 (y el resto igual).

**Paso 2 — Propiedad 2:** En $C$, la fila 2 es $k$ veces la fila 1. Sacamos el $k$:

$$\det(C) = k \cdot \det(C')$$

donde $C'$ tiene la fila 1 repetida en la fila 2 (las dos filas son iguales).

**Paso 3 — Propiedad 5:** $C'$ tiene fila 1 = fila 2, así que $\det(C') = 0$.

**Conclusión:** $\det(B) = \det(A) + k \cdot 0 = \det(A) \quad \blacksquare$

> "Era para mostrarles el ejemplo y cómo aplicar las propiedades. La propiedad 7 básicamente se deduce de las propiedades 1, 2 y 5"

---

## Ejercicio 3: Valores posibles del determinante cuando $A^3 = A$

### Enunciado

Sea $A \in M_{n \times n}(\mathbb{R})$ tal que $A^3 = A$. Hallar los posibles valores de $\det(A)$.

### Desarrollo

**Paso 1:** Tomamos determinante de ambos lados de $A^3 = A$:

$$\det(A^3) = \det(A)$$

**Paso 2:** Por la propiedad 4: $\det(A^3) = \det(A)^3$. Entonces:

$$\det(A)^3 = \det(A)$$

**Paso 3:** Esto ya es una ecuación con números (no con matrices). Llamemos $x = \det(A)$:

$$x^3 = x$$

$$x^3 - x = 0$$

$$x(x^2 - 1) = 0$$

$$x(x-1)(x+1) = 0$$

**Paso 4:** Un producto de factores es cero cuando al menos uno de ellos es cero:
- $x = 0$, o
- $x - 1 = 0 \implies x = 1$, o
- $x + 1 = 0 \implies x = -1$

**Resultado:** Los posibles valores de $\det(A)$ son $\{0, \; 1, \; -1\}$.

### Parte 2: ¿Existen matrices reales para cada valor?

Sí. Acá van ejemplos:

| Valor de $\det(A)$ | Ejemplo | ¿Cumple $A^3 = A$? |
|---------------------|---------|---------------------|
| $0$ | La matriz nula $O$ | $O^3 = O \quad \checkmark$ |
| $1$ | La identidad $I$ | $I^3 = I \quad \checkmark$ |
| $-1$ | $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | $A^3 = A \quad \checkmark$, $\det(A) = -1$ |

---

## Ejercicio 4: Determinante complejo con matrices dadas

### Enunciado

$A = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$ (diagonal), $B$ invertible $3 \times 3$, $C = B^{-1}AB$.

Dada la ecuación: $\det(C - AC) + \det((2A + A^T) \cdot A^{-1}) + \det(C \cdot D) = 0$.

Calcular $\det(D)$.

### Desarrollo

Este ejercicio parece intimidante, pero es cuestión de ir paso a paso usando las propiedades.

**Dato previo:** $A$ es diagonal, así que por la **propiedad 9**: $\det(A) = 2 \cdot 2 \cdot 3 = 12$.

**Cálculo de $\det(C)$:**

$C = B^{-1}AB$. Por la **propiedad 4**:

$$\det(C) = \det(B^{-1}) \cdot \det(A) \cdot \det(B)$$

Por el **Teorema 1**: $\det(B^{-1}) = \frac{1}{\det(B)}$. Entonces:

$$\det(C) = \frac{1}{\det(B)} \cdot \det(A) \cdot \det(B) = \det(A) = 12$$

Los $\det(B)$ se cancelan. El determinante de $C$ es igual al de $A$.

**Término 1: $\det(C - AC)$**

Primero factorizamos: $C - AC = (I - A) \cdot C$.

Por **propiedad 4**: $\det((I-A) \cdot C) = \det(I - A) \cdot \det(C)$

Calculamos $I - A$:

$$I - A = \begin{pmatrix} 1-2 & 0 & 0 \\ 0 & 1-2 & 0 \\ 0 & 0 & 1-3 \end{pmatrix} = \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{pmatrix}$$

Es diagonal, así que $\det(I - A) = (-1)(-1)(-2) = -2$.

Término 1 $= -2 \cdot 12 = -24$.

**Término 2: $\det((2A + A^T) \cdot A^{-1})$**

Como $A$ es diagonal, $A^T = A$ (la transpuesta de una diagonal es ella misma). Entonces el profesor llegó en clase a que la expresión se simplifica a $4I$:

$\det(4I) = 4^3 \cdot \det(I) = 64 \cdot 1 = 64$.

Término 2 $= 64$.

**Término 3: $\det(C \cdot D)$**

Por **propiedad 4**: $\det(C \cdot D) = \det(C) \cdot \det(D) = 12 \cdot \det(D)$.

**Despeje:**

$$-24 + 64 + 12 \cdot \det(D) = 0$$

$$40 + 12 \cdot \det(D) = 0$$

$$12 \cdot \det(D) = -40$$

$$\det(D) = \frac{-40}{12} = -\frac{10}{3}$$

---

## Ejercicio 5: Probar que un determinante es par sin calcularlo

### Enunciado

Se tiene una matriz $4 \times 4$ con entradas enteras. Probar que $\det(A)$ es un número par.

### La idea

No podemos calcular el determinante (no nos dan números concretos). Pero podemos usar las propiedades para demostrar que **tiene** que ser par.

### Desarrollo

**Paso 1 — Propiedad 7:** Aplicamos una combinación lineal en la columna 2 (sumamos la columna 4 a la columna 2). El determinante no cambia.

**Paso 2:** Después de la operación, todas las entradas de la columna 2 resultan ser números pares (por cómo están construidas las entradas originales en el enunciado concreto).

**Paso 3 — Propiedad 2:** Como toda la columna 2 tiene factor $2$, lo sacamos afuera:

$$\det(A) = 2 \cdot \det(A')$$

**Paso 4:** $A'$ tiene entradas enteras (sumas y productos de enteros dan entero), así que $\det(A')$ es un entero. Llamémoslo $k$.

$$\det(A) = 2 \cdot k \quad \text{con } k \in \mathbb{Z}$$

Un número que es $2$ veces un entero es, por definición, **par**. $\blacksquare$

---

## Resultado extra: las matrices nilpotentes tienen determinante 0

### Enunciado

Si $A$ es nilpotente (o sea, $A^k = O$ para algún $k$), entonces $\det(A) = 0$.

### Demostración

Sabemos que $A^k = O$ (la nula). Tomamos determinante:

$$\det(A^k) = \det(O) = 0$$

Por la **propiedad 4**: $\det(A^k) = \det(A)^k$. Entonces:

$$\det(A)^k = 0$$

¿Qué número elevado a cualquier potencia da $0$? Solamente el $0$:

$$\det(A) = 0 \quad \blacksquare$$

**Consecuencia:** Toda matriz nilpotente es **no invertible** (porque su determinante es $0$ y el Teorema 1 dice que si fuera invertible, el determinante sería $\neq 0$).

---

## Resultado extra: matrices antisimétricas de dimensión impar tienen determinante 0

### Recordatorio: ¿qué es antisimétrica?

Una matriz es **antisimétrica** si $A^T = -A$ (la transpuesta es el negativo de la original).

### Enunciado

Si $A$ es antisimétrica y la dimensión $n$ es impar, entonces $\det(A) = 0$.

### Demostración — Parte 1: una igualdad general

Partimos de $A^T = -A$. Tomamos determinante de ambos lados:

$$\det(A^T) = \det(-A)$$

Lado izquierdo — por la **propiedad 8**: $\det(A^T) = \det(A)$.

Lado derecho — por la **propiedad 3**: $\det(-A) = (-1)^n \cdot \det(A)$.

Igualando:

$$\det(A) = (-1)^n \cdot \det(A)$$

### Demostración — Parte 2: si $n$ es impar

Si $n$ es impar (1, 3, 5, 7...), entonces $(-1)^n = -1$. Reemplazamos:

$$\det(A) = -\det(A)$$

Pasamos $\det(A)$ al otro lado:

$$\det(A) + \det(A) = 0$$

$$2 \cdot \det(A) = 0$$

$$\det(A) = 0 \quad \blacksquare$$

**Traducción final:** Toda matriz antisimétrica de dimensión impar ($3 \times 3$, $5 \times 5$, $7 \times 7$, ...) tiene determinante $0$ y por lo tanto es **no invertible**.

---

# PARTE 3 — Teorema 2, inversa por cofactores, demostraciones (Clase 7, 14 de abril)

## La Gran Pregunta de Hoy: Si el determinante es distinto de cero, ¿la matriz es invertible? ¿Y cómo calculo la inversa con el determinante?

En la clase 6 demostramos que si una matriz es invertible, su determinante es $\neq 0$. Hoy se demuestra **la vuelta**: si el determinante es $\neq 0$, entonces la matriz ES invertible. Además, se ve una nueva forma de calcular la inversa usando el determinante y los cofactores. Después, demostraciones de las propiedades (para parcial/examen, no para la evaluación de mañana).

---

## Conexión con la Clase Anterior

La clase 6 cerró con el Teorema 1: invertible $\implies \det \neq 0$. Hoy se completa la otra dirección ($\det \neq 0 \implies$ invertible) y se cierra todo el teórico de determinantes.

---

## Teorema 2: Si $\det(A) \neq 0$, entonces $A$ es invertible

### ¿Qué dice este teorema?

> "Lo que nos dice el teorema es que sea n por n, el determinante de A es distinto de cero, entonces A es invertible"

Con el Teorema 1 (clase 6) y el Teorema 2 (hoy), queda establecido el **"si y solo si"**:

> "Quédense con el si solo si. Matriz invertible, determinante distinto de cero, determinante distinto de cero, matriz invertible."

| Dirección | Enunciado | ¿Dónde se demostró? |
|-----------|-----------|---------------------|
| → | Si $A$ es invertible, entonces $\det(A) \neq 0$ | Teorema 1 (clase 6) |
| ← | Si $\det(A) \neq 0$, entonces $A$ es invertible | Teorema 2 (hoy) |

**Traducción:** Ser invertible y tener determinante distinto de cero son **exactamente lo mismo**. Saber una cosa es saber la otra.

### Además: nueva fórmula para calcular la inversa

El Teorema 2 no solo dice que la inversa existe — también dice cómo calcularla:

$$A^{-1} = \frac{1}{\det(A)} \cdot C_A^T$$

**¿Qué significa cada parte?**

- $A^{-1}$: la inversa que queremos encontrar
- $\frac{1}{\det(A)}$: uno dividido el determinante (por eso necesitamos que sea $\neq 0$)
- $C_A$: la **matriz de cofactores** de $A$ (se explica abajo)
- $C_A^T$: la matriz de cofactores **transpuesta**

---

## Qué es la matriz de cofactores

### Paso 1: Qué es un cofactor

El **cofactor** de la posición $(i,j)$ es un número que se calcula así:

1. Tomás el **signo** de esa posición (el tablero de ajedrez: $(-1)^{i+j}$)
2. Calculás el **determinante de la menor** (borrás fila $i$ y columna $j$, y sacás el determinante de lo que queda)
3. Multiplicás el signo por el determinante de la menor

$$C_{ij} = (-1)^{i+j} \cdot \det(M_{ij})$$

Es exactamente lo que ya hacías en el método recursivo, pero ahora tiene nombre: **cofactor**.

### Paso 2: La matriz de cofactores

La **matriz de cofactores** $C_A$ es una matriz del mismo tamaño que $A$, donde cada entrada es el cofactor de esa posición. Si $A$ es $3 \times 3$, la matriz de cofactores tiene 9 entradas ($C_{11}$, $C_{12}$, ..., $C_{33}$).

### Paso 3: Transponer y multiplicar

Una vez que tenés la matriz de cofactores, la transponés (intercambiás filas por columnas) y multiplicás cada entrada por $\frac{1}{\det(A)}$. El resultado es $A^{-1}$.

---

## Ejemplo completo: inversa por cofactores

> "Vamos a ver un ejemplo igual para bajar la tierra a esto"

$$A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 2 & 4 \\ 1 & 3 & -3 \end{pmatrix}$$

### Paso 1: Calcular $\det(A)$ con Sarrus

Copiamos filas 1 y 2 abajo y hacemos Sarrus:

Diagonales positivas: $1 \cdot 2 \cdot (-3) + 2 \cdot 4 \cdot 1 + (-1) \cdot 2 \cdot 3 = -6 + 8 + (-6) = -4$

Diagonales negativas: $(-1) \cdot 2 \cdot 1 + 1 \cdot 4 \cdot 3 + 2 \cdot 2 \cdot (-3) = -2 + 12 + (-12) = -2$

$$\det(A) = -4 - (-2) = -2$$

Como $\det(A) = -2 \neq 0$, la matriz es invertible.

### Paso 2: Calcular los 9 cofactores

Recordá el tablero de signos para $3 \times 3$:

```
| +  -  + |
| -  +  - |
| +  -  + |
```

**$C_{11}$** (signo $+$, borramos fila 1 col 1):

$\det\begin{pmatrix} 2 & 4 \\ 3 & -3 \end{pmatrix} = -6 - 12 = -18$. Con signo $+$: $C_{11} = -18$

**$C_{12}$** (signo $-$, borramos fila 1 col 2):

$\det\begin{pmatrix} 2 & 4 \\ 1 & -3 \end{pmatrix} = -6 - 4 = -10$. Con signo $-$: $C_{12} = -(-10) = 10$

**$C_{13}$** (signo $+$, borramos fila 1 col 3):

$\det\begin{pmatrix} 2 & 2 \\ 1 & 3 \end{pmatrix} = 6 - 2 = 4$. Con signo $+$: $C_{13} = 4$

**$C_{21}$** (signo $-$, borramos fila 2 col 1):

$\det\begin{pmatrix} 2 & -1 \\ 3 & -3 \end{pmatrix} = -6 + 3 = -3$. Con signo $-$: $C_{21} = -(-3) = 3$

**$C_{22}$** (signo $+$, borramos fila 2 col 2):

$\det\begin{pmatrix} 1 & -1 \\ 1 & -3 \end{pmatrix} = -3 + 1 = -2$. Con signo $+$: $C_{22} = -2$

**$C_{23}$** (signo $-$, borramos fila 2 col 3):

$\det\begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix} = 3 - 2 = 1$. Con signo $-$: $C_{23} = -1$

**$C_{31}$** (signo $+$, borramos fila 3 col 1):

$\det\begin{pmatrix} 2 & -1 \\ 2 & 4 \end{pmatrix} = 8 + 2 = 10$. Con signo $+$: $C_{31} = 10$

**$C_{32}$** (signo $-$, borramos fila 3 col 2):

$\det\begin{pmatrix} 1 & -1 \\ 2 & 4 \end{pmatrix} = 4 + 2 = 6$. Con signo $-$: $C_{32} = -6$

**$C_{33}$** (signo $+$, borramos fila 3 col 3):

$\det\begin{pmatrix} 1 & 2 \\ 2 & 2 \end{pmatrix} = 2 - 4 = -2$. Con signo $+$: $C_{33} = -2$

### Paso 3: Armar la matriz de cofactores

$$C_A = \begin{pmatrix} -18 & 10 & 4 \\ 3 & -2 & -1 \\ 10 & -6 & -2 \end{pmatrix}$$

### Paso 4: Transponer

$$C_A^T = \begin{pmatrix} -18 & 3 & 10 \\ 10 & -2 & -6 \\ 4 & -1 & -2 \end{pmatrix}$$

### Paso 5: Multiplicar por $\frac{1}{\det(A)} = \frac{1}{-2}$

$$A^{-1} = \frac{1}{-2} \begin{pmatrix} -18 & 3 & 10 \\ 10 & -2 & -6 \\ 4 & -1 & -2 \end{pmatrix} = \begin{pmatrix} 9 & -\frac{3}{2} & -5 \\ -5 & 1 & 3 \\ -2 & \frac{1}{2} & 1 \end{pmatrix}$$

> "Parece un poco largo pero tengan en cuenta por ejemplo, si van a calcular la inversa con el método directo y las ecuaciones son medias feas, también le va a llevar tiempo"

**Traducción:** Este método es largo (9 cofactores + transponer + dividir), pero el método directo (plantear el sistema de ecuaciones) también es largo. Después cada uno elige el que le resulte más cómodo.

---

## Demostraciones de las propiedades (para parcial/examen)

> "Estas demostraciones no van para mañana. Esto es teórico, pero para parcial examen. Mañana es mucho más fácil, más práctico y más nivel más bajo"

**Traducción:** Las demostraciones de abajo **no entran en la evaluación continua de mañana**. Son para el parcial y examen. La evaluación de mañana es práctica: calcular determinantes y aplicar propiedades.

---

### Demostración de la Propiedad 1 (dos sumandos en una fila)

**Lo que dice la propiedad:** Si una fila tiene dos sumandos, el determinante se separa en la suma de dos determinantes.

**Idea de la demostración (método directo):** Desarrollás el determinante por la fila que tiene los dos sumandos. Como cada entrada de esa fila es $b_{2j} + c_{2j}$, la sumatoria se separa en dos sumatorias (una con los $b$ y otra con los $c$). Las menores son las mismas en ambos casos (porque al borrar la fila 2, las tres matrices $A$, $B$, $C$ quedan iguales). Cada sumatoria resulta ser el determinante de $B$ y el determinante de $C$ respectivamente.

**También se demostró por inducción completa:**
- Paso base ($1 \times 1$): $\det(b_{11} + c_{11}) = b_{11} + c_{11} = \det(b_{11}) + \det(c_{11})$. Trivial.
- Paso inductivo: Se asume que vale para $n \times n$ y se prueba para $(n+1) \times (n+1)$. Se desarrolla por una fila que NO sea la que tiene los sumandos (por ejemplo la fila 1). Las menores son $n \times n$ y tienen dos sumandos en una fila, así que se les puede aplicar la hipótesis.

> "¿Por qué no se puede por la fila 2? Si yo desarrollo por la fila 2, al aplicar la matriz de juntas se me va esa fila 2. Se me va la fila 2, por lo tanto no puedo aplicar la hipótesis"

**Traducción:** Si desarrollás por la fila que tiene los sumandos, al borrar esa fila para hacer la menor, los sumandos desaparecen y no podés aplicar la hipótesis de inducción. Por eso hay que desarrollar por cualquier OTRA fila.

---

### Demostración de la Propiedad 2 (factor común de una fila)

**Lo que dice la propiedad:** Si toda una fila está multiplicada por $k$, el determinante queda multiplicado por $k$.

**Idea de la demostración:** Desarrollás por la fila multiplicada por $k$. Cada entrada es $k \cdot a_{1j}$. El $k$ está en cada término de la sumatoria, así que sale como factor común. Las menores de $A$ y de $B$ son iguales (porque al borrar la fila 1, ambas matrices quedan iguales). Queda $k$ por el determinante de $A$.

---

### Demostración de la Propiedad 3 (factor de toda la matriz)

**Lo que dice la propiedad:** $\det(\lambda A) = \lambda^n \cdot \det(A)$

**Idea de la demostración:** Si toda la matriz está multiplicada por $\lambda$, eso significa que CADA una de las $n$ filas está multiplicada por $\lambda$. Aplicamos la Propiedad 2 en la fila 1 (sale un $\lambda$), luego en la fila 2 (sale otro $\lambda$), así hasta la fila $n$. Quedan $n$ lambdas afuera: $\lambda^n \cdot \det(A)$.

---

### Demostración de la Propiedad 5 (dos filas iguales → det = 0)

Se demostró **por inducción completa** con fila 1 = fila 2.

**Paso base** ($2 \times 2$): Si fila 1 = fila 2, la matriz es $\begin{pmatrix} a & a \\ a & a \end{pmatrix}$, y $\det = a \cdot a - a \cdot a = 0$.

**Paso inductivo:** Tenemos una matriz $(n+1) \times (n+1)$ con fila 1 = fila 2. Desarrollamos por una fila que NO sea la 1 ni la 2 (por ejemplo la fila 3). Cada menor es $n \times n$ y sigue teniendo fila 1 = fila 2. Por hipótesis de inducción, el determinante de cada menor es $0$. Como estamos sumando cosas multiplicadas por $0$, todo da $0$.

> "Bueno, en este caso es distinta la demostración. Desarrollo por la fila 3 pero puede ser por cualquier fila que no sea la 1 y la 2"

---

### Demostración de la Propiedad 6 (intercambiar filas cambia el signo)

**Lo que dice la propiedad:** Si intercambiamos dos filas, el determinante cambia de signo.

**Idea de la demostración:** Se construye una matriz auxiliar $C$ con fila 1 = (fila 1 + fila 2) y fila 2 = (fila 2 + fila 1). Como ambas filas son iguales ($f_1 + f_2 = f_2 + f_1$), por la Propiedad 5 $\det(C) = 0$.

Después se aplica la Propiedad 1 dos veces (una en fila 1, otra en fila 2), separando $\det(C)$ en 4 determinantes. Dos de ellos tienen filas iguales (y valen $0$ por Propiedad 5). Los otros dos son $\det(A)$ y $\det(B)$. Como $\det(C) = 0$:

$$0 = \det(A) + \det(B) \implies \det(B) = -\det(A)$$

---

### Demostración de la Propiedad 7 (combinación lineal de filas no cambia el det)

**Lo que dice la propiedad:** Si a una fila le sumás combinación lineal de las demás, el determinante no cambia.

**Idea de la demostración:** La fila $j$ tiene la forma: $\lambda_1 \cdot f_1 + \lambda_2 \cdot f_2 + \ldots + f_j + \ldots + \lambda_n \cdot f_n$. Por la Propiedad 1, separamos en $n$ determinantes. Por la Propiedad 2, sacamos cada $\lambda_k$ afuera. En cada uno de esos determinantes (salvo uno), hay dos filas iguales (la fila original y la que se copió), así que por la Propiedad 5 valen $0$. El único que sobrevive es el que tiene la fila $j$ sin modificar, que es $\det(A)$.

> "Bueno, cero más cero más determinante de A más cero más cero, nos queda que el determinante de B es igual al determinante de A"

---

### Propiedad 8 — No se demostró

$\det(A) = \det(A^T)$. El profesor indicó que esta propiedad no se demuestra en el curso.

---

### Demostración de la Propiedad 9 (triangular → producto de la diagonal)

**Lo que dice la propiedad:** Si $A$ es triangular superior, $\det(A) = a_{11} \cdot a_{22} \cdot \ldots \cdot a_{nn}$.

**Idea de la demostración:** Desarrollamos por la columna 1. Como $A$ es triangular superior, todos los elementos debajo de la diagonal en la columna 1 son $0$. Entonces solo sobrevive el primer término: $a_{11} \cdot \det(\text{menor})$. La menor es otra triangular (más chica), así que repetimos: desarrollamos por la columna 1 de la menor, y solo sobrevive $a_{22}$. Seguimos hasta llegar a una $1 \times 1$ que es $a_{nn}$. Queda: $a_{11} \cdot a_{22} \cdot \ldots \cdot a_{nn}$.

> "Es clave acá ir desarrollando por la columna 1"

---

## Ejercicio 5: Matrices ortogonales y el determinante

### Enunciado

Si $A$ es ortogonal (es decir, $A^{-1} = A^T$), probar que $\det(A) = 1$ o $\det(A) = -1$. Investigar si vale el recíproco.

### Parte 1: Prueba de que $\det(A) = \pm 1$

Si $A$ es ortogonal, entonces $A^{-1} = A^T$. Eso implica que $A \cdot A^T = I$.

Tomamos determinante de ambos lados:

$$\det(A \cdot A^T) = \det(I) = 1$$

Por la **Propiedad 4**: $\det(A) \cdot \det(A^T) = 1$

Por la **Propiedad 8**: $\det(A^T) = \det(A)$

Entonces: $\det(A) \cdot \det(A) = 1$, es decir $\det(A)^2 = 1$

Las soluciones son: $\det(A) = 1$ o $\det(A) = -1$. $\blacksquare$

### Parte 2: ¿Vale el recíproco?

El recíproco sería: si $\det(A) = \pm 1$, ¿es $A$ ortogonal?

**No.** Contraejemplo:

$$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

$\det(A) = 1$, pero $A^T \cdot A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \neq I$. Entonces $A$ no es ortogonal a pesar de tener determinante $1$.

---

## Notas prácticas del profesor sobre los ejercicios

- **Ejercicio 6:** Una matriz triangular con todas las entradas de la diagonal $\neq 0$ es invertible. Justificación: Propiedad 9 (det = producto de la diagonal, que es $\neq 0$) + Teorema 2 (det $\neq 0$ → invertible).
- **Ejercicio 7 (verdadero/falso):** Una matriz con una fila entera de ceros NO es invertible (desarrollar por esa fila da det = 0). Una matriz con dos filas iguales tampoco (Propiedad 5 → det = 0 → no invertible).
- **Ejercicio 8:** Para encontrar los valores de $\lambda$ para los cuales una matriz es invertible, calcular el determinante en función de $\lambda$, y ver para qué valores se anula. Donde se anula → no invertible. Para el resto → invertible.

---

## Anuncios

> "Mañana las primeras dos horas, ver dudas práctico. 9 y media tenemos la prueba. Va a durar media hora la prueba. El mismo formato. Nada que no hayamos visto, tenemos conceptos claros. Las demostraciones de hoy no van"

- La evaluación continua es mañana (15 de abril), a las 9:30, media hora, en grupo
- Mismo formato que la primera evaluación
- Las demostraciones de hoy **NO entran**
- La semana que viene empieza el tercer tema: **sistemas de ecuaciones**

---

# PARTE 4 — Preparación para la evaluación continua (15 de abril)

Evaluación sobre **determinantes**. Nivel básico, en grupo, con material. Lo que importa: saber calcular determinantes rápido, aplicar propiedades sin dudar, y no caer en las trampas clásicas.

---

## Lo que SÍ necesitás manejar

- Calcular determinantes de $2 \times 2$ (diagonal principal menos la otra)
- Calcular determinantes de $3 \times 3$ con **Sarrus**
- Calcular determinantes de $4 \times 4$ o más con **desarrollo por cofactores** (elegir fila/columna con más ceros)
- Saber qué es una **menor** (borrar fila $i$ y columna $j$)
- El **patrón de signos** del cofactor: $(-1)^{i+j}$
- Las **9 propiedades** — no memorizarlas textual, sino saber qué hace cada una y cuándo usarla
- El **Teorema 1**: si $A$ es invertible $\implies \det(A) \neq 0$ y $\det(A^{-1}) = \frac{1}{\det(A)}$
- Combinar propiedades para calcular expresiones tipo $\det(3A^2 \cdot B^T)$
- Que $\det(A+B) \neq \det(A) + \det(B)$

## Lo que NO necesitás memorizar

- La fórmula directa del determinante $3 \times 3$ (para eso está Sarrus)
- Demostraciones completas (pero sí el razonamiento general de cada una)
- La fórmula $\sum_{j=1}^{n}$ exacta del cofactor (basta con entender el procedimiento: elegir fila, recorrer columnas, signo alternado, multiplicar por la menor)

## Prerrequisitos de matrices que SÍ necesitás para determinantes

No te piden matrices en esta evaluación, pero necesitás estos conceptos para entender determinantes:

| Concepto de matrices | ¿Por qué lo necesitás? |
|---------------------|----------------------|
| Matriz cuadrada ($n \times n$) | El determinante solo existe para cuadradas |
| Transpuesta ($A^T$) | Propiedad 8: $\det(A) = \det(A^T)$ |
| Matriz invertible y $A^{-1}$ | El Teorema 1 conecta invertibilidad con $\det \neq 0$ |
| Identidad ($I$) | $\det(I) = 1$ — aparece en casi toda demostración |
| Triangular (superior/inferior) | Propiedad 9: $\det = $ producto de la diagonal |
| Diagonal | Caso particular de triangular |
| Nilpotente ($A^k = O$) | Si es nilpotente $\implies \det = 0$ |
| Antisimétrica ($A^T = -A$) | Si $n$ es impar $\implies \det = 0$ |

---

## 5 errores que aparecen en evaluaciones (según el profesor)

### Error 1: Usar Sarrus en matrices que NO son $3 \times 3$

> "He visto varias veces en parciales que aplican la regla de Sarrus para matrices 4x4"

Sarrus **solo** para $3 \times 3$. Para $4 \times 4$ o más: desarrollo por cofactores.

### Error 2: Pensar que $\det(kA) = k \cdot \det(A)$

**MAL:** $\det(4A) = 4 \cdot \det(A)$

**BIEN:** $\det(4A) = 4^n \cdot \det(A)$, donde $n$ es la dimensión.

Si $A$ es $3 \times 3$: $\det(4A) = 4^3 \cdot \det(A) = 64 \cdot \det(A)$.

### Error 3: Pensar que $\det(A+B) = \det(A) + \det(B)$

Esto es **falso**. No existe una propiedad de la suma. Lo que sí existe es $\det(A \cdot B) = \det(A) \cdot \det(B)$ (producto, no suma).

### Error 4: No mirar la matriz antes de calcular

Antes de hacer ninguna cuenta, chequeá:
- ¿Tiene dos filas o columnas iguales? → $\det = 0$ (propiedad 5)
- ¿Es triangular? → multiplicar la diagonal (propiedad 9)
- ¿Hay una fila/columna con muchos ceros? → desarrollar por ahí

### Error 5: Multiplicar la fila objetivo al usar propiedad 7

Cuando sumás combinación lineal de filas a una fila (propiedad 7), la fila que modificás **no puede estar multiplicada** por un número. Si la multiplicás, cambiaste el determinante (propiedad 2).

---

## Checklist rápido antes de calcular un determinante

1. ¿Hay dos filas (o columnas) iguales? → $\det = 0$, listo
2. ¿Es triangular (o diagonal)? → multiplicar la diagonal, listo
3. ¿Hay alguna fila/columna entera de ceros? → $\det = 0$, listo
4. ¿Puedo sacar factor común de alguna fila? → sacarlo (propiedad 2) y simplificar
5. ¿Es $3 \times 3$? → Sarrus
6. ¿Es $4 \times 4$ o más? → buscar la fila/columna con más ceros y desarrollar por cofactores

---

## Referencia rápida de propiedades

| # | Nombre corto | Qué hace | Fórmula |
|---|-------------|----------|---------|
| 1 | Separar sumandos | Si una fila tiene sumas, separá en dos $\det$ | $\det = \det_1 + \det_2$ |
| 2 | Factor de fila | Sacás $k$ de una fila | $k$ sale multiplicando |
| 3 | Factor de toda la matriz | Sacás $k$ de todo | $\det(kA) = k^n \cdot \det(A)$ |
| 4 | Producto | $\det$ del producto = producto de $\det$ | $\det(AB) = \det(A) \cdot \det(B)$ |
| 5 | Filas iguales | Dos filas iguales | $\det = 0$ |
| 6 | Intercambio | Intercambiar dos filas | $\det$ cambia de signo |
| 7 | Comb. lineal | Sumar múltiplos de filas a otra | $\det$ no cambia |
| 8 | Transpuesta | Transponer | $\det(A) = \det(A^T)$ |
| 9 | Triangular | Si es triangular | $\det = $ diagonal multiplicada |
| ✗ | Suma (NO vale) | $\det(A+B)$ | $\neq \det(A) + \det(B)$ |

---

## Preguntas de práctica

### Pregunta 1 (cálculo directo $2 \times 2$)

Calcular $\det\begin{pmatrix} 5 & 3 \\ -2 & 4 \end{pmatrix}$.

> **Respuesta:** $5 \cdot 4 - 3 \cdot (-2) = 20 + 6 = 26$.

---

### Pregunta 2 (cálculo con Sarrus $3 \times 3$)

Calcular $\det\begin{pmatrix} 2 & 1 & 3 \\ 0 & -1 & 4 \\ 1 & 0 & 2 \end{pmatrix}$.

> **Respuesta:** Por Sarrus: positivas $= 2 \cdot (-1) \cdot 2 + 1 \cdot 4 \cdot 1 + 3 \cdot 0 \cdot 0 = -4 + 4 + 0 = 0$. Negativas $= 1 \cdot (-1) \cdot 3 + 2 \cdot 4 \cdot 0 + 2 \cdot 0 \cdot 1 = -3 + 0 + 0 = -3$. Det $= 0 - (-3) = 3$.

**Verificación por cofactores (columna 2, tiene un cero):**

Columna 2: entradas $1, -1, 0$. El $0$ está en posición $(3,2)$, así que solo dos términos:

- $(1,2)$: $1 \cdot (-1)^{1+2} \cdot \det\begin{pmatrix} 0 & 4 \\ 1 & 2 \end{pmatrix} = 1 \cdot (-1) \cdot (0 - 4) = (-1)(-4) = 4$

- $(2,2)$: $(-1) \cdot (-1)^{2+2} \cdot \det\begin{pmatrix} 2 & 3 \\ 1 & 2 \end{pmatrix} = (-1)(+1)(4 - 3) = -1$

- $(3,2)$: $0 \cdot \ldots = 0$

Total: $4 + (-1) + 0 = 3 \quad \checkmark$

---

### Pregunta 3 (propiedad 3 — factor de toda la matriz)

Si $A$ es $3 \times 3$ y $\det(A) = -2$, ¿cuánto vale $\det(5A)$?

> **Respuesta:** $\det(5A) = 5^3 \cdot \det(A) = 125 \cdot (-2) = -250$.

No es $5 \cdot (-2) = -10$. El $5$ sale elevado a la dimensión.

---

### Pregunta 4 (propiedad 4 — producto)

Si $\det(A) = 3$ y $\det(B) = -4$, ¿cuánto vale $\det(A^2 \cdot B)$?

> **Respuesta:** $\det(A^2 \cdot B) = \det(A^2) \cdot \det(B) = \det(A)^2 \cdot \det(B) = 9 \cdot (-4) = -36$.

---

### Pregunta 5 (Teorema 1 — inversa)

Si $\det(A) = 6$, ¿cuánto vale $\det(A^{-1})$?

> **Respuesta:** $\det(A^{-1}) = \frac{1}{\det(A)} = \frac{1}{6}$.

---

### Pregunta 6 (combinar varias propiedades)

$A$ es $2 \times 2$, $\det(A) = 3$. Calcular $\det(2A^{-1})$.

> **Respuesta:** Propiedad 3: $\det(2A^{-1}) = 2^2 \cdot \det(A^{-1}) = 4 \cdot \frac{1}{3} = \frac{4}{3}$.

---

### Pregunta 7 (propiedad 5 — sin calcular)

¿Cuánto vale $\det\begin{pmatrix} 1 & 5 & 3 \\ 2 & 4 & 7 \\ 1 & 5 & 3 \end{pmatrix}$?

> **Respuesta:** $0$. La fila 1 es igual a la fila 3.

---

### Pregunta 8 (propiedad 9 — triangular)

¿Cuánto vale $\det\begin{pmatrix} 3 & 1 & 8 & 2 \\ 0 & -2 & 5 & 1 \\ 0 & 0 & 4 & 7 \\ 0 & 0 & 0 & -1 \end{pmatrix}$?

> **Respuesta:** Es triangular superior. $\det = 3 \cdot (-2) \cdot 4 \cdot (-1) = 24$.

---

### Pregunta 9 (propiedad 6 — intercambio)

Si $\det(A) = 7$ y $B$ se obtiene intercambiando las filas 2 y 4 de $A$, ¿cuánto vale $\det(B)$?

> **Respuesta:** $\det(B) = -\det(A) = -7$.

---

### Pregunta 10 (tramposa — la NO propiedad)

Si $\det(A) = 3$ y $\det(B) = 5$, ¿cuánto vale $\det(A + B)$?

> **Respuesta:** **No se puede saber.** $\det(A+B) \neq \det(A) + \det(B)$. No hay ninguna propiedad que relacione el determinante de la suma con los determinantes individuales.

---

### Pregunta 11 (nilpotente)

Si $A^4 = O$ (la nula), ¿cuánto vale $\det(A)$?

> **Respuesta:** $\det(A^4) = \det(O) = 0$. Por propiedad 4: $\det(A)^4 = 0$. El único número cuya cuarta potencia es $0$ es el $0$. Entonces $\det(A) = 0$.

---

### Pregunta 12 (antisimétrica)

Si $A$ es antisimétrica ($A^T = -A$) y $A$ es $5 \times 5$, ¿cuánto vale $\det(A)$?

> **Respuesta:** $\det(A^T) = \det(-A)$. Lado izquierdo: $\det(A)$ (propiedad 8). Lado derecho: $(-1)^5 \cdot \det(A) = -\det(A)$ (propiedad 3). Entonces $\det(A) = -\det(A)$, lo que implica $2\det(A) = 0$, entonces $\det(A) = 0$.

---

### Pregunta 13 (ejercicio completo — estilo evaluación)

$A$ es $3 \times 3$ invertible, $\det(A) = 4$, $B = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{pmatrix}$.

Calcular: $\det(2A^3 \cdot B^T \cdot A^{-1})$.

> **Respuesta:**
>
> Propiedad 4 (separar el producto): $\det(2A^3) \cdot \det(B^T) \cdot \det(A^{-1})$
>
> - $\det(2A^3) = 2^3 \cdot \det(A^3) = 8 \cdot \det(A)^3 = 8 \cdot 64 = 512$ (P3 + P4)
> - $\det(B^T) = \det(B) = 1 \cdot 3 \cdot 2 = 6$ (P8 + P9)
> - $\det(A^{-1}) = \frac{1}{4}$ (Teorema 1)
>
> Resultado: $512 \cdot 6 \cdot \frac{1}{4} = \frac{3072}{4} = 768$.
