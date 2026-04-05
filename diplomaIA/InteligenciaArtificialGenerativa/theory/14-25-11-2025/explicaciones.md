# Explicación de Temas - Clase del 25-11-2025 (Repaso para el Parcial)

## La Gran Pregunta: ¿Qué Estamos Repasando?

Esta clase es un **repaso completo para el parcial**. El profesor mencionó explícitamente:

> "Hay como 20 pico preguntas de cada tema y después lo agarramos y hacemos alguna cosita de ahí. Creo que la verdad es como bien como una guía, digamos, para ir estudiando cada tema. O sea, de ahí va a salir el parcial, todo lo que está ahí va a salir."

**Temas NO incluidos en el parcial (no se vieron en el curso):**
- Transfer learning
- Zero shot learning
- CLIP (un modelo específico)

El profesor dijo: "Lo único que no vimos es transfer learning, la parte de zero shot, hay una parte de clip que es un modelo, eso no lo vimos nosotros, tuvimos dos clases menos."

---

## El Transformer: Arquitectura Completa

### ¿Qué es un Transformer?

Es una arquitectura que tiene **dos partes principales**:
- **Encoder** (izquierda): Procesa la entrada (ej: frase en español)
- **Decoder** (derecha): Genera la salida (ej: frase en inglés)

El profesor lo explicó así:

> "El encoder aprende una representación eficiente, comprime la información o la codifica de alguna forma, encuentra una representación latente que se la va a pasar al decoder y el decoder aprende a decodificar esa información."

### Bloques del Encoder y Decoder

Los bloques se **repiten N veces** (en el ejercicio de clase, N=2). Pero ojo:

> "Cada vez es como si fueran capas distintas para cada bloque, no es una recurrencia. Son N capas de encoder o de decoder. Lo estándar es que cada una tenga sus propios pesos, sus propios parámetros."

**Esto es diferente a las RNN**: en las RNN los pesos se reutilizan en cada paso temporal. En el Transformer, cada bloque tiene **sus propios parámetros independientes**.

---

## El Encoder: Paso a Paso

### 1. Input Embedding

La frase de entrada pasa por un **embedding**:
- Cada palabra se convierte en un vector de dimensión `d_model`
- El embedding es una **matriz entrenable** de tamaño `vocabulario × d_model`

### 2. Positional Encoding

**¿Por qué se necesita?**

> "El self attention es invariante bajo permutación. Si yo entrevero las palabras, la matriz se entrevera, pero me da los mismos valores. Entonces necesito marcar la posición temporal porque acá no hay ningún tipo de recurrencia."

El Transformer procesa **toda la frase de una vez** (no palabra por palabra como las RNN). Sin el positional encoding, no sabría el orden de las palabras.

### 3. Multi-Head Self Attention

**¿Qué es el Self Attention?**

Es un mecanismo donde **todas las palabras se comparan con todas** para ver quién está relacionado con quién.

> "Acuérdense, piensen en esto como en un traductor. El input va a ser una frase en un idioma y el output es en otro idioma. Lo de multihead es simplemente hacer attention varias veces, con la esperanza de que cada una de ellas capture distintas relaciones semánticas, de sintaxis, distintas relaciones temporales."

**¿Cómo funciona matemáticamente?**

1. Se crean tres matrices: **Q (Query), K (Key), V (Value)**
2. Cada una se calcula multiplicando la entrada por una matriz de pesos:
   - `Q = Z × W_Q`
   - `K = Z × W_K`
   - `V = Z × W_V`

3. Se calcula el attention:
```
Attention = softmax(Q × K^T / √d_k) × V
```

**¿Qué dimensiones tienen?**

Si tenemos N palabras y `d_model = 128`:
- Entrada Z: `N × 128`
- W_Q, W_K, W_V: `128 × d_k` (donde `d_k = d_model / heads`)
- Q, K, V: `N × d_k`
- `Q × K^T`: `N × N` (matriz de atención, todos contra todos)
- Salida: `N × d_v`

### 4. Skip Connection + Layer Normalization

Después del attention:
1. Se **suma** la salida del attention con la entrada original (skip connection)
2. Se aplica **layer normalization**

> "Se suma elemento a elemento. La salida va a tener la misma dimensión que la entrada."

El Layer Normalization tiene **parámetros entrenables**: gamma y beta, cada uno de dimensión `d_model`.

### 5. Feed Forward Network

