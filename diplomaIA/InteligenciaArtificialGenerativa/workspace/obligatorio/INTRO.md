## Introducción
---

Este notebook implementa y compara empíricamente tres arquitecturas de GANs: Vanilla GAN, WGAN y WGAN-GP, desarrollado como obligatorio de Inteligencia Artificial Generativa. Partiendo del paper original de Goodfellow et al. (2014), se demuestra el problema de saturación del discriminador que causa gradientes que desaparecen. WGAN (Arjovsky et al., 2017) soluciona esto reemplazando BCE loss por distancia Wasserstein con un crítico sin sigmoid, pero introduce weight clipping que fuerza los pesos a ±0.01 causando gradientes inestables. Finalmente, WGAN-GP (Gulrajani et al., 2017) reemplaza el clipping por un gradient penalty (λ=10) que enforce la restricción de Lipschitz de forma suave, permitiendo pesos naturales y entrenamiento estable. Los tres modelos se entrenan sobre CIFAR-10 con arquitecturas DCGAN compartidas, y la sección de evaluación demuestra progresivamente cada problema y su solución mediante visualizaciones de: saturación D(real)/D(fake), distancia Wasserstein, distribución de pesos, normas de gradientes, evolución del GP, y calidad de muestras generadas.

Papers:
- Vanilla GAN: https://arxiv.org/abs/1406.2661
- WGAN: https://arxiv.org/abs/1701.07875
- WGAN-GP: https://arxiv.org/abs/1704.00028
