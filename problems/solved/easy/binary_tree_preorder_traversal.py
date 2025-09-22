# preorder traversal of tree
def preordertraversal(root):
    
    res = []

    if root is None:
        return res

    def traverse(node):
        if node is not None:
            res.append(node.val)
            traverse(node.left)
            traverse(node.right)

    traverse(root)

    return res