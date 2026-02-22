import src.app as app_module


def test_successful_signup(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    assert email not in app_module.activities[activity]["participants"]

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert email in app_module.activities[activity]["participants"]


def test_duplicate_signup_returns_400(client):
    # Arrange
    activity = "Chess Club"
    email = "duplicate@mergington.edu"

    # first signup
    r1 = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert r1.status_code == 200

    # Act: duplicate signup
    r2 = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert r2.status_code == 400
    assert "already signed up" in r2.json().get("detail", "")


def test_signup_unknown_activity_returns_404(client):
    # Act
    resp = client.post("/activities/NonExistentActivity/signup", params={"email": "x@y.com"})

    # Assert
    assert resp.status_code == 404
