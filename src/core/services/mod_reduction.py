import galois

def modReduction(
    poly1: str, poly2: str, inputType: str, m: int = 163
) -> int:
    """
    Computes modulo reduction given 2 polynomials (poly1 % poly2) in a Galois Field GF(2^m).

    Arguments:
    poly1: The first polynomial in binary or hexadecimal format.
    poly2: The divisor in binary or hexadecimal format or the irreducible polynomial of a Galois field.
    inputType: The format of both input polynomials ('binary' or 'hexadecimal').
    m (int, optional): The degree of the polynomial field. Defaults to 163.

    Returns:
    Integer.

    Raises:
    ValueError: If the input type is invalid or conversion fails.
    """
    try:
        # Convert inputs based on the input type
        if inputType == "binary":
            poly1Int = int(poly1, 2)
            poly2Int = int(poly2, 2)
        elif inputType == "hexadecimal":
            poly1Int = int(poly1, 16)
            poly2Int = int(poly2, 16)
        else:
            raise ValueError("Invalid input type. Use 'binary' or 'hexadecimal'.")

        # Ensure division by zero is handled
        if poly2Int == 0:
            raise ValueError("Division by zero is not allowed!")

        # For m = 571, handle manually without galois
        if m == 571:
            resultInt = poly1Int
            modDegree = poly2Int.bit_length() - 1  # Degree of the modulus polynomial

            while resultInt.bit_length() - 1 >= modDegree:
                degreeDiff = resultInt.bit_length() - modDegree - 1  # Degree difference
                resultInt ^= poly2Int << degreeDiff  # XOR the mod shifted to align with the leading term

           

            return resultInt

        # For other values of m, use galois
        else:
            gf = galois.GF(2**m)
            fieldPoly1 = gf(poly1Int)
            fieldPoly2 = gf(poly2Int)
            resultInt = fieldPoly1
            modDegree = fieldPoly2.degree

            while resultInt.degree >= modDegree:
                degreeDiff = resultInt.degree - modDegree
                resultInt ^= fieldPoly2 << degreeDiff

            return resultInt

    except ValueError as e:
        raise ValueError(e)
