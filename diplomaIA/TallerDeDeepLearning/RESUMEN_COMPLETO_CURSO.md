# TALLER DE DEEP LEARNING - RESUMEN COMPLETO DEL CURSO
## Universidad ORT Uruguay - Segundo Semestre 2025
## Análisis Exhaustivo de las 12 Clases

---

# RESUMEN EJECUTIVO

Este es un curso **100% práctico** de Deep Learning dictado por el profesor **Joaquín Viña (Joa)** con apoyo de **Marcos** y **Ari**. El curso no tiene presentaciones teóricas tradicionales - todo se trabaja directamente en código con Jupyter Notebooks usando **PyTorch**.

## Estructura del Curso

| Componente | Porcentaje | Descripción |
|------------|------------|-------------|
| Laboratorio 1 | 15% | Clasificación de imágenes (Imagenette) |
| Laboratorio 2 | 15% | Clasificación de secuencias (ECG/ritmos cardíacos) |
| Parcial Escrito | 20% | Preguntas conceptuales + defensa del obligatorio |
| Obligatorio Final | 50% | U-Net para segmentación + competencia Kaggle |

**Aprobación**: 70 puntos. El parcial busca excelencia (90+).

---

# CLASE 1 (20 de Agosto 2025)
## FUNDAMENTOS DE PYTORCH Y TENSORES

### 1.1 ¿Qué es un Tensor?

Un **tensor** es la estructura de datos fundamental en PyTorch. Es una matriz multidimensional que puede tener desde 0 hasta N dimensiones:

- **0 dimensiones**: Escalar (un solo número)
- **1 dimensión**: Vector `[1, 2, 3]`
- **2 dimensiones**: Matriz `[[1,2], [3,4]]`
- **3+ dimensiones**: Tensor de orden superior

**Diferencia con NumPy**:
- NumPy trabaja SOLO en CPU
- PyTorch puede trabajar en **GPU** (~15x más rápido)
- Los tensores pueden calcular **gradientes automáticamente** (autograd)

### 1.2 Tipos de Datos en Tensores

| Tipo | Uso | Ejemplo |
|------|-----|---------|
| `uint8` | Imágenes RGB (0-255) | Píxeles de fotos |
| `int32/int64` | Etiquetas, índices | Clases de clasificación |
| `float32` | **Pesos de redes** (MÁS USADO) | Parámetros del modelo |
| `float16` | Modelos cuantizados | Ahorro de memoria |
| `bool` | Máscaras booleanas | Segmentación |

**Importante**: Todos los elementos de un tensor DEBEN ser del mismo tipo.

### 1.3 Creación de Tensores

```python
import torch

# Desde listas
x = torch.tensor([1, 2, 3])

# Desde NumPy
x = torch.from_numpy(numpy_array)

# Tensores especiales
torch.zeros(2, 3)       # Matriz 2x3 de ceros
torch.ones(2, 3)        # Matriz 2x3 de unos
torch.rand(2, 3)        # Aleatorios uniformes [0,1)
torch.randn(2, 3)       # Distribución normal (media=0, std=1)
torch.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
torch.full((3, 3), 5)   # Llenar con valor específico

# Funciones "like" (muy útiles)
torch.zeros_like(x)     # Mismo shape que x, lleno de ceros
torch.ones_like(x)      # Mismo shape que x, lleno de unos
```

### 1.4 Propiedades de Tensores

```python
x = torch.randn(2, 3, 4)

x.dtype          # Tipo de dato (float32, int64, etc.)
x.shape          # Dimensiones: torch.Size([2, 3, 4])
x.size()         # Igual que shape pero como método
x.size(0)        # Tamaño de dimensión específica: 2
x.ndim           # Número de dimensiones: 3
x.device         # Dónde está: 'cpu', 'cuda:0', 'mps'
x.requires_grad  # Si calcula gradientes
```

### 1.5 Device: CPU vs GPU

```python
# Verificar disponibilidad
if torch.cuda.is_available():
    device = 'cuda'
elif torch.backends.mps.is_available():
    device = 'mps'  # Mac con Apple Silicon
else:
    device = 'cpu'

# Crear tensor en dispositivo específico
x = torch.tensor([1, 2, 3], device=device)

# Mover tensor existente
x = x.to(device)
x = x.cuda()  # Atajo para GPU
x = x.cpu()   # Atajo para CPU
```

**Advertencia**: Mover tensores entre CPU y GPU es costoso. Evitar hacerlo frecuentemente durante entrenamiento.

### 1.6 Broadcasting (PREGUNTA DE PARCIAL)

