# Justificacion de Decisiones y Conclusion de Experimentos

Este documento presenta la justificacion exhaustiva de cada decision tomada en el notebook. Cada eleccion se fundamenta en el paper original de U-Net (Ronneberger et al., 2015), los requisitos del obligatorio, las indicaciones del profesor en clase, y los resultados experimentales documentados en HISTORY.md.

---

## Configuracion General

### Imports (Celda 1)

**PyTorch vs TensorFlow/Keras:**
El obligatorio especifica explicitamente que la implementacion debe realizarse "desde cero utilizando PyTorch". Aunque TensorFlow/Keras ofrece implementaciones pre-hechas de U-Net, el objetivo pedagogico es comprender la arquitectura internamente, lo cual requiere construirla manualmente en PyTorch.

**Albumentations vs torchvision.transforms:**
Se eligio Albumentations sobre torchvision.transforms por una razon critica: en segmentacion semantica, las transformaciones geometricas (rotacion, flip, escala) deben aplicarse identicamente a imagen y mascara. Albumentations maneja esto nativamente con un solo llamado, mientras que torchvision requiere sincronizacion manual de seeds aleatorios entre transformaciones separadas, lo cual es propenso a errores y produce desalineacion imagen-mascara.

**OpenCV vs PIL para redimensionamiento:**
OpenCV (cv2.resize) ofrece control explicito sobre el metodo de interpolacion. Para mascaras binarias, INTER_NEAREST es obligatorio para preservar valores discretos (0 y 1). PIL.Image.resize puede introducir valores intermedios dependiendo del modo, corrompiendo la mascara.

### Configuracion del Dispositivo y Seeds (Celda 2)

**Por que fijar semillas en multiples lugares:**
La aleatoriedad en deep learning proviene de multiples fuentes: inicializacion de pesos (torch), shuffling de datos (numpy, random), y operaciones de GPU (CUDA). Fijar solo una semilla deja otras fuentes de variabilidad activas, haciendo imposible reproducir resultados exactos.

**torch.backends.cudnn.deterministic = True:**
Las operaciones de cuDNN (biblioteca de NVIDIA para redes neuronales) tienen implementaciones no-deterministicas que son mas rapidas pero producen resultados ligeramente diferentes en cada ejecucion. Activar modo deterministico sacrifica ~10-15% de velocidad por reproducibilidad exacta. Este trade-off es aceptable durante desarrollo y experimentacion donde comparar runs es esencial.

**torch.backends.cudnn.benchmark = False:**
Cuando benchmark=True, cuDNN prueba multiples algoritmos para cada operacion y cachea el mas rapido. Esto introduce variabilidad porque la seleccion depende del estado de la GPU. Desactivarlo garantiza que siempre se use el mismo algoritmo.

### Estructura de Directorios (Celda 3)

**Por que subdirectorios separados:**
La organizacion en subdirectorios (`bestModel/`, `graphs/`, `predictions/`, `kaggleSubmission/`) facilita:
1. Localizacion rapida de outputs especificos.
2. Evitar sobrescritura accidental entre tipos de archivos.
3. Limpieza selectiva (borrar graficas sin perder modelos).
4. Cumplimiento del requisito del obligatorio de entregar codigo "escrito de manera clara".

### Hiperparametros (Celda 4)

**IMG_SIZE = 384:**

*Problema:* Las imagenes originales son 800x800. El profesor explico en clase: "entrenar con 800 por 800, olvidenselo, o sea, no ni ni aunque contraten una maquina muy pesada, van a estar entrenando con eso". La memoria GPU crece cuadraticamente con la resolucion (800x800 = 640,000 pixeles vs 384x384 = 147,456 pixeles, factor de ~4.3x).

*Alternativas consideradas:*
- 128x128: Demasiado pequeno, pierde detalles finos de contornos humanos.
- 256x256: Viable, usado en experimentos iniciales (Runs 1-8).
- 384x384: Mejor balance, probado en Run 9.
- 512x512: Posible pero limita batch size a ~4, gradientes menos estables.

*Evidencia experimental (HISTORY.md, Run 9):*
| Resolucion | Mean Dice | Cambio |
|------------|-----------|--------|
| 256x256 (Run 6) | 0.9167 | baseline |
| 384x384 (Run 9) | 0.9352 | +1.85% |

