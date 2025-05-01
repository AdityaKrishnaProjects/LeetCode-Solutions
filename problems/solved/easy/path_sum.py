# recursion, uses or in return statement to allow for any of the possible sums 
# to gives us a true when we are checking for if root to leaf summation is correct
def hasPathSum(root, targetSum):
    """
    accepts root of tree and target sum of sequence of nodes
    """
    
    if root is None:
        return False

    targetSum -= root.val

    if (root.left is None) and (root.right is None):
        return targetSum == 0

    return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)