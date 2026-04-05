# Clase 1 (20 de Agosto 2025) - Taller de Deep Learning
## Introducción a PyTorch y Tensores

---

# INFORMACIÓN DEL CURSO

## Profesores

| Nombre | Rol | Contacto |
|--------|-----|----------|
| **Jo Viña (Joaquín)** | Profesor principal | Teams o email (disponible en Aulas) |
| **Marcos** | Profesor asistente ("una eminencia") | Email |
| **Ari** | Asistente (también alumno de posgrado) | Email |

> "Mi nombre es Jo Viña. Este la forma de contactarme a mí es fuera de clase también en clase. Me pueden escribir por Teams o por mail."

> "Marcos es una eminencia. Es bastante callado, pero todo lo que yo no sepa, él lo sabe mucho más que yo."

## Filosofía del Curso

> "Esta clase es 100% práctica. O sea, no va a haber presentaciones. No va haber ningún discurso, capaz que tocaremos un poquito de pizarrón cuando queramos bajar algo a tierra. Pero vamos a tocar mucha mano de lo que es PyTorch."

**Característica clave**: Todo el curso se trabaja con **Jupyter Notebooks** usando **PyTorch**.

---

# SISTEMA DE EVALUACIÓN

```
╔══════════════════════════════════════════════════════════════════════════╗
║                        DISTRIBUCIÓN DE PUNTOS                            ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║   ┌─────────────────────────────────────────────────────────────────┐   ║
║   │  LABORATORIO 1 .............. 15 puntos                         │   ║
║   │  (entrega mitad de semestre)                                    │   ║
║   │                                                                 │   ║
║   │  LABORATORIO 2 .............. 15 puntos                         │   ║
║   │  (sobre redes recurrentes, hacia el final)                      │   ║
║   │                                                                 │   ║
║   │  PARCIAL ESCRITO ............ 20 puntos                         │   ║
║   │  (preguntas de alto nivel + defensa del obligatorio)            │   ║
║   │                                                                 │   ║
║   │  OBLIGATORIO FINAL .......... 50 puntos                         │   ║
║   │  (incluye competencia en Kaggle)                                │   ║
║   └─────────────────────────────────────────────────────────────────┘   ║
║                                                                          ║
║   TOTAL: 100 puntos                                                      ║
║   APROBACIÓN: 70 puntos                                                  ║
║   EXCELENCIA: 90+ puntos                                                 ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### Sobre el Parcial

> "El parcial no busca... no salvar la materia, sino lo busca la excelencia, pasar los 90 puntos. Es porque le fue realmente muy bien y domina muy bien la materia."

> "Son preguntas de alto nivel. No hay que escribir 15 líneas de código compilable por Python. No, no hay que hacer eso, sino hay que esperar conocimientos a alto nivel."

### Premio Especial: Competencia Kaggle

> "Lo que yo propongo es que al mejor obligatorio, que gane la competencia de Kaggle, un libro."

El profesor mostró un libro de un YouTuber que explica conceptos difíciles como la **atención** (tema de las últimas clases).

### Notebooks Opcionales

> "Todas las notebooks que vamos a ver en las clases, las pueden entregar como valor simbólico. Si hay alguien que está en una cornisa, entregando todas esas notebooks puede pasar para el otro lado."

- **Fecha límite**: 1 de diciembre
- **Recomendación del profesor**: Ir haciéndolas semana a semana, no dejarlas para el final

---

# CONFIGURACIÓN DEL AMBIENTE

## ¿Qué es Conda?

> "Conda te sirve para crear ambientes aislados separados. Entonces, vos tenés un proyecto que requiere Python X y tenés otro del trabajo que requiere Python Y. Te gustaría no tener todo instalado o capaz que tenés problemas de compatibilidades y de alguna manera aislar diferentes ambientes."

**Explicación simple**: Conda es como tener varias computadoras virtuales separadas, cada una con sus propios programas instalados, para que no se mezclen ni se rompan entre sí.

## Archivos de Ambiente

El profesor provee dos archivos:
1. **Sin CUDA** - Para Mac o si no tienes tarjeta NVIDIA
2. **Con CUDA** - Si tienes tarjeta NVIDIA con CUDA instalado

## Opciones para Ejecutar Notebooks

```
╔════════════════════════════════════════════════════════════════════════╗
║                   ¿DÓNDE EJECUTAR LAS NOTEBOOKS?                       ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   OPCIÓN 1: LOCAL                                                      ║
║   ├── Usar archivo environment.yml de Conda                            ║
║   ├── Requiere configuración inicial                                   ║
║   └── Ventaja: Control total                                           ║
║                                                                        ║
║   OPCIÓN 2: GOOGLE COLAB (RECOMENDADO para empezar)                    ║
║   ├── Ya tiene casi todo instalado                                     ║
║   ├── GPU gratuita (limitada)                                          ║
║   └── "Das play y arrancaste"                                          ║
║                                                                        ║
║   OPCIÓN 3: NOTEBOOKS DE LA FACULTAD                                   ║
║   ├── Tienen GPU disponible                                            ║
║   ├── Limitadas (~8 al mismo tiempo)                                   ║
║   └── "Sean buenos ciudadanos: desconéctense cuando terminen"          ║
║                                                                        ║
║   OPCIÓN 4: SERVICIOS PAGOS (Kaggle, Lambda Labs, etc.)                ║
║   ├── ~$5-10/mes                                                       ║
║   └── Solo si las opciones gratuitas no alcanzan                       ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

### Sobre la Necesidad de GPU

> "Te diría que en un 100% es más que no [necesaria], pero me imagino que hay momentos que sí."

> "El obligatorio es muy probable que necesiten GPU. Este año no va a ser tan intenso como el semestre pasado."

---

# ¿QUÉ ES UN TENSOR?

## Definición Simple

> "Es una matriz multidimensional que puede ser desde cero dimensiones hasta N dimensiones."

**Analogía**: Un tensor es como una caja que puede contener números organizados de diferentes formas:

```
╔═══════════════════════════════════════════════════════════════════════╗
║                      DIMENSIONES DE TENSORES                          ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║   0 DIMENSIONES (Escalar):        5                                   ║
║   └── Un solo número                                                  ║
║                                                                       ║
║   1 DIMENSIÓN (Vector):           [1, 2, 3, 4, 5]                     ║
║   └── Una fila de números                                             ║
║                                                                       ║
║   2 DIMENSIONES (Matriz):         [[1, 2, 3],                         ║
║   └── Una tabla de números         [4, 5, 6],                         ║
║                                    [7, 8, 9]]                         ║
║                                                                       ║
║   3+ DIMENSIONES (Tensor):        Cubo, hipercubo, etc.               ║
║   └── "Cuando empezamos con 3 dimensiones, no es algo fácil           ║
║       de imprimir y llevar"                                           ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
```

## ¿Por Qué Tensores y No NumPy?

> "NumPy directamente siempre va a trabajar sobre CPU. Y en realidad PyTorch puede trabajar con GPU, o sea en CUDA."

**Ventajas de PyTorch sobre NumPy**:
1. Puede ejecutar en **GPU** (15-50x más rápido)
2. Calcula **gradientes automáticamente** (para entrenar redes neuronales)
3. Mismas operaciones funcionan en CPU o GPU sin cambiar código

## Regla Importante

> "La característica que tienen los tensores es que todos los elementos que existen dentro de un tensor tienen que tener el mismo tipo."

**No puedes mezclar** enteros, decimales y booleanos en el mismo tensor.

---

# CREAR TENSORES

## ¿Qué significa "crear un tensor"?

