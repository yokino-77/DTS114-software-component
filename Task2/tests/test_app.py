from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[2]
GENERATED_PROJECT_DIR = ROOT_DIR / "Task1" / "generated_project"
sys.path.insert(0, str(GENERATED_PROJECT_DIR))

from app import app


def test_index_returns_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_sample_report_returns_json():
    client = app.test_client()
    response = client.get("/api/sample-report")

    assert response.status_code == 200
    data = response.get_json()

    assert data is not None
    assert data.get("success") is True
    assert "data" in data
    assert "match_summary" in data["data"]


def test_analyse_with_valid_data():
    client = app.test_client()

    payload = {
        "team_a": "Eagles",
        "team_b": "Tigers",
        "score": "2-1",
        "shots": "12-9",
        "possession": "55",
        "events": "Goal by striker, yellow card, late save"
    }

    response = client.post("/api/analyse", json=payload)

    assert response.status_code == 200
    data = response.get_json()

    assert data is not None
    assert data.get("success") is True
    assert "data" in data
    assert "match_summary" in data["data"]
    assert "human_review_note" in data["data"]


def test_analyse_rejects_missing_fields():
    client = app.test_client()

    payload = {
        "team_a": "Eagles",
        "team_b": "Tigers"
    }

    response = client.post("/api/analyse", json=payload)

    assert response.status_code == 400
    data = response.get_json()

    assert data is not None
    assert data.get("success") is False
    assert "error" in data