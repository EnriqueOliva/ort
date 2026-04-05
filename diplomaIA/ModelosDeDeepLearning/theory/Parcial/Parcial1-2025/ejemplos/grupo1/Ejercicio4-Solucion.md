# Ejercicio 4 - CNNs: Convolución, Pooling y Skip Connections

## 1. Diferencia entre convolución y pooling. ¿CNN = solo Conv + Pooling?

### Convolución vs Pooling

**CONVOLUCIÓN:**
- Aplica un filtro (3×3) sobre ventanas de la imagen
- Multiplica elemento por elemento y suma
- **DETECTA PATRONES:** bordes, texturas, formas
- Tiene **parámetros entrenables** (pesos del filtro)

```
Ventana 3×3  ×  Filtro 3×3  =  1 número
[0 0 1]         [1 2 1]
[0 0 8]    ×    [2 1 4]     =  0×1 + 0×2 + 1×1 + ... = 47
[0 1 2]         [2 2 2]
```

**POOLING:**
- Divide feature map en ventanas (2×2)
- Toma el **MÁXIMO** de cada ventana
- **REDUCE DIMENSIONES** a la mitad
- **NO** tiene parámetros entrenables

```
ANTES (4×4):       DESPUÉS (2×2):
┌──────┬──────┐    ┌────┬────┐
│ 1  2 │ 5  6 │    │ 8  │ 6  │
│ 3  8 │ 2  4 │ →  └────┴────┘
├──────┼──────┤    │ 9  │ 7  │
│ 9  1 │ 6  7 │    └────┴────┘
└──────┴──────┘
```

| Aspecto | Convolución | Pooling |
|---------|-------------|---------|
| **Función** | Detectar patrones | Reducir tamaño |
| **Parámetros** | SÍ (filtros) | NO |
| **Dimensiones** | Mantiene (con padding) | Reduce a la mitad |

---

### ¿CNN = solo Conv + Pooling?

**NO.** Una CNN completa incluye:

```
INPUT (32×32×3)
   ↓
BLOQUES CONVOLUCIONALES:
   Conv2D(32 filtros) → ReLU → MaxPool  ← Detecta bordes
   Conv2D(64 filtros) → ReLU → MaxPool  ← Detecta texturas
   Conv2D(128 filtros) → ReLU → MaxPool ← Detecta objetos
   ↓
CLASIFICACIÓN:
   Flatten                              ← (4×4×128) → (2048)
   Dense(512) → ReLU                    ← MLP
   Dense(5) → Softmax                   ← 5 clases
```

**Componentes:**
1. Capas **Conv2D** (detectar features)
2. Capas **MaxPool** (reducir dimensiones)
3. Capa **Flatten** (3D → 1D)
4. Capas **Dense** (clasificar)
5. Funciones de activación (**ReLU**, **Softmax**)

**Fuente:** CONCEPTOS-CNN-EXPLICADOS.md

---

## 2. ¿Se puede procesar imágenes sin Conv/Pooling?

**Respuesta: SÍ, técnicamente posible. Pero NO recomendado.**

### Alternativa: Solo capas Dense

```
Imagen (32×32×3) = 3,072 números
        ↓
     Flatten
        ↓
   [3072 números en fila]
        ↓
   Dense(512) → Dense(10)
```

### Problemas de usar solo Dense:

**1. Pérdida de información espacial:**
- Un MLP trata todos los píxeles igual sin importar su posición
- Si mezclas los píxeles aleatoriamente → **mismo output**
- No sabe qué píxeles son vecinos (información crítica en imágenes)

**2. Número astronómico de parámetros:**

Para imagen 1024×1024×3:
```
Dense(1024×1024×3 → 512):
Parámetros = 1024 × 1024 × 3 × 512 ≈ 1.6 BILLONES

Conv(3×3×3 → 32 filtros):
Parámetros = 3 × 3 × 3 × 32 = 864  ← 1 millón de veces menos
```

### Por qué CNNs son superiores:

**1. LOCALITY (Localidad):**
- Conecta solo píxeles vecinos (ventana 3×3)
- Reduce parámetros exponencialmente

**2. WEIGHT SHARING:**
- Usa el MISMO filtro en toda la imagen
- Un "círculo" arriba se detecta igual que abajo

**Resultado:** CNNs usan **100-300× menos parámetros** que redes Dense y funcionan **mejor** en imágenes.

**Fuente:** Clase 5-29-09-2025

---

## 3. Skip connections: ¿Qué son y para qué sirven?

### ¿Qué son?

Conexiones que **saltan** capas, sumando la entrada directamente a la salida.

```
Input x
  ↓
[Conv → ReLU → Conv] ← Bloque de procesamiento
  ↓
Output = Bloque_output + x  ← Skip: se suma x original
  ↓
ReLU
```

### Utilidad

**1. Resolver el problema de Vanishing Gradients:**

**Sin skip connections:**
```
Gradiente = ∂L/∂w₁ × ∂w₁/∂w₂ × ... × ∂w₁₉/∂w₂₀
            ↑ Cada término < 1 → producto tiende a 0

En capa 20: gradiente ≈ 0 → pesos NO se actualizan
```

**Con skip connections:**
```
Gradiente tiene un camino DIRECTO:
∂L/∂w = ∂L/∂output × (1 + ∂capas/∂w)
                      ↑ "+1" evita que tienda a 0
```

**2. Permitir redes MUY profundas:**
- Sin skips: redes >20 capas no entrenan bien
- Con skips: redes de 50, 100, 152 capas (ResNet)

**3. Efecto de regularización:**
- Suavizan el landscape de la loss function
- Entrenan más rápido y estable

### Conexión con ResNet

**ResNet = Residual Network** (red residual)

Filosofía: En lugar de aprender H(x), aprende el **residual** r(x) = H(x) - x

```
Output = x + r(x) = x + H(x) - x = H(x)

La red aprende la DIFERENCIA, no la transformación absoluta
→ Más fácil de optimizar
```

**Ejemplo:**
```
Sin skip: Aprender f(x) = 10x  (absoluto)
Con skip: Aprender r(x) = 9x, entonces f(x) = x + 9x = 10x  (diferencia)
```

**Fuente:** Clase 7-13-10-2025

---

## Resumen

| Concepto | Qué hace | Para qué sirve |
|----------|----------|----------------|
| **Conv** | Detecta patrones con filtros | Extraer features |
| **Pooling** | Toma máximo de ventanas | Reducir dimensiones 50% |
| **Dense sin Conv** | Posible pero ineficiente | Pierde info espacial, billones de parámetros |
| **Skip connections** | Suma entrada a salida | Evitar vanishing gradients, redes profundas |
