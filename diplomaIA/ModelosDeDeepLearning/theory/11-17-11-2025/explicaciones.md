# Explicación COMPLETA - Clase del 17-11-2025
# Attention Mechanisms y Transformers

---

## Introducción: De Encoder-Decoder a Attention

### El Contexto de la Clase

El profesor comenzó recordando que en clases anteriores habían trabajado con arquitecturas **encoder-decoder** usando RNN (redes neuronales recurrentes), LSTM y GRU. Esta clase introduce una idea **muy potente** que se agrega a esas arquitecturas: el mecanismo de **Attention** (atención).

Como dijo el profesor: "La idea es introducir en esta primer diálogo... la arquitectura encoder-decoder. Y ahora le vamos a agregar una idea muy potente por arriba que es - que surge en este contexto."

### ¿Qué es Encoder-Decoder? (Repaso rápido)

Imagínate que quieres traducir una frase del francés al inglés. La arquitectura encoder-decoder funciona así:

1. **Encoder (codificador)**: Toma toda la frase en francés y la "comprime" en un vector de contexto (una lista de números que representa la información de toda la frase)
2. **Decoder (decodificador)**: Usa ese vector de contexto para generar la traducción en inglés, palabra por palabra

**El problema**: El encoder devolvía un solo vector de contexto de **tamaño fijo** (dimensión fija) para toda la frase, sin importar si la frase tenía 5 palabras o 50 palabras.

---

## El Paper de Bahdanau: Introduciendo Attention

### ¿Quién es Bahdanau?

El profesor explicó que va a seguir principalmente el paper de Bahdanau: "Voy a seguir casi que - prácticamente seguí este paper de Bahdanau."

Mencionó que hay varios autores en el paper, entre ellos **Yoshua Bengio, que es el premio Turing**, pero como el primer autor es Bahdanau, se dice que "Bahdanau introdujo esta noción de attention."

### El Problema que Querían Resolver

El profesor leyó directamente del paper:

**"Los modelos propuestos recientemente para traducción neuronal por máquina a menudo pertenecen a la familia de encoder-decoders y codifican una secuencia fuente en un vector de largo fijo."**

El profesor aclaró: "Dice largo fijo, pero quiere decir dimensión fija. Los matemáticos tienen esas libertades."

Luego continuó leyendo: **"Lo que pasa es que esto es un cuello de botella en el mejoramiento del desempeño de esta arquitectura básica encoder-decoder."**

### Visualización del Cuello de Botella

