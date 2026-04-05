# Clase 3 (03 de Septiembre 2025) - Taller de Deep Learning
## Dataset, DataLoader, Training Loop y Weights & Biases

---

# INFORMACIÓN DE LA CLASE

## Tema Principal
**Predicción de Precios de Casas en California** - Un problema de regresión

La clase se centra en cuatro conceptos fundamentales:

```
╔══════════════════════════════════════════════════════════════════════════╗
║                    LO QUE DEBES APRENDER HOY                             ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║   1. DATASET       →  Qué es y para qué sirve                           ║
║   2. DATALOADER    →  Qué es y para qué sirve                           ║
║   3. TRAINING LOOP →  Cómo estructurar el entrenamiento                 ║
║   4. WEIGHTS & BIASES → Herramienta para experimentación automática     ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

> "¿Qué deberían quedarse luego de esta notebook? Unos conceptos nuevos probablemente es el dataset, el dataloader... vamos a iterar un poquito en lo que ya hemos visto... para seguir entrenándonos en ciclos o loops de entrenamiento y de evaluación."

---

# FILOSOFÍA DE LA CLASE: CONSTRUIR UNA CAJA DE HERRAMIENTAS

> "Lo que vamos a ir haciendo nosotros a medida que vamos avanzando durante el semestre es ir como teniendo una cajita de herramientas... Acá vamos a hacer un training loop que debería servirnos para todos los problemas que nosotros vamos a enfrentarnos de acá a fin de año."

**Concepto clave**: El training loop que construirán en esta clase funcionará para:
- Clasificación o regresión
- Imágenes o texto
- Cualquier arquitectura de red neuronal

---

# EL PROBLEMA: PREDICCIÓN DE PRECIOS DE CASAS

## Dataset: California Housing Prices

**Fuente**: scikit-learn (`fetch_california_housing`)

### Características del Dataset

```
╔════════════════════════════════════════════════════════════════════════╗
║                    CALIFORNIA HOUSING DATASET                          ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   Total de datos: 20,640 bloques/cuadras                              ║
║                                                                        ║
║   Variables predictoras (8):                                          ║
║   ├── MedInc: Ingreso promedio de la cuadra                           ║
║   ├── HouseAge: Edad promedio de las casas                            ║
║   ├── AveRooms: Promedio de habitaciones por casa                     ║
║   ├── AveBedrms: Promedio de dormitorios por casa                     ║
║   ├── Population: Población de la cuadra                              ║
║   ├── AveOccup: Promedio de personas por casa                         ║
║   ├── Latitude: Ubicación geográfica (norte-sur)                      ║
║   └── Longitude: Ubicación geográfica (este-oeste)                    ║
║                                                                        ║
║   Variable objetivo (target):                                         ║
║   └── Precio promedio de las casas                                    ║
║       (expresado en cientos de miles de dólares)                      ║
║       Ejemplo: valor = 2 significa $200,000                           ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

### Concepto Importante: Datos por BLOQUE, no por Casa

> "De alguna manera como notar y decir esta casa, en esta casa ganan tanta plata, por un tema de privacidad, lo que hacen básicamente es toman el bloque para nosotros es la cuadra y hacen el promedio... no es que hay 20,640 casas, sino hay más bien 20,640 cuadras o bloques, ¿no?"

**¿Por qué promedios por bloque?**
- **Privacidad**: No se puede identificar una casa específica
- **Agregación**: Se toman todas las casas de una cuadra y se calcula el promedio de cada variable

---

# CONFIGURACIÓN DEL AMBIENTE

## Imports Necesarios

```python
import torch
from torch import nn
from torch.nn import functional as F
from torch import optim

# ¡LO NUEVO DE HOY!
from torch.utils.data import DataLoader, Dataset, random_split

from torchinfo import summary
from sklearn.datasets import fetch_california_housing
```

**¿Qué es cada import?**

- `torch` → Librería base de PyTorch
- `torch.nn` → Para definir capas de redes neuronales
- `torch.nn.functional` → Funciones útiles (activaciones, etc.)
- `DataLoader, Dataset, random_split` → **LO NUEVO** - Para manejar datos
- `torchinfo.summary` → Para ver resumen de la arquitectura del modelo

### Sobre torchinfo.summary

> "Esta es una forma sencilla de resumir la información de nuestra red, nos puede dar bastante información una vez que nosotros la definimos."

**¿Qué hace `summary`?**
- Muestra la arquitectura completa de tu red
- Indica cuántos parámetros tiene cada capa
- Muestra cuántos parámetros son entrenables
- Estima cuánta memoria VRAM necesitas

---

## Configuración de Device (GPU vs CPU)

```python
# Detectar qué aceleradora está disponible
if torch.cuda.is_available():
    device = 'cuda'
elif torch.backends.mps.is_available():
    device = 'mps'
else:
    device = 'cpu'

print(f"Usando: {device}")
```

