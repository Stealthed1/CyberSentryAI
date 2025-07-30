import streamlit as st

st.set_page_config(page_title="CyberSentry AI", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f2f7fc, #ffffff);
        font-family: 'Segoe UI', sans-serif;
    }
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #0056b3;
        padding: 12px 30px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: white;
    }
    .navbar a {
        color: white;
        text-decoration: none;
        margin-left: 20px;
        font-weight: bold;
    }
    .navbar a:hover {
        text-decoration: underline;
    }
    .hero {
        text-align: center;
        padding: 50px 20px;
        background: linear-gradient(to right, #00b894, #0056b3);
        border-radius: 15px;
        color: white;
        margin-bottom: 30px;
    }
    .hero h1 {
        font-size: 3rem;
        font-weight: bold;
    }
    .hero p {
        font-size: 1.2rem;
    }
    .hero button {
        background-color: white;
        color: #0056b3;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        cursor: pointer;
    }
    .hero button:hover {
        background-color: #f1f1f1;
    }
    .feature-btn {
        background: white;
        color: #0056b3;
        border: 2px solid #0056b3;
        border-radius: 12px;
        padding: 20px;
        width: 100%;
        font-weight: bold;
        text-align: center;
        font-size: 1rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .feature-btn:hover {
        background-color: #0056b3;
        color: white;
        transform: translateY(-4px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        padding: 20px;
        color: #666;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="navbar">
    <div><strong>CyberSentry AI</strong></div>
    <div>
        <a href="#features">Features</a>
        <a href="#scanner">Scanner</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>CyberSentry AI</h1>
    <p>Your Smartest Line of Defense Against Scams and Phishing Attacks</p>
    <button onclick="window.location.href='#scanner'">Start Scanning</button>
</div>
""", unsafe_allow_html=True)

st.markdown("## Features", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="feature-btn">Message Scam Detector</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="feature-btn">Phishing Link Checker</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="feature-btn">AI-Powered Analysis</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="feature-btn">Cybersecurity Tips</div>', unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class="footer">
    © 2025 CyberSentry AI | Built with ❤️ to protect users online.
</div>
""", unsafe_allow_html=True)