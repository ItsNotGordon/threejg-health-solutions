import streamlit as st
from utils.auth import ensure_token
from components.sidebar import render_sidebar
from components.chat_widget import render_chat

st.set_page_config(page_title="Chat", layout="wide")

ensure_token()
render_sidebar()

st.title("🤖 Agent Chat")
st.caption("Talking to your watsonx Orchestrate agent")
st.divider()

render_chat()