> "Esto depende mucho de cada computadora. Si están corriendo en CUDA, si lo están corriendo en MacBook, si lo están corriendo con XPU... En mi caso, está usando MPS. Si ustedes están usando las notebooks de Colab o las notebook del laboratorio, deberían tener CUDA disponible."

---

## Número de Workers

```python
num_workers = 0  # ¡IMPORTANTE! Empezar con 0
```

### ¿Qué son los Workers?

> "Esto va a ser especialmente útil para cuando veamos los dataloader, que es uno de los parámetros... Yo les diría de que arranquen en cero acá, o sea, que no utilicen paralelización, sobre todo si están en Windows o en MacBook."

**Explicación simple**:
- Los workers son "ayudantes" que cargan datos en paralelo
- Cada worker usa un CPU diferente para cargar datos más rápido
- **Problema**: Depende del sistema operativo
  - Linux: Generalmente funciona bien
  - Mac: A veces funciona, a veces no
  - Windows: Problemas comunes

**Consejo práctico**:
```python
# Opción 1: Sin paralelización (siempre funciona)
num_workers = 0

# Opción 2: Con paralelización (si funciona en tu sistema)
num_workers = 4  # Probar con 4 CPUs
```

> "Pueden empezar teniendo un número cuatro... Si no le llega a andar, simplemente ponen cero y ya les debería ignorar ese problema."

---

## Batch Size

```python
batch_size = 1024  # Cuántos datos procesar a la vez
```

### ¿Qué es el Batch Size?

**Definición simple**: Es cuántos ejemplos (datos) se procesan juntos antes de actualizar los pesos de la red.

**Analogía**: Imagina que eres profesor corrigiendo exámenes:
- **Batch size = 1**: Corriges 1 examen, calculas el promedio de errores, ajustas tu forma de enseñar
- **Batch size = 32**: Corriges 32 exámenes, calculas el promedio de esos 32, ajustas
- **Batch size = 1000**: Corriges 1000 exámenes, calculas el promedio...

### Tamaño de Batch: ¿Grande o Pequeño?

> "Batches más grandes, lo que te va a pasar es de que es más estable. Si vos ves la gráfica de la loss, es más estable, pero los movimientos son como más brutos, mientras que los batches chicos van a ser muy ruidosos."

