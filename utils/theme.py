import streamlit as st

THEMES = {
    "🌾 Crop Health (NDVI)": {"primary": "#2ECC71", "bg": "#F0FFF0", "accent": "#27AE60", "text": "#1a5e32"},
    "🌊 Flood Mapping": {"primary": "#2980B9", "bg": "#EBF5FB", "accent": "#154360", "text": "#1a3a5c"},
    "🌳 Deforestation Detection": {"primary": "#E74C3C", "bg": "#FDF2E9", "accent": "#196F3D", "text": "#7b241c"},
    "🏗️ Road Segmentation": {"primary": "#7F8C8D", "bg": "#F2F3F4", "accent": "#2C3E50", "text": "#2c3e50"}
}

def apply_theme(module):
    theme = THEMES.get(module, THEMES["🌾 Crop Health (NDVI)"])
    st.markdown(f"""
    <style>
        .main {{ background-color: {theme['bg']}; }}
        h1, h2, h3 {{ color: {theme['text']}; }}
        .stButton>button {{
            background-color: {theme['primary']};
            color: white;
            border-radius: 10px;
            border: none;
            padding: 10px 20px;
            font-weight: bold;
        }}
        .stSelectbox label {{ color: {theme['text']}; font-weight: bold; }}
        div[data-testid="metric-container"] {{
            background-color: {theme['primary']}22;
            border: 1px solid {theme['primary']};
            border-radius: 10px;
            padding: 10px;
        }}
    </style>
    """, unsafe_allow_html=True)
