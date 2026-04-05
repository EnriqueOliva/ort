# Ejercicio 1 - Transformers: Explicación Detallada de Cada Componente

---

## GLOSARIO DE TÉRMINOS (lee esto primero)

Antes de empezar, aquí están las palabras técnicas que usaremos:

| Término | ¿Qué significa? |
|---------|-----------------|
| **Vocabulario** | La LISTA de todas las palabras que el modelo conoce. Ejemplo: si el vocabulario tiene 30,000 palabras, el modelo solo puede trabajar con esas 30,000. Cualquier palabra fuera del vocabulario es "desconocida". |
| **Token** | Un pedazo de texto. Puede ser una palabra completa ("gato"), parte de palabra ("##iendo"), o un símbolo ("?"). El modelo trabaja con tokens, no con letras sueltas. |
| **Vector** | Una lista ordenada de números. Ejemplo: [0.2, -0.5, 0.8] es un vector de 3 números. Los vectores permiten representar cosas (como palabras) como números que la computadora puede procesar. |
| **Embedding** | Convertir algo (una palabra, una posición) en un vector de números. "El embedding de 'gato'" = el vector que representa a "gato". |
| **d_model** | La cantidad de números que tiene cada vector. En el paper original = 512. Todos los vectores internos del Transformer tienen este tamaño. |
| **Dimensión** | Sinónimo de "cuántos números tiene un vector". Un vector de dimensión 512 tiene 512 números. |
| **Parámetro** | Un número que el modelo APRENDE durante entrenamiento. Las matrices W son colecciones de parámetros. |
| **Entrenamiento** | El proceso donde el modelo APRENDE, ajustando sus parámetros viendo muchos ejemplos. |
| **Inferencia** | Cuando el modelo ya aprendió y lo USAMOS para predecir cosas nuevas. |
| **Secuencia** | Una lista ordenada de tokens. "Hola mundo" es una secuencia de 2 tokens. |
| **Encoder** | La parte que PROCESA la entrada (lee la frase en francés). |
| **Decoder** | La parte que GENERA la salida (escribe la frase en inglés). |
| **Logits** | Números "crudos" antes de convertirlos en probabilidades. Pueden ser negativos o mayores que 1. |
| **Softmax** | Función que convierte logits en probabilidades (números entre 0 y 1 que suman 1). |
| **Gradiente** | Indica "hacia dónde ajustar los parámetros" para que el modelo mejore. |
| **Batch** | Un grupo de ejemplos que se procesan juntos para eficiencia. |

---

## Primero: ¿Dónde encaja cada componente en nuestra clasificación?

Antes de explicar cada uno, clasifiquémoslos según los **TIPOS** que vimos en el curso:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│            CLASIFICACIÓN DE LOS COMPONENTES DEL TRANSFORMER                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   TIPO 1 - REPRESENTACIÓN DE DATOS (convertir cosas reales en números)     │
│   ─────────────────────────────────────────────────────────────────────     │
│   • Input Embedding                                                         │
│   • Output Embedding                                                        │
│   • Positional Encoding                                                     │
│                                                                             │
│   TIPO 2 - CAPAS (operaciones matemáticas que transforman datos)           │
│   ──────────────────────────────────────────────────────────────           │
│   • Multi-Head Attention                                                    │
│   • Masked Multi-Head Attention                                             │
│   • Feed Forward                                                            │
│   • Linear                                                                  │
│   • Softmax                                                                 │
│                                                                             │
│   TIPO 5 - TRUCOS ARQUITECTÓNICOS (mejoras para entrenar mejor)            │
│   ─────────────────────────────────────────────────────────────            │
│   • Add & Norm (Skip Connection + Layer Normalization)                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## El Diagrama del Transformer con Anotaciones

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ARQUITECTURA TRANSFORMER                             │
│                   (implementa el patrón Encoder-Decoder)                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                                        Output Probabilities                 │
│                                               ▲                             │
│                                               │                             │
│                                        ┌──────┴──────┐                      │
│                                        │   SOFTMAX   │ ← (i)                │
│                                        └──────┬──────┘                      │
│                                               │                             │
│                                        ┌──────┴──────┐                      │
│                                        │   LINEAR    │ ← (h)                │
│                                        └──────┬──────┘                      │
│                                               │                             │
│   ╔════════════════════╗               ╔══════╧══════════════╗              │
│   ║     ENCODER        ║               ║      DECODER        ║              │
│   ║    (Nx veces)      ║               ║     (Nx veces)      ║              │
│   ╠════════════════════╣               ╠═════════════════════╣              │
│   ║                    ║               ║                     ║              │
│   ║  ┌──────────────┐  ║               ║  ┌──────────────┐   ║              │
│   ║  │  Add & Norm  │  ║               ║  │  Add & Norm  │   ║ ← (f)        │
│   ║  └───────┬──────┘  ║               ║  └───────┬──────┘   ║              │
│   ║          │         ║               ║          │          ║              │
│   ║  ┌───────┴──────┐  ║               ║  ┌───────┴──────┐   ║              │
│   ║  │ Feed Forward │  ║               ║  │ Feed Forward │   ║ ← (g)        │
│   ║  └───────┬──────┘  ║               ║  └───────┬──────┘   ║              │
│   ║          │         ║               ║          │          ║              │
│   ║  ┌───────┴──────┐  ║               ║  ┌───────┴──────┐   ║              │
│   ║  │  Add & Norm  │  ║               ║  │  Add & Norm  │   ║ ← (f)        │
│   ║  └───────┬──────┘  ║               ║  └───────┬──────┘   ║              │
│   ║          │         ║               ║          │          ║              │
│   ║  ┌───────┴──────┐  ║    K,V        ║  ┌───────┴──────┐   ║              │
│   ║  │  Multi-Head  │──╫───────────────╫─▶│  Multi-Head  │   ║ ← (j) CROSS  │
│   ║  │  Attention   │  ║  (del encoder ║  │  Attention   │   ║    ATTENTION │
│   ║  └───────┬──────┘  ║   al decoder) ║  └───────┬──────┘   ║              │
│   ║          │         ║               ║          │          ║              │
│   ║  ┌───────┴──────┐  ║               ║  ┌───────┴──────┐   ║              │
│   ║  │  Add & Norm  │  ║               ║  │  Add & Norm  │   ║ ← (f)        │
│   ║  └───────┬──────┘  ║               ║  └───────┬──────┘   ║              │
│   ║          │         ║               ║          │          ║              │
│   ║          │         ║               ║  ┌───────┴──────┐   ║              │
│   ║          │         ║               ║  │    Masked    │   ║ ← (e)        │
│   ║          │         ║               ║  │  Multi-Head  │   ║              │
│   ║          │         ║               ║  │  Attention   │   ║              │
│   ║          │         ║               ║  └───────┬──────┘   ║              │
│   ╚══════════╪═════════╝               ╚══════════╪══════════╝              │
│              │                                    │                         │
│         ┌────┴────┐                          ┌────┴────┐                    │
│         │   ⊕     │                          │    ⊕    │ ← Suma             │
│         └────┬────┘                          └────┬────┘                    │
│              │                                    │                         │
│   ┌──────────┴──────────┐             ┌──────────┴──────────┐               │
│   │ Positional Encoding │             │ Positional Encoding │ ← (c)         │
│   └──────────┬──────────┘             └──────────┬──────────┘               │
│              │                                    │                         │
│   ┌──────────┴──────────┐             ┌──────────┴──────────┐               │
│   │  Input Embedding    │             │  Output Embedding   │ ← (a) y (b)   │
│   └──────────┬──────────┘             └──────────┬──────────┘               │
│              │                                    │                         │
│              ▲                                    ▲                         │
│           Inputs                             Outputs                        │
│     (frase en francés)                  (shifted right)                     │
│                                                                             │
│   ════════════════════════════════════════════════════════════════════════  │
│   ⚠️  OJO: Input Embedding y Output Embedding están DIBUJADOS lado a lado   │
│       pero NO están conectados entre sí. Son caminos INDEPENDIENTES:        │
│                                                                             │
│       Input Embedding ──────→ ENCODER (procesa el francés)                  │
│                                   │                                         │
│                                   │ K,V (única conexión)                    │
│                                   ▼                                         │
│       Output Embedding ─────→ DECODER (genera el inglés)                    │
│                                                                             │
│       Están dibujados al mismo nivel porque AMBOS convierten palabras       │
│       en vectores, pero cada uno alimenta a su propia parte del modelo.     │
│   ════════════════════════════════════════════════════════════════════════  │
│   FLUJO DE DATOS:                                                           │
│   1. Encoder procesa el input COMPLETO (todas las Nx capas)                 │
│   2. La SALIDA del encoder va como K,V al cross-attention del decoder       │
│   3. Decoder genera la salida palabra por palabra                           │
│   4. ÚNICA conexión encoder→decoder: la flecha K,V al cross-attention       │
│   ════════════════════════════════════════════════════════════════════════  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# EXPLICACIÓN DETALLADA DE CADA COMPONENTE

