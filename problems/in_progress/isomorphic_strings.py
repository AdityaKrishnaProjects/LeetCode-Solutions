# do later
def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    char = {}
    char2 = {}
    curr_index = 0
    length = len(s)

    while curr_index < length:
        if s[curr_index] in char:
            if t[curr_index] not in char2:
                return False
            else:
                char[s[curr_index]] += 1
                char2[t[curr_index]] += 1
        if s[curr_index] in char:
            if t[curr_index] not in char2:
                return False
            else:
                char[s[curr_index]] += 1
                char2[t[curr_index]] += 1
        else:
            char[s[curr_index]] = 1
            char2[t[curr_index]] = 1
        
        curr_index += 1

    print(char)
    print(char2)

    return True

print(isIsomorphic("egg","add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("pappeer", "tittlle"))
print(isIsomorphic("bbbaaaba", "aaabbbba"))
print(isIsomorphic("baba", "dada"))
print(isIsomorphic("badc", "baba"))