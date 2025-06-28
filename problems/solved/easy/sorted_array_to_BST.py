def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: Optional[TreeNode]
    """
    
    N = len(nums)

    def construct(left,right):
        if left > right:
            return None
        
        mid = (left + right)//2

        node = TreeNode(nums[mid])
        node.left = construct(left, mid-1)
        node.right = construct(mid+1, right)

        return node

    return construct(0,N-1)