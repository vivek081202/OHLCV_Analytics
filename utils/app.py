# main.py
import streamlit as st
from streamlit_extras.colored_header import colored_header

st.set_page_config(
    page_title="TSLA Candlestick Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

pages = {
    "App Navigation": [
        st.Page("Home.py", title="Home", icon="🏠", default=True),
    ],
    "Modules": [
        st.Page("Chart.py", title="TSLA Chart Visualization", icon="📊"),
        st.Page("Chatbot.py", title="TSLA ChatBot", icon="🤖")
    ]
}

with st.sidebar:
    st.markdown("### 📅 About TSLA Dashboard")

    with st.expander("📈 Chart Features", expanded=True):
        st.markdown("""
        - Real-time Candlestick, Line & Bar Charts
        - 🟢 LONG and 🔴 SHORT directional markers
        - 🟩 Support and 🟥 Resistance Bands
        - 🔵 SMA (10-day Simple Moving Average)
        - 📆 Selectable 30-day Segments (Recent, Middle, Oldest)
        """)

    with st.expander("🤖 Gemini Stock Chatbot", expanded=False):
        st.markdown("""
        - Ask queries like: _"How many LONG days in 2023?"_
        - Context-aware Gemini 1.5 API integration
        - Partial data embedding with Smart Prompts
        """)

    st.markdown("---")
    st.caption("🔵 Developed using Python, Streamlit & Gemini API")


pg = st.navigation(pages)
pg.run()
