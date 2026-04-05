# Preguntas preparación parcial - CON RESPUESTAS

## Propiedades de los tensores

- Dado el tensor `x = torch.tensor([[1, 2], [3, 4]])`, ¿cuál es su `dtype`, `device`, `ndim` y `shape`?

**Respuesta para el parcial:** `dtype=torch.int64`, `device=cpu`, `ndim=2`, `shape=torch.Size([2, 2])`.

**Explicación:** PyTorch infiere `int64` porque los valores son enteros sin punto decimal. `cpu` es el device por defecto (si quisieras float usarías `torch.tensor([[1.0, 2.0], [3.0, 4.0]])`). `ndim=2` porque hay dos niveles de corchetes `[[...], [...]]`. Shape `[2, 2]` = 2 filas × 2 columnas.

---

- Explica la utilidad de la propiedad `device` en PyTorch. Proporciona un ejemplo para mover un tensor a la GPU.

**Respuesta para el parcial:** `device` indica dónde está almacenado el tensor (CPU o GPU). Para moverlo a GPU: `x = x.to('cuda')` o `x = x.cuda()`.

**Explicación:** Si intentas `tensor_gpu + tensor_cpu` da error. La GPU tiene su propia memoria separada de la RAM, por eso hay que mover datos explícitamente. La GPU acelera porque tiene miles de núcleos que hacen operaciones matriciales en paralelo.

---

- Crea un tensor unidimensional con 5 elementos y muestra cómo consultar su número de dimensiones y su forma.

**Respuesta para el parcial:** `x = torch.tensor([1, 2, 3, 4, 5])`, luego `x.ndim` → 1, y `x.shape` → `torch.Size([5])`.

**Explicación:** `ndim=1` porque solo hay un nivel de corchetes `[...]` (es un vector, no una matriz). `shape=(5,)` indica que tiene 5 elementos en ese único eje. Una matriz 3×4 tendría `ndim=2` y `shape=(3,4)`.

---

## Concepto de Broadcasting

- Explica el concepto de broadcasting en PyTorch. ¿Por qué es útil?

**Respuesta para el parcial:** Broadcasting permite operar tensores de distintas formas expandiendo automáticamente las dimensiones compatibles. Es útil porque evita crear copias innecesarias y hace el código más simple.

**Explicación:** Sin broadcasting, para sumar `[[1,2],[3,4]] + 10` habría que crear `[[10,10],[10,10]]` manualmente. PyTorch "estira" automáticamente el tensor pequeño. Regla: dos dimensiones son compatibles si son iguales o una de ellas es 1.

---

- Dado `x = torch.tensor([[1, 2], [3, 4]])` y `y = torch.tensor([10, 20])`, ¿qué sucederá al realizar `z = x + y`? Especifica la forma y los valores de `z`.

**Respuesta para el parcial:** `z` tendrá forma `(2, 2)` con valores `[[11, 22], [13, 24]]`. El vector `y` se "expande" a cada fila.

**Explicación:** `y` tiene forma `(2,)`. PyTorch lo trata como `(1, 2)` y lo "replica" virtualmente para cada fila: fila 0: `[1,2] + [10,20] = [11,22]`, fila 1: `[3,4] + [10,20] = [13,24]`. No crea copias reales en memoria.

---

- ¿Es posible sumar un tensor con forma `(4, 3)` y otro con forma `(3,)`? ¿Por qué?

**Respuesta para el parcial:** Sí, es posible. El tensor `(3,)` se expande a `(1, 3)` y luego se replica 4 veces para formar `(4, 3)`, coincidiendo con el primero.

**Explicación:** Broadcasting compara de derecha a izquierda: `(4, 3)` vs `(3,)` → última dim: 3==3 ✓. El `(3,)` se trata como `(1, 3)` y se replica 4 veces. Sería incompatible si fuera `(4, 3)` vs `(4,)` porque 3≠4.

---

## Slicing en tensores

- Dado el tensor `x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`, escribe el código para seleccionar la columna segunda columna.

**Respuesta para el parcial:** `x[:, 1]` → `tensor([2, 5, 8])`.

**Explicación:** La sintaxis es `[filas, columnas]`. `:` = "todas las filas" (equivale a `0:3`). `1` = columna índice 1 (la segunda, porque índices empiezan en 0). Así extrae el elemento de cada fila en la columna 1: 2, 5, 8.

---

- Extrae las dos primeras filas y las dos primeras columnas del tensor `x` con forma `(3, 3)`.

**Respuesta para el parcial:** `x[:2, :2]` → `tensor([[1, 2], [4, 5]])`.

**Explicación:** `:2` = índices 0 y 1 (el 2 no se incluye, como en `range(2)`). `x[:2, :2]` toma filas 0,1 y columnas 0,1. De la matriz original, es la esquina superior izquierda de 2×2.

---

- Usa slicing para seleccionar los elementos de las posiciones impares en un tensor unidimensional.

**Respuesta para el parcial:** `x[1::2]` selecciona elementos en índices 1, 3, 5, ... (posiciones impares).

