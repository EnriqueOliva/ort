### Configuración general

- Notebook optimizada para ser corrida localmente en Windows 11. En particular se utilizó VsCode y una PC con capacidad de procesamiento considerable (i5-13600K, NVidia RTX 4070 12Gb, 64Gb DDR4).
- Se estableció una semilla (SEED = 42) para asegurar reproducibilidad. 42 como valor estándar ya trabajado.
- Localmente se almacena el mejor modelo (el modelo de la época en la que el mean val dice fue mayor), el archivo para subir como predicción a Kaggle, y gráficas para entender el desarrollo del entrenamiento. También se almacena predicciones (5 mejores y 10 peores imágenes) para entender fortalezas pero sobre todo debilidades del modelo. Esto ayudó a entender qué imágenes le estaba costando más al modelo y cómo atacar particularmente estos casos de mayor dificultad. Mejorar los peores casos contribuye directamente a un mejor mean dice en validación.
- Hiperparámetros se pusieron en esta primera sección para tenerlos al alcance y no tener que buscarlos en la notebook. Explicados más adelante en las secciones de implementación y entrenamiento del modelo.

### Análisis del dataset

- Se verificó que todas las imágenes fueran 800x800 como indica el obligatorio.
- Se visualizaron 6 muestras aleatorias del dataset para entender la variabilidad. Esto da una idea de cómo es el dataset y qué procesamientos puede llegar a requerir.
- Se analizó la distribución de foreground/background sobre 200 máscaras aleatorias. Estadísticas obtenidas: promedio 38.4%, mediana 36.6%, mínimo 1.04%, máximo 93.71%. Este desbalance de clases justifica usar Dice Loss en lugar de solo BCE, ya que BCE penaliza cada píxel igual e incentivaría predecir todo como fondo.
- Se visualizaron los casos extremos (mínimo y máximo foreground) para entender los límites del dataset. Personas muy chicas en la imagen vs personas que ocupan casi toda la imagen. Esto ayudó a entender la variabilidad que el modelo debe manejar.

### Procesamiento del dataset

- Se usa Albumentations para transformaciones y data augmentation. Albumentations tiene una funcionalidad útil y es que aplica la misma transformación a imagen y máscara automáticamente.
    - Esta versión final de data augmentation es el resultado de muchas iteraciones y muchas pruebas.
    - En general, se usó como guía las conclusiones derivadas del survey de augmentation (Xu et al., 2022) (https://arxiv.org/pdf/2405.09591)
    - Imágenes redimensionadas de 800x800 a 384x384. Resolución más chica para que entre en memoria, pero no tan chica como para perder detalle en bordes. En primeras iteraciones se usó 256x256, y al aumentar a 384x384 hubo una mejora en la performance del modelo.
    - Se aplicó HorizontalFlip. Una persona mirando a la izquierda es igual de válida que una mirando a la derecha.
    - Rotación limitada a 15 grados. El paper de U-Net usa hasta 30 para células que pueden estar en cualquier orientación. El survey indica que "the angle of rotation should be carefully considered to ensure the preservation of appropriate labels". Según lo que se aprecia visualmente en el dataset, las personas tienen orientación natural vertical en su gran mayoría.
    - No se usa ElasticTransform. El paper de U-Net lo usa porque el tejido biológico se deforma naturalmente. El survey lo describe como transformación que "can alter the shape or posture of an object". Los cuerpos humanos son estructuras rígidas, no tiene sentido deformarlos.
    - Variaciones de iluminación (RandomBrightnessContrast, CLAHE, RandomGamma). El dataset tiene fotos con condiciones de luz muy distintas, el modelo debe aprender a manejarlas.
    - Variaciones de color (HueSaturationValue, ColorJitter, ToGray). Fuerza al modelo a aprender formas y no solo "píxeles color piel = persona".
    - GaussNoise con probabilidad baja (3%). Se usa con baja probabilidad porque el dataset son fotos de buena calidad.
    - Normalización con media y desviación estándar de ImageNet (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]). Centra los valores de entrada en ~0 con std ~1, en teoría debería estabilizar los gradientes y acelerar la convergencia.
