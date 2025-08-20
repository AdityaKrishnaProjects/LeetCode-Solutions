# depth first search
def inorderTraversal(root):
    res = []

    def dfs(root):
        if root is not None:
            dfs(root.left)

            res.append(root.val)

            dfs(root.right)
        
    dfs(root)

    return res

