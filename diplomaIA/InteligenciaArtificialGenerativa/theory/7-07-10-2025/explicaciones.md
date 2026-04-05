# Explicación de Temas - Clase del 07-10-2025

## La Gran Pregunta: ¿Qué Estamos Construyendo?

Esta clase es sobre **GANs (Generative Adversarial Networks)** o **Redes Generativas Adversariales**. Es uno de los modelos más revolucionarios en inteligencia artificial generativa, propuesto en 2014 por **Ian Goodfellow** junto con un equipo que incluye a **Yoshua Bengio** y **Aaron Courville** (autores de libros y papers que ya han visto en el curso).

Como dijo el profesor:

> "Las redes generativas adversariales son un modelo que fue muy importante en su momento en 2014. Lo que viene a ser interesante de este modelo es porque logran resultados de generación que no se estaban logrando antes de entrenarlos, y además porque es una idea **creativa**."

**¿Por qué "creativa"?** Porque plantea el problema generativo como un **juego** entre dos jugadores. No es solo una arquitectura nueva, es una **manera completamente diferente de pensar** el problema de generar datos.

Esta clase cubre:
1. Repaso de ideas fundamentales (modelos paramétricos, negative log-likelihood)
2. La idea del "juego" en las GANs
3. El generador G y el discriminador D
4. La función de pérdida V(D,G)
5. El entrenamiento alternado
6. El práctico DC-GAN con convoluciones

---

## Conexión con Clases Anteriores

### ¿Qué Vimos Antes?

Antes de entrar en GANs, el profesor hizo un repaso de **dos ideas fundamentales** que ya trabajaron:

### Idea 1: Modelos Paramétricos con Distribuciones Latentes

En VAE (Variational Autoencoders) tenían:

1. Una **distribución latente Z** (generalmente una normal estándar N(0,1))
2. Una **función paramétrica f_θ(z)** que convierte Z en un dato X

```
Z ~ N(0,1)  →  [función paramétrica f_θ]  →  X (dato generado)
```

Como explicó el profesor:

> "Nosotros tenemos nuestros modelos que dependen de dos cosas: de alguna distribución latente que asumimos, y de una función paramétrica."

**Ejemplo con VAE:**

> "Con VAE nosotros teníamos un Z. Yo digo que en realidad el X que recibe mi función lo muestreo de un Z. En general es 0,1 o cero identidad dependiendo si es multivariado."

**El decoder terminaba haciendo:**

> "Nuestro decoder terminaba haciendo una función paramétrica que lo que hacía era hacer alguna función de ese Z. Muestreábamos de una normal, multiplicábamos ese Z por un mu y sigma en el caso de entrenamiento, y teníamos un modelo paramétrico que nos generaba un dato."

### Idea 2: Función de Pérdida Basada en Divergencia

Queremos minimizar la diferencia entre:
- **P_data**: La distribución de los datos reales
- **P_θ**: La distribución que genera nuestro modelo

El profesor recordó la clase de modelos autorregresivos:

> "Nosotros, de hecho, lo que queríamos era hallar el min de esto. Minimizar el θ que minimizaba esto. Y esto lo reducíamos a minimizar el negative log likelihood, que era en realidad menos la esperanza con x muestreado de acuerdo a P del logaritmo de x muestreado."

**La fórmula:**

```
min_θ E_{x~P_data}[-log P_θ(x)]
```

El profesor enfatizó:

> "Esto es dos nociones básicas de nuestra materia. Es: tenemos modelos que generan datos a partir de ruido y un modelo paramétrico, y ese modelo paramétrico lo vamos a entrenar usando alguna pérdida, probablemente la KL o similar."

---

## La Idea Central de las GANs: El Juego

### Los Dos Jugadores

Las GANs tienen **dos redes neuronales** que juegan un juego:

```
┌────────────────────────────────────────────────────────────────────┐
│                         EL JUEGO GAN                                │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   GENERADOR (G)                    DISCRIMINADOR (D)                │
│   ─────────────                    ──────────────────               │
│   • Intenta crear datos            • Intenta distinguir             │
│     falsos que parezcan              entre datos reales            │
│     reales                           y datos falsos                 │
│                                                                     │
│   • Es el "ladrón" o               • Es el "policía" o             │
│     "falsificador"                   "detective"                    │
│                                                                     │
│   • Objetivo: ENGAÑAR a D          • Objetivo: DETECTAR a G        │
│                                                                     │
│   • Parámetros: θ (theta)          • Parámetros: φ (phi)           │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

### La Analogía del Policía y el Ladrón

El profesor usó esta analogía varias veces:

> "Es como un juego de policía y ladrón, digamos. G sería el ladrón, ¿no? Y D sería el policía o el detective que tiene que identificar si lo generó el ladrón o el falsificador."

**Extendiendo la analogía:**

> "Pensalo así. Al policía cada tanto lo voy a tratar de evaluar en su capacidad de detectar ladrones. Eso implica que voy a tener que tener algún ladrón. Voy a tener que generar algún billete falso, digamos, pero no voy a estar tocando mi máquina de generación de billetes falsos. Yo voy a estar tocando al policía, voy a estar entrenando al policía."

> "Y en otros momentos yo voy a dejar al policía quieto con su entrenamiento, le voy a **frisar su cerebro** y voy a agarrar la máquina de billetes falsos y la voy a hacer generar billetes, pasarlo por el policía, ver qué me detecta el policía y tocar los tornillos de la máquina de billetes falsos. No voy a tocar al policía."

### El Objetivo Teórico

El profesor explicó:

> "Si yo logro de eso, bueno, obviamente no los puedo distinguir. Este es como el objetivo teórico de todo este modelo, lograr a través de este juego."

**En otras palabras:** Si el generador es perfecto, el discriminador no puede distinguir entre real y falso (D(x) = 0.5 para todo x). Eso significa que G aprendió a generar datos que siguen exactamente la distribución real.

---

## El Generador (G): El Falsificador

### ¿Qué Hace el Generador?

El generador G es una red neuronal con parámetros θ que:

**Entrada**: Recibe ruido aleatorio Z (generalmente Z ~ N(0,1))
**Salida**: Produce un dato X̂ = G(Z) (por ejemplo, una imagen)

```
┌────────────────────────────────────────────────────────────┐
│                    EL GENERADOR G                           │
└────────────────────────────────────────────────────────────┘

