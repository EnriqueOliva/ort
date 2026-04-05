# Explicacion de Temas - Clase del 24-03-2026: Matriz Inversa, Induccion Completa, y Propiedades de la Traza

## La Gran Pregunta: Si no existe "dividir" entre matrices, como se "deshace" una multiplicacion de matrices?

En los numeros reales, si tenemos `3 * x = 6`, dividimos ambos lados por 3 y obtenemos `x = 2`. Pero en matrices **no existe la division**. Entonces, como despejamos una matriz cuando esta "atrapada" en un producto? La respuesta es la **matriz inversa**: una matriz especial que, al multiplicarla por la original, da la identidad (el equivalente al 1 en numeros). Esta clase gira alrededor de esa idea: definir que es la inversa, como encontrarla, que propiedades tiene, y como usarla para resolver problemas que van desde despejar ecuaciones matriciales hasta elevar matrices a potencias enormes como 2019.

---

## Conexion con la Clase Anterior

En la clase del 18-03-2026 se vieron la **traspuesta** (intercambiar filas por columnas), las **matrices simetricas** (`A^T = A`) y **antisimetricas** (`A^T = -A`), y la **traza** (suma de la diagonal principal) con sus cuatro propiedades. Se enfatizo que la traspuesta de un producto **invierte el orden**: `(A * B)^T = B^T * A^T`. Esa inversion de orden va a reaparecer hoy con la inversa. Tambien se demostro que `tr(A * B) = tr(B * A)` — propiedad que hoy se va a usar en una demostracion por el absurdo.

---

## Definicion de Matriz Inversa

### Que es una matriz invertible

> "Siempre que hablamos de matriz inversa estamos en matrices cuadradas"

**Traduccion:** La inversa solo tiene sentido para matrices cuadradas (`n x n`). No se habla de inversa para matrices rectangulares.

Formalmente: sea `A` perteneciente a `M_nxn(R)` (matrices cuadradas `n x n` con entradas reales). Diremos que `A` es **invertible** (o que "tiene inversa") si y solo si existe una matriz `B` tal que:

```
A * B = B * A = I
```

Que significa esto?
- `A` = la matriz original
- `B` = la matriz que estamos buscando
- `I` = la matriz identidad (unos en la diagonal, ceros en el resto)
- La formula completa dice: si multiplicamos A por B (en cualquier orden) y obtenemos la identidad, entonces B es la inversa de A

La notacion para la inversa de `A` es `A^(-1)` ("A a la menos uno"). Es simplemente notacion, **no** significa elevar a una potencia negativa en el sentido aritmetico.

> "Si existe esa matriz B le llamamos, decimos que B es la inversa de A, y la notacion es A a la menos uno"

**Traduccion:** Si encontramos una matriz que al multiplicar por A da la identidad, a esa matriz la llamamos "la inversa de A" y la escribimos `A^(-1)`.

**Analogia:** En los numeros reales, el inverso de 3 es `1/3`, porque `3 * (1/3) = 1` (el neutro de la multiplicacion). En matrices, la inversa de `A` es `A^(-1)`, porque `A * A^(-1) = I` (la identidad, que es el neutro del producto de matrices). Pero puede pasar que una matriz **no tenga inversa** — asi como el 0 no tiene inverso multiplicativo en los reales.

---

## Metodo Directo para Hallar la Inversa

### Planteamiento general

El **metodo directo** consiste en:
1. Plantear una matriz generica `B` con variables como entradas
2. Multiplicar `A * B`
3. Igualar el resultado a la identidad `I`
4. Resolver el sistema de ecuaciones que resulta
5. Si el sistema tiene solucion, la inversa existe y es esa solucion. Si no tiene solucion, la matriz no es invertible.

> "Queremos hallar una matriz B que la multiplico por A y me da la identidad"

**Traduccion:** El plan es sencillo — buscar una matriz desconocida tal que al multiplicarla por la original, el producto sea la identidad.

### Ejemplo 1: Matriz invertible (2x2)

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

Para resolver, el profesor hizo `-3 * (1) + (3)`:
- Se cancelan las `a`: `-3a + 3a = 0`
- Queda: `-6c - 4c = -10c`
- Del otro lado: `-3 + 0 = -3`
- Entonces: `c = 3/10`

