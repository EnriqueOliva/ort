# Explicación de Temas - Clase del 16-09-2025

## La Gran Pregunta: ¿Qué Estamos Haciendo Hoy?

Esta clase es una **continuación directa** de la clase anterior. El profesor conecta dos mundos:

1. **El mundo teórico**: Estimación de distribuciones, KL Divergence, optimización
2. **El mundo práctico**: Entrenar perceptrones con Binary Cross-Entropy

El objetivo es mostrar **la cadena completa de razonamiento**: desde "quiero que mi modelo genere imágenes realistas" hasta "por eso uso `nn.BCELoss()` en PyTorch".

Como dijo el profesor: "Tiene sentido para que puedan aunar lo que tiene práctico, que es bastante concreto, con la teoría."

---

## Conexión con la Clase Anterior

### ¿Qué Vimos la Clase Pasada?

En la clase 4 construimos:
- El modelo de Hinton (perceptrones con matriz triangular)
- El modelo de Bengio (múltiples capas)
- La idea de que cada píxel es una Bernoulli
- El forward pass y la generación secuencial

Pero quedó pendiente una pregunta fundamental: **¿Por qué usamos Binary Cross-Entropy?**

### ¿Por Qué Importa Ahora?

Porque hoy vamos a demostrar que BCE **no es arbitraria**. Viene de:

```
Quiero que mi modelo se parezca a los datos reales
        ↓
KL Divergence (mide diferencia entre distribuciones)
        ↓
Negative Log-Likelihood (simplificación)
        ↓
Binary Cross-Entropy (caso específico para Bernoulli)
```

Cuando termines esta clase, vas a entender **por qué** cada línea de código del práctico tiene sentido.

---

## 1. El Problema Fundamental: Encontrar Buenos Parámetros

### ¿Qué Estamos Tratando de Hacer?

El profesor comienza recordando el objetivo principal:

> "La noción es hallar esos buenos parámetros."

Piensa en esto: cuando tienes una red neuronal, los "parámetros" son todos los pesos (W) y sesgos (B). Pero, ¿cuáles son los "mejores" valores para ellos?

### ¿Qué Significa "Buenos Parámetros"?

La "bondad" de los parámetros se define con **una noción de pérdida (loss)**. Es decir, necesitamos una forma matemática de medir qué tan bien o mal funcionan nuestros parámetros actuales.

### La Notación θ* (theta estrella)

El profesor usa **θ*** (theta estrella) para representar **el mejor conjunto de parámetros posible**.

> "Si yo tengo a mi conjunto de parámetros y lo denomino theta... theta estrella es el mejor conjunto. Lo mismo que hacíamos en agentes."

Esta notación viene de teoría de optimización y agentes inteligentes.

### La Conexión con Inteligencia

> "Es la noción de optimización. Recuerdan que los agentes inteligentes, agentes racionales o sistemas racionales son aquellos que optimizan alguna noción de ganancia o minimizan alguna noción de pérdida."

**En resumen:**

```
θ = parámetros actuales de nuestro modelo (W y B)
θ* = los parámetros óptimos (los que queremos encontrar)
"Óptimos" = minimizan alguna función de pérdida
```

---

## 2. La KL Divergence: Midiendo Diferencias Entre Distribuciones

### ¿Qué es la KL Divergence?

La clase pasada "sacaron de la galera" (como dice el profesor) una medida matemática llamada **KL Divergence**.

La KL Divergence mide **qué tan diferentes son dos distribuciones de probabilidad**.

### ¿Entre Qué Distribuciones?

> "Como yo estoy estimando distribuciones, yo quiero que mi P_θ se parezca mucho a mi P o mi P_data."

Las dos distribuciones son:

| Distribución | Significado | Ejemplo |
|--------------|-------------|---------|
| **P_data** (o simplemente P) | La distribución **real** de los datos | Cómo se ven realmente los números escritos a mano |
| **P_θ** (P theta) | Nuestro **modelo paramétrico** | Lo que el perceptrón cree sobre cómo se ven los números |

> "Básicamente es que mi modelo paramétrico que me estima la distribución de los elementos se parezca mucho a la distribución real, a la chance real que tiene el elemento de ocurrir en mi espacio de sucesos."

### Analogía Simple

```
P_data = Cómo realmente se distribuyen los números escritos a mano en el mundo
P_θ = Lo que tu modelo piensa sobre cómo se distribuyen
KL Divergence = Qué tan equivocado está tu modelo
```

Si KL es pequeño → El modelo es bueno
Si KL es grande → El modelo está muy equivocado

### Propiedades Importantes de la KL Divergence

El profesor menciona dos propiedades cruciales:

**1. Es una medida de distancia:**
> "Se agranda cuando son muy distintas, se achica cuando son parecidas."

- Si las distribuciones son iguales: KL = 0
- Si son muy diferentes: KL es grande

**2. Es derivable:**
> "Es derivable porque al final es el logaritmo de P... Si P es derivable también."

Esto es fundamental porque nos permite optimizar usando gradientes.

### Aclaración sobre Notación

El profesor hace una advertencia importante:

> "Coma es la manera de diferenciar los dos parámetros de la divergencia KL. No tiene un significado... No tiene más semántica que eso."

Cuando veas:
- **KL(P_θ, P_data)** o
- **KL(P_θ || P_data)**

La coma o las barras verticales son **solo separadores**. No tienen significado matemático más allá de separar las dos distribuciones.

---

## 3. De la KL Divergence a la Función de Pérdida Práctica

### La Derivación (que ocupó un pizarrón entero)

> "Yo no voy a hacer la derivación porque esto llevó un pizarrón entero. Pero la clase pasada dijimos esto..."

El profesor nos da el resultado final sin repetir toda la matemática.

### La Simplificación Crucial

Cuando minimizas la KL Divergence respecto a θ (tus parámetros), **gran parte de la expresión desaparece** porque no depende de θ.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          LA SIMPLIFICACIÓN                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   KL(P_data || P_θ) = [parte que no depende de θ] + [parte que depende] │
│                        \_____________________/      \__________________/ │
│                        Se elimina al optimizar      Esto es lo que queda │
│                                                                          │
│   Resultado: Minimizar KL ≈ Minimizar -E[log P_θ(x)]                    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

