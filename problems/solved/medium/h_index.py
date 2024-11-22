# decent solution but could be more efficient
def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    
    current_index = len(citations)-1
    citations.sort(reverse=True)

    while current_index >= 0:
        if citations[current_index] >= (current_index + 1):
            return current_index + 1

        current_index -= 1
    
    return 0

print(hIndex([6,0,6,1,5]))
print(hIndex([1,3,1]))
print(hIndex([0]))
print(hIndex([9]))