# settings.py — simplified for GPT-only use
import streamlit as st

def app_settings():
    st.sidebar.markdown("## ⚙️ Application Settings")

    with st.sidebar.expander("🧠 AI Model Settings", expanded=True):
        st.markdown("**Using Groq**")
        temperature = st.slider(
            "AI Creativity (Temperature)",
            0.0,
            1.0,
            0.3,
            help="Higher = more creative, lower = more factual."
        )

    with st.sidebar.expander("🩺 Health Analysis Settings", expanded=False):
        enable_advice = st.checkbox("Enable Health Advice", value=True)
        run_mode = st.radio("Agent Run Mode", ["Sequential", "Parallel"], index=0)

    with st.sidebar.expander("🎨 Appearance Settings", expanded=False):
        theme = st.selectbox(
            "Theme Mode",
            ["Light", "Dark", "System Default"],
            index=2,
        )

    return {
        "model": "gpt-4o-mini",
        "temperature": temperature,
        "enable_advice": enable_advice,
        "run_mode": run_mode,
        "theme": theme,
    }
