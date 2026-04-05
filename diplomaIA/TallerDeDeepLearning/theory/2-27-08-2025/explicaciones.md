# Clase 2 (27 de Agosto 2025) - Taller Deep Learning
## Perceptrón, Operaciones Lógicas y Redes Neuronales Multi-Capa

---

# UBICACIÓN EN EL CURSO: ¿De dónde venimos y hacia dónde vamos?

```
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                           INICIO DEL CURSO - MAPA DE CLASES                              ║
╠══════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                          ║
║  CLASE 1 (20-Ago) ─────────────────────────────────────────────────────────────────────  ║
║  │  • PyTorch: Tensores, operaciones, broadcasting                                       ║
║  │  • GPU vs CPU                                                                         ║
║  │  • Indexing y slicing                                                                 ║
║  │  • Eficiencia computacional                                                           ║
║  │                                                                                       ║
║  ▼  CONEXIÓN: Ya sabemos crear y manipular tensores                                      ║
║                                                                                          ║
║  ════════════════════════════════════════════════════════════════════════════════════    ║
║  ║ CLASE 2 (27-Ago) ◄─── ESTÁS AQUÍ                                              ║      ║
║  ║  • Perceptrón: el bloque básico de las redes neuronales                       ║      ║
║  ║  • Operaciones lógicas: AND, OR, XOR                                           ║      ║
║  ║  • El problema del XOR: límites del perceptrón simple                          ║      ║
║  ║  • Redes Multi-Capa (MLP): resolviendo XOR                                     ║      ║
║  ║  • Training Loop: forward, loss, backward, optimizer                           ║      ║
║  ║  • Grafos computacionales: cómo PyTorch aprende                                ║      ║
║  ════════════════════════════════════════════════════════════════════════════════════    ║
║  │                                                                                       ║
║  ▼  PROBLEMA CENTRAL: ¿Cómo hacer que una red aprenda automáticamente?                  ║
║                                                                                          ║
║  PRÓXIMAS CLASES ──────────────────────────────────────────────────────────────────────  ║
║     • Convoluciones (CNNs)                                                               ║
║     • Redes Recurrentes (RNNs)                                                           ║
║     • Regularización (Dropout, BatchNorm)                                                ║
║     • Optimización avanzada                                                              ║
║                                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
```

---

## MAPA CONCEPTUAL DE ESTA CLASE: ¿Cómo se conectan los temas?

