import pytest

from src.core.services.multiplication import multiplication


class Testmultiplication:
    def test_multiplication_binary_small_m_successful(
        self, valid_binary_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type = valid_binary_input_small_m.values()
        result = multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
        assert result == int("10001111", 2)

    def test_multiplication_binary_large_m_successful(
        self, valid_binary_input_large_m_mul: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type = valid_binary_input_large_m_mul.values()
        result = multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_large)
        assert result == int(
            "10110000010011001101000011010101011100010111111110010011100000001011010010000001110111011000001001100110100001101010101110001011111111001001110000000101101001000000111011101100000100110011010000110101010111000101111111100100110000011",
            2,
        )

    def test_multiplication_hex_small_m_successful(
        self, valid_hex_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type = valid_hex_input_small_m.values()
        result = multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
        assert result == int("54", 16)

    def test_multiplication_hex_large_m_successful(
        self, valid_hex_input_large_m_mul: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type = valid_hex_input_large_m_mul.values()
        result = multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_large)
        # Replace the expected result below with the correct integer value for your test.
        assert result == int(
            "5294A5294A5294A5294A5294A5294A5294A5294A5294A5294A5294A53A", 16
        )

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

    def test_multiplication_by_zero(
        self, valid_binary_input_small_m: dict[str, str], m_small: int
    ) -> None:
        # multiplicationing by zero should result in zero. Adjust if your logic differs.
        valid_binary_input_small_m["poly2"] = "0" * len(
            valid_binary_input_small_m["poly2"]
        )
        poly1, poly2, input_type = valid_binary_input_small_m.values()
        result = multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
        assert result == 0

    def test_multiplication_empty_input(
        self, empty_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type = empty_input.values()
            multiplication(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
