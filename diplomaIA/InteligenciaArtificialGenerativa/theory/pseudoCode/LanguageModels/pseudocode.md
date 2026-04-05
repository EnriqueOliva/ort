# Pseudocódigo Modelos de Lenguaje (Language Models)

## Idea Central
Predecir el siguiente token. Generar texto token por token.

---

## 1. GENERACIÓN DE SECUENCIAS (Autorregresivo)

**Esta es la pregunta típica del parcial:**

```
FUNCION generar_secuencia(prompt, max_tokens):

    secuencia = tokenizar(prompt)

    MIENTRAS len(secuencia) < max_tokens:

        # 1. Pasar secuencia al modelo
        logits = LM(secuencia)

        # 2. Convertir logits a probabilidades
        probabilidades = softmax(logits)

        # 3. Muestrear siguiente token
        siguiente_token = muestrear(probabilidades)

        # 4. Verificar fin de secuencia
        SI siguiente_token == END_OF_SEQUENCE:
            BREAK

        # 5. Concatenar y repetir
        secuencia = secuencia + [siguiente_token]

    RETORNAR detokenizar(secuencia)
```

---

## 2. EL MODELO ES DETERMINÍSTICO

```
# IMPORTANTE para el parcial:

# El LM en sí es DETERMINÍSTICO
# Misma entrada → Misma distribución de probabilidad

# La GENERACIÓN es ESTOCÁSTICA
# Porque muestreamos de esa distribución

entrada = "Hola, ¿cómo"
probs = LM(entrada)  # SIEMPRE da el mismo vector
token = muestrear(probs)  # PUEDE dar diferentes resultados
```

---

## 3. PROCESO PASO A PASO

```
Entrada: "Hola, ¿cómo"

Paso 1:
    LM("Hola, ¿cómo") → {"estás": 0.35, "andas": 0.15, "te": 0.10, ...}
    Muestrear → "estás"
    Secuencia: "Hola, ¿cómo estás"

Paso 2:
    LM("Hola, ¿cómo estás") → {"?": 0.40, "hoy": 0.20, ...}
    Muestrear → "?"
    Secuencia: "Hola, ¿cómo estás?"

Paso 3:
    LM("Hola, ¿cómo estás?") → {END: 0.60, "Yo": 0.15, ...}
    Muestrear → END
    FIN
```

---

## 4. VARIANTES DE MUESTREO

### Top-K
```
# Solo muestrear de los K tokens más probables
tokens_top_k = top_k(probabilidades, k=50)
siguiente = muestrear(tokens_top_k)
```

### Top-P (Nucleus)
```
# Muestrear hasta acumular probabilidad P
tokens_top_p = []
suma = 0
PARA token en ordenados_por_probabilidad:
    tokens_top_p.append(token)
    suma += probabilidad[token]
    SI suma >= P:
        BREAK
siguiente = muestrear(tokens_top_p)
```

### Temperatura
```
# Modifica la "suavidad" de la distribución
probabilidades = softmax(logits / temperatura)

# temperatura < 1: más determinístico (picos más altos)
# temperatura > 1: más aleatorio (distribución más plana)
```

---

## 5. TOKENIZACIÓN

```
# Texto a tokens (entrada)
tokens = tokenizar("Hola, ¿cómo estás?")
# tokens = [15496, 11, 1212, 734, ...]

# Tokens a texto (salida)
texto = detokenizar([15496, 11, 1212, 734])
# texto = "Hola, ¿cómo estás?"

# IMPORTANTE: Usar el mismo tokenizer siempre
```

---

## Resumen Ultra-Corto

```
GENERAR SECUENCIA:

    MIENTRAS no termine:
        probs = softmax(LM(secuencia))
        token = muestrear(probs)
        SI token == END: terminar
        secuencia = secuencia + token

    RETORNAR secuencia
```

---

## Para el Parcial

**"Implementa en pseudocódigo el proceso de generación de secuencias de un LM"**

```
secuencia = prompt_inicial

REPETIR:
    logits = LM(secuencia)
    probs = softmax(logits)
    token = muestrear(probs)
    SI token == END: SALIR
    secuencia = secuencia + token

RETORNAR secuencia
```
