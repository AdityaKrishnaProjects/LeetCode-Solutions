# subtracting 1 from any power of 2 results in making all trailing 0s 1s. 
def isPowerOfTwo(n):
    
    return n > 0 and (n & (n-1) == 0)

print(isPowerOfTwo(-5))
print(isPowerOfTwo(0))
print(isPowerOfTwo(256))