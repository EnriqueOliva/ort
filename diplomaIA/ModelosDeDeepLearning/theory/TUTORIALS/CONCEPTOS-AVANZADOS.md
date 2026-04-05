# CONCEPTOS AVANZADOS DE DEEP LEARNING

Este archivo explica conceptos fundamentales de deep learning de forma clara y conectada.

**Fuentes:** Transcripciones de clases 1, 5, 6 y 7 (2025)

---

## 1. DROPOUT

### ¿Qué es Dropout?

**Dropout** es una técnica de regularización que **apaga neuronas al azar** durante el entrenamiento para prevenir overfitting.

### ¿Cómo funciona?

Durante entrenamiento, cada neurona tiene probabilidad **p** de ser "apagada" (output = 0).

```
CAPA NORMAL (sin dropout):
Input: [2.5, 3.0, 1.8, 4.2]
       ↓
Output: [2.5, 3.0, 1.8, 4.2]  ← Todas las neuronas activas


CAPA CON DROPOUT (p = 0.2):
Input: [2.5, 3.0, 1.8, 4.2]
       ↓
Máscara aleatoria: [1, 1, 0, 1]  ← 20% probabilidad de 0
       ↓
Output: [2.5, 3.0, 0.0, 4.2]  ← Neurona 3 apagada
```

**En cada batch se genera una máscara diferente:**

```
Batch 1 - Máscara: [1, 1, 0, 1]  → Output: [2.5, 3.0, 0.0, 4.2]
Batch 2 - Máscara: [1, 0, 1, 1]  → Output: [2.5, 0.0, 1.8, 4.2]
Batch 3 - Máscara: [0, 1, 1, 1]  → Output: [0.0, 3.0, 1.8, 4.2]
```

---

### ¿Por qué previene overfitting?

**Analogía del profesor (Clase 6-06-10-2025):**

> "Si una empresa depende mucho de un solo proveedor, cuando ese proveedor falla, todo falla. Al forzar que los proveedores fallen aleatoriamente (dropout), la empresa aprende a distribuir la dependencia entre varios proveedores."

**En términos de la red:**

```
SIN DROPOUT - Una neurona depende MUCHO de pocas conexiones:

Neurona A:  w₁ = 150.0  ← Peso ENORME
            w₂ = 0.5
            w₃ = 0.2

Output = 150.0 × input₁ + 0.5 × input₂ + 0.2 × input₃
         ↑ Depende casi exclusivamente de input₁


CON DROPOUT - La neurona NO puede confiar en que input₁ esté siempre:

Neurona A después de entrenamiento:
            w₁ = 45.0   ← Peso más distribuido
            w₂ = 38.0
            w₃ = 32.0

Output = 45.0 × input₁ + 38.0 × input₂ + 32.0 × input₃
         ↑ Distribuido entre todas las entradas
```

**Resultado:** La red aprende representaciones más robustas y generales.

---

### Probabilidad de Dropout

**Valores típicos:** 0.1, 0.2, 0.3 (10%, 20%, 30% de neuronas apagadas)

```
p = 0.1:   Apaga 10% de neuronas  ← Dropout suave
p = 0.2:   Apaga 20% de neuronas  ← Común
p = 0.5:   Apaga 50% de neuronas  ← Dropout fuerte
```

**Regla práctica:**
- Capas pequeñas: p = 0.1 - 0.2
- Capas grandes (más propensas a overfitting): p = 0.3 - 0.5

Es un **hiperparámetro** que se ajusta en validation.

---

### Training vs Inference

**DURANTE ENTRENAMIENTO:**

```python
# Época 1, Batch 1
x = [3.0, 2.5, 4.0, 1.8]
mask = [1, 0, 1, 1]  ← Generada aleatoriamente
output = x * mask = [3.0, 0.0, 4.0, 1.8]

# Época 1, Batch 2
x = [3.0, 2.5, 4.0, 1.8]
mask = [1, 1, 0, 1]  ← NUEVA máscara aleatoria
output = x * mask = [3.0, 2.5, 0.0, 1.8]
```

