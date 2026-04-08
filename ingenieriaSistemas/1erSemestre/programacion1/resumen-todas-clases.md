# Resumen Completo: Programación 1 — Clases 1 a 8 (16/03 al 07/04/2026)
## Programación 1 · Prof. Gonzalo Wagner (Teórico) · Sergio Cortinas (Oliver) y Andrés Mauricio Repeto Ferrero (Práctico)

---

## La Gran Pregunta del Semestre

¿Cómo se pasa de "tener un problema dando vueltas en la cabeza" a "una computadora que lo resuelve sola, sin ambigüedad, sin que se quede pegada para siempre"?

Esa es la pregunta que une las primeras 8 clases. No arrancamos por la sintaxis de un lenguaje — arrancamos por algo más básico: aprender a *pensar* el problema antes de escribir una sola línea. Después aprendemos a expresar ese pensamiento en pseudocódigo. Y recién al final, en la clase 8, escribimos el primer JavaScript real en una consola del navegador. Todo el camino está diseñado para que cuando llegues a `let` y `prompt()`, ya sepas qué querés decir — y lo que cambia es solo *cómo* decirlo.

---

## Conexión con la Clase Anterior

Estas son las primeras 8 clases del semestre. No hay clase anterior — y eso es exactamente el punto del curso. Asumimos cero conocimiento previo y construimos desde el suelo: qué es una computadora, qué es un programa, qué es pensar como programador, y solo entonces qué es escribir código.

---

## Mapa del Recorrido

```
Clase 1 (Teo) ─┐
               │ FUNDAMENTOS
Clase 2 (Pra) ─┤ (qué es una compu, cómo se evalúa, qué pinta la IA)
               │
Clase 3 (Teo) ─┘── PENSAMIENTO COMPUTACIONAL + ESTRUCTURAS DE CONTROL
                                    │
                                    ▼
Clase 4 (Teo) ─┐
               │ APLICAR ESTRUCTURAS A PROBLEMAS REALES
Clase 5 (Pra) ─┤ + INTRODUCCIÓN A VARIABLES Y AL "PARA" (for)
               │
Clase 6 (Teo) ─┘── EXPRESIONES ARITMÉTICAS Y LÓGICAS
                                    │
                                    ▼
Clase 7 (Teo) ─┐── EJERCICIOS COMPLEJOS (Fibonacci, máximo) +
               │   INTRODUCCIÓN A JAVASCRIPT (infografías)
Clase 8 (Pra) ─┘── PRIMER CÓDIGO JS REAL EN LA CONSOLA DEL NAVEGADOR
```

Tres etapas claras: **fundamentos** → **pseudocódigo con variables** → **JavaScript de verdad**.

---

# Parte I — Las Bases

## Clase 1 — Lunes 16/03/2026 — Introducción al Curso *(Teórico, Wagner)*

Esta clase fue toda contexto. Antes de programar, hay que entender qué es programar y por qué importa.

### Quién es Wagner

> "Soy Gonzalo Wagner, tengo 33 años. Soy licenciado en Sistemas de ORT, tengo un posgrado en inteligencia artificial y un máster en Big Data. Trabajo en Kuanam, en análisis de datos."

**Traducción:** El profe tiene experiencia real en industria *y* en IA — por eso la discusión sobre IA en clase no es teórica.

### Sistema de evaluación (esto va a la pared)

| Instancia | Puntos | Mínimo | Modalidad |
|---|---|---|---|
| Parcial 1 | 15 | 0 | Individual, papel, presencial |
| Obligatorio 1 | 10 | 0 | Pareja, HTML/CSS sin JS |
| Obligatorio 2 | 35 | **18** | Pareja, JS, **defensa obligatoria** |
| Parcial 2 | 40 | **20** | Individual, papel, presencial |
| **Total** | **100** | **70** | |

- Menos de 70 → no aprobás
- 70 a 85 → aprobás pero vas a examen
- 86 o más → exonerado
- **No ir a la defensa = perdés la materia, no importa la nota.**

### Fechas clave del semestre

| Evento | Fecha |
|---|---|
| Parcial 1 | 28 de abril |
| Letra del Obligatorio | 11 de mayo |
| Entrega Obligatorio 1 | 1 de junio |
| Parcial 2 | 6 de junio |
| Entrega Obligatorio 2 | 29 de junio |
| Fin del semestre | 3 de julio |

### Política de IA

> "Permitido: generar preguntas, obtener explicaciones, generar ejemplos, practicar ejercicios. No permitido: generar o resolver trabajos parcial o totalmente, usarla durante la defensa, presentar contenido generado por IA como propio."

**Traducción:** IA para *estudiar* sí. IA para *entregar trabajo que no es tuyo* no.

> "Nunca se va a contradecir. Le decís ¿cuánto es 1 más 1? Le dice 2. Le decís no, es 3, le dice sí, tenés razón, es 3."

**Traducción:** La IA está diseñada para complacer, no para tener razón. Verificar siempre.

### Definiciones formales del libro de cátedra

**Sistema:** conjunto de elementos organizados para llevar a cabo algún método, procedimiento o control mediante el procesamiento de la información.

**Hardware:** los elementos físicos. Se divide en *fundamental* (CPU, RAM, disco) y *accesorio* (mouse, teclado, impresora). Y por dirección: entrada, salida, o entrada/salida.

**Software:** los programas. Se clasifica en *general* (Word, Chrome) vs *específico* (sistema de facturación), y en *base* (sistema operativo) vs *aplicación* (todo lo que corre encima).

**Programa:** el arte de dar comandos a algo que puede ser ejecutado después.

**Diseño:** organizar los comandos antes de programar. Como un novelista que estructura un libro antes de escribirlo.

**Ingeniería de Software:** la aplicación de un enfoque sistemático, disciplinado y cuantificable hacia el desarrollo, operación y mantenimiento del software.

### Niveles de lenguaje

```
Lenguaje máquina   (0s y 1s — corriente sí/no)
       ↑
Assembler           (palabras cortas, 1 a 1 con la máquina)
       ↑
Alto nivel          (Python, JavaScript, Java...)
```

> "El compilado traduce TODO el código a lenguaje máquina primero y después lo ejecuta. El interpretado traduce y ejecuta línea por línea."

**Traducción:**

| | Compilado | Interpretado |
|---|---|---|
| Cuándo traduce | Antes de ejecutar | Durante la ejecución |
| Velocidad | Más rápida | Más lenta |
| Errores | Al compilar | Al llegar a la línea con error |
| Ejemplos | C, C++, Go, Rust | Python, **JavaScript**, Ruby |

JavaScript, el lenguaje del curso, es **interpretado**. Lo ejecuta el navegador línea por línea.

### Ciclo de vida del software

```
Requisitos → Diseño → Implementación → Pruebas → Mantenimiento
    ↑___________________________________________________|
```

- **Alpha testing** = lo hace el equipo de desarrollo
- **Beta testing** = lo hace el cliente o usuarios seleccionados

> "Hice todo el programa, me andaba hermoso, divino. Y mi pareja lo probó un domingo y ya me lo rompió."

**Traducción:** Quien escribió el código está sesgado. Otro encuentra los errores que vos no ves.

### Pensamiento computacional (los 4 pilares — el corazón del curso)

| Pilar | Qué hace |
|---|---|
| **Descomposición** | Romper el problema grande en partes más chicas |
| **Reconocimiento de patrones** | Encontrar similitudes con cosas que ya resolviste |
| **Abstracción** | Quedarte con lo esencial, ignorar el resto |
| **Diseño de algoritmos** | Escribir los pasos ordenados para llegar a la solución |

