# Practico de Matrices — Ejercicios y Soluciones

---

## Ejercicio V.1 — Operaciones basicas (suma, resta, escalar)

**Dadas:**

```
A = | 2  -1  4 |    B = | 0   0  1 |    C = |  1  1   2 |
    | 1   0  6 |        | 3   0  5 |        | -2  4   0 |
    | 1  -1  2 |        | 3  -2  0 |        |  0  5  -1 |
```

### 1(i) Calcular A - 2B

Primero calculo 2B (multiplico cada entrada por 2):

```
2B = | 0   0   2 |
     | 6   0  10 |
     | 6  -4   0 |
```

Luego resto entrada a entrada:

```
A - 2B = | 2-0    -1-0    4-2  |   | 2  -1   2 |
         | 1-6     0-0   6-10  | = | -5   0  -4 |
         | 1-6   -1-(-4)  2-0  |   | -5   3   2 |
```

### 1(ii) Calcular 3A - C

```
3A = | 6  -3  12 |
     | 3   0  18 |
     | 3  -3   6 |

3A - C = | 6-1    -3-1   12-2 |   |  5  -4  10 |
         | 3+2     0-4   18-0 | = |  5  -4  18 |
         | 3-0    -3-5   6+1  |   |  3  -8   7 |
```

### 1(iii) Calcular A + B + C

```
A + B + C = | 2+0+1    -1+0+1   4+1+2  |   | 3  0   7 |
            | 1+3-2     0+0+4   6+5+0  | = | 2  4  11 |
            | 1+3+0    -1-2+5   2+0-1  |   | 4  2   1 |
```

### 2) Hallar D tal que A + B + C + D = O (nula)

Si A + B + C + D = O, entonces D = -(A + B + C). Es decir, la opuesta de la suma anterior:

```
D = | -3   0   -7 |
    | -2  -4  -11 |
    | -4  -2   -1 |
```

---

## Ejercicio V.2 — Productos entre matrices (conformabilidad)

**Dadas:**

```
A (2x3) = | 2  -1  4 |    B (3x3) = | 1   0   1 |    C (3x2) = | 1   6 |
           | 1   0  6 |              | 2  -1   2 |               | -2  4 |
                                      | 3  -2   0 |               | 0   5 |
```

**Primero: cuales productos son posibles?**

| Producto | Dimensiones | Columnas 1ra = Filas 2da? | Resultado |
|----------|-------------|---------------------------|-----------|
| A x B | 2x**3** por **3**x3 | 3 = 3. Se puede | 2x3 |
| A x C | 2x**3** por **3**x2 | 3 = 3. Se puede | 2x2 |
| C x A | 3x**2** por **2**x3 | 2 = 2. Se puede | 3x3 |
| B x C | 3x**3** por **3**x2 | 3 = 3. Se puede | 3x2 |
| B x A | 3x**3** por **2**x3 | 3 ≠ 2. NO se puede | — |
| C x B | 3x**2** por **3**x3 | 2 ≠ 3. NO se puede | — |

**A x B =**

```
Fila 1 de A con cada columna de B:
  (2)(1)+(-1)(2)+(4)(3) = 2-2+12 = 12
  (2)(0)+(-1)(-1)+(4)(-2) = 0+1-8 = -7
  (2)(1)+(-1)(2)+(4)(0) = 2-2+0 = 0

Fila 2 de A con cada columna de B:
  (1)(1)+(0)(2)+(6)(3) = 1+0+18 = 19
  (1)(0)+(0)(-1)+(6)(-2) = 0+0-12 = -12
  (1)(1)+(0)(2)+(6)(0) = 1+0+0 = 1

A x B = | 12   -7   0 |
         | 19  -12   1 |
```

**A x C =**

```
(2)(1)+(-1)(-2)+(4)(0) = 4      (2)(6)+(-1)(4)+(4)(5) = 28
(1)(1)+(0)(-2)+(6)(0) = 1       (1)(6)+(0)(4)+(6)(5) = 36

A x C = |  4  28 |
         |  1  36 |
```

**C x A =**

```
(1)(2)+(6)(1) = 8       (1)(-1)+(6)(0) = -1     (1)(4)+(6)(6) = 40
(-2)(2)+(4)(1) = 0      (-2)(-1)+(4)(0) = 2     (-2)(4)+(4)(6) = 16
(0)(2)+(5)(1) = 5       (0)(-1)+(5)(0) = 0      (0)(4)+(5)(6) = 30

C x A = |  8  -1  40 |
         |  0   2  16 |
         |  5   0  30 |
```

