# Función de Pérdida de los Modelos de Difusión

## La Idea en Una Oración

El modelo aprende a **predecir el ruido** que se agregó a una imagen. La pérdida es simplemente **qué tan bien predice ese ruido**.

---

## ¿Por Qué Es Tan Simple?

A diferencia de VAE (dos términos) o GAN (dos redes), la pérdida de difusión es increíblemente directa:

```
Loss = ||ε - ε_predicho||²
```

**En español:** La diferencia al cuadrado entre:
- **ε:** El ruido real que agregaste
- **ε_predicho:** El ruido que el modelo predijo

---

## El Contexto: Qué Hace el Modelo

### Proceso Forward (Agregar Ruido)

Tomas una imagen limpia y le agregas ruido poco a poco:

```
x₀ (imagen limpia) → x₁ → x₂ → ... → xₜ (casi ruido puro)
```

Este proceso **no se entrena**. Es pura matemática:

```
xₜ = √(ᾱₜ) × x₀ + √(1 - ᾱₜ) × ε
```

Donde:
- **ᾱₜ:** Un número que decrece con t (cuánto de la imagen original queda)
- **ε:** Ruido gaussiano Normal(0, 1)

### Proceso Reverse (Quitar Ruido)

El modelo aprende a **revertir** este proceso:

```
xₜ (ruidoso) → ... → x₁ → x₀ (imagen limpia)
```

Para hacer esto, el modelo necesita saber **cuánto ruido hay** en cada paso.

---

## La Función de Pérdida

### La Fórmula Simple

```
L = E[||ε - εθ(xₜ, t)||²]
```

Donde:
- **ε:** El ruido gaussiano real que agregaste
- **εθ(xₜ, t):** Lo que el modelo predice como ruido
- **xₜ:** La imagen con ruido
- **t:** El paso temporal (cuánto ruido hay)

### ¿Por Qué Predecir Ruido?

Hay dos opciones equivalentes matemáticamente:

**Opción 1: Predecir la imagen limpia**
```
Modelo recibe xₜ → predice x₀
```

**Opción 2: Predecir el ruido (MÁS USADA)**
```
Modelo recibe xₜ → predice ε
```

**¿Por qué la opción 2 es mejor?**
- El ruido siempre tiene la misma distribución: Normal(0, 1)
- Es más estable de entrenar
- El rango de valores es más predecible

---

## El Algoritmo de Entrenamiento

```
Repetir hasta converger:
    1. Tomar imagen real x₀ del dataset

    2. Elegir tiempo t aleatorio (entre 1 y T)

    3. Muestrear ruido ε ~ Normal(0, 1)

    4. Crear imagen ruidosa con forma cerrada:
       xₜ = √(ᾱₜ) × x₀ + √(1 - ᾱₜ) × ε

    5. Pasar (xₜ, t) al modelo → obtener ε_predicho

    6. Calcular pérdida: L = ||ε - ε_predicho||²

    7. Actualizar pesos con gradiente descendente
```

### ¿Por Qué Se Pasa t?

El modelo necesita saber **cuánto ruido hay** para predecir correctamente:

- Si t es alto (mucho ruido): debe predecir ruido fuerte
- Si t es bajo (poco ruido): debe predecir ruido débil

**Un solo modelo para todos los pasos**, condicionado por t.

---

## Variational Lower Bound (VLB)

### La Teoría Formal

La pérdida teórica completa es más complicada:

```
L_VLB = L₀ + L₁ + L₂ + ... + Lₜ
```

Cada término Lₜ es una divergencia KL entre distribuciones gaussianas.

### La Simplificación

El paper de DDPM (Ho et al., 2020) demostró que en la práctica:

```
L_simple = ||ε - εθ(xₜ, t)||²
```

**Funciona igual de bien** y es mucho más fácil de implementar.

---

## Código en PyTorch

