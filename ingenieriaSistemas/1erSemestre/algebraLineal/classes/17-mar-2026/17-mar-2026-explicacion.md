# Explicacion de Temas - Clase del 17-03-2026: Matrices — Definicion, Tipos y Operaciones

## La Gran Pregunta: Por que empezamos un curso de algebra lineal hablando de "tablas de numeros"?

Porque las matrices son **la estructura fundamental** sobre la que se construye todo el curso. Cada tema que viene despues (determinantes, sistemas de ecuaciones, geometria del espacio, espacios vectoriales, transformaciones lineales) depende de que entiendas que es una matriz, como clasificarla, y como operar con ellas. Pensalo como aprender el abecedario antes de leer: sin matrices, no hay algebra lineal.

---

## Conexion con la Clase Anterior

Esta es la **primera clase del curso**, asi que no hay clase anterior. Lo que si hay es un punto de partida: los numeros reales y las operaciones que ya conoces (sumar, multiplicar, el concepto de neutro, de opuesto). Vas a ver que muchas propiedades de las matrices son **analogas** a las de los numeros reales, y el profesor hace ese puente explicito varias veces durante la clase.

---

## Logistica del Curso (Resumen)

Antes de entrar en materia, el profesor dedico un buen rato a explicar como funciona el curso. Si no fuiste a la primera clase, esto es lo que necesitas saber:

**Profesor:** Gabriel Cisneros, ingeniero electrico graduado de ORT en 2023.

**Horarios:** Martes y miercoles, 19:30 a 22:30.

**Sistema de puntos (sobre 100):**

| Componente | Puntos | Detalle |
|------------|--------|---------|
| Ejercicios | 30 | 14 de evaluacion continua + 16 de control de practicos |
| Primer parcial | 20 | Semana 7 (5 de mayo), temas 1-3 + parte de 4 |
| Segundo parcial | 50 | Semana 17 (julio), resto de tema 4 + temas 5-6 |

**Evaluacion continua (14 puntos):** 8 pruebas de 2.5 puntos cada una. Nivel bajo-medio, 30 minutos, grupos de hasta 3 personas, entrega individual, presencial, con material y dispositivos electronicos. Semanas: 2, 4, 5, 8, 12, 13, 14.

**Control de practicos / defensa (16 puntos):** Semana 11, individual, 1 hora, presencial, con material pero **sin celular ni dispositivos electronicos**. Nivel un poco mas alto que la evaluacion continua.

**Exoneracion:** >= 86 puntos.

**Aprobacion (derecho a examen):** >= 70 puntos.

**Segunda instancia:** Si no llegas a 70, podes volver a dar el segundo parcial (mismos 50 puntos). Condiciones: P1 + P2 + ejercicios < 70, P1 + ejercicios >= 20, P2 >= 10/50.

> "La experiencia que tengo, ya se, dos o tres semestres que se vienen implementando, es que la aprobacion en la segunda instancia es muy baja."

**Traduccion:** No cuentes con la segunda instancia como plan B. La tasa de aprobacion es bajisima.

**Sobre inteligencia artificial:**

> "Ser responsable con el uso de la inteligencia artificial... tener la conciencia de ustedes pensar los ejercicios, tratar de resolverlos antes."

**Traduccion:** Podes usar IA como herramienta, pero el dia del parcial estas solo. Si no pensaste los ejercicios vos mismo, no vas a saber resolverlos.

**Los 6 temas del curso:**

| # | Tema | Parcial |
|---|------|---------|
| 1 | Matrices | Primero |
| 2 | Determinantes | Primero |
| 3 | Sistemas de ecuaciones lineales | Primero |
| 4 | Geometria del espacio | Dividido entre ambos |
| 5 | Espacios vectoriales | Segundo |
| 6 | Transformaciones lineales | Segundo |

**Contacto:** Teams (responde mas rapido) o email.

**Ayudantias:** Arrancan semana 3-4, dia a confirmar.

---

## Definicion de Matriz

### Que es una matriz?

> "Una matriz basicamente es un arreglo de numeros... estos numeros los arreglamos, ordenamos en filas y columnas."