**Explicación:** La sintaxis es `[inicio:fin:paso]`. `1::2` significa: empezar en índice 1, ir hasta el final, de 2 en 2.

---

## Diferencias entre cat y stack

- ¿Cuál es la principal diferencia entre `torch.cat` y `torch.stack`? Proporciona un ejemplo.

**Respuesta para el parcial:** `cat` concatena en una dimensión existente (no crea nuevas dimensiones). `stack` crea una nueva dimensión y apila los tensores en ella.

**Explicación:** `cat([a,b], dim=0)` con `a=(3,)` y `b=(3,)` → `(6,)`: los elementos se ponen uno tras otro. `stack([a,b], dim=0)` → `(2, 3)`: crea una matriz donde cada tensor original es una fila. Stack añade una dimensión, cat no.

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

**Explicación:** `(1, 3, 1)` tiene dos dimensiones "sobrantes" de tamaño 1. `squeeze()` las elimina dejando `(3,)`. Útil cuando operaciones añaden dimensiones innecesarias. `squeeze(0)` eliminaría solo la primera → `(3, 1)`.

---

- ¿Qué hace `torch.unsqueeze(x, dim=0)`? Explica y proporciona un ejemplo.

**Respuesta para el parcial:** Añade una nueva dimensión de tamaño 1 en la posición indicada. Si `x` tiene forma `(3,)`, después de `unsqueeze(x, 0)` tiene forma `(1, 3)`.

**Explicación:** Si `x=(3,)` es un vector, `unsqueeze(x, 0)` lo convierte en matriz `(1, 3)` (una fila). `unsqueeze(x, 1)` daría `(3, 1)` (una columna). Muy usado para añadir dimensión de batch cuando el modelo espera `(batch, features)`.

---

- ¿Cómo reestructurarías un tensor de forma `(2, 3)` a `(6,)` usando `reshape`?

**Respuesta para el parcial:** `x.reshape(6)` o `x.reshape(-1)`. El `-1` calcula automáticamente el tamaño.

**Explicación:** `reshape` reorganiza los 6 elementos (2×3=6) en una nueva forma. Lee en orden fila por fila: `[[1,2,3],[4,5,6]]` → `[1,2,3,4,5,6]`. `-1` significa "calcula tú esta dimensión": `reshape(2, -1)` con 6 elementos → `(2, 3)`.

---

## Uso de GPU

- Explica cómo verificar si una GPU está disponible en PyTorch.

**Respuesta para el parcial:** `torch.cuda.is_available()` retorna `True` si hay GPU disponible, `False` si no.

**Explicación:** CUDA es el driver de NVIDIA para GPU. Esta función verifica que: 1) hay GPU NVIDIA física, 2) drivers CUDA instalados, 3) PyTorch compilado con soporte CUDA. Patrón común: `device = 'cuda' if torch.cuda.is_available() else 'cpu'`.

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

**Explicación:** `__init__`: carga/prepara datos (ej: leer CSV). `__len__`: DataLoader llama esto para saber cuántos batches crear. `__getitem__(idx)`: DataLoader llama `dataset[0]`, `dataset[1]`, etc. para obtener cada muestra. Sin estas funciones, DataLoader no puede iterar.

---

- Explica cómo usar el parámetro `batch_size` en un `DataLoader` y qué impacto tiene en el entrenamiento. Muestre alguna situación que convenga subirlo/bajarlo.

**Respuesta para el parcial:** `batch_size` define cuántas muestras se procesan juntas. Mayor batch = más estable pero más memoria. Menor batch = más ruido pero menos memoria. Subir: GPU con mucha RAM. Bajar: poca memoria o querer más regularización.

**Explicación:** Con batch=32, se promedian gradientes de 32 muestras → dirección más estable. Con batch=1, cada muestra cambia los pesos → más ruidoso pero puede escapar mínimos locales. GPU tiene memoria limitada: si batch muy grande → "CUDA out of memory".

---

- ¿Qué hace el parámetro `shuffle` en un `DataLoader` y cuándo es útil activarlo?

**Respuesta para el parcial:** `shuffle=True` mezcla aleatoriamente los datos en cada época. Se activa en entrenamiento para evitar que el modelo aprenda el orden de los datos.

**Explicación:** Sin shuffle, si los datos están ordenados (ej: primero todos los gatos, luego perros), el modelo vería solo gatos al inicio → aprendizaje sesgado. Mezclando, cada batch tiene variedad. En validación `shuffle=False` porque solo queremos medir, no cambiar nada.

---

- Dado el siguiente código:

```python
dataloader = DataLoader(dataset, batch_size=4, num_workers=2)
```

¿Qué significa `num_workers` y cómo afecta el rendimiento del entrenamiento?

**Respuesta para el parcial:** `num_workers` indica cuántos subprocesos paralelos cargan datos. Más workers = carga de datos más rápida, GPU menos ociosa esperando datos.

**Explicación:** Mientras GPU entrena batch 1, los workers cargan batch 2, 3... en paralelo. Sin workers, GPU termina y espera que CPU cargue el siguiente batch (cuello de botella). Regla general: `num_workers = 4 * num_gpus`. En Windows a veces da problemas, usar 0.

