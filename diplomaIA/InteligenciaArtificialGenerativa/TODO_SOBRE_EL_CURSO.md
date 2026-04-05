# Inteligencia Artificial Generativa - Todo Sobre el Curso

**Universidad ORT Uruguay | Agosto - Noviembre 2025**
**Profesor**: Francisco (Franz) | **Ayudante**: Juan Pedro Silva

---

## ¿De qué trata este curso?

En otras materias aprendiste a **clasificar** (dado un dato, decir qué es). Acá se da vuelta el problema: **¿cómo hacer que una máquina cree datos nuevos que parezcan reales?** Imágenes, texto, audio... cosas que nunca existieron.

La diferencia clave:

| Modelo Discriminativo | Modelo Generativo |
|---|---|
| Misma entrada → Misma salida | Misma entrada → Salidas diferentes cada vez |
| "¿Es un gato?" → Sí/No | "Generá una imagen" → Una imagen distinta cada vez |

Que las salidas varíen **no es un error**, es exactamente lo que queremos. El profesor lo demostró pidiéndole a ChatGPT un blues dos veces y obteniendo dos composiciones diferentes.

---

## Parte I: Fundamentos Matemáticos (Clases 1-3)

### Probabilidad: el idioma de la generación

¿Por qué empezamos con probabilidad? Porque generar datos nuevos es fundamentalmente un acto de **muestrear** (elegir al azar) de una distribución. Si querés generar caras de personas realistas, necesitás saber cómo se "distribuyen" las caras reales: qué colores de piel son más comunes, qué proporciones faciales son típicas, etc. Si aprendés esa distribución, podés elegir puntos al azar de ella y cada punto será una cara nueva que se ve realista.

Una distribución es simplemente una descripción de qué tan probable es cada posible resultado. Por ejemplo: "hay 60% de chance de que llueva y 40% de que no" es una distribución sobre el clima. "Generar" un clima es elegir al azar según esas probabilidades — y la mayoría de las veces te va a tocar "llueve", que es lo más probable.

Todo el curso se reduce a esto: **aprender la distribución de los datos reales para después poder muestrear de ella**. Los distintos modelos (autorregresivo, VAE, GAN, difusión) son simplemente distintas estrategias para aprender esa distribución.

**Regla del producto**: si querés saber la probabilidad de que pasen dos cosas juntas, podés descomponerlo en pasos. Ejemplo: ¿cuál es la probabilidad de que llueva Y de que lleves paraguas? Es la probabilidad de que llueva, multiplicada por la probabilidad de que lleves paraguas **dado que** llueve.

```
P(lluvia, paraguas) = P(lluvia) × P(paraguas | lluvia)
```

El símbolo "|" se lee "dado que". Esto parece trivial, pero es **la base de los modelos autorregresivos** que vienen después.

**Regla de la suma (marginalización)**: si te interesa la probabilidad de una sola cosa pero tenés información sobre dos, podés "sumar sobre" la que no te importa. Ejemplo: ¿cuál es la probabilidad de llevar paraguas (sin importar si llueve o no)?

```
P(paraguas) = P(paraguas, llueve) + P(paraguas, no llueve)
```

**Independencia**: dos cosas son independientes si saber una no cambia la probabilidad de la otra. Ejemplo: tirar un dado no afecta tirar una moneda. Cuando son independientes, la probabilidad conjunta es simplemente multiplicar:

```
P(dado=6, moneda=cara) = P(dado=6) × P(moneda=cara)
```

### Variables continuas y distribuciones

El mundo real tiene datos continuos (pesos, alturas, intensidades de píxeles). Las distribuciones principales del curso:

- **Uniforme U(a,b)**: todos los valores entre a y b son igualmente probables. Si graficás su forma, es un rectángulo plano. Ejemplo: un número aleatorio entre 0 y 1 donde todos son igual de probables.

- **Normal (Gaussiana) N(μ, σ²)**: la famosa curva con forma de campana. μ (mu) es el centro de la campana (el valor más probable), y σ (sigma) indica qué tan "ancha" o "dispersa" es. Una σ chica = campana angosta y puntiaguda. Una σ grande = campana ancha y baja. Aproximadamente el 68% de los datos caen entre μ-σ y μ+σ. **Es la distribución más importante del curso** — aparece en VAEs, difusión, GANs, y más.

- **Laplaciana**: parecida a la normal pero con un pico más agudo (como una tienda de campaña en vez de una campana redonda).

### Mixturas de Gaussianas

A veces los datos tienen "grupos" y una sola campana no los describe bien. Ejemplo del profesor: si graficás el peso de todos los gatos (machos y hembras juntos), no ves una sola campana. Ves dos campanas superpuestas, una centrada en el peso promedio de los machos y otra en el de las hembras.

```
P(Peso) = P(Macho) × P(Peso|Macho) + P(Hembra) × P(Peso|Hembra)
```

En español: la probabilidad de un peso dado es una mezcla de dos campanas, cada una pesada por la proporción de machos y hembras. Esto se generaliza a cualquier cantidad de grupos: si hay 3 tipos de flores, hay 3 campanas mezcladas. A cada campana se le llama un "componente" de la mixtura.

### Redes Bayesianas

¿Cómo sabemos qué variables dependen de cuáles? Las redes Bayesianas son diagramas (grafos con flechas) que lo hacen explícito. Ejemplo: "Nube → Lluvia → Piso mojado". La flecha dice "influye en". La utilidad es que **simplifican los cálculos enormemente**: si sabés que llovió, no necesitás saber si había nubes para predecir si el piso está mojado. Eso reduce la cantidad de cosas que el modelo tiene que aprender.

La **cadena de Markov** es un caso particular: cada variable solo depende de la inmediatamente anterior, no de toda la historia. Ejemplo: para predecir el clima de mañana, solo importa el clima de hoy, no el de la semana pasada. Esta simplificación aparece después en los modelos autorregresivos, donde hay que decidir "de cuántos píxeles anteriores depende el siguiente".

