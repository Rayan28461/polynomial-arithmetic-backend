import galois
#from src.core.services.mod_reduction import gf2Mod

def sub(poly1:str, poly2:str, inputType: str, m:int=163) :
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

    #Initialize the Galois Field
    gf=galois.GF(2**m)
    fieldPoly1=None
    fieldPoly2=None

    try:
         #If the input is not compatible in the galois field of the input    
        if inputType=='binary':
            if int(poly1,2)>2**m:
                if m!=571:
                    irreduciblePoly=gf.irreducible_poly 
                    integerRep=int(irreduciblePoly) 
                    poly1=gf2Mod(int(poly1,2), integerRep, inputType, m)
                if m==571: #The most use GF(2^571) polynomial since not stored in library is : x^571 + x^507 + x^475 + 1
                    integerRep=2**571+2**507+2**475+1
                    poly1=gf2Mod(int(poly1,2), integerRep, inputType, m)
            elif int(poly2,2)>2**m:
                if m!=571:
                    irreduciblePoly=gf.irreducible_poly 
                    integerRep=int(irreduciblePoly)
                    poly2=gf2Mod(int(poly2,2), integerRep, inputType, m)
                if m==571: #The most use GF(2^571) polynomial since not stored in library is : x^571 + x^507 + x^475 + 1
                    integerRep=2**571+2**507+2**475+1
                    poly2=gf2Mod(int(poly2,2), integerRep, inputType, m)
        elif inputType=='hexadecimal':
            if int(poly1,16)>2**m:
                if m!=571:
                    irreduciblePoly=gf.irreducible_poly 
                    integerRep=int(irreduciblePoly) 
                    poly1=gf2Mod(int(poly1,16), integerRep)
                if m==571: #The most use GF(2^571) polynomial since not stored in library is : x^571 + x^507 + x^475 + 1
                    integerRep=2**571+2**507+2**475+1
                    poly1=gf2Mod(int(poly1,2), integerRep, inputType, m)
            elif int(poly2,16)>2**m:
                if m!=571:
                    irreduciblePoly=gf.irreducible_poly 
                    integerRep=int(irreduciblePoly) 
                    poly2=gf2Mod(int(poly2,2), integerRep, inputType, m)
                if m==571:
                    integerRep=2**571+2**507+2**475+1
                    poly2=gf2Mod(int(poly2,16),integerRep)

        #Convert based on the input type to the integer representation
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
def testSub():
    #Test for binary input and small m = 8
    poly1 = '00001100'
    poly2 = '00000011'
    m1=8
    testCase1 = sub(poly1, poly2, 'binary',m1)
    expectedOutput1 = '00001111'
    if testCase1 == expectedOutput1 : print("Test Case 1 : Passed")
    else: print("Test Case 1 : Failed")

    #Test for binary input and large m = 163
    poly1 = '101' + ('0'*160)
    poly2 = '01' + ('0'*160) + '1'
    m2 = 163
    testCase2 = sub(poly1, poly2, 'binary', m2)
    expectedOutput2 = '111' + ('0'*159) + '1'
    if testCase2 == expectedOutput2 : print("Test Case 2 : Passed")
    else: print("Test Case 2 : Failed")

    #Test for hex input and small m = 8
    poly1 = '0C'
    poly2 = '03'
    m3 = 8
    testCase3 = sub(poly1, poly2, 'hexadecimal', m3) 
    expectedOutput3 = '0F'
    if testCase3 == expectedOutput3 : print("Test Case 3 : Passed")
    else: print("Test Case 3 : Failed")

    #Test for hex input and large m = 163
    poly1 = '05' + ('00'*20)
    poly2 = '01' + ('00'*19) + '01'
    m4 = 163
    testCase4 = sub(poly1, poly2, 'hexadecimal', m4)
    expectedOutput4 = '4' + ('00'*19) + '01'
    if testCase4 == expectedOutput4 : print("Test Case 4 : Passed")
    else: print("Test Case 4 : Failed")

    #Test Case for invalid binary input
    try:
        poly1 = '0010G'
        poly2 = '00110'
        m = 2
        sub(poly1, poly2, 'binary',m)
    except ValueError as e:
        print("Test Case 5: Passed Invalid Input")
    
    #Test Case for invalid hex input
    try:
        poly1 = '0010F'
        poly2 = '001Z0'
        m = 2
        sub(poly1, poly2, 'hexadecimal',m)
    except ValueError as e:
        print("Test Case 6: Passed Invalid Input")

print(testSub())
