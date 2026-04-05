# Diffusion - Flujo Completo (Modelo de Difusion)

## Qué es

Un modelo que aprende a quitar ruido de imagenes. Para generar, empiezas con ruido puro y vas quitando ruido paso a paso hasta obtener una imagen limpia.

---

## FLUJO DE ENTRENAMIENTO

**Entrada:** Imagenes del dataset
**Salida:** Un modelo que sabe predecir cuanto ruido hay en una imagen

```
1. Tomar una imagen limpia del dataset

2. Elegir un numero aleatorio T (entre 1 y 1000)
   - Este numero representa "cuanto ruido agregar"
   - T bajo = poco ruido
   - T alto = mucho ruido (casi puro)

3. Generar ruido aleatorio (epsilon)
   - Solo numeros aleatorios

4. Crear la imagen ruidosa
   - Mezclar la imagen limpia con el ruido
   - Cuanto de cada uno depende de T
   - ATAJO: puedes saltar directo a cualquier T sin calcular pasos intermedios
   - (Sin este atajo, para T=500 tendrias que hacer 500 operaciones)

5. Darle al modelo la imagen ruidosa Y el numero T
   - El modelo necesita saber T para entender cuanto ruido hay
   - El modelo predice: que ruido cree que tiene la imagen

6. Comparar el ruido predicho vs el ruido real
   - Perdida = diferencia entre ambos

7. Backpropagation y actualizar pesos

8. Repetir muchas veces con diferentes imagenes y diferentes T
```

---

## FLUJO DE GENERACION (crear imagenes nuevas)

**Entrada:** Nada (solo ruido aleatorio)
**Salida:** Una imagen nueva

```
1. Generar una imagen de puro ruido
   - Esta es X_1000 (maximo ruido)

2. Para cada paso T desde 1000 hasta 1:

   a. Darle al modelo la imagen actual y el numero T

   b. El modelo predice cuanto ruido hay

   c. Restar ese ruido de la imagen
      - La imagen queda un poco mas limpia

   d. Agregar un poquito de ruido nuevo (excepto en el ultimo paso)
      - Esto agrega variabilidad

3. Al terminar todos los pasos, tienes X_0
   - Esta es la imagen generada
```

---

## Diagrama

```
ENTRENAMIENTO:

Imagen limpia + T aleatorio + ruido aleatorio
         |
         v
   mezclar (usando el atajo)
         |
         v
   Imagen ruidosa + T --> [MODELO] --> ruido predicho
                                              |
                                   comparar con ruido real
                                              |
                                         perdida


GENERACION:

Ruido puro (T=1000) --> [MODELO predice ruido] --> restar ruido --> imagen un poco mas limpia
                                                         |
                               repetir 1000 veces <------|
                                                         |
                                                         v
                                                    Imagen final
```

---

## Por que funciona

### El atajo (forma cerrada)
- Para entrenar necesitas imagenes con distintos niveles de ruido
- Sin atajo: para crear imagen con ruido nivel 500, haces 500 operaciones
- Con atajo: para crear imagen con ruido nivel 500, haces 1 operacion
- El atajo existe porque agregar ruido es una operacion simple matematicamente
- Sin este atajo el entrenamiento seria extremadamente lento

### Por que la generacion no tiene atajo
- Para quitar ruido necesitas saber que ruido hay
- El modelo solo puede predecir el ruido si ve el estado actual de la imagen
- No hay forma de saltar pasos: debes ir uno por uno
- Por eso la generacion en difusion es lenta (1000 pasos)

### Por que predecir ruido y no la imagen limpia
- El ruido siempre tiene la misma forma (distribucion normal)
- Es mas facil para el modelo predecir algo con forma conocida
- Ambos enfoques son equivalentes pero predecir ruido funciona mejor en practica

---

## Tamanio del espacio latente

- A diferencia de VAE y GAN, en difusion el latente tiene EL MISMO tamanio que la imagen
- Imagen de 64x64 = latente de 64x64
- No hay compresion en el espacio latente tradicional
- La "compresion" viene de que el modelo aprende a organizar el ruido

---

## El numero T (condicionamiento temporal)

- El modelo recibe T como entrada adicional
- Esto le dice "esta imagen tiene ruido nivel T"
- Sin T, el modelo no sabria cuanto ruido quitar
- Un mismo modelo sirve para todos los niveles de ruido
