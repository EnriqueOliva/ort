# RESPUESTAS A PREGUNTAS - GUÍA DE REFERENCIA RÁPIDA

Este archivo responde exclusivamente las preguntas de `/home/enrique/2doSemestre/ModelosDeDeepLearning/preguntasArealizar.txt`

---

## 1. FUNCIONES DE PÉRDIDA (LOSS FUNCTIONS)

### Binary Cross-Entropy (BCE)

**¿Qué es?**
- Función de pérdida para CLASIFICACIÓN BINARIA (2 clases)

**Fórmula:**
```
Loss = -[y·log(ŷ) + (1-y)·log(1-ŷ)]

y  = Etiqueta real (0 o 1)
ŷ  = Probabilidad predicha (0 a 1)
```

**Ejemplo:**
```
Problema: ¿Es spam?
Etiqueta real: y = 1 (sí es spam)
Red predice: ŷ = 0.9 (90% segura)

Loss = -log(0.9) = 0.105 (error pequeño)

Si hubiera predicho ŷ = 0.1:
Loss = -log(0.1) = 2.30 (error grande, penaliza mucho)
```

**Cuándo usarla:**
- Problemas binarios: spam/no spam, perro/gato, sí/no
- Última capa: 1 neurona con activación Sigmoid
- Output: Número entre 0 y 1

---

### Categorical Cross-Entropy (CCE)

**¿Qué es?**
- Función de pérdida para CLASIFICACIÓN MULTICLASE
- Las clases son mutuamente excluyentes (solo UNA correcta)

**Fórmula:**
```
Loss = -Σ(y_i · log(ŷ_i))

y  = Vector one-hot [0,0,1,0,0]
ŷ  = Vector de probabilidades
```

**Ejemplo:**
```
CIFAR-10: 5 clases [car, bus, truck, motor, person]

Etiqueta real: truck
y = [0, 0, 1, 0, 0]  ← One-hot

Predicción:
ŷ = [0.1, 0.05, 0.7, 0.1, 0.05]

Loss = -log(0.7) = 0.357

Solo importa la probabilidad de la clase correcta (truck=0.7)
```

**Cuándo usarla:**
- Clasificación multiclase: CIFAR-10, ImageNet, dígitos
- Última capa: N neuronas con activación Softmax
- Output: N probabilidades que suman 1

---

### Mean Squared Error (MSE)

**¿Qué es?**
- Función de pérdida para REGRESIÓN
- Predecir valores numéricos continuos

**Fórmula:**
```
Loss = (1/N) · Σ(y_i - ŷ_i)²

Promedio del error al cuadrado
```

**Ejemplo:**
```
Predecir precio de casa:
Valor real: y = $200,000
Predicción: ŷ = $195,000

Error: (200,000 - 195,000)² = 25,000,000

Si hubiera predicho $150,000:
Error: (200,000 - 150,000)² = 2,500,000,000
       ↑
    Penaliza MUCHO más los errores grandes (al cuadrado)
```

**Cuándo usarla:**
- Regresión: predecir precios, temperaturas, edades, coordenadas
- Última capa: 1 neurona (o N valores) SIN activación final
- Output: Números reales

---

### Mean Absolute Error (MAE)

**¿Qué es?**
- Función de pérdida para REGRESIÓN
- Menos sensible a outliers que MSE

**Fórmula:**
```
Loss = (1/N) · Σ|y_i - ŷ_i|

Promedio del error absoluto (sin elevar al cuadrado)
```

**Diferencia con MSE:**
```
Error = $10,000
MSE penaliza: 10,000² = 100,000,000
MAE penaliza: |10,000| = 10,000

Error = $100,000
MSE penaliza: 100,000² = 10,000,000,000  ← MUCHO más
MAE penaliza: |100,000| = 100,000

MSE castiga DESPROPORCIONADAMENTE los errores grandes
MAE castiga proporcionalmente
```

