# BST traversal with nonlocal variables
def kthSmallest(root, k):
    count = 0
    result = None

    def traverse(root):
        nonlocal count, result

        if node is None or result is not None:
            return

        traverse(root.left)
        count += 1
        if count == k:
            result = root.val
            return

        traverse(root.right)

    traverse(root)
    
    return result