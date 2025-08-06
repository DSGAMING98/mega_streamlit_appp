import streamlit as st
import os
from datetime import datetime

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("Upload Center")
st.markdown("You can upload files here. Supported types: images, videos, PDFs.")

uploaded_file = st.file_uploader("Select a file", type=["png", "jpg", "jpeg", "mp4", "pdf"])

if uploaded_file:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    save_path = os.path.join(UPLOAD_DIR, f"{timestamp}_{uploaded_file.name}")

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Uploaded: {uploaded_file.name}")
    st.markdown(f"Saved to: `{save_path}`")

    # If it's an image
    if uploaded_file.type.startswith("image/"):
        st.image(save_path, caption="Uploaded Image", use_column_width=True)

    # If it's a video
    elif uploaded_file.type == "video/mp4":
        st.video(save_path)

    # If it's a PDF
    elif uploaded_file.type == "application/pdf":
        st.markdown("PDF uploaded successfully.")
