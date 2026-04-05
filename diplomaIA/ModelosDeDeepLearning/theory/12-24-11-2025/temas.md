# Temas de la Clase 12 - 24 de Noviembre de 2025

## NOTA IMPORTANTE
Esta clase es un **REPASO PARA EL PARCIAL**. El profesor revisó temas de clases anteriores y resolvió ejercicios tipo examen.

---

## 1. TRANSFORMERS (Tema Principal)

### 1.1 Arquitectura General
- Arquitectura Encoder-Decoder
- Bloques de Encoder (aplicados N veces)
- Bloques de Decoder (aplicados N veces)
- Diferencia fundamental con RNN: procesamiento paralelo vs secuencial

### 1.2 Componentes del Encoder
- Multi-head Self-Attention
- Skip Connections (conexiones residuales)
- Layer Normalization
- Feed-Forward Network (MLP de dos capas)
- Positional Encoding

### 1.3 Componentes del Decoder
- Multi-head Self-Attention con Máscara (Masked Attention)
- Multi-head Cross-Attention (Encoder-Decoder Attention)
- Skip Connections
- Layer Normalization
- Feed-Forward Network
- Capa Lineal Final + Softmax

### 1.4 Mecanismo de Attention
- Self-Attention: "todos contra todos"
- Cross-Attention: queries del decoder, keys/values del encoder
- Matrices Q, K, V (Query, Key, Value)
- Matrices de peso WQ, WK, WV, WO
- Fórmula: softmax(Q·K^T / √dk) · V

### 1.5 Multi-head Attention
- Múltiples cabezas en paralelo
- Concatenación de salidas
- Cada cabeza captura diferentes relaciones

### 1.6 Masked Attention (Máscara en Decoder)
- Data leakage temporal
- Máscara triangular inferior
- Por qué se necesita durante entrenamiento

### 1.7 Positional Encoding
- Por qué se necesita (invariancia a permutaciones)
- Cómo se suma a los embeddings

### 1.8 Training vs Inference
- Diferencias en el flujo de datos
- Loop en decoder solo en inference
- Teacher forcing

### 1.9 Embeddings
- Input Embedding (vocabulario fuente → D_model)
- Output Embedding (vocabulario destino → D_model)

---

## 2. CÁLCULO DE PARÁMETROS DE TRANSFORMER

### 2.1 Ejercicio Práctico Completo
- Hiperparámetros: vocab_source=5000, vocab_target=6000, D_model=128, H=4, D_FF=512
- Cálculo de parámetros en Multi-head Attention
- Cálculo de parámetros en Layer Normalization
- Cálculo de parámetros en Feed-Forward
- Cálculo de parámetros en Embeddings
- Cálculo de parámetros en Capa Lineal Final
- **Total: ~3.1 millones de parámetros**

---

## 3. COMPARACIÓN TRANSFORMER VS RNN

### 3.1 Diferencias Principales
- Recurrencia vs no-recurrencia
- Procesamiento secuencial vs paralelo
- Hidden state vs Attention
- Memoria a largo plazo

### 3.2 Seq2Seq con RNN
- Encoder-Decoder recurrente
- Hidden state como contexto
- Teacher forcing en entrenamiento

---

## 4. RESNETS Y SKIP CONNECTIONS

### 4.1 Problema de Degradación
- Redes más profundas entrenan peor
- No es overfitting (pasa en train también)
- Problema de optimización, no de capacidad

### 4.2 Vanishing Gradient
- Gradientes que desaparecen
- Por qué ocurre en redes profundas

### 4.3 Exploding Gradient
- Gradientes que explotan
- Más fácil de controlar

### 4.4 Skip Connections como Solución
- Fórmula: H(x) = F(x) + x
- La derivada siempre tiene un "+1"
- No agregan parámetros extra

---

## 5. BACKPROPAGATION THROUGH TIME (BPTT)

### 5.1 Concepto
- Desplegar la red recurrente
- Hacer backpropagation normal
- Evitar vanishing/exploding gradient

### 5.2 Matriz B Nula
- Si B=0, la RNN se convierte en MLP

---

## 6. LANGUAGE MODELS

### 6.1 Definición
- Predecir la siguiente palabra

### 6.2 Arquitecturas
- Con MLP (ventana fija)
- Con RNN (cualquier longitud)
- Con Transformer

### 6.3 Construcción de Datos
- N-gramas
- Ventana deslizante
- Bigramas, trigramas

---

## 7. WORD2VEC

### 7.1 Ejercicio Mencionado
- Construcción de datos de entrenamiento
- Pares entrada-salida

---

## 8. TOKENS ESPECIALES

### 8.1 Beginning of Sequence (BOS)
- Solo en Decoder
- Necesario para iniciar generación

### 8.2 End of Sequence (EOS)
- Marca fin de secuencia
- Decoder genera hasta encontrarlo

---

## 9. MAPAS DE ATENCIÓN

### 9.1 Interpretación
- Cómo leer las filas
- Qué significa atención alta/media/baja

### 9.2 Ejemplo con Traducción
- Tabla español-inglés
- Completar cualitativamente

---

## 10. PREGUNTAS TIPO PARCIAL REVISADAS

### 10.1 Temas Cubiertos
- Explicar arquitectura Transformer
- Pseudocódigo Seq2Seq
- Beneficios Encoder-Decoder
- Comparación Transformer vs RNN
- Papel de máscaras
- Cálculo de attention
- Positional encoding
- Costo computacional
- ResNets y degradación
- Language models

### 10.2 Consejos del Profesor
- Usar guía de estudio
- Forzarse a calcular parámetros
- Mirar ejercicios del año pasado

---

## 11. INFORMACIÓN ADMINISTRATIVA

### 11.1 Parcial
- Incluye defensa + preguntas escritas
- 2-3 preguntas aproximadamente

### 11.2 Entregas
- Taller 1 y Taller 2
- Competencias Kaggle (puntos extra)

### 11.3 Temas NO Vistos (NO entran)
- Zero-Shot Learning
- Transfer Learning
- Modelo CLIP

---

## RESUMEN: TEMAS PRINCIPALES PARA EL PARCIAL

1. **Transformers** - Arquitectura completa, cálculo de parámetros
2. **Attention** - Self-attention, cross-attention, máscaras
3. **RNN/LSTM** - Comparación con Transformers, BPTT
4. **ResNets** - Skip connections, vanishing gradient
5. **Language Models** - Construcción de datos, n-gramas
6. **Seq2Seq** - Encoder-decoder, teacher forcing
