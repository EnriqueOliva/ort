# Diferenciación Automática y Gradientes - Para Principiantes Absolutos

## Introducción: ¿Por qué necesitamos esto?

Imagina que estás tratando de enseñar a una computadora a reconocer gatos en fotos. La computadora empieza siendo terrible en esto - ve un gato y dice "es un tostador". 

Para mejorar, necesita:
1. **Saber qué tan mal lo está haciendo** (el error)
2. **Entender qué cambiar** para mejorar
3. **Cuánto cambiar** cada parte

Los **gradientes** y la **diferenciación automática** son las herramientas matemáticas que le dicen a la computadora exactamente esto.

## Parte 1: ¿Qué es un Gradiente? (Explicación Ultra Simple)

### Analogía del Termostato

Piensa en un termostato de tu casa:
- **Temperatura actual**: 15°C
- **Temperatura deseada**: 22°C
- **Error**: 7°C (muy frío)

El **gradiente** es como la instrucción que le dice al termostato:
- "Sube la temperatura" (dirección)
- "Está muy frío, sube rápido" (magnitud)

### En una Red Neuronal

Una red neuronal tiene miles de "perillas" (parámetros) que ajustar. El gradiente le dice:
- **Qué perilla girar** 
- **Hacia dónde girarla** (subir o bajar)
- **Cuánto girarla**

```python
# Ejemplo súper simple
temperatura_actual = 15
temperatura_deseada = 22
error = temperatura_deseada - temperatura_actual  # 7

# El "gradiente" nos dice: sube 7 grados
ajuste = error * 0.1  # Ajustamos de a poco (10% del error)
nueva_temperatura = temperatura_actual + ajuste  # 15.7
```

## Parte 2: El Problema de Calcular Cambios

### Sin Automatización (El Problema)

Imagina que tienes una receta de pastel con 20 ingredientes. El pastel sale mal. 

**Pregunta**: ¿Fue mucha harina? ¿Poco azúcar? ¿Temperatura del horno?

Para saberlo manualmente tendrías que:
1. Hacer el pastel 20 veces, cambiando UN ingrediente cada vez
2. Ver cómo afecta cada cambio
3. Es IMPOSIBLE con miles de variables

### Con Diferenciación Automática (La Solución)

La computadora puede:
1. **Recordar cada paso** de la receta
2. **Rastrear cómo cada ingrediente** afectó el resultado
3. **Calcular instantáneamente** qué cambiar

Es como tener un asistente mágico que probó millones de combinaciones en un segundo.

## Parte 3: AutoGrad - El Sistema Mágico de PyTorch

### ¿Qué hace AutoGrad?

AutoGrad es como un **detective** que:
1. **Observa** cada operación matemática que haces
2. **Toma notas** de todo
3. **Puede reconstruir** cómo llegaste al resultado

### Ejemplo Cotidiano

```python
import torch

# Imagina que estás calculando el precio de una compra
precio_base = torch.tensor(100.0, requires_grad=True)  # Le decimos "observa esto"
descuento = 0.2
impuesto = 1.15

# AutoGrad observa cada paso
precio_con_descuento = precio_base * (1 - descuento)  # 80
precio_final = precio_con_descuento * impuesto         # 92

# Ahora preguntamos: "Si cambio el precio_base, ¿cómo cambia el precio_final?"
precio_final.backward()

print(f"Si subo el precio_base en $1, el precio_final sube ${precio_base.grad:.2f}")
# Resultado: 0.92 (porque hay 20% descuento y 15% impuesto)
```

## Parte 4: Cómo Funciona Paso a Paso

### 1. El Viaje de Ida (Forward Pass)

Es como seguir una receta:

```python
# Paso 1: Ingredientes iniciales
huevos = torch.tensor(2.0, requires_grad=True)
harina = torch.tensor(300.0, requires_grad=True)

# Paso 2: Mezclar (la computadora observa)
mezcla = huevos * 50 + harina  # 400

# Paso 3: Hornear (la computadora sigue observando)
pastel = mezcla * 0.8  # 320 (pierde 20% de peso al hornear)

# La computadora ha creado un "mapa" de la receta
```

