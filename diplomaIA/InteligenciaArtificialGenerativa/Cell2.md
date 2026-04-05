### El Problema Original: Vanilla GAN

En la figura 1, apenas empieza el entrenamiento, el discriminador ya sabe perfectamente distinguir lo real de lo falso:

- D(real) → 1.000 (el discriminador está 100% seguro de que las reales son reales)
- D(fake) → 0.000 (el discriminador está 100% seguro de que las falsas son falsas)

Esto pasa en las primeras iteraciones y nunca cambia. El discriminador "ganó" el juego demasiado rápido.

La pérdida de Vanilla GAN usa BCE (Binary Cross-Entropy). Cuando D(fake) → 0, el gradiente desaparece. El generador recibe una señal que dice "es malo" pero no indica cuánto de malo ni cómo mejorar.

### Solución de WGAN

Arjovsky et al. (2017) propusieron reemplazar BCE por la distancia Wasserstein.

1. El discriminador ahora se llama "crítico" y no tiene sigmoid al final
2. En lugar de dar probabilidades (0 a 1), da puntajes sin límites
3. La pérdida es simplemente C(real) - C(fake)

La figura 2 muestra que la W-distance no colapsa a cero. Fluctúa durante todo el entrenamiento, indicando que el crítico siempre está dando información útil al generador.


### Nuevo Problema: Weight Clipping

WGAN introdujo un problema nuevo. Para que la matemática de Wasserstein funcione, el crítico tiene que ser 1-Lipschitz. WGAN resuelve esto recortando todos los pesos al rango [-0.01, 0.01] después de cada paso.

La figura 3 muestra las consecuencias:
- Vanilla GAN: campana de Gauss natural, rango [-0.57, 0.74], std=0.0206
- WGAN: todos los pesos comprimidos en ±0.01, std=0.0067

Si solo se pueden usar pesos de exactamente -0.01 o +0.01, la red pierde capacidad expresiva.

### Consecuencia: Gradientes Explosivos

La figura 4 muestra:
- Vanilla GAN: varianza de gradientes = 8
- WGAN: varianza de gradientes = 983,840

Los gradientes de WGAN son mucho más inestables que los de Vanilla. Cuando se fuerzan los pesos a los extremos, la red se vuelve una función "puntiaguda" donde pequeños cambios en la entrada causan cambios enormes en la salida.

La figura 7 confirma las consecuencias: las imágenes de WGAN son borrosas y apagadas. Mejor que el ruido de Vanilla, pero lejos de ser buenas.


### La Solución de WGAN-GP

Gulrajani et al. (2017) propusieron, en lugar de forzar los pesos, penalizar directamente cuando el gradiente del crítico se aleja de 1.

La figura 5 muestra que WGAN-GP recupera una distribución natural de pesos:
- WGAN: std=0.0067
- WGAN-GP: std=0.0571

La figura 6 muestra dos cosas:
1. Gradientes estables: la varianza baja de 983,840 a 19,449
2. GP converge: empieza en ~1.5 y baja a 0.005, indicando que el crítico aprendió a ser 1-Lipschitz naturalmente


### Las Imágenes

En la figura 7 se ve:
- Vanilla GAN: ruido estático, patrones repetitivos sin sentido
- WGAN: formas borrosas, siluetas sin detalle, colores apagados
- WGAN-GP: imágenes apenas reconocibles


### El Costo: Tiempo de Entrenamiento

Cada mejora tiene un costo computacional:
- Vanilla GAN: 23.08 min (1×)
- WGAN: 65.78 min (2.8×)
- WGAN-GP: 124.40 min (5.4×)

WGAN tarda más porque entrena el crítico 5 veces por cada vez que entrena el generador. WGAN-GP tarda todavía más porque además calcula el gradient penalty.

### Resumen Cuantitativo

Saturación del discriminador:
- Vanilla GAN: D(real)=1, D(fake)=0
- WGAN: no aplica
- WGAN-GP: no aplica

W-distance final:
- WGAN: 15.66
- WGAN-GP: 1.22

Distribución de pesos (std):
- Vanilla GAN: 0.0206
- WGAN: 0.0067
- WGAN-GP: 0.0571

Varianza de gradientes:
- Vanilla GAN: 8
- WGAN: 983,840
- WGAN-GP: 19,449

Calidad visual:
- Vanilla GAN: ruido
- WGAN: borroso
- WGAN-GP: reconocible