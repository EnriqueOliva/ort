# Tarea 1 - Experiment Log

Quick record of all model versions and adjustments we tried.

## Model Architecture (SimpleCNN)

Base architecture (remained constant):
- 3 Conv layers (32 → 64 → 128 filters)
- 3x3 kernels, padding=1
- MaxPool2d after each conv
- 2 FC layers (51200 → 256 → 10)
- ReLU activations throughout

## Experiment History

### Version 1: Multi-Experiment Approach
**Date**: First attempt
**Config**:
- Exp1: Baseline (no regularization)
- Exp2: Dropout only
- Exp3: Dropout + Data Augmentation + Batch Normalization
**Result**: Too complicated, user asked to simplify

### Version 2: Dropout + Data Aug + Early Stopping
**Date**: After simplification
**Config**:
- Dropout(0.5) in FC layers
- Data Augmentation (RandomHorizontalFlip, RandomRotation ±10°)
- Early Stopping (patience=5, delta=0.001)
- Epochs: 20
- Batch size: 64
- Learning rate: 0.001
**Result**:
- Trained successfully
- Train Acc: ~79%
- Val Acc: ~75%
- Stopped at epoch 20
- Gap: ~4-5% (healthy)

### Version 3: Data Aug + Early Stopping Only
**Date**: Completed
**Config**:
- **Removed Dropout completely**
- Data Augmentation only (RandomHorizontalFlip, RandomRotation ±10°)
- Early Stopping (patience=5, delta=0.001)
- Epochs: 25 (increased from 20)
- Batch size: 64
- Learning rate: 0.001
- Optimizer: Adam (no weight decay)
**Reason for changes**: User explicitly requested only 2 regularization techniques
**Result**:
- Stopped at epoch 13 (early stopping)
- **SEVERE OVERFITTING**
- Train Acc: 86.88%
- Val Acc: 69.68%
- **Gap: 17.2%** ⚠️
- Worst classes: chain saw (51% F1), gas pump (60% F1)
- Best classes: tench (80% F1), parachute (75% F1)
**Analysis**: Current regularization (light data aug + early stopping) NOT sufficient. Model memorizing training data.

### Version 4: BatchNorm + Dropout + Weight Decay (ALL AT ONCE) ❌ FAILED
**Date**: Completed
**Config**:
- **BatchNormalization** after each conv layer (3 BN layers)
- **Dropout(0.5)** in FC layers
- **Weight Decay (1e-4)** in Adam optimizer (L2 regularization)
- **Data Augmentation** (RandomHorizontalFlip, RandomRotation ±10°)
- **Early Stopping** (patience=5, delta=0.001)
- Epochs: 30 (ran all 30, early stopping NEVER triggered)
- Batch size: 64
- Learning rate: 0.001
**Result**:
- Train Acc: 53.59%
- Val Acc: 69.38% (best was 70.04% at epoch 28)
- **WORSE than Version 3!** (dropped from 69.68% to 69.38%)
- **NOW UNDERFITTING** (train < val) - over-regularized!
- Worst classes: chain saw (48% F1), gas pump (55% F1)
- Best classes: tench (81% F1), parachute (80% F1)
**Analysis**:
- **CRITICAL MISTAKE**: Added 3 new techniques simultaneously
- Cannot isolate which technique helped vs hurt
- Over-regularized - model can't even learn training data properly
- Need incremental testing: add ONE technique at a time from Version 3 baseline
- **Lesson**: Scientific method requires controlled experiments, not shotgun approach

### Version 5: Dropout ONLY (Starting from V3 baseline) ✅ SUCCESS!
**Date**: Completed
**Config**:
- **Dropout(0.5)** in FC layers (ONLY new addition from V3)
- Data Augmentation (RandomHorizontalFlip, RandomRotation ±10°)
- Early Stopping (patience=5, delta=0.001)
- Epochs: 25 (stopped at 17)
- Batch size: 64
- Learning rate: 0.001
- **NO BatchNorm, NO Weight Decay**
**Regularization Techniques (3 total)**:
1. Dropout (0.5)
2. Data Augmentation
3. Early Stopping
**Result**:
- Stopped at epoch 17 (early stopping worked)
- Train Acc: 82.10%
- Val Acc: **73.81%** (best was 73.92% at epoch 15)
- **Gap: 8.29%** ✅ (reduced from 17.2%!)
- **Improvement over V3**: +4.13% val accuracy (69.68% → 73.81%)
- **Overfitting reduced by more than half**: 17.2% → 8.29%
- Weak classes improved:
  - Chain saw: 51% → 57% F1 (+6 points)
  - Gas pump: 60% → 67% F1 (+7 points)
  - Golf ball: 65% → 69% F1 (+4 points)
