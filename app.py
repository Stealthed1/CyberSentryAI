# Generating the full updated source code for CyberSentry AI in a zip file

import os
import zipfile

# Define base path for file creation
base_path = "/mnt/data/cybersentryai"
os.makedirs(base_path, exist_ok=True)

# Dictionary of files and their content
files = {
    "app.py": '''import streamlit as st
from url_analyzer import is_suspicious_url

st.set_page_config(page_title="CyberSentry AI", layout="centered")

st.title("CyberSentryAI 🛡️")
st.subheader("AI-powered Scam & Phishing Detection for Users")

st.write("Paste a suspicious message or link below and click Analyze.")

message = st.text_area("Enter message to analyze")
url = st.text_input("Or enter a link to analyze")

if st.button("🔍 Analyze"):
    if message.strip():
        scam_words = ["congratulations", "selected", "winner", "urgent", "bank", "account", "bvn", "lottery", "reward", "free", "limited"]
        flagged = [word for word in scam_words if word in message.lower()]
        if flagged:
            st.error(f"⚠️ This message looks suspicious. Words flagged: {', '.join(flagged)}")
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
''',

    "url_analyzer.py": '''from urllib.parse import urlparse

suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq', '.biz', '.info']
suspicious_keywords = ['verify', 'account', 'login', 'secure', 'bank', 'update', 'nigeria', 'waec', 'nysc', 'nimc', 'bvn', 'cbn', 'free', 'selected', 'shortlisted', 'reward', 'lottery', 'win', 'sttps', 'bit.ly', 'tinyurl']
whitelisted_domains = ['waecdirect.org', 'nysc.gov.ng', 'cbn.gov.ng', 'nimc.gov.ng', 'jamb.gov.ng', 'nira.org.ng', 'nipost.gov.ng', 'education.gov.ng']

def is_suspicious_url(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        scheme = parsed.scheme
        path = parsed.path.lower()

        # Whitelist check
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
''',

    "requirements.txt": '''streamlit
'''
}

# Create each file in the directory
for filename, content in files.items():
    file_path = os.path.join(base_path, filename)
    with open(file_path, "w") as f:
        f.write(content)

# Zip the entire directory
zip_path = "/mnt/data/CyberSentryAI_Updated.zip"
with zipfile.ZipFile(zip_path, "w") as zipf:
    for filename in files:
        zipf.write(os.path.join(base_path, filename), arcname=f"cybersentryai/{filename}")

zip_path
