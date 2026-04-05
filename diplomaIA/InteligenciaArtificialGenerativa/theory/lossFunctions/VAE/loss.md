# Función de Pérdida del VAE (ELBO)

## La Idea en Una Oración

La pérdida del VAE tiene **dos partes** que trabajan juntas: una que dice "reconstruye bien la imagen" y otra que dice "mantén el espacio latente organizado".

---

## ¿Por Qué Dos Partes?

Imagina que entrenas a alguien para hacer resúmenes de libros:

1. **Parte 1 (Reconstrucción):** "Tu resumen debe permitir recrear el libro original"
2. **Parte 2 (Regularización):** "Tus resúmenes deben seguir un formato estándar"

Sin la Parte 1: El resumen no serviría para nada.
Sin la Parte 2: Cada resumen tendría un formato diferente y no podrías comparar ni generar nuevos.

---

## La Fórmula Completa

```
Loss = Reconstruction Loss + KL Divergence
```

O más formalmente:

```
L(θ, φ) = -E[log p(x|z)] + D_KL(q(z|x) || p(z))
```

Donde:
- **θ** = parámetros del decoder
- **φ** = parámetros del encoder
- **x** = imagen original
- **z** = vector latente (comprimido)

---

## Parte 1: Reconstruction Loss (Pérdida de Reconstrucción)

### ¿Qué mide?

**Qué tan parecida es la imagen reconstruida a la original.**

### Analogía

Es como fotocopiar un documento y comparar la copia con el original. Cuanto más diferente, peor.

### Fórmulas Comunes

**Opción A: MSE (Mean Squared Error)**
```
L_recon = ||x - x̂||² = Σ(x_i - x̂_i)²
```

Suma de las diferencias al cuadrado entre cada píxel original y reconstruido.

**Opción B: BCE (Binary Cross-Entropy)**
```
L_recon = -Σ[x_i × log(x̂_i) + (1-x_i) × log(1-x̂_i)]
```

Se usa cuando los píxeles están entre 0 y 1.

### ¿Cuál usar?

- **MSE:** Para imágenes con valores continuos
- **BCE:** Para imágenes en blanco y negro (binarias)

### En Código (PyTorch)

```python
# MSE
recon_loss = F.mse_loss(x_recon, x, reduction='sum')

# BCE
recon_loss = F.binary_cross_entropy(x_recon, x, reduction='sum')
```

---

## Parte 2: KL Divergence (Divergencia KL)

### ¿Qué mide?

**Qué tan diferente es la distribución que produce el encoder (q) de una distribución "ideal" (p).**

### Analogía

Imagina que todos los estudiantes deben escribir ensayos con un formato específico (márgenes de 2.5cm, letra Arial 12, etc.). La KL Divergence mide qué tanto se desvían del formato.

- Si todos siguen el formato exactamente: KL = 0
- Si cada uno usa un formato diferente: KL alto

### ¿Por qué queremos esto?

Queremos que el espacio latente Z sea una distribución "bonita" y organizada: **Normal(0, 1)**.

Esto nos permite:
1. **Generar nuevas imágenes:** Simplemente muestreamos de Normal(0,1)
2. **Interpolar:** Movernos suavemente entre dos puntos del espacio latente
3. **Organización:** Imágenes similares quedan cerca en el espacio Z

### La Fórmula

Para comparar dos distribuciones Gaussianas, hay una fórmula cerrada:

```
D_KL = ½ × Σ(μ² + σ² - log(σ²) - 1)
```

Donde:
- **μ (mu):** La media que produce el encoder
- **σ² (sigma²):** La varianza que produce el encoder

### ¿Qué empuja esta pérdida?

- **μ → 0:** Las medias deben acercarse a cero
- **σ → 1:** Las varianzas deben acercarse a uno

### En Código (PyTorch)

```python
# El encoder produce mu y log_var (log de la varianza)
# log_var es más estable numéricamente que σ directamente

kl_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
```

**¿Por qué log_var y no σ?**
- σ debe ser positivo (>0)
- log(σ²) puede ser cualquier número real
- Es más estable para entrenar

---

## El Balance: ¿Cuánto de Cada Uno?

La pérdida total es la suma de ambas:

```
Loss_total = Loss_recon + Loss_KL
```

### El Problema del Balance

- **Mucho peso en reconstrucción:** Imágenes perfectas, pero espacio latente caótico
- **Mucho peso en KL:** Espacio latente perfecto, pero imágenes borrosas/malas

### La Solución: β-VAE

Una variante popular agrega un factor β:

```
Loss_total = Loss_recon + β × Loss_KL
```

- **β = 1:** VAE estándar
- **β > 1:** Más organización en Z (mejor para "disentanglement")
- **β < 1:** Mejor reconstrucción, menos organización

---

## Código Completo

```python
def vae_loss(x, x_recon, mu, log_var):
    """
    Calcula la pérdida del VAE.

    Args:
        x: Imagen original
        x_recon: Imagen reconstruida
        mu: Media del encoder
        log_var: Log-varianza del encoder

    Returns:
        Pérdida total
    """
    # Pérdida de reconstrucción (BCE)
    recon_loss = F.binary_cross_entropy(x_recon, x, reduction='sum')

    # KL Divergence
    # -0.5 * sum(1 + log(σ²) - μ² - σ²)
    kl_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())

    # Total
    return recon_loss + kl_loss
```

---

## Resumen Visual

```
┌─────────────────────────────────────────────────────────────┐
│                    PÉRDIDA DEL VAE                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Loss = Reconstrucción + KL Divergence                     │
│          ↓                  ↓                               │
│   "Que la copia se         "Que el espacio latente         │
│    parezca al original"     sea Normal(0,1)"               │
│                                                             │
│   • MSE: ||x - x̂||²         • ½Σ(μ² + σ² - log(σ²) - 1)   │
│   • BCE: -Σ[x log(x̂)]                                       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Si solo reconstrucción → Memoriza, no generaliza          │
│   Si solo KL → Genera ruido aleatorio                       │
│   AMBAS juntas → Genera imágenes nuevas y coherentes        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Para el Parcial

**ELBO (Evidence Lower Bound):** La función de pérdida del VAE, que es la suma de la pérdida de reconstrucción (qué tan bien se reconstruye x desde z) más la divergencia KL (qué tan cercana es la distribución q(z|x) a la prior p(z)=Normal(0,1)).

**Reconstruction Loss:** Mide la diferencia entre la imagen original y la reconstruida; puede ser MSE o BCE.

**KL Divergence en VAE:** Regularizador que empuja μ hacia 0 y σ hacia 1, asegurando un espacio latente organizado que permite generación.

**β-VAE:** Variante donde se multiplica la KL por un factor β; β>1 da mejor organización del espacio latente.
