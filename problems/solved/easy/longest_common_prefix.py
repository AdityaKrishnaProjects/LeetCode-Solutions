# Could be cleaner if I used startswith
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    str_len = len(strs[0])
    str_len_decided = False
    curr_index = 0
    strs_len = len(strs)
    r_str = ""

    while curr_index < str_len:
        for curr_string in range(1, strs_len):
            if not str_len_decided:
                str_len = min(str_len, len(strs[curr_string]))
                if str_len == 0:
                    return r_str
            if strs[curr_string-1][curr_index] != strs[curr_string][curr_index]:
                return r_str
        
        print(str_len)

        r_str += strs[0][curr_index]
        str_len_decided = True
        curr_index += 1

    return r_str

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["flower","flow","flowing"]))
print(longestCommonPrefix(["abbb","a","accc","aa"]))
print(longestCommonPrefix(["tdaw","sfea","ehrwqwd"]))