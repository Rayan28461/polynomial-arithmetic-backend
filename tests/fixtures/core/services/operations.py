import pytest


@pytest.fixture
def valid_binary_input_small_m() -> dict[str, str]:
    """
    Fixture for a valid binary input with a small m value (e.g., m=8).
    """
    return {
        "poly1": "10101010",
        "poly2": "11001100",
        "input_type": "binary",
    }


@pytest.fixture
def valid_binary_input_large_m() -> dict[str, str]:
    """
    Fixture for a valid binary input with a large m value (e.g., m=256).
    """
    return {
        "poly1": "1" * 233,  # Large binary string of length 233
        "poly2": "0" * 233,  # Another large binary string with a different pattern
        "input_type": "binary",
    }


@pytest.fixture
def valid_binary_input_large_m_div() -> dict[str, str]:
    """
    Fixture for a valid binary input with a large m value (e.g., m=233),
    with poly2 as a mixed pattern.
    """
    return {
        "poly1": "1" * 233,  # Large binary string of length 233
        "poly2": "1010" * 58 + "1",  # Mixed binary pattern of length 233
        "input_type": "binary",
    }


@pytest.fixture
def valid_hex_input_small_m() -> dict[str, str]:
    """
    Fixture for a valid hexadecimal input with a small m value (e.g., m=8).
    """
    return {
        "poly1": "A1",
        "poly2": "FF",
        "input_type": "hexadecimal",
    }


@pytest.fixture
def valid_hex_input_large_m() -> dict[str, str]:
    """
    Fixture for a valid hexadecimal input with a large m value (e.g., m=256).
    """
    return {
        "poly1": "F" * 58,  # Large hexadecimal string of length 58 (233 bits)
        "poly2": "0" * 58,  # Another large hex string with a different pattern
        "input_type": "hexadecimal",
    }


@pytest.fixture
def valid_hex_input_large_m_div() -> dict[str, str]:
    """
    Fixture for a valid hexadecimal input with a large m value (e.g., m=233),
    with poly2 as a mixed pattern.
    """
    return {
        "poly1": "F" * 58,  # Large hexadecimal string of length 58 (233 bits)
        "poly2": "A5" * 29,  # Mixed hex pattern of exactly 233 bits
        "input_type": "hexadecimal",
    }


@pytest.fixture
def invalid_binary_input() -> dict[str, str]:
    """
    Fixture for an invalid binary input with non-binary characters.
    """
    return {
        "poly1": "10101112",  # Invalid binary string
        "poly2": "11001100",
        "input_type": "binary",
    }


@pytest.fixture
def invalid_hexadecimal_input() -> dict[str, str]:
    """
    Fixture for an invalid hexadecimal input with non-hexadecimal characters.
    """
    return {
        "poly1": "1G3H",  # Invalid hexadecimal string
        "poly2": "A5",
        "input_type": "hexadecimal",
    }


@pytest.fixture
def empty_input() -> dict[str, str]:
    """
    Fixture for testing empty input strings.
    """
    return {
        "poly1": "",
        "poly2": "",
        "input_type": "binary",
    }


@pytest.fixture
def m_small() -> int:
    """
    Fixture for a small m value (e.g., m=8).
    """
    return 8


@pytest.fixture
def m_large() -> int:
    """
    Fixture for a large m value (e.g., m=233).
    """
    return 233
