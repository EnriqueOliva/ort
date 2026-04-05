# U-Net Segmentation Improvement Plan

## Current State Summary (After Run 14)

### Performance Metrics
| Metric | Run 2 (Baseline) | Run 12 | Run 14 (Current) | Change R12→R14 |
|--------|------------------|--------|------------------|----------------|
| **Mean Dice** | 0.9012 | 0.9550 | **0.9558** | +0.08% |
| **Median Dice** | 0.9489 | 0.9809 | **0.9819** | +0.10% |
| **Std Deviation** | 0.1241 | 0.0723 | **0.0807** | +11.6% (slightly worse) |
| **Best Case** | 0.9957 | 0.9970 | **0.9982** | +0.12% |
| **Worst Case** | 0.0870 | 0.2897 | **0.3533** | **+22.0%** ✅ |
| **Optimal Threshold** | 0.40 | 0.45 | **0.50** | Changed |

### Total Improvement from Baseline
| Metric | Run 2 → Run 14 | % Improvement |
|--------|----------------|---------------|
| Mean Dice | 0.9012 → 0.9558 | **+6.06%** |
| Median Dice | 0.9489 → 0.9819 | **+3.48%** |
| Std Dev | 0.1241 → 0.0807 | **-35.0%** (better) |
| Worst Case | 0.0870 → 0.3533 | **+306%** ✅✅✅ |

### ✅ Run 14 Further Improved Worst Case!
| Metric | Run 12 → Run 14 | Change |
|--------|-----------------|--------|
| Worst Case | 0.2897 → 0.3533 | **+22%** ✅ |
| Mean Dice | 0.9550 → 0.9558 | +0.08% |

**What worked in Run 14:** Removed CoarseDropout and GaussNoise, lower eta_min (5e-7), 700 epochs

### Current Configuration (Run 14)
| Parameter | Value |
|-----------|-------|
| Image Size | **384×384** (from 800×800) |
| Batch Size | 8 |
| Learning Rate | 1e-4 (initial) |
| Epochs | **700** |
| **Early Stopping** | **DISABLED** |
| **Loss Function** | **BCEDiceLoss (0.3 BCE + 0.7 Dice)** |
| Optimizer | Adam |
| **Scheduler** | **CosineAnnealingLR** (T_max=700, eta_min=5e-7) |
| Normalization | InstanceNorm2d |
| Upsampling | Bilinear + Conv |
| Dropout | p=0.1 at bottleneck |

### 🔄 Run 15 Plan: Color Invariance + Stronger Regularization

**Hypothesis:** Run 14 failures are dominated by color confusion. ChannelShuffle and stronger color augmentation should force shape-based learning.

| Parameter | Run 14 | Run 15 | Rationale |
|-----------|--------|--------|-----------|
| **ChannelShuffle** | None | **p=0.10** | Break "pink=skin" dependency |
| **Color aug p** | 0.35 | **0.50** | More color variation |
| **ToGray** | p=0.20 | **p=0.30** | Better B&W handling |
| **Dropout** | p=0.10 | **p=0.25** | Stronger regularization |
| **eta_min** | 5e-7 | **1e-4** | Keep late epochs productive |

**Expected:** Mean Dice 0.96-0.97, Worst Case 0.40-0.50

### Key Improvements Made
1. ✅ **CosineAnnealingLR** - Smooth LR decay (no warm restarts)
2. ✅ **Loss weights 0.3/0.7** - More weight to Dice since it's the evaluation metric
3. ✅ **Removed early stopping** - Fixed epochs for stable training
4. ✅ **No warm restarts** - Smooth decay outperforms periodic restarts
5. ✅ **384×384 resolution** - Higher resolution captures more detail
6. ✅ **400 epochs** - Extended training with smooth LR decay (NO overfitting!)

### Experiments Completed
| Experiment | Result | Decision |
|------------|--------|----------|
| TTA (Test-Time Augmentation) | Mean Dice -0.0004 | ❌ Discarded |
| TTA + Re-optimized Threshold | No improvement | ❌ Discarded |
| Post-Processing | Couldn't measure on val | ❌ Discarded |
| CosineAnnealingWarmRestarts | Mean Dice +0.0028 (vs ReduceLROnPlateau) | ⚠️ Replaced |
| Loss Weights 0.3/0.7 | Mean Dice +0.0007, Std -0.0055 | ✅ Kept |
| No Early Stop + 120 epochs | Mean Dice +0.0069, Worst +0.042 | ✅ Kept |
| CosineAnnealingLR (no restarts) | Mean Dice +0.0051, Worst +0.131 | ✅ Kept |
| Larger Batch Size (8→18) | Val Dice -0.0074 | ❌ Reverted to batch 8 |
| Dropout (p=0.2) in bottleneck | No effect at equal epochs | ⚠️ INCONCLUSIVE |
| **384×384 + 400 epochs** | **Mean +0.0185, Worst -0.058** | ✅ **BEST MEAN** ⚠️ Worst regressed |
| **Focal Tversky Loss (Run 10)** | **Worst -72%, Mean -1%** | ❌ **FAILED** - BCEDiceLoss better |
| **No Data Augmentation (Run 11)** | **Worst -71%, Mean -0.75%** | ❌ **FAILED** - Overfitting |

### Why CosineAnnealingLR (without Warm Restarts)?

**Problem 1:** ReduceLROnPlateau never triggered because val_dice oscillated without triggering "plateau" detection.

**Problem 2:** CosineAnnealingWarmRestarts was too aggressive - periodic restarts disrupted fine-tuning.

**Solution:** CosineAnnealingLR guarantees smooth LR decay from 1e-4 to 1e-6 following a cosine curve.

| Scheduler | Behavior | Result |
|-----------|----------|--------|
| **ReduceLROnPlateau** | Waits for plateau, then reduces LR | ❌ Never triggered |
| **CosineAnnealingWarmRestarts** | Periodic restarts to max LR | ⚠️ Too aggressive, destabilized outliers |
| **CosineAnnealingLR** | One smooth curve: max → min | ✅ **BEST** - stable convergence |

**Key Finding:** Warm restarts hurt worst-case performance. Removing them improved worst Dice from 0.088 → 0.219 (+148%).

### Why Larger Batch Size Hurt Performance (Run 7)

**Experiment:** Changed batch size from 8 to 18 (same memory as 384×384 batch 8).

**Result:** Val Dice dropped from 0.9167 → 0.9093 (-0.74%)

