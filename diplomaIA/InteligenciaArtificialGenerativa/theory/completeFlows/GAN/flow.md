# GAN - Flujo Completo (Generative Adversarial Network)

## Qué es

Dos redes neuronales que compiten entre si:
- GENERADOR (G): crea imagenes falsas
- DISCRIMINADOR (D): detecta si una imagen es real o falsa

El generador mejora porque quiere engañar al discriminador.
El discriminador mejora porque quiere no ser engañado.

---

## FLUJO DE ENTRENAMIENTO

**Entrada:** Imagenes reales del dataset
**Salida:** Un generador que crea imagenes falsas convincentes

El entrenamiento es ALTERNADO (primero uno, despues el otro):

### PASO A: Entrenar el Discriminador

```
1. Tomar un batch de imagenes REALES del dataset

2. Pasarlas por el discriminador
   - D produce un numero entre 0 y 1
   - 1 significa "creo que es real"
   - 0 significa "creo que es falsa"

3. Calcular perdida para reales
   - Queremos que D diga 1 para imagenes reales
   - Perdida = que tan lejos esta D de decir 1

4. Generar imagenes FALSAS
   - Crear ruido aleatorio Z
   - Pasar Z por el Generador
   - Sale una imagen falsa

5. Pasar las imagenes falsas por el discriminador
   - IMPORTANTE: desconectar el generador (detach)
   - Esto evita que los gradientes lleguen a G

6. Calcular perdida para falsas
   - Queremos que D diga 0 para imagenes falsas
   - Perdida = que tan lejos esta D de decir 0

7. Sumar ambas perdidas

8. Actualizar SOLO los pesos de D
```

### PASO B: Entrenar el Generador

```
1. Generar ruido aleatorio Z

2. Pasar Z por el Generador
   - Sale una imagen falsa

3. Pasar la imagen falsa por el Discriminador
   - D dice que tan real cree que es

4. Calcular perdida del Generador
   - TRUCO DEL FLIPEO: aunque la imagen ES falsa, usamos etiqueta 1 (real)
   - Perdida = que tan lejos esta D de decir 1 para nuestra imagen falsa
   - Esto empuja a G a crear imagenes que D crea que son reales

5. Actualizar SOLO los pesos de G
```

### Repetir pasos A y B muchas veces

---

## FLUJO DE GENERACION (crear imagenes nuevas)

**Entrada:** Nada (solo ruido aleatorio)
**Salida:** Una imagen nueva

```
1. Generar ruido aleatorio Z

2. Pasar Z por el Generador entrenado

3. La salida es la imagen generada
```

---

## Diagrama

```
ENTRENAMIENTO DEL DISCRIMINADOR:

Imagenes reales --> [D] --> prediccion (queremos 1)
Ruido --> [G] --> imagen falsa --> [D] --> prediccion (queremos 0)
                      |
                   detach (cortar gradientes)


ENTRENAMIENTO DEL GENERADOR:

Ruido --> [G] --> imagen falsa --> [D] --> prediccion
                                              |
                                   queremos que D diga 1
                                   (truco del flipeo)


GENERACION:

Ruido --> [G entrenado] --> Imagen nueva
```

---

## Puntos clave

### Por que el detach?
- Cuando entrenas D, no quieres que G cambie
- Si no usas detach, los gradientes llegarian a G
- G se ajustaria para ayudar a D (lo opuesto a lo que quieres)

### Por que el truco del flipeo?
- Si usaras etiqueta 0 para entrenar G, G aprenderia a hacer imagenes que D rechaza
- Usando etiqueta 1, G aprende a hacer imagenes que D acepta
- Es contraintuitivo pero funciona

### Balance entre G y D
- Si D es muy bueno muy rapido: G no aprende (gradientes muy pequenos)
- Si G es muy bueno muy rapido: D no aprende
- Solucion: usar learning rate mas bajo para D que para G

---

## Tamanio del espacio latente

- El ruido Z es un vector (ej: 100 numeros)
- Mucho mas pequeno que la imagen de salida
- El generador "expande" ese ruido en una imagen completa