```
╔════════════════════════════════════════════════════════════════════════╗
║                    BATCH SIZE: GRANDE vs PEQUEÑO                       ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   BATCH GRANDE (ej: 4096):                                             ║
║   ✓ Más estable                                                        ║
║   ✓ Menos ruidoso                                                      ║
║   ✗ Movimientos grandes (puede pasar de largo del mínimo)             ║
║   ✗ Requiere más memoria                                               ║
║                                                                        ║
║   BATCH PEQUEÑO (ej: 32):                                              ║
║   ✓ Actualiza pesos más seguido                                        ║
║   ✓ Funciona como regularizador                                        ║
║   ✗ Muy ruidoso (gráfica de loss con muchos picos)                    ║
║   ✗ Menos eficiente (más iteraciones)                                  ║
║                                                                        ║
║   MINI-BATCH (ej: 128-512):                                            ║
║   ✓ Buen balance entre estabilidad y generalización                    ║
║   ✓ Es lo más común en la práctica                                     ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

**Regla práctica según Yann LeCun**:
> "El tamaño del batch está... varía, pero son múltiplos de potencia de dos: 32, 64, 128."

---

# PREPARACIÓN DE LOS DATOS

## Paso 1: Cargar el Dataset

```python
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
# data.data: Las variables predictoras (20,640 × 8)
# data.target: Los precios (20,640 valores)
```

---

## Paso 2: Análisis Exploratorio de Datos (EDA)

### Verificar Datos Nulos

> "Una de las cosas que deberíamos preguntarnos es, ¿qué pasa, por ejemplo, si hay datos vacíos?"

**En este caso particular**:
> "Es un caso hermoso, poco probable que pase en la vida real, pero no tenemos datos que no existan. O sea, literalmente de esas 20,640 no hay datos que no existan."

### ¿Qué es "sanitizar" los datos?

**Pregunta de estudiante**: "¿Cómo sanitizar?"

**Respuesta del profesor**:
> "Siempre hay que sanitizar los datos antes de empezar a hacer todo el análisis... tenés que saber con qué está trabajando... después puedes elegir distintas estrategias de cómo tratar tus datos... Si hay muchos nulos, capaz que podés llegar a borrarle la columna, pero capaz que no, porque depende cuánta correlación tenga con el target."

**Estrategias comunes para datos nulos**:
1. **Eliminar** la columna completa (si hay muchos nulos)
2. **Imputar con ceros** (llenar con 0)
3. **Imputar con el promedio** o la mediana
4. **Imputar con el valor más frecuente**

**Regla de oro**:
> "Lo que tenés que hacer es argumentar por qué tomas las decisiones que tomas... No es tomar una decisión a ciegas."

---

### Matriz de Correlación

**¿Qué es la correlación?**
- Mide qué tan relacionadas están dos variables
- Va de -1 a +1:
  - **+1**: Perfectamente relacionadas positivamente
  - **0**: No hay relación
  - **-1**: Perfectamente relacionadas negativamente

> "El ingreso promedio dentro de la casa parece estar relacionado con lo que efectivamente vale el valor de la casa. Parece que no es novedad."

**Curiosidad sobre latitud y longitud** (correlación de -0.92):

> **Marcos explica:** "Eso es porque California tiene una forma angulada. Entonces, mientras más latitud, menos longitud y a la reversa, porque va creciendo así como en una escalerita."

---

## Paso 3: Normalización de Datos

### ¿Por qué normalizar?

> "Los datos están en escalas bastante diferentes. Por ejemplo, la latitud y la longitud están en escala de 37, 122. Las poblaciones están en escalas de miles."

**Problema**:
```
Latitud:     37.0 - 42.0    (rango pequeño)
Longitud:   -125 - -114     (rango grande en negativo)
Población:   100 - 35000    (rango enorme)
Cuartos:     1.0 - 10.0     (rango pequeño)
```

### ¿Qué hace la normalización?

> "Una forma de acelerar o de alguna manera mejorar el entrenamiento es que todos los números estén dentro de la misma escala. Lo que vamos a hacer es... vamos a hacerlo con un promedio de cero y una desviación estándar de uno."

**Fórmula**:
```
valor_normalizado = (valor_original - media) / desviación_estándar
```

### Comentario de Marcos sobre la normalización

> "Se normaliza por dos cosas. Uno porque los datos todos están en diferentes escala, entonces los gradientes se ven afectados. Y la otra razón es llevar las entradas a una distribución conocida. Eso estabiliza el entrenamiento."

### ⚠️ IMPORTANTE: NO normalizar el target

> "La única que no normalizamos es la parte de targets. Eso no lo movemos."

**¿Por qué?**
- El target (precio) es lo que queremos predecir
- Queremos que la red aprenda a predecir precios REALES
- Si normalizamos, tendríamos que "desnormalizar" después

---

# DATASET: LA CLASE QUE CONTIENE TUS DATOS

## ¿Qué es un Dataset?

> "Los dataset de alguna manera es una clase... La responsabilidad principal es almacenar, conocer cuáles son los datos y aplicar transformaciones o de alguna manera prepararlos para nuestra red."

**Definición simple**:
Un Dataset es una clase de Python que:
1. **Guarda** tus datos (imágenes, números, texto, lo que sea)
2. **Sabe cuántos** datos tiene
3. **Puede darte** un dato específico cuando le pidas (por índice)
4. **Transforma** los datos al formato que tu red necesita (tensores)

---

## Responsabilidad del Dataset

```
╔════════════════════════════════════════════════════════════════════════╗
║                   RESPONSABILIDADES DEL DATASET                        ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   1. ALMACENAR los datos                                               ║
║      └─ Guardar en memoria (o saber dónde están en disco)             ║
║                                                                        ║
║   2. CONOCER cuántos datos hay                                         ║
║      └─ Método __len__() devuelve el total                            ║
║                                                                        ║
║   3. ENTREGAR un dato específico                                       ║
║      └─ Método __getitem__(índice) devuelve el dato en esa posición   ║
║                                                                        ║
║   4. TRANSFORMAR los datos                                             ║
║      └─ Convertir a tensores                                          ║
║      └─ Aplicar augmentación (próximas clases)                        ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

---

## Estructura de un Dataset: Los 3 Métodos Obligatorios

> "Los datasets van a tener que definir estos tres métodos. Son bien sencillitos."

```
1. __init__()    →  Constructor (recibe y guarda los datos)
2. __len__()     →  Devuelve cuántos datos hay
3. __getitem__() →  Devuelve un dato específico (ya transformado)
```

---

## Implementación del Dataset para California Housing

```python
class CaliforniaDataset(Dataset):
    def __init__(self, dataframe, target_column='target'):
        # Separar variables predictoras (X) del target (y)
        self.X = dataframe.drop(columns=[target_column]).values
        self.y = dataframe[target_column].values

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        # Obtener el dato en posición 'index'
        x = self.X[index]
        y = self.y[index]

        # Convertir a tensores de PyTorch
        x = torch.tensor(x, dtype=torch.float32)
        y = torch.tensor([y], dtype=torch.float32)  # ¡Nota los corchetes!

        return x, y
```

### Explicación Línea por Línea

#### Constructor (`__init__`)

```python
self.X = dataframe.drop(columns=[target_column]).values
```

**¿Qué hace?**
1. `dataframe.drop(columns=[target_column])` → Crea un NUEVO dataframe SIN la columna del target
2. `.values` → Convierte el dataframe a un array de NumPy
3. `self.X = ...` → Guarda ese array en el objeto

> "Para una forma más fácil de trabajar, lo paso a values. Es mucho más sencillo trabajar con una lista de numéricos."

#### `__len__`

```python
def __len__(self):
    return len(self.X)
```

