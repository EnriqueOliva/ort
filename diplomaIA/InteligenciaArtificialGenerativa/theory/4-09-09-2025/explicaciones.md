# Explicación de Temas - Clase del 09-09-2025

## La Gran Pregunta: ¿Qué Estamos Construyendo?

Esta clase es donde **todo empieza a funcionar de verdad**. La clase anterior (clase 3) fue teoría: distribuciones, probabilidades, la idea de que los perceptrones estiman parámetros. Hoy vamos a:

1. Terminar de entender el modelo de Hinton (el primer modelo generativo)
2. Aprender **cómo entrenar** estos modelos (la función de pérdida)
3. Empezar a **programar** un generador de imágenes

Como dijo el profesor: "Los modelos autorregresivos son los primeros modelos generativos que vamos a discutir en el curso". Es decir, esto es **el primer modelo real** que genera cosas.

---

## Conexión con la Clase Anterior

### ¿Qué Vimos la Clase Pasada?

En la clase 3 establecimos las bases:
- Las distribuciones continuas (gaussianas)
- Las mixturas de gaussianas (el ejemplo del gato)
- La idea de que un perceptrón puede estimar parámetros de distribuciones
- La regla del producto para descomponer probabilidades conjuntas

### ¿Por Qué Importa Ahora?

Porque la regla del producto es **la base matemática** de los modelos autorregresivos:

**P(X₁, X₂, ..., Xₙ) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂) × ... × P(Xₙ|X₁,...,Xₙ₋₁)**

Esta fórmula dice: "La probabilidad de todos los píxeles de una imagen es igual al producto de las probabilidades condicionales de cada píxel dado los anteriores".

Esto conecta directamente con lo que vimos sobre P(X|Y) en la clase anterior. Ahora lo aplicamos a imágenes.

---

## Los Modelos Autorregresivos: La Idea Central

### ¿Qué Significa "Autorregresivo"?

**Auto** = a sí mismo, **regresivo** = que vuelve hacia atrás.

Un modelo autorregresivo es uno donde **cada predicción depende de las predicciones anteriores**. El modelo se "alimenta" de sus propias salidas para generar la siguiente.

### La Idea Más Simple Posible

Imagina que estás escribiendo una oración palabra por palabra:

```
"El gato ___"
```

¿Qué palabra sigue? Probablemente "negro", "duerme", "come"... pero NO "el" o "muy".

**La palabra que elijas depende de las palabras anteriores.** Eso es autorregresivo.

Ahora imagina que haces lo mismo pero con **píxeles de una imagen**:

```
Píxel 1: negro
Píxel 2: negro
Píxel 3: ¿? → Probablemente negro (si los anteriores son negros)
```

### Ejemplo Visual: Generando un "1"

Si estás generando la imagen de un "1":

```
Paso 1: Los primeros píxeles (esquina superior) → probablemente negros
Paso 2: Píxeles del medio-arriba → empiezan a ser blancos (la línea del 1)
Paso 3: Píxeles del centro → blancos (el trazo vertical)
Paso 4: Píxeles del final → negros otra vez
```

Cada píxel "sabe" lo que vino antes y decide en consecuencia.

### El Ejemplo Perfecto: ChatGPT

El profesor lo mencionó explícitamente:

> "GPT, ¿cómo nos genera texto? Bueno, nos genera haciendo este tipo de muestreos, condicionando una palabra respecto a las anteriores."

Cuando ChatGPT responde:
1. Genera la primera palabra
2. Usa esa palabra para decidir la segunda
3. Usa las dos primeras para decidir la tercera
4. Y así sucesivamente...

Es **exactamente** lo que vamos a hacer con píxeles de imágenes.

### ¿Por Qué Se Llama "Autorregresivo"?

- **Regresión** en estadística = predecir un valor basándote en otros
- **Auto** = te basas en tus propias predicciones anteriores

Es como una cadena: cada eslabón depende del anterior.

### El Orden es Arbitrario (para imágenes)

Para texto, el orden es natural: las palabras van una después de otra.

Para imágenes, el profesor aclaró algo importante:

> "Para el caso de las imágenes no tiene mucho sentido el concepto de orden porque estamos eligiendo los píxeles totalmente arbitrariamente."

Podríamos procesar los píxeles de arriba a abajo, de izquierda a derecha, en espiral... No importa. Lo que importa es que **una vez elegido el orden, lo mantenemos**.

---

## El Modelo de Hinton: La Primera Implementación

### El Contexto Histórico

Geoffrey Hinton (premio Nobel de Física 2024) propuso una manera de implementar modelos autorregresivos con redes neuronales. Este es el modelo que vamos a programar en el práctico.

### El Problema que Resuelve

Queremos generar imágenes del dataset MNIST: números escritos a mano de 28×28 píxeles.

Eso significa 784 píxeles. Cada uno puede ser 0 (negro) o 1 (blanco).

### La Hipótesis del Modelo

**Cada píxel es una variable aleatoria de Bernoulli**.

---

### ¿Qué es una Distribución de Bernoulli?

Es la distribución de probabilidad más simple que existe. Modela algo que **solo puede tener dos resultados**:

- Cara o cruz
- Sí o no
- Encendido o apagado
- **Blanco (1) o negro (0)** ← nuestro caso

#### El Parámetro α

Una Bernoulli tiene **un solo parámetro**: α (alpha), que es un número entre 0 y 1.

α = la probabilidad de obtener "1" (éxito, cara, blanco, etc.)

**Ejemplos:**

| α | Significado | Ejemplo |
|---|-------------|---------|
| α = 0.5 | 50% chance de 1, 50% chance de 0 | Moneda justa |
| α = 0.8 | 80% chance de 1, 20% chance de 0 | Moneda trucada hacia cara |
| α = 0.1 | 10% chance de 1, 90% chance de 0 | Casi siempre sale cruz |
| α = 1.0 | 100% chance de 1 | Siempre sale cara |
| α = 0.0 | 0% chance de 1 | Siempre sale cruz |

#### ¿Cómo se "Muestrea" de una Bernoulli?

Muestrear = obtener un valor aleatorio siguiendo la distribución.

```python
import random

alpha = 0.7  # 70% de probabilidad de obtener 1

# Muestrear:
if random.random() < alpha:
    resultado = 1
else:
    resultado = 0
```