**Traduccion:** Una matriz es simplemente una tabla de numeros reales organizada en filas (horizontales) y columnas (verticales).

Pensalo como una planilla de Excel: tenes filas que van de izquierda a derecha, columnas que van de arriba a abajo, y en cada celda hay un numero.

### Notacion

La notacion formal es:

```
A ∈ M_mxn(R)
```

Que significa esto?
- **A** = el nombre de la matriz
- **M** = "matrices" (el conjunto al que pertenece)
- **m** = numero de filas
- **n** = numero de columnas
- **R** = numeros reales (todos los numeros que conoces: enteros, decimales, fracciones, etc.)
- La formula completa dice: "A es una matriz de m filas y n columnas con entradas en los numeros reales"

La **dimension** de la matriz es **filas x columnas**, siempre en ese orden. Primero filas, despues columnas.

### Identificar entradas

Cada numero dentro de la matriz se identifica por su posicion: fila y columna. La notacion es:

```
a_ij = entrada en la fila i, columna j
```

**Ejemplo concreto:** Tomemos esta matriz:

```
A = | 1  2  3 |
    | 4  5  6 |
```

Esta matriz tiene 2 filas y 3 columnas, entonces:

```
A ∈ M_2x3(R)
```

Sus entradas son:
- `a_11 = 1` (fila 1, columna 1)
- `a_12 = 2` (fila 1, columna 2)
- `a_13 = 3` (fila 1, columna 3)
- `a_21 = 4` (fila 2, columna 1)
- `a_22 = 5` (fila 2, columna 2)
- `a_23 = 6` (fila 2, columna 3)

### La matriz generica M por N

Para demostraciones teoricas se usa la matriz generica, que representa **cualquier** matriz de m filas y n columnas:

```
A = | a_11  a_12  ...  a_1n |
    | a_21  a_22  ...  a_2n |
    |  ...   ...  ...   ... |
    | a_m1  a_m2  ...  a_mn |
```

Esta la vas a ver muchas veces en el curso. Sirve para demostrar propiedades que valen para **cualquier** dimension, no para un caso particular.

---

## Igualdad de Matrices

### Cuando dos matrices son iguales?

> "Para que dos matrices sean iguales, lo primero que tengo es que tenga la misma dimension... todos los elementos tienen que ser igual uno a uno."

**Traduccion:** Dos matrices son iguales si y solo si tienen la misma cantidad de filas y columnas, y ademas cada entrada coincide una a una.

Formalmente:

```
A = B  si y solo si:
1. Ambas tienen dimension m x n (misma dimension)
2. a_ij = b_ij  para todo i = 1..m, j = 1..n (cada entrada es igual)
```

Que significa esto?
- **a_ij = b_ij** = la entrada de A en fila i columna j es igual a la entrada de B en fila i columna j
- **para todo i, j** = esto tiene que pasar en TODAS las posiciones, no solo en algunas

Analogia: es como comparar dos planillas de Excel. Tienen que tener la misma cantidad de filas y columnas, y cada celda tiene que tener exactamente el mismo numero. Si una sola celda difiere, las matrices son distintas.

---

## Tipos de Matrices

### Matriz Fila (Vector Fila)

Una matriz con **una unica fila** y n columnas.

```
A ∈ M_1xn(R)
```

Forma generica:

```
A = | a_11  a_12  ...  a_1n |
```

**Ejemplo:**

```
A = | 1  2  3 |       A ∈ M_1x3(R)
```

El profesor aclaro que a las matrices fila tambien se las llama **vectores fila**, pero por ahora quedarse con la definicion de matriz fila.

### Matriz Columna (Vector Columna)

Una matriz con m filas y **una unica columna**.

```
A ∈ M_mx1(R)
```

Forma generica:

```
A = | a_11 |
    | a_21 |
    | ...  |
    | a_m1 |
```

Observa que el subindice de la columna siempre es 1 (porque solo hay una columna). Lo que cambia es la fila.

**Ejemplo:**

```
A = | 4 |
    | 7 |       A ∈ M_3x1(R)
    | 9 |
```

> "A veces los vectores los escribimos acostados, a veces los escribimos parados... por ahora quedense con la definicion de matriz fila y matriz columna."

