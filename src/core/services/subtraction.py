import galois

def subtraction(
    poly1: str, poly2: str, inputType: str, m: int = 163
) -> int:
    """
    Subtracts 2 polynomials in a Galois Field GF(2^m).

    Arguments:
    poly1: The first polynomial in binary or hexadecimal format.
    poly2: The second polynomial in binary or hexadecimal format.
    poly1 and poly2 are assumed to be valid inputs for GF(2^m).
    inputType: The format of both input polynomials ('binary' or 'hexadecimal').
    m (int, optional): The degree of the polynomial field. Defaults to 163.

    Returns:
    integer

    Raises:
    ValueError: If the input type is invalid or conversion fails.
    """

    try:
        if inputType == "binary":
            poly1Int = int(poly1, 2)
            poly2Int = int(poly2, 2)
        elif inputType == "hexadecimal":
            poly1Int = int(poly1, 16)
            poly2Int = int(poly2, 16)
        else:
            raise ValueError("Invalid input type! Use 'binary' or 'hexadecimal'.")

        # For m = 571, use XOR directly
        if m == 571:
            resultInt = poly1Int ^ poly2Int  # XOR operation for subtraction in GF(2)
            return resultInt

        # For other values of m, use galois library
        else:
            gf = galois.GF(2**m)
            fieldPoly1 = gf(poly1Int)
            fieldPoly2 = gf(poly2Int)
            result = fieldPoly1 - fieldPoly2  # Subtraction in the Galois Field

            return result

    except ValueError as e:
        raise ValueError(e)