Donde:
- **E** significa "esperanza" o "valor esperado"
- La esperanza se calcula sobre **P_data** (los datos reales)
- **log P_θ(x)** es el logaritmo de la probabilidad que nuestro modelo asigna a un dato x

### ¿Qué Significa Esto en Lenguaje Simple?

**Queremos que nuestro modelo le asigne alta probabilidad a los datos que realmente existen.**

Piénsalo así:
- Si un tipo de número (digamos, el "7") es común en los datos reales
- Nuestro modelo debería darle alta probabilidad
- Si le da baja probabilidad a algo que es común, eso es malo
- El logaritmo negativo convierte esto en algo que queremos minimizar

### Por Qué se Simplifica

> "Si yo estoy minimizando de acuerdo a θ, en realidad se me va gran parte de la expresión."

La razón matemática es que parte de la KL Divergence no contiene θ. Al derivar respecto a θ y buscar el mínimo, esa parte constante desaparece.

---

## 4. Notación en Deep Learning: L y J

### Por Qué Necesitamos Estos Nombres

Cuando trabajas en Deep Learning, vas a encontrar constantemente dos letras: **L** y **J**. El profesor las introduce para que no te confundas al leer papers o libros.

### L (Loss - Pérdida)

> "En contexto de deep learning... a esto se le llama L por loss."

**L** representa la **pérdida para un dato individual**.

> "A cuánto le erro cuando le erro en un dato."

### J (Cost - Costo)

**J** representa el **costo total**, que es el promedio de todas las pérdidas individuales.

> "El J se refiere a la esperanza de esa función... se le llama como costo en algún momento."

**J = E[L]**

### La Diferencia Visual

```
┌─────────────────────────────────────────────────────────────────────┐
│                        L vs J                                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   L = Error en UN dato                                               │
│       Ejemplo: "Qué tan mal predije la imagen #543"                 │
│                                                                      │
│   J = Promedio de TODOS los errores                                  │
│       Ejemplo: "En promedio, qué tan mal predigo las 10,000 imágenes"│
│                                                                      │
│   Relación: J = (1/N) × Σ L(imagen_i)                               │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Por Qué Esta Distinción es Importante

> "Van a estar minimizando J que vas a minimizar... una esperanza de alguna L cuadrada... la L que sea."

Cuando lees código o papers:
- Ves "loss function" → se refieren a L
- Ves "cost function" → se refieren a J
- Son conceptos relacionados pero diferentes
- **J es lo que realmente minimizas** en la práctica (el promedio)

---

## 5. De la Esperanza al Promedio: Empirical Risk Minimization

### El Problema con la Esperanza

El profesor señala algo crucial:

> "La esperanza no es algo accesible, terminamos optimizando la media."

**¿Por qué la esperanza "no es accesible"?**

Para calcular la esperanza **E[log P_θ(x)]** necesitarías:
1. Conocer la distribución real completa P_data
2. Poder integrar o sumar sobre **todos** los posibles datos

¡Pero si conocieras perfectamente P_data, no necesitarías entrenar un modelo! El problema es justamente que **no la conocemos**.

### La Solución Práctica

En lugar de la esperanza teórica, usamos **el promedio sobre nuestro conjunto de entrenamiento**.

> "Asumimos que tenemos algún conjunto de datos de entrenamiento y lo que hacemos es optimizar sobre ese conjunto que es uno sobre N del conjunto por la sumatoria de todos los x que pertenecen a entrenamiento."

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DE TEORÍA A PRÁCTICA                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   TEÓRICO (imposible de calcular):                                   │
│                                                                      │
│       θ* = argmin_θ E_{P_data}[-log P_θ(x)]                         │
│                     ↑                                                │
│                     Esperanza sobre distribución real (desconocida)  │
│                                                                      │
│   PRÁCTICO (lo que realmente hacemos):                               │
│                                                                      │
│       θ* = argmin_θ (1/N) Σ_{x ∈ D_train} [-log P_θ(x)]             │
│                           ↑                                          │
│                           Promedio sobre nuestros datos              │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

Donde:
- **D_train** es tu conjunto de datos de entrenamiento
- **N = |D_train|** es la cantidad de datos (por ejemplo, 10,000 imágenes)
- **Σ** suma sobre todos esos datos

### El Nombre Técnico

> "Van a encontrar en algunos libros... esto se le llama también Empirical Risk Minimization."

**"Empírico"** significa basado en observaciones reales (tus datos de entrenamiento), no en la teoría perfecta.

### Ejemplo Numérico

```
Tienes 3 imágenes en tu dataset:
   - Imagen 1: -log P_θ(imagen1) = 2.3
   - Imagen 2: -log P_θ(imagen2) = 1.5
   - Imagen 3: -log P_θ(imagen3) = 3.1

TEÓRICO (si conocieras todas las imágenes posibles del universo):
   J = E[-log P_θ] = ??? (imposible calcular)

PRÁCTICO (con tus 3 imágenes):
   J = (1/3) × (2.3 + 1.5 + 3.1) = (1/3) × 6.9 = 2.3

