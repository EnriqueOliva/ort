# Explicación de Temas - Clase del 26-08-2025

## Repaso de la Clase Anterior

### El problema de estimar distribuciones

El profesor comenzó recordando lo que habían visto la clase pasada sobre estimación de distribuciones. Habían trabajado con un dataset de tenis y vieron cómo estimar probabilidades usando tablas de frecuencia.

El gran problema que surgió fue: **cuando tengo muchas variables (dimensiones), estimar todas las combinaciones posibles se vuelve imposible**. Como dijo el profesor: "cuando yo tengo que empezar a hacer todas las casuísticas de combinaciones de valores posibles, es demasiado".

Por ejemplo, si tienes 10 variables que pueden ser sí o no, tendrías que estimar probabilidades para 2^10 = 1024 combinaciones diferentes. ¡Es muchísimo!

## La Regla del Producto

### Concepto básico

La regla del producto es una forma de calcular la probabilidad de que pasen varias cosas juntas. El profesor la escribió así:

**P(X, Y) = P(X) × P(Y|X)**

¿Qué significa esto en español simple?
- P(X, Y) = La probabilidad de que pasen X e Y juntas
- P(X) = La probabilidad de que pase X
- P(Y|X) = La probabilidad de que pase Y, dado que ya pasó X

### Ejemplo práctico

Imagínate que quieres saber la probabilidad de que llueva Y haga frío mañana:
- Primero calculas la probabilidad de que llueva
- Luego calculas la probabilidad de que haga frío DADO que está lloviendo
- Multiplicas ambas y obtienes la probabilidad conjunta

### Generalización para múltiples variables

El profesor mostró que esto se puede extender a muchas variables. Para tres variables sería:

**P(X, Y, Z) = P(X) × P(Y|X) × P(Z|X,Y)**

Y así sucesivamente. Como explicó: "esto se puede básicamente componer aplicando esta regla varias veces".

## Independencia Estadística

### ¿Qué significa que dos cosas sean independientes?

El profesor fue muy claro con esto: **dos eventos son independientes cuando saber que pasó uno no cambia la probabilidad del otro**.

Matemáticamente, X e Y son independientes si:
**P(X, Y) = P(X) × P(Y)**

Como explicó el profesor: "la probabilidad de Y dado X no cambia... saber que pasó X no me cambia la probabilidad de Y".

### Ejemplo cotidiano

Si tiras una moneda y luego tiras un dado:
- El resultado de la moneda NO afecta el resultado del dado
- Son eventos independientes
- P(cara y sacar 6) = P(cara) × P(sacar 6) = 0.5 × 1/6

### La ventaja práctica

Si las variables son independientes, **los cálculos se simplifican muchísimo**. Como dijo el profesor: "asumir independencia me abarata las estimaciones".

En lugar de tener que estimar probabilidades para todas las combinaciones, solo necesitas estimar cada variable por separado.

## Independencia Condicional

### Un punto intermedio

Este es un concepto más sutil que el profesor explicó cuidadosamente. La independencia condicional es cuando **dos variables son independientes DADO que conocemos el valor de una tercera**.

El profesor lo escribió así: X es condicionalmente independiente de Z dado Y si:
**P(X, Z|Y) = P(X|Y) × P(Z|Y)**

### ¿Qué significa en la práctica?

Como explicó el profesor: "es un punto intermedio... me permite asumir un fenómeno más complejo y menos complejo a la hora de hablar de la probabilidad conjunta".

Por ejemplo, imagina:
- X = si estudias
- Y = si apruebas el examen
- Z = si tus padres están contentos

X y Z podrían ser independientes SI YA SABEMOS si aprobaste (Y). Es decir, si ya sabemos que aprobaste, el hecho de que hayas estudiado no cambia adicionalmente la probabilidad de que tus padres estén contentos.

### La cadena de Markov

El profesor mencionó un caso especial importante: cuando cada variable solo depende de la anterior. Como dijo: "la probabilidad de un evento siguiente depende solo del inmediato anterior".

Esto simplifica mucho los cálculos porque en lugar de que cada variable dependa de TODAS las anteriores, solo depende de UNA.

## Redes Bayesianas (Bayesian Networks)

### ¿Qué son?

El profesor las describió como **"un grafo dirigido acíclico"** donde:
- Los **nodos son variables aleatorias** (cosas que pueden pasar o no)
- Los **arcos indican dependencia** entre las variables

Como explicó: "la Bayesian network es una sintaxis para describir relaciones entre variables aleatorias".

### ¿Para qué sirven?

Las redes bayesianas nos permiten representar gráficamente qué variables dependen de cuáles. El profesor dio tres casos extremos:

1. **Sin arcos**: Todas las variables son independientes (caso más simple)
2. **Todos los arcos posibles**: Todas dependen de todas (caso más complejo)
3. **Algunos arcos**: Situación intermedia y más realista

## Ejemplo de la Alarma de Sally

### El escenario

El profesor presentó un ejemplo clásico con estas variables:
- **B (Burglar)**: Si entra un ladrón
- **E (Earthquake)**: Si hay un terremoto
- **A (Alarm)**: Si suena la alarma
- **R (Radio)**: Si escuchas sobre el terremoto en la radio
- **J (John calls)**: Si John llama a Sally
- **M (Mary calls)**: Si Mary llama a Sally

### Las relaciones

El profesor dibujó las conexiones:
- Tanto el ladrón como el terremoto pueden hacer sonar la alarma
- Si hay terremoto, lo escucharás en la radio
- Si suena la alarma, John y Mary podrían llamar

### Lo interesante del ejemplo

El profesor notó detalles divertidos: "John definitivamente quiere mucho más a Sally que Mary, porque si suena la alarma, John le avisa más seguido que Mary".

Lo importante es que **cada flecha representa una dependencia directa**, y podemos calcular la probabilidad conjunta de todos estos eventos usando las conexiones del grafo.

## Aplicación a Imágenes (MNIST)

### El problema real

El profesor conectó todo esto con un problema práctico: generar imágenes de números escritos a mano (como los del dataset MNIST de 28×28 píxeles).

### Modelando píxeles como variables

La idea clave: **cada píxel es una variable aleatoria** que puede estar prendido (1) o apagado (0).

Como explicó: "cada píxel es una variable aleatoria que se distribuye de acuerdo a una Bernoulli". Una Bernoulli es simplemente una variable que puede ser 0 o 1 con cierta probabilidad.

### El problema de la explosión de parámetros

Si tenemos 28×28 = 784 píxeles y queremos modelar todas las dependencias:

- **Primer píxel**: 1 parámetro
- **Segundo píxel** (depende del primero): 2 parámetros
- **Tercer píxel** (depende de los dos anteriores): 4 parámetros
- Y así sucesivamente...

El profesor mostró que esto crece exponencialmente: **2^784 parámetros**. Como dijo: "una locura... una explosión de parámetros para estimar".

## Las Estrategias de Simplificación

### Tres opciones que presentó el profesor

1. **Todos independientes**:
   - Solo necesitas 784 parámetros (uno por píxel)
   - "Muy poco realista" según el profesor
   - Generaría solo ruido aleatorio

2. **Independencia condicional** (cada píxel depende solo del anterior):
   - Necesitas 2×784 parámetros
   - "Un poco más realista, pero tampoco es que sea híper realista"

3. **Red Bayesiana arbitraria**:
   - Diseñas qué píxeles dependen de cuáles
   - Punto intermedio entre simplicidad y realismo

### La conclusión del profesor

"El problema es: yo tengo que estimar de algún modo... modelo el problema como un conjunto de variables y tengo que decidir qué dependencias hay entre ellas. En el caso más general sin asumir independencias, la estimación es intratable".

## Conceptos Clave para Recordar

### El trade-off fundamental

El profesor enfatizó constantemente este dilema:
- **Más independencias** = Más fácil de calcular pero menos realista
- **Menos independencias** = Más difícil de calcular pero más realista

### La importancia práctica

Todo esto no es solo teoría. Como mencionó el profesor sobre los modelos de lenguaje modernos: "los grandes modelos de lenguaje hacen eso... condicionan el contexto pero el contexto es acotado. No pueden condicionar a más de n mil palabras hacia atrás".

### El proceso estocástico

El profesor recalcó que estos modelos tienen variabilidad incorporada. No es determinístico - hay aleatoriedad involucrada. Por eso cuando le pides lo mismo dos veces a un modelo generativo, te da respuestas diferentes.

## Resumen Simple

Si tuvieras que explicárselo a alguien que no sabe nada:

**Las Redes Bayesianas son como mapas de influencias**: te dicen qué cosas afectan a qué otras cosas. Si sabes que está lloviendo, es más probable que la gente lleve paraguas. Si suena una alarma, es más probable que sea por un ladrón o un terremoto.

El gran problema es que cuando tienes muchas cosas que se afectan entre sí, los cálculos se vuelven imposibles. Por eso necesitamos hacer simplificaciones inteligentes - asumir que algunas cosas son independientes o que solo dependen de pocas otras cosas.

