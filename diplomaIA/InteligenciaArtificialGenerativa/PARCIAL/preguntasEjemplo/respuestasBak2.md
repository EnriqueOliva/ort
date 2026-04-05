# Preguntas ejemplo parcial

## IA Generativa

---

### Language Models

1. Explica cómo funcionan los modelos autorregresivos generativos con variables discretas y explique cual es la función de pérdida.

**Respuesta corta (para el parcial):**
> Los modelos autorregresivos generan datos secuencialmente: cada variable Xi depende de las anteriores. Usando la regla del producto: P(X) = P(X₁) × P(X₂|X₁) × ... × P(Xₙ|X₁,...,Xₙ₋₁). La función de pérdida es la Negative Log-Likelihood: J(θ) = -(1/N) × Σ Σ log P_θ(xᵢ | x<i), que para variables binarias se implementa como Binary Cross-Entropy.

**Explicación detallada:**

Un modelo autorregresivo genera datos "de a poquito, en orden, donde cada nuevo dato depende de los anteriores". El profesor explicó que esto se basa en la regla del producto de probabilidad.

Para una secuencia de variables X₁, X₂, ..., Xₙ (por ejemplo, píxeles de una imagen):

**P(X₁, X₂, ..., Xₙ) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂) × ... × P(Xₙ|X₁,...,Xₙ₋₁)**

El problema es que estimar todas las condicionales con tablas requeriría 2^(n-1) parámetros para el último término (explosión exponencial). La solución es usar perceptrones para estimar cada probabilidad condicional:

**P(Xᵢ=1 | X<i) = σ(W × X<i + B)**

La función de pérdida se deriva de la KL Divergence entre la distribución real P_data y la distribución del modelo P_θ. Minimizar KL equivale a minimizar el Negative Log-Likelihood:

**J(θ) = -(1/N) × Σ log P_θ(x)**

Para modelos autorregresivos, el logaritmo del producto se convierte en suma de logaritmos:

**J(θ) = -(1/N) × Σₓ Σᵢ log P_θ(xᵢ | x<i)**

Para variables binarias (0 o 1), como el perceptrón siempre da P(X=1), necesitamos la Binary Cross-Entropy que "selecciona" el término correcto:

**BCE = -[xᵢ × log(σᵢ) + (1-xᵢ) × log(1-σᵢ)]**

---

2. Diseña un esquema para preprocesar datos de texto para entrenar un modelo de lenguaje autoregresivo, considerando un vocabulario discreto. Describe cada paso y su importancia.

**Respuesta corta (para el parcial):**
> El preprocesamiento incluye: (1) Tokenización: dividir texto en unidades (palabras/subpalabras/caracteres) y mapearlas a números; (2) Construcción del vocabulario: crear diccionario token→ID único; (3) Agregar tokens especiales (START, END, PAD, UNK); (4) Crear pares entrada-salida desplazados para entrenar la predicción del siguiente token.

**Explicación detallada:**

El profesor explicó que para entrenar un modelo de lenguaje, primero hay que convertir el texto en algo que la red pueda procesar. El proceso tiene varios pasos:

**1. Tokenización:**
- Divide el texto en unidades llamadas tokens
- Opciones: por palabras, caracteres, o sub-palabras (lo más común)
- Como dijo el profesor: "Un tokenizer va con un modelo. Una vez que está todo hecho, no se toca más el tokenizer"

**2. Construcción del vocabulario:**
- Cada token único recibe un ID numérico
- Ejemplo: "hola" → 15432, "mundo" → 8247
- El tamaño del vocabulario es un hiperparámetro importante

**3. Tokens especiales:**
- START: indica inicio de secuencia
- END: indica fin de secuencia
- PAD: relleno para igualar longitudes
- UNK: palabras desconocidas (fuera del vocabulario)

**4. Crear datos de entrenamiento:**
- Para cada secuencia, crear pares (contexto, siguiente token)
- Ejemplo: "El gato negro" → ("El", "gato"), ("El gato", "negro")

**5. Padding y truncamiento:**
- Igualar longitudes de secuencias en un batch
- Truncar secuencias muy largas (los modelos tienen contexto limitado)

La importancia es que el modelo necesita entrada numérica de tamaño fijo para procesar, y la calidad del tokenizador afecta directamente qué tan bien el modelo puede representar el lenguaje.

---

3. En el contexto de los modelos autoregresivos, ¿cómo afecta la elección del tamaño del vocabulario a la complejidad del modelo y a su capacidad de generalización?

**Respuesta corta (para el parcial):**
> Vocabulario grande: más parámetros en la capa de salida (softmax sobre V tokens), mejor representación de palabras raras, pero mayor riesgo de overfitting y más costoso. Vocabulario pequeño: menos parámetros, secuencias más largas (una palabra puede ser varios tokens), pero mejor generalización. El balance típico es usar sub-palabras (BPE/WordPiece).

**Explicación detallada:**

El tamaño del vocabulario V afecta directamente varias cosas:

**Complejidad del modelo:**
- La capa de salida tiene dimensión V (produce logits para cada posible token)
- Más vocabulario = más parámetros = modelo más grande
- El softmax sobre V elementos es más costoso computacionalmente

**Longitud de secuencias:**
- Vocabulario pequeño (ej: caracteres) = secuencias muy largas
- Vocabulario grande (ej: palabras completas) = secuencias más cortas
- Como el profesor explicó: "Estos modelos no son infinitos. No puedo meter cosas muy largas."

**Generalización:**
- Vocabulario muy grande puede tener tokens raros con pocos ejemplos de entrenamiento
- Vocabulario pequeño generaliza mejor a palabras nuevas (las descompone en partes conocidas)

**La solución moderna (sub-palabras):**
- Algoritmos como BPE (Byte-Pair Encoding) encuentran un balance
- Palabras comunes son tokens únicos
- Palabras raras se dividen en sub-palabras conocidas
- Típicamente 30,000-50,000 tokens

---

4. Propón una métrica que usarías para evaluar un modelo autoregresivo generativo en un problema de predicción de secuencias. Justifica tu elección.

**Respuesta corta (para el parcial):**
> Perplexity (perplejidad): mide qué tan "sorprendido" está el modelo ante secuencias reales. Perplexity = exp(-(1/N) × Σ log P(xᵢ|x<i)). Menor perplexity = mejor modelo. Es apropiada porque mide directamente la verosimilitud que el modelo asigna a datos reales, que es exactamente lo que optimizamos durante el entrenamiento.

**Explicación detallada:**

El profesor explicó que evaluar modelos generativos es difícil porque "¿Cuál es el ground truth de una imagen generada?" Sin embargo, para modelos de lenguaje existe una métrica estándar:

**Perplexity:**

Como explicó el profesor: "Es la exponencial de la media de la verosimilitud. Me dice qué tanta probabilidad le asigna un modelo a una secuencia real."

**PPL = exp(-(1/N) × Σ log P(xᵢ | x<i))**

**¿Por qué es buena?**

1. **Directamente relacionada con el entrenamiento:** Es la exponencial del loss (NLL) que minimizamos
2. **Interpretable:** Una perplexity de 10 significa que el modelo está tan "confundido" como si eligiera uniformemente entre 10 opciones
3. **Compara modelos:** Menor perplexity = mejor predicción de secuencias reales
4. **No requiere generación:** Se calcula sobre datos reales, no sobre muestras generadas

**Limitaciones:**
- No mide la calidad de generaciones abiertas
- No evalúa coherencia semántica de largo plazo
- Modelos con vocabularios diferentes no son directamente comparables

Para evaluar generación más completa, se pueden agregar métricas como BLEU (compara n-gramas con referencias) o evaluación humana.

---

5. ¿Cómo afectaría el uso de un modelo autoregresivo como GPT-2 en lugar de un LSTM en términos de captura de dependencias de largo alcance en un texto?

**Respuesta corta (para el parcial):**
> GPT-2 (Transformer) captura mucho mejor las dependencias de largo alcance gracias al mecanismo de atención, que permite acceder directamente a cualquier posición previa. LSTM sufre de vanishing gradients y pierde información en secuencias largas porque procesa secuencialmente. GPT-2 puede atender a miles de tokens previos; LSTM prácticamente pierde información después de ~100 tokens.

**Explicación detallada:**

El profesor explicó en clase la diferencia clave entre RNNs y Transformers:

**LSTM (y RNNs en general):**
- Procesan secuencia token por token de manera **secuencial**
- Mantienen un "estado oculto" que resume todo lo anterior
- Problema: el estado tiene tamaño fijo, la información se "comprime" y pierde
- El vanishing gradient hace difícil que errores en tokens lejanos afecten tokens iniciales
- Como dijo el profesor: "por más que tengas una LSTM o algo, a los miles y miles de palabras ya de tokens, ya, o sea, una LSTM tiene memoria a largo plazo mucho mejor que una RN común" pero aún así es limitada

