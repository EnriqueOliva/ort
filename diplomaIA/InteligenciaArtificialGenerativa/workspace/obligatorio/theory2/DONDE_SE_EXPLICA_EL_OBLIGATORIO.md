# Dónde se Explica el Obligatorio - Resumen

## 📋 Documento Oficial del Obligatorio

**Ubicación**: `theory/obligatorio/Obligatorio IA Generativa 2025.docx.txt`

### Información Clave:

- **Fecha de entrega**: 8/12/2025 hasta las 21:00 horas
- **Formato**: Grupos de hasta 3 personas
- **Puntaje**: Máximo 40 puntos, mínimo 1 punto

### Tema del Obligatorio:

El objetivo es **implementar una técnica de IAG de su interés**.

### Temas Posibles (lista no exhaustiva):
- Image captioning
- Uso de LLMs
- **Variantes de GANs (ej: Conditional GANs)** ← Tu tema entra acá
- Variantes de VAEs
- Audio generation
- Otros (a validar con docentes)

### Ejes Centrales:
1. Comprender una técnica nueva no presentada por los docentes
2. Desarrollar un prototipo funcional en un caso acotado

### Entregables:
- **11/11 y 18/11**: Talleres expositivos (10 minutos máximo)
  - Presentación del tema
  - Introducción teórica
  - Justificación del interés frente a compañeros
- **8/12**: Entrega final (informe + código prototipo)

---

## 📚 Clases Relevantes del Curso

### 1. **Clase del 7 de Octubre (7-07-10-2025)** - GANs Básicas

**Ubicación**: `theory/7-07-10-2025/7-07-10-2025.txt`

**Contenido**:
- Introducción a la teoría detrás de las GANs
- Funcionamiento del modelo básico
- Práctico de GANs disponibilizado
- Explicación de:
  - El Generador (G)
  - El Discriminador (D)
  - La función de pérdida adversarial
  - El equilibrio de Nash
  - Training loop (alternar entrenamiento D y G)

**Frases clave de la clase**:
> "La clase de hoy vamos a trabajar las GANs, vamos a dar una introducción lo que es la teoría detrás de ellas, explicar un poco el funcionamiento de este modelo y también le vamos a disponibilizar el práctico de GANs"

**Relevancia para tu obligatorio**:
- Base teórica de las GANs estándar
- Fundamentos que WGAN y WGAN-GP mejoran
- Comprensión del problema del equilibrio de Nash que WGAN soluciona

---

### 2. **Clase del 30 de Septiembre (6-30-09-2025)** - VAEs (Variational Autoencoders)

**Ubicación**: `theory/6-30-09-2025/explicaciones.md`

**Contenido**:
- Explicación detallada de Variational Autoencoders
- Variables latentes
- Reparametrization trick
- Función de pérdida (reconstrucción + KL divergence)
- Diferencias con autoencoders básicos

**Relevancia para tu obligatorio**:
- Aunque tu tema es WGAN, los VAEs son otro modelo generativo importante del curso
- Comprender diferentes enfoques para modelos generativos
- Contexto del "zoológico de modelos generativos" mencionado por el profesor

---

### 3. **Clase del 16 de Septiembre (5-16-09-2025)** - Introducción a GANs

**Ubicación**: Múltiples archivos en `theory/5-16-09-2025/`
- `explicaciones.md`
- `version_agente1.md`
- `version_agente2.md`
- `version_agente3.md`

**Contenido**:
- Menciones tempranas de GANs
- Contexto previo a la clase principal del 7 de octubre

---

### 4. **Clase del 4 de Noviembre (11-04-11-2025)** - Métricas de Evaluación

**Ubicación**: `theory/11-04-11-2025/11-04-11-2025.txt`

**Contenido**:
- Métricas para evaluar modelos generativos
- FID (Fréchet Inception Distance)
- Inception Score
- Métricas para evaluar GANs

**Relevancia para tu obligatorio**:
- Cómo evaluar la calidad de las imágenes generadas
- Métricas que podrías incluir en tu informe
- Comparación cuantitativa entre WGAN y WGAN-GP

---

### 5. **Clase del 11 de Noviembre (primer taller)** - Presentaciones de Obligatorios

**Nota**: Esta fue una de las fechas de talleres expositivos donde los estudiantes presentaron sus temas.

---

### 6. **Clase del 18 de Noviembre (segundo taller)** - Presentaciones de Obligatorios

**Ubicación**: `theory/12-11-11-2025/12-11-11-2025.txt` (parece estar fechada incorrectamente)

**Contenido**:
- Presentaciones de alumnos sobre sus obligatorios
- Menciones de diferentes implementaciones
- Discusiones sobre proyectos