Es un MLP de **dos capas**:
- Primera capa: `d_model → d_ff` (ej: 128 → 512)
- Segunda capa: `d_ff → d_model` (ej: 512 → 128)

> "La Fit Forward es lo que les decía, es un MLP de dos capas. Lo que hace es pasar de d_model a una dimensión d_ff del medio y después de d_ff pasa otra vez a d_model."

**Importante**: Esta misma red se aplica a **cada palabra por separado**:

> "Es la misma fit forward que se aplica a cada palabra. No es una fit forward global. El hecho de que las filas sean las palabras de la frase es lo que hace que esto pueda consumir una frase de cualquier longitud."

### 6. Otra Skip Connection + Layer Norm

Se repite el proceso: sumar + normalizar.

---

## El Decoder: Las Diferencias Clave

### 1. Masked Multi-Head Self Attention

**¿Por qué la máscara?**

> "El decoder va a recibir toda la secuencia. Entonces cuando él tiene que aprender a hacer la predicción de la palabra que va a venir en el tiempo T, no puede mirar la palabra que está en tiempo T."

Si le permitieras ver el futuro:

> "¿A qué le va a prestar más atención si su objetivo es predecir la palabra que va a ocupar la posición 3 y vos le permitís mirar toda la secuencia? A la palabra 3. Te va a dar identidad."

**¿Cómo se enmascara?**

Se usa una **matriz triangular inferior**. Todo lo que está arriba de la diagonal se pone a `-infinito` antes del softmax, de modo que el softmax lo convierta en 0.

### 2. Cross-Attention (Encoder-Decoder Attention)

Esta es la atención que **conecta encoder con decoder**:

> "Las queries son las palabras del decoder. Los keys y los values vienen del encoder. Lo que va a hacer es que para cada palabra del decoder me va a decir ¿a qué palabra del encoder le tiene que prestar más atención?"

Es exactamente igual que en los modelos Seq2Seq con RNN, pero ahora sin recurrencia.

### 3. El Resto es Igual

- Feed Forward
- Skip Connections
- Layer Normalization

---

## Entrenamiento vs Inferencia: La Diferencia Crucial

### En Entrenamiento

**Se pasa TODO de una vez**:

> "En entrenamiento te sale la probabilidad de todas las palabras. Porque vos tenés la longitud."

- El encoder recibe la frase completa en español
- El decoder recibe la frase completa en inglés (con begin_of_sequence al inicio)
- Se comparan las predicciones con las palabras reales (shifted)

### En Inferencia

**Hay un loop obligatorio**:

> "En inferencia tenemos un loop. Mando una palabra, mando otra, pero es un for. Ahí no hay nada en paralelo, ahí es secuencial."

El proceso:
1. El encoder procesa toda la frase de entrada (español) de una vez
2. Al decoder le pasamos solo `<begin_of_sequence>`
3. Predice la primera palabra
4. Esa palabra se agrega como input
5. Predice la segunda palabra
6. Y así hasta que predice `<end_of_sequence>`

> "Sin el start of sequence no podés arrancar. Es como que no tuvieras ruedas en el auto."

---

## Los Tokens Especiales

### Begin of Sequence (BOS / Start of Sequence)

**Es obligatorio para el decoder**:

> "En cualquier encoder decoder siempre es necesario que entre un begin of sequence."

El encoder NO lo necesita. Solo el decoder.

### End of Sequence (EOS)

Se usa para:
1. Marcar el final de la salida esperada durante entrenamiento
2. Saber cuándo parar durante inferencia

---

## Ejercicio de Cálculo de Parámetros

El profesor hizo un ejercicio detallado. Los hiperparámetros eran:
- Vocabulario source: 5000
- Vocabulario target: 6000
- d_model: 128
- Heads: 4
- d_ff: 512
- N_encoder: 2
- N_decoder: 2

### Parámetros del Multi-Head Attention

**Supuesto estándar**: `d_k = d_v = d_model / heads = 128 / 4 = 32`

Para **una cabeza** (head):
- W_Q: `128 × 32` = 4,096 parámetros
- W_K: `128 × 32` = 4,096 parámetros
- W_V: `128 × 32` = 4,096 parámetros
- b_Q, b_K, b_V: 32 cada uno = 96 parámetros

Total por cabeza: 12,384 parámetros

Para **4 cabezas**: 12,384 × 4 = 49,536 parámetros

**Más la matriz de salida W_O**:
- W_O: `128 × 128` = 16,384 parámetros
- b_O: 128 parámetros

