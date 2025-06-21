import streamlit as st
from urllib.parse import urlparse

# ---------- CONFIG ----------
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

# ---------- FUNCTION ----------
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

# ---------- UI ----------
st.title("CyberSentryAI 🛡️")
st.subheader("AI-powered Scam & Phishing Detection for Users")

st.markdown("""
Enter a **suspicious message or a website link** below and click **Analyze** to get results.  
This tool uses AI logic to help detect scam keywords, link risks, and social engineering traps.
""")

message = st.text_area("✉️ Enter a suspicious message to analyze")
url = st.text_input("🔗 Or enter a suspicious website/link")

if st.button("🔍 Analyze"):
    if message.strip():
        flagged = [word for word in scam_words if word in message.lower()]
        if flagged:
            st.error(f"⚠️ This message looks suspicious. Keywords detected: {', '.join(flagged)}")
        else:
            st.success("✅ Message appears safe.")
    
    elif url.strip():
        is_bad, reason = is_suspicious_url(url)
        if is_bad:
            st.error(f"⚠️ Suspicious link detected: {reason}")
        else:
            st.success("✅ Link looks safe.")
    
    else:
        st.warning("⚠️ Please enter a message or link before analyzing.")
