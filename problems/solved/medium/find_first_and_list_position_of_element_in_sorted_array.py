# Binary searches and finds lowest and highest target value. O(logN) + O(logN).
def searchRange(nums, target):
    N = len(nums)

    if N == 0 or (nums[N-1] < target) or (nums[0] > target):
        return [-1,-1]

    if N == 1:
        if nums[0] == target:
            return [0,0]
        else:
            return [-1,-1]

    l, r = 0, N-1

    res = [-1,-1]

    # left bound
    while l <= r:
        # floor mid (biases left)
        mid = (l+r)//2

        if r == 0 or l == r:
            if nums[r] == target:
                res[0] = r
            break

        if nums[mid] >= target:
            r = mid

        elif nums[mid] < target:
            l = mid + 1

    l, r = 0, N-1

    # right bound
    while l <= r:
        # ceiling mid (biases right)
        mid = -((l+r)//-2)

        if l == N-1 or l == r:
            if nums[l] == target:
                res[1] = l
            break

        if nums[mid] <= target:
            l = mid

        elif nums[mid] > target:
            r = mid - 1

    return res

print(searchRange([5,5,5,5,5,5],5))
print(searchRange([5,7,7,8,8,10],8))
print(searchRange([5,7,7,8,8,10],6))
print(searchRange([],0))
print(searchRange([5,7,7,8,8,10],5))
print(searchRange([1],1))
print(searchRange([2, 2, 2, 2, 2], 2))