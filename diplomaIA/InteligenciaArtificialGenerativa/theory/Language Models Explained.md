Aquí está la explicación de Modelos de Lenguaje con la misma estructura que las de VAE, GAN y Difusión:

---

1. Idea central

Un modelo de lenguaje predice la siguiente palabra. Le das una secuencia de texto y te dice las probabilidades de todas las posibles continuaciones. Es un modelo autorregresivo (la misma idea que el modelo de Hinton con píxeles), pero aplicado a texto en vez de imágenes.

En vez de P(píxel₃ | píxel₁, píxel₂) es P(palabra₃ | palabra₁, palabra₂). La misma regla del producto, el mismo enfoque secuencial, la misma limitación de no poder paralelizar la generación.

2. El modelo es DETERMINÍSTICO

Para la misma entrada, el modelo SIEMPRE da la misma distribución de probabilidades. Lo que es aleatorio es el muestreo: la elección de cuál palabra tomar de esas probabilidades. Por eso una misma pregunta puede dar respuestas diferentes cada vez.

3. Tokenización

Las redes neuronales no entienden letras ni palabras, solo números. La tokenización convierte texto en secuencias de números. Los tokens no son necesariamente palabras completas; pueden ser pedazos de palabras (sub-palabras). Por ejemplo, "inteligencia" podría ser dos tokens: "intel" + "igencia".

Algoritmos comunes: BPE (Byte-Pair Encoding), WordPiece.

Regla de oro del profesor: "Un tokenizer va con un modelo. Una vez que está todo hecho, no se toca más el tokenizer."

3b. Embedding (convertir IDs en vectores con significado)

La tokenización convierte "gato" en un número como 234. Pero ese número suelto no le sirve a la red — es solo un código de barras, no dice nada sobre qué ES un gato.

El embedding convierte ese número/ID en una LISTA de números (un vector). "Gato" pasa de ser el número 234 a ser algo como [0.2, -0.5, 0.8, 0.1, ...] con muchos números (ej: 128 o 768 números).

¿Para qué una lista de números? Porque con listas se pueden representar relaciones. "Gato" = [0.2, -0.5, 0.8, ...] y "perro" = [0.3, -0.4, 0.7, ...] son vectores parecidos (ambos son animales). "Avión" = [-0.9, 0.6, -0.3, ...] es muy diferente. Palabras similares quedan CERCA, palabras distintas quedan LEJOS.

¿De dónde salen estos vectores? De una tabla gigante (una matriz) que tiene una fila por cada palabra del vocabulario. Para buscar el vector de "gato", se va a la fila 234 de la tabla. Esta tabla se APRENDE durante el entrenamiento — arranca con valores aleatorios y se va ajustando hasta que las relaciones entre palabras tengan sentido.

Entonces el flujo completo es: texto → tokenización (texto a IDs) → embedding (IDs a vectores con significado) → modelo.

4. El proceso de generación paso a paso

a. Tokenizar el prompt (texto de entrada) — convertirlo a números, y luego a vectores via embedding
b. Pasar la secuencia por el modelo
c. El modelo produce "logits" para cada palabra del vocabulario (números crudos, no son probabilidades)
d. Softmax convierte esos logits en probabilidades que suman 1
e. Muestrear un token de esas probabilidades
f. Si el token elegido es el token de fin de secuencia: terminar. Si no: agregar a la secuencia y repetir desde b.

5. Logits y Softmax

Los logits son la salida cruda del modelo: pueden ser cualquier número (positivos, negativos, lo que sea). NO son probabilidades.

Softmax los convierte en probabilidades:
- Todos los valores quedan entre 0 y 1
- Suman 1
- Los logits más altos se convierten en probabilidades más altas

¿Por qué no simplemente dividir cada logit por la suma total? Porque los logits pueden ser negativos, y dividir por algo negativo no da una probabilidad válida. Softmax usa la exponencial (e elevado a cada logit) que siempre da positivo, y después divide.

6. Estrategias de muestreo

Una vez que el modelo da las probabilidades, hay distintas formas de elegir el siguiente token:

Greedy: siempre elegir el más probable. Simple pero aburrido — tiende a repetirse.

