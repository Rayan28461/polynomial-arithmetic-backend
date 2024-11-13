import pytest
from fastapi import status

from src.controller.status import status_check


@pytest.mark.asyncio
async def test_status_check() -> None:
    response = await status_check()

    # Decode only if response.body is of type bytes
    res_body = response.body
    if isinstance(res_body, bytes):
        res = eval(res_body.decode("utf-8"))
    elif isinstance(res_body, memoryview):
        res = eval(res_body.tobytes().decode("utf-8"))

    assert response.status_code == status.HTTP_200_OK
    assert res == {"message": "Status check successful", "data": {}}
