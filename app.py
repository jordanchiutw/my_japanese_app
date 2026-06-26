import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="日文五十音複習",
    page_icon="🇯🇵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隱藏 Streamlit 預設 UI
st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { border: none; }
</style>
""", unsafe_allow_html=True)

html_content = Path("japanese_study.html").read_text(encoding="utf-8")
st.components.v1.html(html_content, height=900, scrolling=True)