Devuelve cuántos datos tienes en total. En este caso: 20,640.

#### `__getitem__` (El más importante)

```python
y = torch.tensor([y], dtype=torch.float32)  # [y] con corchetes
```

**¿Por qué `[y]` con corchetes?**

> "Este set de X de index te van a dar varios números. Por lo cual vos lo vas a dar como si fuera un array. Este set de Y pasa un solo número. Quieres que sea una lista con un solo número. Entonces para eso forzas con el paréntesis."

**Visualización**:
```python
# Sin corchetes:
y = 2.5  # Un número suelto → tensor de shape []

# Con corchetes:
y = [2.5]  # Una lista con 1 número → tensor de shape [1]
```

---

## ⚠️ IMPORTANTE: Los Tensores NO están en GPU todavía

> "Estos tensores están en memoria CPU, no están en GPU todavía. Se va a encargar de pasarlo a la GPU en su momento en el training loop."

**¿Por qué NO poner los datos en GPU desde el Dataset?**

> "¿Por qué? Porque nosotros vamos a trabajar con tantos datos que no van a caber en memoria. Vamos a trabajar por batches."

**Flujo correcto**:
```
1. Dataset crea tensores en CPU
2. DataLoader toma un batch (en CPU)
3. Training loop mueve el batch a GPU
4. Se procesa el batch en GPU
5. El batch se "descarta" (libera memoria GPU)
6. Se repite con el siguiente batch
```

---

# DIVIDIR LOS DATOS: random_split

## ¿Para qué dividir los datos?

Necesitamos **3 conjuntos** de datos:

```
╔════════════════════════════════════════════════════════════════════════╗
║                        DIVISIÓN DE DATOS                               ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   TRAINING (80%)  → Para entrenar el modelo                            ║
║   ├─ El modelo aprende de estos datos                                 ║
║   └─ Se calculan gradientes y se actualizan pesos                     ║
║                                                                        ║
║   VALIDATION (10%) → Para ajustar hiperparámetros                      ║
║   ├─ Evaluar durante el entrenamiento                                 ║
║   └─ Detectar overfitting                                             ║
║                                                                        ║
║   TEST (10%)      → Para evaluación final                              ║
║   ├─ NO se usa durante entrenamiento                                  ║
║   └─ Evaluar el modelo final                                          ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

---

## Usar `random_split`

```python
from torch.utils.data import random_split

# Total de datos
total_size = len(dataset)  # 20640

# Calcular tamaños
train_size = int(0.8 * total_size)  # 16512
val_size = int(0.1 * total_size)    # 2064
test_size = total_size - train_size - val_size  # El resto

# Dividir el dataset
train_dataset, val_dataset, test_dataset = random_split(
    dataset,
    [train_size, val_size, test_size]
)
```

**¿Por qué `test_size` se calcula como "el resto"?**

> "El problema por un tema de casteos, si esto todos quedan un 0.3 y sumados me dan un dato más, se me va a romper. Entonces, una forma fácil de evitar eso es, bueno, lo que me queda del resto."

### ⚠️ Importante: Sin Reposición

**Pregunta de estudiante**: "El random hace sin reposición, ¿no?"

**Respuesta**:
> "La reposición te podría llegar a contaminar el dataset de entrenamiento y hacer que aprenda cosas que no debería haber, y entonces validación pierde el sentido."

**Explicación**: `random_split()` es **sin reposición** → cada dato va a UNO SOLO de los 3 conjuntos.

---

# DATALOADER: EL REPARTIDOR DE DATOS

## ¿Qué es un DataLoader?

> "El dataloader es copier. El que reparte cartas. Toma el dataset básicamente y tiene alguna estrategia para darle los datos a la red."

**Analogía**:
- El **Dataset** es el mazo completo de cartas (contiene todos los datos)
- El **DataLoader** es el crupier que reparte las cartas (entrega los datos en batches)

---

## Responsabilidad del DataLoader

```
╔════════════════════════════════════════════════════════════════════════╗
║                  RESPONSABILIDADES DEL DATALOADER                      ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   1. TOMAR datos del Dataset                                           ║
║      └─ Pide datos usando índices                                     ║
║                                                                        ║
║   2. AGRUPAR en batches                                                ║
║      └─ Junta batch_size datos en un solo tensor                      ║
║                                                                        ║
║   3. MEZCLAR (shuffle) si se le pide                                   ║
║      └─ Randomiza el orden de los datos                               ║
║                                                                        ║
║   4. PARALELIZAR la carga (con num_workers)                            ║
║      └─ Usa varios CPUs para cargar datos más rápido                  ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

---

## Parámetros Importantes del DataLoader

```python
train_loader = DataLoader(
    dataset=train_dataset,
    batch_size=1024,
    shuffle=True,
    num_workers=num_workers
)
```

### shuffle - ¿Cuándo mezclar?

> "En el training se hace shuffle y lo que es validaciones y test no. No vale la pena. Siempre hay un shuffle que hay una computación de fondo."

