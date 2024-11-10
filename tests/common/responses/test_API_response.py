import pytest
from src.common.responses.API_response import APIResponse
from fastapi import status

class TestApiResponse:
    @pytest.mark.parametrize(
        "message, status_code, data",
        [
            ("Test message", status.HTTP_200_OK, {}),
            ("Test message", status.HTTP_201_CREATED, {"key": "value"}),
        ],
    )
    def test_api_response_successful(self, message, status_code, data):
        response = APIResponse(message, status_code, data)
        res = eval(response.body.decode("utf-8"))
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
    def test_api_response_invalid(self, message, status_code, data):
        with pytest.raises(ValueError):
            APIResponse(message, status_code, data)
