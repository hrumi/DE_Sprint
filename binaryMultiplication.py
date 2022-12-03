def mult(binary, binary1):
    
    b = int(binary, 2)
    b1 = int(binary1, 2)

    return bin(b * b1)[2:]

print (mult("111", "101"))

