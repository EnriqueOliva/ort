# Respuestas del Parcial - Inteligencia Artificial Generativa 2025

**Facultad de Ingeniería - Universidad ORT**

| | |
|---|---|
| **Fecha:** 09/12/2025 | **Duración:** 2 h |
| **Evaluación:** Parcial | **Uso de Calculadora:** SI |
| **Materia:** Inteligencia Artificial Generativa | **Uso de Material:** NO |
| **Turno:** Nocturno | **Puntaje Máximo/Mínimo:** 30/1 Puntos |

---

## Ejercicio 1 - Language Models (LMs) (8 puntos)

### 1. ¿Qué es un Language Model?

**Respuesta: D. Un modelo que asigna probabilidades a secuencias de texto y predice tokens futuros.**

**Explicación detallada:**

Un Language Model es un sistema que recibe una secuencia de tokens y emite una distribución de probabilidad sobre el siguiente token. Formalmente: LM: Σ* → P(Σ ∪ {END}).

Como lo definió el profesor en clase:
> "Son sistemas que emiten distribuciones de probabilidad. Le imputa una tira de tokens y emite el siguiente símbolo."

No clasifica (A), no corrige gramática (B), y no traduce (C). Su función es modelar la probabilidad de secuencias de texto, lo que después permite generar texto nuevo muestreando token a token.

---

### 2. ¿Por qué un LM necesita tokenizar el texto?

**Respuesta: C. Para poder representar el texto como números procesables por una red neuronal.**

**Explicación detallada:**

Las redes neuronales trabajan con números, no con texto. La tokenización convierte texto en secuencias de índices numéricos que la red puede procesar.

```
"Hola, ¿cómo estás?" → [15432, 11, 8064, 2585, 30]
```

No se trata de eliminar palabras (A), ni reducir tamaño (B), ni detectar sintaxis (D). El propósito fundamental es la conversión de texto a representaciones numéricas.

Como dijo el profesor: "Un tokenizer va con un modelo. Una vez que está todo hecho, no se toca más el tokenizer."

---

### 3. Factorización de la probabilidad en un LM autorregresivo

**Respuesta: D. P(x) = Πᵢ P(xᵢ|x<ᵢ)**

**Explicación detallada:**

Un modelo autorregresivo descompone la probabilidad conjunta como un producto de condicionales, donde cada token depende de todos los anteriores. Esto viene directamente de la regla de la cadena (regla del producto):

```
P(x₁, x₂, ..., xₙ) = P(x₁) × P(x₂|x₁) × P(x₃|x₁,x₂) × ... × P(xₙ|x₁,...,xₙ₋₁)
```

Que se escribe compactamente como: P(x) = Πᵢ P(xᵢ|x<ᵢ)

Las otras opciones son incorrectas porque:
- A (suma): sumar probabilidades no da la probabilidad conjunta
- B (condicional sobre todos menos i): no es la factorización autorregresiva
- C (solo dos variables): ignora el resto de la secuencia

---

### 4. Cuando un LM procesa la frase "Hola, hoy es"

**Respuesta: B. Calcula la probabilidad del siguiente token dependiente del contexto de toda la frase.**

**Explicación detallada:**

Un LM autorregresivo condiciona la predicción del siguiente token en TODA la secuencia anterior. No procesa palabras aisladamente (A), no busca respuestas guardadas (C), y no ignora palabras previas (D).

La predicción es: P(siguiente_token | "Hola", ",", "hoy", "es")

El modelo usa todo el contexto disponible. Por eso los transformers usan mecanismos de atención: para que cada posición pueda "ver" todas las posiciones anteriores.

---

### 5. El siguiente token después de "Hola, hoy es" se obtiene

**Respuesta: B. Muestreando de la distribución de probabilidad que el modelo asigna a todos los posibles tokens siguientes.**

**Explicación detallada:**

El proceso es:
1. El modelo calcula logits para cada posible token del vocabulario
2. Softmax convierte logits en probabilidades
3. Se **muestrea** un token de esa distribución

Observación clave del profesor: "El LM es **determinístico**. Para la misma entrada, siempre da la misma distribución. La **aleatoriedad** viene del sampling."

No se calcula directamente del corpus (A), no hay tabla fija (C), y no se repite el último token (D).

El muestreo puede usar distintas estrategias: greedy, top-K, top-P, temperatura.