Reglas para operar tensores de diferentes shapes:

1. Leer dimensiones de **derecha a izquierda**
2. Dos dimensiones son compatibles si:
   - Son **iguales**, O
   - Una de ellas es **1**, O
   - Una de ellas **no existe**

**Ejemplos**:
```python
# Compatible
x.shape = (5, 3, 4, 1)
y.shape = (    3, 1, 1)
# De derecha a izquierda: 1==1 ✓, 4 vs 1 ✓, 3==3 ✓, 5 vs nada ✓

# NO compatible
a.shape = (3, 4, 2)
b.shape = (3, 4, 3)
# 2 != 3 y ninguno es 1 → ERROR
```

### 1.7 Indexing y Slicing

```python
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

x[0]         # Primera fila: [1, 2, 3]
x[-1]        # Última fila: [7, 8, 9]
x[1:3]       # Filas 1 y 2
x[:, 0]      # Primera columna: [1, 4, 7]
x[0, 0]      # Elemento específico: 1
x[0, 0].item()  # Obtener valor Python nativo
```

**Cuidado**: El slicing crea **vistas**, no copias. Modificar la vista modifica el original. Usar `.clone()` para copiar.

### 1.8 Máscaras Booleanas

```python
x = torch.tensor([1, 2, 3, 4, 5])

# Crear máscara
mask = x > 3  # tensor([False, False, False, True, True])

# Aplicar máscara
x[mask]  # tensor([4, 5])

# Operaciones con máscaras
x[x > 3].sum()  # Suma de elementos > 3
```

**Aplicación práctica**: En segmentación, las máscaras marcan píxeles de "persona" vs "fondo".

### 1.9 Operaciones de Reducción

```python
x = torch.rand(3, 4)

x.sum()        # Suma todos los elementos
x.mean()       # Promedio
x.max()        # Máximo
x.min()        # Mínimo
x.argmax()     # Índice del máximo

# Por dimensión
x.sum(dim=0)   # Suma "a través" de filas → resultado por columnas
x.sum(dim=1)   # Suma "a través" de columnas → resultado por filas
```

### 1.10 Reshape y Squeeze

```python
x = torch.arange(12)  # [0, 1, 2, ..., 11]

x.view(3, 4)          # Matriz 3x4
x.view(-1, 4)         # -1 se calcula automáticamente: 3x4

# Squeeze: eliminar dimensiones de tamaño 1
y = torch.rand(1, 3, 1, 4)
y.squeeze()           # Shape: (3, 4)

# Unsqueeze: agregar dimensión
z = torch.rand(3, 4)
z.unsqueeze(0)        # Shape: (1, 3, 4) - útil para batches
```

### 1.11 Concatenar Tensores

```python
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

# Concatenar (mantiene dimensiones)
torch.cat([x, y], dim=0)  # [1, 2, 3, 4, 5, 6]

# Stack (crea nueva dimensión)
torch.stack([x, y], dim=0)  # [[1,2,3], [4,5,6]]
```

### 1.12 Demostración CPU vs GPU

```python
import time

x = torch.rand(5000, 5000)
y = torch.rand(5000, 5000)

# CPU
start = time.time()
z_cpu = torch.matmul(x, y)
print(f"CPU: {time.time() - start:.2f}s")  # ~52 segundos

# GPU
x_gpu = x.cuda()
y_gpu = y.cuda()
start = time.time()
z_gpu = torch.matmul(x_gpu, y_gpu)
torch.cuda.synchronize()  # Esperar a que termine
print(f"GPU: {time.time() - start:.2f}s")  # ~3.5 segundos
```

**Resultado**: GPU es ~15x más rápida para operaciones matriciales grandes.

---

# CLASE 2 (27 de Agosto 2025)
## PERCEPTRÓN Y REDES MULTICAPA (MLP)

### 2.1 El Perceptrón

El **perceptrón** es la unidad más básica de una red neuronal:

**Componentes**:
1. **Entradas (X)**: Vector de features `[x₁, x₂, ..., xₙ]`
2. **Pesos (W)**: Se aprenden durante entrenamiento `[w₁, w₂, ..., wₙ]`
3. **Bias (b)**: Término independiente
4. **Función de Activación**: Transforma la salida

**Fórmula matemática**:
```
y = activation(W · X + b)
```

### 2.2 Ejemplo: Compuertas Lógicas

**Puerta AND**:
```
X₁  X₂  | Y
0   0   | 0
0   1   | 0
1   0   | 0
1   1   | 1
```