El salto de 256 a 384 produjo mejora significativa porque la resolucion mayor captura mejor los bordes y detalles de la silueta humana. El costo fue mayor tiempo de entrenamiento (~3x) pero el beneficio lo justifica.

**BATCH_SIZE = 8:**

*Problema:* Batch size afecta tanto memoria GPU como dinamica de entrenamiento.

*Alternativas consideradas:*
- Batch 4: Muy pequeno, gradientes muy ruidosos, entrenamiento inestable.
- Batch 8: Balance entre ruido beneficioso y estabilidad.
- Batch 16-18: Probado en Run 7.
- Batch 32+: Imposible con 384x384 en 12GB VRAM.

*Evidencia experimental (HISTORY.md, Run 7):*
| Batch Size | Best Val Dice | Observacion |
|------------|---------------|-------------|
| 8 (Run 6) | 0.9167 | baseline |
| 18 (Run 7) | 0.9093 | -0.74% |

Run 7 demostro que batch size mayor empeoro resultados. La explicacion teorica: batches pequenos introducen ruido estocastico que actua como regularizacion implicita, ayudando a escapar de minimos locales "sharp" que generalizan peor (Keskar et al., 2017: "On Large-Batch Training for Deep Learning").

**VAL_SPLIT = 0.2:**

*Problema:* Cuantos datos reservar para validacion.

*Trade-off:*
- Mas validacion (30%): Mejor estimacion de generalizacion, pero menos datos de entrenamiento.
- Menos validacion (10%): Mas datos de entrenamiento, pero estimacion de validacion menos confiable.

*Decision:* 20% es convencion estandar. Con 2133 imagenes, 20% = 426 imagenes de validacion. Esto proporciona muestra estadisticamente significativa para evaluar rendimiento mientras retiene 1707 imagenes para entrenamiento.

**DROPOUT = 0.1:**

*Origen:* El paper original menciona en Seccion 3.1: "Drop-out layers at the end of the contracting path perform further implicit data augmentation."

*Alternativas consideradas:*
- Sin dropout: Probado implicitamente en runs iniciales.
- Dropout 0.1: Conservador, regularizacion leve.
- Dropout 0.2: Probado en Run 8.
- Dropout 0.25: Usado en configuraciones posteriores.

*Evidencia experimental (HISTORY.md, Run 8):*
Run 8 con dropout 0.2 fue inconcluso por diferencia en epochs. A igual numero de epochs, dropout mostro efecto minimo en val_dice. Conclusion: dropout ayuda marginalmente pero no es factor critico para este dataset de 2133 imagenes.

**LEARNING_RATE = 1e-4:**

*Por que 1e-4 y no otro valor:*
- 1e-3: Tipicamente demasiado alto para Adam, puede causar divergencia o oscilaciones.
- 1e-4: Valor por defecto recomendado para Adam en la mayoria de tareas de vision.
- 1e-5: Demasiado conservador, convergencia muy lenta.

Este valor no fue optimizado exhaustivamente porque funciono bien desde el inicio. El scheduler se encarga de ajustarlo dinamicamente durante entrenamiento.

**NUM_EPOCHS = 600:**

*Problema:* Cuantas epocas entrenar.

*Evidencia experimental:*
| Run | Epochs | Mean Dice | Observacion |
|-----|--------|-----------|-------------|
| Run 2 | 61 (early stop) | 0.9012 | Early stopping prematuro |
| Run 5 | 120 | 0.9116 | Mejora al desactivar early stopping |
| Run 6 | 120 | 0.9167 | Continua mejorando |
| Run 9 | 400 | 0.9352 | Mejor resultado hasta entonces |
| Run 12 | 570 | 0.9550 | Mejor resultado global |

El modelo continuo mejorando significativamente mas alla de 120 epochs. Contrario a la intuicion de que mas epochs = overfitting, el uso de CosineAnnealingLR con decaimiento suave permite refinamiento continuo sin sobreajuste.

**UNET_DEPTH = 4 y UNET_FILTERS = [64,128,256,512,1024]:**

*Origen:* Directamente del paper original. La arquitectura tiene 4 niveles de downsampling con duplicacion de canales en cada nivel.

