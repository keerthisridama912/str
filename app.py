
import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 Gemini AI Chatbot")
st.write("Ask Gemini anything!")

# Input box
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words..."
)

# Button
if st.button("Generate Response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.success("Response generated!")
        st.write(response.text)

    else:
        st.warning("Please enter a prompt.")

