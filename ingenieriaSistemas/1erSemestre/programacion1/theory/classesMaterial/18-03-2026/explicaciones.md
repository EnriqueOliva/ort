# Clase 2 — Miércoles 18/03/2026 — Teórico
## Programación 1 · Prof. Gonzalo Wagner
### Pensamiento Computacional, Algoritmos y Estructuras de Control

---

## La Gran Pregunta

Si ya sabemos qué quiere resolver una computadora, ¿cómo le explicamos exactamente cómo hacerlo, sin ambigüedad, sin que nos malentienda, sin que se quede pegada para siempre?

---

## Conexión con la Clase Anterior

En la primera clase vimos que las computadoras necesitan instrucciones precisas, y que hay niveles de lenguaje entre el código que escribe un humano y el que entiende la máquina. Hoy arrancamos desde ahí: ¿cómo pensamos los problemas antes de escribir una sola línea de código? Eso es el Pensamiento Computacional. Y después vemos las estructuras básicas que usan todos los algoritmos — secuencia, decisión e iteración.

---

## 1. Repaso: Los Cuatro Pilares del Pensamiento Computacional

Wagner empezó preguntando qué recordaban del Video 2 que habían visto en casa. Los estudiantes fueron mencionando piezas, y él armó el mapa completo.

> "¿Hasta cuánto ir bajando, descomponerlo? Hasta que sea un problema que es fácil de resolver, que es obvio, digamos, la resolución, o sencilla"

**Traducción:** No descompongas por descomponer. Pará cuando la pieza que queda sea tan chica que la solución sea evidente.

Los cuatro pilares son:

| Pilar | Qué hace |
|---|---|
| **Descomposición** | Romper el problema grande en partes más chicas y manejables |
| **Reconocimiento de patrones** | Encontrar similitudes con problemas que ya resolviste antes |
| **Abstracción** | Quedarte con lo que importa, ignorar el resto |
| **Diseño de algoritmos** | Escribir los pasos ordenados para llegar a la solución |

Pensá en armar un mueble de IKEA. Primero lo separás en partes (descomposición). Ves que ya armaste algo parecido antes (patrón). Te concentrás en las instrucciones de esta pieza y no en el resto del catálogo (abstracción). Seguís los pasos en orden (algoritmo).

---

## 2. Definición Formal de Pensamiento Computacional

> "Es un proceso de resolución de problemas"

**Traducción:** No es solo "pensar como computadora" — es una metodología completa para atacar problemas.

Características formales que dio Wagner:

- **Formular problemas** para que una computadora pueda procesarlos
- **Organizar y analizar datos** de forma lógica
- **Automatizar soluciones** (ahí está la matemática detrás de la programación)
- **Representar datos** mediante abstracciones: modelos, simulaciones
- **Identificar combinaciones eficientes** de pasos y recursos
- **Generalizar** el proceso de resolución para poder reutilizarlo en otros problemas

> "Obviamente, como yo les decía ya en la clase pasada, tenemos muchas soluciones para un mismo problema, pero hay soluciones que son más eficientes que otras, o que usan menos recursos que otras"

**Traducción:** No hay una sola solución correcta. Pero sí hay soluciones mejores y peores — más rápidas, más claras, que usan menos memoria.

---

## 3. Abstracción: Quedarse Solo con lo que Importa

### El mapa del metro de Buenos Aires

> "Yo quiero llegar de tal lado a tal lado. A mí lo que me interesa es saber... la línea B. A mí el resto, la verdad, no me importa"

**Traducción:** El mapa del metro no muestra calles, edificios ni distancias reales. Solo muestra las líneas y las conexiones. Eso es abstracción: se descartó todo lo que no sirve para el objetivo de llegar de A a B en subte.

> "Me abstraigo de lo que yo necesito. Lo del resto, que sea irrelevante, que no me sirve, está fuera"

