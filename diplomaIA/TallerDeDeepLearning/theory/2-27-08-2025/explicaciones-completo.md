# Clase 2 (27 de Agosto 2025) - Taller de Deep Learning
## Perceptrón, XOR, Redes Multicapa y Grafos Computacionales

---

# CONTEXTO DE LA CLASE

Esta es la **segunda clase del curso**, pero el profesor decidió continuar con contenido de la Clase 1 por dos motivos:
1. No terminaron el notebook 2 la clase anterior
2. No hubo clase el lunes previo, entonces dos clases seguidas sería demasiado

El profesor menciona que:
> "El tema que vamos a dar hoy, ustedes lo van a dar más en profundidad el lunes."

Hay también **dos notebooks extras** que NO forman parte de la clase obligatoria pero están disponibles:
- **Gradientes y optimizadores**: cómo funcionan los optimizadores durante el entrenamiento
- **Precisión float16 vs float32**: comparativas de entrenamiento con diferentes precisiones

---

# MAPA CONCEPTUAL: ¿Qué vamos a aprender?

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                     EVOLUCIÓN DE LA CLASE                                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║   PARTE 1: PERCEPTRÓN SIMPLE (Primera hora)                                 ║
║   ┌────────────────────────────────────────────────────────────┐            ║
║   │  1. Implementar AND con pesos manuales                     │            ║
║   │     └─ Usando multiplicación de matrices                   │            ║
║   │     └─ Dos formas: bias dentro de X, o bias separado       │            ║
║   │                                                             │            ║
║   │  2. Implementar OR (ejercicio estudiantes)                 │            ║
║   │     └─ Encontrar pesos que den: [-1, 1, 1, 1]              │            ║
║   │                                                             │            ║
║   │  3. El problema del XOR                                    │            ║
║   │     └─ NO ES LINEALMENTE SEPARABLE                         │            ║
║   │     └─ El "invierno de la IA" (Minsky, McCarthy)           │            ║
║   │     └─ Impacto histórico: pérdida de financiamiento        │            ║
║   └────────────────────────────────────────────────────────────┘            ║
║                           ▼                                                  ║
║   PARTE 2: PERCEPTRÓN MULTICAPA (Segunda hora)                              ║
║   ┌────────────────────────────────────────────────────────────┐            ║
║   │  4. Solución con Red Neuronal (MLP)                        │            ║
║   │     └─ Arquitectura: 2 → 4 → 1 (con sigmoid)               │            ║
║   │     └─ Dos formas de definir: nn.Module y nn.Sequential    │            ║
║   │                                                             │            ║
║   │  5. Entrenamiento automático                               │            ║
║   │     └─ Loss function: MSE                                  │            ║
║   │     └─ Optimizer: Adam                                     │            ║
║   │     └─ Training loop con .backward() y .step()             │            ║
║   │                                                             │            ║
║   │  6. Ejercicio final: Implementar 3 funciones a la vez      │            ║
║   │     └─ Salida: [AND, OR, XOR] simultáneas                  │            ║
║   │     └─ Arquitectura más grande: 2 → 4 → 3                  │            ║
║   └────────────────────────────────────────────────────────────┘            ║
║                           ▼                                                  ║
║   PARTE 3: GRAFO COMPUTACIONAL (Tercera hora - EXTRA)                       ║
║   ┌────────────────────────────────────────────────────────────┐            ║
║   │  7. ¿Qué es require_grad?                                  │            ║
║   │     └─ Cómo PyTorch rastrea operaciones                    │            ║
║   │     └─ Visualización con torchviz                          │            ║
║   │                                                             │            ║
║   │  8. Forward pass en detalle                                │            ║
║   │     └─ Qué pasa dentro de nn.Linear                        │            ║
║   │     └─ Matriz de pesos W, vector de bias b                 │            ║
║   │                                                             │            ║
║   │  9. Backward pass y optimizadores                          │            ║
║   │     └─ Cómo se calculan gradientes                         │            ║
║   │     └─ Rol del learning rate                               │            ║
║   │     └─ Detach y torch.no_grad()                            │            ║
║   └────────────────────────────────────────────────────────────┘            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## SECCIÓN A: Perceptrón Simple - Implementando AND

### ¿Qué es un perceptrón?

Un **perceptrón** es la unidad más básica de una red neuronal. Hace una multiplicación de matrices y aplica una función de activación.

```
╔════════════════════════════════════════════════════════════╗
║                    ANATOMÍA DEL PERCEPTRÓN                  ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║   INPUTS        PESOS          FUNCIÓN                     ║
║   (x)           (w)            ACTIVACIÓN                  ║
║                                                            ║
║   x₁ ──┐                                                   ║
║         ├──→ [w₁, w₂, b] ──→ Σ ──→ sign() ──→ output      ║
║   x₂ ──┘                                                   ║
║                                                            ║
║   Fórmula: output = sign(x₁*w₁ + x₂*w₂ + b)                ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

### La función signo (sign)

El profesor define su propia función `sign` porque la de PyTorch se comporta diferente con el cero:

```python
# PyTorch nativo:
torch.sign(0)  → 0

# Función personalizada del profesor:
mi_sign(0)  → 1  (trata 0 como positivo)
```

**Implementación:**
```python
def sign(x):
    return torch.where(x >= 0,
                       torch.tensor(1.0),
                       torch.tensor(-1.0))
```

### Tabla de verdad del AND

```
╔═══════════════════════════════════════════════════════╗
║          TABLA DE VERDAD - OPERACIÓN AND              ║
╠═══════════════════════════════════════════════════════╣
║   x₁   │   x₂   │   salida   │  Interpretación        ║
╠════════╪════════╪════════════╪═══════════════════════╣
║   -1   │   -1   │     -1     │  False AND False = F   ║
║   -1   │    1   │     -1     │  False AND True = F    ║
║    1   │   -1   │     -1     │  True AND False = F    ║
║    1   │    1   │      1     │  True AND True = T     ║
╚═══════════════════════════════════════════════════════╝

Donde:  -1 = False,  1 = True
```

### Primera forma: Bias incluido en X

**La idea:** El vector X tiene 3 elementos: [x₁, x₂, 1], donde el último "1" es para multiplicar por el bias.

```python
# Datos de entrada (con columna extra para bias)
x = torch.tensor([
    [-1, -1,  1],    # False, False
    [-1,  1,  1],    # False, True
    [ 1, -1,  1],    # True, False
    [ 1,  1,  1]     # True, True
], dtype=torch.float32)

# Pesos: [w₁, w₂, bias]
w = torch.tensor([0.5, 0.5, -1.0], dtype=torch.float32)