**Why this happened:**
| Factor | Small Batch (8) | Large Batch (18) |
|--------|-----------------|------------------|
| Gradient noise | High (beneficial) | Low |
| Escape local minima | Easier | Harder |
| Minima quality | Flat (better generalization) | Sharp (worse) |
| Updates per epoch | More | Fewer |

**The "flat minima" theory:**
- Small batches introduce noise that helps find "flat" minima
- Flat minima generalize better to unseen data
- Large batches converge to "sharp" minima that overfit
- Reference: "On Large-Batch Training for Deep Learning" (Keskar et al., 2017)

**Practical conclusion:** Keep batch size 8 for this task. For the final 384×384 run, use batch 8 (not higher).

### Why Dropout Didn't Help (Run 8) ⚠️ LESSON LEARNED

**⚠️ We had NO real justification for adding dropout.**

We added dropout purely as an experiment to see what would happen.
This was NOT a hypothesis-driven improvement - there was no evidence of overfitting:

| Indicator | Run 6 Value | What It Means |
|-----------|-------------|---------------|
| Train/Val gap | ~2-3% | Small, healthy gap |
| Val Dice trend | Still improving | Not plateauing |
| Train Dice | ~0.94 | Not memorizing |

**Dropout is meant to fix overfitting. We didn't have overfitting.**

**Run 8 Results (UNFAIR comparison):**

| Metric | Run 6 (120 ep) | Run 8 (70 ep) | Change |
|--------|----------------|---------------|--------|
| Mean Dice | 0.9167 | 0.9051 | -0.0116 ❌ |
| Worst Case | 0.2188 | 0.0574 | -0.1614 ❌ |

**But this comparison is UNFAIR** - Run 8 had only 70 epochs vs Run 6's 120 epochs.

**FAIR Comparison (Run 7 vs Run 8 at epoch 70):**

Using W&B charts to compare at equal epoch counts:
- Both runs had val_dice ≈ 0.90 at epoch 70
- Curves overlap almost perfectly
- **Dropout had MINIMAL effect**

**Why LR decayed faster in Run 8:**
- CosineAnnealingLR with T_max=70 reaches minimum LR at epoch 70
- CosineAnnealingLR with T_max=120 still has LR left at epoch 70
- Run 8's LR was exhausted; Run 7 could still learn

**Key Lessons:**
1. ⚠️ Don't add regularization without evidence of overfitting
2. ⚠️ Fair comparisons require equal training conditions
3. ⚠️ T_max must match NUM_EPOCHS for proper LR decay
4. ✅ Dropout doesn't break anything, just unnecessary here

**Conclusion:** Dropout experiment was INCONCLUSIVE. At equal epochs, no significant effect.
Since we didn't have overfitting, dropout was unnecessary.

---

## Course Scope Analysis

### What's Explicitly Allowed (from obligatorio.txt and class transcripts)

> "los estudiantes tendrán la libertad de ajustar ciertos **hiperparámetros y configuraciones** mientras mantengan la esencia del paper original"

> "Configuración adecuada del ciclo de entrenamiento, incluyendo la elección de la función de pérdida y del **optimizador (Adam, SGD, etc.)**"

> "Se aceptan mejoras como el uso de técnicas adicionales como **batch normalization**, otras funciones de activación, etc."

### Techniques by Course Coverage

| Technique | Taught in Class? | Allowed? | Notes |
|-----------|------------------|----------|-------|
| **Data Augmentation** | ✅ Class 6 | ✅ Yes | Extensively covered |
| **Dropout** | ✅ Class 3-5 | ✅ Yes | Core regularization |
| **BatchNorm/InstanceNorm** | ✅ Class 4-5 | ✅ Yes | Already using InstanceNorm |
| **Early Stopping** | ✅ Multiple classes | ✅ Yes | Already using |
| **LR Schedulers** | ✅ Tarea 1 (ReduceLROnPlateau) | ✅ Yes | CosineAnnealing allowed |
| **Loss Functions** | ✅ BCE, Dice mentioned | ✅ Yes | Focal Loss = justify |
| **Resolution Changes** | ✅ Class 8 (discussed) | ✅ Yes | Professor mentioned |
| **Transfer Learning** | ✅ Class 7 | ⚠️ Partial | Encoder-only maybe |
| **SE/Attention Blocks** | ❌ Not covered | ⚠️ Risky | Not taught, must justify |
| **Mixed Precision** | ❌ Not covered | ✅ Yes | Optimization only |

### What's NOT Allowed
- ❌ Pre-trained encoders (ResNet backbone) - violates "implementación desde cero"
- ❌ Completely different architectures - must be U-Net
- ❌ External model libraries - must implement from scratch

---

## Course Compliance Analysis (Research Results)

### Summary: Compliance Status of Recommended Techniques

| Technique | Allowed? | Justification? | Risk Level | Implement? |
|-----------|----------|----------------|------------|------------|
| **Focal Tversky Loss** | ✅ YES | ❌ NO | 🟢 ZERO | ✅ YES |
| **LR Warmup** | ✅ YES | ❌ NO | 🟢 ZERO | ✅ YES |
| **Elastic Deformations** | ✅ YES | ❌ NO | 🟢 ZERO | ✅ YES (IN ORIGINAL PAPER!) |
| **Multi-scale TTA** | ✅ YES | ❌ NO | 🟢 ZERO | ❌ TESTED - hurts worst case |
| **Progressive Resizing** | ✅ YES | ❌ NO | 🟢 ZERO | ✅ YES |
| **Morphological Post-proc** | ✅ YES | ❌ NO | 🟢 ZERO | ✅ TESTED - worst +8.96%, mean +0.04% (re-test after Run 12) |
| **Snapshot Ensembles** | ✅ YES | ❌ NO | 🟢 ZERO | ✅ YES |
| **Per-image Threshold** | ✅ YES | ❌ NO | 🟢 ZERO | ❌ TESTED - not worth it |
| **Attention Gates** | ⚠️ MAYBE | ✅ YES | 🟡 LOW-MED | ⚠️ OPTIONAL |
| **Deep Supervision** | ⚠️ MAYBE | ✅ YES | 🟡 MEDIUM | ⚠️ SKIP |

**Bottom line:** 8 techniques are completely safe, 2 need justification, 0 are forbidden.

### Techniques Aligned with Original U-Net Paper (STRONGEST DEFENSE)

