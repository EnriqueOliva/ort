# La Evolución de las GANs: Una Historia en 7 Gráficos

Este documento explica paso a paso qué muestra cada gráfico del notebook y cómo cuenta la historia de la evolución desde Vanilla GAN hasta WGAN-GP.

---

## Gráfico 1: El Problema — Saturación del Discriminador

**Archivo:** `1_vanilla_saturation.png`

**Qué muestra:** Las salidas del discriminador de Vanilla GAN durante el entrenamiento:
- Línea verde: D(real) — probabilidad asignada a imágenes reales
- Línea roja: D(fake) — probabilidad asignada a imágenes falsas

**Qué está pasando:**

El discriminador aprende a distinguir imágenes reales de falsas. Al principio, ambas líneas están cerca de 0.5 (incertidumbre). Pero rápidamente:

- D(real) → 1.0 (el discriminador está 100% seguro de que las reales son reales)
- D(fake) → 0.0 (el discriminador está 100% seguro de que las falsas son falsas)

**El problema:**

Esto se llama **saturación**. Cuando el discriminador es "demasiado bueno", el gradiente de la función de pérdida BCE desaparece:

```
BCE Loss = -log(D(fake))
Cuando D(fake) → 0, el gradiente → 0
```

El generador no recibe señal de aprendizaje. No sabe cómo mejorar porque el discriminador simplemente dice "esto es falso" sin dar información útil sobre qué tan falso o cómo mejorarlo.

**Resultado:** El generador no puede aprender. Produce ruido o colapsa.

---

## Gráfico 2: La Solución — Distancia Wasserstein

**Archivo:** `2_wgan_wdistance.png`

**Qué muestra:** La distancia Wasserstein de WGAN durante el entrenamiento:
- W-distance = C(real) - C(fake)

**Qué está pasando:**

WGAN reemplaza el discriminador (que produce probabilidades 0-1) por un **crítico** (que produce puntuaciones sin límites). La distancia Wasserstein mide qué tan diferentes son las distribuciones real y generada.

**Por qué esto soluciona la saturación:**

1. **No hay sigmoid:** El crítico no tiene sigmoid al final, así que no puede saturar a 0 o 1
2. **Gradientes siempre útiles:** La W-distance proporciona gradientes significativos sin importar qué tan diferentes sean las distribuciones
3. **Métrica correlacionada:** A diferencia de BCE loss, la W-distance correlaciona con la calidad de las imágenes generadas

**Observación en el gráfico:**

La curva fluctúa pero NO colapsa a 0. Mantiene valores significativos durante todo el entrenamiento, indicando que el crítico siempre proporciona información útil al generador.

**Resultado:** WGAN soluciona el problema de saturación. Pero introduce un nuevo problema...

---

## Gráfico 3: El Nuevo Problema — Weight Clipping

**Archivo:** `3_weight_clipping.png`

**Qué muestra:** Histogramas de los pesos de las redes:
- Izquierda: Pesos del discriminador de Vanilla GAN
- Derecha: Pesos del crítico de WGAN

**Qué está pasando:**

Para que la distancia Wasserstein funcione matemáticamente, el crítico debe ser **1-Lipschitz continuo** (no puede cambiar su salida demasiado rápido respecto a cambios en la entrada).

WGAN original enforce esto mediante **weight clipping**: después de cada paso de optimización, todos los pesos se recortan al rango [-c, c] (típicamente c=0.01).

**El problema visible en el gráfico:**

- **Vanilla GAN (izquierda):** Distribución natural de pesos, típicamente una campana de Gauss centrada en 0
- **WGAN (derecha):** Los pesos están forzados a exactamente ±0.01. No hay pesos en el medio. Es una distribución bimodal extrema.

**Por qué esto es malo:**

1. **Capacidad reducida:** El crítico solo puede usar valores de peso en los extremos, limitando las funciones que puede representar
2. **Funciones simples:** El crítico tiende a aprender funciones muy simples (casi lineales)
3. **Incapaz de capturar complejidad:** No puede modelar características complejas de las imágenes

**Resultado:** WGAN produce imágenes mejores que Vanilla, pero aún borrosas y de baja calidad.

---

## Gráfico 4: La Consecuencia — Gradientes Explosivos

**Archivo:** `4_gradient_instability.png`

**Qué muestra:** Norma de los gradientes durante el entrenamiento:
- Izquierda: Gradientes del discriminador de Vanilla GAN
- Derecha: Gradientes del crítico de WGAN

**Qué está pasando:**

El weight clipping tiene una consecuencia severa en los gradientes.

**Vanilla GAN (izquierda):**
- Gradientes relativamente estables (aunque inútiles por la saturación)
- Varianza baja

**WGAN (derecha):**
- Gradientes extremadamente volátiles
- Picos que llegan a valores muy altos
- Varianza millones de veces mayor que Vanilla

**Por qué ocurre:**

Cuando los pesos están forzados a los límites ±c, el crítico se vuelve una función "puntiaguda". Pequeños cambios en la entrada causan grandes cambios en la salida. Esto se manifiesta como gradientes inestables que dificultan el entrenamiento.

