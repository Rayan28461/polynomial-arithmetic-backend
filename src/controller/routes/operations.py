from typing import Union

from fastapi import status
from fastapi.routing import APIRouter

from src.common.responses import APIResponse, APIResponseModel
from src.common.utils.types import BinStr, HexStr
from src.controller.schemas import OperationRequest, InverseRequest
from src.core.services.addition import add
from src.core.services.division import divide
from src.core.services.inverse import inverse as inverse_service
from src.core.services.mod_reduction import modReduction
from src.core.services.multiplication import multiplication as multiply
from src.core.services.subtraction import subtraction

services_router = APIRouter(prefix="/operations", tags=["Arithmetic Operations"])


@services_router.post(
    "/addition", response_class=APIResponse, response_model=APIResponseModel
)
async def addition(
    request: OperationRequest,
) -> APIResponse:
    """
    Endpoint to perform addition of two polynomials.

    Args:
        poly1 (Union[HexStr, BinStr]): The first polynomial in either hexadecimal or binary format.
        poly2 (Union[HexStr, BinStr]): The second polynomial in either hexadecimal or binary format.
        input_type (str): The format of the input polynomials ('binary' or 'hexadecimal').
        output_type (str): The desired format of the output polynomial ('binary' or 'hexadecimal').
        m (int, optional): The degree of the polynomial field. Defaults to 163.

    Returns:
        APIResponse: An API response object containing the result of the addition and status code.
    """
    try:
        poly1 = request.poly1
        poly2 = request.poly2
        input_type = request.input_type
        output_type = request.output_type
        m = request.m

        if input_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )
        if output_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )
        
        poly_sum = add(poly1, poly2, input_type, m)
        result = None
        
        if output_type == "binary":
            result = format(poly_sum, f"0{m}b")
        elif output_type == "hexadecimal":
            result = format(poly_sum, f"0{m//4}x")
        
        return APIResponse(
            message="Polynomials added successfully!",
            status_code=status.HTTP_200_OK,
            data={"result": result},
        )
    except ValueError as e:
        return APIResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message=str(e),
            data={"result": None},
        )
    except Exception as e:
        return APIResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
            data={"result": None},
        )


@services_router.post(
    "/division", response_class=APIResponse, response_model=APIResponseModel
)
async def division(
    request: OperationRequest,
) -> APIResponse:
    """
    Endpoint to perform division of two polynomials.

    Args:
        poly1 (Union[HexStr, BinStr]): The dividend polynomial in either hexadecimal or binary format.
        poly2 (Union[HexStr, BinStr]): The divisor polynomial in either hexadecimal or binary format.
        input_type (str): The format of the input polynomials ('binary' or 'hexadecimal').
        output_type (str): The desired format of the output polynomial ('binary' or 'hexadecimal').
        m (int, optional): The degree of the polynomial field. Defaults to 163.

    Returns:
        APIResponse: An API response object containing the result of the division and status code.
    """
    try:
        poly1 = request.poly1
        poly2 = request.poly2
        input_type = request.input_type
        output_type = request.output_type
        m = request.m

        if input_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )
        if output_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )

        poly_quotient = divide(poly1, poly2, input_type, m)
        result = None

        if output_type == "binary":
            result = format(poly_quotient, f"0{m}b")
        elif output_type == "hexadecimal":
            result = format(poly_quotient, f"0{m//4}x")

        return APIResponse(
            message="Polynomials divided successfully!",
            status_code=status.HTTP_200_OK,
            data={"result": result},
        )
    except ValueError as e:
        return APIResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message=str(e),
            data={"result": None},
        )
    except Exception as e:
        return APIResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
            data={"result": None},
        )


@services_router.post(
    "/subtraction", response_class=APIResponse, response_model=APIResponseModel
)
async def sub(
    request: OperationRequest,
) -> APIResponse:
    """
    Endpoint to perform subtraction of two polynomials.

    Args:
        poly1 (Union[HexStr, BinStr]): The first polynomial in either hexadecimal or binary format.
        poly2 (Union[HexStr, BinStr]): The second polynomial in either hexadecimal or binary format.
        input_type (str): The format of the input polynomials ('binary' or 'hexadecimal').
        output_type (str): The desired format of the output polynomial ('binary' or 'hexadecimal').
        m (int, optional): The degree of the polynomial field. Defaults to 163.

    Returns:
        APIResponse: An API response object containing the result of the subtraction and status code.
    """
    try:
        poly1 = request.poly1
        poly2 = request.poly2
        input_type = request.input_type
        output_type = request.output_type
        m = request.m

        if input_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )
        if output_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )

        poly_diff = subtraction(poly1, poly2, input_type, m)
        result = None

        if output_type == "binary":
            result = format(poly_diff, f"0{m}b")
        elif output_type == "hexadecimal":
            result = format(poly_diff, f"0{m//4}x")

        return APIResponse(
            message="Polynomials subtracted successfully!",
            status_code=status.HTTP_200_OK,
            data={"result": result},
        )
    except ValueError as e:
        return APIResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message=str(e),
            data={"result": None},
        )
    except Exception as e:
        return APIResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
            data={"result": None},
        )


