## ⚠️ DEFENSE REMINDER: Mixed Precision Training (AMP)

Mixed Precision Training (`use_amp`, `GradScaler`, `autocast`) was **NOT taught in any class**.
This is self-implemented from external research. Be prepared to explain if asked:
- Uses float16 for forward/backward (faster, less memory)
- Maintains float32 for weight updates (precision)
- GradScaler prevents gradient underflow in float16

---

List of tests carried out:

1. Dry run
2. Run 1: First real run. 35 epochs
3. Run 2: 70 epochs but early stopping at 61
4. TTA and post-processing experiments (no retraining)
5. Run 3: CosineAnnealingWarmRestarts. 100 epochs, patience 20
6. Run 4: Loss weights 0.3/0.7. Early stopping killed run at 84 epochs
7. Run 5: No early stopping, 120 epochs (with warm restarts)
8. Run 6: CosineAnnealingLR without warm restarts, 120 epochs
9. Run 7: Batch size test (18 vs 8), 109/120 epochs (interrupted) ❌ WORSE
10. Run 8: Dropout experiment (p=0.2), 70 epochs. No real reason to do this. Just because it was ⚠️ INCONCLUSIVE
11. Run 9: 384×384 resolution, 400 epochs ✅ BEST MEAN DICE (but worst case regressed)
12. Run 10: Focal Tversky Loss, 120 epochs ❌ FAILED (worst case -72%)
13. Run 11: No Data Augmentation, 120 epochs ❌ FAILED (overfitting)
14. Otsu Per-Image Thresholding (no retraining) ❌ NOT WORTH IT
15. Multi-scale TTA (no retraining) ❌ NOT WORTH IT - hurts worst case
16. Morphological Post-Processing (no retraining) ✅ HELPS WORST CASE (+8.96%)
17. Run 12: Brings back data augmentation but with serious improvements, and 400 epochs. Best run ever.
18. Run 13. Adds even more adjustments to data augmentation and increases LR in second half of training. 
19. Run 14. Reverting back to previous LR scheduler, with twice as low min LR. CoarseDropout and GaussNoise removed from data augmentation.

Explanation of tests:

4. TTA & Post-Processing Experiments

  TTA Validation Results:

  | Metric           | Without TTA | With TTA | Change  |
  |------------------|-------------|----------|---------|
  | Mean Dice        | 0.9012      | 0.9008   | -0.0004 |
  | Median Dice      | 0.9489      | 0.9507   | +0.0017 |
  | Std Dev          | 0.1241      | 0.1273   | +0.0032 |
  | Min Dice (worst) | 0.0870      | 0.1037   | +0.0167 |
  | Max Dice         | 0.9957      | 0.9956   | -0.0001 |

  TTA + Re-optimized Threshold:
  - Optimal threshold remained 0.40 (unchanged)
  - No improvement from threshold re-optimization

  Conclusion: TTA did NOT help. Mean Dice decreased slightly.
  Model already trained with same augmentations, so TTA provides no benefit.
  Post-processing couldn't be measured on validation (only applied to test).

  Decision: Reverted TTA and post-processing. Moving to Phase 2.

5. Run 3: CosineAnnealingWarmRestarts

  Changes from Run 2:
  - Scheduler: ReduceLROnPlateau -> CosineAnnealingWarmRestarts
  - T_0=10, T_mult=2 (cycles: 10, 20, 40 epochs)
  - NUM_EPOCHS: 70 -> 100
  - PATIENCE: 10 -> 20

  Rationale:
  - ReduceLROnPlateau never triggered in Run 2 (LR stayed at 1e-4)
  - CosineAnnealingWarmRestarts forces LR exploration with periodic restarts
  - More epochs + higher patience to let scheduler work

  Results:

  | Metric           | Run 2 (61 ep) | Run 3 (90 ep) | Change  |
  |------------------|---------------|---------------|---------|
  | Mean Dice        | 0.9012        | 0.9040        | +0.0028 |
  | Median Dice      | 0.9489        | 0.9575        | +0.0086 |
  | Std Dev          | 0.1241        | 0.1293        | +0.0052 |
  | Min Dice (worst) | 0.0870        | 0.0484        | -0.0386 |
  | Max Dice         | 0.9957        | 0.9965        | +0.0008 |
  | Optimal Thresh   | 0.40          | 0.40          | -       |

  Training Details:
  - Epochs completed: 90 (early stopping triggered)
  - Best val_dice: 0.9034 at epoch 70
  - Final train_dice: 0.9081 | val_dice: 0.8830
  - Training duration: 1h 30m (5392 seconds)

  Conclusion: CosineAnnealingWarmRestarts successfully broke the plateau.
  Mean Dice improved +0.31%, Median improved +0.91%.
  The warm restarts forced LR exploration that ReduceLROnPlateau couldn't achieve.

6. Run 4: Loss Weights

  Changes from Run 3:
  - BCEDiceLoss weights: 0.5/0.5 -> 0.3/0.7 (more weight to Dice)

  Results:

  | Metric           | Run 3 (90 ep) | Run 4 (84 ep) | Change  |
  |------------------|---------------|---------------|---------|
  | Mean Dice        | 0.9040        | 0.9047        | +0.0007 |
  | Median Dice      | 0.9575        | 0.9540        | -0.0035 |
  | Std Dev          | 0.1293        | 0.1238        | -0.0055 (better) |
  | Min Dice (worst) | 0.0484        | 0.0460        | -0.0024 |
  | Max Dice         | 0.9965        | 0.9950        | -0.0015 |
  | Optimal Thresh   | 0.40          | 0.40          | -       |

  Training Details:
  - Epochs completed: 84 (early stopping triggered)
  - Best val_dice: 0.9042 at epoch 64
  - Training duration: 1h 47m (6462 seconds)

  Note: Loss weights 0.3/0.7 showed slight improvement in Mean Dice (+0.0007)
  and reduced variance (-0.0055 std).

