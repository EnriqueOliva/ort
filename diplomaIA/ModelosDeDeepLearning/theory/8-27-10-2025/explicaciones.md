# Clase 27 de Octubre 2025 - Deep Learning
## Explicaciones para Principiantes Absolutos

---

# ANTES DE EMPEZAR: ¿QUÉ NECESITO SABER?

## ¿Qué es una computadora para nosotros en esta clase?

Una computadora es básicamente una **calculadora muy poderosa**. Solo sabe hacer operaciones matemáticas con números. **NO entiende palabras, imágenes, ni nada que no sean números.**

Todo lo que hacemos en esta materia es encontrar formas de convertir cosas (imágenes, texto, audio) en números para que la computadora pueda trabajar con ellos.

## ¿Qué es Machine Learning (Aprendizaje Automático)?

Imagina que quieres enseñarle a una computadora a distinguir fotos de gatos de fotos de perros.

**Forma tradicional (programación normal):**
Le escribes reglas específicas: "Si tiene orejas puntiagudas Y bigotes largos Y ojos rasgados, entonces es gato."

**Problema:** Es imposible escribir todas las reglas. ¿Qué pasa con gatos sin bigotes? ¿Gatos de perfil? ¿Gatos tapados parcialmente?

**Forma Machine Learning:**
En lugar de escribir reglas, le muestras a la computadora **miles de fotos de gatos y miles de fotos de perros** (esto se llama "datos de entrenamiento"). La computadora **sola descubre los patrones** que distinguen a los gatos de los perros.

Es como enseñarle a un niño: no le das una lista de reglas, le muestras muchos ejemplos hasta que "aprende" a reconocerlos.

## ¿Qué es una Red Neuronal?

Una red neuronal es un **tipo de modelo de Machine Learning** que está inspirado (muy vagamente) en cómo funcionan las neuronas del cerebro.

**Imagínalo así:**
- Es una **cadena de operaciones matemáticas**
- Los datos entran por un lado (por ejemplo, los píxeles de una imagen)
- Pasan por varias "capas" de procesamiento (cada capa transforma los datos de alguna manera)
- Al final sale una respuesta (por ejemplo, "esto es un gato con 95% de probabilidad")

**Cada "capa"** es simplemente:
1. Tomar los datos de entrada
2. Multiplicarlos por unos números (llamados "pesos")
3. Sumarle otro número (llamado "bias")
4. Aplicar una función matemática (llamada "activación")
5. Pasar el resultado a la siguiente capa

## ¿Qué son los "pesos"?

Los pesos son **los números que la red va ajustando para aprender**.

Imagina que tienes una receta de cocina. Los ingredientes son los datos de entrada, y las cantidades de cada ingrediente son los pesos. Si el pastel sale mal (la predicción es incorrecta), ajustas las cantidades (los pesos) hasta que el pastel salga bien.

Cuando decimos que "la red está aprendiendo", lo que realmente está pasando es que **los pesos se están ajustando** para que las predicciones sean cada vez mejores.

## ¿Qué significa "entrenar" una red?

Entrenar una red es el proceso de **ajustar los pesos** hasta que la red haga buenas predicciones.

**El proceso básico es:**
1. Le das datos a la red (por ejemplo, una foto de gato)
2. La red hace una predicción (por ejemplo, "esto es un perro")
3. Comparas con la respuesta correcta y calculas **qué tan equivocada está** (esto se llama "error" o "loss")
4. Ajustas los pesos un poquito para que **la próxima vez se equivoque menos**
5. Repites esto MILLONES de veces con diferentes datos

## ¿Qué es "Deep" en Deep Learning?

"Deep" significa "profundo". Se refiere a que la red tiene **MUCHAS capas** (50, 100, o incluso más).

**¿Por qué muchas capas?**
- Las primeras capas aprenden cosas simples (por ejemplo, "aquí hay una línea diagonal")
- Las capas del medio combinan esas cosas simples en conceptos más complejos ("aquí hay una forma triangular")
- Las últimas capas combinan todo para reconocer conceptos abstractos ("esto parece una oreja de gato")

**En teoría:** Más capas = más capacidad de aprender patrones complejos.

## ¿Qué es "backpropagation" (retropropagación)?

Es el algoritmo que se usa para **calcular cómo ajustar los pesos**.

**Imagina esto:**
1. La red hace una predicción
2. Calculamos el error (qué tan lejos estamos de la respuesta correcta)
3. Necesitamos saber: ¿cuánto contribuyó cada peso a ese error?
4. Backpropagation es un método matemático que **va desde el final hacia el principio** calculando la "culpa" de cada peso

Es como cuando algo sale mal en un proyecto de equipo y quieres saber quién tuvo la culpa de cada parte del problema.

## ¿Qué es una "derivada"?

Sin entrar en matemáticas complicadas: una derivada te dice **cuánto cambia algo cuando modificas otra cosa**.

Si tienes una función que relaciona tus pesos con el error, la derivada te dice: "Si aumentas este peso un poquito, ¿el error sube o baja? ¿Cuánto?"

Es como cuando mueves el volante del auto: la derivada te dice si vas a girar hacia la izquierda o la derecha, y qué tan brusco será el giro.

---

# PARTE 1: EL PROBLEMA DE LAS REDES MUY PROFUNDAS

## 1.1 El Problema: Redes Profundas que No Aprenden

### La expectativa vs. la realidad

**Lo que esperarías:**
- Si una red de 18 capas aprende bien
- Entonces una red de 34 capas debería aprender MEJOR
- Porque tiene más capacidad, más "cerebro" para procesar información

**Lo que realmente pasaba (antes de 2016):**
- La red de 34 capas aprendía PEOR que la de 18 capas
- Incluso en los datos de entrenamiento
- ¡La red con más capacidad no podía ni siquiera memorizar los datos de entrenamiento!

**Esto es MUY raro.** Es como si contrataras a un empleado más inteligente y resulta que hace peor trabajo que uno menos inteligente.

### ¿Por qué pasa esto? El "Vanishing Gradient" (Gradiente que Desaparece)

Recuerda que para entrenar la red necesitamos **ajustar los pesos de cada capa**.

Para ajustar los pesos, usamos backpropagation, que va **desde el final hacia el principio**, calculando cuánto hay que ajustar cada peso.

**El problema matemático:**
- Las capas que están al final (cerca de la salida) reciben una señal clara de cuánto ajustarse
- Pero para las capas del principio, la señal tiene que **pasar por todas las capas intermedias**
- En cada capa, la señal se **multiplica por números** (las derivadas)
- Si esos números son pequeños (por ejemplo, 0.5), al multiplicar muchas veces: 0.5 × 0.5 × 0.5 × 0.5 × ... = algo MUY pequeño

**Ejemplo numérico simple:**
Si tengo 50 capas y en cada una la señal se multiplica por 0.5:
- Después de 10 capas: 0.5^10 = 0.001 (ya es pequeño)
- Después de 20 capas: 0.5^20 = 0.000001 (casi cero)
- Después de 50 capas: 0.5^50 = prácticamente CERO

**¿Qué significa esto en la práctica?**

El profesor lo explica así: **"Es como que se te quedó sin batería el auto."**

Las primeras capas reciben una señal tan débil que básicamente **no se actualizan**. No aprenden. Se quedan congeladas con sus pesos iniciales aleatorios.

Es como si en una empresa, los jefes de arriba toman decisiones, pero el mensaje nunca llega a los empleados de abajo. Los empleados hacen cualquier cosa porque no saben qué deberían hacer.

### El problema opuesto: "Exploding Gradient" (Gradiente que Explota)

Es lo mismo pero al revés: si los números que multiplicas son grandes (por ejemplo, 2), al multiplicar muchas veces se vuelven ENORMES.

2 × 2 × 2 × 2 × ... = números GIGANTESCOS

