Aquí está la explicación de Transformers, Self-Attention y Multi-Head Attention:

---

0. ¿Qué ES un Transformer? (la confusión más común)

Un Transformer NO es un modelo generativo como VAE, GAN o Difusión. Un Transformer es una ARQUITECTURA — es decir, un tipo de red neuronal, una forma de organizar capas y conexiones.

La diferencia es como la diferencia entre "motor" y "auto":
- Motor = arquitectura (una pieza que se usa DENTRO de algo más grande)
- Auto = modelo completo (el sistema entero que hace algo útil)

Ejemplos de arquitecturas: MLP (capas lineales), CNN (convoluciones), RNN (recurrencia), Transformer (attention).
Ejemplos de modelos completos: VAE, GAN, Difusión, GPT.

Un modelo completo ELIGE una arquitectura para funcionar:
- VAE usa CNN como arquitectura
- GAN usa CNN como arquitectura
- Difusión usa U-Net como arquitectura
- GPT usa Transformer como arquitectura
- Stable Diffusion usa TRES arquitecturas juntas: CNN (VAE) + U-Net + Transformer (CLIP)

Entonces: cuando decimos "Transformer", hablamos de la ESTRUCTURA de la red, no de un modelo generativo en sí. GPT es un modelo generativo que USA un Transformer adentro. Es como decir "mi auto usa un motor V8" — el V8 es la arquitectura, el auto es el modelo.

1. Idea central

El Transformer es una arquitectura que reemplaza por completo la recurrencia (RNN). En vez de procesar palabras una por una en orden, procesa toda la frase de una vez. Tiene dos partes principales:

- Encoder (izquierda): procesa la entrada (ej: frase en español). Comprime la información en una representación.
- Decoder (derecha): genera la salida (ej: frase en inglés). Decodifica esa representación.

El profesor lo explicó así: "El encoder aprende una representación eficiente, comprime la información o la codifica de alguna forma, encuentra una representación latente que se la va a pasar al decoder y el decoder aprende a decodificar esa información."

Pensarlo como un traductor: entra una frase en un idioma, sale en otro.

No todos los modelos usan las dos partes:
- Traducción (paper original): usa Encoder + Decoder completo
- GPT (generar texto): usa SOLO el Decoder (no necesita Encoder porque no "traduce" de una entrada a otra, solo continúa texto)
- BERT (entender texto): usa SOLO el Encoder (no genera, solo analiza)

2. Los bloques se repiten N veces (pero NO es recurrencia)

El Encoder y el Decoder están compuestos por bloques que se repiten N veces (ej: N=2, N=6). Pero ojo: cada bloque tiene sus propios pesos independientes. NO se reutilizan los mismos pesos como en las RNN.

"Cada vez es como si fueran capas distintas para cada bloque. No es una recurrencia. Son N capas de encoder o de decoder. Lo estándar es que cada una tenga sus propios pesos, sus propios parámetros."

3. Self-Attention: el mecanismo central

¿Qué problema resuelve? El modelo necesita saber qué palabras están relacionadas entre sí. En "El presidente de Francia visitó Alemania y dijo que su país...", necesita saber que "su país" se refiere a Francia.

Self-Attention es un mecanismo donde TODAS las palabras se comparan con TODAS para ver quién está relacionado con quién. Es un "todos contra todos".

¿Cómo funciona? Ejemplo concreto primero:

Frase: "El gato se sentó en la alfombra porque estaba cansado"

Cuando el modelo procesa la palabra "estaba", necesita averiguar: ¿"estaba" se refiere al gato o a la alfombra? Para eso, "estaba" se compara con TODAS las demás palabras y decide: "le presto 70% de atención a gato, 10% a alfombra, 5% a sentó, etc." Después, la representación de "estaba" se actualiza mezclando la información de todas las otras palabras, pero sobre todo la de "gato" (porque le dio más peso).

ESO es Self-Attention. Ahora veamos cómo lo calcula.

Paso a paso con analogía de Google:

Imaginá que Google funciona así: vos escribís una búsqueda, Google compara tu búsqueda con los títulos de todas las páginas, y te devuelve el contenido de las páginas que más coincidan.