- Se visualizan ejemplos de augmentation para verificar que las transformaciones se ven realistas y que imagen y máscara están alineadas.
- Clase SegmentationDataset custom que carga imagen y máscara, aplica transformaciones, y las devuelve como tensores.
- Se testea el Dataset y DataLoader con un batch para verificar que todo funciona antes de entrenar.
- Se visualiza un batch completo para confirmar que las imágenes y máscaras se ven correctas después de todo el pipeline.
- Split 80% train, 20% validación. Validación se usa para elegir el mejor modelo y optimizar threshold.

### Implementación del modelo

- Arquitectura U-Net siguiendo el paper original.
    - 4 niveles de encoder: 64→128→256→512→1024 canales.
    - 4 niveles de decoder con skip connections por concatenación (no suma). La concatenación preserva la información de bajo nivel del encoder.
    - DoubleConv: dos bloques de Conv 3x3 + InstanceNorm + ReLU.
    - Padding=1 en las convoluciones para mantener las dimensiones espaciales. Si bien esto es una diferencia deliverada con el paper, el cual no usa padding, simplifica las skip connections porque no hay que hacer crop.
    - ConvTranspose2d para upsampling en el decoder.
    - Dropout (p=0.1) aplicado solo en el bottleneck. Regularización en el punto de máxima compresión. Se probó con dropout 0.25, 0.20 y 0.15, pero en todos los casos el mejor mean val dice parecía no llegar al 0.9555 obtenido con dropout 0.1.
- InstanceNorm en lugar de BatchNorm. Con batch size chico (8), BatchNorm tiene estadísticas ruidosas. InstanceNorm calcula estadísticas por imagen individual, funciona igual con cualquier batch size.
- Función de pérdida BCEDiceLoss combinada.
    - BCE aporta gradientes estables pero es sensible al desbalance de clases.
    - Dice Loss optimiza directamente la métrica de Kaggle y es invariante al desbalance.
    - Pesos: BCE 0.3, Dice 0.7. Se le da más peso a Dice porque es la métrica de evaluación. Inicialmente se usó BCE 0.5, Dice 0.5 pero cambiar a BCE 0.3, Dice 0.7 dio mejor resultado.
- Dice Coefficient como métrica de evaluación (no como loss). Es lo que usa Kaggle para rankear.
- Se usó Mixed Precision Training (AMP) con autocast y GradScaler. Reduce uso de memoria ~50% y acelera el entrenamiento. Esto no se vio en clase en sí, pero sí comentamos en la primera clase acerca del uso de float16 y float32 y sus implicancias. Esta nueva técnica se investigó por cuenta apropia para poder entrenar con mayor resolución porque cuando se usó imágenes más grandes en los últimos entrenamientos llevaba demasiado tiempo. Incluso con esta adición varios entrenamientos tomaron cerca de 20 horas o más.
- Optimizador Adam. Se probó AdamW, obteniendo los mismos resultados. No se probó con otros por considerar que Adam siempre funcionó bien. "No arreglar lo que no está roto".
- Scheduler CosineAnnealingLR. Decae el learning rate suavemente siguiendo una curva coseno hasta un mínimo de 1e-6. Se probó CosineAnnealingWarmRestarts pero los reinicios eran muy agresivos y el modelo terminaba sufriendo demasiado esas caídas. No pareció brindar ningún beneficio.
- Funciones de entrenamiento y validación por época que retornan loss y dice promedio.
- Sistema de checkpoints que guarda el mejor modelo según validación.
- Early stopping implementado pero desactivado en la versión final. En los últimos entrenamientos se observaron mejoras de desempeño que tomaban muchas épocas, haciendo que el ES fuera contraproducente.

### Entrenamiento del modelo

