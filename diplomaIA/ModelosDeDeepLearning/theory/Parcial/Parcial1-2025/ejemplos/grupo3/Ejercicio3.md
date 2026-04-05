# Ejercicio 3 - Document Term Matrix

## 1. ¿Sobre qué conjunto se define?

**Sobre el CORPUS (conjunto de documentos)**

La DTM se construye analizando:
- Filas = cada documento del corpus
- Columnas = vocabulario extraído del corpus completo

**Ejemplo:** Si tienes 100 emails → DTM de 100 filas

---

## 2. Document Term Matrix para 5 términos

**Vocabulario seleccionado:** {fox, dog, lazy, the, computer}

**Paso 1: Contar frecuencias**

```
Doc 0: "The big brown fox jumps over the lazy dog"
  the: 2, fox: 1, dog: 1, lazy: 1, computer: 0

Doc 1: "In computer programming, lazy initialization..."
  the: 2, fox: 0, dog: 0, lazy: 1, computer: 1

Doc 2: "By far the most common and widespread species of fox is the red fox"
  the: 2, fox: 2, dog: 0, lazy: 0, computer: 0

Doc 3: "The domestic dog is a member of the genus Canis..."
  the: 2, fox: 0, dog: 1, lazy: 0, computer: 0
```

**DTM (frecuencias):**

|     | the | fox | dog | lazy | computer |
|-----|-----|-----|-----|------|----------|
| 0   | 2   | 1   | 1   | 1    | 0        |
| 1   | 2   | 0   | 0   | 1    | 1        |
| 2   | 2   | 2   | 0   | 0    | 0        |
| 3   | 2   | 0   | 1   | 0    | 0        |

---

## 3. Diferencia con Embeddings

### Document Term Matrix (DTM)

**Representación:**
- Matriz sparse (filas=docs, cols=palabras)
- Valores = frecuencias
- Dimensión = tamaño vocabulario (miles)

**Características:**
```
"fox" → [0, 1, 0, 0, 0, ..., 0]  (10,000 dimensiones, 99.99% ceros)
"dog" → [0, 0, 1, 0, 0, ..., 0]

Distancia("fox", "dog") = √2  (ortogonales, no captura similitud)
```

**Problemas:**
- Alta dimensionalidad
- Sparse (99%+ ceros)
- NO captura semántica
- Palabras similares = vectores ortogonales

---

### Embeddings

**Representación:**
- Vectores densos continuos
- Dimensión = fija (100-300)
- Aprendidos de contexto

**Características:**
```
"fox" → [0.23, -0.45, 0.67, ..., 0.12]  (300 dimensiones, todos útiles)
"dog" → [0.25, -0.43, 0.71, ..., 0.15]

Distancia("fox", "dog") = 0.15  (cercanos, ambos animales)
```

**Ventajas:**
- Baja dimensionalidad (300 vs 10,000)
- Dense (todos valores significativos)
- Captura semántica (similitud real)
- Relaciones geométricas (rey-hombre+mujer≈reina)

---

### Comparación directa

| Aspecto | DTM | Embeddings |
|---------|-----|------------|
| **Dimensiones** | 10,000+ | 100-300 |
| **Sparse** | SÍ (99%) | NO (denso) |
| **Semántica** | NO | SÍ |
| **Memoria** | 10 GB | 60 MB |
| **Similitud** | Ortogonal | Distancia útil |

**Fuente:** Clases 1 y CONCEPTOS-AVANZADOS.md
