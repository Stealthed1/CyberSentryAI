import streamlit as st

st.set_page_config(page_title="CyberSentry AI", layout="wide")

st.title("CyberSentryAI 🛡️")
st.subheader("AI-powered Scam & Phishing Detection for Users")

st.write("Paste a suspicious message below and click Analyze.")

message = st.text_area("Enter message to analyze")

if st.button("🔍 Analyze"):
    if st.button("🔍 Analyze"):
    if not message.strip():
        st.warning("⚠️ Please enter a message before analyzing.")
    elif is_scam(message):
        st.error("⚠️ This message seems suspicious based on its structure and phrasing. Be careful!")
    else:
        st.success("✅ Message appears safe.")
    if "bank" in message.lower() or "urgent" in message.lower():
        st.error("⚠️ This message looks suspicious. Be careful!")
    else:
        st.success("✅ Message appears safe.")
