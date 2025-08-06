import streamlit as st
import os
import sys
import shutil
import zipfile
from io import BytesIO

# Setup backend import
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ENTRIES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "entries"))

# Auth check
if not st.session_state.get("authenticated"):
    st.warning("Please log in to export your diary.")
    st.stop()

st.title("Export Diary Entries")

# List all entries
entries = [f for f in os.listdir(ENTRIES_DIR) if f.endswith(".txt")]

if not entries:
    st.info("You have no diary entries to export.")
else:
    export_option = st.radio("Export format", ["ZIP (.zip)", "Single PDF (.pdf) [coming soon]"])

    if export_option == "ZIP (.zip)":
        if st.button("Download All as .zip"):
            # Create zip in memory
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as zipf:
                for entry in entries:
                    path = os.path.join(ENTRIES_DIR, entry)
                    with open(path, "r", encoding="utf-8") as f:
                        zipf.writestr(entry, f.read())

            zip_buffer.seek(0)
            st.download_button(
                label="📥 Download ZIP",
                data=zip_buffer,
                file_name="my_diary_entries.zip",
                mime="application/zip"
            )
