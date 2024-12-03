import galois

def modReduction(poly1:str, divisor:str, inputType:str, m:int=163):
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

    #Initialize the Galois Field
    gf=galois.GF(2**m)
    fieldPoly1=None
    fieldPoly2=None

    irreduciblePoly=gf.irreducible_poly #Extract the irreducible polynomial stored in the library
    integerRep=int(irreduciblePoly) #Integer representation of the irreducible polynomial

    #If the input is not compatible in the galois field of the input    
    if inputType=='binary':
        if int(poly1,2)>2**m:
            poly1=gf2Mod(poly1, integerRep)
        elif int(poly2,2)>2**m:
            poly2=gf2Mod(poly2,integerRep)
    elif inputType=='hexadecimal':
        if int(poly1,16)>2**m:
            poly1=gf2Mod(poly1, integerRep)
        elif int(poly2,16)>2**m:
            poly2=gf2Mod(poly2,integerRep)

    try:
        #Convert based on the input type to base 10
        if inputType=='binary': #If the input is in base 2
            fieldPoly1=(int(poly1,2))
            fieldPoly2=(int(poly2,2))
        elif inputType=='hexadecimal': #If the inut is in base 16
            fieldPoly1=(int(poly1,16))
            fieldPoly2=(int(poly2,16))
        else: #If the input is not in binary or decimal
            raise ValueError('Invalid input type!')
        
        result=gf2Mod(fieldPoly1, fieldPoly2) #Compute the Remainder of the division (poly1%poly2)

        if inputType == 'binary': #Convert result into binary
            return bin(int(result))[2:].zfill(m)  #Binary string padded to m bits and removing the prefix 
        elif inputType == 'hexadecimal': #Convert result into hexadecimal
            return hex(int(result))[2:].upper().zfill(m // 4)  #Hex string padded to m/4 characters and removing the prefix
        return result #return the result 

    except ValueError as e:
        raise ValueError(e)
        

def gf2Mod(poly:int, mod:int):
    """
    Perform modulo reduction of a polynomial over GF(2^m).
    
    Arguments:
    poly: Integer representation of the polynomial.
    mod: Integer representation of the divisor polynomial.

    Returns: Integer representation of the remainder polynomial.
    """

    mod_degree=mod.bit_length()-1  #Degree of the modulus polynomial
    
    while poly.bit_length()-1 >= mod_degree:
        degree_diff=poly.bit_length() - mod_degree - 1 #Degree difference
        poly^=mod<<degree_diff #XOR the mod shifted to align with poly's leading term
    
    return poly