**Traducción:** La abstracción no es simplificar por simplificar — es identificar qué información necesitás para tu objetivo concreto y filtrar el ruido.

> "Típico cuando van a hablar con un cliente de que les va a dar información que no sirve para nada"

**Traducción:** En el trabajo real como programador, el cliente te va a contar mil cosas. Tu trabajo es abstraerte — identificar qué es lo que realmente necesitás saber para resolver su problema.

### El pastel: niveles de abstracción

Wagner usó el ejemplo de hornear un pastel para mostrar que la abstracción tiene capas.

> "Todo entero de una no me sirve analizarlo. Sirve ir de a poco"

**Traducción:** No intentás procesar toda la receta al mismo tiempo. Primero resolvés la pregunta más grande (¿tengo los ingredientes?), después bajás al siguiente nivel (¿cuánto de cada uno?), después al siguiente (¿cuánto tiempo en el horno?).

Los niveles que mostró:

1. ¿Tengo todos los ingredientes? (no me importa todavía cómo mezclarlos)
2. ¿Qué cantidad de cada ingrediente necesito?
3. ¿Cuánto tiempo de cocción?

Es como armar un proyecto de software: primero preguntás "¿esto es posible hacer?", después "¿qué módulos necesito?", después "¿cómo funciona cada módulo?"

---

## 4. Reconocimiento de Patrones

Wagner mostró varios ejercicios visuales para demostrar que los humanos somos máquinas de reconocer patrones. El punto no era que somos buenos en esto — era que cuando programamos, tenemos que hacer explícito ese proceso que hacemos de forma intuitiva.

> "Esto lo programamos porque tiene que cumplir ciertos patrones para poder funcionar"

**Traducción:** Cuando codificás una solución, no estás adivinando — estás describiendo el patrón que encontraste de forma que la computadora pueda aplicarlo.

Los ejercicios que mostró:

- **Íconos que rotan:** Los estudiantes identificaron rápidamente el patrón (rotación) y predijeron el siguiente. El patrón era evidente en cuestión de segundos.
- **Imagen parcialmente revelada:** Reconocer qué es aunque solo se ve una fracción.
- **Puzzle de regiones con números 1 a N sin vecinos iguales:** Resolver paso a paso usando lógica — cada restricción elimina posibilidades.
- **Personajes de Disney simplificados:** Reconocer a Mowgli, a Jasmine, a personajes de pixeles o siluetas mínimas.
- **Grilla de perros y huesos:** Puzzle con restricciones en filas y columnas.
- **Pirámide de números:** Cada posición es la suma de los dos de abajo. Con algunos datos conocidos, deducís el resto.

La idea común en todos: tu cerebro busca la regla que explica lo que ves. Eso mismo hace un algoritmo.

---

## 5. Algoritmos: Definición y Propiedades

> "Un algoritmo es una secuencia ordenada de pasos para resolver un tipo específico de problema"

**Traducción:** No es cualquier lista de pasos — tiene que estar ordenada, y tiene que resolver un tipo de problema (no solo "este problema una vez").

> "Es importante la palabra ordenada. ¿Por qué? Porque esa secuencia de pasos, si yo no los ordeno, no llego a lo mismo. Por ejemplo, para hacer un café, si no pongo la taza antes, no me va a quedar el café hecho. Me queda en el piso."

**Traducción:** El orden no es decorativo — es estructural. Si cambiás el orden de los pasos, el resultado cambia. Un algoritmo con los pasos correctos pero en el orden equivocado no funciona.

### Las cinco propiedades obligatorias de un algoritmo

**Finito:**

> "La contradicción de infinito. O sea que pueda terminar"

**Traducción:** Un algoritmo que no termina nunca no es un algoritmo — es un problema. El loop infinito que vamos a ver más adelante es justamente cuando algo que debería terminar, no termina.

**Tiene entrada:**

> "El algoritmo va a recibir datos de entrada que lo va a procesar"

