╔══════════════════════════════════════════════════════════════════════════════╗
║          EVOLUCIÓN DE MODELOS DE LENGUAJE (separado por TIPOS)               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  ENFOQUES/CAPAS para predecir la siguiente palabra:                    │  ║
║  │  ──────────────────────────────────────────────────                    │  ║
║  │                                                                        │  ║
║  │  1. N-GRAMAS (conteo de frecuencias)                                   │  ║
║  │     └─ Problema: combinatoria, datos esparsos                          │  ║
║  │                   │                                                    │  ║
║  │                   ▼                                                    │  ║
║  │  2. MLP + EMBEDDINGS (redes neuronales)                                │  ║
║  │     └─ Resuelve: combinatoria gracias a embeddings                     │  ║
║  │     └─ Problema: ventana fija                                          │  ║
║  │                   │                                                    │  ║
║  │                   ▼                                                    │  ║
║  │  3. RNN (recurrentes)                                                  │  ║
║  │     └─ Resuelve: cualquier largo, comparte pesos                       │  ║
║  │     └─ Problema: vanishing gradient, memoria limitada                  │  ║
║  │                   │                                                    │  ║
║  │                   ▼                                                    │  ║
║  │  4. LSTM / GRU (capas con compuertas)                                  │  ║
║  │     └─ Resuelve: memoria a largo plazo                                 │  ║
║  │     └─ Problema: solo genera mismo largo que entrada                   │  ║
║  │                   │                                                    │  ║
║  │                   │ ← Estas CAPAS se usan DENTRO de arquitecturas      │  ║
║  │                   ▼                                                    │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  PATRÓN de diseño:                                                     │  ║
║  │  ─────────────────                                                     │  ║
║  │                                                                        │  ║
║  │  5. ENCODER-DECODER (patrón, NO arquitectura)                          │  ║
║  │     └─ Idea: comprimir entrada en vector → generar salida              │  ║
║  │     └─ Resuelve: diferentes longitudes entrada/salida                  │  ║
║  │     └─ Problema: cuello de botella en el contexto único                │  ║
║  │                   │                                                    │  ║
║  │                   │ ← Este PATRÓN se implementa con arquitecturas      │  ║
║  │                   ▼                                                    │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐  ║
║  │  ARQUITECTURAS que implementan el patrón Encoder-Decoder:              │  ║
║  │  ────────────────────────────────────────────────────────              │  ║
║  │                                                                        │  ║
║  │  6. SEQ2SEQ (arquitectura con LSTM/GRU + Teacher Forcing)              │  ║
║  │     └─ Implementa: Encoder-Decoder usando RNN/LSTM/GRU como capas      │  ║
║  │     └─ Permite: traducción, resumen, captioning                        │  ║
║  │     └─ Problema: cuello de botella, no paraleliza                      │  ║
║  │                   │                                                    │  ║
║  │                   │ + Mejora: Bahdanau Attention (clase 11)            │  ║
║  │                   ▼                                                    │  ║
║  │                                                                        │  ║
║  │  7. TRANSFORMER (arquitectura con Self-Attention)                      │  ║
║  │     └─ Implementa: Encoder-Decoder usando Attention como capas         │  ║
║  │     └─ Resuelve: cuello de botella + paralelización masiva             │  ║
║  │     └─ Es la base de: GPT, BERT, ChatGPT (clases 11-12)                │  ║
║  │                                                                        │  ║
║  └────────────────────────────────────────────────────────────────────────┘  ║
║                                                                              ║
║  CLAVE: LSTM/GRU no se "reemplazan" por Seq2Seq.                             ║
║         LSTM/GRU son capas que se USAN DENTRO de Seq2Seq.                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