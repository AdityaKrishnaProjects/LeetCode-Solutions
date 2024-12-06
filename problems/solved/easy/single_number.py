# beautiful solution
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    r_int = nums[0]

    for i in range(1, len(nums)):
        r_int = r_int ^ nums[i]

    return r_int

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))