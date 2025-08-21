# Propogate down imbalance or height to check for imbalance
def isBalanced(root):

    if root is None:
        return True

    def height(root):
        if root is None:
            return 0

        lh = height(root.left)

        if lh == -1:
            return -1
        
        rh = height(root.right)

        if rh == -1:
            return -1

        if abs(lh - rh) > 1:
            return -1
        
        return max(lh, rh)+1
    
    return (height(root) is not -1)