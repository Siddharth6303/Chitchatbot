# Step 1: Frontend (Streamlit) for Chatbot
# Save this file as streamlit_app.py
import streamlit as st
import requests

st.title("AI Chatbot")
st.write("Chat with an AI powered by LangGraph and OpenAI")

# Chat history storage
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

user_input = st.chat_input("Type your message...")
BACKEND_URL = "https://your-backend-url/chat"  # Update after deployment

if user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    response = requests.post(BACKEND_URL, json={"message": user_input})
    bot_response = response.json().get("response", "No response from backend")
    st.session_state['messages'].append({"role": "assistant", "content": bot_response})
    
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# Step 2: Create requirements.txt
# Content of requirements.txt:
# streamlit
# requests

# Step 3: Deploy on Streamlit Community Cloud
# 1. Push this file and requirements.txt to a GitHub repository.
# 2. Go to https://share.streamlit.io, log in, and click 'New app'.
# 3. Select your repository and branch, then click 'Deploy'.
