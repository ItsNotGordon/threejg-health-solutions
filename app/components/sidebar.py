import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.markdown("## ⚙️ Settings")
        st.markdown("---")
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
        st.markdown("---")
        st.caption("watsonx Orchestrate Hackathon")