En Self-Attention pasa lo mismo, pero cada palabra hace su propia búsqueda contra todas las demás:

a) Cada palabra se transforma en tres cosas distintas (multiplicándola por tres matrices de pesos diferentes):

- Q (Query) = la búsqueda de Google. Es lo que esa palabra está preguntando. "Estaba" pregunta: "¿quién es el sujeto que está cansado?"
- K (Key) = el título de la página. Es lo que esa palabra anuncia. "Gato" anuncia: "soy un sustantivo, soy un ser vivo, soy el sujeto."
- V (Value) = el contenido de la página. Es la información real que se va a usar. "Gato" tiene la información concreta sobre qué es el gato.

La Q, K y V de cada palabra son vectores distintos porque se multiplican por matrices distintas (W_Q, W_K, W_V). El modelo APRENDE estas matrices durante entrenamiento.

b) Se compara la búsqueda de cada palabra con los títulos de todas las demás: Q × K^T. Esto da un puntaje de compatibilidad entre cada par. Si la búsqueda de "estaba" coincide mucho con el título de "gato", ese puntaje será alto.

El resultado es una tabla de N×N (N = cantidad de palabras). Cada fila dice: "para esta palabra, ¿cuánto coincide su búsqueda con el título de cada otra palabra?"

c) Se divide por √d_k. Esto es solo un detalle técnico: sin esta división, los números pueden ser demasiado grandes y el softmax del siguiente paso se saturar (dar casi 100% a uno y 0% al resto). Dividir los achica para que el softmax funcione bien.

d) Softmax fila a fila: convierte esos puntajes en porcentajes que suman 100%. Ahora cada fila dice: "le presto 70% de atención a gato, 10% a alfombra, 5% a sentó..."

e) Se mezcla el contenido: esos porcentajes se usan para mezclar los Values (el contenido real) de todas las palabras. Si "estaba" le prestó 70% a "gato", la nueva representación de "estaba" va a ser 70% el contenido de "gato" + 10% el de "alfombra" + 5% el de "sentó" + ...

La fórmula completa (todo lo anterior en una línea):

Attention = softmax(Q × K^T / √d_k) × V
              ↑         ↑        ↑       ↑
         porcentajes  búsqueda  títulos  contenido
                      vs títulos  traspuestos  que se mezcla

Resumen ultra-corto:
1. Cada palabra genera una búsqueda (Q), un título (K) y un contenido (V)
2. Se comparan todas las búsquedas con todos los títulos → puntajes
3. Softmax → porcentajes de atención
4. Se mezclan los contenidos según esos porcentajes → nueva representación de cada palabra

4. Las dimensiones (shapes)

Esto es crucial para entender y para el parcial:

Si tenemos N palabras y d_model = 128:

- Entrada Z (la frase): N × d_model (N × 128)
- W_Q, W_K: d_model × d_k (128 × 32)
- W_V: d_model × d_v (128 × 32)
- Q = Z × W_Q: N × d_k (N × 32)
- K = Z × W_K: N × d_k (N × 32)
- V = Z × W_V: N × d_v (N × 32)
- Q × K^T: N × N (la matriz de atención, todos contra todos)
- softmax(Q × K^T / √d_k): N × N (probabilidades)
- Salida (× V): N × d_v (N × 32)

Observación clave: la dimensión N (largo de la frase) queda "peladita" en todas las multiplicaciones. Por eso el Transformer puede consumir frases de cualquier longitud.

5. Multi-Head Attention

En vez de hacer Self-Attention una sola vez, se hace varias veces en paralelo. Cada "cabeza" (head) usa sus propias matrices W_Q, W_K, W_V y puede capturar un aspecto diferente:

- Una cabeza puede enfocarse en relaciones semánticas (significado)
- Otra en relaciones sintácticas (gramática)
- Otra en relaciones temporales (posición)

"Lo de multihead es simplemente hacer attention varias veces, con la esperanza de que cada una de ellas capture distintas relaciones semánticas, de sintaxis, distintas relaciones temporales."

¿Cómo se combinan las cabezas? Se concatenan los resultados y se multiplican por una matriz W_O que lleva todo de vuelta a la dimensión d_model:

