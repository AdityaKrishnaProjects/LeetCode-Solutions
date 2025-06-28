# Happy with this. In BST we want to compare nodes in in order (from leftmost to 
# right most) within subtrees. This means a parent wants to be compared with its 
# rightmost left child and its leftmost right child.
def getMinimumDifference(root):
    
    difference = float("inf")
    last_val = None

    def trawl(node):
        nonlocal difference, last_val

        if node is None:
            return
        
        trawl(node.left)

        if last_val is not None:
            difference = min(difference, abs(node.val - last_val))
        
        last_val = node.val
        trawl(node.right)

    trawl(root)

    return difference