Crear un tensor es **reservar un espacio en la memoria** de tu computadora para guardar números organizados de cierta forma. Es como crear una tabla vacía (o con valores) donde después vas a hacer cálculos.

## Formas Básicas de Crear Tensores

### Desde una lista de Python

```python
import torch

x = torch.tensor([1, 2, 3])
```

**¿Qué hace cada parte?**
- `import torch` → Carga la librería PyTorch para poder usarla
- `torch.tensor(...)` → Función que CREA un tensor
- `[1, 2, 3]` → Los datos que quiero guardar (una lista de Python)
- `x = ...` → Guardo el tensor en una variable llamada `x`

**Resultado:** Un tensor de 1 dimensión con 3 elementos: `tensor([1, 2, 3])`

### Desde un array de NumPy

```python
import numpy as np
arr = np.array([1, 2, 3])
x = torch.tensor(arr)
```

**¿Qué hace cada parte?**
- `np.array([1, 2, 3])` → Crea un array de NumPy (otra librería de Python para matemáticas)
- `torch.tensor(arr)` → Convierte ese array de NumPy a un tensor de PyTorch

**¿Por qué harías esto?** Muchos datos vienen en formato NumPy (ej: imágenes cargadas con otras librerías). Necesitas convertirlos a tensores para usar PyTorch.

### Copiar un tensor existente

```python
y = x.clone()
```

**¿Qué hace?**
- `.clone()` → Crea una **copia independiente** del tensor
- La copia vive en memoria separada
- Si modificas `y`, `x` NO se modifica (y viceversa)

**⚠️ ADVERTENCIA:** Si haces `y = x` (sin `.clone()`), NO creas una copia. Ambas variables apuntan al MISMO tensor. Ver sección de advertencias más abajo.

---

## Tensores Especiales (Pre-llenados)

### torch.zeros() - Tensor lleno de ceros

```python
torch.zeros(2, 3)
```

**¿Qué hace cada parte?**
- `torch.zeros(...)` → Crea un tensor lleno de CEROS
- `2, 3` → Las dimensiones: 2 filas, 3 columnas

**Resultado:**
```
tensor([[0., 0., 0.],
        [0., 0., 0.]])
```

**¿Para qué sirve?**
- Inicializar un tensor antes de llenarlo con cálculos
- Crear "lienzos en blanco" para acumular resultados

### torch.ones() - Tensor lleno de unos

```python
torch.ones(2, 3)
```

**¿Qué hace?** Igual que `zeros`, pero llena con UNOS en vez de ceros.

**Resultado:**
```
tensor([[1., 1., 1.],
        [1., 1., 1.]])
```

**¿Para qué sirve?**
- Crear máscaras iniciales
- Inicializar pesos en algunos casos

### torch.rand() - Valores aleatorios entre 0 y 1

```python
torch.rand(2, 3)
```

**¿Qué hace cada parte?**
- `torch.rand(...)` → Crea tensor con valores **aleatorios**
- Los valores están entre 0 y 1 (pero nunca exactamente 0 ni 1)
- Distribución **uniforme**: todos los valores son igual de probables

**Resultado (ejemplo, varía cada vez):**
```
tensor([[0.4523, 0.8912, 0.1234],
        [0.7891, 0.2345, 0.5678]])
```

**¿Para qué sirve?**
- Inicializar pesos de redes neuronales aleatoriamente
- Generar datos de prueba

### torch.randn() - Valores aleatorios con distribución normal

```python
torch.randn(2, 3)
```

**¿Qué hace de diferente a `rand`?**
- Los valores siguen una **distribución normal** (campana de Gauss)
- Media = 0, Desviación estándar = 1
- Los valores pueden ser negativos o mayores que 1
- Valores cercanos a 0 son más probables

**Resultado (ejemplo):**
```
tensor([[-0.5234,  1.2345, -0.0012],
        [ 0.8901, -1.5678,  0.3456]])
```

**¿Para qué sirve?**
- Es la forma más común de inicializar pesos de redes neuronales
- Simular ruido gaussiano

### torch.arange() - Secuencia de números

```python
torch.arange(0, 10, 2)
```

**¿Qué hace cada parte?**
- `torch.arange(inicio, fin, paso)` → Crea secuencia de números
- `0` → Empieza en 0
- `10` → Termina ANTES de 10 (no incluye el 10)
- `2` → Salta de 2 en 2

**Resultado:**
```
tensor([0, 2, 4, 6, 8])
```

**Otros ejemplos:**
```python
torch.arange(5)       # tensor([0, 1, 2, 3, 4]) - del 0 al 4
torch.arange(1, 6)    # tensor([1, 2, 3, 4, 5]) - del 1 al 5
torch.arange(0, 1, 0.1)  # tensor([0.0, 0.1, 0.2, ..., 0.9])
```

### torch.full() - Tensor lleno de un valor específico

```python
torch.full((3, 3), 5)
```

**¿Qué hace cada parte?**
- `torch.full(forma, valor)` → Crea tensor lleno de un valor
- `(3, 3)` → La forma (3 filas × 3 columnas). **Nota: va entre paréntesis**
- `5` → El valor con el que llenar

**Resultado:**
```
tensor([[5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]])
```

---

## Funciones "Like" (Crear tensor con la misma forma que otro)

> "El like es bastante útil porque a nosotros nos puede pasar que viene un input que no sabemos de cuánto es el batch. No sabemos cuántas son las dimensiones."

### ¿Qué problema resuelven?

Imagina que te llega un tensor `x` de algún lugar y necesitas crear otro tensor del MISMO tamaño pero lleno de ceros. Sin las funciones "like" tendrías que hacer:

```python
x = algun_tensor_que_te_llego  # No sabes su tamaño
# Opción complicada:
zeros = torch.zeros(x.size(0), x.size(1), x.size(2)...)  # ¡Tedioso!
```

Con las funciones "like":
```python
zeros = torch.zeros_like(x)  # ¡Automático!
```

### Las funciones "like"

```python
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])  # Tensor de forma 2×3

torch.zeros_like(x)
# Resultado: tensor([[0, 0, 0],
#                    [0, 0, 0]])
# Misma forma (2×3), pero lleno de ceros

torch.ones_like(x)
# Resultado: tensor([[1, 1, 1],
#                    [1, 1, 1]])
# Misma forma, lleno de unos

torch.rand_like(x.float())  # Nota: necesita ser float para rand
# Resultado: tensor([[0.xx, 0.xx, 0.xx],
#                    [0.xx, 0.xx, 0.xx]])
# Misma forma, valores aleatorios
```

**¿Cuándo usarlas?**
- Cuando procesas datos y no sabes de antemano su tamaño
- Cuando quieres crear un tensor "auxiliar" del mismo tamaño
- En funciones que reciben tensores de tamaño variable

---

# ⚠️ ADVERTENCIA: COPIAR TENSORES

## El Error Común

> "Uno de los errores que podemos cometer es que directamente estar igualando un tensor a otro."

```python
x = torch.tensor([1, 2, 3])
y = x  # ⚠️ NO ES UNA COPIA, es la misma memoria

y[0] = 100  # ¡Esto también modifica x!

print(x)  # tensor([100, 2, 3])  ← ¡Cambió!
print(y)  # tensor([100, 2, 3])
```

## La Solución: .clone()

```python
x = torch.tensor([1, 2, 3])
z = x.clone()  # ✅ COPIA REAL, memoria separada

z[0] = 100  # Solo modifica z

print(x)  # tensor([1, 2, 3])  ← Sin cambios
print(z)  # tensor([100, 2, 3])
```

---

# TIPOS DE DATOS EN TENSORES

## Tabla de Tipos Principales

