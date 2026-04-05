## Explicación / Justificación de la notebook

### Objetivo

Demostrar empíricamente los problemas de Vanilla GAN y WGAN, y cómo WGAN-GP los resuelve. Para esto se entrenaron los tres modelos bajo las mismas condiciones y se compararon métricas específicas.

### Dataset

Se eligió CIFAR-10 (imágenes a color 32×32) en lugar de MNIST porque su mayor complejidad hace más evidentes las diferencias entre modelos. Las imágenes se normalizaron a [-1, 1] para coincidir con la salida Tanh del generador.

### Arquitectura

Se usó la misma arquitectura de generador para los tres modelos. Esto permite atribuir las diferencias en resultados exclusivamente a la función de pérdida, no a la arquitectura.

#### Generador (compartido)

Basado en la arquitectura DCGAN (Radford et al., 2015): convoluciones transpuestas que expanden el vector latente Z (128 dimensiones) hasta una imagen de 32×32×3. Cada capa usa BatchNorm y ReLU, excepto la última que usa Tanh para producir valores en [-1, 1].

#### Discriminador Vanilla GAN

Arquitectura espejo del generador: convoluciones que reducen la imagen hasta un escalar. Usa LeakyReLU (pendiente 0.2) y BatchNorm en capas internas. Termina en Sigmoid para producir probabilidades en [0, 1], como especifica el paper original de Goodfellow et al. (2014).

#### Crítico WGAN / WGAN-GP

Similar al discriminador pero sin Sigmoid al final, produciendo puntajes sin límites. Esto es requisito matemático de la distancia Wasserstein según Arjovsky et al. (2017). Además, siguiendo la recomendación del paper de WGAN-GP (Gulrajani et al., 2017), no se usa BatchNorm en el crítico cuando se aplica gradient penalty.


### Restricción de Lipschitz

Una función es 1-Lipschitz si no puede cambiar su salida más rápido que su entrada. Formalmente: |f(x₁) - f(x₂)| ≤ |x₁ - x₂| para todo par de puntos.

¿Por qué importa? La distancia Wasserstein solo tiene sentido matemático si el crítico es 1-Lipschitz. Sin esta restricción, el crítico podría dar valores arbitrariamente grandes, haciendo la métrica inútil.

¿Cómo se ejerce?
- WGAN: Recorta los pesos a [-0.01, 0.01] después de cada paso (weight clipping). Funciona pero es una solución burda que limita la capacidad del crítico.
- WGAN-GP: Añade un término de penalización que castiga cuando ||∇C|| ≠ 1. Es una solución más elegante que permite pesos naturales.

### Hiperparámetros

Todos los valores fueron tomados de los papers originales:

- Vanilla GAN: SGD con momentum (el paper no especifica valores exactos)
- WGAN: RMSprop, lr=5e-5, clip=0.01, n_critic=5
- WGAN-GP: Adam (β₁=0, β₂=0.9), lr=1e-4, λ=10, n_critic=5

### Métricas

- D(real), D(fake): Saturación del discriminador
- Distribución de pesos: Efecto del weight clipping
- Norma de gradientes: Estabilidad del entrenamiento
- Gradient penalty: Convergencia de la restricción Lipschitz
- Muestras generadas: Calidad visual final

### Duración del Entrenamiento

Se entrenaron 150 épocas por modelo, suficientes para observar convergencia o colapso. El tiempo total fue ~3.5 horas (Vanilla: ~23 min, WGAN: ~66 min, WGAN-GP: ~124 min).