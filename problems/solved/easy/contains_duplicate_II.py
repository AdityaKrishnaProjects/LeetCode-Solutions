# decent solution, O(n) time and space complexity
def containsNearbyDuplicate(nums, k):
    """
    gets list of nums and returns true if 
    there are duplicates and their distance is less than k
    """
    
    seen = {}

    for i in range(len(nums)):
        if nums[i] in seen and i - seen[nums[i]] <= k:
            return True
        seen[nums[i]] = i

    return False


print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(containsNearbyDuplicate([1,2,3,1,2,3], 3))
print(containsNearbyDuplicate([1], 1))
print(containsNearbyDuplicate([1,0,1,1], 0))