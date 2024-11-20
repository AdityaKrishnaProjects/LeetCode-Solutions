# Relatively straightforward one
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    k_counter = 1
    seen_value = nums[0]

    for i in nums:
        if i != seen_value:
            nums[k_counter] = i
            k_counter += 1
            seen_value = i
        
    print(nums)
    return k_counter

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

print(removeDuplicates([1,1,2]))