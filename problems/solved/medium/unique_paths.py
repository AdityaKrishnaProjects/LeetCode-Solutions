from math import comb

# Bot must go m down and n to the right. These choices can be made in any order, 
# but they all must be made. This can be simply represented as a combination. 
def uniquepaths(m, n):
    return comb(m+n-2, n-1)

print(uniquepaths(2,3))