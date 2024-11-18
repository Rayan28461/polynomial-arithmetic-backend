import pytest

from src.common.utils.types.HexStr import HexStr, validate_hex_str


class TestHexStr:
    def test_hex_str(self, valid_hex_type: HexStr) -> None:
        assert validate_hex_str(valid_hex_type) == valid_hex_type

    def test_hex_str_invalid(self, invalid_hex_type: HexStr) -> None:
        with pytest.raises(ValueError):
            validate_hex_str(invalid_hex_type)
