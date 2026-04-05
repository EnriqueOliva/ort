# CONCEPTOS DE CNN - EXPLICACIÓN CONECTADA Y SIMPLE

Este archivo explica cómo funcionan las CNNs conectando TODOS los conceptos paso a paso.

**Fuente del ejercicio:** `/home/enrique/2doSemestre/ModelosDeDeepLearning/Screenshot 2025-10-19 195806.png`

---

## PUNTO DE PARTIDA: ¿QUÉ ES UNA IMAGEN?

### Una imagen es una matriz de números

**Imagen en escala de grises (1 canal):**
```
┌──────────┐
│ 0  50  100│  ← Fila 1: 3 píxeles
│ 30 80  150│  ← Fila 2: 3 píxeles
│ 10 90  180│  ← Fila 3: 3 píxeles
└──────────┘

Dimensiones: (3, 3, 1)
              ↑  ↑  ↑
              3  3  1 canal
            alto ancho
```

**Imagen RGB (3 canales):**
```
Canal R:        Canal G:        Canal B:
┌────────┐      ┌────────┐      ┌────────┐
│255 200│      │  0  50│      │  0   0│
│240 180│      │ 10  30│      │  5  10│
└────────┘      └────────┘      └────────┘

3 matrices apiladas = 1 imagen a color

Dimensiones: (2, 2, 3)
              2 × 2 píxeles, 3 canales
```

**CIFAR-10:** (32, 32, 3) = 32 de alto, 32 de ancho, 3 canales RGB

---

## CÓMO FUNCIONA UNA CNN: LA HISTORIA COMPLETA

### PROBLEMA: Reconocer si una imagen es un camión

Tenemos una imagen (32, 32, 3) = 3,072 números.

**Pregunta:** ¿Cómo sabe la red que es un camión?

**Respuesta:** Buscando PATRONES en la imagen.

---

## PASO 1: VENTANAS - Mirar Regiones Pequeñas

### ¿Qué es una ventana?

**VENTANA = Una región pequeña de la imagen**

En lugar de mirar toda la imagen de una vez, miramos pedacitos pequeños.

```
Imagen completa (32×32):
┌───────────────────────────┐
│ · · · · · · · · · · · · ·│
│ · ┌───┐ · · · · · · · · ·│  ← VENTANA 3×3
│ · │ · │ · · · · · · · · ·│     Miramos solo estos 9 píxeles
│ · └───┘ · · · · · · · · ·│
│ · · · · · · · · · · · · ·│
└───────────────────────────┘
```

**Una ventana típica es 3×3:**
```
┌────────┐
│ 0  0  1│  ← 3 píxeles
│ 0  0  8│  ← 3 píxeles
│ 0  1  2│  ← 3 píxeles
└────────┘
```

**Si es RGB, la ventana tiene 3 capas (una por canal):**
```
3×3×3 = 27 números en total
```

---

## PASO 2: FILTROS - Herramientas para Detectar Patrones

### ¿Qué es un filtro?

**FILTRO = Una matriz pequeña (3×3) con números especiales que detecta UN patrón específico**

**Ejemplo: Filtro que detecta líneas verticales**
```
┌────────┐
│-1  0  1│
│-1  0  1│
│-1  0  1│
└────────┘

¿Qué hacen estos números?
  -1 a la izquierda = busca oscuro
   0 en el medio = neutral
   1 a la derecha = busca claro

Si hay oscuro a la izquierda y claro a la derecha = ¡LÍNEA VERTICAL!
```

**Para imagen RGB (3 canales), el filtro también tiene 3 capas:**
```
Filtro R (3×3)    Filtro G (3×3)    Filtro B (3×3)
┌────────┐        ┌────────┐        ┌────────┐
│ 1  2  1│        │ 1  0  1│        │ 1  1  0│
│ 2  1  4│        │ 0  1  0│        │ 1  0  2│
│ 2  2  2│        │ 1  0  1│        │ 0  1  1│
└────────┘        └────────┘        └────────┘

Total: 3×3×3 = 27 números + 1 bias = 28 parámetros
```

**DIFERENCIA CLAVE:**
- **Ventana:** Pedazo de la imagen que estás mirando (los datos)
- **Filtro:** Herramienta con números especiales para analizar esa ventana (los pesos aprendidos)

---

## PASO 3: CONVOLUCIÓN - Usar el Filtro en la Ventana

### ¿Qué es una convolución?

**CONVOLUCIÓN = Comparar la ventana (imagen) con el filtro (herramienta)**

**¿Cómo?** Multiplicando elemento por elemento y sumando TODO.

### Ejemplo completo paso a paso

**VENTANA de la imagen (3×3 de cada canal):**
```
Canal R:         Canal G:         Canal B:
┌────────┐       ┌────────┐       ┌────────┐
│ 0  0  1│       │ 0  0  0│       │ 0  0  5│
│ 0  0  8│       │ 0  0  2│       │ 0  0  1│
│ 0  1  2│       │ 0  3  1│       │ 0  0  0│
└────────┘       └────────┘       └────────┘
```

**FILTRO (3×3 de cada canal):**
```
Filtro R:        Filtro G:        Filtro B:
┌────────┐       ┌────────┐       ┌────────┐
│ 1  2  1│       │ 1  0  1│       │ 1  1  0│
│ 2  1  4│       │ 0  1  0│       │ 1  0  2│
│ 2  2  2│       │ 1  0  1│       │ 0  1  1│
└────────┘       └────────┘       └────────┘
```

**MULTIPLICACIÓN elemento por elemento en CADA canal:**

