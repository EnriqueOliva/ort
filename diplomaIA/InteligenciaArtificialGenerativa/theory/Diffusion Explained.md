Aquí está la explicación de modelos de Difusión con la misma estructura que las de VAE y GAN:

---

1. Idea central

No hay generador vs discriminador (como GAN), ni encoder-decoder (como VAE). En su lugar, hay un solo modelo que aprende a quitar ruido de imágenes.

La analogía: imaginá que tirás una gota de tinta en un vaso de agua. Con el tiempo, la tinta se va difuminando hasta que el agua queda uniformemente gris (ruido). Si pudieras rebobinar ese proceso, partirías de agua gris uniforme y llegarías a la gota de tinta original. Eso es exactamente lo que hace el modelo: aprende a "rebobinar" el ruido.

2. Dos procesos

Forward (agregar ruido): se toma una imagen limpia y se le agrega ruido gaussiano poco a poco, en muchos pasos (típicamente 1000), hasta que se convierte en pura estática. Este proceso no se entrena, es pura matemática.

Reverse (quitar ruido): el modelo aprende a hacer lo contrario: dado una imagen ruidosa, predecir cuánto ruido tiene para poder quitárselo. Este sí se entrena.

3. Entrada del modelo

El modelo recibe dos cosas:
- Una imagen ruidosa (con algún nivel de ruido)
- El número de paso t (un número entre 1 y 1000 que le dice "cuánto ruido hay aproximadamente")

Sin t, el modelo no sabría cuánto ruido quitar. Un mismo modelo sirve para todos los niveles de ruido, condicionado por t.

4. Salida del modelo

El modelo predice el ruido que hay en la imagen. No predice la imagen limpia directamente, sino cuánto ruido se le agregó.
Ambas opciones son matemáticamente equivalentes, pero predecir el ruido funciona mejor en la práctica porque el ruido siempre tiene la misma forma (distribución Gaussiana), lo que hace más estable el entrenamiento.

5. Diferencia clave con VAE y GAN

A diferencia de VAE y GAN, en difusión el espacio latente tiene el MISMO tamaño que la imagen. Si la imagen es 64×64, el ruido es 64×64. No hay compresión. La "compresión" viene de que el modelo aprende a organizar el ruido.

6. El atajo (forma cerrada)

Para entrenar, necesitás imágenes con distintos niveles de ruido. Sin el atajo, para crear una imagen con ruido de nivel 500 habría que hacer 500 operaciones de agregar ruido una por una. Pero existe una fórmula que permite saltar directamente a cualquier nivel:

imagen_ruidosa_t = (algo de la imagen original) + (algo de ruido puro)

Los "algos" son coeficientes que dependen de t. Este atajo existe porque agregar ruido gaussiano es una operación simple matemáticamente. Sin este atajo, el entrenamiento sería imposiblemente lento.

La generación NO tiene atajo: para quitar ruido hay que ir paso por paso porque el modelo necesita ver el estado actual de la imagen para predecir el ruido. Por eso la generación en difusión es lenta (1000 pasos).

7. Arquitectura: U-Net

El modelo que predice el ruido es una U-Net: una red con forma de U que primero achica la imagen (encoder), después la agranda (decoder), y tiene "puentes" (skip connections) que pasan información directamente de un lado al otro. Además, recibe el paso t codificado con funciones sinusoidales (similar al positional encoding del Transformer).

📌 Entrenamiento (qué optimiza el modelo de difusión)

El entrenamiento usa una función de pérdida increíblemente simple comparada con VAE (dos términos) y GAN (dos redes):

a) La pérdida

Loss = (ruido real - ruido predicho) al cuadrado

Es un MSE (Mean Squared Error): la diferencia al cuadrado entre el ruido que nosotros le pusimos a la imagen y el ruido que el modelo predice. Si el modelo predice bien el ruido, la pérdida es baja.

No hay dos términos que balancear (como en VAE), ni dos redes que equilibrar (como en GAN). Es un solo número.

b) El algoritmo de entrenamiento

Para cada imagen limpia del dataset:
1. Elegir un paso t aleatorio entre 1 y 1000
2. Generar ruido aleatorio
3. Usar el atajo para crear la imagen ruidosa en el paso t (mezcla de imagen + ruido)
4. Darle al modelo la imagen ruidosa y t
5. El modelo predice el ruido
6. Calcular el error entre el ruido real y el predicho
7. Backpropagation y actualizar pesos

No hay que recorrer los 1000 pasos en orden. Se elige un t al azar y listo. Esto hace el entrenamiento muy eficiente.

c) El schedule de betas

Los betas definen cuánto ruido se agrega en cada paso. El paper DDPM usa T=1000 pasos, con un schedule lineal que va de beta_1=0.0001 a beta_T=0.02 (empieza con muy poquito ruido y va creciendo). Estos valores son hiperparámetros empíricos, no se entrenan.

📌 Por qué difusión es más estable que GAN

a) Un solo término: no hay que balancear componentes como en VAE (reconstrucción vs KL) ni equilibrar dos redes como en GAN (G vs D).

b) Objetivo claro: predecir ruido gaussiano, que siempre tiene la misma distribución conocida N(0,1).

c) Sin adversarios: no hay "juego" que pueda desbalancearse, ni mode collapse, ni vanishing gradients por un discriminador demasiado bueno.