**Total Multi-Head Attention**: 49,536 + 16,512 = **66,048 parámetros**

### Parámetros del Layer Normalization

- Gamma: 128 parámetros
- Beta: 128 parámetros
- **Total**: 256 parámetros

### Parámetros del Feed Forward

- Capa 1: `(128 + 1) × 512` = 66,048 parámetros
- Capa 2: `(512 + 1) × 128` = 65,664 parámetros
- **Total**: 131,712 parámetros

### Parámetros del Encoder (un bloque)

- 1 Multi-Head Attention: 66,048
- 2 Layer Norms: 256 × 2 = 512
- 1 Feed Forward: 131,712
- **Total por bloque**: 198,272
- **2 bloques**: 396,544

### Parámetros del Decoder (un bloque)

- 2 Multi-Head Attention: 66,048 × 2 = 132,096
- 3 Layer Norms: 256 × 3 = 768
- 1 Feed Forward: 131,712
- **Total por bloque**: 264,576
- **2 bloques**: 529,152

### Parámetros de Embeddings

- Input Embedding: `5000 × 128` = 640,000
- Output Embedding: `6000 × 128` = 768,000

### Capa Lineal de Salida

- `(128 + 1) × 6000` = 774,000

### Total del Transformer

**3,107,688 parámetros** (aproximadamente 3 millones)

El profesor comentó:

> "Y eso con un vocabulario de 5000 tokens es minúsculo. Esto es minúsculo."

---

## Comparación Transformer vs RNN

### Ventajas del Transformer

1. **Paralelización en entrenamiento**:
   > "La guitarra más evidente es que el transformer vos hacés todo de una. Con lo cual aprovechas mucho la eficiencia computacional."

2. **Mejor manejo de secuencias largas**:
   > "El attention considera toda la secuencia. A largo plazo no hay comparación con las RNN."

3. **Self-Attention vs Attention simple**:
   > "En las RNN con attention mirábamos solo la parte que correspondía cuando miramos la salida del encoder con cada palabra. En transformer hay self-attention."

### Similitudes

> "Si uno mira el encoder y el decoder como cajas negras es lo mismo. Solo que la caja negra de la RNN procesa el input paso a paso secuencialmente. Esto lo procesa todo de un saque."

---

## Preguntas Típicas del Parcial

El profesor mostró varias preguntas de parciales anteriores:

### Sobre Attention
- Explicar el mecanismo de attention con Q, K, V
- Completar una tabla de atención cualitativamente
- Comparar soft attention vs hard attention

### Sobre Seq2Seq
- Implementar encoding/decoding con pseudocódigo
- Beneficios de encoder-decoder vs modelo simple
- Explicar teacher forcing

### Sobre Transformers
- Explicar cada componente del diagrama
- Por qué se necesita positional encoding
- Para qué sirve la máscara en el decoder
- Diferencias entre Transformer y RNN

### Sobre Skip Connections y Gradientes
- Por qué una red más profunda puede entrenar peor
- Diferencia entre degradación y overfitting
- Vanishing/Exploding gradient

---

## Modelos de Lenguaje

### Cómo construir datos para entrenar

Dado el texto: "El perro corre rápido. El perro es feliz."

**Con ventana fija (para MLP)**:
- (el, perro) → corre
- (perro, corre) → rápido
- etc.

**Con RNN (cualquier longitud)**:
- el → perro
- el perro → corre
- el perro corre → rápido
- etc.

> "Depende de cómo vayan a implementar el language model. Si lo implementan con un MLP tiene que tener un largo fijo, agarran una ventana de largo fijo y la van corriendo en el texto."

---

## Definiciones para el Parcial

### Transformer
Arquitectura encoder-decoder que reemplaza la recurrencia por mecanismos de atención; procesa toda la secuencia en paralelo durante entrenamiento; usa positional encoding para mantener información de orden.

### Self-Attention
Mecanismo donde todas las palabras se comparan con todas para determinar relaciones; usa matrices Q, K, V; la fórmula es `softmax(QK^T/√d_k) × V`.

### Multi-Head Attention
Hacer self-attention varias veces con diferentes matrices de pesos; cada "head" captura diferentes tipos de relaciones (semánticas, sintácticas, temporales).

### Positional Encoding
Vector que se suma al embedding para indicar la posición de cada palabra; necesario porque el attention es invariante a permutaciones.

### Masked Attention
Atención donde se oculta el "futuro" de la secuencia; se usa en el decoder para evitar que vea las palabras que debe predecir.