**Transformers (GPT-2):**
- Usan mecanismo de atención: "el attention considera toda la secuencia de hidden, no va concentrando en un solo hidden"
- **Procesan todo de una vez** - no hay procesamiento secuencial en entrenamiento
- No hay compresión forzada en un estado fijo
- Las dependencias largas son tan "baratas" como las cortas
- Pueden manejar contextos de 1024, 2048, o más tokens

**Diferencia clave mencionada en clase:**
> "La diferencia más evidente es que el transformer vos hacés todo de una. Con lo cual aprovechas mucho [paralelización]. En entrenamiento, sobre todo, el beneficio es la paralelización."

**Consecuencia práctica:**
- GPT-2 puede mantener coherencia temática en párrafos enteros
- LSTM tiende a "olvidar" el tema después de unas oraciones
- Para generación de texto largo, Transformers son claramente superiores
- En **inferencia**, ambos son secuenciales (hay un loop), pero en **entrenamiento** el Transformer es paralelo

---

### Variational Autoencoders (VAE)

1. Describe el papel de las distribuciones gaussianas en los VAEs y explica cómo el truco de la reparametrización permite entrenar estos modelos con backpropagation.

**Respuesta corta (para el parcial):**
> En VAE, el encoder produce μ y σ (parámetros de una gaussiana), y Z se muestrea de N(μ,σ). El problema: no se puede hacer backpropagation a través de un muestreo aleatorio. El truco de reparametrización: Z = μ + σ × ε, donde ε ~ N(0,1) es fijo. Así la aleatoriedad no depende de los parámetros θ y los gradientes pueden fluir.

**Explicación detallada:**

El profesor fue muy claro sobre por qué esto es importante:

> "Nosotros tenemos una variable aleatoria con parámetros entrenables. Esto nunca les pasó con Matías."

**El rol de las gaussianas:**

1. **En el encoder:** No da un vector Z directamente, sino parámetros μ_θ(X) y σ_θ(X) de una distribución gaussiana
2. **En el espacio latente:** Z se muestrea de N(μ_θ(X), σ_θ(X))
3. **En la pérdida:** La KL divergence fuerza que N(μ,σ) se parezca a N(0,1)

**El problema del muestreo:**

> "¿Cómo hacemos backpropagation a través de un proceso de muestreo?"

Si Z ~ N(μ_θ, σ_θ), la derivada ∂Z/∂θ no está definida porque Z es aleatorio.

**El reparametrization trick:**

**Antes:** Z ~ N(μ_θ(X), σ_θ(X))

**Después:**
- ε ~ N(0,1) ← distribución FIJA, no depende de θ
- Z = μ_θ(X) + σ_θ(X) × ε ← operación DETERMINISTA

Como explicó el profesor: "Los parámetros derivables (θ) los dejo por fuera y la distribución es fija. Tengo una distribución que son los datos que muestreo y otra distribución que son los ε que muestreo, pero nunca muestreo Zs en función de los θ."

**Por qué funciona:**
- Matemáticamente: μ + σ×ε tiene la misma distribución que N(μ,σ)
- Para gradientes: ahora ∂Z/∂μ = 1 y ∂Z/∂σ = ε, ambos definidos
- La regla de la cadena funciona normalmente

---

2. Dado un conjunto de datos de imágenes, ¿qué preprocesamientos aplicarías para entrenar un VAE? Explica cómo la dimensionalidad de los datos afecta el diseño del modelo.

**Respuesta corta (para el parcial):**
> Preprocesamientos: normalizar píxeles al rango [0,1] o [-1,1], redimensionar a tamaño fijo, posiblemente convertir a escala de grises. La dimensionalidad del dato (ej: 28×28×1 = 784) determina el tamaño del encoder/decoder. La dimensionalidad del latente Z es un hiperparámetro: Z grande = más capacidad pero más parámetros; Z pequeño = mejor compresión pero posible pérdida de información.

**Explicación detallada:**

El profesor explicó varios aspectos del preprocesamiento para VAEs:

**Preprocesamientos de los datos:**

1. **Normalización:** "El transform directamente va a ser pasarlo al tensor, no vamos a usar nada de binarización" (a diferencia de las redes de Hinton)
   - Llevar píxeles de [0,255] a [0,1] o [-1,1]

2. **Tamaño consistente:** Todas las imágenes deben tener el mismo tamaño

3. **Canales:** Definir si es escala de grises (1 canal) o color (3 canales)

**Dimensionalidad y diseño del modelo:**

**Dimensión de entrada (X):**
- Determina el tamaño de entrada del encoder
- Para MNIST 28×28: 784 dimensiones
- Para imágenes más grandes, se usan convoluciones para reducir dimensionalidad eficientemente

**Dimensión del latente (Z):**

El profesor fue claro: "La dimensionalidad del latente es un hiperparámetro del algoritmo. Es algo que decidís vos."

- **Z pequeño (ej: 2-10):**
  - Mayor compresión
  - Menos parámetros
  - Posible pérdida de información
  - Más fácil de visualizar

- **Z grande (ej: 100-500):**
  - Más capacidad de representación
  - Más parámetros que entrenar
  - Necesita más datos

> "Cuanto más tamaño tenga, más parámetros vas a tener que entrenar, más datos vas a necesitar o más tiempo de entrenamiento."

**Relación entre dimensiones:**

Si Z tiene casi la misma dimensión que X, no hay compresión real y el modelo podría aprender la función identidad. El "cuello de botella" fuerza al modelo a aprender representaciones útiles.

---

3. ¿Por qué es importante equilibrar los términos de reconstrucción y regularización en la función de pérdida de un VAE? Proporciona un ejemplo práctico para ilustrar esto.

**Respuesta corta (para el parcial):**
> Loss_VAE = Reconstrucción + KL_Divergence. Si domina reconstrucción: reconstrucciones perfectas pero espacio latente caótico, no se puede generar. Si domina KL: espacio latente organizado como N(0,1) pero reconstrucciones borrosas/malas. El balance permite tanto buena reconstrucción como generación válida al muestrear de N(0,1).

**Explicación detallada:**

El profesor explicó la función de pérdida del VAE:

**Loss = E_z[log p_θ(x|z)] - D_KL(q_φ(z|x) || p(z))**

O en términos más simples:

**Loss = Reconstrucción + KL Divergence**

**Término de reconstrucción (E_z[log p_θ(x|z)]):**
- Mide qué tan bien el decoder reconstruye X desde Z
- Si domina: el modelo solo se enfoca en reconstruir perfectamente
- Problema: el espacio latente puede ser caótico, con "huecos"

**Término KL Divergence (-D_KL(q_φ(z|x) || p(z))):**
- Fuerza que la distribución del encoder N(μ,σ) se parezca a N(0,1)
- El profesor explicó: "Nosotros queremos que Z sea una Normal(0,1). Porque después vas a tirar todo lo que está atrás (el encoder), vas a agarrar el decoder y vas a hacer muestreo de acuerdo a una Normal(0,1)."

**Ejemplo práctico con MNIST:**

**Si solo optimizamos reconstrucción:**
- El modelo podría codificar cada dígito en una región muy específica del espacio latente
- El "5" podría ir a Z=(100, -50), el "7" a Z=(-200, 300)
- Reconstrucciones perfectas
- Pero si muestreamos de N(0,1), obtenemos Z cerca de (0,0), que está en una "zona muerta"
- Resultado: imágenes generadas son ruido o sin sentido

**Si solo optimizamos KL:**
- Todos los Z se comprimen a estar cerca de (0,0)
- El espacio latente es perfectamente N(0,1)
- Pero toda la información de qué dígito era se pierde
- Resultado: todas las reconstrucciones son el "dígito promedio", borroso

**Con balance correcto:**
- Los Z se organizan alrededor de (0,0) pero con estructura
- Diferentes dígitos ocupan diferentes regiones, pero todas cerca del origen
- Al muestrear de N(0,1), caemos en regiones válidas
- Resultado: generamos dígitos diversos y realistas

---

4. Diseña un experimento práctico para medir el impacto del tamaño de la latente en un VAE. Describe cómo interpretarías los resultados.

**Respuesta corta (para el parcial):**
> Experimento: entrenar VAEs idénticos pero con latente_dim = 2, 10, 50, 100, 500. Medir: (1) loss de reconstrucción final, (2) loss KL, (3) calidad visual de reconstrucciones y generaciones, (4) FID si es posible. Interpretación: latente muy pequeña → alta reconstrucción loss, imágenes borrosas; latente muy grande → KL difícil de minimizar, posible colapso posterior; óptimo en el medio.

**Explicación detallada:**

El profesor dio consejos sobre experimentación:

> "Lo mejor que puedes hacer es evaluar. Vas a tener algún budget de tiempo y cómputo, dedicarlo a probar con prolijidad y con las métricas que te interesen."

**Diseño del experimento:**

**Variables:**
- Independiente: dimensión del espacio latente (2, 10, 50, 100, 500)
- Controladas: arquitectura del encoder/decoder, learning rate, batch size, epochs

**Métricas a recopilar en cada configuración:**