### Insight del perceptrón (cambio de perspectiva clave)

Cuando un perceptrón (una neurona de una red neuronal) da salida 0.7, normalmente uno piensa "la respuesta es 0.7". Pero en este curso se ve distinto: esa salida **es la probabilidad de que el resultado sea 1**. O sea, está diciendo "hay un 70% de chance de que sea 1 y un 30% de que sea 0".

Este cambio de perspectiva es crucial: las redes neuronales que usabas para clasificar en realidad están estimando probabilidades, y eso es exactamente lo que necesitamos para generar datos nuevos.

---

## Parte II: Modelos Autorregresivos (Clases 3-5)

### La idea central

Ya sabemos que generar = muestrear de la distribución real. Pero ¿cómo aprendemos la distribución de algo tan complejo como una imagen de 784 píxeles? No podemos aprender P(imagen completa) directamente — es un espacio gigantesco. La solución autorregresiva es: **descomponerlo en pasos chiquitos**.

Un modelo autorregresivo genera datos **de a poquito, en orden**, donde cada nuevo dato depende de los anteriores. Es como escribir una historia palabra por palabra: elegís la primera palabra, después elegís la segunda basándote en la primera, la tercera basándote en las dos anteriores, etc. En vez de aprender la distribución de imágenes enteras (imposible), aprendemos la distribución de cada píxel individual dado los anteriores (mucho más manejable).

Para una imagen en blanco y negro de 28×28 = 784 píxeles (como las del dataset MNIST de dígitos escritos a mano), se descompone así (usando la regla del producto de la Parte I):

```
P(todos los píxeles) = P(píxel₁) × P(píxel₂|píxel₁) × P(píxel₃|píxel₁,píxel₂) × ...
```

En español: la probabilidad de la imagen completa es el producto de las probabilidades de cada píxel, donde cada uno depende de todos los que vinieron antes.

### El problema: explosión de parámetros

Si cada píxel puede ser solo 0 (negro) o 1 (blanco), para decidir el valor del píxel N necesitamos saber las probabilidades para **todas las combinaciones posibles** de los N-1 píxeles anteriores. Para el segundo píxel son 2 combinaciones, para el tercero 4, para el cuarto 8... para el píxel 784 serían 2^783 combinaciones — un número más grande que la cantidad de átomos en el universo. Imposible de guardar en memoria.

### La solución: Redes de Hinton (Belief Networks)

Geoffrey Hinton (Premio Nobel de Física 2024) propuso una idea brillante: en vez de guardar una tabla gigante con todas las combinaciones, usar un perceptrón (una neurona) para cada píxel. Cada perceptrón recibe los píxeles anteriores como entrada y calcula la probabilidad de que el píxel actual sea 1.

```
P(píxelᵢ = 1 | píxeles anteriores) = sigmoide(suma pesada de los píxeles anteriores + bias)
```

La función **sigmoide** (σ) simplemente toma cualquier número y lo aplasta al rango entre 0 y 1, para que la salida sea una probabilidad válida. Si le metes un número muy grande da ~1, si le metes uno muy negativo da ~0.

Los perceptrones se organizan con una **matriz de pesos triangular inferior**: una tabla de pesos donde toda la mitad superior es ceros fijos (que NO se entrenan). Esos ceros garantizan que cada píxel solo mire los píxeles anteriores y no los posteriores. Esto reduce la cantidad de parámetros de un crecimiento exponencial (imposible) a un crecimiento **lineal** (totalmente manejable).

### Asimetría fundamental

- **Entrenamiento**: es paralelo — tenés todos los píxeles del dataset de antemano, así que podés calcular todas las probabilidades al mismo tiempo.
- **Generación**: es secuencial — necesitás generar el píxel 3 antes de poder generar el 4, porque el 4 depende de él.

Esta misma limitación aplica a GPT y ChatGPT: por eso van generando texto de a una palabra.

### Entrenamiento: cómo acercar distribuciones

El objetivo del entrenamiento es lograr que el modelo aprenda cómo se ven los datos reales. Tenemos dos distribuciones:
- **P_data**: cómo se distribuyen los datos reales (las imágenes del dataset)
- **P_θ**: lo que el modelo cree actualmente sobre cómo se distribuyen los datos (θ son los parámetros que se entrenan: pesos y biases)

Queremos que P_θ se parezca lo más posible a P_data.

**KL Divergence** es una herramienta que mide qué tan diferentes son dos distribuciones. Pensalo como una "distancia" entre distribuciones (aunque técnicamente no es una distancia porque no es simétrica — medir de A a B da distinto que de B a A). Si la KL da 0, las distribuciones son idénticas. Si da un número grande, son muy diferentes.

Minimizar la KL Divergence equivale a lo siguiente: queremos que el modelo le asigne **alta probabilidad** a los datos que sí existen en la realidad. Si el modelo dice "esta imagen de un 7 tiene probabilidad casi cero", está mal, porque en el dataset hay muchos 7's. En jerga técnica, minimizamos el **Negative Log-Likelihood (NLL)**: tomamos el promedio de -log(probabilidad que el modelo le asigna a cada dato real). Si la probabilidad es alta, -log da un número bajo (bien). Si la probabilidad es baja, -log da un número alto (mal, hay que seguir entrenando).

Como no tenemos infinitos datos, aproximamos este promedio usando los datos del dataset que sí tenemos.

### Binary Cross-Entropy (BCE): la función de pérdida para píxeles binarios

Cuando cada píxel solo puede ser 0 o 1, necesitamos una función que mida qué tan bien predice el modelo. El perceptrón nos da un solo número: la probabilidad de que el píxel sea 1. Llamemos a esa predicción **ŷ** (y-sombrero). Pero necesitamos evaluar si esa predicción es buena tanto cuando el píxel real es 1 como cuando es 0.