Si corres esto muchas veces con α=0.7, obtendrás aproximadamente 70% de unos y 30% de ceros.

#### ¿Por Qué Bernoulli para Píxeles?

Nuestras imágenes están **binarizadas**: cada píxel es 0 (negro) o 1 (blanco).

```
Imagen original (escala de grises):
[0.1, 0.9, 0.5, 0.8, ...]

Imagen binarizada:
[0, 1, 1, 1, ...]  ← Solo 0s y 1s
```

Como cada píxel solo puede ser 0 o 1, modelamos cada píxel como una Bernoulli.

**El trabajo del modelo es estimar α para cada píxel.** Si el modelo dice α=0.9 para el píxel 5, significa "hay 90% de probabilidad de que el píxel 5 sea blanco".

---

#### Aplicando Bernoulli a Nuestro Problema

- Si α = 0.8 → 80% de chance de que el píxel sea blanco (1)
- Si α = 0.2 → 20% de chance de que el píxel sea blanco (1)

### ¿Por Qué No Usar Tablas?

El profesor recordó el enfoque frecuentista: contar cuántas veces ocurre cada combinación.

**El problema**: las tablas explotan exponencialmente.

- Primer píxel: 1 parámetro (α₁)
- Segundo píxel dado el primero: 2 parámetros (uno para X₁=0, otro para X₁=1)
- Tercer píxel dados los dos anteriores: 4 parámetros
- Píxel n: **2^(n-1) parámetros**

Para 784 píxeles, necesitarías 2^783 parámetros. **Imposible**.

### La Solución: Perceptrones

En lugar de tablas, usamos un perceptrón para estimar cada α:

**αᵢ = sigmoid(X_{<i} × Wᵢ + Bᵢ)**

¿Qué significa esto?
- **αᵢ**: El parámetro que queremos estimar para el píxel i
- **X_{<i}**: Todos los píxeles anteriores al píxel i (un vector)
- **Wᵢ**: Los pesos del perceptrón (lo que vamos a aprender)
- **Bᵢ**: El bias (término independiente)
- **sigmoid**: Convierte cualquier número en un valor entre 0 y 1

### ¿Por Qué Redes Neuronales?

El profesor fue muy claro:

> "Esta materia es de modelos de aproximación. Donde podamos meter redes neuronales lo vamos a hacer porque es lo que el área está haciendo y porque es donde hay más impacto."

Las redes neuronales son **aproximadores universales**: pueden aprender a estimar cualquier función si tienen suficiente capacidad.

### Entender el "Tipo" de la Función

El profesor insistió en algo importante para cuando no entiendas algo:

> "Cuando yo no estoy entendiendo algo, marco el tipo de la función y eso por lo menos me da una idea de que entiendo las entradas y salidas."

Para nuestro perceptrón:
- **Entrada**: Valores que pueden ser 0 o 1 (los píxeles anteriores)
- **Salida**: Un valor entre 0 y 1 (la probabilidad del siguiente píxel)

Si entiendes las entradas y salidas, entiendes el 80% del problema.

---

## La Matriz Triangular: El Truco Técnico Clave

### El Problema del "Ver el Futuro"

Durante el entrenamiento, tenemos la imagen completa. Pero queremos que cada perceptrón **solo use información de los píxeles anteriores**.

Si el perceptrón del píxel 5 pudiera "ver" el píxel 6, estaría haciendo trampa.

### La Solución: Una Máscara

Usamos una **matriz triangular inferior** donde la parte superior son ceros:

```
W = [0    0    0    0  ]   ← Primer perceptrón: no ve nada (solo bias)
    [W₂₁  0    0    0  ]   ← Segundo: solo ve el píxel 1
    [W₃₁  W₃₂  0    0  ]   ← Tercero: ve píxeles 1 y 2
    [W₄₁  W₄₂  W₄₃  0  ]   ← Cuarto: ve píxeles 1, 2 y 3
```

Los ceros **no se entrenan**. Como dijo el profesor:

> "Toda esta parte de arriba no le vamos a hacer descenso del gradiente. Esos pesos simplemente permanecen en cero."

### ¿Por Qué Diagonal = -1?

En el práctico usan `torch.tril(diagonal=-1)`. El -1 significa que la diagonal principal también es cero.

¿Por qué? Porque el píxel i no debe depender de sí mismo, solo de los **anteriores** (0 a i-1).

### Lo Brillante de Esta Estructura

Con esta matriz, puedes pasar **toda la imagen a la vez** durante el entrenamiento:

1. Multiplicas la imagen aplanada por la matriz W
2. Sumas el vector de biases B
3. Aplicas la sigmoide
4. Obtienes 784 probabilidades

Todo en paralelo. Pero cada probabilidad solo "ve" los píxeles anteriores gracias a los ceros.

---

## El Modelo de Bengio: Más Capas, Más Poder

### La Limitación de Hinton

El modelo de Hinton usa una sola capa. Los hermanos Bengio (Sami y Joshua) preguntaron:

> "¿Por qué tener un perceptrón de una capa? ¿Por qué no ponerle dos capas?"

### Primero: ¿Qué Hace el Modelo de Hinton?

Recuerda que el modelo de Hinton necesita estimar α (la probabilidad de que un píxel sea blanco). Para hacer esto:

1. Toma los píxeles anteriores como entrada
2. Los multiplica por pesos (W)
3. Suma un bias (B)
4. Aplica sigmoide para obtener un número entre 0 y 1

**Es una transformación directa: entrada → salida, sin pasos intermedios.**

Visualmente:

```
[Píxel 1, Píxel 2, Píxel 3] → × W + B → sigmoide → α = 0.7
```

### El Problema: Relaciones Simples

Un perceptrón de una sola capa solo puede aprender **relaciones lineales** (o casi lineales después de la sigmoide).

**¿Qué significa "relación lineal"?**

Imagina que quieres predecir si el píxel 10 será blanco. Con Hinton, básicamente dices:

"α₁₀ = algo × píxel₁ + algo × píxel₂ + ... + algo × píxel₉"

Es como una suma ponderada. Si el píxel 1 está prendido, suma un poco. Si el píxel 5 está prendido, suma otro poco. Y listo.

**Pero las imágenes reales tienen relaciones más complicadas.** Por ejemplo:
- "Si el píxel 1 Y el píxel 5 están prendidos JUNTOS, entonces el píxel 10 probablemente está apagado"
- "Si hay una diagonal de píxeles prendidos, el siguiente sigue la diagonal"

