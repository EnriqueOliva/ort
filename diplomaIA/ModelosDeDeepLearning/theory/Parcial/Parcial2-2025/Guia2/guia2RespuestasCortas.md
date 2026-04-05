# Guía de Estudio - Parcial 2 - Respuestas Cortas (1-2 oraciones)
## Para el examen real

---

## Ejercicio 1

Considere un token de consulta $q \sim (4)$, dos claves $k_1, k_2 \sim (4)$ y dos valores $v_1, v_2 \sim (4)$:

$$q = (1, 0, 1, 0), \quad k_1 = (1, 1, 0, 0), \quad k_2 = (0, 1, 1, 0),$$
$$v_1 = (2, 0, 1, 1), \quad v_2 = (0, 1, 2, 1).$$

**1. Calcule los puntajes de atención escalada:**
$$e_i = \frac{q \cdot k_i}{\sqrt{4}}.$$

> **R:** e₁ = (1·1 + 0·1 + 1·0 + 0·0)/√4 = 1/2 = 0.5; e₂ = (1·0 + 0·1 + 1·1 + 0·0)/√4 = 1/2 = 0.5

**2. Aplique softmax a $(e_1, e_2)$ para obtener los pesos de atención.**

> **R:** α₁ = α₂ = e^0.5/(e^0.5 + e^0.5) = 0.5 (pesos iguales porque e₁ = e₂)

**3. Compute la salida:**
$$z = \sum_i \alpha_i v_i.$$

> **R:** z = 0.5·(2,0,1,1) + 0.5·(0,1,2,1) = **(1, 0.5, 1.5, 1)**

---

## Ejercicio 2

Suponga:
$$d_{\text{model}} = 512, \quad h = 8.$$

**1. Las dimensiones por cabeza $d_k$ y $d_v$ ¿están determinadas por $d_{\text{model}}$ y $h$?**

> **R:** Sí: d_k = d_v = d_model/h = 512/8 = **64**

**2. Calcule el número de parámetros de las matrices $W_Q$, $W_K$, $W_V$. Ignore los sesgos.**

> **R:** Cada una: d_model × d_model = 512 × 512 = 262,144 → Total: **786,432**

**3. Calcule los parámetros de la proyección final $W_O$.**

> **R:** d_model × d_model = 512 × 512 = **262,144**

---

## Ejercicio 3

El decodificador introduce una capa de *masked self-attention* que bloquea el acceso a tokens futuros.

**1. Explique por qué esta máscara es indispensable durante el entrenamiento, incluso si el modelo tiene acceso a la secuencia completa como referencia.**

> **R:** Evita que el modelo "haga trampa" mirando tokens futuros durante entrenamiento, simulando las condiciones de inferencia donde el futuro es desconocido.

**2. Describa qué comportamiento incorrecto aparecería si la máscara no se aplicara.**

> **R:** El modelo aprendería a copiar la respuesta directamente del futuro en lugar de aprender a predecir, resultando en incapacidad de generar durante inferencia.

**3. Compare esta restricción con el mecanismo de *teacher forcing* utilizado en RNNs. ¿Tienen el mismo propósito? ¿En qué se diferencian?**

> **R:** Teacher forcing proporciona el input correcto al decoder; la máscara oculta posiciones futuras en attention. Ambos evitan ver el futuro pero operan en niveles distintos.

**4. Considere la matriz de puntajes de atención sin normalizar para una secuencia de longitud $T = 4$:**

$$S = \begin{pmatrix} 1.2 & 0.5 & -0.3 & 2.0 \\ 0.7 & 1.0 & 0.9 & -1.0 \\ 1.5 & 0.1 & 0.2 & 0.3 \\ -0.2 & 0.4 & 1.3 & 0.8 \end{pmatrix}.$$

**a) Construya explícitamente la máscara causal $M$.**

> **R:** M = [[0, -∞, -∞, -∞], [0, 0, -∞, -∞], [0, 0, 0, -∞], [0, 0, 0, 0]]

