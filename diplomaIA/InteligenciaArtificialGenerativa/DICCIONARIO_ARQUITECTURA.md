# Diccionario de Arquitectura de Redes Neuronales

**Todos los términos de arquitectura que aparecen en el curso, explicados de forma simple.**

---

## Capas (Layers)

### Linear (Fully Connected / Dense)

Es la capa más básica de una red neuronal. Cada neurona de entrada se conecta con cada neurona de salida. Hace una multiplicación de matrices y suma un bias.

```
salida = entrada × pesos + bias
```

**Para qué sirve**: transformar un vector de un tamaño a otro. Por ejemplo, pasar de 784 valores a 400.

**Cuándo se usa en el curso**:
- En el encoder del VAE: `nn.Linear(784, 400)` — comprime la imagen aplanada
- En el generador de GAN: `nn.Linear(latent_dim, 128*7*7)` — expande el ruido antes de las convoluciones
- En el discriminador de GAN: al final, para dar un solo número (real/falso)
- En el FFN del Transformer: dos capas Linear seguidas dentro de cada bloque

---

### Conv2d (Convolución 2D)

En vez de conectar todo con todo (como Linear), una Conv2d desliza un filtro pequeño (kernel) sobre la imagen, detectando patrones locales como bordes, texturas o formas. La misma operación se aplica en cada posición de la imagen.

```
nn.Conv2d(canales_entrada, canales_salida, tamaño_kernel, stride, padding)
```

- **canales_entrada**: cuántos canales tiene la imagen (1 para blanco y negro, 3 para color)
- **canales_salida**: cuántos filtros diferentes queremos (cada filtro detecta un patrón distinto)
- **kernel**: el tamaño del filtro que se desliza (ej: 4×4)
- **stride**: cuántos píxeles se mueve el filtro en cada paso (stride=2 achica la imagen a la mitad)
- **padding**: cuántos píxeles de borde se agregan para controlar el tamaño de salida

**Para qué sirve**: extraer características de imágenes de forma eficiente. Reduce el tamaño espacial mientras aumenta la cantidad de canales (características detectadas).

**Cuándo se usa en el curso**:
- En el discriminador de DCGAN: `nn.Conv2d(1, 64, 4, 2, 1)` — va achicando la imagen y extrayendo features hasta llegar a un solo número
- En el encoder del VAE convolucional: comprime la imagen detectando patrones cada vez más abstractos

---

### ConvTranspose2d (Convolución Transpuesta / "Deconvolución")

Es la operación inversa de Conv2d. En vez de achicar la imagen, la **agranda**. El profesor lo explicó así: "son básicamente las convoluciones pero para el otro lado... expandiendo en vez de contraer."

```
nn.ConvTranspose2d(canales_entrada, canales_salida, tamaño_kernel, stride, padding)
```

Con stride=2, la imagen se agranda al doble en cada dimensión.

**Para qué sirve**: generar imágenes a partir de representaciones comprimidas. Es la pieza clave para "expandir" información.

**Cuándo se usa en el curso**:
- En el generador de DCGAN: arranca con un vector chiquito y lo va agrandando con ConvTranspose2d hasta llegar al tamaño de la imagen final
- En el decoder del VAE convolucional: expande el código latente de vuelta a una imagen

---

### Flatten

Convierte un tensor multidimensional en un vector de una sola dimensión. Si tenés una imagen de 128 canales × 7 × 7, Flatten la convierte en un vector de 128×7×7 = 6272 valores.

**Para qué sirve**: hacer la transición entre capas convolucionales y capas Linear. Las convoluciones trabajan con tensores 3D (canales × alto × ancho), pero Linear necesita un vector 1D.

**Cuándo se usa en el curso**:
- En el discriminador de DCGAN: después de las convoluciones, aplana todo para pasarlo por la capa Linear final

---

### Unflatten

La operación inversa de Flatten. Toma un vector 1D y lo reestructura en un tensor multidimensional.

```
nn.Unflatten(1, (128, 7, 7))
```

Esto toma un vector y lo convierte en un tensor de 128 canales × 7 × 7.

**Para qué sirve**: hacer la transición inversa — de un vector 1D a un tensor 3D, para que las ConvTranspose2d puedan trabajar.