Con `c = 3/10`, de la ecuacion (1): `a = 1 - 2(3/10) = 1 - 6/10 = 4/10 = 2/5`

Analogamente, `-3 * (2) + (4)` nos da: `-10d = 1`, entonces `d = -1/10`

Con `d = -1/10`, de la ecuacion (2): `b = -2(-1/10) = 2/10 = 1/5`

Por lo tanto:

```
A^(-1) = | 2/5    1/5  |
         | 3/10  -1/10 |
```

### Ejemplo 2: Matriz NO invertible (2x2)

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
- Se cancelan las `a` y las `c`: `-2a + 2a = 0`, `-4c + 4c = 0`
- Queda: `0 = -2`

> "Si llegamos a esto, el sistema no tiene solucion"

**Traduccion:** `0 = -2` es una contradiccion. Significa que no existen numeros `a, b, c, d` que satisfagan las cuatro ecuaciones simultaneamente. Por lo tanto, no existe la inversa. La matriz `C` **no es invertible**.

**Observacion importante:** el profesor aclaro que este metodo funciona para cualquier dimension. En `3x3` la matriz generica tiene 9 entradas y el sistema tiene 9 ecuaciones. En `4x4` son 16. El planteamiento es el mismo, solo cambia la cantidad de cuentas.

> "Por ahora este es el metodo que tenemos"

**Traduccion:** Mas adelante (despues de vacaciones) se veran otros metodos para hallar la inversa: mediante el **determinante** y mediante **sistemas de ecuaciones** (metodo de escalonamiento). Por ahora, el unico metodo disponible es el directo.

---

## Propiedades de la Inversa

Sea `A` perteneciente a `M_nxn(R)`, `A` invertible. Se cumplen:

### Propiedad 1: La inversa es unica

Si existe una matriz `B` tal que `A * B = B * A = I`, esa matriz `B` es la unica con esa propiedad.

### Propiedad 2: (A^(-1))^(-1) = A

> "Si a la matriz le hago la inversa, y a la inversa le vuelvo a hacer la inversa, vuelvo a la matriz original"

**Traduccion:** La inversa de la inversa es la matriz original. Es como deshacer el "deshacer".

**Analogia:** El inverso multiplicativo de 3 es `1/3`. El inverso multiplicativo de `1/3` es 3. Volves al numero original.

Esto es analogo a lo que pasaba con la traspuesta: `(A^T)^T = A`.

### Propiedad 3: (A * B)^(-1) = B^(-1) * A^(-1) (SE INVIERTE EL ORDEN)

> "La inversa de A por B es igual a B inversa por A inversa"

**Traduccion:** Cuando tomas la inversa de un producto de matrices, el resultado es el producto de las inversas **pero en orden invertido**. Primero va `B^(-1)` y despues `A^(-1)`, al reves de como estaban.

> "Esto no es igual a la inversa de A por la inversa de B porque no conmutan"

**Traduccion:** No podes escribir `A^(-1) * B^(-1)` en vez de `B^(-1) * A^(-1)` porque las matrices generalmente no conmutan. Cambiar el orden cambia el resultado.

**Analogia:** Igual que con la traspuesta del producto `(A * B)^T = B^T * A^T`, la inversa del producto invierte el orden. Pensalo como ponerte medias y zapatos: primero medias, despues zapatos. Para sacartelos: primero zapatos, despues medias. El orden se invierte.

### Demostracion de la Propiedad 3 (hecha en clase)

Queremos probar que `(A * B)^(-1) = B^(-1) * A^(-1)`.

Estrategia: multiplicamos `A * B` por `B^(-1) * A^(-1)` y mostramos que da la identidad.

```
(A * B) * (B^(-1) * A^(-1))
```

Aplicamos la **propiedad asociativa** (podemos cambiar parentesis sin cambiar orden):

```
= A * (B * B^(-1)) * A^(-1)      (asociativa)
= A * I * A^(-1)                   (definicion de inversa: B * B^(-1) = I)
= A * A^(-1)                       (I es neutro del producto: A * I = A)
= I                                 (definicion de inversa: A * A^(-1) = I)
```

Como el producto dio la identidad, queda demostrado que `B^(-1) * A^(-1)` es la inversa de `A * B`.

