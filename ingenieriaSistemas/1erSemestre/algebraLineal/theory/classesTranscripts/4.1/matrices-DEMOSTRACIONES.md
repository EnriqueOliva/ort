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

**Hipótesis:** $A \in \mathcal{M}_{n \times n}$ y $\vec{v}_j$ es el vector canónico (columna con un $1$ en la posición $j$ y $0$ en el resto).

**Tesis:** $A \cdot \vec{v}_j$ = columna $j$ de $A$.

**Demostración:**

Sea $A = ((a_{ik}))$ y $\vec{v}_j$ con componentes $v_k = 1$ si $k = j$, $v_k = 0$ si $k \neq j$.

La fila $i$ del producto es:

$$(A \cdot \vec{v}_j)_i = \sum_{k=1}^{n} a_{ik} \cdot v_k \quad \text{(definición de producto fila}\times\text{columna)}$$

$$= a_{ij} \cdot 1 + \sum_{k \neq j} a_{ik} \cdot 0 = a_{ij} \quad \text{(porque }v_k = 0\text{ salvo en }k=j\text{)}$$

Como esto vale para toda fila $i$, el resultado es la columna $j$ de $A$. $\blacksquare$

> Ejemplo numérico desarrollado: ver `matrices-para-PARCIAL.md` PARTE 3 — sección "Producto por vectores canónicos".

---

## B. Traspuesta

### B.1 — Propiedad 1: $(A^T)^T = A$

**Hipótesis:** $A = ((a_{ij})) \in \mathcal{M}_{m \times n}$.

**Tesis:** $(A^T)^T = A$.

**Demostración:**

$$A^T = ((a_{ji})) \quad \text{(definición de traspuesta: intercambiar }i\text{ con }j\text{)}$$

Aplicando traspuesta otra vez, intercambiamos los subíndices de nuevo:

$$(A^T)^T = ((a_{ij})) = A \quad \blacksquare$$

### B.2 — Propiedad 2: $(A + B)^T = A^T + B^T$

**Hipótesis:** $A, B \in \mathcal{M}_{m \times n}$.

**Tesis:** $(A + B)^T = A^T + B^T$.

**Demostración:**

$$[A + B]^T = [((a_{ij})) + ((b_{ij}))]^T \quad \text{(definir }A, B\text{ por entradas)}$$

$$= [((a_{ij} + b_{ij}))]^T \quad \text{(definición de suma entrada por entrada)}$$

$$= ((a_{ji} + b_{ji})) \quad \text{(definición de traspuesta)}$$

$$= ((a_{ji})) + ((b_{ji})) \quad \text{(separar la suma)}$$

$$= A^T + B^T \quad \blacksquare$$

### B.3 — Propiedad 3: $(\alpha \cdot A)^T = \alpha \cdot A^T$

**Hipótesis:** $A \in \mathcal{M}_{m \times n}$, $\alpha \in \mathbb{R}$.

**Tesis:** $(\alpha A)^T = \alpha A^T$.

**Demostración:**

$$(\alpha A)^T = ((\alpha \cdot a_{ij}))^T \quad \text{(definición de producto por escalar)}$$

$$= ((\alpha \cdot a_{ji})) \quad \text{(definición de traspuesta)}$$

$$= \alpha \cdot ((a_{ji})) \quad \text{(sacar }\alpha\text{ como factor común)}$$

$$= \alpha \cdot A^T \quad \blacksquare$$

> **Error común:** escribir $(\alpha A)^T = \alpha^T A^T$. Los escalares no se trasponen.

### B.4 — Propiedad 4: $(A \cdot B)^T = B^T \cdot A^T$ (orden invertido)

**Hipótesis:** $A \in \mathcal{M}_{m \times n}$, $B \in \mathcal{M}_{n \times p}$ (conformables).

**Tesis:** $(AB)^T = B^T A^T$.

**Demostración:**

Sea $C = AB$, con $c_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj}$.

La entrada $(i, j)$ de $C^T$ es la entrada $(j, i)$ de $C$:

$$(C^T)_{ij} = c_{ji} = \sum_{k=1}^{n} a_{jk} \cdot b_{ki}$$

Ahora la entrada $(i, j)$ de $B^T A^T$, sabiendo $(B^T)_{ik} = b_{ki}$ y $(A^T)_{kj} = a_{jk}$:

