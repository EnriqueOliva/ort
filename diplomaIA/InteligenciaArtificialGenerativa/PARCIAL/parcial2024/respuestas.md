# Respuestas del Parcial - Inteligencia Artificial Generativa 2024

**Facultad de Ingeniería - Universidad ORT**

| | |
|---|---|
| **Fecha:** 09/12/2024 | **Duración:** 2 h |
| **Evaluación:** Parcial | **Uso de Calculadora:** SI |
| **Materia:** Inteligencia Artificial Generativa | **Uso de Material:** NO |
| **Turno:** Nocturno | **Puntaje Máximo/Mínimo:** 30/1 Puntos |

---

## Ejercicio 1 - Language Models (LMs) (10 puntos)

### 1. ¿Qué es un Language Model?

**Respuesta corta (para el parcial):**
> Un Language Model es un sistema que recibe una secuencia de tokens y emite una distribución de probabilidad sobre el siguiente token. Formalmente: LM: Σ* → P(Σ ∪ {END}).

**Explicación detallada:**

Un Language Model (modelo de lenguaje) es un modelo autorregresivo aplicado a texto. Su función es, dado un contexto (una secuencia de tokens), predecir la probabilidad de cada posible token siguiente.

Como lo definió el profesor en clase:
> "Son sistemas que emiten distribuciones de probabilidad. Le imputa una tira de tokens y emite el siguiente símbolo."

Características clave:
- **Entrada:** Una secuencia de tokens (pueden ser palabras, caracteres o sub-palabras)
- **Salida:** Una distribución de probabilidad sobre el vocabulario (incluyendo un token especial de fin)
- **Proceso:** Es autorregresivo, es decir, cada predicción depende de las anteriores

La notación formal es:
```
LM: Σ* → P(Σ ∪ {END})
```
Donde Σ* representa todas las posibles secuencias de tokens del vocabulario Σ, y la salida es una distribución de probabilidad sobre el vocabulario más un token de fin de secuencia.

---

### 2. Implementa en pseudocódigo el proceso de generación de secuencias de un LM.

**Respuesta corta (para el parcial):**
```
función generar_secuencia(prompt, max_tokens):
    tokens = tokenizar(prompt)
    mientras len(tokens) < max_tokens:
        logits = modelo(tokens)
        probabilidades = softmax(logits[-1])
        nuevo_token = muestrear(probabilidades)
        si nuevo_token == END: terminar
        tokens.agregar(nuevo_token)
    retornar destokenizar(tokens)
```

**Explicación detallada:**

Antes del pseudocódigo, hay que entender tres conceptos que se usan adentro:

**¿Qué es el vocabulario?**
Es la lista FIJA de todas las palabras (o pedazos de palabra) que el modelo conoce. Se define UNA vez antes de entrenar y nunca cambia. Ejemplo simplificado: {"el"=0, "gato"=1, "come"=2, "pescado"=3, "perro"=4, ...} hasta 50,000 palabras. Si una palabra no está en la lista, se parte en pedazos más chicos que sí estén (por eso "inteligencia" puede ser "intel" + "igencia", dos tokens). El modelo solo puede predecir palabras que estén en su vocabulario.

**¿Qué son los tokens?**
Son las palabras (o pedazos de palabra) convertidos a números usando ese vocabulario. "El gato come" se convierte en [0, 1, 2] (usando el ejemplo de arriba). La red neuronal solo entiende números, no texto. Tokenizar = convertir texto a números. Destokenizar = convertir números de vuelta a texto.

**¿Qué son los logits?**
Cuando el modelo recibe una secuencia de tokens (ej: [0, 1, 2] = "el gato come"), devuelve un número por cada palabra del vocabulario. Si el vocabulario tiene 50,000 palabras, devuelve 50,000 números. Estos números se llaman logits. Un logit ALTO para una palabra significa que el modelo cree que esa palabra es buena continuación. Un logit BAJO significa lo contrario. PERO los logits NO son probabilidades — son números crudos que pueden ser positivos, negativos, lo que sea. Para convertirlos en probabilidades (porcentajes que suman 100%) se les aplica softmax.

Ahora sí, el pseudocódigo paso a paso:

