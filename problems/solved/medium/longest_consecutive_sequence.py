# doesn't look elegant but I like the logic
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    seen = set()
    candidates = {}
    longest = 1

    for num in nums:
        if num in seen:
            continue
        seen.add(num)
        if (num+1 in candidates) and (num-1 in candidates):
            new_val = 1 + candidates[num-1][0] + candidates[num+1][0]
            right_edge = candidates[num+1][2]
            left_edge = candidates[num-1][1]
            candidates[left_edge][0] = new_val
            candidates[left_edge][2] = right_edge
            candidates[right_edge] = candidates[left_edge]
            longest = max(longest, new_val)
        elif num+1 in candidates:
            right_edge = candidates[num+1][2]
            candidates[right_edge][0] += 1
            candidates[right_edge][1] = num
            candidates[num] = candidates[right_edge]
            longest = max(longest, candidates[right_edge][0])
        elif num-1 in candidates:
            left_edge = candidates[num-1][1]
            candidates[left_edge][0] += 1
            candidates[left_edge][2] = num
            candidates[num] = candidates[left_edge]
            longest = max(longest, candidates[left_edge][0])
        else:
            candidates[num] = [1, num, num]

    return longest

print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([1,2,0,1]))
# print(longestConsecutive([100,4,200,1,3,2]))
# print(longestConsecutive([100,4,200,1,3,2]))