- Cada cabeza produce: N × d_v
- Se concatenan H cabezas: N × (H × d_v)
- Se multiplica por W_O: N × d_model

El estándar es que d_k = d_v = d_model / H. Así, con d_model=128 y H=4: d_k = d_v = 32. "Es para facilitarte la implementación. Se puede implementar como una sola multiplicación de matrices grande y después dividir el resultado en H partes."

6. Causal Masking (Masked Attention)

Se usa en el Decoder para que cada palabra NO pueda ver las palabras del futuro.

¿Por qué? Porque si le dejas ver el futuro, hace trampa: "¿A qué le va a prestar más atención si su objetivo es predecir la palabra que va a ocupar la posición 3 y vos le permitís mirar toda la secuencia? A la palabra 3. Te va a dar identidad."

¿Cómo se enmascara? Se usa una matriz triangular inferior. Todo lo que está arriba de la diagonal (el futuro) se pone a -infinito ANTES del softmax. El softmax convierte -infinito en 0 (atención nula).

Es la misma idea que la matriz triangular del modelo autorregresivo de Hinton: no mirar el futuro. La diferencia es que acá se implementa con una máscara explícita porque el Transformer ve toda la secuencia de golpe.

7. Cross-Attention (Encoder-Decoder Attention)

Es la atención que CONECTA el Encoder con el Decoder. Es la segunda capa de atención del Decoder (la que no es la masked self-attention).

La diferencia clave: las Queries vienen del Decoder, pero los Keys y Values vienen del Encoder.

"Las queries son las palabras del decoder. Los keys y los values vienen del encoder. Lo que va a hacer es que para cada palabra del decoder me va a decir ¿a qué palabra del encoder le tiene que prestar más atención?"

Es exactamente igual que en los modelos Seq2Seq con RNN, pero sin recurrencia. Cada palabra del Decoder "pregunta": ¿a cuáles palabras de la entrada original le debo prestar atención?

La fórmula es la misma, pero ahora Q tiene longitud M (frase del decoder) y K, V tienen longitud N (frase del encoder). El resultado es M × N en la matriz de atención.

8. Positional Encoding

El Self-Attention es invariante bajo permutación: si cambiás el orden de las palabras, da los mismos valores. "Si yo entrevero las palabras, la matriz se entrevera, pero me da los mismos valores."

Sin Positional Encoding, el modelo no sabría el orden de las palabras. Se le suman vectores de posición (funciones seno y coseno) al embedding para indicar "esta es la posición 1, esta es la posición 2, etc."

- Tiene la misma dimensión que el embedding (d_model) para poder sumarse
- NO tiene parámetros entrenables (en la versión original del paper)
- Se suma al embedding, no se concatena

9. Input Embedding

¿Qué problema resuelve? La tokenización convierte palabras en números (IDs), por ejemplo "gato" = 234. Pero un número suelto no le dice nada útil a la red. El número 234 no significa que "gato" se parezca a "perro" (235) ni que sea diferente de "avión" (236). Son solo números arbitrarios, como códigos de barras.

El embedding convierte cada número/ID en una LISTA de números (un vector). Por ejemplo, "gato" ya no es solo el número 234, sino que pasa a ser algo como [0.2, -0.5, 0.8, 0.1, ...] con d_model números (ej: 128 números).

¿Por qué una lista de números y no un solo número? Porque con una lista se pueden representar RELACIONES. Si "gato" = [0.2, -0.5, 0.8, ...] y "perro" = [0.3, -0.4, 0.7, ...], los dos vectores son parecidos (porque los dos son animales). Si "avión" = [-0.9, 0.6, -0.3, ...], es muy diferente. Palabras con significados parecidos quedan CERCA en este espacio de vectores. Palabras con significados distintos quedan LEJOS.

¿Cómo se obtienen estos vectores? No se inventan a mano. Existe una TABLA gigante (una matriz) de tamaño vocabulario × d_model. Si el vocabulario tiene 5000 palabras y d_model es 128, la tabla tiene 5000 filas × 128 columnas. Cada fila corresponde a una palabra. Para buscar el vector de "gato" (ID=234), simplemente se va a la fila 234 de la tabla.

