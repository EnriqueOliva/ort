# Explicacion de Temas - Clase del 18-03-2026: Matriz Traspuesta, Simetria, y Traza

## La Gran Pregunta: Si las matrices son tablas de numeros, que pasa cuando las "damos vuelta", las comparamos consigo mismas, o sumamos su diagonal?

En la clase anterior aprendimos a sumar, escalar y multiplicar matrices. Pero las matrices tienen mas estructura interna de la que parece. Hoy vamos a ver tres herramientas nuevas que explotan esa estructura: la **traspuesta** (dar vuelta filas por columnas), la **simetria** (matrices que no cambian al trasponerlas), y la **traza** (sumar la diagonal). Estas tres ideas aparecen constantemente en algebra lineal y son fundamentales para el parcial.

---

## Conexion con la Clase Anterior

En la clase del 17-03-2026 (la primera del curso) se definio que es una matriz, la notacion `m x n`, como se nombran las entradas `a_ij`, y los tipos de matrices: **fila**, **columna**, **rectangular**, **cuadrada**, **diagonal**, **identidad** (neutro de la multiplicacion), y **nula** (neutro de la suma). Tambien se vieron las tres operaciones basicas: **suma** (entrada a entrada, mismas dimensiones), **producto escalar por matriz** (multiplicar cada entrada por un numero), y **producto entre matrices** (condicion de conformabilidad: columnas de la primera = filas de la segunda, y el resultado se calcula fila por columna). Se enfatizo que el producto de matrices **no es conmutativo** — es decir, `A * B` generalmente es distinto de `B * A`. Esa no-conmutatividad va a ser clave hoy.

---

## Matriz Traspuesta

### Definicion

> "Basicamente es cambiar filas por columnas"

**Traduccion:** La traspuesta de una matriz se obtiene intercambiando sus filas por columnas (o equivalentemente, sus columnas por filas). La primera fila pasa a ser la primera columna, la segunda fila pasa a ser la segunda columna, y asi sucesivamente.

Formalmente: dada `A` perteneciente a `M_mxn(R)` (una matriz de `m` filas y `n` columnas con entradas reales), su **traspuesta** `A^T` pertenece a `M_nxm(R)` (se invierten las dimensiones).

La notacion es `A^T` — la letra A con un superindice T.

En terminos de entradas: si la entrada en la fila `i`, columna `j` de `A` es `a_ij`, entonces la entrada en la fila `j`, columna `i` de `A^T` es ese mismo `a_ij`. Dicho de otra forma:

```
(A^T)_ji = a_ij
```

Que significa esto?
- `a_ij` = la entrada que estaba en fila `i`, columna `j` de la original
- `(A^T)_ji` = esa misma entrada ahora esta en fila `j`, columna `i` de la traspuesta
- La formula completa dice: transponer es "espejear" la matriz respecto de su diagonal principal

**Analogia:** Imagina que la matriz es una planilla de Excel donde las filas son alumnos y las columnas son materias. Si la traspones, ahora las filas son materias y las columnas son alumnos. Los datos son los mismos, pero reorganizados.

### Caso generico

Si tenemos una matriz `A` de `m x n`:

```
A = | a_11  a_12  ...  a_1n |
    | a_21  a_22  ...  a_2n |
    | ...   ...   ...  ...  |
    | a_m1  a_m2  ...  a_mn |
```

Entonces su traspuesta `A^T` es de `n x m`:

```
A^T = | a_11  a_21  ...  a_m1 |
      | a_12  a_22  ...  a_m2 |
      | ...   ...   ...  ...  |
      | a_1n  a_2n  ...  a_mn |
```

Fijate: la primera fila de `A` (`a_11, a_12, ..., a_1n`) se convierte en la primera columna de `A^T`. La segunda fila de `A` se convierte en la segunda columna de `A^T`. Y asi con cada fila.

### Ejemplo numerico

Sea `A` una matriz `2 x 3` (2 filas, 3 columnas):

```
A = | 1  2  3 |
    | 4  9  5 |
```

La traspuesta `A^T` es `3 x 2` (3 filas, 2 columnas):

```
A^T = | 1  4 |
      | 2  9 |
      | 3  5 |
```

Verificacion:
- Fila 1 de `A` era `1, 2, 3` → ahora es la columna 1 de `A^T`: `1, 2, 3`
- Fila 2 de `A` era `4, 9, 5` → ahora es la columna 2 de `A^T`: `4, 9, 5`
- Las dimensiones pasaron de `2 x 3` a `3 x 2`

