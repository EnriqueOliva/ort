# Explicación de Temas - Clase del 30-09-2025: Variational Autoencoders (VAEs)

## La Gran Idea de Hoy

Esta clase introduce uno de los modelos generativos más importantes de la historia del deep learning: los **Variational Autoencoders (VAEs)**.

Como dijo el profesor:
> "El tema cuatro vamos a hablar de otro modelo también neuronal, que es muy importante para el área que son los variational auto encoders."

Esta clase es **técnicamente desafiante** porque introduce conceptos nuevos que no viste en Aprendizaje de Máquina con Matías:
1. **Variables latentes** (características ocultas que no vemos en los datos)
2. **Autoencoders** (modelos que comprimen y reconstruyen)
3. **El Reparametrization Trick** (el truco que permite entrenar VAEs)
4. **Esperanzas no diferenciables** (un problema matemático que debemos resolver)

El profesor fue muy claro sobre la dificultad:
> "Esto a mí me costó, me costó un poco hacer, o sea, hacerme la cabeza porque esto no es algo que hacemos en learning, o sea, la materia con Matías nunca estiman parámetros de distribuciones en la mitad del modelo."

---

## Conexión con Clases Anteriores: El Contexto del Curso

### Repaso Rápido: ¿Dónde Estamos?

El profesor empezó con un repaso para ubicarnos:

**Clase 2:** Regla de la suma y modelos bayesianos simples (Iris)
- Aprendimos que P(X) = Σ P(X|Z) × P(Z)
- Trabajamos con el dataset Iris (flores con 3 variedades)
- **La clave:** teníamos una variable Z (la variedad) que **conocíamos**

**Clase 3:** Modelos autorregresivos (Redes de Hinton)
- Modelo que genera píxeles uno por uno
- P(X₁, X₂, ...) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂) × ...
- **La clave:** el primer modelo generativo profundo con optimización

**Clase 6 (HOY):** Variational Autoencoders
- Modelos que aprenden **variables latentes** (características ocultas)
- No conocemos Z, pero sabemos que existe
- **La clave:** primero comprimimos, luego generamos

Como dijo el profesor:
> "Este curso va a ser una especie de zoológico de modelos generativos de donde vamos a ir viendo las ideas. ¿Por qué vamos a hacer eso? Porque todos los modelos que hay hoy en día de algún modo usan y mezclan las ideas que vamos a estar visitando en este curso."

---

## Variables Latentes: El Concepto Más Importante

### ¿Qué es una Variable Latente?

**Latente = oculto, escondido, que no podemos ver directamente**

El profesor dio el ejemplo perfecto con el dataset Iris:

#### Ejemplo 1: Las Flores Iris (CON variable latente observable)

Recuerda la clase 2. Teníamos flores con medidas:
- Largo del pétalo
- Ancho del pétalo
- Largo del sépalo
- Ancho del sépalo

**La distribución de estas medidas era rara:** si graficabas el largo del pétalo de todas las flores, no era una campana normal, eran como "tres montañitas".

¿Por qué? Porque había **3 variedades de flores** (setosa, versicolor, virginica).

El profesor explicó:
> "Nosotros sabíamos que el fenómeno estaba dado de un modo como, bueno, si Z es de la variedad, Z nos definía la distribución del largo del pétalo."

```
Z = variedad de la flor (setosa, versicolor o virginica)
↓
Largo del pétalo se distribuye como Normal(μ_z, σ_z)
```

Si la flor es **setosa**, el largo del pétalo tiene media μ₁.
Si la flor es **versicolor**, el largo del pétalo tiene media μ₂.
Si la flor es **virginica**, el largo del pétalo tiene media μ₃.

**Z es una variable latente que determina las características observables.**

**PERO:** en el Iris, Z estaba **etiquetado** en el dataset. Sabíamos la variedad de cada flor.

#### Ejemplo 2: Dígitos del MNIST (SIN variable latente observable)

Ahora imagina las imágenes de números del 0 al 9:

```
Imagen: [0.1, 0.8, 0.2, 0.9, 0.1, ...]  ← 784 píxeles
```

**Pregunta:** ¿En qué parte de esos 784 números dice "esto es un 5"?

**Respuesta:** ¡En ninguna parte!

El profesor lo explicó perfectamente:
> "Cuando el modelo entrena con un cero, no sabe que ese cero es un cero. Sí que existe. Realmente hay una información latente que nos dice eso, pero esa información no está dada. Si vos miras cada uno de los píxeles que está en la imagen, nada de eso te dice que es un cero. Nosotros como humanos tenemos la capacidad de reconocerlo, pero no hay nada en un lugarcito que diga, esto es un cero."

#### Ejemplo 3: Fotos de Gatos

El profesor dio otro ejemplo hermoso:

> "Si hicimos una foto de un gato. Nada, nada en la foto dice gato. Nosotros humanos identificamos eso y sabemos que existe algo característico a todas las fotos de los gatos, que es que, bueno, obviamente son animales que tienen ciertos ciertas genéticas que hacen que tengan cierto parecido, pero todo eso es un proceso latente que no está dado en la foto en sí, sino el proceso natural que nos que genera el animal que posteriormente fotografiamos."

**Las características "gatunidad" (orejas, bigotes, ojos, pelo) existen, pero no están escritas explícitamente en los píxeles.**

### ¿Por Qué Nos Importan las Variables Latentes?

Porque nos permiten **comprimir** la información:

```
Imagen de 784 píxeles  →  Comprimir  →  Vector de 10 números
                                        (las características esenciales)
```

Esos 10 números podrían representar:
- "¿Qué tan curvo es el trazo?"
- "¿Tiene líneas verticales u horizontales?"
- "¿Tiene círculos?"
- Etc.

**No sabemos exactamente qué representan, pero el modelo aprende a capturar lo importante.**

---

## Autoencoders: Compresión y Reconstrucción

### La Idea Básica

Un **autoencoder** es un modelo que tiene dos partes:

```
┌─────────┐         ┌────────┐         ┌─────────┐
│ ENCODER │  ────→  │   Z    │  ────→  │ DECODER │
│         │         │(latente)│         │         │
└─────────┘         └────────┘         └─────────┘
    ↓                                       ↓
  Imagen                                 Imagen
  original                            reconstruida
(784 píxeles)                         (784 píxeles)
```

El profesor lo dibujó así:
> "Un encoder decoder es un modelo que tiene acá este cuadrito que representa es el dato de entrada, los cuatro valores del Iris, los 728 píxeles de la imagen, lo que quieran... Esto es un perceptrón, por ejemplo, multicapa que cada vez se va achicando más hasta que llega a un vector de un tamaño Z y luego un decoder que va de ese tamaño al mismo espacio."

### ¿Para Qué Sirve un Autoencoder?

El profesor fue claro:
> "¿Para qué me sirve esto? Para hacer compresión. Sí, para aprender en vez de guardar datos, yo tengo una imagen, la meto con un encoder, consigo un vector y ese vector es una representación compacta de la imagen."

**Ejemplo práctico:**

```
Imagen original:      [0.1, 0.8, ..., 0.2]  (784 números)
        ↓
     Encoder
        ↓
Latente comprimido:   [2.3, -1.5, 0.8]      (solo 3 números)
        ↓
     Decoder
        ↓
Imagen reconstruida:  [0.09, 0.81, ..., 0.19] (784 números)
```

Si el modelo está bien entrenado, la imagen reconstruida se parece mucho a la original.

### La Función de Pérdida del Autoencoder Simple

Para entrenar un autoencoder básico:

```
Loss = MSE(X_original, X_reconstruida)
```

MSE = Mean Squared Error (error cuadrático medio)

El modelo aprende a minimizar la diferencia entre la imagen original y la reconstruida.

### ¿Qué Pasa en el Espacio Latente?

Si entrenamos bien el autoencoder:
- Todas las imágenes de "0" van a una región del espacio Z
- Todas las imágenes de "1" van a otra región
- Todas las imágenes de "2" van a otra región
- Etc.

**El modelo aprende a organizar conceptos similares cerca uno del otro en el espacio Z.**

---

## Variational Autoencoders (VAEs): La Diferencia Clave

### El Problema con los Autoencoders Normales

Un autoencoder normal:
```
X  →  Encoder  →  Z (un vector fijo)  →  Decoder  →  X'
```

**Problema:** Z es un vector fijo. Si quiero generar una imagen nueva, ¿qué valor de Z uso?

No puedo simplemente "inventar" un Z aleatorio porque no sé qué valores son válidos.

### La Solución: VAEs

Los VAEs dicen: **"En vez de que el encoder produzca un vector Z, que produzca los PARÁMETROS de una distribución de probabilidad"**

El profesor lo explicó así:
> "Yo voy a tener que hacer un truco. O sea, yo voy a tener que este Z no va a ser un vector de cualquier cosa. ¿Qué es lo que estimo cuando yo estimo variables aleatorias? La distribución. ¿Qué estimo de esas distribuciones? Los parámetros."

### La Arquitectura de un VAE

```
          ┌──────────┐
          │  Encoder │
          └────┬─────┘
               │
        ┌──────┴──────┐
        │             │
     ┌──▼──┐      ┌──▼──┐
     │  μ  │      │  σ  │  ← El encoder produce μ y σ
     └──┬──┘      └──┬──┘     (media y desviación estándar)
        │            │
        └──────┬─────┘
               │
          ┌────▼────┐
          │    Z    │  ← Muestreamos Z ~ Normal(μ, σ)
          └────┬────┘
               │
          ┌────▼────┐
          │ Decoder │
          └────┬────┘
               │
              X'
```

**La diferencia crucial:**
- Autoencoder normal: Encoder → Z (un vector)
- VAE: Encoder → (μ, σ) → **muestrear** Z ~ Normal(μ, σ) → Decoder

El profesor dijo:
> "Mi Z en realidad me va a dar medias y sigmas porque nosotros vamos a hacer una hipótesis que nos conviene mucho y es que Z se distribuye normal."

---

## ¿Por Qué Usamos Normales? La Justificación

### La Pregunta Natural

¿Por qué Z debe ser normal? ¿Por qué Normal(0,1)?

El profesor admitió:
> "Es medio un salto loco. Yo sé que es medio un salto loco y es como es medio un salto y todo lo que no se entienda pregúntenmelo porque sé que es difícil."

### Las Razones

**Razón 1: Empírica**
> "Empíricamente se ha observado que la distribución... las cosas... no es por un tema de cálculo numérico. Es fácil llevar a entrenar algo."

En la práctica, funciona muy bien.

**Razón 2: Matemática**

Las normales tienen propiedades muy convenientes:
- Son fáciles de muestrear (generar números aleatorios)
- Tienen fórmulas analíticas simples
- La KL divergence entre dos normales se puede calcular fácilmente

El profesor explicó:
> "La KL divergence que ya la vemos que nos compara distribuciones entre esto y una 01 es fácil de computar y tenemos buenas propiedades. Entonces, ¿por qué me voy a elegir una Laplace si yo tengo funciones que optimizan mejor?"

**Razón 3: Facilidad de Generación**

> "Muestrear de media cero varianza uno es una pelotudez perdón mi francés pero computar es muy fácil o sea le doy 10 minutos lo pueden hacer contra ChatGPT... no es difícil."

Generar números de Normal(0,1) es trivial:
```python
z = np.random.normal(0, 1, size=latent_dim)
```

---

## Normales Multivariadas: Repaso Necesario

El profesor hizo un repaso de normales multivariadas porque es fundamental para entender VAEs.

### El Problema

Si Z tiene 3 dimensiones, no tenemos solo 3 números, tenemos:
- **3 medias** (μ₁, μ₂, μ₃)
- **Una matriz de covarianza 3×3** (9 números, pero simétrica)

### ¿Qué es una Matriz de Covarianza?

El profesor explicó:

```
       ┌                    ┐
       │  σ²₁   Cov(1,2)   │
Σ  =   │                    │
       │ Cov(2,1)   σ²₂     │
       └                    ┐
```

Donde:
- **σ²₁** = varianza de Z₁ (cuánto se dispersa Z₁)
- **σ²₂** = varianza de Z₂ (cuánto se dispersa Z₂)
- **Cov(1,2)** = covarianza entre Z₁ y Z₂ (cómo varían juntas)

El profesor dijo:
> "Cada elemento en la diagonal representa la varianza de una variable individual que mide la dispersión de datos respecto a su media. Fuera de la diagonal muestran la covarianza entre dos variables distintas. Esta medida cuantifica cómo varían juntas estas dos variables."

### Interpretación Gráfica

Si tenemos dos variables aleatorias normales (X₁, X₂):

```
      X₂
       │
       │     ○○○
       │   ○○○○○○
       │  ○○○○○○○
       │   ○○○○○
       │     ○○
       └──────────── X₁
```

Si la nube de puntos es:
- **Circular** → no hay covarianza, X₁ y X₂ son independientes
- **Elipse inclinada** → hay covarianza positiva o negativa

