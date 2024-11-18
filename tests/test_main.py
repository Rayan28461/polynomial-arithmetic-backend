from fastapi.testclient import TestClient

from src.config import Config
from src.main import app

client = TestClient(app)


class TestMain:
    def test_root(self) -> None:
        response = client.get("/")
        assert response.status_code == 200
        assert response.content != None

    def test_app_successful(self) -> None:
        assert app.title == Config.APP.TITLE
        assert app.description == Config.APP.DESCRIPTION
        assert app.version == Config.APP.VERSION