---

### 6. ¿Por qué un LM utiliza embeddings para representar tokens?

**Respuesta corta (para el parcial):**
> Porque los embeddings transforman tokens (índices discretos) en vectores densos de números reales que capturan relaciones semánticas entre palabras. Sin embeddings, los tokens serían solo índices sin ninguna noción de similitud o significado, y la red no podría aprovechar relaciones como "rey" y "reina" estando semánticamente cerca.

**Explicación detallada:**

Los tokens son índices enteros (ej: "hola" = 15432). Si los usáramos directamente:
- No hay noción de distancia o similitud entre tokens
- El token 15432 y el 15433 no tienen relación semántica alguna
- One-hot encoding sería un vector enorme y disperso (tamaño del vocabulario, ej: 50,000 dimensiones)

Los embeddings resuelven esto:
- Mapean cada token a un vector denso de dimensión fija (ej: 768 dimensiones)
- Tokens con significados similares quedan cerca en el espacio vectorial
- Son parámetros entrenables: el modelo aprende las representaciones óptimas durante el entrenamiento
- Permiten capturar relaciones semánticas y sintácticas

---

## Ejercicio 2 - Generative Adversarial Networks (GANs) (8 puntos)

### 1. Rol de cada término de la pérdida adversarial

```
min_G max_D  E_{x~p_data}[log D(x)] + E_{z~p(z)}[log(1 - D(G(z)))]
```

**Respuesta corta (para el parcial):**

> **Primer término — E[log D(x)]:** Mide qué tan bien D clasifica datos **reales** como reales. D quiere maximizarlo (que D(x) → 1). G no aparece, así que este término no afecta a G directamente.
>
> **Segundo término — E[log(1 - D(G(z)))]:** Mide qué tan bien D detecta datos **falsos** generados por G. D quiere maximizarlo (que D(G(z)) → 0, detectar las falsificaciones). G quiere minimizarlo (que D(G(z)) → 1, engañar al discriminador).

**Explicación detallada:**

#### Primer término: E_{x~p_data}[log D(x)]

- Se calcula con datos **reales** del dataset
- D(x) es la probabilidad que D asigna de que x sea real
- **D quiere maximizar:** si D(x) → 1, entonces log(1) = 0 (máximo posible)
- Si D clasifica mal un dato real (D(x) → 0), log(0) → -∞ (penalización enorme)
- G no participa en este término

#### Segundo término: E_{z~p(z)}[log(1 - D(G(z)))]

- Se calcula con datos **falsos** que G genera a partir de ruido z
- D(G(z)) es la probabilidad que D asigna de que la imagen falsa sea real
- **D quiere maximizar:** si detecta la falsificación D(G(z)) → 0, entonces log(1-0) = 0 (máximo)
- **G quiere minimizar:** si engaña a D, D(G(z)) → 1, entonces log(1-1) = log(0) → -∞

#### La dinámica conjunta:

Es un juego de suma cero (minimax). D intenta maximizar ambos términos (ser buen detective). G intenta minimizar el segundo término (ser buen falsificador). El entrenamiento busca un equilibrio donde G genera datos indistinguibles de los reales.

En la práctica, para G se usa el truco del "label flip": en vez de minimizar log(1-D(G(z))), se maximiza log(D(G(z))), porque da mejores gradientes al inicio del entrenamiento.

---

### 2. Pseudocódigo de entrenamiento de una GAN

**Respuesta corta (para el parcial):**

```
PARA cada época:
    PARA cada batch:

        # === ENTRENAR DISCRIMINADOR ===

        # a. Muestras reales
        x_real = obtener_batch_del_dataset()

        # b. Muestras falsas
        z = muestrear_normal(0, 1, tamaño=batch_size)
        x_falso = G(z).detach()    # detach para NO actualizar G

        # c. Actualización de D
        pred_real = D(x_real)
        pred_falso = D(x_falso)
        loss_D = BCE(pred_real, 1) + BCE(pred_falso, 0)
        optimizer_D.zero_grad()
        loss_D.backward()
        optimizer_D.step()

        # === ENTRENAR GENERADOR ===

        # b. Nuevas muestras falsas
        z = muestrear_normal(0, 1, tamaño=batch_size)
        x_falso = G(z)             # SIN detach, para que fluyan gradientes a G

        # d. Actualización de G
        pred_falso = D(x_falso)
        loss_G = BCE(pred_falso, 1)  # Label flip: label=1 para fakes
        optimizer_G.zero_grad()
        loss_G.backward()
        optimizer_G.step()
```

