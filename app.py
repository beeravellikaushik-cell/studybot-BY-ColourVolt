import streamlit as st
import time
import google.generativeai as genai

# --- Set API key ---
genai.configure(api_key="AIzaSyBbuapBRkFgPLwXIwIWdxwXvdtq4cRkFm0")  # replace with your Gemini API key

st.set_page_config(
    page_title="Study Bot 💡 BY ColourVOLT✨⚡",
    page_icon="✨⚡",
    layout="centered"
)

# --- CSS Styling ---
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

# --- Session State ---
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- Title ---
st.title("Study Bot 💡")
st.markdown("Ask me anything and I'll drop knowledge bombs! 💥")

# --- Gemini Model (latest working one) ---
model = genai.GenerativeModel("models/gemini-2.5-flash")

# --- User Input ---
user_input = st.text_input("Type your question here...")

if st.button("Send") and user_input.strip() != "":
    st.session_state.chat.append(("user", user_input))

    with st.spinner("Study Bot is typing... ⏳"):
        time.sleep(1.2)
        try:
            response = model.generate_content(user_input)
            answer = response.text
        except Exception as e:
            answer = f"⚠️ Something went wrong: {str(e)}"

        st.session_state.chat.append(("bot", answer))

# --- Display Chat (latest on top) ---
for role, msg in reversed(st.session_state.chat):
    if role == "user":
        st.markdown(f"""
        <div style='
            background: linear-gradient(120deg,#a6c0fe,#f68084);
            padding:12px;
            border-radius:15px;
            margin:5px;
            text-align:right;
            color:white;
            font-weight:bold;
            max-width:80%;
            float:right;
            clear:both;
        '>
            You: {msg}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='
            background: linear-gradient(120deg,#e0eafc,#cfdef3);
            padding:12px;
            border-radius:15px;
            margin:5px;
            text-align:left;
            color:black;
            max-width:80%;
            float:left;
            clear:both;
        '>
            Study Bot: {msg}
        </div>
        """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("Made with ❤️ for Gen Z learners!")