```
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                    PROBLEMA CENTRAL: IMPLEMENTAR OPERACIONES LÓGICAS                 ║
║                                                                                      ║
║    ¿Cómo hacer que una red aprenda AND, OR, XOR automáticamente?                     ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
                                          │
        ┌─────────────────────────────────┼─────────────────────────────────┐
        │                                 │                                 │
        ▼                                 ▼                                 ▼
╔═══════════════════╗          ╔═══════════════════╗          ╔═══════════════════╗
║  ENFOQUE MANUAL   ║          ║ EL GRAN PROBLEMA  ║          ║ SOLUCIÓN NEURONAL ║
║  (calcular pesos) ║          ║     (XOR)         ║          ║  (aprender pesos) ║
║                   ║          ║                   ║          ║                   ║
║ • Perceptrón      ║───────▶  ║ • No linealmente  ║───────▶  ║ • Multi-capa MLP  ║
║ • Multiplicación  ║          ║   separable       ║          ║ • Activación      ║
║   matricial       ║          ║ • Necesita más    ║          ║ • Training loop   ║
║ • Función signo   ║          ║   capas           ║          ║ • Backpropagation ║
╚═══════════════════╝          ╚═══════════════════╝          ╚═══════════════════╝
         │                              │                              │
         ▼                              │                              │
╔═══════════════════╗                   │                              │
║    RESOLVEMOS:    ║                   │                              │
║ • AND (manual)    ║                   │                              │
║ • OR (manual)     ║ ──────────────────▶│                              │
║ • NOT (manual)    ║    NO funciona     │                              │
╚═══════════════════╝    para XOR       │                              │
                                         │                              │
        ┌────────────────────────────────┘                              │
        │                                                               │
        ▼                                                               │
╔══════════════════════════════════════════════════════════════════════════════════════╗
║              ¿POR QUÉ EL XOR NO FUNCIONA CON PERCEPTRÓN SIMPLE?                      ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                      ║
║   El perceptrón = encontrar una RECTA que separe los puntos                          ║
║                                                                                      ║
║   Ecuación: W·X + b = 0  (esto es una recta en 2D)                                   ║
║                                                                                      ║
║   XOR en el plano:                                                                   ║
║        (0,0) → 0  ●──────────●  (1,1) → 0                                            ║
║                   │          │                                                       ║
║                   │          │                                                       ║
║        (0,1) → 1  ●──────────●  (1,0) → 1                                            ║
║                                                                                      ║
║   ⚠️ IMPOSIBLE trazar UNA recta que separe los puntos del mismo color               ║
║      Están en diagonal cruzada (no linealmente separable)                            ║
║                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
        │
        │  SOLUCIÓN: Agregar más capas para "doblar" el espacio
        │
        ▼
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                      RED MULTI-CAPA (MLP) - LA SOLUCIÓN                              ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                      ║
║   Arquitectura:  ENTRADA → CAPA OCULTA → CAPA SALIDA                                 ║
║                     2         4 neuronas      1                                      ║
║                                                                                      ║
║   Con funciones de activación NO lineales (sigmoid, ReLU)                            ║
║   podemos transformar el espacio y separar los puntos                                ║
║                                                                                      ║
║   Analogía: "Levantar una hoja de papel para que los puntos se separen"             ║
║                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

---

## SECCIÓN A: El Perceptrón - El Bloque Básico

### ¿Qué es un perceptrón?

> "Básicamente la forma que vamos a iniciar tímidamente es simplemente con una multiplicación de matrices."

Un **perceptrón** es la unidad más básica de una red neuronal. Es una neurona artificial que:
1. Recibe entradas (X)
2. Las multiplica por pesos (W)
3. Suma un sesgo o bias (b)
4. Aplica una función de activación

### La fórmula matemática

```
salida = función_activación(X · W + b)
```

Donde:
- **X** = entrada (por ejemplo, [0, 1] para una operación lógica)
- **W** = pesos (valores que queremos encontrar)
- **b** = bias o sesgo (desplazamiento)
- **función_activación** = transforma el resultado (por ejemplo, función signo)

### Función de activación: SIGNO

> "Cuando nosotros tenemos una respuesta negativa, daríamos un menos uno. En el caso de que sea una respuesta positiva, los ceros con cinco, digamos positiva, no?"

El profesor definió una función **signo personalizada** porque la de PyTorch se comporta diferente:

```python
def signo(x):
    return torch.where(x >= 0, torch.tensor(1.0), torch.tensor(-1.0))
```

**Comportamiento:**
- Si x ≥ 0 → devuelve +1
- Si x < 0 → devuelve -1

**Diferencia con torch.sign():**
- `torch.sign(0)` = 0
- Nuestra `signo(0)` = +1

### ¿Por qué esta función?

> "En nuestro caso particular, sin nuestra cuenta da exactamente cero, devuélveme +1 para eso."

Necesitamos que cuando el resultado sea exactamente 0, se clasifique como positivo (True).

---

## SECCIÓN B: Operación AND - Primer Ejemplo

### Tabla de verdad del AND

| X₁ (entrada 1) | X₂ (entrada 2) | Salida |
|---------------|---------------|--------|
| -1 (False)    | -1 (False)    | -1 (False) |
| -1 (False)    | +1 (True)     | -1 (False) |
| +1 (True)     | -1 (False)    | -1 (False) |
| +1 (True)     | +1 (True)     | +1 (True) |

**Interpretación:** Solo cuando AMBOS son True (1), la salida es True (1).

### Implementación manual (Forma 1: con bias incluido)

> "Nosotros hemos que encontrar aquellos pesos que multiplicado a nuestro X nos de nuestro resultado."

```python
# ENTRADA: incluye un 1 extra para el bias
X = torch.tensor([
    [-1, -1, 1],   # False AND False
    [-1,  1, 1],   # False AND True
    [ 1, -1, 1],   # True AND False
    [ 1,  1, 1],   # True AND True
], dtype=torch.float32)

# PESOS: encontrados manualmente
W = torch.tensor([0.5, 0.5, -1], dtype=torch.float32)

# OPERACIÓN
resultado = signo(torch.matmul(X, W))
# Devuelve: [-1, -1, -1, 1] ✓
```

**¿Cómo funcionan estos pesos?**

Veamos caso por caso:

1. **(-1, -1, 1) · (0.5, 0.5, -1)** = -0.5 - 0.5 - 1 = **-2** → signo = **-1** ✓
2. **(-1, +1, 1) · (0.5, 0.5, -1)** = -0.5 + 0.5 - 1 = **-1** → signo = **-1** ✓
3. **(+1, -1, 1) · (0.5, 0.5, -1)** = 0.5 - 0.5 - 1 = **-1** → signo = **-1** ✓
4. **(+1, +1, 1) · (0.5, 0.5, -1)** = 0.5 + 0.5 - 1 = **0** → signo = **+1** ✓

### Implementación manual (Forma 2: bias separado)

> "Capaz que estaría un poco mejor dejarlo un poco más separado."

```python
# ENTRADA: solo los valores reales
X = torch.tensor([
    [-1, -1],
    [-1,  1],
    [ 1, -1],
    [ 1,  1]
], dtype=torch.float32)

