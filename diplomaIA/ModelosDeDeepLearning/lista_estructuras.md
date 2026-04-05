# Lista de Arquitecturas y Estructuras
## Clases 8, 9, 10, 11 (27-Oct al 17-Nov 2025)

---

## CLASE 8 (27-Oct): Redes Residuales y Word Embeddings

| # | Estructura | Tipo | Descripcion |
|---|------------|------|-------------|
| 1 | **ResNet** | CNN | Skip connections con SUMA: H(x) = F(x) + x |
| 2 | **DenseNet** | CNN | Skip connections con CONCATENACION |
| 3 | **Word2Vec** | Embedding | Vectores de palabras (CBOW y Skip-gram) |

---

## CLASE 9 (03-Nov): Redes Recurrentes

| # | Estructura | Tipo | Descripcion |
|---|------------|------|-------------|
| 4 | **RNN Vanilla** | Secuencial | Ht = tanh(U*Xt + V*Ht-1) |
| 5 | **LSTM** | Secuencial | 4 compuertas + Cell State + Hidden State |
| 6 | **GRU** | Secuencial | 2 compuertas (Reset + Update), solo Hidden |
| 7 | **Bidirectional RNN** | Secuencial | Procesa en ambas direcciones |
| 8 | **Stacked RNN** | Secuencial | Multiples capas RNN apiladas |

---

## CLASE 10 (10-Nov): Encoder-Decoder

| # | Estructura | Tipo | Descripcion |
|---|------------|------|-------------|
| 9 | **Encoder-Decoder** | Seq2Seq | Encoder comprime, Decoder genera |
| 10 | **Teacher Forcing** | Tecnica | Usa palabra correcta en entrenamiento |

---

## CLASE 11 (17-Nov): Attention y Transformers

| # | Estructura | Tipo | Descripcion |
|---|------------|------|-------------|
| 11 | **Attention (Bahdanau)** | Mecanismo | Contexto dinamico: Ci = SUM(alpha_ij * Hj) |
| 12 | **Self-Attention** | Mecanismo | Cada palabra mira a todas las demas |
| 13 | **Multi-Head Attention** | Mecanismo | Multiples heads en paralelo |
| 14 | **Positional Encoding** | Componente | Agrega info de posicion con senos/cosenos |
| 15 | **Transformer** | Arquitectura | Encoder-Decoder con solo Attention |
| 16 | **Feed-Forward Network** | Componente | Linear->ReLU->Linear en cada posicion |

---

## Resumen por Categoria

### Componentes de Bloques
- Skip Connection (ResNet)
- Dense Connection (DenseNet)
- Gates (LSTM: Forget, Input, Output; GRU: Reset, Update)
- Attention Weights
- Residual Connection (Add & Norm)

### Funciones de Activacion
- tanh (RNN, LSTM, GRU, Attention)
- sigmoid (Gates de LSTM/GRU)
- ReLU (ResNet, Feed-Forward)
- Softmax (Clasificacion, Attention)

### Tecnicas de Normalizacion
- Batch Normalization (ResNet)
- Layer Normalization (Transformer)

---

## Formulas Clave (Para Parcial)

```
ResNet:     H(x) = F(x) + x

RNN:        Ht = tanh(U*Xt + V*Ht-1)

LSTM:       Ct = ft*Ct-1 + it*Ct_tilde
            Ht = ot * tanh(Ct)

GRU:        Ht = (1-zt)*Ht_tilde + zt*Ht-1

Attention:  Ci = SUM(alpha_ij * Hj)
            alpha_ij = softmax(score(Si-1, Hj))

Self-Att:   Attention(Q,K,V) = softmax(Q*K^T/sqrt(dk)) * V
```

---

## Archivos Generados

1. `arquitecturas_visuales.md` - Diagramas ASCII detallados
2. `visualizaciones_interactivas.html` - Visualizaciones interactivas
3. `lista_estructuras.md` - Este archivo