```
╔════════════════════════════════════════════════════════════════════════╗
║                           REGLA DE SHUFFLE                              ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   TRAINING    → shuffle = True  ✅                                     ║
║   VALIDATION  → shuffle = False ✅                                     ║
║   TEST        → shuffle = False ✅                                     ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

**¿Por qué shuffle en training?**

> **Marcos explica:** "Si vos siempre estás tomando los mismos datos de alguna manera estás yendo siempre a la misma dirección. Imagínense de esta clase, solo sacamos un batch de dos y agarramos a José y a mí, tipo, todos son taiwaneses. Y aprende que todos son taiwaneses, pero en realidad está overfiteando a ese subset de datos."

---

### ¿Cómo Funciona el Shuffle Internamente?

> "En realidad vos cuando shuffleas, los algoritmos lo que hacen es: vos tenés los índices 0, 1, 2, 3... hasta n-1. Efectivamente haces permutaciones."

**Visualización:**
```
DATOS ORIGINALES:
Índices:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Datos:    [A, B, C, D, E, F, G, H, I, J]

DESPUÉS DEL SHUFFLE:
Índices:  [7, 2, 9, 0, 5, 1, 8, 3, 6, 4]

ACCESO SECUENCIAL POST-SHUFFLE:
Batch 1 (3 datos):  [H, C, J]
Batch 2 (3 datos):  [A, F, B]
...
```

**Lo importante:**
> "El shuffle me lo hizo random, pero yo después tomo de forma secuencial."

---

## Crear los DataLoaders

```python
# Training DataLoader
train_loader = DataLoader(
    dataset=train_dataset,
    batch_size=batch_size,
    shuffle=True,            # ✓ Mezclar para entrenar
    num_workers=num_workers
)

# Validation DataLoader
val_loader = DataLoader(
    dataset=val_dataset,
    batch_size=batch_size,
    shuffle=False,           # ✗ NO mezclar
    num_workers=num_workers
)

# Test DataLoader
test_loader = DataLoader(
    dataset=test_dataset,
    batch_size=batch_size,
    shuffle=False,           # ✗ NO mezclar
    num_workers=num_workers
)
```

---

## ⚠️ Último Batch Incompleto

> "Nosotros tenemos 16,000 datos. Todos los primeros 16 asumo son de 1024, mientras que el último batch es de 128."

**Problema**:
```
Total de datos: 16512
Batch size: 1024

Batches 1-16: 1024 datos cada uno (16 × 1024 = 16,384)
Batch 17: 128 datos (el resto)
```

**Opción: drop_last**
```python
train_loader = DataLoader(
    ...,
    drop_last=True  # Descartar el último batch si está incompleto
)
```

---

# ARQUITECTURA DEL MODELO

## Crear una Red Neuronal Simple

```python
class HousingModel(nn.Module):
    def __init__(self, input_size=8, hidden_size=64, output_size=1):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
```

**Arquitectura**:
```
Input (8) → Linear → ReLU → Linear → Output (1)
              ↓                ↓
          64 neuronas      1 neurona
```

---

## Usar torchinfo.summary

```python
from torchinfo import summary

model = HousingModel(input_size=8, hidden_size=64)
summary(model, input_size=(batch_size, 8))
```

**¿Qué muestra?**
- Arquitectura completa
- Forma de entrada/salida de cada capa
- **Parámetros totales** (cuántos pesos tiene el modelo)
- **Tamaño estimado en memoria**

> "Si ustedes tienen imágenes que son suficientemente pesadas y ustedes le ponen el batch y el tamaño de las imágenes, pueden estimar cuántos megabytes o gigas necesitan en su VRAM."

---

# TRAINING LOOP: EL CICLO DE ENTRENAMIENTO

## Estructura General

```
╔════════════════════════════════════════════════════════════════════════╗
║                      ESTRUCTURA DEL TRAINING LOOP                      ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   Para cada ÉPOCA:                                                     ║
║   │                                                                    ║
║   ├─ Poner modelo en modo train                                       ║
║   │                                                                    ║
║   └─ Para cada BATCH en el DataLoader:                                ║
║       │                                                                ║
║       ├─ 1. Mover datos a GPU                                         ║
║       ├─ 2. Forward pass (calcular predicción)                        ║
║       ├─ 3. Calcular loss                                             ║
║       ├─ 4. optimizer.zero_grad() (limpiar gradientes)                ║
║       ├─ 5. loss.backward() (calcular gradientes)                     ║
║       └─ 6. optimizer.step() (actualizar pesos)                       ║
║                                                                        ║
║   Evaluar en validation                                               ║
║   Loguear resultados                                                  ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

---

## Implementación del Training Loop

