### Análisis del dataset

- Se verificó que todas las imágenes fueran 800x800 como indica el obligatorio. Esto confirma uniformidad y simplifica el pipeline al no requerir manejo de casos especiales.
- Se visualizaron 6 muestras aleatorias del dataset para entender la variabilidad: diversidad de poses, fondos, iluminación, y encuadres. Esto ayudó a anticipar qué augmentations serían útiles y cuáles no.
- Se analizó la distribución de foreground/background sobre 200 máscaras aleatorias. Estadísticas obtenidas: promedio 38.4%, mediana 36.6%, mínimo 1.04%, máximo 93.71%. Este desbalance de clases justifica usar Dice Loss en lugar de solo BCE, ya que BCE penaliza cada píxel igual e incentivaría predecir todo como fondo.
- Se visualizaron los casos extremos (mínimo y máximo foreground) para entender los límites del dataset. Personas muy pequeñas en la imagen vs personas que ocupan casi toda la imagen. Esto ayudó a entender la variabilidad que el modelo debe manejar.