> "Ordenar la habitación de un adolescente — no decís 'ordená el cuarto', lo dividís: ropa, libros, cables, escritorio."

**Traducción:** Un problema grande te paraliza. El mismo problema dividido en partes chicas es atacable.

---

## Clase 2 — Martes 17/03/2026 — Práctico Inicial *(Práctico, Oliver y Mauricio)*

Primera clase del práctico. Casi sin contenido técnico — lo más importante fue entender la dinámica de los martes y la conversación honesta sobre IA y trabajo.

### Quiénes son los profes del práctico

**Sergio Cortinas (Oliver):** terminando Ingeniería en ORT, tiene 20 años de experiencia en IT. Su tesis es **Señor Ked**, un sistema con IA para hogares de ancianos (los enfermeros mandan audios, el sistema los procesa). Tiene financiamiento del BID y clientes reales. También trabaja para ACNUR como Project Manager.

> "Acá PM es todo. Acá el PM es PM, Scrum Master, Product Owner, a veces QA."

**Traducción:** En empresas de Uruguay no tenés un equipo de 5 PMs como en Google. Hacés de todo con pocos recursos.

**Andrés Mauricio Repeto Ferrero (Mauricio):** ingeniero ORT 2011, vive en Medellín, trabaja en IA. Más estructurado que Oliver, va a la claridad.

### Modalidad híbrida (hyflex)

La materia se da en formato **hyflex**: podés ir presencial o conectarte por Zoom *en simultáneo*. No son dos modalidades separadas, es la misma clase al mismo tiempo.

- **Teórico (Wagner):** lunes 20:30–22:30 y miércoles 17:30–19:25
- **Práctico:** martes 17:30–19:25, salón S221 + Zoom

> "Nosotros acá lo que vamos a hacer es ayudarlos a pensar, a tratar de resolver un problema, a ver por dónde empezar y a dónde quiero llegar."

**Traducción:** El práctico no es para repetir teoría. Es para sentarse a resolver, con guía.

> "Siempre la solución está en el aula. El tema es saber cómo llegar a esa solución."

**Traducción:** Las respuestas están publicadas. El trabajo es entender cómo se llega.

### IA: las anécdotas reales que dieron los profes

**Oliver con Copilot:**

> "En la empresa, que es partner de Microsoft, nos pidieron que desarrolláramos una aplicación usando únicamente Copilot, sin tocar código nosotros. Es muy difícil."

**Traducción:** Incluso para profesionales con años de experiencia, delegar todo a la IA sin poder leer ni corregir el código es un problema real.

**El caso COBOL:**

> "Los programadores de COBOL que más le tenían miedo a la IA son los que hoy más la están usando, porque entienden el código."

**Traducción:** La IA es más útil para quien ya sabe programar. Sin base, dependés ciegamente del output.

**Pérdida de fluidez:**

> "Desde que incorporé la IA en mi trabajo, realmente noté como que luego al escribir código por mi cuenta, se me hace mucho más difícil."

**Traducción:** Si delegás todo, la habilidad se atrofia. Como dejar de ir al gimnasio.

> "Es como cuando practicás un deporte. Los futbolistas que pasan meses sin jugar, después son un desastre."

### Sobre la defensa del Obligatorio

> "No ir a la defensa es perder la materia. Sin importar cuánto tenés."

**Traducción:** La defensa no es opcional. Dura unos 30 minutos, te piden un cambio sencillo al código para verificar que lo hiciste vos.

### Consejo para el obligatorio

> "No esperen ni al último día ni al último momento."

**Traducción:** Subir entregas parciales antes del límite es un seguro. Si algo falla el último día, ya tenés algo cargado.

---

## Clase 3 — Miércoles 18/03/2026 — Pensamiento Computacional + Estructuras de Control *(Teórico, Wagner)*

Esta es la clase técnica más importante de las primeras tres. Acá nacen los tres ladrillos con los que se construye cualquier programa: secuencia, decisión e iteración.

### Las 5 propiedades obligatorias de un algoritmo

| Propiedad | Qué significa |
|---|---|
| **Finito** | Termina en algún momento (lo opuesto: loop infinito) |
| **Tiene entrada** | Recibe datos para procesar |
| **Tiene salida** | Devuelve un resultado |
| **Efectivo** | Cada paso es básico y ejecutable en tiempo finito |
| **Preciso** | Sin ambigüedad — no admite interpretación |

> "¿Cuánto es un golpe de horno? ¿Cuánto tiempo es que tiene que estar en el horno?"

**Traducción:** "Un golpe de horno" no es preciso. La computadora — y el cocinero — necesitan temperatura y tiempo exactos.

### Las 3 estructuras de control

> "La secuencia, la decisión y la iteración son lo que llamamos estructuras de control, y con ellas construimos los programas."

**Traducción:** Con solo estos tres ladrillos — hacer cosas en orden, tomar decisiones, repetir — se puede construir *cualquier* programa.

#### 1. Secuencia

Lo más simple. Una lista de pasos en orden.

```
prender el fuego
calentar la sartén
agregar manteca
```

#### 2. Decisión: SI / SI–OTRO CASO

> "El sí siempre va a preguntar una única vez la condición."

```
SI tengo tiempo Y tengo mucha hambre
    pedir jugo, torta y waffles
OTRO CASO
    pedir solo café
```

> "O se ejecuta este o se ejecuta el otro. No me voy a pedir jugo, torta, waffles y además café."

**Traducción:** Uno de los dos bloques siempre se ejecuta, *nunca los dos*.

#### 3. Iteración: REPETIR X VECES

```
REPETIR 5 veces
    tomar un pan
    poner queso
    poner jamón
    tomar otro pan
```

Sirve cuando *sabés exactamente* cuántas veces. En JavaScript se traduce a `for`.

#### 4. Iteración: MIENTRAS (while)

```
MIENTRAS esté seca la tierra
    agregar 15 gotas de agua
```

> "Si la condición es verdadera, ejecuta una iteración. Vuelvo a preguntar si la condición es verdadera, vuelvo a ejecutar la iteración."

> "Imagínense que la voy a ejecutar por primera vez y llovió y la tierra estaba mojada. No se ejecuta."

**Traducción:** El `MIENTRAS` puede ejecutarse **cero veces** si la condición ya es falsa al inicio.

**La regla de oro:** dentro del `MIENTRAS` tiene que haber código que en algún momento haga la condición falsa. Si no, **loop infinito** — el programa nunca termina.

#### 5. Iteración: REPETIR…MIENTRAS (do-while)

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

> "A diferencia del mientras, la primera vez se va a ejecutar el código. El orden cambia. Antes era condición y después ejecuto. Acá es al revés. Ejecuto y luego me fijo si continúo."

**Traducción:** Garantiza al menos una ejecución. La trampa: si usás `REPETIR…MIENTRAS` para los panqueques pero no hay masa, igual ponés manteca en la sartén — un desastre. En cambio, el `MIENTRAS` corta antes y todo queda limpio.

#### Resumen visual

```
SECUENCIA:           paso 1 → paso 2 → paso 3

DECISIÓN:            ¿condición? → SI: bloque A
                                  → NO: bloque B (o nada)

MIENTRAS:            ¿condición? → SI: bloque → vuelve a preguntar
                                  → NO: sigue adelante

REPETIR…MIENTRAS:    bloque → ¿condición? → SI: vuelve al bloque
                                           → NO: sigue adelante
```

### Pseudocódigo

> "Luego cuando empecemos con Javascript van a ver que vamos a tomar los algoritmos hechos con pseudocódigo y le vamos a dar traducir básicamente a JavaScript."