$$(B^T A^T)_{ij} = \sum_{k=1}^{n} b_{ki} \cdot a_{jk} = \sum_{k=1}^{n} a_{jk} \cdot b_{ki}$$

(números reales conmutan dentro de la suma)

Comparando: $(C^T)_{ij} = (B^T A^T)_{ij}$ para todo $i, j$. Entonces $C^T = B^T A^T$, o sea $(AB)^T = B^T A^T$. $\blacksquare$

> **Error común:** escribir $(AB)^T = A^T B^T$. **El orden se invierte** porque las matrices no conmutan, y porque las dimensiones ni siquiera dejan en general.

---

## C. Simétrica y antisimétrica

### C.1 — Suma de simétricas es simétrica

**Hipótesis:** $A, B$ simétricas: $A^T = A$, $B^T = B$.

**Tesis:** $A + B$ es simétrica.

**Demostración:**

$$(A + B)^T = A^T + B^T \quad \text{(propiedad 2 de traspuesta, §B.2)}$$

$$= A + B \quad \text{(hipótesis: }A, B\text{ simétricas)}$$

Como $(A+B)^T = A+B$, entonces $A+B$ es simétrica. $\blacksquare$

> **Análoga:** la suma de antisimétricas es antisimétrica. Demostración igual pero usando que $A^T = -A$ y $B^T = -B$, y termina en $-(A+B)$.

### C.2 — $\alpha \cdot A$ es simétrica si $A$ es simétrica

**Hipótesis:** $A$ simétrica ($A^T = A$); $\alpha \in \mathbb{R}$.

**Tesis:** $\alpha A$ es simétrica.

**Demostración:**

$$(\alpha A)^T = \alpha \cdot A^T \quad \text{(propiedad 3 de traspuesta, §B.3)}$$

$$= \alpha \cdot A \quad \text{(hipótesis: }A\text{ simétrica)}$$

Como $(\alpha A)^T = \alpha A$, $\alpha A$ es simétrica. $\blacksquare$

> **Análoga:** si $A$ es antisimétrica ($A^T = -A$), entonces $(\alpha A)^T = \alpha A^T = \alpha(-A) = -(\alpha A)$, así que $\alpha A$ es antisimétrica.

### C.3 — $AB$ simétrica $\iff AB = BA$ (con $A, B$ simétricas)

**Hipótesis:** $A^T = A$ y $B^T = B$.

**Tesis:** $AB$ simétrica $\iff AB = BA$.

> "$\iff$" pide probar las **dos direcciones**.

**Directo ($\Rightarrow$):** asumimos $AB$ simétrica, queremos $AB = BA$.

$$AB = (AB)^T \quad \text{(hipótesis: }AB\text{ simétrica)}$$

$$= B^T A^T \quad \text{(propiedad 4 de traspuesta, §B.4)}$$

$$= B \cdot A \quad \text{(hipótesis: }A, B\text{ simétricas)}$$

Entonces $AB = BA$. ✓

**Recíproco ($\Leftarrow$):** asumimos $AB = BA$, queremos $AB$ simétrica.

$$(AB)^T = B^T A^T \quad \text{(propiedad 4 de traspuesta)}$$

$$= B \cdot A \quad \text{(hipótesis: }A, B\text{ simétricas)}$$

$$= A \cdot B \quad \text{(hipótesis: }AB = BA\text{)}$$

Entonces $(AB)^T = AB$, o sea $AB$ es simétrica. ✓

Probadas ambas direcciones. $\blacksquare$

### C.4 — $\frac{1}{2}(A + A^T)$ es simétrica

**Hipótesis:** $A$ matriz cuadrada cualquiera.

**Tesis:** $S = \frac{1}{2}(A + A^T)$ es simétrica.

**Demostración:**

$$S^T = \left[\tfrac{1}{2}(A + A^T)\right]^T = \tfrac{1}{2}(A + A^T)^T \quad \text{(propiedad 3 de traspuesta: el escalar sale)}$$

$$= \tfrac{1}{2}\left(A^T + (A^T)^T\right) \quad \text{(propiedad 2 de traspuesta)}$$

$$= \tfrac{1}{2}(A^T + A) \quad \text{(propiedad 1: }(A^T)^T = A\text{)}$$

$$= \tfrac{1}{2}(A + A^T) \quad \text{(conmutativa de la suma)}$$

$$= S$$

