# Conceptos Fundamentales de Deep Learning

Esta guía explica los conceptos básicos de redes neuronales de forma progresiva, desde los fundamentos hasta conceptos más avanzados.

---

## **NIVEL 1: Notación y Conceptos Básicos**

### **¿Qué significan x, y, ŷ?**

Estas son las tres variables fundamentales en machine learning:

- **x** = dato de entrada (input)
- **y** = valor real/verdadero que queremos predecir (target, ground truth)
- **ŷ** (y con sombrero) = predicción que hace la red

**Ejemplo:**
```
Problema: Predecir cuántos helados venderás según la temperatura

x = 25°C          ← La temperatura (dato que tienes)
y = 100 helados   ← Lo que REALMENTE vendiste ese día (dato histórico)
ŷ = 95 helados    ← Lo que tu red PREDICE que venderás

Error = ŷ - y = 95 - 100 = -5 (la red se equivocó por 5 helados)
```

### **¿Qué es un dataset?**

Un **dataset** es un conjunto de pares (x, y) que usas para entrenar tu red.

**Ejemplo:**
```
Dataset de ventas de helados:
Punto 1: x₁ = 20°C → y₁ = 50 helados
Punto 2: x₂ = 25°C → y₂ = 100 helados
Punto 3: x₃ = 30°C → y₃ = 120 helados

Este dataset tiene 3 puntos.
Cada punto tiene una entrada (temperatura) y una salida conocida (ventas).
```

### **¿Cuál es el objetivo de una red neuronal?**

**NO** es memorizar el dataset.

**SÍ** es aprender el patrón para predecir datos nuevos que nunca vio.

**Ejemplo:**
```
Entrenamiento:
- Aprendes con: 20°C→50, 25°C→100, 30°C→120

Uso real (producción):
- Te preguntan: ¿A 27°C cuánto venderé?
- La red predice: ~110 helados (interpolando el patrón aprendido)
```

**Analogía:** Es como estudiar 100 ejercicios de matemáticas para poder resolver ejercicios nuevos en el examen.

---

## **NIVEL 2: Una Neurona Individual**

### **¿Qué es una neurona?**

Una **neurona** es una unidad de cálculo que:
1. Recibe uno o más números
2. Hace una operación matemática
3. Produce un número de salida

**Ejemplo:**
```
Neurona simple:
Recibe: 25
Tiene parámetros: peso = 2, bias = 5
Calcula: salida = (25 × 2) + 5 = 55
Produce: 55
```

### **¿Qué operación matemática hace una neurona?**

La operación depende de cuántos valores recibe:

**CASO 1: Recibe UN valor** (típico en primera capa)
```
Fórmula: z = entrada × peso + bias

Ejemplo:
Entrada: 20
Parámetros: peso = 3, bias = -10
Cálculo: z = (20 × 3) + (-10) = 60 - 10 = 50
Salida: 50
```

**CASO 2: Recibe VARIOS valores** (típico en capas siguientes)
```
Fórmula: z = (entrada₁ × peso₁) + (entrada₂ × peso₂) + ... + bias

Ejemplo:
Entradas: [50, 30]  (dos números)
Parámetros: peso₁ = 0.5, peso₂ = 0.8, bias = 2
Cálculo: z = (50 × 0.5) + (30 × 0.8) + 2
         z = 25 + 24 + 2 = 51
Salida: 51
```

### **¿Qué son los pesos (w) y el bias (b)?**

Son los **parámetros aprendibles** de la neurona:

- **Pesos (w):** Determinan cuánto importa cada entrada
- **Bias (b):** Es un ajuste constante (offset)

**Ejemplo:**
```
Neurona con diferentes parámetros:

Parámetros v1: peso = 10, bias = 0
Entrada: 5 → Salida: (5 × 10) + 0 = 50

Parámetros v2: peso = 1, bias = 100
Entrada: 5 → Salida: (5 × 1) + 100 = 105

Misma entrada, parámetros diferentes → salidas diferentes
```

**Durante el entrenamiento**, la red ajusta automáticamente estos parámetros para reducir el error.

### **¿Cuántos pesos tiene una neurona?**

**Regla fundamental:** Una neurona tiene **tantos pesos como entradas recibe**.