**Traduccion:** No te preocupes todavia por la diferencia entre "vector fila" y "vector columna" mas alla de la forma. Esto se aclara mas adelante en el curso, cuando vean sistemas de ecuaciones.

### Matriz Cuadrada

Una matriz donde el **numero de filas coincide con el numero de columnas**.

```
A ∈ M_nxn(R)
```

**Ejemplo:**

```
A = | 4  7 |
    | 8  9 |       A ∈ M_2x2(R)
```

> "En el curso vamos a trabajar mas que nada con matrices cuadradas porque les podemos calcular el determinante, algunas tienen inversa, vamos a ver que tienen algunas propiedades."

**Traduccion:** Las matrices cuadradas son las protagonistas del curso. Son las unicas a las que les podemos calcular determinante, las unicas que pueden tener inversa, y las que tienen las propiedades mas interesantes.

### Diagonal Principal

Solo existe en **matrices cuadradas**. Son los elementos donde el numero de fila coincide con el numero de columna:

```
Diagonal principal = a_11, a_22, a_33, ..., a_nn
```

Es decir, todos los elementos de la forma `a_ii`. Visualmente, es la diagonal que va desde la esquina superior izquierda hasta la esquina inferior derecha.

**Ejemplo en la matriz anterior:**

```
A = | [4]  7 |
    |  8  [9]|
```

La diagonal principal es: 4 y 9 (los elementos entre corchetes).

### Matriz Triangular Superior

Una **matriz cuadrada** donde todas las entradas **por debajo** de la diagonal principal son cero.

```
A es triangular superior  si y solo si  a_ij = 0  para todo i > j
```

Que significa `i > j`? Que el numero de fila es mayor que el numero de columna. Eso corresponde a los elementos que estan debajo de la diagonal.

Forma generica:

```
A = | a_11  a_12  ...  a_1n |
    |  0    a_22  ...  a_2n |
    |  ...   ...  ...   ... |
    |  0     0    ...  a_nn |
```

**Ejemplo:**

```
A = | 1  3 |
    | 0  2 |       Triangular superior 2x2
```

La diagonal principal (1 y 2) y lo de arriba (3) pueden ser cualquier numero. Lo de abajo **tiene que ser cero**.

El profesor aclaro un punto importante: los elementos de la diagonal principal **pueden ser cero**. Si todos lo son, sigue siendo triangular superior (seria un caso particular).

### Matriz Triangular Inferior

Una **matriz cuadrada** donde todas las entradas **por encima** de la diagonal principal son cero. Es el caso inverso de la triangular superior.

```
A es triangular inferior  si y solo si  a_ij = 0  para todo i < j
```

Forma generica:

```
A = | a_11   0    ...   0   |
    | a_21  a_22  ...   0   |
    |  ...   ...  ...   ... |
    | a_n1  a_n2  ...  a_nn |
```

**Ejemplo:**

```
A = | 1  0 |
    | 3  6 |       Triangular inferior 2x2
```

La diagonal principal (1 y 6) y lo de abajo (3) pueden ser cualquier numero. Lo de arriba (la entrada `a_12`) **tiene que ser cero**.

### Matriz Diagonal

Una **matriz cuadrada** donde todas las entradas **fuera de la diagonal principal** son cero. Es como ser triangular superior **y** triangular inferior al mismo tiempo.

```
A es diagonal  si y solo si  a_ij = 0  para todo i ≠ j
```

Forma generica:

```
A = | a_11   0    ...   0   |
    |  0    a_22  ...   0   |
    |  ...   ...  ...   ... |
    |  0     0    ...  a_nn |
```

**Ejemplo:**

```
A = | 3  0  0 |
    | 0  5  0 |       Diagonal 3x3, A ∈ M_3x3(R)
    | 0  0  1 |
```

Analogia: una matriz diagonal es como una autopista con peajes. Solo importan los puntos donde fila = columna (los peajes en la diagonal). Todo lo demas esta vacio (cero).

### Matriz Identidad

Una **matriz diagonal** donde todos los elementos de la diagonal principal son **1**. Es la matriz mas importante del curso.

