import streamlit as st
import os
import sys

# Path fix to import magic_tools
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

from magic_tools import list_files

# Auth check
if not st.session_state.get("authenticated"):
    st.warning("Please log in to view your profile.")
    st.stop()

st.title("User Profile")

username = st.session_state.get("username")
st.markdown(f"**Logged in as:** `{username}`")

# Directory paths
ENTRIES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "entries"))
UPLOADS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "uploads"))

# Show last 3 diary entries
st.subheader("Recent Diary Entries")
diary_files = list_files(ENTRIES_DIR, ".txt")[:3]
if not diary_files:
    st.info("No entries found.")
else:
    for file in diary_files:
        with open(os.path.join(ENTRIES_DIR, file), "r", encoding="utf-8") as f:
            content = f.read()
        with st.expander(file.replace("_", " ").replace(".txt", "")):
            st.markdown(content)

# Show last 3 uploaded files
st.subheader("Recent Uploads")
upload_files = list_files(UPLOADS_DIR)[:3]
if not upload_files:
    st.info("No uploads yet.")
else:
    for file in upload_files:
        st.markdown(f"• `{file}`")
