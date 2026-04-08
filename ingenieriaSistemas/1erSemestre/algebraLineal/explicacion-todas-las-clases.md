# Explicacion de Todas las Clases - Algebra Lineal (17/03 - 25/03/2026)

Este documento consolida las cuatro primeras clases del curso de Algebra Lineal con Gabriel Cisneros (FI-2103, ORT Uruguay), desde la presentacion del curso hasta el dia anterior a la primera prueba de evaluacion continua y las vacaciones de Semana de Turismo. Cada clase respeta el orden y los matices de la transcripcion original.

## La Gran Pregunta del Modulo de Matrices

Si una matriz no es un numero, sino una grilla de numeros, ¿como se "operan" entre si? ¿Como se suman, como se multiplican, como se invierten? ¿Y por que tantas reglas que parecen "obvias" en numeros (como `a * b = b * a` o "pasar dividiendo") dejan de funcionar? Las primeras cuatro clases construyen el lenguaje, las operaciones y las propiedades de las matrices, hasta llegar al herramienta mas potente: la matriz inversa, que es el equivalente matricial de la division.

---

# Clase 1 - 17 de Marzo de 2026: Presentacion del Curso, Tipos de Matrices y Operaciones

## La Gran Pregunta de Hoy: ¿Que es una matriz y como la operamos?

La primera clase tiene dos partes muy distintas. Primero, la presentacion del curso: como se evalua, cuantos parciales hay, que es la "evaluacion continua", quien es el profesor, etc. Despues, arranca el teorico de matrices: definir que es una matriz, los distintos tipos que hay, y empezar a operarlas con suma, producto por escalar, y producto entre matrices. La idea es construir todo el vocabulario basico para que despues podamos hablar de cosas mas complicadas.

---

## Conexion con la Clase Anterior

No hay clase anterior - es la primera clase del curso y del semestre.

---

## Presentacion del Profesor y del Curso

### Quien es el profesor

> "Mi nombre es Gabriel Cisneros, hace unos anos que estoy aca vinculado a la catedra, estudie aca ingenieria electrica en la ORT, me gradue en 2023"

**Traduccion:** El profesor es Gabriel Cisneros, ingeniero electrico graduado de ORT en 2023, que ahora forma parte del cuerpo docente de Algebra Lineal.

### Horarios

- **Dias:** martes y miercoles
- **Hora:** 19:30 a 22:30
- **Carga semanal:** 6 horas (se reparten entre teorico y practico, generalmente 3+3 o 4+2 segun el tema)

### Sistema de evaluacion (sobre 100 puntos)

| Componente | Puntaje | Detalle |
|------------|---------|---------|
| Ejercicios de evaluacion continua | 30 puntos | 14 puntos en 8 pruebas de 2,5 c/u + 18 puntos del control de practicos |
| Primer parcial | 20 puntos | Semana 7 (5 de mayo, 19:30) |
| Segundo parcial | 50 puntos | Semana 17 (julio) |

### Reglas de aprobacion

- **Mayor o igual a 70 puntos:** derecho a dar examen
- **Mayor o igual a 86 puntos:** exonera (no rinde examen)
- **Menor a 70 puntos:** recursa o tiene derecho a la segunda instancia (si cumple condiciones)

### Segunda instancia (formato nuevo)

> "La aprobacion en la segunda instancia es muy baja"

**Traduccion:** La segunda instancia consiste en volver a dar el segundo parcial. Es una opcion de rescate, no de exoneracion. El profesor recomienda explicitamente **no contar con esto** porque historicamente la tasa de aprobacion es baja.

**Condiciones para acceder a segunda instancia:**
1. Primer parcial + segundo parcial + ejercicios menor a 70 (si no, ya estarias aprobando)
2. Primer parcial + ejercicios mayor o igual a 20 puntos
3. Segundo parcial mayor o igual a 10/50 puntos

Si no se cumple alguna (sobre todo la tercera), se recursa directamente.

### Evaluacion continua

> "Son 8 pruebas de 2,5 puntos cada una de nivel medio-bajo, la idea es mas que nada un seguimiento y aprendizaje continuo"

**Traduccion:** Son 8 pruebas cortas de 30 minutos cada una, distribuidas a lo largo del semestre (semanas 2, 4, 5, 8, 12, 13, 14). Cada una vale 2,5 puntos. Son presenciales, en grupos de hasta 3 personas, con material y dispositivos electronicos permitidos. La entrega es individual aunque se trabaje en grupo. Suman 14 puntos al total. La primera de estas pruebas cae el miercoles 25-03-2026.

### Control de practicos (defensa)

- **Cuando:** semana 11
- **Puntaje:** 18 puntos
- **Formato:** individual, presencial, con material pero **sin** dispositivos electronicos
- **Nivel:** algo mas alto que la evaluacion continua

### Anuncio sobre el uso de IA

> "Ser responsable con el uso de la inteligencia artificial. El dia del parcial ustedes van a estar solos."

**Traduccion:** Pueden usar IA para estudiar, pero deben pensar los ejercicios por su cuenta primero. Si en el parcial dependen de la IA y no la tienen, no van a saber resolver nada. La IA es herramienta, no muleta.

### Temas del curso

| Tema | Cuando | Va al parcial |
|------|--------|---------------|
| 1. Matrices | Semanas 1-2 | Primer parcial |
| 2. Determinantes | Semana 2 (despues de Semana de Turismo) | Primer parcial |
| 3. Sistemas de ecuaciones lineales | Semana 3 | Primer parcial |
| 4. Geometria del espacio | Semana 4 (parte 1 al 1er parcial, parte 2 al 2do) | Ambos |
| 5. Espacios vectoriales | Tema 5 | Segundo parcial |
| 6. Transformaciones lineales | Tema 6 (ultimas 2 semanas) | Segundo parcial |

### Contacto

- **Teams:** Gabriel Cisneros (responde rapido)
- **Correo:** tambien disponible (responde mas lento)

---

## Definicion de Matriz

### Que es una matriz

> "Una matriz basicamente es un arreglo de numeros, nosotros vamos a trabajar en el curso con numeros reales, y basicamente estos numeros los arreglamos, ordenamos en filas y columnas"

**Traduccion:** Una matriz es una grilla rectangular de numeros reales organizados en filas (horizontales) y columnas (verticales).

**Notacion:** Si una matriz `A` tiene `m` filas y `n` columnas, decimos que `A` pertenece a `M_mxn(R)` (matrices de `m` por `n` reales).

```
A = | 1  3  -1 |
    | 2  4   5 |
```

Esta matriz `A` pertenece a `M_2x3(R)` (2 filas, 3 columnas).

### Notacion para entradas

Cada entrada de la matriz se identifica por su fila y su columna usando la notacion `a_ij`, donde `i` es el numero de fila y `j` es el numero de columna.

- `a_11` = entrada en fila 1, columna 1 (en el ejemplo: 1)
- `a_22` = entrada en fila 2, columna 2 (en el ejemplo: 4)
- `a_13` = entrada en fila 1, columna 3 (en el ejemplo: -1)

> "Cuando tengo el doble parentesis, significa eso, que cada entrada de la matriz A se va a llamar a sub i j"

**Traduccion:** La notacion `A = (a_ij)` quiere decir "la matriz A cuyas entradas se llaman a_ij".

**Aclaracion del profesor sobre dimensiones grandes:** si la fila o columna pasan de 9, se usa una coma (por ejemplo, `a_10,5` en vez de `a_105` para evitar ambiguedad). Pero en el curso casi nunca trabajan con matrices tan grandes.

### Matriz generica m por n

Para demostraciones se usa la matriz generica:

```
A = | a_11   a_12   ...   a_1n |
    | a_21   a_22   ...   a_2n |
    |  ...    ...   ...    ... |
    | a_m1   a_m2   ...   a_mn |
```

> "Esta la vamos a usar para las demostraciones, muchas veces se piden demostraciones que se muestren de forma generica, no para una dimension en concreto"

**Traduccion:** Cuando un ejercicio pide demostrar una propiedad para "cualquier matriz", no podemos usar una matriz con numeros concretos. Tenemos que usar la generica con `a_11`, `a_12`, etc., para que el resultado valga sin importar la dimension.

---

## Igualdad de Matrices

### Cuando dos matrices son iguales

Para que dos matrices `A` y `B` sean iguales tienen que cumplirse **dos condiciones**:

1. **Misma dimension:** ambas pertenecen a `M_mxn(R)` con los mismos `m` y `n`.
2. **Mismas entradas:** `a_ij = b_ij` para todo `i = 1...m` y `j = 1...n`.

> "Si una matriz de 3 por 4 no puede ser igual a una matriz de 4 por 3"

**Traduccion:** No alcanza con que tengan los mismos numeros - tienen que estar en las mismas posiciones y tener la misma forma. Una matriz `3x4` jamas puede ser igual a una `4x3`.

---

## Tipos de Matrices

### Matriz fila (vector fila)

Una sola fila, varias columnas. `A` pertenece a `M_1xn(R)`.

```
A = | 1  2  3 |
```

Esta matriz pertenece a `M_1x3(R)`.

### Matriz columna (vector columna)

Varias filas, una sola columna. `A` pertenece a `M_mx1(R)`.

```
A = | 4 |
    | 7 |
    | 9 |
```

Esta matriz pertenece a `M_3x1(R)`.

> "A veces los vectores los escribimos acostados, a veces los escribimos parados, depende a veces del tema"

**Traduccion:** Los vectores se pueden representar como matriz fila o como matriz columna - el contexto define cual conviene. Mas adelante, cuando se vea sistemas de ecuaciones, se aclara cual usar.

### Matriz cuadrada

Numero de filas igual al numero de columnas. `A` pertenece a `M_nxn(R)`.

```
A = | 4  7 |
    | 8  9 |
```

> "Estas son las que mas vamos a trabajar en el curso porque les podemos calcular el determinante, algunas tienen inversa, vamos a ver que tienen algunas propiedades"

**Traduccion:** Casi todo el curso se hace con matrices cuadradas, porque solo en cuadradas se puede definir conceptos como diagonal principal, traza, determinante, inversa, etc.

**Aclaracion sobre tamano en parciales:** las matrices del parcial son maximo `5x5`, por un tema de tiempo de calculo.

### Diagonal principal

Solo existe en matrices cuadradas. Son las entradas donde el numero de fila coincide con el numero de columna: `a_11`, `a_22`, `a_33`, ..., `a_nn`.

```
A = | 1  2  3 |     <- diagonal principal: 1, 5, 9
    | 4  5  6 |
    | 7  8  9 |
```

### Matriz triangular superior

Matriz cuadrada donde todas las entradas **debajo** de la diagonal principal son cero.

```
A = | 1  2  3 |
    | 0  4  5 |
    | 0  0  6 |
```

Formalmente: `a_ij = 0` para todo `i > j`.

Que significa eso?
- Si estamos en la entrada `a_21` (fila 2, columna 1), tenemos `i=2`, `j=1`, entonces `i > j`, asi que `a_21 = 0`.
- Si estamos en `a_31`, `i=3 > j=1`, entonces `a_31 = 0`.
- Y asi para todas las entradas debajo de la diagonal.

