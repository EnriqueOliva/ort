# Guía de Estudio - Parcial 2 - Modelos de Deep Learning
## 2do Semestre 2025
### Solo Enunciados (Sin Respuestas)

---

## Ejercicio 1

Considere un token de consulta $q \sim (4)$, dos claves $k_1, k_2 \sim (4)$ y dos valores $v_1, v_2 \sim (4)$:

$$q = (1, 0, 1, 0), \quad k_1 = (1, 1, 0, 0), \quad k_2 = (0, 1, 1, 0),$$
$$v_1 = (2, 0, 1, 1), \quad v_2 = (0, 1, 2, 1).$$

1. Calcule los puntajes de atención escalada:
$$e_i = \frac{q \cdot k_i}{\sqrt{4}}.$$

2. Aplique softmax a $(e_1, e_2)$ para obtener los pesos de atención.

3. Compute la salida:
$$z = \sum_i \alpha_i v_i.$$

---

## Ejercicio 2

Suponga:
$$d_{\text{model}} = 512, \quad h = 8.$$

1. Las dimensiones por cabeza $d_k$ y $d_v$ ¿están determinadas por $d_{\text{model}}$ y $h$?

2. Calcule el número de parámetros de las matrices $W_Q$, $W_K$, $W_V$. Ignore los sesgos.

3. Calcule los parámetros de la proyección final $W_O$.

---

## Ejercicio 3

El decodificador introduce una capa de *masked self-attention* que bloquea el acceso a tokens futuros.

1. Explique por qué esta máscara es indispensable durante el entrenamiento, incluso si el modelo tiene acceso a la secuencia completa como referencia.

2. Describa qué comportamiento incorrecto aparecería si la máscara no se aplicara.

3. Compare esta restricción con el mecanismo de *teacher forcing* utilizado en RNNs. ¿Tienen el mismo propósito? ¿En qué se diferencian?

4. Considere la matriz de puntajes de atención sin normalizar para una secuencia de longitud $T = 4$:

$$S = \begin{pmatrix} 1.2 & 0.5 & -0.3 & 2.0 \\ 0.7 & 1.0 & 0.9 & -1.0 \\ 1.5 & 0.1 & 0.2 & 0.3 \\ -0.2 & 0.4 & 1.3 & 0.8 \end{pmatrix}.$$

   a) Construya explícitamente la máscara causal $M$.

   b) Calcule $S' = S + M$.

   c) Aplique softmax a la tercera fila de $S'$ y dé los pesos normalizados.

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

A modo de resumen, la arquitectura puede representarse con la siguiente tabla (esquemática, suponiendo longitud máxima de secuencia $L$):

| Módulo | Forma entrada | Forma salida |
|--------|---------------|--------------|
| Input Embedding (src) | $(L, )$ | $(L, 128)$ |
| Output Embedding (tgt) | $(L, )$ | $(L, 128)$ |
| Encoder Layer ×2 | $(L, 128)$ | $(L, 128)$ |
| Decoder Layer ×2 | $(L, 128)$ | $(L, 128)$ |
| Linear salida | $(L, 128)$ | $(L, 6000)$ |

**Preguntas:**

1. Calcule el número de parámetros entrenables en:
   - a) una capa **MHA** individual (incluyendo todos sus sesgos);
   - b) un bloque **FFN** individual (incluyendo sesgos);
   - c) una operación **LayerNorm** individual.

2. Usando la estructura de cada bloque, calcule el número de parámetros de:
   - a) un bloque de **encoder** completo;
   - b) un bloque de **decoder** completo.

3. Calcule el total de parámetros del modelo completo, incluyendo:
   - embedding de entrada,
   - embedding de salida,
   - 2 bloques de encoder,
   - 2 bloques de decoder,
   - capa lineal de salida.

   Ignore cualquier otro posible parámetro no listado.

4. Compare el número de parámetros de este modelo con un *Transformer* que tenga $d_{\text{model}} = 256$, manteniendo todo lo demás igual. ¿Cómo escala aproximadamente el número total de parámetros con $d_{\text{model}}$?

---

## Ejercicio 5

En un modelo Seq2Seq clásico, el encoder resume toda la información de la oración de entrada en un único vector de contexto.

1. Explique por qué este diseño puede ser un cuello de botella cuando la secuencia de entrada es larga o contiene dependencias complejas.

2. Dé un ejemplo concreto de una situación donde se pierda información relevante debido a esta compresión.

3. Describa cómo un mecanismo de atención puede mitigar o eliminar este problema.

---

## Ejercicio 6

En modelos autoregresivos con decoders basados en RNNs, el proceso de entrenamiento difiere del proceso de inferencia.

1. Describa qué información recibe el decoder durante el entrenamiento y por qué.

2. Describa qué información recibe durante la inferencia y por qué necesariamente cambia el flujo.

3. Explique un problema típico que aparece si el modelo se entrena usando únicamente *teacher forcing*.