---

## Propiedades de la Traspuesta

La traspuesta tiene 4 propiedades fundamentales. Las primeras tres son bastante intuitivas. La cuarta es la trampa clasica del parcial.

### Propiedad 1: (A^T)^T = A

> "Yo transpongo la matriz, la vuelvo a transponer y vuelvo a la matriz original"

**Traduccion:** Si traspones una matriz y despues traspones el resultado, volves a la matriz original. Transponer dos veces es como no hacer nada.

**Analogia:** Es como dar vuelta una remera al reves y despues darla vuelta de nuevo — queda como estaba al principio.

**Ejemplo numerico:**

```
A = | 1  2  3 |      A^T = | 1  4 |      (A^T)^T = | 1  2  3 |  = A
    | 4  9  5 |             | 2  9 |                 | 4  9  5 |
                            | 3  5 |
```

### Propiedad 2: (A + B)^T = A^T + B^T

> "Es lo mismo sumar A y B y transponer que sumar A transpuesta con B transpuesta"

**Traduccion:** La traspuesta de una suma es la suma de las traspuestas. No importa si primero sumas y despues traspones, o si primero traspones cada una y despues las sumas — el resultado es el mismo.

**Analogia:** Es como si el "dar vuelta" se distribuyera sobre la suma, igual que cuando distribuimos la multiplicacion sobre la suma de numeros.

**Ejemplo numerico:**

```
A = | 1  2 |    B = | 5  6 |
    | 3  4 |        | 7  8 |

A + B = | 6   8 |    (A + B)^T = | 6  10 |
        | 10  12|                | 8  12 |

A^T = | 1  3 |    B^T = | 5  7 |    A^T + B^T = | 6  10 |
      | 2  4 |          | 6  8 |                 | 8  12 |
```

Mismo resultado por ambos caminos.

### Propiedad 3: (alfa * A)^T = alfa * A^T

> "Es lo mismo multiplicar alfa por A y transponerla que multiplicar alfa por A transpuesta"

**Traduccion:** El escalar (el numero) se puede "sacar afuera" de la traspuesta. Da lo mismo escalar primero y transponer despues, que transponer primero y escalar despues.

**Error comun que el profesor advirtio:** algunos estudiantes escriben `alfa^T * A^T` — esto esta MAL.

> "Alfa es un numero, no podemos transponerlo, es un escalar"

**Traduccion:** No tiene sentido "transponer" un numero suelto. La traspuesta es una operacion para matrices, no para escalares. Un escalar no tiene filas ni columnas, asi que `alfa^T` no existe. Solo se transpone la matriz.

**Ejemplo numerico:**

```
alfa = 3    A = | 1  2 |
                | 3  4 |

alfa * A = | 3   6 |    (alfa * A)^T = | 3  9  |
           | 9  12 |                   | 6  12 |

A^T = | 1  3 |    alfa * A^T = | 3  9  |
      | 2  4 |                 | 6  12 |
```

Mismo resultado.

### Propiedad 4: (A * B)^T = B^T * A^T (SE INVIERTE EL ORDEN)

> "A por B transpuesta es igual a B transpuesta por A transpuesta"

**Traduccion:** Cuando traspones un producto de matrices, el resultado es el producto de las traspuestas **pero en orden invertido**. Primero va `B^T` y despues `A^T`, al reves de como estaban originalmente.

Esta es la propiedad mas importante y la que mas confunde. El orden se invierte.

**Error comun que el profesor advirtio:** muchos estudiantes escriben `(A * B)^T = A^T * B^T` — esto esta **MAL**.

> "Vos no podes asegurar que esto sea igual a esto, porque las matrices generalmente no conmutan"

**Traduccion:** No podes poner las traspuestas en el mismo orden que las originales porque `A^T * B^T` generalmente es distinto de `B^T * A^T`. Recordemos de la clase anterior: el producto de matrices no es conmutativo, asi que cambiar el orden cambia el resultado.

Si alguien te pregunta en el parcial "por que esta mal escribir `(A * B)^T = A^T * B^T`?", la respuesta es: porque eso implicaria que `B^T * A^T = A^T * B^T`, y como las matrices generalmente no conmutan, eso no se puede afirmar.

**Analogia:** Pensalo como ponerse medias y zapatos. Para ponertelos, primero van las medias y despues los zapatos. Pero para sacartelos (la operacion "inversa"), el orden se invierte: primero los zapatos y despues las medias. Con la traspuesta del producto pasa algo parecido.