### 2. El Viaje de Vuelta (Backward Pass)

Ahora vamos hacia atrás preguntando "¿qué causó qué?"

```python
# Queremos un pastel de 350 gramos, salió de 320
error = 350 - 320  # Faltan 30 gramos

# La computadora calcula automáticamente:
pastel.backward()

print(f"Efecto de agregar 1 huevo más: {huevos.grad:.1f} gramos")
print(f"Efecto de agregar 1g más de harina: {harina.grad:.1f} gramos")

# Nos dice cuánto afecta cada ingrediente al peso final
```

## Parte 5: La Regla de la Cadena (La Clave de Todo)

### ¿Qué es la Regla de la Cadena? - Explicación Ultra Simple

La regla de la cadena es como el **efecto dominó** en matemáticas. Cuando una cosa cambia, afecta a la siguiente, que afecta a la siguiente, y así sucesivamente.

### Analogía del Teléfono Descompuesto (Pero Preciso)

Imagina tres amigos pasándose un mensaje:
- **Ana** le dice un número a **Bruno** (multiplicado por 2)
- **Bruno** se lo dice a **Carlos** (sumándole 3)
- **Carlos** obtiene el resultado final

Si queremos saber: "¿Cómo afecta el número de Ana al resultado de Carlos?"

La regla de la cadena dice: **multiplica los efectos**:
- Ana → Bruno: ×2
- Bruno → Carlos: +3 no cambia la multiplicación
- Total: El número de Ana afecta ×2 al resultado

### Ejemplo Súper Visual

```python
# Imagina una bola de nieve rodando por una colina
import torch

# Tamaño inicial de la bola
tamaño_inicial = torch.tensor(1.0, requires_grad=True)

# Primera etapa: la bola duplica su tamaño
tamaño_medio = tamaño_inicial * 2  # 2 cm

# Segunda etapa: la bola crece al cuadrado
tamaño_final = tamaño_medio ** 2  # 4 cm

# PREGUNTA: Si empezamos con 1cm más, ¿cuánto más grande será al final?
tamaño_final.backward()

print(f"Respuesta: {tamaño_inicial.grad} cm más grande")
# Resultado: 8 cm más grande

# ¿Por qué 8?
# - Si empiezas con 2cm en vez de 1cm
# - Primera etapa: 2×2 = 4cm (en vez de 2cm)
# - Segunda etapa: 4² = 16cm (en vez de 4cm)
# - Diferencia: 16 - 4 = 12cm... ¡Ups, no es 8!

# La derivada nos da la tasa de cambio instantánea, no el cambio total
# Es como la velocidad en un momento específico
```

### La Fórmula Sin Dolor

Si tienes una cadena de funciones: `A → B → C`

La regla dice:
```
Cómo A afecta a C = (Cómo A afecta a B) × (Cómo B afecta a C)
```

### Ejemplo Cotidiano: Pizza Delivery

```python
# Cadena de eventos en una pizzería
distancia_km = torch.tensor(5.0, requires_grad=True)

# Paso 1: Distancia → Tiempo (a 30 km/h)
tiempo_minutos = distancia_km * 2  # 10 minutos

# Paso 2: Tiempo → Propina (el cliente da $1 por cada 5 minutos de espera)
propina = tiempo_minutos / 5  # $2

# ¿Cómo afecta la distancia a la propina?
propina.backward()

print(f"Por cada km extra, la propina cambia: ${distancia_km.grad}")
# Resultado: $0.4 por km

# Verificación manual:
# distancia → tiempo: 1 km = 2 minutos extra
# tiempo → propina: 2 minutos = $0.4 extra
# Total: 1 km = $0.4 (¡Coincide!)
```

### ¿Por Qué es Tan Importante?

Las redes neuronales son como **cadenas gigantescas** de operaciones:
- Entrada → Capa1 → Capa2 → Capa3 → ... → Capa100 → Salida

Sin la regla de la cadena, sería IMPOSIBLE saber cómo ajustar los pesos de la Capa1 basándose en el error de la Salida.

### Visualización Paso a Paso

