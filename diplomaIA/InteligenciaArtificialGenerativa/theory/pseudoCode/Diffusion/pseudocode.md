# Pseudocódigo Modelos de Difusión

## Idea Central
Agregar ruido paso a paso. Aprender a quitarlo.

---

## 1. FORWARD PROCESS (Agregar Ruido)

**No se entrena. Es pura matemática.**

```
# Forma cerrada: ir directo de x₀ a xₜ
FUNCION agregar_ruido(x_0, t):

    epsilon = muestrear_normal(0, 1)  # Ruido

    # Calcular imagen ruidosa
    x_t = sqrt(alpha_bar[t]) * x_0 + sqrt(1 - alpha_bar[t]) * epsilon

    RETORNAR x_t, epsilon
```

**Donde:**
- `alpha_bar[t]` decrece con t (más ruido conforme avanza)
- `t = 0`: imagen limpia
- `t = T`: ruido puro

---

## 2. ENTRENAMIENTO

```
PARA cada imagen x_0 del dataset:

    # 1. Elegir tiempo aleatorio
    t = random(1, T)

    # 2. Agregar ruido (forma cerrada)
    epsilon = muestrear_normal(0, 1)
    x_t = sqrt(alpha_bar[t]) * x_0 + sqrt(1 - alpha_bar[t]) * epsilon

    # 3. Predecir el ruido
    epsilon_pred = modelo(x_t, t)

    # 4. Calcular pérdida (MSE entre ruido real y predicho)
    loss = MSE(epsilon, epsilon_pred)

    # 5. Actualizar pesos
    backprop(loss)
    actualizar_pesos()
```

---

## 3. GENERACIÓN (Reverse Process)

```
FUNCION generar_imagen():

    # Partir de ruido puro
    x_T = muestrear_normal(0, 1)

    # Quitar ruido paso a paso
    PARA t = T hasta 1:

        # Predecir el ruido en este paso
        epsilon_pred = modelo(x_t, t)

        # Quitar un poco de ruido
        x_{t-1} = quitar_ruido(x_t, epsilon_pred, t)

    RETORNAR x_0  # Imagen limpia
```

### Fórmula de quitar ruido (simplificada):
```
x_{t-1} = (1/sqrt(alpha[t])) * (x_t - beta[t]/sqrt(1-alpha_bar[t]) * epsilon_pred) + sigma[t] * z

Donde z = muestrear_normal(0, 1) si t > 1, sino z = 0
```

---

## 4. ¿POR QUÉ PREDECIR RUIDO?

```
# Dos opciones equivalentes:
# Opción A: Predecir imagen limpia x_0
# Opción B: Predecir ruido epsilon  ← MÁS USADA

# ¿Por qué B es mejor?
# - El ruido siempre es Normal(0, 1)
# - Distribución conocida = más estable
# - Rango de valores predecible
```

---

## 5. PUNTOS CLAVE

### Espacio Latente = Mismo Tamaño
```
# A diferencia de VAE y GAN:
# En difusión, el latente tiene el MISMO tamaño que la imagen

Imagen: 64x64
Latente (ruido): 64x64  # Mismo tamaño!
```

### El Modelo Necesita el Tiempo t
```
# El modelo recibe t como entrada
epsilon_pred = modelo(x_t, t)

# ¿Por qué?
# Porque necesita saber cuánto ruido hay
# t alto → mucho ruido
# t bajo → poco ruido
```

### Schedule de β
```
# β define cuánto ruido agregar en cada paso
# Típicamente: β crece linealmente de 0.0001 a 0.02
# T = 1000 pasos
```

---

## Resumen Ultra-Corto

```
ENTRENAR:
    t = random
    epsilon = ruido
    x_t = sqrt(ᾱ_t) * x_0 + sqrt(1-ᾱ_t) * epsilon
    loss = MSE(epsilon, modelo(x_t, t))

GENERAR:
    x = ruido_puro
    PARA t = T hasta 1:
        x = quitar_ruido(x, modelo(x, t), t)
    RETORNAR x
```
