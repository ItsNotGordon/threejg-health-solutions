import streamlit as st
import requests
from service.orchestrate_service import load_credentials, chat_with_agent
from config import TRIAGE_ROUTER_AGENT_ID

# ---------- Page config ----------
st.set_page_config(page_title="Patient Intake Assistant", page_icon="🏥")
st.title("🏥 Patient Intake Assistant")

# ---------- Session state ----------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

# ---------- Load credentials ----------
try:
    wxo_url, token = load_credentials()
    creds_loaded = True
except Exception as e:
    creds_loaded = False
    st.error(
        f"Could not load Orchestrate credentials: {e}\n\n"
        "Make sure you've run `orchestrate env activate hackathon`."
    )

# ---------- Render chat history ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- Welcome message ----------
if not st.session_state.messages:
    welcome = (
        "👋 Welcome to our clinic! My name is Apollo! I'm your personal Healthcare agent here to help get you checked in.\n\n"
        "Could you tell me the reason for your visit today? "
        "For example, are you here for personal health care or a work-related injury?"
    )
    st.session_state.messages.append({"role": "assistant", "content": welcome})
    with st.chat_message("assistant"):
        st.markdown(welcome)

# ---------- Chat input ----------
if user_input := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    if creds_loaded:
        with st.spinner("Thinking..."):
            try:
                reply, new_thread_id = chat_with_agent(
                    user_input,
                    TRIAGE_ROUTER_AGENT_ID,
                    st.session_state.thread_id,
                    wxo_url,
                    token,
                )
                st.session_state.thread_id = new_thread_id
            except requests.exceptions.HTTPError as e:
                reply = f"API error: {e.response.status_code} — {e.response.text}"
            except Exception as e:
                reply = f"Error: {e}"
    else:
        reply = "Credentials not loaded. Please activate your environment."

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)

# ---------- Sidebar ----------
with st.sidebar:
    st.subheader("🔧 Debug")
    st.text(f"Thread: {st.session_state.thread_id or 'None'}")
    if st.button("Reset Conversation"):
        st.session_state.messages = []
        st.session_state.thread_id = None
        st.rerun()
