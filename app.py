import streamlit as st
import re

# Streamlit page setup
st.set_page_config(page_title="CyberSentry AI", layout="wide")

st.title("CyberSentryAI 🛡️")
st.subheader("AI-powered Scam & Phishing Detection for Nigerian Users")

st.write("Paste a suspicious message below and click Analyze.")
message = st.text_area("Enter message to analyze")

# Scam detection logic
def is_scam(msg):
    msg = msg.lower()
    red_flags = [
        # Global scam bait
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

        # Nigerian-specific scam patterns
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

        # Business and fake job offers
        r"work from home.*earn",
        r"job offer.*urgent",
        r"interview.*confirmation",
        r"submit.*cv.*with.*fee",
        r"pay.*to.*schedule.*interview",
        r"business.*opportunity.*investment",

        # Religious or emotional manipulation
        r"i had a dream.*reveal",
        r"prophet.*message for you",
        r"miracle.*awaits.*you",
        r"donate.*for.*blessing",
        r"church.*account.*transfer",

        # Fake delivery/logistics
        r"your parcel.*custom.*clearance",
        r"delivery.*fee.*payment",
        r"package.*awaiting.*pickup",

        # Crypto and investment scams
        r"double your bitcoin",
        r"roi.*within.*24 hours",
        r"investment.*plan.*high return",
        r"crypto.*airdrop.*register",
        r"register.*and.*earn",

        # Threat-based intimidation
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

# Analyze button logic
if st.button("🔍 Analyze"):
    if not message.strip():
        st.warning("⚠️ Please enter a message before analyzing.")
    elif is_scam(message):
        st.error("⚠️ This message appears suspicious based on its phrasing and structure. Please be cautious!")
    else:
        st.success("✅ This message appears safe.")
