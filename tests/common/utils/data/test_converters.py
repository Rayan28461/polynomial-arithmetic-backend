import pytest
from src.common.utils.data.converters import Converters
from src.common.utils.types.BinStr import BinStr
from src.common.utils.types.HexStr import HexStr

class TestConverters:
    def test_hex_to_bin_successful(self, valid_hex_input: HexStr, valid_bin_input: BinStr) -> None:
        assert Converters.hex_to_bin(valid_hex_input) == valid_bin_input
    
    def test_hex_to_bin_invalid_input(self, invalid_hex_input: HexStr) -> None:
        with pytest.raises(TypeError):
            Converters.hex_to_bin(invalid_hex_input)

    def test_bin_to_hex_successful(self, valid_hex_input: HexStr, valid_bin_input: BinStr) -> None:
        assert Converters.bin_to_hex(valid_bin_input) == valid_hex_input

    def test_bin_to_hex_invalid_input(self, invalid_bin_input: BinStr) -> None:
        with pytest.raises(ValueError):
            Converters.bin_to_hex(invalid_bin_input)
