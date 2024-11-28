# Feel okay about this solution. m+n time m space
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    
    rn_dict = {}
    m_dict = {}

    for i in magazine:
        if i not in m_dict:
            m_dict[i] = 1
        else:
            m_dict[i] += 1

    for j in ransomNote:
        if j not in m_dict:
            return False
        else:
            m_dict[j] -= 1
            if m_dict[j] < 0:
                return False
    
    return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "abb"))
print(canConstruct("ab", "bbaba"))
print(canConstruct("aa", "bbba"))
print(canConstruct("aaaaaavdw", "baaddavvsdawaa"))