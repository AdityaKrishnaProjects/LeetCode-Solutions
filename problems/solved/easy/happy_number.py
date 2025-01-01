# works fine
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    
    seen = set()

    def happyNum(n):
        hapNum = 0
        while n != 0:
            hapNum += (n % 10)**2
            n //= 10
        if hapNum in seen:
            return False
        seen.add(hapNum)
        return hapNum
    
    while n > 1:
        n = happyNum(n)

    return (n == 1)

print(isHappy(19))
print(isHappy(2))
print(isHappy(1))
print(isHappy(235))