Estas relaciones **no son simples sumas**. Son combinaciones complejas.

### La Solución de Bengio: Capas Ocultas

En lugar de ir directamente de los píxeles al parámetro α:

```
Píxeles anteriores → α (Hinton - UNA transformación)
```

Pasamos por capas intermedias:

```
Píxeles anteriores → Capa oculta 1 → Capa oculta 2 → α (Bengio - VARIAS transformaciones)
```

### ¿Qué es una "Capa Oculta"?

Una capa oculta es simplemente **otra transformación intermedia**. En lugar de ir directo de entrada a salida, pasamos por un "punto intermedio".

**Analogía de la Cocina:**

- **Hinton (sin capa oculta):** Ingredientes crudos → Plato final
- **Bengio (con capas ocultas):** Ingredientes → Preparación intermedia → Cocción → Plato final

Con pasos intermedios, puedes hacer platos más elaborados.

**Ejemplo Concreto:**

Imagina que tienes 9 píxeles de entrada y quieres predecir el píxel 10.

**Hinton (1 capa):**
```
[p1, p2, p3, p4, p5, p6, p7, p8, p9]
    ↓ (multiplica por 9 pesos, suma bias, sigmoide)
    α₁₀ = 0.7
```

**Bengio (3 capas):**
```
[p1, p2, p3, p4, p5, p6, p7, p8, p9]  ← 9 valores de entrada
    ↓ (primera transformación)
[h1, h2, h3, h4, h5]                   ← 5 valores "ocultos" (capa oculta 1)
    ↓ (segunda transformación)
[h1', h2', h3']                        ← 3 valores "ocultos" (capa oculta 2)
    ↓ (tercera transformación)
    α₁₀ = 0.7                          ← 1 valor de salida
```

Los valores "h" son las **activaciones de las capas ocultas**. No los ves directamente, por eso se llaman "ocultas".

### ¿Por Qué Múltiples Capas Funcionan Mejor?

**1. Detectan patrones simples primero, luego los combinan:**

- **Capa 1:** Podría detectar "¿hay una línea horizontal arriba?"
- **Capa 2:** Podría detectar "¿hay una línea horizontal Y una vertical?" (usando la salida de capa 1)
- **Salida:** Combina todo para decidir el siguiente píxel

**2. Más parámetros = más flexibilidad:**

Con más capas tienes más pesos (W) que ajustar. Esto permite "moldear" mejor la función que estimas.

**3. El Teorema de Aproximación Universal:**

Se ha demostrado matemáticamente que una red con suficientes capas ocultas puede aproximar **cualquier función**. Una sola capa no puede hacer esto.

### La Analogía del Profesor: La Tostadora

El profesor lo explicó así:

> "Yo podría tener una tostadora, no me importa. Mientras sea una máquina que le entran todos los valores hasta el momento y me da una buena estimación del parámetro, yo podría tener un árbol de decisión, una red más compleja... siempre que a la salida tenga algo entre 0 y 1."

**¿Qué quiso decir?**

No importa QUÉ hay adentro de la "caja negra". Lo único que importa es:
- **Entrada:** Los píxeles anteriores (valores 0 o 1)
- **Salida:** Un número entre 0 y 1 (la probabilidad α)

Podría ser:
- Un perceptrón simple (Hinton)
- Una red profunda (Bengio)
- Un árbol de decisión
- ¡Hasta una tostadora mágica!

Siempre que cumpla: "entran píxeles, sale una probabilidad", funciona para nuestro modelo autorregresivo.

**Pero** las redes profundas son mejores porque pueden aprender funciones más complicadas.

### La Clave Técnica: Solo la Última Capa Tiene Sigmoide

Este es un detalle importante de implementación:

**Capas ocultas:** Usan ReLU (u otra activación no-limitada)
```
ReLU(x) = max(0, x)   → puede dar cualquier número positivo
```

**Última capa:** Usa sigmoide
```
sigmoide(x) = 1/(1+e^(-x))   → siempre da un número entre 0 y 1
```

**¿Por qué?**

- Las capas intermedias necesitan **flexibilidad**. Si limitaras todo a 0-1, perderías información.
- Solo la **salida final** necesita estar entre 0 y 1 (porque es una probabilidad).

**Ejemplo:**

```
Entrada: [1, 0, 1, 1, 0]

Capa oculta 1 (con ReLU):
    [0.5, 2.3, 0, 1.8]    ← valores libres, pueden ser grandes

Capa oculta 2 (con ReLU):
    [3.1, 0, 0.7]         ← valores libres

Capa de salida (con sigmoide):
    [0.73]                ← AHORA SÍ está entre 0 y 1
```

### Resumen Visual: Hinton vs Bengio

```
HINTON (1 capa):
┌─────────────┐         ┌──────────┐
│  Píxeles    │ ──W,B──→│ Sigmoide │──→ α
│ anteriores  │         └──────────┘
└─────────────┘

BENGIO (múltiples capas):
┌─────────────┐      ┌──────┐      ┌──────┐      ┌──────────┐
│  Píxeles    │─W₁,B₁→│ ReLU │─W₂,B₂→│ ReLU │─W₃,B₃→│ Sigmoide │──→ α
│ anteriores  │      └──────┘      └──────┘      └──────────┘
└─────────────┘       Capa 1        Capa 2         Salida
                      oculta        oculta
```

### ¿Por Qué Esto Importa para el Curso?

El modelo de Bengio es una **extensión natural** del de Hinton. Muestra que:

1. La idea autorregresiva (generar píxel por píxel) es flexible
2. Puedes meter arquitecturas más complejas "adentro" sin cambiar la idea general
3. **Más capas = mejores resultados** (hasta cierto punto)

Esto conecta directamente con Deep Learning: las redes profundas que ves en otras materias son exactamente esto aplicado a otros problemas.

---

## La Función de Pérdida: La Cadena Lógica Completa

Esta es la parte más importante de entender. **La función de pérdida no es arbitraria.** Viene de una cadena lógica que conecta "lo que queremos" con "lo que programamos".

```
Lo que queremos (que el modelo genere imágenes realistas)
      ↓
Formulación matemática (KL Divergence)
      ↓
Simplificación (Negative Log-Likelihood)
      ↓
Aplicación a modelos autorregresivos (suma de logs)
      ↓
Aplicación a variables binarias (Binary Cross-Entropy)
      ↓
Código en PyTorch (nn.BCELoss)
```

