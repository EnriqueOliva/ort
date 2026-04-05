# Ejercicio 2 - Red MLP

## 1. Dimensión D de L_2

**De L_2 con 84 params:**
```
L_2: (None, D) con 84 params
Parámetros = Input × Output + Output
84 = 6 × D + D = 7D
D = 84 / 7 = 12
```
**Respuesta: D = 12**

---

## 2. Dimensión de entrada

L_1 output = (None, 6) → **Entrada = 6 features**

---

## 3. Salida de A_1

```
[[0.0, 0.0, 7.5, 0.2, 0.0, 0.0],
 [6.0, 4.6, 0.7, 0.0, 0.3, 0.0],
 [3.8, 0.0, 9.2, 1.0, 0.0, 0.0],
 [5.7, 4.9, 0.0, 0.5, 0.0, 0.1]]
```

**a) Activación:** Todos valores ≥ 0, negativos anulados → **ReLU**

**b) Batch size:** 4 ejemplos (4 filas) → **Batch = 4**

---

## 4. Salida de A_3

```
[[0.25, 0.25, 0.50],
 [0.40, 0.35, 0.25],
 [0.05, 0.65, 0.30],
 [0.85, 0.02, 0.13]]
```

**a) Activación:** Cada fila suma 1.0, todos ≥ 0 → **Softmax**

**b) Tipo de problema:** 3 clases → **Clasificación multiclase**

**c) Función loss:** Multiclase con softmax → **Categorical Cross-Entropy**

---

## 5. Aciertos en el batch

```
Targets: [[0,0,1], [0,1,0], [0,1,0], [1,0,0]]
Outputs: [[0.25,0.25,0.50], [0.40,0.35,0.25], [0.05,0.65,0.30], [0.85,0.02,0.13]]

Ejemplo 1: max=0.50 (pos 2) vs target clase 2 ✓ Acierto
Ejemplo 2: max=0.40 (pos 0) vs target clase 1 ✗ Error
Ejemplo 3: max=0.65 (pos 1) vs target clase 1 ✓ Acierto
Ejemplo 4: max=0.85 (pos 0) vs target clase 0 ✓ Acierto
```

**Respuesta: 3 aciertos de 4 (75% accuracy)**

---

## 6. Early Stopping

**Gráfica:** Train y validation loss, 8 épocas totales

**Patrón:**
- Época 1-2: Validation baja (mínimo en época 2)
- Época 3-8: Validation sube o se mantiene

**Contando desde época 2:**
Época 2→3→4→5→6→7→8 = 6 épocas sin mejorar

**a) Paciencia = 6**
**b) Mejor modelo = Época 2**

**Fuente:** Clase 7-13-10-2025
