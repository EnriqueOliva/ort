# Explicación COMPLETA - Clase del 17-11-2025
# Attention Mechanisms y Transformers

---

## He leído EXHAUSTIVAMENTE la transcripción completa en 3 pasadas

Esta explicación incluye TODO lo que el profesor dictó en clase, con el nivel de detalle necesario para que alguien que no fue a clase pueda entender completamente todos los temas.

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

El profesor leyó directamente del paper. Aquí está la cita textual que dio en clase:

**"Los modelos propuestos recientemente para traducción neuronal por máquina a menudo pertenecen a la familia de encoder-decoders y codifican una secuencia fuente en un vector de largo fijo."**

El profesor aclaró: "Dice largo fijo, pero quiere decir dimensión fija. Los matemáticos tienen esas libertades."

Luego continuó leyendo: **"Lo que pasa es que esto es un cuello de botella en el mejoramiento del desempeño de esta arquitectura básica encoder-decoder."**

### La Solución Propuesta

El profesor siguió leyendo del paper:

**"Y proponemos extender esto permitiendo al modelo automáticamente soft buscar - buscar de forma soft - partes de la secuencia fuente o inputs que son relevantes para predecir la palabra target, sin tener que [codificar toda la frase en un vector fijo]."**

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

El profesor explicó: "Uno inicializa con un H0 el encoder, y básicamente abajo está el encoder. Entonces ingresaba eso en la celda del encoder, el X1, eso produce un H1, que produce en el siguiente punto al X2, produce el H2, así hasta el HTx."

**El vector de contexto C**:

"A partir de todos ellos o lo más común del último se genera un contexto. El contexto - esto era esencialmente el último hidden state."

El profesor también mencionó: "También se podían haber - se sabía que se podía devolver de repente la concatenación de todos ellos, alguna función de todos los hiddens y no solamente el último."

Pero aclaró: "Sin bien lo más común era devolver el último para que sirviera como contexto para el decoder."

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

Hubo una pregunta sobre cómo se inicializa H0. El profesor fue muy claro:

**"Lo más usual es inicializarlo como cero."**

Luego agregó algo importante: "Hay algunas versiones un poquito posteriores que usan esto como parámetro de la red. Entonces también es entrenable el H0 inicial."

Pero advirtió: **"Pero vos no querés un H0 aleatorio porque después cuando hagas inferencia... el H0 tiene que ser el mismo para todo tu dataset. Si no te queda con un algoritmo randomizado cada vez que va a correr."**

Resumió: "Generalmente este H0 es fijo. Este H0 fijo usualmente [es cero]. Y si no, lo más audaz es usarlo como parámetro entrenable de la red, que también cuenta en el backpropagation y se va actualizando hasta llegar a un H0 que la red aprende."

**Sobre S₀ (estado inicial del decoder)**:

El profesor explicó: "Una buena idea es ponerlo [el contexto C] en cada una de las celdas, no solo la primera. Y de repente también inicializar con un S cero que puede ser cero también."

Hubo confusión sobre si S0 era el contexto. El profesor aclaró: "Podés hacer de cuenta que esto no está. O podés además tener un S0 inicial si querés. Esto es como algo medio general."

Luego explicó mejor: "Para que te quede uniforme siempre lo que le va a entrar como contexto es S0 y C. Entonces S1 y C. Para que te quede uniforme realmente el S0, o sea, tenés que ponerle la primera un S0 que usualmente es cero."

**Teacher Forcing vs Inferencia**:

El profesor recordó una diferencia clave:

"Esto se comporta distinto según si estoy en inferencia o si estoy en entrenamiento."

Un estudiante preguntó cómo era cada uno.

**En entrenamiento (Teacher Forcing)**:

"Si estoy en entrenamiento, por lo menos al principio, lo más probable es que haga teacher forcing, que es que esto va a producir un siguiente hidden state que se va a pasar al siguiente, pero también tengo el y1 verdadero que es lo que le voy a pasar como input también al siguiente."

**En inferencia**:

"En inferencia, en realidad busco el y1 que maximiza esta probabilidad."

El profesor resumió: "Y esto se repite. Ahora entra el contexto. Por eso vieron que la formulita es una función del contexto, el estado y el y(t-1). Entra acá [señalando el diagrama]."

---

## La Gran Idea de Bahdanau: Attention en Secuencias

### El Cambio Fundamental

El profesor leyó del paper:

**"Vamos a extender esto del encoder-decoder para que aprenda a alinear y traducir de forma conjunta."**

El término **"alinear"** es clave. El profesor explicó: "El mecanismo de atención es como una especie de mecanismo de alineación. Esta es una palabra que quedó en la terminología."

Luego leyó más del paper:

**"Cada vez que el modelo propuesto genera una palabra en una traducción, hace un soft search - búsqueda suave - para posiciones en las sentencias fuente, en el input, en donde está la información más relevante concentrada."**

### ¿Qué Significa "Soft Search"?

El profesor explicó: "Cada vez que se va a generar una nueva predicción, se va a hacer [una búsqueda] en las posiciones de la sentencia input. Se hace una búsqueda y se va a buscar información que relacione ese target que lo predecís con posiciones de la secuencia."

### La Nueva Fórmula

El profesor mostró el gran cambio:

**Antes**:
```
P(yᵢ) = función(C, Sᵢ₋₁, yᵢ₋₁)
```

**Ahora con Attention**:
```
P(yᵢ) = función(Cᵢ, Sᵢ₋₁, yᵢ₋₁)
```

El profesor lo explicó: **"¿Cuál es el único cambio que propone? Es hacer que esa [probabilidad] ahora dependa de un contexto que depende de la posición en la que estoy. Ahora dependa de un Cᵢ que depende de la posición en la que estoy en la lectura."**

Aclaró: "Podrías poner todo como una función de S-1. Es decir, que el contexto va a depender de la posición en la que estoy. Va a haber un C distinto para cada palabra target."

---

## ¿Cómo se Construye el Contexto Cᵢ?

### La Fórmula del Contexto

El profesor escribió la fórmula:

```
Cᵢ = Σⱼ αᵢⱼ × Hⱼ
```

Y la explicó: **"El contexto Ci va a depender de la secuencia entera de hidens del encoder. No se va a ser una especie de promedio ponderado de los hidens, donde la ponderación depende de cómo se relaciona el i con el j."**

Desglosando:
- **Hⱼ** son los hidden states del encoder (H₁, H₂, H₃, etc.)
- **αᵢⱼ** son los pesos de atención (números entre 0 y 1 que suman 1)
- **Cᵢ** es el contexto para la posición i del decoder

El profesor explicó más: "Acá yo estoy en la etapa i. Este contexto va a ser un promedio ponderado de todos estos hiddens, en donde la ponderación depende de cómo se relaciona el i con el uno, el i con el dos, el i con el j hasta el i con el TX."

### ¿De Dónde Salen los αᵢⱼ?

El profesor explicó que se calculan con una **softmax**:

```
αᵢⱼ = softmax(eᵢⱼ)
```

"Se calcula a través de una softmax. Esto tiene que - alfa i,j - pensarlo como una probabilidad o un peso que yo le doy."

Interpretación: "Si estoy en la posición i del decoder, ¿qué peso le doy a cada posición j del encoder? O cuán probable es que dependa de esa palabra, de esa posición."

### Los Scores de Alineación (eᵢⱼ)

Los **eᵢⱼ** son números que miden la alineación. El profesor los describió como:

"Generalmente se escriben así como una softmax de ciertos numeritos que se llaman scores de alineación o a veces energía. Analogías con la física, pero piénsenlo como una especie de alineación."

Explicó la intuición: **"Típicamente esto va a ser una especie de producto - piénsenlo, cuán parecidos o cuán alineados están, o sea, las direcciones de estos dos vectores que viven en el mismo espacio."**

Aclaró un punto importante: "El hidden del decoder vive en la misma dimensión que el hidden del encoder. Ustedes, por ejemplo, le pasaban el último [del encoder], se lo pasaban al decoder. Viven en el mismo espacio."

### ¿Qué Significa "Alineado"?

El profesor dio una definición informal: **"Esta palabra 'cuán alineado está', tómenla de forma vaga en el sentido de bueno, van en la misma dirección más o menos. No son ortogonales."**

---

## Por Qué Se Llama "Attention"

Esta es una pregunta que los estudiantes hicieron varias veces, y el profesor al principio no la respondió porque quería explicar primero todo el mecanismo.

Finalmente explicó: **"¿Ven cómo se construye este contexto? ¿Cuál es la idea que hay detrás de que sea una especie de attention?"**

**"Porque lo que está haciendo es ver el estado SI-1, que piénsenlo como lo que yo tengo construido hasta ese momento, cómo se alinea con los distintos hidens del encoder para hacer mi siguiente predicción. O sea, en cierta forma es a qué hidens presto más atención para hacer mi siguiente predicción."**

