# two pointer solution works because moving the lower height value will never 
# sacrifice a potentially larger max area (width decreases, and so you would 
# rather move the heigher height so you can preserve a potentially larger area). 
# In other words once you have evaluated an area for two height elements, the 
# maximum area for those two elements has been achieved, unless there is a 
# higher height element that will enable of the the elements to use more of its 
# height (area is evaluated based on the smaller of the two heights). This means 
# that you should keep the heigher value and search for this higher area, as 
# moving the smaller value is the only way you may increase area by decreasing width.
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