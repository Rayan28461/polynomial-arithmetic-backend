from typing import Union
from pydantic import BaseModel, Field

from src.common.utils.types import BinStr, HexStr

class InverseRequest(BaseModel):
    poly: str = Field(description="Polynomial")
    input_type: str = Field("hexadecimal", description="Type of input data")
    output_type: str = Field("hexadecimal", description="Type of output data")
    m: int = Field(description="Modulus value for the operation")