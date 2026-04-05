# Ejercicio 4 - RNN (Recurrent Neural Network)

## 1. ¿Qué arquitectura representa?

**RNN (Recurrent Neural Network) - Red Neuronal Recurrente**

**Características visibles:**
- Estados ocultos h^(t) conectados temporalmente (h^(t-1) → h^(t) → h^(t+1))
- Mismos pesos W compartidos en todos los pasos
- Procesamiento secuencial (unfold en el tiempo)

---

## 2. ¿Qué tipos de problemas soluciona?

**Datos secuenciales:**

1. **Predicción de texto:** Siguiente palabra dado contexto
2. **Series temporales:** Predicción de stock, temperatura
3. **Traducción:** Secuencia en idioma A → idioma B
4. **Clasificación de secuencias:** Análisis de sentimiento en frases
5. **Generación:** Crear texto, música

**Clave:** Cuando el **orden** importa

---

## 3. ¿Qué fenómeno dificulta entrenar?

**Vanishing Gradients (Gradientes que desaparecen)**

**Por qué ocurre:**
```
Backpropagation Through Time (BPTT):
Gradiente en t=0 depende de multiplicar muchas derivadas

∂L/∂W = ∂L/∂h^(T) × ∂h^(T)/∂h^(T-1) × ... × ∂h^(1)/∂h^(0) × ∂h^(0)/∂W

Con tanh: |derivada| < 1
Producto de muchos <1 → tiende a 0
```

**Resultado:** Pesos lejanos en el tiempo NO se actualizan

**Solución:** LSTM, GRU (variantes con gates)

---

## 4. Parámetros de la arquitectura

**Dimensiones:**
- x: 10
- h: 5
- y: 2

**Matrices:**

**U (input → hidden):**
```
x^(t) de dimensión 10 → h^(t) de dimensión 5
U: (10, 5) → 10×5 = 50 parámetros
```

**W (hidden → hidden):**
```
h^(t-1) de dimensión 5 → h^(t) de dimensión 5
W: (5, 5) → 5×5 = 25 parámetros
```

**V (hidden → output):**
```
h^(t) de dimensión 5 → o^(t) de dimensión 2
V: (5, 2) → 5×2 = 10 parámetros
```

**Biases:**
```
b (para h): dimensión 5 → 5 parámetros
c (para o): dimensión 2 → 2 parámetros
```

**Total:**
```
U: 50
W: 25
V: 10
b: 5
c: 2

Total = 50 + 25 + 10 + 5 + 2 = 92 parámetros
```

**Clave:** Pesos compartidos en todos los pasos temporales (no se multiplica por T)

**Fuente:** Clases sobre arquitecturas recurrentes