```
┌─────────────────────────────────────────────────────────────────────────┐
│                  EL PROBLEMA: CUELLO DE BOTELLA                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   Frase entrada (puede tener 5 o 50 palabras):                          │
│   "El gato negro que vi ayer en el parque estaba durmiendo..."          │
│                              │                                          │
│                              ▼                                          │
│                    ┌─────────────────┐                                  │
│                    │   ENCODER       │                                  │
│                    │   (RNN/LSTM)    │                                  │
│                    └────────┬────────┘                                  │
│                             │                                           │
│                             ▼                                           │
│                    ┌─────────────────┐                                  │
│                    │  CONTEXTO (C)   │  ← Vector de dimensión FIJA      │
│                    │  [256 números]  │    (ej: 256 dimensiones)         │
│                    └────────┬────────┘                                  │
│                             │                                           │
│        ┌────────────────────┴────────────────────┐                     │
│        │                                          │                     │
│        ▼                                          ▼                     │
│   Para generar "The"                       Para generar "sleeping"      │
│   usa el MISMO C                           usa el MISMO C               │
│                                                                         │
│   ⚠️  TODO pasa por este único punto C = cuello de botella              │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### La Solución Propuesta

**"Y proponemos extender esto permitiendo al modelo automáticamente soft buscar - buscar de forma soft - partes de la secuencia fuente o inputs que son relevantes para predecir la palabra target."**

En palabras simples del profesor: "Es ese es el objetivo que se propusieron y fue con ese propósito que inventaron esta noción de attention."

---

## Encoder-Decoder Antes de Attention

### Cómo Funcionaba Antes

El profesor explicó con detalle cómo era la arquitectura tradicional:

"En su forma más general, la arquitectura encoder-decoder, dada una secuencia input que tiene un largo TX, devuelve un vector de contexto C. Era típicamente el último hidden [state]."

**En el Encoder**:
- Empiezas con H₀ (estado inicial)
- Entra X₁ (primera palabra) → produce H₁
- Entra X₂ (segunda palabra) + H₁ → produce H₂
- Y así hasta la última palabra, que produce HTx

**El vector de contexto C**:

"A partir de todos ellos o lo más común del último se genera un contexto. El contexto - esto era esencialmente el último hidden state."

**En el Decoder**:

"El decoder se entrena para predecir la siguiente palabra dado el vector de contexto y todas las palabras anteriores."

La fórmula que el profesor mostró era:

```
P(yᵢ | y₁, ..., yᵢ₋₁, C) = función(Sᵢ₋₁, yᵢ₋₁, C)
```

Donde:
- **C** = contexto (siempre el mismo)
- **Sᵢ₋₁** = estado oculto anterior del decoder
- **yᵢ₋₁** = palabra anterior predicha

### Detalles Técnicos Importantes

**Sobre H₀ (estado inicial del encoder)**:

El profesor fue muy claro: **"Lo más usual es inicializarlo como cero."**

Luego agregó: "Hay algunas versiones un poquito posteriores que usan esto como parámetro de la red. Entonces también es entrenable el H0 inicial."

Pero advirtió: **"Pero vos no querés un H0 aleatorio porque después cuando hagas inferencia... el H0 tiene que ser el mismo para todo tu dataset."**

**Teacher Forcing vs Inferencia**:

**En entrenamiento (Teacher Forcing)**:
"Si estoy en entrenamiento, por lo menos al principio, lo más probable es que haga teacher forcing, que es que esto va a producir un siguiente hidden state que se va a pasar al siguiente, pero también tengo el y1 verdadero que es lo que le voy a pasar como input también al siguiente."

**En inferencia**:
"En inferencia, en realidad busco el y1 que maximiza esta probabilidad."

---

## La Gran Idea de Bahdanau: Attention en Secuencias

### El Cambio Fundamental

El profesor leyó del paper:

**"Vamos a extender esto del encoder-decoder para que aprenda a alinear y traducir de forma conjunta."**

El término **"alinear"** es clave. El profesor explicó: "El mecanismo de atención es como una especie de mecanismo de alineación."

**"Cada vez que el modelo propuesto genera una palabra en una traducción, hace un soft search - búsqueda suave - para posiciones en las sentencias fuente, en el input, en donde está la información más relevante concentrada."**

### La Nueva Fórmula

**Antes**:
```
P(yᵢ) = función(C, Sᵢ₋₁, yᵢ₋₁)
```

**Ahora con Attention**:
```
P(yᵢ) = función(Cᵢ, Sᵢ₋₁, yᵢ₋₁)
```

El profesor lo explicó: **"¿Cuál es el único cambio que propone? Es hacer que ahora dependa de un contexto que depende de la posición en la que estoy. Va a haber un C distinto para cada palabra target."**

### Visualización: Cómo Attention Resuelve el Cuello de Botella

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SEQ2SEQ + BAHDANAU ATTENTION                         │
│                (Sigue siendo Encoder-Decoder, pero MEJORADO)            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ENCODER (RNN/LSTM/GRU) - igual que antes                              │
│   ─────────────────────                                                 │
│   "The"   → H₁ ─────────┐                                               │
│   "black" → H₂ ─────────┤                                               │
│   "cat"   → H₃ ─────────┼─────▶  TODOS los Hⱼ se GUARDAN                │
│   "sleeps"→ H₄ ─────────┤        (¡ya no tiramos ninguno!)              │
│   "in"    → H₅ ─────────┤                                               │
│   "garden"→ H₆ ─────────┘                                               │
│                          │                                              │
│                          ▼                                              │
│              ┌───────────────────────┐                                  │
│              │   MECANISMO ATTENTION │  ← ESTO ES LO NUEVO              │
│              │   (Bahdanau)          │                                  │
│              │                       │                                  │
│              │   Para cada paso i:   │                                  │
│              │   • Calcula αᵢⱼ       │                                  │
│              │   • Cᵢ = Σ αᵢⱼ × Hⱼ   │                                  │
│              └───────────┬───────────┘                                  │
│                          │                                              │
│        ┌─────────────────┼─────────────────┐                           │
│        │                 │                 │                            │
│        ▼                 ▼                 ▼                            │
│       C₁                C₂                C₃     (contextos DIFERENTES) │
│   (enfoca H₁)       (enfoca H₃)       (enfoca H₄)                       │
│        │                 │                 │                            │
│        ▼                 ▼                 ▼                            │
│   genera "El"      genera "gato"    genera "duerme"                     │
│                                                                         │
│   ✅ Cada palabra generada tiene su PROPIO contexto                     │
│   ✅ Ya no hay cuello de botella                                        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**CLAVE:** Attention se AGREGA al Seq2Seq existente. Seguimos teniendo:
- Un **Encoder** (RNN/LSTM/GRU) que procesa la entrada
- Un **Decoder** (RNN/LSTM/GRU) que genera la salida

Lo que cambia es que el Decoder ya no usa un solo C fijo, sino un Cᵢ diferente para cada palabra.

---

## ¿Cómo se Construye el Contexto Cᵢ?

### La Fórmula del Contexto

```
Cᵢ = Σⱼ αᵢⱼ × Hⱼ
```

**"El contexto Ci va a depender de la secuencia entera de hidens del encoder. Va a ser una especie de promedio ponderado de los hidens, donde la ponderación depende de cómo se relaciona el i con el j."**

Desglosando:
- **Hⱼ** son los hidden states del encoder (H₁, H₂, H₃, etc.)
- **αᵢⱼ** son los pesos de atención (números entre 0 y 1 que suman 1)
- **Cᵢ** es el contexto para la posición i del decoder

### ¿De Dónde Salen los αᵢⱼ?

Se calculan con una **softmax**:

```
αᵢⱼ = softmax(eᵢⱼ)
```

"Se calcula a través de una softmax. Esto tiene que - alfa i,j - pensarlo como una probabilidad o un peso que yo le doy."

Interpretación: "Si estoy en la posición i del decoder, ¿qué peso le doy a cada posición j del encoder? O cuán probable es que dependa de esa palabra, de esa posición."

### Los Scores de Alineación (eᵢⱼ)

"Típicamente esto va a ser una especie de producto - piénsenlo, cuán parecidos o cuán alineados están, o sea, las direcciones de estos dos vectores que viven en el mismo espacio."

---

## Por Qué Se Llama "Attention"

**"Porque lo que está haciendo es ver el estado SI-1, que piénsenlo como lo que yo tengo construido hasta ese momento, cómo se alinea con los distintos hidens del encoder para hacer mi siguiente predicción. O sea, en cierta forma es a qué hidens presto más atención para hacer mi siguiente predicción."**

---

## La Terminología Moderna: Query, Key, Value

### De Dónde Viene

El profesor explicó: "A la sucesión de hidens se les llaman los **keys**."

**"Los valores - miren, también van a ser los hidens del encoder. Es una especie de diccionario trivial en el que el H1 tiene como valor H1."**

"Y la **query** es [el hidden] del decoder."

### La Explicación Abstracta

**"Es como que estoy preguntando cuando agarro un hidden del decoder, estoy preguntando en este diccionario, ¿cuál es el key que más se parece a [mi query]? O sea, básicamente es como si estuviera buscando esto dentro de este conjunto y ver cuál es el que más se alinea con esta query que yo estoy haciendo."**

---

## Cómo Implementa Bahdanau el Attention (Attention Aditiva)

### Las entradas en el paso i del decoder:

1. **El input**: yᵢ₋₁ (la palabra anterior del target)
2. **El previous hidden**: Sᵢ₋₁
3. **Los encoder outputs**: Todos los H del encoder

### El Proceso Paso a Paso

**Paso 1: Embedding del Input**
"Acá entra el yi-1, se lo pasa por un embedding y se obtiene el vector embebido que va directo a la GRU."

**Paso 2: Calcular los Scores de Alineación**
Se multiplica:
- **Sᵢ₋₁** por una matriz **Wₛ**
- Cada **Hⱼ** por una matriz **Wₕ**

**"Esto es lo que se llama attention aditiva."**

**Paso 3: Aplicar Tangente Hiperbólica**
```
Bᵢⱼ = tanh(Wₛ × Sᵢ₋₁ + Wₕ × Hⱼ)
```

**Paso 4: Multiplicar por el Vector de Parámetros**
```
eᵢⱼ = vᵀ × Bᵢⱼ
```

**Paso 5: Softmax**
```
αᵢⱼ = softmax(eᵢⱼ)
```

**Paso 6: Crear el Vector de Contexto**
```
Cᵢ = Σⱼ αᵢⱼ × Hⱼ
```

**Paso 7 y 8**: Ese C se le pasa a la GRU junto con el previous hidden y el yi-1, produciendo un nuevo hidden Si y una predicción.

### Los Parámetros Entrenables

- **Wₛ**: Matriz para proyectar el estado del decoder
- **Wₕ**: Matriz para proyectar los hiddens del encoder
- **v**: Vector de parámetros de attention
- Los pesos del embedding y la GRU

---

## El Ejemplo Visual: La Matriz de Attention

### Cómo Se Lee la Matriz

El profesor mostró ejemplos de traducción francés-inglés con matrices de atención:

- **Cuanto más claro el píxel, más alto el peso de atención**
- Se lee por filas: cada fila corresponde a una palabra del output (inglés)
- Cada columna corresponde a una palabra del input (francés)

### LA GRAN CONFUSIÓN: ¿Quién Mira Qué?

**"El que hace - el que implementa el mecanismo de atención es el decoder."**

**"Para predecir la primer palabra, va a mirar la relación que hay - a qué palabras del input le tiene que prestar atención para predecir esta palabra."**

### ¿Se Puede Mirar al Futuro?

Estudiante: "Pero no habíamos dicho como que no miraba el futuro?"

Profesor: **"No mira el futuro del decoder, pero el encoder lo puede mirar todo. En los Transformers la máscara de causalidad está puesta en el decoder, no en el encoder."**

---

## Definición General de Attention

### El Paper "Attention Is All You Need"

El profesor leyó las dos primeras oraciones:

**"Una función de attention se puede describir como un mapping que mapea una query y un conjunto de pares key-value en un output, en donde la query y las keys y los values y el output son todos vectores."**

**"El output es calculado como una suma ponderada de los values, donde el peso asignado a cada value se calcula a partir de una función de compatibilidad entre la query y las correspondientes keys."**

### La Fórmula

```
Output = Σᵢ αᵢ × Vᵢ

