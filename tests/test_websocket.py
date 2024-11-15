import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_websocket():
    with client.websocket_connect("/ws/question") as websocket:
        websocket.send_text("question|1")
        data = websocket.receive_text()
        assert "Answer to" in data