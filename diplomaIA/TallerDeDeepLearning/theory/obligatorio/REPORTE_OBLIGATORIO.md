# Reporte: Información sobre el Obligatorio - Taller de Deep Learning

**Fecha del Reporte**: 06 de noviembre de 2025
**Fuente**: Transcripciones de clases del 22/10/2025, 29/10/2025 y 05/11/2025

---

## 1. INFORMACIÓN GENERAL

### Fechas Clave
- **Fecha de entrega**: 3 de diciembre de 2025 (originalmente 12/12, pero se adelantó)
- **Parcial**: 3 de diciembre de 2025 (mismo día)
- **Posible ajuste**: Se discutió cerrar la competencia de Kaggle un día antes (2/12) para poder entregar material el día del parcial

### Ponderación
- **50 puntos de 100** (la mitad de la nota final)
- Tarea 1: 15 puntos
- Tarea 2: 15 puntos
- Obligatorio: 50 puntos
- Parcial: 20 puntos
- **Total para aprobar**: 70 puntos

### Equipos
- Se puede hacer en equipos
- Hay competencia en Kaggle entre equipos
- Premio: Un libro para el equipo ganador de la competencia de Kaggle

---

## 2. DESCRIPCIÓN DEL PROYECTO

### Tema: Segmentación de Imágenes con U-Net

**Objetivo**: Implementar desde cero una arquitectura U-Net para segmentación semántica de personas en imágenes.

**Problema específico**:
- Dada una imagen de entrada, generar una máscara que identifique dónde hay personas
- Similar a la funcionalidad de crear stickers en WhatsApp
- Es un problema de **segmentación semántica**

### Dataset
- **Train**: ~2,100 imágenes con máscaras de segmentación incluidas
- **Test**: Imágenes sin máscaras (para la competencia de Kaggle)
- **Tamaño**: ~2-3 GB de imágenes
- **Dimensiones**: 800x800 píxeles (todas las imágenes son cuadradas)
- **Formato**: RGB (3 canales) o escala de grises (1 canal)

---

## 3. REQUISITOS TÉCNICOS

### Implementación
1. **Todo desde cero**: NO se permite usar modelos preentrenados
2. **Paper de referencia**: Implementar basándose en el paper de U-Net original (2015)
3. **Flexibilidad**: Se pueden hacer ajustes en:
   - Número de capas
   - Número de canales
   - Profundidad de la red
   - Uso de padding
   - **PERO**: Mantener la esencia de la arquitectura U-Net

### Arquitectura U-Net - Conceptos Clave

**Estructura general**:
- **Encoder (lado izquierdo)**: Reduce dimensiones espaciales, aumenta canales
- **Decoder (lado derecho)**: Aumenta dimensiones espaciales, reduce canales
- **Skip connections**: Concatenación de features del encoder al decoder en el mismo nivel

**Componentes principales**:
1. **Doble convolución**: Patrón repetido en toda la red
   - 2 convoluciones consecutivas
   - Activación ReLU entre ellas
   - Con o sin padding (decisión de diseño)

2. **Max Pooling**: Reduce dimensiones a la mitad en el encoder

3. **Convolución Transpuesta (Up-convolution)**:
   - Nueva capa que NO han visto antes
   - `nn.ConvTranspose2d` en PyTorch
   - Agranda la imagen al doble
   - Los pesos se aprenden durante el entrenamiento

4. **Skip Connections** (MUY IMPORTANTE):
   - Concatenar (NO sumar) features del encoder con el decoder
   - Requiere que las dimensiones coincidan
   - Si no usan padding: necesitarán hacer **cropping** de las imágenes del encoder
   - Si usan padding: las dimensiones coinciden automáticamente

**Desafío del paper original**:
- Sin padding: La imagen de salida es MÁS PEQUEÑA que la entrada (572x572 → 388x388)
- Con padding: La imagen de salida tiene el MISMO tamaño que la entrada

---

## 4. DECISIONES DE DISEÑO CRÍTICAS

### Problema del Tamaño de Imagen

**ALERTA IMPORTANTE**: NO entrenar con imágenes de 800x800
- Tiempo de entrenamiento: ~10 horas por experimento
- Memoria GPU: Batch size muy pequeño (≤4)
- **Feedback loop malo**: No pueden iterar rápidamente

**Recomendaciones del profesor**:
1. Empezar con imágenes pequeñas (80x80 o 100x100) para validar arquitectura
2. Hacer la arquitectura **parametrizable** (tamaño de entrada como variable)
3. Una vez que funciona, ir agrandando progresivamente
4. Considerar el número de niveles de pooling para evitar llegar a tensores de <3x3

