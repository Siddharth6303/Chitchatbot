# Valentine's Day Special: Romantic Chatbot for Shruti from Siddharth
# Save this file as frontend.py
import streamlit as st
import requests
import random
from datetime import datetime

# Romantic Theme
st.set_page_config(page_title="❤️ Chat with Your Sid, Happy Valentine's Day", page_icon="💌", layout="centered")
st.title("💖 Chat with Sid")
st.write("*Hey Suruu, I’m always here for you, no matter the distance. 💕*")

# Background Styling
st.markdown(
    """
    <style>
    body {background-color: #fff0f5;}
    .stChatMessage {border-radius: 20px; padding: 10px;}
    .stButton>button {background-color: #ffb6c1; color: white; font-size:16px; border-radius: 12px;}
    </style>
    """,
    unsafe_allow_html=True
)

# Store chat history
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Display chat history
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Personalized greetings for Suruu
hour = datetime.now().hour
if hour < 12:
    greeting = "Good morning, my sunshine Suruu ☀️"
elif hour < 18:
    greeting = "Good afternoon, my sweetest Suruu 💖"
else:
    greeting = "Good evening, my starry Suruu 🌙"
st.markdown(f"**{greeting}**")

# Input and Backend Call
user_input = st.chat_input("What's on your mind, Suruu? 💬")
BACKEND_URL = "https://chitchatbot-pm4j.onrender.com/chat"  # Update after deployment

if user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = requests.post(BACKEND_URL, json={"message": user_input})
        bot_response = response.json().get("response", "Suruu, you are always on my mind! 💖")
    except Exception:
        bot_response = "Can't reach my heart (backend) right now, but I love you, Suruu! ❤️"
    
    st.session_state['messages'].append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# Add a footer
st.markdown("---")
st.markdown("*Made with ❤️ by Siddharth for his beloved Suruu (Shruti).*")
