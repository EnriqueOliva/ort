# Explicación de Temas - Clase del 02-09-2025

## La Gran Pregunta: ¿Por Qué Estamos Aquí?

Esta clase es un punto de inflexión en el curso. Hasta ahora, en otras materias como Deep Learning y Machine Learning, aprendiste a **clasificar**: dado un dato, ¿a qué categoría pertenece? Ahora vamos a dar vuelta el problema: **¿cómo generamos datos nuevos que se parezcan a los reales?**

El profesor lo dijo claramente:

> "Es una materia que tiene un poquito de otra cabeza. Vamos a usar las herramientas que están viendo en otras materias, pero las vamos a usar un poquito distintas."

Esa "cabeza distinta" es el corazón de la Inteligencia Artificial Generativa.

---

## El Cambio de Perspectiva Fundamental

### Antes (Clasificación):
1. Tienes un dato X (por ejemplo, una imagen de un paciente)
2. Lo pasas por un perceptrón
3. Te da un valor como 0.7
4. Dices: "0.7 > 0.5, entonces tiene la patología"
5. **Emites un veredicto**

### Ahora (Generación):
1. Tienes un perceptrón entrenado
2. Te da un valor como 0.7
3. Ese 0.7 **es el parámetro θ de una distribución de Bernoulli**
4. **Muestreras de esa distribución** para generar un dato nuevo
5. **Creas algo que no existía**

Como explicó el profesor: "En realidad podrías usarlo para generar datos verosímiles de pacientes y sus diagnósticos". La misma herramienta (el perceptrón), usado de manera diferente.

### ¿Qué Significa "Muestrear de una Distribución"?

Este concepto es fundamental y vale la pena entenderlo bien.

#### La Analogía de la Moneda Cargada

Imagina que tienes una moneda, pero no es justa: está "cargada" para que caiga cara el 70% de las veces y cruz el 30%.

**Muestrear** de esta moneda significa simplemente **tirarla y ver qué sale**.

- Si la tiras una vez, te sale cara o cruz (un "muestreo")
- Si la tiras 1000 veces, aproximadamente 700 serán cara y 300 cruz
- Cada tirada es **aleatoria**, pero las probabilidades están definidas

La **distribución** es la descripción de las probabilidades: "70% cara, 30% cruz". El **parámetro** θ = 0.7 es lo que define esa distribución.

#### El Proceso Paso a Paso

Cuando el perceptrón te da θ = 0.7, lo que haces es:

1. **Generas un número aleatorio** entre 0 y 1 (la computadora hace esto)
   - Digamos que sale 0.45

2. **Comparas con θ**:
   - Si el número aleatorio < θ (0.45 < 0.7) → el resultado es 1 (cara, sí, blanco, tiene patología...)
   - Si el número aleatorio ≥ θ → el resultado es 0 (cruz, no, negro, no tiene patología...)

3. **El resultado es tu dato generado**

En código sería algo tan simple como:
```
numero_aleatorio = random()  # genera algo como 0.45
dato_generado = 1 if numero_aleatorio < theta else 0
```

#### ¿Por Qué No Simplemente Usar 0.7 Directamente?

Pregunta natural: si el perceptrón dice 0.7, ¿por qué no decir "el resultado es 0.7" y listo?

Porque **0.7 no es un dato válido**. Si estamos generando píxeles de una imagen blanco y negro, el píxel tiene que ser 0 (negro) o 1 (blanco). No puede ser 0.7.

El 0.7 te dice **qué tan probable** es que sea 1. Pero para generar, necesitas **decidir**: ¿es 1 o es 0? Y esa decisión la tomas con el muestreo.

#### El Resultado: Variedad con Estructura

Lo mágico del muestreo es que introduce **variedad controlada**:

- Si generas 100 datos con θ = 0.7, no vas a obtener 100 unos
- Vas a obtener aproximadamente 70 unos y 30 ceros
- Cada vez que generes, el resultado puede ser diferente
- Pero en promedio, la estructura (70/30) se mantiene

Esto es exactamente lo que queremos en IA Generativa: **crear cosas nuevas que se parezcan a las originales, pero que no sean idénticas**.

#### Extensión a Distribuciones Continuas

