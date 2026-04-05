# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment Setup

This is a Deep Learning workshop course repository using PyTorch for neural network implementations and experiments.

### Creating the Conda Environment
```bash
conda env create -f environment.yml
conda activate taller-dl
```

The environment includes:
- Python >=3.12
- PyTorch (including torchvision, torchaudio)
- Scientific computing: numpy, pandas, scikit-learn, matplotlib
- Deep learning tools: wandb (experiment tracking), torchviz (graph visualization), torchinfo
- NLP libraries: nltk
- Dataset access: kaggle

### Jupyter Notebooks
Work is done in Jupyter notebooks (.ipynb files). Use:
```bash
jupyter notebook
# or
jupyter lab
```

## Course Structure

This is "Taller de Deep Learning" (Deep Learning Workshop) - a practical, hands-on course.

### Evaluation System
- 2 Labs (15% each)
- 1 Exam (20%)
- Final Project (50%)
- Kaggle competition for best project

### Assignment Requirements (Tarea_1-letra.ipynb)

**Task**: Image classification using the Imagenette dataset (10-class subset of ImageNet)

**Key Constraints**:
- **No pre-trained models allowed** - all models must be implemented from scratch
- Must use at least 2 regularization techniques (Dropout, BatchNorm, Data Augmentation, etc.)
- Requires data analysis section including class balance analysis
- All preprocessing decisions must be justified based on data exploration

**Required Metrics**: accuracy, precision, recall, f1-score

**Training Visualization**: Must show model evolution on both train and validation data

**Experiment Tracking**: Must use Weights & Biases (wandb) to log experiments with detailed graphs, logs, and model comparisons

**Deliverable Format**: .ipynb file with all cells already executed

## Course Topics Covered

### Fundamentals (Class 1 - 20-08-2025)
- PyTorch tensors: creation, properties, operations
- GPU acceleration and device management
- Broadcasting rules
- Indexing, slicing, and tensor manipulation
- Computational efficiency considerations

### Neural Networks (Class 2 - 27-08-2025)
- Perceptron implementation (AND, OR, NOT gates)
- XOR problem and linear separability limitations
- Multi-layer networks (MLP) using nn.Linear and nn.Sequential
- Activation functions (sigmoid, sign)
- Training loops: forward pass, loss calculation (MSE), backward pass
- Optimizers (SGD, Adam)
- Computational graphs (require_grad, detach, no_grad)

## Development Workflow

### Working with Notebooks
- All coursework is in .ipynb format
- Notebooks may contain exercises marked as "⚠️ Asignado" (assigned)
- Execute cells sequentially to avoid state issues
- Always include outputs in final submissions

### GPU vs CPU Execution
- Environment supports both CUDA and non-CUDA configurations
- Use `torch.cuda.is_available()` to detect GPU availability
- Move tensors to GPU with `.to(device)` for ~15x speedup on matrix operations
- Recommended platforms: Google Colab, faculty servers, or local GPU

### Experiment Tracking with wandb
Initialize in notebooks:
```python
import wandb
wandb.login()
wandb.init(project="project-name")
# Log metrics during training
wandb.log({"loss": loss, "accuracy": acc})
```

## Architecture Patterns

### From-Scratch Model Implementation
Models must be built using PyTorch primitives without pre-trained weights:
```python
model = nn.Sequential(
    nn.Linear(input_size, hidden_size),
    nn.Sigmoid(),
    nn.Linear(hidden_size, output_size)
)
```

### Training Loop Structure
```python
model.train()
for epoch in range(epochs):
    # Forward pass
    outputs = model(inputs)
    loss = criterion(outputs, targets)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

### Data Preprocessing
- Decisions on transforms and augmentation must be data-driven
- Include exploratory data analysis (EDA) section
- Document class imbalance and mitigation strategies
- Use torchvision.transforms for image preprocessing