---

## (a) Input Embedding

### TIPO: 1 - Representación de Datos

### ¿Qué es?

Convierte cada palabra (o token) de la **entrada** en un vector de números.

### ¿Por qué es necesario?

Las redes neuronales NO pueden procesar palabras directamente. Solo entienden números.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         INPUT EMBEDDING                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ENTRADA (tokens):     "Bonjour"    "le"    "monde"                        │
│                             │          │         │                          │
│                             ▼          ▼         ▼                          │
│                                                                             │
│   PROCESO:              Buscar en tabla de embeddings                       │
│                         (matriz de tamaño [vocab × d_model])                │
│                                                                             │
│                             │          │         │                          │
│                             ▼          ▼         ▼                          │
│                                                                             │
│   SALIDA (vectores):    [0.2, -0.5,  [0.1, 0.8,  [0.9, -0.2,               │
│                          0.8, ...]    0.3, ...]   0.1, ...]                 │
│                                                                             │
│                         (cada uno tiene d_model dimensiones,                │
│                          típicamente 512 en el paper original)              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ¿Cómo funciona internamente?

1. Cada palabra tiene un **índice** en el vocabulario (ej: "Bonjour" = 4523)
2. La tabla de embeddings es una matriz de tamaño [tamaño_vocabulario × d_model]
3. "Buscar" el embedding = seleccionar la fila 4523 de la matriz

### Comparación con lo que ya conoces

| En CNN | En Transformer |
|--------|----------------|
| Foto → Tensor [224×224×3] | Palabra → Vector [d_model] |
| Ya viene en números (píxeles) | Hay que convertir texto a números |

### ¿Se entrena?

**Sí.** Los valores de la tabla de embeddings son parámetros que se ajustan durante el entrenamiento.

---

## (b) Output Embedding

### TIPO: 1 - Representación de Datos

### ¿Qué es?

Exactamente lo mismo que Input Embedding, pero para la **secuencia de salida** (la traducción que queremos generar).

### ¿Qué es un Embedding? (lo más básico)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    EMBEDDING = UN DICCIONARIO                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Un embedding es simplemente una TABLA que dice:                           │
│                                                                             │
│   "gato"    → [0.2, -0.5, 0.8, ...]  (512 números)                          │
│   "perro"   → [0.3, 0.1, -0.2, ...]  (512 números)                          │
│   "hola"    → [0.9, 0.4, 0.1, ...]   (512 números)                          │
│   ...                                                                       │
│   (una fila por cada palabra conocida)                                      │
│                                                                             │
│   Es como un diccionario: le das una palabra, te devuelve números.          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ¿Por qué hay DOS embeddings en el diagrama?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              EJEMPLO CONCRETO: TRADUCIR FRANCÉS → INGLÉS                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   TAREA: Traducir "Bonjour" → "Hello"                                       │
│                                                                             │
│   PROBLEMA:                                                                 │
│   - "Bonjour" es una palabra FRANCESA                                       │
│   - "Hello" es una palabra INGLESA                                          │
│   - Son idiomas DIFERENTES con palabras DIFERENTES                          │
│                                                                             │
│   SOLUCIÓN: Necesitamos DOS diccionarios (dos embeddings)                   │
│                                                                             │
│   ┌─────────────────────────┐       ┌─────────────────────────┐             │
│   │ INPUT EMBEDDING         │       │ OUTPUT EMBEDDING        │             │
│   │ (diccionario francés)   │       │ (diccionario inglés)    │             │
│   ├─────────────────────────┤       ├─────────────────────────┤             │
│   │ "bonjour" → [0.2, ...]  │       │ "hello" → [0.5, ...]    │             │
│   │ "monde"   → [0.3, ...]  │       │ "world" → [0.1, ...]    │             │
│   │ "le"      → [0.1, ...]  │       │ "the"   → [0.8, ...]    │             │
│   │ (50,000 palabras FR)    │       │ (40,000 palabras EN)    │             │
│   └─────────────────────────┘       └─────────────────────────┘             │
│              │                                   │                          │
│              ▼                                   ▼                          │
│          ENCODER                             DECODER                        │
│   (procesa el francés)               (genera el inglés)                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ¿Y si NO es traducción?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│          SI EL INPUT Y OUTPUT SON EL MISMO IDIOMA...                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   EJEMPLO: Resumir un artículo en español                                   │
│                                                                             │
│   Input:  "El presidente anunció hoy que..." (texto largo en español)       │
│   Output: "Presidente anuncia medidas" (resumen corto en español)           │
│                                                                             │
│   Como AMBOS son español, usamos EL MISMO diccionario:                      │
│                                                                             │
│   ┌─────────────────────────┐                                               │
│   │ UN SOLO EMBEDDING       │                                               │
│   │ (diccionario español)   │                                               │
│   ├─────────────────────────┤                                               │
│   │ "presidente" → [...]    │                                               │
│   │ "anunció"    → [...]    │──────┬──────────────────┐                     │
│   │ "medidas"    → [...]    │      │                  │                     │
│   │ (60,000 palabras ES)    │      │                  │                     │
│   └─────────────────────────┘      │                  │                     │
│                                    ▼                  ▼                     │
│                                ENCODER            DECODER                   │
│                                                                             │
│   Input Embedding y Output Embedding son LA MISMA TABLA                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ¿Y si solo hay Decoder? (como GPT/ChatGPT)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GPT: SOLO DECODER, SIN ENCODER                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   EJEMPLO: Completar texto                                                  │
│                                                                             │
│   Input:  "El clima hoy es"                                                 │
│   Output: "soleado"                                                         │
│                                                                             │
│   NO hay encoder, así que NO hay "Input Embedding"                          │
│   Solo hay UN embedding que usa el decoder:                                 │
│                                                                             │
│   ┌─────────────────────────┐                                               │
│   │ ÚNICO EMBEDDING         │                                               │
│   ├─────────────────────────┤                                               │
│   │ "el"      → [...]       │                                               │
│   │ "clima"   → [...]       │                                               │
│   │ "soleado" → [...]       │                                               │
│   └─────────────────────────┘                                               │
│              │                                                              │
│              ▼                                                              │
│          DECODER  (no hay encoder)                                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Resumen: ¿Cuántos embeddings?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   SITUACIÓN                        │ ¿CUÁNTOS EMBEDDINGS?                   │
│   ─────────────────────────────────┼───────────────────────────────────     │
│   Traducción (FR→EN)               │ 2 (uno francés, uno inglés)            │
│   Resumen (ES→ES)                  │ 1 (compartido, mismo idioma)           │
│   GPT (solo decoder)               │ 1 (no hay encoder)                     │
│   BERT (solo encoder)              │ 1 (no hay decoder)                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ¿Qué es "Outputs (shifted right)"?

