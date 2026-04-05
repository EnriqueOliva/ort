# Preguntas preparación parcial - CON RESPUESTAS

## Propiedades de los tensores

- Dado el tensor `x = torch.tensor([[1, 2], [3, 4]])`, ¿cuál es su `dtype`, `device`, `ndim` y `shape`?

**Respuesta para el parcial:** `dtype=torch.int64`, `device=cpu`, `ndim=2`, `shape=torch.Size([2, 2])`.

**Explicación:** El tensor tiene enteros por defecto (int64), está en CPU (por defecto), tiene 2 dimensiones (es una matriz 2x2), y su forma es [2, 2] (2 filas, 2 columnas).

---

- Explica la utilidad de la propiedad `device` en PyTorch. Proporciona un ejemplo para mover un tensor a la GPU.

**Respuesta para el parcial:** `device` indica dónde está almacenado el tensor (CPU o GPU). Para moverlo a GPU: `x = x.to('cuda')` o `x = x.cuda()`.

**Explicación:** Los tensores deben estar en el mismo dispositivo para operar juntos. La GPU acelera cálculos ~15x, pero hay que mover los datos explícitamente.

---

- Crea un tensor unidimensional con 5 elementos y muestra cómo consultar su número de dimensiones y su forma.

**Respuesta para el parcial:** `x = torch.tensor([1, 2, 3, 4, 5])`, luego `x.ndim` → 1, y `x.shape` → `torch.Size([5])`.

**Explicación:** `ndim` cuenta cuántos ejes/dimensiones tiene (1 = vector). `shape` da el tamaño en cada dimensión (5 elementos).

---

## Concepto de Broadcasting

- Explica el concepto de broadcasting en PyTorch. ¿Por qué es útil?

**Respuesta para el parcial:** Broadcasting permite operar tensores de distintas formas expandiendo automáticamente las dimensiones compatibles. Es útil porque evita crear copias innecesarias y hace el código más simple.

**Explicación:** Sin broadcasting, para sumar un escalar a una matriz habría que expandir el escalar manualmente. PyTorch lo hace automáticamente si las dimensiones son compatibles (iguales o una es 1).

---

- Dado `x = torch.tensor([[1, 2], [3, 4]])` y `y = torch.tensor([10, 20])`, ¿qué sucederá al realizar `z = x + y`? Especifica la forma y los valores de `z`.

**Respuesta para el parcial:** `z` tendrá forma `(2, 2)` con valores `[[11, 22], [13, 24]]`. El vector `y` se "expande" a cada fila.

**Explicación:** `y` de forma `(2,)` se trata como `(1, 2)` y se replica para cada fila de `x`. Así `[10, 20]` se suma a `[1, 2]` y a `[3, 4]`.

---

- ¿Es posible sumar un tensor con forma `(4, 3)` y otro con forma `(3,)`? ¿Por qué?

**Respuesta para el parcial:** Sí, es posible. El tensor `(3,)` se expande a `(1, 3)` y luego se replica 4 veces para formar `(4, 3)`, coincidiendo con el primero.

**Explicación:** Broadcasting compara dimensiones de derecha a izquierda. Ambos tienen 3 en la última dimensión. El tensor pequeño se replica en la dimensión faltante.

---

## Slicing en tensores

- Dado el tensor `x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`, escribe el código para seleccionar la columna segunda columna.

**Respuesta para el parcial:** `x[:, 1]` → `tensor([2, 5, 8])`.

**Explicación:** `:` significa "todas las filas", `1` es el índice de la segunda columna (índices empiezan en 0). Resultado: todos los elementos de la columna 1.

---

- Extrae las dos primeras filas y las dos primeras columnas del tensor `x` con forma `(3, 3)`.

**Respuesta para el parcial:** `x[:2, :2]` → `tensor([[1, 2], [4, 5]])`.

**Explicación:** `:2` significa "desde el inicio hasta el índice 2 (sin incluir)". Se aplica a filas y columnas.

---

- Usa slicing para seleccionar los elementos de las posiciones impares en un tensor unidimensional.

**Respuesta para el parcial:** `x[1::2]` selecciona elementos en índices 1, 3, 5, ... (posiciones impares).

**Explicación:** La sintaxis es `[inicio:fin:paso]`. `1::2` significa: empezar en índice 1, ir hasta el final, de 2 en 2.

---

## Diferencias entre cat y stack

- ¿Cuál es la principal diferencia entre `torch.cat` y `torch.stack`? Proporciona un ejemplo.