1. **Loss de reconstrucción:** Qué tan bien reconstruye X̂ a X
2. **Loss KL:** Qué tan parecido es el latente a N(0,1)
3. **Loss total:** La suma ponderada
4. **Calidad visual:** Inspección manual de reconstrucciones
5. **Calidad de generación:** Inspección de imágenes generadas muestreando de N(0,1)
6. **FID (si es posible):** Comparar distribución de generadas vs reales

**Interpretación de resultados esperados:**

**Latente muy pequeña (ej: 2):**
- KL loss: baja (fácil de organizar 2 dimensiones)
- Reconstrucción loss: alta (no hay suficiente capacidad)
- Visual: reconstrucciones borrosas, generaciones limitadas
- Útil: para visualización del espacio latente

**Latente intermedia (ej: 50):**
- Balance entre ambas losses
- Reconstrucciones razonables
- Generaciones diversas y realistas
- El "sweet spot" típico

**Latente muy grande (ej: 500):**
- Reconstrucción loss: muy baja (mucha capacidad)
- KL loss: difícil de minimizar (muchas dimensiones que regularizar)
- Riesgo: "posterior collapse" donde algunas dimensiones se ignoran
- Generaciones pueden ser buenas pero modelo es innecesariamente grande

**Recomendación del profesor:**

> "Siempre lo que recomiendo es ser registrados, registrar, hacer tracking lo mejor posible de sus experimentos para después poder tomar las decisiones informadas."

---

### Generative Adversarial Networks (GAN)

1. Explica cómo el entrenamiento competitivo entre el generador y el discriminador en una GAN puede llevar a inestabilidad. Proporciona dos soluciones comunes para mitigar este problema.

**Respuesta corta (para el parcial):**
> La inestabilidad ocurre porque G y D tienen objetivos opuestos: si D se vuelve muy bueno, G no recibe gradientes útiles; si G domina, D no puede mejorar. Soluciones: (1) Learning rates diferentes (D más bajo que G, típicamente 10x menor); (2) Entrenar D más veces que G por iteración (ratio K); (3) Normalización de datos a [-1,1].

**Explicación detallada:**

El profesor y Juan fueron muy claros sobre la inestabilidad de las GANs:

> "Es un arte encontrar los hiperparámetros correctos."

> "Literalmente es mejor arrancar el entrenamiento de nuevo que intentar recuperarse."

**¿Por qué hay inestabilidad?**

La GAN es un juego de suma cero entre G y D:
- D quiere maximizar: clasificar correctamente reales y falsos
- G quiere minimizar: engañar a D

**Problema 1: D demasiado fuerte**
- D detecta todo como falso sin esfuerzo
- Los gradientes para G son muy pequeños (D da 0 para todo lo que G produce)
- G no puede mejorar

**Problema 2: G demasiado fuerte**
- G engaña completamente a D
- D ya no da feedback útil
- El entrenamiento se estanca

**Soluciones mencionadas en clase:**

**1. Learning rates diferentes:**
```python
optimizer_G = Adam(G.parameters(), lr=0.0002)
optimizer_D = Adam(D.parameters(), lr=0.00002)  # 10x menor
```

Como dijo el profesor: "El discriminador estamos dando un orden menos... ya lo estamos penalizando."

**2. Ratio de entrenamiento (parámetro K):**
- Entrenar D varias veces antes de entrenar G una vez
- O viceversa, dependiendo del problema

> "Es un ratio discriminador-generador... depende del problema."

**3. Normalización de datos:**
El profesor enfatizó: "Esta transformación de normalización ayuda muchísimo... puede ser clave en forma de que si no normalizamos muchas veces directamente no llegamos a un resultado bueno."

Normalizar imágenes a [-1, 1] con la salida de G usando tanh.

**4. Monitoreo constante:**
- Mirar las pérdidas de ambas redes
- Si una va a 0 y se queda, algo está mal
- Mirar imágenes generadas periódicamente

---

2. ¿Qué es el colapso del modo en una GAN y cómo se puede mitigar?

**Respuesta corta (para el parcial):**
> Mode collapse ocurre cuando G genera solo un tipo de dato (ej: solo "3" en MNIST) porque engaña exitosamente a D con eso y no hay incentivo para diversidad. Mitigaciones: (1) GANs condicionales donde se especifica la clase a generar; (2) Agregar ruido a las imágenes durante entrenamiento; (3) Feature matching: comparar estadísticas de capas intermedias de D.

**Explicación detallada:**

El profesor explicó claramente este problema:

> "Si bien aprenden a generar, aprenden a generar un tipo de datos porque nada en el modelo nos incentiva a la variedad."

**¿Qué es mode collapse?**

Imagina entrenando una GAN para generar dígitos 0-9:
- G descubre que puede generar muy buenos "3"
- D no puede distinguir esos "3" de los reales
- G se "queda pegado" generando solo "3"
- Nunca aprende a generar los otros dígitos

Como dijo el profesor: "Si vos aprendes a hacer un buen uno y tu modelo aprende a hacer un muy buen uno y que tu discriminador no discrimina, ya está, ganaste. Siempre que pase ruido te da un buen uno."

**¿Por qué ocurre?**

La función de pérdida de la GAN solo mide si D puede distinguir reales de falsos. NO mide diversidad. Si G puede engañar a D con un solo tipo de imagen, matemáticamente ha "ganado".

**Mitigaciones:**

**1. GANs Condicionales (cGAN):**
El profesor mencionó: "Existen GANs condicionales donde vos te puedes decir de qué clase querés."
- G recibe la clase como entrada adicional: G(z, clase)
- D también recibe la clase y verifica consistencia
- Fuerza a G a aprender todas las clases

**2. Minibatch discrimination:**
- D mira estadísticas del batch completo, no solo imágenes individuales
- Detecta si todas las imágenes del batch son muy similares

**3. Feature matching:**
- En lugar de maximizar la probabilidad de engañar a D
- Minimizar la diferencia de features intermedios entre reales y falsos
- Esto fuerza diversidad a nivel de características

**4. Unrolled GANs:**
- G considera cómo D responderá en los próximos K pasos
- Previene que G explote debilidades específicas de D

---

3. Explica el papel del discriminador en una GAN. ¿Qué debe aprender el discriminador para que el generador mejore su rendimiento?

**Respuesta corta (para el parcial):**
> D es un clasificador binario que distingue imágenes reales de falsas. Debe aprender las características que hacen que una imagen sea "realista" vs "generada". Al entrenar D, este conocimiento se transfiere a G a través de los gradientes: cuando D rechaza una imagen falsa, los gradientes le dicen a G qué características le faltaron. D debe ser suficientemente bueno para dar feedback útil, pero no tan bueno que G no pueda mejorar.

**Explicación detallada:**

El profesor usó la metáfora del policía:

> "El Discriminador es como un policía o detective que trata de detectar cuáles billetes son falsos y cuáles son reales."

**El rol de D:**

1. **Clasificador binario:** Recibe una imagen y produce un número entre 0 y 1
   - D(X) ≈ 1 significa "creo que es real"
   - D(X) ≈ 0 significa "creo que es falsa"

2. **Extractor de características:** Internamente, D aprende qué hace que una imagen sea realista
   - Texturas correctas
   - Formas coherentes
   - Distribución de colores apropiada

**¿Qué debe aprender D?**

D debe aprender a detectar las diferencias sutiles entre datos reales y generados:
- Artefactos de generación
- Inconsistencias en texturas
- Patrones que nunca aparecen en datos reales

**¿Cómo D ayuda a G a mejorar?**

A través de los gradientes del entrenamiento adversarial:

1. G genera una imagen falsa
2. D la clasifica (ej: D(G(z)) = 0.1, "muy falsa")
3. El loss de G depende de la salida de D
4. Al hacer backpropagation, los gradientes "fluyen" desde D hacia G
5. Estos gradientes le dicen a G: "si cambias estos píxeles, D te clasificará mejor"

**El balance crítico:**

- **D muy malo:** Da feedback aleatorio, G no aprende nada útil
- **D muy bueno:** Siempre da 0 para todo lo de G, gradientes son cero, G no puede mejorar
- **D "justo":** Da feedback informativo que G puede usar para mejorar

El profesor enfatizó: "Son dos optimizaciones diferentes" que deben mantenerse balanceadas.

---

4. En una GAN, ¿cómo afecta el balance entre el generador y el discriminador al éxito del entrenamiento?

**Respuesta corta (para el parcial):**
> El balance es crucial: si D domina, G no recibe gradientes útiles y no mejora; si G domina, D pierde capacidad de dar feedback. El entrenamiento exitoso requiere que ambos mejoren gradualmente juntos. Se controla con: learning rates diferentes (D menor), ratio de entrenamiento K, y monitoreo constante de ambas losses.

**Explicación detallada:**

El profesor comparó el entrenamiento de GANs con un equilibrio delicado:

> "Es muy difícil un punto de equilibrio."

**Escenarios de desbalance:**

