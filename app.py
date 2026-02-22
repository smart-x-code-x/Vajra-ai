import streamlit as st
import openai
import PyPDF2
from io import BytesIO

# --- 1. Background API Configuration (FIXED FOR GROQ) ---
# NOTE: Your key is now hardcoded here. Use llama-3.3-70b-versatile for Groq.
GROK_API_KEY = ""
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME = "llama-3.3-70b-versatile"

# Page config
st.set_page_config(page_title="Vajra AI: The Digital Kavach", layout="wide", initial_sidebar_state="expanded")

# Professional UI/UX Styling
st.markdown("""
<style>
    .stApp { background-color: #0a0e17; color: #e2e8f0; }
    h1, h2, h3 { color: #00e5ff !important; text-shadow: 0 0 15px rgba(0, 229, 255, 0.3); }
    .stButton>button { background: transparent; border: 2px solid #00e5ff; color: #00e5ff; border-radius: 6px; font-weight: bold; }
    .stButton>button:hover { background: #00e5ff; color: #0a0e17; box-shadow: 0 0 20px rgba(0, 229, 255, 0.5); }
    .ticker-box { background: #151b2b; border-left: 4px solid #00e5ff; padding: 15px; border-radius: 4px; }
    .ticker-item { margin-bottom: 12px; font-size: 0.9em; border-bottom: 1px solid #1a2333; padding-bottom: 8px; }
</style>
""", unsafe_allow_html=True)

# --- Sidebar: Current Scam Ticker ---
st.sidebar.header("🛡️ Current Scam Ticker (India)")
st.sidebar.markdown(f"""
<div class="ticker-box">
    <div class="ticker-item">⚠️ <strong>Electricity Bill:</strong> Fake disconnection threats via SMS.</div>
    <div class="ticker-item">⚠️ <strong>Digital Arrest:</strong> Scammers posing as CBI/Police on Skype.</div>
    <div class="ticker-item">⚠️ <strong>Voice Cloning:</strong> AI-generated family emergency calls.</div>
    <div class="ticker-item">⚠️ <strong>1930 Helpline:</strong> Report all fraud immediately.</div>
</div>
""", unsafe_allow_html=True)

# --- Main App ---
st.title("🛡️ Vajra AI: The Digital Kavach")

tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "💬 Message Scan", "📄 Document Vault", "🎙️ Vocal DNA"])


def analyze_with_ai(context, content):
    try:
        # Connect to Groq API
        client = openai.OpenAI(api_key=GROK_API_KEY, base_url=GROQ_BASE_URL)

        system_prompt = (
            "You are a Forensic Cyber-Investigator for Vajra AI. Analyze for psychological triggers (Fear, Urgency, Greed). "
            "Flag 10-digit mobile numbers claiming to be institutions. "
            "Provide a RISK SCORE (0-100%) and a draft for a 1930 Cybercrime Portal complaint."
        )

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Context: {context}\n\nEvidence: {content}"}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"❌ API Error: {str(e)}")
        return None


# --- Tab 1: Home ---
with tab1:
    st.markdown("### 👁️ Vision")
    st.info("**Vajra AI protects you from 2026 threats like Digital Arrest, Voice Cloning, and Predatory Fine Print.**")
    st.markdown("### 📜 How to use:")
    st.markdown(
        "1. Choose a tab. \n2. Upload your file or paste text. \n3. Review the AI Risk Report. \n4. Use the draft to report to 1930.")

# --- Tab 2: Message Scan ---
with tab2:
    st.header("💬 Message Scanner")
    text_input = st.text_area("Paste SMS/WhatsApp message:", height=150)
    if st.button("Analyze Message"):
        if text_input:
            with st.spinner("Analyzing..."):
                st.write(analyze_with_ai("Text Message Fraud Analysis", text_input))

# --- Tab 3: Document Vault ---
with tab3:
    st.header("📄 Document & Image Vault")
    uploaded_doc = st.file_uploader("Upload PDF or Screenshot", type=["pdf", "png", "jpg"])
    if st.button("Run Document Forensics"):
        if uploaded_doc:
            with st.spinner("Scanning document..."):
                if uploaded_doc.type == "application/pdf":
                    reader = PyPDF2.PdfReader(uploaded_doc)
                    extracted_text = "".join([p.extract_text() for p in reader.pages])
                    st.write(analyze_with_ai("PDF Document Analysis", extracted_text[:8000]))
                else:
                    st.write(analyze_with_ai("Visual Evidence Check", f"Image file uploaded: {uploaded_doc.name}"))

# --- Tab 4: Vocal DNA ---
with tab4:
    st.header("🎙️ Vocal DNA Analyzer")
    uploaded_audio = st.file_uploader("Upload Audio Note", type=["mp3", "wav", "m4a"])
    if st.button("Scan Voice Patterns"):
        if uploaded_audio:
            st.audio(uploaded_audio)
            with st.spinner("Checking for AI artifacts..."):
                st.write(analyze_with_ai("Audio Voice Analysis", f"Audio file: {uploaded_audio.name}"))