**Respuesta para el parcial:** `cat` concatena en una dimensión existente (no crea nuevas dimensiones). `stack` crea una nueva dimensión y apila los tensores en ella.

**Explicación:** Si tienes dos tensores de forma `(3,)`: `cat` → `(6,)` (los une). `stack` → `(2, 3)` (los apila creando nueva dimensión).

---

- Dado `x = torch.tensor([1, 2])` y `y = torch.tensor([3, 4])`, escribe el código para concatenarlos a lo largo de una nueva dimensión.

**Respuesta para el parcial:** `torch.stack([x, y], dim=0)` → resultado con forma `(2, 2)`.

**Explicación:** `stack` crea una nueva dimensión. Resultado: `tensor([[1, 2], [3, 4]])`.

---

- ¿Qué hará `torch.stack([x, y], dim=0)` si `x` e `y` tienen forma `(2,)`? Proporciona el resultado.

**Respuesta para el parcial:** Crea un tensor de forma `(2, 2)`: `tensor([[1, 2], [3, 4]])`. Se inserta nueva dimensión en posición 0.

**Explicación:** `dim=0` significa que la nueva dimensión se crea al inicio. Los dos tensores se convierten en filas de una matriz.

---

## Funciones squeeze, unsqueeze, reshape

- Dado un tensor con forma `(1, 3, 1)`, ¿cómo eliminarías todas las dimensiones de tamaño 1?

**Respuesta para el parcial:** `x.squeeze()` → resultado con forma `(3,)`.

**Explicación:** `squeeze()` sin argumentos elimina TODAS las dimensiones de tamaño 1. Con argumento (`squeeze(0)`) elimina solo esa dimensión específica si es 1.

---

- ¿Qué hace `torch.unsqueeze(x, dim=0)`? Explica y proporciona un ejemplo.

**Respuesta para el parcial:** Añade una nueva dimensión de tamaño 1 en la posición indicada. Si `x` tiene forma `(3,)`, después de `unsqueeze(x, 0)` tiene forma `(1, 3)`.

**Explicación:** Es lo opuesto a squeeze. Útil para añadir dimensión de batch o preparar tensores para operaciones que requieren cierta forma.

---

- ¿Cómo reestructurarías un tensor de forma `(2, 3)` a `(6,)` usando `reshape`?

**Respuesta para el parcial:** `x.reshape(6)` o `x.reshape(-1)`. El `-1` calcula automáticamente el tamaño.

**Explicación:** `reshape` cambia la forma manteniendo los mismos elementos en el mismo orden (row-major). El total de elementos debe coincidir: 2×3 = 6.

---

## Uso de GPU

- Explica cómo verificar si una GPU está disponible en PyTorch.

**Respuesta para el parcial:** `torch.cuda.is_available()` retorna `True` si hay GPU disponible, `False` si no.

**Explicación:** Esto detecta si CUDA está instalado y hay una GPU NVIDIA compatible. Útil para hacer código portable entre máquinas con/sin GPU.

---

- Escribe el código para mover un tensor `x` a la GPU y luego devolverlo a la CPU.

**Respuesta para el parcial:** A GPU: `x = x.to('cuda')` o `x = x.cuda()`. A CPU: `x = x.to('cpu')` o `x = x.cpu()`.

**Explicación:** `.to(device)` es más flexible (acepta strings o torch.device). `.cuda()` y `.cpu()` son atajos específicos.

---

- ¿Qué sucede si intentas operar entre un tensor en GPU y otro en CPU? Proporciona una solución al problema.

**Respuesta para el parcial:** Da error `RuntimeError`. Solución: mover ambos tensores al mismo dispositivo antes de operar: `y = y.to(x.device)`.

**Explicación:** PyTorch no puede mezclar dispositivos en operaciones. Hay que asegurar que todos los tensores involucrados estén en el mismo device.

---

---

## Datasets y DataLoaders

- ¿Qué funciones debemos implementar cuando creamos un `DataSet` personalizado? Para que sirven?

**Respuesta para el parcial:** `__init__` (inicializa datos), `__len__` (retorna cantidad de muestras), `__getitem__` (retorna una muestra dado un índice).

**Explicación:** Estas 3 funciones permiten que PyTorch sepa cuántos datos hay y cómo acceder a cada uno individualmente, habilitando batching y shuffling.

---

- Explica cómo usar el parámetro `batch_size` en un `DataLoader` y qué impacto tiene en el entrenamiento. Muestre alguna situación que convenga subirlo/bajarlo.