Solución con perceptrón: `W = [1, 1]`, `b = -1.5`, activación = sign

### 2.3 El Problema de XOR

```
X₁  X₂  | Y
0   0   | 0
0   1   | 1
1   0   | 1
1   1   | 0
```

**El perceptrón simple NO puede resolver XOR** porque no es linealmente separable. No existe una línea recta que separe los puntos correctamente.

### 2.4 Solución: Redes Multicapa (MLP)

Para resolver XOR, se necesita una **capa oculta**:

```python
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(2, 4),      # Capa oculta con 4 neuronas
    nn.Sigmoid(),         # Activación no lineal
    nn.Linear(4, 1),      # Capa de salida
    nn.Sigmoid()
)
```

**¿Por qué funciona?** La capa oculta transforma el espacio de entrada a uno donde SÍ es linealmente separable.

### 2.5 Funciones de Activación

| Función | Fórmula | Rango | Uso |
|---------|---------|-------|-----|
| **Sign** | 1 si x>0, -1 si no | {-1, 1} | Histórica, no diferenciable |
| **Sigmoid** | 1/(1+e⁻ˣ) | (0, 1) | Salida de probabilidad |
| **Tanh** | (eˣ-e⁻ˣ)/(eˣ+e⁻ˣ) | (-1, 1) | Capas ocultas |
| **ReLU** | max(0, x) | [0, ∞) | **MÁS POPULAR** actualmente |

**ReLU** es la más usada porque:
- Simple de computar
- No sufre vanishing gradient
- Convergencia más rápida

### 2.6 Loop de Entrenamiento

```python
# Preparación
model = MLP()
criterion = nn.BCELoss()  # Binary Cross-Entropy
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Entrenamiento
for epoch in range(1000):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)

    # Backward pass
    optimizer.zero_grad()  # Limpiar gradientes previos
    loss.backward()        # Calcular gradientes
    optimizer.step()       # Actualizar pesos

    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item():.4f}')
```

### 2.7 Funciones de Pérdida (Loss Functions)

| Función | Uso | PyTorch |
|---------|-----|---------|
| **MSE** | Regresión | `nn.MSELoss()` |
| **BCE** | Clasificación binaria | `nn.BCELoss()` |
| **CrossEntropy** | Clasificación multiclase | `nn.CrossEntropyLoss()` |

### 2.8 Optimizadores

| Optimizador | Descripción | Recomendación |
|-------------|-------------|---------------|
| **SGD** | Básico, learning rate fijo | Para experimentar |
| **Adam** | Adapta LR automáticamente | **Usar por defecto** |

**Consejo del profesor**: "Para empezar, usa Adam con lr=0.001. Funciona bien en el 80% de los casos."

### 2.9 Autograd: Gradientes Automáticos

```python
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2  # y = x²
z = 2 * y   # z = 2x²

z.backward()  # Calcular gradiente dz/dx

print(x.grad)  # 8.0 (derivada: 4x, con x=2)
```

**Contextos importantes**:
```python
# Desactivar gradientes (para inferencia)
with torch.no_grad():
    predictions = model(X_test)

# Detach (separar del grafo computacional)
x_detached = x.detach()
```

---

# CLASES 3-6 (Septiembre - Octubre 2025)
## REDES CONVOLUCIONALES (CNN)

### 3.1 Tarea 1: Dataset Imagenette

**Imagenette** es un subset de 10 clases de ImageNet:
- Clasificación desde cero (sin modelos pre-entrenados)
- Clases: pez, perro, camión, etc.

### 3.2 Capas Convolucionales

```python
# Convolución 2D
conv = nn.Conv2d(
    in_channels=3,      # RGB
    out_channels=64,    # Número de filtros
    kernel_size=3,      # Filtro 3x3
    stride=1,           # Paso
    padding=1           # Mantener tamaño
)
```

**Fórmula de tamaño de salida**:
```
output_size = (input_size - kernel_size + 2*padding) / stride + 1
```

### 3.3 Pooling

```python
# MaxPooling: reduce tamaño tomando el máximo
pool = nn.MaxPool2d(kernel_size=2, stride=2)  # Reduce a la mitad

# AvgPooling: reduce tomando el promedio
pool = nn.AvgPool2d(kernel_size=2, stride=2)
```

### 3.4 Arquitectura CNN Típica

```python
class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(64, 128, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 8 * 8, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x
```

### 3.5 Técnicas de Regularización

**Dropout**: Apaga neuronas aleatoriamente
```python
dropout = nn.Dropout(p=0.5)  # 50% de neuronas apagadas
```

