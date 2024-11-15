# happy with this implementation
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    k_counter = 1
    count = 1
    seen = None
    length = len(nums)

    for i in range(1, length):
        if nums[i] != seen:
            if nums[i] == nums[i-1]:
                count += 1
                nums[k_counter] = nums[i]
                k_counter += 1
            else:
                nums[k_counter] = nums[i]
                k_counter += 1
            
        if count == 2:
            seen = nums[i]
            count = 1
        
    print(nums)
    return k_counter

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

print(removeDuplicates([1,1,2]))

print(removeDuplicates([1,1,1,2,2,3]))

print(removeDuplicates([0,0,1,1,1,1,2,3,3]))