**¿Qué pasa?**
Los pesos cambian de manera muy brusca. La red "salta" de un lugar a otro en vez de ir mejorando gradualmente.

Como dice el profesor: **"la loss puede variar muy bruscamente"** - un momento parece que la red está aprendiendo, al siguiente todo se descontrola.

**¿Cuál es peor?**

Según el profesor, el exploding gradient es **menos grave** porque tiene una solución simple: "Gradient Clipping" (ponerle un límite máximo al gradiente). Es como decir "no importa qué tan grande sea el número, nunca lo dejes pasar de 10".

El vanishing gradient es el problema difícil porque la señal simplemente **desaparece** y no hay cómo recuperarla.

---

## 1.2 La Solución: Skip Connections (Conexiones que "Saltan")

### La idea genial

En 2016, unos investigadores propusieron una solución elegante:

**En lugar de obligar a la información a pasar por TODAS las capas**, le damos un "atajo" para que pueda **saltar directamente** de una capa a otra.

Es como si en una empresa con muchos niveles jerárquicos, permitieras que los mensajes importantes **salten directamente** del CEO a los empleados, sin tener que pasar por cada gerente intermedio.

### Dos formas de hacer skip connections

Hay dos maneras de implementar estos "atajos":

1. **Suma (aditivo)** - usado en ResNet (2016)
   - La información que salta se **SUMA** con la información procesada

2. **Concatenación** - usado en DenseNet (2017)
   - La información que salta se **PEGA AL LADO** de la información procesada

En esta clase nos enfocamos principalmente en la **suma** (ResNet).

---

## 1.3 ResNet: Cómo Funciona la Suma

### El concepto básico

Imagina una capa normal de la red:
- Entra un dato: **x**
- La capa hace su procesamiento: **F(x)** (F representa "todas las operaciones de esta capa")
- Sale el resultado: **F(x)**

Ahora, en ResNet añadimos un "atajo":
- Entra un dato: **x**
- La capa hace su procesamiento: **F(x)**
- PERO TAMBIÉN dejamos pasar **x** directamente
- La salida es: **F(x) + x**

Esto se escribe como: **H(x) = F(x) + x**

Donde:
- **H(x)** = lo que sale de esta capa (la salida final)
- **F(x)** = lo que la capa aprendió a hacer (el "residuo")
- **x** = la entrada original que pasa directamente (la "identidad")

### ¿Por qué esto soluciona el vanishing gradient?

**El truco matemático es este:**

Cuando calculas la derivada de **H(x) = F(x) + x**, obtienes:
- La derivada de F(x) (que puede ser pequeña)
- MÁS la derivada de x respecto a x, que siempre es **1**

¡Ese **1** es la clave!

No importa qué tan pequeña sea la derivada de F(x), al sumarle 1, el resultado **nunca será cero**. La señal siempre puede pasar.

Es como tener una autopista principal (la x que pasa directamente) aunque las calles secundarias (la F(x)) estén congestionadas.

### ¿Qué es un "residuo"?

Un estudiante preguntó esto en clase: **"¿Cuál es la definición de residuo?"**

El profesor respondió: **"Residuo es el error respecto a algún target que tú tengas."**

**Ejemplo de regresión lineal:**
- Tienes datos (puntos en un gráfico)
- Dibujas una línea recta que intenta pasar por los puntos
- El residuo es **cuánto se aleja cada punto de la línea**

**En ResNet:**
- El "target" es la identidad (dejar x igual)
- El residuo F(x) es **cuánto la red decide alejarse de simplemente pasar x**

### ¿Por qué es más fácil aprender así?

El profesor lo explica con esta cita clave:

**"Es más fácil en la práctica entrenar algo respecto a la identidad, es decir, cuánto se desvía de la identidad, que cuánto se desvía de cero."**

**¿Qué significa esto?**

**Sin skip connections:**
- Cuando agregas una capa nueva, tiene que aprender desde cero qué hacer
- Si la capa no aprende bien, el modelo empeora
- Es como contratar a alguien nuevo y esperar que haga todo perfecto desde el día 1

**Con skip connections:**
- La información pasa directamente (x)
- La capa solo tiene que aprender **cuánto modificar** esa información
- Si F(x) es muy pequeño, la salida es básicamente x, y el modelo **no empeora**
- Es como contratar a alguien nuevo pero tener un empleado experimentado supervisando: si el nuevo no sabe qué hacer, el experimentado se encarga

**Otra forma de pensarlo:**

- Sin skip: "Aprende a hacer el trabajo completo desde cero"
- Con skip: "Aprende qué pequeños ajustes hacer al trabajo que ya está hecho"

El segundo es mucho más fácil.

---

## 1.4 Bloques Residuales: La Estructura Práctica

### ¿Qué es un bloque residual?

Un bloque residual es **la unidad básica de construcción de ResNet**. Es la implementación práctica de la idea F(x) + x.

### Estructura típica de un bloque (para imágenes):

1. **Convolución** (una operación que procesa imágenes buscando patrones)
2. **Batch Normalization** (una técnica que estabiliza el entrenamiento)
3. **Activación ReLU** (una función que introduce no-linealidad)

Luego se repite esto, y al final **se suma con la entrada original x**.

### Un detalle técnico importante: el problema de ReLU

**¿Qué es ReLU?**
Es una función muy simple: si el número es negativo, lo convierte en cero. Si es positivo, lo deja igual.
- ReLU(-5) = 0
- ReLU(3) = 3
- ReLU(-100) = 0
- ReLU(7) = 7

**El problema:**
ReLU solo produce valores positivos o cero. Nunca negativos.

Si F(x) siempre es ≥ 0 (porque pasó por ReLU), entonces:
- H(x) = F(x) + x siempre será ≥ x
- La salida siempre está "por arriba" de la entrada

**La solución:**
En bloques con múltiples capas residuales, **no se pone ReLU en la última capa** para permitir que F(x) pueda ser negativa si es necesario.

### El problema de las dimensiones

Un estudiante preguntó sobre esto en clase.

**El problema:**
Para poder sumar F(x) + x, ambos deben tener **la misma dimensión** (el mismo "tamaño").

Imagina que x es un vector de 64 números, pero F(x) es un vector de 128 números. ¡No puedes sumarlos directamente!

**Soluciones:**

1. **Si x es un vector:**
   - Multiplicar x por una matriz W que lo lleve a la dimensión correcta
   - La fórmula queda: H(x) = F(x) + Wx

2. **Si x es una imagen:**
   - Usar una **convolución 1×1** para cambiar el número de canales
   - El profesor explica: "El kernel de uno por uno es como si multiplicaras a todos [los canales] por el mismo número"

En los diagramas de ResNet, **las líneas punteadas** indican estos casos donde hay que ajustar dimensiones.

---

## 1.5 Las Arquitecturas Originales de ResNet

### ¿Qué son las ResNet famosas?

En el paper original de 2016, los autores propusieron varias versiones:
- **ResNet-18:** 18 capas
- **ResNet-34:** 34 capas (la más común según el profesor)
- **ResNet-50, ResNet-101, ResNet-152:** versiones más profundas

**IMPORTANTE:** Todas estas arquitecturas **YA incluyen las skip connections**. Las skip connections son lo que hace que funcionen.

### Estructura de un bloque típico

Para ResNet más profundas, un bloque típico se ve así:

1. **Convolución 1×1** que reduce de 256 a 64 canales (hace las cosas más pequeñas para procesar más rápido)
2. Batch Normalization + ReLU
3. **Convolución 3×3** con 64 canales (el procesamiento principal)
4. Batch Normalization + ReLU
5. **Convolución 1×1** que vuelve a 256 canales (vuelve a la dimensión original)
6. **SUMA con x** ← **ESTA ES LA SKIP CONNECTION**

Todo lo anterior (pasos 1-5) es **F(x)**.
Al final se hace **H(x) = F(x) + x**.

---

