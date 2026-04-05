# Ejercicio 2 - Solución

## Pregunta 1: Partición de datos en train, test y validation

### Objetivo de particionar los datos

En deep learning, dividimos los datos en **tres conjuntos** con roles completamente diferentes:

```
Dataset completo (100%)
    ↓
┌─────────────────────────────────────────────────┐
│ TRAIN (60-70%)                                  │ ← Entrenar la red
├─────────────────────────────────────────────────┤
│ VALIDATION/SELECTION (15-20%)                   │ ← Seleccionar hiperparámetros
├─────────────────────────────────────────────────┤
│ TEST (15-20%)                                   │ ← Evaluar modelo final
└─────────────────────────────────────────────────┘
```

---

### 1. Training Set (Conjunto de entrenamiento)

**Objetivo:** Entrenar la red neuronal - ajustar todos los pesos y biases.

**Uso durante entrenamiento:**
- Se usa en CADA época de entrenamiento
- La red ve estos datos batch por batch
- Se calcula el gradiente de la loss function sobre estos datos
- Los pesos se actualizan mediante backpropagation con estos gradientes

**Proceso:**
```
ÉPOCA 1:
  Para cada batch en train:
    1. Forward pass: calcular predicciones
    2. Calcular loss
    3. Backward pass: calcular gradientes
    4. Actualizar pesos (w ← w - α·∇w)

ÉPOCA 2:
  Repetir con los mismos datos...

ÉPOCA N:
  Repetir...
```

**Característica clave:** La red "ve" estos datos muchas veces (una por época). Los pesos se optimizan para minimizar el error en ESTOS datos específicos.

---

### 2. Validation Set (Conjunto de validación/selección)

**Objetivo:** Monitorear el desempeño durante entrenamiento y seleccionar hiperparámetros.

**Uso durante entrenamiento:**
- Se evalúa AL FINAL de cada época (NO se usa para actualizar pesos)
- Se calcula la loss en validation SIN hacer backpropagation
- Los pesos NO cambian cuando evaluamos en validation

**Para qué sirve:**

**a) Detectar overfitting:**
```
Si:
  train_loss baja pero validation_loss sube
Entonces:
  ¡OVERFITTING! La red memorizó train pero no generaliza
```

**b) Early Stopping:**
```
Monitorear validation_loss:
  Si NO mejora durante N épocas (paciencia) → PARAR
  Devolver los pesos del mejor epoch (menor validation_loss)
```

**c) Selección de hiperparámetros:**
```
Probar diferentes configuraciones:
  - Arquitectura 1 → validation_loss = 0.35
  - Arquitectura 2 → validation_loss = 0.22  ← ELEGIR esta
  - Arquitectura 3 → validation_loss = 0.28

Probar diferentes learning rates:
  - lr = 0.001 → validation_loss = 0.25
  - lr = 0.01  → validation_loss = 0.18  ← ELEGIR este
  - lr = 0.1   → validation_loss = 1.50
```

**Cita de la clase 7-13-10-2025:**
> "Cuando seleccionas usas train y selección... una vez que seleccionaste todos los hiperparámetros, elegiste la red que más te gusta, pero eso lo hice con un conjunto de validación."

**IMPORTANTE:** El conjunto de validation SE USA durante el entrenamiento, pero NO para actualizar pesos. Solo para MONITOREAR y DECIDIR.

---

### 3. Test Set (Conjunto de test)

**Objetivo:** Evaluar el modelo final de forma imparcial.

**Uso:**
- Se usa UNA SOLA VEZ al final de TODO el proceso
- NO se usa durante entrenamiento
- NO se usa para seleccionar hiperparámetros
- Es la evaluación "justa" del modelo

**¿Por qué necesitamos test separado de validation?**

```
PROBLEMA:
  Si usamos validation para elegir hiperparámetros,
  el modelo se "adapta indirectamente" a validation.

SOLUCIÓN:
  Test set = conjunto completamente virgen
  Nunca influenció ninguna decisión de diseño
```