---

## Train & Eval

- ¿Cuál es la diferencia entre `model.train()` y `model.eval()` en PyTorch?

**Respuesta para el parcial:** `model.train()` activa capas como Dropout y BatchNorm en modo entrenamiento. `model.eval()` las pone en modo inferencia (Dropout desactivado, BatchNorm usa estadísticas globales).

**Explicación:** Dropout en train: apaga 50% neuronas al azar. En eval: no apaga ninguna. BatchNorm en train: calcula media/varianza del batch actual. En eval: usa media/varianza acumuladas de todo el entrenamiento. Si no cambias el modo, resultados de evaluación serán incorrectos.

---

- ¿Qué sucede con las capas de dropout cuando llamas a `model.eval()`?

**Respuesta para el parcial:** Se desactivan completamente: no "apagan" ninguna neurona, todas las conexiones se usan.

**Explicación:** En training, dropout "apaga" neuronas para forzar redundancia. En eval, queremos la predicción más precisa posible → usamos TODAS las neuronas. PyTorch automáticamente escala las salidas para compensar que ya no hay neuronas apagadas.

---

- Dado el siguiente código:

```python
model.eval()
with torch.no_grad():
        output = model(x)
```

¿Por qué se utiliza `torch.no_grad()` en este caso?

**Respuesta para el parcial:** `torch.no_grad()` desactiva el cálculo de gradientes, ahorrando memoria y acelerando la inferencia. No necesitamos gradientes si no vamos a hacer backpropagation.

**Explicación:** PyTorch guarda todas las operaciones intermedias para calcular gradientes (backward). Esto usa mucha memoria. En evaluación no vamos a llamar `loss.backward()`, así que ¿para qué guardar todo eso? `no_grad()` dice "no guardes nada, solo calcula el resultado".

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

### Diferencia entre Train, Validation y Test

**Respuesta para el parcial:**
- **Train**: datos para ajustar los pesos del modelo (backpropagation)
- **Validation**: datos para monitorear durante entrenamiento, ajustar hiperparámetros y decidir cuándo parar (early stopping). NO se usa para entrenar.
- **Test**: datos que NUNCA se tocan hasta el final. Evaluación única para reportar rendimiento real.

**Explicación:**
- **Train set**: el modelo "ve" estos datos y aprende de ellos. Se usa para calcular gradientes y actualizar pesos.
- **Validation set**: el modelo "ve" estos datos pero NO aprende de ellos. Sirve para: 1) monitorear overfitting (si val_loss sube → overfitting), 2) elegir hiperparámetros (¿lr=0.01 o lr=0.001?), 3) decidir cuándo parar (early stopping). Como tomamos decisiones basadas en val_loss, hay riesgo de "sobreajustar" a validación indirectamente.
- **Test set**: evaluación final, UNA sola vez. No se usa para ninguna decisión. El número que reportas en un paper/examen es el test accuracy/loss. Si lo usas múltiples veces para ajustar, ya no es "test" sino otra validación.

**Flujo típico:**
```
1. Entrenar con train_loader → ajustar pesos
2. Evaluar con val_loader → decidir si parar, ajustar hiperparámetros
3. Repetir 1-2 hasta satisfecho
4. UNA VEZ al final: evaluar con test_loader → reportar resultado
```

**Proporciones típicas:** 70% train, 15% validation, 15% test (o 80/10/10).

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

**Explicación:** La capa tiene una matriz de pesos W de forma `(out_features, in_features)` y un vector bias b de forma `(out_features,)`. Cada salida es: `output[i] = sum(input * W[i]) + b[i]`. Es la operación fundamental que conecta capas en una red neuronal.

---

- Dado el siguiente código:

```python
layer = nn.Linear(4, 2)
x = torch.randn(3, 4)
output = layer(x)
```

¿Cuál será la forma de `output` y qué representa cada dimensión?

**Respuesta para el parcial:** `output` tiene forma `(3, 2)`. 3 es el batch_size (número de muestras), 2 es out_features (dimensión de salida por muestra).

**Explicación:** `nn.Linear(4, 2)` tiene matriz W de `(2, 4)`. Cada fila de x (4 valores) se multiplica por W: `[1×4] @ [4×2] = [1×2]`. Como x tiene 3 filas (batch=3), se hace para cada fila independientemente → salida `(3, 2)`. El "3" del batch se preserva, solo cambia la última dimensión de 4→2.

---

- ¿Qué impacto tiene el uso de `bias=True` al definir una capa `nn.Linear`?

**Respuesta para el parcial:** Con `bias=True` (default) se añade un término constante a cada neurona: `y = Wx + b`. Sin bias, la salida siempre pasa por el origen cuando la entrada es cero.

**Explicación:** Sin bias: `y = Wx`. Si x=0, entonces y=0 siempre. Con bias: `y = Wx + b`, la salida puede ser distinta de cero aunque la entrada sea cero. Esto permite que cada neurona tenga un "umbral" de activación ajustable.

---

## Capa `nn.Dropout`

