# Explicación de Temas - Clase del 28-10-2025

## La Gran Pregunta: ¿Qué Estamos Construyendo?

Esta clase introduce los **Modelos de Difusión** (Diffusion Models), que son la tecnología detrás de herramientas como DALL-E 2, Stable Diffusion y Midjourney. Estos modelos representan el **estado del arte** en generación de imágenes.

Como dijo el profesor: "Hace tres, cuatro años, imaginarse que una IA podía hacer algo de esto era realmente una locura."

---

## Conexión con las Clases Anteriores

### ¿Qué Vimos Antes?

En clases anteriores vimos otros modelos generativos:
- **GANs** (Generative Adversarial Networks): Dos redes que compiten
- **VAEs** (Variational Autoencoders): Encoder comprime, decoder reconstruye

### ¿Por Qué Ahora Difusión?

Los modelos de difusión son una **tercera familia** de modelos generativos que resuelve problemas de los anteriores:
- Más **estables** de entrenar que GANs
- Generan imágenes de **mayor calidad** que VAEs
- Producen **más diversidad** en las generaciones

---

## Los Modelos de Difusión: La Idea Central

### ¿Qué es un Modelo de Difusión?

Es un modelo que aprende a generar imágenes partiendo de **ruido puro** y **limpiándolo poco a poco** hasta obtener una imagen clara.

### La Analogía Más Simple

Imagina que tienes una foto clara:
1. Le agregas "estática de TV" (ruido) poco a poco
2. Después de muchos pasos, solo queda estática
3. El modelo aprende a hacer lo **inverso**: partir de estática y llegar a una foto

```
FORWARD (Arruinar):
Foto clara → Un poco de ruido → Más ruido → ... → Solo ruido

REVERSE (Generar):
Solo ruido → Menos ruido → Aún menos → ... → Foto clara
```

### ¿Por Qué Se Llama "Difusión"?

El nombre viene de la física. En termodinámica, la difusión es cuando las cosas se desordenan naturalmente (como una gota de tinta expandiéndose en agua). Estos modelos hacen lo contrario: **crean orden desde el desorden**.

### Diferencia Clave con VAEs y GANs

| Modelo | Espacio Latente | Proceso |
|--------|-----------------|---------|
| **VAE** | Más pequeño que la imagen | Comprimir → Expandir |
| **GAN** | Más pequeño que la imagen | Vector → Imagen |
| **Difusión** | **Mismo tamaño** que la imagen | Ruido → Imagen paso a paso |

El profesor lo explicó así:
> "El dato tiene la misma estructura que el latente. Si generas imagen de 10×10, el latente es 10×10."

---

## El Proceso Forward: Agregar Ruido

### ¿Qué Es?

Es el proceso de **destruir** gradualmente una imagen agregándole ruido hasta que no se reconoce nada.

### Paso a Paso

```
x₀ = Imagen original (foto de un gato)
x₁ = Imagen + poquito de ruido (gato un poco borroso)
x₂ = Imagen + más ruido (gato difícil de ver)
...
xₜ = Solo ruido (no se ve nada)
```

### Características Importantes

**1. No requiere entrenamiento:**
- Es pura matemática
- Solo agregas ruido gaussiano (ruido "normal")
- Puedes programarlo con una fórmula simple

**2. Es gradual:**
- No arruinas la imagen de golpe
- Típicamente son **T = 1000 pasos**
- Cada paso agrega un poquito de ruido

**3. Al final llegas a ruido puro:**
- Ruido gaussiano con media 0 y varianza 1
- Como estática de televisión
- Se llama "ruido isotrópico"

### La Fórmula del Forward

```
q(xₜ | xₜ₋₁) = Normal(√(1-βₜ) × xₜ₋₁, βₜ × I)
```

**En español:**
- Tomas la imagen del paso anterior (xₜ₋₁)
- La "achicas" multiplicando por √(1-βₜ)
- Le sumas ruido gaussiano con varianza βₜ

---

## El Schedule de β (Beta): Cuánto Ruido Agregar

### ¿Qué Es β?

Es un número entre 0 y 1 que dice **cuánto ruido agregar en cada paso**.
- β pequeño = poco ruido
- β grande = mucho ruido

### El Schedule (Cronograma)

Es la secuencia β₁, β₂, β₃, ..., βₜ que define cuánto ruido agregar en cada paso.

**El profesor explicó:**
> "El programa de varianza es un conjunto de hiperparámetros que nos dicen cuánto ruido voy a agregar en cada paso."