**Cuándo usarla:**
- Regresión cuando hay outliers
- Ejemplo: predecir edad (personas muy viejas no deben distorsionar)
- Cuando quieres penalizar linealmente (no exponencialmente)

---

### Resumen de Funciones de Pérdida

| Función | Tipo | Última Capa | Output | Cuándo |
|---------|------|-------------|--------|--------|
| **BCE** | Clasificación binaria | 1 + Sigmoid | [0.9] | ¿Es perro? |
| **CCE** | Clasificación multiclase | N + Softmax | [0.1,0.7,0.2] | CIFAR-10 |
| **MSE** | Regresión | N (sin activación) | [195340.5] | Precio |
| **MAE** | Regresión (outliers) | N (sin activación) | [32.5] | Edad |

---

## 2. ARQUITECTURAS DE REDES

### MLP (Multilayer Perceptron)

**¿Qué es?**
- Red completamente conectada (Fully Connected)
- SOLO capas Dense

**Estructura:**
```
Input (vector 1D) → Dense → ReLU → Dense → ReLU → Dense → Softmax
```

**Ejemplo (MNIST):**
```
Input:    784 números (28×28 píxeles aplanados)
  ↓
Dense:    512 neuronas
ReLU
  ↓
Dense:    256 neuronas
ReLU
  ↓
Dense:    10 neuronas (dígitos 0-9)
Softmax
```

**Cómo reconocerla:**
- SOLO Dense layers (Fully Connected)
- NO tiene Conv2D ni Pooling
- Input es 1D (vector aplanado)
- Todas las neuronas conectadas entre capas

**Cuándo usarla:**
- Datos tabulares: edad, salario, características numéricas
- Problemas simples donde no importa estructura espacial

**Desventajas para imágenes:**
- MUCHOS parámetros (millones)
- Pierde estructura espacial (no sabe que píxeles vecinos están relacionados)

---

### CNN (Convolutional Neural Network)

**¿Qué es?**
- Red con capas convolucionales
- Diseñada para imágenes

**Estructura:**
```
Input (imagen 3D) → [Conv2D → ReLU → MaxPool] × N → Flatten → Dense → Softmax
```

**Ejemplo (CIFAR-10):**
```
Input:      (32, 32, 3)
  ↓
Conv2D:     32 filtros → (32, 32, 32)
ReLU
MaxPool:    → (16, 16, 32)
  ↓
Conv2D:     64 filtros → (16, 16, 64)
ReLU
MaxPool:    → (8, 8, 64)
  ↓
Flatten:    → 4096
Dense:      → 512
ReLU
Dense:      → 10
Softmax
```

**Cómo reconocerla:**
- Tiene Conv2D layers
- Tiene MaxPooling o AvgPooling
- Input es 3D (altura × ancho × canales)
- Dimensiones espaciales se REDUCEN (32→16→8)
- Número de canales AUMENTA (3→32→64)

**Cuándo usarla:**
- Clasificación de imágenes
- Detección de objetos
- Segmentación de imágenes
- Cualquier dato con estructura espacial 2D

**Ventajas:**
- 100-300× MENOS parámetros que MLP para imágenes
- Respeta estructura espacial
- Invarianza a traslaciones

---

### RNN (Recurrent Neural Network)

**¿Qué es?**
- Red con memoria para SECUENCIAS
- Procesa datos uno por uno, mantiene estado

**Estructura:**
```
x₁ → [RNN] → h₁
      ↓     (memoria)
x₂ → [RNN] → h₂
      ↓
x₃ → [RNN] → h₃ → Output
```

**Ejemplo (predecir siguiente palabra):**
```
Secuencia: "El perro está ___"

x₁="El"    → RNN → h₁ (recuerda "El")
x₂="perro" → RNN → h₂ (recuerda "El perro")
x₃="está"  → RNN → h₃ (recuerda todo)
                 ↓
            Predice: "ladrando"
```

