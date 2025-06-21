import streamlit as st
import re
from urllib.parse import urlparse

# ---------------------
# STREAMLIT CONFIGURATION
# ---------------------
st.set_page_config(page_title="CyberSentry AI", layout="centered")

st.title("CyberSentryAI 🛡️")
st.subheader("AI-powered Scam & Phishing Detection for Users")
st.write("Paste a suspicious message or link below and click **Analyze**.")

# ---------------------
# SCAM TEXT DETECTOR
# ---------------------
def is_scam(msg):
    msg = msg.lower()
    red_flags = [
        r"congratulations.*(won|selected|shortlisted)",
        r"you have been (selected|shortlisted|chosen)",
        r"you.*won.*(lottery|gift|promotion)",
        r"click.*(link|here).*claim",
        r"urgent.*(action|required|response)",
        r"final warning",
        r"act immediately",
        r"your.*(account|profile).*suspended",
        r"payment.*(required|needed|overdue)",
        r"send.*(bvn|account number|password|otp|card|details)",
        r"claim.*your.*(reward|prize|benefit)",
        r"reset.*password",
        r"you.*inherit.*(fund|money|estate)",
        r"this is from (cbn|efcc|nimc|waec|ncc|nirsal|nddc|frsc)",
        r"nysc.*(selection|payment|batch)",
        r"waec.*result.*(withheld|blocked)",
        r"your.*nin.*(not linked|blocked)",
        r"subsidy.*grant",
        r"smedan.*loan.*disbursement",
        r"survival fund.*approved",
        r"bank.*account.*blocked",
        r"atm.*(blocked|deactivated)",
        r"you've been credited",
        r"register.*to receive",
        r"contact.*our.*agent",
        r"fill.*this.*form.*urgently",
        r"work from home.*earn",
        r"job offer.*urgent",
        r"interview.*confirmation",
        r"submit.*cv.*with.*fee",
        r"pay.*to.*schedule.*interview",
        r"business.*opportunity.*investment",
        r"i had a dream.*reveal",
        r"prophet.*message for you",
        r"miracle.*awaits.*you",
        r"donate.*for.*blessing",
        r"church.*account.*transfer",
        r"your parcel.*custom.*clearance",
        r"delivery.*fee.*payment",
        r"package.*awaiting.*pickup",
        r"double your bitcoin",
        r"roi.*within.*24 hours",
        r"investment.*plan.*high return",
        r"crypto.*airdrop.*register",
        r"register.*and.*earn",
        r"we will report you",
        r"legal.*action.*will be taken",
        r"your file has been forwarded",
        r"investigation.*launched",
        r"debt.*settlement.*now"
    ]
    for pattern in red_flags:
        if re.search(pattern, msg):
            return True
    return False

# ---------------------
# SUSPICIOUS LINK DETECTOR
# ---------------------
suspicious_tlds = ['.xyz', '.tk', '.ru', '.cn', '.top', '.buzz']
suspicious_keywords = [
    'login', 'verify', 'account', 'bank', 'secure', 'update',
    'waec', 'nysc', 'ncc', 'nimc', 'cbn', 'atm', 'bvn',
    'giveaway', 'winner', 'grant', 'payment', 'unlock',
    'tinyurl', 'bit.ly', 'shorturl', 'is.gd'
]

def is_suspicious_url(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        scheme = parsed.scheme
        path = parsed.path.lower()

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

# ---------------------
# ANALYSIS UI
# ---------------------
col1, col2 = st.columns(2)

# Text Message Input & Analysis
with col1:
    st.markdown("### ✉️ Analyze Text Message")
    message = st.text_area("Enter suspicious message:")

    if st.button("🔍 Analyze Message"):
        if not message.strip():
            st.warning("⚠️ Please enter a message before analyzing.")
        elif is_scam(message):
            st.error("🚨 This message appears suspicious. Be cautious!")
        else:
            st.success("✅ This message appears safe.")

# URL Input & Analysis
with col2:
    st.markdown("### 🔗 Analyze Link or URL")
    url = st.text_input("Paste a suspicious link:")

    if st.button("🔍 Analyze Link"):
        if not url.strip():
            st.warning("⚠️ Please enter a link before analyzing.")
        else:
            suspicious, reason = is_suspicious_url(url)
            if suspicious:
                st.error(f"🚨 Suspicious link detected: {reason}")
            else:
                st.success("✅ Link looks clean.")

