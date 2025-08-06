import streamlit as st
import os
import sys
from datetime import datetime

# Setup backend import path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

from magic_tools import list_files

# Auth check
if not st.session_state.get("authenticated"):
    st.warning("Please log in to use the search.")
    st.stop()

st.title("Search Diary Entries")

ENTRIES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "entries"))
diary_files = list_files(ENTRIES_DIR, ".txt")

if not diary_files:
    st.info("No entries found.")
    st.stop()

# Search input
search_query = st.text_input("Enter a keyword to search your entries")

# Show entries that match
results = []
for file in diary_files:
    path = os.path.join(ENTRIES_DIR, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        if search_query.lower() in content.lower():
            results.append((file, content))

st.subheader("Search Results")
if not search_query:
    st.info("Start typing to search your entries.")
elif not results:
    st.warning("No entries matched your search.")
else:
    for file, content in results:
        display_name = file.replace("_", " ").replace(".txt", "")
        st.markdown(f"**{display_name}**")
        st.markdown(content[:300] + "...")
        st.markdown("---")
