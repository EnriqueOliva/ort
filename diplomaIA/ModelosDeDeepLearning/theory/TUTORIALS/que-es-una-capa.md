# ¿Qué es una Capa? - Explicado desde CERO

Esta es LA confusión número 1 que tienen todos cuando empiezan con redes neuronales. El profesor fue MUY enfático con esto en la clase del 01-09-2025.

Te voy a explicar qué es una capa como si nunca hubieras visto esto. Con números concretos. Sin asumir que sabes qué significa ningún símbolo.

---

## **La confusión que todos tenemos al principio**

Ves este dibujo de una red neuronal:

```
[X] → [○ ○] → [Y]
```

Y piensas: "Veo 3 columnas, entonces tiene 3 capas."

**ESTO ES INCORRECTO.**

El profesor dijo bien claro: **"Las capas NO son columnas."**

---

## **La verdad sobre las capas**

### **Una capa NO es una columna de círculos**

Una capa es **LA CONEXIÓN entre dos columnas**.

Es como un puente. El puente NO es ninguna de las dos orillas, es lo que las conecta.

---

## **Ejemplo visual del profesor**

```
        ┌─ Esto es la Capa 1 ─┐   ┌─ Esto es la Capa 2 ─┐
        │                      │   │                      │
     [X] ──────────────────→ [○] ──────────────────────→ [Y]
                              [○]
```

**Pregunta:** ¿Cuántas capas tiene esta red?

**Respuesta:** **DOS capas** (no tres)

**¿Por qué?**

**Capa 1:** Es la conexión que va desde X hasta los dos círculos
**Capa 2:** Es la conexión que va desde los dos círculos hasta Y

---

## **Empecemos con un ejemplo CONCRETO**

Imagina que tienes un número. Llamémoslo **X = 5**

Quieres construir una red que transforme ese 5 en algún resultado final.

---

## **CAPA 1: De 1 número a 2 números**

### **¿Qué hace la Capa 1?**

Toma tu número (5) y lo convierte en DOS números.

**¿Cómo? Con una receta:**

Imagina que tienes dos cajas. Cada caja tiene su propia receta:

**Caja 1 dice:** "Multiplica el número que te doy por 2, y súmale 10"
**Caja 2 dice:** "Multiplica el número que te doy por -3, y súmale 7"

---

### **Aplicando las recetas a nuestro número (5)**

**Caja 1:**
- Multiplico 5 × 2 = 10
- Le sumo 10
- Resultado: 10 + 10 = **20**

**Caja 2:**
- Multiplico 5 × (-3) = -15
- Le sumo 7
- Resultado: -15 + 7 = **-8**

**Ahora tengo dos números:** 20 y -8

---

### **Los ingredientes de cada receta tienen NOMBRES**

En la Caja 1:
- El "2" (por cuánto multiplicas) se llama **peso** o **W**
- El "10" (lo que sumas) se llama **bias** o **b**

En la Caja 2:
- El "-3" se llama **peso** o **W**
- El "7" se llama **bias** o **b**

**Estos números (los pesos y los bias) son los PARÁMETROS.**

---

### **¿Qué es un parámetro?**

**Un parámetro es un número que la red tiene "guardado" y que puede cambiar para aprender.**

Cuando la red "aprende", lo que hace es **ajustar estos números** para que funcione mejor.

En la Capa 1 del ejemplo:
- **Peso de la Caja 1:** 2 ← este es 1 parámetro
- **Bias de la Caja 1:** 10 ← este es 1 parámetro
- **Peso de la Caja 2:** -3 ← este es 1 parámetro
- **Bias de la Caja 2:** 7 ← este es 1 parámetro

**Total:** 4 parámetros en la Capa 1

---

### **Escribámoslo con símbolos (pero ya sabes qué significa cada cosa)**

**Para la Caja 1:**
```
Resultado_1 = X × W₁ + b₁
Resultado_1 = 5 × 2 + 10
Resultado_1 = 20
```

**Para la Caja 2:**
```
Resultado_2 = X × W₂ + b₂
Resultado_2 = 5 × (-3) + 7
Resultado_2 = -8
```

