import pytest


@pytest.fixture
def valid_bin_input() -> dict[str, str]:
    """
    Fixture for a valid binary input pair.
    """
    return {
        "poly1": "10101010",
        "poly2": "11001100",
        "input_type": "binary",
        "output_type": "binary",
    }


@pytest.fixture
def valid_hex_input() -> dict[str, str]:
    """
    Fixture for a valid hexadecimal input pair.
    """
    return {
        "poly1": "A1",
        "poly2": "FF",
        "input_type": "hexadecimal",
        "output_type": "hexadecimal",
    }


@pytest.fixture
def invalid_bin_input() -> dict[str, str]:
    """
    Fixture for an invalid binary input (non-binary characters).
    """
    return {
        "poly1": "10101112",  # Invalid binary string
        "poly2": "11001100",
        "input_type": "binary",
        "output_type": "binary",
    }


@pytest.fixture
def invalid_hex_input() -> dict[str, str]:
    """
    Fixture for an invalid hexadecimal input (invalid hex characters).
    """
    return {
        "poly1": "1G3H",  # Invalid hexadecimal string
        "poly2": "A5",
        "input_type": "hexadecimal",
        "output_type": "hexadecimal",
    }


@pytest.fixture
def input_outside_field() -> dict[str, str]:
    """
    Fixture for input polynomials outside the field.
    """
    return {
        "poly1": "FF1",  # Outside the field
        "poly2": "FF",
        "input_type": "hexadecimal",
        "output_type": "hexadecimal",
    }


@pytest.fixture
def invalid_input_type() -> dict[str, str]:
    """
    Fixture for an invalid input type.
    """
    return {
        "poly1": "10101010",
        "poly2": "11001100",
        "input_type": "decimal",  # Invalid input type
        "output_type": "binary",
    }


@pytest.fixture
def invalid_output_type() -> dict[str, str]:
    """
    Fixture for an invalid output type.
    """
    return {
        "poly1": "10101010",
        "poly2": "11001100",
        "input_type": "binary",
        "output_type": "octal",  # Invalid output type
    }


@pytest.fixture
def m_value() -> int:
    """
    Fixture for m value, set to 8.
    """
    return 8