## 1.6 Los Resultados que Comprobaron que Funciona

### El experimento clave

Los investigadores compararon:
- Red de 18 capas vs. Red de 34 capas
- Con y sin skip connections

### Sin skip connections (el problema):

- La red de 34 capas tiene **MAYOR error** que la de 18 capas
- Incluso en los datos de entrenamiento

**Un estudiante preguntó si esto era "sobreajuste".**

**Respuesta del profesor:** "No es un problema de sobreajuste. Lo que está pasando es que tenés un modelo que en principio es mucho más potente, pero le va peor en train."

### ¿Qué es sobreajuste y por qué esto NO lo es?

**Sobreajuste (overfitting):**
- La red **memoriza** los datos de entrenamiento
- Le va MUY BIEN en entrenamiento
- Le va MAL en datos nuevos (validación)
- Es como un estudiante que memoriza las respuestas del examen pero no entiende el tema

**Lo que pasa aquí es diferente:**
- La red de 34 capas le va mal **INCLUSO en entrenamiento**
- No puede ni siquiera memorizar los datos
- El problema es que **no está aprendiendo bien** debido al vanishing gradient
- Es como un estudiante que ni siquiera puede memorizar las respuestas

### Con skip connections (la solución):

- Los resultados se invierten
- La red de 34 capas ahora sí **performa mejor** que la de 18
- Porque ahora sí puede aprender correctamente

---

## 1.7 Otra Razón Por la Que Funciona: Múltiples Caminos

### Más allá del vanishing gradient

El profesor explica que las skip connections tienen **otro beneficio inesperado**.

### La idea de los múltiples caminos

Cuando tienes dos bloques residuales:
- Bloque 1: H1 = F1(x) + x
- Bloque 2: H2 = F2(H1) + H1

Si expandimos H2:
```
H2 = F2(F1(x) + x) + F1(x) + x
```

**¿Qué significa esto?**

La información tiene **múltiples caminos** para llegar al final:

1. **x puede pasar directamente** sin ninguna modificación (a través de las skip connections)
2. **x puede pasar solo por F1** (se procesa una vez)
3. **x puede pasar solo por F2** (se procesa una vez)
4. **x puede pasar por F1 y F2** (se procesa dos veces)

El profesor dice: **"El número de caminos por los cuales la información puede pasar desde el inicio hasta el final son muchos."**

Con 56 capas, el número de caminos crece **exponencialmente** (se multiplica en cada capa).

### El efecto "ensemble" (conjunto de modelos)

**¿Qué es un ensemble?**
Es una técnica donde combinas las predicciones de **muchos modelos simples** para obtener una predicción mejor.

Es como cuando preguntas a 100 personas y te quedas con la respuesta más votada. Cada persona puede equivocarse, pero el grupo en conjunto suele acertar.

**¿Cómo se relaciona con ResNet?**

El profesor explica:
- Es como tener un ensemble de muchos modelos simples
- Cada "caminito" (cada forma de llegar de la entrada a la salida) es como un modelito simple
- Todos comparten los mismos pesos (no hay parámetros extra)
- Esto da un **efecto regularizador** (ayuda a que la red no se sobreajuste)

### ¿ResNet agrega parámetros extra?

Un estudiante preguntó: **"¿Hay parámetros que se entrenen o es como la mayoría de las regularizaciones que vimos?"**

**Respuesta del profesor:** "Las ResNet no agregan ningún parámetro más. Tienen exactamente la misma cantidad de parámetros que la red sin residual connections, pero son mucho más fáciles de entrenar."

Esto es importante: **las skip connections son gratis**. No hay costo adicional en términos de memoria o parámetros.

---

## 1.8 Pregunta de Parcial Mencionada por el Profesor

El profesor dijo en clase: **"A mí haciendo las diapos se me ocurrió una pregunta de parciales que era mostrar un grafiquito de estos y decir, 'Bueno, ¿cuál tiene residual connections?'"**

Luego un estudiante dijo: "La retiro para que no la uses en el parcial."

El profesor: "Dale. Buenísimo. Qué retirada, qué borrada del registro."

---

### ⚠️ POSIBLE PREGUNTA DE PARCIAL ⚠️

---

#### 📝 PREGUNTA:

**"Se muestran dos gráficos de entrenamiento: uno compara una red de 18 capas vs una de 34 capas, y otro compara las mismas arquitecturas pero con una modificación. ¿Cuál de los dos gráficos corresponde a redes con residual connections?"**

#### ✅ RESPUESTA:

La red que tiene residual connections es aquella donde **la red más profunda (34 capas) tiene MEJOR rendimiento que la red menos profunda (18 capas)**, tanto en training como en validación.

Si observamos que la red de más capas tiene **PEOR error de entrenamiento** que la de menos capas, entonces esa red **NO tiene residual connections**, porque está sufriendo el problema de **vanishing gradient**: los gradientes se hacen tan pequeños al retropropagar por tantas capas que las primeras capas no se actualizan correctamente, y el modelo no puede aprender bien aunque tenga más capacidad expresiva.

Esto **NO es sobreajuste** (porque también le va mal en training), sino un **problema de optimización**.

Con residual connections, la suma "+x" mantiene derivadas constantes de 1, permitiendo que los gradientes fluyan hacia atrás y las capas iniciales se actualicen, por lo que agregar más capas SÍ mejora el rendimiento.

---

## 1.9 Observación sobre los Gráficos

Un estudiante (Atilio) preguntó sobre los gráficos que tienen "sectores bien demarcados", como si hubiera saltos en el entrenamiento.

**Explicación del profesor:**
- El eje X está en **escala logarítmica** (10 a la cuarta batches)
- No son épocas, son iteraciones
- Los "saltos" ocurren tanto con como sin residual connections

**Interpretación:** "Se ve que es un fenómeno que se da en varias redes... a la hora de ir bajando agarra una bajada en el landscape y le da baja baja baja hasta que se estanca y hasta que encuentra otra nueva bajada y sigue bajando."

Es como bajar una montaña con escalones: bajas un tramo, llegas a una meseta, buscas por dónde seguir bajando, y continúas.

---

## 1.10 DenseNet: La Otra Forma de Hacer Skip Connections

El profesor dice: **"A esta le doy menos importancia porque la idea es la misma, salvo que es la misma idea llevada al extremo."**

### ¿Cuál es la diferencia principal?

| Aspecto | ResNet | DenseNet |
|---------|--------|----------|
| Año | 2016 | 2017 |
| Cómo conecta | **SUMA** la información | **CONCATENA** (pega al lado) la información |
| Conexiones | Cada bloque se conecta con el siguiente | Cada capa se conecta con **TODAS las siguientes** |

### ¿Qué significa "concatenar"?

**Sumar:** Si tienes [1, 2, 3] y [4, 5, 6], el resultado es [5, 7, 9]
**Concatenar:** Si tienes [1, 2, 3] y [4, 5, 6], el resultado es [1, 2, 3, 4, 5, 6]

En DenseNet, la información no se combina sumándola, sino **pegándola al lado**.

### Dense Blocks

En un Dense Block:
- Cada capa recibe la salida de **TODAS las capas anteriores**
- La última capa recibe información de todas
- La penúltima recibe de todas menos la última
- Y así sucesivamente

El profesor dice: **"Esta está conectada con todas las siguientes, esta con todas las siguientes, esta con todas las siguientes."**

### Transition Blocks

DenseNet también tiene "transition blocks":
- Una convolución
- Un pooling (reducción de tamaño)
- Sirven para resumir la información acumulada

El profesor explica: **"Como que reutilizases características que ya fueron descubiertas de forma más explícita. Los bordes que había descubierto una capa convolucional los llevaste hasta el final."**

### ¿Cuál tiene más parámetros?

**ResNet tiene más parámetros que DenseNet.**

Aunque DenseNet tiene más conexiones, reutiliza información de manera más eficiente.