### Matriz triangular inferior

Matriz cuadrada donde todas las entradas **encima** de la diagonal principal son cero.

```
A = | 1  0  0 |
    | 4  5  0 |
    | 7  8  9 |
```

Formalmente: `a_ij = 0` para todo `i < j`.

> "Para una matriz triangular superior, la diagonal principal puede ser cero tambien"

**Traduccion:** No es requisito que la diagonal sea distinta de cero. Una matriz con la diagonal todo ceros y todo lo de arriba con valores sigue siendo triangular superior - es un caso particular.

### Matriz diagonal

Matriz cuadrada donde **todas** las entradas fuera de la diagonal principal son cero. Solo la diagonal puede tener valores distintos de cero (aunque algunos pueden ser cero tambien).

```
A = | 4  0  0 |
    | 0  2  0 |
    | 0  0  7 |
```

Formalmente: `a_ij = 0` para todo `i ≠ j`.

**Observacion:** una matriz diagonal es a la vez triangular superior **y** triangular inferior.

### Matriz identidad (I)

Matriz diagonal donde **todos** los elementos de la diagonal principal son `1`.

```
I_2 = | 1  0 |     I_3 = | 1  0  0 |
      | 0  1 |           | 0  1  0 |
                          | 0  0  1 |
```

> "Cumple la particularidad de ser el neutro del producto de matrices"

**Traduccion:** La matriz identidad funciona como el numero `1` en los reales. Si multiplicas cualquier matriz `A` por `I`, te queda `A`. Es decir: `A * I = I * A = A`.

**Notacion:** se nota `I_n` para indicar la identidad `n x n`.

### Matriz nula (O)

Matriz `m x n` (no tiene que ser cuadrada) con todas sus entradas iguales a cero.

```
O_2x3 = | 0  0  0 |
        | 0  0  0 |
```

> "Cumple la propiedad de ser el neutro de la suma de matrices"

**Traduccion:** La matriz nula funciona como el numero `0` en los reales. Si sumas cualquier matriz `A` con la nula, te queda `A`. Es decir: `A + O = O + A = A`.

**Analogia:** En los reales, `1` es el neutro del producto y `0` es el neutro de la suma. En matrices, la `identidad I` es el neutro del producto y la `nula O` es el neutro de la suma.

---

## Operaciones con Matrices

### Suma de matrices

**Requisito:** ambas matrices tienen que tener la **misma dimension**. No se puede sumar una matriz `2x3` con una `4x3`.

**Como se hace:** sumar entrada a entrada.

```
| 1  6 |   | 0  0 |   | 1  6 |
| 4  3 | + | 0  6 | = | 4  9 |
```

Formalmente: si `C = A + B`, entonces `c_ij = a_ij + b_ij` para todo `i, j`.

#### Propiedades de la suma

1. **Cerradura:** la suma de dos matrices `m x n` da una matriz `m x n`.
2. **Conmutativa:** `A + B = B + A`.
3. **Asociativa:** `(A + B) + C = A + (B + C)`.
4. **Existencia del neutro:** existe la matriz nula `O` tal que `A + O = O + A = A`.
5. **Existencia del opuesto:** para toda `A` existe `-A` (la opuesta) tal que `A + (-A) = O`.

> "Parece bastante obvio, pero por ejemplo la multiplicacion no es asi - en la multiplicacion yo puedo multiplicar dos matrices y me cambia la dimension"

**Traduccion:** La cerradura parece trivial, pero es importante porque no siempre se cumple en otras operaciones. Por ejemplo, multiplicar una matriz `2x3` por una `3x4` da una `2x4` - cambio la dimension.

### Producto escalar por matriz

**Operacion:** multiplicar un numero (escalar) `k` por cada entrada de la matriz.

```
       | 2  1  4 |   | 4  2   8 |
2  *  | 6  2  1 | = | 12 4   2 |
       | 3  2  3 |   | 6  4   6 |
```

Formalmente: si `B = k * A`, entonces `b_ij = k * a_ij` para todo `i, j`.

#### Propiedades del producto escalar

1. **Asociativa:** `(α * β) * A = α * (β * A) = β * (α * A)`. Los numeros van y vienen sin alterar el resultado.
2. **Distributiva (numeros y matriz):** `(α + β) * A = α * A + β * A`.
3. **Distributiva (numero y dos matrices):** `α * (A + B) = α * A + α * B`.
4. **Neutro:** `1 * A = A`.

> "No tiene un nombre, esa propiedad. En algunos libros le llaman homogenea"

**Traduccion:** Un alumno pregunto si la primera propiedad tenia nombre, y el profesor aclaro que no tiene un nombre estandar. Algunos libros la llaman "homogenea".

### Producto entre matrices

**Requisito (conformabilidad):** para multiplicar `A` por `B`, el numero de **columnas** de `A` tiene que ser igual al numero de **filas** de `B`.

> "Si A es M por N, B tiene que ser N por P, y la matriz resultante adopta el numero de filas de la primera y el numero de columnas de la segunda - asi tenemos una matriz M por P"

**Traduccion:** Si `A` es `m x n` y `B` es `n x p`, entonces `A * B` es `m x p`. Las dimensiones del medio (las dos `n`) tienen que coincidir y "se cancelan", y queda la dimension de afuera.

```
[A: m x n] * [B: n x p] = [C: m x p]
              ↑    ↑
              tienen que ser iguales
```

**Como se calcula cada entrada:** la entrada `c_ij` (fila `i`, columna `j` del resultado) es el resultado de multiplicar la **fila i de A** con la **columna j de B**, par a par y sumar.

#### Ejemplo: `A` de 2x3 por `B` de 3x4

```
A = | 2  -1  4 |       B = | 1   0   1 |
    | 1   0  6 |           | 2  -1   2 |
                            | 3  -2   0 |
```

Espera, ese ejemplo es 2x3 por 3x3, lo voy a corregir. Vamos al ejemplo real de la transcripcion:

```
A = | 2  -1  4 |       B = | 1   0   1 |
    | 1   0  6 |           | 2  -1   2 |
                            | 3  -2   0 |
```

`A` es `2 x 3`, `B` es `3 x 3`, asi que `A * B` es `2 x 3`.

Calculamos entrada a entrada:

- Entrada `(1,1)`: fila 1 de `A` por columna 1 de `B` = `2*1 + (-1)*2 + 4*3 = 2 - 2 + 12 = 12`
- Entrada `(1,2)`: fila 1 de `A` por columna 2 de `B` = `2*0 + (-1)*(-1) + 4*(-2) = 0 + 1 - 8 = -7`
- Entrada `(1,3)`: fila 1 de `A` por columna 3 de `B` = `2*1 + (-1)*2 + 4*0 = 2 - 2 + 0 = 0`
- Entrada `(2,1)`: fila 2 de `A` por columna 1 de `B` = `1*1 + 0*2 + 6*3 = 1 + 0 + 18 = 19`
- Entrada `(2,2)`: fila 2 de `A` por columna 2 de `B` = `1*0 + 0*(-1) + 6*(-2) = 0 + 0 - 12 = -12`
- Entrada `(2,3)`: fila 2 de `A` por columna 3 de `B` = `1*1 + 0*2 + 6*0 = 1`

```
A * B = | 12  -7   0 |
        | 19 -12   1 |
```

#### Propiedades del producto de matrices

1. **Asociativa:** `(A * B) * C = A * (B * C)`.
2. **Distributiva izquierda:** `A * (B + C) = A * B + A * C`.
3. **Distributiva derecha:** `(A + B) * C = A * C + B * C`.
4. **Neutro:** existe la matriz identidad `I` tal que `A * I = I * A = A`.
5. **Producto con escalar:** `k * (A * B) = (k * A) * B = A * (k * B)` (siempre manteniendo el orden A, B).

#### NO PROPIEDAD: la conmutativa NO se cumple

> "Es un error comun asumir que A por B es igual a B por A. El producto de matrices no es conmutativo. O sea, generalmente A por B es distinto de B por A."

**Traduccion:** Aunque en numeros reales `2 * 3 = 3 * 2`, en matrices cambiar el orden puede cambiar el resultado completamente. **Asumir conmutatividad es uno de los errores mas comunes** y lo corrigen en los parciales.

**Ejemplo concreto del profesor para mostrar que no conmutan:**

```
A = | 1   2 |       B = | 2  1 |
    | 3  -4 |           | 3  4 |
```

Calculamos `A * B`:

```
A * B = | 1*2 + 2*3    1*1 + 2*4    |   | 8     9   |
        | 3*2 + (-4)*3  3*1 + (-4)*4 | = | -6   -13 |
```

Calculamos `B * A`:

```
B * A = | 2*1 + 1*3    2*2 + 1*(-4)  |   | 5    0   |
        | 3*1 + 4*3    3*2 + 4*(-4)  | = | 15  -10 |
```

> "Incluso siendo matriz cuadrada asi todo, se cumple que A por B es distinto de B por A"

**Traduccion:** No solo cuando las dimensiones lo impiden - **incluso entre matrices cuadradas que se pueden multiplicar de las dos formas, los resultados son diferentes**. Aca tenemos `A*B = [[8,9],[-6,-13]]` y `B*A = [[5,0],[15,-10]]`. Son matrices completamente distintas.

> "Si en un caso no se cumple, ya no es una regla. Le llamamos un contraejemplo."

**Traduccion:** Para tirar abajo una "regla" general, alcanza con encontrar **un solo caso** donde no se cumple. Por eso este ejemplo basta para demostrar que la conmutatividad no es propiedad del producto de matrices.

**Casos particulares donde si conmutan:** la matriz identidad conmuta con todas (`A * I = I * A`), y la nula tambien (`A * O = O * A = O`). Tambien conmuta una matriz consigo misma. Pero son **casos excepcionales**, no una regla general.

---

## Anuncios al Final de Clase

- Materiales en Aulas (campus virtual): tienen el teorico y el practico para descargar
- Soluciones del practico al final de la guia
- Pueden adelantar los primeros 13 ejercicios del practico de matrices con lo visto hoy
- El ejercicio 4 del practico (induccion completa) **no** lo pueden hacer todavia
- Los ejercicios 7-13 son de matrices simetricas, traspuesta e inversa - tampoco los pueden hacer todavia

---

# Clase 2 - 18 de Marzo de 2026: Traspuesta, Simetricas, Antisimetricas y Traza

## La Gran Pregunta de Hoy: ¿Como cambian las matrices cuando intercambiamos sus filas y columnas, y por que importa?

Hoy aparecen tres operaciones nuevas que se construyen sobre la idea basica de "intercambiar filas por columnas": la **traspuesta** (la operacion en si), las **matrices simetricas/antisimetricas** (matrices que tienen comportamiento especial frente a la traspuesta), y la **traza** (suma de la diagonal principal). Estas tres herramientas van a ser clave para todas las demostraciones del modulo de matrices.

---

## Conexion con la Clase Anterior