d) Entrenamiento estable: la loss baja consistentemente a lo largo del entrenamiento, a diferencia de GAN donde las losses oscilan.

📌 Problema conocido

Generación lenta: mientras VAE genera en 1 paso y GAN genera en 1 paso, difusión necesita 1000 pasos secuenciales. Cada paso requiere una pasada completa por la U-Net. Es el precio que se paga por la estabilidad y calidad.

📌 Latent Diffusion (Stable Diffusion)

Para solucionar la lentitud, Latent Diffusion combina difusión con VAE:
1. Se comprime la imagen con el encoder de un VAE (512×512 → 64×64)
2. Se hace toda la difusión en ese espacio comprimido (mucho más rápido)
3. Al final se descomprime con el decoder del VAE

Es literalmente VAE + Difusión trabajando juntos. Además, para generar a partir de texto, se usa CLIP (un modelo que traduce texto a números) y un parámetro de guidance que controla cuánto pesa el texto.

📌 Uso después del entrenamiento

1. Generación
   Ruido puro aleatorio → aplicar el modelo 1000 veces quitando ruido → imagen limpia.
   Solo se usa el modelo de denoising. No hay discriminador ni encoder que descartar.

2. No hay reconstrucción directa
   A diferencia del VAE, no hay un encoder que comprima una imagen existente (en difusión básica). Pero se puede agregar ruido a una imagen real y luego denoising para modificarla.

Diagrama

FORWARD (agregar ruido — no se entrena, es pura matemática):

  ┌─────────┐   ┌─────────┐   ┌─────────┐           ┌─────────┐   ┌─────────┐
  │ Imagen  │   │         │   │         │           │         │   │  Pura   │
  │ limpia  │──>│  x₁     │──>│  x₂     │──> ... ──>│  x₉₉₉  │──>│estática │
  │  (x₀)   │   │         │   │         │           │         │   │(x₁₀₀₀) │
  └─────────┘   └─────────┘   └─────────┘           └─────────┘   └─────────┘
                  +ruido        +ruido                 +ruido        +ruido
                            1000 pasos de ruido gaussiano


ENTRENAMIENTO (un solo paso aleatorio, con atajo):

  ┌─────────┐       ┌──────────────────────┐
  │ Imagen  │──────>│                      │
  │ limpia  │       │  ATAJO: mezclar      │      ┌──────────────┐    ┌─────────┐
  │  (x₀)   │       │  directo a paso t    │─────>│              │    │  ruido  │
  └─────────┘       │                      │      │ MODELO       │───>│predicho │
                    └──────────────────────┘      │ (U-Net)      │    │  (ε̂)    │
  ┌─────────┐              │                      │              │    └────┬────┘
  │ t alea- │──────────────┘                      │  recibe xₜ  │         │
  │  torio  │              │                      │  y t         │         │
  └─────────┘              │                      └──────────────┘         │
                           │                                               │
  ┌─────────┐              │                      ┌────────────────────────┘
  │  ruido  │──────────────┘                      │
  │  real   │                                     v
  │  (ε)    │────────────────────────>  ┌──────────────────────┐
  └─────────┘                           │ Loss = (ε - ε̂)²     │
                                        │ (MSE entre ruido     │
                                        │  real y predicho)    │
                                        └──────────────────────┘


GENERACIÓN (quitar ruido — 1000 pasos secuenciales):

  ┌─────────┐   ┌────────┐   ┌─────────┐   ┌────────┐           ┌─────────┐
  │  Pura   │   │ MODELO │   │ un poco │   │ MODELO │           │ Imagen  │
  │estática │──>│ (U-Net)│──>│  menos  │──>│ (U-Net)│──> ... ──>│ limpia  │
  │(x₁₀₀₀) │   │ t=1000 │   │ ruidosa │   │ t=999  │           │  (x₀)   │
  └─────────┘   └────────┘   └─────────┘   └────────┘           └─────────┘
                 predice ε     quita un      predice ε
                               poquito       1000 pasos (lento)


LATENT DIFFUSION (Stable Diffusion):

  ┌──────────┐   ┌─────────────┐   ┌──────────┐   ┌───────────┐   ┌─────────────┐   ┌──────────┐
  │  Imagen  │   │     VAE     │   │  Latente │   │           │   │     VAE     │   │  Imagen  │
  │  grande  │──>│   Encoder   │──>│  64×64   │──>│ DIFUSIÓN  │──>│   Decoder   │──>│  grande  │
  │ 512×512  │   │ (comprime)  │   │          │   │ (en chico)│   │(descomprime)│   │ 512×512  │
  └──────────┘   └─────────────┘   └──────────┘   └───────────┘   └─────────────┘   └──────────┘
                         (comprime)                  (en espacio chico)            (descomprime)


Resumen final

Forward: Imagen limpia → (+ruido poco a poco, 1000 pasos) → Pura estática
Reverse: Pura estática → (modelo predice y quita ruido, 1000 pasos) → Imagen limpia
Loss = (ruido real - ruido predicho) al cuadrado. El loss más simple del curso.
Entrenamiento: elegir t al azar, crear imagen ruidosa con atajo, predecir ruido, MSE.
Generación: arrancar de ruido puro, ir quitando de a poco, 1000 pasos.
Latent Diffusion: comprimir con VAE, difundir en espacio chico, descomprimir.

Si quieres, puedo darte una versión aún más compacta para memorizar o una lista de puntos clave tipo machete para el examen.