Notacion:

```
I_nxn
```

**Ejemplos:**

```
I_1x1 = | 1 |

I_2x2 = | 1  0 |
         | 0  1 |

I_3x3 = | 1  0  0 |
         | 0  1  0 |
         | 0  0  1 |
```

La propiedad clave de la identidad:

```
A * I = I * A = A
```

> "Es el neutro del producto de matrices... seria analogo al 1 en los numeros reales."

**Traduccion:** Asi como multiplicar cualquier numero por 1 te da el mismo numero (5 x 1 = 1 x 5 = 5), multiplicar cualquier matriz por la identidad te da la misma matriz. Por eso la identidad es el **elemento neutro** de la multiplicacion de matrices.

### Matriz Nula

Una matriz donde **todas las entradas son cero**. Puede ser de **cualquier dimension** (no necesita ser cuadrada).

Notacion:

```
0_mxn
```

**Ejemplos:**

```
0_1x1 = | 0 |

0_2x3 = | 0  0  0 |
         | 0  0  0 |
```

La propiedad clave de la matriz nula:

```
A + 0 = 0 + A = A
```

> "Asi como tenemos la identidad que es analogo al 1... vamos a tener la matriz nula que es analogo al 0 en los numeros escalares."

**Traduccion:** Asi como sumar cero a cualquier numero te da el mismo numero (5 + 0 = 0 + 5 = 5), sumar la matriz nula a cualquier matriz te da la misma matriz. Por eso la nula es el **elemento neutro** de la suma de matrices.

### Resumen de tipos de matrices

| Tipo | Condicion | Dimension | Ejemplo 2x2 |
|------|-----------|-----------|--------------|
| Fila | 1 fila, n columnas | 1 x n | `[1, 2]` |
| Columna | m filas, 1 columna | m x 1 | `[1; 2]` |
| Cuadrada | filas = columnas | n x n | `[4,7; 8,9]` |
| Triangular superior | ceros debajo de diagonal | n x n | `[1,3; 0,2]` |
| Triangular inferior | ceros encima de diagonal | n x n | `[1,0; 3,6]` |
| Diagonal | ceros fuera de diagonal | n x n | `[3,0; 0,5]` |
| Identidad | diagonal con todos 1 | n x n | `[1,0; 0,1]` |
| Nula | todo ceros | m x n | `[0,0; 0,0]` |

---

## Suma de Matrices

### Condicion para sumar

> "Lo primero que hay que saber es que para poder sumar dos matrices, la condicion necesaria es que las dos matrices tengan la misma dimension."

**Traduccion:** Solo podes sumar matrices que tienen exactamente la misma cantidad de filas y columnas. No podes sumar una 2x3 con una 4x3.

### Definicion

Sean `A = (a_ij)`, `B = (b_ij)`, `C = (c_ij)`, todas pertenecientes a `M_mxn(R)`. Entonces:

```
C = A + B  si y solo si  c_ij = a_ij + b_ij  para todo i = 1..m, j = 1..n
```

Que significa esto?
- **c_ij = a_ij + b_ij** = cada entrada de la matriz resultado es la suma de las entradas correspondientes de A y B
- **para todo i, j** = esto se hace para TODAS las posiciones

En forma generica:

```
| a_11  a_12  ...  a_1n |     | b_11  b_12  ...  b_1n |     | a_11+b_11  a_12+b_12  ...  a_1n+b_1n |
| a_21  a_22  ...  a_2n |  +  | b_21  b_22  ...  b_2n |  =  | a_21+b_21  a_22+b_22  ...  a_2n+b_2n |
|  ...   ...  ...   ... |     |  ...   ...  ...   ... |     |    ...        ...     ...     ...     |
| a_m1  a_m2  ...  a_mn |     | b_m1  b_m2  ...  b_mn |     | a_m1+b_m1  a_m2+b_m2  ...  a_mn+b_mn |
```

> "Una vez que tenemos las dos matrices de la misma dimension, es sumar entrada a entrada... no tiene mucha ciencia."

**Traduccion:** La suma es la operacion mas simple de matrices. Misma posicion de A, misma posicion de B, sumalas. Repetir para todas las posiciones.

