# first greedy algorithm. Arrived at the idea that the end of the first interval 
# will mark the best place to shoot independently, and the idea that the next 
# end will also be best which was great. Didn't understand how to implement said 
# algorithm without a ton of indexes till I arrived upon this. 
def findMinArrowShots(points):
    
    sorted_intervals = sorted(points, key = lambda x: x[1])
    count = 0
    seen_end = float('-inf')

    for interval in sorted_intervals:
        if interval[0] > seen_end:
            seen_end = interval[1]
            count += 1
        
    return count
 
print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))