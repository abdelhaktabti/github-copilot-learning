import src.app as app_module


def test_successful_unregister(client):
    # Arrange
    activity = "Chess Club"
    email = app_module.activities[activity]["participants"][0]
    assert email in app_module.activities[activity]["participants"]

    # Act
    resp = client.delete(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert email not in app_module.activities[activity]["participants"]


def test_unregister_nonexistent_participant_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "not-a-member@mergington.edu"

    # Act
    resp = client.delete(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 404


def test_unregister_unknown_activity_returns_404(client):
    # Act
    resp = client.delete("/activities/NoActivity/signup", params={"email": "x@y.com"})

    # Assert
    assert resp.status_code == 404