**Ejemplo numerico:**

```
A = | 1  2 |    B = | 5  6 |
    | 3  4 |        | 7  8 |

A * B = | 1*5+2*7  1*6+2*8 | = | 19  22 |
        | 3*5+4*7  3*6+4*8 |   | 43  50 |

(A * B)^T = | 19  43 |
            | 22  50 |

B^T = | 5  7 |    A^T = | 1  3 |
      | 6  8 |          | 2  4 |

B^T * A^T = | 5*1+7*2  5*3+7*4 | = | 19  43 |
            | 6*1+8*2  6*3+8*4 |   | 22  50 |
```

Mismo resultado: `(A * B)^T = B^T * A^T`.

---

## Matrices Simetricas

### Definicion

Una matriz `A` perteneciente a `M_nxn(R)` (cuadrada, de `n x n`) es **simetrica** si y solo si:

```
A^T = A
```

Que significa esto?
- `A^T` = la traspuesta de A (filas cambiadas por columnas)
- `A` = la matriz original
- La formula completa dice: si transpones la matriz y te queda exactamente igual, la matriz es simetrica

En terminos de entradas, esto quiere decir que:

```
a_ij = a_ji    para todo i, j de 1 a n
```

O sea, la entrada en la fila `i` columna `j` es siempre igual a la entrada en la fila `j` columna `i`. Hay **simetria respecto de la diagonal principal**: lo que hay arriba-a-la-derecha de la diagonal es un espejo de lo que hay abajo-a-la-izquierda.

> "Si vos la transpones, la primera fila que es 1,4,6 pasaria a ser la primera columna que tambien es 1,4,6"

**Traduccion:** Al transponer, cada fila se convierte en la columna del mismo numero. Si la fila 1 y la columna 1 ya tienen los mismos valores, al transponer nada cambia. Y eso pasa con todas las filas y columnas de una matriz simetrica.

**Analogia:** Imagina que la matriz es una tabla de distancias entre ciudades. La distancia de Montevideo a Punta del Este es la misma que de Punta del Este a Montevideo. Entonces la tabla es simetrica: `a_ij = a_ji`.

### Ejemplo numerico

```
A = | 1  4  6 |
    | 4  2  5 |
    | 6  5  3 |
```

Verifiquemos la simetria:
- `a_12 = 4` y `a_21 = 4` (iguales)
- `a_13 = 6` y `a_31 = 6` (iguales)
- `a_23 = 5` y `a_32 = 5` (iguales)
- La diagonal (`1, 2, 3`) queda en su lugar al transponer

Traspuesta:

```
A^T = | 1  4  6 |
      | 4  2  5 |  = A
      | 6  5  3 |
```

Como `A^T = A`, la matriz es simetrica.

### Caso particular: las matrices diagonales

Toda **matriz diagonal** es simetrica. Por que? Porque fuera de la diagonal principal todo es cero, asi que `a_ij = 0 = a_ji` para `i ≠ j`. Al transponer, los ceros siguen siendo ceros y la diagonal no cambia.

```
D = | 3  0  0 |        D^T = | 3  0  0 |
    | 0  7  0 |              | 0  7  0 |  = D
    | 0  0  2 |              | 0  0  2 |
```

---

## Matrices Antisimetricas

### Definicion

Una matriz `A` perteneciente a `M_nxn(R)` (cuadrada) es **antisimetrica** si y solo si:

```
A^T = -A
```

Que significa esto?
- `A^T` = la traspuesta de A
- `-A` = la matriz A con todas sus entradas cambiadas de signo
- La formula completa dice: si transpones la matriz y te queda la misma pero con todos los signos invertidos, la matriz es antisimetrica

En terminos de entradas:

```
a_ij = -a_ji    para todo i, j de 1 a n
```

Cada par de entradas simetricas respecto de la diagonal son **opuestas** (tienen el mismo valor absoluto pero signo contrario). Es como una "simetria opuesta" respecto de la diagonal principal.

### La diagonal principal debe ser toda ceros

> "Si yo transpongo es lo mismo que multiplicar por menos uno y me tiene que quedar igual, y hoy ya hemos dicho que si transpongo la diagonal principal no me cambia, entonces el unico numero que es igual a su negativo es el cero"

