# Explicaciones de la Clase 12 - 24 de Noviembre de 2025
## CLASE DE REPASO PARA EL PARCIAL

---

# ANTES DE EMPEZAR: Conceptos Básicos que Necesitas Saber

Esta clase es un **REPASO** para el parcial. El profesor revisó temas de clases anteriores y resolvió ejercicios tipo examen. Antes de entrar en los detalles, asegurémonos de entender algunos conceptos básicos:

## ¿Qué es un Parcial de Deep Learning?

Un parcial es un examen donde te van a hacer preguntas sobre los temas vistos en clase. En este caso:
- **Preguntas escritas**: 2-3 preguntas aproximadamente
- **Defensa**: Explicar tu taller
- **No es solo teoría**: También hay ejercicios de cálculo

## ¿Por qué esta clase es importante?

El profesor dijo exactamente qué tipo de preguntas van a aparecer y cómo estudiar. Si entiendes esta clase, tienes una gran ventaja para el parcial.

## Conceptos que debes recordar de clases anteriores:

1. **Transformer**: Una arquitectura de red neuronal que procesa secuencias (como texto) de forma paralela
2. **RNN (Red Neuronal Recurrente)**: Procesa secuencias de forma secuencial, una palabra a la vez
3. **Attention**: Un mecanismo que permite a la red "prestar atención" a diferentes partes de la entrada
4. **Encoder-Decoder**: Una arquitectura que tiene dos partes: una que "entiende" la entrada y otra que genera la salida
5. **Gradiente**: La dirección en la que la red debe ajustar sus pesos para mejorar
6. **Parámetro**: Un número que la red aprende durante el entrenamiento (los pesos)

---

# PARTE 1: EJERCICIO DE CÁLCULO DE PARÁMETROS DE TRANSFORMER

## 1.1 ¿Por qué es importante este ejercicio?

El profesor dijo: **"Forzarse a calcular los parámetros es como que te fuerza a entender la arquitectura de punta a punta de la red."**

Esto significa: si puedes calcular cuántos parámetros tiene cada parte del Transformer, entonces realmente entiendes cómo funciona.

## 1.2 Los Hiperparámetros del Ejercicio

El profesor dio estos datos:

| Nombre | Símbolo | Valor | ¿Qué significa? |
|--------|---------|-------|-----------------|
| Vocabulario de entrada | vocab_source | 5,000 | Cuántas palabras diferentes puede recibir |
| Vocabulario de salida | vocab_target | 6,000 | Cuántas palabras diferentes puede generar |
| Dimensión del modelo | D_model | 128 | El "tamaño" de cada vector que representa una palabra |
| Número de cabezas | H | 4 | Cuántas "perspectivas" diferentes usa la atención |
| Dimensión feed-forward | D_FF | 512 | El tamaño de la capa intermedia del MLP |
| Bloques de encoder | N_encoder | 2 | Cuántas veces se repite el encoder |
| Bloques de decoder | N_decoder | 2 | Cuántas veces se repite el decoder |

## 1.3 ¿Qué es un Parámetro?

Imagina que tienes una receta de cocina. Los **parámetros** son como los "ajustes" de la receta:
- ¿Cuánta sal? (un número)
- ¿Cuánto tiempo de cocción? (otro número)
- ¿A qué temperatura? (otro número más)

En una red neuronal, cada parámetro es un número que la red aprende. Más parámetros = más capacidad de aprender cosas complejas.

## 1.4 Calculando Parámetros del Multi-Head Attention

### ¿Qué es el Multi-Head Attention?

Es el corazón del Transformer. Permite que la red "preste atención" a diferentes partes de la entrada.

El profesor explicó: **"Cada una de las cabezas captura distintas relaciones semánticas, de sintaxis, distintas relaciones temporales."**

### Los componentes:

Para cada cabeza de atención, necesitamos:
- **WQ** (matriz de Query): convierte la entrada en "preguntas"
- **WK** (matriz de Key): convierte la entrada en "claves"
- **WV** (matriz de Value): convierte la entrada en "valores"
- **Biases**: pequeños ajustes adicionales

### Dimensiones clave:

- D_K = D_model / H = 128 / 4 = **32**
- D_V = D_model / H = 128 / 4 = **32**

**Pregunta de estudiante:** "¿Por qué D_K = D_model / H?"

**Respuesta del profesor:** "Lo usual es eso, pero teóricamente no tenés restricciones. En la multiplicación: Q·K^T el DK desaparece, entonces la matemática no te restringe ahí. Pero lo estándar es usar D_model / H porque facilita la implementación como una única matriz."

