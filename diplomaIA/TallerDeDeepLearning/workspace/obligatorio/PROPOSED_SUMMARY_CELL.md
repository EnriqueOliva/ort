# Proposed Summary Cell Update

## Code to Replace Current Summary Cell

```python
print("=" * 60)
print("RESUMEN FINAL DEL MODELO")
print("=" * 60)

print("\nARQUITECTURA:")
print(f"  Modelo: U-Net (4 niveles encoder/decoder)")
print(f"  Canales: 64 -> 128 -> 256 -> 512 -> 1024")
print(f"  Parámetros totales: {model_info['total_params']:,}")
print(f"  Dropout: 0.1 (en bottleneck)")
print(f"  Input/Output: {IMG_SIZE}x{IMG_SIZE}")

print("\nCONFIGURACION:")
print(f"  Batch size: {BATCH_SIZE}")
print(f"  Learning rate: {LEARNING_RATE}")
print(f"  Epocas maximas: {NUM_EPOCHS}")
print(f"  Val split: {VAL_SPLIT*100:.0f}%")
print(f"  Loss: BCEDiceLoss (BCE=0.3, Dice=0.7)")
print(f"  Optimizer: Adam")
print(f"  Scheduler: CosineAnnealingLR")

print("\nENTRENAMIENTO:")
try:
    _ = history['train_loss'][0]
    valores = history
except (NameError, KeyError, IndexError):
    valores = None

if valores is not None:
    print(f"  Epocas completadas: {len(valores['train_loss'])}")
    print(f"  Mejor Train Dice: {max(valores['train_dice']):.4f}")
    print(f"  Mejor Val Dice: {max(valores['val_dice']):.4f}")
    print(f"  Train Loss final: {valores['train_loss'][-1]:.4f}")
    print(f"  Val Loss final: {valores['val_loss'][-1]:.4f}")
    if 'training_duration_seconds' in valores:
        hours = int(valores['training_duration_seconds'] // 3600)
        minutes = int((valores['training_duration_seconds'] % 3600) // 60)
        print(f"  Duracion total: {hours}h {minutes}m")
else:
    print("  (Entrenamiento no ejecutado en esta sesion)")
    try:
        print(f"  Mejor modelo (checkpoint):")
        print(f"    Epoca: {checkpoint['epoch']}")
        print(f"    Train Dice: {checkpoint['train_dice']:.4f}")
        print(f"    Val Dice: {checkpoint['val_dice']:.4f}")
    except (NameError, KeyError):
        print("  No hay datos de entrenamiento disponibles")

print("\nEVALUACION (Validacion):")
print(f"  Threshold optimo: {optimal_threshold:.2f}")
print(f"  Dice medio: {validation_results['dice_mean']:.4f}")
print(f"  Dice std: {validation_results['dice_std']:.4f}")
print(f"  Dice minimo: {validation_results['dice_min']:.4f}")
print(f"  Dice maximo: {validation_results['dice_max']:.4f}")
print(f"  Imagenes evaluadas: {validation_results['num_images']}")

print("\nPREDICCIONES TEST:")
print(f"  Total imagenes: {len(test_predictions_binary)}")
print(f"  Con foreground: {len(rle_encodings) - empty_predictions}")
print(f"  Vacias (sin persona): {empty_predictions}")
print(f"  Tamano mascaras: {test_predictions_binary.shape[1]}x{test_predictions_binary.shape[2]}")

print("\nSUBMISSION KAGGLE:")
print(f"  Archivo: {submission_path}")
print(f"  Filas: {len(submission_df)}")
file_size_mb = submission_path.stat().st_size / (1024 * 1024)
print(f"  Tamano: {file_size_mb:.2f} MB")

print("\n" + "=" * 60)
objetivo_dice = 0.75
dice_actual = validation_results['dice_mean']
if dice_actual >= objetivo_dice:
    print(f"OBJETIVO CUMPLIDO: Dice {dice_actual:.4f} >= {objetivo_dice}")
    print(f"Margen sobre objetivo: +{(dice_actual - objetivo_dice)*100:.1f}%")
else:
    print(f"OBJETIVO NO CUMPLIDO: Dice {dice_actual:.4f} < {objetivo_dice}")
print("=" * 60)
```

---

## Variables Required

| Variable | Source Cell | Description |
|----------|-------------|-------------|
| `model_info` | Model definition | Dict with `total_params` |
| `IMG_SIZE` | Config | 384 |
| `BATCH_SIZE` | Config | 8 |
| `LEARNING_RATE` | Config | 1e-4 |
| `NUM_EPOCHS` | Config | 700 |
| `VAL_SPLIT` | Config | 0.2 |
| `history` | Training loop | Dict with losses/metrics per epoch |
| `checkpoint` | Load best model | Dict from saved .pth |
| `optimal_threshold` | Threshold search | Float |
| `validation_results` | Evaluation | Dict with dice stats |
| `test_predictions_binary` | Test inference | np.array (N, 800, 800) |
| `rle_encodings` | RLE encoding | List of strings |
| `empty_predictions` | RLE encoding | Int count |
| `submission_df` | Submission creation | DataFrame |
| `submission_path` | Submission creation | Path object |

---

## Changes from Original

| Aspect | Original | Proposed |
|--------|----------|----------|
| Sections | 4 | 7 |
| Config info | None | Complete |
| Architecture detail | "4 niveles" | Full channel progression + dropout |
| Checkpoint fallback | No | Yes |
| Training duration | No | Yes |
| Submission info | No | Yes |
| Kaggle objective check | No | Automatic (>=0.75) |
| Test mask dimensions | No | Yes (800x800) |