**b) Calcule $S' = S + M$.**

> **R:** S' = [[1.2, -∞, -∞, -∞], [0.7, 1.0, -∞, -∞], [1.5, 0.1, 0.2, -∞], [-0.2, 0.4, 1.3, 0.8]]

**c) Aplique softmax a la tercera fila de $S'$ y dé los pesos normalizados.**

> **R:** softmax([1.5, 0.1, 0.2]) ≈ **(0.69, 0.17, 0.14)** (normalizado a 3 elementos)

---

## Ejercicio 4

Considere el siguiente modelo *Transformer* para traducción automática (encoder-decoder). Los hiperparámetros son:

$$\text{Vocab}_{\text{src}} = 5000, \quad \text{Vocab}_{\text{tgt}} = 6000, \quad d_{\text{model}} = 128, \quad h = 4, \quad d_{\text{ff}} = 512,$$
$$N_{\text{enc}} = 2 \text{ (capas de encoder)}, \quad N_{\text{dec}} = 2 \text{ (capas de decoder)}.$$

Cada bloque usa las siguientes componentes:

- **Input embedding (src)**: matriz $E_{\text{src}}$.
- **Output embedding (tgt)**: matriz $E_{\text{tgt}}$.
- **Positional encoding**.
- **Multi-Head Attention (MHA)** con $h = 4$ cabezas: se implementa con matrices $W_Q, W_K, W_V, W_O$, y sesgos $b_Q, b_K, b_V, b_O$ (uno por matriz).
- **Feed-Forward (FFN)**: $\text{FFN}(x) = \max(0, xW_1 + b_1) W_2 + b_2$
- **LayerNorm**: cada normalización de capa tiene parámetros $\gamma, \beta$.

Cada bloque de **encoder** está compuesto por:
1. MHA (self-attention sobre la secuencia de entrada),
2. LayerNorm,
3. FFN,
4. LayerNorm.

Cada bloque de **decoder** está compuesto por:
1. MHA *enmascarada* (self-attention sobre la secuencia de salida),
2. LayerNorm,
3. MHA *encoder–decoder* (queries de la salida, keys/values del encoder),
4. LayerNorm,
5. FFN,
6. LayerNorm.

Al final del modelo se aplica una capa lineal para producir logits sobre el vocabulario de salida con matrices $W_{\text{out}}, b_{\text{out}}$.

**1. Calcule el número de parámetros entrenables en:**

**a) una capa MHA individual (incluyendo todos sus sesgos);**

> **R:** 4 matrices (d_model×d_model) + 4 sesgos (d_model) = 4×128² + 4×128 = 65,536 + 512 = **66,048**

**b) un bloque FFN individual (incluyendo sesgos);**

> **R:** W₁(128×512) + b₁(512) + W₂(512×128) + b₂(128) = 65,536 + 512 + 65,536 + 128 = **131,712**

**c) una operación LayerNorm individual.**

> **R:** γ(128) + β(128) = **256**

**2. Usando la estructura de cada bloque, calcule el número de parámetros de:**

**a) un bloque de encoder completo;**

> **R:** MHA + 2×LN + FFN = 66,048 + 2×256 + 131,712 = **198,272**

**b) un bloque de decoder completo.**

> **R:** 2×MHA + 3×LN + FFN = 2×66,048 + 3×256 + 131,712 = **264,576**

**3. Calcule el total de parámetros del modelo completo, incluyendo: embedding de entrada, embedding de salida, 2 bloques de encoder, 2 bloques de decoder, capa lineal de salida. Ignore cualquier otro posible parámetro no listado.**

> **R:** E_src(5000×128) + E_tgt(6000×128) + 2×enc + 2×dec + Linear(128×6000+6000) = 640,000 + 768,000 + 396,544 + 529,152 + 774,000 ≈ **3.1M parámetros**