# PESOS Y BIAS SEPARADOS
W = torch.tensor([1.0, 1.0], dtype=torch.float32)
b = torch.tensor(-1.0)

# OPERACIÓN
resultado = signo(torch.matmul(X, W) + b)
```

### Dos formas de multiplicar matrices

> "Para multiplicar matrices hay dos formas."

```python
# Forma 1: función torch.matmul
resultado = torch.matmul(X, W)

# Forma 2: operador @
resultado = X @ W

# Ambas son equivalentes
```

---

## SECCIÓN C: Operación OR - Ejercicio Guiado

### Tabla de verdad del OR

| X₁ | X₂ | Salida |
|----|----|----|
| -1 | -1 | -1 |
| -1 | +1 | +1 |
| +1 | -1 | +1 |
| +1 | +1 | +1 |

**Interpretación:** Cuando AL MENOS UNO es True, la salida es True.

### Solución encontrada por los estudiantes

> "Una de las formas más conocidas... es, por ejemplo, poner uno uno menos uno."

```python
W = torch.tensor([1.0, 1.0, -1.0], dtype=torch.float32)
```

**¿Por qué funciona?**

- Cuando ambos son 0 (False): `0 + 0 - 1 = -1` (negativo) → **-1** ✓
- Cuando uno es positivo: `1 + 0 - 1 = 0` → con signo = **+1** ✓
- Cuando ambos son positivos: `1 + 1 - 1 = 1` (positivo) → **+1** ✓

### Concepto clave: No hay pesos únicos

> "Obviamente estos no son valores únicos. O sea, yo puedo tener otros pesos de W que me puedan cumplir."

El profesor demostró que también funcionan otros valores como `[3, 7, -1.3]`.

**Conclusión:** Hay MÚLTIPLES conjuntos de pesos que resuelven el mismo problema.

---

## SECCIÓN D: El Problema del XOR - El "Invierno" de la IA

### Tabla de verdad del XOR

> "La tabla de verdad de léor es solo si uno de los dos es true. No puede pasar de que ninguno de ambos o ambos que ambos sean fos va dar fos."

| X₁ | X₂ | Salida | Explicación |
|----|----|----|------------|
| 0  | 0  | 0  | Ninguno es True → False |
| 0  | 1  | 1  | Solo uno es True → True |
| 1  | 0  | 1  | Solo uno es True → True |
| 1  | 1  | 0  | Ambos son True → False |

**XOR = "O exclusivo"** (uno u otro, pero NO ambos).

### El gran descubrimiento histórico

> "El gran problema que tiene el léor... es que vino una época oscura porque se demostró que no es linealmente separable."

> "Es imposible que ustedes se encuentren los pesos de acá de tal manera que se pueda obtener este resultado."

### ¿Qué significa "linealmente separable"?

> "El perceptrón básicamente aplica... W·X + b. Cuando vos haces eso que tiene dos dimensiones, una persona los X más b igual el cero, son todos los puntos que están aquí de la recta."

**Explicación simple:**
1. Un perceptrón dibuja una **RECTA** (o un plano en más dimensiones)
2. Todo de un lado de la recta es una clase (True)
3. Todo del otro lado es otra clase (False)

**Para XOR:**
```
Plano X₁-X₂:

(0,1) → 1       (1,1) → 0
    ●               ○

    ●               ○
