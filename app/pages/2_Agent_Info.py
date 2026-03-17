import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Agent Info", layout="wide")
st.title("🔍 Agent Info")
st.divider()

st.markdown("### Current Configuration")
st.code(f"""
Host:          {os.getenv('WXO_HOST', 'not set')}
Agent ID:      {os.getenv('AGENT_ID', 'not set')}
Environment:   {os.getenv('AGENT_ENVIRONMENT_ID', 'not set')}
""")