**Ejemplo concreto:**

```
A = | 1  6 |       B = | 0  0 |
    | 4  3 |           | 0  6 |

A + B = | 1+0  6+0 |  =  | 1  6 |
        | 4+0  3+6 |     | 4  9 |
```

### Propiedades de la Suma de Matrices

**1. Cerradura:** Si A y B pertenecen a `M_mxn(R)`, entonces A + B tambien pertenece a `M_mxn(R)`.

En palabras: sumar dos matrices de la misma dimension da como resultado otra matriz de la misma dimension. El resultado no "se escapa" del conjunto.

> "Parece bastante obvio, pero por ejemplo la multiplicacion no es asi. En la multiplicacion yo puedo multiplicar dos matrices y me cambia la dimension."

**Traduccion:** En la suma, las dimensiones nunca cambian. Pero ojo, en la multiplicacion si cambian (lo vemos mas adelante).

**2. Conmutativa:**

```
A + B = B + A
```

El orden no importa. Sumar A + B da lo mismo que sumar B + A. Esto es intuitivo porque cada entrada se suma independientemente, y la suma de numeros reales es conmutativa.

**3. Asociativa:**

```
(A + B) + C = A + (B + C)
```

No importa como agrupes: sumar primero A con B y despues sumarle C da lo mismo que sumar primero B con C y despues sumarle A. El parentesis indica que operacion haces primero, pero el resultado es el mismo.

**4. Existencia del neutro (Matriz nula):**

```
Existe 0_mxn tal que A + 0 = 0 + A = A
```

Ya lo vimos: la matriz nula es el neutro. Sumarle ceros a cualquier matriz no la cambia.

**5. Existencia del opuesto:**

```
Para toda A ∈ M_mxn(R), existe B = -A ∈ M_mxn(R) tal que A + B = B + A = 0_mxn
```

Para cualquier matriz A, siempre existe una matriz opuesta (que es A con todos los signos cambiados). Si sumas A con su opuesta, te da la matriz nula.

**Ejemplo:** Si `A = | 1, 6; 4, 3 |`, entonces `-A = | -1, -6; -4, -3 |`, y `A + (-A) = | 0, 0; 0, 0 |`.

Analogia: es como los numeros reales. El opuesto de 5 es -5, y 5 + (-5) = 0. Lo mismo pero con cada entrada de la matriz.

---

## Producto Escalar por Matriz

### Definicion

Sean `A = (a_ij)` perteneciente a `M_mxn(R)` y `k` un numero real (escalar). Entonces:

```
B = k * A  si y solo si  b_ij = k * a_ij  para todo i = 1..m, j = 1..n
```

Que significa esto?
- **k** = un numero real cualquiera (por eso se llama "escalar")
- **b_ij = k * a_ij** = cada entrada de la matriz resultado es la entrada original multiplicada por k

En palabras: multiplicas **cada entrada** de la matriz por el mismo numero k. Es la operacion mas directa que hay.

**Ejemplo concreto:**

```
A = | 2  1  4 |
    | 6  2  1 |       k = 2
    | 3  2  3 |

2 * A = | 2*2  2*1  2*4 |  =  | 4   2  8 |
        | 2*6  2*2  2*1 |     | 12  4  2 |
        | 2*3  2*2  2*3 |     | 6   4  6 |
```

### Propiedades del Producto Escalar por Matriz

Sean alfa y beta numeros reales, y A, B matrices de `M_mxn(R)`:

**1. Asociatividad de escalares:**

```
(alfa * beta) * A = alfa * (beta * A) = beta * (alfa * A)
```

Los escalares "van y vienen" sin alterar el resultado. No importa en que orden multipliques los escalares.

**Ejemplo:** `(2 * 3) * A = 2 * (3 * A) = 3 * (2 * A)`. Da lo mismo multiplicar la matriz por 6 directamente, que primero por 3 y despues por 2, que primero por 2 y despues por 3.

**2. Distributiva (dos escalares, una matriz):**

```
(alfa + beta) * A = alfa * A + beta * A
```

