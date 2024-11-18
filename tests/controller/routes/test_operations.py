import json

import pytest
from fastapi import status

from src.controller.routes.operations import addition


@pytest.mark.asyncio
class TestAddPolynomials:
    async def test_addition_hex_polynomials_successful(
        self,
        valid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = valid_hex_input.values()
        response = await addition(poly1, poly2, input_type, output_type, m_value)
        res = eval(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Polynomials added successfully!",
            "data": {"result": "5e"},
        }

    async def test_addition_bin_polynomials_successful(
        self,
        valid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = valid_bin_input.values()
        response = await addition(poly1, poly2, input_type, output_type, m_value)
        res = eval(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Polynomials added successfully!",
            "data": {"result": "01100110"},
        }

    async def test_addition_invalid_input_type(
        self,
        invalid_input_type: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_input_type.values()
        response = await addition(poly1, poly2, input_type, output_type, m_value)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_addition_invalid_output_type(
        self,
        invalid_output_type: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_output_type.values()
        response = await addition(poly1, poly2, input_type, output_type, m_value)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_addition_invalid_hex_polynomials(
        self,
        invalid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_hex_input.values()
        response = await addition(poly1, poly2, input_type, output_type, m_value)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 16: '1G3H'",
            "data": {"result": None},
        }

    async def test_addition_invalid_bin_polynomials(
        self,
        invalid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_bin_input.values()
        response = await addition(poly1, poly2, input_type, output_type, m_value)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 2: '10101112'",
            "data": {"result": None},
        }

    async def test_addition_error(
        self,
        input_outside_field: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = input_outside_field.values()
        response = await addition(poly1, poly2, input_type, output_type, m_value)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "GF(2^8) scalars must be in `0 <= x < 256`, not 4081.",
            "data": {"result": None},
        }