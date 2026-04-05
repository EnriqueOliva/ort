# Temas de la Clase - 27 de Octubre 2025
## Deep Learning - Redes Residuales y Procesamiento de Lenguaje Natural

---

## PARTE 1: REDES RESIDUALES (ResNet y DenseNet)

### 1. Problema del Vanishing Gradient
- Definición: gradientes muy pequeños al retropropagar en redes profundas
- Causa: multiplicar muchas derivadas pequeñas (50+ capas)
- Consecuencia: las primeras capas no se actualizan ("se queda sin batería el auto")
- Indicador: estancamiento en el entrenamiento

### 2. Problema del Exploding Gradient
- Definición: gradientes muy grandes que desestabilizan el entrenamiento
- Indicador: la loss se dispara u oscila violentamente
- Solución conocida: Gradient Clipping (recortar gradientes)
- Menos grave que vanishing gradient

### 3. Skip Connections - La Solución
- Dos formas de implementación:
  - **Aditiva (suma)**: usada en ResNet
  - **Concatenación**: usada en DenseNet

### 4. Conexiones Residuales (ResNet)
- Fórmula: H(x) = F(x) + x
- x = identidad (skip connection)
- F(x) = lo que aprende el bloque (residuo)
- Definición de residuo: "cuánto me alejo de la identidad"
- Ventaja: más fácil aprender desviaciones que desde cero

### 5. Por Qué Funciona para Vanishing Gradient
- La suma "+x" tiene derivada constante = 1
- Los gradientes grandes pueden pasar hacia atrás
- Las primeras capas siguen influyendo en el entrenamiento

### 6. Compatibilidad Dimensional
- Problema: F(x) y x deben tener mismo shape para sumar
- Solución para MLPs: matriz W → F(x) + W·x
- Solución para imágenes: convolución 1×1 para ajustar canales

### 7. Estructura de Bloques Residuales
- Bloque típico: Convolución → Batch Normalization → ReLU
- Truco: BN funciona mejor ANTES de la activación
- Problema con ReLU: siempre positiva o nula
- Solución: no poner activación en la última capa del bloque

### 8. Bloques Residuales del Paper Original (2016)
- Convolución 1×1 (reduce canales: 256→64)
- Batch Norm + ReLU
- Convolución 3×3 (mantiene 64 canales)
- Batch Norm + ReLU
- Convolución 1×1 (expande: 64→256)
- Suma con entrada original

### 9. Interpretación: Múltiples Caminos
- Con 2 bloques: H₂ = F₂(F₁(x) + x) + F₁(x) + x
- La información puede tomar múltiples rutas
- Con 56 capas: número de caminos crece exponencialmente

### 10. Efecto de Ensemble Implícito
- ResNet actúa como combinación de muchos modelos simples
- Todos los caminos usan los mismos pesos (weight sharing)
- Efecto regularizador sin agregar parámetros

### 11. Resultados Experimentales
- Sin residual connections: red de 34 capas PEOR que de 18 capas
- Con residual connections: red de 34 capas MEJOR que de 18
- Importante: NO es sobreajuste (también peor en training)
- Es problema de optimización por vanishing gradient

### 12. Comparación con Dropout
- Son formas ortogonales de regularizar
- Dropout: anula conexiones aleatoriamente
- ResNet: múltiples caminos determinísticos
- Se pueden usar juntas

### 13. DenseNet (2017)
- Usa concatenación en lugar de suma
- Cada capa recibe salida de TODAS las anteriores
- Dense Blocks + Transition Blocks
- Mayor costo en memoria, menos parámetros

### 14. Comparación ResNet vs DenseNet

| Aspecto | ResNet | DenseNet |
|---------|--------|----------|
| Año | 2016 | 2017 |
| Conexión | Suma | Concatenación |
| Memoria | Moderada | Mayor |
| Parámetros | Más | Menos |
| Uso actual | Todavía se usa | Menos usado |

### 15. ¿Cuál Usar?
- Respuesta del profesor: "Tirar una moneda"
- Ambas ya pasaron de moda
- ResNet todavía se usa más

---

## PARTE 2: PROCESAMIENTO DE LENGUAJE NATURAL (NLP)

### 16. ¿Qué es NLP?
- Natural Language Processing
- Clásicamente dominada por lingüistas
- Deep Learning "se comió" el área
- Hoy todo integrado en Large Language Models (LLMs)

### 17. Aplicaciones Principales
- **Sentiment Analysis**: detectar sentimientos en texto
- **Machine Translation**: traducción automática (motivó attention)
- **Text Summarization**: resumen de texto
- **Text Classification**: clasificación de documentos
- **Text-to-Speech**: texto a voz
- **Speech Recognition**: voz a texto

