# inverse.py

import math

import galois


def inverse(poly: str, input_type: str, m: int = 163) -> str:
    """
    Compute the multiplicative inverse of a polynomial in a Galois Field.

    Args:
        poly (str): The polynomial to invert, represented as a string.
        input_type (str): The format of the input polynomial, either 'binary' or 'hexadecimal'.
        m (int, optional): The degree of the Galois Field. Defaults to 163.

    Returns:
        str: The multiplicative inverse of the polynomial in the same format as the input.

    Raises:
        ValueError: If the input type is not 'binary' or 'hexadecimal'.
        ValueError: If the polynomial is not within the valid range for the specified Galois Field.
        ValueError: If the polynomial is zero, as inversion is not possible for zero.
    """
    if m == 8:
        gf = galois.GF(2**m, irreducible_poly=0x11B)
    elif m == 233:
        irreducible_poly_233 = (1 << 233) | (1 << 74) | 1
        gf = galois.GF(2**m, irreducible_poly=irreducible_poly_233)
    else:
        gf = galois.GF(2**m)

    if input_type == "binary":
        poly_int = int(poly, 2)
    elif input_type == "hexadecimal":
        poly_int = int(poly, 16)
    else:
        raise ValueError("Invalid input type. Must be 'binary' or 'hexadecimal'.")

    if not (0 <= poly_int < 2**m):
        raise ValueError(
            f"GF(2^{m}) scalars must be in `0 <= x < {2**m}`, not {poly_int}."
        )

    field_poly = gf(poly_int)

    if field_poly == 0:
        raise ValueError("Polynomial inversion is not possible for zero.")

    inverse_poly = gf(1) / field_poly
    inverse_int = int(inverse_poly)

    if input_type == "binary":
        result = bin(inverse_int)[2:].zfill(m)
    else:
        hex_length = math.ceil(m / 4)
        result = hex(inverse_int)[2:].upper().zfill(hex_length)

    return result