- ¿Cuál es el propósito de la capa `nn.Dropout` y cómo afecta el entrenamiento de un modelo?

**Respuesta para el parcial:** Dropout es una técnica de regularización que "apaga" neuronas aleatoriamente (las pone a 0) durante el entrenamiento con probabilidad `p`. Previene overfitting al forzar redundancia.

**Explicación:** Sin dropout, una neurona podría "especializarse" demasiado y el resto depender de ella → si falla, todo falla. Con dropout, cada neurona debe aprender a ser útil por sí sola porque no sabe cuáles de sus compañeras estarán disponibles. Esto crea redundancia y mejor generalización.

---

- Dado el siguiente código:

```python
dropout = nn.Dropout(p=0.5)
x = torch.tensor([1.0, 2.0, 3.0])
output = dropout(x)
```

Explica qué valores podría tomar `output`.

**Respuesta para el parcial:** Cada elemento tiene 50% probabilidad de ser 0. Los que no se apagan se escalan por `1/(1-p) = 2`. Posibles outputs: `[0, 4, 6]`, `[2, 0, 0]`, `[2, 4, 6]`, etc.

**Explicación:** Si `p=0.5`, cada valor tiene 50% de ser 0. Los sobrevivientes se multiplican por 2 (=1/(1-0.5)). Ejemplo: `[1, 2, 3]` podría dar `[0, 4, 0]` o `[2, 0, 6]`. El escalado asegura que la suma esperada sea igual con o sin dropout, evitando reescalar en inferencia.

---

## Capa `nn.Embedding`

- ¿Qué representa la capa `nn.Embedding` y para qué tipo de datos es útil?

**Respuesta para el parcial:** `nn.Embedding` es una tabla de lookup que convierte índices enteros (tokens) en vectores densos. Útil para datos categóricos como palabras, IDs de usuarios, etc.

**Explicación:** No puedes meter la palabra "gato" directamente a una red. Con embedding, "gato"=índice 5 → vector [0.2, -0.5, 0.8, ...]. Estos vectores se aprenden: palabras similares ("gato", "perro") terminan con vectores cercanos. Es como una tabla de búsqueda entrenable.

---

- Dado el siguiente código:

```python
embedding = nn.Embedding(6, 3)
input = torch.tensor([0, 2, 4])
output = embedding(input)
```

¿Cuál será la shape de `output` y qué representa cada dimensión?

**Respuesta para el parcial:** Shape `(3, 3)`. Primera dimensión (3): cantidad de tokens en el input. Segunda dimensión (3): embedding_dim (tamaño del vector por token).

**Explicación:** `Embedding(6, 3)` = tabla de 6 filas × 3 columnas. Input `[0, 2, 4]` significa "dame las filas 0, 2 y 4". Cada índice se reemplaza por su fila de 3 valores. Resultado: 3 tokens × 3 dimensiones = `(3, 3)`.

---

- ¿Cómo inicializarías un embedding con pesos preentrenados?

**Respuesta para el parcial:** `embedding = nn.Embedding.from_pretrained(pretrained_weights)` donde `pretrained_weights` es un tensor con los vectores.

**Explicación:** Word2Vec/GloVe entrenaron embeddings en billones de palabras. En vez de aprender desde cero, cargas esos vectores ya buenos. `pretrained_weights` es tensor de `(vocab_size, embed_dim)`. Puedes congelarlos (`requires_grad=False`) o afinarlos.

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

**Explicación:** Fórmula: `out = (in + 2*pad - kernel)/stride + 1`. Aquí: (28 + 2×1 - 3)/1 + 1 = 28. El padding=1 añade borde de ceros para que kernel 3×3 no reduzca tamaño. `out_channels=3` significa 3 filtros diferentes → 3 mapas de salida. Input `(batch, canales, alto, ancho)` → Output misma estructura.

---

## Capas de pooling

- ¿Qué es una capa de pooling y cuál es su propósito en una red convolucional?

**Respuesta para el parcial:** Pooling reduce las dimensiones espaciales tomando el máximo (MaxPool) o promedio (AvgPool) de regiones. Propósito: reducir parámetros, añadir invarianza a pequeñas traslaciones, y prevenir overfitting.

**Explicación:** Imagen 32×32 después de MaxPool2d(2,2) → 16×16. Cada ventana 2×2 se reduce a 1 pixel (el máximo). Beneficios: menos píxeles = menos cómputo, y si el "ojo" del gato se mueve 1 pixel, el máximo de la zona sigue siendo el mismo → invarianza a pequeños desplazamientos.

---

- Dado el siguiente código:

```python
pool = nn.MaxPool2d(kernel_size=2, stride=2)
x = torch.randn(8, 3, 32, 32)
output = pool(x)
```

¿Cuál será la forma del tensor `output`?

**Respuesta para el parcial:** `(8, 3, 16, 16)`. El pooling reduce las dimensiones espaciales a la mitad (32/2 = 16). Batch y canales no cambian.