Ejemplo: si el modelo predice ŷ = 0.9 (90% de chance de ser blanco):
- Si el píxel real es 1 (blanco): buena predicción, error bajo.
- Si el píxel real es 0 (negro): pésima predicción, error alto.

La BCE combina los dos casos en una sola fórmula:

```
BCE = -[x × log(ŷ) + (1-x) × log(1-ŷ)]
```

Donde **x** es el valor real del píxel (0 o 1) y **ŷ** es lo que predice el modelo. Funciona así:
- Cuando x=1: solo queda -log(ŷ). Si ŷ es alto (cerca de 1), log(1) ≈ 0, el error es bajo. Si ŷ es bajo, -log(0.01) es enorme, el error es alto.
- Cuando x=0: solo queda -log(1-ŷ). Si ŷ es bajo (modelo dice "probablemente 0"), 1-ŷ es alto, error bajo. Si ŷ es alto (el modelo se equivocó), 1-ŷ es bajo, error alto.

El x y el (1-x) actúan como un interruptor que "apaga" el término que no corresponde según el valor real.

**¿Por qué usamos logaritmos?** Porque multiplicar muchas probabilidades chiquitas (como 0.001 × 0.003 × 0.002...) da números tan pequeños que la computadora los redondea a cero. En cambio, sumar los logaritmos de esas probabilidades da números manejables. Es un truco de estabilidad numérica.

---

## Parte III: Variational Autoencoders - VAE (Clase 6)

### ¿Por qué necesitamos otro enfoque?

El modelo autorregresivo funciona, pero tiene un problema fundamental: **genera de a un píxel, en orden, y no puede paralelizar la generación**. Para una imagen de 784 píxeles, son 784 pasos secuenciales. Para texto, cada palabra requiere un paso. Es lento.

¿Se puede generar todo de golpe, en un solo paso? Sí, pero para eso necesitamos otra estrategia. La idea del VAE es: si pudiéramos encontrar un "resumen" compacto de cada imagen (unos pocos números que capturen su esencia), y aprender a ir de "resumen" a "imagen", entonces generar sería simplemente: inventar un resumen aleatorio → pasarlo por la red → obtener una imagen completa en un solo paso.

### Variables latentes

Pero ¿qué sería ese "resumen"? El profesor usó el ejemplo de las flores Iris: si medís el largo y ancho de los pétalos de muchas flores, los datos forman grupos. Cada grupo corresponde a una variedad de flor (setosa, versicolor, virginica). Pero si no sabés qué variedad es cada flor, esa información está "escondida" — existe y afecta los datos, pero no la podés ver directamente. A eso se le llama **variable latente**: algo que influye en los datos pero no podemos observar.

En el caso de imágenes de caras, las variables latentes podrían ser cosas como "tiene barba", "está sonriendo", "es rubio". Nunca las vemos directamente, pero determinan cómo se ve la imagen. Si aprendemos ese espacio de variables latentes, podemos manipularlo para generar.

### De Autoencoder a VAE

¿Cómo descubrimos esas variables latentes? Con un **autoencoder**: una red que se obliga a sí misma a encontrar un resumen compacto. Funciona así:

1. **Encoder** (comprime): toma una imagen y la fuerza a pasar por un cuello de botella chiquito — la comprime en un vector de pocos números llamado **código latente** (Z). Es como pedirle a alguien que describa una foto usando solo 10 números.
2. **Decoder** (expande): toma esos pocos números y trata de reconstruir la imagen original.

Si el autoencoder logra reconstruir bien la imagen pasando por ese cuello de botella, significa que esos pocos números (Z) capturan la información esencial de la imagen. El encoder aprendió a "resumir" y el decoder aprendió a "expandir".

**Pero un autoencoder básico no sirve para generar.** ¿Por qué? Porque cada imagen se comprime a un punto fijo específico en el espacio latente. Si inventás un punto Z al azar y lo pasás por el decoder, probablemente caiga en una zona del espacio que el decoder nunca vio durante entrenamiento, y la salida sería basura. No hay garantía de que el espacio entre los puntos conocidos tenga sentido.

El **VAE** (Variational Autoencoder) resuelve esto cambiando algo fundamental: el encoder no da un punto fijo Z sino que da los **parámetros de una campana gaussiana** — un centro (μ, "mu") y un ancho (σ, "sigma"). Después, Z se obtiene muestreando (eligiendo al azar) un punto de esa campana.

```
Encoder: Imagen → centro de la campana (μ) y ancho de la campana (σ)
         z = un punto aleatorio muestreado de esa campana
Decoder: z → Imagen reconstruida
```

¿Por qué esto sí sirve para generar? Porque al muestrear de una zona (la campana) en vez de un punto fijo, el decoder se ve obligado a aprender a reconstruir bien desde **toda una región** del espacio latente, no solo desde un punto exacto. Esto hace que el espacio latente sea "suave" y continuo — no hay huecos donde el decoder no sabe qué hacer. Y si además forzamos que esas campanas se parezcan a una campana estándar conocida (como se explica en el loss más abajo), entonces para generar simplemente muestreamos de esa campana estándar y el decoder sabe qué hacer con cualquier punto.

### El Reparametrization Trick

Hay un problema técnico: para entrenar una red neuronal, usamos backpropagation, que necesita calcular derivadas de cada operación paso a paso. Pero el paso de "elegir un punto al azar de una campana" es aleatorio, y no se puede derivar a través de algo aleatorio (¿cómo calculás "cuánto cambia el resultado si muevo un poquito los parámetros" cuando el resultado es aleatorio?).

La solución es un truco muy elegante: separar la aleatoriedad de los parámetros entrenables.

