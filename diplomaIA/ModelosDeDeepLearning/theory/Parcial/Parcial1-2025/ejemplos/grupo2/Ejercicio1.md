# Ejercicio 1 - Red Neuronal para Predicción de Retrasos de Vuelos

## 1. Dimensión m (triplica entrada)

Entrada = 5 features → Triplica = 5 × 3 = **15**

**Respuesta: m = 15**

---

## 2. Dimensión n (clasificación binaria)

Predecir probabilidad (0 a 1) → Clasificación binaria → 1 neurona

**Respuesta: n = 1**

---

## 3. Parámetros totales

**Fórmula:** Parámetros = Input × Output + Biases

**L_1 (5→15):** 5×15 + 15 = 75 + 15 = **90**
**L_2 (15→1):** 15×1 + 1 = 15 + 1 = **16**

**Total: 106 parámetros**

---

## 4. Activación A_1 (anular negativos, mantener positivos)

**ReLU(z) = max(0, z)**

Ejemplos: ReLU(-2) = 0, ReLU(3) = 3

**Respuesta: A_1 = ReLU**

---

## 5. Activación A_2 (para probabilidad)

**Sigmoid(z) = 1/(1+e^(-z))** → Output ∈ [0,1]

Ejemplos: Sigmoid(0) = 0.5, Sigmoid(2) = 0.88

**Respuesta: A_2 = Sigmoid**

---

## 6. Función de pérdida

**Binary Cross-Entropy:** BCE = -[y·log(ŷ) + (1-y)·log(1-ŷ)]

**Respuesta: BCE**

---

## 7. Análisis de gráfica

**Patrón:**
- Épocas 0-25: Train y validation bajan juntas ✓
- Épocas 25-100: Train baja, validation SUBE ✗

**Problema: OVERFITTING** (train=0.01, validation=0.18)

**Solución: Early Stopping**
- Paciencia = 5 épocas
- Parar en época ~30
- Devolver modelo de época 25 (validation=0.05)

**Fuente:** Clases 2, 5, 6, 7 (2025)
