from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return None
    except Exception as e:
        print(f"Error loading the image: {e}")
        return None
    if img.format not in ['JPG', 'JPEG']:
        print(f"Error: Unsupported image format {img.format}")
    img_rgb = img.convert("RGB")
    pixels = np.array(img_rgb)
    print(pixels.shape)
    return (pixels)