**4. Compare el número de parámetros de este modelo con un Transformer que tenga $d_{\text{model}} = 256$, manteniendo todo lo demás igual. ¿Cómo escala aproximadamente el número total de parámetros con $d_{\text{model}}$?**

> **R:** Los parámetros escalan aproximadamente con O(d_model²) porque las matrices de attention y FFN son cuadráticas en d_model.

---

## Ejercicio 5

En un modelo Seq2Seq clásico, el encoder resume toda la información de la oración de entrada en un único vector de contexto.

**1. Explique por qué este diseño puede ser un cuello de botella cuando la secuencia de entrada es larga o contiene dependencias complejas.**

> **R:** Toda la información de una secuencia arbitrariamente larga debe comprimirse en un vector de tamaño fijo, perdiendo información cuando la secuencia es larga.

**2. Dé un ejemplo concreto de una situación donde se pierda información relevante debido a esta compresión.**

> **R:** En "El gato que vi ayer en el parque estaba durmiendo", al traducir "durmiendo" el modelo puede haber "olvidado" que el sujeto era "gato".

**3. Describa cómo un mecanismo de atención puede mitigar o eliminar este problema.**

> **R:** Attention permite al decoder mirar TODOS los hidden states del encoder, calculando un contexto dinámico Cᵢ diferente para cada palabra generada.

---

## Ejercicio 6

En modelos autoregresivos con decoders basados en RNNs, el proceso de entrenamiento difiere del proceso de inferencia.

**1. Describa qué información recibe el decoder durante el entrenamiento y por qué.**

> **R:** Recibe la secuencia correcta (ground truth) como input en cada paso gracias a teacher forcing, lo que estabiliza y acelera el entrenamiento.

**2. Describa qué información recibe durante la inferencia y por qué necesariamente cambia el flujo.**

> **R:** Recibe su propia predicción anterior como input, ya que no existe ground truth disponible durante generación.

**3. Explique un problema típico que aparece si el modelo se entrena usando únicamente *teacher forcing*.**

> **R:** Exposure bias: el modelo nunca aprendió a recuperarse de sus propios errores porque siempre vio inputs correctos.

**4. Mencione una solución habitual para reducir este problema.**

> **R:** Scheduled sampling: mezclar gradualmente inputs correctos con predicciones del modelo durante entrenamiento.

---

## Ejercicio 7

Para entrenar y usar un modelo Seq2Seq se introducen los tokens especiales SOS y EOS.

**1. Explique por qué el decoder necesita explícitamente el token SOS.**

> **R:** El decoder necesita un input inicial para el primer paso de generación; SOS actúa como señal de "comenzar a generar".

**2. Describa qué problema surge si no se incluye un token EOS en la secuencia objetivo.**

> **R:** El modelo no sabría cuándo parar de generar, produciendo secuencias infinitas o de longitud arbitraria.

---

## Ejercicio 8

En mecanismos de atención se calculan pesos que indican la importancia relativa de cada posición del input durante la generación de un token.

**1. Explique la interpretación probabilística de los pesos de atención.**

> **R:** Los pesos α forman una distribución de probabilidad (suman 1) sobre las posiciones de entrada, indicando la "probabilidad" de atender a cada posición.

**2. Compare conceptualmente un soft-attention con un hard-attention, indicando ventajas y desventajas.**

> **R:** Soft usa promedio ponderado (diferenciable, permite backprop); Hard selecciona una posición (no diferenciable, requiere REINFORCE, pero más interpretable).

---

## Ejercicio 9

En Seq2Seq con arquitecturas encoder-decoder, cada parte cumple un rol distinto.

**1. Describa el objetivo principal del encoder y qué tipo de información produce.**

> **R:** Procesar la secuencia de entrada y producir una representación rica (hidden states) que capture el significado contextual de cada token.

**2. Explique cómo el decoder utiliza esa información para generar una secuencia de salida.**