#### 🎯 Elastic Deformations (Section 3.1)
> "Especially random elastic deformations of the training samples seem to be the **key concept** to train a segmentation network with very few annotated images."

**Defense:** "As stated in Section 3.1 of the U-Net paper, elastic deformations are identified as THE key data augmentation technique."

#### 🎯 Weighted Loss Functions (Section 3, Equation 1-2)
> "We introduced [weight map] to give some pixels more importance in the training."

**Defense:** "Our Focal Tversky loss is a modern formulation of the paper's weighted loss principle."

#### 🎯 Dropout in Contracting Path (Section 3.1)
> "Drop-out layers at the end of the contracting path perform further implicit data augmentation."

**Defense:** "We tested dropout as suggested in Section 3.1, though our model wasn't overfitting enough to benefit."

### ✅ UPDATE: 400 Epochs Worked! (Research Was Wrong)

**Run 9 proved that 400 epochs is viable and beneficial:**

| What Research Said | What Actually Happened |
|--------------------|------------------------|
| "400 epochs will overfit" | ❌ NO overfitting observed |
| "Use 150 epochs max" | ❌ 400 epochs gave +1.85% Mean Dice |
| "Convergence at 120 epochs" | ❌ Model kept improving past 120 |

**Lesson:** Don't blindly trust general advice. Test with your specific dataset.

### Recommended Implementation Priority

## Upcoming Experiments Plan (Run 10-12)

### Experiment Sequence Logic

We identified that **worst case regressed** (0.2188 → 0.1610) while mean improved.
The strategy is to test changes **independently** in short 120-epoch runs:

```
Run 9 (baseline): Mean=0.9352, Worst=0.1610, BCEDiceLoss, 400ep
    │
    ├─► Run 10: Change ONLY loss function (Focal Tversky)
    │           Goal: Improve worst case
    │           Epochs: 120 (quick test)
    │
    ├─► Run 11: Adjust ONLY data augmentation
    │           Goal: Test if less/different augmentation helps
    │           Epochs: 120 (quick test)
    │
    └─► Run 12: Try ONLY different LR
                Goal: Test if LR affects worst case
                Epochs: 120 (quick test)
```

**Why 120 epochs for Focal Tversky test?**

The goal is to improve **min dice (worst case)**, not mean dice.

Key insight: Focal Tversky Loss changes HOW the model learns from the very beginning
by focusing on hard examples. If this approach helps worst cases, we should see
the improvement trend early in training - we don't need full convergence to validate
the approach.

| What we're testing | What we need to see | Epochs needed |
|--------------------|---------------------|---------------|
| Does Focal Tversky help worst cases? | Positive trend in min dice | ~120 (trend visible) |
| What's the best possible min dice? | Full convergence | ~400 (if trend is positive) |

**Decision logic:**
- If min dice improves at 120 epochs → Run full 400 epochs with Focal Tversky
- If min dice doesn't improve at 120 epochs → The approach doesn't work, try something else

This saves ~11 hours of training if Focal Tversky doesn't help.

---

### ❌ Run 10: Focal Tversky Loss - FAILED

**Hypothesis:** BCEDiceLoss optimizes for average, ignoring hard examples.
Focal Tversky Loss specifically penalizes hard examples.

| Parameter | Value | Change from Run 9 |
|-----------|-------|-------------------|
| Image Size | 384×384 | Same |
| Batch Size | 8 | Same |
| Epochs | **120** | ↓ from 400 |
| T_max | **120** | ↓ from 400 |
| Learning Rate | 1e-4 | Same |
| **Loss** | **FocalTverskyLoss** | ← CHANGE |
| Scheduler | CosineAnnealingLR | Same (no warm restarts) |

**Results - Fair Comparison at Epoch 120:**

| Metric     | Run 9 (BCEDiceLoss) | Run 10 (Focal Tversky) | Change  |
|------------|---------------------|------------------------|---------|
| val_dice   | 0.9202              | 0.9104                 | -0.0098 ❌ |
| **Min Dice** | 0.1610            | **0.0456**             | **-72%** ❌❌❌ |
| Time/Epoch | 97.0 sec            | 105.5 sec              | +8.8% slower |

**Why It FAILED:**
1. BCEDiceLoss was already handling hard examples reasonably well
2. Focal modulation (γ=0.75) was too aggressive, destabilizing edge cases
3. Optimal threshold shifted drastically (0.35 → 0.75) - different confidence patterns

**Conclusion:** Focal Tversky Loss made worst case WORSE, not better.
BCEDiceLoss (0.3/0.7) remains the best loss function for this task.

---

### ❌ Run 11: No Data Augmentation Test - FAILED (OVERFITTING)

**Hypothesis:** Data augmentation might be creating unrealistic training samples
that hurt worst-case performance. Testing if removing it helps.

| Parameter | Value | Change from Run 9 |
|-----------|-------|-------------------|
| Epochs | 120 | ↓ from 400 |
| T_max | 120 | ↓ from 400 |
| Loss | BCEDiceLoss (0.3/0.7) | Same |
| **Augmentation** | **NONE (only resize + normalize)** | ← CHANGE |

**Results - Comparison at Epoch 120:**

| Metric     | Run 9 @ 120ep | Run 11 @ 120ep | Change  |
|------------|---------------|----------------|---------|
| val_dice   | 0.9202        | 0.9127         | -0.0075 ❌ |
| **Min Dice** | 0.1610*     | **0.0466**     | **-71%** ❌❌❌ |
| Std Dev    | ~0.10         | 0.1254         | Worse |
| Threshold  | 0.35          | 0.45           | Changed |

*Run 9 min at 400ep

**Why It FAILED - Classic Overfitting:**

W&B charts showed textbook overfitting:
- train_loss: Dropped to near 0 (memorizing)
- val_loss: **SPIKED UP** around epoch 100-120
- train_dice: ~0.97+ (too high)
- val_dice: Plateaued then declined

**Conclusion:** Data augmentation is ESSENTIAL.
- Worst-case issues are NOT caused by augmentation
- Augmentation prevents overfitting
- The problematic images are just inherently difficult

---

### ✅ Run 12: Smart Augmentation + Dropout ⭐⭐⭐ BEST RUN EVER - COMPLETED

**Status:** ✅ COMPLETED - 570/600 epochs (interrupted but best_model.pth saved)

**Hypothesis:** Current augmentation includes transforms that don't match the data distribution.
By using REALISTIC augmentation + mild dropout, we might get better generalization.

**RESULTS - EXCEEDED ALL EXPECTATIONS:**