**Batch Normalization**: Normaliza activaciones
```python
bn = nn.BatchNorm2d(num_features=64)
```

**Data Augmentation**: Transforma imágenes
```python
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                        std=[0.229, 0.224, 0.225])
])
```

### 3.6 Weights & Biases (wandb)

```python
import wandb

wandb.init(project="imagenette-classifier")
wandb.config.update({
    "learning_rate": 0.001,
    "epochs": 50,
    "batch_size": 32
})

# Durante entrenamiento
wandb.log({"loss": loss.item(), "accuracy": acc})
```

---

# CLASE 7 (15 de Octubre 2025)
## U-NET Y SEGMENTACIÓN DE IMÁGENES

### 7.1 Segmentación vs Clasificación

| Clasificación | Segmentación |
|--------------|--------------|
| Imagen → 1 etiqueta | Imagen → Máscara del mismo tamaño |
| "Es un perro" | Cada píxel es "persona" o "fondo" |

### 7.2 Arquitectura U-Net

La U-Net tiene forma de **"U"** con dos partes:

**Encoder (bajada)**:
- Extrae características
- Reduce tamaño espacial con MaxPooling
- Aumenta número de canales

**Decoder (subida)**:
- Reconstruye tamaño original
- Convoluciones transpuestas
- **Skip connections** del encoder

```
Encoder          Decoder
64  ────────────→  64   (skip connection)
 ↓                 ↑
128 ────────────→ 128
 ↓                 ↑
256 ────────────→ 256
 ↓                 ↑
    [Bottleneck]
```

### 7.3 Bloques de U-Net

**Doble Convolución** (se repite en toda la red):
```python
def double_conv(in_ch, out_ch):
    return nn.Sequential(
        nn.Conv2d(in_ch, out_ch, 3, padding=1),
        nn.BatchNorm2d(out_ch),
        nn.ReLU(inplace=True),
        nn.Conv2d(out_ch, out_ch, 3, padding=1),
        nn.BatchNorm2d(out_ch),
        nn.ReLU(inplace=True)
    )
```

**Convolución Transpuesta** (para subir):
```python
upconv = nn.ConvTranspose2d(in_ch, out_ch, kernel_size=2, stride=2)
```

### 7.4 Skip Connections

Son conexiones que **concatenan** características del encoder con el decoder:

```python
def forward(self, x):
    # Encoder
    enc1 = self.enc1(x)       # Guardar
    x = self.pool1(enc1)
    enc2 = self.enc2(x)       # Guardar
    x = self.pool2(enc2)

    # Bottleneck
    x = self.bottleneck(x)

    # Decoder con skip connections
    x = self.up2(x)
    x = torch.cat([x, enc2], dim=1)  # Concatenar canales
    x = self.dec2(x)

    x = self.up1(x)
    x = torch.cat([x, enc1], dim=1)  # Concatenar canales
    x = self.dec1(x)

    return self.out(x)
```

**¿Por qué son importantes?** Recuperan detalles espaciales que se pierden durante la compresión.

### 7.5 Implementación Completa U-Net

```python
class UNet(nn.Module):
    def __init__(self):
        super().__init__()

        # Encoder
        self.enc1 = self.double_conv(3, 64)
        self.pool1 = nn.MaxPool2d(2)
        self.enc2 = self.double_conv(64, 128)
        self.pool2 = nn.MaxPool2d(2)
        self.enc3 = self.double_conv(128, 256)
        self.pool3 = nn.MaxPool2d(2)
        self.enc4 = self.double_conv(256, 512)
        self.pool4 = nn.MaxPool2d(2)

        # Bottleneck
        self.bottleneck = self.double_conv(512, 1024)

        # Decoder
        self.up4 = nn.ConvTranspose2d(1024, 512, 2, stride=2)
        self.dec4 = self.double_conv(1024, 512)  # 512+512
        self.up3 = nn.ConvTranspose2d(512, 256, 2, stride=2)
        self.dec3 = self.double_conv(512, 256)
        self.up2 = nn.ConvTranspose2d(256, 128, 2, stride=2)
        self.dec2 = self.double_conv(256, 128)
        self.up1 = nn.ConvTranspose2d(128, 64, 2, stride=2)
        self.dec1 = self.double_conv(128, 64)

        # Salida
        self.out = nn.Conv2d(64, 1, 1)

    def double_conv(self, in_ch, out_ch):
        return nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        enc1 = self.enc1(x)
        enc2 = self.enc2(self.pool1(enc1))
        enc3 = self.enc3(self.pool2(enc2))
        enc4 = self.enc4(self.pool3(enc3))

        x = self.bottleneck(self.pool4(enc4))

        x = torch.cat([self.up4(x), enc4], dim=1)
        x = self.dec4(x)
        x = torch.cat([self.up3(x), enc3], dim=1)
        x = self.dec3(x)
        x = torch.cat([self.up2(x), enc2], dim=1)
        x = self.dec2(x)
        x = torch.cat([self.up1(x), enc1], dim=1)
        x = self.dec1(x)

        return torch.sigmoid(self.out(x))
```

