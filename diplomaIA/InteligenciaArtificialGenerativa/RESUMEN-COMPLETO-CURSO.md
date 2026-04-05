# INTELIGENCIA ARTIFICIAL GENERATIVA - RESUMEN COMPLETO DEL CURSO

## INFORMACIÓN DEL CURSO
- **Universidad**: ORT Uruguay
- **Período**: Agosto - Noviembre 2025
- **Profesor**: Francisco (Franz)
- **Ayudante**: Juan Pedro Silva
- **Total de clases**: 11 clases teóricas + prácticos

---

## TABLA DE CONTENIDOS

1. [Introducción - ¿Qué es este curso?](#introducción)
2. [Estructura y Progresión del Curso](#estructura-del-curso)
3. [Resumen Clase por Clase](#clases)
4. [Conceptos Fundamentales](#conceptos-fundamentales)
5. [Diccionario Técnico Completo](#diccionario)
6. [Guía de Estudio](#guía-de-estudio)
7. [Recursos y Referencias](#recursos)
8. [El Obligatorio](#obligatorio)

---

## INTRODUCCIÓN

### ¿Qué es la Inteligencia Artificial Generativa?

La **IA Generativa** es el campo de la inteligencia artificial que se enfoca en crear modelos capaces de **generar nuevos datos** a partir de patrones aprendidos. A diferencia de los modelos discriminativos (que clasifican o predicen), los modelos generativos **crean contenido nuevo**: imágenes, texto, audio, video, etc.

### Diferencia Fundamental: Discriminativo vs Generativo

**Modelos Discriminativos**:
- **Objetivo**: Clasificar, predecir, decidir
- **Ejemplo**: Un modelo que mira una imagen y dice "es un gato" o "es un perro"
- **Input → Output**: Imagen → Etiqueta (siempre la misma)
- **Métrica**: Accuracy, precisión, recall (claras y objetivas)

**Modelos Generativos**:
- **Objetivo**: Crear, generar, sintetizar
- **Ejemplo**: Un modelo que crea nuevas imágenes de gatos que nunca existieron
- **Input → Output**: Ruido/prompt → Dato nuevo (diferentes cada vez)
- **Métrica**: Compleja (fidelidad + diversidad)

### Analogía Simple

Piensa en un **inspector de calidad** (discriminativo) vs un **artista** (generativo):
- El inspector mira un cuadro y dice "es genuino" o "es falso"
- El artista **crea** cuadros nuevos originales

---

## ESTRUCTURA DEL CURSO

### Roadmap General

```
📚 PROGRESIÓN DEL CURSO

SEMANAS 1-2: FUNDAMENTOS
├── Probabilidad y estadística básica
├── Variables aleatorias discretas y continuas
├── Distribuciones (Uniform, Normal, Laplace)
├── Redes Bayesianas
└── Mixturas de Gaussianas

SEMANAS 3-4: MODELOS AUTOREGRESIVOS
├── Generación secuencial pixel-a-pixel
├── Regla de la cadena
├── Arquitectura de Hinton (Belief Networks)
├── Binary Cross-Entropy
└── Maximum Likelihood Estimation

SEMANAS 5-6: VARIATIONAL AUTOENCODERS (VAEs)
├── Arquitectura Encoder-Decoder
├── Espacio latente
├── Reparametrization Trick
├── ELBO (Evidence Lower Bound)
└── β-VAE

SEMANAS 7-8: GANS (GENERATIVE ADVERSARIAL NETWORKS)
├── Juego adversarial: Generador vs Discriminador
├── Función objetivo Min-Max
├── Mode Collapse
├── DCGAN (Deep Convolutional GAN)
└── Conditional GANs

SEMANAS 9-10: MODELOS DE LENGUAJE Y DIFUSIÓN
├── Language Models (LMs)
├── Tokenización (BPE, WordPiece)
├── GPT-2 y arquitectura Transformer
├── Sampling strategies (Top-K, Top-P, temperatura)
├── Modelos de Difusión (Forward/Reverse)
├── DDPM, Stable Diffusion
└── Latent Diffusion Models

SEMANA 11: EVALUACIÓN DE MODELOS GENERATIVOS
├── Inception Score (IS)
├── Fréchet Inception Distance (FID)
├── Perplexity, BLEU, ROUGE
├── Evaluación humana
└── Downstream tasks
```

---

## CLASES

### CLASE 1 (19-08-2025): Introducción y Fundamentos de Probabilidad

#### Temas Principales
- Presentación del curso y metodología de evaluación
- ¿Qué son los modelos generativos?
- Historia de la IA Generativa (Ada Lovelace → Transformers)
- Repaso de probabilidad básica

#### Conceptos Clave

**1. Modelos Generativos - Definición**

Un modelo generativo es un sistema que:
- Aprende la distribución de probabilidad P(X) de los datos
- Puede generar muestras nuevas de esa distribución
- Tiene comportamiento **estocástico** (aleatorio) por diseño

**Ejemplo en clase**: El profesor pidió a los estudiantes generar un blues con ChatGPT. Todos obtuvieron resultados diferentes, demostrando la naturaleza estocástica de estos modelos.

**2. Variables Aleatorias**

Una variable aleatoria es una **función que mapea eventos a números reales**.

Notación:
- Variables: X, Y (mayúsculas)
- Valores: x, y (minúsculas)
- P(X = x): Probabilidad de que X tome el valor x

**Ejemplo del dado y la moneda**:
```
Dado: 6 valores posibles {1, 2, 3, 4, 5, 6}
Moneda: {Cara, Cruz}

P(Dado = 1) = 1/6
P(Moneda = Cara) = 1/2

Si son independientes:
P(Dado = 1, Moneda = Cara) = 1/6 × 1/2 = 1/12
```

**3. Reglas Fundamentales**

**Regla del producto**:
```
P(X, Y) = P(X) × P(Y | X)
```

**Regla de la suma (marginalización)**:
```
P(X) = Σ P(X, Y)
       y
```

**4. Independencia**

X e Y son independientes si:
```
P(X, Y) = P(X) × P(Y)

Equivalentemente:
P(X | Y) = P(X)
```

Significado: Saber el valor de Y no cambia la probabilidad de X.

#### Práctico 1: Dataset de Tenis

**Objetivo**: Estimar distribuciones de probabilidad a partir de datos.

**Dataset**: 14 observaciones con variables:
- Outlook: {Sunny, Overcast, Rain}
- Temperature: Continuous
- Humidity: Continuous
- Wind: {Weak, Strong}
- PlayTennis: {Yes, No}

**Tareas principales**:
1. Construir tablas de frecuencias
2. Estimar P(PlayTennis)
3. Estimar distribución conjunta P(Outlook, PlayTennis)
4. Calcular distribución condicional P(Outlook | PlayTennis) ← **Paso generativo**
5. Muestrear nuevos datos de la distribución

**Punto clave**: Invertir el problema (de P(Y|X) a P(X|Y)) es el núcleo de la generación.

---

### CLASE 2 (26-08-2025): Variables Continuas, Gaussianas y Mixturas

#### Temas Principales
- Variables aleatorias continuas
- Distribuciones: Uniforme, Normal, Laplace
- Mixturas de Gaussianas
- Conexión con modelos generativos

#### Conceptos Clave

**1. Variables Continuas**

Diferencias con variables discretas:

| Discretas | Continuas |
|-----------|-----------|
| P(X = x) (probabilidad puntual) | p(x) (densidad) |
| Σ (sumatoria) | ∫ (integral) |
| Σ P(X = x) = 1 | ∫ p(x)dx = 1 |

**2. Distribución Uniforme U(a, b)**

Todos los valores en [a, b] tienen la misma probabilidad:
```
p(x) = 1/(b-a)  si a ≤ x ≤ b
     = 0        en otro caso
```

Gráfica: Un rectángulo de altura 1/(b-a) entre a y b.

**3. Distribución Normal (Gaussiana) N(μ, σ²)**

La famosa "campana":
```
p(x) = (1 / (σ√(2π))) × exp(-(x-μ)²/(2σ²))

μ = media (centro)
σ = desviación estándar (dispersión)
```

Propiedades:
- ~68% de datos entre μ-σ y μ+σ
- ~95% entre μ-2σ y μ+2σ
- Completamente determinada por μ y σ

**4. Mixturas de Gaussianas - Concepto Clave**

**Motivación: Ejemplo del peso de gatos**

Escenario:
- Y = sexo del gato {Macho, Hembra}
- X = peso del gato (continuo)

Modelo:
```
P(Y = Macho) = θ
P(Y = Hembra) = 1-θ

X | Y=Macho ~ N(μ_macho, σ²_macho)
X | Y=Hembra ~ N(μ_hembra, σ²_hembra)
```

La distribución marginal de X es una **mixtura**:
```
p(x) = θ × N(x; μ_macho, σ²_macho)
     + (1-θ) × N(x; μ_hembra, σ²_hembra)
```

Visualización: Dos "campanas" superpuestas.

**Fórmula general** (N componentes):
```
p(x) = Σ θᵢ × N(x; μᵢ, σ²ᵢ)
      i=1

donde Σ θᵢ = 1
```

**Conexión con modelos generativos**: VAEs y GMMs (Gaussian Mixture Models) usan mixturas para modelar datos complejos.

**5. Conexión con Perceptrones**

El profesor explicó algo fundamental:

"Cuando un perceptrón da salida 0.7, NO está diciendo 'la respuesta es 0.7'. Está dando el **parámetro θ de una Bernoulli**: P(y=1|x) = Bernoulli(θ=0.7)"

Este insight conecta con cómo los modelos generativos producen distribuciones, no valores únicos.

#### Práctico 2: Dataset Iris

**Dataset**: 150 flores de 3 especies con 4 medidas cada una.

**Tareas principales**:
1. **Discretización**: Convertir valores continuos en bins
2. **Visualización**: Histogramas por especie
3. **Estimación de Gaussianas**: Calcular μ y σ para cada característica por especie
4. **Gaussian KDE**: Usar `scipy.stats.gaussian_kde` para ajustar distribuciones
5. **Generación**: Muestrear nuevas flores de las distribuciones aprendidas
6. **Mixtura**: Estimar P(X) sin conocer la especie

**Código ejemplo**:
```python
# Estimar μ y σ manualmente
mu = np.mean(data_species)
sigma = np.std(data_species)

# Generar muestras
samples = np.random.normal(mu, sigma, size=50)

# Comparar con KDE
from scipy.stats import gaussian_kde
kde = gaussian_kde(data_species)
samples_kde = kde.resample(50)
```

---

### CLASE 3 (02-09-2025): Modelos Autoregresivos - Parte 1

#### Temas Principales
- Generación secuencial
- Regla de la cadena para probabilidades
- Factorización de P(X₁, X₂, ..., Xₙ)
- Explosión combinatoria de parámetros

#### Conceptos Clave

**1. ¿Qué es "Autoregresivo"?**

Un modelo donde cada elemento generado **depende de los elementos anteriores**.

Analogía: Escribir una historia palabra por palabra, donde cada nueva palabra depende de las anteriores.

**2. Imagen como Secuencia**

Una imagen de 28×28 píxeles = 784 píxeles.

Podemos tratarla como una secuencia:
```
[píxel₁, píxel₂, píxel₃, ..., píxel₇₈₄]
```

Y generar pixel a pixel, cada uno dependiendo de los anteriores.

**3. Regla de la Cadena**

Teorema fundamental:
```
P(X₁, X₂, ..., Xₙ) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂) × ... × P(Xₙ|X₁,...,Xₙ₋₁)
```

Ejemplo con 3 píxeles:
```
P(imagen) = P(p₁) × P(p₂|p₁) × P(p₃|p₁,p₂)
```

**Interpretación generativa**:
1. Genero p₁ según P(p₁)
2. Genero p₂ condicionado en p₁
3. Genero p₃ condicionado en p₁ y p₂

**4. El Problema de Escalabilidad**

Para imágenes binarias (píxeles 0 o 1):

```
Píxel 1: 1 parámetro (θ₁)
Píxel 2: 2 parámetros (θ₂⁰, θ₂¹)
Píxel 3: 4 parámetros (θ₃⁰⁰, θ₃⁰¹, θ₃¹⁰, θ₃¹¹)
...
Píxel n: 2^(n-1) parámetros

Para 784 píxeles: 2^783 parámetros (más que átomos en el universo)
```

**5. Solución: Aproximación con Funciones**

En lugar de tabular todos los parámetros, usar una **red neuronal**:

```
θᵢ = σ(Wᵢ₁·X₁ + Wᵢ₂·X₂ + ... + Wᵢ,ᵢ₋₁·Xᵢ₋₁ + bᵢ)
```

Ahora el número de parámetros crece **linealmente**, no exponencialmente.

**6. Arquitectura de Hinton (Belief Networks)**

Propuesta: Una red con matriz de pesos **triangular inferior**:

```
W = [0    0    0    ... 0   ]  ← θ₁ no depende de nada
    [W₂₁  0    0    ... 0   ]  ← θ₂ solo de X₁
    [W₃₁  W₃₂  0    ... 0   ]  ← θ₃ de X₁, X₂
    [... ... ...  ... ... ]
    [Wₙ₁  Wₙ₂  Wₙ₃  ... Wₙ,ₙ₋₁]  ← θₙ de todos
```

Los ceros están **fijos** (no se entrenan). Esto garantiza la estructura autoregresiva.

**7. Generación vs Entrenamiento**

**Generación**: Secuencial (no paralelizable)
```
x₁ ~ Bernoulli(θ₁)
x₂ ~ Bernoulli(θ₂(x₁))
x₃ ~ Bernoulli(θ₃(x₁, x₂))
...
```

**Entrenamiento**: Paralelizable (tenemos todas las X de antemano)
```
θ = Red(X)
Loss = Σᵢ BCE(xᵢ, θᵢ)
```

#### Material de Apoyo

El profesor dibujó extensivamente en el pizarrón:
- Diagrama de la matriz triangular
- Flujo de información píxel a píxel
- Conteo de parámetros para mostrar la explosión

---

### CLASE 4 (09-09-2025): Modelos Autoregresivos - Parte 2 (Entrenamiento)

#### Temas Principales
- Función de pérdida para autorregresivos
- Maximum Likelihood Estimation (MLE)
- Binary Cross-Entropy (BCE)
- Estabilidad numérica (log-espacio)

#### Conceptos Clave

**1. De la Teoría al Entrenamiento**

**Objetivo**: Queremos que P_θ(X) se parezca a P_data(X).

**¿Cómo medir "parecido"?** Divergencia KL:
```
KL(P_data || P_θ) = E_{x ~ P_data}[log P_data(x) - log P_θ(x)]
```

**Simplificación**:
```
KL = E[log P_data(x)] - E[log P_θ(x)]
     ↑ constante (no depende de θ)

Minimizar KL ⟺ Maximizar E[log P_θ(x)]
```

Esto es **Maximum Likelihood Estimation (MLE)**.

**2. Aplicando la Regla de la Cadena**

Para modelos autoregresivos:
```
log P_θ(x) = log P_θ(x₁) + log P_θ(x₂|x₁) + ... + log P_θ(xₙ|x₁,...,xₙ₋₁)
           = Σᵢ log P_θ(xᵢ | x₁, ..., xᵢ₋₁)
```

**Función objetivo**:
```
θ* = argmax_θ (1/N) Σ_ejemplos Σ_píxeles log P_θ(xᵢ | padres)
```

**3. Binary Cross-Entropy (BCE)**

Nuestro perceptrón da θᵢ ∈ [0,1], que es P(Xᵢ = 1 | padres).

Necesitamos la probabilidad del valor observado:
- Si xᵢ = 1: probabilidad = θᵢ
- Si xᵢ = 0: probabilidad = 1 - θᵢ

**Fórmula elegante**:
```
P(xᵢ | padres) = θᵢ^xᵢ × (1-θᵢ)^(1-xᵢ)

-log P(xᵢ | padres) = -[xᵢ log θᵢ + (1-xᵢ) log(1-θᵢ)]
```

Esta es la **Binary Cross-Entropy**.

**Ejemplo numérico**:
```
Dato real: xᵢ = 1
Predicción: θᵢ = 0.8

BCE = -log(0.8) = 0.223

Si θᵢ = 0.999:
BCE = -log(0.999) = 0.001  ← Mucho mejor
```

**4. Pérdida Final**

```
L(θ) = -(1/N) Σ_ejemplos Σ_píxeles [xᵢ log θᵢ + (1-xᵢ) log(1-θᵢ)]
```

En PyTorch:
```python
criterion = nn.BCELoss()
loss = criterion(probs, targets)
```

**5. Estabilidad Numérica**

**Problema**: Multiplicar muchas probabilidades pequeñas causa **underflow**.

**Solución**: Trabajar en **log-espacio**:
```
log(a × b × c) = log(a) + log(b) + log(c)
```

Sumar es más estable que multiplicar.

Por eso optimizamos **log-likelihood** en lugar de likelihood directa.

#### Práctico 3: Implementar Modelo Autoregresivo para MNIST

**Tareas**:
1. Implementar matriz de pesos triangular
2. Implementar forward pass
3. Implementar pérdida BCE
4. Entrenar en MNIST (dígitos binarios)
5. Generar nuevas imágenes pixel a pixel
6. **Comparar tiempos**: Entrenamiento (rápido) vs Generación (lento)

**Observación del profesor**: "Entrenar es paralelo (rápido), generar es secuencial (lento). Es inherente a estos modelos."

---

### CLASE 5-6 (16-09 y 30-09-2025): Variational Autoencoders (VAEs)

#### Temas Principales
- Arquitectura Encoder-Decoder
- Espacio latente
- Reparametrization Trick
- ELBO (Evidence Lower Bound)
- β-VAE

#### Conceptos Clave

**1. Motivación**

**Limitaciones de autorregresivos**:
- Generación lenta (secuencial)
- No hay control sobre características de alto nivel

**Idea de VAEs**: Tener una **representación comprimida** donde podamos controlar características.

**Analogía del profesor**: "En lugar de describir una cara con 10,000 píxeles, usa 4 características: 'hombre', 'barba', 'lentes', 'joven'."

**2. Espacio Latente**

Vector de números reales (típicamente 10-100 dims) que **codifica** características de alto nivel.

Ejemplo visual (2D para graficar):
```
Espacio latente (z):

    z₂
     |
  2  |    7 7 7
  1  |  0 0 0
  0  |
 -1  |      1 1 1
 -2  |
     |_____________ z₁
        -2  0  3
```

**Propiedad deseada**: Puntos cercanos en z → imágenes similares.

**3. Arquitectura VAE**

```
ENCODER                  DECODER
Imagen → [CNN] → z → [CNN] → Imagen'

28×28    MLP   10D   MLP    28×28
```

**Objetivo**: Imagen' ≈ Imagen (reconstrucción)

**4. ¿Por qué "Variational"?**

**Diferencia clave**:

| Autoencoder Tradicional | VAE |
|------------------------|-----|
| z = E(x) (determinista) | z ~ N(μ(x), σ²(x)) (probabilístico) |
| Cada x → un único z | Cada x → distribución de z's |

**Razón**: Queremos **generar** muestreando z's aleatorios.

**Problema con determinista**: Los z's están "dispersos", muestrear z aleatorio puede caer en "huecos" → imagen sin sentido.

**Solución VAE**: Forzar z ~ N(0, I). El espacio latente está "poblado" uniformemente.

**5. Encoder en Detalle**

El encoder outputea **μ y σ**:

```
x → [Encoder] → μ(x), σ(x)
                  ↓
              z ~ N(μ(x), σ²(x))
```

Código PyTorch:
```python
class Encoder(nn.Module):
    def __init__(self, latent_dim=10):
        self.fc1 = nn.Linear(784, 400)
        self.fc_mu = nn.Linear(400, latent_dim)
        self.fc_logvar = nn.Linear(400, latent_dim)

    def forward(self, x):
        h = F.relu(self.fc1(x))
        mu = self.fc_mu(h)
        logvar = self.fc_logvar(h)
        return mu, logvar
```

**¿Por qué log(σ²)?** Para estabilidad (σ² siempre positiva, pero log puede ser cualquier real).

**6. Reparametrization Trick**

**Problema**: Si z = sample(N(μ, σ²)), no podemos hacer backprop (no diferenciable).

**Solución**:
```
1. Muestrea ε ~ N(0, 1) (fijo, sin gradiente)
2. Calcula z = μ + σ·ε (diferenciable en μ y σ)
```

Código:
```python
def reparametrize(mu, logvar):
    std = torch.exp(0.5 * logvar)
    eps = torch.randn_like(std)
    z = mu + std * eps
    return z
```

El gradiente fluye a través de μ y σ, no a través de ε.

**7. Decoder**

```python
class Decoder(nn.Module):
    def __init__(self, latent_dim=10):
        self.fc1 = nn.Linear(latent_dim, 400)
        self.fc2 = nn.Linear(400, 784)

    def forward(self, z):
        h = F.relu(self.fc1(z))
        x_recon = torch.sigmoid(self.fc2(h))
        return x_recon
```

**8. Función de Pérdida: ELBO**

**Dos componentes**:
```
Loss = L_reconstruction + L_KL
```

**L_reconstruction**: Qué tan bien reconstruimos
```
MSE(x, x') o BCE(x, x')
```

**L_KL**: Regularización del espacio latente
```
KL(N(μ(x), σ²(x)) || N(0, I))
```

**Fórmula cerrada para KL**:
```
KL = 0.5 × Σᵢ (μᵢ² + σᵢ² - log(σᵢ²) - 1)
```

**Código completo**:
```python
def vae_loss(x, x_recon, mu, logvar):
    recon_loss = F.binary_cross_entropy(x_recon, x, reduction='sum')
    kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return recon_loss + kl_loss
```

**9. Derivación del ELBO (Evidence Lower Bound)**

**Objetivo**: Maximizar log P(x), pero es intratable:
```
P(x) = ∫ P(x|z) P(z) dz  ← Integral intratable
```

**Solución**: Introducir distribución aproximada Q(z|x) (el encoder):

**Resultado (derivación en pizarrón)**:
```
log P(x) ≥ E_{z ~ Q(z|x)}[log P(x|z)] - KL(Q(z|x) || P(z))
           ↑                              ↑
        Reconstruction              Regularization
```

Esta es la **ELBO** (Evidence Lower Bound).

Maximizar ELBO = Minimizar -ELBO.

**10. β-VAE**

Variante con peso β en la KL:
```
Loss = Reconstruction + β × KL
```

- β = 1: VAE estándar
- β < 1: Prioriza reconstrucción
- β > 1: Prioriza regularización (espacio latente más "organizado")

**11. Generación**

```python
# Muestrea z del prior
z = torch.randn(batch_size, latent_dim)

# Decodifica
x_gen = decoder(z)
```

¡Una imagen completamente nueva en un solo forward pass!

#### Práctico VAE

**Dataset**: Fashion-MNIST (ropa)

**Tareas**:
1. Implementar Encoder (CNN → μ, log σ²)
2. Implementar reparametrization trick
3. Implementar Decoder (z → CNN → imagen)
4. Entrenar con ambas pérdidas
5. **Explorar espacio latente** (si latent_dim=2, graficar)
6. **Interpolación**: z₁ → z₂ linealmente, decodificar cada paso
7. Experimentar con diferentes β

---

### CLASE 7 (07-10-2025): GANs (Generative Adversarial Networks)

#### Temas Principales
- Juego adversarial: Generador vs Discriminador
- Función objetivo Min-Max
- Problemas: Mode Collapse, inestabilidad
- DCGAN (Deep Convolutional GAN)
- Conditional GANs

#### Conceptos Clave

**1. La Analogía del Falsificador**

El profesor comenzó con esta analogía:

"Imaginen un falsificador de billetes y un detective":
- **Falsificador (G)**: Intenta hacer billetes falsos convincentes
- **Detective (D)**: Intenta distinguir billetes reales de falsos

Ambos mejoran compitiendo. Al final, el falsificador hace billetes perfectos.

**2. Arquitectura GAN**

```
                GENERADOR (G)
                    ↓
    z ~ N(0,I) → [G] → Imagen falsa
                    ↓

    Imagen real ─┐
                 ├→ [DISCRIMINADOR D] → [0, 1]
    Imagen fake ─┘                      ↑
                                    "Real" o "Fake"
```

**G: Generador**
- Input: z ∈ ℝᵈ (ruido latente)
- Output: Imagen generada

**D: Discriminador**
- Input: Imagen (real o fake)
- Output: Probabilidad de ser real [0, 1]

**3. Función Objetivo (Minimax Game)**

```
min_G max_D V(D,G) = E_{x ~ P_data}[log D(x)] + E_{z ~ P_z}[log(1 - D(G(z)))]
                      ↑                         ↑
                  D acierta con reales      D detecta fakes
```

**Interpretación**:

**D quiere maximizar**:
- `log D(x)` cuando x es real → D(x) → 1
- `log(1 - D(G(z)))` cuando G(z) es fake → D(G(z)) → 0

**G quiere minimizar** (engañar a D):
- `log(1 - D(G(z)))` → D(G(z)) → 1

**4. Problema con la Pérdida Original**

Al inicio, G genera imágenes horribles → D(G(z)) ≈ 0 → log(1 - D(G(z))) ≈ 0 → gradientes pequeños.

**Solución práctica**: En lugar de `min log(1 - D(G(z)))`, usar `max log D(G(z))`.

Mismo punto óptimo, mejores gradientes.

**5. Algoritmo de Entrenamiento**

```
Para cada época:
    # Entrenar Discriminador (k pasos, típicamente k=1)
    Para k iteraciones:
        1. Muestrea m ruidos: {z¹, ..., zᵐ}
        2. Muestrea m imágenes reales: {x¹, ..., xᵐ}
        3. Genera imágenes fake: {x̃¹ = G(z¹), ..., x̃ᵐ = G(zᵐ)}
        4. Actualiza D maximizando:
           V_D = (1/m) Σ[log D(xⁱ) + log(1 - D(x̃ⁱ))]
        (Gradient ASCENT en D, G congelado)

    # Entrenar Generador
    1. Muestrea m ruidos: {z¹, ..., zᵐ}
    2. Actualiza G maximizando:
       V_G = (1/m) Σ[log D(G(zⁱ))]
    (Gradient ASCENT en G, D congelado)
```

**6. Implementación en PyTorch**

```python
# Definir redes
G = Generator(latent_dim=100, img_dim=784)
D = Discriminator(img_dim=784)

# Optimizadores separados
opt_G = torch.optim.Adam(G.parameters(), lr=0.0002)
opt_D = torch.optim.Adam(D.parameters(), lr=0.0002)

criterion = nn.BCELoss()

for epoch in range(num_epochs):
    for real_imgs in dataloader:
        batch_size = real_imgs.size(0)

        # Labels
        real_labels = torch.ones(batch_size, 1)
        fake_labels = torch.zeros(batch_size, 1)

        # ========== Entrenar D ==========
        # Con imágenes reales
        outputs_real = D(real_imgs)
        d_loss_real = criterion(outputs_real, real_labels)

        # Con imágenes fake
        z = torch.randn(batch_size, latent_dim)
        fake_imgs = G(z)
        outputs_fake = D(fake_imgs.detach())  # .detach() congela G
        d_loss_fake = criterion(outputs_fake, fake_labels)

        # Backprop D
        d_loss = d_loss_real + d_loss_fake
        opt_D.zero_grad()
        d_loss.backward()
        opt_D.step()

        # ========== Entrenar G ==========
        z = torch.randn(batch_size, latent_dim)
        fake_imgs = G(z)
        outputs = D(fake_imgs)  # Sin detach: queremos gradiente en G

        # "Engañar" a D: usar real_labels
        g_loss = criterion(outputs, real_labels)

        opt_G.zero_grad()
        g_loss.backward()
        opt_G.step()
```

**Detalle crítico**: `.detach()` al entrenar D para congelar G, pero NO al entrenar G.

**7. Problemas Comunes**

**a) Mode Collapse**

G aprende a generar **solo unos pocos tipos** de muestras.

Ejemplo: Entrenando en MNIST, solo genera 3's y 7's (ignora otros dígitos).

**Causa**: G encuentra un "truco" para engañar a D.

**Detección**: Generar 100 imágenes, si todas son similares → mode collapse.

**b) Vanishing Gradients**

Si D es "demasiado bueno" → D(G(z)) ≈ 0 siempre → gradientes de G desaparecen.

**c) Inestabilidad General**

Difícil encontrar equilibrio entre G y D. Pérdidas oscilan sin converger.

**Soluciones parciales**:
- Arquitecturas específicas (DCGAN)
- Normalización (Batch Norm, Spectral Norm)
- Learning rates cuidadosos
- Variantes: WGAN, LSGAN, StyleGAN

**8. DCGAN (Deep Convolutional GAN)**

**Innovaciones**:
- Usar convoluciones en lugar de fully-connected
- BatchNorm después de cada capa
- LeakyReLU en D, ReLU en G
- No usar pooling, usar strided convolutions
- Tanh en salida de G, Sigmoid en salida de D

**Arquitectura del Generador**:
```python
class Generator(nn.Module):
    def __init__(self, latent_dim=100):
        super().__init__()
        self.main = nn.Sequential(
            # z ∈ ℝ¹⁰⁰ → (128, 7, 7)
            nn.Linear(latent_dim, 128*7*7),
            nn.Unflatten(1, (128, 7, 7)),

            # (128, 7, 7) → (64, 14, 14)
            nn.ConvTranspose2d(128, 64, 4, 2, 1),
            nn.BatchNorm2d(64),
            nn.ReLU(),

            # (64, 14, 14) → (1, 28, 28)
            nn.ConvTranspose2d(64, 1, 4, 2, 1),
            nn.Tanh()
        )
```

**Arquitectura del Discriminador**:
```python
class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.main = nn.Sequential(
            # (1, 28, 28) → (64, 14, 14)
            nn.Conv2d(1, 64, 4, 2, 1),
            nn.LeakyReLU(0.2),

            # (64, 14, 14) → (128, 7, 7)
            nn.Conv2d(64, 128, 4, 2, 1),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),

            # (128, 7, 7) → 1
            nn.Flatten(),
            nn.Linear(128*7*7, 1),
            nn.Sigmoid()
        )
```

**9. Conditional GANs (cGANs)**

Extensión: Condicionar la generación en información adicional (ej: clase).

```
z + etiqueta → [G] → Imagen de esa clase
```

Ejemplo: Generar dígito "7" específicamente.

Implementación: Concatenar etiqueta (one-hot) con z en el input de G, y con x en el input de D.

#### Práctico GAN

**Dataset**: Fashion-MNIST o MNIST

**Tareas**:
1. Implementar G con ConvTranspose2d
2. Implementar D con Conv2d
3. Alternar entrenamiento G y D
4. Monitorear pérdidas de ambos
5. Generar imágenes cada N epochs
6. **Detectar mode collapse**: Generar 100 imágenes, analizar diversidad
7. Experimentar con:
   - Learning rates diferentes
   - Ratio de entrenamiento (k:1)
   - Arquitecturas

---

### CLASE 8-10 (14-10, 21-10, 28-10-2025): Modelos de Lenguaje y Difusión

#### PARTE A: Modelos de Lenguaje (LMs)

**Temas Principales**
- Definición formal de Language Model
- Tokenización (BPE, WordPiece)
- Arquitectura Transformer (repaso)
- Sampling strategies (Greedy, Top-K, Top-P, Temperatura)
- GPT-2

**Conceptos Clave**

**1. Definición Formal de LM**

Un Language Model es una función:
```
LM: Σ* → Δ(Σ ∪ {EOS})
```

Donde:
- Σ: Vocabulario (conjunto de tokens)
- Σ*: Todas las secuencias posibles
- Δ(X): Distribuciones de probabilidad sobre X
- EOS: End Of Sequence

**En palabras**: LM recibe secuencia de tokens → devuelve distribución sobre el siguiente token.

Ejemplo:
```
Input: "Hola, ¿cómo"
Output: {
  "estás": 0.7,
  "te": 0.15,
  "va": 0.1,
  "andas": 0.04,
  ...
}
```

**2. LM como Autoregresivo**

```
P(x₁, x₂, ..., xₙ) = P(x₁) × P(x₂|x₁) × ... × P(xₙ|x₁,...,xₙ₋₁)
```

**Generación**:
```
1. Sample x₁ ~ P(x₁)
2. Sample x₂ ~ P(x₂|x₁)
3. Sample x₃ ~ P(x₃|x₁,x₂)
...
```

**Observación crítica del profesor**: "El LM es **determinístico**. Para la misma entrada, siempre da la misma distribución. La **aleatoriedad** viene del sampling."

**3. Tokenización**

**¿Qué es un token?** NO necesariamente una palabra. Puede ser subpalabra.

**¿Por qué no palabras completas?**
- Vocabulario demasiado grande
- No maneja palabras nuevas
- Ineficiente

**Tokenizers modernos**: BPE, WordPiece, SentencePiece

**Ejemplos**:
```
Texto: "Supercalifragilisticexpialidocious"

GPT-2 tokenizer:
["Super", "cal", "ifrag", "ilistic", "exp", "ial", "idoc", "ious"]

BERT tokenizer:
["super", "##cal", "##ifr", "##ag", "##il", "##istic", ...]
```

**Propiedades**:
- Vocabulario: ~50K-100K tokens
- Tokens frecuentes = palabras completas
- Tokens raros = subpalabras
- Cada modelo tiene **su** tokenizer (no intercambiables)

**Código**:
```python
from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

text = "Hola, ¿cómo estás?"
tokens = tokenizer.encode(text)
print(tokens)  # [33814, 11, 25384, 66, 42933, ...]

decoded = tokenizer.decode(tokens)
print(decoded)  # "Hola, ¿cómo estás?"
```

**4. Arquitectura Transformer (Repaso)**

"La mayoría de LLMs usan Transformers. Solo un repaso rápido."

**Componentes**:

**a) Self-Attention**:
```
Q = W_q × X  (Query: ¿qué busco?)
K = W_k × X  (Key: ¿qué tengo?)
V = W_v × X  (Value: información)

Scores = (Q × K^T) / √d_k
Attention = softmax(Scores)
Output = Attention × V
```

**b) Causal Masking** (para LMs autorregresivos):
```
Scores con máscara:

     T1  T2  T3  T4
T1  [S  -∞  -∞  -∞]  ← T1 solo se ve a sí mismo
T2  [S   S  -∞  -∞]  ← T2 ve T1 y T2
T3  [S   S   S  -∞]  ← T3 ve T1, T2, T3
T4  [S   S   S   S]  ← T4 ve todos
```

Token en posición i **no puede ver el futuro** (j > i).

**c) Bloque Transformer**:
```
Input
  ↓
[Self-Attention] → Add & Norm
  ↓
[Feed-Forward]   → Add & Norm
  ↓
(× N layers)
  ↓
[Linear] → Logits
  ↓
[Softmax] → Probabilidades
```

**5. Estrategias de Sampling**

**a) Greedy Decoding**:
```python
next_token = argmax(probs)
```
Siempre el más probable. Determinístico, puede ser repetitivo.

**b) Sampling Directo**:
```python
next_token = torch.multinomial(probs, 1)
```
Muestrea de toda la distribución. Puede elegir tokens improbables.

