import pytest

from src.common.utils.types.BinStr import BinStr, validate_bin_str


class TestBinStr:
    def test_bin_str(self, valid_bin_type: BinStr) -> None:
        assert validate_bin_str(valid_bin_type) == valid_bin_type

    def test_bin_str_invalid(self, invalid_bin_type: BinStr) -> None:
        with pytest.raises(ValueError):
            validate_bin_str(invalid_bin_type)