**Respuesta para el parcial:** `batch_size` define cuántas muestras se procesan juntas. Mayor batch = más estable pero más memoria. Menor batch = más ruido pero menos memoria. Subir: GPU con mucha RAM. Bajar: poca memoria o querer más regularización.

**Explicación:** Batch grande: gradientes más estables, entrenamiento más rápido por época. Batch pequeño: más ruido (puede actuar como regularización), necesario si hay poca memoria.

---

- ¿Qué hace el parámetro `shuffle` en un `DataLoader` y cuándo es útil activarlo?

**Respuesta para el parcial:** `shuffle=True` mezcla aleatoriamente los datos en cada época. Se activa en entrenamiento para evitar que el modelo aprenda el orden de los datos.

**Explicación:** Sin shuffle, el modelo podría memorizar patrones del orden. En validación/test se usa `shuffle=False` para reproducibilidad.

---

- Dado el siguiente código:

```python
dataloader = DataLoader(dataset, batch_size=4, num_workers=2)
```

¿Qué significa `num_workers` y cómo afecta el rendimiento del entrenamiento?

**Respuesta para el parcial:** `num_workers` indica cuántos subprocesos paralelos cargan datos. Más workers = carga de datos más rápida, GPU menos ociosa esperando datos.

**Explicación:** Con `num_workers=0` el proceso principal carga datos (más lento). Con >0, procesos en background pre-cargan batches mientras la GPU entrena.

---

## Train & Eval

- ¿Cuál es la diferencia entre `model.train()` y `model.eval()` en PyTorch?

**Respuesta para el parcial:** `model.train()` activa capas como Dropout y BatchNorm en modo entrenamiento. `model.eval()` las pone en modo inferencia (Dropout desactivado, BatchNorm usa estadísticas globales).

**Explicación:** Algunas capas se comportan diferente en entrenamiento vs inferencia. El modo determina ese comportamiento.

---

- ¿Qué sucede con las capas de dropout cuando llamas a `model.eval()`?

**Respuesta para el parcial:** Se desactivan completamente: no "apagan" ninguna neurona, todas las conexiones se usan.

**Explicación:** Dropout solo tiene sentido en entrenamiento (regularización). En evaluación queremos usar toda la capacidad del modelo.

---

- Dado el siguiente código:

```python
model.eval()
with torch.no_grad():
        output = model(x)
```

¿Por qué se utiliza `torch.no_grad()` en este caso?

**Respuesta para el parcial:** `torch.no_grad()` desactiva el cálculo de gradientes, ahorrando memoria y acelerando la inferencia. No necesitamos gradientes si no vamos a hacer backpropagation.

**Explicación:** El grafo computacional consume memoria. En evaluación solo queremos el resultado, no entrenar, así que desactivamos los gradientes.

---

- ¿Qué problemas podrían surgir si olvidas cambiar a `model.eval()` durante la evaluación?

**Respuesta para el parcial:** Dropout seguirá apagando neuronas aleatoriamente y BatchNorm usará estadísticas del batch actual, dando resultados inconsistentes/incorrectos.

**Explicación:** Las métricas de evaluación serían inestables y no reflejarían el verdadero rendimiento del modelo.

---

## Pérdidas (train loss, val loss)

- ¿Qué representa la `train loss` y la `val loss` en un modelo de machine learning?

**Respuesta para el parcial:** `train loss` mide el error en datos de entrenamiento (los que el modelo "ve"). `val loss` mide el error en datos de validación (datos nuevos no vistos durante el entrenamiento).

**Explicación:** train_loss muestra qué tan bien memoriza, val_loss muestra qué tan bien generaliza a datos nuevos.

---

- Si la `train loss` disminuye pero la `val loss` aumenta, ¿qué problema podría estar ocurriendo? Cómo se puede detener este fenómeno?

**Respuesta para el parcial:** Overfitting (sobreajuste): el modelo memoriza los datos de entrenamiento pero no generaliza. Soluciones: early stopping, regularización (Dropout, L2), data augmentation, o reducir complejidad del modelo.

**Explicación:** Cuando train_loss baja y val_loss sube, el modelo aprende ruido específico del training set en vez de patrones generales.

---

## Bucles de entrenamiento y evaluación

- Dado el siguiente bucle:

```python
for epoch in range(epochs):
        model.train()
        for batch in train_loader:
                ...
        model.eval()
        with torch.no_grad():
                for batch in val_loader:
                        ...
```

Explica brevemente qué hace cada linea del código.