**c) Top-K Sampling**:
```python
# Filtrar a los K más probables
top_k_probs, top_k_indices = torch.topk(probs, k)
top_k_probs = top_k_probs / top_k_probs.sum()  # Renormalizar
next_token = top_k_indices[torch.multinomial(top_k_probs, 1)]
```

Típicamente K=50. Reduce sorpresas, menos diversidad.

**d) Top-P (Nucleus) Sampling**:
```python
# Ordenar probabilidades
sorted_probs, sorted_indices = torch.sort(probs, descending=True)
cumsum_probs = torch.cumsum(sorted_probs, dim=-1)

# Incluir hasta que cumsum ≥ P
nucleus_mask = cumsum_probs <= p
nucleus_probs = sorted_probs[nucleus_mask]
nucleus_probs = nucleus_probs / nucleus_probs.sum()

next_token = sorted_indices[nucleus_mask][torch.multinomial(nucleus_probs, 1)]
```

Típicamente P=0.9. Más adaptativo que Top-K.

**e) Temperatura**:
```python
probs = softmax(logits / temperature)
```

- T < 1: Más determinista (distribución "afilada")
- T = 1: Sin cambios
- T > 1: Más aleatorio (distribución "plana")

**Ejemplo visual**:
```
Original (T=1):     {estás: 0.7, te: 0.2, va: 0.1}
Con T=0.5:          {estás: 0.9, te: 0.08, va: 0.02}
Con T=2.0:          {estás: 0.5, te: 0.3, va: 0.2}
```

