import google.generativeai as genai
import streamlit as st
import time

# --- Set API key ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- Debug: List available models ---
models = genai.list_models()
st.write("✅ Available Models:")
for m in models:
    st.write(m.name)
