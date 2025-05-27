# TSLA Dashboard

A comprehensive dashboard for analyzing TSLA stock data using Streamlit and TradingView's Lightweight Charts.

## Features

- Interactive candlestick chart with TradingView's Lightweight Charts
- Support and resistance bands visualization
- Trading direction markers (LONG/SHORT)
- AI-powered chatbot for data analysis using Google's Gemini Pro
- Real-time data visualization

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
4. Place your TSLA data CSV file in the `data` directory as `TSLA.csv`

## Running the Application

```bash
streamlit run app.py
```

## Usage

1. **Chart Tab**
   - View the candlestick chart with support/resistance bands
   - Hover over candles to see detailed price information
   - Use the mouse wheel to zoom in/out
   - Click and drag to pan the chart

2. **AI Chatbot Tab**
   - Ask questions about the TSLA data
   - Get insights about price movements, trends, and patterns
   - Analyze trading signals and market conditions

## Data Format

The application expects a CSV file with the following columns:
- Date
- open
- high
- low
- close
- Volume
- direction (LONG/SHORT/None)
- Support (list of support prices)
- Resistance (list of resistance prices)

## Technologies Used

- Python
- Streamlit
- TradingView Lightweight Charts
- Google Gemini Pro API
- Pandas
