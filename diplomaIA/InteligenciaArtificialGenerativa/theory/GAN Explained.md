Aquí está la explicación de GANs con la misma estructura que la de VAE:

---

1. Idea central

No hay encoder ni decoder. En vez de eso, hay dos redes que compiten entre sí:

Generador (G): un falsificador. Recibe ruido aleatorio y trata de crear imágenes falsas que parezcan reales.

Discriminador (D): un policía. Recibe una imagen y dice si es real o falsa (un número entre 0 y 1, donde 1 significa "creo que es real").

El generador mejora porque quiere engañar al discriminador.
El discriminador mejora porque quiere no ser engañado.

2. Entrada del Generador

Ruido aleatorio Z, un vector de números (ej: 100 valores) muestreados de una Gaussiana estándar N(0,1). No recibe ninguna imagen.

3. Generador (G)

El generador toma ese ruido Z y lo transforma en una imagen.
No comprime nada (no hay encoder): directamente expande ruido en una imagen completa.

4. Discriminador (D)

El discriminador recibe una imagen (puede ser real del dataset o falsa del generador) y produce un solo número entre 0 y 1:
- Cerca de 1: "creo que es real"
- Cerca de 0: "creo que es falsa"

Es un clasificador binario (real vs falso) que usa Sigmoid al final para dar una probabilidad.

5. Entrenamiento alternado

No se entrenan las dos redes al mismo tiempo. Se alternan por turnos:

Turno 1 — Entrenar el Discriminador (G congelado):
- Se le muestran imágenes reales → D debe decir 1
- Se le muestran imágenes falsas de G → D debe decir 0
- Se actualizan solo los pesos de D

Turno 2 — Entrenar el Generador (D congelado):
- G genera imágenes falsas
- Se pasan por D
- Queremos que D diga 1 (que crea que son reales)
- Se actualizan solo los pesos de G

Se repiten ambos turnos muchas veces.

6. El .detach()

Cuando entrenamos D con imágenes falsas, usamos .detach() en las imágenes generadas.
Esto corta la conexión de gradientes: los gradientes NO llegan a G.
Así solo se actualizan los pesos de D.

Sin .detach(), al entrenar D los gradientes pasarían por G y lo modificarían, que es lo opuesto a lo que queremos en ese turno.

7. El truco del flipeo (label flip)

Cuando entrenamos G, aunque las imágenes son falsas, le ponemos etiqueta 1 (real).
No es que estemos mintiendo: es un truco matemático que produce gradientes más grandes y útiles al inicio, cuando G todavía genera basura.
Si usáramos etiqueta 0, los gradientes serían casi cero y G no aprendería.

📌 Entrenamiento (qué optimiza la GAN)

La función de pérdida se basa en BCE (Binary Cross-Entropy), la misma función que se usó para entrenar el modelo autorregresivo de Hinton.

a) Pérdida del Discriminador

Mide qué tan bien D clasifica imágenes reales como reales y falsas como falsas.

Loss_D = BCE(D(imagen_real), 1) + BCE(D(imagen_falsa.detach()), 0)

Dos partes sumadas:
- Primera: D recibe reales, queremos que diga 1. Si acierta, pérdida baja.
- Segunda: D recibe falsas, queremos que diga 0. Si acierta, pérdida baja.

Minimizar esta pérdida hace que D sea mejor detective.

b) Pérdida del Generador

Mide qué tan bien G engaña a D.

Loss_G = BCE(D(imagen_falsa), 1)

Una sola parte:
- G genera una imagen falsa, la pasa por D, y queremos que D diga 1.
- Si D dice 1 (G lo engañó), pérdida baja.
- Si D dice 0 (G no lo engañó), pérdida alta.

Minimizar esta pérdida hace que G sea mejor falsificador.

c) Balance

No hay una pérdida total que sume ambas. Son dos pérdidas separadas que se optimizan por turnos.

El equilibrio es fundamental:
- Si D aprende demasiado rápido: los gradientes que llegan a G son casi cero y G no aprende nada.
- Si G aprende demasiado rápido: D no puede seguirle el ritmo.
- Solución típica: learning rate de D más bajo que el de G (ej: lr_D = 0.00005, lr_G = 0.0002).

📌 Problemas conocidos

a) Mode collapse

G descubre que un tipo de imagen engaña a D y solo genera ese tipo. Por ejemplo, solo genera 3's y 7's e ignora el resto de dígitos. Nada en el modelo incentiva variedad.

b) Inestabilidad

Es muy difícil mantener G y D equilibrados. A veces el entrenamiento colapsa y hay que reiniciar de cero. Las losses oscilan sin indicar claramente si el modelo mejora.

c) Vanishing gradients

Si D es demasiado bueno al inicio, detecta todo con 100% de confianza. Los gradientes que llegan a G son casi cero y G queda estancado.

📌 Uso después del entrenamiento

1. Generación
   Ruido Z aleatorio → Generador → imagen nueva.
   Solo se usa G. El discriminador se descarta.

2. No hay reconstrucción
   A diferencia del VAE, no se puede "comprimir" una imagen existente. Solo se pueden crear nuevas desde ruido.

Diagrama

ENTRENAR DISCRIMINADOR (G congelado):

  ┌──────────┐                              ┌────────────────┐
  │ Imágenes │─────────────────────────────>│                │     queremos
  │  reales  │                              │                │──>  que diga 1
  └──────────┘                              │                │
                                            │ DISCRIMINADOR  │
  ┌──────────┐    ┌─────────────┐  detach   │      (D)       │     queremos
  │ Ruido Z  │───>│ GENERADOR G │───(✂)────>│                │──>  que diga 0
  │ ~ N(0,1) │    │ (congelado) │           │                │
  └──────────┘    └─────────────┘           └───────┬────────┘
                                                    │
                                                    v
                                  ┌──────────────────────────────┐
                                  │ Loss_D = BCE(D(real), 1)     │
                                  │        + BCE(D(fake), 0)     │
                                  │ Actualizar solo pesos de D   │
                                  └──────────────────────────────┘


ENTRENAR GENERADOR (D congelado):

  ┌──────────┐    ┌─────────────┐           ┌────────────────┐
  │ Ruido Z  │───>│             │           │ DISCRIMINADOR  │     queremos
  │ ~ N(0,1) │    │ GENERADOR G │──────────>│      (D)       │──>  que diga 1
  └──────────┘    │             │           │ (congelado)    │
                  └─────────────┘           └───────┬────────┘
                                                    │
                                                    v
                                  ┌──────────────────────────────┐
                                  │ Loss_G = BCE(D(fake), 1)     │
                                  │ (flipeo: etiqueta 1 aunque   │
                                  │  la imagen es falsa)         │
                                  │ Actualizar solo pesos de G   │
                                  └──────────────────────────────┘


GENERACIÓN:

  ┌──────────┐    ┌─────────────┐    ┌─────────────┐
  │ Ruido Z  │───>│ GENERADOR G │───>│   Imagen    │
  │ ~ N(0,1) │    │ (entrenado) │    │   nueva     │
  └──────────┘    └─────────────┘    └─────────────┘

  (El discriminador se descarta. Solo se usa el generador.)


Resumen final

Ruido Z → Generador → imagen falsa → Discriminador → "real o falsa?"
Loss D = BCE(D(real), 1) + BCE(D(fake.detach()), 0)
Loss G = BCE(D(fake), 1)  ← truco del flipeo
Se entrenan alternadamente, no juntos.
Después del entrenamiento: solo G genera, D se descarta.

Si quieres, puedo darte una versión aún más compacta para memorizar o una lista de puntos clave tipo machete para el examen.