**Traduccion:** Los elementos de la diagonal principal no cambian al transponer (porque `a_ii` queda en la misma posicion). Pero la definicion dice que `A^T = -A`, entonces cada `a_ii` debe ser igual a `-a_ii`. El unico numero que cumple `x = -x` es `x = 0`. Por lo tanto, toda la diagonal principal de una matriz antisimetrica es cero.

**Analogia:** Si alguien te dice "tu edad es igual al negativo de tu edad", la unica solucion es edad = 0. Lo mismo pasa con cada entrada de la diagonal.

### Ejemplo numerico

```
A = |  0  -2  -4 |
    |  2   0  -6 |
    |  4   6   0 |
```

Verificacion:
- La diagonal es toda ceros: `0, 0, 0`
- `a_12 = -2` y `a_21 = 2` (opuestos)
- `a_13 = -4` y `a_31 = 4` (opuestos)
- `a_23 = -6` y `a_32 = 6` (opuestos)

Traspuesta:

```
A^T = | 0   2   4 |
      | -2  0   6 |
      | -4  -6  0 |
```

Negativo de A:

```
-A = |  0   2   4 |
     | -2   0   6 |
     | -4  -6   0 |
```

Efectivamente `A^T = -A`, asi que `A` es antisimetrica.

### Pregunta de un estudiante: una matriz antisimetrica mas su traspuesta da la nula?

Si. Si `A` es antisimetrica, entonces `A^T = -A`, por lo que:

```
A + A^T = A + (-A) = 0
```

La traspuesta de una matriz antisimetrica es su **opuesta** (opuesta en el sentido de la suma: la matriz que al sumarla da la nula).

---

## Propiedades de Matrices Simetricas y Antisimetricas

### Propiedad 1: La suma de dos matrices simetricas es simetrica

**Demostracion (hecha en clase):**

**Hipotesis:** `A^T = A` y `B^T = B` (ambas son simetricas)

**Tesis:** `(A + B)^T = A + B` (queremos probar que `A + B` es simetrica)

```
(A + B)^T = A^T + B^T       (por propiedad 2 de la traspuesta)
          = A + B             (por hipotesis: A^T = A y B^T = B)
```

Por lo tanto `A + B` es simetrica.

**Ejemplo numerico:**

```
A = | 1  3 |    B = | 5  2 |    A + B = | 6  5 |
    | 3  4 |        | 2  7 |            | 5  11|

(A + B)^T = | 6  5 | = A + B  -->  simetrica
            | 5  11|
```

### Propiedad 2: Si A es simetrica y alfa es un escalar, entonces alfa * A es simetrica

**Demostracion (hecha en clase):**

**Hipotesis:** `A^T = A`

**Tesis:** `(alfa * A)^T = alfa * A`

```
(alfa * A)^T = alfa * A^T    (por propiedad 3 de la traspuesta)
             = alfa * A       (por hipotesis: A^T = A)
```

Por lo tanto `alfa * A` es simetrica.

**Ejemplo numerico:**

```
A = | 1  3 |    alfa = 4    alfa * A = | 4   12 |
    | 3  4 |                           | 12  16 |

(alfa * A)^T = | 4   12 | = alfa * A  -->  simetrica
               | 12  16 |
```

### Propiedad 3: La suma de dos matrices antisimetricas es antisimetrica

**Demostracion (analoga a la propiedad 1):**

**Hipotesis:** `A^T = -A` y `B^T = -B`

**Tesis:** `(A + B)^T = -(A + B)`

```
(A + B)^T = A^T + B^T        (por propiedad 2 de la traspuesta)
          = (-A) + (-B)       (por hipotesis)
          = -(A + B)
```

Por lo tanto `A + B` es antisimetrica.

### Propiedad 4: Si A es antisimetrica y alfa es un escalar, entonces alfa * A es antisimetrica

**Demostracion (analoga a la propiedad 2):**

**Hipotesis:** `A^T = -A`

**Tesis:** `(alfa * A)^T = -(alfa * A)`

```
(alfa * A)^T = alfa * A^T    (por propiedad 3 de la traspuesta)
             = alfa * (-A)    (por hipotesis)
             = -(alfa * A)
```

Por lo tanto `alfa * A` es antisimetrica.

---

## Traza de una Matriz

### Definicion

La **traza** de una matriz cuadrada `A` perteneciente a `M_nxn(R)` es la **suma de los elementos de la diagonal principal**. Se nota `tr(A)`.