### Tipos de Schedule

| Tipo | Descripción | Comportamiento |
|------|-------------|----------------|
| **Lineal** | β crece de forma constante | Más usado, recomendado |
| **Cuadrático** | β crece más rápido al final | A veces mejor |
| **Constante** | β siempre igual | No recomendado |

### Valores del Paper Original (DDPM)

- **T = 1000 pasos**
- **β₁ = 0.0001** (casi nada de ruido al inicio)
- **βₜ = 0.02** (más ruido al final)
- **Schedule: Lineal**

### ¿Se Entrenan los β?

**No.** Son hiperparámetros fijos que tú decides antes de entrenar.

---

## Propiedad de Forma Cerrada: El Atajo Matemático

### El Problema

Si quieres llegar al paso 500, ¿tienes que calcular los 499 pasos anteriores?

### La Solución

**No.** Puedes saltar directamente a cualquier paso con una sola fórmula:

```
xₜ = √ᾱₜ × x₀ + √(1-ᾱₜ) × ε
```

Donde:
- **ᾱₜ** = (1-β₁) × (1-β₂) × ... × (1-βₜ) (producto acumulado)
- **ε** = ruido gaussiano puro

### ¿Por Qué Es Importante?

**Para el entrenamiento:**
- No necesitas simular todos los pasos
- Puedes generar datos de entrenamiento muy rápido
- Eliges un tiempo t aleatorio y calculas xₜ directamente

El profesor lo explicó:
> "Yo puedo decir: che, no muestres el paso siguiente sino el paso que yo quiera."

### Analogía

Es como si quisieras saber cómo se ve tu foto después de 100 días al sol. No necesitas simular cada día; puedes calcular directamente cómo se verá en el día 100.

---

## El Proceso Reverse: Generar (Quitar Ruido)

### ¿Qué Es?

Es el proceso **inverso**: partir de ruido puro y **limpiarlo** paso a paso hasta obtener una imagen.

### El Problema

No podemos simplemente "revertir" el ruido porque:
- El ruido es aleatorio
- No sabemos qué imagen original había
- Hay infinitas imágenes posibles

### La Solución: Entrenar un Modelo

Entrenamos una **red neuronal** que aprende a:
- Tomar una imagen con ruido (xₜ)
- Predecir cómo era un paso antes (xₜ₋₁)

### Dos Formas Equivalentes

**Opción 1: Predecir la imagen anterior**
```
Entrada: xₜ (imagen ruidosa)
Salida: xₜ₋₁ (imagen con menos ruido)
```

**Opción 2: Predecir el ruido** (más común)
```
Entrada: xₜ (imagen ruidosa)
Salida: ε (el ruido que fue agregado)
Luego: xₜ₋₁ = xₜ - ε
```

El profesor explicó:
> "Son matemáticamente equivalentes pero predecir ruido suele ser más estable."

### El Proceso de Generación

```
1. Parte de ruido puro: xₜ ~ Normal(0, I)

2. Para cada paso t = T, T-1, T-2, ..., 1:
   - Predice el ruido con el modelo
   - Resta ese ruido
   - Obtén xₜ₋₁

3. Resultado final: x₀ (imagen generada)
```

### ¿Por Qué Es Lento?

Tienes que hacer **T pasadas** por la red neuronal (típicamente 1000).

El profesor mencionó:
> "Por eso demoran estos modelos, porque tienes que hacer T pasadas por la red neuronal."

---

## Arquitectura del Modelo

### ¿Qué Entra al Modelo?

El modelo recibe **dos cosas**:

1. **La imagen ruidosa (xₜ):** La imagen actual con ruido
2. **El tiempo (t):** El paso en el que estamos

### ¿Por Qué Pasar el Tiempo?

**Porque el modelo necesita saber cuánto ruido hay:**
- En t=1000: hay mucho ruido
- En t=1: hay poco ruido

Si no le dices t, el modelo no sabe si tiene que quitar mucho o poco ruido.

**Ventaja:** Un solo modelo para todos los pasos, condicionado por t.

El profesor explicó:
> "Un solo modelo para todos los pasos. No necesitas 1000 modelos diferentes."

### ¿Qué Sale del Modelo?

El modelo **no** da un valor exacto. Da **parámetros de una distribución**:
- **μ (media):** El centro de la distribución
- **σ² (varianza):** Qué tanto puede variar

