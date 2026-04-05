Proce# Plan de Implementación - Obligatorio U-Net

## 📊 RESUMEN DEL OBLIGATORIO

**Objetivo**: Implementar U-Net desde cero en PyTorch para segmentación de personas en imágenes (como crear stickers de WhatsApp).

**Entregables**:
- 1 notebook .ipynb auto-contenido
- Participación en competencia Kaggle (mínimo Dice 0.75)
- Defensa oral el 3/12/2025

**Dataset**: 2,133 imágenes de entrenamiento (800×800), todas cuadradas, con máscaras binarias.

---

## 🎯 PLAN DE IMPLEMENTACIÓN

### **ESTRUCTURA DEL NOTEBOOK** (usando 80 celdas pre-creadas)

#### **SECCIÓN 1: Setup Inicial** (Celdas 1-4) ✅
```
Cell 1: Imports y configuración del entorno
Cell 2: Device setup, verificación CUDA, seeds
Cell 3: Creación de directorios (logs/, models/, results/)
Cell 4: Funciones auxiliares de visualización
```

#### **SECCIÓN 2: Descarga y Análisis del Dataset** (Celdas 5-12) ✅
```
Cell 5: Obtener IDs de las imágenes
Cell 6: Verificar dimensiones y tipos de datos
Cell 7: Visualizar muestras y guardar en logs/
Cell 8: Estadísticas básicas del dataset
Cell 9: Análisis de balance de clases (% píxeles foreground/background)
Cell 10: Distribución de tamaños de objetos (histograma)
Cell 11: Visualización de casos extremos
Cell 12: Guardar análisis en logs/dataset_analysis.json
```

#### **SECCIÓN 3: Configuración e Hiperparámetros** (Celdas 13-15) ✅
```
Cell 13: Explicación de decisiones de configuración
Cell 14: Hiperparámetros centralizados (LR, epochs, etc.)
Cell 15: Crear diccionario CONFIG para guardar en logs
```

#### **SECCIÓN 4: Data Augmentation** (Celdas 16-19) ✅
```
Cell 16: Setup Albumentations transforms
Cell 17: Test de transformaciones
Cell 18: Visualizar ejemplos de augmentation aplicado a imagen+máscara
Cell 19: Verificar que máscaras se augmentan correctamente (valores binarios)
```

#### **SECCIÓN 5: Dataset Class** (Celdas 20-23) ✅
```
Cell 20: Clase SegmentationDataset
Cell 21: Test del dataset con muestras
Cell 22: Verificar shapes y rangos de valores con DataLoader
Cell 23: Visualizar batch de entrenamiento
```

#### **SECCIÓN 6: Arquitectura U-Net** (Celdas 24-33) ✅
```
Cell 24: Explicación arquitectura U-Net
Cell 25: Módulo DoubleConv (2 conv + InstanceNorm + ReLU)
Cell 26: Módulo Down (MaxPool + DoubleConv)
Cell 27: Módulo Up (Upsample + Conv1x1 + Concatenate + DoubleConv)
Cell 28: Clase UNet completa
Cell 29: Instanciar modelo y mover a GPU
Cell 30: Model summary (parámetros totales)
Cell 31: Test forward pass con tensor dummy
Cell 32: Contar parámetros por capa
Cell 33: Guardar arquitectura en logs/model_architecture.txt
```

#### **SECCIÓN 7: Loss Functions y Métricas** (Celdas 34-37)
```
Cell 34: Implementar DiceLoss
Cell 35: Implementar BCEDiceLoss (combinación)
Cell 36: Función para calcular Dice coefficient (métrica)
Cell 37: Test de las funciones de loss
```

#### **SECCIÓN 8: Training Utilities** (Celdas 38-42)
```
Cell 38: Función train_epoch con progress bar de 1 línea
Cell 39: Función validate_epoch
Cell 40: Función para guardar modelo
Cell 41: Función para graficar training curves
Cell 42: Test de funciones con 1 iteración
```

#### **SECCIÓN 9: Preparación de Datos** (Celdas 43-46)
```
Cell 43: Train/val split (80/20)
Cell 44: Crear DataLoaders
Cell 45: Verificar tamaños de datasets
Cell 46: Visualizar 1 batch final
```

#### **SECCIÓN 10: Entrenamiento** (Celdas 47-53)
```
Cell 47: Configuración de entrenamiento (explicación)
Cell 48: Crear optimizador (Adam, LR=1e-4)
Cell 49: Crear scheduler (ReduceLROnPlateau)
Cell 50: Setup Mixed Precision (AMP)
Cell 51: Training loop principal con logging a archivo
Cell 52: Guardar modelo cada N épocas
Cell 53: Graficar y guardar curvas de training
```

