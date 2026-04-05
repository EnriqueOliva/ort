# Inteligencia Artificial Generativa - Curso Completo

## La Gran Pregunta del Curso: ¿Cómo Puede una Máquina Crear?

Este curso responde una pregunta fundamental que ha fascinado a la humanidad desde los inicios de la computación: **¿Cómo puede una máquina generar datos nuevos que parezcan reales?**

No estamos hablando de copiar o memorizar. Estamos hablando de **crear**: imágenes de gatos que nunca existieron, textos que ningún humano escribió, música original. Esta es la esencia de la Inteligencia Artificial Generativa.

Como dijo el profesor en la primera clase, Ada Lovelace ya hablaba en el siglo XIX sobre usar la máquina analítica de Babbage para escribir música. Las ideas generativas son tan antiguas como la computación misma.

---

# PARTE I: LOS FUNDAMENTOS (Clases 1-3)

## Capítulo 1: El Cambio de Perspectiva

### Generativo vs. Discriminativo: La Diferencia Fundamental

En otras materias como Deep Learning y Machine Learning, aprendiste a **clasificar**: dado un dato, ¿a qué categoría pertenece? En IA Generativa, damos vuelta el problema: **¿cómo generamos datos nuevos que se parezcan a los reales?**

El profesor lo explicó con un ejemplo médico muy claro:

> "Yo no quiero que un clasificador de patologías médicas tenga variabilidad. En realidad ante una misma imagen, el clasificador debería darme suficientemente consistentemente la clase que mayor probabilidad tiene."

Pero en modelos generativos:

> "Para una misma entrada, puedo generar distintas salidas. Y eso no es un problema, de hecho es el correcto funcionamiento del sistema."

### La Demostración en Vivo

El profesor demostró esto con ChatGPT: le pidió "un blues de 12 compases en mi menor" dos veces y obtuvo dos composiciones diferentes. Esto NO es un error. Es exactamente lo que queremos.

| Modelo Discriminativo | Modelo Generativo |
|----------------------|-------------------|
| Misma entrada → Misma salida | Misma entrada → Diferentes salidas |
| "¿Es un tumor?" → Sí/No consistente | "Genera una imagen" → Variedad |
| Veredicto único | Creatividad |

## Capítulo 2: Las Herramientas Matemáticas

### Probabilidad: El Lenguaje de la Generación

Todo modelo generativo se basa en **distribuciones de probabilidad**. Si queremos generar datos realistas, primero debemos entender cómo se distribuyen los datos reales.

#### La Regla del Producto (La Base de Todo)

**P(X, Y) = P(X) × P(Y|X)**

Esta fórmula parece simple, pero es **la base de los modelos autorregresivos** que veremos más adelante. Permite descomponer probabilidades conjuntas complejas en probabilidades más simples.

#### La Regla de la Suma (Marginalización)

**P(X) = Σ P(X, Y) = Σ P(X|Y) × P(Y)**

Esta regla nos permite "borrar" variables que no nos interesan. Es la base de las **mixturas de distribuciones**.

### Variables Aleatorias Continuas

El mundo real tiene datos continuos: pesos, alturas, intensidades de píxeles. Para esto usamos:

1. **Distribución Uniforme U(a,b)**: Todos los valores igualmente probables entre a y b
2. **Distribución Normal (Gaussiana) N(μ, σ²)**: La famosa campana, centrada en μ con dispersión σ
3. **Distribución Laplaciana**: Similar a la normal pero con pico más agudo

**La más importante para el curso: la Gaussiana.** La veremos en VAEs, modelos de difusión, y más.

### Mixturas de Gaussianas: Cuando la Realidad es Compleja

El profesor usó el ejemplo de los gatos:

> "Si graficas el peso de todos los gatos (machos y hembras juntos), no ves una campana perfecta. Ves dos campanas superpuestas."

**P(Peso) = P(Macho) × P(Peso|Macho) + P(Hembra) × P(Peso|Hembra)**

Esto se aplica directamente al práctico de Iris con 3 tipos de flores.

## Capítulo 3: El Primer Modelo - Autorregresivo

### La Idea Central

**Un modelo autorregresivo genera datos de a poquito, en orden, donde cada nuevo dato depende de los anteriores.**