### 7.6 Coeficiente de Dice

**Métrica principal para segmentación**:

$$\text{Dice} = \frac{2 \times |A \cap B|}{|A| + |B|}$$

Donde:
- A = píxeles predichos como "persona"
- B = píxeles reales de "persona"
- Rango: [0, 1], donde 1 = perfecto

**Implementación**:
```python
def dice_coefficient(pred, target, smooth=1e-6):
    pred = pred.view(-1)
    target = target.view(-1)

    intersection = (pred * target).sum()
    dice = (2. * intersection + smooth) / (pred.sum() + target.sum() + smooth)

    return dice

def dice_loss(pred, target):
    return 1 - dice_coefficient(pred, target)
```

### 7.7 Obligatorio: Requisitos

- **Dataset**: 2100 imágenes de 800x800
- **Mínimo requerido**: Dice ≥ 0.75
- **Competencia Kaggle**: Con premio para el mejor
- **Defensa oral**: Preguntas sobre decisiones de diseño

**Consejos del profesor**:
- Empezar con imágenes pequeñas (80x80 o 100x100)
- Modularizar el código
- Justificar TODAS las decisiones
- Las pequeñas decisiones diferencian 75 de 92.5

---

# CLASE 8 (22 de Octubre 2025)
## REDES RECURRENTES (RNN)

### 8.1 Problema: Clasificación de Secuencias

**Dataset de logs**: Secuencias de eventos del sistema
- Números del 1-27 (categorías de eventos)
- Largo variable
- Clasificación binaria: normal vs anómalo

### 8.2 Embeddings

**Problema**: Los números son categorías, no valores matemáticos.

```python
# Evento 2 y evento 4 NO tienen relación matemática
# 4 NO es "el doble" de 2
```

**Solución**: Embeddings - vectores aprendibles para cada categoría.

```python
embedding = nn.Embedding(
    num_embeddings=28,   # 27 eventos + 1 padding
    embedding_dim=8,     # Tamaño del vector
    padding_idx=0        # Índice 0 no se actualiza
)

# Uso
x = torch.tensor([2, 15, 3])
embedded = embedding(x)  # Shape: (3, 8)
```

### 8.3 Padding

Las RNNs necesitan secuencias del mismo largo:

```python
# Original: [5, 12, 3]
# Después de padding: [5, 12, 3, 0, 0, 0, 0, 0, 0, 0]
```

**Decisión**: Padding a la izquierda para RNNs (info importante al final).

### 8.4 Arquitectura RNN

```python
class RNNClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.rnn = nn.RNN(
            input_size=embed_dim,
            hidden_size=hidden_dim,
            num_layers=1,
            batch_first=True
        )
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        # x: (batch, seq_len)
        x = self.embedding(x)         # (batch, seq_len, embed_dim)
        output, hidden = self.rnn(x)  # hidden: (1, batch, hidden_dim)
        x = self.fc(hidden[-1])       # (batch, num_classes)
        return x
```

### 8.5 Salidas de RNN

```python
output, hidden = rnn(x)
```

| Salida | Shape | Uso |
|--------|-------|-----|
| **output** | (batch, seq_len, hidden_size) | Todos los hidden states |
| **hidden** | (num_layers, batch, hidden_size) | Solo el último |

**Para clasificación**: Usar `hidden[-1]` (estado final).

### 8.6 Limitación de RNN Vanilla

Con secuencias largas (100+ tokens), las RNNs "olvidan" lo que pasó al principio.

**Resultado práctico**: ~74% accuracy en dataset de logs.

---

# CLASE 9 (29 de Octubre 2025)
## LSTM (Long Short-Term Memory)

### 9.1 ¿Por qué LSTM?

Resuelve el problema de **vanishing gradients** en secuencias largas.

### 9.2 Diferencia con RNN

| RNN | LSTM |
|-----|------|
| 1 estado (hidden) | 2 estados (hidden + cell) |
| Memoria corta | Memoria larga |
| Pierde info en secuencias largas | Mantiene info |