*Por que no modificar la profundidad:*
El profesor advirtio en clase: "imaginate que vos arranco, no? [...] Es muy es muy es muy probable que aca sea te con un pixel solo. Entonces, no vas a tener como ningun tipo de resultado". Con imagenes de 384x384:
- Nivel 0: 384x384
- Nivel 1: 192x192
- Nivel 2: 96x96
- Nivel 3: 48x48
- Nivel 4 (bottleneck): 24x24

24x24 es suficientemente grande para preservar informacion espacial. Un 5to nivel reduciria a 12x12, aun viable pero con menor beneficio marginal y mayor costo computacional.

---

## Analisis del Dataset

### Funciones de Visualizacion (Celda 5)

**Por que visualizar overlay (imagen + mascara superpuesta):**
La visualizacion side-by-side de imagen y mascara no revela desalineaciones sutiles. El overlay con transparencia permite verificar que la mascara corresponde exactamente a la silueta de la persona, detectando errores de etiquetado o problemas de carga de datos.

### Verificacion de Dimensiones (Celda 7)

**Por que verificar si todas son 800x800:**
El obligatorio menciona que las imagenes tienen "la facilidad de que todas tienen 800 por 800, ya es que no son cuadradas y rectangulares, eso les da una cierta facilidad". Esta verificacion confirma esta asuncion y detectaria imagenes anomalas que requerirean manejo especial (padding, cropping diferente).

### Distribucion de Clases (Celdas 9-10)

**Por que analizar el balance de clases:**
En segmentacion, el desbalance de clases (mas background que foreground) afecta la eleccion de funcion de perdida:

*Si usaramos solo BCE Loss:*
Con imagenes donde la persona ocupa ~20% de pixeles, un modelo trivial que predice todo como "background" obtendria ~80% accuracy. BCE optimizaria hacia esta solucion degenerada.

*Solucion:*
Dice Loss es invariante al desbalance de clases porque mide overlap relativo, no conteo absoluto de pixeles correctos. Por eso combinamos BCE (gradientes estables) con Dice (metrica justa).

---

## Procesamiento del Dataset

### Data Augmentation - Train Transform (Celda 11)

**Resize a 384x384:**

*Interpolacion para imagen (cv2.INTER_LINEAR):*
Interpolacion bilinear suaviza transiciones, produciendo imagenes visualmente naturales al reducir resolucion.

*Interpolacion para mascara (cv2.INTER_NEAREST):*
Nearest-neighbor preserva valores discretos. Cualquier otra interpolacion (bilinear, bicubic) crearia valores intermedios (0.3, 0.7) que corrompen la mascara binaria.

**HorizontalFlip p=0.5:**

*Por que si y VerticalFlip no:*
El profesor explico que el dataset contiene "personas que normalmente estan erguidas". Un flip horizontal produce una persona mirando al lado opuesto (perfectamente realista). Un flip vertical produce una persona cabeza abajo, situacion que nunca ocurre en el dataset real. Entrenar con imagenes irreales perjudica generalizacion.

*Evidencia:* HISTORY.md documenta que VerticalFlip fue removido en Run 12 como parte del analisis de augmentation realista, contribuyendo a mejora de +80% en worst case.

**ShiftScaleRotate con rotate_limit=15:**

*Por que 15 grados y no 30 (valor del paper):*
El paper de U-Net trabaja con celulas microscopicas que pueden aparecer en cualquier orientacion. Las personas en fotografias normalmente estan erguidas o con inclinaciones leves. El profesor dijo: "rotate_limit=30 [...] Too aggressive for humans".

Rotaciones de 30 grados producen personas "cayendose" que no existen en el dataset de test, ensenando patrones irrelevantes al modelo.

**OneOf[RandomBrightnessContrast, CLAHE, RandomGamma] p=0.5:**

*Por que variedad de ajustes de iluminacion:*
El analisis visual del dataset revelo variedad extrema de iluminacion:
- Siluetas (backlit, persona oscura contra fondo brillante).
- Estudio (iluminacion uniforme profesional).
- Exterior (luz natural variable, sombras duras).

*Por que CLAHE especificamente:*
CLAHE (Contrast Limited Adaptive Histogram Equalization) mejora contraste local, ayudando en imagenes con siluetas donde la persona es muy oscura. Esto fue identificado en HISTORY.md como mejora clave de Run 12.