En la clase del 17-03 vimos que es una matriz, los tipos (fila, columna, cuadrada, triangular, diagonal, identidad, nula), la igualdad, y las tres operaciones basicas: **suma**, **producto escalar por matriz** y **producto entre matrices**. Vimos las propiedades de cada operacion, y la **no-propiedad** mas importante: el producto **no es conmutativo** (`A * B ≠ B * A` en general). Hoy se construye sobre todo eso.

---

## Matriz Traspuesta

### Definicion

Sea `A` perteneciente a `M_mxn(R)`. La **traspuesta de A**, notada `A^T` ("A traspuesta"), es la matriz que pertenece a `M_nxm(R)` y tiene **por filas las columnas de A** (o equivalentemente, por columnas las filas de A).

> "Tiene por filas las columnas de A, o lo que es lo mismo decir tambien que tiene por columnas las filas de A"

**Traduccion:** Trasponer es intercambiar el rol de filas y columnas. Lo que antes era la primera fila ahora es la primera columna, lo que era la segunda fila es la segunda columna, etc.

**Observacion sobre dimensiones:** si `A` era `m x n`, entonces `A^T` es `n x m`. Las dimensiones se invierten.

### Ejemplo

```
A = | 3  4  9 |       (es 2x3)
    | 1  2  5 |

A^T = | 3  1 |        (es 3x2)
      | 4  2 |
      | 9  5 |
```

La primera fila de `A` (que era `3, 4, 9`) ahora es la primera columna de `A^T`. La segunda fila (`1, 2, 5`) ahora es la segunda columna.

### Propiedades de la traspuesta

Son **cuatro propiedades** que hay que manejar.

#### Propiedad 1: doble traspuesta vuelve a la original

Sea `A` perteneciente a `M_mxn(R)`. Se cumple:

```
(A^T)^T = A
```

> "Yo transpongo la matriz, la vuelvo a transponer y vuelvo a la matriz original"

**Traduccion:** Trasponer dos veces "deshace" la operacion. Es como dar vuelta una hoja y volverla a dar vuelta.

#### Propiedad 2: la traspuesta de una suma es la suma de las traspuestas

Sean `A, B` pertenecientes a `M_mxn(R)`. Se cumple:

```
(A + B)^T = A^T + B^T
```

**Traduccion:** Es lo mismo sumar dos matrices y trasponer el resultado, que trasponer cada una y despues sumar. El orden no importa entre suma y traspuesta.

#### Propiedad 3: el escalar sale de la traspuesta

Sea `A` perteneciente a `M_mxn(R)` y `α` perteneciente a los reales. Se cumple:

```
(α * A)^T = α * A^T
```

> "Primero, en mi caso, en la izquierda, multiplico alfa por A y luego la transpongo, y aca ya multiplico directamente por la matriz traspuesta"

**Traduccion:** Si tenes un numero multiplicando una matriz, podes trasponer la matriz primero o el producto entero - da lo mismo.

**Error comun que el profesor advirtio:**

> "A veces ponen alfa por a traspuesta igual a alfa traspuesta por a traspuesta. Alfa es un numero, no podemos transponerlo. Es un escalar."

**Traduccion:** No podes "trasponer" un numero. La traspuesta solo aplica a matrices. Escribir `α^T` no tiene sentido.

#### Propiedad 4: la traspuesta de un producto invierte el orden

Sea `A` perteneciente a `M_mxn(R)`, `B` perteneciente a `M_nxp(R)`. Se cumple:

```
(A * B)^T = B^T * A^T
```

> "Esto esta mal porque las matrices no conmutan. B traspuesta por A traspuesta probablemente sea distinto a A traspuesta por B traspuesta"

**Traduccion:** Cuando trasponemos un producto, **el orden se invierte**. Es `B^T * A^T`, no `A^T * B^T`. No podes mantener el orden porque, como ya vimos, las matrices no conmutan.

**Analogia:** Pensalo como ponerte medias y zapatos. Para ponertelos: primero medias, despues zapatos. Para sacartelos: primero zapatos, despues medias. **El orden se invierte** al deshacer.

**Error comun:**

> "A veces ponen A por B traspuesta igual a A traspuesta por B traspuesta. Esto esta mal."

**Traduccion:** Mantener el orden original es el error mas frecuente. **Siempre** se invierte.

---

## Matrices Simetricas

### Definicion

Sea `A` perteneciente a `M_nxn(R)` (cuadrada). Decimos que `A` es **simetrica** si y solo si:

```
A^T = A
```

Es decir, la matriz es igual a su propia traspuesta.

Que significa eso?
- Si `A^T = A`, entonces cada entrada `a_ij` tiene que ser igual a `a_ji` (la entrada en la posicion espejada respecto a la diagonal).
- Formalmente: `a_ij = a_ji` para todo `i, j`.
- En palabras: hay **simetria respecto a la diagonal principal**.

### Ejemplo

```
A = | 1  4  6 |
    | 4  2  5 |
    | 6  5  3 |
```

Verifiquemos: la primera fila es `(1, 4, 6)` y la primera columna es tambien `(1, 4, 6)`. La segunda fila `(4, 2, 5)` coincide con la segunda columna. La tercera fila `(6, 5, 3)` con la tercera columna. Es simetrica.

**Caso especial:** las matrices diagonales **siempre** son simetricas, porque al trasponer la diagonal queda igual y todo lo demas es cero.

---

## Matrices Antisimetricas

### Definicion

Sea `A` perteneciente a `M_nxn(R)`. Decimos que `A` es **antisimetrica** si y solo si:

```
A^T = -A
```

Es decir, trasponer la matriz es lo mismo que multiplicarla por `-1`.

Formalmente: `a_ij = -a_ji` para todo `i, j`.

### Consecuencia clave: la diagonal es nula

> "Si yo transpongo es lo mismo que multiplicar por menos uno, y ya hemos dicho que si transpongo la diagonal principal no me cambia. Entonces el unico numero que es igual a su negativo es el cero, y por eso siempre que tengamos una matriz antisimetrica la diagonal principal es toda nula"

**Traduccion:** Las entradas de la diagonal cumplen `a_ii = -a_ii` (porque `i = j`, asi que la entrada es igual a su propia negativa). El unico numero que cumple esto es `0`. Por lo tanto, **toda matriz antisimetrica tiene diagonal principal nula**.

### Ejemplo

```
A = |  0   2   4 |
    | -2   0   6 |
    | -4  -6   0 |
```

La diagonal es toda cero. Las entradas espejadas son opuestas: `a_12 = 2` y `a_21 = -2`; `a_13 = 4` y `a_31 = -4`; `a_23 = 6` y `a_32 = -6`.

Verificamos `A^T`:

```
A^T = |  0  -2  -4 |
      |  2   0  -6 |
      |  4   6   0 |
```

Y `-A`:

```
-A = |  0  -2  -4 |
     |  2   0  -6 |
     |  4   6   0 |
```

Coinciden, asi que `A^T = -A`. Es antisimetrica.

---

## Propiedades de Simetricas y Antisimetricas

Cuatro propiedades importantes:

1. Si `A, B` simetricas, entonces `A + B` es simetrica.
2. Si `A` simetrica y `α` real, entonces `α * A` es simetrica.
3. Si `A, B` antisimetricas, entonces `A + B` es antisimetrica.
4. Si `A` antisimetrica y `α` real, entonces `α * A` es antisimetrica.

### Demostracion: la suma de simetricas es simetrica

**Hipotesis:** `A^T = A` y `B^T = B` (las dos son simetricas).

**Tesis:** `(A + B)^T = A + B` (la suma es simetrica).

**Demostracion:**

```
(A + B)^T = A^T + B^T          (propiedad 2 de la traspuesta)
          = A + B               (aplicamos hipotesis: A^T = A, B^T = B)
```

Como `(A + B)^T = A + B`, queda demostrado que la suma es simetrica.

### Demostracion: el producto escalar de una simetrica es simetrico

**Hipotesis:** `A^T = A` y `α` real.

**Tesis:** `(α * A)^T = α * A`.

**Demostracion:**

```
(α * A)^T = α * A^T            (propiedad 3 de la traspuesta)
          = α * A               (aplicamos hipotesis: A^T = A)
```

Queda demostrado.

---

## Ejercicio 5.2 del Practico: AB Simetrica si y solo si A y B Conmutan

### Enunciado

Sean `A, B` matrices simetricas `n x n`. Demostrar que `A * B` es simetrica **si y solo si** `A * B = B * A` (es decir, A y B conmutan).

### Que significa "si y solo si"

> "Cuando es un si solo si, esto despues lo vamos a ver en el practico, tenemos que probar el directo y el reciproco"

**Traduccion:** Un "si y solo si" requiere demostrar **dos cosas**:
- **Directo (=>):** Si `A * B` es simetrica, entonces `A` y `B` conmutan.
- **Reciproco (<=):** Si `A` y `B` conmutan, entonces `A * B` es simetrica.

Si solo demostras uno de los dos lados, **estarias haciendo el 50% del ejercicio**.

### Demostracion del directo (=>)

**Hipotesis:** `A^T = A`, `B^T = B`, `(AB)^T = AB` (`AB` es simetrica).

**Tesis:** `A * B = B * A`.

**Demostracion:**

```
A * B = (A * B)^T            (por hipotesis: AB es simetrica)
      = B^T * A^T            (propiedad 4 de la traspuesta - INVIERTE el orden)
      = B * A                 (por hipotesis: A^T = A, B^T = B)
```

Por lo tanto `A * B = B * A`. Conmutan.

### Demostracion del reciproco (<=)

**Hipotesis:** `A^T = A`, `B^T = B`, `A * B = B * A`.

**Tesis:** `(AB)^T = AB` (es decir, `AB` es simetrica).

**Demostracion:**

```
(A * B)^T = B^T * A^T        (propiedad 4 de la traspuesta)
          = B * A             (por hipotesis: A y B simetricas)
          = A * B             (por hipotesis: A y B conmutan)
```

Por lo tanto `(AB)^T = AB`, asi que `AB` es simetrica.

> "Al final de la demostracion se pone este simbolo, que significa lo que queda demostrado"

**Traduccion:** El simbolo `∎` o "QED" o cualquier marca al final indica "demostracion terminada".

---

## Ejercicio 6.1 del Practico: 1/2(A + A^T) es Simetrica

### Enunciado

Sea `A` perteneciente a `M_nxn(R)` (matriz cuadrada cualquiera, no necesariamente simetrica). Probar que `(1/2)(A + A^T)` es simetrica.

### Demostracion

**Tesis:** `((1/2)(A + A^T))^T = (1/2)(A + A^T)`.

**Desarrollo:**

```
((1/2) * (A + A^T))^T 
   = (1/2) * (A + A^T)^T          (propiedad 3: el escalar sale)
   = (1/2) * (A^T + (A^T)^T)      (propiedad 2: traspuesta de la suma)
   = (1/2) * (A^T + A)             (propiedad 1: doble traspuesta)
   = (1/2) * (A + A^T)             (conmutativa de la suma)
```

Llegamos a `(1/2)(A + A^T)`, que era lo que queriamos. Queda demostrado.

> "Al transponer aplicamos primero la propiedad 3, despues la 2, despues la 1, y al final la conmutativa de la suma"