7. Run 5: 120 Epochs, No Early Stopping (with Warm Restarts)

  Changes from Run 4:
  - Early stopping: REMOVED (incompatible with warm restarts)
  - NUM_EPOCHS: 100 -> 120

  Rationale for 120 epochs:
  - With T_0=10, T_mult=2, restart schedule: 10, 30, 70, 150
  - 120 epochs = last restart at epoch 70, then 50 epochs of decay
  - More time to converge after final restart

  Results:

  | Metric           | Run 4 (84 ep) | Run 5 (120 ep) | Change  |
  |------------------|---------------|----------------|---------|
  | Mean Dice        | 0.9047        | 0.9116         | +0.0069 |
  | Median Dice      | 0.9540        | 0.9560         | +0.0020 |
  | Std Dev          | 0.1238        | 0.1193         | -0.0045 (better) |
  | Min Dice (worst) | 0.0460        | 0.0880         | +0.0420 |
  | Max Dice         | 0.9950        | 0.9957         | +0.0007 |
  | Optimal Thresh   | 0.40          | 0.40           | -       |

  Training Details:
  - Epochs completed: 120 (full run, no early stopping)
  - Best val_dice: ~0.91
  - Warm restart spikes visible at epochs 10, 30, 70

  Conclusion: Good improvement, but warm restarts may be too aggressive.
  Decided to try CosineAnnealingLR (no restarts) next.

8. Run 6: CosineAnnealingLR without Warm Restarts ✅ BEST RUN

  Changes from Run 5:
  - Scheduler: CosineAnnealingWarmRestarts -> CosineAnnealingLR
  - T_max=120 (one smooth curve over all epochs)
  - No periodic LR restarts

  Rationale:
  - Warm restarts may be too aggressive for fine-tuning
  - Smooth decay allows continuous refinement without disruption
  - More stable convergence for edge cases

  Results:

  | Metric           | Run 5 (WarmRestarts) | Run 6 (No Restarts) | Change  |
  |------------------|----------------------|---------------------|---------|
  | Mean Dice        | 0.9116               | 0.9167              | +0.0051 ✅ |
  | Median Dice      | 0.9560               | 0.9622              | +0.0062 ✅ |
  | Std Dev          | 0.1193               | 0.1134              | -0.0059 (better) ✅ |
  | Min Dice (worst) | 0.0880               | 0.2188              | +0.1308 ✅✅✅ |
  | Max Dice         | 0.9957               | 0.9962              | +0.0005 |
  | Optimal Thresh   | 0.40                 | 0.50                | Changed |

  Training Details:
  - Epochs completed: 120 (full run)
  - Best val_dice: ~0.92
  - Smooth LR decay from 1e-4 to 1e-6

  Key Observations:
  - EVERY metric improved
  - Worst case improved DRAMATICALLY: 0.088 → 0.219 (+148%)
  - Optimal threshold shifted from 0.40 to 0.50 (model more confident)
  - Variance decreased (more consistent predictions)

  Why Removing Warm Restarts Helped:
  - Warm restarts were too aggressive for this task
  - Model was already finding good solutions
  - Restarts disrupted fine-tuning phase
  - Smooth decay = stable convergence = better outlier handling

  Conclusion: CosineAnnealingLR (no restarts) OUTPERFORMS WarmRestarts.
  This is now the best configuration with Mean Dice 0.9167 (+22.2% above requirement).

9. Run 7: Larger Batch Size Test (Batch 18) ❌ WORSE THAN RUN 6

  Changes from Run 6:
  - Batch size: 8 -> 18

  Rationale:
  - Memory test: 256×256 batch 18 uses similar VRAM to 384×384 batch 8
  - Validate that final run (384×384 batch 8) won't have memory issues
  - Hypothesis: Larger batch size might smooth gradients and improve convergence

  Results:

  | Metric           | Run 6 (batch 8)  | Run 7 (batch 18) | Change  |
  |------------------|------------------|------------------|---------|
  | Best Val Dice    | 0.9167           | 0.9093           | -0.0074 ❌ |

  Training Details:
  - Epochs completed: 109/120 (notebook closed accidentally)
  - Best val_dice: 0.9093 (at some epoch before 109)
  - Train Dice at epoch 109: 0.9402
  - Val Dice at epoch 109: 0.9084
  - Training time: ~2h 12m
  - Threshold optimization: NOT RUN (notebook closed before evaluation)

  Key Observations:
  - Best Val Dice DECREASED by 0.74%
  - Training-validation gap slightly larger (0.9402 - 0.9084 = 0.032 vs ~0.02 in Run 6)
  - Suggests slightly more overfitting with larger batch

  Why Larger Batch Hurt Performance:
  - Smaller batches introduce beneficial noise (stochasticity)
  - This noise helps escape sharp local minima → better generalization
  - Larger batches find sharper minima → worse generalization
  - Known phenomenon: "sharp minima generalize poorly" (Keskar et al., 2017)

  What We Learned:
  1. ✅ MEMORY TEST PASSED: 256×256 batch 18 runs without OOM
     - This confirms 384×384 batch 8 (similar memory) will be safe
  2. ❌ PERFORMANCE HYPOTHESIS FAILED: Larger batch did NOT improve dice
     - Batch size 8 remains optimal for this task
  3. ✅ Training time similar (~2 hours) despite different batch sizes
     - Fewer iterations per epoch offset by larger batches

  Conclusion: Batch size 8 is better than 18 for this task.
  Memory test passed - proceed with 384×384 batch 8 for final run.
  Run 6 remains the best configuration.

