# ¿Por qué WGAN usa RMSprop y WGAN-GP usa Adam?

## El Problema Fundamental

**Weight clipping + Adam = Inestabilidad en el entrenamiento**

### ¿Por qué?

El weight clipping crea **discontinuidades abruptas** en el paisaje de pérdida:
- Los pesos se recortan bruscamente a [-c, c]
- Esto crea "saltos" en la superficie de optimización

**Adam** usa:
- Momentum (acumulación de gradientes pasados)
- Learning rates adaptativos

Estos mecanismos se **confunden** con las discontinuidades del clipping:
- El momentum empuja en direcciones basadas en gradientes pasados
- Pero el clipping cambia abruptamente la dirección
- Los learning rates adaptativos no pueden estabilizarse

### Desde el Paper de WGAN-GP

> "Momentum-based methods such as Adam perform poorly with weight clipping... we were unable to train WGAN with Adam."

## Por lo tanto:

- **WGAN usa RMSprop** → porque **TIENE que usarlo** (Adam falla)
- **WGAN-GP usa Adam** → porque **PUEDE usarlo** (sin discontinuidades por clipping)

## ¿Es Justa la Comparación?

### Perspectiva 1: Control Científico Estricto
**Ambos deberían usar RMSprop** para aislar SOLO la regularización:
- WGAN: RMSprop + clipping
- WGAN-GP: RMSprop + penalty

✅ Comparación pura de regularización
❌ No muestra el potencial completo de WGAN-GP

### Perspectiva 2: Comparación de Sistemas Completos (Paper)
**Cada uno usa su mejor optimizador compatible**:
- WGAN: RMSprop + clipping (Adam no funciona)
- WGAN-GP: Adam + penalty (puede usar Adam)

✅ Muestra rendimiento real
❌ Confunde regularización con optimizador

## Conclusión

**Ambas perspectivas son válidas** dependiendo de la pregunta de investigación:

- **Para aislar regularización**: Ambos RMSprop
- **Para comparar sistemas reales**: Cada uno su mejor optimizador

El paper sigue la segunda: **la incapacidad de usar Adam es parte del problema fundamental de WGAN**. WGAN-GP habilita optimizadores superiores.