**Cita de la clase 7-13-10-2025:**
> "Una vez que hiciste eso, juntas todo y validas el modelo que vos elegiste."

**Ejemplo del proceso completo:**

```
PASO 1: Entrenamiento
  Epochs 1-50:
    - Entrenar con TRAIN
    - Evaluar con VALIDATION al final de cada época
    - Early stopping para cuando validation no mejore

PASO 2: Selección de hiperparámetros
  Probar 10 arquitecturas diferentes:
    - Cada una entrena con TRAIN
    - Cada una evalúa con VALIDATION
    - Elegir la de menor validation_loss

PASO 3: Evaluación final
  Tomar el mejor modelo del PASO 2
  Evaluar UNA VEZ en TEST
  Reportar: "El modelo tiene 92% accuracy en test"
```

---

### Resumen visual del uso

```
┌──────────────────────────────────────────────────────────┐
│ DURANTE ENTRENAMIENTO (cada época)                       │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  TRAIN:                                                  │
│    ├─ Batch 1 → forward → loss → backward → update pesos│
│    ├─ Batch 2 → forward → loss → backward → update pesos│
│    └─ Batch N → forward → loss → backward → update pesos│
│                                                          │
│  VALIDATION (al final de época):                         │
│    └─ Todo el conjunto → forward → loss → NO update     │
│                          ↓                               │
│                    ¿Mejoró?                              │
│                    ↓    ↓                                │
│                   SÍ   NO                                │
│                   ↓     ↓                                │
│              Guardar  Paciencia--                        │
│               pesos                                      │
│                         ↓                                │
│                   Si paciencia=0                         │
│                      → PARAR                             │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ AL FINAL DE TODO                                         │
├──────────────────────────────────────────────────────────┤
│  TEST:                                                   │
│    └─ Evaluar UNA VEZ → Reporte final                   │
└──────────────────────────────────────────────────────────┘
```

---

## Pregunta 2: Análisis de curvas de entrenamiento

### Contexto de las dos gráficas

**Gráfica IZQUIERDA:**
```
Época 0-20
Loss inicial: ~0.35 (train), ~0.20 (validation)
Loss final:   ~0.08 (train), ~0.20 (validation)

Patrón:
  - Train loss BAJA continuamente (0.35 → 0.08)
  - Validation loss BAJA al inicio (0.20 → 0.16 en época ~4)
  - Validation loss SUBE después (0.16 → 0.20)
```

**Gráfica DERECHA:**
```
Época 0-70
Loss inicial: ~0.35 (ambas)
Loss final:   ~0.13 (ambas)

Patrón:
  - Train y validation PEGADAS todo el tiempo
  - Ambas BAJAN juntas suavemente
  - Convergen a ~0.13
```

---

### a. ¿Cuál entrenamiento es mejor?

**Respuesta: La gráfica de la DERECHA es MUCHO mejor**

### Justificación

**Análisis de la gráfica IZQUIERDA:**

```
PROBLEMA: OVERFITTING SEVERO

Época 0-4:
  Train:      0.35 → 0.15  ✓ Mejora
  Validation: 0.20 → 0.16  ✓ Mejora
  → TODO BIEN

Época 4-20:
  Train:      0.15 → 0.08  ✓ Sigue mejorando
  Validation: 0.16 → 0.20  ✗ EMPEORA
  → ¡OVERFITTING!
```

**¿Qué está pasando?**

La red está **memorizando** el conjunto de entrenamiento en lugar de **aprender patrones generales**.

```
ÉPOCA 4:
  Red aprendió: "Detectar bordes, círculos, patrones generales"
  Train loss: 0.15
  Val loss:   0.16
  → Generaliza bien

ÉPOCA 20:
  Red aprendió: "La imagen #347 es un gato, la #891 es un perro..."
  Train loss: 0.08  ← Bajó porque memorizó train
  Val loss:   0.20  ← Subió porque nunca vio validation
  → NO generaliza
```