> "No podes mover el A inversa... acuerdate que no conmuta, no podes cambiar el orden"

**Traduccion:** Un estudiante pregunto si se podia pasar `A^(-1)` al otro lado. La respuesta es no: como el producto de matrices no es conmutativo, **jamas** se puede cambiar el orden de los factores. Siempre hay que multiplicar del mismo lado.

---

## Matrices Idempotentes

### Definicion

Sea `A` perteneciente a `M_nxn(R)`. Diremos que `A` es **idempotente** si y solo si:

```
A^2 = A
```

Que significa esto?
- `A^2` = `A * A` (la matriz multiplicada por si misma)
- `A` = la matriz original
- La formula completa dice: si multiplicas la matriz por si misma y te queda exactamente igual, la matriz es idempotente

**Analogia:** En los numeros reales, los unicos numeros que cumplen `x^2 = x` son `x = 0` y `x = 1` (porque `0^2 = 0` y `1^2 = 1`). En matrices pasa algo parecido pero hay mas opciones.

### Demostracion: si A es idempotente e invertible, entonces A = I

**Hipotesis:** `A^2 = A` y `A` es invertible (existe `A^(-1)`)

**Tesis:** `A = I`

> "Como existe la inversa de A, puedo multiplicar por la inversa a ambos lados"

**Traduccion:** La clave es que, como `A` tiene inversa, podemos "cancelar" una de las `A` del lado izquierdo multiplicando por `A^(-1)`.

```
A^2 = A                            (hipotesis: idempotente)
A * A = A                          (reescribimos A^2 como A * A)
A^(-1) * (A * A) = A^(-1) * A     (multiplicamos por A^(-1) por la IZQUIERDA en ambos lados)
(A^(-1) * A) * A = I               (asociativa a la izquierda, definicion de inversa a la derecha)
I * A = I                           (definicion de inversa: A^(-1) * A = I)
A = I                               (I es neutro del producto: I * A = A)
```

Por lo tanto `A = I`.

**Punto clave del profesor:** siempre que multiplicas por la inversa, tiene que ser **del mismo lado** en ambos miembros de la igualdad. Si multiplicas por la izquierda en un lado, multiplicas por la izquierda en el otro. Nunca mezclar.

### Ejemplo de matriz idempotente que no es la identidad

El profesor pidio un ejemplo de matriz idempotente que no sea `I`. Los estudiantes propusieron:

La **matriz nula** es idempotente: `0 * 0 = 0` (la nula multiplicada por si misma da la nula).

Tambien esta matriz `2x2`:

```
A = | 1  0 |
    | 0  0 |
```

Verificacion: `A * A = A` (el lector puede verificarlo multiplicando).

Notar que estas matrices **no son invertibles** — lo cual es coherente con la demostracion anterior: la unica matriz que es idempotente **e invertible** es la identidad.

---

## Ejercicio Clave: Si A^3 = 0, entonces (A + I) es invertible

### Parte 1: Demostracion

**Hipotesis:** `A` perteneciente a `M_nxn(R)` tal que `A^3 = 0` (la matriz nula)

**Tesis:** `A + I` es invertible, y `(A + I)^(-1) = A^2 - A + I`

> "Si queremos probar que esta matriz es la inversa de esta otra, tengo que multiplicarlas y ver que el resultado me da la identidad"

**Traduccion:** Para demostrar que dos matrices son una la inversa de la otra, basta con multiplicarlas y comprobar que el producto da la identidad.

Multiplicamos `(A + I)` por `(A^2 - A + I)` y aplicamos la **distributiva**:

```
(A + I) * (A^2 - A + I)

= A * A^2 - A * A + A * I + I * A^2 - I * A + I * I

= A^3 - A^2 + A + A^2 - A + I
```

Notas sobre cada termino:
- `A * A^2 = A^3`
- `A * (-A) = -A^2`
- `A * I = A` (la identidad es el neutro)
- `I * A^2 = A^2` (la identidad es el neutro)
- `I * (-A) = -A`
- `I * I = I` (la identidad al cuadrado es la identidad)

Simplificamos:
- `A^2` y `-A^2` se cancelan
- `A` y `-A` se cancelan
- Queda: `A^3 + I`