**Traducción:** El pseudocódigo es el paso intermedio entre "lo pienso" y "código que corre". Lo escribís en español, sin preocuparte por sintaxis exacta. La **indentación** muestra qué pasos están dentro de qué estructura.

### Ejercicio del cruce de calle (la lección clave del MIENTRAS)

**Intento 1 (solo SI — incorrecto):**

```
SI la luz está en verde
    cruzar
```

Si está en rojo, el algoritmo termina y nunca cruzo.

**Solución correcta:**

```
mirar hacia D
MIENTRAS la luz NO esté en verde
    esperar 5 segundos
cruzar a D
```

> "Cuando termina el mientras, ¿en qué estado va a estar la luz? En verde. Porque es la única forma de que esta condición me dé falso."

**Traducción:** Al salir del bucle, sabés con certeza en qué estado quedó la condición. Esto es *fundamental* — vas a usar este truco constantemente.

---

# Parte II — De Pseudocódigo a Variables

## Clase 4 — Lunes 23/03/2026 — Práctico 2 + Variables + el "Para" *(Teórico, Wagner)*

Esta clase mezcla repaso, ejercicios extensos, y la introducción de dos conceptos enormes: **variables** y el **for** (para).

### Repaso con quiz interactivo

Wagner usó un quiz tipo Wooclap para repasar las definiciones del pensamiento computacional, los pilares, las estructuras de control. Las respuestas correctas fueron las "obvias" — pero el ejercicio era para forzar a fijar el vocabulario.

### Práctico 2 — Algoritmos de la vida cotidiana

Los ejercicios que se trabajaron en clase (pseudocódigo, sin código aún):

1. **Anotarse en la universidad** — secuencia + SI con condición ("si cumple requisito de tener sexto salvado")
2. **Pintar un cuarto** — `MIENTRAS paredes sin pintar` o `REPETIR 4 VECES pintar pared`
3. **Descargar e instalar una app** — secuencia + SI
4. **Tirar una moneda** (cara estudio / cruz cine + estudio):

   Primero versión larga con `SI…OTRO CASO`. Después la simplificación:

   ```
   tirar moneda
   SI sale cruz
       ir al cine
   estudiar
   ```

   > "Vean que estamos haciendo exactamente el mismo resultado pero escribiéndolo un poquito más cortito. No repetimos tampoco. Eso siempre vamos a tratar de evitar, repetir el código."

5. **Comprar entrada a un concierto por la web**
6. **Solicitar un préstamo en un banco** — el ejercicio donde quedó claro el `MIENTRAS`:

   ```
   sacar número
   MIENTRAS no es mi turno
       esperar 30 segundos
   ir al mostrador
   ```

   > "Si yo lo hubiera hecho con el SI, en cuanto hay tres personas adelante, el SI se evalúa una sola vez, no es mi turno, y se va a casa."

7. **Reclamar reparación de una computadora** — combina `MIENTRAS` con condición compuesta (`mientras no me solucionaron Y hay superiores`) y termina mostrando que `REPETIR…MIENTRAS` puede simplificar cuando sabés que la primera iteración siempre va.

8. **Retirar dinero del cajero automático** — `SI alcanza mi saldo retirar dinero`.

### Variables (Video 4 — repasado en clase)

> "Una variable es un lugar donde guardamos información."

**Traducción:** Es un casillero en la memoria RAM con un nombre. Le ponés algo, después lo recuperás por el nombre.

**Características que tiene que tener una variable:**

| Característica | Qué significa |
|---|---|
| Vive en RAM | Volátil — se pierde al apagar la computadora |
| Tiene un **nombre** | Identificador único |
| Tiene un **tipo de dato** (en algunos lenguajes) | Número entero, decimal, texto, etc. |
| Tiene un **valor** | Lo que está guardado adentro |

#### Reglas para nombrar variables

> "Tiene que ser mnemotécnico. Que yo al leer el nombre de la variable sepa para qué se va a utilizar."

**Traducción:** Si vas a guardar el precio, llamala `precio`. No `A`, `B`, `X`. El nombre tiene que decir qué guarda.

**camelCase** — la convención del curso:

```
puntajeMaximo       ✓
puntaje_maximo      ✗ (snake_case, no se usa acá)
PuntajeMaximo       ✗ (PascalCase, no se usa acá)
puntajemaximo       ✗ (ilegible)
```

Primera palabra en minúscula. Cada palabra siguiente arranca con mayúscula.

#### El tipo de dato

> "Eso no es en todos los lenguajes. En javascript no tenemos que indicar el tipo de datos. Pero por ejemplo el semestre que viene en Java sí le tienen que indicar."

**Traducción:** JavaScript es **dinámicamente tipado** — no le decís "esta variable guarda enteros". Java es estáticamente tipado — sí se lo tenés que decir.

### Primer ejemplo: precio con IVA

```
mostrar "ingrese precio"
leer precio
mostrar "el precio con IVA es " + precio * 1.22
```

> "A los textos los pongo entre comillas dobles. Si yo no le pongo comillas, él va a buscar una variable que se llama así."

**Traducción:** Comillas = texto literal. Sin comillas = nombre de variable.

### Segundo ejemplo: sumar 10 números (corrida a mano)

```
suma = 0
REPETIR 10 veces
    mostrar "ingrese dato"
    leer dato
    suma = suma + dato
mostrar "la suma es " + suma
```

> "Lo primero que tiene que resolver es lo que está a la derecha del igual. Suma más datos. Suma tiene 0, datos tiene 2, el resultado va a ser 2. Y luego ese 2 se lo va a asignar a la variable suma. Cuando yo lo estoy asignando, pasa por arriba el valor que tenía."

**Traducción de la asignación:** primero se calcula lo que está a la derecha del `=`, después ese resultado se *guarda pisando* lo que había en la variable de la izquierda. **No queda historial** — el valor anterior se pierde.

### Introducción al PARA (for)

> "Bueno, llegó el momento. Vamos a cambiar. En vez de repetir vamos a utilizar lo que se llama 'para'."

**Traducción:** Wagner anunció que `REPETIR X VECES` no se va a usar más — desde acá usamos `PARA`, que es mucho más cercano al `for` de JavaScript.

**Sintaxis del PARA:**

```
PARA (i = 1; i <= 10; i = i + 1)
    mostrar "ingrese dato"
    leer dato
    suma = suma + dato
```

Tres partes entre paréntesis:

1. **Inicialización:** `i = 1` — crea la variable de iteración con valor inicial
2. **Condición:** `i <= 10` — mientras esto sea verdad, sigue
3. **Incremento:** `i = i + 1` — qué hacer al final de cada iteración

**Cómo funciona paso a paso:**

```
1. Inicializa i (i = 1)
2. Evalúa condición (¿i <= 10?)
3. Si es verdadera, ejecuta el bloque
4. Aplica el incremento (i = i + 1)
5. Vuelve a 2
6. Cuando la condición sea falsa, termina
```

**Tarea para casa:** reescribir el mismo ejercicio usando `MIENTRAS` en vez del `PARA`. Y ver el **Video 6** sobre expresiones aritméticas y lógicas.

---

## Clase 5 — Martes 24/03/2026 — Continuación Práctico 2 *(Práctico, Oliver)*

Clase corta. Se siguieron resolviendo ejercicios del práctico 2 ya en pseudocódigo más estructurado.

### Ejercicio 3: Sumar valores con reglas especiales

Enunciado:
- Si se recibe **0**, termina la suma y se muestra el total
- Si se recibe **2**, se suma y luego el total acumulado se duplica
- Si recibe un **número negativo**, se ignora

