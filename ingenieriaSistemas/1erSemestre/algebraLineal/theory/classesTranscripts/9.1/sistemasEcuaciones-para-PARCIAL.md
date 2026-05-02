# Sistemas de Ecuaciones — Explicación paso a paso, desde cero

Este documento cubre **sistemas de ecuaciones lineales**: qué son, cómo se clasifican, cómo se resuelven por escalerización, la inversa por el método de Gauss, y la triple equivalencia que conecta matrices, determinantes y sistemas. Al final hay preparación para la evaluación continua del 22 de abril. Todo explicado asumiendo que no sabés nada.

---

## Mapa de lo que vamos a ver

| Parte | ¿Qué se aprende? |
|-------|-------------------|
| 1 | Qué es un sistema de ecuaciones, clasificación, matriz ampliada, método de escalerización, tres formas escalerizadas, grados de libertad, ejemplos 2×2 y 4×3 (Clase 8) |
| 2 | Sistema con parámetro, inversa por escalerización (Gauss), triple equivalencia (matriz ↔ determinante ↔ sistema), despeje matricial $x = A^{-1}B$, ejemplos de parcial (Clase 9) |
| 3 | **Prep evaluación continua: errores comunes, checklist, preguntas de práctica** |

---

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxx   PLAYBOOK PARA LA PRUEBA   xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxx   (usar durante la prueba)  xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

# PLAYBOOK PARA LA PRUEBA

**Esta sección es la que vas a usar durante la evaluación continua.** Si te trabás, vení acá primero antes de buscar teoría. Está pensada para leer rápido y aplicar.

## ▶ Árbol de decisión: tengo un sistema, ¿qué hago?

```
1. Escribí la matriz ampliada  (A | B)
        ↓
2. ¿Es homogéneo (B = 0)?
        ├─ SÍ  → No puede ser incompatible. Si te da SI, REVISÁ CUENTAS.
        └─ NO → seguí
        ↓
3. Escalerizá aplicando las 3 operaciones  (ver Receta A)
        ↓
4. Mirá la última fila de la matriz escalerizada:
        ├─ (0, 0, …, 0 | k≠0)  → SISTEMA INCOMPATIBLE (SI) — listo, no tiene solución
        ├─ Escalera perfecta (tantos escalones como incógnitas) → SCD (ver Receta B)
        └─ Alguna fila toda en ceros (0 = 0)  → SCI (ver Receta C)
```

---

## ▶ Receta A — Cómo escalerizar (lo que hacés en el 90% del tiempo)

**Objetivo:** generar ceros abajo de la diagonal, columna por columna, de izquierda a derecha.

1. **Mirá el elemento $(1,1)$** (esquina sup. izq.). Si es $0$, intercambiá filas para que arriba haya algo ≠ 0.
2. **Generá ceros debajo** usando la **operación 3**: para cada fila $F_i$ debajo, hacé $F_i \leftarrow F_i + k \cdot F_1$ con $k$ elegido para que la primera entrada de $F_i$ quede en $0$.
3. **Bajá una fila y repetí** sobre el elemento $(2,2)$, generando ceros debajo de él (solo en las filas 3 en adelante).
4. **Continúa** hasta que no queden entradas por anular abajo.

**Cómo elegir $k$ (sale "a ojo" con práctica):**
Si querés eliminar $a_{ij}$ usando la fila pivote $F_p$ cuyo pivote es $a_{pj}$:
$$k = -\frac{a_{ij}}{a_{pj}}$$

**Tip:** al sumar filas **nunca modifiques la fila pivote** — solo se modifica la fila que está "recibiendo" la suma.

---

## ▶ Receta B — Cómo resolver un SCD (escalera perfecta)

**Método:** despejar hacia arriba (back-substitution). Desde la última fila hasta la primera, una incógnita por fila.

1. **Última fila:** tiene una sola incógnita. Despejala directo.
2. **Penúltima fila:** tiene dos incógnitas, pero ya conocés una (la de la última fila). Sustituí y despejá la otra.
3. **Subí una fila más:** ahora conocés dos. Sustituí y despejá la tercera.
4. **Seguí hasta llegar a la primera fila.** Todas las incógnitas están determinadas.

**Verificación (opcional pero recomendada):** sustituí tus valores en la ecuación 2 original y chequeá que se cumpla. Si da, estás bien; si no, revisá cuentas.

---

## ▶ Receta C — Cómo resolver un SCI (hay filas anuladas)

1. **Contá ecuaciones efectivas** (las que NO se anularon): ese número es $p$.
2. **Contá incógnitas totales:** ese número es $n$.
3. **Calculá grados de libertad:** $r = n - p$.
4. **Elegí $r$ incógnitas como parámetros libres** usando letras griegas:
   - 1 grado → $\alpha$
   - 2 grados → $\alpha$, $\beta$
   - 3 grados → $\alpha$, $\beta$, $\gamma$
5. **Despejá las demás incógnitas** en función de los parámetros, usando back-substitution desde la última ecuación efectiva.
6. **Escribí la solución final** como "$x_1 = \ldots, \; x_2 = \ldots, \ldots, \; \text{parámetros} \in \mathbb{R}$".

---

## ▶ Receta D — Cómo manejar un parámetro (ej: $\lambda$)

1. **Escalerizá normalmente** tratando al parámetro como si fuera un número cualquiera.
2. **Cuando llegues a dividir por una expresión con el parámetro**, detenete: pregúntate "¿esta expresión puede ser 0?".
3. **Encontrá los valores críticos** (los que anulan la expresión): resolvés la ecuación tipo $(\lambda - a)(\lambda - b) = 0$.
4. **Caso general** (el parámetro NO es ningún valor crítico): seguís escalerizando y clasificás normalmente.
5. **Caso por caso**, sustituís cada valor crítico en la matriz escalerizada y ves cómo queda (SCD, SCI o SI).
6. **Armás un cuadro resumen** con todos los casos.

---

## ▶ Receta E — Atajos para ahorrar tiempo

Antes de empezar a escalerizar, chequeá rápido:

| Chequeo | Si se cumple… | Conclusión inmediata |
|---------|---------------|---------------------|
| Dos filas idénticas o proporcionales | Una se anula al escalerizar | Probablemente **SCI** |
| Una fila es combinación lineal de otras | Se anula | Probablemente **SCI** |
| Sistema **homogéneo** ($B = \vec{0}$) | Siempre tiene la trivial | **Nunca SI** — solo SCD o SCI |
| Te dan $\det(A) \neq 0$ | Triple equivalencia | Sistema es **SCD**, sin escalerizar |
| Te dan $\det(A) = 0$ | Triple equivalencia | Sistema **no** es SCD — es SCI o SI |

---

## ▶ Errores típicos en evaluaciones (NO los cometas)

1. **Olvidar el término independiente al multiplicar una fila.** Si multiplicás $F_1$ por 3, el número a la derecha de la barra también se multiplica por 3.
2. **Multiplicar una fila por 0.** No vale — destruís la ecuación.
3. **Decir que un sistema homogéneo es incompatible.** Imposible. Si te da, revisá cuentas.
4. **Confundir SCI con SI.** $(0, 0, 0 \mid 0)$ es SCI (ec. $0 = 0$, cierto siempre). $(0, 0, 0 \mid 5)$ es SI (ec. $0 = 5$, imposible).
5. **Contar mal las ecuaciones efectivas.** Las filas anuladas NO cuentan como ecuaciones efectivas.
6. **Modificar la fila pivote al generar ceros.** La fila pivote queda quieta, solo se modifica la fila que "recibe".

---

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxx  FIN DEL PLAYBOOK  xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

El resto del documento es la **teoría detallada** que construyó estas recetas. Si durante la prueba te trabás con un concepto específico, buscá la sección correspondiente más abajo.

---

# PARTE 1 — ¿Qué es un sistema de ecuaciones? (Clase 8, 15 de abril)

## La Gran Pregunta de Hoy: ¿Qué es un sistema de ecuaciones y cómo se resuelve?

Después de cerrar determinantes (con la evaluación continua a la mañana), empieza el tercer tema del curso. Vamos a ver:
1. Qué es un sistema lineal de ecuaciones
2. Cómo se clasifica (compatible determinado, compatible indeterminado, incompatible)
3. Cómo se escribe matricialmente y qué es la matriz ampliada
4. Sistema homogéneo (un caso especial importante)
5. El método de **escalerización** (la herramienta para resolver todo)
6. Ejemplos concretos con interpretación geométrica

---

## Conexión con la Clase Anterior

La clase pasada (14 de abril) cerró el teórico de determinantes con el Teorema 2 (det $\neq 0$ → invertible), la inversa por cofactores y las demostraciones de las propiedades. Hoy a la mañana fue la evaluación continua sobre determinantes. Ahora arranca un tema nuevo que, como vamos a ver, **se conecta con todo lo anterior**: matrices, determinantes e inversa.

> "Bueno, se empieza a relacionar todo, matrices, determinantes, sistemas de ecuaciones. Podemos saber el siguiente tema, que es geometría, también se relaciona con matrices como estamos explicando todo el tiempo"

---

## ¿Qué es un sistema lineal de ecuaciones?

### Primero, un ejemplo concreto

Antes de cualquier fórmula, mirá esto:

$$\begin{cases} 2x + 3y = 7 \\ x - y = 1 \end{cases}$$

Eso **es** un sistema de ecuaciones. Son dos ecuaciones que comparten las mismas incógnitas ($x$ e $y$), y "resolver el sistema" quiere decir encontrar **valores** para $x$ e $y$ que hagan verdaderas a las dos ecuaciones al mismo tiempo.

Por ejemplo, $x = 2$ e $y = 1$ cumple las dos:
- Primera: $2 \cdot 2 + 3 \cdot 1 = 4 + 3 = 7$ ✓
- Segunda: $2 - 1 = 1$ ✓

Listo, eso es un sistema. Todo lo demás en esta sección es generalizar esta idea.

### ¿Por qué se le dice "lineal"?

"Lineal" quiere decir que las incógnitas aparecen **en su forma más simple**: sumadas y multiplicadas por números. No aparecen:
- Al cuadrado ($x^2$) o elevadas a ningún otro exponente.
- Adentro de raíces ($\sqrt{x}$).
- Multiplicadas entre sí ($x \cdot y$).
- Dentro de funciones (seno, log, etc.).

**Ejemplos de ecuaciones lineales (las que nos interesan):**
- $3x + 2y = 5$ ✓
- $x - y + z = 0$ ✓
- $7x = 14$ ✓

**Ejemplos de ecuaciones que NO son lineales:**
- $x^2 + y = 3$ ✗ (hay un cuadrado)
- $xy = 6$ ✗ (incógnitas multiplicadas entre sí)
- $\sqrt{x} + y = 2$ ✗ (raíz)

En todo este curso trabajamos **solo** con sistemas lineales.

---

### La forma genérica — lo que parece jeroglífico pero no lo es

Cuando los matemáticos quieren hablar de "un sistema cualquiera" sin especificar números, escriben esto:

$$\begin{cases} a_{11} x_1 + a_{12} x_2 + \ldots + a_{1n} x_n = b_1 \\ a_{21} x_1 + a_{22} x_2 + \ldots + a_{2n} x_n = b_2 \\ \;\;\vdots \\ a_{m1} x_1 + a_{m2} x_2 + \ldots + a_{mn} x_n = b_m \end{cases}$$

Parece un monstruo con todos esos subíndices, pero **no hay que aprenderlo de memoria**. Es solo una forma de decir "imagínate un sistema de cualquier tamaño". Vamos a descomponerlo:

#### Pieza 1: $m$ y $n$

- $m$ = **cuántas ecuaciones** hay (cuántas filas del sistema).
- $n$ = **cuántas incógnitas** hay.

En el ejemplo del principio ($2x + 3y = 7$ y $x - y = 1$): $m = 2$ (dos ecuaciones) y $n = 2$ (dos incógnitas, $x$ e $y$).

$m$ y $n$ son **independientes** — no tienen por qué ser iguales. Podés tener 3 ecuaciones y 5 incógnitas, o 10 ecuaciones y 2 incógnitas, lo que sea.

#### Pieza 2: $x_1, x_2, x_3, \ldots$

Cuando hay muchas incógnitas, darle un nombre distinto a cada una ($x, y, z, w, t, \ldots$) se complica. Entonces se usa **una sola letra** ($x$) con un **número abajo** (subíndice):

- $x_1$ es la primera incógnita.
- $x_2$ es la segunda.
- $x_3$ es la tercera.
- … y así hasta $x_n$ (la última).

Es solo **una forma de nombrar cosas**, no hay matemática acá. $x_1$ e $y$ serían la misma cosa en un sistema 2×2, solo cambia el nombre.

#### Pieza 3: $b_1, b_2, b_3, \ldots$

Son los **números del lado derecho** de cada ecuación. Se llaman **términos independientes** porque no están "multiplicados por una incógnita" — están "por su cuenta".

- $b_1$ es el término independiente de la ecuación 1.
- $b_2$ es el término independiente de la ecuación 2.
- … hasta $b_m$.

En el ejemplo $\begin{cases} 2x + 3y = 7 \\ x - y = 1 \end{cases}$: $b_1 = 7$ y $b_2 = 1$.

#### Pieza 4: $a_{ij}$ — el que confunde más

$a_{ij}$ es un **coeficiente**, o sea, un número que multiplica a una incógnita. Los dos subíndices ($i$ y $j$) te dicen **de qué ecuación** y **de qué incógnita** se trata:

- $i$ = **número de ecuación** (fila).
- $j$ = **número de incógnita** (columna).

Entonces:

| Notación | Se lee | Significa |
|----------|--------|-----------|
| $a_{11}$ | "a uno uno" | Coeficiente en la ecuación 1, de la incógnita $x_1$ |
| $a_{12}$ | "a uno dos" | Coeficiente en la ecuación 1, de la incógnita $x_2$ |
| $a_{21}$ | "a dos uno" | Coeficiente en la ecuación 2, de la incógnita $x_1$ |
| $a_{23}$ | "a dos tres" | Coeficiente en la ecuación 2, de la incógnita $x_3$ |
| $a_{mn}$ | "a eme ene" | Coeficiente en la última ecuación, de la última incógnita |

**Importante:** $a_{12}$ **NO** se lee "a doce" — se lee "a uno dos", porque son dos subíndices separados. Lo mismo $a_{23}$ es "a dos tres", no "a veintitrés".

#### Ejemplo concreto: identificar los $a_{ij}$ y $b_i$

Tomá este sistema:

$$\begin{cases} 2x_1 + 3x_2 = 7 \\ x_1 - x_2 = 1 \end{cases}$$

Emparejamos con la forma genérica:

- $a_{11} = 2$ (coeficiente de $x_1$ en la primera ecuación)
- $a_{12} = 3$ (coeficiente de $x_2$ en la primera ecuación)
- $a_{21} = 1$ (coeficiente de $x_1$ en la segunda ecuación, porque $x_1$ está solo → es $1 \cdot x_1$)
- $a_{22} = -1$ (coeficiente de $x_2$ en la segunda ecuación)
- $b_1 = 7$ (término independiente de la primera)
- $b_2 = 1$ (término independiente de la segunda)

Y listo. Los subíndices son solo **direcciones** — te dicen dónde está cada número en la "grilla" del sistema.

> "La anotación se empieza a parecer un poco a las matrices que veíamos. Después vamos a ver que hay una forma matricial de expresarlo"

**Conexión con matrices:** el subíndice $a_{ij}$ es idéntico al que usaban las matrices (fila $i$, columna $j$). No es casualidad — vas a ver en un momento que los coeficientes de un sistema **forman una matriz**.

---

## ¿Qué es una solución?

### La idea simple

Una **solución** es **un conjunto de valores** (uno por incógnita) que hace que TODAS las ecuaciones se cumplan al mismo tiempo.

Dos palabras clave:
- **"Todas":** si verifica algunas ecuaciones pero otras no, no sirve — no es solución.
- **"Al mismo tiempo":** los mismos valores deben funcionar en las dos (o tres, o cien) ecuaciones.

**Analogía:** pensá en el sistema como una lista de condiciones que hay que cumplir **todas juntas**. Es como cuando buscás un departamento y tenés una lista: tiene que tener balcón, estar cerca del trabajo, costar menos de X. Un departamento con balcón pero lejos del trabajo **no** cumple. Una solución del sistema es como el departamento que cumple toda la lista.

### Ejemplo paso a paso

Sistema:

$$\begin{cases} x + y = 3 \\ x - y = 1 \end{cases}$$

**¿Es $(x, y) = (2, 1)$ solución?** Probemos.

Ecuación 1: sustituimos $x = 2$, $y = 1$.
$$2 + 1 = 3 \quad \checkmark$$

Ecuación 2: sustituimos los mismos valores.
$$2 - 1 = 1 \quad \checkmark$$

Las dos se cumplen → **Sí, $(2, 1)$ es solución**.

**¿Y $(x, y) = (3, 0)$?** Probemos.

Ecuación 1: $3 + 0 = 3$ ✓
Ecuación 2: $3 - 0 = 3$ ✗ (debería dar 1)

La primera se cumple pero la segunda no → **No es solución**. No importa que una de las dos haya dado bien: tenían que dar bien **las dos**.

### Observación importante: "un conjunto de números"

Cuando decimos "una solución", no es **un número** — es **una tupla** (un grupo ordenado de números). En un sistema con 2 incógnitas, una solución es un par como $(2, 1)$. En un sistema con 3 incógnitas, una solución es un trío como $(1, 2, 3)$. Y así.

**Regla general:** si el sistema tiene $n$ incógnitas, una solución es un conjunto ordenado de $n$ números, uno por cada incógnita.

---

## Clasificación de los sistemas

Todo sistema cae en una (y solo una) de estas tres categorías:

| Categoría | Abreviatura | ¿Cuántas soluciones tiene? |
|-----------|-------------|---------------------------|
| Compatible determinado | **SCD** | Una única solución |
| Compatible indeterminado | **SCI** | Infinitas soluciones |
| Incompatible | **SI** | Ninguna solución |

