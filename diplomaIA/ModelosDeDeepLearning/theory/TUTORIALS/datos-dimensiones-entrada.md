# Guía de Dimensiones en Redes Neuronales

## Lo Básico: ¿Qué es un DATO?

**UN DATO = UNA FILA de tu tabla de datos.**

Ejemplo:
```
Tabla de vuelos:
       hora│día│mes│aero│dur
Fila 1: 14 │ 1 │ 3 │ 5  │120  ← ESTO es UN DATO
Fila 2:  9 │ 5 │ 7 │ 2  │180  ← ESTO es otro DATO
Fila 3: 16 │ 3 │12 │ 8  │ 95  ← ESTO es otro DATO
```

Cada fila completa = 1 dato.

---

## Las Dos Notaciones del Curso

Dependiendo del tipo de datos, la notación cambia:

### 1. Datos Tabulares → (N, M)

### 2. Imágenes → (N, H, W, C)

---

## CASO 1: Datos Tabulares → (N, M)

### Qué significa cada letra

```
(N, M)
 ↑  ↑
 |  └── M = cuántos NÚMEROS tiene cada fila (cada dato)
 └───── N = cuántas FILAS estás procesando (batch size)
```

### Ejemplo Real 1: Vuelos (Clase 7)
*Fuente: `/7-13-10-2025/7-13-10-2025.txt`*

**Una tabla de vuelos tiene estas columnas:**
- hora, día, mes, aerolínea, duración = **5 columnas**

**Procesando 1 vuelo:**
```
[14, 1, 3, 5, 120]  ← 1 fila con 5 números

Dimensión: (1, 5)
            ↑  ↑
            |  └── M = 5 (5 números por vuelo)
            └───── N = 1 (1 vuelo)
```

**Procesando 32 vuelos:**
```
[14, 1,  3, 5, 120]  ← fila 1
[9,  5,  7, 2, 180]  ← fila 2
[16, 3, 12, 8,  95]  ← fila 3
...
(32 filas en total)

Dimensión: (32, 5)
            ↑   ↑
            |   └── M = 5 (cada fila tiene 5 números)
            └────── N = 32 (32 filas)
```

**La red:** 5 → 15 → 1
- Entrada: (N, 5)
- Con N=1: (1, 5)
- Con N=32: (32, 5)
- Con N=100: (100, 5)

**M siempre es 5** porque cada vuelo siempre tiene 5 números.
**N cambia** según cuántos vuelos procesas juntos.

---

### Ejemplo Real 2: Excel (Clase 2)
*Fuente: `/2-01-09-2025/2-01-09-2025.txt`*

**Una tabla con puntos tiene esta columna:**
- coordenada x = **1 columna**

**El dataset tiene 9 puntos (9 filas):**
```
Punto 1: [x₁]  ← 1 fila con 1 número
Punto 2: [x₂]  ← 1 fila con 1 número
...
Punto 9: [x₉]

Dimensión: (9, 1)
            ↑  ↑
            |  └── M = 1 (1 número por punto)
            └───── N = 9 (9 puntos)
```

**La red:** 1 → 2 → 1
- Entrada: (N, 1)
- Con N=1: (1, 1) ← procesas 1 punto
- Con N=9: (9, 1) ← procesas 9 puntos

---

### Ejemplo Real 3: Micrograd (Clase 3)
*Fuente: `/3-08-09-2025/3-08-09-2025.txt`*

**Cada dato tiene 3 números (3 features):**

**Procesando 1 dato:**
```
[x₁, x₂, x₃]  ← 1 fila con 3 números

Dimensión: (1, 3)
            ↑  ↑
            |  └── M = 3 (3 números por dato)
            └───── N = 1 (1 dato)
```

**Procesando 4 datos:**
```
[x₁, x₂, x₃]  ← fila 1
[x₁, x₂, x₃]  ← fila 2
[x₁, x₂, x₃]  ← fila 3
[x₁, x₂, x₃]  ← fila 4

Dimensión: (4, 3)
            ↑  ↑
            |  └── M = 3 (cada fila tiene 3 números)
            └───── N = 4 (4 filas)
```