---

## La Terminología Moderna: Query, Key, Value

### De Dónde Viene

El profesor explicó: "Esto esto lo vamos a ver bien en un ratito. A la sucesión de hidens se les llaman los **keys**."

Luego aclaró: **"Los valores - miren, también van a ser los hidens del encoder. Es una especie de diccionario trivial en el que el H1 tiene como valor H1."**

"Y la **query** es [el hidden] del decoder."

### La Explicación Abstracta

El profesor dio una buena explicación: **"Es como que estoy preguntando cuando agarro un hidden del decoder, estoy preguntando en este diccionario, ¿cuál es el key que más se parece a [mi query]? O sea, básicamente es como si estuviera buscando esto dentro de este conjunto y ver cuál es el que más se alinea con esta query que yo estoy haciendo."**

Admitió: "O sea, esto es medio abstracto, pero este es un poquito la idea de la terminología moderna."

---

## Cómo Implementa Bahdanau el Attention (Attention Aditiva)

### El Diagrama Completo del Decoder

El profesor mostró un diagrama detallado y lo explicó paso a paso:

**Las entradas en el paso i**:

"Para cada paso i del decoder, ¿qué es lo que entra?"
1. **El input**: yᵢ₋₁ (la palabra anterior del target)
2. **El previous hidden**: Sᵢ₋₁
3. **Los encoder outputs**: Todos los H del encoder

### Paso 1: Embedding del Input

**"Acá entra el yi-1, se lo pasa por un embedding, un por-qué-no, y se obtiene el vector embebido que va directo a la GRU."**

El profesor también mencionó: "Se lo pasa por un embedding. Y le aplicas un dropout."

Pero luego dijo: **"El dropout si quieren olvídense."** - No es esencial para entender el concepto.

### Paso 2: Calcular los Scores de Alineación

El profesor explicó el proceso de proyecciones:

**"Proyecto - esto de proyectar quiere decir multiplicar por una matriz que lo lleve a un espacio de dimensión más pequeño. Es aplicar capas lineales sin activación y sin bias."**

Se multiplica:
- **Sᵢ₋₁** por una matriz **Wₛ**
- Cada **Hⱼ** por una matriz **Wₕ**

**"Se proyecta el hidden anterior [Sᵢ₋₁], lo mismo con el Hⱼ, el hidden, y después se lo suma. Esto es lo que se llama **attention aditiva**."**

### Paso 3: Aplicar Tangente Hiperbólica

```
Bᵢⱼ = tanh(Wₛ × Sᵢ₋₁ + Wₕ × Hⱼ)
```

El profesor explicó: "A eso le hacemos - porque nos encanta - una tangente hiperbólica. Y eso es lo que vamos a llamar el vector Bᵢⱼ."

Hubo una pregunta interesante de un estudiante: "¿Tiene sentido que sea una tangente hiperbólica y esto - voy a tirar un golazo - porque -1 entiendo que me daría que están ortogonales?"

El profesor respondió: **"Claro. Yo diría cero te diría que están como ortogonales. Y menos uno como que están así. Sí, sí, sí. O sea, sí, me imagino que queda más fácil de aprender."**

### Paso 4: Multiplicar por el Vector de Parámetros

```
eᵢⱼ = vᵀ × Bᵢⱼ
```

El profesor explicó: **"Estos son los vectores de alineación intermedia. Entonces si yo voy acá al dibujito, esto se va a multiplicar por un vector que es este align vector, que es un vector de parámetros, entrenable, y son los parámetros de la attention."**

Luego aclaró algo importante sobre la nomenclatura: "Los eᵢⱼ van a ser multiplicar, hacer el producto escalar - el dot product - entre ese B y el B tilde J. Acá hay un error: es beta tilde i,j."

### Paso 5: Softmax

```
αᵢⱼ = softmax(eᵢⱼ)
```

**"Y el alfa i,j es el softmax de eso."**

El profesor explicó qué significa cada cosa: "El beta tilde i,j es el vector intermedio que depende de j. El v no depende de nadie, son parámetros del mecanismo de atención. Y el alfa i,j es la probabilidad de alinear yi con la posición j."

### Paso 6: Crear el Vector de Contexto

```
Cᵢ = Σⱼ αᵢⱼ × Hⱼ
```

**"Al final ese vector de pesos es el que me va a decir cómo tengo que ponderar los hidens."**

"Entonces cuando salgo acá salen los attention weights, que es ese vector de pesos alfa, y ese vector de pesos alfa se multiplica con todos los hidens del encoder para hacer esa ponderación y darme el vector de contexto."

El profesor explicó que esto es un producto escalar: "Esto es un producto matricial, pero es un producto escalar. Es el producto escalar entre los pesos de atención y todos los hiddens y entonces me da un promedio ponderado de todos los hiddens y eso me va a dar el context vector para ese instante, el Ci."

### Paso 7: Entrada a la GRU

**"Ese C se le pasa a la GRU además del previous hidden además del yi-1 y eso va a producir un nuevo hidden el Si."**

### Paso 8: Predicción Final

**"Y a través de alguna capa lineal una predicción de cuál es el yi o cuál es su distribución."**

### Los Parámetros Entrenables

Hubo una pregunta sobre qué parámetros son entrenables. El profesor aclaró:

**"¿Cuáles son? Son el Ws y el Wh."**

Y sobre el vector v: "Y el beta tilde J. El v no depende de nadie, son parámetros del mecanismo de atención."

En resumen, los parámetros entrenables son:
- **Wₛ**: Matriz para proyectar el estado del decoder
- **Wₕ**: Matriz para proyectar los hiddens del encoder
- **v**: Vector de parámetros de attention
- **Los pesos del embedding**
- **Los pesos de la GRU**

---

## El Ejemplo Visual: La Matriz de Attention

### Cómo Es la Matriz

El profesor mostró ejemplos del paper original:

"Acá hay un ejemplo. No me quiero hacer justo además el paper. Dice: 'no es tan grande como su padre'. Quiere decir eso."

"Y acá tenemos el input, y paso 5, y acá la traducción, el output."

"Y esto se supone que lo que está graficando - muy bien, pero - son los alfa i,j."

### LA GRAN CONFUSIÓN: ¿Cómo Se Lee la Matriz?

Esta fue una de las partes más confusas de la clase. Los estudiantes preguntaron varias veces cómo leerla.

Un estudiante preguntó: "Para cada palabra de la entrada que está ahí, la columna es qué tan alineado está?"

Profesor: **"Es al revés."**

Estudiante: "¿Ah, al revés? Lo estoy leyendo mal."

Profesor: "Porque no - o sea, tu intuición es correcta, pero es - lo que nosotros queremos es... el que hace - el que produce - el que implementa el mecanismo de atención es el **decoder**."

### La Explicación Detallada

El profesor lo explicó con mucho cuidado:

**"Entonces el decoder ve como input todo esto [ya pasó por el encoder]. Ahora él va a predecir la primer palabra."**

**"Entonces lo que va a hacer es va a mirar acá porque es la primer palabra, pero va a mirar cómo se relaciona esa primer palabra, esa primera posición, y a la hora de predecir esa palabra - porque J no está predicho todavía - va a mirar la relación que hay - a qué palabras del input, qué palabras del input le tiene que prestar atención para predecir esta palabra."**

Un estudiante captó: "Ah, las más claras son las [más importantes]."

Profesor: **"Cuanto más claro más alto."**

### Ejemplos de Alineamiento

El profesor comentó sobre ejemplos específicos:

**"Por ejemplo, his está alineado con padre, que si ustedes saben del francés... Entonces yo que sé."**

**"Al principio como que lo que yo veo es que no tiene mucho sentido a qué cosas le presta atención."**

**"Después ya empieza bastante bien. Por ejemplo, his está alineado con padre. Entonces yo que sé. Y padre con padre también."**

El profesor bromeó: "Los dos primeros yo no sé qué está haciendo."

Y un estudiante preguntó: "Y esto está bien, o sea, ¿ya está entrenado bastante o no?"

Profesor: **"Sí, sí, estos son ejemplos de esto está en el tutorial de PyTorch. Acá de ahí - esa imagen salió de ahí."**

### La Pregunta Sobre Mirar al Futuro

Hubo una pregunta MUY importante que generó discusión:

Estudiante: "Pero no habíamos dicho como que no miraba el futuro, que no miraba lo siguiente, en este caso?"

Profesor: **"No, no mira el futuro del decoder, pero el encoder - eso va a pasar también en los transformers. Vos le pasas todo el hidden, o sea, el contexto de todo el encoder. Eso puede mirar todo esto, lo puede mirar todo tal cual."**

Aclaró algo crucial: **"Pero lo que no puede es - a la hora de predecir la siguiente palabra, no puede usar palabras del futuro en el entrenamiento del decoder."**