**Solución con `do-while` (repetir-mientras):**

```
total = 0
suma = 0
REPETIR
    mostrar "ingrese número"
    leer número
    SI número > 0
        total = total + número
    SI número == 2
        total = total * 2
MIENTRAS número != 0
mostrar total
```

> "El repetir también está bien porque la condición no la pone al principio sino al final. Una cosa es un while y una cosa es un do while. Son cosas diferentes."

**Traducción:** Si la condición está al principio (`while`), tenés que pedir el primer dato *antes* del bucle. Si está al final (`do-while`), podés pedir el dato dentro del bucle desde la primera iteración.

> "Está bien que llegues a la solución, pero vayan siempre por la solución simple. No se compliquen. He visto mucha gente complicándose en el parcial cuando la solución era muy fácil."

### Ejercicio 4: Leer 5 valores y mostrar resultados

Enunciado: leer 5 valores y mostrar:
- Suma de los primeros dos
- Multiplicación del tercero y cuarto
- Promedio de los cinco
- Suma de los tres resultados anteriores

> "Si me dijeran leer N valores, haría un bucle. Pero como dice 5, acá no vale la pena complicarse — directamente leer valor1, valor2, valor3, valor4, valor5."

**Traducción:** Cuando la cantidad es fija y chica, no usés bucle — escribilo plano. La regla "no repetir código" no es absoluta: a veces el bucle es más complicado que el plano.

**El consejo clave de la clase:**

> "Vayan siempre por la solución simple. No se compliquen. Lo mismo, mi consejo es para el parcial."

---

## Clase 6 — Miércoles 25/03/2026 — Expresiones Aritméticas y Lógicas *(Teórico, Wagner)*

Esta clase es densa pero crucial. Acá se introducen el operador módulo, las tablas de verdad de las operaciones lógicas, y el patrón de validación de input.

### Ejercicio: Promedio sin contar el 99

Enunciado: leer números hasta que ingresen 99, calcular el promedio sin incluir el 99.

**Versión 1: con `MIENTRAS` clásico (la más limpia)**

```
suma = 0
canti = 0
mostrar "ingrese dato"
leer dato
MIENTRAS dato != 99
    suma = suma + dato
    canti = canti + 1
    mostrar "ingrese dato"
    leer dato
SI canti != 0
    promedio = suma / canti
    mostrar "el promedio es " + promedio
OTRO CASO
    mostrar "no se ingresaron datos"
```

> "¿Qué pasa si en la primera ejecución leo datos y me ingresa un 99? No hay promedio. Te va a dar error porque no se puede dividir entre 0."

**Traducción:** Hay que validar que `canti` no sea cero antes de dividir. Esto es **dividir por cero** — un error real que rompe el programa.

**Versión 2: con `do-while`** — pedís el dato adentro del bucle, pero tenés que validar adentro:

```
REPETIR
    mostrar "ingrese dato"
    leer dato
    SI dato != 99
        suma = suma + dato
        canti = canti + 1
MIENTRAS dato != 99
```

**Versión 3: forzando la primera iteración con un valor "trampa"**

```
dato = -1   // o cualquier valor != 99 para forzar entrar
MIENTRAS dato != 99
    mostrar "ingrese dato"
    leer dato
    SI dato != 99
        suma = suma + dato
        canti = canti + 1
```

> "No es que ninguna de estas tres sean mejores que otras. Las tres van a llegar a un mismo resultado. Es una forma diferente. Lo que tenés que considerar es que tenés que tener una condición dentro para que no te tome el 99."

### Ejercicio: Sueldos con bonificación por antigüedad

Enunciado: pedir sueldo y antigüedad. Si la antigüedad es entre 5 y 10 años, sube 10%. Si es mayor a 10, sube 20%. Sumar todos los sueldos hasta que ingresen sueldo = 0.

```
pagar = 0
mostrar "ingrese sueldo"
leer sueldo
MIENTRAS sueldo != 0
    mostrar "ingrese antigüedad"
    leer ant
    SI ant >= 5 Y ant <= 10
        sueldo = sueldo * 1.10
    SI ant > 10
        sueldo = sueldo * 1.20
    pagar = pagar + sueldo
    mostrar "ingrese sueldo"
    leer sueldo
mostrar "total a pagar: " + pagar
```

> "Ojo. Si yo le pongo 110, en realidad te faltó la división entre 100. Sería sueldo por 110 dividido 100. O directamente sueldo por 1.10."

**Traducción:** En programación, **el porcentaje no existe como operador**. `110%` no significa "el 110%". Tenés que multiplicar por `1.10` (que es 110/100).

**Detalle sobre condiciones compuestas:**

> "5 y 10 — no podemos poner todo con una sola variable. Son dos condiciones separadas. Sería: si ant >= 5 Y ant <= 10."

**Traducción:** En matemática escribís `5 ≤ ant ≤ 10`. En programación tenés que escribir las dos condiciones por separado unidas con `Y`.

### Validación de input negativo (patrón importante)

```
mostrar "ingrese sueldo"
leer sueldo
MIENTRAS sueldo < 0
    mostrar "valor negativo, ingrese de nuevo"
    leer sueldo
```

> "Cuando llegue a este punto, el sueldo que me ingresó ya es válido. Si me sigue ingresando negativos, se vuelve a repetir. Cuando sale el mientras, ya tengo el valor correcto."

**Traducción:** Patrón clásico de validación con `MIENTRAS` — pedís hasta que el dato cumpla la condición, y al salir tenés garantizado un dato válido.

### Expresiones aritméticas

Operadores:

| Operador | Qué hace |
|---|---|
| `+` | Suma |
| `-` | Resta |
| `*` | Multiplicación |
| `/` | División |
| `%` | **Módulo** (resto de la división) |

> "El módulo se escribe con el símbolo de porcentaje. Sirve mucho para saber si A es divisible entre B. Cuando es divisible, el resto es 0."

**Aplicación clave: detectar par o impar**

```
SI número % 2 == 0
    es par
SI no
    es impar
```

**Otra aplicación: extraer el último dígito**

```
último = número % 10
```

Si `número = 1234`, entonces `1234 % 10 = 4`. El módulo te da el último dígito.

### Expresiones lógicas — Tablas de Verdad

Las operaciones lógicas devuelven solo dos valores: **true** (verdadero) o **false** (falso).

**Operadores de comparación:** `>`, `<`, `>=`, `<=`, `==` (igual), `!=` (distinto)

**AND (y) — `&&`:**

| A | B | A AND B |
|---|---|---|
| F | F | F |
| F | V | F |
| V | F | F |
| V | V | **V** |

> "La única forma de que esta operación lógica me dé verdadero es que ambas condiciones sean verdaderas."

**OR (o) — `||`:**

| A | B | A OR B |
|---|---|---|
| F | F | F |
| F | V | V |
| V | F | V |
| V | V | V |

> "La única forma de que me dé falso es que ambas sean falsas. Con que una sola sea verdadera, es verdadero."

**NOT (negado) — `!`:**

| A | NOT A |
|---|---|
| F | V |
| V | F |

> "Si era falso, me da verdadero. Si era verdadero, me da falso."

### Tarea para casa

> "Quiero que hagan una infografía sobre JavaScript. Lo pueden hacer en pares si quieren. La idea es que todo lo importante de JavaScript lo veamos en una imagen."

---

# Parte III — JavaScript Real

## Clase 7 — Lunes 06/04/2026 — Ejercicios Avanzados + Introducción a JavaScript *(Teórico, Wagner)*

Clase larga. Mitad ejercicios complejos en pseudocódigo, mitad introducción a JavaScript a partir de las infografías que hicieron los estudiantes.

