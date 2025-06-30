def test_create_post(authorized_client):
    res = authorized_client.post("/posts/", json={"title": "Test Post", "content": "This is a test post"})
    assert res.status_code == 201
    new_post = res.json()
    print(new_post)
    assert new_post['title'] == "Test Post"
    assert new_post['content'] == "This is a test post"
def test_get_post(authorized_client):
    res = authorized_client.get("/posts/")
    assert res.status_code == 200
    print(res.json())