@services_router.post(
    "/mod-reduction", response_class=APIResponse, response_model=APIResponseModel
)
async def mod_reduction(
    request: OperationRequest,
) -> APIResponse:
    """
    Endpoint to perform modulo reduction of two polynomials.

    Args:
        poly1 (Union[HexStr, BinStr]): The first polynomial in either hexadecimal or binary format.
        poly2 (Union[HexStr, BinStr]): The divisor polynomial in either hexadecimal or binary format.
        input_type (str): The format of the input polynomials ('binary' or 'hexadecimal').
        output_type (str): The desired format of the output polynomial ('binary' or 'hexadecimal').
        m (int, optional): The degree of the polynomial field. Defaults to 163.

    Returns:
        APIResponse: An API response object containing the result of the modulo reduction and status code.
    """
    try:

        poly1 = request.poly1
        poly2 = request.poly2
        input_type = request.input_type
        output_type = request.output_type
        m = request.m

        if input_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )
        if output_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )


        poly_mod = modReduction(poly1, poly2, input_type, m)
        result = None

        if output_type == "binary":
            result = format(poly_mod, f"0{m}b")
        elif output_type == "hexadecimal":
            result = format(poly_mod, f"0{m//4}x")

        return APIResponse(
            message="Modulo reduction performed successfully!",
            status_code=status.HTTP_200_OK,
            data={"result": result},
        )
    except ValueError as e:
        return APIResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message=str(e),
            data={"result": None},
        )
    except Exception as e:
        return APIResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
            data={"result": None},
        )


@services_router.post(
    "/multiplication", response_class=APIResponse, response_model=APIResponseModel
)
async def multiplication(
    request: OperationRequest,
) -> APIResponse:
    """
    Endpoint to perform multiplication of two polynomials over GF(2^m).

    Args:
        poly1 (Union[HexStr, BinStr]): The first polynomial in either hexadecimal or binary format.
        poly2 (Union[HexStr, BinStr]): The second polynomial in either hexadecimal or binary format.
        input_type (str): The format of the input polynomials ('binary' or 'hexadecimal').
        output_type (str): The desired format of the output polynomial ('binary' or 'hexadecimal').
        m (int, optional): The degree of the polynomial field. Defaults to 163.

    Returns:
        APIResponse: An API response object containing the result of the multiplication and status code.
    """
    try:
        poly1 = request.poly1
        poly2 = request.poly2
        input_type = request.input_type
        output_type = request.output_type
        m = request.m

        if input_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )

        if output_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )

        poly_product = multiply(poly1, poly2, input_type, m)
        result = None

        if output_type == "binary":
            result = format(poly_product, f"0{m}b")
        elif output_type == "hexadecimal":
            result = format(poly_product, f"0{m//4}x")

        return APIResponse(
            message="Polynomials multiplied successfully!",
            status_code=status.HTTP_200_OK,
            data={"result": result},
        )

    except ValueError as e:
        return APIResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message=str(e),
            data={"result": None},
        )
    except Exception as e:
        return APIResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
            data={"result": None},
        )


@services_router.post(
    "/inverse", response_class=APIResponse, response_model=APIResponseModel
)
async def inverse_operation(
    request: InverseRequest,
) -> APIResponse:
    """
    Handle the inverse operation request.

    Args:
        request (InverseRequest): The request object containing the polynomial, input type, output type, and degree of the Galois Field.

    Returns:
        APIResponse: The response object containing the status code, message, and the result of the inverse operation.

    Raises:
        HTTPException: If the input type or output type is invalid.
    """
    try:
        poly = request.poly
        input_type = request.input_type
        output_type = request.output_type
        m = request.m

        if input_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid input type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )
        if output_type not in ["binary", "hexadecimal"]:
            return APIResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Invalid output type.\nPlease provide either 'binary' or 'hexadecimal'.",
                data={"result": None},
            )

        inverse_result = inverse_service(poly=poly, input_type=input_type, m=m)

        if output_type == "binary":
            result = inverse_result
        elif output_type == "hexadecimal":
            if input_type == "binary":
                inverse_int = int(inverse_result, 2)
                hex_len = (m + 3) // 4
                result = hex(inverse_int)[2:].upper().rjust(hex_len, "0")
            else:

                result = inverse_result

        return APIResponse(
            message="Polynomial inverse computed successfully!",
            status_code=status.HTTP_200_OK,
            data={"result": result},
        )
    except ValueError as e:

        return APIResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message=str(e),
            data={"result": None},
        )
    except Exception as e:

        return APIResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
            data={"result": None},
        )
