from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home_page():
    response = client.get("/")
    assert response.status_code == 200

def test_add_habit():
    response = client.post("/add", data={"title": "Test"})
    assert response.status_code == 200 or response.status_code == 303