### Cálculo paso a paso:

**Paso 1: Matrices WQ, WK, WV (una cabeza)**
- Cada matriz: 128 × 32 = 4,096 parámetros
- Son 3 matrices: 3 × 4,096 = **12,288 parámetros**

**Paso 2: Biases (una cabeza)**
- Cada bias: 32 parámetros
- Son 3 biases: 3 × 32 = **96 parámetros**

**Paso 3: Multiplicar por 4 cabezas**

El profesor enfatizó: **"Nos olvidamos de contar que hay cuatro heads."**

- Matrices: 12,288 × 4 = **49,152 parámetros**
- Biases: 96 × 4 = **384 parámetros**

**Paso 4: Matriz de salida WO**
- Concatenamos 4 cabezas de 32 = 128
- Salida: 128
- Matriz WO: 128 × 128 = **16,384 parámetros**
- Bias BO: **128 parámetros**

**TOTAL Multi-Head Attention:**
```
49,152 + 384 + 16,384 + 128 = 66,048 parámetros
```

## 1.5 Calculando Parámetros del Layer Normalization

### ¿Qué es Layer Normalization?

Es como "estandarizar" los valores. Imagina que tienes estudiantes con notas de 0-100 y otros de 0-10. Para compararlos, los normalizas.

El profesor explicó: **"El layer normalization lo que hace es normalizar fila a fila. Le resta la media de la fila, divide entre el desvío estándar de la fila, multiplica por gamma y suma beta."**

### Parámetros:
- **Gamma (γ)**: 128 parámetros (uno por dimensión)
- **Beta (β)**: 128 parámetros (uno por dimensión)
- **Total por layer norm: 256 parámetros**

En el encoder hay 2 layer norms (después de attention y después de feed-forward).
En el decoder hay 3 layer norms.

## 1.6 Calculando Parámetros del Feed-Forward

### ¿Qué es el Feed-Forward?

Es un MLP (perceptrón multicapa) simple de 2 capas. Procesa cada palabra individualmente.

### Estructura:
- **Capa 1**: D_model → D_FF (128 → 512)
- **Capa 2**: D_FF → D_model (512 → 128)

### Cálculo:

**Capa 1:**
- Matriz: 128 × 512 = 65,536
- Bias: 512
- Subtotal: (128 + 1) × 512 = **66,048 parámetros**

**Capa 2:**
- Matriz: 512 × 128 = 65,536
- Bias: 128
- Subtotal: (512 + 1) × 128 = **65,664 parámetros**

**TOTAL Feed-Forward: 131,712 parámetros**

Un estudiante notó: **"66,048 otra vez."**

El profesor confirmó: **"Sí, sí, sí. Lo mismo que el multihead."**

## 1.7 Calculando un Bloque de Encoder Completo

Un bloque de encoder tiene:
- 1 × Multi-Head Attention: 66,048
- 2 × Layer Norm: 2 × 256 = 512
- 1 × Feed-Forward: 131,712

**Total por bloque: 198,272 parámetros**

Con 2 bloques: **396,544 parámetros**

## 1.8 Calculando un Bloque de Decoder Completo

Un bloque de decoder tiene:
- 1 × Masked Multi-Head Attention: 66,048
- 1 × Cross-Attention (encoder-decoder): 66,048
- 3 × Layer Norm: 3 × 256 = 768
- 1 × Feed-Forward: 131,712

**Total por bloque: 264,576 parámetros**

Con 2 bloques: **529,152 parámetros**

**Pregunta de estudiante:** "¿Por qué el decoder tiene más parámetros?"

**Respuesta:** Porque tiene DOS mecanismos de atención (self-attention y cross-attention) en lugar de uno.

## 1.9 Calculando los Embeddings

### ¿Qué es un Embedding?

Es una matriz que convierte palabras en vectores. Cada palabra del vocabulario tiene su propio vector de D_model dimensiones.

### Cálculo:

**Input Embedding (encoder):**
- vocab_source × D_model = 5,000 × 128 = **640,000 parámetros**

**Output Embedding (decoder):**
- vocab_target × D_model = 6,000 × 128 = **768,000 parámetros**

**Total Embeddings: 1,408,000 parámetros**

**Pregunta de estudiante:** "Los embeddings también son aprendidos, ¿no?"

**Respuesta del profesor:** "Los embeddings son aprendidos."

## 1.10 Calculando la Capa Lineal Final