Vamos paso a paso.

---

## Paso 1: ¿Qué Queremos Lograr?

Tenemos:
- **P_data**: La distribución "real" de las imágenes (los datos de MNIST)
- **P_θ**: La distribución que nuestro modelo estima (θ son los parámetros W y B)

**Queremos que P_θ se parezca lo más posible a P_data.**

Si lo logramos, cuando muestreemos de P_θ, obtendremos imágenes que parecen reales.

---

## Paso 2: ¿Cómo Medir "Parecido" Entre Distribuciones?

Necesitamos un número que diga: "¿qué tan diferentes son P_data y P_θ?"

Usamos la **divergencia de Kullback-Leibler (KL)**:

```
KL(P_data || P_θ) = Σ P_data(x) × log(P_data(x) / P_θ(x))
```

En español: "Cuánto se equivoca el modelo P_θ cuando la realidad es P_data".

### Propiedades de la KL

El profesor demostró en el pizarrón que:

1. **KL ≥ 0**: Siempre es positiva o cero
2. **KL = 0 solo si P_data = P_θ**: Distribuciones idénticas
3. **No es simétrica**: KL(P||Q) ≠ KL(Q||P)

**Conclusión:** Minimizar KL = Hacer que P_θ se parezca a P_data.

---

## Paso 3: Simplificando la KL → Negative Log-Likelihood

Expandamos la KL:

```
KL(P_data || P_θ) = Σ P_data(x) × log(P_data(x)) - Σ P_data(x) × log(P_θ(x))
                    \_________________________/   \__________________________/
                           Parte A                         Parte B
```

**Parte A:** Solo depende de P_data (los datos reales). **No podemos cambiarla.**

**Parte B:** Depende de P_θ (nuestro modelo). **Esta sí podemos cambiarla.**

Como dijo el profesor:

> "La parte de la izquierda no se ve afectada por θ. ¿Qué significa eso? Que la mandamos a volar."

Entonces minimizar KL es equivalente a minimizar:

```
-Σ P_data(x) × log(P_θ(x))
```

Esto se llama **Negative Log-Likelihood (NLL)**.

**En español:** Queremos que nuestro modelo asigne **alta probabilidad** a los datos reales.

---

## Paso 4: De Esperanza a Promedio

No conocemos P_data exactamente. Solo tenemos un dataset finito de T imágenes.

Aproximamos la esperanza con un promedio:

```
NLL ≈ -(1/T) × Σ log P_θ(x)    para cada x en el dataset
```

Esto se llama **Empirical Risk Minimization**: minimizar el error empírico porque no tenemos acceso al error real.

---

## Paso 5: Aplicando a Modelos Autorregresivos

### El Problema: Multiplicar Muchos Números Pequeños

La probabilidad de una imagen es:

```
P_θ(imagen) = P(píxel₁) × P(píxel₂|píxel₁) × P(píxel₃|píxel₁,píxel₂) × ...
```

Esto son **784 multiplicaciones** de números entre 0 y 1.

**Ejemplo:**
```
0.8 × 0.7 × 0.6 × 0.9 × 0.5 × ... (784 veces) = 0.0000000000000000000001
```

**Problema:** Las computadoras no pueden manejar números tan pequeños (*underflow*).

### La Solución: Logaritmos

```
log(a × b × c) = log(a) + log(b) + log(c)
```

**El logaritmo convierte multiplicaciones en sumas.**

Entonces:
```
log P_θ(imagen) = log P(píxel₁) + log P(píxel₂|píxel₁) + log P(píxel₃|...) + ...
```

Las sumas no causan *underflow*.

### La Función de Pérdida para Autorregresivos

```
J(θ) = -(1/T) × Σ_{imágenes} Σ_{píxeles} log P(píxel_i | píxeles anteriores)
```

**Traducción:**
1. Para cada imagen del dataset...
2. Calcula log(probabilidad) de cada píxel dado los anteriores
3. Súmalos todos
4. Promedia sobre todas las imágenes
5. Ponle signo negativo

**Mientras más bajo sea J(θ), mejor es el modelo.**

---

## Paso 6: ¿Qué es P(píxel_i | anteriores)?

Aquí es donde entra **el modelo específico que elegimos**.

Dijimos que cada píxel es una **variable Bernoulli** (solo puede ser 0 o 1).

Una Bernoulli tiene un parámetro α (probabilidad de ser 1):

```
P(píxel = 1) = α
P(píxel = 0) = 1 - α
```

Nuestro modelo (el perceptrón/MLP) **estima α** para cada píxel:

```
α_i = sigmoid(función de los píxeles anteriores)
```

### El Log-Likelihood de una Bernoulli

Si el píxel real es `y` (0 o 1) y nuestro modelo predice `α`:

```
P(y | α) = α^y × (1-α)^(1-y)
```

¿Por qué funciona? Veamos los dos casos:
- Si y=1: P = α¹ × (1-α)⁰ = α ✓
- Si y=0: P = α⁰ × (1-α)¹ = 1-α ✓

Tomando logaritmo:

```
log P(y | α) = y × log(α) + (1-y) × log(1-α)
```

---

## Paso 7: Llegamos a Binary Cross-Entropy

El NLL para un píxel es:

```
-log P(y | α) = -[y × log(α) + (1-y) × log(1-α)]
```

**¡Esto es exactamente la fórmula de Binary Cross-Entropy!**

```
BCE = -[y × log(ŷ) + (1-y) × log(1-ŷ)]
```

Donde:
- `y` = valor real del píxel (0 o 1)
- `ŷ` = lo que predice el modelo (entre 0 y 1)

### ¿Por Qué Funciona Esta Fórmula?

**Caso 1: El píxel real es 1 (y=1)**
```
BCE = -[1 × log(ŷ) + 0 × log(1-ŷ)] = -log(ŷ)
```
Queremos que ŷ → 1. Si ŷ=0.9, BCE ≈ 0.1 (bajo = bien).

**Caso 2: El píxel real es 0 (y=0)**
```
BCE = -[0 × log(ŷ) + 1 × log(1-ŷ)] = -log(1-ŷ)
```
Queremos que ŷ → 0. Si ŷ=0.1, BCE ≈ 0.1 (bajo = bien).

