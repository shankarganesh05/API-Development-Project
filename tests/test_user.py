from src import schemas

def test_root(client):
    res = client.get("/")
    assert res.json().get('message') == "Welcome to the FastAPI Project!"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/signup",json={"email":"test123@test.com","password":"password123"}) 
    new_user = schemas.UserResponse(**res.json())
    assert new_user.email == "test123@test.com"
    assert res.status_code==201

def test_login_user(client,test_user):
    res = client.post("/login",data={"username":test_user['email'],"password":test_user['password']})
    print(res.json())
    assert res.status_code == 200