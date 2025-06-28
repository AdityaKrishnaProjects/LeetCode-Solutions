# simple and works
def averageOfLevels(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[float]
    """
    
    r_list = []

    def valueAppender(root, curr_level):
        if root is None:
            return
        if len(r_list) < curr_level:
            r_list.append([])
        r_list[curr_level-1].append(root.val)

        valueAppender(root.left, curr_level+1)
        valueAppender(root.right, curr_level+1)

    valueAppender(root, 1)

    avg_vals = []

    for vals in r_list:
        avg_vals.append(sum(vals)/len(vals))

    return avg_vals