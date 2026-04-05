Relaciones entre modelos: quién usa qué, y cómo se conectan

---

El profesor dijo: "Este curso va a ser una especie de zoológico de modelos generativos donde vamos a ir viendo las ideas. Porque todos los modelos que hay hoy en día de algún modo usan y mezclan las ideas que vamos a estar visitando."

Este archivo aclara qué es qué, en qué categoría va cada cosa, y cómo se relacionan.

---

1. La jerarquía: no todo es lo mismo

Hay que distinguir entre tres niveles:

CONCEPTOS (ideas matemáticas/teóricas):
- Autorregresión (generar de a uno, condicionado a los anteriores)
- Espacio latente (representación comprimida de los datos)
- Encoder-Decoder (comprimir → descomprimir)
- Adversarial training (dos redes compitiendo)
- Denoising (quitar ruido)
- Attention (decidir a qué prestarle atención)

ARQUITECTURAS (estructuras de red neuronal):
- MLP (capas lineales + activaciones)
- CNN (convoluciones)
- RNN (recurrencia)
- Transformer (self-attention + feed-forward)
- U-Net (encoder-decoder con skip connections)

MODELOS GENERATIVOS (sistemas completos que generan datos):
- Autorregresivo de Hinton (concepto: autorregresión, arquitectura: MLP)
- VAE (concepto: encoder-decoder + espacio latente, arquitectura: CNN o MLP)
- GAN (concepto: adversarial, arquitectura: CNN)
- Difusión / DDPM (concepto: denoising, arquitectura: U-Net)
- Modelos de Lenguaje / GPT (concepto: autorregresión, arquitectura: Transformer)
- Latent Diffusion / Stable Diffusion (concepto: denoising + encoder-decoder + attention, arquitectura: VAE + U-Net + Transformer)

Un Transformer NO es un modelo generativo por sí mismo. Es una ARQUITECTURA que se usa DENTRO de modelos generativos.

---

2. "Encoder-Decoder" significa cosas distintas en cada modelo

El término aparece en VAE, Transformer, U-Net y Latent Diffusion, pero con roles diferentes:

VAE:
- Encoder: imagen → vector latente z (comprime mucho: 64×64 → 128 números)
- Decoder: vector latente z → imagen (reconstruye)
- Propósito: aprender una representación comprimida y organizada

Transformer (traducción):
- Encoder: frase en idioma A → representación contextualizada
- Decoder: representación + historial → frase en idioma B
- Propósito: procesar una secuencia de entrada y generar otra secuencia de salida
- NO comprime a un vector fijo; la salida tiene la misma cantidad de filas que la entrada

U-Net (Difusión):
- Encoder: imagen ruidosa → representación cada vez más pequeña
- Decoder: representación pequeña → predicción del ruido (mismo tamaño que la entrada)
- Propósito: achica y agranda la imagen, con skip connections que preservan detalles
- El espacio latente tiene el MISMO tamaño que la imagen original (no comprime)

GPT / Modelos de Lenguaje:
- Solo usa el Decoder del Transformer (no hay Encoder ni Cross-Attention)
- Es puramente autorregresivo: predice el siguiente token dado los anteriores

Lo que tienen en común: la idea de "procesar información para obtener una representación útil y después generar algo con ella". Lo que cambia es QUÉ se comprime, CUÁNTO se comprime, y PARA QUÉ.

---

3. Ideas compartidas entre modelos

┌─────────────────────────────┬───────┬─────┬─────┬──────────┬─────────────┐
│         Idea                │Hinton │ VAE │ GAN │ Difusión │ LM/GPT      │
├─────────────────────────────┼───────┼─────┼─────┼──────────┼─────────────┤
│ Autorregresión              │  SÍ   │     │     │          │    SÍ       │
│ (generar de a uno)          │       │     │     │          │             │
├─────────────────────────────┼───────┼─────┼─────┼──────────┼─────────────┤
│ Espacio latente comprimido  │       │ SÍ  │ SÍ  │          │             │
│ (datos → vector chico)      │       │     │     │          │             │
├─────────────────────────────┼───────┼─────┼─────┼──────────┼─────────────┤
│ Encoder-Decoder             │       │ SÍ  │     │ SÍ*      │             │
│                             │       │     │     │ (U-Net)  │             │
├─────────────────────────────┼───────┼─────┼─────┼──────────┼─────────────┤
│ Skip Connections            │       │     │     │ SÍ       │ SÍ          │
│                             │       │     │     │ (U-Net)  │ (Transf.)   │
├─────────────────────────────┼───────┼─────┼─────┼──────────┼─────────────┤
│ Self-Attention              │       │     │     │          │ SÍ          │
│                             │       │     │     │          │ (Transf.)   │
├─────────────────────────────┼───────┼─────┼─────┼──────────┼─────────────┤
│ Cross-Attention             │       │     │     │ SÍ**     │             │
│                             │       │     │     │          │             │
├─────────────────────────────┼───────┼─────┼─────┼──────────┼─────────────┤
│ Causal Masking              │  SÍ   │     │     │          │ SÍ          │
│ (no ver el futuro)          │(triang│     │     │          │ (Transf.)   │
│                             │ ular) │     │     │          │             │
├─────────────────────────────┼───────┼─────┼─────┼──────────┼─────────────┤
│ Sinusoidal Encoding         │       │     │     │ SÍ       │ SÍ          │
│                             │       │     │     │(timestep)│(posicional) │
├─────────────────────────────┼───────┼─────┼─────┼──────────┼─────────────┤
│ Reparametrization Trick     │       │ SÍ  │     │ SÍ       │             │
│ (z = μ + σ × ε)            │       │     │     │          │             │
└─────────────────────────────┴───────┴─────┴─────┴──────────┴─────────────┘

 * Difusión usa U-Net que tiene forma encoder-decoder, pero NO comprime el latente.