(0,0) → 0       (1,0) → 1
```

Los puntos están en **diagonal cruzada**. No hay forma de trazar UNA recta que separe los ● de los ○.

### El "Invierno de la IA" - Historia

> "Era en la época donde... se demostró que no es linealmente separable... entonces no tiene tanta potencia."

El profesor explicó el contexto histórico:

**1950s-1960s:** Gran entusiasmo
- Frank Rosenblatt crea el Perceptrón
- Se pensaba resolver IA en 10 años
- Financiamiento militar (DARPA, Departamento de Defensa USA)

**1969:** El libro de Minsky y Papert
> "Después ese de libro perrón de de Popes lo del leor el le le puso la cruz."

- Marvin Minsky y Seymour Papert publican "Perceptrons"
- Demuestran matemáticamente que el perceptrón NO puede resolver XOR
- Conclusión: "Si no puede hacer algo tan simple, ¿cómo hará cosas complejas?"

**Consecuencias:**
- Cae el financiamiento
- "Invierno de la IA" (AI Winter)
- Investigación estancada por décadas

### Reflexión del profesor sobre expectativas

> "Somos muy malos estimando el tiempo... sobre estimamos lo que puedo hacer en un día y subestimamos lo que podemos hacer en 10 años."

Citó a Bill Gates sobre expectativas de tecnología.

---

## SECCIÓN E: La Solución - Redes Multi-Capa (MLP)

### La intuición geométrica

> "Sería preferida... ver si doblando el plano se decir una solución, por ejemplo, que el madad es los puntos rojos. Le levanto mira tu un carne."

**Analogía:** Si no puedes separar puntos en un papel plano con una línea, **levanta el papel** en 3D. Ahora sí puedes separarlos.

### ¿Qué hace la capa oculta?

> "Por eso decían que ponga capa más... podrías una forma de levantar el francés."

Las capas ocultas **transforman el espacio** a una dimensión donde sí es posible separar los puntos.

### Arquitectura propuesta

```python
class XORNet(nn.Module):
    def __init__(self):
        super().__init__()
        # Capa 1: de 2 entradas a 4 neuronas ocultas
        self.input = nn.Linear(2, 4)
        # Capa 2: de 4 neuronas a 1 salida
        self.output = nn.Linear(4, 1)

    def forward(self, x):
        # Pasar por capa 1 + activación
        x = self.input(x)
        x = torch.sigmoid(x)
        # Pasar por capa 2 + activación
        x = self.output(x)
        x = torch.sigmoid(x)
        return x
```

### Forma alternativa: nn.Sequential

> "Hay uno que le gusta, eh, utilizar el secuencia no, sobre todo para cosas que son no muy compleja."

```python
model = nn.Sequential(
    nn.Linear(2, 4),      # Entrada → Oculta
    nn.Sigmoid(),         # Activación
    nn.Linear(4, 1),      # Oculta → Salida
    nn.Sigmoid()          # Activación final
)
```

**Diferencia:**
- `XORNet` → Define arquitectura + forward explícito
- `nn.Sequential` → Pipeline automático (más simple para redes lineales)

### ¿Cuántas neuronas y capas usar?

**Pregunta de estudiante:** "¿Cómo saber cuántas neuronas poner?"

> "Es un poco en lo que es el arte... la alquimia... Uno pensaría de que mientras más neuronas y mientras más capas le demos esto va a funcionar mejor. Eso no necesariamente tiene que ser así."

**Respuesta del profesor:**
- No hay fórmula mágica
- Depende del problema y la experiencia
- Más grande NO siempre es mejor (riesgo de overfitting)
- **Estrategia:** Buscar en papers similares y adaptar

### Profundidad vs Ancho

> "En las redes son más importantes que sean profundas juntas a que sean anchas."

**Analogía del papel:**
> "Yo te digo toma una hoja de papel y hacer de ocho cortes. Si ocho personas sí. Cuántos cortes ahora? Yo te digo agarr la hace cuatro cortes. Y a cada corte hacer cuatro cortes más."

- **Ancho** (muchas neuronas en una capa): Hace cortes en paralelo
- **Profundo** (muchas capas): Hace cortes secuenciales, más regiones

**Redes profundas** capturan más patrones complejos con menos neuronas totales.

---

## SECCIÓN F: El Training Loop - Cómo Aprende la Red

### Problema: Pesos aleatorios

> "Al final de todo son pesos que son tensores... la salida va a ser nómada al principio."

Cuando creamos una red, los pesos se inicializan **aleatoriamente**. La salida inicial es basura.

**Demostración del profesor:**
```python
net = XORNet()
output = net(X)
# Resultado: [0.43, 0.46, 0.45, 0.42]
# Esperado:  [0,    1,    1,    0   ]
```

¡Totalmente incorrecto!

### Los 3 componentes esenciales

**1. Función de pérdida (Loss Function)**
```python
criterion = nn.MSELoss()  # Mean Squared Error
```

> "De alguna manera puedo hacer una función de pérdida que alinee el resultado o... cuando yo minimizo la loss... se acerca mejor."

**¿Qué hace?**
- Compara la predicción con el valor esperado
- Devuelve un número: **qué tan mal está**
- Mientras más chico → mejor

**2. Optimizador**
```python
optimizer = torch.optim.SGD(model.parameters(), lr=1.0)
```

> "Nosotros lo que hicimos... es tomar los pesos de cada uno de las matrices y calculados a mano... como esto es machine learning... puedo delegar esa responsabilidad de actualizar los pesos... a un optimizador."

**¿Qué hace?**
- Ajusta los pesos para **reducir** la loss
- Usa el gradiente (derivadas) para saber en qué dirección moverse
- **Learning rate (lr):** cuánto ajustar en cada paso

**3. Training Loop**

El ciclo completo:

```python
model.train()  # Poner en modo entrenamiento

