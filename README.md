# 🛸 Smart Earth Monitor

A multi-module satellite image analysis platform built with Streamlit and ML.

## Modules
- 🌾 **Crop Health (NDVI)** - Monitor vegetation health using NDVI
- 🌊 **Flood Mapping** - Detect flood affected areas
- 🌳 **Deforestation Detection** - Compare before/after images
- 🏗️ **Road Segmentation** - U-Net based road/building detection

## Setup
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure
```
smart_earth_monitor/
├── app.py              # Main Streamlit app
├── models/             # ML model architectures
│   ├── unet.py         # U-Net for segmentation
│   ├── flood_model.py
│   └── deforest_model.py
├── utils/              # Utility functions
│   ├── theme.py        # Dynamic color themes
│   ├── preprocess.py   # Image preprocessing
│   ├── ndvi.py         # NDVI calculation
│   └── visualize.py    # Result visualization
├── data/               # Sample satellite images
├── notebooks/          # Google Colab training notebooks
└── requirements.txt
```

## Data Sources
- Sentinel-2 (Free) - https://scihub.copernicus.eu
- Landsat 8/9 (Free) - https://earthexplorer.usgs.gov
- Google Earth Engine - https://earthengine.google.com
