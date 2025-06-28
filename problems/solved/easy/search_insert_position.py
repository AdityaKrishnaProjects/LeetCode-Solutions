def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    N = len(nums)

    left = 0
    # right equal to N, even though right is inclusive as target can be outside 
    # of bound
    right = N

    while left < right:
        mid = (left+right)//2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    # loop terminates when left = right as mid+1 will never make left greater 
    # than right. If target bigger than any number in list right will be equal 
    # to the N, or one greater than the last index in the list.  
    return left