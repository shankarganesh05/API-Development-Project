from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.json().get('message')=="Welcome to the FastAPI Project!"
    assert res.statuscode == 200