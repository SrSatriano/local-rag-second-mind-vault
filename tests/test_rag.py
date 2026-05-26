from fastapi.testclient import TestClient

from src.api.main import app
from src.store import reset_store


def test_health():
    reset_store()
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_ingest_and_query():
    reset_store()
    client = TestClient(app)
    client.post("/ingest/text", json={"text": "Python é uma linguagem.", "source_id": "doc1"})
    r = client.post("/query", json={"question": "Python", "top_k": 3})
    assert r.status_code == 200
    body = r.json()
    assert "doc1" in body["sources"] or "Python" in body["answer"]
