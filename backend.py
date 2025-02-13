# backend.py for Valentine's Day Chatbot
import os
from fastapi import FastAPI, Request
from openai import OpenAI
from pydantic import BaseModel

# Load API key securely using os.environ.get()
api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a romantic and loving chatbot."},
                {"role": "user", "content": request.message}
            ]
        )
        answer = response.choices[0].message['content'].strip()
        return {"response": answer}
    except Exception as e:
        return {"response": f"Oops, something went wrong: {str(e)}"}