Esta tabla se APRENDE durante el entrenamiento. Al principio los vectores son aleatorios (no significan nada). A medida que el modelo entrena, los ajusta hasta que palabras similares quedan con vectores similares.

Para el Encoder: una tabla con el vocabulario de la entrada (ej: 5000 tokens × 128)
Para el Decoder: otra tabla con el vocabulario de la salida (ej: 6000 tokens × 128)
Son tablas separadas si los vocabularios son distintos.

10. Skip Connection (Residual Connection)

Después de cada sub-capa (Attention o Feed-Forward), se SUMA la entrada original con la salida. Esto permite que el gradiente fluya directamente a capas anteriores sin pasar por todas las transformaciones. "Si una capa no aporta nada útil, puede aprender la identidad y no empeorar el resultado."

Para que funcione, la salida debe tener la misma dimensión que la entrada. Por eso todo está diseñado para mantener dimensión d_model.

11. Layer Normalization

Se aplica después de cada Skip Connection. Normaliza cada vector (cada palabra/fila) por separado:

- Resta la media de esa fila
- Divide por la desviación estándar de esa fila
- Multiplica por gamma (γ) y suma beta (β), que son parámetros entrenables

Gamma y beta tienen dimensión d_model. Un Layer Norm agrega 2 × d_model parámetros.

"El layer normalization lo que hace es normalizar fila a fila. Le resta la media de la fila, divide entre el desvío estándar de la fila, multiplica por gamma y suma beta."

12. Feed-Forward Network

Es un MLP de dos capas que se aplica a cada palabra POR SEPARADO (no es global):

- Primera capa: d_model → d_ff (ej: 128 → 512)
- Activación (ReLU o GELU)
- Segunda capa: d_ff → d_model (ej: 512 → 128)

"Es la misma Feed Forward que se aplica a cada palabra. No es una Feed Forward global. El hecho de que las filas sean las palabras de la frase es lo que hace que esto pueda consumir una frase de cualquier longitud."

📌 El Encoder completo (paso a paso)

Cada bloque del Encoder tiene:
1. Multi-Head Self-Attention (Q=K=V=entrada, todos contra todos)
2. Skip Connection + Layer Norm
3. Feed-Forward Network (palabra por palabra)
4. Skip Connection + Layer Norm

Flujo: Frase → Embedding + Positional Encoding → [Bloque × N veces] → Representación final

📌 El Decoder completo (paso a paso)

Cada bloque del Decoder tiene:
1. Masked Multi-Head Self-Attention (Q=K=V=entrada del decoder, con máscara triangular)
2. Skip Connection + Layer Norm
3. Cross-Attention (Q=decoder, K=V=salida del encoder)
4. Skip Connection + Layer Norm
5. Feed-Forward Network (palabra por palabra)
6. Skip Connection + Layer Norm

Al final del Decoder hay una capa Linear + Softmax que produce probabilidades sobre el vocabulario de salida.

📌 Tokens especiales

Begin of Sequence (BOS): obligatorio para el decoder. "Sin el start of sequence no podés arrancar. Es como que no tuvieras ruedas en el auto." El encoder NO lo necesita.

End of Sequence (EOS): marca el final de la salida esperada. En entrenamiento se agrega al final del target. En inferencia, cuando el modelo predice EOS, se para.

📌 Entrenamiento vs Inferencia

a) Entrenamiento (todo en paralelo)

- El Encoder recibe la frase completa de entrada (ej: español)
- El Decoder recibe la frase completa de salida con BOS al inicio (ej: inglés)
- Se procesan TODAS las posiciones a la vez
- Se comparan las predicciones con las palabras reales (shifted)
- La máscara hace que no vea el futuro aunque toda la frase esté presente

"En entrenamiento te sale la probabilidad de todas las palabras. Porque vos tenés la longitud."

b) Inferencia (loop obligatorio)

1. El Encoder procesa toda la frase de entrada de una vez
2. Al Decoder le pasamos solo <BOS>
3. Predice la primera palabra
4. Esa palabra se agrega como input
5. Predice la segunda
6. Y así hasta que predice <EOS>

"En inferencia tenemos un loop. Mando una palabra, mando otra, pero es un for. Ahí no hay nada en paralelo, ahí es secuencial."