El profesor explicó:
> "Si la elipse no tiene inclinación respecto al eje, es que hay independencia en la variabilidad... Si la elipse tiene inclinación, tiene pendiente, el eje principal de la elipse o el eje secundario tiene una inclinación, significa que hay covarianza."

Mostró ejemplos:
> "Acá tengo varios ejemplos. Por ejemplo, esta es una de media cero porque las dos están en cero, está centrada en cero y varianza uno y covarianza cero. Significa que respecto al otro no cambia. Acá lo mismo, pero esta tiene la primer variable aleatoria tiene más dispersión, que queda más ancha la nube de puntos... Y ahora cuando empezamos a tener valores en la diagonal, a medida que se acercan al uno, lo que me va marcando es la pendiente de esa elipse."

### ¿Por Qué Importa para VAEs?

Porque cuando el encoder produce μ y σ:
- **μ** es un vector (por ejemplo, de tamaño 3)
- **σ** es una matriz (3×3)

Pero en la práctica, **asumimos independencia**, entonces σ es solo un vector de varianzas (3 números).

El profesor lo mencionó al final:
> "Si las asumís independientes funciona igual. O sea, la fácil es querés una matriz de 10 por 10, querés que sea un vector, va a funcionar en las dos dimensiones."

---

## El Problema: Esperanzas No Diferenciables

### ¿Qué Quiere Decir "Diferenciable"?

**Diferenciable = poder calcular derivadas = poder hacer backpropagation = poder entrenar con descenso de gradiente**

El profesor lo planteó así:
> "Ahora, ahora llegamos a que el encoder me da un Z, pero el Z no es el vector de latente per se, sino que el Z es los parámetros de la distribución de mi vector de latente. Y esto a mí me costó, me costó un poco hacer la cabeza porque esto no es algo que hacemos en learning."

### El Contexto: Backprop Normal (con Matías)

En un modelo normal, hacemos:

```
Loss = f(X, θ)  donde θ son los parámetros

Gradiente = ∂Loss/∂θ

θ_nuevo = θ_viejo - learning_rate × Gradiente
```

El profesor dibujó esto:

> "Nosotros en mi plan cuando nosotros queremos derivar... todo lo que yo entreno sobre cualquiera de mis modelos es una red derivada de mi modelo, derivada de una función de pérdida. Cuando es porque derivo respecto a esos parámetros."

La clave es que podemos escribir:

```
∂/∂θ E[Loss] = E[∂Loss/∂θ]
```

Es decir: **"la derivada de una esperanza es igual a la esperanza de la derivada"**

El profesor lo explicó:
> "Yo tengo la derivada de la esperanza y la esperanza de la derivada. Acá dice lo mismo. Yo tengo la derivada de la esperanza y lo que lo convierto es en la esperanza de las derivadas."

Y lo mejor: podemos aproximar la esperanza con un promedio:

```
E[∂Loss/∂θ] ≈ (1/N) Σ ∂Loss_i/∂θ
```

> "Esto es la estimación por método Monte Carlo de la esperanza. Y como el gradiente es lineal, lo puedo meter para adentro."

### El Problema con VAEs

**En VAEs, la distribución de Z depende de θ:**

```
Z ~ Normal(μ_θ(X), σ_θ(X))
```

El profesor escribió:

> "Tenemos una variable aleatoria con parámetros entrenables. Esto nunca les pasó con Matías."

Ahora la esperanza es:

```
E_{Z ~ p_θ(Z)} [Loss(Z)]
```

**El problema:** cuando intentamos derivar respecto a θ, la derivada "atraviesa" el símbolo de esperanza y afecta TANTO a la función Loss COMO a la distribución p_θ(Z).

El profesor lo mostró algebraicamente:

```
∂/∂θ ∫ p_θ(z) f_θ(z) dz
```

Usando la regla del producto:

```
= ∫ [∂p_θ(z)/∂θ × f_θ(z) + p_θ(z) × ∂f_θ(z)/∂θ] dz
```

Se convierte en:

```
= ∫ ∂p_θ(z)/∂θ × f_θ(z) dz  +  ∫ p_θ(z) × ∂f_θ(z)/∂θ dz
    \_____________________/      \____________________/
         PARTE INFELIZ                 PARTE FELIZ
```

El profesor dijo:
> "El otro lado no me queda solucionable por este método Monte Carlo, no me queda una esperanza... no lo puedo estimar."

**La parte feliz:** puede aproximarse como E[∂f/∂θ]
**La parte infeliz:** NO puede aproximarse fácilmente porque incluye ∂p_θ(z)/∂θ

### El Nombre Técnico

El profesor lo llamó: **"Non-differentiable expectations"** (esperanzas no diferenciables)

---

## La Solución: El Reparametrization Trick

### La Idea Genial

**En vez de muestrear directamente de una distribución paramétrica, muestreamos de una distribución FIJA y luego aplicamos una transformación paramétrica.**

El profesor lo introdujo así:
> "¿Qué pasa si yo cambio de variable? Si yo ahora tengo una variable ε (epsilon) que se distribuye con un p de epsilon conocido, y Z ya no se distribuye con una distribución paramétrica que depende de Z. Z es una función que depende de una función paramétrica que depende de X... pero la parte aleatoria de Z no la dejo paramétrica. La parte aleatoria la meto en una distribución dada, conocida, una normal."

### La Transformación

**Antes (no funciona bien):**
```
Z ~ Normal(μ_θ, σ_θ)  ← muestreo directo, parámetros entrenables
```

**Después (con reparametrization trick):**
```
ε ~ Normal(0, 1)       ← muestreo de distribución FIJA
Z = μ_θ + σ_θ × ε      ← transformación determinística
```

El profesor lo dibujó:

```
┌─────────┐
│ Encoder │
└────┬────┘
     │
  ┌──┴──┐
  │     │
 μ_θ   σ_θ   ← salidas del encoder
  │     │
  └──┬──┘
     │
     │    ε ~ Normal(0,1)  ← muestreo FIJO
     │    │
     └────┼──→  Z = μ_θ + σ_θ × ε
          │
     ┌────▼────┐
     │ Decoder │
     └─────────┘
```

### ¿Por Qué Funciona?

**Propiedad matemática de las normales:**

Si X ~ Normal(0, 1), entonces:
```
μ + σ × X ~ Normal(μ, σ)
```

El profesor confirmó:
> "Esta es una equivalencia. O sea, yo lo que digo es hacer esto de acá, esto de acá, te da un Z que tiene esta distribución, no te cambia."

**Ejemplo numérico:**

```python
# Método 1 (directo, no funciona para backprop):
z = np.random.normal(mu, sigma)

# Método 2 (reparametrization trick):
epsilon = np.random.normal(0, 1)
z = mu + sigma * epsilon
```

**Los dos producen el mismo Z estadísticamente, pero el segundo es diferenciable respecto a μ y σ.**

### La Magia: Ahora Es Diferenciable

Con el reparametrization trick:

```
E_{ε ~ Normal(0,1)} [Loss(μ_θ + σ_θ × ε)]
```

Ahora cuando derivamos:
- La distribución de ε NO depende de θ
- Solo la función (μ_θ + σ_θ × ε) depende de θ

El profesor explicó:
> "Como la distribución no es paramétrica, me salgo de este contexto, no tengo una distribución paramétrica de Z. Z no depende de parámetros a la hora de muestrearse. No depende directamente."

Y concluyó:
> "Miren, este planteo, yo lo que estoy diciendo al final del día es mantengo la derivada, cambio la esperanza, la P no depende de Z, la P depende de epsilon... y lo que hago es Z la paso es una construcción que depende de ese epsilon, pero como Z es una construcción que depende de ese epsilon, esa esperanza ya no queda vinculada a la variable derivada."

### Ahora Podemos Hacer Monte Carlo

**Finalmente:**

```
∂/∂θ E_ε [f(μ_θ + σ_θ × ε)] = E_ε [∂f/∂θ (μ_θ + σ_θ × ε)]
```

Y aproximamos:

```
≈ (1/N) Σ ∂f/∂θ (μ_θ + σ_θ × ε_i)
```

El profesor escribió:
> "Esto sí puedo meterlo a la derivada para dentro de la derivada en θ de f de g de θ de x, epsilon de x... Obviamente yo como lo aproximo, como ya tengo esto, lo que hago es muestrear 1 sobre n la sumatoria de i=1 hasta n de la derivada en θ."

---

## La Función de Pérdida del VAE

### Las Dos Partes

Un VAE tiene una función de pérdida con **dos términos**:

```
Loss_total = Loss_reconstrucción + Loss_KL
```

El profesor lo dibujó:

```
         ┌──────────┐
         │  Encoder │
         └────┬─────┘
              │
         ┌────┴────┐
         │         │
        μ_θ       σ_θ
         │         │
         └────┬────┘
              │
    ┌─────────┼─────────┐
    │         │         │
    │     ε ~ N(0,1)    │
    │         │         │
    │   Z = μ + σ×ε     │
    │         │         │
    │    ┌────▼────┐    │
    │    │ Decoder │    │
    │    └────┬────┘    │
    │         │         │
    │        X'         │
    └─────────┴─────────┘
         │         │
         │         │
      ┌──▼──┐   ┌──▼──┐
      │ KL  │   │ MSE │
      └─────┘   └─────┘
         │         │
         └────┬────┘
              │
         Loss_total
```

El profesor explicó:
> "Vamos a tener una loss que compara esto con la normal 01 y la KL divergence que ya la vemos que nos compara distribuciones... y hay otra loss que es la de reconstrucción."

### Término 1: Loss de Reconstrucción

**Objetivo:** La imagen reconstruida debe parecerse a la original.

```
Loss_reconstrucción = MSE(X, X')
```

Donde:
- X = imagen original
- X' = imagen reconstruida por el decoder

El profesor dijo que esto lo debemos completar nosotros:
> "Tienen que pensar. Están comparando el input con el output... pueden pensar. Les tengo fe."

**Pista del profesor:** las imágenes ya NO son binarias (0 o 1), ahora son escalas de grises (0 a 255):
> "Una diferencia que no hablamos es que antes estábamos saliendo todo distribuciones Bernoulli... Acá a priori nosotros decimos que tenemos que salida X, no decimos qué. Entonces, vamos a poder generar imágenes. En este caso van a seguir siendo en blanco y negro, pero no va a ser o blanco o negro, sino que vamos a tener una escala de 0 a 255."

### Término 2: KL Divergence

**Objetivo:** Los latentes Z deben parecerse a Normal(0, 1).

**¿Qué es KL Divergence?**

KL = Kullback-Leibler divergence

Es una medida de "qué tan diferente" es una distribución de otra.

```
KL(P || Q) = ¿Qué tan diferente es P de Q?
```

Si KL = 0 → las distribuciones son idénticas
Si KL > 0 → las distribuciones son diferentes

**En nuestro caso:**

```
KL(Normal(μ_θ, σ_θ) || Normal(0, 1))
```

Queremos que esto sea pequeño → queremos que Z ~ Normal(0, 1).

### La Fórmula de KL para Normales

Cuando comparamos una Normal(μ, σ) con una Normal(0, 1), la KL divergence tiene una fórmula cerrada:

```
KL = -0.5 × Σ [1 + log(σ²) - μ² - σ²]
```

El profesor dijo:
> "Yo les puse una fórmula rara... Ahora, cuando nosotros estamos haciendo la KL con una normal 01, podemos reducir esta fórmula... básicamente es eso. Cuando hacemos la KL contra una distribución normal 01, terminamos reduciendo estas fórmulas."

**En el práctico, esta fórmula ya está dada:**
> "Me parecía un poco mucho hacerlo llenar esto, así que es esta fórmula y no mucho más."

### ¿Por Qué Necesitamos KL?

**Sin KL:**
- El encoder podría aprender μ = 1000000 y σ = 0.001
- Los latentes serían valores gigantescos muy específicos
- Después no podríamos generar nada muestreando de Normal(0, 1)

**Con KL:**
- Forzamos a que μ ≈ 0 y σ ≈ 1
- Los latentes se distribuyen como Normal(0, 1)
- Después podemos generar muestreando ε ~ Normal(0, 1) y pasándolo por el decoder

El profesor lo explicó perfectamente:
> "¿Por qué vos querés que Z se parezca a una normal 01 y no se parezca a cualquier cosa? Porque vos después vas a decir, vas a tirar todo lo que está atrás, lo vas a agarrar y vas a decir, va a ser un Z sampling... que lo vas a hacer de acuerdo a una normal... le van a pedir PyTorch random normal 01... Y cuando vos metas esto acá, si está bien entrenado tu modelo, por la salida va a ser una imagen o un dato verosímil a los datos que usaste para entrenar."

---

## El Proceso Completo: Paso a Paso

### Durante el Entrenamiento

**Paso 1:** Tomar una imagen X del dataset

**Paso 2:** Pasar por el encoder
```
μ_θ(X), σ_θ(X) = Encoder(X)
```

**Paso 3:** Muestrear epsilon
```
ε ~ Normal(0, 1)
```