| Tipo | Descripción | Uso Común |
|------|-------------|-----------|
| `uint8` | Enteros 0-255 | Píxeles de imágenes RGB |
| `int32`, `int64` | Enteros con signo | Etiquetas, índices |
| `float32` | Decimales (32 bits) | **PESOS DE REDES NEURONALES** (más usado) |
| `float16` | Decimales (16 bits) | Modelos grandes (ahorra memoria) |
| `bool` | Verdadero/Falso | Máscaras |

### Sobre float32 (El Más Importante)

> "Yo diría que el más conocido o el que más van a utilizar son los float. Porque bueno, básicamente todos los pesos que vamos a tener dentro de nuestra red probablemente estén en ese tipo de precisión."

### Sobre float16 y Cuantización

> "Cuando tenés modelos MUY grandes, te puede interesar el tema de 16 o no. Y hay cosas que te interesa que estén en 32 y que no."

El profesor Marcos explicó:
- **float32**: 4 bytes, mayor precisión
- **float16**: 2 bytes, menor precisión pero ahorra memoria
- **bfloat16**: Formato especial de Google, mantiene rango pero pierde precisión

### Ejemplo: Imágenes

> "Los píxeles pueden ser representados de 0 a 255. Pero muchas veces lo que hacemos con las imágenes es normalizarlas y pasarlas de 0-255 a 0-1."

```python
# Imagen original (uint8)
imagen = torch.tensor([0, 128, 255], dtype=torch.uint8)

# Normalizada (float32)
imagen_norm = imagen.float() / 255.0  # [0.0, 0.5, 1.0]
```

---

# PROPIEDADES DE TENSORES

## ¿Qué son las propiedades?

Las propiedades son **información sobre el tensor**: su tamaño, tipo de datos, dónde vive en memoria, etc. Son como la "ficha técnica" del tensor.

## Las Propiedades Más Importantes (Explicadas)

```python
x = torch.randn(2, 3, 4)  # Creamos un tensor 3D de 2×3×4
```

### dtype - Tipo de dato

```python
x.dtype
# Resultado: torch.float32
```

**¿Qué significa?**
- `dtype` = "data type" = tipo de dato
- Te dice qué tipo de números guarda el tensor
- `float32` significa números decimales de 32 bits de precisión

**Tipos comunes:**
- `torch.float32` → Decimales (el más usado para redes neuronales)
- `torch.int64` → Enteros
- `torch.bool` → Verdadero/Falso

### shape - Dimensiones del tensor

```python
x.shape
# Resultado: torch.Size([2, 3, 4])
```

**¿Qué significa?**
- Te dice la "forma" del tensor
- `[2, 3, 4]` significa:
  - 2 "capas" (primera dimensión)
  - 3 filas en cada capa (segunda dimensión)
  - 4 columnas en cada fila (tercera dimensión)
- Total de elementos: 2 × 3 × 4 = 24 números

### size() - Igual que shape pero como método

```python
x.size()      # torch.Size([2, 3, 4]) - igual que shape
x.size(0)     # 2 - solo la primera dimensión
x.size(1)     # 3 - solo la segunda dimensión
x.size(2)     # 4 - solo la tercera dimensión
```

**¿Cuál usar?**

> "Yo diría que la forma más adecuada o más prolija es el size(). ¿Por qué? Si bien dan el mismo resultado, nosotros podemos preguntarle, por ejemplo, size(0), size(1)."

- `size()` es más flexible porque puedes pedir una dimensión específica
- `shape` es más rápido de escribir

### ndim - Número de dimensiones

```python
x.ndim
# Resultado: 3
```

**¿Qué significa?**
- `ndim` = "number of dimensions" = número de dimensiones
- Te dice cuántas dimensiones tiene el tensor
- Un escalar tiene 0, un vector tiene 1, una matriz tiene 2, etc.

### device - Dónde vive el tensor

```python
x.device
# Resultado: device(type='cpu')
```

**¿Qué significa?**
- Te dice si el tensor está en CPU (memoria RAM) o GPU (memoria de la tarjeta gráfica)
- Puede ser `'cpu'`, `'cuda:0'` (primera GPU NVIDIA), `'mps'` (GPU de Mac), etc.

### requires_grad - ¿Calcula gradientes?

```python
x.requires_grad
# Resultado: False
```

**¿Qué significa?**
- `requires_grad` = "requiere gradientes"
- Si es `True`, PyTorch guardará un historial de operaciones para calcular derivadas
- Se usa para entrenar redes neuronales (lo veremos en la clase 2)

---

# DEVICE: CPU vs GPU

## ¿Qué es el Device?

> "Los tensores pueden vivir en memoria CPU, en la RAM, o en la GPU."

**Device** (dispositivo) es DÓNDE vive el tensor en tu computadora:
- **CPU**: En la memoria RAM normal de tu computadora
- **GPU**: En la memoria de tu tarjeta gráfica (mucho más rápida para matemáticas)

```
╔════════════════════════════════════════════════════════════════════════╗
║                        DISPOSITIVOS (DEVICES)                          ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   'cpu'     →  Memoria RAM normal (siempre disponible)                 ║
║               Todas las computadoras la tienen                         ║
║                                                                        ║
║   'cuda'    →  GPU NVIDIA (requiere CUDA instalado)                    ║
║   'cuda:0'  →  Primera GPU NVIDIA                                      ║
║   'cuda:1'  →  Segunda GPU (si tienes varias)                          ║
║               Tu RTX 4070 sería 'cuda:0'                               ║
║                                                                        ║
║   'mps'     →  GPU de Mac (M1, M2, etc.)                               ║
║               Solo en computadoras Apple Silicon                       ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

## ¿Por qué usar GPU?

La GPU puede hacer miles de operaciones matemáticas **en paralelo**, mientras que la CPU las hace una por una. Para multiplicar matrices grandes (que es lo que hacen las redes neuronales), la GPU es 15-50 veces más rápida.

## Verificar Disponibilidad de GPU

```python
# ¿Tengo GPU NVIDIA disponible?
if torch.cuda.is_available():
    device = 'cuda'
# ¿Tengo Mac con chip M (Apple Silicon)?
elif torch.backends.mps.is_available():
    device = 'mps'
# Si no hay GPU, uso CPU
else:
    device = 'cpu'

print(device)
```

**¿Qué hace cada línea?**
- `torch.cuda.is_available()` → Pregunta si hay GPU NVIDIA con CUDA instalado
- `torch.backends.mps.is_available()` → Pregunta si hay GPU de Mac
- `device = 'cuda'` → Guarda el nombre del dispositivo para usarlo después

## Crear o Mover Tensores a GPU

### Opción 1: Crear directamente en GPU

```python
x = torch.tensor([1, 2, 3], device='cuda')
```

**¿Qué hace?**
- `device='cuda'` → Le dice a PyTorch que cree el tensor directamente en la GPU
- El tensor nunca pasa por la CPU

### Opción 2: Mover un tensor existente

```python
x = torch.tensor([1, 2, 3])  # Creado en CPU (por defecto)
x = x.to('cuda')             # Movido a GPU
```

**¿Qué hace?**
- `.to('cuda')` → Crea una COPIA del tensor en la GPU
- El original en CPU se descarta (si no lo guardaste en otra variable)

### Forma más flexible (funciona en cualquier computadora)

```python
device = 'cuda' if torch.cuda.is_available() else 'cpu'
x = torch.tensor([1, 2, 3]).to(device)
```

**¿Por qué hacerlo así?**
- Si tienes GPU, usa GPU
- Si no tienes GPU, usa CPU
- El mismo código funciona en cualquier computadora

## ⚠️ Advertencia IMPORTANTE sobre Mover Tensores

> "Mover un tensor suficientemente grande de un lado a otro puede ser una operación entre comillas costosa. Si todo el tiempo estás pasando de memoria a GPU, puede ser un cuello de botella."

**El problema:**
- Mover datos entre CPU y GPU es LENTO
- Si mueves datos en cada iteración, pierdes todo el beneficio de la GPU

**La solución:**
- Mueve los datos a GPU UNA VEZ al principio
- Haz todos los cálculos en GPU
- Solo mueve resultados finales de vuelta a CPU cuando termines

## ⚠️ Los tensores deben estar en el MISMO device para operar

```python
x_cpu = torch.tensor([1, 2, 3])           # En CPU
x_gpu = torch.tensor([4, 5, 6]).to('cuda')  # En GPU

