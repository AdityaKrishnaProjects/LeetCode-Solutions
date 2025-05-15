# Using sliding window, we only ever move the left and right index N times each. 
# The operations we do after moving them are constant, so the algorithm runs in 
# O(n) time and constant space. The reason we will never miss a possibly smaller 
# subarray is that as we slide the window to the right we consider the smallest 
# possible subarray with our current left value, and then we slide the left 
# value to consider the smallest possible subarray with our right value.
def minSubarraySum(nums, target):
    
    N = len(nums)
    best = float("inf")
    total = 0
    left = 0

    for right in range(N):
        total += nums[right]

        while total >= target:
            best = min(best, (right-left+1))
            total -= nums[left]
            left += 1

    if best == float("inf"):
        return 0
    else: 
        return best


print(minSubarraySum([2,3,1,2,4,3], 7))
print(minSubarraySum([1,4,4], 4))
print(minSubarraySum([1,1,1,1,1,1,1,1], 11))
print(minSubarraySum([12,28,83,4,25,26,25,2,25,25,25,12], 213))
print(minSubarraySum([1,4,4], 9))