```
tr(A) = a_11 + a_22 + a_33 + ... + a_nn
```

Escrito con sumatoria:

```
tr(A) = Σ (i = 1 hasta n) a_ii
```

Que significa esto?
- `a_ii` = la entrada que esta en la fila `i`, columna `i` (o sea, sobre la diagonal)
- `Σ` = sumar todos esos valores desde `i = 1` hasta `i = n`
- La formula completa dice: la traza es simplemente sumar los numeros que estan en la diagonal principal

La traza solo esta definida para **matrices cuadradas** (las unicas que tienen diagonal principal completa).

**Analogia:** Si la matriz es una tabla de datos, la diagonal principal es como "la linea que va de la esquina superior-izquierda a la esquina inferior-derecha". La traza es sumar todos los numeros que caen sobre esa linea.

### Ejemplo numerico

```
A = | 4  7  2 |
    | 1  1  8 |
    | 3  6  5 |

tr(A) = 4 + 1 + 5 = 10
```

Solo importan los elementos de la diagonal: `a_11 = 4`, `a_22 = 1`, `a_33 = 5`. Los demas se ignoran.

---

## Propiedades de la Traza

### Propiedad 1: tr(A + B) = tr(A) + tr(B)

**Demostracion (hecha en clase):**

```
tr(A) = Σ a_ii
tr(B) = Σ b_ii

tr(A + B) = Σ (a_ii + b_ii)       (la entrada diagonal de A+B es a_ii + b_ii)
          = Σ a_ii + Σ b_ii        (la sumatoria se distribuye)
          = tr(A) + tr(B)
```

La traza de la suma es la suma de las trazas.

**Ejemplo numerico:**

```
A = | 4  1 |    B = | 3  5 |    A + B = | 7  6 |
    | 2  6 |        | 8  2 |            | 10 8 |

tr(A) = 4 + 6 = 10
tr(B) = 3 + 2 = 5
tr(A + B) = 7 + 8 = 15 = 10 + 5 = tr(A) + tr(B)
```

### Propiedad 2: tr(alfa * A) = alfa * tr(A)

**Demostracion (hecha en clase):**

```
tr(alfa * A) = Σ (alfa * a_ii)     (cada entrada diagonal se multiplica por alfa)
             = alfa * Σ a_ii        (el escalar sale de la sumatoria)
             = alfa * tr(A)
```

El escalar se puede "sacar afuera" de la traza.

**Ejemplo numerico:**

```
A = | 4  1 |    alfa = 3
    | 2  6 |

alfa * A = | 12  3 |
           | 6  18 |

tr(alfa * A) = 12 + 18 = 30
alfa * tr(A) = 3 * (4 + 6) = 3 * 10 = 30
```

### Propiedad 3: tr(A^T) = tr(A)

> "Si tenemos una matriz y la transponemos, la diagonal principal no cambia, entonces no va a cambiar la traza"

**Traduccion:** Al transponer, los elementos de la diagonal principal quedan en el mismo lugar (porque `a_ii` esta en fila `i`, columna `i`, y al transponer sigue estando en fila `i`, columna `i`). Como la traza solo depende de la diagonal, no cambia.

**Ejemplo numerico:**

```
A = | 4  1  7 |        A^T = | 4  2  3 |
    | 2  6  8 |              | 1  6  9 |
    | 3  9  5 |              | 7  8  5 |

tr(A)   = 4 + 6 + 5 = 15
tr(A^T) = 4 + 6 + 5 = 15
```

### Propiedad 4: tr(A * B) = tr(B * A)

> "Lo que me dice la propiedad 4 es que la traza de A por B es igual a la traza de B por A. Hoy dia hemos visto que A por B generalmente es distinto de B por A... pero la suma de la diagonal principal me da lo mismo"

**Traduccion:** Aunque `A * B` y `B * A` son generalmente matrices diferentes (recordemos: las matrices no conmutan), la suma de sus diagonales principales da el mismo numero. Es decir, las matrices son distintas, pero sus trazas coinciden.

> "Incluso si yo hago A por B me queda M por M y si hago B por A me queda N por N, o sea tienen dimensiones distintas, sin embargo sumo la diagonal principal y me da lo mismo"

**Traduccion:** Lo mas sorprendente es que esto funciona incluso cuando `A` y `B` no son cuadradas. Si `A` es `m x n` y `B` es `n x m`, entonces `A * B` es `m x m` y `B * A` es `n x n` — matrices de dimensiones **diferentes**. Y aun asi, la traza de ambas es la misma. Esto es, como dijo el profesor, **"muy poco intuitivo"**.

