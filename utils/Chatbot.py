# Chatbot.py

import streamlit as st
from data_loader import load_tsla_data
from streamlit_extras.colored_header import colored_header
import google.generativeai as genai
import pandas as pd
from dotenv import load_dotenv

# Load secrets/environment
load_dotenv()
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Cache a preview for context
@st.cache_data(show_spinner=False)
def format_df_for_context(df: pd.DataFrame) -> str:
    return df.to_csv(index=False)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Header
st.title("🤖 TSLA Chatbot")
colored_header(
    "Query the Dataset using Gemini LLM",
    description="Ask financial insights about TSLA directly using LLM.",
    color_name="blue-70"
)

st.markdown("""
This chatbot is powered by **Google Gemini Pro**, designed to respond to analytical queries on TSLA stock dataset.

💡 **Example Questions**:
- How many days in 2023 were TSLA stocks bullish?
- What was the average volume when TSLA closed higher than it opened?
- How many LONG signals were there in January 2022?
""")

# Load TSLA data
with st.spinner("Loading Gemini chatbot..."):
    df = load_tsla_data()

# Display context preview toggle
with st.expander("📄 Preview TSLA Dataset Context Sent to LLM"):
    st.dataframe(df.head(50))


# Header
colored_header(
    "Gemini-Powered TSLA Chatbot",
    description="Ask financial insights about TSLA directly using LLM.",
    color_name="blue-70"
)

# Load TSLA data
with st.spinner("Loading dataset..."):
    df = load_tsla_data()
    context = format_df_for_context(df)

# Show chat history
for entry in st.session_state.chat_history:
    st.chat_message("user").write(entry["user"])
    st.chat_message("assistant").write(entry["bot"])

# Chat input
prompt = st.chat_input("Ask something about TSLA dataset")

if prompt:
    st.chat_message("user").write(prompt)

    full_prompt = f"""
    You are a financial data analyst and assistant.

    You will be shown a preview of TSLA stock dataset. Your job is to analyze the dataset context using reasoning and respond to user questions in detail relevance with high accuracy. Do not return Python code unless specifically asked.

    You need to memorize you previous responses as well in the current sessions, So that in case any user asks Query refereing to previous query you could answer well.
    
    You have to generate appropriate and accurate visualizations where ever required relevant with query.

    Context Data (Whole TSLA Dataset):
    {context}

    Now answer the following user query using insights and calculation from the whole dataset.

    User Query: {prompt}
    """

    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(full_prompt)
            reply = response.text.strip()
            st.chat_message("assistant").write(reply)

            # Save to history
            st.session_state.chat_history.append({
                "user": prompt,
                "bot": reply
            })

        except Exception as e:
            st.error(f"Error: {e}")

st.caption("🤖 Powered by Gemini | 🧠 Context-aware multi-turn Q&A")