**Escenario 1: D demasiado fuerte**
- D clasifica perfectamente: D(real)→1, D(fake)→0
- Loss de D es muy baja
- Pero los gradientes para G son casi cero (D está "saturado")
- G no puede mejorar porque no recibe señal
- Resultado: G produce ruido aleatorio indefinidamente

**Escenario 2: G demasiado fuerte**
- G engaña completamente a D
- D no puede distinguir reales de falsos (D→0.5 para todo)
- D ya no da información útil
- G podría estar en mode collapse y D no lo detecta
- Resultado: G genera un solo tipo de imagen repetidamente

**El entrenamiento ideal:**

Ambas redes mejoran gradualmente en tándem:
- D mejora un poco → detecta nuevos problemas en las imágenes de G
- G mejora un poco → corrige esos problemas
- D mejora otro poco → detecta problemas más sutiles
- Y así sucesivamente...

**Mecanismos de control:**

1. **Learning rates:**
   ```python
   lr_G = 0.0002
   lr_D = 0.00002  # 10x menor
   ```

2. **Ratio K:**
   - Entrenar D K veces por cada vez que se entrena G
   - O viceversa

3. **Monitoreo:**
   - Si loss_D → 0 y se queda: D dominando
   - Si loss_D → 0.69 (log(0.5)): D confundido
   - Ambas losses deberían oscilar, no converger a extremos

---

5. Compara las GANs estándar con las GANs condicionales. ¿Cuáles son las ventajas de usar un discriminador condicionado?

**Respuesta corta (para el parcial):**
> GAN estándar: G(z)→imagen, D(imagen)→real/falso. No hay control sobre qué genera. GAN condicional: G(z, clase)→imagen, D(imagen, clase)→real/falso Y consistente con clase. Ventajas: (1) Control sobre la generación especificando la clase; (2) Reduce mode collapse al forzar diversidad por clases; (3) D verifica consistencia imagen-clase, mejor supervisión.

**Explicación detallada:**

El profesor mencionó las GANs condicionales como solución al mode collapse:

> "Existen GANs condicionales donde vos te puedes decir de qué clase querés."

**GAN Estándar:**

**Generador:** G(z) → imagen
- Entrada: solo ruido z
- Salida: imagen
- No hay control sobre qué tipo de imagen genera

**Discriminador:** D(imagen) → [0,1]
- Entrada: solo la imagen
- Salida: probabilidad de ser real
- No considera clases

**Problema:** No puedes pedir "generame un 7" o "generame un gato"

**GAN Condicional (cGAN):**

**Generador:** G(z, c) → imagen
- Entrada: ruido z + condición c (ej: clase, texto, otra imagen)
- Salida: imagen que debería corresponder a la condición
- Puedes especificar qué quieres generar

**Discriminador:** D(imagen, c) → [0,1]
- Entrada: imagen + condición
- Salida: probabilidad de ser real Y consistente con la condición
- Verifica que la imagen "tenga sentido" dado c

**Ventajas del discriminador condicionado:**

1. **Verificación de consistencia:**
   - D no solo pregunta "¿es realista?"
   - También pregunta "¿es un 7 realista?" (si c=7)
   - Si G genera un 3 cuando c=7, D lo rechaza aunque el 3 sea perfecto

2. **Reduce mode collapse:**
   - G no puede generar solo un tipo de imagen
   - Debe aprender a generar todas las clases porque D verifica la condición
   - Cada clase es una "tarea" separada

3. **Generación controlable:**
   - En inferencia: G(z, "gato") → imagen de gato
   - Permite aplicaciones prácticas como text-to-image

---

6. ¿Qué impacto tiene la arquitectura del generador en la calidad de las muestras generadas por una GAN? Da ejemplos de modificaciones comunes.

**Respuesta corta (para el parcial):**
> La arquitectura de G determina la capacidad de modelar distribuciones complejas. Modificaciones comunes: (1) DC-GAN: usar convoluciones transpuestas para expansión progresiva; (2) Batch Normalization entre capas para estabilidad; (3) Activaciones: ReLU intermedias, tanh en salida; (4) Skip connections (como en U-Net) para preservar detalles espaciales.

**Explicación detallada:**

El profesor y Juan hablaron específicamente de DC-GAN:

> "Dijimos que podía ser cualquier cosa que tenga parámetros y que sea derivable. Entonces, vamos a aprovechar que estamos usando imágenes y usar convoluciones."

**Impacto de la arquitectura:**

1. **Capacidad de representación:**
   - Más capas/parámetros = puede modelar distribuciones más complejas
   - Pero también más difícil de entrenar

2. **Estructura espacial:**
   - Convoluciones preservan relaciones espaciales (importante para imágenes)
   - Fully connected pierde información espacial

3. **Resolución de salida:**
   - La arquitectura determina qué tamaño de imagen puede generar
   - DC-GAN expande progresivamente: 4×4 → 8×8 → 16×16 → ...

**Modificaciones comunes:**

**1. DC-GAN (Deep Convolutional GAN):**
```
Z (100) → FC → reshape (128, 7, 7)
        → ConvTranspose (128 → 64) → 14×14
        → ConvTranspose (64 → 1) → 28×28
```
Juan explicó: "Las convoluciones, pero para el otro lado" - convoluciones transpuestas que expanden en lugar de reducir.

**2. Batch Normalization:**
- Normaliza activaciones entre capas
- Estabiliza gradientes
- Acelera convergencia
- Se usa en todas las capas excepto salida de G y entrada de D

**3. Activaciones:**
- **Intermedias en G:** ReLU o LeakyReLU
- **Salida de G:** tanh (para salida en [-1, 1])
- **En D:** LeakyReLU (permite gradientes negativos pequeños)

**4. Progressive Growing (ProGAN):**
- Empieza generando 4×4
- Gradualmente agrega capas para mayor resolución
- Permite generar imágenes de muy alta resolución

---

7. ¿Por qué las GANs pueden ser más difíciles de entrenar que otros modelos generativos como los VAEs?

**Respuesta corta (para el parcial):**
> GANs son más difíciles porque: (1) Optimización adversarial en vez de loss directa - no hay garantía de convergencia; (2) Requiere balancear dos redes con objetivos opuestos; (3) Propenso a mode collapse; (4) No hay métrica clara de progreso - la loss no indica calidad; (5) Sensible a hiperparámetros. VAEs tienen loss bien definida y entrenamiento estable con gradiente descendente estándar.

**Explicación detallada:**

El profesor y Juan fueron muy claros sobre la dificultad:

> "Es un arte encontrar los hiperparámetros correctos."

> "Literalmente es mejor arrancar el entrenamiento de nuevo que intentar recuperarse."

**¿Por qué VAE es más fácil?**

1. **Loss bien definida:** Loss = Reconstrucción + KL
   - Ambos términos tienen significado claro
   - Se minimizan con gradiente descendente estándar

2. **Un solo modelo:** Encoder-Decoder se entrenan juntos
   - No hay competencia
   - Los gradientes fluyen normalmente

3. **Convergencia garantizada:**
   - Loss siempre puede bajar
   - El entrenamiento progresa monotónicamente

**¿Por qué GAN es más difícil?**

**1. Optimización adversarial:**
- No es minimización estándar, es un juego min-max
- No hay garantía de convergencia a un equilibrio

**2. Balance de dos redes:**
- G y D tienen objetivos opuestos
- Si una domina, la otra no puede mejorar
- El "punto dulce" es difícil de mantener

**3. Mode collapse:**
- G puede colapsar a generar un solo tipo de dato
- La loss no detecta esto (D puede estar confundido pero G no es diverso)

**4. La loss no indica calidad:**
> "Las pérdidas de G y D oscilan y no necesariamente una pérdida baja significa mejor modelo."

- Solo mirando la loss no sabes si las imágenes son buenas
- Necesitas inspección visual constante

**5. Sensibilidad a hiperparámetros:**
- Learning rates, arquitecturas, batch size, K...
- Pequeños cambios pueden hacer que el entrenamiento falle completamente

**6. No hay métrica directa de verosimilitud:**
- VAE maximiza log P(x) directamente
- GAN optimiza un juego, no una verosimilitud clara

---

### Diffusion Models

1. Describe el proceso de generación en un modelo de difusión.

**Respuesta corta (para el parcial):**
> El proceso de generación (backward/reverse diffusion) parte de ruido puro X_T ~ N(0,1) y aplica T pasos de "denoising". En cada paso t→t-1, el modelo predice el ruido en X_t y lo remueve parcialmente: X_{t-1} = f(X_t, ruido_predicho, t). Después de T pasos (~1000), se obtiene X_0 que es una imagen limpia.

**Explicación detallada:**

El profesor explicó la idea central:

> "Comenzar con ruido puro y refinarlo gradualmente para generar datos como imágenes."

**El proceso tiene dos fases:**

**Forward Diffusion (durante entrenamiento):**
- Tomamos una imagen real X_0
- Agregamos ruido gaussiano gradualmente en T pasos
- Al final, X_T es ruido puro N(0,1)
- Esto se usa para crear datos de entrenamiento

