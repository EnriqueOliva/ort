# Los 4 "POR QUÉ" del Mecanismo de Attention

Este archivo explica la **cadena de razonamiento** que lleva desde Seq2Seq básico hasta el Transformer completo. Cada "por qué" resuelve un problema específico del paso anterior.

---

## La Cadena de Problemas y Soluciones

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    DE SEQ2SEQ A TRANSFORMER: LOS 4 "POR QUÉ"                        │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   PROBLEMA 1                        SOLUCIÓN 1                                      │
│   ──────────                        ──────────                                      │
│   Vector de contexto FIJO           ATTENTION (Bahdanau)                            │
│   es un cuello de botella           Contexto DINÁMICO Cᵢ                            │
│              │                                │                                     │
│              └────────────────────────────────┘                                     │
│                                               │                                     │
│                                               ▼                                     │
│   PROBLEMA 2                        SOLUCIÓN 2                                      │
│   ──────────                        ──────────                                      │
│   Bahdanau solo mira                SELF-ATTENTION                                  │
│   encoder → decoder                 Cada palabra mira a TODAS                       │
│   (no captura contexto interno)     (incluso dentro de la misma secuencia)          │
│              │                                │                                     │
│              └────────────────────────────────┘                                     │
│                                               │                                     │
│                                               ▼                                     │
│   PROBLEMA 3                        SOLUCIÓN 3                                      │
│   ──────────                        ──────────                                      │
│   Self-Attention es INVARIANTE      POSITIONAL ENCODING                             │
│   a permutaciones (no sabe orden)   Suma información de posición                    │
│              │                                │                                     │
│              └────────────────────────────────┘                                     │
│                                               │                                     │
│                                               ▼                                     │
│   PROBLEMA 4                        SOLUCIÓN 4                                      │
│   ──────────                        ──────────                                      │
│   Un solo attention captura         MULTI-HEAD ATTENTION                            │
│   un solo tipo de relación          Múltiples "expertos" en paralelo                │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

# 1. POR QUÉ ATTENTION: El Vector Fijo Era Limitante

## El Problema: Cuello de Botella en Seq2Seq

En la arquitectura Seq2Seq **sin** attention:

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           SEQ2SEQ SIN ATTENTION                                     │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   ENCODER procesa: "El gato negro que vi ayer en el parque estaba durmiendo"        │
│                                                                                     │
│   "El" → h₁                                                                         │
│   "gato" → h₂                                                                       │
│   "negro" → h₃           Todos estos estados intermedios                            │
│   "que" → h₄             SE PIERDEN. Solo guardamos                                 │
│   "vi" → h₅              el ÚLTIMO estado.                                          │
│   ...                           │                                                   │
│   "durmiendo" → h₁₂ ────────────┘                                                   │
│                    │                                                                │
│                    ▼                                                                │
│              ┌───────────┐                                                          │
│              │ CONTEXTO  │  ← Vector de tamaño FIJO (ej: 256 dimensiones)           │
│              │    C      │     TODA la información debe caber aquí                  │
│              └─────┬─────┘                                                          │
│                    │                                                                │
│                    ▼                                                                │
│   DECODER usa el MISMO C para generar TODAS las palabras:                           │
│                                                                                     │
│   C + <SOS> → "The"                                                                 │
│   C + "The" → "black"      ← Siempre el MISMO C                                     │
│   C + "black" → "cat"      ← No importa qué palabra genero                          │
│   ...                                                                               │
│                                                                                     │
│   ⚠️  PROBLEMA: Para traducir "durmiendo" necesito recordar el principio            │
│                 de la oración, pero C ya "olvidó" esa información.                  │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## La Solución: Attention (Bahdanau, 2014)