```python
def diffusion_loss(model, x_0, t, noise_scheduler):
    """
    Calcula la pérdida de difusión.

    Args:
        model: Red neuronal (UNet típicamente)
        x_0: Imagen original limpia
        t: Paso temporal (tensor de enteros)
        noise_scheduler: Objeto que maneja los α y β

    Returns:
        Pérdida (MSE entre ruido real y predicho)
    """
    # 1. Muestrear ruido
    epsilon = torch.randn_like(x_0)

    # 2. Crear imagen ruidosa (forma cerrada)
    sqrt_alpha_bar = noise_scheduler.sqrt_alphas_cumprod[t]
    sqrt_one_minus_alpha_bar = noise_scheduler.sqrt_one_minus_alphas_cumprod[t]

    # Expandir dimensiones para broadcasting
    sqrt_alpha_bar = sqrt_alpha_bar.view(-1, 1, 1, 1)
    sqrt_one_minus_alpha_bar = sqrt_one_minus_alpha_bar.view(-1, 1, 1, 1)

    # x_t = √(ᾱ_t) * x_0 + √(1-ᾱ_t) * ε
    x_t = sqrt_alpha_bar * x_0 + sqrt_one_minus_alpha_bar * epsilon

    # 3. El modelo predice el ruido
    epsilon_pred = model(x_t, t)

    # 4. Pérdida: MSE entre ruido real y predicho
    loss = F.mse_loss(epsilon_pred, epsilon)

    return loss
```

### Loop de Entrenamiento

```python
for epoch in range(num_epochs):
    for batch in dataloader:
        x_0 = batch['image']  # Imagen limpia

        # Tiempo aleatorio para cada imagen del batch
        t = torch.randint(0, T, (batch_size,))

        # Calcular pérdida
        loss = diffusion_loss(model, x_0, t, scheduler)

        # Actualizar
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

---

## Comparación con Otras Pérdidas

| Modelo | Pérdida | Componentes |
|--------|---------|-------------|
| **VAE** | ELBO | Reconstrucción + KL |
| **GAN** | Minimax | Loss_D + Loss_G |
| **Difusión** | MSE de ruido | Solo ||ε - εθ||² |

### ¿Por Qué Difusión Es Más Estable?

1. **Un solo término:** No hay que balancear componentes
2. **Objetivo claro:** Predecir ruido gaussiano
3. **Sin adversarios:** No hay "juego" que pueda desbalancearse
4. **Distribución conocida:** El ruido siempre es Normal(0,1)

---

## Resumen Visual

```
┌────────────────────────────────────────────────────────────────┐
│                 PÉRDIDA DE DIFUSIÓN                            │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   Input: x₀ (imagen limpia) + t (tiempo) + ε (ruido real)      │
│                                                                │
│   1. Crear xₜ:  xₜ = √(ᾱₜ) × x₀ + √(1-ᾱₜ) × ε                 │
│                                                                │
│   2. Modelo predice: εθ(xₜ, t)                                 │
│                                                                │
│   3. Pérdida: L = ||ε - εθ(xₜ, t)||²                           │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   Ventajas:                                                    │
│   • Un solo término (simple)                                   │
│   • Muy estable de entrenar                                    │
│   • El ruido siempre es Normal(0,1)                            │
│                                                                │
│   Desventaja:                                                  │
│   • Generación lenta (T pasos)                                 │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## Para el Parcial

**Pérdida de Difusión:** MSE entre el ruido real (ε) y el ruido predicho (εθ); L = ||ε - εθ(xₜ, t)||².

**Por Qué Predecir Ruido:** Es más estable que predecir la imagen directamente porque el ruido siempre tiene distribución conocida Normal(0,1).

**Condicionamiento por t:** El modelo recibe el paso temporal t como entrada para saber cuánto ruido hay en la imagen actual.

**Forma Cerrada:** Permite calcular xₜ directamente desde x₀ sin pasar por pasos intermedios: xₜ = √(ᾱₜ) × x₀ + √(1-ᾱₜ) × ε.

**VLB vs Simple Loss:** La pérdida teórica (VLB) es compleja, pero en práctica el MSE simple funciona igual de bien.