- Respecto a la duración del entrenamiento:
  - En esta versión final se entrenó durante 600 épocas.
  - Se entrenó múltiples veces utilizando distintos valores, 20 entrenamientos registrados en Wandb (algunos entrenamientos adicionales se descartaron por constatar errores que en esencia invalidaban la corrida)
  - Se observó que con la implementación actual, el modelo ya alcanzaba muy buenos valores de mean val dice a las 40 - 50 épocas, superando valores de 0.90.
  - Se llegó a entrenar hasta 770 épocas solo para ver hasta qué techo llegaba el modelo. La ganancia en desempeño empieza a ser extremadamente marginal a partir de las 150 épocas aproximadamente.
  - Entrenamientos de de 100 - 120 épocas tomaban 2 horas al principio bajo las primeras condiciones experimentales. Luego 600 épocas tomaron 16 horas bajo las condiciones actuales. Otros más largos de 700, 700 épocas tomaron más de 20 horas.
  - Se entiende tras esta experimentación exhaustiva de épocas que el modelo ya alcanzó bajo estas condiciones el techo teórico de lo que puede lograr la Unet, o se está muy cerca de alcanzarlo, porque en todos los casos se alcanzaron valores de 0.95 mean val dice.
- Se intentó seguir en la mayor medida de lo posible la metodología de cambiar solo una cosa a la vez. De lo contrario, si se prueban varios cambios en una misma corrida, no va a ser posible qué cambios fueron los que hicieron mejorar o empeorar al modelo.
- Batch size 8. Se probó batch size 16 y 18, pero dieron peor resultado. Parecería que batches más chicos introducen ruido que actúa como regularización implícita.
- En cada época se calcula loss y dice promedio tanto para train como para validación.
- Se guarda el mejor modelo según mean val dice. Así al final del entrenamiento tenemos el mejor modelo, no necesariamente el de la última época.
- Se visualizan las curvas de entrenamiento (loss y dice para train/val) para verificar que no hay overfitting y que el modelo está aprendiendo correctamente.
- Entrenamientos registrados en Wandb (hubo más pero se descartaron por no aportar información relevante):
    - Dry run de 2 épocas
    - Entrenamiento 1. 35 Épocas
    - Entrenamiento 2. 70 Épocas, ES en 61 Épocas
    - Entrenamiento 3. CosineAnnealingWarmRestarts, 100 Épocas
    - Entrenamiento 4. Loss weights ajustados pero los warm restarts de CosineAnnealingLR triggerearon el early stopping por error.
    - Entrenamiento 5. Loss weights ajustados, sin early stopping. 120 Épocas
    - Entrenamiento 6. Eliminamos los warm restarts del LR.
    - Entrenamiento 7. Se aumentó batch size de 8 a 18 para probar memoria para futura corrida con imágenes más grandes (Entrenamiento 9)
    - Entrenamiento 8. Revierto batch size a 8 y agrego dropout 0.2 solo para ver qué pasa. No tenía justificación real para hacerlo.
    - Entrenamiento 9. Aumento tamaño imágenes a 384x384. 400 épocas
    - Entrenamiento 10. Pruebo Tversky Focal Loss en corrida corta de 120 épocas para ver si introduce mejoras
    - Entrenamiento 11. Revierto Tversky Focal Loss y pruebo eliminar el data augmentation
    - Entrenamiento 12. Reintroduzco data augmentation pero con mejoras significativas. 600 épocas interrumpidas por error a las 570. Este fue el entrenamiento de mejores resultados.
    - Entrenamiento 13. Hago más ajustes al data augmentation y elevo el LR en 2da mitad del entrenamiento
    - Entrenamiento 14. Reduje a la mitad LR mínimo e implementé aún más mejoras a data augmentation
    - Entrenamiento 15. Revertí LR mínimo al usado anteriormente, aumenté dropout a 0.25 y refactoricé data augmentation. Abortada manualmente
    - Entrenamiento 16. Refactoricé data augmentation, reduje dropout a 0.15 y añadí ES.
    - Entrenamiento 17. Revertí a data augmentation de la mejor run (Run 12), aumenté LR y cambié Adam a AdamW. Sufrí Gradient Explosion
    - Entrenamiento 18. Mismas condiciones que Entrenamiento 12 (mejores resultados) pero con AdamW. Abortado por no ver cambios y por falta de tiempo.
    - Entrenamiento 19. Mismas condiciones que Entrenamiento 12 pero con AdamW y estrategia de LR diferente. Abortado a las 770 épocas por no ver cambios.
    - Entrenamiento 20. Repetición del Entrenamiento 12 (mejores resultados) pero se aplicará TTA luego del entrenamiento

