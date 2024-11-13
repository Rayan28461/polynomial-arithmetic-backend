import galois
from galois import FieldArray


def add(poly1: list[int], poly2: list[int], m: int = 163) -> FieldArray:
    gf = galois.GF(2**m)
    field_poly1 = gf(poly1)
    field_poly2 = gf(poly2)
    return field_poly1 + field_poly2