Para una distribución **gaussiana** (la campana), el proceso es similar pero en lugar de decidir entre 0 y 1, generas cualquier número real:

1. La distribución tiene parámetros μ (media) y σ (desviación estándar)
2. El muestreo genera un número que probablemente esté cerca de μ
3. Cuanto más lejos de μ, menos probable (pero posible)

Por ejemplo, si μ = 5kg y σ = 0.5kg para el peso de gatos hembra:
- Muestrear podría darte: 4.8kg, 5.2kg, 4.6kg, 5.1kg...
- Raramente te daría 3kg o 7kg (muy lejos de la media)
- Cada muestreo es diferente, pero todos "tienen sentido" como pesos de gatos hembra

---

## Las Reglas Fundamentales: ¿Por Qué las Repasamos?

El profesor empezó repasando dos reglas de probabilidad. No fue un repaso aleatorio: estas reglas son las **herramientas matemáticas** que necesitamos para todo lo que viene.

### La Regla de la Suma (Marginalización)

**P(X = x) = Σ P(X = x, Y = yi)**

¿Para qué sirve? Para "borrar" una variable que no nos interesa. Si quiero saber la probabilidad de que un gato pese 5kg, pero el peso depende del sexo, sumo las probabilidades para machos y hembras.

### La Regla del Producto

**P(X, Y) = P(X) × P(Y|X)**

¿Para qué sirve? Para descomponer una probabilidad conjunta (dos cosas pasando juntas) en probabilidades más simples. **Esta regla es la base de los modelos autoregresivos** que veremos más adelante.

### La Conexión con Esperanzas

Combinando ambas reglas:

**P(X) = Esperanza sobre Y de [P(X|Y)]**

El profesor lo explicó con un ejemplo: si tienes objetos (auto, camioneta, avión) y quieres saber la probabilidad de que algo sea un auto, puedes hacerlo promediando sobre los colores. Esto parece abstracto ahora, pero es exactamente lo que usaremos para las **mixturas de gaussianas**.

---

## Variables Aleatorias Continuas: El Salto al Mundo Real

### ¿Por Qué Necesitamos Esto?

Hasta ahora trabajamos con variables **discretas**: sí/no, categorías, valores separados. Pero el mundo real tiene:
- Pesos de gatos (cualquier valor entre 2kg y 10kg)
- Longitudes de pétalos de flores (4.3cm, 5.7cm, 6.234cm...)
- Intensidades de píxeles (0.0 a 1.0)

Como dijo el profesor: "Dejo de tener valores uno-cero, evento sucede o no sucede, y paso a tener espacios continuos".

### Tres Familias de Distribuciones

El profesor presentó tres distribuciones, pero fue honesto:

> "Vamos a usar más que nada gaussianas. Pero necesitan conocer estas familias para entender los conceptos."

#### 1. Distribución Uniforme
- **Forma**: Una línea recta paralela al eje X entre A y B
- **Significado**: Todos los valores entre A y B son igualmente probables
- **Ejemplo**: Un sorteo completamente justo
- **Parámetros**: A y B (los límites)

#### 2. Distribución Normal (Gaussiana)
- **Forma**: La famosa campana
- **Significado**: Los valores se concentran alrededor de la media, con menos valores en los extremos
- **Parámetros**: μ (media, el centro) y σ (desviación estándar, qué tan ancha es)
- **Importancia**: Es la que más vamos a usar en el curso

#### 3. Distribución Laplaciana
- **Forma**: Como una campana pero con un pico más agudo en el centro
- **Parámetros**: μ (media) y b (concentración)

**Regla fundamental**: En todas las distribuciones continuas, el área bajo la curva siempre suma 1.

---

## El Momento Clave: Perceptrones = Estimadores de Parámetros

Aquí el profesor conectó todo con lo que ya sabías de Deep Learning. Esta es **la idea central del curso**:

> "Cuando un perceptrón te da un valor como 0.7, ese valor ES un parámetro de una distribución."

### Lo que Esto Significa

Cuando entrenas un perceptrón para clasificar patologías:
- Le pasas datos de un paciente
- Te da 0.7
- En clasificación, dices "tiene la patología" (porque 0.7 > 0.5)

