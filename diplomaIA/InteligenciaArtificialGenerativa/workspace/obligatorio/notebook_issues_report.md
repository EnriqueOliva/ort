# Jupyter Notebook Analysis Report
**File:** `C:\Users\Enrique\Documents\2doSemestre\InteligenciaArtificialGenerativa\workspace\obligatorio\main.ipynb`
**Analysis Date:** 2025-11-18

---

## Executive Summary

**Total Cells:** 71 (indexed 0-70)

### Critical Issues Found:
1. **DUPLICATE EXPERIMENT NUMBER** - Two different cells are labeled "Experimento 4"
2. **Cell 33** contains only markdown text (no executable code)
3. **Mismatched experiment numbering** between cells 56, 58, and 60

---

## 1. Complete Cell Index (Abbreviated)

| Index | Type     | Content Preview (First 100 chars)                                                    |
|-------|----------|--------------------------------------------------------------------------------------|
| 0     | markdown | # Evolución de las GANs: Vanilla GAN → WGAN → WGAN-GP  **Autor:** Enrique Oliva... |
| 1     | markdown | ## 1. Configuración e Importaciones                                                 |
| 2     | code     | # Para correr en Google Colabs (descomentar):  # !pip install wandb...              |
| 3     | code     | import os import torch import torch.nn as nn import torch.optim as optim...          |
| ...   | ...      | ...                                                                                  |
| 33    | markdown | ### 6.3 Entrenamiento WGAN-GP (Gradient Penalty)  WGAN-GP reemplaza el weight...    |
| ...   | ...      | ...                                                                                  |
| 56    | markdown | ## Experimento 4: Análisis de Distribución de Pesos (WGAN vs WGAN-GP)               |
| 58    | markdown | ## Experimento 5: Sensibilidad a Hiperparámetros                                     |
| 60    | markdown | ## Experimento 4: Sensibilidad a Hiperparámetros                                     |
| ...   | ...      | ...                                                                                  |
| 70    | markdown | ---  ## Referencias  1. **Goodfellow, I., Pouget-Abadie, J., Mirza, M...            |

---

## 2. Cell 33 Detailed Analysis

**Cell Index:** 33
**Cell Type:** markdown (NOT code)
**Content Type:** Documentation/explanation text

### Full Content of Cell 33:
```markdown
### 6.3 Entrenamiento WGAN-GP (Gradient Penalty)

WGAN-GP reemplaza el weight clipping con una penalización por gradiente. En lugar de forzar los pesos, penaliza cuando la norma del gradiente se desvía de 1.

**Mejoras sobre WGAN:**
- No restringe artificialmente los pesos
- Mejor utilización de la capacidad del modelo
- Gradientes más estables y predecibles
- Menor sensibilidad a hiperparámetros
```

### Analysis:
- **Issue:** This is a markdown cell, not a code cell
- **Impact:** When you "ran" cell 33, nothing printed because it's just documentation text
- **Expected Behavior:** Markdown cells display formatted text but don't execute Python code
- **This explains why it "ran but didn't print anything"**

---

## 3. Experiment 4 and 5 Occurrences

### Experimento 4 Found In:

#### Cell 56 (markdown) - FIRST "Experimento 4"
```markdown
## Experimento 4: Análisis de Distribución de Pesos (WGAN vs WGAN-GP)

Un problema fundamental del weight clipping en WGAN es que **fuerza los pesos h...
```

#### Cell 60 (markdown) - SECOND "Experimento 4" (DUPLICATE!)
```markdown
## Experimento 4: Sensibilidad a Hiperparámetros

Evaluamos cómo cada método responde a diferentes valores de sus hiperparámetros principales:
- **WGA...
```

#### Cell 61 (code) - Related code for second Experimento 4
```python
print("EXPERIMENTO 4: Sensibilidad a Hiperparámetros")
print(f"Épocas por experimento: {NUM_EPOCHS}\n")
```

#### Cell 63 (code) - Related plotting code
```python
plt.suptitle('Experimento 4: Sensibilidad a Hiperparámetros', ...)
```

### Experimento 5 Found In:

#### Cell 58 (markdown) - ONLY "Experimento 5"
```markdown
## Experimento 5: Sensibilidad a Hiperparámetros

**Objetivo**: Demostrar empíricamente que WGAN-GP es más robusta a variaciones en sus hiperparámetro...
```

---

## 4. Duplicate Experiment Detection

### Complete Experiment Distribution:

| Experiment # | Occurrences | Status       | Cells                |
|--------------|-------------|--------------|----------------------|
| Experimento 1 | 1          | ✓ OK         | Cell 44              |
| Experimento 2 | 1          | ✓ OK         | Cell 47              |
| Experimento 3 | 1          | ✓ OK         | Cell 51              |
| **Experimento 4** | **2** | **✗ DUPLICATE** | **Cells 56 and 60** |
| Experimento 5 | 1          | ✓ OK         | Cell 58              |

