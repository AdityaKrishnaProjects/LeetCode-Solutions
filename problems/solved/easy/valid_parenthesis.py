# # more domain general solution (accepts random chars between parenthesese)
# def isValid(s):
#     """
#     :type s: str
#     :rtype: bool
#     """

#     stack = []
#     par_dict = {"[":"]", "{":"}", "(":")"}
#     left_par = ["[", "{", "("]
#     right_par = ["]", "}", ")"]

#     for char in s:
#         if char in left_par:
#             stack.append(char)
#             continue

#         N = len(stack)

#         if N == 0:
#             if char in right_par:
#                 return False
#             else:
#                 continue

#         if char in right_par:
#             if char != par_dict[stack[N-1]]:
#                 return False
#             else: 
#                 stack.pop()

#     return not stack

# print(isValid("()"))
# print(isValid("()[]{}"))
# print(isValid("(]"))
# print(isValid("()"))
# print(isValid("([])"))
# print(isValid("(["))
# print(isValid("(adwqdwqe[qweqweqwe]wee)"))
# print(isValid("(adwqdwqe[qweqweqwe{wee)"))
# print(isValid("}}"))

# more domain general and cleaner than the above
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    par_dict = {"[":"]", "{":"}", "(":")"}
    left_par = ["[", "{", "("]
    right_par = ["]", "}", ")"]

    for char in s:
        if char in left_par:
            stack.append(char)
            continue

        N = len(stack)

        if char in right_par:
            if N == 0:
                return False
            if char != par_dict[stack[N-1]]:
                return False
            else: 
                stack.pop()

    return not stack