Pero en realidad, ese 0.7 es **θ, el parámetro de una Bernoulli**. El perceptrón está diciendo: "La probabilidad de que tenga la patología, dado estos datos, es 0.7".

### La Distinción Importante de Parámetros

El profesor fue muy cuidadoso aquí:

- **Parámetros de la distribución** (μ, σ, θ): Definen la forma de la distribución. Son lo que queremos **estimar**.
- **Parámetros de la red** (W, B): Los pesos que se entrenan con gradiente descendente. Son los que **ajustamos** para estimar los primeros.

> "Cuando entrenemos no vamos a tocar esos valores [μ, σ, θ]. Vamos a tener modelos que van a inferir estos parámetros."

---

## Mixtura de Gaussianas: Cuando la Realidad es Compleja

### El Ejemplo de los Gatos

El profesor usó un ejemplo perfecto para explicar por qué necesitamos mixturas:

**Variables**:
- **Y**: El sexo del gato (macho/hembra) - variable discreta
- **X**: El peso del gato - variable continua

**El modelo**:
- Y se distribuye como Bernoulli (aproximadamente 50/50)
- X dado Y=macho se distribuye como una Gaussiana con μ_macho y σ_macho
- X dado Y=hembra se distribuye como otra Gaussiana con μ_hembra y σ_hembra

### ¿Qué Ves Cuando Graficas Todos los Pesos Juntos?

Alguien en la clase lo entendió perfecto: "Tenés dos campanas".

Exactamente. No ves UNA campana perfecta. Ves **dos campanas superpuestas**:
- Una centrada en el peso promedio de los machos
- Otra centrada en el peso promedio de las hembras

Como dijo el profesor: "Cuando haces la conjunta te da dos picos de acumulación".

### La Fórmula de la Mixtura

**P(X) = θ × Normal(μ_macho, σ_macho) + (1-θ) × Normal(μ_hembra, σ_hembra)**

Esto es exactamente la **esperanza sobre Y** que repasamos al principio. No fue coincidencia que el profesor empezara con esa regla.

### ¿Por Qué Importa?

Porque en el práctico con las flores de Iris harás exactamente esto:
- Tienes 3 tipos de flores (no 2 sexos de gatos)
- Cada tipo tiene su propia distribución de tamaños
- La distribución total es una **mixtura de 3 gaussianas**

### Una Reflexión del Profesor sobre Modelado

> "Estamos modelando el problema. Estamos diciendo 'yo creo que el sexo se distribuye de esta manera'. Capaz que en realidad no. Es una decisión de diseño, una hipótesis de cómo querés modelar tu fenómeno."

No hay una respuesta correcta única. Podrías asumir que los machos se distribuyen con una gaussiana y las hembras con una laplaciana. Esa es una **decisión de diseño**.

---

## Modelos Autoregresivos: La Estrategia para Generar

Esta fue la parte más compleja de la clase, pero es donde todo se conecta.

### La Idea Central

**Un modelo autoregresivo genera datos de a poquito, en orden, donde cada nuevo dato depende de los anteriores.**

Como dijo el profesor: "El modelo autorregresivo asume que existe una relación de dependencia entre variables aleatorias en un orden."

### ¿Por Qué Funciona?

Por la **regla del producto** (que repasamos al principio):

P(X1, X2, X3, ..., Xn) = P(X1) × P(X2|X1) × P(X3|X1,X2) × ... × P(Xn|X1,...,Xn-1)

La probabilidad conjunta de todos los píxeles de una imagen se puede escribir como un **producto de condicionales**. Esto es exactamente la regla del producto aplicada en cadena.

### Aplicación a Imágenes Blanco y Negro

Imagina una imagen donde cada píxel es 0 (negro) o 1 (blanco):

- **X1** (primer píxel): Se distribuye como Bernoulli(θ1)
- **X2 dado X1**: Se distribuye como Bernoulli(θ2) - pero θ2 depende del valor de X1
- **X3 dado X1 y X2**: Se distribuye como Bernoulli(θ3) - pero θ3 depende de X1 y X2
- Y así sucesivamente...

### El Problema: Explosión de Parámetros