Durante **entrenamiento**, al decoder le pasamos la traducción correcta, pero **desplazada una posición a la derecha**.

¿Qué significa esto? Le damos la respuesta "atrasada" para que prediga la siguiente palabra:

```
Traducción que queremos:  "Hello"  "world"  "<EOS>"
                                               ↑
                                    (EOS = End Of Sequence = "fin")

Lo que le damos al decoder: "<SOS>"  "Hello"  "world"
                              ↑
                   (SOS = Start Of Sequence = "inicio")

El decoder recibe una palabra y debe predecir LA SIGUIENTE:
   Recibe "<SOS>"  → debe predecir "Hello"   (la primera palabra real)
   Recibe "Hello"  → debe predecir "world"   (la segunda palabra)
   Recibe "world"  → debe predecir "<EOS>"   (que ya terminó)
```

### ¿Qué son SOS y EOS? (EXPLICACIÓN ULTRA SIMPLE)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TOKENS ESPECIALES: SOS y EOS                        │
│                    (son "palabras inventadas" con un propósito)             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   SOS y EOS son "palabras falsas" que agregamos al vocabulario.             │
│   No existen en ningún idioma real, pero el modelo las necesita.            │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   SOS = "Start Of Sequence" = INICIO DE SECUENCIA                           │
│   ─────────────────────────────────────────────────                         │
│                                                                             │
│   ANALOGÍA: Es como el "¡En sus marcas, listos, FUERA!" de una carrera.     │
│                                                                             │
│   Sin SOS, el decoder no sabe cómo empezar.                                 │
│                                                                             │
│   Pensalo así:                                                              │
│   - El decoder SIEMPRE necesita recibir algo para generar algo              │
│   - Pero al principio... ¡no hay nada generado todavía!                     │
│   - SOS es la "primera palabra falsa" que le damos para que arranque        │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                     │   │
│   │   SIN SOS:                                                          │   │
│   │                                                                     │   │
│   │   Decoder: "Tengo que generar la primera palabra..."                │   │
│   │   Decoder: "Pero para generar necesito recibir algo..."            │   │
│   │   Decoder: "Pero no tengo nada..."                                  │   │
│   │   Decoder: "¿¿¿???"  ← SE TRABA, NO PUEDE EMPEZAR                   │   │
│   │                                                                     │   │
│   │   Es como un auto sin llave. No puede arrancar.                     │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                     │   │
│   │   CON SOS:                                                          │   │
│   │                                                                     │   │
│   │   Le damos: "<SOS>"                                                 │   │
│   │   Decoder: "Ah, recibí SOS, eso significa que tengo que generar     │   │
│   │            la PRIMERA palabra de la traducción"                     │   │
│   │   Decoder: → genera "Hello"                                         │   │
│   │                                                                     │   │
│   │   SOS es la llave que enciende el motor.                            │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   EOS = "End Of Sequence" = FIN DE SECUENCIA                                │
│   ──────────────────────────────────────────────                            │
│                                                                             │
│   ANALOGÍA: Es como "FIN" o "THE END" al final de una película.             │
│                                                                             │
│   Sin EOS, el decoder no sabe cuándo parar.                                 │
│                                                                             │
│   Pensalo así:                                                              │
│   - El decoder genera palabra tras palabra tras palabra...                  │
│   - Pero ¿cuándo debe detenerse?                                            │
│   - EOS es la señal de "ya terminé, no genero más"                          │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                     │   │
│   │   SIN EOS:                                                          │   │
│   │                                                                     │   │
│   │   Traducir "Bonjour" (= "Hello")                                    │   │
│   │                                                                     │   │
│   │   Decoder genera: "Hello"                                           │   │
│   │   Decoder genera: "my"        ← ¿por qué sigue?                     │   │
│   │   Decoder genera: "friend"    ← nadie le dijo que pare              │   │
│   │   Decoder genera: "how"                                             │   │
│   │   Decoder genera: "are"                                             │   │
│   │   Decoder genera: "you"                                             │   │
│   │   Decoder genera: "today"                                           │   │
│   │   ... (SIGUE PARA SIEMPRE)                                          │   │
│   │                                                                     │   │
│   │   Es como un grifo abierto sin forma de cerrarlo.                   │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                     │   │
│   │   CON EOS:                                                          │   │
│   │                                                                     │   │
│   │   Traducir "Bonjour" (= "Hello")                                    │   │
│   │                                                                     │   │
│   │   Decoder genera: "Hello"                                           │   │
│   │   Decoder genera: "<EOS>"     ← "¡Listo! Ya terminé"                │   │
│   │                                                                     │   │
│   │   Cuando el decoder genera EOS, PARAMOS de generar.                 │   │
│   │   EOS es la llave que apaga el motor.                               │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   RESUMEN:                                                                  │
│                                                                             │
│   ┌───────────┬────────────────────────────────────────────────────────┐    │
│   │   TOKEN   │   ¿PARA QUÉ SIRVE?                                     │    │
│   ├───────────┼────────────────────────────────────────────────────────┤    │
│   │   SOS     │   Señal de ARRANQUE. "Empezá a generar."               │    │
│   │           │   Sin esto: el decoder no puede empezar.               │    │
│   ├───────────┼────────────────────────────────────────────────────────┤    │
│   │   EOS     │   Señal de PARADA. "Ya terminé."                       │    │
│   │           │   Sin esto: el decoder genera infinitamente.           │    │
│   └───────────┴────────────────────────────────────────────────────────┘    │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   EJEMPLO COMPLETO:                                                         │
│                                                                             │
│   Traducir "Bonjour le monde" → "Hello world"                               │
│                                                                             │
│   PASO 1: Damos "<SOS>" al decoder                                          │
│           Decoder genera: "Hello"                                           │
│                                                                             │
│   PASO 2: Damos "<SOS> Hello" al decoder                                    │
│           Decoder genera: "world"                                           │
│                                                                             │
│   PASO 3: Damos "<SOS> Hello world" al decoder                              │
│           Decoder genera: "<EOS>"   ← ¡SEÑAL DE PARAR!                      │
│                                                                             │
│   RESULTADO FINAL: "Hello world" (sin incluir SOS ni EOS)                   │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   NOTA: A veces se usan otros nombres:                                      │
│                                                                             │
│   SOS también se llama: <BOS> (Begin Of Sequence), <START>, [CLS]           │
│   EOS también se llama: <END>, </s>, [SEP]                                  │
│                                                                             │
│   Son lo mismo, solo cambia el nombre según el modelo.                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## (c) Positional Encoding

