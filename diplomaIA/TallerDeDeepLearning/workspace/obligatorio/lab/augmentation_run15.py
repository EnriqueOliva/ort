_grayscale_flag = [False]

def detect_grayscale(image, **kwargs):
    r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
    _grayscale_flag[0] = np.allclose(r, g, atol=5) and np.allclose(g, b, atol=5)
    return image

def restore_grayscale(image, **kwargs):
    if _grayscale_flag[0]:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    return image

train_transform = A.Compose([
    A.RandomResizedCrop(
        size=(IMG_SIZE, IMG_SIZE),
        scale=(0.5, 1.0),
        ratio=(1.0, 1.0),
        p=1.0
    ),

    A.Lambda(image=detect_grayscale),

    A.HorizontalFlip(p=0.5),

    A.OneOf([
        A.RandomBrightnessContrast(
            brightness_limit=0.15,
            contrast_limit=0.15,
            p=1.0
        ),
        A.RandomGamma(
            gamma_limit=(85, 115),
            p=1.0
        ),
    ], p=0.5),

    A.OneOf([
        A.HueSaturationValue(
            hue_shift_limit=8,
            sat_shift_limit=15,
            val_shift_limit=12,
            p=1.0
        ),
        A.ColorJitter(
            brightness=0.08,
            contrast=0.08,
            saturation=0.12,
            hue=0.05,
            p=1.0
        ),
        A.ChannelShuffle(p=1.0),
    ], p=0.50),

    A.ToGray(p=0.30), 

    A.Lambda(image=restore_grayscale),

    A.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),

    ToTensorV2()
])

val_transform = A.Compose([
    A.Resize(IMG_SIZE, IMG_SIZE),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2()
])

test_transform = A.Compose([
    A.Resize(IMG_SIZE, IMG_SIZE),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2()
])