### ¿Cuándo usar cada una?

Un estudiante preguntó: **"¿Cuándo usarías una y cuándo la otra?"**

**Respuesta del profesor:** "Eh, bien, la verdad tirar una moneda y ahí la que te salga."

Luego aclara:
- "Estas ya pasaron de moda"
- ResNet todavía se usa
- DenseNet no tanto
- "Habría que mirar un estudio comparativo"

---

## 1.11 Referencias para Estudiar

**Para estudiar:**
- El paper de ResNet (2016): 9 páginas, "se lee bien"
- El libro de Dive into Deep Learning: "tres, cuatro páginas y el paper"

---

# PARTE 2: PROCESAMIENTO DE LENGUAJE NATURAL (NLP)

Después de un descanso, el profesor continúa con un tema completamente diferente.

---

## 2.1 ¿Qué es NLP?

**NLP = Natural Language Processing = Procesamiento de Lenguaje Natural**

Es la disciplina que estudia **cómo hacer que las computadoras "entiendan" el lenguaje humano**.

El profesor explica: **"Es una disciplina en la cual clásicamente había muchos lingüistas que estudiaban estas cosas y en realidad se la comió la ciencia de datos/machine learning/deep learning."**

### El problema fundamental

Las computadoras solo entienden **números**. No entienden palabras, frases, ni significados.

Cuando tú escribes "hola", la computadora ve una secuencia de códigos (104, 111, 108, 97 en ASCII). No tiene idea de que es un saludo.

El desafío de NLP es encontrar formas de **convertir texto en números** de manera que la computadora pueda trabajar con él.

---

## 2.2 Aplicaciones Principales de NLP

El profesor enumera los "típicos problemas":

### 1. Sentiment Analysis (Análisis de Sentimientos)

**¿Qué es?**
A partir de reseñas, comentarios, posteos, deducir el sentimiento escondido detrás del mensaje.

**Ejemplos de preguntas que responde:**
- ¿La persona está contenta o frustrada?
- ¿Va a volver a comprar el producto?
- ¿Va a recomendar la película?

**Uso práctico:** Las empresas lo usan para analizar miles de reseñas automáticamente sin que un humano tenga que leerlas todas.

### 2. Machine Translation (Traducción Automática)

**¿Qué es?**
Traducir automáticamente de un idioma a otro.

El profesor dice: **"Fue un gran problema durante mucho tiempo, hasta más o menos 2015."**

**¿Por qué es difícil?**
- Los idiomas cambian el orden de las palabras
- Cambian el largo de las frases
- Una palabra puede tener múltiples traducciones según el contexto
- "No es algo para nada obvio"

**Importancia histórica:**
Este problema motivó la creación de los **mecanismos de attention** (atención), que luego dieron origen a los Transformers y a modelos como GPT.

El profesor menciona a Bahdanau: "que nadie lo conoce, que inventó junto con Bengio y otros los mecanismos de atención estudiando problemas de machine translation"

**Nombre técnico:** "Problemas de seq to seq, de secuencia a secuencia"

### 3. Text Summarization (Resumen de Texto)

Tomar un texto largo y generar un resumen automáticamente.

### 4. Text Classification (Clasificación de Texto)

Asignar categorías a textos. Por ejemplo: ¿este email es spam o no spam?

### 5. Otras Aplicaciones

- **Texto a voz (Text to Speech)**
- **Reconocimiento de voz (Speech Recognition)**

El profesor aclara: **"También usan el mismo tipo de técnicas que el procesamiento de lenguaje natural, porque son datos que vienen en secuencia. Un audio es una señal a lo largo del tiempo."**

### Estado actual (2025)

El profesor dice: **"Hoy me digo que está todo integrado en una especie de herramienta única, que son los grandes modelos de lenguaje."**

(Se refiere a modelos como GPT, Claude, etc.)

---

## 2.3 ¿Qué Significa "Entender" un Texto?

El profesor da un ejemplo:

**Texto:**
"literally your Facebook message app is useless I only want it to increase profit. Please fix yourself Facebook."

**De este texto, un humano puede extraer:**
- **Emoción:** Alguien frustrado
- **Tono:** Negativo
- **Subjetividad:** Es una opinión personal
- **Entidades:** Facebook (organización), mensaje app (producto)
- **Adjetivos:** Useless (inútil)
- **Idioma:** Inglés
- **Formalidad:** Informal

El profesor dice: **"Todo eso significa entender un texto básicamente."**

### Otro ejemplo: Extracción de Información

**Frase:** "Cynthia sold the bike to George for $500"

**Un humano extrae automáticamente:**
- Vendedor: Cynthia
- Comprador: George
- Artículo: bicicleta
- Precio: $500

El profesor dice: **"Eso también requiere cierta comprensión de lo que está escrito."**

---

## 2.4 Las Dificultades del Lenguaje Natural

### Dificultad 1: El Contexto lo es TODO

El profesor dice: **"El lenguaje natural es terriblemente sensible al contexto."**

**"Cualquier frase sacada del contexto puede querer decir... la gente puede hacer querer inducir significados sacando las cosas de contexto."**

**Ejemplo dado en clase:**

La frase: **"Take your clothes off"** (Quítate la ropa)

**Diferentes contextos:**
1. Un extraño gritando a la nada en la calle → Perturbador
2. Dos amantes en una habitación → Romántico
3. Una madre a punto de bañar a su hijo → Normal, cotidiano
4. Un doctor antes de un examen médico → Profesional

El profesor: **"O sea, el contexto incluye casi tanto como la frase en sí."**

**¿Cómo manejan esto los modelos modernos?**

El profesor dice: **"Los grandes modelos de lenguaje preentrenados han logrado conquistar"** este problema.

### Dificultad 2: Los Sinónimos

Una sola palabra puede significar muchas cosas.

**Ejemplo en inglés:**
La palabra "culture" puede significar:
- Cultivation (cultivo)
- Civilization (civilización)
- Refinement (refinamiento)
- Society (sociedad)
- Education (educación)
- Y más...

El profesor: **"Una propia una sola palabra puede tener significados diferentes y eso también es un problemón para los algoritmos."**

### Dificultad 3: La Correferencia

El profesor dice: **"Esto fue un dolor de cabeza hasta hace poco."**

**¿Qué es la correferencia?**
Es cuando usamos palabras como "él", "ella", "esto", "lo" que **refieren a algo mencionado antes**.

**Ejemplo:**
"I voted for Nader because he was most aligned with my values, she said"

**Correferencias:**
- "she" (ella) refiere a "I" (la persona que habla)
- "my" (mi) también refiere a "I"
- "he" (él) refiere a "Nader"

El profesor explica: **"Toda esa dependencia de esa correferencia que hay en el texto, cuando somos chicos nos cuestan bastante aprenderlas, pero después de un tiempo son como intuitivas para nosotros, pero son difíciles de aprender [para máquinas]."**

---

## 2.5 El Pipeline (Proceso) de NLP

El profesor dice: **"Esto es bastante general para cualquier problema de lenguaje natural."**

Luego aclara: **"Esto también puede que esté un poco viejo porque las aplicaciones... ¿qué es lo que se está estilando ahora? Es intentar agarrar algún modelo preentrenado y fine-tunearlo o usarlo directamente."**

**Pero si vamos a lo básico:**

### Paso 0: El Corpus

**¿Qué es un corpus?**
- Es tu **conjunto de datos** (dataset)
- Puede ser un montón de documentos o un documento gigante
- En NLP, el dataset se llama **corpus** (terminología específica del campo)
- Cada dato puede ser un texto concreto: un email, una reseña, un artículo, etc.

### Paso 1: Preprocesamiento

El profesor dice: **"Siempre hay alguna etapa de preprocesamiento de esos datos."**