**B x C =**

```
(1)(1)+(0)(-2)+(1)(0) = 1       (1)(6)+(0)(4)+(1)(5) = 11
(2)(1)+(-1)(-2)+(2)(0) = 4      (2)(6)+(-1)(4)+(2)(5) = 18
(3)(1)+(-2)(-2)+(0)(0) = 7      (3)(6)+(-2)(4)+(0)(5) = 10

B x C = |  1  11 |
         |  4  18 |
         |  7  10 |
```

---

## Ejercicio V.3 — Producto por vectores canonicos

**Dada A generica 3x3 y los vectores canonicos:**

```
A = | a11  a12  a13 |       v1 = | 1 |    v2 = | 0 |    v3 = | 0 |
    | a21  a22  a23 |            | 0 |         | 1 |         | 0 |
    | a31  a32  a33 |            | 0 |         | 0 |         | 1 |
```

**Resultados:**

```
A * v1 = | a11 |       A * v2 = | a12 |       A * v3 = | a13 |
         | a21 |                | a22 |                | a23 |
         | a31 |                | a32 |                | a33 |
```

**Conclusion:** Multiplicar una matriz por el vector canonico j-esimo extrae la columna j de la matriz. Todos los resultados son matrices columna en M_3x1(R).

---

## Ejercicio V.4 — Induccion completa (NO ENTRA EN LA EVALUACION)

**Dato:** A = [[1,1,1],[0,1,1],[0,0,1]]. Probar que A^n = [[1,n,n(n+1)/2],[0,1,n],[0,0,1]].

*Ejercicio de induccion completa. El profesor confirmo que induccion NO entra en la evaluacion continua del 25 de marzo.*

---

## Ejercicio V.5 — Propiedades de matrices simetricas

**Enunciado:** Sean A, B simetricas n x n y λ ∈ R.

### Parte 1: Probar que A + B y λA son simetricas

```
(A + B)^T = A^T + B^T        (propiedad de la traspuesta)
          = A + B              (hipotesis: A^T = A, B^T = B)

(λA)^T = λ * A^T              (propiedad de la traspuesta)
       = λ * A                 (hipotesis: A^T = A)
```

Ambas son simetricas.

### Parte 2: AB simetrica si y solo si A y B conmutan

**Ida (AB simetrica → AB = BA):**

```
AB simetrica  →  (AB)^T = AB
Pero (AB)^T = B^T * A^T = B * A     (porque A, B simetricas)
Entonces AB = BA
```

**Vuelta (AB = BA → AB simetrica):**

```
(AB)^T = B^T * A^T = B * A = AB     (por hipotesis AB = BA)
Entonces AB es simetrica
```

---

## Ejercicio V.6 — Descomposicion simetrica/antisimetrica

### Parte 1: ½(A + A^T) es simetrica

```
(½(A + A^T))^T = ½(A + A^T)^T
               = ½(A^T + (A^T)^T)
               = ½(A^T + A)
               = ½(A + A^T)
```

Es igual a si misma al trasponerla, por lo tanto es simetrica.

### Parte 2: ½(A - A^T) es antisimetrica

```
(½(A - A^T))^T = ½(A^T - A)
               = -½(A - A^T)
```

Al trasponerla queda el negativo de si misma, por lo tanto es antisimetrica.

### Parte 3: Cualquier matriz = simetrica + antisimetrica

```
½(A + A^T) + ½(A - A^T) = ½A + ½A^T + ½A - ½A^T = A
```

---

## Ejercicio V.7 — Matrices nilpotentes

**Definicion:** A es nilpotente de grado k si A^k = O (nula) y A^(k-1) ≠ O.

**Dada:**

```
A = | 0  1  1 |
    | 0  0  1 |
    | 0  0  0 |
```

### Parte 1: Probar que A es nilpotente y dar el grado

```
A^2 = | 0  0  1 |      A^3 = A^2 * A = | 0  0  0 |
      | 0  0  0 |                       | 0  0  0 |  = O (nula)
      | 0  0  0 |                       | 0  0  0 |
```

Como A^3 = O y A^2 ≠ O, A es nilpotente de **grado 3**.

### Parte 2: P^(-1)AP es nilpotente del mismo grado

```
(P^(-1)AP)^2 = P^(-1)AP * P^(-1)AP = P^(-1) A (PP^(-1)) A P = P^(-1) A^2 P
(P^(-1)AP)^3 = P^(-1) A^3 P = P^(-1) O P = O
```