x_cpu + x_gpu  # ❌ ERROR: no se pueden sumar tensores en diferentes devices
```

**Solución:** Mover ambos al mismo device antes de operar.

---

# OPERACIONES BÁSICAS

## ¿Qué significa "operación elemento a elemento"?

Cuando sumas, restas, multiplicas o divides dos tensores del mismo tamaño, la operación se hace **posición por posición**:
- El primer elemento de uno con el primer elemento del otro
- El segundo con el segundo
- Y así sucesivamente

## Operaciones Elemento a Elemento

```python
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
```

### Suma: `x + y`

```python
x + y
# Resultado: tensor([5, 7, 9])
```

**¿Qué hizo?**
```
x:       [1, 2, 3]
y:       [4, 5, 6]
         ─────────
x + y:   [5, 7, 9]   # 1+4=5, 2+5=7, 3+6=9
```

### Resta: `x - y`

```python
x - y
# Resultado: tensor([-3, -3, -3])
```

**¿Qué hizo?**
```
x:       [1, 2, 3]
y:       [4, 5, 6]
         ─────────
x - y:   [-3, -3, -3]   # 1-4=-3, 2-5=-3, 3-6=-3
```

### Multiplicación: `x * y`

```python
x * y
# Resultado: tensor([4, 10, 18])
```

**¿Qué hizo?**
```
x:       [1, 2, 3]
y:       [4, 5, 6]
         ─────────
x * y:   [4, 10, 18]   # 1×4=4, 2×5=10, 3×6=18
```

**⚠️ OJO:** Esto NO es multiplicación de matrices, es multiplicación elemento por elemento.

### División: `x / y`

```python
x / y
# Resultado: tensor([0.25, 0.4, 0.5])
```

**¿Qué hizo?**
```
x:       [1,    2,   3  ]
y:       [4,    5,   6  ]
         ────────────────
x / y:   [0.25, 0.4, 0.5]   # 1/4=0.25, 2/5=0.4, 3/6=0.5
```

### Otras operaciones útiles

```python
x ** 2      # Potencia: tensor([1, 4, 9]) - cada elemento al cuadrado
x % 2       # Módulo: tensor([1, 0, 1]) - resto de dividir por 2
torch.sqrt(x.float())  # Raíz cuadrada: tensor([1.0, 1.41, 1.73])
```

**Requisito**: Los tensores deben tener el mismo tamaño (o ser "broadcastables" - ver siguiente sección).

---

## Operaciones In-Place (Con Guión Bajo)

> "Las operaciones in-place terminan en guión bajo. Básicamente sustituyen directamente el tensor que están operando."

### ¿Qué es "in-place"?

"In-place" significa **modificar el tensor original** en lugar de crear uno nuevo. Es como escribir encima del papel en vez de usar una hoja nueva.

### Comparación: Normal vs In-Place

```python
x = torch.tensor([1, 2, 3])

# OPERACIÓN NORMAL (crea nuevo tensor)
y = x + 5
print(x)  # tensor([1, 2, 3]) - x NO cambió
print(y)  # tensor([6, 7, 8]) - y es el resultado nuevo
```

```python
x = torch.tensor([1, 2, 3])

# OPERACIÓN IN-PLACE (modifica x directamente)
x.add_(5)
print(x)  # tensor([6, 7, 8]) - x SÍ cambió
# No hay 'y', el resultado se guardó en x
```

### Lista de operaciones in-place comunes

```python
x.add_(5)      # x = x + 5
x.sub_(5)      # x = x - 5
x.mul_(2)      # x = x * 2
x.div_(2)      # x = x / 2
x.zero_()      # Llena x con ceros
x.fill_(7)     # Llena x con 7
```

**Patrón:** El guión bajo `_` al final indica que modifica el tensor original.

### ¿Cuándo usar in-place?

> "Cuando vos manejás tensores suficientemente grandes y simplemente vas a hacer x igual a x + algo, capaz que es mucho mejor hacer un in-place y no estar generando una nueva memoria mientras estás esperando."

**Usar in-place cuando:**
- Tienes tensores muy grandes (ahorras memoria)
- No necesitas el valor original

**NO usar in-place cuando:**
- Necesitas conservar el valor original
- Estás calculando gradientes (puede causar errores)

---

# ⚠️ BROADCASTING (PREGUNTA DE PARCIAL)

> "Pregunta de parcial. Yo siempre voy diciendo esto."

## ¿Qué es Broadcasting?

Broadcasting permite operar tensores de **diferentes tamaños** automáticamente, "expandiendo" el más pequeño.

## Las 3 Reglas (MEMORIZAR)

```
╔════════════════════════════════════════════════════════════════════════╗
║                    REGLAS DE BROADCASTING                              ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   1. Comparar dimensiones de DERECHA a IZQUIERDA                       ║
║                                                                        ║
║   2. Dos dimensiones son compatibles si:                               ║
║      • Son IGUALES, o                                                  ║
║      • Una de ellas es 1, o                                            ║
║      • Una de ellas NO EXISTE                                          ║
║                                                                        ║
║   3. Si ALGUNA comparación falla → ERROR                               ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

## Ejemplos Resueltos

### Ejemplo 1: SON Broadcastables ✅

```
Tensor X:  (5, 3, 4, 1)
Tensor Y:      (3, 1, 1)

Comparamos de derecha a izquierda:
  1 vs 1  → Iguales ✅
  4 vs 1  → Una es 1 ✅
  3 vs 3  → Iguales ✅
  5 vs -  → No existe ✅

RESULTADO: SON compatibles ✅
```

### Ejemplo 2: NO son Broadcastables ❌

```
Tensor A:  (3, 4, 2)
Tensor B:  (3, 4, 3)

Comparamos de derecha a izquierda:
  2 vs 3  → No son iguales, ninguno es 1, ambos existen ❌

RESULTADO: NO son compatibles ❌
```

### Ejemplo 3: Ejercicio de Clase

```python
x = torch.randn(3)      # shape: (3,)
y = torch.randn(1, 3)   # shape: (1, 3)
z = torch.randn(2, 3)   # shape: (2, 3)

# ¿Se puede x + y?
#   3 vs 3 → Iguales ✅
#   - vs 1 → No existe ✅
# RESULTADO: SÍ ✅

# ¿Se puede x + z?
#   3 vs 3 → Iguales ✅
#   - vs 2 → No existe ✅
# RESULTADO: SÍ ✅

# ¿Se puede y + z?
#   3 vs 3 → Iguales ✅
#   1 vs 2 → Una es 1 ✅
# RESULTADO: SÍ ✅
```

---

# INDEXING Y SLICING

## ¿Qué son Indexing y Slicing?

- **Indexing** = Acceder a UN elemento específico por su posición
- **Slicing** = Acceder a un RANGO de elementos (una "rebanada")

> "Esto hereda cómo indexamos o hacemos el slice. Es algo que ya viene de Python, no es nada nuevo dentro de PyTorch."