```
CANAL ROJO:
0×1=0   0×2=0   1×1=1
0×2=0   0×1=0   8×4=32  ← ¡Más grande!
0×2=0   1×2=2   2×2=4

Suma R = 0+0+1+0+0+32+0+2+4 = 39
```

```
CANAL VERDE:
0×1=0   0×0=0   0×1=0
0×0=0   0×1=0   2×0=0
0×1=0   3×0=0   1×1=1

Suma G = 1
```

```
CANAL AZUL:
0×1=0   0×1=0   5×0=0
0×1=0   0×0=0   1×2=2
0×0=0   0×1=0   0×1=0

Suma B = 2
```

**RESULTADO FINAL:**
```
Total = 39 + 1 + 2 + 5 (bias) = 47

UN SOLO NÚMERO: 47
```

**¿Qué significa 47?**

47 indica "qué tan bien esta región coincide con el patrón que busca el filtro".

- Si fuera 200 = ¡Patrón MUY presente!
- Si fuera 5 = Patrón casi no está

**Fuente:** Clase 6, convolución paso a paso

---

## PASO 4: FEATURE MAP - El Resultado de Aplicar 1 Filtro

### ¿Qué pasa ahora?

**No nos quedamos en una sola ventana. Movemos el filtro por TODA la imagen.**

```
Posición 1:      Posición 2:      Posición 3:      ...
┌───┐            ┌───┐            ┌───┐
│▓▓▓│··          ·│▓▓▓│·          ··│▓▓▓│
│▓▓▓│··          ·│▓▓▓│·          ··│▓▓▓│
│▓▓▓│··          ·│▓▓▓│·          ··│▓▓▓│
└───┘            └───┘            └───┘
  ↓                ↓                ↓
47               23               12

Mueves el filtro 1 píxel a la derecha cada vez
```

**Al final, tienes un MAPA completo de números:**

```
FEATURE MAP (32×32):
┌────────────────┐
│ 47  23  12  5  │
│  8  89  45  2  │
│  3   1  67  4  │
│ ...            │
└────────────────┘
```

### ¿Qué es un Feature Map?

**FEATURE MAP = Un mapa que muestra DÓNDE está el patrón en la imagen**

**Feature = Patrón** (línea vertical, borde, esquina, etc.)

**Ejemplo visual:**
```
IMAGEN original:          FEATURE MAP (después de aplicar filtro):

    🚛                    47  23  12  5   ...
  (camión)                 8  89  45  2   ...
                           3   1  67  4   ...

                          ↑
                       89 = ¡Línea vertical MUY fuerte aquí! (marco del camión)
                       47 = Línea vertical fuerte (rueda)
                        5 = No hay línea vertical (cielo)
```

**EN RESUMEN:**
- Aplicaste 1 filtro a toda la imagen
- Obtuviste 1 feature map
- El feature map te dice: "En esta posición SÍ hay ese patrón, en esta NO"

---

## PASO 5: CAPA CONVOLUCIONAL - Aplicar MUCHOS Filtros

### Un solo filtro no es suficiente

**Problema:** Un filtro solo detecta UN patrón (ej: líneas verticales).

Para reconocer un camión necesitas detectar:
- Líneas verticales
- Líneas horizontales
- Esquinas
- Círculos (ruedas)
- Texturas
- Etc.

**Solución:** ¡Aplicar MUCHOS filtros!

### ¿Qué es una Capa Convolucional?

**CAPA CONVOLUCIONAL = Aplicar múltiples filtros (32, 64, 128...) a la misma imagen**

```
IMAGEN (32×32×3)
   ↓
Aplicas Filtro 1  → Feature Map 1  (dónde hay líneas verticales)
Aplicas Filtro 2  → Feature Map 2  (dónde hay líneas horizontales)
Aplicas Filtro 3  → Feature Map 3  (dónde hay esquinas)
Aplicas Filtro 4  → Feature Map 4  (dónde hay círculos)
...
Aplicas Filtro 32 → Feature Map 32 (dónde hay texturas)

RESULTADO: 32 feature maps (32×32×32)
```

### Visualización

```
ANTES (entrada):             DESPUÉS (salida):
┌──────────┐                ┌──────────┐
│          │                │  Mapa 1  │ ← Líneas vert
│  IMAGEN  │   →  32  →     ├──────────┤
│  32×32×3 │    filtros     │  Mapa 2  │ ← Líneas horiz
│          │                ├──────────┤
└──────────┘                │  Mapa 3  │ ← Esquinas
                            ├──────────┤
                            │   ...    │
                            ├──────────┤
                            │ Mapa 32  │ ← Texturas
                            └──────────┘

                            32 mapas apilados = (32×32×32)
```

### Entradas y Salidas de la Capa

**Entrada de la capa:** (N, 32, 32, 3)
- N = batch size (cuántas imágenes procesas a la vez)
- 32×32 = tamaño espacial
- 3 = canales de entrada (R, G, B)

**Salida de la capa:** (N, 32, 32, 32)
- N = batch size (igual)
- 32×32 = tamaño espacial (igual, si usas padding='same')
- 32 = canales de salida = 32 feature maps

**Los 32 feature maps de salida = 32 CANALES DE FEATURES**

Es solo otro nombre para lo mismo.

### ¿Cuántos parámetros tiene esta capa?

```
32 filtros × (3×3×3 números por filtro) + 32 biases

= 32 × 27 + 32
= 864 + 32
= 896 parámetros que la red aprende

Fórmula:
Parámetros = (kernel_alto × kernel_ancho × canales_entrada × canales_salida) + canales_salida
```

