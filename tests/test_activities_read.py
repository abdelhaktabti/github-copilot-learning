def test_get_activities_returns_all(client, snapshot):
    # Arrange: fixtures provide `client` and `snapshot`
    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    assert resp.json() == snapshot
