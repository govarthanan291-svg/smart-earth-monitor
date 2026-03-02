import numpy as np
from PIL import Image
import io

def load_image(uploaded_file):
    """Load uploaded image and return as numpy array"""
    try:
        img = Image.open(uploaded_file)
        img_array = np.array(img)
        return img_array
    except Exception as e:
        try:
            import rasterio
            with rasterio.open(uploaded_file) as src:
                img_array = src.read()
                img_array = np.moveaxis(img_array, 0, -1)
            return img_array
        except:
            return None

def normalize_image(img_array):
    """Normalize image to 0-255 range"""
    if img_array is None:
        return None
    img_min = img_array.min()
    img_max = img_array.max()
    if img_max == img_min:
        return np.zeros_like(img_array, dtype=np.uint8)
    normalized = ((img_array - img_min) / (img_max - img_min) * 255).astype(np.uint8)
    return normalized

def resize_image(img_array, size=(512, 512)):
    """Resize image to given size"""
    img = Image.fromarray(img_array.astype(np.uint8))
    img_resized = img.resize(size)
    return np.array(img_resized)
