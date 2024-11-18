import re
from typing import Annotated

from pydantic.functional_validators import BeforeValidator


def validate_hex_str(value: str) -> str:
    """
    Validate that the provided string is a valid hexadecimal string.

    Args:
        value (str): The string to validate.

    Returns:
        str: The validated hexadecimal string.

    Raises:
        ValueError: If the input string is not a valid hexadecimal string.
    """
    if not re.match(r"^[a-fA-F0-9]*$", value):
        raise ValueError("Invalid hex string")
    return value


HexStr = Annotated[str, BeforeValidator(validate_hex_str)]
