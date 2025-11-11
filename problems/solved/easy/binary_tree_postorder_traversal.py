# dfs postorder
def postorderTraversal(root):

    res = []

    def search(node):
        if node is None:
            return

        search(node.left)
        search(node.right)

        res.append(node.val)

    search(root)

    return res