**Similar a los VAEs:** El modelo predice parámetros para hacer un muestreo.

### Arquitectura Típica: UNet

- Red con forma de "U"
- Capas de **atención** para mejor calidad
- Recibe el tiempo t como embedding adicional

---

## El Entrenamiento: Cómo Aprende el Modelo

### Datos de Entrenamiento

**¿Qué necesitas?**
- Un dataset de imágenes (CIFAR-10, ImageNet, etc.)
- **No necesitas pares** (imagen ruidosa, imagen limpia)

**¿Por qué no necesitas pares?**
- Tú mismo generas los pares
- Tomas una imagen, le agregas ruido, y ya tienes el par

### El Algoritmo de Entrenamiento

```
Repetir hasta converger:
    1. Toma una imagen real x₀ del dataset

    2. Elige un tiempo t aleatorio (entre 1 y T)

    3. Genera ruido ε ~ Normal(0, I)

    4. Crea xₜ usando la forma cerrada:
       xₜ = √ᾱₜ × x₀ + √(1-ᾱₜ) × ε

    5. Pasa xₜ y t por el modelo → obtén ε_predicho

    6. Calcula la pérdida: L = ||ε - ε_predicho||²

    7. Actualiza los pesos con gradiente descendente
```

### La Función de Pérdida

**Versión simple:**
```
L = ||ε - εθ(xₜ, t)||²
```

**En español:**
- ε = el ruido real que agregaste
- εθ = el ruido que el modelo predijo
- La pérdida es la diferencia al cuadrado

**Objetivo:** Que el modelo aprenda a predecir exactamente el ruido que agregaste.

### Variational Lower Bound (VLB)

**Teoría más formal:**
- La loss teórica es una sumatoria de divergencias KL
- VLB = L₀ + L₁ + L₂ + ... + Lₜ
- Cada término compara distribuciones gaussianas

El profesor mencionó:
> "La variational lower bound es una sumatoria de términos... cada término compara distribuciones gaussianas."

**En la práctica:** La versión simple ||ε - εθ||² funciona igual de bien y es más fácil.

---

## Propiedad Markoviana: Eficiencia en el Entrenamiento

### ¿Qué Significa?

Cada paso **solo depende del paso anterior**, no de toda la historia.

```
xₜ solo depende de xₜ₋₁
(no de x₀, x₁, x₂, ... xₜ₋₂)
```

### ¿Por Qué Es Importante?

**Cualquier par consecutivo (xₜ, xₜ₋₁) es un dato de entrenamiento válido.**

El profesor explicó:
> "Cualquier dos puntos del camino me sirven como dato para entrenamiento."

### Ventaja Práctica

De una sola imagen x₀ generas **T ejemplos** de entrenamiento:
- (x₁, x₀)
- (x₂, x₁)
- (x₃, x₂)
- ...
- (xₜ, xₜ₋₁)

**¡Multiplicaste tus datos por T!** (típicamente 1000)

---

## Reparameterization Trick: Hacer Diferenciable el Muestreo

### El Problema

Queremos hacer backpropagation, pero hay muestreo aleatorio en el medio.
El muestreo no es diferenciable.

### La Solución

Separar la parte aleatoria de la parte aprendible:

```
En vez de:
    x ~ Normal(μ, σ²)  → No diferenciable

Hacer:
    ε ~ Normal(0, 1)   → Parte aleatoria fija
    x = μ + σ × ε      → Diferenciable en μ y σ
```

### Es el Mismo Truco que en VAEs

Si entendiste el reparameterization trick en VAEs, es exactamente lo mismo aquí.

---

## Comparación Detallada: Difusión vs GANs vs VAEs

### Tabla Comparativa

| Aspecto | GANs | VAEs | Difusión |
|---------|------|------|----------|
| **Arquitectura** | Generador + Discriminador | Encoder + Decoder | Modelo único |
| **Tamaño del latente** | Pequeño | Pequeño | **Mismo que el dato** |
| **Entrenamiento** | Inestable | Estable | **Muy estable** |
| **Calidad de imágenes** | Alta (pero problemas) | Media (borrosas) | **Muy alta** |
| **Diversidad** | Baja (mode collapse) | Media | **Muy alta** |
| **Velocidad generación** | **Muy rápida** (1 paso) | **Rápida** (1 paso) | Lenta (1000 pasos) |
| **Al final usas** | Solo Generador | Solo Decoder | Todo el modelo |

### GANs: Fortalezas y Debilidades