Para una imagen con píxeles X₁, X₂, ..., Xₙ:

**P(X₁, X₂, ..., Xₙ) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂) × ... × P(Xₙ|X₁,...,Xₙ₋₁)**

### El Problema de la Explosión de Parámetros

Si cada píxel puede ser 0 o 1:
- P(X₂|X₁) requiere 2 parámetros
- P(X₃|X₁,X₂) requiere 4 parámetros
- P(Xₙ|X₁,...,Xₙ₋₁) requiere **2^(n-1) parámetros**

Para una imagen de 28×28 (784 píxeles), necesitarías 2^783 parámetros. **Imposible.**

### La Solución Brillante: Perceptrones

En lugar de tablas gigantes, usamos funciones (perceptrones):

**P(X₂=1|X₁) = σ(W₂₁ × X₁ + B₂)**

Donde σ es la sigmoide. Esto reduce de crecimiento exponencial a **crecimiento lineal**.

### Las Redes de Hinton

Geoffrey Hinton (Premio Nobel de Física 2024) propuso organizar todos estos perceptrones en una matriz triangular inferior, donde los ceros garantizan que cada píxel solo dependa de los anteriores.

---

# PARTE II: EL ENTRENAMIENTO (Clases 4-5)

## Capítulo 4: ¿Cómo Entrenar un Modelo Generativo?

### El Objetivo: Acercar Distribuciones

Tenemos:
- **P_data**: La distribución real de los datos
- **P_θ**: La distribución que nuestro modelo estima

Queremos que P_θ se parezca lo más posible a P_data.

### KL Divergence: Midiendo la Diferencia

La **divergencia de Kullback-Leibler** mide qué tan diferentes son dos distribuciones:

**KL(P || Q) = E_P[log(P/Q)]**

Propiedades importantes:
- KL ≥ 0 siempre
- KL = 0 solo si P = Q
- No es simétrica

### De KL a Negative Log-Likelihood

Minimizar la KL divergence es equivalente a minimizar:

**-E[log P_θ(x)]**

Esto se llama **Negative Log-Likelihood (NLL)**. Queremos que nuestro modelo asigne alta probabilidad a los datos reales.

### Empirical Risk Minimization

No podemos calcular la esperanza real (necesitaríamos infinitos datos). La aproximamos con el promedio sobre nuestro dataset:

**J(θ) = -(1/N) × Σ log P_θ(x)**

### Binary Cross-Entropy: La Función Práctica

Para perceptrones binarios, usamos:

**BCE = -[x × log(ŷ) + (1-x) × log(1-ŷ)]**

El profesor explicó por qué esto es necesario:

> "Un perceptrón no me da P_θ(x_i), me da P_θ(x_i = 1). Para cuando x_i es cero, al perceptrón solo no lo puedo usar."

La BCE actúa como un "selector" que elige el término correcto según el valor real del dato.

## Capítulo 5: Implementando Hinton en PyTorch

### La Estructura del Código

```python
class Hinton(nn.Module):
    def __init__(self, input_size):
        self.W = nn.Parameter(...)  # Pesos entrenables
        self.B = nn.Parameter(...)  # Bias entrenable
        self.mask = torch.tril(torch.ones(n, n), diagonal=-1)  # NO entrenable

    def forward(self, x):
        W_masked = self.W * self.mask  # Aplicar máscara
        z = x @ W_masked.T + self.B
        return torch.sigmoid(z)
```

### La Asimetría Fundamental

- **Entrenamiento**: Paralelo (tienes todos los datos)
- **Generación**: Secuencial (cada paso depende del anterior)

> "No puedes paralelizar la generación. Necesitas la palabra 3 antes de darte la 4."

Esta es una limitación fundamental de los modelos autorregresivos que también aplica a GPT y ChatGPT.

---

# PARTE III: VARIATIONAL AUTOENCODERS (Clase 6)

## Capítulo 6: Un Nuevo Paradigma

### Variables Latentes: Lo Que No Vemos

El profesor usó el ejemplo de las flores Iris:

> "Si nosotros no conocemos la variable [variedad de flor], si no sabemos que la variedad es lo que nos induce efectivamente a cierta forma de la distribución... yo le llamo a esa variable aleatoria latente porque existe pero no la puedo observar."

