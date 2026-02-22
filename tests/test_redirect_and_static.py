def test_root_redirects_to_static_index(client):
    # Act: prevent automatic redirects so we can inspect the Location header
    resp = client.get("/", follow_redirects=False)

    # Assert: FastAPI RedirectResponse usually uses a temporary redirect
    assert resp.status_code in (307, 302)
    assert resp.headers.get("location") == "/static/index.html"


def test_static_index_served(client):
    resp = client.get("/static/index.html")
    assert resp.status_code == 200
    # Basic content checks
    assert "Mergington High School" in resp.text
    assert "<title>Mergington High School Activities</title>" in resp.text