Nilpotente de grado 3 tambien.

---

## Ejercicio V.8 — Ecuacion matricial para hallar inversa

**Dada:**

```
A = | 1  1  0 |
    | 0  1  0 |
    | 0  0  3 |
```

### Parte 1: Verificar que -A^3 + 5A^2 - 7A + 3Id = O

```
A^2 = | 1  2  0 |       A^3 = | 1   3   0 |
      | 0  1  0 |             | 0   1   0 |
      | 0  0  9 |             | 0   0  27 |

-A^3       = | -1  -3    0 |
5A^2       = |  5  10    0 |
-7A        = | -7  -7    0 |
3Id        = |  3   0    0 |

Sumando fila 1: -1+5-7+3=0, -3+10-7+0=0, 0+0+0+0=0
Sumando fila 2: 0+0+0+0=0, -1+5-7+3=0, 0+0+0+0=0
Sumando fila 3: 0+0+0+0=0, 0+0+0+0=0, -27+45-21+3=0

Resultado: O (verificado).
```

### Parte 2: Hallar A^(-1) usando la ecuacion

De -A^3 + 5A^2 - 7A + 3Id = O, multiplico todo por A^(-1):

```
-A^2 + 5A - 7Id + 3A^(-1) = O
3A^(-1) = A^2 - 5A + 7Id
A^(-1) = (1/3)(A^2 - 5A + 7Id)
```

```
A^2 - 5A + 7Id = | 1  2  0 |   | 5  5   0 |   | 7  0  0 |   | 3  -3  0 |
                  | 0  1  0 | - | 0  5   0 | + | 0  7  0 | = | 0   3  0 |
                  | 0  0  9 |   | 0  0  15 |   | 0  0  7 |   | 0   0  1 |

A^(-1) = (1/3) * | 3  -3  0 |   | 1  -1    0  |
                  | 0   3  0 | = | 0   1    0  |
                  | 0   0  1 |   | 0   0  1/3  |
```

---

## Ejercicio V.9 — Inversa por metodo directo

### Matriz A = [[3, 2], [1, 1]]

det(A) = 3 - 2 = 1 (distinto de cero, es invertible)

Para 2x2 la formula rapida es: si A = [[a,b],[c,d]], entonces A^(-1) = (1/det) * [[d,-b],[-c,a]]

```
A^(-1) = (1/1) * | 1  -2 |   | 1  -2 |
                  | -1   3 | = | -1   3 |
```

### Matriz B = [[2, 1], [4, 2]]

det(B) = 4 - 4 = 0. **B no es invertible.**

### Matriz C = [[1, 1, -1], [1, -1, 1], [1, 1, 1]]

```
C^(-1) = |  1/2   1/2    0  |
          |   0   -1/2   1/2 |
          | -1/2    0    1/2 |
```

### Matriz D = [[1, 2, 3], [0, 5, 0], [2, 4, 3]]

```
D^(-1) = |  -1   -2/5    1  |
          |   0    1/5    0  |
          |  2/3    0   -1/3 |
```

### Matriz E (4x4) = [[1, 0, 1, -1], [2, 1, 1, 0], [0, 1, 1, 0], [0, -1, 2, 1]]

```
E^(-1) = |   0     1/2   -1/2     0   |
          | -1/4    1/8    5/8   -1/4  |
          |  1/4   -1/8    3/8    1/4  |
          | -3/4    3/8   -1/8    1/4  |
```

*Nota: para 3x3 y 4x4 mas adelante se ve el metodo de Gauss-Jordan que es mas practico.*

---

## Ejercicio V.10 — Inversa a partir de ecuacion A^2 = 2A - Id

**Dada:**

```
A = |  5  -4   2 |
    |  2  -1   1 |
    | -4   4  -1 |
```

### Parte 1: Probar que A^2 = 2A - Id

Calcular A^2 = A * A y verificar que coincide con 2A - Id.

```
2A - Id = | 10  -8   4 |   | 1  0  0 |   |  9  -8   4 |
          |  4  -2   2 | - | 0  1  0 | = |  4  -3   2 |
          | -8   8  -2 |   | 0  0  1 |   | -8   8  -3 |
```

Se verifica que A^2 da exactamente eso.

**Deducir que A es invertible:** De A^2 = 2A - Id, reordenamos:
A^2 - 2A + Id = O → A(A - 2Id) = -Id → A(2Id - A) = Id

Por lo tanto la inversa de A es **(2Id - A)**:

```
A^(-1) = 2Id - A = | -3   4  -2 |
                    | -2   3  -1 |
                    |  4  -4   3 |
```