**Cita de la clase 7-13-10-2025:**
> "En validación nos puede pasar esto... Overfit... ¿Y qué soluciones, qué técnicas? Regularizar. Exacto."

**Síntomas de overfitting:**
1. Gap enorme entre train y validation loss (0.08 vs 0.20)
2. Train loss sigue bajando mientras validation sube
3. El modelo es inútil para datos nuevos

**Desempeño real:**
```
En entrenamiento: Excelente (loss = 0.08)
En validación:    MALO (loss = 0.20)
En test:          Probablemente MALO (similar a validation)

Conclusión: Modelo SOBREAJUSTADO, no sirve en práctica
```

---

**Análisis de la gráfica DERECHA:**

```
COMPORTAMIENTO IDEAL

Época 0-70:
  Train:      0.35 → 0.13  ✓ Mejora gradualmente
  Validation: 0.35 → 0.13  ✓ Mejora gradualmente
  → Las curvas están PEGADAS
```

**¿Qué está pasando?**

La red está **aprendiendo patrones generales** que funcionan tanto en train como en validation.

```
ÉPOCA 70:
  Red aprendió: "Detectar features complejas que generalizan"
  Train loss: 0.13
  Val loss:   0.13  ← ¡Casi idéntico!
  → Generaliza perfectamente
```

**Síntomas de buen entrenamiento:**
1. Train y validation loss casi idénticos
2. Ambas curvas bajan juntas de forma suave
3. NO hay divergencia entre las curvas
4. Gap mínimo (ambas ~0.13)

**Desempeño real:**
```
En entrenamiento: Bueno (loss = 0.13)
En validación:    Bueno (loss = 0.13)
En test:          Probablemente BUENO

Conclusión: Modelo GENERALIZA BIEN, útil en práctica
```

---

**Comparación directa:**

| Aspecto | Izquierda (MALA) | Derecha (BUENA) |
|---------|------------------|-----------------|
| **Train loss final** | 0.08 | 0.13 |
| **Validation loss final** | 0.20 | 0.13 |
| **Gap (train-val)** | 0.12 (enorme) | 0.00 (mínimo) |
| **Patrón** | Divergen | Pegadas |
| **Overfitting** | SÍ (severo) | NO |
| **Generalización** | MALA | EXCELENTE |
| **Utilidad práctica** | Inútil | Útil |

**Conclusión:**

La gráfica DERECHA es mejor porque:
1. **Generaliza:** Val loss = Train loss
2. **Sin overfitting:** Las curvas NO divergen
3. **Confiable:** El desempeño en train predice el desempeño en test
4. **Útil:** Funcionará bien con datos nuevos

La gráfica IZQUIERDA muestra un modelo que:
1. **NO generaliza:** Val loss >> Train loss
2. **Sobreajustado:** Memorizó train
3. **Engañoso:** Parece "mejor" en train (0.08 vs 0.13) pero es PEOR en práctica
4. **Inútil:** No funcionará con datos nuevos

**Mejor modelo = menor validation loss, NO menor training loss**

---

### b. ¿Qué técnica hace que la izquierda tenga dominio más acotado?

**Respuesta: EARLY STOPPING**

### Justificación

**Observación de las gráficas:**

```
Gráfica IZQUIERDA:  Entrena hasta época 20
Gráfica DERECHA:    Entrena hasta época 70

Diferencia: La izquierda paró ANTES
```

**¿Por qué paró antes?**

La técnica de **Early Stopping** detectó que el validation loss dejó de mejorar y DETUVO el entrenamiento.

---

### ¿Qué es Early Stopping?

**Definición:** Técnica que para el entrenamiento cuando el validation loss deja de mejorar durante N épocas consecutivas (paciencia).

**Cita de la clase 6-06-10-2025:**
> "Early Stopping es una técnica que se podría usar en cualquier situación en la que uno tiene un algoritmo que en cada situación busca la siguiente mejor opción, y monitorea lo que va pasando en validación."

