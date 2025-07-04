# The pivot, k is between index 1 and N-1, so we know that pivot is 
# gauranteed to exist within the array. N-k is equal to the number
# of values displaced to the end of the list. Any value to the right
# of the pivot is strictly less than any value to the left of the 
# pivot, so we know that any value less than the first value of the 
# list must be a part of the right of the pivot (as the first value 
# must always be to the left of the pivot). If the current value we 
# are checking is greater than the next value it is the pivot. If 
# not: if it is greater than the first value of the list the pivot 
# is to the right, if it is less than the first value of the list, 
# the pivot is to the left
def search(nums, target):
    
    N = len(nums)

    l, r = 0, N-1

    while l < r:
        mid = (l + r)//2

        if nums[mid] > nums[mid+1]:
            pivot = mid
            break

        if nums[mid] > nums[0]:
            l = mid
        else:
            r = mid
    
    return pivot

print(search(,))
print(search(,))
print(search(,))
print(search(,))
print(search(,))
print(search(,))