Este 2.3 es tu pérdida empírica. Es lo que minimizas.
```

---

## 6. La Generalidad del Enfoque: Agnóstico del Modelo

### Un Punto MUY Importante

El profesor hace una pausa crucial:

> "Esto hasta este momento, todo lo que escribí es **agnóstico del modelo** que estoy usando."

**"Agnóstico"** significa que **no depende del tipo específico de modelo**.

### Los Diferentes Tipos de Modelos Generativos

El profesor enumera cuatro tipos muy diferentes:

1. **Modelos autorregresivos** (como el perceptrón de Hinton)
2. **Redes Generativas Adversarias (GANs)**
3. **Variational Autoencoders (VAEs)**
4. **Modelos de Difusión**

> "Nombré cuatro modelos que son todos distintos y que estiman la probabilidad de un elemento de manera distinta... pero no nos importa."

### ¿Por Qué es Importante Esto?

> "Hasta esta línea... vamos a decir que tenemos un enfoque general para distribuciones con deep learning. Siempre que yo tenga un modelo paramétrico que me estima la probabilidad de un elemento, yo puedo hacer esta optimización para obtener θ*."

**Lo que importa es:**
1. Tener un modelo P_θ que estime probabilidades
2. Poder evaluar esas probabilidades
3. Poder derivar respecto a θ

Si cumples esos tres requisitos, **puedes usar todo lo que el profesor acaba de explicar**, independientemente del tipo específico de modelo.

### La Línea Divisoria Visual

```
┌─────────────────────────────────────────────────────────────────────┐
│            HASTA AQUÍ: TEORÍA GENERAL                                │
│                                                                      │
│   θ* = argmin_θ (1/N) Σ [-log P_θ(x)]                               │
│                                                                      │
│   Aplica a: Autorregresivos, GANs, VAEs, Difusión, etc.             │
├─────────────────────────────────────────────────────────────────────┤
│            DE AQUÍ EN ADELANTE: ZOOM EN AUTORREGRESIVOS              │
│                                                                      │
│   Vamos a hacer específico para modelos autorregresivos             │
│   (como el perceptrón de Hinton)                                    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 7. Modelos Autorregresivos: El Zoom Específico

### La Transición

> "El saltito que les quiero mostrar es bueno, cómo de esto se llega en realidad a la pérdida que está asociada al perceptrón de Hinton o a cualquier modelo autorregresivo."

### ¿Qué es un Modelo Autorregresivo?

> "Cualquier modelo que me estima la probabilidad de una variable condicionada por sus predecesoras."

En palabras más simples:
- **"Auto"** = sí mismo
- **"Regresivo"** = hacia atrás
- Un modelo que usa valores anteriores para predecir el siguiente

### Variables Múltiples

El profesor hace una aclaración importante:

> "Una cosa que está oculta es que este x en realidad es un elemento multivariado, o sea, que tiene sus... es una serie de variables aleatorias conjuntas."

Cuando escribimos **x**, en realidad es:

**x = (x₁, x₂, x₃, ..., xₙ)**

```
Ejemplo: Una imagen de 28×28 = 784 píxeles

x = (x₁, x₂, x₃, ..., x₇₈₄)
     ↑   ↑   ↑        ↑
     │   │   │        └── Píxel 784 (esquina inferior derecha)
     │   │   └── Píxel 3
     │   └── Píxel 2
     └── Píxel 1 (esquina superior izquierda)
```

---

## 8. La Regla de la Cadena para Probabilidades

### El Problema de las Probabilidades Conjuntas

> "¿Cómo estimamos la probabilidad... cómo estimamos la conjunta? Pero nunca tenemos un estimador de la conjunta."

**¿Por qué no?** Porque estimar P(x₁, x₂, ..., x₇₈₄) directamente requeriría considerar todas las posibles combinaciones de 784 píxeles.

```
Para 784 píxeles binarios:
   Combinaciones posibles = 2^784

   Eso es un número con 236 dígitos.
   Más que el número de átomos en el universo observable.

   IMPOSIBLE de almacenar o procesar.
```

### La Solución: Descomponer con la Regla de la Cadena

> "Es una productoria de las condicionales."

Usando la **regla del producto** (o regla de la cadena):

```
P(x) = P(x₁, x₂, ..., xₙ)
     = P(x₁) × P(x₂|x₁) × P(x₃|x₁,x₂) × ... × P(xₙ|x₁,...,xₙ₋₁)
```

> "Es la productoria de mis condicionales desde i = 1 hasta n, siendo n, por ejemplo, el tamaño de imagen, la cantidad de píxeles."

### Ejemplo con 3 Píxeles

Para entenderlo mejor, imagina solo 3 píxeles:

```
P(x₁, x₂, x₃) = P(x₁) × P(x₂|x₁) × P(x₃|x₁,x₂)

Traducción:
- P(x₁): Probabilidad del primer píxel (sin condiciones)
- P(x₂|x₁): Probabilidad del segundo píxel DADO el primero
- P(x₃|x₁,x₂): Probabilidad del tercero DADOS los dos primeros
```

### Visualización del Proceso

```
┌─────────────────────────────────────────────────────────────────────┐
│                    REGLA DE LA CADENA                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   Imagen: [■][□][■][□][■]...  (784 píxeles)                         │
│            1  2  3  4  5                                             │
│                                                                      │
│   P(imagen completa) =                                               │
│                                                                      │
│      P(■)  × P(□|■)  × P(■|■,□)  × P(□|■,□,■)  × ...                │
│       ↑        ↑          ↑           ↑                              │
│       │        │          │           │                              │
│    Píxel 1  Píxel 2    Píxel 3    Píxel 4                           │
│    (solo)   (dado 1)  (dados 1,2) (dados 1,2,3)                     │
│                                                                      │
│   Cada término es una probabilidad condicional.                      │
│   Cada perceptrón del modelo estima UNA de estas.                   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Aplicando a Nuestra Pérdida

Entonces, cuando calculamos **-log P_θ(x)**, tenemos:

```
-log P_θ(x) = -log [P_θ(x₁) × P_θ(x₂|x₁) × ... × P_θ(xₙ|x₁,...,xₙ₋₁)]
```

---

## 9. El Truco del Logaritmo: Estabilidad Numérica

### Un Problema Técnico Importante

El profesor introduce un tema de computación numérica:

> "Esto es muy lindo y la expresión podríamos dejarla acá. Nosotros estamos trabajando con computadores. ¿Qué pasa con las computadoras y con la representación numérica?"

Y pregunta: "¿Qué tenemos?"

### Las Respuestas de los Estudiantes

Los estudiantes responden:
- "Float... precisión"
- "Se va de rango"
- "Queda no representable"

> "Sí, se va de rango o queda no representable."

### El Problema Explicado

**1. Valores muy pequeños (underflow):**

> "Estos elementos son valores entre 0 y 1 y esto es una productoria."

Cuando multiplicas muchas probabilidades:

```
0.9 × 0.85 × 0.92 × 0.88 × ... (784 veces)

