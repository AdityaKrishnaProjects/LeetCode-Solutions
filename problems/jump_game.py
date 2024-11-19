# Pretty happy with this. Would be nice if the singleton case was not a 
# special case
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
        
    distance_to_goal = 1

    for i in range(len(nums)-2, 0, -1):
        if nums[i] >= distance_to_goal:
            distance_to_goal = 1
        else:
            distance_to_goal += 1

    if len(nums) == 1 or nums[0] >= distance_to_goal:
        return True 

    return False

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))
print(canJump([2,3,0,0,4]))
print(canJump([3]))
print(canJump([2,0,0]))