**Respuesta para el parcial:**
- `for epoch in range(epochs)`: itera sobre las épocas de entrenamiento
- `model.train()`: activa modo entrenamiento (Dropout ON, BatchNorm en modo training)
- `for batch in train_loader`: itera sobre batches de datos de entrenamiento
- `model.eval()`: activa modo evaluación (Dropout OFF)
- `with torch.no_grad()`: desactiva gradientes para ahorrar memoria
- `for batch in val_loader`: itera sobre batches de validación para medir rendimiento

**Explicación:** Este es el patrón estándar: entrenar con todos los batches, luego evaluar sin gradientes para medir progreso real.

---

## Weights & Biases (WandB)

- ¿Qué hace Weights & Biases y por qué es útil en el entrenamiento de modelos?

**Respuesta para el parcial:** WandB es una plataforma para tracking de experimentos: registra métricas, hiperparámetros, y visualiza el progreso del entrenamiento. Útil para comparar experimentos y reproducibilidad.

**Explicación:** Sin tracking es difícil recordar qué configuración dio mejores resultados. WandB guarda todo automáticamente en la nube.

---

- Explique la diferencia entre un `sweep` y un `run`.

**Respuesta para el parcial:** Un `run` es una ejecución individual del entrenamiento con hiperparámetros fijos. Un `sweep` es una búsqueda automática de hiperparámetros que ejecuta múltiples runs con diferentes configuraciones.

**Explicación:** Sweep automatiza la búsqueda de la mejor combinación de hiperparámetros (learning rate, batch size, etc.) probando muchas configuraciones.

---

---

## Capa `nn.Linear`

- Explica qué hace la capa `nn.Linear` y cómo transforma una entrada en una salida.

**Respuesta para el parcial:** `nn.Linear(in_features, out_features)` aplica una transformación lineal: `output = input @ W^T + b`. Multiplica la entrada por una matriz de pesos y suma un bias.

**Explicación:** Es la capa básica de redes neuronales. Cada neurona de salida es una combinación lineal de todas las entradas.

---

- Dado el siguiente código:

```python
layer = nn.Linear(4, 2)
x = torch.randn(3, 4)
output = layer(x)
```

¿Cuál será la forma de `output` y qué representa cada dimensión?

**Respuesta para el parcial:** `output` tiene forma `(3, 2)`. 3 es el batch_size (número de muestras), 2 es out_features (dimensión de salida por muestra).

**Explicación:** Cada fila de entrada (4 valores) se transforma en 2 valores. Las 3 muestras se procesan en paralelo.

---

- ¿Qué impacto tiene el uso de `bias=True` al definir una capa `nn.Linear`?

**Respuesta para el parcial:** Con `bias=True` (default) se añade un término constante a cada neurona: `y = Wx + b`. Sin bias, la salida siempre pasa por el origen cuando la entrada es cero.

**Explicación:** El bias permite desplazar la función de activación, dando más flexibilidad al modelo. Casi siempre se usa.

---

## Capa `nn.Dropout`

- ¿Cuál es el propósito de la capa `nn.Dropout` y cómo afecta el entrenamiento de un modelo?

**Respuesta para el parcial:** Dropout es una técnica de regularización que "apaga" neuronas aleatoriamente (las pone a 0) durante el entrenamiento con probabilidad `p`. Previene overfitting al forzar redundancia.

**Explicación:** Si algunas neuronas se apagan al azar, el modelo no puede depender demasiado de ninguna neurona específica, mejorando generalización.

---

- Dado el siguiente código:

```python
dropout = nn.Dropout(p=0.5)
x = torch.tensor([1.0, 2.0, 3.0])
output = dropout(x)
```

Explica qué valores podría tomar `output`.

**Respuesta para el parcial:** Cada elemento tiene 50% probabilidad de ser 0. Los que no se apagan se escalan por `1/(1-p) = 2`. Posibles outputs: `[0, 4, 6]`, `[2, 0, 0]`, `[2, 4, 6]`, etc.

**Explicación:** El escalado (`/1-p`) compensa los valores apagados para que la suma esperada sea igual que sin dropout. Esto evita ajustar en inferencia.

---

## Capa `nn.Embedding`

- ¿Qué representa la capa `nn.Embedding` y para qué tipo de datos es útil?

**Respuesta para el parcial:** `nn.Embedding` es una tabla de lookup que convierte índices enteros (tokens) en vectores densos. Útil para datos categóricos como palabras, IDs de usuarios, etc.

**Explicación:** Las redes neuronales necesitan números continuos. Embedding convierte categorías discretas (palabra 5, palabra 10) en vectores que capturan relaciones semánticas.

