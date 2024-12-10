import galois


def modReduction(
    poly1: str, poly2: str, inputType: str, m: int = 163
) -> galois.FieldArray:
    """
    Computes modulo reduction given 2 polynomials (poly1%poly2) in a Galois Field GF(2^m).

    Arguments:
    poly1: The first polynomial in binary or hexadecimal format.
    poly2: The divisor in binary or hexadecimal format or the irreducible polynomial of a galois field.
    inputType: The format of both input polynomials ('binary' or 'hexadecimal').
    m(int,optional) : The degree of the polynomial field. Set to 163 if not specified.

    Returns:
    galois.FieldArray: The result of the modulo reduction in a the Galois Field

    Raises:
    ValueError: If the input type is invalid or conversion fails.
    """

    # Initialize the Galois Field
    gf = galois.GF(2**m)
    fieldPoly1 = None
    fieldPoly2 = None

    try:
        # Convert based on the input type to the integer representation
        if inputType == "binary":  # If the input is in base 2
            fieldPoly1 = gf(int(poly1, 2))
            fieldPoly2 = gf(int(poly2, 2))
            fieldPolyInt1 = int(poly1, 2)
            fieldPolyInt2 = int(poly2, 2)
        elif inputType == "hexadecimal":  # If the input is in base 16
            fieldPoly1 = gf(int(poly1, 16))
            fieldPoly2 = gf(int(poly2, 16))
            fieldPolyInt1 = int(poly1, 16)
            fieldPolyInt2 = int(poly2, 16)
        if fieldPoly1 is None or fieldPoly2 is None:
            raise ValueError("Invalid input type")

        if fieldPolyInt2 == 0:
            raise ValueError("Division by 0 not allowed!")

        resultInt = fieldPolyInt1
        modDegree = fieldPolyInt2.bit_length() - 1  # Degree of the modulus polynomial

        while resultInt.bit_length() - 1 >= modDegree:
            degreeDiff = resultInt.bit_length() - modDegree - 1  # Degree difference
            resultInt ^= (
                fieldPolyInt2 << degreeDiff
            )  # XOR the mod shifted to align with poly's leading term
        result = gf(resultInt)
        return result

    except ValueError as e:
        raise ValueError(e)