# Operación
resultado = sign(torch.matmul(x, w))
# Da: [-1, -1, -1, 1] ✓
```

### ¿Por qué estos pesos funcionan?

**Ejemplo con (1, 1):**
```
Cálculo: (1 × 0.5) + (1 × 0.5) + (1 × -1.0) = 0.5 + 0.5 - 1.0 = 0
sign(0) = 1  ✓ (correcto, True AND True = True)
```

**Ejemplo con (-1, 1):**
```
Cálculo: (-1 × 0.5) + (1 × 0.5) + (1 × -1.0) = -0.5 + 0.5 - 1.0 = -1.0
sign(-1.0) = -1  ✓ (correcto, False AND True = False)
```

### Segunda forma: Bias separado

```python
# Datos sin columna extra
x = torch.tensor([
    [-1, -1],
    [-1,  1],
    [ 1, -1],
    [ 1,  1]
], dtype=torch.float32)

# Pesos separados
w = torch.tensor([1.0, 1.0], dtype=torch.float32)
b = torch.tensor(-1.0)

# Operación
resultado = sign(torch.matmul(x, w) + b)
# Da: [-1, -1, -1, 1] ✓
```

**Ventaja:** Es más claro conceptualmente. El bias no "contamina" los datos de entrada.

### Broadcasting en PyTorch

El profesor menciona que aunque `x @ w` da un vector de forma `(4, 1)` y `b` es un escalar, PyTorch puede sumarlos gracias a **broadcasting**:

> "Por más que no tenga el mismo shape, se puede hacer la operación bajo broadcasting."

---

## SECCIÓN B: Implementando OR (Ejercicio en clase)

### Tabla de verdad del OR

```
╔═══════════════════════════════════════════════════════╗
║          TABLA DE VERDAD - OPERACIÓN OR               ║
╠═══════════════════════════════════════════════════════╣
║   x₁   │   x₂   │   salida   │  Interpretación        ║
╠════════╪════════╪════════════╪═══════════════════════╣
║   -1   │   -1   │     -1     │  False OR False = F    ║
║   -1   │    1   │      1     │  False OR True = T     ║
║    1   │   -1   │      1     │  True OR False = T     ║
║    1   │    1   │      1     │  True OR True = T      ║
╚═══════════════════════════════════════════════════════╝

Solo cuando AMBOS son False, el resultado es False.
```

### Solución (mencionada en clase)

```python
# Pesos conocidos:
w = torch.tensor([1.0, 1.0, -1.0])  # Con bias incluido

# O con bias separado:
w = torch.tensor([1.0, 1.0])
b = torch.tensor(-1.0)
```

El profesor da 5-10 minutos para que los estudiantes lo implementen por su cuenta.

---

## SECCIÓN C: El Problema del XOR - El Invierno de la IA

### Tabla de verdad del XOR

```
╔═══════════════════════════════════════════════════════╗
║          TABLA DE VERDAD - OPERACIÓN XOR              ║
╠═══════════════════════════════════════════════════════╣
║   x₁   │   x₂   │   salida   │  Interpretación        ║
╠════════╪════════╪════════════╪═══════════════════════╣
║   -1   │   -1   │     -1     │  False XOR False = F   ║
║   -1   │    1   │      1     │  False XOR True = T    ║
║    1   │   -1   │      1     │  True XOR False = T    ║
║    1   │    1   │     -1     │  True XOR True = F     ║
╚═══════════════════════════════════════════════════════╝

XOR = "Uno u otro, pero NO ambos"
```

### ¿Por qué es imposible con perceptrón simple?

El profesor explica que **NO es linealmente separable**:

> "Si vos puedes dibujar en el plano con coordenadas los puntos, y básicamente trazar una línea recta que puede dejar del mismo lado los puntos del mismo color... pero con XOR los puntos quedan cruzados."

```
Visualización en el plano:

    x₂
     │
   1 │    ⊕ (1,1)        ○ (-1,1)      ⊕ = True (1)
     │                                  ○ = False (-1)
   0 ├─────────────────────
     │
  -1 │    ○ (-1,-1)      ⊕ (1,-1)
     │
     └─────────────────────── x₁
        -1        0        1

¿Puedes trazar UNA línea recta que separe ⊕ de ○?
¡NO! Los puntos están en diagonal opuesta.
```

### Interpretación geométrica

El profesor explica:

> "Cuando vos hacés w·x + b = 0, estás haciendo una recta. El vector w es la normal de la recta. Lo único que hace el bias b es mover la recta."

> "sign() lo único que hace es poner un valor a los que están de un lado de la recta, y otro valor a los del otro lado."

**Entonces:** Un perceptrón simple = buscar UNA recta que separe los datos.

### Historia: El "invierno de la IA"

El profesor cuenta la historia completa:

> "En los años 70 [Minsky y otros] demostraron que el perceptrón no puede resolver XOR. Esto causó lo que se llama el 'invierno de la IA'."

**Contexto histórico:**

1. **Años 50-60:** Gran optimismo sobre IA
   - McCarthy y otros decían: "En menos de 10 años ya vamos a resolver el problema de razonamiento humano"
   - Único financiador importante: Departamento de Defensa de EE.UU.

2. **Años 70:** Llega el libro de Minsky sobre XOR
   > "Viene el libro famoso de Perceptrons [de Minsky] que demostró que el perceptrón no puede resolver XOR. Le puso la cruz."

3. **El impacto:**
   > "Si vos apostás a una tecnología porque especulás que va a crecer, e imaginate que vine alguien y diga matemáticamente este es el límite... ¿qué pensabas que va a pasar con la bolsa? Va a bajar."

   > "No va a haber financiamiento. Era una época donde había muy poca gente trabajando en IA, y el que invertía más era el gobierno de Estados Unidos."

4. **El problema filosófico:**
   > "No puede hacer algo tan simple como XOR, ¿por qué haría algo más complejo?"

### La solución (adelanto): Multicapa

> "Una de las formas más conocidas [de resolver XOR] es poner más capas. Sería podrías levantar [el plano]. Una dimensión más sería una forma de levantar."

La idea: si no puedes separar en 2D con una línea, **levanta el espacio a 3D** y separa con un plano.

---

## SECCIÓN D: Implementando NAND y NOR (Rápido)

El profesor menciona brevemente que también hay que implementar:

- **NAND** (NOT AND): negativo del AND
  - Pesos: `-1 * pesos_del_AND`

- **NOR** (NOT OR): negativo del OR
  - Mismo problema que XOR si se usa perceptrón simple

```
NAND:  [-1, -1] → 1,  [-1, 1] → 1,  [1, -1] → 1,  [1, 1] → -1
NOR:   [-1, -1] → 1,  [-1, 1] → -1,  [1, -1] → -1,  [1, 1] → -1
```

---

## SECCIÓN E: Solución con Perceptrón Multicapa (MLP)

### La arquitectura propuesta

```
╔═══════════════════════════════════════════════════════════════════════╗
║                   RED NEURONAL PARA RESOLVER XOR                      ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║   INPUT         CAPA OCULTA        SALIDA                             ║
║   (2 neuronas)  (2 neuronas)       (1 neurona)                        ║
║                                                                       ║
║      x₁ ───┐                                                          ║
║             ├──→ ●                                                    ║
║      x₂ ───┼──→ ● ─────→ sigmoid ──→ ● ──→ sigmoid ──→ output        ║
║             ├──→ ●                   ↑                                ║
║             └──→ ●                   │                                ║
║                  ↑                   │                                ║
║               sigmoid                │                                ║
║                                      │                                ║
║   2 entradas → 2 ocultas → 1 salida                                   ║
║                                                                       ║
║   Código PyTorch:                                                     ║
║   nn.Linear(2, 2)  → primera capa                                     ║
║   nn.Sigmoid()     → activación                                       ║
║   nn.Linear(2, 1)  → segunda capa                                     ║
║   nn.Sigmoid()     → activación final                                 ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
```

### Forma 1: Definir con `nn.Module`

```python
class XorNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.input = nn.Linear(2, 2)    # 2 → 2
        self.output = nn.Linear(2, 1)   # 2 → 1

    def forward(self, x):
        x = torch.sigmoid(self.input(x))   # Primera capa + activación
        x = torch.sigmoid(self.output(x))  # Segunda capa + activación
        return x