---

- Dado el siguiente código:

```python
embedding = nn.Embedding(6, 3)
input = torch.tensor([0, 2, 4])
output = embedding(input)
```

¿Cuál será la shape de `output` y qué representa cada dimensión?

**Respuesta para el parcial:** Shape `(3, 3)`. Primera dimensión (3): cantidad de tokens en el input. Segunda dimensión (3): embedding_dim (tamaño del vector por token).

**Explicación:** Cada índice (0, 2, 4) se reemplaza por su vector de 3 dimensiones de la tabla de embeddings.

---

- ¿Cómo inicializarías un embedding con pesos preentrenados?

**Respuesta para el parcial:** `embedding = nn.Embedding.from_pretrained(pretrained_weights)` donde `pretrained_weights` es un tensor con los vectores.

**Explicación:** Útil para usar embeddings como Word2Vec o GloVe ya entrenados en grandes corpus de texto.

---

## Capas convolucionales

- Dado el siguiente código:

```python
conv = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=3, stride=1, padding=1)
x = torch.randn(1, 1, 28, 28)
output = conv(x)
```

¿Qué shape tiene output? ¿Y si `stride` es `0`?

**Respuesta para el parcial:** Output shape: `(1, 3, 28, 28)`. Con padding=1 y kernel=3, las dimensiones espaciales se mantienen. Si stride=0 da error, stride debe ser ≥1.

**Explicación:** Fórmula: `out_size = (in_size + 2*padding - kernel_size)/stride + 1`. Con los valores dados: (28 + 2 - 3)/1 + 1 = 28.

---

## Capas de pooling

- ¿Qué es una capa de pooling y cuál es su propósito en una red convolucional?

**Respuesta para el parcial:** Pooling reduce las dimensiones espaciales tomando el máximo (MaxPool) o promedio (AvgPool) de regiones. Propósito: reducir parámetros, añadir invarianza a pequeñas traslaciones, y prevenir overfitting.

**Explicación:** Después de convoluciones, pooling comprime la información espacial, manteniendo las características más importantes.

---

- Dado el siguiente código:

```python
pool = nn.MaxPool2d(kernel_size=2, stride=2)
x = torch.randn(8, 3, 32, 32)
output = pool(x)
```

¿Cuál será la forma del tensor `output`?

**Respuesta para el parcial:** `(8, 3, 16, 16)`. El pooling reduce las dimensiones espaciales a la mitad (32/2 = 16). Batch y canales no cambian.

**Explicación:** kernel=2, stride=2 significa que cada ventana 2x2 produce 1 valor (el máximo), reduciendo cada dimensión espacial por 2.

---

## Capas recurrentes (`nn.RNN`, `nn.LSTM`, `nn.GRU`)

- Explica las principales diferencias entre `nn.RNN` y `nn.LSTM`.

**Respuesta para el parcial:** RNN simple sufre de vanishing gradient en secuencias largas. LSTM añade "puertas" (forget, input, output) y un cell state que permite memorizar dependencias a largo plazo.

**Explicación:** LSTM puede "decidir" qué información olvidar y qué recordar. RNN simple pierde información de pasos lejanos durante backpropagation.

---

- Dado el siguiente código:

```python
rnn = nn.RNN(input_size=10, hidden_size=20, num_layers=2, batch_first=True)
x = torch.randn(5, 15, 10)
output, h_n = rnn(x)
```

¿Cuál será la forma de `output` y `h_n`?

**Respuesta para el parcial:** `output`: `(5, 15, 20)` - (batch, seq_len, hidden_size). `h_n`: `(2, 5, 20)` - (num_layers, batch, hidden_size).

**Explicación:** `output` tiene la salida de cada timestep. `h_n` es el estado oculto final de cada capa. `batch_first=True` pone batch en primera dimensión.

---

## Preguntas sobre DenseNet

- Explica el concepto de conexión densa en DenseNet. ¿Cómo se diferencian de las conexiones residuales en ResNet?

**Respuesta para el parcial:** En DenseNet, cada capa recibe como entrada las salidas de TODAS las capas anteriores (concatenación). En ResNet, solo se suma la entrada del bloque a su salida (skip connection).

**Explicación:** DenseNet concatena features (canal crece), ResNet suma features (canal igual). DenseNet reutiliza más información pero usa más memoria.

---

- ¿Qué representa el parámetro `growth_rate` en una DenseNet?

