# # solution for O(n)
# def countNodes(root):
#     """
#     :type root: Optional[TreeNode]
#     :rtype: int
#     """
    
#     if root is None:
#         return 0

#     return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# left or right subtree must be perfect, so we can check if they are the same 
# depth, if they are not then we know that the right subtree is perfect, so we 
# can add 2^n, to account for the nodes in this perfect subtree and the parent 
# node and then call countNodes on the remaining left subtree. If they are 
# equal in depth then we know the left subtree is perfect and we can do the same 
# but call countNodes on the right subtree 
def countNodes(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    
    def subTreeDepth(root):
        if root is None:
            return 0
        return subTreeDepth(root.left) + 1

    if root is None:
        return 0
    
    leftDepth = subTreeDepth(root.left)
    rightDepth = subTreeDepth(root.right)

    if leftDepth == rightDepth:
        return (2 ** leftDepth) + self.countNodes(root.right)
    else:
        return (2 ** rightDepth) + self.countNodes(root.left)
    