**OneOf[HueSaturationValue, ColorJitter] p=0.35:**

*Problema:* El modelo podria aprender "piel = persona" basandose en tonos de color especificos.

*Solucion:* Variar colores durante entrenamiento fuerza al modelo a aprender formas y texturas, no solo colores. Esto mejora robustez ante:
- Diferentes tonos de piel.
- Ropa de cualquier color.
- Efectos de post-procesamiento fotografico.

**ToGray p=0.20:**

*Origen:* El analisis del dataset revelo que algunas imagenes son fotografias en blanco y negro o con efectos vintage.

*Mecanismo:* Convertir imagenes a escala de grises durante entrenamiento ensena al modelo a segmentar basandose puramente en forma y textura, sin depender de color. Esto es especialmente importante para el problema identificado en HISTORY.md donde el modelo confundia fondos color-piel (mantas rosadas, rocas naranjas) con personas.

**GaussNoise p=0.03 con var_limit=(5,20):**

*Por que probabilidad tan baja (3%):*
El analisis del dataset determino que "Only ~3% of images have noise" porque son mayormente fotografias profesionales o semi-profesionales. Aplicar ruido al 20-30% de imagenes introduciria artefactos no representativos del dataset real.

*Por que varianza baja (5-20):*
Varianzas altas (40-50 como en configuraciones iniciales) producen ruido visible que degrada la imagen significativamente. Valores bajos simulan ruido de sensor sutil sin destruir detalles importantes.

**Ausencia de ElasticTransform:**

*Presente en paper original, removido aqui:*
El paper de U-Net usa deformaciones elasticas porque trabaja con tejido biologico que naturalmente se deforma. Las personas son cuerpos rigidos; deformaciones elasticas producen:
- Brazos ondulados.
- Cabezas deformadas.
- Bordes borrosos.

HISTORY.md documenta que ElasticTransform fue removido en Run 12, contribuyendo a mejor preservacion de bordes y mejora en worst case.

### Clase SegmentationDataset (Celda 14)

**Normalizacion de mascara (mask / 255.0):**

*Problema:* Las mascaras PNG se cargan con valores 0 y 255.

*Solucion:* Dividir por 255 convierte a rango [0, 1] requerido para:
- BCELoss espera targets en [0, 1].
- Dice coefficient se calcula sobre valores [0, 1].

**Manejo de caso sin mascara (test set):**

El test set de Kaggle no tiene mascaras. El dataset retorna solo la imagen cuando mask_paths=None, permitiendo reutilizar la misma clase para train, val y test.

### Division Train/Validation (Celda 18)

**Por que shuffle antes de split:**
Sin shuffle, las primeras 80% de imagenes (ordenadas alfabeticamente) van a train y las ultimas 20% a val. Si el dataset tiene algun orden subyacente (por ejemplo, imagenes del mismo fotografo agrupadas), esto introduce sesgo. Shuffle aleatoriza la asignacion.

**Por que seed fijo para shuffle:**
Permite reproducir exactamente la misma particion en futuras ejecuciones, esencial para comparar experimentos de manera justa.

---

## Implementacion del Modelo

### Bloque DoubleConv (Celda 20)

**Padding=1 vs sin padding (paper original):**

*Paper original (sin padding):*
Cada convolucion 3x3 reduce dimensiones en 2 pixeles (borde perdido). Con doble convolucion por nivel y 4 niveles, la salida es significativamente menor que la entrada (572x572 -> 388x388 en el paper).

*Consecuencia:* Se requiere cropping de feature maps en skip connections para alinear dimensiones.

*Nuestra decision (padding=1):*
Padding=1 con kernel 3x3 mantiene dimensiones constantes. El profesor explico en clase:
"si vos, por ejemplo, haces padding, los de la derecha te quedan del mismo tamano que de izquierda y no tenes que hacer crom [...] son dos caracteres [...] pero te cambia absolutamente la forma".

*Ventajas:*
1. Skip connections triviales (mismas dimensiones, solo concatenar).
2. Output mismo tamano que input (384x384 -> 384x384).
3. Codigo mas simple, menos propenso a errores.
4. La mascara de salida corresponde directamente a la imagen de entrada.

*Desventaja teorica:*
Padding introduce "informacion inventada" en los bordes. En practica, con imagenes de 384x384 y kernel 3x3, el impacto es minimo.

