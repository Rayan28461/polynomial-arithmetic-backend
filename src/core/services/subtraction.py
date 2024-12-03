import galois

def subtraction(poly1:str, poly2:str, inputType: str, m:int=163) -> galois.FieldArray:
    """
    Subtracts 2 polynomials in a Galois Field GF(2^m).

    Arguments:
    poly1: The first polynomial in binary or hexadecimal format.
    poly2: The second polynomial in binary or hexadecimal format.
    poly1 and poly2 are assumed to be valid inputs for GF(2^m).
    inputType: The format of both input polynomials ('binary' or 'hexadecimal').
    m(int,optional) : The degree of the polynomial field. Set to 163 if not specified.

    Returns:
    galois.FieldArray: The result of the subtraction in a the Galois Field.

    Raises:
    ValueError: If the input type is invalid or conversion fails.
    """

    #Initialize the Galois Field
    gf=galois.GF(2**m)
    fieldPoly1=None
    fieldPoly2=None

    try:
        #Convert based on the input type to base 10
        if inputType=='binary': #If the input is in base 2
            fieldPoly1=gf(int(poly1,2))
            fieldPoly2=gf(int(poly2,2))
        elif inputType=='hexadecimal': #If the inut is in base 16
            fieldPoly1=gf(int(poly1,16))
            fieldPoly2=gf(int(poly2,16))
        else: #If the input is not in binary or decimal
            raise ValueError('Invalid input type!')

        result = fieldPoly1-fieldPoly2 #Compute the subtraction (galois.FieldArray is interger)

        if inputType == 'binary': #Convert result into binary
            return bin(int(result))[2:].zfill(m)  # Binary string padded to m bits and removing the prefix 
        elif inputType == 'hexadecimal': #Convert result into hexadecimal
            return hex(int(result))[2:].upper().zfill(m // 4)  # Hex string padded to m/4 characters and removing the prefix
        return result #return the result 
    
    except ValueError as e:
        raise ValueError(e)
