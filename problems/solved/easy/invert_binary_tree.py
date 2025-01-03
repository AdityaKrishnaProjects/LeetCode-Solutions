# invert binary tree
def invertTree(root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """
    
    r_root = root

    if root != None:
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)

    return r_root