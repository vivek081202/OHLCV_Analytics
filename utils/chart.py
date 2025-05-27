# Chart.py
import streamlit as st
import pandas as pd
from chart_plotter import plot_tsla_chart
from streamlit_extras.colored_header import colored_header
import ast

colored_header("TSLA Candlestick Chart", description="Interactive stock chart with trade signals, support & resistance overlays.", color_name="blue-70")

st.markdown("""
Interactive TradingView-style chart with:

- 🟢 LONG and 🔴 SHORT directional markers
- 🟩 Support and 🟥 Resistance Bands
- 🔵 SMA (10-day Simple Moving Average) line
- 📆 Selectable 30-day windows (Recent, Middle, Oldest)
""")

def load_data():
    df = pd.read_csv("../data/TSLA_data_final.csv")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Convert support/resistance string lists to actual lists of floats
    df['Support'] = df['Support'].apply(lambda x: list(map(float, ast.literal_eval(x))) if pd.notna(x) else [])
    df['Resistance'] = df['Resistance'].apply(lambda x: list(map(float, ast.literal_eval(x))) if pd.notna(x) else [])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by='timestamp')
    df.reset_index(drop=True, inplace=True)
    return df

with st.spinner("Loading chart data..."):
    df = load_data()
    plot_tsla_chart(df)

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

