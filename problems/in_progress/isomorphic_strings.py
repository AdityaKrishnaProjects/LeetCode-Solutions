# do later
def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    counter = 1
    char_to_num = {}
    inv_char_to_num = {}
    char_to_num2 = {}
    inv_char_to_num2 = {}
    length = len(s)
    curr_index = 0

    while curr_index < length:
        if s[curr_index] not in inv_char_to_num:
            char_to_num[counter] = s[curr_index]
            inv_char_to_num[s[curr_index]] = counter
            
            if t[curr_index] in inv_char_to_num2:
                return False

            char_to_num2[counter] = t[curr_index]
            inv_char_to_num2[t[curr_index]] = counter

            counter += 1

        if t[curr_index] not in inv_char_to_num2:
            char_to_num2[counter] = t[curr_index]
            inv_char_to_num2[t[curr_index]] = counter

            if s[curr_index] in inv_char_to_num:
                return False
            
            char_to_num[counter] = s[curr_index]
            inv_char_to_num[s[curr_index]] = counter

            counter += 1

        curr_index += 1

    print(char_to_num)
    print(char_to_num2)

    return True

print(isIsomorphic("egg","add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("pappeer", "tittlle"))
print(isIsomorphic("bbbaaaba", "aaabbbba"))
print(isIsomorphic("baba", "dada"))
print(isIsomorphic("badc", "baba"))