**Tabla resumen:**

| Píxel real | Modelo predice | BCE | ¿Está bien? |
|------------|----------------|-----|-------------|
| 1 | 0.95 | 0.05 | ✓ Bajo = bien |
| 1 | 0.10 | 2.30 | ✗ Alto = mal |
| 0 | 0.05 | 0.05 | ✓ Bajo = bien |
| 0 | 0.90 | 2.30 | ✗ Alto = mal |

Como explicó el profesor:

> "Si nosotros tenemos un píxel 0, no vamos a querer comparar con nuestra salida que apunta a que era 1. Entonces queremos 'flippearlo' y eso es lo que nos da la binary cross-entropy."

---

## Resumen: La Cadena Completa

```
┌─────────────────────────────────────────────────────────────┐
│  QUEREMOS: Que P_θ se parezca a P_data                      │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  MEDIMOS CON: KL Divergence (distancia entre distribuciones)│
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  SIMPLIFICAMOS A: Negative Log-Likelihood                   │
│  (porque parte de KL no depende del modelo)                 │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  PARA AUTORREGRESIVO: Suma de log P(cada píxel | anteriores)│
│  (usamos log para evitar underflow)                         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  PARA BERNOULLI: -[y×log(ŷ) + (1-y)×log(1-ŷ)]              │
│  = Binary Cross-Entropy                                      │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  EN CÓDIGO: nn.BCELoss() o F.binary_cross_entropy()         │
└─────────────────────────────────────────────────────────────┘
```

---

## ¿Y Otras Funciones de Pérdida?

**BCE no es una fórmula mágica.** Es la consecuencia de:
1. Querer que el modelo se parezca a los datos reales (KL)
2. Asumir que los píxeles son Bernoulli (0 o 1)

**Cada función de pérdida corresponde a una suposición diferente:**

| Función de Pérdida | Suposición sobre los datos | Cuándo usarla |
|-------------------|---------------------------|---------------|
| **BCE** | Bernoulli (0 o 1) | Píxeles binarios, clasificación binaria |
| **Cross-Entropy** | Categórico (una de N clases) | Clasificación: ¿es un 0, 1, 2...9? |
| **MSE** | Gaussiano (número continuo) | Imágenes escala de grises, regresión |

### ¿Por qué MSE para Gaussianas?

Si asumimos que los datos son Gaussianos:

```
P(y | μ, σ) = (1/√(2πσ²)) × exp(-(y-μ)²/(2σ²))
```

Tomando -log:

```
-log P = constante + (y-μ)²/(2σ²)
```

Si σ es fijo, minimizar esto es minimizar **(y-μ)²** = **Mean Squared Error**.

### En Código

```python
# Píxeles binarios (0 o 1) → Bernoulli → BCE
criterion = nn.BCELoss()

# Píxeles continuos (0.0 a 1.0) → Gaussiano → MSE
criterion = nn.MSELoss()

# Clasificación (¿qué dígito es?) → Categórico → CrossEntropy
criterion = nn.CrossEntropyLoss()
```

**Si eliges la función equivocada, el modelo aprenderá mal** porque estás haciendo suposiciones incorrectas sobre los datos.

---

## El Modelo Completo: De Entrada a Pérdida

Antes de hablar de derivadas, veamos **el modelo completo** que construimos en esta clase:

### El Flujo Completo (Forward Pass)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           EL MODELO COMPLETO                                 │
└─────────────────────────────────────────────────────────────────────────────┘

ENTRADA: Imagen de 784 píxeles (cada uno es 0 o 1)
   │
   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ PASO 1: Multiplicación de Matrices                                          │
│                                                                              │
│   z = X × W^T + B                                                           │
│                                                                              │
│   - X: los 784 píxeles de entrada (vector)                                  │
│   - W: matriz de pesos 784×784 (con máscara triangular)                     │
│   - B: vector de bias (784 valores)                                         │
│   - z: resultado intermedio (784 valores, pueden ser cualquier número)      │
└─────────────────────────────────────────────────────────────────────────────┘
   │
   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ PASO 2: Sigmoide                                                            │
│                                                                              │
│   ŷ = sigmoid(z) = 1 / (1 + e^(-z))                                         │
│                                                                              │
│   - Convierte cada valor de z en un número entre 0 y 1                      │
│   - ŷ: las 784 probabilidades predichas (una por píxel)                     │
└─────────────────────────────────────────────────────────────────────────────┘
   │
   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ PASO 3: Binary Cross-Entropy (la pérdida)                                   │
│                                                                              │
│   BCE = -[y × log(ŷ) + (1-y) × log(1-ŷ)]                                    │
│                                                                              │
│   - y: los píxeles reales (0 o 1)                                           │
│   - ŷ: las probabilidades predichas (entre 0 y 1)                           │
│   - BCE: un número que dice "qué tan mal está el modelo"                    │
└─────────────────────────────────────────────────────────────────────────────┘
   │
   ▼
SALIDA: Un número (la pérdida). Queremos que sea lo más bajo posible.
```

### Ejemplo Numérico Concreto

```
Entrada X = [1, 0, 1, 0, 0, 1, ...]  (784 píxeles reales)

PASO 1: Multiplicación
   z = X × W^T + B
   z = [2.3, -1.5, 0.8, -0.2, ...]  (784 números, cualquier valor)

PASO 2: Sigmoide
   ŷ = sigmoid(z)
   ŷ = [0.91, 0.18, 0.69, 0.45, ...]  (784 números entre 0 y 1)

PASO 3: BCE (comparando con los píxeles reales)
   Para píxel 1: y=1, ŷ=0.91 → BCE = -log(0.91) = 0.09  ✓ bajo
   Para píxel 2: y=0, ŷ=0.18 → BCE = -log(1-0.18) = 0.20  ✓ bajo
   ...

   BCE_total = promedio de todos = 0.34
