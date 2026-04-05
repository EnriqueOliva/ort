# Ejercicio 2 - Análisis de Arquitectura CNN

## a. Tipo de problema

**Clasificación multiclase** - La salida muestra "classify" con múltiples clases (car, bus, truck, motor, person)

---

## b. Tipo de arquitectura

**CNN (Convolutional Neural Network)** - Bloques convolucionales (3,4,5) seguidos de capas densas (6,7)

---

## c. Matching números-letras

**1. Input inicial (matriz 3D con valores)**
→ **C. Canales de entrada** (RGB, 3 canales)

**2. Bloques verdes (operaciones sobre volúmenes 3D)**
→ **E. Bloque convolucional** (Conv + activación + pooling)

**3. Primera operación verde (filtros aplicados)**
→ **A. Función de activación** (ReLU después de conv)

**4. Líneas punteadas dentro de bloques**
→ **G. Skip connections** (conexiones residuales)

**5. Bloques más oscuros dentro de verdes**
→ **F. Alto de las features** (mayor profundidad = más canales)

**6. Barras azules/celestes (capas MLP)**
→ **D. Capas densas** (fully connected)

**7. Vector final antes de classify**
→ **I. Canales de las features** (features extraídas para clasificar)

---

**Letras sin match:**
- **B. Dropout** - No visible en diagrama
- **H. Ancho de las features** - Las dimensiones espaciales (reducidas por pooling)
- **J. Batch size** - No se representa en el diagrama

---

## d. Función de pérdida

**Categorical Cross-Entropy (CCE)**

Clasificación multiclase + Softmax → CCE

**Fuentes:** Clases 6 y 7 (2025)