### Padding vs No Padding

**Sin Padding (como el paper original)**:
- Pros: Arquitectura original, paper probado
- Contras:
  - Necesitas hacer cropping en skip connections
  - Salida más pequeña que entrada
  - Más complejo de implementar

**Con Padding**:
- Pros:
  - Más simple de implementar
  - Salida del mismo tamaño que entrada
  - No necesitas cropping
- Contras:
  - Se desvía un poco del paper original
- **Recomendación**: Solo 2 caracteres de código (`padding=1` en convolutions)

### Salida del Modelo

**Problema**: Entrenarás con imágenes redimensionadas (ej: 128x128), pero debes generar máscaras de 800x800 para Kaggle

**Opciones**:
1. Redimensionar la salida del modelo de vuelta a 800x800
2. Diseñar la red para que la salida sea 800x800 desde el inicio (no recomendado por tiempo de cómputo)
3. Trabajar con múltiples resoluciones

---

## 5. MÉTRICAS Y EVALUACIÓN

### Métrica Principal: Coeficiente de Dice

**Fórmula**:
```
Dice = 2 × |A ∩ B| / (|A| + |B|)
```
Donde:
- A = píxeles predichos como persona
- B = píxeles reales de persona

**Escala**:
- 0 = Sin coincidencia
- 1 = Coincidencia perfecta

**Mínimo requerido**: 0.75 (75% de coincidencia)

### Competencia de Kaggle
- Límite de submissions: 3 por día por usuario
- El leaderboard público muestra resultados en ~30% del test set
- El leaderboard final (privado) se revela con el 100% del test set el día de cierre
- Pueden haber cambios de posiciones entre leaderboard público y privado

### Formato de Entrega para Kaggle
- Archivo CSV con encoding RLE (Run-Length Encoding)
- NO se suben las imágenes de las máscaras directamente
- El código para generar el CSV está proporcionado en el material del curso

**RLE explicado**:
- Aplanar la imagen columna por columna
- Indicar: posición del primer píxel de persona, cantidad de píxeles consecutivos
- Ejemplo: "31 1 62 93 141" = en posición 31 hay 1 píxel, en 6 hay 2 píxeles, etc.

---

## 6. CRITERIOS DE EVALUACIÓN (50 puntos)

### 1. Análisis del Dataset (puntos no especificados)
- Gráficas del dataset
- Análisis de balanceo de clases (¿mayoría de píxeles son personas o fondo?)
- Estudio de la distribución de los datos
- Comprensión de los valores de píxeles (0-255, qué significa cada valor)

### 2. Implementación Correcta del Modelo
- Basada en el paper de U-Net
- Código claro y bien estructurado
- Modularización recomendada (crear bloques reutilizables):
  - Doble convolución
  - Bloque de encoder
  - Bloque de decoder

### 3. Entrenamiento del Modelo
- Técnicas de regularización aplicadas y justificadas
- Gráficas de training/validation loss
- Conclusiones sobre el proceso de entrenamiento
- Data augmentation (si se usa)
- W&B (Weights & Biases) es opcional para este obligatorio

### 4. Evaluación de Resultados
- Métricas de segmentación (Dice coefficient)
- Análisis detallado de los resultados
- **Visualización de ejemplos**: Mostrar imagen original + máscara predicha superpuesta
- Casos de éxito y casos de fallo

### 5. Competencia de Kaggle
- Al menos 1 submission subida
- Puntaje mínimo de Dice: 0.75

### 6. Justificación de Decisiones
**CRÍTICO**: Cada decisión debe estar justificada:
- ¿Por qué redimensionaste a ese tamaño?
- ¿Por qué usaste/no usaste padding?
- ¿Por qué aplicaste esa transformación?
- ¿Por qué usaste esos hiperparámetros?
- ¿Qué problema intentabas resolver con cada cambio?

**Ejemplo de justificación**:
- "Normalicé las imágenes porque el modelo no entrenaba sin normalización"
- "Reduje a 128x128 porque con 256x256 el entrenamiento tomaba 5 horas por época"

---

## 7. DEFENSA ORAL (día del parcial)

### Formato
- Día: 3 de diciembre (día del parcial)
- Duración: ~15 minutos por equipo
- Preguntas rápidas sobre el trabajo

### Tipo de Preguntas Esperadas

**NO te preguntarán**:
- Detalles minuciosos de implementación
- Número exacto de canales en cada capa