| Metric | Run 9 | Run 12 | Change | Expected |
|--------|-------|--------|--------|----------|
| **Mean Dice** | 0.9352 | **0.9550** | **+2.1%** | +1-2% |
| **Median Dice** | 0.9732 | **0.9809** | **+0.8%** | - |
| **Std Dev** | 0.0981 | **0.0723** | **-26%** | - |
| **Worst Case** | 0.1610 | **0.2897** | **+80%** | +15-25% |
| **Threshold** | 0.35 | **0.45** | Changed | - |

**Worst case improved 80% vs expected 15-25%!**

**Dataset Analysis (Visual Review of 5 Images):**

| Image | Observation | Augmentation Implication |
|-------|-------------|-------------------------|
| Image 1 | Silhouette with extreme backlighting | Needs CLAHE |
| Image 100 | Indoor natural light, back to camera | Needs brightness variety |
| Image 500 | Portrait with color grading effects | Needs HueSaturationValue |
| Image 1500 | Black & white professional portrait | Needs ToGray |
| Image 2000 | Vibrant colors, occupational setting | Needs ColorJitter |
| ALL | People UPRIGHT (never inverted) | Remove VerticalFlip |

**Implemented Changes:**

```python
train_transform = A.Compose([
    A.Resize(IMG_SIZE, IMG_SIZE),
    A.HorizontalFlip(p=0.5),
    A.ShiftScaleRotate(
        shift_limit=0.1,
        scale_limit=0.15,
        rotate_limit=15,
        border_mode=cv2.BORDER_CONSTANT,
        value=0, mask_value=0,
        p=0.5
    ),
    A.OneOf([
        A.GridDistortion(num_steps=5, distort_limit=0.2, p=1.0),
        A.OpticalDistortion(distort_limit=0.05, shift_limit=0.05, p=1.0),
    ], p=0.15),
    A.OneOf([
        A.RandomBrightnessContrast(brightness_limit=0.35, contrast_limit=0.35, p=1.0),
        A.CLAHE(clip_limit=(2, 5), tile_grid_size=(8, 8), p=1.0),
        A.RandomGamma(gamma_limit=(70, 130), p=1.0),
    ], p=0.6),
    A.OneOf([
        A.HueSaturationValue(hue_shift_limit=15, sat_shift_limit=25, val_shift_limit=20, p=1.0),
        A.ColorJitter(brightness=0.15, contrast=0.15, saturation=0.2, hue=0.1, p=1.0),
    ], p=0.4),
    A.ToGray(p=0.12),
    A.GaussNoise(var_limit=(5.0, 20.0), p=0.03),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2()
])

# UNet with Dropout2d(p=0.1) in bottleneck
```

| Change | Before → Run 12 | Reason |
|--------|-----------------|--------|
| VerticalFlip | p=0.3 → **REMOVED** | Nobody upside down |
| ElasticTransform | p=0.3 → **REMOVED** | Blurs edges, distorts humans |
| (none) | → **GridDistortion/OpticalDistortion(p=0.15)** | Edge-preserving alternative |
| rotate_limit | 30 → **15** | People mostly upright |
| GaussNoise | p=0.2, var=10-50 → **p=0.03, var=5-20** | Only ~3% of images have noise |
| RandomBrightnessContrast | p=0.3 → **OneOf([Brightness,CLAHE,Gamma], p=0.6)** | Extreme lighting variety |
| (none) | → **HueSaturationValue/ColorJitter(p=0.4)** | Color effects in dataset |
| (none) | → **ToGray(p=0.12)** | B&W images in dataset |
| Dropout | None → **Dropout2d(p=0.1)** | Paper U-Net Sec 3.1 + compensate |

**Remaining Worst Cases Analysis:**

| Rank | Dice | Image | Failure Reason |
|------|------|-------|----------------|
| 1 | 0.2897 | Person on red/orange rocks | Color confusion - rocks ≈ skin |
| 2 | 0.4282 | Baby on pink blanket | Color confusion - blanket ≈ skin |
| 3 | 0.6150 | Extreme close-up neck/hair | Unusual framing |
| 4 | 0.6192 | Child on beige bed | Color confusion - bed ≈ skin |
| 5 | 0.6359 | Woman in dark doorway | Low light + wood ≈ skin |

**Pattern:** Remaining failures are **inherent dataset ambiguities** (skin-colored backgrounds).
This is the ceiling for vanilla U-Net without attention mechanisms.

**Why Run 12 Succeeded:**
1. ✅ Removed VerticalFlip - no more unrealistic upside-down people
2. ✅ Removed ElasticTransform - better edge preservation
3. ✅ Added CLAHE - better handling of extreme lighting
4. ✅ Added ToGray - better B&W image handling
5. ✅ GridDistortion - edge-preserving alternative
6. ✅ Dataset-aligned augmentation - only realistic transforms

---

### 🔄 Run 13: Fixed Color Handling (IN PROGRESS)

**Status:** Code changes implemented, training pending

**Problem Found in Run 12:**

Analyzing augmentation examples showed B&W images receiving pink/red tints - unrealistic!

**Why Simple Fixes Don't Work:**
1. `A.OneOf([ToGray, HueSaturationValue])` - HueSaturationValue still adds color to already-gray images
2. Dataset-level restoration - visualization code bypasses Dataset, showing wrong results

**CORRECT Solution: A.Lambda in Transform Pipeline**

```python
_grayscale_state = {'is_gray': False}

def detect_grayscale(image, **kwargs):
    _grayscale_state['is_gray'] = np.allclose(image[:,:,0], image[:,:,1], atol=3) and \
                                   np.allclose(image[:,:,1], image[:,:,2], atol=3)
    return image

def restore_grayscale_if_needed(image, **kwargs):
    if _grayscale_state['is_gray']:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    return image

train_transform = A.Compose([
    A.Lambda(image=detect_grayscale),         # DETECT at START
    # ... all augmentations ...
    A.Lambda(image=restore_grayscale_if_needed),  # RESTORE before Normalize
    A.Normalize(...),
])
```

**Changes Implemented:**

| Change | Run 12 → Run 13 | Why |
|--------|-----------------|-----|
| **A.Lambda(detect_grayscale)** | None → START | Detect B&W before augmentation |
| **A.Lambda(restore_grayscale)** | None → before Normalize | Restore B&W after augmentation |
| hue_shift_limit | 15 | **30** (more color invariance) |
| sat_shift_limit | 25 | **40** (more color invariance) |
| ChannelShuffle | None | **p=0.05** (breaks "red=skin" dependency) |