Ruido Z        Generador G          Imagen Falsa
  (ej: 100      con parámetros θ      (ej: 28×28)
  números       (pesos de red
  aleatorios)    neuronal)
     │               │                     │
     ▼               ▼                     ▼
   [0.5]                              ┌───────┐
   [0.2]          ┌─────────┐         │░░░░░░░│
   [-0.1]  ──────→│    G    │────────→│░██░░██│
   [0.8]          │  θ      │         │░██░░██│
   [...]          └─────────┘         │░░░░░░░│
                                      └───────┘
```

### G es un Modelo de Muestreo, NO de Distribución

El profesor hizo una aclaración muy importante:

> "G no recibe un X y me da una probabilidad, recibe un Z, que es ruido, y me da un elemento. Me convierte ruido aleatorio, ruido blanco en elemento de mi dataset."

**¿Qué significa esto?**

- **Modelo de distribución:** Te da P(x) para cualquier x (como los autorregresivos que te dan log P(x))
- **Modelo de muestreo:** Te permite generar datos, pero NO te da P(x) directamente

**Las GANs son modelos de muestreo:**

> "G es un modelo de muestreo porque nos permite muestrear, pero no nos da para todo x la probabilidad real."

El profesor comentó:

> "De hecho, hay muchos papers que han tratado modelos de muestreo a partir de teoría que habla de modelos de distribución. Nada, es un comentario, pero lo que digo es que G no recibe un X y me da una probabilidad."

### La Conexión con VAE

El profesor comparó con el decoder de VAE:

> "El G va a ser como el decoder. O sea, genera. Obviamente la idea es que el G va a tener que recibir algo, un latente, un Z, algo, ruido, pero esa es la única info que va a tener para generar y de ese ruido va a tener que generar algo que engañe lo mejor posible al discriminador."

---

## El Discriminador (D): El Detective

### ¿Qué Hace el Discriminador?

El discriminador D es una red neuronal con parámetros φ que:

**Entrada**: Recibe una imagen X (puede ser real o generada)
**Salida**: Produce D(X) ∈ [0, 1] que representa la probabilidad de que X sea real

```
┌────────────────────────────────────────────────────────────┐
│                  EL DISCRIMINADOR D                         │
└────────────────────────────────────────────────────────────┘

Imagen X         Discriminador D      Probabilidad
(real o falsa)   con parámetros φ     (0 a 1)
    │                  │                    │
    ▼                  ▼                    ▼
┌───────┐                                 0.95
│░██░░██│          ┌─────────┐
│░██░░██│  ───────→│    D    │───────→  "95% seguro
│░░░░░░░│          │  φ      │           que es REAL"
└───────┘          └─────────┘            (i = 1)

                       ó

┌───────┐                                 0.12
│▓▓▓░▓▓▓│          ┌─────────┐
│▓░▓▓░▓▓│  ───────→│    D    │───────→  "12% seguro
│▓▓▓▓▓▓▓│          │  φ      │           que es REAL"
└───────┘          └─────────┘            (i = 0)
                                         "Probablemente FALSA"
```

### ¿Qué Significa D(X)?

El profesor lo definió así:

> "D de i condicionado con X. Esto qué es? Un modelo que me va a generar... va a recibir datos y va a saber decirme si el dato es o no es generado."

**Valores:**
- **D(X) ≈ 1**: El discriminador cree que X es real (i = 1)
- **D(X) ≈ 0**: El discriminador cree que X es falsa (i = 0)
- **D(X) ≈ 0.5**: El discriminador no sabe (está confundido)

### El Discriminador NO Sabe de Dónde Vienen los Datos

**Importante**: El discriminador NO recibe como entrada si la imagen es real o falsa. Solo recibe la imagen.

El profesor enfatizó:

> "El discriminador va a tener que emitir un veredicto dependiendo de donde le venga el dato, pero el discriminador como modelo no tiene ese conocimiento. Va ir recibiendo de los dos lados, va a tener que aprender a clasificarlos."

Un estudiante preguntó si D recibe la información de si es real o generada:

> "No, no. Esa información no la recibe. Esa es la etiqueta. No la recibe porque... si no está haciendo trampa."

---

## El Esquema Completo del Sistema GAN

### Diagrama del Sistema

```
┌──────────────────────────────────────────────────────────────────────┐
│                         SISTEMA GAN                                   │
└──────────────────────────────────────────────────────────────────────┘

                    Ruido Z ~ P(Z)
                         │
                         ↓
                  ┌─────────────┐
                  │ Generador G │
                  │ (parámetros │
                  │     θ)      │
                  └─────────────┘
                         │
                         ↓
                    X_fake = G(Z)
                    (x con label 0)
                         │
                         │
    Datos reales         │
    X_real ~ P_data      │
    (x con label 1)      │
         │               │
         │               │
         ↓               ↓
    ┌────────────────────────────────┐
    │      Discriminador D           │
    │      (parámetros φ)            │
    └────────────────────────────────┘
                    │
                    ↓
            D(X) ∈ [0, 1]
    "Probabilidad de que X sea real"