**Traducción:** Los datos con los que trabaja el algoritmo. Por ejemplo, el algoritmo de Euclides para el máximo común divisor recibe dos números.

**Tiene salida:**

> "Va a devolver un dato"

**Traducción:** Siempre produce un resultado. El algoritmo de Euclides devuelve el MCD de los dos números que recibió.

**Efectivo:**

> "Todas las operaciones son lo suficientemente básicas para que puedan ser realizadas en tiempo finito"

**Traducción:** Cada paso tiene que ser algo concreto y ejecutable. No podés tener un paso que diga "resolver la vida" — eso no es básico ni finito.

**Preciso:**

> "Todos los pasos están bien detallados"

**Traducción:** Sin ambigüedad. Wagner usó un ejemplo excelente:

> "¿Cuánto es un golpe de horno? ¿Cuánto tiempo es que tiene que estar en el horno?"

**Traducción:** Si la receta dice "un golpe de horno", eso no es preciso. La computadora — y el cocinero — necesitan temperatura exacta y tiempo exacto. La imprecisión rompe el algoritmo.

### Los videos de algoritmos cotidianos

Wagner mostró tres videos que representaban algoritmos de la vida diaria:

**Hacer un sándwich:** Lista secuencial de pasos. Simple, lineal, sin decisiones.

**Cambiar una lamparita:** Incluía una decisión ("si no tenés reemplazo, ir a comprar") y una iteración ("repetir el giro hasta que se afloje"). Ya no es solo secuencia.

**Coser un botón:** Si no tenés hilo, aguja o botón, ir al negocio. Mientras el botón no esté firme, pasar la aguja. Dos estructuras: decisión e iteración.

> "La secuencia, la decisión y la iteración son lo que llamamos estructuras de control, y con ellas construimos los programas."

**Traducción:** Con solo estas tres piezas — hacer cosas en orden, tomar decisiones, y repetir — se puede construir cualquier programa. Todo lo que va a venir en el curso se basa en estas tres.

---

## 6. Estructuras de Control

Esta es la parte técnica central de la clase. Las estructuras de control son los tres ladrillos con los que se construye todo algoritmo.

### 6.1 Secuencia

La más básica. Una lista de pasos que se ejecutan uno después del otro, en orden.

```
prender el fuego
calentar la sartén
agregar manteca
```

Sin condiciones, sin repeticiones, sin indentación especial. Lo que está arriba pasa antes que lo que está abajo, siempre.

---

### 6.2 Decisión (SI / SI — OTRO CASO)

> "El sí siempre va a preguntar una única vez la condición"

**Traducción:** La estructura SI evalúa la condición exactamente una vez. Si es verdadera, ejecuta el bloque. Si es falsa, lo saltea. No vuelve a preguntar.

> "Para volver a ejecutar varias veces necesitamos una iterativa"

**Traducción:** El SI no repite — si necesitás repetir algo hasta que una condición cambie, necesitás MIENTRAS.

**SI sin otro caso:**

```
SI tengo frío
    ponerme el abrigo
```

Si no hace frío, no pasa nada. El algoritmo continúa normalmente después del SI.

**SI con OTRO CASO:**

```
SI tengo tiempo Y tengo mucha hambre
    pedir jugo, torta y waffles
OTRO CASO
    pedir solo café
```

> "O se ejecuta este o se ejecuta el otro. No me voy a pedir jugo, torta, waffles y además café. Eso no va a pasar."

**Traducción:** Uno de los dos bloques siempre se ejecuta. Nunca los dos al mismo tiempo.

Wagner enfatizó el caso con condición compuesta: para entrar al primer bloque, las DOS condiciones tienen que ser verdaderas (por el Y). Si tengo tiempo pero no tengo hambre, voy al OTRO CASO.

> "Y en el otro caso también podés meter condición. Lo que está dentro del sí, del otro caso, del mientras — yo puedo armar un algoritmo nuevo entero."

