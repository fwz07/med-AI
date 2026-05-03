# app.py — GPT-only version (OpenAI API)
import streamlit as st
import warnings
from ai_agent import create_med_ai_agent
from ui_components import section_header, result_card
from utils import extract_text_from_file
from settings import app_settings
from theme_utils import apply_theme
import os

warnings.filterwarnings("ignore", category=UserWarning, module="langchain")

st.set_page_config(page_title="Med AI Enterprise", layout="wide", page_icon="🧠")

st.markdown(
    """
    <h1 style='text-align:center;
               font-weight:800;
               background: linear-gradient(to right, #007bff, #00bcd4);
               -webkit-background-clip: text;
               -webkit-text-fill-color: transparent;'>
     Med AI — Enterprise Health Coach
    </h1>
    """,
    unsafe_allow_html=True,
)

# Load user settings and apply theme
user_settings = app_settings()
apply_theme(user_settings["theme"])

# ✅ Check OpenAI API key connectivity
# Load API key from secrets or environment
api_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))
if api_key:
    st.sidebar.success("🟢 Connected to Groq API (LLaMA 3 70B — Free & Fast)")
else:
    st.sidebar.error("🔴 No Groq API key found — add it in .streamlit/secrets.toml")

# Always use Groq’s best free model
selected_model = "llama-3.1-8b-instant"

# Initialize the Med AI agent (Groq-based)
agent_executor = create_med_ai_agent(
    model_name=selected_model,
    temperature=user_settings["temperature"],
)
# Apply theme color tweaks
if user_settings["theme"] == "Dark":
    st.markdown("<style>body{background-color:#1e1e1e;color:white;}</style>", unsafe_allow_html=True)
elif user_settings["theme"] == "Light":
    st.markdown("<style>body{background-color:white;color:black;}</style>", unsafe_allow_html=True)

# -------------------- MAIN INTERFACE --------------------
st.write("### Upload your medical document or bill:")
file = st.file_uploader("Upload File (.txt or .pdf)", type=["txt", "pdf"])

if file:
    file_text = extract_text_from_file(file)
    col1, col2 = st.columns(2)

    with col1:
        mode = st.radio("Select Task:", ["Full Medical Analysis", "Bill Analyzer"])

    with col2:
        run = st.button("🚀 Run AI Analysis")

    if run:
        if not file_text:
            st.error("📄 No text could be extracted from the uploaded file.")
        else:
            with st.spinner("🤖 Processing document..."):
                try:
                    # Bill Analyzer path
                    if mode == "Bill Analyzer":
                        section_header("Medical Bill Insights", "📑")
                        try:
                            bill_result = agent_executor["bill_agent"].invoke({"text": file_text})
                        except Exception as e:
                            st.exception(e)
                            bill_result = f"Error invoking bill_agent: {e}"
                        result_card("Bill Analysis", str(bill_result))

                    # Full Medical Analysis path
                    else:
                        if user_settings["run_mode"] == "Parallel":
                            section_header("Full Medical Analysis (Parallel)", "🩺")
                            try:
                                parallel_result = agent_executor["parallel_agent"].invoke({"text": file_text})
                            except Exception as e:
                                st.exception(e)
                                parallel_result = None

                            if isinstance(parallel_result, dict):
                                result_card("🧾 Bill Analysis", parallel_result.get("bill_analysis", "No bill_analysis key"))
                                result_card("📋 Medical Summary", parallel_result.get("medical_summary", "No medical_summary key"))
                                result_card("💊 Price Estimation", parallel_result.get("price_estimation", "No price_estimation key"))
                                if user_settings["enable_advice"]:
                                    result_card("💡 Health Advice", parallel_result.get("health_advice", "No health_advice key"))
                            else:
                                st.warning("Parallel agent did not return a dict. Showing raw output instead.")
                                result_card("Parallel Output (raw)", str(parallel_result))

                        # Sequential mode
                        else:
                            section_header("Sequential Medical Pipeline", "🧬")

                            # Step 1 – Medical summary
                            try:
                                med_summary = agent_executor["medical_agent"].invoke({"text": file_text})
                            except Exception as e:
                                st.exception(e)
                                med_summary = f"Error invoking medical_agent: {e}"
                            result_card("📋 Medical Summary", str(med_summary))

                            # Step 2 – Price estimation
                            try:
                                price_input = med_summary if isinstance(med_summary, str) else str(med_summary)
                                price_info = agent_executor["price_agent"].invoke({"text": price_input})
                            except Exception as e:
                                st.exception(e)
                                price_info = f"Error invoking price_agent: {e}"
                            result_card("💊 Price Estimation", str(price_info))

                            # Step 3 – Advice (optional)
                            if user_settings["enable_advice"]:
                                try:
                                    advice_input = med_summary if isinstance(med_summary, str) else str(med_summary)
                                    advice = agent_executor["advice_agent"].invoke({"text": advice_input})
                                except Exception as e:
                                    st.exception(e)
                                    advice = f"Error invoking advice_agent: {e}"
                                result_card("💡 Health Advice", str(advice))

                except Exception as outer_e:
                    st.error("An unexpected error occurred during analysis.")
                    st.exception(outer_e)
else:
    st.info("📤 Upload a document or bill to start the AI analysis.")

# Footer
st.markdown(
    "<p style='text-align:center;font-size:13px;color:gray;'>© 2025 Med AI Health Systems — Powered by OpenAI GPT-4o + LangChain</p>",
    unsafe_allow_html=True,
)