```

### Los Dos Conjuntos de Datos

El profesor explicó cómo se estructuran los datos:

> "Yo voy a tener un conjunto de datos S1 que van a ser todos elementos de la forma x coma 1. Esta es la i, esta es la etiqueta. Van a ser muestreados de acuerdo a P_data."

> "Y voy a tener otro S2 que van a ser muestreados de acuerdo a P_theta. Y estos datos van a ser todos imputados al discriminador."

**Resumen:**
- **S1**: Datos reales (x, 1) ~ P_data
- **S2**: Datos generados (G(z), 0) ~ P_θ

---

## La Función Objetivo: V(D,G)

### La Expresión Matemática Completa

El profesor escribió en el pizarrón:

```
V(D,G) = E_{x~P_data}[log D(x)] + E_{z~P(z)}[log(1 - D(G(z)))]
```

Y luego la formulación minimax completa:

```
min_G max_D V(D,G)
```

### Desglose de Cada Parte

**Primera parte: E[log D(x)] cuando x viene de P_data**

El profesor explicó:

> "Yo quiero que si el dato es de P_data, yo quiero maximizar el logaritmo de la probabilidad."

- Si D(x) = 1 (detecta correctamente que es real): log(1) = 0 (máximo)
- Si D(x) = 0 (falla): log(0) = -∞ (mínimo)
- **Maximizar esta parte = que D diga "real" para datos reales**

**Segunda parte: E[log(1 - D(G(z)))] cuando G(z) es generado**

> "Y si el dato viene del generador, lo quiero también maximizar, pero el logaritmo de 1 menos D(x)."

- Si D(G(z)) = 0 (detecta correctamente que es falso): log(1-0) = log(1) = 0 (máximo)
- Si D(G(z)) = 1 (falla, cree que es real): log(1-1) = log(0) = -∞ (mínimo)
- **Maximizar esta parte = que D diga "falso" para datos falsos**

### El Juego MinMax

El profesor explicó:

> "Fíjate este juego de minimización de maximización. Dentro del mejor detector posible voy a querer el mejor generador posible. O sea, el generador que minimiza la detección del mejor discriminador."

**En tabla:**

| Jugador | Objetivo | Acción |
|---------|----------|--------|
| **D (Discriminador)** | Maximizar V | Ser un buen clasificador |
| **G (Generador)** | Minimizar V | Engañar al discriminador |

---

## Los Gráficos de Logaritmos

El profesor dibujó dos gráficas fundamentales para entender cómo funcionan los gradientes:

### Gráfica 1: log(D(x))

```
      │
    0 ├─────────────────────────●   ← log(1) = 0
      │                      ╱
      │                   ╱
      │                ╱
      │             ╱
      │          ╱
      │       ╱
   -∞ ├────●───────────────────────  ← log(0) = -∞
      │
      └────────────────────────────
      0                    1
                D(x)
```

**Interpretación del profesor:**
- La pendiente es **positiva** en todo el rango
- El gradiente empuja D(x) hacia **arriba** (hacia 1)
- **Para datos reales: queremos D(x) alto**

### Gráfica 2: log(1 - D(x))

```
      │
    0 ├●──────────────────────────  ← log(1-0) = 0
      │ ╲
      │   ╲
      │     ╲
      │       ╲
      │         ╲
      │           ╲
   -∞ ├──────────────────────────●  ← log(1-1) = -∞
      │
      └───────────────────────────
      0                    1
                D(x)
```

**Interpretación:**
- La pendiente es **negativa** en todo el rango
- El gradiente empuja D(x) hacia **abajo** (hacia 0)
- **Para datos falsos: queremos D(x) bajo**

### ¿Cómo Funciona el Gradiente?

El profesor explicó:

> "Lo que queremos es: si el dato es bueno, yo quiero que mi ascenso de gradiente me va a ir moviendo mis probabilidades hacia acá. Y si el dato no viene de mi distribución, mi probabilidad del discriminador debería acercarse lo más posible a cero."

> "Dependiendo de dónde venga el dato, qué es lo que va a tener que ajustar el discriminador. Si el dato es falso, si el dato es trucho, debería minimizar D para maximizar logaritmo 1 menos D. Y si el dato es real, debería maximizar D para maximizar el logaritmo de D."

---

## ¿Por Qué G Solo Se Ve Afectado Por Una Parte?

### La Observación Clave

El profesor señaló algo muy importante:

> "Cuando yo quiera minimizar G de θ, toda esta expresión no depende de θ. Cuando vos minimizás algo respecto de una variable y no tenés nada de esa variable que me afecta el término, lo pelo."

**Mirando la fórmula:**

```
V(D,G) = E_{x~P_data}[log D(x)] + E_{z~P(z)}[log(1 - D(G(z)))]
         \_____________________/   \_________________________/
               Parte 1                      Parte 2
         NO depende de θ              SÍ depende de θ
         (solo datos reales)          (aparece G)
