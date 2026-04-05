# Letra Parcial - Inteligencia Artificial Generativa 2025

**Facultad de Ingeniería - Universidad ORT**

| | |
|---|---|
| **Fecha:** 09/12/2025 | **Duración:** 2 h |
| **Evaluación:** Parcial | **Uso de Calculadora:** SI |
| **Materia:** Inteligencia Artificial Generativa | **Uso de Material:** NO |
| **Turno:** Nocturno | **Puntaje Máximo/Mínimo:** 30/1 Puntos |

---

## Ejercicio 1 - Language Models (LMs) (8 puntos)

Seleccione la opción correcta en cada ítem:

1. ¿Qué es un Language Model?

   A. Un modelo que clasifica textos en categorías fijas.
   B. Un modelo que corrige errores gramaticales.
   C. Un modelo que traduce entre idiomas automáticamente.
   D. Un modelo que asigna probabilidades a secuencias de texto y predice tokens futuros.

2. ¿Por qué un LM necesita tokenizar el texto?

   A. Para eliminar palabras irrelevantes.
   B. Para reducir el tamaño del documento.
   C. Para poder representar el texto como números procesables por una red neuronal.
   D. Para detectar automáticamente la sintaxis.

3. En un LM autorregresivo, la probabilidad de una secuencia x₁, x₂, ...xₙ se factoriza como:

   A. P(x) = Σᵢ P(xᵢ)
   B. P(x) = Πᵢ P(xᵢ|x≠ᵢ)
   C. P(x) = P(x₁, x₂)
   D. P(x) = Πᵢ P(xᵢ|x<ᵢ)

4. Cuando un LM procesa la frase "Hola, hoy es":

   A. Considera cada palabra por separado, sin contexto.
   B. Calcula la probabilidad del siguiente token dependiente del contexto de toda la frase.
   C. Busca en memoria respuestas predefinidas.
   D. Ignora las palabras iniciales y predice solo en función de "es".

5. El siguiente token después de "Hola, hoy es" se obtiene:

   A. Calculando la distribución de probabilidad en el corpus.
   B. Muestreando de la distribución de probabilidad que el modelo asigna a todos los posibles tokens siguientes.
   C. Usando una tabla fija de respuestas.
   D. Repitiendo el último token.

6. (Justificar en no más de 2 líneas.)

   ¿Por qué un LM utiliza embeddings para representar tokens?

---

## Ejercicio 2 - Generative Adversarial Networks (GANs) (8 puntos)

1. La siguiente expresión corresponde a la pérdida adversarial utilizada en GANs clásicas:

   ```
   min_G max_D  E_{x~p_data}[log D(x)] + E_{z~p(z)}[log(1 - D(G(z)))]
   ```

   Explique brevemente el rol de cada uno de los dos términos y cómo se relacionan con los objetivos del generador y el discriminador.

2. Describa en pseudocódigo simple cómo se entrena la GAN.
   Debe incluir:

   a. muestras reales.
   b. muestras falsas.
   c. actualización de D.
   d. actualización de G.

3. ¿Cómo se generan nuevas muestras durante la inferencia? (Explique en 1 o 2 líneas.)

---

## Ejercicio 3 - Diffusion Models (6 puntos)

Dada la siguiente imagen:

```
                    q(x_t | x_{t-1})
x₀  ──→  ...  ──→  x_{t-1}  ──→  x_t  ──→  ...  ──→  x_T
                    ←──────────────────
                    p_θ(x_{t-1} | x_t)
```

Explique a alto nivel qué significa "aprender a invertir el proceso de difusión" y por qué esto permite generar imágenes desde ruido.

---

## Ejercicio 4 - Variational Autoencoders (VAEs) (8 puntos)

1. Dado el siguiente desarrollo que presenta una equivalencia para el gradiente de una esperanza sobre una distribución parametrizada por θ:

   ```
   ∇_θ E_{p_θ(z)}[f_θ(z)] = ∇_θ ∫ p_θ(z) f_θ(z) dz

                            = ∫ ∇_θ [p_θ(z) f_θ(z)] dz

                            = ∫ f_θ(z) ∇_θ p_θ(z) dz  +  ∫ p_θ(z) ∇_θ f_θ(z) dz

                            = ∫ f_θ(z) ∇_θ p_θ(z) dz  +  E_z[∇_θ f_θ(z)]
   ```

   Se pide:

   a. Explique por qué este término NO puede estimarse directamente mediante muestreo Monte Carlo usando muestras de p_θ(z).

   b. Describa qué problema práctico genera esto al entrenar modelos como las VAEs.

   c. Mencione la idea general de cómo la reparametrización soluciona esta limitación.

2. La siguiente fórmula expresa el término de Loss utilizado para entrenar VAEs.

   ```
   log p_θ(x^(i)) ≥ L(x^(i), θ, φ) = E_z[log p_θ(x^(i) | z)]  -  D_KL(q_φ(z | x^(i)) || p_θ(z))
                                       \______________________/     \____________________________/
                                        Reconstruct the Input Data          KL Divergence

   θ*, φ* = arg max_{θ,φ} Σ_{i=1}^{N} L(x^(i), θ, φ)
   ```

   Explique por qué el KL tiende a regularizar el espacio latente y qué ocurriría si se retirara completamente.
