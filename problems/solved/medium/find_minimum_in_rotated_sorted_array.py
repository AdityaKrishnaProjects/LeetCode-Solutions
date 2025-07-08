# If index is rotated we know if we are greater than nums[0] we are to the left 
# of the min, and if we are less than nums[0] we are to the right of the min. 
# Binary search to find the min in O(logN).
def findMin(nums):
    N = len(nums)

    l, r = 0, N-1

    # deal with rotate by N case, and N == 1 case
    if N == 1 or nums[0] < nums[N-1]:
        return nums[0]

    while l <= r:
        mid = (l + r)//2

        if nums[mid] < nums[0]:
            r = mid - 1
        
        else:
            l = mid + 1

    return nums[l]

# print(findMin([3,4,5,1,2]))
# print(findMin([4,5,6,7,0,1,2]))
# print(findMin([1,2,3,4,5,6,7,0]))
# print(findMin([11,13,15,17]))
print(findMin([1]))
print(findMin([2,1]))
print(findMin([3,1,2]))