```

### Consecuencia

**Cuando entrenamos D (max_φ V):**
- Usamos **ambas partes** de V
- D aprende con datos reales Y con datos falsos

**Cuando entrenamos G (min_θ V):**
- Solo usamos la **segunda parte** de V
- G solo se preocupa por engañar a D

El profesor lo resumió:

> "Por eso también es eso de que se entrenan cosas un poco distintas. La expresión general es la misma, pero de toda la expresión hay partes en las que el discriminador se ve afectado para las dos partes, el generador no se ve afectado para los datos reales."

---

## Entrenamiento Alternado: ¿Por Qué No Simultáneo?

### La Pregunta del Estudiante

Un estudiante preguntó si se podría entrenar las dos redes al mismo tiempo. El profesor explicó:

> "Vos en un momento vas a tener que hacer un cálculo. ¿Con qué pesos de la red haces el cálculo? Podrías como en tiempo real ir ajustando, pero es poco realista y medio complicado de estructurar ese entrenamiento. Lo más sencillo es una cantidad de ciclos uno, otra cantidad de ciclos otro, alterno."

### El Mecanismo: Congelar Parámetros

El profesor usó la analogía de "frisar" (congelar):

> "Yo voy a dejar al policía quieto con su entrenamiento, le voy a **frisar su cerebro** y voy a agarrar la máquina de billetes falsos y la voy a hacer generar billetes, pasarlo por el policía, ver qué me detecta el policía y tocar los tornillos de la máquina de billetes falsos. No voy a tocar al policía."

> "Entonces, yo voy alternadamente. O sea, uno es accesorio del otro en el aprendizaje, pero cuando entreno uno no entreno el otro."

### Diagrama del Entrenamiento Alternado

```
┌──────────────────────────────────────────────────────────────────────┐
│                    RÉGIMEN 1: ENTRENAR D                              │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│   Z ──→ G(θ) ──→ datos falsos ──→ ┐                                  │
│         ↑                          │                                  │
│      CONGELADO                     ├──→ D(φ) ──→ loss_D              │
│   (no se actualiza θ)              │     ↑                           │
│                                    │  SE ACTUALIZA φ                 │
│   datos reales ───────────────────→ ┘                                │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                    RÉGIMEN 2: ENTRENAR G                              │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│   Z ──→ G(θ) ──→ datos falsos ──→ D(φ) ──→ loss_G                   │
│         ↑                          ↑                                 │
│    SE ACTUALIZA θ              CONGELADO                             │
│                             (no se actualiza φ)                      │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

### Los Detach en PyTorch

Un estudiante mencionó los detach y el profesor confirmó:

> "Sale de ahí todo lo que son los detach."

**¿Qué es `.detach()`?**
- Es una función de PyTorch que "desconecta" un tensor del grafo computacional
- Si haces `x.detach()`, PyTorch **no calcula gradientes** para x

El profesor lo explicó de otra manera:

> "Imagínate datitos de mi distribución, los barajo. Estos datitos van a ser cero, estos datitos van a ser uno. Los barajo y los meto todo por acá y entreno este modelo, un clasificador entreno. No te importa que los verdes vinieron de algo que era paramétrico. Está **congelado** esto. Ni lo viste. Son datos y son false y entreno un clasificador."

---

## El Truco del Log: Estabilidad Numérica

### El Problema con la Formulación Original

La formulación original para entrenar G es:

```
min_θ E[log(1 - D(G(z)))]
```

**El problema:** Cuando G es malo (al principio del entrenamiento), D(G(z)) ≈ 0. Entonces:

- log(1 - 0) = log(1) = 0
- El gradiente es casi **cero** (saturado)
- G aprende **muy lento** justo cuando más necesita aprender

El profesor explicó:

> "Cuando yo me empiezo a acercar acá, empiezo a tener gradientes muy grandes o muy chicos. Tengo fenómenos que se llaman exploding gradient o vanishing gradient."

### La Solución: Cambiar la Formulación

En lugar de minimizar log(1 - D(G(z))), **maximizamos** log(D(G(z))):

```
max_θ E[log D(G(z))]
```

El profesor explicó:

> "Los muchachos del paper nos proponen en realidad es no minimizar exactamente eso, sino que lo que hacen es maximizar. Dicen, 'Che, hay una igualdad. Toda minimización es una maximización, pero con el signo opuesto.'"

> "Es muy estándar cambiar la minimización de 1 menos un logaritmo por la maximización de un logaritmo."

**¿Por qué funciona mejor?**

| D(G(z)) | log(1 - D(G(z))) | log(D(G(z))) |
|---------|------------------|--------------|
| 0.01 | log(0.99) ≈ -0.01 (gradiente pequeño) | log(0.01) ≈ -4.6 (gradiente GRANDE) |
| 0.5 | log(0.5) ≈ -0.69 | log(0.5) ≈ -0.69 |
| 0.99 | log(0.01) ≈ -4.6 | log(0.99) ≈ -0.01 |

**Cuando G es malo (D(G(z)) ≈ 0):**
- La formulación original tiene gradiente pequeño
- La formulación nueva tiene gradiente GRANDE
- **G aprende más rápido cuando más lo necesita**

---

## El Algoritmo del Paper

### El Algoritmo Paso a Paso

El profesor mostró el algoritmo del paper original:

```
┌──────────────────────────────────────────────────────────────────────┐
│              ALGORITMO DE ENTRENAMIENTO DE GANs                       │
└──────────────────────────────────────────────────────────────────────┘

Por cada training iteration:

  1. Por K veces:

     a) Muestrear m ruidos: z₁, z₂, ..., z_m ~ P(z)

     b) Muestrear m ejemplos reales: x₁, x₂, ..., x_m ~ P_data

     c) Actualizar D con gradient ascent:
        ∇_φ [1/m Σ log D(xᵢ) + 1/m Σ log(1 - D(G(zᵢ)))]

  2. Muestrear m ruidos: z₁, z₂, ..., z_m ~ P(z)

  3. Actualizar G con gradient descent:
     ∇_θ [1/m Σ log(1 - D(G(zᵢ)))]

     (O con la versión mejorada: maximizar Σ log D(G(zᵢ)))
```

