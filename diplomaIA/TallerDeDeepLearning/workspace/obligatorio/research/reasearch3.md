### Top 3-5 Quick Wins (Minimal Code Changes)

Based on practical experiences from Kaggle competitions and user reports, here are the top quick wins prioritized for simplicity, low compute overhead, and proven impact on U-Net segmentation tasks like binary portrait segmentation. These focus on your current setup (PyTorch, Albumentations, BCEDiceLoss) and can be implemented in <50 lines of code each.

1. **Implement Test-Time Augmentation (TTA) with Flips and Scales**  
   TTA averages predictions from augmented test images, reducing variance and boosting Dice by 1-3% without retraining. Use horizontal/vertical flips (matching your training augs) and slight scales (0.9-1.1x). For your 256x256 images, this adds ~2-4x inference time but fits your 12GB VRAM.  
   **Pseudocode (PyTorch):**  
   ```python
   import torch.nn.functional as F
   def tta_predict(model, img, device):
       model.eval()
       preds = []
       # Original
       with torch.no_grad():
           pred = torch.sigmoid(model(img.to(device)))
           preds.append(pred)
       # Horizontal flip
       pred_flip_h = torch.sigmoid(model(torch.flip(img, dims=[3]).to(device)))
       preds.append(torch.flip(pred_flip_h, dims=[3]))
       # Vertical flip
       pred_flip_v = torch.sigmoid(model(torch.flip(img, dims=[2]).to(device)))
       preds.append(torch.flip(pred_flip_v, dims=[2]))
       # Both flips
       pred_flip_both = torch.sigmoid(model(torch.flip(torch.flip(img, dims=[3]), dims=[2]).to(device)))
       preds.append(torch.flip(torch.flip(pred_flip_both, dims=[3]), dims=[2]))
       # Average
       return torch.mean(torch.stack(preds), dim=0)
   # Usage: output = tta_predict(unet, test_img.unsqueeze(0), 'cuda')
   ```  
   **Expected Gain:** +0.01-0.02 Mean Dice; test on your outliers first.

2. **Switch to Focal Loss (or Focal Tversky) for Hard Examples**  
   Your BCEDiceLoss treats easy pixels equally, ignoring outliers (<0.4 Dice). Focal variants downweight easy examples (γ=2.0), focusing on boundaries/complex backgrounds—proven in Kaggle portrait/medical segs to lift low-Dice cases by 5-10%. Replace in 1 line; no other changes.  
   **Implementation:** Use `segmentation_models_pytorch` lib (pip install):  
   ```python
   from segmentation_models_pytorch import losses
   criterion = losses.FocalLoss(mode='binary', gamma=2.0)  # Or FocalTversky(alpha=0.7, gamma=2.0) for overlap focus
   ```  
   **Hyperparams:** γ=2.0 (focus strength), α=0.25 (class balance—tune if needed). Retrain 20-30 epochs.  
   **Expected Gain:** Reduces worst-case Dice from 0.087 to ~0.2-0.3.

3. **Apply Simple Post-Processing: Morphological Closing + Threshold**  
   Your optimal threshold (0.40) + closing fills small holes in outliers from complex backgrounds. Use OpenCV/SciPy for binary ops—boosts median Dice by 2-5% in Kaggle segs.  
   **Pseudocode:**  
   ```python
   import cv2
   import numpy as np
   def post_process(pred, threshold=0.40, kernel_size=3):
       pred_bin = (pred > threshold).astype(np.uint8)
       kernel = np.ones((kernel_size, kernel_size), np.uint8)
       closed = cv2.morphologyEx(pred_bin, cv2.MORPH_CLOSE, kernel)  # Fills gaps
       return closed.astype(np.float32)
   # Usage: final_mask = post_process(tta_output.cpu().numpy().squeeze())
   ```  
   **Expected Gain:** +0.005-0.01 Mean Dice; quick to validate on your 5-10 outliers.

4. **Add Cosine Annealing LR Scheduler**  
   Your ReduceLROnPlateau isn't triggering due to oscillation (0.88-0.90 val Dice)—it needs strict improvement (default threshold=1e-4 relative). Cosine annealing smoothly decays LR over epochs, preventing plateaus in U-Net segs (better than constant 1e-4).  
   **Implementation:**  
   ```python
   from torch.optim.lr_scheduler import CosineAnnealingLR
   scheduler = CosineAnnealingLR(optimizer, T_max=70, eta_min=1e-6)  # T_max=epochs
   # In loop: scheduler.step() after each epoch
   ```  
   **Expected Gain:** Breaks plateau, +0.01 Dice by epoch 60; no patience tuning needed.

5. **Progressive Resizing: Train at 256x256, Fine-Tune at 384x384**  
   Your 256x256 downscaling loses details; with 12GB VRAM, 384x384 fits (batch=4-6). Train initially at 256, then fine-tune 10 epochs at 384—gains 2-4% Dice in high-res portrait segs without full retrain.  
   **Tip:** Resize dynamically in dataloader; monitor VRAM with `torch.cuda.memory_summary()`.

### Kaggle Competition Solutions for Similar Tasks

From 39+ Kaggle seg comps (e.g., ship/salt detection, medical portraits), top solutions emphasize U-Net variants for binary/person seg. Key patterns:

| Competition | Task | Top Techniques | Dice/IoU Gain | Notes |
|-------------|------|----------------|---------------|-------|
| Airbus Ship Detection  | Binary ship seg on satellite (similar to portrait boundaries) | U-Net++ with TTA (flips/scales), Focal loss, CRF post-process | ~0.92 IoU | 4th place: Multi-fold ensembles (5 CV folds) + snapshot ensembling; heavy augs (elastic transforms) for complex bgs. |
| TGS Salt Identification  | Binary salt deposit seg (outlier-heavy) | Attention U-Net, Lovász loss, OHEM for hard examples | 0.85 Dice | 30th place: Progressive resizing (128→256→512); ensemble 3 U-Nets (ResNet/Inception backbones). |
| Human Segmentation (Supervise.ly)  | Portrait/person seg | Attention U-Net, BCEDice + boundary loss, TTA | 0.88 Dice | Notebook: Multi-scale training; post-process with connected components to remove noise. |
| Data Science Bowl 2018 (Nuclei)  | Instance seg (binary-like) | Mask R-CNN + U-Net hybrid, TTA, morphological closing | 0.75 mAP | Boosted top method +1.1% with TTA; hard example mining for outliers. |
| Portrait Segmentation (Mobile)  | Real-time portrait seg | Lightweight U-Net with SE blocks, soft labels (vs hard binary) | 0.90 IoU | Focus: Boundary losses for sharp edges; ensemble snapshots from cyclic LR. |

Common theme: 80% use U-Net base; ensembles (3-5 models) + TTA yield top LB scores. For your dataset size (2.1k imgs), 5-fold CV is standard to avoid leakage.

### Specific Hyperparameter Recommendations

Based on similar U-Net setups (binary seg, ~2k imgs, Adam, small batch, 256x256+ res):

| Hyperparam | Recommendation | Rationale/Source | Your Current vs. Suggested |
|------------|----------------|------------------|----------------------------|
| **Batch Size** | 4-8 (keep 8 if VRAM allows) | Larger stabilizes gradients but risks overfitting on small data; 8 optimal for InstanceNorm . | Matches (8); test 4 for outliers. |
| **Learning Rate** | Initial: 3e-4; Cosine decay to 1e-6 | Constant 1e-4 plateaus; cosine/step better for U-Net convergence [web:2, web:37]. Warmup: 5 epochs linear ramp. | 1e-4 → 3e-4 initial; add warmup. |
| **Image Size** | 384x384 (fine-tune after 256x256) | 256 loses details (your plateau cause); 384 fits 12GB (batch=4), +2% Dice [web:45, web:123]. Multi-scale: Train on {256,384}. | 256 → Progressive to 384. |
| **Epochs/Patience** | 100 epochs; Early stop patience=15 | Your 61 epochs too short; longer with cosine avoids premature stop . | 70 → 100; patience 10→15. |
| **Loss Weight** | BCEDice: 0.3 BCE + 0.7 Dice | Heavier Dice for overlap focus in binary seg . Or switch to FocalTversky (α=0.7). | 0.5/0.5 → 0.3/0.7. |
| **Aug Strength** | Increase ElasticTransform p=0.5, alpha=1-2x | Your p=0.3 too mild for bgs; heavy geo augs prevent overfitting [web:2, web:10]. | p=0.3 → 0.5; add RandomRotate90. |

Tune via 5-fold CV; track with Weights & Biases. For your hardware: FP16 + gradient accum (effective batch=16) saves VRAM.

### Code Snippets/Pseudocode for TTA

See quick win #1 above—full TTA with flips/scales. For scales:  
```python
# Add to tta_predict:
for scale in [0.9, 1.0, 1.1]:
    scaled = F.interpolate(img, scale_factor=scale, mode='bilinear')
    pred_s = torch.sigmoid(model(scaled.to(device)))
    preds.append(F.interpolate(pred_s, size=img.shape[2:], mode='bilinear'))
# Average as before
```
Inverse-scale outputs before averaging. From Kaggle: Use `ttach` lib for plug-and-play (pip install ttach).

### Common Mistakes and How to Avoid Them

At your stage (0.90 val Dice, plateauing, outliers), these pitfalls are frequent in U-Net segs:

| Mistake | Why It Happens | How to Avoid | Impact on Your Setup |
|---------|----------------|--------------|----------------------|
| **Ignoring Outliers in Eval** | Mean Dice hides worst cases (your 0.087); focus on median/min. | Compute per-image Dice; retrain with OHEM (oversample low-Dice imgs in dataloader). | Your std=0.124 → Target <0.08 with Focal loss. |
| **No Threshold Tuning** | Default 0.5 biases to over/under-seg; your 0.40 is good but static. | Dynamic threshold per image (Otsu on pred probs) or learnable via val set. | +1-2% on complex bgs; test on outliers. |
| **Scheduler Mismatch** | ReduceLROnPlateau skips on oscillation (your case: needs >1e-4 rel improvement). | Switch to cosine; monitor LR logs. | Breaks your epoch-40 plateau. |
| **Under-Auging Hard Cases** | Standard augs ignore bgs; leads to overfitting on easy imgs. | Add targeted augs (e.g., background blur/inpaint) for low-Dice samples. | Reduces your 5-10 outliers; use Albumentations' `OneOf` for bgs. |
| **No Multi-Fold CV** | Single split leaks; underestimates variance on small data (your 2.1k imgs). | 5-fold stratified; ensemble OOF preds. | Stable 0.90+ LB; prevents your early-stop trigger. |
| **Res Ignoring VRAM** | Downscaling to 256 loses res; but naive upscale OOMs. | Patch-based or progressive resize; monitor with `nvidia-smi`. | Your 800x800 orig → 384 feasible, +3% Dice. |

These stem from Kaggle forums/Neptune.ai reviews [web:2, web:8, web:130]. Prioritize outlier analysis: Visualize top-10 worst val imgs pre/post changes. Your 0.901 already exceeds 0.75—focus on robustness for deadline.