# do later
def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    char_num = 0
    char2_num = 0
    counter = 1

    a_to_n = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 
    'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 
    's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

    for char in s:
        char_num += a_to_n[char] * counter
        counter *= 1000
    
    counter = 1

    for char in t:
        char2_num += a_to_n[char] * counter
        counter *= 1000

    print(char_num)
    print(char2_num)

print(isIsomorphic("egg","add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("pappeer", "tittlle"))
print(isIsomorphic("bbbaaaba", "aaabbbba"))
print(isIsomorphic("baba", "dada"))
print(isIsomorphic("badc", "baba"))