> **R:** El decoder consume el contexto del encoder (directamente o via attention) y genera la salida autoregressivamente, condicionado a esa representación.

**3. Explique por qué un encoder-decoder puede producir secuencias de longitud variable, mientras que una RNN estándar no.**

> **R:** El decoder genera hasta producir EOS, independientemente de la longitud de entrada; una RNN estándar produce una salida por cada input.

---

## Ejercicio 10

Considere la siguiente oración en inglés y su traducción al español:

**Inglés (fuente):**
```
The book that the professor recommended yesterday was excellent.
```

**Español (destino):**
```
El libro que recomendó ayer el profesor era excelente.
```

**Complete la tabla cualitativamente (alta/media/baja) e interprete en el contexto Seq2Seq con RNNs.**

> **R (Tabla de atención con valores altos en diagonal semántica):**
> - El→The (alta), libro→book (alta), que→that (alta), recomendó→recommended (alta), ayer→yesterday (alta), profesor→professor (alta), era→was (alta), excelente→excellent (alta)

> **R (Interpretación):** Cada fila muestra a qué palabras del input el decoder presta atención al generar cada palabra de salida; la diagonal indica alineamiento entre traducciones equivalentes.

---

## Ejercicio 11

En una ResNet, la suma residual requiere que $F(x)$ y $x$ tengan igual dimensionalidad.

**1. Explique por qué una convolución $1 \times 1$ puede resolver incompatibilidades de canales.**

> **R:** Una convolución 1×1 puede cambiar el número de canales sin modificar las dimensiones espaciales, proyectando x al mismo número de canales que F(x).

**2. Describa qué cambiaría si se usara concatenación en lugar de suma.**

> **R:** El número de canales crecería en cada bloque (se duplicaría), aumentando memoria y parámetros, como ocurre en DenseNet.

---

## Ejercicio 12

Compare una red profunda estándar con una red con conexiones residuales.

**1. Explique por qué los gradientes se atenúan más en la red sin conexiones de salto.**

> **R:** Al propagar hacia atrás por muchas capas, el gradiente se multiplica repetidamente por valores < 1, causando vanishing gradient.

**2. Muestre conceptualmente cómo la expresión $H(x) = F(x) + x$ facilita la propagación del gradiente.**

> **R:** ∂H/∂x = ∂F/∂x + 1, garantizando que siempre fluye gradiente 1 directamente, evitando desvanecimiento.

**3. Describa por qué esto acelera el entrenamiento.**

> **R:** Los gradientes llegan más fuertes a capas tempranas, permitiendo actualizaciones significativas y convergencia más rápida.

---

## Ejercicio 13

En algunos bloques residuales se elimina la última activación para evitar asimetrías. Describa cómo esta asimetría puede limitar la capacidad del modelo.

> **R:** Si hay ReLU al final del bloque, la salida es siempre ≥ 0, pero la skip connection puede ser negativa, limitando el rango de funciones que el bloque puede representar.

---

## Ejercicio 14

Las conexiones de salto pueden implementarse mediante suma o concatenación.

**1. Compare el flujo de información entre suma y concatenación.**

> **R:** Suma mezcla las representaciones (información se fusiona); concatenación preserva ambas señales por separado (información se acumula).

**2. Indique cuál de las dos estrategias hace crecer el número de canales y por qué.**

> **R:** Concatenación, porque apila los canales de ambas ramas en lugar de sumarlos elemento a elemento.

**3. Dé una ventaja práctica de cada enfoque.**

> **R:** Suma: eficiente en memoria, no aumenta parámetros. Concatenación: preserva más información, mayor expresividad.

---

## Ejercicio 15

Considere dos redes convolucionales entrenadas sobre el mismo conjunto de datos: una red de 20 capas (Red A) y una red de 56 capas (Red B). Durante el entrenamiento se observa que:

- La Red B obtiene un *mayor error de entrenamiento* que la Red A.
- La Red B obtiene también un *mayor error de validación*.
- La Red B nunca alcanza el rendimiento de la Red A, incluso tras muchas iteraciones.

**1. Explique por qué este fenómeno no puede interpretarse como sobreajuste.**

> **R:** En sobreajuste el error de entrenamiento es bajo; aquí el error de entrenamiento es ALTO, indicando incapacidad de optimizar, no de generalizar.

**2. Describa el fenómeno conocido como *degradación* al incrementar excesivamente la profundidad en redes sin conexiones de salto. ¿Por qué, en principio, aumentar el número de capas no debería empeorar el rendimiento del modelo?**

> **R:** El optimizador no puede encontrar buenos mínimos en redes muy profundas sin skip connections debido a vanishing gradients y paisajes de pérdida complejos. Teóricamente no debería empeorar porque la red profunda podría aprender la identidad en capas extra.

**3. Justifique conceptualmente por qué una red más profunda puede *entrenar peor* que una red más superficial, incluso teniendo mayor capacidad representacional.**

> **R:** Mayor profundidad = gradientes más pequeños = actualizaciones insuficientes = la red queda atrapada en mínimos subóptimos.

**4. Compare este fenómeno con el sobreajuste real:**
- ¿Qué ocurre típicamente con el error de entrenamiento en un caso de sobreajuste?
- ¿Qué ocurre con el error de validación?
- ¿En qué se diferencia este comportamiento del observado en el presente experimento?

> **R:**
> - Sobreajuste: error entrenamiento BAJO, error validación ALTO (brecha grande).
> - Degradación: AMBOS errores ALTOS (no hay brecha, simplemente no entrena bien).

---

## Ejercicio 16

Considere una RNN definida por:

$$h_t = \sigma(Ux_t + Vh_{t-1} + b_h), \quad y_t = \sigma(Wh_t + b_y).$$

**1. Explique el papel de cada matriz de pesos $U$, $V$ y $W$.**

> **R:** U: transforma entrada xₜ al espacio oculto. V: transforma estado anterior hₜ₋₁ (recurrencia). W: transforma estado oculto a salida.

**2. Justifique por qué $V$ introduce memoria en el sistema.**

> **R:** V conecta hₜ con hₜ₋₁, haciendo que el estado actual dependa del pasado, permitiendo "recordar" información previa.

**3. Describa qué ocurriría si $V$ fuese la matriz nula. ¿La red seguiría siendo recurrente?**

> **R:** No sería recurrente; cada hₜ dependería solo de xₜ, equivalente a aplicar la misma capa feedforward independientemente a cada input.

---

## Ejercicio 17

Una secuencia tiene longitud total $n = 1000$ y la red se entrena con *BPTT truncada* usando un horizonte $k = 20$.

**1. Explique qué significa "desplegar 20 pasos hacia atrás".**

> **R:** Solo se propaga el gradiente a través de los últimos 20 pasos temporales, tratando el estado h_{t-20} como constante (sin gradiente).

**2. Justifique cómo truncar el horizonte reduce el riesgo de desvanecimiento o explosión de gradientes.**

> **R:** Menos multiplicaciones de matrices = gradientes más estables; se sacrifica aprendizaje de dependencias muy largas para estabilidad numérica.

---

## Ejercicio 18

Las arquitecturas LSTM y GRU introducen compuertas para controlar el flujo de información.

**1. Mencione limitaciones concretas de una RNN simple que estas arquitecturas resuelven.**

> **R:** Vanishing gradient impide aprender dependencias largas; la información se "olvida" rápidamente.

**2. Explique el rol de la *forget gate* en LSTM y de la *reset gate* en GRU.**

> **R:** Forget gate decide qué información borrar del cell state. Reset gate decide cuánto del estado anterior ignorar al calcular el candidato.

**3. Indique una ventaja práctica de usar GRU en lugar de LSTM.**

