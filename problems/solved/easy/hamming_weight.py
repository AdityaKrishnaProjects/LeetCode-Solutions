def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    
    count = 0

    while n != 0:
        count += n & 1
        n >>= 1

    return count

print(hammingWeight(11))
print(hammingWeight(3))
print(hammingWeight(2147483645))