### TIPO: 1 - Representación de Datos

### ¿Qué es?

Agrega información de **posición** a cada vector.

### ¿Por qué es necesario?

El Transformer procesa todas las palabras **en paralelo** (no secuencialmente como la RNN). Por lo tanto, **no sabe qué palabra viene primero**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      EL PROBLEMA DE LA POSICIÓN                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Sin Positional Encoding:                                                  │
│                                                                             │
│   "El perro mordió al hombre"                                               │
│   "El hombre mordió al perro"                                               │
│                                                                             │
│   → El Transformer vería EXACTAMENTE LO MISMO                               │
│     (mismas palabras, mismos embeddings)                                    │
│                                                                             │
│   ¡Pero significan cosas completamente diferentes!                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ¿Cómo funciona?

Se **suma** un vector de posición al embedding de cada palabra:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      POSITIONAL ENCODING                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Palabra "gato" en posición 3:                                             │
│                                                                             │
│   Embedding("gato")     = [0.2, -0.5, 0.8, 0.1, ...]                        │
│                            +                                                │
│   PosEncoding(pos=3)    = [0.1, 0.9, -0.3, 0.0, ...]                        │
│                            ─────────────────────────                        │
│   Resultado             = [0.3, 0.4, 0.5, 0.1, ...]                         │
│                                                                             │
│   La misma palabra "gato" en posición 7 tendría:                            │
│                                                                             │
│   Embedding("gato")     = [0.2, -0.5, 0.8, 0.1, ...]  (igual)               │
│                            +                                                │
│   PosEncoding(pos=7)    = [0.7, -0.2, 0.5, 0.3, ...]  (diferente!)          │
│                            ─────────────────────────                        │
│   Resultado             = [0.9, -0.7, 1.3, 0.4, ...]  (diferente!)          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ¿Cómo se calculan los valores?

Con funciones **seno y coseno** de diferentes frecuencias:

```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

No te preocupes por la fórmula exacta. Lo importante es entender que:
- Cada posición tiene un patrón **único**
- Los patrones se pueden distinguir unos de otros
- **No se entrena:** son valores fijos calculados con la fórmula

### Comparación con RNN

| RNN | Transformer |
|-----|-------------|
| Procesa secuencialmente → sabe el orden automáticamente | Procesa en paralelo → necesita Positional Encoding |
| Posición implícita en el orden de procesamiento | Posición explícita sumada al embedding |

---

## (d) Multi-Head Attention

### TIPO: 2 - Capa (operación matemática)

### ¿Qué es?

La operación central del Transformer. Permite que cada palabra "mire" a todas las demás palabras para entender su contexto.

### ¿Por qué "Multi-Head"?

En lugar de hacer attention una sola vez, lo hacemos **múltiples veces en paralelo** (típicamente 8 "cabezas"), cada una aprendiendo a enfocarse en relaciones diferentes.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       MULTI-HEAD ATTENTION                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ¿Por qué múltiples cabezas?                                               │
│                                                                             │
│   Cabeza 1: Aprende relaciones GRAMATICALES                                 │
│             "El gato [que está en la mesa] duerme"                          │
│              ↑                              ↑                                │
│              └──── sujeto ──────────────────┘                               │
│                                                                             │
│   Cabeza 2: Aprende relaciones SEMÁNTICAS                                   │
│             "El banco está cerca del río"                                   │
│              ↑                        ↑                                     │
│              └─ banco de tierra ──────┘                                     │
│                                                                             │
│   Cabeza 3: Aprende relaciones de PROXIMIDAD                                │
│             Palabras cercanas tienden a relacionarse                        │
│                                                                             │
│   ... y así hasta 8 cabezas (o más)                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### El mecanismo Query-Key-Value

Cada cabeza usa tres transformaciones:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         QUERY, KEY, VALUE                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Para cada palabra, calculamos tres vectores:                              │
│                                                                             │
│   QUERY (Q): "¿Qué estoy buscando?"                                         │
│              Es lo que la palabra actual quiere saber                       │
│                                                                             │
│   KEY (K):   "¿Qué información tengo para ofrecer?"                         │
│              Es cómo cada palabra se "etiqueta" a sí misma                  │
│                                                                             │
│   VALUE (V): "¿Cuál es mi contenido?"                                       │
│              Es la información que cada palabra aporta                      │
│                                                                             │
│   ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│   Ejemplo: "El gato negro duerme"                                           │
│                                                                             │
│   Para "duerme":                                                            │
│   Q = "¿Quién está durmiendo?" (busca el sujeto)                            │
│                                                                             │
│   Comparamos Q de "duerme" con K de todas las palabras:                     │
│   - K de "El" → poca relación                                               │
│   - K de "gato" → ¡alta relación! (es el sujeto)                            │
│   - K de "negro" → relación media                                           │
│                                                                             │
│   Resultado: "duerme" presta más ATENCIÓN a "gato"                          │
│              y usa el VALUE de "gato" para enriquecer su representación     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### La fórmula

```
Attention(Q, K, V) = softmax(Q × K^T / √d_k) × V
```

Donde:
- `Q × K^T` = qué tan relacionadas están las palabras
- `/ √d_k` = escala para evitar números muy grandes
- `softmax` = convierte en pesos que suman 1
- `× V` = promedio ponderado de los valores

### En el ENCODER

Multi-Head Attention en el encoder es **Self-Attention**: cada palabra de la entrada mira a todas las demás palabras de la entrada.

---

## (e) Masked Multi-Head Attention

### TIPO: 2 - Capa (con modificación para entrenamiento)

### ¿Qué es?

Es **exactamente igual** que Multi-Head Attention, pero con una **máscara** que impide mirar el futuro.

### ¿Por qué es necesario?

Durante **entrenamiento**, el decoder ve toda la secuencia de salida de una vez. Pero en **inferencia**, genera palabra por palabra. Si durante entrenamiento pudiera "ver el futuro", haría trampa.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      MASKED MULTI-HEAD ATTENTION                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Secuencia: "<SOS>" "Hello" "world" "<EOS>"                                │
│               pos 0   pos 1   pos 2   pos 3                                 │
│                                                                             │
│   Sin máscara (MAL - hace trampa):                                          │
│   ──────────────────────────────────                                        │
│   Para predecir pos 1: puede ver pos 0, 1, 2, 3                             │
│   → Sabe que después viene "world", ¡trampa!                                │
│                                                                             │
│   Con máscara (BIEN - no puede ver el futuro):                              │
│   ────────────────────────────────────────────                              │
│   Para predecir pos 1: solo puede ver pos 0, 1                              │
│   Para predecir pos 2: solo puede ver pos 0, 1, 2                           │
│   Para predecir pos 3: solo puede ver pos 0, 1, 2, 3                        │
│                                                                             │
│                                                                             │
│   La máscara visualmente:                                                   │
│                                                                             │
│              puede ver →                                                    │
│            pos0  pos1  pos2  pos3                                           │
│   pos0  [   1     0     0     0  ]   ← solo ve a sí mismo                   │
│   pos1  [   1     1     0     0  ]   ← ve pos0 y pos1                       │
│   pos2  [   1     1     1     0  ]   ← ve pos0, pos1, pos2                  │
│   pos3  [   1     1     1     1  ]   ← ve todo                              │
│                                                                             │
│   Los 0 se convierten en -∞ antes del softmax, haciendo que esos            │
│   pesos de atención sean 0.                                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Comparación con RNN

| RNN | Transformer con Masked Attention |
|-----|----------------------------------|
| No puede ver el futuro porque procesa secuencialmente | Necesita máscara explícita para no ver el futuro |
| "Natural" | "Forzado" pero permite paralelización |

---

## (f) Add & Norm

### TIPO: 5 - Truco Arquitectónico

### ¿Qué es?

Son **dos operaciones juntas**:
1. **Add** = Skip Connection (conexión residual)
2. **Norm** = Layer Normalization

### Add (Skip Connection)

Es la misma idea que vimos en ResNet en la clase 8:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          SKIP CONNECTION                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                    ┌─────────────────┐                                      │
│          ┌────────▶│  Alguna capa    │────────┐                             │
│          │         │  (Attention o   │        │                             │
│   X ─────┤         │   FeedForward)  │        ▼                             │
│          │         └─────────────────┘    ┌───────┐                         │
│          │                                │  (+)  │───▶ Salida              │
│          └────────────────────────────────▶       │                         │
│                                           └───────┘                         │
│                                                                             │
│   Salida = X + Capa(X)                                                      │
│                                                                             │
│   ¿Por qué funciona?                                                        │
│   • El gradiente puede fluir directamente por el "atajo"                    │
│   • Evita vanishing gradient en redes muy profundas                         │
│   • La capa solo necesita aprender el "residuo" (lo que falta)              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Norm (Layer Normalization)

Normaliza los valores para que estén "centrados" y con escala uniforme:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       LAYER NORMALIZATION                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Entrada:  [2.0, 8.0, 4.0, 6.0]                                            │
│                                                                             │
│   1. Calcular MEDIA (promedio): μ = (2+8+4+6)/4 = 5.0                       │
│                                                                             │
│   2. Calcular VARIANZA (qué tan dispersos están los números):               │
│      σ² = promedio de (cada número - media)²                                │
│                                                                             │
│   3. NORMALIZAR: restar la media y dividir por la desviación                │
│      (x - μ) / σ                                                            │
│                                                                             │
│   Salida:   [-1.34, 1.34, -0.45, 0.45]  (aprox)                             │
│             ↑                                                               │
│   Ahora los números están "centrados" alrededor de 0                        │
│                                                                             │
│   ¿Por qué funciona?                                                        │
│   • Estabiliza el entrenamiento (los números no se van a extremos)          │
│   • Los valores no "explotan" (muy grandes) ni desaparecen (muy pequeños)   │
│   • Hace que el entrenamiento sea más rápido                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Diferencia con Batch Normalization

| Batch Norm (usado en CNN) | Layer Norm (usado en Transformer) |
|---------------------------|-----------------------------------|
| Normaliza a través del batch | Normaliza dentro de cada ejemplo |
| Depende del tamaño del batch | Independiente del batch |
| Problemas con secuencias de largo variable | Funciona bien con secuencias |

---

## (g) Feed Forward

### TIPO: 2 - Capa (operación matemática)

### ¿Qué es? (EXPLICACIÓN ULTRA SIMPLE)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          FEED FORWARD                                       │
│                                                                             │
│   Primero, recordemos qué son esos "512 números" que representan            │
│   cada palabra:                                                             │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ¿QUÉ SON LOS 512 NÚMEROS DE CADA PALABRA?                                 │
│   ──────────────────────────────────────────                                │
│                                                                             │
│   Cada número representa una CARACTERÍSTICA de la palabra.                  │
│   No sabemos exactamente qué significa cada uno, pero imaginemos:           │
│                                                                             │
│   La palabra "banco" podría tener estos 512 números:                        │
│                                                                             │
│   número[0] = 0.8   (qué tan relacionado está con "dinero")                 │
│   número[1] = 0.3   (qué tan relacionado está con "sentarse")               │
│   número[2] = 0.1   (qué tan relacionado está con "comida")                 │
│   número[3] = 0.7   (qué tan "sustantivo" es)                               │
│   número[4] = 0.0   (qué tan "verbo" es)                                    │
│   ... y así hasta 512 características                                       │
│                                                                             │
│   Estos números son como una "ficha técnica" de la palabra.                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   AHORA SÍ: ¿QUÉ HACE FEED FORWARD?                                         │
│   ──────────────────────────────────                                        │
│                                                                             │
│   Feed Forward es una CALCULADORA que toma los 512 números                  │
│   y los TRANSFORMA en 512 números NUEVOS (mejores).                         │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   EJEMPLO CONCRETO: La palabra "banco"                                      │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   SITUACIÓN: La oración es "Me senté en el banco del parque"                │
│                                                                             │
│   DESPUÉS DE ATTENTION:                                                     │
│   La palabra "banco" ya "sabe" que está cerca de "senté" y "parque"         │
│   porque Attention le permitió ver las otras palabras.                      │
│                                                                             │
│   Sus 512 números ahora son algo como:                                      │
│   número[0] = 0.8   (dinero)      ← todavía alto, no se ha decidido         │
│   número[1] = 0.6   (sentarse)    ← subió porque vio "senté"                │
│   número[2] = 0.1   (comida)                                                │
│   número[3] = 0.7   (sustantivo)                                            │
│   ...                                                                       │
│                                                                             │
│   PROBLEMA: Los números están "crudos". Attention juntó información         │
│   pero no la INTERPRETÓ.                                                    │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ENTRA FEED FORWARD:                                                       │
│                                                                             │
│   Feed Forward es como una FÓRMULA que dice:                                │
│                                                                             │
│   "Si número[1] (sentarse) es alto Y número[0] (dinero) también es alto,    │
│    entonces probablemente 'banco' significa el asiento, no el financiero.   │
│    Voy a BAJAR número[0] y SUBIR número[1]."                                │
│                                                                             │
│   DESPUÉS DE FEED FORWARD:                                                  │
│   número[0] = 0.2   (dinero)      ← BAJÓ                                    │
│   número[1] = 0.9   (sentarse)    ← SUBIÓ                                   │
│   número[2] = 0.1   (comida)                                                │
│   número[3] = 0.7   (sustantivo)                                            │
│   ...                                                                       │
│                                                                             │
│   Ahora "banco" tiene una representación más REFINADA:                      │
│   los números reflejan mejor que es un banco para sentarse.                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   OTRO EJEMPLO: La palabra "cura"                                           │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ORACIÓN A: "El cura de la iglesia"                                        │
│   ORACIÓN B: "La cura de la enfermedad"                                     │
│                                                                             │
│   En ambos casos, "cura" empieza con los mismos 512 números base.           │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ORACIÓN A: "El cura de la iglesia"                                        │
│                                                                             │
│   Después de Attention: "cura" vio "iglesia"                                │
│   Después de Feed Forward:                                                  │
│      número[persona] = ALTO                                                 │
│      número[religión] = ALTO                                                │
│      número[medicina] = BAJO                                                │
│      → "cura" ahora representa al SACERDOTE                                 │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ORACIÓN B: "La cura de la enfermedad"                                     │
│                                                                             │
│   Después de Attention: "cura" vio "enfermedad"                             │
│   Después de Feed Forward:                                                  │
│      número[persona] = BAJO                                                 │
│      número[religión] = BAJO                                                │
│      número[medicina] = ALTO                                                │
│      → "cura" ahora representa al REMEDIO                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   ENTONCES, ¿QUÉ ES FEED FORWARD EN RESUMEN?                                │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   Es una CALCULADORA APRENDIDA que:                                         │
│                                                                             │
│   1. RECIBE: Los 512 números de una palabra (después de Attention)          │
│                                                                             │
│   2. APLICA: Fórmulas que el modelo APRENDIÓ durante entrenamiento          │
│              Estas fórmulas detectan patrones como:                         │
│              - "Si X es alto e Y es bajo, entonces Z debería subir"         │
│              - "Si esto parece un verbo, activar estas características"     │
│              - "Si el contexto es médico, ajustar estos números"            │
│                                                                             │
│   3. DEVUELVE: 512 números NUEVOS, más refinados, más útiles                │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   ANALOGÍA FINAL:                                                           │
│                                                                             │
│   Attention = Un DETECTIVE que RECOLECTA pistas de los testigos             │
│               (habla con todos, junta información)                          │
│                                                                             │
│   Feed Forward = El detective ANALIZA las pistas en su oficina              │
│                  (conecta los puntos, saca conclusiones)                    │
│                                                                             │
│   - Attention: "El sospechoso fue visto cerca del banco, había un parque"   │
│   - Feed Forward: "Ajá, banco + parque = banco para sentarse, no robo"      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   ¿CÓMO LO HACE TÉCNICAMENTE? (opcional, si querés saber)                   │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   Feed Forward es una red neuronal MUY simple de 2 capas:                   │
│                                                                             │
│   512 números                                                               │
│       │                                                                     │
│       ▼                                                                     │
│   ┌────────────────────────────────────────┐                                │
│   │  CAPA 1: Multiplicar por una matriz    │                                │
│   │  Resultado: 2048 números               │                                │
│   │  (se "expande" para ver más detalles)  │                                │
│   └────────────────────────────────────────┘                                │
│       │                                                                     │
│       ▼                                                                     │
│   ┌────────────────────────────────────────┐                                │
│   │  ReLU: Si un número es negativo → 0    │                                │
│   │  (se descartan cosas irrelevantes)     │                                │
│   └────────────────────────────────────────┘                                │
│       │                                                                     │
│       ▼                                                                     │
│   ┌────────────────────────────────────────┐                                │
│   │  CAPA 2: Multiplicar por otra matriz   │                                │
│   │  Resultado: 512 números                │                                │
│   │  (se "comprime" al tamaño original)    │                                │
│   └────────────────────────────────────────┘                                │
│       │                                                                     │
│       ▼                                                                     │
│   512 números NUEVOS (refinados)                                            │
│                                                                             │
│   Las matrices se APRENDEN durante entrenamiento.                           │
│   El modelo descubre qué transformaciones son útiles.                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ¿Por qué es necesario? (ATTENTION vs FEED FORWARD)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│         ATTENTION vs FEED FORWARD: HACEN COSAS DIFERENTES                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│   ATTENTION = RECOLECTAR información de otras palabras                      │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   "banco" mira a "parque" y "senté" → ahora tiene información nueva         │
│   Pero esa información está "cruda", sin procesar                           │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│   FEED FORWARD = INTERPRETAR esa información                                │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   Toma la información cruda y la TRANSFORMA:                                │
│   "banco" + contexto de "parque" → definitivamente es asiento, no dinero    │
│                                                                             │
│   ───────────────────────────────────────────────────────────────────────   │
│                                                                             │
│   El Transformer ALTERNA entre los dos:                                     │
│                                                                             │
│   Attention → Feed Forward → Attention → Feed Forward → ...                 │
│   (recolectar)  (interpretar) (recolectar) (interpretar)                    │
│                                                                             │
│   Cada vez los números de cada palabra se vuelven MÁS PRECISOS.             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## (h) Linear

### TIPO: 2 - Capa (operación matemática)

### ¿Qué es? (EXPLICACIÓN ULTRA SIMPLE)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              LINEAR                                         │
│              (en palabras simples: "ELEGIR UNA PALABRA")                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   PROBLEMA QUE RESUELVE:                                                    │
│   ──────────────────────                                                    │
│                                                                             │
│   Después de todo el procesamiento, el Decoder tiene 512 números.           │
│   Pero nosotros queremos una PALABRA, no números.                           │
│                                                                             │
│   ¿Cómo pasamos de números a una palabra?                                   │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ANALOGÍA: EXAMEN DE OPCIÓN MÚLTIPLE                                       │
│   ─────────────────────────────────────                                     │
│                                                                             │
│   Imaginate que el idioma inglés tiene 30,000 palabras.                     │
│   El modelo tiene que elegir UNA de esas 30,000.                            │
│                                                                             │
│   Es como un examen de opción múltiple con 30,000 opciones:                 │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────┐               │
│   │  PREGUNTA: ¿Cuál es la siguiente palabra?               │               │
│   │                                                         │               │
│   │  a) the                                                 │               │
│   │  b) a                                                   │               │
│   │  c) hello     ← ¡ESTA!                                  │               │
│   │  d) world                                               │               │
│   │  e) cat                                                 │               │
│   │  ... (30,000 opciones más)                              │               │
│   └─────────────────────────────────────────────────────────┘               │
│                                                                             │
│   ¿Cómo elige? Dando un PUNTAJE a cada opción.                              │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   ¿QUÉ HACE LINEAR EXACTAMENTE?                                             │
│   ─────────────────────────────────                                         │
│                                                                             │
│   ENTRADA: 512 números (representan "la idea de la palabra que quiero")     │
│                                                                             │
│   PROCESO: Compara esos 512 números con CADA palabra del vocabulario        │
│            y dice: "¿Cuánto se parece esta idea a cada palabra?"            │
│                                                                             │
│   SALIDA: 30,000 números (un puntaje para cada palabra)                     │
│                                                                             │
│           "the"   → puntaje: 1.2                                            │
│           "a"     → puntaje: 0.5                                            │
│           "hello" → puntaje: 8.5   ← ¡EL MÁS ALTO!                          │
│           "world" → puntaje: 2.1                                            │
│           "cat"   → puntaje: -1.3                                           │
│           ... (30,000 puntajes)                                             │
│                                                                             │
│   El puntaje más alto gana. En este caso: "hello"                           │
│                                                                             │
│   ═══════════════════════════════════════════════════════════════════════   │
│                                                                             │
│   RESUMEN:                                                                  │
│                                                                             │
│   512 números ──→ LINEAR ──→ 30,000 puntajes ──→ El más alto gana           │
│   (idea vaga)              (uno por palabra)    (palabra elegida)           │
│                                                                             │
│   Es como: "Tengo una idea" → "¿A qué palabra se parece más?" → "¡Esta!"    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ¿Qué pasa después de LINEAR?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   LINEAR da puntajes "crudos" (pueden ser negativos, mayores que 1, etc.)   │
│                                                                             │
│   Estos puntajes se llaman "LOGITS"                                         │
│                                                                             │
│   Después viene SOFTMAX que convierte los logits en PROBABILIDADES:         │
│                                                                             │
│   ANTES (logits):     "hello"=8.5, "hi"=7.0, "world"=2.1, ...               │
│                              ↓                                              │
│   DESPUÉS (probs):    "hello"=85%, "hi"=10%, "world"=2%, ...                │
│                                                                             │
│   Ahora podemos decir: "hello tiene 85% de probabilidad de ser la palabra"  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## (i) Softmax

### TIPO: 2 - Capa (función de activación)

### ¿Qué es?

Convierte los "logits" (números sin normalizar) en **probabilidades** que suman 1.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            SOFTMAX                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Entrada (logits):     [2.0, 1.0, 0.1, 5.0, ...]  (30,000 números)         │
│                                    │                                        │
│                                    ▼                                        │
│                         softmax(xᵢ) = e^xᵢ / Σⱼ e^xⱼ                        │
│                                    │                                        │
│                                    ▼                                        │
│   Salida (probabilidades): [0.05, 0.02, 0.01, 0.85, ...]                    │
│                                                                             │
│                             ↑                                               │
│                    La palabra 4 tiene 85% de probabilidad                   │
│                    de ser la siguiente palabra                              │
│                                                                             │
│   Propiedades:                                                              │
│   • Todos los valores están entre 0 y 1                                     │
│   • La suma de todos los valores es exactamente 1                           │
│   • El valor más alto corresponde a la palabra más probable                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### En inferencia

Se toma la palabra con mayor probabilidad (o se samplea del top-k para ser más creativo).

---

## (j) Multi-Head Attention (en el decoder - Cross-Attention)

### TIPO: 2 - Capa (operación matemática)

### ¿Qué es?

Es Multi-Head Attention, pero las **Keys (K) y Values (V) vienen del encoder**, mientras que las **Queries (Q) vienen del decoder**.

### ¿Por qué hay dos Multi-Head Attention en el decoder?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│            LOS DOS ATTENTION DEL DECODER                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   1. MASKED SELF-ATTENTION (primero):                                       │
│      • Q, K, V vienen todos del DECODER                                     │
│      • Cada palabra del output mira a las anteriores del output             │
│      • "¿Qué he generado hasta ahora?"                                      │
│                                                                             │
│   2. CROSS-ATTENTION (segundo):                                             │
│      • Q viene del DECODER                                                  │
│      • K, V vienen del ENCODER                                              │
│      • Las palabras del output miran a las del input                        │
│      • "¿Qué parte del input es relevante para lo que genero?"              │
│                                                                             │
│   ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│   Ejemplo traduciendo "Bonjour le monde" → "Hello world":                   │
│                                                                             │
│   Cuando genero "world":                                                    │
│   • Self-Attention: miro "Hello" (lo que ya generé)                         │
│   • Cross-Attention: miro "monde" (la palabra correspondiente en francés)   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Este es el equivalente a Bahdanau Attention

El Cross-Attention del Transformer cumple la misma función que Bahdanau Attention en Seq2Seq:
- Permite al decoder "mirar" toda la secuencia del encoder
- Genera un contexto dinámico para cada paso de generación
- Resuelve el cuello de botella

---

## RESUMEN FINAL

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESUMEN DE COMPONENTES                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   COMPONENTE              │ TIPO │ FUNCIÓN PRINCIPAL                        │
│   ────────────────────────┼──────┼─────────────────────────────────────     │
│   Input Embedding         │  1   │ Palabra → Vector                         │
│   Output Embedding        │  1   │ Palabra → Vector (vocabulario destino)   │
│   Positional Encoding     │  1   │ Agrega información de posición           │
│   Multi-Head Attention    │  2   │ Cada palabra mira a todas (encoder)      │
│   Masked Multi-Head Att.  │  2   │ Decoder mira sus propias palabras        │
│   Cross-Attention         │  2   │ Decoder mira al encoder                  │
│   Feed Forward            │  2   │ MLP que transforma cada posición         │
│   Linear                  │  2   │ Proyecta a tamaño vocabulario            │
│   Softmax                 │  2   │ Convierte a probabilidades               │
│   Add & Norm              │  5   │ Skip connection + normalización          │
│                                                                             │
│   ⚠️  OJO: Masked Multi-Head Att. y Cross-Attention NO son lo mismo:        │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │ MASKED MULTI-HEAD ATTENTION          │ CROSS-ATTENTION             │   │
│   ├─────────────────────────────────────────────────────────────────────┤   │
│   │ Q, K, V del DECODER                  │ Q del DECODER               │   │
│   │                                      │ K, V del ENCODER            │   │
│   ├─────────────────────────────────────────────────────────────────────┤   │
│   │ Palabras generadas se miran          │ Decoder mira al input       │   │
│   │ ENTRE SÍ (solo el pasado)            │ (frase a traducir)          │   │
│   ├─────────────────────────────────────────────────────────────────────┤   │
│   │ "¿Qué generé hasta ahora?"           │ "¿Qué debo traducir?"       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## HISTORIA CRONOLÓGICA: ¿QUÉ PASA PASO A PASO?

Vamos a seguir una traducción completa de "Bonjour le monde" → "Hello world" paso a paso.

---

### FASE 1: PREPARACIÓN DE LA ENTRADA (ENCODER)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 1: INPUT EMBEDDING                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   TENEMOS: La frase en francés "Bonjour le monde"                           │
│                                                                             │
│   HACEMOS:                                                                  │
│   1. Dividimos en tokens: ["Bonjour", "le", "monde"]                        │
│   2. Buscamos cada token en la lista de palabras francesas                  │
│   3. Cada token se convierte en su vector de 512 números                    │
│                                                                             │
│   RESULTADO:                                                                │
│   "Bonjour" → [0.2, -0.5, 0.8, ...(512 números)]                            │
│   "le"      → [0.1, 0.3, -0.2, ...(512 números)]                            │
│   "monde"   → [0.9, 0.1, 0.4, ...(512 números)]                             │
│                                                                             │
│   AHORA TENEMOS: 3 vectores de 512 números cada uno                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 2: POSITIONAL ENCODING                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   PROBLEMA: Los 3 vectores no saben en qué orden están                      │
│                                                                             │
│   HACEMOS:                                                                  │
│   SUMAMOS un vector de posición a cada uno:                                 │
│                                                                             │
│   Vector("Bonjour") + Vector(posición 0) = Vector con posición              │
│   Vector("le")      + Vector(posición 1) = Vector con posición              │
│   Vector("monde")   + Vector(posición 2) = Vector con posición              │
│                                                                             │
│   RESULTADO: Los mismos 3 vectores, pero ahora "saben" su posición          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 3: SELF-ATTENTION (Multi-Head Attention en Encoder)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   OBJETIVO: Que cada palabra entienda su contexto mirando las otras         │
│                                                                             │
│   HACEMOS:                                                                  │
│   Para cada palabra, calculamos:                                            │
│   - Q (Query): ¿qué busco?                                                  │
│   - K (Key): ¿qué ofrezco?                                                  │
│   - V (Value): ¿qué contenido tengo?                                        │
│                                                                             │
│   "Bonjour" mira a "le" y "monde" → ¿cuánto me importan?                    │
│   "le" mira a "Bonjour" y "monde" → ¿cuánto me importan?                    │
│   "monde" mira a "Bonjour" y "le" → ¿cuánto me importan?                    │
│                                                                             │
│   Se hace 8 veces en paralelo (8 "cabezas") cada una buscando               │
│   relaciones diferentes                                                     │
│                                                                             │
│   RESULTADO: 3 vectores ENRIQUECIDOS con información del contexto           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 4: ADD & NORM                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   HACEMOS:                                                                  │
│   1. ADD: Sumamos la entrada original (antes de attention) con la salida    │
│      → Esto permite que el gradiente fluya fácil (skip connection)          │
│                                                                             │
│   2. NORM: Normalizamos los números para que no se vayan a extremos         │
│      → Esto estabiliza el entrenamiento                                     │
│                                                                             │
│   RESULTADO: 3 vectores normalizados                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 5: FEED FORWARD                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   HACEMOS:                                                                  │
│   A cada vector (independientemente) le aplicamos:                          │
│   - Capa 1: Expande de 512 → 2048 números                                   │
│   - ReLU: Si el número es negativo, lo hace 0                               │
│   - Capa 2: Comprime de 2048 → 512 números                                  │
│                                                                             │
│   OBJETIVO: Procesar lo que cada palabra aprendió del contexto              │
│                                                                             │
│   RESULTADO: 3 vectores transformados                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 6: ADD & NORM (de nuevo)                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Lo mismo que el paso 4: sumar entrada + salida, luego normalizar          │
│                                                                             │
│   RESULTADO: 3 vectores listos                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Los pasos 3-6 se repiten N veces** (típicamente N=6). Cada repetición refina más el entendimiento.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   FIN DEL ENCODER                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   RESULTADO FINAL DEL ENCODER:                                              │
│   3 vectores de 512 números cada uno                                        │
│   que representan "Bonjour le monde" con TODO su contexto entendido         │
│                                                                             │
│   Estos vectores se guardan para que el DECODER los use                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### FASE 2: GENERACIÓN DE LA SALIDA (DECODER)

Ahora vamos a generar "Hello world" palabra por palabra.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 7: OUTPUT EMBEDDING + POSITIONAL ENCODING                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   TENEMOS: Lo que ya generamos (al principio, solo "<SOS>")                 │
│                                                                             │
│   HACEMOS:                                                                  │
│   - Convertimos "<SOS>" en vector usando la tabla de palabras INGLESAS      │
│   - Sumamos el positional encoding (posición 0)                             │
│                                                                             │
│   RESULTADO: 1 vector de 512 números representando "<SOS>"                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 8: MASKED SELF-ATTENTION                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   OBJETIVO: Que las palabras generadas se miren entre sí                    │
│             (pero SIN mirar el futuro)                                      │
│                                                                             │
│   HACEMOS:                                                                  │
│   Como solo tenemos "<SOS>", solo puede mirarse a sí mismo                  │
│                                                                             │
│   La MÁSCARA impide ver posiciones futuras (que aún no generamos)           │
│                                                                             │
│   RESULTADO: Vector procesado                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 9: ADD & NORM                                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 10: CROSS-ATTENTION (¡EL PASO CLAVE!)                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   OBJETIVO: Mirar la frase francesa para saber qué traducir                 │
│                                                                             │
│   HACEMOS:                                                                  │
│   - Q (Query) viene del DECODER: "¿qué palabra debo generar ahora?"         │
│   - K y V (Key, Value) vienen del ENCODER: la representación de             │
│     "Bonjour le monde"                                                      │
│                                                                             │
│   El decoder pregunta: "Tengo <SOS>, ¿a qué parte del francés debo mirar?"  │
│   El encoder responde: "Mira sobre todo a 'Bonjour'"                        │
│                                                                             │
│   RESULTADO: Vector enriquecido con información del INPUT                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 11: ADD & NORM                                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 12: FEED FORWARD + ADD & NORM                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Igual que en el encoder: 512 → 2048 → 512                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Los pasos 8-12 se repiten N veces** (típicamente N=6).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 13: LINEAR                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   TENEMOS: Un vector de 512 números                                         │
│                                                                             │
│   HACEMOS:                                                                  │
│   Lo proyectamos a 40,000 números (uno por cada palabra inglesa posible)    │
│                                                                             │
│   RESULTADO: 40,000 números (logits) - uno por palabra                      │
│              "Hello" podría tener 8.5                                       │
│              "World" podría tener 2.1                                       │
│              "Cat" podría tener -3.2                                        │
│              ...                                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   PASO 14: SOFTMAX                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   TENEMOS: 40,000 números (logits)                                          │
│                                                                             │
│   HACEMOS:                                                                  │
│   Convertimos a PROBABILIDADES (números entre 0 y 1 que suman 1)            │
│                                                                             │
│   RESULTADO:                                                                │
│   "Hello" = 0.85  (85% de probabilidad)  ← LA MÁS ALTA                      │
│   "Hi"    = 0.10  (10%)                                                     │
│   "World" = 0.02  (2%)                                                      │
│   ...                                                                       │
│                                                                             │
│   DECISIÓN: Elegimos "Hello" (la de mayor probabilidad)                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### FASE 3: REPETIR PARA LA SIGUIENTE PALABRA

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   ITERACIÓN 2: Generar "world"                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   AHORA TENEMOS: "<SOS>" "Hello"                                            │
│                                                                             │
│   Repetimos los pasos 7-14:                                                 │
│   - Output Embedding convierte ambos en vectores                            │
│   - Masked Self-Attention: "Hello" puede ver a "<SOS>" y a sí mismo         │
│   - Cross-Attention: "Hello" mira al encoder, ve que corresponde "monde"    │
│   - Linear + Softmax → "world" tiene la mayor probabilidad                  │
│                                                                             │
│   RESULTADO: Generamos "world"                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   ITERACIÓN 3: Generar "<EOS>"                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   AHORA TENEMOS: "<SOS>" "Hello" "world"                                    │
│                                                                             │
│   Repetimos los pasos 7-14:                                                 │
│   - El modelo ve que ya tradujo todo                                        │
│   - Linear + Softmax → "<EOS>" tiene la mayor probabilidad                  │
│                                                                             │
│   RESULTADO: Generamos "<EOS>" = FIN                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### RESUMEN DEL FLUJO COMPLETO

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RESUMEN: DE PRINCIPIO A FIN                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ENTRADA: "Bonjour le monde"                                               │
│                │                                                            │
│                ▼                                                            │
│   ┌────────────────────────────────────────┐                                │
│   │ ENCODER                                │                                │
│   │ 1. Input Embedding (palabra→vector)    │                                │
│   │ 2. + Positional Encoding               │                                │
│   │ 3. Self-Attention × N veces            │                                │
│   │ 4. Feed Forward × N veces              │                                │
│   │ (con Add&Norm después de cada uno)     │                                │
│   └────────────────────────────────────────┘                                │
│                │                                                            │
│                ▼                                                            │
│   REPRESENTACIÓN del francés (3 vectores enriquecidos)                      │
│                │                                                            │
│                │◄──────────────────────────────────────┐                    │
│                                                        │                    │
│   ┌────────────────────────────────────────┐           │                    │
│   │ DECODER (genera palabra por palabra)   │           │                    │
│   │ 1. Output Embedding                    │           │                    │
│   │ 2. + Positional Encoding               │           │                    │
│   │ 3. Masked Self-Attention               │           │                    │
│   │ 4. Cross-Attention ◄───────────────────┼───────────┘                    │
│   │    (mira la representación del encoder)│                                │
│   │ 5. Feed Forward                        │                                │
│   │ 6. Linear → Softmax                    │                                │
│   └────────────────────────────────────────┘                                │
│                │                                                            │
│                ▼                                                            │
│   SALIDA: "Hello" (iteración 1)                                             │
│           "world" (iteración 2)                                             │
│           "<EOS>" (iteración 3) → FIN                                       │
│                                                                             │
│   TRADUCCIÓN COMPLETA: "Hello world"                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```
