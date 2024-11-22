def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
        
    potential_h = {}
    list_of_keys = set()

    for i in citations:
        if i not in potential_h:
            potential_h[i] = 1
            list_of_keys.add(i)
            continue

        for i in range(i+1):
            if i in list_of_keys:
                print(i)
                potential_h[i] = potential_h[i]+1

    print(potential_h)

hIndex([3,0,6,1,5])
hIndex([1,3,1])