Donde:
- **X** = tu número de entrada (5)
- **W₁** = el peso de la primera caja (2)
- **b₁** = el bias de la primera caja (10)
- **W₂** = el peso de la segunda caja (-3)
- **b₂** = el bias de la segunda caja (7)

---

### **Pero espera, falta un paso: la activación**

Los resultados 20 y -8 son muy crudos. Necesitamos "suavizarlos" con una **función de activación**.

El profesor usó una llamada **SoftPlus**. No importa exactamente qué hace, solo imagina que:
- Los números muy grandes los hace un poco más chicos
- Los números negativos los acerca a cero
- Los números positivos los deja parecidos

Llamemos **A₁** y **A₂** a los resultados después de aplicar la función de activación:

```
A₁ = SoftPlus(20) ≈ 20  (casi lo mismo porque ya era positivo)
A₂ = SoftPlus(-8) ≈ 0.0003  (casi cero porque era negativo)
```

**Ahora sí terminamos la Capa 1:**
- Entramos con: 1 número (X = 5)
- Salimos con: 2 números (A₁ ≈ 20, A₂ ≈ 0.0003)

---

## **CAPA 2: De 2 números a 1 número**

### **¿Qué hace la Capa 2?**

Toma los DOS números que salieron de la Capa 1 y los combina en UN número final.

**La receta única de esta capa dice:**

"Toma el primer número (A₁), multiplícalo por 0.5, toma el segundo número (A₂), multiplícalo por 1.2, suma todo, y agrégale 3"

---

### **Aplicando la receta**

Tenemos:
- A₁ ≈ 20
- A₂ ≈ 0.0003

**Calculamos:**
- Primer número contribuye: 20 × 0.5 = 10
- Segundo número contribuye: 0.0003 × 1.2 ≈ 0.0004
- Sumamos todo: 10 + 0.0004 = 10.0004
- Le agregamos el bias: 10.0004 + 3 = 13.0004

**Resultado final: Ŷ ≈ 13**

---

### **Los parámetros de la Capa 2**

En esta receta teníamos:
- **Peso para A₁:** 0.5 ← este es 1 parámetro
- **Peso para A₂:** 1.2 ← este es 1 parámetro
- **Bias:** 3 ← este es 1 parámetro

**Total:** 3 parámetros en la Capa 2

---

### **Escribámoslo con símbolos (ahora ya sabes qué es cada cosa)**

```
Ŷ = A₁ × W₁⁽²⁾ + A₂ × W₂⁽²⁾ + b⁽²⁾
```

Donde:
- **Ŷ** = resultado final (lo que predice la red)
- **A₁** = primer número que salió de la Capa 1 (≈20)
- **A₂** = segundo número que salió de la Capa 1 (≈0.0003)
- **W₁⁽²⁾** = peso para el primer número en la capa 2 (0.5)
- **W₂⁽²⁾** = peso para el segundo número en la capa 2 (1.2)
- **b⁽²⁾** = bias de la capa 2 (3)

**El "(2)" arriba significa "de la capa 2".**

Con números concretos:
```
Ŷ = 20 × 0.5 + 0.0003 × 1.2 + 3
Ŷ ≈ 13
```

---

## **Resumen completo de la red**

```
Entrada: X = 5

Capa 1 (1 → 2):
  Caja 1: 5 × 2 + 10 = 20 → Activación → A₁ ≈ 20
  Caja 2: 5 × (-3) + 7 = -8 → Activación → A₂ ≈ 0.0003

Capa 2 (2 → 1):
  20 × 0.5 + 0.0003 × 1.2 + 3 ≈ 13

Salida: Ŷ = 13
```

---

## **Ahora sí: ¿Cuántos parámetros tiene esta red?**

Un **parámetro** es cada número que la red puede ajustar para aprender.

### **Capa 1: De 1 entrada a 2 salidas**

**Caja 1 (para hacer la primera salida):**
- 1 peso (el número por el que multiplicas la entrada)
- 1 bias (el número que sumas)