**Traducción:** Las decisiones anidadas son válidas. Un SI dentro de otro SI, o un MIENTRAS dentro de un SI. La indentación muestra a qué estructura pertenece cada bloque.

---

### 6.3 Iteración — REPETIR X VECES

Cuando sabés exactamente cuántas veces querés repetir algo.

> "Repetir cinco veces. Tomar un pan, poner queso, poner jamón, tomar otro pan."

**Traducción:** Todo lo que está dentro del bloque se ejecuta 5 veces en total. El número es fijo de antemano.

```
REPETIR 5 veces
    tomar un pan
    poner queso
    poner jamón
    tomar otro pan
```

Wagner mencionó que en JavaScript esto se convierte en el bucle `for`. Por ahora lo escribimos en pseudocódigo.

---

### 6.4 Iteración — MIENTRAS (while)

La estructura más importante de la clase, y la que más cuidado requiere.

> "Si la condición es verdadera, ejecuta una iteración. Vuelvo a preguntar si la condición es verdadera, vuelvo a ejecutar la iteración"

**Traducción:** El orden es siempre: (1) evaluar condición, (2) si es verdadera ejecutar el bloque, (3) volver a (1). Si en el paso (1) la condición ya es falsa, el bloque NUNCA se ejecuta.

```
MIENTRAS esté seca la tierra
    agregar 15 gotas de agua
```

> "Imagínense que la voy a ejecutar por primera vez y llovió y la tierra estaba mojada. No se ejecuta."

**Traducción:** Si llovió y la tierra ya está húmeda, el bloque no se ejecuta ni una vez. El MIENTRAS puede ejecutarse cero veces.

**La regla de oro del MIENTRAS:**

> "Es muy importante que dentro de esa iteración modifique esa condición y en algún momento se vuelva falsa"

**Traducción:** Si el código dentro del MIENTRAS nunca cambia la condición, la condición siempre va a ser verdadera, y el algoritmo nunca va a terminar. Eso es un **loop infinito**. El programa se queda colgado para siempre.

---

### 6.5 Iteración — REPETIR...MIENTRAS (do...while)

> "A diferencia del mientras, la primera vez se va a ejecutar el código. El orden cambia. Antes era condición y después ejecuto. Acá es al revés. Ejecuto y luego me fijo si continúo"

**Traducción:** La diferencia fundamental con MIENTRAS es que REPETIR...MIENTRAS garantiza que el bloque se ejecuta al menos una vez, sin importar la condición.

```
REPETIR
    poner manteca
    poner preparación
    esperar 30 segundos
    dar vuelta
    esperar 30 segundos
    sacar panqueque
MIENTRAS haya preparación
```

También existe la variante con **HASTA** en lugar de MIENTRAS, que invierte la condición: en vez de "continuar mientras X sea verdad", es "continuar hasta que X sea verdad". Son equivalentes.

> "Hay que tener cuidado en qué momento se utiliza el uno o el otro"

**Traducción:** Wagner mostró el ejemplo de los panqueques para ilustrar la diferencia crítica:

- **MIENTRAS haya preparación:** Si no hiciste la mezcla, el código no se ejecuta. La sartén nunca llega a calentarse para nada.
- **REPETIR...MIENTRAS haya preparación:** Si no hiciste la mezcla, igual intentás hacer el panqueque. Ponés manteca en la sartén, ponés "nada" porque no hay preparación, y terminás con un desastre.

La regla práctica: usá MIENTRAS cuando tiene sentido que el bloque nunca se ejecute. Usá REPETIR...MIENTRAS cuando el bloque siempre tiene que ejecutarse al menos una vez por lógica del problema.

---

### Resumen visual de las estructuras

```
SECUENCIA:           paso 1 → paso 2 → paso 3

DECISIÓN:            ¿condición? → SI: bloque A
                                  → NO: bloque B (o nada)

MIENTRAS:            ¿condición? → SI: bloque → vuelve a preguntar
                                  → NO: sigue adelante

REPETIR...MIENTRAS:  bloque → ¿condición? → SI: vuelve al bloque
                                           → NO: sigue adelante
```