```python
def train(model, optimizer, criterion, train_loader, val_loader,
          epochs, device, log_function=None, log_every=1):

    epoch_train_losses = []
    epoch_val_losses = []

    for epoch in range(epochs):
        # 1. Poner modelo en modo entrenamiento
        model.train()
        train_loss = 0.0

        # 2. Iterar sobre batches
        for X, y in train_loader:
            # 2.1 Mover datos a GPU
            X = X.to(device)
            y = y.to(device)

            # 2.2 Forward pass
            output = model(X)

            # 2.3 Calcular loss
            loss = criterion(output, y)

            # 2.4 Limpiar gradientes
            optimizer.zero_grad()

            # 2.5 Backward pass
            loss.backward()

            # 2.6 Actualizar pesos
            optimizer.step()

            # 2.7 Acumular loss
            train_loss += loss.item()

        # 3. Calcular loss promedio
        avg_train_loss = train_loss / len(train_loader)
        epoch_train_losses.append(avg_train_loss)

        # 4. Evaluar en validation
        val_loss = evaluate(model, criterion, val_loader, device)
        epoch_val_losses.append(val_loss)

        # 5. Loguear si corresponde
        if log_function and (epoch + 1) % log_every == 0:
            log_function(epoch + 1, avg_train_loss, val_loss)

    return epoch_train_losses, epoch_val_losses
```

---

## Explicación Detallada

### `model.train()`

> "Hoy en día con las redes que nosotros estamos haciendo no va a haber ninguna diferencia. Pero es una buena costumbre."

**Capas que se comportan diferente** (próximas clases):
- **Dropout**: Se activa en training, se desactiva en evaluation
- **BatchNorm**: Actualiza estadísticas en training, usa estadísticas fijas en evaluation

### Mover datos a GPU

```python
X = X.to(device)
y = y.to(device)
```

> "Tanto si vas a operar dos tensores como simplemente sumarlos, como directamente tomar un tensor que son mis datos y pasarlo por mi red, tienen que estar dentro del mismo dispositivo."

### Calcular loss

```python
loss = criterion(output, y)
```

**Sobre el orden de los parámetros**:

> "Vamos a primero lo que nosotros obtenemos y segundo el que espera. Exactamente."

```python
loss = criterion(predicción, valor_real)  # ✓ Correcto
```

### optimizer.zero_grad()

> "Los gradientes se acumulan. Si no los limpias, los gradientes del batch anterior se suman al nuevo."

### loss.backward()

> "El backward actualiza los gradientes. Recuerden que esta loss tiene detrás el grafo computacional."

### optimizer.step()

> "El optimizer.step() efectivamente cambia nuestros pesos."

### loss.item()

> "Este loss.item() te permite llamar ese número tensor y volverlo a Python."

Convierte el tensor de loss (que vive en GPU) a un número de Python normal.

### Promediar loss

```python
avg_train_loss = train_loss / len(train_loader)
```

> "Yo acá por cada batch estoy sumando una loss. ¿Cómo de alguna manera yo lo reduzco a lo que es de una sola época?"

---

# EVALUATION LOOP: EL CICLO DE EVALUACIÓN

## Implementación

```python
def evaluate(model, criterion, dataloader, device):
    model.eval()  # Poner modelo en modo evaluación
    total_loss = 0.0

    with torch.no_grad():  # NO calcular gradientes
        for X, y in dataloader:
            X = X.to(device)
            y = y.to(device)

            output = model(X)
            loss = criterion(output, y)

            total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    return avg_loss
```

---

## Diferencias con el Training Loop

### 1. `model.eval()`

> "Nosotros no estamos entrenando. Por lo cual no deberíamos cambiar nuestros pesos."

### 2. `torch.no_grad()`

> "Esto es necesario... anda más rápido porque directamente no va a calcular los gradientes."

```
╔════════════════════════════════════════════════════════════════════════╗
║                    TRAINING vs EVALUATION                              ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   TRAINING:                                                            ║
║   ├─ model.train()                                                     ║
║   ├─ CON gradientes                                                    ║
║   ├─ Actualiza pesos                                                   ║
║   └─ MÁS LENTO (calcula grafo computacional)                           ║
║                                                                        ║
║   EVALUATION:                                                          ║
║   ├─ model.eval()                                                      ║
║   ├─ SIN gradientes (torch.no_grad())                                  ║
║   ├─ NO actualiza pesos                                                ║
║   └─ MÁS RÁPIDO (no calcula grafo)                                     ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

### 3. NO hay optimizer

En evaluación solo MEDIMOS, no ENTRENAMOS:
- ❌ `optimizer.zero_grad()`
- ❌ `loss.backward()`
- ❌ `optimizer.step()`

---

# WEIGHTS & BIASES (W&B): EXPERIMENTACIÓN AUTOMATIZADA

## El Problema que Resuelve

> "¿Qué pasa? Dependiendo de la experiencia que tengan o no, probablemente ustedes les gustaría probar diferentes cosas... vienen acá, dicen 'yo acá con 64 neuronas voy a probar con 128'. Lo corro, espero 10 minutos, veo el resultado..."

**El ciclo tedioso de experimentación manual**:
```
1. Cambiar hiperparámetro en el código
2. Correr entrenamiento (10 min - 10 horas)
3. Anotar resultado en Excel/libreta
4. Cambiar otro hiperparámetro
5. Esperar otra vez...
6. Repetir 100 veces...
```

---

## ¿Qué es Weights & Biases?

> "Estaría bueno que haya una herramienta que me permita hacer combinaciones diferentes, le vaya notando cómo le fue a cada uno y yo al final de todo elijo a cuál le fue mejor."

```
╔════════════════════════════════════════════════════════════════════════╗
║                   ¿QUÉ HACE WEIGHTS & BIASES?                          ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║   1. AUTOMATIZAR experimentos                                          ║
║      └─ Define rangos de hiperparámetros                              ║
║      └─ Corre múltiples configuraciones automáticamente               ║
║                                                                        ║
║   2. LOGUEAR resultados                                                ║
║      └─ Guarda losses, métricas, gráficos en la nube                  ║
║      └─ Visualización en tiempo real                                  ║
║                                                                        ║
║   3. COMPARAR experimentos                                             ║
║      └─ Ver qué configuración funcionó mejor                          ║
║      └─ Gráficos comparativos                                         ║
║                                                                        ║
║   4. GUARDAR modelos                                                   ║
║      └─ Guarda los pesos del mejor modelo                             ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

