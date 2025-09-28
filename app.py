import streamlit as st
import time
import google.generativeai as genai

# --- Set API key ---
genai.configure(api_key="YOUR_API_KEY_HERE")  # replace with your Gemini API key

# --- Page Setup ---
st.set_page_config(
    page_title="Study Bot 💡 BY ColourVOLT✨⚡",
    page_icon="✨⚡",
    layout="centered"
)

# --- CSS Styling ---
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #fbc2eb, #a6c1ee);
}
input, textarea {
    border-radius: 12px;
    padding: 8px;
}
button {
    background-color: #6a11cb;
    color: white;
    padding: 8px 16px;
    border-radius: 12px;
    border: none;
    cursor: pointer;
}
button:hover {
    background-color: #2575fc;
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