**SÍ te preguntarán**:
- ¿Cuáles fueron las 3 decisiones más importantes que tomaste?
- ¿Cuántos niveles tiene tu U-Net?
- ¿Redimensionaste las imágenes? ¿A qué tamaño? ¿Por qué?
- ¿Usaste padding o no? ¿Por qué?
- ¿Qué problema tuviste y cómo lo resolviste?
- Justificación de decisiones macro

**Objetivo**: Verificar que entiendes tu propio trabajo y que realmente lo hiciste tú

---

## 8. ENTREGA

### Plataforma
- **Gestión** (sistema de la universidad)
- NO se entrega por Aulas
- Límite de tamaño: 30-50 MB máximo

### Formato
- Jupyter Notebook (.ipynb)
- **Todas las celdas ya ejecutadas** (el profesor NO volverá a ejecutar)
- Código claro y documentado
- Decisiones de diseño explicadas en el notebook

### Recomendación de Seguridad
- Hacer una entrega 2 días antes con lo que tengas
- Puedes entregar varias veces
- En el peor caso, tienes algo entregado

### NO Incluir
- Las imágenes del dataset (muy pesadas)
- Posiblemente los pesos del modelo entrenado (muy pesados)

---

## 9. CONSEJOS DEL PROFESOR

### Gestión del Proyecto

1. **No subestimes el obligatorio**
   - "Programar la red toma ~20% del trabajo"
   - El 80% restante es: experimentación, ajustes, debugging, análisis

2. **Tiempo estimado**
   - El profesor dedicó 5-6 horas solo para lograr que empiece a bajar el loss
   - Planea dedicar varios fines de semana

3. **Relación con Tarea 2**
   - La Tarea 2 se entrega el 16/11
   - "NO le dediquen más de 2 fines de semana a la Tarea 2"
   - Prioriza el obligatorio que vale mucho más

4. **Iteración rápida**
   - Empieza con modelos pequeños y rápidos
   - Valida que todo funciona
   - Luego escala progresivamente
   - "10 horas de entrenamiento = mal feedback loop"

### Implementación

5. **Modularización**
   - Crea bloques reutilizables
   - Doble convolución como módulo
   - Encoder/Decoder como módulos
   - Más fácil de debuggear

6. **Arquitectura parametrizable**
   - Tamaño de imagen como variable
   - Número de niveles como variable
   - Facilita experimentación

7. **Debugging progresivo**
   - Usa `model.summary()` o herramientas similares
   - Verifica shapes en cada paso
   - No esperes que compile a la primera

8. **Recursos computacionales**
   - Google Colab es suficiente
   - Si puedes, usa GPU local
   - Servidores de facultad como opción

### Durante el desarrollo

9. **Llevar registro**
   - Documenta cada experimento
   - Anota qué funcionó y qué no
   - Será útil para la defensa

10. **Visualización constante**
    - Mira las máscaras predichas frecuentemente
    - No te guíes solo por la métrica
    - Puede estar prediciendo bien pero de forma escalonada (por redimensionamiento)

---

## 10. RECURSOS DISPONIBLES

### Paper Original
- U-Net: Convolutional Networks for Biomedical Image Segmentation (2015)
- Enfoque en la arquitectura, no todos los detalles

### Código de Ejemplo
- El profesor tiene el obligatorio de un alumno del año pasado como referencia
- Código en ~40-50 líneas para el modelo (bien modularizado)

### Competencia de Kaggle
- Ya está creada y disponible
- Dataset de train y test disponibles para descarga

### Material del Curso
- Notebooks con ejemplos de CNNs
- Código para generar el CSV con formato RLE
- Utils para métricas de segmentación

---

## 11. PREGUNTAS FRECUENTES (de las transcripciones)

**P: ¿Puedo usar Transfer Learning?**
R: NO. Todo debe ser desde cero.

**P: ¿La cantidad de canales del paper original son fijos?**
R: No, puedes ajustarlos. Lo importante es mantener la estructura U-Net.

**P: ¿Qué hago si mi imagen de entrada es 800x800 pero mi salida queda más chica?**
R: Opciones:
   1. Usar padding en todas las convoluciones
   2. Redimensionar la salida de vuelta a 800x800
   3. Diseñar la arquitectura para que llegue a 800x800 (más complejo)

**P: ¿Cuántos niveles de max pooling debería tener?**
R: Depende del tamaño de tu imagen de entrada. Si empiezas con 80x80 y haces 4 niveles de pooling: 80→40→20→10→5. Con convoluciones sin padding, puedes llegar a <3x3 y tendrás error. Ajusta según tu caso.