**InstanceNorm2d vs BatchNorm2d:**

*BatchNorm:*
Normaliza usando estadisticas del batch actual. Con batch size pequeno (8), las estadisticas son ruidosas y la normalizacion es inestable.

*InstanceNorm:*
Normaliza cada imagen independientemente. No depende del batch size, produciendo normalizacion estable incluso con batch=1.

*Layer Norm / Group Norm:*
Alternativas validas, pero InstanceNorm es estandar en tareas de imagen-a-imagen (segmentacion, style transfer).

**Bias=False en convoluciones antes de normalizacion:**

La normalizacion (Batch, Instance, etc.) recentra las activaciones a media cero. El bias de la convolucion seria anulado por este recentrado, desperdiciando parametros. Omitirlo reduce parametros sin afectar capacidad del modelo.

### Bloque Down (Celda 21)

**MaxPool2d(2) vs otros metodos de downsampling:**

*Alternativas:*
- Strided convolution: Aprendible pero mas parametros.
- Average pooling: Suaviza demasiado, pierde detalles de bordes.
- Max pooling: Preserva activaciones mas fuertes (bordes, texturas).

*Decision:* Max pooling siguiendo el paper. Para segmentacion donde los bordes son criticos, preservar maximos locales es preferible a promediar.

### Bloque Up (Celda 22)

**ConvTranspose2d vs interpolacion + convolucion:**

*ConvTranspose2d (paper original):*
Upsampling aprendido. Los pesos determinan como expandir features.

*Interpolacion bilinear + Conv2d (alternativa comun):*
Upsampling fijo seguido de convolucion. Menos artefactos de "checkerboard" que ConvTranspose2d.

*Decision:* ConvTranspose2d siguiendo el paper. Los artefactos de checkerboard se mitigan con las convoluciones siguientes en DoubleConv.

**Concatenacion vs suma de skip connections:**

*Suma (ResNet style):*
Combina features sumando elemento a elemento. Requiere mismas dimensiones.

*Concatenacion (U-Net style):*
Apila features en dimension de canales. Duplica canales pero preserva toda la informacion.

El profesor enfatizo: "Concatenacion, no suma [...] terminás aca estas con 1024 canales. Este de aca tiene 1024 canales. La convolucion transpuesta lo va a llevar a la mitad, 512 [...] y la vas a concatenar."

La concatenacion preserva informacion de bajo nivel (bordes, texturas del encoder) junto con informacion semantica de alto nivel (que es persona del decoder), permitiendo localizacion precisa.

### Clase UNet Principal (Celda 23)

**Dropout solo en bottleneck:**

*Por que ahi y no en otros lugares:*
- En encoder: Perderia informacion que se propaga via skip connections.
- En decoder: Perderia informacion reconstruida, danando la salida.
- En bottleneck: Es el punto de maxima compresion (menor resolucion espacial, maximos canales). Dropout aqui regulariza la representacion mas abstracta sin afectar propagacion de detalles espaciales.

**Convolucion final 1x1:**

*Proposito:* Reducir de 64 canales a n_classes (1 para binario).

*Por que 1x1 y no 3x3:*
Una convolucion 1x1 actua como combinacion lineal de canales por pixel, sin mezclar informacion espacial. Esto es suficiente para la clasificacion final pixel-wise y es mas eficiente (9x menos parametros que 3x3).

### Inicializacion de Pesos (Celda 24)

**Kaiming (He) initialization:**

*Problema:* Con inicializacion aleatoria ingenua, las activaciones crecen o decrecen exponencialmente a traves de capas profundas, causando gradientes explosivos o desvanecientes.

*Solucion de Kaiming:* Inicializar con varianza = 2/fan_in, disenado especificamente para ReLU. Mantiene varianza de activaciones constante a traves de capas.

*Paper original:* Seccion 3 menciona "drawing the initial weights from a Gaussian distribution with a standard deviation of sqrt(2/N)" que es exactamente Kaiming initialization.

---

## Entrenamiento del Modelo

### Funcion de Perdida BCEDiceLoss (Celda 27)

**Por que combinar BCE y Dice:**

*Solo BCE:*
- Ventaja: Gradientes bien definidos, entrenamiento estable.
- Desventaja: Sensible a desbalance de clases. Penaliza igualmente cada pixel.