**DURANTE INFERENCIA (test/producción):**

```python
# NO aplicamos dropout, PERO escalamos pesos

Si entrenamos con p = 0.2 (apagar 20%):
  - Durante entrenamiento: en promedio, 80% neuronas activas
  - Durante inferencia: 100% neuronas activas

Solución: Multiplicar pesos por 0.8

Ejemplo:
  Peso entrenado: w = 10.0
  Peso en inferencia: w × 0.8 = 8.0
```

**¿Por qué este escalado?**

```
DURANTE ENTRENAMIENTO (p=0.2):
Input = [5.0, 5.0, 5.0, 5.0, 5.0]  (5 neuronas)
Mask =  [1,   0,   1,   1,   0  ]  (20% apagadas)
Output después de capa: suma = 15.0  ← Solo 3 neuronas activas

DURANTE INFERENCIA:
Input = [5.0, 5.0, 5.0, 5.0, 5.0]  (5 neuronas)
Mask =  [1,   1,   1,   1,   1  ]  (todas activas)
Output sin escalar: suma = 25.0  ← ¡Valor diferente!

Output con escalar (×0.8): suma = 25.0 × 0.8 = 20.0  ← Más cercano

Promedio esperado durante training: 0.8 × 25.0 = 20.0  ✓
```

**Cita de la clase 6-06-10-2025:**
> "Al hacer inferencia, no hay máscaras. Hay que multiplicar los pesos entrenados por R (la probabilidad de que una unidad permaneciera activa). Esto escala correctamente porque durante el entrenamiento, los pesos se adaptaron a que las neuronas caían aleatoriamente."

---

### Efecto Ensemble

Dropout entrena **múltiples subredes** simultáneamente:

```
Red completa: 4 neuronas

Batch 1 - Máscara [1,1,0,1]: Subred A con neuronas {1,2,4}
Batch 2 - Máscara [1,0,1,1]: Subred B con neuronas {1,3,4}
Batch 3 - Máscara [0,1,1,1]: Subred C con neuronas {2,3,4}
...

Inferencia: Promedio (aproximado) de todas las subredes
```

**Resultado:** Reduce varianza, mejora generalización.

---

## 2. TRANSFER LEARNING VS ENTRENAMIENTO DESDE CERO

### ¿Qué es Transfer Learning?

Tomar una red **pre-entrenada** en un dataset grande, congelar las capas que ya aprendieron features útiles, y entrenar solo las capas finales para tu tarea específica.

### Comparación Detallada

```
┌──────────────────────────────────────────────────────────────┐
│ ENTRENAMIENTO DESDE CERO                                     │
└──────────────────────────────────────────────────────────────┘

Dataset: Tu dataset (ej: 5,000 imágenes de rostros)
         ↓
Inicialización: Pesos ALEATORIOS en TODAS las capas
         ↓
Entrenamiento: TODAS las capas se entrenan
         ↓
Resultado: Red aprende TODO desde cero
         - Capas iniciales: detectar bordes
         - Capas medias: detectar texturas, formas
         - Capas finales: detectar objetos completos

Parámetros a entrenar: 14,700,000  (TODOS)
Tiempo: 50-100 épocas
Datos necesarios: 50,000+ imágenes (idealmente)


┌──────────────────────────────────────────────────────────────┐
│ TRANSFER LEARNING                                            │
└──────────────────────────────────────────────────────────────┘

Modelo pre-entrenado: VGG16 entrenado en ImageNet
  - 1.2 millones de imágenes
  - 1,000 categorías
  - Capas Conv ya aprendieron features generales
         ↓
CONGELAR capas Conv (no entrenar)
         ↓
Tu dataset: 5,000 imágenes de rostros
         ↓
SOLO entrenar capas Dense finales (MLP)
         ↓
Resultado: Reutiliza features pre-aprendidas
         - Capas Conv (FROZEN): bordes, texturas
         - Capas Dense (TRAINED): clasificar rostros

Parámetros a entrenar: 500,000  (solo MLP)
Tiempo: 10-20 épocas
Datos necesarios: 2,000-5,000 imágenes
```