**Idea clave:** En lugar de un solo C fijo, calcular un **contexto diferente Cᵢ** para cada palabra que genera el decoder.

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           SEQ2SEQ CON ATTENTION                                     │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   ENCODER procesa y GUARDA TODOS los estados:                                       │
│                                                                                     │
│   "El" → h₁ ─────────┐                                                              │
│   "gato" → h₂ ───────┤                                                              │
│   "negro" → h₃ ──────┼─────▶  TODOS los hⱼ se GUARDAN                               │
│   ...                │                                                              │
│   "durmiendo" → h₁₂ ─┘                                                              │
│                      │                                                              │
│                      ▼                                                              │
│              ┌───────────────────┐                                                  │
│              │  MECANISMO        │                                                  │
│              │  ATTENTION        │                                                  │
│              │                   │                                                  │
│              │  Para cada paso i:│                                                  │
│              │  Cᵢ = Σⱼ αᵢⱼ × hⱼ │  ← Promedio ponderado de TODOS los h             │
│              └─────────┬─────────┘                                                  │
│                        │                                                            │
│        ┌───────────────┼───────────────┐                                            │
│        ▼               ▼               ▼                                            │
│       C₁              C₂              C₃        (contextos DIFERENTES)              │
│   (enfoca h₁)     (enfoca h₂)     (enfoca h₁₂)                                      │
│        │               │               │                                            │
│        ▼               ▼               ▼                                            │
│   genera "The"   genera "cat"   genera "sleeping"                                   │
│                                                                                     │
│   ✅ Cada palabra generada puede "mirar" la parte relevante del input               │
│   ✅ Ya no hay cuello de botella                                                    │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Fórmula del Cambio

```
ANTES (Seq2Seq):     P(yᵢ) = f(C,  sᵢ₋₁, yᵢ₋₁)    ← C fijo para todo
DESPUÉS (Attention): P(yᵢ) = f(Cᵢ, sᵢ₋₁, yᵢ₋₁)    ← Cᵢ cambia en cada paso

donde: Cᵢ = Σⱼ αᵢⱼ × hⱼ
       αᵢⱼ = softmax(score(sᵢ₋₁, hⱼ))
```

---

# 2. POR QUÉ SELF-ATTENTION: Para Capturar Contexto Interno

## El Problema: Bahdanau Solo Mira Encoder → Decoder

Bahdanau Attention resuelve el cuello de botella, pero tiene una limitación:

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    LIMITACIÓN DE BAHDANAU ATTENTION                                 │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   Bahdanau Attention:                                                               │
│                                                                                     │
│        ENCODER                              DECODER                                 │
│   ┌──────────────┐                    ┌──────────────┐                              │
│   │ h₁ h₂ h₃ h₄  │ ──── attention ───▶│ s₁ s₂ s₃    │                              │
│   └──────────────┘                    └──────────────┘                              │
│                                                                                     │
│   ⚠️  PROBLEMA: Las palabras del ENCODER no se miran ENTRE SÍ.                      │
│                 Las palabras del DECODER no se miran ENTRE SÍ.                      │
│                                                                                     │
│   Ejemplo: "The bank by the river was steep"                                        │
│                                                                                     │
│   ¿Qué significa "bank"?                                                            │
│   - ¿Banco financiero? ❌                                                           │
│   - ¿Orilla del río? ✓                                                              │
│                                                                                     │
│   Para saber qué significa "bank", NECESITO mirar "river" que está                  │
│   en la MISMA secuencia. Pero con Bahdanau, las palabras del encoder                │
│   no se comunican entre sí - solo el decoder mira al encoder.                       │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## La Solución: Self-Attention

**Idea clave:** Cada palabra mira a **TODAS** las demás palabras de la **misma secuencia**.

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              SELF-ATTENTION                                         │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   Secuencia: "The bank by the river"                                                │
│                                                                                     │
│   Con Self-Attention, CADA palabra puede mirar a TODAS las demás:                   │
│                                                                                     │
│        "The"  "bank"  "by"  "the"  "river"                                          │
│          │      │      │      │       │                                             │
│          ▼      ▼      ▼      ▼       ▼                                             │
│        ┌─────────────────────────────────┐                                          │
│        │       SELF-ATTENTION            │                                          │
│        │                                 │                                          │
│        │  Cada palabra genera Q, K, V    │                                          │
│        │  Cada Q mira todos los K        │                                          │
│        │  Resultado: contexto enriquecido│                                          │
│        └─────────────────────────────────┘                                          │
│          │      │      │      │       │                                             │
│          ▼      ▼      ▼      ▼       ▼                                             │
│        "The"  "bank"  "by"  "the"  "river"                                          │
│               (ahora sabe que                                                       │
│                es "orilla")                                                         │
│                                                                                     │
│   ─────────────────────────────────────────────────────────────────────────────     │
│                                                                                     │
│   Matriz de atención para "bank":                                                   │
│                                                                                     │
│              The   bank   by   the   river                                          │
│   bank  [   0.05  0.10  0.05  0.05  0.75  ]  ← "bank" presta 75% atención a "river" │
│                                                                                     │
│   Ahora "bank" SABE que está relacionado con "river" → es "orilla", no "banco"      │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Diferencia Clave