### Layer Normalization
Normalización que opera fila a fila (palabra a palabra); tiene parámetros entrenables gamma y beta de dimensión d_model.

### Skip Connection (Residual Connection)
Conexión que suma la entrada de un bloque con su salida; permite que el gradiente fluya más fácilmente; evita vanishing gradient.

### Feed Forward Network
MLP de dos capas que se aplica a cada palabra por separado; va de d_model a d_ff y de vuelta a d_model.

### Teacher Forcing
Técnica de entrenamiento donde se usa la salida real (no la predicha) como entrada del siguiente paso; acelera el entrenamiento de modelos secuenciales.

### Vanishing Gradient
Problema donde los gradientes se vuelven muy pequeños al propagarse hacia atrás en redes profundas; las redes dejan de aprender.

### Encoder
Parte del modelo que procesa la entrada y genera una representación comprimida/latente; en traducción, procesa la frase en el idioma origen.

### Decoder
Parte del modelo que genera la salida a partir de la representación del encoder; en traducción, genera la frase en el idioma destino.

---

## Posibles Preguntas para el Parcial

### ¿Por qué el Transformer necesita positional encoding?
Porque el self-attention es invariante a permutaciones. Si cambio el orden de las palabras, sin el positional encoding obtendría los mismos valores. Se agrega para que el modelo sepa en qué posición está cada palabra.

### ¿Para qué sirve la máscara en el decoder?
Para que al predecir la palabra en posición T, el modelo no pueda "ver" las palabras de la posición T en adelante. Sin la máscara, el modelo haría trampa mirando exactamente la palabra que tiene que predecir.

### ¿Qué diferencia hay entre el entrenamiento y la inferencia en un Transformer?
En entrenamiento se pasa todo de una vez y se calcula la pérdida para todas las posiciones. En inferencia hay que hacer un loop: se empieza con el token de inicio y se va generando palabra por palabra.

### ¿Cuál es la ventaja del Transformer sobre las RNN?
El Transformer puede procesar toda la secuencia en paralelo durante entrenamiento, lo que lo hace mucho más eficiente. Además, el attention puede "ver" toda la secuencia, mientras que las RNN tienen problemas con dependencias a largo plazo.

### ¿Qué representa cada fila en una matriz de atención?
Cada fila representa una palabra de la secuencia y muestra a cuáles otras palabras le presta atención al momento de procesarla. Los valores altos indican mayor relevancia.

### ¿Por qué el encoder no necesita begin/end of sequence pero el decoder sí?
El encoder solo comprime la información de entrada, no genera nada secuencialmente. El decoder sí genera secuencialmente, entonces necesita saber cuándo empezar (BOS) y cuándo terminar (EOS).

### ¿Qué son los keys, queries y values en attention?
Son transformaciones de la entrada. La query "pregunta", los keys "responden" indicando relevancia, y los values son la información que se extrae. El attention es como buscar en un diccionario: la query busca keys similares y obtiene sus values.

### ¿Por qué una red más profunda puede entrenar peor que una más superficial?
Por el vanishing gradient: al tener muchas capas, los gradientes se vuelven muy pequeños al propagarse hacia atrás y la red deja de aprender. Es diferente al overfitting, que es cuando la red memoriza los datos de entrenamiento.

### ¿Cómo ayudan las skip connections?
Permiten que el gradiente fluya directamente a capas anteriores sin pasar por todas las transformaciones. Además, si una capa no aporta nada útil, puede aprender la identidad y no empeorar el resultado.

### ¿Qué hace el layer normalization?
Normaliza cada vector (cada palabra) restando su media y dividiendo por su desviación estándar. Tiene parámetros gamma y beta que permiten escalar y desplazar el resultado si es necesario.

### ¿Por qué d_k = d_model / heads es el estándar?
Por facilidad de implementación. Así se puede implementar como una sola multiplicación de matrices grande y después dividir el resultado en H partes, una por cada head.

### ¿Cómo se manejan las diferencias de longitud entre entrada y salida en traducción?
El encoder y decoder tienen longitudes independientes. El encoder procesa N palabras y salen N vectores. El decoder puede generar M palabras diferentes. La conexión es a través del cross-attention, que puede manejar cualquier combinación de longitudes.

### ¿Para qué sirve el padding?
Solo aparece cuando se hace entrenamiento por batches. Como las frases tienen diferentes longitudes, se agrega padding para que todas tengan el mismo largo y se puedan procesar juntas como matrices.
