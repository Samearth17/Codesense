"""Integration and contract tests for the API scan endpoint."""

import pytest
from fastapi.testclient import TestClient

from app.main import create_app
from app.schemas.scan import ScanResponse


@pytest.fixture
def client() -> TestClient:
    app = create_app()
    return TestClient(app)


def test_health_endpoint(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "codesense-backend"}


def test_scan_endpoint_valid_human_code(client: TestClient) -> None:
    # A simple clean human python code snippet
    code = """def add_numbers(a: int, b: int) -> int:
    return a + b
"""
    response = client.post("/api/v1/scan", json={"code": code, "filename": "add.py"})
    assert response.status_code == 200
    data = response.json()

    # Validate structure using schemas
    validated = ScanResponse(**data)
    assert validated.filename == "add.py"
    assert validated.label in ("human", "ai")
    assert validated.confidence >= 0.0 and validated.confidence <= 1.0
    assert validated.vulnerability_count == len(validated.vulnerabilities)


def test_scan_endpoint_empty_code(client: TestClient) -> None:
    response = client.post("/api/v1/scan", json={"code": "", "filename": "empty.py"})
    assert response.status_code == 422  # Pydantic validation error due to min_length=1


def test_scan_endpoint_code_too_large(client: TestClient) -> None:
    large_code = "a = 1\n" * 100000  # More than 500KB
    response = client.post("/api/v1/scan", json={"code": large_code, "filename": "large.py"})
    assert response.status_code == 422  # Pydantic validation error due to max_length=500_000
