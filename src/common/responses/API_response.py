from typing import Any
from fastapi import status
from fastapi.responses import JSONResponse as FastAPIJSONResponse

class APIResponse(FastAPIJSONResponse):
    """
    Custom API response class inheriting from FastAPI's JSONResponse.
    
    Attributes:
        media_type (str): The media type of the response, set to "application/json".
    """
    media_type = "application/json"

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_200_OK,
        data: dict[str, Any] = {},
    ) -> None:
        """
        Initialize the APIResponse instance.

        Args:
            message (str): The message to be included in the response.
            status_code (int, optional): The HTTP status code for the response. Defaults to 200 (OK).
            data (dict[str, Any], optional): Additional data to include in the response. Defaults to an empty dictionary.

        Raises:
            ValueError: If message or status_code is not provided.
        """
        if not message:
            raise ValueError("message must be provided")
        if not status_code:
            raise ValueError("status_code must be provided")
        content = {
            "message": message,
            "data": data,
        }
        super().__init__(
            content=content,
            status_code=status_code,
        )
