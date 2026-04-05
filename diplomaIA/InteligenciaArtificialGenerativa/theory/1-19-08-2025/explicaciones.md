# Explicación de Temas - Clase del 19-08-2025

## Introducción a Modelos Generativos

### ¿Qué son los modelos generativos?

Imagínate que tienes un sistema (como ChatGPT) que es capaz de crear cosas nuevas. El profesor lo explicó de manera muy sencilla: **un modelo generativo es un sistema que puede generar datos nuevos a partir de un input**.

Cuando le escribes algo a ChatGPT, por ejemplo "escríbeme un poema", el modelo **genera** texto nuevo que no existía antes. No está copiando y pegando de algún lugar - está creando algo original basándose en lo que aprendió.

### El concepto básico

El profesor usó un ejemplo práctico muy claro: le pidió a ChatGPT que compusiera "un blues de 12 compases en mi menor". Lo interesante es que cuando hizo el mismo pedido dos veces, ChatGPT generó **dos blues diferentes**. ¿Por qué? Porque estos modelos tienen algo llamado **variabilidad** - no dan siempre la misma respuesta.

Esto es fundamental: **los modelos generativos no memorizan y repiten**, sino que **crean datos nuevos** cada vez que les pides algo.

## Diferencia con Modelos Discriminativos

Esta es una distinción súper importante que el profesor explicó con un ejemplo médico muy claro:

### Modelos Discriminativos (Clasificadores)
Imagínate un sistema que mira una radiografía y tiene que decir si hay un tumor o no. Este es un **clasificador** o modelo discriminativo. Su trabajo es:
- Mirar una imagen médica
- Decidir: "tumor" o "no tumor"
- **SIEMPRE dar la misma respuesta para la misma imagen**

El profesor enfatizó: "Yo no quiero que un clasificador de patologías médicas tenga variabilidad". Si le muestras la misma radiografía 10 veces, debe decirte 10 veces lo mismo. No sería bueno que a veces dijera "tumor" y a veces "no tumor" para la misma imagen, ¿verdad?

### Modelos Generativos
En cambio, un modelo generativo hace lo contrario:
- Le das una entrada (por ejemplo: "genera un blues")
- Te da una salida **diferente cada vez**
- Esta variabilidad **no es un error, es el comportamiento correcto**

El profesor lo explicó así: "para una misma entrada, puedo tener distintas salidas, y eso no es un problema, de hecho es el correcto funcionamiento del sistema".

## Características de los Modelos Generativos

### 1. Proceso Estocástico

"Estocástico" suena complicado pero es simple: significa que hay **aleatoriedad** involucrada. El profesor explicó que estos modelos tienen un proceso estocástico detrás, lo que significa que:
- Cuando le pides algo al modelo
- A menos que le fijemos la semilla (un valor que controla la aleatoriedad)
- **No va a generar el mismo dato cada vez**

### 2. Variabilidad en las Salidas

El profesor demostró esto en vivo con el ejemplo del blues. Pidió dos veces lo mismo a ChatGPT:
- Primera vez: generó un blues
- Segunda vez: generó un blues **diferente**
- Ambos eran blues de 12 compases en mi menor (cumplían los requisitos)
- Pero eran composiciones distintas

Como dijo el profesor: "la variedad de su generación es parte de lo que uno desea de este tipo de sistemas".

### 3. Capacidad de Generar Datos Nuevos

Esta es la característica más importante. El profesor contrastó dos cosas:
- **Memorización**: simplemente recordar y repetir lo que ya existe
- **Generación**: crear algo nuevo que no existía antes

Los modelos generativos hacen lo segundo. No están buscando en una base de datos y copiando - están **creando** basándose en patrones que aprendieron.

El profesor dio un ejemplo muy claro: cuando un modelo genera una imagen de un gatito, "esa imagen se espera que no exista en el conjunto de entrenamiento". Es una imagen **completamente nueva**.

## Aplicaciones de Modelos Generativos

El profesor mencionó varias aplicaciones, aunque algunas solo las nombró brevemente:

### 1. Generación de Texto (✅ Explicado en detalle)
- Es el caso más común que vemos todos los días
- Modelos como ChatGPT que generan texto en lenguaje natural
- El profesor lo usó como ejemplo principal durante toda la clase

### 2. Generación de Imágenes (⚠️ Solo mencionado)
- Modelos que crean imágenes nuevas
- Por ejemplo, generar "imágenes de gatitos" que no existían antes
- También mencionó aplicaciones médicas para generar imágenes médicas

