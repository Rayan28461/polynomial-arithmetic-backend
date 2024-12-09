import galois


def inverse(poly: str, input_type: str, m: int = 163) -> galois.FieldArray:
    """
    Computes the multiplicative inverse of a polynomial in a Galois field.

    Args:
        poly (str): The polynomial in either binary or hexadecimal format.
        input_type (str): The format of the input polynomial ('binary' or 'hexadecimal').
        m (int, optional): The degree of the polynomial field. Defaults to 163.

    Returns:
        galois.FieldArray: The multiplicative inverse of the polynomial in the Galois field.

    Raises:
        ValueError: If the input type is invalid, conversion fails, or the polynomial is zero.
    """
    gf = galois.GF(2**m)
    print(gf.irreducible_poly)
    field_poly = None

    try:
        if input_type == "binary":
            field_poly = gf(int(poly, 2))
        elif input_type == "hexadecimal":
            field_poly = gf(int(poly, 16))

        if field_poly is None:
            raise ValueError("Invalid input type")

        if field_poly == 0:
            raise ValueError("Inverse of zero is not defined in Galois fields")

        return gf(1) / field_poly

    except ValueError as e:
        raise ValueError(e)
