# Techniques That Don't Require Retraining

Use Run 9's trained model (400 epochs, Mean Dice 0.9352).

## Can Test Now (Inference-Time)

| Technique | Expected Gain | Time | Status |
|-----------|---------------|------|--------|
| Per-image Threshold (Otsu) | +0.5-1% | 15 min | ❌ TESTED - not worth it (mean -0.03%, worst +0.69%) |
| Multi-scale TTA (0.75x, 1.0x, 1.25x) | +0.18% mean | 15 min | ❌ TESTED - hurts worst case (-4.88%) |
| Morphological Post-proc | **+8.96% worst** | 20 min | ✅ TESTED - BEST! Re-test after Run 12 (may not be needed) |

## Requires Retraining

- LR Warmup
- Elastic Deformations
- Data Augmentation changes
- LR experiments
- Architecture changes