Como $S^T = S$, $S$ es simétrica. $\blacksquare$

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

**Hipótesis:** $A, B \in \mathcal{M}_{n \times n}$.

**Tesis:** $tr(A+B) = tr(A) + tr(B)$.

**Demostración:**

$$tr(A + B) = \sum_{i=1}^{n} (A + B)_{ii} \quad \text{(definición de traza)}$$

$$= \sum_{i=1}^{n} (a_{ii} + b_{ii}) \quad \text{(definición de suma)}$$

$$= \sum_{i=1}^{n} a_{ii} + \sum_{i=1}^{n} b_{ii} \quad \text{(separar la sumatoria)}$$

$$= tr(A) + tr(B) \quad \blacksquare$$

### D.2 — Propiedad 2: $tr(\alpha A) = \alpha \cdot tr(A)$

**Hipótesis:** $A \in \mathcal{M}_{n \times n}$, $\alpha \in \mathbb{R}$.

**Tesis:** $tr(\alpha A) = \alpha \cdot tr(A)$.

**Demostración:**

$$tr(\alpha A) = \sum_{i=1}^{n} (\alpha A)_{ii} = \sum_{i=1}^{n} \alpha \cdot a_{ii} = \alpha \cdot \sum_{i=1}^{n} a_{ii} = \alpha \cdot tr(A) \quad \blacksquare$$

### D.3 — Propiedad 3: $tr(A^T) = tr(A)$

**Hipótesis:** $A \in \mathcal{M}_{n \times n}$.

**Tesis:** $tr(A^T) = tr(A)$.

**Demostración:**

La diagonal principal de $A$ son los $a_{ii}$ con $i = 1, \ldots, n$. Al trasponer, la entrada $(i,i)$ pasa a la posición $(i,i)$ — es decir, **la diagonal no cambia**:

$$(A^T)_{ii} = a_{ii} \quad \text{(definición de traspuesta: }(M^T)_{ij} = M_{ji}\text{; con }i = j\text{ es lo mismo)}$$

Por lo tanto:

$$tr(A^T) = \sum_{i=1}^{n} (A^T)_{ii} = \sum_{i=1}^{n} a_{ii} = tr(A) \quad \blacksquare$$

### D.4 — Propiedad 4: $tr(AB) = tr(BA)$

**Hipótesis:** $A, B \in \mathcal{M}_{n \times n}$.

**Tesis:** $tr(AB) = tr(BA)$.

**Demostración:**

Por definición de producto, $(AB)_{ii} = \sum_{k=1}^{n} a_{ik} \cdot b_{ki}$. Entonces:

$$tr(AB) = \sum_{i=1}^{n} (AB)_{ii} = \sum_{i=1}^{n} \sum_{k=1}^{n} a_{ik} \cdot b_{ki}$$

Intercambiamos el orden de las dos sumatorias (vale porque son finitas) y renombramos los índices ($i \leftrightarrow k$ para mayor claridad):

$$= \sum_{k=1}^{n} \sum_{i=1}^{n} b_{ki} \cdot a_{ik} = \sum_{k=1}^{n} \sum_{i=1}^{n} b_{ki} \cdot a_{ik}$$

Por definición, $(BA)_{kk} = \sum_{i=1}^{n} b_{ki} \cdot a_{ik}$, así que la suma anterior es:

$$= \sum_{k=1}^{n} (BA)_{kk} = tr(BA) \quad \blacksquare$$

> **Notable:** esto vale aunque $AB \neq BA$. Las dos matrices son distintas, pero sus diagonales suman lo mismo.

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

**Tesis:** No existen matrices cuadradas $A, B$ tales que $AB - BA = \text{Id}$.

**Demostración por absurdo:** supongamos que sí existen. Entonces:

$$AB - BA = \text{Id}$$

Tomamos traza a ambos lados:

$$tr(AB - BA) = tr(\text{Id})$$

**Lado izquierdo:**

$$tr(AB - BA) = tr(AB) - tr(BA) \quad \text{(corolario §D.5)}$$

$$= tr(AB) - tr(AB) \quad \text{(propiedad 4, §D.4)}$$

$$= 0$$

**Lado derecho:**

$$tr(\text{Id}) = \underbrace{1 + 1 + \cdots + 1}_{n \text{ veces}} = n$$