### Parte 2: A^3 = 3A - 2Id

```
A^3 = A * A^2 = A * (2A - Id) = 2A^2 - A = 2(2A - Id) - A = 3A - 2Id
```

---

## Ejercicio V.11 — Ley de simplificacion

### Parte 1: Si AB = A y A es invertible → B = Id

```
A^(-1) * (AB) = A^(-1) * A
(A^(-1)A) * B = Id
Id * B = Id
B = Id
```

### Parte 2: Si AB = AC y A es invertible → B = C

```
A^(-1) * (AB) = A^(-1) * (AC)
B = C
```

### Parte 3: Contraejemplo cuando A NO es invertible

```
A = | 0  3 |    B = | 2  1 |    C = | 5  4 |
    | 0  0 |        | 3  0 |        | 3  0 |

AB = | 9  0 |    AC = | 9  0 |
     | 0  0 |         | 0  0 |
```

AB = AC pero B ≠ C. Esto es posible porque A **no es invertible** (det = 0). No se puede simplificar.

---

## Ejercicio V.12 — Matriz ortogonal

**Definicion:** A es ortogonal si A es invertible y A^(-1) = A^T.

**Dada:**

```
A = | 4/5    3/5 |
    |  α      β  |
```

Encontrar α y β para que A sea ortogonal.

**Solucion:** A^T * A = Id

```
| 4/5   α | * | 4/5  3/5 | = | 1  0 |
| 3/5   β |   |  α    β  |   | 0  1 |
```

De la entrada (1,1): 16/25 + α^2 = 1 → α^2 = 9/25
De la entrada (2,2): 9/25 + β^2 = 1 → β^2 = 16/25
De la entrada (1,2): 12/25 + αβ = 0 → αβ = -12/25

**Dos soluciones:**

```
α = 3/5, β = -4/5    →    A^(-1) = A^T = | 4/5   3/5 |
                                           | 3/5  -4/5 |

α = -3/5, β = 4/5    →    A^(-1) = A^T = |  4/5  -3/5 |
                                           |  3/5   4/5 |
```

---

## Ejercicio V.13 — Diagonalizacion P^(-1)AP

**Dadas:**

```
A = | 1  2 |    P = | 2  1 |
    | 5  4 |        | x  y |
```

Hallar x e y para que P^(-1)AP = [[6,0],[0,-1]].

**Solucion:** AP = P * [[6,0],[0,-1]]

```
| 1  2 | * | 2  1 | = | 2  1 | * | 6   0 |
| 5  4 |   | x  y |   | x  y |   | 0  -1 |

Lado izquierdo: | 2+2x   1+2y  |
                 | 10+4x  5+4y  |

Lado derecho: | 12  -1 |
               | 6x  -y |

Igualando: 2+2x = 12 → x = 5
           1+2y = -1 → y = -1
```

---

## Ejercicio V.14 — A y B invertibles, es A+B invertible? es AB invertible?

### Parte 1: A+B invertible? **NO necesariamente.**

Contraejemplo: A = Id, B = -Id. Ambas invertibles.

```
A + B = Id + (-Id) = O (la nula)
```

La nula no es invertible. Entonces A + B puede no ser invertible.

### Parte 2: AB invertible? **SI, siempre.**

Si A y B son invertibles, entonces (AB)^(-1) = B^(-1) * A^(-1).

---

## Ejercicio V.15 — Conmutatividad

### Parte 1: Si A conmuta con B y A conmuta con C, entonces A conmuta con D = μB + λC

```
A * D = A(μB + λC) = μAB + λAC = μBA + λCA = (μB + λC)A = D * A
```

### Parte 2: Hallar todas las matrices que conmutan con A = [[1,-1],[1,0]]

Sea B = [[a,b],[c,d]]. Imponemos AB = BA:

```
| 1  -1 | * | a  b | = | a-c    b-d  |
| 1   0 |   | c  d |   |  a      b   |

| a  b | * | 1  -1 | = | a+b   -a  |
| c  d |   | 1   0 |   | c+d   -c  |
```

Igualando: c = -b y d = a + b. Entonces B = [[a, b],[-b, a+b]] para cualquier a, b reales.

Verificacion: A misma conmuta (a=1, b=-1). Id conmuta (a=1, b=0).
D1 = [[2,-1],[1,1]] = A + Id. D2 = [[0,-1],[1,-1]] = A - Id. Ambas conmutan.

---

## Ejercicio V.16 — Verdadero o falso con demostracion/contraejemplo

