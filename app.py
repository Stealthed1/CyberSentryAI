import streamlit as st
import re  # required for pattern matching

st.set_page_config(page_title="CyberSentry AI", layout="wide")

st.title("CyberSentryAI 🛡️")
st.subheader("AI-powered Scam & Phishing Detection for Users")

st.write("Paste a suspicious message below and click Analyze.")
message = st.text_area("Enter message to analyze")

# Define scam detection logic
def is_scam(msg):
    msg = msg.lower()
    red_flags = [
        r"congratulations.*won", 
        r"verify.*account", 
        r"send.*details", 
        r"act now", 
        r"click.*link", 
        r"you have been selected", 
        r"dear customer.*issue", 
        r"urgent response needed"
    ]
    for pattern in red_flags:
        if re.search(pattern, msg):
            return True
    return False

# Analyze button logic
if st.button("🔍 Analyze"):
    if not message.strip():
        st.warning("⚠️ Please enter a message before analyzing.")
    elif is_scam(message):
        st.error("⚠️ This message seems suspicious based on its structure and phrasing. Be careful!")
    else:
        st.success("✅ Message appears safe.")
