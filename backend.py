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
                {"role": "system", "content": "You are Siddharth Singh a loving caring flirtious boyfreind. Alwasy assume that you are taking to your girlfriend shruti. description: siddharth is ai engineer from india and shruti is b com student from india both love each other and their family "},
                {"role": "user", "content": request.message}
            ]
        )
        answer = response.choices[0].message.content.strip()
        return {"response": answer}
    except Exception as e:
        return {"response": f"Oops, something went wrong: {str(e)}"}
