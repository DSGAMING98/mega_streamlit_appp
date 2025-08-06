import streamlit as st
import os
import sys
from PIL import Image

# Setup backend import
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

from magic_tools import list_files

# Auth check
if not st.session_state.get("authenticated"):
    st.warning("Please log in to view the gallery.")
    st.stop()

st.title("Image Gallery")

UPLOADS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "uploads"))

# Get all image files
image_files = list_files(UPLOADS_DIR)
image_files = [f for f in image_files if f.lower().endswith((".png", ".jpg", ".jpeg"))]

if not image_files:
    st.info("No images uploaded yet.")
else:
    # Display in columns
    cols = st.columns(3)
    for index, file in enumerate(image_files):
        col = cols[index % 3]
        img_path = os.path.join(UPLOADS_DIR, file)
        with col:
            st.image(Image.open(img_path), caption=file, use_column_width=True)
