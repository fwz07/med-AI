# ui_components.py
import streamlit as st


def sidebar_info():
    """Displays info text in the sidebar."""
    st.sidebar.markdown("## ⚙️ Settings")
    st.sidebar.markdown(
        "Upload your medical reports or bills for instant AI analysis."
    )
    st.sidebar.divider()


def section_header(title, emoji="💡"):
    """Renders a section header with emoji."""
    st.markdown(f"### {emoji} {title}", unsafe_allow_html=True)


def result_card(title, content, theme="Light", is_code=False):
    """Renders a result card with a soft white (or gray) box background."""
    if theme and theme.lower().startswith("dark"):
        # Dark theme styling
        card_bg = "#1e1e1e"       # soft gray card background
        title_color = "#7fe3ff"
        text_color = "#e6eef8"
        code_bg = "#2a2a2a"
        code_text = "#f1f1f1"
        shadow = "0 3px 8px rgba(0, 0, 0, 0.4)"
    else:
        # Light theme styling
        card_bg = "#ffffff"       # white box background
        title_color = "#007bff"
        text_color = "#0f172a"
        code_bg = "#f9fafc"       # slight contrast for code
        code_text = "#1a1a1a"
        shadow = "0 3px 10px rgba(0,0,0,0.08)"

    escaped = content.replace("<", "&lt;").replace(">", "&gt;")
    escaped = escaped.replace("\n", "<br>")

    if is_code:
        html = f"""
        <div style="
            background:{card_bg};
            border-radius:12px;
            padding:18px;
            margin-bottom:16px;
            box-shadow:{shadow};
        ">
            <h4 style="margin:0 0 10px 5px;color:{title_color};">{title}</h4>
            <pre style="
                background:{code_bg};
                color:{code_text};
                padding:14px;
                border-radius:8px;
                white-space:pre-wrap;
                overflow:auto;
                font-family:Consolas,Monaco,'Courier New',monospace;
                font-size:14px;
                box-shadow:inset 0 1px 4px rgba(0,0,0,0.05);
            ">{escaped}</pre>
        </div>
        """
    else:
        html = f"""
        <div style="
            background:{card_bg};
            border-radius:12px;
            padding:18px;
            margin-bottom:16px;
            box-shadow:{shadow};
        ">
            <h4 style="margin:0 0 10px 5px;color:{title_color};">{title}</h4>
            <div style="color:{text_color}; font-size:15px; line-height:1.6;">{escaped}</div>
        </div>
        """

    st.markdown(html, unsafe_allow_html=True)
