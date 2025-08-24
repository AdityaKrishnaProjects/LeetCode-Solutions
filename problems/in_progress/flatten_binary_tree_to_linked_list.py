def flatten(root):

    if root is None:
        return root

    res = TreeNode(root.val)

    def traverse(root, curr):

        if root is None:
            return

        curr.right = TreeNode(root.val)

        traverse(root.left, curr.right)

        traverse(root.right, curr.right)