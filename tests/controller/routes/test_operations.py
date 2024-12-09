import json

import pytest
from fastapi import status

from src.controller.routes.operations import (
    addition,
    division,
    inverse,
    mod_reduction,
    multiplication,
    sub,
)
from src.controller.schemas.operationRequest import OperationRequest


@pytest.mark.asyncio
class TestAddPolynomials:
    async def test_addition_hex_polynomials_successful(
        self,
        valid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = valid_hex_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await addition(request)
        res = json.loads(response.body)

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
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await addition(request)
        res = json.loads(response.body)

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
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await addition(request)
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
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await addition(request)
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
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await addition(request)
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
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await addition(request)
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
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await addition(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "GF(2^8) scalars must be in `0 <= x < 256`, not 4081.",
            "data": {"result": None},
        }


@pytest.mark.asyncio
class TestDividePolynomials:
    async def test_division_hex_polynomials_successful(
        self,
        valid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        request = OperationRequest(
            poly1=valid_hex_input["poly1"],
            poly2=valid_hex_input["poly2"],
            input_type=valid_hex_input["input_type"],
            output_type=valid_hex_input["output_type"],
            m=m_value,
        )
        response = await division(request=request)
        res = eval(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Polynomials divided successfully!",
            "data": {"result": "54"},
        }

    async def test_division_bin_polynomials_successful(
        self,
        valid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        request = OperationRequest(
            poly1=valid_bin_input["poly1"],
            poly2=valid_bin_input["poly2"],
            input_type=valid_bin_input["input_type"],
            output_type=valid_bin_input["output_type"],
            m=m_value,
        )
        response = await division(request=request)
        res = eval(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Polynomials divided successfully!",
            "data": {"result": "10001111"},
        }

    async def test_division_invalid_input_type(
        self,
        invalid_input_type: dict[str, str],
        m_value: int,
    ) -> None:
        request = OperationRequest(
            poly1=invalid_input_type["poly1"],
            poly2=invalid_input_type["poly2"],
            input_type=invalid_input_type["input_type"],
            output_type=invalid_input_type["output_type"],
            m=m_value,
        )
        response = await division(request=request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_division_invalid_output_type(
        self,
        invalid_output_type: dict[str, str],
        m_value: int,
    ) -> None:
        request = OperationRequest(
            poly1=invalid_output_type["poly1"],
            poly2=invalid_output_type["poly2"],
            input_type=invalid_output_type["input_type"],
            output_type=invalid_output_type["output_type"],
            m=m_value,
        )
        response = await division(request=request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_division_invalid_hex_polynomials(
        self,
        invalid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        request = OperationRequest(
            poly1=invalid_hex_input["poly1"],
            poly2=invalid_hex_input["poly2"],
            input_type=invalid_hex_input["input_type"],
            output_type=invalid_hex_input["output_type"],
            m=m_value,
        )
        response = await division(request=request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 16: '1G3H'",
            "data": {"result": None},
        }

    async def test_division_invalid_bin_polynomials(
        self,
        invalid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        request = OperationRequest(
            poly1=invalid_bin_input["poly1"],
            poly2=invalid_bin_input["poly2"],
            input_type=invalid_bin_input["input_type"],
            output_type=invalid_bin_input["output_type"],
            m=m_value,
        )
        response = await division(request=request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 2: '10101112'",
            "data": {"result": None},
        }

    async def test_division_by_zero(
        self,
        valid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        request = OperationRequest(
            poly1=valid_bin_input["poly1"],
            poly2=valid_bin_input["poly2"],
            input_type=valid_bin_input["input_type"],
            output_type=valid_bin_input["output_type"],
            m=m_value,
        )
        request.poly2 = "0" * len(request.poly2)
        response = await division(request=request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "Division by zero is not allowed in Galois fields",
            "data": {"result": None},
        }

    async def test_division_error(
        self,
        input_outside_field: dict[str, str],
        m_value: int,
    ) -> None:
        request = OperationRequest(
            poly1=input_outside_field["poly1"],
            poly2=input_outside_field["poly2"],
            input_type=input_outside_field["input_type"],
            output_type=input_outside_field["output_type"],
            m=m_value,
        )
        response = await division(request=request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "GF(2^8) scalars must be in `0 <= x < 256`, not 4081.",
            "data": {"result": None},
        }


@pytest.mark.asyncio
class TestSubtractPolynomials:
    async def test_subtraction_hex_polynomials_successful(
        self,
        valid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = valid_hex_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await sub(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Polynomials subtracted successfully!",
            "data": {"result": "5e"},
        }

    async def test_subtraction_bin_polynomials_successful(
        self,
        valid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = valid_bin_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await sub(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Polynomials subtracted successfully!",
            "data": {"result": "01100110"},
        }

    async def test_subtraction_invalid_input_type(
        self,
        invalid_input_type: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_input_type.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await sub(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_subtraction_invalid_output_type(
        self,
        invalid_output_type: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_output_type.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await sub(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_subtraction_invalid_hex_polynomials(
        self,
        invalid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_hex_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await sub(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 16: '1G3H'",
            "data": {"result": None},
        }

    async def test_subtraction_invalid_bin_polynomials(
        self,
        invalid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_bin_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await sub(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 2: '10101112'",
            "data": {"result": None},
        }

    async def test_subtraction_error(
        self,
        input_outside_field: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = input_outside_field.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await sub(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "GF(2^8) scalars must be in `0 <= x < 256`, not 4081.",
            "data": {"result": None},
        }


@pytest.mark.asyncio
class TestModuloReduction:
    async def test_mod_reduction_hex_polynomials_successful(
        self,
        valid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = valid_hex_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await mod_reduction(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Modulo reduction performed successfully!",
            "data": {"result": "5e"},
        }

    async def test_mod_reduction_bin_polynomials_successful(
        self,
        valid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = valid_bin_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await mod_reduction(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Modulo reduction performed successfully!",
            "data": {"result": "01100110"},
        }

    async def test_mod_reduction_invalid_input_type(
        self,
        invalid_input_type: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_input_type.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await mod_reduction(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_mod_reduction_invalid_output_type(
        self,
        invalid_output_type: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_output_type.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await mod_reduction(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_mod_reduction_invalid_hex_polynomials(
        self,
        invalid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_hex_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await mod_reduction(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 16: '1G3H'",
            "data": {"result": None},
        }

    async def test_mod_reduction_invalid_bin_polynomials(
        self,
        invalid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_bin_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await mod_reduction(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 2: '10101112'",
            "data": {"result": None},
        }

    async def test_mod_reduction_out_of_field_error(
        self,
        input_outside_field: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = input_outside_field.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await mod_reduction(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "GF(2^8) scalars must be in `0 <= x < 256`, not 4081.",
            "data": {"result": None},
        }


@pytest.mark.asyncio
class TestMultiplyPolynomials:
    async def test_multiplication_hex_polynomials_successful(
        self,
        valid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = valid_hex_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await multiplication(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Polynomials multiplied successfully!",
            "data": {"result": "0b"},
        }

    async def test_multiplication_bin_polynomials_successful(
        self,
        valid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = valid_bin_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await multiplication(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Polynomials multiplied successfully!",
            "data": {"result": "11001001"},
        }

    async def test_multiplication_invalid_input_type(
        self,
        invalid_input_type: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_input_type.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await multiplication(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_multiplication_invalid_output_type(
        self,
        invalid_output_type: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_output_type.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await multiplication(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_multiplication_invalid_hex_polynomials(
        self,
        invalid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_hex_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await multiplication(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 16: '1G3H'",
            "data": {"result": None},
        }

    async def test_multiplication_invalid_bin_polynomials(
        self,
        invalid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_bin_input.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await multiplication(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 2: '10101112'",
            "data": {"result": None},
        }

    async def test_multiplication_out_of_field_error(
        self,
        input_outside_field: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = input_outside_field.values()
        request = OperationRequest(
            poly1=poly1,
            poly2=poly2,
            input_type=input_type,
            output_type=output_type,
            m=m_value,
        )
        response = await multiplication(request)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "GF(2^8) scalars must be in `0 <= x < 256`, not 4081.",
            "data": {"result": None},
        }


@pytest.mark.asyncio
class TestInversePolynomials:
    async def test_inverse_hex_polynomials_successful(
        self,
        valid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = valid_hex_input.values()
        response = await inverse(poly1, input_type, output_type, m_value)
        res = eval(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Polynomial inverse calculated successfully!",
            "data": {"result": "00"},
        }

    async def test_inverse_bin_polynomials_successful(
        self,
        valid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = valid_bin_input.values()
        response = await inverse(poly1, input_type, output_type, m_value)
        res = eval(response.body)

        assert response.status_code == status.HTTP_200_OK
        assert res == {
            "message": "Polynomial inverse calculated successfully!",
            "data": {"result": "00000000"},
        }

    async def test_inverse_invalid_input_type(
        self,
        invalid_input_type: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_input_type.values()
        response = await inverse(poly1, input_type, output_type, m_value)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_inverse_invalid_output_type(
        self,
        invalid_output_type: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_output_type.values()
        response = await inverse(poly1, input_type, output_type, m_value)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert res == {
            "message": "Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
            "data": {"result": None},
        }

    async def test_inverse_invalid_hex_polynomials(
        self,
        invalid_hex_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_hex_input.values()
        response = await inverse(poly1, input_type, output_type, m_value)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 16: '1G3H'",
            "data": {"result": None},
        }

    async def test_inverse_invalid_bin_polynomials(
        self,
        invalid_bin_input: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = invalid_bin_input.values()
        response = await inverse(poly1, input_type, output_type, m_value)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "invalid literal for int() with base 2: '10101112'",
            "data": {"result": None},
        }

    async def test_inverse_error(
        self,
        input_outside_field: dict[str, str],
        m_value: int,
    ) -> None:
        poly1, poly2, input_type, output_type = input_outside_field.values()
        response = await inverse(poly1, input_type, output_type, m_value)
        res = json.loads(response.body)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert res == {
            "message": "GF(2^8) scalars must be in `0 <= x < 256`, not 4081.",
            "data": {"result": None},
        }