### Repaso con quiz de expresiones

Quiz interactivo sobre las tablas de verdad y precedencia de operadores. Conceptos clave:

> "B or not B — sin importar el valor que tenga B, siempre va a dar true."

**Traducción:** Si una de las dos partes del OR es siempre verdadera, todo el OR es siempre verdadero. Esto se llama **tautología**.

> "B and not B — siempre va a dar false."

**Traducción:** En el AND, si una parte es siempre falsa, todo el AND es siempre falso. Esto se llama **contradicción**.

**Precedencia de operadores aritméticos:**

```
6 + 4 * 2 = 14    (no 20)
```

> "Es igual que en matemática. Se separa por términos. El más separa términos. Tenemos 6 por un lado y 4 * 2 por otro."

### Ejercicio: Ordenar dos números y mostrar todos los del medio

Enunciado: leer A y B, ordenarlos si hace falta, mostrar todos los números entre ellos.

**Truco del swap (intercambio) con variable auxiliar:**

```
mostrar "ingrese A"
leer A
mostrar "ingrese B"
leer B

SI A > B
    C = B    // guardo B en una variable temporal
    B = A    // pongo A en B
    A = C    // pongo el B original (ahora en C) en A

PARA (i = A; i <= B; i = i + 1)
    mostrar i
```

**¿Por qué la variable C?**

> "Si ya pisás B con A, perdiste el valor anterior. Tenés que sobreescribir, pero usando C para no perderlo."

**Traducción:** Si querés intercambiar dos cajas, no podés hacerlo directamente — necesitás una caja vacía donde guardar una temporalmente. Es exactamente igual con variables.

### Ejercicio: Pirámide de asteriscos

Enunciado: leer N (positivo), mostrar N asteriscos.

```
leer N
PARA (i = 0; i < N; i = i + 1)
    mostrar "*"
```

> "Si empezaba con i = 0 uso menor. Si empezaba con i = 1 uso menor o igual. Cualquiera de las dos formas es válida."

### Ejercicio: Contar cuántos pares hay entre N números

```
leer N
canti = 0
PARA (i = 0; i < N; i = i + 1)
    leer dato
    SI dato % 2 == 0
        canti = canti + 1
mostrar "pares: " + canti
```

### Comparación: `==` vs `===` (la rareza de JavaScript)

> "Cuando es un solo signo igual es para asignar. Cuando son dos iguales es una comparación, si son iguales solo en valor. Y después tenemos el triple igual — se va a fijar si el valor es igual Y el tipo de dato es igual."

**Traducción:**

| Operador | Qué hace |
|---|---|
| `=` | **Asigna** un valor a una variable |
| `==` | Compara solo el **valor** (con conversión automática) |
| `===` | Compara **valor Y tipo** (estricto) |

**Ejemplos:**

```
"2" == 2     →  true   (mismo valor, distinto tipo, JS los convierte)
"2" === 2    →  false  (distinto tipo)
"2" + 2      →  "22"   (concatenación, no suma)
```

> "Cuando uno de los dos lados es un texto, le va a dar prioridad al texto. Al otro que no es texto, lo convierte en texto y los concatena."

**Traducción:** El `+` con strings es traicionero. `"2" + 2` no es 4 — es `"22"`. JavaScript convierte el número en texto y los pega.

### Ejercicio: Algoritmo de Fibonacci

> "La sucesión de Fibonacci empieza con 0 y 1. Cada número siguiente es la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13..."

$$a_0 = 0, \quad a_1 = 1, \quad a_n = a_{n-1} + a_{n-2}$$

**Que significa esto?**
- $a_0$ = el primer término (0)
- $a_1$ = el segundo término (1)
- $a_n$ = cualquier término después es la suma de los dos anteriores

**Solución en pseudocódigo:**

```
leer N
a = 0     // término actual a mostrar
b = 1     // término siguiente

PARA (i = 0; i < N; i = i + 1)
    mostrar a
    c = a + b   // calculo el próximo
    a = b       // muevo b a a
    b = c       // muevo c a b
```

> "Es como si yo estuviera parado así, ahora estoy parado así. Al siguiente voy a estar parado así. Y así sucesivamente."

**Traducción:** En cada iteración, las dos variables se "deslizan" un paso adelante en la secuencia. La variable `c` es el truco temporal para no perder el valor de `b` cuando lo movés.

### Ejercicio: Encontrar el máximo (con variable booleana)

Enunciado: leer datos hasta que ingresen 0, mostrar el máximo (excluyendo el 0). Si ingresaron solo 0, decir "sin datos".

> "Vamos a usar una variable booleana que no hemos usado. Vamos a ponerle hubo, igual a false. Es como una bandera, una lucecita."

```
hubo = false
max = MIN_VALUE
mostrar "ingrese dato"
leer dato
MIENTRAS dato != 0
    hubo = true        // levanto la bandera
    SI dato > max
        max = dato
    mostrar "ingrese dato"
    leer dato
SI hubo
    mostrar "el máximo es " + max
OTRO CASO
    mostrar "sin datos"
```

> "Cuando está en false, está abajo la bandera. Una vez que se pasa a true, la levanta. No debería volver a bajar."

**Traducción:** El patrón de **bandera booleana** sirve cuando querés saber si pasó algo *al menos una vez* en un bucle.

**El truco del MIN_VALUE:**

> "¿Qué pasa si ingreso todos valores negativos? Mi máximo va a ser cero. Voy a mostrar cero y está mal. Entonces, en vez de inicializar max = 0, lo inicializo en MIN_VALUE — el valor más chico que puede representar la máquina."

**Traducción:** Si arrancás `max = 0` y todos los datos son negativos, ningún dato va a ser mayor que 0 y el resultado queda mal. Inicializar en el "menos infinito" del lenguaje garantiza que el primer dato siempre va a ser mayor.

### Encontrar el mínimo (versión inversa)

```
min = MAX_VALUE
SI dato < min
    min = dato
```

Misma lógica al revés: empezás con el valor más grande posible para que el primer dato siempre sea menor.

### Introducción a JavaScript (con las infografías de los estudiantes)

Wagner pidió que hicieran infografías y las presentaron una por una. Los puntos clave que fueron saliendo:

#### Historia

- Creado por **Brendan Eich** en **Netscape** en **1995**
- Lo escribió en **10 días**
- Nombre original: **Mocha** → **LiveScript** → **JavaScript** (cambio de nombre por marketing, para aprovechar la popularidad de Java)
- **JavaScript ≠ Java** — solo comparten el nombre. No tienen relación técnica.

#### Características

| Característica | Significado |
|---|---|
| **Alto nivel** | Más cercano al lenguaje humano que a la máquina |
| **Interpretado** | Se traduce y ejecuta línea por línea, sin compilación previa |
| **Dinámicamente tipado** | No declarás el tipo de dato — la variable lo toma del valor que le ponés |
| **Multiplataforma** | Corre en cualquier sistema operativo (porque corre en el navegador) |
| **Multipanaritma** | Soporta orientado a objetos, funcional, imperativo |
| **ECMAScript** | Es el estándar oficial que define el núcleo del lenguaje |

#### Dónde corre

- **Frontend** — en el navegador (Chrome, Firefox, Safari…), nativamente
- **Backend** — en servidores con **Node.js**

> "Es de los más usados — lo usa el 98.9% de los sitios web del mundo."

#### Una página web tiene tres lenguajes

| Lenguaje | Función | Analogía con una casa |
|---|---|---|
| **HTML** | Estructura | Las paredes, los cimientos |
| **CSS** | Estilo (apariencia) | La pintura, la decoración |
| **JavaScript** | Comportamiento | La llave de luz, los electrodomésticos |