---

### Algoritmo de Early Stopping

```
INICIALIZACIÓN:
  mejor_loss = ∞
  mejor_época = 0
  paciencia_restante = PACIENCIA (ej: 4 épocas)

PARA cada época:
  1. Entrenar con train set
  2. Evaluar en validation set → val_loss

  3. SI val_loss < mejor_loss:
       mejor_loss = val_loss
       mejor_época = época_actual
       paciencia_restante = PACIENCIA  ← Resetear contador
       Guardar pesos actuales
     SINO:
       paciencia_restante = paciencia_restante - 1

  4. SI paciencia_restante == 0:
       PARAR entrenamiento
       Cargar pesos de mejor_época
       RETURN
```

**Cita de la clase 6-06-10-2025:**
> "Es ir entrenando época a época, y cuando uno ve que durante un cierto periodo de épocas la función de costo en validación no mejora, es decir, no disminuye por una cierta cantidad de épocas, parar el entrenamiento y volver hacia el mejor momento."

---

### Aplicación a la gráfica IZQUIERDA

```
SUPOSICIÓN: Paciencia = 4 épocas

Época 0:  val_loss = 0.20  → mejor_loss = 0.20  [Resetear paciencia]
Época 1:  val_loss = 0.19  → mejor_loss = 0.19  [Resetear paciencia]
Época 2:  val_loss = 0.17  → mejor_loss = 0.17  [Resetear paciencia]
Época 3:  val_loss = 0.165 → mejor_loss = 0.165 [Resetear paciencia]
Época 4:  val_loss = 0.16  → mejor_loss = 0.16  [Resetear paciencia] ← MEJOR
Época 5:  val_loss = 0.165 → NO mejoró [paciencia = 3]
Época 6:  val_loss = 0.17  → NO mejoró [paciencia = 2]
Época 7:  val_loss = 0.175 → NO mejoró [paciencia = 1]
Época 8:  val_loss = 0.18  → NO mejoró [paciencia = 0]
                              ↓
                         ¡PARAR!

Resultado: Paró en época 8 (pero el gráfico muestra ~20)
         Devuelve modelo de época 4 (mejor validation loss)
```

**Nota:** La gráfica muestra que llegó a época ~20, lo que sugiere:
- O no usaron early stopping
- O la paciencia era muy grande (~16 épocas)
- O decidieron entrenar todas las épocas de todas formas

Si hubieran usado early stopping con paciencia = 4:
```
┌──────────────────────────────┐
│ CON Early Stopping (p=4)     │
├──────────────────────────────┤
│ Pararía en época ~8-10       │
│ Devolvería modelo de época 4 │
│ Validation loss = 0.16       │
│                              │
│ MEJOR que seguir hasta 20:   │
│   Época 20: val_loss = 0.20  │
└──────────────────────────────┘
```

---

### ¿Por qué la DERECHA tiene dominio más largo?

**Razón:** En la gráfica derecha, el validation loss SIEMPRE mejora (o se mantiene estable bajando).

```
Época 0-70:
  Validation loss: 0.35 → 0.13

  NO HAY momento en que validation loss deje de mejorar
  durante PACIENCIA épocas consecutivas

  → Early stopping NUNCA se activa
  → Entrena todas las 70 épocas
```

**Comparación:**

| Aspecto | Izquierda | Derecha |
|---------|-----------|---------|
| **Val loss mejora** | Solo hasta época ~4 | Hasta época 70 |
| **Early stopping se activa** | SÍ (época ~8-10) | NO |
| **Épocas totales** | Para en ~20 | Completa 70 |
| **Dominio** | Acotado [0,20] | Extendido [0,70] |

---

### Early Stopping como Regularización

**Cita de la clase 6-06-10-2025:**
> "Tiene un efecto regularizador y se puede ver que es equivalente es muy parecido a una regularización L2."

**¿Por qué es regularización?**

