import streamlit as st
from urllib.parse import urlparse

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="CyberSentry AI", layout="centered")

# ---------- WHITELIST & RULES ----------
suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq', '.biz', '.info']
suspicious_keywords = [
    'verify', 'account', 'login', 'secure', 'bank', 'update', 'nigeria',
    'waec', 'nysc', 'nimc', 'bvn', 'cbn', 'free', 'selected', 'shortlisted',
    'reward', 'lottery', 'win', 'sttps', 'bit.ly', 'tinyurl'
]
whitelisted_domains = [
    'waecdirect.org', 'nysc.gov.ng', 'cbn.gov.ng', 'nimc.gov.ng',
    'jamb.gov.ng', 'nira.org.ng', 'nipost.gov.ng', 'education.gov.ng'
]
scam_words = [
    "congratulations", "selected", "shortlisted", "winner", "urgent",
    "bank", "account", "bvn", "lottery", "reward", "free", "click", "update"
]

# ---------- URL CHECK FUNCTION ----------
def is_suspicious_url(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        scheme = parsed.scheme
        path = parsed.path.lower()

        for safe_domain in whitelisted_domains:
            if domain.endswith(safe_domain):
                return False, "Domain is trusted (whitelisted)"

        if scheme != "https":
            return True, "URL does not use HTTPS (insecure)"

        for tld in suspicious_tlds:
            if domain.endswith(tld):
                return True, f"Suspicious domain ending ({tld})"

        if domain.count('.') > 3:
            return True, "Too many subdomains (likely spoofed)"

        for keyword in suspicious_keywords:
            if keyword in domain or keyword in path:
                return True, f"Suspicious keyword found: '{keyword}'"

        return False, "Link looks clean."
    except Exception as e:
        return True, f"Error analyzing link: {str(e)}"

# ---------- HEADER ----------
st.title("CyberSentryAI 🛡️")
st.subheader("Detect Scam Messages and Suspicious Links Easily")

st.markdown("Enter either a suspicious message or a link below. Each section has its own button for analysis.")

st.divider()

# ---------- MESSAGE ANALYSIS ----------
st.markdown("### 📩 Message Analysis")
message = st.text_area("Enter a suspicious message")

if st.button("🕵️ Analyze Message"):
    if message.strip():
        flagged = [word for word in scam_words if word in message.lower()]
        if flagged:
            st.error(f"⚠️ Suspicious message detected. Keywords: {', '.join(flagged)}")
        else:
            st.success("✅ Message appears safe.")
    else:
        st.warning("Please enter a message before analyzing.")

st.divider()

# ---------- LINK ANALYSIS ----------
st.markdown("### 🔗 Link Analysis")
url = st.text_input("Enter a suspicious website or link")

if st.button("🔍 Analyze Link"):
    if url.strip():
        is_bad, reason = is_suspicious_url(url)
        if is_bad:
            st.error(f"⚠️ Suspicious link detected: {reason}")
        else:
            st.success("✅ Link looks safe.")
    else:
        st.warning("Please enter a link before analyzing.")