Y agregó: "En los Transformers la máscara de causalidad está puesta en el decoder, no en el encoder."

### ¿Entrenamiento o Inferencia?

Un estudiante preguntó: "Entonces acá estamos en tiempo de inferencia?"

Otro estudiante corrigió: "Un problema de traducción y no de generación. Lo de traducción, vos la palabra input la tenés toda. Entonces tenés derecho a mirarla toda."

Profesor: "Problema de generación como el prompt."

Explicaron la diferencia:
- **En traducción**: Tienes toda la frase de entrada, puedes mirarla completa
- **En generación de texto**: No tienes la frase completa, vas generando palabra por palabra

### ¿Cómo Se Formó Esta Matriz?

Un estudiante preguntó de dónde venían los valores.

Un estudiante pensó: "Es algo preestablecido, preentrenado."

Profesor: **"¿Qué cosa?"**

Estudiante: "Lo de la claridad de las palabras... ¿Cómo se armó esta matriz?"

Otro estudiante respondió: "De un entrenamiento."

Profesor: **"De un entrenamiento. Sí, sí, sí, tal cual."**

### Rango de Valores

Hubo una pregunta sobre el rango: "La tabla que va ahí va, ¿puede ser de cero a 1?"

Otro estudiante respondió: "Por el número el tamaño del vocabulario."

Profesor: **"Ah, sí, sí, de cero a uno. Siempre de cero a uno."**

Estudiante: "Sí, porque suman uno. Es una softmax."

Profesor: "Ah, de veras. Okay."

---

## Definición General de Attention

### El Paper "Attention Is All You Need"

El profesor hizo una transición: "Entonces vamos a hacer una pausita y seguimos con [el paper de Transformers]."

Después del recreo, continuó: "Entonces ya puede ser una segunda más tarde."

El profesor hizo un comentario muy honesto: **"Hay una habilidad que yo no tengo mucho que tiene cierta gente de expresar o de darle un sentido de la matemática. Yo - este texto me cuesta mucho más entenderlo que las fórmulas. Las fórmulas son objetivas. Y es lo que quiere decir cada cosa. Q es esto, P es esto, X es esto. Estoy haciendo este producto, me da esto."**

Pero luego dijo: **"De todas maneras, ahora en esta segunda que quiero dar como la definición general de lo que en realidad llamamos self-attention. En las primeras dos oraciones del paper de Vaswani, esas sí las pude traducir perfectamente a matemáticas."**

### La Primera Oración del Paper

El profesor leyó:

**"Una función de attention se puede describir como un mapping - como un mapping, o sea, algo que mapea - una query y un conjunto de pares key-value en un output."**

**"En donde la query y las keys y los values y el output son todos vectores."**

### La Formalización

El profesor escribió: "Hay un espacio de queries que se llama Q. Hay un espacio de keys que se llama K cursiva. Hay un espacio de valores que se llama V. Y hay un espacio de diccionarios key-values."

**"Y un mecanismo de attention es una función que agarra una query y un diccionario y me devuelve un value en el espacio de V."**

### Analogía del Diccionario de Traducción

**"Básicamente, piensen, imagínense - esto es la query - va a buscar en el diccionario. Y va a devolver el valor que corresponde."**

Dio un ejemplo concreto: **"Si esto fuera un diccionario tal cual, me dice - el diccionario, vamos a suponer de ahora en adelante que Q el espacio de queries es igual al espacio de keys... Si yo le doy el key que dice 'hola', el valor asociado de 'hello' me devuelve 'hello'."**

Eso sería un diccionario normal. Pero en attention:

**"Lo que pasa que como vimos en Bahdanau, en realidad va a ser un soft attention que me va a decir: 'lo más probable es que sea este, pero 80%, pero hay un 15% este y no sé cuánto por este otro'."**

### La Segunda Oración del Paper

El profesor continuó leyendo:

**"El output es calculado como una suma ponderada de los values, donde el peso asignado a cada value se calcula a partir de una función de compatibilidad entre la query y las correspondientes keys."**

Matemáticamente:
```
Output = Σᵢ αᵢ × Vᵢ

donde: αᵢ = función_compatibilidad(Q, Kᵢ)
```

El profesor explicó: **"Eso también está bueno porque me dice - el output es calculado como una suma ponderada. Eso es esto [señalando]. El output se calcula como una suma ponderada de valores. Acá tengo los valores ponderados por estos coeficientes."**

**"Donde el peso asignado a cada valor - este coeficiente alfa i - es calculado usando alguna función de compatibilidad, que es mi función alfa i, entre la query y las correspondientes keys."**

### ¿Cómo Se Mide la Compatibilidad?

El profesor explicó: **"Es mirar la query respecto a estas keys y mirar la ponderación para el i-ésimo valor."**

Dio otra analogía: "Si justo mi query es - si fuera un diccionario tal cual - y mi query es una de ellas [una de las keys], me va a devolver un alto peso cuando coincide con - cuando la query coincide con el key que corresponde."

**"Las funciones alfa calculan la compatibilidad entre el Q y la key."**

---

## Casos Extremos de Attention

### Caso 1: Indecisión Total

El profesor explicó: **"Hay un caso extremo que es... imagínense la indecisión total - da una query y esta colección de keys para mí son todos iguales. No tengo ni idea cuál es el valor que corresponde. No logré identificar una mejor key asociada a esa query."**

**Resultado**: Todos los αᵢ = 1/n

**"Ahí te daría toda la misma probabilidad."**

Un estudiante preguntó: "Todos esos elementos tienen la misma probabilidad, ¿qué significa?"

Profesor: **"Te está diciendo: mira, contribuyan todos un 1/n."**

Estudiante: "Es como no decir nada."

Profesor: "Sí, es como no decir nada."

Un estudiante preguntó: "¿Se engancha con la temperatura o todavía?"

Profesor: **"Sí, sí, se engancha con la temperatura."**

### Caso 2: Certeza Absoluta

El profesor explicó: **"Y el caso opuesto... Dame el más alineado de todos. Dame el que me maximiza la alineación. Es como proyectar - dame el que más, el que en esta distancia del coseno está más cerca."**

Un estudiante preguntó: "Ese, ¿por qué es extremo? No hace lo que yo quisiera."

Profesor: **"Es un caso extremo. No. No, vos querés un soft search que te devuelva... Este es un caso extremo: estoy recontra seguro que es este."**

Estudiante: "Tampoco te sirve."

Profesor: **"Porque lo único que te está diciendo es que el más influyente es ese, pero te estás perdiendo otros que pueden influir."**

Estudiante: "Sí. Vos querés ahí un intermedio."

Otro estudiante: "Lo que pasa pensando en traducción, capaz que hay unas palabras también."

Estudiante: "Claro, indicar no solo va a depender de una."

Profesor: "Claro, por ejemplo el sexo."

Estudiante: "O sea, capaz que en otras palabras."

Profesor: **"Exacto. Por eso vos no solo querés que dependa de una sola posición, sino que hay otras más que pueden influir."**

### Caso 3: Soft Attention (Lo Ideal)

**"Entonces algo intermedio sería agarrar la softmax de los productos escalares de cada query con cada key."**

Esto es lo que se usa en la práctica.

### Relación con Temperatura

El profesor explicó: **"Y los extremos anteriores se obtienen si yo en la softmax uso una temperatura que en el caso de temperatura cero se me concentra en el máximo y el caso de temperatura infinito mi indecisión total."**

---

## La Fórmula con Múltiples Queries

### Procesamiento en Paralelo

El profesor explicó: **"Si tenemos múltiples queries, si tenemos varias queries para hacer, simplemente lo que hacemos es considerar la secuencia de queries como un vector."**

**"Y la ventaja es que esto sí se puede escribir como un producto matricial."**

**Fórmula matricial**:
```
Attention(Q, K, V) = softmax(Q × K^T) × V
```

Donde:
- **Q**: Matriz con queries en las filas (m × dₖ)
- **K**: Matriz con keys en las filas (n × dₖ)
- **V**: Matriz con values en las filas (n × dᵥ)

### Cómo Funciona

El profesor explicó en detalle:

**"Entonces si yo los pongo a los Q en varias filas, puedo hacer el producto de varias queries a la vez."**

**"Y lo que me queda es una softmax de Q por K transpuesta - queda Q por K transpuesta multiplicado por la matriz de values."**

"Q es la matriz de queries, K es la matriz de keys y V es la matriz de values."

### El Producto Q × K^T

El profesor explicó qué hace este producto:

**"Esto lo único que les quería decir - cuando uno hace esto - es el Q transpuesta, es hacer los productos escalares de la query 1 con todas las keys, esa la primer fila. Después hacer los productos de la segunda query con cada una de las keys, así, etcétera, hasta la query m con cada una de las keys."**

**"Después uno hace softmax fila a fila."**

