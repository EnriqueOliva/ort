# Pseudocódigo VAE (Variational Autoencoder)

## Idea Central
Comprimir datos a un espacio latente y reconstruirlos.

---

## 1. ENTRENAMIENTO

```
PARA cada imagen X del dataset:

    # ENCODER: comprimir
    mu, sigma = Encoder(X)

    # REPARAMETRIZATION TRICK
    epsilon = muestrear_normal(0, 1)
    Z = mu + sigma * epsilon

    # DECODER: reconstruir
    X_reconstruida = Decoder(Z)

    # PÉRDIDA
    Loss_recon = MSE(X, X_reconstruida)
    Loss_KL = -0.5 * suma(1 + log(sigma²) - mu² - sigma²)
    Loss_total = Loss_recon + Loss_KL

    # ACTUALIZAR
    backprop(Loss_total)
    actualizar_pesos()
```

---

## 2. GENERACIÓN

```
# Muestrear del espacio latente
Z = muestrear_normal(0, 1)

# Decodificar
X_nueva = Decoder(Z)

RETORNAR X_nueva
```

---

## 3. REPARAMETRIZATION TRICK (detalle)

**Problema:** No podemos hacer backprop a través de un muestreo.

**Solución:**
```
# EN VEZ DE:
Z = muestrear_normal(mu, sigma)    # NO diferenciable

# HACEMOS:
epsilon = muestrear_normal(0, 1)   # Fijo, no depende de parámetros
Z = mu + sigma * epsilon           # Diferenciable respecto a mu y sigma
```

---

## Resumen Ultra-Corto

```
ENTRENAR:
    Z = Encoder(X) → mu, sigma
    Z = mu + sigma * ruido
    X' = Decoder(Z)
    Loss = Reconstrucción + KL

GENERAR:
    Z = ruido ~ Normal(0,1)
    X_nueva = Decoder(Z)
```
