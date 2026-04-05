# Álgebra Lineal y Matemáticas de Tensores - Explicación desde Cero

## Introducción: ¿Por qué necesitamos esto en Deep Learning?

El profesor comenzó explicando que haría *"un repaso de tensores y álgebra lineal sin asustar a nadie"*. Su objetivo no es que memorices fórmulas, sino que cuando veas una ecuación, *"la logren entender y más o menos sepan de qué está hablando y lo hagan corresponder al código"*.

En Deep Learning, toda la información (imágenes, texto, sonido) se representa como números organizados en estructuras llamadas **tensores**. Son el lenguaje fundamental que las computadoras usan para procesar información.

## ¿Qué es un Tensor?

### Definición simple
Un **tensor** es simplemente una forma de organizar números en una estructura con múltiples dimensiones. Piensa en él como un contenedor de números con una forma específica.

### El origen del nombre
El profesor explicó que la palabra viene de las matemáticas: *"un tensor es un operador multilineal... va a corresponder con una especie de matriz de más dimensiones"*. Pero no te preocupes por la definición matemática compleja - en la práctica, es solo una forma de organizar datos.

## Las Dimensiones de los Tensores (0D a nD)

El profesor explicó que los tensores pueden tener diferentes números de dimensiones, y cada dimensión tiene un significado específico.

### Tensor 0D - Escalar
- **¿Qué es?** Un solo número
- **Ejemplo**: La temperatura actual (25°C)
- **Shape**: No tiene dimensiones, es solo un número
- **En código**: `tensor(25)`

### Tensor 1D - Vector
- **¿Qué es?** Una lista de números en fila
- **Ejemplo**: Las notas de un estudiante [8, 7, 9, 6, 10]
- **Shape**: (5,) - significa 5 elementos
- **En código**: `tensor([8, 7, 9, 6, 10])`
- **Analogía**: Como una fila de casilleros

### Tensor 2D - Matriz
- **¿Qué es?** Una tabla de números (filas y columnas)
- **Ejemplo**: Una imagen en blanco y negro (píxeles organizados en filas y columnas)
- **Shape**: (altura, ancho) como (28, 28) para una imagen pequeña
- **En código**: Una tabla de números
- **Analogía**: Como una hoja de cálculo de Excel

### Tensor 3D
- **¿Qué es?** Un cubo de números
- **Ejemplo**: El profesor mencionó *"una imagen en RGB"* - tiene altura, ancho y 3 canales de color
- **Shape**: (altura, ancho, canales) como (224, 224, 3)
- **Analogía**: Como un libro donde cada página es una matriz

### Tensor 4D y superiores
- **¿Qué es?** Estructuras con aún más dimensiones
- **Ejemplo**: Un lote de imágenes para entrenar (batch, altura, ancho, canales)
- **Shape**: (32, 224, 224, 3) - 32 imágenes RGB

## El Concepto de Shape (Forma)

El profesor enfatizó mucho la importancia del **shape**: *"nos va a importar bastante cuál es el shape del tensor"*.

### ¿Qué es el shape?
El **shape** es una tupla que te dice exactamente cómo está organizado tu tensor:
- Shape (10,) → Vector con 10 elementos
- Shape (5, 3) → Matriz de 5 filas y 3 columnas
- Shape (32, 28, 28) → 32 imágenes de 28×28 píxeles

### ¿Por qué es tan importante?
El profesor advirtió: *"el tema del shape siempre es un niño... siempre aparece un error por el tema de tener mal el shape"*. Es decir, muchos errores en Deep Learning vienen de intentar operar con tensores de shapes incompatibles.

## Diferencia entre Definición Matemática e Implementación

El profesor hizo una distinción crucial que confunde a muchos principiantes:

### En Matemáticas
- Un **vector columna** es técnicamente una matriz de shape (n, 1)
- Un **vector fila** es una matriz de shape (1, n)

### En Código (PyTorch/NumPy)
- Un **vector** es simplemente un tensor 1D de shape (n,)
- No es lo mismo que una matriz de shape (n, 1)

Como explicó el profesor: *"un vector en realidad en código es un tensor de dimensión uno... pero en matemática, un vector en realidad... es un tensor de dimensión dos"*.

### Ejemplo práctico de la diferencia
```python
# En código:
vector_1d = tensor([1, 2, 3, 4])  # Shape: (4,)
vector_columna = tensor([[1], [2], [3], [4]])  # Shape: (4, 1)

# ¡No son lo mismo! Operan diferente
```

## Operaciones con Tensores

### 1. Operaciones Element-wise (Elemento a elemento)

Son operaciones que se aplican a cada elemento individualmente:

**Suma element-wise**: Sumar dos tensores del mismo shape
- Ejemplo: [1, 2, 3] + [4, 5, 6] = [5, 7, 9]
- Cada posición se suma con su correspondiente