**Analogía:** Es como intentar caminar por un terreno muy irregular con picos y valles pronunciados, en lugar de una superficie suave.

**Resultado:** El entrenamiento de WGAN es inestable. Se necesita otra forma de enforcar la restricción de Lipschitz.

---

## Gráfico 5: La Solución Final — Gradient Penalty (Pesos)

**Archivo:** `5_wgangp_weights.png`

**Qué muestra:** Comparación de distribución de pesos:
- Izquierda: WGAN (con weight clipping)
- Derecha: WGAN-GP (con gradient penalty)

**Qué está pasando:**

WGAN-GP reemplaza el weight clipping por un **gradient penalty**:

```
Loss = W-distance + λ * E[(||∇C(x̂)||₂ - 1)²]
```

En lugar de recortar los pesos, añadimos un término de penalización que castiga cuando la norma del gradiente del crítico se aleja de 1. Esto enforce la restricción de Lipschitz de forma "suave".

**El resultado visible:**

- **WGAN (izquierda):** Pesos en ±0.01, distribución bimodal
- **WGAN-GP (derecha):** Distribución natural tipo campana de Gauss, pesos pueden tomar cualquier valor

**Por qué esto es mejor:**

1. **Capacidad completa:** El crítico puede usar todo el rango de valores de peso
2. **Funciones complejas:** Puede aprender representaciones más ricas
3. **Sin restricciones artificiales:** Los pesos evolucionan naturalmente

---

## Gráfico 6: La Solución Final — Gradient Penalty (Gradientes + Mecanismo)

**Archivo:** `6_wgangp_gradients.png`

**Qué muestra:** Dos subgráficos:
- Izquierda: Comparación de normas de gradientes (WGAN vs WGAN-GP)
- Derecha: Evolución del término de Gradient Penalty

**Subgráfico izquierdo — Estabilidad de gradientes:**

- **WGAN (naranja):** Gradientes altos y volátiles (miles)
- **WGAN-GP (verde):** Gradientes bajos y estables (cerca de 0)

La diferencia es dramática. WGAN-GP tiene una varianza de gradientes órdenes de magnitud menor que WGAN.

**Subgráfico derecho — El mecanismo GP:**

El gradient penalty comienza alto (el crítico inicialmente no cumple la restricción de Lipschitz) y gradualmente decrece hacia 0.

- **GP → 0** significa que ||∇C|| ≈ 1, es decir, la restricción de Lipschitz se está cumpliendo
- El crítico aprende a ser 1-Lipschitz de forma natural, sin necesidad de clipping

**Resultado:** Entrenamiento estable con gradientes controlados.

---

## Gráfico 7: Evidencia Final — Muestras Generadas

**Archivo:** `7_final_samples.png`

**Qué muestra:** Imágenes generadas por cada modelo después del entrenamiento:
- Izquierda: Vanilla GAN
- Centro: WGAN
- Derecha: WGAN-GP

**Vanilla GAN:**
- Ruido, patrones repetitivos, colores saturados sin sentido
- Resultado del colapso por saturación del discriminador
- El generador nunca aprendió porque no recibió gradientes útiles

**WGAN:**
- Formas borrosas, colores apagados, poca variedad
- Mejor que Vanilla (sí aprendió algo)
- Limitado por el weight clipping que reduce la capacidad del crítico

**WGAN-GP:**
- Imágenes reconocibles con texturas, colores, formas coherentes
- Variedad entre las muestras
- El crítico con capacidad completa guía al generador efectivamente

---

## Resumen: La Historia Completa

```
┌─────────────────────────────────────────────────────────────────────┐
│  VANILLA GAN                                                         │
│  ───────────                                                         │
│  Problema: Discriminador satura (D→0 o D→1)                         │
│  Consecuencia: Gradientes desaparecen                               │
│  Resultado: Generador no aprende → imágenes basura                  │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│  WGAN                                                                │
│  ────                                                                │
│  Solución: Wasserstein distance (no satura)                         │
│  Nuevo problema: Weight clipping fuerza pesos a ±c                  │
│  Consecuencia: Gradientes explosivos, capacidad reducida            │
│  Resultado: Mejor que Vanilla, pero borroso                         │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│  WGAN-GP                                                             │
│  ───────                                                             │
│  Solución: Gradient penalty en vez de clipping                      │
│  Resultado: Pesos naturales, gradientes estables                    │
│  Resultado: Imágenes reconocibles y variadas                        │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Métricas Clave a Observar

| Métrica | Vanilla GAN | WGAN | WGAN-GP |
|---------|-------------|------|---------|
| D(real)/D(fake) | Saturan a 1/0 | N/A | N/A |
| Rango de pesos | Natural | ±c exacto | Natural |
| Varianza gradientes | Baja (pero inútil) | Muy alta | Baja |
| Calidad imágenes | Ruido | Borroso | Reconocible |

---

## Referencias

1. **Vanilla GAN:** Goodfellow et al., "Generative Adversarial Nets" (2014)
2. **WGAN:** Arjovsky et al., "Wasserstein GAN" (2017)
3. **WGAN-GP:** Gulrajani et al., "Improved Training of Wasserstein GANs" (2017)