```
ANTES (no funciona para entrenar):
   z = punto aleatorio de una campana centrada en μ con ancho σ

DESPUÉS (funciona):
   ε = punto aleatorio de una campana estándar fija (centro 0, ancho 1)
   z = μ + σ × ε
```

Es matemáticamente lo mismo (produce puntos de la misma distribución), pero ahora:
- ε es aleatorio, pero NO depende de ningún parámetro entrenable
- z es una multiplicación y suma normales, donde μ y σ sí son entrenables
- Podemos calcular derivadas respecto a μ y σ sin problema

### Función de pérdida del VAE

El VAE tiene dos objetivos que se expresan como dos partes del loss (error):

```
Loss = Reconstrucción + KL Divergence
```

- **Reconstrucción**: mide qué tan parecida es la imagen reconstruida a la original. Se usa MSE (error cuadrático medio — la diferencia al cuadrado entre cada píxel original y el reconstruido) o BCE (la misma fórmula de antes para píxeles binarios). Queremos que este error sea **bajo**.

- **KL Divergence**: mide qué tan diferente es la campana que produce el encoder respecto a una campana estándar (centro 0, ancho 1). Queremos que este número sea **bajo**, es decir, que las campanas del encoder se parezcan a la campana estándar.

¿Por qué forzar que se parezca a la campana estándar? Porque a la hora de **generar imágenes nuevas**, tiramos a la basura el encoder, nos quedamos solo con el decoder, y muestreamos puntos de la campana estándar (centro 0, ancho 1) — que es fácil de muestrear. Si durante el entrenamiento forzamos al encoder a producir campanas parecidas a la estándar, entonces cuando muestreemos de la estándar, los puntos van a caer en regiones que el decoder conoce y va a generar imágenes que tengan sentido.

### β-VAE

Una variante que le pone un peso extra a la parte de KL:

```
Loss = Reconstrucción + β × KL
```

- β > 1: prioriza tener un espacio latente ordenado, pero las reconstrucciones salen más borrosas.
- β < 1: prioriza reconstruir bien, pero el espacio latente queda más desordenado (peor para generar).

### Generación con VAE

```python
z = torch.randn(batch_size, latent_dim)  # punto aleatorio de campana estándar
imagen_nueva = decoder(z)                 # el decoder genera una imagen en un solo paso
```

---

## Parte IV: GANs - Redes Adversariales (Clases 7-8)

### ¿Por qué otro modelo si ya tenemos VAE?

El VAE funciona y genera en un solo paso, pero tiene un problema visible: **las imágenes salen borrosas**. Esto pasa porque el loss de reconstrucción (MSE) calcula el promedio de los errores por píxel. Si el modelo no está seguro de si un píxel debe ser claro u oscuro, pone un gris intermedio — que minimiza el error promedio pero no se ve nítido. Las caras generadas se ven como fotos desenfocadas.

Las GANs atacan este problema con una idea completamente diferente: en vez de medir el error píxel a píxel, usan **otra red neuronal** para juzgar si la imagen generada "se ve real o no". Si se ve borrosa, la red juez la detecta como falsa. Esto fuerza al generador a producir imágenes con detalles nítidos.

### La idea: un juego entre dos redes

Ian Goodfellow (2014) propuso modelar la generación como una competencia:

- **Generador (G)**: un falsificador de billetes. Recibe ruido aleatorio z y produce imágenes falsas.
- **Discriminador (D)**: un policía. Recibe una imagen y dice si es real o falsa (da un número entre 0 y 1: 1 = "creo que es real", 0 = "creo que es falsa").

Ambos mejoran compitiendo. Al final, G produce imágenes tan buenas que D no puede distinguirlas.

### Función objetivo (Minimax)

```
min_G max_D V(D,G) = E[log D(x)] + E[log(1 - D(G(z)))]
```

Esta fórmula parece intimidante pero dice algo simple:

- **E[log D(x)]**: ¿qué tan bien detecta D las imágenes **reales**? Si D acierta (D(x) ≈ 1), log(1) ≈ 0 (valor alto). Si falla (D(x) ≈ 0), log(0) → -∞ (valor bajo).
- **E[log(1 - D(G(z)))]**: ¿qué tan bien detecta D las imágenes **falsas**? Si D las detecta como falsas (D(G(z)) ≈ 0), log(1-0) = 0 (valor alto para D). Si G logra engañarlo (D(G(z)) ≈ 1), log(1-1) → -∞ (valor bajo para D, que es lo que G quiere).

D quiere **maximizar** los dos términos (ser buen detective). G quiere **minimizar** el segundo (engañar al detective).

### Entrenamiento alternado

```
Para cada época:
    1. Congelar G, entrenar D con datos reales (label=1) y falsos (label=0)
    2. Congelar D, entrenar G para engañar a D
```

**Truco del "Label Flip"**: cuando entrenamos G, le decimos al sistema que las imágenes falsas son reales (label=1). No es que estemos mintiendo — es un truco matemático que produce gradientes más útiles al inicio del entrenamiento, cuando G todavía genera basura.

**Detalle técnico crucial**: al entrenar D, se usa `.detach()` en las imágenes generadas por G. Esto corta la conexión de gradientes hacia G, asegurando que solo D se actualice. Cuando entrenamos G, NO usamos `.detach()`, para que los gradientes sí fluyan hasta G y pueda aprender.

### DCGAN (Deep Convolutional GAN)

Una versión de GAN que usa capas convolucionales (las mismas que se usan en clasificación de imágenes) en vez de capas fully-connected:
- En G se usa **ConvTranspose2d** para ir agrandando una imagen chiquita hasta el tamaño final.
- En D se usa **Conv2d** para ir achicando la imagen hasta dar un solo número (real/falso).
- **BatchNorm** después de cada capa para estabilizar el entrenamiento.
- **LeakyReLU** en D (como ReLU pero deja pasar un poquito de señal cuando el valor es negativo), **ReLU** en G.

### Problemas conocidos