**Paso 4:** Calcular Z (reparametrization trick)
```
Z = μ_θ(X) + σ_θ(X) × ε
```

**Paso 5:** Pasar Z por el decoder
```
X' = Decoder(Z)
```

**Paso 6:** Calcular las dos losses
```
Loss_reconstrucción = MSE(X, X')
Loss_KL = -0.5 × Σ [1 + log(σ²) - μ² - σ²]
Loss_total = Loss_reconstrucción + Loss_KL
```

**Paso 7:** Backpropagation
```
Actualizar θ usando ∂Loss_total/∂θ
```

### Durante la Generación (después del entrenamiento)

**Paso 1:** Muestrear de Normal(0, 1)
```
Z_nuevo ~ Normal(0, 1)
```

**Paso 2:** Pasar por el decoder
```
X_nueva = Decoder(Z_nuevo)
```

**Paso 3:** Obtenemos una imagen nueva

El profesor resumió:
> "Entonces, ¿qué hacemos con ese muestreo? Vamos a decir, bueno, ¿por qué no agarro y se lo paso al decoder? Entonces si yo estoy muestreando con la misma distribución voy a encontrar algún supuestamente valor de z que yo hubiese encodeado y llevado a eso. Entonces cuando hago el decoder, si yo lo entrené, me debería dar ese valor."

---

## El Práctico: Implementación

### El Dataset

Vamos a trabajar con **MNIST** (dígitos del 0 al 9).

**Diferencia importante:** Ya NO binarizamos las imágenes.

El profesor explicó:
> "Una diferencia, por ejemplo, que no hablamos es que nosotros siempre estábamos saliendo todo distribuciones Bernoulli... Entonces, estábamos trabajando con siempre imágenes que tenían píxeles 01. Acá a priori nosotros decimos que tenemos que salida X, no decimos qué. Entonces, no vamos a tener que tener en cuenta eso a la hora de nuestra salida. Entonces, vamos a poder generar imágenes. En este caso van a seguir siendo en blanco y negro, pero no va a ser o blanco o negro, sino que vamos a tener una escala de 0 a 255."

### Los Hiperparámetros

**latent_dim = 2** (para empezar)

El profesor aclaró:
> "La dimensión de espacio latente no tiene nada que ver con la cantidad de clases. Es esa dimensión de este vector Z que nosotros va a ser la entrada nuestro decoder y la salida nuestro encoder."

**¿Por qué empezar con 2?**

Porque con 2 dimensiones podemos **visualizar** el espacio latente en un gráfico 2D.

El profesor dijo:
> "Está seteada en dos y para una parte de más adelante está bueno que lo prueben una vez en dos y después hay unas preguntas como para pensar qué pasa si la cambiamos y les incentivo a que la cambien."

### La Arquitectura

**Encoder:**
```python
class Encoder:
    def __init__(self):
        self.fc = nn.Linear(784, 400)
        self.fc_mu = nn.Linear(400, latent_dim)
        self.fc_sigma = nn.Linear(400, latent_dim)

    def forward(self, x):
        h = relu(self.fc(x))
        mu = self.fc_mu(h)
        log_var = self.fc_sigma(h)
        return mu, log_var
```

El profesor comentó sobre la estructura:
> "Agarren, hagan un encoder que les parezca. Cómo hice yo? Acá separé después lo que sería la media de la varianza. Entonces, el encoder es como una partecita y después se separó para dar una salida de media y una salida de varianza. Si quieren usarlo bien, se los recomiendo. Si quieren agarrar decir, 'Bueno, mi salida del encoder lo separo en una parte es la media, otra parte es la varianza', no hay ningún problema."

**Reparametrization:**
```python
def reparametrize(self, mu, log_var):
    std = torch.exp(0.5 * log_var)
    eps = torch.randn_like(std)
    z = mu + std * eps
    return z
```

**Decoder:**
```python
class Decoder:
    def __init__(self):
        self.fc = nn.Linear(latent_dim, 400)
        self.fc_out = nn.Linear(400, 784)

    def forward(self, z):
        h = relu(self.fc(z))
        x_reconstructed = sigmoid(self.fc_out(h))
        return x_reconstructed
```

### La Loss

**Parte 1: KL Divergence (ya está implementada)**

```python
def kl_loss(mu, log_var):
    kl = -0.5 * torch.sum(1 + log_var - mu**2 - log_var.exp())
    return kl
```

**Parte 2: Reconstruction Loss (hay que completarla)**

El profesor dejó esto para nosotros:
> "Tienen que pensar. Están comparando el input con el output... Van a comparar un vector de x otro vector de x. ¿Qué valores puede tener acá? ¿Qué valores puede tener acá? ¿Qué estoy comparando?"

Pista: **Ya no es binario**. Las imágenes tienen valores continuos de 0 a 1.

**Sugerencia:** Usar MSE (Mean Squared Error):
```python
reconstruction_loss = F.mse_loss(x_reconstructed, x_original)
```

**Loss Total:**
```python
total_loss = reconstruction_loss + kl_loss
```

### Forward Pass Completo

```python
def forward(self, x):
    mu, log_var = self.encoder(x)
    z = self.reparametrize(mu, log_var)
    x_reconstructed = self.decoder(z)
    return x_reconstructed, mu, log_var
```

El profesor aclaró:
> "Pasamos el X, la media y la varianza. Ahora esto es lo que tienen que ver: devuelve la reconstrucción, que sería el X', la media y la varianza para después poder enchufar la loss... si no, no tenemos eso."

### Generación

Para generar nuevas imágenes:

```python
def generate(self, num_samples):
    z = torch.randn(num_samples, latent_dim)
    x_generated = self.decoder(z)
    return x_generated
```

El profesor enfatizó:
> "A la hora de generar, nada, tenemos un generar, simplemente usamos el generar... vamos a usar solamente el decoder, no vamos a usar el encoder y vamos a tener que partir desde un ruido agregado que nosotros asumimos que ajustamos a Normal 01."

### Visualización del Espacio Latente

Cuando latent_dim = 2, podemos hacer algo muy cool:

```python
z1 = np.linspace(-3, 3, 10)
z2 = np.linspace(-3, 3, 10)

for i in z1:
    for j in z2:
        z = torch.tensor([[i, j]])
        x = decoder(z)
```

Esto nos permite ver **qué imagen genera cada región del espacio Z**.

El profesor dijo sobre esto:
> "Después acá hay una función que imprime lo que sería el espacio latente más o menos, que lo que hace básicamente es explora un poquito el espacio latente e imprime las generaciones que hacen y en base a eso nos muestra qué imágenes capturó nuestro espacio latente. Es como un poco divertido verlo. Está interesante."

---

## Preguntas Frecuentes del Profesor

### 1. ¿Cuántas clases está detectando el modelo?

**Respuesta:** El modelo NO detecta clases. La dimensión latente NO es el número de clases.

El profesor fue muy claro cuando un alumno preguntó:
> **Alumno:** "Ahí donde vos le estás diciendo que hay dos clases de cosas adentro..."
> **Profesor:** "No, no, no. La dimensión de espacio latente no tiene nada que ver con la cantidad de clases."

latent_dim = 2 significa que Z es un vector de 2 números, no que hay 2 clases.

### 2. ¿Qué pasa si aumentamos latent_dim?

**Respuesta:** Más capacidad de representación, pero más parámetros para entrenar.

El profesor explicó:
> "¿Qué significa aumentar el Z? Bueno, tenemos más valores en el medio. Estamos comprimiendo. Si comprimimos algo más chico, ¿qué pasa si agrandamos esa compresión? Si yo te digo, tengo la misma dimensionalidad que esto o más, no es muy útil."

Si latent_dim = 784 (igual que la imagen), no estamos comprimiendo nada.
Si latent_dim = 2, estamos comprimiendo muchísimo (quizás demasiado).
Si latent_dim = 10, es un balance razonable.

### 3. ¿Por qué asumimos independencia en σ?

**Respuesta:** Por simplicidad. Funciona bien en la práctica.

Cuando un alumno preguntó sobre la matriz de covarianza:
> **Profesor:** "Si las asumís independientes funciona igual. O sea, la fácil es querés una matriz de 10 por 10, querés que sea un vector, va a funcionar en las dos dimensiones."

En vez de una matriz Σ de 10×10 (100 parámetros), usamos un vector σ de 10 elementos.

### 4. ¿Usamos el dataset de test?

**Respuesta:** No, pero podríamos.

El profesor dijo:
> "No usamos test. Si quieren, si quieren lo pueden ver como una extensión de nuestro dataset. Tenemos más train."

En modelos generativos, el test set a veces se agrega al train porque no estamos clasificando, solo aprendiendo la distribución.

### 5. ¿Cómo sé qué loss de reconstrucción usar?

**Respuesta:** Piensa en qué estás comparando.

El profesor dio la pista:
> "Van a comparar un vector de x otro vector de x. ¿Qué valores puede tener acá? ¿Qué valores puede tener acá? ¿Qué estoy comparando?"

Antes (con Bernoulli): usábamos Binary Cross-Entropy porque los píxeles eran 0 o 1.
Ahora (con valores continuos): MSE es más apropiado.

---

## Resumen de Conceptos Clave

### 1. Variables Latentes
**Variables ocultas que existen pero no se observan directamente en los datos.**

Ejemplo: La "gatunidad" de una foto no está en los píxeles, pero existe.

### 2. Autoencoders
**Modelos que comprimen datos a un espacio latente y luego los reconstruyen.**

```
X → Encoder → Z → Decoder → X'
```

### 3. Variational Autoencoders
**Autoencoders donde el espacio latente es una distribución probabilística.**

```
X → Encoder → (μ, σ) → Z ~ Normal(μ, σ) → Decoder → X'
```

### 4. Reparametrization Trick
**Técnica para hacer diferenciable el muestreo de distribuciones paramétricas.**

```
En vez de:  Z ~ Normal(μ_θ, σ_θ)
Hacemos:    Z = μ_θ + σ_θ × ε, donde ε ~ Normal(0, 1)
```

### 5. KL Divergence
**Medida de diferencia entre dos distribuciones.**

Usamos KL para forzar que Z ~ Normal(0, 1).

### 6. Normales Multivariadas
**Distribuciones normales con múltiples variables correlacionadas.**

Parámetros: vector de medias μ y matriz de covarianza Σ.

---

## Analogías para Entender VAEs

### Analogía 1: Recetas de Cocina

**Imagen = Plato de comida**

**Encoder = Chef que analiza el plato**
- Ve el plato terminado
- Identifica los ingredientes principales (μ)
- Identifica cuánta variación hay (σ)
- Dice: "Este plato es 70% tomate, 20% queso, 10% albahaca, con variación ±5%"

**Latente Z = La receta**
- No es el plato, es la descripción comprimida

**Decoder = Otro chef que cocina**
- Lee la receta (Z)
- Prepara un plato nuevo
- Se parece al original, pero con pequeñas diferencias

**Generación = Inventar recetas**
- Inventas una receta aleatoria (Z ~ Normal(0,1))
- El chef la cocina
- Sale un plato nuevo que se parece a los que vio durante el entrenamiento

### Analogía 2: El Juego del Teléfono Descompuesto

**Sin reparametrization trick:**
```
Persona 1 susurra → Persona 2 escucha (parámetros cambian) → mensaje cambia
                     ↑
         No puedo "practicar" mejores susurros porque
         el acto de escuchar es aleatorio y no diferenciable
```

**Con reparametrization trick:**
```
Persona 1 escribe un mensaje (μ) + nivel de ruido (σ)
→ Ruido fijo se agrega (ε)
→ Persona 2 lee mensaje con ruido (Z = μ + σ×ε)
  ↑
Ahora puedo practicar mejores mensajes porque
el ruido es independiente de mis parámetros
```

---

## Citas Memorables del Profesor

> "Esto a mí me costó, me costó un poco hacer la cabeza porque esto no es algo que hacemos en learning, o sea, la materia con Matías nunca estiman parámetros de distribuciones en la mitad del modelo."

> "Es medio un salto loco. Yo sé que es medio un salto loco y es como es medio un salto y todo lo que no se entienda pregúntenmelo porque sé que es difícil."

> "Tenemos una variable aleatoria con parámetros entrenables. Esto nunca les pasó con Matías."

> "No le digan esto a Matías, por favor. Pero hay una realidad que es que hay pequeños problemitas en estos modelos que que le dan sabor."

> "Muestrear de media cero varianza uno es una pelotudez perdón mi francés pero computar es muy fácil."

> "Es como el mismo te das cuentas. Por eso se llama reparametrization trick. Es un truco, es una manera de expresar una distribución como una operación sobre otra distribución."

> "Todos los modelos que hay hoy en día de algún modo usan y mezclan las ideas que vamos a estar visitando en este curso."

---

## Checklist de Comprensión

Antes de hacer el práctico, deberías poder responder:

- [ ] ¿Qué es una variable latente y por qué es "latente"?
- [ ] ¿Cuál es la diferencia entre un autoencoder y un VAE?
- [ ] ¿Por qué el encoder produce (μ, σ) en vez de Z directamente?
- [ ] ¿Qué es el reparametrization trick y por qué es necesario?
- [ ] ¿Para qué sirve la KL divergence en la loss?
- [ ] ¿Por qué asumimos que Z ~ Normal(0, 1)?
- [ ] ¿Cómo generas imágenes nuevas después del entrenamiento?
- [ ] ¿Qué significa que latent_dim = 2 vs latent_dim = 10?
- [ ] ¿Por qué ya no binarizamos las imágenes como en Hinton?
- [ ] ¿Cuáles son las DOS partes de la loss del VAE?

---

## Últimas Palabras

Los VAEs son uno de los modelos fundacionales del deep learning generativo. Introducen conceptos que reaparecerán en modelos futuros.

Como dijo el profesor al final:
> "A mí no me estresa. Lo voy poniendo como dos semanas como para que siga en el ritmo... Sinceramente, para acompañar el proceso de aprendizaje."

**¡Adelante con el práctico!**

---

## MAPA COMPLETO DE UNA VAE ESTÁNDAR

Este es el diagrama exhaustivo de una VAE, explicando cada componente paso a paso.

### Vista General: Los Dos Modos de Operación

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           VAE: DOS MODOS DE USO                                ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   MODO 1: ENTRENAMIENTO              MODO 2: GENERACIÓN                       ║
║   ─────────────────────              ──────────────────                       ║
║                                                                               ║
║   X_real → [ENCODER] → (μ,σ)         Z ~ N(0,1)                               ║
║                ↓                          ↓                                   ║
║         Z = μ + σ×ε                  [DECODER]                                ║
║                ↓                          ↓                                   ║
║          [DECODER]                   X_nueva                                  ║
║                ↓                                                              ║
║            X_reconstruida                                                     ║
║                ↓                                                              ║
║         LOSS = MSE + KL                                                       ║
║                                                                               ║
║   (Usa encoder + decoder)            (Solo usa decoder)                       ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

### El Flujo Completo de Entrenamiento (Paso a Paso)

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    FLUJO COMPLETO DE ENTRENAMIENTO                             ║
╚═══════════════════════════════════════════════════════════════════════════════╝

PASO 1: ENTRADA
══════════════════════════════════════════════════════════════════════════════════

         ┌─────────────────────────────────────────┐
         │              IMAGEN ORIGINAL             │
         │                   (X)                    │
         │                                         │
         │    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░        │
         │    ░░░░░░░░██████░░░░░░░░░░░░░░        │
         │    ░░░░░░██░░░░░░██░░░░░░░░░░░░        │
         │    ░░░░██░░░░░░░░░░██░░░░░░░░░░        │  Ejemplo: imagen
         │    ░░░░██░░░░░░░░░░██░░░░░░░░░░        │  de un "0"
         │    ░░░░██░░░░░░░░░░██░░░░░░░░░░        │
         │    ░░░░░░██░░░░░░██░░░░░░░░░░░░        │
         │    ░░░░░░░░██████░░░░░░░░░░░░░░        │
         │    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░        │
         │                                         │
         │    Dimensión: 28 × 28 = 784 píxeles     │
         │    Valores: 0.0 a 1.0 (escala de grises)│
         └─────────────────────────────────────────┘
                              │
                              │ Se aplana a vector
                              ▼
         ┌─────────────────────────────────────────┐
         │  X = [0.0, 0.0, 0.1, 0.9, 0.8, ..., 0.0]│
         │      ←────── 784 valores ──────→        │
         └─────────────────────────────────────────┘
                              │
                              ▼

PASO 2: ENCODER (Compresión)
══════════════════════════════════════════════════════════════════════════════════

    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                              ENCODER                                         │
    │                                                                             │
    │   ┌───────────────────────────────────────────────────────────────────┐    │
    │   │                      CAPA DE ENTRADA                               │    │
    │   │                                                                    │    │
    │   │   X (784 valores) ──→ Linear(784, 400) ──→ ReLU                   │    │
    │   │                                                                    │    │
    │   │   ┌──────────────────────────────────────────────────────────┐    │    │
    │   │   │ Operación: h = ReLU(W₁ × X + b₁)                         │    │    │
    │   │   │                                                          │    │    │
    │   │   │ • W₁: matriz de pesos de 400 × 784                      │    │    │
    │   │   │ • b₁: vector de bias de 400                             │    │    │
    │   │   │ • ReLU: max(0, valor) - elimina negativos               │    │    │
    │   │   │                                                          │    │    │
    │   │   │ Resultado: h = vector de 400 valores                    │    │    │
    │   │   └──────────────────────────────────────────────────────────┘    │    │
    │   └───────────────────────────────────────────────────────────────────┘    │
    │                                        │                                    │
    │                                        │ h (400 valores)                    │
    │                                        │                                    │
    │                           ┌────────────┴────────────┐                      │
    │                           │                         │                      │
    │                           ▼                         ▼                      │
    │   ┌────────────────────────────────┐  ┌────────────────────────────────┐   │
    │   │        RAMA DE MEDIA (μ)       │  │     RAMA DE VARIANZA (σ)       │   │
    │   │                                │  │                                │   │
    │   │  h ──→ Linear(400, latent_dim) │  │ h ──→ Linear(400, latent_dim)  │   │
    │   │                                │  │                                │   │
    │   │  ┌───────────────────────┐     │  │  ┌───────────────────────┐     │   │
    │   │  │ μ = W_μ × h + b_μ     │     │  │  │ log_var = W_σ × h + b_σ│     │   │
    │   │  │                       │     │  │  │                       │     │   │
    │   │  │ Si latent_dim = 2:    │     │  │  │ Si latent_dim = 2:    │     │   │
    │   │  │ μ = [μ₁, μ₂]         │     │  │  │ log_var = [lv₁, lv₂]  │     │   │
    │   │  │                       │     │  │  │                       │     │   │
    │   │  │ • W_μ: 2 × 400       │     │  │  │ • W_σ: 2 × 400        │     │   │
    │   │  │ • b_μ: 2             │     │  │  │ • b_σ: 2              │     │   │
    │   │  └───────────────────────┘     │  │  └───────────────────────┘     │   │
    │   │                                │  │                                │   │
    │   │  Salida: μ                     │  │  Salida: log(σ²)               │   │
    │   │  (vector de latent_dim)        │  │  (vector de latent_dim)        │   │
    │   └────────────────────────────────┘  └────────────────────────────────┘   │
    │                    │                                   │                    │
    └────────────────────│───────────────────────────────────│────────────────────┘
                         │                                   │
                         ▼                                   ▼
                  ┌──────────┐                        ┌──────────────┐
                  │  μ = [μ₁, μ₂]                    │ log_var = [lv₁, lv₂]
                  │          │                        │              │
                  │  Ejemplo:│                        │  Ejemplo:    │
                  │  [0.5, -0.3]                      │  [-0.2, 0.1] │
                  └──────────┘                        └──────────────┘
                         │                                   │
                         └─────────────┬─────────────────────┘
                                       │
                                       ▼

PASO 3: REPARAMETRIZATION TRICK (El Truco Genial)
══════════════════════════════════════════════════════════════════════════════════

    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                        REPARAMETRIZATION TRICK                               │
    │                                                                             │
    │    ¿Por qué es necesario?                                                   │
    │    ─────────────────────                                                    │
    │    Si muestreamos Z ~ N(μ,σ) directamente, NO podemos hacer backprop        │
    │    porque el muestreo es una operación aleatoria no diferenciable.          │
    │                                                                             │
    │    La solución: Separar la parte aleatoria de la parte paramétrica          │
    │                                                                             │
    │    ┌───────────────────────────────────────────────────────────────────┐   │
    │    │                                                                   │   │
    │    │     ENTRADA:  μ (del encoder)    log_var (del encoder)           │   │
    │    │                     │                      │                      │   │
    │    │                     │                      ▼                      │   │
    │    │                     │            ┌─────────────────────┐          │   │
    │    │                     │            │  σ = exp(0.5 × log_var)       │   │
    │    │                     │            │                     │          │   │
    │    │                     │            │  ¿Por qué exp(0.5×log_var)?   │   │
    │    │                     │            │  • log_var = log(σ²)          │   │
    │    │                     │            │  • 0.5 × log(σ²) = log(σ)     │   │
    │    │                     │            │  • exp(log(σ)) = σ            │   │
    │    │                     │            │                     │          │   │
    │    │                     │            │  Esto garantiza σ > 0         │   │
    │    │                     │            └─────────────────────┘          │   │
    │    │                     │                      │                      │   │
    │    │                     │                      ▼                      │   │
    │    │                     │                   σ = [σ₁, σ₂]             │   │
    │    │                     │                      │                      │   │
    │    │                     ▼                      ▼                      │   │
    │    │              ┌─────────────────────────────────────┐              │   │
    │    │              │                                     │              │   │
    │    │              │   ε ~ Normal(0, 1)  ←── RUIDO FIJO  │              │   │
    │    │              │   (vector de latent_dim)            │              │   │
    │    │              │                                     │              │   │
    │    │              │   Ejemplo: ε = [0.7, -1.2]         │              │   │
    │    │              │                                     │              │   │
    │    │              │   Este muestreo NO depende de θ     │              │   │
    │    │              │   (parámetros del modelo)           │              │   │
    │    │              │                                     │              │   │
    │    │              └─────────────────────────────────────┘              │   │
    │    │                              │                                    │   │
    │    │                              ▼                                    │   │
    │    │              ┌─────────────────────────────────────┐              │   │
    │    │              │                                     │              │   │
    │    │              │    Z = μ + σ × ε                    │              │   │
    │    │              │                                     │              │   │
    │    │              │    Ejemplo numérico:                │              │   │
    │    │              │    μ = [0.5, -0.3]                  │              │   │
    │    │              │    σ = [0.9, 1.1]                   │              │   │
    │    │              │    ε = [0.7, -1.2]                  │              │   │
    │    │              │                                     │              │   │
    │    │              │    Z₁ = 0.5 + 0.9 × 0.7 = 1.13     │              │   │
    │    │              │    Z₂ = -0.3 + 1.1 × (-1.2) = -1.62│              │   │
    │    │              │                                     │              │   │
    │    │              │    Z = [1.13, -1.62]               │              │   │
    │    │              │                                     │              │   │
    │    │              └─────────────────────────────────────┘              │   │
    │    │                              │                                    │   │
    │    │                              │ AHORA ES DIFERENCIABLE             │   │
    │    │                              │ porque ∂Z/∂μ = 1 y ∂Z/∂σ = ε       │   │
    │    │                              │                                    │   │
    │    └──────────────────────────────│────────────────────────────────────┘   │
    │                                   │                                         │
    └───────────────────────────────────│─────────────────────────────────────────┘
                                        │
                                        ▼
                                 ┌──────────────┐
                                 │ Z = [1.13, -1.62]
                                 │              │
                                 │ Vector en el │
                                 │ espacio      │
                                 │ latente      │
                                 └──────────────┘
                                        │
                                        ▼