```
FUNCIÓN generar_secuencia(prompt, max_tokens):

    # ══════════════════════════════════════════════════════════════
    # PASO 1: TOKENIZAR
    # ══════════════════════════════════════════════════════════════
    # La red no entiende texto, solo números.
    # Tokenizar convierte "el gato come" → [0, 1, 2]
    # Cada número es un ID del vocabulario.
    # A partir de acá, todo se trabaja con estos números.
    secuencia = tokenizar(prompt)

    # ══════════════════════════════════════════════════════════════
    # PASO 2: LOOP — generar una palabra a la vez
    # ══════════════════════════════════════════════════════════════
    # "secuencia" arranca siendo el prompt tokenizado (ej: [0, 1, 2]).
    # En cada vuelta del loop se agrega un token más al final.
    # Vuelta 1: secuencia = [0, 1, 2]           → "el gato come"
    # Vuelta 2: secuencia = [0, 1, 2, 3]        → "el gato come pescado"
    # Vuelta 3: secuencia = [0, 1, 2, 3, 47]    → "el gato come pescado fresco"
    # ... y así hasta que el modelo decida parar.
    MIENTRAS longitud(secuencia) < max_tokens:

        # ──────────────────────────────────────────────────────────
        # 2.1 METER LA SECUENCIA AL MODELO
        # ──────────────────────────────────────────────────────────
        # Le damos la secuencia que llevamos hasta ahora
        # (que crece en cada vuelta del loop).
        #
        # El modelo la procesa y devuelve logits: 50,000 números
        # (uno por cada palabra del vocabulario).
        # Estos números dicen "qué tan buena continuación sería
        # cada palabra del vocabulario".
        #
        # ¿PARA QUÉ? Para saber qué palabra viene después.
        logits = modelo_forward(secuencia)

        # ──────────────────────────────────────────────────────────
        # 2.2 AGARRAR SOLO LOS LOGITS DE LA ÚLTIMA POSICIÓN
        # ──────────────────────────────────────────────────────────
        # El modelo devuelve logits para TODAS las posiciones,
        # pero solo nos importa la última, porque esa es la predicción
        # de la SIGUIENTE palabra (la que aún no existe).
        # ¿PARA QUÉ? No nos importa "qué vendría después de la palabra 1"
        # ni "qué vendría después de la palabra 2". Solo nos importa
        # "qué viene después de la ÚLTIMA palabra".
        logits_siguiente = logits[-1]

        # ──────────────────────────────────────────────────────────
        # 2.3 CONVERTIR LOGITS A PROBABILIDADES (SOFTMAX)
        # ──────────────────────────────────────────────────────────
        # logits_siguiente es un vector de 50,000 números crudos.
        # Softmax los convierte en 50,000 probabilidades que suman 1.
        # Ejemplo: [2.5, 1.0, -0.3, ...] → [0.30, 0.07, 0.02, ...]
        #           ↑ logit alto              ↑ probabilidad alta
        # ¿PARA QUÉ? Porque necesitamos probabilidades para poder
        # elegir la siguiente palabra (no se puede "elegir" de números crudos).
        probabilidades = softmax(logits_siguiente)

        # ──────────────────────────────────────────────────────────
        # 2.4 ELEGIR UN TOKEN (MUESTREAR)
        # ──────────────────────────────────────────────────────────
        # Ahora tenemos probabilidades. Hay que elegir UNA palabra.
        # Formas de elegir:
        #   - Greedy: siempre la de mayor probabilidad (aburrido, repetitivo)
        #   - Top-K: elegir al azar entre las K más probables
        #   - Top-P: elegir al azar entre las que suman hasta P% de probabilidad
        # ¿PARA QUÉ? Esta elección es lo que GENERA el texto.
        # La misma distribución puede dar palabras distintas cada vez
        # (por eso ChatGPT puede responder diferente a la misma pregunta).
        nuevo_token = muestrear_de_distribucion(probabilidades)

        # ──────────────────────────────────────────────────────────
        # 2.5 ¿ES EL TOKEN DE FIN?
        # ──────────────────────────────────────────────────────────
        # Existe un token especial que significa "ya terminé de hablar".
        # Si el modelo lo elige, paramos.
        SI nuevo_token == TOKEN_FIN:
            SALIR DEL BUCLE

        # ──────────────────────────────────────────────────────────
        # 2.6 AGREGAR EL TOKEN Y REPETIR
        # ──────────────────────────────────────────────────────────
        # El token elegido se agrega al final de la secuencia.
        # Ahora la secuencia es un token más larga.
        # En la siguiente vuelta del loop, el modelo recibe esta
        # secuencia más larga y predice la SIGUIENTE palabra.
        secuencia.agregar(nuevo_token)

    # ══════════════════════════════════════════════════════════════
    # PASO 3: DESTOKENIZAR
    # ══════════════════════════════════════════════════════════════
    # Convertir los números de vuelta a texto.
    # [15, 234, 89, 712, 45] → "el gato come pescado fresco"
    texto_generado = destokenizar(secuencia)
    RETORNAR texto_generado
```