**¿Por qué es necesario?**
- El texto puede tener tags de HTML que no queremos
- Si son emails puede haber información irrelevante (firmas, encabezados)
- Puede haber mayúsculas y minúsculas mezcladas
- Pueden haber signos de puntuación que no necesitamos

**Ejemplos de preprocesamiento:**
- Dejar todo en minúscula
- Quitar las comas
- Eliminar etiquetas HTML
- Quitar espacios extra

El profesor dice: **"Hay todo un preprocesamiento como para dejarlo limpito."**

**IMPORTANTE:** Esto se hace **completamente a mano**. Tú decides qué limpiar según tu problema específico.

### Paso 2: Tokenización

El profesor dice: **"Hoy por hoy la palabra token se ha popularizado un poquito más."**

**¿Qué es tokenizar?**
Es **pasar de un texto continuo a una lista de piezas** (tokens).

**Ejemplo:**
- Texto: "El gato negro duerme"
- Tokenizado: ["El", "gato", "negro", "duerme"]

**Los tokens pueden ser:**
- Palabras completas
- Pedazos de palabras
- Sílabas
- Incluso caracteres individuales

El profesor dice: **"Generalmente esto es medio antiguo y depende un poco de la tarea en cuestión."**

### Paso 3 (Opcional): Eliminación de Stop Words

**¿Qué son los stop words?**
Son palabras muy comunes que generalmente no aportan significado útil.

**Ejemplo:**
Si buscas "el auto verde", lo importante es "auto" y "verde".
La palabra "el" se puede eliminar sin perder información relevante.

**Stop words comunes en español:** el, la, los, las, un, una, de, que, y, en, con, por, para...

**Stop words comunes en inglés:** the, a, an, is, are, was, were, of, to, in, for...

El profesor dice: **"En algunas aplicaciones... palabras como esas se sacan porque no tienen relevancia."**

**Beneficio:** Reduce el tamaño del vocabulario, haciendo el problema más manejable.

**¿Se usa hoy?** El profesor dice: **"Para aplicaciones modernas no se usa tanto."**

### Paso 4 (Opcional): Stemming y Lemmatization (Reducción a la Raíz)

**¿Para qué sirve?**
Reducir diferentes formas de una palabra a una raíz común.

**Ejemplo en español:**
- jugaba → jugar
- jugábamos → jugar
- jugarían → jugar

**Ejemplo en inglés:**
- running → run
- ran → run
- runs → run

**Beneficio:** Reduce aún más el vocabulario.

**¿Se usa hoy?** El profesor dice: **"Tampoco es necesario, sobre todo en las aplicaciones modernas."**

Pero para aplicaciones sencillas (detector de spam, análisis de sentimiento básico), **sí funciona bien**.

#### ¿Cuál es la diferencia entre Stemming y Lemmatization?

**STEMMING:**
- Es más "bruto"
- Corta las palabras siguiendo reglas simples
- Puede dejar palabras **que no existen en el idioma**
- Ejemplo: "organization" → "organ" (¡"organ" existe pero no es la raíz correcta!)
- Ventajas: Simple y rápido
- Desventaja: El texto queda incomprensible

**LEMMATIZATION:**
- Es más "inteligente"
- Busca la **raíz gramatical correcta**
- Las raíces resultantes **sí existen en el idioma**
- Ejemplo: "organization" → "organization" (mantiene la palabra correcta)
- Ejemplo: "better" → "good" (encuentra la forma base)

**Ejemplos del profesor:**

| Palabra | Stemming | Lemmatization |
|---------|----------|---------------|
| Dancing | danc | dance |
| Dancer | danc | dancer |
| Organization | organ | organization |
| Happiness | happi | happy |

#### Pregunta de un estudiante sobre idiomas

**Pregunta:** "¿Y por idioma?"

**Respuesta del profesor:** "Sí. Tal cual. Tenés que elegir un idioma. Cuando vas a implementar un reductor de raíz como estos, tenés que elegir en qué idioma lo vas a usar."

**Implicación práctica:** "Puedes tener un buen detector de spam en inglés, pero pésimo en español."

#### ¿Es trabajo manual?

**Pregunta de un estudiante:** "¿Esto es un trabajo manual?"

**Respuesta del profesor:** "Manual en el sentido de que alguien alguna vez lo hizo manual... como SGD. Como cuando usas cualquier modelo de optimización, la primera vez el que lo implementó por primera vez hizo todo el paso a paso. Acá también: esta palabra tiene esta raíz, esta palabra tiene esta raíz."

**"Hoy no lo haces manual. Usas lo que alguien hizo."** (Es decir, usas librerías ya implementadas)

### Paso 5: VECTORIZACIÓN (La Parte Más Importante)

El profesor enfatiza: **"Esta parte sí que es la parte central de todas las aplicaciones modernas."**

**¿Por qué es tan importante?**

El profesor dice: **"Con una lista de strings no podemos hacer nada. Lo tenemos que transformar en vectores."**

**El problema:** Las computadoras solo entienden números. Necesitamos convertir palabras en números de alguna manera.

El profesor dice: **"Vectorizar un texto no es tan trivial. Es que digo, podemos sentarnos a pensar otras ideas, ah, pero no es algo tan sencillo de hacer."**

---

## 2.6 Formas de Vectorización

El profesor presenta varias formas, desde las más simples hasta las más sofisticadas.

---

### 2.6.1 Bag of Words (BoW) - Bolsa de Palabras

**¿Qué es?**
Es la forma **más simple** de convertir texto en números.

El profesor dice: **"Hay una forma bien sencilla de transformar un texto en vectores."**

**¿Para qué sirve?**
- Sentiment Analysis
- Detección de spam

El profesor dice: **"Incluso en algunas aplicaciones del estilo sentiment analysis y cosas, este tipo de cosas funcionan super bien. No hace falta hacer nada sofisticado... una regresión logística en función de BoW para saber si una reseña es positiva o negativa."**

**¿Por qué funciona para spam?**
El profesor explica: **"Para ese tipo de problemas importa un poco que aparezca la palabra. Si aparece esa mala palabra [típica de spam], ya está."**

#### ¿Cómo se construye?

**Paso a paso:**

1. **Define tu vocabulario** (todas las palabras únicas que vas a considerar)

2. **Crea una tabla:**
   - Una **fila por cada documento** (cada email, cada reseña, etc.)
   - Una **columna por cada palabra del vocabulario**

3. **En cada celda, pon:** cuántas veces aparece esa palabra en ese documento

**Ejemplo:**

Supongamos que tenemos estos documentos:
- Doc 1: "el gato negro"
- Doc 2: "el perro negro"
- Doc 3: "el gato gato"

Y este vocabulario: [el, gato, negro, perro]

La tabla Bag of Words sería:

|          | el | gato | negro | perro |
|----------|----|----- |-------|-------|
| Doc 1    | 1  | 1    | 1     | 0     |
| Doc 2    | 1  | 0    | 1     | 1     |
| Doc 3    | 1  | 2    | 0     | 0     |

**Resultado:** Cada documento es ahora un **vector de números**.
- Doc 1 = [1, 1, 1, 0]
- Doc 2 = [1, 0, 1, 1]
- Doc 3 = [1, 2, 0, 0]

¡Ahora la computadora puede trabajar con estos números!

#### Las Limitaciones de Bag of Words

**Un estudiante preguntó:** "¿Se pierde el orden?"

**Respuesta del profesor:** "Se pierde todo. Sí. O sea, solo cuenta frecuencias estadísticas de apariciones de palabras."

**¿Qué se pierde?**
- **El orden de las palabras:** "El perro mordió al hombre" vs "El hombre mordió al perro" dan el mismo vector
- **El significado semántico:** No sabe qué significan las palabras
- **La similitud entre palabras:** "perro" y "can" son completamente diferentes para BoW
- **Todo el contexto**

El profesor dice: **"Toda esa información se perdió."**

**¿Y las variantes de palabras (conjugaciones)?**