### 3. Generación de Audio (⚠️ Solo mencionado)
- Aplicaciones que convierten texto en voz
- "Aplicativos que generan voces... texto que se convierte en audio a partir del prompt"

### 4. Generación de Grafos/Moléculas (⚠️ Solo mencionado)
- Súper interesante para química y materiales
- El profesor dijo: "la generación de grafos nuevos... puede estar creando moléculas nuevas, elementos químicos nuevos"
- Los datos moleculares se modelan como grafos

### 5. Aprendizaje por Refuerzo (⚠️ Solo mencionado)
- Se pueden usar modelos generativos para generar un modelo del ambiente
- En lugar de guardar estados en una tabla, se puede aprender la distribución de los estados

## Conceptos Clave para Recordar

### La diferencia fundamental
El profesor fue muy claro en esto:
- **Modelos discriminativos**: Dan un veredicto consistente (siempre lo mismo)
- **Modelos generativos**: Generan variedad (siempre algo diferente)

### El problema de la evaluación
El profesor advirtió que evaluar modelos generativos es difícil. Dio un ejemplo:
- En un clasificador: si clasifica bien o mal es claro
- En un generativo: "¿Cuál es el ground truth de una imagen generada de un gatito?"

No hay una respuesta "correcta" única cuando generas algo nuevo.

### La importancia histórica
El profesor contó que estas ideas son muy antiguas. Ada Lovelace (una de las primeras científicas computacionales) ya hablaba en el siglo XIX sobre usar máquinas para escribir música. La idea de que las computadoras generen cosas nuevas está desde los inicios de la computación misma.

## Resumen Simple

Si tuvieras que explicárselo a alguien que no sabe nada:

**Los modelos generativos son como artistas digitales**: les das una idea y crean algo nuevo cada vez. No copian, no memorizan - crean. Y cada creación es diferente, aunque le pidas lo mismo. Esto no es un error, es exactamente lo que queremos que hagan.

En cambio, los clasificadores son como jueces: miran algo y dan un veredicto que debe ser siempre el mismo. No queremos creatividad de ellos, queremos consistencia.

La magia de los modelos generativos está en que pueden crear infinitas variaciones de cosas que nunca existieron antes, desde textos hasta imágenes, música, o incluso moléculas nuevas para medicamentos.

---

## Definiciones para el Parcial

### Conceptos Fundamentales

**Modelo Generativo:** Sistema que puede crear datos nuevos que no existían antes a partir de un input; para una misma entrada puede generar distintas salidas, y esa variabilidad es parte de su correcto funcionamiento.

**Modelo Discriminativo (Clasificador):** Sistema que toma una entrada y produce un veredicto o clasificación consistente; para una misma entrada debe dar siempre la misma respuesta (ej: un clasificador de tumores debe decir lo mismo cada vez que ve la misma radiografía).

**Proceso Estocástico:** Proceso que involucra aleatoriedad; en modelos generativos significa que el modelo no generará el mismo dato cada vez que le pidas algo, a menos que fijes la semilla.

**Variabilidad:** Capacidad de un modelo generativo de producir salidas diferentes para una misma entrada; no es un error sino una característica deseada que permite la creatividad del sistema.

**Semilla (Seed):** Valor que controla la aleatoriedad en un proceso estocástico; si fijas la semilla, el modelo generará siempre el mismo resultado para la misma entrada.

### Memorización vs Generación

**Memorización:** Cuando un modelo simplemente recuerda y repite datos que ya existen en su conjunto de entrenamiento; no es lo que queremos de un modelo generativo.

**Generación:** Crear datos completamente nuevos que no existían antes, basándose en patrones aprendidos; una imagen generada de un gatito se espera que no exista en el conjunto de entrenamiento.

### Evaluación

**Ground Truth:** La respuesta "correcta" contra la cual comparamos la predicción de un modelo; en modelos discriminativos es claro (la etiqueta real), pero en modelos generativos es difícil definirlo porque no hay una única respuesta correcta para datos generados.

### Diferencia Clave

| Característica | Modelo Discriminativo | Modelo Generativo |
|----------------|----------------------|-------------------|
| Objetivo | Clasificar/decidir | Crear datos nuevos |
| Variabilidad | No deseada (consistencia) | Deseada (creatividad) |
| Ejemplo | Clasificador de tumores | ChatGPT generando texto |
| Misma entrada → | Misma salida siempre | Diferentes salidas cada vez |