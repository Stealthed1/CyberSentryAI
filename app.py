import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="CyberSentry AI", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
    <style>
    .stApp {background: linear-gradient(to right, #f2f7fc, #ffffff); font-family: 'Segoe UI', sans-serif;}
    .navbar {display: flex; justify-content: space-between; align-items: center;
             background-color: #0056b3; padding: 12px 30px; border-radius: 10px;
             margin-bottom: 20px; color: white;}
    .navbar a {color: white; text-decoration: none; margin-left: 20px; font-weight: bold;}
    .navbar a:hover {text-decoration: underline;}
    .hero {text-align: center; padding: 50px 20px;
           background: linear-gradient(to right, #00b894, #0056b3);
           border-radius: 15px; color: white; margin-bottom: 30px;}
    .hero h1 {font-size: 3rem; font-weight: bold;}
    .hero p {font-size: 1.2rem;}
    .hero button {background-color: white; color: #0056b3;
                  padding: 10px 20px; border: none; border-radius: 8px;
                  font-weight: bold; cursor: pointer;}
    .hero button:hover {background-color: #f1f1f1;}
    .feature-card {background-color: white; padding: 20px; border-radius: 12px;
                   box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center;
                   transition: transform 0.3s;}
    .feature-card:hover {transform: translateY(-5px);}
    .feature-title {font-weight: bold; color: #0056b3; margin-top: 10px;}
    .footer {text-align: center; margin-top: 40px; padding: 20px;
             color: #666; font-size: 0.9rem;}
    </style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------
menu = st.sidebar.radio("Navigate", ["Home", "Message Analyzer", "Link Analyzer", "Cybersecurity Tips"])

whitelisted_domains = ['waecdirect.org', 'nysc.gov.ng', 'cbn.gov.ng', 'nimc.gov.ng', 
                       'jamb.gov.ng', 'nipost.gov.ng', 'education.gov.ng', 'nira.org.ng']
suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq', '.biz', '.info', '.xyz', '.top']
suspicious_keywords = ['verify', 'account', 'login', 'secure', 'bank', 'update', 'nigeria',
                       'nimc', 'bvn', 'cbn', 'selected', 'shortlisted', 'reward', 'lottery',
                       'win', 'bit.ly', 'tinyurl', 'urgent', 'gift', 'claim', 'bonus', 'promo']
scam_words = ["congratulations", "you have been selected", "you have been shortlisted",
              "dear customer", "urgent action", "verify your account", "claim your reward",
              "you've won", "update your bank", "click to receive", "limited time offer"]

def is_suspicious_url(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower().strip()
        scheme = parsed.scheme
        path = parsed.path.lower()
        domain = domain.replace("www.", "")

        if domain in whitelisted_domains:
            return False
        if scheme != "https":
            return True
        if any(domain.endswith(tld) for tld in suspicious_tlds):
            return True
        if domain.count('.') > 3:
            return True
        if any(keyword in domain or keyword in path for keyword in suspicious_keywords):
            return True
        return False
    except:
        return True

# ---------------- PAGES ----------------
if menu == "Home":
    st.markdown("""
    <div class="navbar">
        <div><strong>🛡️ CyberSentry AI</strong></div>
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
        <button onclick="window.location.href='#scanner'">🚀 Start Scanning</button>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Features", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="feature-card">Message Scam Detector</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="feature-card">Phishing Link Checker</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="feature-card">AI-Powered Analysis</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="feature-card">Cybersecurity Tips</div>', unsafe_allow_html=True)

elif menu == "Message Analyzer":
    st.header("Message Scam Checker")
    message = st.text_area("Paste the suspicious message here")
    if st.button("Analyze Message"):
        if message.strip():
            if any(word in message.lower() for word in scam_words + suspicious_keywords):
                st.error("Message is likely suspicious.")
            else:
                st.success("Message appears safe.")
        else:
            st.warning("Please enter a message first.")

elif menu == "Link Analyzer":
    st.header("Link Phishing Checker")
    url = st.text_input("Paste the suspicious website or link")
    if st.button("Analyze Link"):
        if url.strip():
            if is_suspicious_url(url):
                st.error("Link looks suspicious.")
            else:
                st.success("Link looks safe.")
        else:
            st.warning("Please enter a link first.")

elif menu == "Cybersecurity Tips":
    st.header("Cybersecurity Tips")
    tips = [
        "Use strong and unique passwords for every account.",
        "Never click on unknown email links or attachments.",
        "Enable Two-Factor Authentication (2FA).",
        "Avoid public Wi-Fi when accessing sensitive accounts.",
        "Keep your devices and apps updated regularly.",
        "Be cautious of urgent or 'too good to be true' messages.",
        "Use antivirus and anti-phishing tools."
    ]
    for tip in tips:
        st.info(tip)

st.markdown('<div class="footer">© 2025 CyberSentry AI | Built with ❤️ to protect users online.</div>', unsafe_allow_html=True)