---

## 7. Pseudocódigo y Diagramas de Flujo

### Pseudocódigo

> "Luego cuando empecemos con Javascript van a ver que vamos a tomar los algoritmos hechos con pseudocódigo y le vamos a dar traducir básicamente a JavaScript"

**Traducción:** El pseudocódigo es el paso intermedio entre "cómo pienso el problema" y "código que ejecuta la computadora". Lo escribís en español, con la estructura lógica del algoritmo pero sin preocuparte por la sintaxis exacta del lenguaje.

> "Para que nos sea fácil de leer y decir, ok, esto es dentro del sí"

**Traducción:** La **indentación** (sangría) en pseudocódigo es visual — sirve para que vos y cualquier otro que lea el código entienda qué pasos están dentro de qué estructura.

> "Hay algunos lenguajes de programación que si no se escribe con los espacios correspondientes no funciona"

**Traducción:** En Python, por ejemplo, la indentación es obligatoria — si no indentás correctamente, el programa no corre. En JavaScript es convención de estilo, pero igualmente importante para la legibilidad.

### Diagramas de Flujo

Representación gráfica del mismo algoritmo. Los símbolos clave:

```
[Rectángulo]   — paso de proceso (una acción)
<Rombo>        — condición (SI / MIENTRAS)
-->            — flecha de flujo
```

El MIENTRAS en diagrama de flujo tiene una flecha que vuelve hacia atrás (hacia arriba) hasta el rombo de la condición — eso es lo que hace visible el "loop".

Wagner mostró el video del hotel a la estación de tren, donde el mismo problema se representaba de cuatro formas: mapa, texto, diagrama de flujo, código. Todas son el mismo algoritmo expresado diferente.

> "Muchas veces hay más de un posible algoritmo para resolver efectivamente un problema"

**Traducción:** La solución no es única. Hay múltiples caminos válidos, aunque algunos sean más eficientes que otros.

---

## 8. Ejercicio del Dibujo: Por Qué la Precisión Importa

Wagner dio instrucciones verbales para dibujar algo (una carita sonriente). Los estudiantes interpretaron diferente.

> "Dibujar en la parte inferior de la circunferencia la parte inferior de media circunferencia más chica"

**Traducción:** La instrucción parece clara, pero cada estudiante dibujó algo distinto. Algunos hicieron la sonrisa al revés, otros la hicieron fuera del círculo. Demuestra que lo que parece preciso para el emisor puede ser ambiguo para el receptor.

Después usó ChatGPT para dar instrucciones de dibujo de un gato — también imprecisas. Luego intentó un cohete en arte ASCII — los triángulos terminaron en lugares incorrectos.

> "Le dijo abajo, pero tomó la base del texto, no la base del cuadrado."

**Traducción:** La computadora (o la IA) interpreta literalmente. Si decís "abajo" sin especificar abajo de qué, va a interpretar lo que le parezca. La lección: **la especificidad es todo** en programación.

---

## 9. Ejercicio del Cruce de Calle (A a D)

Enunciado: hay una intersección con semáforo. Hay que ir del punto A al punto D cruzando la calle.

**Intento 1 (solo SI):**

```
SI la luz está en verde
    cruzar
```

Problema: si está en rojo, el algoritmo termina y nunca cruzo.

**Solución correcta con MIENTRAS:**

```
mirar hacia D
MIENTRAS la luz NO esté en verde
    esperar 5 segundos
cruzar a D
```

> "Cuando termina el mientras, ¿en qué estado va a estar la luz? En verde. Porque es la única forma de que esta condición me dé falso"

**Traducción:** Al salir del bucle, la condición de salida garantiza que la luz es verde. No necesito verificarlo de nuevo. Esto es algo fundamental del MIENTRAS: cuando termina, sabés exactamente en qué estado quedó la condición.