**Fortalezas:**
- Generación muy rápida
- Imágenes de alta calidad

**Debilidades:**
- Entrenamiento inestable (difícil balancear)
- **Mode collapse**: genera siempre cosas parecidas
- Difícil de entrenar bien

### VAEs: Fortalezas y Debilidades

**Fortalezas:**
- Entrenamiento estable
- Latente interpretable

**Debilidades:**
- Imágenes a veces borrosas
- Calidad menor que GANs y Difusión

### Difusión: Fortalezas y Debilidades

**Fortalezas:**
- Entrenamiento muy estable
- Mejor calidad de imágenes
- Mayor diversidad
- No sufre mode collapse

**Debilidades:**
- **Muy lento** para generar (necesita muchos pasos)
- Alto costo computacional

El profesor resumió:
> "Son más eficientes en el entrenamiento, tienen entrenamiento más estable y producen salidas más diversas y realistas."

---

## Aplicaciones Reales: DALL-E y Stable Diffusion

### DALL-E 2

**¿Qué es?**
- Modelo de OpenAI
- Genera imágenes a partir de texto
- "Un astronauta montando un caballo en el espacio" → Imagen

**Componentes:**
1. **CLIP:** Convierte texto en un vector numérico (embedding)
2. **Prior:** Conecta el embedding de texto con el de imagen
3. **Decoder (Difusión):** Genera la imagen
4. **Upsampler (Difusión):** Mejora la resolución

**El profesor mencionó:**
> "Tiene el embedding de texto, modelos que hacen de texto a imagen como CLIP adentro."

### Stable Diffusion

**Diferencias con DALL-E 2:**
- Es **open source** (código abierto)
- Puedes correrlo en tu computadora
- Usa **latent diffusion** (más eficiente)

**Latent Diffusion:**
- En vez de hacer difusión sobre píxeles
- Primero comprimes la imagen a un espacio latente
- Haces difusión ahí (más rápido)

### El Impacto

El profesor reflexionó:
> "Fue como un elemento clave cuando salió. Imaginarse que una IA podía hacer algo de esto hace tres, cuatro años era realmente una locura."

---

## Extensiones y Mejoras

### Conditioning (Condicionamiento)

**¿Qué es?**
Agregar información extra al modelo para guiar la generación.

**Tipos:**
- **Texto:** "un gato naranja"
- **Clase:** "generar un perro"
- **Sketch:** partir de un dibujo

### Attention Mechanisms

- Capas de atención para mejor calidad
- Permiten que el modelo "enfoque" en partes importantes
- Común en arquitecturas tipo UNet

### Diffusion Cascades

- Generar imagen de baja resolución primero
- Luego aumentar resolución con otro modelo
- Mejor calidad final

---

## El Práctico 7: Implementación

### Objetivo

**No vas a entrenar un modelo** (requiere mucho cómputo).

**Vas a:**
1. Usar modelo pre-entrenado de Hugging Face
2. Generar imágenes jugando con parámetros
3. Explorar el proceso paso a paso
4. Hacer interpolaciones en espacio latente

### Herramientas

| Herramienta | Descripción |
|-------------|-------------|
| **Modelo** | DDPM pre-entrenado |
| **Dataset** | CIFAR-10 (32×32 pixels, 10 clases) |
| **Framework** | Diffusers de Hugging Face |

### Dataset CIFAR-10

10 clases de imágenes pequeñas (32×32 pixels):
- Avión, Auto, Pájaro, Gato, Ciervo
- Perro, Rana, Caballo, Barco, Camión

### Código Básico

```python
from diffusers import DDPMPipeline
import torch

# Cargar modelo pre-entrenado
pipeline = DDPMPipeline.from_pretrained("google/ddpm-cifar10-32")

# Generar una imagen
image = pipeline(
    num_inference_steps=1000,
    generator=torch.manual_seed(42)
).images[0]

# Mostrar
image.show()
```

### Experimentos del Práctico

**1. Seeds (Semillas):**
- Misma seed = misma imagen
- Diferente seed = diferente imagen
- Para reproducibilidad

**2. Batch Generation:**
- Generar muchas imágenes en paralelo
- Aprovechar GPU
- Comparar tiempos

**3. Número de Pasos:**
- Menos pasos = más rápido pero peor calidad
- Más pasos = mejor calidad pero más lento

**4. Proceso Paso a Paso:**
- Ver cómo evoluciona la imagen
- Desde ruido puro hasta imagen final