**Cuándo se usa en el curso**:
- En el generador de DCGAN: después de la capa Linear, se hace Unflatten para poder empezar a aplicar ConvTranspose2d

---

### Embedding

Convierte un índice (un número entero) en un vector de números decimales. Es una tabla de búsqueda: el índice 42 se traduce al vector que está en la fila 42 de la tabla. Esos vectores se entrenan junto con el modelo.

```
nn.Embedding(tamaño_vocabulario, dimensión_embedding)
```

**Para qué sirve**: representar elementos discretos (palabras, tokens) como vectores continuos que la red pueda procesar.

**Cuándo se usa en el curso**:
- En los language models: cada token del vocabulario tiene su embedding
- En CLIP: texto e imágenes se convierten a embeddings para poder compararlos
- En difusión condicional: el timestep t se codifica como embedding

---

## Funciones de Activación

### Sigmoid (σ)

Toma cualquier número y lo aplasta al rango [0, 1]. Números muy grandes → cerca de 1. Números muy negativos → cerca de 0.

```
σ(x) = 1 / (1 + e^(-x))
```

**Para qué sirve**: producir una salida que se interprete como **probabilidad** (entre 0 y 1).

**Cuándo se usa en el curso**:
- En la salida del discriminador de GAN: "¿creo que es real (1) o falsa (0)?"
- En el modelo autorregresivo de Hinton: la salida de cada perceptrón es P(píxel=1)
- Distinción importante: en WGAN el crítico **NO** tiene sigmoid al final (da cualquier número, no una probabilidad)

---

### ReLU (Rectified Linear Unit)

La activación más simple: si el número es positivo, lo deja igual. Si es negativo, lo convierte en 0.

```
ReLU(x) = max(0, x)
```

**Para qué sirve**: introducir no-linealidad (que la red pueda aprender patrones complejos, no solo líneas rectas) de forma muy eficiente.

**Cuándo se usa en el curso**:
- En las capas intermedias del generador de DCGAN
- En capas ocultas de MLPs
- En el FFN del Transformer (como alternativa a GELU)

---

### LeakyReLU

Como ReLU, pero en vez de dar exactamente 0 para valores negativos, deja pasar una señal muy chiquita (típicamente 0.2 veces el valor).

```
LeakyReLU(x) = x         si x > 0
LeakyReLU(x) = 0.2 × x   si x ≤ 0
```

**Para qué sirve**: evitar el problema de "neuronas muertas" de ReLU (cuando una neurona siempre recibe valores negativos, con ReLU nunca vuelve a activarse; con LeakyReLU siempre pasa algo de señal).

**Cuándo se usa en el curso**:
- En el discriminador de DCGAN: "Usa LeakyReLU (pendiente 0.2)"
- La razón de usar LeakyReLU en el discriminador y ReLU en el generador es una guía establecida de DCGAN

---

### Tanh (Tangente Hiperbólica)

Aplasta cualquier número al rango [-1, 1]. Parecida a sigmoid pero centrada en 0.

```
Tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))
```

**Para qué sirve**: producir salidas en el rango [-1, 1], que es útil cuando los datos están normalizados a ese rango.

**Cuándo se usa en el curso**:
- En la última capa del generador de DCGAN: "la última que usa Tanh para producir valores en [-1, 1]"
- Los datos de imagen se normalizan a [-1, 1] para que coincidan con el rango de Tanh

---

### Softmax

Toma un vector de números cualesquiera (llamados logits) y los convierte en probabilidades que suman 1. Los valores más grandes se convierten en probabilidades más altas.

```
softmax(xᵢ) = e^(xᵢ) / Σ e^(xⱼ)
```

**Para qué sirve**: cuando necesitás elegir **una** opción entre muchas (como la siguiente palabra entre todo el vocabulario).

**Cuándo se usa en el curso**:
- En language models: convierte los logits en probabilidades sobre todo el vocabulario
- En el mecanismo de atención del Transformer: convierte los scores de atención en pesos que suman 1
- En Inception Score: la red Inception Net usa softmax para clasificar

---

### GELU (Gaussian Error Linear Unit)

Similar a ReLU pero con una transición suave en vez de un corte abrupto en 0. Multiplica cada valor por la probabilidad de que una gaussiana lo considere "positivo".

**Para qué sirve**: lo mismo que ReLU pero con mejores resultados en la práctica para modelos grandes (Transformers).

