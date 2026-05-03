# theme_utils.py
import streamlit as st

def apply_theme(theme: str):
    """Applies enterprise-grade light/dark mode themes with full UI coverage."""

    if theme == "Dark":
        dark_css = """
        <style>
        html, body, [class*="stAppViewContainer"], [class*="stMarkdown"], [data-testid="stAppViewContainer"] {
            background-color: #181a1b !important;
            color: #e0e0e0 !important;
        }

        [data-testid="stSidebar"], [class*="stSidebarContent"] {
            background-color: #1f1f1f !important;
            color: #e0e0e0 !important;
            border-right: 1px solid #333333 !important;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #00bcd4 !important;
        }

        .stButton>button {
            background-color: #00bcd4 !important;
            color: white !important;
            border-radius: 6px !important;
            border: none !important;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.3) !important;
        }

        .stButton>button:hover {
            background-color: #0099b8 !important;
        }

        [data-testid="stFileUploader"] section {
            background-color: #2b2b2b !important;
            border: 2px dashed #555555 !important;
            border-radius: 10px !important;
        }

        [data-testid="stFileUploader"] section:hover {
            border-color: #00bcd4 !important;
        }

        .stTextInput>div>div>input, textarea {
            background-color: #2a2a2a !important;
            color: #e0e0e0 !important;
            border: 1px solid #444444 !important;
            border-radius: 5px !important;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #202020 !important;
            border-radius: 10px !important;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.2) !important;
        }
        </style>
        """
        st.markdown(dark_css, unsafe_allow_html=True)

    elif theme == "Light":
        light_css = """
        <style>
        /* Main background + text */
        html, body, [class*="stAppViewContainer"], [class*="stMarkdown"], [data-testid="stAppViewContainer"] {
            background-color: #f8f9fb !important;  /* Dim soft white */
            color: #202124 !important;
        }

        /* Sidebar styling */
        [data-testid="stSidebar"], [class*="stSidebarContent"] {
            background-color: #f2f3f5 !important;
            color: #202124 !important;
            border-right: 1px solid #dcdcdc !important;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #007bff !important;
        }

        /* Buttons */
        .stButton>button {
            background-color: #007bff !important;
            color: white !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            border: none !important;
            box-shadow: 0px 3px 8px rgba(0,0,0,0.1) !important;
        }

        .stButton>button:hover {
            background-color: #005ec2 !important;
        }

        /* File uploader */
        [data-testid="stFileUploader"] section {
            background-color: #ffffff !important;
            border: 2px dashed #d0d0d0 !important;
            border-radius: 10px !important;
            transition: border-color 0.3s ease;
        }

        [data-testid="stFileUploader"] section:hover {
            border-color: #007bff !important;
        }

        /* Inputs and text areas */
        .stTextInput>div>div>input, textarea {
            background-color: #ffffff !important;
            color: #1a1a1a !important;
            border: 1px solid #cccccc !important;
            border-radius: 6px !important;
            box-shadow: 0px 1px 3px rgba(0,0,0,0.05) inset !important;
        }

        /* Cards and panels */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #ffffff !important;
            border-radius: 12px !important;
            box-shadow: 0px 3px 10px rgba(0,0,0,0.06) !important;
            padding: 1rem !important;
        }

        /* Streamlit alert/info boxes */
        [data-testid="stAlert"] {
            background-color: #e9f3ff !important;
            color: #202124 !important;
            border-left: 4px solid #007bff !important;
            border-radius: 6px !important;
        }
        </style>
        """
        st.markdown(light_css, unsafe_allow_html=True)

    else:
        st.markdown("<style>body{background-color:inherit;color:inherit;}</style>", unsafe_allow_html=True)
