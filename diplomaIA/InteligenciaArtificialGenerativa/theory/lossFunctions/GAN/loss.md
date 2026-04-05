# Función de Pérdida de las GANs

## La Idea en Una Oración

Las GANs son un **juego** entre dos redes: el Generador (G) intenta crear datos falsos convincentes, y el Discriminador (D) intenta detectar cuáles son falsos. Cada uno tiene su propia pérdida.

---

## ¿Por Qué Es Diferente?

En otros modelos (VAE, Diffusion), entrenas **una cosa** para hacer **una tarea**.

En GANs, entrenas **dos cosas** que **compiten** entre sí:
- **Generador (G):** Quiere engañar a D
- **Discriminador (D):** Quiere no ser engañado

Es como entrenar a un falsificador de billetes y a un detector de billetes falsos **al mismo tiempo**.

---

## La Función Objetivo: V(D,G)

La función que define el juego es:

```
V(D,G) = E[log D(x)] + E[log(1 - D(G(z)))]
```

Donde:
- **D(x):** Probabilidad que D asigna a que x sea real (entre 0 y 1)
- **G(z):** Imagen generada a partir de ruido z
- **D(G(z)):** Probabilidad que D asigna a que la imagen generada sea real

---

## El Juego Minimax

```
min_G max_D V(D,G)
```

**En español:**
1. El Discriminador quiere **maximizar** V (ser mejor detectando)
2. El Generador quiere **minimizar** V (ser mejor engañando)
3. El óptimo es cuando G engaña tan bien que D no sabe qué es real → D(x) = 0.5

---

## Pérdida del Discriminador

### ¿Qué quiere D?

D quiere ser un **buen clasificador**:
- Para datos **reales**: D(x) → 1 (decir "esto es real")
- Para datos **falsos**: D(G(z)) → 0 (decir "esto es falso")

### La Fórmula

```
Loss_D = -[E[log D(x)] + E[log(1 - D(G(z)))]]
```

O con BCE (Binary Cross-Entropy):

```
Loss_D = BCE(D(x_real), 1) + BCE(D(x_fake), 0)
```

### Desglose

**Primera parte: E[log D(x)]**
- D recibe datos **reales**
- Queremos que D(x) → 1
- Si D(x) = 1: log(1) = 0 (pérdida mínima)
- Si D(x) = 0: log(0) = -∞ (pérdida máxima)

**Segunda parte: E[log(1 - D(G(z)))]**
- D recibe datos **generados**
- Queremos que D(G(z)) → 0
- Si D(G(z)) = 0: log(1-0) = 0 (pérdida mínima)
- Si D(G(z)) = 1: log(1-1) = -∞ (pérdida máxima)

### En Código (PyTorch)

```python
# Pérdida del discriminador
real_labels = torch.ones(batch_size, 1)   # Etiqueta 1 para reales
fake_labels = torch.zeros(batch_size, 1)  # Etiqueta 0 para falsos

# Imágenes reales
output_real = D(real_images)
loss_real = F.binary_cross_entropy(output_real, real_labels)

# Imágenes falsas (G(z))
z = torch.randn(batch_size, latent_dim)
fake_images = G(z)
output_fake = D(fake_images.detach())  # .detach() = no actualizar G aquí
loss_fake = F.binary_cross_entropy(output_fake, fake_labels)

# Total
loss_D = loss_real + loss_fake
```

---

## Pérdida del Generador

### ¿Qué quiere G?

G quiere **engañar** a D:
- Para datos generados: D(G(z)) → 1 (que D crea que son reales)

### La Fórmula Original

```
Loss_G = E[log(1 - D(G(z)))]
```

Queremos **minimizar** esto, lo cual empuja D(G(z)) hacia 1.

### El Problema: Gradientes Saturados

Al inicio del entrenamiento:
- G es malo → genera basura
- D(G(z)) ≈ 0 → D detecta fácilmente
- log(1 - 0) = log(1) = 0
- **Gradiente casi cero** → G no aprende

### La Solución: Truco del Log

En lugar de minimizar log(1 - D(G(z))), **maximizamos** log(D(G(z))):

```
Loss_G = -E[log D(G(z))]
```

O equivalente:

```
Loss_G = BCE(D(G(z)), 1)  # ¡Usamos etiqueta 1!
```

**¿Por qué funciona?**
- Cuando D(G(z)) ≈ 0 (G es malo)
- log(0.01) = -4.6 (gradiente GRANDE)
- G aprende más rápido cuando más lo necesita

### El "Truco del Flipeo"

Aunque sabemos que las imágenes son **falsas**, usamos etiqueta **1** (real):

