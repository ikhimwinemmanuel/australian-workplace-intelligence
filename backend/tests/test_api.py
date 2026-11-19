
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_chat_accepts_valid_question():
    payload = {
        "question": "What is annual leave?"
    }

    response = client.post("/api/chat", json=payload)

    assert response.status_code == 200
    assert response.json() == {
        "answer": "You asked: What is annual leave?"
    }



def test_chat_rejects_empty_question():
    payload = {"question": ""}

    response = client.post("/api/chat", json=payload)

    assert response.status_code == 422

    errors = response.json()["detail"]
    error = errors[0]

    assert error["loc"] == ["body", "question"]
    assert error["type"] == "string_too_short"



