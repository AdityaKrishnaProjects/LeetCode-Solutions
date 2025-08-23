def minDepth(root):

    if root is None:
        return 0

    def minLook(root):
        if root.left is None and root.right is None:
            return 1
        elif root.right is None and root.left is not None:
            return minLook(root.left)+1
        elif root.left is None and root.right is not None:
            return minLook(root.right)+1

        return min(minLook(root.left), minLook(root.right))+1

    return minLook(root)