**Analogia:** Imagina dos recetas diferentes con los mismos ingredientes. Las recetas producen platos distintos (las matrices son distintas), pero si sumas todas las calorias de la diagonal de cada plato, el total es el mismo. No tiene por que ser obvio, pero es asi.

**Ejemplo numerico con matrices de distinta dimension:**

```
A (2x3) = | 1  2  3 |       B (3x2) = | 1  0 |
          | 0  1  0 |                  | 0  1 |
                                       | 1  1 |

A * B (2x2) = | 1*1+2*0+3*1  1*0+2*1+3*1 | = | 4  5 |
              | 0*1+1*0+0*1  0*0+1*1+0*1 |   | 0  1 |

tr(A * B) = 4 + 1 = 5

B * A (3x3) = | 1*1+0*0  1*2+0*1  1*3+0*0 | = | 1  2  3 |
              | 0*1+1*0  0*2+1*1  0*3+1*0 |   | 0  1  0 |
              | 1*1+1*0  1*2+1*1  1*3+1*0 |   | 1  3  3 |

tr(B * A) = 1 + 1 + 3 = 5
```

Matrices totalmente distintas (`2 x 2` vs `3 x 3`), pero `tr(A * B) = tr(B * A) = 5`.

---

## Ejercicios Practicos Resueltos en Clase

### Ejercicio 2: Todos los productos posibles entre A(2x3), B(3x3), C(3x2)

La condicion de conformabilidad dice: para multiplicar `X (p x q)` por `Y (r x s)`, necesitamos que `q = r` (columnas de la primera = filas de la segunda). El resultado tiene dimension `p x s`.

| Producto | Dimensiones | Conformable? | Dimension resultado |
|----------|-------------|-------------|---------------------|
| A * B | 2x**3** * **3**x3 | Si (3 = 3) | 2 x 3 |
| A * C | 2x**3** * **3**x2 | Si (3 = 3) | 2 x 2 |
| B * A | 3x**3** * **2**x3 | No (3 ≠ 2) | --- |
| B * C | 3x**3** * **3**x2 | Si (3 = 3) | 3 x 2 |
| C * A | 3x**2** * **2**x3 | Si (2 = 2) | 3 x 3 |
| C * B | 3x**2** * **3**x3 | No (2 ≠ 3) | --- |

### Calculo de A * B

```
A = | 2  -1  4 |       B = | 1   0  1 |
    | 1   0  6 |           | 2  -1  2 |
                            | 3  -2  0 |
```

Para cada entrada del resultado, multiplicamos la fila correspondiente de `A` por la columna correspondiente de `B`:

```
Entrada (1,1): 2*1 + (-1)*2 + 4*3 = 2 - 2 + 12 = 12
Entrada (1,2): 2*0 + (-1)*(-1) + 4*(-2) = 0 + 1 - 8 = -7
Entrada (1,3): 2*1 + (-1)*2 + 4*0 = 2 - 2 + 0 = 0
Entrada (2,1): 1*1 + 0*2 + 6*3 = 1 + 0 + 18 = 19
Entrada (2,2): 1*0 + 0*(-1) + 6*(-2) = 0 + 0 - 12 = -12
Entrada (2,3): 1*1 + 0*2 + 6*0 = 1 + 0 + 0 = 1
```

```
A * B = | 12  -7   0 |
        | 19  -12  1 |
```

### Ejercicio 3: Multiplicar una matriz generica por vectores canonicos

Sea `A` una matriz `3 x 3` generica:

```
A = | a_11  a_12  a_13 |
    | a_21  a_22  a_23 |
    | a_31  a_32  a_33 |
```

Los vectores canonicos (o vectores de la base estandar) son:

```
e1 = | 1 |    e2 = | 0 |    e3 = | 0 |
     | 0 |         | 1 |         | 0 |
     | 0 |         | 0 |         | 1 |
```

Multiplicando:

```
A * e1 = | a_11*1 + a_12*0 + a_13*0 |   | a_11 |
         | a_21*1 + a_22*0 + a_23*0 | = | a_21 |  = primera columna de A
         | a_31*1 + a_32*0 + a_33*0 |   | a_31 |

A * e2 = | a_11*0 + a_12*1 + a_13*0 |   | a_12 |
         | a_21*0 + a_22*1 + a_23*0 | = | a_22 |  = segunda columna de A
         | a_31*0 + a_32*1 + a_33*0 |   | a_32 |

A * e3 = | a_11*0 + a_12*0 + a_13*1 |   | a_13 |
         | a_21*0 + a_22*0 + a_23*1 | = | a_23 |  = tercera columna de A
         | a_31*0 + a_32*0 + a_33*1 |   | a_33 |
```

