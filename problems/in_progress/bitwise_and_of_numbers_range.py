# extremely happy with this solution
def rangeBitwiseAnd(left, right):
    """
    :type left: int
    :type right: int
    :rtype: int
    """

    # subtract by successive bits and then and them (1, 2, 4, 8, 16, etc.)
    n = 1
    while left < right:
        right &= (right ^ n)
        n <<= 1

    return left & right

print(rangeBitwiseAnd(5,7))
print(rangeBitwiseAnd(7,7))
print(rangeBitwiseAnd(5,5))
print(rangeBitwiseAnd(9,11))
print(rangeBitwiseAnd(8,9))
print(rangeBitwiseAnd(1,283983918))