**"Y esto al multiplicarlo por V... se ve que la fila j de esa matriz, de esta matriz que es hacer esto, es justamente el attention de aplicar la query Qj."**

### El Consejo del Profesor

Luego dio un consejo importante: **"Entonces cuando ustedes hacen esta fórmula, lo que les queda es una matriz que cada fila es el attention de haber hecho la query correspondiente a cada una de las filas de Q."**

**"Es como que pueden hacer varias queries de una con un solo producto matricial."**

Pero agregó: **"Pero no se entreveren con esto de las matrices. Piensen en realidad - piensen en este diagrama. Yo creo que este diagrama es el que tienen que tener en mente."**

Se refería al diagrama simple de una query, un diccionario, y el output.

---

## Self-Attention

### La Transición

El profesor dijo: **"Esto fue attention general. Ahora vayamos a lo que sería el mecanismo de self-attention."**

"Les voy a leer, este es otro paper que está bastante bueno, que hace como un raconto histórico hasta ese momento sobre los distintos mecanismos de atención que hubo."

### Definición: Repaso de Bahdanau

El paper que leyó el profesor decía:

**"Originalmente Bahdanau describió la atención como el proceso de computar un vector de contexto para el siguiente paso del decoder que contiene la información más relevante de todos los hidden del encoder haciendo un promedio ponderado de esos hiddens."**

**"Cuánto cada uno de los hidden states contribuye a ese promedio ponderado se determina por un score de alineamiento entre el estado del encoder y el preview estado del encoder anterior."**

### Reinterpretación con Query, Key, Value

Luego el paper dice algo importante:

**"Ahora dice más en general, podemos considerar el estado del decoder como un vector query, y el hidden del encoder como un key-value al mismo tiempo. Entonces sería como un diccionario trivial en el que el key-value son lo mismo."**

El profesor explicó: **"Es el diccionario tonto. El diccionario que si yo le doy H1, el value es H1."**

**"Dice: el output es un promedio ponderado de esos vectores de valor, de los hidens, donde los pesos son determinados por una función de compatibilidad entre la query y las correspondientes [keys]."**

El profesor resumió: **"Básicamente este segundo párrafo describe lo que hacía Bahdanau usando esta terminología de queries y values."**

### ¿Qué es Self-Attention?

Ahora viene la definición clave:

**"El mecanismo de self-attention es el proceso de aplicar un mecanismo - el mecanismo de atención aplicado anteriormente - a cada punto de la secuencia."**

El profesor lo explicó más simple: **"A cada posición del input le vas a aplicar el mecanismo de attention. Es como si hicieras tantas queries como palabras tenés en el input."**

### Cómo Se Hace

**"Esto se hace creando tres vectores - Query, Key y Value - para cada posición de la secuencia, y después aplicando el mecanismo de atención para cada posición Xi usando Xi como vector query, como key-value para todas las otras posiciones."**

Un estudiante preguntó: "¿Incluido el mismo?"

Profesor: **"Incluido el mismo, sí."**

### El Output

**"Como resultado, da una secuencia X de input de palabras se transforma en una secuencia Yi - donde Yi - no piensen en este Y como el output del modelo, sino piénsenlo como el output de este self-attention - donde Yi incorpora la información de Xi además de cómo Xi se relaciona con todas las otras posiciones de X."**

### Cómo Se Crean los Vectores

**"Los query key value pueden ser creados aplicando proyecciones lineales."**

El profesor aclaró qué significa "proyectar": **"Esto de proyectar quiere decir multiplicar por una matriz que lo lleve a un espacio de dimensión más pequeño. Es aplicar capas lineales sin activación y sin bias."**

**"Es multiplicar por una matriz no más. Es como un MLP tonto - una sola capa densa sin activación y sin bias."**

---

## Implementación de Self-Attention

### El Diagrama con "Thinking Machines"

El profesor mostró un diagrama muy claro:

**"Imagínense que ustedes tienen un X1. Acá tengo la secuencia de entrada X1 hasta X3."**

**"Entonces X1 con ciertas proyecciones lineales, con tres proyecciones lineales distintas, se va a transformar en un Q1, en un K1 y en un V1. X2 lo mismo."**

### La Gracia: Pesos Compartidos

El profesor enfatizó algo crucial:

**"¿Cuál es la gracia? Que son los mismos pesos. Se comparten las mismas proyecciones. Es la misma matriz que están multiplicando."**

```
Q₁ = Wᵩ × X₁
K₁ = Wₖ × X₁
V₁ = Wᵥ × X₁

Q₂ = Wᵩ × X₂  (¡Misma Wᵩ!)
K₂ = Wₖ × X₂  (¡Misma Wₖ!)
V₂ = Wᵥ × X₂  (¡Misma Wᵥ!)
```

**"Entonces obtenemos para cada vector de entrada tres vectores: uno es el query, otro es el key."**

### El Proceso Completo

**Paso 1**: "Después armamos esta matriz que es Q por K transpuesta - es esta matriz que nos hace todos los productos escalares."

**Paso 2**: "Le aplicamos la softmax fila a fila. Obtenemos los coeficientes."

**Paso 3**: "Y entonces vamos a obtener, al multiplicar el vector V1 por estos coeficientes... cuando hacemos este producto, la fila i-ésima de ese producto va a ser la suma ponderada de los valores de j ponderados por [los weights]."

### Qué Representa

El profesor explicó el significado: **"Esto es el self-attention en un diagrama."**

**"Entonces en resumen, ¿qué es lo que ustedes tienen que sacar de self-attention? Que lo que hace es para cada X - esta matriz está haciendo todo el mundo con todo el mundo."**

**"Entonces cuando - para cada posición lo que va a ser es decirnos esta posición con qué otras posiciones se relaciona de forma más fuerte."**

Dio un ejemplo conceptual: **"Es como aquello de cuando decimos - no, pero antes habíamos hablado de esa persona, entonces ese pronombre se liga fuertemente con el nombre de esa persona. La idea es que aprenda esas relaciones estadísticas a partir del entrenamiento."**

### Lo Que Se Aprende

**"Lo que va a aprender acá - lo que voy a aprender es las matrices que me generan los Q, K, V en esta etapa."**

Es decir, las matrices **Wᵩ, Wₖ, y Wᵥ** son los parámetros entrenables.

---

## Scaled Dot-Product Attention

### El "Numerito Mágico"

El profesor mencionó: **"Lo único que les quiero decir es que en realidad no se hace solo el producto escalar, sino que se lo divide por un numerito mágico que es la raíz cuadrada de la dimensión de las keys."**

**Fórmula completa**:
```
Attention(Q, K, V) = softmax(Q × K^T / √dₖ) × V
```

### ¿Por Qué?

**"Y eso tiene que ver por cómo crece, por cuál es la tasa de crecimiento de estos productos escalares cuando uno aumenta."**

**"Es una estandarización que se hace para dar estabilidad numérica. O sea, no tiene significado de machine learning, digamos."**

**"Es para no tener problemas de cálculo numérico y que no se me saturen las softmax y ese tipo de cosas."**

### No Es Machine Learning

El profesor fue muy claro: **"Dividir entre ese número es para no tener problemas de cálculo numérico y que no se me sature la softmax."**

**"Probablemente cuando ustedes vean por ahí la ecuación de attention, la van a ver dividida por ese numerito. Pero ese numerito es un escalado que se hace para no tener problemas numéricos."**

---

## El Problema de la Invariancia por Permutaciones

### El Anuncio Importante

El profesor dijo con énfasis: **"Y lo último es esto que es importante. Va para parcial."**

### El Problema

**"Y es que este mecanismo de atención es completamente invariante al orden de la secuencia."**

**"Así que las redes de self-attention necesitan incorporar información posicional."**

### ¿Qué Significa "Invariante"?

El profesor explicó: **"Es decir, si yo cambio acá en este diagrama de self-attention - si yo cambio X2, intercambio X2 con X1, se me intercambian los Q, el Q también se intercambia, el V1 con el V2 también se intercambian. Y todo este producto matricial tiene sentido y me da exactamente lo mismo."**

Continuó: **"Todo se intercambia y cuando yo calculo la attention me da todo igual en diferente - en el orden que corresponde. Pero me sigue - me va a dar, ahora el X2, ahora el X1 va a estar acá, pero me va a decir que la attention de X1 respecto al X18 es el mismo que si hubiese estado en la primer posición."**

**"¿Se entiende? Entonces es invariante por permutaciones la attention."**

### Por Qué Es Un Problema

**"Y uno no quiere eso porque el texto tiene un orden."**

**"Entonces si yo altero el texto al azar, no puede ser que la attention me diga siempre lo mismo. Sería completamente inútil el mecanismo con esa propiedad."**

### La Solución

**"Entonces por eso se necesita poner alguna información posicional a los X para que el mecanismo deje de ser invariante por permutaciones."**