### 18. Dificultades del Lenguaje Natural

#### 18.1 Sensibilidad al Contexto
- Ejemplo: "Take your clothes off" tiene 5 significados según contexto
- El contexto importa tanto como la frase

#### 18.2 Sinónimos
- Una palabra puede tener múltiples significados
- Ejemplo: "culture" tiene 8+ significados en inglés

#### 18.3 Correferencia
- Dependencias entre palabras en una frase
- Ejemplo: "I voted for Nader because he..." (¿quién es "he"?)
- Difícil para máquinas, intuitivo para humanos

---

## PARTE 3: PIPELINE DE PROCESAMIENTO DE TEXTO

### 19. Corpus
- Nombre del dataset en NLP
- Puede ser un documento grande o muchos pequeños

### 20. Preprocesamiento
- Completamente manual
- Eliminar tags HTML
- Convertir a minúsculas
- Sacar puntuación (opcional)
- Depende del problema

### 21. Tokenización
- Pasar de texto continuo a lista de tokens
- Token puede ser: palabra, subpalabra, sílaba
- "Token" se popularizó con los LLMs

### 22. Stop Words Removal (Opcional)
- Eliminar palabras sin relevancia (el, la, de, en...)
- Reduce tamaño del vocabulario
- Ya no se usa en aplicaciones modernas

### 23. Stemming (Opcional)
- Reducir palabras a su raíz
- Puede dejar raíces que NO existen en el idioma
- Ejemplo: dancing → danc
- Ventajas: simplicidad, velocidad
- Desventaja: texto incomprensible

### 24. Lemmatization (Opcional)
- Reducir palabras a forma gramatical válida
- Las raíces SÍ existen en el idioma
- Ejemplo: dancing → dance
- Preserva legibilidad

### 25. Stemming vs Lemmatization
- Específico por idioma
- Buen detector en inglés puede ser pésimo en español
- Implementados en Python (sklearn, NLTK)
- Alguien lo hizo manual una vez, hoy usamos librerías

---

## PARTE 4: VECTORIZACIÓN DE TEXTO

### 26. Necesidad de Vectorizar
- No podemos trabajar con strings directamente
- Debemos transformar texto a números/vectores
- **Parte más importante** de aplicaciones modernas

### 27. Bag of Words (BoW)
- Forma más sencilla de vectorizar
- Tabla: filas=documentos, columnas=palabras, valores=frecuencias
- **Se pierde**: orden, semántica, similitud, contexto
- Funciona bien para: spam detection, sentiment analysis simple

### 28. TF-IDF (Term Frequency - Inverse Document Frequency)

#### TF (Term Frequency)
- Bag of Words normalizado por fila
- TF = (veces que aparece) / (total de tokens en documento)

#### IDF (Inverse Document Frequency)
- Mide cuán raro es un token en el corpus
- IDF = log(total documentos / documentos que contienen token)
- Token en todos los documentos → IDF = 0 (no aporta información)
- Token raro → IDF alto (aporta mucha información)

#### TF-IDF
- TF × IDF
- Normalización opcional (norma L1 o L2)

### 29. Label Encoding
- Asignar número a cada token (A=1, B=2, C=3...)
- **Problema**: diferencias numéricas sin significado
- Mala idea

### 30. One-Hot Encoding
- Vector del tamaño del vocabulario
- Un 1 en posición de la palabra, resto 0s
- **Problemas**: vector gigante, sparse, sin semántica
- Palabras similares tienen vectores completamente distintos
- También mala idea

---

## PARTE 5: WORD EMBEDDINGS

### 31. Concepto de Embedding
- Año: 2013 (Word2Vec)
- "Embedding" = "encaje" en español
- Preserva propiedades del texto original

### 32. Propiedades Deseadas
- **Baja dimensión**: 100-300 en lugar de 10,000
- **Denso**: sin ceros, todos valores significativos
- **Aprendido de datos**: no predefinido
- **Preserva estructura semántica**

### 33. Propiedades Semánticas
- Direcciones con significado gramatical
- Ejemplo famoso: king - man + woman ≈ queen
- Palabras similares → vectores cercanos

### 34. Entrenar Embeddings
- **Opción 1**: Entrenar desde cero para tu problema
- **Opción 2**: Usar preentrenados (Word2Vec, GloVe, FastText...)

### 35. Word2Vec - Dos Métodos

