# uses two pointers. Since array is sorted, we can look for the optimal sum by 
# adjusting the left or right index. If sum too large for target, we can adjust 
# right pointer one to the left, as we know any sum with that right value
# will be too large (left pointer is pointing to smallest potentially valid 
# index). If sum too small for target we move left pointer one to the right, as 
# we know that any sum with that left value will be too small (right pointer is 
# pointing to largest potentially valid index)
def twoSum(numbers, target):
    
    N = len(numbers)
    l, r = 0, N-1

    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l+1, r+1]