Top-K: quedarse solo con las K más probables (ej: las 50 más probables) e ignorar el resto. Después elegir al azar entre esas K.

Top-P (Nucleus): incluir palabras hasta que la suma de sus probabilidades llegue a P (ej: 0.9 = 90%). Si una palabra tiene 80% de probabilidad, solo esa entra. Si la más probable tiene 20%, entran varias. Es más adaptativo que Top-K porque la cantidad de opciones varía según la situación.

Temperatura: divide los logits por T antes de aplicar softmax.
- T baja (ej: 0.3): las diferencias se amplían, la más probable domina. Más predecible.
- T alta (ej: 1.5): las diferencias se achican, todas se vuelven parecidas. Más creativo pero puede ser incoherente.
- T = 1: las probabilidades quedan tal cual.

7. La arquitectura: Transformers

¿Por qué se necesita una arquitectura especial? Porque para predecir la siguiente palabra, el modelo necesita entender contexto de largo alcance. En "El presidente de Francia visitó Alemania y dijo que su país...", el modelo necesita recordar que "su país" se refiere a Francia, muchas palabras atrás.

El Transformer resuelve esto con Self-Attention: un mecanismo que permite que cada palabra "mire" a todas las anteriores y decida cuáles son relevantes.

Cada token genera tres vectores:
- Query (Q): "¿qué información estoy buscando?"
- Key (K): "¿qué información tengo para ofrecer?"
- Value (V): "esta es mi información concreta"

Se calcula un puntaje entre cada par de tokens (Q × K), se normaliza con softmax, y se usa para ponderar los Values.

Causal Masking: se ponen puntajes de -infinito en las posiciones futuras. Después del softmax, esos -infinito se convierten en 0 (atención nula). Así cada token solo puede ver los anteriores, no el futuro. Es la misma idea que la matriz triangular de Hinton pero implementada de otra forma.

Multi-Head Attention: en vez de un solo "ojo" de atención, hay varios (ej: 12) en paralelo. Cada uno puede enfocarse en un aspecto diferente: gramática, tema, posición, etc.

Positional Encoding: como el Transformer procesa toda la secuencia de golpe (en paralelo), no sabe el orden de las palabras. Se le suman vectores de posición (funciones seno y coseno) para que sepa "esta es la posición 1, esta es la posición 2, etc."

Cada bloque del Transformer tiene:
1. Multi-Head Self-Attention
2. Skip connection + LayerNorm
3. Feed-Forward Network (dos capas Linear)
4. Skip connection + LayerNorm

📌 Entrenamiento (qué optimiza un modelo de lenguaje)

a) La pérdida: Cross-Entropy

Mide qué tan lejos está la predicción del modelo de la palabra correcta.

L = -log(probabilidad que el modelo le asignó a la palabra correcta)

Si el modelo dijo 90% para la palabra correcta: -log(0.9) ≈ 0.1 (pérdida baja, bien).
Si el modelo dijo 5% para la palabra correcta: -log(0.05) ≈ 3.0 (pérdida alta, mal).

Es esencialmente la misma idea que el Negative Log-Likelihood usado para entrenar el modelo autorregresivo de Hinton. Penaliza cuando el modelo asigna baja probabilidad al dato correcto.

b) El algoritmo de entrenamiento

Para cada texto del dataset:
1. Crear pares de entrada-salida: "El" → "gato", "El gato" → "come", "El gato come" → "pescado"
2. Pasar las entradas por el modelo → logits
3. Softmax → probabilidades
4. Cross-Entropy: comparar con la palabra correcta
5. Backpropagation y actualizar pesos

Diferencia clave con la generación: en entrenamiento se procesa todo en paralelo (ya se conocen todas las palabras), en generación hay que ir de a una.

c) Perplexity

La métrica principal para evaluar un modelo de lenguaje. Es el exponencial de la pérdida promedio:

Perplexity = exp(pérdida promedio)

Mide qué tan "sorprendido" se queda el modelo ante texto real. Si predice bien, la perplejidad es baja. Si predice mal, es alta. Baja = mejor.

Referencia: si el vocabulario tiene 50,000 palabras, perplejidad de 50,000 sería como adivinar al azar. Perplejidad de 20 es muy buena.

📌 Diferencia con los otros modelos del curso