#### CBOW (Continuous Bag of Words)
- Dado el contexto, predecir palabra central
- Ventana de texto, tapar palabra del medio
- Predecir cuál es

#### Skip-gram
- Dada palabra central, predecir contexto
- Al revés de CBOW
- Parece más difícil (una palabra → muchos contextos)

### 36. Aprendizaje Auto-supervisado
- No necesita etiquetas manuales
- Los datos se etiquetan solos
- Ground truth: la palabra que tapaste (ya la conocías)

### 37. Arquitectura de Red Word2Vec
- 2 capas (shallow, no deep learning)
- Input: One-Hot (tamaño vocabulario)
- Hidden: Embedding (ej: 300 dimensiones, SIN activación)
- Output: Softmax (tamaño vocabulario)

### 38. Cómo Funciona
- Multiplicar One-Hot × matriz = seleccionar columna
- Cada columna de la matriz = embedding de una palabra
- Después de entrenar: quedarse solo con la matriz de embedding

### 39. Función de Pérdida
- Categorical Cross-Entropy (clasificación multiclase)
- Para CBOW y Skip-gram

### 40. Word2Vec NO Usa Orden
- No importa si palabras del contexto van antes o después
- Solo importa QUÉ palabras están en el contexto

### 41. Similitud con Autoencoders
- Estructura: grande → chiquito → grande
- Nos quedamos con el "encoder" (embedding)
- Espacio latente de 300 dimensiones

### 42. Visualización de Embeddings
- PCA para reducir 300D a 2D/3D
- t-SNE (otra técnica)
- Herramientas: Word Embedding Playground

### 43. Por Qué Son Relevantes
- Respetan similitud semántica
- Propiedades geométricas = propiedades semánticas
- "No son numeritos cualesquiera"
- Consumidos por: redes recurrentes, Transformers

---

## AVISOS ADMINISTRATIVOS

- Entrega próxima: cuestionario (con Martín)
- Martín preparará presentación sobre arquitecturas modernas de CV

---

## REFERENCIAS MENCIONADAS

### Papers
- ResNet (2016): 9 páginas, "se lee bien"
- Word2Vec (2013): link en las diapositivas

### Libros
- Libro de Alice: ResNets resumidas en 3-4 páginas

### Herramientas
- Word Embedding Playground / Projector
- Implementaciones en Python: sklearn, NLTK, spaCy

### Embeddings Preentrenados
- Word2Vec (Google, Wikipedia)
- GloVe (Stanford)
- "2-3 más famosos"

---

## POSIBLES PREGUNTAS DE PARCIAL (Mencionadas por el Profesor)

---

### ⚠️ PREGUNTA CLAVE MENCIONADA POR EL PROFESOR ⚠️

> *"A mí haciendo las diapos se me ocurrió una pregunta de parciales que era mostrar un grafiquito de estos y decir, 'Bueno, ¿cuál tiene residual connections?'"*
>
> Un estudiante dijo: "La retiro para que no la uses en el parcial."
>
> El profesor respondió: "Dale. Buenísimo. Qué retirada, qué borrada del registro."

---

### 📝 PREGUNTA:

**"Se muestran dos gráficos de entrenamiento: uno compara una red de 18 capas vs una de 34 capas, y otro compara las mismas arquitecturas pero con una modificación. ¿Cuál de los dos gráficos corresponde a redes con residual connections?"**

---

### ✅ RESPUESTA:

La red que tiene residual connections es aquella donde **la red más profunda (34 capas) tiene MEJOR rendimiento que la red menos profunda (18 capas)**, tanto en training como en validación. Si observamos que la red de más capas tiene **PEOR error de entrenamiento** que la de menos capas, entonces esa red **NO tiene residual connections**, porque está sufriendo el problema de **vanishing gradient**: los gradientes se hacen tan pequeños al retropropagar por tantas capas que las primeras capas no se actualizan correctamente, y el modelo no puede aprender bien aunque tenga más capacidad expresiva. Esto **NO es sobreajuste** (porque también le va mal en training), sino un **problema de optimización**. Con residual connections, la suma "+x" mantiene derivadas constantes de 1, permitiendo que los gradientes fluyan hacia atrás y las capas iniciales se actualicen, por lo que agregar más capas SÍ mejora el rendimiento.

---

### Otras posibles preguntas:

2. Identificar sobreajuste vs problema de optimización
   - Sobreajuste: bueno en train, malo en validación
   - Problema de optimización: malo en train Y validación

3. Errores intencionales en tablas de TF-IDF (columnas duplicadas, valores incorrectos)

4. Cálculos de IDF
