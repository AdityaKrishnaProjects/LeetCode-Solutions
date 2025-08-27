# Flatten left and right subtree, recursive call returns tail of subtree. Attach 
# right node to tail of left subtree, make current right node start of left subtree. 
def flatten(root):

    if not root:
        return None

    def traverse(root):

        if not root:
            return None

        left_subtree = traverse(root.left)
        right_subtree = traverse(root.right)

        if left_subtree:
            left_subtree.right = root.right
            root.right = root.left
            root.left = None

        return right_subtree or left_subtree or root

    traverse(root)