**Expected Impact:**
- **Guaranteed** B&W images stay B&W (works for visualization AND training)
- Better color invariance (worst cases were color confusion)
- ChannelShuffle forces model to not rely on "red channel = skin"

---

### 🔄 Future Run: Warm Restarts (First Epochs Only)

**Hypothesis:** Warm restarts might help exploration early in training, but hurt fine-tuning later.

**Background:**
- We tested CosineAnnealingWarmRestarts in Run 3 → improved mean but hurt worst case
- We then removed warm restarts in Run 6 → worst case improved from 0.0484 to 0.2188 (+351%)
- **Key insight:** Warm restarts during late training disrupt fine-tuning of hard examples

**Proposed Experiment:**
Use warm restarts **only in the first N epochs**, then switch to smooth decay:

| Phase | Epochs | Scheduler | Behavior |
|-------|--------|-----------|----------|
| Phase 1 (Exploration) | 0-40 | CosineAnnealingWarmRestarts(T_0=10) | 4 restarts to explore |
| Phase 2 (Convergence) | 40-400 | CosineAnnealingLR(T_max=360) | Smooth decay, no restarts |

**Implementation Approach:**
```python
# Two schedulers with manual switch
scheduler_warmup = CosineAnnealingWarmRestarts(optimizer, T_0=10, T_mult=1)
scheduler_main = CosineAnnealingLR(optimizer, T_max=360, eta_min=1e-6)

for epoch in range(NUM_EPOCHS):
    if epoch < 40:
        scheduler_warmup.step()
    else:
        if epoch == 40:
            # Reset LR for smooth decay phase
            for param_group in optimizer.param_groups:
                param_group['lr'] = LEARNING_RATE
        scheduler_main.step()
```

**Expected Outcome:**
- Better exploration in early epochs (warm restarts)
- Stable convergence in later epochs (smooth decay)
- Potentially best of both worlds for worst-case performance

**Priority:** Lower than Focal Tversky Loss test. Only try if Run 10-12 don't solve worst case.

---

### Decision Tree After Experiments

```
After Run 10 (Focal Tversky):
├── If worst case improves significantly:
│   └── Keep Focal Tversky for final run
└── If no improvement:
    └── Try combining with augmentation changes (Run 11)

After Run 11 (Augmentation):
├── If helps:
│   └── Combine best augmentation with best loss
└── If no help:
    └── Keep original augmentation

After Run 12 (LR):
├── If helps:
│   └── Use best LR for final run
└── If no help:
    └── Keep 1e-4

FINAL RUN: Combine all improvements, run 400 epochs
```

---

#### Phase 1: COMPLETED ✅
| Change | Status | Result |
|--------|--------|--------|
| 384×384 Resolution | ✅ DONE (Run 9) | +1.85% Mean Dice |
| 400 epochs | ✅ DONE (Run 9) | No overfitting |
| Loss weights 0.3/0.7 | ✅ DONE | Already in use |

#### Phase 2: IN PROGRESS 🔄
| Run | Change | Status | Goal |
|-----|--------|--------|------|
| **10** | **Focal Tversky Loss** | ❌ **FAILED** | Worst case got WORSE (-72%) |
| **11** | **No Data Augmentation** | ❌ **FAILED** | Overfitting, worst -71% |
| **12** | **Smart Augmentation + Dropout** | 🔄 **IN PROGRESS** | Match augmentation to data distribution |

#### Phase 3: AFTER QUICK TESTS
- Combine best configurations from Runs 10-12
- Final 400-epoch run with optimal settings

#### Phase 4: SKIP (Too Risky)
- Attention Gates (needs justification)
- Deep Supervision (architecture change)

---

## Remaining Experiments (Prioritized by Course Relevance)

### Priority 1: High Impact, Course-Relevant

#### Experiment A: Increase Resolution to 384×384 ✅ COMPLETED (Run 9)
**Status:** ✅ DONE - Mean Dice improved +1.85%!
**Result:** Mean Dice 0.9167 → 0.9352 (+0.0185)

| Metric | Before (256×256) | After (384×384) | Change |
|--------|------------------|-----------------|--------|
| Mean Dice | 0.9167 | **0.9352** | +1.85% ✅ |
| Worst Case | 0.2188 | **0.1610** | -26% ❌ |

**Lesson:** Higher resolution helps mean but may hurt worst case.

---

#### Experiment B: Adjust BCEDiceLoss Weights ✅ ALREADY DONE
**Status:** ✅ Already implemented (0.3 BCE + 0.7 Dice)
**In use since:** Run 4

---

#### Experiment C: Add Dropout to Bottleneck ⚠️ TESTED - INCONCLUSIVE
**Course Relevance:** HIGH - Dropout extensively covered in classes 3-5
**Status:** ⚠️ TESTED in Run 8 - No significant effect

**What We Tested:**
- Added Dropout2d(p=0.2) to bottleneck
- Ran for 70 epochs with T_max=70

**Results:**
- At equal epochs (70), dropout showed NO significant effect vs no-dropout
- The apparent performance drop (0.9167 → 0.9051) was due to fewer epochs, not dropout

**Why It Didn't Help:**
⚠️ **We had NO justification for adding dropout in the first place.**
- Run 6 train/val gap was only ~2-3% (healthy, not overfitting)
- Model was already well-regularized by data augmentation
- Dropout fixes overfitting - we didn't have overfitting

**Lesson Learned:**
Don't add regularization without evidence of the problem it solves.
This was an exploratory experiment, not a hypothesis-driven improvement.

**Implementation (for reference):**
```python
# In the U-Net __init__, after bottleneck conv:
self.dropout = nn.Dropout2d(p=0.2)

# In forward, after bottleneck:
x5 = self.down4(x4)
x5 = self.dropout(x5)  # Dropout here
```

**Teacher's Dropout Explanation (Transformers vs U-Net):**

In class (transcript1.txt), the teacher explained dropout in the context of Transformers:
> "en cada sublayer, antes de ser añadido al input y normalizado, se aplica un dropout de 0.1"

The Transformer pattern: `X → Sublayer → Dropout → Add residual → LayerNorm`

**For U-Net, the pattern is different:**
| Aspect | Transformer | U-Net |
|--------|-------------|-------|
| Connection type | ADD (residual) | CONCATENATE (skip) |
| Normalization | LayerNorm | BatchNorm/InstanceNorm |
| Dropout location | Before add+norm | **Bottleneck** (between encoder/decoder) |

