def maxArea(height):

    N = len(height)

    l, r = 0, N-1
    max_area = float("-inf")

    while l < r:
        max_area = max((min(height[l], height[r])*(r-l)), max_area)

        if height[l] < height[r]:
            l += 1

        elif height[l] > height[r]:
            r -= 1

        else:
            l += 1
        
    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
print(maxArea([0,0]))
print(maxArea([5,5,5,5,5]))