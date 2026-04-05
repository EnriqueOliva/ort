BATCH_SIZE = 64
IMAGE_SIZE = 32
NUM_CHANNELS = 3
LATENT_DIM = 128
GENERATOR_FEATURES = 128
NUM_EPOCHS = 150

VANILLA_LR = 0.01
VANILLA_MOMENTUM = 0.9
VANILLA_DISCRIMINATOR_FEATURES = 128

WGAN_LR = 5e-5
WGAN_CLIP = 0.01
WGAN_CRITIC_FEATURES = 128
WGAN_CRITIC_ITERATIONS = 5

WGANGP_LR = 1e-4
WGANGP_LAMBDA = 10
WGANGP_BETAS = (0.0, 0.9)
WGANGP_CRITIC_FEATURES = 128
WGANGP_CRITIC_ITERATIONS = 5

Files already downloaded and verified
Dataset: CIFAR-10
Imágenes: 50000
Batches/época: 781

Entrenando Vanilla GAN: lr=0.01, momentum=0.9, épocas=150
Época 150/150
Completado: 23.08 min

Entrenando WGAN: lr=5e-05, c=0.01, épocas=150
Época 150/150
Completado: 65.78 min

Entrenando WGAN-GP: lr=0.0001, λ=10, épocas=150
Época 150/150
Completado: 124.40 min

D(real) → 1.000, D(fake) → 0.000

W-distance final: 15.6595

Vanilla: rango [-0.573, 0.736]
WGAN: rango [-0.010, 0.009]

Varianza Vanilla: 8
Varianza WGAN: 9.84e+05

WGAN std: 0.0067
WGAN-GP std: 0.0571

Varianza WGAN: 9.84e+05
Varianza WGAN-GP: 19449
GP final: 0.0046

RESUMEN
Modelo       Tiempo     Var. Grad    Peso std  
Vanilla      23.1       8            0.0206    
WGAN         65.8       9.84e+05     0.0067    
WGAN-GP      124.4      19449        0.0571    

RESUMEN COMPARATIVO

TIEMPOS DE ENTRENAMIENTO:
  Vanilla GAN: 23.08 min
  WGAN:        65.78 min (5x critic iterations)
  WGAN-GP:     124.40 min (5x critic iterations + GP)

WASSERSTEIN DISTANCE FINAL (solo WGAN/WGAN-GP):
  WGAN:    15.6595
  WGAN-GP: 1.2201

DISTRIBUCIÓN DE PESOS:
  Vanilla GAN: rango=[-0.5731, 0.7362], std=0.0206
  WGAN:        rango=[-0.0100, 0.0089], std=0.0067
  WGAN-GP:     rango=[-0.4868, 0.6185], std=0.0571

ESTABILIDAD DE GRADIENTES (varianza):
  Vanilla GAN: 7.6776
  WGAN:        983839.6050
  WGAN-GP:     19449.1499

