# Ejercicio 3 - Transfer Learning

## 1. ¿Qué es transfer learning?

**Transfer learning** es tomar una red pre-entrenada en un dataset grande (ej: ImageNet con millones de imágenes), **congelar** las capas convolucionales (no entrenarlas), y **reemplazar** solo las capas Dense finales para tu tarea específica.

```
Red pre-entrenada:     Conv blocks → MLP → [1000 clases ImageNet]
                           ↓ CONGELAR
Tu tarea:              Conv blocks (frozen) → MLP nuevo → [5 clases tuyas]
                                              ↑ ENTRENAR solo esto
```

**Fuente:** Clase 6-06-10-2025

---

## 2. Beneficios vs entrenamiento desde cero

| Aspecto | Desde cero | Transfer Learning |
|---------|------------|-------------------|
| **Tiempo** | Días/semanas | Horas |
| **Datos necesarios** | Millones | Miles |
| **Parámetros a entrenar** | Todos (~25M) | Solo MLP (~50k) |
| **Resultados** | Buenos con muchos datos | Buenos con pocos datos |

**Por qué funciona:**
- Las capas Conv ya aprendieron features generales: bordes, texturas, formas, patrones
- Estas features son útiles para MUCHAS tareas de visión
- Solo necesitas entrenar el clasificador final para tu problema específico

---

## 3. ¿Cómo seleccionar el modelo pre-entrenado?

**Criterios:**

1. **Dataset de pre-entrenamiento:**
   - Si tu tarea es visión general → ImageNet (VGG, ResNet)
   - Si es médica → modelo pre-entrenado en imágenes médicas
   - Si es texto → BERT, GPT

2. **Complejidad:**
   - Problema simple → VGG16, ResNet50
   - Problema complejo → ResNet101, EfficientNet

3. **Recursos computacionales:**
   - GPU limitada → modelo más pequeño (VGG16)
   - GPU potente → modelo más grande (ResNet152)

**Disponibles públicamente:** VGG, ResNet, Inception, EfficientNet (descargables con Keras/PyTorch)

---

## 4. Ejemplo práctico

**Problema:** Clasificar 5 tipos de rostros humanos con solo 2,000 imágenes.

**Solución con Transfer Learning:**

```python
# 1. Cargar red pre-entrenada (entrenada en ImageNet)
from keras.applications import VGG16

base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224,224,3))

# 2. CONGELAR capas convolucionales
for layer in base_model.layers:
    layer.trainable = False  # No entrenar estas capas

# 3. Agregar nuevo clasificador para 5 clases
model = Sequential([
    base_model,                    # Capas Conv CONGELADAS
    Flatten(),
    Dense(256, activation='relu'), # MLP nuevo
    Dense(5, activation='softmax') # 5 tipos de rostros
])

# 4. Entrenar SOLO las capas Dense nuevas
model.compile(optimizer='adam', loss='categorical_crossentropy')
model.fit(X_train, y_train, epochs=10)
```

**Resultado:**
- Solo entrenar 2 capas Dense (~500k parámetros)
- Las capas Conv (14M parámetros) ya saben detectar features faciales
- Converge rápido con pocos datos

**Comparación:**

```
SIN Transfer Learning:
  - Entrenar 14.7M parámetros desde cero
  - Necesita 100k+ imágenes
  - Entrena 50+ épocas
  - Accuracy: 70% (con 2k imágenes insuficientes)

CON Transfer Learning:
  - Entrenar 500k parámetros (solo MLP)
  - 2k imágenes son suficientes
  - Entrena 10-15 épocas
  - Accuracy: 92% (features pre-aprendidas)
```

**Fuente:** Clase 6-06-10-2025

---
