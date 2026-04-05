# Preguntas ejemplo parcial — Solo respuestas cortas

## IA Generativa

---

## Language Models

### 1. Explica cómo funcionan los modelos autorregresivos generativos con variables discretas y explique cual es la función de pérdida.

> Los modelos autorregresivos generan datos secuencialmente: cada variable Xi depende de las anteriores. Usando la regla del producto: P(X) = P(X₁) × P(X₂|X₁) × ... × P(Xₙ|X₁,...,Xₙ₋₁). La función de pérdida es la Negative Log-Likelihood: J(θ) = -(1/N) × Σ Σ log P_θ(xᵢ | x<i), que para variables binarias se implementa como Binary Cross-Entropy.

---

### 2. Diseña un esquema para preprocesar datos de texto para entrenar un modelo de lenguaje autoregresivo, considerando un vocabulario discreto. Describe cada paso y su importancia.

> El preprocesamiento incluye: (1) Tokenización: dividir texto en unidades (palabras/subpalabras/caracteres) y mapearlas a números; (2) Construcción del vocabulario: crear diccionario token→ID único; (3) Agregar tokens especiales (START, END, PAD, UNK); (4) Crear pares entrada-salida desplazados para entrenar la predicción del siguiente token.

---

### 3. En el contexto de los modelos autoregresivos, ¿cómo afecta la elección del tamaño del vocabulario a la complejidad del modelo y a su capacidad de generalización?

> Vocabulario grande: más parámetros en la capa de salida (softmax sobre V tokens), mejor representación de palabras raras, pero mayor riesgo de overfitting y más costoso. Vocabulario pequeño: menos parámetros, secuencias más largas (una palabra puede ser varios tokens), pero mejor generalización. El balance típico es usar sub-palabras (BPE/WordPiece).

---

### 4. Propón una métrica que usarías para evaluar un modelo autoregresivo generativo en un problema de predicción de secuencias. Justifica tu elección.

> Perplexity (perplejidad): mide qué tan "sorprendido" está el modelo ante secuencias reales. Perplexity = exp(-(1/N) × Σ log P(xᵢ|x<i)). Menor perplexity = mejor modelo. Es apropiada porque mide directamente la verosimilitud que el modelo asigna a datos reales, que es exactamente lo que optimizamos durante el entrenamiento.

---

### 5. ¿Cómo afectaría el uso de un modelo autoregresivo como GPT-2 en lugar de un LSTM en términos de captura de dependencias de largo alcance en un texto?

> GPT-2 (Transformer) captura mucho mejor las dependencias de largo alcance gracias al mecanismo de atención, que permite acceder directamente a cualquier posición previa. LSTM sufre de vanishing gradients y pierde información en secuencias largas porque procesa secuencialmente. GPT-2 puede atender a miles de tokens previos; LSTM prácticamente pierde información después de ~100 tokens.

---

## Variational Autoencoders (VAE)

### 1. Describe el papel de las distribuciones gaussianas en los VAEs y explica cómo el truco de la reparametrización permite entrenar estos modelos con backpropagation.

> En VAE, el encoder produce μ y σ (parámetros de una gaussiana), y Z se muestrea de N(μ,σ). El problema: no se puede hacer backpropagation a través de un muestreo aleatorio. El truco de reparametrización: Z = μ + σ × ε, donde ε ~ N(0,1) es fijo. Así la aleatoriedad no depende de los parámetros θ y los gradientes pueden fluir.

---

### 2. Dado un conjunto de datos de imágenes, ¿qué preprocesamientos aplicarías para entrenar un VAE? Explica cómo la dimensionalidad de los datos afecta el diseño del modelo.

> Preprocesamientos: normalizar píxeles al rango [0,1] o [-1,1], redimensionar a tamaño fijo, posiblemente convertir a escala de grises. La dimensionalidad del dato (ej: 28×28×1 = 784) determina el tamaño del encoder/decoder. La dimensionalidad del latente Z es un hiperparámetro: Z grande = más capacidad pero más parámetros; Z pequeño = mejor compresión pero posible pérdida de información.