**Fuente:** Clase 7, CIFAR-10

---

## CONCEPTO IMPORTANTE: PADDING

### ¿Para qué necesitamos el padding?

**PADDING resuelve 2 problemas:**

**PROBLEMA 1: Los bordes se ignoran**

Sin padding, los píxeles del borde NUNCA pueden ser el centro de una ventana 3×3:

```
Imagen 5×5 sin padding:
┌─────────────┐
│ 1  2  3  4  5│  ← Píxel 1: NO puede ser centro (falta izquierda)
│ 6  7  8  9 10│
│11 12 13 14 15│     Solo estos 9 píxeles centrales
│16 17 18 19 20│     pueden ser centro de ventana 3×3
│21 22 23 24 25│  ← Píxel 25: NO puede ser centro (falta abajo)
└─────────────┘

Resultado: Salida 3×3 (perdimos los bordes)
```

**¿Por qué es problema?**
- Los bordes tienen información importante
- En una foto, objetos pueden estar en el borde
- Perdemos datos valiosos

**PROBLEMA 2: La imagen se encoge rápido**

```
Sin padding:
32×32 → 30×30 → 28×28 → 26×26 → ...

Después de 5 capas: 22×22 (perdimos 10 píxeles por lado)
Después de 10 capas: 12×12
No puedes hacer redes profundas
```

### Cómo funciona el padding

**PADDING = Agregar ceros alrededor ANTES de aplicar el filtro**

```
PASO 1: Imagen original 5×5
┌─────────────┐
│ 1  2  3  4  5│
│ 6  7  8  9 10│
│11 12 13 14 15│
│16 17 18 19 20│
│21 22 23 24 25│
└─────────────┘

PASO 2: Agregar padding=1 (una fila/columna de ceros en cada lado)
┌───────────────────┐
│ 0  0  0  0  0  0  0│  ← Fila de ceros arriba
│ 0  1  2  3  4  5  0│  ← Imagen original rodeada de ceros
│ 0  6  7  8  9 10  0│
│ 0 11 12 13 14 15  0│
│ 0 16 17 18 19 20  0│
│ 0 21 22 23 24 25  0│
│ 0  0  0  0  0  0  0│  ← Fila de ceros abajo
└───────────────────┘
Ahora es 7×7

PASO 3: Aplicar filtro 3×3
AHORA el píxel 1 SÍ puede ser centro:

Ventana 3×3 centrada en píxel 1:
┌────────┐
│ 0  0  0│  ← Incluye ceros del padding
│ 0  1  2│  ← El píxel 1 es el centro
│ 0  6  7│
└────────┘

Resultado: Salida 5×5 (¡mantiene el tamaño!)
```

### Padding "same"

```
padding='same' calcula automáticamente el padding para mantener dimensiones

Para kernel 3×3: padding=1
Entrada: (32, 32, 3)
  ↓ Agrega padding=1
(34, 34, 3)
  ↓ Aplica filtro 3×3
Salida:  (32, 32, 32)  ← MISMO tamaño

Para kernel 5×5: padding=2
Para kernel 7×7: padding=3

Fórmula: padding = (kernel_size - 1) / 2
```

### Cómo se conjuga en la arquitectura completa

```
SIN padding (se encoge en cada capa):
(32,32,3) → Conv → (30,30,32) → Conv → (28,28,64) → ...
Problema: Pierde bordes, encoge rápido

CON padding='same':
(32,32,3) → Conv(padding=1) → (32,32,32)  ← Mantiene
           ↓
        MaxPool(2×2)        → (16,16,32)  ← Solo pooling reduce
           ↓
        Conv(padding=1)     → (16,16,64)  ← Mantiene
           ↓
        MaxPool(2×2)        → (8,8,64)    ← Solo pooling reduce

Control total: La reducción viene SOLO del pooling
```

### ¿Los ceros afectan el aprendizaje?

**NO, porque:**

```
Convolución en el borde:
Ventana:        Filtro:
┌────────┐     ┌────────┐
│ 0  0  0│     │ 1  2  1│
│ 0  5  3│  ×  │ 2  1  4│
│ 0  2  8│     │ 2  2  2│
└────────┘     └────────┘

Cálculo:
0×1 + 0×2 + 0×1 = 0  ← Los ceros NO contribuyen
0×2 + 5×1 + 3×4 = 17
0×2 + 2×2 + 8×2 = 20

Total: 0 + 17 + 20 = 37

Los ceros simplemente "no aportan" a la suma.
El filtro aprende a usar SOLO los píxeles reales.
```

**Fuente:** Clase 7, ejercicio con padding='same'

---

## PASO 6: MÚLTIPLES CAPAS CONVOLUCIONALES - Patrones Cada Vez Más Complejos

### Una capa no es suficiente

**La magia de las CNNs:** Apilar VARIAS capas convolucionales.

**¿Por qué?** Cada capa detecta patrones MÁS COMPLEJOS que la anterior.

### Flujo completo de 3 capas

