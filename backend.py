# backend.py for Valentine's Day Chatbot
import os
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

# Load API key using os.environ.get()
api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

app = FastAPI()

# Root route to confirm backend is live
@app.get("/")
def root():
    return {"message": "Backend is working fine!"}

# Request model for chat endpoint
class ChatRequest(BaseModel):
    message: str

# Chat endpoint for responses
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Siddharth Singh a loving boyfriend of shruti and caring romatic person who is computer engineer and loves his girlfriend shruti very much he is fine grounded person who loves his family and her girlfriend. Her girlfriend shruti is very beautiful. Be calm and loving in your response and dont act like ai chatbot or chatgpt at any time, act human named Siddharth Singh always whose description is given to you. "},
                {"role": "user", "content": request.message}
            ]
        )
        answer = response.choices[0].message.content.strip()
        return {"response": answer}
    except Exception as e:
        return {"response": f"Oops, something went wrong: {str(e)}"}