### De Autoencoder a VAE

Un **autoencoder** básico tiene:
1. **Encoder**: Comprime X → Z (vector pequeño)
2. **Decoder**: Expande Z → X̂ (reconstrucción)

Un **VAE** cambia algo fundamental:
- El encoder no da un vector Z directamente
- Da **parámetros de una distribución** (μ y σ)
- Muestreamos Z de esa distribución

### El Problema: Backpropagation a Través del Muestreo

¿Cómo hacemos backpropagation cuando hay un paso aleatorio en medio?

> "Esto nunca les pasó con Matías. Tenemos una variable aleatoria con parámetros entrenables."

### La Solución: Reparametrization Trick

**Antes (problemático):**
```
Z ~ Normal(μ_θ(X), σ_θ(X))
```

**Después (solución):**
```
ε ~ Normal(0, 1)  # Fijo, no depende de θ
Z = μ_θ(X) + σ_θ(X) × ε
```

Matemáticamente es equivalente, pero ahora podemos derivar respecto a θ.

### La Función de Pérdida del VAE

**Loss = Reconstrucción + KL Divergence**

- **Reconstrucción**: ¿Qué tan bien reconstruye X̂ a X?
- **KL Divergence**: ¿Qué tan parecido es el espacio latente a Normal(0,1)?

¿Por qué forzar Normal(0,1)?

> "Porque después vas a tirar todo lo que está atrás (el encoder), vas a agarrar el decoder y vas a hacer muestreo de una Normal(0,1). Si está bien entrenado, la salida va a ser una imagen verosímil."

---

# PARTE IV: REDES ADVERSARIALES (Clase 7)

## Capítulo 7: GANs - El Juego de Suma Cero

### La Idea Creativa

Ian Goodfellow (2014) propuso modelar la generación como un **juego entre dos redes**:

1. **Generador (G)**: Como un falsificador de billetes
2. **Discriminador (D)**: Como un policía que detecta falsificaciones

> "El objetivo de uno es opuesto al del otro. El objetivo de G es lograr engañar a D. El objetivo de D es descubrir a G."

### La Función de Pérdida

**min_G max_D V(D,G) = E[log D(x)] + E[log(1 - D(G(z)))]**

- D quiere **maximizar**: ser buen detective
- G quiere **minimizar**: engañar al detective

### El Entrenamiento Alternado

```
Para cada época:
    1. Congelar G, entrenar D con datos reales y falsos
    2. Congelar D, entrenar G para engañar a D
```

### El Truco del "Label Flip"

Cuando entrenamos G:

> "Aunque sabemos que son truchos, el label que le pasamos es uno."

Esto es numéricamente más estable que minimizar log(1-D(G(z))).

### Problemas Conocidos

**Mode Collapse:**
> "Si G aprende a generar un tipo de datos porque nada en el modelo nos incentiva a la variedad."

**Inestabilidad:**
> "Es muy difícil un punto de equilibrio. Literalmente es mejor arrancar el entrenamiento de nuevo que intentar recuperarse."

---

# PARTE V: MODELOS DE LENGUAJE (Clase 9)

## Capítulo 8: De Imágenes a Texto

### ¿Qué es un Language Model?

> "Son sistemas que emiten distribuciones de probabilidad. Le imputa una tira de tokens y emite el siguiente símbolo."

Definición formal:
**LM: Σ* → P(Σ ∪ {END})**

### Tokenización

Antes de procesar texto, hay que convertirlo en números:

```python
texto = "Hola, ¿cómo estás?"
tokens = tokenizer.encode(texto)  # [15432, 11, 8064, 2585, 30]
```

Opciones de tokenización:
- Por palabras
- Por caracteres
- Por sub-palabras (lo más común)

**Regla de oro:**
> "Un tokenizer va con un modelo. Una vez que está todo hecho, no se toca más el tokenizer."

### El Proceso de Generación

```
1. Entrada: "Hola, ¿cómo"
2. Tokenizar → [15432, 11, 8064]
3. Pasar por modelo → Vector de logits
4. Softmax → Probabilidades
5. Muestrear un token
6. Concatenar y repetir
```

