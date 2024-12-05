import galois

def multiplication(poly1: str, poly2: str, input_type: str, m: int = 163):

    """
    Multiplies two polynomials in any Galois field.
    Args:
        poly1 (str): The first polynomial in either binary or hexadecimal format.
        poly2 (str): The second polynomial in either binary or hexadecimal format.
        input_type (str): The format of the input polynomials ('binary' or 'hexadecimal').
        m (int): The degree of the polynomial field. Default is 163.
    Returns:
        galois.FieldArray: The result of the multiplication in the Galois field.
    Raises:
        ValueError: If the input type is invalid or conversion doesnt work.
    """
    gf = galois.GF(2**m)
    field_poly1 = None
    field_poly2 = None
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
#Do multiplication
        return field_poly1 * field_poly2
    except ValueError as e:
        raise ValueError(e)