# tree traversal and recursion
def sumOfLeftLeaves(root):

    def search(root, left):
        total = 0
        child = False

        if root.left:
            total += search(root.left, True)
            child = True
        if root.right:
            total += search(root.right, False)
            child = True

        if not child and left:
            total += root.val 

        return total

    return search(root, False)