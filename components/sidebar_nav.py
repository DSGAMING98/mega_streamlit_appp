import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("Mega Streamlit App")
        st.caption("Built with 💼 by you.")

        # Optional: Quick user status display
        if st.session_state.get("authenticated"):
            st.success(f"Logged in as {st.session_state.get('username')}")
        else:
            st.warning("Not logged in")


        st.markdown("---")
        st.caption("Use the sidebar to access all features.")
