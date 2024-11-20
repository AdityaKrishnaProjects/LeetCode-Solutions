# Uses Boyer-Moore majority vote algorithm. Intuition is that if we know that a 
# majority element exists then we can be certain that the candidate element we 
# get at the end must be this majority element (no other element can have a 
# positive counter). Say we have some element that makes up the last 4 values 
# in our list, but the total length of the list is 10 values, in order to have a 
# majority the first 6 values would have to be our majority element, which would 
# make our candidate element our majority element. This algorithm notably does 
# not work for pluralities.
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    candidate = None
    counter = 1

    for i in nums: 
        if i != candidate:
            counter -= 1
        else:
            counter += 1
        
        if counter == 0:
            candidate = i
            counter = 1

    return candidate