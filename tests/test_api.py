from fastapi.testclient import TestClient

from nba_clv_dashboard.app import app

client = TestClient(app)


def test_metrics() -> None:
    r = client.get("/api/metrics")
    assert r.status_code == 200
    data = r.json()
    assert "calibration" in data
    assert data["overall_accuracy"] > 0.5