---

### 3. ¿Por qué es importante equilibrar los términos de reconstrucción y regularización en la función de pérdida de un VAE? Proporciona un ejemplo práctico para ilustrar esto.

> Loss_VAE = Reconstrucción + KL_Divergence. Si domina reconstrucción: reconstrucciones perfectas pero espacio latente caótico, no se puede generar. Si domina KL: espacio latente organizado como N(0,1) pero reconstrucciones borrosas/malas. El balance permite tanto buena reconstrucción como generación válida al muestrear de N(0,1).

---

### 4. Diseña un experimento práctico para medir el impacto del tamaño de la latente en un VAE. Describe cómo interpretarías los resultados.

> Experimento: entrenar VAEs idénticos pero con latente_dim = 2, 10, 50, 100, 500. Medir: (1) loss de reconstrucción final, (2) loss KL, (3) calidad visual de reconstrucciones y generaciones, (4) FID si es posible. Interpretación: latente muy pequeña → alta reconstrucción loss, imágenes borrosas; latente muy grande → KL difícil de minimizar, posible colapso posterior; óptimo en el medio.

---

## Generative Adversarial Networks (GAN)

### 1. Explica cómo el entrenamiento competitivo entre el generador y el discriminador en una GAN puede llevar a inestabilidad. Proporciona dos soluciones comunes para mitigar este problema.

> La inestabilidad ocurre porque G y D tienen objetivos opuestos: si D se vuelve muy bueno, G no recibe gradientes útiles; si G domina, D no puede mejorar. Soluciones: (1) Learning rates diferentes (D más bajo que G, típicamente 10x menor); (2) Entrenar D más veces que G por iteración (ratio K); (3) Normalización de datos a [-1,1].

---

### 2. ¿Qué es el colapso del modo en una GAN y cómo se puede mitigar?

> Mode collapse ocurre cuando G genera solo un tipo de dato (ej: solo "3" en MNIST) porque engaña exitosamente a D con eso y no hay incentivo para diversidad. Mitigaciones: (1) GANs condicionales donde se especifica la clase a generar; (2) Agregar ruido a las imágenes durante entrenamiento; (3) Feature matching: comparar estadísticas de capas intermedias de D.

---

### 3. Explica el papel del discriminador en una GAN. ¿Qué debe aprender el discriminador para que el generador mejore su rendimiento?

> D es un clasificador binario que distingue imágenes reales de falsas. Debe aprender las características que hacen que una imagen sea "realista" vs "generada". Al entrenar D, este conocimiento se transfiere a G a través de los gradientes: cuando D rechaza una imagen falsa, los gradientes le dicen a G qué características le faltaron. D debe ser suficientemente bueno para dar feedback útil, pero no tan bueno que G no pueda mejorar.

---

### 4. En una GAN, ¿cómo afecta el balance entre el generador y el discriminador al éxito del entrenamiento?

> El balance es crucial: si D domina, G no recibe gradientes útiles y no mejora; si G domina, D pierde capacidad de dar feedback. El entrenamiento exitoso requiere que ambos mejoren gradualmente juntos. Se controla con: learning rates diferentes (D menor), ratio de entrenamiento K, y monitoreo constante de ambas losses.

---

### 5. Compara las GANs estándar con las GANs condicionales. ¿Cuáles son las ventajas de usar un discriminador condicionado?

> GAN estándar: G(z)→imagen, D(imagen)→real/falso. No hay control sobre qué genera. GAN condicional: G(z, clase)→imagen, D(imagen, clase)→real/falso Y consistente con clase. Ventajas: (1) Control sobre la generación especificando la clase; (2) Reduce mode collapse al forzar diversidad por clases; (3) D verifica consistencia imagen-clase, mejor supervisión.

---

### 6. ¿Qué impacto tiene la arquitectura del generador en la calidad de las muestras generadas por una GAN? Da ejemplos de modificaciones comunes.

