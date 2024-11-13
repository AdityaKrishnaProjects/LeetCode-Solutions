# # First implementation. Quite high O and low memory efficiency

# def isPalindrome(x):
#     """
#     accepts int
#     returns bool
#     """

#     num_list = str(x)
#     length = len(num_list)

#     for i in range(length // 2):
#         if num_list[i] != num_list[(i+1)*-1]:
#             return False

#     return True

# Ends up being about as efficient according to LeetCode
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if (x < 0) or ((x % 10) == 0 and (x != 0)):
        return False

    reverse_half = 0

    while x > reverse_half:
        reverse_half = (reverse_half*10 + (x % 10))
        x = x // 10

    return (x == reverse_half) or (x == (reverse_half // 10))