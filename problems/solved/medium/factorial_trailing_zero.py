def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    
    # every number can be decomposed into its prime factors, trailing zeros are 
    # a result of multiplications with factors of 5. Only numbers that can be 
    # divided by 5 contribute to trailing 0s, with some contributing more if 
    # they contain multiple factors of 5.

    # count = 0
    # while n >= 5:
    #     n //= 5
    #     count += n
    # return count

    return n//5 + n//25 + n//125 + n//625 + n//3125

print(trailingZeroes(3))
print(trailingZeroes(25))
print(trailingZeroes(0))