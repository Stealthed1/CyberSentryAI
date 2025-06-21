import streamlit as st

st.set_page_config(page_title="CyberSentry AI", layout="wide")

st.title("🛡️ CyberSentry AI")
st.subheader("AI-powered Scam & Phishing Detection for Nigerian Users")

st.write("Paste a suspicious message below and click Analyze.")

message = st.text_area("Enter message to analyze")

if st.button("🔍 Analyze"):
    if "bank" in message.lower() or "urgent" in message.lower():
        st.error("⚠️ This message looks suspicious. Be careful!")
    else:
        st.success("✅ Message appears safe.")
