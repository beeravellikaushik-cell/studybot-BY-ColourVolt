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
        background-color: #0d0d0d; /* Dark mode base */
        background-image: 
            radial-gradient(circle at 10% 20%, transparent 0, transparent 5px, #0d0d0d 5px),
            radial-gradient(circle at 90% 80%, transparent 0, transparent 5px, #0d0d0d 5px),
            radial-gradient(circle at 50% 50%, transparent 0, transparent 5px, #0d0d0d 5px);
        background-size: 150px 150px;
        color: white;
    }

    /* Add floating thunderbolts */
    .thunder {
        position: fixed;
        font-size: 18px;
        color: #FFD700;
        animation: float 6s linear infinite;
        opacity: 0.7;
    }

    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0.7; }
        50% { transform: translateY(-20px) rotate(15deg); opacity: 1; }
        100% { transform: translateY(0px) rotate(-15deg); opacity: 0.7; }
    }
    </style>

    <!-- Place thunder icons randomly -->
    <div class="thunder" style="top:10%; left:15%;">⚡</div>
    <div class="thunder" style="top:30%; left:70%;">⚡</div>
    <div class="thunder" style="top:60%; left:40%;">⚡</div>
    <div class="thunder" style="top:80%; left:20%;">⚡</div>
    <div class="thunder" style="top:50%; left:85%;">⚡</div>
""", unsafe_allow_html=True)

# ==============================
# ⚡ App Title
# ==============================
st.title("⚡ Study Bot - Powered by ColourVolt ⚡")

st.markdown("Ask me anything and I'll drop knowledge bombs! 💥")

# --- Gemini Model (latest working one) ---
model = genai.GenerativeModel("models/gemini-2.5-flash")

# --- User Input ---
user_input = st.text_input("Ask me anything:")

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
