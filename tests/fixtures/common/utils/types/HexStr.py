import pytest


@pytest.fixture
def valid_hex_type() -> str:
    return "af"


@pytest.fixture
def invalid_hex_type() -> str:
    return "ag"