**Ejemplo con arquitectura 1 → 3 → 1:**
```
RED:
Entrada: 1 número (temperatura)
Capa 1: 3 neuronas
Capa 2: 1 neurona

PESOS:
Cada neurona de Capa 1:
  - Recibe 1 entrada → tiene 1 peso + 1 bias

Neurona de Capa 2:
  - Recibe 3 entradas (de las 3 neuronas de Capa 1)
  - Tiene 3 pesos + 1 bias

Total de parámetros:
Capa 1: 3 neuronas × (1 peso + 1 bias) = 6 parámetros
Capa 2: 1 neurona × (3 pesos + 1 bias) = 4 parámetros
TOTAL: 10 parámetros
```

**Regla general:** Si una capa tiene N neuronas, cada neurona de la siguiente capa necesita N pesos.

---

## **NIVEL 3: Funciones de Activación**

### **¿Qué es una función de activación?**

Es una transformación no-lineal que se aplica **después** de calcular z.

**Proceso completo de una neurona:**
```
Paso 1: z = (entradas × pesos) + bias     ← Combinación lineal
Paso 2: a = activación(z)                 ← Función de activación
Paso 3: a es la salida final
```

**Ejemplo con ReLU:**
```
Neurona:
Entrada: 10
Parámetros: peso = -2, bias = 5

Paso 1: z = (10 × -2) + 5 = -15
Paso 2: a = ReLU(-15) = max(0, -15) = 0    ← ReLU convierte negativos en 0
Paso 3: Salida = 0
```

### **¿Por qué se necesitan funciones de activación?**

**Sin activación:** Solo puedes aprender líneas rectas, sin importar cuántas capas tengas.

**Con activación:** Puedes aprender curvas y patrones complejos.

**Ejemplo que muestra el problema sin activación:**
```
Red con 2 capas SIN activación:

Capa 1: z₁ = x × 2 + 3
Capa 2: z₂ = z₁ × 4 + 1

Expandiendo:
z₂ = (x × 2 + 3) × 4 + 1
z₂ = x × 8 + 12 + 1
z₂ = x × 8 + 13  ← ¡Es solo una línea recta!

Conclusión: 2 capas sin activación = 1 capa simple
```

**Con activación:**
```
Red con 2 capas CON ReLU:

Capa 1: a₁ = ReLU(x × 2 + 3)
Capa 2: z₂ = a₁ × 4 + 1

Esto NO se puede reducir a una línea recta simple.
ReLU introduce un "quiebre" que permite curvas.
```

### **¿Cuáles son las funciones de activación principales?**

**1. ReLU (Rectified Linear Unit)** - La más usada
```
Fórmula: ReLU(z) = max(0, z)

Ejemplos:
ReLU(-5) = 0
ReLU(0) = 0
ReLU(3) = 3
ReLU(10) = 10

Comportamiento: Elimina valores negativos, mantiene positivos.
```

**2. Sigmoid**
```
Fórmula: sigmoid(z) = 1 / (1 + e^(-z))

Ejemplos aproximados:
sigmoid(-10) ≈ 0
sigmoid(0) = 0.5
sigmoid(10) ≈ 1

Comportamiento: Convierte cualquier número a rango [0, 1]
Útil para: Probabilidades
```

**3. SoftPlus**
```
Fórmula: softplus(z) = log(1 + e^z)

Comportamiento: Similar a ReLU pero suave (sin quiebres bruscos)
```

---

## **NIVEL 4: Capas y Arquitectura**

### **¿Qué es una capa?**

Una **capa** es un grupo de neuronas que:
- Trabajan en **paralelo** (al mismo tiempo)
- Están al mismo **nivel** en la red
- Todas reciben las **mismas entradas**

**Ejemplo:**
```
Capa con 3 neuronas:

Entrada: 25 (el mismo número va a las 3)

Neurona 1: (25 × 2) + 0 = 50
Neurona 2: (25 × -1) + 30 = 5      ← Las 3 calculan EN PARALELO
Neurona 3: (25 × 0.5) + 10 = 22.5

Salida de la capa: [50, 5, 22.5]
```

### **¿Por qué tener múltiples neuronas en una capa?**

Para obtener **múltiples perspectivas** del mismo dato.

