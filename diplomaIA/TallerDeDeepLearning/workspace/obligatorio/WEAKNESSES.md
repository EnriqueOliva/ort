# U-Net Human Segmentation Analysis

## Context

This project implements U-Net for human segmentation as part of a Deep Learning course assignment. The goal is to segment people from images using a model built from scratch in PyTorch, following the original U-Net paper architecture.

### Assignment Requirements
- Implement U-Net based on the original paper (Ronneberger et al., 2015)
- Achieve Dice Coefficient ≥ 0.75 on Kaggle test set
- Justify all design decisions
- Participate in a private Kaggle competition

### Current Performance (Run 14)
| Metric | Value |
|--------|-------|
| Mean Dice | 0.9558 |
| Median Dice | 0.9819 |
| Min Dice (worst) | 0.3533 |
| Max Dice | 0.9982 |
| Std Dev | 0.0807 |

---

## Dataset

### Structure
- **Training images:** 2133 RGB images
- **Original resolution:** 800×800 pixels
- **Training resolution:** 384×384 pixels (resized)
- **Task:** Binary segmentation (person vs background)
- **Masks:** Binary (0 = background, 1 = person)

### Dataset Characteristics
| Characteristic | Observation |
|----------------|-------------|
| Image quality | Professional/semi-professional photography |
| Lighting | Extreme variety (silhouettes, studio, outdoor, low-light) |
| Subjects | Single person per image |
| Orientation | All people upright (never inverted) |
| Color variety | Full spectrum including B&W images |
| Backgrounds | Varied (indoor, outdoor, solid colors, complex scenes) |

### Class Balance
- Foreground (person) ratio varies significantly across images
- Some images have very small subjects (low foreground ratio)
- Some images have close-ups (high foreground ratio)

---

## Model Weaknesses

### 1. Color Confusion (Primary Weakness)

The model learned to segment "skin-colored pixels" rather than "human shape".

| Failure Case | Description | Dice Score |
|--------------|-------------|------------|
| Orange/red rocks | Rocks segmented as person | 0.35 |
| Pink blankets | Blanket segmented as person | 0.42 |
| Wooden textures | Wood segmented as person | 0.59 |
| Beige bedding | Bedding segmented as person | 0.62 |

**Root cause:** RGB color patterns are strong predictors during training. The model exploits color shortcuts instead of learning semantic "human" features.

### 2. B&W Image Handling

Without color information, the model relies on texture/shape but performs worse.

| Issue | Impact |
|-------|--------|
| No color cues available | Model loses primary feature |
| Texture confusion | Dark clothing blends with dark backgrounds |
| Grayscale textures | Walls, floors can look skin-like in grayscale |

### 3. White/Light Clothing Under-segmentation

The model fails to segment white clothing (e.g., bride's dress, white shirts).

**Reason:** Training data likely has more exposed skin than white clothing. The model associates "person" with skin tones, not clothing.

### 4. Object Bleeding

Objects near or touching humans get incorrectly segmented.

| Object | Reason |
|--------|--------|
| Bikes | Proximity to person, similar textures |
| Backpacks | Touching person, confused as body part |
| Teddy bears | Skin-like texture |

### 5. Mild Overfitting

| Metric | Train | Val | Gap |
|--------|-------|-----|-----|
| Dice | 0.9916 | 0.9542 | 3.9% |
| Loss | 0.0099 | 0.0633 | 6.4x |

The train-val gap indicates the model memorizes some training patterns that don't generalize.

---

## Fundamental Limitations

### Why These Weaknesses Exist

1. **No semantic understanding:** Vanilla U-Net learns pixel-level patterns, not object-level concepts like "this is a human".

2. **No pretrained features:** Building from scratch means the model must learn everything from 2133 images. Pretrained encoders (ResNet, EfficientNet) have seen millions of images and understand "human" semantically.

3. **No attention mechanisms:** The model processes all regions equally. Attention would help focus on relevant human features and ignore confusing backgrounds.

4. **BCE+Dice loss optimizes average:** The loss function doesn't specifically target hard examples. Worst cases contribute minimally to the total loss.

### Theoretical Ceiling

For vanilla U-Net without pretrained encoders or attention:
- Mean Dice: ~0.96-0.97 (achievable)
- Worst Case: ~0.40-0.50 (limited by color confusion)

The remaining failures are **inherent dataset ambiguities** that require semantic understanding to resolve.

---

## Mitigation Strategies Tested

| Strategy | Result | Impact on Worst Case |
|----------|--------|---------------------|
| Focal Tversky Loss | Failed | -72% |
| Remove augmentation | Failed (overfitting) | -71% |
| Smart augmentation | Success | +80% |
| Morphological post-processing | Helps | +9% |
| Multi-scale TTA | Hurts | -5% |
| Per-image Otsu threshold | Marginal | +0.7% |

### What Works
- Dataset-aligned augmentation (remove unrealistic transforms)
- ToGray augmentation (expose model to B&W)
- ChannelShuffle (break color dependency)
- More training epochs with proper LR decay
- Connected component filtering (remove small false positives)

### What Doesn't Work
- Focal/Tversky losses (too aggressive for this task)
- Removing augmentation (causes overfitting)
- Multi-scale TTA (hurts edge cases)
- Very low learning rates in late epochs (wasted compute)
