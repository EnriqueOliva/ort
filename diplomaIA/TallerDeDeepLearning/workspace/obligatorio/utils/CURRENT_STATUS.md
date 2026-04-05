# U-Net Segmentation Project - Current Status

## Project Overview

- **Task:** Human segmentation (binary masks) using U-Net from scratch
- **Dataset:** Custom dataset from teacher, 4800 images total (2133 train, 534 test), 800×800 pixels
- **Course Requirement:** Mean Dice >= 0.75
- **Current Achievement:** Mean Dice 0.9352 (+24.7% above requirement)
- **Notebook:** `C:\Users\Enrique\Documents\2doSemestre\TallerDeDeepLearning\workspace\obligatorio\lab\obligatorio.ipynb`

---

## Current Best Model: Run 9

| Metric | Value |
|--------|-------|
| **Mean Dice** | **0.9352** ✅ |
| Median Dice | 0.9732 |
| Std Dice | 0.0981 |
| **Min Dice (worst)** | **0.1610** ❌ |
| Max Dice | 0.9969 |
| Optimal Threshold | 0.35 |

### Run 9 Configuration

| Parameter | Value |
|-----------|-------|
| Image Size | 384×384 (from 800×800) |
| Batch Size | 8 |
| Epochs | 400 |
| Learning Rate | 1e-4 → 1e-6 |
| Scheduler | CosineAnnealingLR (T_max=400, no warm restarts) |
| Loss | BCEDiceLoss (0.3 BCE + 0.7 Dice) |
| Normalization | InstanceNorm2d |
| Early Stopping | DISABLED |
| Data Augmentation | HorizontalFlip, VerticalFlip, ShiftScaleRotate, ElasticTransform, RandomBrightnessContrast, GaussNoise |

### Worst Case Problem

The worst case (Min Dice = 0.1610) is concerning. The same 5 images consistently perform poorly:
- **Indices:** [198, 257, 283, 7, 97]
- **Scores:** [0.161, 0.187, 0.329, 0.423, 0.530]

---

## All Experiments Summary

### Training Runs (Require Retraining)

| Run | Changes | Mean Dice | Min Dice | Result |
|-----|---------|-----------|----------|--------|
| 2 | Baseline 70ep | 0.9012 | 0.0870 | Baseline |
| 3 | CosineAnnealingWarmRestarts | 0.9040 | 0.0484 | +0.28% mean |
| 4 | Loss weights 0.3/0.7 | 0.9047 | 0.0460 | Kept |
| 5 | No early stopping, 120ep | 0.9116 | 0.0880 | +0.69% mean |
| 6 | No warm restarts | 0.9167 | **0.2188** | Best worst case! |
| 7 | Batch 18 (vs 8) | 0.9093 | - | ❌ Larger batch hurt |
| 8 | Dropout p=0.2 | 0.9051 | 0.0574 | ⚠️ Inconclusive (fewer epochs) |
| **9** | **384×384, 400ep** | **0.9352** | 0.1610 | ✅ **BEST MEAN** |
| 10 | Focal Tversky Loss | 0.9112 | 0.0456 | ❌ Worst -72% |
| 11 | No Augmentation | 0.9127 | 0.0466 | ❌ Overfitting |

### Inference-Time Tests (No Retraining)

All tested on Run 9's model:

| Technique | Mean Change | Worst Change | Verdict |
|-----------|-------------|--------------|---------|
| Otsu Per-Image Threshold | -0.03% | +0.69% | ❌ Not worth it |
| Multi-scale TTA (0.75x, 1.0x, 1.25x) | +0.18% | **-4.88%** | ❌ Hurts worst case |
| **Morphological Post-proc** | +0.04% | **+8.96%** | ✅ **BEST!** |

**Key Finding:** Morphological post-processing is the ONLY technique that improved worst case!
- Worst case: 0.1609 → 0.1754 (+8.96%)
- Operations: opening, closing, remove small objects (<100px), fill holes (<100px)

**Decision:** NOT adding to notebook permanently yet. This is a "band-aid" for Run 9's noisy predictions. Run 12 might produce cleaner predictions that don't need this fix. Re-test after Run 12.

---

## Key Lessons Learned

### What Worked
1. **CosineAnnealingLR (no warm restarts)** - Smooth LR decay is better than periodic restarts
2. **384×384 resolution** - Higher resolution captures more detail (+1.85% mean)
3. **400 epochs** - Did NOT overfit (contrary to expectations)
4. **Loss weights 0.3/0.7** - More weight to Dice since it's the evaluation metric
5. **Batch size 8** - Small batches generalize better than large batches
6. **Morphological post-processing** - Improves worst case by cleaning up noisy predictions

### What Failed
1. **Focal Tversky Loss** - Made worst case 72% WORSE
2. **No Data Augmentation** - Caused classic overfitting
3. **Larger Batch Size (18)** - Hurt performance (sharp minima)
4. **Multi-scale TTA** - Hurt worst case by 4.88%
5. **Warm Restarts** - Too aggressive, hurt worst case

### Key Insights
- Warm restarts disrupt fine-tuning of hard examples
- Data augmentation is ESSENTIAL (Run 11 proved this)
- The worst-case images are NOT caused by augmentation - they're inherently difficult
- Model was trained at 384×384, so other scales (TTA) are out-of-distribution

---

## Dataset Analysis

Manual review of training images revealed:

| Observation | Current Augmentation | Problem |
|-------------|---------------------|---------|
| All people UPRIGHT | VerticalFlip(p=0.3) | 30% upside-down - unrealistic |
| HIGH quality photos | GaussNoise(p=0.2) | Only ~3% have noise |
| EXTREME lighting variety | Brightness(p=0.3) | Should be HIGHER priority |
| Realistic poses only | ElasticTransform(p=0.3) | Distorts bodies, blurs edges |
| People mostly upright | rotate_limit=30 | Too aggressive |

**Dataset Size Context:**
- Original U-Net paper: ~30 images → HEAVY augmentation needed
- Our dataset: 2133 images → MODERATE augmentation needed
- Run 11 proved: Can't remove augmentation (overfitting)
- But: Don't need unrealistic transforms

---

## Next Step: Run 12 - Smart Augmentation + Dropout

**Hypothesis:** Current augmentation includes transforms that don't match the data distribution. By using REALISTIC augmentation + dropout, we might get better generalization.

### Proposed Changes

```python
train_transform = A.Compose([
    A.Resize(IMG_SIZE, IMG_SIZE),
    A.HorizontalFlip(p=0.5),                    # KEEP
    # REMOVED: VerticalFlip                     # Nobody upside down
    A.ShiftScaleRotate(
        shift_limit=0.1,
        scale_limit=0.2,
        rotate_limit=10,                        # REDUCED from 30
        border_mode=cv2.BORDER_CONSTANT,
        p=0.5
    ),
    # REMOVED: ElasticTransform                 # Blurs edges, distorts bodies
    A.RandomBrightnessContrast(
        brightness_limit=0.4,                   # INCREASED
        contrast_limit=0.4,
        p=0.6                                   # INCREASED
    ),
    A.GaussNoise(var_limit=(5.0, 25.0), p=0.05), # REDUCED to match data
    A.Normalize(...),
    ToTensorV2()
])

# + Dropout(0.2) in bottleneck to compensate for reduced augmentation
```

### Summary of Changes

| Change | Current → Proposed | Reason |
|--------|-------------------|--------|
| VerticalFlip | p=0.3 → REMOVE | Nobody upside down |
| ElasticTransform | p=0.3 → REMOVE | Distorts humans, blurs edges |
| rotate_limit | 30 → 10 | People mostly upright |
| GaussNoise | p=0.2 → p=0.05 | Only ~3% of images have noise |
| Brightness | p=0.3 → p=0.6 | Lighting is main variation |
| Dropout | None → 0.2 | Compensate for reduced augmentation |

### Expected Outcome
- Less total augmentation but BETTER MATCHED to data
- ElasticTransform removal may help edge definition on worst cases
- Dropout compensates for reduced variety

---

## Important Files

| File | Purpose |
|------|---------|
| `lab/obligatorio.ipynb` | Main notebook |
| `lab/models/best_model.pth` | Run 9's trained model |
| `lab/logs/validation_results.json` | Current validation metrics |
| `lab/results/submission.csv` | Kaggle submission file |
| `HISTORY.md` | Detailed experiment log |
| `IMPROVEMENT_PLAN.md` | Full improvement plan and analysis |
| `NO_RETRAIN_TESTS.md` | Inference-time tests summary |

---

## Notebook Structure (Key Cells)

| Cells | Purpose |
|-------|---------|
| 1-3 | Imports, device, paths |
| 14 | IMG_SIZE, BATCH_SIZE, NUM_EPOCHS |
| 16 | Data augmentation transforms |
| 20 | SegmentationDataset class |
| 28 | UNet class definition |
| 43-44 | Train/val split, DataLoaders |
| 45-50 | Optimizer, scheduler, training setup |
| **51** | **Training loop (SKIP when loading model)** |
| 52-53 | Save history, plot curves (SKIP) |
| 54 | Load best_model.pth |
| 55-58 | Validation and threshold optimization |
| 62-64 | Test inference |
| 69-71 | RLE encoding and submission.csv |

**To load model without retraining:** Run cells 1-50, SKIP 51-53, run 54.

---

## Dropout Implementation (for Run 12)

From teacher's class (Transformers context):
> "en cada sublayer, antes de ser añadido al input y normalizado, se aplica un dropout de 0.1"

For U-Net, placement is different:
- Transformers: Multiple dropout points (after each sublayer)
- **U-Net: Single dropout in bottleneck** (most compressed features)

```python
# In UNet __init__, after bottleneck conv:
self.dropout = nn.Dropout2d(p=0.2)

# In forward, after bottleneck:
x5 = self.down4(x4)
x5 = self.dropout(x5)  # Dropout here
```

---

## Quick Reference: Defense Justifications

| Technique | Justification |
|-----------|---------------|
| CosineAnnealingLR | "ReduceLROnPlateau no se disparaba. CosineAnnealingLR da decaimiento suave y estable." |
| 400 epochs | "Probamos 400 épocas y NO hubo overfitting. Mean Dice subió de 0.9167 a 0.9352." |
| 384×384 | "Mayor resolución captura más detalle. Run 9 demostró +1.85% en Mean Dice." |
| BCEDiceLoss 0.3/0.7 | "Más peso a Dice (0.7) porque es la métrica de evaluación." |
| Data Augmentation | "Run 11 demostró que sin augmentation hay overfitting clásico." |
| Morphological Post-proc | "Limpia predicciones ruidosas. Mejoró worst case +8.96% sin afectar mean." |

---

**Last Updated:** 2025-11-26
**Current Phase:** Ready for Run 12 (Smart Augmentation + Dropout)