Resultado: 0.000000000000000000000000000000...1

Este número es TAN pequeño que la computadora lo redondea a 0.
Eso se llama "underflow".
```

**2. Error acumulado:**

> "El error acumulado por la productoria es mayor que el error acumulado por la sumatoria."

Cada operación en una computadora tiene un pequeño error de redondeo. Cuando haces 784 multiplicaciones, estos errores se acumulan significativamente.

### La Solución: Logaritmos

> "El logaritmo de la productoria es lo mismo que la suma de los logaritmos."

**Propiedad matemática fundamental:**

```
log(A × B × C) = log(A) + log(B) + log(C)
```

Aplicándolo:

```
log[P(x₁) × P(x₂|x₁) × ...] = log P(x₁) + log P(x₂|x₁) + ...
```

### ¿Por Qué es Mejor?

> "Ese truco es un cambio... que podríamos no hacerlo, es la misma expresión, pero optimizando numéricamente me aporta... Porque no me achica tanto los elementos y no soy castigado por los errores aportados por la representación."

```
┌─────────────────────────────────────────────────────────────────────┐
│              CON MULTIPLICACIÓN vs CON LOGARITMOS                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   CON MULTIPLICACIÓN:                                                │
│   0.9 × 0.85 × 0.92 × ... = 0.000000000001 → UNDERFLOW → 0          │
│                                                                      │
│   CON LOGARITMOS:                                                    │
│   log(0.9) + log(0.85) + log(0.92) + ...                            │
│   = -0.105 + (-0.163) + (-0.083) + ...                              │
│   = -28.5  ← Número manejable, sin problemas                        │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

> "El logaritmo nos cambia el orden de magnitud de los elementos."

### La Expresión Final para Autorregresivos

Después de aplicar el logaritmo:

```
θ* = argmin_θ (1/N) Σₓ Σᵢ₌₁ⁿ [-log P_θ(xᵢ | x₁, ..., xᵢ₋₁)]

Traducción:
- Para cada imagen x en el dataset...
- Para cada píxel i de la imagen...
- Calcula -log de la probabilidad condicional
- Suma todo
- Promedia
- Minimiza respecto a θ
```

---

## 10. El Problema del Perceptrón Binario

### Una Sutileza Crucial

> "Acá faltó algo que podemos hablar que es en realidad que nos aporta de cara al práctico..."

Hasta ahora, todo ha sido teoría general. Ahora viene **el detalle técnico específico** de los perceptrones.

### ¿Qué Nos Da un Perceptrón?

El profesor plantea:

> "Todo esto está muy lindo... yo quiero minimizar menos el logaritmo de la probabilidad de un elemento. Sí, pero... yo asumo que mi función de probabilidad me da la probabilidad efectiva de que el xᵢ tome el valor que toma."

Luego pregunta: "Cuando ustedes entrenan un perceptrón, ¿qué probabilidad da el perceptrón? Un perceptrón binario."

Un estudiante responde: "La probabilidad de que valga uno"

### El Problema Fundamental

El profesor lo hace explícito:

> "Yo no quiero la probabilidad de que valga uno. Yo quiero... la probabilidad que valga cero."

```
┌─────────────────────────────────────────────────────────────────────┐
│                    EL PROBLEMA DEL PERCEPTRÓN                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   NECESITAMOS:                                                       │
│   P_θ(Xᵢ = xᵢ | predecesores)                                       │
│           ↑                                                          │
│           Puede ser 0 o 1, dependiendo del dato real                │
│                                                                      │
│   EL PERCEPTRÓN NOS DA:                                              │
│   P_θ(Xᵢ = 1 | predecesores)                                        │
│           ↑                                                          │
│           SIEMPRE la probabilidad de que sea 1                      │
│                                                                      │
│   PROBLEMA:                                                          │
│   - Si xᵢ = 1 en los datos → OK, usamos lo que da el perceptrón    │
│   - Si xᵢ = 0 en los datos → ¿¿¿??? El perceptrón no nos da eso   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Profundizando en el Problema

> "Los valores que pueden tomar mis elementos las posiciones pueden ser uno o cero. Entonces, cuando yo meto todos los predecesores en mi perceptrón, mi perceptrón siempre me da la probabilidad de uno. Pero, ¿qué pasa si mi dato en esa posición es un cero?"

### Notación: Variable vs Valor

El profesor hace una distinción notacional importante:

> "Esto es como... variable aleatoria Xᵢ sea igual a xᵢ condicionado con los x... Y acá... Esto es valor y esto es variable."

```
┌─────────────────────────────────────────────────────────────────────┐
│                    VARIABLE vs VALOR                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   Xᵢ (mayúscula o notación especial) = VARIABLE ALEATORIA           │
│       "El i-ésimo píxel"                                             │
│       Puede tomar diferentes valores (0 o 1)                        │
│                                                                      │
│   xᵢ (minúscula) = VALOR CONCRETO observado                         │
│       "El valor específico que tiene el píxel i en ESTA imagen"     │
│       Por ejemplo: xᵢ = 1                                           │
│                                                                      │
│   P(Xᵢ = xᵢ) = "Probabilidad de que la variable Xᵢ                  │
│                 tome el valor concreto xᵢ"                          │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### La Limitación Expresada Formalmente

> "Un perceptrón no me termina de satisfacer esta expresión. Si yo tengo un perceptrón, no lo puedo... Esa es la optimización... Porque el perceptrón no me da en una dirección una probabilidad, no me da la probabilidad cuando valores."

Y concluye:

> "O sea, un perceptrón no es esta función. Un perceptrón es la probabilidad de que Xᵢ sea uno condicionado con los demás, no la probabilidad de que Xᵢ en general, no es la probabilidad de cuando que Xᵢ es cero."

### Lo Que Necesitamos vs Lo Que Tenemos

