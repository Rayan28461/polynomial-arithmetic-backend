import pytest
from src.core.services.multiplication import multiplication


class Testmultiplication:
    def test_multiplication_binary_small_m_successful(
        self, valid_binary_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type = valid_binary_input_small_m.values()
        result = multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
        assert result == int("11001001", 2)

    def test_multiplication_binary_large_m_successful(
        self, valid_binary_input_large_m_mul: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type = valid_binary_input_large_m_mul.values()
        result = multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_large)
        assert result == int("0",2)

    def test_multiplication_hex_small_m_successful(
        self, valid_hex_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type = valid_hex_input_small_m.values()
        result = multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
        assert result == int("11", 16)

    def test_multiplication_hex_large_m_successful(
        self, valid_hex_input_large_m_mul: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type = valid_hex_input_large_m_mul.values()
        result = multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_large)
        assert result == int("0", 16)

    def test_multiplication_invalid_bin_input(
        self, invalid_binary_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type = invalid_binary_input.values()
            multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)

    def test_multiplication_invalid_hex_input(
        self, invalid_hexadecimal_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type = invalid_hexadecimal_input.values()
            multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)


    def test_multiplication_empty_input(
        self, empty_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type = empty_input.values()
            multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