Igualando: $0 = n$. Como $n \geq 1$, esto es **absurdo**. Por lo tanto, no pueden existir $A, B$ con $AB - BA = \text{Id}$. $\blacksquare$

---

## E. Inversa

### E.1 — Propiedad 1: $(A^{-1})^{-1} = A$

**Hipótesis:** $A$ invertible.

**Tesis:** $A^{-1}$ es invertible y su inversa es $A$, o sea $(A^{-1})^{-1} = A$.

**Demostración:** por definición de inversa, $A^{-1} \cdot A = \text{Id}$ y $A \cdot A^{-1} = \text{Id}$.

Esto mismo dice que **$A$ funciona como inversa de $A^{-1}$**: existe una matriz (a saber, $A$) tal que multiplicada por $A^{-1}$ da $\text{Id}$. Por unicidad de la inversa:

$$(A^{-1})^{-1} = A \quad \blacksquare$$

### E.2 — Propiedad 2: $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$ (orden invertido)

**Hipótesis:** $A, B$ invertibles, mismas dimensiones $n \times n$.

**Tesis:** $(AB)^{-1} = B^{-1} A^{-1}$.

**Estrategia:** para probar que $X$ es la inversa de $Y$, basta verificar $Y \cdot X = \text{Id}$ (por unicidad).

**Demostración:** verificamos $(AB) \cdot (B^{-1} A^{-1}) = \text{Id}$.

$$(AB)(B^{-1} A^{-1}) = A \cdot (B \cdot B^{-1}) \cdot A^{-1} \quad \text{(asociativa)}$$

$$= A \cdot \text{Id} \cdot A^{-1} \quad \text{(definición de inversa: }B \cdot B^{-1} = \text{Id}\text{)}$$

$$= A \cdot A^{-1} \quad \text{(neutro: }M \cdot \text{Id} = M\text{)}$$

$$= \text{Id} \quad \text{(definición de inversa)}$$

Entonces $B^{-1} A^{-1}$ es la inversa de $AB$, es decir $(AB)^{-1} = B^{-1} A^{-1}$. $\blacksquare$

> **Analogía:** si te ponés medias y después zapatos, para sacarlos hacés el orden inverso — primero zapatos, después medias. Lo último que entra es lo primero que sale.

### E.3 — Propiedad 3: $(\alpha A)^{-1} = \frac{1}{\alpha} A^{-1}$, $\alpha \neq 0$

**Hipótesis:** $A$ invertible, $\alpha \neq 0$.

**Tesis:** $(\alpha A)^{-1} = \frac{1}{\alpha} A^{-1}$.

**Demostración:** verificamos $(\alpha A) \cdot \left(\frac{1}{\alpha} A^{-1}\right) = \text{Id}$.

$$(\alpha A) \cdot \left(\tfrac{1}{\alpha} A^{-1}\right) = \alpha \cdot \tfrac{1}{\alpha} \cdot (A \cdot A^{-1}) \quad \text{(escalares conmutan; agrupar)}$$

$$= 1 \cdot \text{Id} \quad \text{(}\alpha \cdot \frac{1}{\alpha} = 1\text{; definición de inversa)}$$

$$= \text{Id}$$

Entonces $\frac{1}{\alpha} A^{-1}$ es la inversa de $\alpha A$. $\blacksquare$

### E.4 — Propiedad 4: $(A^T)^{-1} = (A^{-1})^T$

**Hipótesis:** $A$ invertible.

**Tesis:** $A^T$ es invertible y $(A^T)^{-1} = (A^{-1})^T$.

**Demostración:** verificamos $A^T \cdot (A^{-1})^T = \text{Id}$.

$$A^T \cdot (A^{-1})^T = (A^{-1} \cdot A)^T \quad \text{(propiedad 4 de traspuesta usada al revés: }X^T Y^T = (YX)^T\text{)}$$

$$= \text{Id}^T \quad \text{(definición de inversa)}$$

$$= \text{Id} \quad \text{(la identidad es simétrica)}$$

Entonces $(A^{-1})^T$ es la inversa de $A^T$, es decir $(A^T)^{-1} = (A^{-1})^T$. $\blacksquare$

---

## F. Idempotente y nilpotente

### F.1 — Idempotente $+$ invertible $\Rightarrow A = \text{Id}$ (ejercicio VI.2)

**Hipótesis:** $A^2 = A$ (idempotente) **y** $A$ invertible.