The teacher's concept of "regularization through dropout" applies, but the exact placement differs:
- Transformers: Multiple dropout points (after each sublayer)
- U-Net: Single dropout in bottleneck (deepest point, most abstract features)

**Why bottleneck?** It's where features are most compressed (1024 channels in our case). Dropping activations here forces the decoder to be robust to missing high-level features.

**Conclusion:** Dropout is unnecessary for this task. Model already generalizes well.

---

### Priority 2: Medium Impact, Course-Relevant

#### Experiment D: Stronger Data Augmentation
**Course Relevance:** HIGH - Class 6 was entirely about data augmentation
**Expected Gain:** +0.005 to +0.01 Dice
**Implementation Time:** ~10 min code, ~1.5 hours training

**Implementation:**
```python
train_transform = A.Compose([
    A.Resize(IMG_SIZE, IMG_SIZE),
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5),  # Increased from 0.3
    A.RandomRotate90(p=0.5),  # NEW
    A.ShiftScaleRotate(
        shift_limit=0.15,
        scale_limit=0.15,
        rotate_limit=45,
        p=0.7
    ),
    A.ElasticTransform(alpha=150, sigma=6, p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    A.GaussNoise(var_limit=(0.0, 0.02), p=0.3),
    A.Normalize(...),
    ToTensorV2()
])
```

**Justification for notebook:**
"Se intensificó el data augmentation para mejorar la generalización del modelo, aumentando las probabilidades de rotación, escala y transformaciones elásticas."

---

#### Experiment E: Focal Tversky Loss ⭐ NEXT STEP (Run 10)
**Course Relevance:** HIGH - Loss functions explicitly allowed, addresses worst-case issue
**Expected Gain:** +10-15% worst case improvement
**Implementation Time:** ~20 min code, ~2-3 hours training (120 epochs)

**Why Focal Tversky Loss?**
- BCEDiceLoss optimizes for average performance
- Focal Tversky specifically targets hard examples (like our worst-case images)
- Combines Tversky's asymmetric weighting with focal modulation

**Run 10 Configuration:**
```python
IMG_SIZE = 384  # Keep from Run 9
BATCH_SIZE = 8
NUM_EPOCHS = 120  # Quick test before committing to 400
LEARNING_RATE = 1e-4
T_max = 120

class FocalTverskyLoss(nn.Module):
    def __init__(self, alpha=0.3, beta=0.7, gamma=0.75, smooth=1e-6):
        super().__init__()
        self.alpha = alpha  # Weight for false positives
        self.beta = beta    # Weight for false negatives (higher = penalize more)
        self.gamma = gamma  # Focal parameter (lower = more focus on hard examples)
        self.smooth = smooth

    def forward(self, predictions, targets):
        predictions = torch.sigmoid(predictions)
        predictions = predictions.view(-1)
        targets = targets.view(-1)

        TP = (predictions * targets).sum()
        FP = ((1 - targets) * predictions).sum()
        FN = (targets * (1 - predictions)).sum()

        tversky_index = (TP + self.smooth) / (TP + self.alpha * FP + self.beta * FN + self.smooth)
        focal_tversky = (1 - tversky_index) ** self.gamma

        return focal_tversky

criterion = FocalTverskyLoss(alpha=0.3, beta=0.7, gamma=0.75)
```

**Why These Parameters?**
- `alpha=0.3, beta=0.7`: Penalize false negatives more (missing parts of the mask)
- `gamma=0.75`: Focus on hard examples without being too aggressive

**Justification for notebook:**
"Se implementó Focal Tversky Loss para mejorar el rendimiento en los casos difíciles. El paper U-Net original usa weighted loss (Ecuación 1-2) para dar más importancia a píxeles difíciles; Focal Tversky es una formulación moderna del mismo principio."

---

### Priority 3: Lower Priority / More Risky

#### Experiment F: SE Blocks (Attention)
**Course Relevance:** LOW - Not covered in class
**Risk:** High - May be questioned in defense
**Expected Gain:** +0.005 to +0.01 Dice

**Recommendation:** Only attempt if other experiments done and time permits. Would need strong justification.

---

## Recommended Experiment Order

Based on course relevance and effort vs. gain:

### Phase 1: Quick Wins (Already Done)
- ~~TTA~~ → ❌ Failed
- ~~CosineAnnealingLR~~ → ✅ Success (+0.0028)

### Phase 2: Next Steps (Choose 1-2)
1. **Experiment A: 384×384 Resolution** - Highest expected gain, course-discussed
2. **Experiment C: Dropout** - Proven in Tarea 1, addresses outliers

### Phase 3: If Time Permits
3. **Experiment B: Loss Weights** - Easy change, low risk
4. **Experiment D: Stronger Augmentation** - Course-covered, may help variance

### Phase 4: Advanced (Only if needed)
5. **Experiment E: Focal Loss** - For outliers, must justify

---

## Tracking Progress

### Run History
| Run | Config Changes | Mean Dice | Median | Std | Worst | Notes |
|-----|---------------|-----------|--------|-----|-------|-------|
| 1 | Baseline 35ep | ? | ? | ? | ? | Initial test |
| 2 | 70ep, patience=10 | 0.9012 | 0.9489 | 0.1241 | 0.0870 | ReduceLROnPlateau never triggered |
| 3 | WarmRestarts, 100ep | 0.9040 | 0.9575 | 0.1293 | 0.0484 | Plateau broken |
| 4 | Loss 0.3/0.7, 84ep | 0.9047 | 0.9540 | 0.1238 | 0.0460 | Early stop killed run |
| 5 | No early stop, 120ep | 0.9116 | 0.9560 | 0.1193 | 0.0880 | Good, but warm restarts aggressive |
| 6 | No warm restarts | 0.9167 | 0.9622 | 0.1134 | 0.2188 | Best worst case |
| 7 | Batch 8→18 | 0.9093* | - | - | - | ❌ Larger batch hurt (-0.74%) |
| 8 | Dropout p=0.2, 70ep | 0.9051 | 0.9541 | 0.1238 | 0.0574 | ⚠️ INCONCLUSIVE |
| **9** | **384×384, 400ep** | **0.9352** | **0.9732** | **0.0981** | **0.1610** | ✅ **BEST MEAN** ⚠️ Worst regressed |
| 10 | Focal Tversky, 120ep | 0.9112 | 0.9527 | 0.1186 | 0.0456 | ❌ **FAILED** - Worst case -72% |
| 11 | No Augmentation, 120ep | 0.9127 | 0.9628 | 0.1254 | 0.0466 | ❌ **FAILED** - Overfitting |
| **12** | **Smart Aug + Dropout** | **0.9550** | **0.9809** | **0.0723** | **0.2897** | ⭐⭐⭐ BEST RUN (at the time) |
| 13 | Fixed Color Handling + Custom LR | - | - | - | - | Superseded by Run 14 |
| **14** | **CosineAnnealingLR restored, cleaner aug** | **0.9558** | **0.9819** | **0.0807** | **0.3533** | ⭐⭐⭐ **CURRENT BEST** |
| **15** | **ChannelShuffle + stronger reg** | ? | ? | ? | ? | 🔄 **PLANNED** |

