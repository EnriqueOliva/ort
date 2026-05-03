# Matrices — Banco de Demostraciones

Este archivo contiene **todas las demostraciones formales** del módulo de matrices, organizadas por tema. Es el complemento de `matrices-para-PARCIAL.md` (la teoría/explicación). Cuando una propiedad aparezca con la marca **🟢 SE PIDE — demo en demos.md §X.Y**, esa demo está acá.

Las demos están escritas siguiendo el **esquema oficial pedido por el profesor**:

1. **Hipótesis** explícita (qué te dan)
2. **Tesis** explícita (qué probar)
3. **Pasos** justificados con la propiedad/definición que se aplica en cada uno
4. **Cierre con $\blacksquare$**

Recordá: el profesor dijo *"en los parciales se pide justificar las propiedades que aplican"* — toda demo en parcial necesita justificar cada paso.

---

## Índice

| § | Demostración |
|---|---|
| **A** | **Producto y vectores canónicos** |
| A.1 | Producto por vector canónico extrae columna $j$ |
| **B** | **Traspuesta** |
| B.1 | Prop 1: $(A^T)^T = A$ |
| B.2 | Prop 2: $(A+B)^T = A^T + B^T$ |
| B.3 | Prop 3: $(\alpha A)^T = \alpha A^T$ |
| B.4 | Prop 4: $(AB)^T = B^T A^T$ (orden invertido) |
| **C** | **Simétrica y antisimétrica** |
| C.1 | Suma de simétricas es simétrica |
| C.2 | $\alpha A$ simétrica si $A$ simétrica (+ análogas para antisimétrica) |
| C.3 | $AB$ simétrica $\iff AB = BA$ (con $A, B$ simétricas) |
| C.4 | $\frac{1}{2}(A + A^T)$ es simétrica |
| C.5 | $\frac{1}{2}(A - A^T)$ es antisimétrica |
| C.6 | Toda matriz cuadrada $A = $ simétrica $+$ antisimétrica |
| **D** | **Traza** |
| D.1 | Prop 1: $tr(A+B) = tr(A) + tr(B)$ |
| D.2 | Prop 2: $tr(\alpha A) = \alpha \cdot tr(A)$ |
| D.3 | Prop 3: $tr(A^T) = tr(A)$ |
| D.4 | Prop 4: $tr(AB) = tr(BA)$ |
| D.5 | Corolario: $tr(A - B) = tr(A) - tr(B)$ |
| D.6 | **Aplicación clásica:** NO existen $A, B$ con $AB - BA = \text{Id}$ |
| **E** | **Inversa** |
| E.1 | Prop 1: $(A^{-1})^{-1} = A$ |
| E.2 | Prop 2: $(AB)^{-1} = B^{-1} A^{-1}$ (orden invertido) |
| E.3 | Prop 3: $(\alpha A)^{-1} = \frac{1}{\alpha} A^{-1}$ |
| E.4 | Prop 4: $(A^T)^{-1} = (A^{-1})^T$ |
| **F** | **Idempotente y nilpotente** |
| F.1 | Idempotente $+$ invertible $\Rightarrow A = \text{Id}$ (V.I.2) |
| F.2 | Si $A$ idempotente, $(A + \text{Id})^3 = \text{Id} + 7A$ |
| F.3 | $P^{-1} A P$ nilpotente del mismo grado que $A$ (V.7.2) |
| **G** | **Inducción** |
| G.1 | $A^n$ con $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ (VI.1) |
| G.2 | $A^n$ con $A^2 = 2A - \text{Id}$ (V.10.3) |
| G.3 | $A^n$ con $A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$ (V.4) |
| G.4 | $A^k$ para matriz diagonal |
| **H** | **Factorización para hallar inversa** |
| H.1 | $A^3 - A = \text{Id} \Rightarrow A^{-1} = A^2 - \text{Id}$ |
| H.2 | $A^3 = \mathcal{O} \Rightarrow (A + \text{Id})^{-1} = A^2 - A + \text{Id}$ (VI.3) |
| **I** | **Otros del práctico** |
| I.1 | V.11: ley de simplificación a izquierda |
| I.2 | V.14: $A, B$ invertibles $\Rightarrow AB$ invertible (con su inversa explícita) |
| I.3 | V.15: si $AB = BA$ y $AC = CA$, entonces $A$ conmuta con $\mu B + \lambda C$ |

---

## A. Producto y vectores canónicos

### A.1 — Producto por vector canónico extrae columna $j$

> **Cómo leer esta demo (en una frase):** vamos a escribir el producto $A \cdot \vec{v}_j$ usando la fórmula con sumatoria. Como $\vec{v}_j$ es casi todo ceros, casi todos los términos de la suma se cancelan y queda solo uno — justamente el de la columna $j$ de $A$.

**Hipótesis:**
- $A \in \mathcal{M}_{n \times n}$ — una matriz cuadrada $n \times n$ cualquiera.
- $\vec{v}_j$ es el "vector canónico $j$" — una columna con un $1$ en la posición $j$ y $0$ en todas las demás posiciones.

> **Traducción:** si $j = 2$ y $n = 3$, $\vec{v}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$. El subíndice te dice **dónde está el $1$**.

**Tesis:** $A \cdot \vec{v}_j$ = la columna $j$ de $A$.

**Demostración paso a paso:**

**Paso 1 — Notación.** Llamemos $a_{ik}$ a la entrada de $A$ en la fila $i$, columna $k$. Y a las componentes de $\vec{v}_j$ las llamamos $v_k$:

$$v_k = \begin{cases} 1 & \text{si } k = j \\ 0 & \text{si } k \neq j \end{cases}$$

> **¿Qué dice esto?** Solamente hay un $1$ en $\vec{v}_j$, y está en la posición $j$. El resto son ceros.

**Paso 2 — Aplicar la fórmula del producto.** Para encontrar la entrada $i$ del resultado (la fila $i$ de la columna que sale), usás la regla "fila por columna":

$$(A \cdot \vec{v}_j)_i = \sum_{k=1}^{n} a_{ik} \cdot v_k$$

> **¿Qué significa esa $\sum$?** Es una suma con $n$ términos: $a_{i1} v_1 + a_{i2} v_2 + a_{i3} v_3 + \cdots + a_{in} v_n$. La $\sum_{k=1}^{n}$ te dice "sumá desde $k=1$ hasta $k=n$".

**Paso 3 — Aprovechar que casi todos los $v_k$ son cero.** En esa suma, casi todos los términos se anulan. Solo sobrevive el término donde $k = j$ (porque solo ahí $v_k = 1$):

$$\sum_{k=1}^{n} a_{ik} \cdot v_k = \underbrace{a_{ij} \cdot 1}_{\text{término } k=j} + \underbrace{\sum_{k \neq j} a_{ik} \cdot 0}_{\text{el resto}} = a_{ij}$$

> **¿Qué pasó?** El único término no cero es $a_{ij} \cdot 1 = a_{ij}$. Los otros $n-1$ términos son $a_{ik} \cdot 0 = 0$.

**Paso 4 — Concluir.** Como $(A \cdot \vec{v}_j)_i = a_{ij}$ para CUALQUIER fila $i$ (esto vale para todas), el vector resultante tiene como entradas $a_{1j}, a_{2j}, \ldots, a_{nj}$ — que es exactamente la **columna $j$ de $A$**. $\blacksquare$

> **Idea central:** los ceros del vector canónico **borran** todos los números de la fila menos uno, y el $1$ del vector deja pasar exactamente el de la columna $j$. Por eso el resultado es la columna $j$.
>
> Ejemplo numérico desarrollado: ver `matrices-para-PARCIAL.md` PARTE 3 — sección "Producto por vectores canónicos".

---

## B. Traspuesta

### B.1 — Propiedad 1: $(A^T)^T = A$

> **Cómo leer esta demo (en una frase):** trasponer cambia $a_{ij} \to a_{ji}$. Si trasponés DE NUEVO, cambiás $a_{ji} \to a_{ij}$. Volvés a la original.

**Hipótesis:** $A = ((a_{ij})) \in \mathcal{M}_{m \times n}$ — una matriz $m \times n$ cualquiera con entradas $a_{ij}$.

**Tesis:** $(A^T)^T = A$.

**Demostración paso a paso:**

**Paso 1 — Trasponer una vez.** Por definición, trasponer significa intercambiar fila por columna. Lo que estaba en posición $(i,j)$ ahora está en $(j,i)$:

$$A^T = ((a_{ji}))$$

> **¿Qué dice esa notación?** $((a_{ji}))$ es la matriz cuya entrada en posición $(i,j)$ es $a_{ji}$. O sea: si quiero saber qué hay en la fila 1 columna 2 de $A^T$, voy a buscar la entrada que estaba en fila 2 columna 1 de $A$.

**Paso 2 — Trasponer otra vez.** Aplicamos la traspuesta una segunda vez. Igual que antes, intercambiamos los subíndices: $a_{ji} \to a_{ij}$.

$$(A^T)^T = ((a_{ij}))$$

> **¿Qué cambió?** El subíndice volvió a ser $a_{ij}$ — exactamente igual al de $A$.

**Paso 3 — Concluir.** $((a_{ij})) = A$ por definición. Entonces:

$$(A^T)^T = A \quad \blacksquare$$

> **Idea central:** trasponer es una operación "involutiva" — hacerla dos veces te devuelve al inicio. Como dar vuelta una hoja de papel dos veces.

### B.2 — Propiedad 2: $(A + B)^T = A^T + B^T$

> **Cómo leer esta demo (en una frase):** sumar dos matrices y luego trasponer da lo mismo que trasponer cada una y después sumar. Vamos a probarlo manipulando las entradas.

**Hipótesis:** $A, B \in \mathcal{M}_{m \times n}$ (misma dimensión, requisito para poder sumarlas).

**Tesis:** $(A + B)^T = A^T + B^T$.

**Demostración paso a paso:**

**Paso 1 — Escribir $A$ y $B$ por sus entradas.** Llamamos $A = ((a_{ij}))$ y $B = ((b_{ij}))$:

$$[A + B]^T = [((a_{ij})) + ((b_{ij}))]^T$$

> **¿Por qué hago esto?** Para poder operar adentro del corchete necesito ver las entradas de cada matriz, no las matrices "en bloque". Es como si quisiera calcular $(3+5) \cdot 2$: primero sumo adentro del paréntesis, después multiplico.

**Paso 2 — Aplicar la definición de suma de matrices.** Sumar dos matrices significa sumar entrada por entrada en posiciones correspondientes. Entonces $A + B$ es la matriz cuya entrada $(i,j)$ es $a_{ij} + b_{ij}$:

$$= [((a_{ij} + b_{ij}))]^T$$

> **¿Qué cambió?** Antes tenía dos matrices separadas; ahora tengo UNA sola matriz cuyas entradas son la suma. Es solo otra forma de escribir lo mismo.

**Paso 3 — Aplicar la definición de traspuesta.** Trasponer intercambia $i$ y $j$ en cada subíndice. Tanto el de $a$ como el de $b$:

$$= ((a_{ji} + b_{ji}))$$

> **¿Qué cambió?** Saqué el corchete $[\;]^T$ porque ya apliqué la operación traspuesta — y eso se materializa como cambiar $a_{ij} \to a_{ji}$ y $b_{ij} \to b_{ji}$.

**Paso 4 — Separar la suma adentro de la matriz.** Una matriz cuya entrada es $a_{ji} + b_{ji}$ es lo mismo que la suma de una matriz cuya entrada es $a_{ji}$ más otra cuya entrada es $b_{ji}$:

$$= ((a_{ji})) + ((b_{ji}))$$

> **¿Por qué puedo separar?** Porque la definición de suma de matrices funciona en ambas direcciones: si tengo entradas que son sumas, puedo escribirlas como suma de matrices.

**Paso 5 — Reconocer las matrices traspuestas.** $((a_{ji}))$ es justamente $A^T$ (por la definición del paso 1). Lo mismo $((b_{ji})) = B^T$:

$$= A^T + B^T \quad \blacksquare$$