**Backward/Reverse Diffusion (generación):**

Este es el proceso de generación propiamente dicho:

```
Paso 1: Muestrear X_T ~ N(0,1)  # Ruido puro

Paso 2: Para t = T hasta 1:
    - Modelo predice el ruido en X_t
    - Calcular X_{t-1} = quitar_ruido(X_t, ruido_predicho, t)

Paso 3: X_0 es la imagen generada
```

**Pseudocódigo detallado:**

```python
def generar_imagen(modelo, T, betas):
    # 1. Partir de ruido puro
    x_T = torch.randn(shape_imagen)  # N(0,1)
    x_actual = x_T

    # 2. Iterar quitando ruido
    for t in range(T, 0, -1):
        # 2.1 Predecir ruido presente
        ruido_predicho = modelo(x_actual, t)

        # 2.2 Calcular imagen menos ruidosa
        media = calcular_media(x_actual, ruido_predicho, t, betas)

        # 2.3 Agregar ruido estocástico (excepto último paso)
        if t > 1:
            z = torch.randn_like(x_actual)
            x_anterior = media + sqrt(varianza[t]) * z
        else:
            x_anterior = media

        x_actual = x_anterior

    # 3. Retornar imagen limpia
    return x_actual  # x_0
```

**¿Por qué funciona?**

El profesor explicó: "El dato tiene la misma estructura que el latente... arranco una imagen que es ruido y le voy pasando varias iteraciones donde voy eliminando el ruido."

El modelo aprendió durante entrenamiento cómo se ve el proceso de agregar ruido. En generación, invierte ese proceso paso a paso.

---

2. Compara los modelos de difusión con GANs en términos de estabilidad de entrenamiento y calidad de las muestras generadas.

**Respuesta corta (para el parcial):**
> **Estabilidad:** Difusión es mucho más estable - optimiza loss de denoising directa (MSE) sin adversario; GAN es inestable por naturaleza adversarial y balance de redes. **Calidad:** Difusión produce muestras más diversas y realistas; GAN puede generar muestras nítidas pero sufre mode collapse. **Trade-off:** Difusión es lento en generación (T pasos); GAN genera en una pasada.

**Explicación detallada:**

El profesor destacó las ventajas de los modelos de difusión:

> "Son más eficientes en el entrenamiento, tienen un entrenamiento más estable y producen salidas más diversas y realistas."

**Estabilidad de entrenamiento:**

**GANs:**
- Entrenamiento adversarial: juego min-max sin garantía de convergencia
- Requiere balancear dos redes con objetivos opuestos
- Sensible a hiperparámetros
- "Literalmente es mejor arrancar de nuevo que intentar recuperarse"

**Difusión:**
- Loss directa: MSE entre ruido real y ruido predicho
- Un solo modelo, sin competencia
- Entrenamiento estándar con gradiente descendente
- Progreso más predecible y monotónico

> "Cualquier par de puntos del camino me sirven como dato de entrenamiento. Son independientes."

**Calidad de muestras:**

**GANs:**
- Puede producir imágenes muy nítidas (a veces mejor que datos reales)
- Propenso a mode collapse (poca diversidad)
- Los artefactos son consistentes y a veces detectables

**Difusión:**
- Produce muestras muy diversas (cubre bien la distribución)
- Alta fidelidad a los datos reales
- Diversidad inherente al proceso estocástico

**Velocidad de generación:**

**GANs:**
- Una sola pasada: z → G(z) → imagen
- Muy rápido (milisegundos)

**Difusión:**
- T pasos iterativos (~1000)
- Mucho más lento (segundos a minutos)
- Trade-off: calidad vs velocidad

**Resumen:**

| Aspecto | GAN | Difusión |
|---------|-----|----------|
| Estabilidad | Baja | Alta |
| Diversidad | Riesgo de mode collapse | Alta |
| Velocidad | Rápida | Lenta |
| Facilidad de entrenamiento | Difícil | Más fácil |

---

3. Dado un modelo de difusión entrenado, diseña un procedimiento para ajustar su rendimiento en un nuevo conjunto de datos con una distribución ligeramente diferente.

**Respuesta corta (para el parcial):**
> Fine-tuning: (1) Partir del modelo pre-entrenado; (2) Usar learning rate bajo (10-100x menor que entrenamiento original); (3) Entrenar en el nuevo dataset por pocas épocas; (4) Monitorear que no olvide características generales. Alternativa: mezclar datos nuevos con pequeña porción de datos originales para evitar "catastrophic forgetting".

**Explicación detallada:**

Aunque el profesor no cubrió fine-tuning en detalle, podemos aplicar principios generales de transfer learning:

**Procedimiento propuesto:**

**1. Evaluación inicial:**
- Generar muestras con el modelo pre-entrenado
- Evaluar qué tan diferentes son del nuevo dominio
- Identificar qué características necesitan ajuste

**2. Preparación del fine-tuning:**
```python
# Cargar modelo pre-entrenado
modelo = cargar_modelo_preentrenado()

# Reducir learning rate significativamente
lr_finetune = lr_original / 100  # Típicamente 10-100x menor

# Configurar optimizer
optimizer = Adam(modelo.parameters(), lr=lr_finetune)
```

**3. Estrategia de entrenamiento:**

**Opción A: Fine-tuning directo**
- Entrenar solo con datos nuevos
- Pocas épocas (el modelo ya sabe "denoising" general)
- Monitorear para evitar sobreajuste

**Opción B: Entrenamiento mixto (recomendado)**
- Mezclar datos nuevos con pequeña porción de datos originales (ej: 90% nuevos, 10% originales)
- Previene "catastrophic forgetting"
- Mantiene capacidades generales

**4. Monitoreo:**
- Loss de denoising en datos nuevos (debe bajar)
- Calidad visual de generaciones
- Opcional: generar algunas muestras del dominio original para verificar que no se olvidó

**5. Consideraciones especiales para difusión:**

- El schedule de ruido (betas) puede mantenerse igual
- Si los datos nuevos tienen diferente rango/escala, normalizar apropiadamente
- T (número de pasos) puede mantenerse igual

**Ventaja de difusión para transfer:**

El modelo aprende a predecir ruido, que es una tarea general. Las características específicas del dominio se capturan en cómo el modelo interpreta las imágenes a diferentes niveles de ruido. Esto hace que el transfer sea relativamente suave.

---

4. Explica cómo los modelos de difusión pueden generar imágenes o secuencias desde ruido, paso a paso. ¿Qué hace único este proceso comparado con GANs o VAEs?

**Respuesta corta (para el parcial):**
> Difusión: parte de ruido puro y lo refina en T pasos (~1000), quitando ruido gradualmente. Único: (1) El espacio latente tiene MISMA dimensión que el dato (no hay compresión); (2) Proceso iterativo vs una pasada; (3) Cada paso es una pequeña mejora, más controlable; (4) El modelo aprende transiciones locales, no la generación completa.

**Explicación detallada:**

El profesor explicó la diferencia fundamental:

> "A diferencia de VAEs: el espacio latente tiene la misma dimensionalidad que el dato original."

**El proceso paso a paso:**

```
t=T (ruido puro):  [ruido aleatorio - nada reconocible]
        ↓ modelo predice y remueve ruido
t=T-1:             [ruido con muy ligera estructura]
        ↓
t=T-2:             [formas muy borrosas empiezan a aparecer]
        ↓
...     ↓ (repite ~1000 veces)
...     ↓
t=10:              [imagen borrosa pero reconocible]
        ↓
t=5:               [detalles empiezan a definirse]
        ↓
t=1:               [imagen casi final, pequeños ajustes]
        ↓
t=0 (imagen):      [imagen limpia y detallada]
```

**¿Qué hace único a Difusión?**

**1. Espacio latente = espacio del dato:**

| Modelo | Espacio latente | Dato |
|--------|-----------------|------|
| VAE | Z de dimensión pequeña (ej: 100) | X de dimensión grande (ej: 784) |
| GAN | Z de dimensión pequeña (ej: 100) | X de dimensión grande (ej: 784) |
| Difusión | X_T de MISMA dimensión que X_0 | X de dimensión grande (ej: 784) |

**2. Generación iterativa:**

- **GAN:** Una pasada: z → G(z) → imagen
- **VAE:** Una pasada: z → Decoder(z) → imagen
- **Difusión:** T pasos: X_T → X_{T-1} → ... → X_1 → X_0

**3. El modelo aprende transiciones locales:**

- **GAN/VAE:** Aprenden a generar imagen completa de una vez
- **Difusión:** Aprende solo: "dado X_t con ruido, ¿cuál era X_{t-1} con menos ruido?"
- Tarea más simple y local

**4. Diversidad inherente:**

- Cada paso tiene componente estocástico
- Diferentes "caminos" de denoising llevan a diferentes imágenes
- Menos propenso a mode collapse que GAN

**5. Interpretabilidad:**

- Puedes ver el proceso de generación
- Puedes intervenir a mitad de camino
- El nivel de ruido controla qué tan "cercano" estás a una imagen

