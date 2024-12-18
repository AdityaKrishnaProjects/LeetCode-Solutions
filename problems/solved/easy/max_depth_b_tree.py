# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """

    # stops recursion on null 
    if root is None:
        return 0
    
    # gets depth of right and left
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    
    # sets depth of root to 1 + max of next depths
    return 1 + max(left_depth, right_depth)