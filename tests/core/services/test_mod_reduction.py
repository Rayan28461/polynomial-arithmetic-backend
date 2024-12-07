import pytest

from src.core.services.mod_reduction import modReduction


class TestModReduction:
    def test_mod_binary_small_m_successful(
        self, valid_binary_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type = valid_binary_input_small_m.values()
        result = modReduction(poly1=poly1, poly2=poly2, inputType=input_type, m=m_small)
        assert result == int("01100110", 2)  # Expected result in binary (example)

    def test_mod_binary_large_m_successful(
        self, valid_binary_input_large_m: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type = valid_binary_input_large_m.values()
        result = modReduction(poly1=poly1, poly2=poly2, inputType=input_type, m=m_large)
        assert result == int("1" * 233, 2)  # Adjusted expected result for test

    def test_mod_hex_small_m_successful(
        self, valid_hex_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly1, poly2, input_type = valid_hex_input_small_m.values()
        result = modReduction(poly1=poly1, poly2=poly2, inputType=input_type, m=m_small)
        assert result == int("5E", 16)  # Expected result in hexadecimal

    def test_mod_hex_large_m_successful(
        self, valid_hex_input_large_m: dict[str, str], m_large: int
    ) -> None:
        poly1, poly2, input_type = valid_hex_input_large_m.values()
        result = modReduction(poly1=poly1, poly2=poly2, inputType=input_type, m=m_large)
        assert result == int("F" * 58, 16)  # Adjusted expected result for test

    def test_mod_invalid_bin_input(
        self, invalid_binary_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type = invalid_binary_input.values()
            modReduction(poly1=poly1, poly2=poly2, inputType=input_type, m=m_small)

    def test_mod_invalid_hex_input(
        self, invalid_hexadecimal_input: dict[str, str], m_small: int
    ) -> None:
        with pytest.raises(ValueError):
            poly1, poly2, input_type = invalid_hexadecimal_input.values()
            modReduction(poly1=poly1, poly2=poly2, inputType=input_type, m=m_small)