*Solo Dice:*
- Ventaja: Optimiza directamente la metrica de evaluacion. Invariante a desbalance.
- Desventaja: Gradientes pueden ser inestables cuando prediccion o target son vacios.

*Combinacion:*
BCE proporciona gradientes estables. Dice orienta la optimizacion hacia la metrica objetivo.

**Por que pesos 0.3 BCE / 0.7 Dice:**

*Experimento (HISTORY.md, Run 4):*
| Pesos BCE/Dice | Mean Dice | Std Dev | Cambio |
|----------------|-----------|---------|--------|
| 0.5/0.5 (Run 3) | 0.9040 | 0.1293 | baseline |
| 0.3/0.7 (Run 4) | 0.9047 | 0.1238 | +0.07%, std -4.2% |

Dar mas peso a Dice (la metrica de Kaggle) mejoro ligeramente Mean Dice y redujo varianza (predicciones mas consistentes).

### Metrica Dice Coefficient (Celda 28)

**Smooth factor = 1e-6:**

*Problema:* Si prediccion y target son ambos cero (imagen sin persona), Dice = 0/0 = NaN.

*Solucion:* Agregar epsilon pequeno:
```
Dice = (2 * intersection + smooth) / (sum_pred + sum_target + smooth)
```

Con smooth=1e-6, si ambos son cero: Dice = 1e-6 / 1e-6 = 1.0 (prediccion correcta de vacio).

### Funcion de Entrenamiento (Celda 29)

**Mixed Precision Training (AMP):**

*Que hace:*
- Forward/backward pass en float16 (media precision).
- Actualizacion de pesos en float32 (precision completa).
- GradScaler previene underflow de gradientes en float16.

*Beneficios:*
- ~50% menos memoria GPU (float16 = 2 bytes vs float32 = 4 bytes).
- ~20-50% mas rapido en GPUs modernas con Tensor Cores.
- Precision de modelo final identica (pesos son float32).

*Nota de defensa:* HISTORY.md advierte que AMP no fue ensenado en clase y es implementacion propia de investigacion externa.

**Gradient Clipping (max_norm=1.0):**

*Problema:* En redes profundas, gradientes pueden explotar (valores muy grandes) causando actualizaciones enormes que desestabilizan entrenamiento.

*Solucion:* Si la norma del gradiente excede 1.0, escalar todos los gradientes proporcionalmente para que la norma sea exactamente 1.0. Esto limita el tamano maximo de actualizacion.

### Configuracion del Scheduler (Celda 32)

**CosineAnnealingLR vs alternativas:**

*ReduceLROnPlateau (probado en Runs 1-2):*
Reduce LR cuando val_loss deja de mejorar. Problema: En Run 2, nunca se activo porque val_loss siempre fluctuaba ligeramente. LR quedo en 1e-4 todo el entrenamiento.

*CosineAnnealingWarmRestarts (probado en Runs 3-5):*
LR decae con coseno y se reinicia periodicamente a valor inicial.

*CosineAnnealingLR sin reinicios (Run 6+):*
LR decae suavemente de inicial a minimo sin reinicios.

*Evidencia experimental (HISTORY.md):*
| Scheduler | Run | Mean Dice | Worst Case |
|-----------|-----|-----------|------------|
| ReduceLROnPlateau | 2 | 0.9012 | 0.0870 |
| WarmRestarts | 5 | 0.9116 | 0.0880 |
| **Sin reinicios** | **6** | **0.9167** | **0.2188** |

Run 6 supero a Run 5 en todas las metricas, especialmente worst case (+148%). Explicacion: Los reinicios de LR eran demasiado agresivos, perturbando la fase de fine-tuning donde el modelo refina predicciones en casos dificiles.

**T_max = NUM_EPOCHS:**

Con T_max=600, el LR sigue un coseno completo:
- Epoch 0: LR = 1e-4 (maximo)
- Epoch 300: LR = ~5e-5 (punto medio)
- Epoch 600: LR = eta_min (minimo)

Esto proporciona:
1. Fase inicial de aprendizaje rapido (LR alto).
2. Fase media de refinamiento (LR moderado).
3. Fase final de ajuste fino (LR bajo).

### Sistema de Checkpoints (Celda 33)

**Guardar solo cuando val_dice mejora:**