Esta capa convierte la salida del decoder (128 dimensiones) al vocabulario de salida (6,000 palabras).

### Cálculo:
- Matriz: 128 × 6,000 = 768,000
- Bias: 6,000
- **Total: (128 + 1) × 6,000 = 774,000 parámetros**

## 1.11 TOTAL DE PARÁMETROS DEL TRANSFORMER

```
Encoder Blocks:           396,544
Decoder Blocks:           529,152
Input Embedding:          640,000
Output Embedding:         768,000
Output Linear Layer:      774,000
─────────────────────────────────
TOTAL:                  3,107,696 parámetros
```

**Aproximadamente: 3.1 millones de parámetros**

El profesor comentó: **"Pero es un transformer chiquito, ¿no? 4 heads, 128 de D_model. Fíjense que digo, ¿cuánto tiene el transformer? Creo que era 512 el D_model."**

Y sobre GPT-3: **"No sé cuántas capas... debe tener 100,000 no sé... 200,000... o sea esto es un mini transformer."**

---

# PARTE 2: ARQUITECTURA DEL TRANSFORMER - REPASO

## 2.1 La Idea General

El profesor explicó: **"Lo que el encoder aprende es una representación eficiente, comprime la información o la codifica de alguna forma, encuentra una representación latente que se la va a pasar al decoder y el decoder aprende a decodificar esa información."**

### Analogía Simple:

Imagina que quieres traducir un libro de español a inglés:

1. **Encoder** = Un lector muy inteligente que lee todo el libro en español y lo "entiende"
2. **Representación latente** = Las ideas principales del libro (no las palabras exactas)
3. **Decoder** = Un escritor que toma esas ideas y las escribe en inglés

## 2.2 Self-Attention vs Cross-Attention

### Self-Attention (todos contra todos):

El profesor dijo: **"El self attention es todos contra todos. Cuando vos mirás todos contra todos, cada fila te dice: cuando vas a predecir esta palabra, ¿a qué cosas le presta atención?"**

### Cross-Attention (encoder-decoder):

**"En la segunda atención que combina encoder con decoder: las queries son las palabras del decoder, los keys y los values vienen del encoder. Para cada palabra del decoder, me va a decir: bueno, esta palabra, ¿cómo se relaciona con las palabras que estaban en español?"**

## 2.3 Positional Encoding

### ¿Por qué se necesita?

El profesor explicó: **"Se necesita marcar la posición temporal porque aquí no hay ningún tipo de recurrencia. Se le pasa la frase entera, no hay orden. El self attention es invariante bajo permutación, entonces necesito marcar en qué posición está cada palabra."**

### Analogía:

Imagina que tienes las palabras "gato", "el", "negro" en una bolsa. Sin orden, podrían significar:
- "el gato negro"
- "negro el gato"
- "gato negro el"

El Positional Encoding es como numerar cada palabra: "1-el", "2-gato", "3-negro".

## 2.4 La Máscara en el Decoder

### ¿Por qué se necesita?

El profesor explicó: **"Data leakage temporal: el decoder va a recibir toda la secuencia. Cuando va a aprender a hacer la predicción de la palabra en el tiempo t sin poder mirar la palabra que está en tiempo T, le vas a multiplicar por una máscara que todo lo que está después no lo vea."**

### Analogía:

Imagina que estás haciendo un examen:
- **Sin máscara**: Puedes ver todas las respuestas antes de responder (trampa)
- **Con máscara**: Solo puedes ver las respuestas que ya escribiste (justo)

Durante el entrenamiento, el Transformer ve toda la secuencia de salida. La máscara evita que "haga trampa" mirando las palabras futuras.

## 2.5 Training vs Inference

### Durante el Entrenamiento:

- El encoder procesa toda la frase de entrada en paralelo
- El decoder recibe toda la secuencia objetivo (con máscara)
- Todo se procesa en paralelo

### Durante la Inferencia:

El profesor dijo: **"En diferencia sí, tenés que hacer uno a uno... En inferencia tenemos un loop. Sí. Sí o sí."**

- El encoder procesa la entrada (una sola vez)
- El decoder genera palabra por palabra
- Cada palabra nueva se agrega como entrada para generar la siguiente

**Pregunta de estudiante:** "¿Ah, pero o sea, acá no hay recurrencia, pero sí va a haber un loop?"

**Respuesta del profesor:** "Hay loop solo en el decoder. En el decoder. Exacto."

---

# PARTE 3: COMPARACIÓN TRANSFORMER VS RNN

