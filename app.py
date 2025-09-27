import streamlit as st
import time
import google.generativeai as genai

# --- Set API key ---
genai.configure(api_key="AIzaSyDhcBf0dk_a3cv9V1W9efdhjDuvd6Jk4a0")  # replace with your Gemini API key

# --- Page Setup ---
st.set_page_config(
    page_title="Study Bot 💡 BY ColourVOLT✨⚡",
    page_icon="✨⚡",
    layout="centered"
)

# --- CSS Styling ---
st.markdown("""
<style>
/* Background */
body {
    background: linear-gradient(to right, #fbc2eb, #a6c1ee);
    font-family: 'Arial', sans-serif;
}

/* Navbar */
.navbar {
    background: #6a11cb;
    padding: 12px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 15px;
    color: white;
    font-weight: bold;
    font-size: 20px;
}

/* Chat bubbles */
.user-bubble {
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
}

.bot-bubble {
    background: linear-gradient(120deg,#e0eafc,#cfdef3);
    padding:12px;
    border-radius:15px;
    margin:5px;
    text-align:left;
    color:black;
    max-width:80%;
    float:left;
    clear:both;
}

/* Floating clear chat button */
.clear-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #ff4b5c;
    color: white;
    border: none;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    font-size: 18px;
    cursor: pointer;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.3);
}
.clear-btn:hover {
    background: #ff1e38;
}

/* Mobile tweaks */
@media (max-width: 768px) {
    .user-bubble, .bot-bubble {
        max-width: 95%;
        font-size: 14px;
    }
    .navbar {
        font-size: 18px;
    }
}
</style>
""", unsafe_allow_html=True)

# --- Navbar ---
st.markdown("<div class='navbar'>📚 Study Bot 💡 by ColourVOLT ✨⚡</div>", unsafe_allow_html=True)

# --- Session State ---
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- Gemini Model ---
model = genai.GenerativeModel("gemini-1.5-flash")

# --- User Input ---
user_input = st.text_input("Type your question here...")

if st.button("Send") and user_input.strip() != "":
    st.session_state.chat.append(("user", user_input))

    with st.spinner("Study Bot is typing... ⏳"):
        try:
            response = model.generate_content(user_input)
            answer = response.text
        except Exception as e:
            answer = f"⚠️ Something went wrong: {str(e)}"

        st.session_state.chat.append(("bot", answer))

# --- Display Chat (latest on top) with typing effect ---
for role, msg in reversed(st.session_state.chat):
    if role == "user":
        st.markdown(f"<div class='user-bubble'>You: {msg}</div>", unsafe_allow_html=True)
    else:
        # Typing effect for bot messages
        placeholder = st.empty()
        full_text = ""
        for char in msg:
            full_text += char
            placeholder.markdown(f"<div class='bot-bubble'>Study Bot: {full_text}</div>", unsafe_allow_html=True)
            time.sleep(0.01)

# --- Floating Clear Chat Button ---
if st.button("🗑️", key="clear_chat"):
    st.session_state.chat = []
    st.rerun()

# --- Footer ---
st.markdown("<br><br><center>Made with ❤️ for Gen Z learners!</center>", unsafe_allow_html=True)