#### Sintaxis básica

```javascript
// Esto es un comentario de una línea

let edad = 20;        // variable que puede cambiar
const PI = 3.14;      // constante, no cambia
var algo = "viejo";   // forma vieja, no la usamos

if (edad >= 18) {
    console.log("mayor");
} else {
    console.log("menor");
}

for (let i = 0; i < 10; i++) {
    console.log(i);
}
```

> "El punto y coma en JavaScript no es obligatorio, pero les vamos a pedir siempre que lo hagan. ¿Por qué? Porque van a dar Java el semestre que viene y ahí sí es obligatorio."

#### Tipos de datos en JavaScript

| Tipo | Ejemplo |
|---|---|
| `string` | `"hola"` o `'hola'` |
| `number` | `42`, `3.14`, `Infinity`, `NaN` (uno solo, no entero/decimal por separado) |
| `boolean` | `true`, `false` |
| `array` | `[1, 2, 3]` |
| `object` | `{ nombre: "Juan", edad: 20 }` |
| `undefined` | variable sin valor asignado |
| `null` | ausencia explícita de valor |

> "Acá no hay un tipo para entero y otro para decimal. Es todo number. El decimal usa punto, no coma."

**Tarea:** ver el **Video 7 — Codificación básica de JavaScript**.

---

## Clase 8 — Martes 07/04/2026 — Práctico 4: Consola y Primer JavaScript Real *(Práctico, Oliver y Mauricio)*

La clase donde finalmente escribimos código JavaScript que la computadora ejecuta. Pasamos del pseudocódigo a la consola del navegador.

### Cómo abrir la consola del navegador

```
1. Abrir Chrome (o cualquier navegador)
2. Nueva pestaña en about:blank
3. Atajo:  Ctrl + Shift + I    (o también F12)
4. O por menú: Más herramientas → Herramientas para desarrolladores
5. Pestaña "Console"
```

### Quiz 1: La parte numérica de JavaScript

Resolvieron un quiz en grupos sobre cosas raras de JavaScript con números:

**División por cero (no da error):**

```javascript
1 / 0      →  Infinity
-3 / 0     →  -Infinity
0 / 0      →  NaN          // Not a Number
```

> "La división por cero matemáticamente no tiene resultado, entonces le ponen NaN. Por convención de JavaScript."

**Traducción:** A diferencia de otros lenguajes, JavaScript no rompe con división por cero — devuelve infinito o `NaN`.

**`isNaN()` — para chequear si algo es NaN:**

```javascript
isNaN(NaN)        →  true
isNaN("hola")     →  true
isNaN(42)         →  false
```

**Constantes de la clase Number:**

```javascript
Number.MAX_VALUE          // ≈ 1.79 × 10^308 — el mayor número representable
Number.MIN_VALUE          // ≈ 5 × 10^-324 — el menor positivo cerca de 0 (¡no es negativo!)
Number.MAX_SAFE_INTEGER   // el mayor entero "seguro" para operar
Number.MIN_SAFE_INTEGER   // el menor entero seguro (este sí es negativo)
```

> "El MIN_VALUE no es un número negativo. Es un número bien cercano a cero, pero no llega a cero. Lo más chico positivo que puedo representar."

**Traducción:** Cuidado con `MIN_VALUE` vs `MIN_SAFE_INTEGER`. Cuando querés inicializar una variable para encontrar el máximo, usá `MIN_SAFE_INTEGER` (el negativo), no `MIN_VALUE` (el positivo cerca de 0).

**Math — la otra clase con constantes y métodos útiles:**

```javascript
Math.PI               // 3.14159...
Math.pow(2, 8)        // 256 — potencia
2 ** 8                // 256 — operador alternativo
Math.sqrt(16)         // 4 — raíz cuadrada
Math.abs(-5)          // 5 — valor absoluto
```

**Trampa de la concatenación:**

```javascript
let suma = 5;
let m = 10;
console.log("suma " + suma + m);    // "suma 510"  ❌
console.log("suma " + (suma + m));  // "suma 15"   ✓
```

> "El operador más, cuando estás trabajando con strings, no suma — concatena. Primero va a resolver suma+m de izquierda a derecha. Como suma es texto, le va a apendear el 5, y por último apendear el 10."

**Traducción:** Sin paréntesis, `"suma " + 5 + 10` se evalúa como `"suma 5" + 10` = `"suma 510"`. Con paréntesis, fuerza a que la suma numérica se haga primero.

### Quiz 2: La parte de strings

**Propiedades y métodos básicos de strings:**

```javascript
"hola".length              // 4 — cantidad de caracteres
"hola".toUpperCase()       // "HOLA"
"hola".toLowerCase()       // "hola"
"hola".charAt(2)           // "l" — el carácter en posición 2
```

> "JavaScript maneja los strings como una lista de caracteres. Y siempre empiezan con índice 0."

**Posiciones de "hola":**

| Posición | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Carácter | h | o | l | a |

> "Como estamos accediendo a la 2, siempre nos va a decir la L."

**Funciones de conversión:**

```javascript
parseInt("124")         // 124 — convierte texto a entero
parseFloat("3.14")      // 3.14 — convierte texto a decimal
typeof "hola"           // "string" — devuelve el tipo
typeof 42               // "number"
```

> "Tomen en cuenta que cualquier dato que tomen por consola que pide al usuario, siempre lo van a tomar como una cadena de caracteres. Si son números y los quieren operar, los tienen que parsear. No queda otra."

**Traducción:** Cuando el usuario te ingresa "5", para JavaScript es el texto `"5"`, no el número `5`. Si lo querés sumar, hay que pasarlo por `parseInt()` primero.

### Brainstorm: ¿cómo resolverías un problema desconocido?

Hicieron un ejercicio de pizarra colaborativa: ¿cómo harías para aprender a usar un combobox en JavaScript que no sabés cómo se hace?

Ideas que salieron:

| Estrategia | Cuándo usarla |
|---|---|
| Buscar en Google / documentación | Siempre primero |
| Preguntarle a ChatGPT (citando que lo usaste) | Para explicaciones rápidas |
| Buscar tutorial en YouTube | Para conceptos visuales |
| Consultar al profesor o ayudantía | Cuando ya intentaste solo |
| Preguntarle a un compañero más avanzado | Cuando hay alguien cerca |
| Tirarte a probar código | Para aprender haciendo |
| Revisar materiales de la cátedra | Cuando es algo del curso |

**Lo mismo aplicado al obligatorio:**

| Estrategia | Para qué |
|---|---|
| Mejorar los datos de prueba | Encontrar bugs antes de entregar |
| Mejorar la documentación | Que el corrector entienda fácil |
| Chequear estándares (camelCase, mnemotécnico, ;) | No perder puntos por detalles |
| Revisar la rúbrica | Sabes exactamente sobre qué te van a calificar |
| Hablar con estudiantes que ya cursaron | Tener visión de qué se espera |
| Pedir segunda opinión a la cátedra | Antes de la entrega final |

### Snippets — la herramienta del día

> "Vamos a ir a la parte de Sources, y ahí tenemos snippets. Le pueden dar a 'new snippet', le ponemos un nombre, y la idea es que a partir de ahora vayamos creando snippets para ir trabajando justamente ese código."

**Traducción:** Los **snippets** son archivos pequeños de JavaScript que vivís dentro del navegador. Los escribís en el editor del navegador, los corrés con `Ctrl + Enter` (o el botón Run), y ves el resultado en la consola.

