import google.generativeai as genai
import streamlit as st
import time

# --- Set API key ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- Debug: List available models ---
models = genai.list_models()
for m in models:
    print(m.name)   # this will show in terminal logs
