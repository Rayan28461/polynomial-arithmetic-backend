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
        int: The result of the subtraction in the Galois field.

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

        if poly1Int >= 2**m or poly2Int >= 2**m:
            raise ValueError ("Invalid Input for Specified m!")
        resultInt = poly1Int ^ poly2Int
        return resultInt

    except ValueError as e:
        raise ValueError(e)