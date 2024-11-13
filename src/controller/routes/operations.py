from fastapi import status
from fastapi.routing import APIRouter

from src.common.responses.API_response import APIResponse
from src.common.utils.data.converters import Converters
from src.common.utils.types.HexStr import HexStr
from src.core.services.addition import add

services_router = APIRouter(prefix="/operations", tags=["Arithmetic Operations"])


@services_router.post("/add", response_model=APIResponse)
async def add_polynomials(poly1: HexStr, poly2: HexStr, m: int) -> APIResponse:
    try:
        poly1 = Converters.hex_to_bin(poly1)
        poly2 = Converters.hex_to_bin(poly2)
        poly1_list = Converters.binStr_to_list(poly1)
        poly2_list = Converters.binStr_to_list(poly2)

        result = Converters.list_to_binStr(add(poly1_list, poly2_list, m))
        return APIResponse(
            status_code=status.HTTP_200_OK,
            message="Polynomials added successfully",
            data={"result": Converters.bin_to_hex(result)},
        )
    except Exception as e:
        return APIResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="An error occurred while adding the polynomials",
            data={"error": str(e)},
        )