> **R:** Menos parámetros (2 gates vs 3), entrenamiento más rápido, similar rendimiento en muchas tareas.

---

## Ejercicio 19

Considere una RNN vanilla con las siguientes características:

- Dimensión de entrada: $d_x = 10$.
- Dimensión del estado oculto: $d_h = 20$.
- Dimensión de salida: $d_y = 5$.

La dinámica está dada por

$$h_t = \tanh(Ux_t + Vh_{t-1} + b_h), \quad y_t = Wh_t + b_y,$$

donde $U$, $V$, $W$, $b_h$ y $b_y$ son los parámetros entrenables del modelo.

**1. Calcule la cantidad de parámetros asociada a cada uno de los siguientes componentes:**

**a) La matriz $U$.**

> **R:** d_h × d_x = 20 × 10 = **200**

**b) La matriz $V$.**

> **R:** d_h × d_h = 20 × 20 = **400**

**c) El vector de sesgo $b_h$.**

> **R:** d_h = **20**

**2. Calcule la cantidad de parámetros asociada a:**

**a) La matriz $W$.**

> **R:** d_y × d_h = 5 × 20 = **100**

**b) El vector de sesgo $b_y$.**

> **R:** d_y = **5**

**3. Determine el número total de parámetros del modelo completo.**

> **R:** 200 + 400 + 20 + 100 + 5 = **725**

**4. Suponga ahora que se duplica la dimensión del estado oculto a $d_h = 40$, manteniendo $d_x$ y $d_y$ iguales.**

**a) Exprese nuevamente el número total de parámetros.**

> **R:** U: 40×10=400, V: 40×40=1600, b_h: 40, W: 5×40=200, b_y: 5 → Total: **2245**

**b) Explique brevemente qué término pasa a dominar el conteo de parámetros al aumentar $d_h$.**

> **R:** V (d_h × d_h) domina porque crece cuadráticamente con d_h.

---

## Ejercicio 20

Considere el siguiente texto:

```
"el gato negro duerme en el sillón grande"
```

Utilice una ventana simétrica de tamaño $w = 2$ para generar ejemplos de entrenamiento para modelos Word2Vec.

**1. Construya todos los pares (contexto, target) correspondientes al modelo CBOW, donde el contexto está formado por las palabras dentro de la ventana y la palabra central es el objetivo.**

> **R:** (el,gato,duerme,en)→negro, (gato,negro,en,el)→duerme, (negro,duerme,el,sillón)→en, etc.

**2. Construya todos los pares (input, output) correspondientes al modelo Skip-Gram, donde la palabra central actúa como entrada y cada palabra del contexto actúa como salida.**

> **R:** negro→el, negro→gato, negro→duerme, negro→en; duerme→gato, duerme→negro, duerme→en, duerme→el; etc.

**3. Explique por qué, para corpus grandes, el modelo Skip-Gram suele aprender mejores representaciones para palabras poco frecuentes.**

> **R:** Skip-Gram crea múltiples ejemplos por palabra (uno por cada vecino), dando más oportunidades de actualizar embeddings de palabras poco frecuentes.

**4. Justifique por qué el modelo CBOW tiende a ser más rápido de entrenar en la práctica.**

> **R:** CBOW hace una predicción por ventana; Skip-Gram hace 2w predicciones por ventana, multiplicando el costo.

---

## Ejercicio 21

Considere un modelo de lenguaje neuronal que utiliza una ventana fija de tamaño $N = 4$. Cada palabra se representa mediante un vector de embedding, y la arquitectura consiste en:

$$e = [e_{t-3}; e_{t-2}; e_{t-1}; e_t], \quad h = f(We + b), \quad \hat{y} = \text{softmax}(Uh + c).$$

**1. Explique por qué este modelo es conceptualmente similar a un modelo n-grama, pero presenta ventajas importantes respecto de enfoques estadísticos clásicos.**

> **R:** Usa contexto fijo como n-grama, pero los embeddings permiten generalizar a palabras similares no vistas y reducen sparsity.

