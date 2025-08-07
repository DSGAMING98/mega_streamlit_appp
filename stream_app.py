import os
import sys
import streamlit as st

# Make sure the root of your project is added to sys.path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

from backend.magic_tools import list_files, ensure_dir


if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def inject_custom_css():
    css_path = os.path.join("assets", "site_styles.css")
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

inject_custom_css()

st.set_page_config(
    page_title="Mega Streamlit App",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

from components.sidebar_nav import render_sidebar
render_sidebar()

st.title("Welcome to the Mega Streamlit App")
st.markdown("Navigate using the **sidebar** to access all available modules and tools.")