### ¿Qué es K?

El profesor explicó:

> "Hay un ratio discriminador generador. No es la misma cantidad."

Un estudiante preguntó: "¿Cuál es el buen K?"

> "Depende del problema. Eso digamos no entra en el for por la época, eso sería fuera de eso."

### ¿Por Qué Se Pueden Juntar las Esperanzas?

El profesor explicó:

> "La esperanza de la suma es la suma de las esperanzas, o sea, yo puedo juntar las dos esperanzas."

> "Como son sobre distribuciones distintas, yo tengo que muestrear: el X viene de P_data y el Z viene de P(Z), y los pongo juntitos."

---

## Equilibrio de Nash y D* = 1/2

### El Discriminador Óptimo

Un estudiante preguntó sobre cuál era el "buen discriminador". El profesor explicó:

> "Un buen generador es aquel que el discriminador para tu dato no sabe de dónde viene. Es que el discriminador piense que es real."

> "Pasa que el discriminador que piensa que todo es real no sirve para nada. Es muy difícil un caso que mi discriminador sea bueno y que a su vez..."

### ¿Por Qué No Queremos D "Demasiado Bueno"?

El profesor aclaró:

> "Vos no querés un buen discriminador, en realidad vos querés un buen generador. Es un punto medio donde D no tiene idea. Cuando ve un dato tuyo no sabe qué decirte."

**El equilibrio ideal:**
- G genera datos tan buenos que D no puede distinguir
- D(x) = 0.5 para todo x (está "adivinando")
- Este es el **equilibrio de Nash**

### Un Error en el Paper

El profesor hizo una observación interesante:

> "Por las dudas quería mostrar las slides del paper. De hecho, yo esto descubrí el año pasado. Esto está mal. Porque le falta el minmax a la derecha. Esto así es la definición de V nada más. Hay una igualdad que está mal. Así que bueno, cuando quieran le arreglamos el paper."

---

## El Problema del Mode Collapse

### ¿Qué es?

El profesor explicó:

> "Estos modelos a veces presentan mode collapse. ¿Qué significa? Que si bien aprenden a generar, aprenden a generar un tipo de datos porque nada en el modelo nos incentiva a la variedad."

### Ejemplo Concreto

> "Si vos aprendes a hacer un buen uno y tu modelo aprende a hacer un muy buen uno y que tu discriminador no discrimina, ya está, ganaste. Siempre que te pase ruido te genera un buen uno."

**Escenario de mode collapse:**
```
Iteración 1: G genera basura variada
Iteración 100: G aprende a generar "1" decentes
Iteración 200: G perfecciona los "1"
Iteración 300: G SOLO genera "1" (mode collapse)
```

### ¿Por Qué Pasa?

**La función de pérdida no incentiva variedad.** Solo dice "engaña al discriminador", no dice "genera cosas variadas".

### Soluciones

El profesor mencionó:

> "Empiezan a aparecer GANs condicionales donde vos te puedes decir de qué clase querés, empiezan a aparecer soluciones sencillas que están bastante buenas para estos problemas."

---

## El Práctico: DC-GAN

### ¿Qué es DC-GAN?

El ayudante Juan explicó:

> "El nombre del práctico dice DC-GAN, que es Deep Convolutional GAN. Vamos a hacer convoluciones para implementar tanto G como D."

**DC-GAN = Deep Convolutional Generative Adversarial Network**

- **Deep**: Múltiples capas
- **Convolutional**: Usa convoluciones (especializadas para imágenes)
- **GAN**: Red generativa adversarial

### ¿Por Qué Convoluciones?

> "Dijimos que podía ser cualquier cosa que tenga parámetros y que sea derivable. Entonces, vamos a aprovechar que nosotros estamos usando imágenes y usar convoluciones."

> "Sí, podemos no usar convoluciones. Sí, perfectamente, sin ningún problema."

---

## La Arquitectura del Generador

### Convoluciones Transpuestas

Juan explicó:

> "Usa las convoluciones transpuestas, que son básicamente las convoluciones pero para el otro lado. Tenemos un kernel, algo del tamaño de la imagen, y vamos píxel por píxel expandiendo en vez de contraer. Es la operación al revés."

**Convolución normal:** Reduce tamaño (28×28 → 14×14)
**Convolución transpuesta:** Aumenta tamaño (7×7 → 14×14 → 28×28)

### Estructura del Generador

```
ENTRADA: Vector Z de tamaño [batch, latent_dim]  (ej: 100)
          ↓
      [Reshape]  → Convertir en tensor 4D
          ↓
  [ConvTranspose2d + BatchNorm + ReLU]  → Expandir
          ↓
  [ConvTranspose2d + BatchNorm + ReLU]  → Expandir más
          ↓
  [ConvTranspose2d + BatchNorm + ReLU]  → Expandir más
          ↓
  [ConvTranspose2d + Tanh]  → Última capa, genera imagen
          ↓
SALIDA: Imagen de 28×28 (Fashion-MNIST)
```

### Las Condiciones del Generador

Juan explicó:

> "Sabemos que por ejemplo qué sabemos del generador: partimos de un espacio latente. Entonces ya tenemos un par de dimensiones. ¿Cuál es el espacio latente? A definir. Pero partimos de un espacio latente."

> "¿Qué va con la salida de G? Por ejemplo, dimensión de imagen. Nosotros queremos generar imágenes. Entonces, ya tenemos una dimensión."

---

## La Arquitectura del Discriminador

