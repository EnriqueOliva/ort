---
pdf_options:
  format: A4
  margin: 15mm 18mm 15mm 18mm
  printBackground: true
  displayHeaderFooter: true
  headerTemplate: '<div></div>'
  footerTemplate: '<div style="width:100%;text-align:center;font-size:9px;color:#888;padding:0 20mm;">Algebra Lineal — Guia Evaluacion Continua 25/03/2026 &emsp;|&emsp; Pag. <span class="pageNumber"></span> / <span class="totalPages"></span></div>'
css: |-
  body {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 11.5px;
    line-height: 1.55;
    color: #111;
  }
  h1 {
    font-size: 20px;
    border-bottom: 2px solid #333;
    padding-bottom: 4px;
    margin-top: 18px;
    page-break-before: auto;
  }
  h2 {
    font-size: 15px;
    margin-top: 14px;
    border-bottom: 1px solid #bbb;
    padding-bottom: 2px;
  }
  h3 { font-size: 13px; margin-top: 10px; }
  hr { border: none; border-top: 1px solid #ccc; margin: 12px 0; }
  code {
    font-family: 'Cascadia Mono', 'Consolas', monospace;
    font-size: 10.5px;
    background: #f4f4f4;
    padding: 1px 4px;
    border-radius: 3px;
    border: 1px solid #ddd;
  }
  pre {
    background: #f8f8f8;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 8px 10px;
    font-size: 10px;
    line-height: 1.5;
    overflow-x: auto;
    page-break-inside: avoid;
  }
  pre code {
    background: none;
    border: none;
    padding: 0;
    font-size: 10px;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    font-size: 10.5px;
    margin: 8px 0;
    page-break-inside: avoid;
  }
  th, td {
    border: 1px solid #bbb;
    padding: 4px 8px;
    text-align: left;
  }
  th { background: #eee; font-weight: bold; }
  blockquote {
    border-left: 3px solid #999;
    padding: 4px 12px;
    margin: 8px 0;
    color: #444;
    font-size: 10.5px;
    page-break-inside: avoid;
  }
  strong { color: #000; }
  p { margin: 4px 0; }
  ul, ol { margin: 4px 0 4px 20px; }
  li { margin: 2px 0; }
---

# Guia de Preparacion — Evaluacion Continua del 25-03-2026

## Que entra en esta evaluacion?

Todo el tema de **matrices** EXCEPTO induccion completa. Segun el profesor:

> "Mañana tenemos la prueba. Va a ver lo que es matrices. Induccion completa no, el resto si. Inversa va. Inversa tambien, si. Acuerdense que es con material y los ejercicios no va a ser un nivel mas bien bajo. No va a ser muy complicado, nada que no haya movido."

**Condiciones:** con material, grupos de hasta 3, ~30 minutos, nivel bajo.

**Referencia de ejercicios resueltos:** practico-matrices-soluciones.md (en carpeta practicoMatrices)

---

## ANTES DE TODO: Que Simbolos Vas a Ver y Que Significan

| Simbolo | Se lee | Significado |
|---------|--------|-------------|
| `A ∈ M_mxn(R)` | "A pertenece a M m por n reales" | Matriz de m filas, n columnas, numeros reales |
| `a_ij` | "a sub i j" | Numero en fila i, columna j de A |
| `A^T` | "A traspuesta" | A con filas y columnas intercambiadas |
| `A^(-1)` | "A inversa" | Matriz que al multiplicar por A da la identidad |
| `I` o `I_n` | "Identidad n por n" | Unos en la diagonal, ceros en el resto |
| `0` | "Matriz nula" | Todo ceros |
| `tr(A)` | "traza de A" | Suma de la diagonal principal de A |
| `k`, `alfa`, `λ` | "k", "alfa", "lambda" | Un numero real cualquiera (escalar) |

---

# TIPO 1: Operaciones Basicas — Suma, Resta, Escalar, Producto

**Ejercicios del practico:** V.1 (operaciones), V.2 (productos)

---

## Sumar o restar dos matrices

**Requisito:** Misma dimension (misma cantidad de filas y columnas).

**Como se hace:** Entrada a entrada.

**Ejemplo (del practico V.1):**

```
A = | 2  -1  4 |    B = | 0   0  1 |
    | 1   0  6 |        | 3   0  5 |
    | 1  -1  2 |        | 3  -2  0 |

A + B = | 2+0   -1+0   4+1 |   | 2  -1  5 |
        | 1+3    0+0   6+5 | = | 4   0  11|
        | 1+3   -1-2   2+0 |   | 4  -3  2 |
```

---

## Multiplicar un escalar por una matriz

**Como se hace:** Multiplicas cada entrada por el numero.

**Ejemplo (del practico V.1, para calcular 2B):**

```
2 * B = | 2*0   2*0   2*1  |   | 0   0   2 |
        | 2*3   2*0   2*5  | = | 6   0  10 |
        | 2*3   2*(-2) 2*0 |   | 6  -4   0 |
```

Despues podes restar: A - 2B = A + (-2B). Es sumar A con la matriz anterior con signo cambiado.

---

## Hallar una matriz D para que una suma de cero

**Ejercicio del practico:** V.1 parte 2 — "Hallar D tal que A + B + C + D = O"

**Como se hace:** Si queremos que A + B + C + D = O (la nula), entonces D tiene que ser la **opuesta** de A + B + C. Simplemente calculas A + B + C y le cambias el signo a cada entrada.

```
Si A + B + C = | 3  0   7 |        entonces D = | -3   0   -7 |
               | 2  4  11 |                      | -2  -4  -11 |
               | 4  2   1 |                      | -4  -2   -1 |
```

---

## Multiplicar dos matrices

### Paso 0: Verificar que se puede (conformabilidad)

El numero de **columnas de la primera** tiene que ser igual al numero de **filas de la segunda**.

```
     Primera        Segunda
  [filas x COLS]  [FILS x columnas]
                ^    ^
                estos dos tienen que coincidir
```

**Ejemplo real del practico V.2** (A es 2x3, B es 3x3, C es 3x2):

```
Producto    Dims                  Resultado
A x B       2x[3] por [3]x3      3=3 SE PUEDE  -->  2x3
A x C       2x[3] por [3]x2      3=3 SE PUEDE  -->  2x2
C x A       3x[2] por [2]x3      2=2 SE PUEDE  -->  3x3
B x C       3x[3] por [3]x2      3=3 SE PUEDE  -->  3x2
B x A       3x[3] por [2]x3      3≠2 NO SE PUEDE
C x B       3x[2] por [3]x3      2≠3 NO SE PUEDE
```

### Paso 1: Calcular cada entrada

Para el numero en [fila F, columna C] del resultado: tomas la **fila F de la primera** y la **columna C de la segunda**, multiplicas par a par, y sumas.

**Ejemplo: A x C (del practico V.2)**

```
A (2x3) = | 2  -1  4 |       C (3x2) = | 1   6 |
           | 1   0  6 |                 | -2  4 |
                                          | 0   5 |

Resultado sera 2x2.

[fila 1, col 1]: (2)(1) + (-1)(-2) + (4)(0) = 2 + 2 + 0 = 4
[fila 1, col 2]: (2)(6) + (-1)(4) + (4)(5) = 12 - 4 + 20 = 28
[fila 2, col 1]: (1)(1) + (0)(-2) + (6)(0) = 1 + 0 + 0 = 1
[fila 2, col 2]: (1)(6) + (0)(4) + (6)(5) = 6 + 0 + 30 = 36

A x C = | 4   28 |
         | 1   36 |
```

**REGLA DE ORO:** A * B generalmente es **distinto** de B * A. NUNCA cambies el orden.

---

# TIPO 2: Traspuesta

---

## Calcular la traspuesta

**Como se hace:** Las filas pasan a ser columnas. Si A es `m x n`, A^T es `n x m`.

```
A = | 1  2  3 |        A^T = | 1  4 |
    | 4  5  6 |               | 2  5 |
                               | 3  6 |
```

## Propiedades de la traspuesta

| Propiedad | Formula | En palabras |
|-----------|---------|-------------|
| Doble traspuesta | `(A^T)^T = A` | Trasponer dos veces = no hacer nada |
| Traspuesta de suma | `(A + B)^T = A^T + B^T` | Se distribuye sobre la suma |
| Escalar por matriz | `(k * A)^T = k * A^T` | El numero sale afuera, no se traspone |
| Traspuesta de producto | `(A * B)^T = B^T * A^T` | **EL ORDEN SE INVIERTE** |

### Traspuesta de escalar por matriz explicada

Si tenes un numero multiplicando a una matriz y te piden la traspuesta de todo eso, el numero "sale afuera" y solo traspones la matriz:

```
k = 3       A = | 1  2 |
                | 3  4 |

(3 * A)^T:
    3 * A = | 3   6 |   -->  trasponer  -->  | 3  9 |
            | 9  12 |                         | 6  12|

O el atajo: 3 * A^T = 3 * | 1  3 | = | 3   9 |     (mismo resultado)
                           | 2  4 |   | 6  12 |
```

### Traspuesta de producto explicada

Cuando traspones un producto de dos matrices, **el orden se da vuelta**: no queda `A^T * B^T`, queda `B^T * A^T`.

```
Si tenes (A * B) y te piden la traspuesta:

    MAL:   A^T * B^T      <-- esto esta MAL
    BIEN:  B^T * A^T      <-- el que estaba segundo pasa a primero
```

Analogia: para ponerte medias y zapatos vas en ese orden (medias -> zapatos). Para sacartelos, vas al reves (zapatos -> medias).

---

## Verificar si una matriz es simetrica

**Ejercicio del practico:** V.5, V.6

Una matriz es simetrica si `A^T = A`. En la practica: verificar que `a_ij = a_ji` para todo par.

```
A = | 1  4  6 |     Verifico: a_12=4=a_21, a_13=6=a_31, a_23=5=a_32. Simetrica.
    | 4  2  5 |
    | 6  5  3 |
```

## Verificar si una matriz es antisimetrica

Una matriz es antisimetrica si `A^T = -A`. Requisitos: diagonal toda ceros, y `a_ij = -a_ji`.

```
A = |  0  -2  -4 |     Diagonal: 0,0,0. a_12=-2, a_21=2 (opuestos). Antisimetrica.
    |  2   0  -6 |
    |  4   6   0 |
```

---

## Demostrar que A+B es simetrica (si A y B lo son)

**Ejercicio del practico:** V.5 parte 1

```
(A + B)^T = A^T + B^T    (propiedad de la traspuesta)
          = A + B          (hipotesis: A^T = A y B^T = B)
```

Mismo patron para λA: `(λA)^T = λA^T = λA`.

---

## Demostrar que ½(A + A^T) es simetrica y ½(A - A^T) es antisimetrica

**Ejercicio del practico:** V.6

```
Simetrica:     (½(A + A^T))^T = ½(A^T + A) = ½(A + A^T)     -->  igual a si misma
Antisimetrica: (½(A - A^T))^T = ½(A^T - A) = -½(A - A^T)    -->  cambia de signo
```

Y cualquier matriz A = ½(A + A^T) + ½(A - A^T) = parte simetrica + parte antisimetrica.

---

# TIPO 3: Traza

---

## Calcular la traza

**Solo matrices cuadradas.** Sumar los numeros de la diagonal principal.

```
A = | 4  7  2 |      tr(A) = 4 + 1 + 5 = 10
    | 1  1  8 |
    | 3  6  5 |
```

## Propiedades de la traza

| Propiedad | Formula | En palabras |
|-----------|---------|-------------|
| Traza de suma | `tr(A + B) = tr(A) + tr(B)` | La traza de la suma = suma de trazas |
| Escalar | `tr(k * A) = k * tr(A)` | El numero sale afuera |
| Traspuesta | `tr(A^T) = tr(A)` | Transponer no cambia la traza |
| Producto | `tr(A * B) = tr(B * A)` | Aunque AB ≠ BA, sus trazas son iguales |

## Verificar una propiedad de la traza

**Como se hace:** Calcular el lado izquierdo y el lado derecho por separado y ver que dan igual.

```
Verificar tr(P - Q) = tr(P) - tr(Q):

1. tr(P) = sumar diagonal de P
2. tr(Q) = sumar diagonal de Q
3. Lado derecho = tr(P) - tr(Q)
4. Calcular P - Q (entrada a entrada)
5. Lado izquierdo = tr(P - Q) = sumar diagonal del resultado
6. Comparar: si son iguales, verificado
```

---

# TIPO 4: Inversa por Metodo Directo

**Ejercicios del practico:** V.9, VI.3

---

## Que es la inversa?

La inversa de A es una matriz A^(-1) que cumple: `A * A^(-1) = A^(-1) * A = I`

**Solo para matrices cuadradas.** No todas la tienen. El metodo directo te dice si existe y cual es.

**Analogia:** El inverso de 3 es 1/3 porque 3 * (1/3) = 1. En matrices: A * A^(-1) = I (identidad = "el 1" de las matrices).

---

## Metodo directo para 2x2 (el mas probable en la evaluacion)

**Ejemplo completo (inspirado en practico V.9, A = [[3,2],[1,1]]):**

**Paso 1:** Plantear A * B = I con B generica

```
| 3  2 | * | a  b | = | 1  0 |
| 1  1 |   | c  d |   | 0  1 |
```

**Paso 2:** Multiplicar el lado izquierdo

```
| 3a + 2c    3b + 2d | = | 1  0 |
|  a + c      b + d  |   | 0  1 |
```

**Paso 3:** Igualar entrada a entrada (4 ecuaciones, 4 incognitas)

```
(1) 3a + 2c = 1
(2) 3b + 2d = 0
(3)  a + c  = 0
(4)  b + d  = 1
```

**Paso 4:** Resolver (a y c con ecuaciones 1 y 3; b y d con 2 y 4)

De (3): a = -c. Sustituyo en (1): 3(-c) + 2c = 1 → -c = 1 → c = -1, a = 1.
De (4): b = 1 - d. Sustituyo en (2): 3(1-d) + 2d = 0 → 3 - d = 0 → d = 3, b = -2.

**Paso 5:** Armar la inversa

```
A^(-1) = |  1  -2 |
          | -1   3 |
```

**Verificacion rapida:** A * A^(-1) = [[3-2, -6+6],[1-1,-2+3]] = [[1,0],[0,1]] = I.

---

## Cuando la inversa NO existe

**Ejemplo (practico V.9, B = [[2,1],[4,2]]):**

```
| 2  1 | * | a  b | = | 1  0 |
| 4  2 |   | c  d |   | 0  1 |

Ecuaciones:
(1) 2a + c  = 1
(3) 4a + 2c = 0

Hago -2*(1) + (3): -4a - 2c + 4a + 2c = -2 + 0  →  0 = -2  CONTRADICCION
```

No tiene solucion. **B no es invertible.**

---

## Propiedades de la inversa

| Propiedad | Formula | En palabras |
|-----------|---------|-------------|
| Unicidad | Solo hay una inversa | Si existe, es unica |
| Doble inversa | `(A^(-1))^(-1) = A` | Invertir dos veces = original |
| Inversa de producto | `(AB)^(-1) = B^(-1) * A^(-1)` | **EL ORDEN SE INVIERTE** |
| Traspuesta de inversa | `(A^T)^(-1) = (A^(-1))^T` | Se puede invertir y trasponer en cualquier orden |

---

# TIPO 5: Inversa Usando una Ecuacion Matricial

**Ejercicios del practico:** V.8, V.10, VI.3

Este es un tipo de ejercicio que aparecio en clase y en el practico. Te dan una ecuacion que cumple la matriz y te piden hallar la inversa a partir de esa ecuacion.

---

## Patron general

Te dan algo como: `A^2 = 2A - Id` (ejercicio V.10) o `A^3 = O` (ejercicio VI.3).

El truco es siempre el mismo: **reordenar la ecuacion hasta que quede algo * A = Id**. Ese "algo" es la inversa.

---

## Ejemplo 1: A^2 = 2A - Id (practico V.10)

```
A^2 = 2A - Id                    (dato)
A^2 - 2A + Id = O                (paso todo a un lado)
A * A - 2A + Id = O              (reescribo A^2 como A*A)
A * (A - 2Id) + Id = O           (factorizo A del primer par)
A * (A - 2Id) = -Id              (paso Id al otro lado)
A * (-(A - 2Id)) = Id            (multiplico por -1)
A * (2Id - A) = Id               (simplifico)
```

Entonces A^(-1) = **2Id - A**. Solo restar A de 2 veces la identidad:

```
A = |  5  -4   2 |        A^(-1) = 2Id - A = | -3   4  -2 |
    |  2  -1   1 |                             | -2   3  -1 |
    | -4   4  -1 |                             |  4  -4   3 |
```

---

## Ejemplo 2: A^3 = O (practico VI.3, visto en clase)

```
Quiero probar que (A + Id)^(-1) = A^2 - A + Id.

Multiplico: (A + Id) * (A^2 - A + Id)
= A^3 - A^2 + A + A^2 - A + Id      (distributiva)
= A^3 + Id                            (-A^2+A^2 y +A-A se cancelan)
= O + Id                              (por hipotesis A^3 = O)
= Id

Como el producto da Id, son inversas.
```

**Para la parte 2** (hallar la inversa de una matriz concreta):

1. Despejar A: la matriz dada = A + Id, entonces A = matriz dada - Id
2. Verificar que A^3 = O (calcular A^2, luego A^3)
3. Si se cumple, la inversa = A^2 - A + Id (solo hacer esas sumas y restas)

---

## Ejemplo 3: -A^3 + 5A^2 - 7A + 3Id = O (practico V.8)

Multiplicar toda la ecuacion por A^(-1):

```
-A^2 + 5A - 7Id + 3A^(-1) = O
3A^(-1) = A^2 - 5A + 7Id
A^(-1) = (1/3)(A^2 - 5A + 7Id)
```

Calcular A^2, sustituir, y simplificar.

---

# TIPO 6: Matrices Idempotentes

**Ejercicio del practico:** VI.2

---

## Que es idempotente?

A es idempotente si `A^2 = A` (se multiplica por si misma y da lo mismo).

## Si A es idempotente e invertible → A es la identidad

```
A * A = A                         (hipotesis: A^2 = A)
A^(-1) * (A * A) = A^(-1) * A    (multiplico por A^(-1) por la izquierda)
(A^(-1) * A) * A = Id            (asociativa + definicion de inversa)
Id * A = Id
A = Id
```

## Ejemplo de idempotente que no sea Id ni O

```
A = | 1  0 |       A^2 = | 1  0 | * | 1  0 | = | 1  0 | = A
    | 0  0 |              | 0  0 |   | 0  0 |   | 0  0 |
```

---

# TIPO 7: Ecuaciones Matriciales (Despejar una Matriz)

---

## Reglas fundamentales

1. **NO existe dividir entre matrices.** Solo multiplicar por la inversa.
2. **Multiplicar del mismo lado** en ambos miembros (izquierda o derecha, no mezclar).
3. **No sumar un numero a una matriz.** Usar la identidad (Id) en vez de 1.
4. **Al factorizar, cuidar el lado.** Si X esta a la derecha en todos los terminos, factorizarla a la derecha.

---

## Ejemplo (de la clase): Despejar X de AX + X = 2A

**Paso 1: Reescribir X como Id * X**

```
A * X + Id * X = 2A
```

**Paso 2: Factorizar X por la derecha** (X estaba a la derecha en ambos terminos)

```
(A + Id) * X = 2A
```

**ERRORES COMUNES:**
- Escribir `X * (A + Id)` → MAL (X estaba a la derecha, no a la izquierda)
- Escribir `(A + 1)` → MAL (no se puede sumar 1 a una matriz, se suma la identidad)

**Paso 3: Multiplicar por (A + Id)^(-1) por la izquierda**

```
(A + Id)^(-1) * (A + Id) * X = (A + Id)^(-1) * 2A
Id * X = (A + Id)^(-1) * 2A
X = (A + Id)^(-1) * 2A
```

---

# TIPO 8: Ley de Simplificacion (AB = A implica B = Id?)

**Ejercicio del practico:** V.11

---

## Si A es invertible: SI se puede simplificar

```
AB = A  y  A es invertible
→  A^(-1) * AB = A^(-1) * A
→  B = Id
```

Lo mismo con AB = AC: si A es invertible, B = C.

## Si A NO es invertible: NO se puede simplificar

Contraejemplo del practico V.11:

```
A = | 0  3 |    B = | 2  1 |    C = | 5  4 |
    | 0  0 |        | 3  0 |        | 3  0 |

AB = AC = | 9  0 |    pero B ≠ C
          | 0  0 |
```

Esto pasa porque A no es invertible (det = 0). **Moraleja:** no "cancelar" matrices a menos que sepas que son invertibles.

---

# TIPO 9: Verdadero o Falso con Contraejemplo

**Ejercicio del practico:** V.14, V.16

---

## A y B invertibles → A + B invertible? **FALSO**

```
A = Id, B = -Id. Ambas invertibles.
A + B = O (nula, no invertible).
```

## A y B invertibles → AB invertible? **VERDADERO**

```
(AB)^(-1) = B^(-1) * A^(-1)
```

## (A+B)^2 = A^2 + 2AB + B^2 ? **FALSO en general**

No vale porque AB ≠ BA. Lo que si vale:

```
(A+B)^2 = (A+B)(A+B) = A^2 + AB + BA + B^2
```

Solo da A^2 + 2AB + B^2 si AB = BA (conmutan).

## A, B simetricas → AB simetrica? **FALSO en general**

Solo es cierto si AB = BA. Contraejemplo en el practico V.16.

## A invertible → (A^T)^(-1) = (A^(-1))^T ? **VERDADERO**

```
A^T * (A^(-1))^T = (A^(-1) * A)^T = Id^T = Id
```

---

# TIPO 10: Demostracion por el Absurdo (AB - BA ≠ I)

---

## Como se demuestra que no existen A, B tales que AB - BA = I

```
Paso 1: Suponer que SI existen A y B con AB - BA = I

Paso 2: Tomar traza del lado derecho
    tr(I) = n     (la identidad n x n tiene n unos en la diagonal)

Paso 3: Tomar traza del lado izquierdo
    tr(AB - BA) = tr(AB) - tr(BA)     (propiedad: traza de resta)
                = tr(AB) - tr(AB)     (propiedad: tr(AB) = tr(BA))
                = 0

Paso 4: Contradiccion
    0 = n    (imposible, porque n >= 1)

Conclusion: No pueden existir tales matrices.
```

---

# RESUMEN FINAL: Formulas en una Pagina

```
TRASPUESTA:
    (A^T)^T = A
    (A + B)^T = A^T + B^T
    (k * A)^T = k * A^T
    (A * B)^T = B^T * A^T              <-- orden invertido

TRAZA:
    tr(A + B) = tr(A) + tr(B)
    tr(k * A) = k * tr(A)
    tr(A^T) = tr(A)
    tr(A * B) = tr(B * A)

INVERSA:
    A * A^(-1) = A^(-1) * A = I
    (A^(-1))^(-1) = A
    (A * B)^(-1) = B^(-1) * A^(-1)    <-- orden invertido
    (A^T)^(-1) = (A^(-1))^T

IDENTIDAD Y NULA:
    A * I = I * A = A                   (neutro del producto)
    A + 0 = 0 + A = A                  (neutro de la suma)

PRODUCTO:
    NO CONMUTATIVO: A * B ≠ B * A      (en general)
    ASOCIATIVO: (A * B) * C = A * (B * C)
    DISTRIBUTIVO: A * (B + C) = A*B + A*C
                  (A + B) * C = A*C + B*C
    ESCALAR: k * (A * B) = (k*A) * B = A * (k*B)

SIMETRICA: A^T = A          ANTISIMETRICA: A^T = -A (diagonal = 0)
IDEMPOTENTE: A^2 = A        INVERTIBLE: existe A^(-1) con A*A^(-1) = I
```

---

# CHECKLIST ANTES DE ENTREGAR

- Las dimensiones cuadran en cada producto?
- Al trasponer o invertir un producto, invertiste el orden?
- Al despejar, multiplicaste por la inversa del **mismo lado** en ambos miembros?
- Al factorizar, X quedo del **lado correcto**?
- No escribiste "dividir" entre matrices?
- No sumaste un numero a una matriz? (usar Id en vez de 1)
- No cambiaste el orden de un producto sin justificacion?
- Si "simplificaste" una matriz, verificaste que sea invertible?
- Simplificaste las fracciones en los resultados?