📌 Cálculo de parámetros (ejemplo del parcial)

Con d_model=128, H=4, d_ff=512, vocab_source=5000, vocab_target=6000, N=2:

Multi-Head Attention (una capa):
- Por cabeza: W_Q (128×32) + W_K (128×32) + W_V (128×32) + biases (32×3) = 12,384
- 4 cabezas: 12,384 × 4 = 49,536
- W_O (128×128) + bias (128) = 16,512
- Total MHA: 66,048 parámetros

Layer Normalization:
- gamma (128) + beta (128) = 256 parámetros

Feed-Forward:
- Capa 1: (128+1) × 512 = 66,048
- Capa 2: (512+1) × 128 = 65,664
- Total FF: 131,712 parámetros

Un bloque Encoder: 66,048 + 256×2 + 131,712 = 198,272
Un bloque Decoder: 66,048×2 + 256×3 + 131,712 = 264,576

Embeddings: 5000×128 + 6000×128 = 1,408,000
Capa lineal final: (128+1) × 6000 = 774,000

Total: ~3,107,688 parámetros (~3 millones)

"Y eso con un vocabulario de 5000 tokens es minúsculo. Esto es minúsculo."

📌 Transformer vs RNN

Ventajas del Transformer:
- Paralelización en entrenamiento: "el transformer vos hacés todo de una. Aprovechas mucho la eficiencia computacional."
- Mejor manejo de secuencias largas: "el attention considera toda la secuencia. A largo plazo no hay comparación con las RNN."
- Self-Attention vs Attention simple: "en las RNN mirábamos solo la parte que correspondía. En transformer hay self-attention."

Similitud: "Si uno mira el encoder y el decoder como cajas negras es lo mismo. Solo que la caja negra de la RNN procesa el input paso a paso secuencialmente. Esto lo procesa todo de un saque."

📌 ¿Dónde aparece el Transformer en el curso?

a) Modelos de Lenguaje: GPT usa solo el Decoder del Transformer (sin Encoder ni Cross-Attention). Es puramente autorregresivo: predice la siguiente palabra dado las anteriores. Usa Causal Masking para no ver el futuro.

b) Difusión (Latent Diffusion / Stable Diffusion): usa Cross-Attention para condicionar la generación con texto. El texto pasa por un Transformer (CLIP) que produce vectores, y esos vectores entran como Keys y Values en la U-Net.

c) Traducción automática: el caso original del paper "Attention is All You Need". Usa Encoder + Decoder completo.

d) El modelo autorregresivo de Hinton: la misma idea conceptual (no ver el futuro, generar secuencialmente) pero implementada de forma distinta. El Transformer usa la misma matriz triangular inferior que Hinton, pero como máscara de atención.

Diagramas

ENCODER (un bloque):

  ┌──────────────────┐
  │   Frase entrada   │
  └────────┬─────────┘
           │
           v
  ┌──────────────────┐
  │    EMBEDDING      │    vocabulario × d_model
  │  + Pos. Encoding  │    (se suman)
  └────────┬─────────┘
           │
           v
  ┌──────────────────────────────────────────────────┐
  │                BLOQUE ENCODER (×N)                │
  │                                                    │
  │   ┌───────────────────────────────────────┐       │
  │   │      MULTI-HEAD SELF-ATTENTION        │       │
  │   │    Q = K = V = entrada (todos=todos)   │       │
  │   │                                        │       │
  │   │  Para cada cabeza h:                   │       │
  │   │    Q_h = Z × W_Q_h                    │       │
  │   │    K_h = Z × W_K_h                    │       │
  │   │    V_h = Z × W_V_h                    │       │
  │   │    head_h = softmax(Q_h K_h^T/√d_k)V_h│       │
  │   │                                        │       │
  │   │  Concat(heads) × W_O → salida          │       │
  │   └────────────────┬──────────────────────┘       │
  │                    │                               │
  │                    v                               │
  │            ┌──────────────┐                       │
  │   Z ──────>│  + (SKIP)    │                       │
  │            │  Layer Norm  │                       │
  │            └──────┬───────┘                       │
  │                   │                                │
  │                   v                                │
  │   ┌───────────────────────────────────┐           │
  │   │       FEED-FORWARD NETWORK        │           │
  │   │  (palabra por palabra, no global)  │           │
  │   │                                    │           │
  │   │  d_model → d_ff → d_model          │           │
  │   │   (128)   (512)   (128)            │           │
  │   └────────────────┬──────────────────┘           │
  │                    │                               │
  │                    v                               │
  │            ┌──────────────┐                       │
  │   Z ──────>│  + (SKIP)    │                       │
  │            │  Layer Norm  │                       │
  │            └──────┬───────┘                       │
  │                   │                                │
  └───────────────────┼────────────────────────────────┘
                      │
                      v
          ┌──────────────────┐
          │  Representación   │    N × d_model
          │  del Encoder      │    (una fila por palabra)
          └──────────────────┘