**Cuándo se usa en el curso**:
- En GPT-2: usa GELU en vez de ReLU en el FFN
- En general, los Transformers modernos prefieren GELU

---

## Normalización

### BatchNorm (Batch Normalization)

Toma un lote (batch) de datos y normaliza cada canal para que tenga media 0 y varianza 1. Después aplica una escala y un desplazamiento entrenables.

**Para qué sirve**: estabiliza y acelera el entrenamiento. Sin BatchNorm, los valores internos de la red pueden crecer o achicarse de forma descontrolada, haciendo el entrenamiento inestable.

**Cuándo se usa en el curso**:
- En DCGAN: "BatchNorm después de cada capa" (tanto en generador como en discriminador, excepto la primera capa del discriminador y la última del generador)
- Distinción importante: en WGAN-GP **no** se usa BatchNorm en el crítico (porque la gradient penalty necesita que cada muestra se procese de forma independiente, y BatchNorm mezcla información entre muestras del batch)

---

### LayerNorm (Layer Normalization)

Normaliza cada muestra individualmente (no sobre el batch como BatchNorm, sino sobre todas las features de una sola muestra).

**Para qué sirve**: lo mismo que BatchNorm pero funciona bien cuando el tamaño del batch es chico o variable, y cuando cada muestra debe procesarse de forma independiente.

**Cuándo se usa en el curso**:
- En el Transformer: cada bloque tiene LayerNorm después de la atención y después del FFN ("Add & Norm")
- En WGAN-GP: como reemplazo de BatchNorm en el crítico

---

### InstanceNorm (Instance Normalization)

Normaliza cada canal de cada muestra por separado (más granular que LayerNorm).

**Cuándo se usa en el curso**:
- Como alternativa a BatchNorm en WGAN-GP: "WGAN-GP debe usar InstanceNorm o LayerNorm (NO BatchNorm)"

---

## Mecanismos de Atención

### Self-Attention (Auto-atención)

Cada elemento de la secuencia "mira" a todos los demás para decidir cuáles son relevantes para entenderlo. Es lo que permite al Transformer capturar dependencias de largo alcance.

Cada token genera tres vectores:
- **Query (Q)**: "¿qué información estoy buscando?"
- **Key (K)**: "¿qué información tengo para ofrecer?"
- **Value (V)**: "esta es mi información concreta"

Se calcula un puntaje entre cada par de tokens (Q × K), se normaliza con softmax, y se usa para ponderar los Values.

```
Attention(Q, K, V) = softmax(Q × K^T / √d_k) × V
```

El √d_k es para evitar que los puntajes crezcan demasiado cuando la dimensión es grande.

**Para qué sirve**: que cada palabra entienda su contexto. En "El gato se sentó porque estaba cansado", self-attention permite que "estaba" preste atención a "gato" para saber quién estaba cansado.

**Cuándo se usa en el curso**:
- En cada bloque del Transformer
- En la U-Net de difusión condicional (cross-attention con el texto)

---

### Multi-Head Attention

En vez de tener un solo mecanismo de atención, se tienen varios (ej: 12) en paralelo. Cada "cabeza" puede enfocarse en un aspecto diferente.

```
MultiHead = Concatenar(head_1, head_2, ..., head_h) × W_o
```

**Para qué sirve**: capturar múltiples tipos de relaciones simultáneamente. Una cabeza puede capturar gramática, otra el tema, otra la posición, etc.

**Cuándo se usa en el curso**:
- En el Transformer: cada bloque tiene Multi-Head Attention

---

### Cross-Attention

Igual que Self-Attention, pero el Query viene de una secuencia y el Key/Value vienen de otra secuencia diferente.

**Para qué sirve**: conectar dos secuencias distintas. Por ejemplo, que el decoder "mire" lo que procesó el encoder.

**Cuándo se usa en el curso**:
- En el Transformer completo (encoder-decoder): el decoder usa cross-attention para mirar la salida del encoder
- En Stable Diffusion: la U-Net usa cross-attention para incorporar la información del texto (embeddings de CLIP)

---

### Causal Masking (Máscara Causal)

Pone -infinito en las posiciones futuras de la matriz de atención, de forma que después del softmax esas posiciones se conviertan en 0. Resultado: cada token solo puede ver los tokens anteriores.