```
┌─────────────────────────────────────────────────────────────────────┐
│                    NECESITAMOS vs TENEMOS                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   NECESITAMOS una función que:                                       │
│   - Si el dato real es 1 → nos dé P(X=1)                            │
│   - Si el dato real es 0 → nos dé P(X=0)                            │
│                                                                      │
│   TENEMOS un perceptrón que:                                         │
│   - SIEMPRE da P(X=1)                                                │
│   - Nunca da P(X=0) directamente                                    │
│                                                                      │
│   CONCLUSIÓN:                                                        │
│   "Esta expresión no la puedo usar si tengo un perceptrón.          │
│    Necesito hacer algo más."                                        │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 11. Teoría General vs Implementación Práctica

### Clarificación del Nivel de Abstracción

> "Yo creo que lo importante eso. No está mal. Tiene que ver... O sea, esto no está mal. Yo tengo una función que me da esto, pero un perceptrón no me da eso."

Y resume:

> "Lo que digo es hasta acá de vuelta estamos en teoría general de la Empirical Risk Minimization de modelos autorregresivos. Es válido."

### El "Pero" Crucial

> "Pero si tengo un perceptrón, no lo puedo enchufar en esta función de... no lo puedo enchufar acá directamente porque un perceptrón no es un P_θ de un xᵢ cualquiera, es un P_θ de xᵢ = 1."

### Explicación Conceptual

El profesor lo plantea de forma muy clara:

> "Para cuando el xᵢ es cero, al perceptrón solo no lo puedo usar... no puedo derivarlo porque no me está dando el valor que yo quiero."

Y luego simplifica:

> "Piénsenlo así, sin mirar a fondo, yo quiero una función de probabilidad que cuando mi dato tiene chances de ser cero, le dé mucha probabilidad ahí. Y cuando mi dato tiene mucha chance de ser uno, le dé mucha probabilidad a ser uno."

**En resumen:** Necesitamos una función flexible que funcione bien tanto cuando el dato es 0 como cuando es 1.

---

## 12. La Solución: Binary Cross-Entropy (BCE)

### La Introducción

> "Lo podés hacer. Sí, lo puedes hacer. Y ahí estamos induciendo lo que se llama la entropía cruzada."

> "No es otro gran término, es este término así... para el perceptrón."

### La Fórmula de Binary Cross-Entropy

El profesor escribe:

```
BCE(xᵢ) = -[xᵢ × log(σᵢ) + (1-xᵢ) × log(1-σᵢ)]

Donde:
- xᵢ = el valor real del dato (0 o 1)
- σᵢ = la salida del perceptrón = P_θ(Xᵢ=1 | predecesores)
```

### ¿Cómo Funciona la Magia?

> "¿Y qué me hace esto? Que si el dato es uno, me voy a quedar con la probabilidad... con el logaritmo... y si el dato es cero..."

**CASO 1: El dato real es xᵢ = 1**

```
BCE = -[1 × log(σᵢ) + (1-1) × log(1-σᵢ)]
    = -[1 × log(σᵢ) + 0 × log(1-σᵢ)]
    = -[log(σᵢ) + 0]
    = -log(σᵢ)

Queremos que σᵢ sea GRANDE (cercano a 1)
para que -log(σᵢ) sea PEQUEÑO (buena predicción).
```

**CASO 2: El dato real es xᵢ = 0**

```
BCE = -[0 × log(σᵢ) + (1-0) × log(1-σᵢ)]
    = -[0 + 1 × log(1-σᵢ)]
    = -log(1-σᵢ)

Queremos que (1-σᵢ) sea GRANDE, es decir,
que σᵢ sea PEQUEÑO (cercano a 0).
```

### Tabla de Ejemplo

| Dato real (xᵢ) | Perceptrón (σᵢ) | BCE | ¿Bien o mal? |
|----------------|-----------------|-----|--------------|
| 1 | 0.95 | -log(0.95) = 0.05 | Bien (bajo) |
| 1 | 0.10 | -log(0.10) = 2.30 | Mal (alto) |
| 0 | 0.05 | -log(0.95) = 0.05 | Bien (bajo) |
| 0 | 0.90 | -log(0.10) = 2.30 | Mal (alto) |

### Notación del Perceptrón

> "Como el perceptrón... este P no es cualquier P_θ i, es un perceptrón, llamémosle... es σ... el logaritmo es de σ perceptrón... Y obviamente tiene los parámetros θ."

**σ (sigma)** es la notación común para la salida de un perceptrón con sigmoide.

---

## 13. Interpretación de la Binary Cross-Entropy

### Pregunta de un Estudiante

Un estudiante observa:

> "Ahí está... estás usando la Binary Cross Entropy, pero no como una función de costo, sino más bien como una función de activación o una cosa parecida... para poder manipular el resultado perceptrón a lo que vos necesitás."

### La Respuesta del Profesor

> "Es una función de costo también... es una función de costo local a la probabilidad condicional que termina, vos tenés que terminar haciendo una adición en todas las condicionales para tener el costo efectivo del dato."

### Los Niveles de la Función de Costo

```
┌─────────────────────────────────────────────────────────────────────┐
│                    NIVELES DE COSTO                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   NIVEL 1: BCE para una posición (local)                            │
│   BCE(xᵢ) = error en predecir el píxel i                            │
│   Ejemplo: BCE del píxel 543 = 0.12                                 │
│                                                                      │
│   NIVEL 2: Pérdida de un dato (suma de BCEs)                        │
│   L(x) = Σᵢ BCE(xᵢ) = error total en una imagen                     │
│   Ejemplo: L(imagen) = suma de 784 BCEs = 95.4                      │
│                                                                      │
│   NIVEL 3: Costo total (promedio sobre datos)                       │
│   J = (1/N) Σₓ L(x) = error promedio en todo el dataset             │
│   Ejemplo: J = promedio de 10,000 imágenes = 87.2                   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### ¿De Dónde Viene?

> "¿De qué se deriva esto? De que la probabilidad paramétrica de que un dato sea efectivamente de ese valor, no es lo que el perceptrón nos da por cómo está escrito."

### Interpretación del Profesor

> "Es una derivación mía, una interpretación nuestra... pero al final es lo que terminamos haciendo, porque tengo que recordar eso que el perceptrón es un estimador, pero en realidad no estima para un lado solo."

**La BCE es un "adaptador"** que hace que el perceptrón funcione para nuestro problema específico.

---

