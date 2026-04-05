# Language Models - Flujo Completo (Modelos de Lenguaje)

## Qué es

Un modelo que predice la siguiente palabra. Le das una secuencia de palabras y te dice cual palabra probablemente viene despues.

---

## FLUJO DE ENTRENAMIENTO

**Entrada:** Textos (libros, paginas web, documentos)
**Salida:** Un modelo que sabe predecir la siguiente palabra

```
1. Tomar un texto del dataset
   - Ejemplo: "El gato come pescado"

2. Tokenizar el texto
   - Convertir palabras a numeros
   - Cada palabra tiene un ID unico en el vocabulario
   - Ejemplo: [15, 234, 89, 456]

3. Crear pares de entrada-salida
   - Entrada: "El"           Salida esperada: "gato"
   - Entrada: "El gato"      Salida esperada: "come"
   - Entrada: "El gato come" Salida esperada: "pescado"

4. Para cada par:

   a. Pasar la entrada por el modelo
      - El modelo produce "logits" para cada palabra del vocabulario
      - Logits = numeros que indican que tan probable es cada palabra

   b. Convertir logits a probabilidades (softmax)
      - Los logits se transforman en numeros entre 0 y 1 que suman 1
      - Ahora tienes una probabilidad para cada palabra posible

   c. Calcular perdida (cross-entropy)
      - Mide que tan lejos esta la prediccion de la palabra correcta
      - Si el modelo dijo 90% para la palabra correcta: perdida baja
      - Si el modelo dijo 5% para la palabra correcta: perdida alta

   d. Backpropagation y actualizar pesos

5. Repetir con muchos textos
```

---

## FLUJO DE GENERACION (crear texto nuevo)

**Entrada:** Un prompt inicial (texto de inicio)
**Salida:** Texto generado

```
1. Tokenizar el prompt
   - Ejemplo: "El gato" --> [15, 234]

2. Pasar la secuencia por el modelo
   - Modelo produce probabilidades para la siguiente palabra
   - Ejemplo: {come: 0.35, duerme: 0.20, corre: 0.15, ...}

3. Elegir la siguiente palabra (MUESTREO)
   - No siempre eliges la mas probable
   - Muestrear = elegir al azar pero respetando las probabilidades
   - 35% de las veces saldra "come", 20% saldra "duerme", etc

4. Verificar si es fin de secuencia
   - Si la palabra elegida es el token de fin: terminar
   - Si no: continuar

5. Agregar la palabra elegida a la secuencia
   - Secuencia ahora es: "El gato come"

6. Repetir desde paso 2
   - Hasta llegar al maximo de palabras o al token de fin
```

---

## Diagrama

```
ENTRENAMIENTO:

"El gato come pescado" --> tokenizar --> [15, 234, 89, 456]
                                               |
                                               v
                    Para cada posicion crear par entrada/salida
                                               |
                                               v
          [15, 234] --> [MODELO] --> logits --> softmax --> probabilidades
                                                                  |
                                             comparar con palabra correcta (89)
                                                                  |
                                                              perdida


GENERACION:

Prompt: "El gato" --> tokenizar --> [15, 234]
                                        |
                                        v
                               [MODELO] --> probabilidades
                                                |
                                         muestrear --> "come" (89)
                                                |
                                                v
                            agregar a la secuencia --> [15, 234, 89]
                                                |
                            repetir <-----------|
                                                |
                                                v
                          hasta token de fin o maximo de palabras
```

---

## Puntos clave

### Logits vs Probabilidades
- Logits: salida cruda del modelo, pueden ser cualquier numero
- Probabilidades: numeros entre 0 y 1 que suman 1
- Softmax transforma logits en probabilidades

### Por que muestrear y no elegir siempre la mas probable
- Si siempre eliges la mas probable: texto repetitivo y aburrido
- Muestrear introduce variabilidad
- Puedes ajustar cuanta variabilidad quieres (temperatura)

### Temperatura
- Temperatura baja (ejemplo 0.1): casi siempre elige la mas probable, texto predecible
- Temperatura alta (ejemplo 2.0): elige mas al azar, texto creativo pero puede ser incoherente
- Temperatura 1.0: comportamiento por defecto

### Top-K y Top-P
- Top-K: solo considera las K palabras mas probables al muestrear
- Top-P: solo considera palabras hasta que sumen probabilidad P
- Ambos evitan elegir palabras muy improbables

---

## El modelo es DETERMINISTICO

- Para la misma entrada, el modelo SIEMPRE da la misma distribucion de probabilidades
- Lo que es aleatorio es el MUESTREO
- Por eso: misma entrada puede dar diferentes salidas
- La aleatoriedad viene del paso de muestrear, no del modelo

---

## Tokenizacion

- El modelo no trabaja con letras ni con palabras completas
- Trabaja con "tokens" que pueden ser partes de palabras
- Ejemplo: "inteligencia" puede ser ["intel", "igencia"]
- El tokenizer define como se divide el texto
- Siempre usar el mismo tokenizer para entrenar y generar
