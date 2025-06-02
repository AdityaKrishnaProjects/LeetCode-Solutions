# takes advantage of combinations being easily constructed using increasing 
# indices for well ordering. (If we are considering 2 as our starting element, 
# we can be sure we have done every combination with 1, so we no longer ever 
# need to consider 1 as a possible element)
def combine(n, k):
    """
    return k combinations of n
    """

    res = []

    def set_builder(path, start):
        if len(path) == k:
            res.append(path)
            return
        
        for i in range(start, n+1):
            path.append(i)
            set_builder(path[:], i+1)
            path.pop()
        
    set_builder([], 1)

    return res

print(combine(4, 2))
print(combine(1, 1))
print(combine(5, 5))