```python
import torch

# Una mini red neuronal de 3 capas
x = torch.tensor(1.0, requires_grad=True)  # Entrada

# Capa 1: multiplicar por peso w1
w1 = torch.tensor(2.0, requires_grad=True)
h1 = x * w1  # 2

# Capa 2: multiplicar por peso w2
w2 = torch.tensor(3.0, requires_grad=True)
h2 = h1 * w2  # 6

# Capa 3: multiplicar por peso w3
w3 = torch.tensor(0.5, requires_grad=True)
salida = h2 * w3  # 3

# Calcular gradientes
salida.backward()

print("Efecto de cada peso en la salida:")
print(f"w1 (primera capa): {w1.grad}")  # 1.5
print(f"w2 (segunda capa): {w2.grad}")  # 1.0
print(f"w3 (tercera capa): {w3.grad}")  # 6.0

# Nota: Los pesos más cercanos a la salida tienen gradientes más grandes
# porque tienen un efecto más directo
```

## Parte 6: Ejemplo Completo - Aprendiendo Desde Cero

### La Magia del Aprendizaje Automático

Vamos a enseñarle a la computadora algo que no sabe: convertir temperaturas.

### Versión Súper Simplificada

```python
import torch

# Lo que sabemos (ejemplos de la vida real)
celsius = torch.tensor([0.0, 20.0, 100.0])
fahrenheit_correcto = torch.tensor([32.0, 68.0, 212.0])

# La computadora empieza sin saber nada
a = torch.tensor(0.5, requires_grad=True)  # Número random
b = torch.tensor(10.0, requires_grad=True)  # Otro número random

# La computadora intenta aprender
for intento in range(1000):
    # Intenta adivinar
    fahrenheit_intento = celsius * a + b

    # Ve qué tan mal lo hizo
    error = ((fahrenheit_intento - fahrenheit_correcto) ** 2).mean()

    # Calcula cómo mejorar (aquí entra la magia del autograd)
    error.backward()

    # Ajusta un poquito
    with torch.no_grad():
        a = a - a.grad * 0.001  # Paso pequeñito
        b = b - b.grad * 0.001
        a.grad.zero_()
        b.grad.zero_()

    # Cada 200 intentos, veamos el progreso
    if intento % 200 == 0:
        print(f"Intento {intento}: F = C×{a:.2f} + {b:.2f} (Error: {error:.2f})")

print(f"\n¡Aprendió! F = C×{a:.2f} + {b:.2f}")
print(f"Respuesta correcta: F = C×1.8 + 32")
```

### ¿Qué Está Pasando Realmente?

```python
# Desglosemos paso por paso un ciclo de aprendizaje

# PASO 1: Estado inicial
a = torch.tensor(0.5, requires_grad=True)  # Mal valor inicial
celsius_ejemplo = torch.tensor(100.0)  # Agua hirviendo
fahrenheit_correcto = 212.0

# PASO 2: Hacer predicción (muy mala al principio)
prediccion = celsius_ejemplo * a  # 100 × 0.5 = 50°F (¡Muy frío!)

# PASO 3: Calcular error
error = (prediccion - fahrenheit_correcto) ** 2  # (50-212)² = 26,244 (¡Enorme!)

# PASO 4: La magia - Autograd calcula cómo cambiar 'a'
error.backward()
print(f"El gradiente dice: 'Sube a en {-a.grad:.1f}'")
# El gradiente es negativo porque 'a' es muy pequeño

# PASO 5: Ajustar
with torch.no_grad():
    a_nuevo = a - a.grad * 0.001  # Subir 'a' un poquito
    print(f"Nuevo valor de a: {a_nuevo:.3f} (era {a:.3f})")
```

## Parte 7: ¿Por Qué es Revolucionario?

### El Problema del Tamaño

Imagina ajustar:
- **10 perillas**: Posible manualmente
- **100 perillas**: Muy difícil
- **1,000 perillas**: Imposible para humanos
- **175,000,000,000 perillas** (GPT-3): Solo posible con autograd

### Comparación Real