| Bahdanau Attention | Self-Attention |
|-------------------|----------------|
| Decoder mira al Encoder | Cada palabra mira a TODAS (misma secuencia) |
| Comunicación unidireccional | Comunicación total |
| Q del decoder, K/V del encoder | Q, K, V todos de la misma secuencia |
| Resuelve cuello de botella | Captura contexto interno |

---

# 3. POR QUÉ POSITIONAL ENCODING: Invariancia por Permutaciones

## El Problema: Self-Attention No Sabe el Orden

Self-Attention tiene un problema matemático fundamental:

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    EL PROBLEMA DE LA INVARIANCIA POR PERMUTACIONES                  │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   Self-Attention calcula:                                                           │
│                                                                                     │
│   Attention(Q, K, V) = softmax(QKᵀ) × V                                             │
│                                                                                     │
│   Esta operación es INVARIANTE A PERMUTACIONES.                                     │
│   Es decir, si cambio el orden de las palabras, ¡el resultado es el mismo!          │
│                                                                                     │
│   ─────────────────────────────────────────────────────────────────────────────     │
│                                                                                     │
│   EJEMPLO:                                                                          │
│                                                                                     │
│   Oración A: "El perro mordió al hombre"                                            │
│   Oración B: "El hombre mordió al perro"                                            │
│                                                                                     │
│   Mismas palabras, diferente orden → SIGNIFICADOS OPUESTOS                          │
│                                                                                     │
│   Pero para Self-Attention (sin positional encoding):                               │
│                                                                                     │
│   Embeddings de A: {E("El"), E("perro"), E("mordió"), E("al"), E("hombre")}         │
│   Embeddings de B: {E("El"), E("hombre"), E("mordió"), E("al"), E("perro")}         │
│                                                                                     │
│   ¡Son el MISMO CONJUNTO! Solo cambia el orden.                                     │
│   Self-Attention produce el MISMO resultado porque:                                 │
│   - Los productos punto Q·K son los mismos (solo cambia el orden)                   │
│   - El promedio ponderado es el mismo                                               │
│                                                                                     │
│   ⚠️  El modelo NO PUEDE distinguir estas dos oraciones.                            │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## ¿Por Qué la RNN No Tiene Este Problema?

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    RNN vs TRANSFORMER: ORDEN DE PALABRAS                            │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   RNN:                                                                              │
│   ────                                                                              │
│   Procesa SECUENCIALMENTE: palabra 1 → palabra 2 → palabra 3 → ...                  │
│   El orden está IMPLÍCITO en el orden de procesamiento.                             │
│   h₃ sabe que viene después de h₂ porque se calculó después.                        │
│                                                                                     │
│   TRANSFORMER:                                                                      │
│   ────────────                                                                      │
│   Procesa EN PARALELO: todas las palabras al mismo tiempo.                          │
│   No hay orden implícito → necesita información EXPLÍCITA de posición.              │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## La Solución: Positional Encoding

