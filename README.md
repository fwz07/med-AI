# Med AI: Enterprise Health Coach
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white)

An agentic AI approach to medical document analysis and expense optimization. This enterprise-grade web application translates complex medical data into clear, actionable, and financially relevant insights using high-speed LLM inference.

## 🚀 Key Features

*   **Dual-Path Document Extraction:** Implements a robust ingestion pipeline that attempts fast digital text extraction via PyPDF2, automatically falling back to a Tesseract-OCR and pdf2image pipeline for scanned PDFs.
*   **Full Medical Analysis:** Utilizes a sequential LangChain architecture to provide a diagnostic summary, estimate medication and consultation costs (in INR), and deliver actionable health advice.
*   **Medical Bill Auditor:** Deploys a specialized billing agent to analyze line items, detect potential overcharges, calculate billing accuracy percentages, and recommend refunds.
*   **Enterprise UI:** A custom-themed, modular Streamlit interface featuring adjustable AI creativity settings, parallel/sequential run modes, and Light/Dark themes.
*   **High-Speed Inference:** Powered by the Groq API (LLaMA 3) to ensure near-instantaneous, real-time responses without the latency of local models.

## 🛠️ Tech Stack

*   **Frontend:** Streamlit
*   **AI/Backend:** LangChain (`RunnableSequence`, `RunnableParallel`), Groq API (`ChatGroq`)
*   **Data Processing:** Python, PyPDF2, Pytesseract, pdf2image, Pillow

## 📋 System Prerequisites

Because this application uses advanced Optical Character Recognition (OCR) for scanned medical documents, you **must** install the following system-level dependencies before running the app:

1.  **Tesseract-OCR:** Download and install the Tesseract binaries. You must add the Tesseract installation folder (e.g., `C:\Program Files\Tesseract-OCR`) to your system's PATH environment variables.
2.  **Poppler:** Download the Poppler for Windows binaries. Extract the folder and add the `Library\bin` directory to your system's PATH environment variables.

## 💻 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/fwz07/Med-AI.git](https://github.com/fwz07/Med-AI.git)
   cd Med-AI
Install Python dependencies:

Bash
pip install -r requirements.txt
Configure API Keys:
Create a .streamlit folder in the root directory, and inside it, create a secrets.toml file. Add your Groq API key like this:

Ini, TOML
GROQ_API_KEY = "your_groq_api_key_here"
Launch the Application:

Bash
streamlit run app.py
## 📂 Usage Guide
Upload a .txt or .pdf file (up to 200MB limit) via the drag-and-drop interface. Select either "Full Medical Analysis" or "Bill Analyzer" to initiate the LangChain workflow.

## Developed by 
**Fawaz Peer Mohamed Sheik**
