# Explicación de Temas - Clase del 21-10-2025: Modelos de Lenguaje (Language Models)

## La Gran Pregunta: ¿Qué Estamos Construyendo?

Imagina que tienes una máquina que puede predecir cuál es la siguiente palabra en una oración. Le dices "Hola, ¿cómo" y ella te responde con las palabras que probablemente vengan después (como "estás", "andas", etc.) junto con qué tan probable es cada una. **Eso es un modelo de lenguaje**.

Esta clase cubre los modelos de lenguaje desde un punto de vista **conceptual y funcional**. A diferencia de lo que verán en Deep Learning (donde se estudia la implementación de modelos), aquí nos enfocamos en **qué son** y **cómo funcionan**.

Como dijo el profesor: "La idea es práctico bastante temprano hoy. Hoy vamos a ver un tema que entiendo lo van a tratar en deep learning desde el punto de vista de los modelos y acá lo vamos a ver desde el punto de vista más conceptual o de su funcionalidad."

---

## ¿Qué es un Modelo de Lenguaje?

### La Definición Más Simple

Cuando el profesor preguntó "¿Qué es un modelo de lenguaje?", alguien respondió correctamente: **"Predice la próxima palabra"**.

Un modelo de lenguaje es un sistema que:
1. Recibe texto (una oración o parte de ella)
2. Te dice cuál es la probabilidad de cada posible palabra siguiente
3. Te permite ir generando texto poco a poco

### Definición Más Formal

El profesor lo explicó así: "Son sistemas que emiten distribuciones de probabilidad a los que se les imputa una parte de una tira de un lenguaje y emiten un siguiente símbolo."

También los podemos pensar como **modelos autorregresivos** (similar a lo que vieron con píxeles): "Condicionado con los símbolos que el sistema vio previamente puede emitir un veredicto sobre cuáles son los siguientes más probables."

---

## La Definición Matemática Formal del Language Model

Esta es la parte MÁS IMPORTANTE de la clase desde el punto de vista teórico.

### La Función del Language Model

El profesor escribió en la pizarra:

```
LM: Σ* → Δ(Σ ∪ {end_of_sequence})
```

**¿Qué significa esto? Vamos por partes:**

### ¿Qué es Σ (Sigma)?

**Σ** es el **conjunto de símbolos** o **tokens** que consideramos válidos.

- Pueden ser palabras enteras: "hola", "casa", "computadora"
- Pueden ser partes de palabras: "comput", "adora"
- Son los "bloques básicos" con los que construimos nuestras oraciones

El profesor dijo: "Estos son los tokens del lenguaje... Pueden ser palabras enteras, pueden ser parte de palabras, son símbolos."

### ¿Qué es Σ* (Sigma Estrella)?

**Σ*** es la **clausura de Σ por concatenación**.

**¿Qué significa en lenguaje simple?**
- Son **TODAS las combinaciones posibles** de símbolos de Σ
- Todas las "tiras" o "secuencias" que puedes formar concatenando elementos de Σ

El profesor explicó: "Van a estar típicamente oraciones. No le vamos a poner letras así a nuestro sistema. Vamos a poner oraciones en algún idioma, lenguaje válido que tengan sentido o comunicaciones."

**Nota importante:** Formalmente, podrías meter cualquier cosa. El profesor dijo: "Podrías agarrar el teclado y sentarte arriba. Le doy enter y el sistema va a dar algo a la salida. ¿Qué hace eso? ¿Qué significa? No tengo idea." El sistema está entrenado para dar respuestas razonables cuando le das entrada razonable.

### ¿Qué es Δ (Delta)? - El Probability Simplex

**Δ(Σ ∪ {end_of_sequence})** representa el **probability simplex**.

**¿Qué es un probability simplex?**
- Es el **espacio de todas las distribuciones de probabilidad** sobre un conjunto
- La salida del LM es un **vector de probabilidades**
- Todos los valores suman 1
- Todos los valores están entre 0 y 1

El profesor lo resumió: "Este sistema recibe tiras, recibe texto y emite distribuciones de probabilidad."

### ¿Qué es {end_of_sequence}?

Este es un **símbolo especial** que indica que la secuencia ha terminado.

El profesor explicó con claridad: "El end of sequence también es un elemento que puede salir. Puede mi sistema, tiene la capacidad de emitir una distribución de probabilidad y esa distribución de probabilidad tiene un elemento que es el fin de la secuencia y ese elemento fin de secuencia tiene probabilidad de ocurrir."