**Caja 2 (para hacer la segunda salida):**
- 1 peso
- 1 bias

**Total Capa 1:** 2 pesos + 2 bias = **4 parámetros**

### **Capa 2: De 2 entradas a 1 salida**

**Caja única (para hacer la única salida):**
- 1 peso para la primera entrada
- 1 peso para la segunda entrada
- 1 bias

**Total Capa 2:** 2 pesos + 1 bias = **3 parámetros**

### **Total de la red completa: 4 + 3 = 7 parámetros**

Estos 7 números son los que la red ajustará cuando "aprenda".

---

## **La fórmula general (ahora que entiendes el concepto)**

Para cualquier capa:

**Si tienes:**
- **I** entradas (números que llegan)
- **O** salidas (números que produces)

**Necesitas:**
- **I × O** pesos (porque cada entrada se conecta con cada salida)
- **O** bias (uno por cada salida)

**Total:** **(I × O) + O** parámetros

### **Aplicado a nuestro ejemplo:**

**Capa 1:** I=1, O=2
- Pesos: 1 × 2 = 2
- Bias: 2
- Total: 2 + 2 = 4 ✓

**Capa 2:** I=2, O=1
- Pesos: 2 × 1 = 2
- Bias: 1
- Total: 2 + 1 = 3 ✓

---

## **¿Por qué I × O pesos?**

Porque **cada entrada** necesita conectarse con **cada salida**.

**Ejemplo visual de la Capa 2:**

```
A₁ (entrada 1) ──────→ Necesita 1 peso ──┐
                                           ├──→ Salida única
A₂ (entrada 2) ──────→ Necesita 1 peso ──┘

Total: 2 pesos (porque son 2 entradas × 1 salida)
```

**Si la Capa 2 tuviera 3 salidas en vez de 1:**

```
         ──→ Salida 1 (necesita 2 pesos, uno de cada entrada)
A₁ ───┼──→ Salida 2 (necesita 2 pesos, uno de cada entrada)
A₂ ───┘──→ Salida 3 (necesita 2 pesos, uno de cada entrada)

Total: 2 × 3 = 6 pesos
```

---

## **¿Por qué O bias?**

Porque cada salida tiene su propia "constante que le sumas al final".

Si tienes 2 salidas, necesitas 2 bias (uno para cada una).
Si tienes 5 salidas, necesitas 5 bias (uno para cada una).

Simple.

---

## **Ejercicio para practicar (con números concretos)**

**Red:** 3 entradas → 4 salidas → 2 salidas

Imagina que tienes 3 números: X₁=2, X₂=5, X₃=-1

### **Pregunta 1:** ¿Cuántas capas tiene?

<details>
<summary>Respuesta</summary>

**2 capas**

- Capa 1: de 3 números a 4 números
- Capa 2: de 4 números a 2 números

</details>

### **Pregunta 2:** ¿Cuántos parámetros tiene cada capa?

<details>
<summary>Respuesta</summary>

**Capa 1:** I=3, O=4
- Pesos: 3 × 4 = 12 (cada una de las 3 entradas se conecta con cada una de las 4 salidas)
- Bias: 4 (uno por cada salida)
- **Total: 16 parámetros**

**Capa 2:** I=4, O=2
- Pesos: 4 × 2 = 8 (cada una de las 4 entradas se conecta con cada una de las 2 salidas)
- Bias: 2 (uno por cada salida)
- **Total: 10 parámetros**

</details>

### **Pregunta 3:** ¿Cuántos parámetros en total?

<details>
<summary>Respuesta</summary>

16 + 10 = **26 parámetros**

Estos 26 números son los que la red ajustará cuando aprenda.

</details>

---

## **¿Qué significa "Capa Densa" o "Fully Connected"?**

El profesor dijo: **"Una capa densa conecta todo el mundo con todo el mundo."**

**¿Qué significa?**

Que CADA entrada se conecta con CADA salida. No se salta ninguna conexión.

**Ejemplo visual:**

```
Entrada 1 ─────┬───→ Salida 1
               │
Entrada 2 ─────┼───→ Salida 2
               │
               └───→ Salida 3
```