```
Chrome → F12 → Sources → Snippets → New snippet
```

### Las tres funciones para interactuar con el usuario

```javascript
let edad = prompt("¿Cuántos años tenés?");   // pedir input al usuario
console.log("Hola " + edad);                  // mostrar en consola
alert("El área del triángulo es " + area);    // mostrar en pop-up
```

**`prompt()`** es la primera forma real de pedir un dato al usuario — equivale al "leer dato" del pseudocódigo. Devuelve siempre un string.

### Ejercicio 1 (resuelto entre todos): área de un triángulo

Enunciado: pedir la base y la altura, mostrar el área. Si se lee 6 y 2, mostrar 6 (porque base × altura / 2).

```javascript
let base = parseInt(prompt("Ingrese base"));
let altura = parseInt(prompt("Ingrese altura"));
let area = base * altura / 2;
alert("El área del triángulo es " + area);
```

**Línea por línea:**

- `let base = parseInt(prompt("Ingrese base"));` — el `prompt` muestra una ventanita pidiendo la base. El usuario escribe "6". Eso llega como el string `"6"`. El `parseInt` lo convierte al número `6`. El `let base =` lo guarda en una variable nueva llamada `base`.
- `let altura = parseInt(prompt("Ingrese altura"));` — exactamente lo mismo para la altura.
- `let area = base * altura / 2;` — calcula y guarda en una nueva variable `area`. Por precedencia de operadores, `*` y `/` se ejecutan de izquierda a derecha: primero `base * altura`, después dividido 2.
- `alert("El área del triángulo es " + area);` — muestra un pop-up. Acá `+` está concatenando un string con un número, JavaScript convierte el número a string automáticamente.

> "En JavaScript no es obligatorio el punto y coma, pero les vamos a pedir siempre que lo hagan, por un tema de que cuando ya pasen a Java va a ser obligatorio."

### Ejercicios para hacer en clase

- **Ejercicio 2:** ingresar 3 valores enteros y mostrar el menor
- **Ejercicio 3:** ingresar 3 datos y mostrar la suma de sus valores absolutos (ej: -1, 5, -30 → 36)
- **Ejercicio 4:** pedir un número N y mostrar la suma de todos los impares múltiplos de 3 entre 1 y N

**Solución del ejercicio 2 (mínimo de tres):**

```javascript
let min = Number.MAX_SAFE_INTEGER;
for (let i = 1; i <= 3; i = i + 1) {
    let valor = parseInt(prompt("Ingrese valor"));
    if (valor < min) {
        min = valor;
    }
}
alert("el mínimo es " + min);
```

**Solución del ejercicio 3 (suma de valores absolutos):**

```javascript
let n1 = parseInt(prompt("Ingrese 1"));
let n2 = parseInt(prompt("Ingrese 2"));
let n3 = parseInt(prompt("Ingrese 3"));
let suma = Math.abs(n1) + Math.abs(n2) + Math.abs(n3);
alert("la suma de absolutos es " + suma);
```

### Tarea para la próxima

> "Les queda de deberes si quieren seguir practicando. Están todos los ejercicios de la parte de variables que hicimos en pseudocódigo — los pueden pasar a JavaScript. Y continuar con el práctico 5."

**Lo que viene:** funciones y strings — "lo único que vamos a hacer es hacer un wrap de todo este código y lo vamos a poner en funciones".

---

# Síntesis de la Evolución del Curso

## Cómo cambió el "vocabulario" entre las clases

| Concepto | Cómo lo llamábamos al principio | Cómo lo llamamos ahora |
|---|---|---|
| Repetir un bloque N veces | `REPETIR X VECES` | `PARA (i=1; i<=N; i++)` → `for` |
| Repetir mientras se cumple una condición | `MIENTRAS condición` | `while (condición)` |
| Tomar una decisión | `SI condición / OTRO CASO` | `if / else` |
| Mostrar al usuario | `mostrar` | `console.log()` o `alert()` |
| Pedir un dato al usuario | `leer` | `prompt()` |
| Guardar un valor en memoria | "crear variable" | `let nombre = valor` |
| Comparar igualdad | `==` | `===` (estricto) |
| Texto | `"comillas"` | `"comillas"` o `'comillas'` |

## Patrones que ya sabemos identificar

| Patrón | Cuándo usarlo | Pseudocódigo típico |
|---|---|---|
| **Acumulador** | Sumar N valores | `suma = suma + dato` dentro de un bucle |
| **Contador** | Contar cuántos cumplen una condición | `canti = canti + 1` dentro de un `SI` |
| **Bandera (booleana)** | Saber si pasó algo al menos una vez | `hubo = false` → `hubo = true` cuando pasa |
| **Buscar máximo/mínimo** | Encontrar el extremo de una lista | Inicializar en el extremo opuesto, comparar y sustituir |
| **Validar input** | Asegurar que el usuario ingresa un valor válido | `MIENTRAS dato no es válido, pedir de nuevo` |
| **Swap (intercambio)** | Cambiar valores entre dos variables | Necesitás una variable temporal |
| **Forzar primera iteración** | Cuando querés un do-while pero usás while | Inicializar la condición con un valor "trampa" |

---

## Definiciones Consolidadas para el Parcial

### Sobre fundamentos

**Sistema:** conjunto de elementos organizados para llevar a cabo algún método, procedimiento o control mediante el procesamiento de la información.

**Hardware:** elementos físicos. Se clasifica en fundamental/accesorio y entrada/salida/entrada-salida.

**Software:** los programas. Se clasifica en general/específico y base/aplicación.

**Programa:** el arte de dar comandos a algo que puede ser ejecutado después.

**Ingeniería de Software:** aplicación de un enfoque sistemático, disciplinado y cuantificable al desarrollo, operación y mantenimiento del software.

**Lenguaje compilado:** lenguaje de alto nivel que traduce todo el código a lenguaje máquina antes de ejecutarlo.

**Lenguaje interpretado:** lenguaje de alto nivel que traduce y ejecuta el código línea por línea al mismo tiempo. JavaScript es interpretado.

**Alpha testing:** pruebas realizadas por el equipo de desarrollo.

**Beta testing:** pruebas realizadas con colaboración del cliente o usuarios seleccionados.

### Sobre pensamiento computacional

**Pensamiento computacional:** habilidad de descomponer problemas, reconocer patrones, abstraer lo esencial y diseñar algoritmos para resolverlos.

**Descomposición:** dividir un problema complejo en partes más pequeñas hasta que cada parte tenga una solución obvia.

**Reconocimiento de patrones:** identificar similitudes, repeticiones o regularidades en un problema.

**Abstracción:** quedarse con lo esencial e ignorar los detalles irrelevantes para el problema actual.

**Algoritmo:** secuencia ordenada, finita, precisa, efectiva, con entrada y salida, de pasos para resolver un tipo específico de problema.

### Sobre estructuras de control

**Secuencia:** estructura que ejecuta pasos uno después del otro, en orden, sin condiciones.

**Decisión (SI):** evalúa una condición una sola vez. Si es verdadera ejecuta un bloque, si es falsa lo saltea (o ejecuta el bloque OTRO CASO). Nunca se ejecutan ambos.

**Iteración MIENTRAS (while):** evalúa la condición antes de cada ejecución. Puede ejecutarse cero veces si la condición es falsa desde el inicio.

**Iteración REPETIR…MIENTRAS (do-while):** ejecuta el bloque primero y evalúa la condición después. Garantiza al menos una ejecución.

**PARA (for):** estructura de iteración con tres partes: inicialización, condición y paso. Se usa cuando se conoce o se controla explícitamente el número de iteraciones.