**Cómo reconocerla:**
- Capas RNN, LSTM, o GRU
- Input es secuencia 2D (tiempo × features)
- Tiene "estados ocultos" que se pasan entre pasos
- Flechas que apuntan hacia atrás (recurrencia)

**Cuándo usarla:**
- Procesamiento de lenguaje: traducción, chatbots
- Series temporales: predecir precio de acciones, clima
- Generación de texto/música
- Cualquier dato secuencial

**Variantes:**
- **LSTM** (Long Short-Term Memory): Mejor memoria largo plazo
- **GRU** (Gated Recurrent Unit): Más simple que LSTM, similar rendimiento

---

### Transformer

**¿Qué es?**
- Arquitectura basada en "Attention"
- NO usa recurrencia, procesa todo en paralelo

**Estructura:**
```
Input → Embedding → Positional Encoding
  ↓
[Multi-Head Attention → Feed Forward] × N layers
  ↓
Output
```

**Cómo reconocerla:**
- Capas de "Attention" o "Multi-Head Attention"
- NO tiene RNN/LSTM
- Tiene "Positional Encoding"
- Procesa toda la secuencia simultáneamente

**Cuándo usarla:**
- NLP moderno: GPT, BERT, Claude
- Traducción automática
- Generación de texto
- Cualquier tarea que antes usaba RNN

**Ventajas sobre RNN:**
- Mucho más RÁPIDO (paralelizable)
- Mejor en secuencias largas
- Captura relaciones a larga distancia

---

### ResNet (Residual Network)

**¿Qué es?**
- CNN con "skip connections"
- Permite redes MUY profundas (50-200 capas)

**Estructura:**
```
x → [Conv → ReLU → Conv] → ⊕ → ReLU
↓__________________________|
   Skip connection (suma x + output)
```

**Cómo reconocerla:**
- Es una CNN
- Tiene skip connections (flechas que saltan capas)
- Símbolo ⊕ (suma de tensores)
- Bloques residuales repetidos

**Cuándo usarla:**
- Clasificación de imágenes complejas (ImageNet)
- Cuando necesitas red muy profunda
- Transfer learning (pre-entrenada en ImageNet)

**Por qué funciona:**
- Skip connections ayudan a que gradientes fluyan
- Evita "vanishing gradient" en redes profundas

---

### U-Net

**¿Qué es?**
- CNN en forma de "U"
- Diseñada para SEGMENTACIÓN

**Estructura:**
```
        Encoder (reduce)    Decoder (expande)
Input → Conv → Pool → ... → UpConv → Conv → Output
         ↓___________________|
           Skip connection
```

**Cómo reconocerla:**
- Forma simétrica de U
- Encoder: reduce tamaño espacial
- Decoder: aumenta tamaño espacial (upsampling)
- Skip connections horizontales entre encoder y decoder
- Output tiene MISMO tamaño que input

**Cuándo usarla:**
- Segmentación de imágenes médicas
- Segmentación semántica
- Cuando output debe tener mismo tamaño que input
- Necesitas localización precisa

---

### Resumen de Arquitecturas

| Arquitectura | Input | Componentes Clave | Uso |
|--------------|-------|-------------------|-----|
| **MLP** | 1D vector | Solo Dense | Datos tabulares |
| **CNN** | 3D imagen | Conv2D + Pool | Imágenes |
| **RNN/LSTM** | 2D secuencia | Recurrencia | Series temporales, NLP |
| **Transformer** | 2D secuencia | Attention | NLP moderno |
| **ResNet** | 3D imagen | CNN + Skip | Clasificación profunda |
| **U-Net** | 3D imagen | Encoder-Decoder | Segmentación |

---

## 3. TIPOS DE PROBLEMAS

### Clasificación Binaria

**¿Qué predice?**
- Entre 2 clases: sí/no, 0/1, verdadero/falso

**Ejemplos:**
- ¿Es spam? (sí/no)
- ¿Tiene cáncer? (sí/no)
- ¿Es perro? (perro/no-perro)