### 9.3 Gates (Puertas)

LSTM tiene 3 puertas que controlan el flujo de información:

1. **Forget gate**: ¿Qué olvidar?
2. **Input gate**: ¿Qué agregar?
3. **Output gate**: ¿Qué mostrar?

### 9.4 Cell State vs Hidden State

**Hidden state (h)**: Salida visible, se usa para predicciones.

**Cell state (c)**: Memoria interna a largo plazo.

**Analogía**: Cell state = memoria a largo plazo (infancia), Hidden = memoria de trabajo (ahora).

### 9.5 Implementación (Cambio Mínimo)

```python
# Antes (RNN)
self.rnn = nn.RNN(input_size, hidden_size, num_layers)
output, hidden = self.rnn(x)

# Después (LSTM)
self.lstm = nn.LSTM(input_size, hidden_size, num_layers)
output, (hidden, cell) = self.lstm(x)
```

**El resto del código es idéntico.**

### 9.6 Resultados

| Modelo | Accuracy |
|--------|----------|
| RNN vanilla | ~74% |
| LSTM | ~87% |

### 9.7 GRU (Alternativa)

**GRU** (Gated Recurrent Unit): Similar a LSTM pero más simple (2 gates vs 3).

```python
self.gru = nn.GRU(input_size, hidden_size, num_layers)
output, hidden = self.gru(x)  # Solo hidden, no cell
```

A veces funciona igual de bien y entrena más rápido.

### 9.8 Tarea 2: Clasificación de ECG

**Dataset**: Señales de electrocardiograma
- 5 clases de ritmos cardíacos
- ~180 puntos por secuencia
- Dataset desbalanceado

**Diferencia**: Son valores continuos, NO necesitan embeddings.

```python
class ECGClassifier(nn.Module):
    def __init__(self, hidden_size, num_classes):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=1,  # Señal unidimensional
            hidden_size=hidden_size,
            num_layers=2,
            batch_first=True,
            dropout=0.3
        )
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # x: (batch, seq_len, 1)
        _, (hidden, _) = self.lstm(x)
        return self.fc(hidden[-1])
```

---

# CLASES 10-11 (Noviembre 2025)
## SEQUENCE-TO-SEQUENCE Y TRADUCCIÓN

### 10.1 Nuevo Problema

| Antes | Ahora |
|-------|-------|
| Sequence-to-One | Sequence-to-Sequence |
| Secuencia → 1 etiqueta | Secuencia → Secuencia |
| Clasificación | Traducción |

**Ejemplo**:
```
Input:  "Hello world"    (2 tokens)
Output: "¡Hola mundo!"   (4 tokens)
```

### 10.2 Vocabulario

Mapeo palabra ↔ número. Se necesitan **DOS vocabularios** (uno por idioma).

```python
class Vocabulary:
    def __init__(self):
        self.word_to_idx = {"<PAD>": 0, "<SOS>": 1, "<EOS>": 2, "<UNK>": 3}
        self.idx_to_word = {0: "<PAD>", 1: "<SOS>", 2: "<EOS>", 3: "<UNK>"}
        self.idx = 4

    def add_word(self, word):
        if word not in self.word_to_idx:
            self.word_to_idx[word] = self.idx
            self.idx_to_word[self.idx] = word
            self.idx += 1
```

**Tokens especiales**:
- `<PAD>`: Padding
- `<SOS>`: Start of Sequence
- `<EOS>`: End of Sequence
- `<UNK>`: Unknown word

### 10.3 Arquitectura Encoder-Decoder

```
ENCODER (inglés)
[hello, world] → LSTM → [hidden, cell]
                           ↓
DECODER (español)
<SOS> → LSTM → [¡] → LSTM → [hola] → LSTM → [mundo] → ... → <EOS>
```

**Flujo**:
1. Encoder procesa toda la entrada
2. Guarda hidden y cell final
3. Decoder empieza con `<SOS>` y estados del encoder
4. Genera palabra por palabra
5. Para cuando predice `<EOS>`

### 10.4 Encoder

```python
class Encoder(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)

    def forward(self, x):
        x = self.embedding(x)
        _, (hidden, cell) = self.lstm(x)
        return hidden, cell
```

### 10.5 Decoder

```python
class Decoder(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x, hidden, cell):
        x = self.embedding(x.unsqueeze(1))  # (batch, 1, embed)
        output, (hidden, cell) = self.lstm(x, (hidden, cell))
        prediction = self.fc(output.squeeze(1))
        return prediction, hidden, cell
```

### 10.6 Teacher Forcing

