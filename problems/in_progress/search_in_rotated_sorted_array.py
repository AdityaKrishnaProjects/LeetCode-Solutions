# The pivot is between index 1 and N-1, so we know that pivot is 
# gauranteed to exist within the array. The value of our pivot 
# is equal to the number of values that will be displaced to the 
# end of the array in their original sorted order.
# Searching for the pivot requires us to find the place where the 
# array stops being strictly increasing (we know that all values 
# are unique). We can select the middle of the array and compare 
# out current value with our next value, we first check if this 
# value is the pivot (if the next value is less than the current value).
def search(nums, target):