**Método Manual (Sin Autograd):**
```python
# Para cada peso, tendríamos que:
# 1. Cambiar el peso un poquito
# 2. Recalcular TODO
# 3. Ver si mejoró o empeoró
# 4. Repetir para CADA peso

# Con 1 millón de pesos y 1ms por cálculo:
# Tiempo = 1,000,000 × 1ms = 16.7 minutos POR ITERACIÓN
```

**Método Automático (Con Autograd):**
```python
# Autograd calcula TODOS los gradientes en una pasada
# Tiempo = unos pocos segundos para TODOS los pesos
```

### Analogía Final

**Sin Autograd**: Como intentar encontrar la salida de un laberinto probando cada camino uno por uno.

**Con Autograd**: Como tener un mapa que te dice instantáneamente hacia dónde ir desde cualquier punto.

## Parte 8: Múltiples Entradas y Salidas (Jacobiano Simplificado)

### ¿Qué Pasa con Múltiples Variables?

Hasta ahora vimos: 1 entrada → 1 salida

Pero en la vida real: Muchas entradas → Muchas salidas

### Ejemplo: Control de Dron

```python
import torch

# Un dron tiene 4 motores
motores = torch.tensor([100.0, 100.0, 100.0, 100.0], requires_grad=True)
# [frontal_izq, frontal_der, trasero_izq, trasero_der]

# Los motores afectan 3 cosas:
# 1. Altura
altura = motores.sum() / 100  # Suma de todos

# 2. Inclinación frontal (pitch)
pitch = (motores[0] + motores[1] - motores[2] - motores[3]) / 100

# 3. Inclinación lateral (roll)
roll = (motores[0] + motores[2] - motores[1] - motores[3]) / 100

# Si queremos subir 1 metro sin inclinarnos:
# ¿Qué motor ajustar y cuánto?

# El Jacobiano es como una tabla de control:
#             Motor1  Motor2  Motor3  Motor4
# Altura:      +1      +1      +1      +1     (todos suben altura)
# Pitch:       +1      +1      -1      -1     (frontales vs traseros)
# Roll:        +1      -1      +1      -1     (izquierdos vs derechos)
```

### Versión Súper Simple

```python
# Tienes 2 palancas que controlan 2 luces
palanca_a = torch.tensor(5.0, requires_grad=True)
palanca_b = torch.tensor(3.0, requires_grad=True)

# Las luces dependen de ambas palancas
luz_roja = palanca_a * 2 + palanca_b      # 13
luz_azul = palanca_a - palanca_b * 2      # -1

# Pregunta: ¿Cómo afecta cada palanca a cada luz?
# Respuesta: El Jacobiano te da una tabla 2x2:
#              Luz_Roja  Luz_Azul
# Palanca_A:      2         1
# Palanca_B:      1        -2

# Esto significa:
# - Subir palanca_a → luz_roja +2, luz_azul +1
# - Subir palanca_b → luz_roja +1, luz_azul -2
```

## Parte 9: Conceptos Importantes Explicados Desde Cero

### ¿Qué es `with torch.no_grad()`?

**Primero entendamos el problema:**

Cuando PyTorch calcula algo, por defecto "graba" todos los pasos (como vimos antes). Esto usa memoria y tiempo.

```python
# Por defecto, PyTorch SIEMPRE observa y graba
x = torch.tensor(2.0, requires_grad=True)
y = x * 2  # PyTorch graba: "multipliqué x por 2"
z = y + 3  # PyTorch graba: "sumé 3 a y"
# Toda esta "grabación" usa memoria
```

**¿Cuándo NO necesitas grabar?**

Cuando solo quieres usar tu red, no entrenarla:

```python
# Analogía: Grabar vs Solo Ver

# CUANDO ENTRENAS (necesitas grabar para aprender)
# Como grabar tu partido de fútbol para ver errores después
celsius = torch.tensor(100.0)
a = torch.tensor(1.5, requires_grad=True)  # Parámetro a aprender
fahrenheit = celsius * a + 32
error = (fahrenheit - 212) ** 2
error.backward()  # Necesitas los gradientes para mejorar 'a'

# CUANDO YA APRENDISTE (solo quieres usar)
# Como jugar un partido amistoso sin grabar
with torch.no_grad():  # "No grabes nada, solo calcula"
    celsius_nuevo = torch.tensor(50.0)
    fahrenheit_nuevo = celsius_nuevo * 1.8 + 32  # Solo calcular
    print(f"50°C = {fahrenheit_nuevo}°F")
    # Más rápido, menos memoria
```

