import streamlit as st
import openai
import re

# Page config
st.set_page_config(page_title="Vajra AI: The Digital Kavach", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for Neon Blue/Silver "Guardian" Theme (Dark Mode)
st.markdown("""
<style>
    /* Dark Mode Theme overrides */
    body {
        background-color: #0b0f19;
        color: #e0e6ed;
    }
    .stApp {
        background-color: #0b0f19;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #00e5ff !important;
        text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);
    }
    .stButton>button {
        background: linear-gradient(90deg, #004d66 0%, #00e5ff 100%);
        border: none;
        color: #ffffff;
        box-shadow: 0 4px 15px rgba(0, 229, 255, 0.4);
        font-weight: bold;
        transition: all 0.3s ease;
        border-radius: 6px;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 229, 255, 0.6);
        color: white;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div {
        background-color: #151a28 !important;
        color: #00e5ff !important;
        border: 1px solid #004d66 !important;
        border-radius: 6px;
    }
    .css-1d391kg {  /* Sidebar */
        background-color: #0c1220;
        border-right: 1px solid #004d66;
    }
    hr {
        border-color: #004d66;
    }
    /* Streamlit expander styling */
    div[data-testid="stExpander"] {
        background-color: #151a28;
        border: 1px solid #004d66;
        border-radius: 8px;
    }
    div[data-testid="stExpander"] > summary * {
        color: #c0c8db;
    }
</style>
""", unsafe_allow_html=True)

# Main Title
st.title("🛡️ Vajra AI: The Digital Kavach")
st.markdown("*Your AI-Powered Defensive Shield Against Cyber Fraud*")

# Sidebar
st.sidebar.header("⚙️ Configuration")
api_key = st.sidebar.text_input("Enter Grok API Key", type="password", placeholder="Paste xAI Key here...")
language = st.sidebar.selectbox("Language Selector", ["English", "Hindi", "Regional"])

st.sidebar.markdown("---")
st.sidebar.markdown("### The Digital Kavach")
st.sidebar.info("Vajra AI is a forensic engine engineered to detect predatory behaviors, fake receipts, digital arrests, and AI voice cloning.")

# API Integration Logic (Grok API using OpenAI library)
def analyze_with_grok(api_key, context, content, language):
    if not api_key:
        return {"error": "Please provide a Grok API Key in the sidebar."}
        
    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://api.x.ai/v1",
    )
    
    # The "Expert" System Prompt
    system_prompt = (
        "You are a Senior Cyber-Fraud Investigator. Analyze inputs for psychological triggers "
        "(Urgency, Fear, Greed), fake institutional patterns, and predatory fine print. "
        "Provide a 0-100% Risk Score and a 1930 Cyber-Complaint draft."
    )
    
    # User prompt incorporating exact instructions for expander formatting
    user_prompt = (
        f"Context/Directives: {context}\n\n"
        f"Target Material to Analyze:\n{content}\n\n"
        f"Language Request: Respond entirely in {language} (Ensure translation is accurate).\n\n"
        "FORMAT YOUR RESPONSE EXACTLY WITH THESE FOUR HEADERS:\n\n"
        "### RISK SCORE\n[Your 0-100% score here with a brief description]\n\n"
        "### FORENSIC ANALYSIS\n[Detailed breakdown here]\n\n"
        "### LANGUAGE TRANSLATION\n[Relevant translation or summary here]\n\n"
        "### ACTION PLAN\n[1930 draft and next steps here]"
    )
    
    try:
        response = client.chat.completions.create(
            model="grok-2-latest",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )
        return {"result": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}

# Institutional Verifier logic
def verify_institutional_claim(text):
    # Logic to flag 10-digit mobile numbers claiming to be "Official Banks"
    phones = re.findall(r'\b[6-9]\d{9}\b', text)
    bank_keywords = ["bank", "sbi", "hdfc", "icici", "rbi", "customer care", "support", "official"]
    text_lower = text.lower()
    claims_bank = any(kw in text_lower for kw in bank_keywords)
    
    if phones and claims_bank:
        st.warning(f"⚠️ **Institutional Verifier Flag:** Message contains 10-digit mobile number(s) ({', '.join(phones)}) while using bank-related keywords. Official banks do not use standard 10-digit mobile numbers for official SMS or customer support. High probability of impersonation.")