**Última capa:**
```
Dense(1, activation='sigmoid')
Output: [0.87]  → 87% probabilidad de clase 1

Si > 0.5 → Clase 1
Si ≤ 0.5 → Clase 0
```

**Loss:** Binary Cross-Entropy

**Cómo reconocerlo:**
- 1 sola neurona de salida
- Activación Sigmoid
- Output es UN número entre 0 y 1

---

### Clasificación Multiclase

**¿Qué predice?**
- Entre 3+ clases MUTUAMENTE EXCLUYENTES
- Un ejemplo pertenece a UNA sola clase

**Ejemplos:**
- CIFAR-10: [car, bus, truck, motor, person] (una imagen es UNA cosa)
- Dígitos: [0,1,2,3,4,5,6,7,8,9] (un dígito es UN número)
- Clasificar flor: [rosa, tulipán, girasol] (una flor es UNA especie)

**Última capa:**
```
Dense(5, activation='softmax')
Output: [0.1, 0.05, 0.7, 0.1, 0.05]  → Suman 1.0
         car  bus  truck motor person
                    ↑
              70% → Es truck
```

**Loss:** Categorical Cross-Entropy

**Cómo reconocerlo:**
- N neuronas de salida (una por clase)
- Activación Softmax
- Output suma 1.0
- Solo UNA clase es correcta

---

### Clasificación Multilabel

**¿Qué predice?**
- Múltiples clases SIMULTÁNEAMENTE
- Un ejemplo puede tener VARIAS etiquetas

**Ejemplos:**
- Etiquetar foto: [perro, gato, persona, coche] (puede tener varios)
- Clasificar película: [comedia, drama, acción] (puede ser varias)
- Tags de artículo: [python, machine-learning, tutorial]

**Última capa:**
```
Dense(4, activation='sigmoid')  ← Sigmoid, NO Softmax
Output: [0.9, 0.05, 0.85, 0.1]  → NO suman 1.0
        perro gato persona coche

Interpretación:
perro=0.9   → SÍ (>0.5)
gato=0.05   → NO (<0.5)
persona=0.85 → SÍ (>0.5)
coche=0.1   → NO (<0.5)

Resultado: ["perro", "persona"]
```

**Loss:** Binary Cross-Entropy (aplicada a CADA neurona independientemente)

**Cómo reconocerlo:**
- N neuronas de salida
- Activación Sigmoid (NO Softmax)
- Outputs NO suman 1.0
- Múltiples clases pueden ser verdaderas simultáneamente

**Diferencia clave:**
```
Multiclase (Softmax):  [0.7, 0.2, 0.1] → Solo UNA clase
Multilabel (Sigmoid):  [0.9, 0.05, 0.85] → Múltiples clases
```

---

### Regresión

**¿Qué predice?**
- Valores NUMÉRICOS CONTINUOS (no categorías)

**Ejemplos:**
- Predecir precio de casa: $195,340.50
- Predecir temperatura: 25.3°C
- Predecir edad: 32.5 años
- Predecir coordenadas: (45.2, -122.8)

**Última capa:**
```
Dense(1)  # Sin activación (o ReLU si solo valores positivos)
Output: [195340.5]  → Número real

O para múltiples valores:
Dense(3)
Output: [25.3, 15.8, 1013.2]
        temp  humedad presión
```

**Loss:** MSE o MAE

**Cómo reconocerlo:**
- 1+ neuronas de salida
- SIN activación (linear) o ReLU si solo positivos
- Output es número(s) real(es)
- No hay clases, solo valores continuos

**Variantes:**
- **Regresión simple:** Predecir 1 valor
- **Regresión múltiple:** Predecir N valores simultáneamente

---

### Segmentación

**¿Qué predice?**
- Clase de CADA PÍXEL en imagen
- Output tiene mismo tamaño espacial que input

**Ejemplos:**
- Segmentación semántica: etiquetar cada píxel (cielo, calle, árbol)
- Segmentación médica: delimitar tumor en imagen
- Separar fondo de primer plano