**6. Uso Práctico: GPT-2**

```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model.eval()

prompt = "Once upon a time"
input_ids = tokenizer.encode(prompt, return_tensors="pt")

output = model.generate(
    input_ids,
    max_length=50,
    temperature=0.8,
    top_k=50,
    top_p=0.95,
    do_sample=True
)

text = tokenizer.decode(output[0], skip_special_tokens=True)
print(text)
```

**Parámetros importantes**:
- `max_length`: Longitud máxima
- `temperature`: Control de aleatoriedad
- `top_k`, `top_p`: Estrategias de sampling
- `do_sample=True`: Habilitar sampling (sino usa greedy)

---

#### PARTE B: Modelos de Difusión

**Temas Principales**
- Forward diffusion (agregar ruido)
- Reverse diffusion (quitar ruido)
- DDPM (Denoising Diffusion Probabilistic Models)
- Latent Diffusion (Stable Diffusion)
- Conditional Diffusion (texto → imagen)

**Conceptos Clave**

**1. La Idea Central**

```
Forward:  Imagen limpia → (+ruido gradual) → Ruido puro
Reverse:  Ruido puro   → (-ruido gradual) → Imagen limpia
```

Entrenamos la red para **predecir y quitar ruido**.

**Analogía del profesor**: "Imagina un dibujo que vas borrando poco a poco. Entrenar un modelo para 'des-borrar'."

