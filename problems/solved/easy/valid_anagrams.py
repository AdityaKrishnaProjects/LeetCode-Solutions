# solution is lowkey garbage but whatever
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    s_dict = {}
    s_len = len(s)
    t_len = len(t)
    curr_index = 0

    if s_len != t_len:
        return False

    for char in s:
        if char not in s_dict:
            s_dict[char] = 1
        else:
            s_dict[char] += 1

    for char in t:
        if char not in s_dict:
            return False
        else:
            s_dict[char] -= 1
            if s_dict[char] < 0:
                return False

    return True

    
print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("anagram", "naga"))
print(isAnagram("anagram", "nagaramsilly"))