#### **SECCIÓN 11: Evaluación en Validación** (Celdas 54-60)
```
Cell 54: Cargar mejor modelo
Cell 55: Optimización de threshold (probar 0.3-0.7)
Cell 56: Evaluar con threshold óptimo
Cell 57: Calcular Dice por imagen y estadísticas
Cell 58: Visualizar mejores/peores predicciones
Cell 59: Guardar predicciones en logs/predictions/
Cell 60: Guardar métricas en logs/validation_results.json
```

#### **SECCIÓN 12: Predicciones para Test** (Celdas 61-65)
```
Cell 61: Cargar imágenes de test
Cell 62: Generar predicciones en 256×256
Cell 63: Resize predicciones a 800×800 (tamaño original)
Cell 64: Aplicar threshold óptimo
Cell 65: Guardar máscaras predichas
```

#### **SECCIÓN 13: RLE Encoding para Kaggle** (Celdas 66-71)
```
Cell 66: Implementar mask2rle con order='F' ⚠️ CRÍTICO
Cell 67: Implementar rle2mask para testing
Cell 68: Test round-trip en varias máscaras
Cell 69: Generar RLE para todas las predicciones de test
Cell 70: Crear CSV de submission
Cell 71: Guardar en results/submission.csv
```

#### **SECCIÓN 14: Resumen Final** (Celdas 72-75)
```
Cell 72: Resumen de decisiones tomadas
Cell 73: Métricas finales (Dice train/val, threshold óptimo)
Cell 74: Decisiones de arquitectura justificadas
Cell 75: Próximos pasos para mejorar
```

---

## 🔑 DECISIONES TÉCNICAS CLAVE

### **1. Tamaño de Imagen: 256×256**
**Justificación**:
- Divisible por 2^4 = 16 (para 4 niveles de U-Net)
- Balance entre calidad y velocidad de entrenamiento
- Permite batch size razonable (4-8)
- Evita las 10+ horas que tomaría con 800×800

### **2. Arquitectura U-Net**
```
Encoder (Contracting Path):
- Input: 256×256×3 → DoubleConv → 256×256×64
- Down1: MaxPool → 128×128×64 → DoubleConv → 128×128×128
- Down2: MaxPool → 64×64×128 → DoubleConv → 64×64×256
- Down3: MaxPool → 32×32×256 → DoubleConv → 32×32×512

Bottleneck:
- Down4: MaxPool → 16×16×512 → DoubleConv → 16×16×1024

Decoder (Expansive Path):
- Up1: Upsample+Conv → 32×32×512 + Skip → DoubleConv → 32×32×512
- Up2: Upsample+Conv → 64×64×256 + Skip → DoubleConv → 64×64×256
- Up3: Upsample+Conv → 128×128×128 + Skip → DoubleConv → 128×128×128
- Up4: Upsample+Conv → 256×256×64 + Skip → DoubleConv → 256×256×64

Output:
- Conv1×1 → 256×256×1 → Sigmoid
```

**Modificaciones respecto al paper original**:
- ✅ Padding=1 (evita reducción de tamaño)
- ✅ Instance Normalization (mejor para batch pequeño)
- ✅ Bilinear Upsampling + Conv1×1 (más rápido, menos parámetros)

### **3. Entrenamiento**
- **Loss**: BCE + Dice (estabilidad + manejo de desbalance)
- **Optimizer**: Adam (lr=1e-4)
- **Scheduler**: ReduceLROnPlateau (patience=5, factor=0.5)
- **Batch Size**: 4-8 (según memoria disponible)
- **Epochs**: 30-50 (dependiendo de convergencia)
- **Mixed Precision**: ✅ (AMP para 1.5× speedup)

### **4. Data Augmentation** (Albumentations)
```python
HorizontalFlip(p=0.5)
VerticalFlip(p=0.3)
ShiftScaleRotate(shift=0.1, scale=0.2, rotate=30, p=0.5)
RandomBrightnessContrast(p=0.3)
GaussNoise(p=0.2)
```

### **5. Estrategia de Evaluación**
- Optimizar threshold en validación (probar 0.3-0.7)
- Dice coefficient como métrica principal
- Visualizar predicciones constantemente

### **6. RLE Encoding** ⚠️ CRÍTICO
```python
# DEBE usar order='F' (Fortran/column-major)
pixels = img.flatten(order='F')  # NO usar img.flatten()
```

---

## 📁 ESTRUCTURA DE ARCHIVOS GENERADOS

```
lab/
├── obligatorio.ipynb (el notebook principal)
├── logs/
│   ├── dataset_analysis.json
│   ├── config.json
│   ├── model_architecture.txt
│   ├── model_info.json
│   ├── training_history.json
│   ├── training_curves.png
│   ├── validation_results.json
│   ├── foreground_distribution.png
│   ├── augmentation_samples/
│   └── predictions/
├── models/
│   ├── best_model.pth
│   └── checkpoint_epoch_X.pth
└── results/
    └── submission.csv
```

**Ventaja**: Todos los resultados guardados en archivos permiten análisis sin problemas de outputs largos del notebook.

