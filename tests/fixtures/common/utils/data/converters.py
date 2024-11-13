import pytest


@pytest.fixture
def valid_hex_input() -> str:
    return "af"


@pytest.fixture
def valid_bin_input() -> str:
    return "10101111"


@pytest.fixture
def invalid_bin_input() -> str:
    return "10102"


@pytest.fixture
def invalid_hex_input() -> str:
    return "ag"