**¿Cuál es la probabilidad de end_of_sequence?** Depende del contexto:
- Si escribes "Hola, ¿cómo" → Probabilidad de terminar muy baja (oración incompleta)
- Si escribes "Hola, ¿cómo estás?" → Probabilidad de terminar más alta (oración completa)

El profesor dio este ejemplo: "Capaz que si yo imputo 'Hola, ¿cómo' tiene poca probabilidad o nula de que termine. Pero si digo 'Hola, ¿cómo estás?' capaz que sí tiene probabilidad de ocurrir."

---

## ¿Cómo Funciona la Generación de Texto? (Generación Autorregresiva)

### El Proceso Paso a Paso

Los modelos de lenguaje funcionan de manera **autorregresiva**: generan texto **un token a la vez**, usando lo que ya generaron para decidir qué viene después.

### Ejemplo Concreto del Profesor

1. **Entrada inicial:** "Hola, ¿cómo"
2. **El modelo devuelve:** Una distribución de probabilidad sobre TODAS las palabras posibles:
   - "estás" → probabilidad 0.02
   - "milanesa" → probabilidad 0.01
   - ... (y así para todos los tokens que conoce)

3. **Muestreamos:** El profesor explicó: "Agarro, le paso este vector al numpy y le digo: 'Che, haceme un sample con esta distribución. Sampleame un elemento.'" Supongamos que sale "estás".

4. **Concatenamos:** "Lo vas a concatenar acá y lo vas a volver a imputar a tu sistema."

5. **Nueva entrada:** "Hola, ¿cómo estás"

6. **El modelo devuelve:** Otra distribución de probabilidad (diferente a la anterior):
   - Ahora "la probabilidad milanesa cae más y la probabilidad de estás cae también, pero justo se levanta la probabilidad de el signo de interrogación"

7. **Y así sucesivamente...**

El profesor describió el proceso como una **"calecita"** o loop: "Esa idea es de manera recursiva ir metiendo tiras, todas emitiendo una distribución, haciendo sampling sobre esa distribución y reimputándola a mi sistema."

---

## ¿Es el Modelo Determinístico o Estocástico?

Esta fue una pregunta importante que surgió en clase.

### El LM en sí es DETERMINÍSTICO

El profesor fue muy claro: "Para una tira de entrada, para un prefijo, para un conjunto de palabras, un conjunto de tokens, para una oración, la salida es un único vector."

**¿Qué significa esto?**
- Si le das la misma entrada ("Hola, ¿cómo"), **siempre** te devuelve el mismo vector de probabilidades
- Para "estás" siempre será 0.02, para "?" siempre será 0.15, etc.
- No hay aleatoriedad en el cálculo del LM

El profesor agregó: "Esto no es un sistema probabilístico, o sea, esto es un sistema determinístico que me da una distribución de probabilidad."

### Pero el PROCESO DE GENERACIÓN es ESTOCÁSTICO

¿Por qué? Porque **muestreamos** de esa distribución.

El profesor lo resumió: "Yo sobre esa distribución de salida hago el muestreo y eso es lo que me termina dando... al final termino muestreando tiras de sigma estrella."

### Nota sobre Implementaciones Reales

El profesor mencionó que en sistemas comerciales podría haber pequeñísimas variaciones numéricas: "En los modelos comerciales, no es directo que no haya... esto entra en un batch y ese batch dependiendo la carga del servidor puede dar una salida distinta."

Pero esto son "detalles que exceden un poco la parte más teórica." Lo importante: **teóricamente, el LM es determinístico**.

El profesor incluso sugirió probarlo: "Van a poder chequear si corren 100 veces eso, que todos los vectores que salen son el mismo. Exactamente."

---

## Tokenizers: Convirtiendo Texto en Números

### ¿Por qué Necesitamos Tokenizers?

Los modelos de lenguaje, en su interior, son **matrices que operan con vectores de números reales**.

El profesor explicó: "Todos los modelos que nosotros tenemos a fin de cuentas son matrices que reciben vectores reales en batch... son reales. Entonces, ¿cómo pasamos de texto a reales? Y eso es importante. Entonces, ahí es donde entra en juego lo que serían los tokenizers."

### ¿Qué Hace un Tokenizer?

Un tokenizer tiene dos funciones principales:
1. **encode**: Convierte texto → tokens → números
2. **decode**: Convierte números → tokens → texto

El profesor dijo: "Tienen dos funciones que son el encode y el decode que son las importantes."

### Formas de Tokenizar