4. Mencione una solución habitual para reducir este problema.

---

## Ejercicio 7

Para entrenar y usar un modelo Seq2Seq se introducen los tokens especiales SOS y EOS.

1. Explique por qué el decoder necesita explícitamente el token SOS.

2. Describa qué problema surge si no se incluye un token EOS en la secuencia objetivo.

---

## Ejercicio 8

En mecanismos de atención se calculan pesos que indican la importancia relativa de cada posición del input durante la generación de un token.

1. Explique la interpretación probabilística de los pesos de atención.

2. Compare conceptualmente un soft-attention con un hard-attention, indicando ventajas y desventajas.

---

## Ejercicio 9

En Seq2Seq con arquitecturas encoder-decoder, cada parte cumple un rol distinto.

1. Describa el objetivo principal del encoder y qué tipo de información produce.

2. Explique cómo el decoder utiliza esa información para generar una secuencia de salida.

3. Explique por qué un encoder-decoder puede producir secuencias de longitud variable, mientras que una RNN estándar no.

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

A continuación se muestra una tabla que representa un mapa de atención. Complete la tabla *cualitativamente*, por ejemplo, con una "X" o con un valor cualitativo como alta/media/baja).

|           | The | book | that | the | professor | recommended | yesterday | was | excellent | . |
|-----------|-----|------|------|-----|-----------|-------------|-----------|-----|-----------|---|
| El        |     |      |      |     |           |             |           |     |           |   |
| libro     |     |      |      |     |           |             |           |     |           |   |
| que       |     |      |      |     |           |             |           |     |           |   |
| recomendó |     |      |      |     |           |             |           |     |           |   |
| ayer      |     |      |      |     |           |             |           |     |           |   |
| el        |     |      |      |     |           |             |           |     |           |   |
| profesor  |     |      |      |     |           |             |           |     |           |   |
| era       |     |      |      |     |           |             |           |     |           |   |
| excelente |     |      |      |     |           |             |           |     |           |   |
| .         |     |      |      |     |           |             |           |     |           |   |

¿Cómo se interpreta dicha tabla en el contexto Seq2Seq con RNNs?

---

## Ejercicio 11

En una ResNet, la suma residual requiere que $F(x)$ y $x$ tengan igual dimensionalidad.

1. Explique por qué una convolución $1 \times 1$ puede resolver incompatibilidades de canales.

2. Describa qué cambiaría si se usara concatenación en lugar de suma.

---

## Ejercicio 12

Compare una red profunda estándar con una red con conexiones residuales.

1. Explique por qué los gradientes se atenúan más en la red sin conexiones de salto.

2. Muestre conceptualmente cómo la expresión $H(x) = F(x) + x$ facilita la propagación del gradiente.

3. Describa por qué esto acelera el entrenamiento.

---

## Ejercicio 13

En algunos bloques residuales se elimina la última activación para evitar asimetrías. Describa cómo esta asimetría puede limitar la capacidad del modelo.

---

## Ejercicio 14

Las conexiones de salto pueden implementarse mediante suma o concatenación.

1. Compare el flujo de información entre suma y concatenación.

2. Indique cuál de las dos estrategias hace crecer el número de canales y por qué.

3. Dé una ventaja práctica de cada enfoque.

---

## Ejercicio 15

Considere dos redes convolucionales entrenadas sobre el mismo conjunto de datos: una red de 20 capas (Red A) y una red de 56 capas (Red B). Durante el entrenamiento se observa que:

- La Red B obtiene un *mayor error de entrenamiento* que la Red A.
- La Red B obtiene también un *mayor error de validación*.
- La Red B nunca alcanza el rendimiento de la Red A, incluso tras muchas iteraciones.

Responda:

1. Explique por qué este fenómeno **no puede interpretarse como sobreajuste**.

2. Describa el fenómeno conocido como *degradación* al incrementar excesivamente la profundidad en redes sin conexiones de salto. ¿Por qué, en principio, aumentar el número de capas no debería empeorar el rendimiento del modelo?

3. Justifique conceptualmente por qué una red más profunda puede *entrenar peor* que una red más superficial, incluso teniendo mayor capacidad representacional.

4. Compare este fenómeno con el **sobreajuste real**:
   - ¿Qué ocurre típicamente con el error de entrenamiento en un caso de sobreajuste?
   - ¿Qué ocurre con el error de validación?
   - ¿En qué se diferencia este comportamiento del observado en el presente experimento?

---

## Ejercicio 16

Considere una RNN definida por:

$$h_t = \sigma(Ux_t + Vh_{t-1} + b_h), \quad y_t = \sigma(Wh_t + b_y).$$

1. Explique el papel de cada matriz de pesos $U$, $V$ y $W$.

2. Justifique por qué $V$ introduce memoria en el sistema.

3. Describa qué ocurriría si $V$ fuese la matriz nula. ¿La red seguiría siendo recurrente?