```
════════════════════════════════════════════════════════════════

ENTRADA: IMAGEN del camión
(N, 32, 32, 3)
   ↑    ↑   ↑
   |    |   └── 3 canales: Valores de R, G, B en cada píxel
   |    └────── 32 píxeles de ancho
   └─────────── 32 píxeles de alto

════════════════════════════════════════════════════════════════

CAPA CONVOLUCIONAL 1:

¿Qué hace?
  - Recibe: (N, 32, 32, 3)  ← La imagen con colores R, G, B
  - Aplica: 32 filtros
  - Cada filtro busca un patrón BÁSICO en la imagen
  - Produce: 32 feature maps

¿Qué detecta?
  - Feature Map 1: Dónde hay líneas verticales
  - Feature Map 2: Dónde hay líneas horizontales
  - Feature Map 3: Dónde hay bordes diagonales
  - ...
  - Feature Map 32: Dónde hay cambios de intensidad

Salida: (N, 32, 32, 32)
   ↑    ↑   ↑
   |    |   └── 32 canales de features (32 mapas de patrones BÁSICOS)
   |    └────── 32 píxeles de ancho (igual)
   └─────────── 32 píxeles de alto (igual)

════════════════════════════════════════════════════════════════

MAX POOLING (2×2):

¿Qué hace?
  - Recibe: (N, 32, 32, 32)
  - Divide cada mapa en ventanas 2×2
  - Toma el MÁXIMO de cada ventana
  - Reduce el tamaño a la MITAD

Ejemplo en UN mapa:
ANTES (4×4):          DESPUÉS (2×2):
┌──────┬──────┐      ┌────┬────┐
│ 1  2 │ 5  6 │      │ 8  │ 6  │
│ 3  8 │ 2  4 │  →   ├────┼────┤
├──────┼──────┤      │ 9  │ 7  │
│ 9  1 │ 6  7 │      └────┴────┘
│ 5  3 │ 4  2 │
└──────┴──────┘
max(1,2,3,8)=8      max(5,6,2,4)=6
max(9,1,5,3)=9      max(6,7,4,2)=7

Salida: (N, 16, 16, 32)
   ↑    ↑   ↑
   |    |   └── 32 canales (IGUAL, pooling NO cambia canales)
   |    └────── 16 píxeles de ancho (32/2 = 16)
   └─────────── 16 píxeles de alto (32/2 = 16)

¿Para qué sirve Max Pooling?

1. REDUCIR DIMENSIONES: De 32×32 a 16×16 (75% menos números)
2. REDUCIR CÓMPUTO: Menos números = procesamiento más rápido
3. ROBUSTEZ: Si el patrón se mueve 1 píxel, max pooling da valor similar

¿Por qué perdemos información pero agregamos más filtros?

TRADEOFF INTELIGENTE:

Lo que PERDEMOS con pooling:
- 75% de posiciones espaciales (32×32 → 16×16)
- Posición EXACTA del patrón (¿está en píxel 47 o 48?)
- Detalles finos

Lo que CONSERVAMOS:
- QUE el patrón EXISTE en esa región
- La FUERZA del patrón (valor máximo)
- Suficiente información para siguiente capa

Lo que GANAMOS con más filtros:
- 100% más TIPOS de patrones (32 → 64 filtros)
- Más DIVERSIDAD de detección

RESULTADO NETO:
- Menos lugares donde buscar (1024 → 256 posiciones)
- Más cosas que buscar (32 → 64 tipos de patrones)
- Igual o MÁS información útil, menos ruido

Principio: No necesitas alta resolución espacial para patrones complejos.
Una "rueda" de 8×8 píxeles tiene información suficiente.
Lo que necesitas son MÁS FILTROS para detectar ruedas de diferentes tipos.

════════════════════════════════════════════════════════════════

CAPA CONVOLUCIONAL 2:

¿Qué hace?
  - Recibe: (N, 16, 16, 32)  ← Los 32 mapas de patrones básicos
  - Aplica: 64 filtros
  - PERO AHORA los filtros buscan patrones EN los feature maps anteriores
  - Los filtros ya no miran píxeles, miran PATRONES
  - Produce: 64 feature maps

¿Qué detecta?
  - Feature Map 1: Esquinas (combinando líneas verticales + horizontales)
  - Feature Map 2: Círculos (combinando varios bordes)
  - Feature Map 3: Rectángulos
  - ...
  - Feature Map 64: Texturas complejas

Salida: (N, 16, 16, 64)
         ↑    ↑   ↑
         |    |   └── 64 canales de features (patrones MEDIOS)
         |    └────── 16 píxeles de ancho (igual)
         └─────────── 16 píxeles de alto (igual)

════════════════════════════════════════════════════════════════

MAX POOLING (2×2):

Salida: (N, 8, 8, 64)
         ↑   ↑  ↑
         |   |  └── 64 canales (igual)
         |   └───── 8 píxeles ancho (16/2 = 8)
         └────────── 8 píxeles alto (16/2 = 8)

════════════════════════════════════════════════════════════════

CAPA CONVOLUCIONAL 3:

¿Qué hace?
  - Recibe: (N, 8, 8, 64)  ← Los 64 mapas de patrones medios
  - Aplica: 128 filtros
  - Los filtros buscan patrones AÚN MÁS COMPLEJOS
  - Produce: 128 feature maps

¿Qué detecta?
  - Feature Map 1: Ruedas completas (combinando círculos + texturas)
  - Feature Map 2: Ventanas de vehículos
  - Feature Map 3: Parachoques
  - ...
  - Feature Map 128: Formas completas de vehículos

Salida: (N, 8, 8, 128)
         ↑  ↑  ↑
         |  |  └── 128 canales de features (patrones COMPLEJOS)
         |  └───── 8 píxeles de ancho (igual)
         └──────── 8 píxeles de alto (igual)

════════════════════════════════════════════════════════════════

MAX POOLING (2×2):

Salida: (N, 4, 4, 128)
         ↑  ↑  ↑
         |  |  └── 128 canales
         |  └───── 4 píxeles ancho (8/2 = 4)
         └──────── 4 píxeles alto (8/2 = 4)

════════════════════════════════════════════════════════════════
```

