import galois


def add(poly1: str, poly2: str, input_type: str, m: int = 163) -> galois.FieldArray:
    """
    Adds two polynomials in a Galois field.

    Args:
        poly1 (str): The first polynomial in either binary or hexadecimal format.
        poly2 (str): The second polynomial in either binary or hexadecimal format.
        input_type (str): The format of the input polynomials ('binary' or 'hexadecimal').
        m (int, optional): The degree of the polynomial field. Defaults to 163.

    Returns:
        galois.FieldArray: The result of the addition in the Galois field.

    Raises:
        ValueError: If the input type is invalid or conversion fails.
    """
    if m == 571:
        if input_type == "binary":
            return int(poly1, 2) ^ int(poly2, 2)
        elif input_type == "hexadecimal":
            return int(poly1, 16) ^ int(poly2, 16)
        
    gf = galois.GF(2**m)
    field_poly1, field_poly2 = None, None

    try:
        # Convert based on input type
        if input_type == "binary":
            field_poly1 = gf(int(poly1, 2))
            field_poly2 = gf(int(poly2, 2))
        elif input_type == "hexadecimal":
            field_poly1 = gf(int(poly1, 16))
            field_poly2 = gf(int(poly2, 16))

        if field_poly1 is None or field_poly2 is None:
            raise ValueError("Invalid input type")
        return field_poly1 + field_poly2
    except ValueError as e:
        raise ValueError(e)
