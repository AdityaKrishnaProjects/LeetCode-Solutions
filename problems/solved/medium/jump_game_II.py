# Inefficient DP solution
def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    final_index = len(nums) - 1

    outcomes = [float("inf") for i in range(final_index+1)]

    outcomes[0] = 0

    for index, value in enumerate(nums):
        jumps = outcomes[index]+1

        if (index + value) < final_index:
            check_range = value
        else:
            check_range = final_index - index

        for i in range(1, check_range+1):
            if outcomes[index+i] > jumps:
                outcomes[index+i] = jumps

    return outcomes[final_index]

print(jump([1,3,4,15,0,0,1,2,1]))
print(jump([2,3,1,1,4]))
print(jump([2,3,0,1,4]))