El profesor mencionó varias opciones: "¿Cómo pasamos 'Hola, ¿cómo' a tokens toda la secuencia? No es tan directo."

- **Por palabras:** "Podríamos separarlo por palabras"
- **Por caracteres:** "Podríamos separarlo por caracteres"
- **Por partes:** "Podríamos separarlo por la mitad de hola, la mitad de como"
- **Cualquier otra forma:** "Varias otras formas y cualquier otra forma que se les ocurra"

El profesor enfatizó: "Lo importante ahí es qué nosotros definimos como token."

### Consistencia del Tokenizer: MUY IMPORTANTE

El profesor fue muy enfático: "Un modelo va con un tokenizer. Y eso tengan lo claro. ¿Cuál es el tokenizer? Se puede elegir, se puede cambiar, pero una vez que está todo hecho no se toca más el tokenizer."

**¿Qué pasa si usas otro tokenizer?**

El profesor explicó: "Si nosotros le pasamos otro tokenizer antes, hace cualquier cosa hasta el punto de que podríamos irnos de las posibles clases que tenemos. Podríamos decir token 35 que ni siquiera existe."

Usó una analogía: "Es como el encoding que vos hacés... un tipo de encoding y para vos el código cero es casa, tienes que casarte con eso porque poner cero y el modelo va a creer que es una casa. Puedes decir 'Ah, no, para mí el cero es un departamento.' Un modelo lo roba."

### Representación de Cualquier Texto

Alguien preguntó qué pasa si le paso un texto que no tiene token asociado.

El profesor respondió: "Cualquier palabra se tiene que poder tokenizar... porque una palabra si nosotros [no podemos tokenizarla]... no vas a poder reconstruir esa palabra."

Los tokenizers tienen:
- Tokens para caracteres individuales como fallback
- Tokens especiales para casos raros
- Estrategias de subpalabras para construir palabras desconocidas

### Evolución de los Tokenizers

El profesor explicó cómo han evolucionado:

**Antes:** "Se hacía muy vinculado a lo que es usos del lenguaje, de los idiomas, o sea, español, inglés, cada idioma tenía su tokenización."

**Ahora (como GPT):** "Lo que hace está muy asociado a temas de cálculos de teoría de la información en realidad donde se busca maximizar u optimizar el tamaño de representación. Entonces, para eso lo que se busca es qué tan común es un token, un conjunto de texto y a partir de ahí se empieza a definir."

El profesor observó: "Empieza a perderse mucho lo que es como el lenguaje natural, esa parte de estudio, lenguaje natural y los idiomas etcétera y pasa mucho a la eficiencia."

### Símbolos Especiales

El profesor mencionó que hay símbolos especiales importantes (entre barras |...|): tokens para fin de secuencia, separadores, caracteres especiales, etc.

---

## Logits y Softmax

### ¿Qué son los Logits?

Cuando le pasas texto a un modelo, la **salida cruda** son los **logits**.

El profesor explicó: "Los logits son lo que sería la salida cruda a esa capa de activación final."

Los logits son simplemente **números reales** (pueden ser positivos, negativos, grandes, pequeños). **NO son probabilidades todavía**.

El profesor agregó: "No representa una distribución de probabilidad porque la suma de los elementos... [no suma 1]."

### ¿Cómo Convertimos Logits en Probabilidades?

Usando la función **Softmax**.

El profesor preguntó: "¿Qué función de activación usamos para transformar un vector de reales directamente en una distribución de probabilidad?"

Respuesta: **Softmax**

### ¿Por qué No Solo Dividir por la Suma?

Alguien sugirió: "¿Por qué no hacer cada valor dividido la suma del vector?"

El profesor respondió: "¿Qué pasa si tengo valores negativos? Las probabilidades... si hago directamente el valor sobre el asunto, ese es el único tema que tenemos."

Si tienes logits negativos y los divides por la suma, obtienes "probabilidades" negativas, lo cual es imposible.

### ¿Cómo Funciona Softmax?

El profesor explicó: "La Softmax ya nos cubre los casos y no tenemos ningún problema... hay una exponencial en un lado."

La exponencial:
1. Convierte todos los números en positivos
2. Los números negativos se vuelven valores muy pequeños (pero positivos)

El profesor dijo: "Si sale negativo, chiquitito, más negativo, más chiquitita. Exactamente."

Softmax hace que los logits "se transformen en vectores reales cualquiera... en esa distribución de probabilidad."

---

## Estrategias de Sampling (Muestreo)