Un estudiante preguntó sobre "jumped" (saltó) vs "jump" (saltar).

**Respuesta del profesor:** "Eso es opcional... lo que importa para el Bag of Words es que vos tengas un vocabulario ya predefinido."

(Es decir, puedes usar stemming/lemmatization antes, o no. Depende del problema.)

---

### 2.6.2 TF-IDF (Term Frequency - Inverse Document Frequency)

**¿Qué problema resuelve?**

El profesor explica: **"Se pierde la relación que tiene cada documento con su propio corpus."**

**El problema con Bag of Words:**

Imagina que quieres detectar si un trabajo fue hecho con ChatGPT.

El profesor dice: **"Casi todos los obligatorios van a estar hechos con lenguaje que más o menos nosotros usamos. Y van a haber palabras que son raras en el propio corpus. Que no son usadas por los demás."**

Una palabra que aparece en TODOS los documentos no nos dice nada útil.
Una palabra que aparece en UN SOLO documento es muy informativa.

TF-IDF captura esta idea.

#### ¿Qué significa TF-IDF?

**TF = Term Frequency (Frecuencia del Término)**

Es básicamente Bag of Words, pero **normalizado** (dividido por el total de palabras del documento).

**Fórmula:**
```
TF(palabra, documento) = Número de veces que aparece la palabra / Total de palabras en el documento
```

**Ejemplo:**
Si un documento tiene 100 palabras y "gato" aparece 5 veces:
TF("gato", documento) = 5/100 = 0.05

Esto convierte los conteos en **proporciones/porcentajes**.

**IDF = Inverse Document Frequency (Frecuencia Inversa de Documento)**

Mide **qué tan rara es una palabra en todo el corpus**.

El profesor conecta esto con un concepto de teoría de la información:

**"¿Se acuerdan de entropía, de cómo medíamos el contenido de información de un evento que tiene probabilidad P de ocurrir?"**

- Si algo pasa siempre (probabilidad = 1) → no aporta información
- Si algo pasa muy raramente (probabilidad muy baja) → aporta MUCHA información

**Fórmula:**
```
IDF(palabra) = log(Total de documentos / Documentos que contienen la palabra)
```

**Ejemplos:**
- Si "el" aparece en todos los 100 documentos: IDF = log(100/100) = log(1) = 0 (no aporta información)
- Si "criptografía" aparece en 2 documentos: IDF = log(100/2) = log(50) = alto (muy informativa)

El profesor explica: **"Un token que aparece en todos los documentos no aporta información. Un token que aparece pocas veces aporta información."**

#### TF-IDF = TF × IDF

Simplemente multiplicas los dos valores.

**¿Qué significa un valor alto de TF-IDF?**
- La palabra aparece **frecuentemente en este documento** (TF alto)
- PERO es **rara en el corpus general** (IDF alto)
- Por lo tanto, es una palabra **característica/distintiva** de este documento

**¿Qué significa un valor bajo?**
- La palabra es muy común en todos los documentos (como "el", "de", "que")
- O aparece muy poco en este documento específico

#### Normalización opcional

A veces los valores de TF-IDF son muy pequeños. Se puede normalizar:
- Dividiendo por la suma de la fila
- Dividiendo por la norma euclidiana (raíz cuadrada de la suma de cuadrados)

Un estudiante preguntó: **"¿Cómo saca la columna norma?"**

El profesor respondió: **"La norma euclidiana que es sumar los cuadrados y hacer la raíz cuadrada."**

---

### 2.6.3 Label Encoding

**¿Qué es?**
Asignar a cada palabra un número único.

**Ejemplo:**
- "gato" → 1
- "perro" → 2
- "pájaro" → 3
- etc.

**El problema:**

El profesor explica: **"Lo pasamos a un número... pero qué quiere decir hacer A - B?"**

Si "gato" = 1 y "pájaro" = 3, entonces pájaro - gato = 2.

¿Qué significa ese 2? ¡Nada! Pero el modelo podría pensar que sí significa algo.

**"Ahora a y b tienen diferencia de uno en los encodings y a y c tienen diferencia de dos. ¿Qué quiere decir esa diferencia de dos?"**

El problema es que estamos **introduciendo relaciones numéricas que no existen** en el significado real de las palabras.

---

### 2.6.4 One-Hot Encoding

El profesor dice: **"Hay otra forma igual de mala de codificar que se llama One-Hot encoding, ya lo conocen, ¿verdad?"**

**¿Qué es?**
- Creas un vector del tamaño del vocabulario
- Pones un 1 donde está la palabra
- Todo lo demás son 0s

**Ejemplo:**
Vocabulario: [gato, perro, pájaro, pez]

- "gato" = [1, 0, 0, 0]
- "perro" = [0, 1, 0, 0]
- "pájaro" = [0, 0, 1, 0]
- "pez" = [0, 0, 0, 1]

**Diferencia importante con Bag of Words:**

El profesor aclara: **"Es diferente a lo anterior porque estamos hablando de vectorizar cada palabra, no el documento entero."**

- Bag of Words: un vector para TODO el documento
- One-Hot: un vector para CADA palabra

#### Problemas de One-Hot Encoding

1. **Vectores gigantes:** Si tienes 100,000 palabras, cada vector tiene 100,000 dimensiones

2. **Lleno de ceros:** 99.999% del vector son ceros, solo hay un 1

3. **No captura significado:** El profesor dice: **"Son vectores que podemos sumar y multiplicar... pero no quieren decir nada de esas multiplicaciones"**

4. **Palabras similares son completamente diferentes:**
   - "perro" = [0, 1, 0, 0]
   - "can" = [0, 0, 0, ..., 1, ..., 0]
   - ¡Parecen igual de diferentes que "perro" y "refrigerador"!

5. **Pésimo para contexto**

---

### 2.6.5 Word Embeddings (La Solución Moderna)

El profesor dice: **"Surge en el año 2013 la idea."**

**"En realidad existían de antes algunas ideas que llevaban hacia esto."**

El profesor conecta con conceptos previos: **"¿Se acuerdan cuando les hablé de representation learning, que les hablé de encontrar representaciones más adecuadas para los tipos de problemas?"**

#### ¿Es Deep Learning?

El profesor aclara: **"Todavía no era deep learning porque las redes que se usan para encontrar embeddings... el primero de todos, Word2Vec, es una red shallow, o sea, es poco profunda."**

(Solo tiene 2 capas, no es "profunda")

#### El Problema que Resuelven

El profesor plantea: Si mi diccionario tiene 10,000 palabras y uso One-Hot encoding → vectores de dimensión 10,000 llenos de ceros.

**La pregunta:** "¿Cómo podemos hacer para capturar toda la información que representa esa palabra en algo mucho más denso, más chiquito?"

**La respuesta:** "Por ejemplo... un vector de dimensión 100 puede ser suficiente."

#### ¿Qué es un Word Embedding?

Es una forma de representar cada palabra como un **vector denso de números** que captura su significado.

**Características:**

1. **Baja dimensión:** En lugar de 10,000 dimensiones, usas 100, 200 o 300

2. **Denso:** Sin ceros. El profesor dice: **"completamente lo opuesto a One-Hot"**

3. **Aprendido de los datos:** No se asigna arbitrariamente, se aprende

4. **Preserva estructura:** Aquí está la magia...

#### ¿Qué significa "Embedding"?

El profesor explica: **"La palabra embedding quiere decir encaje en español."**

**"Finalmente uno piensa cuando uno encaja algo en otra cosa, preserva las propiedades de lo que está encajando."**

**Contraste:**
- One-Hot encoding: "Es un mapeo cualquiera, es un mapeo de texto a vectores que **no preserva nada**."
- Word Embedding: "La idea es que preserve por lo menos alguna estructura que el texto tenga."

#### ¿Qué propiedades se preservan?

**1. Direcciones con significado gramatical:**

