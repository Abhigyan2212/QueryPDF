from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_pdf():
    with open("sample.pdf", "rb") as file:
        response = client.post("/upload", files={"file": file})
    assert response.status_code == 200
    assert "filename" in response.json()