**Explicación:** Input `(8, 3, 32, 32)` = 8 imágenes, 3 canales (RGB), 32×32 píxeles. Pooling con kernel=2, stride=2: ventana 2×2 sin solapamiento → 32/2=16. Solo cambian dimensiones espaciales. Batch (8) y canales (3) se mantienen igual.

---

## Capas recurrentes (`nn.RNN`, `nn.LSTM`, `nn.GRU`)

- Explica las principales diferencias entre `nn.RNN` y `nn.LSTM`.

**Respuesta para el parcial:** RNN simple sufre de vanishing gradient en secuencias largas. LSTM añade "puertas" (forget, input, output) y un cell state que permite memorizar dependencias a largo plazo.

**Explicación:** En RNN, gradientes se multiplican en cada paso temporal → si secuencia es larga, gradientes se hacen muy pequeños (vanishing) o muy grandes (exploding). LSTM tiene "autopista" de información (cell state) donde los gradientes fluyen sin multiplicarse tanto. Las puertas controlan qué entra/sale de esta autopista.

---

- Dado el siguiente código:

```python
rnn = nn.RNN(input_size=10, hidden_size=20, num_layers=2, batch_first=True)
x = torch.randn(5, 15, 10)
output, h_n = rnn(x)
```

¿Cuál será la forma de `output` y `h_n`?

**Respuesta para el parcial:** `output`: `(5, 15, 20)` - (batch, seq_len, hidden_size). `h_n`: `(2, 5, 20)` - (num_layers, batch, hidden_size).

**Explicación:** Input `(5, 15, 10)` = 5 secuencias (batch), 15 pasos temporales, 10 features por paso. `output (5, 15, 20)`: para cada paso temporal, la salida de la última capa (20 = hidden_size). `h_n (2, 5, 20)`: estado oculto FINAL de cada capa (2 capas). `batch_first=True` hace que batch sea dim 0 en vez de dim 1.

---

## Preguntas sobre DenseNet

- Explica el concepto de conexión densa en DenseNet. ¿Cómo se diferencian de las conexiones residuales en ResNet?

**Respuesta para el parcial:** En DenseNet, cada capa recibe como entrada las salidas de TODAS las capas anteriores (concatenación). En ResNet, solo se suma la entrada del bloque a su salida (skip connection).

**Explicación:** ResNet: `output = F(x) + x` (suma). DenseNet: `output = concat(x, F(x))` (concatena). En ResNet, si x tiene 64 canales, output tiene 64. En DenseNet, si x tiene 64 y F(x) añade 32, output tiene 96. DenseNet preserva TODA la información original, ResNet la "mezcla".

---

- ¿Qué representa el parámetro `growth_rate` en una DenseNet?

**Respuesta para el parcial:** `growth_rate` (k) es cuántos canales/filtros añade cada capa. Si una capa tiene k0 canales y growth_rate=32, tras n capas tendrá k0 + n*32 canales.

**Explicación:** Si empiezas con 64 canales y growth_rate=32: capa 1 → 64+32=96, capa 2 → 96+32=128, capa 3 → 160... Valor bajo (12) = modelo compacto. Valor alto (32) = más capacidad pero crece rápido en memoria. Por eso DenseNet usa "transition layers" para reducir canales periódicamente.

---

- ¿Qué beneficio aporta la concatenación de características en lugar de su suma como en ResNet?

**Respuesta para el parcial:** La concatenación preserva todas las características originales sin pérdida de información. La suma puede "perder" información al mezclar features.

**Explicación:** Suma: `a + b` puede perder información (si a=5, b=-5 → 0). Concatenación: `[a, b]` preserva ambos valores intactos. En DenseNet, capa 10 puede "ver" directamente las features de capa 1, 2, 3... sin que hayan sido modificadas. Mejor flujo de gradientes y reutilización de features primitivas (bordes) junto con complejas (objetos).

---

## Regularización

- ¿Qué es la regularización en el contexto de redes neuronales y por qué es importante?

**Respuesta para el parcial:** Son técnicas que previenen overfitting penalizando la complejidad del modelo o añadiendo ruido. Importante porque los modelos de deep learning tienen muchos parámetros y pueden memorizar datos fácilmente.

**Explicación:** Una red con millones de parámetros puede memorizar el dataset completo (train_loss≈0) pero no aprender patrones generales. Regularización añade "fricción": penaliza pesos grandes, apaga neuronas, etc. Esto fuerza al modelo a encontrar soluciones más simples que generalicen mejor.

---

- Nombre alguna de la técnicas vistas en clase y la idea detrás de ellas.

**Respuesta para el parcial:**
- **Dropout**: Apaga neuronas al azar, evita co-adaptación.
- **L2 (Weight Decay)**: Penaliza pesos grandes, favorece soluciones simples.
- **BatchNorm**: Normaliza activaciones, estabiliza entrenamiento.
- **Data Augmentation**: Genera variantes de los datos, aumenta diversidad.
- **Early Stopping**: Detiene cuando val_loss empeora, evita sobreentrenamiento.