### PATRÓN CLAVE

**Observa cómo cambian las dimensiones:**

```
Imagen:    (32, 32,   3)   ← Colores
  ↓
Capa 1:    (16, 16,  32)   ← Patrones básicos
  ↓
Capa 2:    ( 8,  8,  64)   ← Patrones medios
  ↓
Capa 3:    ( 4,  4, 128)   ← Patrones complejos

ESPACIAL (H, W):  32 → 16 → 8 → 4  (se REDUCE)
CANALES (C):       3 → 32 → 64 → 128  (AUMENTA)
```

### ¿POR QUÉ SE DUPLICAN LOS FILTROS? (3 → 32 → 64 → 128)

**Esta es una pregunta MUY importante que no tiene una respuesta matemática fija.**

Es una **decisión de diseño** que sigue una lógica clara:

#### 1. COMPENSACIÓN entre Espacio y Canales

**Analogía:** Imagina que tienes un presupuesto fijo de "capacidad de información"

```
Información total ≈ Alto × Ancho × Canales

Entrada:  32 × 32 × 3    = 3,072   valores
Capa 1:   16 × 16 × 32   = 8,192   valores  ↑ (más que antes)
Capa 2:    8 ×  8 × 64   = 4,096   valores  ↓
Capa 3:    4 ×  4 × 128  = 2,048   valores  ↓
```

**¿Qué está pasando?**

- **Dimensión espacial BAJA:** 32×32 → 16×16 → 8×8 → 4×4
- **Canales SUBEN:** 3 → 32 → 64 → 128

**¿Por qué?**
- Al reducir el tamaño espacial (con pooling), perdemos RESOLUCIÓN
- NECESITAMOS más canales (más filtros) para compensar esa pérdida
- Más canales = más formas diferentes de interpretar lo que queda

#### 2. PATRONES MÁS COMPLEJOS necesitan MÁS FILTROS

**Capa 1 (32 filtros):**
```
3 colores de entrada → 32 patrones básicos
- Detecta: 32 tipos de líneas/bordes básicos
- No necesita muchos filtros (los patrones son simples)
```

**Capa 2 (64 filtros):**
```
32 patrones básicos → 64 patrones medios
- Combina los 32 patrones básicos de MUCHAS formas
- Necesita MÁS filtros porque hay MÁS combinaciones posibles
- Detecta: esquinas, círculos, texturas
```

**Capa 3 (128 filtros):**
```
64 patrones medios → 128 patrones complejos
- Combina los 64 patrones de MUCHÍSIMAS formas
- Necesita AÚN MÁS filtros
- Detecta: ruedas, ventanas, objetos completos
```

**Analogía con el lenguaje:**
- **Letras** (3 colores RGB): Solo hay ~26 letras → No necesitas muchas
- **Palabras** (32 patrones): Hay miles de palabras → Necesitas más
- **Frases** (64 patrones): Hay millones de frases → Necesitas muchísimas más
- **Párrafos** (128 patrones): Combinaciones infinitas

#### 3. ¿POR QUÉ se DUPLICA específicamente? (×2)

**Duplicar es un patrón común, pero NO es obligatorio:**

```
Común:     3 → 32 → 64 → 128    (duplica)
También:   3 → 16 → 32 → 64     (duplica, menos filtros)
También:   3 → 32 → 48 → 64     (NO duplica, crece más lento)
También:   3 → 64 → 128 → 256   (duplica, más filtros)
```

**¿Por qué duplicar es común?**

1. **Potencias de 2 = Eficiencia computacional**
   - Las GPUs funcionan MEJOR con potencias de 2 (16, 32, 64, 128, 256)
   - Los cálculos son más rápidos

2. **Regla de bolsillo simple**
   - Es fácil de recordar y diseñar
   - Funciona bien en la práctica

3. **Balance entre capacidad y eficiencia**
   - Duplicar = crece rápido pero no demasiado
   - Triplicar = crece muy rápido, muchos parámetros
   - Crecer más lento (×1.5) = puede ser insuficiente

#### 4. ¿CÓMO decidir cuántos filtros usar?

**NO hay fórmula mágica.** Es parte del **diseño de la arquitectura:**

**Factores que influyen:**

1. **Complejidad del problema**
   - Problema simple (dígitos 0-9): Menos filtros (16, 32, 64)
   - Problema complejo (1000 categorías): Más filtros (64, 128, 256, 512)

2. **Tamaño del dataset**
   - Dataset pequeño: Menos filtros (evitar overfitting)
   - Dataset grande: Más filtros (puede aprender más patrones)

3. **Recursos computacionales**
   - GPU pequeña: Menos filtros
   - GPU grande: Puedes usar más filtros

**Ejemplos de arquitecturas reales:**

```
VGG-16 (clasificación ImageNet):
  3 → 64 → 128 → 256 → 512 → 512

ResNet-50 (clasificación ImageNet):
  3 → 64 → 256 → 512 → 1024 → 2048

Arquitectura simple (MNIST):
  1 → 16 → 32 → 64
```

#### 5. RESUMEN: La Lógica del Diseño

**En nuestro ejemplo (CIFAR-10):**

```
Entrada RGB:     (32, 32, 3)
                    ↓
                 32 filtros ← Suficiente para patrones básicos
Capa 1:          (16, 16, 32)
                    ↓
                 64 filtros ← Duplicamos porque:
                             - Espacial se redujo a la mitad
                             - Patrones más complejos
Capa 2:          (8, 8, 64)
                    ↓
                128 filtros ← Duplicamos de nuevo por las
                             mismas razones
Capa 3:          (4, 4, 128)
```