**2. Forward Diffusion Process**

Dado x₀ (imagen original), agregar ruido en T pasos:

```
x_t = √(1-β_t) × x_{t-1} + √β_t × ε

donde ε ~ N(0, I)
```

**Proceso**:
```
x₀ (imagen) → x₁ → x₂ → ... → x_T (ruido puro)
```

**Propiedades**:
- β_t: "schedule" de ruido (cuánto agregar en paso t)
- β₁ < β₂ < ... < β_T (aumenta con t)
- Al final: x_T ≈ N(0, I)

**Fórmula cerrada** (puedes saltar pasos):
```
x_t = √(ᾱ_t) × x₀ + √(1-ᾱ_t) × ε

donde ᾱ_t = ∏ᵢ₌₁ᵗ (1-βᵢ)
```

**3. Reverse Diffusion Process**

**Objetivo**: Aprender x_{t-1} dado x_t.

Si conociéramos P(x_{t-1}|x_t), podríamos:
```
x_T ~ N(0,I)  (ruido)
x_{T-1} ~ P(x_{T-1}|x_T)
...
x_0  (imagen generada)
```

**Solución**: Aproximar con red neuronal ε_θ(x_t, t).

**4. ¿Qué Predice la Red?**

En lugar de predecir x_{t-1} directamente, predice **el ruido ε** agregado.

