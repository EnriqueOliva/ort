# VAE - Flujo Completo (Variational Autoencoder)

## Qué es

Un modelo que comprime imágenes a un espacio pequeño y luego las reconstruye. Lo especial es que ese espacio pequeño está organizado de una manera que permite generar imágenes nuevas.

---

## FLUJO DE ENTRENAMIENTO

**Entrada:** Una imagen del dataset
**Salida:** La misma imagen reconstruida

```
1. Tomar una imagen del dataset

2. Pasarla por el ENCODER (una red neuronal)
   - El encoder NO produce un punto fijo
   - Produce DOS cosas: una media (mu) y una varianza (sigma)
   - Estos definen una "zona" en el espacio latente

3. MUESTREAR un punto de esa zona
   - Generar un numero aleatorio (epsilon)
   - Calcular el punto Z usando mu, sigma y epsilon
   - Esto se llama "reparametrization trick"
   - Por que? Porque si solo muestrearas, no podrias entrenar (no hay gradientes)

4. Pasar Z por el DECODER (otra red neuronal)
   - El decoder toma el punto Z
   - Genera una imagen reconstruida

5. Comparar imagen original vs reconstruida
   - Calcular perdida de reconstruccion (que tan diferente es)

6. Calcular perdida KL
   - Mide que tan diferente es la zona (mu, sigma) de una distribucion "ideal"
   - Esto fuerza al espacio latente a estar organizado

7. Sumar ambas perdidas

8. Backpropagation y actualizar pesos
```

---

## FLUJO DE GENERACION (crear imagenes nuevas)

**Entrada:** Nada (solo ruido aleatorio)
**Salida:** Una imagen nueva que no existia

```
1. Generar un punto aleatorio Z
   - Simplemente numeros aleatorios de una distribucion normal

2. Pasar Z por el DECODER
   - El decoder ya esta entrenado
   - Convierte Z en una imagen

3. Esa imagen es la imagen nueva generada
```

---

## Diagrama

```
ENTRENAMIENTO:

Imagen --> [ENCODER] --> mu, sigma --> muestrear --> Z --> [DECODER] --> Imagen reconstruida
   |                                                                            |
   |_____________ comparar (perdida de reconstruccion) _________________________|
                                    +
                    mu, sigma --> calcular perdida KL


GENERACION:

Ruido aleatorio --> Z --> [DECODER] --> Imagen nueva
```

---

## Por que funciona

- El ENCODER aprende a comprimir la informacion importante de la imagen
- La perdida KL obliga a que el espacio latente sea "suave" y organizado
- Sin KL: el encoder podria poner cada imagen en un punto aislado (memorizacion)
- Con KL: puntos cercanos en Z generan imagenes similares
- Esto permite: interpolar entre imagenes, generar variaciones, crear imagenes nuevas

---

## Tamanio del espacio latente

- Una imagen puede tener miles de pixeles (ej: 64x64 = 4096)
- El espacio latente Z es MUCHO mas pequeno (ej: 128 o 256 numeros)
- Esto fuerza a comprimir solo la informacion esencial
