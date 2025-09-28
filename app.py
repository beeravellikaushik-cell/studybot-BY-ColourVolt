import streamlit as st
import time
import google.generativeai as genai

# --- Set API key ---
genai.configure(api_key="AIzaSyBbuapBRkFgPLwXIwIWdxwXvdtq4cRkFm0")  # replace with your Gemini API key
# ==============================
st.markdown("""
    <style>
    body {
        background-color: #0d0d0d; /* Sleek dark background */
        background-image: 
            radial-gradient(circle at 10% 20%, #FFD700 2px, transparent 2px),
            radial-gradient(circle at 90% 80%, #FFD700 2px, transparent 2px),
            radial-gradient(circle at 50% 50%, #FFD700 2px, transparent 2px),
            radial-gradient(circle at 70% 30%, #FFD700 2px, transparent 2px),
            radial-gradient(circle at 30% 70%, #FFD700 2px, transparent 2px);
        background-size: 150px 150px; /* space out thunder sparks */
        color: white;
    }
    .stApp {
        background: inherit;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================
# ⚡ App Title
# ==============================
st.title("⚡ Study Bot - Powered by ColourVolt ⚡")

# ==============================
# 📝 User Input
# ==============================
user_input = st.text_input("Ask me anything:")

if user_input:
    try:
        # Create model instance
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Generate response
        response = model.generate_content(user_input)

        # Show output
        st.subheader("💡 Answer:")
        st.write(response.text)

    except Exception as e:
        st.error(f"⚠️ Something went wrong: {e}")