**Principio general:**

> **A medida que la imagen se hace más PEQUEÑA espacialmente,**
> **necesitamos más CANALES para capturar la complejidad creciente**
> **de los patrones que estamos detectando.**

**Fuente:** Principio de diseño común en arquitecturas CNN. El número específico de filtros se determina experimentalmente y se ajusta según el problema.
`/home/enrique/2doSemestre/ModelosDeDeepLearning/7-13-10-2025/7-13-10-2025.txt` (se menciona que el número de filtros es parte del diseño de la arquitectura)

**Mientras más profundo:**
- Tamaño espacial MÁS PEQUEÑO (menos píxeles)
- MÁS canales (más tipos de patrones detectados)
- Patrones MÁS COMPLEJOS

**Fuente:** Clase 7, arquitectura completa CIFAR-10

---

## PASO 7: CAPAS DENSAS - Clasificación Final

### Ahora tienes 128 mapas de patrones complejos

**Problema:** Tienes (N, 4, 4, 128) = un cubo 3D con patrones detectados.

**Necesitas:** Un número que diga "es un truck" o "es un car".

### ¿Qué haces?

**PASO 1: APLANAR (Flatten)**

Convierte el cubo 3D en una lista de números:

```
(N, 4, 4, 128)  →  4 × 4 × 128 = 2,048 números  →  (N, 2048)

[0.5, 0.8, 0.3, 0.1, ..., 0.7]
 ↑                           ↑
 Número 1                    Número 2048
```

**PASO 2: CAPAS DENSAS**

Ahora usas capas como en los MLPs:

```
(N, 2048)           ← ENTRADA: 2048 números (del flatten)
   ↓
Dense(2048 → 512):  ← 512 neuronas
                      Cada neurona recibe LOS 2048 números
                      y produce 1 número de salida

                      Neurona 1: w₁·x₁ + w₂·x₂ + ... + w₂₀₄₈·x₂₀₄₈ + b₁ = salida₁
                      Neurona 2: (otra combinación de los 2048) = salida₂
                      ...
                      Neurona 512: (otra combinación de los 2048) = salida₅₁₂
   ↓
(N, 512)            ← SALIDA: 512 números (uno por neurona)
                      Cada número representa una "característica aprendida"
   ↓
Dense(512 → 5):     ← 5 neuronas (una por clase)
                      Cada neurona recibe LOS 512 números

                      Neurona 1 (car):    w₁·512números + b = score_car
                      Neurona 2 (bus):    w₂·512números + b = score_bus
                      Neurona 3 (truck):  w₃·512números + b = score_truck
                      Neurona 4 (motor):  w₄·512números + b = score_motor
                      Neurona 5 (person): w₅·512números + b = score_person
   ↓
(N, 5)              ← 5 números (scores, uno por clase)
   ↓
Softmax             ← Convierte en probabilidades que suman 1.0
   ↓
[0.15, 0.07, 0.68, 0.09, 0.01]
 car   bus   truck motor person
              ↑
            68% → ¡Es un TRUCK!
```

**¿Por qué 512?**
- El 2048 es FIJO (viene de 4×4×128)
- El 512 es una ELECCIÓN de diseño (podría ser 256, 512, 1024, etc.)
- 512 es un "paso intermedio" para reducir de 2048 a 5
- Patrón común: entrada grande → intermedio → salida pequeña

### ¿Qué es una Capa Densa?

**CAPA DENSA = Cada neurona de salida conectada a TODAS las entradas**

Es EXACTAMENTE igual que en los MLPs.

```
3 entradas  →  2 salidas

x1 ────┬──→ y1 = x1·w1 + x2·w2 + x3·w3 + b1
x2 ────┼──→ y2 = x1·w4 + x2·w5 + x3·w6 + b2
x3 ────┘

Cada y mira TODOS los x
```

**Parámetros Dense(2048 → 512):**
```
(2048 × 512) + 512 = 1,048,576 + 512 = 1,049,088 parámetros
```

**Fuente:** Clase 7

---

## RESUMEN: TODO CONECTADO

```
════════════════════════════════════════════════════════════════
                        FLUJO COMPLETO
════════════════════════════════════════════════════════════════

IMAGEN del camión (32×32×3) = 3,072 números (píxeles RGB)
   ↓

┌──────────────────────────────────────────────────────────────┐
│ BLOQUES CONVOLUCIONALES                                      │
│ (Detectan patrones cada vez más complejos)                  │
└──────────────────────────────────────────────────────────────┘

BLOQUE 1:
  Conv(3→32):    Aplica 32 filtros, genera 32 feature maps
                 Detecta: líneas, bordes básicos
  MaxPool(2×2):  Reduce tamaño a la mitad

  Salida: (16×16×32)

BLOQUE 2:
  Conv(32→64):   Aplica 64 filtros EN los 32 mapas anteriores
                 Detecta: esquinas, círculos, formas simples
  MaxPool(2×2):  Reduce tamaño

  Salida: (8×8×64)

BLOQUE 3:
  Conv(64→128):  Aplica 128 filtros EN los 64 mapas anteriores
                 Detecta: ruedas, ventanas, objetos completos
  MaxPool(2×2):  Reduce tamaño

  Salida: (4×4×128)

   ↓

┌──────────────────────────────────────────────────────────────┐
│ CLASIFICACIÓN                                                │
│ (Decide qué es basándose en los patrones encontrados)       │
└──────────────────────────────────────────────────────────────┘

Flatten:         (4×4×128) → (2048) números en fila
Dense(2048→512): Cada neurona mira los 2048 números
Dense(512→5):    5 neuronas (una por clase)
Softmax:         Convierte en probabilidades

   ↓

[0.15, 0.07, 0.68, 0.09, 0.01]
 car   bus   truck motor person
              ↑
            68%

RESULTADO: "Es un TRUCK con 68% de confianza"

════════════════════════════════════════════════════════════════
```