**Ejemplo:**
```
Temperatura: 25°C (entrada)

Neurona 1 con peso = 4, bias = -50:
(25 × 4) - 50 = 50  ← "Detecta" temperaturas altas

Neurona 2 con peso = -3, bias = 80:
(25 × -3) + 80 = 5  ← "Detecta" temperaturas bajas

Ambas analizan la misma temperatura pero desde ángulos diferentes.
La siguiente capa puede combinar estas perspectivas: [50, 5]
```

**¿Por qué es importante?**

Si solo tuvieras una neurona produciendo un solo número, la siguiente capa tendría poca información para trabajar.

Con múltiples neuronas: [50, 5, 22] → la siguiente capa puede hacer combinaciones complejas.

### **¿Cómo fluye la información entre capas?**

El flujo es **secuencial**: Capa 1 → Capa 2 → Capa 3 → ...

**Reglas fundamentales:**
1. Cada capa **solo ve** las salidas de la capa inmediatamente anterior
2. La Capa 2 **NO ve** la entrada original, solo ve lo que produjo Capa 1
3. Dentro de una capa, las neuronas procesan en **paralelo**

**Ejemplo completo:**
```
Dataset: temperatura = 30°C
Red: 1 → 2 → 1 (1 entrada, 2 neuronas en capa 1, 1 neurona en capa 2)

CAPA 1 (recibe entrada original):
Neurona 1: (30 × 2) + 0 = 60      ← Procesa en paralelo
Neurona 2: (30 × -1) + 50 = 20    ← con Neurona 1
Salida de Capa 1: [60, 20]

CAPA 2 (recibe salidas de Capa 1):
Neurona 1: (60 × 0.5) + (20 × 0.8) + 5
         = 30 + 16 + 5 = 51
Salida final: 51

Nota: Capa 2 NUNCA vio los 30°C originales, solo vio [60, 20]
```

---

## **NIVEL 5: Procesamiento del Dataset**

### **¿Cómo procesa una neurona el dataset completo?**

**Respuesta directa:** Una neurona procesa **un punto a la vez**, pero eventualmente procesa **todos los puntos**.

**Ejemplo:**
```
Dataset: [20°C, 25°C, 30°C]
Neurona: peso = 2, bias = 5

MOMENTO 1: Procesa 20°C
z = (20 × 2) + 5 = 45
Salida para punto 1: 45

MOMENTO 2: Procesa 25°C
z = (25 × 2) + 5 = 55
Salida para punto 2: 55

MOMENTO 3: Procesa 30°C
z = (30 × 2) + 5 = 65
Salida para punto 3: 65

Resultado: La neurona transformó [20, 25, 30] en [45, 55, 65]
```

### **¿Qué sucede momento a momento con múltiples capas?**

**Ejemplo completo:**
```
Dataset: [20, 25]
Red: 1 → 2 → 1

════════════════════════════════════════
PROCESANDO PUNTO 1: x = 20
════════════════════════════════════════

CAPA 1:
Neurona 1: (20 × 2) + 5 = 45    ← EN PARALELO
Neurona 2: (20 × -1) + 30 = 10  ← EN PARALELO
Salidas de Capa 1: [45, 10]

CAPA 2 (recibe [45, 10]):
Neurona 1: (45 × 0.5) + (10 × 0.8) + 2 = 32.5
Predicción para punto 1: 32.5

════════════════════════════════════════
PROCESANDO PUNTO 2: x = 25
════════════════════════════════════════

CAPA 1:
Neurona 1: (25 × 2) + 5 = 55
Neurona 2: (25 × -1) + 30 = 5
Salidas de Capa 1: [55, 5]

CAPA 2 (recibe [55, 5]):
Neurona 1: (55 × 0.5) + (5 × 0.8) + 2 = 33.5
Predicción para punto 2: 33.5

════════════════════════════════════════
RESULTADO FINAL:
════════════════════════════════════════
Dataset de entrada: [20, 25]
Predicciones: [32.5, 33.5]
```

**Puntos clave:**
- Cada punto pasa por TODA la red antes del siguiente punto
- Dentro de cada capa, las neuronas trabajan en paralelo
- Entre capas, el flujo es secuencial

---

## **NIVEL 6: Entrenamiento vs Producción**

### **¿Cuál es la diferencia entre entrenamiento e inferencia?**

**ENTRENAMIENTO** (aprender):
- Tienes x e y (entrada y respuesta correcta)
- Calculas error = ŷ - y
- Ajustas pesos para reducir error
- Objetivo: mejorar la red