**"Y lo que se hace usualmente es - acá menciona tres formas. Una es agregar un - básicamente es agregar lo que se llama un positional encoding."**

---

## Positional Encoding en Detalle

### ¿Qué Es?

El profesor dijo: **"Que es una palabra medio pomposa para básicamente codificar la posición en la que está cada frase."**

**"Se codifica con una onda sinusoidal los cero, que tiene como frecuencia la posición en que está básicamente."**

### Formas de Hacerlo

El profesor mencionó: **"O también de forma más audaz, hay positional encodings que son aprendidos. Y hay otras cosas más generales, pero no voy a entrar en detalle muchas cosas."**

Pero enfatizó: **"Lo único que les voy a mencionar más adelante es el sinusoidal."**

### El Concepto Sinusoidal

**"La posición uno es una onda sola. Es una cuerda que va de extremo a extremo. La posición dos es una que tiene frecuencia doble, la posición tres es una que tiene frecuencia tres."**

### Visualización

El profesor mostró una imagen:

**"Acá hay una imagen. Acá tengo toda la matemática de lo que es. Acá... son 512. O sea, esta es la dimensión del embedding, o sea, son las coordenadas del embedding. Y esto que está acá es la posición de la palabra en la secuencia."**

**"O sea, esos son cada uno - cada fila es una palabra, un vector una palabra."**

Explicó las filas: **"Entonces es esto que está acá sería como la posición."**

### ¿Por Qué Ondas?

Un estudiante preguntó si no sería más simple ponerle un número.

Profesor: **"Es casi como poner una coordenada más que te diga en qué posición estaba."**

**"Lo que pasa que deben haber probado eso, no debe haber funcionado bien. Y este sí."**

Luego agregó: **"Por alguna razón hay algo matemático que te permite hacerlo más fácil con cosas que parecen más complejas que ponerle una etiqueta de en qué posición está."**

**"Sé que hay cosas que se llaman Fourier embeddings y que está relacionado con las ondas."**

### La Fórmula Matemática

**"Lo que hace el sinusoidal es... la coordenada par es con seno y la coordenada impar es con coseno."**

**"Entonces la posición es la posición en la que está la palabra. Entonces posición cero, ¿cuánto vale seno de cero? Vale cero. Y coseno de cero vale uno."**

**"Entonces para la primer palabra es 0, 1, 0, 1. Ese es el encoding. Ese es el positional encoding para la primer palabra."**

**"Para la segunda posición la formulita da algo así, en donde descubren la frecuencia."**

### Cómo Se Suma al Embedding

**"En el X1, o sea, en el embedding, vos le vas a sumar al embedding otra codificación que codifica la posición en la que está la palabra."**

```
Input final = Embedding(palabra) + Positional Encoding(posición)
```

### Ejemplo con Palabras Repetidas

Un estudiante dio un ejemplo importante: **"Si tuviera 'thinking machine thinking' de nuevo, X1 y X3 son distintos, ¿no?"**

Profesor: **"Claro, claro. X1 y X3 son distintos."**

Porque aunque la palabra sea la misma ("thinking"), el positional encoding hace que sean diferentes según su posición en la secuencia.

---

## El Tamaño del Embedding - Discusión Importante

### La Pregunta Original

Un estudiante preguntó: "El tamaño del embedding te lo da el tamaño de tus palabras, ¿no?"

### La Aclaración

Profesor: **"No, porque vos lo único que precisás es que el positional encoding - hay varias formas de hacer positional encoding - pero por ejemplo este de las ondas, por lo que le sumas una onda a este vectorcito. Y entonces lo único que precisas es que tenga la misma dimensión que este vectorcito, pero esa dimensión vos la elegís vos y ya está."**

### Es un Hiperparámetro

**"Pero lo que digo es es un hiperparámetro que vos elegís. Por ejemplo, el de Vaswani usaban 512, dimensión 512."**

### Recomendaciones

Un estudiante recordó: **"En taller nos habían recomendado usar la raíz cuadrada del vocabulario."**

Profesor: **"Ah, bueno, sí, sí, sí. No, no, pueden haber recomendaciones. Eso sí."**

**"Pero pero lo que digo es es un hiperparámetro que vos elegís."**

### El Trade-off

**"Vos deberías ser capaz de representar cualquier token."**

**"Hay una soft-relación en el que tu embedding tiene que tener suficientes dimensiones para representar todas las palabras que quiera y a la vez no debe ser demasiado grande porque si no te quedás super esparzo y estás gastando un montón de cómputo."**

### Discusión Sobre Entropía

Hubo una discusión interesante que se fue un poco por las ramas.

Un estudiante dijo: **"Pero casi eso es como una receta para tener problema. Porque si yo estoy repitiendo embedding para palabras que no tienen nada que ver porque no me da lugar."**

Profesor: **"Claro, no, por eso sí, pero ojo... los pesos van a dar. Seguro que si vos le ponés dimensión 500 va a estar bien."**

Luego se habló de entropía del lenguaje. Un estudiante mencionó: "Acabo de buscar por las dudas que me acordaba - más que era entropía. Un tema de ordenamiento."

Profesor: **"No, la entropía es como... Pero sí, sí, nos estamos yendo, nos estamos yendo."**

El profesor trató de explicar: **"Pensá en un lenguaje como una especie de árbol en el que vos vas concatenando palabras. Ese árbol tiene una entropía asociada... Vos lo que querés es en cierta forma encajar ese árbol en un espacio. Y si tu espacio no tiene la capacidad de abarcar ese desorden, no lo no lo vas a poner encajar, vas a colapsar cosas."**

Pero concluyó que no era esencial para el tema.

---

## Ejemplo Concreto de Self-Attention: "Thinking Machines"

### El Ejemplo Paso a Paso

El profesor mostró un ejemplo del blog que recomendó:

**"Imagínense que tienen estas palabras: thinking machines. Esta es la frase. X1, X2. Hacen el embedding, o sea, a partir de X1, X2 que son los embeddings - digamos que tenemos el positional encoding en el medio, pero si no tenemos, el funcionamiento es el mismo."**

### Generación de Q, K, V

**"Se generan tres vectores igualitos que son Q1, K1, V1 y Q2, K2, V2."**

### Cálculo para "Thinking"

**"Va a ser el producto de Q1 - para 'thinking' - va a ser el producto de Q1 para K1 y de Q1 con K2."**

Los números del ejemplo:
- Q₁ · K₁ = 112
- Q₁ · K₂ = 96

### Normalización

**"Eso da ciertos números. Los va a normalizar con el factor raíz de dk."**

Dividiendo por √64 = 8:
- 112/8 = 14
- 96/8 = 12

### Softmax

**"Pasa la softmax y me da 0.88 y 0.12."**

### Suma Ponderada

**"Y entonces el vector V1 va ponderado con 0.88 y el vector V2 va ponderado con 0.12. Se hace esa suma y este es el Z1."**

**"Este sería como el vector self-attention de contexto para la palabra 'thinking'."**

### Para "Machines"

**"Después se hace lo mismo para la palabra 'machines'. Se va a calcular Q2 con K1, Q2 con K2, se va a hacer la softmax, se divide en la raíz de no sé qué, se hace la softmax, etcétera."**

### Interpretación

**"El resultado es un vector contextual que depende de las demás palabras de la secuencia."**

**"El objetivo es determinar qué parte del input de la secuencia son más relevantes para generar cada palabra del output."**

---

## La Dependencia del Contexto

### El Problema de Palabras con Múltiples Significados

El profesor mostró un slide: **"Esto es como algo obvio, pero es esta dependencia del contexto de una palabra. ¿Cómo depende de su contexto?"**

Ejemplos:

**"date"**:
- **"go on a date"**: Cita romántica
- **"the date"**: La fecha

**"La palabra 'date' no tiene el mismo sentido en 'go on a date' y 'the date'."**

**"see"**:
- **"see you"**: Nos vemos
- **"see what you mean"**: Entiendo lo que dices

**"O 'see you' y 'see what you mean' es distinto."**

### La Solución

**"Se precisan representaciones sensibles al contexto y eso es lo que self-attention intenta abordar."**

**"Básicamente es como que te va a dar - ajusta lo que el modelo va a usar de cada palabra según el contexto."**

### Ejemplo Visual: "The train left the station"

El profesor mostró una matriz: **"Acá hay un ejemplito que es lo mismo, pero es self-attention. Por eso ven las mismas filas que la misma frase."**

**"Para cada palabra se calculan los scores de relevancia con todas las demás. Esos son products escalares. Los scores indican qué tan relacionadas están las palabras, se aplica la softmax, y se realiza una suma ponderada de los vectores y eso da una nueva representación contextual."**

El ejemplo mostraba que **"station"** presta atención a:
- **"train"** (relación fuerte)
- **"left"** (relación moderada)
- **"station"** (consigo misma)

