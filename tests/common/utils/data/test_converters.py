from typing import Any

import galois
import pytest

from src.common.utils.data.converters import Converters
from src.common.utils.types.BinStr import BinStr
from src.common.utils.types.HexStr import HexStr


class TestConverters:
    def test_hex_to_bin_successful(
        self, valid_hex_input: HexStr, valid_bin_input: BinStr
    ) -> None:
        assert Converters.hex_to_bin(valid_hex_input) == valid_bin_input

    def test_hex_to_bin_invalid_input(self, invalid_hex_input: HexStr) -> None:
        with pytest.raises(TypeError):
            Converters.hex_to_bin(invalid_hex_input)

    def test_bin_to_hex_successful(
        self, valid_hex_input: HexStr, valid_bin_input: BinStr
    ) -> None:
        assert Converters.bin_to_hex(valid_bin_input) == valid_hex_input

    def test_bin_to_hex_invalid_input(self, invalid_bin_input: BinStr) -> None:
        with pytest.raises(ValueError):
            Converters.bin_to_hex(invalid_bin_input)

    def test_binStr_to_list_successful(self, valid_bin_input: BinStr) -> None:
        assert Converters.binStr_to_list(valid_bin_input) == [
            1,
            0,
            1,
            0,
            1,
            1,
            1,
            1,
        ]

    def test_binStr_to_list_invalid_input(self, invalid_bin_input: BinStr) -> None:
        with pytest.raises(TypeError):
            Converters.binStr_to_list(invalid_bin_input)

    def test_fieldArray_to_binStr_successful(
        self, valid_fieldArray_input: galois.FieldArray, valid_bin_input: BinStr
    ) -> None:
        assert (
            Converters.fieldArray_to_binStr(valid_fieldArray_input) == valid_bin_input
        )

    def test_fieldArray_to_binStr_invalid_input(
        self, invalid_fieldArray_input: Any
    ) -> None:
        with pytest.raises(ValueError):
            Converters.fieldArray_to_binStr(invalid_fieldArray_input)
