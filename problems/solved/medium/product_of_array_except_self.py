# linear time, only constant space if you don't consider the output array space
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    N = len(nums)

    r_nums = [1 for i in range(N)]

    i, j = 1, N-2

    while i < N:
        r_nums[i] = r_nums[i-1] * nums[i-1]

        i+= 1

    temp = nums[N-1]
    temp2 = nums[N-1]
    while j > -1:
        temp2 *= nums[j]
        r_nums[j] = r_nums[j] * temp
        temp = temp2
        j -= 1

    return r_nums

print(productExceptSelf([1,23,3,14,24,12,45]))
print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
print(productExceptSelf([-1,1,1,-3,3]))