---

### Preguntas prácticas

1. Considera que un modelo GAN produce imágenes borrosas en lugar de detalladas. Propón dos estrategias para mejorar la calidad de las imágenes generadas.

**Respuesta corta (para el parcial):**
> Estrategias: (1) Aumentar capacidad del generador: más capas, más filtros convolucionales, arquitectura más profunda; (2) Mejorar el balance G-D: si D es muy débil, G no tiene incentivo para detalles - aumentar capacidad de D o entrenar D más veces (mayor K); (3) Usar técnicas como progressive growing (empezar con baja resolución y escalar).

**Explicación detallada:**

Las imágenes borrosas en GANs pueden tener varias causas:

**Causa 1: Generador con capacidad insuficiente**

El G no tiene suficientes parámetros para modelar los detalles finos.

**Solución: Aumentar capacidad de G**
```python
# Antes: G simple
self.conv1 = nn.ConvTranspose2d(latent_dim, 64, 4)
self.conv2 = nn.ConvTranspose2d(64, 1, 4)

# Después: G más profundo
self.conv1 = nn.ConvTranspose2d(latent_dim, 256, 4)
self.conv2 = nn.ConvTranspose2d(256, 128, 4)
self.conv3 = nn.ConvTranspose2d(128, 64, 4)
self.conv4 = nn.ConvTranspose2d(64, 1, 4)
```

**Causa 2: Discriminador demasiado débil**

Si D no puede detectar la diferencia entre imágenes nítidas y borrosas, G no tiene incentivo para mejorar los detalles.

**Solución: Mejorar D**
- Aumentar capacidad de D (más capas/filtros)
- Entrenar D más veces por cada vez que entrenas G (aumentar K)
- Usar arquitectura de D más sofisticada

**Causa 3: Colapso del entrenamiento temprano**

G converge a una solución "fácil" (imágenes borrosas que engañan a D).

**Solución: Progressive Growing**
```
Fase 1: Entrenar G y D para generar 4×4
Fase 2: Agregar capas, entrenar para 8×8
Fase 3: Agregar capas, entrenar para 16×16
...
Fase N: Entrenar para resolución final
```

**Otras mejoras:**
- Usar loss perceptual (comparar features de una red pre-entrenada)
- Batch Normalization apropiada
- Verificar normalización de datos ([-1, 1] con tanh en G)

---

2. Implementa en pseudocódigo el paso de inferencia de un modelo de difusión para generar nuevas muestras. Explica cada paso del proceso.

**Respuesta corta (para el parcial):**
```
función generar_imagen(modelo, T_pasos):
    x_T = muestrear_ruido_gaussiano()  # Paso 1: ruido puro N(0,1)
    x = x_T
    PARA t = T hasta 1:                 # Paso 2: iterar
        ruido_pred = modelo(x, t)       # 2a: predecir ruido
        x = quitar_ruido(x, ruido_pred, t)  # 2b: remover ruido
        si t > 1: x += ruido_estocástico    # 2c: agregar aleatoriedad
    retornar x                          # Paso 3: imagen final
```

**Explicación detallada:**

```python
def generar_imagen(modelo_denoising, T, betas):
    """
    Genera una imagen nueva usando un modelo de difusión entrenado.

    Parámetros:
    - modelo_denoising: Red neuronal que predice el ruido dado X_t y t
    - T: Número de pasos de difusión (típicamente 1000)
    - betas: Schedule de varianza para cada paso

    Retorna:
    - x_0: Imagen generada (limpia)
    """

    # ════════════════════════════════════════════════════════════
    # PASO 1: Partir de ruido puro
    # ════════════════════════════════════════════════════════════
    # Muestreamos de N(0,1) con la misma forma que la imagen deseada
    # Este ruido puro es nuestro "punto de partida" X_T
    x_T = muestrear_normal(media=0, varianza=1, forma=dimension_imagen)
    x_actual = x_T

    # ════════════════════════════════════════════════════════════
    # PASO 2: Iterar quitando ruido (de t=T hasta t=1)
    # ════════════════════════════════════════════════════════════
    PARA t DESDE T HASTA 1:

        # ─────────────────────────────────────────────────────────
        # Paso 2a: Predecir el ruido presente en x_actual
        # ─────────────────────────────────────────────────────────
        # El modelo recibe la imagen ruidosa Y el timestep t
        # t le dice al modelo "cuánto ruido hay aproximadamente"
        ruido_predicho = modelo_denoising(x_actual, t)

        # ─────────────────────────────────────────────────────────
        # Paso 2b: Calcular la imagen del paso anterior (menos ruidosa)
        # ─────────────────────────────────────────────────────────
        # Fórmula simplificada:
        # x_{t-1} = (1/√α_t) * (x_t - (β_t/√(1-ᾱ_t)) * ruido_predicho)

        alpha_t = 1 - betas[t]
        alpha_acumulado_t = producto(alpha_i para i=1 hasta t)

        media_estimada = (1/sqrt(alpha_t)) * (
            x_actual - (betas[t] / sqrt(1 - alpha_acumulado_t)) * ruido_predicho
        )

        # ─────────────────────────────────────────────────────────
        # Paso 2c: Agregar ruido estocástico (excepto en el último paso)
        # ─────────────────────────────────────────────────────────
        # Esto hace que cada generación sea diferente
        SI t > 1:
            z = muestrear_normal(0, 1, forma=dimension_imagen)
            varianza = betas[t]  # simplificado
            x_anterior = media_estimada + sqrt(varianza) * z
        SINO:
            # En el último paso, no agregamos ruido
            x_anterior = media_estimada

        x_actual = x_anterior

    # ════════════════════════════════════════════════════════════
    # PASO 3: Retornar la imagen generada
    # ════════════════════════════════════════════════════════════
    # Después de T pasos, x_actual es x_0: la imagen "limpia"
    x_0 = x_actual

    RETORNAR x_0
```

**Explicación de cada paso:**

1. **Ruido puro:** Partimos de ruido gaussiano porque el forward process termina en eso
2. **Predicción de ruido:** El modelo aprendió a detectar cuánto ruido hay
3. **Remoción de ruido:** Usamos la predicción para "retroceder" un paso
4. **Ruido estocástico:** Introduce variedad en las generaciones
5. **Imagen final:** Después de T iteraciones, tenemos una imagen realista

---

3. Implementa en pseudocódigo el proceso de generación de secuencias de un LM.

**Respuesta corta (para el parcial):**
```
función generar_secuencia(prompt, max_tokens):
    tokens = tokenizar(prompt)
    MIENTRAS len(tokens) < max_tokens:
        logits = modelo(tokens)           # Forward pass
        probabilidades = softmax(logits[-1])  # Solo último token
        nuevo_token = muestrear(probabilidades)  # Elegir siguiente
        SI nuevo_token == END: terminar
        tokens.agregar(nuevo_token)
    retornar destokenizar(tokens)
```

**Explicación detallada:**

El profesor explicó: "GPT, ¿cómo nos genera texto? Bueno, nos genera haciendo este tipo de muestreos, condicionando una palabra respecto a las anteriores."