Un estudiante propuso usar REPETIR...MIENTRAS en lugar de MIENTRAS:

> "Lo que me estás describiendo es el mismo MIENTRAS. El repetir, por ejemplo, cinco veces, como la que habíamos puesto hoy, siempre le tenés que poner la cantidad de veces."

**Traducción:** REPETIR X VECES no sirve acá porque no sabés cuántas veces va a cambiar el semáforo. El MIENTRAS es la estructura correcta para "esperar hasta que pase algo".

Los estudiantes propusieron varias soluciones alternativas:

- Cruzar primero a B (perpendicular), después a D
- Ir en diagonal
- Mirar el semáforo de la calle perpendicular (si B está en rojo, D está en verde)

> "Hay más de una solución"

**Traducción:** En programación también hay múltiples soluciones correctas a un mismo problema. Algunas son más eficientes, más legibles, o más robustas.

---

## 10. Ejercicio de los Panqueques

Este ejercicio integra secuencia, MIENTRAS y la discusión de REPETIR...MIENTRAS.

**Algoritmo completo construido en clase:**

```
prender el fuego
calentar la sartén
MIENTRAS haya preparación (masa)
    poner manteca o aceite en la sartén
    poner una cucharada de preparación en la sartén
    esperar 30 segundos
    dar vuelta el panqueque
    esperar 30 segundos
    sacar el panqueque
apagar el fuego
lavar todo
```

> "Si no hacemos ese último paso vamos a tener problemas en casa"

**Traducción:** Los pasos de "limpieza" o cierre del proceso son parte del algoritmo. No son opcionales. En programación, esto se traduce en cerrar conexiones, liberar memoria, manejar los estados finales correctamente.

**La trampa del MIENTRAS vs REPETIR...MIENTRAS en este caso:**

> "Si yo le saco la condición, la de la masa, y ejecuto esto, voy a prender el fuego, calentar la sartén, apago el fuego y lavo. Porque va a llegar acá y no tener preparación."

**Traducción:** Si usás MIENTRAS y no hay masa, el programa salta todo el bloque de cocción y va directo a apagar y lavar. Seguro, limpio, correcto. Si usás REPETIR...MIENTRAS, intenta cocinar sin masa — un error.

---

## 11. Ejercicios de Bebras.org

Wagner mostró varios ejercicios del sitio bebras.org que trabajan reconocimiento de patrones y algoritmos.

**Nave espacial:** Había una secuencia de movimientos (izquierda, izquierda, arriba) que se repetía 3 veces para llegar al destino. La respuesta era 3.

**Secuencia numérica (2, 5, 10, ...):** El patrón era sumar números impares crecientes: +3, +5, +7, +9, +11... La respuesta era B (65).

**Tabla de ruteo de empresa de transporte:** Partiendo de B3 se generaba un loop infinito — la tabla de instrucciones te mandaba de vuelta a un punto ya visitado sin condición de salida.

**Robot en grilla:** Con instrucciones numéricas (0=arriba, 1=abajo, 2=derecha, 3=izquierda), la secuencia 3,0,2,0,1 terminaba en la posición H.

**Ecuación de frutas:** 4 manzanas = 28, entonces manzana = 7. Con ese valor conocido, resolver el sistema de ecuaciones para el resto de las frutas. Resultado: 25.

---

## 12. Tangente: Juegos y Algoritmos

Los estudiantes mencionaron ajedrez, Go, póker y Jenga. Wagner aprovechó para conectar con algoritmos.

**Ajedrez:** Árboles de decisión enormes. Las máquinas pueden calcular todas las posibilidades en fracciones de segundo.

> "Una máquina muy rápido puede ver todas esas decisiones. Va a ver cuál es la mejor. Y se utiliza un sistema de recompensa."

**Traducción:** Las IAs de ajedrez usan reinforcement learning — se premian las jugadas que llevan a ganar y se castigan las que llevan a perder. Con millones de partidas, el sistema "aprende" los mejores caminos.

