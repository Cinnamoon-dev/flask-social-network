from tests import app, client

def test(app, client):
    with app.app_context():
        response = client.get("/user/all")
        data = response.get_json()

        assert data.get("users") == []