import streamlit as st
from utils.theme import apply_theme
from utils.preprocess import load_image
from utils.ndvi import calculate_ndvi
from utils.visualize import show_result

st.set_page_config(
    page_title="Smart Earth Monitor 🌍",
    page_icon="🛸",
    layout="wide"
)

# Sidebar
st.sidebar.title("🛸 Smart Earth Monitor")
st.sidebar.markdown("---")
module = st.sidebar.selectbox(
    "Select Module",
    ["🌾 Crop Health (NDVI)", "🌊 Flood Mapping", "🌳 Deforestation Detection", "🏗️ Road Segmentation"]
)

apply_theme(module)

st.sidebar.markdown("---")
st.sidebar.markdown("**Made with ❤️ - College Project**")

if "Crop Health" in module:
    st.title("🌾 Crop Health Monitoring (NDVI)")
    st.markdown("Upload a **multispectral satellite image** to analyze crop health using NDVI.")
    col1, col2 = st.columns(2)
    with col1:
        uploaded = st.file_uploader("Upload Satellite Image (.tif / .png / .jpg)", type=["tif","tiff","png","jpg"])
    with col2:
        st.info("**How it works:**\n\n1. Upload Sentinel-2 image\n2. NDVI calculated automatically\n3. Healthy/Unhealthy crops identified\n4. Color map displayed")
    if uploaded:
        img = load_image(uploaded)
        st.subheader("📊 NDVI Analysis Result")
        ndvi_result = calculate_ndvi(img)
        show_result(ndvi_result, module="ndvi")

elif "Flood" in module:
    st.title("🌊 Flood Mapping")
    st.markdown("Upload a **SAR or optical satellite image** to detect flood affected areas.")
    col1, col2 = st.columns(2)
    with col1:
        uploaded = st.file_uploader("Upload Satellite Image", type=["tif","tiff","png","jpg"])
    with col2:
        st.info("**How it works:**\n\n1. Upload SAR image\n2. Water pixels detected\n3. Flood boundary mapped\n4. Affected area calculated")
    if uploaded:
        img = load_image(uploaded)
        st.subheader("🗺️ Flood Detection Result")
        show_result(img, module="flood")

elif "Deforestation" in module:
    st.title("🌳 Deforestation Detection")
    st.markdown("Upload **before & after satellite images** to detect deforestation.")
    col1, col2 = st.columns(2)
    with col1:
        before = st.file_uploader("Upload BEFORE Image", type=["tif","tiff","png","jpg"])
    with col2:
        after = st.file_uploader("Upload AFTER Image", type=["tif","tiff","png","jpg"])
    if before and after:
        img_before = load_image(before)
        img_after = load_image(after)
        st.subheader("🔍 Deforestation Analysis Result")
        show_result((img_before, img_after), module="deforest")

elif "Road" in module:
    st.title("🏗️ Road & Building Segmentation")
    st.markdown("Upload a **high resolution satellite image** to segment roads and buildings.")
    col1, col2 = st.columns(2)
    with col1:
        uploaded = st.file_uploader("Upload Satellite Image", type=["tif","tiff","png","jpg"])
    with col2:
        st.info("**How it works:**\n\n1. Upload high-res image\n2. U-Net model segments\n3. Roads highlighted\n4. Buildings outlined")
    if uploaded:
        img = load_image(uploaded)
        st.subheader("🗺️ Segmentation Result")
        show_result(img, module="road")
