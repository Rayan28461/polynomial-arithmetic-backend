import binascii

from galois import FieldArray

from ..types.BinStr import BinStr
from ..types.HexStr import HexStr


class Converters:
    """
    A utility class for converting between hexadecimal and binary strings.
    """

    @staticmethod
    def hex_to_bin(hex_str: HexStr) -> BinStr:
        """
        Convert a hexadecimal string to a binary string.

        Args:
            hex_str (HexStr): The hexadecimal string to convert.

        Returns:
            BinStr: The resulting binary string.

        Raises:
            TypeError: If the input hexadecimal string is invalid.
        """
        try:
            binary_data = binascii.unhexlify(hex_str)  # Convert hex to bytes
            # Convert each byte to an 8-bit binary string and join them
            return "".join(format(byte, "08b") for byte in binary_data)
        except binascii.Error:
            raise TypeError("Invalid hex input")

    @staticmethod
    def bin_to_hex(bin_str: BinStr) -> HexStr:
        """
        Convert a binary string to a hexadecimal string.

        Args:
            bin_str (BinStr): The binary string to convert.

        Returns:
            HexStr: The resulting hexadecimal string.
        """

        def str_to_bytes(bin_str: str) -> bytes:
            return bytes(int(bin_str[i : i + 8], 2) for i in range(0, len(bin_str), 8))

        return binascii.hexlify(str_to_bytes(bin_str)).decode("utf-8")

    @staticmethod
    def fieldArray_to_binStr(lst: FieldArray) -> BinStr:
        """
        Convert a list of integers to a binary string.

        Args:
            lst (FieldArray): The list of integers to convert.

        Returns:
            BinStr: The resulting binary string.
        """
        if not isinstance(lst, FieldArray):
            raise ValueError("Input must be a list of integers")
        return "".join(str(bit) for bit in lst)
