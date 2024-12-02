from src.core.services.subtraction import substraction as sub

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
