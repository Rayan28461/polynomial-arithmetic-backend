import galois

# from ...common.utils.types import BinStr, HexStr


def add(poly1: str, poly2: str, input_type: str, m: int = 163) -> galois.FieldArray:
    gf = galois.GF(2**m)
    field_poly1, field_poly2 = None, None

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
