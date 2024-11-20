def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    
    k_counter = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k_counter] = nums[i]
            k_counter += 1
        
    print(nums)
    return k_counter

print(removeElement([0,1,2,3,2,2,1,3,5], 2))

print(removeElement([0,1,2,2,3,0,4,2], 2))

print(removeElement([1],1))

print(removeElement([2],3))