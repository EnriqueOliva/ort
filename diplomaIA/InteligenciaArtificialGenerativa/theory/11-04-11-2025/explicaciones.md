# Explicación de Temas - Clase del 11-04-2025

## La Gran Pregunta: ¿Cómo Sabemos Si Nuestro Modelo Es Bueno?

Esta clase marca el cierre del curso y trata un tema fundamental: **la evaluación de modelos generativos**. Ya aprendimos a construir VAEs, GANs, modelos de difusión y autorregresivos. Ahora viene la pregunta difícil: **¿cómo medimos qué tan buenos son?**

Como dijo el profesor: "La definición de métricas para la evaluación de los modelos generativos es un área activa de investigación y avanzar en estas métricas es un desafío en sí mismo, independientemente de avanzar en los modelos."

Es decir, **medir la calidad es tan difícil como crear los modelos mismos**.

---

## ¿Por Qué Es Tan Difícil Evaluar Modelos Generativos?

### La Diferencia Con Modelos Discriminativos

En los modelos que ya conoces (clasificación, regresión):

```
Dato → Modelo → Predicción
         ↓
    Comparar con etiqueta real → Precisión, Accuracy, F1-Score
```

**Es fácil**: tienes una etiqueta verdadera. Si el modelo dice "gato" y la etiqueta dice "gato", acertó. Si dice "perro" y era "gato", falló. Fin de la historia.

### El Problema de los Modelos Generativos

En modelos generativos:

```
Ruido → Modelo → Nueva imagen de gato
         ↓
    ¿Es un gato? ¿Se parece a los datos reales? ¿Es diverso?
```

**No hay una etiqueta correcta**. No existe "la imagen correcta de gato" con la cual comparar.

Como explicó el profesor: "Nosotros no queremos saber si nuestro modelo acertó a un dato, sino que queremos saber si nuestro modelo caracterizó adecuadamente la distribución."

### Ejemplo Concreto

Imagina que entrenas un modelo con 1000 fotos de perros. Tu modelo genera estas imágenes:

**Modelo A:**
- Genera 100 imágenes perfectas de UN SOLO perro específico
- Todas idénticas, parecen fotos reales

**Modelo B:**
- Genera 100 imágenes de distintos perros
- Algunas tienen pequeños artefactos (errores visuales)

**¿Cuál es mejor?**

- Modelo A tiene **alta fidelidad** (parecen reales) pero **baja diversidad** (solo un perro)
- Modelo B tiene **alta diversidad** (muchos perros) pero **fidelidad media** (algunos errores)

**No hay una respuesta única**. Depende de para qué necesites el modelo.

---

## Los Dos Ejes Fundamentales: Fidelidad y Diversidad

### Eje 1: Fidelidad

**¿Qué tan realistas son las muestras?**

- Una imagen fiel parece una foto real
- No tiene artefactos, ruido o deformaciones
- Si muestras la imagen a una persona, no distingue que es falsa

### Eje 2: Diversidad

**¿Qué tanto cubre la variedad del conjunto de datos?**

- Si tus datos tienen perros de muchas razas, ¿tu modelo genera muchas razas?
- Si tus datos tienen gatos negros, blancos, rayados... ¿tu modelo genera todos?
- ¿O solo genera gatos negros perfectos?

### Los Dos Extremos (Ambos Son Malos)

**Modelo muy fiel pero poco diverso:**
- Reproduce fotos reales perfectas
- Pero repite los mismos patrones una y otra vez
- **Problema**: Mode collapse (colapso de modas) - común en GANs

**Modelo muy diverso pero poco fiel:**
- Genera mucha variedad
- Pero con artefactos, ruido, imágenes que claramente se ven falsas
- **Problema**: No sirve porque las imágenes son malas

**Un buen modelo equilibra ambos aspectos.**

---

## Diferencias Entre Arquitecturas

El profesor mencionó que cada arquitectura tiene sus fortalezas y debilidades:

### VAEs (Variational Autoencoders)

**Fortaleza:** Amplia cobertura de modos (diversidad)
**Debilidad:** Muestras borrosas (baja fidelidad)

Es como tener un artista que sabe dibujar muchos tipos de gatos, pero todos sus dibujos están un poco desenfocados.

### GANs (Generative Adversarial Networks)

**Fortaleza:** Alta fidelidad (imágenes muy realistas)
**Debilidad:** Colapso de modos (baja diversidad)

Es como tener un artista que dibuja UN gato perfecto, fotorrealista, pero siempre el mismo.

### Modelos de Difusión

**Fortaleza:** Buen balance entre fidelidad y diversidad
**Debilidad:** Más lentos de muestrear

Es como tener un artista que dibuja bien y variado, pero tarda mucho en cada dibujo.

### LLMs (Language Models)

**Fortaleza:** Coherencia contextual, sintácticamente correctos
**Debilidad:** La semántica a veces diverge de la realidad factual (alucinaciones)

Es como tener un escritor que escribe muy bien, con oraciones perfectas, pero a veces inventa hechos.

---

## El Problema Fundamental: ¿Qué Medimos?

### No Podemos Comparar Distribuciones Directamente

En teoría, queremos:

```
Medir distancia entre P_data (distribución real) y P_θ (distribución del modelo)
```

**Problema 1:** P_data no es accesible

No tenemos "la máquina universal que genera gatos". Solo tenemos un muestreo (nuestro dataset de fotos).

Como dijo el profesor: "Cuando yo tengo una foto de un gato, no solo necesito una cámara y un gato, necesito el proceso del universo que me generó ese dato, que me generó esa luz en ese momento y que me dio una cámara con un cierto lente para que esa imagen quede capturada."

**Problema 2:** Las distancias en alta dimensión son difíciles de estimar

Una imagen de 256x256 píxeles RGB tiene 256×256×3 = 196,608 dimensiones. Calcular distancias en espacios de 196,608 dimensiones es computacionalmente muy difícil.

### La Solución: Comparar Conjuntos de Muestras

En vez de comparar distribuciones completas, comparamos:
- Un conjunto de imágenes reales (del dataset)
- Un conjunto de imágenes generadas (del modelo)

Y medimos qué tan parecidos son estos conjuntos.

---

## Métricas Matemáticas: Las Distancias Entre Distribuciones

### Diferencia Entre Métrica y Función de Pérdida

**IMPORTANTE:** El profesor aclaró esto porque genera confusión:

**Función de pérdida (loss):** Lo que minimizamos durante el entrenamiento
**Métrica:** Lo que medimos para evaluar un modelo ya entrenado

Puedes entrenar con una cosa y evaluar con otra.

**Ejemplo:**
- Entrenas un VAE minimizando KL divergence
- Evalúas el VAE ya entrenado con FID (una métrica diferente)

Como explicó el profesor: "Una cosa es cómo el modelo aprende, otra cómo lo evaluamos. A veces coinciden, pero quiero que se queden como por separado con esos conceptos."

### KL Divergence (Kullback-Leibler)

**¿Qué es?** Una medida de qué tan diferentes son dos distribuciones.

**Fórmula:**
```
KL(P_data || P_θ) = ∫ P_data(x) × log(P_data(x) / P_θ(x)) dx
```

**Propiedades:**
- KL ≥ 0 siempre
- KL = 0 solo si las distribuciones son idénticas
- **No es simétrica**: KL(P||Q) ≠ KL(Q||P)

**Traducción simple:** "Cuánto se equivoca el modelo P_θ cuando la realidad es P_data"

**Problema:** P_data no es conocida exactamente, solo tenemos muestras.

### Jensen-Shannon Divergence

**¿Qué es?** El promedio simétrico de dos KL.

**Ventaja:** Es simétrica (a diferencia de KL)

**Uso:** Las GANs originales optimizan esta distancia (según algunos trabajos teóricos).

