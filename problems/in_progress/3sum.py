def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    r_list = []

    complements = {}
    seen = {}

    for n in nums:
        for k in seen:
            if (-(n+k) == n) or (-(n+k) == k):
                pass
            elif (-(n+k) in seen):
                r_list.append([-(n+k), n, k])
            elif -(n+k) in complements:
                complements[-(n+k)].append([n,k])
            else:
                complements[-(n+k)] = [[n,k]]
        seen[n] = 1

    print(complements)
    print(seen)

    return r_list

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([-1,0,1,2,-1,-4, 4,-3]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
print(threeSum([0,0,0,0,0]))
print(threeSum([-1,0,1,0]))