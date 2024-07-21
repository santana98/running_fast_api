import pytest
from fastapi.testclient import TestClient

from running_fast_api.app import app


@pytest.fixture()
def client():
    return TestClient(app)