- Best classes: tench (82% F1), English springer (81% F1), parachute (81% F1)
**Analysis**:
- **VALIDATES incremental approach**: Adding ONLY Dropout isolated its positive impact
- Dropout was the missing piece - it alone solved most of the overfitting
- Healthy train/val gap (8.29%) indicates good generalization
- Model still has capacity to learn (82% train acc) but isn't memorizing
- Scientific method worked: controlled experiment showed Dropout's clear benefit

### Version 6: Dropout + LR Scheduler (Starting from V5) ⚠️ WORSE
**Date**: Completed
**Config**:
- **Dropout(0.5)** in FC layers
- Data Augmentation (RandomHorizontalFlip, RandomRotation ±10°)
- Early Stopping (patience=5, delta=0.001)
- **Learning Rate Scheduler: ReduceLROnPlateau** (ONLY new addition)
  - Reduces LR by factor of 0.5 when val loss plateaus (patience=3)
  - Min LR: 1e-6
  - Starts at LR: 0.001
- Epochs: 30 (stopped at 18)
- Batch size: 64
- **NO BatchNorm, NO Weight Decay**
**Regularization Techniques (4 total)**:
1. Dropout (0.5)
2. Data Augmentation
3. Early Stopping
4. Learning Rate Scheduling
**Result**:
- Stopped at epoch 18 (early stopping)
- Train Acc: 83.09%
- Val Acc: 72.76%
- **Gap: 10.33%** (worse than V5's 8.29%)
- **WORSE than V5**: -1.05% val accuracy (73.81% → 72.76%)
**Analysis**:
- LR scheduler hurt performance instead of helping
- Likely triggered too early, cutting LR while model was still learning
- Random initialization variance also played a role
- Lesson: Not all "best practices" help every model - validate incrementally

### Version 7: Improved Architecture (ImprovedCNN) - Starting from V5 ✅ SUCCESS!
**Date**: Completed
**Architecture Changes (vs SimpleCNN)**:
- **4 convolutional layers** (vs 3 in SimpleCNN)
- **Wider channels**: 64→128→256→512 (vs 32→64→128)
- **Larger FC hidden layer**: 512 units (vs 256)
- **More capacity**: ~27.8M parameters (vs ~13M in SimpleCNN)
- Keeps same proven regularization from V5
**Config**:
- Architecture: ImprovedCNN (4 conv + 2 FC)
- Dropout(0.5) in FC layers
- Data Augmentation (RandomHorizontalFlip, RandomRotation ±10°)
- Early Stopping (patience=5, delta=0.001, tracking val_loss)
- Epochs: 25 (stopped at 17)
- Batch size: 64
- Learning rate: 0.001
- **NO LR Scheduler** (V6 showed it didn't help)
**Regularization Techniques (3 total)**:
1. Dropout (0.5)
2. Data Augmentation
3. Early Stopping
**Result**:
- Stopped at epoch 17 (early stopping triggered)
- Train Acc: 87.42%
- Val Acc: **75.59%** (final), **76.66%** (best at epoch 14)
- **Gap: 11.83%** (increased from V5's 8.29%)
- **BEST ACCURACY YET**: 75.59% val accuracy (vs V5's 73.81%)
- F1-Score: 75.72%
- Val loss peaked at epoch 12 (0.7935), but val acc peaked at epoch 14 (76.66%)
- Weak classes:
  - Chain saw: 53% precision, 62% recall, 57% F1 (still worst)
  - French horn: 69% precision, 79% recall, 73% F1
  - Gas pump: 78% precision, 65% recall, 71% F1
- Best classes: tench (84% F1), parachute (81% F1), English springer (83% F1)
**Analysis**:
- **Architecture improvement worked!** +1.78% val accuracy (73.81% → 75.59%)
- Deeper + wider architecture provides better feature extraction
- However, **overfitting increased**: gap grew from 8.29% to 11.83%
- **Early stopping may have triggered too early**:
  - Stopped based on val_loss at epoch 12
  - But val_acc was BEST at epoch 14 (76.66%)
  - Training curves show model still improving when stopped
- Chain saw remains problematic class across all versions
- Trade-off: Better capacity = better accuracy but more overfitting

### Version 8: Remove Early Stopping Experiment (Test V7 Theory) ❌ FAILED - PROVED EARLY STOPPING WAS CORRECT
**Date**: Completed
**Hypothesis**: V7's early stopping triggered too early; model would continue improving beyond epoch 17
**Config**:
- Architecture: ImprovedCNN (same as V7)
- Dropout(0.5) in FC layers
- Data Augmentation (RandomHorizontalFlip, RandomRotation ±10°)
- **NO Early Stopping** (removed to test full training)
- Epochs: 30 (all completed)
- Batch size: 64
- Learning rate: 0.001
**Regularization Techniques (2 total)**:
1. Dropout (0.5)
2. Data Augmentation
**Result**:
- Completed all 30 epochs (no early stopping)
- Train Acc: **93.60%** (kept climbing - memorization)
- Val Acc: **75.26%** (final), **75.64%** (best at epoch 21)
- **Gap: 18.34%** (SEVERE overfitting - almost doubled from V7's 11.83%)
- Val loss: 0.83 at epoch 12 → 1.32 at epoch 30 (EXPLODED)
- F1-Score: 75.21%
- Essentially same val accuracy as V7 (75.26% vs 75.59%)
- Weak classes: chain saw (59% F1), cassette player (72% F1), gas pump (70% F1)
- Best classes: tench (85% F1), church (78% F1), parachute (80% F1)
**Analysis**:
- **HYPOTHESIS REJECTED**: Model did NOT improve beyond epoch 17
- **Early stopping was PROTECTIVE, not restrictive**:
  - Epochs 1-12: Healthy learning (val climbing)
  - Epochs 12-21: Val plateaus around 75-76% (best 75.64% at epoch 21)
  - Epochs 21-30: Pure memorization (train→93.6%, val stagnates)
- **Gained only +0.05% peak val accuracy** (75.59% → 75.64%) but **doubled overfitting** (11.83% → 18.34%)
- **Critical insight**: We've hit the **ceiling at ~75-76% val accuracy** with current regularization
- Dropout 0.5 alone is **insufficient regularization** for 27.8M parameters on 9,469 images
- After epoch 15, model has learned all generalizable patterns and starts memorizing training data
- **Conclusion**: V7 was optimal; early stopping saved us from this disaster

### Version 9: V7 + Weight Decay (Final Optimization Attempt) ⚠️ NO IMPROVEMENT
**Date**: Completed
**Hypothesis**: Adding L2 regularization (weight decay) will break the 76% ceiling
**Rationale**:
- V7 showed ImprovedCNN (27.8M params) needs more regularization
- Weight decay is the ONE technique we haven't properly isolated
- V4 tested it but mixed with BatchNorm (bad science)
- This is clean: V7 + only weight decay added
**Config**:
- Architecture: ImprovedCNN (same as V7)
- Dropout(0.5) in FC layers
- Data Augmentation (RandomHorizontalFlip, RandomRotation ±10°)
- Early Stopping (patience=5, delta=0.001, tracking val_loss)
- **Weight Decay (1e-4)** - NEW ADDITION
- Epochs: 25 (stopped at 18)
- Batch size: 64
- Learning rate: 0.001
**Regularization Techniques (4 total)**:
1. Dropout (0.5)
2. Data Augmentation
3. Early Stopping
4. Weight Decay (L2 regularization)
**Result**:
- Stopped at epoch 18 (early stopping triggered)
- Train Acc: 85.94%
- Val Acc: **75.39%** (final), **75.77%** (best at epoch 13)
- **Gap: 10.55%** (improved from V7's 11.83%)
- F1-Score: 75.47%
- **WORSE than V7**: -0.20% val accuracy (75.59% → 75.39%)
- Weak classes: chain saw (61% F1), gas pump (66% F1), cassette player (73% F1)
- Best classes: parachute (81% F1), tench (88% F1), English springer (82% F1)
**Analysis**:
- **HYPOTHESIS REJECTED**: Weight decay did NOT break the 76% ceiling
- Weight decay HELPED overfitting (gap: 11.83% → 10.55%) but HURT val accuracy (75.59% → 75.39%)
- Trade-off: Better regularization vs slightly worse generalization
- **Critical conclusion**: We've definitively hit the **75-76% ceiling** with ImprovedCNN architecture
- **V7 remains the best model**: 75.59% val acc with manageable 11.83% gap
- To break 76% would require architectural changes (ResNet, skip connections, etc.) or significantly more training data

### Final Submission Model: ImprovedCNN (Clean V7 Replication)
**Date**: Completed - SUBMITTED
**Purpose**: Final clean run for submission with best configuration
**Config**:
- Architecture: ImprovedCNN (4 conv + 2 FC)
- Dropout(0.5) in FC layers
- Data Augmentation (RandomHorizontalFlip, RandomRotation ±10°)
- Early Stopping (patience=5, delta=0.001, tracking val_loss)
- **NO Weight Decay** (V9 showed it didn't help)
- Epochs: 25 (stopped at 13)
- Batch size: 64
- Learning rate: 0.001
**Regularization Techniques (3 total)**:
1. Dropout (0.5)
2. Data Augmentation
3. Early Stopping
**Result**:
- Stopped at epoch 13 (early stopping triggered earlier this run)
- Train Acc: 83.55%
- Val Acc: **74.96%** (best 75.62% at epoch 10)
- **Gap: 8.59%** (healthy, better than V7's 11.83%)
- F1-Score: 74.59%
- Weak classes: chain saw (54% F1), gas pump (69% F1)
- Best classes: tench (85% F1), English springer (83% F1), parachute (80% F1)
**Analysis**:
- Consistent with all other runs (~75% val accuracy ceiling)
- Better regularization than V7 (gap: 8.59% vs 11.83%) due to earlier stopping
- Random initialization gave slightly different convergence path but same ceiling
- **Final model is solid and submission-ready**: 75% accuracy with healthy train-val gap

## Summary: What Worked and What Didn't

**Successful Strategies:**
- ✅ Incremental testing methodology (one change at a time)
- ✅ ImprovedCNN architecture (4 layers, wider) over SimpleCNN
- ✅ Dropout (0.5) in FC layers - critical for generalization
- ✅ Data Augmentation (moderate flips/rotations)
- ✅ Early Stopping - protected from severe overfitting

**Failed Strategies:**
- ❌ Weight Decay (improved gap but hurt val accuracy)
- ❌ Learning Rate Scheduler (cut LR too aggressively)
- ❌ Removing Early Stopping (led to severe memorization)
- ❌ Over-regularization (BatchNorm + Dropout + Weight Decay together)

**Key Insights:**
- Performance ceiling: **~75-76% validation accuracy** with ImprovedCNN
- Random initialization variance: ±1-2% across runs
- Early stopping is essential for this architecture/dataset combination
- Breaking 76% requires architectural changes (ResNet, skip connections) or more training data

## Key Fixes Applied

1. **Pillow version mismatch**: Added reinstall cells at notebook start
2. **Dataset download error**: Changed `download=True` to `download=False`
3. **Missing Resize transform**: Added `Resize((160, 160))` to all transform pipelines (CRITICAL)
4. **Image stacking error**: Rewrote statistics calculation to process images individually
5. **Class names as tuples**: Added conditional logic to handle tuple class names
6. **Broken experiment cells**: Removed cells 35-44 from old multi-experiment version
7. **Cell type errors**: Fixed cells 28 and 32 (were "code" but contained markdown)

## Notes

- Using Imagenette 160px version (9,469 train / 3,925 val images)
- Class balance: ~10% per class (well balanced, no special handling needed)
- Normalization: ImageNet stats (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
- Device: CUDA (RTX 4070)
- Wandb project: 'Tarea1'
