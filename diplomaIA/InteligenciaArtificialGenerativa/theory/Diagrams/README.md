# Diagramas Interactivos - IA Generativa

Este directorio contiene diagramas HTML interactivos de los modelos y arquitecturas de deep learning enseñados en el curso de Inteligencia Artificial Generativa.

## 📂 Estructura de Archivos

```
Diagrams/
├── index.html                          # Página principal de navegación
├── 7-07-10-2025/                       # Clase 7: GANs
│   ├── gan_arquitectura_general.html   # Arquitectura completa del sistema GAN
│   ├── gan_funcion_perdida.html        # Funciones de pérdida y optimización
│   ├── gan_entrenamiento_alternado.html # Proceso de entrenamiento animado
│   └── dcgan_arquitectura.html         # Deep Convolutional GAN
└── 8-14-10-2025/                       # Clase 8: Administrativa
    └── clase_administrativa.html       # Información sobre el obligatorio
```

## 🎯 Cómo usar los diagramas

1. **Abre `index.html`** en tu navegador para ver el índice de todos los diagramas
2. Haz clic en cualquier tarjeta para acceder al diagrama específico
3. Los diagramas interactivos tienen elementos clickeables que muestran explicaciones
4. Los diagramas animados incluyen controles (▶️ Iniciar, ⏸️ Pausar, 🔄 Reiniciar)

## 📚 Contenido por Clase

### Clase 7: GANs (7 de Octubre 2025)

#### 1. **gan_arquitectura_general.html**
- Esquema visual completo del sistema GAN
- Componentes: Generador (G), Discriminador (D), Ruido (Z)
- Flujo de datos: reales vs generados
- Explicaciones interactivas al hacer clic en cada componente

#### 2. **gan_funcion_perdida.html**
- Función minimax: min_G max_D V(D,G)
- Pérdida del Discriminador (BCE con datos reales y falsos)
- Pérdida del Generador (versión teórica vs versión práctica)
- Gráficos interactivos de log(D(x)) y log(1-D(x))
- Algoritmo de entrenamiento paso a paso

#### 3. **gan_entrenamiento_alternado.html**
- Animación del proceso de entrenamiento
- Alternancia entre entrenar D y entrenar G
- Visualización de congelamiento de pesos
- Ejemplos de código en PyTorch
- Timeline interactiva del proceso

#### 4. **dcgan_arquitectura.html**
- Arquitectura del Generador con convoluciones transpuestas
- Arquitectura del Discriminador con convoluciones
- Flujo de dimensiones detallado
- Comparación GAN vs DC-GAN
- Guías de diseño y mejores prácticas
- Ejemplos de código completos

### Clase 8: Información Administrativa (14 de Octubre 2025)

#### **clase_administrativa.html**
- Esta clase no tuvo contenido técnico
- Información sobre el trabajo obligatorio
- Fechas de entrega y presentaciones
- Recomendaciones para el proyecto

## 🎨 Características de los Diagramas

- **Diseño responsive**: Se adaptan a diferentes tamaños de pantalla
- **Interactividad**: Hover effects, elementos clickeables, animaciones
- **Código incluido**: Ejemplos de implementación en PyTorch
- **Explicaciones detalladas**: Cada componente tiene su explicación
- **Visualizaciones**: SVG, Canvas, CSS animations
- **Autocontenidos**: Cada HTML funciona de manera independiente

## 🔍 Temas Cubiertos

### GANs (Generative Adversarial Networks)
- ✅ Concepto del juego adversario
- ✅ Arquitectura Generador-Discriminador
- ✅ Función de pérdida minimax
- ✅ Entrenamiento alternado
- ✅ Binary Cross-Entropy Loss
- ✅ Problemas comunes (Mode Collapse, vanishing gradients)

### DC-GANs (Deep Convolutional GANs)
- ✅ Convoluciones transpuestas
- ✅ Batch Normalization
- ✅ Funciones de activación (ReLU, LeakyReLU, Tanh, Sigmoid)
- ✅ Arquitectura sin pooling
- ✅ Guías de diseño específicas
- ✅ Hiperparámetros recomendados

## 💡 Para estudiantes de otras disciplinas

Los diagramas están diseñados para ser comprensibles incluso si no tienes experiencia previa en deep learning:

- **Explicaciones desde lo básico**: Cada concepto se explica desde cero
- **Analogías**: Se usan metáforas (falsificador vs detective) para facilitar la comprensión
- **Ejemplos concretos**: Dimensiones específicas (28×28, vector de 100, etc.)
- **Visualización**: Los diagramas muestran gráficamente lo que las fórmulas describen
- **Paso a paso**: El proceso de entrenamiento se desglosa en pasos claros

## 🛠️ Tecnologías Utilizadas

- HTML5
- CSS3 (Flexbox, Grid, Animations, Gradients)
- JavaScript (Vanilla JS, Canvas API)
- SVG para diagramas vectoriales

## 📝 Notas

- Los archivos son totalmente autocontenidos (no requieren conexión a internet)
- Compatibles con navegadores modernos (Chrome, Firefox, Edge, Safari)
- Los colores y estilos son consistentes en todos los diagramas
- Se puede imprimir a PDF si se necesita una versión estática

## 🎓 Contexto Académico

Estos diagramas fueron creados basándose en:
- Transcripciones de las clases del curso
- Paper original de GANs (Goodfellow et al., 2014)
- Paper de DC-GAN (Radford et al., 2015)
- Implementaciones prácticas en PyTorch

---

**Curso**: Inteligencia Artificial Generativa
**Semestre**: 2do Semestre 2025
**Fecha de creación**: 9 de Diciembre 2025