---

## Vectores (1 Dimensión)

```python
x = torch.tensor([1, 2, 3, 4, 5])
#                 ^  ^  ^  ^  ^
#    Posiciones:  0  1  2  3  4
#    Posiciones: -5 -4 -3 -2 -1  (negativas cuentan desde el final)
```

### Acceder a UN elemento (Indexing)

```python
x[0]      # tensor(1) - primer elemento (posición 0)
x[2]      # tensor(3) - tercer elemento (posición 2)
x[-1]     # tensor(5) - ÚLTIMO elemento (posición -1)
x[-2]     # tensor(4) - penúltimo elemento
```

**¿Por qué se empieza en 0?** Es convención en programación. El primer elemento está en posición 0, el segundo en posición 1, etc.

### Acceder a un RANGO (Slicing)

La sintaxis es: `tensor[inicio:fin:paso]`
- `inicio` → Dónde empezar (incluido)
- `fin` → Dónde terminar (NO incluido)
- `paso` → De cuánto en cuánto avanzar

```python
x[1:4]    # tensor([2, 3, 4])
```

**¿Qué hizo?**
```
x = [1, 2, 3, 4, 5]
     0  1  2  3  4   ← posiciones
        ↑     ↑
      inicio  fin (no incluido)

Resultado: elementos en posiciones 1, 2, 3 → [2, 3, 4]
```

### Más ejemplos de slicing

```python
x[2:]     # tensor([3, 4, 5]) - desde posición 2 hasta el final
x[:3]     # tensor([1, 2, 3]) - desde el inicio hasta posición 2 (3 no incluido)
x[::2]    # tensor([1, 3, 5]) - todos, pero de 2 en 2 (paso = 2)
x[::-1]   # tensor([5, 4, 3, 2, 1]) - al revés (paso negativo)
```

---

## Matrices (2 Dimensiones)

```python
m = torch.tensor([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
```

La matriz se ve así:
```
         Columnas
           0  1  2
         ┌─────────┐
Fila 0 → │ 1  2  3 │
Fila 1 → │ 4  5  6 │
Fila 2 → │ 7  8  9 │
         └─────────┘
```

### Acceder a UN elemento: `m[fila, columna]`

```python
m[0, 0]     # tensor(1) - fila 0, columna 0 → esquina superior izquierda
m[1, 2]     # tensor(6) - fila 1, columna 2
m[-1, -1]   # tensor(9) - última fila, última columna → esquina inferior derecha
```

### Acceder a una FILA completa: `m[fila, :]`

```python
m[1, :]     # tensor([4, 5, 6]) - toda la fila 1
```

**¿Qué significa `:` ?**
- Los dos puntos sin nada significan "todo"
- `m[1, :]` = "fila 1, todas las columnas"

### Acceder a una COLUMNA completa: `m[:, columna]`

```python
m[:, 2]     # tensor([3, 6, 9]) - toda la columna 2
```

**¿Qué significa?**
- `m[:, 2]` = "todas las filas, columna 2"

### Acceder a una SUBMATRIZ

```python
m[0:2, 1:3]
# Resultado: tensor([[2, 3],
#                    [5, 6]])
```

**¿Qué hizo?**
```
         Columnas 1:3 (columnas 1 y 2)
              ↓  ↓
    [[1,  [2, 3],    ← Fila 0 (incluida en 0:2)
     [4,  [5, 6],    ← Fila 1 (incluida en 0:2)
     [7,   8, 9]]]   ← Fila 2 (NO incluida en 0:2)
```

---

## ⚠️ ADVERTENCIA MUY IMPORTANTE: Indexing Crea VISTAS, No Copias

> "Cuando estamos haciendo indexaciones o slicing, esto es literalmente como una vista. Lo que está haciendo es como una forma de ver un pedazo o una ventana de los datos originales."

**El problema:**

```python
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

y = x[1, :]      # y = la fila 1 de x
print(y)         # tensor([4, 5, 6])

y[0] = 100       # Cambio el primer elemento de y

print(y)         # tensor([100, 5, 6]) - y cambió (esperado)
print(x)         # ¡SORPRESA! x TAMBIÉN cambió:
# tensor([[  1,   2,   3],
#         [100,   5,   6],   ← ¡El 4 se convirtió en 100!
#         [  7,   8,   9]])
```

**¿Por qué pasa esto?**

`y` NO es una copia, es una "ventana" que mira los mismos datos que `x`. Cuando modificas `y`, modificas los datos originales.

**Solución: Usar `.clone()`**

```python
y = x[1, :].clone()  # Ahora y es una COPIA independiente
y[0] = 100           # Solo modifica y, no x
```

---

## Obtener Valor Python Nativo: .item()

> "Cuando yo agarro un tensor y literalmente agarro una posición, me está dando un tensor escalar, no el número."

**El problema:**

```python
x = torch.tensor([1, 2, 3, 4, 5])

valor = x[0]
print(valor)       # tensor(1)  ← Sigue siendo un tensor, no un número
print(type(valor)) # <class 'torch.Tensor'>
```

**La solución: `.item()`**

```python
valor = x[0].item()
print(valor)       # 1  ← Ahora sí es un número de Python
print(type(valor)) # <class 'int'>
```

**¿Cuándo usarlo?**

```python
# Útil para imprimir valores durante entrenamiento
print(f"Loss: {loss.item():.4f}")  # "Loss: 0.5234"

# Útil para guardar en listas de Python
resultados.append(accuracy.item())
```

**Restricción:** `.item()` solo funciona con tensores de UN solo elemento (escalares).

---

# MÁSCARAS BOOLEANAS

## ¿Qué es una máscara booleana?

Una **máscara** es un tensor de `True` y `False` que indica qué elementos queremos seleccionar. Es como un "filtro" que deja pasar solo algunos elementos.

> "Probablemente en su obligatorio van a tener que trabajar con tensores booleanos. Se trate de segmentación."

---

## Crear Máscara con una Condición

```python
x = torch.tensor([1, 2, 3, 4])

mask = x > 2
print(mask)  # tensor([False, False, True, True])
```

**¿Qué hizo?**
```
x =     [1,     2,     3,    4   ]
         ↓      ↓      ↓     ↓
x > 2 = [1>2?, 2>2?, 3>2?, 4>2?]
      = [False, False, True, True]
```

PyTorch evaluó la condición `> 2` para CADA elemento y guardó el resultado (`True` o `False`).

### Otras condiciones que puedes usar

```python
x = torch.tensor([1, 2, 3, 4])

x > 2   # tensor([False, False, True, True])  - mayores que 2
x >= 2  # tensor([False, True, True, True])   - mayores o iguales a 2
x == 2  # tensor([False, True, False, False]) - iguales a 2
x != 2  # tensor([True, False, True, True])   - diferentes de 2
x < 3   # tensor([True, True, False, False])  - menores que 3
```

---

## Aplicar Máscara (Filtrar Elementos)

```python
x = torch.tensor([1, 2, 3, 4])
mask = torch.tensor([True, False, True, True])

resultado = x[mask]
print(resultado)  # tensor([1, 3, 4])
```

**¿Qué hizo?**
```
x =       [1,    2,     3,    4   ]
mask =    [True, False, True, True]
           ↓     ✗      ↓     ↓
x[mask] = [1,           3,    4   ]
```

Solo se quedaron los elementos donde la máscara era `True`.

---

## Ejemplo Práctico: Sumar Elementos que Cumplen Condición