a) Igual que Hinton pero para texto: misma regla del producto P(secuencia) = P(w₁) × P(w₂|w₁) × P(w₃|w₁,w₂)... Misma generación secuencial. Misma limitación de no poder paralelizar la generación.

b) Diferente a VAE y GAN: no hay espacio latente comprimido, no hay encoder-decoder (en el sentido de VAE), no hay discriminador. Es puramente autorregresivo: predecir el siguiente token dado los anteriores.

c) Training es paralelo, generación es secuencial: durante el entrenamiento, como ya se conoce todo el texto, se procesan todas las posiciones a la vez. Durante la generación, hay que ir de a un token porque cada uno depende del anterior.

📌 Uso después del entrenamiento

1. Generación
   Prompt → tokenizar → modelo → probabilidades → muestrear → token nuevo → repetir.
   Se va construyendo el texto de a un token hasta llegar al token de fin o al máximo permitido.

2. El modelo solo se usa completo
   No se descarta ninguna parte (a diferencia de GAN donde se descarta D, o de VAE donde para generar se descarta el encoder).

Diagrama

ENTRENAMIENTO (paralelo — todas las posiciones a la vez):

  ┌──────────────────────┐
  │ "El gato come pesca" │
  └──────────┬───────────┘
             │
             v
  ┌──────────────────────┐    Pares entrada → target:
  │     TOKENIZAR        │
  │  [15, 234, 89, 456]  │      [15]          → 234 ("gato")
  └──────────┬───────────┘      [15, 234]     → 89  ("come")
             │                  [15, 234, 89] → 456 ("pescado")
             v
  ┌──────────────────────┐   ┌──────────┐   ┌──────────┐   ┌─────────────┐
  │       MODELO         │   │          │   │          │   │ probabili-  │
  │    (Transformer)     │──>│  logits  │──>│ softmax  │──>│   dades     │
  │                      │   │          │   │          │   │             │
  └──────────────────────┘   └──────────┘   └──────────┘   └──────┬──────┘
                                                                  │
                                                                  v
                                                   ┌─────────────────────────┐
                                                   │ Loss = -log(prob de la  │
                                                   │    palabra correcta)    │
                                                   │    (Cross-Entropy)      │
                                                   └─────────────────────────┘


GENERACIÓN (secuencial — de a un token, en loop):

                      ┌─────────────────────────────────────────────────┐
                      │                                                 │
                      v                                                 │
  ┌──────────┐   ┌──────────────────┐   ┌────────┐   ┌─────────┐       │
  │  tokens  │   │     MODELO       │   │        │   │ softmax │       │
  │ actuales │──>│  (Transformer)   │──>│ logits │──>│  / T    │       │
  │          │   │                  │   │        │   │         │       │
  └──────────┘   └──────────────────┘   └────────┘   └────┬────┘       │
                                                          │            │
                                                          v            │
                                                   ┌────────────┐      │
                                                   │  muestrear │      │
                                                   │ (Top-K,    │      │
                                                   │  Top-P)    │      │
                                                   └─────┬──────┘      │
                                                         │             │
                                                         v             │
                                                  ┌─────────────┐     │
                                                  │ token nuevo │     │
                                                  └──────┬──────┘     │
                                                         │             │
                                           ┌─────────────┴──────┐     │
                                           │ ¿es fin de         │     │
                                           │  secuencia?        │     │
                                           └──┬─────────────┬───┘     │
                                              │             │         │
                                           Sí v          No v         │
                                         ┌────────┐  agregar token    │
                                         │ PARAR  │  a la secuencia ──┘
                                         └────────┘


Resumen final

Texto → tokenizar → números → modelo → logits → softmax → probabilidades → muestrear → token
Loss = -log(probabilidad de la palabra correcta) = Cross-Entropy = misma idea que NLL de Hinton
El modelo es determinístico, la aleatoriedad viene del muestreo (Top-K, Top-P, Temperatura)
Transformers: Self-Attention (Q,K,V) + Causal Masking + Multi-Head + Positional Encoding
Entrenamiento paralelo, generación secuencial (de a un token)

Si quieres, puedo darte una versión aún más compacta para memorizar o una lista de puntos clave tipo machete para el examen.
