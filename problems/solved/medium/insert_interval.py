# # not clean but the logic makes sense. Find left edge, once you do, append to
# # results list and search for right edge, once you do merge remaining. 
# def insert(intervals, newInterval):
    
#     r_list = []
#     left_edge = [newInterval[0], False]
#     right_edge = [newInterval[1], False]

#     for i in intervals:
#         if left_edge[0] <= i[1] and not left_edge[1]:
#             left_edge[0] = min(i[0], left_edge[0])
#             r_list.append([left_edge[0], right_edge[0]])
#             left_edge[1] = True
#         if left_edge[1] and not right_edge[1]:
#             if right_edge[0] >= i[0]:
#                 right_edge[0] = max(i[1], right_edge[0])
#                 r_list[-1][1] = right_edge[0]
#                 continue
#             else:
#                 right_edge[1] = True
#                 r_list.append(i)
#                 continue
#         r_list.append(i)

#     if not left_edge[1]:
#         r_list.append(newInterval)

#     return r_list
            
# print(insert([[1,3],[6,9]], [2,5]))
# print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
# print(insert([[1,5]], [2,3]))
# print(insert([], [5,7]))
# print(insert([[1,5]], [6,8]))
# print(insert([[2,5],[6,7],[8,9]], [0,1]))

# much cleaner implementation of the same idea

def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result