El profesor explica: **"Las direcciones de ese espacio representen cosas gramaticales."**

**Ejemplos:**
- Una dirección en el espacio = cambiar el género (rey → reina)
- Otra dirección = cambiar el número (gato → gatos)
- Otra dirección = cambiar el tiempo verbal (corro → corrí)

**2. Relaciones vectoriales que tienen sentido:**

**El ejemplo famoso:**
```
king - man + woman ≈ queen
(rey) - (hombre) + (mujer) ≈ (reina)
```

El profesor explica: **"No tiene por qué dar exactamente queen, pero da un vector cuyo embedding más cercano es queen."**

**¿Qué significa esto?**
- Si a "rey" le quitas el concepto de "hombre" y le agregas "mujer", obtienes "reina"
- Los embeddings capturan estas relaciones semánticas automáticamente

#### Pregunta sobre la dimensionalidad

**Pregunta de un estudiante:** "¿El espacio puede tener capacidad para una cantidad mayor de palabras del vocabulario? Yo tengo mi vocabulario son 100 palabras y hago un embedding de 10 o 20 dimensiones."

**Respuesta del profesor:** "Sí, la dimensión del embedding va a ser un hiperparámetro."

"Vas a tener que las palabras van a estar diseminadas en diferentes lugares, no van a estar cerquita."

**Aclaración importante:**
El profesor explica que las dimensiones no tienen significados absolutos, sino relativos.

**"Capaz que no es la dimensión original. Hay una especie de cambio de base de este espacio en el cual ahora esta dimensión que podría ser parte de la base quiere decir algo, quiere decir cambiar de género."**

Es decir: moverse en cierta dirección del espacio significa algo (como cambiar de masculino a femenino), aunque esa dirección no sea exactamente uno de los ejes originales.

#### ¿Cómo se entrenan los embeddings?

**Dos opciones:**

**1. Entrenar de cero para tu problema específico:**

El profesor dice: **"Quieren hacer spam detection. Pueden hacer una capa de embedding al principio y después poner un MLP, un par de capas y que diga si es spam o no."**

**"El propio embedding va a ser entrenado usando el propio problema que se desea resolver. Entonces va a encontrar la mejor representación de las palabras para ese problema en cuestión."**

**2. Usar embeddings preentrenados:**

El profesor menciona: **"Hay un montón de embeddings preentrenados."**

**Embeddings famosos:**
- **Word2Vec** (2013) - El primero
- **GloVe** (Google, 2014)
- "Hay dos o tres más famosos"

**"Si buscan por ahí 'Word Embedding preentrenados conocidos' van a ver ahí una listita de cuatro o cinco."**

---

### 2.6.6 Word2Vec en Detalle

El profesor dice: **"Yo les voy a hablar de Word2Vec porque fue el primero."**

#### Dos Arquitecturas de Word2Vec

**1. CBOW (Continuous Bag of Words)**
- El profesor dice: "No sé por qué se llama así"
- **Dado el contexto, predice la palabra central**

**2. Skip-gram**
- El profesor dice: "También es medio misterioso el nombre"
- **Dada la palabra central, predice el contexto**

#### ¿Cómo se entrenan? Aprendizaje Autosupervisado

**¿Qué datos se usan?**

El profesor dice: **"Se entrenan usando todo Wikipedia. Creo que el original de Word2Vec era usando Wikipedia."**

**"El de Google creo que se usó con anuncios de publicidad y cosas así."**

**IMPORTANTE:** No hace falta tener los documentos separados.

El profesor explica: **"No hace falta tenerlos separados en documentos, sino que puede ser un pedazo de texto gigantesco que se va recorriendo."**

**"Es lo mismo que los language models."**

#### CBOW: Del Contexto a la Palabra

**¿Cómo funciona?**

1. Miras una **ventana de texto** (por ejemplo, 5 palabras)
2. **Tapas la palabra central** (la del medio)
3. Con las palabras del contexto (las que rodean), **predices cuál es la palabra tapada**

**Ejemplo visual:**
```
[El] [gato] [___] [en] [el]
              ↑
         ¿Cuál es?
```

Respuesta correcta: "duerme" (o alguna palabra que tenga sentido ahí)

El profesor explica: **"Yo ahora conozco la verdad porque la palabra que está acá yo sé cuál es."**

**Tipo de aprendizaje:**

El profesor dice: **"Es un problema de aprendizaje autosupervisado."**

**"Yo tengo datos que los puedo volver etiquetados de forma muy sencilla, como por ejemplo, ocultar una parte y decir 'la etiqueta es esa'."**

**Analogía con imágenes:**
El profesor da una analogía: **"En imágenes se hace también: se tapa una parte de la imagen y se entrena un modelo para que la rellene. Vos conocés la verdad porque tenías la foto entera."**

#### Skip-gram: De la Palabra al Contexto

Es exactamente al revés: dada una palabra, predice cuáles son las palabras que la rodean.

**Ejemplo:**
```
[___] [___] [duerme] [___] [___]
                ↓
         ¿Cuál es el contexto?
```

Respuesta: "El", "gato", "en", "el" (o algo así)

**Un estudiante observó:** "Yo ese segundo caso como que de una palabra sacar podría sacar muchos contextos, ¿no?"

**Respuesta del profesor:** "Sí, de una palabra podrías tener muchos contextos. Tal cual."

**"Me parece más restrictivo el otro [CBOW]."**

El profesor está de acuerdo: **"Porque el otro tenés cuatro datos para sacar uno y es como que de acá al revés tenés uno para sacar cuatro."**

#### La Arquitectura de la Red

El profesor pregunta a la clase: **"¿Quién tiene cuántas capas tiene?"**

**Respuesta:** "Dos."

**Estructura:**
```
Input Layer    →    Embedding Layer    →    Output Layer
(Vocabulario)        (ej: 300 dim)         (Vocabulario)
```

**Input Layer:**
- Tamaño = tamaño del vocabulario (ej: 10,000)
- Las palabras entran codificadas en **One-Hot**

**Primera Capa (Embedding):**
- El profesor dice: **"Es el embedding, que en realidad no tiene activación"**
- **"Es una transformación, no tiene activación"**
- Dimensión típica: 300
- "Va a pasar de, no sé, 10,000 palabras a 300"

**¿Cómo funciona?**

El profesor explica: **"Es una capa densa."**

**"Básicamente lo que está haciendo es agarrar ese One-Hot y multiplicarlo por una matriz."**

**Truco del One-Hot:**

El profesor dice: **"Es como agarrar la columna que corresponde de esa matriz, la columna que corresponde a esa palabra."**

**"Las columnas de esta matriz van a estar indexadas de acuerdo a la palabra y cada columna me va a dar un vectorcito de dimensión 300."**

**Segunda Capa:**
- Vuelve al tamaño del vocabulario
- Es "como un embudo" que se expande de nuevo

#### Confusión sobre las Activaciones

Hubo un poco de confusión en clase sobre si había activaciones o no.

**Aclaración del profesor:** **"Perdón. O sea, el embedding te quedas sin la activación. La red tiene activación, pero el embedding lo cortas antes."**

**"Acá puede haber una [activación] perfectamente. No sé qué activación, pero hay."**

La red completa tiene activación (porque si no, dos capas lineales serían equivalentes a una sola). Pero cuando extraemos el embedding, nos quedamos solo con la primera capa, antes de la activación.

#### Digresión: ¿Por qué funciona sin activación para embeddings?

Un estudiante cuestionó por qué dos capas lineales sin activación serían útiles.

**Respuesta del profesor:**

**"Podría servir igual para el objetivo del problema. Podría servir igual porque esa factorización no es obvia."**

**"Vos estás agarrando una matriz y la estás factorizando de una forma especial."**

**Ejemplo: Sistemas de Recomendación**

El profesor da un ejemplo detallado:

**"Hay métodos para los sistemas de recomendación que consisten en hacer una matriz con usuarios y productos."**