## 14. La BCE como Selector

### La Observación de los Ayudantes

Un ayudante comenta:

> "Tenemos que pensar que en realidad la BCE... es una especie de selector... esto no vale de los dos lados, o vale de uno, o vale del otro."

### Los Dos Términos

Recordemos la fórmula:

```
BCE = -[xᵢ × log(σᵢ) + (1-xᵢ) × log(1-σᵢ)]
      \______________/   \________________/
       Término 1          Término 2
```

**Solo uno de estos términos se "activa" a la vez:**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    BCE COMO SELECTOR                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   Si xᵢ = 1:                                                         │
│      Término 1: 1 × log(σᵢ) = log(σᵢ)     ← ACTIVO                  │
│      Término 2: (1-1) × log(1-σᵢ) = 0     ← APAGADO                 │
│                                                                      │
│   Si xᵢ = 0:                                                         │
│      Término 1: 0 × log(σᵢ) = 0           ← APAGADO                 │
│      Término 2: (1-0) × log(1-σᵢ) = log(1-σᵢ)  ← ACTIVO            │
│                                                                      │
│   Es como un switch: dependiendo del dato real,                     │
│   se usa un término o el otro, NUNCA los dos.                       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### La Explicación Semántica

> "Y cuando vale de uno es el término que ya teníamos y cuando vale del otro es un tema semántico, la probabilidad de ser cero es uno menos la probabilidad de ser uno que es lo que estima mi función."

**En palabras simples:**
- Para x=1: Usamos directamente log P(X=1), que es lo que da el perceptrón
- Para x=0: Usamos log P(X=0) = log(1 - P(X=1)), que calculamos del perceptrón

---

## 15. Recapitulación: La Cadena Completa de Equivalencias

### La Pregunta sobre el Objetivo

> "Para todo este planteo... es para después... nosotros queremos minimizar el BCE... y lo que estamos haciendo es estamos minimizando la diferencia entre las dos distribuciones... y entre qué distribuciones... que nosotros estamos aproximando y la real."

### La Conexión con KL Divergence

> "Entonces minimizar ese BCE se reduce en sí... Cuando yo tiro para el BCE... al final del día minimizar el BCE en un perceptrón es un caso particular de minimizar la KL Divergence."

### ¿Por Qué Esto es Bueno?

> "Lo cual si me dice, 'Ah, pero ¿por qué estás minimizando el BCE en un perceptrón que esto es bueno?' ¿Porque esto me aprende la distribución real de los datos?"

Y responde:

> "Porque estimarla localmente punto a punto... En el contexto que estamos usando nosotros, que vamos a mostrar con una cadena de muestreos, es lo mismo que minimizar la KL de esa cadena de ese producto de distribuciones versus la distribución real de los datos."

### La Cadena Completa de Equivalencias

```
┌─────────────────────────────────────────────────────────────────────┐
│            LA CADENA COMPLETA: DE OBJETIVO A CÓDIGO                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   1. OBJETIVO INICIAL:                                               │
│      Queremos que P_θ ≈ P_data                                      │
│      (nuestro modelo se parezca a la realidad)                      │
│                              ↓                                       │
│   2. MEDIDA FORMAL:                                                  │
│      Minimizar KL(P_data || P_θ)                                    │
│                              ↓                                       │
│   3. SIMPLIFICACIÓN TEÓRICA:                                         │
│      = Minimizar -E[log P_θ(x)]                                     │
│                              ↓                                       │
│   4. APROXIMACIÓN EMPÍRICA:                                          │
│      ≈ Minimizar (1/N) Σₓ [-log P_θ(x)]                             │
│                              ↓                                       │
│   5. PARA MODELOS AUTORREGRESIVOS:                                   │
│      = Minimizar (1/N) Σₓ Σᵢ [-log P_θ(xᵢ | x<i)]                   │
│                              ↓                                       │
│   6. PARA PERCEPTRONES BINARIOS:                                     │
│      = Minimizar (1/N) Σₓ Σᵢ BCE(xᵢ, σᵢ)                            │
│                              ↓                                       │
│   7. EN CÓDIGO PYTORCH:                                              │
│      loss = nn.BCELoss()(predictions, targets)                      │
│                                                                      │
├─────────────────────────────────────────────────────────────────────┤
│   POR LO TANTO:                                                      │
│   Minimizar BCE en cada píxel = Aprender la distribución real       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Para Conectar con el Práctico

> "Y aparte tiene sentido para que puedan aunar lo que tiene práctico, que es bastante concreto con la teoría."

**Cuando en el práctico escribas:**

```python
loss = criterion(predictions, images)  # donde criterion = nn.BCELoss()
```

Estás implementando todo este razonamiento teórico.

---

## 16. Aplicación Práctica: Implementación en Python

### La Estructura de Datos

> "La Binary Cross Entropy de un vector, porque al final del día esto es un vector, la sumatoria de BCE de un vector... se puede hacer por broadcast en Python. Entonces es muy fácil."

**¿Qué es "broadcast"?**
Es una característica de NumPy/PyTorch donde las operaciones se aplican automáticamente elemento por elemento, sin necesidad de escribir bucles.

```python
import torch

# Datos reales (784 píxeles de una imagen)
y = torch.tensor([1, 0, 1, 0, 1, 0, ...])  # cada uno es 0 o 1

# Predicciones del perceptrón (784 probabilidades)
sigma = torch.tensor([0.9, 0.2, 0.85, 0.1, 0.95, 0.15, ...])

# BCE calculada para TODOS los píxeles a la vez (broadcast)
bce = -(y * torch.log(sigma) + (1-y) * torch.log(1-sigma))

