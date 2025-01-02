# shows I have a weakpoint in recursion
def isSameTree(p, q):
    """
    :type p: Optional[TreeNode]
    :type q: Optional[TreeNode]
    :rtype: bool
    """

    if (not p and q) or (not q and p):
        return False

    if (not p and not q):
        return True

    if p.val != q.val:
        return False

    return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))