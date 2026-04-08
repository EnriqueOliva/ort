---
pdf_options:
  format: A4
  margin: 12mm 14mm 12mm 14mm
  printBackground: true
  displayHeaderFooter: true
  headerTemplate: '<div></div>'
  footerTemplate: '<div style="width:100%;text-align:center;font-size:8px;color:#888;padding:0 16mm;">Algebra Lineal — Resumen Teorico &emsp;|&emsp; Pag. <span class="pageNumber"></span> / <span class="totalPages"></span></div>'
css: |-
  body {
    font-family: 'Segoe UI', Calibri, Arial, sans-serif;
    font-size: 10.5px;
    line-height: 1.45;
    color: #111;
    columns: 2;
    column-gap: 18px;
  }
  h1 {
    font-size: 17px;
    border-bottom: 2px solid #333;
    padding-bottom: 3px;
    margin-top: 0;
    column-span: all;
  }
  h2 {
    font-size: 12.5px;
    margin-top: 10px;
    margin-bottom: 4px;
    border-bottom: 1px solid #bbb;
    padding-bottom: 2px;
    column-span: all;
  }
  h3 {
    font-size: 11px;
    margin-top: 8px;
    margin-bottom: 2px;
  }
  hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 8px 0;
    column-span: all;
  }
  code {
    font-family: 'Cascadia Mono', 'Consolas', monospace;
    font-size: 9.5px;
    background: #f0f0f0;
    padding: 0px 3px;
    border-radius: 2px;
    border: 1px solid #ddd;
  }
  pre {
    background: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 3px;
    padding: 5px 7px;
    font-size: 9px;
    line-height: 1.4;
    overflow-x: auto;
    break-inside: avoid;
  }
  pre code {
    background: none;
    border: none;
    padding: 0;
    font-size: 9px;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    font-size: 9.5px;
    margin: 5px 0;
    break-inside: avoid;
  }
  th, td {
    border: 1px solid #bbb;
    padding: 3px 5px;
    text-align: left;
  }
  th { background: #e8e8e8; font-weight: bold; }
  p { margin: 3px 0; }
  ul, ol { margin: 2px 0 2px 16px; padding: 0; }
  li { margin: 1px 0; }
  strong { color: #000; }
  blockquote {
    border-left: 2px solid #999;
    padding: 2px 8px;
    margin: 4px 0;
    color: #444;
    font-size: 9.5px;
    break-inside: avoid;
  }
---

# Resumen Teorico — Evaluacion Continua 25/03/2026

## 1. Definiciones Fundamentales

### Matriz

Arreglo rectangular de numeros reales organizado en filas y columnas. Se denota `A ∈ M_mxn(R)` donde m = filas, n = columnas.

### Tipos de matrices

| Tipo | Condicion |
|------|-----------|
| Cuadrada | m = n (mismas filas que columnas) |
| Fila | m = 1 (una sola fila) |
| Columna | n = 1 (una sola columna) |
| Nula (O) | Todas las entradas son 0 |
| Diagonal | Cuadrada; solo la diagonal puede tener valores ≠ 0 |
| Triangular superior | Cuadrada; todo debajo de la diagonal = 0 |
| Triangular inferior | Cuadrada; todo arriba de la diagonal = 0 |
| Identidad (I) | Diagonal con todos 1 en la diagonal |
| Simetrica | Cuadrada; `A^T = A` (a_ij = a_ji) |
| Antisimetrica | Cuadrada; `A^T = -A` (a_ij = -a_ji, diagonal = 0) |
| Idempotente | Cuadrada; `A^2 = A` |
| Invertible | Cuadrada; existe A^(-1) tal que AA^(-1) = I |
| Nilpotente | Cuadrada; existe k tal que A^k = O |

### Diagonal principal

Los elementos a_11, a_22, a_33, ..., a_nn. Son los que tienen el mismo numero de fila que de columna.

---

## 2. Operaciones y Sus Reglas

### Suma / Resta

- **Requisito:** misma dimension
- Se opera entrada a entrada
- A + O = A (la nula es el neutro)
- A + (-A) = O

### Producto escalar por matriz

- Se multiplica cada entrada por el numero
- k(A + B) = kA + kB
- (k + h)A = kA + hA

### Producto de matrices

- **Requisito:** columnas de la 1ra = filas de la 2da
- Si A es mxn y B es nxp, resultado es mxp
- Entrada [F, C] = fila F de A por columna C de B (par a par y sumar)
- **NO conmutativo:** AB ≠ BA en general
- **Asociativo:** (AB)C = A(BC)
- **Distributivo:** A(B+C) = AB + AC y (A+B)C = AC + BC
- AI = IA = A (la identidad es el neutro)
- AO = OA = O

---

## 3. Traspuesta — Definicion y Propiedades

**Definicion:** A^T se obtiene intercambiando filas por columnas. Si A es mxn, A^T es nxm.

| Propiedad | Formula |
|-----------|---------|
| Doble traspuesta | (A^T)^T = A |
| Suma | (A + B)^T = A^T + B^T |
| Escalar | (kA)^T = kA^T |
| Producto | **(AB)^T = B^T A^T** (orden invertido) |

**Sobre simetricas:**
- A simetrica ⟺ A^T = A ⟺ a_ij = a_ji
- Si A, B simetricas: A+B es simetrica, kA es simetrica
- AB es simetrica **solo si AB = BA** (conmutan)

**Sobre antisimetricas:**
- A antisimetrica ⟺ A^T = -A ⟺ diagonal = 0 y a_ij = -a_ji

**Descomposicion:** Toda matriz A = ½(A + A^T) + ½(A - A^T) = parte simetrica + parte antisimetrica.

---

## 4. Traza — Definicion y Propiedades

**Definicion:** tr(A) = suma de la diagonal principal = a_11 + a_22 + ... + a_nn. Solo para matrices cuadradas.

| Propiedad | Formula |
|-----------|---------|
| Suma | tr(A + B) = tr(A) + tr(B) |
| Escalar | tr(kA) = k tr(A) |
| Traspuesta | tr(A^T) = tr(A) |
| Producto | **tr(AB) = tr(BA)** |

**Valores importantes:**
- tr(I_n) = n (la identidad nxn tiene n unos)
- tr(O) = 0

---

## 5. Inversa — Definicion y Propiedades

**Definicion:** A^(-1) es la unica matriz tal que A A^(-1) = A^(-1) A = I. Solo para matrices cuadradas. No todas la tienen.

| Propiedad | Formula |
|-----------|---------|
| Doble inversa | (A^(-1))^(-1) = A |
| Producto | **(AB)^(-1) = B^(-1) A^(-1)** (orden invertido) |
| Traspuesta | (A^T)^(-1) = (A^(-1))^T |

**Metodo directo (2x2):** Plantear A * [[a,b],[c,d]] = I. Resolver el sistema de 4 ecuaciones. Si hay solucion: es la inversa. Si hay contradiccion (0 = k con k≠0): no es invertible.

**Reglas con la inversa:**
- AB = A y A invertible → B = I
- AB = AC y A invertible → B = C
- Si A NO es invertible, **no se puede simplificar** (pueden existir B ≠ C con AB = AC)

---

## 6. Identidad — El Neutro del Producto

La identidad I tiene 1 en la diagonal, 0 en el resto.

```
I_2 = | 1  0 |     I_3 = | 1  0  0 |
      | 0  1 |           | 0  1  0 |
                          | 0  0  1 |
```

- AI = IA = A para toda A compatible
- I^T = I
- I^(-1) = I
- I^n = I
- tr(I_n) = n

---

## 7. Errores Frecuentes

| Error | Correccion |
|-------|-----------|
| AB = BA | **FALSO en general.** El producto no conmuta |
| (AB)^T = A^T B^T | **FALSO.** Es B^T A^T (orden invertido) |
| (AB)^(-1) = A^(-1) B^(-1) | **FALSO.** Es B^(-1) A^(-1) (orden invertido) |
| "Divido por A" | **NO EXISTE.** Se multiplica por A^(-1) |
| A + 1 = A + I | **NO.** No se puede sumar un numero a una matriz. Se suma la identidad |
| A invertible + B invertible → A+B invertible | **FALSO.** Contraejemplo: I + (-I) = O |
| (A+B)^2 = A^2 + 2AB + B^2 | **FALSO.** Es A^2 + AB + BA + B^2. Solo vale si AB = BA |
| A, B simetricas → AB simetrica | **FALSO.** Solo si AB = BA |
| AB = AC → B = C | **Solo si A es invertible** |
| Al despejar, multiplicar por la inversa de lados distintos | **Siempre del mismo lado** (izq o der, no mezclar) |

---

## 8. Resultados Importantes Para Demostraciones

### Idempotente + invertible = identidad

Si A^2 = A y A es invertible, entonces A = I.
Prueba: multiplicar ambos lados por A^(-1).

### AB - BA ≠ I (demostracion por el absurdo)

Suponer AB - BA = I. Tomar traza: tr(AB - BA) = tr(AB) - tr(BA) = 0. Pero tr(I) = n ≥ 1. Contradiccion.

### Inversa a partir de ecuacion

Si te dan una ecuacion como A^2 = 2A - I o A^3 = O, podes despejar la inversa:
- De A^2 = 2A - I → A(2I - A) = I → A^(-1) = 2I - A
- De A^3 = O → (A+I)(A^2 - A + I) = I → (A+I)^(-1) = A^2 - A + I

### Descomposicion simetrica/antisimetrica

Toda matriz se puede escribir como ½(A + A^T) + ½(A - A^T).

---

## 9. Posibles Preguntas de la Evaluacion

**Operaciones (las mas probables por ser nivel bajo):**

1. Dadas A, B, C: calcular 2A - 3B + C
2. Determinar cuales productos son posibles entre A, B, C de distintas dimensiones y calcular los que se puedan
3. Hallar una matriz D tal que una suma de cero

**Traspuesta y simetria:**

4. Dada A: calcular A^T. Determinar si es simetrica o antisimetrica
5. Demostrar que si A es simetrica, kA es simetrica
6. Demostrar que ½(A + A^T) es simetrica

**Traza:**

7. Calcular tr(A), tr(B), verificar que tr(A+B) = tr(A) + tr(B)
8. Demostrar que no existen A, B tales que AB - BA = I

**Inversa (muy probable, tema nuevo):**

9. Hallar la inversa de una matriz 2x2 por metodo directo (o concluir que no existe)
10. Dada una ecuacion matricial (ej: A^2 = 2A - I), deducir A^(-1)
11. Dada A^3 = O, demostrar que (A+I)^(-1) = A^2 - A + I y usarla para invertir una matriz concreta

**Ecuaciones matriciales:**

12. Despejar X de una ecuacion como AX + X = 2A

**Idempotentes:**

13. Probar que si A es idempotente e invertible, entonces A = I
14. Dar ejemplo de matriz idempotente que no sea I ni O

**Verdadero/Falso:**

15. A, B invertibles: AB invertible? (V) y A+B invertible? (F, dar contraejemplo)
16. (A+B)^2 = A^2 + 2AB + B^2? (F, dar contraejemplo)

---

## 10. Respuestas Cortas a las Preguntas

**1-3:** Operar entrada a entrada. Para D: cambiar signo a cada entrada de la suma.

**4:** Intercambiar filas por columnas. Simetrica si A^T = A. Antisimetrica si A^T = -A y diagonal = 0.

**5-6:** Trasponer la expresion usando propiedades y verificar que queda igual (simetrica) o con signo cambiado (antisimetrica).

**7:** Sumar diagonal. La propiedad se verifica si ambos lados dan el mismo numero.

**8:** Absurdo: tr del lado izq = 0, tr del lado der = n. Contradiccion.

**9:** Plantear A * B_generica = I, sistema de 4 ecuaciones, resolver. Si hay contradiccion: no invertible.

**10:** Reordenar la ecuacion hasta que quede algo * A = I. Ese "algo" es A^(-1).

**11:** Multiplicar (A+I)(A^2-A+I), expandir, usar A^3=O, verificar que da I. Para la concreta: sacar A = B - I, verificar A^3=O, calcular A^2-A+I.

**12:** Reescribir X como IX, factorizar, multiplicar por la inversa del mismo lado.

**13:** A^2=A → A^(-1)A^2 = A^(-1)A → A = I.

**14:** Ejemplo: [[1,0],[0,0]].

**15:** AB invertible: SI, (AB)^(-1) = B^(-1)A^(-1). A+B invertible: NO, contraejemplo I+(-I)=O.

**16:** FALSO. (A+B)^2 = A^2+AB+BA+B^2 ≠ A^2+2AB+B^2 porque AB ≠ BA en general.