## 3.1 La Diferencia Fundamental

El profesor explicó: **"Visto como caja negra este [RNN seq2seq] y es eso [Transformer]. O sea, es lo mismo, solo que la caja negra de la RN procesa el input paso a paso secuencialmente. Esto lo procesa todo de una."**

### Tabla de Comparación:

| Aspecto | RNN | Transformer |
|---------|-----|-------------|
| Procesamiento | Secuencial (una palabra a la vez) | Paralelo (todas a la vez) |
| Recurrencia | Sí | No |
| Memoria temporal | Hidden state | Positional Encoding + Attention |
| Self-attention | No (solo attention con encoder) | Sí |
| Velocidad de entrenamiento | Lento | Rápido |
| Memoria a largo plazo | Limitada (incluso con LSTM) | Excelente |

## 3.2 Ventaja del Transformer en Memoria a Largo Plazo

El profesor dijo: **"Una LSTM tiene memoria a largo plazo mucho mejor que una RN común. La atención, o sea, el attention considera toda la secuencia de hidden, ¿no? Nos va concentrando en un solo hidden pasando. O sea, a largo plazo no hay comparación."**

### Analogía:

Imagina que estás leyendo un libro muy largo:

- **RNN**: Es como leer sin poder volver atrás. Solo recuerdas lo más reciente.
- **LSTM**: Es como tener notas pegadas en algunas páginas importantes.
- **Transformer con Attention**: Es como tener el libro completo abierto frente a ti, pudiendo mirar cualquier página instantáneamente.

## 3.3 ¿Cuándo el Costo del Transformer es Prohibitivo?

**Pregunta de estudiante:** "¿A qué se refiere costo prohibitivo?"

**Respuesta del profesor:** "Muy alto. Costo de... exagerado."

El Transformer tiene complejidad O(n²) donde n es la longitud de la secuencia. Con secuencias muy largas (miles de tokens), el costo se vuelve prohibitivo.

---

# PARTE 4: RESNETS Y SKIP CONNECTIONS - REPASO

## 4.1 El Problema de Degradación

El profesor explicó: **"¿Por qué en principio, si voy a aumentar el número de capas no deberían pedir el rendimiento?"**

Y la respuesta: **"La respuesta es que vos en teoría la capa del medio, existe la posibilidad que la capa del medio sea la identidad y entonces el modelo se te reduce al que tiene una capa media. Todo lo que puedas expresar con dos capas lo puedes expresar con tres."**

### ¿Qué significa esto?

Si agregas más capas a una red, en teoría no debería empeorar porque las capas extra podrían simplemente "no hacer nada" (ser la identidad). Pero en la práctica, entrenar esas capas extra es muy difícil.

## 4.2 Vanishing Gradient vs Exploding Gradient

### Vanishing Gradient (Gradiente que Desaparece):

Los gradientes se hacen muy pequeños. Las capas iniciales casi no se actualizan.

El profesor dijo: **"Pero el tema es si te estás frenando, o sea, si estás yendo demasiado rápido frenar podés, pero si te estás frenando acelerar no podés."**

### Exploding Gradient (Gradiente que Explota):

Los gradientes se hacen muy grandes. Los pesos oscilan sin control.

El profesor comentó: **"El explodient sí oscila como loco, pero llegaba algún momento a [convergencia]... Además, el explodient es más fácil de controlar porque puede ser para arriba o para abajo también."**

## 4.3 Skip Connections como Solución

La idea de ResNet: **H(x) = F(x) + x**

El profesor explicó: **"Justamente esa era la idea de la ResNet, justamente cuánto te desvías de la identidad."**

### ¿Por qué funciona?

La derivada de H(x) respecto a x es:
```
dH/dx = dF/dx + 1
```

El "+1" garantiza que los gradientes nunca desaparezcan completamente.

### ⚠️📝 POSIBLE PREGUNTA DE PARCIAL ✅

El profesor dijo que esta pregunta está en la guía de estudio:

**"Justifique conceptualmente por qué una red más profunda puede entrenar peor que una red más superficial, incluso teniendo mayor capacidad representacional."**

**Respuesta esperada:**
1. En teoría, los pesos pueden ser la identidad (no hacer nada)
2. Entonces una red profunda puede replicar una superficial
3. Pero el vanishing gradient impide que el optimizador encuentre esos pesos
4. Los gradientes se vuelven muy pequeños en las capas iniciales
5. Skip connections solucionan esto con el "+1" en la derivada

---