**Conclusion:** Multiplicar una matriz por el vector canonico `e_k` (que tiene un 1 en la posicion `k` y ceros en las demas) **extrae la columna `k` de la matriz**. A medida que vas corriendo el 1 de posicion, vas copiando la columna correspondiente.

### Ejercicio 5.2: Probar que A * B es simetrica si y solo si A y B conmutan (A, B simetricas)

> "Siempre que vean un si solo si, acuerdense que tienen que demostrar para los dos lados, si no estarian haciendo 50%"

**Traduccion:** Un "si y solo si" (abreviado "sii") requiere dos demostraciones: la ida y la vuelta. Si solo demostras un sentido, tenes la mitad del ejercicio.

**Hipotesis general:** `A` y `B` son simetricas (`A^T = A`, `B^T = B`)

**Parte directa: Si A * B es simetrica, entonces A * B = B * A (conmutan)**

Sabemos que `A * B` es simetrica, es decir `(A * B)^T = A * B`. Desarrollamos el lado izquierdo:

```
(A * B)^T = B^T * A^T    (por propiedad 4 de la traspuesta)
          = B * A          (porque A^T = A y B^T = B por hipotesis)
```

Entonces: `A * B = (A * B)^T = B * A`. Queda demostrado que conmutan.

**Parte reciproca: Si A * B = B * A (conmutan), entonces A * B es simetrica**

Partimos de `A * B = B * A` y transponemos ambos lados:

```
(A * B)^T = (B * A)^T
```

Desarrollamos el lado derecho:

```
(B * A)^T = A^T * B^T     (por propiedad 4 de la traspuesta)
          = A * B           (porque A^T = A y B^T = B)
```

Entonces: `(A * B)^T = A * B`. Eso significa que `A * B` es simetrica.

### Ejercicio 6.1: Probar que (1/2)(A + A^T) es simetrica para cualquier matriz cuadrada A

Necesitamos demostrar que al transponer `(1/2)(A + A^T)` obtenemos lo mismo.

```
[(1/2)(A + A^T)]^T
= (1/2) * (A + A^T)^T           (propiedad 3 de traspuesta: escalar sale)
= (1/2) * (A^T + (A^T)^T)       (propiedad 2 de traspuesta: se distribuye)
= (1/2) * (A^T + A)              (propiedad 1 de traspuesta: (A^T)^T = A)
= (1/2) * (A + A^T)              (la suma de matrices es conmutativa)
```

Como `[(1/2)(A + A^T)]^T = (1/2)(A + A^T)`, la matriz es simetrica.

**Nota del profesor:** a partir de esta propiedad y su analoga antisimetrica, se puede concluir que **cualquier matriz cuadrada se puede escribir como la suma de una simetrica y una antisimetrica**. La parte simetrica es `(1/2)(A + A^T)` y la parte antisimetrica es `(1/2)(A - A^T)`.

---

## Comentarios sobre Conmutatividad

Un estudiante pregunto: si dos matrices son conformables en ambos sentidos (por ejemplo una `3 x 2` y una `2 x 3`), los productos `A * B` y `B * A` dan lo mismo? La respuesta es **no**.

Incluso cuando ambos productos son posibles, generalmente son matrices distintas (y en este caso, de dimensiones distintas: `A * B` seria `3 x 3` y `B * A` seria `2 x 2`).

Incluso matrices **cuadradas** del mismo tamanio generalmente no conmutan.

Los casos especiales que si conmutan son muy pocos:
- La **matriz nula** conmuta con cualquiera: `A * 0 = 0 * A = 0`
- La **matriz identidad** conmuta con cualquiera: `A * I = I * A = A`
- Cualquier **matriz consigo misma**: `A * A = A * A`
- Una matriz con su **inversa** (cuando existe): `A * A^(-1) = A^(-1) * A = I`

Pero estos son excepciones. La regla general es: **las matrices no conmutan**.

En el practico hay un ejercicio que pide encontrar **todas** las matrices que conmutan con una matriz dada `A`. La solucion es un conjunto infinito de matrices que satisfacen ciertas condiciones.