```python
x = torch.tensor([1, 2, 3, 4])

# Paso 1: Crear máscara para elementos > 2
mask = x > 2  # tensor([False, False, True, True])

# Paso 2: Filtrar elementos
filtrados = x[mask]  # tensor([3, 4])

# Paso 3: Sumar
total = filtrados.sum()  # tensor(7) porque 3 + 4 = 7

# Forma corta (todo en una línea):
(x[x > 2]).sum()  # tensor(7)
```

---

## Ejemplo: Crear Tensor con Valores Selectivos

```python
x = torch.tensor([1, 2, 3, 4])
mask = torch.tensor([True, False, True, True])

# Paso 1: Crear tensor de ceros del mismo tamaño
zeros = torch.zeros_like(x)
print(zeros)  # tensor([0, 0, 0, 0])

# Paso 2: Copiar valores de x solo donde mask es True
zeros[mask] = x[mask]
print(zeros)  # tensor([1, 0, 3, 4])
```

**¿Qué hizo?**
```
x =      [1,    2,    3,    4   ]
mask =   [True, False, True, True]
zeros =  [0,    0,    0,    0   ]

Después de zeros[mask] = x[mask]:
zeros =  [1,    0,    3,    4   ]
          ↑     ↑     ↑     ↑
          |    no     |     |
       copiado cambió copiado copiado
```

**Aplicación en el Obligatorio**: En segmentación de imágenes, la máscara indica qué píxeles son "persona" y cuáles son "fondo".

---

# OPERACIONES DE REDUCCIÓN

## ¿Qué es una "reducción"?

Una **reducción** es una operación que toma MUCHOS números y los convierte en MENOS números (o en un solo número). Por ejemplo:
- Sumar todos los elementos → obtienes UN número
- Calcular el promedio → obtienes UN número
- Encontrar el máximo por fila → obtienes UNA fila

---

## Funciones de Reducción Principales

```python
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
# x tiene 6 elementos en total
```

### .sum() - Sumar todos los elementos

```python
x.sum()  # tensor(21)
```

**¿Qué hizo?** Sumó TODOS los elementos: 1+2+3+4+5+6 = 21

### .mean() - Calcular el promedio

```python
x.mean()  # tensor(3.5)
```

**¿Qué hizo?** Calculó el promedio: (1+2+3+4+5+6)/6 = 21/6 = 3.5

**Nota:** Requiere que el tensor sea de tipo float. Si tienes enteros, usa `x.float().mean()`.

### .max() y .min() - Máximo y mínimo

```python
x.max()  # tensor(6) - el elemento más grande
x.min()  # tensor(1) - el elemento más pequeño
```

### .argmax() - Índice del máximo

```python
x.argmax()  # tensor(5)
```

**¿Qué significa?** El elemento más grande (el 6) está en la posición 5 si "aplanas" el tensor:
```
[[1, 2, 3],  →  [1, 2, 3, 4, 5, 6]
 [4, 5, 6]]       0  1  2  3  4  5  ← posiciones
                              ↑
                          posición 5 = donde está el 6
```

---

## Reducción por Dimensión (IMPORTANTE)

> "Muchas veces nos interesa que sea el máximo de cada una de las columnas o el promedio de cada una de las filas."

Puedes hacer la reducción solo en UNA dimensión, no en todo el tensor.

```python
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
```

Visualizado:
```
         Columnas
           0  1  2
         ┌────────┐
Fila 0 → │ 1  2  3 │
Fila 1 → │ 4  5  6 │
         └────────┘
```

### Reducir por dim=0 (sumar "hacia abajo", a lo largo de filas)

```python
x.sum(dim=0)  # tensor([5, 7, 9])
```

**¿Qué hizo?**
```
Columna 0: 1 + 4 = 5
Columna 1: 2 + 5 = 7
Columna 2: 3 + 6 = 9

Resultado: [5, 7, 9] (una suma por columna)
```

### Reducir por dim=1 (sumar "hacia la derecha", a lo largo de columnas)

```python
x.sum(dim=1)  # tensor([6, 15])
```

**¿Qué hizo?**
```
Fila 0: 1 + 2 + 3 = 6
Fila 1: 4 + 5 + 6 = 15

Resultado: [6, 15] (una suma por fila)
```

### Truco para recordarlo

> "A mí me cuesta un poco, no lo veo muy intuitivo."

**Forma de pensarlo:** El número de `dim` es la dimensión que **DESAPARECE**.
- `dim=0` → La dimensión 0 (filas) desaparece → queda 1 fila con valores por columna
- `dim=1` → La dimensión 1 (columnas) desaparece → queda 1 columna con valores por fila

### Ejemplos con otras funciones

```python
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])

x.mean(dim=0)  # tensor([2.5, 3.5, 4.5]) - promedio por columna
x.mean(dim=1)  # tensor([2., 5.])        - promedio por fila

x.max(dim=0)   # Devuelve (valores, índices):
               # values=tensor([4, 5, 6])  - máximo de cada columna
               # indices=tensor([1, 1, 1]) - en qué fila estaba

x.max(dim=1)   # values=tensor([3, 6])     - máximo de cada fila
               # indices=tensor([2, 2])    - en qué columna estaba
```

---

# RESHAPE Y MANIPULACIÓN DE FORMA

## ¿Qué es "reshape"?

**Reshape** significa cambiar la "forma" de un tensor sin cambiar sus datos. Es como reorganizar los mismos números en una estructura diferente.

Imagina que tienes 12 caramelos en una fila. Puedes reorganizarlos en:
- 1 fila de 12
- 2 filas de 6
- 3 filas de 4
- 4 filas de 3
- 6 filas de 2
- etc.

Son los mismos 12 caramelos, solo cambia cómo están organizados.

---

## reshape() - Cambiar Dimensiones

```python
x = torch.arange(9)  # tensor([0, 1, 2, 3, 4, 5, 6, 7, 8])
# Es un vector de 9 elementos

y = x.reshape(3, 3)
print(y)
# tensor([[0, 1, 2],
#         [3, 4, 5],
#         [6, 7, 8]])
# Ahora es una matriz de 3×3 = 9 elementos (los mismos!)
```

**¿Qué hizo?**
```
Vector original: [0, 1, 2, 3, 4, 5, 6, 7, 8]

Se reorganizó en 3 filas de 3:
Fila 0: [0, 1, 2]
Fila 1: [3, 4, 5]
Fila 2: [6, 7, 8]
```

**Restricción:** El número total de elementos debe ser el mismo.
- 9 elementos pueden ser 3×3, pero no 4×3 (eso serían 12).

---

## El Truco del -1 (MUY ÚTIL)

> "Algo bastante común y útil es utilizar este -1. Lo que está diciendo es: hacé de 3 filas y ni idea las columnas, calculalas vos."

El `-1` significa "calcula esta dimensión automáticamente".

```python
x = torch.arange(12)  # tensor([0, 1, 2, ..., 11]) - 12 elementos

x.reshape(3, -1)
# Resultado: tensor de 3×4
# PyTorch calculó: 12 elementos / 3 filas = 4 columnas
```

```python
x.reshape(-1, 4)
# Resultado: tensor de 3×4
# PyTorch calculó: 12 elementos / 4 columnas = 3 filas
```

```python
x.reshape(2, 2, -1)
# Resultado: tensor de 2×2×3
# PyTorch calculó: 12 elementos / (2×2) = 3 en la última dimensión
```

**¿Por qué es útil?**
Cuando no sabes exactamente el tamaño de los datos pero sabes que quieres cierta estructura.

---

## squeeze() - Eliminar Dimensiones de Tamaño 1

A veces los tensores tienen dimensiones "innecesarias" de tamaño 1. `squeeze()` las elimina.

