# Ejercicio 1 - Dataset Desbalanceado (Neumonía)

## Contexto

**Dataset:** Radiografías de tórax
- 90% clase No (sin neumonía)
- 10% clase Yes (con neumonía)

**Problema:** Dataset desbalanceado

---

## a. Class Weights para balancear errores

**Sin class weights:**
```
Modelo naive: "Predecir siempre No"
Accuracy: 90% (¡parece bueno pero es inútil!)
Nunca detecta neumonía (los casos importantes)
```

**Con class weights:**

**Fórmula:**
```
weight_clase = N_total / (N_clases × N_ejemplos_clase)

N_total = 1000 imágenes
N_clases = 2
No: 900 ejemplos → weight_No = 1000/(2×900) = 0.56
Yes: 100 ejemplos → weight_Yes = 1000/(2×100) = 5.0
```

**Efecto en la loss:**
```
Loss_total = Σ (weight_clase × loss_ejemplo)

Ejemplo No mal clasificado: loss × 0.56
Ejemplo Yes mal clasificado: loss × 5.0  ← Penaliza 9× más

Resultado: Red aprende a detectar neumonía (clase minoritaria)
```

**Objetivo:** Que ambos tipos de errores valgan igual
- Error en No: común pero peso bajo (×0.56)
- Error en Yes: raro pero peso alto (×5.0)
- Esperanza de loss balanceada

---

## b. ¿Es regularización?

**NO es regularización técnicamente**

**Regularización:** Técnicas que modifican loss para prevenir overfitting
- L1/L2: penalizan pesos grandes
- Dropout: apagan neuronas
- Objetivo: generalizar mejor

**Class weights:**
- Modifica importancia relativa de clases
- NO penaliza complejidad del modelo
- Objetivo: balancear dataset desbalanceado

**Por qué se puede confundir:**
- Ambas modifican la loss function
- Ambas mejoran generalización indirectamente

**Diferencia clave:**
- Regularización: controla capacidad del modelo
- Class weights: corrige sesgo de datos

**Respuesta: NO, class weights NO es regularización. Es una técnica de balanceo de datos.**

**Fuente:** Clase 5-29-09-2025