DECODER (un bloque):

  ┌──────────────────┐
  │  Frase de salida   │    (con <BOS> al inicio)
  └────────┬─────────┘
           │
           v
  ┌──────────────────┐
  │    EMBEDDING      │    vocabulario_target × d_model
  │  + Pos. Encoding  │
  └────────┬─────────┘
           │
           v
  ┌────────────────────────────────────────────────────────────────┐
  │                   BLOQUE DECODER (×N)                          │
  │                                                                │
  │   ┌───────────────────────────────────────┐                   │
  │   │   MASKED MULTI-HEAD SELF-ATTENTION    │                   │
  │   │   Q = K = V = entrada del decoder      │                   │
  │   │                                        │                   │
  │   │   Igual que Self-Attention, PERO:      │                   │
  │   │   se pone -∞ arriba de la diagonal     │                   │
  │   │   (softmax lo convierte en 0)          │                   │
  │   │   → cada palabra solo ve las anteriores │                   │
  │   └────────────────┬──────────────────────┘                   │
  │                    │                                           │
  │                    v                                           │
  │            ┌──────────────┐                                   │
  │   Z ──────>│  + (SKIP)    │                                   │
  │            │  Layer Norm  │                                   │
  │            └──────┬───────┘                                   │
  │                   │                                            │
  │                   v                                            │
  │   ┌───────────────────────────────────────┐                   │
  │   │        CROSS-ATTENTION                │                   │
  │   │                                        │                   │
  │   │   Q = salida del paso anterior         │  ← del Decoder   │
  │   │   K = salida del Encoder               │  ← del Encoder   │
  │   │   V = salida del Encoder               │  ← del Encoder   │
  │   │                                        │                   │
  │   │   "¿a qué palabra de la entrada        │                   │
  │   │    le presto atención?"                │                   │
  │   └────────────────┬──────────────────────┘                   │
  │                    │                                           │
  │                    v                                           │
  │            ┌──────────────┐                                   │
  │   Z ──────>│  + (SKIP)    │                                   │
  │            │  Layer Norm  │                                   │
  │            └──────┬───────┘                                   │
  │                   │                                            │
  │                   v                                            │
  │   ┌───────────────────────────────────┐                       │
  │   │       FEED-FORWARD NETWORK        │                       │
  │   │  d_model → d_ff → d_model          │                       │
  │   └────────────────┬──────────────────┘                       │
  │                    │                                           │
  │                    v                                           │
  │            ┌──────────────┐                                   │
  │   Z ──────>│  + (SKIP)    │                                   │
  │            │  Layer Norm  │                                   │
  │            └──────┬───────┘                                   │
  │                   │                                            │
  └────────────────────┼────────────────────────────────────────────┘
                      │
                      v
            ┌──────────────────┐
            │   CAPA LINEAR     │    d_model → vocabulario_target
            │   + SOFTMAX       │    → probabilidades
            └──────────────────┘


