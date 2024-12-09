def rangeBitwiseAnd(left, right):
    """
    :type left: int
    :type right: int
    :rtype: int
    """
    
    b_len = 0
    int_left = left

    while int_left != 0:
        if ((int_left >> 1) != 0):
            b_len += 1

        int_left >>= 1

    mult = 2**b_len

    print(mult)

print(rangeBitwiseAnd(5,7))
print(rangeBitwiseAnd(7,7))
print(rangeBitwiseAnd(8,16))
print(rangeBitwiseAnd(0,0))
print(rangeBitwiseAnd(1,2147483647))
print(rangeBitwiseAnd(2147483646,2147483647))