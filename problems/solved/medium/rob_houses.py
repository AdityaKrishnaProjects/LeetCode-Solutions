# suffix dp, problem is symmetric. Would be exponential in growth if we didn't 
# cache but because we do each index only has constant computations and we see 
# each index once so our solution is linear time and space 
def rob(nums):
    
    N = len(nums)
    has_cache = [False] * N
    cache = [None] * N

    def getMax(index):
        if index >= N:
            return 0

        if has_cache[index]:
            return cache[index]

        robThis = nums[index] + getMax(index+2)
        dontRobThis = getMax(index+1)

        cache[index] = max(robThis, dontRobThis)
        has_cache[index] = True
        
        return cache[index]

    return getMax(0)