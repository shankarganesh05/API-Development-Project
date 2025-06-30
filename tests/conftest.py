from fastapi.testclient import TestClient
from src.main import app
from src.database import engine
from sqlmodel import SQLModel
import pytest

@pytest.fixture()
def client():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    yield TestClient(app)
    
@pytest.fixture()
def test_user(client):
    user_data = {
        "email": "test123@test.com",
        "password": "password123"
    }
    res = client.post("/users/signup", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
      # Ensure password is set for login
    assert new_user['email'] == user_data["email"]
    new_user['password'] = user_data['password']
    return new_user
@pytest.fixture()
def token(client,test_user):
    res = client.post("/login",data={"username":test_user['email'],"password":test_user['password']})
    assert res.status_code == 200
    return res.json()['access_token']
@pytest.fixture()
def authorized_client(client,token):
    client.headers = {**client.headers,"Authorization": f"Bearer {token}"}
    return client