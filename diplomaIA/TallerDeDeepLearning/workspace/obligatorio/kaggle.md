Overview
Esta competencia se centra en la tarea de segmentación binaria de imágenes de personas. Los participantes deben desarrollar un modelo que sea capaz de generar una máscara de segmentación precisa que identifique el cuerpo humano en las imágenes proporcionadas.

Cada imagen es de tamaño 800x800 píxeles y la tarea consiste en predecir una máscara binaria (0 para fondo y 1 para el cuerpo de la persona) para cada imagen. El formato de la máscara debe ser comprimido utilizando Run-Length Encoding (RLE), que será el formato en el que las predicciones deberán ser subidas a Kaggle.

El objetivo final es que el modelo aprenda a distinguir claramente entre el fondo y la persona, generando una máscara precisa para cada imagen.

Start

a month ago
Close
6 days to go
Formato de Envío (Submission Format)
Para participar en la competencia, cada predicción debe subirse en un archivo CSV que contenga dos columnas: id y encoded_pixels. Este archivo representa las máscaras de segmentación predichas para cada imagen en el conjunto de prueba. La máscara predicha debe ser codificada utilizando Run-Length Encoding (RLE), que es el formato requerido para la entrega de predicciones.

Descripción de las columnas:
id: El nombre de archivo de la imagen (por ejemplo, image_001.png) que fue utilizada como entrada al modelo.
encoded_pixels: La máscara de segmentación predicha para la imagen, representada en formato Run-Length Encoding (RLE).
Run-Length Encoding (RLE)
El formato RLE es una forma de comprimir la máscara de segmentación en una cadena de texto, representando secuencias consecutivas de píxeles con valores positivos (es decir, donde la máscara tiene valor 1, que representa el cuerpo de la persona). El formato codifica las posiciones iniciales y las longitudes de cada secuencia de píxeles contiguos con valor 1.

La secuencia RLE tiene el formato siguiente:

start length start length start length ...
start: Es la posición (en el vector aplanado de la máscara) donde comienza una secuencia de 1s.
length: Es el número de píxeles consecutivos con valor 1, comenzando desde la posición start.
Las posiciones en RLE están basadas en un vector aplanado en orden Fortran (columna por columna).

Ejemplo de Envío
El archivo de envío debe estar en formato CSV con dos columnas: id y encoded_pixels. Aquí tienes un ejemplo de cómo debería verse un archivo de envío:

id,encoded_pixels
image_001.png,3 5 13 4 28 2
image_002.png,10 6 30 3 50 4
image_003.png,7 2 22 5 40 3
Explicación del ejemplo:
image_001.png: La máscara predicha para la imagen image_001.png tiene secuencias de píxeles contiguos con valor 1, comenzando en la posición 3 con una longitud de 5 píxeles, luego en la posición 13 con 4 píxeles, y así sucesivamente.

image_002.png: De manera similar, la máscara para image_002.png tiene secuencias de píxeles con valor 1 que empiezan en la posición 10 con 6 píxeles, etc.

Consideraciones Importantes:
Tamaño de las imágenes y las máscaras: Cada imagen y cada máscara deben tener un tamaño de 800x800 píxeles. Asegúrate de que todas las máscaras predichas sigan esta especificación antes de codificarlas en formato RLE.

Valores de la máscara: Las máscaras deben contener solo valores binarios, es decir, 0 para el fondo y 1 para el cuerpo de la persona.

Formato CSV: El archivo de envío debe guardarse en formato CSV, con el nombre del archivo como valor en la columna id, y la cadena RLE correspondiente a la máscara en la columna encoded_pixels.

Citation
Joaquin Vigna. [TDL] Obligatorio 2025. https://kaggle.com/competitions/tdl-obligatorio-2025, 2025. Kaggle.

Dataset Description
El dataset está diseñado para la segmentación binaria de personas en imágenes. Contiene imágenes de 800x800 píxeles y se espera que las máscaras predecidas también sigan este tamaño. A continuación, se describe la estructura del dataset:

train: Contiene dos subcarpetas:
images: Contiene las imágenes de entrenamiento.
masks: Contiene las máscaras correspondientes en el conjunto de entrenamiento.
test/images: Contiene las imágenes de prueba.
Las máscaras de entrenamiento y prueba están representadas por valores binarios (0 y 1) en lugar de los valores 0 a 255.