**Go (AlphaGo):** Wagner mencionó la película de AlphaGo. Mucho más complejo que el ajedrez — las posibilidades se ramifican exponencialmente.

**Póker:** Cálculo de probabilidades, conteo de cartas. A diferencia del ajedrez, hay un componente de azar.

**Ta-te-ti:** Menos decisiones posibles — buen ejemplo para aprender a programar árboles de decisión de forma manejable.

---

## Planificar un Viaje: Ejemplo Completo de Descomposición

Wagner usó el ejemplo de planificar un trimestre (mes 1: tareas habituales, mes 2: viaje a Río, mes 3: preparar examen) para mostrar cómo la descomposición se aplica niveles cada vez más profundos.

Del viaje, se extrajo "tomar el avión", que se descompuso en:

```
¿Tengo valijas para despachar?
    SI: despachar valijas
    NO: ir directo a embarcar
embarcar
subir al avión
desayunar
```

**Despachar valijas** se descompuso aún más:

```
MIENTRAS me quede valija
    tomar una valija
    pesarla
    ponerle el sticker
    despacharla
SI se superó el peso permitido
    pagar recargo
```

**Desayunar en el avión:**

```
SI hay buen tiempo Y tengo mucha hambre
    pedir jugo y waffles
OTRO CASO
    pedir solo café
```

> "Esto lo vamos a ir haciendo de a poco. Tampoco tenemos problemas tan grandes en la práctica."

**Traducción:** En el curso, los problemas van a ser manejables. No necesitás resolver un sistema de control de vuelos — con cruzar una calle y hacer panqueques ya estamos practicando todas las estructuras.

---

## Para la Próxima Clase

> "Video 4 de variables"

Wagner asignó ver el **Video 4 sobre Variables** antes de la próxima clase. Los ejercicios restantes de Bebras.org que no alcanzaron a terminar en clase quedan como tarea.

> "Les dejo para terminar lo que queda y los vemos en la clase que viene"

---

## Definiciones para el Parcial

**Pensamiento Computacional:** Proceso de resolución de problemas que incluye descomposición, reconocimiento de patrones, abstracción y diseño de algoritmos, con el objetivo de formular soluciones que puedan ser ejecutadas por una computadora.

**Descomposición:** Separar un problema complejo en partes más pequeñas hasta que cada parte tenga una solución obvia o sencilla.

**Abstracción:** Quedarse con la información relevante para el problema que se está resolviendo e ignorar el resto. Tiene niveles — se puede ir de lo más general a lo más específico.

**Algoritmo:** Secuencia ordenada, finita, precisa y efectiva de pasos para resolver un tipo específico de problema, con al menos una entrada y una salida.

**Finitud:** Propiedad de un algoritmo que garantiza que termina en algún momento. Un algoritmo que no termina nunca no es un algoritmo válido.

**Precisión:** Propiedad de un algoritmo donde todos los pasos están lo suficientemente detallados como para no admitir interpretación ambigua.

**Secuencia:** Estructura de control que ejecuta pasos uno después del otro, en orden, sin condiciones ni repeticiones.

**Decisión (SI):** Estructura de control que evalúa una condición una sola vez y ejecuta un bloque si es verdadera, o lo saltea (o ejecuta el bloque OTRO CASO) si es falsa. Nunca se ejecutan ambos bloques.

**Iteración MIENTRAS:** Estructura de control que evalúa la condición antes de cada ejecución del bloque. Si la condición es falsa desde el inicio, el bloque nunca se ejecuta. El bloque interno debe modificar la condición para evitar un loop infinito.

**Iteración REPETIR...MIENTRAS:** Estructura de control que ejecuta el bloque primero y evalúa la condición después. Garantiza al menos una ejecución del bloque, independientemente de la condición inicial.