Aquí viene el problema. ¿Cuántos parámetros necesitas?

- Para X1: 1 parámetro (θ1)
- Para X2|X1: 2 parámetros (uno para X1=0, otro para X1=1)
- Para X3|X1,X2: 4 parámetros (todas las combinaciones: 00, 01, 10, 11)
- Para Xn: **2^(n-1) parámetros**

Como dijo el profesor: "Una locura". Para una imagen de 100x100 píxeles (10,000 píxeles), tendrías 2^9999 parámetros. Imposible.

### La Solución: Aproximación con Perceptrones

En lugar de estimar **tablas gigantes**, usamos **funciones de aproximación** (perceptrones).

#### Para X2 dado X1:
- **Con tablas**: 2 parámetros separados
- **Con perceptrón**: σ(X1 × W2 + B2) = solo 2 parámetros (W2 y B2)

Parece lo mismo, pero mira lo que pasa con X3:

#### Para X3 dado X1 y X2:
- **Con tablas**: 4 parámetros
- **Con perceptrón**: σ(X1 × W31 + X2 × W32 + B3) = solo 3 parámetros

El profesor lo resumió perfectamente:

> "Uno crece cuadráticamente y el otro linealmente."

### ¿Por Qué Funciona el Perceptrón?

Porque las probabilidades condicionales son funciones que van de combinaciones de 0s y 1s a un valor entre 0 y 1. ¡Eso es exactamente lo que hace una sigmoide!

Como explicó el profesor: "Un perceptrón encaja muy bien. Es una función de transformación."

### Las Belief Networks de Hinton

Geoffrey Hinton (premio Nobel de Física 2024 por su trabajo en AI) propuso una forma elegante de organizar todo esto:

En lugar de tener un perceptrón separado por cada píxel, tienes **una gran red** donde:
- Las entradas son todos los píxeles
- Las salidas son todos los píxeles
- Los pesos forman una **matriz triangular** (algunos fijados en cero)

¿Por qué triangular? Porque la salida del píxel 1 no depende de nadie. La salida del píxel 2 solo depende del 1 (los demás pesos están en cero). La del píxel 3 solo depende del 1 y 2. Y así.

### La Asimetría Entre Entrenar y Generar

Algo importante que mencionó el profesor:

- **Para entrenar**: Puedes procesar toda la imagen a la vez (paralelismo). Pasas la imagen, calculas todas las probabilidades, comparas con los valores reales, ajustas los pesos.
- **Para generar**: Tienes que ir **píxel por píxel** en orden. Porque cada píxel depende de los anteriores, y no conoces los anteriores hasta que los generas.

> "Para muestrear yo tengo que muestrear de a uno porque yo dependo de lo que me salió en el anterior."

Esta asimetría es característica de los modelos autoregresivos y la vas a ver en modelos de lenguaje también (como GPT).

---

## El Práctico: Dataset Iris

### ¿Por Qué Este Práctico? El Propósito

Acabamos de ver mucha teoría:
- Distribuciones continuas (gaussianas)
- Mixturas de gaussianas (el ejemplo de los gatos)
- La diferencia entre clasificar (P(Y|X)) y generar (P(X|Y))
- Cómo estimar parámetros de distribuciones

El práctico de Iris es donde **todo esto se vuelve concreto**. Vas a tomar datos reales, estimar distribuciones, y luego **generar datos nuevos** que nunca existieron pero que se parecen a los reales.

Como dijo Juan: "Estos primeros prácticos son para entender los conceptos y jugar con las cosas. La idea es que después, cuando vayamos a los modelos más complejos, estos conceptos queden claros."

### ¿Qué es Iris?

Un dataset clásico de flores con:
- **3 tipos de flores**: Setosa, Versicolor, Virginica
- **4 medidas continuas**: largo y ancho del pétalo y del sépalo
- **150 observaciones**: 50 de cada tipo

Juan (el ayudante) aclaró algo importante: el **sépalo** son "las hojitas verdes que están abajo de la flor". La clase se rió.

#### ¿Por qué Iris es perfecto para aprender esto?

1. **Tiene subpoblaciones claras**: Los 3 tipos de flores son como los machos y hembras del ejemplo de los gatos. Cada tipo tiene sus propias características típicas.

