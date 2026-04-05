# Preguntas ejemplo parcial

## IA Generativa

---

### Language Models

1. Explica cómo funcionan los modelos autorregresivos generativos con variables discretas y explique cual es la función de pérdida.

2. Diseña un esquema para preprocesar datos de texto para entrenar un modelo de lenguaje autoregresivo, considerando un vocabulario discreto. Describe cada paso y su importancia.

3. En el contexto de los modelos autoregresivos, ¿cómo afecta la elección del tamaño del vocabulario a la complejidad del modelo y a su capacidad de generalización?

4. Propón una métrica que usarías para evaluar un modelo autoregresivo generativo en un problema de predicción de secuencias. Justifica tu elección.

5. ¿Cómo afectaría el uso de un modelo autoregresivo como GPT-2 en lugar de un LSTM en términos de captura de dependencias de largo alcance en un texto?

---

### Variational Autoencoders (VAE)

1. Describe el papel de las distribuciones gaussianas en los VAEs y explica cómo el truco de la reparametrización permite entrenar estos modelos con backpropagation.

2. Dado un conjunto de datos de imágenes, ¿qué preprocesamientos aplicarías para entrenar un VAE? Explica cómo la dimensionalidad de los datos afecta el diseño del modelo.

3. ¿Por qué es importante equilibrar los términos de reconstrucción y regularización en la función de pérdida de un VAE? Proporciona un ejemplo práctico para ilustrar esto.

4. Diseña un experimento práctico para medir el impacto del tamaño de la latente en un VAE. Describe cómo interpretarías los resultados.

---

### Generative Adversarial Networks (GAN)

1. Explica cómo el entrenamiento competitivo entre el generador y el discriminador en una GAN puede llevar a inestabilidad. Proporciona dos soluciones comunes para mitigar este problema.

2. ¿Qué es el colapso del modo en una GAN y cómo se puede mitigar?

3. Explica el papel del discriminador en una GAN. ¿Qué debe aprender el discriminador para que el generador mejore su rendimiento?

4. En una GAN, ¿cómo afecta el balance entre el generador y el discriminador al éxito del entrenamiento?

5. Compara las GANs estándar con las GANs condicionales. ¿Cuáles son las ventajas de usar un discriminador condicionado?

6. ¿Qué impacto tiene la arquitectura del generador en la calidad de las muestras generadas por una GAN? Da ejemplos de modificaciones comunes.

7. ¿Por qué las GANs pueden ser más difíciles de entrenar que otros modelos generativos como los VAEs?

---

### Diffusion Models

1. Describe el proceso de generación en un modelo de difusión.

2. Compara los modelos de difusión con GANs en términos de estabilidad de entrenamiento y calidad de las muestras generadas.

3. Dado un modelo de difusión entrenado, diseña un procedimiento para ajustar su rendimiento en un nuevo conjunto de datos con una distribución ligeramente diferente.

4. Explica cómo los modelos de difusión pueden generar imágenes o secuencias desde ruido, paso a paso. ¿Qué hace único este proceso comparado con GANs o VAEs?

---

### Preguntas prácticas

1. Considera que un modelo GAN produce imágenes borrosas en lugar de detalladas. Propón dos estrategias para mejorar la calidad de las imágenes generadas.

2. Implementa en pseudocódigo el paso de inferencia de un modelo de difusión para generar nuevas muestras. Explica cada paso del proceso.

3. Implementa en pseudocódigo el proceso de generación de secuencias de un LM.