# Resultado: tensor de 784 valores, uno por píxel
```

### Los Componentes Necesarios

> "Si yo tengo la estructura del fin de días, tengo n datos, los tenemos una estructura que tenga posicionalmente los bits de la imagen adecuados, los datos correctos... y un perceptrón que me exprese la relación entre bits predecesores y el bit futuro."

**Necesitas:**
1. **Datos de entrada**: Los píxeles anteriores (predecesores)
2. **Dato objetivo**: El píxel que quieres predecir
3. **Perceptrón**: Una red que toma predecesores y estima el píxel siguiente

### El Proceso de Entrenamiento

> "Yo puedo pasar esos bits predecesores por mi perceptrón, obtener una estimación del bit futuro, el bit futuro real, los meto en la BCE, los sumo todos, hago el step, hago el backward step y ajusto a 100 veces y estoy entrenando un módulo neural que me aproxima estas distribuciones."

```
┌─────────────────────────────────────────────────────────────────────┐
│                    UN PASO DE ENTRENAMIENTO                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   1. FORWARD PASS:                                                   │
│      imagen → perceptrón(W, B) → σ (784 probabilidades)             │
│                                                                      │
│   2. CALCULAR PÉRDIDA:                                               │
│      BCE(imagen_real, σ) → un número (la pérdida total)             │
│                                                                      │
│   3. BACKWARD PASS:                                                  │
│      loss.backward() → calcula ∂loss/∂W y ∂loss/∂B                  │
│                                                                      │
│   4. ACTUALIZAR PARÁMETROS:                                          │
│      W = W - lr × ∂loss/∂W                                          │
│      B = B - lr × ∂loss/∂B                                          │
│                                                                      │
│   5. REPETIR con la siguiente imagen del dataset                    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**En código:**

```python
for epoch in range(num_epochs):
    for images, _ in train_loader:  # ignoramos labels
        # 1. Forward pass
        predictions = model(images)

        # 2. Calcular pérdida
        loss = criterion(predictions, images)  # BCE

        # 3. Backward pass
        optimizer.zero_grad()
        loss.backward()

        # 4. Actualizar parámetros
        optimizer.step()
```

---

## 17. Cierre y Transición al Práctico

### Apertura de las Salas

> "Bueno, si no hay consultas, los dejo trabajar en los prácticos... Bueno, yo les creé las salas, están abiertas."

### Discusión sobre la Entrega

> "Una pregunta, ¿la entrega del práctico se había movido al final o no?"

> "Se movió, pero... no la movimos en aula todavía."

> "Dice que no se confíen que quede una semana no más."

---

## Conceptos Clave para Recordar

### 1. El Objetivo Fundamental

Encontrar parámetros θ* que minimicen la diferencia entre nuestra distribución estimada P_θ y la distribución real P_data.

### 2. La KL Divergence

Es una medida de qué tan diferentes son dos distribuciones. Minimizarla hace que nuestro modelo se parezca a los datos reales.

### 3. Empirical Risk Minimization

Como no tenemos acceso a la distribución real completa, minimizamos sobre nuestros datos de entrenamiento (el promedio reemplaza la esperanza).

### 4. Modelos Autorregresivos

Descomponen la probabilidad conjunta P(x₁, x₂, ..., xₙ) en un producto de probabilidades condicionales usando la regla de la cadena.

### 5. El Truco del Logaritmo

Convertir productos en sumas mejora la estabilidad numérica:
- Evita underflow (números demasiado pequeños)
- Reduce el error acumulado

### 6. El Problema del Perceptrón

Un perceptrón binario solo da P(X=1), no P(X=valor_real) para cualquier valor.

### 7. Binary Cross-Entropy (BCE)

Es la solución que "adapta" el perceptrón para que funcione con valores binarios. Actúa como un selector:
- Si dato = 1: usa log P(X=1)
- Si dato = 0: usa log(1 - P(X=1)) = log P(X=0)

### 8. La Cadena Completa

Minimizar BCE en cada perceptrón = Minimizar la suma de -log condicionales = Minimizar KL Divergence = Aprender la distribución real.

---

## Terminología Técnica

| Término | Significado |
|---------|-------------|
| **θ (theta)** | Los parámetros (W y B) del modelo |
| **θ* (theta estrella)** | Los parámetros óptimos |
| **P_data** | La distribución real de los datos |
| **P_θ** | Nuestra estimación de esa distribución |
| **KL Divergence** | Medida de diferencia entre distribuciones |
| **L (Loss)** | Pérdida en un dato individual |
| **J (Cost)** | Costo total (promedio de L) |
| **E[...]** | Esperanza o valor esperado |
| **Empirical Risk** | Riesgo calculado sobre datos de entrenamiento |
| **BCE** | Binary Cross-Entropy |
| **σ (sigma)** | Salida del perceptrón (probabilidad estimada) |
| **Forward pass** | Calcular predicciones |
| **Backward pass** | Calcular gradientes |
| **Broadcast** | Operación vectorizada en Python |

---

## Resumen Ultra-Simplificado

### Para Alguien Completamente Nuevo

Imagina que quieres enseñarle a una computadora a generar imágenes de números.

**El problema:**
El perceptrón te dice "hay 70% de probabilidad de que este píxel sea blanco". Pero a veces el píxel real es negro. ¿Cómo le dices "te equivocaste"?

**La solución (BCE):**
Binary Cross-Entropy es como un interruptor inteligente:
- Si el píxel real es **blanco** → mira qué tan bien predijiste "blanco"
- Si el píxel real es **negro** → mira qué tan bien predijiste "negro"

**El entrenamiento:**
```
1. El modelo predice (forward)
2. BCE calcula qué tan mal está (pérdida)
3. PyTorch calcula cómo mejorar (backward)
4. Ajustas los pesos (update)
5. Repites miles de veces
```

**Por qué funciona:**
Toda la teoría matemática (KL Divergence, etc.) garantiza que si minimizas BCE en cada píxel, estás aprendiendo cómo se distribuyen los números reales.

---

## Lo Que NO Necesitas Memorizar

### Sobre las Fórmulas

El profesor fue claro: **No es necesario memorizar todas las derivaciones matemáticas.**

> "Esto llevó un pizarrón entero" para la derivación de KL, pero no espera que la reproduzcas.

### Lo Que SÍ es Importante

1. **Entender los conceptos**: Qué es una distribución, qué es optimización, por qué minimizamos algo
2. **Poder aplicarlos en código**: El práctico te ayuda a familiarizarte
3. **Conectar teoría con práctica**: Entender que tu código implementa estos conceptos
4. **Saber el flujo lógico**: De KL Divergence → Empirical Risk → BCE → Código

