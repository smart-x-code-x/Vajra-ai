# Vajra AI: The Digital Kavach

## Introduction
**Vajra AI** is your digital bodyguard, engineered to protect users from modern online threats such as Digital Arrests, AI Voice Cloning, and Predatory Documents. Acting as an automated Forensic Cyber-Investigator, Vajra AI leverages the power of the Grok API to detect psychological manipulation (Fear, Urgency, Greed), flag fraudulent institutional actors, and automatically draft formal complaints for the National Cybercrime Portal (1930).

## System Requirements
- **OS:** Windows / macOS / Linux
- **Python:** 3.8+ 
- **API Access:** A valid Grok API Key (xAI)
- **Internet:** Active connection required for API processing

## Detailed Setup Instructions

1. **Prepare your Workspace**
   Ensure `app.py` is saved in your project directory (e.g., `D:\vajra ai\`).

2. **Configure your API Key**
   Open `app.py` in your code editor. 
   At the very top of the file, locate the `GROK_API_KEY` variable and replace `"PASTE_YOUR_KEY_HERE"` with your actual Grok API key:
   ```python
   # 1. The "Invisible" API Logic
   GROK_API_KEY = "xai-your-api-key-here"
   ```

3. **Install Dependencies**
   Install the required Python packages using pip:
   ```bash
   pip install streamlit openai PyPDF2
   ```

4. **Launch the Application**
   Run the Streamlit server from your terminal:
   ```bash
   cd "D:\vajra ai"
   streamlit run app.py
   ```
   The application will automatically open in your default web browser.

## How to use the scanner

- **Message Scan (Text & SMS):** 
  Navigate to the "Message Scan" tab. Paste any suspicious SMS, WhatsApp message, or Email into the text area. Click **Run Forensic Text Scan** to analyze the text for psychological manipulation and institutional spoofing. The engine will supply a forensic report and a drafted 1930 complaint.
- **Document Vault (PDFs & Images):** 
  Go to the "Document Vault" tab. Upload a suspicious PDF (such as a fake CBI notice or loan agreement) or image. Click **Analyze Document Artifacts**. If it's a PDF, the text will be extracted via PyPDF2 and scanned for hidden predatory clauses.
- **Vocal DNA (Audio):** 
  In the "Vocal DNA" tab, upload an audio clip (e.g., a forwarded WhatsApp voice note). Click **Analyze Vocal DNA** to obtain forensic guidelines regarding AI voice cloning artifacts and synthetic anomalies.
