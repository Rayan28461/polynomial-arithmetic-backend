import pytest

from src.common.utils.types.BinStr import BinStr, validate_bin_str


class TestBinStr:
    def test_bin_str(self, valid_bin_input: BinStr) -> None:
        assert validate_bin_str(valid_bin_input) == valid_bin_input

    def test_bin_str_invalid(self, invalid_bin_input: BinStr) -> None:
        with pytest.raises(ValueError):
            validate_bin_str(invalid_bin_input)