Una vez que tienes la distribución de probabilidad, necesitas **elegir** un token.

### Top-K Sampling

El profesor explicó: "El top K nos indica: bueno, vamos a muestrear sobre los K elementos más probables. Vamos a ignorar aquellos que tienen muy baja probabilidad."

**Proceso:**
1. Ordena todos los tokens por probabilidad
2. Toma solo los primeros K
3. Ignora todos los demás
4. Muestrea solo de esos K

El profesor aclaró que K es un número elegido "arbitrariamente".

**¿Por qué hacerlo?** Para eliminar tokens con probabilidad casi cero que no tienen sentido en el contexto.

### Top-P Sampling (Nucleus Sampling)

El profesor explicó: "Top P es similar, pero no es K sino que es la suma de la probabilidad acumulada de los ordenados más probables, vamos sumando la probabilidad hasta que lleguemos a P."

**Proceso:**
1. Ordena los tokens por probabilidad
2. Va sumando las probabilidades desde el más probable
3. Cuando la suma acumulada llegue a P, ahí cortas
4. Muestreas solo de esos tokens seleccionados

**Diferencia clave con Top-K:**
- Top-K: número fijo de tokens (siempre K)
- Top-P: número **variable** de tokens (depende de la distribución)

El profesor resumió: "Son dos formas distintas de reducir nuestro [espacio de muestreo]."

### Temperatura

Alguien preguntó si esto está relacionado con la temperatura.

El profesor explicó: "La temperatura es un parámetro que se le agrega a la softmax para hacer más suave o avisar, o no, la distribución básicamente, pero no está directamente relacionado con K."

**¿Qué hace la temperatura?**

El profesor usó una analogía: "Pensar en una función sin modo de solo un cero es una S. Y depende de la temperatura qué tan plana o qué tan vertical te queda."

- **Temperatura alta:** Suaviza la distribución (más aleatoriedad)
- **Temperatura baja:** Hace la distribución más puntiaguda (más determinismo)

**¿Afecta a Top-K?** El profesor aclaró: "La temperatura no te va a [cambiar] cuáles son los top K" porque no cambia el **orden** de las probabilidades.

**¿Afecta a Top-P?** "Te puede afectar cuántos símbolos te incluyen ese top P. Te cambia la integral de esa distribución."

---

## Criterios de Terminación

### ¿Cuándo Para el Modelo de Generar?

El profesor explicó que hay **dos formas** de terminar:

**1. El modelo quiere terminar (end_of_sequence)**
El modelo muestrea el token especial de fin.

**2. Alcanzamos el máximo de tokens**

El profesor advirtió: "Un modelo de lenguaje nos daba un token de salida. Pero no nos garantiza que en ningún momento el end of sequence tenga probabilidad de cero. Eso podría pasar. Entonces podríamos no terminar."

**Solución:** "Siempre le ponemos un máximo de la secuencia que bueno, llevamos hasta aquí, porque no tenemos ninguna garantía de terminar en esa definición de momento."

---

## Límites de Contexto del Modelo

### Los Modelos No Son Infinitos

El profesor fue claro: "Estos modelos no son infinitos. Yo no puedo meter, por lo menos en transformers..."

**¿Por qué?** Los transformers tienen una **estructura fija**. El profesor lo comparó: "Es como vos tenés un modelo que tiene 10 neuronas de entrada, no le puedes poner 12."

### Redes Recurrentes vs Transformers

El profesor mencionó brevemente: "Si el modelo de lenguaje fue implementado con otra cosa, no sé si redes recurrentes. Bueno, red recurrente no tiene largo contexto, o sea, tiene pérdida."

Las redes recurrentes pueden procesar secuencias largas, pero tienen pérdida de memoria para contextos muy extensos.

---

## Entrenamiento de un LM (Conceptual)

El profesor lo mencionó brevemente ya que no era el foco de la clase.

### El Proceso General

"¿Cuál es la gracia de esto? Bueno, dónde está la carrera acá es entrenar estos bichos."

**Fase 1 - Pre-entrenamiento:**
"Se hace una parte con descenso estocástico entrenando un clasificador donde el problema de clasificación es: para una secuencia de entrada tengo que predecir correctamente la siguiente, la siguiente palabra."

Ejemplo: Si la entrada es "Hola, ¿cómo estás", quiero que el modelo prediga "?" correctamente.

Se hace "sobre corpus muy grandes de texto."

