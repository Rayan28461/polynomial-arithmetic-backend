import pytest


@pytest.fixture
def valid_bin_type() -> str:
    return "10101111"


@pytest.fixture
def invalid_bin_type() -> str:
    return "10102"