*Run 7 interrupted at epoch 109/120.
*Run 8 had 70 epochs vs Run 6's 120 epochs.
*Run 11 showed classic overfitting (val_loss spiked up).
*Run 12: Smart augmentation (removed VerticalFlip, ElasticTransform; added CLAHE, ToGray, GridDistortion) + Dropout2d(p=0.1). 570/600 epochs.
*Run 14: Reverted to CosineAnnealingLR, removed CoarseDropout/GaussNoise, eta_min=5e-7, 700 epochs. **Worst case +22% vs Run 12.**
*Run 15: ChannelShuffle p=0.10, color aug p=0.50, ToGray p=0.30, dropout p=0.25, eta_min=1e-4.

---

## Current Performance vs Target

| Scenario | Mean Dice | Worst Case | Status |
|----------|-----------|------------|--------|
| Baseline (Run 2) | 0.9012 | 0.0870 | ✅ Achieved |
| + WarmRestarts (Run 3) | 0.9040 | 0.0484 | ✅ Achieved |
| + Loss Weights 0.3/0.7 (Run 4) | 0.9047 | 0.0460 | ✅ Achieved |
| + No Early Stopping (Run 5) | 0.9116 | 0.0880 | ✅ Achieved |
| + No Warm Restarts (Run 6) | 0.9167 | 0.2188 | Previous best worst |
| + 384×384, 400ep (Run 9) | 0.9352 | 0.1610 | Previous best mean |
| + Smart Aug + Dropout (Run 12) | 0.9550 | 0.2897 | Previous best overall |
| **+ Cleaner Aug (Run 14)** | **0.9558** | **0.3533** | ⭐⭐⭐ **CURRENT BEST** |
| **Course Requirement** | 0.75 | - | ✅ EXCEEDED (+27.4%) |

**Status:** Mean Dice 0.9558 is **well above** the 0.75 requirement (+27.4%).

✅ **Run 14 improved worst case:** 0.2897 → 0.3533 (+22%)

**What worked (Run 12 → Run 14):**
- Removed unrealistic transforms (VerticalFlip, ElasticTransform)
- Matched augmentation to actual data distribution
- Added CLAHE (for extreme lighting), ToGray (for B&W images), GridDistortion (edge-preserving)
- Run 14: Removed CoarseDropout and GaussNoise (cleaner signal)
- Run 14: Lower eta_min (5e-7) for more fine-tuning
- Run 14: 700 epochs for thorough convergence

