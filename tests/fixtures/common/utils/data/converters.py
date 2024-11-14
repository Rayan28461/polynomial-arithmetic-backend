import galois
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


@pytest.fixture
def valid_fieldArray_input() -> galois.FieldArray:
    gf = galois.GF(2**8)
    return gf([1, 0, 1, 0, 1, 1, 1, 1])


@pytest.fixture
def invalid_fieldArray_input() -> list[int]:
    return [1, 0]