**Mode Collapse**: G aprende a generar solo unos pocos tipos de muestras (ej: solo 3's y 7's, ignora el resto). Nada en el modelo incentiva la variedad: si G encontró un tipo de imagen que engaña a D, no tiene razón para probar cosas nuevas.

**Inestabilidad**: es muy difícil mantener G y D equilibrados. Si D es mucho mejor que G (o viceversa), el entrenamiento colapsa. A veces es mejor reiniciar de cero que intentar recuperarse.

**Vanishing Gradients** (gradientes que desaparecen): si D es "demasiado bueno" al inicio, detecta todas las imágenes falsas con 100% de confianza. En ese caso, los gradientes que llegan a G son casi cero y G no puede aprender nada — queda estancado.

### Conditional GANs (cGANs)

Extensión donde le decís al generador **qué** querés que genere. Por ejemplo, en vez de "generá un dígito cualquiera", le decís "generá un 7". Se logra pasándole la información de la clase (como un vector one-hot) junto con el ruido z.

---

## Parte V: Modelos de Lenguaje (Clase 9)

### ¿Por qué vemos modelos de lenguaje en un curso de IA generativa?

Hasta ahora todos los modelos generaban imágenes. Pero la idea autorregresiva que vimos con Hinton (generar de a un pedacito, donde cada pedacito depende de los anteriores) **es exactamente la misma idea detrás de ChatGPT**. Solo que en vez de píxeles, se generan palabras. En vez de P(píxel₃ | píxel₁, píxel₂), es P(palabra₃ | palabra₁, palabra₂). La misma regla del producto, el mismo enfoque secuencial, la misma limitación de no poder paralelizar la generación.

### ¿Qué es un Language Model?

Es un modelo que recibe una secuencia de texto y predice cuál es la siguiente palabra (o más precisamente, el siguiente **token**). Le das "Hola, ¿cómo" y te dice las probabilidades de todas las posibles continuaciones: "estás" tiene 40%, "te" tiene 15%, "va" tiene 10%, etc.

Son literalmente **modelos autorregresivos aplicados a texto**: generan una palabra a la vez, donde cada palabra depende de las anteriores. Es el mismo concepto de la Parte II pero en otro dominio.

Observación clave del profesor: "El LM es **determinístico**: para la misma entrada, siempre da las mismas probabilidades. La **aleatoriedad** viene del muestreo — de la elección aleatoria de cuál palabra tomar de esas probabilidades."

### Tokenización

Las redes neuronales no entienden letras ni palabras — solo entienden números. La **tokenización** convierte texto en secuencias de números. Los tokens no son necesariamente palabras completas; pueden ser pedazos de palabras (sub-palabras). Por ejemplo, "desafortunadamente" podría ser 3 tokens: "des" + "afortuna" + "damente".

Algoritmos comunes: BPE (Byte-Pair Encoding), WordPiece, SentencePiece.

**Regla de oro del profesor**: "Un tokenizer va con un modelo. Una vez que está todo hecho, no se toca más el tokenizer."

### El proceso de generación paso a paso

```
1. Texto de entrada: "Hola, ¿cómo"
2. Tokenizar: convertir a números → [15432, 11, 8064]
3. Pasar por el modelo → el modelo devuelve un "score" (llamado logit) para
   cada posible palabra del vocabulario
4. Softmax → convierte esos scores en probabilidades que suman 1
   (softmax toma números cualesquiera y los transforma en probabilidades:
   los scores altos se vuelven probabilidades altas, los bajos se vuelven bajas)
5. Muestrear un token de esas probabilidades
6. Agregar ese token a la secuencia y repetir desde el paso 3
```

### Estrategias de muestreo

Una vez que el modelo da las probabilidades, hay distintas formas de elegir el siguiente token:

**Greedy**: siempre elegir el más probable. Simple pero aburrido — tiende a repetirse.

**Top-K**: en vez de considerar TODAS las palabras posibles, quedarse solo con las K más probables (ej: las 50 más probables) e ignorar el resto. Después elegir al azar entre esas K.

**Top-P (Nucleus)**: similar pero en vez de un número fijo K, se incluyen palabras hasta que la suma de sus probabilidades llegue a P (ej: 0.9 = 90%). Si una palabra tiene 80% de probabilidad, solo esa entra. Si la más probable tiene 20%, entran varias. Es más adaptativo que Top-K.

**Temperatura**: un número que controla qué tan "atrevido" es el muestreo.

```
probabilidades = softmax(scores / T)
```

Lo que hace: divide los scores por T antes de convertirlos a probabilidades.
- T baja (ej: 0.3): las diferencias entre probabilidades se amplían. La más probable domina aún más. Resultado: más predecible, menos creativo.
- T alta (ej: 1.5): las diferencias se achican. Todas las opciones se vuelven más parecidas en probabilidad. Resultado: más aleatorio, más creativo (pero puede generar incoherencias).
- T = 1: las probabilidades quedan tal cual las da el modelo.

### Transformers (la arquitectura detrás de GPT)

¿Por qué necesitamos una arquitectura especial? Porque un modelo de lenguaje necesita entender **contexto**: para predecir la siguiente palabra de "El presidente de Francia visitó Alemania y dijo que su país...", el modelo necesita recordar que "su país" se refiere a Francia, que está muchas palabras atrás. Las redes simples (como los perceptrones de Hinton) no manejan bien dependencias largas. Los Transformers resuelven esto con un mecanismo llamado atención.

**Self-Attention** (auto-atención): el mecanismo que permite que cada palabra "mire" a todas las demás para decidir cuáles son relevantes. Ejemplo: en "El gato se sentó en su alfombra porque estaba cansado", para entender "estaba", el modelo necesita prestar atención a "gato" (no a "alfombra") para saber quién estaba cansado.