> La arquitectura de G determina la capacidad de modelar distribuciones complejas. Modificaciones comunes: (1) DC-GAN: usar convoluciones transpuestas para expansión progresiva; (2) Batch Normalization entre capas para estabilidad; (3) Activaciones: ReLU intermedias, tanh en salida; (4) Skip connections (como en U-Net) para preservar detalles espaciales.

---

### 7. ¿Por qué las GANs pueden ser más difíciles de entrenar que otros modelos generativos como los VAEs?

> GANs son más difíciles porque: (1) Optimización adversarial en vez de loss directa - no hay garantía de convergencia; (2) Requiere balancear dos redes con objetivos opuestos; (3) Propenso a mode collapse; (4) No hay métrica clara de progreso - la loss no indica calidad; (5) Sensible a hiperparámetros. VAEs tienen loss bien definida y entrenamiento estable con gradiente descendente estándar.

---

## Diffusion Models

### 1. Describe el proceso de generación en un modelo de difusión.

> El proceso de generación (backward/reverse diffusion) parte de ruido puro X_T ~ N(0,1) y aplica T pasos de "denoising". En cada paso t→t-1, el modelo predice el ruido en X_t y lo remueve parcialmente: X_{t-1} = f(X_t, ruido_predicho, t). Después de T pasos (~1000), se obtiene X_0 que es una imagen limpia.

---

### 2. Compara los modelos de difusión con GANs en términos de estabilidad de entrenamiento y calidad de las muestras generadas.

> **Estabilidad:** Difusión es mucho más estable - optimiza loss de denoising directa (MSE) sin adversario; GAN es inestable por naturaleza adversarial y balance de redes. **Calidad:** Difusión produce muestras más diversas y realistas; GAN puede generar muestras nítidas pero sufre mode collapse. **Trade-off:** Difusión es lento en generación (T pasos); GAN genera en una pasada.

---

### 3. Dado un modelo de difusión entrenado, diseña un procedimiento para ajustar su rendimiento en un nuevo conjunto de datos con una distribución ligeramente diferente.

> Fine-tuning: (1) Partir del modelo pre-entrenado; (2) Usar learning rate bajo (10-100x menor que entrenamiento original); (3) Entrenar en el nuevo dataset por pocas épocas; (4) Monitorear que no olvide características generales. Alternativa: mezclar datos nuevos con pequeña porción de datos originales para evitar "catastrophic forgetting".

---

### 4. Explica cómo los modelos de difusión pueden generar imágenes o secuencias desde ruido, paso a paso. ¿Qué hace único este proceso comparado con GANs o VAEs?

> Difusión: parte de ruido puro y lo refina en T pasos (~1000), quitando ruido gradualmente. Único: (1) El espacio latente tiene MISMA dimensión que el dato (no hay compresión); (2) Proceso iterativo vs una pasada; (3) Cada paso es una pequeña mejora, más controlable; (4) El modelo aprende transiciones locales, no la generación completa.

---

## Preguntas prácticas

### 1. Considera que un modelo GAN produce imágenes borrosas en lugar de detalladas. Propón dos estrategias para mejorar la calidad de las imágenes generadas.

> Estrategias: (1) Aumentar capacidad del generador: más capas, más filtros convolucionales, arquitectura más profunda; (2) Mejorar el balance G-D: si D es muy débil, G no tiene incentivo para detalles - aumentar capacidad de D o entrenar D más veces (mayor K); (3) Usar técnicas como progressive growing (empezar con baja resolución y escalar).

---

### 2. Implementa en pseudocódigo el paso de inferencia de un modelo de difusión para generar nuevas muestras. Explica cada paso del proceso.

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

---

### 3. Implementa en pseudocódigo el proceso de generación de secuencias de un LM.

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

---

## Transformers (basado en clase 25-11-2025)

### 1. ¿Por qué se necesita el Positional Encoding en los Transformers?

> El self attention es invariante bajo permutación: si entrevero las palabras, la matriz entrevera pero da los mismos valores. Como no hay recurrencia (se pasa la frase entera), necesito marcar la posición temporal de cada palabra para que pierda esa invariancia.