```python
x = torch.zeros(1, 3, 1, 4)
print(x.shape)  # torch.Size([1, 3, 1, 4])
```

**Visualización:**
```
Forma original: [1, 3, 1, 4]
                 ↑     ↑
            Dimensiones de tamaño 1 (innecesarias)
```

```python
y = x.squeeze()
print(y.shape)  # torch.Size([3, 4])
```

**¿Qué hizo?** Eliminó TODAS las dimensiones de tamaño 1.

### squeeze() específico

```python
x = torch.zeros(1, 3, 1, 4)

x.squeeze(0)   # torch.Size([3, 1, 4]) - solo eliminó la dimensión 0
x.squeeze(2)   # torch.Size([1, 3, 4]) - solo eliminó la dimensión 2
```

---

## unsqueeze() - Agregar Dimensión de Tamaño 1

> "Todas las redes que vamos a ver toman los elementos en batches. ¿Qué pasa si terminamos de entrenar y queremos saber qué clasificación tiene esta imagen? Esta imagen no es un batch. Entonces tenemos que hacer un batch de una."

`unsqueeze()` es lo contrario de `squeeze()`: AGREGA una dimensión de tamaño 1.

### El problema que resuelve

Las redes neuronales esperan recibir datos en "lotes" (batches). Si tienes UNA sola imagen, necesitas "fingir" que es un lote de 1 imagen.

```python
imagen = torch.zeros(3, 224, 224)  # Una imagen: 3 canales, 224×224 píxeles
print(imagen.shape)  # torch.Size([3, 224, 224])

# La red espera shape [batch, canales, alto, ancho]
# Necesitamos agregar la dimensión del batch
```

### Usar unsqueeze()

```python
imagen = torch.zeros(3, 224, 224)  # shape: [3, 224, 224]

imagen_batch = imagen.unsqueeze(0)  # Agrega dimensión en posición 0
print(imagen_batch.shape)  # torch.Size([1, 3, 224, 224])
#                            ↑
#                     Nueva dimensión (batch de 1)
```

### unsqueeze() en diferentes posiciones

```python
x = torch.zeros(3, 4)  # shape: [3, 4]

x.unsqueeze(0)  # shape: [1, 3, 4] - dimensión agregada al INICIO
x.unsqueeze(1)  # shape: [3, 1, 4] - dimensión agregada en posición 1
x.unsqueeze(2)  # shape: [3, 4, 1] - dimensión agregada al FINAL
x.unsqueeze(-1) # shape: [3, 4, 1] - -1 también significa "al final"
```

---

# CONCATENAR Y APILAR TENSORES

## ¿Qué es concatenar vs apilar?

- **Concatenar (cat)**: Unir tensores "en línea", como pegar vagones de tren
- **Apilar (stack)**: Poner tensores uno encima de otro, como apilar hojas de papel

---

## torch.cat() - Concatenar (Une tensores existentes)

```python
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

resultado = torch.cat([x, y], dim=0)
print(resultado)  # tensor([1, 2, 3, 4, 5, 6])
```

**¿Qué hizo?**
```
x = [1, 2, 3]
y = [4, 5, 6]

cat = [1, 2, 3, 4, 5, 6]
       └──x──┘ └──y──┘
       Los pegó uno después del otro
```

**Nota:** Ambos tensores mantuvieron sus dimensiones (1D + 1D = 1D más largo).

### cat() con matrices

```python
a = torch.tensor([[1, 2],
                  [3, 4]])

b = torch.tensor([[5, 6],
                  [7, 8]])

# Concatenar por filas (dim=0) - "pegar abajo"
torch.cat([a, b], dim=0)
# tensor([[1, 2],
#         [3, 4],
#         [5, 6],
#         [7, 8]])
# shape: [4, 2] (4 filas, 2 columnas)

# Concatenar por columnas (dim=1) - "pegar a la derecha"
torch.cat([a, b], dim=1)
# tensor([[1, 2, 5, 6],
#         [3, 4, 7, 8]])
# shape: [2, 4] (2 filas, 4 columnas)
```

---

## torch.stack() - Apilar (Crea nueva dimensión)

```python
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

resultado = torch.stack([x, y], dim=0)
print(resultado)
# tensor([[1, 2, 3],
#         [4, 5, 6]])
print(resultado.shape)  # torch.Size([2, 3])
```

**¿Qué hizo?**
```
x = [1, 2, 3]  (shape: [3])
y = [4, 5, 6]  (shape: [3])

stack = [[1, 2, 3],   (shape: [2, 3])
         [4, 5, 6]]
         ↑
    Nueva dimensión (el "2" indica que hay 2 tensores apilados)
```

### La diferencia clave: cat vs stack

| | cat | stack |
|---|---|---|
| **Entrada** | 2 tensores [3] | 2 tensores [3] |
| **Salida** | 1 tensor [6] | 1 tensor [2, 3] |
| **Dimensiones** | Se mantienen | Se crea una nueva |

**Analogía:**
- `cat` = Pegar 2 trenes de 3 vagones → 1 tren de 6 vagones
- `stack` = Poner 2 trenes en pisos diferentes → Estacionamiento de 2 pisos con 3 vagones cada uno

---

## split() y chunk() - Dividir Tensores

Son lo inverso de concatenar: dividen UN tensor en VARIOS.

### torch.split() - Dividir por TAMAÑO de cada trozo

```python
x = torch.arange(6)  # tensor([0, 1, 2, 3, 4, 5])

partes = torch.split(x, 2)  # Cada trozo de tamaño 2
print(partes)
# (tensor([0, 1]), tensor([2, 3]), tensor([4, 5]))
#   trozo 1         trozo 2         trozo 3
#   tamaño 2        tamaño 2        tamaño 2
```

### torch.chunk() - Dividir en N CANTIDAD de trozos

```python
x = torch.arange(6)  # tensor([0, 1, 2, 3, 4, 5])

partes = torch.chunk(x, 3)  # Dividir en 3 partes
print(partes)
# (tensor([0, 1]), tensor([2, 3]), tensor([4, 5]))
#   parte 1         parte 2         parte 3
```

### Diferencia: split vs chunk

| | split(x, 2) | chunk(x, 3) |
|---|---|---|
| **Parámetro** | Tamaño de cada trozo | Cantidad de trozos |
| **Significado** | "Trozos de 2 elementos" | "Dividir en 3 partes" |

---

# COMPARACIONES

## ¿Cómo comparar tensores?

Puedes comparar tensores igual que comparas números en Python, pero el resultado es un tensor de `True`/`False`.

---

## Comparaciones elemento a elemento

```python
x = torch.tensor([1, 2, 3])
y = torch.tensor([3, 2, 1])
```

### Igualdad: `==`

```python
x == y  # tensor([False, True, False])
```

**¿Qué hizo?**
```
x = [1,     2,    3   ]
y = [3,     2,    1   ]
     ↓      ↓     ↓
    1==3?  2==2? 3==1?
    False  True  False
```

### Mayor que: `>`

```python
x > 2  # tensor([False, False, True])
```

**¿Qué hizo?**
```
x = [1,     2,     3   ]
     ↓      ↓      ↓
    1>2?   2>2?   3>2?
    False  False  True
```

### Otras comparaciones

```python
x = torch.tensor([1, 2, 3])
y = torch.tensor([3, 2, 1])

x == y    # tensor([False, True, False])  - iguales
x != y    # tensor([True, False, True])   - diferentes
x > y     # tensor([False, False, True])  - x mayor que y
x < y     # tensor([True, False, False])  - x menor que y
x >= y    # tensor([False, True, True])   - x mayor o igual
x <= y    # tensor([True, True, False])   - x menor o igual
```

---