**Problema**: Si el decoder se equivoca, todas las siguientes predicciones están mal.

**Solución**: Durante entrenamiento, dar el token CORRECTO como input.

```python
teacher_forcing_ratio = 0.5

for t in range(target_len):
    output, hidden, cell = decoder(input, hidden, cell)

    if random.random() < teacher_forcing_ratio:
        input = target[t]      # Token correcto (ayuda)
    else:
        input = output.argmax()  # Predicción (sin ayuda)
```

### 10.7 Padding en Seq2Seq

| Encoder | Decoder |
|---------|---------|
| Padding IZQUIERDA | Padding DERECHA |
| `[0, 0, hello, world]` | `[<SOS>, hola, mundo, <EOS>, 0, 0]` |

---

# CLASE 12 (19 de Noviembre 2025)
## MECANISMO DE ATENCIÓN Y TRANSFORMERS

### 12.1 Problema del Encoder-Decoder

Toda la información se comprime en UN SOLO vector (hidden/cell). Es un "bottleneck".

### 12.2 Atención

En cada paso del decoder, "mirar" TODAS las salidas del encoder y decidir a cuáles prestar atención.

**Componentes**:
- **Query (Q)**: ¿Qué busco? (del decoder)
- **Keys (K)**: ¿Qué características tengo? (del encoder)
- **Values (V)**: ¿Qué información aporto? (del encoder)

**Fórmula**:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

### 12.3 Self-Attention

La secuencia se mira a sí misma para entender contexto.

**Ejemplo**: "El banco está cerca del río"
- Self-attention permite que "banco" mire a "río" y entienda que es un borde de río, no institución financiera.

### 12.4 Multi-Head Attention

Múltiples atenciones en paralelo. Cada "cabeza" aprende diferentes relaciones.

### 12.5 Positional Encoding

La atención NO tiene noción de orden. Se agrega información posicional:

$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$
$$PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

### 12.6 Diferencias RNN vs Transformer

| RNN/LSTM | Transformer |
|----------|-------------|
| Secuencial | Paralelo |
| Lento | Rápido |
| Memoria limitada | Toda la secuencia |
| Pierde info en largas | Maneja largas |
| Más simple | Más complejo |

---

# GLOSARIO COMPLETO

## A
- **Accuracy**: Porcentaje de predicciones correctas
- **Activation function**: Función no lineal (ReLU, Sigmoid, etc.)
- **Adam**: Optimizador adaptativo popular
- **Argmax**: Índice del valor máximo
- **Attention**: Mecanismo para "mirar" selectivamente partes de la entrada
- **Autograd**: Sistema automático de gradientes en PyTorch

## B
- **Backpropagation**: Calcular gradientes propagando error hacia atrás
- **Batch**: Conjunto de muestras procesadas simultáneamente
- **Batch_first**: Parámetro para poner dimensión de batch primero
- **BatchNorm**: Normalización por batch para estabilizar entrenamiento
- **Bottleneck**: Punto más comprimido en una arquitectura
- **Broadcasting**: Reglas para operar tensores de diferente shape

## C
- **Cell state**: Memoria a largo plazo en LSTM
- **Channel**: Dimensión de características (ej: RGB = 3 canales)
- **CNN**: Red convolucional para imágenes
- **Collate function**: Procesa batches antes de pasar al modelo
- **CrossEntropyLoss**: Pérdida para clasificación multiclase
- **CUDA**: Framework de NVIDIA para GPU

## D
- **Decoder**: Reconstruye/genera secuencias
- **Device**: CPU, CUDA o MPS
- **Dice coefficient**: Métrica de segmentación (0-1)
- **Dropout**: Regularización que apaga neuronas aleatoriamente
- **dtype**: Tipo de dato del tensor

## E
- **Embedding**: Vector aprendible para categorías
- **Encoder**: Comprime información de entrada
- **EOS**: End Of Sequence token
- **Epoch**: Pasada completa por todo el dataset

## F
- **F1-score**: Media armónica de precision y recall
- **Feature map**: Salida de capa convolucional
- **Float16/32**: Tipos de punto flotante
- **Forward pass**: Calcular salida de la red

## G
- **Gate**: Componente de LSTM que controla flujo de info
- **Gradient**: Derivada para actualizar pesos
- **GRU**: Alternativa más simple a LSTM

## H
- **Hidden state**: Estado oculto en RNNs
- **Hidden size**: Dimensión del vector oculto

## K
- **Kernel**: Filtro en convoluciones

