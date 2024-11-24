# pretty happy with this one, could be made better if dynamically check for 
# potential start indices while iterating through haystack (so if needle check 
# fails) can revert check index to next possible needle start rather than next 
# index in haystack
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    
    needle_index = 0
    needle_length = len(needle)-1
    haystack_length = len(haystack)
    i = 0
    
    while i < haystack_length:
        if haystack[i] == needle[needle_index]:
            if needle_index == needle_length:
                return i - needle_length
            needle_index += 1
        else:
            i -= needle_index
            needle_index = 0
        
        i += 1

    return -1

print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "sad"))
print(strStr("leetcode", "leeto"))
print(strStr("sbut sad", "sad"))
print(strStr("mississipi", "issip"))