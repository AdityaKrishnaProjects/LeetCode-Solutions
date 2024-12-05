# ok solution. Not very clean. 
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    
    if x == 0:
        return 0

    if x in (1, 2, 3):
        return 1

    pot = x // 2

    def sqrtTooBig(pot, x):
        last_pot = pot
        while pot * pot > x:
            last_pot = pot
            pot //= 2

        while last_pot - pot > 1:
            mid = (pot + last_pot) // 2
            if mid * mid <= x:
                pot = mid
            else:
                last_pot = mid

        return pot

    return sqrtTooBig(pot, x)


print(mySqrt(1))
print(mySqrt(0))
print(mySqrt(2))
print(mySqrt(3))
print(mySqrt(4))
print(mySqrt(124))
print(mySqrt(64))
print(mySqrt(53))
print(mySqrt(9097))