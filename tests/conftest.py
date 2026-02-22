import copy
import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(scope="session")
def snapshot():
    """Session-scoped snapshot of the initial activities state."""
    return copy.deepcopy(app_module.activities)


@pytest.fixture
def client():
    """TestClient for the FastAPI app."""
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities(snapshot):
    """Restore the global activities to the initial snapshot before each test."""
    app_module.activities = copy.deepcopy(snapshot)
    yield
    app_module.activities = copy.deepcopy(snapshot)
