def rangeBitwiseAnd(left, right):
    """
    :type left: int
    :type right: int
    :rtype: int
    """
    
    blen = 0
    int_right = right
    int_left = left

    # Count the number of bits for which left and right are non-zero
    while int_right != 0:
        if ((int_right >> 1) != 0) and ((int_left >> 1) == 0):
            return 0  # If right has higher bits set than left, return 0
        else:
            blen += 1
            int_right >>= 1  # Right shift to check the next bit
            int_left >>= 1 

    # can't figure out how to determine what ints are good and candidates
    poss_and = (1 << blen) - 1
    new_left = left
    mult = 0

    while poss_and > left:
        poss_and -= (1 << mult)
        if poss_and > left and poss_and < right:
            new_left &= poss_and
        mult += 1

    return new_left & right

print(rangeBitwiseAnd(5,7))
print(rangeBitwiseAnd(7,7))
print(rangeBitwiseAnd(5,5))
print(rangeBitwiseAnd(9,11))