Todas las entradas van a todas las salidas. Por eso se llama "fully connected" (completamente conectado).

---

## **Los nombres que verás en código**

Esta misma idea tiene diferentes nombres según dónde la veas:

- **Dense layer** (Keras) ← al profesor le gusta este
- **Linear layer** (PyTorch) ← porque hace la parte "lineal"
- **Fully connected layer** ← el más descriptivo

**Todos significan lo mismo:** una capa donde todo se conecta con todo.

**En código se ve así:**

```python
# PyTorch
capa1 = nn.Linear(1, 2)  # 1 entrada → 2 salidas
capa2 = nn.Linear(2, 1)  # 2 entradas → 1 salida

# Keras
model.add(Dense(2, input_dim=1))  # Capa 1
model.add(Dense(1))               # Capa 2
```

---

## **Resumen en una imagen mental**

Una **capa** es como una fábrica con múltiples líneas de producción:

```
         ┌─────────────────┐
         │   CAPA 1        │
         │   (Fábrica)     │
         │                 │
X=5  ──→ │  [Línea 1] ───→ │ ──→ A₁=20
         │  [Línea 2] ───→ │ ──→ A₂≈0
         │                 │
         └─────────────────┘
```

- **Entra:** 1 número
- **Cada línea de producción:** aplica su propia receta (peso × entrada + bias)
- **Sale:** 2 números

La fábrica completa es la CAPA. Cada línea de producción usa sus propios parámetros.

---

## **La frase del profesor que resume todo**

> "Acuérdense: las capas no son columnas de unidades, sino que son pares input-output. Una capa es un par input-output."
>
> — Profesor, clase 01-09-2025

**En español simple:**

Una capa no es un montón de círculos. Es **el proceso que transforma** un grupo de números en otro grupo de números.

---

## **¿Por qué importa entender esto?**

### **1. Para saber cuánto puede aprender tu red**

Más parámetros = más capacidad de aprender patrones complejos.

Si tu red tiene solo 7 parámetros (como nuestro ejemplo), puede aprender cosas simples.
Si tu red tiene 1,000,000 de parámetros, puede aprender cosas muy complejas.

### **2. Para diseñar redes**

Cuando te dicen "diseña una red 10→20→5", sabes exactamente qué hacer:
- Capa 1: 10 entradas, 20 salidas → (10×20)+20 = 220 parámetros
- Capa 2: 20 entradas, 5 salidas → (20×5)+5 = 105 parámetros
- Total: 325 parámetros

### **3. Para entender errores**

Si ves un error:
```
Error: Expected input of size 10, got 5
```

Sabes que intentaste meter 5 números en una capa que espera 10.

### **4. Para leer papers y tutoriales**

Cuando leas "una red de 3 capas con 256, 128, y 10 unidades", entenderás perfectamente qué significa.

---

## **Último concepto: ¿Qué son esos círculos en los dibujos?**

El profesor aclaró: **"Cada círculo no es una neurona, es una unidad."**

**Unidad:** Un número en un momento dado del procesamiento.

**Neurona:** El proceso completo (multiplicar, sumar, activar).

Pero para fines prácticos, cuando veas dibujos con círculos, solo recuerda:
- No cuentes los círculos para contar capas
- Cuenta las CONEXIONES entre grupos de círculos

---

## **Verificación final: ¿Entendiste?**

**Dime con tus propias palabras:**

1. ¿Qué es un parámetro?
2. ¿Qué es una capa?
3. Si una capa tiene 5 entradas y 3 salidas, ¿cuántos parámetros tiene?

<details>
<summary>Respuestas esperadas</summary>

1. **Parámetro:** Un número que la red puede ajustar para aprender (los pesos y bias)

2. **Capa:** La transformación/conexión que convierte un grupo de números en otro grupo de números

3. **Parámetros:** (5×3) + 3 = 15 + 3 = 18 parámetros

</details>

---

*Todo esto viene de la clase del 01-09-2025 donde el profesor dedicó tiempo específico a aclarar esta confusión fundamental que todos tienen al empezar con redes neuronales.*