### Otras Distancias (Solo Conocer Nombres)

El profesor mencionó que existen otras, solo para que no nos asustemos si las vemos:

**Wasserstein Distance (Earth Mover's Distance):**
- Mide cuánto "trabajo" lleva transformar una distribución en otra
- Usada en Wasserstein GANs (WGANs)

**MMD (Maximum Mean Discrepancy):**
- Otra forma de medir diferencias entre distribuciones
- Usada en variantes de GANs

**Consejo del profesor:** "Es como los Pokémones, ¿no? Cuantos más ven, menos se asustan si aparece uno nuevo en un paper."

### ¿Cómo Se Calculan en Práctica?

El profesor explicó:

1. Generas una muestra de datos reales (de tu dataset)
2. Generas una muestra con tu modelo
3. Comparas las distribuciones de ambas muestras
4. Calculas la distancia

**Importante:** Una distancia baja no siempre significa que el modelo sea bueno en fidelidad Y diversidad. Puede tener mode collapse y aún así tener una distancia baja.

Como advirtió el profesor: "No siempre una de estas métricas baja significa que el modelo sea un buen modelo, que tenga baja... que tenga alta fidelidad y alta diversidad. Hay modelos que a veces optimizan estas métricas con un mode collapse."

---

## Métricas Para Imágenes: Inception Score y FID

### Inception Score (IS)

**Idea central:** Usar un clasificador preentrenado (Inception) para medir calidad.

**¿Cómo funciona?**

1. Tomas imágenes generadas por tu modelo
2. Las pasas por el modelo Inception (red preentrenada en ImageNet)
3. Inception te da probabilidades de clases para cada imagen
4. Calculas una KL divergence especial

**Fórmula:**
```
IS = Esperanza[ KL( P(y|x) || P(y) ) ]
```

Donde:
- `P(y|x)` = probabilidad que Inception asigna a cada clase dado x
- `P(y)` = probabilidad marginal sobre todas las clases

**¿Qué mide?**

- **Alta IS:** Cada imagen tiene una predicción confiada (ej: 95% "perro", 5% otras)
  Y hay variedad de clases predichas
- **Baja IS:** Las predicciones son difusas (ej: 33% "perro", 33% "gato", 33% "auto")
  O todas las imágenes son de la misma clase

**Traducción simple:**

Si tu modelo genera:
- Imagen 1: Inception dice 98% "perro" → Confianza alta
- Imagen 2: Inception dice 97% "gato" → Confianza alta
- Imagen 3: Inception dice 95% "auto" → Confianza alta
- **Hay diversidad de clases** → IS alto

Si tu modelo genera:
- Imagen 1: Inception dice 50% "perro", 50% "gato" → Confusión
- Imagen 2: Inception dice 40% "auto", 60% ruido → Confusión
- **Inception está confundido** → IS bajo

**Problemas:**

1. **Solo funciona para el dominio de Inception**
   - Inception fue entrenado con ImageNet (perros, gatos, objetos cotidianos)
   - Si generas imágenes médicas, Inception no sabe qué hacer

2. **No siempre correlaciona con percepción humana**
   - A veces un humano dice "estas imágenes son horribles"
   - Pero IS dice que son buenas

### FID (Fréchet Inception Distance)

**Idea central:** Comparar representaciones internas de Inception entre datos reales y generados.

**¿Cómo funciona?**

1. Tomas imágenes reales
2. Tomas imágenes generadas
3. Pasas AMBAS por Inception hasta la **penúltima capa**
4. Esa capa te da un "embedding" (vector de características)
5. Calculas media y covarianza de embeddings reales
6. Calculas media y covarianza de embeddings generados
7. Mides la distancia de Fréchet entre estas distribuciones

**¿Qué es un embedding?**

Es una representación del dato en un espacio de menor dimensión.

**Ejemplo:**
- Imagen original: 256×256×3 = 196,608 dimensiones
- Embedding de Inception: 2048 dimensiones

**Analogía:** Es como resumir una película de 2 horas en un párrafo de 10 líneas. Pierdes detalles, pero capturas la esencia.

**¿Por qué usar embeddings?**

Como explicó el profesor: "Comparar imágenes en su espacio dimensional original no es tan fácil. Entonces, estas ideas lo que hacen es decir: yo puedo proyectar la imagen en algún lugar y de ahí comparar."

**La intuición:**

Si Inception fue bien entrenado, aprendió a "resumir" imágenes de manera que:
- Perros similares quedan cerca en el espacio de embeddings
- Gatos similares quedan cerca
- Perros y gatos quedan lejos

Entonces:
- Si tus imágenes generadas proyectan en el mismo lugar que las reales → FID bajo → Buen modelo
- Si tus imágenes generadas proyectan lejos → FID alto → Mal modelo

**Fórmula (no memorizar):**
```
FID = ||μ_real - μ_gen||² + Tr(Σ_real + Σ_gen - 2(Σ_real × Σ_gen)^(1/2))
```

Donde:
- μ = media de los embeddings
- Σ = matriz de covarianza

**Traducción:** Distancia entre dos distribuciones gaussianas en el espacio de embeddings.

**Interpretación:**

- **FID bajo (ej: 10):** Imágenes generadas muy parecidas a las reales
- **FID alto (ej: 200):** Imágenes generadas muy diferentes

**Ventaja sobre IS:** Sí compara contra datos reales (IS solo mira datos generados).

**Problemas (los mismos de IS):**

1. Depende de Inception → Solo sirve para su dominio
2. No siempre correlaciona perfectamente con percepción humana

### ¿Qué Hacer Si Mis Datos No Son Del Dominio de Inception?

El profesor dio una sugerencia muy práctica:

"Si existe un modelo de referencia preentrenado en el dominio que estoy usando, puede ser interesante meter datos reales por ahí, meter datos generados y ver dónde caen."

**Ejemplo:**

Si trabajas con imágenes médicas:
1. Busca un modelo preentrenado en imágenes médicas
2. Proyecta tus datos reales → obtén embeddings
3. Proyecta tus datos generados → obtén embeddings
4. Mide distancia (puede ser Euclidiana simple)

**Importante:** Siempre complementar con evaluación humana. No confiar ciegamente en métricas.

### Otras Técnicas Para Imágenes

El profesor mencionó brevemente:

**Precision-Recall Curves para Embeddings:**
- Hay trabajos en NeurIPS que proponen visualizar TR2 (precision-recall curves) en el espacio de embeddings
- No lo revisó en detalle, pero dejó la referencia

---

## Métricas Para Texto: Perplexity, BLEU, ROUGE

### Perplexity

**¿Qué mide?** Qué tanta probabilidad le asigna un modelo a una secuencia real.

**Fórmula:**
```
Perplexity = exp( -1/N × Σ log P(palabra_i | palabras anteriores) )
```

**Traducción simple:** "¿Qué tan sorprendido está el modelo por los datos reales?"

- **Perplexity bajo:** El modelo esperaba esas palabras → Buen modelo
- **Perplexity alto:** El modelo está sorprendido → Mal modelo

**Ejemplo:**

Texto real: "El gato negro duerme"

**Modelo A:**
- P("El") = 0.9
- P("gato"|"El") = 0.8
- P("negro"|"El gato") = 0.7
- P("duerme"|"El gato negro") = 0.85
- **Perplexity bajo** → Modelo A es bueno

**Modelo B:**
- P("El") = 0.1
- P("gato"|"El") = 0.2
- P("negro"|"El gato") = 0.15
- **Perplexity alto** → Modelo B está sorprendido, es malo

**Ventaja:** Es intrínseca al modelo. No necesitas generar texto, solo calcular probabilidades.

**Desventaja:** No evalúa coherencia global ni factualidad. Un modelo puede tener baja perplexity pero generar texto redundante o sin sentido a largo plazo.

Como aclaró el profesor: "Equivale al exponencial de la entropía cruzada promedio. Cuanto menor es, más alta la probabilidad asignada a las palabras reales. Es una métrica intrínseca, usa las probabilidades del modelo, no necesita generar texto. No evalúa coherencia global ni factualidad."

### BLEU (Bilingual Evaluation Understudy)

**¿Qué mide?** Coincidencia entre texto generado y referencias.

**Uso original:** Traducción automática.

**Idea:** Contar cuántos n-gramas del texto generado aparecen en las referencias.

**¿Qué es un n-grama?**

- **Unigrama (n=1):** Una palabra → "gato", "negro", "duerme"
- **Bigrama (n=2):** Dos palabras → "gato negro", "negro duerme"
- **Trigrama (n=3):** Tres palabras → "el gato negro"

**Fórmula (simplificada):**
```
BLEU = BP × exp( Σ w_n × log(P_n) )
```

Donde:
- `P_n` = precisión de n-gramas (cuántos coinciden)
- `w_n` = peso para cada tamaño de n-grama
- `BP` = penalización por brevedad (si el texto es muy corto)

**Ejemplo del profesor:**

Referencia: "El gato negro duerme"
Generado: "El gato duerme"

**Unigramas:**
- "El" ✓ está
- "gato" ✓ está
- "duerme" ✓ está
- **Precisión unigramas:** 3/3 = 100%

**Bigramas:**
- "El gato" ✓ está
- "gato duerme" ✗ NO está (en referencia debería ser "gato negro")
- **Precisión bigramas:** 1/2 = 50%

**Penalización por brevedad:**
- Longitud generado (C) = 3
- Longitud referencia (R) = 4
- C < R → se aplica penalización
- BP = exp(1 - 4/3) ≈ 0.71

**BLEU final:** Combinación de todo → valor entre 0 y 1

**Interpretación:**
- **BLEU alto:** Muchas coincidencias
- **BLEU bajo:** Pocas coincidencias o texto muy corto

**Problemas:**

1. **No captura sinonimia**
   - Referencia: "El perro come"
   - Generado: "El can se alimenta"
   - **BLEU = 0** (no hay coincidencias), pero semánticamente es correcto

2. **Puede favorecer modelos con overfitting**
   - Si tu modelo genera exactamente las referencias, BLEU = 100%
   - Pero eso puede ser overfitting

Como criticó el profesor: "Las métricas para ver la calidad de los modelos generativos no dicen tanto realmente... son mecanismos de pattern matching y conteo."

### ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

**¿Qué mide?** Similar a BLEU, pero enfocado en recall (cobertura).

**Diferencia con BLEU:**
- BLEU: Precisión → "¿Cuánto de lo generado está en la referencia?"
- ROUGE: Recall → "¿Cuánto de la referencia está en lo generado?"

**Fórmula (simplificada):**
```
ROUGE-N = (n-gramas en común) / (n-gramas en referencia)
```

**Ejemplo:**

Referencia: "El gato negro duerme en la cama"
Generado: "El gato negro duerme"

**ROUGE-1 (unigramas):**
- Unigramas en referencia: 6 (El, gato, negro, duerme, en, la, cama)
- Unigramas en común: 4 (El, gato, negro, duerme)
- **ROUGE-1 = 4/6 = 0.67**

**Interpretación:**
- **ROUGE alto:** El generado cubre mucho de la referencia
- **ROUGE bajo:** El generado cubre poco

**Uso:** Resúmenes de texto (queremos que el resumen cubra los puntos clave).

**Variantes mencionadas por el profesor:**

**ROUGE-L:** Basada en la subsecuencia común más larga (Longest Common Subsequence).

Ejemplo:
- Referencia: "El gato negro duerme"
- Generado: "El gato duerme"
- LCS = "El gato" (longitud 2) o "gato duerme" (depende del cálculo)

### Limitaciones de BLEU y ROUGE

Como dijo el profesor: "Las métricas para ver la calidad de los modelos generativos no dicen tanto realmente... son mecanismos de pattern matching y conteo."

**Problemas comunes:**
1. No capturan semántica (solo coincidencias literales)
2. No miden coherencia global
3. Pueden optimizarse fácilmente con trucos

**Consejo:** Usar estas métricas como **comparativas**, no como verdades absolutas.

---

## Métricas Basadas en Embeddings: BERTScore, CLIPScore

### El Problema de BLEU/ROUGE

BLEU y ROUGE solo comparan palabras exactas. No entienden significado.

**Ejemplo:**
- Referencia: "El perro está feliz"
- Generado: "El can está alegre"

BLEU = 0 (no hay coincidencias), pero semánticamente es casi idéntico.

### La Solución: Embeddings

**¿Qué es un embedding?** Una representación vectorial del texto que captura significado.

**Idea:** Palabras con significados similares tienen embeddings cercanos.

**Ejemplo (embeddings inventados):**
- "perro" → [0.8, 0.3, 0.1]
- "can" → [0.79, 0.31, 0.09]  (muy cercano)
- "gato" → [0.2, 0.8, 0.4]    (lejano)

### BERTScore

**¿Qué hace?** Usa el modelo BERT para comparar embeddings de texto.

**Proceso:**
1. Pasas el texto real por BERT → obtienes embeddings
2. Pasas el texto generado por BERT → obtienes embeddings
3. Mides similitud coseno entre embeddings

**Ventaja:** Captura sinónimos y parafraseo.

**Ejemplo:**
- Referencia: "El perro come"
- Generado: "El can se alimenta"

BLEU = 0, pero BERTScore = 0.85 (alta similitud semántica)

Como mencionó el profesor: "BERTScore usa el modelo BERT para comparar embeddings de texto generado versus reales."

### CLIPScore

**¿Qué hace?** Compara texto con imágenes usando el modelo CLIP.

**CLIP:** Modelo que aprendió a relacionar texto e imágenes.

**Uso:** Evaluar modelos texto-a-imagen (como DALL-E, Stable Diffusion).

**Proceso:**
1. Generas una imagen a partir del texto "Un gato negro en un sofá"
2. CLIP calcula qué tan bien la imagen corresponde al texto
3. Te da un score de 0 a 1

**Interpretación:**
- **Score alto:** La imagen corresponde bien al texto
- **Score bajo:** La imagen no corresponde

**Ejemplo:**

Prompt: "Un perro jugando en el parque"

**Imagen A:** Perro corriendo en pasto verde → CLIPScore = 0.92
**Imagen B:** Gato durmiendo en sofá → CLIPScore = 0.23

Como explicó el profesor: "CLIPScore hace lo mismo, pero para modelos texto-imagen."

### HPS (Human Preference Score)

**Idea:** Entrenar un modelo que predice qué le gusta a los humanos.

**Proceso:**
1. Muestras muchas imágenes a personas
2. Les preguntas: "¿Qué tan buena es esta imagen del 1 al 10?"
3. Entrenas un modelo que aprende a predecir estas calificaciones
4. Usas ese modelo para evaluar imágenes nuevas

**Ventaja:** Se aproxima a la percepción humana.

**Desventaja:** Depende de qué tan bueno fue el entrenamiento del modelo HPS.

Como mencionó el profesor: "Hay modelos de Human Preference Score que lo que hacen es modelar la calidad de una imagen usando como ground truth la preferencia de personas."

### Limitaciones Generales de Estas Métricas

Como dijo el profesor: "Métricas basadas en features dependen del modelo preentrenado. La correlación con percepción humana puede ser limitada."

**Problemas:**
1. Heredan los sesgos del modelo base
2. No siempre correlacionan con lo que un humano considera "bueno"
3. Dependen del dominio del modelo preentrenado

**Conclusión:** Siempre combinar métricas automáticas con evaluación humana.

---

## Evaluación Humana: Lo Más Confiable (Pero Caro)

### ¿Por Qué Evaluación Humana?

**Problema:** Las métricas automáticas no siempre capturan:
- Realismo
- Coherencia
- Originalidad
- Factualidad (para texto)

**Solución:** Preguntarle a personas.

### Métodos de Evaluación Humana

El profesor mencionó varios:

#### 1. Comparación Pareada (Pairwise Comparison)

**Proceso:**
1. Generas dos imágenes (de dos modelos distintos)
2. Le preguntas a una persona: "¿Cuál prefieres?"
3. Repites con muchas personas
4. El modelo que gane más veces es el mejor

**Ejemplo:**

Modelo A genera: [Imagen de perro realista]
Modelo B genera: [Imagen de perro con artefactos]

10 personas eligen → 9 prefieren A, 1 prefiere B
**Conclusión:** Modelo A es mejor

#### 2. Escalas Likert

**Proceso:**
1. Muestras una imagen
2. Le preguntas: "Del 1 al 5, ¿qué tan realista es?"
3. Promedias las respuestas

**Ejemplo:**

Imagen generada: [Gato en sofá]

- Persona 1: 4/5
- Persona 2: 5/5
- Persona 3: 3/5
- **Promedio: 4/5** → Imagen de buena calidad

#### 3. Ranking Múltiple

**Proceso:**
1. Muestras 5 imágenes
2. Pides ordenarlas de mejor a peor
3. Analizas los rankings

#### 4. Test de Turing Visual

**Proceso:**
1. Mezclas imágenes reales y generadas
2. Le preguntas a personas: "¿Cuáles son reales?"
3. Si no pueden distinguir → Tu modelo es muy bueno

**Ejemplo de uso real:**

El profesor mencionó: "¿Han usado ChatGPT? Visto que en algún momento te tiran para salir y dice: '¿Cuál te gusta más?' Está haciendo esto. Es el equipo de OpenAI intentando medir la calidad de su modelo."

### Limitaciones de la Evaluación Humana

Como explicó el profesor:

1. **Tamaño de muestra limitado:** "El tamaño de muestra y garantía de evaluadores son limitantes. Yo no puedo esto para millones de datos porque tengo que tener mucha gente y tiempo para poder ejecutar y evaluar."

2. **Costo:** "Se pueden conseguir evaluaciones de menor calidad con crowdsourcing, o se puede mejorar la calidad de la evaluación pagando a gente que es experta en el dominio, pero obviamente eso sale más caro."

3. **Subjetividad:** "Obviamente esto correlaciona directamente con la percepción humana porque tenemos a humanos haciendo las evaluaciones. La desventaja es que es más caro y está es subjetivo, pero está, la percepción humana es subjetivo."

### Métricas de Consistencia Entre Evaluadores

**Problema:** Si 5 personas evalúan la misma imagen:
- 3 dicen "excelente"
- 2 dicen "horrible"

¿Es la métrica confiable?

**Solución:** Medir acuerdo inter-evaluador (por ejemplo, con Kappa de Cohen).

Como mencionó el profesor: "Hay métricas para ver la consistencia entre evaluadores que lo que buscan es, bueno, todo bien con el ranking que me da, pero después cómo se distribuyen mis evaluadores respecto a un dato."

### Crowdsourcing vs. Expertos

**Crowdsourcing:**
- Usar plataformas como Amazon Mechanical Turk
- Muchas personas, barato
- Calidad variable

**Expertos:**
- Contratar personas expertas en el dominio (ej: médicos para imágenes médicas)
- Menos personas, caro
- Alta calidad

---

## Evaluación Orientada a Tareas (Downstream Tasks)

### El Concepto de "Tarea Río Abajo"

**Idea:** En vez de evaluar el modelo generativo directamente, evaluar cómo ayuda en una tarea específica.

**Ejemplo:**

No preguntas: "¿Qué tan buenas son estas imágenes generadas?"

Sino: "Si uso estas imágenes para entrenar un clasificador, ¿mejora la accuracy?"

### ¿Por Qué Hacer Esto?

Como explicó el profesor: "Muchas veces en algunos problemas donde yo tengo modelos generativos integrados en mi solución, no me interesa tanto la calidad del modelo generativo en sí... me interesa la calidad del resultado final en mi problema específico."

**Traducción:** Si tu modelo generativo va a ser usado para algo concreto, mide ese "algo concreto", no el modelo en sí.

### Ejemplos de Downstream Tasks

#### Ejemplo 1: Data Augmentation

**Problema:** Tienes 1000 imágenes de tumores para entrenar un clasificador.

**Solución:** Usar un modelo generativo para crear 10,000 imágenes sintéticas adicionales.

**Evaluación:**
1. Entrenar clasificador solo con 1000 reales → Accuracy = 85%
2. Entrenar clasificador con 1000 reales + 10,000 sintéticas → Accuracy = 88%

**Conclusión:** El modelo generativo ayudó (mejoró 3%)

**Nota importante del profesor:** "Yo dirigí una tesis que usaba datos generados para mejorar modelos de clasificación. Mi experiencia es que no, que si tu conjunto de datos usas datos para entrenar un modelo generativo y con eso tratas de aumentar tu conjunto de datos para después entrenar un clasificador, mi experiencia es que no tenías grandes mejoras."

**Moraleja:** No siempre funciona, pero vale la pena intentarlo.

El profesor también mencionó: "Hay un paper interesante que hace nada que habla de si los datos generados a partir de modelos generativos sirven para hacer clasificadores con estos datos."

#### Ejemplo 2: Detección de Fallos

**Problema:** Tienes un sistema que detecta fallos en logs usando un LLM.

**Evaluación:** No medir perplexity del LLM, sino:
- ¿Cuántos fallos detectó correctamente?
- ¿Cuántos falsos positivos generó?
- Accuracy, precision, recall

Como dijo el profesor: "Yo tengo un agente que lo que tiene que hacer es detectar fallos en un sistema. Yo estoy usando un gran modelo de lenguaje para que procese logs y me detecte fallos. No digo que sea la mejor idea del mundo, pero mucho de esto se hace. Capaz que no me interesa cuál es la perplexity de ese modelo de lenguaje, pero sí me interesa la accuracy."

#### Ejemplo 3: Robustez de Modelos

**Problema:** ¿Tu modelo de clasificación funciona bien con imágenes variadas?

**Proceso:**
1. Generas imágenes sintéticas con variaciones (rotaciones, ruido, etc.)
2. Pruebas tu clasificador con esas imágenes
3. Mides si el clasificador mantiene buena accuracy

**Interpretación:**
- Si accuracy se mantiene → El clasificador es robusto
- Si accuracy cae mucho → El clasificador no es robusto

**Beneficio:** El modelo generativo te ayudó a descubrir debilidades del clasificador.

### Ventajas de Evaluación por Tareas

1. **Métricas conocidas:** Accuracy, F1-score, precision, recall (del curso de machine learning)
2. **Tangibles:** Resuelves un problema concreto
3. **Justificables:** Puedes decir "Este modelo generativo mejoró mi sistema en X%"

### Desventajas

1. **Específico al dominio:** Lo que funciona en tumores no funciona en gatos
2. **Indirecto:** No mides el generativo directamente

---

## Factualidad en Modelos de Lenguaje

### El Problema de las Alucinaciones

**Alucinación:** Cuando un modelo genera texto sintácticamente correcto pero semánticamente falso.

**Ejemplo:**

Prompt: "¿Cuándo nació Napoleón?"

**Respuesta del modelo:** "Napoleón Bonaparte nació el 15 de agosto de 1769 en Ajaccio, Córcega."

**Evaluación:**
- Sintácticamente: ✓ Perfecto
- Semánticamente: ✓ Coherente
- Factualmente: ✓ Correcto (es la fecha real)

**Pero podría generar:**

"Napoleón Bonaparte nació el 3 de marzo de 1812 en París, Francia."

**Evaluación:**
- Sintácticamente: ✓ Perfecto
- Semánticamente: ✓ Coherente
- Factualmente: ✗ FALSO (es una alucinación)

### ¿Cómo Medir Factualidad?

El profesor mencionó métricas como:

**TruthfulQA:**
- Un dataset con preguntas cuyas respuestas pueden verificarse
- Mides qué porcentaje de respuestas son factualmente correctas

**MMLU (Massive Multitask Language Understanding):**
- Benchmark con preguntas de múltiples dominios
- Mides accuracy en tareas de conocimiento

**HaluEval:**
- Dataset específico para detectar alucinaciones
- Mides qué tan seguido el modelo alucina

Como mencionó el profesor: "Hay métricas que buscan factualidad, usefulness y utilidad práctica como TruthfulQA, MMLU o HaluEval que miden estas nociones de factualidad, usefulness, utilidad práctica."

### El Desafío

Como dijo el profesor: "Los LLMs no están entrenados para ser factuales, están entrenados para ser verosímiles."

**Traducción:** El objetivo del entrenamiento es generar texto que "suene convincente", no que sea verdadero.

**Problema:** Un modelo puede tener baja perplexity (suena muy natural) pero alta tasa de alucinaciones.

---

## Otras Dimensiones de Evaluación

El profesor mencionó rápidamente otras dimensiones importantes:

### 1. Equidad y Sesgo

**Pregunta:** ¿Tu modelo generativo replica sesgos de los datos?

**Ejemplo:**
- Entrenas con fotos donde "doctores" son mayormente hombres
- Tu modelo genera fotos de doctores → casi todos son hombres
- **Problema de sesgo**

Como mencionó el profesor: "Hay otras dimensiones que van a aparecer por ahí como la equidad, el sesgo, la seguridad, la escalabilidad que pueden ser interesantes."

### 2. Seguridad

**Pregunta:** ¿Tu modelo puede generar contenido dañino?

**Ejemplo:**
- Modelo de texto que genera instrucciones para construir armas
- Modelo de imágenes que genera deepfakes

### 3. Escalabilidad y Costo

**Pregunta:** ¿Cuánto cuesta usar tu modelo?

**Mediciones:**
- Tiempo de generación
- Costo computacional (GPU horas)
- Costo monetario (si usas APIs de terceros)

Como mencionó el profesor: "Nos va a pasar obviamente y es muy natural que tengan 'che, cuánto gasta este modelo, qué pasa si usas este otro'. Medir eso también es interesante en producción."

**Herramientas:** "Hay muchas veces lo que hacemos es usar una librería que nos permita taguear los usos de APIs en el caso de que el modelo sea tercero para poder saber cuánto estamos gastando, pero eso es más una especie de observabilidad o de uso, no tanto una métrica de calidad del sistema inteligente en sí."

---

## Resumen: No Hay Una Bala de Plata

### La Gran Conclusión

Como dijo el profesor: "Hay muchos niveles de evaluación, todos ellos son útiles y complementan un poco el nivel anterior, pero ninguno es una bala de plata."

**Traducción:** No existe una métrica perfecta. Necesitas combinar varias.

### Los Tres Grandes Ejes

El profesor los resumió así:

1. **Fidelidad vs. Diversidad**
   - Alta fidelidad, baja diversidad = GANs clásicas
   - Baja fidelidad, alta diversidad = VAEs
   - Balance = Modelos de difusión

2. **Precisión vs. Robustez**
   - Precisión: ¿Qué tan correcto es?
   - Robustez: ¿Funciona en casos variados?

3. **Utilidad vs. Costo**
   - Utilidad: ¿Resuelve mi problema?
   - Costo: ¿Cuánto cuesta usarlo?

### La Estrategia Recomendada

**Para el obligatorio y en general:**

1. **Métricas automáticas:** FID, IS, BLEU (según tu dominio)
2. **Evaluación humana:** Aunque sea informal (mostrar a compañeros)
3. **Downstream task:** Si aplica, medir en la tarea final
4. **Análisis cualitativo:** Mirar las salidas, buscar patrones de error

Como dijo el profesor: "Está bueno por lo menos cotejarlas, tenerlas, y muchas veces ya hay implementaciones. Ni siquiera es que tenemos que hacer nada, es entender que está en alguna librería por ahí, integrarla en el proceso de entrenamiento y dejarla registrada."

### Lo Que el Profesor Espera en el Obligatorio

**Si no usan estas métricas:**

"Si ven que nada de esto es pertinente, bueno, cuéntennos por qué. Cuéntennos qué métrica sí consideran adecuada para su caso de estudio."

**Si su dominio no es estándar:**

"Seguro si están apegados a algún paper de referencia o algún trabajo de referencia, esa métrica tiene que existir."

**Lo importante:** Justificar las decisiones, no solo aplicar métricas ciegamente.

Como enfatizó el profesor: "Lo que está bueno también que se lleven es el recurso: evalúo, tengo alguna evaluación cualitativa, alguna evaluación cuantitativa que pueda sin excederme en la complejidad, y de ahí analizo, saco conclusiones, digo: 'Mira, esta métrica me sirvió, esta me parece una porquería.' Que también es válido."

---

## Consejos Prácticos del Profesor

### 1. Las Métricas Son Indicadores, No Verdades

"Si aparece algo raro, las métricas son como indicadores, son como grandes sumarizadores del comportamiento del modelo. Yo capaz que la métrica no me dice nada, no me dice nada... un día cambia la métrica y ese cambio puede estar diciéndome algo."

**Traducción:** No obsesionarse con el valor absoluto, sino con cambios y tendencias.

### 2. Siempre Complementar Con Evaluación Cualitativa

"Estaría bueno que ustedes también se metieran un chequeo, muestren algunos datos y digan: 'Bueno, che, mira, esta técnica me da esto, yo considero que cualitativamente no está bueno', o 'yo considero que cualitativamente está excelente y la métrica me da peor'."

**Traducción:** Mirar las salidas con tus propios ojos. Las métricas pueden mentir.

### 3. No Reinventar la Rueda

"Muchas veces ya hay implementaciones. Ni siquiera es que tenemos que hacer nada, es entender que está en alguna librería por ahí."

**Traducción:** Usar librerías existentes (torch-fidelity, CLIP, etc.).

### 4. El Espíritu del Curso

"Lo que está bueno también que se lleven es el recurso: evalúo, tengo alguna evaluación cualitativa, alguna evaluación cuantitativa que pueda sin excederme en la complejidad, y de ahí analizo, saco conclusiones."

**Traducción:** Experimentar, analizar, sacar conclusiones propias.

### 5. No Exagerar Con la Matemática

El profesor recordó que en el Deep Learning Book (capítulo final), los autores también dicen que evaluar modelos generativos es complejo. No es solo tu problema, es un problema de toda el área.

---

## Actualización Sobre Modelos de Difusión

Al inicio de la clase, el profesor mencionó una actualización importante:

### Simplificación del Entrenamiento

"Actualicé las slides de difusión. El paper de Denoising Diffusion Models hace una simplificación: bajo ciertas hipótesis, el Variational Lower Bound es equivalente a minimizar los mínimos cuadrados del error."

**Traducción:**

En vez de minimizar el ELBO completo (complicado), puedes:

**Minimizar:**
```
E[ ||ε - ε_θ(x_t, t)||² ]
```

Donde:
- ε = ruido real que agregaste
- ε_θ = ruido predicho por tu modelo

**Pseudocódigo del algoritmo:**

```
Para cada imagen de entrenamiento:
    1. Elegir un paso de tiempo t aleatorio
    2. Muestrear ruido ε ~ N(0, I)
    3. Crear imagen ruidosa: x_t = √(α_t) × x_0 + √(1-α_t) × ε
    4. Predecir ruido: ε_pred = modelo(x_t, t)
    5. Calcular pérdida: loss = ||ε - ε_pred||²
    6. Actualizar pesos con SGD
```

Como explicó el profesor: "Se muestra una imagen real de los datos. Se elige un paso de tiempo, con ese tiempo se calcula, se muestrea un ruido. En realidad sí, el ruido depende obviamente del cálculo del alfa, que recuerdan que el alfa en realidad era una conjunción de una serie de betas, porque teníamos aquel scheduling de ruido y eso se multiplica por una variable aleatoria epsilon. Luego el modelo predice el error, el ruido en ese dato, sabiendo de qué tiempo, cuánto tiempo en el proceso de difusión se le agregó el ruido y se minimiza la diferencia entre eso y el ruido que se mostró."

**Intuición:** "Los parámetros theta se ajustan para predecir el ruido añadido en cada paso de difusión, lo que equivale a aprender la inversa del proceso de degradación."

Esto confirma lo que vieron en la clase de difusión: en la práctica, es más simple de lo que parece teóricamente.

---

## Definiciones Para el Parcial (Máximo 2 Renglones Cada Una)

### Evaluación de Modelos Generativos

**Fidelidad:** Qué tan realistas son las muestras generadas; una imagen fiel parece una foto real sin artefactos, ruido o deformaciones.

**Diversidad:** Qué tanto cubre la variedad del conjunto de datos; un modelo diverso genera distintas modas de la distribución, no solo una repetidamente.

**Mode Collapse:** Problema de GANs donde el modelo genera solo un tipo de muestra (alta fidelidad, baja diversidad); el generador encuentra un "truco" para engañar al discriminador con una sola salida.

**Downstream Task:** Tarea río abajo; evaluar el modelo generativo no directamente, sino midiendo cómo ayuda en una tarea específica (ej: accuracy de un clasificador entrenado con datos sintéticos).

### Diferencia Métrica vs. Loss

**Métrica:** Medida para evaluar un modelo ya entrenado; no se usa para optimización, solo para reportar desempeño; mide qué tan bueno es el modelo con parámetros fijos.

**Función de Pérdida (Loss):** Función que se minimiza durante el entrenamiento con descenso del gradiente; guía la optimización ajustando parámetros del modelo.

**Importante:** Puedes entrenar con una loss y evaluar con otra métrica; no son lo mismo; una cosa es cómo el modelo aprende, otra cómo lo evaluamos.

### Distribuciones y Distancias

**P_data:** Distribución real de los datos; no es accesible directamente, solo tenemos muestras (nuestro dataset); incluye "el proceso del universo" que generó los datos.

**P_θ:** Distribución aprendida por el modelo; queremos que P_θ ≈ P_data; θ son los parámetros del modelo.

**KL Divergence:** Mide qué tan diferentes son dos distribuciones; KL(P||Q) = ∫ P(x) log(P(x)/Q(x)); no es simétrica (KL(P||Q) ≠ KL(Q||P)).

**Jensen-Shannon Divergence:** Promedio simétrico de dos KL; es simétrica y se usa en GANs originales según trabajos teóricos.

**Wasserstein Distance:** Mide cuánto "trabajo" lleva transformar una distribución en otra (Earth Mover's Distance); usada en WGANs.

**MMD (Maximum Mean Discrepancy):** Otra norma entre distribuciones; se puede estimar a partir de muestras; usada en variantes de GANs.

**Problema de Alta Dimensión:** Calcular distancias entre distribuciones en espacios de 100,000+ dimensiones (imágenes) es computacionalmente muy difícil o imposible.

### Métricas Para Imágenes

**Inception Score (IS):** Usa Inception preentrenado para medir calidad; calcula KL entre P(y|x) (predicción confiada por imagen) y P(y) (distribución marginal sobre clases); IS alto = imágenes con predicciones confiadas y variedad de clases.

**FID (Fréchet Inception Distance):** Compara embeddings de Inception (penúltima capa) entre datos reales y generados; mide distancia de Fréchet entre dos distribuciones gaussianas (medias y covarianzas); FID bajo = imágenes generadas parecidas a reales.

**Embedding:** Proyección de un dato en un espacio de menor dimensión que captura características esenciales; ej: imagen de 256×256×3 (196,608 dims) → vector de 2048 dimensiones.

**Por Qué Usar Embeddings:** Comparar imágenes en su espacio original (196,608 dimensiones) es difícil computacionalmente; proyectar a espacio menor facilita cálculo de distancias y captura la esencia del dato.

**Limitación de IS/FID:** Dependen de Inception, solo funcionan bien en dominio de Inception (ImageNet); si generas imágenes médicas, Inception no sabe qué hacer y métricas no tienen sentido.

### Métricas Para Texto

**Perplexity:** Exponencial de la entropía cruzada promedio; mide qué tanta probabilidad le asigna el modelo a secuencias reales; perplexity bajo = el modelo esperaba esas palabras (buen modelo).

**BLEU:** Mide coincidencia de n-gramas entre texto generado y referencias; BLEU alto = muchas coincidencias literales; incluye penalización por brevedad (BP) si el texto es muy corto.

**N-grama:** Secuencia de n palabras consecutivas; unigrama = 1 palabra ("gato"), bigrama = 2 palabras ("gato negro"), trigrama = 3 palabras ("el gato negro").

**ROUGE:** Similar a BLEU pero enfocado en recall (cobertura); ROUGE = (n-gramas en común) / (n-gramas en referencia); usado en resúmenes de texto.

**ROUGE-L:** Variante basada en la subsecuencia común más larga (Longest Common Subsequence); mide la secuencia continua más larga que coincide.

**Limitación BLEU/ROUGE:** Solo comparan palabras exactas (pattern matching), no capturan semántica; "perro" vs "can" = 0% coincidencia aunque sean sinónimos; pueden optimizarse con overfitting.

### Métricas Basadas en Embeddings

**BERTScore:** Usa BERT para comparar embeddings de texto; mide similitud coseno entre embeddings de texto real y generado; captura sinónimos y parafraseo.

**CLIPScore:** Compara texto con imágenes usando CLIP; evalúa modelos texto-a-imagen (DALL-E, Stable Diffusion); score alto = imagen corresponde bien al texto.

**CLIP:** Modelo preentrenado que aprendió a relacionar texto e imágenes en un espacio común; textos similares semánticamente a imágenes quedan cercanos en el espacio de embeddings.

**HPS (Human Preference Score):** Modelo entrenado para predecir qué le gusta a los humanos; aprende de calificaciones humanas (ground truth) y luego evalúa imágenes nuevas automáticamente.

**Limitación Embeddings:** Dependen del modelo preentrenado (BERT, CLIP); heredan sesgos del modelo base; no siempre correlacionan con percepción humana real.

### Evaluación Humana

**Comparación Pareada:** Mostrar dos salidas y preguntar cuál prefieren; el modelo que gane más veces en las comparaciones es mejor.

**Escalas Likert:** Pedir calificar del 1 al 5 (o 1 al 10) en algún criterio (realismo, coherencia); promediar respuestas de múltiples evaluadores.

**Ranking Múltiple:** Mostrar varias salidas (ej: 5 imágenes) y pedir ordenarlas de mejor a peor; analizar los rankings resultantes.

**Test de Turing Visual:** Mezclar imágenes reales y generadas; preguntar a personas cuáles son reales; si no pueden distinguir, el modelo es muy bueno.

**Limitaciones Evaluación Humana:** Costosa (tiempo y dinero), no escalable (no puedes evaluar miles de muestras), subjetiva (personas diferentes tienen preferencias diferentes); tamaño de muestra limitado.

**Crowdsourcing:** Usar plataformas como Amazon Mechanical Turk para conseguir evaluaciones baratas; muchas personas pero calidad variable.

**Expertos:** Contratar personas expertas en el dominio (ej: médicos para imágenes médicas); más caro pero mayor calidad; menos personas.

**Consistencia Entre Evaluadores:** Métricas como Kappa de Cohen para medir acuerdo inter-evaluador; importante saber si evaluadores están de acuerdo o muy dispersos.

### Evaluación por Tareas

**Data Augmentation:** Usar datos sintéticos del modelo generativo para aumentar dataset de entrenamiento; evaluar si mejora accuracy del clasificador final.

**Robustez:** Usar datos sintéticos con variaciones (rotaciones, ruido) para probar si clasificador mantiene accuracy; si cae mucho, no es robusto.

**Ventaja Downstream:** Métricas conocidas (accuracy, F1, precision, recall del curso de ML), tangibles (resuelves problema concreto), justificables (puedes cuantificar mejora porcentual).

**Desventaja Downstream:** Específico al dominio (lo que funciona en tumores no funciona en gatos); indirecto (no mides el generativo directamente sino su utilidad).

### Factualidad

**Alucinación:** Cuando un modelo genera texto sintácticamente correcto y semánticamente coherente pero factualmente falso; ej: inventar fechas históricas que suenan convincentes.

**TruthfulQA:** Dataset con preguntas verificables cuyas respuestas pueden chequearse contra hechos; mide porcentaje de respuestas factualmente correctas.

**MMLU (Massive Multitask Language Understanding):** Benchmark con preguntas de múltiples dominios (historia, ciencia, etc.); mide accuracy en tareas de conocimiento.

**HaluEval:** Dataset específico para detectar alucinaciones; mide qué tan seguido el modelo inventa información falsa.

**Problema LLMs:** Entrenados para ser verosímiles (convincentes, que suenen natural), no factuales (verdaderos); pueden tener baja perplexity (texto natural) pero alta tasa de alucinaciones.

### Otras Dimensiones

**Sesgo:** Si tu modelo replica sesgos de los datos de entrenamiento; ej: generar solo doctores hombres porque dataset tenía mayoría de hombres.

**Seguridad:** Si tu modelo puede generar contenido dañino (deepfakes, instrucciones peligrosas); importante en producción.

**Costo Computacional:** Tiempo de generación, GPU horas, costo monetario si usas APIs de terceros; importante medir en producción para presupuesto.

**Observabilidad:** Usar librerías que taguen llamadas a APIs para monitorear uso y costos; más relacionado a ingeniería que a calidad del modelo.

### Conceptos de Difusión (Actualización)

**Simplificación ELBO:** Bajo ciertas hipótesis, minimizar el Variational Lower Bound es equivalente a minimizar E[||ε - ε_θ(x_t, t)||²] (mínimos cuadrados del error entre ruido real y predicho).

**Scheduling de Ruido:** Los parámetros alfa (α_t) dependen de una serie de betas (β_t); controlan cuánto ruido se agrega en cada paso del proceso de difusión.

**Intuición Difusión:** Los parámetros theta se ajustan para predecir el ruido añadido en cada paso de difusión, lo que equivale a aprender la inversa del proceso de degradación.

---

## Posibles Preguntas Para el Parcial (Con Respuestas Cortas)

### Pregunta 1: ¿Por qué es más difícil evaluar un modelo generativo que uno discriminativo?

**Respuesta:**

En modelos discriminativos existe una etiqueta correcta con la cual comparar (si predice "gato" y era "gato", acertó). En modelos generativos no hay "imagen correcta"; queremos que el modelo caracterice toda la distribución de datos, no un dato específico. Debemos medir fidelidad (qué tan reales son las muestras) y diversidad (qué tanto cubre variedad), y no hay métricas perfectas para esto. Como dijo el profesor: "Nosotros no queremos saber si nuestro modelo acertó a un dato, sino que queremos saber si nuestro modelo caracterizó adecuadamente la distribución."

### Pregunta 2: ¿Qué es mode collapse y en qué arquitectura es común?

**Respuesta:**

Mode collapse (colapso de modas) es cuando un modelo generativo genera solo un tipo de muestra en vez de capturar toda la variedad de los datos. Es común en GANs: el modelo puede generar un perro perfecto (alta fidelidad) pero siempre el mismo perro (baja diversidad). Ocurre porque el generador encuentra un "truco" para engañar al discriminador con un solo tipo de salida. Es un problema de baja diversidad a pesar de alta fidelidad.

### Pregunta 3: Explica la diferencia entre métrica y función de pérdida.

**Respuesta:**

La función de pérdida (loss) es lo que minimizamos durante el entrenamiento con descenso del gradiente; guía la optimización del modelo ajustando sus parámetros. Una métrica es lo que medimos para evaluar un modelo ya entrenado con parámetros fijos; no se usa para optimizar, solo para reportar desempeño. Puedes entrenar con una loss (ej: KL divergence) y evaluar con otra métrica (ej: FID). Como aclaró el profesor: "Una cosa es cómo el modelo aprende, otra cómo lo evaluamos."

### Pregunta 4: ¿Por qué no podemos comparar P_data y P_θ directamente?

**Respuesta:**

Dos problemas: (1) P_data no es accesible directamente, solo tenemos muestras (nuestro dataset), no el "proceso universal" que genera datos reales. Como dijo el profesor: "Cuando yo tengo una foto de un gato, no solo necesito una cámara y un gato, necesito el proceso del universo que me generó ese dato." (2) Calcular distancias en espacios de alta dimensión (ej: imágenes de 196,608 dimensiones) es computacionalmente muy difícil. Solución: comparar conjuntos de muestras reales vs. generadas en espacios de menor dimensión (embeddings).

### Pregunta 5: ¿Qué mide Inception Score y cuál es su limitación principal?

**Respuesta:**

IS mide calidad de imágenes generadas pasándolas por Inception (red preentrenada) y calculando KL entre P(y|x) (predicción confiada por imagen) y P(y) (distribución marginal sobre clases). IS alto = imágenes con predicciones confiadas (no difusas) y variedad de clases. Limitación principal: solo funciona en el dominio de Inception (ImageNet con perros, gatos, objetos); si generas imágenes médicas u otro dominio, Inception no sabe qué hacer y las métricas no tienen sentido.

### Pregunta 6: ¿Qué ventaja tiene FID sobre Inception Score?

**Respuesta:**

FID compara datos reales con generados proyectándolos en el espacio de embeddings de Inception y midiendo la distancia de Fréchet entre ambas distribuciones (medias y covarianzas). IS solo mira datos generados, no los compara directamente con reales. FID te dice si las imágenes generadas caen en el mismo lugar del espacio de embeddings que las reales. Es una comparación directa entre lo que generas y lo que existe realmente en los datos.

### Pregunta 7: ¿Por qué usamos embeddings en vez de comparar imágenes directamente?

**Respuesta:**

Una imagen de 256×256 RGB tiene 196,608 dimensiones. Comparar en ese espacio es muy difícil computacionalmente y poco interpretable. Los embeddings proyectan la imagen a un espacio menor (ej: 2048 dimensiones) que captura características esenciales. Como explicó el profesor: "Comparar imágenes en su espacio dimensional original no es tan fácil. Yo puedo proyectar la imagen en algún lugar y de ahí comparar." Si un modelo fue bien entrenado, imágenes similares quedan cerca en el espacio de embeddings, facilitando el análisis estadístico.

### Pregunta 8: ¿Qué mide perplexity y cómo se interpreta?

**Respuesta:**

Perplexity mide qué tanta probabilidad le asigna un modelo a secuencias reales. Es la exponencial de la entropía cruzada promedio. Perplexity bajo = el modelo esperaba esas palabras (buen modelo). Perplexity alto = el modelo está sorprendido por las palabras (mal modelo). Es intrínseca al modelo: solo calculas probabilidades de los datos bajo el modelo, no necesitas generar texto nuevo. No evalúa coherencia global ni factualidad, un modelo puede tener baja perplexity pero generar texto redundante o alucinado.

### Pregunta 9: ¿Cuál es la limitación principal de BLEU y ROUGE?

**Respuesta:**

Solo comparan palabras exactas (pattern matching), no capturan semántica ni sinonimia. Si la referencia dice "perro" y el generado dice "can", BLEU/ROUGE = 0% aunque sean sinónimos. Como criticó el profesor: "Son mecanismos de pattern matching y conteo." Tampoco miden coherencia global. Pueden optimizarse con trucos (generar exactamente las referencias = BLEU 100% pero overfitting). Se usan como métricas comparativas entre modelos, no como verdades absolutas. BERTScore soluciona esto usando embeddings semánticos.

### Pregunta 10: ¿Qué es una downstream task y por qué es útil para evaluación?

**Respuesta:**

Es una tarea río abajo; en vez de evaluar el modelo generativo directamente, evalúas cómo ayuda en una tarea específica. Ejemplo: usas datos sintéticos para entrenar un clasificador y mides si mejora la accuracy. Útil porque: (1) usa métricas conocidas (accuracy, F1 del curso de ML), (2) es tangible (resuelves problema concreto), (3) es justificable (puedes cuantificar mejora). Como dijo el profesor: "Me interesa la calidad del resultado final en mi problema específico." Evita dificultades de evaluar modelos generativos directamente.

### Pregunta 11: ¿Qué es una alucinación en LLMs y por qué ocurre?

**Respuesta:**

Alucinación es cuando un modelo genera texto sintácticamente correcto y semánticamente coherente pero factualmente falso (ej: inventar fechas históricas que suenan convincentes). Ocurre porque, como dijo el profesor: "Los LLMs están entrenados para ser verosímiles (convincentes), no factuales (verdaderos)." El objetivo del entrenamiento es generar texto que "suene natural", no que sea cierto. Pueden tener baja perplexity (texto muy natural) pero alta tasa de alucinaciones. Se miden con benchmarks como TruthfulQA que verifican factualidad.

### Pregunta 12: ¿Cuándo usarías evaluación humana en vez de métricas automáticas?

**Respuesta:**

Cuando las métricas automáticas no capturan lo importante: realismo, coherencia, originalidad, factualidad. Las métricas pueden dar resultados buenos pero la salida ser mala (o viceversa). Evaluación humana correlaciona directamente con percepción real, pero es costosa (tiempo y dinero), no escalable (no puedes evaluar millones de muestras) y subjetiva (diferentes personas, diferentes preferencias). Como dijo el profesor: "Obviamente esto correlaciona directamente con la percepción humana... La desventaja es que es más caro y es subjetivo." Se usa en combinación con métricas automáticas.

### Pregunta 13: ¿Qué estrategia recomendó el profesor para evaluar modelos generativos?

**Respuesta:**

Combinar varios niveles: (1) Métricas automáticas (FID, IS, BLEU según dominio) para tener números comparables, (2) Evaluación humana aunque sea informal (mostrar a compañeros), (3) Downstream task si aplica (medir en tarea final), (4) Análisis cualitativo (mirar salidas, buscar patrones de error). Como dijo: "Hay muchos niveles de evaluación, todos ellos son útiles y complementan un poco el nivel anterior, pero ninguno es una bala de plata." Justificar las decisiones, no aplicar métricas ciegamente.

### Pregunta 14: Si tus datos no son del dominio de Inception, ¿qué haces?

**Respuesta:**

Como sugirió el profesor: "Si existe un modelo de referencia preentrenado en el dominio que estoy usando, puede ser interesante meter datos reales por ahí, meter datos generados y ver dónde caen." Buscar modelo preentrenado en tu dominio (ej: modelo médico para imágenes médicas), proyectar datos reales y generados, medir distancia en espacio de embeddings. Importante: siempre complementar con evaluación cualitativa (mirar las salidas). Si no existe modelo preentrenado, usar métricas más simples o desarrollar técnica análoga adaptada a tu dominio.

### Pregunta 15: ¿Qué actualización hizo el profesor sobre modelos de difusión?

**Respuesta:**

El paper de Denoising Diffusion Models demuestra que bajo ciertas hipótesis, minimizar el ELBO (Variational Lower Bound) es equivalente a minimizar los mínimos cuadrados del error entre ruido real y ruido predicho: E[||ε - ε_θ(x_t, t)||²]. Esto simplifica mucho el entrenamiento. El pseudocódigo: elegir imagen, elegir paso t aleatorio, agregar ruido ε, predecir ruido con modelo, minimizar diferencia cuadrática, actualizar pesos con SGD. Intuición del profesor: "Los parámetros theta se ajustan para predecir el ruido añadido en cada paso de difusión, lo que equivale a aprender la inversa del proceso de degradación."

---

## Reflexión Final: El Espíritu de la Evaluación

Como cerró el profesor: "Hay muchos niveles de evaluación, todos ellos son útiles y complementan un poco el nivel anterior, pero ninguno es una bala de plata."

**Lo importante no es encontrar LA métrica perfecta (no existe), sino:**

1. **Entender qué mide cada métrica** y cuándo es apropiada
2. **Combinar múltiples fuentes de información** (automáticas, humanas, tareas)
3. **Justificar las decisiones** con análisis crítico
4. **Estar atento a cambios** en las métricas como indicadores de problemas
5. **No obsesionarse con números** sin mirar cualitativamente las salidas

En el obligatorio, lo que se espera es:
- Elegir métricas apropiadas al dominio
- Justificar por qué esas métricas (o por qué otras no sirven)
- Complementar con análisis cualitativo
- Mostrar pensamiento crítico

Como enfatizó el profesor: "Si ven que nada de esto es pertinente, bueno, cuéntennos por qué. Cuéntennos qué métrica sí consideran adecuada para su caso de estudio."

**No hay respuestas únicas, hay decisiones bien justificadas.**

Y el consejo final: "Lo que está bueno también que se lleven es el recurso: evalúo, tengo alguna evaluación cualitativa, alguna evaluación cuantitativa que pueda sin excederme en la complejidad, y de ahí analizo, saco conclusiones, digo: 'Mira, esta métrica me sirvió, esta me parece una porquería.' Que también es válido."

**La evaluación es un arte, no una ciencia exacta.**

---

## Referencias Mencionadas en Clase

El profesor dejó referencias en las slides para:
- Métricas para imágenes (IS, FID, precision-recall curves en embeddings)
- Métricas para texto (Perplexity, BLEU, ROUGE)
- Métricas basadas en embeddings (BERTScore, CLIPScore, HPS)
- Factualidad (TruthfulQA, MMLU, HaluEval)
- Papers sobre uso de datos sintéticos para clasificadores
- Deep Learning Book (capítulo final sobre evaluación de modelos generativos)
- Papers de NeurIPS sobre técnicas de visualización en espacios de embeddings

**Recomendación:** Revisar las slides en Aulas para referencias específicas según el dominio de tu obligatorio.

---

**Fin del Documento**

Este documento cubre **TODO** lo tratado en la clase del 11-04-2025. El tema central fue la evaluación de modelos generativos, un área compleja sin soluciones únicas pero con múltiples herramientas que, combinadas, permiten tener una idea sólida de la calidad de nuestros modelos. El profesor enfatizó que evaluar es tan difícil como construir los modelos, que no hay métricas perfectas, y que lo importante es justificar decisiones con pensamiento crítico.
