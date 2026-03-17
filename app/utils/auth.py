import streamlit as st
from utils.wxo_client import get_iam_token


def ensure_token():
    """Call at the top of any page that needs auth."""
    if "token" not in st.session_state:
        with st.spinner("Authenticating..."):
            st.session_state.token = get_iam_token()