---

## Configurar un Sweep (Barrido de Hiperparámetros)

### ¿Qué es un Sweep?

**Sweep** = Conjunto de experimentos con diferentes configuraciones

### Definir Configuración del Sweep

```python
sweep_config = {
    'method': 'random',  # Cómo muestrear: random, grid, bayes
    'metric': {
        'name': 'val_loss',
        'goal': 'minimize'
    },
    'parameters': {
        'learning_rate': {
            'min': 0.001,
            'max': 0.1
        },
        'optimizer': {
            'values': ['adam', 'sgd']
        },
        'batch_size': {
            'values': [32, 256, 1024, 4096]
        }
    }
}
```

---

### Explicación de la Configuración

#### `method`

**Opciones**:
- `'random'` → Muestreo aleatorio
- `'grid'` → Prueba TODAS las combinaciones (exhaustivo, puede ser muy lento)
- `'bayes'` → Optimización bayesiana (aprende de experimentos anteriores)

> "El creador lo que dice es, si tenés pocos experimentos, tipo cinco, usa bayesiano, pero cuando vos tenés suficientes experimentos, el randómico supera el bayesiano."

#### `metric`

```python
'metric': {
    'name': 'val_loss',
    'goal': 'minimize'
}
```

**IMPORTANTE:**

> "Este atributo es el que tiene que coincidir con lo que logueas. Muy importante porque si no, no sabe qué estás logueando."

El nombre `'val_loss'` **DEBE SER IGUAL** al nombre que usas en `wandb.log()`.

#### `parameters`

**Parámetro continuo (rango)**:
```python
'learning_rate': {
    'min': 0.001,
    'max': 0.1
}
```
W&B elegirá valores aleatorios entre 0.001 y 0.1.

**Parámetro discreto (opciones)**:
```python
'optimizer': {
    'values': ['adam', 'sgd']
}
```
W&B elegirá 'adam' O 'sgd'.

---

## La Función de Entrenamiento para W&B

```python
def run():
    # 1. Inicializar el run
    wandb.init()

    # 2. Obtener configuración para este experimento
    config = wandb.config
    learning_rate = config.learning_rate
    optimizer_name = config.optimizer
    batch_size = config.batch_size

    # 3. Crear DataLoaders con ese batch_size
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    # 4. Crear modelo
    model = HousingModel().to(device)

    # 5. Crear optimizador según la configuración
    if optimizer_name == 'adam':
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    else:
        optimizer = optim.SGD(model.parameters(), lr=learning_rate)

    # 6. Función de logging para wandb
    def wandb_log(epoch, train_loss, val_loss):
        wandb.log({
            'epoch': epoch,
            'train_loss': train_loss,
            'val_loss': val_loss  # ¡Debe coincidir con 'metric.name'!
        })

    # 7. Entrenar
    train(model, optimizer, criterion, train_loader, val_loader,
          epochs=100, device=device, log_function=wandb_log, log_every=1)

    # 8. Guardar modelo
    torch.save(model.state_dict(), 'model.pth')
    wandb.save('model.pth')
```

---

## Correr el Sweep

```python
# Crear el sweep
sweep_id = wandb.sweep(sweep_config, project="mi-proyecto")

# Correr experimentos
wandb.agent(sweep_id, function=run, count=10)
```

**¿Qué hace?**
1. Pide una configuración a W&B
2. Llama a `run()` con esa configuración
3. Entrena el modelo y loguea resultados
4. Repite hasta completar `count` experimentos

---

## Estrategia de Experimentación Iterativa

> "Vos ves de los 10 experimentos que el que tiene menos loss es el que tiene hiperparámetro tanto. Entonces vas al código y definís un nuevo experimento donde vos habías dicho que el learning rate iba entre 0.1 y 1. Ahora lo vas a hacer entre 0.5 y 1 porque se acercó."