**Traduccion:** En las demostraciones del parcial **hay que justificar cada paso** indicando que propiedad se uso. No alcanza con escribir las cuentas.

### Para que sirve este resultado

La parte 3 del ejercicio (que se queda como tarea) pide concluir que **toda matriz cuadrada se puede escribir como suma de una simetrica y una antisimetrica**:

```
A = (1/2)(A + A^T) + (1/2)(A - A^T)
        ↑               ↑
    simetrica       antisimetrica
```

Esta descomposicion va a aparecer en otros temas del curso.

---

## Traza de una Matriz

### Definicion

Sea `A` perteneciente a `M_nxn(R)` (cuadrada). La **traza de A**, notada `tr(A)`, es la **suma de los elementos de la diagonal principal**.

```
tr(A) = a_11 + a_22 + a_33 + ... + a_nn
```

O en notacion de sumatoria:

```
tr(A) = Σ (i=1 hasta n) a_ii
```

### Ejemplo

```
A = | 4  0  2 |
    | 1  1  3 |
    | 5  2  5 |
```

`tr(A) = 4 + 1 + 5 = 10`.

> "Solo la matriz cuadrada tiene traza, porque solo la cuadrada tiene diagonal principal"

**Traduccion:** Una matriz rectangular no tiene traza definida. Solo cuadradas.

### Propiedades de la traza

Cuatro propiedades, todas importantes.

#### Propiedad 1: traza de la suma

Sean `A, B` pertenecientes a `M_nxn(R)`. Se cumple:

```
tr(A + B) = tr(A) + tr(B)
```

#### Propiedad 2: traza del escalar por matriz

Sea `A` perteneciente a `M_nxn(R)`, `α` real. Se cumple:

```
tr(α * A) = α * tr(A)
```

#### Propiedad 3: traza de la traspuesta

Sea `A` perteneciente a `M_nxn(R)`. Se cumple:

```
tr(A^T) = tr(A)
```

> "Ven que habiamos visto que si tenemos una matriz y la transponemos la diagonal principal no cambia, entonces no va a cambiar la traza"

**Traduccion:** La traspuesta intercambia filas por columnas, pero la diagonal principal se queda donde estaba (porque las entradas `a_ii` tienen `i = j`, asi que su posicion no cambia). Por eso la suma de la diagonal es la misma.

#### Propiedad 4: traza del producto (la mas curiosa)

Sea `A` perteneciente a `M_mxn(R)`, `B` perteneciente a `M_nxm(R)`. Se cumple:

```
tr(A * B) = tr(B * A)
```

> "Es muy intuitivo eso, incluso si yo hago A por B me queda M por M, y si hago B por A me queda N por N. O sea tienen dimensiones distintas A,B y B,A. Son matrices distintas. Sin embargo sumo la diagonal principal y me da lo mismo."

**Traduccion:** Aunque `A * B` y `B * A` son matrices completamente distintas (incluso pueden tener dimensiones distintas si `A` no es cuadrada), **la suma de sus diagonales principales coincide**. Es un resultado muy curioso y va a ser clave para una demostracion famosa.

### Demostracion de la propiedad 1

**Hipotesis:** `A, B` cuadradas `n x n`.

**Tesis:** `tr(A + B) = tr(A) + tr(B)`.

**Demostracion:**

```
tr(A + B) = Σ (i=1 hasta n) (a_ii + b_ii)       (definicion de traza aplicada a A+B)
          = Σ a_ii + Σ b_ii                      (separamos la sumatoria)
          = tr(A) + tr(B)                        (definicion de traza)
```

### Demostracion de la propiedad 2

**Demostracion:**

```
tr(α * A) = Σ (i=1 hasta n) (α * a_ii)          (definicion de traza)
          = α * Σ a_ii                            (sacamos el escalar afuera)
          = α * tr(A)                             (definicion de traza)
```

---

## Anuncios al Final de Clase

- La primera prueba de evaluacion continua sera el **miercoles 25-03-2026**, en horario de clase, a las **9:30 PM**.
- Formato: media hora, presencial, grupos hasta 3 (entrega individual), con material y dispositivos electronicos pero **sin celular**.
- Contenido: ejercicio similar al practico.
- Tarea: avanzar con los ejercicios 5.2, 6.2 y 7.1 del practico.

---

# Clase 3 - 24 de Marzo de 2026: Matriz Inversa, Induccion Completa y Demostraciones con Trazas

## La Gran Pregunta de Hoy: Si no existe "dividir" entre matrices, ¿como se "deshace" una multiplicacion de matrices?

En los numeros reales, si tenemos `3 * x = 6`, dividimos ambos lados por `3` y obtenemos `x = 2`. Pero en matrices **no existe la division**. Entonces, ¿como despejamos una matriz cuando esta "atrapada" en un producto? La respuesta es la **matriz inversa**: una matriz especial que, al multiplicarla por la original, da la identidad (el equivalente al `1` en numeros). Esta clase gira alrededor de esa idea: definir que es la inversa, como encontrarla, que propiedades tiene, y como usarla para resolver problemas que van desde despejar ecuaciones matriciales hasta elevar matrices a potencias enormes como `2019`.

---

## Conexion con la Clase Anterior

En la clase del 18-03 vimos la **traspuesta** (intercambiar filas por columnas), las **matrices simetricas** (`A^T = A`) y **antisimetricas** (`A^T = -A`), y la **traza** (suma de la diagonal principal) con sus cuatro propiedades. Se enfatizo que la traspuesta de un producto **invierte el orden**: `(A * B)^T = B^T * A^T`. Esa inversion de orden va a reaparecer hoy con la inversa. Tambien se demostro que `tr(A * B) = tr(B * A)` - propiedad que hoy se va a usar en una demostracion por el absurdo.

---

## Definicion de Matriz Inversa

### Que es una matriz invertible

> "Siempre que hablamos de matriz inversa estamos en matrices cuadradas"

**Traduccion:** La inversa solo tiene sentido para matrices cuadradas (`n x n`). No se habla de inversa para matrices rectangulares.

Formalmente: sea `A` perteneciente a `M_nxn(R)`. Diremos que `A` es **invertible** (o que "tiene inversa") si y solo si existe una matriz `B` tal que:

```
A * B = B * A = I
```

Que significa esto?
- `A` = la matriz original
- `B` = la matriz que estamos buscando
- `I` = la matriz identidad
- La formula completa dice: si multiplicamos A por B (en cualquier orden) y obtenemos la identidad, entonces B es la inversa de A.

La notacion para la inversa de `A` es `A^(-1)` ("A a la menos uno"). Es **solamente notacion**, no significa elevar a una potencia negativa en sentido aritmetico.

> "Si existe esa matriz B, le llamamos B la inversa de A, y la notacion es A a la menos uno"

**Analogia:** En los reales, el inverso de `3` es `1/3`, porque `3 * (1/3) = 1`. En matrices, la inversa de `A` es `A^(-1)`, porque `A * A^(-1) = I`. Pero puede pasar que una matriz **no tenga inversa** - asi como el `0` no tiene inverso multiplicativo en los reales.

---

## Metodo Directo para Hallar la Inversa

### Planteamiento general

El **metodo directo** consiste en:
1. Plantear una matriz generica `B` con variables como entradas.
2. Multiplicar `A * B`.
3. Igualar el resultado a la identidad `I`.
4. Resolver el sistema de ecuaciones que resulta.
5. Si el sistema tiene solucion: la inversa existe y es esa solucion. Si no tiene solucion: la matriz no es invertible.

> "Queremos hallar una matriz B que la multiplico por A y me da la identidad"

### Ejemplo 1: matriz invertible (2x2)

Sea la matriz:

```
A = | 1   2 |
    | 3  -4 |
```

Planteamos `A * B = I`:

```
| 1   2 | * | a  b | = | 1  0 |
| 3  -4 |   | c  d |   | 0  1 |
```

Hacemos el producto del lado izquierdo:

```
| a + 2c    b + 2d  | = | 1  0 |
| 3a - 4c   3b - 4d |   | 0  1 |
```

Igualamos entrada a entrada y obtenemos el sistema de 4 ecuaciones con 4 incognitas:

```
(1)  a + 2c  = 1
(2)  b + 2d  = 0
(3)  3a - 4c = 0
(4)  3b - 4d = 1
```

Para resolver, hacemos `-3 * (1) + (3)`:
- Se cancelan las `a`: `-3a + 3a = 0`
- Queda: `-6c - 4c = -10c`
- Del otro lado: `-3 + 0 = -3`
- Entonces: `c = 3/10`

Con `c = 3/10`, de la ecuacion (1): `a = 1 - 2(3/10) = 1 - 6/10 = 4/10 = 2/5`

Analogamente, `-3 * (2) + (4)` nos da: `-10d = 1`, entonces `d = -1/10`.

Con `d = -1/10`, de la ecuacion (2): `b = -2(-1/10) = 2/10 = 1/5`

Por lo tanto:

```
A^(-1) = | 2/5    1/5  |
         | 3/10  -1/10 |
```

### Ejemplo 2: matriz NO invertible (2x2)

Sea la matriz:

```
C = | 1  2 |
    | 2  4 |
```

Planteamos el mismo sistema:

```
| 1  2 | * | a  b | = | 1  0 |
| 2  4 |   | c  d |   | 0  1 |
```

El sistema que resulta es:

```
(1)  a + 2c = 1
(2)  b + 2d = 0
(3)  2a + 4c = 0
(4)  2b + 4d = 1
```

Si hacemos `-2 * (1) + (3)`:
- Se cancelan las `a` y las `c`: `0 = 0` para esos terminos
- Queda: `0 = -2`

> "Si llegamos a esto, el sistema no tiene solucion"

**Traduccion:** `0 = -2` es una contradiccion. Significa que **no existen** numeros `a, b, c, d` que satisfagan las cuatro ecuaciones simultaneamente. Por lo tanto, **no existe la inversa**. La matriz `C` no es invertible.

**Observacion sobre dimensiones:** este metodo funciona para cualquier dimension. En `3x3` la matriz generica tiene 9 entradas y el sistema tiene 9 ecuaciones. En `4x4` son 16. El planteamiento es el mismo, solo cambia la cantidad de cuentas.

> "Por ahora este es el metodo que tenemos"

**Traduccion:** Mas adelante (despues de Semana de Turismo) se veran otros metodos para hallar la inversa: mediante el **determinante** y mediante **sistemas de ecuaciones** (escalonamiento). Por ahora, el unico metodo disponible es el directo.

---

## Propiedades de la Inversa

Sea `A` perteneciente a `M_nxn(R)`, `A` invertible.

### Propiedad 1: la inversa es unica

Si existe una matriz `B` tal que `A * B = B * A = I`, esa matriz `B` es la unica con esa propiedad.

### Propiedad 2: doble inversa vuelve a la original

```
(A^(-1))^(-1) = A
```

> "Si a la matriz le hago la inversa, y a la inversa le vuelvo a hacer la inversa, vuelvo a la matriz original"

**Traduccion:** La inversa de la inversa es la matriz original. Es como deshacer el "deshacer".