```

El modelo predijo bien (BCE bajo). Si hubiera predicho mal, BCE sería alto.

---

## ¿Por Qué Necesitamos Derivadas?

### El Problema: Queremos Mejorar el Modelo

Tenemos:
- **W** y **B**: los parámetros del modelo (lo que queremos ajustar)
- **BCE**: la pérdida (lo que queremos minimizar)

**Pregunta:** ¿Cómo ajustamos W y B para que BCE baje?

### La Respuesta: Gradiente Descendente

La derivada nos dice **en qué dirección cambiar** cada parámetro para reducir la pérdida.

```
∂BCE/∂W = "si aumento W un poquito, ¿BCE sube o baja?"
```

- Si ∂BCE/∂W > 0 → Aumentar W hace que BCE suba → Debemos BAJAR W
- Si ∂BCE/∂W < 0 → Aumentar W hace que BCE baje → Debemos SUBIR W

### La Regla de Actualización

```
W_nuevo = W_viejo - learning_rate × (∂BCE/∂W)
```

Es como bajar una montaña: siempre caminas en la dirección que baja.

---

## ¿Cómo se Calculan las Derivadas? (Backpropagation)

Un estudiante preguntó: "¿Cómo aplico gradiente a todos los W que están ahí adentro?"

El profesor respondió:

> "Si vos me creés que un perceptrón es derivable, ¿por qué el producto de la salida de los perceptrones no va a ser derivable?"

### La Cadena de Derivadas (Chain Rule)

Tenemos una cadena de operaciones:

```
X → [multiplicación] → z → [sigmoide] → ŷ → [BCE] → pérdida
```

Para encontrar ∂pérdida/∂W, usamos la **regla de la cadena**:

```
∂pérdida/∂W = (∂pérdida/∂ŷ) × (∂ŷ/∂z) × (∂z/∂W)
```

**Backpropagation = calcular estas derivadas de atrás hacia adelante.**

### Paso a Paso (Simplificado)

```
FORWARD (adelante): Calcular la pérdida
─────────────────────────────────────────────────────────────────────
X ──→ z = X×W+B ──→ ŷ = sigmoid(z) ──→ BCE = -[y×log(ŷ) + ...]
      (paso 1)         (paso 2)              (paso 3)


BACKWARD (atrás): Calcular los gradientes
─────────────────────────────────────────────────────────────────────
                                             ∂BCE/∂ŷ = -(y/ŷ) + ...
                                                  │
                              ∂ŷ/∂z = ŷ×(1-ŷ)    │
                                   │              │
                                   ▼              ▼
                              ∂BCE/∂z = ∂BCE/∂ŷ × ∂ŷ/∂z
                                   │
              ∂z/∂W = X            │
                   │               │
                   ▼               ▼
              ∂BCE/∂W = ∂BCE/∂z × ∂z/∂W    ← ESTO es lo que usamos para actualizar W
```

### ¿Por Qué Todo es Derivable?

Cada operación tiene una derivada conocida:

| Operación | Derivada |
|-----------|----------|
| z = X × W + B | ∂z/∂W = X |
| ŷ = sigmoid(z) | ∂ŷ/∂z = ŷ × (1 - ŷ) |
| BCE = -log(ŷ) | ∂BCE/∂ŷ = -1/ŷ |
| Suma | ∂(a+b)/∂a = 1 |

Como todas las piezas son derivables, **la composición también es derivable**.

---

## PyTorch Hace Todo Esto Automáticamente

El profesor lo resumió perfectamente:

> "Los muchachos de PyTorch, si ven una sumatoria, se cagan de risa. Entonces yo te digo: derivame la suma de 10 perceptrones. No es un problema técnico."

### Lo Que Tú Escribes

```python
# Forward pass (calcular pérdida)
predictions = model(images)           # Hace pasos 1 y 2
loss = criterion(predictions, images) # Hace paso 3 (BCE)

# Backward pass (calcular gradientes)
loss.backward()  # PyTorch calcula ∂loss/∂W y ∂loss/∂B automáticamente

# Actualizar parámetros
optimizer.step()  # W = W - lr × ∂loss/∂W
```

### Lo Que PyTorch Hace Por Ti

1. **Guarda** todas las operaciones que hiciste (el "grafo computacional")
2. **Calcula** las derivadas de cada operación (backpropagation)
3. **Multiplica** todo usando la regla de la cadena
4. **Almacena** los gradientes en `W.grad` y `B.grad`

**No necesitas calcular derivadas a mano.** Solo defines el modelo y PyTorch hace el resto.

### Resumen del Ciclo de Entrenamiento

```
┌─────────────────────────────────────────────────────────────────┐
│                    UN PASO DE ENTRENAMIENTO                      │
└─────────────────────────────────────────────────────────────────┘

1. FORWARD: Calcular predicciones y pérdida
   imagen → modelo(W, B) → predicción → BCE(predicción, imagen) → pérdida

2. BACKWARD: Calcular gradientes
   pérdida.backward() → calcula ∂pérdida/∂W y ∂pérdida/∂B

3. UPDATE: Actualizar parámetros
   W = W - lr × ∂pérdida/∂W
   B = B - lr × ∂pérdida/∂B

4. REPETIR con la siguiente imagen del dataset
```

Después de miles de repeticiones, W y B estarán ajustados para que el modelo genere buenas imágenes.

---

## Entrenamiento vs. Generación: La Asimetría Fundamental

### Durante el Entrenamiento (RÁPIDO)

Tienes la imagen completa. Haces UNA operación:

```
784 píxeles → [Matriz W] → 784 probabilidades (en paralelo)
```

Todo se calcula al mismo tiempo. Tarda milisegundos.

### Durante la Generación (LENTO)

No tienes nada. Debes hacer 784 pasos:

```
Paso 1: [] → probabilidad₁ → muestrear → píxel₁
Paso 2: [píxel₁] → probabilidad₂ → muestrear → píxel₂
Paso 3: [píxel₁, píxel₂] → probabilidad₃ → muestrear → píxel₃
...
Paso 784: [píxel₁...píxel₇₈₃] → probabilidad₇₈₄ → muestrear → píxel₇₈₄
```

**No puedes paralelizar.** Cada paso necesita el resultado del anterior.

### Por Qué ChatGPT "Escribe" Palabra por Palabra

Esta asimetría explica por qué los modelos de lenguaje como ChatGPT demoran en responder:

> "No puedes paralelizar la generación. Necesitas la palabra 3 antes de darte la 4."

Es la misma limitación. No puede generar toda la respuesta de golpe porque cada palabra depende de las anteriores.

### Resumen de la Asimetría

| | Entrenamiento | Generación |
|--|---------------|------------|
| Datos disponibles | Imagen completa | Nada (empiezas de cero) |
| Cálculo | Paralelo | Secuencial |
| Velocidad | Rápido | Lento |
| Operaciones | 1 pasada | 784 pasos |

---

## El Práctico: Implementando Hinton

### El Objetivo

Implementar el modelo de Hinton para generar imágenes de MNIST (números escritos a mano) y Fashion-MNIST (prendas de ropa).

### Los Datasets

- **MNIST**: Números del 0 al 9, imágenes de 28×28 píxeles
- **Fashion-MNIST**: Prendas de ropa, mismo formato

Los datos vienen en escala de grises (0-255). Los **binarizamos** a 0 o 1:

```python
if pixel > 0.5:
    pixel = 1