**Fase 2 - Refinamiento:**
"Después hace refinamiento con técnicas similares o con técnicas de reinforcement learning donde, bueno, la señal de retroalimentación está asociada a un input humano que te dice qué tan buena es una frase."

---

## GPT-2 y la Práctica de Hoy

### ¿Por qué GPT-2?

El profesor explicó las razones: "¿Por qué este? Porque es uno más liviano porque no queremos tampoco hacerlo muy pesado, que tengo un tiempo relativamente razonable en una máquina razonable."

Incluso aclaró: "Van a ver que ni siquiera estamos en GPT-2, sino que una versión achicada de GPT-2."

### De Dónde Bajamos los Modelos

"Hugging Face... directamente vamos a bajar los pesos y vamos a poder usar."

Las librerías a usar: "transformers de Hugging Face y PyTorch."

### Objetivo de la Práctica

El profesor fue claro: "La idea un poco del práctico de hoy no es meternos en lo que sería la implementación de un modelo de lenguaje. Eso ya van a tener para hacerlo en Taller. La idea es trabajar sobre algo ya entrenado y jugar un poco con lo que serían las entradas y las salidas."

Lo más importante: "Para mí de la clase hoy es entender esto: un lenguaje matemáticamente es esto, entro una tira de tokens y me da una distribución de probabilidad."

### Pasos del Práctico

1. **Jugar con tokenizers diferentes** (GPT-2 y BERT) para ver que "diferentes tokenizers nos van a dar distintos tokens y se tokeniza de forma distinta."

2. **Cargar el modelo:** "Cargamos el modelo así, le ponemos el modo evaluación porque no vamos a estar entrenando ni nada."

3. **Ver los logits:** "Un poco hacemos un input para hacer los inputs. Como les decía, tenemos que hacer la tokenización del prompt... directamente lo pasamos, vemos lo que sería el shape y directamente hacemos el forward."

4. **Implementar Top-K y Top-P:** "La idea es un poco implementar lo que sería Top-K, Top-P, y directamente una función para hacer la generación manual."

5. **Comparar resultados:** Ver qué resultados da con diferentes parámetros, "Top-K, Top-P, temperatura" y comparar "GPT-2 pequeño vs GPT-2 más grande, tiempo de inferencia, qué tan mejor es."

---

## Puntos Clave Mencionados por el Profesor

### Sobre Tokenizers

"Un modelo va con un tokenizer. Y eso tengan lo claro."

"Distintos modelos usan distintos tokenizers y está bien. Lo importante es ser consistente."

### Sobre la Práctica

"La idea es que entiendan cómo funciona para atrás, que no es nada raro, lo más raro [son los tokenizers]."

### Sobre el Curso

"Cuanto más potente, cuanto más pesos tenga y bueno, más volátiles, más lindas van a ser las tiras y mayor contexto lo voy a poder imputar."

---

## Definiciones para el Parcial

**Modelo de Lenguaje (Language Model):** Sistema que recibe secuencias de tokens y devuelve distribuciones de probabilidad sobre el siguiente token posible; predice la próxima palabra de forma autorregresiva.

**Token:** Unidad básica de texto que el modelo procesa; puede ser una palabra completa, parte de palabra o carácter, dependiendo del tokenizer usado.

**Tokenizer:** Sistema con dos funciones (encode y decode) que convierte texto a números para el modelo y números de vuelta a texto; debe ser consistente con el modelo.

**Σ (Sigma):** Conjunto de símbolos o tokens válidos que el modelo puede procesar.

**Σ* (Sigma Estrella):** Clausura por concatenación de Σ; representa todas las combinaciones posibles de tokens, es decir, todas las secuencias posibles.

**Probability Simplex (Δ):** Espacio matemático de todas las distribuciones de probabilidad válidas; vectores donde cada elemento está entre 0 y 1 y todos suman 1.

**End of Sequence (EOS):** Token especial que indica fin de la secuencia; tiene su propia probabilidad que varía según el contexto de entrada.

**Generación Autorregresiva:** Proceso de generar texto token por token, donde cada nuevo token depende de todos los anteriores; es un loop recursivo.

**Logits:** Salida cruda del modelo antes de softmax; números reales que pueden ser negativos y no representan probabilidades todavía.

**Softmax:** Función de activación que convierte logits en distribución de probabilidad usando exponenciales; garantiza valores positivos que suman 1.

**Top-K Sampling:** Estrategia de muestreo que solo considera los K tokens más probables, descartando todos los demás; K es fijo y arbitrario.

