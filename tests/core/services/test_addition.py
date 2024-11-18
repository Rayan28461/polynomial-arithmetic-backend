import pytest

from src.core.services.addition import add


class TestAdd:
    def test_add_binary_small_m_successful(
        self, valid_binary_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type = valid_binary_input_small_m.values()
        result = add(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
        assert result == int("01100110", 2)

    def test_add_binary_large_m_successful(
        self, valid_binary_input_large_m: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type = valid_binary_input_large_m.values()
        result = add(poly1=poly1, poly2=poly2, input_type=input_type, m=m_large)
        assert result == int("1" * 233, 2)

    def test_add_hex_small_m_successful(
        self, valid_hex_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type = valid_hex_input_small_m.values()
        result = add(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
        assert result == int("5E", 16)

    def test_add_hex_large_m_successful(
        self, valid_hex_input_large_m: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type = valid_hex_input_large_m.values()
        result = add(poly1=poly1, poly2=poly2, input_type=input_type, m=m_large)
        assert result == int("F" * 58, 16)

    def test_add_invalid_bin_input(
        self, invalid_binary_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type = invalid_binary_input.values()
            add(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)

    def test_add_invalid_hex_input(
        self, invalid_hexadecimal_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type = invalid_hexadecimal_input.values()
            add(poly1=poly1, poly2=poly2, input_type=input_type, m=m_small)
