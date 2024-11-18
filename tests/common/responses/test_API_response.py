import pytest
from fastapi import status

from src.common.responses.API_response import APIResponse


class TestApiResponse:
    @pytest.mark.parametrize(
        "message, status_code, data",
        [
            ("Test message", status.HTTP_200_OK, {}),
            ("Test message", status.HTTP_201_CREATED, {"key": "value"}),
        ],
    )
    def test_api_response_successful(
        self, message: str, status_code: int, data: dict[str, str]
    ) -> None:
        response = APIResponse(message, status_code, data)

        # Decode only if response.body is of type bytes
        res_body = response.body
        if isinstance(res_body, bytes):
            res = eval(res_body.decode("utf-8"))
        elif isinstance(res_body, memoryview):
            res = eval(res_body.tobytes().decode("utf-8"))

        assert response.status_code == status_code
        assert res["message"] == message
        assert res["data"] == data
        assert response.media_type == "application/json"

    @pytest.mark.parametrize(
        "message, status_code, data",
        [
            ("", status.HTTP_200_OK, {}),
            ("Test message", None, {}),
        ],
    )
    def test_api_response_invalid(
        self, message: str, status_code: int, data: dict[str, str]
    ) -> None:
        with pytest.raises(ValueError):
            APIResponse(message, status_code, data)