**Para qué sirve**: impedir que el modelo "haga trampa" mirando el futuro durante el entrenamiento. Al generar, el futuro todavía no existe, así que el modelo tiene que aprender sin verlo.

**Cuándo se usa en el curso**:
- En todos los language models autorrregresivos (GPT, etc.)
- Es la misma idea que la matriz triangular de Hinton pero implementada de otra forma

---

## Arquitecturas Completas

### Autoencoder

Dos redes conectadas: un **encoder** que comprime los datos a una representación chiquita (código latente), y un **decoder** que intenta reconstruir los datos originales a partir de esa representación.

```
Imagen → [Encoder] → código latente Z → [Decoder] → Imagen reconstruida
```

**Para qué sirve**: aprender una representación comprimida de los datos. El cuello de botella fuerza a la red a capturar solo lo esencial.

**Limitación**: no sirve directamente para generar porque el espacio latente no está estructurado (inventar un Z al azar probablemente caiga en una zona que el decoder nunca vio).

---

### VAE (Variational Autoencoder)

Autoencoder donde el encoder no da un punto fijo sino los parámetros de una campana gaussiana (μ y σ). Z se muestrea de esa campana. El loss fuerza que las campanas se parezcan a N(0,1).

**Para qué sirve**: generar datos nuevos en un solo paso. Al forzar el espacio latente a ser gaussiano, podemos muestrear de N(0,1) y el decoder genera algo coherente.

---

### U-Net

Red con forma de U: un encoder que achica progresivamente, un decoder que agranda progresivamente, y **skip connections** que conectan cada nivel del encoder con el nivel correspondiente del decoder.

```
Encoder:  [64] → [128] → [256] → [512]  (achica)
                                    ↓
Decoder:  [64] ← [128] ← [256] ← [512]  (agranda)
           ↑       ↑       ↑
         skip    skip    skip  (pasan información directa)
```

Además, recibe el timestep t como entrada (codificado con funciones sinusoidales, similar al positional encoding del Transformer).

**Para qué sirve**: predecir el ruido en modelos de difusión. Las skip connections permiten preservar detalles finos que se perderían en la compresión.

**Cuándo se usa en el curso**:
- En DDPM / difusión: es la arquitectura principal que predice el ruido

---

### Transformer

Arquitectura basada enteramente en mecanismos de atención (sin recurrencia ni convoluciones). Procesa toda la secuencia en paralelo.

Cada bloque tiene:
1. Multi-Head Self-Attention
2. Add & Norm (conexión residual + LayerNorm)
3. Feed-Forward Network (dos capas Linear con activación)
4. Add & Norm

**Para qué sirve**: procesar secuencias capturando dependencias de largo alcance de forma eficiente.

**Cuándo se usa en el curso**:
- GPT-2: Transformer decoder-only para generar texto
- En Stable Diffusion: la U-Net incorpora bloques de atención tipo Transformer

---

### Feed-Forward Network (FFN)

Dentro de cada bloque del Transformer: un MLP de dos capas que se aplica a cada posición por separado.

```
FFN(x) = Linear₂(activación(Linear₁(x)))
```

Va de dimensión D_model → D_ff (más grande, típicamente 4×) → D_model.

**Para qué sirve**: agregar capacidad de procesamiento no-lineal después de la atención. La atención mezcla información entre posiciones; el FFN procesa cada posición individualmente.

---

## Conceptos de Arquitectura

### Skip Connections (Conexiones Residuales)

En vez de que la salida de una capa sea solo su propia salida, se le **suma** la entrada original:

```
salida = capa(x) + x
```

**Para qué sirve**: permitir que los gradientes fluyan directamente a través de la red sin degradarse. Sin skip connections, las redes muy profundas sufren de vanishing gradients (los gradientes se hacen tan pequeños que las primeras capas no aprenden).

**Cuándo se usa en el curso**:
- En la U-Net de difusión (skip connections entre encoder y decoder)
- En cada bloque del Transformer ("Add & Norm" = residual + normalización)
- Concepto de ResNet mencionado como referencia

---

### Cuello de Botella (Bottleneck)

La parte más estrecha de una red encoder-decoder. Fuerza a la información a pasar por una representación comprimida.