**Ejemplo concreto de una vuelta del loop:**

```
Secuencia actual: [15, 234, 89]  →  "el gato come"

Paso 2.1: modelo([15, 234, 89]) → logits para cada posición
Paso 2.2: agarrar solo los logits de la posición 3 (la última)
           → [2.5, -1.0, 0.3, 4.1, ..., -0.8]  (50,000 números crudos)
Paso 2.3: softmax → [0.05, 0.001, 0.02, 0.30, ..., 0.0002]
           "pescado" tiene 0.30, "carne" tiene 0.05, "mucho" tiene 0.02...
Paso 2.4: muestrear → cae "pescado" (token 712)
Paso 2.5: ¿es fin? No.
Paso 2.6: secuencia = [15, 234, 89, 712]  →  "el gato come pescado"

Siguiente vuelta: el modelo recibe [15, 234, 89, 712] y predice qué sigue...
```

**¿Por qué funciona así?**

Esto se basa en la regla de la cadena para probabilidades:
```
P(x₁, x₂, ..., xₙ) = P(x₁) × P(x₂|x₁) × P(x₃|x₁,x₂) × ... × P(xₙ|x₁,...,xₙ₋₁)
```

El modelo predice cada P(xᵢ|x₁,...,xᵢ₋₁), es decir, la probabilidad del token i dado todos los anteriores.

---

### 3. ¿Existe alguna diferencia a la hora de muestrear si este LM es un transformer, un MLP o una RNN?

**Respuesta corta (para el parcial):**
> No hay diferencia a la hora de muestrear. El proceso de muestreo es agnóstico de la arquitectura: siempre se obtiene una distribución de probabilidad sobre el vocabulario (via softmax) y se muestrea de ella. La arquitectura afecta cómo se computan los logits, no cómo se muestrea de ellos.

**Explicación detallada:**

El proceso de muestreo es **independiente de la arquitectura interna del modelo**. Esto es porque:

1. **La interfaz es la misma:** Todas las arquitecturas producen como salida un vector de logits del tamaño del vocabulario.

2. **El muestreo opera sobre probabilidades:** Después de aplicar softmax a los logits, obtenemos una distribución de probabilidad. El muestreo se hace sobre esta distribución, sin importar cómo se calcularon los logits.

3. **Es un enfoque agnóstico del modelo:** Como explicó el profesor sobre los modelos autorregresivos: "Esto hasta este momento es agnóstico del modelo que estoy usando." El profesor mencionó que "podría tener una tostadora" - lo único que importa es que la salida sea una distribución de probabilidad válida.

**Lo que SÍ cambia entre arquitecturas:**

| Aspecto | MLP | RNN | Transformer |
|---------|-----|-----|-------------|
| Cómo procesa el contexto | Ventana fija | Secuencial con estado oculto | Atención sobre todo el contexto |
| Velocidad de entrenamiento | Rápido pero limitado | Secuencial (lento) | Paralelizable |
| Manejo de dependencias largas | Pobre | Difícil (vanishing gradient) | Excelente |
| Cómputo de logits | Directamente | Recursivamente | Con mecanismo de atención |

**Pero el muestreo final es idéntico:**
```
logits = modelo(contexto)        # Esto cambia según la arquitectura
probabilidades = softmax(logits) # Esto es igual
token = muestrear(probabilidades) # Esto es igual
```

---

## Ejercicio 2 - Generative Adversarial Networks (GANs) (8 puntos)

### 1. Explica, con un esquema y pseudocódigo el funcionamiento de las GANs, tanto en entrenamiento como en inferencia.

**Respuesta corta (para el parcial):**
> Las GANs usan dos redes: un Generador (G) que crea datos falsos desde ruido, y un Discriminador (D) que clasifica datos como reales o falsos. Se entrenan alternadamente: D aprende a detectar falsificaciones, G aprende a engañar a D. En inferencia, solo se usa G para generar.

**Explicación detallada:**

#### Arquitectura General

