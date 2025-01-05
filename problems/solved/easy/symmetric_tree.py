def isSymmetric(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    
    def isMirror(L, R):
        if (L == None and R != None) or (L != None and R == None):
            return False
        if (L == None and R == None):
            return True
        return (L.val == R.val and isMirror(L.left, R.right) and isMirror(L.right, R.left))

    return isMirror(root, root)