for epoch in range(1000):  # 1000 épocas
    # 1. FORWARD PASS: calcular predicción
    output = model(X)

    # 2. LOSS: calcular error
    loss = criterion(output, y_esperado)

    # 3. BACKWARD PASS: calcular gradientes
    optimizer.zero_grad()  # Limpiar gradientes anteriores
    loss.backward()        # Calcular gradientes

    # 4. OPTIMIZER STEP: actualizar pesos
    optimizer.step()

    # Imprimir progreso
    if epoch % 100 == 0:
        print(f"Época {epoch}, Loss: {loss.item()}")
```

### Paso a paso: ¿Qué ocurre internamente?

**Paso 1: Forward Pass**
> "Toma dos matrices, las multiplica materialmente y añade el bias."

```
X (entrada) → Capa1 → Activación → Capa2 → Activación → Output
```

**Paso 2: Calcular Loss**
```python
loss = (output - target)²
```

**Paso 3: Backward Pass**
> "El backward... va recorriendo la red de la capa de salida hasta la capa de entrada y calcular los gradientes."

**¿Qué es un gradiente?**
- Es la **derivada** de la loss respecto a cada peso
- Indica: "Si aumento este peso en 0.1, ¿cuánto cambia la loss?"

**Paso 4: Optimizer Step**
> "El optimizer es el que toma cada uno de esos gradientes... y termina actualizando los pesos."

```python
# Simplificado (lo que hace SGD internamente):
peso_nuevo = peso_viejo - learning_rate * gradiente
```

### ¿Por qué funciona?

> "Están condenados a aprender... porque el algoritmo que tienen es lo que hace decir trata reducir las pérdidas."

El algoritmo **siempre** mejora (si no hay problemas numéricos):
1. Calcula qué tan mal está
2. Calcula en qué dirección mejorar (gradientes)
3. Se mueve en esa dirección
4. Repite hasta que el error sea aceptablemente bajo

---

## SECCIÓN G: Grafos Computacionales - El Secreto de PyTorch

### ¿Qué es require_grad?

> "Una de las propiedades que puede poner... es que requiere grad."

```python
a = torch.tensor(3.0, requires_grad=True)
b = torch.tensor(2.0, requires_grad=True)
c = torch.tensor(1.0, requires_grad=True)

x = a * c + b * b  # x = 3*1 + 2*2 = 7
```

**¿Qué hace `requires_grad=True`?**
> "Le estás diciendo de que en el momento yo voy a operar bajo estos tensores, yo tengo que ir calculando cómo fue llegado el resultado."

PyTorch guarda un **historial** de operaciones.

### El grafo computacional

> "Ese historial de cómo llegó atrás, eso es lo que hace lo que hace pay que hace forma automática."

Cada tensor resultante sabe:
- Su valor (7)
- Qué operaciones se usaron (multiplicación, suma)
- Qué tensores participaron (a, b, c)

### ¿Para qué sirve esto?

> "Si vos sabes todos los elementos que pasaron a través de y que operaciones hubo, de alguna manera puedes encontrar el culpable o qué tanto podés ajustar cada uno de estos elementos."

**Aplicado a redes:**
1. La red predice 0.43, debería ser 0.0
2. Loss = (0.43 - 0.0)² = 0.1849
3. El grafo sabe que 0.43 vino de Capa2 que vino de Capa1
4. PyTorch calcula: "¿Cuánto cambio W₁ y W₂ para reducir la loss?"

### Backward propagation

```python
loss.backward()  # Calcula todos los gradientes automáticamente
```

Recorre el grafo **al revés** (desde la salida hasta la entrada).

### Redes neuronales tienen grad activado automáticamente

> "Cuando vos en las redes neuronales, todas estas capas por efecto por atrás ya tienen hay en True."

```python
model = nn.Linear(2, 4)
# Los pesos internos YA tienen requires_grad=True automáticamente
```

### Detach: Cortar el historial

> "El detach vos sacalo de grafo computacional... pierdo el historial de cómo ya llegué ahí."

```python
x = tensor_con_historial.detach()
# x ahora NO tiene grafo computacional
```

**Analogía del profesor:**
> "Es como cuando entrar en incógnito, no se guarda nada."

---

## PUNTOS CLAVE PARA RECORDAR

1. ✅ **Perceptrón = multiplicación matricial + activación**
2. ✅ **XOR no es linealmente separable** (necesita multi-capa)
3. ✅ **Training loop:** forward → loss → backward → step
4. ✅ **Always call `optimizer.zero_grad()`** antes de backward
5. ✅ **Grafos computacionales** guardan historial automáticamente
6. ✅ **Backward** calcula gradientes de forma automática
7. ✅ **Optimizer** usa gradientes para ajustar pesos
8. ✅ **Learning rate** controla velocidad de aprendizaje
9. ✅ **Sigmoid** introduce no linealidad (permite aprender XOR)
10. ✅ **model.train() / model.eval()** para cambiar modos

---

## CÓDIGO COMPLETO - RESOLVIENDO XOR

```python
import torch
import torch.nn as nn

