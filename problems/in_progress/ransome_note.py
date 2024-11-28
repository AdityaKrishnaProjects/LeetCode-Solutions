def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    
    rn_dict = {}
    m_dict = {}

    for i in ransomNote:
        if i not in rn_dict:
            rn_dict[i] = i
        else:
            rn_dict[i] += i

    print(rn_dict)

    return False

print(canConstruct("a", "b"))
print(canConstruct("aa", "aabb"))
print(canConstruct("ab", "bbaba"))
print(canConstruct("aa", "bbba"))
print(canConstruct("aaaaaavdw", "baaddavvsdawaa"))