**Proceso iterativo**:
```
Sweep 1: Exploración amplia
  LR: 0.001 - 0.1
  Mejor resultado: LR = 0.03

Sweep 2: Refinar alrededor del mejor
  LR: 0.01 - 0.05
  Mejor resultado: LR = 0.025
```

---

## Experimentación Colaborativa

> "Pueden haber corriendo tres al mismo tiempo y está graficando en línea los tres experimentos... vos imaginas mi máquina acá está corriendo todo el código y lo único que hace es loguear."

**Ventaja**:
- Tú corres experimentos 1, 2, 3 en tu máquina
- Tu compañero corre experimentos 4, 5, 6 en su máquina
- Todos ven los resultados en la MISMA página de W&B

---

# CONSEJOS Y MEJORES PRÁCTICAS

## Sobre Experimentación

**Pregunta de estudiante**: "¿Qué recomienda para final, ir moviendo de a un parámetro o de varios?"

**Respuesta**:

> "Una sola variable. ¿Sabes que si cambias varios y tenés una mejor? No sabes cuál te hizo la diferencia."

**Pero también:**

> "El problema es que hay algunas variables que mejoran si las cambias juntos. Entonces es un poco de prueba y error."

---

# GLOSARIO DE TÉRMINOS NUEVOS

| Término | Definición |
|---------|------------|
| **Dataset** | Clase que almacena datos y los convierte a tensores |
| **DataLoader** | Clase que agrupa datos en batches y los entrega iterativamente |
| **Batch** | Grupo de datos procesados juntos (ej: 1024 datos) |
| **Shuffle** | Mezclar el orden de los datos aleatoriamente |
| **Época (Epoch)** | Una pasada completa por todos los datos de training |
| **Sanitizar** | Limpiar datos (eliminar/corregir nulos, errores) |
| **Normalizar** | Escalar datos para que tengan media 0 y desviación estándar 1 |
| **Sweep** | Barrido automático de hiperparámetros |
| **W&B / wandb** | Weights & Biases (herramienta de experimentación) |

---

# GLOSARIO DE FUNCIONES NUEVAS

| Función/Método | Descripción | Ejemplo |
|----------------|-------------|---------|
| `Dataset.__init__()` | Constructor del dataset | `def __init__(self, data)` |
| `Dataset.__len__()` | Devuelve cantidad de datos | `return len(self.X)` |
| `Dataset.__getitem__(idx)` | Devuelve dato en posición idx | `return self.X[idx], self.y[idx]` |
| `random_split()` | Divide dataset en partes | `train, val = random_split(dataset, [0.8, 0.2])` |
| `DataLoader()` | Crea dataloader | `DataLoader(dataset, batch_size=32)` |
| `model.train()` | Pone modelo en modo entrenamiento | `model.train()` |
| `model.eval()` | Pone modelo en modo evaluación | `model.eval()` |
| `torch.no_grad()` | Context manager que desactiva gradientes | `with torch.no_grad(): ...` |
| `optimizer.zero_grad()` | Limpia gradientes anteriores | `optimizer.zero_grad()` |
| `loss.backward()` | Calcula gradientes (backpropagation) | `loss.backward()` |
| `optimizer.step()` | Actualiza pesos con los gradientes | `optimizer.step()` |
| `tensor.item()` | Extrae valor numérico de tensor escalar | `loss.item()` |
| `wandb.init()` | Inicializa experimento de W&B | `wandb.init(project="name")` |
| `wandb.log()` | Loguea métricas a W&B | `wandb.log({'loss': 0.5})` |
| `wandb.sweep()` | Crea sweep en W&B | `sweep_id = wandb.sweep(config)` |
| `wandb.agent()` | Ejecuta experimentos del sweep | `wandb.agent(sweep_id, run)` |

---

# RESUMEN EJECUTIVO

## Lo Más Importante de Esta Clase

1. **Dataset** = Almacena datos y los transforma a tensores
   - Implementar `__init__`, `__len__`, `__getitem__`

2. **DataLoader** = Agrupa datos en batches y los mezcla
   - `shuffle=True` en training, `False` en validation/test

3. **Training Loop** = Ciclo que entrena el modelo
   - forward → loss → backward → step
   - `model.train()` antes de entrenar

4. **Evaluation Loop** = Ciclo que evalúa el modelo
   - Solo forward y calcular loss
   - `model.eval()` y `torch.no_grad()`

5. **Weights & Biases** = Automatiza experimentación
   - Define rangos de hiperparámetros
   - Corre múltiples experimentos
   - Elige la mejor configuración

---

## Para la Próxima Clase

> "Este training loop va a ir evolucionando a medida que vamos pasando por todo el semestre. Vamos a ir agregando diferentes trucos."

---

*Documento generado a partir del análisis exhaustivo (3 pasadas por 3 agentes) de la transcripción de la clase del 03 de septiembre de 2025.*
