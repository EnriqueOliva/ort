## Conclusiones

### Resumen

Este trabajo buscaba responder dos preguntas: ¿por qué entrenar GANs es tan difícil? y ¿cómo lo solucionaron los investigadores? Los resultados de 400 épocas de entrenamiento sobre CIFAR-10 demuestran de forma clara cada problema y su solución.


### El Problema Original: Vanilla GAN

El primer gráfico cuenta toda la historia. Apenas comienza el entrenamiento, el discriminador ya sabe perfectamente distinguir lo real de lo falso:

- D(real) → 1.000 (el discriminador está 100% seguro de que las reales son reales)
- D(fake) → 0.000 (el discriminador está 100% seguro de que las falsas son falsas)

Esto pasa en las primeras iteraciones y nunca cambia. El discriminador "ganó" el juego demasiado rápido.

¿Por qué esto es un desastre? La pérdida de Vanilla GAN usa BCE (Binary Cross-Entropy). Cuando D(fake) → 0, el gradiente desaparece. El generador recibe una señal que dice "es malo" pero no indica cuánto de malo ni cómo mejorar.

El Gráfico 7 muestra el resultado: las imágenes de Vanilla GAN son ruido puro. Patrones estáticos sin ninguna estructura.


### La Primera Solución: WGAN

Arjovsky et al. (2017) identificaron el problema: la función de pérdida está mal. Propusieron reemplazar BCE por la distancia Wasserstein.

¿Qué cambió?
1. El discriminador ahora se llama "crítico" y no tiene sigmoid al final
2. En lugar de dar probabilidades (0 a 1), da puntajes sin límites
3. La pérdida es simplemente C(real) - C(fake)

El Gráfico 2 muestra que la W-distance no colapsa a cero. Fluctúa durante todo el entrenamiento, indicando que el crítico siempre está dando información útil al generador.


### El Nuevo Problema: Weight Clipping

WGAN introdujo un problema nuevo. Para que la matemática de Wasserstein funcione, el crítico tiene que ser 1-Lipschitz. WGAN resuelve esto recortando todos los pesos al rango [-0.01, 0.01] después de cada paso.

El Gráfico 3 muestra las consecuencias:
- Vanilla GAN: campana de Gauss natural, rango [-1.02, 1.19], std=0.0212
- WGAN: todos los pesos comprimidos en ±0.01, std=0.0014

¿Por qué esto es malo? Si solo se pueden usar pesos de exactamente -0.01 o +0.01, la red pierde capacidad expresiva. Es como intentar dibujar un retrato pero solo con dos colores.


### La Consecuencia: Gradientes Explosivos

El Gráfico 4 muestra algo dramático:
- Vanilla GAN: varianza de gradientes = 92
- WGAN: varianza de gradientes = 1,127,321

Los gradientes de WGAN son 12,300 veces más inestables que los de Vanilla. Cuando se fuerzan los pesos a los extremos, la red se vuelve una función "puntiaguda" donde pequeños cambios en la entrada causan cambios enormes en la salida.

El Gráfico 7 confirma las consecuencias: las imágenes de WGAN son borrosas y apagadas. Mejor que el ruido de Vanilla, pero lejos de ser buenas.


### La Solución Final: WGAN-GP

Gulrajani et al. (2017) propusieron una idea elegante: en lugar de forzar los pesos, penalizar directamente cuando el gradiente del crítico se aleja de 1. La fórmula es GP = E[(||∇C(x̂)||₂ - 1)²].

El Gráfico 5 muestra que WGAN-GP recupera una distribución natural de pesos:
- WGAN: std=0.0014 (aplastado)
- WGAN-GP: std=0.0802 (57× más expresivo)

El Gráfico 6 muestra dos cosas:
1. Gradientes estables: la varianza baja de 1,127,321 a 12,468 (90× mejor)
2. GP converge: empieza en ~1.4 y baja a 0.02, indicando que el crítico aprendió a ser 1-Lipschitz naturalmente


### La Evidencia Final: Las Imágenes

El Gráfico 7 es el juez final. Después de 400 épocas:
- Vanilla GAN: ruido estático, patrones repetitivos sin sentido
- WGAN: formas borrosas, siluetas sin detalle, colores apagados
- WGAN-GP: imágenes reconocibles, se distinguen animales, vehículos, texturas


### El Costo: Tiempo de Entrenamiento

Cada mejora tiene un costo computacional:
- Vanilla GAN: 59.76 min (1×)
- WGAN: 165.37 min (2.8×)
- WGAN-GP: 334.07 min (5.6×)

WGAN tarda más porque entrena el crítico 5 veces por cada vez que entrena el generador. WGAN-GP tarda aún más porque además calcula el gradient penalty.

¿Vale la pena? Sí. Vanilla GAN no produce resultados utilizables sin importar cuánto tiempo se entrene.


### Resumen Cuantitativo

Saturación del discriminador:
- Vanilla GAN: D(real)=1, D(fake)=0
- WGAN: no aplica
- WGAN-GP: no aplica

W-distance final:
- WGAN: 16.12
- WGAN-GP: 0.91

Distribución de pesos (std):
- Vanilla GAN: 0.0212
- WGAN: 0.0014
- WGAN-GP: 0.0802

Varianza de gradientes:
- Vanilla GAN: 92
- WGAN: 1,127,321
- WGAN-GP: 12,468

Calidad visual:
- Vanilla GAN: ruido
- WGAN: borroso
- WGAN-GP: reconocible


### Lecciones Aprendidas

Cada paper resolvió un problema pero introdujo otro:

1. Goodfellow et al. (2014) inventó las GANs, pero la formulación con BCE sufre de saturación. El discriminador "gana" muy rápido y el generador no puede aprender.

2. Arjovsky et al. (2017) identificó que el problema era la función de pérdida y propuso Wasserstein. Pero el weight clipping limita la capacidad del crítico y causa gradientes explosivos.

3. Gulrajani et al. (2017) encontró una forma más elegante de enforcar la restricción de Lipschitz. El gradient penalty permite pesos naturales y gradientes estables.

La lección general: en deep learning, los detalles importan. Una función de pérdida mal diseñada puede hacer que un modelo brillante no funcione.


### Trabajo Futuro

Este experimento usó la implementación básica de cada modelo. Existen extensiones que podrían mejorar los resultados:

- GANs Condicionales: permiten controlar qué clase generar
- Progressive Growing: entrenar primero en resolución baja y aumentar gradualmente
- Spectral Normalization: otra forma de enforcar Lipschitz
- Métricas cuantitativas: FID e IS darían una evaluación más objetiva

Sin embargo, el objetivo de este trabajo era demostrar los problemas y sus soluciones, no optimizar la calidad de imagen. Los gráficos cuentan exactamente la historia que se buscaba contar.