Early stopping evita que la red se sobreajuste al conjunto de entrenamiento:
- Para ANTES de que la red memorice todos los ejemplos
- Devuelve el modelo en el "punto óptimo" de generalización
- Previene overfitting SIN agregar términos de penalización

**Beneficio práctico:**

```
SIN Early Stopping (gráfica izquierda si hubiera seguido):
  Época 4:  val_loss = 0.16  ← Mejor momento
  Época 20: val_loss = 0.20  ← Peor
  Época 50: val_loss = 0.25  ← Mucho peor

CON Early Stopping (paciencia=4):
  Pararía en época ~8
  Devolvería modelo de época 4 (val_loss = 0.16)
  ¡Evita overfitting automáticamente!
```

**Cita de la clase 6-06-10-2025:**
> "Lo que sí es más efectivo, es más eficiente que la regularización L2. Porque uno tiene que hacer menos prueba, o sea, la cantidad de lambdas distintos que tendría que buscar como hiperparámetro al hacer regularización L2. Generalmente con la paciencia uno busca menos, busca dos o tres valores de paciencia."

---

### Ejemplo práctico de implementación

**En Keras/TensorFlow:**

```python
from keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor='val_loss',           # Monitorear validation loss
    patience=4,                   # Esperar 4 épocas sin mejora
    restore_best_weights=True,    # Devolver pesos del mejor epoch
    verbose=1                     # Mostrar mensajes
)

model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=100,                   # Máximo 100 épocas
    callbacks=[early_stop]        # Pero puede parar antes
)

# Si val_loss deja de mejorar por 4 épocas consecutivas,
# para automáticamente y devuelve los mejores pesos
```

---

### Visualización del concepto

```
GRÁFICA IZQUIERDA (con Early Stopping ideal):

Loss
0.35│
    │ Train ─────────╮
0.30│               │
    │ Val ──────╮   │
0.25│          │   │
    │         │   │
0.20│────────┼───┴─────────  ← Val deja de bajar
    │        │   ↑
0.15│       ╰───┘  Mejor (época 4)
    │      ↑
0.10│     │  Train sigue bajando (overfitting)
    │    ╰──────────────────
0.05│
    └─────────────────────────────► Época
      0   4   8  12  16  20
          ↑   ↑
      Mejor  Early stopping para aquí (si paciencia=4)


GRÁFICA DERECHA (Early Stopping NO se activa):

Loss
0.35│ Train ─────╮
    │ Val ───────┤ Pegadas
0.30│            │
    │           │
0.25│          │
    │         │
0.20│        │
    │       │
0.15│      │
    │     │
0.13│────┴──────  Ambas convergen sin divergir
    └──────────────────────────────────────────► Época
      0        20        40        60    70

      Early stopping NUNCA se activa porque
      validation loss SIEMPRE mejora
```

---

## Resumen Final

### Pregunta 1: Train/Test/Validation

| Set | Uso | Actualiza pesos | Frecuencia |
|-----|-----|-----------------|------------|
| **Train** | Entrenar red | SÍ | Cada batch |
| **Validation** | Monitorear/Seleccionar | NO | Cada época |
| **Test** | Evaluar final | NO | Una vez al final |

### Pregunta 2a: ¿Cuál es mejor?

**Derecha** es MUCHO mejor:
- Val loss = Train loss (generaliza)
- Sin overfitting
- Útil en práctica

**Izquierda** es MALA:
- Val loss >> Train loss (no generaliza)
- Overfitting severo
- Inútil en práctica

### Pregunta 2b: Técnica para dominio acotado

**Early Stopping:**
- Para cuando val_loss deja de mejorar por N épocas (paciencia)
- Devuelve pesos del mejor epoch
- Previene overfitting automáticamente
- La izquierda pararía antes con early stopping bien configurado

---

**Fuentes:**
- Clase 6-06-10-2025: Early Stopping, Regularización
- Clase 7-13-10-2025: Train/Test/Validation, Análisis de curvas de entrenamiento