> **Idea central:** la traspuesta "se reparte" entre los sumandos — y la prueba se hace yendo a las entradas y volviendo.

### B.3 — Propiedad 3: $(\alpha \cdot A)^T = \alpha \cdot A^T$

> **Cómo leer esta demo (en una frase):** un número $\alpha$ multiplicado por una matriz se puede sacar fuera de la traspuesta sin tocarlo (los números no se trasponen).

**Hipótesis:** $A \in \mathcal{M}_{m \times n}$, $\alpha \in \mathbb{R}$ (un número real).

**Tesis:** $(\alpha A)^T = \alpha A^T$.

**Demostración paso a paso:**

**Paso 1 — Escribir $\alpha A$ por sus entradas.** Multiplicar una matriz por un escalar significa multiplicar cada entrada por ese escalar:

$$(\alpha A)^T = ((\alpha \cdot a_{ij}))^T$$

> **¿Qué dice?** La matriz $\alpha A$ es la que tiene $\alpha \cdot a_{ij}$ en cada posición $(i,j)$.

**Paso 2 — Aplicar la traspuesta.** Trasponer intercambia $i$ con $j$:

$$= ((\alpha \cdot a_{ji}))$$

> **¿Qué cambió?** El subíndice de $a$ pasó de $a_{ij}$ a $a_{ji}$. Notá que **el $\alpha$ no se traspone** — es solo un número, no tiene "filas y columnas" para intercambiar.

**Paso 3 — Sacar $\alpha$ como factor común.** Como $\alpha$ multiplica a cada entrada, podemos escribir esa matriz como $\alpha$ por la matriz $((a_{ji}))$:

$$= \alpha \cdot ((a_{ji}))$$

> **¿Por qué puedo?** Porque por definición, $\alpha M$ (escalar por matriz) es la matriz que tiene $\alpha$ multiplicando cada entrada. Acá lo aplico al revés: si toda entrada está multiplicada por $\alpha$, lo saco afuera.

**Paso 4 — Reconocer la traspuesta.** $((a_{ji})) = A^T$ por definición:

$$= \alpha \cdot A^T \quad \blacksquare$$

> **Idea central:** los escalares atraviesan la traspuesta sin tocarse. **Error común a evitar en parcial:** escribir $(\alpha A)^T = \alpha^T A^T$. **Los escalares no se trasponen** — un número real no tiene filas y columnas.

### B.4 — Propiedad 4: $(A \cdot B)^T = B^T \cdot A^T$ (orden invertido)

> **Cómo leer esta demo (en una frase):** vamos a calcular la entrada $(i,j)$ tanto de $(AB)^T$ como de $B^T A^T$ usando sumatorias, y mostrar que dan la misma fórmula. Si las entradas coinciden, las matrices coinciden.

**Hipótesis:** $A \in \mathcal{M}_{m \times n}$, $B \in \mathcal{M}_{n \times p}$ — conformables (las columnas de $A$ coinciden con las filas de $B$, así se puede hacer el producto).

**Tesis:** $(AB)^T = B^T A^T$.

**Demostración paso a paso:**

**Paso 1 — Nombrar el producto.** Para no andar arrastrando "$AB$" todo el tiempo, llamemos $C = AB$. Por la fórmula del producto matricial:

$$c_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj}$$

> **¿Qué dice esto?** La entrada $(i,j)$ de $C$ se obtiene multiplicando la fila $i$ de $A$ por la columna $j$ de $B$ (par a par y sumando). El índice $k$ recorre las posiciones dentro de la fila/columna.

**Paso 2 — Calcular la entrada $(i,j)$ de $C^T$.** Por definición de traspuesta, la entrada $(i,j)$ de $C^T$ es la entrada $(j,i)$ de $C$:

$$(C^T)_{ij} = c_{ji}$$

Ahora aplicamos la fórmula del paso 1 para $c_{ji}$ (intercambiando los roles de $i$ y $j$):

$$(C^T)_{ij} = c_{ji} = \sum_{k=1}^{n} a_{jk} \cdot b_{ki} \qquad (\star)$$

> **¿Qué cambió?** Donde antes decía $a_{ik}$ ahora dice $a_{jk}$, y donde decía $b_{kj}$ ahora dice $b_{ki}$. Es solo aplicar la misma fórmula con los índices intercambiados.

**Paso 3 — Calcular la entrada $(i,j)$ de $B^T A^T$.** Por la fórmula del producto:

$$(B^T A^T)_{ij} = \sum_{k=1}^{n} (B^T)_{ik} \cdot (A^T)_{kj}$$

Pero por definición de traspuesta, $(B^T)_{ik} = b_{ki}$ y $(A^T)_{kj} = a_{jk}$. Sustituyendo:

$$(B^T A^T)_{ij} = \sum_{k=1}^{n} b_{ki} \cdot a_{jk}$$

**Paso 4 — Conmutar los factores adentro de la suma.** Adentro de la sumatoria estoy sumando productos de **números reales** ($b_{ki}$ y $a_{jk}$ son números, no matrices). Y los números reales SÍ conmutan: $b_{ki} \cdot a_{jk} = a_{jk} \cdot b_{ki}$:

$$(B^T A^T)_{ij} = \sum_{k=1}^{n} a_{jk} \cdot b_{ki} \qquad (\star\star)$$

> **¿Por qué importa esta distinción?** Las MATRICES no conmutan, pero los NÚMEROS sí. Acá, dentro de la $\sum$, estoy multiplicando dos numeritos — eso siempre conmuta.

**Paso 5 — Comparar.** Mirá $(\star)$ y $(\star\star)$. Son **idénticas**:

$$(C^T)_{ij} = \sum_{k=1}^{n} a_{jk} \cdot b_{ki} = (B^T A^T)_{ij}$$

Como las entradas $(i,j)$ coinciden para CUALQUIER $i, j$, las matrices son iguales:

$$C^T = (AB)^T = B^T A^T \quad \blacksquare$$

> **Idea central:** dos matrices son iguales si tienen las mismas entradas en cada posición. La prueba consiste en calcular esa entrada por dos caminos distintos y mostrar que dan lo mismo.
>
> **Error común a evitar:** escribir $(AB)^T = A^T B^T$. **El orden se invierte.** Una forma de recordarlo: si $A$ es $2 \times 3$ y $B$ es $3 \times 4$, entonces $A^T$ es $3 \times 2$ y $B^T$ es $4 \times 3$. ¿Se puede hacer $A^T B^T$? No: las columnas de $A^T$ son 2 y las filas de $B^T$ son 4, no coinciden. ¿Se puede $B^T A^T$? Sí: $4 \times 3 \cdot 3 \times 2$ funciona.

---

## C. Simétrica y antisimétrica

### C.1 — Suma de simétricas es simétrica

> **Cómo leer esta demo (en una frase):** trasponemos la suma usando la propiedad 2, después usamos que $A$ y $B$ son simétricas para volver a tener $A + B$. Como $(A+B)^T = A+B$, la suma es simétrica.

**Hipótesis:** $A, B$ son simétricas, lo que significa $A^T = A$ y $B^T = B$.

> **Recordá:** "matriz simétrica" significa "es igual a su traspuesta". Es la definición.

**Tesis:** $A + B$ es simétrica — o sea, queremos llegar a $(A+B)^T = A + B$.

**Demostración paso a paso:**

**Paso 1 — Trasponer la suma.** Por la propiedad 2 de traspuesta (§B.2), trasponer una suma es lo mismo que sumar las traspuestas:

$$(A + B)^T = A^T + B^T$$

> **¿Por qué puedo hacer esto?** Esa es exactamente la propiedad 2 que demostramos antes. La estoy aplicando.

**Paso 2 — Usar la hipótesis (que son simétricas).** Por hipótesis $A^T = A$ y $B^T = B$, así que reemplazo:

$$= A + B$$

**Paso 3 — Concluir.** Logré $(A + B)^T = A + B$. Eso es la **definición** de matriz simétrica aplicada a $A+B$. Por lo tanto $A+B$ es simétrica. $\blacksquare$

> **Idea central:** trasponemos, usamos la simetría, llegamos al inicio. Solo dos pasos.
>
> **Análoga (ejercicio mental):** la suma de antisimétricas es antisimétrica. Misma demo pero con $A^T = -A$ y $B^T = -B$, terminás en $-(A+B)$.

### C.2 — $\alpha A$ es simétrica si $A$ es simétrica

> **Cómo leer esta demo (en una frase):** trasponemos $\alpha A$ usando la propiedad 3 (el escalar sale), luego usamos que $A$ es simétrica para volver a $\alpha A$.

**Hipótesis:** $A$ simétrica ($A^T = A$); $\alpha \in \mathbb{R}$ un número real cualquiera.

**Tesis:** $\alpha A$ es simétrica — o sea, $(\alpha A)^T = \alpha A$.

**Demostración paso a paso:**

**Paso 1 — Sacar $\alpha$ afuera de la traspuesta.** Por la propiedad 3 (§B.3), trasponer un escalar por matriz es lo mismo que dejar el escalar afuera:

$$(\alpha A)^T = \alpha \cdot A^T$$

**Paso 2 — Usar que $A$ es simétrica.** Reemplazamos $A^T$ por $A$ (eso dice la hipótesis):

$$= \alpha \cdot A$$

**Paso 3 — Concluir.** Logré $(\alpha A)^T = \alpha A$. Por definición, eso significa que $\alpha A$ es simétrica. $\blacksquare$

> **Análoga:** si $A$ es antisimétrica ($A^T = -A$), seguís el mismo camino y terminás en $\alpha (-A) = -(\alpha A)$, así que $\alpha A$ resulta antisimétrica.

### C.3 — $AB$ simétrica $\iff AB = BA$ (con $A, B$ simétricas)

> **Cómo leer esta demo (en una frase):** "$\iff$" significa "si y solo si" — hay que probar **dos cosas**: ida (si $AB$ es simétrica entonces $AB = BA$) y vuelta (si $AB = BA$ entonces $AB$ es simétrica). En ambas direcciones se usa la propiedad 4 de traspuesta.

**Hipótesis:** $A^T = A$ y $B^T = B$ ($A$ y $B$ son simétricas).

**Tesis:** $AB$ simétrica $\iff AB = BA$.

> **¿Qué quiere decir "iff"?** "Si y solo si" exige probar **dos direcciones**:
> - **Ida ($\Rightarrow$):** asumir el lado izquierdo, llegar al derecho.
> - **Vuelta ($\Leftarrow$):** asumir el lado derecho, llegar al izquierdo.
>
> Una sola dirección NO alcanza.

---

#### Dirección IDA ($\Rightarrow$): asumimos $AB$ simétrica, probamos $AB = BA$

**Paso 1 — Usar la hipótesis adicional ($AB$ simétrica).** "Simétrica" significa que es igual a su traspuesta:

$$AB = (AB)^T$$

> **¿De dónde sale esto?** Estoy usando la definición de simetría aplicada a $AB$.

**Paso 2 — Aplicar la propiedad 4 de traspuesta.** $(AB)^T = B^T A^T$:

$$= B^T A^T$$

> **Cuidado: el orden se invierte.** No es $A^T B^T$ — siempre cambia el orden.

**Paso 3 — Usar que $A$ y $B$ son simétricas.** Como $A^T = A$ y $B^T = B$, reemplazamos:

$$= B \cdot A$$

**Paso 4 — Cerrar la cadena.** Juntando los pasos anteriores: $AB = BA$. ✓

---

#### Dirección VUELTA ($\Leftarrow$): asumimos $AB = BA$, probamos $AB$ simétrica

**Paso 1 — Trasponer $AB$.** Por la propiedad 4:

$$(AB)^T = B^T A^T$$

**Paso 2 — Usar simetría de $A$ y $B$.** $A^T = A$ y $B^T = B$:

$$= B \cdot A$$

**Paso 3 — Usar la nueva hipótesis ($AB = BA$).** Por hipótesis los podemos intercambiar:

$$= A \cdot B$$