### Primera división: ¿tiene solución o no?

- **Compatible:** el sistema tiene al menos una solución.
- **Incompatible:** el sistema no tiene ninguna solución.

### Segunda división (dentro de compatible): ¿cuántas soluciones?

- **Determinado:** una única solución.
- **Indeterminado:** más de una solución (en la práctica, siempre serán infinitas).

> "En los casos que vamos a ver en la práctica, los compatibles indeterminados van a ser de infinitas soluciones. Pero para clasificarlos, si tiene más de una solución ya decimos que es compatible indeterminado"

**Traducción:** técnicamente, "indeterminado" es cualquier sistema con más de una solución. Pero en este curso, siempre que nos aparezca uno indeterminado, va a tener **infinitas** soluciones.

---

## Expresión matricial: $A \cdot x = B$

Esta parte es solo **una forma distinta de escribir el mismo sistema** — no cambia nada del problema, solo el "formato" de presentación.

### Paso 1: ¿Qué problema estamos resolviendo al "reescribir"?

Escribir un sistema con muchas ecuaciones y muchas incógnitas ocupa mucho espacio. Mirá:

$$\begin{cases} 2x + 3y - z = 7 \\ x - y + 2z = 4 \\ 3x + 2y + z = 8 \end{cases}$$

Tres ecuaciones, tres incógnitas. Ya ocupa tres líneas. Si fueran 10 ecuaciones y 10 incógnitas, ocuparía 10 líneas y sería difícil de leer.

La **expresión matricial** resuelve esto: **mete todo el sistema en una sola ecuación**, usando matrices. No es magia — es solo un reordenamiento.

### Paso 2: Descomponer el sistema en 3 piezas

Mirá el sistema y separá mentalmente tres cosas:

**Pieza 1: Los coeficientes** (los números que multiplican a las incógnitas).

En el ejemplo: $2, 3, -1, 1, -1, 2, 3, 2, 1$. Los organizamos en una **grilla rectangular** (una matriz) respetando la estructura original (fila por ecuación, columna por incógnita):

$$A = \begin{pmatrix} 2 & 3 & -1 \\ 1 & -1 & 2 \\ 3 & 2 & 1 \end{pmatrix}$$

Esto se llama **matriz de coeficientes** y se nota $A$.

**Pieza 2: Las incógnitas** (los nombres de lo que queremos encontrar).

Las apilamos verticalmente en un **vector columna** (una matriz de una sola columna):

$$x = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$$

**Pieza 3: Los términos independientes** (los números del lado derecho de cada ecuación).

También apilados verticalmente:

$$B = \begin{pmatrix} 7 \\ 4 \\ 8 \end{pmatrix}$$

### Paso 3: La afirmación

**El sistema de arriba es exactamente lo mismo que escribir:**

$$A \cdot x = B$$

Es decir:

$$\begin{pmatrix} 2 & 3 & -1 \\ 1 & -1 & 2 \\ 3 & 2 & 1 \end{pmatrix} \cdot \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 7 \\ 4 \\ 8 \end{pmatrix}$$

**Espera, ¿por qué esto es lo mismo?** Vamos a probarlo, porque no es obvio.

### Paso 4: Verificar que la afirmación es cierta (hacer el producto)

Acordate del **producto matriz × vector** que vieron con matrices: para cada fila de la matriz, multiplicás "entrada por entrada" con el vector y sumás.

**Fila 1 de $A$ por el vector $x$:**
$$\underbrace{2}_{a_{11}} \cdot x + \underbrace{3}_{a_{12}} \cdot y + \underbrace{-1}_{a_{13}} \cdot z = 2x + 3y - z$$

¡Eso es el lado izquierdo de la primera ecuación del sistema!

**Fila 2 de $A$ por el vector $x$:**
$$1 \cdot x + (-1) \cdot y + 2 \cdot z = x - y + 2z$$

¡Lado izquierdo de la segunda ecuación!

**Fila 3 de $A$ por el vector $x$:**
$$3 \cdot x + 2 \cdot y + 1 \cdot z = 3x + 2y + z$$

¡Lado izquierdo de la tercera!

Entonces el producto $A \cdot x$ te devuelve un **vector columna** donde cada entrada es el lado izquierdo de una ecuación:

$$A \cdot x = \begin{pmatrix} 2x + 3y - z \\ x - y + 2z \\ 3x + 2y + z \end{pmatrix}$$

Igualar ese vector a $B = \begin{pmatrix} 7 \\ 4 \\ 8 \end{pmatrix}$ **entrada por entrada** te da las tres ecuaciones originales:

- Primera entrada: $2x + 3y - z = 7$ ✓
- Segunda: $x - y + 2z = 4$ ✓
- Tercera: $3x + 2y + z = 8$ ✓

**Recuperamos el sistema original.** La expresión $A \cdot x = B$ es **idénticamente lo mismo** que el sistema — solo que escrito más compacto.

### Paso 5: Resumen de la correspondencia

| En el sistema | En la expresión matricial |
|---------------|---------------------------|
| Coeficientes (los $a_{ij}$) | Matriz $A$ |
| Incógnitas (los $x_i$) | Vector $x$ |
| Términos independientes (los $b_i$) | Vector $B$ |
| "El lado izquierdo es igual al derecho" | $A \cdot x = B$ |

### ¿Para qué sirve escribirlo así?

Dos razones:
1. **Es más corto:** una sola ecuación $A \cdot x = B$ reemplaza 10 líneas.
2. **Permite usar herramientas de matrices:** cosas como "multiplicar por la inversa a ambos lados" (que es como despejás $x$, más adelante) solo se pueden hacer en forma matricial.

---

## Matriz ampliada

### Paso 1: El problema

Ya sabemos que un sistema se puede escribir como $A \cdot x = B$. Pero cuando vamos a **resolverlo**, el vector $x$ (con los nombres de las incógnitas) **no aporta información nueva** — son solo nombres.

Pensalo así: si yo te digo "resolvé este sistema" y te paso la matriz $A$ y el vector $B$, vos podés resolverlo aunque no sepas si las incógnitas se llaman $(x, y, z)$, $(a, b, c)$ o $(x_1, x_2, x_3)$. Los nombres son decorativos.

Entonces, para resolver, nos alcanza con **dos** piezas: $A$ y $B$.

### Paso 2: La idea

En vez de llevar $A$ por un lado y $B$ por otro, los **juntamos** en una sola matriz, pegando $B$ como una columna extra a la derecha de $A$. Los separamos con una **barra vertical** solo para acordarnos cuál es cuál.

Esa matriz combinada se llama **matriz ampliada** y se escribe $(A \mid B)$.

### Paso 3: Ejemplo concreto

Tomemos el mismo sistema de antes:

$$\begin{cases} 2x + 3y - z = 7 \\ x - y + 2z = 4 \\ 3x + 2y + z = 8 \end{cases}$$

Con:

$$A = \begin{pmatrix} 2 & 3 & -1 \\ 1 & -1 & 2 \\ 3 & 2 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 7 \\ 4 \\ 8 \end{pmatrix}$$

La **matriz ampliada** pega $B$ como cuarta columna, separándola con una barra:

$$(A \mid B) = \left(\begin{array}{ccc|c} 2 & 3 & -1 & 7 \\ 1 & -1 & 2 & 4 \\ 3 & 2 & 1 & 8 \end{array}\right)$$

Cada fila de esta matriz ampliada **es una ecuación del sistema**:

- Fila 1: los coeficientes $2, 3, -1$ a la izquierda, el término independiente $7$ a la derecha → ecuación $2x + 3y - z = 7$.
- Fila 2: coeficientes $1, -1, 2$ y $4$ → ecuación $x - y + 2z = 4$.
- Fila 3: coeficientes $3, 2, 1$ y $8$ → ecuación $3x + 2y + z = 8$.

### Paso 4: ¿Qué significa la barra vertical?

**La barra no es un operador matemático** — es puramente visual, para recordarte qué parte son coeficientes y qué parte son términos independientes.

Antes de la barra: los números que **multiplican a las incógnitas**.
Después de la barra: los números del **lado derecho** de cada ecuación.

Si sacaras la barra, la matriz seguiría siendo la misma matemáticamente — la barra solo te ayuda a leerla.

### Paso 5: ¿Para qué vamos a usar la matriz ampliada?

Para **resolver el sistema**. El método de escalerización (que viene en la próxima sección) se aplica sobre la matriz ampliada: se hacen operaciones sobre sus filas hasta llegar a una forma simple que revela la solución.

> "Obviamos el vector de incógnitas. Es la matriz base para escalerizar, que va a ser la forma de resolver estos sistemas"

**Traducción:** la matriz ampliada tira los nombres de las incógnitas porque no importan para resolver, y se queda con los dos conjuntos de números que sí importan (coeficientes y términos independientes), juntos en una sola estructura lista para operar.

---

## Sistema homogéneo

### ¿Qué es?

Un sistema **homogéneo** es un sistema donde **TODOS** los términos independientes son cero. Es decir: $B = \vec{0}$.

$$\begin{cases} a_{11} x_1 + \ldots + a_{1n} x_n = 0 \\ a_{21} x_1 + \ldots + a_{2n} x_n = 0 \\ \;\;\vdots \\ a_{m1} x_1 + \ldots + a_{mn} x_n = 0 \end{cases}$$

### La propiedad clave: nunca es incompatible

> "Este tipo de sistemas siempre va a ser compatible. ¿Por qué? Si yo tomo $x_1 = x_2 = \ldots = x_n = 0$, esto va a ser solución siempre"

**La razón:** si hacés cero todas las incógnitas, cada ecuación te queda "$0 = 0$", que se cumple siempre. Entonces **todo sistema homogéneo tiene al menos una solución** (la de poner todo en cero).

A esa solución se le llama **solución trivial**:

$$x_1 = 0, \; x_2 = 0, \; \ldots, \; x_n = 0$$

### Consecuencia

Un sistema homogéneo solo puede ser:
- **Compatible determinado** (si la trivial es la única solución), o
- **Compatible indeterminado** (si hay otras soluciones además de la trivial).

**Nunca puede ser incompatible.**

> "En un parcial, hace un par de años se preguntó, si ponía un sistema homogéneo no así genérico sino con unos particulares y se pedía, sin hacer cuentas porque se podía concluir que es compatible. Entonces había que decir eso"

**Traducción:** en el parcial puede aparecer un sistema homogéneo y te pueden pedir clasificarlo **sin hacer cuentas**. Como es homogéneo, sabés que no puede ser incompatible — solo puede ser SCD o SCI. Decí eso y ya justificaste la mitad del ejercicio.

> "Otra cosa que a veces pasa en los parciales es que se pide resolver un sistema homogéneo y les da incompatible, eso no puede pasar. Más allá de que le hayan errado alguna cuenta, conceptualmente nunca les puede pasar"

**Traducción:** si resolvés un sistema homogéneo y te da "incompatible", **revisá las cuentas**, porque es imposible.

---

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxx  TEORÍA CLAVE — Las 3 operaciones de escalerización  xxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Sistemas equivalentes y las tres operaciones

Esta sección es **la base de toda la resolución**. Si la entendés, el resto es aplicar mecanismo.

### Paso 1: ¿Qué quiere decir "dos sistemas equivalentes"?

Dos sistemas son **equivalentes** cuando **tienen exactamente las mismas soluciones**. Punto. No importa cómo se ven las ecuaciones, cuántas haya, o en qué orden estén. Si los valores que resuelven uno también resuelven el otro (y viceversa), los dos sistemas son equivalentes.

**Ejemplo simple de sistemas equivalentes:**

Sistema A:
$$\begin{cases} x + y = 3 \\ x - y = 1 \end{cases}$$

Sistema B (el mismo A pero con las ecuaciones al revés):
$$\begin{cases} x - y = 1 \\ x + y = 3 \end{cases}$$

Los dos tienen la misma solución: $(x, y) = (2, 1)$. Entonces son **equivalentes**. Solo cambiamos el orden de las filas — nada más.

**Analogía:** son como dos listas de compras distintas que llevan a comprar exactamente los mismos productos. La lista puede estar en distinto orden, con los productos escritos de distinta forma, pero el resultado final (lo que metés en la bolsa) es idéntico.

### Paso 2: La pregunta clave

¿**Qué cosas le puedo hacer a un sistema** sin cambiar sus soluciones?

Esta es la pregunta de oro. Si yo puedo **transformar** un sistema difícil en uno fácil **sin alterar las soluciones**, puedo resolver el fácil y ya tengo la solución del difícil.

La respuesta son **tres operaciones específicas**. Hay muchísimas cosas que **sí** alteran las soluciones (ej: sumarle 5 a un lado de una ecuación sin tocar el otro), pero estas tres **nunca** las alteran.

### Paso 3: La notación $F_1, F_2, F_3, \ldots$ (leé esto antes de seguir)

Antes de ver las tres operaciones, necesitás entender **cómo se escriben**. En todo el resto del documento vas a ver cosas como:

- $F_2 \leftarrow F_2 - 2 F_1$
- $F_1 \leftarrow 3 F_1$
- $F_3 \leftarrow F_3 + F_2$

Si no manejás esta notación, ese tipo de líneas son jeroglíficos. Vamos desde cero.

#### ¿Qué significa $F_i$?

La letra **$F$** quiere decir **"fila"**. El subíndice (el número abajo) dice **qué fila**:

- $F_1$ = **fila 1** (la primera fila de la matriz)
- $F_2$ = **fila 2** (la segunda fila)
- $F_3$ = **fila 3**
- $F_i$ = una fila cualquiera, la fila $i$

Es literalmente una abreviatura. "$F_2$" es más corto que "la fila número 2". Nada más.

**Ejemplo:** en esta matriz:

$$\left(\begin{array}{cc|c} 2 & 3 & 7 \\ 1 & -1 & 1 \\ 0 & 4 & 8 \end{array}\right)$$

- $F_1 = (2, 3, 7)$
- $F_2 = (1, -1, 1)$
- $F_3 = (0, 4, 8)$

Cuando hablamos de "la fila" nos referimos a **toda** la fila — los coeficientes **y** el término independiente juntos.

#### ¿Qué significa la flecha $\leftarrow$?

La flecha **$\leftarrow$** se lee **"se reemplaza por"** o **"pasa a ser"**. Es como un "=" pero con dirección: dice qué va a **cambiar** y qué **lo reemplaza**.

$$\underbrace{F_2}_{\text{lo que va a cambiar}} \;\leftarrow\; \underbrace{\text{alguna expresión}}_{\text{lo que lo reemplaza}}$$

**Se lee:** "la fila 2 se reemplaza por el resultado de alguna expresión".

**Analogía con programación (si te ayuda):** es como la asignación `F2 = F2 - 2*F1` en código. Tomás la expresión de la derecha, la calculás, y el resultado lo guardás en la variable de la izquierda.

#### Cómo leer las operaciones enteras

Ahora ya podés descifrar cualquier expresión. Tres ejemplos:

**Ejemplo A — $F_1 \leftarrow 3 F_1$**

Se lee: "la fila 1 pasa a ser 3 veces la fila 1". O sea: multiplicá toda la fila 1 por 3, y reemplazala con el resultado.

Si $F_1 = (2, 3, 7)$, después de la operación:
$$F_1 = 3 \cdot (2, 3, 7) = (6, 9, 21)$$

**Ejemplo B — $F_2 \leftarrow F_2 - 2 F_1$**

Se lee: "la fila 2 pasa a ser la fila 2 menos 2 veces la fila 1".

Paso a paso: tomá la fila 2 actual, restale el doble de la fila 1 (entrada por entrada), y el resultado reemplaza a la fila 2. **La fila 1 no cambia** — solo se usa para hacer el cálculo.

Si $F_1 = (2, 3, 7)$ y $F_2 = (1, -1, 1)$, entonces:
- $2 F_1 = (4, 6, 14)$
- $F_2 - 2 F_1 = (1 - 4, \; -1 - 6, \; 1 - 14) = (-3, -7, -13)$
- Nueva $F_2 = (-3, -7, -13)$
- $F_1$ queda igual: $(2, 3, 7)$

**Ejemplo C — $F_3 \leftarrow F_3 + F_2$**

Se lee: "la fila 3 pasa a ser la fila 3 más la fila 2" (sin multiplicarla por nada, o multiplicarla por 1).

#### Resumen rápido de la notación

| Notación | Se lee | Qué hace |
|----------|--------|----------|
| $F_i$ | "fila $i$" | La fila número $i$ de la matriz |
| $F_i \leftarrow (\text{algo})$ | "la fila $i$ se reemplaza por (algo)" | Cambiar la fila $i$ por el resultado de la expresión |
| $F_i \leftarrow k \cdot F_i$ | "la fila $i$ se reemplaza por $k$ por la fila $i$" | Multiplicar la fila $i$ por $k$ |
| $F_i \leftarrow F_i + k \cdot F_j$ | "la fila $i$ se reemplaza por ella más $k$ por la fila $j$" | A la fila $i$ le sumás $k$ veces la fila $j$ |
| $F_i \leftrightarrow F_j$ | "intercambio de filas $i$ y $j$" | Cambiar de lugar las filas $i$ y $j$ |

**Con esta notación sola podés leer cualquier operación de escalerización del documento.** Volvé acá si te perdés.

---

### Paso 4: Las tres operaciones, una por una

#### Antes de ver los ejemplos: cómo se muestra una operación

En los ejemplos de abajo vas a ver algo así:

$$\left(\begin{array}{cc|c} 1 & 3 & 4 \\ 2 & 5 & 9 \end{array}\right) \xrightarrow{F_2 \leftarrow F_2 - 2F_1} \left(\begin{array}{cc|c} 1 & 3 & 4 \\ 0 & -1 & 1 \end{array}\right)$$

**Ojo — esto puede confundir al principio:** lo que está a **cada lado de la flecha** es la **matriz COMPLETA del sistema**, no una fila suelta. A la izquierda está la matriz **antes** de aplicar la operación; a la derecha está **después**.

