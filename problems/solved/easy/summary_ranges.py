# intervals
def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    
    if not nums:
        return ""

    N = len(nums)
    r_list = []
    i = 0
    new_interval = True

    while i < N:
        if new_interval:
            candidate_val = str(nums[i]) + "->"
            init_i = nums[i]
            new_interval = False
        if (i+1 < N) and ((nums[i]+1) == (nums[i+1])):
            i += 1
            continue
        else:
            if nums[i] == init_i:
                candidate_val = str(init_i)
            else:
                candidate_val += str(nums[i])
            r_list.append(candidate_val)
            new_interval = True
            i += 1

    return r_list

print(summaryRanges([0,1,2,4,5,7]))
print(summaryRanges([0,2,3,4,6,8,9]))
print(summaryRanges([]))