```
Red: ε_θ(x_t, t) → ε̂ (estimación del ruido)
```

**¿Por qué?** Más estable numéricamente.

**5. Función de Pérdida**

```
L(θ) = E_{x₀, t, ε} [||ε - ε_θ(x_t, t)||²]
```

Simplemente: ¿Qué tan bien predices el ruido agregado?

**Algoritmo de entrenamiento**:
```python
for epoch in range(num_epochs):
    # 1. Toma imagen real
    x_0 = sample_from_dataset()

    # 2. Elige paso aleatorio
    t = random.randint(1, T)

    # 3. Genera ruido y agrega
    epsilon = torch.randn_like(x_0)
    x_t = sqrt(alpha_bar[t]) * x_0 + sqrt(1 - alpha_bar[t]) * epsilon

    # 4. Predice ruido
    epsilon_pred = model(x_t, t)

    # 5. Pérdida
    loss = F.mse_loss(epsilon_pred, epsilon)

    # 6. Backprop
    loss.backward()
    optimizer.step()
```

**6. Generación**

**Algoritmo DDPM**:
```python
# 1. Empieza con ruido puro
x = torch.randn(batch_size, channels, height, width)

# 2. Itera T pasos hacia atrás
for t in reversed(range(T)):
    # Predice ruido
    epsilon_pred = model(x, t)

    # Remueve ruido
    alpha_t = alphas[t]
    alpha_bar_t = alphas_cumprod[t]

    mean = (1 / sqrt(alpha_t)) * (x - ((1 - alpha_t) / sqrt(1 - alpha_bar_t)) * epsilon_pred)

    if t > 0:
        sigma_t = sqrt(betas[t])
        x = mean + sigma_t * torch.randn_like(x)
    else:
        x = mean

# x es la imagen generada
```

**7. Arquitectura: U-Net**

```
ENCODER          DECODER
    ↓               ↑
[Conv] ─────────→ [ConvT]  ← Skip connection
    ↓               ↑
[Conv] ─────────→ [ConvT]
    ↓               ↑
[Conv] ─────────→ [ConvT]
    ↓
Attention layers
```

**Características**:
- **Skip connections**: Información de encoder → decoder
- **Time embedding**: t se codifica con sinusoidales y se inyecta en cada capa
- **Attention**: Dependencias de largo alcance

**8. Conditional Diffusion**

**Objetivo**: Generar imagen dado prompt de texto.

**Dos enfoques**:

**a) Classifier Guidance**:
```
ε̂_conditioned = ε̂_unconditioned - √(1-ᾱ_t) × ∇_{x_t} log p_φ(y|x_t)
```
Requiere clasificador separado.

**b) Classifier-Free Guidance** (más común):
```
ε̂ = w × ε_θ(x_t, t, c) + (1-w) × ε_θ(x_t, t, null)
```

donde:
- c: condición (ej: texto)
- null: sin condición
- w: guidance scale (típicamente 7.5)

**Entrenamiento**: Con probabilidad p (ej: 10%), reemplazar c por null.

**9. Latent Diffusion Models (Stable Diffusion)**

**Problema**: Diffusion en píxeles es costoso (512×512 = 262K dims).

**Solución**: Hacer diffusion en **espacio latente comprimido**.

```
Imagen (512×512×3)
    ↓
[VAE Encoder]
    ↓
Latent (64×64×4)  ← 64× más pequeño
    ↓
[Diffusion Model]  ← Aquí se hace el denoising
    ↓
Latent denoised
    ↓
[VAE Decoder]
    ↓
Imagen generada
```

**Ventajas**:
- 64× más rápido
- Misma calidad visual
- Menos memoria

**10. CLIP para Texto → Imagen**

**CLIP**: Contrastive Language-Image Pre-training

Aprende embeddings conjuntos de texto e imagen.

```
Texto → [CLIP Text Encoder] → Embedding texto
Imagen → [CLIP Image Encoder] → Embedding imagen

Similarity = cos(emb_texto, emb_imagen)
```

**Uso en Stable Diffusion**:
```
Prompt: "un gato astronauta"
    ↓
[CLIP Text Encoder]
    ↓
Text embeddings (77×768)
    ↓
[U-Net con Cross-Attention]  ← Embeddings condicionan la generación
    ↓
Latent denoised
    ↓
[VAE Decoder]
    ↓
Imagen del gato astronauta
```

**11. Comparación de Modelos Generativos**

| Modelo | Velocidad | Calidad | Diversidad | Controlabilidad |
|--------|-----------|---------|------------|-----------------|
| **GAN** | ⚡⚡⚡ (1 paso) | ⭐⭐⭐ | ⭐⭐ (mode collapse) | ⭐ |
| **VAE** | ⚡⭐⭐ (1 paso) | ⭐⭐ (borroso) | ⭐⭐⭐ | ⭐⭐ |
| **Autoreg** | ⚡ (n pasos) | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ |
| **Diffusion** | ⚡ (T pasos) | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Observación del profesor**: "Diffusion models dominan actualmente en generación de imágenes de alta calidad."