else:
    pixel = 0
```

### No Hay Test Set en Generativa

El profesor destacó algo importante:

> "¿Qué pasa con el train/test split? No existe el test. No queremos comparar contra test. Es una cosa que nos va a pasar en generativa."

¿Cómo validamos entonces? **Generamos imágenes y las miramos**. Si parecen números, funciona. Si no, no funciona.

### Simplificación Inicial: Un Solo Dígito

Para empezar, entrenamos solo con un tipo de dígito (por ejemplo, solo con "1"):

> "Nosotros no vamos a poder decir 'generame un 1, generame un 2'. Es simplemente vamos a generar. Entonces por simplicidad vamos a decir: solo vamos a generar un tipo de número."

### La Clase `Hinton`

Lo que hay que implementar:

```python
class Hinton(nn.Module):
    def __init__(self, input_size):
        # Definir:
        # - self.W: los pesos (matriz 784×784)
        # - self.B: los bias (vector de 784)
        # - self.mask: la máscara triangular

    def forward(self, x):
        # 1. Aplicar máscara a W (W * mask)
        # 2. Multiplicar x por W (cuidado con transpuesta)
        # 3. Sumar B
        # 4. Aplicar sigmoide
        # 5. Retornar

    def generate(self, num_images):
        # Generar imágenes píxel por píxel
        # Para cada píxel:
        #   1. Hacer forward
        #   2. Tomar la probabilidad del píxel actual
        #   3. Muestrear (Bernoulli)
        #   4. Actualizar la imagen
```

### El Forward: Solo 4-5 Líneas

```python
def forward(self, x):
    W_masked = self.W * self.mask  # Aplicar máscara
    z = x @ W_masked.T + self.B    # Multiplicar y sumar bias
    return torch.sigmoid(z)         # Sigmoide
```

Cuidado con las dimensiones. Si algo no funciona, imprime los shapes.

### El Generate: La Parte Compleja

El profesor explicó el proceso:

1. Empiezas con **ruido aleatorio** (o ceros) como imagen inicial
2. Pasas eso por forward → obtienes 784 probabilidades
3. **Solo usas la primera probabilidad** (para el primer píxel)
4. Muestreas: ¿0 o 1?
5. **Actualizas** la imagen con ese valor real
6. Vuelves a hacer forward → ahora el segundo píxel depende del primero real
7. Solo usas la segunda probabilidad, muestreas, actualizas
8. Repites 784 veces

> "Nosotros no podemos decirle a la red: te voy a pasar nada, vos dame solo una salida. La red siempre te va a dar 784 salidas. Lo único importante es que vos estás usando el primero. Todo lo demás está condicionado por el ruido que le diste."

### El Loop de Entrenamiento

```python
for epoch in range(num_epochs):
    for images, labels in train_loader:
        # Ignoramos labels (aprendizaje no supervisado)

        optimizer.zero_grad()
        predictions = model(images)
        loss = criterion(predictions, images)  # BCE Loss
        loss.backward()
        optimizer.step()

        # Cada N batches, generar y mostrar imágenes