---

## CONCEPTO IMPORTANTE: REGULARIZACIÓN L1 Y L2

### ¿Qué problema resuelve la regularización?

**PROBLEMA: Overfitting (sobreajuste)**

```
Imagina una red con estos pesos:

Neurona 1:  w₁ = 150.0    ← PESO ENORME
            w₂ =   0.1
            w₃ =   0.2

La neurona 1 depende MUCHÍSIMO del input 1.
Si ese input cambia un poquito, la predicción colapsa.
```

**SOLUCIÓN: Penalizar pesos grandes**

Modificamos la función de pérdida para que la red NO SOLO minimice errores, sino también el tamaño de los pesos.

---

## REGULARIZACIÓN L1 (Lasso)

### Fórmula

```
Loss_TOTAL = Loss_ORIGINAL + λ × Σ|pesos|
                             ↑     ↑
                             │     └─ Suma de VALORES ABSOLUTOS
                             │
                             └─ Parámetro de regularización
                                (controla cuánto penalizamos)
```

### Ejemplo Numérico

**Red sin regularización:**

```
Pesos de una capa:
w₁ = 10.0
w₂ = -8.0
w₃ = 15.0
w₄ = 0.5

Loss_original = 0.25  (error de predicción)
Loss_TOTAL = 0.25     (solo minimiza error)
```

**Red con regularización L1 (λ = 0.01):**

```
Pesos:
w₁ = 10.0  →  |10.0| = 10.0
w₂ = -8.0  →  |-8.0| = 8.0   ← Valor absoluto
w₃ = 15.0  →  |15.0| = 15.0
w₄ = 0.5   →  |0.5|  = 0.5

Suma de valores absolutos:
Σ|pesos| = 10.0 + 8.0 + 15.0 + 0.5 = 33.5

Penalización L1:
λ × Σ|pesos| = 0.01 × 33.5 = 0.335

Loss_TOTAL = Loss_original + Penalización L1
           = 0.25 + 0.335
           = 0.585
```

**¿Qué pasa durante el entrenamiento?**

La red ahora tiene DOS objetivos:
1. Minimizar error de predicción (Loss_original ↓)
2. Minimizar suma de valores absolutos de pesos (Σ|pesos| ↓)

**Resultado:** La red prefiere usar MUCHOS pesos pequeños en vez de POCOS pesos gigantes.

---

### Característica especial de L1: SPARSITY (Pesos exactamente cero)

**L1 tiende a poner pesos en CERO:**

```
ANTES (sin regularización):
w₁ = 10.0
w₂ = -8.0
w₃ = 15.0
w₄ = 0.5    ← Peso pequeño pero NO cero
w₅ = -0.8
w₆ = 1.2

DESPUÉS (con L1):
w₁ = 8.5
w₂ = -6.2
w₃ = 12.0
w₄ = 0.0    ← ¡EXACTAMENTE CERO!
w₅ = 0.0    ← ¡EXACTAMENTE CERO!
w₆ = 0.0    ← ¡EXACTAMENTE CERO!

Resultado: Solo 3 conexiones activas (las otras están "apagadas")
```

**¿Por qué L1 crea ceros?**

El valor absoluto |w| tiene una esquina en w=0. El gradiente "empuja" los pesos pequeños directamente a cero.

**Ventaja: Selección automática de features**

Si w₄ = 0, significa que el input 4 NO IMPORTA para la predicción.
→ L1 automáticamente descarta features irrelevantes.

---

## REGULARIZACIÓN L2 (Ridge)

### Fórmula

```
Loss_TOTAL = Loss_ORIGINAL + λ × Σ(pesos²)
                             ↑     ↑
                             │     └─ Suma de CUADRADOS
                             │
                             └─ Parámetro de regularización
```

### Ejemplo Numérico

**Red con regularización L2 (λ = 0.01):**

```
Pesos:
w₁ = 10.0  →  (10.0)² = 100.0
w₂ = -8.0  →  (-8.0)² = 64.0   ← Se eleva al cuadrado
w₃ = 15.0  →  (15.0)² = 225.0
w₄ = 0.5   →  (0.5)²  = 0.25

Suma de cuadrados:
Σ(pesos²) = 100.0 + 64.0 + 225.0 + 0.25 = 389.25

Penalización L2:
λ × Σ(pesos²) = 0.01 × 389.25 = 3.89

Loss_TOTAL = Loss_original + Penalización L2
           = 0.25 + 3.89
           = 4.14
```

**Comparación de penalizaciones (mismo ejemplo):**

```
           L1              L2
w₁ = 10.0  → 10.0         → 100.0   ← L2 penaliza MUCHO más
w₂ = -8.0  → 8.0          → 64.0
w₃ = 15.0  → 15.0         → 225.0   ← El peso más grande
w₄ = 0.5   → 0.5          → 0.25    ← Peso chico casi no afecta

Total:       33.5           389.25

Con λ=0.01:  0.335          3.89     ← L2 penaliza más
```

---

### Característica especial de L2: Pesos pequeños pero NO cero

**L2 NO pone pesos en cero:**

