def binary_search(sorted_list, value, low=0, high=None):
    """
    Takes: sorted list, value to find, and optional low/high indices.
    Returns: index of value in the list, or -1 if not found.
    """
    if high is None:
        high = len(sorted_list) - 1

    if low > high:
        return -1  # Value not found

    m = (low + high) // 2  # Middle index

    if sorted_list[m] == value:
        return m
    elif sorted_list[m] > value:
        return binary_search(sorted_list, value, low, m - 1)
    else:
        return binary_search(sorted_list, value, m + 1, high)


# Test the function
evil_list = [137, 507, 674, 918, 1092, 1106, 1126, 1261, 1343, 1368, 1705, 2200,
 2234, 2332, 2439, 2680, 2702, 2749, 3097, 3141, 3217, 3381, 3394, 3504, 3626, 
 3630, 3825, 3826, 3842, 3897, 4009, 4069, 4263, 4840, 4841, 4874, 5047, 5071, 
 5080, 5269, 5440, 5466, 5825, 5847, 5922, 5994, 6069, 6247, 6341, 6521, 6638, 
 7018, 7076, 7756, 8416, 8420, 8545, 8910, 9039, 9109, 9185, 9212, 9652]

print(evil_list[binary_search(evil_list, 2749)])