*Problema:* El modelo puede degradarse en epochs finales (overfitting tardio).

*Solucion:* Guardar checkpoint solo cuando val_dice supera el mejor previo. El archivo `best_model.pth` siempre contiene el mejor modelo historico.

*Ejemplo de HISTORY.md:*
```
Epoch 60: val_dice = 0.95 -> best_model.pth guardado
Epoch 70: val_dice = 0.85 -> NO guardado
Epoch 600: val_dice = 0.70 -> NO guardado

Al generar submission, se carga best_model.pth (epoch 60, 0.95)
```

**Guardar tambien ultimo checkpoint:**

`last_checkpoint.pth` permite resumir entrenamiento si se interrumpe (crash, cierre accidental). Contiene estado de optimizer y scheduler, no solo modelo.

---

## Evaluacion del Modelo

### Carga del Mejor Modelo (Celda 40)

**map_location=device:**

Permite cargar checkpoints guardados en GPU diferente (o CPU). Sin esto, cargar un checkpoint de GPU:0 en GPU:1 fallaria.

**weights_only=False:**

Necesario para cargar objetos Python arbitrarios (diccionario con epoch, loss, etc.), no solo tensores de pesos.

### Optimizacion de Threshold con TTA (Celda 41)

**Test-Time Augmentation (TTA):**

*Que hace:*
1. Predice imagen original -> probabilidades P1
2. Predice imagen flipeada horizontalmente -> probabilidades P2 (flipear de vuelta)
3. Promedia: P_final = (P1 + P2) / 2

*Por que solo HorizontalFlip:*
El modelo fue entrenado con HorizontalFlip. Usar augmentations no vistas durante entrenamiento (rotacion, escala) produce predicciones fuera de distribucion que degradan el promedio.

*Beneficio:*
Predicciones en bordes son menos confiables. El promedio de dos perspectivas suaviza incertidumbre en bordes.

**Busqueda de threshold optimo:**

*Por que no usar 0.5:*
El modelo produce probabilidades, no segmentacion binaria. El threshold 0.5 asume que el modelo esta calibrado (0.5 significa 50% confianza). En practica, modelos de segmentacion suelen estar over- o under-confident.

*Busqueda empirica:*
Probar thresholds [0.30, 0.35, ..., 0.75] y seleccionar el que maximiza Mean Dice en validacion. Esto adapta el threshold a la distribucion de confianza especifica del modelo.

*Evidencia (HISTORY.md):*
| Run | Threshold Optimo | Observacion |
|-----|------------------|-------------|
| Run 6 | 0.50 | Modelo confiado |
| Run 9 | 0.35 | Modelo menos confiado |
| Run 12 | 0.45 | Intermedio |

El threshold optimo varia entre modelos, justificando la busqueda.

### Analisis de Mejores y Peores Casos (Celda 43)

**Por que visualizar worst cases:**

El obligatorio requiere: "analisis detallado de los resultados, incluyendo un analisis de errores para identificar y discutir casos dificiles."

*Patrones identificados en HISTORY.md (Run 12 worst case analysis):*
| Rank | Dice | Problema |
|------|------|----------|
| 1 | 0.29 | Rocas color piel |
| 2 | 0.43 | Manta rosada = piel |
| 3 | 0.62 | Encuadre inusual (solo cuello) |
| 4 | 0.62 | Cama beige = piel |
| 5 | 0.64 | Madera marron = piel |

*Conclusion:* El modelo aprendio "pixeles color piel = persona", no estrictamente "forma humana". Esta es una limitacion inherente de U-Net sin mecanismos de atencion o encoders preentrenados.

---

## Predicciones para Kaggle

### Binarizacion y Redimensionamiento (Celda 48)

**Orden de operaciones: threshold primero, resize despues:**

*Alternativa 1: Threshold en 384x384, luego resize a 800x800*
- Mascara binaria (0/1) se escala.
- INTER_NEAREST preserva valores binarios.
- Bordes "escalonados" pero correctos.

*Alternativa 2: Resize probabilidades a 800x800, luego threshold*
- Interpolacion de probabilidades suaviza bordes.
- Threshold produce bordes mas suaves.
- Pero: el modelo nunca vio imagenes 800x800, las probabilidades a esa escala son extrapolacion.