# PARTE 5: BACKPROPAGATION THROUGH TIME (BPTT)

## 5.1 ¿Qué es BPTT?

El profesor explicó: **"Está esto es sobre back propagation time, que se acuerdan que simplemente es desplegar la red, una cierta cantidad de pasos y hacer back propagation como corriente."**

### Analogía:

Imagina una RNN como un acordeón cerrado. BPTT es como abrir el acordeón y ver todas las "copias" de la red, una para cada paso de tiempo. Luego calculas los gradientes como si fuera una red normal muy larga.

## 5.2 ¿Para qué sirve?

**"¿Para qué uno hace eso? Para evitar el vanishing gradient o el explodient."**

Si despliegas solo unos pocos pasos en lugar de toda la secuencia, los gradientes no tienen que multiplicarse tantas veces.

## 5.3 Si la Matriz B es Nula

**Pregunta de parcial mencionada:** "En una red recurrente, escriba qué ocurriría si B fuese la matriz nula."

**Respuesta del profesor:** "Si fuese cero... es un MLP."

Si no hay conexiones recurrentes (B=0), la red no puede "recordar" información de pasos anteriores. Se convierte en un MLP simple que procesa cada entrada independientemente.

---

# PARTE 6: LANGUAGE MODELS - REPASO

## 6.1 ¿Qué es un Language Model?

Un modelo que predice la siguiente palabra dado un contexto de palabras anteriores.

## 6.2 Construcción de Datos de Entrenamiento

### Con Ventana Fija (MLP):

El profesor explicó: **"Si lo implementan con un MLP, por ejemplo, que tiene que tener un largo fijo, agarran una ventana de largo fijo y la van corriendo en el texto."**

**Ejemplo del profesor con el texto "El perro corre rápido. El perro es feliz.":**

```
Entrada: [El, perro, corre] → Salida: rápido
Entrada: [perro, corre, rápido] → Salida: .
Entrada: [corre, rápido, .] → Salida: El
... y así sucesivamente
```

### Con N-gramas (Bigramas):

**"Si fuera un grama es: el perro. Perro corre, corre rápido, rápido. Punto. Punto. Él... el perro perro es, es feliz, feliz punto."**

```
el → perro
perro → corre
corre → rápido
rápido → .
. → El
El → perro
perro → es
es → feliz
feliz → .
```

### Con RNN:

**"Pero si lo hacen con una recurrente que puede tomar cualquier longitud, de repente pueden agarrar de todas las actitudes. Se agarran el 1, 3 y 4 g de todas las ventanas posibles."**

La RNN es más flexible: puede recibir secuencias de cualquier longitud.

---

# PARTE 7: TOKENS ESPECIALES

## 7.1 Beginning of Sequence (BOS)

El profesor explicó: **"En el encoder la meto... en el decoder meto algo, meto el begin of sequence."**

**Pregunta:** "¿Dónde entra la frase en español durante inferencia?"

**Respuesta:** "La frase en español entra en el encoder. Después en el decoder entra el BEGIN_OF_SEQUENCE. Sin eso no podes arrancar. Recién con eso sacas la primer palabra."

## 7.2 End of Sequence (EOS)

**"Va a pasar por el end of sequence... la última no hay una próxima."**

El decoder genera palabras hasta que produce el token EOS.

---

# PARTE 8: MAPAS DE ATENCIÓN

## 8.1 ¿Cómo se Leen?

El profesor preguntó: **"¿Cómo lo importante es cómo se leen estos? Tienen que hacer... tienen que llenar las columnas o tienen que llenar la fila?"**

**Estudiantes:** "Las filas."

**Profesor:** "Las filas, ¿verdad?"

### Interpretación:

Cada **fila** representa una palabra de salida. Los valores en esa fila muestran cuánta atención presta a cada palabra de entrada.

### Ejemplo del profesor (traducción español-inglés):

Se muestra una tabla donde hay que completar con "alta", "media", "baja":
- Cuando predices "book", ¿a qué palabra en español prestas más atención? → "libro" (alta)
- Cuando predices "the", ¿a qué prestas atención? → "el" (alta)

---

# PARTE 9: PREGUNTAS TIPO PARCIAL

## 9.1 Preguntas del Parcial del Año Pasado Revisadas

El profesor revisó el parcial 2 del año pasado y mencionó estas preguntas:

### Pregunta 1: Diagrama de Atención
"¿Qué operación se está realizando en el siguiente diagrama? Explique con el mayor nivel de detalle posible."

