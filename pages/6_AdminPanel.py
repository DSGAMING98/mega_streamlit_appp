import streamlit as st
import os
import sys

# Force add backend path directly
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "backend"))

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from magic_tools import list_files

# Protect admin panel
if not st.session_state.get("authenticated"):
    st.warning("Access denied. Please log in as admin.")
    st.stop()

st.title("Admin Dashboard")
st.markdown("This dashboard allows you to view all user-generated content.")

ENTRIES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "entries"))
UPLOADS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "uploads"))
CONTACT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "contact_messages"))

# Show Diary Entries
st.subheader("Diary Entries")
diary_files = list_files(ENTRIES_DIR, ".txt")
if not diary_files:
    st.info("No diary entries found.")
else:
    for file in diary_files:
        with open(os.path.join(ENTRIES_DIR, file), "r", encoding="utf-8") as f:
            content = f.read()
        with st.expander(file.replace("_", " ").replace(".txt", "")):
            st.markdown(content)

# Show Contact Messages
st.subheader("Contact Submissions")
contact_files = list_files(CONTACT_DIR, ".txt")
if not contact_files:
    st.info("No contact messages yet.")
else:
    for file in contact_files:
        with open(os.path.join(CONTACT_DIR, file), "r", encoding="utf-8") as f:
            content = f.read()
        with st.expander(file.replace("_", " ").replace(".txt", "")):
            st.markdown(content)

# Show Uploaded Files
st.subheader("Uploaded Files")
uploaded_files = list_files(UPLOADS_DIR)
if not uploaded_files:
    st.info("No uploads found.")
else:
    for file in uploaded_files:
        file_path = os.path.join(UPLOADS_DIR, file)
        st.markdown(f"• `{file}` — saved at `{file_path}`")