** Cross-Attention aparece en Stable Diffusion (condicionamiento con texto), no en DDPM básico.

---

4. La cadena de evolución: por qué existe cada modelo

Cada modelo nuevo surgió para solucionar un problema del anterior:

Hinton (Autorregresivo)
  │  Problema: genera de a un píxel → MUY lento
  │
  v
VAE
  │  Solución: genera en UN paso desde un espacio latente comprimido
  │  Problema: imágenes borrosas (porque la loss promedia errores pixel a pixel)
  │
  v
GAN
  │  Solución: genera imágenes nítidas usando un discriminador como juez
  │  Problema: entrenamiento inestable + mode collapse
  │
  v
Difusión
  │  Solución: la calidad de GAN con la estabilidad de VAE
  │  Problema: generación lenta (1000 pasos secuenciales)
  │
  v
Latent Diffusion (Stable Diffusion)
     Solución: comprimir con VAE primero, difundir en espacio chico → mucho más rápido

---

5. Stable Diffusion: el modelo que mezcla TODO

Stable Diffusion es el ejemplo máximo de cómo las ideas se combinan. Usa TRES arquitecturas distintas:

┌─────────────────────────────────────────────────────────────────────────────┐
│                          STABLE DIFFUSION                                   │
│                                                                             │
│  ┌──────────────┐                                                          │
│  │ "un gato     │                                                          │
│  │  astronauta" │                                                          │
│  └──────┬───────┘                                                          │
│         │                                                                   │
│         v                                                                   │
│  ┌──────────────┐                                                          │
│  │    CLIP       │  ← Arquitectura: TRANSFORMER                            │
│  │ (Text Encoder)│    Convierte texto en vectores numéricos                │
│  └──────┬───────┘                                                          │
│         │ embeddings de texto                                               │
│         │ (vectores numéricos que                                           │
│         │  representan el significado                                       │
│         │  del texto; entran como K y V                                     │
│         │  en Cross-Attention)                                              │
│         │                                                                   │
│         v                                                                   │
│  ┌──────────────────────────────────────────────────────────────┐          │
│  │                                                              │          │
│  │  ┌──────────┐      ┌──────────────┐      ┌──────────────┐   │          │
│  │  │ Imagen   │      │              │      │              │   │          │
│  │  │ original │─────>│ VAE ENCODER  │─────>│ Latente 64×64│   │          │
│  │  │ 512×512  │      │ (comprime)   │      │              │   │          │
│  │  └──────────┘      └──────────────┘      └──────┬───────┘   │          │
│  │                                                  │           │          │
│  │  ← Arquitectura: CNN (VAE)                       v           │          │
│  │    Comprime la imagen para                ┌──────────────┐   │          │
│  │    que la difusión trabaje                │   DIFUSIÓN   │   │          │
│  │    en espacio chico                       │   (U-Net)    │   │          │
│  │                                           │              │   │          │
│  │  ← Arquitectura: U-Net + Cross-Attention  │ + texto via  │   │          │
│  │    Quita ruido paso a paso,               │ Cross-Attn   │   │          │
│  │    condicionada por el texto               └──────┬───────┘   │          │
│  │                                                  │           │          │
│  │                                                  v           │          │
│  │                                           ┌──────────────┐   │          │
│  │                                           │ VAE DECODER  │   │          │
│  │                                           │(descomprime) │   │          │
│  │  ← Arquitectura: CNN (VAE)                └──────┬───────┘   │          │
│  │    Agranda el resultado de                       │           │          │
│  │    vuelta a tamaño original               ┌──────────────┐   │          │
│  │                                           │ Imagen nueva │   │          │
│  │                                           │   512×512    │   │          │
│  │                                           └──────────────┘   │          │
│  └──────────────────────────────────────────────────────────────┘          │
│                                                                             │
│  Resumen: CLIP (Transformer) + VAE (CNN) + Difusión (U-Net)                │
│  = tres arquitecturas combinadas en un solo sistema                        │
└─────────────────────────────────────────────────────────────────────────────┘