**5. Interpolación:**
- Tomar dos imágenes
- Interpolar en espacio de ruido
- Ver transición suave

**6. Agregar y Quitar Ruido:**
- Partir de imagen real
- Agregar ruido (forward)
- Quitar ruido (reverse)
- ¿Recuperas la original?

### Advertencia del Profesor

> "Si tienen problemas de dependencias, usen Google Colab."
> "No vas a entrenar un modelo, eso requiere más cómputo."

---

## Conceptos Técnicos Adicionales

### Ruido Isotrópico

**¿Qué es?**
- Ruido gaussiano donde cada dimensión es independiente
- Media 0, varianza 1
- Es una "nube" de números aleatorios

**Es el punto final del forward:**
Cuando t → T, la imagen desaparece y solo queda este ruido.

### Time Step Embedding

**¿Cómo se pasa t al modelo?**
- Se convierte t en un vector (embedding)
- Se concatena o suma a las features
- Similar a positional encoding en Transformers

### UNet

**Arquitectura común para el modelo:**
- Forma de "U" (encoder-decoder con skip connections)
- Down-sampling → Bottleneck → Up-sampling
- Skip connections para preservar detalles

---

## Resumen: El Flujo Completo

### 1. Forward (No requiere entrenamiento)

```
Imagen real → Agregar ruido gradualmente → Ruido puro
    x₀    →    x₁ → x₂ → ... →    xₜ
```

### 2. Entrenamiento

```
Para cada imagen:
    1. Elige t aleatorio
    2. Genera ruido ε
    3. Crea xₜ con forma cerrada
    4. Modelo predice ruido
    5. Compara con ruido real
    6. Actualiza pesos
```

### 3. Generación (Reverse)

```
Ruido puro → Quitar ruido paso a paso → Imagen generada
    xₜ     →    xₜ₋₁ → ... → x₁ →    x₀
```

### 4. Validación

- No hay test set tradicional
- **Miramos las imágenes generadas**
- Métricas específicas (FID, IS, etc.)

---

## Definiciones para el Parcial

### Modelo de Difusión
Modelo generativo que crea datos partiendo de ruido puro y eliminándolo progresivamente en pasos iterativos hasta obtener datos coherentes.

### Proceso Forward (Difusión hacia adelante)
Proceso de agregar ruido gaussiano gradualmente a un dato real en T pasos hasta convertirlo en ruido isotrópico puro.

### Proceso Reverse (Difusión inversa)
Proceso generativo que elimina ruido iterativamente desde ruido puro hasta generar un dato de la distribución original.

### Schedule de Varianza (β)
Conjunto de hiperparámetros fijos (no entrenables) que controlan cuánto ruido se agrega en cada paso del forward.

### Ruido Isotrópico
Ruido gaussiano con media cero y varianza uno, independiente en todas las dimensiones; es el punto final del proceso forward.

### Propiedad de Forma Cerrada
Capacidad de calcular xₜ directamente desde x₀ sin pasar por pasos intermedios, usando el producto acumulado de α.

### Variational Lower Bound (VLB)
Cota inferior de la log-verosimilitud que se optimiza; es sumatoria de divergencias KL que en la práctica simplifica a ||ε - εθ||².

### Time Step Conditioning
Técnica de pasar el paso temporal t como entrada al modelo para que sepa cuánto ruido hay y ajuste su predicción.

### Reparameterization Trick
Técnica para hacer diferenciable el muestreo separando parte aleatoria (ε ~ N(0,1)) de parámetros aprendibles (x = μ + σε).

### Proceso Markoviano
Propiedad donde cada paso solo depende del paso anterior, permitiendo que cualquier par consecutivo sea dato de entrenamiento.

### DDPM (Denoising Diffusion Probabilistic Models)
Paper fundacional de modelos de difusión que propone T=1000 pasos con schedule lineal de β desde 0.0001 hasta 0.02.

### Latente en Difusión
A diferencia de VAE/GAN, en difusión el espacio latente tiene la misma dimensión que los datos originales.

---

## Posibles Preguntas para el Parcial

### ¿Qué es un modelo de difusión y cómo genera imágenes?
Es un modelo que parte de ruido puro y lo limpia paso a paso hasta generar una imagen coherente, aprendiendo a predecir el ruido en cada paso.

### ¿Cuál es la diferencia principal del espacio latente entre difusión y VAE?
En difusión el latente tiene el mismo tamaño que el dato (imagen 32×32 → latente 32×32), mientras en VAE el latente es más pequeño.