---

### Comparación Numérica Ejemplo

**Problema:** Clasificar 5 tipos de flores con 3,000 imágenes

**DESDE CERO:**

```
Arquitectura:
  Conv(3→32) → Conv(32→64) → Conv(64→128) → Flatten → Dense(512) → Dense(5)

Parámetros:
  Capa 1: 3×3×3×32 + 32 = 896
  Capa 2: 3×3×32×64 + 64 = 18,496
  Capa 3: 3×3×64×128 + 128 = 73,856
  Dense 1: (4×4×128)×512 + 512 = 1,049,088
  Dense 2: 512×5 + 5 = 2,565

  TOTAL: 1,144,901 parámetros a entrenar

Recursos:
  Épocas: 100
  Tiempo: 8 horas (GPU)
  Resultado con 3k imágenes: 75% accuracy (insuficientes datos)
```

**TRANSFER LEARNING (VGG16):**

```
Arquitectura:
  VGG16 Conv blocks (CONGELADAS) → Flatten → Dense(512) → Dense(5)
                                              ↑ ENTRENAR solo esto

Parámetros:
  VGG16 Conv: 14,714,688  ← CONGELADOS (no se entrenan)
  Dense 1: (7×7×512)×512 + 512 = 12,845,568
  Dense 2: 512×5 + 5 = 2,565

  TOTAL A ENTRENAR: 12,848,133  (solo capas Dense)

Recursos:
  Épocas: 15
  Tiempo: 1 hora (GPU)
  Resultado con 3k imágenes: 94% accuracy (features pre-aprendidas)
```

**Comparación:**

| Aspecto | Desde Cero | Transfer Learning |
|---------|------------|-------------------|
| **Parámetros totales** | 1.1M | 27.6M |
| **Parámetros a entrenar** | 1.1M (100%) | 12.8M (46%) |
| **Épocas** | 100 | 15 |
| **Tiempo** | 8 horas | 1 hora |
| **Accuracy (3k imgs)** | 75% | 94% |
| **Datos ideales** | 50k+ | 2k-5k |

---

### ¿Cuándo usar cada uno?

**TRANSFER LEARNING si:**
- Tienes **pocos datos** (< 10,000 imágenes)
- Tu tarea es **similar** al dominio pre-entrenado (ej: ImageNet → clasificar flores)
- Quieres resultados **rápidos**
- Recursos computacionales **limitados**

**Ejemplo:** Clasificar animales con 5,000 imágenes
- ImageNet ya tiene animales → features útiles
- Transfer Learning ✓

**DESDE CERO si:**
- Tienes **muchos datos** (> 100,000 imágenes)
- Tu tarea es **muy diferente** del dominio pre-entrenado
- Necesitas **arquitectura customizada**
- Tienes recursos computacionales **abundantes**

**Ejemplo:** Clasificar imágenes médicas de rayos X
- ImageNet no tiene rayos X → features menos útiles
- Mejor desde cero (o transfer learning de modelo médico pre-entrenado)

**Cita de la clase 6-06-10-2025:**
> "Si tu tarea es clasificación de rostros, agarrás una red convolucional grande pre-entrenada con muchos datos. Esa red ya aprendió buenos kernels para estudiar imágenes. Congelás esos bloques convolucionales (congelás todos los gradientes) y creás tu propio MLP arriba con la arquitectura que quieras. Entrenás solo ese MLP para clasificar rostros."

---

## 3. EMBEDDINGS

### ¿Qué son los Embeddings?

**Embeddings** son representaciones de items discretos (palabras, tokens) como **vectores continuos** en un espacio de alta dimensionalidad que preserva relaciones semánticas.