2. **Tiene valores continuos**: El largo de un pétalo puede ser 4.7cm, 5.1cm, 4.832cm... No son categorías discretas.

3. **Es pequeño y manejable**: Solo 150 flores. Puedes ver los datos, graficarlos, entenderlos.

4. **Los patrones son reales**: Las Setosas tienden a tener sépalos más cortos que las Virginicas. Hay estructura real que descubrir.

### La Inversión del Problema: El Corazón del Cambio de Perspectiva

Esta es quizás la parte más importante de entender.

#### El Problema de Clasificación (lo que ya conoces)

En Machine Learning tradicional, el problema con Iris sería:

> "Tengo una flor. Medí su sépalo: 5.1cm de largo. ¿Qué tipo de flor es?"

Matemáticamente: **P(Y|X)** = "¿Cuál es la probabilidad de que sea Setosa/Versicolor/Virginica, dado que mide 5.1cm?"

Entrenas un clasificador, le das la medida, te dice "probablemente es Versicolor".

**El objetivo**: Dado un dato, predecir su categoría.

#### El Problema de Generación (lo nuevo)

En IA Generativa, damos vuelta la pregunta:

> "Quiero crear una flor Setosa ficticia pero realista. ¿Qué medidas debería tener?"

Matemáticamente: **P(X|Y)** = "¿Cuál es la probabilidad de que mida cierta cantidad, dado que es Setosa?"

**El objetivo**: Dada una categoría, generar datos realistas para esa categoría.

#### ¿Por Qué Este Cambio Importa?

Piensa en aplicaciones reales:

- **Clasificación**: "Esta imagen, ¿es un gato o un perro?" → Útil para etiquetar fotos
- **Generación**: "Generame una imagen de un gato" → Útil para crear contenido nuevo

En clasificación, consumes datos existentes. En generación, **creas datos nuevos**.

Como dijo alguien en la clase: "Dimos vuelta el problema". Exactamente.

#### Lo que Esto Significa en la Práctica

Para poder generar flores Setosa realistas, necesitas saber **cómo se distribuyen las medidas de las Setosas**:
- ¿Cuál es el largo de sépalo típico? (la media μ)
- ¿Cuánto varían entre sí? (la desviación estándar σ)

Una vez que tienes μ y σ, puedes **muestrear** de esa distribución gaussiana para crear medidas nuevas que "tienen sentido" como flores Setosa.

### Parte 1: Discretización - Un Atajo para Empezar

#### El Problema con los Valores Continuos

Hasta ahora, en el práctico anterior (el de tenis), trabajaste con variables discretas:
- ¿Llueve? Sí/No
- ¿Viento? Fuerte/Débil
- ¿Jugamos tenis? Sí/No

Podías contar: "De 14 días, 9 fueron sí y 5 fueron no. Entonces P(jugar) = 9/14".

Pero ahora tienes: "El sépalo mide 5.1cm, 4.9cm, 5.4cm, 4.8cm, 5.0cm..."

¿Cómo calculas P(sépalo = 5.1)? Si cada medida es única, ¡la probabilidad de exactamente 5.1cm sería casi cero!

#### La Solución: Agrupar en "Bins"

La discretización es convertir valores continuos en categorías:

```
Bin 0: sépalos entre 4.3cm y 5.0cm
Bin 1: sépalos entre 5.0cm y 5.5cm
Bin 2: sépalos entre 5.5cm y 6.0cm
... y así sucesivamente
```

Ahora puedes contar: "De 50 flores Setosa, 30 cayeron en Bin 1, 15 en Bin 0, 5 en Bin 2..."

Y calcular probabilidades como antes: P(Bin 1 | Setosa) = 30/50 = 0.6

#### ¿Por Qué Hacer Esto?

**Ventaja**: Vuelves al territorio conocido. Es el mismo enfoque que usaste con las variables discretas del tenis.

**Desventaja**: Pierdes información. Como dijo Juan: "Para nosotros 5.1 y 4.9 podría ser lo mismo".

Una flor con sépalo de 4.99cm y otra con 5.01cm son casi idénticas, pero si el corte está en 5.0, una queda en Bin 0 y otra en Bin 1.