**Analogia:** El inverso multiplicativo de `3` es `1/3`. El inverso multiplicativo de `1/3` es `3`. Volves al numero original. Igual que la traspuesta: `(A^T)^T = A`.

### Propiedad 3: la inversa de un producto invierte el orden

```
(A * B)^(-1) = B^(-1) * A^(-1)
```

> "La inversa de A por B es igual a B inversa por A inversa"

> "Esto no es igual a la inversa de A por la inversa de B porque no conmutan"

**Traduccion:** Cuando tomas la inversa de un producto de matrices, el resultado es el producto de las inversas **pero en orden invertido**. Primero va `B^(-1)` y despues `A^(-1)`, al reves de como estaban. **No** podes escribir `A^(-1) * B^(-1)` porque las matrices no conmutan.

**Analogia (igual que con la traspuesta):** Medias y zapatos. Para sacartelos, el orden se invierte.

### Demostracion de la Propiedad 3

Queremos probar que `(A * B)^(-1) = B^(-1) * A^(-1)`.

**Estrategia:** multiplicamos `A * B` por `B^(-1) * A^(-1)` y mostramos que da la identidad.

```
(A * B) * (B^(-1) * A^(-1))
= A * (B * B^(-1)) * A^(-1)      (asociativa)
= A * I * A^(-1)                  (definicion de inversa: B * B^(-1) = I)
= A * A^(-1)                      (I es neutro del producto)
= I                                (definicion de inversa: A * A^(-1) = I)
```

Como el producto dio la identidad, queda demostrado que `B^(-1) * A^(-1)` es la inversa de `A * B`.

> "No podes mover el A inversa... acuerdate que no conmuta, no podes cambiar el orden"

**Traduccion:** Un estudiante pregunto si se podia "pasar" `A^(-1)` al otro lado. La respuesta es **NO**: como el producto de matrices no es conmutativo, **jamas** se puede cambiar el orden de los factores. Siempre hay que multiplicar del mismo lado en ambos miembros de la igualdad.

---

## Matrices Idempotentes

### Definicion

Sea `A` perteneciente a `M_nxn(R)`. Decimos que `A` es **idempotente** si y solo si:

```
A^2 = A
```

Que significa esto?
- `A^2` = `A * A` (la matriz multiplicada por si misma)
- Si multiplicas la matriz por si misma y te queda exactamente igual, es idempotente.

**Analogia:** En los reales, los unicos numeros que cumplen `x^2 = x` son `0` y `1`. En matrices pasa algo parecido pero hay mas opciones.

### Demostracion: si A es idempotente e invertible, entonces A = I

**Hipotesis:** `A^2 = A` y `A` es invertible (existe `A^(-1)`).

**Tesis:** `A = I`.

> "Como existe la inversa de A, puedo multiplicar por la inversa a ambos lados"

**Demostracion:**

```
A^2 = A                            (hipotesis: idempotente)
A * A = A                          (reescribimos A^2 como A*A)
A^(-1) * (A * A) = A^(-1) * A     (multiplicamos por A^(-1) por la IZQUIERDA)
(A^(-1) * A) * A = I               (asociativa + definicion de inversa)
I * A = I                           (definicion de inversa)
A = I                               (I es neutro)
```

Por lo tanto `A = I`.

**Punto clave del profesor:** siempre que multiplicas por la inversa, tiene que ser **del mismo lado** en ambos miembros de la igualdad. Si multiplicas por la izquierda en un lado, multiplicas por la izquierda en el otro. **Nunca mezclar.**

### Ejemplo de matriz idempotente que no es la identidad

La **matriz nula** es idempotente: `O * O = O`.

Tambien esta matriz `2x2`:

```
A = | 1  0 |
    | 0  0 |
```

Verificacion: `A * A = A` (se puede comprobar multiplicando entrada a entrada).

**Notar:** estas matrices **no son invertibles** - lo cual es coherente con la demostracion anterior. La unica matriz que es **idempotente E invertible** es la identidad.

---

## Ejercicio Clave: Si A^3 = O, entonces (A + I) es Invertible

### Parte 1: demostracion

**Hipotesis:** `A` perteneciente a `M_nxn(R)` tal que `A^3 = O` (la matriz nula).

**Tesis:** `A + I` es invertible, y `(A + I)^(-1) = A^2 - A + I`.

> "Si queremos probar que esta matriz es la inversa de esta otra, tengo que multiplicarlas y ver que el resultado me da la identidad"

**Multiplicamos** `(A + I)` por `(A^2 - A + I)` y aplicamos la **distributiva**:

```
(A + I) * (A^2 - A + I)
= A * A^2 - A * A + A * I + I * A^2 - I * A + I * I
= A^3 - A^2 + A + A^2 - A + I
```

Notas sobre cada termino:
- `A * A^2 = A^3`
- `A * (-A) = -A^2`
- `A * I = A`
- `I * A^2 = A^2`
- `I * (-A) = -A`
- `I * I = I`

Simplificamos:
- `A^2` y `-A^2` se cancelan
- `A` y `-A` se cancelan
- Queda: `A^3 + I`

Aplicamos la hipotesis (`A^3 = O`):

```
= O + I = I
```

Como el producto dio la identidad, queda demostrado que `(A + I)^(-1) = A^2 - A + I`.

> "Si probaste que esta es la inversa, estas probando las dos cosas a la misma vez"

**Traduccion:** Al encontrar una matriz que multiplicada da la identidad, estas simultaneamente probando que es invertible **Y** cual es su inversa. No hay que probar primero que existe.

### Parte 2: aplicacion a una matriz 4x4 concreta

Hallar la inversa de la matriz:

```
B = | 1  1  0  0 |
    | 0  1  0  1 |
    | 0  0  1  0 |
    | 0  0  0  1 |
```

**Paso 1:** identificar `A`.

Si `B = A + I`, entonces `A = B - I`:

```
A = | 0  1  0  0 |
    | 0  0  0  1 |
    | 0  0  0  0 |
    | 0  0  0  0 |
```

**Paso 2:** verificar que `A^3 = O`.

Calculamos `A^2`:

```
A^2 = | 0  0  0  1 |
      | 0  0  0  0 |
      | 0  0  0  0 |
      | 0  0  0  0 |
```

Luego `A^3 = A^2 * A`:

```
A^3 = | 0  0  0  0 |
      | 0  0  0  0 | = O   (matriz nula)
      | 0  0  0  0 |
      | 0  0  0  0 |
```

`A^3 = O`, asi que estamos en la hipotesis.

**Paso 3:** calcular la inversa como `A^2 - A + I`:

```
B^(-1) = | 1  -1  0   1 |
         | 0   1  0  -1 |
         | 0   0  1   0 |
         | 0   0  0   1 |
```

> "La clave aca es darnos cuenta que estamos en la hipotesis"

**Traduccion:** Lo mas importante del ejercicio no son las cuentas, sino el **razonamiento**: identificar que la matriz dada se puede expresar como `A + I`, verificar que `A^3 = O`, y recien entonces aplicar la formula.

---

## Demostracion por Induccion Completa

### Que es la induccion completa

La induccion completa tiene **tres pasos**:

1. **Paso base:** verificar que la propiedad se cumple para el minimo valor de `n` (generalmente `n = 1`).
2. **Hipotesis inductiva:** suponer que se cumple para `n = h`.
3. **Tesis inductiva + Demostracion:** probar que, si se cumple para `h`, entonces se cumple para `h + 1`.

**Analogia:** Es como una fila infinita de fichas de domino. El paso base es empujar la primera ficha. La hipotesis y la tesis dicen: "si la ficha `h` cae, la ficha `h+1` tambien cae". Si ambas cosas son ciertas, **todas** las fichas caen.

### Ejemplo 1: potencia de una matriz 2x2

**Enunciado:** Sea `A = [[1, 1], [0, 1]]`. Demostrar por induccion completa que:

```
A^n = | 1  n |
      | 0  1 |
```

**Paso base** (`n = 1`):

```
A^1 = | 1  1 |
      | 0  1 |
```

Sustituimos `n = 1` en la formula: `[[1, 1], [0, 1]]`. Coincide. El paso base se cumple.

**Hipotesis inductiva** (se cumple para `n = h`):

```
A^h = | 1  h |
      | 0  1 |
```

**Tesis** (se cumple para `n = h + 1`):

```
A^(h+1) = | 1  h+1 |
          | 0  1   |
```

**Demostracion:**

```
A^(h+1) = A^h * A                                  (propiedad de potencias)

        = | 1  h | * | 1  1 |                       (sustituimos por la hipotesis)
          | 0  1 |   | 0  1 |

        = | 1*1+h*0   1*1+h*1 |                     (multiplicamos)
          | 0*1+1*0   0*1+1*1 |

        = | 1  1+h |
          | 0  1   |
```

Llegamos a `[[1, h+1], [0, 1]]`, que es la tesis. Queda demostrado.

### Ejemplo 2: potencia de una matriz diagonal

**Enunciado:** Si `A` es una matriz **diagonal** `n x n`, demostrar que:

```
A^k = | a_11^k    0      ...    0     |
      |   0     a_22^k   ...    0     |
      |  ...     ...     ...   ...    |
      |   0       0      ...  a_nn^k  |
```

Es decir, elevar una matriz diagonal a la `k` es lo mismo que elevar a la `k` cada elemento de la diagonal principal.

**Paso base** (`k = 1`): trivial, `A^1 = A` y al sustituir `k=1` en la formula obtenemos `A`.

**Hipotesis inductiva** (`k = h`): asumimos que `A^h` es diagonal con entradas `a_ii^h`.

**Demostracion para `k = h + 1`:**

```
A^(h+1) = A^h * A
```

Como ambas son diagonales, al multiplicarlas cada entrada de la diagonal del resultado es el producto de las entradas correspondientes:

```
= | a_11^h * a_11    0            ...    0             |
  |   0            a_22^h * a_22  ...    0             |
  |  ...            ...           ...   ...            |
  |   0              0            ...  a_nn^h * a_nn   |
```

Por propiedad de potencias, `a_ii^h * a_ii = a_ii^(h+1)`:

```
= | a_11^(h+1)    0          ...    0           |
  |   0         a_22^(h+1)   ...    0           |
  |  ...         ...         ...   ...          |
  |   0           0          ...  a_nn^(h+1)    |
```

Llegamos a la tesis. Queda demostrado.

---

## Ejercicio: A^2 = 4I

### Parte 1: probar que (A - I) es invertible y su inversa es (1/3)(A + I)

**Hipotesis:** `A^2 = 4I`.

**Tesis:** `(A - I)^(-1) = (1/3)(A + I)`.

**Estrategia:** multiplicamos `(A - I)` por `(1/3)(A + I)` y mostramos que da la identidad.

> "El un tercio lo puedo sacar para afuera"

**Traduccion:** Por la propiedad `B * (k * A) = k * (B * A)`, podemos sacar el escalar `1/3` afuera del producto.

```
(A - I) * (1/3)(A + I) = (1/3) * (A - I) * (A + I)
```

Aplicamos distributiva:

```
(A - I) * (A + I) = A^2 + A * I - I * A - I^2
                  = A^2 + A - A - I
                  = A^2 - I
```