#### Prácticos

**Práctico LM (GPT-2)**:
1. Cargar tokenizer y modelo
2. Experimentar con diferentes prompts
3. Implementar Top-K y Top-P desde cero
4. Comparar temperaturas (0.3, 0.7, 1.0, 1.5)
5. Calcular Perplexity en texto de prueba
6. (Opcional) Fine-tune en dataset pequeño

**Práctico Diffusion**:
1. Implementar schedule de ruido (βs, ᾱs)
2. Implementar forward process
3. Implementar U-Net simple
4. Entrenar prediciendo ruido
5. Implementar reverse process
6. Generar imágenes desde ruido
7. Visualizar proceso paso a paso

---

### CLASE 11 (04-11-2025): Evaluación de Modelos Generativos

#### Temas Principales
- Desafíos en evaluación
- Métricas para imágenes (IS, FID)
- Métricas para texto (Perplexity, BLEU, ROUGE)
- Evaluación humana
- Downstream tasks

#### Conceptos Clave

**1. El Problema Fundamental**

"Evaluar modelos generativos es **difícil**."

**En clasificación**:
```
Predicción: "Gato"
Ground truth: "Gato"
Métrica: Accuracy = 100% ✓ Fácil
```

**En generación**:
```
Generado: [Imagen de gato]
¿Es bueno? 🤔
- ¿Se parece a un gato?
- ¿Es realista?
- ¿Es diferente a los datos de entrenamiento?
```

**Dos dimensiones principales**:
1. **Fidelidad**: ¿Qué tan realistas son las muestras?
2. **Diversidad**: ¿Cubren la variedad del dataset?

**Trade-off común**:
- Modelo A: 1's perfectos, nada más → Alta fidelidad, baja diversidad
- Modelo B: Todos los dígitos, borrosos → Alta diversidad, baja fidelidad

**2. Métricas de Distancia entre Distribuciones**

**a) KL Divergence**:
```
D_KL(P || Q) = ∫ P(x) log(P(x) / Q(x)) dx
```
- Asimétrica
- Penaliza fuertemente cuando Q subestima P

**b) Jensen-Shannon Divergence**:
```
D_JS(P || Q) = 0.5 × D_KL(P || M) + 0.5 × D_KL(Q || M)
donde M = 0.5(P + Q)
```
- Simétrica
- Usada implícitamente en GANs

**c) Wasserstein Distance** (Earth Mover's Distance):
- "Cuánto trabajo se necesita para transformar P en Q"
- Más estable en alta dimensión
- Usada en WGANs

**Problema común**: Todas requieren conocer P_data explícitamente (difícil).

**3. Métricas Basadas en Modelos Pre-entrenados**

**a) Inception Score (IS)**

**Idea**: Usar Inception Net (clasificador pre-entrenado) para evaluar.

```
IS = exp(E_x [D_KL(p(y|x) || p(y))])
```

**Interpretación**:
- **p(y|x) sharp** (distribución concentrada): Imagen clara, fácil de clasificar
- **p(y) flat** (distribución uniforme): Imágenes diversas

Alto IS = Imágenes claras y diversas.

**Limitaciones**:
- Solo funciona en dominio de Inception (ImageNet)
- No compara con datos reales

**b) Fréchet Inception Distance (FID)**

**Idea**: Comparar estadísticas de features de Inception.

**Algoritmo**:
1. Pasa imágenes reales por Inception → features → μ_real, Σ_real
2. Pasa imágenes generadas → features → μ_gen, Σ_gen
3. Calcula distancia Fréchet:

```
FID = ||μ_real - μ_gen||² + Tr(Σ_real + Σ_gen - 2√(Σ_real × Σ_gen))
```

**Interpretación**:
- **Bajo FID**: Mejor (distribuciones similares)
- **Alto FID**: Peor

**Valores típicos**:
- FID < 10: Excelente
- FID < 20: Muy bueno
- FID < 50: Aceptable
- FID > 100: Malo

**Ventaja sobre IS**: Compara directamente con datos reales.

**Código**:
```python
from pytorch_fid import fid_score

fid = fid_score.calculate_fid_given_paths(
    ['real_images/', 'generated_images/'],
    batch_size=50,
    device='cuda',
    dims=2048
)
print(f"FID: {fid:.2f}")
```

**c) CLIP Score** (para texto → imagen)

```
CLIP_Score = Similarity(CLIP_text(prompt), CLIP_image(img_gen))
```

¿Qué tan bien la imagen corresponde al prompt?

**4. Métricas para Texto**

**a) Perplexity (PPL)**

```
PPL = exp(-1/N × Σᵢ log P(wᵢ | w₁, ..., wᵢ₋₁))
```

**Interpretación**:
- **Baja PPL**: Modelo asigna alta probabilidad a secuencias reales
- **Alta PPL**: Modelo "sorprendido"

**Importante**: Mide qué tan bien el modelo modela el lenguaje, **NO** calidad del texto generado.

**Código**:
```python
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs, labels=inputs["input_ids"])
    loss = outputs.loss

perplexity = torch.exp(loss).item()
```

**b) BLEU (Bilingual Evaluation Understudy)**

**Idea**: Contar n-gramas comunes con referencia.

```
BLEU = BP × exp(Σₙ wₙ log(pₙ))
```

donde:
- pₙ: precisión de n-gramas
- BP: brevity penalty (penaliza textos cortos)

**Ejemplo**:
```
Referencia: "El gato negro duerme"
Generado:   "El gato duerme"

Unigramas coincidentes: "El", "gato", "duerme" → 3/3
Bigramas coincidentes: "El gato" → 1/2
```

**Limitación**: No captura sinonimia ("gato" vs "felino" → 0 match).

**c) ROUGE**

Similar a BLEU pero enfocado en **recall** (cobertura).

Usado más en resúmenes.

**d) BERTScore**

**Idea**: Usar embeddings de BERT para comparar semánticamente.

```
BERTScore = F1(cos_sim(embed_ref, embed_gen))
```

**Ventaja**: Captura similitud semántica, no solo léxica.

**5. Evaluación Humana**

**Técnicas**:

**a) A/B Testing**:
- Mostrar dos imágenes (modelos A y B)
- "¿Cuál prefieres?"
- Calcular win rate

**b) Likert Scale**:
- Mostrar imagen
- "¿Qué tan realista? (1-5)"
- Calcular promedio

**c) Turing Test**:
- Mezclar imágenes reales y generadas
- "¿Real o fake?"
- Calcular tasa de error

**Ventajas**:
- Captura percepción humana (gold standard)

**Desventajas**:
- Costoso ($$$)
- No escalable
- Subjetivo (varía entre evaluadores)

**6. Evaluación Orientada a Tareas (Downstream Tasks)**

**Idea**: Evaluar **utilidad** en tarea específica.

**Ejemplo 1: Data Augmentation**
```
1. Entrenar clasificador con datos reales: Accuracy = 85%
2. Entrenar con reales + sintéticos: Accuracy = 90%
→ Datos sintéticos son útiles (+5%)
```

**Ejemplo 2: Few-shot Learning**
```
1. Tarea con pocas muestras
2. LLM genera más ejemplos
3. Medir accuracy en test
→ ¿El LLM ayudó?
```

**Ventaja**: Métricas tangibles (accuracy, F1, etc.).

**7. Resumen de Métricas por Modelo**

| Modelo | Métricas Comunes |
|--------|------------------|
| **VAE** | ELBO, Reconstruction Loss, FID |
| **GAN** | Inception Score, FID, Precision/Recall |
| **Diffusion** | FID, CLIP Score, Human Preference |
| **LLM** | Perplexity, BLEU, ROUGE, Human Eval |

**8. Limitaciones Generales**

El profesor concluyó: "Ninguna métrica es perfecta. Evaluación de modelos generativos es un **problema abierto**."

**Problemas**:
- **Sesgo del modelo base**: FID depende de Inception (ImageNet)
- **Correlación imperfecta**: FID bajo ≠ siempre mejores imágenes
- **Trade-offs**: Fidelidad vs diversidad
- **Dependencia del dominio**: BLEU funciona en traducción, no en diálogo

**Recomendación práctica**:
1. Usar **múltiples métricas** automáticas
2. Complementar con **análisis cualitativo** (mirar las muestras)
3. Si es crítico, hacer **evaluación humana**
4. Considerar **downstream tasks** si es aplicable

---

## CONCEPTOS FUNDAMENTALES

### Probabilidad y Estadística

**Variable Aleatoria**: Función que mapea eventos a números reales.

**Distribución de Probabilidad**: Función que asigna probabilidades a valores.

**Regla del Producto**: P(X, Y) = P(X) × P(Y | X)

**Regla de la Suma**: P(X) = Σ_y P(X, Y)

