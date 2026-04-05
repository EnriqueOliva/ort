# Ejercicio 3 - Comparación de Redes Neuronales

## 1. Activación última capa (10 clases)

**Softmax** - Convierte 10 valores → 10 probabilidades que suman 1

**Por qué:** Clasificación multiclase necesita probabilidad por clase

---

## 2. Regla de decisión

```
Output = [p₀, p₁, ..., p₉]
Clase predicha = argmax(p)
```

**Ejemplo:** [0.05, 0.10, 0.60, 0.15, 0.03, 0.02, 0.01, 0.02, 0.01, 0.01]
→ Predice clase 2 (max = 0.60)

---

## 3. Función de loss

**Categorical Cross-Entropy (CCE)**

Multiclase + Softmax → CCE

---

## 4. Valores de D para que B < A en parámetros

**Red A:**
```
L_1: d→128: (d+1)×128 = 128d + 128
L_2: 128→64: 129×64 = 8,256
L_3: 64→10: 65×10 = 650

Total A = 128d + 128 + 8,256 + 650 = 128d + 9,034
```

**Red B:**
```
L_1: d→128: 128d + 128
L_2: 128→D: (128+1)×D = 129D
L_3: D→64: (D+1)×64 = 64D + 64
L_4: 64→10: 650

Total B = 128d + 129D + 64D + 128 + 64 + 650
        = 128d + 193D + 842
```

**Condición B < A:**
```
128d + 193D + 842 < 128d + 9,034
193D < 8,192
D < 42.44
```

**Respuesta: D ∈ {1, 2, ..., 42}**

**Ejemplos:**
- D=32: B tiene 128d+7,018 params (menos que A)
- D=42: B tiene 128d+8,948 params (casi igual)
- D=43: B tiene 128d+9,141 params (más que A)

**Fuente:** Clase 2-01-09-2025