**Nota importante:** `A * I = A` y `I * A = A` - la identidad **conmuta con todas las matrices**. Por eso `A * I - I * A = 0`.

Aplicamos la hipotesis (`A^2 = 4I`):

```
= (1/3) * (4I - I)
= (1/3) * 3I
= I
```

Como el producto dio la identidad: `(A - I)^(-1) = (1/3)(A + I)`.

### Parte 2: aplicacion concreta

Dadas:

```
A = | 8/5    6/5  |       B = | 3/5    6/5  |
    | 6/5   -8/5  |           | 6/5   -3/5  |
```

**Verificar que `A^2 = 4I`:**

```
A * A = | (8/5)^2 + (6/5)^2          (8/5)(6/5) + (6/5)(-8/5)  |
        | (6/5)(8/5) + (-8/5)(6/5)   (6/5)^2 + (-8/5)^2        |

      = | 64/25 + 36/25    48/25 - 48/25  |
        | 48/25 - 48/25    36/25 + 64/25  |

      = | 100/25    0    |   | 4  0 |
        |   0    100/25  | = | 0  4 | = 4I
```

Se cumple la hipotesis.

**Observar que `B = A - I`:**

```
A - I = | 8/5 - 1    6/5         |   | 3/5    6/5  |
        | 6/5       -8/5 - 1    | = | 6/5   -13/5 |
```

(El profesor corrigio durante la clase la entrada `(2,2)` a `-3/5` para que coincida con `B`.)

**Calcular la inversa:**

```
B^(-1) = (1/3)(A + I)
```

Donde:

```
A + I = | 13/5   6/5  |
        | 6/5   -3/5  |
```

Entonces:

```
B^(-1) = (1/3) * | 13/5   6/5  | = | 13/15   2/5  |
                  | 6/5   -3/5  |   | 2/5    -1/5  |
```

> "La clave estaba en darse cuenta que la matriz B era A menos la identidad"

**Traduccion:** El truco no es hacer cuentas - es **reconocer** que `B = A - I` y que `A^2 = 4I`, para poder usar la formula demostrada.

---

## Ejercicio: C = B^(-1) * A * B - Hallar C^2019

### Enunciado

Dadas:

```
A = | 1   0   0 |       B perteneciente a M_3x3(R), B invertible
    | 0  -1   0 |
    | 0   0   2 |

C = B^(-1) * A * B
```

Hallar `C^2019` en funcion de `B`, `B^(-1)`, y potencias de algun numero.

### Desarrollo: descubrir el patron

**C^2:**

```
C^2 = C * C = (B^(-1) * A * B) * (B^(-1) * A * B)
```

Aplicamos asociativa:

```
= B^(-1) * A * (B * B^(-1)) * A * B
= B^(-1) * A * I * A * B
= B^(-1) * A * A * B
= B^(-1) * A^2 * B
```

La clave: `B * B^(-1) = I` se cancela en el medio.

**C^3:**

```
C^3 = C^2 * C = (B^(-1) * A^2 * B) * (B^(-1) * A * B)
              = B^(-1) * A^3 * B
```

**Patron general:**

```
C^n = B^(-1) * A^n * B
```

Por lo tanto:

```
C^2019 = B^(-1) * A^2019 * B
```

### Calcular A^2019

`A` es **diagonal**, asi que por induccion completa, elevarla a 2019 es elevar cada entrada de la diagonal:

```
A^2019 = | 1^2019      0           0       |   | 1    0       0      |
         |    0     (-1)^2019      0       | = | 0   -1       0      |
         |    0         0       2^2019     |   | 0    0    2^2019    |
```

- `1^2019 = 1`
- `(-1)^2019 = -1` (porque 2019 es **impar**)
- `2^2019` queda como esta

**Resultado final:**

```
C^2019 = B^(-1) * | 1    0       0      | * B
                   | 0   -1       0      |
                   | 0    0    2^2019    |
```

> "Solo con C cuadrado y C cubo ya podes generalizar"

**Traduccion:** Como la letra pide "hallar una expresion" y no "demostrar", basta con ver el patron en los primeros casos. No hace falta hacer induccion completa formal.

---

## Propiedades de la Traza: tr(A - B) = tr(A) - tr(B)

### Demostracion

**Propiedad conocida 1:** `tr(A + B) = tr(A) + tr(B)`.

**Propiedad conocida 2:** `tr(α * A) = α * tr(A)`.

```
tr(A - B) = tr(A + (-1) * B)            (reescribimos como suma)
          = tr(A) + tr((-1) * B)         (propiedad 1)
          = tr(A) + (-1) * tr(B)         (propiedad 2 con α = -1)
          = tr(A) - tr(B)
```

### Verificacion con ejemplo numerico

```
A = | 1  0  2 |       B = | 2  1  0 |
    | 1  2  1 |           | 0  1  3 |
    | 0  3  2 |           | 2  1  1 |
```

- `tr(A) = 1 + 2 + 2 = 5`
- `tr(B) = 2 + 1 + 1 = 4`

```
A - B = | -1  -1   2 |
        |  1   1  -2 |
        | -2   2   1 |
```

- `tr(A - B) = -1 + 1 + 1 = 1`

Verificamos: `tr(A) - tr(B) = 5 - 4 = 1`. Coincide.

---

## Demostracion por el Absurdo: No Existen A, B tales que AB - BA = I

### Que es probar por el absurdo

> "Vamos a suponer que el enunciado es cierto, y si llegamos a una contradiccion, es que no puede ser cierto"

**Traduccion:** Asumimos que SI existen las matrices. Si esa suposicion lleva a algo imposible, entonces nuestra suposicion era falsa.

### Demostracion

**Supongamos** que existen `A, B` tales que `A * B - B * A = I`.

Tomamos la traza de ambos lados:

**Lado derecho:**

```
tr(I) = 1 + 1 + ... + 1 = n     (la identidad tiene n unos en la diagonal)
```

**Lado izquierdo:**

```
tr(A * B - B * A) = tr(A * B) - tr(B * A)     (propiedad de la traza demostrada hoy)
```

Pero por la propiedad 4 de la traza vista en clase 2:

```
tr(A * B) = tr(B * A)        (siempre se cumple)
```

> "A por B es una matriz, B por A es otra, pero sumo las diagonales principales y me da lo mismo. Es algo bastante curioso."

Entonces:

```
tr(A * B) - tr(B * A) = tr(A * B) - tr(A * B) = 0
```

Pero dijimos que debia ser igual a `n`:

```
0 = n
```

Esto es una **contradiccion** (porque `n >= 1`). Por lo tanto, la suposicion era falsa.

**Conclusion:** No existen matrices `A, B` en `M_nxn(R)` tales que `A * B - B * A = I`.

---

## Despeje de Ecuaciones Matriciales

### Ejercicio: dado AX + X = 2A, hallar X en funcion de A

> "Acuerdense que X es una matriz, no puedo pasar X dividiendo"

> "Lo que es analogo a pasar una matriz dividiendo es multiplicar por la inversa"

**Traduccion:** En matrices **no existe la division**. El equivalente es multiplicar por la inversa del lado correspondiente.

**Paso 1:** factorizar X.

```
A * X + X = 2A
```

Queremos sacar factor comun `X`. Pero `X` aparece multiplicada por `A` a la izquierda y "sola" (que es lo mismo que multiplicada por `I`):

```
A * X + I * X = 2A
(A + I) * X = 2A
```

**Error comun que el profesor advirtio:**

> "No puedo sumar un numero a una matriz, tengo que factorizar con la identidad"

**Traduccion:** Algunos estudiantes escriben `(A + 1)` - esto esta **MAL**. No se puede sumar un numero a una matriz. Hay que escribir `(A + I)`, donde `I` es la matriz identidad.

**Otro error comun:** Escribir `X * (A + I)` en vez de `(A + I) * X`. Esto cambia el orden y, como las matrices no conmutan, el resultado es distinto.

**Paso 2:** multiplicar por la inversa de `(A + I)` para despejar X.

Multiplicamos por `(A + I)^(-1)` **por la izquierda** en ambos lados:

```
(A + I)^(-1) * (A + I) * X = (A + I)^(-1) * 2A
I * X = (A + I)^(-1) * 2A
X = (A + I)^(-1) * 2A
```

> "Tengo que multiplicar por la izquierda, asi esto me queda la identidad"

**Traduccion:** Multiplicamos por la izquierda porque `(A + I)` esta a la izquierda de `X`. Si multiplicaramos por la derecha, no se cancelaria.

> "Si vos tenes algo y algo a la menos uno, ese producto te da la identidad"

**Traduccion:** No importa que haya dentro del parentesis - cualquier expresion `(M)` multiplicada por `(M)^(-1)` da la identidad.

---

## Anuncios al Final de Clase

- **Prueba de evaluacion continua manana (25-03-2026):** nivel basico, con material, grupos de hasta 3 personas, duracion 30 minutos, empieza 9:30 PM.
- **Contenido de la prueba:** todo lo visto de matrices (NO incluye induccion completa ni determinantes).
- **Determinantes:** se veran despues de las vacaciones de Semana de Turismo.
- Con esta clase **se completa el teorico de matrices**.

---

# Clase 4 - 25 de Marzo de 2026: Practica para la Evaluacion Continua

## La Gran Pregunta de Hoy: ¿Como aplicamos todo lo visto a ejercicios concretos antes de la prueba?

Esta es una clase corta y casi exclusivamente practica - el profesor dedica el tiempo previo a la prueba de evaluacion continua (que es en la misma clase a las 9:30 PM) a resolver tres ejercicios clave: **uno de despeje de inversa por factorizacion**, **uno de matriz idempotente** (verificar una identidad usando que `A^2 = A`), **uno de invertir una matriz 3x3 con dos metodos** (factorizacion y metodo directo). Tambien repasa los ejercicios 7, 8 y 11 del practico, e introduce informalmente el concepto de **matriz ortogonal** (la inversa coincide con la traspuesta).

---

## Conexion con la Clase Anterior

En la clase del 24-03 cerramos el teorico de matrices con la **inversa** (definicion, metodo directo, propiedades), las **matrices idempotentes**, la **induccion completa** y la **demostracion por absurdo de que `AB - BA ≠ I`**. Hoy aplicamos todo eso a ejercicios concretos para preparar la prueba de evaluacion continua.

---

## Ejercicio 1: Si A^3 - A = I, entonces A es Invertible

### Enunciado

Sea `A` perteneciente a `M_3x3(R)` tal que `A^3 - A = I`. Probar que `A` es invertible y hallar su inversa.

### Estrategia

Necesitamos encontrar una matriz que multiplicada por `A` de la identidad. Por la definicion: si `A * algo = I`, entonces ese "algo" es `A^(-1)`.

### Desarrollo

Partimos de la hipotesis:

```
A^3 - A = I
```

Factorizamos `A` por la izquierda:

```
A * (A^2 - I) = I
```

> "Acuerdense que la identidad se puede expresar como A por A inversa"

**Traduccion:** Si `A * algo = I`, entonces ese "algo" es `A^(-1)` por definicion.