### El Problema de la Acumulación de Gradientes

**¿Qué significa que los gradientes se acumulan?**

```python
# Experimento simple para entender
x = torch.tensor(3.0, requires_grad=True)

# Primera vez
y = x * 2
y.backward()
print(f"Gradiente después de 1 cálculo: {x.grad}")  # 2

# Segunda vez (sin limpiar)
y = x * 2
y.backward()
print(f"Gradiente después de 2 cálculos: {x.grad}")  # 4 (¡se sumó!)

# Tercera vez (sin limpiar)
y = x * 2
y.backward()
print(f"Gradiente después de 3 cálculos: {x.grad}")  # 6 (¡sigue sumando!)
```

**¿Por qué PyTorch hace esto?**

Es útil en algunos casos avanzados, pero normalmente es un problema.

**La solución: Limpiar después de usar**

```python
# Reiniciemos
x = torch.tensor(3.0, requires_grad=True)

for i in range(3):
    y = x * 2
    y.backward()
    print(f"Gradiente: {x.grad}")

    # IMPORTANTE: Limpiar para el siguiente cálculo
    if x.grad is not None:  # Solo si existe
        x.grad.zero_()  # Poner en cero
```

### ¿Qué es el "Grafo Computacional"?

**Explicación simple:**

El grafo computacional es el "mapa" que PyTorch dibuja de tus cálculos.

```python
# PyTorch crea un mapa invisible como este:
x = torch.tensor(2.0, requires_grad=True)
y = x * 3        # Paso 1: x → (*3) → y
z = y + 5        # Paso 2: y → (+5) → z
w = z ** 2       # Paso 3: z → (**2) → w

# El "grafo" es:
# x --(*3)--> y --(+5)--> z --(**2)--> w

# Cuando haces backward(), PyTorch recorre este mapa al revés
w.backward()
# w <--(**2)-- z <--(+5)-- y <--(*3)-- x
```

**¿Qué pasa con el grafo después de backward()?**

```python
# Después de backward(), el mapa se destruye automáticamente
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
y.backward()  # Usa el mapa y lo destruye
# y.backward()  # ERROR: ¡el mapa ya no existe!

# Si necesitas usarlo dos veces (raro):
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
y.backward(retain_graph=True)  # "No destruyas el mapa"
y.backward()  # Ahora sí funciona
```

### Consejos Prácticos para Principiantes

#### 1. Siempre Limpia los Gradientes en Loops

```python
# Patrón que SIEMPRE funciona:
parametro = torch.tensor(1.0, requires_grad=True)

for epoca in range(100):
    # Hacer cálculos
    resultado = parametro * 2
    error = (resultado - 5) ** 2

    # Calcular gradientes
    error.backward()

    # Usar gradientes para mejorar
    with torch.no_grad():
        parametro = parametro - 0.01 * parametro.grad

    # SIEMPRE limpiar al final
    parametro.grad.zero_()
```

#### 2. Usa no_grad() Cuando No Entrenes

```python
# Regla simple:
# ¿Estás ajustando parámetros? NO uses no_grad()
# ¿Solo estás calculando? SÍ usa no_grad()

# Entrenando (ajustando)
a = torch.tensor(1.0, requires_grad=True)
resultado = a * 2
error = (resultado - 4) ** 2
error.backward()  # Necesitas esto para ajustar 'a'

# Solo usando (sin ajustar)
with torch.no_grad():
    test = a * 2
    print(f"Resultado: {test}")
    # No necesitas gradientes, solo el resultado
```

#### 3. Mensajes de Error Comunes y Qué Significan