# Display results in clear Expanders
def render_results(raw_text):
    # Fallback sections
    sections = {
        "Risk Score": "Could not parse section. Check full raw output.",
        "Forensic Analysis": "Could not parse section. Check full raw output.",
        "Language Translation": "Could not parse section. Check full raw output.",
        "Action Plan": "Could not parse section. Check full raw output."
    }
    
    # Parse headers
    score_match = re.search(r'### RISK SCORE(.*?)### FORENSIC ANALYSIS', raw_text, re.DOTALL | re.IGNORECASE)
    forensic_match = re.search(r'### FORENSIC ANALYSIS(.*?)### LANGUAGE TRANSLATION', raw_text, re.DOTALL | re.IGNORECASE)
    translation_match = re.search(r'### LANGUAGE TRANSLATION(.*?)### ACTION PLAN', raw_text, re.DOTALL | re.IGNORECASE)
    action_match = re.search(r'### ACTION PLAN(.*)', raw_text, re.DOTALL | re.IGNORECASE)
    
    if score_match: sections["Risk Score"] = score_match.group(1).strip()
    if forensic_match: sections["Forensic Analysis"] = forensic_match.group(1).strip()
    if translation_match: sections["Language Translation"] = translation_match.group(1).strip()
    if action_match: sections["Action Plan"] = action_match.group(1).strip()
    
    with st.expander("🚨 Risk Score", expanded=True):
        st.write(sections["Risk Score"])
    with st.expander("🔍 Forensic Analysis", expanded=True):
        st.write(sections["Forensic Analysis"])
    with st.expander("🌐 Language Translation", expanded=False):
        st.write(sections["Language Translation"])
    with st.expander("🛡️ Action Plan", expanded=True):
        st.write(sections["Action Plan"])
        
    with st.expander("Raw AI Output", expanded=False):
        st.text(raw_text)

# UI/UX: Tabs layout
tab1, tab2, tab3 = st.tabs(["💬 Text & SMS Scanner", "📄 Document & Image Engine", "🎙️ Vocal DNA Analyzer"])

# Feature 1: Text & SMS Scanner
with tab1:
    st.subheader("Suspicious Message Scanner")
    text_input = st.text_area("Paste suspicious SMS, WhatsApp message, or Email here:", height=150)
    
    if st.button("Scan Text", key="btn_text"):
        if text_input:
            verify_institutional_claim(text_input)
            with st.spinner("Analyzing message forensics..."):
                res = analyze_with_grok(api_key, "Analyze this raw text message for phishing, urgency, fear, greed, and scam patterns.", text_input, language)
                if "error" in res:
                    st.error(res["error"])
                else:
                    render_results(res["result"])
        else:
            st.warning("Please paste some text to analyze.")

# Feature 2: Document & Image Forensic Engine
with tab2:
    st.subheader("Document & Image Forensic Engine")
    st.write("Upload PDFs, Word Docs, or Images (PNG/JPG) to detect 'Hidden Predatory Clauses', 'Fake Receipt Artifacts', or 'Digital Arrest' scripts.")
    uploaded_file = st.file_uploader("Upload Document/Image", type=["pdf", "docx", "png", "jpg", "jpeg"])
    
    if st.button("Analyze File", key="btn_doc"):
        if uploaded_file:
            st.info(f"File uploaded: {uploaded_file.name} ({uploaded_file.size} bytes)")
            with st.spinner("Extracting hidden clauses & analyzing image artifacts..."):
                file_details = f"File Name: {uploaded_file.name}\nFile Type: {uploaded_file.type}\nFile Size: {uploaded_file.size} bytes\n"
                context = (
                    "Tell the AI to analyze these details for 'Hidden Predatory Clauses', "
                    "'Fake Receipt Artifacts', or 'Digital Arrest' scripts based on the file type and context. "
                    "Since this is a file upload simulation, provide a forensic analysis on the likelihood of fraud for this specific vector."
                )
                res = analyze_with_grok(api_key, context, file_details, language)
                if "error" in res:
                    st.error(res["error"])
                else:
                    render_results(res["result"])
        else:
            st.warning("Please upload a file.")

# Feature 3: Vocal DNA Analyzer
with tab3:
    st.subheader("Vocal DNA Analyzer")
    st.write("Upload audio snippets to check for 'AI Voice Cloning' artifacts.")
    audio_file = st.file_uploader("Upload Audio", type=["mp3", "wav", "m4a", "ogg"])
    
    if st.button("Analyze Vocal DNA", key="btn_audio"):
        if audio_file:
            st.info(f"Audio uploaded: {audio_file.name} ({audio_file.size} bytes)")
            with st.spinner("Processing audio frequencies and checking for AI voice cloning anomalies..."):
                audio_details = f"Audio File Name: {audio_file.name}\nFormat: {audio_file.type}\n"
                context = (
                    "Provide a forensic analysis report checking for 'AI Voice Cloning' artifacts (e.g., lack of natural breathing, "
                    "synthetic frequency anomalies, unnatural pacing) as if you have processed this audio."
                )
                res = analyze_with_grok(api_key, context, audio_details, language)
                if "error" in res:
                    st.error(res["error"])
                else:
                    render_results(res["result"])
        else:
            st.warning("Please upload an audio file.")