**Multiplicación element-wise**: Multiplicar elemento por elemento
- Ejemplo: [2, 3] × [4, 5] = [8, 15]
- NO es multiplicación matricial

### 2. Multiplicación Matricial

El profesor explicó que esto es fundamental: *"la multiplicación entre matrices corresponde a componer transformaciones lineales"*.

**Regla básica**: 
- Para multiplicar A×B, las columnas de A deben coincidir con las filas de B
- Si A tiene shape (m, n) y B tiene shape (n, p), el resultado tiene shape (m, p)
- *"la dimensión del medio intermedia... tiene que coincidir"*

**Ejemplo visual**:
```
Matriz A (2×3) × Matriz B (3×4) = Matriz C (2×4)
         ↑              ↑
    Estos deben coincidir
```

### 3. Transposición

**¿Qué es?** Intercambiar filas por columnas
- Una matriz de shape (3, 2) transpuesta queda (2, 3)
- Es como rotar la tabla 90 grados

## Broadcasting: La Magia de PyTorch

El profesor dedicó tiempo considerable al broadcasting, advirtiendo sobre sus sutilezas.

### ¿Qué es Broadcasting?

Es la capacidad de PyTorch de hacer operaciones entre tensores de diferentes shapes automáticamente, expandiendo los más pequeños.

### Ejemplo simple del profesor
*"Si yo agarro un tensor... una matriz de shape (m, n) y le sumo un tensor de dimensión uno que tiene shape (n,), esto va a hacer broadcasting y es como sumar ese vector a cada una de las filas"*.

**Ejemplo visual**:
```
Matriz (3×3)  +  Vector (3,)  =  Resultado (3×3)
[[1, 2, 3]       [10, 20, 30]    [[11, 22, 33]
 [4, 5, 6]   +                =   [14, 25, 36]
 [7, 8, 9]]                       [17, 28, 39]]

El vector se "repite" para cada fila automáticamente
```

### Las reglas del Broadcasting

El profesor explicó que el broadcasting *"sigue una regla que es difícil de entender... lee las dimensiones de derecha a izquierda"*:

1. **Compara shapes de derecha a izquierda**
2. **Si falta una dimensión, la considera como 1**
3. **Expande las dimensiones de tamaño 1 para que coincidan**

### Advertencia del profesor
*"A veces, si uno juega con shapes y suma cosas, nunca le va a tirar error. Probablemente siempre haga algún broadcasting"*. Esto puede causar bugs sutiles si no entiendes qué está pasando.

## Operaciones de Reducción

El profesor explicó las operaciones que "reducen" las dimensiones:

### Sum (Suma)
- **Por filas**: Suma todos los elementos de cada fila → reduce una dimensión
- **Por columnas**: Suma todos los elementos de cada columna
- **Total**: Suma todos los elementos → resulta en un escalar

### Mean (Promedio)
Similar a sum pero divide por el número de elementos

### Ejemplo del profesor
*"Si yo tengo una matriz y le digo suma en el eje 0, lo que estoy haciendo es sumar las columnas"*.

## Indexación y Slicing

El profesor mostró cómo acceder a partes específicas de un tensor:

### Notación
- `X[i, j, k]` - Accede a un elemento específico
- `X[:, j, :]` - Toma toda una "rebanada" fijando j
- `X[2:5, :]` - Toma filas del 2 al 4

Como explicó: *"Si yo hago X dos puntos coma j... estoy agarrando j y lo estoy fijando... es como si estuviera cortando"*.

## Errores Comunes y Consejos del Profesor

### 1. Errores de Shape
*"Van a estar dos horas y les devuelve que no es la dimensión correcta"*. Siempre verifica los shapes antes de operar.

### 2. Confundir vector 1D con matriz columna
Recuerda que en código, shape (n,) ≠ shape (n, 1)

### 3. Broadcasting no intencional
*"Siempre que tengas que ir al caso concreto... yo tengo un tensor de este shape y uno de este shape, ¿cómo es el broadcasting?"*

### 4. No entender qué eje estás operando
Cuando reduces o sumas, asegúrate de entender qué dimensión estás colapsando

## Conexión con el Código

El profesor enfatizó la importancia de conectar la teoría con la práctica:
- *"El objetivo... es que ustedes, cuando vean una ecuación, la logren entender... y la hagan corresponder al código"*
- No se trata de memorizar, sino de entender la correspondencia matemática-código

## Resumen Final

Los tensores son la base de todo en Deep Learning:
- **Son contenedores de datos** con formas específicas
- **El shape es crucial** - determina qué operaciones puedes hacer
- **Las operaciones básicas** (suma, multiplicación, broadcasting) son los bloques de construcción
- **La práctica es esencial** - los errores de shape son comunes al principio

Como concluyó el profesor, no es necesario ser experto en álgebra lineal, pero sí entender estos conceptos básicos para poder trabajar con Deep Learning efectivamente.