donde: αᵢ = función_compatibilidad(Q, Kᵢ)
```

### Analogía del Diccionario

**"Básicamente, piensen - esto es la query - va a buscar en el diccionario. Y va a devolver el valor que corresponde."**

Pero en soft attention: **"Lo más probable es que sea este, pero 80%, pero hay un 15% este y no sé cuánto por este otro."**

---

## Casos Extremos de Attention

### Caso 1: Indecisión Total

Todos los αᵢ = 1/n
**"Es como no decir nada."**

### Caso 2: Certeza Absoluta

Un αᵢ = 1, todos los demás = 0
**"Tampoco te sirve porque lo único que te está diciendo es que el más influyente es ese, pero te estás perdiendo otros que pueden influir."**

### Caso 3: Soft Attention (Lo Ideal)

**"Algo intermedio sería agarrar la softmax de los productos escalares."**

**"Y los extremos anteriores se obtienen si yo en la softmax uso una temperatura que en el caso de temperatura cero se me concentra en el máximo y el caso de temperatura infinito mi indecisión total."**

---

## Self-Attention

### ¿Qué Es?

**"El mecanismo de self-attention es el proceso de aplicar el mecanismo de atención a cada punto de la secuencia."**

**"A cada posición del input le vas a aplicar el mecanismo de attention. Es como si hicieras tantas queries como palabras tenés en el input."**

### Cómo Se Hace

**"Esto se hace creando tres vectores - Query, Key y Value - para cada posición de la secuencia, y después aplicando el mecanismo de atención para cada posición Xi usando Xi como vector query, como key-value para todas las otras posiciones."**

Un estudiante preguntó: "¿Incluido el mismo?"

Profesor: **"Incluido el mismo, sí."**

### El Output

**"Yi incorpora la información de Xi además de cómo Xi se relaciona con todas las otras posiciones de X."**

---

## Implementación de Self-Attention

### Pesos Compartidos - La Clave

**"¿Cuál es la gracia? Que son los mismos pesos. Se comparten las mismas proyecciones. Es la misma matriz que están multiplicando."**

```
Q₁ = Wᵩ × X₁
K₁ = Wₖ × X₁
V₁ = Wᵥ × X₁

