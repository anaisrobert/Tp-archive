# tests/test_integration_example.py
from app import app

def test_index_page_loads():
    """Vérifie que la route principale renvoie un code 200."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200