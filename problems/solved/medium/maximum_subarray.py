# subarray is contiguous, so once array stops contributing to sum 
# (current sum goes negative), start new sum with current num. 
def maxSubArray(nums):
    
    best = float('-inf')
    curr = 0

    for n in nums:
        curr = max(n, curr + n)
        best = max(curr, best)
    
    return best