### El Caso Interesante de Palabras Repetidas

Un estudiante notó algo importante: **"Lo más interesante ahí es que hay dos 'the', pero hay uno que claramente es el 'the' de la station y otro que es el 'the' de train."**

Profesor: **"Y ahí él se da cuenta de que hay un 'the' que es importante y el otro no."**

Estudiante: **"Ahí es donde debe usar el tema de la posición."**

Profesor: **"Sí, exacto, exactamente."**

---

## Analogía del Diccionario de Imágenes

### Un Ejemplo Brillante

El profesor usó una analogía muy clara: **"Esto de query, key, values es realmente - piénsenlo como buscar en un diccionario. Imagínense que ustedes tienen una query que es 'dogs on the beach'."**

### El Diccionario de Imágenes

**Keys y Values**:
- **Key 1**: "beach" → **Value 1**: [imagen de playa sola]
- **Key 2**: "beach, dog" → **Value 2**: [imagen de perros en la playa]
- **Key 3**: "dog" → **Value 3**: [imagen de perro solo]

### El Proceso

**"'Dogs on the beach' matchea solo 'beach'. Acá matchea dos, matchea 'beach' y 'dog'. Y acá matchea solo 'dog'."**

**"Entonces el attention va a ser más grande para esta imagen de acá [perros en la playa]."**

### Hard Attention vs Soft Attention

**"Entonces si estuviéramos haciendo una especie de argmax - una especie es lo que se llama hard attention - si estuviésemos una especie de argmax devolvería esta imagen."**

Pero en soft attention, devuelve una combinación ponderada de todas.

### Por Qué Esta Terminología

**"Y por eso se llaman, por eso es la terminología queries, keys and values."**

El profesor enfatizó: **"Acá son vectores que viven en el mismo espacio que nosotros especificamos cuál es la dimensión, ese es un parámetro que especificamos nosotros, pero después el modelo aprende cómo tiene que construir esos [vectores]."**

---

## Multi-Head Attention

### ¿Qué Es?

El profesor lo explicó directamente: **"El multi-head attention es lo mismo que el self-attention, solo que se hace varias veces. Esto parece misterioso, no sé qué, pero es hacer el self-attention 8 veces."**

### ¿Por Qué Múltiples Cabezas?

**"Porque de repente vieron como pasa como los MLPs, que yo que sé, esta neurona aprendió algo y esta otra aprendió otra cosa. Entonces cada attention de repente aprende cosas distintas, relaciones distintas."**

### Ejemplo con Traducción

El profesor mostró un ejemplo: **"El multi-head attention también ayuda a obtener representaciones que son más ricas."**

**"Por ejemplo acá en amarillo está el self-attention original. Y en rojo hay otra cabeza de attention, que es exactamente lo mismo, solo que con otras matrices aprende otra cosa."**

**"Puede estar diciéndome que 'traeré' refiere a 'la bolsa'."**

### Cómo Funciona Técnicamente

Un estudiante preguntó: **"Lo anterior son los pesos de las matrices?"**

Profesor: **"Claro, cambian las matrices. Sí, lo único."**

Explicó: **"O sea, vos lo que hacés es decís: 'Tengo un self-attention que se llama self-attention 1.' Esa tiene sus matrices. El self-attention 2 tiene sus matrices. El self-attention 3 es la suya. Y así haces cuántas quieres y eso se llama multi-head attention."**

### Combinación

**"Y después lo que haces es concatenar todos los resultados."**

**"Entonces es como que tenés - todas las diferentes relaciones."**

El profesor dio un ejemplo conceptual: **"Por ejemplo acá, esto sería ideal que - no sé, esto es medio ficticio, pero es como que 'traeré' no solo no solo podría ser tipo hay print, sino que también es refiero a [otra cosa]."**

---

## De Attention a Transformers

### El Gran Descubrimiento

El profesor explicó la transición: **"Básicamente el transformer, por eso el paper se llama 'attention is all you need', en el sentido de que vos no precisas una recurrencia sobre el tiempo."**

**"Podés procesar todo en paralelo, toda la secuencia."**

### Por Qué Es Revolucionario

**"Eso le da una rapidez enorme en comparación a la recurrente. Una eficiencia de cómputo en comparación a la recurrente que tiene que ir - tiene que procesar todo el encoder paso a paso y después el decoder también."**

**"Acá procesa la secuencia [completa en paralelo]."**

### El Descubrimiento Clave

**"En ese paper descubren que el mecanismo de self-attention puede reemplazar a la unidad recurrente en el seq2seq."**

**"Y eso es bastante interesante."**

### El Impacto

**"Su gran impacto fue la escalabilidad. Fue una revolución. Son la base de la revolución de hoy por hoy, de los modelos de lenguaje."**

**"Fueron generalizados y usados en visión, en audio y muchas otras áreas más."**

### Aplicaciones Mencionadas

**Vision Transformers**: Un estudiante mencionó aplicaciones en videojuegos:

**"Para imágenes, por ejemplo... Se usa en DLSS [tecnología de NVIDIA]. Se usa para generar frames de los juegos."**

**"Las tarjetas de video usan eso adentro. Ahora calcula muchos imágenes y las rellena con esas imágenes. Hace un upscaling."**

Otro estudiante agregó: **"Te genera fotogramas en medio entre fotograma real y fotograma real. Entonces parece que tira más."**

El profesor comentó: **"Mira, tira más, pero ha generado el tiempo frame. Además aumenta la cantidad de frames."**

Un estudiante mencionó un problema: **"Yo escuchaba que había pila de jugadores que se quejaban, que no podían influir en algún frame y lo veían y no podían mover el bicho."**

---

## La Arquitectura Transformer Completa

### Introducción a la Arquitectura

El profesor mostró el diagrama clásico del paper:

**"Entonces los Transformers - tengo mi dibujito acá. La arquitectura del transformer es igual que tiene un encoder, que es esto, y tiene un decoder, que es esto que está acá. Y después tiene como antes una parte lineal para hacer la predicción de probabilidades, igual que siempre."**

### Inputs y Embeddings

**"Los inputs acá son la frase, por ejemplo, en francés. Se hace - cada frase se le hace un embedding, perdón, a cada palabra se le hace un embedding."**

**"Después se le agrega un - vieron que hay una onda dibujada acá - se le hace un positional encoding, para marcar la posición."**

El profesor recordó: **"Que la verdad conceptualmente, piénsenlo, como eso de poner una etiqueta."**

### El Encoder - Estructura Detallada

**"En el encoder - y después, bueno, eso lo mismo se hace con el output, que es la frase en inglés. Y eso va a pasar por un multi-head self-attention. Esa es la primer parte."**

El profesor describió la estructura:

**"Acá que dice multi-head attention es un multi-head self-attention."**

**"Y lo que hace es descubrir las relaciones de cada palabra con la frase."**

Luego explicó el bloque completo:

**"Tengo un multi-head self-attention. Esto del más máscara de padding es cuando uno hace las cosas con batch, pero son para mí conceptualmente por fuera de la arquitectura."**

**Componentes del bloque de encoder**:

1. **Multi-Head Self-Attention**

2. **Add & Norm**: **"Hay hay una residual connection acá, una conexión residual, o sea, a la salida de la attention se le suma lo que venía acá."**

3. **Feed-Forward Network**: **"Se pasa a una feed-forward que en realidad en la versión original es simplemente un MLP de dos capas."**

4. **Add & Norm**: **"También hay una skip connection con la salida final de esto, perdón, una residual connection con la salida final. Y eso produce la salida deseada del encoder."**

### El Decoder - Estructura Detallada

**"En el decoder se entra también acá - en el multi-head attention..."**

Un estudiante preguntó: **"Esta es la del encoder?"**

Profesor: **"No, no, no. La primera entrada del decoder es, por ejemplo, acá es la frase en francés y acá es la frase en inglés a la hora de entrenar."**

Un estudiante confirmó: **"Sí, sí."**

**Componentes del bloque de decoder**:

El profesor explicó que tiene una estructura similar pero con diferencias clave:

1. **Masked Multi-Head Self-Attention**

2. **Add & Norm**

3. **Multi-Head Attention** (encoder-decoder)

4. **Add & Norm**

5. **Feed-Forward Network**

6. **Add & Norm**

7. **Linear + Softmax**

### La Máscara de Causalidad - MUY IMPORTANTE

El profesor explicó: **"Vieron que la diferencia que dice 'mask' - o sea, que está masqueado."**

**"No queremos - no me está dando el tiempo para ir a los detalles, pero es decir, no queremos... ahí lo que va a hacer es va a mirar cada palabra, va a hacer su self-attention con las palabras anteriores, pero no con todo el paquete."**

Aclaró la diferencia con el encoder:

**"En el encoder eso no es problema porque la frase en francés siempre está dada. Entonces podemos hacer todo el mundo con todo el mundo."**

