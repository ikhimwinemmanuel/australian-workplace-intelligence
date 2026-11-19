from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel, StringConstraints


app = FastAPI()
class ChatRequest(BaseModel):
    question: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=1,
            max_length=2000,
        ),
    ]


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/chat")
async def chat(request: ChatRequest):
    return {
        "answer": f"You asked: {request.question}"
    }