### Lo Que NO es Necesario

1. Derivar todas las fórmulas desde cero
2. Memorizar la expresión exacta de cada término
3. Hacer demostraciones matemáticas formales
4. Recordar cada detalle notacional

---

## Reflexión Final

Esta clase es el **puente crítico** entre teoría abstracta e implementación práctica.

El profesor te mostró cómo:
1. Un concepto matemático elegante (KL Divergence)
2. Se traduce en una expresión optimizable (-log P)
3. Se adapta a modelos autorregresivos (suma de log condicionales)
4. Se implementa con perceptrones específicos (usando BCE)
5. Se programa en Python (con operaciones vectorizadas)

**Cada paso tiene su justificación teórica**, pero al final del día, lo importante es que funciona: puedes entrenar modelos que aprenden a generar datos realistas.

Como dijo el profesor: tienen que poder "aunar lo que tiene práctico, que es bastante concreto, con la teoría". La teoría sin práctica es abstracta; la práctica sin teoría es recetas sin entendimiento. **Juntas, te dan comprensión profunda.**

---

## Definiciones para el Parcial

### Optimización y Parámetros

**θ (theta):** Notación para el conjunto de todos los parámetros del modelo (W y B); lo que ajustamos durante el entrenamiento.

**θ* (theta estrella):** El mejor conjunto de parámetros posible; el óptimo que buscamos; θ* = argmin_θ J(θ).

**Función de Pérdida:** Medida matemática de qué tan bien o mal funcionan los parámetros actuales; queremos minimizarla.

### Funciones de Costo

**L (Loss):** Pérdida para un dato individual; "a cuánto le erro cuando le erro en un dato"; ejemplo: error en predecir una imagen específica.

**J (Cost):** Costo total, es el promedio de todas las pérdidas individuales; J = E[L] = (1/N) × Σ L(xᵢ); es lo que realmente minimizamos.

### KL Divergence

**P_data:** La distribución real de los datos; cómo realmente se distribuyen los números escritos a mano en el mundo; es desconocida.

**P_θ:** Nuestro modelo paramétrico; lo que el perceptrón estima sobre cómo se distribuyen los datos.

**KL Divergence:** Mide qué tan diferentes son P_data y P_θ; si KL es pequeño el modelo es bueno; si KL es grande el modelo está muy equivocado; es derivable, lo que permite optimizar.

**Propiedad de KL:** KL ≥ 0 siempre; KL = 0 solo si P_data = P_θ (distribuciones idénticas).

### Empirical Risk Minimization

**Esperanza E[...]:** Promedio teórico sobre todos los posibles datos; es inaccesible porque no conocemos la distribución real completa.

**Empirical Risk Minimization:** En lugar de la esperanza teórica, usamos el promedio sobre nuestros datos de entrenamiento; E[L] ≈ (1/N) × Σ L(xᵢ).

**"Empírico":** Basado en observaciones reales (datos de entrenamiento), no en teoría perfecta.

### Modelos Autorregresivos

**Modelo Agnóstico:** La teoría de minimizar KL aplica a cualquier modelo (autorregresivos, GANs, VAEs, difusión) siempre que estime probabilidades y sea derivable.

**Regla de la Cadena:** P(x₁,...,xₙ) = P(x₁) × P(x₂|x₁) × ... × P(xₙ|x₁,...,xₙ₋₁); descompone la conjunta en producto de condicionales.

**Variable Aleatoria (Xᵢ mayúscula):** El i-ésimo píxel como concepto; puede tomar diferentes valores (0 o 1).

**Valor Concreto (xᵢ minúscula):** El valor específico que tiene el píxel i en una imagen particular; por ejemplo xᵢ = 1.

### Estabilidad Numérica

**Underflow:** Problema cuando multiplicamos muchas probabilidades pequeñas; el resultado es tan pequeño que se redondea a 0.

**Truco del Logaritmo:** log(A × B × C) = log(A) + log(B) + log(C); convierte productos en sumas para evitar underflow y reducir error acumulado.

### El Problema del Perceptrón

**Limitación del Perceptrón:** Solo da P(X=1|predecesores), pero necesitamos P(X=valor_real|predecesores) donde valor_real puede ser 0 o 1.

**Por qué es problema:** Si el dato real es 0, el perceptrón no nos da directamente la probabilidad de 0; solo estima "hacia un lado".

### Binary Cross-Entropy

**BCE como Selector:** La fórmula BCE = -[xᵢ × log(σᵢ) + (1-xᵢ) × log(1-σᵢ)] actúa como un switch; cuando xᵢ=1 usa log(σᵢ), cuando xᵢ=0 usa log(1-σᵢ).

**σ (sigma):** Salida del perceptrón; la probabilidad estimada P_θ(X=1|predecesores).

**Niveles de Costo:** BCE local (un píxel) → L (una imagen = suma de BCEs) → J (todo el dataset = promedio de Ls).

### Implementación

**Broadcast:** Característica de NumPy/PyTorch donde las operaciones se aplican elemento por elemento sin escribir bucles.

**Forward Pass:** Calcular predicciones: imagen → perceptrón → 784 probabilidades → BCE → pérdida.

**Backward Pass:** Calcular gradientes: loss.backward() → obtener ∂loss/∂W y ∂loss/∂B automáticamente.

### La Cadena Completa de Equivalencias

```
Objetivo: P_θ ≈ P_data
    ↓
Minimizar KL(P_data || P_θ)
    ↓
Minimizar -E[log P_θ(x)]
    ↓
Minimizar (1/N) Σ [-log P_θ(x)]  (Empirical Risk)
    ↓
Minimizar (1/N) Σₓ Σᵢ [-log P_θ(xᵢ|x<i)]  (Autorregresivo)
    ↓
Minimizar (1/N) Σₓ Σᵢ BCE(xᵢ, σᵢ)  (Perceptrón binario)
    ↓
loss = nn.BCELoss()(predictions, targets)  (PyTorch)
```

**Conclusión:** Minimizar BCE en cada píxel = Aprender la distribución real de los datos.