10. Run 8: Dropout Experiment ⚠️ INCONCLUSIVE

  Changes from Run 6:
  - Added: Dropout2d(p=0.2) in bottleneck
  - Batch size: 18 -> 8 (reverted to optimal)
  - NUM_EPOCHS: 120 -> 70 (shorter run for quick test)
  - T_max: 120 -> 70 (LR decays fully in 70 epochs)

  ⚠️ IMPORTANT: NO REAL JUSTIFICATION FOR DROPOUT

  We added dropout purely as an experiment to see what would happen.
  There was NO evidence of overfitting that would justify dropout:
  - Run 6 train/val gap was only ~2-3% (healthy, not overfitting)
  - Model was already well-regularized by data augmentation
  - Dropout is meant to fix overfitting, which we didn't have

  This was an exploratory test, not a hypothesis-driven improvement.

  Results (UNFAIR initial comparison):

  | Metric           | Run 6 (120 ep) | Run 8 (70 ep) | Change  |
  |------------------|----------------|---------------|---------|
  | Mean Dice        | 0.9167         | 0.9051        | -0.0116 ❌ |
  | Median Dice      | 0.9622         | 0.9541        | -0.0081 ❌ |
  | Std Dev          | 0.1134         | 0.1238        | +0.0104 (worse) |
  | Min Dice (worst) | 0.2188         | 0.0574        | -0.1614 ❌ |
  | Optimal Thresh   | 0.50           | 0.40          | Changed |

  Training Details:
  - Epochs completed: 70 (full run)
  - Best val_dice: 0.9047
  - Training time: 1h 12m 26s
  - Final epoch: Train D=0.9210, Val D=0.9031

  ⚠️ WHY THIS COMPARISON IS UNFAIR:

  Run 6 had 120 epochs, Run 8 had only 70 epochs.
  We cannot attribute the difference to dropout alone.

  FAIR Comparison (Run 7 vs Run 8 at epoch 70):

  Using W&B charts to compare at the same epoch count:

  | Metric @ epoch 70 | Run 7 (no dropout) | Run 8 (dropout) |
  |-------------------|--------------------|-----------------|
  | Val Dice          | ~0.90              | ~0.90           |
  | Train Dice        | ~0.92              | ~0.92           |

  At the same epoch count, dropout had MINIMAL effect on val_dice.
  The curves in W&B overlap almost perfectly.

  Why LR Decayed Faster in Run 8:

  CosineAnnealingLR uses T_max to define the full cosine curve.
  - Run 7: T_max=120 → at epoch 70, LR is ~2e-5 (still decaying)
  - Run 8: T_max=70 → at epoch 70, LR is ~1e-6 (at minimum)

  Run 8's LR was exhausted at epoch 70, while Run 7 could still learn.

  Key Observations:
  1. Dropout showed no benefit at equal epoch counts
  2. The apparent performance drop was due to fewer epochs, not dropout
  3. Train dice was slightly lower with dropout (expected - regularization)
  4. No evidence that dropout helps when overfitting isn't present

  What We Learned:
  1. ⚠️ Don't add regularization without evidence of overfitting
  2. ⚠️ Fair comparisons require equal training epochs
  3. ⚠️ T_max affects LR decay rate - must match NUM_EPOCHS
  4. ✅ Dropout doesn't break anything, just doesn't help here

  Conclusion: Dropout experiment was INCONCLUSIVE due to unfair comparison.
  At equal epochs, dropout showed no significant effect.
  Since there was no overfitting to fix, dropout was unnecessary.
  Run 6 remains the best configuration.