```
        ESQUEMA DE UNA GAN

    [Ruido Z ~ N(0,1)] ──────┐
                             │
                             ▼
                      ┌──────────────┐
                      │  GENERADOR   │
                      │     (G)      │
                      └──────────────┘
                             │
                             ▼
                      [Imagen Falsa X̂]
                             │
                             ▼
                      ┌──────────────┐
    [Datos Reales X]─▶│DISCRIMINADOR │──▶ [Real/Falso]
                      │     (D)      │    (número 0-1)
                      └──────────────┘
```

**Componentes:**

- **Generador (G):** Red neuronal que transforma ruido aleatorio Z en datos sintéticos. G: Z → X̂
- **Discriminador (D):** Red neuronal clasificadora que determina si un dato es real o falso. D: X → [0,1]

#### Antes del pseudocódigo: las ideas clave

**La GAN tiene dos redes que se entrenan POR TURNOS, nunca al mismo tiempo.**

Turno 1 — entrenar al policía (D): le mostramos fotos reales y fotos falsas. Queremos que aprenda a distinguirlas. El falsificador (G) NO se toca en este turno.

Turno 2 — entrenar al falsificador (G): G genera fotos falsas y se las pasamos al policía. Queremos que el policía se equivoque y diga "es real". El policía (D) NO se toca en este turno.

**¿Qué es el ruido z?** Es un vector de números aleatorios (ej: 100 números sacados de una distribución normal). Es la "semilla" del generador. De cada ruido distinto sale una imagen distinta. El generador aprendió a convertir estos números aleatorios en imágenes.

**¿Qué es .detach()?** Cuando entrenamos al policía (D), necesitamos pasarle imágenes falsas de G. Pero NO queremos que este paso modifique a G (porque es el turno de D, no de G). El .detach() corta la conexión: le dice a PyTorch "usá esta imagen pero olvidate de cómo se generó, no le pases gradientes a G". Sin .detach(), al hacer backpropagation los gradientes llegarían hasta G y lo modificarían, que es justo lo que NO queremos en el turno de D.

**¿Qué es BCE?** Binary Cross-Entropy. Es una función que mide qué tan lejos está una predicción de lo que queríamos. Si queríamos que D diga 1 (real) y dijo 0.9, el error es bajo. Si dijo 0.2, el error es alto.

**¿Qué son optimizer.zero_grad(), loss.backward(), optimizer.step()?** Son los tres pasos estándar de PyTorch para actualizar los pesos de una red:
1. zero_grad() = borrar los gradientes del paso anterior (si no, se acumulan)
2. backward() = calcular los gradientes (cuánto y en qué dirección ajustar cada peso)
3. step() = aplicar esos gradientes (mover los pesos)

#### Régimen de Entrenamiento (Pseudocódigo)

```
FUNCIÓN entrenar_GAN(datos_reales, épocas, K):

    G = inicializar_generador()
    D = inicializar_discriminador()

    PARA cada época EN épocas:
        PARA cada batch_real EN datos_reales:

            # ═══════════════════════════════════════════════════════
            # TURNO 1: ENTRENAR AL POLICÍA (D)
            # El falsificador G está congelado. Solo se ajusta D.
            # ═══════════════════════════════════════════════════════
            PARA k EN rango(K):

                # Paso A: G genera imágenes falsas a partir de ruido
                # z es un vector de 100 números aleatorios (la "semilla")
                # G convierte esa semilla en una imagen
                z = muestrear_normal(0, 1, tamaño=batch_size)
                batch_falso = G(z)

                # Paso B: D mira las imágenes reales y dice un número
                # Queremos que diga algo cercano a 1 ("creo que es real")
                pred_real = D(batch_real)

                # Paso C: D mira las imágenes falsas y dice un número
                # Queremos que diga algo cercano a 0 ("creo que es falsa")
                # .detach() = "usá esta imagen pero NO toques a G"
                pred_falso = D(batch_falso.detach())

                # Paso D: Calcular qué tan bien lo hizo D
                # BCE compara lo que D dijo vs lo que queríamos que diga
                loss_D_real = BCE(pred_real, unos)     # ¿dijo ~1 para las reales?
                loss_D_falso = BCE(pred_falso, ceros)  # ¿dijo ~0 para las falsas?
                loss_D = loss_D_real + loss_D_falso

                # Paso E: Ajustar los pesos de D (y SOLO de D)
                optimizer_D.zero_grad()   # borrar gradientes viejos
                loss_D.backward()         # calcular gradientes nuevos
                optimizer_D.step()        # mover los pesos de D

            # ═══════════════════════════════════════════════════════
            # TURNO 2: ENTRENAR AL FALSIFICADOR (G)
            # El policía D está congelado. Solo se ajusta G.
            # ═══════════════════════════════════════════════════════

            # Paso A: G genera imágenes falsas nuevas
            z = muestrear_normal(0, 1, tamaño=batch_size)
            batch_falso = G(z)

            # Paso B: Se las pasamos a D
            # Ahora NO usamos .detach() porque SÍ queremos que los
            # gradientes lleguen hasta G (es su turno de aprender)
            pred_falso = D(batch_falso)

            # Paso C: Calcular qué tan bien lo hizo G
            # TRUCO: le decimos a BCE que compare contra 1 (no contra 0)
            # Aunque la imagen ES falsa, queremos que D CREA que es real.
            # Si D dijo 0.9 ("creo que es real") → el error es bajo → G lo engañó bien
            # Si D dijo 0.1 ("creo que es falsa") → el error es alto → G falló
            loss_G = BCE(pred_falso, unos)

            # Paso D: Ajustar los pesos de G (y SOLO de G)
            optimizer_G.zero_grad()
            loss_G.backward()
            optimizer_G.step()
```