## L
- **Learning rate**: Tamaño del paso de actualización
- **Loss function**: Mide el error de predicciones
- **LSTM**: RNN con memoria a largo plazo

## M
- **Mask**: Tensor booleano para selección
- **MaxPool**: Reduce tamaño tomando máximo
- **MLP**: Multi-Layer Perceptron
- **Multi-head attention**: Múltiples atenciones en paralelo

## N
- **ndim**: Número de dimensiones
- **num_layers**: Capas apiladas en RNN

## O
- **Optimizer**: Actualiza pesos (Adam, SGD)
- **Overfitting**: Memorizar datos de entrenamiento

## P
- **PAD**: Token de padding
- **Padding**: Rellenar secuencias/imágenes
- **Perceptron**: Neurona artificial básica
- **Positional encoding**: Información de posición en Transformers
- **Precision**: TP/(TP+FP)

## R
- **Recall**: TP/(TP+FN)
- **ReLU**: max(0, x)
- **Reshape**: Cambiar dimensiones
- **RLE**: Run-Length Encoding para máscaras
- **RNN**: Red recurrente para secuencias

## S
- **Self-attention**: Secuencia se mira a sí misma
- **Seq2Seq**: Secuencia a secuencia
- **Shape**: Dimensiones del tensor
- **Sigmoid**: 1/(1+e^-x)
- **Skip connection**: Conexión que salta capas
- **Softmax**: Convierte logits en probabilidades
- **SOS**: Start Of Sequence token
- **Squeeze**: Eliminar dimensiones de tamaño 1
- **Stride**: Paso en convolución/pooling

## T
- **Teacher forcing**: Usar valores correctos durante entrenamiento
- **Tensor**: Matriz multidimensional
- **Token**: Unidad básica en secuencias
- **Transformer**: Arquitectura basada en atención

## U
- **U-Net**: Arquitectura en U para segmentación
- **UNK**: Token para palabras desconocidas
- **Unsqueeze**: Agregar dimensión de tamaño 1

## V
- **Vanishing gradient**: Gradientes muy pequeños en redes profundas
- **View**: Cambiar shape del tensor
- **Vocabulary**: Mapeo palabra ↔ número

## W
- **wandb**: Weights & Biases para tracking
- **Weights**: Parámetros aprendibles

---

# FÓRMULAS MATEMÁTICAS CLAVE

### Perceptrón
```
y = activation(W · X + b)
```

### Funciones de Activación
```
Sigmoid:  σ(x) = 1 / (1 + e^(-x))
Tanh:     tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))
ReLU:     ReLU(x) = max(0, x)
```

### Convolución
```
output_size = (input_size - kernel_size + 2*padding) / stride + 1
```

### Dice Coefficient
```
Dice = (2 × |A ∩ B|) / (|A| + |B|)
```

### RNN
```
h_t = tanh(W_ih · x_t + W_hh · h_{t-1} + b)
```

### Atención
```
Attention(Q, K, V) = softmax(Q·K^T / √d_k) · V
```

### Positional Encoding
```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

---

# CONSEJOS DEL PROFESOR

## Para Programar
- "Siempre trackeen los shapes mientras desarrollan"
- "Modularicen el código - crear bloques reutilizables"
- "Prueben con datos pequeños primero"
- "Usen `batch_first=True` siempre en RNNs"

## Para Entrenar
- "Empiecen con modelos pequeños para iterar rápido"
- "Si cada época demora 30 min, nunca van a experimentar"
- "GPU es 15-50x más rápido, úsenla"
- "Guarden checkpoints durante el entrenamiento"

## Para el Obligatorio
- "Las pequeñas decisiones hacen la diferencia entre 75 y 92.5"
- "Justifiquen TODAS sus decisiones"
- "El 80% del trabajo NO es programar la red"
- "Data augmentation, preprocessing, análisis es lo más importante"

## General
- "Broadcasting es pregunta segura de parcial"
- "No subestimen el obligatorio (50% de la nota)"
- "El parcial no busca reprobar, busca excelencia (90+)"
- "Usen wandb para no perder experimentos"

---

# HERRAMIENTAS DEL CURSO

| Herramienta | Uso |
|-------------|-----|
| **PyTorch** | Framework de deep learning |
| **Jupyter Notebook** | Desarrollo interactivo |
| **Anaconda/Conda** | Gestión de ambientes |
| **Google Colab** | GPU gratuita en la nube |
| **Weights & Biases** | Tracking de experimentos |
| **Kaggle** | Competencias y datasets |

---

*Documento generado mediante análisis exhaustivo (3 pasadas) de las 12 transcripciones del curso.*