Por lo tanto:

```
A^(-1) = A^2 - I
```

`A` es invertible y su inversa es `A^2 - I`.

> "Si hago A por esa expresion, me da la identidad. Exacto."

**Traduccion:** El truco esta en factorizar inteligentemente la hipotesis para que quede de la forma `A * algo = I`. Recien ahi podemos identificar el "algo" como la inversa.

---

## Ejercicio 2: Matriz Idempotente, Probar (A + I)^3 = I + 7A

### Enunciado

Sea `A` perteneciente a `M_nxn(R)` idempotente (`A^2 = A`). Verificar que `(A + I)^3 = I + 7A`.

### Estrategia

> "O sea, lo que tenemos que hacer es bajar un grado. La idea es expandir y usar A^2 = A en cada paso"

**Traduccion:** Vamos a expandir `(A + I)^3` usando la distributiva. Cada vez que aparezca `A^2`, lo sustituimos por `A` (aplicando la hipotesis). El objetivo es reducir todas las potencias de `A` hasta dejar solo `A` y `I`.

### Desarrollo

**Paso 1:** expandir `(A + I)^3` como `((A + I)^2) * (A + I)`.

Calculamos primero `(A + I)^2`:

```
(A + I)^2 = (A + I)(A + I)
          = A * A + A * I + I * A + I * I
          = A^2 + A + A + I
          = A^2 + 2A + I
```

**Aplicamos la hipotesis** (`A^2 = A`):

```
(A + I)^2 = A + 2A + I = 3A + I
```

**Paso 2:** multiplicar por `(A + I)`.

```
(A + I)^3 = (3A + I)(A + I)
          = 3A * A + 3A * I + I * A + I * I
          = 3A^2 + 3A + A + I
          = 3A^2 + 4A + I
```

**Aplicamos la hipotesis de nuevo:**

```
= 3A + 4A + I
= 7A + I
= I + 7A             (conmutativa de la suma)
```

Llegamos a `I + 7A`, que era lo que queriamos. Queda verificado.

> "I por cualquier matriz da la misma matriz, y lo mismo para la identidad"

**Traduccion:** Cada vez que aparecio `A * I` o `I * A`, lo simplificamos a `A`. Es el neutro del producto.

---

## Ejercicio 8 del Practico: Verificar una Ecuacion y Hallar la Inversa

### Enunciado

Sea la matriz:

```
A = | 1   0   0 |
    | 0   2  -2 |
    | 0   0   3 |
```

Verificar que `-A^3 + 3A^2 + A - 3I = O` (matriz nula).

Despues, hallar `A^(-1)` por **dos metodos**:
1. A partir de la ecuacion anterior (factorizando).
2. Por el metodo directo.

### Parte 1: verificar la ecuacion (operativo)

Esta parte es 100% cuentas. Hay que calcular `A^2`, despues `A^3`, sustituir en la expresion, y comprobar que da la matriz nula. El profesor lo deja como tarea operativa para que practiquen calculo de potencias.

(Como referencia, `A^2` se calcula multiplicando `A * A`. Despues `A^3 = A^2 * A`. Despues se hace la suma final.)

### Parte 2 - Metodo 1: factorizar la ecuacion

Partimos de:

```
-A^3 + 3A^2 + A - 3I = O
```

**Paso 1:** pasar `-3I` al otro lado:

```
-A^3 + 3A^2 + A = 3I
```

**Paso 2:** factorizar `A` por la izquierda:

```
A * (-A^2 + 3A + I) = 3I
```

**Paso 3:** dividir por 3 (o multiplicar por `1/3`):

```
A * (1/3)(-A^2 + 3A + I) = I
```

Por definicion de inversa:

```
A^(-1) = (1/3)(-A^2 + 3A + I)
```

Una vez que tenemos esta expresion, basta sustituir `A^2` (que ya calculamos en la parte 1) y hacer las cuentas finales para obtener la matriz inversa numerica.

### Parte 2 - Metodo 2: metodo directo

Plantear `A * B = I` con `B` generica `3x3`:

```
A * | a  b  c | = | 1  0  0 |
    | d  e  f |   | 0  1  0 |
    | g  h  i |   | 0  0  1 |
```

Multiplicar y obtener un sistema de **9 ecuaciones con 9 incognitas**. El profesor desarrolla las primeras filas de la cuenta:

```
A * B = | a       b           c          |
        | -2d + 2g  -2e + 2h  -2f + 2i  |    
        | 3g       3h          3i        |
```

(Las ecuaciones son distintas a las del transcript pero el principio es el mismo: cada entrada del producto se iguala a la entrada correspondiente de la identidad.)

Resolver el sistema da los valores de las 9 incognitas, y con eso se reconstruye `A^(-1)`. Por supuesto, el resultado tiene que coincidir con el del metodo 1.

> "Le deberia dar lo mismo eso que por la parte anterior cuando echamos la expresion a la menos uno y sustituimos las matrices"

**Traduccion:** Los dos metodos deben dar exactamente la misma matriz inversa. Si no coinciden, hay un error en alguno de los dos.

> "Importante, no subestimen las cuentas porque despues en los parciales el tiempo no sobra y a veces tiene que estar como agil para las cuentas"

**Traduccion:** En el parcial el factor tiempo importa mucho. Practicar las cuentas a mano es necesario aunque parezca tedioso.

---

## Ejercicio 7 del Practico: Matriz Nilpotente

### Definicion de matriz nilpotente

> "La empiezo a multiplicar por si misma la matriz y en un momento se anula. Entonces a la k es la matriz nula y a la k menos 1 es distinta de la matriz nula. Ahi decimos que la matriz es nilpotente de grado k."

**Traduccion:** Una matriz `A` es **nilpotente de grado `k`** si:
- `A^k = O` (la matriz nula)
- `A^(k-1) ≠ O` (la potencia anterior **no** es nula)

Es decir, `k` es la **primera** potencia que la anula.

### Parte 1: averiguar el grado de nilpotencia

Sea:

```
A = | 0  1  1 |
    | 0  0  1 |
    | 0  0  0 |
```

Empezamos a multiplicar:
- `A^1 ≠ O`
- `A^2`: calcular `A * A` - resulta en una matriz con un solo `1` (no es nula)
- `A^3`: calcular `A^2 * A` - resulta en la matriz nula

**Conclusion:** `A` es nilpotente de **grado 3**.

### Parte 2: si P invertible, demostrar que P^(-1) * A * P es nilpotente del mismo grado

**Estrategia:** usar la misma idea del ejercicio `C^2019` de la clase anterior. Para una expresion del tipo `P^(-1) * A * P`, las potencias se simplifican en `P^(-1) * A^k * P`.

**Cuidado con el error tentador:**

> "Asociativo, va por ahi, no? Acuerdense que no conmuta, no podes hacer eso"

**Traduccion:** Un estudiante intento aplicar conmutativa para "cancelar" `P^(-1) * P` en posiciones que no estaban juntas. **Esta mal.** Solo se puede cancelar si las matrices estan **adyacentes** y en el orden correcto (`P * P^(-1)` o `P^(-1) * P`).

**Desarrollo:**

```
(P^(-1) * A * P)^2 = (P^(-1) * A * P) * (P^(-1) * A * P)
```

Por asociativa:

```
= P^(-1) * A * (P * P^(-1)) * A * P
= P^(-1) * A * I * A * P
= P^(-1) * A * A * P
= P^(-1) * A^2 * P
```

Analogamente:

```
(P^(-1) * A * P)^3 = P^(-1) * A^3 * P
```

Por la parte 1, `A^3 = O`. Entonces:

```
P^(-1) * A^3 * P = P^(-1) * O * P = O
```

**Conclusion:** `P^(-1) * A * P` es nilpotente de grado 3 (igual que `A`).

> "Por la asociativa vamos a expresarlo como P a la menos 1 por A cubo por P"

**Traduccion:** El patron es identico al del ejercicio `C^n = B^(-1) * A^n * B` que se vio en clase 3. La estructura `algo^(-1) * X * algo` "preserva" la potencia de X.

---

## Ejercicio 11 del Practico: Si A es Invertible y AB = A, entonces B = I

### Estrategia

Multiplicamos ambos lados por `A^(-1)` por la **izquierda**:

```
AB = A
A^(-1) * (AB) = A^(-1) * A
(A^(-1) * A) * B = I
I * B = I
B = I
```

Queda demostrado.

**Punto clave:** la condicion "**A invertible**" es necesaria. Si `A` no fuera invertible, no podriamos multiplicar por `A^(-1)`, y la conclusion ya no se sigue.

### Generalizacion: si AB = AC y A invertible, entonces B = C

```
AB = AC
A^(-1) * AB = A^(-1) * AC
(A^(-1) * A) * B = (A^(-1) * A) * C
I * B = I * C
B = C
```

**Si A no es invertible**, esto puede fallar. El profesor menciona que la parte 3 del ejercicio da un contraejemplo concreto donde `AB = AC` pero `B ≠ C` (porque `A` no es invertible).

---

## Concepto Adicional: Matriz Ortogonal

> "Una matriz ortogonal significa que la inversa coincide con la traspuesta"

**Traduccion:** Una matriz `A` es **ortogonal** si:

```
A^(-1) = A^T
```

Equivalentemente: `A * A^T = A^T * A = I`.

### Ejemplo de aplicacion

Dado:

```
A = | 4/5    α  |
    | 3/5    β  |
```

Hallar `α` y `β` para que `A` sea ortogonal.

**Estrategia:** plantear `A * A^T = I` y resolver el sistema.

`A^T`:

```
A^T = | 4/5   3/5 |
      |  α     β  |
```

Multiplicamos `A * A^T`:

```
A * A^T = | (4/5)^2 + α^2          (4/5)(3/5) + αβ  |
          | (4/5)(3/5) + αβ        (3/5)^2 + β^2    |

        = | 16/25 + α^2     12/25 + αβ |
          | 12/25 + αβ      9/25 + β^2 |
```

Igualamos a la identidad:

```
| 16/25 + α^2     12/25 + αβ |   | 1  0 |
| 12/25 + αβ      9/25 + β^2 | = | 0  1 |
```

Sistema de ecuaciones:

```
(1)  16/25 + α^2 = 1     →   α^2 = 9/25
(2)  12/25 + αβ = 0      →   αβ = -12/25
(3)  9/25 + β^2 = 1      →   β^2 = 16/25
```

De (1) y (3): `α = ±3/5`, `β = ±4/5`.

Por (2), `αβ = -12/25` (negativo), asi que tienen signos opuestos.

Por ejemplo: `α = 3/5`, `β = -4/5`. (O `α = -3/5`, `β = 4/5`.)

> "No, nunca importa la verdad. Por la definicion de la inversa, A por A inversa es la identidad, y tambien A inversa por A es la identidad"

**Traduccion:** Un estudiante pregunto si importaba multiplicar `A * A^T` o `A^T * A`. La respuesta es que **no importa** - por definicion de inversa, los dos productos tienen que dar identidad. Podemos elegir el orden que nos sea mas comodo de calcular.

---

## Ejercicio 14 del Practico: ¿Es A + B siempre Invertible?