### Estrategias de Muestreo

**Top-K:** Solo considerar los K tokens más probables

**Top-P (Nucleus):** Considerar tokens hasta que sumen probabilidad P

**Temperatura:**
- Baja (0.3): Más determinístico, menos creativo
- Alta (1.5): Más aleatorio, más creativo

### La Conexión con Autorregresivos

Los LLMs son **modelos autorregresivos aplicados a texto**. La misma limitación aplica:

> "Estos modelos no son infinitos. No puedo meter cosas muy largas."

---

# PARTE VI: MODELOS DE DIFUSIÓN (Clase 10)

## Capítulo 9: La Revolución Reciente

### La Idea Central

> "Comenzar con ruido puro y refinarlo gradualmente para generar datos como imágenes."

A diferencia de VAEs: el espacio latente tiene **la misma dimensionalidad** que el dato original.

### Forward Diffusion (Agregar Ruido)

En T pasos (típicamente 1000), agregamos ruido gaussiano gradualmente:

```
X_0 (imagen real) → X_1 → X_2 → ... → X_T (ruido puro)
```

El **schedule de varianza** β controla cuánto ruido se agrega en cada paso.

### Backward Diffusion (Quitar Ruido)

El modelo aprende P(X_{t-1} | X_t): cómo era la imagen un paso antes.

En generación: partimos de ruido puro y aplicamos el modelo T veces.

### Ventajas sobre Modelos Anteriores

> "Son más eficientes en el entrenamiento, tienen un entrenamiento más estable y producen salidas más diversas y realistas."

### Eficiencia en Entrenamiento

> "Cualquier par de puntos del camino me sirven como dato de entrenamiento. Son independientes."

Esto permite entrenar con cualquier transición X_t → X_{t-1}, no secuencialmente.

---

# PARTE VII: EVALUACIÓN (Clases 11-12)

## Capítulo 10: ¿Cómo Saber si un Modelo Generativo es Bueno?

### El Problema Fundamental

> "En los modelos discriminativos evaluamos con métricas claras como accuracy. En los modelos generativos se nos complica porque lo que yo quiero es aproximar la distribución completa."

### Los Dos Ejes de Evaluación

1. **Fidelidad**: ¿Qué tan realistas son las muestras?
2. **Diversidad**: ¿Qué tanto cubre la variedad del conjunto de datos?

> "Si mi modelo me genera un uno perfecto pero solo genera ese uno, ¿es bueno?"

### Métricas Matemáticas

| Métrica | Descripción | Uso |
|---------|-------------|-----|
| KL Divergence | Diferencia entre distribuciones | VAEs, Difusión |
| Jensen-Shannon | KL simétrica | GANs |
| Wasserstein | "Trabajo" para transformar distribuciones | Wasserstein GAN |
| MMD | Diferencia de medias | Varios |

### Métricas con Modelos Pre-entrenados

**Inception Score (IS):**
- Usa Inception para clasificar imágenes generadas
- Score alto = buena calidad y diversidad

**FID (Fréchet Inception Distance):**
> "Pasas el dato por la red hasta la penúltima capa. Asumes que esa capa es una representación sucinta de lo que el dato contiene."

FID bajo = distribuciones similares = mejor calidad

### Métricas para Texto

**Perplexity:**
> "Es la exponencial de la media de la verosimilitud. Me dice qué tanta probabilidad le asigna un modelo a una secuencia real."

**BLEU:** Compara n-gramas con referencias

**ROUGE:** Similar a BLEU pero enfocado en recall

### Evaluación Humana

> "Correlaciona directamente con la percepción humana porque tenemos a humanos haciendo las evaluaciones."

Pero: es costoso y no escala.

### La Recomendación del Profesor

> "Combina múltiples métricas. Entiende qué mide cada una. Considera el contexto."

---

# PARTE VIII: SÍNTESIS Y CONEXIONES

## El Zoológico de Modelos Generativos

Como dijo el profesor:

> "Este curso va a ser una especie de zoológico de modelos generativos donde vamos a ir viendo las ideas. Porque todos los modelos que hay hoy en día de algún modo usan y mezclan las ideas que vamos a estar visitando."

### Comparación de Modelos