### Detailed Duplicate Information:

**Experimento 4 - First Instance (Cell 56):**
- Title: "Análisis de Distribución de Pesos (WGAN vs WGAN-GP)"
- Topic: Weight distribution analysis comparing WGAN and WGAN-GP
- Related code: Cell 57

**Experimento 4 - Second Instance (Cell 60):**
- Title: "Sensibilidad a Hiperparámetros"
- Topic: Hyperparameter sensitivity analysis
- Related code: Cells 61, 62, 63

---

## 5. Structural Issues Summary

### Issue 1: Duplicate "Experimento 4"
**Location:** Cells 56 and 60
**Problem:** Two different experiments both labeled as "Experimento 4"
**Impact:** Confusing numbering, makes it unclear which is the actual 4th experiment

### Issue 2: Missing/Misplaced "Experimento 5"
**Location:** Cell 58
**Problem:** "Experimento 5" appears BEFORE the second "Experimento 4" (Cell 60)
**Impact:** Illogical experiment ordering (4 → 5 → 4)

### Issue 3: Cell 33 is Markdown (not Code)
**Location:** Cell 33
**Problem:** User expected executable code, but it's just documentation
**Impact:** No output when "run", leading to confusion

---

## 6. Recommended Fixes

### Option A: Renumber Second "Experimento 4" to "Experimento 5"
1. Keep Cell 56 as "Experimento 4: Análisis de Distribución de Pesos"
2. **DELETE** Cell 58 (current "Experimento 5")
3. **RENAME** Cell 60 from "Experimento 4" to "Experimento 5: Sensibilidad a Hiperparámetros"
4. Update Cell 61 print statement to say "EXPERIMENTO 5"
5. Update Cell 63 plot title to say "Experimento 5"

### Option B: Renumber to Create Experimento 6
1. Keep Cell 56 as "Experimento 4: Análisis de Distribución de Pesos"
2. Keep Cell 58 as "Experimento 5: Sensibilidad a Hiperparámetros"
3. **RENAME** Cell 60 from "Experimento 4" to "Experimento 6: Sensibilidad a Hiperparámetros Detallado"
4. Update Cell 61 print statement to say "EXPERIMENTO 6"
5. Update Cell 63 plot title to say "Experimento 6"

### Option C: Merge Experiments 4 and 5
1. Keep Cell 56 as "Experimento 4: Análisis de Distribución de Pesos"
2. **DELETE** Cells 58 and 60 (both markdown headers)
3. Create a **NEW** markdown cell after Cell 56: "Experimento 5: Sensibilidad a Hiperparámetros"
4. Move code cells 61-63 to follow the new Experimento 5 header

---

## 7. Cell-by-Cell Experiment Structure

Current structure with issues highlighted:

```
Cell 44:  ## Experimento 1: Estableciendo Baselines - Las 3 Variantes ✓
Cell 45-46: [Code for Experimento 1]

Cell 47:  ## Experimento 2: Comparación General - Evolución del Entrenamiento ✓
Cell 48-50: [Code for Experimento 2]

Cell 51:  ## Experimento 3: Análisis de Estabilidad de Gradientes ✓
Cell 52-55: [Code for Experimento 3]

Cell 56:  ## Experimento 4: Análisis de Distribución de Pesos (WGAN vs WGAN-GP) ✓
Cell 57:  [Code for Experimento 4 - First instance]

Cell 58:  ## Experimento 5: Sensibilidad a Hiperparámetros ← ISSUE: Out of sequence
Cell 59:  [Code for Experimento 5]

Cell 60:  ## Experimento 4: Sensibilidad a Hiperparámetros ← ISSUE: DUPLICATE NUMBER
Cell 61-63: [Code for Experimento 4 - Second instance]
```

---

## 8. Why Cell 33 Didn't Print Anything

**Explanation:**
- Cell 33 is a **markdown cell**, not a code cell
- Markdown cells display formatted text/documentation
- They don't execute Python code
- When you "run" a markdown cell, it just renders the formatted text
- No print statements = no output to console

**What Cell 33 Actually Does:**
It displays a formatted section header and explanation text about WGAN-GP's gradient penalty approach. It's purely documentation.

---

## Conclusion

The notebook has a clear structural issue with duplicate experiment numbering:
- **Two cells** are labeled "Experimento 4" (Cells 56 and 60)
- These experiments cover **different topics** (Weight Distribution vs Hyperparameter Sensitivity)
- Cell 58's "Experimento 5" appears between the two "Experimento 4" cells
- This creates a confusing sequence: Exp 1 → Exp 2 → Exp 3 → Exp 4 → Exp 5 → Exp 4 (again)

**Recommended Action:** Choose one of the renumbering options above to fix the duplicate numbering and restore logical experiment ordering.