**Respuesta esperada:** Explicar Q, K, V, las matrices de peso, la fórmula softmax(Q·K^T/√dk)·V.

### Pregunta 2: Elementos del Transformer
"Explique en más de tres renglones los siguientes elementos:"
- Input Embedding
- Output Embedding
- Positional Encoding
- Multihead Attention
- Masked Multihead Attention
- Layer Normalization
- Skip Connections
- Feed-Forward
- Capa lineal final
- Softmax

### Pregunta 3: Seq2Seq con RNN
"Explique con ejemplos y pseudocódigo cómo implementaría el paso de codificación (encoding) y decodificación (decoding) de una secuencia en un modelo seq2seq."

**El profesor dijo:** "El pseudocódigo es digo para cada palabra... es como una recetita de paso a paso."

### Pregunta 4: Beneficios de Encoder-Decoder
"¿Qué beneficios tiene un modelo encoder-decoder para los problemas seq2seq frente a un modelo que emite un output en cada paso de la secuencia?"

**Respuesta clave:** La salida puede ser de diferente longitud que la entrada.

### Pregunta 5: Diferencias Transformer vs RNN
"¿Qué diferencias tiene implementar el punto uno con una RN o con un modelo de tipo Transformer?"

**Respuestas clave:**
- Procesamiento paralelo vs secuencial
- Atención sobre toda la secuencia
- Sin recurrencia

### Pregunta 6: Problemas que Resuelve Self-Attention
"¿Qué problemas específicos de las RN resuelve la autoatención (self-attention) en los Transformers?"

**Respuesta:** Memoria a largo plazo. El attention considera toda la secuencia, no solo los últimos tokens.

### Pregunta 7: Papel de las Máscaras
"Explique el papel de las máscaras en el mecanismo de atención de un Transformer."

**Respuesta:** Evitar data leakage temporal. El decoder no debe ver palabras futuras.

## 9.2 Consejos del Profesor para Estudiar

1. **"Usen esto como guía de estudio, de tratar de responder estas preguntas cuando están estudiando el tema."**

2. **"Forzarse a calcular los parámetros es como que te fuerza a entender la arquitectura de punta a punta."**

3. **"Cuando lean teoría, miren ejercicio. Eso ayuda a asociar."**

4. El profesor mencionó que los ejercicios largos de cálculo de parámetros no van a aparecer completos en el parcial, pero **"sí una partecita"**.

---

# PARTE 10: INFORMACIÓN ADMINISTRATIVA

## 10.1 Estructura del Parcial

- **Defensa**: No es solo defensa, hay más
- **Preguntas escritas**: 2-3 preguntas aproximadamente
- **Formato**: Escribir en "letra de máquina" (legible)

## 10.2 Temas que NO Entran

El profesor aclaró: **"Zero-shot learning. Esto no lo vimos que es transfer... no nos dieron clases."**

**NO estudiar:**
- Zero-Shot Learning
- Transfer Learning
- Modelo CLIP

## 10.3 Entregas y Talleres

- Taller 1 y Taller 2 tienen fechas de entrega
- Competencias Kaggle suman puntos extra
- Las competencias anteriores se cierran

## 10.4 Contacto

El profesor dijo: **"Cualquier cosa de orden, me escriben a mí con copia, Martín. Teams, no lo más fácil."**

---

# RESUMEN FINAL: LO MÁS IMPORTANTE PARA EL PARCIAL

## 1. Transformer (Tema Principal)
- Entender la arquitectura completa
- Saber calcular parámetros (al menos parcialmente)
- Diferencia entre self-attention y cross-attention
- Por qué se necesita la máscara
- Por qué se necesita positional encoding
- Diferencia entre training e inference

## 2. Comparación Transformer vs RNN
- Paralelo vs secuencial
- Memoria a largo plazo
- Ventajas y desventajas

## 3. ResNets y Skip Connections
- Por qué redes más profundas pueden entrenar peor
- Vanishing gradient
- Cómo las skip connections solucionan esto

## 4. Seq2Seq
- Encoder-decoder
- Teacher forcing
- Pseudocódigo de codificación y decodificación

## 5. Language Models
- Construcción de datos de entrenamiento
- N-gramas
- Ventana fija vs RNN

---

# ⚠️ RECORDATORIO FINAL

El profesor cerró la clase con un comentario humano:

**"Aparte de todo eso, también tenemos trabajo, familia, hijos. No te olvides..."**

Estudia con calma, pero estudia bien. ¡Éxito en el parcial!
