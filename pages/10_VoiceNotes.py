import streamlit as st
import os
import sys

# Setup backend path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

from magic_tools import list_files

# Auth check
if not st.session_state.get("authenticated"):
    st.warning("Please log in to access voice notes.")
    st.stop()

st.title("Voice Notes")

UPLOADS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "uploads"))

# File uploader
audio_file = st.file_uploader("Upload a voice note (.mp3 or .wav)", type=["mp3", "wav"])
if audio_file:
    save_path = os.path.join(UPLOADS_DIR, audio_file.name)
    with open(save_path, "wb") as f:
        f.write(audio_file.getbuffer())
    st.success(f"Uploaded: {audio_file.name}")

# Load all audio files
audio_files = list_files(UPLOADS_DIR)
audio_files = [f for f in audio_files if f.lower().endswith((".mp3", ".wav"))]

if not audio_files:
    st.info("No voice notes found.")
else:
    st.subheader("Saved Voice Notes")
    for file in audio_files:
        file_path = os.path.join(UPLOADS_DIR, file)
        st.audio(file_path, format="audio/wav" if file.endswith(".wav") else "audio/mp3")
        st.markdown(f"`{file}`")
