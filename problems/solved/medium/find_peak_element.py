# Can use binary search as we know that we are gauranteed to find a peak element
# on the side that contains a greater element than our mid element. We know 
# this because the boundaries are negative infinities, so there must be a peak 
# somewhere in the subarray containing the value greater than mid. 
def findPeakElement(nums):

    N = len(nums)
    left, right = 0, N-1

    while left < right:
        mid = (left + right)//2
        
        # right side contains gauranteed peak
        if nums[mid] < nums[mid+1]:
            left = mid + 1

        # left side contains gauranteed peak (could be mid)
        else:
            right = mid

    return left

print(findPeakElement([1,2,3,1]))
print(findPeakElement([1,2,1,3,5,6,4]))
print(findPeakElement([2]))
print(findPeakElement([1,2]))
print(findPeakElement([4, 3, 2, 1, 4]))