```
Palabra (discreto)  →  Vector continuo (embedding)

"gato"   →  [0.23, -0.45, 0.67, 0.12, ..., -0.89]  (300 dimensiones)
"perro"  →  [0.25, -0.43, 0.71, 0.15, ..., -0.85]  (300 dimensiones)
"auto"   →  [-0.67, 0.89, -0.12, 0.45, ..., 0.23]  (300 dimensiones)
```

---

### Propiedades de los Embeddings

**1. Similitud semántica = cercanía geométrica**

```
Palabras similares → vectores cercanos

"gato"  = [0.23, -0.45, 0.67]
"perro" = [0.25, -0.43, 0.71]
          ↑ Vectores cercanos (animales domésticos)

"auto"  = [-0.67, 0.89, -0.12]
          ↑ Vector lejano (no es animal)
```

**2. Direcciones significativas**

El ejemplo más famoso:

```
rey - hombre + mujer ≈ reina

Vector("rey") = [0.5, 0.8, 0.3, ...]
Vector("hombre") = [0.3, 0.2, 0.1, ...]
Vector("mujer") = [0.3, 0.2, 0.9, ...]

Vector("rey") - Vector("hombre") + Vector("mujer")
  = [0.2, 0.6, -0.6, ...] + [0.3, 0.2, 0.9, ...]
  = [0.5, 0.8, 1.1, ...]
  ≈ Vector("reina")
```

**Cita de la clase 1-18-08-2025:**
> "Existe una dirección tal que si te movés en esa dirección cambias el género de las palabras. 'King' menos 'man' más 'woman' aproximadamente igual a 'queen'. Hay direcciones para singular/plural, tiempos verbales, etc."

---

### ¿Cómo se aprenden? (Word2Vec ejemplo)

**Word2Vec (2013):** Primera técnica exitosa a gran escala

**Enfoque 1: CBOW (Continuous Bag of Words)**

```
Texto: "el gato come pescado fresco"

Ventana de 5 palabras:
  [el] [gato] [___] [pescado] [fresco]
           ↑
    Predecir palabra del centro

Entrada: ["el", "gato", "pescado", "fresco"]
         ↓
Red neuronal (embeddings + MLP)
         ↓
Salida: probabilidades para cada palabra
         {"come": 0.85, "bebe": 0.10, ...}
```

**Enfoque 2: Skip-gram**

```
Inverso: Dada palabra del centro, predecir contexto

Entrada: "come"
         ↓
Red neuronal
         ↓
Salida: probabilidades para palabras de contexto
         {"el": 0.3, "gato": 0.4, "pescado": 0.5, ...}
```

**No necesita etiquetas:** El mismo texto proporciona supervisión (self-supervised learning)

---

### Embeddings vs One-Hot Encoding

**ONE-HOT ENCODING:**

```
Vocabulario: ["gato", "perro", "come", "bebe", "agua"]  (5 palabras)

"gato"  → [1, 0, 0, 0, 0]
"perro" → [0, 1, 0, 0, 0]
"come"  → [0, 0, 1, 0, 0]
"bebe"  → [0, 0, 0, 1, 0]
"agua"  → [0, 0, 0, 0, 1]

Problemas:
  1. Dimensionalidad = tamaño vocabulario (10,000+ palabras = 10,000 dims)
  2. Vectores SPARSE (99.99% son ceros)
  3. NO captura similitud ("gato" y "perro" son ortogonales: distancia = √2)
  4. Ineficiente en memoria y cómputo
```

**EMBEDDINGS:**

```
Vocabulario: 10,000 palabras → Embeddings de 300 dimensiones

"gato"  → [0.23, -0.45, 0.67, ..., -0.89]  (300 dims)
"perro" → [0.25, -0.43, 0.71, ..., -0.85]  (300 dims)

Ventajas:
  1. Dimensionalidad FIJA (100-300 dims típicamente)
  2. Vectores DENSOS (todos valores significativos)
  3. CAPTURA similitud (distancia("gato", "perro") pequeña)
  4. Eficiente en memoria: 10,000 × 300 vs 10,000 × 10,000
```

