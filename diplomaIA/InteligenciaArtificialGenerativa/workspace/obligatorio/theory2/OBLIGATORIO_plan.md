# WGAN-GP Obligatorio Plan

## Objective
Validate WGAN-GP's improvements over WGAN (weight clipping vs gradient penalty)

## Setup
- **Dataset:** CIFAR-10 (32×32 RGB)
- **Architecture:** DCGAN
  - Generator: ConvTranspose + BatchNorm + ReLU
  - Critic: Conv + LeakyReLU (**NO BatchNorm** - critical for showing differences)
- **Methods compared:** WGAN (weight clipping) vs WGAN-GP (gradient penalty)

## Experiments

### Exp 1: Training Speed & Quality ⭐⭐⭐
- Train WGAN (c=0.01) and WGAN-GP (λ=10)
- Measure: FID score, loss curves, visual samples
- Expected: WGAN-GP converges faster and more stable

### Exp 3: Gradient Behavior ⭐⭐
- Log gradient norms per layer during training
- Expected: WGAN shows explosion/vanishing, WGAN-GP stable

### Exp 4: Hyperparameter Sensitivity ⭐⭐
- WGAN: c ∈ {0.001, 0.01, 0.1}
- WGAN-GP: λ ∈ {1, 10, 100}
- Expected: WGAN high variance in FID, WGAN-GP low variance

### Exp 5: Weight Distribution ⭐
- Histogram of critic weights after training
- Expected: WGAN clusters at ±c boundaries, WGAN-GP natural distribution

## Training Runs Required
1. WGAN (c=0.01) - main
2. WGAN-GP (λ=10) - main
3. WGAN (c=0.001) - sensitivity
4. WGAN (c=0.1) - sensitivity
5. WGAN-GP (λ=1) - sensitivity
6. WGAN-GP (λ=100) - sensitivity

**Total: 6 runs** (~12-18 GPU hours on RTX 4070)

## Flow Diagram

```
START
  │
  │   Architecture: DCGAN, NO BatchNorm in Critic
  │   Dataset: CIFAR-10
  │
  ├─► Train WGAN (c=0.01) ──────┐
  │     • Log losses            │
  │     • Log gradient norms    ├─► Exp 1, 3, 5
  │     • Calculate FID         │
  │                             │
  ├─► Train WGAN-GP (λ=10) ─────┘
  │     • Same metrics
  │
  ├─► WGAN (c=0.001, c=0.1) ────┐
  │                             ├─► Exp 4
  ├─► WGAN-GP (λ=1, λ=100) ─────┘
  │
  └─► DONE
```

## Key Implementation Details
- Use Adam for WGAN-GP (lr=0.0001, betas=(0, 0.9))
- Use RMSProp for WGAN (lr=0.00005)
- Critic iterations per generator: ncritic=5
- Gradient penalty coefficient: λ=10 (default)
- Weight clipping: c=0.01 (default)

## Deliverables
- Single Jupyter notebook (.ipynb)
- Visualizations: FID curves, gradient plots, weight histograms
- Final report with analysis