**Independencia**: P(X, Y) = P(X) × P(Y)

**Independencia Condicional**: P(X, Z | Y) = P(X | Y) × P(Z | Y)

**Esperanza**: E[X] = Σ_x x × P(X = x)

### Distribuciones Comunes

**Bernoulli**: Variable binaria (0 o 1)
- P(X = 1) = θ
- P(X = 0) = 1 - θ

**Uniforme U(a, b)**: Todos los valores en [a, b] igualmente probables
- p(x) = 1/(b-a) si a ≤ x ≤ b

**Normal/Gaussiana N(μ, σ²)**: La "campana"
- p(x) = (1/σ√(2π)) exp(-(x-μ)²/(2σ²))
- μ: media, σ: desviación estándar

**Mixtura de Gaussianas**: Suma ponderada de Gaussianas
- p(x) = Σᵢ θᵢ N(x; μᵢ, σᵢ²)

### Conceptos de Deep Learning

**Red Neuronal**: Composición de funciones lineales y no lineales.

**Perceptrón**: Unidad básica σ(w·x + b)

**Sigmoid**: σ(x) = 1/(1 + e^(-x)), mapea a [0, 1]

**Softmax**: Convierte logits en probabilidades que suman 1
- softmax(x)ᵢ = exp(xᵢ) / Σⱼ exp(xⱼ)

**Backpropagation**: Algoritmo para calcular gradientes.

**Gradient Descent**: Optimización siguiendo el gradiente negativo.

**Overfitting**: Modelo memoriza entrenamiento pero falla en test.

### Funciones de Pérdida

**Binary Cross-Entropy (BCE)**: Para clasificación binaria
- BCE = -[y log(ŷ) + (1-y) log(1-ŷ)]

**Cross-Entropy**: Para clasificación multi-clase
- CE = -Σᵢ yᵢ log(ŷᵢ)

**Mean Squared Error (MSE)**: Para regresión
- MSE = (1/n) Σᵢ (yᵢ - ŷᵢ)²

**KL Divergence**: Diferencia entre distribuciones
- D_KL(P || Q) = Σ P(x) log(P(x) / Q(x))

### Conceptos de Modelos Generativos

**Autoregresivo**: Cada elemento depende de los anteriores.

**Espacio Latente**: Representación comprimida de datos.

**Encoder**: Comprime dato → código latente.

**Decoder**: Descomprime código → dato reconstruido.

**Reparametrization Trick**: z = μ + σ·ε para hacer sampling diferenciable.

**ELBO**: Evidence Lower Bound, objetivo de VAEs.

**Mode Collapse**: GAN genera solo pocos tipos de muestras.

**Forward Diffusion**: Agregar ruido gradualmente.

**Reverse Diffusion**: Quitar ruido gradualmente.

**Token**: Unidad mínima en modelos de lenguaje.

**Tokenizer**: Sistema que convierte texto ↔ tokens.

---

## DICCIONARIO

### A

**Adam**: Algoritmo de optimización (variante de SGD).

**Attention**: Mecanismo que permite a la red "enfocarse" en partes relevantes.

**Autoencoder**: Encoder + Decoder para comprimir y reconstruir.

**Autoregresivo**: Modelo donde cada salida depende de salidas anteriores.

### B

**Backpropagation**: Algoritmo para calcular gradientes en redes neuronales.

**Batch**: Conjunto de datos procesados simultáneamente.

**BatchNorm**: Normalización por batch para estabilizar entrenamiento.

**BCE (Binary Cross-Entropy)**: Pérdida para clasificación binaria.

**BERT**: Bidirectional Encoder Representations from Transformers.

**Bernoulli**: Distribución de probabilidad binaria.

**BLEU**: Métrica para evaluar texto generado.

**BPE (Byte-Pair Encoding)**: Algoritmo de tokenización.

### C

**Causal Masking**: Evitar que tokens vean el futuro en LMs.

**CLIP**: Contrastive Language-Image Pre-training.

**CNN (Convolutional Neural Network)**: Red con capas convolucionales.

**Conditional**: Dependiente de información adicional (ej: clase).

**Cross-Entropy**: Función de pérdida para clasificación.

### D

**DALL-E**: Modelo texto → imagen de OpenAI.

**DCGAN**: Deep Convolutional GAN.

**Decoder**: Red que reconstruye dato desde código latente.

**Discriminador**: Red en GAN que detecta datos falsos.

**Distribución**: Función de probabilidad.

**Downstream Task**: Tarea final para la que se usa el modelo.

### E

**ELBO**: Evidence Lower Bound, objetivo de VAEs.

**Embedding**: Representación vectorial densa.

**Encoder**: Red que comprime dato a código latente.

**Epoch**: Pasada completa por el dataset de entrenamiento.

**EOS**: End Of Sequence.

**Esperanza (Expectation)**: Valor promedio E[X].

### F

**FID**: Fréchet Inception Distance, métrica para imágenes.

**Fine-tuning**: Ajustar modelo pre-entrenado en nueva tarea.

**Forward Pass**: Pasar dato por la red hacia adelante.

### G

**GAN**: Generative Adversarial Network.

**Gaussiana (Normal)**: Distribución con forma de campana.

**Generador**: Red que crea datos nuevos.

**GMM**: Gaussian Mixture Model.

**GPT**: Generative Pre-trained Transformer.

**Gradient**: Vector de derivadas parciales.

**Greedy**: Estrategia que siempre elige la opción más probable.

### H

**Hiperparámetro**: Valor configurado antes de entrenar.

**Hugging Face**: Librería popular para Transformers.

### I

**Inception Score (IS)**: Métrica de calidad para imágenes.

**Independencia**: P(X, Y) = P(X) × P(Y).

**Inferencia**: Usar modelo entrenado para hacer predicciones.

### K

**KDE**: Kernel Density Estimation.

**KL Divergence**: Divergencia de Kullback-Leibler.

### L

**Latent Space**: Espacio de representación comprimida.

**LeakyReLU**: ReLU(x) = max(αx, x) con α pequeño.

**Learning Rate**: Tamaño del paso en optimización.

**Likelihood**: Verosimilitud P(data | model).

**LLM**: Large Language Model.

**Logits**: Salidas crudas de red antes de activación.

**Loss**: Función de pérdida a minimizar.

### M

**Marginalización**: Sumar sobre variable: P(X) = Σ_y P(X, Y).

**Maximum Likelihood**: Maximizar P(data | model).

**MLP**: Multi-Layer Perceptron.

**Mode Collapse**: Problema en GANs (baja diversidad).

**MSE**: Mean Squared Error.

### N

**N(μ, σ²)**: Distribución Normal/Gaussiana.

**NLL**: Negative Log-Likelihood.

**Normalización**: Escalar datos a rango estándar.

**Nucleus Sampling**: Top-P sampling.

### O

**Optimizer**: Algoritmo de optimización (Adam, SGD, etc.).

**Overfitting**: Memorizar entrenamiento, fallar en test.

### P

**Parámetro**: Peso aprendido por la red.

**Perceptrón**: Unidad básica σ(w·x + b).

**Perplexity**: Métrica para modelos de lenguaje.

**Píxel**: Punto individual en imagen.

**Posterior**: Distribución P(z | x).

**Prior**: Distribución inicial P(z).

**Prompt**: Texto inicial para generar con LM.

### R

**ReLU**: Rectified Linear Unit, max(0, x).

**Reparametrization Trick**: z = μ + σ·ε.

**RLHF**: Reinforcement Learning from Human Feedback.

**ROUGE**: Métrica para resúmenes de texto.

**Ruido**: Valores aleatorios (típicamente Gaussianos).

### S

**Sampling**: Muestrear de una distribución.

**SGD**: Stochastic Gradient Descent.

**Sigmoid**: σ(x) = 1/(1+e^(-x)).

**Softmax**: Convertir logits en probabilidades.

**Stable Diffusion**: Modelo de difusión en espacio latente.

**Stochastic**: Probabilístico, con aleatoriedad.

### T

**Temperatura**: Parámetro que controla aleatoriedad en sampling.

**Token**: Unidad mínima de texto.

**Tokenizer**: Convierte texto ↔ tokens.

**Top-K**: Sampling de K tokens más probables.

**Top-P**: Sampling de tokens hasta probabilidad acumulada P.

**Transformer**: Arquitectura basada en attention.

### U

**U-Net**: Arquitectura encoder-decoder con skip connections.

**Underfitting**: Modelo demasiado simple.

**Uniforme**: Distribución con todos valores igualmente probables.

### V

**VAE**: Variational Autoencoder.

**Validation**: Conjunto de datos para evaluar durante entrenamiento.

**Varianza**: σ², medida de dispersión.

**Verosimilitud (Likelihood)**: P(data | model).

### W

**Wasserstein**: Distancia entre distribuciones.

**Weight**: Peso de la red neuronal.

**WordPiece**: Algoritmo de tokenización.

### Z

**z**: Típicamente denota el espacio latente.

