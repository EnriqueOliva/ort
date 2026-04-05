# Ejercicio 6 - CNN para Clasificación

## 1. Tabla de shapes (C₁=32, C₂=64)

| Operación | Salida (N,H,W,C) |
|-----------|------------------|
| Entrada | (N,32,32,3) |
| Conv 3×3, 3→32, stride 1, same | (N,32,32,32) |
| ReLU | (N,32,32,32) |
| Conv 3×3, 32→32, stride 1, same | (N,32,32,32) |
| ReLU | (N,32,32,32) |
| MaxPool 2×2, stride 2 | (N,16,16,32) |
| Conv 3×3, 32→64, stride 1, same | (N,16,16,64) |
| ReLU | (N,16,16,64) |
| Conv 3×3, 64→64, stride 1, same | (N,16,16,64) |
| ReLU | (N,16,16,64) |
| MaxPool 2×2, stride 2 | (N,8,8,64) |
| GAP | (N,64) |
| Linear 64→10 | (N,10) |
| Softmax | (N,10) |

**C_out después de GAP = 64**

---

## 2. Parámetros totales

```
Conv 3×3 (3→32): 3×3×3×32 + 32 = 896
Conv 3×3 (32→32): 3×3×32×32 + 32 = 9,248
Conv 3×3 (32→64): 3×3×32×64 + 64 = 18,496
Conv 3×3 (64→64): 3×3×64×64 + 64 = 36,928
Linear (64→10): 64×10 + 10 = 650

Total: 896 + 9,248 + 18,496 + 36,928 + 650 = 66,218 params
```

---

## 3. BatchNorm

**Parámetros por capa:** 2 × canales (γ y β)

```
Después de cada Conv:
  BN(32): 2×32 = 64
  BN(32): 2×32 = 64
  BN(64): 2×64 = 128
  BN(64): 2×64 = 128

Total BN: 384 params
```

**Total con BN: 66,218 + 384 = 66,602 params**

---

## 4. Comparación con MLP

**MLP:** Input (32,32,3) → Flatten → Dense(512) → Dense(512) → Dense(10)

```
Flatten: 32×32×3 = 3,072 valores

Dense(3,072→512): 3,072×512 + 512 = 1,573,376
Dense(512→512): 512×512 + 512 = 262,656
Dense(512→10): 512×10 + 10 = 5,130

Total MLP: 1,841,162 params
```

**Comparación:**

| Aspecto | CNN | MLP |
|---------|-----|-----|
| **Parámetros** | 66,218 | 1,841,162 |
| **Ratio** | 1× | **28× más** |

**(i) Número parámetros:** CNN tiene 28× menos

**(ii) Equivalencia por traslación:** CNN SÍ (filtros detectan patrones en cualquier posición), MLP NO (cada peso es posición específica)

**(iii) Sobreajuste esperado:** MLP mucho mayor (1.8M params memorizan fácilmente), CNN menor (66k params más generalizable)

**Fuente:** Clases 5, 6, 7 (2025)
