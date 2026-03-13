from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_submit_user_profile():
    """Verify that user submission endpoint accepts valid data."""

    payload = {
        "name": "Tim",
        "email": "timothey@test.com",
        "experience_level": "Mid-level (2-5 years)",
        "primary_stack": "Backend Development",
        "preferred_duration": "Short-term (1-3 months)",
        "skills": "Java",
        "projects": [1, 2, 3],
        "availability_confirmed": True
    }

    response = client.post("/users/submit", json=payload)

    assert response.status_code == 200
    assert response.json()["message"] == "Profile saved successfully"


def test_submit_user_profile_without_projects():
    """Verify that submission fails when no projects are selected."""

    payload = {
        "name": "Tim",
        "email": "timothey@test.com",
        "experience_level": "Mid-level (2-5 years)",
        "primary_stack": "Backend Development",
        "preferred_duration": "Short-term (1-3 months)",
        "skills": "Java",
        "projects": [],
        "availability_confirmed": True
    }

    response = client.post("/users/submit", json=payload)

    assert response.status_code == 422