**Explicación:** Dropout: "no confíes en una sola neurona". L2: "no hagas pesos enormes, mantén todo pequeño". BatchNorm: "normaliza para estabilizar". Data Augmentation: "aprende a reconocer gatos en cualquier orientación". Early Stopping: "para antes de que empieces a memorizar".

---

## Data Augmentation

- ¿Qué es data augmentation y cómo ayuda a mejorar el desempeño de un modelo de aprendizaje profundo?

**Respuesta para el parcial:** Data augmentation genera variantes de los datos de entrenamiento aplicando transformaciones (rotación, flip, etc.). Aumenta la diversidad del dataset sin recolectar más datos, mejorando generalización.

**Explicación:** Si solo tienes 1000 fotos de gatos, con augmentation generas variantes: gato volteado, gato rotado, gato más brillante... El modelo aprende que "gato" no depende de la orientación exacta. Es como tener más datos gratis, sin fotografiar más gatos.

---

- Proporciona ejemplos comunes de data augmentation para imágenes.

**Respuesta para el parcial:** Flip horizontal/vertical, rotación, recorte aleatorio (RandomCrop), cambio de brillo/contraste, zoom, traslación, añadir ruido.

**Explicación:** Flip: gato mirando izquierda = gato mirando derecha. Rotación: gato inclinado sigue siendo gato. Crop: gato parcialmente visible sigue siendo gato. Brillo: gato en sombra = gato al sol. Cada transformación enseña invarianza a ese factor específico.

---

- Proporcionar un ejemplo donde es contraproducente proporcionar una determinada transformación.

**Respuesta para el parcial:** Flip horizontal en reconocimiento de dígitos (un 6 volteado puede parecer 9) o en texto. Rotación extrema en clasificación de flechas direccionales.

**Explicación:** El dígito "6" rotado 180° es visualmente idéntico a "9". Si aplicamos rotación, el modelo aprenderá que 6=9, lo cual es incorrecto. Otro ejemplo: en radiografías médicas, voltear puede cambiar izquierda↔derecha del paciente, información crucial para el diagnóstico.

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

**Explicación:** RandomHorizontalFlip: 50% flip, 50% nada. RandomRotation(30): ángulo aleatorio entre -30° y +30°, incluyendo ~0°. Si no hay flip (50%) y rotación≈0° (baja probabilidad), la imagen sale casi igual. Esto es válido: el modelo también debe aprender imágenes sin transformar.

---

---

## Early Stopping

- ¿Qué es el early stopping y cómo puede prevenir el sobreentrenamiento?

**Respuesta para el parcial:** Early stopping detiene el entrenamiento cuando la val_loss deja de mejorar por cierto número de épocas (patience). Previene overfitting al no seguir entrenando cuando el modelo empieza a memorizar.

**Explicación:** Imagina gráfica: train_loss siempre baja. val_loss baja, llega a un mínimo, y luego sube. Ese punto mínimo es el "sweet spot". Early stopping: "si val_loss no mejora en 5 épocas, para y guarda el modelo del mínimo". Sin esto, seguirías entrenando y empeorando en validación.

---

- Describe cómo la loss en validación (`val_loss`) se utiliza para implementar el early stopping.

**Respuesta para el parcial:** Se monitorea val_loss cada época. Si no mejora en N épocas consecutivas (patience), se detiene. Se guarda el mejor modelo (menor val_loss) para usarlo al final.

**Explicación:** Algoritmo: guardar `best_val_loss = ∞`, `counter = 0`. Cada época: si val_loss < best_val_loss → guardar modelo, reset counter. Si no → counter += 1. Si counter >= patience → STOP. Al final, cargar el modelo guardado (el del mejor val_loss, no el último).

---

---

## Preguntas sobre pre-procesamiento y vocabulario

### Preprocesamiento

- ¿Cuál es el objetivo de normalizar texto antes de entrenar un modelo NLP? Proporciona un ejemplo práctico.

**Respuesta para el parcial:** Reducir variabilidad innecesaria: "Hola", "HOLA", "hola" → "hola". Reduce tamaño del vocabulario y mejora generalización. Ejemplo: convertir a minúsculas, eliminar puntuación, eliminar stopwords.

**Explicación:** Sin normalización, "Gato", "gato", "GATO" serían 3 entradas diferentes en el vocabulario, cada una con su propio embedding. Esto desperdicia capacidad. Normalizando a "gato", todas contribuyen a aprender un solo embedding más robusto. Menos vocabulario = menos parámetros = mejor generalización.

---

- ¿Cuáles son las transformaciones que aplicarías a un texto para analizar su sentimiento?

**Respuesta para el parcial:** Convertir a minúsculas, eliminar puntuación (excepto ! y ?), eliminar URLs/menciones, tokenizar, posiblemente mantener emojis (contienen sentimiento), eliminar stopwords opcionales.