```

Nota: **ignoramos los labels**. No los necesitamos porque es aprendizaje no supervisado.

### ¿Qué Pasa con Múltiples Dígitos?

Un estudiante preguntó: "Si entrenamos con 0 y 1, ¿qué genera?"

El profesor explicó:

> "Vos no vas a poder elegir si generar un cero o generar un uno. Pero acordate que cada píxel que vas eligiendo va dependiendo de los anteriores. Entonces, si arrancas generando algo que parece un uno, debería terminar de generar el uno."

Es aleatorio cuál número genera. Y teóricamente podría generar algo raro (un 0 con un 1 superpuesto), pero:

> "Debería ser baja la probabilidad, pero no es nula. Por eso, por ejemplo, cuando los modelos alucinan..."

---

## Conceptos Clave para Recordar

### 1. Autorregresivo = Secuencial en Generación

**Entrenamiento**: Paralelo (tienes todos los datos).
**Generación**: Secuencial (cada paso depende del anterior).

Esta es una **limitación fundamental**.

### 2. La Matriz Triangular Oculta el Futuro

Sin ella, el modelo haría trampa durante el entrenamiento. Los ceros garantizan que cada píxel solo depende de los anteriores.

### 3. Minimizamos el Negative Log-Likelihood

Queremos que el modelo asigne alta probabilidad a los datos reales. Minimizar -log P(x) = maximizar P(x).

### 4. En la Práctica Usamos Binary Cross-Entropy

Es la implementación de NLL para variables binarias. PyTorch lo tiene: `nn.BCELoss()`.

### 5. No Hay Test Set en Generativa

Validamos **mirando** las imágenes generadas. ¿Parecen reales? Si sí, funciona.

### 6. Todo es Derivable

Sigmoide, logaritmo, suma, producto... todo es derivable. PyTorch calcula los gradientes automáticamente.

---

## La Conexión con lo que Viene

### GPT y Modelos de Lenguaje

Todo lo que estamos haciendo con píxeles se aplica a palabras. GPT genera texto exactamente así:
- Cada palabra es una variable aleatoria (categórica, no Bernoulli)
- Cada palabra depende de las anteriores
- Se genera secuencialmente

### Otros Modelos Generativos

Los modelos autorregresivos son solo el comienzo. Después veremos:
- **VAEs** (Variational Autoencoders)
- **GANs** (Generative Adversarial Networks)
- **Diffusion Models**

Cada uno tiene una forma diferente de estimar P(x), pero todos buscan lo mismo: aprender la distribución de los datos para generar datos nuevos.

### Por Qué Hinton es el Punto de Partida

El modelo de Hinton es simple pero poderoso. Entenderlo te da las bases para entender todo lo demás.

---

## ¿Es Necesario Saber Todas las Fórmulas?

El profesor fue claro:

> "Esto no es un curso de matemáticas puras. La idea es entender los conceptos y poder implementarlos."

### Lo que SÍ Necesitas

- **Entender** qué hace un modelo autorregresivo
- **Entender** por qué la matriz es triangular
- **Poder implementar** el código en PyTorch
- **Entender** la diferencia entre entrenar y generar
- **Saber usar** BCELoss

### Lo que NO Necesitas

- Memorizar la fórmula de KL divergencia
- Saber demostrar que KL ≥ 0
- Derivar manualmente las ecuaciones

### El Consejo del Profesor

> "La idea es que machaquemos hasta que quede. Son conceptos que son abstractos y empezar a jugar con esas abstracciones de manera sencilla es un desafío. Quédense tranquilos."

---

## Resumen: El Flujo Completo

### 1. El Modelo
- Cada píxel es una Bernoulli con parámetro α
- α se estima con un perceptrón
- Los perceptrones están organizados en una matriz triangular

### 2. El Entrenamiento
- Pasamos imágenes completas
- La máscara garantiza que cada píxel solo ve los anteriores
- Minimizamos BCE (Binary Cross-Entropy)
- Los pesos W y B se actualizan con gradiente descendente

### 3. La Generación
- Empezamos con ruido
- Generamos píxel por píxel
- Cada píxel se muestrea de su Bernoulli
- El resultado se usa para generar el siguiente

### 4. La Validación
- No hay test set
- Miramos las imágenes generadas
- Si parecen números, funciona

Este es el primer modelo generativo completo. Todo lo que viene después es variaciones y mejoras sobre estas ideas fundamentales.

---

## Definiciones para el Parcial

### Modelos Autorregresivos

**Modelo Autorregresivo:** Modelo donde cada predicción depende de las predicciones anteriores; se "alimenta" de sus propias salidas para generar la siguiente; ejemplos: GPT (palabras), Hinton (píxeles).

**Regla de la Cadena (Probabilidades):** P(X₁,...,Xₙ) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂) × ...; permite descomponer la probabilidad conjunta en producto de condicionales que podemos estimar.

**Asimetría Entrenamiento/Generación:** Durante entrenamiento es paralelo (tienes todos los datos), durante generación es secuencial (cada paso depende del anterior); esto explica por qué ChatGPT "escribe" palabra por palabra.

### El Modelo de Hinton

**Distribución de Bernoulli:** Distribución con un solo parámetro α entre 0 y 1 que modela algo con dos resultados (0 o 1); α = probabilidad de obtener 1.

**Modelo de Hinton:** Primer modelo autorregresivo neuronal; usa perceptrones de una capa para estimar α de cada píxel; organizado en matriz triangular.

**Matriz Triangular (Máscara):** Estructura donde la parte superior son ceros fijos (no entrenables); garantiza que cada píxel solo "vea" los anteriores, no el futuro; usa diagonal=-1 porque el píxel i no debe depender de sí mismo.

### El Modelo de Bengio

**Modelo de Bengio:** Extensión de Hinton con múltiples capas ocultas; más capas = puede aprender relaciones más complejas entre píxeles.

**Capa Oculta:** Transformación intermedia entre entrada y salida; permite detectar patrones simples primero y luego combinarlos; usa ReLU para flexibilidad.

**ReLU vs Sigmoide:** ReLU(x) = max(0, x) para capas intermedias (valores libres); Sigmoide solo en la última capa (para obtener probabilidad entre 0 y 1).

### La Función de Pérdida

**KL Divergence (Kullback-Leibler):** Mide qué tan diferentes son dos distribuciones P_data y P_θ; KL ≥ 0 siempre; KL = 0 solo si son idénticas; minimizarla = hacer que el modelo se parezca a los datos reales.

**Negative Log-Likelihood (NLL):** Simplificación de KL; queremos que el modelo asigne alta probabilidad a datos reales; minimizar -log P_θ(x) = maximizar P_θ(x).

**Binary Cross-Entropy (BCE):** BCE = -[y × log(ŷ) + (1-y) × log(1-ŷ)]; implementación de NLL para variables binarias; funciona como "selector" que usa el término correcto según si el dato real es 0 o 1.

**Por qué BCE:** Si dato=1, queremos ŷ alto (cerca de 1); si dato=0, queremos ŷ bajo (cerca de 0); BCE penaliza cuando el modelo se equivoca en cualquier dirección.

### Estabilidad Numérica

**Underflow:** Problema cuando multiplicamos muchas probabilidades pequeñas (0.9 × 0.8 × ... 784 veces) y el resultado es tan pequeño que la computadora lo redondea a 0.

**Truco del Logaritmo:** log(A × B × C) = log(A) + log(B) + log(C); convierte multiplicaciones en sumas, evitando underflow y reduciendo error acumulado.

### Entrenamiento

**Forward Pass:** Calcular predicciones pasando datos por el modelo; imagen → modelo → 784 probabilidades.

**Backward Pass (Backpropagation):** Calcular gradientes de la pérdida respecto a cada parámetro usando la regla de la cadena de derivadas.

**Regla de la Cadena (Derivadas):** ∂pérdida/∂W = (∂pérdida/∂ŷ) × (∂ŷ/∂z) × (∂z/∂W); permite calcular cómo cada peso afecta la pérdida final.

### Generación

**Proceso de Generación:** 1) Empezar con ruido o ceros, 2) Forward pass, 3) Usar solo la probabilidad del píxel actual, 4) Muestrear (Bernoulli), 5) Actualizar imagen, 6) Repetir 784 veces.

**No hay Test Set en Generativa:** Validamos mirando las imágenes generadas; si parecen números reales, el modelo funciona.

### Correspondencia Distribución-Loss

| Tipo de dato | Distribución asumida | Función de pérdida |
|--------------|---------------------|-------------------|
| Binario (0/1) | Bernoulli | BCE (Binary Cross-Entropy) |
| Categórico (1 de N) | Categórica | Cross-Entropy |
| Continuo | Gaussiana | MSE (Mean Squared Error) |

### Fórmulas Clave

**Probabilidad Bernoulli:** P(y|α) = α^y × (1-α)^(1-y)

**BCE:** -[y × log(ŷ) + (1-y) × log(1-ŷ)]

**Actualización de pesos:** W_nuevo = W_viejo - lr × (∂BCE/∂W)
