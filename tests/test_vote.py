def test_vote(authorized_client, post_data):
    res = authorized_client.post("/vote",json={"post_id": post_data['id'], "dir": True})
    assert res.status_code == 201
    print(res.json())