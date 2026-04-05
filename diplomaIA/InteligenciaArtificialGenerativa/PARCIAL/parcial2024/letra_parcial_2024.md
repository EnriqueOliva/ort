# Letra Parcial - Inteligencia Artificial Generativa 2024

**Facultad de Ingeniería - Universidad ORT**

| | |
|---|---|
| **Fecha:** 09/12/2024 | **Duración:** 2 h |
| **Evaluación:** Parcial | **Uso de Calculadora:** SI |
| **Materia:** Inteligencia Artificial Generativa | **Uso de Material:** NO |
| **Turno:** Nocturno | **Puntaje Máximo/Mínimo:** 30/1 Puntos |

---

## Ejercicio 1 - Language Models (LMs) (10 puntos)

1. ¿Qué es un Language Model?

2. Implementa en pseudocódigo el proceso de generación de secuencias de un LM.

3. ¿Existe alguna diferencia a la hora de muestrear si este LM es un transformer, un MLP o una RNN?

---

## Ejercicio 2 - Generative Adversarial Networks (GANs) (8 puntos)

1. Explica, con un esquema y pseudocódigo el funcionamiento de las GANs, tanto en entrenamiento cómo en inferencia.

   Se espera que se discuta: Arquitectura general, régimen de entrenamiento, régimen de inferencia.

2. ¿Cuáles son las dificultades presentes al entrenar este tipo de arquitectura?

   Se espera que haga un punteo y explique en no más de 2 renglones cada dificultad identificada.

---

## Ejercicio 3 - Diffusion Models (4 puntos)

1. Implementa en pseudocódigo el paso de inferencia de un modelo de difusión para generar nuevas muestras. Explica cada paso del proceso.

---

## Ejercicio 4 - Variational Autoencoders (VAEs) (8 puntos)

1. La siguiente imagen presenta la reparameterización de la expresión de las VAEs.

   ### Reparametrizing the sampling layer

   ```
   Original form:                    Reparametrized form:

        ┌───┐                              ┌───┐
        │ f │                    Backprop  │ f │
        └─┬─┘                        ↓     └─┬─┘
          │                         ∂f/∂z    │
        ┌─┴─┐                       ↓      ┌─┴─┐
        │ z │  z ~ p_φ(z|x)               │ z │  z = g(φ, x, ε)
        └─┬─┘                       ↓     └─┬─┘
          │                        ∂f/∂φ    │         ┌───┐
        ┌─┴─┐                       ↓      ┌─┴─┐      │ ε │ ~ N(0,1)
        │ φ │───────│ x │                 │ φ │──│ x │──┴───┘
        └───┘       └───┘                 └───┘  └───┘

   ◆ Deterministic node
   ● Stochastic node
   ```

   **Se pide:** Explique, al menos intuitivamente, porque es necesaria la forma reparametrizada de esta expresión en el contexto del entrenamiento de las VAEs.

2. La siguiente fórmula expresa el término de Loss utilizado para entrenar VAEs.

   ```
   log p_θ(x^(i)) ≥ L(x^(i), θ, φ) = E_z[log p_θ(x^(i) | z)] - D_KL(q_φ(z | x^(i)) || p_θ(z))
                                     \_____________________/   \__________________________/
                                      Reconstruct the Input Data       KL Divergence

   θ*, φ* = arg max_{θ,φ} Σ_{i=1}^{N} L(x^(i), θ, φ)
   ```

   **Se pide:** Explique brevemente qué función cumple cada sumando.
