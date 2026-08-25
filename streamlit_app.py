from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="微康核心菌株科研成果智查助手",
    page_icon="🔎",
    layout="wide",
)

portal_html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(portal_html, height=1400, scrolling=True)