Aplicamos la hipotesis (`A^3 = 0`):

```
= 0 + I = I
```

Como el producto dio la identidad, queda demostrado que `(A + I)^(-1) = A^2 - A + I`.

> "Si probaste que esta es la inversa, estas probando las dos cosas a la misma vez"

**Traduccion:** Un estudiante pregunto si habia que probar primero que `A + I` es invertible. La respuesta es que al encontrar una matriz que multiplicada da la identidad, estas simultaneamente probando que es invertible Y cual es su inversa.

### Parte 2: Aplicacion a una matriz 4x4 concreta

Hallar la inversa de la matriz:

```
B = | 1  1  0  0 |
    | 0  1  0  1 |
    | 0  0  1  0 |
    | 0  0  0  1 |
```

**Paso 1:** Identificar cual es la matriz `A`.

Si `B = A + I`, entonces `A = B - I`:

```
A = | 1-1  1    0    0  |   | 0  1  0  0 |
    | 0    1-1  0    1  | = | 0  0  0  1 |
    | 0    0    1-1  0  |   | 0  0  0  0 |
    | 0    0    0    1-1|   | 0  0  0  0 |
```

**Paso 2:** Verificar que estamos en la hipotesis (`A^3 = 0`).

Primero calculamos `A^2 = A * A`:

```
A^2 = | 0  1  0  0 |   | 0  1  0  0 |   | 0  0  0  1 |
      | 0  0  0  1 | * | 0  0  0  1 | = | 0  0  0  0 |
      | 0  0  0  0 |   | 0  0  0  0 |   | 0  0  0  0 |
      | 0  0  0  0 |   | 0  0  0  0 |   | 0  0  0  0 |
```

Luego `A^3 = A^2 * A`:

```
A^3 = | 0  0  0  1 |   | 0  1  0  0 |   | 0  0  0  0 |
      | 0  0  0  0 | * | 0  0  0  1 | = | 0  0  0  0 | = 0  (matriz nula)
      | 0  0  0  0 |   | 0  0  0  0 |   | 0  0  0  0 |
      | 0  0  0  0 |   | 0  0  0  0 |   | 0  0  0  0 |
```

`A^3 = 0`, asi que estamos en la hipotesis.

**Paso 3:** Calcular la inversa como `A^2 - A + I`:

```
A^2 - A + I = | 0  0  0  1 |   | 0  1  0  0 |   | 1  0  0  0 |
              | 0  0  0  0 | - | 0  0  0  1 | + | 0  1  0  0 |
              | 0  0  0  0 |   | 0  0  0  0 |   | 0  0  1  0 |
              | 0  0  0  0 |   | 0  0  0  0 |   | 0  0  0  1 |
```

```
B^(-1) = | 1  -1  0   1 |
         | 0   1  0  -1 |
         | 0   0  1   0 |
         | 0   0  0   1 |
```

> "La clave aca es darnos cuenta que estamos en la hipotesis"

**Traduccion:** Lo mas importante del ejercicio no es la cuenta en si, sino el razonamiento: identificar que la matriz dada se puede expresar como `A + I`, verificar que `A^3 = 0`, y recien entonces aplicar la formula. Si `A^3` no fuera la nula, no se podria usar este metodo.

---

## Demostracion por Induccion Completa

### Que es la induccion completa

La induccion completa tiene **tres pasos**:

1. **Paso base:** verificar que la propiedad se cumple para el minimo valor de `n` (generalmente `n = 1`)
2. **Hipotesis inductiva:** suponer que se cumple para `n = h`
3. **Tesis inductiva + Demostracion:** probar que, si se cumple para `h`, entonces se cumple para `h + 1`

**Analogia:** Es como una fila infinita de fichas de domino. El paso base es empujar la primera ficha. La hipotesis y la tesis dicen: "si la ficha `h` cae, la ficha `h+1` tambien cae". Si ambas cosas son ciertas, todas las fichas caen.

### Ejemplo 1: Potencia de una matriz 2x2

**Enunciado:** Sea `A = [[1, 1], [0, 1]]`. Demostrar por induccion completa que:

```
A^n = | 1  n |
      | 0  1 |
```

**Paso base** (`n = 1`):