**Detalles importantes:**

- **`.detach()`** al entrenar D: corta el grafo computacional para que los gradientes no lleguen a G. Solo queremos actualizar D en este paso.
- **Sin `.detach()`** al entrenar G: necesitamos que los gradientes fluyan desde D a través de G(z) hasta los pesos de G.
- **Label flip** al entrenar G: usamos label=1 para las imágenes falsas. Esto es equivalente a maximizar log(D(G(z))) en vez de minimizar log(1-D(G(z))), lo cual es numéricamente más estable.
- Las muestras reales (a) y falsas (b) se usan para D. Para G solo se generan nuevas muestras falsas.

---

### 3. ¿Cómo se generan nuevas muestras durante la inferencia?

**Respuesta corta (para el parcial):**
> Se muestrea un vector de ruido z ~ N(0,1) y se pasa por el generador entrenado: imagen = G(z). El discriminador ya no se usa. La generación es en un solo paso (forward pass).

**Explicación detallada:**

```
z = muestrear_normal(0, 1, tamaño=dimensión_latente)
imagen_generada = G_entrenado(z)
```

En inferencia solo se necesita el generador. El discriminador cumplió su función durante el entrenamiento (forzar a G a mejorar) y se descarta. Cada z diferente produce una imagen diferente.

---

## Ejercicio 3 - Diffusion Models (6 puntos)

### Explique qué significa "aprender a invertir el proceso de difusión" y por qué permite generar imágenes desde ruido.

**Respuesta corta (para el parcial):**

> El proceso **forward** de difusión agrega ruido gaussiano gradualmente a una imagen real en T pasos hasta convertirla en ruido puro. "Aprender a invertir" significa entrenar un modelo para hacer lo contrario: dado un paso ruidoso x_t, predecir cómo era la imagen un paso antes (x_{t-1}, menos ruidosa). Si el modelo aprende bien esta inversión, se puede partir de ruido puro x_T ~ N(0,1) y aplicar la red T veces para generar una imagen nueva x₀, porque cada aplicación quita un poco de ruido.

**Explicación detallada:**

#### El proceso forward: q(x_t | x_{t-1})

Es un proceso **fijo** (no se entrena). Agrega ruido gaussiano gradualmente:

```
x₀ (imagen real) → x₁ (poco ruido) → ... → x_T (ruido puro)
```

En cada paso: x_t = √(1-β_t) × x_{t-1} + √β_t × ε, donde ε ~ N(0,1)

Después de suficientes pasos (T ≈ 1000), x_T es indistinguible de ruido gaussiano puro.

#### El proceso reverse: p_θ(x_{t-1} | x_t)

Es lo que el modelo **aprende**. Dado un x_t ruidoso y el timestep t, el modelo predice el ruido ε que se agregó:

```
ε̂ = modelo(x_t, t)
```

Con esa predicción, se puede calcular x_{t-1} (la imagen con un poco menos de ruido).

#### ¿Por qué esto permite generar desde ruido?

1. **Partimos de ruido puro:** x_T ~ N(0,I). Esto es fácil de muestrear.
2. **Aplicamos el modelo T veces:** en cada paso, el modelo estima el ruido presente y lo quita parcialmente.
3. **Al final obtenemos x₀:** una imagen limpia que pertenece a la distribución de los datos de entrenamiento.

```
x_T (ruido) → modelo → x_{T-1} → modelo → ... → x₁ → modelo → x₀ (imagen)
```

#### ¿Por qué funciona?

- Durante el entrenamiento, el modelo vio millones de pares (x_t, ε) — imágenes a distintos niveles de ruido y el ruido que se les agregó.
- Aprendió la relación estadística entre "cómo se ve una imagen con ruido" y "qué ruido se le agregó".
- El timestep t le indica al modelo cuánto ruido hay aproximadamente, para saber cuánto quitar.
- A diferencia de un VAE, el espacio latente tiene **la misma dimensionalidad** que la imagen original.

Como dijo el profesor:
> "Comenzar con ruido puro y refinarlo gradualmente para generar datos como imágenes."

#### Ventajas del enfoque:

- **Entrenamiento estable:** la función de pérdida es simplemente MSE: L = ||ε - ε̂||²
- **Cualquier par sirve:** no hay que recorrer los T pasos secuencialmente en entrenamiento. Se elige t aleatorio y se usa la fórmula cerrada para saltar directo a x_t.
- **Alta calidad:** el refinamiento gradual en T pasos produce resultados muy detallados.

---

## Ejercicio 4 - Variational Autoencoders (VAEs) (8 puntos)

### 1a. ¿Por qué el término ∫ f_θ(z) ∇_θ p_θ(z) dz NO puede estimarse directamente con Monte Carlo?

**Respuesta corta (para el parcial):**
> Porque para estimar una integral con Monte Carlo, necesitamos muestrear de la distribución que aparece multiplicando a la función. En este caso, el integrando es f_θ(z) × ∇_θ p_θ(z), pero ∇_θ p_θ(z) **no es una distribución de probabilidad** (no integra a 1, puede ser negativo). No podemos muestrear de algo que no es una distribución. Si muestreamos z de p_θ(z), obtenemos E_{p_θ}[f_θ(z) × ∇_θ log p_θ(z)] (que es otra cosa, el score function estimator), no el término original directamente.

**Explicación detallada:**

Monte Carlo estima integrales de la forma:

```
E_{p(z)}[g(z)] = ∫ p(z) g(z) dz ≈ (1/N) Σ g(zᵢ)    donde zᵢ ~ p(z)
```

Para que esto funcione, necesitamos:
1. Poder muestrear de p(z)
2. Que p(z) sea una distribución de probabilidad válida

El término problemático es:

```
∫ f_θ(z) ∇_θ p_θ(z) dz
```

Aquí, ∇_θ p_θ(z) es el **gradiente de la densidad** respecto a θ. Este gradiente:
- Puede ser positivo o negativo
- No integra a 1
- No es una distribución de probabilidad

Por lo tanto, no podemos simplemente muestrear z de "∇_θ p_θ(z)" y promediar f_θ(z).

---

### 1b. ¿Qué problema práctico genera esto al entrenar VAEs?

**Respuesta corta (para el parcial):**
> En un VAE, el encoder produce parámetros θ (o φ) de una distribución q_φ(z|x), y necesitamos calcular el gradiente de la pérdida respecto a esos parámetros para hacer backpropagation. Pero la pérdida involucra una esperanza sobre z ~ q_φ(z|x), y como z se obtiene por muestreo de una distribución que depende de φ, no podemos propagar el gradiente a través del paso de muestreo. Esto **bloquea el entrenamiento** porque no hay forma de calcular ∂Loss/∂φ directamente.

**Explicación detallada:**

En un VAE:
```
x → Encoder(φ) → μ_φ(x), σ_φ(x) → [MUESTREO: z ~ N(μ, σ²)] → Decoder(θ) → x̂
```

El paso de muestreo es un "muro" para el gradiente:
- Backpropagation necesita calcular derivadas de cada operación
- El muestreo z ~ N(μ_φ, σ²_φ) es una operación estocástica
- ∂z/∂φ no está definido porque z es aleatorio
- Sin este gradiente, no podemos actualizar los pesos del encoder

Como dijo el profesor:
> "Nosotros tenemos una variable aleatoria con parámetros entrenables. Esto nunca les pasó con Matías."

---

### 1c. ¿Cómo la reparametrización soluciona esta limitación?

**Respuesta corta (para el parcial):**
> La reparametrización separa la aleatoriedad de los parámetros entrenables. En vez de muestrear z ~ N(μ_φ, σ²_φ), se expresa z = μ_φ + σ_φ × ε, donde ε ~ N(0,1) es independiente de φ. Ahora z es una función **determinista** de φ (y del ruido externo ε), así que podemos calcular ∂z/∂μ = 1 y ∂z/∂σ = ε, y la cadena de backpropagation funciona normalmente.

**Explicación detallada:**

#### Antes (problemático):
```
z ~ N(μ_φ(x), σ²_φ(x))     ← muestreo directo, no derivable respecto a φ
```

#### Después (reparametrizado):
```
ε ~ N(0, 1)                  ← ruido fijo, NO depende de φ
z = μ_φ(x) + σ_φ(x) × ε     ← función determinista de φ
```

