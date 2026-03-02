import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from utils.ndvi import classify_ndvi

def show_result(data, module="ndvi"):
    if module == "ndvi":
        show_ndvi_result(data)
    elif module == "flood":
        show_flood_result(data)
    elif module == "deforest":
        show_deforest_result(data)
    elif module == "road":
        show_road_result(data)

def show_ndvi_result(img_array):
    from utils.ndvi import calculate_ndvi, classify_ndvi
    ndvi = calculate_ndvi(img_array)
    if ndvi is None:
        st.error("Could not process image. Please upload a valid image.")
        return

    ndvi_map, percentages = classify_ndvi(ndvi)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🗺️ NDVI Map")
        fig, ax = plt.subplots(figsize=(6, 5))
        cmap = plt.get_cmap("RdYlGn")
        im = ax.imshow(ndvi, cmap=cmap, vmin=-1, vmax=1)
        plt.colorbar(im, ax=ax, label="NDVI Value")
        ax.set_title("NDVI Heatmap")
        ax.axis("off")
        st.pyplot(fig)
        plt.close()

    with col2:
        st.subheader("📊 Vegetation Stats")
        for category, pct in percentages.items():
            st.metric(label=category, value=f"{pct}%")

def show_flood_result(img_array):
    if img_array is None:
        st.error("Could not process image.")
        return
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📸 Original Image")
        if img_array.dtype != np.uint8:
            img_array = ((img_array - img_array.min()) / (img_array.max() - img_array.min()) * 255).astype(np.uint8)
        st.image(img_array[:,:,:3] if img_array.ndim == 3 and img_array.shape[2] >= 3 else img_array)
    
    with col2:
        st.subheader("🌊 Flood Detection")
        # Simple water detection using blue channel
        if img_array.ndim == 3:
            blue = img_array[:,:,2].astype(float)
            red = img_array[:,:,0].astype(float)
            water_mask = (blue > red * 1.2).astype(np.uint8) * 255
            fig, ax = plt.subplots(figsize=(6,5))
            ax.imshow(water_mask, cmap="Blues")
            ax.set_title("Detected Water/Flood Areas")
            ax.axis("off")
            st.pyplot(fig)
            plt.close()
            flood_pct = round((water_mask > 0).sum() / water_mask.size * 100, 2)
            st.metric("Flood Affected Area", f"{flood_pct}%")

def show_deforest_result(data):
    img_before, img_after = data
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🌳 Before")
        if img_before.dtype != np.uint8:
            img_before = ((img_before - img_before.min()) / (img_before.max() - img_before.min()) * 255).astype(np.uint8)
        st.image(img_before[:,:,:3] if img_before.ndim == 3 and img_before.shape[2] >= 3 else img_before)
    with col2:
        st.subheader("🔥 After")
        if img_after.dtype != np.uint8:
            img_after = ((img_after - img_after.min()) / (img_after.max() - img_after.min()) * 255).astype(np.uint8)
        st.image(img_after[:,:,:3] if img_after.ndim == 3 and img_after.shape[2] >= 3 else img_after)
    with col3:
        st.subheader("📊 Change Map")
        if img_before.shape == img_after.shape:
            diff = np.abs(img_before.astype(int) - img_after.astype(int)).mean(axis=2) if img_before.ndim == 3 else np.abs(img_before.astype(int) - img_after.astype(int))
            fig, ax = plt.subplots(figsize=(5,5))
            ax.imshow(diff, cmap="Reds")
            ax.set_title("Change Detected")
            ax.axis("off")
            st.pyplot(fig)
            plt.close()

def show_road_result(img_array):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📸 Original Image")
        if img_array.dtype != np.uint8:
            img_array = ((img_array - img_array.min()) / (img_array.max() - img_array.min()) * 255).astype(np.uint8)
        st.image(img_array[:,:,:3] if img_array.ndim == 3 and img_array.shape[2] >= 3 else img_array)
    with col2:
        st.subheader("🏗️ Segmentation (U-Net)")
        st.info("🔄 U-Net model integration coming soon!\n\nTrain your model in Google Colab notebook and load weights here.")
        st.markdown("**Steps:**\n1. Train U-Net in `notebooks/training.ipynb`\n2. Save model weights to `models/`\n3. Load and predict here!")
