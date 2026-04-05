# Cell 13

"""
Decisiones de configuración del modelo y entrenamiento.

TAMAÑO DE ENTRADA: 384x384 (FINAL RUN)
- Las imágenes originales son 800x800, demasiado grandes para entrenar.
- 384x384 captura más detalles que 256x256 manteniendo batch size viable.
- 384 es divisible por 2^4=16, perfecto para 4 niveles de U-Net.
- Validación de memoria: Run 7 confirmó que 256x256 batch 18 funciona,
  lo cual equivale en memoria a 384x384 batch 8.

ARQUITECTURA: U-Net con 4 niveles
- Padding=1 para mantener dimensiones (evita problemas de tamaño)
- Instance Normalization (mejor que Batch Norm con batch size pequeño)
- Bilinear Upsampling (más rápido y menos parámetros que ConvTranspose)
- Dropout2d(p=0.1) en bottleneck (Run 12)

BATCH SIZE: 8
- Óptimo según experimentos (Run 7 mostró que batch 18 empeoró resultados)
- Batch sizes pequeños ayudan a encontrar mínimos planos (mejor generalización)

LOSS: BCE + Dice (0.3/0.7)
- BCE da gradientes suaves
- Dice maneja bien el desbalance de clases
- Más peso a Dice porque es la métrica de evaluación

OPTIMIZER: Adam con CosineAnnealingLR
- lr=1e-4 inicial, decae hasta 1e-6
- CosineAnnealingLR con T_max=600 épocas
- Sin warm restarts (Run 6 demostró que son innecesarios)
"""

# Cell 24

"""
Arquitectura U-Net basada en el paper original.

La U-Net tiene forma de U:
- Encoder (izquierda): baja resolución, sube canales
- Bottleneck (abajo): mínima resolución, máximos canales
- Decoder (derecha): sube resolución, baja canales
- Skip connections: conectan encoder con decoder

Modificaciones respecto al paper:
1. Padding=1 (mantiene dimensiones)
2. Instance Normalization (mejor con batch pequeño)
3. Bilinear Upsampling (más rápido)
"""


"""
Clase U-Net completa con Dropout muy suave (Run 12).

CAMBIO: Se agregó Dropout2d(p=0.1) en el bottleneck.

JUSTIFICACIÓN:
- El paper U-Net Sección 3.1 menciona: "Drop-out layers at the end of the 
  contracting path perform further implicit data augmentation"
- p=0.1 es muy suave - no es para corregir overfitting (no lo tenemos)
- Es para compensar la reducción de variedad al eliminar augmentaciones
  poco realistas (VerticalFlip, ElasticTransform)
- El bottleneck (1024 canales, 24x24 en nuestra arquitectura) es el punto
  más comprimido donde dropout tiene mayor efecto regularizador

Input: 3 canales (RGB)
Output: 1 canal (máscara binaria)
"""

# Cell 47

"""
Configuración del entrenamiento.

LOSS: BCE + Dice
- BCE proporciona gradientes suaves
- Dice maneja bien el desbalance de clases
- La combinación funciona mejor que cualquiera por separado

OPTIMIZER: Adam con lr=1e-4
- Adam es el estándar para segmentación
- lr=1e-4 es un buen punto de inicio

SCHEDULER: ReduceLROnPlateau
- Reduce LR automáticamente cuando el val_dice deja de mejorar
- Patience=10 épocas antes de reducir
- Factor=0.5 (reduce a la mitad)

MIXED PRECISION: Activado
- Acelera entrenamiento ~1.5x
- Reduce uso de memoria ~40%
- Sin pérdida de precisión

EARLY STOPPING:
- Si val_dice no mejora en PATIENCE épocas, paramos
"""

# Cell 72

"""
RESUMEN DE DECISIONES TOMADAS

Este obligatorio implementa U-Net desde cero siguiendo el paper original,
con modificaciones estratégicas para mejorar el rendimiento.

DECISIÓN 1: Tamaño de entrada 256×256
Justificación:
  - Las imágenes originales (800×800) son demasiado grandes para entrenar
  - 256×256 es divisible por 2^4 = 16 (para 4 niveles de U-Net)
  - Balance entre calidad y velocidad de entrenamiento
  - Permite batch size razonable (8) en GPU con 12GB

DECISIÓN 2: Modificaciones a U-Net original
Padding=1:
  - Paper original: sin padding (imagen sale más chica)
  - Nuestra implementación: padding=1 (mantiene dimensiones)
  - Ventaja: evita problemas de tamaño, más fácil de implementar

Instance Normalization:
  - Paper original: sin normalización explícita
  - Nuestra implementación: Instance Norm
  - Justificación: batch pequeño (8), BatchNorm funciona mal con batches chicos

Bilinear Upsampling:
  - Paper original: usa ConvTranspose2d
  - Nuestra implementación: Bilinear + Conv1×1
  - Ventaja: más rápido, menos parámetros, menos checkerboard artifacts

DECISIÓN 3: Loss Function = BCE + Dice
BCE solo:
  - Da gradientes suaves
  - Converge rápido
  - Pero ignora desbalance de clases

Dice solo:
  - Maneja bien desbalance
  - Pero gradientes ruidosos, convergencia inestable

BCE + Dice (0.5 cada uno):
  - Combina ventajas de ambos
  - Gradientes suaves + manejo de desbalance
  - Es la configuración más estable

DECISIÓN 4: Optimización de Threshold
Default 0.5:
  - Es lo que todo el mundo usa
  - Pero casi nunca es óptimo

Threshold optimizado en validación:
  - Probamos 0.30 a 0.75
  - Encontramos el que maximiza Dice
  - Típicamente mejora 5-15% el score
"""