**Paso 4 — Concluir.** $(AB)^T = AB$, que es la definición de simétrica. ✓

---

**Conclusión.** Probadas las dos direcciones, queda probada la equivalencia. $\blacksquare$

> **Idea central:** la propiedad 4 ($(XY)^T = Y^T X^T$) hace casi todo el trabajo. Combinándola con la simetría de $A$ y $B$, ambas direcciones salen en 3-4 pasos.

### C.4 — $\frac{1}{2}(A + A^T)$ es simétrica

> **Cómo leer esta demo (en una frase):** llamamos $S$ a la matriz $\frac{1}{2}(A + A^T)$ y trasponemos. Usando las propiedades 1, 2 y 3 de traspuesta, llegamos a que $S^T = S$, lo que significa que $S$ es simétrica.

**Hipótesis:** $A$ es una matriz cuadrada **cualquiera** (no hace falta que sea simétrica).

**Tesis:** $S = \frac{1}{2}(A + A^T)$ es simétrica — o sea, $S^T = S$.

> **¿Por qué importa este resultado?** Porque junto con C.5 y C.6, te permite **descomponer cualquier matriz cuadrada en una parte simétrica más una antisimétrica**.

**Demostración paso a paso:**

**Paso 1 — Calcular $S^T$ aplicando la traspuesta a la expresión.**

$$S^T = \left[\tfrac{1}{2}(A + A^T)\right]^T$$

> **Estrategia:** voy a transformar $S^T$ paso a paso hasta volver a obtener $S$ — eso prueba que $S^T = S$.

**Paso 2 — Sacar el $\frac{1}{2}$ afuera (propiedad 3 de traspuesta).** Como $\frac{1}{2}$ es un escalar, sale sin trasponerse:

$$= \tfrac{1}{2} (A + A^T)^T$$

**Paso 3 — Trasponer la suma (propiedad 2).** $(X+Y)^T = X^T + Y^T$ aplicado con $X = A$, $Y = A^T$:

$$= \tfrac{1}{2}(A^T + (A^T)^T)$$

> **¿Qué pasó?** Cada sumando se traspuso por separado.

**Paso 4 — Aplicar $(A^T)^T = A$ (propiedad 1).** El segundo sumando vuelve a ser $A$:

$$= \tfrac{1}{2}(A^T + A)$$

**Paso 5 — Conmutar la suma.** La suma de matrices SÍ es conmutativa, así que $A^T + A = A + A^T$:

$$= \tfrac{1}{2}(A + A^T)$$

> **¿Por qué puedo conmutar acá?** La SUMA de matrices conmuta (no como el producto). Eso es lo que me permite reordenar.

**Paso 6 — Reconocer que es $S$.** Llegamos exactamente a la definición original de $S$:

$$= S$$

**Conclusión.** $S^T = S$, así que $S$ es simétrica. $\blacksquare$

> **Idea central:** apliqué las 3 propiedades de traspuesta en cadena, más la conmutativa de la suma. Todo eran herramientas del repertorio que ya conocíamos.

### C.5 — $\frac{1}{2}(A - A^T)$ es antisimétrica

**Hipótesis:** $A$ matriz cuadrada cualquiera.

**Tesis:** $T = \frac{1}{2}(A - A^T)$ es antisimétrica.

**Demostración:**

$$T^T = \left[\tfrac{1}{2}(A - A^T)\right]^T = \tfrac{1}{2}(A - A^T)^T$$

$$= \tfrac{1}{2}\left(A^T - (A^T)^T\right) \quad \text{(prop 2 + linealidad de traspuesta)}$$

$$= \tfrac{1}{2}(A^T - A) \quad \text{(prop 1)}$$

$$= -\tfrac{1}{2}(A - A^T) = -T$$

Como $T^T = -T$, $T$ es antisimétrica. $\blacksquare$

### C.6 — Toda matriz cuadrada $A$ se escribe como simétrica $+$ antisimétrica

**Hipótesis:** $A$ matriz cuadrada cualquiera.

**Tesis:** existen $S$ simétrica y $T$ antisimétrica tales que $A = S + T$.

**Demostración:** definimos:

$$S = \tfrac{1}{2}(A + A^T), \qquad T = \tfrac{1}{2}(A - A^T)$$

Por C.4, $S$ es simétrica. Por C.5, $T$ es antisimétrica. Verificamos que $S + T = A$:

$$S + T = \tfrac{1}{2}(A + A^T) + \tfrac{1}{2}(A - A^T) = \tfrac{1}{2}A + \tfrac{1}{2}A^T + \tfrac{1}{2}A - \tfrac{1}{2}A^T = A \quad \blacksquare$$

---

## D. Traza

### D.1 — Propiedad 1: $tr(A + B) = tr(A) + tr(B)$

> **Cómo leer esta demo (en una frase):** desarmamos la traza usando su definición (suma de la diagonal), aplicamos que la suma de matrices es entrada por entrada, separamos en dos sumatorias y reconocemos que cada una es la traza de una matriz. Total: 4 pasos.

**Hipótesis:** $A, B \in \mathcal{M}_{n \times n}$ — cuadradas, misma dimensión (necesario para sumar y para que la traza tenga sentido).

**Tesis:** $tr(A+B) = tr(A) + tr(B)$.

> **Mini-recordatorio sobre $\sum$:** $\sum_{i=1}^n x_i$ significa $x_1 + x_2 + \cdots + x_n$. Es una notación corta para una suma con muchos términos.

**Demostración paso a paso:**

**Paso 1 — Aplicar la definición de traza.** La traza de una matriz $M$ es la suma de los elementos de su diagonal: $tr(M) = \sum_{i=1}^{n} m_{ii}$. Aplicado a $M = A + B$:

$$tr(A + B) = \sum_{i=1}^{n} (A + B)_{ii}$$

> **¿Qué dice esto?** Estoy sumando las entradas $(1,1), (2,2), \ldots, (n,n)$ de la matriz $A+B$.

**Paso 2 — Aplicar la definición de suma de matrices.** Cada entrada $(A+B)_{ii}$ es la suma de las entradas correspondientes de $A$ y $B$, o sea $a_{ii} + b_{ii}$:

$$= \sum_{i=1}^{n} (a_{ii} + b_{ii})$$

> **¿Qué cambió?** Donde antes había $(A+B)_{ii}$, ahora aparecen las entradas individuales $a_{ii}$ y $b_{ii}$ sumadas.

**Paso 3 — Separar la sumatoria.** Una propiedad de las sumatorias: $\sum (x_i + y_i) = \sum x_i + \sum y_i$. Aplicada acá:

$$= \sum_{i=1}^{n} a_{ii} + \sum_{i=1}^{n} b_{ii}$$

> **¿Por qué puedo separar?** Porque la suma es asociativa y conmutativa. Sumar $(a_1 + b_1) + (a_2 + b_2) + \ldots$ es lo mismo que sumar todos los $a_i$ por un lado y todos los $b_i$ por otro, y al final sumar los dos resultados.

**Paso 4 — Reconocer que cada sumatoria es una traza.** Por la definición de traza:

- $\sum_{i=1}^{n} a_{ii} = tr(A)$
- $\sum_{i=1}^{n} b_{ii} = tr(B)$

Sustituyendo:

$$= tr(A) + tr(B) \quad \blacksquare$$

> **Idea central:** la demostración consiste en bajar al nivel de las entradas, hacer la operación allí (donde es trivial), y volver a subir al nivel de matrices. Esa es la estrategia para muchas demos de propiedades.

### D.2 — Propiedad 2: $tr(\alpha A) = \alpha \cdot tr(A)$

> **Cómo leer esta demo (en una frase):** desarmamos la traza usando su definición, sacamos $\alpha$ como factor común de la sumatoria, y reconstruimos.

**Hipótesis:** $A \in \mathcal{M}_{n \times n}$, $\alpha \in \mathbb{R}$.

**Tesis:** $tr(\alpha A) = \alpha \cdot tr(A)$.

**Demostración paso a paso:**

**Paso 1 — Aplicar la definición de traza a $\alpha A$.**

$$tr(\alpha A) = \sum_{i=1}^{n} (\alpha A)_{ii}$$

**Paso 2 — Aplicar la definición de producto por escalar.** Cada entrada de $\alpha A$ es $\alpha$ por la entrada correspondiente de $A$:

$$= \sum_{i=1}^{n} \alpha \cdot a_{ii}$$

**Paso 3 — Sacar $\alpha$ como factor común.** Como $\alpha$ multiplica a cada término de la suma, lo puedo "factorizar" afuera:

$$= \alpha \cdot \sum_{i=1}^{n} a_{ii}$$

> **¿Por qué puedo?** Esa es una propiedad de las sumatorias: $\sum c \cdot x_i = c \cdot \sum x_i$ para cualquier constante $c$.

**Paso 4 — Reconocer la traza.**

$$= \alpha \cdot tr(A) \quad \blacksquare$$

### D.3 — Propiedad 3: $tr(A^T) = tr(A)$

> **Cómo leer esta demo (en una frase):** la traspuesta intercambia $a_{ij}$ con $a_{ji}$, pero los elementos de la **diagonal** ($a_{ii}$) no se mueven. Como la traza es la suma de la diagonal, no cambia.

**Hipótesis:** $A \in \mathcal{M}_{n \times n}$.

**Tesis:** $tr(A^T) = tr(A)$.

**Demostración paso a paso:**

**Paso 1 — Ver qué hace la traspuesta con la diagonal.** La traspuesta cambia $a_{ij}$ por $a_{ji}$. Pero en la diagonal $i = j$, así que $a_{ii}$ se cambia por $a_{ii}$ — **se queda igual**:

$$(A^T)_{ii} = a_{ii}$$

> **Visualización:** trasponer es como "voltear" la matriz por la diagonal. La diagonal misma queda fija — es el "eje de simetría" de la operación.

**Paso 2 — Calcular $tr(A^T)$ usando la definición.**

$$tr(A^T) = \sum_{i=1}^{n} (A^T)_{ii} = \sum_{i=1}^{n} a_{ii}$$

**Paso 3 — Reconocer la traza original.**

$$= tr(A) \quad \blacksquare$$

> **Idea central:** la traspuesta no toca la diagonal. Por eso la traza, que solo "ve" la diagonal, no cambia.

### D.4 — Propiedad 4: $tr(AB) = tr(BA)$

> **Cómo leer esta demo (en una frase):** escribimos $tr(AB)$ como una doble sumatoria (suma sobre $i$ de productos sobre $k$). Reordenamos los factores y los índices. Lo que queda coincide con la definición de $tr(BA)$.

**Hipótesis:** $A, B \in \mathcal{M}_{n \times n}$.

**Tesis:** $tr(AB) = tr(BA)$.

> **¿Por qué es notable?** Porque en general $AB \neq BA$ — son matrices distintas. Pero pese a eso, sus trazas coinciden.

**Demostración paso a paso:**

**Paso 1 — Calcular la entrada $(i,i)$ del producto $AB$.** Por la fórmula del producto matricial, la entrada $(i,i)$ se obtiene multiplicando la fila $i$ de $A$ por la columna $i$ de $B$:

$$(AB)_{ii} = \sum_{k=1}^{n} a_{ik} \cdot b_{ki}$$

> **¿Qué dice esa $\sum$?** Es la "fila $i$ por columna $i$" expresada compactamente: $a_{i1}b_{1i} + a_{i2}b_{2i} + \cdots + a_{in}b_{ni}$.

**Paso 2 — Aplicar la definición de traza a $AB$.** $tr(AB) = \sum_{i=1}^n (AB)_{ii}$. Sustituyendo lo del paso 1:

$$tr(AB) = \sum_{i=1}^{n} (AB)_{ii} = \sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik} \cdot b_{ki}$$

> **Atención: doble sumatoria.** Estamos sumando sobre dos índices: $i$ va de 1 a $n$, y para cada $i$, $k$ también va de 1 a $n$. En total son $n^2$ términos.
>
> **Visualización:** imaginá una grilla $n \times n$ donde en la celda $(i,k)$ está el número $a_{ik} \cdot b_{ki}$. La doble sumatoria suma todas esas celdas.

