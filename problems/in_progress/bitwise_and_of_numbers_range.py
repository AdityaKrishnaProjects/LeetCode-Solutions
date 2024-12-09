def rangeBitwiseAnd(left, right):
    """
    :type left: int
    :type right: int
    :rtype: int
    """
    
    l_blen = 0
    r_blen = 0
    int_left = left
    int_right = right

    while int_left != 0:
        if ((int_left >> 1) != 0):
            l_blen += 1

        int_left >>= 1

    while int_right != 0:
        if ((int_right >> 1) != 0):
            r_blen += 1

        int_right >>= 1

    if l_blen != r_blen:
        return 0

    mult = 2**l_blen

    r_int = 0
    while (left != 0) and (right != 0):
        if ((left-mult) > -1) and ((right-mult) > -1):
            left -= mult
            right -= mult
            r_int += mult
        elif ((right-mult) > -1):
            right -= mult
        elif ((left-mult) > -1):
            left -= mult
        mult //= 2

    return r_int

print(rangeBitwiseAnd(5,7))
print(rangeBitwiseAnd(7,7))
print(rangeBitwiseAnd(8,16))
print(rangeBitwiseAnd(0,0))
print(rangeBitwiseAnd(1,2147483647))
print(rangeBitwiseAnd(2147483646,2147483647))
print(rangeBitwiseAnd(44,55))
print(rangeBitwiseAnd(33,44))