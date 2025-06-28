# complement of min subarray is best possible wrap around case.
def maxSubarraySumCircular(nums):
    
    best = float('-inf')
    worst = float('inf')
    curr, neg_curr, total = 0, 0, 0

    for x in nums:
        curr = max(x, curr + x)
        neg_curr = min(x, neg_curr + x)
        worst = min(worst, neg_curr)
        best = max(best, curr)
        total += x

    return best if best < 0 else max(best, total - worst)

print(maxSubarraySumCircular([1,-2,3,-2]))
print(maxSubarraySumCircular([5,-3,5]))
print(maxSubarraySumCircular([-3,-2,-3]))
print(maxSubarraySumCircular([5,-3,5,-6,5]))
print(maxSubarraySumCircular([5,-3,5,-10,5]))