#### Régimen de Inferencia (Pseudocódigo)

```
FUNCIÓN generar_datos(G_entrenado, cantidad):

    # Solo usamos el generador, descartamos D

    # Muestrear ruido del mismo tipo usado en entrenamiento
    z = muestrear_normal(0, 1, tamaño=cantidad)

    # Pasar por el generador
    datos_generados = G_entrenado(z)

    RETORNAR datos_generados
```

**Nota importante:** En inferencia, el discriminador ya no se usa. Solo se necesita el generador entrenado y ruido aleatorio.

---

### 2. ¿Cuáles son las dificultades presentes al entrenar este tipo de arquitectura?

**Respuesta corta (para el parcial):**
> Las principales dificultades son: (1) Inestabilidad del entrenamiento - es difícil mantener G y D balanceados; (2) Mode collapse - G genera un solo tipo de dato; (3) Vanishing gradients - cuando D es muy bueno, G no recibe señales útiles; (4) No hay métrica clara de convergencia.

**Explicación detallada:**

#### 1. **Inestabilidad del Entrenamiento**
El entrenamiento es como un equilibrio delicado entre dos oponentes. Si uno se vuelve demasiado dominante, el entrenamiento colapsa.

Como dijo el profesor:
> "Literalmente es mejor arrancar el entrenamiento de nuevo que intentar recuperarse."

El balance se mantiene mediante:
- Learning rates diferentes (D típicamente más bajo)
- Ratio de entrenamiento K (entrenar D más veces que G)

#### 2. **Mode Collapse (Colapso de Modos)**
G aprende a generar solo un tipo de dato porque engaña exitosamente a D con él.

Como explicó el profesor:
> "Si bien aprenden a generar, aprenden a generar un tipo de datos porque nada en el modelo nos incentiva a la variedad."

Ejemplo: Si entrenas para generar dígitos 0-9, G puede aprender a generar solo "3" perfectos e ignorar los demás dígitos.

#### 3. **Vanishing Gradients (Gradientes que Desaparecen)**
Al inicio del entrenamiento, D detecta fácilmente las imágenes falsas de G (que son muy malas). Esto produce gradientes muy pequeños para G, haciendo que no aprenda.

El paper original propone un truco: en lugar de minimizar log(1-D(G(z))), maximizar log(D(G(z))) - esto produce gradientes más estables.

#### 4. **No Hay Métrica Clara de Convergencia**
A diferencia de otros modelos donde la pérdida baja consistentemente:
> "Las pérdidas de G y D oscilan y no necesariamente una pérdida baja significa mejor modelo."

La única forma confiable de evaluar es inspeccionar visualmente las imágenes generadas.

#### 5. **Sensibilidad a Hiperparámetros**
Pequeños cambios en learning rate, arquitectura, o batch size pueden hacer que el entrenamiento falle completamente.

Como dijo Juan en clase:
> "Es un arte" encontrar los hiperparámetros correctos.

---

## Ejercicio 3 - Diffusion Models (4 puntos)

### 1. Implementa en pseudocódigo el paso de inferencia de un modelo de difusión para generar nuevas muestras. Explica cada paso del proceso.

