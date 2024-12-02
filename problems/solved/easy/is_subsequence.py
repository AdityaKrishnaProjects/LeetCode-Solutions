# seems fine. O(n) uses a pointer approach
def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    len_sub = len(s)
    len_string = len(t)
    curr_index = 0
    key_index = 0

    if not s:
        return True

    while curr_index < len_string:
        if s[key_index] == t[curr_index]:
            key_index += 1
        curr_index += 1
        if key_index == len_sub:
            return True

    return False

print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("aaaa", "ahbgdc"))