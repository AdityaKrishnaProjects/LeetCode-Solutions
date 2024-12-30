# big implementation
# def canCompleteCircuit(gas, cost):
#     """
#     :type gas: List[int]
#     :type cost: List[int]
#     :rtype: int
#     """
    
#     N = len(gas)
#     pot_i = -1
#     curr_sum = 0

#     for i in range(2*N-1):
#         old_i = i
#         i %= N
#         diff = gas[i] - cost[i]

#         # finds candidate first values
#         if pot_i < 0:
#             if diff < 0:
#                 continue
#             # checks if we are on second loop (shouldn't reconsider candidates)
#             if old_i < N:
#                 pot_i = i
        
#         # checks if candidates ever fail
#         curr_sum += diff
#         if curr_sum < 0:
#             pot_i = -1
#             curr_sum = 0

#     return pot_i
    
# print(canCompleteCircuit([4,5,2,6,5,3], [3,2,7,3,2,9]))

# simple implementation. Intuition is that if the sum ever 
# goes negative we need a new candidate. This works because 
# we know the solution is unique. 
def gasstation(gas, cost):
    sum_gas=sum(gas)
    sum_cost=sum(cost)
    if sum_cost>sum_gas:
        return -1
    current=0
    index=0
    for i in range(len(gas)):
        current+=gas[i]-cost[i]
        if current<0:
            current=0
            index=i+1
    return index

print(gasstation([1000,-1001,1010,1,10,-1000]))