En el ejemplo de arriba, la matriz tiene **dos filas**:

- La fila de arriba ($F_1$): $(1, 3, 4)$
- La fila de abajo ($F_2$): $(2, 5, 9)$

La operación $F_2 \leftarrow F_2 - 2F_1$ dice "la fila 2 se reemplaza por la fila 2 menos 2 veces la fila 1". Entonces **solo cambia la fila de abajo**. La fila de arriba queda intacta.

Fijate en la matriz del lado derecho:
- La fila de arriba sigue siendo $(1, 3, 4)$ — **no se tocó**.
- La fila de abajo, que era $(2, 5, 9)$, ahora es $(0, -1, 1)$ — **esta es la nueva $F_2$**.

**Resumen de la convención:** cuando veas una matriz con varias filas en un ejemplo de operación, es la matriz entera del sistema. La operación indicada sobre la flecha cambia **una** de esas filas; las otras quedan como estaban. Mostramos la matriz entera para que veas el efecto en contexto.

---

#### Operación 1: Intercambiar dos ecuaciones

**Qué hacés:** tomás dos ecuaciones del sistema y las cambiás de lugar. La que era la 1 ahora es la 2, y al revés.

**Por qué no cambia las soluciones:** un sistema es una **lista de condiciones que hay que cumplir todas**. El orden de la lista no importa. Si tenés que cumplir "A y B", es lo mismo que cumplir "B y A".

**En la matriz ampliada:** intercambiás dos filas enteras.

**Ejemplo:**

$$\left(\begin{array}{cc|c} 1 & 1 & 3 \\ 1 & -1 & 1 \end{array}\right) \xrightarrow{\text{intercambio filas}} \left(\begin{array}{cc|c} 1 & -1 & 1 \\ 1 & 1 & 3 \end{array}\right)$$

Las dos matrices representan sistemas equivalentes. ¿Para qué querrías hacer esto? Por ejemplo, para poner arriba una fila que tenga un $1$ (más fácil de usar como pivote).

---

#### Operación 2: Multiplicar una ecuación por un número distinto de cero

**Qué hacés:** elegís una ecuación, y multiplicás TODA la ecuación por un número $k$ (donde $k$ puede ser cualquier cosa menos cero). "Toda" significa: los coeficientes **y** el término independiente.

**Por qué no cambia las soluciones:** si "$A = B$" es verdadero, entonces "$k \cdot A = k \cdot B$" también es verdadero. Multiplicar ambos lados por lo mismo preserva la igualdad.

**Por qué $k$ NO puede ser cero:** si multiplicás por $0$, ambos lados se vuelven $0$, y la ecuación se convierte en "$0 = 0$" — que es cierto pero no dice nada. Perdés información.

**En la matriz ampliada:** multiplicás la fila entera (incluyendo lo que está a la derecha de la barra).

**Ejemplo:** multiplicar la fila 1 por $3$:

$$\left(\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & 1 & 3 \end{array}\right) \xrightarrow{F_1 \leftarrow 3 F_1} \left(\begin{array}{cc|c} 3 & 6 & 15 \\ 0 & 1 & 3 \end{array}\right)$$

Fijate que el $5$ (término independiente) también se multiplicó por 3, convirtiéndose en $15$. **Eso es crítico** — si olvidás multiplicar el término independiente, rompés el sistema.

> "Cuando digo una ecuación, es a ambos lados la ecuación"

---

#### Operación 3: Sumar una ecuación (o un múltiplo de ella) a otra

**Qué hacés:** tomás una ecuación, la multiplicás por algún número (o no), y se la sumás a otra ecuación. La que **recibe** la suma es la que cambia; la otra queda igual.

**Por qué no cambia las soluciones:** si $(x, y, \ldots)$ cumple dos ecuaciones al mismo tiempo, entonces también cumple su suma. Y recíprocamente, si cumple la suma y una de las originales, cumple la otra (por resta).

**En la matriz ampliada:** le sumás una fila (multiplicada por lo que elijas) a otra fila. La notación típica:

$$F_2 \leftarrow F_2 + k \cdot F_1$$

Se lee: "la nueva fila 2 es igual a la fila 2 actual más $k$ veces la fila 1".

**Ejemplo:** $F_2 \leftarrow F_2 - 2 F_1$ (o sea, le sumamos a la fila 2 la fila 1 multiplicada por $-2$):

$$\left(\begin{array}{cc|c} 1 & 3 & 4 \\ 2 & 5 & 9 \end{array}\right) \xrightarrow{F_2 \leftarrow F_2 - 2F_1} \left(\begin{array}{cc|c} 1 & 3 & 4 \\ 0 & -1 & 1 \end{array}\right)$$

Cálculo entrada por entrada de la nueva fila 2:
- Columna 1: $2 - 2 \cdot 1 = 0$
- Columna 2: $5 - 2 \cdot 3 = -1$
- Término independiente: $9 - 2 \cdot 4 = 1$

**¿Para qué sirve?** Para **generar ceros**. Mirá el resultado: la nueva fila 2 empieza con $0$. Eso es lo que vamos a usar todo el tiempo.

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxx  TABLA RESUMEN — Las 3 operaciones  xxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Paso 5: Tabla resumen

| # | Operación | Notación típica | Para qué sirve |
|---|-----------|-----------------|----------------|
| 1 | Intercambiar dos filas | $F_i \leftrightarrow F_j$ | Poner arriba filas cómodas |
| 2 | Multiplicar fila por $k \neq 0$ | $F_i \leftarrow k \cdot F_i$ | Simplificar coeficientes (ej: dividir por 2) |
| 3 | Sumar múltiplo de una fila a otra | $F_i \leftarrow F_i + k \cdot F_j$ | Generar ceros donde queremos |

**Las tres se pueden combinar** libremente. Podés aplicar tantas como quieras, en el orden que quieras. El sistema se mantiene equivalente todo el tiempo.

### Paso 6: ¿Para qué sirve todo esto?

Estas tres operaciones son **la caja de herramientas** del método de escalerización. El plan es:

1. Empezar con la matriz ampliada del sistema original (difícil de resolver directamente).
2. Aplicar las tres operaciones hasta **transformar** la matriz en una forma "escalera" (fácil de leer).
3. Como el sistema sigue siendo equivalente, sus soluciones son las mismas — pero ahora es fácil encontrarlas.

---

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxx  MÉTODO CENTRAL — Escalerización  xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## El método de escalerización

### La idea en una oración

**Transformá** la matriz ampliada, usando las tres operaciones, **hasta que adopte forma de escalera**. Esa forma final te dice inmediatamente cómo es el sistema (SCD, SCI, SI) y te permite leer la solución.

### ¿Qué es "forma de escalera" concretamente?

Es una matriz donde **los ceros se acumulan en el triángulo inferior izquierdo**, formando una escalera que desciende. Esquemáticamente (usando $\ast$ para números cualquiera):

$$\left(\begin{array}{ccc|c} \ast & \ast & \ast & \ast \\ 0 & \ast & \ast & \ast \\ 0 & 0 & \ast & \ast \end{array}\right)$$

Fijate los ceros: forman un triángulo abajo a la izquierda. Cada fila tiene un cero **más** que la anterior. Eso es "escalera".

### ¿Por qué la forma de escalera es útil?

Porque **cada fila tiene menos incógnitas que la anterior**. Mirá:

- La última fila: solo tiene un coeficiente no nulo (el del final) → involucra solo **una incógnita** → la podés despejar directamente.
- La penúltima fila: tiene dos coeficientes no nulos → involucra **dos incógnitas**, pero una de ellas ya la sabés del paso anterior → despeje fácil.
- Y así hacia arriba: cada fila te da la información justa para despejar la siguiente incógnita.

En contraste, en un sistema sin ordenar, cada ecuación mezcla todas las incógnitas juntas y es imposible despejar una sola.

### Procedimiento, paso a paso

1. **Escribí la matriz ampliada** $(A \mid B)$ del sistema original.
2. **Mirá la primera columna** (a la izquierda). Si el primer elemento ($a_{11}$) es $0$, intercambiá filas para que arriba haya un número distinto de $0$.
3. **Generá ceros en la primera columna**, abajo del $a_{11}$. Para cada fila por debajo, aplicás una operación del tipo $F_i \leftarrow F_i + k \cdot F_1$ con $k$ elegido para que quede $0$.
4. **Ignorá la primera fila** (ya está lista) y bajá a la segunda columna, desde la segunda fila hacia abajo. Repetí: el $a_{22}$ tiene que ser distinto de $0$, y generás ceros debajo.
5. **Seguí bajando**: la tercera columna desde la tercera fila, la cuarta columna desde la cuarta fila, etc.
6. **Cuando termines**, la matriz está en forma de escalera.
7. **Clasificá** mirando la forma final: SI (fila "$0 = k$" con $k \neq 0$), SCD (escalera perfecta), o SCI (alguna fila anulada).
8. **Si es compatible, resolvé** desde la última fila hacia arriba (despeje hacia arriba o **back-substitution**).

### Dos notas importantes

**Nota 1 — No hay un solo camino:** hay muchas maneras de llegar a la forma escalerada. Dos estudiantes pueden usar operaciones distintas y llegar a matrices finales diferentes; **siempre y cuando ambos hayan aplicado solo las tres operaciones válidas, el sistema resultante es equivalente al original y las soluciones finales coinciden**.

**Nota 2 — El objetivo es GENERAR CEROS:** el 90% del trabajo es aplicar la operación 3 (sumar múltiplos de filas) para fabricar ceros en las posiciones que querés. Las operaciones 1 y 2 son auxiliares.

### Cómo elegir el $k$ de la operación 3 (la parte técnica)

Cuando querés eliminar el elemento $a_{ij}$ usando la fila $i_{\text{pivote}}$ (donde $a_{i_{\text{pivote}}, j}$ es el pivote), el $k$ que tenés que usar es:

$$k = -\frac{a_{ij}}{a_{i_{\text{pivote}}, j}}$$

**Explicado sin fórmula:** es el número que, al multiplicar al pivote y sumarlo al elemento que querés eliminar, te da $0$.

**Ejemplo:** querés eliminar el $6$ de la posición $(2, 1)$ usando la fila 1, que empieza con $2$.

$$\left(\begin{array}{cc|c} 2 & 4 & 10 \\ 6 & 7 & 9 \end{array}\right)$$

Necesitás que la nueva entrada $(2,1)$ sea $0$. Operación: $F_2 \leftarrow F_2 + k \cdot F_1$ con $k$ tal que $6 + k \cdot 2 = 0 \Rightarrow k = -3$.

Aplicás $F_2 \leftarrow F_2 - 3 F_1$:
- Columna 1: $6 - 3 \cdot 2 = 0$ ✓
- Columna 2: $7 - 3 \cdot 4 = -5$
- Término indep: $9 - 3 \cdot 10 = -21$

$$\left(\begin{array}{cc|c} 2 & 4 & 10 \\ 0 & -5 & -21 \end{array}\right)$$

Listo — ya tenés el cero. **No hace falta memorizar la fórmula de $k$**; con práctica sale "a ojo".

### Las tres formas escalonadas posibles

Después de escalerizar, el sistema va a quedar en **una (y solo una) de tres formas características**. La forma final te dice directamente qué clasificación tiene el sistema: no hay que hacer más cuentas, alcanza con mirar la matriz.

#### Antes de arrancar: ¿qué significa el símbolo $\ast$ en los esquemas?

En las matrices de abajo vas a ver el símbolo $\ast$ (asterisco). **No es un número específico** — es una forma de decir "acá puede haber **cualquier número**". Lo usamos como marcador cuando lo que importa es la **forma** de la matriz (dónde hay ceros, dónde hay escalones), no los valores exactos.

**Ejemplo:** si digo que una matriz tiene la forma

$$\begin{pmatrix} \ast & \ast \\ 0 & \ast \end{pmatrix}$$

quiero decir que la esquina inferior izquierda es $0$ y los otros tres lugares tienen **algún número** (podría ser $3, -7, 0.5$, lo que sea). Lo que **no** puede pasar es que haya un número donde escribí $0$.

En los esquemas de abajo, lo importante son los **ceros** — ellos definen la forma. Los $\ast$ son números cualquiera que pueden variar.

---

#### Forma 1: Sistema Incompatible (SI)

**La característica visual:** la matriz escalonada tiene una fila donde **todos los coeficientes son $0$ pero el término independiente (lo que está después de la barra) NO es $0$**:

$$\left(\begin{array}{ccc|c} \ast & \ast & \ast & \ast \\ 0 & \ast & \ast & \ast \\ 0 & 0 & 0 & 1 \end{array}\right)$$

Mirá la **fila de abajo**: los tres coeficientes a la izquierda de la barra son todos $0$, pero a la derecha de la barra hay un $1$ (o cualquier número distinto de cero — podría ser $7$, $-3$, lo que sea).

**¿Por qué eso hace el sistema imposible de resolver?**

Acordate de cómo "se lee" una fila de la matriz ampliada como ecuación: los números antes de la barra son los coeficientes de las incógnitas, y el número después de la barra es el término independiente. Entonces esa última fila dice:

$$0 \cdot x_1 + 0 \cdot x_2 + 0 \cdot x_3 = 1$$

Pero **cualquier número** multiplicado por $0$ da $0$. Así que no importa qué valores pongas para $x_1, x_2, x_3$: el lado izquierdo siempre te va a dar $0$. Y el lado derecho es $1$. Nunca va a pasar que $0 = 1$.

**Por eso el sistema no tiene solución:** una de las ecuaciones es literalmente imposible de cumplir, pase lo que pase con las incógnitas.

**Analogía:** es como si el sistema te dijera "necesito que tengas exactamente 1 euro en tu bolsillo, y además necesito que ese 1 euro esté hecho de 0 monedas". Imposible — si tenés 0 monedas, tenés 0 euros, no 1.

**Ejemplo numérico concreto** (mismo patrón, con números reales):

$$\left(\begin{array}{ccc|c} 2 & 1 & 3 & 5 \\ 0 & 4 & -1 & 2 \\ 0 & 0 & 0 & 7 \end{array}\right)$$

La última fila dice "$0 \cdot x + 0 \cdot y + 0 \cdot z = 7$" → imposible → **SI**.

---

#### Forma 2: Sistema Compatible Determinado (SCD)

**La característica visual:** la matriz queda como una **"escalera perfecta"**. Esto significa dos cosas al mismo tiempo:

1. En cada fila aparece un coeficiente **no nulo** (distinto de cero) en una posición más a la derecha que el coeficiente no nulo de la fila anterior. Cada fila "avanza" un paso hacia la derecha respecto a la anterior, como subiendo una escalera.
2. La cantidad de escalones (filas efectivas con un coeficiente no nulo) coincide **exactamente** con la cantidad de incógnitas.

$$\left(\begin{array}{ccc|c} \ast & \ast & \ast & \ast \\ 0 & \ast & \ast & \ast \\ 0 & 0 & \ast & \ast \end{array}\right)$$

Mirá el patrón: el primer coeficiente no nulo de la fila 1 está en la columna 1. El primer coeficiente no nulo de la fila 2 está en la columna 2 (avanzó un lugar). El primer coeficiente no nulo de la fila 3 está en la columna 3 (avanzó otro lugar). Los asteriscos que están a la derecha de cada "escalón" pueden ser cualquier cosa — lo que importa son los ceros a la izquierda, que forman un triángulo.

**¿Por qué "escalera perfecta"?** Porque cada fila sube **exactamente un escalón**. Si una fila saltara dos columnas (ej: la fila 3 empezara directo en la columna 4 sin pasar por la 3), no sería "perfecta" — faltaría un escalón.

**¿Por qué esto da una única solución?**

Leé las filas como ecuaciones **de abajo hacia arriba**:

- La última fila es tipo $\ast \cdot x_3 = \ast$. Como el coeficiente $\ast$ no es cero, podés **despejar $x_3$**: es un número concreto.
- Subís a la penúltima fila: $\ast \cdot x_2 + \ast \cdot x_3 = \ast$. Ya sabés cuánto vale $x_3$ (del paso anterior), así que podés sustituir y despejar $x_2$.
- Subís a la primera fila: $\ast \cdot x_1 + \ast \cdot x_2 + \ast \cdot x_3 = \ast$. Ya sabés $x_2$ y $x_3$, así que despejás $x_1$.

Cada incógnita queda definida por un único valor → **una única solución**.

**Analogía:** es como cuando juntás piezas de un rompecabezas donde cada pieza encaja en un solo lugar. No hay ambigüedad — hay una manera de armarlo y una sola.

**Ejemplo numérico concreto:**

$$\left(\begin{array}{ccc|c} 2 & 1 & 3 & 10 \\ 0 & 4 & -1 & 6 \\ 0 & 0 & 5 & 15 \end{array}\right)$$

- Fila 3: $5z = 15 \Rightarrow z = 3$
- Fila 2: $4y - 3 = 6 \Rightarrow y = \frac{9}{4}$
- Fila 1: $2x + \frac{9}{4} + 9 = 10 \Rightarrow x = -\frac{5}{8}$

Una sola solución → **SCD**.

---

#### Forma 3: Sistema Compatible Indeterminado (SCI)

**La característica visual:** la matriz tiene **"escalones largos"**, o alguna fila se anuló completamente (todos ceros, incluido el término independiente):

$$\left(\begin{array}{ccc|c} \ast & \ast & \ast & \ast \\ 0 & \ast & \ast & \ast \\ 0 & 0 & 0 & 0 \end{array}\right)$$

Mirá la última fila: es **toda ceros**, incluido el lado derecho de la barra. No hay ningún número distinto de cero. Eso significa que esa fila se "anuló" al escalerizar: perdimos una ecuación.

**¿Qué significa que una fila se anule?**

Cuando al aplicar las operaciones de escalerización llegás a una fila completamente de ceros, lo que pasó es que esa ecuación original **era una combinación de las otras** — no aportaba información nueva. Era "redundante".