**La red:** 3 → 4 → 4 → 1
- Entrada: (N, 3)
- Micrograd usa N=1 (procesa de a uno)

---

### Resumen Datos Tabulares

```
(N, M)
 ↑  ↑
 |  └── M = columnas de tu tabla (cuántos números por fila)
 └───── N = filas que procesas juntas (batch size)

M es FIJO (depende de tu problema)
N lo eliges tú (cuántos datos procesas a la vez)
```

**Ejemplos del curso:**
- Vuelos: (N, 5) porque cada vuelo tiene 5 columnas
- Excel: (N, 1) porque cada punto tiene 1 columna
- Micrograd: (N, 3) porque cada dato tiene 3 columnas

---

## CASO 2: Imágenes → (N, H, W, C)

### Qué significa cada letra

```
(N, H, W, C)
 ↑  ↑  ↑  ↑
 |  |  |  └── C = Channels (canales de color)
 |  |  |         1 = imagen en blanco y negro
 |  |  |         3 = imagen a color (RGB: Red, Green, Blue)
 |  |  └───── W = Width (ancho en píxeles)
 |  └──────── H = Height (alto en píxeles)
 └─────────── N = cuántas imágenes (batch size)
```

### Ejemplo Real 1: MNIST (Clase 6)
*Fuente: `/6-06-10-2025/6-06-10-2025.txt`*

**Imágenes de dígitos escritos a mano:**
- Alto: 28 píxeles
- Ancho: 28 píxeles
- Canales: 1 (blanco y negro)

**Procesando 1 imagen:**
```
Una imagen de 28×28 en blanco y negro

Dimensión: (1, 28, 28, 1)
            ↑  ↑   ↑   ↑
            |  |   |   └── C = 1 (blanco y negro)
            |  |   └────── W = 28 (28 píxeles de ancho)
            |  └────────── H = 28 (28 píxeles de alto)
            └─────────── N = 1 (1 imagen)
```

**Procesando 64 imágenes:**
```
64 imágenes de 28×28 en blanco y negro

Dimensión: (64, 28, 28, 1)
            ↑   ↑   ↑   ↑
            |   |   |   └── C = 1
            |   |   └────── W = 28
            |   └────────── H = 28
            └─────────── N = 64 (64 imágenes)
```

**La red CNN:**
- Entrada: (N, 28, 28, 1)
- H, W, C son FIJOS (todas las imágenes MNIST son 28×28×1)
- N cambia según cuántas imágenes procesas

---

### Ejemplo Real 2: CIFAR-10 (Clase 7)
*Fuente: `/7-13-10-2025/7-13-10-2025.txt`*

**Imágenes pequeñas a color:**
- Alto: 32 píxeles
- Ancho: 32 píxeles
- Canales: 3 (color RGB)

**Procesando 1 imagen:**
```
Una imagen de 32×32 a color

Dimensión: (1, 32, 32, 3)
            ↑  ↑   ↑   ↑
            |  |   |   └── C = 3 (RGB: rojo, verde, azul)
            |  |   └────── W = 32 (32 píxeles de ancho)
            |  └────────── H = 32 (32 píxeles de alto)
            └─────────── N = 1 (1 imagen)
```

**Procesando 64 imágenes:**
```
64 imágenes de 32×32 a color

Dimensión: (64, 32, 32, 3)
            ↑   ↑   ↑   ↑
            |   |   |   └── C = 3
            |   |   └────── W = 32
            |   └────────── H = 32
            └─────────── N = 64 (64 imágenes)
```