**Respuesta corta (para el parcial):**
```
función generar_imagen(modelo, T_pasos):
    x_T = muestrear_ruido_puro()  # Imagen de ruido gaussiano
    PARA t = T hasta 1:
        ruido_predicho = modelo(x_t, t)
        x_{t-1} = quitar_ruido(x_t, ruido_predicho, t)
    retornar x_0  # Imagen generada
```

**Explicación detallada:**

#### Contexto
Los modelos de difusión tienen dos procesos:
1. **Forward (entrenamiento):** Agregar ruido gradualmente a una imagen real
2. **Backward (inferencia):** Quitar ruido gradualmente para generar una imagen

En inferencia solo usamos el proceso **backward** (denoising).

#### Pseudocódigo de Inferencia

```
FUNCIÓN generar_imagen(modelo_denoising, T, betas):
    """
    modelo_denoising: Red entrenada para predecir el ruido
    T: Número de pasos de difusión (típicamente 1000)
    betas: Schedule de varianza para cada paso
    """

    # ════════════════════════════════════════════════════════
    # PASO 1: Partir de ruido puro
    # ════════════════════════════════════════════════════════
    # Muestrear ruido gaussiano con la misma forma que la imagen deseada
    x_T = muestrear_normal(media=0, varianza=1, forma=dimensión_imagen)

    # El ruido inicial es nuestra "imagen" de partida
    x_actual = x_T

    # ════════════════════════════════════════════════════════
    # PASO 2: Iterar quitando ruido (de t=T hasta t=1)
    # ════════════════════════════════════════════════════════
    PARA t DESDE T HASTA 1:

        # 2.1 Predecir el ruido presente en x_actual
        # El modelo recibe la imagen ruidosa Y el timestep t
        ruido_predicho = modelo_denoising(x_actual, t)

        # 2.2 Calcular la imagen del paso anterior (menos ruidosa)
        # Usando la fórmula de denoising:
        # x_{t-1} = (1/√α_t) * (x_t - (β_t/√(1-ᾱ_t)) * ruido_predicho) + σ_t * z

        alpha_t = 1 - betas[t]
        alpha_acumulado_t = producto(alpha_i para i=1 hasta t)

        # Término principal: estimar x_{t-1} a partir de x_t
        media_estimada = (1/sqrt(alpha_t)) * (
            x_actual - (betas[t] / sqrt(1 - alpha_acumulado_t)) * ruido_predicho
        )

        # Agregar ruido estocástico (excepto en el último paso)
        SI t > 1:
            z = muestrear_normal(0, 1, forma=dimensión_imagen)
            varianza = calcular_varianza(betas, t)
            x_anterior = media_estimada + sqrt(varianza) * z
        SINO:
            x_anterior = media_estimada  # Sin ruido en el paso final

        # Actualizar para la siguiente iteración
        x_actual = x_anterior

    # ════════════════════════════════════════════════════════
    # PASO 3: Retornar la imagen generada
    # ════════════════════════════════════════════════════════
    x_0 = x_actual  # Después de T pasos, tenemos la imagen final

    RETORNAR x_0
```

#### Explicación de Cada Paso

1. **Partir de ruido puro (x_T):**
   - Muestreamos una imagen de ruido gaussiano puro (media 0, varianza 1)
   - Esta es nuestra "imagen inicial" que vamos a refinar
   - Tiene la misma dimensión que las imágenes que queremos generar

2. **Iterar quitando ruido:**
   - En cada paso t, el modelo predice cuánto ruido hay en la imagen actual
   - Usando esa predicción, calculamos cómo era la imagen un paso antes (menos ruidosa)
   - El proceso es gradual: no quitamos todo el ruido de golpe, sino poquito a poquito
   - El timestep t le dice al modelo "cuánto ruido hay aproximadamente"

3. **¿Por qué se agrega un poquito de ruido nuevo en cada paso?**
   - Esto viene de la matemática del paper DDPM: el proceso inverso (quitar ruido) no es simplemente "restar el ruido predicho". La fórmula exacta del paso inverso incluye un término de ruido pequeño (σ_t × z), porque el proceso original de agregar ruido también era aleatorio, y para revertirlo correctamente hay que respetar esa aleatoriedad.
   - Efecto práctico: si NO se agrega ese ruido, el modelo siempre genera la misma imagen a partir del mismo ruido inicial (se vuelve determinístico). Con el ruido, partiendo del mismo punto se pueden generar imágenes distintas.
   - En el último paso (t=1) no se agrega, porque ya estamos en la imagen final y no queremos ensuciarla.
   - Este detalle no cambia la idea conceptual (el modelo quita ruido paso a paso), pero es parte de la fórmula que aparece en el pseudocódigo.