**2. Mencione una razón por la cual este enfoque no escala bien a vocabularios muy grandes.**

> **R:** La capa softmax final tiene |V| salidas, haciendo el cálculo O(|V|) por predicción, muy costoso para vocabularios grandes.

---

## Ejercicio 22

Considere un modelo de lenguaje basado en una RNN definido por:

$$h_t = f(Ux_t + Vh_{t-1} + b), \quad \hat{y}_t = \text{softmax}(Wh_t + c),$$

donde durante el entrenamiento se aplica *teacher forcing*, es decir, el input $x_t$ corresponde siempre a la palabra correcta del corpus.

**1. Explique por qué este modelo no requiere una ventana fija como el modelo MLP.**

> **R:** El estado oculto hₜ acumula información de TODA la historia previa, no solo de una ventana.

**2. Describa cómo la recurrencia permite capturar dependencias largas que un modelo de ventana fija no puede modelar.**

> **R:** La recurrencia propaga información a través del tiempo via hₜ₋₁ → hₜ, teóricamente permitiendo recordar indefinidamente.

**3. Explique el rol del *teacher forcing* durante el entrenamiento y por qué acelera la convergencia.**

> **R:** Proporciona el input correcto en cada paso, evitando acumulación de errores y dando gradientes más informativos.

**4. Identifique un problema que aparece durante la inferencia autoregresiva y explique cómo se relaciona con el hecho de que, durante el entrenamiento, el modelo recibe siempre el input correcto.**

> **R:** Exposure bias: durante inferencia usa sus propias predicciones (posiblemente erróneas), situación nunca vista en entrenamiento, causando errores acumulativos.

---

## Ejercicio 23

Considere un modelo de lenguaje basado en una RNN vanilla con las siguientes características:

- Tamaño del vocabulario: $|V| = 8000$.
- Dimensión de los embeddings de palabras: $d_e = 128$.
- Dimensión del estado oculto de la RNN: $d_h = 256$.

El modelo funciona así:

- Cada palabra $w \in V$ se representa mediante un embedding $e(w)$ contenido en una matriz de embeddings $E$.
- En cada paso temporal se aplica la celda recurrente

$$h_t = \tanh(Ux_t + Vh_{t-1} + b_h),$$

donde $x_t$ es el embedding de la palabra en el paso $t$.

- La distribución de probabilidad sobre la siguiente palabra se obtiene como

$$\hat{y}_t = \text{softmax}(Wh_t + b_y),$$

donde $\hat{y}_t$ es un vector de dimensión $|V|$.

Los parámetros entrenables del modelo son: $E$, $U$, $V$, $W$, $b_h$ y $b_y$.

**1. Calcule la cantidad de parámetros de la matriz de embeddings $E$.**

> **R:** |V| × d_e = 8000 × 128 = **1,024,000**

**2. Calcule la cantidad de parámetros de la celda recurrente (es decir, de $U$, $V$ y $b_h$ en conjunto).**

> **R:** U: d_h × d_e = 256×128 = 32,768; V: d_h × d_h = 256×256 = 65,536; b_h: 256 → Total: **98,560**

**3. Calcule la cantidad de parámetros de la capa de salida (es decir, de $W$ y $b_y$ en conjunto).**

> **R:** W: |V| × d_h = 8000×256 = 2,048,000; b_y: 8000 → Total: **2,056,000**

**4. Determine el número total de parámetros del modelo.**

> **R:** 1,024,000 + 98,560 + 2,056,000 = **3,178,560**

**5. Si duplicamos la dimensión del estado oculto a $d_h = 512$ manteniendo fijo $|V|$ y $d_e$, ¿qué parte del modelo provoca el mayor aumento en el número total de parámetros?**

> **R:** La capa de salida W (|V| × d_h) porque |V| es grande y se multiplica por d_h; pasa de 2M a 4M parámetros.
