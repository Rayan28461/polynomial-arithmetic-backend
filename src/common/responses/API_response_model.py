from typing import Any, Dict

from pydantic import BaseModel


class APIResponseModel(BaseModel):
    message: str
    data: Dict[str, Any] = {}