**INFERENCIA** (usar en producción):
- Solo tienes x (entrada)
- Calculas ŷ (predicción)
- NO hay error (no conoces y)
- Objetivo: hacer predicciones útiles

**Ejemplo:**
```
FASE 1: ENTRENAMIENTO (aprendiendo del pasado)
Dataset histórico:
20°C → 50 helados vendidos (conocido)
25°C → 100 helados vendidos (conocido)
30°C → 120 helados vendidos (conocido)

Red predice: 20°C → 48 (error: -2)
             25°C → 102 (error: +2)
             30°C → 118 (error: -2)

Ajusta pesos para reducir errores → Red mejora

FASE 2: PRODUCCIÓN (prediciendo el futuro)
Pregunta del negocio: Mañana habrá 27°C, ¿cuánto comprar?
Red predice: 27°C → 110 helados

Usas esta predicción para decisiones de compra.
NO puedes calcular error porque no sabes cuánto venderás realmente.
```

### **¿Cómo saber si la red funciona bien antes de usarla en producción?**

Usas **datos de validación**: datos históricos que apartas y no usas para entrenar.

**Ejemplo:**
```
Total de datos históricos: 100 días

DIVISIÓN:
80 días → Entrenamiento (la red aprende de estos)
20 días → Validación (la red NUNCA vio estos durante entrenamiento)

PROCESO:
1. Entrenas con 80 días
2. Pruebas con los 20 días de validación
3. Si funciona bien en validación → confías que funcionará con datos nuevos
4. Si funciona mal en validación → tu red no aprendió bien

Ejemplo:
Validación: 28°C → vendiste 115 (real)
Red predice: 28°C → 112 (predicción)
Error: -3 helados ← ¡Bastante bueno!
```

---

## **NIVEL 7: Overfitting (Sobreajuste)**

### **¿Qué es el overfitting?**

**Overfitting** ocurre cuando tu red **memoriza** el dataset de entrenamiento en lugar de **aprender** el patrón general.

**Ejemplo:**
```
RED CON OVERFITTING:
Error en entrenamiento: 0.1 ← ¡Casi perfecto!
Error en validación: 45.3 ← ¡Horrible!

Problema: Memorizó ejemplos específicos pero no generalizó el patrón.
```

### **¿Por qué pasa y cómo detectarlo?**

**Causa:** Demasiados parámetros para pocos datos, o entrenar demasiado tiempo.

**Detección:** Gran diferencia entre error de entrenamiento y validación.

**Progresión temporal:**
```
Época 50: Error entrenamiento: 5 | Error validación: 6 ✓ (balance óptimo)
Época 200: Error entrenamiento: 0.1 | Error validación: 45 ✗ (overfitting)
```

### **¿Cómo prevenirlo?**

1. **Más datos** (10,000 puntos vs 10 puntos)
2. **Red más simple** (menos parámetros)
3. **Early stopping** (parar cuando validación sube)
4. **Regularización** (penalizar pesos grandes)

**La validación es tu detector de overfitting.**

---

## **Resumen: De lo Básico a lo Complejo**

**1. Fundamentos:**
- x = entrada, y = verdad, ŷ = predicción
- Dataset = conjunto de pares (x, y)

**2. Una neurona:**
- Hace: z = (entradas × pesos) + bias
- Tiene tantos pesos como entradas recibe
- Siempre tiene 1 bias

**3. Activación:**
- Se aplica después: salida = activación(z)
- Permite aprender curvas, no solo líneas rectas
- Más común: ReLU

**4. Capas:**
- Grupo de neuronas en paralelo
- Múltiples neuronas = múltiples perspectivas
- Flujo entre capas es secuencial

**5. Procesamiento:**
- Cada neurona procesa todos los puntos del dataset
- En cada momento: procesa un punto
- Orden: punto 1 → toda la red → punto 2 → toda la red...

**6. Uso:**
- Entrenamiento: tienes x e y → ajustas pesos
- Producción: solo tienes x → haces predicción
- Validación: pruebas con datos que la red nunca vio

**7. Overfitting:**
- Memorizar vs aprender el patrón general
- Se detecta: error entrenamiento << error validación
- Se previene: más datos, red simple, early stopping, regularización
- Validación es el detector de overfitting

---

*Documento actualizado con explicaciones progresivas y ejemplos*