```python
def generar_secuencia(prompt, modelo, tokenizer, max_tokens, temperatura=1.0, top_k=None):
    """
    Genera texto de forma autorregresiva usando un modelo de lenguaje.

    Parámetros:
    - prompt: Texto inicial (string)
    - modelo: Red neuronal que predice distribución del siguiente token
    - tokenizer: Convierte texto <-> tokens
    - max_tokens: Máximo de tokens a generar
    - temperatura: Controla aleatoriedad (menor = más determinístico)
    - top_k: Si se especifica, solo considera los K tokens más probables

    Retorna:
    - texto_generado: String con el texto completo
    """

    # ════════════════════════════════════════════════════════════
    # PASO 1: Tokenizar el prompt inicial
    # ════════════════════════════════════════════════════════════
    # Convertir texto a secuencia de IDs numéricos
    secuencia = tokenizer.encode(prompt)  # Ej: "Hola" → [15432]

    # ════════════════════════════════════════════════════════════
    # PASO 2: Generar tokens uno a uno (autorregresivo)
    # ════════════════════════════════════════════════════════════
    MIENTRAS longitud(secuencia) < max_tokens:

        # ─────────────────────────────────────────────────────────
        # Paso 2a: Forward pass - obtener predicciones del modelo
        # ─────────────────────────────────────────────────────────
        # El modelo recibe toda la secuencia actual
        # Devuelve logits para cada posición (predicción del siguiente)
        logits = modelo.forward(secuencia)  # Shape: (seq_len, vocab_size)

        # ─────────────────────────────────────────────────────────
        # Paso 2b: Tomar solo los logits de la última posición
        # ─────────────────────────────────────────────────────────
        # Queremos predecir el SIGUIENTE token
        # Los logits de la posición -1 predicen qué viene después
        logits_siguiente = logits[-1]  # Shape: (vocab_size,)

        # ─────────────────────────────────────────────────────────
        # Paso 2c: Aplicar temperatura (opcional)
        # ─────────────────────────────────────────────────────────
        # Temperatura < 1: más determinístico (picos más pronunciados)
        # Temperatura > 1: más aleatorio (distribución más uniforme)
        logits_siguiente = logits_siguiente / temperatura

        # ─────────────────────────────────────────────────────────
        # Paso 2d: Convertir logits a probabilidades con softmax
        # ─────────────────────────────────────────────────────────
        probabilidades = softmax(logits_siguiente)

        # ─────────────────────────────────────────────────────────
        # Paso 2e: Aplicar top-k filtering (opcional)
        # ─────────────────────────────────────────────────────────
        SI top_k no es None:
            # Solo mantener los k tokens más probables
            # Poner probabilidad 0 al resto
            indices_ordenados = argsort(probabilidades, descendente=True)
            probabilidades[indices_ordenados[top_k:]] = 0
            # Re-normalizar
            probabilidades = probabilidades / suma(probabilidades)

        # ─────────────────────────────────────────────────────────
        # Paso 2f: Muestrear un token de la distribución
        # ─────────────────────────────────────────────────────────
        # Elegir aleatoriamente según las probabilidades
        nuevo_token = muestrear_categorica(probabilidades)

        # ─────────────────────────────────────────────────────────
        # Paso 2g: Verificar si es token de fin
        # ─────────────────────────────────────────────────────────
        SI nuevo_token == tokenizer.END_TOKEN:
            SALIR DEL BUCLE

        # ─────────────────────────────────────────────────────────
        # Paso 2h: Agregar el nuevo token a la secuencia
        # ─────────────────────────────────────────────────────────
        secuencia.agregar(nuevo_token)

    # ════════════════════════════════════════════════════════════
    # PASO 3: Destokenizar y retornar
    # ════════════════════════════════════════════════════════════
    # Convertir la secuencia de IDs de vuelta a texto
    texto_generado = tokenizer.decode(secuencia)

    RETORNAR texto_generado
```

**Puntos clave que mencionó el profesor:**

1. **Es autorregresivo:** "La probabilidad de un evento siguiente depende solo del inmediato anterior" (en realidad, de todos los anteriores en el contexto)

2. **No hay diferencia por arquitectura:** "¿Existe alguna diferencia a la hora de muestrear si este LM es un transformer, un MLP o una RNN? No hay diferencia. El proceso de muestreo es agnóstico de la arquitectura."

3. **Por qué es lento:** "No puedes paralelizar la generación. Necesitas la palabra 3 antes de darte la 4."

---

### Transformers (basado en clase 25-11-2025)

1. ¿Por qué se necesita el Positional Encoding en los Transformers?

**Respuesta corta (para el parcial):**
> El self attention es invariante bajo permutación: si entrevero las palabras, la matriz entrevera pero da los mismos valores. Como no hay recurrencia (se pasa la frase entera), necesito marcar la posición temporal de cada palabra para que pierda esa invariancia.

**Explicación detallada:**

Como explicó el profesor: "El self attention es invariante bajo permutación así tal cual lo definimos. Entonces si yo entrevero las palabras, la matriz entrevera, pero me da los mismos valores."

**El problema:**
- En los Transformers no hay ningún tipo de recurrencia
- Se le pasa la frase entera de una sola vez
- Sin marcas de posición, el modelo no sabe en qué orden están las palabras

**La solución:**
- Se agrega un positional encoding que marca en qué posición está cada palabra
- Esto se suma al embedding de cada palabra
- Así el modelo pierde la invariancia a permutaciones

---

2. ¿Qué es y para qué sirve el Masked Multi-Head Attention en el Decoder?

**Respuesta corta (para el parcial):**
> Se enmascara la matriz de attention poniendo -∞ (que luego softmax convierte a 0) en todas las posiciones futuras. Esto evita que el modelo "haga trampa" mirando la palabra que tiene que predecir. Es necesario porque en inferencia no tendremos las palabras futuras.

**Explicación detallada:**

Como explicó el profesor: "En cada instante de tiempo no le vamos a permitir que mire la atención de las palabras que están hacia el futuro."

**¿Por qué es necesario?**
- En entrenamiento, el decoder recibe toda la secuencia target
- Si no enmascaramos, cuando tenga que predecir la palabra 3, podría mirar directamente la palabra 3 (que ya está en el input)
- "¿A qué le va a prestar más atención si su objetivo es predecir la palabra que va en el lugar 3 y vos le permitís mirar toda la secuencia? A la palabra 3. El attention te va a dar un uno gigante en la palabra tres."

**Implementación:**
- Se multiplica la matriz de attention por una máscara triangular inferior
- Todo lo que está de la diagonal para arriba se pone a -∞ ANTES del softmax
- Después del softmax, esos valores se convierten en 0

**¿Por qué replicamos la secuencialidad?**
- En inferencia, cuando queremos traducir, no tenemos las palabras target
- Solo tenemos el begin_of_sequence y vamos generando palabra por palabra
- "Si él aprende a mirar para adelante, no va a tener nada para adelante, va a hacer cualquier cosa"

---

3. Explique el proceso de inferencia en un Transformer para traducción (Seq2Seq).

**Respuesta corta (para el parcial):**
> En inferencia: (1) El encoder procesa la frase completa en español de una vez; (2) El decoder arranca solo con el token BEGIN_OF_SEQUENCE; (3) Se genera la primera palabra, se agrega al input del decoder; (4) Se repite hasta generar END_OF_SEQUENCE. El encoder no tiene loop, el decoder sí.

**Explicación detallada:**

Esta fue una discusión importante en clase. El profesor aclaró:

**Encoder (sin loop):**
- "La frase en español, ¿dónde la meto? En el encoder. Igual que en la RNN."
- Se procesa toda la frase de una vez
- Sale una matriz donde cada fila representa una palabra codificada

**Decoder (con loop):**
- "¿Qué va a entrar a la derecha? El begin_of_sequence. Sin eso no podés arrancar."
- "Es como que no tuvieras ruedas en el auto. Sin eso no podés arrancar."

**El proceso paso a paso:**
1. Encoder procesa frase en español → sale matriz de representaciones
2. Decoder recibe BEGIN_OF_SEQUENCE
3. Se hace el masked self-attention (pero solo hay un token)
4. Se hace attention con la salida del encoder
5. Se pasa por la capa lineal y softmax → probabilidad de cada palabra
6. Se elige la palabra más probable (o se muestrea)
7. Esa palabra se agrega al input del decoder
8. Se repite desde el paso 3 hasta que salga END_OF_SEQUENCE

**Diferencia importante con entrenamiento:**
- En entrenamiento: se pasa toda la frase target de una vez (con máscara)
- En inferencia: hay un loop porque no tenemos la frase target

---

4. ¿Cuántos parámetros tiene una capa de Multi-Head Attention?

**Respuesta corta (para el parcial):**
> Para H heads con D_model dimensión: 3×(D_model×D_k)×H + 3×D_k×H (biases) + D_model×D_model + D_model (Wo y bias). Típicamente D_k = D_model/H, entonces queda aproximadamente 4×D_model².

**Explicación detallada (del ejercicio en clase):**

El profesor hizo un ejercicio detallado con estos valores:
- D_model = 128
- H = 4 heads
- D_k = D_v = D_model/H = 32

**Matrices por cada head:**
- W_Q: 128 × 32 = 4,096 parámetros
- W_K: 128 × 32 = 4,096 parámetros
- W_V: 128 × 32 = 4,096 parámetros
- Biases: 32 + 32 + 32 = 96 parámetros

**Para 4 heads:**
- (4,096 × 3 + 96) × 4 = 49,152 + 384 = 49,536 parámetros

**Matriz de salida W_O:**
- W_O: 128 × 128 = 16,384 parámetros
- Bias: 128 parámetros

**Total Multi-Head Attention:**
- 49,536 + 16,384 + 128 = **66,048 parámetros**

---

5. ¿Cuál es la diferencia entre un modelo Seq2Seq con RNNs vs con Transformers?

**Respuesta corta (para el parcial):**
> Vistos como cajas negras son iguales: encoder codifica, decoder decodifica. La diferencia interna: RNN procesa secuencialmente token por token; Transformer procesa todo en paralelo. En entrenamiento, Transformer es más eficiente. En inferencia, ambos tienen un loop en el decoder.

**Explicación detallada:**

El profesor fue muy claro: "Si uno mira el encoder y el decoder como cajas negras es lo mismo. O sea, es lo mismo, solo que la caja negra de la RNN procesa el input paso a paso secuencialmente. Esto lo procesa todo de un saque."

**Similitudes:**
- Ambos son encoder-decoder
- El encoder produce una representación de la entrada
- El decoder genera la salida condicionado en esa representación
- En inferencia, ambos necesitan un loop para generar palabra por palabra

**Diferencias:**