**Tesis:** $A = \text{Id}$.

**Demostración:** multiplicamos a izquierda por $A^{-1}$ en la igualdad de idempotencia.

$$A^2 = A$$

$$A^{-1} \cdot A^2 = A^{-1} \cdot A \quad \text{(multiplicar por }A^{-1}\text{ a izquierda)}$$

$$A^{-1} \cdot A \cdot A = A^{-1} \cdot A \quad \text{(reescribir }A^2 = A \cdot A\text{)}$$

$$\text{Id} \cdot A = \text{Id} \quad \text{(}A^{-1} A = \text{Id}\text{)}$$

$$A = \text{Id} \quad \blacksquare$$

> **Aclaración:** esto NO dice que toda idempotente sea $\text{Id}$. Solo cuando además es invertible. La nula y $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ son idempotentes y NO son $\text{Id}$ — pero tampoco son invertibles.

### F.2 — Si $A$ es idempotente, $(A + \text{Id})^3 = \text{Id} + 7A$

**Hipótesis:** $A^2 = A$ (lo que implica $A^k = A$ para todo $k \geq 1$).

**Tesis:** $(A + \text{Id})^3 = \text{Id} + 7A$.

**Demostración:** $A$ y $\text{Id}$ siempre conmutan, así que vale el binomio de Newton:

$$(A + \text{Id})^3 = A^3 + 3 A^2 \text{Id} + 3 A \text{Id}^2 + \text{Id}^3$$

$$= A^3 + 3 A^2 + 3 A + \text{Id} \quad \text{(}\text{Id}^k = \text{Id}\text{; multiplicar por }\text{Id}\text{ no cambia)}$$

$$= A + 3 A + 3 A + \text{Id} \quad \text{(hipótesis: }A^2 = A\text{ y por inducción }A^k = A\text{)}$$

$$= 7A + \text{Id} = \text{Id} + 7A \quad \blacksquare$$

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

**Tesis:** Para todo $n \geq 1$:

$$A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$$

**Base ($n = 1$):** $A^1 = A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, coincide con la fórmula tomando $n=1$. ✓

**Hipótesis inductiva ($n = h$):** $A^h = \begin{pmatrix} 1 & h \\ 0 & 1 \end{pmatrix}$.

**Tesis ($n = h+1$):** $A^{h+1} = \begin{pmatrix} 1 & h+1 \\ 0 & 1 \end{pmatrix}$.

**Paso inductivo:**

$$A^{h+1} = A^h \cdot A = \begin{pmatrix} 1 & h \\ 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

$$= \begin{pmatrix} 1\cdot1 + h\cdot0 & 1\cdot1 + h\cdot1 \\ 0\cdot1 + 1\cdot0 & 0\cdot1 + 1\cdot1 \end{pmatrix} = \begin{pmatrix} 1 & h+1 \\ 0 & 1 \end{pmatrix} \;\;\checkmark$$

Por inducción, vale para todo $n \geq 1$. $\blacksquare$

### G.2 — Inducción para $A^n$ con $A^2 = 2A - \text{Id}$ (ejercicio V.10.3)

**Hipótesis sobre $A$:** $A^2 = 2A - \text{Id}$.

**Tesis:** Para todo $n \geq 1$, $A^n = nA - (n-1)\text{Id}$.

**Base ($n = 1$):** $A^1 = A = 1 \cdot A - 0 \cdot \text{Id}$. ✓

**Hipótesis inductiva ($n = h$):** $A^h = hA - (h-1)\text{Id}$.

**Tesis ($n = h+1$):** $A^{h+1} = (h+1)A - h \cdot \text{Id}$.

**Paso inductivo:**

$$A^{h+1} = A^h \cdot A = [hA - (h-1)\text{Id}] \cdot A \quad \text{(hipótesis inductiva)}$$

$$= h A^2 - (h-1) A \quad \text{(distributiva; }\text{Id} \cdot A = A\text{)}$$

$$= h(2A - \text{Id}) - (h-1) A \quad \text{(hipótesis sobre }A^2\text{)}$$

$$= 2hA - h\,\text{Id} - (h-1)A = [2h - (h-1)]A - h \,\text{Id}$$

$$= (h+1)A - h \,\text{Id} \;\;\checkmark$$

Por inducción, vale para todo $n \geq 1$. $\blacksquare$