---

## 🎨 ESTILO DEL NOTEBOOK

### **Textos explicativos** (en español, informal):
```python
"""
Acá vamos a cargar el dataset de Kaggle.
Las imágenes son de 800×800 pero vamos a redimensionarlas a 256×256
porque si no tarda años en entrenar.
"""
```

### **Progress de entrenamiento** (1 línea actualizable):
```python
# En lugar de:
# Epoch 1/50 - Loss: 0.5
# Epoch 2/50 - Loss: 0.4
# ...

# Usar:
print(f"\rÉpoca {epoch}/{epochs} | Loss: {loss:.4f} | Dice: {dice:.4f}", end="")
```

---

## ⚠️ PUNTOS CRÍTICOS A VIGILAR

1. **RLE Encoding**: DEBE usar `order='F'` - error silencioso que destruye el score
2. **Threshold Optimization**: 0.5 raramente es óptimo
3. **Máscaras en Augmentation**: Usar `interpolation=cv2.INTER_NEAREST`
4. **Resize a 800×800**: Antes de generar RLE para Kaggle
5. **model.eval()**: Antes de inference (BatchNorm/Dropout)
6. **Visualización constante**: Para detectar errores en pipeline

---

## 🚀 FLUJO DE TRABAJO PROPUESTO

### **Sesión 1**: Implementar hasta SECCIÓN 6 (arquitectura) ✅
- ✅ Verificar que dataset carga correctamente
- ✅ Verificar que modelo compila y hace forward pass

### **Sesión 2**: Implementar SECCIÓN 7-10 (training)
- Entrenar 5-10 épocas para verificar que funciona
- Ajustar batch size según memoria

### **Sesión 3**: SECCIÓN 11-13 (evaluación y submission)
- Optimizar threshold
- Generar submission
- Primera subida a Kaggle

### **Iteraciones**: Mejorar según resultados
- Ajustar augmentation
- Probar diferentes loss functions
- Aumentar épocas si está mejorando

---

## 📊 EXPECTATIVAS REALISTAS

- **Primera submission**: Dice ~0.70-0.80 (objetivo: pasar 0.75)
- **Con optimizaciones**: Dice ~0.85-0.90
- **Tiempo de training**: 2-4 horas (30 épocas, 256×256, batch=4)

---

## 📝 ESTADO ACTUAL

### ✅ Completado (Sesión 1):
- [x] Sección 1: Setup Inicial (Celdas 1-4)
- [x] Sección 2: Análisis del Dataset (Celdas 5-12)
- [x] Sección 3: Configuración (Celdas 13-15)
- [x] Sección 4: Data Augmentation (Celdas 16-19)
- [x] Sección 5: Dataset Class (Celdas 20-23)
- [x] Sección 6: U-Net Architecture (Celdas 24-33)

### ✅ Completado (Sesión 2):
- [x] Sección 7: Loss Functions y Métricas (Celdas 34-37)
- [x] Sección 8: Training Utilities (Celdas 38-42)
- [x] Sección 9: Preparación de Datos (Celdas 43-46)
- [x] Sección 10: Entrenamiento (Celdas 47-53)

### ✅ Completado (Sesión 3):
- [x] Sección 11: Evaluación en Validación (Celdas 54-60)
- [x] Sección 12: Predicciones para Test (Celdas 61-65)
- [x] Sección 13: RLE Encoding para Kaggle (Celdas 66-71)
- [x] Sección 14: Resumen Final (Celdas 72-75)

---

## 🔍 VERIFICACIONES IMPORTANTES

### Antes de entrenar:
- ✅ Dataset carga correctamente
- ✅ Máscaras mantienen valores binarios después de augmentation
- ✅ Forward pass del modelo funciona
- ✅ Shapes son correctos en todo el pipeline
- ✅ Modelo está en GPU

### Durante entrenamiento:
- [ ] Loss disminuye consistentemente
- [ ] Dice aumenta en train y val
- [ ] No hay overfitting severo
- [ ] GPU se está usando (nvidia-smi)

### Antes de submission:
- [ ] Threshold optimizado en validación
- [ ] RLE encoding testeado con round-trip
- [ ] Predicciones de test tienen el tamaño correcto (800×800)
- [ ] CSV tiene formato correcto para Kaggle

---

## 📚 REFERENCIAS CLAVE

- **Paper Original**: U-Net: Convolutional Networks for Biomedical Image Segmentation (2015)
- **Transcripción de clase**: `8-22-10-2025.txt`
- **Research**: `research.md` - Guía práctica de implementación
- **Obligatorio**: `obligatorio.txt` - Requisitos oficiales

---

**Última actualización**: ✅ TODAS LAS SESIONES COMPLETADAS (1, 2, 3)
**Próximo paso**: Entrenar el modelo ejecutando las celdas 1-53, luego ejecutar 54-75 para evaluar y generar submission