**"Pero a la hora de ir de hacer generación, se - no puede saberse el futuro. No se puede comparar con el futuro."**

**"De vuelta, no miramos para [adelante]."**

### Máscara Incluso en Entrenamiento

Un estudiante preguntó algo importante: **"¿Aunque esté aprendiendo?"**

Profesor: **"Aunque esté aprendiendo. Sí. Exacto."**

### La Attention Encoder-Decoder

**"Entonces acá se le agrega una máscara para que el self-attention se apague y le ponga ceros a todo lo que está del tiempo en el que él está en adelante."**

**"Y después se hace un attention al estilo como hacíamos en Bahdanau entre lo que sale de acá y lo que salió del encoder. Se hace un attention común entre esas cosas."**

**"Y eso después hay connections por todos lados y eso después se pasa a una feed-forward más residual connection, normalizaciones, una lineal, softmax."**

### Múltiples Capas

**"Los distintos modelos de lenguaje usan Transformers con distintas cantidad de bloques en el encoder y en el decoder."**

**"Pueden hacerlo como que es un solo encoder y un decoder o varias capas, varios bloques de encoders y varios bloques de decoders."**

Un estudiante comparó: **"Como los layers de la recurrente."**

Profesor: **"Como los layers de la recurrente. Tal cual. Igualito."**

---

## Entrenamiento vs Inferencia en Transformers

### Durante el Entrenamiento

El profesor explicó las diferencias:

**En el Encoder**:

**"La gran ventaja es que a la hora de entrenar podés pasar toda la frase, sobre todo en el encoder."**

**"Vas a hacerlo en los dos, pero sobre todo en el encoder donde... la estructura es: hay un multi-head self-attention en el encoder."**

**En el Decoder**:

Un estudiante preguntó: **"¿También le pasan todas las frases?"**

Profesor: **"Ah, en el encoder. Sí, en el encoder, sí."**

Alguien resumió: **"Como etapas iniciales pasan en paralelo."**

Profesor: **"Claro. Sí, solo hasta acá que preciso [el encoder]."**

### Durante la Inferencia

Un estudiante preguntó: **"¿En inferencia qué hago? Empiezo poniendo el [token inicial]?"**

Otro estudiante respondió: **"El encoder que es igual. O sea, lo que al principio entra nada o puede ser una [señal]."**

Profesor: **"Pero solo por el decoder, ¿verdad?"**

Estudiante: **"Sí, solo por el decoder. El encoder lo corres una vez por el input que tengas y sale de todo."**

### El Decoder en Inferencia

**"Y después el decoder lo que va a hacer es para cada una de las probabilidades vas a agarrar una palabra y la vas a volver a [meter]."**

Un estudiante dijo: **"Hace como una recurrente."**

Profesor: **"Sí, ahí no tiene otra que generar palabra por palabra."**

**"Ahí le queda otra que ir una porque la salida acá es la entrada."**

### Sobre la Velocidad

Un estudiante comentó: **"Pero ahí no hay problema porque el conjunto no se diferente."**

Otro: **"Pero pero ahí yo no estoy aprendiendo mucho."**

Profesor: **"Ahí no estás aprendiendo. Pero igual pequeños segundos hacen que vos veas que ya te escribe como un taponazo o perfecto."**

**"Pero en comparación a la demora de entrenar, no va."**

**"O sea, la gran la gran ventaja es que a la hora de entrenar vos puedes pasar toda la frase, sobre todo en el encoder."**

---

## Layer Normalization

### ¿Qué Es?

El profesor dijo: **"Layer normalization. Es eso, se lo muestro acá bien rápido porque es una capa bien sencilla."**

**"Imagínense un vectorcito U, que es una secuencia de - perdón, es una capa que tiene como entrada un vector."**

### El Proceso

**Paso 1**: **"Y lo que hace es normaliza a lo largo de las coordenadas de ese vector, no como en el batch normalization que se normalizaba a lo largo del batch."**

**Paso 2**: **"Le va a restar la media del vector, va a dividir entre el desvío del vector."**

**Paso 3**: **"Eso va a dar un vectorcito, un sombrerito."**

**Paso 4**: **"Y después lo que se hace es se lo reescala de nuevo, se lo multiplica por un gamma y se le suma un beta como se hacía en batch normalization."**

### Parámetros

**"Y este gamma y este beta son aprendibles."**

### Diferencia con Batch Normalization

**"Se hace secuencia a secuencia. Es lo que - no se hace a batch por batch, sino que se hace por palabrita."**

**"Y si tenemos una matriz de muchas palabras, se aplica simplemente word a word, o sea, a cada palabra."**

### Qué Vectores Normaliza

**"Este vector va a representar el embedding de una palabra, por ejemplo, o el self-attention de ese vector con todos los demás."**

---

## Residual Connections (Skip Connections)

### Qué Son

El profesor las mencionó varias veces:

**"Aparece una residual connection acá, o sea, a la salida de la attention se le suma lo que venía acá."**

**Fórmula general**:
```
Output = SubLayer(X) + X
```

Luego se aplica Layer Normalization.

### Dónde Aparecen

En cada bloque del Transformer hay dos residual connections:
1. Alrededor de la capa de attention
2. Alrededor de la feed-forward network

**"Hay una skip connection con la salida final de esto, perdón, una residual connection con la salida final."**

### Importancia para el Parcial

El profesor mencionó al final: **"Skip connection fue lo que no quedó para el primero [parcial]."**

Esto significa que es un tema importante que entra en este parcial.

---

## Feed-Forward Network

### ¿Qué Es?

**"En la versión original es simplemente un MLP de dos capas."**

**"Acá dice dos capas densas porque eso es original. Es así."**

### Estructura

Es una red feed-forward simple con:
- Una capa lineal
- Activación (generalmente ReLU)
- Otra capa lineal

### Características

**"Lo único que digo es que la salida tiene - se hace que de tal forma que la salida tenga la misma dimensión que la entrada, cosa de poder hacer esto n veces."**

Esto permite apilar múltiples bloques de encoder o decoder sin cambiar las dimensiones.

---

## Matrices Compartidas - Punto Clave

### La Importancia

El profesor enfatizó varias veces: **"Lo único bueno es que es la misma matriz siempre. Son las mismas matrices siempre."**

### La Ventaja Principal

**"Y eso permite algo muy importante. Que como es la misma matriz que se aplica de forma independiente a cada palabra, es que el transformer pueda procesar palabras de secuencias de cualquier longitud sin crecer."**

**"Sin crecer. Es la misma matriz. Siempre es la misma matriz."**

### Ejemplo Práctico

**"Si yo fijo el tamaño del embedding, ya está. Ya fijé la matriz."**

**"Y puedo - acá puedo poner una palabra de longitud dos o una palabra de longitud 17. Va a procesarla igual."**

**"Lo único bueno es que puede procesar toda a la vez porque todo esto es en paralelo."**

### Sin Recurrencia

**"No tiene que hacer 'thinking', después 'machines', después no sé qué, después no sé qué. Hace todo en paralelo."**

---

## Por Qué Query, Key y Value (No 2 o 7)

### La Pregunta

Un estudiante preguntó: **"¿Por qué son 3 y no 2 o 7?"**

Otro agregó: **"¿Por qué no seis?"**

### La Respuesta del Profesor

**"Query, key, value tiene un sentido semántico."**

### Analogía de la Biblioteca

**"Yo hago una query en un [diccionario], es como que voy a la biblioteca y pido por un libro tal. Van y lo van a buscar."**

**"O sea, preciso el libro que quiero, la dirección y el libro. O sea, preciso tres cosas."**

**"¿Qué podrías hacer con seis que no [puedas con tres]?"**

### Analogía del Catálogo

**"Es como buscar en un catálogo. Yo tengo un catálogo de fotos. Hago una query sobre ese catálogo. Las keys es el caption de cada foto. Y voy a tratar de matchear mi query con cada caption y ver qué caption es el que más ajusta para devolverme el value que es la foto."**

**"Preciso solo esas tres cosas."**

### Componentes Adicionales

Un estudiante mencionó: **"Igual después internamente me pasa que tenés otras cosas - el estante, la estantería en el que está, la posición del elemento. Internamente para la red..."**

Profesor: **"O sea, como las matrices de peso. O sea, son componentes que en su conjunto arman el sistema para poder armar."**

### El Positional Encoding

**"El positional encoding es importante porque es lo que nos va a dar el orden, o sea, es lo que nos va a dar que no sea invariante por permutaciones."**

---

## La Magia del Aprendizaje

### Lo Que Se Aprende

El profesor enfatizó: **"Aprende cuáles son las matrices."**

**"Aprende cómo tiene que codificar X en una query, cómo tiene que codificarlo en un key cuando lo quieren buscar a él."**

