# Pseudocódigo GAN (Generative Adversarial Network)

## Idea Central
Dos redes compiten: G crea falsas, D detecta falsas.

---

## 1. ENTRENAMIENTO (Alternado)

```
PARA cada epoch:
    PARA cada batch de imágenes reales:

        # ========================================
        # PASO 1: ENTRENAR DISCRIMINADOR
        # ========================================

        # Imágenes reales
        pred_real = D(imagenes_reales)
        loss_D_real = BCE(pred_real, etiqueta=1)

        # Imágenes falsas
        z = muestrear_normal(0, 1)
        imagenes_falsas = G(z)
        pred_fake = D(imagenes_falsas.detach())  # IMPORTANTE: .detach()
        loss_D_fake = BCE(pred_fake, etiqueta=0)

        # Actualizar D
        loss_D = loss_D_real + loss_D_fake
        backprop(loss_D)
        actualizar_pesos_D()

        # ========================================
        # PASO 2: ENTRENAR GENERADOR
        # ========================================

        z = muestrear_normal(0, 1)
        imagenes_falsas = G(z)
        pred_fake = D(imagenes_falsas)

        # TRUCO: etiqueta=1 aunque son falsas
        loss_G = BCE(pred_fake, etiqueta=1)

        backprop(loss_G)
        actualizar_pesos_G()
```

---

## 2. GENERACIÓN

```
# Muestrear ruido
z = muestrear_normal(0, 1)

# Generar imagen
imagen_nueva = G(z)

RETORNAR imagen_nueva
```

---

## 3. PUNTOS CLAVE

### El .detach()
```
# Al entrenar D con imágenes falsas:
D(imagenes_falsas.detach())

# .detach() corta el gradiente
# Así NO actualizamos G cuando entrenamos D
```

### El Truco del Flipeo
```
# Al entrenar G:
loss_G = BCE(D(fake), etiqueta=1)  # Decimos que son "reales"

# Aunque sabemos que son falsas,
# ponemos etiqueta=1 para que G aprenda a engañar a D
```

### Balance D vs G
```
# Si D es muy bueno: G no aprende (gradientes muy pequeños)
# Si G es muy bueno: D no aprende

# Solución típica:
learning_rate_D < learning_rate_G
# D aprende más lento para mantener equilibrio
```

---

## Resumen Ultra-Corto

```
ENTRENAR D:
    loss = BCE(D(real), 1) + BCE(D(G(z).detach()), 0)

ENTRENAR G:
    loss = BCE(D(G(z)), 1)    # Flipeo: etiqueta 1 para falsas

GENERAR:
    imagen = G(ruido)
```