**Comparación numérica:**

```
Vocabulario: 50,000 palabras

ONE-HOT:
  Dimensiones: 50,000
  Memoria por palabra: 50,000 × 4 bytes = 200 KB
  Memoria total: 50,000 × 200 KB = 10 GB
  Sparse: 99.998% son ceros

EMBEDDINGS (300 dims):
  Dimensiones: 300
  Memoria por palabra: 300 × 4 bytes = 1.2 KB
  Memoria total: 50,000 × 1.2 KB = 60 MB  ← 166× menos
  Dense: todos valores útiles
```

**Cita de la clase 1-18-08-2025:**
> "One-hot encoding es super ineficiente. Crea vectores extremadamente sparse con un solo 1 y muchos 0s. Desperdicia memoria y recursos computacionales."

---

### Visualización de Embeddings

```
ESPACIO 2D SIMPLIFICADO (real: 300D)

      felino
        ↑
  gato  ·  león
        |
────────┼──────── comida
        |
 perro  ·  lobo
        ↓
      canino

Palabras relacionadas están cerca en el espacio vectorial.
Distancia = similitud semántica.
```

---

## 4. DOCUMENT TERM MATRIX (DTM)

### ¿Qué es una Document Term Matrix?

Una **matriz** donde:
- **Filas** = Documentos
- **Columnas** = Palabras (términos) del vocabulario
- **Valores** = Frecuencia de cada palabra en cada documento

```
         gato  perro  come  bebe  agua
Doc 1:    2     0     1     0     1
Doc 2:    0     3     1     2     0
Doc 3:    1     1     0     1     2

Documento 1: "el gato come. el gato bebe agua"
  → gato: 2, come: 1, agua: 1

Documento 2: "el perro come. el perro bebe. el perro juega"
  → perro: 3, come: 1, bebe: 2

Documento 3: "el gato y el perro beben agua. beben agua"
  → gato: 1, perro: 1, bebe: 1, agua: 2
```

---

### Variantes de DTM

**1. Frecuencia simple (count):**

```
Valor = número de veces que palabra aparece en documento
```

**2. Binaria:**

```
Valor = 1 si palabra aparece, 0 si no
```

**3. TF-IDF (Term Frequency - Inverse Document Frequency):**

```
TF-IDF(palabra, doc) = TF(palabra, doc) × IDF(palabra)

TF(palabra, doc) = frecuencia(palabra, doc) / total_palabras(doc)
IDF(palabra) = log(total_docs / docs_que_contienen_palabra)

Intuición:
  - Palabras comunes (en muchos docs) → IDF bajo
  - Palabras raras (en pocos docs) → IDF alto
  - Da más peso a palabras distintivas
```

**Ejemplo:**

```
3 documentos:
Doc 1: "el gato come pescado"
Doc 2: "el perro come carne"
Doc 3: "el gato bebe agua"

Palabra "el": aparece en 3/3 docs → IDF = log(3/3) = 0 (no distintiva)
Palabra "gato": aparece en 2/3 docs → IDF = log(3/2) = 0.18
Palabra "pescado": aparece en 1/3 docs → IDF = log(3/1) = 0.48 (distintiva)

TF-IDF("pescado", Doc1) = (1/4) × 0.48 = 0.12  ← Alto
TF-IDF("el", Doc1) = (1/4) × 0 = 0  ← Palabra común, valor bajo
```

---

### Problemas de Document Term Matrix

**1. ALTA DIMENSIONALIDAD Y SPARSITY**

```
Vocabulario real: 50,000 palabras
Documentos: 10,000

Matriz: 10,000 × 50,000 = 500 millones de celdas
Sparse: 99%+ son ceros (cada doc usa ~500 palabras diferentes)
```

**2. NO CAPTURA SEMÁNTICA**

