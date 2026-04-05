# How to Download the Imagenette Dataset

To download the Imagenette dataset using torchvision, you simply need to set `download=True` when creating the dataset object.

## Basic Usage

```python
from torchvision.datasets import Imagenette
from torchvision import transforms

# Define your data directory
data_root = './data'

# Download and load the training set
train_dataset = Imagenette(
    root=data_root,
    split='train',
    size='full',  # or '320px', '160px' for smaller versions
    download=True,  # This will download the dataset
    transform=transforms.ToTensor()
)

# Download and load the validation set
val_dataset = Imagenette(
    root=data_root,
    split='val',
    size='full',
    download=True,
    transform=transforms.ToTensor()
)

print(f"Training samples: {len(train_dataset)}")
print(f"Validation samples: {len(val_dataset)}")
print(f"Number of classes: {len(train_dataset.classes)}")
print(f"Classes: {train_dataset.classes}")
```

## Parameters Explained

- **`root`**: Directory where to save the dataset (it will create an 'imagenette2' folder inside)
- **`split`**: Either `'train'` or `'val'` for training/validation sets
- **`size`**: Choose from:
  - `'full'` - Original resolution images
  - `'320px'` - Images resized to 320px
  - `'160px'` - Images resized to 160px (fastest to download and process)
- **`download=True`**: Downloads the dataset if not already present
- **`transform`**: Apply transforms to images (e.g., normalization, augmentation)
- **`target_transform`**: Apply transforms to labels

## Important Notes

- The first time you run this, it will download the dataset (this may take a few minutes depending on your connection)
- Subsequent runs will use the already-downloaded data
- The dataset will only download once - if it's already in the `root` directory, setting `download=True` won't re-download it
- The dataset will be saved in a subfolder called 'imagenette2' inside your specified `root` directory

## Dataset Information

- **10 classes** (subset of ImageNet)
- Training set: ~9,500 images
- Validation set: ~3,900 images
- Classes include: tench, English springer, cassette player, chain saw, church, French horn, garbage truck, gas pump, golf ball, parachute