### Estructura del Discriminador

```
ENTRADA: Imagen [batch, 1, 28, 28]
          ↓
  [Conv2d + LeakyReLU]  → Reducir tamaño
          ↓
  [Conv2d + BatchNorm + LeakyReLU]  → Reducir más
          ↓
  [Conv2d + BatchNorm + LeakyReLU]  → Reducir más
          ↓
  [Flatten]  → Convertir en vector
          ↓
  [Linear + Sigmoid]  → Clasificar
          ↓
SALIDA: Probabilidad [batch, 1]
```

### Las Condiciones del Discriminador

Juan explicó:

> "D, ¿qué sabemos? Recibe imagen. ¿Y qué tiene como salida? Es un discriminador que lo que hace es agarra una imagen y te dice si es real o no."

> "Nuestra salida va a pasar por una sigmoide. Nos va a dar 0 o 1. Y recibimos una imagen."

---

## Los Hiperparámetros: Learning Rates Diferentes

### El Descubrimiento

Juan mostró:

> "El discriminador estamos dando un learning rate de un orden menos. Eso es porque el discriminador termina aprendiendo más rápido. Entonces ya lo estamos penalizando para que ese learning rate sea menor."

```python
learning_rate_G = 0.0002  # Para el generador
learning_rate_D = 0.00005  # Para el discriminador (¡4 veces menor!)
```

### ¿Por Qué Son Diferentes?

> "Generalmente como que la tarea es más fácil, la del discriminador, entonces por eso termina siendo mejor más rápido."

**Tarea del discriminador (FÁCIL):**
- Recibe imagen de ruido vs imagen estructurada
- Distinguir es relativamente simple

**Tarea del generador (DIFÍCIL):**
- Debe crear estructura desde cero
- Más complejo

### El Riesgo del Desbalance

Juan advirtió:

> "Queremos que los dos vayan mejorando a la par y que no haya ninguno que se desbalance mucho. Es lo que es lo más importante, porque si hay uno va a dejar de entrenar y ya no tiene sentido el entrenamiento."

---

## La Función de Pérdida: BCE

### ¿Por Qué BCE?

Juan explicó:

> "A fin de cuentas, ¿esto a qué se reduce? A la BCE."

**Binary Cross-Entropy (BCE):**
```
BCE(y, ŷ) = -[y × log(ŷ) + (1-y) × log(1-ŷ)]
```

### El Truco del Flipeo de Labels

Juan explicó algo crucial:

> "Vamos a flipear el label. Nosotros decimos estos son datos generados, ya sabemos que son datos generados, pero para entrenar el generador estos datos generados se los quiero ajustar para que sean más parecidos a los datos reales."

**Para entrenar G:**
```python
# Generamos imágenes falsas
fake_images = G(z)

# Pero usamos label = 1 (¡como si fueran reales!)
loss_G = BCE(D(fake_images), ones)  # Target = 1
```

**¿Por qué funciona?**

> "Nuestro objetivo es que la salida del discriminador sea... el discriminador se confunde y cree que estos son reales. Entonces lo que hacemos es compararlo con 1."

> "Aunque sabemos que son truchos, el target que le pasamos es 1. Solo cuando entrenamos el generador. Cuando entrenamos el discriminador queremos discriminarlos, entonces ahí sí son ceros."

---

## Los Dos Optimizadores

### ¿Por Qué Dos?

Juan explicó:

> "Vamos a tener dos optimizadores, uno para el discriminador y otro para el generador."

```python
optimizer_G = torch.optim.Adam(G.parameters(), lr=lr_G)
optimizer_D = torch.optim.Adam(D.parameters(), lr=lr_D)
```

**Razones:**
1. Cada red tiene sus propios parámetros
2. Queremos learning rates diferentes
3. Se entrenan en momentos diferentes

---

## La Normalización: Crítica

### La Importancia

Juan enfatizó:

> "Esta transformación de normalización ayuda muchísimo a la estabilidad del entrenamiento. De hecho, hasta puede ser clave en el sentido de que si no normalizamos, muchas veces directamente no llegamos a un resultado bueno."

### ¿Qué es Normalizar?

Convertir píxeles de [0, 1] a [-1, 1]:

```python
transform = transforms.Compose([
    transforms.ToTensor(),  # Convierte a [0, 1]
    transforms.Normalize((0.5,), (0.5,))  # Convierte a [-1, 1]
])
```

### ¿Por Qué [-1, 1]?

- El generador usa **Tanh** que produce valores entre -1 y 1
- Si los datos reales están en [-1, 1], coinciden
- Sin normalización, D podría distinguir solo por el rango de valores

---

## El Concepto de "Época" en GANs

### El Problema

El profesor explicó:

> "El concepto de época se pierde un poco. El concepto de época es un número que refiere a cuántas veces visitaste todos los datos de tu entrenamiento."

> "Cada vez estoy agarrando del dataset el batch que elija y voy haciendo. Cada vez es una, y cada vez una vez la otra."

### La Solución

> "Puedes llamar la época al número de iteración, pero no tenés un mapeo exacto con el entrenamiento de una clase más estándar."

En la práctica, usamos **iteraciones** en lugar de épocas.

---

## El Problema de que No es Condicional

### La Limitación

Juan explicó:

> "Tomen en cuenta que no estamos tomando ningún tipo de condición. Seguimos en lo mismo: estamos generando imágenes del dataset. ¿Cuál generamos? No hay nada. Esa información por ahora no la tenemos."

**No puedes hacer esto:**
```python
G.generate(class_label=3)  # "Generame un 3" ← IMPOSIBLE
```