**Ejemplo intuitivo:** si tenés tres ecuaciones y una es exactamente el doble de otra, no tenés "tres condiciones independientes" — tenés solo dos condiciones distintas (la repetida no cuenta dos veces). La ecuación redundante se convierte en "$0 = 0$" al escalerizar.

**¿Por qué esto da infinitas soluciones?**

Leé la fila anulada como ecuación: "$0 \cdot x_1 + 0 \cdot x_2 + 0 \cdot x_3 = 0$". Esto se cumple **siempre**, pongas lo que pongas en $x_1, x_2, x_3$. No te restringe nada. Es una ecuación "vacía" — no te pide nada.

Entonces te quedan **menos ecuaciones efectivas que incógnitas**. Eso significa que hay incógnitas que no están "atadas" a ningún valor fijo — son libres. Podés elegirles cualquier valor, y después las otras incógnitas se van acomodando a esa elección.

Como cada valor libre que elijas da una solución distinta del sistema, y podés elegir **infinitos** valores distintos → hay **infinitas soluciones**.

**Analogía:** imaginate un mapa con intersecciones (cada ecuación es una calle). Si todas las calles son distintas, se cruzan en un solo punto (SCD). Pero si dos de las "tres" calles son en realidad la misma calle duplicada, solo tenés dos calles distintas — que en 3D pueden cruzarse en toda una línea, no en un solo punto. Esa línea tiene infinitos puntos → infinitas soluciones.

**La manera de expresar esas infinitas soluciones** es con **parámetros** (letras griegas $\alpha, \beta, \ldots$) — a esto se le llama "grados de libertad", y lo explico en la siguiente sección.

**Ejemplo numérico concreto:**

$$\left(\begin{array}{ccc|c} 2 & 1 & 3 & 10 \\ 0 & 4 & -1 & 6 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

La fila 3 es "$0 = 0$" → se cumple siempre, no aporta nada. Te quedan 2 ecuaciones reales (filas 1 y 2) y 3 incógnitas → una incógnita queda libre → infinitas soluciones → **SCI**.

---

### Tabla resumen de las tres formas

| Forma escalonada | ¿Qué mirar? | Clasificación | ¿Cuántas soluciones? |
|-------------------|-------------|---------------|---------------------|
| Fila de ceros **pero con un número $\neq 0$ a la derecha** | La última fila dice "$0 = k$" con $k \neq 0$ | **Incompatible (SI)** | Ninguna |
| **Escalera perfecta** — tantos escalones como incógnitas | Cada fila avanza un escalón, ninguna se anula | **Compatible determinado (SCD)** | Una única |
| **Alguna fila toda de ceros** (incluido el lado derecho) | La última fila dice "$0 = 0$" | **Compatible indeterminado (SCI)** | Infinitas |

### La regla en 3 segundos

Después de escalerizar, mirá **la última fila** de la matriz:

- ¿Es $(0, 0, \ldots, 0 \mid k)$ con $k \neq 0$? → **SI** (imposible)
- ¿Es $(0, 0, \ldots, 0 \mid 0)$? → **SCI** (infinitas)
- ¿Tiene al menos un coeficiente no nulo a la izquierda de la barra? → **SCD** (única), siempre que las filas anteriores también tengan escalera perfecta.

---

## Grados de libertad

Esta sección explica un concepto que suena abstracto pero es muy concreto. Vamos desde cero, sin fórmulas.

---

### Paso 1: ¿Cuál es el problema que queremos resolver?

Cuando un sistema es **compatible indeterminado (SCI)**, ya sabemos que tiene **infinitas soluciones**. El problema es: ¿cómo **escribimos** todas esas infinitas soluciones? No podemos listarlas una por una (son infinitas). Necesitamos una manera compacta de decir "estas son todas las soluciones".

Los **grados de libertad** son la herramienta para eso.

---

### Paso 2: La idea con un ejemplo súper simple

Imaginá que tenés **una sola ecuación** con dos incógnitas:

$$x + y = 5$$

¿Cuántas soluciones tiene?

Pensalo: cualquier par de números que sume $5$ es solución. Algunas:

- $x = 0, \; y = 5$ (porque $0 + 5 = 5$ ✓)
- $x = 1, \; y = 4$ (porque $1 + 4 = 5$ ✓)
- $x = 2, \; y = 3$ (porque $2 + 3 = 5$ ✓)
- $x = 100, \; y = -95$ (porque $100 + (-95) = 5$ ✓)
- $x = -7, \; y = 12$ (porque $-7 + 12 = 5$ ✓)

Hay **infinitas** soluciones. No las podemos listar todas.

**Ahora fijate en el patrón:** yo puedo **elegir libremente el valor de $x$** (cualquier número real), y una vez elegido, **$y$ queda forzado** a ser $5 - x$. Es decir:

- $x$ es **libre** — podés elegir lo que quieras.
- $y$ está **atado** — depende de lo que elijas para $x$.

**A esa "libertad de elegir $x$" le llamamos 1 grado de libertad.**

Entonces: en $x + y = 5$ hay **1 grado de libertad** (una incógnita libre, la otra atada).

---

### Cómo escribimos la solución (primera versión, sin letras raras)

Sabemos dos cosas sobre la solución:
1. $x$ puede ser **cualquier número real** (libre).
2. $y$ depende de lo que elegiste para $x$: concretamente, $y = 5 - x$.

La forma más directa de escribir la solución sería exactamente así, en palabras:

> "$x$ es cualquier número real, e $y$ vale $5 - x$."

Eso ya es una respuesta correcta. Si la dejaras así en el parcial, no estaría mal.

---

### Cómo escribimos la solución (segunda versión, con $\alpha$) — **esto es lo que te trabó**

En matemática se usa una **convención** para escribir lo mismo de forma más prolija. En vez de decir "$x$ es cualquier número real", le damos un **nombre** a ese número cualquiera. El nombre es una letra griega: $\alpha$ (alfa).

**Lo único que hacemos es ponerle un nombre.** No hay una transformación mágica, no es una nueva variable. $\alpha$ es literalmente **otra forma de llamar al valor que estás eligiendo**.

Paso a paso:

**Paso A — Le ponemos nombre al valor libre.**

Decimos: "el número que voy a elegir para $x$, lo voy a llamar $\alpha$". Eso se escribe así:

$$x = \alpha$$

Se lee: "$x$ es igual a $\alpha$". Que es lo mismo que decir "$x$ y $\alpha$ son el mismo número". Yo elijo un valor, lo llamo $\alpha$, y ese es el valor de $x$.

**Paso B — Reescribimos $y$ usando $\alpha$.**

Como $y = 5 - x$, y ahora estamos llamando $\alpha$ a $x$, podemos reemplazar:

$$y = 5 - \alpha$$

Se lee: "$y$ es igual a $5$ menos $\alpha$". Literalmente: "una vez que elegiste $\alpha$ (que es lo mismo que elegir $x$), $y$ vale $5 - \alpha$".

**Paso C — Decimos qué valores puede tomar $\alpha$.**

Como $\alpha$ es "el número que podés elegir libremente", y podés elegir cualquier número real, aclaramos:

$$\alpha \in \mathbb{R}$$

Esta notación se lee "$\alpha$ pertenece a los números reales", que es la forma matemática de decir **"$\alpha$ puede ser cualquier número real"**.

**¿Qué significan los símbolos $\in$ y $\mathbb{R}$?**

- El símbolo $\in$ se lee **"pertenece a"**. Es como decir "está dentro de".
- El símbolo $\mathbb{R}$ (una R con doble palito) es la notación matemática para **el conjunto de todos los números reales** (enteros, decimales, negativos, cero, todo).
- Entonces $\alpha \in \mathbb{R}$ junto significa: "$\alpha$ es un número real cualquiera".

---

### Las tres líneas juntas

Poniendo las tres piezas en una sola línea queda la notación estándar:

$$x = \alpha, \quad y = 5 - \alpha, \quad \alpha \in \mathbb{R}$$

Que leído en español, de corrido, dice:

> "Llamá $\alpha$ al valor libre. Entonces $x$ vale $\alpha$, $y$ vale $5 - \alpha$, y $\alpha$ puede ser cualquier número real."

**Es exactamente la misma información que la primera versión** ("$x$ es cualquier real, $y = 5 - x$"), pero con un nombre extra ($\alpha$) que el profesor quiere ver en el parcial.

---

### ¿Pero entonces por qué molestarse en escribir $x = \alpha$? ¿No es redundante?

**En este ejemplo chiquito, sí — es un poco redundante.** Podrías no usar $\alpha$ y dejar todo en función de $x$. Funcionaría igual.

**Pero hay dos razones por las que vale la pena aprender esta notación:**

1. **En sistemas con más incógnitas, $\alpha$ desambigua.** Si tenés un sistema con $x, y, z$ y dos de ellas son libres, es más claro decir "$x = \alpha, \; y = \beta, \; z = 3 - \alpha + 2\beta$" que "expresá todo en función de $x$ e $y$" — especialmente cuando combinás varias.

2. **Es lo que el profesor espera ver.** En el parcial, la forma aceptada de expresar la solución general de un SCI es con letras griegas. Es una convención que tenés que manejar.

---

### Diccionario rápido de letras griegas

Cada grado de libertad usa **una letra griega distinta**. Las que vas a ver en el curso (en orden):

| Letra | Nombre | Se usa para |
|-------|--------|-------------|
| $\alpha$ | alfa | El primer grado de libertad |
| $\beta$ | beta | El segundo grado de libertad |
| $\gamma$ | gamma | El tercer grado de libertad |
| $\delta$ | delta | El cuarto (raro que aparezca) |

**Regla:** si tu SCI tiene **1 grado de libertad**, usás solo $\alpha$. Si tiene **2**, usás $\alpha$ y $\beta$. Y así.

---

### Paso 3: Un ejemplo con 2 grados de libertad

Ahora imaginá **una sola ecuación** con **tres incógnitas**:

$$x + y + z = 10$$

¿Cuántos valores podés elegir libremente?

- Podés elegir $x$ libremente (ej: $x = 2$)
- Podés elegir $y$ libremente (ej: $y = 3$)
- Una vez elegidos esos dos, $z$ queda forzado: $z = 10 - x - y = 10 - 2 - 3 = 5$

Dos cosas libres y una atada → **2 grados de libertad**.

Como tenemos dos parámetros libres, usamos **dos letras griegas** distintas: $\alpha$ y $\beta$.

$$x = \alpha, \quad y = \beta, \quad z = 10 - \alpha - \beta, \quad \alpha, \beta \in \mathbb{R}$$

Cada par distinto $(\alpha, \beta)$ que elijas te da una solución distinta. Como hay infinitos pares posibles, hay infinitas soluciones — pero todas tienen la forma de arriba.

---

### Paso 4: La "regla" para contar los grados de libertad

Fijate el patrón de los dos ejemplos:

| Ejemplo | Incógnitas | Ecuaciones | Grados de libertad |
|---------|------------|------------|---------------------|
| $x + y = 5$ | 2 | 1 | 1 |
| $x + y + z = 10$ | 3 | 1 | 2 |

**La regla:**

$$\text{grados de libertad} = \text{incógnitas} - \text{ecuaciones efectivas}$$

En fórmula, usando $r$ para grados de libertad, $n$ para incógnitas y $p$ para ecuaciones efectivas:

$$r = n - p$$

### ¿Por qué tiene sentido esta fórmula?

Pensalo así: cada incógnita es una "cosa a determinar". Cada ecuación es una "condición que restringe". Si tenés:

- Más incógnitas que condiciones → sobran incógnitas → algunas son libres.
- Exactamente tantas condiciones como incógnitas → todas quedan determinadas (0 libres).
- Más condiciones que incógnitas → o bien son compatibles (y alguna es redundante), o el sistema no tiene solución.

La cantidad que "sobra" entre incógnitas y condiciones es exactamente los grados de libertad.

---

### Paso 5: ¿Qué quiere decir "ecuaciones efectivas"?

Esta es la parte sutil que siempre confunde. **Ecuaciones efectivas** son las ecuaciones que **realmente restringen algo** después de escalerizar. Las filas que se anulan (quedan $0 = 0$) **no cuentan**, porque no dicen nada útil.

**Ejemplo concreto.** Imaginá este sistema:

$$\begin{cases} x + y + z = 5 \\ 2x + 2y + 2z = 10 \\ x - y + z = 1 \end{cases}$$

A primera vista parece que tenés 3 ecuaciones y 3 incógnitas. Pero si mirás bien, la ecuación 2 es el doble de la ecuación 1 — **están diciendo lo mismo**. Al escalerizar, la fila 2 se va a anular ($0 = 0$).

Después de escalerizar, la matriz va a quedar algo así:

$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 5 \\ 0 & -2 & 0 & -4 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

Contemos:

- Incógnitas: $n = 3$ (porque tenés $x, y, z$)
- Filas con contenido real (no todas ceros): **2** → $p = 2$ ecuaciones efectivas
- Grados de libertad: $r = n - p = 3 - 2 = 1$

**Hay 1 grado de libertad.** Una incógnita queda libre, las otras dos quedan determinadas por lo que elijas para esa.

### Regla práctica para contar ecuaciones efectivas

Después de escalerizar:
- **Contá las filas.**
- **Restá las filas que quedaron todas en ceros** (las "$0 = 0$").
- El resultado es $p$.

Es como decir: "originalmente tenía 3 ecuaciones, pero una se anuló, entonces tengo solo 2 ecuaciones efectivas".

---

### Paso 6: ¿Por qué el SCD tiene 0 grados de libertad?

Un sistema compatible determinado (SCD) es uno que tiene **una única solución**. Si tiene solo una solución, significa que **ninguna incógnita es libre** — todas están atadas a un valor específico.

Si aplicamos la fórmula: SCD significa que $n = p$ (tantas incógnitas como ecuaciones efectivas). Entonces:

$$r = n - p = n - n = 0$$

**0 grados de libertad = 0 parámetros libres = solución única y concreta.**

Ejemplo rápido: si escalerizás y llegás a

$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 1 & 2 & 5 \\ 0 & 0 & 3 & 6 \end{array}\right)$$

3 incógnitas, 3 filas con contenido real → $p = 3$ → $r = 0$ → SCD con solución única.

---

### Paso 7: Tabla de parámetros según grados de libertad

| Grados de libertad ($r$) | Cuántos parámetros necesito | Cómo los escribo |
|--------------------------|----------------------------|------------------|
| 0 | Ninguno (solución única) | — |
| 1 | Uno | $\alpha$ |
| 2 | Dos | $\alpha, \beta$ |
| 3 | Tres | $\alpha, \beta, \gamma$ |
| 4 | Cuatro | $\alpha, \beta, \gamma, \delta$ |

**Regla:** usás **tantas letras griegas como grados de libertad** tenga el sistema.

---

### Paso 8: Resumen en 3 puntos

1. **Grados de libertad** = cantidad de incógnitas que podés **elegir libremente**, sin que se rompa el sistema.
2. Se calculan con la fórmula $r = n - p$, donde $n$ son las incógnitas totales y $p$ son las filas no nulas después de escalerizar.
3. A cada grado de libertad le asignás una letra griega ($\alpha, \beta, \gamma, \ldots$) como parámetro, y expresás la solución general usando esos parámetros.

**En el parcial:** cuando te dé SCI, siempre hacé estos tres pasos: (1) contar $n$, (2) contar $p$, (3) calcular $r$ y elegir ese número de letras griegas.

---

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxx  EJEMPLO PRÁCTICO S1 — Sistema 2×2 SCD  xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Ejemplo S1: Sistema 2×2, compatible determinado

**Este es el ejemplo base de todos.** Si lo entendés paso por paso, tenés la técnica resuelta.

### El problema

Nos dan este sistema de dos ecuaciones con dos incógnitas:

$$\begin{cases} 2x - y = 0 \\ x + y = 3 \end{cases}$$

Nuestra tarea es: (1) clasificar el sistema, (2) si tiene solución, encontrarla.

---

### Paso 1 — Escribir la matriz ampliada

Agarramos los números del sistema y los acomodamos en una grilla, con los coeficientes a la izquierda y los términos independientes a la derecha separados por una barra.

**Cómo armarla:**
- Fila 1 sale de la ecuación 1 ($2x - y = 0$): los coeficientes son $2$ (acompaña a $x$) y $-1$ (acompaña a $y$), y el término independiente es $0$.
- Fila 2 sale de la ecuación 2 ($x + y = 3$): los coeficientes son $1$ y $1$, término independiente $3$.

$$\left(\begin{array}{cc|c} 2 & -1 & 0 \\ 1 & 1 & 3 \end{array}\right)$$

La columna 1 tiene los coeficientes de $x$, la columna 2 los de $y$, y después de la barra están los números del lado derecho.

---

### Paso 2 — Elegir la estrategia (acá es donde hay que pensar)

Queremos llegar a forma de **escalera**: o sea, que el elemento de la posición $(2,1)$ (abajo a la izquierda) sea $0$. Eso es el primer (y en un sistema 2×2, único) cero que tenemos que generar.

Hay varias formas de hacerlo, pero **la más cómoda es intercambiar las filas primero** para que arriba quede el $1$ en lugar del $2$. Con un $1$ como pivote, las cuentas son más fáciles.

**Operación A — Intercambiar $F_1$ y $F_2$:**

$$\left(\begin{array}{cc|c} 2 & -1 & 0 \\ 1 & 1 & 3 \end{array}\right) \xrightarrow{F_1 \leftrightarrow F_2} \left(\begin{array}{cc|c} 1 & 1 & 3 \\ 2 & -1 & 0 \end{array}\right)$$

Ahora $F_1 = (1, 1, 3)$ y $F_2 = (2, -1, 0)$.

**Tip:** al intercambiar, cambió el orden, pero el sistema es **equivalente** (tiene las mismas soluciones). No pasa nada con clasificación ni valores.

---

### Paso 3 — Generar el cero en $(2,1)$

