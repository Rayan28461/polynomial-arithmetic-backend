import pytest

from src.core.services.inverse import inverse


class TestInverse:
    def test_inverse_binary_small_m_successful(
        self, valid_binary_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type = valid_binary_input_small_m.values()
        result = inverse(poly=poly1, input_type=input_type, m=m_small)
        assert result == 181

    def test_inverse_binary_large_m_successful(
        self, valid_binary_input_large_m: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type, output_type = valid_binary_input_large_m.values()
        result = inverse(poly=poly1, input_type=input_type, m=m_large)
        assert result == int(
            "11010010111011101001001110101100111011000101000110111010101001010101110101101001001110011101001001100111101011101010101010000101101111110000011110010011010000111001101001010000110111100010101000111101",
            2,
        )

    def test_inverse_hex_small_m_successful(
        self, valid_hex_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type, output_type = valid_hex_input_small_m.values()
        result = inverse(poly=poly1, input_type=input_type, m=m_small)
        assert result == int("3D", 16)

    def test_inverse_hex_large_m_successful(
        self, valid_hex_input_large_m: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type, output_type = valid_hex_input_large_m.values()
        result = inverse(poly=poly1, input_type=input_type, m=m_large)
        assert result == int(
            "8AC50D4A3B5721E9A7F5678A934A8F65E232478B6BFEF029FF3258E98C9F", 16
        )

    def test_inverse_invalid_bin_input(
        self, invalid_binary_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type, output_type = invalid_binary_input.values()
            inverse(poly=poly1, input_type=input_type, m=m_small)

    def test_inverse_invalid_hex_input(
        self, invalid_hexadecimal_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type, output_type = invalid_hexadecimal_input.values()
            inverse(poly=poly1, input_type=input_type, m=m_small)

    def test_inverse_empty_input(
        self, empty_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type, output_type = empty_input.values()
            inverse(poly=poly1, input_type=input_type, m=m_small)