Podes sumar primero los escalares y despues multiplicar, o multiplicar por separado y despues sumar las matrices. El resultado es el mismo.

**3. Distributiva (un escalar, dos matrices):**

```
alfa * (A + B) = alfa * A + alfa * B
```

Podes sumar primero las matrices y despues multiplicar por el escalar, o multiplicar cada una por separado y despues sumar. Mismo resultado.

**4. Identidad escalar:**

```
1 * A = A  para toda A
```

Multiplicar cualquier matriz por 1 no la cambia. Consistente con todo lo que sabemos de los numeros reales.

---

## Producto entre Matrices

### Condicion: Matrices Conformables

Esta es la operacion mas compleja de las tres. Lo primero: **no cualquier par de matrices se puede multiplicar.**

> "La multiplicacion no es asi, yo puedo multiplicar dos matrices y me cambia la dimension."

**Traduccion:** A diferencia de la suma (donde ambas matrices deben tener la misma dimension), en la multiplicacion las dimensiones pueden ser distintas, y ademas la dimension del resultado puede ser diferente a la de los factores.

La condicion para poder multiplicar es:

```
Si A ∈ M_mxn(R) y B ∈ M_nxp(R), entonces A * B ∈ M_mxp(R)
```

Que significa esto?
- **n** aparece dos veces: el numero de **columnas de A** tiene que ser igual al numero de **filas de B**
- El resultado tiene **m filas** (las filas de A) y **p columnas** (las columnas de B)
- La dimension que "coincide" (n) **desaparece** en el resultado

Analogia: es como un enchufe. A tiene n "pines" de salida (columnas) y B tiene n "agujeros" de entrada (filas). Si no coinciden, no se puede enchufar.

**Ejemplo de dimensiones:**

```
A es 2x3, B es 3x4  -->  A*B es 2x4  (el 3 "desaparece")
A es 2x3, B es 2x4  -->  A*B NO SE PUEDE (3 ≠ 2, no son conformables)
```

### Como calcular cada entrada

Para encontrar la entrada `(i, j)` del resultado, tomas la **fila i de A** y la **columna j de B**, multiplicas elemento a elemento, y sumas todo:

```
c_ij = a_i1 * b_1j + a_i2 * b_2j + ... + a_in * b_nj
```

Es decir: fila i de A "contra" columna j de B, producto punto a punto y suma.

**Ejemplo concreto completo:**

Tomemos las matrices que uso el profesor para demostrar la no conmutatividad:

```
A = | 1   2 |       B = | 2  1 |
    | 3  -4 |           | 3  4 |
```

Ambas son 2x2, asi que son conformables (2 columnas de A = 2 filas de B).

Para calcular A * B:

```
Entrada (1,1): fila 1 de A * columna 1 de B = 1*2 + 2*3 = 2 + 6 = 8
Entrada (1,2): fila 1 de A * columna 2 de B = 1*1 + 2*4 = 1 + 8 = 9
Entrada (2,1): fila 2 de A * columna 1 de B = 3*2 + (-4)*3 = 6 - 12 = -6
Entrada (2,2): fila 2 de A * columna 2 de B = 3*1 + (-4)*4 = 3 - 16 = -13

A * B = | 8    9 |
        | -6  -13|
```

### Propiedades del Producto de Matrices

**1. Asociativa:**

```
(A * B) * C = A * (B * C)
```

Multiplicar primero A por B y el resultado por C da lo mismo que multiplicar primero B por C y el resultado por A. El parentesis se puede mover.

**2. Distributiva (dos versiones):**

```
A * (B + C) = A * B + A * C
(A + B) * C = A * C + B * C
```

**Atencion:** en la segunda version, C va a la **derecha** en ambos terminos. No se puede mover de lado porque el producto no es conmutativo.

**3. Existencia del neutro (Matriz identidad):**

```
A * I = I * A = A
```

Ya lo vimos: la identidad es el neutro del producto.

**4. Asociatividad con escalares:**

```
k * (A * B) = (k * A) * B = A * (k * B)
```

> "El numero puede ir y venir y no me cambia el resultado. Siempre y cuando tengo que mantener el orden de que esta primero A y luego B."