| Modelo | Tipo | Muestreo | Fortaleza | Debilidad |
|--------|------|----------|-----------|-----------|
| Hinton | Autorregresivo | Secuencial | Simple | Lento |
| VAE | Encoder-Decoder | En latente | Latentes interpretables | Imágenes borrosas |
| GAN | Adversarial | Del generador | Imágenes nítidas | Inestable |
| Difusión | Denoising | Iterativo | Alta calidad | Lento en generación |
| LLM | Autorregresivo | Secuencial | Texto coherente | Alucinaciones |

### El Hilo Conductor: Probabilidad

Todos los modelos buscan lo mismo: **aproximar la distribución real de los datos** para poder muestrear datos nuevos.

- Autorregresivos: Descomponen P(X) en producto de condicionales
- VAEs: Aprenden P(X|Z) y P(Z|X) con regularización
- GANs: Entrenan G para que P_G ≈ P_data mediante adversario
- Difusión: Aprenden a revertir un proceso de ruido
- LLMs: Predicen P(token_siguiente | contexto)

### El Insight Central del Curso

**Los modelos de Deep Learning que usas para clasificar son, en realidad, estimadores de parámetros de distribuciones de probabilidad. Si cambias tu perspectiva de "quiero predecir" a "quiero muestrear", la misma herramienta se convierte en un generador.**

---

# CONCEPTOS CLAVE PARA RECORDAR

## Fundamentos

1. **Distribuciones de probabilidad** son la herramienta fundamental
2. **P(Y|X) = clasificación**, **P(X|Y) = generación**
3. **Muestrear** significa generar datos nuevos desde una distribución

## Modelos

4. **Autorregresivo**: Cada variable depende de las anteriores
5. **VAE**: Encoder-Decoder con espacio latente regularizado
6. **GAN**: Dos redes compitiendo (generador vs discriminador)
7. **Difusión**: Aprender a quitar ruido gradualmente
8. **LLM**: Modelo autorregresivo sobre tokens de texto

## Entrenamiento

9. **KL Divergence** mide diferencia entre distribuciones
10. **BCE** es la función de pérdida para variables binarias
11. **Reparametrization Trick** permite derivar a través de muestreos

## Evaluación

12. **Fidelidad + Diversidad** son los dos ejes
13. **FID** es la métrica más usada para imágenes
14. **Perplexity** es la métrica más usada para texto

---

# REFLEXIÓN FINAL

Este curso no es solo sobre técnicas. Es sobre **un cambio de mentalidad**: pasar de ver las redes neuronales como clasificadores a verlas como estimadores de distribuciones.

Como dijo el profesor:

> "Es una materia que tiene un poquito de otra cabeza. Vamos a usar las herramientas que están viendo en otras materias, pero las vamos a usar un poquito distintas."

La IA Generativa no es magia. Es matemática (probabilidad), computación (redes neuronales), y creatividad (diseño de arquitecturas). Y ahora tienes las herramientas para entender cómo funcionan los sistemas que están transformando el mundo.

---

## Estructura del Curso

| Clase | Fecha | Tema Principal |
|-------|-------|----------------|
| 1 | 19-08-2025 | Introducción y fundamentos de probabilidad |
| 2 | 26-08-2025 | Variables continuas, Redes Bayesianas |
| 3 | 02-09-2025 | Práctico Iris, mixturas de gaussianas |
| 4 | 09-09-2025 | Función de pérdida (KL, NLL, BCE) |
| 5 | 16-09-2025 | Implementación de Hinton |
| 6 | 30-09-2025 | Variational Autoencoders |
| 7 | 07-10-2025 | GANs (Redes Adversariales) |
| 8 | 14-10-2025 | Presentación del obligatorio |
| 9 | 21-10-2025 | Modelos de Lenguaje |
| 10 | 28-10-2025 | Modelos de Difusión |
| 11 | 04-11-2025 | Exposiciones de proyectos |
| 12 | 11-11-2025 | Métricas de evaluación |
| 13 | 18-11-2025 | Exposiciones orales |
| 14 | 25-11-2025 | Cierre del curso |

---

*Este documento fue creado como síntesis completa del curso de Inteligencia Artificial Generativa, basado en las transcripciones de las 14 clases.*
