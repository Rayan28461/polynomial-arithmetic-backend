import pytest

from src.core.services.division import divide


class TestDivide:
    def test_divide_binary_small_m_successful(
        self, valid_binary_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type = valid_binary_input_small_m.values()
        result = divide(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
        assert result == int("10001111", 2)

    def test_divide_binary_large_m_successful(
        self, valid_binary_input_large_m_div: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type = valid_binary_input_large_m_div.values()
        result = divide(poly1=poly1, poly2=poly2, input_type=input_type, m=m_large)
        assert result == int(
            "10110000010011001101000011010101011100010111111110010011100000001011010010000001110111011000001001100110100001101010101110001011111111001001110000000101101001000000111011101100000100110011010000110101010111000101111111100100110000011",
            2,
        )

    def test_divide_hex_small_m_successful(
        self, valid_hex_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type = valid_hex_input_small_m.values()
        result = divide(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
        assert result == int("54", 16)

    def test_divide_hex_large_m_successful(
        self, valid_hex_input_large_m_div: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type = valid_hex_input_large_m_div.values()
        result = divide(poly1=poly1, poly2=poly2, input_type=input_type, m=m_large)
        assert result == int(
            "5294A5294A5294A5294A5294A5294A5294A5294A5294A5294A5294A53A", 16
        )

    def test_divide_invalid_bin_input(
        self, invalid_binary_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type = invalid_binary_input.values()
            divide(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)

    def test_divide_invalid_hex_input(
        self, invalid_hexadecimal_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type = invalid_hexadecimal_input.values()
            divide(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)

    def test_divide_by_zero(
        self, valid_binary_input_small_m: dict[str, str], m_small: int
    ) -> None:
        valid_binary_input_small_m["poly2"] = "0" * len(
            valid_binary_input_small_m["poly2"]
        )
        with pytest.raises(
            ValueError, match="Division by zero is not allowed in Galois fields"
        ):
            poly1, poly2, input_type = valid_binary_input_small_m.values()
            divide(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)

    def test_divide_empty_input(
        self, empty_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type = empty_input.values()
            divide(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
