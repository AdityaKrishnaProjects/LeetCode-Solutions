# # Highest values determine the total trapped rain water. Ideally pinpoint the highest 
# # value(s), and WLOG pick one and expand outwards to the next highest closest value, 
# # prioritizing height over distance (if current highest value is 5, even if the next
# # 5 value is at the end of the array we would select it, however if next highest 
# # is 4, and there are multiple, we would select the nearest 4 as our next highest 
# # value and continue the procedure). Measuring trapped rainwater between these indices
# # will always result in capturing the most rainwater, and will never access each 
# # index more than once (we can be sure all nodes of the same height will be visited 
# # as they will all be in the visitor set of any node of that height, hence selecting 
# # our first node at random from our set of highest nodes). In order to discover these 
# # highest nodes and their indices we can walk through the array, once from left 
# # to right, and once from right to left. If a value is higher or equal to our current 
# # value and not equal to 0 we will record it as a possible index and make it our 
# # current value. If we never find a higher value, we are on a strictly decreasing run, 
# # which will be covered by the second walk through. Space complexity is O(N), time 
# # complexity is O(N) as we take O(2N) to find our potential indices, and then we 
# # iterate between these indices to calculate trapped rain, seeing each index at 
# # most twice, performing O(1) operations.
# def trap(height):

#     N = len(height)
#     left_i = []
#     right_i = []
#     curr = 0

#     if N == 1:
#         return 0

#     for i in range(N):
#         if curr <= height[i]:
#             left_i.append(i)
#             curr = height[i]

#     curr = 0

#     for i in range(N-1, left_i[-1], -1):
#         if curr <= height[i]:
#             right_i.append(i)
#             curr = height[i]

#     total = 0
#     indices = left_i + right_i[::-1]
#     print(indices)

#     for i, j in zip(indices, indices[1:]):
#         curr = min(height[i], height[j])*(j-i-1)
#         for k in range(i+1, j):
#             curr -= height[k]
#         total += curr

#     return total

# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(trap([4,2,0,3,2,5]))
# print(trap([4,2,0,3,2,3]))
# print(trap([1]))
# print(trap([0]))
# print(trap([5,5,5]))

# Should do two pointer solution that takes O(1) space.
def rain(heights):
    pass