### Enunciado

Si `A` y `B` son invertibles, ¿es necesariamente `A + B` invertible? En caso afirmativo, probarlo. En caso negativo, dar un contraejemplo.

### Respuesta: NO necesariamente

**Contraejemplo clasico:** `A = I` y `B = -I`. Ambas son invertibles (sus inversas son `I` y `-I` respectivamente). Pero `A + B = I + (-I) = O` (la matriz nula), y la matriz nula **no es invertible**.

**Conclusion:** la suma de matrices invertibles **no** tiene por que ser invertible.

> "Si yo aca tomo dos matrices que son invertibles, las sumo y el resultado no es invertible, entonces esta afirmacion no es cierta"

**Traduccion:** Para refutar una afirmacion general basta con un solo contraejemplo. No hace falta una demostracion compleja - solo un caso concreto que no cumpla.

### Si A y B son invertibles, ¿es A * B invertible?

**Respuesta: SI.** Y ya tenemos la formula:

```
(A * B)^(-1) = B^(-1) * A^(-1)
```

Esto es la propiedad 3 de la inversa, demostrada en la clase anterior.

> "Como regla general, si algo es cierto hay que probarlo para n por n, y si es falso o en algun caso no se cumple, ya no es cierto"

**Traduccion:** Para afirmar que algo es cierto en general, hay que demostrarlo para `n x n` (caso generico). Para refutar, alcanza con un contraejemplo.

---

## Anuncios al Final de Clase

- A las **9:30 PM** comienza la primera prueba de evaluacion continua.
- Despues de la prueba: vacaciones de **Semana de Turismo** (Pascuas).
- A la vuelta arrancan con el **segundo tema: determinantes**.

---

# Definiciones Consolidadas para el Parcial

**Matriz:** arreglo rectangular de numeros reales organizado en filas y columnas. Si tiene `m` filas y `n` columnas, pertenece a `M_mxn(R)`.

**Diagonal principal:** entradas `a_ii` de una matriz cuadrada (donde la fila coincide con la columna).

**Matriz cuadrada:** matriz con igual numero de filas que de columnas (`m = n`).

**Matriz triangular superior:** cuadrada con todas las entradas debajo de la diagonal nulas (`a_ij = 0` para `i > j`).

**Matriz triangular inferior:** cuadrada con todas las entradas encima de la diagonal nulas (`a_ij = 0` para `i < j`).

**Matriz diagonal:** cuadrada con todas las entradas fuera de la diagonal nulas (`a_ij = 0` para `i ≠ j`).

**Matriz identidad (I):** diagonal con todos los elementos de la diagonal iguales a `1`. Es el neutro del producto.

**Matriz nula (O):** matriz con todas las entradas iguales a `0`. Es el neutro de la suma.

**Suma de matrices:** operacion entrada a entrada; requiere que ambas matrices tengan la misma dimension.

**Producto escalar por matriz:** multiplicar cada entrada de la matriz por un numero real.

**Producto de matrices:** para `A` de `mxn` y `B` de `nxp`, el resultado `C = A * B` es una matriz `mxp` donde `c_ij` se calcula como la fila `i` de `A` multiplicada por la columna `j` de `B` (par a par y sumado). Requiere conformabilidad: columnas de `A` = filas de `B`. **NO es conmutativo.**

**Matriz traspuesta (`A^T`):** se obtiene intercambiando filas por columnas. Si `A` es `mxn`, entonces `A^T` es `nxm`.

**Matriz simetrica:** matriz cuadrada que cumple `A^T = A`. Hay simetria respecto a la diagonal principal.

**Matriz antisimetrica:** matriz cuadrada que cumple `A^T = -A`. La diagonal principal siempre es nula.

**Traza (`tr(A)`):** suma de los elementos de la diagonal principal de una matriz cuadrada.

**Matriz invertible:** matriz cuadrada `A` para la que existe otra matriz `B` (llamada `A^(-1)`) tal que `A * B = B * A = I`.

**Metodo directo para hallar la inversa:** plantear `A * B = I` con `B` generica, igualar entrada a entrada, y resolver el sistema de ecuaciones resultante.

**Matriz idempotente:** matriz cuadrada que cumple `A^2 = A`.

**Matriz nilpotente de grado k:** matriz cuadrada tal que `A^k = O` y `A^(k-1) ≠ O`.

**Matriz ortogonal:** matriz cuadrada cuya inversa coincide con su traspuesta (`A^(-1) = A^T`).

**Induccion completa:** metodo de demostracion con tres pasos: paso base (verificar para `n = 1`), hipotesis inductiva (suponer para `n = h`), y demostracion (probar para `n = h + 1`).

**Prueba por el absurdo:** suponer que algo es cierto, llegar a una contradiccion, y concluir que la suposicion era falsa.

---

# Posibles Preguntas Consolidadas para el Parcial

**¿Cuando dos matrices son iguales?**
Cuando tienen la misma dimension Y todas sus entradas correspondientes son iguales (`a_ij = b_ij` para todo `i, j`).

**¿Que requisito tiene la suma de matrices?**
Que ambas tengan la misma dimension (mismo `m` y mismo `n`).

**¿Que requisito tiene el producto de matrices? ¿Cual es la dimension del resultado?**
El numero de columnas de la primera tiene que ser igual al numero de filas de la segunda (conformabilidad). Si `A` es `mxn` y `B` es `nxp`, el resultado es `mxp`.

**¿Por que el producto de matrices NO es conmutativo? Dar un ejemplo.**
Porque en general `A * B ≠ B * A`. Ejemplo: `A = [[1,2],[3,-4]]` y `B = [[2,1],[3,4]]` dan `AB = [[8,9],[-6,-13]]` y `BA = [[5,0],[15,-10]]`. Son distintas.

**¿Que es la matriz traspuesta? ¿Como se nota?**
Se obtiene intercambiando filas por columnas. Si `A` es `mxn`, entonces `A^T` es `nxm` y se nota `A^T`.

**¿Cuales son las cuatro propiedades de la traspuesta?**
1. `(A^T)^T = A`
2. `(A + B)^T = A^T + B^T`
3. `(α * A)^T = α * A^T`
4. `(A * B)^T = B^T * A^T` (orden invertido)

**¿Que es una matriz simetrica? ¿Y una antisimetrica?**
Simetrica: `A^T = A`. Antisimetrica: `A^T = -A`. La antisimetrica tiene siempre diagonal nula.

**Demostrar que la suma de dos matrices simetricas es simetrica.**
`(A+B)^T = A^T + B^T = A + B`, por las propiedades 2 de la traspuesta y la hipotesis.

**Demostrar que `(1/2)(A + A^T)` es simetrica.**
Trasponer la expresion: `((1/2)(A + A^T))^T = (1/2)(A^T + (A^T)^T) = (1/2)(A^T + A) = (1/2)(A + A^T)`. Coincide con la original, asi que es simetrica.

**¿Cuando es `AB` simetrica si `A` y `B` son simetricas?**
Si y solo si `A * B = B * A` (es decir, conmutan).

**¿Que es la traza de una matriz?**
La suma de los elementos de la diagonal principal. Solo aplica a matrices cuadradas.

**¿Cuales son las cuatro propiedades de la traza?**
1. `tr(A + B) = tr(A) + tr(B)`
2. `tr(α * A) = α * tr(A)`
3. `tr(A^T) = tr(A)`
4. `tr(A * B) = tr(B * A)`

**¿Por que no existen matrices `A, B` tales que `AB - BA = I`?**
Porque `tr(AB - BA) = tr(AB) - tr(BA) = 0` (por propiedad 4 de la traza), pero `tr(I) = n ≠ 0` para cualquier `n ≥ 1`. Contradiccion.

**¿Que significa que una matriz sea invertible?**
Que existe otra matriz (la inversa) tal que al multiplicarlas - en cualquier orden - da la identidad. Se nota `A^(-1)`. Puede no existir.

**¿Como se halla la inversa por el metodo directo?**
Se plantea `A * B = I` con `B` generica, se multiplica, se iguala a la identidad entrada a entrada, y se resuelve el sistema de ecuaciones resultante. Si no tiene solucion, la matriz no es invertible.

**¿Por que `(A * B)^(-1) = B^(-1) * A^(-1)` y NO `A^(-1) * B^(-1)`?**
Porque las matrices no conmutan. El orden se invierte (igual que con la traspuesta). Se demuestra multiplicando `(AB)` por `(B^(-1) A^(-1))` y usando asociativa para cancelar `B * B^(-1) = I`.

**Si `A` es idempotente e invertible, ¿que es `A`?**
La identidad. Se demuestra multiplicando ambos lados de `A^2 = A` por `A^(-1)`.

**¿Por que no se puede "pasar dividiendo" una matriz?**
Porque la division no esta definida para matrices. El equivalente es multiplicar por la inversa **del mismo lado** en ambos miembros.

**¿Por que al factorizar `X` de la expresion `AX + X` hay que usar la identidad?**
Porque `X = I * X`, entonces `AX + X = AX + IX = (A + I)X`. No se puede escribir `(A + 1)X` porque no se puede sumar un numero a una matriz.

**¿Que dice la propiedad de la potencia de una matriz diagonal?**
Si `A` es diagonal, entonces `A^k` se obtiene elevando a la `k` cada entrada de la diagonal principal. Se demuestra por induccion completa.

**Si `A^3 = O`, ¿cual es la inversa de `A + I`?**
`(A + I)^(-1) = A^2 - A + I`. Se demuestra multiplicando `(A + I)(A^2 - A + I)` y verificando que da `I`.

**¿Si `A` y `B` son invertibles, es `A + B` invertible?**
NO necesariamente. Contraejemplo: `A = I` y `B = -I` son invertibles pero `A + B = O` no lo es.

**¿Si `A` y `B` son invertibles, es `A * B` invertible?**
SI. Y `(AB)^(-1) = B^(-1) * A^(-1)`.

**¿Si `AB = AC` y `A` es invertible, podemos concluir `B = C`?**
SI. Multiplicamos por `A^(-1)` por la izquierda en ambos lados.

**¿Y si `A` no es invertible?**
NO necesariamente. Pueden existir `B ≠ C` con `AB = AC`.

**¿Que es una matriz ortogonal?**
Una matriz cuadrada cuya inversa coincide con su traspuesta: `A^(-1) = A^T`. Equivalentemente, `A * A^T = I`.

**¿Que es una matriz nilpotente de grado `k`?**
Una matriz cuadrada tal que `A^k = O` pero `A^(k-1) ≠ O`. Es decir, `k` es la primera potencia que la anula.

**Si `A` es nilpotente de grado `k` y `P` es invertible, ¿de que grado es nilpotente `P^(-1) * A * P`?**
Del mismo grado `k`. Porque `(P^(-1) * A * P)^n = P^(-1) * A^n * P`, y este se anula exactamente cuando `A^n = O`.

---

Documento generado a partir de las transcripciones de las cuatro primeras clases de Algebra Lineal (FI-2103) con el Prof. Gabriel Cisneros, ORT Uruguay, periodo 17/03/2026 - 25/03/2026.