**Top-P Sampling (Nucleus):** Estrategia de muestreo que incluye tokens hasta que la probabilidad acumulada sume P%; el número de tokens es variable.

**Temperatura:** Parámetro que modifica la softmax; alta temperatura = distribución más suave (creativo); baja temperatura = más puntiaguda (conservador).

**Determinismo del LM:** El modelo es determinístico (misma entrada = mismo vector de probabilidades); la estocasticidad viene del muestreo posterior.

**Contexto Máximo:** Límite de tokens que un modelo puede procesar; en transformers está determinado por la arquitectura fija.

**Máximo de Secuencia:** Límite impuesto a la generación porque no hay garantía de que el modelo genere EOS; evita generación infinita.

---

## Posibles Preguntas para el Parcial

**¿Qué es un modelo de lenguaje?**
Es un sistema que recibe una secuencia de tokens y devuelve una distribución de probabilidad sobre cuál debería ser el siguiente token, permitiendo generar texto de forma autorregresiva.

**¿Qué es Σ* (sigma estrella) en la definición formal?**
Es la clausura por concatenación del conjunto de tokens; representa todas las secuencias posibles que se pueden formar combinando elementos de Σ.

**¿El modelo de lenguaje es determinístico o estocástico?**
El modelo en sí es determinístico: misma entrada siempre da mismo vector de probabilidades. La estocasticidad aparece en el muestreo que se hace sobre esa distribución.

**¿Qué son los logits y por qué no son probabilidades?**
Son la salida cruda del modelo, números reales que pueden ser negativos y no suman 1. Se necesita aplicar softmax para convertirlos en probabilidades.

**¿Por qué softmax usa exponenciales y no solo división?**
Porque si hay logits negativos, la división simple daría probabilidades negativas. La exponencial convierte todo a positivo primero.

**¿Qué hace un tokenizer?**
Convierte texto a tokens (encode) y tokens a texto (decode). Es el puente entre lenguaje natural y la representación numérica que el modelo entiende.

**¿Puedo usar un tokenizer diferente al del modelo?**
No. Cada modelo está entrenado con su tokenizer específico. Cambiar el tokenizer hace que el modelo interprete incorrectamente la entrada.

**¿Cuál es la diferencia entre Top-K y Top-P sampling?**
Top-K selecciona los K tokens más probables (número fijo). Top-P selecciona tokens hasta acumular P% de probabilidad (número variable según la distribución).

**¿Cómo afecta la temperatura al sampling?**
Temperatura alta suaviza la distribución (más aleatorio/creativo). Temperatura baja la acentúa (más determinista/conservador). No cambia el orden de probabilidades.

**¿La temperatura afecta a Top-K?**
No afecta cuáles son los top K tokens porque no cambia el orden. Pero sí puede afectar Top-P porque cambia cuántos tokens necesitas para llegar a P%.

**¿Para qué sirve el token end_of_sequence?**
Indica que la secuencia debe terminar. Tiene su propia probabilidad en cada paso, permitiendo que el modelo decida cuándo parar de generar.

**¿Por qué necesitamos un máximo de tokens al generar?**
Porque no hay garantía de que end_of_sequence tenga probabilidad alta. Sin máximo, la generación podría continuar infinitamente.

**¿Por qué los modelos tienen contexto limitado?**
Por su arquitectura (especialmente transformers). Es como una red con N entradas fijas: no puedes meter N+1 valores.

**¿Cómo se entrena un modelo de lenguaje conceptualmente?**
Primero pre-entrenamiento con descenso de gradiente en clasificación (predecir siguiente token). Luego refinamiento con reinforcement learning y feedback humano.

**¿Por qué en la práctica usan GPT-2 y no GPT-4?**
Porque GPT-2 es más liviano, se puede correr en tiempo razonable en máquinas comunes, y es suficiente para entender los conceptos.

**¿Qué pasa si una palabra no está en el vocabulario del tokenizer?**
Se descompone en sub-tokens más pequeños que sí estén. Cualquier palabra debe poder tokenizarse para poder reconstruirla después.

**Explicar el proceso de generación autorregresiva.**
1) Entrada al LM → 2) Obtener distribución de probabilidad → 3) Samplear un token → 4) Concatenarlo a la entrada → 5) Volver al paso 1. Repetir hasta EOS o máximo de tokens.

**Si ejecuto el LM dos veces con la misma entrada, ¿obtengo el mismo texto?**
No necesariamente. Obtienes la misma distribución de probabilidad, pero el sampling es aleatorio, entonces los tokens seleccionados pueden variar.
