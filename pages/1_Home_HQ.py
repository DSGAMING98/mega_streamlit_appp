import streamlit as st
import os
import sys
import json
from datetime import datetime

# Setup
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

from magic_tools import list_files, ensure_dir

# Auth check
if not st.session_state.get("authenticated"):
    st.warning("Please log in to access the dashboard.")
    st.stop()

st.title("🏠 Home Dashboard")

username = st.session_state.get("username") or "User"

# Time-based greeting
hour = datetime.now().hour
if hour < 12:
    greeting = "Good morning"
elif hour < 17:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

st.markdown(f"### {greeting}, `{username}` 👋")
st.write("Welcome back to your personal HQ. Here’s what’s going on:")

# === QUICK STATS ===
ENTRIES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "entries"))
UPLOADS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "uploads"))
TODO_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "todos"))
ensure_dir(ENTRIES_DIR)
ensure_dir(UPLOADS_DIR)
ensure_dir(TODO_DIR)

entry_count = len(list_files(ENTRIES_DIR, ".txt"))
upload_count = len(list_files(UPLOADS_DIR))
todo_file = os.path.join(TODO_DIR, f"{username}_todos.json")

if os.path.exists(todo_file):
    try:
        with open(todo_file, "r", encoding="utf-8") as f:
            todos = json.load(f)
            incomplete_tasks = len([t for t in todos if not t.get("done")])
    except (json.JSONDecodeError, UnicodeDecodeError):
        incomplete_tasks = 0

else:
    incomplete_tasks = 0

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📓 Diary Entries", entry_count)
with col2:
    st.metric("📤 Files Uploaded", upload_count)
with col3:
    st.metric("✅ Pending Tasks", incomplete_tasks)

# === QUICK NAVIGATION ===
st.markdown("---")
st.subheader("⚡ Quick Access")

col1, col2, col3 = st.columns(3)
with col1:
    st.button("✍️ Diary Vault", key="diary_vault", help="Go to the Diary Vault page from the sidebar")
    st.button("📊 Analytics", key="analytics_dash", help="Use the sidebar to open Analytics Dashboard")
with col2:
    st.button("🖼️ Image Gallery", key="image_gallery", help="Open from sidebar")
    st.button("✅ To-Do List", key="todo_list", help="Open from sidebar")
with col3:
    st.button("🔊 Voice Notes", key="voice_notes", help="Use sidebar")
    st.button("🤖 AI Analysis", key="ai_analysis", help="Use sidebar")

st.markdown("👉 Use the **sidebar** to navigate to these tools.")

# === DAILY PROMPT ===
st.markdown("---")
st.subheader("🧠 Daily Journal Prompt")

prompt = "What’s one thing you’re proud of this week, and why?"
st.markdown(f"> *{prompt}*")

response = st.text_area("Your reflection", height=150, placeholder="Type here...")

if st.button("Save Reflection", key="save_reflection"):
    if not response.strip():
        st.warning("You didn’t write anything.")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(ENTRIES_DIR, f"prompt_{timestamp}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Prompt: {prompt}\n\nResponse:\n{response.strip()}")
        st.success("Reflection saved to your diary.")