**REPETIR X VECES:** Estructura de control que ejecuta el bloque un número fijo y conocido de veces. Se convierte en el bucle `for` en JavaScript.

**Loop infinito:** Error que ocurre cuando la condición de un MIENTRAS nunca se vuelve falsa porque el cuerpo del bucle no la modifica, haciendo que el programa nunca termine.

**Pseudocódigo:** Descripción de un algoritmo en lenguaje natural (no en un lenguaje de programación), usando indentación para mostrar la estructura lógica. Se usa como paso previo a escribir código real.

**Indentación (sangría):** Espacio que se agrega al inicio de una línea para indicar que ese código pertenece a una estructura de control (SI, MIENTRAS, etc.). Facilita la lectura y en algunos lenguajes (Python) es obligatoria.

**Diagrama de flujo:** Representación gráfica de un algoritmo usando rectángulos para pasos y rombos para condiciones, con flechas que muestran el flujo de ejecución.

---

## Posibles Preguntas para el Parcial

**¿Cuáles son los cuatro pilares del pensamiento computacional?**
Descomposición, reconocimiento de patrones, abstracción y diseño de algoritmos.

**¿Cuáles son las cinco propiedades obligatorias de un algoritmo?**
Finito, tiene entrada, tiene salida, efectivo y preciso.

**¿Qué diferencia hay entre SI y MIENTRAS?**
El SI evalúa la condición una sola vez. El MIENTRAS la evalúa repetidamente hasta que sea falsa. Si la condición del SI es falsa, el bloque se saltea y listo. Si la condición del MIENTRAS es falsa desde el inicio, el bloque nunca se ejecuta, pero si es verdadera se repite hasta que cambie.

**¿Qué diferencia hay entre MIENTRAS y REPETIR...MIENTRAS?**
MIENTRAS evalúa la condición antes de ejecutar el bloque — puede ejecutarse cero veces. REPETIR...MIENTRAS ejecuta el bloque primero y evalúa la condición después — siempre se ejecuta al menos una vez.

**¿Por qué es peligroso el loop infinito y cómo se evita?**
El loop infinito ocurre cuando la condición del MIENTRAS nunca se vuelve falsa, haciendo que el programa corra para siempre. Se evita asegurando que dentro del cuerpo del bucle exista código que en algún momento modifique la condición hacia falso.

**¿Qué es la abstracción y para qué sirve?**
Es quedarse con la información relevante para el objetivo actual e ignorar el resto. Sirve para simplificar problemas complejos analizándolos por capas en lugar de todo junto.

**Si una receta dice "agregar un golpe de horno", ¿qué propiedad de los algoritmos viola?**
Viola la precisión, porque "un golpe de horno" es ambiguo — no especifica temperatura ni tiempo exacto, lo que genera interpretaciones diferentes.

**En el algoritmo del cruce de calle, ¿por qué no alcanza con un SI para esperar el semáforo?**
Porque el SI evalúa la condición una sola vez. Si la luz es roja, el SI no ejecuta el bloque y el algoritmo termina — la persona nunca cruza. El MIENTRAS sigue esperando hasta que la condición cambie.

**¿Qué garantiza saber sobre el estado de la condición cuando un bucle MIENTRAS termina?**
Que la condición se volvió falsa. Al salir del MIENTRAS, se garantiza que la condición de continuación ya no se cumple.

**Escribir en pseudocódigo un algoritmo para hacer panqueques mientras haya masa.**
```
prender el fuego
calentar la sartén
MIENTRAS haya preparación
    poner manteca en la sartén
    poner cucharada de preparación
    esperar 30 segundos
    dar vuelta el panqueque
    esperar 30 segundos
    sacar el panqueque
apagar el fuego
lavar todo
```

---

*Documento generado mediante análisis exhaustivo (3 pasadas) de la transcripción de la clase del 18/03/2026 — Programación 1, Prof. Gonzalo Wagner. ORT Uruguay, Ingeniería en Sistemas, 1er semestre 2026.*