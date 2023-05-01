from fastapi.testclient import TestClient
from yagupov_fastapi.main import app
from yagupov_fastapi.settings import settings

def test_answer():
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {"status" : "ok"}
    