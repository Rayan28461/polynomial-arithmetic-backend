import re
from typing import Annotated

from pydantic.functional_validators import BeforeValidator


def validate_bin_str(value: str) -> str:
    """
    Validate that the provided string is a valid binary string.

    Args:
        value (str): The string to validate.

    Returns:
        str: The validated binary string.

    Raises:
        ValueError: If the input string is not a valid binary string.
    """
    if not re.match(r"^[01]*$", value):
        raise ValueError("Invalid binary string")
    return value


BinStr = Annotated[str, BeforeValidator(validate_bin_str)]