```
A^1 = | 1  1 | = | 1  1 |
      | 0  1 |   | 0  1 |
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
A^(h+1) = A^h * A                          (propiedad de potencias)

        = | 1  h | * | 1  1 |              (sustituimos A^h por la hipotesis)
          | 0  1 |   | 0  1 |

        = | 1*1+h*0   1*1+h*1 |            (multiplicamos)
          | 0*1+1*0   0*1+1*1 |

        = | 1  1+h |
          | 0  1   |
```

Llegamos a `[[1, h+1], [0, 1]]`, que es exactamente la tesis. Queda demostrado.

### Ejemplo 2: Potencia de una matriz diagonal

**Enunciado:** Si `A` es una matriz **diagonal** `n x n`, demostrar que:

```
A^k = | a_11^k    0      ...    0     |
      |   0     a_22^k   ...    0     |
      |  ...     ...     ...   ...    |
      |   0       0      ...  a_nn^k  |
```

Es decir, elevar una matriz diagonal a la `k` es lo mismo que elevar a la `k` cada elemento de la diagonal principal.

**Paso base** (`k = 1`):

```
A^1 = | a_11^1    0      ...    0     |   | a_11    0      ...    0     |
      |   0     a_22^1   ...    0     | = |   0   a_22     ...    0     |  = A
      |  ...     ...     ...   ...    |   |  ...   ...     ...   ...    |
      |   0       0      ...  a_nn^1  |   |   0     0      ...  a_nn   |
```

Se cumple.

**Hipotesis inductiva** (se cumple para `k = h`):

```
A^h = | a_11^h    0      ...    0     |
      |   0     a_22^h   ...    0     |
      |  ...     ...     ...   ...    |
      |   0       0      ...  a_nn^h  |
```

**Demostracion:**

```
A^(h+1) = A^h * A
```

Como `A^h` es diagonal (por hipotesis) y `A` es diagonal (por enunciado), al multiplicarlas cada entrada de la diagonal se multiplica entre si:

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

## Ejercicio: A^2 = 4I (Material Complementario)

### Parte 1: Probar que (A - I) es invertible y su inversa es (1/3)(A + I)

**Hipotesis:** `A` perteneciente a `M_nxn(R)` tal que `A^2 = 4I`

**Tesis:** `(A - I)^(-1) = (1/3)(A + I)`

Estrategia: multiplicamos `(A - I)` por `(1/3)(A + I)` y mostramos que da la identidad.

> "El un tercio lo puedo sacar para afuera"

**Traduccion:** Por la propiedad `B * (k * A) = k * (B * A)`, podemos sacar el escalar `1/3` afuera del producto para simplificar.

```
(A - I) * (1/3)(A + I) = (1/3) * (A - I) * (A + I)
```

Aplicamos distributiva:

```
(A - I) * (A + I) = A^2 + A * I - I * A - I^2
                   = A^2 + A - A - I
                   = A^2 - I
```

**Nota importante:** `A * I = A` y `I * A = A` — la identidad conmuta con **todas** las matrices. Entonces `A * I - I * A = A - A = 0`, y se cancelan.

Aplicamos la hipotesis (`A^2 = 4I`):

```
= (1/3) * (4I - I)
= (1/3) * 3I
= I
```

Como el producto dio la identidad: `(A - I)^(-1) = (1/3)(A + I)`.

### Parte 2: Aplicacion con matrices 2x2 concretas

Dadas:

```
A = | 8/5    6/5  |       B = | 3/5    6/5  |
    | 6/5   -8/5  |           | 6/5   -3/5  |
```

**Paso A:** Verificar que `A^2 = 4I`.

```
A * A = | (8/5)(8/5) + (6/5)(6/5)      (8/5)(6/5) + (6/5)(-8/5)  |
        | (6/5)(8/5) + (-8/5)(6/5)     (6/5)(6/5) + (-8/5)(-8/5) |

      = | 64/25 + 36/25    48/25 - 48/25  |
        | 48/25 - 48/25    36/25 + 64/25  |

      = | 100/25    0     |   | 4  0 |
        |   0     100/25  | = | 0  4 | = 4I
```

Se cumple la hipotesis.

**Paso B:** Observar que `B = A - I`.

