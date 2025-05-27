import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import pandas as pd
import ast

MAX_Y = 1000
MIN_Y = 0

def safe_list_parse(val):
    try:
        result = ast.literal_eval(str(val))
        if isinstance(result, list):
            filtered = [float(x) for x in result if MIN_Y <= float(x) <= MAX_Y]
            return filtered if filtered else []
    except:
        return []
    return []

def plot_tsla_chart(df: pd.DataFrame):
    st.markdown("""
        <style>
            .chart-wrapper {
                background-color: #000;
                padding: 2rem;
                border-radius: 20px;
                box-shadow: 0 0 15px rgba(0,0,0,0.4);
                height: 600px;
            }
        </style>
    """, unsafe_allow_html=True)

    

    st.subheader("📈 TSLA Candlestick Chart with Indicators")
    st.markdown("This chart includes directional markers, support/resistance bands, and is interactively zoomable.")

    df['Support'] = df['Support'].apply(safe_list_parse)
    df['Resistance'] = df['Resistance'].apply(safe_list_parse)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Set date slider range strictly based on data
    full_min_date = df['timestamp'].min().date()
    full_max_date = df['timestamp'].max().date()

    date_range = st.slider("Select date range", min_value=full_min_date,
                           max_value=full_max_date,
                           value=(full_min_date, full_max_date))
    df = df[(df['timestamp'].dt.date >= date_range[0]) & (df['timestamp'].dt.date <= date_range[1])]

    # Dropdown after filtering
    view_option = st.selectbox("Select range to view (after date filter)", ["Last 30 days", "Last 90 days", "All"])
    if view_option == "Last 30 days":
        df = df.tail(30)
    elif view_option == "Last 90 days":
        df = df.tail(90)

    candlestick_data, markers, support_band, resistance_band, sma_data = [], [], [], [], []

    window = 10
    df['sma'] = df['close'].rolling(window=window).mean()

    for _, row in df.iterrows():
        ts = row['timestamp'].strftime("%Y-%m-%d")

        candlestick_data.append({
            "time": ts,
            "open": float(row['open']),
            "high": float(row['high']),
            "low": float(row['low']),
            "close": float(row['close'])
        })

        if not pd.isna(row['sma']):
            sma_data.append({"time": ts, "value": round(row['sma'], 2)})

        direction = str(row['direction']).upper() if pd.notna(row['direction']) else "NONE"
        if direction == 'LONG':
            markers.append({"time": ts, "position": "belowBar", "color": "green", "shape": "arrowUp", "text": "LONG"})
        elif direction == 'SHORT':
            markers.append({"time": ts, "position": "aboveBar", "color": "red", "shape": "arrowDown", "text": "SHORT"})
        else:
            markers.append({"time": ts, "position": "inBar", "color": "yellow", "shape": "circle", "text": "NO DIR"})

        if row['Support']:
            support_band.append({"time": ts, "value": min(row['Support']), "color": "rgba(0,255,0,0.2)"})
            support_band.append({"time": ts, "value": max(row['Support']), "color": "rgba(0,255,0,0.2)"})

        if row['Resistance']:
            resistance_band.append({"time": ts, "value": min(row['Resistance']), "color": "rgba(255,0,0,0.2)"})
            resistance_band.append({"time": ts, "value": max(row['Resistance']), "color": "rgba(255,0,0,0.2)"})

    series = [
        {
            "type": "Candlestick",
            "data": candlestick_data,
            "options": {
                "upColor": "#06f762",
                "downColor": "#ff0501",
                "borderUpColor": "#26a69a",
                "borderDownColor": "#ef5350",
                "wickUpColor": "#26a642",
                "wickDownColor": "#ff0400"
            }
        },
        {
            "type": "Area",
            "data": support_band,
            "options": {
                "color": "rgba(0,255,0,0.2)",
                "lineColor": "green",
                "lineWidth": 1,
                "title": f"Support"
            }
        },
        {
            "type": "Area",
            "data": resistance_band,
            "options": {
                "color": "rgba(255,0,0,0.2)",
                "lineColor": "red",
                "lineWidth": 1,
                "title": f"Resistance"
            }
        },
        {
            "type": "Line",
            "data": sma_data,
            "options": {
                "color": "#03a9f4",
                "lineWidth": 2,
                "lineStyle": 0,
                "title": f"SMA {window}"
            }
        }
    ]

    renderLightweightCharts(
        charts=[{
            "series": series,
            "markers": markers,
            "chart": {
                "height": 500,
                "layout": {
                    "background": {"type": "solid", "color": "#1e1e1e"},
                    "textColor": "#ffffff"
                },
                "rightPriceScale": {
                    "scaleMargins": {"top": 0.2, "bottom": 0.1}
                },
                "timeScale": {"timeVisible": True}
            }
        }]
    )