**Traduccion:** El escalar k se puede "pegar" a cualquiera de las dos matrices, pero lo que **no podes hacer** es cambiar el orden de A y B entre si.

### NO PROPIEDAD: El Producto NO es Conmutativo

Esta es quizas la leccion mas importante de la clase.

> "Es un error comun... lo veo siempre en los parciales."

> "A por B igual a B por A, que lo asumen, y eso en realidad, salvo que justo de casualidad de lo mismo, no es una regla, es una casualidad."

**Traduccion:** A * B **no es igual** a B * A. Si alguna vez te da igual, es casualidad, no regla. Nunca asumas que podes cambiar el orden.

**Demostracion con ejemplo (el mismo que uso el profesor):**

```
A = | 1   2 |       B = | 2  1 |
    | 3  -4 |           | 3  4 |
```

Ya calculamos A * B arriba:

```
A * B = | 8    9 |
        | -6  -13|
```

Ahora calculemos B * A:

```
Entrada (1,1): 2*1 + 1*3 = 2 + 3 = 5
Entrada (1,2): 2*2 + 1*(-4) = 4 - 4 = 0
Entrada (2,1): 3*1 + 4*3 = 3 + 12 = 15
Entrada (2,2): 3*2 + 4*(-4) = 6 - 16 = -10

B * A = | 5    0 |
        | 15  -10|
```

Comparemos:

```
A * B = | 8    9 |       B * A = | 5    0 |
        | -6  -13|              | 15  -10|
```

**Son completamente diferentes.** Incluso siendo ambas matrices cuadradas 2x2, el producto no conmuta.

> "Si en un caso no se cumple, ya no es una regla. Le llamamos un contraejemplo."

**Traduccion:** Basta con encontrar **un solo caso** donde A * B sea distinto de B * A para probar que el producto no es conmutativo en general. Y acabamos de encontrarlo.

**Casos especiales que SI conmutan (pero son excepciones, no reglas):**
- A * I = I * A (la identidad conmuta con cualquier matriz)
- A * 0 = 0 * A (la nula conmuta con cualquier matriz)
- A * A = A * A (una matriz consigo misma, trivialmente)

Pero estas son excepciones. La regla general es que **no conmuta**.

---

## Ejercicio Resuelto en Clase

**Enunciado:** Sean A y B matrices de 2x2. Dados:

```
2A - B = | 1   6 |
         | 3  -1 |

A + B  = | 2   3 |
         | 0  -2 |
```

Hallar A y B.

**Resolucion paso a paso:**

**Paso 1:** Sumar ambas ecuaciones. La idea es que -B y +B se cancelan:

```
(2A - B) + (A + B) = | 1   6 | + | 2   3 |
                      | 3  -1 |   | 0  -2 |
```

Por el lado izquierdo, agrupamos por asociativa:

```
(2A + A) + (-B + B) = 3A + 0 = 3A
```

Por el lado derecho, sumamos entrada a entrada:

```
| 1+2   6+3  |  =  | 3   9 |
| 3+0  -1-2  |     | 3  -3 |
```

**Paso 2:** Despejar A dividiendo por 3 (o sea, multiplicando por 1/3):

```
3A = | 3   9 |
     | 3  -3 |

A = (1/3) * | 3   9 |  =  | 1   3 |
            | 3  -3 |     | 1  -1 |
```

**Paso 3:** Obtener B usando la segunda ecuacion (A + B = ...):

```
B = (A + B) - A = | 2   3 | - | 1   3 |  =  | 1   0 |
                  | 0  -2 |   | 1  -1 |     | -1  -1|
```

**Resultado:**

```
A = | 1   3 |       B = | 1   0 |
    | 1  -1 |           | -1  -1|
```

---

## Temas que Quedan para las Proximas Clases

El profesor cerro la clase mencionando lo que falta ver del tema matrices:

- **Matriz traspuesta** (cambiar filas por columnas)
- **Traza** de una matriz
- **Matriz inversa**
- **Induccion completa**
- Mas tipos de matrices que se definen a partir de estas operaciones (simetrica, potente, etc.)

---

## Definiciones para el Parcial