Funciona así: cada token genera tres vectores:
- **Query (Q)**: "¿qué información estoy buscando?"
- **Key (K)**: "¿qué información tengo para ofrecer?"
- **Value (V)**: "¿cuál es mi información concreta?"

Se calcula un "puntaje de atención" entre cada par de tokens (multiplicando Q de uno por K de otro). Los puntajes altos significan "estos tokens son relevantes entre sí". Después se usa ese puntaje para crear una mezcla ponderada de los Values.

**Causal Masking**: ¿te acordás de la matriz triangular de Hinton, donde los ceros impedían que cada píxel viera los posteriores? Causal masking es **exactamente la misma idea** pero implementada de otra forma: en vez de ceros en una matriz de pesos, se ponen puntajes de -infinito en las posiciones futuras del mecanismo de atención. Después del softmax, esos -infinito se convierten en 0 (atención nula). Resultado: cada token solo puede ver los tokens anteriores, no el futuro (que al generar, todavía no existe).

**Multi-Head Attention**: en vez de tener un solo "ojo" de atención, se tienen varios (ej: 12) en paralelo. Cada uno puede enfocarse en un aspecto diferente: uno captura relaciones gramaticales, otro el tema, otro la posición, etc.

### Función de pérdida para LMs

**Cross-Entropy**: es esencialmente la misma idea que el Negative Log-Likelihood de la Parte II. Mide qué tan lejos está la predicción del modelo de la palabra correcta. Si el modelo le asigna alta probabilidad a la palabra que realmente viene después, el error es bajo. Si le asigna probabilidad baja, el error es alto.

```
L = -log(probabilidad que el modelo le asignó a la palabra correcta)
```

Es la misma fórmula que usamos para entrenar Hinton, pero aplicada a tokens de texto en vez de píxeles.

---

## Parte VI: Modelos de Difusión (Clase 10)

### ¿Por qué necesitamos otro enfoque más?

La GAN genera imágenes nítidas, pero es **muy difícil de entrenar**: el entrenamiento es inestable, sufre de mode collapse (genera poca variedad), y no hay una métrica clara de progreso — las losses oscilan sin indicar si el modelo está mejorando. A veces hay que reiniciar todo de cero.

Los modelos de difusión ofrecen lo mejor de ambos mundos: **la calidad de las GANs con la estabilidad de entrenamiento de los VAEs** (y de hecho con un loss más simple que ambos). El precio que pagan: la generación es lenta (1000 pasos en vez de 1).

### La idea central

Imaginá que agarrás una foto y le vas tirando estática (ruido) encima, un poquito a la vez, hasta que después de 1000 pasos la foto se convierte en pura estática. Ahora imaginá que entrenás una red neuronal para hacer lo contrario: dado un paso con estática, que prediga cómo se veía la imagen un paso antes (con un poquito menos de estática). Si lo lográs, podés arrancar de **pura estática** (que es fácil de generar) y aplicar la red 1000 veces para obtener una imagen limpia.

A diferencia de los VAEs, acá no hay compresión: la imagen ruidosa tiene **el mismo tamaño** que la imagen original en cada paso. Y a diferencia de las GANs, no hay un discriminador — solo una red que aprende a quitar ruido.

```
Forward:  Imagen limpia → (+ruido poco a poco, 1000 pasos) → Pura estática
Reverse:  Pura estática → (-ruido poco a poco, 1000 pasos) → Imagen limpia
```

### Forward Diffusion (agregar ruido)

En cada paso t, se mezcla la imagen con un poquito de ruido gaussiano. El parámetro β_t (beta) controla cuánto ruido se agrega en cada paso — típicamente empieza chiquito y va creciendo.

Hay un atajo matemático que permite saltar directamente al paso t que quieras sin calcular todos los pasos intermedios:

```
imagen_ruidosa_en_paso_t = (algo de la imagen original) + (algo de ruido puro)
```

Los "algos" son coeficientes que dependen de t. A medida que t crece, la imagen original pesa menos y el ruido pesa más, hasta que en t=1000 es prácticamente solo ruido.

### Reverse Diffusion (quitar ruido)

El modelo recibe dos cosas: la imagen ruidosa y el número de paso t (que le dice "cuánto ruido hay aproximadamente"). Con eso, predice **cuánto ruido hay** en la imagen. No predice la imagen limpia directamente, sino el ruido — es más estable numéricamente.

### Función de pérdida

Muy simple: la diferencia al cuadrado entre el ruido real (que nosotros pusimos) y el ruido que el modelo predice:

```
L = ||ruido_real - ruido_predicho||²
```

### Entrenamiento

```
Para cada imagen limpia:
    1. Elegir un paso t aleatorio entre 1 y 1000
    2. Generar ruido aleatorio
    3. Usar el atajo para crear la imagen en el paso t (mezcla de imagen + ruido)
    4. Pedirle al modelo que prediga el ruido
    5. Calcular el error entre el ruido real y el predicho
```

Una ventaja enorme: no hay que recorrer los 1000 pasos en orden. Se elige un t al azar y listo. Esto hace el entrenamiento muy eficiente.

### Generación

```
Arrancar con una imagen de puro ruido aleatorio
Para t = 1000 hasta 1:
    Predecir el ruido con el modelo
    Quitar un poquito de ese ruido de la imagen
Resultado: una imagen limpia generada desde cero
```

### Arquitectura: U-Net

La red que se usa tiene forma de U: primero achica la imagen (encoder), después la agranda (decoder), y tiene "puentes" (skip connections) que pasan información directamente del encoder al decoder. Además, recibe el paso t como entrada para saber cuánto ruido esperar.

### Latent Diffusion (Stable Diffusion)