### Evaluación del modelo

- Se carga el mejor modelo guardado durante el entrenamiento (el de mejor mean val dice, no el de la última época).
- Test-Time Augmentation (TTA) con HorizontalFlip. Se predice la imagen original y la imagen flipeada, luego se promedian las probabilidades. El promedio suaviza incertidumbre, especialmente en bordes.
- Optimización de threshold. El modelo produce probabilidades entre 0 y 1, hay que elegir un umbral para binarizar. Se prueban valores de 0.30 a 0.75 en validación y se elige el que maximiza mean dice. El threshold óptimo varió entre experimentos.
- Se calcula dice por cada imagen individual para identificar mejores y peores casos.
- Se visualizan y guardan las 5 mejores y 10 peores predicciones. Esto permite entender en qué imágenes le va bien al modelo y en cuáles le está costando más.
    - Observando las peores predicciones se puede concluir que el modelo confunde fondos de colores similares a la piel (rocas naranjas, mantas rosadas, madera marrón) con personas.
    - Las augmentaciones de color ayudan pero se ve que no eliminan el problema. Se intentó transformaciones más agresivas para atacar este problema, como ChannelShuffle, ColorShuffle, etc. pero el rendimiento del modelo empeoró en todos los casos. Se ve que debe haber un balance muy fino en donde el rendimiento del modelo es óptimo solo bajo ciertas transformaciones.
    - Una observación importante es que los cambios en estas transformaciones afectan significativamente el rendimiento del modelo, tanto para bien como para mal. Este parece ser uno de los factores con mayor influencia en el rendimiento.
- Se genera histograma de distribución de Dice scores para ver la variabilidad de las predicciones.
- Para las predicciones de test:
    - Se aplica TTA igual que en validación.
    - Se usa el threshold óptimo encontrado en validación.
    - Las máscaras se generan a 384x384 y se redimensionan a 800x800 con interpolación nearest-neighbor (para preservar valores binarios 0/1).
- RLE (Run-Length Encoding) para Kaggle.
    - Comprime la máscara binaria en un string de pares "inicio longitud".
    - Detalle crítico: order='F' al aplanar la máscara. Kaggle espera columnas primero (Fortran order), Python usa filas por defecto. Sin esto las predicciones quedan rotadas 90°.
    - Se implementó verificación: encode → decode → comparar con original.
- Se genera el archivo submission.csv para subir a Kaggle.

### Métricas finales del modelo

- El modelo supera ampliamente el requisito mínimo de Dice >= 0.75 establecido en el obligatorio, alcanzando un Dice medio de 0.9549 en validación.
- La mediana (0.9811) es significativamente mayor que la media (0.9549), lo que indica que la mayoría de las predicciones son muy buenas pero hay algunos outliers que bajan el promedio.
- El Dice máximo de 0.9970 muestra que el modelo puede lograr predicciones casi perfectas cuando la imagen no presenta ambigüedades.
- El Dice mínimo de 0.3851 corresponde a los casos problemáticos identificados en la sección de evaluación (fondos con colores similares a piel).
- La diferencia entre Train Dice (0.9859) y Val Dice (0.9526) es pequeña, indicando que no hay overfitting severo.
- Predicciones de test: 534 imágenes, todas con foreground detectado (ninguna máscara vacía). El modelo siempre detecta algo, no hay casos donde prediga que no hay persona.