**Respuesta para el parcial:** `growth_rate` (k) es cuántos canales/filtros añade cada capa. Si una capa tiene k0 canales y growth_rate=32, tras n capas tendrá k0 + n*32 canales.

**Explicación:** Controla qué tan rápido crece el número de features. Valor típico: 12-32. Más alto = más capacidad pero más memoria.

---

- ¿Qué beneficio aporta la concatenación de características en lugar de su suma como en ResNet?

**Respuesta para el parcial:** La concatenación preserva todas las características originales sin pérdida de información. La suma puede "perder" información al mezclar features.

**Explicación:** Con concatenación, capas posteriores tienen acceso directo a features de todas las capas anteriores, mejorando el flujo de gradientes y reutilización de features.

---

## Regularización

- ¿Qué es la regularización en el contexto de redes neuronales y por qué es importante?

**Respuesta para el parcial:** Son técnicas que previenen overfitting penalizando la complejidad del modelo o añadiendo ruido. Importante porque los modelos de deep learning tienen muchos parámetros y pueden memorizar datos fácilmente.

**Explicación:** Sin regularización, el modelo puede ajustarse perfectamente a los datos de entrenamiento pero fallar en datos nuevos.

---

- Nombre alguna de la técnicas vistas en clase y la idea detrás de ellas.

**Respuesta para el parcial:**
- **Dropout**: Apaga neuronas al azar, evita co-adaptación.
- **L2 (Weight Decay)**: Penaliza pesos grandes, favorece soluciones simples.
- **BatchNorm**: Normaliza activaciones, estabiliza entrenamiento.
- **Data Augmentation**: Genera variantes de los datos, aumenta diversidad.
- **Early Stopping**: Detiene cuando val_loss empeora, evita sobreentrenamiento.

**Explicación:** Todas buscan que el modelo aprenda patrones generales en vez de memorizar casos específicos.

---

## Data Augmentation

- ¿Qué es data augmentation y cómo ayuda a mejorar el desempeño de un modelo de aprendizaje profundo?

**Respuesta para el parcial:** Data augmentation genera variantes de los datos de entrenamiento aplicando transformaciones (rotación, flip, etc.). Aumenta la diversidad del dataset sin recolectar más datos, mejorando generalización.

**Explicación:** El modelo ve más variaciones de los mismos datos, aprendiendo a ser robusto a cambios irrelevantes (como orientación de una imagen).

---

- Proporciona ejemplos comunes de data augmentation para imágenes.

**Respuesta para el parcial:** Flip horizontal/vertical, rotación, recorte aleatorio (RandomCrop), cambio de brillo/contraste, zoom, traslación, añadir ruido.

**Explicación:** Cada transformación enseña al modelo que la clase no cambia por esos factores (un gato volteado sigue siendo gato).

---

- Proporcionar un ejemplo donde es contraproducente proporcionar una determinada transformación.

**Respuesta para el parcial:** Flip horizontal en reconocimiento de dígitos (un 6 volteado puede parecer 9) o en texto. Rotación extrema en clasificación de flechas direccionales.

**Explicación:** Si la transformación cambia la semántica de la imagen (el significado), confunde al modelo en vez de ayudarlo.

---

- Dado el siguiente código para data augmentation en imágenes:

```python
transform = transforms.Compose([
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(30),
        transforms.ToImage()
])
```

Explica qué hace cada transformación y sus parámetros. ¿Es posible que la imagen visualmente salga igual de cómo entró?

**Respuesta para el parcial:**
- `RandomHorizontalFlip(p=0.5)`: 50% probabilidad de voltear horizontalmente
- `RandomRotation(30)`: Rota aleatoriamente entre -30° y +30°
- `ToImage()`: Convierte a tensor imagen de PyTorch

Sí, es posible que salga igual si no hay flip (50% chance) y la rotación es ~0°.

**Explicación:** Las transformaciones son probabilísticas. Hay una pequeña probabilidad de que ninguna modifique significativamente la imagen.

---

---

## Early Stopping

- ¿Qué es el early stopping y cómo puede prevenir el sobreentrenamiento?

**Respuesta para el parcial:** Early stopping detiene el entrenamiento cuando la val_loss deja de mejorar por cierto número de épocas (patience). Previene overfitting al no seguir entrenando cuando el modelo empieza a memorizar.

**Explicación:** Si seguimos entrenando después del punto óptimo, train_loss sigue bajando pero val_loss sube (overfitting). Early stopping detecta y evita esto.

---

- Describe cómo la loss en validación (`val_loss`) se utiliza para implementar el early stopping.

