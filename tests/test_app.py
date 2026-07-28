from app import app
import pytest

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_employees(client):
    response = client.get("/employees")

    assert response.status_code == 200
    assert response.get_json() == [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Mary"}
    ]

