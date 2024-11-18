from fastapi import APIRouter, status

from src.common.responses import APIResponse, APIResponseModel

status_router = APIRouter(
    prefix="/status",
    tags=["Status"],
)


@status_router.get(
    "",
    response_class=APIResponse,
    response_model=APIResponseModel,
    response_description="Status check",
    responses={
        status.HTTP_200_OK: {"description": "Status check successful"},
        status.HTTP_404_NOT_FOUND: {"description": "Status check failed"},
    },
)
async def status_check() -> APIResponse:
    """
    Endpoint to check the status of the service.

    Returns:
        APIResponse: An API response object containing a message and status code.
    """
    return APIResponse(
        message="Status check successful",
        status_code=status.HTTP_200_OK,
    )