#### El Propósito Pedagógico

Este paso existe para que veas que **el problema continuo se puede aproximar con el enfoque discreto que ya conoces**. Es un puente entre lo que sabes y lo nuevo.

Pero no es la solución ideal. Por eso pasamos a...

### Parte 2: Estimar Gaussianas - La Forma "Correcta"

#### La Idea Central

En lugar de discretizar (y perder información), asumimos que las medidas de cada tipo de flor siguen una **distribución gaussiana**.

¿Por qué gaussiana? Porque muchos fenómenos naturales se distribuyen así:
- Alturas de personas
- Pesos de animales de la misma especie
- Medidas de flores del mismo tipo

Es una **hipótesis de modelado** (recuerda lo que dijo el profesor: "Es una decisión de diseño").

#### Qué Estimas para Cada Tipo de Flor

Para las 50 flores Setosa, calculas:
- **μ_setosa**: El promedio del largo del sépalo (por ejemplo, 5.0cm)
- **σ_setosa**: La desviación estándar (por ejemplo, 0.35cm)

Esto significa: "Las Setosas típicamente tienen sépalos de ~5.0cm, variando ±0.35cm aproximadamente".

Repites para Versicolor y Virginica. Ahora tienes **6 parámetros** (2 por cada tipo).

#### Cómo Generas Datos Nuevos

Una vez que tienes μ_setosa y σ_setosa, puedes **muestrear** de esa gaussiana:

```python
nuevo_sepalo_setosa = np.random.normal(mu_setosa, sigma_setosa)
# Podría darte: 4.87, 5.23, 4.95, 5.11...
```

Cada vez que muestreas, obtienes un valor **diferente** pero **realista** para una flor Setosa.

#### El Test de Calidad

¿Cómo sabes si tu modelo es bueno?

1. Generas 50 sépalos "artificiales" de Setosa
2. Los graficas junto a los 50 sépalos reales de Setosa
3. Si las distribuciones se parecen, tu modelo capturó el patrón

Como dijo Juan: "Grafiquen los datos generados y comparen con las gráficas originales. Deberían ser similares."

Si son muy diferentes, tu hipótesis (que es gaussiana) podría estar mal, o tus estimaciones de μ y σ son incorrectas.

### La Mixtura de Gaussianas: Viendo Todo Junto

#### El Contexto

Hasta ahora, siempre separaste por tipo de flor:
- "Para Setosa, la distribución es esta gaussiana"
- "Para Versicolor, es esta otra"
- "Para Virginica, es esta otra"

Eso es **P(X|Y)**: la distribución de X (medidas) condicionada a Y (tipo de flor).

Pero, ¿qué pasa si tomas **todas las flores juntas**, sin importar el tipo?

#### La Pregunta

Si alguien te da una medida de sépalo al azar de una de las 150 flores, sin decirte qué tipo es, ¿cuál es la distribución de esas medidas?

Eso es **P(X)**: la probabilidad marginal de X, sin condicionar.

#### La Conexión con la Teoría del Principio

¿Recuerdas la regla de la esperanza que repasamos al principio?

**P(X) = Esperanza sobre Y de [P(X|Y)]**

O escrito como suma:

**P(X) = P(Y=Setosa) × P(X|Setosa) + P(Y=Versicolor) × P(X|Versicolor) + P(Y=Virginica) × P(X|Virginica)**

Como hay 50 flores de cada tipo (150 total), cada tipo tiene probabilidad 1/3:

**P(X) = 1/3 × Gaussiana_Setosa + 1/3 × Gaussiana_Versicolor + 1/3 × Gaussiana_Virginica**

#### ¿Qué Ves Cuando Graficas Esto?

Recuerda el ejemplo de los gatos: cuando graficabas el peso de todos los gatos (machos y hembras juntos), veías **dos campanas superpuestas**.

Con Iris, ves **tres campanas superpuestas** (una por cada tipo de flor).

Si las tres tienen medias muy diferentes, verás tres picos separados.
Si las medias son similares, verás picos que se solapan.

#### Por Qué Importa

La mixtura te muestra **la estructura oculta** de tus datos:

- Si la mixtura tiene un solo pico, los tres tipos de flores son muy similares en esa medida (no es útil para distinguirlas)
- Si tiene tres picos separados, esa medida es muy diferente entre tipos (útil para clasificar)

Cuando Juan preguntó "¿Qué es eso?" y alguien respondió "La P(X)", estaba diciendo: "Es la distribución de las medidas cuando ignoras el tipo de flor".

### Resumen: El Flujo Completo del Práctico

1. **Cargas los datos**: 150 flores con sus medidas y tipos

2. **Discretización (opcional)**: Conviertes medidas continuas a bins para practicar el enfoque discreto

3. **Estimas P(X|Y) para cada tipo**:
   - Calculas μ y σ de las Setosas → tienes una gaussiana
   - Lo mismo para Versicolor y Virginica
   - Ahora puedes generar medidas nuevas para cualquier tipo

4. **Generas datos y comparas**: Muestreas de tus gaussianas, graficas, verificas que se parecen a los reales

5. **Calculas la mixtura P(X)**: Combinas las tres gaussianas ponderadas para ver la distribución total

El práctico te lleva de "tengo datos reales" a "puedo generar datos nuevos que se parecen a los reales". Ese es el objetivo de la IA Generativa.

---

## El Hilo Conductor: Todo Conectado

Ahora puedes ver cómo todo se conecta:

1. **Regla del producto** → nos permite descomponer probabilidades conjuntas → base de modelos autoregresivos

2. **Regla de la suma + producto = esperanza** → nos permite calcular marginales como mezclas → base de mixturas de gaussianas

3. **Perceptrones** → aproximan funciones de probabilidad condicional → reducen exponencialmente los parámetros necesarios

4. **Distribuciones continuas** → modelan datos del mundo real → gaussianas son las más útiles

5. **Mixturas** → cuando la población tiene subgrupos → cada subgrupo tiene su propia distribución

6. **P(X|Y) vs P(Y|X)** → clasificación vs generación → el cambio de perspectiva del curso

---

## Conceptos Clave para el Examen

### 1. El perceptrón como estimador de parámetros
El output de un perceptrón no es solo "una probabilidad". Es el **parámetro θ de una distribución de Bernoulli**. Para generar, muestreas de esa distribución.

### 2. Las distribuciones son familias paramétricas
- Uniforme: 2 parámetros (A, B)
- Gaussiana: 2 parámetros (μ, σ)
- Bernoulli: 1 parámetro (θ)

No memorices las fórmulas. Entiende qué representa cada parámetro.

### 3. Mixtura = promedio ponderado de distribuciones
Cuando tienes subpoblaciones, la distribución total es una combinación de las individuales, ponderadas por la probabilidad de cada subpoblación.

### 4. Autoregresivo = generar en orden, cada paso depende de los anteriores
Para entrenar: todo en paralelo. Para generar: uno por uno.

### 5. Aproximación con funciones reduce complejidad exponencial a lineal
En lugar de 2^n parámetros en tablas, usas n parámetros en un perceptrón.

---

## Resumen Simple (Si Tuvieras que Explicárselo a Alguien)

Imagina que tienes muchas fotos de gatos y quieres que una computadora **invente fotos nuevas de gatos**.

Primer problema: las fotos tienen millones de píxeles. No puedes guardar una tabla con todas las combinaciones posibles.

Solución 1: Generas la foto **píxel por píxel**. Cada nuevo píxel depende de los anteriores. Esto se llama **modelo autoregresivo**.

Pero aún así, cada píxel podría depender de millones de píxeles anteriores. Las tablas siguen siendo enormes.

Solución 2: Usas un **perceptrón** para aproximar esas probabilidades. En lugar de tablas de 2^n valores, tienes una función con n parámetros.

¿Y qué da el perceptrón? No solo "la probabilidad de que el píxel sea blanco". Da el **parámetro de una distribución**. Luego lanzas una moneda cargada con ese parámetro para decidir si el píxel es blanco o negro.

Para datos continuos (como el peso de un gato), usas **gaussianas** en lugar de monedas. El perceptrón te da la media y desviación estándar, y luego muestreas de esa campana.