---

## GUÍA DE ESTUDIO

### Cronograma de Estudio (4 semanas)

**Semana 1: Fundamentos**
- [ ] Repasar probabilidad básica
- [ ] Entender regla del producto y suma
- [ ] Practicar con datasets simples
- [ ] Dominar conceptos de distribuciones

**Semana 2: Modelos Básicos**
- [ ] Autorregresivos: arquitectura de Hinton
- [ ] VAEs: reparametrization trick y ELBO
- [ ] Implementar ambos desde cero
- [ ] Comparar generación

**Semana 3: Modelos Avanzados**
- [ ] GANs: entrenamiento adversarial
- [ ] Diffusion: forward y reverse process
- [ ] LMs: tokenización y sampling
- [ ] Identificar problemas comunes

**Semana 4: Evaluación y Práctica**
- [ ] Dominar métricas (FID, BLEU, etc.)
- [ ] Resolver prácticos completos
- [ ] Preparar presentación obligatorio

### Temas Críticos para Dominar

**1. Probabilidad Condicional** (Base de TODO)
```
P(X, Y) = P(X) × P(Y | X)
```

**2. Autoregresión** (Concepto Central)
```
P(x₁, ..., xₙ) = ∏ᵢ P(xᵢ | x₁, ..., xᵢ₋₁)
```

**3. Reparametrization Trick** (Clave para VAEs)
```
z = μ + σ·ε  donde ε ~ N(0,1)
```

**4. Juego Adversarial** (Núcleo de GANs)
```
min_G max_D V(D, G)
```

**5. Denoising** (Esencia de Difusión)
```
Predecir ruido ε agregado en cada paso
```

### Checklist de Habilidades

**Conceptuales:**
- [ ] Explicar diferencia discriminativo vs generativo
- [ ] Justificar reparametrization trick en VAEs
- [ ] Describir mode collapse en GANs
- [ ] Explicar por qué diffusion es lento
- [ ] Comparar pros/cons de cada familia de modelos

**Técnicas:**
- [ ] Derivar pérdida de modelo autorregresivo
- [ ] Implementar ELBO con KL para Gaussianas
- [ ] Escribir algoritmo de entrenamiento de GAN
- [ ] Calcular FID dados embeddings
- [ ] Implementar Top-K y Top-P sampling

**Prácticas:**
- [ ] Entrenar VAE en MNIST/Fashion-MNIST
- [ ] Detectar mode collapse en GAN
- [ ] Generar texto con GPT-2
- [ ] Implementar diffusion simplificado
- [ ] Evaluar modelo con múltiples métricas

### Preguntas Tipo Examen

**Teóricas:**
1. ¿Cuál es la diferencia fundamental entre modelo discriminativo y generativo?
2. ¿Por qué usamos log-likelihood en lugar de likelihood directa?
3. Explique el ELBO y sus dos componentes.
4. ¿Qué es mode collapse y cómo detectarlo?
5. ¿Por qué predecir ruido en diffusion en lugar de x_{t-1}?

**Técnicas:**
1. Derive la BCE a partir de la Bernoulli.
2. Calcule KL divergence entre dos Gaussianas.
3. Escriba el algoritmo de entrenamiento alternado de GANs.
4. Implemente sampling con temperatura.

**Prácticas:**
1. Dado un VAE entrenado, genere 10 imágenes nuevas.
2. Detecte si una GAN colapsó viendo sus outputs.
3. Evalúe calidad de imágenes con FID.
4. Compare texto generado con diferentes temperaturas.

### Errores Comunes a Evitar

1. **Confundir P(X|Y) con P(Y|X)** - Son diferentes (Bayes)
2. **Olvidar .detach() en GANs** - Rompe el flujo de gradientes
3. **Usar β=1 sin experimentar en VAEs** - Puede no ser óptimo
4. **Ignorar mode collapse en GANs** - Revisar siempre diversidad
5. **Asumir FID bajo = mejor modelo** - Complementar con otras métricas

---

## RECURSOS

### Papers Fundamentales

**VAEs:**
- Kingma & Welling (2013): "Auto-Encoding Variational Bayes"

**GANs:**
- Goodfellow et al. (2014): "Generative Adversarial Networks"
- Radford et al. (2015): "Unsupervised Representation Learning with Deep Convolutional GANs" (DCGAN)

**Diffusion:**
- Sohl-Dickstein et al. (2015): "Deep Unsupervised Learning using Nonequilibrium Thermodynamics"
- Ho et al. (2020): "Denoising Diffusion Probabilistic Models" (DDPM)
- Rombach et al. (2022): "High-Resolution Image Synthesis with Latent Diffusion Models" (Stable Diffusion)

**Language Models:**
- Vaswani et al. (2017): "Attention is All You Need" (Transformers)
- Radford et al. (2019): "Language Models are Unsupervised Multitask Learners" (GPT-2)

**Evaluación:**
- Heusel et al. (2017): "GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium" (FID)

### Código y Librerías

**PyTorch**: Framework principal
- pytorch.org

**HuggingFace Transformers**: LMs pre-entrenados
- huggingface.co/transformers

**Datasets**:
- MNIST, Fashion-MNIST: `torchvision.datasets`
- CIFAR-10: `torchvision.datasets.CIFAR10`
- Iris: `sklearn.datasets.load_iris`

**Métricas**:
- FID: `pytorch-fid` (pip install pytorch-fid)
- BLEU: `nltk.translate.bleu_score`

### Recursos Online

**Tutoriales**:
- "The Illustrated Transformer" - Jay Alammar
- "Understanding Diffusion Models" - Lilian Weng
- distill.pub (artículos visuales)

**Comunidades**:
- Reddit: r/MachineLearning
- Papers with Code: paperswithcode.com

### Material del Curso

**Aulas**: Plataforma educativa ORT
- Slides de cada clase
- PDFs teóricos
- Referencias bibliográficas

**Nota del profesor**: "Los pizarrones de clase son únicos. Tomen fotos o notas de las explicaciones."

---

## OBLIGATORIO

### Información General

**Fecha de entrega**: 8 de diciembre, 21:00 horas (RÍGIDA)
**Formato**: ZIP o PDF, máximo 40MB
**Grupos**: Hasta 3 personas (mismo dictado)

### Presentaciones

**Fechas**: 11 y 18 de noviembre
**Duración**: 10 minutos por equipo
**Obligatoria**: No se puede perder (requisito para aprobar)

### Objetivo

Implementar una técnica generativa de interés personal:
- Prototipo funcional en caso acotado
- Justificar por qué es interesante
- Definir cómo evaluar el modelo

### Temas Sugeridos

**Recomendados**:
- Image captioning
- Language models y uso de LLMs
- Variantes de GANs (Conditional GANs)
- Variantes de VAEs
- Generación de audio (advertencia: difícil de evaluar)

**Otros temas**: Consultar con docentes previamente

### Requisitos

**Implementación**:
- Prototipo funcional (no producción)
- Dataset acotado pero representativo
- Código documentado

**Evaluación**:
- Definir métricas apropiadas
- Justificar elección de métricas
- Incluir evaluación cualitativa (ejemplos)

**Informe**:
- Introducción y motivación
- Metodología
- Resultados (cuantitativos + cualitativos)
- Conclusiones
- Referencias

### Uso de IA Generativa

**Permitido** con conciencia:
- No dejar que haga todo el trabajo
- Entender todo el código generado
- Documentar qué se usó y cómo

### Consejos del Profesor

1. **Elegir tema de interés genuino** (más motivación)
2. **Scope pequeño pero completo** (mejor pequeño y funcional que grande e incompleto)
3. **Negociar alcance con docentes** (usar horarios de consulta)
4. **Registrarse en planilla** (fecha límite: 6 de noviembre)
5. **Presentar temprano para feedback** (11 de noviembre mejor que 18)

### Criterios de Evaluación

**Técnico (60%)**:
- Correctitud de la implementación
- Calidad del código
- Elección apropiada de técnicas

**Evaluación (20%)**:
- Métricas apropiadas
- Análisis de resultados
- Comparaciones relevantes

**Presentación (20%)**:
- Claridad del informe
- Calidad de visualizaciones
- Presentación oral

---

## NOTA FINAL

Este documento resume **TODO** lo dictado en las 11 clases del curso de Inteligencia Artificial Generativa. Cada concepto está explicado desde cero asumiendo NO hay conocimiento previo.

Si algo no está claro, revisa:
1. La sección específica de esa clase
2. El diccionario técnico
3. Los conceptos fundamentales
4. Los prácticos relacionados

**Importante**: Este resumen complementa pero NO reemplaza:
- Asistir a clases
- Hacer los prácticos
- Leer los papers fundamentales
- Experimentar con código

**¡Éxito en el curso!**

---

*Documento compilado a partir de transcripciones completas de las 11 clases del curso (19/08/2025 - 04/11/2025)*
*Universidad ORT Uruguay - Profesor: Francisco - Ayudante: Juan Pedro Silva*