**Matriz:** Arreglo de numeros reales organizados en filas y columnas. Se denota `A ∈ M_mxn(R)` donde m es filas y n es columnas.

**Dimension de una matriz:** Filas por columnas (m x n). Siempre filas primero.

**Entrada a_ij:** Elemento ubicado en la fila i y la columna j de la matriz A.

**Igualdad de matrices:** Dos matrices son iguales si tienen la misma dimension y todas sus entradas coinciden una a una.

**Matriz fila:** Matriz con una unica fila y n columnas. `A ∈ M_1xn(R)`.

**Matriz columna:** Matriz con m filas y una unica columna. `A ∈ M_mx1(R)`.

**Matriz cuadrada:** Matriz donde filas = columnas. `A ∈ M_nxn(R)`.

**Diagonal principal:** En una matriz cuadrada, los elementos `a_11, a_22, ..., a_nn` (donde fila = columna).

**Matriz triangular superior:** Matriz cuadrada con todos ceros debajo de la diagonal principal. `a_ij = 0` para todo `i > j`.

**Matriz triangular inferior:** Matriz cuadrada con todos ceros encima de la diagonal principal. `a_ij = 0` para todo `i < j`.

**Matriz diagonal:** Matriz cuadrada con todos ceros fuera de la diagonal principal. `a_ij = 0` para todo `i ≠ j`.

**Matriz identidad (I_nxn):** Matriz diagonal con todos unos en la diagonal principal. Neutro del producto de matrices: `A * I = I * A = A`.

**Matriz nula (0_mxn):** Matriz con todas sus entradas iguales a cero, de cualquier dimension. Neutro de la suma de matrices: `A + 0 = 0 + A = A`.

**Matrices conformables:** Dos matrices son conformables para la multiplicacion si el numero de columnas de la primera es igual al numero de filas de la segunda.

**Producto de matrices NO conmutativo:** En general, `A * B ≠ B * A`. No se puede asumir que el orden no importa.

---

## Posibles Preguntas para el Parcial

**Cuando dos matrices son iguales?**
Cuando tienen la misma dimension (m x n) y cada entrada coincide una a una: `a_ij = b_ij` para todo i y j.

**Que condicion se necesita para sumar dos matrices?**
Ambas matrices deben tener la misma dimension. La suma se hace entrada a entrada.

**Que condicion se necesita para multiplicar dos matrices?**
Las matrices deben ser conformables: el numero de columnas de la primera debe ser igual al numero de filas de la segunda. Si A es m x n y B es n x p, el resultado A * B es m x p.

**Es conmutativo el producto de matrices?**
No. En general A * B es distinto de B * A. Si alguna vez da igual, es casualidad, no regla.

**Cual es la diagonal principal de una matriz cuadrada?**
Los elementos donde el numero de fila coincide con el numero de columna: `a_11, a_22, ..., a_nn`.

**Que diferencia hay entre una matriz diagonal y la matriz identidad?**
Ambas tienen ceros fuera de la diagonal principal. La diferencia es que la identidad exige que todos los elementos de la diagonal sean 1, mientras que una diagonal cualquiera puede tener otros valores.

**Cual es el neutro de la suma de matrices? Y del producto?**
El neutro de la suma es la matriz nula (todo ceros). El neutro del producto es la matriz identidad (diagonal con unos).

**Puede una matriz nula ser cuadrada?**
Si, la nula puede ser de cualquier dimension: cuadrada (n x n) o rectangular (m x n).

**Si A es 2x3 y B es 3x4, se puede calcular A*B? Y B*A?**
A * B si se puede (columnas de A = 3 = filas de B) y da una matriz 2x4. B * A no se puede (columnas de B = 4 ≠ 2 = filas de A).

**Dado un sistema de ecuaciones matriciales, como se despeja una matriz?**
Se usan las propiedades de suma y producto escalar. Por ejemplo, sumando ecuaciones para cancelar terminos (como se hizo en el ejercicio de clase: 2A - B + A + B = 3A).

---

Documento generado mediante analisis exhaustivo (3 pasadas) de la transcripcion de la clase del 17-03-2026, Algebra Lineal, profesor Gabriel Cisneros.