```
ANTES (sin regularización):
w₁ = 10.0
w₂ = -8.0
w₃ = 15.0
w₄ = 0.5
w₅ = -0.8
w₆ = 1.2

DESPUÉS (con L2):
w₁ = 7.2    ← Reducido
w₂ = -5.8   ← Reducido
w₃ = 10.5   ← Muy reducido (era el más grande)
w₄ = 0.4    ← Ligeramente reducido pero NO cero
w₅ = -0.6   ← Ligeramente reducido pero NO cero
w₆ = 0.9    ← Ligeramente reducido pero NO cero

Resultado: TODOS los pesos son más pequeños, pero NINGUNO es cero
```

**¿Por qué L2 NO crea ceros?**

El cuadrado w² es suave en w=0. El gradiente nunca empuja completamente a cero, solo hace pesos más y más pequeños.

**Ventaja: Pesos distribuidos uniformemente**

Todos los inputs contribuyen un poquito. La red no depende de pocas features.

---

## COMPARACIÓN L1 vs L2

### Ejemplo con 4 pesos diferentes

```
ESCENARIO: Mismos pesos iniciales

Pesos originales:
w₁ = 20.0  (grande)
w₂ = 5.0   (mediano)
w₃ = 0.8   (chico)
w₄ = 0.1   (muy chico)

Loss_original = 0.3  (mismo para ambos casos)
λ = 0.01             (mismo para ambos casos)
```

**Penalización L1:**

```
|20.0| + |5.0| + |0.8| + |0.1| = 25.9

Penalización: 0.01 × 25.9 = 0.259

Loss_TOTAL = 0.3 + 0.259 = 0.559
```

**Penalización L2:**

```
(20.0)² + (5.0)² + (0.8)² + (0.1)² = 400 + 25 + 0.64 + 0.01 = 425.65

Penalización: 0.01 × 425.65 = 4.26

Loss_TOTAL = 0.3 + 4.26 = 4.56
```

**Observación clave:**

```
L1 penaliza:  0.259
L2 penaliza:  4.26  ← ¡16 veces más!

¿Por qué? Porque L2 CASTIGA DESPROPORCIONADAMENTE los pesos grandes:
w₁ = 20.0:
  L1 contribuye:  20.0    (100×0.2)
  L2 contribuye:  400.0   (2000×0.2)  ← 20 veces más por este peso

w₄ = 0.1:
  L1 contribuye:  0.1
  L2 contribuye:  0.01    ← 10 veces menos por este peso
```

---

## TABLA RESUMEN: L1 vs L2

| Aspecto | L1 (Lasso) | L2 (Ridge) |
|---------|------------|------------|
| **Fórmula** | λ × Σ\|W\| | λ × Σ(W²) |
| **Penalización** | Valor absoluto | Cuadrado |
| **Efecto en pesos grandes** | Penaliza linealmente | Penaliza exponencialmente |
| **Efecto en pesos chicos** | Penaliza proporcional | Penaliza muy poco |
| **¿Crea ceros?** | SÍ (sparsity) | NO (solo achica) |
| **Selección features** | SÍ | NO |
| **Interpretabilidad** | Alta (menos conexiones) | Baja (todas conectadas) |
| **Cuándo usar** | Muchas features, pocas útiles | Todas features útiles |

---

## ¿Cómo se usa en Keras?

**Regularización L1:**

```python
Dense(16, kernel_regularizer='l1', activation='relu')
```

**Regularización L2:**

```python
Dense(16, kernel_regularizer='l2', activation='relu')
```

**Ambas (Elastic Net):**

```python
from keras.regularizers import l1_l2

Dense(16, kernel_regularizer=l1_l2(l1=0.01, l2=0.01), activation='relu')
```

---

## Ejemplo visual del efecto

```
RED SIN REGULARIZACIÓN:
═══════════════════════

Capa Dense(32):
Pesos: [150, -80, 0.2, 0.5, 200, -120, ...]  ← Algunos GIGANTES
                                               ← Red FRÁGIL

Loss = 0.15  (error bajo en entrenamiento)
Test Error = 2.50  (error ALTO en test)  ← OVERFITTING


RED CON L1 (λ=0.01):
═══════════════════

Capa Dense(32):
Pesos: [8.5, -6.2, 0.0, 0.0, 12.0, 0.0, ...]  ← Muchos CEROS
                                               ← Solo 10 conexiones activas

Loss = 0.28  (error un poco más alto en entrenamiento)
Test Error = 0.35  (error BAJO en test)  ← GENERALIZA BIEN


RED CON L2 (λ=0.01):
═══════════════════

Capa Dense(32):
Pesos: [7.2, -5.8, 0.15, 0.4, 10.5, -8.1, ...]  ← TODOS más chicos
                                                 ← 32 conexiones activas

Loss = 0.25  (error un poco más alto en entrenamiento)
Test Error = 0.32  (error BAJO en test)  ← GENERALIZA BIEN
```

---

## ¿Cuál elegir?

**Usa L1 si:**
- Tienes MUCHAS features (100, 1000, 10000)
- Sospechas que solo POCAS son realmente importantes
- Quieres interpretabilidad (saber cuáles features importan)
- Ejemplo: análisis de texto con 10,000 palabras

**Usa L2 si:**
- Todas las features son potencialmente útiles
- Quieres distribuir importancia entre todas
- Es el más común en práctica (default en muchos casos)
- Ejemplo: procesamiento de imágenes (todos los píxeles pueden importar)

**Usa ambos (Elastic Net) si:**
- No estás seguro
- Quieres combinar ventajas de ambos

**Fuente:** Clase 5-29-09-2025 (transcripción completa)

---