**Respuesta para el parcial:** Se monitorea val_loss cada época. Si no mejora en N épocas consecutivas (patience), se detiene. Se guarda el mejor modelo (menor val_loss) para usarlo al final.

**Explicación:** Ejemplo: patience=5. Si val_loss no baja en 5 épocas seguidas, paramos y recuperamos los pesos de la mejor época.

---

---

## Preguntas sobre pre-procesamiento y vocabulario

### Preprocesamiento

- ¿Cuál es el objetivo de normalizar texto antes de entrenar un modelo NLP? Proporciona un ejemplo práctico.

**Respuesta para el parcial:** Reducir variabilidad innecesaria: "Hola", "HOLA", "hola" → "hola". Reduce tamaño del vocabulario y mejora generalización. Ejemplo: convertir a minúsculas, eliminar puntuación, eliminar stopwords.

**Explicación:** Sin normalización, el modelo trataría "Gato", "gato" y "GATO" como palabras completamente diferentes.

---

- ¿Cuáles son las transformaciones que aplicarías a un texto para analizar su sentimiento?

**Respuesta para el parcial:** Convertir a minúsculas, eliminar puntuación (excepto ! y ?), eliminar URLs/menciones, tokenizar, posiblemente mantener emojis (contienen sentimiento), eliminar stopwords opcionales.

**Explicación:** Para sentimiento, conservamos palabras que expresan emoción. Los signos ! y emojis pueden indicar intensidad de sentimiento.

---

### Vocabulario

- ¿Qué es un token y cómo se relaciona con un vocabulario en NLP?

**Respuesta para el parcial:** Un token es una unidad de texto (palabra, subpalabra, o caracter). El vocabulario es el conjunto de todos los tokens únicos con sus índices numéricos asignados.

**Explicación:** Tokenización divide el texto en tokens. El vocabulario mapea cada token a un número único que la red neuronal puede procesar.

---

- Explica el propósito de limitar el tamaño del vocabulario (`max_vocab_size`) en datasets grandes. ¿Cuáles descartarías?

**Respuesta para el parcial:** Limitar el vocabulario reduce memoria y parámetros del embedding. Se descartan las palabras menos frecuentes (que aportan poco y podrían ser ruido/errores).

**Explicación:** Palabras raras tienen pocos ejemplos para aprender un buen embedding. Mejor agruparlas como `<unk>` (unknown).

---

- Dado el siguiente vocabulario:

```python
vocab = {"<pad>": 0, "<unk>": 1, "el": 2, "análisis": 3, "texto": 4}
```

¿Cómo se representaría la frase `"el análisis de texto"` usando este vocabulario?

**Respuesta para el parcial:** `[2, 3, 1, 4]`. "el"→2, "análisis"→3, "de"→1 (no está, es `<unk>`), "texto"→4.

**Explicación:** Cada palabra se reemplaza por su índice. Las palabras fuera del vocabulario se mapean a `<unk>`.

---

### Padding y truncamiento

- Explica el propósito del padding y truncamiento en NLP.

**Respuesta para el parcial:** Las redes necesitan secuencias de longitud fija. Padding añade tokens `<pad>` a secuencias cortas. Truncamiento corta secuencias largas. Ambos permiten crear batches uniformes.

**Explicación:** Sin esto, cada secuencia tendría distinta longitud y no podríamos procesarlas en batch eficientemente.

---

### Representación numérica de texto

- ¿Por qué no podemos usar directamente palabras en una red neuronal?

**Respuesta para el parcial:** Las redes neuronales solo procesan números (tensores). Las palabras son strings/símbolos discretos sin valor numérico ni relaciones matemáticas definidas.

**Explicación:** Necesitamos convertir palabras a vectores numéricos donde operaciones matemáticas (suma, multiplicación) tengan sentido.

---

- Explica cómo se utiliza `nn.Embedding` para mapear palabras a vectores densos.

**Respuesta para el parcial:** `nn.Embedding(vocab_size, embed_dim)` es una tabla donde cada fila es el vector de una palabra. Dado un índice, retorna su vector. Los vectores se aprenden durante el entrenamiento.

**Explicación:** Es como una matriz W. Input índice i → Output fila W[i]. Los pesos se actualizan por backpropagation para que palabras similares tengan vectores cercanos.

---

- Dado un embedding:

```python
embedding = nn.Embedding(10, 4)
input = torch.tensor([[0, 1, 2]])
```

¿Cuál será la forma de la salida y qué representa cada dimensión?

