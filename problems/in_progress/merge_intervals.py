# O(Nlogn), happy with the solution but wonder if there is a way to do it 
# without sorting that doesn't take tons of space
def merge(intervals):
    
    N = len(intervals)
    sort = sorted(intervals, key = lambda x: x[0])
    r_list = [sort[0]]
    right_edge = sort[0][1]

    print(sort)

    for i in range(1, N):
        if sort[i][0] <= right_edge:
            new_right_edge = max(sort[i][1], r_list[len(r_list)-1][1])
            r_list[len(r_list)-1][1] = new_right_edge
            right_edge = new_right_edge
        else:
            r_list.append(sort[i])
            right_edge = sort[i][1]

    return r_list

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,4],[4,5], [0,4]]))
print(merge([[1,4],[2,3]]))
print(merge([[1,4],[0,4]]))
print(merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))