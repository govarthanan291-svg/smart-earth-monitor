import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def calculate_ndvi(img_array):
    """
    Calculate NDVI from image array
    For RGB images: uses Red channel as proxy
    For multispectral: uses NIR (band 4) and Red (band 3)
    NDVI = (NIR - Red) / (NIR + Red)
    """
    if img_array is None:
        return None
    
    if img_array.ndim == 3:
        if img_array.shape[2] >= 4:
            # Multispectral - use NIR (band 4) and Red (band 3)
            nir = img_array[:, :, 3].astype(float)
            red = img_array[:, :, 2].astype(float)
        else:
            # RGB - use Green as proxy for NIR, Red channel
            nir = img_array[:, :, 1].astype(float)  # Green as NIR proxy
            red = img_array[:, :, 0].astype(float)
    else:
        return None

    # Avoid division by zero
    denominator = nir + red
    denominator[denominator == 0] = 1

    ndvi = (nir - red) / denominator
    return ndvi

def classify_ndvi(ndvi):
    """Classify NDVI values into categories"""
    if ndvi is None:
        return None, {}
    
    categories = {
        "Water/No Vegetation": (ndvi < 0).sum(),
        "Bare Soil": ((ndvi >= 0) & (ndvi < 0.2)).sum(),
        "Sparse Vegetation": ((ndvi >= 0.2) & (ndvi < 0.4)).sum(),
        "Moderate Vegetation": ((ndvi >= 0.4) & (ndvi < 0.6)).sum(),
        "Dense/Healthy Vegetation": (ndvi >= 0.6).sum()
    }
    
    total = ndvi.size
    percentages = {k: round((v/total)*100, 2) for k, v in categories.items()}
    return ndvi, percentages