**"Cuál es la query que tiene que hacer cuando quiero buscar por él, cuál es el key cuando buscan - cuando piden por él, y cuál es el valor que tiene que devolver cuando buscan por él."**

### El Mapeo

Un estudiante dijo: **"Está el mapeo."**

Profesor: **"Ahí va. Eso, eso todo es aprendido. Es como mágico."**

El modelo aprende las matrices de transformación (Wq, Wk, Wv) que convierten cada palabra en sus representaciones de query, key y value.

---

## Recursos Recomendados por el Profesor

### El Blog "The Illustrated Transformer"

El profesor lo mencionó varias veces:

**"Les voy a mostrar - esto - si ustedes entran al link, yo acá les puse - no sé si les puse. Ah, no, en la siguiente día. Les puse el link de donde saqué esta imagen."**

**"Que es un blog también que está muy bueno que explica toda esta arquitectura de Transformers con dibujitos y con fórmulas."**

**"Está muy lindo este blog. Les va mostrando cómo se va haciendo todo cada uno a uno."**

### Tutorial de PyTorch

**"Acá de ahí - esa acá hay otro, pero es lo mismo. Estos todos los saqué de ahí de ese tutorial [de PyTorch sobre seq2seq con attention]."**

**"Está el código."**

Preguntó a los estudiantes: **"Ya hicieron la entrega de esto ustedes."**

Y recomendó: **"Si no lo han visto, mírenlo porque está bueno, está hecho con código. O sea, creo que todas estas formulitas si les cuesta entender es más fácil mirar código ahí está el código."**

### Los Papers Originales

**1. Bahdanau et al.**:
- El paper que introdujo Attention
- Tiene a Yoshua Bengio (Premio Turing) entre los autores
- El profesor siguió principalmente este paper en la primera parte de la clase

**2. Vaswani et al.** - "Attention is All You Need":
- Los autores son: Vaswani, Parmar, Cor, Jones, Gómez, Kaiser, Polosukhin
- **"Es uno de los más citados de la historia"**
- Introdujo los Transformers

**3. Un paper de revisión histórica**:
- El profesor mencionó que hay "otro paper que está bastante bueno, que hace como un raconto histórico hasta ese momento sobre los distintos mecanismos de atención que hubo"

---

## Para el Parcial - LO QUE ENTRA

### La Confirmación Explícita

Al final de la clase, un estudiante preguntó:

Estudiante: **"Eh, si de este lunes al próximo es el parcial. Yo pensaba que la próxima íbamos a hacer ejercicio."**

Profesor: **"Sí, sí, sí, vamos a hacer ejercicio."**

Estudiante: **"¿Y qué es lo que entraría ahí en el parcial?"**

Profesor: **"Desde Skip Connections en adelante."**

Estudiante: **"Skip connection en adelante. Okay."**

Profesor: **"Sí. Skip connection fue lo que no quedó para el primero."**

### Lista Completa de Temas

Basándome en todo lo que el profesor cubrió y enfatizó, los temas son:

1. **Skip Connections / Residual Connections**
   - Qué son
   - Dónde se usan en el Transformer

2. **Layer Normalization**
   - Cómo funciona
   - Diferencia con Batch Normalization

3. **Mecanismo de Attention (Bahdanau)**
   - El problema del vector de contexto fijo
   - Cómo se construye Cᵢ (contexto variable)
   - Scores de alineación eᵢⱼ
   - Pesos αᵢⱼ (softmax de los scores)
   - Attention aditiva (tanh de Ws×Si-1 + Wh×Hj)

4. **Query, Key, Value**
   - Qué representa cada uno
   - Analogía del diccionario
   - Por qué son tres

5. **Self-Attention**
   - Qué es (cada palabra mira a todas las demás)
   - Cómo se generan Q, K, V (proyecciones lineales)
   - El producto Q × K^T
   - La suma ponderada con V
   - El diccionario trivial (K y V son lo mismo)

6. **Scaled Dot-Product Attention**
   - División por √dₖ
   - Por qué se hace (estabilidad numérica)

7. **Positional Encoding** ← MUY IMPORTANTE
   - **Por qué es necesario** (invariancia por permutaciones)
   - El problema si no lo usamos
   - Cómo funciona (ondas sinusoidales)
   - Por qué no simplemente un número

8. **Multi-Head Attention**
   - Por qué múltiples cabezas
   - Qué captura cada cabeza
   - Cómo se combinan (concatenación)

9. **Arquitectura del Transformer**
   - Estructura del Encoder (Multi-Head Self-Attention + FFN)
   - Estructura del Decoder (Masked Self-Attention + Encoder-Decoder Attention + FFN)
   - Las tres capas de attention diferentes

10. **Máscara de Causalidad**
    - Dónde se aplica (solo en el decoder)
    - Por qué es necesaria (no mirar al futuro)
    - Por qué el encoder no la necesita

11. **Diferencias entre Entrenamiento e Inferencia**
    - En entrenamiento: Paralelización (con teacher forcing)
    - En inferencia: Secuencial en el decoder

12. **Feed-Forward Networks**
    - Estructura (MLP de 2 capas)
    - Dónde aparecen

### Temas Especialmente Enfatizados

El profesor dijo **"Va para parcial"** sobre:
- **La invariancia por permutaciones** y por qué necesitamos positional encoding
- **Skip connections** (porque no entraron en el primer parcial)

---

## Resumen Ultra-Simplificado

### El Viaje Completo: De RNN a Transformers

**Paso 1: Seq2Seq Clásico (Antes de Attention)**:
- Comprimes toda la frase en UN vector C fijo
- Usas ese mismo C para generar cada palabra de salida
- **Problema**: Pierdes información, especialmente en frases largas

**Paso 2: Attention de Bahdanau**:
- Para cada palabra que vas a generar, miras TODO el input de nuevo
- Decides a qué partes prestarle más atención
- Cada palabra tiene su propio contexto Cᵢ
- **Ventaja**: No pierdes información
- **Limitación**: Aún usa redes recurrentes (lento)

**Paso 3: Transformers (Vaswani)**:
- Eliminas las redes recurrentes completamente
- SOLO usas attention (multi-head self-attention)
- Procesas todo en paralelo
- Agregas positional encoding para el orden
- **Resultado**: Mucho más rápido, escalable

### La Analogía Final del Diccionario

Imagina que tienes esta pregunta: **"Busco información sobre perros en la playa"**

**Diccionario normal**:
- Buscas "perros" → obtienes info sobre perros
- O buscas "playa" → obtienes info sobre playas
- Tienes que elegir UNO

**Attention (Diccionario inteligente)**:
- Buscas con tu query completa: "perros en la playa"
- El diccionario tiene keys: ["playa", "playa + perros", "perros"]
- Matchea con cada uno:
  - "playa": 15% match
  - "playa + perros": 80% match ← ¡Mejor match!
  - "perros": 5% match
- Te devuelve: 0.15 × [info playas] + 0.80 × [info perros en playas] + 0.05 × [info perros]
- **Resultado**: Una respuesta contextualizada que combina lo mejor de cada fuente

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
- Usa ondas sinusoidales (no un simple número)
- Ahora la posición 1 ≠ posición 2, aunque sea la misma palabra

---

## Consejos del Profesor

### Sobre Entender vs Memorizar

El profesor fue muy honesto: **"No quiero matarlos. Quiero que entiendan cómo funciona."**

Y también dijo: **"Este texto me cuesta mucho más entenderlo que las fórmulas. Las fórmulas son objetivas."**

### Sobre Recursos

**"Si no lo han visto [el tutorial de PyTorch], mírenlo porque está bueno, está hecho con código. Si les cuesta entender [las fórmulas] es más fácil mirar código ahí está el código."**

### Sobre los Detalles

Cuando explicaba algo muy técnico, a veces decía: **"No se preocupen por el detalle."**

O cuando iba a profundizar mucho: **"No me está dando el tiempo para ir a los detalles."**

Esto indica que **entiende los conceptos generales** es más importante que memorizar cada fórmula.

### Sobre las Matrices

**"Pero no se entreveren con esto de las matrices. Piensen en realidad - piensen en este diagrama."**

Se refería a pensar conceptualmente en query, diccionario, output, en lugar de perderse en los productos matriciales.

---

## Notas Finales

### El Estilo de la Clase

La clase fue muy interactiva:
- El profesor valoraba las preguntas ("está bien la pregunta", "perfecto")
- Admitía cuando algo era complicado ("esto es medio abstracto")
- Repetía explicaciones de diferentes formas hasta que quedara claro
- Usaba muchas analogías (biblioteca, catálogo de fotos, etc.)

### Lo Más Importante

El profesor terminó diciendo: **"Voy a ver si la clase que viene capaz redondea un poquito el tema, pero tampoco quiero matarlos. Quiero que entiendan cómo funciona."**

Y sobre la próxima clase: **"Vamos a hacer ejercicio."**

### Para Estudiar

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
