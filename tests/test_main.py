import sys
import os

# اضافه کردن مسیر ریشه به sys.path برای شناسایی فایل main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert response.json() == {"detail": "User registered successfully"}

def test_login_user():
    client.post("/register", json={"username": "testuser", "password": "testpass"})
    response = client.post("/login", data={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()
