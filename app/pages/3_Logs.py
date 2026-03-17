import streamlit as st

st.set_page_config(page_title="Logs", layout="wide")
st.title("📋 Conversation Logs")
st.divider()

if "messages" not in st.session_state or not st.session_state.messages:
    st.info("No messages yet. Start a conversation on the Chat page.")
else:
    for i, msg in enumerate(st.session_state.messages):
        with st.expander(f"{msg['role'].upper()} — message {i+1}"):
            st.write(msg["content"])