### Parte 1: (A+B)^2 = A^2 + 2AB + B^2 ? **FALSO en general.**

```
Contraejemplo: A = | 1  0 |    B = | 1  1 |
                    | 1  0 |        | 1  0 |

(A+B)^2 = | 2  1 |^2 = | 6  2 |
           | 2  0 |     | 4  2 |

A^2 + 2AB + B^2 = | 1  0 | + 2| 1  1 | + | 2  1 | = | 6  3 |
                   | 1  0 |    | 1  1 |   | 1  1 |   | 4  3 |
```

No son iguales. Es cierto **solo si AB = BA** (las matrices conmutan).

### Parte 2: A, B simetricas → AB simetrica? **FALSO en general.**

```
Contraejemplo: A = |  1  -1 |    B = | 1  1 |    (ambas simetricas)
                    | -1   2 |        | 1  1 |

AB = | 0  0 |   que NO es simetrica.
     | 1  1 |
```

Es cierto **solo si AB = BA**.

### Parte 3: Si A invertible → A^T invertible y (A^T)^(-1) = (A^(-1))^T ? **VERDADERO.**

```
(A^T) * (A^(-1))^T = (A^(-1) * A)^T = Id^T = Id
```

Por lo tanto (A^(-1))^T es la inversa de A^T.

---

## Ejercicio V.17 — Opcional (no relevante para evaluacion)

Ejercicio sobre conmutatividad con λId. Omitido por ser opcional.

---

# SECCION VI: EVALUACION

---

## Ejercicio VI.1 — Induccion completa (NO ENTRA)

Probar por induccion que [[1,1],[0,1]]^n = [[1,n],[0,1]].

*Excluido de la evaluacion continua del 25 de marzo.*

---

## Ejercicio VI.2 — Matrices idempotentes

**Definicion:** A es idempotente si A^2 = A.

### Parte 1: Si A idempotente e invertible → A = Id

```
A^2 = A                         (hipotesis: idempotente)
A^(-1) * A^2 = A^(-1) * A      (multiplico por A^(-1) por la izquierda)
A = Id
```

### Parte 2: Ejemplo de idempotente que no sea Id ni O

```
A = | 1  0 |       A^2 = | 1  0 | * | 1  0 | = | 1  0 | = A
    | 0  0 |              | 0  0 |   | 0  0 |   | 0  0 |
```

Tambien la nula funciona: O^2 = O. Pero se pide una que no sea ni Id ni O, y la de arriba cumple.

---

## Ejercicio VI.3 — Inversa usando A^3 = O

**Dato:** A^3 = O (nula).

### Parte 1: Demostrar que (A + Id)^(-1) = A^2 - A + Id

```
(A + Id) * (A^2 - A + Id)

= A^3 - A^2 + A + A^2 - A + Id     (distributiva)

= A^3 + Id                          (se cancelan -A^2+A^2 y +A-A)

= O + Id                            (por hipotesis A^3 = O)

= Id
```

Como el producto da Id, una es la inversa de la otra.

### Parte 2: Hallar la inversa de la matriz 4x4

```
Dada la matriz: B = | 1  1  0  0 |
                     | 0  1  0  1 |
                     | 0  0  1  0 |
                     | 0  0  0  1 |
```

**Paso 1:** Identificar A tal que B = A + Id

```
A = B - Id = | 0  1  0  0 |
             | 0  0  0  1 |
             | 0  0  0  0 |
             | 0  0  0  0 |
```

**Paso 2:** Verificar que A^3 = O

```
A^2 = | 0  0  0  1 |       A^3 = A^2 * A = | 0  0  0  0 |
      | 0  0  0  0 |                        | 0  0  0  0 | = O
      | 0  0  0  0 |                        | 0  0  0  0 |
      | 0  0  0  0 |                        | 0  0  0  0 |
```

Estamos en las hipotesis.

**Paso 3:** B^(-1) = A^2 - A + Id

```
A^2       = | 0  0  0  1 |
             | 0  0  0  0 |
             | 0  0  0  0 |
             | 0  0  0  0 |

-A        = | 0  -1  0   0 |
             | 0   0  0  -1 |
             | 0   0  0   0 |
             | 0   0  0   0 |

Id        = | 1  0  0  0 |
             | 0  1  0  0 |
             | 0  0  1  0 |
             | 0  0  0  1 |

B^(-1) = | 1  -1  0   1 |
          | 0   1  0  -1 |
          | 0   0  1   0 |
          | 0   0  0   1 |
```
