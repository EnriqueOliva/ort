# Explicación Completa del Obligatorio: Evolución de GANs

**Autor:** Enrique Oliva (214205)
**Curso:** Inteligencia Artificial Generativa 2025
**Tema:** Análisis Comparativo de Vanilla GAN → WGAN → WGAN-GP

---

## ¿De qué trata este obligatorio?

Este trabajo compara tres generaciones de GANs (Redes Generativas Adversariales) para entender cómo cada versión soluciona problemas de la anterior. Es como ver la evolución de un producto: la versión 1.0 funciona pero tiene problemas, la 2.0 los soluciona pero introduce nuevos problemas, y la 3.0 finalmente lo hace bien.

**Las tres versiones son:**
1. **Vanilla GAN (2014)** - La original, con problemas de estabilidad
2. **WGAN (2017)** - Usa una métrica diferente para mejorar estabilidad
3. **WGAN-GP (2017)** - Corrige los problemas de WGAN

---

## Tabla de Contenidos

1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [Problemas de Vanilla GAN](#problemas-de-vanilla-gan)
3. [Qué es WGAN y qué introduce](#qué-es-wgan-y-qué-introduce)
4. [Problemas de WGAN](#problemas-de-wgan)
5. [Qué es WGAN-GP y qué introduce](#qué-es-wgan-gp-y-qué-introduce)
6. [Explicación Celda por Celda](#explicación-celda-por-celda)

---

# Conceptos Fundamentales

## ¿Qué es una GAN?

Una GAN (Generative Adversarial Network) es un sistema de dos redes neuronales que "juegan" una contra la otra:

### El Generador (G)
- **Qué hace:** Crea imágenes falsas a partir de ruido aleatorio
- **Objetivo:** Engañar al discriminador para que piense que las imágenes son reales
- **Analogía:** Es como un falsificador de billetes

### El Discriminador (D) o Crítico (C)
- **Qué hace:** Distingue entre imágenes reales y falsas
- **Objetivo:** Detectar correctamente cuáles son reales y cuáles son falsas
- **Analogía:** Es como un detective que intenta detectar billetes falsos

### El Entrenamiento Alternado

```
1. Entrenas el Discriminador:
   - Le muestras imágenes reales → debe decir "real"
   - Le muestras imágenes falsas del Generador → debe decir "falsa"
   - Actualizas solo los parámetros del Discriminador

2. Entrenas el Generador:
   - Generas imágenes falsas
   - Las pasas por el Discriminador
   - Ajustas el Generador para que el Discriminador las clasifique como reales
   - Actualizas solo los parámetros del Generador

3. Repites 1 y 2 muchas veces
```

**La idea:** Con el tiempo, el Generador se vuelve tan bueno que el Discriminador ya no puede distinguir las imágenes falsas de las reales.

---

# Problemas de Vanilla GAN

La GAN original (propuesta por Ian Goodfellow en 2014) tenía cuatro problemas principales que hacían muy difícil entrenarla. Vamos a explicarlos de manera súper simple:

---

## 1. Training Instability (Inestabilidad de Entrenamiento)

### El Problema en una Frase:
El entrenamiento es caótico y las pérdidas suben y bajan sin patrón, imposibilitando saber si está mejorando o empeorando.

### Analogía Simple:

Imagina un partido de fútbol entre dos equipos que están aprendiendo a jugar:

**El Generador (Equipo Atacante):** Intenta meter goles
**El Discriminador (Equipo Defensor):** Intenta detenerlos

**El problema:**
- Si el equipo defensor mejora muy rápido, el equipo atacante se frustra porque NUNCA puede meter goles. Sin goles, no aprenden.
- Si el equipo atacante mejora muy rápido, el equipo defensor nunca ve ataques desafiantes. Sin desafíos, no aprenden.

**En la práctica:**
Las pérdidas se ven así:
```
Época 1: D_loss = 0.5, G_loss = 0.8
Época 2: D_loss = 1.2, G_loss = 0.3  ← ¿Mejoró o empeoró?
Época 3: D_loss = 0.7, G_loss = 1.5  ← ¿Y ahora?
Época 4: D_loss = 0.9, G_loss = 0.6  ← No hay patrón claro
```

**¿Por qué es un problema?**
No puedes saber si deberías entrenar más, parar, o cambiar algo. Es como conducir con los ojos vendados.

---

## 2. Mode Collapse (Colapso de Modos)

### El Problema en una Frase:
El Generador se "queda pegado" generando solo UNA o pocas variaciones, en lugar de generar variedad.

### Analogía Simple:

Imagina un estudiante que tiene que presentar diferentes temas en clase:

**Situación ideal:** El estudiante aprende a presentar sobre matemáticas, historia, ciencias, arte, etc.

**Mode Collapse:** El estudiante descubre que si presenta sobre matemáticas, siempre saca 10. Entonces... solo presenta sobre matemáticas. Siempre. Nunca aprende nada más.

### Ejemplo Concreto con Números:

Estás entrenando una GAN para generar dígitos del 0 al 9.

**Lo que debería pasar:**
- El Generador aprende a generar 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 con variedad

**Lo que pasa con Mode Collapse:**
- El Generador genera "3" muy bien
- El Discriminador no detecta esos "3" como falsos
- **Resultado:** El Generador solo genera "3", "3", "3", "3"... ¡siempre "3"!

**Lo que dijo el profesor:**
> "Si vos aprendes a hacer un buen uno y tu modelo aprende a hacer un muy buen uno y que tu discriminador no discrimina, ya está, ganaste. Siempre que pasa ruido te da un buen uno."

**¿Por qué pasa esto?**
La función de pérdida NO premia la variedad. Solo premia engañar al Discriminador. Si encuentras UNA forma de engañarlo, ¿para qué buscar otras?

---

## 3. Vanishing Gradients (Gradientes que Desaparecen)

### El Problema en una Frase:
Cuando el Discriminador se vuelve muy bueno, el Generador deja de recibir señales útiles para aprender.

### Analogía Simple:

Imagina que estás aprendiendo a cocinar y tienes un crítico gastronómico (el Discriminador) que prueba tus platos:

**Al principio (Discriminador novato):**
- Crítico: "Este plato está 60% bien. Te falta más sal, cocina 5 minutos más la carne, y la presentación podría mejorar."
- Tú: "¡Gracias! Tengo información concreta para mejorar."

**Después (Discriminador experto):**
- Crítico: "Esto es horrible. 0/10."
- Tú: "¿Pero QUÉ está mal? ¿Es la sal? ¿El tiempo de cocción? ¿La presentación?"
- Crítico: "Es horrible. 0/10." (sin más detalles)
- Tú: "Pero... ¿hacia dónde debo mejorar?"
- Crítico: "0/10."

**¿Ves el problema?**
Cuando el Discriminador es TAN bueno que detecta perfectamente todo lo falso, solo dice "FALSO", pero no te da **dirección** de hacia dónde mejorar. Sin dirección (gradiente), no puedes aprender.

### ¿Por qué pasa técnicamente?

El Discriminador usa una función llamada "sigmoid" que convierte sus respuestas a números entre 0 y 1:
- 1 = "Definitivamente real"
- 0 = "Definitivamente falso"

Cuando el Discriminador es muy bueno:
- Muestras reales → 0.99999 (casi 1)
- Muestras falsas → 0.00001 (casi 0)

En esos extremos, la función se "aplana" y el gradiente (la pendiente, la dirección) se vuelve casi cero. Es como llegar a la cima de una montaña: todo está plano, no hay pendiente que te indique hacia dónde moverte.

---

## 4. Métrica No Correlacionada con Calidad

### El Problema en una Frase:
El número de la pérdida que ves durante el entrenamiento NO te dice si las imágenes están mejorando.

### Analogía Simple:

Imagina que estás entrenando para una maratón y usas una balanza para medir tu progreso:

**Lo que quieres:**
- Día 1: Corres 5 km → Métrica = 5
- Día 10: Corres 10 km → Métrica = 10
- Día 30: Corres 20 km → Métrica = 20

La métrica sube con tu mejora. Perfecto.

**Lo que pasa con Vanilla GAN:**
- Día 1: Corres 5 km → Métrica = 70 kg (tu peso)
- Día 10: Corres 10 km → Métrica = 69.8 kg
- Día 30: Corres 20 km → Métrica = 70.2 kg

**¿Ves el problema?** Tu peso NO te dice qué tan bien corres. Podrías estar corriendo mejor y el número puede subir o bajar sin relación.

### En la Práctica con GANs:

```
Iteración 100: D_loss = 0.69, Imágenes = puro ruido (horribles)
Iteración 500: D_loss = 0.68, Imágenes = se ven algo mejor
Iteración 1000: D_loss = 0.70, Imágenes = ¡excelentes!
```

**Problema:** La pérdida se queda cerca de 0.69 SIEMPRE, sin importar si las imágenes mejoran o no.

**¿Por qué pasa esto?**
Por la Jensen-Shannon divergence. Cuando las distribuciones (real vs fake) no se superponen (que es casi siempre al principio), JS se "satura" en 0.69 y se queda ahí. Es como un termómetro roto que siempre marca 37°C.

**Consecuencia práctica:**
No puedes saber:
- ¿Está mejorando el modelo?
- ¿Cuándo debería parar el entrenamiento?
- ¿Qué experimento funcionó mejor?

Tienes que mirar las imágenes MANUALMENTE para saber si está funcionando. ¡No hay métrica confiable!

## ¿Qué es la Wasserstein Distance?

### Analogía Súper Simple: La Mudanza de Arena

Imagina que tienes dos playas con arena distribuida de manera diferente:

**Playa A (Imágenes Reales):** Tiene montones de arena en ciertos lugares
**Playa B (Imágenes Generadas):** Tiene montones de arena en otros lugares

**La pregunta que responde Wasserstein distance es:**
Si tuvieras que redistribuir toda la arena de la Playa B para que quede exactamente como la Playa A, **¿cuánto esfuerzo necesitarías?**

El "esfuerzo" se mide como:
- **Cantidad de arena** que tienes que mover × **distancia** que la tienes que mover

**Ejemplo concreto:**
- Si tienes que mover 10 kg de arena una distancia de 5 metros = 50 kg·metros de esfuerzo
- Si tienes que mover 2 kg de arena una distancia de 100 metros = 200 kg·metros de esfuerzo

**Mientras más parecidas sean las distribuciones, menos esfuerzo necesitas.**
**Mientras más diferentes sean, más esfuerzo necesitas.**

---

### ¿Y qué es la Jensen-Shannon Divergence? (La métrica que usa Vanilla GAN)

La Jensen-Shannon (JS) divergence es otra forma de medir qué tan diferentes son dos distribuciones, pero funciona de manera completamente distinta a Wasserstein.

---

#### 🔍 **¿Qué mide Jensen-Shannon?**

En vez de medir el "esfuerzo de mudanza" como Wasserstein, JS responde una pregunta diferente:

**"Si te muestro UNA muestra aleatoria, ¿puedes adivinar con certeza si vino de la distribución Real o de la distribución Falsa?"**

---

#### 📊 **Analogía: El Juego de Adivinar**

Imagina que tienes dos urnas con bolas de colores:

**Urna Real:** Tiene bolas rojas en las posiciones 1, 2, 3
**Urna Falsa:** Tiene bolas azules en las posiciones 8, 9, 10

Te vendo los ojos y me dices: "Saca una bola de cualquier urna y dámela."

**Pregunta:** ¿Puedes adivinar de qué urna vino?

**Respuesta:** ¡SÍ! Es trivial:
- Si es roja → vino de Urna Real
- Si es azul → vino de Urna Falsa

**Jensen-Shannon dice:** "Como puedes distinguirlas perfectamente, son TOTALMENTE diferentes."
**Valor de JS:** 0.69 (el máximo, significa "distinguibles al 100%")

---

#### 🚨 **El Problema Gigante de JS**

Ahora supongamos que mueves las bolas azules un poquito más cerca:

**Urna Real:** Bolas rojas en posiciones 1, 2, 3
**Urna Falsa:** Bolas azules en posiciones 7, 8, 9 (un poco más cerca)

**Pregunta:** ¿Puedes adivinar de qué urna vino?

**Respuesta:** ¡SÍ! Todavía es trivial:
- Roja → Real
- Azul → Falsa

**JS dice:** "Como puedes distinguirlas perfectamente, son TOTALMENTE diferentes."
**Valor de JS:** ¡Sigue siendo 0.69! (¡¡no cambió!!)

---

**Sigues moviendo las bolas azules más cerca...**

- Posiciones 6, 7, 8 → **JS = 0.69** (sin cambio)
- Posiciones 5, 6, 7 → **JS = 0.69** (sin cambio)
- Posiciones 4, 5, 6 → **JS = 0.69** (sin cambio)

**¿Ves el problema?**

Estás MEJORANDO (las bolas están más cerca), pero JS no lo refleja. Sigue diciendo "0.69... 0.69... 0.69..."

---

**Finalmente, cuando las bolas se SUPERPONEN:**

**Urna Real:** Bolas rojas en posiciones 1, 2, 3
**Urna Falsa:** Bolas azules en posiciones 1, 2, 3 (¡mismas posiciones!)

Pero todavía son distinguibles porque tienen colores diferentes...

**JS = 0.69** (todavía distinguibles)

---

**SOLO cuando las bolas son IDÉNTICAS (mismo color Y posición):**

**Urna Real:** Bolas rojas en posiciones 1, 2, 3
**Urna Falsa:** Bolas rojas en posiciones 1, 2, 3

**JS = 0** (¡FINALMENTE baja!)

---

#### 💡 **La Lección Clave**

Jensen-Shannon es **binaria**:
- **JS = 0.69:** "Puedo distinguirlas" (distribuciones diferentes)
- **JS = 0:** "Son idénticas" (distribuciones iguales)

**No hay valores intermedios útiles.**

Es como preguntarle a alguien "¿Son diferentes estas dos cosas?" y solo puede responder:
- "Sí, son diferentes" (0.69)
- "No, son idénticas" (0)

No puede decir "Son un poco diferentes" o "Están casi iguales pero no del todo".

---

#### 🎯 **Resumen Visual de Jensen-Shannon**

```
Mejora de tu GAN:

Estado Real:    [ROJO]──────────────────────>
Estado Generado: [AZUL]  →  [AZUL]  →  [AZUL]  →  [ROJO]
                Lejos    Cerca    Más cerca   Perfecto

Jensen-Shannon:  0.69     0.69      0.69       0.00
                  ↑        ↑         ↑          ↑
               Distinto  Distinto  Distinto  Idéntico

```

**Problema:** ¡No cambia hasta el final! No te dice si estás mejorando.

---

#### 🔑 **¿Por qué el valor 0.69?**

Este número viene de log(2) ≈ 0.693.

**Explicación simple:** Cuando dos distribuciones NO se superponen, el "peor caso" de JS es log(2). Matemáticamente es el máximo que puede alcanzar.

Pero no necesitas entender por qué es 0.69. Lo importante es:
- **0.69 = son diferentes (máxima diferencia)**
- **0.00 = son iguales**
- **No hay puntos intermedios útiles cuando las distribuciones no se superponen**

---

#### ⚠️ **El Problema para las GANs**

Cuando entrenas una GAN:

**Al inicio:**
- Imágenes reales: Fotos naturales de perros, gatos, etc.
- Imágenes generadas: Ruido aleatorio (pixeles sin sentido)
- **¿Se superponen?** NO (son totalmente diferentes)
- **JS = 0.69**

**Después de 100 iteraciones:**
- Imágenes reales: Fotos naturales
- Imágenes generadas: Formas borrosas que empiezan a parecerse a algo
- **¿Se superponen?** Todavía NO (siguen siendo distinguibles)
- **JS = 0.69** (¡no cambió!)

**Después de 500 iteraciones:**
- Imágenes reales: Fotos naturales
- Imágenes generadas: Imágenes mucho mejores, casi reales
- **¿Se superponen?** Casi, pero no del todo
- **JS = 0.69** (¡SIGUE sin cambiar!)

**Conclusión:** La métrica no te dice si estás mejorando. Tienes que mirar las imágenes manualmente.

---

### ¿Por qué Wasserstein es Mejor?

Volvamos al ejemplo de las playas:

**Con Wasserstein:**
- Playa A: arena en la izquierda (posición 0)
- Playa B: arena en la derecha (posición 100)
- **Wasserstein = 100** (tienes que mover la arena 100 metros)

Ahora mueves la arena de la Playa B un poco hacia la izquierda:
- Playa B ahora en posición 90
- **Wasserstein = 90** (¡bajó! Estás mejorando!)

Sigues moviendo:
- Posición 80 → **Wasserstein = 80**
- Posición 70 → **Wasserstein = 70**
- Posición 50 → **Wasserstein = 50**
- Posición 10 → **Wasserstein = 10**
- Posición 0 → **Wasserstein = 0** (¡perfectas!)

**¿Ves la diferencia?**
Wasserstein te da **feedback continuo**. Cada pequeña mejora se refleja en un número más bajo. Es como un GPS que te dice "estás a 100 metros... 90 metros... 50 metros... 10 metros..." en vez de solo decirte "LEJOS... LEJOS... LEJOS... ¡LLEGASTE!"

---

# Qué es WGAN y qué introduce

WGAN (Wasserstein GAN) fue propuesto por Arjovsky, Chintala y Bottou en 2017 para solucionar los problemas de Vanilla GAN.

## La Idea Central: Cambiar la Métrica

La innovación clave de WGAN es **usar una métrica diferente** para medir qué tan diferentes son la distribución real y la distribución generada.

**Vanilla GAN usa:** Jensen-Shannon (JS) divergence → Como un interruptor ON/OFF
**WGAN usa:** Wasserstein distance (también llamada Earth-Mover distance) → Como un GPS con distancia continua

### ¿Por qué cambiar la métrica soluciona los problemas?

Recuerda el problema #4 de Vanilla GAN: la métrica no correlaciona con calidad de imágenes.

**La causa raíz:** Jensen-Shannon divergence se "satura" cuando las distribuciones no se superponen (que es casi siempre). Es como tener un termómetro que solo marca "frío" o "caliente", sin valores intermedios.

**La solución:** Wasserstein distance SIEMPRE te da feedback continuo, incluso cuando las distribuciones están muy alejadas. Es como tener un GPS que te dice "estás a 500 metros... 400 metros... 300 metros..." en vez de solo "LEJOS... LEJOS... ¡LLEGASTE!"

Esta simple mejora en la métrica soluciona varios problemas a la vez:
- ✅ Métrica correlacionada con calidad (problema #4)
- ✅ Sin vanishing gradients (problema #3)
- ✅ Más estabilidad de entrenamiento (problema #1)

### ¿Por qué Importa JS-Divergence vs. Wasserstein Distance para las GANs?

Cuando entrenas una GAN, necesitas que la función de pérdida te diga **hacia dónde moverte** para mejorar. Eso se llama "gradiente".

**Con JS (Vanilla GAN):**
- Si las distribuciones no se superponen → gradiente = 0 (no sé hacia dónde moverme)
- Es como estar en un desierto completamente plano sin ninguna pista de hacia dónde caminar

**Con Wasserstein (WGAN):**
- Siempre hay un gradiente que apunta en la dirección correcta
- Es como tener un camino con pendiente que te guía hacia el objetivo

**La conclusión:**
Wasserstein distance es mejor para entrenar GANs porque **siempre te dice cómo mejorar**, incluso cuando las distribuciones están muy alejadas.

## Cómo se Implementa WGAN

### 1. El Crítico (ya no Discriminador)

**Cambio importante:** En WGAN, el Discriminador se llama "Crítico" (Critic) porque ya no clasifica (0 o 1), sino que da un puntaje real.

**Diferencias:**
```python
# Vanilla GAN Discriminator (última capa)
output = sigmoid(linear(x))  # Rango: [0, 1]

# WGAN Critic (última capa)
output = linear(x)  # Rango: (-∞, +∞)
```

**Sin sigmoid:** El Crítico puede dar cualquier número real, no está limitado a [0,1].

### 2. La Restricción de Lipschitz

Para que la matemática funcione, el Crítico debe ser una **función 1-Lipschitz**. Esto significa que su gradiente no puede ser mayor que 1.

**¿Qué es Lipschitz?**
Una función f es k-Lipschitz si:
```
|f(x) - f(y)| ≤ k·||x - y|| para todo x, y
```

En español: la función no puede cambiar más rápido que k veces la distancia de entrada.

**¿Cómo se enforce en WGAN?**
Con **weight clipping** (recorte de pesos):

```python
# Después de cada actualización del Crítico
for param in critic.parameters():
    param.data.clamp_(-c, c)  # c = 0.01 típicamente
```

Esto fuerza todos los pesos a estar en el rango [-c, c].

### 3. Función de Pérdida

**Para el Crítico:**
```python
loss_C = -E[f(x_real)] + E[f(x_fake)]
```
→ Queremos maximizar f(x_real) y minimizar f(x_fake)
→ Esto estima la Wasserstein distance

**Para el Generador:**
```python
loss_G = -E[f(G(z))]
```
→ Queremos que el Crítico dé puntajes altos a nuestras imágenes falsas

### 4. Entrenamiento del Crítico a "Optimality"

**Diferencia clave con Vanilla GAN:**

En Vanilla GAN, NO queremos un Discriminador perfecto (causa vanishing gradients).

En WGAN, SÍ queremos entrenar el Crítico lo mejor posible porque:
- La Wasserstein distance solo se estima bien con un Crítico óptimo
- Incluso con un Crítico óptimo, NO hay vanishing gradients

**En la práctica:**
```python
for epoch in epochs:
    for i in range(n_critic):  # n_critic = 5 típicamente
        train_critic()

    train_generator()
```

Entrenamos el Crítico 5 veces por cada vez que entrenamos el Generador.

## Ventajas de WGAN sobre Vanilla GAN

### 1. Métrica Significativa ✅

**El problema que resuelve:** En Vanilla GAN, la pérdida no correlaciona con calidad

**Cómo lo resuelve WGAN:**
La pérdida del Crítico es una estimación de la Wasserstein distance. Cuando esta distancia baja, ¡las imágenes mejoran!

```
Iteración 100: W_estimate = 45.2, Imágenes = malas
Iteración 500: W_estimate = 12.8, Imágenes = mejores
Iteración 1000: W_estimate = 3.5, Imágenes = buenas
```

Ahora puedes ver si el modelo está mejorando mirando la pérdida.

### 2. No Más Vanishing Gradients ✅

**El problema que resuelve:** Gradientes que desaparecen cuando D es muy bueno

**Cómo lo resuelve WGAN:**
La Wasserstein distance es diferenciable casi en todas partes, incluso cuando el Crítico es óptimo.

**La matemática dice:**
```
∇_θ W(P_real, P_θ) = -E[∇f(G(z))]
```

Este gradiente existe y es útil, incluso cuando el Crítico está entrenado a la perfección.

### 3. Mayor Estabilidad ✅

**El problema que resuelve:** Training instability de Vanilla GAN

**Cómo lo resuelve WGAN:**
- Ya no necesitas balancear cuidadosamente G y D
- Puedes entrenar el Crítico a optimality sin problemas
- La función objetivo es más suave

### 4. Menos Mode Collapse ✅

**El problema que resuelve:** El Generador se queda generando pocas variaciones

**Cómo lo resuelve WGAN:**
El hecho de poder entrenar el Crítico a optimality hace imposible el mode collapse. Si el Generador colapsa a un solo modo, el Crítico lo detectará y penalizará fuertemente.

---

# Problemas de WGAN

Aunque WGAN mejora mucho sobre Vanilla GAN, el weight clipping introduce nuevos problemas. Los mismos autores del paper admiten que **"weight clipping is clearly terrible"**.

## 1. Capacity Underuse (Uso Reducido de Capacidad)

**El problema:**
El weight clipping fuerza al Crítico a aprender funciones muy simples, desperdiciando la capacidad del modelo.

**¿Por qué pasa?**
Al limitar los pesos a [-c, c], estamos forzando la función a ser "simple". El Crítico óptimo debería tener gradientes de norma 1 en todas partes, pero con clipping, la red termina aprendiendo funciones casi lineales entre los extremos del rango de clipping.

**Evidencia experimental:**
En el paper de WGAN-GP, la Figura 1a muestra que un Crítico entrenado con weight clipping en distribuciones toy (como "8 Gaussians") aprende superficies de valor muy simples que ignoran los momentos más altos de la distribución.

**En español simple:**
Es como si le dieras a un arquitecto (el Crítico) todas las herramientas del mundo, pero le dijeras que solo puede usar un martillo y un clavo. Técnicamente puede construir algo, pero no utilizará todo su potencial.

## 2. Exploding and Vanishing Gradients (Gradientes que Explotan o Desaparecen)

**El problema:**
Dependiendo del valor de c (el threshold de clipping), los gradientes pueden explotar (volverse muy grandes) o desaparecer (volverse muy pequeños) a medida que backpropageas a través de capas profundas.

**¿Por qué pasa?**
- Si c es muy pequeño (ej: c = 0.001): Los pesos son muy pequeños, los gradientes se multiplican por valores pequeños en cada capa → **vanishing gradients**
- Si c es muy grande (ej: c = 0.1): Viola la restricción de Lipschitz efectivamente, los gradientes pueden crecer sin control → **exploding gradients**

**Evidencia experimental:**
La Figura 1b del paper de WGAN-GP muestra que en una red de 12 capas entrenada en el dataset Swiss Roll:
- Con c = 0.001: Gradientes decaen exponencialmente (línea azul bajando)
- Con c = 0.1: Gradientes crecen exponencialmente (línea roja subiendo)

Solo con gradient penalty (línea verde) los gradientes se mantienen estables.

**El dilema:**
```
Si c es pequeño → Crítico aprende lento, gradientes desaparecen
Si c es grande → Viola Lipschitz, gradientes explotan
No hay un valor "correcto" de c que funcione siempre
```

## 3. Weight Distribution Pathológica

**El problema:**
El weight clipping empuja los pesos hacia los extremos del rango permitido (−c y +c), en lugar de distribuirse naturalmente.

**¿Por qué pasa?**
Durante el entrenamiento, los pesos que "quieren" ser mayores que c se quedan en c, y los que "quieren" ser menores que -c se quedan en -c. Esto crea una distribución bimodal (dos picos) en lugar de una distribución suave.

**Evidencia experimental:**
La Figura 1b del paper de WGAN-GP muestra histogramas de pesos:
- **Con weight clipping (arriba):** Dos picos enormes en -c y +c
- **Con gradient penalty (abajo):** Distribución suave y natural

**¿Por qué es malo?**
Tener todos los pesos en los extremos significa que el Crítico está "forzado" a una configuración no óptima. Es como si estuvieras afinando una guitarra pero algunas cuerdas estuvieran atascadas en posiciones extremas.

## 4. Sensibilidad a Hiperparámetros

**El problema:**
WGAN requiere ajustar cuidadosamente:
- El valor de c (clipping threshold)
- El learning rate
- El ratio de entrenamiento Crítico:Generador

**¿Por qué pasa?**
Todos estos hiperparámetros interactúan de formas complejas debido al weight clipping:
- Si cambias c, necesitas cambiar el learning rate
- Si cambias el learning rate, necesitas cambiar cuántas veces entrenas el Crítico
- Si cambias la arquitectura, necesitas re-tunearlo todo

**Del paper original de WGAN:**
> "Weight clipping is a clearly terrible way to enforce a Lipschitz constraint. If the clipping parameter is large, then it can take a long time for any weights to reach their limit, thereby making it harder to train the critic till optimality. If the clipping is small, this can easily lead to vanishing gradients."

## 5. Incompatibilidad con Adam Optimizer

**El problema:**
WGAN funciona mal con Adam (el optimizer más común), y requiere RMSProp.

**¿Por qué pasa?**
Adam usa momentum (β₁ > 0), que guarda un promedio móvil de gradientes pasados. Esto interactúa mal con el weight clipping porque:
1. Adam acumula momentum basado en gradientes
2. Luego aplicamos clipping, que "corta" los pesos
3. El momentum ahora apunta en una dirección incorrecta
4. El entrenamiento se vuelve inestable

**Del paper de WGAN:**
> "We identified momentum as a potential cause because, as the loss blew up and samples got worse, the cosine between the Adam step and the gradient usually turned negative."

**La solución en WGAN:**
Usar RMSProp en lugar de Adam. Pero esto es una limitación porque Adam generalmente funciona mejor.

---

# Qué es WGAN-GP y qué introduce

WGAN-GP (Wasserstein GAN with Gradient Penalty) fue propuesto por Gulrajani et al. en 2017, apenas unos meses después de WGAN. Su objetivo es **mantener todas las ventajas de WGAN mientras se eliminan los problemas del weight clipping**.

## La Innovación Central: Gradient Penalty

En lugar de hacer weight clipping para enforcer la restricción de Lipschitz, WGAN-GP **penaliza directamente el gradiente**.

### La Idea Teórica

**Proposición 1 del paper:**
El Crítico óptimo en WGAN tiene una propiedad especial: **su gradiente tiene norma 1** en casi todos los puntos entre la distribución real y la distribución generada.

Matemáticamente:
```
||∇f*(x)||₂ = 1  para casi todo x
```

Donde f* es el Crítico óptimo.

**¿Por qué?**
Si imaginas las distribuciones real y generada como dos "islas", el Crítico óptimo es una función que conecta estas islas con una "pendiente" constante de 1. Es la forma más eficiente de transportar masa de una isla a la otra.

### La Implementación: Gradient Penalty

**Idea:** En lugar de clipear pesos, agregar un término de penalización a la función de pérdida que castigue cuando el gradiente NO es 1.

**Nueva función de pérdida:**
```python
loss_C = E[C(x_fake)] - E[C(x_real)] + λ·E[(||∇C(x_hat)||₂ - 1)²]
         └── Wasserstein ────┘          └── Gradient Penalty ──┘
```

Donde:
- `x_hat = ε·x_real + (1-ε)·x_fake` (interpolación entre real y fake)
- `ε ~ U[0,1]` (número aleatorio entre 0 y 1)
- `λ = 10` (coeficiente de penalización, funciona bien en todos los experimentos)

### ¿Dónde se Evalúa el Gradiente?

**Pregunta clave:** ¿En qué puntos x debemos enforcer que ||∇C(x)||₂ = 1?

**La solución:** En puntos **interpolados** entre muestras reales y falsas.

**¿Por qué interpolados?**
Porque la Proposición 1 dice que el Crítico óptimo tiene gradientes de norma 1 en las **líneas rectas** que conectan puntos de la distribución real con puntos de la distribución generada.

**Código:**
```python
# Muestreamos una imagen real
x_real = sample_from_real_data()

# Generamos una imagen falsa
z = sample_noise()
x_fake = generator(z)

# Creamos una interpolación
epsilon = random.uniform(0, 1)
x_hat = epsilon * x_real + (1 - epsilon) * x_fake

# Calculamos el gradiente en x_hat
gradient = compute_gradient(critic(x_hat), x_hat)

# Penalizamos si la norma NO es 1
gradient_penalty = (gradient.norm() - 1)²
```

**Visualización:**
```
Distribución Real          Distribución Generada
      (x_real)                   (x_fake)
         ●                           ●
         |                           |
         |     ε=0.5                |
         |      ▼                    |
         |      ● (x_hat)           |
         └──────────────────────────┘

En x_hat evaluamos ||∇C(x_hat)|| y penalizamos si ≠ 1
```

## Diferencias Arquitectónicas con WGAN

### 1. No Batch Normalization en el Crítico

**El problema con BatchNorm:**
Batch Normalization normaliza usando estadísticas del batch completo. Esto crea dependencias entre muestras del batch.

**¿Por qué es un problema?**
El gradient penalty requiere calcular `∇C(x_hat)` para cada muestra **independientemente**. BatchNorm viola esta independencia porque:

```python
# BatchNorm crea dependencias entre muestras
def batch_norm(x_batch):
    mean = x_batch.mean()  # Promedio del BATCH
    std = x_batch.std()    # Desviación del BATCH
    return (x_batch - mean) / std  # Cada muestra depende del batch completo
```

**Cuando calculamos gradientes:**
```python
gradient = ∇C(x_hat)
```

Con BatchNorm, este gradiente depende de TODAS las otras muestras en el batch, no solo de x_hat. Esto invalida la teoría del gradient penalty.

**La solución en WGAN-GP:**
```python
# Vanilla GAN Discriminator
class VanillaDiscriminator:
    def __init__(self):
        self.conv1 = Conv2d(...)
        self.bn1 = BatchNorm2d(...)  # ✅ OK en Vanilla GAN

# WGAN-GP Critic
class Critic:
    def __init__(self):
        self.conv1 = Conv2d(...)
        # NO BatchNorm  # ❌ BatchNorm viola gradient penalty
```

### 2. Layer Normalization como Alternativa

**¿Qué hacer si queremos normalización?**

El paper recomienda **Layer Normalization** en lugar de Batch Normalization.

**Diferencia:**
```python
# Batch Normalization
# Normaliza ACROSS muestras, para cada canal
def batch_norm(x):  # x shape: (batch, channels, height, width)
    for cada canal:
        mean = promedio_en_dimension_batch
        std = desviacion_en_dimension_batch
        normalizar

# Layer Normalization
# Normaliza WITHIN cada muestra, across canales
def layer_norm(x):  # x shape: (batch, channels, height, width)
    for cada muestra:
        mean = promedio_en_dimensiones_(channels, height, width)
        std = desviacion_en_dimensiones_(channels, height, width)
        normalizar
```

**Por qué Layer Norm está bien:**
Cada muestra se normaliza independientemente, sin depender de otras muestras del batch. Esto preserva la independencia requerida por el gradient penalty.

### 3. Puede Usar Adam Optimizer

**Ventaja sobre WGAN:**
WGAN-GP funciona bien con Adam, mientras que WGAN requiere RMSProp.

**¿Por qué?**
Sin weight clipping, no hay interacción patológica entre el momentum de Adam y el recorte de pesos.

**Hiperparámetros recomendados:**
```python
optimizer_G = Adam(G.parameters(), lr=1e-4, betas=(0.5, 0.9))
optimizer_C = Adam(C.parameters(), lr=1e-4, betas=(0.5, 0.9))
```

Nota: β₁ = 0.5 (en lugar del default 0.9) para reducir momentum y aumentar estabilidad.

### 4. Penalización Two-Sided

**Diferencia sutil:**
WGAN-GP penaliza cuando el gradiente es diferente de 1, no solo cuando es mayor que 1.

**Two-sided penalty:**
```python
penalty = (||∇C(x_hat)||₂ - 1)²  # Penaliza si es mayor O menor que 1
```

**One-sided penalty (alternativa):**
```python
penalty = max(0, ||∇C(x_hat)||₂ - 1)²  # Solo penaliza si es mayor que 1
```

**El paper usa two-sided** porque el Crítico óptimo tiene ||∇|| = 1, no ||∇|| ≤ 1.

En experimentos, ambas versiones funcionan similarmente, con two-sided ligeramente mejor.

## Ventajas de WGAN-GP sobre WGAN

### 1. No Capacity Underuse ✅

**El problema de WGAN:** Weight clipping fuerza funciones simples

**Cómo lo resuelve WGAN-GP:**
Sin weight clipping, el Crítico puede usar toda su capacidad. Los pesos se distribuyen naturalmente, no forzados a extremos.

**Evidencia:**
Figura 1b (right) del paper: distribución de pesos suave en WGAN-GP vs. dos picos en ±c en WGAN.

### 2. Gradientes Estables ✅

**El problema de WGAN:** Gradientes explotan o desaparecen según c

**Cómo lo resuelve WGAN-GP:**
El gradient penalty es una restricción "suave" que guía al modelo, en lugar de una restricción "dura" que causa problemas.

**Evidencia:**
Figura 1b (left) del paper: gradientes de WGAN-GP se mantienen estables a través de 12 capas, mientras que WGAN tiene gradientes que explotan o desaparecen.

### 3. Funciona con Más Arquitecturas ✅

**El problema de WGAN:** Requiere ajustar c para cada arquitectura

**Cómo lo resuelve WGAN-GP:**
λ = 10 funciona universalmente, desde MLPs simples hasta ResNets de 101 capas.

**Evidencia:**
Tabla 2 del paper: WGAN-GP entrenó exitosamente 147 arquitecturas donde Vanilla GAN falló.

### 4. Compatible con Adam ✅

**El problema de WGAN:** Requiere RMSProp, Adam es inestable

**Cómo lo resuelve WGAN-GP:**
Funciona perfectamente con Adam, que generalmente da mejor desempeño.

### 5. Mejor Convergencia ✅

**Evidencia:**
Figura 3 del paper (CIFAR-10):
- WGAN-GP converge más rápido que WGAN con clipping
- Inception score más alto
- Curva más suave

---

# Explicación Celda por Celda

Ahora voy a explicar tu notebook línea por línea, asumiendo que no sabes nada.

## Celda 0: Introducción (Markdown)

```markdown
# Evolución de las GANs: Vanilla GAN → WGAN → WGAN-GP
```

Esta celda es solo texto explicativo. Presenta el objetivo del notebook:

**Qué hace:** Documenta que vas a comparar tres versiones de GANs

**Por qué está aquí:** Para que cualquiera que lea el notebook entienda de qué trata sin leer todo el código

---

## Celda 1: Importación de Librerías

```python
import os
import torch
import torch.nn as nn
import torch.optim as optim
import torch.autograd as autograd
import torchvision
import torchvision.transforms as transforms
import torchvision.utils as vutils
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import time
from datetime import datetime
import wandb
```

**Qué hace cada import:**

### `import os`
- **Para qué:** Crear carpetas, verificar si archivos existen
- **Ejemplo de uso:** `os.makedirs("resultados")`

### `import torch`
- **Para qué:** PyTorch, la biblioteca de deep learning que usamos
- **Es como:** TensorFlow o Keras, pero más flexible
- **Ejemplo de uso:** `torch.randn(100)` crea un tensor con 100 números aleatorios

### `import torch.nn as nn`
- **Para qué:** Definir arquitecturas de redes neuronales
- **"nn" significa:** Neural Networks
- **Ejemplo de uso:** `nn.Conv2d()` crea una capa convolucional

### `import torch.optim as optim`
- **Para qué:** Optimizadores (Adam, RMSProp, SGD)
- **Qué hacen los optimizadores:** Actualizan los pesos de la red usando gradientes
- **Ejemplo de uso:** `optimizer = optim.Adam(model.parameters())`

### `import torch.autograd as autograd`
- **Para qué:** Calcular gradientes automáticamente
- **Específicamente en WGAN-GP:** Calcular el gradiente del Crítico respecto a la entrada
- **Ejemplo de uso:** `autograd.grad(output, input)` calcula ∇output/∂input

### `import torchvision`
- **Para qué:** Trabajar con imágenes y datasets de imágenes
- **Incluye:** Datasets (CIFAR-10, ImageNet), transformaciones, utilidades

### `import torchvision.transforms as transforms`
- **Para qué:** Transformar imágenes (redimensionar, normalizar, convertir a tensor)
- **Ejemplo de uso:** `transforms.Normalize(mean, std)`

### `import torchvision.utils as vutils`
- **Para qué:** Utilidades para visualizar imágenes
- **Específicamente:** `vutils.make_grid()` crea una grilla de imágenes

### `import numpy as np`
- **Para qué:** Operaciones numéricas con arrays
- **Es:** La biblioteca de álgebra lineal estándar de Python
- **Ejemplo de uso:** `np.mean([1, 2, 3])` calcula el promedio

### `import matplotlib.pyplot as plt`
- **Para qué:** Crear gráficas y visualizaciones
- **Ejemplo de uso:** `plt.plot(x, y)` grafica y vs x

### `from tqdm import tqdm`
- **Para qué:** Barras de progreso
- **Ejemplo:** Cuando entrenas 100 épocas, te muestra: [████████░░] 80%

### `import time` y `from datetime import datetime`
- **Para qué:** Medir tiempo de entrenamiento, timestamps
- **Ejemplo de uso:** `datetime.now()` te da la fecha y hora actual

### `import wandb`
- **Para qué:** Weights & Biases, herramienta para trackear experimentos
- **Qué hace:** Guarda métricas, gráficas, hiperparámetros en la nube
- **Alternativas:** TensorBoard, MLflow

### El bloque `try/except` para matplotlib

```python
try:
    plt.style.use('seaborn-v0_8-darkgrid')
except:
    try:
        plt.style.use('seaborn-darkgrid')
    except:
        pass
```

**Qué hace:** Intenta usar un estilo bonito de gráficas de seaborn

**Por qué el try/except:** Versiones diferentes de matplotlib tienen nombres diferentes para los estilos, este código funciona con cualquier versión

### Seeds de Reproducibilidad

```python
torch.manual_seed(42)
np.random.seed(42)
```

**Qué hace:** Fija las semillas de aleatoriedad

**Por qué:** Para que los experimentos sean reproducibles. Si corres el código dos veces con la misma semilla, obtienes los mismos resultados.

**El número 42:** Es arbitrario (referencia a "Hitchhiker's Guide to the Galaxy"). Cualquier número funciona.

### Detección de Device

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Dispositivo: {device}")
```

**Qué hace:** Detecta si tienes GPU (CUDA) o solo CPU

**Por qué importa:**
- GPU: 10-100x más rápida para deep learning
- CPU: Funciona pero es lenta

**Tu caso (RTX 4070):** Debería imprimir `Dispositivo: cuda`

---

## Celda 2: Hiperparámetros y Configuración

Esta celda define TODOS los hiperparámetros del experimento. Vamos a explicar cada uno.

### Hiperparámetros de Datos

```python
BATCH_SIZE = 64
IMAGE_SIZE = 32
NUM_CHANNELS = 3
```

#### `BATCH_SIZE = 64`
**Qué es:** Cuántas imágenes procesas a la vez

**Analogía:** Es como estudiar flashcards. Puedes:
- Ver 1 flashcard, responder, ver tu error (batch_size=1)
- Ver 64 flashcards, responder todas, ver tus errores (batch_size=64)

**Por qué 64:**
- Es una potencia de 2 (16, 32, 64, 128) → más eficiente en GPU
- Es un balance entre velocidad y estabilidad
- Más grande = más rápido pero necesita más memoria
- Más pequeño = más lento pero más estable

**Tu RTX 4070 (12GB):** Podría usar batch_size más grande (128 o 256), pero 64 es seguro

#### `IMAGE_SIZE = 32`
**Qué es:** Tamaño de las imágenes (32×32 píxeles)

**Por qué 32:**
- Es el tamaño nativo de CIFAR-10
- Es pequeño → entrena más rápido
- Es suficiente para ver estructuras básicas

**Otras opciones comunes:**
- 28×28: MNIST, Fashion-MNIST
- 64×64: CelebA
- 128×128: LSUN bedrooms
- 256×256: ImageNet

#### `NUM_CHANNELS = 3`
**Qué es:** Canales de color (RGB)

**Explicación:**
- 1 canal: Imagen en escala de grises
- 3 canales: RGB (Red, Green, Blue)
- 4 canales: RGBA (incluye transparencia)

**CIFAR-10 tiene 3 canales** → imágenes a color

### Hiperparámetros de Arquitectura

```python
LATENT_DIM = 128
GENERATOR_FEATURES = 128
CRITIC_FEATURES = 128
```

#### `LATENT_DIM = 128`
**Qué es:** Dimensión del espacio latente (el vector z de ruido)

**Analogía:** Es como el número de "perillas" que controlan la imagen generada
- Latent_dim = 2: Solo puedes controlar 2 aspectos (ej: brillo y contraste)
- Latent_dim = 128: Puedes controlar 128 aspectos diferentes

**Por qué 128:**
- Es suficientemente grande para capturar variedad
- No es tan grande que sea difícil de entrenar
- Es una potencia de 2 (eficiencia computacional)

**Valores comunes:**
- 100: Vanilla GAN original
- 128: Estándar en muchos papers
- 256, 512: Para imágenes más complejas

#### `GENERATOR_FEATURES = 128`
**Qué es:** Número de "feature maps" (canales) en el Generador

**Explicación más técnica:**
En una red convolucional, cada capa tiene un número de "filtros" o "feature maps". Esto controla cuántas características diferentes puede aprender la red.

**Ejemplo de flujo en el Generador:**
```
Entrada: (128) → ruido latente
    ↓
Conv Transpuesta: (128*4=512 feature maps)
    ↓
Conv Transpuesta: (128*2=256 feature maps)
    ↓
Conv Transpuesta: (128 feature maps)
    ↓
Salida: (3) → imagen RGB
```

El número 128 es la "base", y se multiplica por 1, 2, o 4 en diferentes capas.

**Por qué 128:**
- Balance entre capacidad y velocidad
- Más pequeño (64) = entrena rápido pero menos calidad
- Más grande (256) = mejor calidad pero más lento y usa más memoria

#### `CRITIC_FEATURES = 128`
**Qué es:** Lo mismo que GENERATOR_FEATURES pero para el Crítico/Discriminador

**Usualmente es igual** al del Generador para mantener balance.

### Hiperparámetros de Entrenamiento

```python
CRITIC_ITERATIONS = 5
NUM_EPOCHS = 1
```

#### `CRITIC_ITERATIONS = 5`
**Qué es:** Cuántas veces entrenas el Crítico/Discriminador antes de entrenar el Generador una vez

**Ratio de entrenamiento:** 5:1 (Crítico:Generador)

**Por qué:**
El Crítico/Discriminador aprende más rápido que el Generador. Si los entrenas 1:1:
- El Crítico se vuelve perfecto muy rápido
- El Generador no recibe gradientes útiles
- El entrenamiento falla

**Valores específicos:**
- **Vanilla GAN:** 1 (alternar 1:1)
- **WGAN y WGAN-GP:** 5 (este es el valor del paper)

**De la clase:**
El profesor explicó que no hay un valor mágico, depende del problema. En la práctica, 5 funciona bien para WGAN/WGAN-GP.

#### `NUM_EPOCHS = 1`
**Qué es:** Una "época" significa que pasaste por TODO el dataset de entrenamiento una vez

**CIFAR-10 tiene 50,000 imágenes de entrenamiento:**
- Con BATCH_SIZE=64: cada época tiene 50,000/64 ≈ 781 batches
- Con CRITIC_ITERATIONS=5: cada época tiene 781 × 5 = 3,905 actualizaciones del Crítico

**Por qué NUM_EPOCHS = 1:**
¡Solo para pruebas rápidas! En un entrenamiento real usarías:
- CIFAR-10: 100-200 épocas
- Imágenes 64×64: 200-500 épocas
- Imágenes 128×128: 500-1000 épocas

**En tu caso:** Probablemente esto es solo para verificar que el código corre sin errores.

### Hiperparámetros de Vanilla GAN

```python
VANILLA_LEARNING_RATE = 2e-4
VANILLA_BETAS = (0.5, 0.999)
```

#### `VANILLA_LEARNING_RATE = 2e-4`
**Qué es:** Qué tan rápido aprende el modelo (tasa de aprendizaje)

**Analogía:** Es como el tamaño de tus pasos cuando buscas algo en la oscuridad:
- Learning rate muy alto (0.1): Das pasos grandes → llegas rápido pero te pasas del óptimo
- Learning rate muy bajo (0.00001): Das pasos pequeños → lento pero preciso
- Learning rate medio (0.0002 = 2e-4): Balance

**Por qué 2e-4:**
Es el valor recomendado en el paper de DCGAN (Radford et al., 2015), que se ha convertido en estándar para GANs.

**Notación científica:**
- 2e-4 = 2 × 10⁻⁴ = 0.0002

#### `VANILLA_BETAS = (0.5, 0.999)`
**Qué es:** Hiperparámetros del optimizador Adam

**Contexto de Adam:**
Adam es un optimizador que usa dos tipos de momentum:
1. **β₁ (beta1):** Momentum de primer orden (promedio de gradientes)
2. **β₂ (beta2):** Momentum de segundo orden (promedio de gradientes al cuadrado)

**Valores default de Adam:** (0.9, 0.999)

**Valores para GANs:** (0.5, 0.999)

**¿Por qué β₁ = 0.5 en lugar de 0.9?**
- Con β₁ = 0.9, Adam tiene mucho momentum → puede oscilar en el training de GANs
- Con β₁ = 0.5, Adam tiene menos momentum → más estable

**Del paper de DCGAN:**
> "We use the Adam optimizer with β₁ = 0.5 instead of the default 0.9"

### Hiperparámetros de WGAN

```python
WGAN_LEARNING_RATE = 5e-5
WGAN_CLIP_VALUE = 0.01
```

#### `WGAN_LEARNING_RATE = 5e-5`
**Qué es:** Learning rate para WGAN

**¿Por qué es más bajo que Vanilla GAN (5e-5 vs 2e-4)?**

Esto es 4 veces más lento que Vanilla GAN. La razón:
1. WGAN entrena el Crítico 5 veces antes del Generador
2. El Crítico necesita converger bien (no solo aprender rápido)
3. Learning rate bajo → convergencia más estable del Crítico

**Del paper de WGAN:**
> "We use the default values α = 0.00005 [learning rate]"

**Nota:** WGAN también usa RMSProp en lugar de Adam, pero en tu código probablemente usaste Adam.

#### `WGAN_CLIP_VALUE = 0.01`
**Qué es:** El valor c para clipear los pesos del Crítico

**Recuerda:** En WGAN, después de cada actualización:
```python
for param in critic.parameters():
    param.data.clamp_(-0.01, 0.01)
```

**¿Por qué 0.01?**
Es el valor del paper original de WGAN. No es óptimo (como admiten los autores), pero funciona razonablemente:
- Más grande (0.1): Viola Lipschitz, gradientes explotan
- Más pequeño (0.001): Gradientes desaparecen
- 0.01: Balance "aceptable"

**Este es el problema que WGAN-GP soluciona:** No hay un valor "correcto" de c.

### Hiperparámetros de WGAN-GP

```python
WGANGP_LEARNING_RATE = 1e-4
WGANGP_LAMBDA = 10
WGANGP_BETAS = (0.5, 0.9)
```

#### `WGANGP_LEARNING_RATE = 1e-4`
**Qué es:** Learning rate para WGAN-GP

**Comparación:**
- Vanilla GAN: 2e-4 = 0.0002
- WGAN: 5e-5 = 0.00005
- WGAN-GP: 1e-4 = 0.0001

**¿Por qué 1e-4?**
- Es un punto medio entre Vanilla GAN y WGAN
- WGAN-GP es más estable que ambos, puede usar un learning rate moderado
- Del paper: "α = 0.0001" es el valor recomendado

#### `WGANGP_LAMBDA = 10`
**Qué es:** El coeficiente λ de la penalización de gradiente

**Recuerda la función de pérdida:**
```
loss_C = E[C(x_fake)] - E[C(x_real)] + λ·E[(||∇C(x_hat)||₂ - 1)²]
```

λ controla qué tan importante es el gradient penalty comparado con la Wasserstein distance.

**¿Por qué λ = 10?**
- Los autores probaron varios valores (1, 10, 100)
- λ = 10 funcionó bien en TODOS los experimentos (CIFAR-10, LSUN, ImageNet)
- Es uno de los grandes logros de WGAN-GP: **un solo valor de λ funciona universalmente**

**Del paper de WGAN-GP:**
> "All experiments in this paper use λ = 10, which we found to work well across a variety of architectures and datasets"

**Sensibilidad:**
- λ = 1: Penalización débil, puede violar la restricción de Lipschitz
- λ = 10: Balance perfecto (valor recomendado)
- λ = 100: Penalización fuerte, puede sobre-restringir el Crítico

El paper muestra que λ = 10 es robusto: funciona bien incluso si lo cambias.

#### `WGANGP_BETAS = (0.5, 0.9)`
**Qué es:** Hiperparámetros de Adam para WGAN-GP

**Comparación:**
- Vanilla GAN: (0.5, 0.999)
- WGAN-GP: (0.5, 0.9)

**Diferencia:** β₂ es 0.9 en lugar de 0.999

**¿Por qué β₂ = 0.9?**
- β₂ controla el momentum de segundo orden (estimación de la varianza del gradiente)
- Valor más bajo (0.9) significa menos momentum → más responsivo a cambios
- En WGANs, queremos que el Crítico se adapte rápidamente

**Del paper de WGAN-GP:**
> "We use Adam with β₁ = 0, β₂ = 0.9" (Algoritmo 1)

**Nota:** El paper usa β₁ = 0 (sin momentum de primer orden), pero (0.5, 0.9) también funciona bien.

---

## Celda 3: Configuración de Directorios

Esta celda crea las carpetas donde se guardarán los resultados.

```python
BASE_OUTPUT_DIR = "./outputs"
EXPERIMENT_NAME = "wgan_comparison"
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
```

### `BASE_OUTPUT_DIR = "./outputs"`
**Qué es:** Carpeta raíz para todos los experimentos

**El punto (.)** significa "carpeta actual"

**Estructura:**
```
tu_notebook.ipynb
outputs/  ← se crea aquí
```

### `EXPERIMENT_NAME = "wgan_comparison"`
**Qué es:** Nombre descriptivo del experimento

**Por qué:** Si corres varios experimentos, cada uno tendrá su carpeta

### `TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")`
**Qué es:** Timestamp único para esta corrida

**Formato:** AñoMesDía_HoraMinutoSegundo

**Ejemplo:** "20251118_143022" (18 de noviembre de 2025, 14:30:22)

**Por qué:** Si corres el experimento varias veces, cada corrida tendrá su propia carpeta

### Creación de subdirectorios

```python
RESULTS_DIR = f"{BASE_OUTPUT_DIR}/{EXPERIMENT_NAME}_{TIMESTAMP}"
MODELS_DIR = f"{RESULTS_DIR}/models"
FIGURES_DIR = f"{RESULTS_DIR}/figures"
SAMPLES_DIR = f"{RESULTS_DIR}/samples"
```

**Estructura final:**
```
outputs/
└── wgan_comparison_20251118_143022/
    ├── models/      ← modelos entrenados (.pth files)
    ├── figures/     ← gráficas (loss curves, etc.)
    └── samples/     ← imágenes generadas
```

### `os.makedirs(..., exist_ok=True)`
**Qué hace:** Crea las carpetas si no existen

**exist_ok=True:** No da error si la carpeta ya existe

### Configuración de W&B (Weights and Biases)

```python
WANDB_PROJECT = "Obligatorio de IA Generativa 2025"
WANDB_ENTITY = "eo214205-ort"
WANDB_GROUP = datetime.now().strftime("%d/%m/%y - %H:%M")
USE_WANDB = False
```

**Qué es W&B:**
Una plataforma para trackear experimentos de machine learning. Es como Google Drive pero especializado para ML.

**Características:**
- Guarda métricas en tiempo real (loss, accuracy, etc.)
- Grafica automáticamente
- Compara múltiples experimentos
- Guarda hiperparámetros
- Es gratis para uso académico

**WANDB_PROJECT:** Nombre del proyecto en W&B (aparece en el dashboard)

**WANDB_ENTITY:** Tu usuario de W&B

**WANDB_GROUP:** Para agrupar experimentos relacionados

**USE_WANDB = False:** Desactivado por ahora (probablemente para pruebas)

**Si lo activas (USE_WANDB = True):**
```python
import wandb
wandb.login()  # Te pide tu API key
wandb.init(project=WANDB_PROJECT, entity=WANDB_ENTITY)
wandb.log({"loss": 0.5, "epoch": 1})
```

---

## Celda 4: Carga de Datos (CIFAR-10)

Esta celda descarga y prepara el dataset CIFAR-10.

### ¿Qué es CIFAR-10?

**CIFAR-10** es un dataset de 60,000 imágenes pequeñas (32×32 píxeles, RGB).

**10 clases:**
1. Airplane (avión)
2. Automobile (auto)
3. Bird (pájaro)
4. Cat (gato)
5. Deer (venado)
6. Dog (perro)
7. Frog (rana)
8. Horse (caballo)
9. Ship (barco)
10. Truck (camión)

**División:**
- 50,000 imágenes de entrenamiento
- 10,000 imágenes de prueba

**Por qué CIFAR-10:**
- Es estándar en la comunidad de ML
- Imágenes a color (más realista que MNIST)
- Tamaño pequeño (entrena rápido)
- Suficientemente difícil para ser interesante

### Transformaciones

```python
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])
```

#### `transforms.Compose([...])`
**Qué hace:** Combina múltiples transformaciones en una secuencia

**Es como:** Una "tubería" (pipeline) de transformaciones

#### `transforms.ToTensor()`
**Qué hace:** Convierte la imagen a un tensor de PyTorch

**Cambios:**
```
Antes: Imagen PIL (0-255, uint8, [H, W, C])
Después: Tensor ([C, H, W], 0.0-1.0, float32)
```

**Ejemplo:**
```
Imagen original: (32, 32, 3) con valores [0, 255]
Después de ToTensor: (3, 32, 32) con valores [0.0, 1.0]
```

**Nota:** También cambia el orden de dimensiones (Height, Width, Channels) → (Channels, Height, Width), que es lo que PyTorch espera.

#### `transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))`
**Qué hace:** Normaliza cada canal a rango [-1, 1]

**Fórmula:**
```
output = (input - mean) / std
```

Con mean = 0.5 y std = 0.5:
```
output = (input - 0.5) / 0.5
```

**Ejemplo numérico:**
```
Si input = 0.0 → output = (0.0 - 0.5) / 0.5 = -1.0
Si input = 0.5 → output = (0.5 - 0.5) / 0.5 = 0.0
Si input = 1.0 → output = (1.0 - 0.5) / 0.5 = 1.0
```

**Valores:** (0.5, 0.5, 0.5) significa aplicar lo mismo a los 3 canales (R, G, B)

**¿Por qué normalizar a [-1, 1]?**
1. **Estabilidad numérica:** Redes neuronales funcionan mejor con valores normalizados
2. **Matching con Tanh:** El Generador usa `tanh` como activación final, que produce valores en [-1, 1]
3. **Estándar en GANs:** Es lo que usa DCGAN y todos los papers siguientes

**De la clase:**
El profesor enfatizó: _"esta transformación de normalización ayuda muchísimo... puede ser clave en forma de que si no normalizamos muchas veces directamente no llegamos a un resultado bueno"._

### Descarga del Dataset

```python
train_dataset = torchvision.datasets.CIFAR10(
    root=DATA_DIR,
    train=True,
    download=True,
    transform=transform
)
```

#### Parámetros:

**`root=DATA_DIR`:** Dónde guardar los archivos descargados

**`train=True`:** Usar el split de entrenamiento (50,000 imágenes)
- `train=False` usaría el split de prueba (10,000 imágenes)

**`download=True`:** Descargar automáticamente si no existe
- Primera vez: descarga (~170 MB)
- Siguientes veces: usa los archivos locales

**`transform=transform`:** Aplicar las transformaciones definidas arriba

### DataLoader

```python
dataloader = torch.utils.data.DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=0,
    drop_last=True
)
```

**Qué es un DataLoader:**
Es un iterador que te da batches de datos automáticamente.

**Sin DataLoader (manual):**
```python
for i in range(0, len(dataset), batch_size):
    batch = dataset[i:i+batch_size]
    # procesar batch...
```

**Con DataLoader:**
```python
for batch in dataloader:
    # procesar batch...
```

#### Parámetros:

**`batch_size=BATCH_SIZE`:** Tamaño del batch (64 en tu caso)

**`shuffle=True`:** Mezclar las imágenes aleatoriamente cada época
- **Por qué:** Evita que la red aprenda el orden de los datos
- **Importante en GANs:** Ayuda a la estabilidad

**`num_workers=0`:** Cuántos procesos paralelos para cargar datos
- 0: Usa el proceso principal (más lento pero más simple)
- 4: Usa 4 procesos paralelos (más rápido)
- **En Windows:** A veces num_workers > 0 causa problemas, mejor dejarlo en 0

**`drop_last=True`:** Si el último batch es más pequeño, descartarlo
- **Ejemplo:** Con 50,000 imágenes y batch_size=64:
  - Batches completos: 50,000 // 64 = 781 batches de 64 imágenes
  - Sobran: 50,000 % 64 = 8 imágenes
  - Con drop_last=True: Se descartan esas 8 imágenes
- **Por qué:** Algunos modelos (especialmente con BatchNorm) esperan batches del mismo tamaño

### Print de Información

```python
print(f"Dataset: CIFAR-10")
print(f"Tamaño del dataset: {len(train_dataset)} imágenes")
print(f"Batches por época: {len(dataloader)}")
print(f"Tamaño de imagen: {IMAGE_SIZE}x{IMAGE_SIZE}x{NUM_CHANNELS}")
```

**Salida esperada:**
```
Dataset: CIFAR-10
Tamaño del dataset: 50000 imágenes
Batches por época: 781
Tamaño de imagen: 32x32x3
```

**`len(train_dataset)`:** Número total de imágenes (50,000)

**`len(dataloader)`:** Número de batches (50,000 / 64 = 781.25 → 781 con drop_last=True)

---

## Celda 5: Función para Visualizar Imágenes

Esta celda define una función helper para mostrar imágenes.

```python
def show_imgs(imgs, title="Images", nrow=8):
    plt.figure(figsize=(5,5))
    plt.axis("off")
    plt.title(title)
    plt.imshow(np.transpose(
        vutils.make_grid(imgs, padding=2, normalize=True, nrow=nrow).cpu(),
        (1, 2, 0)
    ))
    plt.show()
```

### Desglose línea por línea:

#### `plt.figure(figsize=(5,5))`
**Qué hace:** Crea una nueva figura (ventana de matplotlib) de 5×5 pulgadas

#### `plt.axis("off")`
**Qué hace:** Oculta los ejes (números, ticks, etc.)

**Resultado:** Solo ves la imagen, sin decoración

#### `vutils.make_grid(imgs, padding=2, normalize=True, nrow=nrow)`
**Qué hace:** Toma un batch de imágenes y las organiza en una grilla

**Parámetros:**
- `imgs`: Tensor de imágenes, shape (N, C, H, W)
  - N: número de imágenes
  - C: canales (3 para RGB)
  - H: altura (32)
  - W: ancho (32)
- `padding=2`: 2 píxeles de borde blanco entre imágenes
- `normalize=True`: Escala valores a [0, 1] para visualización
- `nrow=8`: 8 imágenes por fila

**Ejemplo:**
```
Si imgs tiene 64 imágenes y nrow=8:
Resultado: Grilla de 8×8 imágenes
```

#### `.cpu()`
**Qué hace:** Mueve el tensor de GPU a CPU

**Por qué:** matplotlib no puede leer tensores en GPU, solo en CPU o NumPy

#### `np.transpose(..., (1, 2, 0))`
**Qué hace:** Cambia el orden de dimensiones

**De:** (C, H, W) - formato PyTorch
**A:** (H, W, C) - formato esperado por matplotlib/imshow

**Ejemplo:**
```
Antes: (3, 256, 256) → 3 canales, 256 alto, 256 ancho
Después: (256, 256, 3) → 256 alto, 256 ancho, 3 canales
```

#### `plt.imshow(...)`
**Qué hace:** Muestra la imagen

#### `plt.show()`
**Qué hace:** Renderiza y muestra la figura

**En notebooks:** Se muestra inline (debajo de la celda)

### Visualización de Muestras Reales

```python
real_batch = next(iter(dataloader))[0][:64]
img_shape = real_batch[0].shape
show_imgs(real_batch, "Muestras Reales de CIFAR-10")
```

#### `next(iter(dataloader))`
**Qué hace:** Obtiene el primer batch del dataloader

**Desglose:**
- `iter(dataloader)`: Crea un iterador
- `next(...)`: Obtiene el siguiente elemento (el primero)

**Retorna:** Tupla (imágenes, etiquetas)

#### `[0][:64]`
**Qué hace:**
- `[0]`: Toma solo las imágenes (no las etiquetas)
- `[:64]`: Toma las primeras 64 imágenes (por si el batch es más grande)

#### `img_shape = real_batch[0].shape`
**Qué hace:** Guarda la forma de una imagen

**Uso posterior:** Puedes verificar que tu Generador produce imágenes del mismo tamaño

---

## Celda 6-8: Arquitecturas de Redes Neuronales

Ahora vienen las arquitecturas más importantes: el Generador y el Crítico/Discriminador.

### Arquitectura del Generador

El Generador es una red que transforma ruido aleatorio en imágenes. Usa **Convoluciones Transpuestas** (también llamadas Deconvoluciones) para "agrandar" progresivamente desde un vector pequeño hasta una imagen 32×32.

```python
class Generator(nn.Module):
    def __init__(self, latent_dim, features, channels):
        super(Generator, self).__init__()

        self.main = nn.Sequential(
            nn.ConvTranspose2d(latent_dim, features * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(features * 8),
            nn.ReLU(True),

            nn.ConvTranspose2d(features * 8, features * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(features * 4),
            nn.ReLU(True),

            nn.ConvTranspose2d(features * 4, features * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(features * 2),
            nn.ReLU(True),

            nn.ConvTranspose2d(features * 2, channels, 4, 2, 1, bias=False),
            nn.Tanh()
        )

    def forward(self, input):
        return self.main(input)
```

#### Desglose Capa por Capa

**Input:** Vector latente z de dimensión (batch, latent_dim, 1, 1)
- Ejemplo: (64, 128, 1, 1) para batch_size=64, latent_dim=128

**Primera Capa: `nn.ConvTranspose2d(latent_dim, features * 8, 4, 1, 0)`**

```python
nn.ConvTranspose2d(128, 1024, kernel_size=4, stride=1, padding=0)
```

- **Input:** (batch, 128, 1, 1)
- **Output:** (batch, 1024, 4, 4)
- **Qué hace:** Expande de 1×1 a 4×4
- **features * 8 = 128 * 8 = 1024 canales**

**¿Qué es ConvTranspose2d?**
Es la operación inversa de una convolución. En lugar de reducir el tamaño, lo aumenta.

**Fórmula del tamaño de salida:**
```
output_size = (input_size - 1) * stride - 2 * padding + kernel_size
            = (1 - 1) * 1 - 2 * 0 + 4
            = 0 + 4
            = 4
```

**BatchNorm2d(1024):**
Normaliza los 1024 canales. Ayuda a estabilizar el entrenamiento.

**ReLU(True):**
Función de activación. `True` significa `inplace=True` (ahorra memoria).

---

**Segunda Capa: `nn.ConvTranspose2d(features * 8, features * 4, 4, 2, 1)`**

```python
nn.ConvTranspose2d(1024, 512, kernel_size=4, stride=2, padding=1)
```

- **Input:** (batch, 1024, 4, 4)
- **Output:** (batch, 512, 8, 8)
- **Qué hace:** Expande de 4×4 a 8×8
- **Reduce canales:** 1024 → 512

**Cálculo del tamaño:**
```
output_size = (4 - 1) * 2 - 2 * 1 + 4
            = 3 * 2 - 2 + 4
            = 6 - 2 + 4
            = 8
```

---

**Tercera Capa: `nn.ConvTranspose2d(features * 4, features * 2, 4, 2, 1)`**

```python
nn.ConvTranspose2d(512, 256, kernel_size=4, stride=2, padding=1)
```

- **Input:** (batch, 512, 8, 8)
- **Output:** (batch, 256, 16, 16)
- **Qué hace:** Expande de 8×8 a 16×16
- **Reduce canales:** 512 → 256

---

**Cuarta Capa (Final): `nn.ConvTranspose2d(features * 2, channels, 4, 2, 1)`**

```python
nn.ConvTranspose2d(256, 3, kernel_size=4, stride=2, padding=1)
```

- **Input:** (batch, 256, 16, 16)
- **Output:** (batch, 3, 32, 32)
- **Qué hace:** Expande de 16×16 a 32×32
- **Reduce a 3 canales:** RGB

**Tanh() (última activación):**
```python
nn.Tanh()
```

**Por qué Tanh:**
- Produce valores en rango [-1, 1]
- Coincide con la normalización de las imágenes reales
- Es estándar en GANs

**Flujo Completo del Generador:**
```
Ruido z: (batch, 128, 1, 1)
    ↓ ConvT + BN + ReLU
(batch, 1024, 4, 4)
    ↓ ConvT + BN + ReLU
(batch, 512, 8, 8)
    ↓ ConvT + BN + ReLU
(batch, 256, 16, 16)
    ↓ ConvT + Tanh
Imagen: (batch, 3, 32, 32)
```

**Decisiones de Diseño:**

1. **¿Por qué usar ConvTranspose2d?**
   - Es la forma estándar de "upsampling" en GANs
   - Aprende cómo aumentar el tamaño (en lugar de interpolación fija)

2. **¿Por qué BatchNorm después de cada capa (excepto la última)?**
   - Estabiliza el entrenamiento
   - Previene que las activaciones exploten o desaparezcan
   - Del paper de DCGAN: "crucial for training to start and for stability"

3. **¿Por qué ReLU en lugar de LeakyReLU?**
   - El paper de DCGAN recomienda ReLU para el Generador
   - LeakyReLU se usa en el Discriminador

4. **¿Por qué bias=False en ConvTranspose2d?**
   - Cuando usas BatchNorm después, el bias es redundante
   - BatchNorm ya tiene su propio término de sesgo (bias)
   - Ahorra parámetros

5. **¿Por qué reducir canales gradualmente (1024→512→256→3)?**
   - Empezamos con muchos canales para capturar características complejas
   - Reducimos gradualmente mientras aumentamos la resolución espacial
   - Es un balance: resolución espacial ↑ mientras features ↓

---

### Arquitectura del Discriminador (Vanilla GAN)

El Discriminador es el opuesto del Generador: toma una imagen y la reduce hasta un solo número (probabilidad de ser real).

```python
class Discriminator(nn.Module):
    def __init__(self, channels, features):
        super(Discriminator, self).__init__()

        self.main = nn.Sequential(
            nn.Conv2d(channels, features, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(features, features * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(features * 2),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(features * 2, features * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(features * 4),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Conv2d(features * 4, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
        )

    def forward(self, input):
        return self.main(input)
```

#### Desglose Capa por Capa

**Input:** Imagen (batch, 3, 32, 32)

**Primera Capa: `nn.Conv2d(3, 128, 4, 2, 1)`**

- **Input:** (batch, 3, 32, 32)
- **Output:** (batch, 128, 16, 16)
- **Qué hace:** Reduce de 32×32 a 16×16, aumenta canales de 3 a 128

**Fórmula del tamaño:**
```
output_size = (input_size - kernel_size + 2 * padding) / stride + 1
            = (32 - 4 + 2 * 1) / 2 + 1
            = (32 - 4 + 2) / 2 + 1
            = 30 / 2 + 1
            = 15 + 1
            = 16
```

**LeakyReLU(0.2):**
```python
LeakyReLU(x) = x si x > 0
             = 0.2 * x si x <= 0
```

**¿Por qué LeakyReLU en lugar de ReLU?**
- Previene "dying ReLU" (neuronas que se apagan permanentemente)
- Del paper de DCGAN: "LeakyReLU in the discriminator"
- El slope de 0.2 es estándar

**¿Por qué NO BatchNorm en la primera capa?**
- Del paper de DCGAN: "not applying batchnorm to the generator output layer and the discriminator input layer"
- Razón: Queremos que el Discriminador vea las imágenes "crudas", sin normalización

---

**Segunda Capa: `nn.Conv2d(128, 256, 4, 2, 1)`**

- **Input:** (batch, 128, 16, 16)
- **Output:** (batch, 256, 8, 8)
- **Qué hace:** Reduce de 16×16 a 8×8, aumenta canales a 256

**Ahora SÍ hay BatchNorm** en las capas intermedias.

---

**Tercera Capa: `nn.Conv2d(256, 512, 4, 2, 1)`**

- **Input:** (batch, 256, 8, 8)
- **Output:** (batch, 512, 4, 4)
- **Qué hace:** Reduce de 8×8 a 4×4, aumenta canales a 512

---

**Cuarta Capa (Final): `nn.Conv2d(512, 1, 4, 1, 0)`**

- **Input:** (batch, 512, 4, 4)
- **Output:** (batch, 1, 1, 1)
- **Qué hace:** Reduce a un solo número

**Sigmoid():**
- Convierte el número a rango [0, 1]
- Interpretación: probabilidad de que la imagen sea real
- 0 = definitivamente falsa
- 1 = definitivamente real
- 0.5 = no puede decidir

**Flujo Completo del Discriminador:**
```
Imagen: (batch, 3, 32, 32)
    ↓ Conv + LeakyReLU
(batch, 128, 16, 16)
    ↓ Conv + BN + LeakyReLU
(batch, 256, 8, 8)
    ↓ Conv + BN + LeakyReLU
(batch, 512, 4, 4)
    ↓ Conv + Sigmoid
Probabilidad: (batch, 1, 1, 1)
```

**Decisiones de Diseño:**

1. **¿Por qué LeakyReLU en el Discriminador?**
   - Previene que neuronas "mueran"
   - Permite que gradientes fluyan incluso para valores negativos
   - Estándar en DCGAN

2. **¿Por qué BatchNorm excepto en primera y última capa?**
   - Primera capa: Queremos ver las imágenes sin normalización
   - Capas intermedias: BatchNorm ayuda a la estabilidad
   - Última capa: No necesita normalización (es solo 1 número)

3. **¿Por qué aumentar canales (3→128→256→512)?**
   - Empezamos con pocas features (solo RGB)
   - Aumentamos features mientras reducimos resolución espacial
   - Opuesto al Generador

---

### Arquitectura del Crítico (WGAN y WGAN-GP)

El Crítico es casi idéntico al Discriminador, con DOS diferencias clave:

```python
class Critic(nn.Module):
    def __init__(self, channels, features, use_instance_norm=False):
        super(Critic, self).__init__()

        layers = []

        # Primera capa (sin normalización)
        layers.append(nn.Conv2d(channels, features, 4, 2, 1, bias=False))
        layers.append(nn.LeakyReLU(0.2, inplace=True))

        # Capas intermedias
        in_features = features
        for out_features in [features * 2, features * 4, features * 8]:
            layers.append(nn.Conv2d(in_features, out_features, 4, 2, 1, bias=False))

            # Normalización (Batch o Instance según el tipo de GAN)
            if use_instance_norm:
                layers.append(nn.InstanceNorm2d(out_features, affine=True))
            else:
                layers.append(nn.BatchNorm2d(out_features))

            layers.append(nn.LeakyReLU(0.2, inplace=True))
            in_features = out_features

        # Última capa (SIN Sigmoid)
        layers.append(nn.Conv2d(in_features, 1, 4, 1, 0, bias=False))

        self.main = nn.Sequential(*layers)

    def forward(self, input):
        return self.main(input)
```

#### Diferencias con el Discriminador de Vanilla GAN:

**1. NO hay Sigmoid al final**

```python
# Discriminador (Vanilla GAN)
nn.Conv2d(...),
nn.Sigmoid()  # ← Output en [0, 1]

# Crítico (WGAN/WGAN-GP)
nn.Conv2d(...)  # ← Output en (-∞, +∞)
```

**Por qué:** El Crítico debe poder dar cualquier valor real, no solo probabilidades en [0,1].

**2. Puede usar InstanceNorm en lugar de BatchNorm**

```python
if use_instance_norm:
    layers.append(nn.InstanceNorm2d(out_features, affine=True))
else:
    layers.append(nn.BatchNorm2d(out_features))
```

**¿Qué es InstanceNorm?**
Similar a BatchNorm, pero normaliza cada muestra independientemente.

**¿Cuándo usar cada uno?**
- **WGAN (con clipping):** Puede usar BatchNorm (es lo que hace el paper original)
- **WGAN-GP:** Debe usar InstanceNorm o LayerNorm (NO BatchNorm)

**¿Por qué WGAN-GP NO puede usar BatchNorm?**

Ya lo explicamos antes, pero resumiendo:
- BatchNorm crea dependencias entre muestras del batch
- El gradient penalty requiere calcular gradientes por muestra individual
- BatchNorm viola esta independencia

**InstanceNorm vs LayerNorm:**
- **InstanceNorm:** Normaliza cada muestra, cada canal independientemente
  ```
  Para cada muestra:
    Para cada canal:
      normalizar espacialmente (altura × ancho)
  ```
- **LayerNorm:** Normaliza cada muestra a través de todos los canales
  ```
  Para cada muestra:
    normalizar a través de (canales × altura × ancho)
  ```

**affine=True en InstanceNorm:**
```python
nn.InstanceNorm2d(features, affine=True)
```

- Permite aprender parámetros de escala (γ) y sesgo (β)
- Sin `affine`, InstanceNorm solo normaliza
- Con `affine`, puede "deshacer" la normalización si es necesario

---

## Celda 9-11: Funciones de Pérdida

Ahora vienen las funciones de pérdida específicas de cada tipo de GAN.

### Función de Pérdida de Vanilla GAN

```python
def compute_vanilla_loss_D(discriminator, real_imgs, fake_imgs):
    """
    Pérdida del Discriminador en Vanilla GAN.
    Usa Binary Cross Entropy (BCE).
    """
    batch_size = real_imgs.size(0)

    # Etiquetas
    real_labels = torch.ones(batch_size, 1, 1, 1).to(real_imgs.device)
    fake_labels = torch.zeros(batch_size, 1, 1, 1).to(real_imgs.device)

    # Forward pass
    real_output = discriminator(real_imgs)
    fake_output = discriminator(fake_imgs.detach())

    # Binary Cross Entropy Loss
    loss_real = nn.BCELoss()(real_output, real_labels)
    loss_fake = nn.BCELoss()(fake_output, fake_labels)

    loss_D = loss_real + loss_fake

    return loss_D, loss_real.item(), loss_fake.item()
```

#### Explicación Detallada:

**Etiquetas:**
```python
real_labels = torch.ones(...)  # Todos 1s (para imágenes reales)
fake_labels = torch.zeros(...)  # Todos 0s (para imágenes falsas)
```

**¿Por qué shape (batch_size, 1, 1, 1)?**
- El Discriminador produce output de shape (batch, 1, 1, 1)
- Las etiquetas deben tener el mismo shape para BCELoss

**Forward pass:**
```python
real_output = discriminator(real_imgs)  # D(x_real)
fake_output = discriminator(fake_imgs.detach())  # D(G(z))
```

**¿Qué es .detach()?**
```python
fake_imgs.detach()
```

- Detach "corta" el grafo computacional
- Significa: "No calcules gradientes a través de fake_imgs"
- ¿Por qué? Porque cuando entrenamos el Discriminador, NO queremos actualizar el Generador

**Sin detach:**
```
z → Generador → fake_imgs → Discriminador → loss
     ↑________________ gradientes fluyen aquí ✗
```

**Con detach:**
```
z → Generador → fake_imgs.detach() → Discriminador → loss
     ↑________ gradientes NO fluyen aquí ✓
```

**Binary Cross Entropy Loss:**
```python
BCE(pred, target) = -[target * log(pred) + (1 - target) * log(1 - pred)]
```

**Para imágenes reales (target=1):**
```
loss_real = -log(D(x_real))
```
- Si D(x_real) = 1 (correcto) → loss = -log(1) = 0 (mínimo)
- Si D(x_real) = 0 (incorrecto) → loss = -log(0) = ∞ (máximo)

**Para imágenes falsas (target=0):**
```
loss_fake = -log(1 - D(G(z)))
```
- Si D(G(z)) = 0 (correcto) → loss = -log(1) = 0 (mínimo)
- Si D(G(z)) = 1 (incorrecto) → loss = -log(0) = ∞ (máximo)

**Pérdida total del Discriminador:**
```python
loss_D = loss_real + loss_fake
```

Queremos que el Discriminador:
- Dé valores altos (cercanos a 1) para imágenes reales
- Dé valores bajos (cercanos a 0) para imágenes falsas

---

**Función de Pérdida del Generador (Vanilla GAN):**

```python
def compute_vanilla_loss_G(discriminator, fake_imgs):
    """
    Pérdida del Generador en Vanilla GAN.
    Usa el truco de maximizar log(D(G(z))) en lugar de minimizar log(1 - D(G(z))).
    """
    batch_size = fake_imgs.size(0)
    real_labels = torch.ones(batch_size, 1, 1, 1).to(fake_imgs.device)

    fake_output = discriminator(fake_imgs)

    # Truco: maximizar log(D(G(z))) = minimizar -log(D(G(z)))
    loss_G = nn.BCELoss()(fake_output, real_labels)

    return loss_G
```

#### El "Truco" del Generador:

**Pérdida original del paper:**
```
min_G log(1 - D(G(z)))
```

**Problema:** Cuando D es bueno, D(G(z)) ≈ 0, entonces:
```
log(1 - 0) = log(1) = 0
```
Gradiente ≈ 0 → vanishing gradients

**Truco propuesto en el paper:**
```
max_G log(D(G(z)))  =  min_G -log(D(G(z)))
```

**Implementación:**
```python
fake_output = discriminator(fake_imgs)
real_labels = torch.ones(...)  # Pretendemos que las falsas son "reales"
loss_G = BCELoss(fake_output, real_labels)
```

Esto es equivalente a minimizar `-log(D(G(z)))`.

**¿Por qué funciona mejor?**
Cuando D(G(z)) es pequeño:
- Pérdida original: `log(1 - ε) ≈ 0` (gradiente pequeño)
- Pérdida con truco: `-log(ε)` → muy grande (gradiente grande)

El Generador recibe señales más fuertes cuando está produciendo imágenes malas.

---

### Función de Pérdida de WGAN

```python
def compute_wgan_loss_C(critic, real_imgs, fake_imgs):
    """
    Pérdida del Crítico en WGAN.
    Estima la Wasserstein distance.
    """
    real_output = critic(real_imgs)
    fake_output = critic(fake_imgs.detach())

    # Wasserstein loss
    loss_C = -(torch.mean(real_output) - torch.mean(fake_output))

    # Para logging
    wasserstein_distance = torch.mean(real_output) - torch.mean(fake_output)

    return loss_C, wasserstein_distance.item()
```

#### Explicación:

**Sin Sigmoid:** El Crítico produce valores en (-∞, +∞), no en [0,1]

**Wasserstein Loss:**
```python
loss_C = -(E[C(x_real)] - E[C(G(z))])
       = -E[C(x_real)] + E[C(G(z))]
       = E[C(G(z))] - E[C(x_real)]
```

**¿Por qué el signo negativo?**
- Queremos **minimizar** la pérdida
- Pero queremos que `C(x_real)` sea grande y `C(G(z))` sea pequeño
- Entonces minimizamos `-(C(x_real) - C(G(z)))` = maximizamos `C(x_real) - C(G(z))`

**Interpretación:**
- Queremos que el Crítico dé puntajes **altos** a imágenes reales
- Queremos que el Crítico dé puntajes **bajos** a imágenes falsas
- La diferencia `E[C(x_real)] - E[C(G(z))]` es un estimado de la Wasserstein distance

**Weight Clipping (aplicado después de la actualización):**
```python
def clip_weights(critic, clip_value):
    for p in critic.parameters():
        p.data.clamp_(-clip_value, clip_value)
```

**Función de Pérdida del Generador (WGAN):**

```python
def compute_wgan_loss_G(critic, fake_imgs):
    """
    Pérdida del Generador en WGAN.
    """
    fake_output = critic(fake_imgs)

    # Queremos maximizar C(G(z)) = minimizar -C(G(z))
    loss_G = -torch.mean(fake_output)

    return loss_G
```

**Más simple que Vanilla GAN:**
```python
loss_G = -E[C(G(z))]
```

Queremos que el Crítico dé puntajes altos a nuestras imágenes falsas.

---

### Función de Pérdida de WGAN-GP

```python
def compute_gradient_penalty(critic, real_imgs, fake_imgs, device):
    """
    Calcula el gradient penalty para WGAN-GP.
    """
    batch_size = real_imgs.size(0)

    # Muestrear ε ~ U[0, 1]
    epsilon = torch.rand(batch_size, 1, 1, 1).to(device)

    # Interpolar entre real y fake
    interpolated = epsilon * real_imgs + (1 - epsilon) * fake_imgs
    interpolated = interpolated.requires_grad_(True)

    # Forward pass
    interpolated_output = critic(interpolated)

    # Calcular gradientes
    gradients = autograd.grad(
        outputs=interpolated_output,
        inputs=interpolated,
        grad_outputs=torch.ones_like(interpolated_output),
        create_graph=True,
        retain_graph=True,
    )[0]

    # Calcular norma de los gradientes
    gradients = gradients.view(batch_size, -1)
    gradient_norm = gradients.norm(2, dim=1)

    # Penalty: (||∇||₂ - 1)²
    gradient_penalty = torch.mean((gradient_norm - 1) ** 2)

    return gradient_penalty
```

#### Explicación Paso a Paso:

**1. Muestrear ε:**
```python
epsilon = torch.rand(batch_size, 1, 1, 1)
```
- Valores aleatorios entre 0 y 1
- Shape (batch, 1, 1, 1) para poder hacer broadcasting

**2. Interpolar:**
```python
interpolated = ε * real + (1 - ε) * fake
```

**Ejemplos:**
```
Si ε = 0: interpolated = fake (imagen 100% falsa)
Si ε = 0.5: interpolated = 0.5*real + 0.5*fake (mezcla 50/50)
Si ε = 1: interpolated = real (imagen 100% real)
```

**3. requires_grad_(True):**
```python
interpolated = interpolated.requires_grad_(True)
```

- Por default, los tensores de datos NO tienen gradientes habilitados
- Necesitamos calcular ∇C(interpolated), por lo que debemos habilitar gradientes

**4. Forward pass:**
```python
interpolated_output = critic(interpolated)
```

**5. Calcular gradientes con autograd.grad:**
```python
gradients = autograd.grad(
    outputs=interpolated_output,
    inputs=interpolated,
    grad_outputs=torch.ones_like(interpolated_output),
    create_graph=True,
    retain_graph=True,
)[0]
```

**Parámetros de autograd.grad:**

**`outputs`:** El tensor cuyo gradiente queremos calcular (C(x̂))

**`inputs`:** Respecto a qué queremos el gradiente (x̂)

**`grad_outputs`:** Gradientes de salida (necesario para scalar outputs)
- Es como el "dL/dy" en la chain rule
- Usamos `torch.ones_like(...)` porque queremos `∂C/∂x̂`

**`create_graph=True`:**
- Mantén el grafo computacional de los gradientes
- Necesario porque vamos a hacer backpropagation A TRAVÉS de los gradientes
- Sin esto, no podríamos calcular `∂(gradient_penalty)/∂(weights_critic)`

**`retain_graph=True`:**
- No elimines el grafo después de calcular gradientes
- Necesario porque vamos a usar el mismo grafo para el Generador más tarde

**6. Calcular norma:**
```python
gradients = gradients.view(batch_size, -1)  # Flatten
gradient_norm = gradients.norm(2, dim=1)  # Norma L2 por muestra
```

**`view(batch_size, -1)`:**
- Reshape de (batch, C, H, W) a (batch, C*H*W)
- Flatten todas las dimensiones excepto batch

**`.norm(2, dim=1)`:**
- Calcula la norma L2 (euclidiana) a través de dim=1
- Resultado: (batch,) con una norma por muestra

**Norma L2:**
```
||x||₂ = sqrt(x₁² + x₂² + ... + xₙ²)
```

**7. Gradient Penalty:**
```python
gradient_penalty = torch.mean((gradient_norm - 1) ** 2)
```

- Queremos que `gradient_norm ≈ 1`
- Penalizamos desviaciones con (gradient_norm - 1)²
- Promediamos sobre el batch

**Función de Pérdida del Crítico (WGAN-GP):**

```python
def compute_wgangp_loss_C(critic, real_imgs, fake_imgs, device, lambda_gp=10):
    """
    Pérdida del Crítico en WGAN-GP.
    """
    real_output = critic(real_imgs)
    fake_output = critic(fake_imgs.detach())

    # Wasserstein loss
    wasserstein_loss = -(torch.mean(real_output) - torch.mean(fake_output))

    # Gradient penalty
    gradient_penalty = compute_gradient_penalty(critic, real_imgs, fake_imgs, device)

    # Pérdida total
    loss_C = wasserstein_loss + lambda_gp * gradient_penalty

    return loss_C, wasserstein_loss.item(), gradient_penalty.item()
```

**Pérdida total:**
```
loss_C = E[C(x̃)] - E[C(x)] + λ·E[(||∇C(x̂)||₂ - 1)²]
         └── Wasserstein ──┘   └── Gradient Penalty ──┘
```

**λ = 10:** Coeficiente estándar del paper

---

## Celda 12-14: Loops de Entrenamiento

Ahora vienen las funciones que realmente entrenan los modelos.

### Loop de Entrenamiento de Vanilla GAN

```python
def train_vanilla_gan(generator, discriminator, dataloader, num_epochs, device):
    # Optimizadores
    opt_G = optim.Adam(generator.parameters(),
                       lr=VANILLA_LEARNING_RATE,
                       betas=VANILLA_BETAS)
    opt_D = optim.Adam(discriminator.parameters(),
                       lr=VANILLA_LEARNING_RATE,
                       betas=VANILLA_BETAS)

    # Listas para métricas
    G_losses = []
    D_losses = []

    for epoch in range(num_epochs):
        for i, (real_imgs, _) in enumerate(tqdm(dataloader, desc=f"Epoch {epoch+1}/{num_epochs}")):
            batch_size = real_imgs.size(0)
            real_imgs = real_imgs.to(device)

            # =================== Entrenar Discriminador ===================
            # Generar imágenes falsas
            z = torch.randn(batch_size, LATENT_DIM, 1, 1).to(device)
            fake_imgs = generator(z)

            # Calcular pérdida
            loss_D, _, _ = compute_vanilla_loss_D(discriminator, real_imgs, fake_imgs)

            # Actualizar
            opt_D.zero_grad()
            loss_D.backward()
            opt_D.step()

            # =================== Entrenar Generador ===================
            # Generar nuevas imágenes falsas
            z = torch.randn(batch_size, LATENT_DIM, 1, 1).to(device)
            fake_imgs = generator(z)

            # Calcular pérdida
            loss_G = compute_vanilla_loss_G(discriminator, fake_imgs)

            # Actualizar
            opt_G.zero_grad()
            loss_G.backward()
            opt_G.step()

            # Guardar métricas
            G_losses.append(loss_G.item())
            D_losses.append(loss_D.item())

    return G_losses, D_losses
```

#### Explicación del Loop:

**1. Configuración de Optimizadores:**
```python
opt_G = optim.Adam(generator.parameters(), ...)
opt_D = optim.Adam(discriminator.parameters(), ...)
```

**Dos optimizadores separados** porque entrenamos G y D independientemente.

**2. Loop sobre Épocas y Batches:**
```python
for epoch in range(num_epochs):
    for i, (real_imgs, _) in enumerate(dataloader):
```

**`(real_imgs, _)`:**
- `real_imgs`: las imágenes
- `_`: las etiquetas (las ignoramos en GANs no condicionales)

**3. Entrenamiento del Discriminador:**

**Paso 1: Generar imágenes falsas**
```python
z = torch.randn(batch_size, LATENT_DIM, 1, 1).to(device)
fake_imgs = generator(z)
```

**torch.randn:** Muestrea de una distribución Normal(0, 1)

**Paso 2: Calcular pérdida**
```python
loss_D, _, _ = compute_vanilla_loss_D(discriminator, real_imgs, fake_imgs)
```

**Paso 3: Actualizar pesos**
```python
opt_D.zero_grad()  # Limpia gradientes anteriores
loss_D.backward()  # Calcula gradientes
opt_D.step()       # Actualiza pesos
```

**¿Por qué zero_grad()?**
Por default, PyTorch **acumula** gradientes. Si no los limpias, se suman a los gradientes anteriores.

**4. Entrenamiento del Generador:**

**Similar al Discriminador, pero:**
- Generamos **nuevas** imágenes falsas (no reutilizamos las del Discriminador)
- Solo actualizamos el Generador, el Discriminador se queda fijo

**¿Por qué generar nuevas imágenes falsas?**
Porque el Discriminador acaba de ser actualizado, las imágenes falsas anteriores ya son "viejas".

---

### Loop de Entrenamiento de WGAN

```python
def train_wgan(generator, critic, dataloader, num_epochs, device):
    # Optimizadores (RMSProp en el paper original, aquí usamos Adam)
    opt_G = optim.Adam(generator.parameters(), lr=WGAN_LEARNING_RATE)
    opt_C = optim.Adam(critic.parameters(), lr=WGAN_LEARNING_RATE)

    G_losses = []
    C_losses = []
    W_distances = []

    for epoch in range(num_epochs):
        for i, (real_imgs, _) in enumerate(tqdm(dataloader)):
            batch_size = real_imgs.size(0)
            real_imgs = real_imgs.to(device)

            # ========== Entrenar Crítico (n_critic veces) ==========
            for _ in range(CRITIC_ITERATIONS):
                z = torch.randn(batch_size, LATENT_DIM, 1, 1).to(device)
                fake_imgs = generator(z)

                loss_C, w_dist = compute_wgan_loss_C(critic, real_imgs, fake_imgs)

                opt_C.zero_grad()
                loss_C.backward()
                opt_C.step()

                # Weight clipping
                clip_weights(critic, WGAN_CLIP_VALUE)

            # ========== Entrenar Generador ==========
            z = torch.randn(batch_size, LATENT_DIM, 1, 1).to(device)
            fake_imgs = generator(z)

            loss_G = compute_wgan_loss_G(critic, fake_imgs)

            opt_G.zero_grad()
            loss_G.backward()
            opt_G.step()

            # Guardar métricas
            G_losses.append(loss_G.item())
            C_losses.append(loss_C.item())
            W_distances.append(w_dist)

    return G_losses, C_losses, W_distances
```

#### Diferencias con Vanilla GAN:

**1. n_critic iteraciones:**
```python
for _ in range(CRITIC_ITERATIONS):  # 5 veces
    # Entrenar Crítico
```

**Por qué:** El Crítico necesita converger bien para estimar correctamente la Wasserstein distance.

**2. Weight Clipping:**
```python
clip_weights(critic, WGAN_CLIP_VALUE)
```

Después de cada actualización, clipeamos los pesos a [-c, c].

**3. Métricas adicionales:**
```python
W_distances.append(w_dist)
```

Guardamos la estimación de la Wasserstein distance, que debería correlacionar con la calidad de las imágenes.

---

### Loop de Entrenamiento de WGAN-GP

```python
def train_wgangp(generator, critic, dataloader, num_epochs, device):
    opt_G = optim.Adam(generator.parameters(),
                       lr=WGANGP_LEARNING_RATE,
                       betas=WGANGP_BETAS)
    opt_C = optim.Adam(critic.parameters(),
                       lr=WGANGP_LEARNING_RATE,
                       betas=WGANGP_BETAS)

    G_losses = []
    C_losses = []
    GP_values = []

    for epoch in range(num_epochs):
        for i, (real_imgs, _) in enumerate(tqdm(dataloader)):
            batch_size = real_imgs.size(0)
            real_imgs = real_imgs.to(device)

            # ========== Entrenar Crítico (n_critic veces) ==========
            for _ in range(CRITIC_ITERATIONS):
                z = torch.randn(batch_size, LATENT_DIM, 1, 1).to(device)
                fake_imgs = generator(z)

                loss_C, w_loss, gp = compute_wgangp_loss_C(
                    critic, real_imgs, fake_imgs, device, WGANGP_LAMBDA
                )

                opt_C.zero_grad()
                loss_C.backward()
                opt_C.step()

                # NO hay weight clipping en WGAN-GP

            # ========== Entrenar Generador ==========
            z = torch.randn(batch_size, LATENT_DIM, 1, 1).to(device)
            fake_imgs = generator(z)

            loss_G = compute_wgangp_loss_G(critic, fake_imgs)

            opt_G.zero_grad()
            loss_G.backward()
            opt_G.step()

            G_losses.append(loss_G.item())
            C_losses.append(loss_C.item())
            GP_values.append(gp)

    return G_losses, C_losses, GP_values
```

#### Diferencias con WGAN:

**1. NO hay weight clipping:**
```python
# En WGAN:
clip_weights(critic, WGAN_CLIP_VALUE)

# En WGAN-GP:
# (nada aquí - el gradient penalty ya enforce Lipschitz)
```

**2. Usa gradient penalty:**
```python
loss_C, w_loss, gp = compute_wgangp_loss_C(...)
```

**3. Betas diferentes en Adam:**
```python
betas=WGANGP_BETAS  # (0.5, 0.9)
```

---

## Celda 15-17: Evaluación con FID

La métrica FID (Fréchet Inception Distance) mide qué tan similares son las imágenes generadas a las reales.

### ¿Qué es el FID?

**Intuición:**
Compara las **estadísticas** de las imágenes reales vs. las generadas, usando una red pre-entrenada (Inception v3).

**Proceso:**
1. Pasa las imágenes reales por Inception → obtienes features
2. Pasa las imágenes generadas por Inception → obtienes features
3. Calcula la media (μ) y covarianza (Σ) de ambos conjuntos de features
4. Calcula la distancia de Fréchet entre las dos distribuciones:

```
FID = ||μ_real - μ_fake||² + Tr(Σ_real + Σ_fake - 2√(Σ_real·Σ_fake))
```

**Interpretación:**
- FID bajo = imágenes generadas parecidas a las reales
- FID alto = imágenes generadas muy diferentes de las reales
- FID = 0 sería perfecto (casi imposible de lograr)

**Valores típicos en CIFAR-10:**
- Muy bueno: FID < 20
- Bueno: FID 20-40
- Aceptable: FID 40-60
- Malo: FID > 60

### Implementación del FID

```python
from pytorch_fid import fid_score

def compute_fid(generator, dataloader, device, num_samples=10000):
    """
    Calcula FID entre imágenes reales y generadas.
    """
    # Crear carpetas temporales
    real_dir = "temp_real_images"
    fake_dir = "temp_fake_images"
    os.makedirs(real_dir, exist_ok=True)
    os.makedirs(fake_dir, exist_ok=True)

    # Guardar imágenes reales
    real_count = 0
    for real_imgs, _ in dataloader:
        for img in real_imgs:
            if real_count >= num_samples:
                break
            save_image(img, f"{real_dir}/{real_count}.png", normalize=True)
            real_count += 1
        if real_count >= num_samples:
            break

    # Generar y guardar imágenes falsas
    generator.eval()
    with torch.no_grad():
        for i in range(num_samples):
            z = torch.randn(1, LATENT_DIM, 1, 1).to(device)
            fake_img = generator(z)
            save_image(fake_img, f"{fake_dir}/{i}.png", normalize=True)

    # Calcular FID
    fid_value = fid_score.calculate_fid_given_paths(
        [real_dir, fake_dir],
        batch_size=50,
        device=device,
        dims=2048
    )

    # Limpiar carpetas temporales
    shutil.rmtree(real_dir)
    shutil.rmtree(fake_dir)

    return fid_value
```

#### Explicación:

**1. Guardar imágenes reales:**
```python
save_image(img, f"{real_dir}/{real_count}.png", normalize=True)
```

**normalize=True:** Escala de [-1,1] a [0,1] para guardado correcto

**2. Generar imágenes falsas:**
```python
generator.eval()  # Modo evaluación (desactiva dropout, etc.)
with torch.no_grad():  # No calcular gradientes (más rápido)
    z = torch.randn(1, LATENT_DIM, 1, 1).to(device)
    fake_img = generator(z)
```

**3. Calcular FID con pytorch-fid:**
```python
fid_value = fid_score.calculate_fid_given_paths(...)
```

**dims=2048:** Dimensionalidad de las features de Inception (capa pool3)

---

## Celda 18-20: Experimento Completo y Resultados

Finalmente, corremos el experimento completo y comparamos los tres modelos.

### Pseudocódigo del Experimento:

```
Para cada tipo de GAN (Vanilla, WGAN, WGAN-GP):
    1. Crear Generador y Discriminador/Crítico
    2. Entrenar por NUM_EPOCHS épocas
    3. Generar muestras visuales cada pocas épocas
    4. Guardar el modelo entrenado
    5. Calcular FID
    6. Graficar las curvas de pérdida

Comparar los tres modelos:
    - Calidad visual de las imágenes generadas
    - Valores de FID
    - Estabilidad de las curvas de pérdida
    - Tiempo de entrenamiento
```

### Visualización de Resultados

```python
def plot_training_curves(losses_dict, save_path):
    """
    Grafica las curvas de pérdida de los tres modelos.
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Vanilla GAN
    axes[0].plot(losses_dict['vanilla_G'], label='Generator', alpha=0.7)
    axes[0].plot(losses_dict['vanilla_D'], label='Discriminator', alpha=0.7)
    axes[0].set_title('Vanilla GAN')
    axes[0].set_xlabel('Iteration')
    axes[0].set_ylabel('Loss')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # WGAN
    axes[1].plot(losses_dict['wgan_G'], label='Generator', alpha=0.7)
    axes[1].plot(losses_dict['wgan_C'], label='Critic', alpha=0.7)
    axes[1].plot(losses_dict['wgan_W'], label='Wasserstein Dist', alpha=0.7)
    axes[1].set_title('WGAN')
    axes[1].set_xlabel('Iteration')
    axes[1].set_ylabel('Loss')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    # WGAN-GP
    axes[2].plot(losses_dict['wgangp_G'], label='Generator', alpha=0.7)
    axes[2].plot(losses_dict['wgangp_C'], label='Critic', alpha=0.7)
    axes[2].plot(losses_dict['wgangp_GP'], label='Gradient Penalty', alpha=0.7)
    axes[2].set_title('WGAN-GP')
    axes[2].set_xlabel('Iteration')
    axes[2].set_ylabel('Loss')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
```

### Tabla de Comparación de FID

```
| Modelo      | FID Score | Training Time | Stability |
|-------------|-----------|---------------|-----------|
| Vanilla GAN | 39.05     | ~2 hours      | Medium    |
| WGAN        | 52.18     | ~3 hours      | High      |
| WGAN-GP     | 50.94     | ~3 hours      | Very High |
```

---

## Conclusiones del Obligatorio

### Qué Aprendimos:

**1. Evolución de GANs:**
- Vanilla GAN introduce el framework adversarial, pero tiene problemas de estabilidad
- WGAN soluciona muchos problemas usando Wasserstein distance, pero weight clipping es limitante
- WGAN-GP elimina weight clipping con gradient penalty, logrando mayor estabilidad

**2. Trade-offs:**
- **Vanilla GAN:**
  - Ventajas: Entrena más rápido, puede dar buena calidad con setup óptimo
  - Desventajas: Inestable, mode collapse, métricas no confiables

- **WGAN:**
  - Ventajas: Más estable, métrica correlacionada con calidad
  - Desventajas: Weight clipping limita capacidad, gradientes problemáticos

- **WGAN-GP:**
  - Ventajas: Muy estable, funciona con muchas arquitecturas, métrica confiable
  - Desventajas: Más lento (gradient penalty es costoso computacionalmente)

**3. ¿Cuál es mejor?**

Depende del contexto:
- **Para experimentación rápida:** Vanilla GAN (con DCGAN architecture)
- **Para robustez arquitectural:** WGAN-GP (funciona con muchas arquitecturas sin tuning)
- **Para producción:** Probablemente Vanilla GAN bien tuneada o StyleGAN (evolución posterior)

**4. Lecciones prácticas:**
- Las funciones de pérdida importan MUCHO (JS vs Wasserstein hace gran diferencia)
- Los detalles importan (BatchNorm sí/no, learning rate, ratio de entrenamiento)
- No existe "el mejor modelo" - hay trade-offs
- Las métricas correlacionadas con calidad (como Wasserstein distance) son valiosas

---

## Apéndice: Todos los Hiperparámetros Explicados

### Por qué cada hiperparámetro tiene el valor que tiene:

#### LATENT_DIM = 128
**Origen:** Vanilla GAN usa 100, DCGAN populariza 128
**Por qué:** Balance entre variedad (128 dimensiones de control) y simplicidad
**Experimentos del paper:** 100-256 todos funcionan similarmente

#### GENERATOR_FEATURES = 128 y CRITIC_FEATURES = 128
**Origen:** DCGAN usa 64 para 64×64 images, escalamos proporcionalmente
**Por qué:** Control de capacidad del modelo
**Tu caso (RTX 4070):** Podrías usar 256 sin problemas

#### CRITIC_ITERATIONS = 5
**Origen:** Paper de WGAN (Algorithm 1)
**Por qué:** El Crítico aprende más rápido que el Generador, necesita más actualizaciones
**Sensibilidad:** 3-10 todos funcionan, 5 es estándar

#### VANILLA_LEARNING_RATE = 2e-4
**Origen:** DCGAN paper (Radford et al., 2015)
**Por qué:** Balance entre velocidad y estabilidad
**Historia:** Es el learning rate que "just works" para Adam en GANs

#### VANILLA_BETAS = (0.5, 0.999)
**Origen:** DCGAN paper
**Por qué β₁=0.5:** Menos momentum → más estable en adversarial training
**Por qué β₂=0.999:** Valor default de Adam, controla varianza

#### WGAN_LEARNING_RATE = 5e-5
**Origen:** WGAN paper (Algorithm 1)
**Por qué es menor:** El Crítico necesita converger suavemente para estimar bien Wasserstein
**Es 4x más lento** que Vanilla GAN porque también entrena 5x más el Crítico

#### WGAN_CLIP_VALUE = 0.01
**Origen:** WGAN paper
**Por qué 0.01:** Balance entre enforcer Lipschitz y no causar gradientes patológicos
**Problema:** No hay valor "correcto" (por eso WGAN-GP lo reemplaza)

#### WGANGP_LEARNING_RATE = 1e-4
**Origen:** WGAN-GP paper (Algorithm 1)
**Por qué:** Punto medio entre Vanilla (2e-4) y WGAN (5e-5)
**Robustez:** Funciona bien en rango 5e-5 a 2e-4

#### WGANGP_LAMBDA = 10
**Origen:** WGAN-GP paper
**Por qué 10:** Los autores probaron 1, 10, 100. λ=10 funcionó bien en TODO
**Robustez:** Es sorprendentemente robusto, 5-20 todos funcionan bien

#### WGANGP_BETAS = (0.5, 0.9)
**Origen:** WGAN-GP paper (usa (0, 0.9), nosotros usamos (0.5, 0.9))
**Por qué β₂=0.9:** Menos momentum de segundo orden → más responsivo
**Diferencia con Vanilla:** β₂=0.9 en lugar de 0.999

#### BATCH_SIZE = 64
**Origen:** Estándar en muchos papers
**Por qué 64:** Potencia de 2 (eficiente en GPU), balance memoria/estabilidad
**Tu GPU:** Podrías usar 128 o 256 sin problemas

#### NUM_EPOCHS = 1
**En tu código:** Solo para pruebas
**Valores reales:** 100-200 épocas para CIFAR-10

---

## 🎯 RESUMEN RÁPIDO PARA EXPLICAR EN CLASE

### Jensen-Shannon (JS) Divergence vs Wasserstein Distance

**Pregunta clave:** ¿Cómo medimos qué tan diferentes son las imágenes reales vs las generadas?

#### Jensen-Shannon Divergence (Vanilla GAN)

**En una oración:** Mide si puedes distinguir entre dos distribuciones, pero solo responde "SÍ (0.69)" o "NO (0)", sin valores intermedios.

**Analogía del Juego de Adivinar:**
- Urna Roja (real) y Urna Azul (falsa)
- Pregunta: "¿Puedo adivinar de qué urna vino cada bola?"
- Si puedo distinguirlas → JS = 0.69 (el máximo)
- Si son idénticas → JS = 0
- **Problema:** Aunque muevas las bolas más cerca (mejorando), JS sigue en 0.69 hasta que sean IDÉNTICAS

**Comportamiento:**
```
GAN mejorando:  Horrible → Mala → Buena → Casi perfecta → Perfecta
Jensen-Shannon:  0.69      0.69    0.69      0.69          0.00
                  ↑         ↑       ↑         ↑             ↑
                Diferente  Dif.    Dif.      Dif.       Idénticas
```

**Problema:** Es binaria, no te da feedback gradual → no puedes saber si estás mejorando

---

#### Wasserstein Distance (WGAN)

**En una oración:** Es como un GPS que te dice "estás a 100 metros... 90 metros... 50 metros... ¡llegaste!"

**Analogía de la Mudanza de Arena:**
1. Tienes dos playas con arena distribuida de forma diferente
2. Wasserstein mide: ¿cuánto esfuerzo necesitas para redistribuir la arena de una playa para que quede igual a la otra?
3. Esfuerzo = cantidad de arena × distancia que la mueves

**Ejemplo numérico:**
- Distribuciones muy diferentes → Wasserstein = 100 (mucha arena, lejos)
- Mejoras un poco → Wasserstein = 80 (¡bajó!)
- Mejoras más → Wasserstein = 50
- Perfecto → Wasserstein = 0

**Ventaja:** Te da feedback continuo en cada paso → sabes si estás mejorando

---

### Los 4 Problemas de Vanilla GAN (Súper Resumido)

**1. Training Instability (Inestabilidad)**
- Analogía: Partido de fútbol donde si un equipo se hace muy bueno, el otro no puede aprender
- Consecuencia: Pérdidas caóticas que suben y bajan sin patrón

**2. Mode Collapse (Colapso de Modos)**
- Analogía: Estudiante que solo presenta sobre matemáticas porque siempre saca 10
- Consecuencia: Generador produce solo 1 tipo de imagen, sin variedad

**3. Vanishing Gradients (Gradientes que Desaparecen)**
- Analogía: Crítico gastronómico que solo dice "0/10" sin darte detalles de qué mejorar
- Consecuencia: Generador no sabe hacia dónde mejorar

**4. Métrica No Correlacionada**
- Analogía: Usar tu peso para medir qué tan bien corres
- Consecuencia: El número de pérdida no te dice si las imágenes mejoran
- Causa: Jensen-Shannon se queda en 0.69 siempre

---

### ¿Cómo WGAN Soluciona Estos Problemas?

**Cambio principal:** Usar Wasserstein distance en vez de Jensen-Shannon

**Resultados:**
- ✅ Métrica correlacionada: Wasserstein baja cuando las imágenes mejoran
- ✅ Sin vanishing gradients: Siempre hay dirección para mejorar
- ✅ Más estabilidad: Feedback continuo ayuda al entrenamiento

**Trade-off:**
- ⚠️ WGAN usa "weight clipping" que introduce nuevos problemas
- ✅ WGAN-GP soluciona eso con "gradient penalty"

---

### Puntos Clave para Memorizar

1. **JS divergence pregunta:** "¿Puedo distinguir entre real y falso?" → Responde solo SÍ (0.69) o NO (0)
2. **Wasserstein pregunta:** "¿Cuánto esfuerzo para transformar falso en real?" → Responde con números continuos (100... 80... 50... 0)
3. **JS divergence = interruptor binario** → malo para entrenar (no sabes si mejoras)
4. **Wasserstein = GPS con distancia continua** → bueno para entrenar (sabes cada mejora)
5. **El valor 0.69 viene de log(2)** → es el máximo de JS cuando las distribuciones no se superponen
6. **Feedback continuo = clave para aprendizaje** → necesitas saber si mejoras poco a poco, no solo "perfecto" vs "imperfecto"

---

## Referencias

**Papers Principales:**
1. Goodfellow et al. (2014). "Generative Adversarial Nets"
2. Radford et al. (2015). "Unsupervised Representation Learning with Deep Convolutional GANs" (DCGAN)
3. Arjovsky et al. (2017). "Wasserstein GAN"
4. Gulrajani et al. (2017). "Improved Training of Wasserstein GANs"

**Implementaciones de Referencia:**
- PyTorch-GAN: https://github.com/eriklindernoren/PyTorch-GAN
- WGAN-GP Official: https://github.com/igul222/improved_wgan_training

**Lecturas Recomendadas:**
- Tutorial de GANs de Ian Goodfellow: NIPS 2016 Tutorial
- Distill.pub article on GANs: https://distill.pub/2017/aia/
- Lilian Weng's blog on GANs: https://lilianweng.github.io/lil-log/2017/08/20/from-GAN-to-WGAN.html

---

**Fin de la Explicación Completa del Obligatorio**

¡Espero que esta explicación te ayude a entender cada aspecto de tu código y de la evolución de GANs! Si tienes preguntas sobre alguna parte específica, no dudes en preguntar.
