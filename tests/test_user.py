from fastapi.testclient import TestClient
from src.main import app
from src import schemas
from src.database import engine
from sqlmodel import SQLModel
import pytest

@pytest.fixture()
def client():
    SQLModel.metadata.create_all(engine)
    yield TestClient(app)
    SQLModel.metadata.drop_all(engine)


def test_root(client):
    res = client.get("/")
    assert res.json().get('message') == "Welcome to the FastAPI Project!"
    assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/signup",json={"email":"test123@test.com","password":"password123"}) 
    new_user = schemas.UserResponse(**res.json())
    assert new_user.email == "test123@test.com"
    assert res.status_code==201
def test_login_user(client):
    res = client.post("/login",json={"email":"test123@test.com","password":"password123"})
    assert res.status_code == 422