---

### 2. ¿Qué es y para qué sirve el Masked Multi-Head Attention en el Decoder?

> Se enmascara la matriz de attention poniendo -∞ (que luego softmax convierte a 0) en todas las posiciones futuras. Esto evita que el modelo "haga trampa" mirando la palabra que tiene que predecir. Es necesario porque en inferencia no tendremos las palabras futuras.

---

### 3. Explique el proceso de inferencia en un Transformer para traducción (Seq2Seq).

> En inferencia: (1) El encoder procesa la frase completa en español de una vez; (2) El decoder arranca solo con el token BEGIN_OF_SEQUENCE; (3) Se genera la primera palabra, se agrega al input del decoder; (4) Se repite hasta generar END_OF_SEQUENCE. El encoder no tiene loop, el decoder sí.

---

### 4. ¿Cuántos parámetros tiene una capa de Multi-Head Attention?

> Para H heads con D_model dimensión: 3×(D_model×D_k)×H + 3×D_k×H (biases) + D_model×D_model + D_model (Wo y bias). Típicamente D_k = D_model/H, entonces queda aproximadamente 4×D_model².

---

### 5. ¿Cuál es la diferencia entre un modelo Seq2Seq con RNNs vs con Transformers?

> Vistos como cajas negras son iguales: encoder codifica, decoder decodifica. La diferencia interna: RNN procesa secuencialmente token por token; Transformer procesa todo en paralelo. En entrenamiento, Transformer es más eficiente. En inferencia, ambos tienen un loop en el decoder.

---

### 6. ¿Para qué sirven los tokens especiales BEGIN_OF_SEQUENCE y END_OF_SEQUENCE?

> BEGIN_OF_SEQUENCE: señal de inicio para el decoder, permite generar la primera palabra cuando no hay contexto previo. END_OF_SEQUENCE: indica que la secuencia terminó, permite que la salida tenga longitud variable diferente a la entrada.

---

### 7. ¿Por qué una red más profunda puede entrenar peor que una más superficial? (Degradación vs Overfitting)

> No es overfitting: incluso en TRAIN la red profunda tiene peor loss. Es el problema de degradación por vanishing gradient: los gradientes se hacen muy pequeños y la red no puede aprender. La solución son las skip connections (ResNet) que permiten que los gradientes fluyan directamente.

---

### 8. ¿Qué es el Layer Normalization y cuántos parámetros tiene?

> Normaliza fila a fila (palabra a palabra): resta la media de la fila, divide por desviación estándar, multiplica por gamma y suma beta. Tiene 2×D_model parámetros (gamma y beta son vectores de dimensión D_model).

---

### 9. ¿Qué es el Feed Forward Network en el Transformer y cómo funciona?

> Es un MLP de dos capas que se aplica a cada palabra (fila) por separado. Va de D_model → D_ff → D_model con activación (ReLU o GELU). Tiene (D_model × D_ff + D_ff) + (D_ff × D_model + D_model) parámetros.

---

### 10. ¿Qué beneficios tiene un modelo encoder-decoder para problemas Seq2Seq frente a un modelo que emite un output en cada paso?

> El encoder-decoder permite que la salida tenga longitud diferente a la entrada. Un modelo que emite output en cada paso está limitado a que la salida tenga el mismo largo que la entrada. Crucial para traducción donde las frases pueden tener longitudes muy diferentes.

---

### 11. ¿Qué representa la matriz de attention en un modelo Seq2Seq?

> Cada fila representa una palabra del decoder y cada columna una palabra del encoder. El valor en (i,j) indica cuánta atención le presta la palabra i del decoder a la palabra j del encoder al momento de generar la traducción.

---

### 12. ¿Qué pasaría en una RNN si la matriz B (de input a hidden) fuese la matriz nula?

> Si B = 0, la RNN ignora completamente el input y se convierte en un MLP simple. No habría propagación temporal de la información del input, solo pasaría información a través de la matriz A (hidden a hidden).
