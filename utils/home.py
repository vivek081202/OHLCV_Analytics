# Home.py
import streamlit as st
from streamlit_extras.colored_header import colored_header

st.title("graph TSLA Intelligent Visualization")
colored_header("Welcome to the TSLA Intelligent Visualization Platform", description="Explore TSLA stock like never before with Smart Overlays, AI Chatbot, and Dynamic Charts.", color_name="blue-70")

st.image("../assets/stockimg.jpg")

st.markdown("""
### 🚀 What You Can Do Here:

- **View Beautiful Candlestick Charts** 📈 using TradingView-style interactive visualizations
- **Overlay Trade Signals** 🟢🔴 based on direction (LONG, SHORT, None)
- **Inspect Support & Resistance Zones** 🟩🟥 automatically parsed from CSV
- **Query the Dataset using Gemini AI** 🤖 for insights like bullish days, volume trends
- **Experience a Bonus TradingView Replay** 🎞️ animation-style candle playback (optional)

---

🔄 Navigate through the tabs from the sidebar to explore features.
""")

st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 14px; padding: 10px; color: #888;">
    <p><strong>TSLA Dashboard 📊</strong></p>
    <p>
        Interactive TradingView-style platform for TSLA stock analysis powered by smart visualizations and LLM insights.
    </p>
    <p>© 2025 | Built with ❤️ by the TSLA Dashboard Team using Python, Streamlit & Gemini API.</p>
</div>
""", unsafe_allow_html=True)