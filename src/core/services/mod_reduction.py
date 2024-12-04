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
                    if inputType == "binary":  # Convert result into binary
                        poly1 = bin(int(poly1))[2:].zfill(
                            m
                        )  # Binary string padded to m bits and removing the prefix
                    elif inputType == "hexadecimal":  # Convert result into hexadecimal
                        poly1 = (
                            hex(int(poly1))[2:].upper().zfill(m // 4)
                        )  # Hex string padded to m/4 characters and removing the prefix
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
            fieldPoly1 = int(poly1, 2)
            fieldPoly2 = int(poly2, 2)
        elif inputType == "hexadecimal":  # If the input is in base 16
            fieldPoly1 = int(poly1, 16)
            fieldPoly2 = int(poly2, 16)
        else:  # If the input is not in binary or decimal
            raise ValueError("Invalid input type!")

        resultInt = fieldPoly1
        modDegree = fieldPoly2.bit_length() - 1  # Degree of the modulus polynomial

        while resultInt.bit_length() - 1 >= modDegree:
            degreeDiff = resultInt.bit_length() - modDegree - 1  # Degree difference
            resultInt ^= (
                fieldPoly2 << degreeDiff
            )  # XOR the mod shifted to align with poly's leading term
        result = gf(resultInt)
        return result

    except ValueError as e:
        raise ValueError(e)


def gf2Mod(poly: int, mod: int, inputType: str, m: int) -> str:
    """
    Perform modulo reduction of a polynomial over GF(2^m) with the irreducible polynomial.

    Arguments:
    poly: Integer representation of the polynomial.
    mod: Integer representation of the irreducible polynomial.
    inputType: Original input type in order to return correct type for the modReduction function.
    m: Degree of the polynomial field set.

    Returns: Either a binary or hexadecimal representation of the remainder polynomial.
    """

    modDegree = mod.bit_length() - 1  # Degree of the modulus polynomial
    res = poly

    while poly.bit_length() - 1 >= modDegree:
        degreeDiff = poly.bit_length() - modDegree - 1  # Degree difference
        res ^= (
            mod << degreeDiff
        )  # XOR the mod shifted to align with poly's leading term
    if inputType == "binary":  # Convert result into binary
        res = bin(int(poly))[2:].zfill(
            m
        )  # Binary string padded to m bits and removing the prefix
    elif inputType == "hexadecimal":  # Convert result into hexadecimal
        res = (
            hex(int(poly))[2:].upper().zfill(m // 4)
        )  # Hex string padded to m/4 characters and removing the prefix
    return res  # return the result