**Paso 3 — Intercambiar el orden de las sumatorias.** En sumas finitas, es válido cambiar el orden: $\sum_i \sum_k = \sum_k \sum_i$. Es lo mismo que sumar primero por filas o primero por columnas en la grilla — el total es igual.

$$= \sum_{k=1}^{n} \sum_{i=1}^{n} a_{ik} \cdot b_{ki}$$

> **¿Por qué puedo cambiar el orden?** Porque las sumas finitas son asociativas y conmutativas. Si tengo una grilla de números, sumarlos por filas o por columnas da el mismo total.

**Paso 4 — Conmutar los factores adentro.** $a_{ik}$ y $b_{ki}$ son **números reales**, así que conmutan: $a_{ik} \cdot b_{ki} = b_{ki} \cdot a_{ik}$:

$$= \sum_{k=1}^{n} \sum_{i=1}^{n} b_{ki} \cdot a_{ik}$$

> **Cuidado:** las MATRICES no conmutan, pero adentro de la sumatoria estamos manipulando NÚMEROS — y los números siempre conmutan.

**Paso 5 — Reconocer la entrada $(k,k)$ de $BA$.** Por la fórmula del producto, la entrada $(k,k)$ de $BA$ se obtiene multiplicando la fila $k$ de $B$ por la columna $k$ de $A$:

$$(BA)_{kk} = \sum_{i=1}^{n} b_{ki} \cdot a_{ik}$$

Comparando con la sumatoria interna del paso 4, ¡es exactamente eso! Entonces:

$$\sum_{k=1}^{n} \sum_{i=1}^{n} b_{ki} \cdot a_{ik} = \sum_{k=1}^{n} (BA)_{kk}$$

**Paso 6 — Reconocer la traza de $BA$.** Por la definición de traza:

$$\sum_{k=1}^{n} (BA)_{kk} = tr(BA)$$

**Conclusión.** Encadenando los pasos:

$$tr(AB) = tr(BA) \quad \blacksquare$$

> **Idea central:** la prueba es una manipulación de doble sumatoria. La clave fue reconocer que después de intercambiar el orden y conmutar los factores, lo que queda es exactamente la traza de $BA$.
>
> **Por qué es tan útil esta propiedad:** es la base de la "demo estrella" $D.6$. Sin ella, no se podría probar que no existen $A, B$ con $AB - BA = \text{Id}$.

### D.5 — Corolario: $tr(A - B) = tr(A) - tr(B)$

**Hipótesis:** $A, B \in \mathcal{M}_{n \times n}$.

**Tesis:** $tr(A - B) = tr(A) - tr(B)$.

**Demostración:**

$$tr(A - B) = tr(A + (-1) \cdot B) \quad \text{(reescribir la resta)}$$

$$= tr(A) + tr((-1) B) \quad \text{(propiedad 1, §D.1)}$$

$$= tr(A) + (-1) \cdot tr(B) \quad \text{(propiedad 2, §D.2)}$$

$$= tr(A) - tr(B) \quad \blacksquare$$

### D.6 — Aplicación clásica: NO existen $A, B$ tales que $AB - BA = \text{Id}$

> 🌟 **La estrella del módulo de traza** — la demo más probable de caer en parcial.
>
> **Cómo leer esta demo (en una frase):** demostración por **absurdo**. Suponemos que existen tales $A, B$, le tomamos traza a ambos lados, y llegamos a $0 = n$. Como eso es imposible (porque $n \geq 1$), nuestra suposición debe ser falsa.

**Tesis:** No existen matrices cuadradas $A, B$ tales que $AB - BA = \text{Id}$.

> **¿Qué es "demostración por absurdo"?** Es una técnica: para probar que algo NO existe (o NO se cumple), asumimos que SÍ existe (o SÍ se cumple), y mostramos que eso lleva a una contradicción. Como las matemáticas no toleran contradicciones, la suposición original debe ser falsa.

**Demostración paso a paso:**

**Paso 1 — Asumir lo opuesto (la suposición que va a romperse).** Supongamos que SÍ existen $A, B$ cuadradas $n \times n$ tales que:

$$AB - BA = \text{Id}$$

> **Lo que voy a hacer:** voy a operar en esta ecuación hasta llegar a un absurdo, lo que probará que la suposición no puede ser cierta.

**Paso 2 — Tomar traza a ambos lados.** Si dos matrices son iguales, sus trazas también:

$$tr(AB - BA) = tr(\text{Id})$$

> **¿Por qué traza?** Porque la traza tiene una propiedad mágica para esta situación: $tr(AB) = tr(BA)$ aunque $AB \neq BA$. Eso va a ser clave para forzar la contradicción.

**Paso 3 — Calcular el lado izquierdo.** Aplicamos el corolario §D.5 (la traza distribuye sobre la resta):

$$tr(AB - BA) = tr(AB) - tr(BA)$$

Ahora aplicamos la propiedad 4 de traza ($tr(AB) = tr(BA)$):

$$= tr(AB) - tr(AB) = 0$$

> **¿Qué pasó?** $tr(AB)$ y $tr(BA)$ son el **mismo número** (por propiedad 4). Restar un número de sí mismo da cero.

**Paso 4 — Calcular el lado derecho.** La traza de la identidad $n \times n$ es la suma de los $n$ unos de su diagonal:

$$tr(\text{Id}) = \underbrace{1 + 1 + \cdots + 1}_{n \text{ veces}} = n$$

> **Recordá:** $\text{Id}$ tiene $1$ en cada lugar de la diagonal y $0$ afuera. Si es $\text{Id}_{3\times 3}$, $tr(\text{Id}) = 1+1+1 = 3$.

**Paso 5 — Confrontar.** Volviendo al paso 2, lado izquierdo igual a lado derecho:

$$0 = n$$

**Paso 6 — Detectar el absurdo.** $n$ es la dimensión de las matrices, y por definición $n \geq 1$. Pero acá tendríamos $0 = n \geq 1$, o sea $0 \geq 1$. **Eso es falso** — es una contradicción matemática.

**Conclusión.** Como llegar a una contradicción significa que algo en la cadena de razonamientos era inválido, y el único paso que era una **suposición** fue el paso 1, esa suposición debe ser falsa.

Por lo tanto: **no existen matrices $A, B$ tales que $AB - BA = \text{Id}$.** $\blacksquare$

> **Idea central:** la propiedad 4 de traza ($tr(AB) = tr(BA)$) es lo que mata la suposición. Sin esa propiedad, $tr(AB) - tr(BA)$ no daría $0$ y todo el argumento se cae.
>
> **Por qué es elegante:** esta demo prueba que algo "nunca pasa" sin tener que verificar caso por caso. Ese tipo de razonamiento abstracto es lo que el profesor quiere ver en parcial.

---

## E. Inversa

### E.1 — Propiedad 1: $(A^{-1})^{-1} = A$

> **Cómo leer esta demo (en una frase):** la propia definición de inversa ya nos dice que $A$ es la inversa de $A^{-1}$ — solo hay que mirar la igualdad al revés.

**Hipótesis:** $A$ invertible.

**Tesis:** $A^{-1}$ también es invertible y $(A^{-1})^{-1} = A$.

**Demostración paso a paso:**

**Paso 1 — Recordar la definición de inversa.** Por hipótesis, $A^{-1}$ es la inversa de $A$:

$$A^{-1} \cdot A = \text{Id} \qquad \text{y} \qquad A \cdot A^{-1} = \text{Id}$$

**Paso 2 — Mirar esa misma igualdad pensando en $A^{-1}$ como la "matriz central".** Las dos igualdades anteriores dicen exactamente que **$A$ funciona como inversa de $A^{-1}$**: hay una matriz (que es $A$) que multiplicada por $A^{-1}$ por cualquier lado da $\text{Id}$.

**Paso 3 — Concluir por unicidad.** Como la inversa es única, esa matriz tiene que ser $(A^{-1})^{-1}$. Pero ya identificamos que es $A$:

$$(A^{-1})^{-1} = A \quad \blacksquare$$

> **Idea central:** "ser inversa" es una relación simétrica. Si $B$ es inversa de $A$, entonces $A$ es inversa de $B$.

### E.2 — Propiedad 2: $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$ (orden invertido)

> **Cómo leer esta demo (en una frase):** queremos probar que la inversa de $AB$ es $B^{-1}A^{-1}$. Para hacerlo, multiplicamos $AB$ por $B^{-1}A^{-1}$ y mostramos que el resultado es $\text{Id}$ — eso prueba (por unicidad) que esa es la inversa.

**Hipótesis:** $A$ y $B$ son matrices invertibles, ambas $n \times n$.

> **Recordá:** "$A$ invertible" significa que existe $A^{-1}$ tal que $A \cdot A^{-1} = A^{-1} \cdot A = \text{Id}$. Lo mismo para $B$.

**Tesis:** $(AB)^{-1} = B^{-1} A^{-1}$.

**Estrategia general antes de empezar.** Para probar que cierta matriz $X$ es la inversa de otra matriz $Y$, alcanza con verificar $Y \cdot X = \text{Id}$ (por unicidad de la inversa, eso es suficiente). Acá $Y = AB$ y queremos probar que $X = B^{-1}A^{-1}$ es la inversa.

**Demostración paso a paso:**

**Paso 1 — Plantear el producto a verificar.** Multiplicamos $AB$ por nuestro candidato a inversa $B^{-1}A^{-1}$:

$$(AB)(B^{-1} A^{-1})$$

> **Objetivo:** llegar a $\text{Id}$. Si lo logramos, queda probada la tesis.

**Paso 2 — Reagrupar usando asociativa.** El producto de matrices es asociativo, así que puedo reorganizar los paréntesis sin cambiar el resultado. Reagrupo de modo que $B$ y $B^{-1}$ queden juntos:

$$(AB)(B^{-1} A^{-1}) = A \cdot (B \cdot B^{-1}) \cdot A^{-1}$$

> **¿Qué hice?** Antes los paréntesis agrupaban $(AB)$ y $(B^{-1}A^{-1})$. Ahora los reagrupé como $A \cdot (B B^{-1}) \cdot A^{-1}$. Es válido porque la asociativa me deja mover paréntesis sin cambiar el orden de los factores.

**Paso 3 — Usar la definición de inversa de $B$.** Por definición, $B \cdot B^{-1} = \text{Id}$:

$$= A \cdot \text{Id} \cdot A^{-1}$$

> **¿Qué cambió?** El bloque $B \cdot B^{-1}$ del medio se convirtió en $\text{Id}$.

**Paso 4 — Aplicar el neutro del producto.** Multiplicar por $\text{Id}$ no cambia nada: $A \cdot \text{Id} = A$:

$$= A \cdot A^{-1}$$

> **¿Qué pasó?** El $\text{Id}$ del medio "desapareció" porque multiplicar por la identidad deja todo igual.

**Paso 5 — Usar la definición de inversa de $A$.** Por definición, $A \cdot A^{-1} = \text{Id}$:

$$= \text{Id}$$

**Conclusión.** Logramos $(AB) \cdot (B^{-1} A^{-1}) = \text{Id}$. Por la estrategia inicial, esto significa que $B^{-1} A^{-1}$ es la inversa de $AB$:

$$(AB)^{-1} = B^{-1} A^{-1} \quad \blacksquare$$

> **Analogía para no olvidar el orden invertido:** si te ponés medias y después zapatos, para sacártelos hacés el orden inverso — primero zapatos, después medias. **Lo último que entra es lo primero que sale.**
>
> **Idea central:** la prueba consiste en hacer que "el del medio" ($B \cdot B^{-1}$) se simplifique a $\text{Id}$, lo que destapa al "de afuera" ($A \cdot A^{-1}$), que también se simplifica a $\text{Id}$.

### E.3 — Propiedad 3: $(\alpha A)^{-1} = \frac{1}{\alpha} A^{-1}$, $\alpha \neq 0$