**Idea clave:** SUMAR un vector único para cada posición al embedding.

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           POSITIONAL ENCODING                                       │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   ANTES (sin posición):                                                             │
│                                                                                     │
│   "perro" en posición 2  →  E("perro") = [0.2, -0.5, 0.8, ...]                       │
│   "perro" en posición 5  →  E("perro") = [0.2, -0.5, 0.8, ...]  ← ¡IGUAL!           │
│                                                                                     │
│   ─────────────────────────────────────────────────────────────────────────────     │
│                                                                                     │
│   DESPUÉS (con positional encoding):                                                │
│                                                                                     │
│   "perro" en posición 2:                                                            │
│   E("perro")           = [0.2, -0.5, 0.8, ...]                                       │
│   PE(pos=2)            = [0.9,  0.1, 0.4, ...]   (calculado con seno/coseno)         │
│                          ─────────────────────                                      │
│   Entrada al modelo    = [1.1, -0.4, 1.2, ...]   ← DIFERENTE                        │
│                                                                                     │
│   "perro" en posición 5:                                                            │
│   E("perro")           = [0.2, -0.5, 0.8, ...]                                       │
│   PE(pos=5)            = [0.1, -0.7, 0.2, ...]   (diferente patrón)                  │
│                          ─────────────────────                                      │
│   Entrada al modelo    = [0.3, -1.2, 1.0, ...]   ← DIFERENTE                        │
│                                                                                     │
│   ✅ Ahora el modelo puede distinguir "perro" en posición 2 vs posición 5           │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Las Fórmulas del Positional Encoding

```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))    ← dimensiones pares
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))    ← dimensiones impares
```

**¿Por qué seno y coseno?**
- Cada posición tiene un patrón ÚNICO
- Posiciones cercanas tienen patrones SIMILARES
- El modelo puede aprender relaciones de distancia relativa
- Es determinístico (no requiere entrenamiento)

---

# 4. POR QUÉ MULTI-HEAD: Capturar Diferentes Relaciones

## El Problema: Un Solo Attention Captura Un Solo Tipo de Relación

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│               LIMITACIÓN DE SINGLE-HEAD ATTENTION                                   │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   Oración: "The animal didn't cross the street because it was too tired"            │
│                                                                                     │
│   ¿A qué se refiere "it"?                                                           │
│   → Se refiere a "animal" (porque está cansado)                                     │
│                                                                                     │
│   Con UN SOLO attention, el modelo aprende UNA forma de calcular relaciones.        │
│   Pero las palabras tienen MÚLTIPLES tipos de relaciones:                           │
│                                                                                     │
│   RELACIÓN GRAMATICAL:                                                              │
│   "animal" ←──── sujeto de ────→ "didn't cross"                                     │
│   "it" ←──── pronombre que reemplaza ────→ "animal"                                 │
│                                                                                     │
│   RELACIÓN SEMÁNTICA:                                                               │
│   "tired" ←──── describe estado de ────→ "animal/it"                                │
│                                                                                     │
│   RELACIÓN DE POSICIÓN:                                                             │
│   "it" ←──── está cerca de ────→ "street" (pero NO se refiere a street)             │
│                                                                                     │
│   ⚠️  Un solo attention tiene que elegir QUÉ tipo de relación capturar.             │
│       No puede capturar TODAS simultáneamente.                                      │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## La Solución: Multi-Head Attention