Ahora queremos que el $2$ en la posición $(2,1)$ se convierta en $0$. Para eso usamos la **operación 3**: le sumamos a $F_2$ un múltiplo de $F_1$ tal que el primer elemento quede en cero.

**Pensalo:** $F_2$ empieza con $2$. $F_1$ empieza con $1$. Queremos que $2 + k \cdot 1 = 0$, o sea $k = -2$. Entonces restamos $2$ veces $F_1$ a $F_2$:

$$F_2 \leftarrow F_2 - 2 F_1$$

**Cálculo entrada por entrada** (OJO: solo cambia $F_2$, $F_1$ queda intacta):

- Columna 1 de nueva $F_2$: $\; 2 - 2 \cdot 1 = 2 - 2 = \mathbf{0}$ ✓ (ese es el cero que buscábamos)
- Columna 2 de nueva $F_2$: $\; -1 - 2 \cdot 1 = -1 - 2 = \mathbf{-3}$
- Término indep. de nueva $F_2$: $\; 0 - 2 \cdot 3 = 0 - 6 = \mathbf{-6}$

Reemplazamos $F_2$ por el resultado. $F_1$ no se tocó:

$$\left(\begin{array}{cc|c} 1 & 1 & 3 \\ 0 & -3 & -6 \end{array}\right)$$

**Esta es la matriz escalerizada.** Tiene forma de escalera: la fila 1 empieza en la columna 1, la fila 2 empieza en la columna 2. Ya terminamos de escalerizar.

---

### Paso 4 — Clasificar

Mirá la matriz escalerizada:
- Cantidad de incógnitas: $n = 2$ (tenemos $x$ e $y$).
- Cantidad de filas no nulas (ecuaciones efectivas): $p = 2$. **Ninguna** fila se anuló.
- Ninguna fila tiene forma $(0, 0 \mid k \neq 0)$ (o sea, no hay incompatibilidad).

Es una **escalera perfecta** con tantos escalones como incógnitas → **SCD** (sistema compatible determinado, solución única).

---

### Paso 5 — Resolver (back-substitution: de abajo hacia arriba)

Traducimos cada fila de la matriz escalerizada de vuelta a ecuación:

- Fila 1: $1 \cdot x + 1 \cdot y = 3$, o sea $x + y = 3$.
- Fila 2: $0 \cdot x + (-3) \cdot y = -6$, o sea $-3y = -6$.

**Ahora empezamos por la última (la más fácil) y subimos:**

**Despejar $y$ de la fila 2:**

$$-3y = -6 \;\Rightarrow\; y = \frac{-6}{-3} = 2$$

Entonces $y = 2$.

**Despejar $x$ de la fila 1 sustituyendo $y = 2$:**

$$x + y = 3 \;\Rightarrow\; x + 2 = 3 \;\Rightarrow\; x = 3 - 2 = 1$$

Entonces $x = 1$.

### Solución final

$$\boxed{x = 1, \quad y = 2}$$

---

### Paso 6 — Verificar (opcional pero muy recomendado)

Sustituimos $x = 1$ e $y = 2$ en las ecuaciones **originales** (no en las escalerizadas — en las del enunciado):

- Ecuación 1: $2 \cdot 1 - 2 = 2 - 2 = 0$ ✓
- Ecuación 2: $1 + 2 = 3$ ✓

Las dos se cumplen → la solución está bien.

---

### Interpretación geométrica (bonus)

Cada ecuación lineal de 2 variables representa **una recta** en el plano. El sistema pide los puntos que están en **las dos rectas al mismo tiempo**.

- Recta 1: $2x - y = 0$ ⇒ $y = 2x$ (pasa por el origen, pendiente $2$).
- Recta 2: $x + y = 3$ (pasa por $(3,0)$ y $(0,3)$).

Las dos rectas se cortan en **un solo punto: $(1, 2)$**. Ese punto es exactamente la solución.

**Regla visual:**

| Cómo se ven las rectas | Clasificación | Soluciones |
|------------------------|---------------|-----------|
| Se cortan en un punto | **SCD** | Una (el punto de corte) |
| Son paralelas (nunca se cortan) | **SI** | Ninguna |
| Son coincidentes (la misma recta) | **SCI** | Infinitas |

---

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxx  EJEMPLO PRÁCTICO S2 — Sistema 2×2 SI  xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Ejemplo S2: Sistema 2×2, incompatible

**Mismo procedimiento que S1, pero este va a dar "sin solución".**

### El problema

$$\begin{cases} x - y = 1 \\ -2x + 2y = 4 \end{cases}$$

### Paso 1 — Matriz ampliada

Coeficientes y términos independientes:

$$\left(\begin{array}{cc|c} 1 & -1 & 1 \\ -2 & 2 & 4 \end{array}\right)$$

$F_1 = (1, -1, 1)$ y $F_2 = (-2, 2, 4)$.

### Paso 2 — Generar el cero en $(2,1)$

Queremos que el $-2$ en la posición $(2,1)$ se vuelva $0$. Como $F_1$ empieza con $1$, si le sumamos $2$ veces $F_1$ a $F_2$, la primera entrada queda en cero: $-2 + 2 \cdot 1 = 0$.

**Operación:** $F_2 \leftarrow F_2 + 2 F_1$

**Cálculo entrada por entrada:**

- Columna 1: $-2 + 2 \cdot 1 = -2 + 2 = \mathbf{0}$ ✓
- Columna 2: $2 + 2 \cdot (-1) = 2 - 2 = \mathbf{0}$
- Término indep.: $4 + 2 \cdot 1 = 4 + 2 = \mathbf{6}$

Matriz resultante:

$$\left(\begin{array}{cc|c} 1 & -1 & 1 \\ 0 & 0 & 6 \end{array}\right)$$

### Paso 3 — Clasificar (acá viene lo distinto)

Mirá la fila 2: $(0, 0 \mid 6)$. Traducida a ecuación dice:

$$0 \cdot x + 0 \cdot y = 6 \;\; \Longleftrightarrow \;\; 0 = 6$$

Eso es **imposible**. No existe ningún par de valores $(x, y)$ que haga que $0$ sea igual a $6$. Pase lo que pase con $x$ e $y$, el lado izquierdo va a dar siempre cero.

→ **Sistema incompatible (SI)**. **No tiene solución.** Fin del ejercicio.

**Importante:** cuando una fila queda $(0, 0, \ldots, 0 \mid k)$ con $k \neq 0$, **no** tenés que seguir resolviendo — ya sabés que no hay solución, escribí "SI" y terminá.

### Geométricamente

- Recta 1: $x - y = 1$
- Recta 2: $-2x + 2y = 4$ ⇒ dividiendo ambos lados por $-2$: $x - y = -2$

Las dos rectas tienen la **misma pendiente** (la misma forma $x - y$), pero distinto término independiente ($1$ vs. $-2$). Entonces son **paralelas no coincidentes** → nunca se cortan → no hay punto en común → no hay solución.

---

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxx  EJEMPLO PRÁCTICO S3 — Sistema 2×2 SCI  xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Ejemplo S3: Sistema 2×2, compatible indeterminado

**Mismo procedimiento, pero este va a tener infinitas soluciones. Te muestra cómo escribir la solución con parámetros.**

### El problema

$$\begin{cases} 2x - y = 1 \\ -4x + 2y = -2 \end{cases}$$

### Paso 1 — Matriz ampliada

$$\left(\begin{array}{cc|c} 2 & -1 & 1 \\ -4 & 2 & -2 \end{array}\right)$$

### Paso 2 — Generar el cero en $(2,1)$

$F_2$ empieza con $-4$, $F_1$ empieza con $2$. Si le sumamos $2$ veces $F_1$ a $F_2$, la primera entrada queda en cero: $-4 + 2 \cdot 2 = 0$.

**Operación:** $F_2 \leftarrow F_2 + 2 F_1$

**Cálculo entrada por entrada:**

- Columna 1: $-4 + 2 \cdot 2 = -4 + 4 = \mathbf{0}$ ✓
- Columna 2: $2 + 2 \cdot (-1) = 2 - 2 = \mathbf{0}$
- Término indep.: $-2 + 2 \cdot 1 = -2 + 2 = \mathbf{0}$

Matriz resultante:

$$\left(\begin{array}{cc|c} 2 & -1 & 1 \\ 0 & 0 & 0 \end{array}\right)$$

### Paso 3 — Clasificar

Mirá la fila 2: $(0, 0 \mid 0)$. Traducida a ecuación dice $0 = 0$, que **siempre se cumple** — no nos restringe nada. **Perdimos una ecuación** durante el proceso (significa que la ecuación 2 del sistema original era solo la 1 multiplicada por algún número; no aportaba información nueva).

**Conteo:**
- Incógnitas: $n = 2$ ($x$, $y$).
- Ecuaciones efectivas: $p = 1$ (solo la fila 1 no es nula; la fila 2 se anuló).
- Grados de libertad: $r = n - p = 2 - 1 = 1$.

→ **SCI** (sistema compatible indeterminado) con **1 grado de libertad** → infinitas soluciones, se expresan usando **1 letra griega** (alfa).

### Paso 4 — Resolver usando el parámetro $\alpha$

La única ecuación efectiva es la fila 1, que dice $2x - y = 1$.

**La idea:** como tenemos 1 grado de libertad, **una de las dos incógnitas es "libre"** — podemos elegir cualquier valor — y la otra queda determinada por la ecuación.

**Elegimos cuál es libre.** En este caso, tomemos $x$ como la libre. Le damos el nombre $\alpha$:

$$x = \alpha$$

Esto literalmente dice: "llamá $\alpha$ al valor de $x$, que puede ser cualquier número real".

**Despejamos $y$ de la ecuación** ($2x - y = 1$) sustituyendo $x = \alpha$:

$$2\alpha - y = 1$$
$$-y = 1 - 2\alpha$$
$$y = 2\alpha - 1$$

Entonces $y$ queda en función de $\alpha$.

### Solución final

$$\boxed{x = \alpha, \quad y = 2\alpha - 1, \quad \text{con } \alpha \in \mathbb{R}}$$

Eso significa: **para cada valor de $\alpha$ que elijas, obtenés una solución distinta**. Por ejemplo:
- Si $\alpha = 0$: $(x, y) = (0, -1)$. Verificamos: $2(0) - (-1) = 1$ ✓
- Si $\alpha = 1$: $(x, y) = (1, 1)$. Verificamos: $2(1) - 1 = 1$ ✓
- Si $\alpha = 5$: $(x, y) = (5, 9)$. Verificamos: $2(5) - 9 = 1$ ✓

Todos los pares $(\alpha, 2\alpha - 1)$ son soluciones. Son infinitos.

### Geométricamente

Si dividís la segunda ecuación original por $-2$: $-4x + 2y = -2$ queda $2x - y = 1$ — **la misma que la ecuación 1**. Las dos rectas son **coincidentes** (son la misma recta dibujada dos veces). Todos los puntos de esa recta son solución → infinitas soluciones.

---

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxx  EJEMPLO PRÁCTICO 4×3 — SCI, 1 grado libertad  xxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Ejemplo de 4 ecuaciones y 3 incógnitas (SCI con 1 grado de libertad)

**Acá ves un sistema "más grande" donde varias filas se anulan. Es similar al tipo de ejercicio de parcial.**

### El problema

$$\begin{cases} x + 2y + z = 3 \\ 3x + 6y + z = 9 \\ 4x + 8y + 2z = 12 \\ x + 3y + 3z = 3 \end{cases}$$

Tres incógnitas ($x, y, z$) y cuatro ecuaciones.

### Paso 1 — Matriz ampliada

$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 3 & 6 & 1 & 9 \\ 4 & 8 & 2 & 12 \\ 1 & 2 & 1 & 3 \end{array}\right)$$

**Observación antes de empezar** (esto ahorra tiempo): mirá $F_1$ y $F_4$ — son idénticas. Eso te dice que $F_4$ se va a anular al escalerizar, adelantando que probablemente el sistema sea SCI.

### Paso 2 — Generar ceros en la columna 1, usando $F_1$ como pivote

Queremos convertir en $0$ las primeras entradas de $F_2, F_3, F_4$. Para cada fila, pensamos qué múltiplo de $F_1$ hay que restar.

**Para $F_2$:** $F_2$ empieza con $3$. Queremos $3 - k \cdot 1 = 0$, entonces $k = 3$. Operación: $F_2 \leftarrow F_2 - 3 F_1$.

Cálculo de la nueva $F_2$:
- Col 1: $3 - 3 \cdot 1 = 0$ ✓
- Col 2: $6 - 3 \cdot 2 = 6 - 6 = 0$
- Col 3: $1 - 3 \cdot 1 = -2$
- Término indep: $9 - 3 \cdot 3 = 0$

Entonces nueva $F_2 = (0, 0, -2, 0)$.

**Para $F_3$:** $F_3$ empieza con $4$. Entonces $k = 4$. Operación: $F_3 \leftarrow F_3 - 4 F_1$.

- Col 1: $4 - 4 \cdot 1 = 0$ ✓
- Col 2: $8 - 4 \cdot 2 = 0$
- Col 3: $2 - 4 \cdot 1 = -2$
- Término indep: $12 - 4 \cdot 3 = 0$

Nueva $F_3 = (0, 0, -2, 0)$.

**Para $F_4$:** $F_4$ empieza con $1$, igual que $F_1$. Entonces $k = 1$. Operación: $F_4 \leftarrow F_4 - F_1$.

- Col 1: $1 - 1 = 0$ ✓
- Col 2: $2 - 2 = 0$
- Col 3: $1 - 1 = 0$
- Término indep: $3 - 3 = 0$

Nueva $F_4 = (0, 0, 0, 0)$ — fila entera anulada. (Confirma lo que adelantamos: $F_4$ era idéntica a $F_1$.)

**Matriz después del paso 2:**

$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

### Paso 3 — Eliminar $F_3$ porque es igual a $F_2$

$F_2$ y $F_3$ son idénticas. Hacemos $F_3 \leftarrow F_3 - F_2$ y $F_3$ se anula:

- Col 1: $0 - 0 = 0$
- Col 2: $0 - 0 = 0$
- Col 3: $-2 - (-2) = 0$
- Término indep: $0 - 0 = 0$

**Matriz escalerizada final:**

$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

### Paso 4 — Clasificar

**Conteo:**
- Incógnitas: $n = 3$ ($x, y, z$).
- Ecuaciones efectivas (filas no nulas): $p = 2$ (solo $F_1$ y $F_2$ tienen contenido; $F_3$ y $F_4$ son nulas).
- Grados de libertad: $r = n - p = 3 - 2 = 1$.

Ninguna fila tiene forma $(0, 0, 0 \mid k \neq 0)$, así que no es SI.

→ **SCI con 1 grado de libertad** → infinitas soluciones, expresadas con **1 letra griega** (alfa).

### Paso 5 — Resolver usando $\alpha$

Traducimos las dos filas no nulas a ecuaciones:

- Fila 1: $x + 2y + z = 3$
- Fila 2: $0 \cdot x + 0 \cdot y + (-2) \cdot z = 0$, o sea $-2z = 0$, que simplifica a $z = 0$.

**Pensar cuál incógnita tomar como libre.** Fila 2 ya fija $z = 0$. Nos queda la fila 1 con $x + 2y + 0 = 3$, o sea $x + 2y = 3$. Esa ecuación relaciona $x$ con $y$, pero ninguna está fijada individualmente — podemos elegir **una de las dos** libremente.

**Tomamos $y$ como la libre** (podría ser $x$, pero $y$ sale más limpio). Llamamos $y = \alpha$.

**Despejamos $x$** de $x + 2y = 3$ sustituyendo $y = \alpha$:

$$x + 2\alpha = 3 \;\Rightarrow\; x = 3 - 2\alpha$$

### Solución final

$$\boxed{x = 3 - 2\alpha, \quad y = \alpha, \quad z = 0, \quad \text{con } \alpha \in \mathbb{R}}$$

**Chequeo rápido con $\alpha = 0$:** $(x, y, z) = (3, 0, 0)$. Verificamos en la ecuación 1 original: $3 + 0 + 0 = 3$ ✓. Ecuación 2: $3 \cdot 3 + 0 + 0 = 9$ ✓. Funciona.

**Chequeo con $\alpha = 1$:** $(x, y, z) = (1, 1, 0)$. Ecuación 1: $1 + 2 + 0 = 3$ ✓. Ecuación 2: $3 + 6 + 0 = 9$ ✓.

Infinitas soluciones posibles, todas con esa forma.

### Resolver

De la fila 2: $-2z = 0 \Rightarrow z = 0$.

De la fila 1: $x + 2y + z = 3 \Rightarrow x + 2y = 3$.

Tomamos $x = \alpha$ (el grado de libertad):

$$2y = 3 - \alpha \Rightarrow y = \frac{3 - \alpha}{2}$$

**Solución general:** $\quad x = \alpha, \quad y = \dfrac{3 - \alpha}{2}, \quad z = 0$.

> "En este caso tenemos una matriz digamos no cuadrada porque tenemos tres incógnitas y cuatro ecuaciones. No tiene por qué ser cuadrada. Hablamos de $m$ por $n$ y no tiene por qué coincidir"

**Traducción:** el sistema puede tener cualquier cantidad de ecuaciones y de incógnitas (no tiene que ser la misma). La matriz de coeficientes $A$ puede ser rectangular.

---

## Adelanto de lo que viene: la triple equivalencia

> "Si el determinante de $A$ distinto de $0$, el sistema es compatible determinado y $A$ tiene inversa"

La clase que viene (clase 9) se va a demostrar que estos **tres enunciados son equivalentes** (todos iguales entre sí):

1. $\det(A) \neq 0$
2. $A$ es invertible
3. $A \cdot x = B$ es un sistema compatible determinado (para todo $B$)

Ya sabíamos que los primeros dos son equivalentes (Teoremas 1 y 2 de determinantes). Hoy nos adelantan que el tercero también entra en el grupo. Esto junta matrices, determinantes y sistemas en un solo concepto.

---