```python
# ERROR 1: "can't backward through the graph a second time"
# Significa: Intentaste backward() dos veces
x = torch.tensor(1.0, requires_grad=True)
y = x * 2
y.backward()
# y.backward()  # Este causaría el error

# ERROR 2: "element 0 of tensors does not require grad"
# Significa: Olvidaste requires_grad=True
x = torch.tensor(1.0)  # Falta requires_grad=True
y = x * 2
# y.backward()  # Este causaría el error

# ERROR 3: "grad can be implicitly created only for scalar outputs"
# Significa: Solo puedes hacer backward() en un número, no en un vector
x = torch.tensor([1.0, 2.0], requires_grad=True)
y = x * 2  # y es [2.0, 4.0], no un solo número
# y.backward()  # Error
y.sum().backward()  # Correcto: sum() lo convierte en un número
```

## Parte 10: Juntando Todo - Un Ejemplo Completo Paso a Paso

### Problema: Predecir Si Aprobaré el Examen

Vamos a crear un "predictor" que aprenda de ejemplos.

```python
import torch

# Datos históricos de estudiantes:
# [horas_estudio, horas_sueño] -> aprobará (1) o no (0)

# Entrada: horas de estudio y sueño
estudio_sueno = torch.tensor([
    [1.0, 4.0],  # Poco estudio, poco sueño
    [1.0, 8.0],  # Poco estudio, buen sueño
    [5.0, 4.0],  # Mucho estudio, poco sueño
    [5.0, 8.0],  # Mucho estudio, buen sueño
])

# Salida: 0 = reprueba, 1 = aprueba
resultados = torch.tensor([
    [0.0],  # Reprobó
    [0.0],  # Reprobó
    [0.0],  # Reprobó (cansado)
    [1.0],  # ¡Aprobó!
])

# Nuestro "modelo" simple: resultado = w1*estudio + w2*sueño + b
w1 = torch.tensor(0.1, requires_grad=True)  # Peso para horas de estudio
w2 = torch.tensor(0.1, requires_grad=True)  # Peso para horas de sueño
b = torch.tensor(0.0, requires_grad=True)   # Sesgo

print("Valores iniciales (aleatorios):")
print(f"Peso estudio: {w1.item():.2f}")
print(f"Peso sueño: {w2.item():.2f}")
print(f"Sesgo: {b.item():.2f}")

# ENTRENAMIENTO - Aprender de los ejemplos
for epoca in range(500):
    # 1. Hacer predicción con los pesos actuales
    prediccion = estudio_sueno[:, 0] * w1 + estudio_sueno[:, 1] * w2 + b

    # 2. Aplicar función sigmoid para obtener probabilidad (0 a 1)
    # Sigmoid convierte cualquier número a un valor entre 0 y 1
    probabilidad = 1 / (1 + torch.exp(-prediccion))

    # 3. Calcular qué tan mal lo hicimos
    error = ((probabilidad - resultados.squeeze()) ** 2).mean()

    # 4. Calcular gradientes (la magia de autograd)
    error.backward()

    # 5. Actualizar pesos (aprender)
    with torch.no_grad():  # No grabar estos cambios
        w1 = w1 - w1.grad * 0.5  # Ajustar peso de estudio
        w2 = w2 - w2.grad * 0.5  # Ajustar peso de sueño
        b = b - b.grad * 0.5     # Ajustar sesgo

        # Mantener requires_grad
        w1.requires_grad = True
        w2.requires_grad = True
        b.requires_grad = True

    # 6. Limpiar gradientes para siguiente iteración
    if w1.grad is not None:
        w1.grad.zero_()
        w2.grad.zero_()
        b.grad.zero_()

    # Mostrar progreso
    if epoca % 100 == 0:
        print(f"\nÉpoca {epoca}:")
        print(f"  Error: {error.item():.4f}")
        print(f"  Pesos: estudio={w1.item():.2f}, sueño={w2.item():.2f}, sesgo={b.item():.2f}")

# PRUEBA FINAL - Ver qué aprendió
print("\n=== RESULTADOS FINALES ===")
print(f"Fórmula aprendida:")
print(f"Probabilidad = sigmoid({w1.item():.2f}*estudio + {w2.item():.2f}*sueño + {b.item():.2f})")

print("\nPredicciones:")
with torch.no_grad():  # Solo calcular, no grabar
    for i in range(4):
        estudio = estudio_sueno[i, 0].item()
        sueno = estudio_sueno[i, 1].item()
        pred = estudio * w1 + sueno * w2 + b
        prob = 1 / (1 + torch.exp(-pred))
        real = resultados[i].item()

        print(f"Estudio: {estudio}h, Sueño: {sueno}h")
        print(f"  Predicción: {prob.item():.1%} de aprobar")
        print(f"  Realidad: {'Aprobó' if real == 1 else 'Reprobó'}")
        print()

# INTERPRETACIÓN
print("\n=== QUÉ APRENDIÓ LA RED ===")
if w1.item() > w2.item():
    print("El estudio es más importante que el sueño")
else:
    print("El sueño es más importante que el estudio")

print(f"\nPor cada hora extra de estudio: +{w1.item():.1f} puntos")
print(f"Por cada hora extra de sueño: +{w2.item():.1f} puntos")
```