11. Run 9: 384×384 Resolution + 400 Epochs ✅ BEST MEAN DICE

  Changes from Run 6:
  - Image size: 256×256 -> 384×384
  - NUM_EPOCHS: 120 -> 400
  - T_max: 120 -> 400 (full cosine decay over 400 epochs)

  Rationale:
  - Higher resolution captures more detail from original 800×800 images
  - Memory validated in Run 7 (256×256 batch 18 ≈ 384×384 batch 8)
  - 400 epochs allows full exploration with smooth LR decay
  - Research suggested this might overfit, but we tested anyway

  Results:

  | Metric           | Run 6 (256×256, 120ep) | Run 9 (384×384, 400ep) | Change  |
  |------------------|------------------------|------------------------|---------|
  | Mean Dice        | 0.9167                 | 0.9352                 | +0.0185 ✅✅ |
  | Median Dice      | 0.9622                 | 0.9732                 | +0.0110 ✅ |
  | Std Dev          | 0.1134                 | 0.0981                 | -0.0153 (better) ✅ |
  | Min Dice (worst) | 0.2188                 | 0.1610                 | -0.0578 ❌ |
  | Max Dice         | 0.9962                 | 0.9969                 | +0.0007 ✅ |
  | Optimal Thresh   | 0.50                   | 0.35                   | Changed |

  Training Details:
  - Epochs completed: 400 (full run)
  - Best val_dice: ~0.935
  - Smooth LR decay from 1e-4 to 1e-6 over 400 epochs
  - Training time: ~13-15 hours

  Key Observations:
  1. ✅ Mean Dice improved DRAMATICALLY: +1.85 percentage points
  2. ✅ Median improved: +1.1 percentage points
  3. ✅ Standard deviation decreased (more consistent predictions)
  4. ❌ Worst case REGRESSED: 0.2188 → 0.1610 (-26%)
  5. Optimal threshold shifted DOWN from 0.50 to 0.35 (model less confident)

  Why Mean Dice Improved So Much:
  - Higher resolution (384×384) captures finer details
  - More epochs allow better convergence
  - The combination amplified benefits of both changes
  - 400 epochs did NOT cause overfitting (contrary to research suggestions)

  Why Worst Case Got Worse:
  - The same problematic images (257, 283, 7) remain difficult
  - Higher resolution may have introduced noise in edge cases
  - Model optimized for average performance, not outliers
  - BCEDiceLoss doesn't specifically target hard examples

  Worst Images Analysis:
  - Index 198: 0.1610 (new worst case)
  - Index 257: 0.1874 (was worst in Run 6 too)
  - Index 283: 0.3288 (was #2 worst in Run 6)
  - Index 7: 0.4228 (was #4 worst in Run 6)
  - These are inherently difficult images that need special handling

  Research Was WRONG About:
  - ❌ "400 epochs will cause overfitting" - It didn't
  - ❌ "Use 150 epochs max" - 400 worked much better
  - ❌ "Convergence happens around 120 epochs" - Model kept improving

  What We Learned:
  1. ✅ Higher resolution + more epochs = significant improvement
  2. ✅ 400 epochs is viable for this task (no overfitting)
  3. ❌ Average metrics can improve while worst-case regresses
  4. ⚠️ Need Focal Tversky Loss or similar to address outliers

  Conclusion: Run 9 is the BEST for Mean Dice (0.9352).
  However, the worst-case regression (0.2188 → 0.1610) is concerning.

  Next Step: Implement Focal Tversky Loss in a 120-epoch test run
  to see if it can improve worst-case performance without sacrificing mean.

12. Run 10: Focal Tversky Loss Test ❌ FAILED

  Changes from Run 9:
  - Loss: BCEDiceLoss -> FocalTverskyLoss(alpha=0.3, beta=0.7, gamma=0.75)
  - NUM_EPOCHS: 400 -> 120 (quick test)
  - T_max: 400 -> 120

  Hypothesis: Focal Tversky Loss would improve worst-case performance by
  focusing on hard examples (false negatives penalized more with beta=0.7).

  Results - Fair Comparison at Epoch 120:

  | Metric     | Run 9 (BCEDiceLoss) | Run 10 (Focal Tversky) | Change  |
  |------------|---------------------|------------------------|---------|
  | val_dice   | 0.9202              | 0.9104                 | -0.0098 ❌ |
  | train_dice | 0.9345              | 0.9264                 | -0.0081 |
  | val_loss   | 0.1057              | 0.1279                 | +0.0222 (worse) |

  Final Validation Results (Run 10 @ 120 epochs):

  | Metric           | Run 10 Value |
  |------------------|--------------|
  | Mean Dice        | 0.9112       |
  | Median Dice      | 0.9527       |
  | Std Dev          | 0.1186       |
  | Min Dice (worst) | 0.0456 ❌    |
  | Max Dice         | 0.9968       |
  | Optimal Thresh   | 0.75         |

  Worst Case Comparison:

  | Run    | Min Dice | Change from Run 9 |
  |--------|----------|-------------------|
  | Run 9  | 0.1610   | (baseline)        |
  | Run 10 | 0.0456   | -72% ❌❌❌        |

  Training Time Comparison:

  | Run    | Duration | Epochs | Time/Epoch |
  |--------|----------|--------|------------|
  | Run 9  | 10h 47m  | 400    | 97.0 sec   |
  | Run 10 | 3h 31m   | 120    | 105.5 sec  |

  Focal Tversky Loss is ~8.8% SLOWER per epoch than BCEDiceLoss.

  Why Focal Tversky Loss FAILED:

  1. The hypothesis was wrong for this dataset
     - Hard examples weren't being "ignored" by BCEDiceLoss
     - BCEDiceLoss was already handling them reasonably well

  2. Focal modulation may have been too aggressive
     - gamma=0.75 focuses heavily on very hard examples
     - This may have destabilized training for edge cases

  3. Different optimal threshold (0.75 vs 0.35)
     - The model learned very different confidence patterns
     - Higher threshold suggests less confident predictions overall

  Key Observations:
  1. ❌ Worst case got MUCH worse: 0.1610 → 0.0456 (-72%)
  2. ❌ Mean performance at 120 epochs: 0.9202 → 0.9104 (-1%)
  3. ❌ Training is ~9% slower per epoch
  4. ❌ Optimal threshold shifted drastically (0.35 → 0.75)

  Conclusion: Focal Tversky Loss FAILED to improve worst-case performance.
  The hypothesis that it would help hard examples was WRONG for this dataset.
  BCEDiceLoss remains the better choice.

  Lesson Learned: Not all "advanced" loss functions improve results.
  The original BCEDiceLoss (0.3/0.7) was already well-suited for this task.

13. Run 11: No Data Augmentation Test ❌ FAILED - OVERFITTING

  Changes from Run 9:
  - Data Augmentation: REMOVED (only resize + normalize)
  - NUM_EPOCHS: 400 -> 120 (quick test)
  - T_max: 400 -> 120
  - Loss: BCEDiceLoss (0.3/0.7) - kept from Run 9

  Hypothesis: Data augmentation might be creating unrealistic training samples
  that hurt worst-case performance. Testing if removing it helps.

  Results - Comparison at Epoch 120:

  | Metric     | Run 9 @ 120ep | Run 11 @ 120ep | Change  |
  |------------|---------------|----------------|---------|
  | val_dice   | 0.9202        | 0.9127         | -0.0075 ❌ |
  | Min Dice   | 0.1610*       | 0.0466         | -71% ❌❌❌ |
  | Median     | ~0.96         | 0.9628         | Similar |
  | Std Dev    | ~0.10         | 0.1254         | Worse |
  | Threshold  | 0.35          | 0.45           | Changed |

  *Run 9 min at 400ep, but the trend is clear

  Final Validation Results (Run 11 @ 120 epochs):

  | Metric           | Run 11 Value |
  |------------------|--------------|
  | Mean Dice        | 0.9127       |
  | Median Dice      | 0.9628       |
  | Std Dev          | 0.1254       |
  | Min Dice (worst) | 0.0466 ❌    |
  | Max Dice         | 0.9976       |
  | Optimal Thresh   | 0.45         |

  Why It FAILED - Classic Overfitting:

  Looking at W&B charts:
  - train_loss: Dropped to near 0 (model memorizing training data)
  - val_loss: Started INCREASING around epoch 100-120 (classic overfit signal)
  - train_dice: Reached ~0.97+ (higher than Run 9's ~0.95)
  - val_dice: Plateaued then started declining

  The smoking gun: val_loss SPIKED UP at the end while train_loss kept decreasing.
  This is textbook overfitting behavior.

  Without augmentation:
  1. Model memorized training set (train_dice ~0.97, train_loss near 0)
  2. Stopped generalizing to validation (val_loss started increasing)
  3. Worst cases collapsed catastrophically (min_dice 0.0466)

  Key Observations:
  1. ❌ Mean dice WORSE: 0.9202 → 0.9127 (-0.75%)
  2. ❌ Worst case CATASTROPHIC: ~0.16 → 0.0466 (-71%)
  3. ❌ Clear overfitting pattern in val_loss
  4. ❌ Higher train-val gap (overfitting)

  Conclusion: Data augmentation is ESSENTIAL for this task.

  The worst-case problem in Run 9 is NOT caused by augmentation.
  Augmentation prevents overfitting and helps generalization.
  The problematic images are just inherently difficult.

  What We Learned:
  1. ✅ Data augmentation is CRITICAL - removing it causes overfitting
  2. ✅ Worst-case issues are NOT from augmentation
  3. ✅ Even 120 epochs can overfit without augmentation
  4. ❌ This hypothesis was completely wrong

14. Otsu Per-Image Thresholding Test ❌ NOT WORTH IT (No Retraining)

  Test Type: Inference-time optimization (no retraining required)
  Model Used: Run 9's best_model.pth (Mean Dice 0.9352)

  Hypothesis: Per-image adaptive thresholding using Otsu's method might improve
  results compared to a fixed global threshold (0.35).

  Results:

  | Metric      | Fixed (0.35) | Otsu Per-Image | Change    |
  |-------------|--------------|----------------|-----------|
  | Mean Dice   | 0.9352       | 0.9349         | -0.03% ❌ |
  | Median Dice | 0.9732       | 0.9718         | -0.14%    |
  | Min Dice    | 0.1609       | 0.1678         | +0.69% ✅ |
  | Std Dice    | 0.0981       | 0.0978         | -0.3%     |

  Otsu Threshold Distribution:
  - Mean: 0.4924
  - Min: 0.3804
  - Max: 0.5804

  Worst 5 Images Comparison:
  - Fixed: [0.161, 0.187, 0.329, 0.423, 0.530]
  - Otsu:  [0.168, 0.196, 0.330, 0.423, 0.532]

  Why Otsu Didn't Help Much:
  1. Fixed threshold (0.35) was already optimized on validation set
  2. Otsu can't beat a globally tuned threshold for homogeneous data
  3. Small improvement in worst case (+0.69%) not worth the complexity
  4. Mean Dice actually got slightly WORSE (-0.03%)

  Conclusion: Per-image Otsu thresholding is NOT worth using.
  The fixed threshold 0.35 remains the best choice.
  The marginal worst-case improvement doesn't justify added complexity.

15. Multi-scale TTA Test ❌ NOT WORTH IT - HURTS WORST CASE (No Retraining)

  Test Type: Inference-time optimization (no retraining required)
  Model Used: Run 9's best_model.pth (Mean Dice 0.9352)

  Hypothesis: Running inference at multiple scales (0.75x, 1.0x, 1.25x) and
  averaging predictions might improve results by capturing both fine details
  and global context.

  Scales Tested:
  - 0.75x = 288×288
  - 1.0x = 384×384 (original)
  - 1.25x = 480×480

  Results:

  | Metric      | Single (1.0x) | TTA (3 scales) | Change    |
  |-------------|---------------|----------------|-----------|
  | Mean Dice   | 0.9352        | 0.9370         | +0.18% ✅ |
  | Median Dice | 0.9732        | 0.9738         | +0.06%    |
  | Min Dice    | 0.1609        | 0.1531         | -4.88% ❌ |
  | Std Dice    | 0.0981        | 0.0981         | same      |

  Per-image Analysis:
  - Images improved: 171/426 (40%)
  - Images hurt: 96/426 (23%)
  - Images unchanged: 159/426 (37%)

  Worst 5 Images Comparison:
  - Single: [0.161, 0.187, 0.329, 0.423, 0.530]
  - TTA:    [0.153, 0.194, 0.317, 0.424, 0.554]

  Why TTA HURT Worst Cases:
  1. Model was trained at 384×384 - other scales are out-of-distribution
  2. Averaging with wrong-scale predictions dilutes correct predictions
  3. Difficult images have features at specific scales that get averaged away
  4. The very worst image got worse (0.1609 → 0.1531)

  Conclusion: Multi-scale TTA is NOT worth using.
  - Tiny mean improvement (+0.18%) not worth 3x inference time
  - CRITICAL: Worst case got WORSE (-4.88%)
  - This is opposite of our goal (improve worst case)

16. Morphological Post-Processing Test ✅ HELPS WORST CASE (No Retraining)

  Test Type: Inference-time optimization (no retraining required)
  Model Used: Run 9's best_model.pth (Mean Dice 0.9352)

  Hypothesis: Morphological operations (opening, closing, remove small objects,
  fill holes) might clean up noisy predictions and improve edge cases.

  Operations Applied:
  - Opening (erosion → dilation): removes small noise/islands
  - Closing (dilation → erosion): fills small holes
  - Remove small objects: eliminate regions < 100 pixels
  - Fill small holes: fill holes < 100 pixels inside mask

  Parameters:
  - Kernel size: 3 (disk radius)
  - Min object size: 100 pixels
  - Max hole size to fill: 100 pixels

  Results:

  | Metric      | Raw (threshold) | With Morph | Change     |
  |-------------|-----------------|------------|------------|
  | Mean Dice   | 0.9352          | 0.9356     | +0.04%     |
  | Median Dice | 0.9732          | 0.9728     | -0.04%     |
  | Min Dice    | 0.1609          | 0.1754     | +8.96% ✅✅ |
  | Std Dice    | 0.0981          | 0.0976     | -0.5% (better) |

  Per-image Analysis:
  - Images improved: 105/426 (25%)
  - Images hurt: 64/426 (15%)
  - Images unchanged: 257/426 (60%)

  Worst 5 Images Comparison:
  - Raw:   [0.161, 0.187, 0.329, 0.423, 0.530]
  - Morph: [0.175, 0.192, 0.329, 0.423, 0.531]

  Same worst images: [198, 257, 283, 7, 97] - order unchanged

  Why Morphological Processing HELPED Worst Cases:
  1. Difficult images likely had fragmented/noisy predictions
  2. Opening removed small false positive islands
  3. Closing filled small holes inside the mask
  4. Cleaning up predictions improved Dice score on edge cases

  Comparison of All Inference-Time Techniques:

  | Technique          | Mean Change | Worst Change | Verdict |
  |--------------------|-------------|--------------|---------|
  | Otsu Threshold     | -0.03%      | +0.69%       | ❌ Not worth it |
  | Multi-scale TTA    | +0.18%      | -4.88%       | ❌ Hurts worst case |
  | **Morphological**  | **+0.04%**  | **+8.96%**   | ✅ **BEST** |

  Conclusion: Morphological post-processing is the ONLY inference-time
  technique that improves the worst case without hurting mean performance.

  **This is the first technique to actually improve worst case performance!**

  Note: This test was run on validation set only. To use for final submission,
  would need to modify the test inference cells (62-64) to apply morphological
  operations before RLE encoding.

  **Decision: NOT adding to notebook permanently (yet)**

  Morphological post-processing is a "band-aid" that helps Run 9's noisy predictions.
  Run 12 (Smart Augmentation + Dropout) might produce cleaner predictions that
  don't need this fix. Plan:
  1. First train Run 12 with smart augmentation
  2. Test if morphological still helps on new model
  3. Only add permanently if still beneficial

  The +8.96% worst-case improvement might disappear if the new model is better
  at edge cases from the start (removing ElasticTransform should help edges).

---

## Design Decision: Early Stopping DISABLED

### Why We Don't Use Early Stopping

**Historical Evidence from Our Experiments:**

| Run | Early Stopping | Result |
|-----|----------------|--------|
| Run 2 | patience=10 | Stopped at epoch 61 (out of 70) |
| Run 4 | patience=20 | Stopped at epoch 84 (out of 100) - killed best potential |
| Run 5 | **DISABLED** | Full 120 epochs → Mean Dice +0.0069 |
| Run 6 | **DISABLED** | Full 120 epochs → Worst case improved +148% |
| Run 9 | **DISABLED** | Full 400 epochs → Mean Dice 0.9352 (BEST) |

**Conclusion:** Every time we disabled early stopping, performance improved.

### Why CosineAnnealingLR Makes Early Stopping Unnecessary

CosineAnnealingLR provides **natural convergence** without needing early stopping:

```
LR Schedule (T_max=600):
Epoch 0:   LR = 1e-4  (maximum)
Epoch 300: LR = 5e-5  (midpoint)
Epoch 600: LR = 1e-6  (minimum, eta_min)
```

The LR decays smoothly to near-zero, so the model naturally stops learning aggressively.
No need for early stopping to prevent overfitting - the LR decay handles it.

### Robust Checkpoint System Protects Against Degradation

**Hypothetical worst-case scenario:**
- Epoch 60: val_dice = 0.95 (all-time high) → `best_model.pth` saved
- Epoch 70: val_dice drops to 0.85 → best_model.pth NOT overwritten
- Epoch 600: val_dice = 0.70 (model degraded) → `last_checkpoint.pth` saved

**When generating submission.csv:**
- Inference code explicitly loads `best_model.pth` (epoch 60, 0.95)
- Submission reflects best performance, not final degraded state

**Code protection:**
```python
# Training loop - only saves when val_dice improves
if val_dice > best_val_dice:
    best_val_dice = val_dice
    save_checkpoint(..., MODELS_DIR / 'best_model.pth')

# Inference - always loads best model
checkpoint = torch.load(MODELS_DIR / 'best_model.pth')
model.load_state_dict(checkpoint['model_state_dict'])
print(f"Modelo cargado desde época {checkpoint['epoch']}, Val Dice: {checkpoint['val_dice']}")
```

### Summary: Why This Design Is Better

| Approach | Risk | Mitigation |
|----------|------|------------|
| Early Stopping | Premature termination kills potential gains | None - run ends |
| **Fixed Epochs + Best Checkpoint** | Model might degrade late | `best_model.pth` preserves peak performance |

**Our approach:** Let the model train fully with CosineAnnealingLR's natural decay.
If performance degrades, we still have the best checkpoint saved.
This is strictly better than early stopping which would have killed Runs 5, 6, and 9 prematurely.

---

## Next Steps: Dataset-Aware Augmentation Analysis

### Dataset Characteristics (Manual Review)

We reviewed actual training images to understand what augmentations match the data:

| Observation | Evidence | Current Augmentation | Problem |
|-------------|----------|---------------------|---------|
| All people UPRIGHT | 9/9 images reviewed | VerticalFlip(p=0.3) | 30% upside-down people - NEVER in real data |
| HIGH quality photos | Professional/semi-pro | GaussNoise(p=0.2) | Only ~3% of images have noise |
| EXTREME lighting variety | Silhouettes, studio, outdoor | Brightness(p=0.3) | Should be HIGHER priority |
| Realistic poses only | Natural human movements | ElasticTransform(p=0.3) | Distorts body shapes unrealistically |
| People mostly upright | Slight tilts only | rotate_limit=30 | Too aggressive for humans |

### Dataset Size Analysis

| Dataset | Training Images | Augmentation Need |
|---------|-----------------|-------------------|
| Original U-Net paper | ~30 | HEAVY |
| **Our dataset** | **2133** | **MODERATE** |
| Large datasets | 1M+ | LIGHT |

Run 11 proved: 2133 images is NOT enough without augmentation (overfitting at 120 epochs).
But we don't need U-Net paper's aggressive augmentation (they had 30 images).

### ✅ Run 12: Smart Augmentation + Dropout ⭐⭐⭐ BEST RUN EVER

**Status:** ✅ COMPLETED - Interrupted at epoch 570/600 but best_model.pth saved

**Hypothesis:** Current augmentation includes transforms that don't match the data distribution.
By using REALISTIC augmentation + mild dropout, we might get better generalization.

**RESULTS - BEST IN ALL METRICS:**

| Metric | Run 9 | Run 12 | Change |
|--------|-------|--------|--------|
| **Mean Dice** | 0.9352 | **0.9550** | **+2.1%** ✅✅ |
| **Median Dice** | 0.9732 | **0.9809** | **+0.8%** ✅ |
| **Std Dev** | 0.0981 | **0.0723** | **-26%** (much better) ✅ |
| **Worst Case** | 0.1610 | **0.2897** | **+80%** ✅✅✅ |
| **Best Case** | 0.9969 | **0.9970** | +0.01% |
| **Threshold** | 0.35 | **0.45** | Changed |

**Training Details:**
- Epochs completed: 570/600 (interrupted accidentally, but best checkpoint saved)
- Best val_dice: ~0.955
- Training time: ~15+ hours (extrapolated)

**Visual Dataset Analysis (5 images reviewed):**
- Image 1: Silhouette with extreme backlighting → needs CLAHE
- Image 100: Indoor natural light, person with back to camera → needs brightness variety
- Image 500: Portrait with color grading effects → needs HueSaturationValue
- Image 1500: Black & white professional portrait → needs ToGray
- Image 2000: Vibrant colors, occupational setting → needs ColorJitter
- ALL people are UPRIGHT (never inverted) in all reviewed images

**Changes Implemented:**

| Before (Run 9) | Run 12 | Reason |
|----------------|--------|--------|
| VerticalFlip(p=0.3) | **REMOVED** | Nobody upside down in dataset |
| ElasticTransform(p=0.3) | **REMOVED** | Distorts human bodies, blurs edges |
| rotate_limit=30 | **rotate_limit=15** | People are mostly upright |
| GaussNoise(p=0.2, var=10-50) | **p=0.03, var=5-20** | Only ~3% of images have noise |
| RandomBrightnessContrast(p=0.3) | **OneOf([Brightness, CLAHE, RandomGamma], p=0.6)** | Extreme lighting variety in dataset |
| (none) | **HueSaturationValue/ColorJitter (p=0.4)** | Post-processing color effects |
| (none) | **ToGray(p=0.12)** | B&W images in dataset |
| (none) | **GridDistortion/OpticalDistortion (p=0.15)** | Edge-preserving alternative to Elastic |
| No dropout | **Dropout2d(p=0.1) in bottleneck** | Paper U-Net Sec 3.1 + compensate reduced aug |

**Configuration:**
```
IMG_SIZE: 384×384
BATCH_SIZE: 8
NUM_EPOCHS: 600 (completed 570)
T_max: 600
Loss: BCEDiceLoss (0.3/0.7)
Scheduler: CosineAnnealingLR (no warm restarts)
Dropout: p=0.1 at bottleneck
Early Stopping: DISABLED
```

**Data Augmentation Visual Analysis:**

The augmentation examples show:
- ✅ No VerticalFlip - all people upright
- ✅ No ElasticTransform - no body distortions
- ✅ Subtle rotations (15°) with gray border padding
- ✅ Color tinting from HueSaturationValue/ColorJitter
- ✅ Augmentations are REALISTIC and match dataset distribution

**Worst Case Analysis - Why They Still Fail:**

| Rank | Dice | Image Description | Failure Reason |
|------|------|-------------------|----------------|
| 1 | 0.2897 | Person on red/orange rocks | **Color confusion** - rocks similar to skin |
| 2 | 0.4282 | Baby on pink blanket | **Color confusion** - pink blanket ≈ skin |
| 3 | 0.6150 | Extreme close-up of neck/hair | **Unusual framing** - partial body |
| 4 | 0.6192 | Child on beige bed/pillows | **Color confusion** - beige ≈ skin |
| 5 | 0.6359 | Woman in red dress, dark doorway | **Low light** + brown wood ≈ skin |

**Pattern:** Model learned to segment "skin-colored things" not strictly "humans".
This is the **ceiling for U-Net without attention mechanisms**.

**Why Run 12 Succeeded:**

1. **Removing VerticalFlip**: No more upside-down training samples that never exist in real data
2. **Removing ElasticTransform**: Better edge preservation, no unrealistic body distortions
3. **Adding CLAHE**: Better handling of extreme lighting (silhouettes improved)
4. **Adding ToGray**: Better handling of B&W images in dataset
5. **Reduced GaussNoise**: Matches actual dataset (professional photography)
6. **Dataset-aligned augmentation**: Only augmentations that match real data distribution

**Improvement vs Expectations:**

| Expected | Actual |
|----------|--------|
| Worst case +15-25% | **+80%** ✅✅✅ |
| Mean dice +1-2% | **+2.1%** ✅ |

We **exceeded expectations** significantly, especially on worst case.

**Conclusion:**

Run 12 is the **BEST RUN** in the entire experiment history:
- Mean Dice 0.9550 (+27.3% above 0.75 requirement)
- Worst case improved from 0.1610 to 0.2897 (+80%)
- All metrics improved simultaneously
- The "smart augmentation" hypothesis was CORRECT

The remaining worst cases are **inherent dataset ambiguities** (color confusion with skin-like backgrounds), not model failures. This is near the ceiling for vanilla U-Net.

---

### 🔄 Run 13: Final Augmentation + TTA + Asymmetric LR (TO BE TESTED)

**Status:** Code changes implemented, training pending

**Changes from Run 12:**

1. **Even more improved data augmentation:**
   - Fixed B&W colorization bug (grayscale detect/restore)
   - Removed CLAHE (amplified film grain in vintage photos)
   - Removed GridDistortion/OpticalDistortion (unrealistic warping)
   - Reduced CoarseDropout from p=0.15 to p=0.05 (more conservative)
   - Increased ToGray from p=0.12 to p=0.15 (more shape-based learning)
   - Added ChannelShuffle p=0.05 (breaks color dependency)
   - Reduced GaussNoise var_limit to (2.0, 10.0)

2. **TTA (Test-Time Augmentation):**
   - HorizontalFlip averaging at inference time
   - Applied to both validation (Cell 55) and test (Cell 62)
   - Expected +1-3% Dice improvement

3. **Custom Asymmetric LR Schedule (replaces CosineAnnealingLR):**

   **Problem identified from Run 12 graphs:**
   - Epochs 0-150: Curves very jaggy/volatile (high LR, fast learning - PRODUCTIVE)
   - Epochs 300+: Curves completely flat (LR too low, epochs WASTED)
   - Standard cosine decays uniformly, but training dynamics are asymmetric
   - Old min LR (1e-6) was too low - updates became negligible

   **Solution: Two-phase LambdaLR scheduler**

   | Phase | Epochs | Decay Type | LR Range | Purpose |
   |-------|--------|------------|----------|---------|
   | 1 | 0-370 | Cosine | 1e-4 → 2.5e-5 | Fast initial learning |
   | 2 | 370-600 | Linear | 2.5e-5 → 1e-5 | Productive fine-tuning |

   **LR comparison vs old CosineAnnealingLR:**

   | Epoch | Old LR | New LR | Change |
   |-------|--------|--------|--------|
   | 0 | 1e-4 | 1e-4 | Same |
   | 100 | ~7e-5 | ~6.5e-5 | Similar |
   | 200 | ~4e-5 | ~4e-5 | Similar |
   | 370 | ~2.5e-5 | 2.5e-5 | Same |
   | 450 | ~1.2e-5 | **2e-5** | **1.7x higher** |
   | 530 | ~3e-6 | **1.4e-5** | **4.7x higher** |
   | 600 | 1e-6 | **1e-5** | **10x higher** |

   **Key insight:** Last ~200 epochs in Run 12 were essentially wasted (LR too low for meaningful updates). New schedule keeps LR productive throughout.

   **Implementation (Cell 49):**
   ```python
   def lr_lambda(epoch):
       transition_epoch = 370
       total_epochs = 600
       min_lr_factor = 0.10   # Final: 1e-4 * 0.10 = 1e-5
       mid_lr_factor = 0.25   # At 370: 1e-4 * 0.25 = 2.5e-5

       if epoch < transition_epoch:
           # Phase 1: Cosine from 1.0 -> 0.25
           progress = epoch / transition_epoch
           cosine_decay = (1 + math.cos(math.pi * progress)) / 2
           return mid_lr_factor + (1.0 - mid_lr_factor) * cosine_decay
       else:
           # Phase 2: Linear from 0.25 -> 0.10
           progress = (epoch - transition_epoch) / (total_epochs - transition_epoch)
           return mid_lr_factor - (mid_lr_factor - min_lr_factor) * progress

   scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)
   ```

**Hypothesis:** Cleaner augmentation + TTA + productive late-epoch LR should improve both mean and worst-case Dice.