*Decision:* Alternativa 1. Aplicar threshold en la resolucion donde el modelo fue entrenado es mas consistente con su aprendizaje.

### Funciones RLE (Celda 52)

**order='F' (Fortran order) - Critico:**

*Problema:* Kaggle espera RLE en orden column-major (columnas primero). NumPy por defecto usa row-major (filas primero).

*Sin order='F':*
La mascara aplanada recorre filas: [fila0, fila1, fila2, ...]
Kaggle interpreta como columnas, resultando en mascara rotada 90 grados.

*Con order='F':*
La mascara aplanada recorre columnas: [col0, col1, col2, ...]
Coincide con expectativa de Kaggle.

*Impacto:* Sin este parametro, todas las predicciones estarian rotadas y el Dice seria ~0.

---

## Metricas Finales del Modelo

### Resumen Final (Celda 56)

Esta celda compila toda la informacion del experimento para referencia rapida y cumple con el requisito del obligatorio de presentar "resultados claros".

---

## Resumen de Decisiones Clave y Alternativas Rechazadas

| Decision | Alternativas Consideradas | Por que se rechazo la alternativa |
|----------|---------------------------|-----------------------------------|
| IMG_SIZE=384 | 256, 512 | 256 pierde detalle (-1.85% Dice). 512 limita batch size. |
| BATCH_SIZE=8 | 16, 18 | Batch mayor = peor generalizacion (Run 7). |
| Padding=1 | Sin padding (paper) | Requiere cropping complejo, propenso a errores. |
| InstanceNorm | BatchNorm | BatchNorm inestable con batch pequeno. |
| CosineAnnealingLR | WarmRestarts, ReduceLROnPlateau | WarmRestarts muy agresivo. ReduceLR nunca activo. |
| BCEDice 0.3/0.7 | 0.5/0.5, solo BCE, solo Dice | 0.3/0.7 mejor Mean Dice y menor varianza. |
| Dropout=0.1 | Sin dropout, 0.2, 0.25 | Sin dropout menos regularizado. Valores altos sin beneficio claro. |
| HorizontalFlip | VerticalFlip, ambos | Personas nunca invertidas en dataset. |
| rotate_limit=15 | 30 (paper) | 30 grados irreal para personas erguidas. |
| Sin ElasticTransform | Con ElasticTransform | Distorsiona bordes de cuerpos humanos. |
| ToGray p=0.20 | Sin ToGray | Dataset tiene imagenes B&W, necesario para generalizacion. |
| TTA HorizontalFlip | TTA multi-escala | Multi-escala empeoro worst case (HISTORY.md). |

---

## Cumplimiento de Requisitos del Obligatorio

| Criterio | Puntos | Evidencia de Cumplimiento |
|----------|--------|---------------------------|
| Analisis del Dataset | 5 | Celdas 5-10: visualizacion, dimensiones, distribucion de clases, histogramas. |
| Implementacion U-Net | 20 | Celdas 20-26: arquitectura modular, 4 niveles, skip connections, paper fiel con mejoras justificadas. |
| Entrenamiento | 10 | Celdas 27-39: BCEDiceLoss, AdamW, CosineAnnealingLR, graficas de evolucion, checkpoints. |
| Evaluacion | 10 | Celdas 40-45: threshold optimization, TTA, estadisticas Dice, analisis de errores, visualizaciones. |
| Kaggle | 5 | Celdas 46-55: predicciones test, RLE encoding, submission.csv valido. |

---

## Conclusiones

La implementacion sigue la arquitectura U-Net del paper original con adaptaciones justificadas:

1. **Padding=1**: Simplifica skip connections y garantiza salida del mismo tamano que entrada.
2. **InstanceNorm**: Estabilidad con batch size pequeno.
3. **Augmentation realista**: Transformaciones que reflejan variabilidad real del dataset.
4. **CosineAnnealingLR sin reinicios**: Supero alternativas en experimentos controlados.
5. **600 epochs**: El modelo continuo mejorando significativamente mas alla de configuraciones conservadoras.

Cada decision fue guiada por experimentacion sistematica (15+ runs documentados en HISTORY.md), requisitos del obligatorio, indicaciones del profesor, y principios del paper original. El resultado es un modelo que cumple el requisito minimo de Dice >= 0.75 con margen significativo.