SELF-ATTENTION (el cálculo interno, una sola cabeza):

  ┌───────────┐
  │  Entrada Z │   N × d_model
  └─────┬─────┘
        │
        ├──────────────────┬──────────────────┐
        │                  │                  │
        v                  v                  v
  ┌───────────┐      ┌───────────┐      ┌───────────┐
  │  × W_Q    │      │  × W_K    │      │  × W_V    │
  │           │      │           │      │           │
  │  → Q      │      │  → K      │      │  → V      │
  │ (N × d_k) │      │ (N × d_k) │      │ (N × d_v) │
  └─────┬─────┘      └─────┬─────┘      └─────┬─────┘
        │                  │                    │
        v                  v                    │
  ┌──────────────────────────┐                 │
  │    Q × K^T               │                 │
  │    ─────────             │                 │
  │      √d_k                │                 │
  │                          │                 │
  │    → Scores (N × N)      │                 │
  └────────────┬─────────────┘                 │
               │                                │
               v                                │
  ┌──────────────────────┐                     │
  │ MÁSCARA (solo Decoder)│                     │
  │ -∞ arriba diagonal   │                     │
  └────────────┬─────────┘                     │
               │                                │
               v                                │
  ┌──────────────────────┐                     │
  │  Softmax (fila×fila) │                     │
  │  → Pesos de atención │                     │
  │    (N × N, suman 1)  │                     │
  └────────────┬─────────┘                     │
               │                                │
               v                                v
  ┌──────────────────────────────────────────────┐
  │          Pesos × V                            │
  │                                               │
  │  → Salida: combinación ponderada de Values    │
  │    (N × d_v)                                  │
  └───────────────────────────────────────────────┘


CAUSAL MASKING (ejemplo con 4 palabras):

  Matriz de atención ANTES de la máscara (todos contra todos):

       w₁    w₂    w₃    w₄
  w₁ [ 0.5   0.3   0.1   0.1 ]
  w₂ [ 0.2   0.6   0.1   0.1 ]
  w₃ [ 0.1   0.3   0.5   0.1 ]
  w₄ [ 0.1   0.2   0.3   0.4 ]

  Máscara (triangular inferior, -∞ arriba de la diagonal):

       w₁    w₂    w₃    w₄
  w₁ [ 0.5   -∞    -∞    -∞  ]    ← w₁ solo se ve a sí misma
  w₂ [ 0.2   0.6   -∞    -∞  ]    ← w₂ ve w₁ y w₂
  w₃ [ 0.1   0.3   0.5   -∞  ]    ← w₃ ve w₁, w₂, w₃
  w₄ [ 0.1   0.2   0.3   0.4 ]    ← w₄ ve todas (es la última)

  Después de Softmax (-∞ se convierte en 0):

       w₁    w₂    w₃    w₄
  w₁ [ 1.0   0.0   0.0   0.0 ]
  w₂ [ 0.3   0.7   0.0   0.0 ]
  w₃ [ 0.1   0.4   0.5   0.0 ]
  w₄ [ 0.1   0.2   0.3   0.4 ]


ENTRENAMIENTO (todo en paralelo):

  ┌────────────────┐                        ┌───────────────────────┐
  │ Frase español   │                        │ <BOS> + frase inglés   │
  │ "el gato come"  │                        │ "<BOS> the cat eats"   │
  └───────┬────────┘                        └──────────┬────────────┘
          │                                             │
          v                                             v
  ┌──────────────────┐                      ┌──────────────────┐
  │    EMBEDDING      │                      │    EMBEDDING      │
  │  + Pos. Encoding  │                      │  + Pos. Encoding  │
  └───────┬──────────┘                      └──────────┬───────┘
          │                                             │
          v                                             v
  ┌──────────────────┐    salida Encoder    ┌──────────────────────┐
  │                  │ ──────────────────>  │                      │
  │    ENCODER       │    (K y V para       │      DECODER         │
  │    (×N bloques)  │     Cross-Attention)  │      (×N bloques)    │
  │                  │                      │                      │
  └──────────────────┘                      └──────────┬───────────┘
                                                       │
                                                       v
                                            ┌──────────────────┐
                                            │ LINEAR + SOFTMAX  │
                                            │ → probabilidades  │
                                            │   por posición    │
                                            └────────┬─────────┘
                                                     │
                                                     v
                                            ┌────────────────────────┐
                                            │ Comparar con target:    │
                                            │ "the cat eats <EOS>"    │
                                            │                        │
                                            │ Loss = Cross-Entropy   │
                                            │ (por cada posición)    │
                                            └────────────────────────┘