```
Documentos similares pueden tener DTM muy diferentes:

Doc A: "el gato está sentado"
Doc B: "el felino está sentado"

DTM:
         gato  felino  está  sentado
Doc A:    1      0      1      1
Doc B:    0      1      1      1

Distancia = √2  ← "gato" y "felino" parecen completamente diferentes
```

**3. PÉRDIDA DE ORDEN**

```
"el perro muerde al gato"
"el gato muerde al perro"

→ MISMA representación DTM (bag of words)
→ Significados OPUESTOS
```

**4. PALABRAS FUERA DE VOCABULARIO (OOV)**

```
Vocabulario: ["gato", "perro", "come"]

Nueva palabra "león" → ¿cómo representarla?
→ NO está en la matriz
→ Requiere reentrenar todo
```

---

### DTM vs Embeddings: Comparación

```
┌────────────────────────────────────────────────────────┐
│ DOCUMENT TERM MATRIX (DTM)                             │
└────────────────────────────────────────────────────────┘

Representación: Sparse matrix (10,000 docs × 50,000 palabras)
Dimensiones: 50,000 (tamaño vocabulario)
Valores: Frecuencias o TF-IDF
Semántica: NO captura ("gato" ≠ "felino")
Orden: NO preserva
Memoria: 500M celdas (99% ceros)
Adaptable: NO (palabras nuevas requieren reconstruir matriz)


┌────────────────────────────────────────────────────────┐
│ EMBEDDINGS (Word2Vec, BERT, etc.)                      │
└────────────────────────────────────────────────────────┘

Representación: Dense vectors (cada palabra = vector)
Dimensiones: 300-768 (fijo, independiente del vocabulario)
Valores: Números continuos aprendidos
Semántica: SÍ captura (distancia("gato", "felino") pequeña)
Orden: Con modelos contextuales (BERT) SÍ preserva
Memoria: 50,000 palabras × 300 dims = 15M valores útiles
Adaptable: SÍ (embeddings nuevos sin reentrenar todo)
```

---

### Evolución histórica

```
1. DOCUMENT TERM MATRIX (1960s-2000s)
   ↓
   Problemas: sparse, no semántica, alta dimensionalidad

2. WORD EMBEDDINGS (2013+)
   Word2Vec, GloVe
   ↓
   Mejora: dense, captura semántica, baja dimensionalidad
   Problema: una palabra = un embedding (sin contexto)

3. CONTEXTUAL EMBEDDINGS (2018+)
   BERT, GPT, Transformers
   ↓
   Mejora: mismo palabra tiene diferentes embeddings según contexto

   Ejemplo:
     "el banco del río" → banco₁ = [0.2, 0.5, ...]  (geográfico)
     "el banco del dinero" → banco₂ = [0.8, -0.3, ...]  (financiero)
```

---

### Cuándo usar cada uno

**DTM + TF-IDF:**
- Clasificación de documentos simple
- Sistemas legacy
- Baseline rápido
- Cuando semántica no es crítica

**Embeddings:**
- NLP moderno
- Búsqueda semántica
- Similitud de textos
- Cuando importa significado
- Tareas con contexto

---

## RESUMEN COMPARATIVO

| Concepto | Qué hace | Para qué sirve |
|----------|----------|----------------|
| **Dropout** | Apaga neuronas al azar (p%) | Prevenir overfitting, distribuir pesos |
| **Transfer Learning** | Congela conv pre-entrenadas, entrena MLP | Menos datos, menos tiempo, mejores resultados |
| **Embeddings** | Vectores densos continuos | Representar palabras capturando semántica |
| **DTM** | Matriz sparse frecuencias | Representación clásica texto (obsoleta) |

---

**Fuentes:**
- Clase 1-18-08-2025: Embeddings, representación de datos
- Clase 5-29-09-2025: One-hot encoding, clasificación
- Clase 6-06-10-2025: Dropout, Transfer Learning, regularización
- Clase 7-13-10-2025: Arquitecturas, fine-tuning