**Solo puedes hacer:**
```python
z = torch.randn(1, latent_dim)
image = G(z)  # ¿Qué saldrá? ¡Aleatorio!
```

### Soluciones Futuras

> "Empiezan a aparecer GANs condicionales donde vos te puedes decir de qué clase querés."

---

## Evaluación: ¿Cómo Saber si Funciona?

### No Hay Métricas Tradicionales

Juan explicó:

> "En cuanto a las losses generalmente no nos da mucha info, pero acá las imágenes, fuimos mirando, más o menos si parecen."

**Las losses de GANs no son interpretables directamente.**

### La Métrica Real: Tus Ojos

1. Cada N iteraciones, genera imágenes
2. Míralas
3. ¿Parecen camisetas/zapatos/etc reales?

### Señales de Problemas

Juan advirtió:

> "Van a ver que es un fenómeno que pasa que literalmente es mejor arrancar el entrenamiento de nuevo que intentar recuperarse. Una vez que llegan a ese punto de que uno se hace muy bueno, es mejor arrancar el entrenamiento de cero."

**Señales de que algo va mal:**
- Una loss va a cero y no cambia
- Las imágenes generadas no mejoran
- Mode collapse (todas las imágenes iguales)

---

## Consistencia del Muestreo

### El Consejo Crucial

Juan advirtió:

> "Lo único que sí es de lo que se muestreen en el entrenamiento, ese mismo muestreo tiene que ser el que hagan a la hora de generar. No cambien la forma de muestrear."

> "Si yo muestreo completamente random con una uniforme a la hora de entrenamiento, no me muestreen con una normal a la hora de generar."

**En código:**
```python
# Durante entrenamiento Y generación:
z = torch.randn(batch_size, latent_dim)  # Normal(0,1)

# NO cambiar después:
# z = torch.rand(batch_size, latent_dim)  # Uniforme ← ERROR
```

---

## Los Datasets

### Fashion-MNIST

- 28×28 píxeles
- Blanco y negro (1 canal)
- Prendas de ropa (camisetas, pantalones, zapatos, etc.)

### CIFAR-10 (Opcional)

Juan mencionó:

> "Hay una parte abajo que menciona otro dataset. Ese sí tiene color, son imágenes a color, así que es algo divertido como para cambiar un poco de las imágenes blanco y negro."

- 32×32 píxeles
- **Color** (3 canales RGB)
- 10 clases de objetos

**Cambio necesario:**
> "Lo único que tenemos que cumplir es que la salida del generador sea el tamaño de las imágenes y que la entrada del discriminador sea el tamaño de imagen."

---

## Resumen: El Flujo Completo

### La Arquitectura

```
Ruido Z → Generador G(θ) → Imagen falsa → Discriminador D(φ) → 0 (falso)
Imagen real ────────────────────────────→ Discriminador D(φ) → 1 (real)
```

### El Entrenamiento

**Por cada iteración:**

1. **Entrenar D (k veces):**
   - Generar m datos falsos: z ~ P(z), x_fake = G(z)
   - Tomar m datos reales: x_real ~ P_data
   - loss_D = BCE(D(x_real), 1) + BCE(D(x_fake.detach()), 0)
   - Actualizar φ

2. **Entrenar G (1 vez):**
   - Generar m datos falsos: z ~ P(z), x_fake = G(z)
   - loss_G = BCE(D(x_fake), 1)  ← Truco del flipeo
   - Actualizar θ

### La Evaluación

- Mirar las imágenes generadas
- Monitorear que las losses estén balanceadas
- Detectar mode collapse
- Si algo falla, reiniciar

---

## Código Ejemplo

```python
# Hiperparámetros
latent_dim = 100
lr_G = 0.0002
lr_D = 0.00005
batch_size = 128

# Modelos
G = Generator(latent_dim=100, output_channels=1)
D = Discriminator(input_channels=1)

# Optimizadores
optimizer_G = optim.Adam(G.parameters(), lr=lr_G)
optimizer_D = optim.Adam(D.parameters(), lr=lr_D)

# Loss
criterion = nn.BCELoss()

# Entrenamiento
for iteration in range(num_iterations):
    # --- ENTRENAR D ---
    real_images, _ = next(iter(dataloader))
    z = torch.randn(batch_size, latent_dim)
    fake_images = G(z)

    optimizer_D.zero_grad()
    loss_D_real = criterion(D(real_images), torch.ones(batch_size, 1))
    loss_D_fake = criterion(D(fake_images.detach()), torch.zeros(batch_size, 1))
    loss_D = loss_D_real + loss_D_fake
    loss_D.backward()
    optimizer_D.step()

    # --- ENTRENAR G ---
    z = torch.randn(batch_size, latent_dim)
    fake_images = G(z)

    optimizer_G.zero_grad()
    loss_G = criterion(D(fake_images), torch.ones(batch_size, 1))  # Flipeo
    loss_G.backward()
    optimizer_G.step()
```

---

## Definiciones para el Parcial

### GANs Básico

**GAN (Generative Adversarial Network):** Modelo generativo propuesto por Goodfellow (2014) que plantea el problema como un juego entre dos redes: un generador G que crea datos falsos y un discriminador D que intenta distinguir entre real y falso; entrenan alternadamente hasta que G genera datos indistinguibles de los reales.

**Generador G:** Red neuronal que recibe ruido Z ~ P(z) como entrada y genera un dato X_fake = G(z); sus parámetros θ se optimizan para engañar al discriminador; después del entrenamiento, se descarta D y solo se usa G para generar.