**Explicación:** Para sentimiento, "excelente!!!" tiene más fuerza que "excelente". Por eso mantenemos !. Emojis como 😊😡 son señales directas de sentimiento. Pero URLs (@usuario, http://...) son ruido. Stopwords ("el", "la") no aportan sentimiento pero ocupan espacio en la secuencia.

---

### Vocabulario

- ¿Qué es un token y cómo se relaciona con un vocabulario en NLP?

**Respuesta para el parcial:** Un token es una unidad de texto (palabra, subpalabra, o caracter). El vocabulario es el conjunto de todos los tokens únicos con sus índices numéricos asignados.

**Explicación:** "El gato come" → tokenización → ["el", "gato", "come"] → vocabulario → [2, 5, 8]. Cada palabra se convierte en un número. El vocabulario es el diccionario que define qué número corresponde a cada palabra. Sin vocabulario, no hay forma de convertir texto a números.

---

- Explica el propósito de limitar el tamaño del vocabulario (`max_vocab_size`) en datasets grandes. ¿Cuáles descartarías?

**Respuesta para el parcial:** Limitar el vocabulario reduce memoria y parámetros del embedding. Se descartan las palabras menos frecuentes (que aportan poco y podrían ser ruido/errores).

**Explicación:** `nn.Embedding(vocab_size, dim)` tiene `vocab_size × dim` parámetros. Si vocabulario=100,000 palabras y dim=300 → 30 millones de parámetros solo en embeddings. Palabras que aparecen 1-2 veces no tienen suficientes ejemplos para aprender buen embedding. Mejor descartar las menos frecuentes y mapearlas a `<unk>`.

---

- Dado el siguiente vocabulario:

```python
vocab = {"<pad>": 0, "<unk>": 1, "el": 2, "análisis": 3, "texto": 4}
```

¿Cómo se representaría la frase `"el análisis de texto"` usando este vocabulario?

**Respuesta para el parcial:** `[2, 3, 1, 4]`. "el"→2, "análisis"→3, "de"→1 (no está, es `<unk>`), "texto"→4.

**Explicación:** Proceso: "el"→buscar en vocab→2. "análisis"→buscar→3. "de"→buscar→NO ESTÁ→usar `<unk>`→1. "texto"→buscar→4. Resultado: `[2, 3, 1, 4]`. `<pad>` (índice 0) se usa para rellenar secuencias cortas.

---

### Padding y truncamiento

- Explica el propósito del padding y truncamiento en NLP.

**Respuesta para el parcial:** Las redes necesitan secuencias de longitud fija. Padding añade tokens `<pad>` a secuencias cortas. Truncamiento corta secuencias largas. Ambos permiten crear batches uniformes.

**Explicación:** Secuencias: ["hola", "mundo"] (2 tokens) y ["el", "gato", "come", "pescado"] (4 tokens). Para batch, necesitan misma longitud. Padding: añadir `<pad>` → [2, 5, 0, 0] y [3, 7, 8, 9]. Truncamiento: si max_len=3, cortar → [3, 7, 8]. Así todas las secuencias del batch tienen igual forma.

---

### Representación numérica de texto

- ¿Por qué no podemos usar directamente palabras en una red neuronal?

**Respuesta para el parcial:** Las redes neuronales solo procesan números (tensores). Las palabras son strings/símbolos discretos sin valor numérico ni relaciones matemáticas definidas.

**Explicación:** Una red hace `y = Wx + b`. Si x="gato", ¿qué es W×"gato"? No tiene sentido. Las redes solo entienden tensores de números. Necesitamos representar "gato" como vector, por ejemplo [0.2, -0.5, 0.8]. Ahí sí podemos multiplicar, sumar, etc.

---

- Explica cómo se utiliza `nn.Embedding` para mapear palabras a vectores densos.

**Respuesta para el parcial:** `nn.Embedding(vocab_size, embed_dim)` es una tabla donde cada fila es el vector de una palabra. Dado un índice, retorna su vector. Los vectores se aprenden durante el entrenamiento.

**Explicación:** Embedding es una matriz de `vocab_size × embed_dim`. Palabra "gato"=índice 5 → devuelve fila 5 de la matriz. Durante entrenamiento, backpropagation ajusta estas filas. Resultado: palabras que aparecen en contextos similares ("perro", "gato") terminan con vectores cercanos en el espacio.

---

- Dado un embedding:

```python
embedding = nn.Embedding(10, 4)
input = torch.tensor([[0, 1, 2]])
```

¿Cuál será la forma de la salida y qué representa cada dimensión?

**Respuesta para el parcial:** Forma: `(1, 3, 4)`. 1 = batch_size, 3 = longitud de secuencia (tokens), 4 = embedding_dim (dimensión del vector por token).

**Explicación:** Input `[[0, 1, 2]]` tiene forma `(1, 3)`: 1 secuencia de 3 tokens. `Embedding(10, 4)` reemplaza cada índice por vector de 4 dims. Resultado `(1, 3, 4)`: 1 secuencia × 3 tokens × 4 dimensiones por token. La forma del input + una dimensión extra para embed_dim.

---

---

## Seq2Seq

- Explica cómo funcionan el codificador (encoder) y el decodificador (decoder) en un modelo Seq2Seq. ¿Qué información pasa del primero al segundo?

**Respuesta para el parcial:** El encoder procesa la secuencia de entrada y produce un "context vector" (estado oculto final) que resume toda la información. El decoder recibe este context vector como estado inicial y genera la secuencia de salida token a token.

**Explicación:** Encoder (típicamente LSTM/GRU): lee "How are you?" token a token, actualizando su estado oculto. Al final, ese estado oculto contiene el "significado" de toda la frase. Decoder: arranca con ese estado oculto y genera "¿Cómo estás?" token a token. El context vector es el "puente" entre ambos.

---

- ¿Qué significa `Teacher Forcing` y cómo afecta al entrenamiento?

**Respuesta para el parcial:** Teacher forcing usa la salida correcta (ground truth) como entrada del siguiente paso del decoder en vez de la predicción anterior. Acelera entrenamiento pero puede causar discrepancia train/test.

**Explicación:** Sin teacher forcing: si el decoder predice mal el token 1, ese error se propaga y empeora tokens 2, 3, 4... Con teacher forcing: siempre usamos el token correcto como entrada → entrenamiento estable y rápido. Problema: en inferencia no tenemos tokens correctos, solo predicciones. El modelo no aprendió a recuperarse de errores.

---

- ¿Por qué es útil agregar un token `<SOS>` al inicio de una secuencia en el decodificador?

**Respuesta para el parcial:** `<SOS>` (Start Of Sequence) indica al decoder que comience a generar. Sin él, no sabría qué token usar como primera entrada.

**Explicación:** El decoder genera token a token: entrada → predicción. Para el PRIMER token, ¿qué entrada usamos? No hay predicción previa. `<SOS>` es el "arrancador": cuando el decoder ve `<SOS>`, sabe que debe generar el primer token real de la secuencia de salida.

---

- Durante la inferencia, ¿cómo se determina el fin de una predicción en un modelo Seq2Seq?

**Respuesta para el parcial:** El modelo genera hasta producir el token `<EOS>` (End Of Sequence) o hasta alcanzar una longitud máxima predefinida.

**Explicación:** Sin `<EOS>`, el decoder generaría infinitamente. Durante entrenamiento, las secuencias target terminan con `<EOS>`, así el modelo aprende: "después de completar la idea, predice `<EOS>`". En inferencia: cuando el modelo predice `<EOS>` → STOP. Si no lo predice, paramos en max_length para evitar loops infinitos.

---

---

## Transformers

- ¿Cuántos mecanismos de atención hay en el encoder y decoder del transformer del paper "attention is all you need"? ¿En qué se diferencian?

**Respuesta para el parcial:** Hay 3 mecanismos: 1) Self-attention en encoder (atiende a toda la entrada), 2) Masked self-attention en decoder (solo atiende a posiciones anteriores), 3) Cross-attention en decoder (atiende al output del encoder).

