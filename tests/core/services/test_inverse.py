import galois
import pytest

from src.core.services.inverse import inverse as inverse_service


class TestInverse:
    def test_inverse_binary_small_m_successful(
        self, valid_binary_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly = valid_binary_input_small_m["poly1"]
        input_type = valid_binary_input_small_m["input_type"]
        result_str = inverse_service(poly=poly, input_type=input_type, m=m_small)
        result = int(result_str, 2)

        GF = galois.GF(2**m_small, irreducible_poly=0x11B)
        poly_int = int(poly, 2)
        field_poly = GF(poly_int)
        expected_inverse = int(GF(1) / field_poly)

        assert result == expected_inverse, f"Expected {expected_inverse}, got {result}"

    def test_inverse_binary_large_m_successful(
        self, valid_binary_input_large_m: dict[str, str], m_large: int
    ) -> None:
        poly = valid_binary_input_large_m["poly1"]
        input_type = valid_binary_input_large_m["input_type"]
        result_str = inverse_service(poly=poly, input_type=input_type, m=m_large)
        result = int(result_str, 2)

        irreducible_poly_233 = (1 << 233) | (1 << 74) | 1
        GF = galois.GF(2**m_large, irreducible_poly=irreducible_poly_233)
        poly_int = int(poly, 2)
        field_poly = GF(poly_int)
        expected_inverse = int(GF(1) / field_poly)

        assert result == expected_inverse, f"Expected {expected_inverse}, got {result}"

    def test_inverse_hex_small_m_successful(
        self, valid_hex_input_small_m: dict[str, str], m_small: int
    ) -> None:
        poly = valid_hex_input_small_m["poly1"]
        input_type = valid_hex_input_small_m["input_type"]
        result_str = inverse_service(poly=poly, input_type=input_type, m=m_small)
        result = int(result_str, 16)

        GF = galois.GF(2**m_small, irreducible_poly=0x11B)
        poly_int = int(poly, 16)
        field_poly = GF(poly_int)
        expected_inverse = int(GF(1) / field_poly)

        assert result == expected_inverse, f"Expected {expected_inverse}, got {result}"

    def test_inverse_hex_large_m_successful(
        self, valid_hex_input_large_m: dict[str, str], m_large: int
    ) -> None:
        poly = valid_hex_input_large_m["poly1"]
        input_type = valid_hex_input_large_m["input_type"]
        result_str = inverse_service(poly=poly, input_type=input_type, m=m_large)
        result = int(result_str, 16)

        irreducible_poly_233 = (1 << 233) | (1 << 74) | 1
        GF = galois.GF(2**m_large, irreducible_poly=irreducible_poly_233)
        poly_int = int(poly, 16)
        field_poly = GF(poly_int)
        expected_inverse = int(GF(1) / field_poly)

        assert result == expected_inverse, f"Expected {expected_inverse}, got {result}"

    def test_inverse_invalid_bin_input(
        self, invalid_binary_input: dict[str, str], m_small: int
    ) -> None:
        poly = invalid_binary_input["poly1"]
        input_type = invalid_binary_input["input_type"]
        with pytest.raises(ValueError):
            inverse_service(poly=poly, input_type=input_type, m=m_small)

    def test_inverse_invalid_hex_input(
        self, invalid_hexadecimal_input: dict[str, str], m_small: int
    ) -> None:
        poly = invalid_hexadecimal_input["poly1"]
        input_type = invalid_hexadecimal_input["input_type"]
        with pytest.raises(ValueError):
            inverse_service(poly=poly, input_type=input_type, m=m_small)
