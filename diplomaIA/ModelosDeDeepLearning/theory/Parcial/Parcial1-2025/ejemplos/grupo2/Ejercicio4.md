# Ejercicio 4 - Cálculos Manuales en Red Neuronal

## 1a. Calcular z₁, z₂ para input (5,5)

**Sin bias:**
```
z₁ = W₁₁⁽¹⁾·x₁ + W₂₁⁽¹⁾·x₂
   = 2·5 + (-1)·5
   = 10 - 5 = 5

z₂ = W₁₂⁽¹⁾·x₁ + W₂₂⁽¹⁾·x₂
   = (-3)·5 + (-1)·5
   = -15 - 5 = -20
```

**Después de ReLU:**
```
a₁ = ReLU(5) = 5    ✓ Activa
a₂ = ReLU(-20) = 0  ✗ No activa
```

**Neuronas activas: Solo neurona 1**

---

## 1b. Agregar bias b⁽¹⁾ = (b₁⁽¹⁾, b₂⁽¹⁾) para activaciones positivas

Queremos a₁ > 0 y a₂ > 0

```
a₁ = ReLU(5 + b₁⁽¹⁾) > 0  ← Ya es 5, cualquier b₁ ≥ -5 funciona
a₂ = ReLU(-20 + b₂⁽¹⁾) > 0  ← Necesita b₂⁽¹⁾ > 20
```

**Respuesta: b₁⁽¹⁾ = 0, b₂⁽¹⁾ = 21** (cualquier b₂ > 20 funciona)

**Verificación:**
```
z₁ = 5 + 0 = 5 → a₁ = 5 ✓
z₂ = -20 + 21 = 1 → a₂ = 1 ✓
```

---

## 2a. Cambio en ŷ al variar W₂₁⁽²⁾

**Forward pass actual:**
```
a₁ = 5, a₂ = 0 (sin bias del 1b)
ŷ = W₁₁⁽²⁾·a₁ + W₂₁⁽²⁾·a₂
  = 0.5·5 + (-1.5)·0
  = 2.5
```

**Si aumenta W₂₁⁽²⁾:** ŷ NO cambia (porque a₂ = 0)

**Respuesta:** ŷ NO cambia mientras a₂ = 0

---

## 2b. Signo de actualización de W₁₁⁽²⁾ bajo MSE cuando ŷ < y

**MSE:** Loss = (y - ŷ)²

**Gradiente:**
```
∂Loss/∂W₁₁⁽²⁾ = -2(y - ŷ)·a₁

Si ŷ < y:
  (y - ŷ) > 0
  -2(y - ŷ)·a₁ < 0  (porque a₁ = 5 > 0)
```

**Actualización:** W₁₁⁽²⁾ ← W₁₁⁽²⁾ - α·(gradiente negativo) → **Aumenta** (signo +)

---

## 3. Mini-batch con dos inputs

```
x⁽¹⁾: z₁ > 0, z₂ ≤ 0  → Solo columna 1 de W⁽¹⁾ recibe gradiente
x⁽²⁾: z₁ ≤ 0, z₂ > 0  → Solo columna 2 de W⁽¹⁾ recibe gradiente
```

**Por qué ambas columnas reciben gradiente:**
- Columna 1 (W₁₁⁽¹⁾, W₂₁⁽¹⁾): Se actualiza por x⁽¹⁾
- Columna 2 (W₁₂⁽¹⁾, W₂₂⁽¹⁾): Se actualiza por x⁽²⁾

**Promedio del batch:** Ambas contribuyen

---

## 4. Leaky ReLU: Aα(z) = máx{z, αz} con α > 0

**ReLU:** Derivada = 0 para z < 0 → pesos no se actualizan

**Leaky ReLU:** Derivada = α para z < 0 (α pequeño, ej: 0.01)

**Ventaja:** Neuronas con z < 0 todavía reciben gradiente pequeño → pueden "revivir"

**Ejemplo:**
```
z = -5
ReLU: output = 0, derivada = 0 (neurona "muerta")
Leaky ReLU (α=0.01): output = -0.05, derivada = 0.01 (sigue aprendiendo)
```

**Fuente:** Clase 2-01-09-2025
