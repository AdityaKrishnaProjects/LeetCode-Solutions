# should do more heap problems
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    
    h = []

    def push(x):
        heapq.heappush(h, x)

    def pop():
        return heapq.heappop(h)

    for x in nums:
        push(x)

        while len(h) > k:
            pop()

    return pop()