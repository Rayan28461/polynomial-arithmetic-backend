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
        if inputType == "binary":
            poly1Int = int(poly1, 2)
            poly2Int = int(poly2, 2)
        elif inputType == "hexadecimal":
            poly1Int = int(poly1, 16)
            poly2Int = int(poly2, 16)
        else:
            raise ValueError("Invalid input type. Use 'binary' or 'hexadecimal'.")
        if poly2Int == 0:
            raise ValueError("Modulo by zero is not allowed!")
        
        resultInt = 0
        if m == 571:
            resultInt = poly1Int
            modDegree = poly2Int.bit_length() - 1 

            while resultInt.bit_length() - 1 >= modDegree:
                degreeDiff = resultInt.bit_length() - modDegree - 1  
                resultInt ^= poly2Int << degreeDiff  
        else:
            gf = galois.GF(2**m)
            fieldPoly1 = galois.Poly(poly1Int, field=gf)
            fieldPoly2 = galois.Poly(poly2Int, field=gf)
            resultInt = fieldPoly1
            modDegree = fieldPoly2.degree

            while resultInt.degree >= modDegree:
                degreeDiff = resultInt.degree - modDegree
                resultInt ^= fieldPoly2 << degreeDiff

        return resultInt

    except ValueError as e:
        raise ValueError(e)
