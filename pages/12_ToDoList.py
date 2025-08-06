import streamlit as st
import os
import sys
import json

# Path setup
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

from magic_tools import ensure_dir

# Auth check
if not st.session_state.get("authenticated"):
    st.warning("Please log in to access your to-do list.")
    st.stop()

st.title("Your To-Do List")

username = st.session_state.get("username")
if not username:
    st.warning("Something went wrong. Please log in again.")
    st.stop()

# Path to todo file
TODO_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data", "todos"))
ensure_dir(TODO_DIR)

TODO_FILE = os.path.join(TODO_DIR, f"{username}_todos.json")

# Create file if missing
if not os.path.exists(TODO_FILE):
    with open(TODO_FILE, "w") as f:
        json.dump([], f)

# Load tasks
with open(TODO_FILE, "r") as f:
    try:
        tasks = json.load(f)
    except json.JSONDecodeError:
        tasks = []

# Add task
with st.form("add_task_form"):
    new_task = st.text_input("New Task")
    submitted = st.form_submit_button("Add Task")
    if submitted and new_task.strip():
        tasks.append({"text": new_task.strip(), "done": False})
        with open(TODO_FILE, "w") as f:
            json.dump(tasks, f)
        st.success("Task added.")
        st.experimental_rerun()

# Show tasks
st.subheader("Your Tasks")
if not tasks:
    st.info("No tasks added yet.")
else:
    for i, task in enumerate(tasks):
        col1, col2, col3 = st.columns([0.05, 0.8, 0.15])
        with col1:
            done = st.checkbox("", value=task["done"], key=f"task_{i}")
        with col2:
            st.markdown(f"{'~~' + task['text'] + '~~' if done else task['text']}")
        with col3:
            if st.button("🗑️", key=f"delete_{i}"):
                tasks.pop(i)
                with open(TODO_FILE, "w") as f:
                    json.dump(tasks, f)
                st.experimental_rerun()
        task["done"] = done

    # Save completion status
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f)