## all() y any() - Verificar condiciones

### .all() - ¿TODOS cumplen la condición?

```python
x = torch.tensor([1, 2, 3, 4])

(x > 2).all()  # tensor(False)
```

**¿Qué hizo?**
```
x > 2 = [False, False, True, True]
         ↓
¿TODOS son True?
         ↓
        False (porque hay False)
```

```python
(x > 0).all()  # tensor(True)
```

**¿Por qué True?** Porque TODOS los elementos de x son > 0.

### .any() - ¿AL MENOS UNO cumple la condición?

```python
x = torch.tensor([1, 2, 3, 4])

(x > 2).any()  # tensor(True)
```

**¿Qué hizo?**
```
x > 2 = [False, False, True, True]
         ↓
¿AL MENOS UNO es True?
         ↓
        True (porque hay al menos un True)
```

```python
(x > 10).any()  # tensor(False)
```

**¿Por qué False?** Porque NINGÚN elemento es > 10.

### Resumen de all() vs any()

| Función | Pregunta que responde | Devuelve True si... |
|---------|----------------------|---------------------|
| `.all()` | "¿TODOS cumplen?" | Todos son True |
| `.any()` | "¿ALGUNO cumple?" | Al menos uno es True |

---

# GPU vs CPU: DEMOSTRACIÓN DE VELOCIDAD

## El Experimento de Clase

> "La primera operación va a multiplicar matricialmente estos dos tensores y lo va a hacer 5 veces y va a tomar rondas de 3. Y básicamente va a tomar el promedio."

```python
# Crear tensores grandes
x = torch.randn(5000, 5000)
y = torch.randn(5000, 5000)

# CPU
%timeit torch.matmul(x, y)
# ~52,000 milisegundos (52 segundos)

# GPU
x_gpu = x.to('cuda')
y_gpu = y.to('cuda')
%timeit torch.matmul(x_gpu, y_gpu)
# ~3,500 milisegundos (3.5 segundos)
```

## Resultado

> "En CPU tomó unos 52,000 milisegundos. Mientras que en MPS, que está optimizado para hacer este tipo de cálculos, tardó 3,500. Son 15 veces más rápido."

```
╔════════════════════════════════════════════════════════════════════════╗
║                    COMPARACIÓN DE VELOCIDAD                            ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   CPU:  52,000 ms ████████████████████████████████████████████████    ║
║                                                                        ║
║   GPU:   3,500 ms ███                                                  ║
║                                                                        ║
║   SPEEDUP: ~15x más rápido en GPU                                      ║
║                                                                        ║
║   "¿Ustedes qué prefieren, correr por una hora o correrlo por          ║
║    10 horas?"                                                          ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

---

# EJERCICIOS ASIGNADOS EN CLASE

> "Todos son de una o dos líneas de código."

## Lista de Ejercicios

| # | Ejercicio |
|---|-----------|
| 1 | Crear un tensor de 2×3 con valores aleatorios entre 0 y 1 |
| 2 | Crear un tensor de 3×3 con todos los elementos en valor 0 |
| 3 | Crear un vector de 10 elementos con valores aleatorios con media 5 y varianza 1 |
| 4 | Crear función que tome un tensor y devuelva el tensor elevado al cuadrado |
| 5 | Crear función que tome n, m y devuelva los primeros n×m números pares |
| 6 | Crear función que tome un tensor y devuelva el máximo y mínimo |
| 7 | Crear función que tome un tensor y devuelva la media y desviación estándar |
| 8 | Crear función que tome un vector y devuelva los elementos en orden inverso (usar `.flip()`) |
| 9 | Crear tensor n×m aleatorio, sumar las filas y multiplicar por una constante |
| 10 | Crear función que determine si dos tensores tienen elementos comunes en la misma posición |
| 11 | Crear función que devuelva los elementos únicos de un tensor (usar `torch.unique()`) |
| 12 | Crear función que retorne tensor con elementos comunes en la misma posición |

> "No los tienen que entregar. Es bueno como para consolidar algunas de las cosas."

---

# RECURSOS MENCIONADOS

## Libros

1. **"Dive into Deep Learning" (D2L)** - d2l.ai
   > "Es totalmente gratuita. Hay un montón de ejemplos. Pueden elegir si lo quieren hacer con PyTorch o TensorFlow."

2. **Pocket Reference (O'Reilly)**
   > "Si quieren un libro de bolsillo de lo que puede hacer PyTorch a bajo nivel, es una muy buena guía."

3. **Libro del YouTuber (premio para ganador de Kaggle)**
   > "Explica conceptos muy difíciles, como la atención."

## Páginas Web

- **Aulas** - Plataforma del curso con todas las notebooks
- **Google Colab** - Para ejecutar notebooks en la nube
- **Kaggle** - Competencia del obligatorio

---

# GLOSARIO DE FUNCIONES PYTORCH

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `torch.tensor()` | Crear tensor desde datos | `torch.tensor([1,2,3])` |
| `torch.zeros()` | Tensor de ceros | `torch.zeros(2, 3)` |
| `torch.ones()` | Tensor de unos | `torch.ones(2, 3)` |
| `torch.rand()` | Aleatorio uniforme [0,1) | `torch.rand(2, 3)` |
| `torch.randn()` | Aleatorio normal | `torch.randn(2, 3)` |
| `torch.arange()` | Secuencia | `torch.arange(0, 10, 2)` |
| `torch.full()` | Llenar con valor | `torch.full((3,3), 5)` |
| `torch.zeros_like()` | Ceros con misma forma | `torch.zeros_like(x)` |
| `.clone()` | Copiar tensor | `y = x.clone()` |
| `.to()` | Mover a dispositivo | `x.to('cuda')` |
| `.dtype` | Tipo de dato | `x.dtype` |
| `.shape` / `.size()` | Dimensiones | `x.size()` |
| `.ndim` | Número de dimensiones | `x.ndim` |
| `.device` | Dispositivo | `x.device` |
| `.item()` | Valor Python | `x[0].item()` |
| `.sum()` | Sumar | `x.sum()` |
| `.mean()` | Promedio | `x.mean()` |
| `.max()` / `.min()` | Máximo/mínimo | `x.max()` |
| `.argmax()` | Índice del máximo | `x.argmax()` |
| `.reshape()` | Cambiar forma | `x.reshape(3, 3)` |
| `.squeeze()` | Quitar dims de 1 | `x.squeeze()` |
| `.unsqueeze()` | Agregar dim de 1 | `x.unsqueeze(0)` |
| `torch.cat()` | Concatenar | `torch.cat([x, y])` |
| `torch.stack()` | Apilar | `torch.stack([x, y])` |
| `.flip()` | Invertir orden | `x.flip(0)` |
| `torch.unique()` | Elementos únicos | `torch.unique(x)` |
| `.add_()` | Suma in-place | `x.add_(5)` |

---

# RESUMEN EJECUTIVO

## Lo Más Importante de Esta Clase

1. **Tensores** son la unidad básica de PyTorch (matrices multidimensionales)
2. **GPU** acelera cálculos ~15x (usar `x.to('cuda')`)
3. **Broadcasting** es PREGUNTA DE PARCIAL (memorizar las 3 reglas)
4. **Cuidado** con igualar tensores: usar `.clone()` para copiar
5. **Indexing** crea vistas, no copias
6. **Evaluación**: 70 puntos para aprobar, entregas valen 80 puntos

## Para la Próxima Clase

> "La próxima clase veremos otra notebook. Hoy fue más que nada para familiarizarnos con PyTorch."

---

*Documento generado a partir del análisis exhaustivo de la transcripción de la clase del 20 de agosto de 2025.*