# PARTE 2 — Sistema con parámetro, inversa por escalerización, triple equivalencia (Clase 9, 21 de abril)

## La Gran Pregunta de Hoy: ¿Cómo resuelvo un sistema cuando aparece un parámetro? ¿Cómo calculo la inversa por escalerización? ¿Cómo se conectan determinante, invertibilidad y clasificación del sistema?

Hoy se ve:
1. **Sistema con parámetro** — cuando uno de los coeficientes es una letra variable y hay que discutir según valores.
2. **Inversa por escalerización** (método de Gauss) — la tercera forma de calcular $A^{-1}$, además del método directo y cofactores.
3. **Triple equivalencia** — el teorema que cierra todo.
4. **Despeje matricial** $x = A^{-1} B$ — cómo resolver un sistema usando la inversa.

---

## Conexión con la Clase Anterior

La clase 8 introdujo sistemas de ecuaciones, la clasificación, la matriz ampliada, el método de escalerización y las tres formas escalonadas. Hoy se aplica todo eso a un sistema con parámetro y se cierra el teórico del tema con la triple equivalencia.

---

## Sistema con parámetro

### Paso 1: ¿Qué es un "parámetro"?

Hasta ahora todos los sistemas que vimos tenían **solo números** como coeficientes (cosas como $2, -3, 5$). Un **sistema con parámetro** es uno donde uno o más coeficientes son **una letra** en vez de un número.

Por ejemplo:

$$\begin{cases} x + y = 3 \\ 2x + \lambda y = 6 \end{cases}$$

Fijate el $\lambda$ (lambda, letra griega) multiplicando a $y$ en la segunda ecuación. Esa letra **no es una incógnita** como $x$ o $y$ — es un **parámetro**, que representa un número desconocido pero **fijo** (aunque nosotros no sepamos cuál).

**Para aclarar la diferencia:**

| Letra | ¿Qué es? | ¿Se resuelve para ella? |
|-------|----------|-------------------------|
| $x$, $y$, $z$ | Incógnitas | Sí — buscamos sus valores |
| $\lambda$, $a$, $m$, $k$ | Parámetros | No — los tratamos como "un número cualquiera" que el ejercicio nos da |

### Paso 2: ¿Por qué existen?

En la vida real, muchas veces tenés un sistema cuya forma es fija, pero algunos coeficientes **dependen de una variable externa**. Por ejemplo: resistencias eléctricas que dependen de la temperatura, precios que dependen del dólar, etc. El parámetro representa esa variable externa.

En el parcial, el parámetro aparece porque **permite preguntar cosas más ricas**: no "resolvé este sistema" (respuesta única), sino "decime cómo se comporta este sistema según cuánto valga $\lambda$" (respuesta con varios casos).

### Paso 3: La gran diferencia con un sistema normal

En un sistema sin parámetro, hay **una sola** clasificación: o es SCD, o es SCI, o es SI. Punto.

En un sistema con parámetro, **la clasificación puede cambiar según el valor del parámetro**. El mismo sistema, con distintos valores de $\lambda$, puede dar:

- SCD para algunos valores de $\lambda$.
- SCI para otros valores.
- SI para otros valores.

**Ejemplo intuitivo:** imaginá el sistema de arriba con $\lambda = 2$:

$$\begin{cases} x + y = 3 \\ 2x + 2y = 6 \end{cases}$$

La segunda ecuación es el doble de la primera — son redundantes → **SCI**.

Pero si $\lambda = 5$:

$$\begin{cases} x + y = 3 \\ 2x + 5y = 6 \end{cases}$$

Ya no son proporcionales, son dos condiciones independientes → **SCD**.

**Misma forma del sistema, distinta clasificación según $\lambda$.** Eso es lo que hace interesantes (y complicados) los sistemas con parámetro.

### Paso 4: Lo que se pide en el parcial

"Discutir el sistema según el parámetro" significa:

1. **Escalerizar normalmente** (tratando al parámetro como si fuera un número cualquiera).
2. Cuando quieras **dividir por una expresión** que contiene el parámetro, **detenerte** y preguntarte: "¿esta expresión podría valer $0$?".
3. Si puede valer $0$, encontrar los **valores del parámetro** que la anulan. A esos los llamamos **valores críticos**.
4. **Caso general:** resolver normalmente suponiendo que el parámetro NO toma ningún valor crítico.
5. **Por cada valor crítico:** sustituir en la matriz escalerizada, ver qué tipo de sistema queda, y resolverlo aparte.
6. Armar un **cuadro resumen** con todos los casos.

### Paso 5: La trampa típica — cuándo podés dividir

Esta es la parte más delicada. Cuando al escalerizar te queda una expresión como $(\lambda - 3) \cdot y = 5$, te **tentás** a despejar $y = \frac{5}{\lambda - 3}$. Pero ojo: **solo podés dividir si $\lambda - 3 \neq 0$**, o sea, si $\lambda \neq 3$.

¿Qué hay que hacer?

- **Caso $\lambda \neq 3$** (caso general): dividís tranquilo, $y = \frac{5}{\lambda - 3}$.
- **Caso $\lambda = 3$** (valor crítico): la ecuación te queda "$0 \cdot y = 5$", o sea, imposible → **SI**.

El valor crítico ($\lambda = 3$) es el que anula la expresión por la que querías dividir. Esos son los valores que hay que tratar aparte.

### Paso 6: Las letras más comunes

Las letras que usan los profesores para parámetros (para no confundir con incógnitas):

| Letra | Nombre | Dónde aparece |
|-------|--------|---------------|
| $a$ | a | Muy común |
| $\lambda$ | lambda | Muy común, del álgebra lineal clásica |
| $m$ | eme | Común en clase |
| $k$ | ka | Común en ejercicios |
| $t$ | te | A veces |

**Importante:** estas letras son **parámetros** (valores fijos pero desconocidos), no se confunden con las **letras griegas de grados de libertad** ($\alpha, \beta, \gamma$), que representan "valores que vos elegís libremente". Son cosas distintas a pesar de que ambas sean letras.

> "Esta $a$ puede tomar infinitos valores reales, y vamos a decir que, bueno, si $a$ toma este valor es compatible determinado, si $a$ toma este y otro es incompatible, y si $a$ toma este y otro es compatible indeterminado"

---

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxx  EJEMPLO PRÁCTICO — Sistema 3×3 con parámetro  xxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Ejemplo completo: sistema 3×3 con parámetro $a$

### Enunciado

$$\begin{cases} a \cdot x + y + z = 1 \\ x + a \cdot y + z = 1 \\ x + y + a \cdot z = a^2 \end{cases}$$

### Paso 1 — Matriz ampliada

$$\left(\begin{array}{ccc|c} a & 1 & 1 & 1 \\ 1 & a & 1 & 1 \\ 1 & 1 & a & a^2 \end{array}\right)$$

### Paso 2 — Escalerizar en dos pasos

**Operación 1:** $F_2 \leftarrow F_2 - F_1$, $F_3 \leftarrow F_3 - a \cdot F_1$

- Nueva fila 2: $(1-a, \; a-1, \; 0, \; 0)$
- Nueva fila 3: $(1-a^2, \; 1-a, \; 0, \; a^2 - a)$

$$\left(\begin{array}{ccc|c} a & 1 & 1 & 1 \\ 1-a & a-1 & 0 & 0 \\ 1-a^2 & 1-a & 0 & a^2-a \end{array}\right)$$

**Operación 2:** $F_3 \leftarrow F_3 + F_2$

- Nueva fila 3 columna 1: $(1-a^2) + (1-a) = -a^2 - a + 2$
- Nueva fila 3 columna 2: $(1-a) + (a-1) = 0$
- Nueva fila 3 columna 3: $0 + 0 = 0$
- Nueva fila 3 término indep: $(a^2-a) + 0 = a^2 - a$

$$\left(\begin{array}{ccc|c} a & 1 & 1 & 1 \\ 1-a & a-1 & 0 & 0 \\ -a^2-a+2 & 0 & 0 & a^2-a \end{array}\right)$$

(Nota: en la clase el profesor escaleró en el sentido inverso al de ejemplos anteriores, dejando el escalón avanzando hacia la izquierda en vez de la derecha. Es equivalente.)

### Paso 3 — Despejar $x$ y encontrar las condiciones sobre $a$

De la fila 3: $(-a^2 - a + 2) \cdot x = a^2 - 1$.

> "Siempre y cuando, ¿qué tiene que pasar? $-a^2 - a + 2$ todo eso tiene que ser distinto de $0$"

**Traducción:** para poder despejar $x$, tenemos que poder dividir por $(-a^2 - a + 2)$. Y solo podemos dividir si ese número es $\neq 0$. Si es $0$, pasa algo raro y tenemos que analizar por separado.

### Paso 3.1 — Encontrar las raíces de $-a^2 - a + 2 = 0$

Usamos la fórmula resolvente ($-a^2 - a + 2 = 0$):

$$a = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(-1)(2)}}{2(-1)} = \frac{1 \pm \sqrt{1 + 8}}{-2} = \frac{1 \pm 3}{-2}$$

- $a = \dfrac{1+3}{-2} = -2$
- $a = \dfrac{1-3}{-2} = 1$

Los **valores problemáticos** son $a = -2$ y $a = 1$.

### Paso 3.2 — Factorizar el denominador

$$-a^2 - a + 2 = -(a + 2)(a - 1)$$

### Paso 3.3 — Despejar $x$ cuando $a \neq -2$ y $a \neq 1$

$$x = \frac{a^2 - 1}{-(a+2)(a-1)}$$

Usamos la identidad $a^2 - 1 = (a+1)(a-1)$:

$$x = \frac{(a+1)(a-1)}{-(a+2)(a-1)} = -\frac{a+1}{a+2}$$

El $(a-1)$ se cancela (podemos cancelar porque estamos en el caso $a \neq 1$).

### Paso 4 — Despejar $y$ y $z$

De la ecuación 2 ($(1-a) x + (a-1) y = 0$), dividiendo por $(a-1)$ (podemos porque $a \neq 1$):

$$-x + y = 1 \Rightarrow y = 1 + x = 1 - \frac{a+1}{a+2} = \frac{(a+2) - (a+1)}{a+2} = \frac{1}{a+2}$$

De la ecuación 1 ($a x + y + z = 1$), sustituyendo los valores:

$$z = 1 - a \cdot \left(-\frac{a+1}{a+2}\right) - \frac{1}{a+2} = \frac{(a+2) + a(a+1) - 1}{a+2} = \frac{a^2 + 2a + 1}{a+2} = \frac{(a+1)^2}{a+2}$$

(El numerador es el cuadrado del binomio.)

### Paso 5 — Analizar los casos problemáticos

#### Caso $a = 1$

Sustituimos $a = 1$ en la matriz ampliada escalerizada:

$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

Dos filas se anularon. Una sola ecuación efectiva ($p = 1$) con tres incógnitas ($n = 3$) → $r = 2$ grados de libertad → **SCI**.

La única ecuación es $x + y + z = 1$. Tomamos $y = \alpha$, $z = \beta$:

$$x = 1 - \alpha - \beta$$

**Solución:** $\quad x = 1 - \alpha - \beta, \quad y = \alpha, \quad z = \beta, \quad \alpha, \beta \in \mathbb{R}$.

#### Caso $a = -2$

Sustituimos $a = -2$ en la matriz ampliada escalerizada. La fila 3 era $(-a^2 - a + 2, \; 0, \; 0, \; a^2 - a)$:

$$(-4 + 2 + 2, \; 0, \; 0, \; 4 - (-2)) = (0, \; 0, \; 0, \; 6)$$

Es decir: "$0 \cdot x + 0 \cdot y + 0 \cdot z = 6$", que es imposible → **SI**.

### Paso 6 — Cuadro resumen

| Valor de $a$ | Clasificación | Solución |
|--------------|---------------|----------|
| $a \neq -2$ y $a \neq 1$ | SCD | $x = -\dfrac{a+1}{a+2}, \; y = \dfrac{1}{a+2}, \; z = \dfrac{(a+1)^2}{a+2}$ |
| $a = 1$ | SCI (2 grados de libertad) | $x = 1 - \alpha - \beta, \; y = \alpha, \; z = \beta$ |
| $a = -2$ | SI | — |

> "Entonces bueno, tenemos esa complejidad en las cuentas, pero el procedimiento es el mismo"

**Traducción:** con parámetros, **las cuentas se complican pero el método es el mismo** — escalerizar, clasificar, resolver. Lo que se agrega es ir detectando condiciones sobre el parámetro (cuándo hay que dividir, cuándo hay que factorizar) y discutir aparte los valores que rompen esas condiciones.

---

## Inversa por escalerización (método de Gauss)

### Paso 1: ¿Qué problema estamos resolviendo?

Queremos **calcular la inversa** de una matriz $A$. Ya conocemos dos métodos de antes:

| Método | Cuándo se vio | Cómo funciona |
|--------|---------------|---------------|
| **Directo** | Unidad de matrices | Plantear un sistema con las entradas de $A^{-1}$ como incógnitas |
| **Cofactores** | Unidad de determinantes | $A^{-1} = \frac{1}{\det(A)} \cdot C_A^T$ |

Hoy agregamos el **tercer método**: por escalerización (también llamado **método de Gauss**).

### Paso 2: La idea — lo que vamos a hacer

El método se resume en una línea:

$$(A \mid I) \xrightarrow{\text{escalerizar}} (I \mid A^{-1})$$

**En palabras:**

1. Agarrás la matriz $A$ y la ponés a la izquierda.
2. Pegás a la derecha la matriz identidad $I$ (del mismo tamaño que $A$), separada por una barra.
3. Aplicás operaciones de escalerización **a toda esa matriz grande** hasta que la parte de la izquierda (donde antes estaba $A$) se convierta en $I$.
4. Cuando eso pasa, **lo que quedó a la derecha es $A^{-1}$**.

Suena raro y mágico. La sección siguiente explica por qué funciona.

### Paso 3: ¿Por qué funciona? — la intuición

Acordate del despeje matricial: calcular $A^{-1}$ es lo mismo que encontrar una matriz $X$ tal que $A \cdot X = I$.

**La matriz $X$ es la inversa que buscamos.** Le pusimos el nombre $X$ porque es la incógnita del problema; cuando la encontremos, será $A^{-1}$.

Ahora, acá viene el truco: **pensemos a $X$ por columnas**. Toda matriz se puede ver como un conjunto de columnas pegadas. Si $A$ es $3 \times 3$, entonces $X$ también es $3 \times 3$, y tiene tres columnas. Las llamamos $X_1$, $X_2$, $X_3$:

$$X = \left(\; X_1 \;\mid\; X_2 \;\mid\; X_3 \;\right)$$

Cada $X_i$ es un vector columna (con 3 entradas). Cuando hacés $A \cdot X$, el resultado también se puede ver por columnas: la $i$-ésima columna del resultado es $A \cdot X_i$.

Entonces $A \cdot X = I$ se descompone en **tres ecuaciones matriciales separadas**, una por columna:

$$A \cdot X_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad A \cdot X_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad A \cdot X_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

(Las columnas de la derecha son las columnas de $I$.)

**Cada una de esas tres ecuaciones es un sistema de 3 ecuaciones con 3 incógnitas** (las 3 entradas de $X_i$). Todos comparten la **misma matriz de coeficientes $A$**, pero tienen **términos independientes distintos** (las columnas de $I$).

### Paso 4: La idea de "resolver los tres a la vez"

Podríamos resolver los tres sistemas por separado, escalerizando tres veces. Pero **sería muy repetitivo** — estaríamos haciendo las mismas operaciones de filas sobre $A$ tres veces, cambiando solo el término independiente.

**La optimización:** resolver los tres sistemas **en paralelo**, pegándolos lado a lado. Eso es lo que hace la matriz ampliada $(A \mid I)$: en vez de una columna a la derecha (como cuando tenemos un solo sistema), pone **tres columnas** (una por cada sistema).

Cuando escalerizás $(A \mid I)$, cada operación de fila se aplica a **toda la fila grande** — los coeficientes de $A$ **y** las tres columnas de términos independientes se actualizan al mismo tiempo.

Cuando llegás a la forma "$(I \mid \text{algo})$", el "algo" son **las tres soluciones**, que juntas forman $A^{-1}$.

> "Estoy resolviendo estos $n$ sistemas a la vez, hallando $X_1, X_2, \ldots, X_n$, y por lo tanto hallando la inversa"

### Paso 5: Procedimiento paso a paso (resumido)

1. **Armar $(A \mid I)$:** a la izquierda ponés $A$, a la derecha la identidad del mismo tamaño, separadas por una barra vertical.
2. **Escalerizar:** aplicar las tres operaciones (intercambiar filas, multiplicar fila por $k \neq 0$, sumar múltiplo de una fila a otra) **sobre la matriz ampliada completa**. Cada operación afecta a TODA la fila, incluyendo el lado derecho.
3. **Objetivo:** llegar a la forma $(I \mid \text{algo})$, o sea, que la parte izquierda sea la identidad.
4. **Leer el resultado:** cuando la izquierda es $I$, la derecha es $A^{-1}$.

### Paso 6: Dos notas importantes

**Nota 1 — Diferencia con escalerización normal.** Cuando escalerizás para resolver un sistema, te basta con llegar a "forma de escalera" (ceros abajo de la diagonal). Acá tenés que ir **más lejos**: también necesitás ceros **arriba** de la diagonal, y unos en la diagonal. Eso se llama **forma reducida por filas** (o Gauss-Jordan).

**Nota 2 — Si la matriz NO es invertible.** Si $A$ no tiene inversa, al escalerizar **nunca vas a poder** hacer que la parte izquierda sea $I$. En algún momento te va a quedar una fila de ceros a la izquierda, que te delata que $A$ no es invertible.

### Cuándo conviene este método

> "Cuando la matriz $A$ es lo más parecida a la matriz identidad, este método es más fácil. Si hay que aplicar 300 pasos para llegar a la identidad, me complico más, me conviene más el método directo o el cofactor"