**"Podrías llegar a poner el ranking que usó, o una matriz de 0 y 1 [si compró o no]."**

**"Un método de recomendación es factorizar esa matriz como producto de dos matrices."**

**Resultado:**
- El espacio de salida de la primera matriz = embedding de los **productos**
- El espacio de entrada de la segunda = embedding de los **clientes**

**"Podés llevar clientes y productos a un mismo espacio de embedding y mirar la similitud entre esos vectores."**

**"Si hay mucha similitud le recomiendo el producto, si hay poca similitud no se lo recomiendo."**

#### Construcción del Dataset de Entrenamiento

El profesor muestra cómo se crean los datos:

**Texto:** "This is the first document"

**Con una ventana de tamaño 5:**
Se recorre el texto extrayendo pares (contexto, palabra central).

**Ejemplos de pares:**
- Contexto: [this, is] → Palabra central: the
- Contexto: [is, first] → Palabra central: the
- etc.

#### CBOW en Acción

**Proceso:**
1. Tomamos las palabras del contexto
2. Las convertimos a One-Hot
3. Hacemos el **promedio** (o suma) de los One-Hots
4. Eso entra a la red
5. La red predice probabilidades para cada palabra del vocabulario
6. Tomamos la palabra con mayor probabilidad

**El profesor explica:** **"Eso es lo que entra acá. Pasa por esta capa que no sé qué hace y después pasa por esta otra capa que no sé qué hace pero me devuelve probabilidades."**

**"Agarro la palabra que tenga mayor probabilidad."**

**Función de pérdida:**

Un estudiante preguntó: **"En el caso anterior la pérdida va a ser la entropía cruzada?"**

El profesor: **"Sí, sí, sí... Categórica. En los dos casos categórica."**

(Es decir, cross-entropy loss, típica para problemas de clasificación)

#### Skip-gram en Acción

**"Entra la palabra central, pasa por la red y se toman los dos valores más probables, como es una ventana de tamaño dos."**

#### Observación Importante: No usa el orden

Un estudiante observó: **"La información de si las palabras de contexto están antes o después, no la uso."**

El profesor confirma: **"No. No viste que no lo usa. Solo trata de adivinar cuál es el contexto."**

**"Word2Vec no usa cuál es la que iba antes y cuál es la que iba después. Lo único que importa es adivinar cuál es el contexto."**

#### El Output Final

**Salida de la red:**
El profesor explica: **"La salida es con una softmax."**

**"Hacés el argmax para saber qué palabra era."**

**Lo importante - Quedarse con el Embedding:**

Un estudiante dice: **"Después me quedo solo con la parte del embedding."**

El profesor: **"Claro, una vez que entrenaste así te quedas. Tu embedding es solo esta matriz."**

**"Para cada palabra te dice cuál es el vector de ese espacio y tiene esas propiedades."**

#### Visualización de Word Embeddings

El profesor busca herramientas interactivas:

**"Busqué, si ustedes buscan Word Embedding playground o algo así."**

**Herramienta mencionada: TensorFlow Projector**

**"Esto es el PCA del Word Embedding en 3... podemos ponerlo en dos componentes."**

**Ejemplo con "King":**

**"Acá está King. Esto es un PCA no más."**

**"Acá me dice cuáles son las palabras más cercanas en el espacio: King, Queen, Throne, Son, Emperor."**

El profesor muestra frustración con la demo: **"Lo malo de esto es que tengo que pararlo en algún momento y no sé cuándo pararlo."**

#### Comparación con Autoencoders

Un estudiante hace una conexión:

**"Me trae a la mente lo que vimos en el autoencoder decoder."**

El profesor: **"Es muy parecido... porque hace [el espacio] chiquito y después grande, un espacio latente de esas dimensiones y después..."**

**"Exacto. Nosotros nos quedamos con el encoder. Acá nos estamos quedando con el [embedding]."**

#### ¿Por Qué Son Relevantes los Word Embeddings?

Un estudiante pregunta: **"¿Y por qué es relevante?"**

**Respuesta del profesor:**

**"Porque de cierta forma respeta ya sea la similitud de las palabras."**

**"King aparecía, su palabra más cercana era queen."**

**"Además tiene esas propiedades de que hay ciertas propiedades geométricas que se traducen en propiedades semánticas."**

**"No son numeritos cualesquiera, digamos."**

**Logro:**
**"Lograste representar el significado semántico de la palabra en un espacio latente."**

#### Uso en Modelos Posteriores

El profesor dice: **"Esto es lo que van a consumir las redes recurrentes, Transformers, todas esas cosas."**

**"Los Transformers tienen su propio embedding que se entrena al entrenar el transformer."**

**"Pero como primer paso quería hablarles de Word Embedding."**

Un estudiante pregunta: **"¿Podrías usar un embedding para hacer un entrenamiento de un modelo?"**

El profesor: **"Claro, vos puedes crear el propio embedding en función del problema que tenés, o sea, o usar un Word Embedding ya preentrenado como estos."**

---

## 2.7 Anécdota sobre las Comas

Un estudiante contó una historia interesante durante la discusión del preprocesamiento:

**Historia de los adivinos antiguos:**

**"Antiguamente los adivinos tenían frases que eran restringidas por comas."**

**"Por ejemplo: 'Iréis, volveréis, nunca en la guerra pereceréis.'"**

**"Entonces llegaba la señora llorando que su esposo había ido a la guerra, pero había muerto y le reclamaba al adivino."**

**"Y él le repetía la misma historia, pero le cambiaba la coma: 'Iréis, volveréis nunca, en la guerra pereceréis.'"**

**"Y cambiaba la coma y la adivinanza era cierta."**

**Respuesta del profesor:**

**"Tal cual, tal cual, tal cual."**

**"Pero también es opcional eso. Ese preprocesamiento es... si a vos en el problema que vas a estudiar, por ejemplo, para saber si un correo es spam o no, capaz que la coma no importa."**

**"Pero para saber si voy a volver de la guerra o no, capaz que sí."**

**"Es algo que depende... trabajando con el problema."**

---

# RESUMEN FINAL: LO MÁS IMPORTANTE DE CADA TEMA

## Redes Residuales (ResNet)

1. **El problema:** Las redes muy profundas no aprenden bien por el vanishing gradient
2. **La solución:** Skip connections que suman la entrada con la salida: H(x) = F(x) + x
3. **Por qué funciona:** La derivada de x respecto a x siempre es 1, así que los gradientes nunca desaparecen
4. **Bonus:** Crean múltiples caminos para la información, como un ensemble implícito
5. **No cuestan nada:** No agregan parámetros extra

## NLP Básico

1. **El problema fundamental:** Las computadoras solo entienden números, no texto
2. **El pipeline:** Preprocesamiento → Tokenización → Vectorización
3. **Bag of Words:** Contar frecuencias de palabras (simple pero pierde todo el contexto)
4. **TF-IDF:** Como BoW pero considera qué tan rara es cada palabra
5. **One-Hot:** Un vector con un solo 1 (ineficiente, sin semántica)
6. **Word Embeddings:** Vectores densos que preservan el significado

## Word2Vec

1. **Qué hace:** Crea embeddings que capturan relaciones semánticas (king - man + woman ≈ queen)
2. **CBOW:** Del contexto predice la palabra central
3. **Skip-gram:** De la palabra central predice el contexto
4. **Arquitectura:** Red de 2 capas (entrada → embedding de ~300 dim → salida)
5. **Resultado:** Una matriz donde cada columna es el vector de una palabra

---

## PRÓXIMA ENTREGA

El profesor anunció al final: **"Esta semana con Martín les vamos a poner una entrega. Es un cuestionario."**

**"Igual si quieren lo charlamos la semana que viene para entregar."**

---

*Documento generado para facilitar el estudio. Contiene las explicaciones del profesor de la manera más fiel posible.*
