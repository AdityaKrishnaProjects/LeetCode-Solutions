def rob(nums):
    
    N = len(nums)
    has_cache = [False] * N
    cache = [None] * N

    def getMax(index):
        if index >= N:
            return 0

        robThis = nums[index] + getMax(index+2)
        dontRobThis = getMax(index+1)

        cache[index] = max(robThis, dontRobThis)
        has_cache[index] = True
        
        return cache[index]

    return getMax(0)