# Paso 1: Definir datos
X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

# Paso 2: Definir modelo
model = nn.Sequential(
    nn.Linear(2, 4),
    nn.Sigmoid(),
    nn.Linear(4, 1),
    nn.Sigmoid()
)

# Paso 3: Definir loss y optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1.0)

# Paso 4: Training loop
model.train()
for epoch in range(1000):
    output = model(X)
    loss = criterion(output, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Época {epoch}, Loss: {loss.item():.4f}")

# Paso 5: Evaluar
model.eval()
with torch.no_grad():
    predicciones = model(X)
    clases = torch.round(predicciones)
    print(clases)  # [[0], [1], [1], [0]] ✓
```

---

## SECCIÓN H: Preguntas de Estudiantes (Respuestas del Profesor)

### "¿Cómo se entera el optimizador de la función de pérdida?"

> "Por el backward. Técnicamente funciona de esta manera: en esa etapa solamente estás declarando quién es quién. Cuando llamas al backward, se calculan los gradientes en cada peso. Después el optimizer.step() usa esos gradientes."

**Respuesta corta:** El optimizador NO conoce directamente la función de pérdida. La conexión es:
1. `loss.backward()` calcula los gradientes y los guarda en cada peso
2. `optimizer.step()` lee esos gradientes y actualiza los pesos

### "¿Por qué se pone model.train() dentro del loop?"

> "Es defensivo. Es muy probable que cada tantas épocas de entrenamiento te interese evaluar frente a tu set de validación. Y cuando estás evaluando lo pones en model.eval(). Entonces por las dudas lo ponemos al inicio del loop."

### "¿El optimizador siempre mejora?"

> "Lo que trata de hacer la red es optimizar. Pero como la entrada va cambiando, se va desajustando. Lo que hiciste bien para una entrada, no te sirve para otra. Estás haciendo un ajuste promedio."

> "Si no tenés problemas de cálculo numérico como el vanishing gradient o exploding gradient, las redes neuronales están condenadas a aprender."

### "¿Cuántas neuronas y capas necesito?"

> "Básicamente lo que se suele hacer es buscar si alguien resolvió algo parecido, copiar la arquitectura, y después empezar a ajustar."

> "Las redes son más importantes que sean profundas que anchas. Hay un video que explica cómo se ve el plano de entrada: más capas te dan más fronteras de decisión."

### "¿Qué pasa si mis datos tienen contradicciones?"

> "Si tenés un dato que dice 'A lleva a B' y otro que dice 'A lleva a C', ya tenés un problema más allá de la red. Es un problema de datos. Por eso es tan importante que los datos estén bien."

---

## SECCIÓN I: Conceptos Adicionales Importantes

### Épocas vs Iteraciones

> "Una época es haber pasado todos los datos una vez."

```
┌──────────────────────────────────────────────────────────────────┐
│                    ÉPOCAS Y BATCHES                              │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Si tienes 1000 datos y batches de 100:                         │
│                                                                  │
│  1 ÉPOCA = 10 iteraciones (batches)                             │
│                                                                  │
│  Cada época = pasar TODOS los datos una vez                     │
│  Cada iteración = pasar UN BATCH de datos                       │
│                                                                  │
│  "Cada época ajustás un poco más los pesos"                     │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Learning Rate: Muy Grande vs Muy Chico

> "El learning rate es simplemente una tasa de aprendizaje. Te dice cuánto del aprendizaje que detectaste vas a aplicar."

```
┌──────────────────────────────────────────────────────────────────┐
│              LEARNING RATE: ANALOGÍA DE LA MONTAÑA               │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Imagina que bajas una montaña buscando el punto más bajo:      │
│                                                                  │
│  LR MUY GRANDE:                 LR MUY CHICO:                   │
│                                                                  │
│      ╱╲                            ╱╲                           │
│     ╱  ╲     ← → saltos           ╱  ╲                          │
│    ╱    ╲    muy grandes         ╱ ·  ╲   pasitos               │
│   ╱      ╲   (oscilás)          ╱  ·   ╲  muy lentos            │
│  ╱   ●    ╲                    ╱   ·    ╲                       │
│ ╱    ↑↓    ╲                  ╱    ·     ╲                      │
│     nunca llegas               tardás mucho                     │
│                                                                  │
│  "Podés empezar a oscilar,    "Bajás muy despacio y            │
│   bajas y subís sin llegar     tardás mucho en converger"      │
│   nunca al mínimo"                                              │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Adam vs SGD

> "Adam de alguna manera usa el concepto de inercia. Si ve un cambio rápido, trata de avanzar más rápido. Y si ve que no estás incrementando mucho, hace cambios más chicos."

| Optimizador | Comportamiento | Cuándo usar |
|-------------|---------------|-------------|
| **SGD** | Pasos constantes | Problemas simples, más control |
| **Adam** | Adapta el paso automáticamente | Recomendado para empezar |

### NAND y NOR (Mencionados brevemente)

El profesor mencionó que NAND y NOR tienen los **pesos negativos** de AND y OR:

| Operación | Pesos (ejemplo) |
|-----------|-----------------|
| AND | [0.5, 0.5, -1.0] |
| NAND | [-0.5, -0.5, 1.0] |
| OR | [1.0, 1.0, -1.0] |
| NOR | [-1.0, -1.0, 1.0] |

> "El NOT XOR tampoco es linealmente separable. Tiene el mismo problema que XOR."

### torch.no_grad() vs detach()

| Método | Uso | Efecto |
|--------|-----|--------|
| `torch.no_grad()` | Context manager | No calcula gradientes dentro del bloque |
| `.detach()` | Método de tensor | Crea copia SIN historial |

```python
# Durante evaluación (más eficiente)
with torch.no_grad():
    output = model(x)
    # No se calcula grafo → más rápido, menos memoria

# Para usar valor sin afectar entrenamiento
valor_fijo = tensor_entrenando.detach()
```

---

## SECCIÓN J: Ejercicio Final - Tres Operaciones Simultáneas

> "Lo que vamos a hacer ahora es resolver AND, OR y XOR al mismo tiempo."

El desafío final de la clase fue crear una red que resuelva las tres operaciones con una sola arquitectura:

```python
# Entrada: misma para todos
X = torch.tensor([
    [0., 0.],
    [0., 1.],
    [1., 0.],
    [1., 1.]
])

# Salida: 3 columnas (AND, OR, XOR)
y = torch.tensor([
    [0., 0., 0.],  # 0,0 → AND=0, OR=0, XOR=0
    [0., 1., 1.],  # 0,1 → AND=0, OR=1, XOR=1
    [0., 1., 1.],  # 1,0 → AND=0, OR=1, XOR=1
    [1., 1., 0.]   # 1,1 → AND=1, OR=1, XOR=0
])

# Modelo con 3 salidas
model = nn.Sequential(
    nn.Linear(2, 4),
    nn.Sigmoid(),
    nn.Linear(4, 3),  # ← 3 salidas (una por operación)
    nn.Sigmoid()
)
```

---

## SECCIÓN K: Historia Completa del "Invierno de la IA"

### Los protagonistas

> "McCarthy es uno de los padres de la IA. De hecho, inventó la palabra y luego se arrepintió."

| Persona | Contribución |
|---------|-------------|
| **John McCarthy** | Acuñó el término "Inteligencia Artificial" (1956) |
| **Marvin Minsky** | Co-fundador del MIT AI Lab |
| **Seymour Papert** | Co-autor del libro "Perceptrons" (1969) |
| **Frank Rosenblatt** | Inventor del Perceptrón (1957) |

### La secuencia de eventos

1. **1956 - Conferencia de Dartmouth**: Nace el campo de la IA
   > "La IA nace como simbólica, no como conexionista. Estaban pensando que el razonamiento se atacaba del lado lógico."

2. **1957 - El Perceptrón**: Gran entusiasmo
   > "Decían que en menos de 10 años ya iban a resolver el problema del razonamiento humano."

3. **1969 - El libro "Perceptrons"**: El golpe fatal
   > "Minsky y Papert le pusieron la cruz al perceptrón."

4. **1970s-1980s - El Invierno**: Estancamiento
   > "Era una época donde la gente que invertía era muy poca. Sobre todo el gobierno de Estados Unidos, los departamentos de defensa. Si algo tan simple no funciona, ¿para qué invertir?"

### La lección

> "Somos muy malos estimando el tiempo. Sobre-estimamos lo que podemos hacer en un día y sub-estimamos lo que podemos hacer en 10 años."

---

## RESUMEN VISUAL COMPLETO

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    RESUMEN DE LA CLASE 2 (27-08-2025)                        ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  1. PERCEPTRÓN SIMPLE                                                  │  ║
║  │     • Multiplicación de matrices + función de activación               │  ║
║  │     • Puede hacer AND, OR (linealmente separables)                     │  ║
║  │     • NO puede hacer XOR (puntos en diagonal)                          │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                    │                                         ║
║                                    ▼                                         ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  2. EL PROBLEMA DEL XOR                                                │  ║
║  │     • No es linealmente separable                                      │  ║
║  │     • Minsky y Papert lo demostraron (1969)                           │  ║
║  │     • Causó el "Invierno de la IA"                                    │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                    │                                         ║
║                                    ▼                                         ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  3. SOLUCIÓN: PERCEPTRÓN MULTICAPA                                     │  ║
║  │     • Agregar capas ocultas "levanta el papel"                        │  ║
║  │     • nn.Module vs nn.Sequential                                       │  ║
║  │     • Profundidad > Anchura                                            │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                    │                                         ║
║                                    ▼                                         ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  4. TRAINING LOOP                                                      │  ║
║  │     1. Forward pass: outputs = model(x)                                │  ║
║  │     2. Loss: loss = criterion(outputs, y)                              │  ║
║  │     3. Backward: optimizer.zero_grad() + loss.backward()               │  ║
║  │     4. Update: optimizer.step()                                        │  ║
║  │     5. Repetir por N épocas                                            │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                    │                                         ║
║                                    ▼                                         ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  5. GRAFO COMPUTACIONAL                                                │  ║
║  │     • requires_grad=True: guarda historial de operaciones             │  ║
║  │     • detach(): corta el historial ("modo incógnito")                 │  ║
║  │     • torch.no_grad(): no calcular gradientes (evaluación)            │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## GLOSARIO DE TÉRMINOS

| Término | Significado Simple |
|---------|-------------------|
| **Perceptrón** | La neurona artificial más simple |
| **Pesos (weights)** | Números que la red aprende/ajusta |
| **Bias** | Un ajuste adicional (como un offset) |
| **Función de activación** | Transforma la salida (sigmoid, ReLU, signo) |
| **Linealmente separable** | Se puede dividir con una línea/plano recto |
| **MLP** | Multi-Layer Perceptron (perceptrón multicapa) |
| **Forward pass** | Pasar datos por la red para obtener predicción |
| **Backward pass** | Calcular gradientes yendo de la salida a la entrada |
| **Loss/Pérdida** | Medida de qué tan mal está la predicción |
| **Gradiente** | "Culpa" de cada peso en el error |
| **Época** | Una pasada completa por todos los datos |
| **Batch** | Un subconjunto de datos procesados juntos |
| **Learning rate** | Qué tanto ajustar los pesos en cada paso |
| **Grafo computacional** | Historial de operaciones para calcular gradientes |
| **SGD** | Stochastic Gradient Descent (optimizador básico) |
| **Adam** | Optimizador adaptativo (recomendado) |

---

## PRÓXIMA CLASE

> "La semana que viene vamos a ver regresión con redes neuronales y Weights & Biases, una herramienta para monitorear experimentos."

---

## RECURSOS MENCIONADOS EN CLASE

- **Notebook principal**: `1-perceptron.ipynb`
- **Notebooks extra**:
  - `grads_optimizers.ipynb` - Explicación detallada de gradientes
  - `precision.ipynb` - Float16, Float32, BFloat16
- **torchviz**: Paquete para visualizar grafos computacionales
- **Video recomendado**: Explicación visual de profundidad vs anchura en redes

---

**FIN DEL DOCUMENTO - CLASE 2 (27-08-2025)**

Temas cubiertos: Perceptrón, Operaciones Lógicas (AND, OR, NAND, NOR), XOR y Separabilidad Lineal, Historia del Invierno de la IA (McCarthy, Minsky, Papert), MLP, Training Loop Completo, Grafos Computacionales, Optimizadores (SGD, Adam), Learning Rate, Épocas y Batches.
