import streamlit as st
import os
import sys
from datetime import datetime

# Import tools
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

from magic_tools import list_files, ensure_dir

# Auth check
if not st.session_state.get("authenticated"):
    st.warning("Please log in to use the diary.")
    st.stop()

st.title("Diary Vault")

# Path to save entries
ENTRIES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "entries"))
ensure_dir(ENTRIES_DIR)

# Input box
entry_text = st.text_area("Write your entry here", height=200)

# Save entry
if st.button("Save Entry"):
    if entry_text.strip() == "":
        st.warning("Entry cannot be empty.")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(ENTRIES_DIR, f"entry_{timestamp}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(entry_text.strip())
        st.success("Entry saved successfully.")
        st.experimental_rerun()

# Show saved entries
st.subheader("Saved Entries")
entries = list_files(ENTRIES_DIR, ".txt")

if not entries:
    st.info("No entries saved yet.")
else:
    for file in entries:
        with open(os.path.join(ENTRIES_DIR, file), "r", encoding="utf-8") as f:
            content = f.read()
        with st.expander(file.replace("entry_", "").replace(".txt", "").replace("_", " ")):
            st.markdown(content)