Es como tratar de predecir el tráfico: no puedes considerar cada auto individualmente y cómo afecta a todos los demás. Necesitas simplificar y decir "el tráfico en esta calle solo depende del tráfico en las calles conectadas directamente".

La magia está en encontrar el balance correcto entre simplicidad (para poder calcularlo) y realismo (para que sea útil).

## ¿Es necesario saberse todas las fórmulas?

El profesor fue muy claro sobre esto: **NO es necesario memorizar todas las fórmulas matemáticas**.

Como él mismo dijo: "Esto no es un curso de estadística. No soy experto en estadística, pero tenemos que ir hablando algunas de estas bases porque nos van a dar las herramientas para poder describir estos fenómenos".

### Lo que SÍ es importante:

- **Entender los conceptos**: Qué es una probabilidad conjunta, qué es independencia condicional
- **Poder aplicarlos en código**: Los prácticos están diseñados para familiarizarte con estos conceptos de forma práctica
- **Asociarlo a ejemplos reales**: Por eso usan el dataset de tenis y luego imágenes

### Lo que NO es necesario:

- Memorizar fórmulas
- Hacer demostraciones matemáticas formales
- Ser experto en estadística

Como advirtió el profesor: "Si quieren pedirle a ChatGPT que lo haga bien, lo va a hacer seguramente bien, pero después no van a tener los conceptos básicos en el teórico y capaz que después se pierden un poco más".

La idea es **entender conceptualmente qué hacen las herramientas**, no derivar todas las matemáticas desde cero.

---

## Definiciones para el Parcial

### Reglas de Probabilidad

**Regla del Producto:** Forma de calcular la probabilidad de que pasen varias cosas juntas: P(X, Y) = P(X) × P(Y|X); se puede extender a múltiples variables: P(X, Y, Z) = P(X) × P(Y|X) × P(Z|X,Y).

**Probabilidad Conjunta P(X, Y):** La probabilidad de que ocurran X e Y juntas; sin la regla del producto, estimar todas las combinaciones posibles crece exponencialmente y se vuelve intratable.

**Probabilidad Condicional P(Y|X):** La probabilidad de que ocurra Y dado que ya sabemos que ocurrió X; es la base de los modelos autorregresivos.

**Marginalización (Regla de la Suma):** Proceso de "eliminar" una variable que no interesa sumando sobre todos sus posibles valores: P(X) = Σ P(X, Y=yi); permite obtener la probabilidad de X sin importar el valor de Y.

### Independencia

**Independencia Estadística:** Dos eventos X e Y son independientes cuando saber que pasó uno no cambia la probabilidad del otro; matemáticamente P(X, Y) = P(X) × P(Y); simplifica enormemente los cálculos porque no hay que considerar interacciones.

**Independencia Condicional:** X y Z son condicionalmente independientes dado Y si P(X, Z|Y) = P(X|Y) × P(Z|Y); es un punto intermedio que permite modelar fenómenos más complejos sin la explosión combinatoria de la dependencia total.

**Cadena de Markov:** Caso especial donde cada variable solo depende de la inmediata anterior, no de toda la historia; P(Xₙ|X₁,...,Xₙ₋₁) = P(Xₙ|Xₙ₋₁); simplifica mucho los cálculos porque limita las dependencias.

### Redes Bayesianas

**Red Bayesiana (Bayesian Network):** Grafo dirigido acíclico donde los nodos son variables aleatorias y los arcos indican dependencia entre ellas; es una sintaxis visual para describir qué variables afectan a cuáles.

**Grafo Dirigido Acíclico (DAG):** Estructura de nodos y flechas donde las flechas tienen dirección y no hay ciclos (no puedes volver al punto de partida siguiendo las flechas); es la estructura matemática de las redes bayesianas.

### Distribuciones

**Distribución de Bernoulli:** Distribución de probabilidad más simple, modela algo con solo dos resultados posibles (cara/cruz, sí/no, 0/1); tiene un único parámetro θ que indica la probabilidad del resultado "1".

### Problemas Computacionales

**Explosión de Parámetros:** Problema que surge cuando tenemos muchas variables dependientes: el número de parámetros crece exponencialmente (2^n para n variables binarias); hace imposible estimar todas las combinaciones.

**Trade-off Independencias:** Dilema fundamental: más independencias = más fácil de calcular pero menos realista; menos independencias = más difícil de calcular pero más realista; hay que encontrar un balance.

### Tabla Comparativa

| Asunción | Parámetros necesarios | Realismo |
|----------|----------------------|----------|
| Todas independientes | n (lineal) | Muy bajo |
| Dependencia total | 2^n (exponencial) | Alto pero intratable |
| Independencia condicional | Intermedio | Balance útil |