4. **Retornar la imagen final:**
   - Después de T pasos, x_0 es una imagen "limpia" (sin ruido)
   - Si el modelo está bien entrenado, esta imagen pertenece a la distribución de los datos de entrenamiento

#### ¿Por qué funciona?

Como explicó el profesor:
> "El dato tiene la misma estructura que el latente... arranc una imagen que es ruido y le voy pasando varias iteraciones donde voy eliminando el ruido."

El modelo aprendió durante el entrenamiento cómo se ve el proceso de agregar ruido a imágenes reales. En inferencia, invierte ese proceso: sabe qué ruido quitar para que algo que parece ruido puro se convierta gradualmente en una imagen real.

---

## Ejercicio 4 - Variational Autoencoders (VAEs) (8 puntos)

### 1. Reparametrizing the sampling layer

```
Original form:                    Reparametrized form:

     ┌───┐                              ┌───┐
     │ f │                    Backprop  │ f │
     └─┬─┘                        ↓     └─┬─┘
       │                         ∂f/∂z    │
     ┌─┴─┐                       ↓      ┌─┴─┐
     │ z │  z ~ p_φ(z|x)               │ z │  z = g(φ, x, ε)
     └─┬─┘                       ↓     └─┬─┘
       │                        ∂f/∂φ    │         ┌───┐
     ┌─┴─┐                       ↓      ┌─┴─┐      │ ε │ ~ N(0,1)
     │ φ │───────│ x │                 │ φ │──│ x │──┴───┘
     └───┘       └───┘                 └───┘  └───┘

◆ Deterministic node
● Stochastic node
```

**Se pide:** Explique, al menos intuitivamente, porque es necesaria la forma reparametrizada de esta expresión en el contexto del entrenamiento de las VAEs.

**Respuesta corta (para el parcial):**
> La reparametrización es necesaria porque no se puede hacer backpropagation a través de un nodo estocástico (muestreo aleatorio). Al expresar z = μ + σ × ε, donde ε ~ N(0,1) es independiente de los parámetros φ, movemos la aleatoriedad a un nodo que no depende de φ, permitiendo calcular ∂f/∂φ y entrenar con gradientes.

**Explicación detallada:**

#### El Problema

En un VAE, el encoder produce parámetros de una distribución (μ y σ), y necesitamos muestrear z de esa distribución para pasarlo al decoder.

**Forma original:**
```
x → [Encoder con φ] → μ_φ(x), σ_φ(x) → [MUESTREO de N(μ,σ)] → z → [Decoder] → x̂
```

El problema es el paso de muestreo. Como explicó el profesor:
> "Nosotros tenemos una variable aleatoria con parámetros entrenables. Esto nunca les pasó con Matías."

**¿Por qué no podemos derivar a través del muestreo?**

Cuando muestreamos z ~ N(μ_φ, σ_φ), el proceso es:
1. La distribución de z DEPENDE de φ (los parámetros del encoder)
2. Para hacer backpropagation, necesitamos calcular ∂Loss/∂φ
3. Pero ∂z/∂φ no está definido porque z es aleatorio

Matemáticamente, si queremos calcular:
```
∇_φ E_{z~p_φ(z|x)}[f(z)]
```

No podemos simplemente "meter la derivada adentro" de la esperanza porque p_φ(z|x) depende de φ.

#### La Solución: Reparametrización

**Forma reparametrizada:**
```
x → [Encoder con φ] → μ_φ(x), σ_φ(x)
                                       ↘
                                         z = μ_φ(x) + σ_φ(x) × ε  → [Decoder] → x̂
                                       ↗
                      ε ~ N(0,1) [fijo, NO depende de φ]
```

Ahora:
- ε se muestrea de N(0,1), que NO depende de φ
- z se calcula de forma DETERMINISTA: z = μ + σ × ε
- La única aleatoriedad viene de ε, que es independiente de los parámetros

**¿Por qué esto funciona?**

1. **Matemáticamente equivalente:** Si ε ~ N(0,1), entonces μ + σ×ε ~ N(μ, σ²). La distribución de z es la misma.