---

## Ejercicio 17

Una secuencia tiene longitud total $n = 1000$ y la red se entrena con *BPTT truncada* usando un horizonte $k = 20$.

1. Explique qué significa "desplegar 20 pasos hacia atrás".

2. Justifique cómo truncar el horizonte reduce el riesgo de desvanecimiento o explosión de gradientes.

---

## Ejercicio 18

Las arquitecturas LSTM y GRU introducen compuertas para controlar el flujo de información.

1. Mencione limitaciones concretas de una RNN simple que estas arquitecturas resuelven.

2. Explique el rol de la *forget gate* en LSTM y de la *reset gate* en GRU.

3. Indique una ventaja práctica de usar GRU en lugar de LSTM.

---

## Ejercicio 19

Considere una RNN vanilla con las siguientes características:

- Dimensión de entrada: $d_x = 10$.
- Dimensión del estado oculto: $d_h = 20$.
- Dimensión de salida: $d_y = 5$.

La dinámica está dada por

$$h_t = \tanh(Ux_t + Vh_{t-1} + b_h), \quad y_t = Wh_t + b_y,$$

donde $U$, $V$, $W$, $b_h$ y $b_y$ son los parámetros entrenables del modelo.

1. Calcule la cantidad de parámetros asociada a cada uno de los siguientes componentes:
   - a) La matriz $U$.
   - b) La matriz $V$.
   - c) El vector de sesgo $b_h$.

2. Calcule la cantidad de parámetros asociada a:
   - a) La matriz $W$.
   - b) El vector de sesgo $b_y$.

3. Determine el **número total de parámetros** del modelo completo.

4. Suponga ahora que se duplica la dimensión del estado oculto a $d_h = 40$, manteniendo $d_x$ y $d_y$ iguales.
   - a) Exprese nuevamente el número total de parámetros.
   - b) Explique brevemente qué término pasa a dominar el conteo de parámetros al aumentar $d_h$.

---

## Ejercicio 20

Considere el siguiente texto:

```
"el gato negro duerme en el sillón grande"
```

Utilice una ventana simétrica de tamaño $w = 2$ para generar ejemplos de entrenamiento para modelos Word2Vec.

1. Construya todos los pares (contexto, target) correspondientes al modelo **CBOW**, donde el contexto está formado por las palabras dentro de la ventana y la palabra central es el objetivo.

2. Construya todos los pares (input, output) correspondientes al modelo **Skip-Gram**, donde la palabra central actúa como entrada y cada palabra del contexto actúa como salida.

3. Explique por qué, para corpus grandes, el modelo **Skip-Gram** suele aprender mejores representaciones para palabras poco frecuentes.

4. Justifique por qué el modelo **CBOW** tiende a ser más rápido de entrenar en la práctica.

---

## Ejercicio 21

Considere un modelo de lenguaje neuronal que utiliza una ventana fija de tamaño $N = 4$. Cada palabra se representa mediante un vector de embedding, y la arquitectura consiste en:

$$e = [e_{t-3}; e_{t-2}; e_{t-1}; e_t], \quad h = f(We + b), \quad \hat{y} = \text{softmax}(Uh + c).$$

1. Explique por qué este modelo es conceptualmente similar a un modelo n-grama, pero presenta ventajas importantes respecto de enfoques estadísticos clásicos.

2. Mencione una razón por la cual este enfoque no escala bien a vocabularios muy grandes.

---

## Ejercicio 22

Considere un modelo de lenguaje basado en una RNN definido por:

$$h_t = f(Ux_t + Vh_{t-1} + b), \quad \hat{y}_t = \text{softmax}(Wh_t + c),$$

donde durante el entrenamiento se aplica *teacher forcing*, es decir, el input $x_t$ corresponde siempre a la palabra correcta del corpus.

1. Explique por qué este modelo no requiere una ventana fija como el modelo MLP.

2. Describa cómo la recurrencia permite capturar dependencias largas que un modelo de ventana fija no puede modelar.

3. Explique el rol del *teacher forcing* durante el entrenamiento y por qué acelera la convergencia.

4. Identifique un problema que aparece durante la inferencia autoregresiva y explique cómo se relaciona con el hecho de que, durante el entrenamiento, el modelo recibe siempre el input correcto.

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

1. Calcule la cantidad de parámetros de la matriz de embeddings $E$.

2. Calcule la cantidad de parámetros de la celda recurrente (es decir, de $U$, $V$ y $b_h$ en conjunto).

3. Calcule la cantidad de parámetros de la capa de salida (es decir, de $W$ y $b_y$ en conjunto).

4. Determine el **número total de parámetros** del modelo.

5. Si duplicamos la dimensión del estado oculto a $d_h = 512$ manteniendo fijo $|V|$ y $d_e$, ¿qué parte del modelo provoca el mayor aumento en el número total de parámetros?