### G.3 — Inducción para $A^n$ con $A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$ (ejercicio V.4)

**Tesis:** Para todo $n \geq 1$:

$$A^n = \begin{pmatrix} 1 & n & \frac{n(n+1)}{2} \\ 0 & 1 & n \\ 0 & 0 & 1 \end{pmatrix}$$

**Base ($n = 1$):** $A^1 = A$. La fórmula da $\frac{1 \cdot 2}{2} = 1$ en posición $(1,3)$. ✓

**Hipótesis ($n = h$):** $A^h = \begin{pmatrix} 1 & h & \frac{h(h+1)}{2} \\ 0 & 1 & h \\ 0 & 0 & 1 \end{pmatrix}$.

**Paso inductivo:**

$$A^{h+1} = A^h \cdot A = \begin{pmatrix} 1 & h & \frac{h(h+1)}{2} \\ 0 & 1 & h \\ 0 & 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$$

La entrada crítica es $(1,3)$:

$$1 \cdot 1 + h \cdot 1 + \tfrac{h(h+1)}{2} \cdot 1 = 1 + h + \tfrac{h(h+1)}{2} = \tfrac{2 + 2h + h^2 + h}{2} = \tfrac{h^2 + 3h + 2}{2} = \tfrac{(h+1)(h+2)}{2} \;\;\checkmark$$

Las otras entradas dan $h+1$ en $(1,2)$ y $(2,3)$, y los unos/ceros se mantienen. La fórmula vale para $h+1$. $\blacksquare$

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

**Hipótesis:** $A$ cuadrada con $A^3 - A = \text{Id}$.

**Tesis:** $A$ es invertible y $A^{-1} = A^2 - \text{Id}$.

**Demostración:** factorizamos para que aparezca $A \cdot (\ldots) = \text{Id}$.

$$A^3 - A = \text{Id}$$

$$A \cdot A^2 - A \cdot \text{Id} = \text{Id} \quad \text{(reescribir }A^3 = A \cdot A^2\text{ y }A = A \cdot \text{Id}\text{)}$$

$$A \cdot (A^2 - \text{Id}) = \text{Id} \quad \text{(factor común }A\text{ a izquierda)}$$

Por la definición de inversa: $A$ es invertible y $A^{-1} = A^2 - \text{Id}$. $\blacksquare$

### H.2 — $A^3 = \mathcal{O} \Rightarrow (A + \text{Id})^{-1} = A^2 - A + \text{Id}$ (ejercicio VI.3)

**Hipótesis:** $A^3 = \mathcal{O}$.

**Tesis:** $A + \text{Id}$ es invertible y $(A + \text{Id})^{-1} = A^2 - A + \text{Id}$.

**Demostración:** verificamos que $(A + \text{Id}) \cdot (A^2 - A + \text{Id}) = \text{Id}$.

$$(A + \text{Id})(A^2 - A + \text{Id}) = A^3 - A^2 + A + A^2 - A + \text{Id} \quad \text{(distributiva, }\text{Id}\cdot M = M\text{)}$$

$$= A^3 + \text{Id} \quad \text{(los términos }-A^2 + A^2\text{ y }A - A\text{ se cancelan)}$$

$$= \mathcal{O} + \text{Id} = \text{Id} \quad \text{(hipótesis: }A^3 = \mathcal{O}\text{)}$$

Entonces $A^2 - A + \text{Id}$ es la inversa de $A + \text{Id}$. $\blacksquare$

> **Truco:** este es el caso matricial de la identidad polinomial $(x+1)(x^2 - x + 1) = x^3 + 1$.

---

## I. Otros del práctico

### I.1 — V.11: Ley de simplificación a izquierda

**Enunciado:** Si $A$ es invertible y $AB = AC$, entonces $B = C$.

**Hipótesis:** $A$ invertible; $AB = AC$.

**Tesis:** $B = C$.

**Demostración:** multiplicamos a izquierda por $A^{-1}$.

$$AB = AC \implies A^{-1}(AB) = A^{-1}(AC) \implies (A^{-1} A) B = (A^{-1} A) C \implies \text{Id} \cdot B = \text{Id} \cdot C \implies B = C \quad \blacksquare$$

> **Cuidado:** esto NO vale si $A$ no es invertible. Contraejemplo (V.11.3): $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, $C = \begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix}$. Verificás $AB = AC$ pero $B \neq C$.

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