**Entrada y salida:**
```
Input:  (256, 256, 3)  ← Imagen RGB
Output: (256, 256, N)  ← MISMO tamaño espacial
         ↑        ↑
         |        └─ N clases (cielo, calle, árbol)
         └───────── Cada píxel clasificado

Ejemplo para un píxel:
Píxel (100, 50) → [0.1, 0.8, 0.1] → Clase "calle" (mayor prob)
```

**Arquitectura típica:**
- U-Net o FCN (Fully Convolutional Network)

**Loss:** Categorical Cross-Entropy aplicada píxel por píxel

**Cómo reconocerlo:**
- Output tiene MISMAS dimensiones espaciales que input
- Clasificación densa (cada píxel)
- Arquitectura encoder-decoder

---

### Detección de Objetos

**¿Qué predice?**
- MÚLTIPLES objetos en imagen
- Para cada objeto: clase + ubicación (bounding box)

**Ejemplos:**
- YOLO, Faster R-CNN
- Detectar todos los objetos en foto de calle

**Output:**
```
Lista de objetos detectados:
[
  {clase: "perro",   bbox: (50,60,200,300),  confianza: 0.95},
  {clase: "gato",    bbox: (400,100,600,400), confianza: 0.88},
  {clase: "persona", bbox: (10,20,100,500),   confianza: 0.92}
]

bbox = (x, y, ancho, alto) del rectángulo
```

**Arquitecturas típicas:**
- YOLO (You Only Look Once)
- Faster R-CNN
- SSD (Single Shot Detector)

**Loss:** Múltiples (clasificación + regresión de coordenadas)

**Cómo reconocerlo:**
- Output incluye coordenadas de bounding boxes
- Múltiples objetos por imagen
- Clasificación + localización simultáneas

---

### Resumen de Tipos de Problemas

| Tipo | Output | Activación | Loss | Ejemplo |
|------|--------|------------|------|---------|
| **Binaria** | 1 número | Sigmoid | BCE | ¿Spam? |
| **Multiclase** | N probabilidades (suman 1) | Softmax | CCE | CIFAR-10 |
| **Multilabel** | N probabilidades (independientes) | Sigmoid×N | BCE×N | Tags foto |
| **Regresión** | 1+ números reales | None/ReLU | MSE/MAE | Precio |
| **Segmentación** | (H,W,N) - clase por píxel | Softmax | CCE×píxel | Máscara |
| **Detección** | Lista objetos+boxes | Múltiple | Múltiple | YOLO |

---

## 4. TIPOS DE CAPAS

### Capas de Procesamiento

#### Conv2D (Convolutional 2D)

**¿Qué hace?**
- Aplica filtros para detectar patrones en imágenes

**Parámetros:**
- SÍ (los números de los filtros se aprenden)

**Entrada/Salida:**
```
Entrada: (N, H, W, C_in)
Salida:  (N, H', W', C_out)

H' y W' pueden cambiar según padding
C_out = número de filtros
```

**Ejemplo:**
```
Conv2D(64 filtros, kernel=3×3, padding='same')
Entrada: (N, 32, 32, 3)
Salida:  (N, 32, 32, 64)  ← 64 feature maps
```

**Uso:** Detectar patrones (líneas, bordes, formas, objetos)

---

#### MaxPooling

**¿Qué hace?**
- Reduce dimensiones espaciales
- Toma el MÁXIMO en ventanas (típicamente 2×2)

**Parámetros:**
- NO (solo toma máximo, no aprende)

**Entrada/Salida:**
```
Entrada: (N, H, W, C)
Salida:  (N, H/2, W/2, C)

Reduce espacial a la mitad
NO cambia número de canales
```

**Ejemplo:**
```
MaxPool(2×2)
Entrada: (N, 32, 32, 64)
Salida:  (N, 16, 16, 64)  ← Mismo # canales
```

**Uso:** Reducir tamaño, aumentar robustez

---

#### Dense / Fully Connected