---

## 🎯 Tu Tema Específico: WGAN-GP vs WGAN

### ¿Dónde se menciona WGAN/WGAN-GP?

**Solo en**: `theory/obligatorio/OBLIGATORIO-COMPLETO-II.md`

Esto significa que:
- **WGAN y WGAN-GP NO fueron explicados en clase**
- Son temas que debías investigar por tu cuenta (cumpliendo con el eje 1: "Comprender una técnica nueva no presentada por los docentes")
- Tu implementación demuestra investigación independiente

### Papers de Referencia (mencionados en tu notebook):

1. **WGAN Paper** (Arjovsky et al., 2017)
   - "Wasserstein GAN"
   - arXiv:1701.07875

2. **WGAN-GP Paper** (Gulrajani et al., 2017)
   - "Improved Training of Wasserstein GANs"
   - arXiv:1704.00028

---

## 📊 Tu Implementación en Contexto

### Lo que viste en clase:
- **GANs básicas** (7 de octubre)
  - Concepto de adversarial training
  - Generador vs Discriminador
  - Problemas de convergencia y mode collapse

### Lo que investigaste e implementaste:
- **WGAN** (Wasserstein GAN)
  - Usa Wasserstein distance en lugar de JS divergence
  - Weight clipping para enforcar Lipschitz constraint
  - Más estable que GAN básica

- **WGAN-GP** (Wasserstein GAN with Gradient Penalty)
  - Mejora sobre WGAN
  - Reemplaza weight clipping con gradient penalty
  - Evita problemas de capacidad reducida del modelo

### Validaciones que hiciste:

✅ **Experimento 1**: Comparación básica de convergencia
✅ **Experimento 3**: Estabilidad de gradientes (715x más estable en WGAN-GP)
✅ **Experimento 4**: Sensibilidad a hiperparámetros (WGAN-GP más robusto)
✅ **Experimento 5**: Distribución de pesos (WGAN saturado en ±0.01, WGAN-GP natural)

---

## 🗂️ Archivos Complementarios en la Carpeta Obligatorio

### `theory/obligatorio/`

1. **`OBLIGATORIO-COMPLETO.md`**
   - Explicación completa del obligatorio

2. **`OBLIGATORIO-COMPLETO-II.md`**
   - Versión extendida con más detalles
   - Menciona WGAN-GP específicamente

3. **`info.txt`**
   - Información adicional

---

## 💡 Resumen Ejecutivo

### Para entender el contexto de tu obligatorio, lee:

1. **Primero**: `theory/obligatorio/Obligatorio IA Generativa 2025.docx.txt`
   - Para entender los requisitos formales

2. **Segundo**: `theory/7-07-10-2025/7-07-10-2025.txt`
   - Para entender la base teórica de GANs

3. **Tercero**: Papers de WGAN y WGAN-GP
   - Para entender las mejoras específicas que implementaste

4. **Cuarto**: Tu propio notebook
   - `workspace/obligatorio/WGAN_GP_vs_WGAN_Comparison.ipynb`
   - Que valida experimentalmente las afirmaciones de los papers

### Documentación que creé para ayudarte:

1. **`EXPLICACION_NOTEBOOK.md`**
   - Explicación paso a paso de tu notebook
   - Con analogías simples para cada concepto

2. **`ANALISIS_CELDA_POR_CELDA.md`**
   - Análisis técnico detallado
   - Resultados de cada experimento
   - Validación de las hipótesis

3. **Este archivo** (`DONDE_SE_EXPLICA_EL_OBLIGATORIO.md`)
   - Mapa de dónde encontrar cada concepto en las clases

---

## 🎓 Conclusión

**El obligatorio NO se explicó en una clase específica** porque:
- El propósito es que investigues un tema nuevo por tu cuenta
- Las GANs básicas (base teórica) sí se explicaron el 7 de octubre
- WGAN y WGAN-GP son extensiones que debías investigar usando los papers

**Tu implementación cumple perfectamente** con los objetivos:
1. ✅ Comprendes una técnica nueva (WGAN-GP)
2. ✅ Tienes un prototipo funcional
3. ✅ Validaste experimentalmente las afirmaciones del paper

**Estado de tu proyecto**:
- Solo entrenaste 1 época (para pruebas rápidas)
- Todos los experimentos funcionan correctamente
- Validaste las 4 afirmaciones principales del paper WGAN-GP
- Para la entrega final, considera entrenar 50-100 épocas para mejores imágenes

---

**Fecha de creación de este documento**: 18/11/2025
**Última actualización**: 18/11/2025