INFERENCIA (loop secuencial en el Decoder):

  ┌────────────────┐
  │ Frase español   │     SE PROCESA UNA SOLA VEZ
  │ "el gato come"  │
  └───────┬────────┘
          │
          v
  ┌──────────────────┐
  │    ENCODER       │──────────────────────────────────────┐
  │    (procesa todo │                                      │
  │     de una vez)  │                                      │
  └──────────────────┘                                      │
                                                            │
                          ┌────────────────────────────┐    │
                          │                            │    │
                          v                            │    │
                ┌──────────────────┐                   │    │
                │  tokens actuales  │                   │    │
                │  del Decoder      │                   │    │
                │                  │                   │    │
                │  Paso 1: [<BOS>] │                   │    │
                │  Paso 2: [<BOS>, │                   │    │
                │           "the"] │                   │    │
                │  Paso 3: ...     │                   │    │
                └────────┬─────────┘                   │    │
                         │                             │    │
                         v                             │    │
                ┌──────────────────┐ K,V del Encoder   │    │
                │    DECODER       │<──────────────────┘────┘
                └────────┬─────────┘
                         │
                         v
                ┌──────────────────┐
                │ LINEAR + SOFTMAX  │
                │ → probabilidad    │
                │   siguiente       │
                │   palabra         │
                └────────┬─────────┘
                         │
                         v
                ┌──────────────────┐
                │ Elegir palabra    │
                └────────┬─────────┘
                         │
               ┌─────────┴──────────┐
               │ ¿Es <EOS>?         │
               └──┬──────────────┬──┘
                  │              │
               Sí v           No v
            ┌────────┐   agregar palabra
            │ PARAR  │   al Decoder ──────────────────┘
            └────────┘


MULTI-HEAD ATTENTION (cómo se combinan las cabezas):

  ┌───────────┐
  │  Entrada Z │
  └──┬──┬──┬──┘
     │  │  │
     │  │  └──────────────────────────────────────────┐
     │  └──────────────────────┐                      │
     │                         │                      │
     v                         v                      v
  ┌──────────┐           ┌──────────┐           ┌──────────┐
  │ Cabeza 1 │           │ Cabeza 2 │           │ Cabeza H │
  │          │           │          │           │          │
  │ W_Q₁     │           │ W_Q₂     │           │ W_Q_H    │
  │ W_K₁     │           │ W_K₂     │           │ W_K_H    │
  │ W_V₁     │           │ W_V₂     │           │ W_V_H    │
  │          │           │          │           │          │
  │ N × d_v  │           │ N × d_v  │           │ N × d_v  │
  └────┬─────┘           └────┬─────┘           └────┬─────┘
       │                      │                      │
       └──────────┬───────────┴──────────┬───────────┘
                  │                      │
                  v                      │
       ┌──────────────────────┐         │
       │   CONCATENAR         │<────────┘
       │   N × (H × d_v)     │
       └──────────┬───────────┘
                  │
                  v
       ┌──────────────────────┐
       │     × W_O            │    (H × d_v) × d_model
       │                      │
       │  → N × d_model       │    (vuelve a la dimensión original)
       └──────────────────────┘


Resumen final

Transformer = Encoder + Decoder. Reemplaza la recurrencia por Self-Attention.
Self-Attention = softmax(Q × K^T / √d_k) × V. Todos contra todos.
Multi-Head = hacer attention varias veces con matrices distintas, concatenar, multiplicar por W_O.
Causal Masking = -∞ arriba de la diagonal → softmax → 0. No ver el futuro.
Cross-Attention = Q del Decoder, K y V del Encoder. Conecta las dos partes.
Positional Encoding = se suma al embedding para indicar orden (sin esto, el modelo no sabe posiciones).
Skip Connection = sumar entrada + salida. Permite flujo de gradientes.
Layer Norm = normalizar fila a fila. Parámetros: gamma y beta (2 × d_model).
Feed-Forward = MLP de 2 capas, palabra por palabra, d_model → d_ff → d_model.
Entrenamiento = todo en paralelo. Inferencia = loop secuencial.
Tokens especiales: BOS (obligatorio para arrancar el Decoder), EOS (para saber cuándo parar).
