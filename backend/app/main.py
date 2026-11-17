from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()
class ChatRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/chat")
async def chat(request: ChatRequest):
    return {
        "answer": f"You asked: {request.question}"
    }