¿Por qué funciona?
1. **Matemáticamente equivalente:** si ε ~ N(0,1), entonces μ + σ×ε ~ N(μ, σ²). La distribución de z es idéntica.
2. **Ahora sí podemos derivar:** z = μ + σ × ε es una operación aritmética estándar.
   - ∂z/∂μ = 1
   - ∂z/∂σ = ε
3. **La aleatoriedad quedó aislada** en ε, que no tiene parámetros entrenables.

Como dijo el profesor:
> "Los parámetros derivables (θ) los dejo por fuera y la distribución es fija. Tengo una distribución que son los datos que muestreo y otra distribución que son los ε que muestreo, pero nunca muestreo Zs en función de los θ."

---

### 2. ¿Por qué el KL regulariza el espacio latente y qué pasaría sin él?

```
log p_θ(x^(i)) ≥ L(x^(i), θ, φ) = E_z[log p_θ(x^(i) | z)]  -  D_KL(q_φ(z | x^(i)) || p_θ(z))
                                    \______________________/     \____________________________/
                                     Reconstruct the Input Data          KL Divergence
```

**Respuesta corta (para el parcial):**
> El KL fuerza a que la distribución aprendida por el encoder q_φ(z|x) se parezca al prior p(z) = N(0,1). Esto **regulariza** el espacio latente manteniéndolo organizado, continuo y centrado cerca del origen. Sin el KL, el encoder podría mapear cada dato a regiones arbitrarias y lejanas del espacio latente (como un autoencoder normal): las reconstrucciones serían excelentes, pero no se podría generar datos nuevos porque no sabríamos de qué distribución muestrear z, y el espacio latente tendría huecos que producen basura.

**Explicación detallada:**

#### ¿Qué hace el término KL?

D_KL(q_φ(z|x) || p(z)) mide qué tan diferente es la distribución del encoder q_φ(z|x) respecto al prior p(z) = N(0,1).

- KL = 0: el encoder produce exactamente N(0,1) para cualquier input → no codifica nada útil
- KL grande: el encoder produce distribuciones muy distintas a N(0,1) → buena codificación pero espacio latente desorganizado

Al minimizar el KL (con signo negativo, lo maximizamos en la fórmula), forzamos:
- Que las μ estén cerca de 0
- Que las σ estén cerca de 1
- Que las distribuciones de distintos datos se superpongan parcialmente

#### ¿Por qué esto permite generar?

Como explicó el profesor:
> "Porque después vas a tirar todo lo que está atrás (el encoder), vas a agarrar el decoder y vas a hacer muestreo de una Normal(0,1). Si está bien entrenado, la salida va a ser una imagen verosímil."

Si el espacio latente se parece a N(0,1), entonces muestrear z ~ N(0,1) en generación produce vectores que caen en regiones "conocidas" por el decoder.

#### ¿Qué pasaría si se retira el KL completamente?

1. **Degeneración a autoencoder determinístico:** el encoder colapsaría σ → 0 y cada dato se mapearía a un punto fijo μ con varianza cero. Se pierde la naturaleza probabilística.

2. **Espacio latente desorganizado:** sin restricción, el encoder puede poner cada dato en cualquier región del espacio. El dato "3" podría estar en z = [150, -300] y el "7" en z = [-2000, 42].

3. **No se puede generar:** si muestreamos z ~ N(0,1), estos vectores caerían en regiones del espacio latente que el decoder nunca vio durante entrenamiento → la salida sería ruido o basura.

4. **Huecos en el espacio latente:** habría grandes regiones vacías entre los clusters de datos, y cualquier z que caiga ahí produciría resultados sin sentido.

5. **Reconstrucción excelente pero generación inútil:** el modelo reconstruiría perfectamente (loss de reconstrucción bajo), pero no serviría como modelo **generativo**.

#### El balance

Los dos términos del loss están en tensión:

| Término | Si domina... |
|---|---|
| Reconstrucción | Espacio latente caótico, buena reconstrucción, mala generación |
| KL | Espacio latente organizado, reconstrucción borrosa, buena generación |

El VAE busca un equilibrio: reconstruir razonablemente bien **y** mantener el espacio latente organizado para poder generar.

La variante **β-VAE** (Loss = Reconstrucción + β × KL) permite controlar este balance:
- β > 1: prioriza organización del espacio latente
- β < 1: prioriza calidad de reconstrucción
