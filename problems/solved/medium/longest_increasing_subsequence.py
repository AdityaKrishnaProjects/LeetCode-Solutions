# Naive solution iterates through list and determines longest increasing subsequence by 
# determining whether current element can extend any previous elements longest 
# subsequence. O(N^2), as we iterate through the loop, and for each element we 
# iterate through the loop again. To improve on this logic, we realize that subsequences 
# are contributed to by their elements in order, so once we have an element in 
# the list, if we add another element that is greater we can store all our possible 
# future subsequences in the same list by simply replacing the value that our 
# value is smaller than. This doesn't change the length of our list, but does 
# allow future subsequences to potentially be greater.
import bisect

def lengthofLIS(nums):
    
    N = len(nums)
    tails = [float("inf")] * N

    for n in nums:
        i = bisect.bisect_left(tails, n)
        tails[i] = n

    for i in range(N):
        if tails[i] == float("inf"):
            return i
    
    return N

print(lengthofLIS([10,9,2,5,3,7,101,18]))
print(lengthofLIS([0,1,0,3,2,3]))
print(lengthofLIS([7,7,7,7,7,7,7]))

# Given array of nums

# Return length of longest strictly increasing subsequence
#     Subsequences can be derived from sequences by deleting some or no elements without changing order of the remaining elements
#         evaluating all subsets requires entertaining N^2 subsets

# nums can be negative

# nums = [0,1,0,3,2,3]

# We have to iterate through the whole loop as the subsequence could be the length of the entire list.
#     How do we keep track of competing subsequences?

# Knowing if a possible subsequence can be extended by a current element only requires we know the value of the last element in the subsequence. 
#     Once we have seen an element and entertained it as a part of some subsequence, it is no longer necessary to consider said element 
#         as either it is part of a subsequence, or it will never be used again

# Choices when looking at ith element:
#     If we have no subsequences:
#         Add ith element to possible subsequence
#     If we have one subsequence:
#         If ith element is greater than edge element of our subsequence:
#             Add element to length of subsequence, and replace edge element with ith element
#         If ith element is equal to edge element of our subsequence:
#             Does not contribute to current subsequence, 
#             Can not be starting element of a bigger subsequence 
#                 as we already have a longer subsequence ending in our edge element
#         If ith element is less than edge element of our subsequence:
#             Does not contribute to current subsequence
#             Could be a starting point of a larger subsequence if edge_element - nums[i] > length of current longest subsequence
#             Can always replace edge of subsequence
#                 This will be true for any subsequence containing a value larger than current value