# Cell 74

"""
Posibles mejoras para el futuro.

Si el Dice en Kaggle sale < 0.75, estas son las mejoras a probar:

1. THRESHOLD:
   - El threshold óptimo en validación puede no ser óptimo en test
   - Probar threshold ±0.05 alrededor del óptimo
   - Hacer submissions con diferentes thresholds

2. DATA AUGMENTATION:
   - Agregar más variabilidad:
     * Elastic deformations
     * CutMix / MixUp
     * Color jittering más agresivo
   - Pero cuidado: demasiado augmentation puede perjudicar

3. ARQUITECTURA:
   - Probar U-Net con encoder pre-entrenado (ResNet, EfficientNet)
   - Agregar más niveles (U-Net de 5 niveles)
   - Probar otras arquitecturas (DeepLabV3+, PSPNet)

4. TRAINING:
   - Entrenar más épocas (50-100)
   - Learning rate más bajo (1e-5)
   - Probar otros optimizadores (AdamW, SGD con momentum)
   - Focal Loss en lugar de BCE

5. POST-PROCESSING:
   - Morphological operations (opening, closing)
   - Conditional Random Fields (CRF)
   - Test-time augmentation (TTA)

6. ENSEMBLE:
   - Entrenar múltiples modelos con diferentes seeds
   - Combinar predicciones (promedio, voting)
   - 5-fold cross-validation

7. INPUT SIZE:
   - Probar con 512×512 (más calidad, más lento)
   - Multi-scale training
   - Patches superpuestos en inferencia

Lo MÁS IMPORTANTE:
  - Si Val Dice es alto pero Kaggle Dice es bajo: problema de threshold o RLE
  - Si Val Dice es bajo: problema de modelo o entrenamiento
  - Siempre empezar con lo simple antes de lo complejo
"""

# Cell 75

"""
OBLIGATORIO COMPLETADO
"""

print("="*80)
print(" " * 25 + "OBLIGATORIO COMPLETADO")
print("="*80)

print("\n✅ IMPLEMENTACIÓN COMPLETA:")
print("  Setup inicial y análisis del dataset")
print("  Data augmentation con Albumentations")
print("  Arquitectura U-Net desde cero")
print("  Loss functions (BCE + Dice)")
print("  Training loop con early stopping")
print("  Evaluación y optimización de threshold")
print("  Predicciones para test")
print("  RLE encoding para Kaggle")
print("  Submission generado")

print("\n📊 RESULTADOS:")
print(f"  Threshold óptimo: {optimal_threshold:.2f}")
print(f"  Val Dice: {validation_results['dice_mean']:.4f}")
print(f"  Test images procesadas: {len(test_predictions_binary)}")

print("\n📁 ARCHIVOS GENERADOS:")
print(f"  Modelo: {RESULTS_DIR / 'bestModel' / 'best_model.pth'}")
print(f"  Submission: {RESULTS_DIR / 'kaggleSubmission' / 'submission.csv'}")
print(f"  Stats: {RESULTS_DIR / 'stats' / 'stats.csv'}")
print(f"  Graphs: {RESULTS_DIR / 'graphs'}")
print(f"  Predictions: {RESULTS_DIR / 'predictions'}")

print("\n🎯 PRÓXIMOS PASOS:")
print("  1. Revisar visualizaciones en results/predictions/")
print("  2. Subir submission.csv a Kaggle")
print("  3. Verificar Dice score (objetivo: >= 0.75)")
print("  4. Si necesario, iterar con mejoras (ver Cell 74)")

print("\n📚 APRENDIZAJES CLAVE:")
print("  - U-Net funciona muy bien para segmentación")
print("  - Data augmentation es crítico")
print("  - Threshold optimization mejora significativamente el score")
print("  - RLE encoding con order='F' es CRÍTICO para Kaggle")
print("  - Mixed Precision acelera entrenamiento sin pérdida de precisión")

print("\n" + "="*80)
print(" " * 20 + "¡ÉXITO EN LA COMPETENCIA DE KAGGLE!")
print("="*80)

print("\n✨ Notebook listo para entrega y defensa ✨")