---

## Temas Pendientes para la Proxima Clase

El profesor menciono que en la proxima clase se veran:

- **Matriz inversa:** definicion, como calcularla, propiedades, y ejemplo de una matriz invertible y una que no lo es
- **Induccion completa:** herramienta de demostracion necesaria para el ejercicio 4 del practico
- **Matriz nilpotente:** una matriz `A` es nilpotente de grado `k` si `A^k = 0` (la nula), donde `k` es el primer exponente para el cual esto sucede

---

## Anuncios Administrativos

- **Primera evaluacion continua:** miercoles 25 de marzo, 9:30 PM (en horario de clase)
- **Formato:** maximo 30 minutos, grupos de hasta 3 personas, entrega individual, con material de consulta, **sin dispositivos electronicos**
- **Tipo de ejercicio:** similar a los vistos en los practicos

---

## Definiciones para el Parcial

**Traspuesta:** Dada `A` de `m x n`, su traspuesta `A^T` es de `n x m` y se obtiene intercambiando filas por columnas. La entrada `(A^T)_ji = a_ij`.

**Matriz simetrica:** Matriz cuadrada que cumple `A^T = A`. Equivale a que `a_ij = a_ji` para todo `i, j` — hay simetria respecto de la diagonal principal.

**Matriz antisimetrica:** Matriz cuadrada que cumple `A^T = -A`. Equivale a que `a_ij = -a_ji` para todo `i, j` — la diagonal principal es toda ceros y las entradas simetricas son opuestas.

**Traza:** Para una matriz cuadrada `A` de `n x n`, `tr(A) = a_11 + a_22 + ... + a_nn` (suma de la diagonal principal).

**Propiedad clave de la traspuesta del producto:** `(A * B)^T = B^T * A^T` — el orden se invierte.

**Propiedad clave de la traza del producto:** `tr(A * B) = tr(B * A)` — las matrices pueden ser distintas (incluso de distinta dimension), pero la traza es la misma.

---

## Posibles Preguntas para el Parcial

**Que es la traspuesta de una matriz y como se obtiene?**
Es la matriz que resulta de intercambiar filas por columnas. Si `A` es `m x n`, entonces `A^T` es `n x m`, y la entrada `(i,j)` de `A^T` es la entrada `(j,i)` de `A`.

**Por que `(A * B)^T = B^T * A^T` y no `A^T * B^T`?**
Porque las matrices no conmutan. Si fuera `A^T * B^T`, estariamos asumiendo que `A^T * B^T = B^T * A^T`, lo cual generalmente es falso.

**Que condicion deben cumplir los elementos de la diagonal de una matriz antisimetrica?**
Deben ser todos cero, porque al transponer la diagonal no cambia, pero la definicion exige que `A^T = -A`, asi que `a_ii = -a_ii`, lo cual solo se cumple si `a_ii = 0`.

**Que pasa si sumas una matriz antisimetrica con su traspuesta?**
Da la matriz nula, porque `A + A^T = A + (-A) = 0`.

**La traza de `A * B` es igual a la traza de `B * A`. Significa que `A * B = B * A`?**
No. Las matrices `A * B` y `B * A` generalmente son diferentes (pueden incluso tener dimensiones distintas). Lo que coincide es unicamente la suma de sus diagonales principales.

**Como se demuestra que la suma de dos matrices simetricas es simetrica?**
Se transpone `A + B` usando la propiedad `(A + B)^T = A^T + B^T`, y como ambas son simetricas (`A^T = A`, `B^T = B`), queda `A^T + B^T = A + B`. Entonces `(A + B)^T = A + B`.

**Que resultado se obtiene al multiplicar una matriz por un vector canonico `e_k`?**
Se obtiene la columna `k` de la matriz.

**Que significa que A * B sea simetrica cuando A y B ya son simetricas?**
Significa que A y B conmutan (`A * B = B * A`). Es un si y solo si: A * B es simetrica si y solo si A y B conmutan.

**Toda matriz cuadrada se puede escribir como suma de una simetrica y una antisimetrica?**
Si. La parte simetrica es `(1/2)(A + A^T)` y la parte antisimetrica es `(1/2)(A - A^T)`.

---

Documento generado mediante analisis exhaustivo (3 pasadas) de la transcripcion de la clase del 18-03-2026 del curso de Algebra Lineal, profesor Gabriel Cisneros, ORT Uruguay.