**Idea clave:** Ejecutar **h** mecanismos de attention **en paralelo**, cada uno con sus propias matrices W^Q, W^K, W^V.

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           MULTI-HEAD ATTENTION                                      │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   En lugar de 1 attention, tenemos h = 8 "cabezas" en paralelo:                     │
│                                                                                     │
│                              Entrada X                                              │
│                                  │                                                  │
│            ┌──────────┬──────────┼──────────┬──────────┐                            │
│            ▼          ▼          ▼          ▼          ▼                            │
│        ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐                        │
│        │Head 1 │  │Head 2 │  │Head 3 │  │Head 4 │  │ ...   │                        │
│        │       │  │       │  │       │  │       │  │       │                        │
│        │W¹_Q   │  │W²_Q   │  │W³_Q   │  │W⁴_Q   │  │       │                        │
│        │W¹_K   │  │W²_K   │  │W³_K   │  │W⁴_K   │  │       │                        │
│        │W¹_V   │  │W¹_V   │  │W³_V   │  │W⁴_V   │  │       │                        │
│        └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘                        │
│            │          │          │          │          │                            │
│            ▼          ▼          ▼          ▼          ▼                            │
│          [d_v]      [d_v]      [d_v]      [d_v]      [d_v]                           │
│            │          │          │          │          │                            │
│            └──────────┴──────────┴──────────┴──────────┘                            │
│                                  │                                                  │
│                                  ▼                                                  │
│                           ┌───────────┐                                             │
│                           │ CONCATENAR│                                             │
│                           │ [h × d_v] │                                             │
│                           └─────┬─────┘                                             │
│                                 │                                                   │
│                                 ▼                                                   │
│                           ┌───────────┐                                             │
│                           │    W^O    │  ← Proyección final                         │
│                           │[d_model]  │                                             │
│                           └─────┬─────┘                                             │
│                                 │                                                   │
│                                 ▼                                                   │
│                              Salida                                                 │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## ¿Qué Aprende Cada Cabeza?

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│              EJEMPLO: QUÉ APRENDE CADA CABEZA                                       │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   Oración: "The cat sat on the mat"                                                 │
│                                                                                     │
│   CABEZA 1 - Relaciones gramaticales (sujeto-verbo):                                │
│   ─────────────────────────────────────────────────                                 │
│   "sat" presta atención a: "cat" (0.8), "The" (0.1), otros (0.1)                    │
│   → Aprendió que el verbo mira al sujeto                                            │
│                                                                                     │
│   CABEZA 2 - Relaciones de posición (palabras cercanas):                            │
│   ───────────────────────────────────────────────────                               │
│   "on" presta atención a: "sat" (0.4), "the" (0.4), otros (0.2)                     │
│   → Aprendió a mirar vecinos inmediatos                                             │
│                                                                                     │
│   CABEZA 3 - Relaciones semánticas:                                                 │
│   ──────────────────────────────────                                                │
│   "mat" presta atención a: "sat" (0.5), "on" (0.3), otros (0.2)                     │
│   → Aprendió la relación "sentarse sobre algo"                                      │
│                                                                                     │
│   CABEZA 4 - Artículos y sustantivos:                                               │
│   ────────────────────────────────────                                              │
│   "The" presta atención a: "cat" (0.9), otros (0.1)                                 │
│   → Aprendió que "The" modifica al sustantivo siguiente                             │
│                                                                                     │
│   ... y así cada cabeza especializa en un tipo de relación diferente.               │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## ¿Por Qué Dividir d_model Entre h Cabezas?

```
OPCIÓN A (no usada): h cabezas de d_model cada una
    → Costo computacional: h × d_model² = 8 × 512² = muy caro

OPCIÓN B (usada): h cabezas de d_k = d_model/h cada una
    → d_k = 512/8 = 64 por cabeza
    → Al concatenar: 8 × 64 = 512 = d_model
    → Costo similar a single-head, pero más expresivo
```

---

# RESUMEN: La Cadena Completa

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              RESUMEN VISUAL                                         │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│   SEQ2SEQ (RNN)                                                                     │
│       │                                                                             │
│       │ Problema: Cuello de botella (vector C fijo)                                 │
│       ▼                                                                             │
│   + ATTENTION (Bahdanau)  →  Cᵢ dinámico para cada palabra                          │
│       │                                                                             │
│       │ Problema: Solo decoder→encoder, no contexto interno                         │
│       ▼                                                                             │
│   + SELF-ATTENTION  →  Cada palabra mira a todas las demás                          │
│       │                                                                             │
│       │ Problema: No sabe el orden (invariante a permutaciones)                     │
│       ▼                                                                             │
│   + POSITIONAL ENCODING  →  Suma información de posición                            │
│       │                                                                             │
│       │ Problema: Un attention = un tipo de relación                                │
│       ▼                                                                             │
│   + MULTI-HEAD  →  h "expertos" capturando relaciones diferentes                    │
│       │                                                                             │
│       ▼                                                                             │
│   = TRANSFORMER                                                                     │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Clasificación por TIPO

| Concepto | TIPO | Qué resuelve |
|----------|------|--------------|
| Attention (Bahdanau) | MECANISMO (se agrega a Seq2Seq) | Cuello de botella |
| Self-Attention | CAPA (TIPO 2) | Captura contexto interno |
| Positional Encoding | REPRESENTACIÓN (TIPO 1) | Invariancia por permutaciones |
| Multi-Head Attention | CAPA (TIPO 2) | Captura múltiples relaciones |
