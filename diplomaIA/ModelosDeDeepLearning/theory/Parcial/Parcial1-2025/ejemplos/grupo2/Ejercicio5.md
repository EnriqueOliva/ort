# Ejercicio 5 - Dropout

## 1. Cómo funciona Dropout durante entrenamiento

**Cada neurona tiene probabilidad p de "apagarse" (output = 0)**

```
Ejemplo con p = 0.2 (20% dropout):

Capa con 5 neuronas antes de dropout:
  [3.5, 2.1, -0.8, 4.2, 1.5]

Máscara aleatoria (Bernoulli):
  [1, 0, 1, 1, 0]  ← 20% son 0

Después de dropout:
  [3.5, 0.0, -0.8, 4.2, 0.0]
```

**Nueva máscara cada batch:**
```
Batch 1: [1,0,1,1,0] → neuronas 2 y 5 apagadas
Batch 2: [1,1,0,1,1] → neurona 3 apagada
Batch 3: [0,1,1,1,0] → neuronas 1 y 5 apagadas
```

**Efecto:** Red no puede depender de neuronas específicas → aprende features distribuidas

---

## 2. Ajuste del forward en inferencia

**Durante training:**
- Dropout activo: algunas neuronas = 0
- Promedio de neuronas activas = (1-p) × total

**Durante inferencia:**
- NO hay dropout: todas activas
- Sin ajuste: outputs serían más grandes

**Solución: Escalar pesos por (1-p)**

```
Ejemplo con p = 0.2:

Training (p=0.2):
  Input: [5, 5, 5, 5, 5]
  Máscara: [1, 0, 1, 1, 0]
  Output: [5, 0, 5, 5, 0]
  Suma promedio: (5+0+5+5+0) = 15

Inferencia sin escalar:
  Input: [5, 5, 5, 5, 5]
  Output: [5, 5, 5, 5, 5]
  Suma: 25  ← Muy diferente!

Inferencia con escalar (×0.8):
  Output: [4, 4, 4, 4, 4]
  Suma: 20  ← Más cercano a 15
```

**Fórmula:** W_inferencia = W_training × (1-p)

---

## 3. Efecto ensemble

**Dropout entrena múltiples subredes:**

```
Red completa: 4 neuronas {1,2,3,4}

Batch 1: Máscara [1,1,0,1] → Subred A = {1,2,4}
Batch 2: Máscara [1,0,1,1] → Subred B = {1,3,4}
Batch 3: Máscara [0,1,1,1] → Subred C = {2,3,4}
...
```

**Con N neuronas y p=0.5: 2^N subredes posibles**

**En inferencia:** Promedia implícitamente todas las subredes entrenadas

**Por qué reduce varianza:**
- Ensemble de modelos: promedio de predicciones más estable
- Cada subred especializada en diferentes features
- Combinación reduce errores individuales

**Analogía:** Consultar 5 médicos (promedio) vs 1 médico (más varianza)

**Fuente:** Clase 6-06-10-2025