**Respuesta para el parcial:** Forma: `(1, 3, 4)`. 1 = batch_size, 3 = longitud de secuencia (tokens), 4 = embedding_dim (dimensión del vector por token).

**Explicación:** Cada uno de los 3 índices se reemplaza por un vector de 4 dimensiones. El batch tiene 1 secuencia.

---

---

## Seq2Seq

- Explica cómo funcionan el codificador (encoder) y el decodificador (decoder) en un modelo Seq2Seq. ¿Qué información pasa del primero al segundo?

**Respuesta para el parcial:** El encoder procesa la secuencia de entrada y produce un "context vector" (estado oculto final) que resume toda la información. El decoder recibe este context vector como estado inicial y genera la secuencia de salida token a token.

**Explicación:** Encoder: secuencia → vector fijo. Decoder: vector fijo → secuencia. El estado oculto final del encoder "transfiere el conocimiento" al decoder.

---

- ¿Qué significa `Teacher Forcing` y cómo afecta al entrenamiento?

**Respuesta para el parcial:** Teacher forcing usa la salida correcta (ground truth) como entrada del siguiente paso del decoder en vez de la predicción anterior. Acelera entrenamiento pero puede causar discrepancia train/test.

**Explicación:** En entrenamiento: usamos tokens reales. En inferencia: usamos predicciones. Esta diferencia puede degradar rendimiento (exposure bias).

---

- ¿Por qué es útil agregar un token `<SOS>` al inicio de una secuencia en el decodificador?

**Respuesta para el parcial:** `<SOS>` (Start Of Sequence) indica al decoder que comience a generar. Sin él, no sabría qué token usar como primera entrada.

**Explicación:** El decoder necesita una entrada inicial. `<SOS>` es una señal especial que significa "empieza a generar".

---

- Durante la inferencia, ¿cómo se determina el fin de una predicción en un modelo Seq2Seq?

**Respuesta para el parcial:** El modelo genera hasta producir el token `<EOS>` (End Of Sequence) o hasta alcanzar una longitud máxima predefinida.

**Explicación:** `<EOS>` es un token especial que el modelo aprende a predecir cuando la secuencia debe terminar.

---

---

## Transformers

- ¿Cuántos mecanismos de atención hay en el encoder y decoder del transformer del paper "attention is all you need"? ¿En qué se diferencian?

**Respuesta para el parcial:** Hay 3 mecanismos: 1) Self-attention en encoder (atiende a toda la entrada), 2) Masked self-attention en decoder (solo atiende a posiciones anteriores), 3) Cross-attention en decoder (atiende al output del encoder).

**Explicación:** Self-attention relaciona posiciones de la misma secuencia. Cross-attention conecta decoder con encoder. La máscara en decoder evita "ver el futuro".

---

- Dado el cálculo de atención:

```python
scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
attention = torch.softmax(scores, dim=-1)
context = torch.matmul(attention, value)
```

Explica qué hace cada línea.

**Respuesta para el parcial:**
1. `scores`: producto punto entre query y keys, dividido por √d_k para estabilizar gradientes (scaled dot-product)
2. `attention`: softmax convierte scores en probabilidades (pesos que suman 1)
3. `context`: suma ponderada de values según los pesos de atención

**Explicación:** Query pregunta "qué busco", keys dicen "qué tengo", values son "qué devuelvo". La atención decide cuánto de cada value incluir.

---

- Dado el siguiente fragmento:

```python
pos_encoding = torch.sin(position / (10000 ** (2 * (i // 2) / d_model)))
```

¿Cómo ayuda este cálculo a incorporar información posicional en un Transformer?

**Respuesta para el parcial:** Los Transformers no tienen noción inherente del orden. El positional encoding añade un vector único a cada posición usando funciones seno/coseno de diferentes frecuencias, permitiendo distinguir posiciones.

**Explicación:** Cada posición tiene una "firma" única. Las frecuencias variadas permiten al modelo aprender relaciones de posición relativa (posición 5 vs posición 10).

---

- Explica cómo las máscaras evitan que un Transformer preste atención a posiciones no deseadas durante el entrenamiento.

**Respuesta para el parcial:** La máscara pone -∞ en los scores de posiciones prohibidas antes del softmax. El softmax convierte -∞ en 0, eliminando esa atención. En decoder, la máscara triangular impide ver tokens futuros.

**Explicación:** Durante entrenamiento del decoder, al predecir posición t, no debe ver posiciones >t (sería trampa). La máscara triangular inferior bloquea esas posiciones.

---