### ¿Qué Acaba de Pasar?

1. **Definimos el problema**: Predecir aprobación basado en estudio y sueño
2. **Inicializamos parámetros aleatorios**: w1, w2, b con `requires_grad=True`
3. **Hicimos predicciones**: Multiplicamos y sumamos
4. **Calculamos el error**: Qué tan lejos estamos de la respuesta correcta
5. **Usamos backward()**: PyTorch calculó automáticamente cómo ajustar
6. **Actualizamos pesos**: Movimos los valores en la dirección correcta
7. **Repetimos**: 500 veces hasta que aprendió

**Lo increíble**: Nunca le dijimos la fórmula. La descubrió sola mirando ejemplos.

## Resumen: Lo Que Aprendiste Hoy

### Los Conceptos Básicos (En Orden)

1. **Tensor con requires_grad=True**
   - Es un número que PyTorch "observa"
   - Como poner una cámara en tu cálculo

2. **Forward Pass**
   - Los cálculos normales que haces
   - PyTorch los graba mientras los haces

3. **Backward Pass**
   - Retroceder por los cálculos
   - Descubrir qué causó qué

4. **Gradiente**
   - La instrucción de "sube esto" o "baja esto"
   - Te dice cómo cambiar cada parámetro

5. **Regla de la Cadena**
   - Conecta cambios a través de múltiples pasos
   - Como el efecto dominó en matemáticas

### El Ciclo de Aprendizaje

```python
# SIEMPRE es el mismo patrón:

# 1. Crear parámetro que quieres ajustar
parametro = torch.tensor(valor_inicial, requires_grad=True)

# 2. Hacer cálculos con ese parámetro
resultado = hacer_calculos(parametro)

# 3. Medir qué tan mal está
error = calcular_error(resultado, objetivo)

# 4. Calcular cómo mejorar
error.backward()  # PyTorch calcula los gradientes

# 5. Mejorar un poquito
with torch.no_grad():
    parametro = parametro - learning_rate * parametro.grad
    parametro.requires_grad = True  # Mantener la observación

# 6. Limpiar para el siguiente intento
parametro.grad.zero_()
```

### Lo Revolucionario

**Antes de AutoGrad:**
- Calcular derivadas a mano para cada parámetro
- Imposible con más de 10 parámetros
- Días de cálculos matemáticos

**Con AutoGrad:**
- PyTorch calcula todo automáticamente
- Funciona con millones de parámetros
- Milisegundos de cálculo

### Para la Próxima Clase

Ahora que entiendes cómo la computadora puede "aprender" ajustando números automáticamente, en las próximas clases veremos:

1. **Redes Neuronales**: Muchos parámetros trabajando juntos
2. **Backpropagation**: Cómo se propagan los gradientes en redes profundas
3. **Optimizadores**: Formas inteligentes de ajustar parámetros

### El Mensaje Clave

La diferenciación automática es el **motor** del deep learning. Sin ella, sería imposible entrenar las redes neuronales modernas. Es la diferencia entre:

- Ajustar 1 perilla manualmente
- Ajustar 175 billones de perillas automática y perfectamente (GPT-3)

**Lo más importante**: No necesitas ser un genio matemático. PyTorch hace los cálculos difíciles por ti. Solo necesitas entender el concepto.