Y si los gatos vienen en subtipos (machos vs hembras, diferentes razas), cada subtipo tiene su propia campana. La distribución total es una **mezcla de campanas**.

Eso es, en esencia, lo que vimos hoy.

---

## Definiciones para el Parcial

### El Cambio de Perspectiva

**P(Y|X) - Clasificación:** Dado un dato X, ¿a qué categoría Y pertenece?; es el problema tradicional de Machine Learning donde emites un veredicto consistente.

**P(X|Y) - Generación:** Dada una categoría Y, ¿qué datos X son típicos de ella?; es el problema de IA Generativa donde creas datos nuevos que se parecen a los reales.

**Inversión del Problema:** El cambio fundamental entre clasificación y generación; en clasificación consumes datos existentes, en generación creas datos nuevos.

### Muestrear de una Distribución

**Muestrear (Sampling):** Obtener un valor aleatorio que sigue una distribución de probabilidad; es como tirar una moneda cargada donde el parámetro θ define qué tan cargada está.

**Parámetro de una Distribución (θ, μ, σ):** Valores que definen la forma de la distribución; el perceptrón los estima pero NO los aprende directamente.

**Parámetros de la Red (W, B):** Los pesos y biases que se ajustan con gradiente descendente para que la red aprenda a estimar los parámetros de distribución.

### Distribuciones Continuas

**Distribución Uniforme:** Todos los valores entre A y B son igualmente probables; forma de línea recta horizontal; parámetros: A y B (los límites).

**Distribución Normal (Gaussiana):** La famosa "campana"; valores se concentran alrededor de la media con menos probabilidad en los extremos; parámetros: μ (media, el centro) y σ (desviación estándar, el ancho).

**Distribución Laplaciana:** Similar a la gaussiana pero con pico más agudo en el centro; parámetros: μ (media) y b (concentración).

### Mixturas

**Mixtura de Gaussianas:** Combinación ponderada de varias distribuciones gaussianas; se usa cuando los datos vienen de subpoblaciones distintas (ej: pesos de gatos machos + hembras = dos campanas superpuestas).

**Fórmula de Mixtura:** P(X) = θ × Normal(μ₁, σ₁) + (1-θ) × Normal(μ₂, σ₂); cada componente representa una subpoblación ponderada por su probabilidad.

### Modelos Autorregresivos

**Modelo Autorregresivo:** Modelo que genera datos de a poquito, en orden, donde cada nuevo dato depende de los anteriores; usa la regla del producto: P(X₁,...,Xₙ) = P(X₁) × P(X₂|X₁) × ...

**Explosión de Parámetros en Autorregresivos:** Sin aproximación, el píxel n necesita 2^(n-1) parámetros; para 784 píxeles sería 2^783, imposible de manejar.

**Aproximación con Perceptrones:** En lugar de tablas gigantes, usamos perceptrones que aproximan las probabilidades condicionales; reduce complejidad de exponencial a lineal.

**Belief Networks de Hinton:** Arquitectura con matriz triangular donde cada perceptrón solo "ve" los píxeles anteriores gracias a que los pesos superiores están fijados en cero.

### El Práctico de Iris

**Discretización:** Convertir valores continuos en categorías (bins) para poder usar el enfoque de conteo de frecuencias; pierde información pero simplifica el problema.

**Estimación de Gaussianas:** Calcular μ y σ de los datos para cada categoría; permite generar datos nuevos muestreando de Normal(μ, σ).

### Conceptos Matemáticos

**Esperanza (Valor Esperado):** Promedio ponderado de todos los valores posibles de una variable aleatoria; E[X] = Σ x·P(x); conecta la regla de la suma con las mixturas.

**Área bajo la curva = 1:** Propiedad fundamental de todas las distribuciones de probabilidad; garantiza que las probabilidades sumen 100%.

### Resumen de Relaciones Clave

| Concepto | Para qué sirve |
|----------|---------------|
| Regla del producto | Descomponer conjuntas en condicionales |
| Regla de la suma | Eliminar variables, calcular marginales |
| Perceptrón | Aproximar funciones de probabilidad condicional |
| Mixtura | Modelar datos con subpoblaciones |
| Autorregresivo | Generar secuencialmente, cada paso depende del anterior |