**Para qué sirve**: si la red logra reconstruir bien pasando por el cuello de botella, significa que esa representación comprimida captura la información esencial.

**Cuándo se usa en el curso**:
- En el VAE: el espacio latente Z es el cuello de botella
- En la U-Net: la parte central más comprimida

---

### Positional Encoding (Codificación Posicional)

Como el Transformer procesa toda la secuencia de golpe (en paralelo), no tiene noción inherente de orden. El positional encoding le agrega información de posición sumando vectores que codifican "esta es la posición 1", "esta es la posición 2", etc.

Se usan funciones seno y coseno de distintas frecuencias para generar estos vectores.

**Para qué sirve**: que el modelo sepa en qué orden están las palabras. Sin esto, "el gato comió el ratón" y "el ratón comió el gato" serían indistinguibles.

**Cuándo se usa en el curso**:
- En el Transformer (sumado a los embeddings de entrada)
- En la U-Net de difusión: el timestep t se codifica con sinusoidales de forma análoga

---

### Stride

En una convolución, es cuántos píxeles se mueve el filtro en cada paso.

- **Stride 1**: el filtro se mueve de a 1 píxel → la salida tiene casi el mismo tamaño
- **Stride 2**: el filtro se mueve de a 2 píxeles → la salida tiene la mitad del tamaño

**Para qué sirve**: controlar cuánto se achica (o agranda, en ConvTranspose2d) la imagen.

**Cuándo se usa en el curso**:
- En DCGAN: se usan strided convolutions en vez de pooling (guía de DCGAN: "No usar pooling, usar strided convolutions")

---

### Padding

Píxeles extra que se agregan alrededor del borde de la imagen antes de aplicar la convolución.

**Para qué sirve**: controlar el tamaño de la salida. Sin padding, cada convolución achica un poco la imagen. Con padding adecuado, se puede mantener el tamaño.

---

### Kernel (Filtro)

El filtro pequeño que se desliza sobre la imagen en una convolución. Típicamente de 3×3 o 4×4. Sus valores se entrenan.

**Para qué sirve**: detectar patrones locales. Un kernel puede aprender a detectar bordes verticales, otro bordes horizontales, otro texturas, etc.

---

### Pooling / MaxPool

Reduce el tamaño de la imagen tomando el valor máximo (MaxPool) o el promedio (AvgPool) de cada región.

**Cuándo se usa en el curso**:
- En el encoder del VAE convolucional: `Conv2d + ReLU + MaxPool`
- En DCGAN: explícitamente **no** se usa — "No usar pooling, usar strided convolutions"

---

## Técnicas de Entrenamiento

### .detach()

Operación de PyTorch que corta la conexión de gradientes. El tensor resultante ya no tiene historial de operaciones, así que backpropagation no puede pasar a través de él.

**Para qué sirve**: controlar qué red se actualiza y cuál no.

**Cuándo se usa en el curso**:
- Al entrenar el discriminador de GAN: `D(G(z).detach())` — se corta el gradiente para que solo D se actualice, no G
- Al entrenar el generador: **no** se usa .detach(), para que los gradientes sí lleguen a G

---

### Label Flip

Truco donde se le dice al sistema que las imágenes falsas son reales (label=1) cuando se entrena el generador.

**Para qué sirve**: produce gradientes más útiles al inicio del entrenamiento, cuando el generador todavía genera basura. No es "mentir" — es un truco matemático que da la misma dirección de optimización pero con gradientes más grandes.

---

### Weight Clipping (Recorte de Pesos)

Después de cada paso de entrenamiento, se recortan todos los pesos de la red a un rango fijo (ej: [-0.01, 0.01]).

**Para qué sirve**: forzar que el crítico de WGAN cumpla la condición de Lipschitz (que no cambie su salida demasiado rápido).

**Cuándo se usa en el curso**:
- En WGAN original. Reemplazado por gradient penalty en WGAN-GP porque weight clipping "es una solución burda que limita la capacidad del crítico"

---

### Gradient Penalty

En vez de recortar pesos, se agrega un término al loss que penaliza cuando la norma del gradiente del crítico no es 1.

**Para qué sirve**: una forma más elegante de forzar la condición de Lipschitz en WGAN-GP.

---

### Backpropagation