> **Cómo leer esta demo (en una frase):** verificamos que $\frac{1}{\alpha} A^{-1}$ funciona como inversa de $\alpha A$ multiplicándolas. Los escalares se simplifican a $1$, las matrices a $\text{Id}$, total $\text{Id}$.

**Hipótesis:** $A$ invertible, $\alpha \neq 0$.

> **¿Por qué $\alpha \neq 0$?** Porque $\frac{1}{\alpha}$ tiene que estar definido. Si $\alpha = 0$, $\alpha A$ sería la nula, y la nula no es invertible.

**Tesis:** $(\alpha A)^{-1} = \frac{1}{\alpha} A^{-1}$.

**Demostración paso a paso:**

**Paso 1 — Plantear el producto a verificar.** Multiplicamos $\alpha A$ por nuestro candidato a inversa:

$$(\alpha A) \cdot \left(\tfrac{1}{\alpha} A^{-1}\right)$$

**Paso 2 — Reagrupar escalares y matrices por separado.** Los escalares conmutan con todo, así que los puedo "juntar" al frente:

$$= \alpha \cdot \tfrac{1}{\alpha} \cdot (A \cdot A^{-1})$$

> **¿Qué hice?** Saqué $\alpha$ y $\frac{1}{\alpha}$ afuera de las matrices y los junté. Las matrices $A$ y $A^{-1}$ quedan multiplicándose entre sí.

**Paso 3 — Simplificar el producto de escalares.** $\alpha \cdot \frac{1}{\alpha} = 1$:

$$= 1 \cdot (A \cdot A^{-1})$$

**Paso 4 — Aplicar la inversa de $A$.** $A \cdot A^{-1} = \text{Id}$:

$$= 1 \cdot \text{Id} = \text{Id}$$

**Conclusión.** Verificamos que $(\alpha A) \cdot \left(\frac{1}{\alpha} A^{-1}\right) = \text{Id}$. Por definición:

$$(\alpha A)^{-1} = \tfrac{1}{\alpha} A^{-1} \quad \blacksquare$$

> **Idea central:** los escalares se invierten "naturalmente" — si la matriz se multiplica por $\alpha$, la inversa se multiplica por $\frac{1}{\alpha}$. Es como con números: $(5 \cdot x)^{-1} = \frac{1}{5} \cdot x^{-1}$.

### E.4 — Propiedad 4: $(A^T)^{-1} = (A^{-1})^T$

> **Cómo leer esta demo (en una frase):** verificamos que $(A^{-1})^T$ funciona como inversa de $A^T$ usando la propiedad 4 de traspuesta al revés.

**Hipótesis:** $A$ invertible.

**Tesis:** $A^T$ también es invertible y $(A^T)^{-1} = (A^{-1})^T$.

**Demostración paso a paso:**

**Paso 1 — Plantear el producto a verificar.** Multiplicamos $A^T$ por nuestro candidato $(A^{-1})^T$:

$$A^T \cdot (A^{-1})^T$$

**Paso 2 — Aplicar la propiedad 4 de traspuesta al revés.** La propiedad dice $(XY)^T = Y^T X^T$. Si la leés al revés: $Y^T X^T = (XY)^T$. Identificando $Y^T = A^T$ (entonces $Y = A$) y $X^T = (A^{-1})^T$ (entonces $X = A^{-1}$):

$$A^T \cdot (A^{-1})^T = (A^{-1} \cdot A)^T$$

> **¿Qué pasó?** Junté las dos traspuestas en una sola, pero el orden adentro se invirtió: lo que estaba afuera (en el orden $A^T \cdot (A^{-1})^T$) adentro queda como $A^{-1} \cdot A$.

**Paso 3 — Aplicar $A^{-1} \cdot A = \text{Id}$.**

$$= \text{Id}^T$$

**Paso 4 — Aplicar que la identidad es simétrica ($\text{Id}^T = \text{Id}$).**

$$= \text{Id}$$

**Conclusión.** Verificamos $A^T \cdot (A^{-1})^T = \text{Id}$. Por definición:

$$A^T \text{ es invertible y } (A^T)^{-1} = (A^{-1})^T \quad \blacksquare$$

> **Idea central:** trasponer y invertir son operaciones que **conmutan entre sí**: hacer una y después la otra da lo mismo que hacerlas al revés. Por eso $(A^T)^{-1} = (A^{-1})^T$.

---

## F. Idempotente y nilpotente

### F.1 — Idempotente $+$ invertible $\Rightarrow A = \text{Id}$ (ejercicio VI.2)

> **Cómo leer esta demo (en una frase):** partimos de la idempotencia ($A^2 = A$) y multiplicamos a izquierda por $A^{-1}$. Eso "cancela" un $A$ del lado izquierdo y deja $A = \text{Id}$.

**Hipótesis:**
- $A^2 = A$ — esto es la definición de **idempotente**.
- $A$ es **invertible** — existe $A^{-1}$.

> **¿Por qué necesito ambas?** Si solo fuera idempotente, $A$ podría ser cualquier proyección (por ejemplo $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$). Lo que descarta esos casos es que también sea invertible.

**Tesis:** $A = \text{Id}$.

**Demostración paso a paso:**

**Paso 1 — Empezar por la hipótesis de idempotencia.**

$$A^2 = A$$

> **Estrategia:** voy a "despejar" $A$ multiplicando por $A^{-1}$ a izquierda en ambos lados. Cuando $A^{-1}$ aparezca junto a $A$, se simplifican a $\text{Id}$.

**Paso 2 — Multiplicar a izquierda por $A^{-1}$ en ambos lados.**

$$A^{-1} \cdot A^2 = A^{-1} \cdot A$$

> **¿Por qué a izquierda y no a derecha?** Es indiferente, pero a izquierda funciona naturalmente con $A^2 = A \cdot A$ porque va a "comer" el primer $A$. La regla general: en una igualdad podés multiplicar ambos lados por la misma matriz, del mismo lado, sin perder la igualdad.
>
> **¿Por qué necesito que $A$ sea invertible?** Para que $A^{-1}$ exista. Si $A$ no fuera invertible, esta multiplicación no sería válida.

**Paso 3 — Reescribir $A^2$ como $A \cdot A$.**

$$A^{-1} \cdot A \cdot A = A^{-1} \cdot A$$

> **¿Qué hice?** $A^2$ por definición es $A \cdot A$. Lo escribo así para que se vea claramente cómo se va a simplificar.

**Paso 4 — Aplicar $A^{-1} \cdot A = \text{Id}$ en ambos lados.** Por definición de inversa, $A^{-1}A$ se simplifica a $\text{Id}$. Eso pasa en ambos lados de la igualdad:

$$\text{Id} \cdot A = \text{Id}$$

> **¿Qué pasó?** En el lado izquierdo, $A^{-1} \cdot A \cdot A$ → reagrupando como $(A^{-1} A) \cdot A$ → eso es $\text{Id} \cdot A$. En el lado derecho, $A^{-1} \cdot A = \text{Id}$ directo.

**Paso 5 — Aplicar $\text{Id} \cdot A = A$.** Multiplicar por la identidad no cambia nada:

$$A = \text{Id} \quad \blacksquare$$

**Conclusión.** $A$ es exactamente la matriz identidad.

> **Idea central:** la idempotencia te da $A \cdot A = A$. La invertibilidad te permite "cancelar" un $A$ multiplicando por $A^{-1}$. Cancelando, queda $A = \text{Id}$.
>
> **Aclaración importante:** esto NO dice que TODA matriz idempotente sea $\text{Id}$. Solo cuando además es invertible. La nula $\mathcal{O}$ y $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ son idempotentes y NO son $\text{Id}$ — pero tampoco son invertibles, así que no contradicen el resultado.

### F.2 — Si $A$ es idempotente, $(A + \text{Id})^3 = \text{Id} + 7A$

> **Cómo leer esta demo (en una frase):** desarrollamos $(A + \text{Id})^3$ usando el binomio de Newton (lo que se enseña para $(x+y)^3$, pero acá con matrices), simplificamos $\text{Id}^k = \text{Id}$, usamos que $A^k = A$ por idempotencia, y juntamos términos.

**Hipótesis:** $A^2 = A$ (idempotente).

> **Consecuencia importante:** si $A^2 = A$, entonces $A^3 = A \cdot A^2 = A \cdot A = A^2 = A$. Por inducción, $A^k = A$ para todo $k \geq 1$.

**Tesis:** $(A + \text{Id})^3 = \text{Id} + 7A$.

**Demostración paso a paso:**

**Paso 1 — Aplicar el binomio de Newton.** Para $(x+y)^3$ del álgebra: $x^3 + 3x^2y + 3xy^2 + y^3$. Eso vale para matrices SIEMPRE QUE las matrices conmuten entre sí. Acá $A$ y $\text{Id}$ sí conmutan ($\text{Id}$ conmuta con todas las matrices), así que aplicamos:

$$(A + \text{Id})^3 = A^3 + 3 A^2 \text{Id} + 3 A \text{Id}^2 + \text{Id}^3$$

> **¿Por qué tengo que verificar que conmuten?** Porque si no conmutaran, los términos cruzados no se podrían escribir como $3 A^2 \text{Id}$ — habría que mantener el orden y aparecerían más términos. Como $A \cdot \text{Id} = \text{Id} \cdot A$, no hay drama.

**Paso 2 — Simplificar las potencias de $\text{Id}$.** $\text{Id}^k = \text{Id}$ para cualquier $k$ (multiplicar la identidad por sí misma da la identidad). Y multiplicar por $\text{Id}$ no cambia la matriz:

$$= A^3 + 3 A^2 + 3 A + \text{Id}$$

> **Detalle:** $A^2 \text{Id} = A^2$, $A \text{Id}^2 = A \cdot \text{Id} = A$, y $\text{Id}^3 = \text{Id}$.

**Paso 3 — Aplicar la hipótesis de idempotencia.** Como $A^k = A$ para todo $k \geq 1$:

- $A^3 = A$
- $A^2 = A$

Sustituyendo:

$$= A + 3A + 3A + \text{Id}$$

**Paso 4 — Sumar los términos en $A$.**

$$A + 3A + 3A = (1 + 3 + 3) A = 7A$$

Quedando:

$$= 7A + \text{Id} = \text{Id} + 7A \quad \blacksquare$$

> **Idea central:** todo el truco está en que $A$ idempotente convierte $A^2, A^3, \ldots$ todos en $A$. Eso "colapsa" el binomio de Newton en una expresión muy simple.

### F.3 — $P^{-1} A P$ es nilpotente del mismo grado que $A$ (ejercicio V.7.2)

> **Cómo leer esta demo (en una frase):** la demo tiene **dos partes**: (1) probar que $B^k = \mathcal{O}$ usando que $P P^{-1} = \text{Id}$ se cancela en el medio; (2) probar que $B^{k-1} \neq \mathcal{O}$ por absurdo.

**Hipótesis:**
- $A$ es nilpotente de grado $k$. Esto significa: $A^k = \mathcal{O}$ Y $A^{k-1} \neq \mathcal{O}$.
- $P$ es invertible (existe $P^{-1}$).

> **Recordá:** "nilpotente de grado $k$" = la primera potencia que da la nula es $k$. Si $k = 3$: $A, A^2$ no son nulas pero $A^3$ sí.

**Tesis:** $B = P^{-1} A P$ es nilpotente de grado **exactamente** $k$. Es decir:
- $B^k = \mathcal{O}$
- $B^{k-1} \neq \mathcal{O}$

> **Por qué hay que probar las dos cosas:** "nilpotente de grado $k$" exige no solo que la potencia $k$ se anule, sino que la anterior NO. Si solo probáramos $B^k = \mathcal{O}$, podría ser que $B^{k-1} = \mathcal{O}$ también, y entonces el grado sería menor que $k$.

---

#### PARTE 1 — Probar que $B^k = \mathcal{O}$

**Paso 1 — Calcular $B^2$ para entender el patrón.**

$$B^2 = (P^{-1} A P)(P^{-1} A P)$$

**Paso 2 — Reagrupar usando asociativa.** Saco los paréntesis y reagrupo de modo que $P$ y $P^{-1}$ del medio queden juntos:

$$= P^{-1} A (P P^{-1}) A P$$

**Paso 3 — Aplicar $P P^{-1} = \text{Id}$.**

$$= P^{-1} A \cdot \text{Id} \cdot A P = P^{-1} \cdot A^2 \cdot P$$

> **¿Qué pasó?** El "sandwich" $P P^{-1}$ del medio se simplificó a $\text{Id}$, que después desapareció (porque multiplicar por $\text{Id}$ no cambia nada). Lo que sobrevive es $A \cdot A = A^2$ con $P^{-1}$ a izquierda y $P$ a derecha.

**Paso 4 — Generalizar a $B^k$.** El mismo patrón se repite cuando hacés $B^k$: cada vez que se forma un $P P^{-1}$ en el medio, se cancela. Por inducción se prueba:

$$B^k = P^{-1} A^k P$$

> **¿Cómo se demuestra eso por inducción?** Asumís $B^h = P^{-1} A^h P$. Calculás $B^{h+1} = B^h \cdot B = (P^{-1} A^h P)(P^{-1} A P) = P^{-1} A^h (P P^{-1}) A P = P^{-1} A^{h+1} P$. ✓

**Paso 5 — Aplicar la hipótesis $A^k = \mathcal{O}$.**

$$B^k = P^{-1} \cdot \mathcal{O} \cdot P = \mathcal{O}$$

> **¿Por qué $P^{-1} \cdot \mathcal{O} \cdot P = \mathcal{O}$?** Cualquier producto que tenga la matriz nula como factor da la matriz nula. Multiplicás todo por cero, todo es cero.

✓ **Probado: $B^k = \mathcal{O}$.**

---

#### PARTE 2 — Probar que $B^{k-1} \neq \mathcal{O}$ (por absurdo)

**Paso 1 — Suponer lo contrario.** Asumimos que sí, $B^{k-1} = \mathcal{O}$. Vamos a ver que eso lleva a una contradicción.

**Paso 2 — Escribir $B^{k-1}$ en términos de $A$.** Por el patrón visto antes, $B^{k-1} = P^{-1} A^{k-1} P$. Si esto es $\mathcal{O}$:

$$P^{-1} A^{k-1} P = \mathcal{O}$$

**Paso 3 — Despejar $A^{k-1}$.** Multiplico a izquierda por $P$ y a derecha por $P^{-1}$:

$$P \cdot P^{-1} A^{k-1} P \cdot P^{-1} = P \cdot \mathcal{O} \cdot P^{-1}$$

**Paso 4 — Simplificar.** $P \cdot P^{-1} = \text{Id}$ a izquierda; $P \cdot P^{-1} = \text{Id}$ a derecha; cualquier cosa por nula es nula:

$$\text{Id} \cdot A^{k-1} \cdot \text{Id} = \mathcal{O}$$

$$A^{k-1} = \mathcal{O}$$

**Paso 5 — Detectar la contradicción.** Pero la hipótesis del ejercicio dice $A^{k-1} \neq \mathcal{O}$ (porque $A$ es nilpotente de grado **exactamente** $k$). Contradicción.

✓ Por lo tanto, **$B^{k-1} \neq \mathcal{O}$.**

---

**Conclusión.** Combinando PARTE 1 y PARTE 2: $B^k = \mathcal{O}$ y $B^{k-1} \neq \mathcal{O}$, así que $B = P^{-1} A P$ es nilpotente de grado **exactamente** $k$. $\blacksquare$

> **Idea central:** el "sandwich $P^{-1} \ldots P$" se mantiene a través de todas las potencias. Eso permite trasladar las propiedades de $A$ ($A^k = \mathcal{O}$, $A^{k-1} \neq \mathcal{O}$) a $B$ exactamente.

### F.3 — $P^{-1} A P$ es nilpotente del mismo grado que $A$ (ejercicio V.7.2)

**Hipótesis:** $A$ nilpotente de grado $k$ ($A^k = \mathcal{O}$, $A^{k-1} \neq \mathcal{O}$); $P$ invertible.

**Tesis:** $B = P^{-1} A P$ es nilpotente de grado exactamente $k$.

**Demostración (paso 1: $B^k = \mathcal{O}$).**

Calculemos $B^2$ primero para ver el patrón:

$$B^2 = (P^{-1} A P)(P^{-1} A P) = P^{-1} A (P P^{-1}) A P = P^{-1} A \cdot \text{Id} \cdot A \cdot P = P^{-1} A^2 P$$

Por inducción se generaliza: $B^k = P^{-1} A^k P$.

$$B^k = P^{-1} A^k P = P^{-1} \cdot \mathcal{O} \cdot P = \mathcal{O} \quad \text{(hipótesis: }A^k = \mathcal{O}\text{)}$$

**Paso 2: $B^{k-1} \neq \mathcal{O}$ (por absurdo).**

Supongamos que $B^{k-1} = \mathcal{O}$. Entonces:

$$P^{-1} A^{k-1} P = \mathcal{O}$$

Multiplicando por $P$ a izquierda y $P^{-1}$ a derecha:

$$P \cdot P^{-1} A^{k-1} P \cdot P^{-1} = P \cdot \mathcal{O} \cdot P^{-1}$$

$$\text{Id} \cdot A^{k-1} \cdot \text{Id} = \mathcal{O}$$

$$A^{k-1} = \mathcal{O}$$

Pero esto **contradice** la hipótesis de que $A^{k-1} \neq \mathcal{O}$. Absurdo.

Combinando paso 1 y paso 2: $B$ es nilpotente de grado exactamente $k$. $\blacksquare$

---

## G. Inducción

> **Esquema común para inducciones de potencias:**
> 1. **Base** ($n = 1$ o $n = 2$): verificar directo.
> 2. **Hipótesis inductiva** ($n = h$): asumir la fórmula para $h$.
> 3. **Tesis** ($n = h+1$): escribir lo que querés probar.
> 4. **Paso inductivo:** usar $A^{h+1} = A^h \cdot A$ y aplicar la hipótesis.

### G.1 — Inducción para $A^n$ con $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ (ejercicio VI.1)

> **Cómo leer esta demo (en una frase):** la **inducción completa** es una técnica para probar fórmulas que valen "para todo $n$". Tiene 3 partes: (1) verificar para $n=1$, (2) asumir que vale para algún $h$, (3) probar que vale para $h+1$.

**¿Qué es la inducción completa?** Imaginá una fila infinita de fichas de dominó. Si demostrás que (a) la primera ficha cae, y (b) cada vez que cae una ficha hace caer a la siguiente, entonces todas las fichas caen.

En matemáticas, eso se traduce en:
- **Base:** mostrar que la fórmula vale para $n = 1$.
- **Hipótesis inductiva:** ASUMIR que vale para un $n = h$ cualquiera.
- **Paso inductivo:** PROBAR que entonces vale para $n = h + 1$.

Si lográs los 3, la fórmula vale para TODO $n \geq 1$.

---

**Hipótesis sobre $A$:** $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

**Tesis:** Para todo $n \geq 1$:

$$A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$$

> **¿Qué dice esta fórmula?** Que para sacar $A^n$, basta con poner $n$ en la posición $(1,2)$ y dejar el resto igual a $A$.

**Demostración por inducción paso a paso:**

#### PARTE A — Base ($n = 1$)

Verifico que la fórmula valga para el primer caso:

$$A^1 = A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

Y la fórmula con $n = 1$ da $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

**Coinciden.** ✓ La fórmula vale para $n = 1$.

#### PARTE B — Hipótesis inductiva ($n = h$)

Asumimos (sin probarla, solo la suponemos) que la fórmula vale para algún $h$ cualquiera:

$$A^h = \begin{pmatrix} 1 & h \\ 0 & 1 \end{pmatrix}$$

> **¿Por qué puedo asumir esto?** Porque la inducción funciona así: en este paso no estoy probando nada, solo estoy "agarrándome" del caso $h$ para usarlo como apoyo en el siguiente paso.

#### PARTE C — Tesis del paso inductivo ($n = h+1$)

Lo que tengo que demostrar:

$$A^{h+1} = \begin{pmatrix} 1 & h+1 \\ 0 & 1 \end{pmatrix}$$

> **¿Qué cambió respecto a la hipótesis?** Donde antes había $h$ ahora hay $h+1$. La idea es ver que si la fórmula vale con $h$, entonces vale con $h+1$.

#### PARTE D — Paso inductivo (demostración propiamente dicha)

**Paso 1 — Reescribir $A^{h+1}$ en términos de $A^h$.** Por definición de potencias, $A^{h+1} = A^h \cdot A$:

$$A^{h+1} = A^h \cdot A$$

> **¿De dónde sale esto?** Es solo la propiedad de potencias: $X^{n+1} = X^n \cdot X$. Vale para números y para matrices.

**Paso 2 — Usar la hipótesis inductiva.** Reemplazo $A^h$ por la fórmula que asumí en la PARTE B:

$$= \begin{pmatrix} 1 & h \\ 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

> **Esto es lo más importante:** el paso inductivo siempre usa la hipótesis. Sin usarla, no es inducción.

**Paso 3 — Hacer la multiplicación de matrices, entrada por entrada.** Aplico la regla "fila por columna" para cada una de las 4 entradas:

- Entrada $(1,1)$: fila 1 · col 1 = $1 \cdot 1 + h \cdot 0 = 1$
- Entrada $(1,2)$: fila 1 · col 2 = $1 \cdot 1 + h \cdot 1 = 1 + h = h + 1$
- Entrada $(2,1)$: fila 2 · col 1 = $0 \cdot 1 + 1 \cdot 0 = 0$
- Entrada $(2,2)$: fila 2 · col 2 = $0 \cdot 1 + 1 \cdot 1 = 1$

Armando la matriz resultante:

$$= \begin{pmatrix} 1 & h+1 \\ 0 & 1 \end{pmatrix}$$

**Paso 4 — Comparar con la tesis.** ¡Coincide exactamente con la PARTE C! ✓

#### Conclusión

Probamos las 3 partes:
- Base: vale para $n = 1$.
- Suponiendo que vale para $h$, probamos que vale para $h + 1$.

Por el principio de inducción completa, la fórmula vale para TODO $n \geq 1$. $\blacksquare$

> **Idea central de toda inducción:** la "ficha de dominó" del caso $h$ tira la ficha del caso $h+1$. Como la primera ficha (caso $n=1$) ya cayó, todas caen.

### G.2 — Inducción para $A^n$ con $A^2 = 2A - \text{Id}$ (ejercicio V.10.3)

> **Cómo leer esta demo (en una frase):** misma estructura de inducción que G.1, pero acá el truco está en usar la hipótesis $A^2 = 2A - \text{Id}$ para "bajar la potencia": cuando aparece $A^2$ en el medio, lo reemplazamos por $2A - \text{Id}$ y todo se simplifica.

**Hipótesis sobre $A$:** $A$ cuadrada con $A^2 = 2A - \text{Id}$.

> **¿Qué tipo de matriz cumple esto?** Es una propiedad poco usual — solo ciertas matrices la satisfacen. La existencia de la hipótesis es la clave para resolver el ejercicio.

**Tesis:** Para todo $n \geq 1$, $A^n = nA - (n-1)\text{Id}$.

> **¿Qué dice la fórmula?** Que toda potencia $A^n$ se puede escribir como combinación lineal de $A$ y $\text{Id}$ (con coeficientes $n$ y $-(n-1)$). Es muy útil porque te ahorra calcular potencias gigantes.

**Demostración por inducción paso a paso:**

#### PARTE A — Base ($n = 1$)

$$A^1 = A$$

Y la fórmula con $n = 1$ da:

$$1 \cdot A - (1-1) \cdot \text{Id} = A - 0 = A \quad \checkmark$$

Coincide.

#### PARTE B — Hipótesis inductiva ($n = h$)

Asumimos:

$$A^h = h \cdot A - (h-1) \cdot \text{Id}$$

#### PARTE C — Tesis ($n = h+1$)

Queremos probar:

$$A^{h+1} = (h+1) \cdot A - h \cdot \text{Id}$$

#### PARTE D — Paso inductivo

**Paso 1 — Reescribir $A^{h+1}$ en términos de $A^h$.**

$$A^{h+1} = A^h \cdot A$$

**Paso 2 — Aplicar la hipótesis inductiva.** Reemplazo $A^h$:

$$= [hA - (h-1)\text{Id}] \cdot A$$

**Paso 3 — Distribuir el producto.** Aplico la propiedad distributiva (cada término del corchete multiplica a $A$):

$$= hA \cdot A - (h-1)\text{Id} \cdot A$$

> **Cuidado con los escalares:** $h$ y $(h-1)$ son números, así que se quedan como factor. Lo que estoy multiplicando son matrices: $A \cdot A$ y $\text{Id} \cdot A$.

**Paso 4 — Simplificar usando $A \cdot A = A^2$ y $\text{Id} \cdot A = A$.**

$$= h A^2 - (h-1) A$$

> **¿Qué pasó?** $A \cdot A$ por definición es $A^2$. Y $\text{Id} \cdot A = A$ porque $\text{Id}$ es el neutro del producto.

**Paso 5 — Aplicar la hipótesis sobre $A^2$.** Acá viene el truco clave. La hipótesis del enunciado dice $A^2 = 2A - \text{Id}$:

$$= h(2A - \text{Id}) - (h-1) A$$

> **Esto es lo único que cambia respecto a una inducción "normal".** En lugar de tener un $A^2$ que no podemos manipular, lo reemplazamos por algo que sí podemos manipular ($2A - \text{Id}$).

**Paso 6 — Distribuir el $h$ del primer término.**

$$= 2hA - h \, \text{Id} - (h-1) A$$

**Paso 7 — Agrupar los términos en $A$.** Los términos en $A$ son $2hA$ y $-(h-1)A$. Sumándolos:

$$= [2h - (h-1)] \, A - h \, \text{Id}$$

> **¿Qué hago acá?** Saco $A$ como factor común de los dos primeros términos.

**Paso 8 — Simplificar el coeficiente de $A$.**

$$2h - (h-1) = 2h - h + 1 = h + 1$$

Así que:

$$= (h+1) A - h \, \text{Id} \quad \checkmark$$

#### Conclusión

Coincide exactamente con la tesis de la PARTE C. Por inducción, la fórmula vale para todo $n \geq 1$. $\blacksquare$

> **Idea central:** el paso 5 (reemplazar $A^2$ por $2A - \text{Id}$) es lo que hace que la inducción funcione. Sin esa hipótesis no se podría reducir la potencia.

### G.3 — Inducción para $A^n$ con $A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$ (ejercicio V.4)

> **Cómo leer esta demo (en una frase):** misma estructura de inducción que G.1, pero con matriz $3 \times 3$. La entrada conflictiva es la $(1,3)$ porque ahí aparece la fórmula $\frac{n(n+1)}{2}$, y hay que verificar que siga valiendo cuando pasamos de $h$ a $h+1$.

**Hipótesis sobre $A$:** $A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$ (triangular superior con unos).

**Tesis:** Para todo $n \geq 1$:

$$A^n = \begin{pmatrix} 1 & n & \frac{n(n+1)}{2} \\ 0 & 1 & n \\ 0 & 0 & 1 \end{pmatrix}$$

> **¿Cómo se interpreta la fórmula?** En $A^n$, la entrada $(1,2)$ es $n$, la entrada $(1,3)$ es $\frac{n(n+1)}{2}$ (que para $n = 5$ es $\frac{5 \cdot 6}{2} = 15$), la entrada $(2,3)$ es $n$, y los unos/ceros se mantienen.

**Demostración por inducción paso a paso:**

#### PARTE A — Base ($n = 1$)

Para $n = 1$, la fórmula da:

$$\begin{pmatrix} 1 & 1 & \frac{1 \cdot 2}{2} \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix} = A \;\;\checkmark$$

> **Verificación:** $\frac{1 \cdot 2}{2} = 1$. La fórmula coincide con $A$ para $n = 1$.

#### PARTE B — Hipótesis inductiva ($n = h$)

Asumimos:

$$A^h = \begin{pmatrix} 1 & h & \frac{h(h+1)}{2} \\ 0 & 1 & h \\ 0 & 0 & 1 \end{pmatrix}$$

#### PARTE C — Tesis ($n = h+1$)

Queremos probar:

$$A^{h+1} = \begin{pmatrix} 1 & h+1 & \frac{(h+1)(h+2)}{2} \\ 0 & 1 & h+1 \\ 0 & 0 & 1 \end{pmatrix}$$

#### PARTE D — Paso inductivo

**Paso 1 — Reescribir $A^{h+1}$ como $A^h \cdot A$:**

$$A^{h+1} = A^h \cdot A = \begin{pmatrix} 1 & h & \frac{h(h+1)}{2} \\ 0 & 1 & h \\ 0 & 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$$

**Paso 2 — Calcular la matriz producto entrada por entrada.** Aplico fila × columna en cada una de las 9 entradas:

- $(1,1)$: $1 \cdot 1 + h \cdot 0 + \frac{h(h+1)}{2} \cdot 0 = 1$
- $(1,2)$: $1 \cdot 1 + h \cdot 1 + \frac{h(h+1)}{2} \cdot 0 = 1 + h = h + 1$
- $(1,3)$: $1 \cdot 1 + h \cdot 1 + \frac{h(h+1)}{2} \cdot 1 = 1 + h + \frac{h(h+1)}{2}$ ← **acá hay que trabajar más**
- $(2,1)$: $0$
- $(2,2)$: $0 \cdot 1 + 1 \cdot 1 + h \cdot 0 = 1$
- $(2,3)$: $0 \cdot 1 + 1 \cdot 1 + h \cdot 1 = 1 + h = h + 1$
- $(3,1) = (3,2) = 0$, $(3,3) = 1$.

**Paso 3 — Trabajar la entrada $(1,3)$.** Necesitamos llegar a $\frac{(h+1)(h+2)}{2}$.

Partimos de:

$$1 + h + \frac{h(h+1)}{2}$$

Sacamos denominador común $2$:

$$= \frac{2 + 2h + h(h+1)}{2}$$

> **¿Qué hice?** Multipliqué $1$ y $h$ por $\frac{2}{2}$ para que tengan denominador $2$. Eso me deja todo en una sola fracción.

Expandimos $h(h+1)$:

$$= \frac{2 + 2h + h^2 + h}{2}$$

Agrupamos términos:

$$= \frac{h^2 + 3h + 2}{2}$$

> **¿Es esa la fórmula que queremos?** Veamos. $(h+1)(h+2) = h^2 + 2h + h + 2 = h^2 + 3h + 2$. ¡Sí! Entonces:

$$= \frac{(h+1)(h+2)}{2} \;\;\checkmark$$

**Paso 4 — Armar la matriz resultante.**

$$A^{h+1} = \begin{pmatrix} 1 & h+1 & \frac{(h+1)(h+2)}{2} \\ 0 & 1 & h+1 \\ 0 & 0 & 1 \end{pmatrix}$$

Coincide con la tesis (PARTE C). ✓

#### Conclusión

Por inducción, la fórmula vale para todo $n \geq 1$. $\blacksquare$

> **Idea central:** la entrada $(1,3)$ es la única "no trivial". Las otras 8 son cálculos directos. Todo el trabajo algebraico está en simplificar $1 + h + \frac{h(h+1)}{2}$ hasta llegar a $\frac{(h+1)(h+2)}{2}$.

### G.4 — $A^k$ para matriz diagonal

> **Cómo leer esta demo (en una frase):** elevar una matriz diagonal a la $k$ es tan fácil como elevar cada entrada de la diagonal a la $k$. Probamos por inducción.

**Hipótesis:** $A = \text{diag}(d_1, d_2, \ldots, d_n)$ — una matriz diagonal con elementos $d_1, \ldots, d_n$ en la diagonal y ceros afuera.

**Tesis:** Para todo $k \geq 1$:

$$A^k = \text{diag}(d_1^k, d_2^k, \ldots, d_n^k)$$

> **Ejemplo concreto:** si $A = \text{diag}(2, 3, 5)$, entonces $A^2 = \text{diag}(4, 9, 25)$, $A^3 = \text{diag}(8, 27, 125)$, etc.

**Demostración por inducción:**

#### Base ($k = 1$)

$A^1 = A = \text{diag}(d_1, d_2, \ldots, d_n)$. Y $d_i^1 = d_i$, así que coincide. ✓

#### Hipótesis ($k = h$)

$$A^h = \text{diag}(d_1^h, d_2^h, \ldots, d_n^h)$$

#### Paso inductivo ($k = h+1$)

**Paso 1 — Escribir $A^{h+1} = A^h \cdot A$.**

$$A^{h+1} = A^h \cdot A = \text{diag}(d_1^h, \ldots, d_n^h) \cdot \text{diag}(d_1, \ldots, d_n)$$

**Paso 2 — Multiplicar dos matrices diagonales.** Cuando multiplicás dos matrices diagonales, el resultado es diagonal — y cada entrada de la diagonal del resultado es el producto de las entradas correspondientes:

$$\text{diag}(a_1, \ldots, a_n) \cdot \text{diag}(b_1, \ldots, b_n) = \text{diag}(a_1 b_1, \ldots, a_n b_n)$$

> **¿Por qué?** Porque al hacer "fila × columna" en posiciones de la diagonal, solo sobrevive el término donde ambos factores son no-cero. Las demás entradas dan cero por la estructura de las diagonales.

Aplicado:

$$A^{h+1} = \text{diag}(d_1^h \cdot d_1, d_2^h \cdot d_2, \ldots, d_n^h \cdot d_n)$$

**Paso 3 — Simplificar cada entrada.** $d_i^h \cdot d_i = d_i^{h+1}$:

$$= \text{diag}(d_1^{h+1}, d_2^{h+1}, \ldots, d_n^{h+1}) \;\;\checkmark$$

#### Conclusión

Coincide con la tesis para $k = h+1$. Por inducción, vale para todo $k \geq 1$. $\blacksquare$

> **Idea central:** las matrices diagonales se comportan "componente por componente" — y elevarlas a una potencia es solo elevar cada componente.

### G.4 — $A^k$ para matriz diagonal

**Hipótesis:** $A = \text{diag}(d_1, d_2, \ldots, d_n)$.

**Tesis:** Para todo $k \geq 1$, $A^k = \text{diag}(d_1^k, d_2^k, \ldots, d_n^k)$.

**Base ($k = 1$):** trivial. ✓

**Hipótesis ($k = h$):** $A^h = \text{diag}(d_1^h, \ldots, d_n^h)$.

**Paso inductivo:** el producto de dos diagonales es diagonal con entradas multiplicadas:

$$A^{h+1} = A^h \cdot A = \text{diag}(d_1^h \cdot d_1, \ldots, d_n^h \cdot d_n) = \text{diag}(d_1^{h+1}, \ldots, d_n^{h+1}) \;\;\checkmark$$

$\blacksquare$

---

## H. Factorización para hallar inversa

### H.1 — $A^3 - A = \text{Id} \Rightarrow A^{-1} = A^2 - \text{Id}$

> **Cómo leer esta demo (en una frase):** factorizamos la ecuación hasta que quede en la forma $A \cdot (\text{algo}) = \text{Id}$. Cuando logramos esa forma, ese "algo" es por definición $A^{-1}$.

**Hipótesis:** $A$ cuadrada satisface $A^3 - A = \text{Id}$.

**Tesis:** $A$ es invertible **y** $A^{-1} = A^2 - \text{Id}$.

> **Estrategia general:** la idea es transformar la ecuación dada hasta que aparezca un producto $A \cdot X = \text{Id}$. Si lo logramos, automáticamente $X$ es la inversa de $A$.

**Demostración paso a paso:**

**Paso 1 — Empezar de la hipótesis.**

$$A^3 - A = \text{Id}$$

