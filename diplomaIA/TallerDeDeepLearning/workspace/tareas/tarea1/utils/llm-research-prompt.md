# Research Prompt for LLM with Web Search Capability

## Context

We are working on a Deep Learning course assignment (Tarea 1) with the following constraints and situation:

### Assignment Requirements
- **Dataset**: Imagenette (10-class subset of ImageNet, 160px version)
- **Constraint**: NO pre-trained models allowed - must implement from scratch
- **Requirements**:
  - At least 2 regularization techniques
  - Report accuracy, precision, recall, f1-score
  - Show training evolution on train and validation data
  - Use Weights & Biases for experiment tracking
  - Submit as executed .ipynb notebook

### Dataset Details
- Training set: 9,469 images
- Validation set: 3,925 images
- 10 classes: tench, English springer, cassette player, chain saw, church, French horn, garbage truck, gas pump, golf ball, parachute
- Class balance: ~10% per class (well balanced)
- Image dimensions: Variable, resized to 160x160
- Normalization: ImageNet stats (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

### Hardware
- GPU: NVIDIA RTX 4070
- RAM: 64GB
- Training time budget: ~30-60 minutes per experiment is acceptable

### Current Situation

**Current Architecture**: SimpleCNN (LeNet-style)
- 3 Conv layers: 3→32→64→128 channels
- 3x3 kernels, padding=1, MaxPool2d after each conv
- 2 FC layers: 51,200→256→10
- Total params: ~13M parameters
- ReLU activations throughout

**Performance History**:

| Version | Architecture | Regularization | Train Acc | Val Acc | Gap | Status |
|---------|-------------|----------------|-----------|---------|-----|--------|
| V3 | SimpleCNN | DataAug + EarlyStopping | 86.88% | 69.68% | 17.2% | Severe overfitting |
| V4 | SimpleCNN + BatchNorm | BatchNorm + Dropout + WeightDecay + DataAug + EarlyStopping | 53.59% | 69.38% | -15.8% | Underfitting (worse than V3) |
| V5 | SimpleCNN | Dropout + DataAug + EarlyStopping | Currently training... | | | Testing incremental change |

**Key Problems**:
1. Current simple CNN architecture seems to have hit a ceiling (~70% val accuracy)
2. Severe overfitting when under-regularized (17% gap)
3. Underfitting when over-regularized
4. Struggling to break past 70% validation accuracy

**Weak Classes** (consistently low F1-scores):
- Chain saw: ~48-51% F1
- Gas pump: ~55-60% F1
- Golf ball: ~65-70% F1

### What We've Learned
- Class transcripts mention LeNet and DenseNet architectures
- Professor expects ~70%+ accuracy achievable
- Data augmentation should be moderate (≤10° rotation recommended)
- BatchNorm is standard in modern CNNs
- Dropout is effective for overfitting in FC layers

## Research Request

**Please perform web searches to answer the following questions:**

### 1. Architecture Recommendations for Imagenette/Small ImageNet Subsets

Search for:
- "best CNN architecture Imagenette dataset 2024"
- "small ImageNet subset CNN architecture from scratch"
- "CNN architecture 10 class image classification 160x160"

**Questions:**
- What architectures work well for Imagenette specifically?
- What's the typical accuracy ceiling for scratch-trained models on Imagenette?
- Are there modern lightweight architectures better than LeNet for this task?
- Should we consider ResNet-18/34 scale models? VGG-style? MobileNet-style?

### 2. Optimal Model Capacity for Our Dataset Size

Search for:
- "optimal CNN parameters 9000 training images"
- "model capacity vs dataset size deep learning"
- "how many parameters for 10k image dataset"

**Questions:**
- Is 13M parameters too much or too little for 9,469 training images?
- What's the rule of thumb for parameters vs training samples?
- Would a smaller or larger model be better?

### 3. Specific Architecture Suggestions

Search for:
- "implement ResNet from scratch PyTorch small dataset"
- "VGG architecture variations small images"
- "modern CNN architecture better than LeNet 2024"

**Questions:**
- What are concrete architectures we can implement from scratch in PyTorch?
- What are the key architectural improvements over LeNet that we should adopt?
- Which modern techniques (residual connections, inception modules, etc.) are worth implementing?

### 4. Regularization Strategies for CNNs

Search for:
- "best regularization techniques CNN overfitting 2024"
- "dropout placement CNN convolutional layers vs fully connected"
- "batch normalization placement best practices CNN"

**Questions:**
- Where exactly should we place Dropout in CNNs (after conv? after FC? both?)
- Is BatchNorm before or after activation functions? (we need the 2024 consensus)
- Should we use Dropout in conv layers or only FC layers?
- What dropout rate is optimal for conv vs FC layers?

### 5. Training Hyperparameters

Search for:
- "optimal learning rate CNN image classification"
- "batch size vs model performance CNN"
- "learning rate schedule ImageNet training"

**Questions:**
- Is 0.001 learning rate with Adam optimal, or should we adjust?
- Should we implement learning rate scheduling/decay?
- Is batch size 64 optimal for our GPU (RTX 4070) and dataset size?
- Would SGD with momentum be better than Adam for this task?

### 6. Data Augmentation Best Practices

Search for:
- "data augmentation techniques ImageNet CNN 2024"
- "optimal augmentation strength small datasets"
- "random crop vs random rotation image classification"

**Questions:**
- What data augmentation techniques are most effective for ImageNet-style datasets?
- Should we add RandomCrop, ColorJitter, RandomGrayscale, etc.?
- Is our current augmentation (flip + 10° rotation) too weak?
- What's the standard augmentation pipeline for ImageNet training in 2024?

## Output Format Requested

Please structure your response as:

### 1. Architecture Recommendation
- Specific architecture name and justification
- Expected performance range (accuracy)
- Number of parameters estimate
- Implementation complexity (easy/medium/hard)

### 2. Regularization Strategy
- Specific techniques in priority order
- Exact placement in architecture
- Hyperparameter values (dropout rates, etc.)

### 3. Training Configuration
- Learning rate and optimizer recommendation
- Batch size recommendation
- Learning rate schedule if applicable
- Number of epochs estimate

### 4. Data Augmentation Pipeline
- Specific transforms to add/remove/modify
- Recommended parameters for each transform

### 5. Expected Outcomes
- Realistic accuracy range we should aim for
- Estimated training time
- Key metrics to monitor

### 6. Implementation Complexity Assessment
- How difficult would it be to implement your recommended architecture from scratch?
- Are there simpler alternatives that might give 90% of the benefit?

## Additional Context

- We have ~3 hours left before submission deadline
- We need to document our experiments in the notebook
- We're following a scientific approach: one change at a time
- The assignment values the "story" and justification more than raw accuracy
- We have access to class transcripts mentioning LeNet and DenseNet specifically

Thank you for your research assistance!