**Discriminador D:** Red neuronal clasificadora que recibe un dato X (real o falso) y predice D(X) ∈ [0,1] donde 1=real y 0=falso; sus parámetros φ se optimizan para distinguir correctamente; durante generación se descarta.

**P_data vs P_θ:** P_data es la distribución real de los datos (el dataset); P_θ es la distribución que genera el modelo G; el objetivo teórico es que P_θ = P_data (distribuciones idénticas).

**Modelo de Muestreo:** Las GANs son modelos de muestreo (te permiten generar datos pero no te dan P(x) directamente); a diferencia de modelos de distribución que sí te dan P(x) para cualquier x.

### La Función Objetivo

**V(D,G):** V(D,G) = E[log D(x)] + E[log(1-D(G(z)))]; función objetivo de las GANs; D quiere maximizarla (ser buen clasificador), G quiere minimizarla (engañar a D); es un juego minimax.

**MinMax:** min_G max_D V(D,G); dentro del mejor discriminador posible, buscar el mejor generador posible; no tiene solución analítica cerrada, se resuelve con entrenamiento alternado.

**Por Qué G Solo Afecta Una Parte:** La primera parte E[log D(x)] no contiene los parámetros θ de G (solo depende de datos reales y de φ); cuando minimizamos respecto a θ, esa parte es constante y se ignora.

### Entrenamiento

**Entrenamiento Alternado:** Durante el entrenamiento de D, los parámetros θ de G quedan fijos; durante el entrenamiento de G, los parámetros φ de D quedan fijos; se implementa con `.detach()` en PyTorch.

**Detach en PyTorch:** `.detach()` desconecta un tensor del grafo computacional; PyTorch no calcula gradientes para ese tensor; se usa en entrenamiento de D: `G(z).detach()` para que los gradientes no se propaguen hacia G.

**Parámetro K:** Número de veces que entrenas D antes de entrenar G una vez; k=1 es balanceado; no hay valor mágico, depende del problema.

### Estabilidad

**Truco del Log:** En lugar de minimizar log(1-D(G(z))), maximizamos log(D(G(z))); la razón es estabilidad numérica: cuando G es malo, la formulación original tiene gradientes pequeños, la nueva tiene gradientes grandes; G aprende más rápido cuando más lo necesita.

**Learning Rates Diferentes:** lr_D < lr_G (típicamente 4-10x menor); razón: discriminador aprende más rápido (tarea más fácil); previene desbalance.

**Mode Collapse:** El generador aprende a generar solo un tipo de dato; ocurre porque la pérdida no incentiva variedad; solución: reiniciar o usar GANs condicionales.

**Equilibrio de Nash:** Cuando P_G = P_data, D*(x) = 0.5 para todo x; el discriminador no puede distinguir; es el objetivo teórico del juego.

### Pérdida

**BCE para Discriminador:** loss_D = BCE(D(x_real), 1) + BCE(D(x_fake.detach()), 0); quiere que D(x_real)→1 y D(x_fake)→0.

**Truco del Flipeo:** Para entrenar G, calculamos BCE(D(G(z)), 1) donde el target es 1 (no 0); esto empuja a D(G(z)) hacia 1; como solo actualizamos θ (no φ), G aprende a engañar.

### DC-GAN

**DC-GAN (Deep Convolutional GAN):** Implementación de GAN usando convoluciones; el generador usa convoluciones transpuestas para expandir, el discriminador usa convoluciones normales para contraer.

**Convolución Transpuesta:** Operación que expande dimensiones espaciales; inversa de convolución normal; usada en el generador para convertir vector latente en imagen.

**Normalización:** Transformar píxeles de [0,1] a [-1,1]; crítica para estabilidad porque coincide con salida de Tanh en G.

### Arquitectura

**Generador:** Ruido Z → [ConvTranspose + ReLU] × N → [ConvTranspose + Tanh] → Imagen; activación final Tanh produce [-1,1].

**Discriminador:** Imagen → [Conv + LeakyReLU] × N → Flatten → Linear + Sigmoid → Probabilidad; activación final Sigmoid produce [0,1].

### Evaluación

**No Hay Test Set en GANs:** Validamos mirando las imágenes generadas; ¿parecen reales?, ¿hay variedad?; las losses no son interpretables directamente.

**Señales de Problemas:** Mode collapse (todas las imágenes iguales); loss_D→0 (D demasiado bueno); imágenes siguen siendo ruido; si pasa, reiniciar.

### Limitaciones

**No Condicional:** DC-GAN básico no permite controlar qué clase generar; G genera aleatoriamente de todas las clases; GANs condicionales sí permiten control.

**Concepto de Época:** Se pierde porque el ruido Z es infinito; usamos iteraciones en lugar de épocas.

**Consistencia de Muestreo:** La distribución de Z debe ser la misma en entrenamiento y generación; si entrenas con Normal, debes generar con Normal.

---

## Fórmulas Clave

**Función objetivo:**
```
min_G max_D V(D,G) = min_G max_D [E_{x~P_data}[log D(x)] + E_{z~P(z)}[log(1-D(G(z)))]]
```

**Para entrenar D:**
```
max_φ [E[log D(x)] + E[log(1-D(G(z)))]]
```

**Para entrenar G (versión mejorada):**
```
max_θ E[log D(G(z))]
```

**En código:**
```python
# Discriminador
loss_D = BCE(D(x_real), 1) + BCE(D(G(z).detach()), 0)

# Generador
loss_G = BCE(D(G(z)), 1)  # Flipeo: target=1
```

**Discriminador óptimo (cuando P_G = P_data):**
```
D*(x) = 0.5 para todo x
```
