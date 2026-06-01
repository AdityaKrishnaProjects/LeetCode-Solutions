# bitwise or and then check final bits to see if they are 1 while removing the 
# final bit
def hammingDistance(x, y):
    ans = abs(x ^ y)
    total = 0

    while ans:
        total += (ans & 1)
        ans >>= 1

    return total

print(hammingDistance(1, 3))