def containsNearbyDuplicate(nums, k):
    """
    gets list of nums and returns true if 
    there are duplicates and their distance is less than k
    """
    
    seen = {}

    for i in range(len(nums)):
        val = nums[i]
        if val not in seen:
            seen[val] = i
        elif (i - seen[val]) > k:
            seen[val] = i
        else:
            return True

    return False


print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(containsNearbyDuplicate([1,2,3,1,2,3], 3))
print(containsNearbyDuplicate([1], 1))
print(containsNearbyDuplicate([1,0,1,1], 0))