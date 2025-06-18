import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Validate API key
if api_key is None:
    st.error("API key not found. Did you set OPENROUTER_API_KEY in .env?")
    st.stop()

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# Streamlit UI
st.title("💬 Chirag's Chatbot")
st.caption("Powered by Streamlit + OpenRouter")

# Session state to hold chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from OpenRouter
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528-qwen3-8b:free",
            messages=st.session_state.messages,
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error: {e}"

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