**La red CNN:**
```
Entrada:        (N, 32, 32, 3)
Conv(3→10):     (N, 32, 32, 10)  ← cambian canales
MaxPool(2×2):   (N, 16, 16, 10)  ← cambian alto y ancho
Conv(10→20):    (N, 16, 16, 20)  ← cambian canales
MaxPool(2×2):   (N, 8, 8, 20)    ← cambian alto y ancho
GlobalAvgPool:  (N, 20)          ← colapsa a forma tabular
Dense(20→10):   (N, 10)          ← salida final
```

**H, W, C iniciales son FIJOS** (todas las imágenes CIFAR son 32×32×3)
**N cambia** según cuántas imágenes procesas

---

### Resumen Imágenes

```
(N, H, W, C)
 ↑  ↑  ↑  ↑
 |  |  |  └── C = canales (1=b/n, 3=color)
 |  |  └───── W = ancho en píxeles
 |  └──────── H = alto en píxeles
 └─────────── N = cuántas imágenes (batch size)

H, W, C son FIJOS (dependen del tipo de imagen)
N lo eliges tú (cuántas imágenes procesas a la vez)
```

**Ejemplos del curso:**
- MNIST: (N, 28, 28, 1) porque son imágenes 28×28 en blanco y negro
- CIFAR-10: (N, 32, 32, 3) porque son imágenes 32×32 a color

---

## Comparación Lado a Lado

### Mismo Dataset, Diferente Notación

**MNIST como tabla (MLP, Clase 2):**
- Aplanamos la imagen: 28×28 = 784 números
- Dimensión: (N, 784)
- Es datos tabulares: cada imagen = 1 fila con 784 columnas

**MNIST como imagen (CNN, Clase 6):**
- Mantenemos la estructura de imagen
- Dimensión: (N, 28, 28, 1)
- Es imagen: cada imagen tiene alto, ancho, canales

**Ambas son la MISMA imagen, solo organizadas diferente.**

---

## Tabla de Todos los Ejemplos del Curso

| Red | Tipo | Forma Entrada | Significado | Fuente |
|-----|------|---------------|-------------|--------|
| Excel 1→2→1 | Tabular | (9, 1) | 9 puntos, 1 coordenada | Clase 2 |
| Micrograd 3→4→4→1 | Tabular | (4, 3) | 4 datos, 3 features | Clase 3 |
| Vuelos 5→15→1 | Tabular | (32, 5) | 32 vuelos, 5 features | Clase 7 |
| MLP MNIST | Tabular | (N, 784) | N imágenes aplanadas | Clase 2 |
| CNN MNIST | Imagen | (N, 28, 28, 1) | N imágenes 28×28 b/n | Clase 6 |
| CNN CIFAR-10 | Imagen | (N, 32, 32, 3) | N imágenes 32×32 RGB | Clase 7 |

---

## Reglas Simples

### ¿Cómo saber qué notación usar?

**Pregunta 1: ¿Son imágenes?**
- SÍ → usa (N, H, W, C)
- NO → usa (N, M)

**Pregunta 2: ¿Qué es N?**
- N = cuántos datos procesas a la vez (batch size)
- TÚ lo eliges
- La red funciona con cualquier N

**Pregunta 3: ¿Qué es M (en tabulares)?**
- M = cuántas columnas tiene tu tabla
- FIJO para tu problema
- Ejemplos: 5 para vuelos, 1 para Excel, 3 para micrograd

**Pregunta 4: ¿Qué son H, W, C (en imágenes)?**
- H = alto en píxeles (FIJO para tu dataset)
- W = ancho en píxeles (FIJO para tu dataset)
- C = canales: 1 para b/n, 3 para color (FIJO)

---

## La Única Regla Universal

**LA PRIMERA DIMENSIÓN SIEMPRE ES N (batch size).**

```
Datos tabulares:  (N, M)
Imágenes:         (N, H, W, C)

N = lo eliges tú (cuántos datos procesas juntos)
Todo lo demás = FIJO (depende de tu problema/dataset)
```

**La red NO cambia con N.**
- Pesos: iguales
- Arquitectura: igual
- Solo cambia cuántas filas/imágenes procesas a la vez