model = XorNet()
```

**Explicación del profesor:**

> "Muchas veces cuando se define el forward, ya se hace la función de activación y pasado por esa capa en la misma línea. Pero perfectamente esto lo pueden hacer en dos líneas diferentes."

```python
# Alternativa más explícita:
def forward(self, x):
    x = self.input(x)       # Paso 1: multiplicación matricial
    x = torch.sigmoid(x)     # Paso 2: activación
    x = self.output(x)       # Paso 3: segunda capa
    x = torch.sigmoid(x)     # Paso 4: activación final
    return x
```

### Forma 2: Usar `nn.Sequential`

```python
model = nn.Sequential(
    nn.Linear(2, 2),
    nn.Sigmoid(),
    nn.Linear(2, 1),
    nn.Sigmoid()
)
```

**Comentario del profesor:**

> "Esto es un pipeline. Cuando nosotros vemos ese estilo cascada, podemos utilizar nn.Sequential. Es una forma más simplificada de hacer lo mismo."

### ¿Cuándo usar cada forma?

El profesor explica:

> "A medida que vamos avanzando en el curso, vamos a tener arquitecturas mucho más complejas que no son simplemente lineales, sino que van a tener algún tipo de vuelta. Van a hacer arquitecturas que no definen una cascada."

**Entonces:**
- **nn.Sequential**: Para arquitecturas sencillas, "pipeline" lineal
- **nn.Module**: Para arquitecturas complejas con conexiones no lineales

---

## SECCIÓN F: Entrenamiento de la Red

### Los componentes necesarios

```python
# 1. Definir el modelo
model = XorNet()

# 2. Función de pérdida (loss function)
criterion = nn.MSELoss()  # Mean Squared Error

