from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_projects_endpoint():
    """Verify that GET /projects returns a successful response."""
    response = client.get("/projects")

    assert response.status_code == 200