La difusión funciona increíble, pero tiene un problema práctico: hacer 1000 pasos de quitar ruido sobre una imagen de 512×512 píxeles es extremadamente costoso en GPU y tiempo. Acá es donde los conceptos se conectan: ¿te acordás del VAE que comprimía imágenes a un espacio latente chiquito? Latent Diffusion **combina las dos ideas**: primero comprimir la imagen con un VAE a un tamaño mucho menor (ej: 64×64 — 64 veces más chico), hacer toda la difusión en ese espacio comprimido (mucho más rápido), y al final descomprimir con el decoder del VAE. Es literalmente VAE + Difusión trabajando juntos.

```
Imagen grande → [VAE comprime] → Imagen chica → [Difusión] → Imagen chica limpia → [VAE descomprime] → Imagen grande
```

### Conditional Diffusion (generar imágenes a partir de texto)

Para que el modelo genere lo que le pedís con texto (ej: "un gato astronauta"), se usa un modelo llamado **CLIP** que convierte el texto en una representación numérica. Esa representación se le pasa al modelo de difusión como guía.

**Classifier-Free Guidance**: una técnica donde el modelo genera con la guía del texto y sin ella, y después mezcla los resultados. Un parámetro **w** (típicamente 7.5) controla cuánto pesa el texto: más alto = la imagen sigue más fielmente el texto pero puede perder naturalidad.

---

## Parte VII: Evaluación de Modelos Generativos (Clase 11)

### ¿Por qué es un tema aparte?

Después de ver 5 modelos distintos (autorregresivo, VAE, GAN, LM, difusión), surge una pregunta natural: ¿cuál es mejor? ¿Cómo comparamos? En clasificación es fácil — tenés la respuesta correcta y calculás el porcentaje de aciertos. Pero en generación no hay "respuesta correcta": el modelo inventa algo que nunca existió. ¿Cómo evaluás algo que no tiene referencia?

### El problema fundamental

No hay una respuesta correcta contra la cual comparar una imagen generada. No podés decir "esta cara inventada está 73% bien". Necesitamos métricas especiales diseñadas para modelos generativos.

### Dos ejes de evaluación

1. **Fidelidad**: ¿qué tan realistas son las imágenes generadas? ¿Parecen fotos reales o se ven raras?
2. **Diversidad**: ¿genera variedad? ¿O siempre genera lo mismo?

Si el modelo genera un 1 perfecto pero SOLO genera 1's, tiene alta fidelidad pero baja diversidad. Ambas cosas importan.

### Métricas entre distribuciones

| Métrica | Qué mide en simple | Uso |
|---|---|---|
| KL Divergence | Qué tan diferentes son dos distribuciones (pero da resultados distintos si las comparás "de ida" vs "de vuelta") | VAEs, Difusión |
| Jensen-Shannon | Lo mismo que KL pero simétrica (da igual en ambas direcciones) | GANs |
| Wasserstein | Cuánto "esfuerzo" cuesta transformar una distribución en la otra (imaginá mover montañitas de arena) | WGANs |

### Métricas con modelos pre-entrenados

**Inception Score (IS)**: pasa las imágenes generadas por una red de clasificación pre-entrenada (Inception Net). Si la red clasifica cada imagen con alta confianza (dice "es un perro" sin dudas) Y las imágenes caen en muchas categorías distintas, el score es alto. Limitación: no compara con datos reales, solo evalúa las generadas.

**FID (Fréchet Inception Distance)**: pasa imágenes reales Y generadas por Inception Net, pero en vez de mirar la clasificación final, mira las "features" de la penúltima capa (una representación comprimida de lo que la red "entiende" de la imagen). Compara las estadísticas de esas features entre reales y generadas.

```
FID bajo = las distribuciones de features son parecidas = las imágenes generadas se parecen a las reales
```

Valores de referencia: <10 excelente, <20 muy bueno, <50 aceptable, >100 malo.

**CLIP Score**: para cuando generás imágenes a partir de texto. Mide qué tan bien la imagen generada corresponde al texto que le pediste.

### Métricas para texto

**Perplexity** (perplejidad): mide qué tan "sorprendido" se queda el modelo al ver texto real. Si el modelo predice bien las palabras que vienen, la perplejidad es baja (no le sorprende nada). Si predice mal, la perplejidad es alta. Baja = mejor.

**BLEU**: compara el texto generado con una referencia contando cuántas secuencias de palabras consecutivas (de largo 1, 2, 3, 4) coinciden. Enfocado en **precisión** (de lo que generó, ¿cuánto aparece en la referencia?). Usado en traducción.

**ROUGE**: similar a BLEU pero enfocado en **cobertura** (de lo que hay en la referencia, ¿cuánto capturó el modelo?). Usado en resúmenes.

**BERTScore**: usa una red neuronal (BERT) para comparar el significado en vez de las palabras exactas. Puede detectar que "contento" y "feliz" significan lo mismo aunque sean palabras diferentes.

### Evaluación humana

Se les muestra imágenes/textos a personas y se les pide que evalúen (A/B testing, escalas del 1 al 5, etc.). Es lo más confiable pero es caro, lento, y no escala.

### Recomendación del profesor

"Combiná múltiples métricas. Entendé qué mide cada una. Considerá el contexto."

---

## Comparación de todos los modelos

| Modelo | Tipo | Cómo genera | Fortaleza | Debilidad |
|---|---|---|---|---|
| Hinton | Autorregresivo | Píxel a píxel, secuencial | Simple, principio teórico claro | Lento generando |
| VAE | Encoder-Decoder | Muestreo en espacio latente | Latentes interpretables, rápido | Imágenes borrosas |
| GAN | Adversarial | Del generador en un paso | Imágenes nítidas | Inestable, mode collapse |
| Difusión | Denoising | Iterativo (1000 pasos) | Altísima calidad | Lento generando |
| LLM | Autorregresivo | Token a token | Texto coherente | Alucinaciones, contexto limitado |

### El hilo conductor: Probabilidad

Todos los modelos buscan lo mismo: **aprender cómo se ven los datos reales** para poder crear datos nuevos que se parezcan.

