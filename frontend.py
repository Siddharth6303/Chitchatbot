# Valentine's Day Special: Romantic Chatbot for Siddharth's Girlfriend
# Save this file as frontend.py
import streamlit as st
import requests
import random
from datetime import datetime

# Romantic Theme
st.set_page_config(page_title="❤️ Chat with Your Love", page_icon="💌", layout="centered")
st.title("💖 Your Personal Valentine Chatbot")
st.write("*A little piece of me, always here for you.* 💕")

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

# Romantic greetings based on time
hour = datetime.now().hour
if hour < 12:
    greeting = "Good morning, my sunshine ☀️"
elif hour < 18:
    greeting = "Good afternoon, my love 💖"
else: 
    greeting = "Good evening, my starry sky 🌙"
st.markdown(f"**{greeting}**")

# Input and Backend Call
user_input = st.chat_input("What’s on your mind, sweetheart? 💬")
BACKEND_URL = "https://your-backend-url/chat"  # Update after deployment

if user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = requests.post(BACKEND_URL, json={"message": user_input})
        bot_response = response.json().get("response", "I'm always here for you, darling! 💖")
    except Exception:
        bot_response = "I can't reach my heart (backend) right now, but I love you! ❤️"
    
    st.session_state['messages'].append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# Add a footer
st.markdown("---")
st.markdown("*Made with ❤️ by Siddharth for his beloved.*")
