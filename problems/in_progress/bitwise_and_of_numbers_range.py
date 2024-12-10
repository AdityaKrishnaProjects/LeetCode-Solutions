def rangeBitwiseAnd(left, right):
    """
    :type left: int
    :type right: int
    :rtype: int
    """
    
    if left == right:
        return left

    blen = 0
    int_right = right
    int_left = left

    while int_right != 0:
        if ((int_right >> 1) != 0) and ((int_left >> 1) == 0):
            return 0  
        blen += 1
        int_right >>= 1
        int_left >>= 1 

    # subtract by successive bits and then and them (1, 2, 4, 8, 16, etc.)
    right_c = right

print(rangeBitwiseAnd(5,7))
print(rangeBitwiseAnd(7,7))
print(rangeBitwiseAnd(5,5))
print(rangeBitwiseAnd(9,11))
print(rangeBitwiseAnd(8,9))