---

6. Qué se descarta de cada modelo después de entrenar

Otro punto donde los modelos difieren:

│ Modelo       │ Qué se usa para generar         │ Qué se descarta          │
│──────────────│─────────────────────────────────│──────────────────────────│
│ VAE          │ Solo el Decoder                  │ El Encoder               │
│ GAN          │ Solo el Generador                │ El Discriminador         │
│ Difusión     │ Todo el modelo (U-Net completa)  │ Nada                     │
│ LM / GPT     │ Todo el modelo (Transformer)     │ Nada                     │
│ Stable Diff. │ VAE Decoder + U-Net + CLIP       │ VAE Encoder*             │
│──────────────│─────────────────────────────────│──────────────────────────│

* El VAE Encoder solo se usa si querés modificar una imagen existente (img2img).
  Para generar desde cero, se parte de ruido puro y no se necesita el encoder.

---

7. El espacio latente: mismo nombre, distinto significado

│ Modelo       │ Tamaño del latente          │ Relación con los datos        │
│──────────────│─────────────────────────────│───────────────────────────────│
│ VAE          │ Mucho más chico que la      │ Vector comprimido (ej: 128    │
│              │ imagen                       │ números para una imagen       │
│              │                              │ de 64×64 = 4096 píxeles)     │
│──────────────│─────────────────────────────│───────────────────────────────│
│ GAN          │ Mucho más chico que la      │ Vector de ruido (ej: 100     │
│              │ imagen                       │ números → imagen completa)    │
│──────────────│─────────────────────────────│───────────────────────────────│
│ Difusión     │ MISMO tamaño que la imagen  │ No hay compresión real;       │
│ (DDPM)       │                              │ el ruido es del mismo        │
│              │                              │ tamaño que el dato           │
│──────────────│─────────────────────────────│───────────────────────────────│
│ Latent       │ Más chico (gracias al VAE)  │ VAE comprime primero         │
│ Diffusion    │ 512×512 → 64×64             │ (64 veces más chico)         │
│──────────────│─────────────────────────────│───────────────────────────────│
│ LM / GPT     │ No hay espacio latente      │ Puramente autorregresivo,    │
│              │ explícito                    │ no comprime nada             │
│──────────────│─────────────────────────────│───────────────────────────────│

---

8. Las funciones de pérdida comparadas

│ Modelo     │ Loss                              │ Complejidad                │
│────────────│───────────────────────────────────│────────────────────────────│
│ Hinton     │ NLL (Negative Log-Likelihood)      │ Un término                 │
│ VAE        │ Reconstrucción + KL Divergence     │ Dos términos que balancear │
│ GAN        │ BCE para D + BCE para G             │ Dos redes, dos losses      │
│            │ (se optimizan por turnos)           │ separadas por turnos       │
│ Difusión   │ MSE (ruido real - ruido predicho)²  │ Un solo número. La más     │
│            │                                     │ simple del curso.          │
│ LM / GPT   │ Cross-Entropy = -log(prob correcta)│ Un término (= NLL)         │
│────────────│───────────────────────────────────│────────────────────────────│

Observación del profesor: la loss de Difusión es "increíblemente simple comparada con VAE (dos términos) y GAN (dos redes)".

---

Resumen de relaciones en una oración cada una

Hinton → GPT: misma idea autorregresiva (de a uno, sin ver el futuro), pero Hinton usa MLP con píxeles y GPT usa Transformer con tokens.

VAE → Stable Diffusion: el VAE comprime y descomprime la imagen; Stable Diffusion hace toda la difusión en ese espacio comprimido.

Transformer → GPT: GPT usa solo el Decoder del Transformer, sin Encoder ni Cross-Attention.

Transformer → Stable Diffusion: CLIP (un Transformer) codifica el texto, y ese texto entra via Cross-Attention a la U-Net de difusión.

Hinton → Transformer (Decoder): ambos usan la misma idea de no ver el futuro; Hinton con una matriz triangular de pesos, el Transformer con Causal Masking (-∞ antes del softmax).

VAE ↔ Difusión: ambos usan el Reparametrization Trick (z = μ + σ × ε) para hacer muestreo diferenciable.

U-Net ↔ Transformer: ambos usan sinusoidal encoding (la U-Net para el timestep t, el Transformer para la posición de cada palabra) y skip connections.

GAN vs todos: es el único que NO tiene ninguna forma de encoder ni estructura encoder-decoder. Solo tiene Generador (expande ruido) y Discriminador (clasifica real/falso).