Q₂ = Wᵩ × X₂  (¡Misma Wᵩ!)
K₂ = Wₖ × X₂  (¡Misma Wₖ!)
V₂ = Wᵥ × X₂  (¡Misma Wᵥ!)
```

### El Proceso

**Paso 1**: Armar la matriz Q × K^T (todos los productos escalares)
**Paso 2**: Aplicar softmax fila a fila
**Paso 3**: Multiplicar por V → suma ponderada de los valores

### Qué Representa

**"Para cada posición lo que va a ser es decirnos esta posición con qué otras posiciones se relaciona de forma más fuerte."**

**"Es como aquello de cuando decimos - no, pero antes habíamos hablado de esa persona, entonces ese pronombre se liga fuertemente con el nombre de esa persona. La idea es que aprenda esas relaciones estadísticas a partir del entrenamiento."**

---

## Scaled Dot-Product Attention

### El "Numerito Mágico"

**Fórmula completa**:
```
Attention(Q, K, V) = softmax(Q × K^T / √dₖ) × V
```

### ¿Por Qué Dividir por √dₖ?

**"Es una estandarización que se hace para dar estabilidad numérica. No tiene significado de machine learning."**

**"Dividir entre ese número es para no tener problemas de cálculo numérico y que no se me sature la softmax."**

---

## El Problema de la Invariancia por Permutaciones

### El Anuncio Importante

El profesor dijo con énfasis: **"Y lo último es esto que es importante. Va para parcial."**

### El Problema

**"Este mecanismo de atención es completamente invariante al orden de la secuencia."**

**"Si yo cambio X2 con X1, todo se intercambia y cuando yo calculo la attention me da todo igual."**

### Por Qué Es Un Problema

**"El texto tiene un orden. Entonces si yo altero el texto al azar, no puede ser que la attention me diga siempre lo mismo."**

### La Solución

**"Se necesita poner alguna información posicional a los X para que el mecanismo deje de ser invariante por permutaciones."**

**"Se llama positional encoding."**

---

## Positional Encoding en Detalle

### ¿Qué Es?

**"Una palabra medio pomposa para básicamente codificar la posición en la que está cada palabra."**

**"Se codifica con una onda sinusoidal."**

### El Concepto Sinusoidal

**"La posición uno es una onda sola. Es una cuerda que va de extremo a extremo. La posición dos es una que tiene frecuencia doble, la posición tres es una que tiene frecuencia tres."**

La fórmula: La coordenada par es con seno y la coordenada impar es con coseno.

### Cómo Se Suma al Embedding

```
Input final = Embedding(palabra) + Positional Encoding(posición)
```

### Ejemplo con Palabras Repetidas

Estudiante: "Si tuviera 'thinking machine thinking' de nuevo, X1 y X3 son distintos, ¿no?"

Profesor: **"Claro, claro. X1 y X3 son distintos."**

Porque aunque la palabra sea la misma, el positional encoding hace que sean diferentes según su posición.

---

## El Tamaño del Embedding

### Es un Hiperparámetro

**"El tamaño del embedding es un hiperparámetro que vos elegís. Por ejemplo, el de Vaswani usaban 512, dimensión 512."**

### El Trade-off

**"Tu embedding tiene que tener suficientes dimensiones para representar todas las palabras que quiera y a la vez no debe ser demasiado grande porque si no te quedás super esparzo."**

---

## Ejemplo Concreto: "Thinking Machines"

### Los Números del Ejemplo

- Q₁ · K₁ = 112, Q₁ · K₂ = 96
- Dividiendo por √64 = 8: 14 y 12
- Después de softmax: 0.88 y 0.12
- Z₁ = 0.88 × V₁ + 0.12 × V₂

**"Este sería como el vector self-attention de contexto para la palabra 'thinking'."**

---

## La Dependencia del Contexto

### Palabras con Múltiples Significados

**"date"**:
- "go on a date": Cita romántica
- "the date": La fecha

**"Se precisan representaciones sensibles al contexto y eso es lo que self-attention intenta abordar."**

---

## Analogía del Diccionario de Imágenes

### El Ejemplo

Query: "dogs on the beach"

Keys: ["beach", "beach + dogs", "dogs"]

**"'Dogs on the beach' matchea solo 'beach'. Acá matchea dos: 'beach' y 'dog'. Y acá matchea solo 'dog'."**

**"Entonces el attention va a ser más grande para esta imagen [perros en la playa]."**

En soft attention, devuelve una combinación ponderada de todas.

---

## Multi-Head Attention

### ¿Qué Es?

**"El multi-head attention es lo mismo que el self-attention, solo que se hace varias veces. Esto parece misterioso, pero es hacer el self-attention 8 veces."**

### ¿Por Qué Múltiples Cabezas?

**"Porque de repente esta neurona aprendió algo y esta otra aprendió otra cosa. Entonces cada attention de repente aprende cosas distintas, relaciones distintas."**

### Cómo Funciona

**"Tengo un self-attention 1 que tiene sus matrices. El self-attention 2 tiene sus matrices. Y así haces cuántas quieres y eso se llama multi-head attention."**

**"Y después lo que haces es concatenar todos los resultados."**

---

## De Attention a Transformers

### El Gran Descubrimiento

**"El transformer, por eso el paper se llama 'attention is all you need', en el sentido de que vos no precisas una recurrencia sobre el tiempo. Podés procesar todo en paralelo, toda la secuencia."**

### Por Qué Es Revolucionario

**"Eso le da una rapidez enorme en comparación a la recurrente. Una eficiencia de cómputo en comparación a la recurrente que tiene que ir paso a paso."**

**"Su gran impacto fue la escalabilidad. Son la base de la revolución de hoy por hoy, de los modelos de lenguaje."**

**"Fueron generalizados y usados en visión, en audio y muchas otras áreas más."**

---

## La Arquitectura Transformer Completa

### Estructura General

**"La arquitectura del transformer tiene un encoder y tiene un decoder. Y después tiene como antes una parte lineal para hacer la predicción de probabilidades."**

### Inputs y Embeddings

**"Los inputs acá son la frase, por ejemplo, en francés. A cada palabra se le hace un embedding."**

**"Después se le hace un positional encoding, para marcar la posición."**

### El Encoder - Estructura

1. **Multi-Head Self-Attention**
2. **Add & Norm**: "A la salida de la attention se le suma lo que venía (residual connection)"
3. **Feed-Forward Network**: "En la versión original es simplemente un MLP de dos capas"
4. **Add & Norm**: Otra residual connection

### El Decoder - Estructura

1. **Masked Multi-Head Self-Attention**
2. **Add & Norm**
3. **Multi-Head Attention** (encoder-decoder)
4. **Add & Norm**
5. **Feed-Forward Network**
6. **Add & Norm**
7. **Linear + Softmax**

### La Máscara de Causalidad - MUY IMPORTANTE

**"La diferencia que dice 'mask': no queremos que pueda saberse el futuro."**

**"En el encoder eso no es problema porque la frase en francés siempre está dada. Podemos hacer todo el mundo con todo el mundo."**

**"Pero a la hora de hacer generación, no se puede comparar con el futuro."**

Estudiante: "¿Aunque esté aprendiendo?"

Profesor: **"Aunque esté aprendiendo. Sí. Exacto."**

### Múltiples Capas

**"Los distintos modelos de lenguaje usan Transformers con distintas cantidad de bloques en el encoder y en el decoder."**

Estudiante: "Como los layers de la recurrente."

Profesor: **"Tal cual. Igualito."**

---

## Entrenamiento vs Inferencia

### Durante el Entrenamiento

**"La gran ventaja es que a la hora de entrenar podés pasar toda la frase, sobre todo en el encoder."**

### Durante la Inferencia

**"El encoder lo corres una vez por el input que tengas."**

**"El decoder lo que va a hacer es para cada una de las probabilidades vas a agarrar una palabra y la vas a volver a meter."**

Estudiante: "Hace como una recurrente."

Profesor: **"Sí, ahí no tiene otra que generar palabra por palabra."**

---

## Layer Normalization

### ¿Qué Es?

**"Es una capa que tiene como entrada un vector. Lo que hace es normaliza a lo largo de las coordenadas de ese vector, no como en el batch normalization que se normalizaba a lo largo del batch."**

### El Proceso

1. Restar la media del vector
2. Dividir entre el desvío del vector
3. Reescalar: multiplicar por gamma y sumar beta

**"Este gamma y este beta son aprendibles."**

**"Se hace secuencia a secuencia. No se hace a batch por batch, sino que se hace por palabrita."**

---

## Matrices Compartidas - Punto Clave

**"Lo único bueno es que es la misma matriz siempre. Son las mismas matrices siempre."**

**"Eso permite algo muy importante: que el transformer pueda procesar secuencias de cualquier longitud sin crecer."**

**"Si yo fijo el tamaño del embedding, ya está. Ya fijé la matriz. Puedo poner una palabra de longitud dos o una palabra de longitud 17."**

**"Puede procesar toda a la vez porque todo esto es en paralelo. No tiene que hacer 'thinking', después 'machines'. Hace todo en paralelo."**

---

## Por Qué Query, Key y Value (No 2 o 7)

### La Pregunta

Estudiante: "¿Por qué son 3 y no 2 o 7?"

### La Respuesta

**"Query, key, value tiene un sentido semántico."**

**"Es como buscar en un catálogo. Yo tengo un catálogo de fotos. Hago una query sobre ese catálogo. Las keys es el caption de cada foto. Y voy a tratar de matchear mi query con cada caption para devolverme el value que es la foto."**

**"Preciso solo esas tres cosas."**

---

## Recursos Recomendados

### El Blog "The Illustrated Transformer"

**"Está muy lindo este blog. Les va mostrando cómo se va haciendo todo cada uno a uno."**

### Tutorial de PyTorch

**"Si no lo han visto, mírenlo porque está bueno, está hecho con código. Si les cuesta entender [las fórmulas] es más fácil mirar código."**

### Los Papers Originales

1. **Bahdanau et al.**: El paper que introdujo Attention (con Yoshua Bengio)
2. **Vaswani et al.** - "Attention is All You Need": **"Es uno de los más citados de la historia"**

---

## Para el Parcial - LO QUE ENTRA

### La Confirmación Explícita

Estudiante: "¿Y qué es lo que entraría ahí en el parcial?"

Profesor: **"Desde Skip Connections en adelante."**

**"Skip connection fue lo que no quedó para el primero [parcial]."**

### Lista Completa de Temas

1. **Skip Connections / Residual Connections**
2. **Layer Normalization**
3. **Mecanismo de Attention (Bahdanau)**
4. **Query, Key, Value**
5. **Self-Attention**
6. **Scaled Dot-Product Attention**
7. **Positional Encoding** ← MUY IMPORTANTE (VA PARA PARCIAL)
8. **Multi-Head Attention**
9. **Arquitectura del Transformer**
10. **Máscara de Causalidad**
11. **Diferencias entre Entrenamiento e Inferencia**
12. **Feed-Forward Networks**

### Temas Especialmente Enfatizados

El profesor dijo **"Va para parcial"** sobre:
- La invariancia por permutaciones y por qué necesitamos positional encoding
- Skip connections (porque no entraron en el primer parcial)

---

## Resumen Ultra-Simplificado

### El Viaje Completo: De RNN a Transformers

**Paso 1: Seq2Seq Clásico**:
- Comprimes toda la frase en UN vector C fijo
- **Problema**: Pierdes información en frases largas

**Paso 2: Attention de Bahdanau**:
- Para cada palabra que vas a generar, miras TODO el input de nuevo
- Cada palabra tiene su propio contexto Cᵢ
- **Limitación**: Aún usa redes recurrentes (lento)

**Paso 3: Transformers**:
- Eliminas las redes recurrentes completamente
- SOLO usas attention (multi-head self-attention)
- Procesas todo en paralelo
- Agregas positional encoding para el orden
- **Resultado**: Mucho más rápido, escalable

### Los 3 Conceptos Clave

**1. Query (Q)**: Lo que buscas
**2. Key (K)**: Cómo te encuentran
**3. Value (V)**: Lo que devuelves

Cada palabra se convierte en las tres cosas (por eso se llama "self"-attention).

### Por Qué Es Revolucionario

**Antes (RNN/LSTM)**:
- Palabra 1 → Palabra 2 → Palabra 3 → ... (secuencial)
- No puedes paralelizar
- Lento de entrenar

**Ahora (Transformers)**:
- Todas las palabras se procesan al mismo tiempo
- Cada una mira a todas las demás
- Se entrena 10x-100x más rápido
- Escala a modelos gigantes (GPT, BERT, etc.)

### La Trampa y La Solución

**Trampa**: Self-attention es invariante al orden
- "El perro muerde al gato" = "Al gato muerde el perro" ← ¡MALO!

**Solución**: Positional Encoding
- Le sumas a cada palabra una "señal de posición"
- Usa ondas sinusoidales
- Ahora la posición 1 ≠ posición 2, aunque sea la misma palabra

---

## Consejos del Profesor

**"No quiero matarlos. Quiero que entiendan cómo funciona."**

**"Si les cuesta entender [las fórmulas] es más fácil mirar código."**

**"No se entreveren con esto de las matrices. Piensen en el diagrama."**

---

## Para Estudiar

1. **Entiende el flujo conceptual**: RNN → Attention → Self-Attention → Transformers
2. **Domina las analogías**: El diccionario, la biblioteca, el catálogo de fotos
3. **Entiende POR QUÉ** cada cosa:
   - Por qué Attention (vector fijo era limitante)
   - Por qué Self-Attention (para capturar contexto)
   - Por qué Positional Encoding (invariancia por permutaciones)
   - Por qué Multi-Head (capturar diferentes relaciones)
4. **No memorices todas las fórmulas**, pero entiende qué hace cada una
5. **Mira el código** del tutorial de PyTorch si las fórmulas te confunden

---

## FIN DEL DOCUMENTO

Este documento contiene TODO lo que el profesor dictó en la clase del 17-11-2025, explicado de la forma más simple posible para alguien que viene de otra disciplina y no sabe nada del tema.