**Remaining worst cases (Run 14 analysis):**
- Color confusion: pink blankets, orange rocks, wooden textures segmented as skin
- B&W images: model struggles without color cues
- White clothing: under-segmented (bride's dress)
- Object bleeding: bikes, backpacks near humans get segmented

**Run 15 targets:** ChannelShuffle to break color dependency, higher ToGray for B&W robustness

### Experiments Summary
| Experiment | Expected | Actual | Status |
|------------|----------|--------|--------|
| Focal Tversky Loss | +10-15% worst | **-72% worst** | ❌ **FAILED Run 10** |
| No Data Augmentation | Unknown | **-71% worst** | ❌ **FAILED Run 11** |
| **Smart Augmentation + Dropout** | +15-25% worst | **+80% worst, +2.1% mean** | ⭐⭐⭐ **SUCCESS Run 12** |
| Multi-scale TTA | Unknown | -4.88% worst | ❌ TESTED - hurts worst case |
| Morphological Post-proc | Unknown | +8.96% worst | ✅ TESTED - may not need now |
| Per-image Threshold (Otsu) | Unknown | +0.69% worst | ❌ TESTED - not worth it |
| 384×384 Resolution | +1-2% mean | +1.85% mean | ✅ DONE (Run 9) |
| Larger Batch Size | Unknown | -0.74% mean | ❌ TESTED Run 7 - hurt |
| Dropout p=0.2 (alone) | Unknown | No effect | ⚠️ TESTED Run 8 - inconclusive |
| Attention Gates | +2-5% | N/A | ⚠️ Not needed - Run 12 is excellent |
| Deep Supervision | +2-3% | N/A | ⚠️ SKIP - risky, not needed |

---

## Important Reminders

1. **Justify every change** - The professor will ask "¿por qué hiciste esto?"
2. **Only use course-covered techniques** unless you can strongly justify
3. **CosineAnnealingLR is allowed** - It's a hyperparameter configuration (LR scheduler)
4. **Monitor VRAM** when changing resolution or batch size
5. **Save checkpoints** before each experiment
6. **Document in notebook** - "Se cambió X porque Y"

---

## Quick Reference: Justifications for Defense

| Technique | Justification |
|-----------|---------------|
| CosineAnnealingLR (sin restarts) | "ReduceLROnPlateau no se disparaba. Probamos WarmRestarts pero era muy agresivo y dañaba los casos difíciles. CosineAnnealingLR (sin restarts) da un decaimiento suave y estable." |
| Sin Early Stopping | "Decidimos entrenar por un número fijo de épocas porque: (1) CosineAnnealingLR proporciona convergencia natural sin necesidad de early stopping, (2) nuestros experimentos mostraron que early stopping mató runs prematuramente (Run 2 y Run 4), (3) tenemos un sistema de checkpoints robusto que guarda `best_model.pth` solo cuando val_dice mejora, así que aunque el modelo degrade después, siempre tenemos guardado el mejor estado." |
| Loss Weights 0.3/0.7 | "Más peso a Dice (0.7) porque es la métrica de evaluación. BCE (0.3) mantiene estabilidad del entrenamiento." |
| InstanceNorm vs BatchNorm | "InstanceNorm funciona mejor con batch sizes pequeños según el paper U-Net." |
| BCEDiceLoss | "Combina BCE para estabilidad con Dice para optimizar directamente la métrica de evaluación." |
| **384×384 Resolution** | "Mayor resolución captura más detalle de las imágenes originales de 800×800. Run 9 demostró +1.85% en Mean Dice." |
| **400 epochs** | "Probamos 400 épocas y NO hubo overfitting. El modelo siguió mejorando. Mean Dice subió de 0.9167 a 0.9352." |
| Data Augmentation | "Aumenta la variabilidad del dataset y reduce overfitting, como vimos en clase 6." |
| Smart Augmentation (Run 12) | "Se modificó el augmentation para alinearlo con las características reales del dataset: se eliminó VerticalFlip porque ninguna imagen tiene personas invertidas, se reemplazó ElasticTransform por GridDistortion para preservar bordes, se agregó CLAHE para siluetas y ToGray para imágenes B&W." |
| Dropout p=0.1 (Run 12) | "El paper U-Net Sección 3.1 menciona dropout en el bottleneck. Usamos p=0.1 muy suave para compensar la reducción de variedad al eliminar augmentaciones poco realistas." |
| Threshold 0.35 | "El umbral óptimo bajó de 0.50 a 0.35 con la resolución mayor. Se optimiza con grid search en validación." |
| Batch Size 8 (no más) | "Probamos batch 18 en Run 7 y empeoró el rendimiento. Batch sizes pequeños introducen ruido beneficioso que ayuda a encontrar mínimos planos y mejorar la generalización." |
| Focal Tversky Loss | "El paper original usa weighted loss para dar más importancia a píxeles difíciles (Ecuación 1-2). Focal Tversky es una formulación moderna del mismo principio." |
| Elastic Deformations | "Sección 3.1 del paper U-Net las identifica como EL concepto clave de data augmentation para entrenar con pocos datos." |
| LR Warmup | "Técnica estándar de scheduling. Permite que el modelo encuentre una buena región del espacio de parámetros antes de empezar el decaimiento coseno." |

---

## Defense Talking Points

### Opening Statement
> "Implementamos U-Net siguiendo la arquitectura y estrategias de entrenamiento del paper original. Realizamos 11 experimentos sistemáticos, logrando un Mean Dice de 0.9352 (+24.7% sobre el requisito de 0.75). Todas nuestras modificaciones están dentro de las técnicas permitidas: ajuste de hiperparámetros, diferentes funciones de pérdida, data augmentation, y learning rate scheduling."

### If Asked About Deviations from the Paper
> "Mientras el paper usa batch size 1 con alto momentum, usamos batch size 8 que es más práctico para GPUs modernas y aún suficientemente pequeño para buena generalización. También modernizamos ciertos componentes como usar InstanceNorm en lugar de BatchNorm, y una función de pérdida compuesta en lugar de weighted cross-entropy, pero ambos sirven el mismo propósito: enfatizar ejemplos difíciles."

### If Asked About Experiments
> "Realizamos 11 experimentos probando varias configuraciones. Hallazgos clave: (1) CosineAnnealingLR superó significativamente a ReduceLROnPlateau y warm restarts, (2) batch sizes pequeños (8) dieron mejor generalización que batches grandes (18), (3) 400 épocas NO causaron overfitting (contrario a lo esperado), (4) resolución 384×384 mejoró el Mean Dice en +1.85%."

### Prepared Answers for Common Questions

**Q: "¿Por qué 400 épocas? ¿No es demasiado?"**
> A: "Probamos 400 épocas y observamos que el modelo siguió mejorando sin overfitting. El Mean Dice subió de 0.9167 (120 épocas) a 0.9352 (400 épocas). El gap train-val se mantuvo saludable (~3-4%). CosineAnnealingLR con T_max=400 garantiza un decaimiento suave del learning rate."

**Q: "¿Por qué no usaron batch size 1 como el paper?"**
> A: "El paper usó batch size 1 por limitaciones de memoria GPU. Con GPUs modernas y normalización apropiada (InstanceNorm), batch size 8 da mejor estabilidad de gradientes. Validamos esto en Run 7 donde batch 18 empeoró el rendimiento, confirmando que batches pequeños generalizan mejor."

**Q: "¿Por qué el worst case empeoró en Run 9?"**
> A: "BCEDiceLoss optimiza el promedio, no los casos extremos. Identificamos esto y planeamos implementar Focal Tversky Loss, que específicamente penaliza ejemplos difíciles. Es una técnica permitida (loss functions) y está alineada con el weighted loss del paper original (Ecuación 1-2)."

**Q: "¿Por qué no usaron dropout como sugiere el paper?"**
> A: "Probamos dropout (p=0.2) en el bottleneck como sugiere la Sección 3.1. Sin embargo, nuestro gap train-val era solo 2-3%, indicando que el modelo no estaba haciendo overfitting. Dropout no mostró mejora en nuestros experimentos (Run 8). El énfasis del paper en dropout era para su dataset más pequeño (30 imágenes); con 2133 imágenes y augmentation fuerte, no lo necesitamos."

**Q: "¿Por qué resolución 384×384?"**
> A: "Las imágenes originales son 800×800. 384×384 es el mejor compromiso entre detalle y memoria GPU. Es divisible por 2^4=16 (perfecto para 4 niveles de U-Net). Run 9 demostró +1.85% de mejora en Mean Dice respecto a 256×256."

**Q: "¿Por qué no usaron early stopping? ¿No es arriesgado entrenar 600 épocas?"**
> A: "Deshabilitamos early stopping por tres razones: (1) CosineAnnealingLR ya proporciona convergencia natural - el LR decae suavemente de 1e-4 a 1e-6, así que el modelo naturalmente deja de aprender agresivamente. (2) Nuestros experimentos mostraron que early stopping mató runs prematuramente - Run 2 paró en época 61, Run 4 paró en época 84, ambos antes de alcanzar su potencial máximo. Cuando deshabilitamos early stopping en Run 5 y Run 6, el rendimiento mejoró significativamente. (3) Tenemos un sistema de checkpoints robusto: `best_model.pth` se guarda SOLO cuando val_dice mejora. Si el modelo degrada después (hipotéticamente), aún tenemos el mejor estado guardado. La inferencia siempre carga `best_model.pth`, no el estado final. Es estrictamente mejor que early stopping."
