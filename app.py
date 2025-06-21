import streamlit as st
from urllib.parse import urlparse

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="CyberSentry AI", layout="centered")

# ✨ Add background and styling
def add_custom_styles():
    st.markdown("""
        <style>
        /* Set background gradient */
        .stApp {
            background: linear-gradient(to right, #f2f7fc, #e0ecf1);
            background-attachment: fixed;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Style headers */
        h1, h2, h3 {
            color: #002244;
        }

        /* Style text areas and input boxes */
        textarea, .stTextInput > div > input {
            background-color: #ffffff;
            border: 1px solid #c3d3e5;
            border-radius: 10px;
        }

        /* Buttons */
        button[kind="primary"] {
            background-color: #0056b3;
            color: white;
            border-radius: 8px;
        }

        /* Metrics & boxes */
        .stMetric {
            background-color: #f7fbff;
            border: 1px solid #d0e2f2;
            border-radius: 10px;
            padding: 8px;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #f0f6fb;
        }

        </style>
    """, unsafe_allow_html=True)

add_custom_styles()
# ---------------- TRUSTED & SCAM RULES ----------------
whitelisted_domains = [
    'waecdirect.org',
    'nysc.gov.ng',
    'cbn.gov.ng',
    'nimc.gov.ng',
    'jamb.gov.ng',
    'nipost.gov.ng',
    'education.gov.ng',
    'nira.org.ng'
]

suspicious_tlds = [
    '.tk', '.ml', '.ga', '.cf', '.gq', '.biz', '.info', '.xyz', '.top'
]

suspicious_keywords = [
    'verify', 'account', 'login', 'secure', 'bank', 'update', 'nigeria',
    'nimc', 'bvn', 'cbn', 'selected', 'shortlisted', 'reward', 'lottery',
    'win', 'bit.ly', 'tinyurl', 'urgent', 'gift', 'claim', 'bonus', 'promo'
]

scam_words = [
    "congratulations", "you have been selected", "you have been shortlisted",
    "dear customer", "urgent action", "verify your account", "claim your reward",
    "you've won", "update your bank", "click to receive", "limited time offer"
]

# ---------------- URL ANALYSIS FUNCTION ----------------
def is_suspicious_url(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower().strip()
        scheme = parsed.scheme
        path = parsed.path.lower()

        # Clean domain
        domain = domain.replace("www.", "")
        if domain in whitelisted_domains:
            return False, "✅ Link looks safe."

        if scheme != "https":
            return True, "❌ URL is not secure (uses HTTP instead of HTTPS)"

        for tld in suspicious_tlds:
            if domain.endswith(tld):
                return True, "❌ Suspicious domain ending detected"

        if domain.count('.') > 3:
            return True, "❌ Too many subdomains (may be spoofed)"

        for keyword in suspicious_keywords:
            if keyword in domain or keyword in path:
                return True, "❌ Suspicious pattern found in link"

        return False, "✅ Link looks clean."
    except Exception as e:
        return True, "⚠️ Error checking the link"


# ---------------- STREAMLIT UI ----------------
st.title("CyberSentry AI 🛡️")
st.subheader("Your Smartest Line of Defense Against Scams and Phishing Attacks")

st.markdown("Analyze suspicious **messages** or **website links** to avoid scams and phishing.")

st.divider()

# ---------------- MESSAGE ANALYSIS ----------------
st.markdown("### 📩 Message Scam Checker")
message = st.text_area("Paste the suspicious message here", key="msg_input")

if st.button("🕵️ Analyze Message", key="analyze_msg"):
    if message.strip():
        matched = [word for word in scam_words if word in message.lower()]
        if matched:
            st.error(f"⚠️ Message is likely **suspicious**.\n\nDetected scam phrases: **{', '.join(matched)}**")
        else:
            st.success("✅ Message appears safe. No known scam phrases found.")
    else:
        st.warning("⚠️ Please enter a message first.")

st.divider()

# ---------------- LINK ANALYSIS ----------------
st.markdown("### 🔗 Link Phishing Checker")
url = st.text_input("Paste the suspicious website or link", key="url_input")

if st.button("🔍 Analyze Link", key="analyze_url"):
    if url.strip():
        risk, reason = is_suspicious_url(url)
        if risk:
            st.error(reason)
        else:
            st.success(reason)
    else:
        st.warning("⚠️ Please enter a link first.")
