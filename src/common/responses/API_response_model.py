from typing import Any, Dict

from pydantic import BaseModel


class APIResponseModel(BaseModel):
    """
    A Pydantic model for API responses.

    Attributes:
        message (str): A message string in the response.
        data (Dict[str, Any]): A dictionary to hold any additional data, defaulting to an empty dictionary.
    """

    message: str
    data: Dict[str, Any] = {}