### ¿Qué controlan los parámetros β en el proceso forward?
Controlan cuánto ruido gaussiano se agrega en cada paso; valores típicos van de 0.0001 al inicio hasta 0.02 al final.

### ¿Por qué el proceso forward no necesita entrenamiento?
Porque solo agrega ruido gaussiano con fórmulas matemáticas predefinidas; no hay parámetros que aprender.

### ¿Qué predice el modelo en el proceso reverse?
Puede predecir el ruido agregado (ε) o el dato sin ruido; ambos son matemáticamente equivalentes pero predecir ruido es más estable.

### ¿Por qué se pasa el tiempo t como entrada al modelo?
Para que el modelo sepa cuánto ruido hay en la imagen actual y ajuste su predicción; permite usar un solo modelo para todos los pasos.

### ¿Qué es la propiedad markoviana y por qué es ventajosa?
Cada paso depende solo del anterior, permitiendo que cualquier par consecutivo sirva como dato de entrenamiento independiente.

### ¿Cuál es la función de pérdida típica en modelos de difusión?
La diferencia cuadrática entre el ruido real y el predicho: L = ||ε - εθ(xₜ, t)||².

### ¿Qué ventajas tienen los modelos de difusión sobre GANs?
Entrenamiento más estable, mayor diversidad en generaciones, no sufren mode collapse, y generan imágenes de mayor calidad.

### ¿Cuál es la principal desventaja de los modelos de difusión?
El proceso de generación es lento porque requiere muchos pasos iterativos (típicamente 1000 pasadas por la red).

### ¿Qué es la propiedad de forma cerrada y para qué sirve?
Permite calcular xₜ directamente desde x₀ sin pasos intermedios, acelerando la generación de datos de entrenamiento.

### ¿Cuántos pasos usa típicamente un modelo de difusión según el paper DDPM?
T = 1000 pasos con schedule lineal de β desde 10⁻⁴ hasta 0.02.

### ¿Qué es el conditioning en modelos de difusión?
Agregar información adicional (texto, clase, sketch) al modelo para guiar la generación hacia contenidos específicos.

### ¿Qué modelo usa DALL-E 2 para generar imágenes?
Usa modelos de difusión condicionados por embeddings de texto generados por CLIP.

### ¿Qué es el reparameterization trick y para qué sirve?
Técnica para hacer diferenciable el muestreo separando ruido fijo (ε) de parámetros aprendibles (μ, σ); permite backpropagation.

### ¿Por qué predecir ruido es más estable que predecir el dato directamente?
Porque el ruido tiene distribución conocida N(0,I) y rango limitado, mientras el dato tiene distribución compleja y desconocida.

### ¿Cuántos modelos se entrenan en difusión?
Un solo modelo compartido para todos los pasos, condicionado por el tiempo t actual.

### ¿Qué es un schedule lineal de β?
Configuración donde β crece linealmente desde un valor pequeño inicial (0.0001) hasta un valor mayor final (0.02).

---

## Recursos Mencionados en Clase

### Papers
1. **"Denoising Diffusion Probabilistic Models"** (DDPM) - Ho et al., Berkeley
2. **"Deep Unsupervised Learning using Nonequilibrium Thermodynamics"** - Paper original sobre difusión

### Blogs y Referencias
- **Blog de Lilian Weng** - Excelente recurso de referencia sobre diffusion models

### Herramientas
- **HuggingFace Diffusers** - Biblioteca para usar modelos pre-entrenados
- **Google Colab** - Recomendado si hay problemas de dependencias locales

---

## Notas Finales

### Lo que SÍ Necesitas Entender

- Qué es el proceso forward y reverse
- Por qué se usa ruido gaussiano
- Qué predice el modelo (ruido)
- Por qué se pasa el tiempo t
- Las ventajas sobre GANs y VAEs
- Cómo es el algoritmo de entrenamiento básico

### Lo que NO Necesitas Memorizar

- Las derivaciones matemáticas completas del VLB
- Los detalles exactos de la arquitectura UNet
- Las fórmulas exactas (pero sí entender qué representan)

### El Consejo del Profesor

> "Realmente quienes se meten a hacer todas estas cosas, los equipos que están peleando la punta en generación, es gente que está contratada ocho horas para hacer esto."

La idea es entender los conceptos fundamentales, no convertirse en experto en un semestre.