Algoritmo para calcular cómo cada parámetro de la red contribuye al error. Recorre la red de atrás hacia adelante, calculando derivadas paso a paso.

**Para qué sirve**: saber en qué dirección mover cada peso para reducir el error.

**Problema en el curso**: el muestreo aleatorio del VAE no es diferenciable → solución: Reparametrization Trick.

---

## Optimizadores

### Adam

El optimizador más usado en el curso. Variante de SGD que adapta la tasa de aprendizaje para cada parámetro individualmente, usando promedios móviles del gradiente y su cuadrado.

```python
torch.optim.Adam(model.parameters(), lr=0.0002, betas=(0.5, 0.999))
```

**Cuándo se usa en el curso**:
- En DCGAN, VAE, WGAN-GP, y la mayoría de los modelos

---

### SGD (Stochastic Gradient Descent)

El optimizador más básico: mover los pesos en la dirección contraria al gradiente, multiplicado por la tasa de aprendizaje.

**Cuándo se usa en el curso**:
- En vanilla GAN original (con momentum)

---

### RMSprop

Optimizador que adapta la tasa de aprendizaje dividiendo por un promedio móvil de los gradientes al cuadrado.

**Cuándo se usa en el curso**:
- En WGAN original: `RMSprop, lr=5e-5`

---

## Términos de PyTorch

### nn.Module

Clase base de PyTorch para definir redes neuronales. Toda red hereda de `nn.Module`.

### nn.Sequential

Contenedor que aplica capas en orden, una tras otra. Útil para redes simples donde los datos fluyen en línea recta.

```python
nn.Sequential(
    nn.Linear(784, 400),
    nn.ReLU(),
    nn.Linear(400, 20)
)
```

### loss.backward()

Ejecuta backpropagation: calcula los gradientes de todos los parámetros respecto al loss.

### optimizer.zero_grad()

Pone todos los gradientes en cero antes de calcular nuevos. Necesario porque PyTorch acumula gradientes por defecto.

### optimizer.step()

Actualiza los pesos usando los gradientes calculados por `backward()`.

### torch.bernoulli

Muestrea 0 o 1 según una probabilidad dada. Ejemplo: si la probabilidad es 0.7, da 1 el 70% de las veces.

**Cuándo se usa en el curso**:
- En el modelo autorregresivo de Hinton: `torch.bernoulli(probs[:, pixel])` — genera cada píxel como 0 o 1

### torch.multinomial

Muestrea un índice de una distribución de probabilidades. Ejemplo: si las probabilidades son [0.1, 0.3, 0.6], da el índice 2 el 60% de las veces.

**Cuándo se usa en el curso**:
- En language models: para elegir el siguiente token según las probabilidades de softmax

### torch.tril

Crea una matriz triangular inferior (ceros arriba de la diagonal).

**Cuándo se usa en el curso**:
- En el modelo autorregresivo de Hinton: `self.mask = torch.tril(torch.ones(n, n), diagonal=-1)` — la máscara que impide que cada píxel vea los posteriores
- En causal masking del Transformer: para generar la máscara de atención

---

## Resumen visual: qué se usa en cada modelo

| Componente | Hinton | VAE | DCGAN | LM/Transformer | Difusión |
|---|---|---|---|---|---|
| Linear | ✓ | ✓ | ✓ | ✓ | |
| Conv2d | | ✓* | ✓ (en D) | | ✓ (U-Net) |
| ConvTranspose2d | | ✓* | ✓ (en G) | | ✓ (U-Net) |
| Sigmoid | ✓ | | ✓ (en D) | | |
| ReLU | | ✓ | ✓ (en G) | ✓ (FFN) | ✓ |
| LeakyReLU | | | ✓ (en D) | | |
| Tanh | | | ✓ (en G) | | |
| Softmax | | | | ✓ | |
| BatchNorm | | | ✓ | | |
| LayerNorm | | | | ✓ | |
| Self-Attention | | | | ✓ | |
| Cross-Attention | | | | | ✓ (cond.) |
| Skip Connections | | | | ✓ (residual) | ✓ (U-Net) |
| Embedding | | | | ✓ | ✓ (timestep) |

*\* En la versión convolucional del VAE*

---

*Compilado a partir de las transcripciones, prácticos, teoría y exámenes del curso de IA Generativa (ORT 2025).*