**Paso 2 — Reescribir $A^3$ y $A$ para que aparezca un factor común.** Quiero que ambos términos del lado izquierdo tengan $A$ "afuera":

$$A^3 = A \cdot A^2 \qquad\text{(definición de potencia)}$$

$$A = A \cdot \text{Id} \qquad\text{(neutro del producto)}$$

Sustituyendo:

$$A \cdot A^2 - A \cdot \text{Id} = \text{Id}$$

> **¿Por qué reescribo $A$ como $A \cdot \text{Id}$?** Para que ambos términos del lado izquierdo empiecen con $A$. Esto me permite usar la propiedad distributiva al revés (sacar factor común).

**Paso 3 — Sacar $A$ como factor común a izquierda.** Por la propiedad distributiva: $A \cdot X - A \cdot Y = A \cdot (X - Y)$:

$$A \cdot (A^2 - \text{Id}) = \text{Id}$$

> **¿Qué pasó?** Junté los dos términos del lado izquierdo en un solo producto, donde $A$ multiplica a $(A^2 - \text{Id})$.
>
> **Cuidado:** el factor común tiene que estar del MISMO lado en ambos términos para poder sacarlo. Acá $A$ estaba a izquierda en los dos. Si hubiera estado a izquierda en uno y a derecha en otro, no se podría factorizar así (porque las matrices no conmutan).

**Paso 4 — Reconocer la forma "matriz por algo igual a Id".** Tenemos:

$$A \cdot (A^2 - \text{Id}) = \text{Id}$$

Esto dice exactamente que **$A$ tiene una inversa** (porque encontramos una matriz, $A^2 - \text{Id}$, que multiplicada por $A$ a derecha da $\text{Id}$). Por definición de inversa:

$$A^{-1} = A^2 - \text{Id} \quad \blacksquare$$

> **Idea central:** este es el método universal para encontrar inversas a partir de ecuaciones polinomiales. Siempre que veas algo de la forma "$P(A) = \text{Id}$" con $P$ un polinomio que tiene $A$ como factor, podés despejar $A^{-1}$.
>
> **Aclaración técnica:** verificamos $A \cdot (A^2 - \text{Id}) = \text{Id}$ pero no $(A^2 - \text{Id}) \cdot A = \text{Id}$. Para matrices cuadradas, se puede probar (por unicidad) que si $XY = \text{Id}$ con $X, Y$ cuadradas de la misma dimensión, automáticamente también $YX = \text{Id}$. Por eso alcanza con un lado.

### H.2 — $A^3 = \mathcal{O} \Rightarrow (A + \text{Id})^{-1} = A^2 - A + \text{Id}$ (ejercicio VI.3)

> **Cómo leer esta demo (en una frase):** queremos probar que $A^2 - A + \text{Id}$ es la inversa de $A + \text{Id}$. Hacemos el producto, distribuimos, los términos del medio se cancelan, queda $A^3 + \text{Id}$, y como $A^3 = \mathcal{O}$ por hipótesis, queda $\text{Id}$. Eso prueba que es la inversa.

**Hipótesis:** $A^3 = \mathcal{O}$ (la matriz nula).

> **¿Qué quiere decir esa hipótesis?** Que multiplicar $A$ por sí misma 3 veces da la matriz cero. $A$ es **nilpotente** de grado $\leq 3$.

**Tesis:** $A + \text{Id}$ es invertible **y** su inversa es $A^2 - A + \text{Id}$.

> **Estrategia:** lo mismo que en E.2. Para probar que $X$ es la inversa de $Y$, multiplicamos $Y \cdot X$ y mostramos que da $\text{Id}$. Acá $Y = A + \text{Id}$ y $X = A^2 - A + \text{Id}$.

**Demostración paso a paso:**

**Paso 1 — Plantear el producto.** Multiplicamos $(A + \text{Id})$ por $(A^2 - A + \text{Id})$:

$$(A + \text{Id})(A^2 - A + \text{Id})$$

**Paso 2 — Distribuir todos los términos.** Hay que multiplicar cada término del primer paréntesis con cada término del segundo. Son 2 términos × 3 términos = 6 productos:

$$= A \cdot A^2 + A \cdot (-A) + A \cdot \text{Id} + \text{Id} \cdot A^2 + \text{Id} \cdot (-A) + \text{Id} \cdot \text{Id}$$

> **¿Por qué puedo distribuir?** El producto de matrices ES distributivo sobre la suma — esa es una de las propiedades del producto. Por eso puedo "abrir" los paréntesis.
>
> **Cuidado:** $A$ y $\text{Id}$ siempre conmutan, por eso no me preocupo del orden con $\text{Id}$. Pero si fueran dos matrices distintas, el orden importaría.

**Paso 3 — Simplificar cada producto.**

- $A \cdot A^2 = A^3$
- $A \cdot (-A) = -A^2$
- $A \cdot \text{Id} = A$
- $\text{Id} \cdot A^2 = A^2$
- $\text{Id} \cdot (-A) = -A$
- $\text{Id} \cdot \text{Id} = \text{Id}$

Reescribiendo todo:

$$= A^3 - A^2 + A + A^2 - A + \text{Id}$$

> **¿Por qué puedo simplificar así?** Porque $\text{Id}$ es el neutro del producto — multiplicar por $\text{Id}$ no cambia nada.

**Paso 4 — Agrupar términos que se cancelan.** Mirá los términos: $-A^2 + A^2 = \mathcal{O}$ y $A - A = \mathcal{O}$. Esos se anulan:

$$= A^3 + \underbrace{(-A^2 + A^2)}_{=\mathcal{O}} + \underbrace{(A - A)}_{=\mathcal{O}} + \text{Id}$$

$$= A^3 + \text{Id}$$

> **¿Qué pasó?** Los 4 términos del medio se cancelaron en pares. Solo sobreviven el primero ($A^3$) y el último ($\text{Id}$).

**Paso 5 — Aplicar la hipótesis.** Como $A^3 = \mathcal{O}$:

$$= \mathcal{O} + \text{Id} = \text{Id}$$

**Conclusión.** Verificamos que $(A + \text{Id})(A^2 - A + \text{Id}) = \text{Id}$. Por definición de inversa:

$$A + \text{Id} \text{ es invertible y } (A + \text{Id})^{-1} = A^2 - A + \text{Id} \quad \blacksquare$$

> **Truco mnemotécnico:** este es el caso matricial de la identidad polinomial conocida $(x+1)(x^2 - x + 1) = x^3 + 1$. Si $x = A$, entonces $A^3 + 1 = A^3 + \text{Id}$. Si encima $A^3 = \mathcal{O}$, eso da $\text{Id}$. Cuando veas estructuras así en parcial, pensá en factorizaciones de polinomios conocidas.
>
> **Idea central:** $A^3 = \mathcal{O}$ es lo que hace que el primer término "desaparezca" y permite que el resto colapse a $\text{Id}$. Sin esa hipótesis la fórmula no funciona.

---

## I. Otros del práctico

### I.1 — V.11: Ley de simplificación a izquierda

> **Cómo leer esta demo (en una frase):** "cancelar un $A$" en una ecuación matricial NO es como cancelar números — hay que multiplicar por $A^{-1}$ del mismo lado en ambos miembros. El truco solo funciona si $A$ es invertible.

**Enunciado:** Si $A$ es invertible y $AB = AC$, entonces $B = C$.

**Hipótesis:** $A$ invertible; $AB = AC$.

**Tesis:** $B = C$.

**Demostración paso a paso:**

**Paso 1 — Empezar de la igualdad dada.**

$$AB = AC$$

**Paso 2 — Multiplicar por $A^{-1}$ a izquierda en ambos lados.** Como $A$ es invertible, existe $A^{-1}$. En una igualdad puedo multiplicar ambos lados por la misma cosa, del mismo lado, sin perder la igualdad:

$$A^{-1} \cdot (AB) = A^{-1} \cdot (AC)$$

> **¿Por qué a izquierda y no a derecha?** Porque la $A$ está a izquierda de $B$ y de $C$. Para "cancelarla", $A^{-1}$ tiene que ir del mismo lado que $A$, o sea a izquierda.
>
> **¿Por qué multiplico por la izquierda en AMBOS lados?** Porque si solo multiplicara en uno, la igualdad se rompería. Es la regla básica de operar con ecuaciones: lo que hago de un lado lo hago del otro.

**Paso 3 — Reagrupar usando asociativa.** Muevo los paréntesis para juntar $A^{-1}$ con $A$:

$$(A^{-1} \cdot A) \cdot B = (A^{-1} \cdot A) \cdot C$$

**Paso 4 — Aplicar $A^{-1} \cdot A = \text{Id}$.**

$$\text{Id} \cdot B = \text{Id} \cdot C$$

**Paso 5 — Aplicar $\text{Id} \cdot M = M$ (neutro del producto).**

$$B = C \quad \blacksquare$$

> **Idea central:** "cancelar" en matrices es siempre "multiplicar por la inversa del mismo lado". No se "pasa restando" ni "dividiendo" como con números.
>
> ⚠️ **CUIDADO — esto NO vale si $A$ no es invertible.** Contraejemplo (V.11.3):
>
> $$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \quad C = \begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix}$$
>
> Verificás que $AB = AC = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ pero $B \neq C$. La diferencia: esta $A$ NO es invertible (su determinante da $0$), por eso falla la "cancelación".

### I.2 — V.14: $A, B$ invertibles $\Rightarrow AB$ invertible (con su inversa explícita)

**Hipótesis:** $A, B$ invertibles.

**Tesis:** $AB$ es invertible y $(AB)^{-1} = B^{-1} A^{-1}$.

**Demostración:** ya hecha en §E.2. $\blacksquare$

> **Contraparte:** $A + B$ NO necesariamente invertible. Contraejemplo: $A = \text{Id}$, $B = -\text{Id}$. Ambas son invertibles pero $A + B = \mathcal{O}$ no lo es.

### I.3 — V.15: Si $AB = BA$ y $AC = CA$, entonces $A$ conmuta con $\mu B + \lambda C$

**Hipótesis:** $AB = BA$, $AC = CA$, $\mu, \lambda \in \mathbb{R}$.

**Tesis:** $A$ conmuta con $D = \mu B + \lambda C$, es decir $AD = DA$.

**Demostración:**

$$A \cdot D = A \cdot (\mu B + \lambda C) \quad \text{(definición de }D\text{)}$$

$$= \mu (AB) + \lambda (AC) \quad \text{(distributiva + escalar entre factores)}$$

$$= \mu (BA) + \lambda (CA) \quad \text{(hipótesis: }AB = BA\text{, }AC = CA\text{)}$$

$$= (\mu B + \lambda C) \cdot A \quad \text{(distributiva)}$$

$$= D \cdot A \quad \blacksquare$$

---

## Cómo usar este banco para estudiar

| Si tenés... | Hacé esto |
|-------------|-----------|
| 30 minutos antes del parcial | Revisá las demos **D.6, E.2, F.1, C.3** (las más probables) |
| Una hora | Sumá **B.4** (traspuesta del producto) y **H.1, H.2** (factorización) |
| Más tiempo | Hacé todas las inducciones **G.1–G.4** una vez sin mirar |
| Querés sentirte seguro | Reescribí cada demo desde cero solo viendo la tesis. Si lo lográs, dominás el módulo |

---

## Reglas que el profesor pidió en parcial sobre demos

| Regla | Por qué |
|-------|---------|
| Escribir **hipótesis** y **tesis** explícitamente | Estructura mínima esperada |
| Justificar cada paso citando la propiedad usada | *"En los parciales se pide justificar las propiedades que aplican"* (clase 2) |
| No hace falta el **número** de la propiedad — describirla con palabras | *"Lo que importa es saber aplicarla y aclarar qué propiedad estás aplicando"* (clase 5) |
| Cerrar con $\blacksquare$ o "L.Q.Q.D." o "queda demostrado" | Cierre formal |
| **Nunca asumir $AB = BA$** salvo hipótesis explícita | Es el error #1 que el prof flageó: *"lo veo siempre en los parciales"* |
