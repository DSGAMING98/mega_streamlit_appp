import streamlit as st
import os
import sys

# Fix import path for backend folder
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

# Now import from backend.auth.py
from backend.auth import register_user, authenticate_user

st.title("User Authentication")

# Switch between Login and Sign Up
auth_mode = st.radio("Choose mode", ["Login", "Sign Up"])

if auth_mode == "Sign Up":
    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")

    if st.button("Create Account"):
        if new_user.strip() and new_pass.strip():
            success = register_user(new_user.strip(), new_pass.strip())
            if success:
                st.success("Account created. You can now log in.")
            else:
                st.error("Username already exists.")
        else:
            st.warning("Please fill all fields.")

elif auth_mode == "Login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("Login successful.")
        else:
            st.error("Invalid credentials.")

# If already logged in, show logout
if st.session_state.get("authenticated"):
    st.sidebar.markdown(f"Logged in as: `{st.session_state.get('username')}`")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.rerun()  # ← Updated for latest Streamlit