**Traducción:** si $A$ ya se parece bastante a la identidad (muchos $1$ en la diagonal, muchos $0$ fuera de la diagonal), este método es muy rápido porque tenés que "corregir" poco. Si $A$ es muy distinta de $I$, los tres métodos cuestan más o menos lo mismo — usá el que prefieras.

---

```
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxx  EJEMPLO PRÁCTICO — Inversa por escalerización  xxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Ejemplo completo: inversa por escalerización

### Enunciado

Calcular la inversa de:

$$A = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

### Paso 1 — Armar $(A \mid I)$

$$\left(\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 & 1 & 0 \\ 0 & 1 & 1 & 0 & 0 & 1 \end{array}\right)$$

### Paso 2 — Generar un $0$ en la posición $(2,1)$

$F_2 \leftarrow F_2 - F_1$:

$$\left(\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & -1 & 0 & -1 & 1 & 0 \\ 0 & 1 & 1 & 0 & 0 & 1 \end{array}\right)$$

### Paso 3 — Generar un $0$ en la posición $(3,2)$

$F_3 \leftarrow F_3 + F_2$:

$$\left(\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & -1 & 0 & -1 & 1 & 0 \\ 0 & 0 & 1 & -1 & 1 & 1 \end{array}\right)$$

### Paso 4 — Generar un $0$ en la posición $(1,2)$

$F_1 \leftarrow F_1 + F_2$:

$$\left(\begin{array}{ccc|ccc} 1 & 0 & 0 & 0 & 1 & 0 \\ 0 & -1 & 0 & -1 & 1 & 0 \\ 0 & 0 & 1 & -1 & 1 & 1 \end{array}\right)$$

### Paso 5 — Convertir el $-1$ de la fila 2 en un $1$

$F_2 \leftarrow -F_2$:

$$\left(\begin{array}{ccc|ccc} 1 & 0 & 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & -1 & 1 & 1 \end{array}\right)$$

La parte izquierda es la identidad → la parte derecha es $A^{-1}$:

$$A^{-1} = \begin{pmatrix} 0 & 1 & 0 \\ 1 & -1 & 0 \\ -1 & 1 & 1 \end{pmatrix}$$

### Verificación

Podemos verificar haciendo $A \cdot A^{-1}$ y viendo que da $I$. Tomando la primera columna:

$A \cdot \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 \cdot 0 + 1 \cdot 1 + 0 \cdot (-1) \\ 1 \cdot 0 + 0 \cdot 1 + 0 \cdot (-1) \\ 0 \cdot 0 + 1 \cdot 1 + 1 \cdot (-1) \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \checkmark$

(Las otras columnas dan $(0,1,0)^T$ y $(0,0,1)^T$.)

---

## La triple equivalencia

Esta sección junta **tres cosas** que aparentemente eran separadas (determinante, invertibilidad, clasificación de sistemas) y muestra que son **una misma cosa** mirada desde tres ángulos. Es uno de los teoremas más importantes del curso.

### Paso 1: Recordemos las tres cosas separadas

**Cosa 1 — Determinante de una matriz.** En la unidad de determinantes aprendimos a calcular un número $\det(A)$ a partir de una matriz cuadrada $A$. Ese número puede valer $0$ o puede ser distinto de $0$.

**Cosa 2 — Invertibilidad de una matriz.** Una matriz $A$ es **invertible** si existe otra matriz $A^{-1}$ tal que $A \cdot A^{-1} = I$. Si no existe tal matriz, $A$ es **no invertible**.

**Cosa 3 — Clasificación de un sistema.** Un sistema $A \cdot x = B$ se clasifica como SCD (una solución), SCI (infinitas) o SI (ninguna).

Hasta ahora cada una vivía por su lado. La triple equivalencia dice: **están todas unidas**.

### Paso 2: El enunciado

Para cualquier matriz cuadrada $A$ (de tamaño $n \times n$), los siguientes **tres enunciados son equivalentes entre sí**:

| Enunciado | Lo que dice |
|-----------|-------------|
| (1) $\det(A) \neq 0$ | El determinante no es cero |
| (2) $A$ es invertible | Existe $A^{-1}$ |
| (3) $A \cdot x = B$ es SCD para cualquier $B$ | El sistema siempre tiene solución única |

### Paso 3: ¿Qué significa "equivalentes entre sí"?

Significa que **si uno vale, los otros dos también valen**. Y si uno NO vale, los otros dos tampoco.

No es que uno cause a los otros — son **la misma información**, dicha de tres formas distintas.

**Analogía:** es como decir "está lloviendo", "hay agua cayendo del cielo" y "mejor agarrá un paraguas". Las tres frases describen el mismo fenómeno. Si una es verdad, las tres son verdad. Si una es falsa, las tres son falsas.

**Consecuencia práctica:** si podés verificar **una** de las tres (la más fácil), ya sabés las otras dos **sin hacer más cuentas**.

### Paso 4: Pensalo al revés (el caso negativo)

La equivalencia también funciona en sentido contrario. Si una falla, las tres fallan. En ese caso:

| Si pasa esto… | Entonces pasa esto… | Y también esto… |
|---------------|---------------------|-----------------|
| $\det(A) = 0$ | $A$ no es invertible | $A x = B$ no es SCD (es SCI o SI) |

**Nota importante sobre el caso $\det(A) = 0$:** la triple equivalencia te dice que el sistema **no** es SCD. Pero no te dice **cuál de los otros dos es** (SCI o SI). Eso depende del vector $B$ específico:

- Para algunos $B$ el sistema puede ser SCI.
- Para otros $B$ puede ser SI.

Solo escalerizando descubrís cuál.

### Paso 5: El poder de la equivalencia — ejemplo de parcial

> "Me acuerdo que en un parcial había un sistema $A x = B$ que me quedaba SCD. El ejercicio era resolverlo. Luego, con la misma matriz $A$, les cambiaba el vector $B$ y les preguntaba que no lo resolviera el nuevo sistema pero que sí lo clasificara"

**Cómo resolverías eso usando la triple equivalencia:**

1. En la parte 1 resolviste el sistema original y te dio SCD.
2. Por la triple equivalencia (SCD → $A$ invertible → $\det(A) \neq 0$), **$A$ es invertible** y su determinante **no** es cero.
3. En la parte 2 te cambian $B$ pero **no cambian $A$**.
4. Como $A$ sigue siendo la misma, $A$ sigue siendo invertible, sigue teniendo $\det \neq 0$.
5. Por la triple equivalencia **en sentido contrario**, el sistema $A x = B'$ (con el nuevo $B'$) **también es SCD**.
6. **Terminaste — sin hacer cuentas.**

**Esto es muy valioso en el parcial:** el profesor puede pedirte que clasifiques un sistema con una matriz $A$ que ya sabés que es invertible, y **no hace falta escalerizar** — directo es SCD.

### Paso 6: Sección opcional — la fórmula que conecta $\det(A)$ con $\det(E)$

Esto es información adicional del teórico; **no es crítico para el parcial de esta unidad**, pero te deja entender "por qué" la triple equivalencia es cierta. Si no te interesa, saltala.

Al escalerizar la matriz $A$ llegás a una matriz $E$ (la forma escalerizada). Existe una relación entre ambos determinantes:

$$\det(A) = (-1)^k \cdot \frac{1}{\alpha_1} \cdot \frac{1}{\alpha_2} \cdot \ldots \cdot \frac{1}{\alpha_p} \cdot \det(E)$$

Donde $k$ es la cantidad de intercambios de filas que hiciste, y los $\alpha_i$ son los números por los que multiplicaste filas. Esa fórmula sale de aplicar las propiedades 2 (factor común de una fila) y 6 (intercambio de filas) del determinante.

**Lo importante de esa fórmula** es que el coeficiente $(-1)^k \cdot \prod (1/\alpha_i)$ **nunca** es cero. Entonces:

$$\det(A) \neq 0 \iff \det(E) \neq 0$$

Y como la única forma escalerizada con $\det(E) \neq 0$ es la **escalera perfecta** (o sea, SCD), cerramos la equivalencia:

$$\det(A) \neq 0 \iff \text{sistema SCD}$$

---

## Despeje matricial: resolver $A x = B$ usando la inversa

### Paso 1: El problema

Tenemos el sistema en forma matricial:

$$A \cdot x = B$$

donde $A$ y $B$ son conocidos (datos del problema), y $x$ (el vector de incógnitas) es lo que queremos encontrar.

**Pregunta:** ¿podemos "despejar" $x$ directamente, como hacemos en una ecuación normal?

Con números normales es fácil. Si tengo $5 \cdot x = 30$, divido ambos lados por $5$ y me queda $x = 6$. Pero con matrices, **no existe la "división"**. ¿Cómo despejamos?

### Paso 2: La idea clave — multiplicar por la inversa

En matrices, el equivalente a "dividir" es **multiplicar por la inversa**. Si $A$ tiene inversa ($A^{-1}$), entonces multiplicar por $A^{-1}$ "cancela" a $A$, igual que dividir por 5 cancelaría al 5.

Más formalmente: $A^{-1} \cdot A = I$ (la matriz identidad), y la identidad en matrices juega el mismo rol que el $1$ en números.

### Paso 3: El despeje paso a paso

Partimos de:

$$A \cdot x = B$$

**Paso A — Multiplicamos ambos lados por $A^{-1}$ a izquierda.**

$$A^{-1} \cdot A \cdot x = A^{-1} \cdot B$$

Fijate **dos cosas críticas**:

1. Multiplicamos **ambos lados** (lo que hagas en un lado, lo hacés en el otro — igual que en ecuaciones normales).
2. Multiplicamos **a izquierda**, o sea, el $A^{-1}$ va **antes** del resto en ambos lados.

> "Lo que tengo que hacer es multiplicar por la inversa a izquierda, no puedo mover el $A^{-1}$. Acuérdate que no conmuta, no podes cambiar el orden"

**¿Por qué "a izquierda" y no a derecha?** Porque el producto de matrices **no conmuta**: $A \cdot B$ y $B \cdot A$ pueden dar resultados distintos. Si multiplicás a la izquierda de un lado y a la derecha del otro, rompés la igualdad.

**Paso B — Agrupamos el lado izquierdo.**

Por la propiedad asociativa del producto de matrices ($A^{-1} \cdot A \cdot x = (A^{-1} \cdot A) \cdot x$):

$$(A^{-1} \cdot A) \cdot x = A^{-1} \cdot B$$

**Paso C — Simplificamos $A^{-1} \cdot A$.**

Por definición de inversa: $A^{-1} \cdot A = I$.

$$I \cdot x = A^{-1} \cdot B$$

**Paso D — Simplificamos $I \cdot x$.**

La matriz identidad $I$ multiplicada por cualquier cosa la deja igual (como el $1$ en números): $I \cdot x = x$.

$$x = A^{-1} \cdot B \quad \blacksquare$$

### Paso 4: La fórmula final

$$\boxed{x = A^{-1} \cdot B}$$

**Cómo se usa en la práctica:**

1. Calculás $A^{-1}$ (por cualquier método: cofactores, Gauss, directo).
2. Multiplicás $A^{-1}$ por $B$.
3. El vector que sale es directamente la solución $x$.

### Paso 5: La condición crítica — $A$ TIENE que ser invertible

**Si $\det(A) = 0$, este método no sirve.** Literalmente, $A^{-1}$ no existe, entonces no podés multiplicar por ella.

Por la triple equivalencia: si $\det(A) = 0$, el sistema NO es SCD → es SCI o SI → hay que resolverlo por escalerización.

**Regla de oro antes de usar el despeje matricial:**

1. ¿$\det(A) \neq 0$? → Sí, podés usar $x = A^{-1} B$.
2. ¿$\det(A) = 0$? → No, andá a escalerización directamente.

### Paso 6: Comparación con escalerización

¿Por qué aprender el despeje matricial si igual podés escalerizar siempre?

| Método | Cuándo conviene | Desventajas |
|--------|-----------------|-------------|
| Escalerización | Siempre funciona | Hay que hacer muchas operaciones |
| $x = A^{-1} B$ | Cuando ya tenés $A^{-1}$ calculada o te la dan | Solo funciona si $A$ invertible |

El despeje matricial es útil en dos casos:
1. Te dan $A^{-1}$ ya calculada y solo te piden la solución (es más rápido que escalerizar).
2. Te piden justificar que el sistema es SCD **y** dar la solución; con el despeje matricial, ambas cosas salen en un paso.

---

## Ejercicio integrador — parcial 2017

### Enunciado

$$S : \begin{cases} 2x + y - z = 2 \\ 2x + z = 3 \\ x - y = 0 \end{cases}$$

Se pide:
1. Calcular $\det(A)$ y concluir que $A$ es invertible.
2. Expresar $x$ en función de $A^{-1}$ y $B$, justificando que es SCD.
3. Resolver $S$ por escalerización.
4. Verificar que $A^{-1}$ toma la expresión dada (con un multiplicador $\tfrac{1}{5}$ y una matriz particular) y comprobar la expresión de la parte 2 comparándola con la solución de la parte 3.

> "Este ejercicio es bien de parcial. En un mismo ejercicio te meto a todos los temas. Matrices, determinantes y ecuaciones"

### Forma matricial

$$A = \begin{pmatrix} 2 & 1 & -1 \\ 2 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 2 \\ 3 \\ 0 \end{pmatrix}$$

### Parte 1 — $\det(A)$

Por Sarrus:

- Diagonales positivas: $2 \cdot 0 \cdot 0 + 1 \cdot 1 \cdot 1 + (-1) \cdot 2 \cdot (-1) = 0 + 1 + 2 = 3$
- Diagonales negativas: $(-1) \cdot 0 \cdot 1 + 2 \cdot 1 \cdot (-1) + 0 \cdot 2 \cdot 1 = 0 - 2 + 0 = -2$

$$\det(A) = 3 - (-2) = 5 \neq 0$$

Como $\det(A) \neq 0$, $A$ es invertible ✓.

### Parte 2 — Despeje matricial

Por la triple equivalencia: $\det(A) \neq 0$ ⟹ $A$ invertible ⟹ $Ax = B$ es SCD, y su solución es $x = A^{-1} B$.

### Parte 3 — Resolver por escalerización

Matriz ampliada:

$$\left(\begin{array}{ccc|c} 2 & 1 & -1 & 2 \\ 2 & 0 & 1 & 3 \\ 1 & -1 & 0 & 0 \end{array}\right)$$

$F_2 \leftarrow F_2 - F_1$:

$$\left(\begin{array}{ccc|c} 2 & 1 & -1 & 2 \\ 0 & -1 & 2 & 1 \\ 1 & -1 & 0 & 0 \end{array}\right)$$

$F_3 \leftarrow -2 F_3 + F_2$:

$$\left(\begin{array}{ccc|c} 2 & 1 & -1 & 2 \\ 0 & -1 & 2 & 1 \\ 0 & 1 & 2 & 1 \end{array}\right)$$

(Nota: la transcripción indica cuentas exactas un poco caóticas; el ejercicio termina con $z = 1$, $y = 1$, $x = 1$.)

$F_3 \leftarrow F_3 + F_2$:

$$\left(\begin{array}{ccc|c} 2 & 1 & -1 & 2 \\ 0 & -1 & 2 & 1 \\ 0 & 0 & 4 & 2 \end{array}\right)$$

**Clasificar:** escalera perfecta, 3 ecuaciones efectivas, 3 incógnitas → SCD (consistente con la triple equivalencia).

**Resolver:**

- De la fila 3: $5z = 5 \Rightarrow z = 1$
- De la fila 2: $-y + 2z = 1 \Rightarrow -y + 2 = 1 \Rightarrow y = 1$
- De la fila 1: $2x + y - z = 2 \Rightarrow 2x + 1 - 1 = 2 \Rightarrow x = 1$

**Solución:** $x = 1, \; y = 1, \; z = 1$.

### Parte 4 — Verificar $A^{-1}$ y comparar

La inversa dada es:

$$A^{-1} = \frac{1}{5} \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & -4 \\ -2 & 3 & -2 \end{pmatrix}$$

**Verificar multiplicando $A^{-1} \cdot A$** (debe dar $I$):

$$\frac{1}{5} \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & -4 \\ -2 & 3 & -2 \end{pmatrix} \cdot \begin{pmatrix} 2 & 1 & -1 \\ 2 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix} = \frac{1}{5} \begin{pmatrix} 5 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 5 \end{pmatrix} = I \checkmark$$

**Calcular $x = A^{-1} B$:**

$$x = \frac{1}{5} \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & -4 \\ -2 & 3 & -2 \end{pmatrix} \begin{pmatrix} 2 \\ 3 \\ 0 \end{pmatrix} = \frac{1}{5} \begin{pmatrix} 5 \\ 5 \\ 5 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$$

Coincide con la parte 3 ✓. La triple equivalencia funciona: el despeje matricial da lo mismo que la escalerización.

---

## Ejercicio de sistema homogéneo con parámetro $m$

### Enunciado

$A \cdot x = \vec{0}$ (sistema homogéneo) con

$$A = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 1 & 3 & 4 & 5 \\ 1 & 2 & 4 & 5 \\ 1 & 2 & m & m^2 - 5 \end{pmatrix}$$

Parte 1: discutir según $m$ y resolver cuando sea SCI.

Parte 2 (después): se da una matriz particular concreta y se pide deducir su determinante a partir de la discusión de la parte 1.

### Parte 1 — Escalerizar

Operaciones: $F_2 \leftarrow F_2 - F_1$, $F_3 \leftarrow F_3 - F_1$, $F_4 \leftarrow F_4 - F_1$:

$$\left(\begin{array}{cccc|c} 1 & 2 & 3 & 4 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & m-3 & m^2-9 & 0 \end{array}\right)$$

$F_4 \leftarrow F_4 - (m-3) F_3$:

$$\left(\begin{array}{cccc|c} 1 & 2 & 3 & 4 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & m^2 - m - 6 & 0 \end{array}\right)$$

(Cálculo del último elemento: $(m^2 - 9) - (m-3) \cdot 1 = m^2 - m - 6$.)

### Discusión

**Factorizar $m^2 - m - 6$:**

$m^2 - m - 6 = (m - 3)(m + 2)$

Las raíces son $m = 3$ y $m = -2$.

**Caso $m \neq 3$ y $m \neq -2$:**

$m^2 - m - 6 \neq 0$. De la fila 4: $(m^2 - m - 6) \cdot t = 0 \Rightarrow t = 0$. Subiendo: $z = 0$, $y = 0$, $x = 0$.

**SCD con solución trivial** (lo esperado en un homogéneo si la matriz es invertible).

**Caso $m = 3$ o $m = -2$:**

La fila 4 se anula. Queda la matriz:

$$\left(\begin{array}{cccc|c} 1 & 2 & 3 & 4 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right)$$

3 ecuaciones efectivas, 4 incógnitas → **SCI con 1 grado de libertad**.

**Resolver:** tomamos $z = \alpha$. De la fila 3: $z + t = 0 \Rightarrow t = -\alpha$. De la fila 2: $y + z + t = 0 \Rightarrow y + \alpha - \alpha = 0 \Rightarrow y = 0$. De la fila 1: $x + 2y + 3z + 4t = 0 \Rightarrow x + 3\alpha - 4\alpha = 0 \Rightarrow x = \alpha$.

**Solución:** $x = \alpha, \; y = 0, \; z = \alpha, \; t = -\alpha$.

### Cuadro resumen

| Valor de $m$ | Clasificación | Solución |
|--------------|---------------|----------|
| $m \neq 3$ y $m \neq -2$ | SCD | Trivial: $x = y = z = t = 0$ |
| $m = 3$ o $m = -2$ | SCI (1 grado de libertad) | $x = \alpha, \; y = 0, \; z = \alpha, \; t = -\alpha$ |

(Notar: el sistema homogéneo nunca es incompatible, consistente con lo que vimos en la clase 8.)

### Parte 2 — Determinante sin calcular cuentas

Se da una matriz $A_0$ concreta (la matriz $A$ sustituida con $m = -2$). ¿Cuánto vale $\det(A_0)$?

**Razonamiento (triple equivalencia):**

- Con $m = -2$, el sistema es SCI.
- Si el sistema es SCI, por la triple equivalencia, la matriz **no** es invertible.
- Si la matriz no es invertible, su determinante es $0$.

**Conclusión:** $\det(A_0) = 0$.

> "Justamente estamos aplicando la triple equivalencia. Sistema compatible indeterminado, por lo tanto, la matriz no es invertible, por lo tanto el determinante es $0$"

**Traducción:** cuando te piden el determinante de una matriz y ya resolviste antes un sistema con esa matriz, **podés deducir el determinante sin calcularlo**. Si el sistema dio SCI o SI, el determinante es $0$. Si dio SCD, el determinante es $\neq 0$.

---

## Cuadro general: la triple equivalencia en acción

| Si... | Entonces... | Y también... |
|-------|-------------|--------------|
| $\det(A) \neq 0$ | $A$ es invertible | $Ax = B$ es SCD (para todo $B$) |
| $\det(A) = 0$ | $A$ no es invertible | $Ax = B$ es SCI o SI (depende del $B$) |

**Consecuencia práctica:** cualquiera de los tres cálculos (determinante, inversa, escalerización) te da información sobre los otros dos.

---

# PARTE 3 — Preparación para la evaluación continua (22 de abril)

Evaluación sobre **sistemas de ecuaciones**. Nivel básico, en grupo, con material. Mismo formato que las dos anteriores (matrices y determinantes). Duración: media hora.

> "Mañana tenemos la prueba de sistema de ecuaciones. El mismo formato de siempre. Lo que hemos visto del sistema de ecuaciones: vas a resolver un sistema de ecuaciones por escalerización. No va a haber ninguna sorpresa"

---

## Lo que SÍ necesitás manejar

- **Escribir la matriz ampliada** de un sistema.
- **Escalerizar** aplicando las tres operaciones (intercambiar filas, multiplicar por $k \neq 0$, sumar filas).
- **Identificar** las tres formas escalonadas y **clasificar** el sistema (SCD, SCI, SI).
- **Calcular los grados de libertad** en un SCI: $r = n - p$ (incógnitas menos ecuaciones efectivas).
- **Resolver** un SCD despejando hacia arriba desde la última fila.
- **Resolver un SCI** introduciendo parámetros ($\alpha$, $\beta$, …) para los grados de libertad.
- **Reconocer un sistema homogéneo** y saber que **nunca es incompatible**.
- **Interpretar geométricamente** un sistema 2×2 (rectas que se cortan / paralelas / coincidentes).

## Lo que probablemente NO entra en esta evaluación

- Sistemas con parámetro (vienen en el parcial, según el profesor).
- Inversa por escalerización (concepto visto al final de la clase 9).
- Demostración de la triple equivalencia.
- La fórmula $\det(A) = (-1)^k \cdot \prod (1/\alpha_i) \cdot \det(E)$.

Estos temas ya vistos **sí entran en el parcial** del 5 de mayo.

## Prerrequisitos de matrices y determinantes que vas a usar

| Concepto previo | ¿Por qué lo necesitás? |
|-----------------|----------------------|
| Producto matriz × vector | Para entender la forma $A \cdot x = B$ |
| Matriz identidad $I$ | Aparece en la inversa y en el despeje matricial |
| Determinante $\neq 0$ ⟺ invertible | Triple equivalencia |
| Operaciones elementales sobre filas | Son las mismas que en escalerización |

---

## 5 errores que pueden aparecer en la evaluación

### Error 1: Olvidar la condición $k \neq 0$ al multiplicar una fila

> Cuando multiplicás una ecuación por un número, ese número tiene que ser **distinto de cero**. Si multiplicás por $0$, estás reemplazando la ecuación por "$0 = 0$", lo que pierde información y rompe la equivalencia.

### Error 2: Olvidar aplicar la operación al término independiente

Cuando multiplicás una fila por un número o le sumás otra fila, tenés que hacerlo también con el **término independiente** (lo que está a la derecha de la barra). La matriz ampliada se trata como una sola fila larga.

### Error 3: Decir que un sistema homogéneo es incompatible

> "Más allá de que le hayan errado alguna cuenta, conceptualmente nunca les puede pasar"

Un sistema homogéneo **siempre** tiene al menos la solución trivial, entonces **nunca puede ser incompatible**. Si al resolver te da incompatible, revisá las cuentas.

### Error 4: Confundir SCI con SI

- SCI: fila de ceros completa ("$0 = 0$"). El sistema tiene infinitas soluciones.
- SI: fila con todos los coeficientes en cero pero el término independiente **no** es cero ("$0 = 1$"). El sistema no tiene solución.

Mirá bien el término independiente de la fila problemática antes de clasificar.

### Error 5: Calcular mal los grados de libertad

$r = n - p$, donde:
- $n$ = **incógnitas**
- $p$ = **ecuaciones efectivas** (las que quedaron después de escalerizar, sin contar las que se anularon a "$0 = 0$")

Es tentador contar todas las filas originales, pero las que se anulan **no cuentan**. Si escalerizaste un sistema 4×3 y dos filas se anularon, quedan $p = 2$ ecuaciones efectivas.

---

## Checklist antes de entregar

1. ¿Escribí la matriz ampliada correctamente (con la barra separando coeficientes y términos independientes)?
2. ¿Apliqué solo las tres operaciones permitidas (intercambio, multiplicación por $\neq 0$, suma de filas)?
3. ¿Revisé cada operación en las dos partes (coeficientes y término independiente)?
4. ¿Clasifiqué el sistema (SCD, SCI, o SI) explícitamente?
5. Si es SCI, ¿calculé bien los grados de libertad e introduje los parámetros apropiados?
6. Si es SCD, ¿despejé todas las incógnitas desde la última fila?
7. Si es un sistema homogéneo, ¿verifiqué que **no** me dio incompatible?

---

## Referencia rápida

| Concepto | Fórmula/Regla |
|----------|---------------|
| Forma matricial | $A \cdot x = B$ |
| Sistema homogéneo | $A \cdot x = \vec{0}$ — siempre compatible |
| Solución trivial | $x_1 = x_2 = \ldots = x_n = 0$ |
| Grados de libertad | $r = n - p$ |
| Despeje si $A$ invertible | $x = A^{-1} \cdot B$ |
| Triple equivalencia | $\det(A) \neq 0 \Leftrightarrow A$ invertible $\Leftrightarrow Ax = B$ es SCD |

### Las tres formas escalonadas

| Forma | Ejemplo (última fila) | Clasificación |
|-------|----------------------|---------------|
| Fila de ceros con $\neq 0$ a la derecha | $(0, 0, 0 \mid 1)$ | SI |
| Escalera perfecta | $(0, 0, a \mid b)$ con $a \neq 0$ | SCD |
| Fila entera de ceros | $(0, 0, 0 \mid 0)$ | SCI |

---

## Preguntas de práctica

### Pregunta 1 (clasificación rápida)

Un sistema homogéneo $A \cdot x = \vec{0}$ tiene $\det(A) = 0$. ¿Cuál es la clasificación?

> **Respuesta:** SCI. Un homogéneo nunca es incompatible. Si $\det(A) = 0$, no es invertible, entonces no puede ser SCD. Queda SCI.

---

### Pregunta 2 (escalerización 2×2 básica)

Resolver:

$$\begin{cases} 3x - y = 5 \\ x + 2y = 4 \end{cases}$$

> **Respuesta:**
>
> Matriz ampliada: $\begin{pmatrix} 3 & -1 & | & 5 \\ 1 & 2 & | & 4 \end{pmatrix}$. Aplicamos $F_2 \leftarrow 3F_2 - F_1$: $\begin{pmatrix} 3 & -1 & | & 5 \\ 0 & 7 & | & 7 \end{pmatrix}$. De la fila 2: $y = 1$. De la fila 1: $3x - 1 = 5 \Rightarrow x = 2$. **SCD con solución $(2, 1)$**.

---

### Pregunta 3 (sistema incompatible)

Clasificar (sin resolver):

$$\begin{cases} x + y = 3 \\ 2x + 2y = 7 \end{cases}$$

> **Respuesta:** $F_2 \leftarrow F_2 - 2F_1 \Rightarrow$ fila 2 queda $(0, 0, 1)$, o sea "$0 = 1$". **SI (incompatible)**. Geométricamente: las rectas $x + y = 3$ y $x + y = 3.5$ son paralelas.

---

### Pregunta 4 (grados de libertad)

Un sistema 4×5 (4 ecuaciones, 5 incógnitas) da, después de escalerizar, 2 filas que se anularon. ¿Cuántos grados de libertad tiene?

> **Respuesta:** Ecuaciones efectivas $p = 4 - 2 = 2$. Incógnitas $n = 5$. $r = n - p = 3$ grados de libertad. El sistema es SCI, y la solución se expresa con tres parámetros $\alpha, \beta, \gamma$.

---

### Pregunta 5 (sistema homogéneo)

Sea $A$ una matriz cuadrada con $\det(A) = 7$. Clasificar el sistema $A \cdot x = \vec{0}$.

> **Respuesta:** $\det(A) \neq 0 \Rightarrow A$ invertible $\Rightarrow Ax = B$ es SCD para todo $B$, en particular para $B = \vec{0}$. La única solución del sistema homogéneo es la trivial: $x = \vec{0}$. **SCD con solución trivial**.

---

### Pregunta 6 (interpretación geométrica)

Las rectas $2x + y = 4$ y $4x + 2y = 7$ representan un sistema. ¿Cómo se ven geométricamente y qué clasificación tiene?

> **Respuesta:** La segunda es "casi" el doble de la primera, pero no exactamente ($4x + 2y = 8$ sería exactamente el doble). Las dos rectas tienen la misma pendiente pero distinto término — son **paralelas no coincidentes** → **SI**.

---

### Pregunta 7 (escalerización 3×3)

Clasificar y resolver:

$$\begin{cases} x + y + z = 3 \\ 2x + 2y + 2z = 6 \\ x - y = 0 \end{cases}$$

> **Respuesta:**
>
> Matriz ampliada: $\begin{pmatrix} 1 & 1 & 1 & | & 3 \\ 2 & 2 & 2 & | & 6 \\ 1 & -1 & 0 & | & 0 \end{pmatrix}$. $F_2 \leftarrow F_2 - 2F_1$ anula la fila 2 completamente (era el doble de la primera). $F_3 \leftarrow F_3 - F_1$: $(0, -2, -1 \mid -3)$. Queda:
>
> $\begin{pmatrix} 1 & 1 & 1 & | & 3 \\ 0 & 0 & 0 & | & 0 \\ 0 & -2 & -1 & | & -3 \end{pmatrix}$. Dos ecuaciones efectivas, 3 incógnitas → **SCI con 1 grado de libertad**.
>
> Tomamos $z = \alpha$. De la fila 3: $-2y - \alpha = -3 \Rightarrow y = \frac{3 - \alpha}{2}$. De la fila 1: $x + \frac{3-\alpha}{2} + \alpha = 3 \Rightarrow x = \frac{3 - \alpha}{2}$.
>
> Solución: $x = \frac{3 - \alpha}{2}, \; y = \frac{3 - \alpha}{2}, \; z = \alpha$.

---

### Pregunta 8 (despeje matricial)

$A$ es 3×3 invertible con $A^{-1} = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \\ 1 & 1 & 0 \end{pmatrix}$ y $B = \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix}$. Resolver $A \cdot x = B$.

> **Respuesta:** $x = A^{-1} B = \begin{pmatrix} 1 \cdot 2 + 0 \cdot 3 + 2 \cdot 1 \\ 0 \cdot 2 + 1 \cdot 3 + (-1) \cdot 1 \\ 1 \cdot 2 + 1 \cdot 3 + 0 \cdot 1 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \\ 5 \end{pmatrix}$.

---

### Pregunta 9 (triple equivalencia — sin cuentas)

Se resolvió $A \cdot x = B_1$ y dio **compatible determinado**. Ahora cambian el término independiente a $B_2$ sin modificar $A$. ¿Qué clasificación tiene $A \cdot x = B_2$?

> **Respuesta:** Como $A \cdot x = B_1$ es SCD, $\det(A) \neq 0$, entonces $A$ es invertible. Por la triple equivalencia, $A \cdot x = B$ es SCD **para todo $B$** — incluido $B_2$. Entonces **$A \cdot x = B_2$ es SCD** sin hacer cuentas.

---

### Pregunta 10 (SCI con dos grados de libertad)

Un sistema homogéneo $4 \times 4$, después de escalerizar, tiene dos filas anuladas. ¿Cuántos grados de libertad? ¿Cómo se escribe la solución?

> **Respuesta:** $p = 4 - 2 = 2$ ecuaciones efectivas, $n = 4$ incógnitas, $r = 2$ grados de libertad. La solución tiene dos parámetros, típicamente $\alpha$ y $\beta$. Dos de las incógnitas se despejan en función de las otras dos.

---

### Pregunta 11 (detección por inspección)

Sin hacer cuentas, ¿qué podés decir del determinante de la matriz de este sistema?

$$\begin{cases} x + 2y + 3z = 5 \\ 2x + 4y + 6z = 10 \\ x - y + z = 2 \end{cases}$$

> **Respuesta:** La fila 2 es exactamente el doble de la fila 1 (tanto en coeficientes como en término independiente). Al escalerizar se va a anular. Queda un sistema con 2 ecuaciones efectivas y 3 incógnitas → **SCI**. Por la triple equivalencia, la matriz de coeficientes **no es invertible** y su **determinante es $0$**. Todo esto sin hacer ninguna cuenta.

---

### Pregunta 12 (sistema con parámetro — estilo parcial)

Dado el sistema

$$\begin{cases} x + y = 2 \\ 2x + \lambda y = 4 \end{cases}$$

discutir y resolver en función de $\lambda$.

> **Respuesta:**
>
> Matriz ampliada: $\begin{pmatrix} 1 & 1 & | & 2 \\ 2 & \lambda & | & 4 \end{pmatrix}$. $F_2 \leftarrow F_2 - 2F_1$: $\begin{pmatrix} 1 & 1 & | & 2 \\ 0 & \lambda - 2 & | & 0 \end{pmatrix}$.
>
> **Caso $\lambda \neq 2$:** $\lambda - 2 \neq 0$. Fila 2: $(\lambda - 2) y = 0 \Rightarrow y = 0$. Fila 1: $x = 2$. SCD con solución $(2, 0)$.
>
> **Caso $\lambda = 2$:** fila 2 se anula. 1 ecuación efectiva, 2 incógnitas, $r = 1$. Tomamos $y = \alpha$. De la fila 1: $x = 2 - \alpha$. SCI con solución $(2 - \alpha, \alpha)$.
>
> Cuadro:
>
> | Valor de $\lambda$ | Clasificación | Solución |
> |--------------------|---------------|----------|
> | $\lambda \neq 2$ | SCD | $x = 2, \; y = 0$ |
> | $\lambda = 2$ | SCI (1 gr. libertad) | $x = 2 - \alpha, \; y = \alpha$ |
>
> (Nunca da incompatible en este ejemplo, pero podría dar SI si el término independiente no encajara con el patrón de paralelismo.)

---

## Cierre

Con esta parte cerramos los sistemas de ecuaciones. La **triple equivalencia** es el concepto más importante de la unidad — conecta todo lo visto en el curso: matrices, determinantes, invertibilidad, sistemas. Entender que **saber una cosa es saber las tres** es clave para el parcial, porque permite resolver ejercicios sin calcular lo que ya está implícito.

> "Este no es un teórico complejo a diferencia de otros temas más pesados con temas de demostraciones, pero hay que agarrar la mano con las cuentas, saber escalerizar las matrices, que no es poca cosa"

El próximo tema del curso es **geometría del espacio** (cuarto y último tema antes del parcial del 5 de mayo), que también se va a relacionar con todo lo anterior.