```
A - I = | 8/5 - 1    6/5      |   | 3/5    6/5  |
        | 6/5       -8/5 - 1  | = | 6/5   -13/5 |
```

Atencion: el profesor corrigio durante la clase que la entrada `(2,2)` de `B` era `-3/5`, no `-13/5`. Con la matriz correcta `A = [[8/5, 6/5], [6/5, -8/5]]` y `B = A - I`, la inversa se calcula como:

```
B^(-1) = (1/3)(A + I)
```

Donde:

```
A + I = | 8/5 + 1    6/5      |   | 13/5   6/5  |
        | 6/5       -8/5 + 1  | = | 6/5   -3/5  |
```

Entonces:

```
B^(-1) = (1/3) * | 13/5   6/5  | = | 13/15   6/15  | = | 13/15   2/5  |
                  | 6/5   -3/5  |   | 6/15   -3/15  |   | 2/5    -1/5  |
```

> "La clave estaba en darse cuenta que la matriz B era A menos la identidad"

**Traduccion:** El truco de este ejercicio no es hacer cuentas — es **reconocer** que `B = A - I` y que como `A^2 = 4I`, podemos usar la formula demostrada en la parte 1.

---

## Ejercicio: C = B^(-1) * A * B — Hallar C^2019

### Enunciado

Dadas:

```
A = | 1   0   0 |       B perteneciente a M_3x3(R), B invertible
    | 0  -1   0 |
    | 0   0   2 |

C = B^(-1) * A * B
```

Hallar `C^2019` en funcion de `B`, `B^(-1)`, y potencia de algun numero natural.

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
= B^(-1) * A^2 * (B * B^(-1)) * A * B
= B^(-1) * A^2 * A * B
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

`A` es una **matriz diagonal**, asi que por lo demostrado por induccion completa, elevarla a la 2019 es elevar cada entrada de la diagonal:

```
A^2019 = | 1^2019      0          0       |
         |    0     (-1)^2019      0       |
         |    0         0       2^2019     |
```

Ahora:
- `1^2019 = 1` (1 elevado a cualquier potencia es 1)
- `(-1)^2019 = -1` (porque 2019 es **impar**; `-1` elevado a impar da `-1`, a par da `1`)
- `2^2019` queda como esta (es un numero enorme)

```
A^2019 = | 1    0       0      |
         | 0   -1       0      |
         | 0    0    2^2019    |
```

**Resultado final:**

```
C^2019 = B^(-1) * | 1    0       0      | * B
                   | 0   -1       0      |
                   | 0    0    2^2019    |
```

> "Solo con C cuadrado y C cubo ya podes generalizar"

**Traduccion:** No necesitas hacer induccion completa aca — como la letra pide "hallar una expresion" y no "demostrar", basta con ver el patron en los primeros casos.

---

## Propiedades de la Traza: tr(A - B) = tr(A) - tr(B)

### Demostracion

Usando las propiedades vistas en la clase anterior:

**Propiedad conocida 1:** `tr(A + B) = tr(A) + tr(B)` (la traza de la suma es la suma de las trazas)

**Propiedad conocida 2:** `tr(alfa * A) = alfa * tr(A)` (el escalar sale de la traza)

Entonces:

```
tr(A - B) = tr(A + (-1) * B)           (reescribimos la resta como suma con -1 * B)
          = tr(A) + tr((-1) * B)        (por propiedad 1)
          = tr(A) + (-1) * tr(B)        (por propiedad 2, con alfa = -1)
          = tr(A) - tr(B)
```

### Verificacion con ejemplo numerico

Dadas las matrices `3x3`:

```
A = | 1  0  2 |       B = | 2  1  0 |
    | 1  2  1 |           | 0  1  3 |
    | 0  3  2 |           | 2  1  1 |
```

- `tr(A) = 1 + 2 + 2 = 5`
- `tr(B) = 2 + 1 + 1 = 4`

Calculamos `A - B`:

```
A - B = | -1  -1   2 |
        |  1   1  -2 |
        | -2   2   1 |
```

- `tr(A - B) = -1 + 1 + 1 = 1`

Verificamos: `tr(A) - tr(B) = 5 - 4 = 1`. Coincide.

---

