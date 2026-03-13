import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from src.main import app
import uuid

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}


def test_register_user():
    email = f"{uuid.uuid4()}@test.com"

    response = client.post(
        "/users/register",
        json={
            "email": email,
            "password": "test123"
        }
    )

    assert response.status_code == 200

def test_login_user():
    response = client.post(
        "/users/login",
        json={
            "email": "test@example.com",
            "password": "test123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()