**¿Qué hace?**
- Cada neurona de salida conectada a TODAS las entradas
- Igual que en MLPs

**Parámetros:**
- SÍ (muchos: input_size × output_size + output_size)

**Entrada/Salida:**
```
Entrada: (N, X)  ← Vector
Salida:  (N, Y)  ← Y neuronas

Parámetros = X×Y + Y
```

**Ejemplo:**
```
Dense(512)
Entrada: (N, 2048)
Salida:  (N, 512)

Parámetros: 2048×512 + 512 = 1,049,088
```

**Uso:** Clasificación final, capas intermedias

---

#### Flatten

**¿Qué hace?**
- Convierte tensor 3D/4D en vector 1D
- NO es realmente una "capa", es operación

**Parámetros:**
- NO

**Entrada/Salida:**
```
Entrada: (N, H, W, C)
Salida:  (N, H×W×C)

Ejemplo:
Entrada: (N, 4, 4, 128)
Salida:  (N, 2048)  ← 4×4×128=2048
```

**Uso:** Conectar CNNs con Dense layers

---

### Capas de Activación

#### ReLU (Rectified Linear Unit)

**¿Qué hace?**
- Deja pasar positivos sin cambios
- Convierte negativos a 0

**Fórmula:**
```
ReLU(x) = max(0, x)
```

**Uso:** Después de Conv2D y Dense

**Propiedades:**
- No lineal (permite aprender patrones complejos)
- Simple y rápida
- NO cambia dimensiones

---

#### Softmax

**¿Qué hace?**
- Convierte números en probabilidades que suman 1

**Uso:** SOLO al final para clasificación multiclase

**Propiedades:**
- Output suma 1.0
- Todas las salidas están entre 0 y 1

---

#### Sigmoid

**¿Qué hace?**
- Convierte números a rango 0-1

**Uso:**
- Clasificación binaria (última capa)
- Clasificación multilabel (cada salida independiente)

**Propiedades:**
- Output entre 0 y 1 (pero NO necesariamente suman 1)

---

### Capas de Regularización

#### Dropout

**¿Qué hace?**
- Apaga neuronas al AZAR durante entrenamiento
- Probabilidad p de apagar cada neurona

**Parámetros:**
- NO (solo el hiperparámetro p)

**Uso:** Evitar overfitting

**Comportamiento:**
```
Entrenamiento: Apaga neuronas al azar
Inferencia: Todas activas (ajusta pesos por p)
```

---

#### BatchNormalization

**¿Qué hace?**
- Normaliza activaciones en cada batch
- Media=0, varianza=1 por feature

**Parámetros:**
- SÍ (pocos: escala γ y shift β por feature)

**Uso:**
- Acelerar entrenamiento
- Estabilizar aprendizaje
- Permite learning rates más altos

---

### Resumen de Capas

| Capa | Parámetros | Cambia Dimensiones | Uso Principal |
|------|------------|-------------------|---------------|
| **Conv2D** | SÍ (filtros) | Canales aumentan | Detectar patrones |
| **MaxPool** | NO | Espacial reduce | Reducir tamaño |
| **Dense** | SÍ (muchos) | Cualquiera | Clasificación |
| **Flatten** | NO | 3D→1D | Conectar CNN→Dense |
| **ReLU** | NO | No cambia | Activación |
| **Softmax** | NO | No cambia | Clasificación final |
| **Dropout** | NO | No cambia | Regularización |
| **BatchNorm** | SÍ (pocos) | No cambia | Estabilizar |

---

## FUENTES

Este archivo responde las preguntas de:
- `/home/enrique/2doSemestre/ModelosDeDeepLearning/preguntasArealizar.txt`

Basado en material de las clases:
- `/home/enrique/2doSemestre/ModelosDeDeepLearning/6-06-10-2025/6-06-10-2025.txt`
- `/home/enrique/2doSemestre/ModelosDeDeepLearning/7-13-10-2025/7-13-10-2025.txt`