## Prueba por el Absurdo: No existen A, B tales que AB - BA = I

### Enunciado

Probar que no existen dos matrices `A, B` pertenecientes a `M_nxn(R)` tales que `A * B - B * A = I`.

### Que es probar por el absurdo

> "Vamos a suponer que el enunciado es cierto, y si llegamos a una contradiccion, es que no puede ser cierto"

**Traduccion:** Asumimos que SI existen esas matrices. Si esa suposicion nos lleva a algo imposible (como `0 = n`), entonces nuestra suposicion era falsa.

### Demostracion

**Supongamos** que existen `A, B` tales que `A * B - B * A = I`.

Tomamos la traza de ambos lados:

**Lado derecho:**

```
tr(I) = 1 + 1 + ... + 1 = n     (la identidad tiene n unos en la diagonal)
```

**Lado izquierdo:**

```
tr(A * B - B * A) = tr(A * B) - tr(B * A)     (por la propiedad que acabamos de probar)
```

Pero recordemos la propiedad de la traza vista en el teorico:

```
tr(A * B) = tr(B * A)        (siempre se cumple, incluso si A*B ≠ B*A)
```

> "A por B es una matriz, B por A es otra, pero sumo las diagonales principales y me da lo mismo. Es algo bastante curioso."

**Traduccion:** Aunque `A * B` y `B * A` son matrices distintas (no conmutan), sus trazas son iguales. Las matrices son diferentes, pero la suma de sus diagonales coincide.

Entonces:

```
tr(A * B) - tr(B * A) = tr(A * B) - tr(A * B) = 0
```

Pero dijimos que debia ser igual a `n`:

```
0 = n
```

Esto es una **contradiccion** (porque `n >= 1`, ya que estamos hablando de matrices `n x n` con `n` al menos 1). Por lo tanto, la suposicion de que existen tales matrices es falsa.

**Conclusion:** No existen matrices `A, B` en `M_nxn(R)` tales que `A * B - B * A = I`.

---

## Despeje de Ecuaciones Matriciales

### Ejercicio: Dado AX + X = 2A, hallar X en funcion de A

> "Acuerdense que X es una matriz, no puedo pasar X dividiendo"

**Traduccion:** En matrices **no existe la division**. No se puede "pasar X dividiendo" como hariamos con una variable numerica. Lo que si se puede hacer es multiplicar por la inversa.

> "Lo que es analogo a pasar una matriz dividiendo es multiplicar por la inversa"

**Traduccion:** El equivalente matricial de dividir es multiplicar por la inversa. Si queres "cancelar" una matriz de un lado, la multiplicas por su inversa.

**Paso 1:** Factorizar X.

```
A * X + X = 2A
```

Queremos "sacar factor comun X". Pero ojo: `X` aparece multiplicada por `A` a la izquierda y sola (que es lo mismo que multiplicada por `I`). Entonces:

```
A * X + I * X = 2A
(A + I) * X = 2A
```

**Error comun que el profesor advirtio:** Algunos estudiantes escriben `(A + 1)` — esto esta **MAL**. No se puede sumar un numero a una matriz. Hay que escribir `(A + I)`, donde `I` es la matriz identidad.

> "No puedo sumar un numero a una matriz, tengo que factorizar con la identidad"

**Traduccion:** Cuando factorizamos `X` del termino que esta "solo", en realidad estamos sacando `X` de `I * X` (porque `I * X = X`). Entonces el factor comun queda `(A + I)`.

**Otro error comun:** Escribir `X * (A + I)` en vez de `(A + I) * X`. Esto esta **MAL** porque cambia el orden, y como las matrices no conmutan, `X * (A + I) ≠ (A + I) * X` en general. El factor comun tiene que quedar del **mismo lado** donde estaban las matrices que multiplican a X.

**Paso 2:** Multiplicar por la inversa de `(A + I)` para despejar X.

```
(A + I) * X = 2A
```

Multiplicamos por `(A + I)^(-1)` **por la izquierda** en ambos lados:

```
(A + I)^(-1) * (A + I) * X = (A + I)^(-1) * 2A
I * X = (A + I)^(-1) * 2A
X = (A + I)^(-1) * 2A
```

> "Tengo que multiplicar por la izquierda, asi esto me queda la identidad"