2. **Ahora sí podemos derivar:** Como z = g(φ, x, ε) es una función determinista de φ:
   ```
   ∂z/∂μ = 1
   ∂z/∂σ = ε
   ```
   Y como μ y σ son funciones de φ (el encoder), podemos aplicar la regla de la cadena.

3. **La esperanza ahora es sobre ε:** Como p(ε) no depende de φ:
   ```
   ∇_φ E_{ε~N(0,1)}[f(g(φ, x, ε))] = E_{ε~N(0,1)}[∇_φ f(g(φ, x, ε))]
   ```
   ¡Ahora SÍ podemos meter la derivada adentro!

Como resumió el profesor:
> "Los parámetros derivables (θ) los dejo por fuera y la distribución es fija. Tengo una distribución que son los datos que muestreo y otra distribución que son los ε que muestreo, pero nunca muestreo Zs en función de los θ."

---

### 2. La fórmula del Loss de VAEs

```
log p_θ(x^(i)) ≥ L(x^(i), θ, φ) = E_z[log p_θ(x^(i) | z)] - D_KL(q_φ(z | x^(i)) || p_θ(z))
                                  \_____________________/   \__________________________/
                                   Reconstruct the Input Data       KL Divergence

θ*, φ* = arg max_{θ,φ} Σ_{i=1}^{N} L(x^(i), θ, φ)
```

**Se pide:** Explique brevemente qué función cumple cada sumando.

**Respuesta corta (para el parcial):**
> **E_z[log p_θ(x|z)] (Reconstrucción):** Mide qué tan bien el decoder reconstruye el dato original x a partir del latente z. Queremos maximizarlo para que x̂ ≈ x.
>
> **-D_KL(q_φ(z|x) || p_θ(z)) (KL Divergence):** Fuerza que la distribución del espacio latente q_φ(z|x) se parezca a una distribución conocida (típicamente N(0,1)). Esto permite generar muestreando de N(0,1).

**Explicación detallada:**

#### Primer Término: E_z[log p_θ(x|z)] - Reconstrucción

**¿Qué mide?**
Este término mide la **verosimilitud de reconstrucción**: dado un código latente z, ¿qué tan probable es que el decoder produzca el dato original x?

**En la práctica:**
- El encoder codifica x en z
- El decoder decodifica z en x̂
- Comparamos x con x̂

**Función de pérdida asociada:**
- Para imágenes continuas: MSE (Mean Squared Error)
- Para imágenes binarias: Binary Cross-Entropy

**Intuición:**
Queremos **maximizar** este término, lo que equivale a minimizar el error de reconstrucción. Si el decoder hace un buen trabajo, log p_θ(x|z) será alto (cercano a 0).

#### Segundo Término: -D_KL(q_φ(z|x) || p_θ(z)) - KL Divergence

**¿Qué mide?**
Este término mide qué tan diferente es la distribución que el encoder produce, q_φ(z|x), de una distribución "prior" que elegimos, p_θ(z) (típicamente N(0,1)).

**¿Por qué queremos esto?**
Como explicó el profesor:
> "Nosotros queremos que Z sea una Normal(0,1). Porque después vas a tirar todo lo que está atrás (el encoder), vas a agarrar el decoder y vas a hacer muestreo de acuerdo a una Normal(0,1)."

**Intuición:**
- Si no tuviéramos este término, el encoder podría producir latentes en cualquier lugar del espacio
- Al forzar q_φ(z|x) ≈ N(0,1), garantizamos que:
  1. El espacio latente está "organizado" alrededor del origen
  2. No hay "huecos" en el espacio latente
  3. Podemos generar nuevos datos simplemente muestreando de N(0,1)

**Nota:** El término tiene signo negativo porque KL ≥ 0, y queremos minimizar la diferencia (o equivalentemente, maximizar -KL).

#### Balance entre los Términos

Los dos términos tienen objetivos que pueden estar en tensión:

| Término | Objetivo | Si domina... |
|---------|----------|--------------|
| Reconstrucción | Reconstruir perfectamente | El espacio latente puede ser caótico |
| KL Divergence | Organizar el espacio latente | Las reconstrucciones pueden ser borrosas |

El entrenamiento busca un **balance**: reconstruir bien PERO manteniendo el espacio latente organizado como N(0,1).

Como resumió el profesor:
> "Forzas a que tus latentes se parezcan a algo que vos después puedes muestrear fácil."
