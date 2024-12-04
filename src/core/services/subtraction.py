import galois

from src.core.services.mod_reduction import gf2Mod


def subtraction(poly1: str, poly2: str, inputType: str, m: int = 163) -> galois.FieldArray:
    """
    Subtracts 2 polynomials in a Galois Field GF(2^m).

    Arguments:
    poly1: The first polynomial in binary or hexadecimal format.
    poly2: The second polynomial in binary or hexadecimal format.
    poly1 and poly2 are assumed to be valid inputs for GF(2^m).
    inputType: The format of both input polynomials ('binary' or 'hexadecimal').
    m(int,optional) : The degree of the polynomial field. Set to 163 if not specified.

    Returns:
    The result of the subtraction in a the Galois Field .

    Raises:
    ValueError: If the input type is invalid or conversion fails.
    """

    # Initialize the Galois Field
    gf = galois.GF(2**m)
    fieldPoly1 = None
    fieldPoly2 = None

    try:
        # If the input is not compatible in the galois field of the input
        # If the input is not compatible in the galois field of the input
        if inputType == "binary":
            if int(poly1, 2) > 2**m:
                if m != 571:
                    irreduciblePoly = gf.irreducible_poly
                    integerRep = int(irreduciblePoly)
                    poly1 = gf2Mod(int(poly1, 2), integerRep, inputType, m)
                elif (
                    m == 571
                ):  # The most use GF(2^571) polynomial since not stored in library is : x^571 + x^507 + x^475 + 1
                    integerRep = 2**571 + 2**507 + 2**475 + 1
                    poly1 = gf2Mod(int(poly1, 2), integerRep, inputType, m)
            if int(poly2, 2) > 2**m:
                if m != 571:
                    irreduciblePoly = gf.irreducible_poly
                    integerRep = int(irreduciblePoly)
                    poly2 = gf2Mod(int(poly2, 2), integerRep, inputType, m)
                elif (
                    m == 571
                ):  # The most use GF(2^571) polynomial since not stored in library is : x^571 + x^507 + x^475 + 1
                    integerRep = 2**571 + 2**507 + 2**475 + 1
                    poly2 = gf2Mod(int(poly2, 2), integerRep, inputType, m)
        elif inputType == "hexadecimal":
            if int(poly1, 16) > 2**m:
                if m != 571:
                    irreduciblePoly = gf.irreducible_poly
                    integerRep = int(irreduciblePoly)
                    poly1 = gf2Mod(int(poly1, 16), integerRep, inputType, m)
                elif (
                    m == 571
                ):  # The most use GF(2^571) polynomial since not stored in library is : x^571 + x^507 + x^475 + 1
                    integerRep = 2**571 + 2**507 + 2**475 + 1
                    poly1 = gf2Mod(int(poly1, 2), integerRep, inputType, m)
            if int(poly2, 16) > 2**m:
                if m != 571:
                    irreduciblePoly = gf.irreducible_poly
                    integerRep = int(irreduciblePoly)
                    poly2 = gf2Mod(int(poly2, 2), integerRep, inputType, m)
                elif m == 571:
                    integerRep = 2**571 + 2**507 + 2**475 + 1
                    poly2 = gf2Mod(int(poly2, 16), integerRep, inputType, m)

        # Convert based on the input type to the integer representation
        if inputType == "binary":  # If the input is in base 2
            fieldPoly1 = gf(int(poly1, 2))
            fieldPoly2 = gf(int(poly2, 2))
        elif inputType == "hexadecimal":  # If the inut is in base 16
            fieldPoly1 = gf(int(poly1, 16))
            fieldPoly2 = gf(int(poly2, 16))
        else:  # If the input is not in binary or decimal
            raise ValueError("Invalid input type!")

        result = (
            fieldPoly1 - fieldPoly2
        )  # Compute the subtraction (galois.FieldArray is interger)

        return result  # return the result

    except ValueError as e:
        raise ValueError(e)