**P: ¿Está bien empezar con imágenes muy pequeñas?**
R: Sí, es lo recomendado. Empieza con 80x80 o 100x100 para validar que todo funciona.

**P: ¿W&B es obligatorio?**
R: No para el obligatorio (sí lo fue para Tarea 1 y Tarea 2).

**P: ¿Qué pasa si me equivoco en una decisión?**
R: Lo importante es que justifiques por qué lo intentaste. "Lo probé y funcionó" con contexto de qué problema tenías es válido.

**P: ¿La fecha de entrega del obligatorio se puede mover?**
R: NO. Es "incorrible, no se puede correr, imposible" (palabras del profesor). Es el 3 de diciembre y hay parcial el mismo día.

---

## 12. CHECKLIST PARA ANTES DE RENDIR EL OBLIGATORIO

### Implementación
- [ ] Arquitectura U-Net implementada desde cero
- [ ] Skip connections funcionando (concatenación, no suma)
- [ ] Salida del modelo del tamaño correcto (800x800 o con estrategia para llegar a ese tamaño)
- [ ] Código modularizado y legible

### Experimentación
- [ ] Al menos 3-4 experimentos documentados
- [ ] Gráficas de training/validation loss
- [ ] Visualización de máscaras predichas vs reales

### Análisis
- [ ] EDA (Exploratory Data Analysis) del dataset completo
- [ ] Análisis de balanceo de clases
- [ ] Análisis de casos de éxito y fallo del modelo

### Métricas
- [ ] Coeficiente de Dice calculado
- [ ] Otras métricas de segmentación si aplican
- [ ] Dice score > 0.75 en Kaggle

### Kaggle
- [ ] Al menos 1 submission exitosa
- [ ] CSV con formato RLE correcto
- [ ] Verificar que el score en Kaggle sea razonable

### Documentación
- [ ] Todas las decisiones de diseño justificadas
- [ ] Notebook con celdas ejecutadas
- [ ] Conclusiones sobre cada experimento
- [ ] Explicación de preprocesamiento de datos

### Defensa Oral
- [ ] Puedes explicar las 3 decisiones más importantes
- [ ] Sabes cuántos niveles tiene tu red
- [ ] Puedes justificar el tamaño de imagen elegido
- [ ] Entiendes por qué funcionó o no funcionó algo

---

## 13. RESUMEN EJECUTIVO

### Lo MÁS importante

1. **Fecha límite**: 3 de diciembre (día del parcial) - NO NEGOCIABLE
2. **Puntaje**: 50 de 100 puntos - la mitad de tu nota
3. **Métrica mínima**: Dice ≥ 0.75 en Kaggle
4. **Implementación**: Desde cero, basada en U-Net paper
5. **Defensa oral**: ~15 minutos el día del parcial

### Lo que DEBES hacer antes de empezar a codear

1. Leer (al menos la parte de arquitectura) del paper de U-Net
2. Entender las skip connections y cómo funcionan
3. Decidir: ¿padding o no padding?
4. Planear la modularización del código
5. Elegir un tamaño de imagen inicial pequeño para testear

### Lo que te hará DESTACAR

1. Buenas visualizaciones de resultados
2. Análisis profundo de casos de éxito y fallo
3. Experimentos bien documentados con conclusiones claras
4. Código limpio y modular
5. Justificaciones sólidas de cada decisión
6. Buen puntaje en la competencia de Kaggle (pero no es el único criterio)

---

## ÚLTIMA RECOMENDACIÓN

El profesor enfatizó múltiples veces:

> "El obligatorio NO es solo programar la red. Eso es el 20%. El resto es experimentación, análisis, ajustes y documentación. No lo subestimen."

Empieza YA. Tienes ~1 mes desde ahora (6 de noviembre) hasta el 3 de diciembre.

**Plan sugerido**:
- Semana 1 (6-12 nov): Leer paper, diseñar arquitectura, implementar versión básica
- Semana 2 (13-19 nov): Experimentar, debuggear, hacer funcionar bien con imágenes pequeñas
- Semana 3 (20-26 nov): Escalar, optimizar, subir a Kaggle, refinar
- Semana 4 (27 nov-3 dic): Documentar, analizar, preparar defensa, buffer para imprevistos

---

**Fin del Reporte**

*Este reporte se basa en las transcripciones completas de las clases del 22, 29 de octubre y 5 de noviembre de 2025. Cualquier actualización posterior debe verificarse con el profesor o en el material oficial del curso.*