**Explicación:** 1) Self-attention encoder: cada palabra atiende a todas las demás de la entrada ("The cat sat" → "cat" puede ver "The" y "sat"). 2) Masked self-attention decoder: cada palabra solo atiende a las anteriores (para no hacer trampa viendo el futuro). 3) Cross-attention: el decoder atiende al output del encoder para "consultar" la entrada mientras genera.

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

**Explicación:** Analogía: buscas en biblioteca. Query = "libros de cocina". Keys = títulos de cada libro. Scores = qué tan relevante es cada libro. Softmax = convertir scores en % (suman 100%). Values = contenido de cada libro. Context = resumen ponderado: 80% del libro más relevante + 15% del segundo + 5% del tercero. División por √d_k evita que scores sean muy grandes (gradientes estables).

---

- Dado el siguiente fragmento:

```python
pos_encoding = torch.sin(position / (10000 ** (2 * (i // 2) / d_model)))
```

¿Cómo ayuda este cálculo a incorporar información posicional en un Transformer?

**Respuesta para el parcial:** Los Transformers no tienen noción inherente del orden. El positional encoding añade un vector único a cada posición usando funciones seno/coseno de diferentes frecuencias, permitiendo distinguir posiciones.

**Explicación:** Self-attention trata "El gato come" igual que "come gato El" (no tiene orden inherente). Positional encoding suma un vector único a cada posición. Usa sin/cos de diferentes frecuencias: posición 0 tiene un patrón, posición 1 otro, etc. Como cada posición tiene "firma" única, el modelo puede aprender que posición importa (sujeto antes de verbo, etc.).

---

- Explica cómo las máscaras evitan que un Transformer preste atención a posiciones no deseadas durante el entrenamiento.

**Respuesta para el parcial:** La máscara pone -∞ en los scores de posiciones prohibidas antes del softmax. El softmax convierte -∞ en 0, eliminando esa atención. En decoder, la máscara triangular impide ver tokens futuros.

**Explicación:** Matriz de scores antes de softmax. Máscara pone -∞ en posiciones prohibidas. Softmax(-∞) = 0 → esa posición no contribuye nada. En decoder, para predecir palabra 3, solo puede ver palabras 1, 2 (no 4, 5, 6). La máscara es triangular: fila 1 ve solo col 1, fila 2 ve cols 1-2, fila 3 ve cols 1-3, etc. Así el modelo no hace "trampa" viendo el futuro.

---