**Loop infinito:** error donde la condición de un bucle nunca se vuelve falsa y el programa nunca termina.

**Pseudocódigo:** descripción de un algoritmo en lenguaje natural usando indentación para mostrar la estructura lógica.

### Sobre variables y expresiones

**Variable:** lugar en la memoria RAM con un nombre, donde se guarda un dato. Es volátil — se pierde al apagar la computadora.

**camelCase:** convención de nombres donde la primera palabra va en minúscula y cada palabra siguiente arranca con mayúscula. Ej: `puntajeMaximo`.

**Mnemotécnico:** característica de un nombre que permite entender qué guarda solo con leerlo.

**Tipo de dato:** clase de información que puede almacenar una variable (entero, decimal, texto, booleano…). En JavaScript no se declara — se infiere del valor.

**Asignación (`=`):** operación que guarda en una variable el resultado de la expresión a la derecha del signo. El valor anterior se pierde.

**Operador módulo (`%`):** devuelve el resto de una división. Útil para detectar pares (`x % 2 == 0`).

**Operación lógica:** expresión que devuelve solo true o false. Las tres principales son AND (`&&`), OR (`||`) y NOT (`!`).

**Variable booleana:** variable que solo puede tomar dos valores, true o false. Se usa como bandera.

### Sobre JavaScript

**JavaScript:** lenguaje de alto nivel, interpretado, dinámicamente tipado, multiplataforma, multipanaritma. Creado por Brendan Eich en Netscape en 1995, en 10 días.

**ECMAScript:** estándar oficial que define el núcleo de JavaScript. Permite que distintos navegadores ejecuten el mismo código.

**`==` (doble igual):** compara solo el valor, con conversión automática de tipos. `"2" == 2` es `true`.

**`===` (triple igual):** compara valor y tipo. `"2" === 2` es `false`.

**`prompt()`:** función que muestra un pop-up pidiendo input al usuario. Devuelve siempre un string.

**`parseInt()`:** función que convierte un string a número entero.

**`alert()`:** función que muestra un pop-up con un mensaje.

**`console.log()`:** función que escribe un mensaje en la consola del navegador.

**Snippet:** archivo de código pequeño que se crea dentro de las herramientas para desarrolladores del navegador, en la pestaña Sources.

---

## Posibles Preguntas para el Parcial

**¿Cuál es la diferencia entre un lenguaje compilado y uno interpretado?**
El compilado traduce todo el código a lenguaje máquina antes de ejecutarlo. El interpretado traduce y ejecuta línea por línea durante la ejecución. JavaScript es interpretado.

**¿Cuáles son los cuatro pilares del pensamiento computacional?**
Descomposición, reconocimiento de patrones, abstracción y diseño de algoritmos.

**¿Cuáles son las cinco propiedades obligatorias de un algoritmo?**
Finito, tiene entrada, tiene salida, efectivo y preciso.

**¿Qué diferencia hay entre SI y MIENTRAS?**
El SI evalúa la condición una sola vez. El MIENTRAS la evalúa repetidamente hasta que sea falsa. El SI puede ejecutar el bloque cero o una vez; el MIENTRAS puede ejecutarlo cero o muchas veces.

**¿Qué diferencia hay entre MIENTRAS y REPETIR…MIENTRAS?**
MIENTRAS evalúa la condición antes de ejecutar el bloque — puede ejecutarse cero veces. REPETIR…MIENTRAS ejecuta el bloque primero y evalúa la condición después — siempre se ejecuta al menos una vez.

**¿Por qué es peligroso el loop infinito y cómo se evita?**
El loop infinito ocurre cuando la condición del MIENTRAS nunca se vuelve falsa y el programa corre para siempre. Se evita asegurando que dentro del bucle exista código que en algún momento modifique la condición hacia falso.

**¿Qué garantiza saber cuando un MIENTRAS termina?**
Que la condición de continuación se volvió falsa. Es el truco que se usa en problemas como el cruce de calle: al salir del bucle, sabés con certeza que la luz está en verde.

**¿Qué es el pseudocódigo y para qué sirve?**
Es la descripción de un algoritmo en lenguaje natural con la estructura lógica del programa pero sin la sintaxis exacta. Sirve como paso intermedio entre pensar el problema y escribir código real.

**¿Qué es una variable y cómo se la nombra?**
Es un lugar en la memoria RAM con un nombre, donde se guarda un dato. Se nombra en camelCase y de forma mnemotécnica — el nombre tiene que decir qué guarda. Ej: `puntajeMaximo`, no `pm`.

**¿Cómo se detecta si un número es par usando el operador módulo?**
`numero % 2 == 0`. Si el resto de dividir entre 2 es cero, el número es par. Si es uno, es impar.

**¿Cuándo el AND da verdadero?**
Solo cuando ambas condiciones son verdaderas. En cualquier otro caso da falso.

**¿Cuándo el OR da falso?**
Solo cuando ambas condiciones son falsas. Con que una sola sea verdadera, el OR da verdadero.

**¿Por qué `"2" == 2` da verdadero pero `"2" === 2` da falso en JavaScript?**
Porque `==` compara solo el valor (y JavaScript convierte automáticamente los tipos), pero `===` compara también el tipo de dato. Uno es string y el otro es number.

**¿Por qué `"suma " + 5 + 10` da `"suma 510"` y no `"suma 15"`?**
Porque el operador `+`, cuando trabaja con strings, concatena en vez de sumar. Como JavaScript evalúa de izquierda a derecha, primero une `"suma " + 5` formando `"suma 5"`, y después le pega el `10` formando `"suma 510"`. Para sumar, hay que usar paréntesis: `"suma " + (5 + 10)`.

**¿Por qué `prompt()` siempre devuelve un string, incluso si el usuario escribió un número?**
Porque la entrada del usuario por consola es siempre texto. Si querés operar matemáticamente con ese valor, hay que pasarlo por `parseInt()` o `parseFloat()` primero, o si no JavaScript lo va a tratar como cadena y `+` va a concatenar en vez de sumar.

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

**Escribir en pseudocódigo un algoritmo para encontrar el máximo de una serie de números que se ingresan hasta que se ingrese un 0.**

```
hubo = false
max = MIN_SAFE_INTEGER
mostrar "ingrese dato"
leer dato
MIENTRAS dato != 0
    hubo = true
    SI dato > max
        max = dato
    mostrar "ingrese dato"
    leer dato
SI hubo
    mostrar "el máximo es " + max
OTRO CASO
    mostrar "no se ingresaron datos"
```

**¿Para qué sirve aprender a programar si la IA ya programa por vos?**
Porque la IA es más efectiva para quien entiende el código que genera. Un programador que sabe leer, verificar y corregir código puede usar la IA como multiplicador. Quien no sabe programar depende ciegamente del output sin poder evaluar su calidad. Como dijeron los profes: los programadores de COBOL que más le tenían miedo a la IA son los que hoy más la están usando, porque entienden el código.

---

## Lo Que Viene (Próximas Clases)

- **Funciones y strings** — "wrap" del código que ya escribimos en funciones reutilizables
- **Más práctica con snippets** en el navegador
- Continuación del **práctico 5** con ejercicios en JavaScript real
- **Parcial 1: 28 de abril** — todo el contenido visto hasta ese momento

---

*Documento generado a partir del análisis de las transcripciones de las clases 1 a 8 (16/03/2026 al 07/04/2026) — Programación 1, ORT Uruguay, Ingeniería en Sistemas, 1er semestre 2026. Profesores: Gonzalo Wagner (teórico), Sergio Cortinas y Andrés Mauricio Repeto Ferrero (práctico).*
