# backend.py for Valentine's Day Chatbot with In-Memory Checkpointer
import os
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

# Load API key
api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# In-memory Checkpointer (Store chat history)
chat_history = [
    {"role": "system", "content": "You are a romantic and loving chatbot designed by Siddharth for his beloved Suruu (Shruti). Speak warmly and lovingly."}
]

app = FastAPI()

# Request model
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Backend is working fine!"}

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        # Add user message to chat history
        chat_history.append({"role": "user", "content": request.message})

        # Get completion with entire chat history
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=chat_history
        )

        # Retrieve AI response
        answer = response.choices[0].message.content.strip()

        # Add assistant response to chat history
        chat_history.append({"role": "assistant", "content": answer})

        return {"response": answer}

    except Exception as e:
        return {"response": f"Oops, something went wrong: {str(e)}"}  