| Aspecto | RNN Seq2Seq | Transformer |
|---------|-------------|-------------|
| Procesamiento encoder | Secuencial | Paralelo |
| Contexto que ve | Hidden comprimido | Toda la secuencia |
| Attention | Hidden actual vs encoder | Todos vs todos |
| Paralelización entrenamiento | Limitada | Alta |
| Máscaras | No necesarias | Necesarias en decoder |

**Sobre el attention:**
- En RNN: "Mirábamos el hidden del decoder y se miraba el attention de ese hidden con los del encoder"
- En Transformer: "Se hace un self attention de todos contra todos, pero masqueado"

---

6. ¿Para qué sirven los tokens especiales BEGIN_OF_SEQUENCE y END_OF_SEQUENCE?

**Respuesta corta (para el parcial):**
> BEGIN_OF_SEQUENCE: señal de inicio para el decoder, permite generar la primera palabra cuando no hay contexto previo. END_OF_SEQUENCE: indica que la secuencia terminó, permite que la salida tenga longitud variable diferente a la entrada.

**Explicación detallada:**

El profesor explicó claramente por qué son necesarios:

**BEGIN_OF_SEQUENCE:**
- "¿Qué va a entrar en el decoder? El begin_of_sequence. Sin eso no podés arrancar."
- "Es como que no tuvieras ruedas en el auto."
- Problema: para predecir la primera palabra, necesitas un input
- Solución: el token BEGIN le dice al modelo "empieza a generar"

**END_OF_SEQUENCE:**
- Permite que la salida tenga longitud diferente a la entrada
- "Una frase de cinco palabras en inglés podría traducirse en francés a algo de ocho palabras"
- El modelo genera hasta que produce END_OF_SEQUENCE
- "La última no hay una próxima, entonces por eso necesitás el END"

**En el decoder durante entrenamiento:**
- Entrada: [BEGIN, palabra1, palabra2, ..., palabra_n]
- Salida esperada: [palabra1, palabra2, ..., palabra_n, END]
- La entrada tiene uno más que la salida que queremos predecir

---

7. ¿Por qué una red más profunda puede entrenar peor que una más superficial? (Degradación vs Overfitting)

**Respuesta corta (para el parcial):**
> No es overfitting: incluso en TRAIN la red profunda tiene peor loss. Es el problema de degradación por vanishing gradient: los gradientes se hacen muy pequeños y la red no puede aprender. La solución son las skip connections (ResNet) que permiten que los gradientes fluyan directamente.

**Explicación detallada:**

El profesor enfatizó que esto NO es overfitting:

**¿Por qué en teoría debería funcionar?**
- "La capa del medio podría ser la identidad, entonces el modelo se te reduce al que tiene una capa menos"
- "Todo lo que puedas expresar con dos capas lo puedes expresar con tres"
- Más capas = más capacidad representacional

**¿Por qué en la práctica falla?**
- El problema es el **vanishing gradient**
- "Cuando tenés muchas capas, se estanca antes"
- "En train no lograbas bajar" la loss
- Los gradientes se hacen muy pequeños y la red no aprende

**Diferencia con overfitting:**
- En overfitting: train loss baja, test loss sube
- En degradación: train loss SE ESTANCA, no baja
- "El que tenía más capas quedaba más corrido [peor] pero llegaba igual"

**La solución (Skip Connections):**
- Las ResNets aprenden "cuánto te desvías de la identidad"
- Los gradientes pueden fluir directamente saltando capas
- Permite entrenar redes muy profundas sin degradación

---

8. ¿Qué es el Layer Normalization y cuántos parámetros tiene?

**Respuesta corta (para el parcial):**
> Normaliza fila a fila (palabra a palabra): resta la media de la fila, divide por desviación estándar, multiplica por gamma y suma beta. Tiene 2×D_model parámetros (gamma y beta son vectores de dimensión D_model).

**Explicación detallada:**

Del ejercicio en clase:

**Operación:**
- Para cada fila (cada palabra): resta la media de esa fila
- Divide entre la desviación estándar de esa fila
- Multiplica por γ (gamma) - elemento a elemento
- Suma β (beta) - elemento a elemento

**Parámetros:**
- γ (gamma): vector de dimensión D_model
- β (beta): vector de dimensión D_model
- Total: 2 × D_model parámetros

**En el ejemplo de clase (D_model = 128):**
- 2 × 128 = 256 parámetros por Layer Norm

**Ubicación en el Transformer:**
- En el encoder: 2 Layer Norms por bloque (después de attention, después de FFN)
- En el decoder: 3 Layer Norms por bloque (después de masked attention, después de cross-attention, después de FFN)

---

9. ¿Qué es el Feed Forward Network en el Transformer y cómo funciona?

**Respuesta corta (para el parcial):**
> Es un MLP de dos capas que se aplica a cada palabra (fila) por separado. Va de D_model → D_ff → D_model con activación (ReLU o GELU). Tiene (D_model × D_ff + D_ff) + (D_ff × D_model + D_model) parámetros.

**Explicación detallada:**

Del ejercicio en clase:

**Arquitectura:**
- Es "un MLP de dos capas, solo tiene el input y el output layer"
- Capa 1: D_model → D_ff (típicamente D_ff = 4 × D_model)
- Activación: ReLU o GELU
- Capa 2: D_ff → D_model

**Punto importante:**
- "Es la misma fit forward que se aplica a cada una de las palabras"
- "No es una fit forward global, sino que es la misma fit forward que se aplica a cada palabra"
- Se aplica fila por fila (palabra por palabra)

**Cálculo de parámetros (del ejercicio con D_model=128, D_ff=512):**
- Capa 1: (128 + 1) × 512 = 66,048 parámetros
- Capa 2: (512 + 1) × 128 = 65,664 parámetros
- Total: 131,712 parámetros

**¿Por qué funciona por fila?**
- "El hecho de que las filas sean las palabras de la frase es lo que hace que esto pueda consumir una frase de cualquier longitud"
- "En todas estas multiplicaciones el N [largo de la frase] quedó peladito ahí siempre"

---

10. ¿Qué beneficios tiene un modelo encoder-decoder para problemas Seq2Seq frente a un modelo que emite un output en cada paso?

**Respuesta corta (para el parcial):**
> El encoder-decoder permite que la salida tenga longitud diferente a la entrada. Un modelo que emite output en cada paso está limitado a que la salida tenga el mismo largo que la entrada. Crucial para traducción donde las frases pueden tener longitudes muy diferentes.

**Explicación detallada:**

Como explicó el profesor:

**El problema:**
- "La salida puede ser distinto largo"
- "En caso de traducción que lo querés pasar de español a inglés, la frase en español puede ser más larga que la frase en inglés"

**Si emites un output por cada paso de entrada:**
- La cantidad de pasos = largo de la secuencia de entrada
- Tendrías un output por el largo del español
- "Si es una frase más larga [la salida], no podría seguir"

**Solución del encoder-decoder:**
- El encoder comprime toda la entrada a un espacio latente
- El decoder decodifica de manera independiente al largo de entrada
- Genera hasta encontrar END_OF_SEQUENCE
- Permite longitudes completamente diferentes

---

11. ¿Qué representa la matriz de attention en un modelo Seq2Seq?

**Respuesta corta (para el parcial):**
> Cada fila representa una palabra del decoder y cada columna una palabra del encoder. El valor en (i,j) indica cuánta atención le presta la palabra i del decoder a la palabra j del encoder al momento de generar la traducción.

**Explicación detallada:**

Como explicó el profesor con el ejemplo de traducción:

**Cómo leer la matriz:**
- Las filas: palabras que queremos predecir (output)
- Las columnas: palabras del input (encoder)
- "Vas a mirar la palabra [que querés predecir], o sea, la palabra que querés predecir. Vas a mirar el attention de esa posición con los hidden de todas estas palabras [del input]"

**Ejemplo práctico:**
- Si traducimos "The book that the professor recommended" → "El libro que recomendó el profesor"
- La fila de "libro" debería tener alta atención en "book"
- La fila de "recomendó" debería tener alta atención en "recommended"

**En Transformers:**
- Además del attention encoder-decoder, hay self-attention
- Self-attention: "todos contra todos" dentro de la misma secuencia
- Cross-attention: palabras del decoder vs palabras del encoder

---

12. ¿Qué pasaría en una RNN si la matriz B (de input a hidden) fuese la matriz nula?

**Respuesta corta (para el parcial):**
> Si B = 0, la RNN ignora completamente el input y se convierte en un MLP simple. No habría propagación temporal de la información del input, solo pasaría información a través de la matriz A (hidden a hidden).

**Explicación detallada:**

Del ejercicio de la guía:

La ecuación de una RNN es:
```
h_t = f(A × h_{t-1} + B × x_t + bias)
```

**Si B = 0:**
- El término B × x_t desaparece
- No entra ninguna información del input x_t
- Solo queda: h_t = f(A × h_{t-1} + bias)
- "Es un MLP" - se pierde toda la capacidad de procesar secuencias

**Punto importante:**
- La matriz B es la que permite que la información del input fluya al hidden state
- Sin ella, el modelo no puede "ver" los datos de entrada