PASO 4: DECODER (Reconstrucción)
══════════════════════════════════════════════════════════════════════════════════

    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                              DECODER                                         │
    │                                                                             │
    │   ┌───────────────────────────────────────────────────────────────────┐    │
    │   │                      CAPA DE ENTRADA                               │    │
    │   │                                                                    │    │
    │   │   Z (latent_dim valores) ──→ Linear(latent_dim, 400) ──→ ReLU     │    │
    │   │                                                                    │    │
    │   │   ┌──────────────────────────────────────────────────────────┐    │    │
    │   │   │ Operación: h' = ReLU(W₃ × Z + b₃)                        │    │    │
    │   │   │                                                          │    │    │
    │   │   │ • W₃: matriz de pesos de 400 × latent_dim               │    │    │
    │   │   │ • b₃: vector de bias de 400                             │    │    │
    │   │   │                                                          │    │    │
    │   │   │ Ejemplo: Si latent_dim = 2                               │    │    │
    │   │   │   Z = [1.13, -1.62]                                      │    │    │
    │   │   │   W₃ tiene tamaño 400 × 2                                │    │    │
    │   │   │   h' tiene tamaño 400                                    │    │    │
    │   │   └──────────────────────────────────────────────────────────┘    │    │
    │   └───────────────────────────────────────────────────────────────────┘    │
    │                                        │                                    │
    │                                        │ h' (400 valores)                   │
    │                                        ▼                                    │
    │   ┌───────────────────────────────────────────────────────────────────┐    │
    │   │                      CAPA DE SALIDA                                │    │
    │   │                                                                    │    │
    │   │   h' ──→ Linear(400, 784) ──→ Sigmoid                             │    │
    │   │                                                                    │    │
    │   │   ┌──────────────────────────────────────────────────────────┐    │    │
    │   │   │ Operación: X' = Sigmoid(W₄ × h' + b₄)                    │    │    │
    │   │   │                                                          │    │    │
    │   │   │ • W₄: matriz de pesos de 784 × 400                      │    │    │
    │   │   │ • b₄: vector de bias de 784                             │    │    │
    │   │   │ • Sigmoid: 1/(1+e^(-x)) - valores entre 0 y 1           │    │    │
    │   │   │                                                          │    │    │
    │   │   │ ¿Por qué Sigmoid al final?                               │    │    │
    │   │   │ Porque los píxeles tienen valores entre 0 y 1            │    │    │
    │   │   └──────────────────────────────────────────────────────────┘    │    │
    │   └───────────────────────────────────────────────────────────────────┘    │
    │                                        │                                    │
    └────────────────────────────────────────│────────────────────────────────────┘
                                             │
                                             ▼
                  ┌─────────────────────────────────────────┐
                  │          IMAGEN RECONSTRUIDA            │
                  │                   (X')                   │
                  │                                         │
                  │  X' = [0.02, 0.01, 0.12, 0.87, ...]     │
                  │       ←────── 784 valores ──────→       │
                  │                                         │
                  │  Se puede re-formar a 28 × 28:          │
                  │                                         │
                  │    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░        │
                  │    ░░░░░░░░██████░░░░░░░░░░░░░░        │
                  │    ░░░░░░██░░░░░░██░░░░░░░░░░░░        │
                  │    ░░░░██░░░░░░░░░░██░░░░░░░░░░        │
                  │    ░░░░██░░░░░░░░░░██░░░░░░░░░░        │
                  │    ░░░░██░░░░░░░░░░██░░░░░░░░░░        │
                  │    ░░░░░░██░░░░░░██░░░░░░░░░░░░        │
                  │    ░░░░░░░░██████░░░░░░░░░░░░░░        │
                  │    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░        │
                  │                                         │
                  │    (Debería parecerse al "0" original)  │
                  └─────────────────────────────────────────┘
                                             │
                                             ▼

PASO 5: CÁLCULO DE LA LOSS (Función de Pérdida)
══════════════════════════════════════════════════════════════════════════════════

    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                         CÁLCULO DE LA LOSS                                   │
    │                                                                             │
    │   La loss del VAE tiene DOS partes que se suman:                            │
    │                                                                             │
    │   ┌─────────────────────────────────────────────────────────────────────┐  │
    │   │                                                                     │  │
    │   │   LOSS_TOTAL = LOSS_RECONSTRUCCIÓN + LOSS_KL                       │  │
    │   │                                                                     │  │
    │   └─────────────────────────────────────────────────────────────────────┘  │
    │                                                                             │
    │   ════════════════════════════════════════════════════════════════════════ │
    │                                                                             │
    │   PARTE 1: LOSS DE RECONSTRUCCIÓN                                          │
    │   ──────────────────────────────────                                        │
    │                                                                             │
    │   ┌─────────────────────────────────────────────────────────────────────┐  │
    │   │                                                                     │  │
    │   │   Objetivo: Que X' se parezca a X                                  │  │
    │   │                                                                     │  │
    │   │   Fórmula: MSE(X, X') = (1/784) × Σ (Xᵢ - X'ᵢ)²                   │  │
    │   │                                                                     │  │
    │   │   Ejemplo:                                                          │  │
    │   │   X  = [0.0, 0.0, 0.1, 0.9, 0.8, ...]   (original)                 │  │
    │   │   X' = [0.02, 0.01, 0.12, 0.87, 0.79, ...] (reconstruida)          │  │
    │   │                                                                     │  │
    │   │   Diferencias²: (0.02)², (0.01)², (0.02)², (0.03)², (0.01)², ...   │  │
    │   │   MSE = promedio de todas las diferencias²                         │  │
    │   │                                                                     │  │
    │   │   Si X' ≈ X → MSE pequeño → modelo reconstruye bien               │  │
    │   │   Si X' ≠ X → MSE grande → modelo reconstruye mal                 │  │
    │   │                                                                     │  │
    │   └─────────────────────────────────────────────────────────────────────┘  │
    │                                                                             │
    │   ════════════════════════════════════════════════════════════════════════ │
    │                                                                             │
    │   PARTE 2: LOSS KL (Kullback-Leibler Divergence)                           │
    │   ───────────────────────────────────────────────                           │
    │                                                                             │
    │   ┌─────────────────────────────────────────────────────────────────────┐  │
    │   │                                                                     │  │
    │   │   Objetivo: Que la distribución N(μ,σ) se parezca a N(0,1)         │  │
    │   │                                                                     │  │
    │   │   ¿Por qué queremos esto?                                          │  │
    │   │   • Para poder generar después muestreando de N(0,1)               │  │
    │   │   • Si μ y σ fueran cualquier valor, no sabríamos qué muestrear    │  │
    │   │                                                                     │  │
    │   │   Fórmula: KL = -0.5 × Σ (1 + log(σ²) - μ² - σ²)                  │  │
    │   │                                                                     │  │
    │   │   En código (usando log_var = log(σ²)):                            │  │
    │   │   KL = -0.5 × Σ (1 + log_var - μ² - exp(log_var))                 │  │
    │   │                                                                     │  │
    │   │   Ejemplo:                                                          │  │
    │   │   μ = [0.5, -0.3]                                                  │  │
    │   │   log_var = [-0.2, 0.1]                                            │  │
    │   │                                                                     │  │
    │   │   Para dimensión 1:                                                │  │
    │   │   KL₁ = -0.5 × (1 + (-0.2) - (0.5)² - exp(-0.2))                  │  │
    │   │       = -0.5 × (1 - 0.2 - 0.25 - 0.82)                             │  │
    │   │       = -0.5 × (-0.27) = 0.135                                     │  │
    │   │                                                                     │  │
    │   │   Si μ ≈ 0 y σ ≈ 1 → KL pequeño (distribuciones similares)        │  │
    │   │   Si μ ≠ 0 o σ ≠ 1 → KL grande (distribuciones diferentes)        │  │
    │   │                                                                     │  │
    │   └─────────────────────────────────────────────────────────────────────┘  │
    │                                                                             │
    │   ════════════════════════════════════════════════════════════════════════ │
    │                                                                             │
    │   BALANCE ENTRE LAS DOS LOSSES:                                            │
    │                                                                             │
    │   ┌─────────────────────────────────────────────────────────────────────┐  │
    │   │                                                                     │  │
    │   │   • Solo Loss_Reconstrucción → reconstruye bien pero no genera     │  │
    │   │     (el espacio latente sería caótico)                             │  │
    │   │                                                                     │  │
    │   │   • Solo Loss_KL → espacio latente ordenado pero no reconstruye    │  │
    │   │     (todo sería ruido)                                             │  │
    │   │                                                                     │  │
    │   │   • AMBAS → reconstruye bien Y puede generar                       │  │
    │   │     (el equilibrio perfecto)                                       │  │
    │   │                                                                     │  │
    │   └─────────────────────────────────────────────────────────────────────┘  │
    │                                                                             │
    └─────────────────────────────────────────────────────────────────────────────┘
                                             │
                                             ▼

PASO 6: BACKPROPAGATION (Actualización de Pesos)
══════════════════════════════════════════════════════════════════════════════════

    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                          BACKPROPAGATION                                     │
    │                                                                             │
    │   El gradiente fluye HACIA ATRÁS a través de todo el modelo:               │
    │                                                                             │
    │   LOSS_TOTAL                                                                │
    │       │                                                                     │
    │       ▼                                                                     │
    │   ┌───────────────────────────────────────────────────────────────────┐    │
    │   │ ∂Loss/∂X' (gradiente respecto a la reconstrucción)                │    │
    │   └───────────────────────────────────────────────────────────────────┘    │
    │       │                                                                     │
    │       ▼                                                                     │
    │   ┌───────────────────────────────────────────────────────────────────┐    │
    │   │ ∂Loss/∂W₄, ∂Loss/∂b₄ (gradientes del decoder - capa salida)      │    │
    │   └───────────────────────────────────────────────────────────────────┘    │
    │       │                                                                     │
    │       ▼                                                                     │
    │   ┌───────────────────────────────────────────────────────────────────┐    │
    │   │ ∂Loss/∂W₃, ∂Loss/∂b₃ (gradientes del decoder - capa entrada)     │    │
    │   └───────────────────────────────────────────────────────────────────┘    │
    │       │                                                                     │
    │       ▼                                                                     │
    │   ┌───────────────────────────────────────────────────────────────────┐    │
    │   │ ∂Loss/∂Z (gradiente respecto al vector latente)                  │    │
    │   └───────────────────────────────────────────────────────────────────┘    │
    │       │                                                                     │
    │       │ AQUÍ ES DONDE EL REPARAMETRIZATION TRICK ES CRUCIAL             │
    │       │ Z = μ + σ × ε                                                    │
    │       │ ∂Z/∂μ = 1                                                        │
    │       │ ∂Z/∂σ = ε                                                        │
    │       │ (ε es constante, no depende de los parámetros)                  │
    │       │                                                                     │
    │       ├──────────────────────┬──────────────────────┐                      │
    │       │                      │                      │                      │
    │       ▼                      ▼                      ▼                      │
    │   ┌──────────┐          ┌──────────┐          ┌──────────────────────┐    │
    │   │∂Loss/∂μ  │          │∂Loss/∂σ  │          │∂Loss_KL/∂μ, ∂Loss_KL/∂σ│    │
    │   │(viene del│          │(viene del│          │(viene directamente   │    │
    │   │ decoder) │          │ decoder) │          │ de la Loss KL)       │    │
    │   └──────────┘          └──────────┘          └──────────────────────┘    │
    │       │                      │                      │                      │
    │       └──────────────────────┴──────────────────────┘                      │
    │                              │                                              │
    │                              ▼                                              │
    │   ┌───────────────────────────────────────────────────────────────────┐    │
    │   │ ∂Loss/∂W_μ, ∂Loss/∂b_μ, ∂Loss/∂W_σ, ∂Loss/∂b_σ                  │    │
    │   │ (gradientes de las ramas μ y σ del encoder)                      │    │
    │   └───────────────────────────────────────────────────────────────────┘    │
    │       │                                                                     │
    │       ▼                                                                     │
    │   ┌───────────────────────────────────────────────────────────────────┐    │
    │   │ ∂Loss/∂W₁, ∂Loss/∂b₁ (gradientes del encoder - capa compartida)  │    │
    │   └───────────────────────────────────────────────────────────────────┘    │
    │                                                                             │
    │   Finalmente, se actualizan TODOS los pesos:                               │
    │                                                                             │
    │   W_nuevo = W_viejo - learning_rate × ∂Loss/∂W                             │
    │                                                                             │
    └─────────────────────────────────────────────────────────────────────────────┘
```

---

### El Flujo de Generación (Después del Entrenamiento)

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                      FLUJO DE GENERACIÓN (POST-ENTRENAMIENTO)                  ║
╚═══════════════════════════════════════════════════════════════════════════════╝

   ┌─────────────────────────────────────────────────────────────────────────────┐
   │                                                                             │
   │   NOTA IMPORTANTE: Durante la generación, NO usamos el encoder.            │
   │   El encoder solo se usa durante el entrenamiento.                         │
   │                                                                             │
   └─────────────────────────────────────────────────────────────────────────────┘

PASO 1: MUESTREAR DEL ESPACIO LATENTE
══════════════════════════════════════════════════════════════════════════════════

         ┌─────────────────────────────────────────┐
         │                                         │
         │        Z ~ Normal(0, 1)                 │
         │                                         │
         │    Muestreamos directamente de la       │
         │    distribución normal estándar         │
         │                                         │
         │    Ejemplo:                             │
         │    Z = torch.randn(1, latent_dim)       │
         │    Z = [0.8, -0.5]                     │
         │                                         │
         │    ¿Por qué N(0,1)?                     │
         │    Porque entrenamos con Loss_KL        │
         │    para que el espacio latente          │
         │    se parezca a N(0,1)                  │
         │                                         │
         └─────────────────────────────────────────┘
                              │
                              ▼

PASO 2: PASAR POR EL DECODER (ya entrenado)
══════════════════════════════════════════════════════════════════════════════════

         ┌─────────────────────────────────────────┐
         │            DECODER (congelado)          │
         │                                         │
         │   Z = [0.8, -0.5]                       │
         │          │                              │
         │          ▼                              │
         │   Linear(2, 400) + ReLU                 │
         │          │                              │
         │          ▼                              │
         │   Linear(400, 784) + Sigmoid            │
         │          │                              │
         │          ▼                              │
         │   X_generada = [0.01, 0.02, ...]       │
         │   (784 valores entre 0 y 1)             │
         │                                         │
         └─────────────────────────────────────────┘
                              │
                              ▼

PASO 3: OBTENER IMAGEN NUEVA
══════════════════════════════════════════════════════════════════════════════════

         ┌─────────────────────────────────────────┐
         │           IMAGEN GENERADA               │
         │                                         │
         │    Reformar vector de 784 a 28×28:      │
         │                                         │
         │    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░        │
         │    ░░░░░░░░░░░░██░░░░░░░░░░░░░░        │
         │    ░░░░░░░░░░░███░░░░░░░░░░░░░░        │
         │    ░░░░░░░░░░████░░░░░░░░░░░░░░        │
         │    ░░░░░░░░░██░██░░░░░░░░░░░░░░        │
         │    ░░░░░░░░░░░░██░░░░░░░░░░░░░░        │
         │    ░░░░░░░░░░░░██░░░░░░░░░░░░░░        │
         │    ░░░░░░░░░░██████░░░░░░░░░░░░        │
         │    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░        │
         │                                         │
         │    ¡Una imagen NUEVA que nunca          │
         │    existió en el dataset!               │
         │                                         │
         └─────────────────────────────────────────┘
```

---

### Diagrama Completo: Todo en Una Imagen

```
╔═══════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                       ║
║                            VAE COMPLETO - VISTA UNIFICADA                             ║
║                                                                                       ║
╠═══════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                       ║
║                                      ENCODER                                          ║
║   ┌───────────────────────────────────────────────────────────────────────────────┐  ║
║   │                                                                               │  ║
║   │   X (784)                                                                     │  ║
║   │     │                                                                         │  ║
║   │     ▼                                                                         │  ║
║   │   ┌─────────────────┐                                                         │  ║
║   │   │ Linear(784,400) │                                                         │  ║
║   │   │    + ReLU       │                                                         │  ║
║   │   └────────┬────────┘                                                         │  ║
║   │            │                                                                  │  ║
║   │            │ h (400)                                                          │  ║
║   │            │                                                                  │  ║
║   │     ┌──────┴──────┐                                                           │  ║
║   │     │             │                                                           │  ║
║   │     ▼             ▼                                                           │  ║
║   │   ┌─────────┐   ┌─────────┐                                                   │  ║
║   │   │Linear   │   │Linear   │                                                   │  ║
║   │   │(400,2)  │   │(400,2)  │                                                   │  ║
║   │   └────┬────┘   └────┬────┘                                                   │  ║
║   │        │             │                                                        │  ║
║   │        ▼             ▼                                                        │  ║
║   │       μ (2)      log_var (2)                                                  │  ║
║   │                                                                               │  ║
║   └───────────────────────────────────────────────────────────────────────────────┘  ║
║                        │             │                                               ║
║                        │             │                                               ║
║   ┌────────────────────┼─────────────┼────────────────────────────────────────────┐  ║
║   │                    │             │                    REPARAMETRIZATION TRICK │  ║
║   │                    │             ▼                                            │  ║
║   │                    │      σ = exp(0.5 × log_var)                              │  ║
║   │                    │             │                                            │  ║
║   │                    │             │                                            │  ║
║   │                    ▼             ▼                                            │  ║
║   │                    μ      +      σ      ×      ε ~ N(0,1)                     │  ║
║   │                    └──────┬──────┘             │                              │  ║
║   │                           │                    │                              │  ║
║   │                           │←───────────────────┘                              │  ║
║   │                           │                                                   │  ║
║   │                           ▼                                                   │  ║
║   │                    Z = μ + σ × ε                                              │  ║
║   │                        (2)                                                    │  ║
║   └───────────────────────────────────────────────────────────────────────────────┘  ║
║                               │                                                      ║
║                               │                                                      ║
║                               ▼                                                      ║
║                                      DECODER                                         ║
║   ┌───────────────────────────────────────────────────────────────────────────────┐  ║
║   │                                                                               │  ║
║   │                          Z (2)                                                │  ║
║   │                            │                                                  │  ║
║   │                            ▼                                                  │  ║
║   │                    ┌─────────────────┐                                        │  ║
║   │                    │ Linear(2, 400)  │                                        │  ║
║   │                    │    + ReLU       │                                        │  ║
║   │                    └────────┬────────┘                                        │  ║
║   │                             │                                                 │  ║
║   │                             │ h' (400)                                        │  ║
║   │                             │                                                 │  ║
║   │                             ▼                                                 │  ║
║   │                    ┌─────────────────┐                                        │  ║
║   │                    │ Linear(400,784) │                                        │  ║
║   │                    │   + Sigmoid     │                                        │  ║
║   │                    └────────┬────────┘                                        │  ║
║   │                             │                                                 │  ║
║   │                             ▼                                                 │  ║
║   │                          X' (784)                                             │  ║
║   │                    (imagen reconstruida)                                      │  ║
║   │                                                                               │  ║
║   └───────────────────────────────────────────────────────────────────────────────┘  ║
║                               │                                                      ║
║                               │                                                      ║
║                               ▼                                                      ║
║                                       LOSS                                           ║
║   ┌───────────────────────────────────────────────────────────────────────────────┐  ║
║   │                                                                               │  ║
║   │     ┌─────────────────────────────┐   ┌─────────────────────────────┐        │  ║
║   │     │                             │   │                             │        │  ║
║   │     │    LOSS RECONSTRUCCIÓN      │   │         LOSS KL             │        │  ║
║   │     │                             │   │                             │        │  ║
║   │     │    MSE(X, X')               │   │   -0.5 × Σ(1 + log_var     │        │  ║
║   │     │                             │   │         - μ² - exp(log_var))│        │  ║
║   │     │    Compara original vs      │   │                             │        │  ║
║   │     │    reconstruida             │   │   Fuerza N(μ,σ) ≈ N(0,1)   │        │  ║
║   │     │                             │   │                             │        │  ║
║   │     └──────────────┬──────────────┘   └──────────────┬──────────────┘        │  ║
║   │                    │                                 │                        │  ║
║   │                    └────────────────┬────────────────┘                        │  ║
║   │                                     │                                         │  ║
║   │                                     ▼                                         │  ║
║   │                              LOSS_TOTAL                                       │  ║
║   │                                     │                                         │  ║
║   │                                     ▼                                         │  ║
║   │                              BACKPROPAGATION                                  │  ║
║   │                                     │                                         │  ║
║   │                                     ▼                                         │  ║
║   │                           Actualizar W, b                                     │  ║
║   │                                                                               │  ║
║   └───────────────────────────────────────────────────────────────────────────────┘  ║
║                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
```

---

---

### ¿Por Qué Muestrear de N(0,1) Genera Imágenes Coherentes? (No es "ruido")

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   PREGUNTA CLAVE: Si muestreo "ruido" N(0,1), ¿cómo sale una imagen real?    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

La confusión viene de pensar que N(0,1) es "ruido sin sentido".
¡NO LO ES! Es un ESPACIO ORGANIZADO que el modelo aprendió.

══════════════════════════════════════════════════════════════════════════════════
DURANTE EL ENTRENAMIENTO: El modelo ORGANIZA el espacio latente
══════════════════════════════════════════════════════════════════════════════════

   La Loss KL hace algo crucial:

   KL(N(μ,σ) || N(0,1)) → Fuerza a que μ ≈ 0 y σ ≈ 1

   Esto significa que TODAS las imágenes del dataset se mapean a regiones
   CERCANAS a N(0,1):

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                     ESPACIO LATENTE (2D para visualizar)                │
   │                                                                         │
   │                              ↑ Z₂                                       │
   │                              │                                          │
   │                         ○○○○○│○○○○○                                     │
   │                       ○○ 1's │  7's○○                                   │
   │                      ○○      │       ○○                                 │
   │                     ○  4's   │   9's   ○                                │
   │               ──────○────────┼──────────○──────→ Z₁                     │
   │                     ○  2's   │   6's   ○                                │
   │                      ○○      │       ○○                                 │
   │                       ○○ 3's │  5's○○                                   │
   │                         ○○○○○│○○○○○                                     │
   │                              │                                          │
   │                                                                         │
   │   El círculo grande ≈ donde está el 95% de N(0,1)                      │
   │   Cada región corresponde a un tipo de dígito                          │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘

   El encoder aprendió a mapear:
   • Imágenes de "1" → región superior izquierda del espacio
   • Imágenes de "7" → región superior derecha
   • Imágenes de "3" → región inferior izquierda
   • etc.

   Y TODO esto está contenido aproximadamente en N(0,1) gracias a la Loss KL.

══════════════════════════════════════════════════════════════════════════════════
DURANTE LA GENERACIÓN: Muestreamos de ese espacio ORGANIZADO
══════════════════════════════════════════════════════════════════════════════════

   Cuando hacemos Z ~ N(0,1), NO estamos generando "ruido":

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   Z = [0.8, -0.5]  ← Este punto NO es "ruido aleatorio"                │
   │                                                                         │
   │   Es un PUNTO ESPECÍFICO en el espacio latente que corresponde         │
   │   a alguna combinación de características aprendidas.                  │
   │                                                                         │
   │   El decoder aprendió:                                                  │
   │   • Si Z está en la región de los "1" → genera algo parecido a un 1   │
   │   • Si Z está en la región de los "7" → genera algo parecido a un 7   │
   │   • Si Z está ENTRE regiones → genera algo intermedio (interpolación) │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════════════════
ANALOGÍA: El Espacio Latente es como un MAPA
══════════════════════════════════════════════════════════════════════════════════

   Imagina que el espacio latente es un mapa de una ciudad:

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   ENTRENAMIENTO = El modelo DIBUJA el mapa                             │
   │   ─────────────────────────────────────────                             │
   │                                                                         │
   │   • Ve muchas fotos de casas → las pone en el barrio residencial       │
   │   • Ve muchas fotos de tiendas → las pone en el centro comercial       │
   │   • Ve muchas fotos de parques → las pone en la zona verde             │
   │                                                                         │
   │   La Loss KL dice: "el mapa debe caber en un cuadrado de 1x1"          │
   │   (para que después sepamos dónde buscar)                              │
   │                                                                         │
   │   ─────────────────────────────────────────────────────────────────────│
   │                                                                         │
   │   GENERACIÓN = Elegimos un punto del mapa y vemos qué hay ahí          │
   │   ────────────────────────────────────────────────────────────          │
   │                                                                         │
   │   • Si elijo un punto en el barrio residencial → sale una casa         │
   │   • Si elijo un punto en el centro comercial → sale una tienda         │
   │   • Si elijo un punto entre ambos → sale algo intermedio               │
   │                                                                         │
   │   Muestrear de N(0,1) = elegir puntos aleatorios dentro del mapa       │
   │   (NO es elegir puntos aleatorios del universo entero)                 │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════════════════
¿QUÉ PASA SI MUESTREO MUY LEJOS DE N(0,1)?
══════════════════════════════════════════════════════════════════════════════════

   Si muestreas Z = [10, 10] (muy lejos del centro):

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   El decoder NUNCA VIO puntos tan lejanos durante el entrenamiento     │
   │   (porque la Loss KL forzó a que todo esté cerca de N(0,1))            │
   │                                                                         │
   │   Resultado: La imagen generada será BASURA o artefactos extraños      │
   │                                                                         │
   │   Por eso muestreamos de N(0,1): para quedarnos en la región           │
   │   donde el decoder fue entrenado y sabe qué hacer.                     │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════════════════
RESUMEN: El "ruido" N(0,1) NO es ruido
══════════════════════════════════════════════════════════════════════════════════

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   N(0,1) durante ENTRENAMIENTO (reparametrization trick):              │
   │   ε ~ N(0,1) → Sí es ruido, pero se TRANSFORMA con μ y σ               │
   │   Z = μ + σ × ε → Z tiene información de la imagen                     │
   │                                                                         │
   │   ─────────────────────────────────────────────────────────────────────│
   │                                                                         │
   │   N(0,1) durante GENERACIÓN:                                           │
   │   Z ~ N(0,1) → NO es ruido, es un punto en el espacio organizado       │
   │   El decoder sabe interpretar ese punto porque fue entrenado así       │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘
```

---

### ¿Qué Redes Se Usan en una VAE? (MLP, CNN, RNN...)

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   VAE ES UN FRAMEWORK, NO UNA ARQUITECTURA ESPECÍFICA                        ║
║                                                                               ║
║   El encoder y decoder pueden ser CUALQUIER tipo de red neuronal.            ║
║   Lo único que importa es:                                                   ║
║   • Encoder: entrada X → salida (μ, σ)                                       ║
║   • Decoder: entrada Z → salida X'                                           ║
║   • Usar el reparametrization trick en el medio                              ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

══════════════════════════════════════════════════════════════════════════════════
OPCIÓN 1: MLP (Multilayer Perceptron) - Lo que vimos en clase
══════════════════════════════════════════════════════════════════════════════════

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   ENCODER (MLP):                                                        │
   │   ──────────────                                                        │
   │                                                                         │
   │   X (784) ──→ Linear(784,400) ──→ ReLU ──→ Linear(400,2) ──→ μ         │
   │                                       └──→ Linear(400,2) ──→ σ         │
   │                                                                         │
   │   DECODER (MLP):                                                        │
   │   ──────────────                                                        │
   │                                                                         │
   │   Z (2) ──→ Linear(2,400) ──→ ReLU ──→ Linear(400,784) ──→ Sigmoid ──→ X'
   │                                                                         │
   │   ─────────────────────────────────────────────────────────────────────│
   │                                                                         │
   │   VENTAJAS:                                                             │
   │   ✓ Simple de implementar                                               │
   │   ✓ Rápido de entrenar                                                  │
   │   ✓ Bueno para datos pequeños (MNIST 28×28)                            │
   │                                                                         │
   │   DESVENTAJAS:                                                          │
   │   ✗ No captura estructura espacial (trata cada píxel independiente)    │
   │   ✗ Muchos parámetros para imágenes grandes                            │
   │   ✗ Imágenes generadas tienden a ser borrosas                          │
   │                                                                         │
   │   CUÁNDO USARLO:                                                        │
   │   • Imágenes pequeñas (MNIST, Fashion-MNIST)                           │
   │   • Datos tabulares (no imágenes)                                      │
   │   • Cuando quieres simplicidad                                         │
   │   • EN ESTE CURSO (es lo que se pide en el práctico)                   │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════════════════
OPCIÓN 2: CNN (Convolutional Neural Network) - Para imágenes reales
══════════════════════════════════════════════════════════════════════════════════

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   ENCODER (CNN):                                                        │
   │   ──────────────                                                        │
   │                                                                         │
   │   X (1,28,28)                                                           │
   │       │                                                                 │
   │       ▼                                                                 │
   │   Conv2d(1,32,3) + ReLU + MaxPool    →  (32,14,14)                     │
   │       │                                                                 │
   │       ▼                                                                 │
   │   Conv2d(32,64,3) + ReLU + MaxPool   →  (64,7,7)                       │
   │       │                                                                 │
   │       ▼                                                                 │
   │   Flatten                             →  (3136)                         │
   │       │                                                                 │
   │       ▼                                                                 │
   │   Linear(3136,256) + ReLU            →  (256)                          │
   │       │                                                                 │
   │       ├──→ Linear(256,latent_dim)    →  μ                              │
   │       └──→ Linear(256,latent_dim)    →  σ                              │
   │                                                                         │
   │   ─────────────────────────────────────────────────────────────────────│
   │                                                                         │
   │   DECODER (CNN transpuesta):                                            │
   │   ──────────────────────────                                            │
   │                                                                         │
   │   Z (latent_dim)                                                        │
   │       │                                                                 │
   │       ▼                                                                 │
   │   Linear(latent_dim,256) + ReLU      →  (256)                          │
   │       │                                                                 │
   │       ▼                                                                 │
   │   Linear(256,3136) + ReLU            →  (3136)                         │
   │       │                                                                 │
   │       ▼                                                                 │
   │   Reshape                             →  (64,7,7)                       │
   │       │                                                                 │
   │       ▼                                                                 │
   │   ConvTranspose2d(64,32,3) + ReLU    →  (32,14,14)                     │
   │       │                                                                 │
   │       ▼                                                                 │
   │   ConvTranspose2d(32,1,3) + Sigmoid  →  (1,28,28)                      │
   │       │                                                                 │
   │       ▼                                                                 │
   │   X' (imagen reconstruida)                                              │
   │                                                                         │
   │   ─────────────────────────────────────────────────────────────────────│
   │                                                                         │
   │   VENTAJAS:                                                             │
   │   ✓ Captura estructura espacial (bordes, texturas, formas)             │
   │   ✓ Menos parámetros que MLP para imágenes grandes                     │
   │   ✓ Imágenes generadas más nítidas                                     │
   │   ✓ Funciona con imágenes de cualquier tamaño                          │
   │                                                                         │
   │   DESVENTAJAS:                                                          │
   │   ✗ Más complejo de implementar                                        │
   │   ✗ Hay que calcular bien las dimensiones en cada capa                 │
   │   ✗ Más lento de entrenar                                              │
   │                                                                         │
   │   CUÁNDO USARLO:                                                        │
   │   • Imágenes grandes (CelebA, CIFAR-10, ImageNet)                      │
   │   • Cuando necesitas calidad en las imágenes generadas                 │
   │   • En producción / investigación seria                                │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘

   ¿Qué es ConvTranspose2d?
   ────────────────────────

   Es la operación "inversa" de Conv2d:
   • Conv2d: imagen grande → imagen pequeña (reduce dimensiones)
   • ConvTranspose2d: imagen pequeña → imagen grande (aumenta dimensiones)

   También se llama "deconvolución" o "convolución transpuesta".

══════════════════════════════════════════════════════════════════════════════════
OPCIÓN 3: RNN/LSTM/Transformer - Para secuencias
══════════════════════════════════════════════════════════════════════════════════

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   PARA DATOS SECUENCIALES:                                              │
   │   • Texto (oraciones, documentos)                                       │
   │   • Audio (música, voz)                                                 │
   │   • Series temporales                                                   │
   │                                                                         │
   │   ENCODER (LSTM):                                                       │
   │   ────────────────                                                      │
   │                                                                         │
   │   Secuencia X = [x₁, x₂, x₃, ..., xₜ]                                  │
   │       │                                                                 │
   │       ▼                                                                 │
   │   Embedding (si es texto)                                               │
   │       │                                                                 │
   │       ▼                                                                 │
   │   LSTM(input_size, hidden_size)                                         │
   │       │                                                                 │
   │       ▼                                                                 │
   │   Último hidden state h_T                                               │
   │       │                                                                 │
   │       ├──→ Linear(hidden_size, latent_dim) → μ                         │
   │       └──→ Linear(hidden_size, latent_dim) → σ                         │
   │                                                                         │
   │   ─────────────────────────────────────────────────────────────────────│
   │                                                                         │
   │   DECODER (LSTM):                                                       │
   │   ────────────────                                                      │
   │                                                                         │
   │   Z (latent_dim)                                                        │
   │       │                                                                 │
   │       ▼                                                                 │
   │   Linear(latent_dim, hidden_size) → h₀ (hidden inicial)                │
   │       │                                                                 │
   │       ▼                                                                 │
   │   LSTM genera secuencia token por token                                 │
   │       │                                                                 │
   │       ▼                                                                 │
   │   X' = [x'₁, x'₂, x'₃, ..., x'ₜ]                                       │
   │                                                                         │
   │   ─────────────────────────────────────────────────────────────────────│
   │                                                                         │
   │   NOTA: Para texto moderno se usan Transformers en vez de LSTM         │
   │   (como en VAE para texto o GPT)                                       │
   │                                                                         │
   │   CUÁNDO USARLO:                                                        │
   │   • Generación de texto                                                 │
   │   • Generación de música                                                │
   │   • Cualquier dato secuencial                                          │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════════════════
COMPARACIÓN: ¿Qué red usar según el problema?
══════════════════════════════════════════════════════════════════════════════════

   ┌──────────────────┬─────────────────┬─────────────────────────────────────┐
   │ Tipo de dato     │ Red recomendada │ Ejemplo                             │
   ├──────────────────┼─────────────────┼─────────────────────────────────────┤
   │ Imágenes         │ MLP             │ MNIST (28×28) - simple             │
   │ pequeñas         │                 │                                     │
   ├──────────────────┼─────────────────┼─────────────────────────────────────┤
   │ Imágenes         │ CNN             │ CelebA (64×64), CIFAR (32×32)      │
   │ medianas/grandes │                 │ Fotos reales                        │
   ├──────────────────┼─────────────────┼─────────────────────────────────────┤
   │ Texto            │ RNN/LSTM o      │ Generación de oraciones,           │
   │                  │ Transformer     │ autocompletado                      │
   ├──────────────────┼─────────────────┼─────────────────────────────────────┤
   │ Audio            │ CNN 1D o        │ Generación de música,              │
   │                  │ WaveNet         │ síntesis de voz                     │
   ├──────────────────┼─────────────────┼─────────────────────────────────────┤
   │ Datos tabulares  │ MLP             │ Datos médicos, financieros         │
   │                  │                 │                                     │
   └──────────────────┴─────────────────┴─────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════════════════
EN ESTE CURSO: Usamos MLP
══════════════════════════════════════════════════════════════════════════════════

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   En el práctico de VAE usamos MLP porque:                             │
   │                                                                         │
   │   1. MNIST es pequeño (28×28 = 784 píxeles)                            │
   │   2. Es más simple de entender e implementar                           │
   │   3. El foco está en entender el CONCEPTO de VAE, no la arquitectura   │
   │   4. MLP es suficiente para ver resultados decentes                    │
   │                                                                         │
   │   En la vida real / investigación:                                     │
   │   → Para imágenes usarías CNN                                          │
   │   → Para texto usarías Transformers                                    │
   │   → Pero el concepto de VAE (encoder→μ,σ→reparam→decoder) es el mismo │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════════════════
DIAGRAMA: VAE es un "envoltorio" que puede contener cualquier red
══════════════════════════════════════════════════════════════════════════════════

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │                        VAE (FRAMEWORK GENERAL)                          │
   │                                                                         │
   │   ┌─────────────────────────────────────────────────────────────────┐  │
   │   │                         ENCODER                                  │  │
   │   │   ┌───────────────────────────────────────────────────────────┐ │  │
   │   │   │                                                           │ │  │
   │   │   │   Puede ser:  • MLP (capas Linear)                       │ │  │
   │   │   │               • CNN (capas Conv2d)                        │ │  │
   │   │   │               • RNN/LSTM (capas recurrentes)              │ │  │
   │   │   │               • Transformer (self-attention)              │ │  │
   │   │   │               • Cualquier combinación                     │ │  │
   │   │   │                                                           │ │  │
   │   │   └───────────────────────────────────────────────────────────┘ │  │
   │   │                              │                                   │  │
   │   │                              ▼                                   │  │
   │   │                           (μ, σ)                                 │  │
   │   └─────────────────────────────────────────────────────────────────┘  │
   │                                  │                                      │
   │                                  ▼                                      │
   │   ┌─────────────────────────────────────────────────────────────────┐  │
   │   │              REPARAMETRIZATION TRICK                             │  │
   │   │                                                                  │  │
   │   │              Z = μ + σ × ε,  donde ε ~ N(0,1)                   │  │
   │   │                                                                  │  │
   │   │              (Esto SIEMPRE es igual, no importa la red)         │  │
   │   └─────────────────────────────────────────────────────────────────┘  │
   │                                  │                                      │
   │                                  ▼                                      │
   │   ┌─────────────────────────────────────────────────────────────────┐  │
   │   │                         DECODER                                  │  │
   │   │   ┌───────────────────────────────────────────────────────────┐ │  │
   │   │   │                                                           │ │  │
   │   │   │   Puede ser:  • MLP (capas Linear)                       │ │  │
   │   │   │               • CNN transpuesta (ConvTranspose2d)         │ │  │
   │   │   │               • RNN/LSTM (generación secuencial)          │ │  │
   │   │   │               • Transformer decoder                       │ │  │
   │   │   │               • Cualquier combinación                     │ │  │
   │   │   │                                                           │ │  │
   │   │   └───────────────────────────────────────────────────────────┘ │  │
   │   │                              │                                   │  │
   │   │                              ▼                                   │  │
   │   │                             X'                                   │  │
   │   └─────────────────────────────────────────────────────────────────┘  │
   │                                                                         │
   │   LOSS = Reconstrucción(X, X') + KL(N(μ,σ) || N(0,1))                 │
   │                                                                         │
   │   (La loss SIEMPRE tiene estas dos partes, no importa la red)         │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘
```

---

### Tabla Resumen: Dimensiones en Cada Paso

| Paso | Componente | Entrada | Salida | Operación |
|------|------------|---------|--------|-----------|
| 1 | Imagen original | - | 784 | Aplanar 28×28 |
| 2 | Encoder capa 1 | 784 | 400 | Linear + ReLU |
| 3 | Encoder rama μ | 400 | latent_dim | Linear |
| 4 | Encoder rama σ | 400 | latent_dim | Linear |
| 5 | Reparametrization | (μ, σ, ε) | latent_dim | Z = μ + σ×ε |
| 6 | Decoder capa 1 | latent_dim | 400 | Linear + ReLU |
| 7 | Decoder capa 2 | 400 | 784 | Linear + Sigmoid |
| 8 | Imagen reconstruida | 784 | 28×28 | Reformar |

**Con latent_dim = 2:**
- Compresión: 784 → 2 (reducción de 392×)
- Expansión: 2 → 784 (expansión de 392×)

---

### Código Correspondiente al Diagrama

```python
class VAE(nn.Module):
    def __init__(self, input_dim=784, hidden_dim=400, latent_dim=2):
        super(VAE, self).__init__()

        # ═══════════════════════════════════════════════════
        # ENCODER
        # ═══════════════════════════════════════════════════

        # Capa compartida
        self.encoder_fc = nn.Linear(input_dim, hidden_dim)  # 784 → 400

        # Rama de media (μ)
        self.fc_mu = nn.Linear(hidden_dim, latent_dim)      # 400 → 2

        # Rama de varianza (log_var)
        self.fc_logvar = nn.Linear(hidden_dim, latent_dim)  # 400 → 2

        # ═══════════════════════════════════════════════════
        # DECODER
        # ═══════════════════════════════════════════════════

        self.decoder_fc = nn.Linear(latent_dim, hidden_dim) # 2 → 400
        self.decoder_out = nn.Linear(hidden_dim, input_dim) # 400 → 784

    def encode(self, x):
        """
        X (784) → h (400) → μ (2), log_var (2)
        """
        h = F.relu(self.encoder_fc(x))
        mu = self.fc_mu(h)
        log_var = self.fc_logvar(h)
        return mu, log_var

    def reparameterize(self, mu, log_var):
        """
        El truco genial:
        En vez de: Z ~ N(μ, σ)
        Hacemos:   Z = μ + σ × ε, donde ε ~ N(0,1)
        """
        std = torch.exp(0.5 * log_var)  # σ = exp(0.5 × log(σ²))
        eps = torch.randn_like(std)      # ε ~ N(0,1)
        z = mu + std * eps               # Z = μ + σ × ε
        return z

    def decode(self, z):
        """
        Z (2) → h' (400) → X' (784)
        """
        h = F.relu(self.decoder_fc(z))
        x_reconstructed = torch.sigmoid(self.decoder_out(h))
        return x_reconstructed

    def forward(self, x):
        """
        Flujo completo de entrenamiento
        """
        mu, log_var = self.encode(x)
        z = self.reparameterize(mu, log_var)
        x_reconstructed = self.decode(z)
        return x_reconstructed, mu, log_var

    def generate(self, num_samples):
        """
        Generación (post-entrenamiento)
        Solo usa el decoder
        """
        z = torch.randn(num_samples, self.latent_dim)  # Z ~ N(0,1)
        x_generated = self.decode(z)
        return x_generated


def loss_function(x_reconstructed, x_original, mu, log_var):
    """
    Loss total = Loss reconstrucción + Loss KL
    """
    # Loss de reconstrucción (MSE)
    reconstruction_loss = F.mse_loss(x_reconstructed, x_original, reduction='sum')

    # Loss KL: -0.5 × Σ(1 + log_var - μ² - exp(log_var))
    kl_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())

    return reconstruction_loss + kl_loss
```

---

## Definiciones para el Parcial

### Conceptos Fundamentales

**Variable Latente:** Variable aleatoria que existe y afecta los datos observables, pero que no podemos medir ni observar directamente en el dataset (ej: "ser un 3" no está escrito en los píxeles de una imagen del número 3).

**Espacio Latente:** Espacio de menor dimensión donde se representan las características esenciales comprimidas de los datos; cada punto en este espacio corresponde a una configuración de características abstractas aprendidas por el modelo.

**Autoencoder:** Red neuronal compuesta por un encoder (que comprime datos a un espacio latente de menor dimensión) y un decoder (que reconstruye los datos originales desde esa representación comprimida), entrenada para minimizar el error de reconstrucción.

**Encoder:** Parte de un autoencoder que transforma datos de alta dimensión (ej: imagen de 784 píxeles) en una representación compacta de baja dimensión (ej: vector de 10 números); en un VAE, produce los parámetros μ y σ de una distribución.

**Decoder:** Parte de un autoencoder que transforma la representación latente comprimida de vuelta al espacio original de los datos; en generación, recibe ruido aleatorio y produce datos nuevos.

**Variational Autoencoder (VAE):** Modelo generativo que extiende el autoencoder haciendo que el encoder produzca parámetros de una distribución probabilística (μ, σ) en lugar de un vector fijo, permitiendo muestrear del espacio latente para generar datos nuevos.

### El Truco Central

**Reparametrization Trick:** Técnica que permite hacer backpropagation a través de un muestreo al expresar Z = μ + σ × ε, donde ε ~ N(0,1) es ruido fijo independiente de los parámetros, separando así la parte aleatoria (ε) de la parte paramétrica (μ, σ).

**Esperanza No Diferenciable:** Problema que surge cuando la distribución de la cual muestreamos depende de los parámetros que queremos optimizar; no podemos simplemente "meter la derivada dentro de la esperanza" porque la regla del producto genera un término que no es una esperanza.

### Funciones de Pérdida

**Loss de Reconstrucción:** Término de la pérdida del VAE que mide qué tan bien el decoder reconstruye la entrada original; típicamente MSE para valores continuos o BCE para valores binarios.

**KL Divergence (Kullback-Leibler):** Medida de qué tan diferente es una distribución de probabilidad respecto a otra; en VAEs, penaliza que la distribución latente aprendida se aleje de N(0,1), y tiene valor 0 solo cuando ambas distribuciones son idénticas.

**Función de Pérdida del VAE:** Suma de dos términos: L = L_reconstrucción + L_KL, donde el primero fuerza buenas reconstrucciones y el segundo fuerza que los latentes sigan una distribución N(0,1).

### Distribuciones y Estadística

**Distribución Normal (Gaussiana):** Distribución de probabilidad en forma de campana caracterizada por dos parámetros: media μ (centro) y varianza σ² (ancho); la notación N(μ, σ²) indica una normal con esos parámetros.

**Normal Multivariada:** Generalización de la normal a múltiples dimensiones, caracterizada por un vector de medias μ y una matriz de covarianza Σ que describe tanto las varianzas individuales como las correlaciones entre variables.

**Matriz de Covarianza:** Matriz simétrica donde los elementos de la diagonal son las varianzas de cada variable y los elementos fuera de la diagonal son las covarianzas entre pares de variables; define la forma y orientación de la "elipse" de una normal multivariada.

**Covarianza:** Medida de cómo dos variables aleatorias varían juntas; Cov(X,Y) > 0 significa que cuando X sube, Y tiende a subir; Cov(X,Y) < 0 significa relación inversa; Cov(X,Y) = 0 indica independencia lineal.

**Varianza:** Medida de dispersión de una variable aleatoria respecto a su media; Var(X) = E[(X - μ)²]; indica "qué tan ancha es la campana" de la distribución.

**Esperanza (Valor Esperado):** Promedio ponderado de todos los valores posibles de una variable aleatoria, donde cada valor se pondera por su probabilidad; E[X] = Σ x·P(x) para variables discretas.

### Optimización

**Estimación Monte Carlo:** Técnica para aproximar una esperanza E[f(X)] calculando el promedio de f(x) sobre muestras aleatorias: E[f(X)] ≈ (1/N) Σ f(xᵢ).

**Backpropagation:** Algoritmo que calcula eficientemente los gradientes de la función de pérdida respecto a todos los parámetros de la red, propagando el error desde la salida hacia la entrada usando la regla de la cadena.

**Descenso de Gradiente:** Algoritmo de optimización que actualiza los parámetros en la dirección opuesta al gradiente: θ_nuevo = θ_viejo - lr × ∂Loss/∂θ, donde lr es el learning rate.

### Conceptos del Práctico

**Dimensión Latente (latent_dim):** Hiperparámetro que define el tamaño del vector Z en el espacio latente; valores pequeños (ej: 2) comprimen mucho pero permiten visualización, valores grandes (ej: 64) capturan más detalle pero son más difíciles de visualizar.

**Hiperparámetro:** Parámetro del modelo que NO se aprende durante el entrenamiento sino que se define antes de entrenar (ej: latent_dim, learning_rate, número de capas); se ajusta mediante experimentación.

### Reglas Probabilísticas

**Regla de la Suma:** P(X) = Σ_z P(X|Z) × P(Z); permite escribir la probabilidad de X como suma sobre todos los posibles valores de una variable latente Z.

**Regla de la Cadena (Derivadas):** ∂f(g(x))/∂x = (∂f/∂g) × (∂g/∂x); permite derivar composiciones de funciones multiplicando las derivadas parciales; es la base matemática de backpropagation.

### Comparación Clave

| Concepto | Autoencoder Simple | VAE |
|----------|-------------------|-----|
| Salida del encoder | Vector Z fijo | Parámetros μ y σ |
| Naturaleza de Z | Determinístico | Probabilístico (muestreado) |
| Puede generar | No (necesita entrada) | Sí (muestrea de N(0,1)) |
| Loss | Solo reconstrucción | Reconstrucción + KL |

### Fórmulas Clave

**Reparametrization:** Z = μ_θ(x) + σ_θ(x) × ε, donde ε ~ N(0,1)

**KL para Normales vs N(0,1):** KL = -0.5 × Σ(1 + log(σ²) - μ² - σ²)

**Loss Total VAE:** L = MSE(X, X̂) + KL(N(μ,σ) || N(0,1))

---

## Posibles Preguntas de Parcial

### ¿Qué pasa si cambiamos la dimensión del espacio latente (latent_dim)?

> "Está seteada en dos y para una parte de más adelante está bueno que lo prueben una vez en dos y después hay unas preguntas como para pensar qué pasa si la cambiamos y les incentivo a que la cambien."

**Respuesta:** Si **aumentamos** latent_dim (ej: de 2 a 10 o 64), el modelo tiene más capacidad para representar características de los datos, mejorando la reconstrucción, pero perdemos la posibilidad de visualizar el espacio latente en 2D y aumentamos los parámetros a entrenar. Si **disminuimos** latent_dim (ej: a 1), comprimimos demasiado y las reconstrucciones serán malas porque no hay suficiente capacidad para capturar la variabilidad de los datos. El balance está en encontrar un latent_dim lo suficientemente pequeño para comprimir, pero lo suficientemente grande para representar bien los datos.

### ¿Por qué el encoder de un VAE produce (μ, σ) en vez de Z directamente?

**Respuesta:** Porque queremos que el espacio latente sea una **distribución probabilística** de la cual podamos muestrear, no un vector fijo. Al producir los parámetros de una distribución Normal(μ, σ), podemos luego generar imágenes nuevas muestreando de Normal(0,1) y pasando por el decoder.

### ¿Qué es el Reparametrization Trick y por qué es necesario?

**Respuesta:** Es expresar Z = μ + σ × ε donde ε ~ N(0,1), en vez de muestrear directamente Z ~ N(μ,σ). Es necesario porque el muestreo directo de una distribución paramétrica no es diferenciable (no podemos hacer backprop a través de él), pero con el truco, la parte aleatoria (ε) queda separada de los parámetros entrenables (μ, σ).

### ¿Para qué sirve la KL divergence en la loss del VAE?

**Respuesta:** Para forzar que la distribución latente aprendida (Normal(μ,σ)) se parezca a Normal(0,1). Sin ella, el encoder podría aprender valores extremos (μ=1000000, σ=0.001) que funcionan para reconstruir pero no permiten generar, porque después muestreamos de N(0,1).

### ¿Cuál es la diferencia fundamental entre un Autoencoder simple y un VAE?

**Respuesta:** En un autoencoder simple, el encoder produce un vector Z **fijo y determinístico**, mientras que en un VAE produce los **parámetros de una distribución** (μ, σ) de la cual se muestrea Z. Esto permite que el VAE pueda generar datos nuevos muestreando del espacio latente.

### ¿Por qué usamos distribuciones Normales (Gaussianas) para el espacio latente?

**Respuesta:** Por tres razones: (1) empíricamente funcionan muy bien, (2) tienen propiedades matemáticas convenientes (la KL entre dos normales tiene fórmula cerrada), y (3) muestrear de N(0,1) es computacionalmente trivial.

### ¿Qué es una variable latente y por qué se llama "latente"?

**Respuesta:** Es una variable que **existe y afecta los datos**, pero que **no podemos observar directamente** en el dataset. Se llama "latente" (= oculta) porque no está escrita explícitamente en los datos; por ejemplo, "ser un 3" no está en ningún píxel de una imagen del número 3.

### ¿Qué problema tienen las "esperanzas no diferenciables"?

**Respuesta:** Cuando la distribución de la cual muestreamos depende de los parámetros θ que queremos optimizar, al derivar la esperanza aparece un término ∂p_θ(z)/∂θ que no se puede aproximar fácilmente con Monte Carlo. El reparametrization trick soluciona esto separando la parte aleatoria de la parte paramétrica.

### ¿Por qué la loss del VAE tiene DOS términos y no solo uno?

**Respuesta:** Porque tiene dos objetivos: (1) **reconstruir bien** (loss de reconstrucción: que X' se parezca a X), y (2) **regularizar el espacio latente** (KL divergence: que Z se parezca a N(0,1) para poder generar después). Sin el segundo término, el modelo reconstruiría bien pero no podríamos generar.

### ¿Cómo se generan imágenes nuevas con un VAE ya entrenado?

**Respuesta:** Se descarta el encoder, se muestrea Z ~ Normal(0,1), y se pasa ese Z por el decoder. Si el modelo está bien entrenado, la salida será una imagen verosímil similar a las del dataset de entrenamiento.

### ¿Qué representa la matriz de covarianza en una normal multivariada?

**Respuesta:** Los elementos de la **diagonal** son las varianzas de cada variable (cuánto se dispersa cada una). Los elementos **fuera de la diagonal** son las covarianzas entre pares de variables (cómo varían juntas). Si la covarianza es cero, las variables son independientes; si no, están correlacionadas.