- **Autorregresivos**: aprenden a predecir cada pedacito dado los anteriores
- **VAEs**: aprenden a comprimir y descomprimir, forzando que el espacio comprimido tenga una forma conocida de la cual se pueda muestrear
- **GANs**: un generador aprende a crear datos realistas siendo obligado por un discriminador que intenta detectar las falsificaciones
- **Difusión**: aprenden a quitarle ruido a imágenes ruidosas, paso a paso
- **LLMs**: aprenden a predecir la siguiente palabra dado todo el texto anterior

---

## Pseudocódigo de cada modelo

### VAE

```
ENTRENAR:
    Para cada imagen X:
        μ, σ = Encoder(X)
        ε = punto aleatorio de campana estándar
        Z = μ + σ × ε              ← reparametrization trick
        X_recon = Decoder(Z)
        Loss = error_reconstrucción(X, X_recon) + KL(μ, σ)

GENERAR:
    Z = punto aleatorio de campana estándar
    Imagen_nueva = Decoder(Z)
```

### GAN

```
ENTRENAR D:
    loss_D = BCE(D(real), 1) + BCE(D(G(z).detach()), 0)

ENTRENAR G:
    loss_G = BCE(D(G(z)), 1)       ← flipeo: label=1 para fakes

GENERAR:
    imagen = G(ruido_aleatorio)
```

### Difusión

```
ENTRENAR:
    Para cada imagen limpia:
        t = paso aleatorio entre 1 y 1000
        ruido = punto aleatorio de campana estándar
        imagen_ruidosa = mezclar(imagen, ruido, t)
        ruido_predicho = modelo(imagen_ruidosa, t)
        loss = error_cuadrático(ruido, ruido_predicho)

GENERAR:
    x = pura estática aleatoria
    Para t = 1000 hasta 1:
        ruido_predicho = modelo(x, t)
        x = quitar_un_poco_de_ruido(x, ruido_predicho, t)
```

### Language Model

```
GENERAR:
    secuencia = tokenizar(prompt)
    Mientras no termine:
        scores = LM(secuencia)
        probabilidades = softmax(scores / temperatura)
        token = muestrear(probabilidades)    ← top-k, top-p, etc.
        si token == FIN: parar
        secuencia = secuencia + token
```

---

## Los prácticos del curso

| # | Tema | Dataset | Qué se hizo |
|---|---|---|---|
| 1 | Probabilidad | Tennis (14 obs) | Estimar distribuciones, muestrear datos nuevos |
| 2 | Distribuciones continuas | Iris (150 flores) | Gaussianas, KDE, mixturas, generar flores nuevas |
| 3 | Autorregresivo (Hinton) | MNIST | Matriz triangular, BCE, generar dígitos píxel a píxel |
| 4 | VAE | Fashion-MNIST | Encoder-Decoder, reparametrization, explorar espacio latente |
| 5 | GAN (DCGAN) | Fashion-MNIST | Generador vs Discriminador, detectar mode collapse |
| 6 | Language Models | Texto | GPT-2, tokenización, Top-K/Top-P, temperatura |
| 7 | Difusión | CIFAR-10 | Forward/reverse process, U-Net, generar desde ruido |

---

## El obligatorio

**Entrega**: 8 de diciembre, 21:00 (estricto)
**Grupos**: hasta 3 personas
**Presentaciones**: 11 y 18 de noviembre (obligatorio asistir)

**Objetivo**: implementar una técnica generativa de interés personal con prototipo funcional, métricas de evaluación definidas, y un informe con resultados.

**Evaluación**: Técnico 60% | Evaluación del modelo 20% | Presentación 20%

**Temas sugeridos**: image captioning, variantes de GANs, variantes de VAEs, language models, generación de audio.

**Consejo clave del profesor**: mejor algo pequeño y que funcione que algo grande e incompleto.

---

## El insight central del curso

> Los modelos de Deep Learning que usás para clasificar son, en realidad, estimadores de probabilidades. Si cambiás tu perspectiva de "quiero predecir una categoría" a "quiero generar datos nuevos eligiendo al azar de esas probabilidades", la misma herramienta se convierte en un generador.

---

## Estructura del curso clase por clase

| Clase | Fecha | Tema |
|---|---|---|
| 1 | 19-08-2025 | Introducción, modelos generativos, probabilidad básica |
| 2 | 26-08-2025 | Variables continuas, Gaussiana, Uniforme, Laplace, redes Bayesianas |
| 3 | 02-09-2025 | Mixturas de Gaussianas, modelos autorregresivos, Hinton |
| 4 | 09-09-2025 | KL Divergence, NLL, BCE, entrenamiento de autorregresivos |
| 5 | 16-09-2025 | Implementación de Hinton, MLE formal, estabilidad numérica |
| 6 | 30-09-2025 | Variational Autoencoders: ELBO, reparametrization trick, β-VAE |
| 7 | 07-10-2025 | GANs: minimax, DCGAN, entrenamiento alternado |
| 8 | 14-10-2025 | Lectura del obligatorio, conditional GANs, mode collapse |
| 9 | 21-10-2025 | Modelos de lenguaje, tokenización, sampling, GPT-2 |
| 10 | 28-10-2025 | Modelos de difusión: forward/reverse, DDPM, Stable Diffusion |
| 11 | 04-11-2025 | Evaluación: IS, FID, Perplexity, BLEU, ROUGE, evaluación humana |
| 12 | 11-11-2025 | Exposiciones de proyectos, aplicaciones |
| 13 | 18-11-2025 | Exposiciones orales |
| 14 | 25-11-2025 | Transformers, Self-Attention, Multi-Head Attention, cierre |

---

*Compilado a partir de las transcripciones de las 14 clases, explicaciones detalladas, flujos completos, funciones de pérdida, pseudocódigo, y todos los materiales del curso.*
