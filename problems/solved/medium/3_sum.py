# sorts list of nums so we don't see duplicate as we are iterating through. 
# Picks out number, solves two sum with two pointer solution, then goes to next 
# number ignoring duplicates. O(n^2) + O(nlogn), so time complexity is O(n^2).
def threeSum(nums):
    
    nums.sort()
    N = len(nums)
    r_list = []

    for i in range(N):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l,r = (i+1), (N-1)
        target = -nums[i]

        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r_list.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return r_list