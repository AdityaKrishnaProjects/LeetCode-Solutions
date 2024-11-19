# Pretty happy with this. Would be nice if the singleton case was not a 
# special case
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
        
    current_index = len(nums)-2
    distance_to_goal = 1

    while current_index > 0:
        if nums[current_index] >= distance_to_goal:
            distance_to_goal = 1
            current_index -= 1
        else:
            current_index -= 1
            distance_to_goal += 1

    if len(nums) == 1:
        return True 

    if nums[0] >= distance_to_goal:
        return True
    else:
        return False

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))
print(canJump([2,3,0,0,4]))
print(canJump([3]))
print(canJump([2,0,0]))