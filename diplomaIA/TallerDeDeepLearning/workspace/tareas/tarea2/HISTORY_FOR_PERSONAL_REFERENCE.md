# Tarea 2 - History Log (Personal Reference)

## CURRENT SESSION: Realistic Progression (Iterations 1-4)
**Date:** 2025-11-16
**Wandb Project:** Taller de IA - Tarea 2

---

### ITERATION 1: Baseline (h=64, d=0.0, e=20)
**Wandb Name:** `Corrida 1 - Sin regularización (baseline)`

**Results:**
- Val Acc: 92.46%
- Test Acc: 92.54%
- Macro F1: 51.26%

**Per-Class (Test):**
- N: precision=0.93, recall=0.99, f1=0.96
- S: precision=0.00, recall=0.00, f1=0.00 ← ZERO!
- V: precision=0.88, recall=0.58, f1=0.70
- F: precision=0.00, recall=0.00, f1=0.00 ← ZERO!
- Q: precision=0.93, recall=0.88, f1=0.90

**Analysis:** Model ignores minorities. Just predicts N. High accuracy but terrible F1.

---

### ITERATION 2: More Epochs (h=64, d=0.0, e=50)
**Wandb Name:** `Corrida 2 - De 20 a 50 épocas`

**Results:**
- Val Acc: 98.00% (best at epoch 36)
- Test Acc: 97.13%
- Macro F1: 83.91% (+32.65%)

**Per-Class (Test):**
- N: precision=0.98, recall=0.99, f1=0.99
- S: precision=0.88, recall=0.55, f1=0.68
- V: precision=0.92, recall=0.92, f1=0.92
- F: precision=0.57, recall=0.75, f1=0.64
- Q: precision=0.98, recall=0.96, f1=0.97

**Analysis:** Huge improvement! S and F now detected. Instability at epochs 43-45.

---

### ITERATION 3: Bigger Model (h=128, d=0.0, e=50)
**Wandb Name:** `Corrida 3 - Hidden 64 a 128`

**Results:**
- Val Acc: 98.46% (best at epoch 48)
- Test Acc: 97.90%
- Macro F1: 89.22% (+5.31%)

**Per-Class (Test):**
- N: precision=0.99, recall=0.99, f1=0.99
- S: precision=0.90, recall=0.69, f1=0.78
- V: precision=0.95, recall=0.91, f1=0.93
- F: precision=0.80, recall=0.76, f1=0.78
- Q: precision=0.96, recall=0.99, f1=0.97

**Analysis:** Best results so far. Balanced precision/recall. No overfitting (gap 0.29%).

---

### ITERATION 4: Class Weights (h=128, d=0.0, e=50, weighted loss)
**Wandb Name:** `Corrida 4 - Agregando pesos por clase`

**Results:**
- Val Acc: 94.27% (best at epoch 36) ← DOWN
- Test Acc: 93.34% ← DOWN
- Macro F1: 77.56% ← DOWN from 89.22%

**Per-Class (Test):**
- N: precision=0.99, recall=0.93, f1=0.96
- S: precision=0.41, recall=0.79, f1=0.54 ← HIGH RECALL, LOW PRECISION
- V: precision=0.79, recall=0.95, f1=0.86
- F: precision=0.40, recall=0.91, f1=0.55 ← HIGH RECALL, LOW PRECISION
- Q: precision=0.94, recall=0.98, f1=0.96

**Analysis:** Class weights TOO AGGRESSIVE. Model over-predicts minorities. Recall up but precision terrible. F1 dropped significantly.

---

### ITERATION 5: Extended Training (h=128, d=0.0, e=200)
**Wandb Name:** `Corrida 5 - Revertir pesos, 200 épocas`

**Results:**
- Val Acc: 98.70% (best at epoch 170)
- Test Acc: 98.54%
- Macro F1: 91.73% (+14.17% from iter 4, +2.51% from iter 3)

**Per-Class (Test):**
- N: precision=0.99, recall=1.00, f1=0.99
- S: precision=0.89, recall=0.80, f1=0.84
- V: precision=0.97, recall=0.95, f1=0.96
- F: precision=0.77, recall=0.84, f1=0.80
- Q: precision=0.99, recall=0.99, f1=0.99

**Analysis:** Reverting weights was correct! Extended training allowed natural learning of minority patterns with BALANCED precision/recall. Best overall F1. Train/val gap ~1% - minimal overfitting.

---

## COMPARISON TABLE

| Iter | Config | Val Acc | Macro F1 | S Recall | F Recall | S Precision | F Precision |
|------|--------|---------|----------|----------|----------|-------------|-------------|
| 1 | h64 e20 | 92.46% | 51.26% | 0% | 0% | - | - |
| 2 | h64 e50 | 98.00% | 83.91% | 55% | 75% | 88% | 57% |
| 3 | h128 e50 | 98.46% | 89.22% | 69% | 76% | 90% | 80% |
| 4 | h128 e50 + weights | 94.27% | 77.56% | 79% | 91% | 41% | 40% |
| 5 | h128 e200 | 98.70% | **91.73%** | **80%** | 84% | **89%** | **77%** |

---

## KEY INSIGHT: Class Weights Backfired

Inverse frequency weights were:
- N: ~0.068 (83% of data → low weight)
- S: ~2.26 (2.5% of data → medium weight)
- F: ~7.12 (0.7% of data → HIGH weight)

Result: Model became "afraid" of missing F and S, so it predicts them too often → many false positives.

**ITERATION 3 WAS THE BEST RESULT (F1=89.22%)**

---

## OLD EXPERIMENTS (for reference)

### Run 1: Initial Training (20 epochs) - BEFORE CURRENT SESSION
**Wandb Group:** None (ungrouped) - 4 models trained simultaneously

- LSTM h64 l2: 92.52%
- LSTM h128 l2: 96.78%
- LSTM h64 l3: 95.45%
- GRU h64 l2: 97.87% ← Winner with 20 epochs

### Run 2: Extended Training (200 epochs) - BEFORE CURRENT SESSION
**Wandb Group:** "Extended Training (200 epochs)"

- LSTM h64 l2: 98.71%
- **LSTM h128 l2: 98.89%** ← Final Winner
- LSTM h64 l3: 98.74%
- GRU h64 l2: 98.79%

Final model (LSTM h128 l2 with dropout 0.3, 200 epochs):
- Test Acc: 98.64%
- F1-Score: 92.70%
- S recall: 83%, F recall: 82%