**Traduccion:** Multiplicamos por la izquierda porque `(A + I)` esta a la izquierda de `X`. Si multiplicaramos por la derecha, no se cancelaria.

> "No existe pasar dividiendo, lo que tenemos aca en la herramienta es multiplicar por la inversa a un lado"

**Traduccion:** El unico mecanismo para "despejar" una matriz en un producto es multiplicar por su inversa del lado correcto. Nunca escribir algo como `X = 2A / (A + I)` — esa notacion no existe en matrices.

**Recordatorio:** `A * A^(-1) = I`, pero tambien: si tenemos cualquier expresion `(M)` y la multiplicamos por `(M)^(-1)`, obtenemos `I`. No importa lo que haya dentro del parentesis — lo que importa es que `algo * algo^(-1) = I`.

> "Si vos tenes algo y algo a la menos uno, ese producto te da la identidad"

---

## Anuncios de la Clase

- **Prueba de evaluacion continua manana (25-03-2026)**: nivel basico, con material, grupos de hasta 3 personas, duracion media hora, empieza 9:30
- **Contenido de la prueba:** todo lo visto de matrices (NO incluye induccion completa ni determinantes)
- **Determinantes:** se veran despues de las vacaciones de Semana de Turismo
- **Con esta clase se completa el teorico de matrices**

---

## Definiciones para el Parcial

**Matriz invertible:** Una matriz cuadrada `A` es invertible si existe una matriz `B` (llamada `A^(-1)`) tal que `A * B = B * A = I`.

**Metodo directo:** Plantear `A * B = I` con `B` generica, igualar entrada a entrada para obtener un sistema de ecuaciones, y resolverlo.

**Matriz idempotente:** Una matriz cuadrada `A` tal que `A^2 = A`.

**Induccion completa:** Metodo de demostracion con tres pasos: paso base (verificar para `n = 1`), hipotesis inductiva (suponer para `n = h`), y demostracion (probar para `n = h + 1` usando la hipotesis).

**Prueba por el absurdo:** Suponer que algo es cierto, llegar a una contradiccion, y concluir que no puede ser cierto.

---

## Posibles Preguntas para el Parcial

**Que significa que una matriz sea invertible?**
Que existe otra matriz (su inversa) tal que al multiplicarlas — en cualquier orden — da la identidad. Se nota `A^(-1)`. Puede no existir.

**Como se halla la inversa por el metodo directo?**
Se plantea `A * B = I` con `B` generica (con variables como entradas), se multiplica, se iguala a la identidad entrada a entrada, y se resuelve el sistema de ecuaciones resultante.

**Por que la inversa de (A * B) es B^(-1) * A^(-1) y NO A^(-1) * B^(-1)?**
Porque las matrices no conmutan. El orden se invierte igual que con la traspuesta. Se demuestra multiplicando `(A * B)` por `(B^(-1) * A^(-1))` y usando asociativa para cancelar `B * B^(-1) = I`.

**Si A es idempotente e invertible, que es A?**
La identidad. Se demuestra multiplicando ambos lados de `A^2 = A` por `A^(-1)`.

**Por que no se puede "pasar dividiendo" una matriz?**
Porque la division no esta definida para matrices. Lo que se hace es multiplicar por la inversa del lado correspondiente.

**Por que al factorizar X de la expresion AX + X hay que usar la identidad?**
Porque `X = I * X`, entonces `AX + X = AX + IX = (A + I)X`. No se puede escribir `(A + 1)X` porque no se puede sumar un numero a una matriz.

**Por que no existen A, B tales que AB - BA = I?**
Porque `tr(AB - BA) = tr(AB) - tr(BA) = 0` (ya que `tr(AB) = tr(BA)` siempre), pero `tr(I) = n ≠ 0`. La igualdad `0 = n` es una contradiccion.

**Que dice la propiedad de la potencia de una matriz diagonal?**
Si `A` es diagonal, entonces `A^k` se obtiene elevando a la `k` cada entrada de la diagonal principal. Se demuestra por induccion completa.

---

Documento generado mediante analisis exhaustivo (3 pasadas) de la transcripcion de la clase del 24-03-2026 de Algebra Lineal (FI-2103), ORT Uruguay.