# Guía de Patrones y Prácticas - Prácticos de IA Generativa

## Índice
1. [Estructura General](#estructura-general)
2. [Patrones de Código](#patrones-de-código)
3. [Estilos de Documentación](#estilos-de-documentación)
4. [Patrones por Práctico](#patrones-por-práctico)
5. [Convenciones de Nomenclatura](#convenciones-de-nomenclatura)
6. [Prácticas de Machine Learning](#prácticas-de-machine-learning)

---

## Estructura General

### Organización de Notebooks

Todos los notebooks siguen esta estructura consistente:

1. **Título principal en Markdown** (nivel 1 `#`)
2. **Sección de Imports** claramente marcada
3. **Secciones numeradas** con títulos descriptivos
4. **Celdas de markdown explicativas** antes de cada bloque de código
5. **Ejercicios y preguntas** al final de cada sección importante
6. **Sección de ejercicios finales** al terminar el notebook

### Patrón de Celdas

```
[Markdown: Título de sección]
[Markdown: Explicación conceptual]
[Code: Código con comentarios]
[Markdown: Preguntas o instrucciones]
[Code: Código para completar (con ...)]
```

---

## Patrones de Código

### 1. Imports

**Siempre se organizan en una sección dedicada** al inicio del notebook:

```python
# Imports estándar
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Imports de deep learning
import torch
import torch.nn as nn

# Imports específicos del práctico
from sklearn import datasets
from transformers import AutoTokenizer, AutoModelForCausalLM
```

**Reglas:**
- Imports estándar primero (numpy, pandas, matplotlib)
- Imports de frameworks (torch, tensorflow) después
- Imports específicos al final
- Un comentario opcional separando categorías
- Nunca mezclar imports en medio del código

### 2. Configuración de Device

**Patrón estándar para PyTorch:**

```python
DEVICE = torch.device(
    'cuda:0' if torch.cuda.is_available() else
    'mps' if torch.backends.mps.is_available() else
    'cpu'
)
print(DEVICE)

torch.manual_seed(42)
torch.backends.cudnn.deterministic = True
```

**Características:**
- Variable en MAYÚSCULAS (`DEVICE`)
- Prioridad: CUDA > MPS > CPU
- Siempre imprimir el device seleccionado
- Fijar semilla para reproducibilidad (`42` es el valor estándar)
- Hacer determinístico el backend

### 3. Hiperparámetros

**Siempre usar variables en MAYÚSCULAS:**

```python
BATCH_SIZE = 64
LR = 0.001
EPOCHS = 10
LATENT_DIM = 100
NUM_CLASSES = 10
```

**Reglas:**
- Nombres descriptivos en UPPER_CASE
- Agrupar hiperparámetros relacionados
- Definir antes de crear modelos
- Usar `...` para valores que el estudiante debe completar

### 4. Comentarios "TODO"

**Formato estándar para código a completar:**

```python
# TODO: Completar esta sección
# TODO: Definir las capas de la red
# TODO: Implementar el forward pass
```

**Patrón alternativo con placeholder:**

```python
def forward(self, x):
    # TODO: Completar esta sección.
    # Debes codificar 'x' usando la capa encoder
    # computar la media y la varianza de la distribución latente.
    # Devuelve la media y varianza
    ...
```

### 5. Placeholders para Código Incompleto

**Usar `...` (Ellipsis) en Python:**

```python
# Código a completar
variable = ...

# Función a completar
def mi_funcion():
    ...

# Dentro de expresiones
resultado = funcion_a_completar(...)
```

**Nunca usar:**
- `None` (puede causar errores si se ejecuta)
- `pass` (no es claro que hay que completar)
- Comentarios solos sin placeholder

### 6. Visualización de Imágenes

**Patrón estándar para mostrar grillas de imágenes:**

```python
def show_images(images, title="MNIST Images"):
    n = len(images)
    rows = math.floor(math.sqrt(n))
    columns = math.ceil(n / rows)

    fig, axs = plt.subplots(rows, columns)
    fig.suptitle(title, fontsize=14, y=.95)

    for i in range(rows):
        for j in range(columns):
            index = i*columns + j
            if index < n:
                axs[i,j].imshow(images[index], cmap='gray')
            axs[i,j].axis('off')

    plt.show()
```

**Características:**
- Función reutilizable con parámetro `title`
- Cálculo automático de filas/columnas
- Manejo de índices fuera de rango
- `axis('off')` para ocultar ejes
- `cmap='gray'` para imágenes en escala de grises

---

## Estilos de Documentación

### 1. Títulos de Secciones

```markdown
# Título Principal del Notebook
## Sección Principal (Parte 1, Parte 2, etc.)
### Subsección (Paso 1, Paso 2, etc.)
#### Sub-subsección (opcional)
```

### 2. Explicaciones Conceptuales

**Siempre antes del código:**

```markdown
### Nombre de la Sección

Explicación breve de qué se va a hacer y por qué es importante.

Conceptos clave:
- Concepto 1
- Concepto 2
```

### 3. Preguntas y Ejercicios

**Formato con viñetas o números:**

```markdown
### Ejercicio:
- ¿Pregunta 1?
- ¿Pregunta 2?
- Tarea: Implementar X

### Ejercicios:
1. Complete el código de...
2. Entrene el modelo usando...
3. Compare resultados...
```

### 4. Notas Importantes

```markdown
**Importante:** Texto destacado

**Nota:** Observación relevante

**IMPORTANTE:** Para cosas muy críticas
```

### 5. Instrucciones Técnicas

```markdown
Puede utilizar la función `nombre_funcion`.
Link: https://docs...

Recomendamos usar `método_x` de pandas.

No se olviden de...
```

---

## Patrones por Práctico

### Práctico 1: Tennis (Distribuciones Discretas)

**Estructura:**
1. Carga de datos con pandas
2. Eliminación de columnas innecesarias
3. Separación de features (X) y target (Y)
4. Construcción de tablas de frecuencia
5. Cálculo de distribuciones conjuntas
6. Cálculo de distribuciones condicionales
7. Muestreo desde distribuciones

**Patrones específicos:**

```python
# Separación de features y target
X_names = df.columns.to_list()[:-1]
X = df.iloc[:,0:-1]
Y_name = df.columns.to_list()[-1]
Y = df.iloc[:,-1]

# Tabla de observaciones
obs = pd.DataFrame(0, columns=yvalues, index=xvalues)

# Probabilidad conjunta
joint_x_y = obs / N

# Probabilidad condicional
p_y_x = pd.DataFrame(0, columns=yvalues, index=xvalues)
# División por suma de filas para P(y|x)
```

**Preguntas típicas:**
- "¿Qué significa el valor calculado en...?"
- "¿Por qué la suma de las filas da 1?"
- "¿Qué pasaría si...?"

### Práctico 2: Redes Bayesianas e Iris (Distribuciones Continuas)

**Estructura Parte 1 (Bayesianas):**
1. Instalación de pgmpy
2. Carga de datos
3. Definición de relaciones entre variables
4. Creación del modelo bayesiano
5. Ajuste con MaximumLikelihoodEstimator
6. Visualización del grafo
7. Inspección de CPDs (Conditional Probability Distributions)
8. Inferencia con VariableElimination

**Patrones específicos:**

```python
# Definición de relaciones
relations = [(var1, target), (var2, target)]

# Creación del modelo
model = BayesianNetwork(relations)

# Ajuste
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Inferencia
inferencia = VariableElimination(model)
resultado = inferencia.query(
    variables=[target],
    evidence={var1: 'value', var2: 'value'}
)
```

**Estructura Parte 2 (Iris - Continuas):**
1. Carga de dataset Iris
2. Selección de una feature
3. Discretización con `np.digitize` y `np.linspace`
4. Visualización con `sns.displot` (kde)
5. Aproximación de p(x|y) con histogramas
6. Muestreo con `gaussian_kde` de scipy
7. Aproximación con distribuciones normales
8. Mezcla de Gaussianas

**Patrones específicos:**

```python
# Discretización
NBINS = 10
bin_size = (np.max(data) - np.min(data)) / NBINS
end = np.max(data) - bin_size
bins = np.linspace(start=np.min(data), stop=end, num=NBINS)
xfeature_digitized = np.digitize(x=data, bins=bins)

# Visualización KDE
sns.displot(data=pd_cats, x='x', kind='kde', hue='cat', fill=True)

# Muestreo con KDE
from scipy.stats import gaussian_kde
kde = gaussian_kde(data_for_class)
samples = kde.resample(size=50)
```

### Práctico 3: Hinton Perceptron (Autoregresivo)

**Estructura:**
1. Configuración de device
2. Transformaciones (binarización)
3. Dataset y DataLoader
4. Exploración del dataset
5. Definición de Hinton Perceptron
6. Creación del modelo e hiperparámetros
7. Función de entrenamiento
8. Entrenamiento del modelo
9. Generación de imágenes

**Patrones específicos:**

```python
# Transformación personalizada
class BinarizedTransform:
    def __call__(self, img):
        return (img > .5).float()

# Filtrado de dataset por labels
train_data = [(image, label) for image, label in train_data
              if labels_used and label in labels_used]

# Máscara autoregresiva
self.mask = torch.tril(torch.ones((self.img_size, self.img_size)), diagonal=-1)

# Aplicación de máscara
w_masked = self.w * self.mask

# Generación autore

gresiva
with torch.no_grad():
    for pixel in range(num_pixels):
        # Obtener probabilidades
        probs = model(x_partial)
        # Muestrear Bernoulli
        x[:, pixel] = torch.bernoulli(probs[:, pixel])
```

**Función de pérdida específica:**

```python
# Binary Cross Entropy para cada píxel
criterion = nn.BCELoss()
loss = criterion(preds, x)
```

### Práctico 4: VAE (Variational AutoEncoder)

**Estructura:**
1. Dataset MNIST
2. Definición de la arquitectura VAE
3. Función de pérdida (reconstruction + KLD)
4. Entrenamiento
5. Generación
6. Visualización del espacio latente

**Patrones específicos:**

```python
class VAE(nn.Module):
    def __init__(self, input_dim=784, latent_dim=2, device='cpu'):
        # Encoder
        self.encoder = nn.Sequential(...)
        self.mean_layer = nn.Linear(hidden_dim, latent_dim)
        self.logvar_layer = nn.Linear(hidden_dim, latent_dim)

        # Decoder
        self.decoder = nn.Sequential(...)

    def reparameterization(self, mean, var):
        # Reparameterization trick
        epsilon = torch.randn_like(var).to(self.device)
        z = mean + var * epsilon
        return z

# Función de pérdida
def loss_function(x, x_hat, mean, log_var):
    reproduction_loss = F.binary_cross_entropy(x_hat, x, reduction='sum')
    KLD = -0.5 * torch.sum(1 + log_var - mean.pow(2) - log_var.exp())
    return reproduction_loss + KLD
```

**Visualización del espacio latente:**

```python
def plot_latent_space(model, scale=5.0, n=25):
    grid_x = np.linspace(-scale, scale, n)
    grid_y = np.linspace(-scale, scale, n)[::-1]

    for i, yi in enumerate(grid_y):
        for j, xi in enumerate(grid_x):
            z_sample = torch.tensor([[xi, yi]])
            x_decoded = model.decode(z_sample)
            # Colocar en grilla
```

### Práctico 5: GAN (Generative Adversarial Networks)

**Estructura:**
1. Dataset (FashionMNIST o SVHN)
2. Definición del Generador (ConvTranspose2d)
3. Definición del Discriminador (Conv2d)
4. Hiperparámetros (con LR diferentes)
5. Función de entrenamiento alternada
6. Generación de imágenes

**Patrones específicos:**

```python
# Generador con ConvTranspose2d
class Generator(nn.Module):
    def __init__(self, latent_dim, number_feature_maps, output_channels):
        self.main = nn.Sequential(
            nn.ConvTranspose2d(latent_dim, nfm * 4, 7, 1, 0, bias=False),
            nn.BatchNorm2d(nfm * 4),
            nn.ReLU(True),
            # ... más capas
            nn.ConvTranspose2d(nfm, output_channels, 3, 1, 1, bias=False),
            nn.Tanh()
        )

# Discriminador con Conv2d
class Discriminator(nn.Module):
    def __init__(self, input_channels, number_feature_maps, output_dim):
        self.conv_layers = nn.Sequential(
            nn.Conv2d(input_channels, nfm, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            # ... más capas
        )
        self.fully_connected = nn.Sequential(
            nn.Flatten(1),
            nn.Linear(..., output_dim),
            nn.Sigmoid()
        )

# Entrenamiento alternado
def train(generator, discriminator, ...):
    optimizer_G = optim.Adam(generator.parameters(), lr=generator_lr)
    optimizer_D = optim.Adam(discriminator.parameters(), lr=discriminator_lr)

    for epoch in range(n_epochs):
        for i, (imgs, _) in enumerate(dataloader):
            # Etiquetas
            valid = torch.ones(bs, 1)
            fake = torch.zeros(bs, 1)

            # Entrenar Generador
            z = torch.randn(bs, latent_dim, 1, 1)
            gen_imgs = generator(z)
            g_loss = adversarial_loss(discriminator(gen_imgs), valid)

            optimizer_G.zero_grad()
            g_loss.backward()
            optimizer_G.step()

            # Entrenar Discriminador (con .detach())
            real_loss = adversarial_loss(discriminator(real_imgs), valid)
            fake_loss = adversarial_loss(discriminator(gen_imgs.detach()), fake)
            d_loss = (real_loss + fake_loss) / 2

            optimizer_D.zero_grad()
            d_loss.backward()
            optimizer_D.step()
```

**Función de pérdida:**

```python
adversarial_loss = nn.BCELoss()
```

### Práctico 6: Language Models (GPT-2)

**Estructura:**
1. Carga de tokenizer y modelo
2. Comparación de tokenizers (BERT vs GPT-2)
3. Análisis de logits
4. Implementación manual de Top-K y Top-P sampling
5. Generación de texto con diferentes parámetros
6. Análisis de sesgos

**Patrones específicos:**

```python
# Configuración de logging
from transformers import logging as transformers_logging
transformers_logging.set_verbosity_error()

# Carga de modelo
tokenizer = AutoTokenizer.from_pretrained('distilgpt2')
model = AutoModelForCausalLM.from_pretrained('distilgpt2')
model.eval()

# Top-K sampling
def top_k_sampling(logits, k=50):
    top_k_probs, top_k_indices = torch.topk(logits, k)
    top_k_probs = F.softmax(top_k_probs, dim=-1)
    next_token_idx = torch.multinomial(top_k_probs, 1)
    next_token = top_k_indices.gather(-1, next_token_idx)
    return next_token

# Top-P sampling
def top_p_sampling(logits, p=0.9):
    sorted_logits, sorted_indices = torch.sort(logits, descending=True)
    sorted_probs = F.softmax(sorted_logits, dim=-1)
    cumulative_probs = torch.cumsum(sorted_probs, dim=-1)

    sorted_indices_to_remove = cumulative_probs > p
    sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
    sorted_indices_to_remove[..., 0] = 0

    indices_to_remove = sorted_indices[sorted_indices_to_remove]
    logits[indices_to_remove] = float('-inf')

    probs = F.softmax(logits, dim=-1)
    next_token = torch.multinomial(probs, 1)
    return next_token

# Generación con parámetros
output = model.generate(
    **inputs,
    max_length=20,
    temperature=0.7,
    top_k=50,
    top_p=0.9,
    do_sample=True
)
```

### Práctico 7: Diffusion Models

**Estructura:**
1. Instalación de librerías (diffusers)
2. Carga del modelo preentrenado (DDPM)
3. Generación de imágenes con diferentes timesteps
4. Manipulación de ruido (seeds)
5. Generación en batch
6. Proceso step-by-step con scheduler
7. Interpolación en espacio latente
8. Denoising controlado

**Patrones específicos:**

```python
# Creación de carpetas
import os
os.makedirs("./imgs", exist_ok=True)
os.makedirs("./grid", exist_ok=True)
os.makedirs("./gifs", exist_ok=True)

# Carga del pipeline
from diffusers import DDPMPipeline
pipeline = DDPMPipeline.from_pretrained("google/ddpm-cifar10-32")

# Generación con parámetros
imgs = pipeline(
    num_inference_steps=50,
    batch_size=16,
    generator=torch.manual_seed(42)
).images

# Acceso al scheduler
scheduler = pipeline.scheduler
scheduler.set_timesteps(num_inference_steps)

# Denoising paso a paso
def denoise_image(unet_model, noisy_image, scheduler, num_inference_steps):
    image = noisy_image
    for t in range(num_inference_steps):
        current_timestep = scheduler.timesteps[t]

        with torch.no_grad():
            model_output = unet_model(image, current_timestep).sample

        image = scheduler.step(model_output, current_timestep, image).prev_sample

    return image

# Interpolación en espacio latente
alpha_values = np.linspace(0, 1, steps)
for alpha in alpha_values:
    interpolated_noise = (1 - alpha) * noise1 + alpha * noise2
    image = denoise_image(pipeline.unet, interpolated_noise, scheduler, steps)

# Crear GIF
import imageio
images_for_gif = [...]
imageio.mimsave('output.gif', images_for_gif, duration=0.5)
```

---

## Convenciones de Nomenclatura

### Variables

| Tipo | Convención | Ejemplo |
|------|------------|---------|
| Hiperparámetros | UPPER_CASE | `BATCH_SIZE`, `LR`, `EPOCHS` |
| Constantes globales | UPPER_CASE | `DEVICE`, `NUM_CLASSES` |
| Variables locales | snake_case | `data_loader`, `train_loss` |
| DataFrames | snake_case | `df`, `train_data`, `iris_df` |
| Tensores | snake_case | `x`, `y`, `z`, `images` |
| Modelos | snake_case | `model`, `generator`, `discriminator` |
| Funciones | snake_case | `train_model`, `generate_images` |
| Clases | PascalCase | `HintonPerceptron`, `VAE`, `Generator` |

### Nombres Específicos de ML

| Concepto | Variable típica |
|----------|----------------|
| Input | `x`, `X`, `inputs` |
| Target | `y`, `Y`, `labels`, `targets` |
| Predictions | `preds`, `y_hat`, `outputs` |
| Loss | `loss`, `g_loss`, `d_loss` |
| Latent vector | `z`, `latent` |
| Batch | `batch`, `imgs` |
| Index | `i`, `j`, `idx` |
| Epoch | `epoch` |
| Dataset | `dataset`, `train_data`, `test_data` |
| DataLoader | `dataloader`, `train_loader` |

---

## Prácticas de Machine Learning

### 1. Entrenamiento de Modelos

**Estructura estándar de función de entrenamiento:**

```python
def train_model(
    model: nn.Module,
    criterion: nn.Module,
    n_epochs: int,
    train_loader: DataLoader,
    optim: torch.optim.Optimizer,
    print_epoch: int = 1
):
    for epoch in tqdm(range(n_epochs)):
        start_time = time.time()
        learning_error = 0

        for batch_idx, (x, y) in enumerate(train_loader):
            # Mover datos al device
            x = x.to(DEVICE)
            y = y.to(DEVICE)

            # Resetear gradientes
            optim.zero_grad()

            # Forward pass
            preds = model(x)

            # Calcular loss
            loss = criterion(preds, y)

            # Backward pass
            loss.backward()

            # Optimizar
            optim.step()

            learning_error += loss.item()

        if epoch % print_epoch == 0:
            # Visualización o métricas
            print(f"Epoch: {epoch+1} - duration {time.time()-start_time}s - error: {learning_error/len(train_loader)}")

    return model
```

**Características clave:**
- Type hints en parámetros
- `tqdm` para progress bar
- Timer para medir duración
- Acumulación de error
- `optim.zero_grad()` antes del forward
- `.item()` para extraer valor de tensor
- Retornar modelo entrenado

### 2. Generación de Datos

**Patrón estándar:**

```python
def generate(model, num_samples=16):
    model.eval()  # Modo evaluación

    with torch.no_grad():  # No calcular gradientes
        # Generar ruido
        z = torch.randn(num_samples, latent_dim).to(DEVICE)

        # Generar muestras
        samples = model.generate(z)  # o model.decode(z)

    return samples
```

### 3. Manejo de Datasets

**Patrón estándar:**

```python
# Transformaciones
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Dataset
dataset = datasets.MNIST(
    root='./data',
    train=True,
    transform=transform,
    download=True
)

# DataLoader
dataloader = DataLoader(
    dataset=dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

# Iteración
for batch_idx, (images, labels) in enumerate(dataloader):
    # Procesar batch
    pass
```

### 4. Evaluación y Métricas

**Siempre usar `model.eval()` y `torch.no_grad()`:**

```python
model.eval()

with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(DEVICE)
        labels = labels.to(DEVICE)

        outputs = model(images)
        # Calcular métricas
```

### 5. Guardado y Carga de Modelos

**Aunque no se usa en los prácticos, el patrón estándar sería:**

```python
# Guardar
torch.save(model.state_dict(), 'model.pth')

# Cargar
model = ModelClass()
model.load_state_dict(torch.load('model.pth'))
model.eval()
```

---

## Patrones de Preguntas

### Tipo 1: Comprensión Conceptual

```markdown
### Ejercicio:
- ¿Por qué es necesario el truco de reparametrización en las VAE?
- ¿Qué representan las variables mean y var en la VAE?
- ¿Cuál es el propósito de la competencia entre el generador y el discriminador?
```

### Tipo 2: Experimentación

```markdown
### Ejercicio:
1. Entrene el modelo con diferentes hiperparámetros
2. Compare los resultados
3. ¿Cómo afecta X al rendimiento?
```

### Tipo 3: Implementación

```markdown
### Ejercicio:
1. Complete el código de...
2. Implemente la función...
3. Agregue la funcionalidad de...
```

### Tipo 4: Análisis

```markdown
### Ejercicio:
- Explique qué ve en la imagen generada
- Compare esta gráfica con...
- ¿Qué observa cuando cambia el parámetro X?
```

---

## Patrones de Comentarios

### En Código

```python
# Comentario simple para una línea

# Comentario de múltiples conceptos
# que requiere varias líneas para
# explicar el proceso completo
```

### En Markdown

```markdown
### Título de Sección

Explicación general del concepto.

Detalles adicionales o notas importantes.
```

### Docstrings en Funciones

```python
def calculate_prob(y, o, h, w, t):
    "Calculate the probability of occurrence of a row"
    # Implementación
```

**Nota:** Se usa comillas simples `"..."` para docstrings cortos, no triples comillas.

---

## Gestión de Errores y Debugging

### Práctica 1: Validación de Datos

```python
# Verificar dimensiones
print(f'Cantidad total de elementos: {N}')
print(f'Elementos únicos: {unique_values}')

# Mostrar formas
print(data.shape)
print(tensor.shape)
```

### Práctica 2: Assertions y Checks

```python
# Verificar modelo
model.check_model()  # En Bayesian Networks

# Verificar dimensiones de salida
assert output.shape == expected_shape
```

### Práctica 3: Visualización Intermedia

```python
if epoch % print_epoch == 0:
    # Generar y mostrar imágenes
    imgs = model.generate_x(12).cpu()
    show_images(imgs, f"Generated images on epoch {epoch+1}")
```

---

## Estilos de Salida y Presentación

### 1. Formateo de Strings

**Usar f-strings (Python 3.6+):**

```python
print(f"Epoch: {epoch+1} - error: {error:.4f}")
print(f"[Epoch {epoch}/{n_epochs}] [Batch {i}/{len(dataloader)}]")
print(f"Texto generado: '{text}'")
```

### 2. Separadores Visuales

```python
print("-" * 50)
print("=" * 50)
```

### 3. Títulos en Gráficos

```python
plt.title("Generated Images")
plt.title(f"Epoch {epoch}")
fig.suptitle(title, fontsize=14, y=.95)
```

---

## Manejo de Tiempo y Performance

### Timer Pattern

```python
import time

start_time = time.time()
# ... operación ...
duration = time.time() - start_time

print(f"Tiempo de inferencia: {duration:.4f}s")
```

### Progress Bar

```python
from tqdm import tqdm

for epoch in tqdm(range(n_epochs)):
    # Entrenamiento
    pass
```

---

## Organización de Archivos

### Estructura de Carpetas (Práctico 7)

```python
import os

os.makedirs("./imgs", exist_ok=True)
os.makedirs("./grid", exist_ok=True)
os.makedirs("./gifs", exist_ok=True)
```

**Usar siempre `exist_ok=True`** para evitar errores si la carpeta ya existe.

---

## Consideraciones Finales

### 1. Reproducibilidad

Siempre fijar semillas al inicio:

```python
torch.manual_seed(42)
np.random.seed(42)
random.seed(42)
torch.backends.cudnn.deterministic = True
```

### 2. Limpieza de Memoria

En notebooks con modelos grandes:

```python
# Liberar memoria GPU
del model
torch.cuda.empty_cache()
```

### 3. Warnings

Suprimir warnings solo cuando sea necesario:

```python
import warnings
warnings.filterwarnings("ignore")

# O específico para transformers
from transformers import logging as transformers_logging
transformers_logging.set_verbosity_error()
```

### 4. Compatibilidad

Comentarios para instalación de dependencias:

```python
#!pip install transformers
#!pip install pgmpy
# !python -m pip install torchinfo
```

**Usar `#` comentado por defecto**, el usuario descomentar si necesita instalar.

---

## Resumen de Reglas de Oro

1. **Estructura consistente**: Título → Imports → Configuración → Secciones numeradas → Ejercicios
2. **Comentarios claros**: Antes del código, nunca dentro de expresiones complejas
3. **Variables descriptivas**: `UPPER_CASE` para constantes, `snake_case` para variables
4. **Placeholders con `...`**: Para código a completar
5. **Funciones reutilizables**: Especialmente para visualización
6. **Device management**: Siempre al inicio, con fallback CPU
7. **Seeds fijas**: Para reproducibilidad (`42` es estándar)
8. **Type hints**: En definiciones de funciones importantes
9. **Documentación en Markdown**: Antes de cada sección de código
10. **Preguntas pedagógicas**: Al final de cada sección importante

---

**Última actualización:** Noviembre 2025
**Autor:** Documentación generada para el curso de IA Generativa
**Uso:** Referencia para completar prácticos manteniendo consistencia con el material del curso