# 3. Optimizador
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
```

### Datos de entrada y salida

```python
# Entrada (cambio importante: ahora usamos 0 y 1)
x = torch.tensor([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=torch.float32)

# Salida esperada (XOR)
y = torch.tensor([
    [0],
    [1],
    [1],
    [0]
], dtype=torch.float32)
```

**IMPORTANTE:** Aquí el profesor usa **0 y 1** en vez de **-1 y 1**:

> "Fíjense que acá no tenemos menos uno y uno, sino tenemos 0 y 1. Si tenemos de nuestra salida que da 0 o 1, es justamente una clasificación binaria."

### El training loop

```python
model.train()  # Poner en modo entrenamiento

for epoch in range(1000):
    # Forward pass
    output = model(x)

    # Calcular loss
    loss = criterion(output, y)

    # Backward pass
    optimizer.zero_grad()  # Limpiar gradientes anteriores
    loss.backward()        # Calcular nuevos gradientes
    optimizer.step()       # Actualizar pesos

    # Mostrar progreso cada 100 épocas
    if epoch % 100 == 0:
        print(f'Época {epoch}, Loss: {loss.item()}')
```

### ¿Qué hace cada línea?

**`model.train()`:**

El profesor aclara:

> "No es que el 1 de enero vamos a empezar a ejercitarnos para llegar al próximo verano, sino que va a cambiar el comportamiento de nuestra red."

> "En este caso particular, como tenemos simplemente capas secuenciales y sigmoid, no va a hacer ningún tipo de diferencia. Pero cuando veamos algunas capas especiales como dropout, se comportan ligeramente diferentes si está en modo entrenamiento o modo evaluación."

**`optimizer.zero_grad()`:**

> "Si no haces esto, los gradientes se van acumulando de épocas anteriores."

**`loss.backward()`:**

> "Utiliza la red, recorriendo de la capa de salida hasta la capa de entrada, y calcula los gradientes o cuánto tenemos que ajustar cada uno de los pesos."

**`optimizer.step()`:**

> "El optimizer toma cada uno de esos gradientes y termina actualizando los pesos."

### ¿Por qué va bajando el loss?

El profesor explica:

> "Al principio los pesos son totalmente aleatorios. Esto me dio 0.7, y tendría que haber dado 1. Esto tendría que haber dado 0 y me dio 0.4. Esto me dio 0.8 y me tendría que dar 0."

> "A medida que vamos entrenando, la loss va bajando hasta acercarse a un número relativamente chico o aceptable para que digamos que la red funciona."

---

## SECCIÓN G: Predicción y Redondeo

### Salida cruda del modelo

Después de entrenar, si haces:

```python
output = model(x)
print(output)
```

Obtienes algo como:
```
tensor([[0.0234],
        [0.9876],
        [0.9823],
        [0.0145]], grad_fn=<SigmoidBackward>)
```

### Convertir a 0 o 1

El profesor usa `torch.where`:

```python
output_binario = torch.where(output < 0.5,
                              torch.tensor(0.0),
                              torch.tensor(1.0))
```

**Explicación:**

> "Si x es menor que 0.5, imprime 0. Si no, 1."

**Analogía con if-else:**

> "Es un if esto, sino esto."

**Alternativa con round:**

También podrías usar `torch.round(output)` para redondear 0.48 → 0, 0.87 → 1.

---

## SECCIÓN H: Ejercicio Final - 3 Funciones Simultáneas

### El desafío

El profesor propone:

> "Vamos a implementar tres funciones al mismo tiempo: la salida del OR, la salida del AND, y la salida del XOR."

```python
# Entrada (sigue siendo la misma)
x = torch.tensor([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=torch.float32)

# Salida AMPLIADA (3 columnas)
y = torch.tensor([
    [0, 0, 0],  # 0,0 → AND=0, OR=0, XOR=0
    [0, 1, 1],  # 0,1 → AND=0, OR=1, XOR=1
    [0, 1, 1],  # 1,0 → AND=0, OR=1, XOR=1
    [1, 1, 0]   # 1,1 → AND=1, OR=1, XOR=0
], dtype=torch.float32)
```

### Arquitectura necesaria

```
2 entradas → 4 ocultas → 3 salidas

nn.Sequential(
    nn.Linear(2, 4),   # Más neuronas ocultas
    nn.Sigmoid(),
    nn.Linear(4, 3),   # 3 salidas (una por función)
    nn.Sigmoid()
)
```

**Comentario del profesor:**

> "Probablemente la arquitectura de 2 → 2 → 1 no les sirva. Ustedes tienen que empezar a mapear: ¿qué tanto sacando una neurona más [necesito]?"

---

## SECCIÓN I: Grafo Computacional y `require_grad`

### ¿Qué es el grafo computacional?

El profesor explica:

> "Cuando uno pasa por una red, termina teniendo un tensor el cual, como cualquiera lo hemos visto antes, lleva aparte de los valores resultantes un historial de alguna manera sabe por dónde pasó para llegar ahí."

### Ejemplo simple

```python
a = torch.tensor(5.0, requires_grad=True)
b = torch.tensor(3.0, requires_grad=True)
c = torch.tensor(2.0, requires_grad=True)

x = a * c + b * b
```

**¿Qué contiene `x`?**

1. **Valor:** 5*2 + 3*3 = 10 + 9 = 19
2. **Historial:** Sabe que vino de `a`, `b`, `c` y qué operaciones se hicieron

### Visualización con `torchviz`

El profesor usa la librería `torchviz` (no obligatoria, solo para esta clase):

```python
from torchviz import make_dot
make_dot(x, params={'a': a, 'b': b, 'c': c})
```

Esto genera un gráfico que muestra:

```
        x (raíz)
         │
    ┌────┴────┐
    │         │
   MUL       ADD
    │         │
  ┌─┴─┐    ┌─┴─┐
  a   c    b   b
```

**Interpretación:**

- Los **grises** son operaciones (MUL, ADD)
- Los **celestes** son tensores (hojas del árbol)
- La **raíz** es el resultado final (x)

### ¿Para qué sirve esto?

> "Para saber por qué esto llegó a 19, tengo que saber cuáles de estos pesos y cómo intercedieron para llegar a ese resultado."

> "Es lo que hace el `backward()`. Si vos sabés todos los elementos que pasaron y qué operaciones hubo, de alguna manera puedes encontrar el culpable o qué tanto podés ajustar cada uno de estos elementos."

---

## SECCIÓN J: `require_grad` en Redes Neuronales

### ¿Dónde está activado?

**Pregunta de estudiante:**

> "En el perceptrón nunca le pusimos `require_grad=True`. ¿Cómo funciona?"

**Respuesta del profesor:**

> "Cuando vos usás capas neuronales, todas estas capas por defecto por atrás ya tienen `require_grad=True`. Los pesos de cada capa ya tienen esto activado."

```python
model = nn.Linear(2, 4)

# Los pesos internos ya tienen require_grad=True
print(model.weight.requires_grad)  # True
print(model.bias.requires_grad)    # True
```

### ¿Y la entrada X?

> "La entrada, el X, no lo tiene. Pero todo lo que pasa para atrás, cuando se lo empieza a operar, se lo empieza a calcular."

**Entonces:**
- **Pesos y bias:** `requires_grad=True` (queremos actualizarlos)
- **Entrada X:** `requires_grad=False` (son datos fijos)

---

## SECCIÓN K: Forward Pass en Detalle

### ¿Qué hay dentro de `nn.Linear`?

```python
capa = nn.Linear(2, 4)
```

Internamente guarda:

1. **Matriz de pesos W:** forma `(4, 2)`
2. **Vector de bias b:** forma `(4,)`

```
╔═════════════════════════════════════════════════════════════╗
║                    DENTRO DE nn.Linear                      ║
╠═════════════════════════════════════════════════════════════╣
║                                                             ║
║   capa.weight:                                              ║
║   ┌────────────────┐                                        ║
║   │ w₁₁    w₁₂     │                                        ║
║   │ w₂₁    w₂₂     │  ← Forma (4, 2)                        ║
║   │ w₃₁    w₃₂     │                                        ║
║   │ w₄₁    w₄₂     │                                        ║
║   └────────────────┘                                        ║
║                                                             ║
║   capa.bias:                                                ║
║   [ b₁, b₂, b₃, b₄ ]  ← Forma (4,)                          ║
║                                                             ║
║   Operación:                                                ║
║   output = X @ W.T + b                                      ║
║          = (N, 2) @ (2, 4) + (4,)                           ║
║          = (N, 4)                                           ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝
```

### Inicialización de pesos

El profesor menciona:

> "Hoy en día con estos pesos en general, se hace una estrategia de inicialización totalmente al azar."

> "Después se encuentran papers que pueden decir: para este tipo en particular de problemas, la inicialización se hace mediante otra estrategia."

**Pero en general:** Al inicio los pesos son aleatorios, por eso la salida es "papa fritas" (basura).

---

## SECCIÓN L: Backward Pass y Gradientes

### ¿Qué hace `loss.backward()`?

El profesor explica paso a paso:

1. **Se tiene la salida de la red** (valores aleatorios al principio)
2. **Se compara con la salida esperada** (usando la loss function)
3. **Se calcula la diferencia** (el error)
4. **Se recorre la red hacia atrás**, calculando para cada peso:

> "Qué tanto se relaciona ese peso con la salida, o más bien con el loss."

> "En cada neurona va a calcular el gradiente. Qué tanto cambiar ese peso afecta a la salida."

### Ejemplo numérico (informal)

Supón que:
- La red predijo `0.7` pero debía predecir `1.0`
- Error: `(0.7 - 1.0)² = 0.09`

El backward calcula:
- Si aumento `w₁` en 0.01 → el error baja a 0.08 → gradiente **negativo**
- Si aumento `w₂` en 0.01 → el error sube a 0.10 → gradiente **positivo**

### ¿Qué hace `optimizer.step()`?

Toma esos gradientes y **actualiza los pesos**:

```
w_nuevo = w_viejo - learning_rate × gradiente
```

**Ejemplo:**
```
w₁ = 0.5 - 0.1 × (-0.3) = 0.5 + 0.03 = 0.53  (sube porque grad negativo)
w₂ = 0.8 - 0.1 × (+0.2) = 0.8 - 0.02 = 0.78  (baja porque grad positivo)
```

---

## SECCIÓN M: Épocas, Batches y el Training Loop

### ¿Qué es una época?

**Pregunta de estudiante:**

> "¿La época es haber pasado todos los datos una vez?"

**Respuesta del profesor:**

> "Exacto. En este caso particular, cuando nosotros hacemos el forward, pasamos las 4 filas a la vez. Eso sería 1 época."

### Épocas vs Iteraciones

```
╔══════════════════════════════════════════════════════════════╗
║               ÉPOCAS vs BATCHES vs ITERACIONES               ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Si tienes 1000 datos y batch_size = 100:                   ║
║                                                              ║
║  1 ÉPOCA = 10 iteraciones (1000 / 100)                       ║
║                                                              ║
║  Iteración 1: datos 0-99                                     ║
║  Iteración 2: datos 100-199                                  ║
║  ...                                                         ║
║  Iteración 10: datos 900-999                                 ║
║                                                              ║
║  ¡Completaste 1 época!                                       ║
║                                                              ║
║  Ahora vuelves a pasar por todos (época 2)...                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

En el ejemplo de XOR:
- Solo hay **4 datos**
- Se pasan **todos juntos** (batch de 4)
- Entonces: **1 iteración = 1 época**

### ¿Por qué múltiples épocas?

**Pregunta de estudiante:**

> "Si hace un ajuste promedio en cada época, ¿por qué hacerlo muchas veces?"

**Respuesta del profesor:**

> "Lo que estás haciendo vos es tratar de aprender la distribución de los datos. Cuando hacés la segunda época, el error promedio baja más, porque lo achicaste en la primera y ahora lo achicás más."

> "Si vos no tenés problemas de cálculo numérico [vanishing/exploding gradient], las redes neuronales están condenadas a aprender."

---

## SECCIÓN N: `detach()` y `torch.no_grad()`

### ¿Qué hace `detach()`?

El profesor explica:

> "A veces a mí me interesaría que el cálculo de un tensor simplemente sacarlo del grafo computacional. Digo: mira, yo llegué a este resultado, pero no quiero que siga."

```python
x = modelo(entrada)    # Tiene grafo computacional
x_sin_grad = x.detach()   # Pierde el historial

# Ahora si operas con x_sin_grad, no se rastrea
```

**Analogía:**

> "Es como cuando entrás en incógnito, no se guarda nada. Es lo mismo, yo saco la historia."

### `torch.no_grad()`

```python
with torch.no_grad():
    output = modelo(entrada)
    # Aquí NO se calcula el grafo
```

**Diferencia:**

- `detach()`: Saca UN tensor del grafo
- `torch.no_grad()`: Bloque completo sin grafo

### ¿Cuándo usarlo?

El profesor menciona:

> "Cuando estás en la evaluación [del modelo], no te interesa que este output calcule el grafo computacional, porque no lo vas a usar para nada. Es costoso."

**Uso típico:**

```python
model.eval()  # Modo evaluación

with torch.no_grad():
    predictions = model(test_data)
    accuracy = calcular_accuracy(predictions, test_labels)
```

---

## SECCIÓN O: Arquitectura de Redes - Profundidad vs Anchura

### La pregunta clave

**Estudiante pregunta:**

> "¿Hay alguna regla para decir cuántas capas o neuronas necesito?"

**Respuesta del profesor:**

> "Eh, aquí... Todavía no estoy haciendo deep learning [en mi trabajo]."

> "Lo que sí: buscás si alguien resolvió algo parecido, copiás la arquitectura, y después empezás a ajustar."

### Factores a considerar

**1. Complejidad de la entrada:**

> "Lo que tenés que tener en cuenta es: entendé la complejidad de tu entrada. Si es muy sencillo, no vas a meter muchas capas. Con dos o tres capas con pocas neuronas tenés para resolver."

**2. Cantidad de patrones:**

> "Porque vos lo que puede hacer es capturar patrones de la entrada. Dependiendo de la cantidad del dominio de patrones de la entrada, vas a necesitar [más o menos neuronas]."

### Profundidad vs Anchura

**Concepto importante:**

> "En las redes, son más importantes que sean **profundas** [muchas capas] a que sean **anchas** [muchas neuronas por capa]."

**Analogía del papel:**

> "Te digo: tomá una hoja de papel y hacé 8 cortes en línea. ¿Cuántos cortes conseguís? Ahora te digo: agarrá la hoja, hacé 4 cortes, y a cada corte hacele 4 cortes más. ¿En cuántos casos conseguís más regiones?"

**Respuesta:** Con capas (profundidad), consigues exponencialmente más regiones de separación.

El profesor menciona que hay un video explicando esto geométricamente (lo pasará después).

---

## SECCIÓN P: Learning Rate y Optimizadores

### El rol del learning rate

```python
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)
                                                   ↑
                                            learning rate
```

**Pregunta de estudiante:**

> "El learning rate participa ahí?"

**Respuesta:**

> "Sí, exacto. El learning rate es simplemente un multiplicador. El algoritmo [optimizer] multiplica el gradiente por ese learning rate."

```
peso_nuevo = peso_viejo - lr × gradiente
```

### Problemas con learning rate

**Muy grande:**

> "Si le das muy grande, llegas al tema de no converger. Estás tratando de bajar un valle hasta un mínimo local, y si vas dando saltos muy grandes, podés empezar a rebotar. Bajás, subís, y nunca llegás al mínimo."

**Muy chico:**

> "Cuando el learning rate es muy chiquito, podés ser que estés bajando muy despacio."

### Optimizadores inteligentes (Adam)

El profesor explica que **Adam** es más sofisticado que SGD:

> "De alguna manera usa el concepto de inercia. Si vos ves un cambio rápido [en el loss], trata de avanzar más rápido. Y si ves que no estás incrementando mucho, hace cambios más chicos."

---

## SECCIÓN Q: Funciones de Pérdida

### MSE (Mean Squared Error)

```python
criterion = nn.MSELoss()
```

**Fórmula:**
```
MSE = (1/N) × Σ (predicción - real)²
```

**Código manual (equivalente):**
```python
loss = ((output - y) ** 2).mean()
```

**Explicación del profesor:**

> "Si yo resto esos valores y les saco el cuadrado, mientras ese valor sea lo más chico posible, más voy a estar cerca de mi predicción."

### Ventaja de usar la función nativa

> "Nosotros no regularíamos el loss directamente con funciones, sino que existe directamente esta función implementada en el paquete nn."

---

## SECCIÓN R: `model.train()` vs `model.eval()`

### ¿Por qué se pone dentro del loop?

**Pregunta de estudiante:**

> "¿Por qué `model.train()` está dentro del loop de épocas? ¿No podría ir afuera?"

**Respuesta del profesor:**

> "Muy buena pregunta. Se pone acá porque es muy probable que cada tantas épocas de entrenamiento vos te interese evaluar frente a un validation set."

```python
for epoch in range(epochs):
    model.train()       # Modo entrenamiento
    # ... entrenar ...

    if epoch % 10 == 0:
        model.eval()    # Modo evaluación
        # ... validar ...
```

> "Es defensivo. Para que ustedes se vayan acostumbrando desde el código, de alguna manera va simplemente agregando cosas y no tanto moviendo líneas."

### ¿Cambia algo en este caso?

El profesor aclara:

> "En este caso particular, como tenemos simplemente capas secuenciales y sigmoid, no va a hacer ningún tipo de diferencia."

> "Pero vamos a repasar esto cuando veamos algunas capas especiales como el **dropout** que se comportan ligeramente diferentes si está en modo entrenamiento o en modo evaluación."

---

## SECCIÓN S: Memoria y Eficiencia del Grafo

### Costo de memoria

**Pregunta de estudiante:**

> "Calcular el grafo computacional, ¿es costoso en memoria?"

**Respuesta del profesor:**

> "Claro. Calcular el grafo computacional es algo computacionalmente costoso y aparte el lugar en memoria."

### Solución: No calcular en inferencia

Por eso en **evaluación** (cuando ya no entrenas):

```python
model.eval()
with torch.no_grad():
    predictions = model(test_data)
```

Esto ahorra memoria porque NO construye el grafo computacional.

---

## SECCIÓN T: Dropout y Capas que Cambian Comportamiento

### ¿Qué es Dropout?

El profesor lo menciona brevemente:

> "Dropout es una forma de regularización. Es como esconder nodos y decir: de esta capa, que otros nodos no contribuyan."

**Analogía:**

> "Es algo parecido a lo que vieron [en otra materia]. Es como tener varias redes neuronales juntas."

### Comportamiento diferente

```python
# En entrenamiento:
model.train()
output = model(x)   # Dropout ACTIVO (apaga neuronas al azar)

# En evaluación:
model.eval()
output = model(x)   # Dropout DESACTIVADO (usa todas las neuronas)
```

**Por eso es importante poner `model.train()` y `model.eval()`.**

---

## RESUMEN VISUAL: Todo el Flujo de Entrenamiento

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                         FLUJO COMPLETO DE ENTRENAMIENTO                      ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  PASO 1: INICIALIZACIÓN                                                      ║
║  ┌─────────────────────────────────────────────────────────────────┐         ║
║  │ model = nn.Sequential(...)                                      │         ║
║  │ criterion = nn.MSELoss()                                        │         ║
║  │ optimizer = torch.optim.Adam(model.parameters(), lr=0.1)        │         ║
║  │                                                                 │         ║
║  │ Pesos W y bias b se inicializan ALEATORIAMENTE                  │         ║
║  └─────────────────────────────────────────────────────────────────┘         ║
║                           ▼                                                  ║
║  PASO 2: TRAINING LOOP (por cada época)                                      ║
║  ┌─────────────────────────────────────────────────────────────────┐         ║
║  │ model.train()  ← Modo entrenamiento                             │         ║
║  │                                                                 │         ║
║  │ for epoch in range(1000):                                       │         ║
║  │                                                                 │         ║
║  │   ┌──────────── FORWARD PASS ────────────┐                      │         ║
║  │   │ output = model(x)                    │                      │         ║
║  │   │   • x pasa por nn.Linear(2, 2)       │                      │         ║
║  │   │   • Aplica sigmoid                   │                      │         ║
║  │   │   • Pasa por nn.Linear(2, 1)         │                      │         ║
║  │   │   • Aplica sigmoid                   │                      │         ║
║  │   │   • Construye GRAFO COMPUTACIONAL    │                      │         ║
║  │   └──────────────────────────────────────┘                      │         ║
║  │                  ▼                                               │         ║
║  │   ┌──────────── CALCULAR LOSS ────────────┐                     │         ║
║  │   │ loss = criterion(output, y)           │                     ║
║  │   │   • Resta: (output - y)               │                     ║
║  │   │   • Cuadrado: (...)²                  │                     ║
║  │   │   • Promedio: mean()                  │                     ║
║  │   │   • loss también tiene grafo!         │                     ║
║  │   └──────────────────────────────────────┘                      ║
║  │                  ▼                                               │         ║
║  │   ┌──────────── BACKWARD PASS ────────────┐                     │         ║
║  │   │ optimizer.zero_grad()                 │                     ║
║  │   │   • Limpia gradientes anteriores      │                     ║
║  │   │                                       │                     ║
║  │   │ loss.backward()                       │                     ║
║  │   │   • Recorre el grafo HACIA ATRÁS      │                     ║
║  │   │   • Calcula ∂loss/∂w para cada peso   │                     ║
║  │   │   • Almacena en w.grad, b.grad        │                     ║
║  │   └──────────────────────────────────────┘                      ║
║  │                  ▼                                               │         ║
║  │   ┌──────────── ACTUALIZAR PESOS ─────────┐                     │         ║
║  │   │ optimizer.step()                      │                     ║
║  │   │   • w_nuevo = w_viejo - lr × w.grad   │                     ║
║  │   │   • b_nuevo = b_viejo - lr × b.grad   │                     ║
║  │   │   • (Adam hace ajustes más sofisticad)│                     ║
║  │   └──────────────────────────────────────┘                      ║
║  │                                                                 │         ║
║  │   if epoch % 100 == 0:                                          │         ║
║  │       print(f'Época {epoch}, Loss: {loss.item()}')              │         ║
║  │                                                                 │         ║
║  └─────────────────────────────────────────────────────────────────┘         ║
║                           ▼                                                  ║
║  PASO 3: EVALUACIÓN                                                          ║
║  ┌─────────────────────────────────────────────────────────────────┐         ║
║  │ model.eval()  ← Modo evaluación                                 │         ║
║  │                                                                 │         ║
║  │ with torch.no_grad():  ← No construir grafo                     │         ║
║  │     output = model(x_test)                                      │         ║
║  │     predictions = (output > 0.5).float()                        │         ║
║  └─────────────────────────────────────────────────────────────────┘         ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## CONCEPTOS CLAVE - Glosario

### Términos Básicos

| Término | Explicación | Analogía del Profesor |
|---------|-------------|----------------------|
| **Perceptrón** | Unidad básica: multiplica entradas × pesos + bias | "Es literalmente una multiplicación de matrices" |
| **Función de activación** | Transforma el resultado (ej: sigmoid, sign, ReLU) | "Desdibuja la linealidad" |
| **Linealmente separable** | Problemas que se pueden resolver con UNA línea recta | "Dibujar una recta que separe los puntos" |
| **MLP** | Multi-Layer Perceptron: varias capas de perceptrones | "Perceptrón multicapa" |
| **Época** | Una pasada completa por todos los datos | "Haber pasado todos los datos una vez" |

### Términos de Entrenamiento

| Término | Explicación | Analogía del Profesor |
|---------|-------------|----------------------|
| **Loss function** | Mide qué tan mal está la predicción | "Cuánto me alejé de lo que esperaba" |
| **Optimizer** | Algoritmo que actualiza los pesos | "El responsable de ajustar los pesos" |
| **Learning rate** | Velocidad de ajuste de pesos | "Cuánto del aprendizaje detectado aplicar" |
| **Backward pass** | Calcular gradientes (derivadas) | "Recorrer la red hacia atrás" |
| **Forward pass** | Pasar datos por la red | "Hacer las multiplicaciones matriciales" |

### Términos Avanzados

| Término | Explicación | Analogía del Profesor |
|---------|-------------|----------------------|
| **Grafo computacional** | Historial de operaciones para calcular derivadas | "Saber por dónde pasó para llegar ahí" |
| **require_grad** | Marca tensores para rastrear operaciones | "Indicar que necesita computar el historial" |
| **detach()** | Quitar tensor del grafo computacional | "Entrar en incógnito, no se guarda nada" |
| **torch.no_grad()** | Bloque de código sin rastreo | "Cuando evaluás, no te interesa el grafo" |
| **Broadcasting** | Operar tensores de distintas formas | "Hace que puedan sumarse cosas de distinto shape" |

---

## CÓDIGOS COMPLETOS

### 1. Perceptrón Simple para AND (con bias separado)

```python
import torch
import torch.nn as nn

# Función signo personalizada
def sign(x):
    return torch.where(x >= 0,
                       torch.tensor(1.0),
                       torch.tensor(-1.0))

# Datos
x = torch.tensor([
    [-1, -1],
    [-1,  1],
    [ 1, -1],
    [ 1,  1]
], dtype=torch.float32)

# Pesos y bias
w = torch.tensor([1.0, 1.0], dtype=torch.float32)
b = torch.tensor(-1.0)

# Operación
resultado = sign(torch.matmul(x, w) + b)
print(resultado)  # tensor([-1., -1., -1.,  1.])
```

### 2. Red Neuronal para XOR (con nn.Module)

```python
import torch
import torch.nn as nn

class XorNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.input = nn.Linear(2, 2)
        self.output = nn.Linear(2, 1)

    def forward(self, x):
        x = torch.sigmoid(self.input(x))
        x = torch.sigmoid(self.output(x))
        return x

# Datos
x = torch.tensor([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=torch.float32)

y = torch.tensor([
    [0],
    [1],
    [1],
    [0]
], dtype=torch.float32)

# Modelo
model = XorNet()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)

# Entrenamiento
model.train()
for epoch in range(1000):
    output = model(x)
    loss = criterion(output, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f'Época {epoch}, Loss: {loss.item():.4f}')

# Evaluación
model.eval()
with torch.no_grad():
    predictions = model(x)
    predictions_binary = torch.where(predictions < 0.5,
                                      torch.tensor(0.0),
                                      torch.tensor(1.0))
    print("Predicciones:", predictions_binary.T)
```

### 3. Red con nn.Sequential (equivalente)

```python
model = nn.Sequential(
    nn.Linear(2, 2),
    nn.Sigmoid(),
    nn.Linear(2, 1),
    nn.Sigmoid()
)

# El resto del código es IDÉNTICO
```

### 4. Red para 3 funciones simultáneas (AND, OR, XOR)

```python
# Salida esperada: 3 columnas
y = torch.tensor([
    [0, 0, 0],  # 0,0 → AND=0, OR=0, XOR=0
    [0, 1, 1],  # 0,1 → AND=0, OR=1, XOR=1
    [0, 1, 1],  # 1,0 → AND=0, OR=1, XOR=1
    [1, 1, 0]   # 1,1 → AND=1, OR=1, XOR=0
], dtype=torch.float32)

# Modelo más grande
model = nn.Sequential(
    nn.Linear(2, 4),   # 2 → 4
    nn.Sigmoid(),
    nn.Linear(4, 3),   # 4 → 3
    nn.Sigmoid()
)

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)

# Training loop (igual que antes)
```

---

## DIAGRAMAS ASCII

### Separabilidad Lineal - XOR vs AND

```
╔═══════════════════════════════════════════════════════════════╗
║              ¿POR QUÉ XOR NO ES LINEALMENTE SEPARABLE?        ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║   AND (separable):              XOR (NO separable):           ║
║                                                               ║
║     x₂                             x₂                         ║
║      │                              │                         ║
║    1 │  ○        ⊕                1 │  ⊕        ○             ║
║      │                              │                         ║
║      │ ╱ ← línea                    │    ¿línea?              ║
║    0 ├──────────────── x₁          0 ├──────────────── x₁     ║
║      │╱                             │                         ║
║      │                              │                         ║
║   -1 │  ○        ○                -1 │  ○        ⊕             ║
║      │                              │                         ║
║      └──────────────────            └──────────────────       ║
║     -1        0        1           -1        0        1       ║
║                                                               ║
║   ✓ UNA línea separa                ✗ NO existe UNA línea     ║
║     ○ de ⊕                            que separe ○ de ⊕       ║
║                                                               ║
║   Solución: LEVANTAR a 3D (multicapa)                         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

### Anatomía del Grafo Computacional

```
╔═════════════════════════════════════════════════════════════════╗
║                 GRAFO COMPUTACIONAL EJEMPLO                     ║
║                 x = a*c + b*b                                   ║
╠═════════════════════════════════════════════════════════════════╣
║                                                                 ║
║                         x (resultado = 19)                      ║
║                         │ requires_grad=True                    ║
║                         │ grad_fn=<AddBackward>                 ║
║                         │                                       ║
║                    ┌────┴────┐                                  ║
║                    │         │                                  ║
║                   MUL       ADD  ← OPERACIONES (grises)         ║
║                    │         │                                  ║
║                  ┌─┴─┐    ┌─┴─┐                                ║
║                  │   │    │   │                                 ║
║                  a   c    b   b  ← TENSORES (celestes/hojas)   ║
║                  │   │    │   │                                 ║
║                  5   2    3   3                                 ║
║                                                                 ║
║   Cuando haces x.backward():                                    ║
║   • Calcula ∂x/∂a = c = 2                                       ║
║   • Calcula ∂x/∂b = 2*b = 6                                     ║
║   • Calcula ∂x/∂c = a = 5                                       ║
║                                                                 ║
╚═════════════════════════════════════════════════════════════════╝
```

### Forward Pass vs Backward Pass

```
╔═════════════════════════════════════════════════════════════════╗
║                  FORWARD PASS vs BACKWARD PASS                  ║
╠═════════════════════════════════════════════════════════════════╣
║                                                                 ║
║   FORWARD PASS (output = model(x))                              ║
║   ───────────────────────────────────────────                   ║
║                                                                 ║
║   Input      Capa 1        Capa 2      Output                   ║
║   [0, 1] ──▶ [●  ●] ──▶ sigmoid ──▶ [●] ──▶ sigmoid ──▶ 0.987  ║
║              ↑                       ↑                           ║
║           W₁, b₁                  W₂, b₂                         ║
║                                                                 ║
║   • Multiplica: X @ W₁ + b₁                                     ║
║   • Activa: sigmoid(...)                                        ║
║   • Multiplica: ... @ W₂ + b₂                                   ║
║   • Activa: sigmoid(...)                                        ║
║   • Guarda TODO en el grafo computacional                       ║
║                                                                 ║
║   ═══════════════════════════════════════════════════════       ║
║                                                                 ║
║   BACKWARD PASS (loss.backward())                               ║
║   ─────────────────────────────────────                         ║
║                                                                 ║
║   0.987 (pred)                                                  ║
║   1.000 (real)       ← Loss = (0.987 - 1.0)² = 0.000169        ║
║                                                                 ║
║   Output      Capa 2        Capa 1      Input                   ║
║   0.987 ◀── [●] ◀── sigmoid ◀── [●  ●] ◀── [0, 1]              ║
║              ↓                       ↓                           ║
║           ∂L/∂W₂                 ∂L/∂W₁  ← GRADIENTES            ║
║           ∂L/∂b₂                 ∂L/∂b₁                          ║
║                                                                 ║
║   • Usa la regla de la cadena                                   ║
║   • Calcula ∂Loss/∂peso para cada peso                          ║
║   • Almacena en W.grad, b.grad                                  ║
║                                                                 ║
║   ═══════════════════════════════════════════════════════       ║
║                                                                 ║
║   OPTIMIZER STEP (optimizer.step())                             ║
║   ───────────────────────────────────────────                   ║
║                                                                 ║
║   W₁_nuevo = W₁_viejo - lr × ∂L/∂W₁                             ║
║   b₁_nuevo = b₁_viejo - lr × ∂L/∂b₁                             ║
║   W₂_nuevo = W₂_viejo - lr × ∂L/∂W₂                             ║
║   b₂_nuevo = b₂_viejo - lr × ∂L/∂b₂                             ║
║                                                                 ║
╚═════════════════════════════════════════════════════════════════╝
```

---

## CONSEJOS DEL PROFESOR

### Sobre arquitecturas

> "La parte de cuántas neuronas pongo y cuántas capas es algo más artesanal."

> "Buscás si alguien resolvió algo parecido, copiás la arquitectura, y después empezás a ajustar."

> "En las redes, son más importantes que sean **profundas** a que sean **anchas**."

### Sobre entrenamiento

> "Si las redes neuronales no tienen problemas de cálculo numérico [vanishing/exploding gradient], están condenadas a aprender."

> "Es importante que los datos estén bien. Si tenés un dato que te dice 'A lleva a B' y otro que dice 'A lleva a C', ya tenés un problema allá de datos."

### Sobre learning rate

> "Si es muy grande, podés no converger. Si es muy chico, vas bajando muy despacio."

> "Hay valores que ya están estudiados intensamente."

### Sobre optimización

> "Al principio es totalmente aleatorio. A medida que vas entrenando, la loss va bajando."

> "El optimizer hace cambios. Pero qué pasa: como la entrada va cambiando, va desajustando. Hiciste reducir el error para esta entrada, pero cuando viene otra entrada, esos valores no te sirven tanto. Estás haciendo reducir el **error promedio**."

---

## ERRORES COMUNES Y CÓMO EVITARLOS

### Error 1: No llamar `optimizer.zero_grad()`

```python
# ✗ MALO
for epoch in range(100):
    output = model(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()   # Los gradientes se acumulan!
```

```python
# ✓ BUENO
for epoch in range(100):
    output = model(x)
    loss = criterion(output, y)
    optimizer.zero_grad()  # Limpia primero
    loss.backward()
    optimizer.step()
```

### Error 2: Usar -1/1 con sigmoid

```python
# ✗ MALO (sigmoid da valores entre 0 y 1)
y = torch.tensor([[-1], [1], [1], [-1]])
criterion = nn.MSELoss()  # La red nunca llegará a -1
```

```python
# ✓ BUENO
y = torch.tensor([[0], [1], [1], [0]])
criterion = nn.MSELoss()  # Ahora sí puede llegar
```

### Error 3: Olvidar poner tipos correctos

```python
# ✗ MALO
x = torch.tensor([[0, 1], [1, 0]])  # dtype=int64 por defecto
```

```python
# ✓ BUENO
x = torch.tensor([[0, 1], [1, 0]], dtype=torch.float32)
```

### Error 4: No usar `model.eval()` en inferencia

```python
# ✗ MALO (Dropout sigue activo, no_grad no está)
predictions = model(test_data)
```

```python
# ✓ BUENO
model.eval()
with torch.no_grad():
    predictions = model(test_data)
```

---

## RECURSOS ADICIONALES (mencionados en clase)

### Notebooks extra (NO obligatorios):

1. **Gradientes y optimizadores:** Explicación paso a paso de cómo funciona el backward y el optimizer
2. **Precisión float16 vs float32:** Comparativas de entrenamiento, errores con diferentes precisiones

### Video mencionado:

- **"Por qué profundidad > anchura"**: Explicación visual de cómo las capas profundas consiguen exponencialmente más regiones de separación que las anchas.

### Herramienta:

- **torchviz**: Visualizar grafos computacionales (instalar con `pip install torchviz`)

---

## PREGUNTAS Y RESPUESTAS DE CLASE

### P: "¿El bias siempre tiene que ser -1?"

**R:** No, los pesos no son únicos. El profesor mostró varios ejemplos:

```python
# Opción 1:
w = [0.5, 0.5], b = -1.0

# Opción 2 (también funciona):
w = [3.0, 7.0], b = -1.3

# Opción 3:
w = [1.0, 1.0], b = -0.5
```

### P: "¿Los parámetros del grafo tienen nombre?"

**R:** No, el grafo solo sabe el origen de cada tensor, no el nombre de las variables que usaste en Python.

> "Sabe que tiene un origen, pero no sabe cómo se llama. Yo le puedo poner 'pepe' acá y va a poner 'pepe' en el grafo."

### P: "Si un dato cambia mucho los parámetros, ¿tiene historial de cambios anteriores?"

**R:** No, solo guarda el estado actual de los pesos. Pero optimizadores como **Adam** usan un concepto de "inercia" (momentum) que considera cambios recientes.

---

## LO MÁS IMPORTANTE DE ESTA CLASE

### 1. Conceptos históricos:
- El perceptrón simple NO puede resolver XOR
- Esto causó el "invierno de la IA" en los años 70
- La solución es usar **múltiples capas** (MLP)

### 2. Implementación práctica:
- Dos formas de definir redes: `nn.Module` y `nn.Sequential`
- Training loop: forward → loss → backward → step
- Siempre llamar `optimizer.zero_grad()` antes del backward

### 3. Grafo computacional:
- PyTorch rastrea operaciones automáticamente
- `require_grad=True` activa el rastreo
- Es costoso en memoria, desactivarlo en inferencia con `torch.no_grad()`

### 4. Arquitecturas:
- No hay reglas fijas para número de neuronas/capas
- **Profundidad > Anchura** (más capas es mejor que más neuronas)
- Copiar arquitecturas conocidas y ajustar

### 5. Optimización:
- Learning rate controla velocidad de aprendizaje
- Adam es más sofisticado que SGD (usa inercia)
- Las redes "están condenadas a aprender" si los datos son buenos

---

## PRÓXIMA CLASE

El profesor menciona que el lunes darán estos temas con más profundidad, probablemente:
- Más sobre optimizadores (SGD, Adam, RMSprop)
- Regularización (Dropout, BatchNorm)
- Overfitting y validation

---

**FIN DEL DOCUMENTO - CLASE 2 (27 de Agosto 2025)**

📌 **Nota:** Este documento cubre TODA la transcripción de 2460 líneas de la clase del 27 de agosto de 2025. Todos los temas dictados por el profesor están explicados aquí con máximo detalle.