```python
# Pérdida del generador
z = torch.randn(batch_size, latent_dim)
fake_images = G(z)
output = D(fake_images)

# ¡Etiqueta 1! (queremos que D crea que son reales)
loss_G = F.binary_cross_entropy(output, torch.ones(batch_size, 1))
```

---

## El Entrenamiento Alternado

**No se entrenan G y D juntos.** Se alternan:

### Paso 1: Entrenar D (k veces)

```
1. Generar imágenes falsas: x_fake = G(z)
2. Obtener imágenes reales: x_real ~ dataset
3. loss_D = BCE(D(x_real), 1) + BCE(D(x_fake.detach()), 0)
4. Actualizar solo los pesos de D
```

### Paso 2: Entrenar G (1 vez)

```
1. Generar imágenes falsas: x_fake = G(z)
2. loss_G = BCE(D(x_fake), 1)  # Truco del flipeo
3. Actualizar solo los pesos de G
```

### ¿Por Qué Alternado?

- Si entrenas ambos juntos, es caótico
- D necesita estar "fijo" para que G aprenda a engañarlo
- G necesita estar "fijo" para que D aprenda a detectarlo

### El .detach() en PyTorch

Cuando entrenas D, usas `fake_images.detach()`:
- Esto **desconecta** el tensor del grafo computacional
- Los gradientes NO se propagan hacia G
- Solo se actualizan los pesos de D

---

## El Balance: Learning Rates Diferentes

Típicamente:

```python
lr_G = 0.0002   # Para el generador
lr_D = 0.00005  # Para el discriminador (¡4x menor!)
```

**¿Por qué?**
- D aprende más rápido (tarea más fácil: clasificar)
- Si D es demasiado bueno, G no aprende
- Hay que mantener el balance

---

## Resumen Visual

```
┌────────────────────────────────────────────────────────────────┐
│                    PÉRDIDAS DE LA GAN                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   DISCRIMINADOR (D)                  GENERADOR (G)             │
│   ─────────────────                  ─────────────             │
│                                                                │
│   Loss_D = BCE(D(real), 1)           Loss_G = BCE(D(fake), 1)  │
│          + BCE(D(fake), 0)                                     │
│                                                                │
│   Quiere:                            Quiere:                   │
│   • D(real) → 1                      • D(fake) → 1             │
│   • D(fake) → 0                        (engañar a D)           │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   IMPORTANTE:                                                  │
│   • Se entrenan alternadamente (no juntos)                     │
│   • Usar .detach() al entrenar D                               │
│   • Learning rate de D < Learning rate de G                    │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## Código Completo

```python
# Hiperparámetros
lr_G = 0.0002
lr_D = 0.00005
latent_dim = 100

# Optimizadores (uno para cada red)
optimizer_G = torch.optim.Adam(G.parameters(), lr=lr_G)
optimizer_D = torch.optim.Adam(D.parameters(), lr=lr_D)

# Pérdida
criterion = nn.BCELoss()

for iteration in range(num_iterations):
    # === ENTRENAR DISCRIMINADOR ===
    real_images, _ = next(iter(dataloader))
    batch_size = real_images.size(0)

    # Etiquetas
    real_labels = torch.ones(batch_size, 1)
    fake_labels = torch.zeros(batch_size, 1)

    # Generar imágenes falsas
    z = torch.randn(batch_size, latent_dim)
    fake_images = G(z)

    # Pérdida de D
    optimizer_D.zero_grad()
    loss_D_real = criterion(D(real_images), real_labels)
    loss_D_fake = criterion(D(fake_images.detach()), fake_labels)
    loss_D = loss_D_real + loss_D_fake
    loss_D.backward()
    optimizer_D.step()

    # === ENTRENAR GENERADOR ===
    z = torch.randn(batch_size, latent_dim)
    fake_images = G(z)

    # Pérdida de G (¡etiqueta 1!)
    optimizer_G.zero_grad()
    loss_G = criterion(D(fake_images), real_labels)  # Truco del flipeo
    loss_G.backward()
    optimizer_G.step()
```

---

## Para el Parcial

**V(D,G):** Función objetivo de las GANs = E[log D(x)] + E[log(1-D(G(z)))]; D quiere maximizarla, G quiere minimizarla.

**Loss del Discriminador:** BCE(D(real), 1) + BCE(D(fake), 0); quiere clasificar correctamente reales y falsos.

**Loss del Generador:** BCE(D(fake), 1); quiere que D clasifique sus imágenes como reales.

**Truco del Log:** En lugar de minimizar log(1-D(G(z))), maximizar log(D(G(z))); evita gradientes saturados al inicio.

**Entrenamiento Alternado:** Primero D (con G congelado), luego G (con D congelado); usar .detach() para implementar.

**Balance de Learning Rates:** lr_D < lr_G para evitar que D sea demasiado bueno y G no aprenda.
